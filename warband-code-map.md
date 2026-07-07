# 🗺️ WARBRAND CODE MAP

Auto-generated analysis of Warband Module System v1.171
============================================================

## 1. КОНСТАНТЫ И ИДЕНТИФИКАТОРЫ

### header_animations.py
| Константа | Значение |
|-----------|----------|
| arf_blend_in_0 | 0x00000001 |
| arf_blend_in_1 | 0x00000002 |
| arf_cyclic | 0x10000000 |
| arf_use_walk_progress | 0x20000000 |
| arf_make_walk_sound | 0x00000100 |
| ... | (more constants) |

### header_common.py
| Константа | Значение |
|-----------|----------|
| multiplayer_event_set_item_selection | 0 |
| multiplayer_event_set_bot_selection | 1 |
| s0 | 0 |
| reg0 | opmask_register\|0 |
| ... | (many more) |

### header_dialogs.py
| Константа | Значение |
|-----------|----------|
| speaker_pos | 0 |
| ipt_token_pos | 1 |
| anyone | 0x00000fff |
| plyr | 0x00010000 |

### header_factions.py
| Константа | Значение |
|-----------|----------|
| ff_always_hide_label | 0x00000001 |
| ff_max_rating_bits | 8 |

### header_game_menus.py
| Константа | Значение |
|-----------|----------|
| mnf_join_battle | 0x00000001 |
| mnf_auto_enter | 0x00000010 |

### header_ground_types.py
| Константа | Значение |
|-----------|----------|
| ground_gray_stone | 0 |
| ground_brown_stone | 1 |
| ground_turf | 2 |

### header_item_modifiers.py
| Константа | Значение |
|-----------|----------|
| imod_plain | 0 |
| imod_cracked | 1 |
| imodbit_masterwork | 131072 |

### header_items.py
| Константа | Значение |
|-----------|----------|
| itp_type_horse | 0x0000000000000001 |
| itp_type_one_handed_wpn | 0x0000000000000002 |
| itp_unique | 0x0000000000001000 |

### header_map_icons.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_meshes.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_mission_templates.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_mission_types.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_music.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_operations.py
| Константа | Значение |
|-----------|----------|
| op_add | 0 |
| op_this_or_next | 1 |
| op_jump | 100 |
| op_player_is_female | 101 |
| ... | (ещё 76 констант) |

### header_particle_systems.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_parties.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_postfx.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_presentations.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_quests.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_scene_props.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_scenes.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_skills.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_skins.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_sounds.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_strings.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_tableau_materials.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_terrain_types.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_triggers.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

### header_troops.py
| Константа | Значение |
|-----------|----------|
| *Нет констант* |  |

## 2. СТРУКТУРА ДАННЫХ (TUPLES)

### module_animations.py
- **Имя массива:** `animations`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] const:3.0
  [1] const:myanim
  [2] const:0
  [3] const:50
  [4] var:arf_cyclic
  ```

### module_constants.py
- **Имя массива:** Не определено
- **Структура:** Не найдена

### module_dialogs.py
- **Имя массива:** `dialogs`
- **Количество элементов в кортеже:** 8
- **Структура первого элемента:**
  ```
  [0] var:dialog_begin
  [1] const:setup_char
  [2] var:vc_meet_bandit_leader
  [3] nested[2]
  [4] nested[3]
  ```

### module_factions.py
- **Имя массива:** `factions`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] const:fac_kingdom_1
  [1] const:Kingdom 1
  [2] const:0xFFFFFF
  [3] const:0xCCCCCC
  ```

### module_game_menus.py
- **Имя массива:** `game_menus`
- **Количество элементов в кортеже:** 6
- **Структура первого элемента:**
  ```
  [0] var:menu_char_view
  [1] const:presentation_char_view_screen
  [2] const:0
  [3] nested[3]
  [4] nested[3]
  ```

### module_info.py
- **Имя массива:** `game_strings`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```
  [0] const:Module string
  ```

### module_info_pages.py
- **Имя массива:** `info_pages`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] const:title
  [1] nested[2]
  ```

### module_items.py
- **Имя массива:** `items`
- **Количество элементов в кортеже:** 13
- **Структура первого элемента:**
  ```
  [0] var:itp_long_axe
  [1] const:Long Axe
  [2] var:itp_type_axe
  [3] nested[4]
  [4] nested[3]
  ```

### module_map_icons.py
- **Имя массива:** `map_icons`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] var:icon_lord
  [1] const:map_icon_lordly
  [2] const:0
  ```

### module_meshes.py
- **Имя массива:** `meshes`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```
  [0] var:mesh_castle_a
  ```

### module_mission_templates.py
- **Имя массива:** `mission_templates`
- **Количество элементов в кортеже:** 6
- **Структура первого элемента:**
  ```
  [0] var:mission_template_siege
  [1] nested[5]
  [2] nested[2]
  [3] nested[5]
  [4] nested[3]
  ```

### module_music.py
- **Имя массива:** `music_tracks`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] const:track_local_map
  [1] const:audio/music
  ```

### module_particle_systems.py
- **Имя массива:** `particle_systems`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:psys_dust_cloud
  [1] nested[3]
  ```

### module_parties.py
- **Имя массива:** `parties`
- **Количество элементов в кортеже:** 16
- **Структура первого элемента:**
  ```
  [0] var:p_main_party
  [1] var:party_template_kingdom_heroes
  [2] const:0
  [3] const:0
  [4] nested[2]
  ```

### module_party_templates.py
- **Имя массива:** `party_templates`
- **Количество элементов в кортеже:** 7
- **Структура первого элемента:**
  ```
  [0] var:party_template_kingdom_heroes
  [1] nested[20]
  [2] nested[2]
  [3] const:1
  [4] const:10
  ```

### module_postfx.py
- **Имя массива:** `postfx_params`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] var:pf_color_grading_0
  [1] const:0
  [2] const:0
  ```

### module_presentations.py
- **Имя массива:** `presentations`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] var:presentation_character_sheet
  [1] nested[20]
  [2] nested[3]
  [3] nested[3]
  [4] nested[3]
  ```

### module_quests.py
- **Имя массива:** `quests`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:qst_retrieve_items_from_bandits
  [1] const:Retrieve Items from Bandits
  ```

### module_scene_props.py
- **Имя массива:** `scene_props`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] var:prop_torch
  [1] const:torch
  [2] const:0
  ```

### module_scenes.py
- **Имя массива:** `scenes`
- **Количество элементов в кортеже:** 7
- **Структура первого элемента:**
  ```
  [0] var:scn_village_a
  [1] const:village_a
  [2] const:0
  [3] nested[3]
  [4] nested[2]
  [5] nested[2]
  [6] nested[3]
  ```

### module_scripts.py
- **Имя массива:** `scripts`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:script_calculate_arrow_damage
  [1] nested[10]
  ```

### module_simple_triggers.py
- **Имя массива:** `simple_triggers`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] const:Every Day
  [1] nested[2]
  [2] nested[3]
  [3] nested[3]
  ```

### module_skills.py
- **Имя массива:** `skills`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] var:skl_weapon_master
  [1] const:Weapon Master
  [2] const:0
  [3] const:0
  ```

### module_skins.py
- **Имя массива:** `skins`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:skin_human
  [1] const:human
  ```

### module_sounds.py
- **Имя массива:** `sounds`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:snd_hit_flesh_s1
  [1] const:snd_hit_flesh_s1
  ```

### module_strings.py
- **Имя массива:** `game_strings`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```
  [0] const:module_strings_item_descriptors_start
  ```

### module_tableau_materials.py
- **Имя массива:** `tableau_materials`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] var:tm_char_portrait
  [1] const:portrait_0
  [2] const:0
  ```

### module_triggers.py
- **Имя массива:** `triggers`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] const:0
  [1] nested[2]
  [2] nested[3]
  ```

### module_troops.py
- **Имя массива:** `troops`
- **Количество элементов в кортеже:** 20
- **Структура первого элемента:**
  ```
  [0] var:troop_player
  [1] const:Player
  [2] var:fac_player_faction
  [3] nested[4]
  [4] nested[4]
  ```

### module_variables.py
- **Имя массива:** Не определено
- **Структу��а:** Не найдена

## 3. РЕЕСТР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ

### Использованные глобальные переменные ($var):

- `$player_account_gold`
- `$player_battle_killed_count`
- `$player_battle_won_count`
- `$player_death_count`
- `$player_killed_count`
- `$player_party_morale`
- `$player_renown`
- `$player_troop_morale`
- `$player_wounded_count`
- `$temp_array_a`
- `$temp_array_b`
- `$temp_inventory`
- `$temp_quest_giver`
- `$temp_target_npc`

**Всего уникальных глобальных переменных:** 14

## 4. РЕЕСТР ЛОКАЛЬНЫХ РЕГИСТРОВ И СТРОК

### Паттерны использования регистров:

| Регистр | Количество использований |
|---------|-------------------------|
| reg0 | 342 |
| reg1 | 318 |
| reg2 | 298 |
| reg3 | 267 |
| reg4 | 245 |
| reg5 | 178 |
| reg6 | 165 |
| reg7 | 142 |
| s0 | 89 |
| s1 | 76 |
| pos_0 | 42 |
| pos_1 | 38 |
| reg8 | 35 |

*Всего типов регистров: 13*

---

**Сгенерировано:** 48 файлов констант, 21 файлов данных, 59 файлов обработки

**Базовая директория:** `./Vanilla Module System v1.171`
