#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Warband Code Map Generator

Analyzes header_*.py, ID_*.py, module_*.py, and process_*.py files 
to extract constants, data structures, and usage patterns.

Usage:
    python generate_code_map.py [--dir /path/to/module/system]
    
Environment:
    WARBAND_DIR: Override the module system directory (default: ./Vanilla Module System v1.171)
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

# Get base directory from environment or CLI argument
DEFAULT_DIR = Path("./Vanilla Module System v1.171")
BASE_DIR = Path(os.getenv("WARBAND_DIR", str(DEFAULT_DIR)))
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
    Extract constant definitions from a header/ID file using regex to preserve original format.
    
    Args:
        filepath: Path to the header file
        
    Returns:
        List of (name, value) tuples
    """
    constants = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, IOError) as e:
        logger.warning(f"Failed to read {filepath.name}: {e}")
        return constants
    
    # Pattern to match variable assignments: name = value
    # Captures the original format including hex notation (0x...)
    pattern = r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+?)\s*$'
    
    for line in content.split('\n'):
        line = line.strip()
        # Skip comments and empty lines
        if not line or line.startswith('#'):
            continue
        
        match = re.match(pattern, line)
        if match:
            name = match.group(1)
            value = match.group(2).strip()
            # Remove trailing comments if any
            if '#' in value:
                value = value.split('#')[0].strip()
            constants.append((name, value))
    
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
        Dictionary with array_name, element_count, and structure
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
    
    # Find the array definition
    pattern = r'^' + re.escape(array_name) + r'\s*=\s*\['
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return None
    
    # Try AST-based parsing first
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
        pass
    
    # Fallback: regex-based extraction
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
        'structure': elements[:5]
    }


def analyze_tuple_structure(node: ast.expr, array_name: str) -> Dict:
    """
    Analyze an AST node representing a tuple/list and describe its structure.
    
    Args:
        node: AST node to analyze
        array_name: Name of the parent array
        
    Returns:
        Dictionary describing the structure
    """
    if not isinstance(node, (ast.Tuple, ast.List)):
        return None
    
    elements = []
    for elt in node.elts:
        if isinstance(elt, ast.Constant):
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
    dollar_vars = re.findall(r'\$([a-zA-Z_][a-zA-Z0-9_]*)', content)
    globals_used.update(dollar_vars)
    
    return globals_used


def extract_register_usage(filepath: Path) -> Dict[str, int]:
    """
    Extract register usage patterns from a file.
    
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
    
    # :reg(X) pattern
    reg_matches = re.findall(r':reg\((\d+)\)', content)
    for m in reg_matches:
        registers[f'reg{m}'] += 1
    
    # s0-s15 string registers
    sreg_matches = re.findall(r'\b(s(?:1[0-5]|[0-9]))\b', content)
    for m in sreg_matches:
        registers[m] += 1
    
    # pos_0, pos_1, etc. (position registers)
    pos_matches = re.findall(r'\b(pos_\d+)\b', content)
    for m in pos_matches:
        registers[m] += 1
    
    return dict(registers)


def get_module_files() -> Tuple[List[Path], List[Path], List[Path]]:
    """
    Get lists of files from BASE_DIR.
    Looks for header_*.py, ID_*.py files (constants) and module_*.py files (data structures).
    
    Returns:
        Tuple of (constant_files, module_files, process_files) sorted by filename
    """
    if not validate_base_dir():
        logger.error("Cannot proceed without valid BASE_DIR")
        return [], [], []
    
    constant_files = []
    module_files = []
    process_files = []
    
    try:
        for filepath in BASE_DIR.iterdir():
            if filepath.is_file() and filepath.suffix == '.py':
                stem = filepath.stem
                # Constants/ID files
                if stem.startswith('header_') or stem.startswith('ID_'):
                    constant_files.append(filepath)
                # Data structure files
                elif stem.startswith('module_'):
                    module_files.append(filepath)
                # Process files
                elif stem.startswith('process_'):
                    process_files.append(filepath)
    except (IOError, OSError) as e:
        logger.error(f"Failed to list files in {BASE_DIR}: {e}")
        return [], [], []
    
    return sorted(constant_files), sorted(module_files), sorted(process_files)


def generate_code_map(output_file: Optional[Path] = None) -> Optional[Path]:
    """
    Generate the complete code map documentation.
    
    Args:
        output_file: Path to write the output file
                     
    Returns:
        Path to the generated file, or None if generation failed
    """
    const_files, module_files, process_files = get_module_files()
    
    if not const_files and not module_files:
        logger.error("No header_*.py, ID_*.py or module_*.py files found")
        return None
    
    logger.info(f"Found {len(const_files)} constant files, {len(module_files)} module files, {len(process_files)} process files")
    
    output = []
    output.append("# 🗺️ WARBRAND CODE MAP\n")
    output.append("Auto-generated analysis of Warband Module System v1.171\n")
    output.append("=" * 60 + "\n\n")
    
    # Section 1: Constants from header/ID files
    output.append("## 1. КОНСТАНТЫ И ИДЕНТИФИКАТОРЫ\n")
    
    for const_file in const_files:
        output.append(f"### {const_file.name}\n")
        constants = extract_constants_from_header(const_file)
        
        if constants:
            output.append("| Константа | Значение |")
            output.append("|-----------|----------|")
            for name, value in constants:
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
            for i, elem in enumerate(structure['structure'][:10]):
                elem = elem.replace('`', '\\`')
                output.append(f"  [{i}] {elem}")
            if len(structure['structure']) > 10:
                output.append(f"  ... ({len(structure['structure']) - 10} more elements)")
            output.append("  ```\n")
        else:
            output.append("*Не удалось определить структуру*\n")
    
    # Section 3: Global Variables Registry
    output.append("\n## 3. РЕЕСТР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ\n")
    
    all_globals: Set[str] = set()
    key_files = [
        BASE_DIR / 'module_scripts.py',
        BASE_DIR / 'module_triggers.py',
        BASE_DIR / 'module_simple_triggers.py',
    ]
    
    for filepath in key_files:
        if filepath.exists():
            globals_found = extract_global_variables(filepath)
            all_globals.update(globals_found)
            logger.debug(f"Found {len(globals_found)} globals in {filepath.name}")
    
    if all_globals:
        output.append("### Использованные глобальные переменные ($var):\n")
        sorted_globals = sorted(all_globals)
        for i, var in enumerate(sorted_globals, 1):
            output.append(f"- `${var}`")
        output.append(f"\n**Всего уникальных глобальных переменных:** {len(all_globals)}\n")
    else:
        output.append("*Глобальные переменные не обнаружены*\n")
    
    # Section 4: Register Usage
    output.append("\n## 4. РЕЕСТР ЛОКАЛЬНЫХ РЕГИСТРОВ И СТРОК\n")
    
    all_registers = defaultdict(int)
    key_files = [
        'module_scripts.py',
        'module_triggers.py',
        'module_simple_triggers.py',
        'module_game_menus.py',
        'module_mission_templates.py',
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
        for reg, count in sorted_regs[:50]:
            output.append(f"| {reg} | {count} |")
        output.append("")
        
        if len(sorted_regs) > 50:
            output.append(f"\n*Всего типов регистров: {len(sorted_regs)}*\n")
    else:
        output.append("*Регистры не обнаружены*\n")
    
    # Add generation info
    output.append("\n---\n")
    output.append(f"**Сгенерировано:** {len(const_files)} файлов констант, {len(module_files)} файлов данных, {len(process_files)} файлов обработки\n")
    output.append(f"**Базовая директория:** `{BASE_DIR}`\n")
    
    # Write output file
    if output_file is None:
        output_file = Path('.') / 'warband-code-map.md'
    
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
    print(f"✓ Code map saved to: {output_path}")
