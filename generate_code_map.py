#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Warband Code Map Generator

Analyzes header_*.py and module_*.py files to extract constants, data structures, and usage patterns.

Usage:
    python generate_code_map.py [--dir /path/to/module/system]
    
Environment:
    WARBAND_DIR: Override the module system directory (default: current directory)
"""

import os
import re
import ast
import sys
import logging
from pathlib import Path
from collections import defaultdict
from typing import List, Tuple, Dict, Optional, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Get base directory from environment or CLI argument, default to current directory
BASE_DIR = Path(os.getenv("WARBAND_DIR", "."))
if len(sys.argv) > 1 and sys.argv[1] == "--dir" and len(sys.argv) > 2:
    BASE_DIR = Path(sys.argv[2])


def validate_base_dir() -> bool:
    """Validate that BASE_DIR exists and is accessible."""
    if not BASE_DIR.exists():
        logger.error(f"Directory not found: {BASE_DIR}")
        return False
    if not BASE_DIR.is_dir():
        logger.error(f"Path is not a directory: {BASE_DIR}")
        return False
    return True


def extract_constants_from_header(filepath: Path) -> List[Tuple[str, str]]:
    """
    Extract constant definitions from a header file using AST parsing.
    
    This is more reliable than regex as it handles multi-line assignments
    and correctly ignores comments on the same line as code.
    
    Args:
        filepath: Path to the header file
        
    Returns:
        List of (name, value) tuples
    """
    constants = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
    except (SyntaxError, UnicodeDecodeError) as e:
        logger.warning(f"Failed to parse {filepath.name}: {e}")
        return constants
    
    # Extract module-level assignments
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    try:
                        # Use ast.unparse if available (Python 3.9+), otherwise fallback
                        if hasattr(ast, 'unparse'):
                            value_str = ast.unparse(node.value)
                        else:
                            value_str = ast.literal_eval(node.value) if isinstance(
                                node.value, (ast.Constant, ast.List, ast.Dict)
                            ) else str(node.value)
                        
                        # Truncate very long values for readability
                        value_str = str(value_str)[:100]
                        constants.append((target.id, value_str))
                    except (ValueError, AttributeError) as e:
                        logger.debug(f"Could not unparse value in {filepath.name}: {e}")
                        continue
    
    return constants


def extract_main_array_structure(
    filepath: Path,
    array_name: Optional[str] = None
) -> Optional[Dict]:
    """
    Extract the structure of the main array from a module file.
    
    Args:
        filepath: Path to the module file
        array_name: Name of the array to analyze (auto-detected if None)
        
    Returns:
        Dictionary with array_name, element_count, and structure, or None if not found
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except (IOError, OSError) as e:
        logger.warning(f"Could not read {filepath.name}: {e}")
        return None
    
    # Auto-detect array name if not provided
    if array_name is None:
        match = re.search(r'^(\w+)\s*=\s*\[', content, re.MULTILINE)
        if not match:
            return None
        array_name = match.group(1)
    
    # Find the array definition with boundary check for regex
    pattern = r'^' + re.escape(array_name) + r'\s*=\s*\['
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return None
    
    # Try AST-based parsing first (most reliable)
    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == array_name:
                        if isinstance(node.value, (ast.List, ast.Tuple)):
                            if len(node.value.elts) > 0:
                                first_element = node.value.elts[0]
                                return analyze_tuple_structure(first_element, array_name)
    except (SyntaxError, ValueError):
        pass  # Fall back to regex approach
    
    # Fallback: regex-based extraction for the first element
    try:
        array_match = re.search(
            r'^' + re.escape(array_name) + r'\s*=\s*\[(.+?)\],',
            content,
            re.DOTALL | re.MULTILINE
        )
        if array_match:
            first_elem_str = array_match.group(1).strip()
            return count_top_level_elements(first_elem_str, array_name)
    except (ValueError, IndexError) as e:
        logger.debug(f"Regex fallback failed for {filepath.name}: {e}")
    
    return None


def count_top_level_elements(elem_str: str, array_name: str) -> Dict:
    """
    Count top-level elements in a tuple string by tracking bracket depth.
    
    Args:
        elem_str: String representation of a tuple
        array_name: Name of the array for context
        
    Returns:
        Dictionary with element count and sample structure
    """
    elem_str = elem_str.strip()
    elements = []
    depth = 0
    current = ""
    
    for char in elem_str:
        if char in '([{':
            depth += 1
            current += char
        elif char in ')]}':
            depth -= 1
            current += char
        elif char == ',' and depth == 0:
            if current.strip():
                elements.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        elements.append(current.strip())
    
    return {
        'array_name': array_name,
        'element_count': len(elements),
        'structure': elements[:5]  # First five elements as sample
    }


def analyze_tuple_structure(node: ast.expr, array_name: str) -> Dict:
    """
    Analyze an AST node representing a tuple/list and describe its structure.
    
    Args:
        node: AST node to analyze
        array_name: Name of the parent array
        
    Returns:
        Dictionary describing the structure, or None if not a tuple/list
    """
    if not isinstance(node, (ast.Tuple, ast.List)):
        return None
    
    elements = []
    for elt in node.elts:
        if isinstance(elt, ast.Constant):
            # Handle constant values
            val = str(elt.value)[:50]
            elements.append(f"const:{val}")
        elif isinstance(elt, ast.Name):
            elements.append(f"var:{elt.id}")
        elif isinstance(elt, ast.Call):
            func_name = _get_func_name(elt.func)
            elements.append(f"call:{func_name}(...)")
        elif isinstance(elt, (ast.List, ast.Tuple)):
            elements.append(f"nested[{len(elt.elts)}]")
        elif isinstance(elt, ast.BinOp):
            elements.append(f"expr:{type(elt.op).__name__}")
        else:
            elements.append(type(elt).__name__)
    
    return {
        'array_name': array_name,
        'element_count': len(node.elts),
        'structure': elements
    }


def _get_func_name(node: ast.expr) -> str:
    """Extract function name from an AST call node."""
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return node.attr
    return "unknown"


def extract_global_variables(filepath: Path) -> Set[str]:
    """
    Extract global variable references (those prefixed with $).
    
    Args:
        filepath: Path to the file to analyze
        
    Returns:
        Set of global variable names found
    """
    globals_used = set()
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except (IOError, OSError) as e:
        logger.warning(f"Could not read {filepath.name}: {e}")
        return globals_used
    
    # Pattern for $variable (Warband global variables)
    # Must start with letter or underscore, followed by alphanumerics or underscores
    dollar_vars = re.findall(r'\$([a-zA-Z_][a-zA-Z0-9_]*)', content)
    globals_used.update(dollar_vars)
    
    return globals_used


def extract_register_usage(filepath: Path) -> Dict[str, int]:
    """
    Extract register usage patterns from a file.
    
    Tracks:
    - :reg(N) patterns
    - s0-s15 string registers
    - pos_0, pos_1, etc. position registers
    
    Args:
        filepath: Path to the file to analyze
        
    Returns:
        Dictionary mapping register names to usage counts
    """
    registers = defaultdict(int)
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except (IOError, OSError) as e:
        logger.warning(f"Could not read {filepath.name}: {e}")
        return dict(registers)
    
    # :reg(X) pattern - registers accessed via function
    reg_matches = re.findall(r':reg\((\d+)\)', content)
    for m in reg_matches:
        registers[f'reg{m}'] += 1
    
    # s0-s999 pattern (string registers) - but limit to realistic s0-s15 range
    # Use word boundaries to avoid false positives
    sreg_matches = re.findall(r'\b(s(?:1[0-5]|[0-9]))\b', content)
    for m in sreg_matches:
        registers[m] += 1
    
    # pos_0, pos_1, etc. (position registers)
    pos_matches = re.findall(r'\b(pos_\d+)\b', content)
    for m in pos_matches:
        registers[m] += 1
    
    return dict(registers)


def get_module_files() -> Tuple[List[Path], List[Path]]:
    """
    Get lists of header and module files from BASE_DIR.
    
    Returns:
        Tuple of (header_files, module_files) sorted by filename
    """
    if not validate_base_dir():
        logger.error("Cannot proceed without valid BASE_DIR")
        return [], []
    
    header_files = []
    module_files = []
    
    try:
        for filepath in BASE_DIR.iterdir():
            if filepath.is_file() and filepath.suffix == '.py':
                if filepath.stem.startswith('header_'):
                    header_files.append(filepath)
                elif filepath.stem.startswith('module_'):
                    module_files.append(filepath)
    except (IOError, OSError) as e:
        logger.error(f"Failed to list files in {BASE_DIR}: {e}")
        return [], []
    
    return sorted(header_files), sorted(module_files)


def generate_code_map(output_file: Optional[Path] = None) -> Optional[Path]:
    """
    Generate the complete code map documentation.
    
    Args:
        output_file: Path to write the output file. If None, defaults to
                     BASE_DIR/warband-code-map.md
                     
    Returns:
        Path to the generated file, or None if generation failed
    """
    header_files, module_files = get_module_files()
    
    if not header_files and not module_files:
        logger.error("No header_*.py or module_*.py files found")
        return None
    
    logger.info(f"Found {len(header_files)} header files and {len(module_files)} module files")
    
    output = []
    output.append("# 🗺️ WARBRAND CODE MAP\n")
    output.append("Auto-generated analysis of Warband Module System\n")
    output.append("=" * 60 + "\n\n")
    
    # Section 1: Constants from header files
    output.append("## 1. КОНСТАНТЫ И ФЛАГИ\n")
    
    for header_file in header_files:
        output.append(f"### {header_file.name}\n")
        constants = extract_constants_from_header(header_file)
        
        if constants:
            output.append("| Константа | Значение |")
            output.append("|-----------|----------|")
            for name, value in constants:
                # Escape pipe characters in values
                value = value.replace('|', '\\|')
                output.append(f"| {name} | {value} |")
            output.append("")
        else:
            output.append("*Нет констант*\n")
    
    # Section 2: Data Structures from module files
    output.append("\n## 2. СТРУКТУРА ДАННЫХ (TUPLES)\n")
    
    for module_file in module_files:
        output.append(f"### {module_file.name}\n")
        structure = extract_main_array_structure(module_file)
        
        if structure:
            output.append(f"- **Имя массива:** `{structure['array_name']}`")
            output.append(f"- **Количество элементов в кортеже:** {structure['element_count']}")
            output.append("- **Структура первого элемента:**")
            output.append("  ```")
            for i, elem in enumerate(structure['structure']):
                # Escape backticks in elements
                elem = elem.replace('`', '\\`')
                output.append(f"  [{i}] {elem}")
            output.append("  ```\n")
        else:
            output.append("*Не удалось определить структуру*\n")
    
    # Section 3: Global Variables Registry
    output.append("\n## 3. РЕЕСТР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ\n")
    
    all_globals: Set[str] = set()
    key_files = [
        BASE_DIR / 'module_scripts.py',
        BASE_DIR / 'module_triggers.py',
        BASE_DIR / 'module_variables.py'
    ]
    
    for filepath in key_files:
        if filepath.exists():
            globals_found = extract_global_variables(filepath)
            all_globals.update(globals_found)
            logger.debug(f"Found {len(globals_found)} globals in {filepath.name}")
    
    if all_globals:
        output.append("### Использованные глобальные переменные ($var):\n")
        for var in sorted(all_globals):
            output.append(f"- `${var}`")
        output.append("")
    else:
        output.append("*Глобальные переменные не обнаружены в стандартном формате*\n")
    
    # Section 4: Register Usage
    output.append("\n## 4. РЕЕСТР ЛОКАЛЬНЫХ РЕГИСТРОВ И СТРОК\n")
    
    all_registers = defaultdict(int)
    key_files = [
        'module_scripts.py',
        'module_triggers.py',
        'module_game_menus.py',
        'module_mission_templates.py',
        'module_dialogs.py'
    ]
    
    for filename in key_files:
        filepath = BASE_DIR / filename
        if filepath.exists():
            regs = extract_register_usage(filepath)
            for reg, count in regs.items():
                all_registers[reg] += count
            logger.debug(f"Found {len(regs)} register types in {filename}")
    
    if all_registers:
        output.append("### Паттерны использования регистров:\n")
        output.append("| Регистр | Количество использований |")
        output.append("|---------|-------------------------|")
        
        sorted_regs = sorted(all_registers.items(), key=lambda x: x[1], reverse=True)
        for reg, count in sorted_regs[:50]:  # Top 50
            output.append(f"| {reg} | {count} |")
        output.append("")
    else:
        output.append("*Регистры не обнаружены*\n")
    
    # Write output file
    if output_file is None:
        output_file = BASE_DIR / 'warband-code-map.md'
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output))
        logger.info(f"Code map generated: {output_file}")
        return output_file
    except (IOError, OSError) as e:
        logger.error(f"Failed to write output file: {e}")
        return None


if __name__ == '__main__':
    output_path = generate_code_map()
    if output_path is None:
        sys.exit(1)
