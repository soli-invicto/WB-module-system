# Vanilla Module System v1.171

This is a Mount & Blade module system directory containing Python scripts for game modding.

## Overview

The Mount & Blade Module System allows you to create custom modifications (mods) for the Mount & Blade game by defining game content through Python scripts.

## Directory Structure

### ID Files (`ID_*.py`)
Contains identifier definitions for various game elements:
- `ID_animations.py` - Animation definitions
- `ID_factions.py` - Faction identifiers
- `ID_items.py` - Item definitions
- `ID_meshes.py` - 3D mesh references
- `ID_scenes.py` - Scene locations
- `ID_scripts.py` - Script identifiers
- `ID_strings.py` - String table entries
- `ID_troops.py` - Character/troop definitions
- And more...

### Header Files (`header_*.py`)
Contains constants, flags, and helper functions:
- `header_common.py` - Common constants and utilities
- `header_items.py` - Item-related constants
- `header_mission_templates.py` - Mission template definitions
- `header_operations.py` - Script operations reference
- `header_triggers.py` - Trigger conditions and effects
- And more...

### Module Files (`module_*.py`)
Main configuration files where you define your mod's content:
- `module_items.py` - Define custom items
- `module_troops.py` - Create characters and troops
- `module_factions.py` - Set up factions
- `module_scenes.py` - Configure scenes
- `module_mission_templates.py` - Design mission templates
- `module_scripts.py` - Write game logic scripts
- `module_game_menus.py` - Create dialogue and menus
- `module_triggers.py` - Set up event triggers
- And more...

### Process Files (`process_*.py`)
Build system files that compile module definitions into game data. **Do not modify these files.**

## Quick Start

1. **Edit module files** - Customize your mod by editing the appropriate `module_*.py` files
2. **Run build script** - Execute `build_module.bat` (Windows) to compile your module
3. **Test in game** - Launch Mount & Blade with your mod

## Important Files

- `module_info.py` - Module metadata (name, version, etc.)
- `build_module.bat` - Windows build script to compile the module
- `variables.txt` - Global variable documentation

## Resources

- Official documentation: [www.taleworlds.com/mb_module_system.html](http://www.taleworlds.com/mb_module_system.html)
- Community forums: TaleWorlds Entertainment forums

## Notes

- This is version 1.171 of the module system
- Compatible with Mount & Blade (Warband)
- Python 2.x required for building modules
- Always backup your module files before making changes

## License

Refer to the original Mount & Blade license terms for modding guidelines.
