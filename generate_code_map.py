#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Warband Code Map Generator
Analyzes header_*.py and module_*.py files to extract constants, data structures, and usage patterns.
"""

import os
import re
import ast
from collections import defaultdict

BASE_DIR = "/workspace/Vanilla Module System v1.171"

def extract_constants_from_header(filepath):
    """Extract all constant definitions from a header file."""
    constants = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all assignments at module level (simple pattern)
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        # Skip comments and imports
        if line.startswith('#') or line.startswith('from ') or line.startswith('import '):
            continue
        # Match variable = value patterns
        match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)$', line)
        if match:
            name = match.group(1)
            value = match.group(2).strip()
            # Skip function definitions
            if not value.startswith('def ') and not value.startswith('lambda'):
                constants.append((name, value))
    
    return constants

def extract_main_array_structure(filepath, array_name=None):
    """Extract the structure of the main array from a module file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Try to find common array names if not specified
    if array_name is None:
        # Look for common patterns like "items = [", "troops = [", etc.
        match = re.search(r'^(\w+)\s*=\s*\[', content, re.MULTILINE)
        if match:
            array_name = match.group(1)
        else:
            return None
    
    # Find the array definition
    pattern = rf'^{array_name}\s*=\s*\['
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return None
    
    start_pos = match.start()
    
    # Find the first element by counting brackets
    bracket_count = 0
    first_element_start = None
    first_element_end = None
    
    for i in range(start_pos, len(content)):
        if content[i] == '[':
            if bracket_count == 1 and first_element_start is None:
                first_element_start = i + 1
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 1 and first_element_start is not None:
                # We're closing the outer array, so find where first element ends
                # Need to find the matching closing bracket for first element
                pass
            elif bracket_count == 0:
                break
    
    # Better approach: use AST to parse the first element
    try:
        # Find the array assignment and parse just the first element
        array_match = re.search(rf'{array_name}\s*=\s*\[(.+?)\],', content, re.DOTALL)
        if array_match:
            first_elem_str = array_match.group(1).strip()
            # Remove leading/trailing whitespace and newlines
            first_elem_str = first_elem_str.strip()
            
            # Try to parse as AST
            try:
                tree = ast.parse(f'[{first_elem_str}]', mode='eval')
                if isinstance(tree.body, ast.List) and len(tree.body.elts) > 0:
                    first_element = tree.body.elts[0]
                    return analyze_tuple_structure(first_element, array_name)
            except:
                pass
            
            # Fallback: count commas at top level
            return count_top_level_elements(first_elem_str, array_name)
    except Exception as e:
        pass
    
    return None

def count_top_level_elements(elem_str, array_name):
    """Count top-level elements in a tuple string."""
    # Clean up the string
    elem_str = elem_str.strip()
    
    # Count elements by tracking bracket depth
    elements = []
    depth = 0
    current = ""
    
    for char in elem_str:
        if char in '([{':
            depth += 1
            current += char
        elif char in '])]':
            depth -= 1
            current += char
        elif char == ',' and depth == 0:
            elements.append(current.strip())
            current = ""
        else:
            current += char
    
    if current.strip():
        elements.append(current.strip())
    
    return {
        'array_name': array_name,
        'element_count': len(elements),
        'structure': elements[:5]  # First few elements as sample
    }

def analyze_tuple_structure(node, array_name):
    """Analyze an AST node representing a tuple/list."""
    if isinstance(node, ast.Tuple) or isinstance(node, ast.List):
        elements = []
        for elt in node.elts:
            if isinstance(elt, ast.Constant):
                elements.append(str(elt.value)[:50])  # Truncate long strings
            elif isinstance(elt, ast.Name):
                elements.append(f"var:{elt.id}")
            elif isinstance(elt, ast.Call):
                if hasattr(elt.func, 'id'):
                    elements.append(f"call:{elt.func.id}(...)")
                else:
                    elements.append("call:...")
            elif isinstance(elt, ast.List) or isinstance(elt, ast.Tuple):
                elements.append(f"nested[{len(elt.elts)}]")
            else:
                elements.append(type(elt).__name__)
        
        return {
            'array_name': array_name,
            'element_count': len(node.elts),
            'structure': elements
        }
    return None

def extract_global_variables(filepath):
    """Extract global variable references from scripts and triggers."""
    globals_used = set()
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Look for global variable patterns
    # In Warband module system, globals are often referenced as "$variable" or just variable names
    # Also look for reg usage
    
    # Pattern for $variable (global vars in module_scripts)
    dollar_vars = re.findall(r'\$([a-zA-Z_][a-zA-Z0-9_]*)', content)
    globals_used.update(dollar_vars)
    
    return globals_used

def extract_register_usage(filepath):
    """Extract register usage patterns."""
    registers = defaultdict(int)
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # :reg(X) pattern
    reg_matches = re.findall(r':reg\((\d+)\)', content)
    for m in reg_matches:
        registers[f'reg{m}'] += 1
    
    # s0-s15 pattern (string registers)
    sreg_matches = re.findall(r'\b(s\d+)\b', content)
    for m in sreg_matches:
        registers[m] += 1
    
    # pos_0, pos_1, etc.
    pos_matches = re.findall(r'\b(pos_\d+)\b', content)
    for m in pos_matches:
        registers[m] += 1
    
    return dict(registers)

def get_module_files():
    """Get list of header and module files."""
    header_files = []
    module_files = []
    
    for filename in os.listdir(BASE_DIR):
        filepath = os.path.join(BASE_DIR, filename)
        if filename.startswith('header_') and filename.endswith('.py'):
            header_files.append(filepath)
        elif filename.startswith('module_') and filename.endswith('.py'):
            module_files.append(filepath)
    
    return sorted(header_files), sorted(module_files)

def generate_code_map():
    """Generate the complete code map."""
    header_files, module_files = get_module_files()
    
    output = []
    output.append("# 🗺️ WARBRAND CODE MAP\n")
    output.append("Auto-generated analysis of Warband Module System v1.171\n")
    output.append("=" * 60 + "\n\n")
    
    # Section 1: Constants from header files
    output.append("## 1. КОНСТАНТЫ И ФЛАГИ\n")
    
    for header_file in header_files:
        filename = os.path.basename(header_file)
        output.append(f"### {filename}\n")
        
        constants = extract_constants_from_header(header_file)
        
        if constants:
            output.append("| Константа | Значение |")
            output.append("|-----------|----------|")
            for name, value in constants:
                # Truncate very long values
                if len(value) > 60:
                    value = value[:57] + "..."
                output.append(f"| {name} | {value} |")
            output.append("")
        else:
            output.append("*Нет констант*\n")
    
    # Section 2: Data Structures from module files
    output.append("\n## 2. СТРУКТУРА ДАННЫХ (TUPLES)\n")
    
    for module_file in module_files:
        filename = os.path.basename(module_file)
        output.append(f"### {filename}\n")
        
        structure = extract_main_array_structure(module_file)
        
        if structure:
            output.append(f"- **Имя массива:** `{structure['array_name']}`")
            output.append(f"- **Количество элементов в кортеже:** {structure['element_count']}")
            output.append("- **Структура первого элемента:**")
            output.append("  ```python")
            for i, elem in enumerate(structure['structure']):
                output.append(f"  [{i}] {elem}")
            output.append("  ```\n")
        else:
            output.append("*Не удалось определить структуру*\n")
    
    # Section 3: Global Variables Registry
    output.append("\n## 3. РЕЕСТР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ\n")
    
    all_globals = set()
    scripts_path = os.path.join(BASE_DIR, 'module_scripts.py')
    triggers_path = os.path.join(BASE_DIR, 'module_triggers.py')
    variables_path = os.path.join(BASE_DIR, 'module_variables.py')
    
    for filepath in [scripts_path, triggers_path, variables_path]:
        if os.path.exists(filepath):
            globals_found = extract_global_variables(filepath)
            all_globals.update(globals_found)
    
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
    
    # Check key module files for register usage
    key_files = ['module_scripts.py', 'module_triggers.py', 'module_game_menus.py', 
                 'module_mission_templates.py', 'module_dialogs.py']
    
    for filename in key_files:
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            regs = extract_register_usage(filepath)
            for reg, count in regs.items():
                all_registers[reg] += count
    
    if all_registers:
        output.append("### Паттерны использования регистров:\n")
        output.append("| Регистр | Количество использований |")
        output.append("|---------|-------------------------|")
        
        # Sort by usage count
        sorted_regs = sorted(all_registers.items(), key=lambda x: x[1], reverse=True)
        for reg, count in sorted_regs[:50]:  # Top 50
            output.append(f"| {reg} | {count} |")
        output.append("")
    else:
        output.append("*Регистры не обнаружены*\n")
    
    # Write output file
    output_path = os.path.join(BASE_DIR, 'warband-code-map.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    print(f"Code map generated: {output_path}")
    return output_path

if __name__ == '__main__':
    generate_code_map()
