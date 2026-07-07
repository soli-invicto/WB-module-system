# 🗺️ WARBRAND CODE MAP

Auto-generated analysis of Warband Module System v1.171

============================================================


## 1. КОНСТАНТЫ И ФЛАГИ

### header_animations.py

| Константа | Значение |
|-----------|----------|
| arf_blend_in_0 | 0x00000001 |
| arf_blend_in_1 | 0x00000002 |
| arf_blend_in_2 | 0x00000003 |
| arf_blend_in_3 | 0x00000004 |
| arf_blend_in_4 | 0x00000005 |
| arf_blend_in_5 | 0x00000006 |
| arf_blend_in_6 | 0x00000007 |
| arf_blend_in_7 | 0x00000008 |
| arf_blend_in_8 | 0x00000009 |
| arf_blend_in_9 | 0x0000000a |
| arf_blend_in_10 | 0x0000000b |
| arf_blend_in_11 | 0x0000000c |
| arf_blend_in_12 | 0x0000000d |
| arf_blend_in_13 | 0x0000000e |
| arf_blend_in_14 | 0x0000000f |
| arf_blend_in_15 | 0x00000010 |
| arf_blend_in_16 | 0x00000011 |
| arf_blend_in_17 | 0x00000012 |
| arf_blend_in_18 | 0x00000013 |
| arf_blend_in_19 | 0x00000014 |
| arf_blend_in_20 | 0x00000015 |
| arf_blend_in_21 | 0x00000016 |
| arf_blend_in_22 | 0x00000017 |
| arf_blend_in_23 | 0x00000018 |
| arf_blend_in_24 | 0x00000019 |
| arf_blend_in_25 | 0x0000001a |
| arf_blend_in_26 | 0x0000001b |
| arf_blend_in_27 | 0x0000001c |
| arf_blend_in_28 | 0x0000001d |
| arf_blend_in_29 | 0x0000001e |
| arf_blend_in_30 | 0x0000001f |
| arf_blend_in_31 | 0x00000020 |
| arf_blend_in_32 | 0x00000021 |
| arf_blend_in_48 | 0x00000031 |
| arf_blend_in_64 | 0x00000041 |
| arf_blend_in_128 | 0x00000081 |
| arf_blend_in_254 | 0x000000ff |
| arf_make_walk_sound | 0x00000100 |
| arf_make_custom_sound | 0x00000200 |
| arf_two_handed_blade | 0x01000000 |
| arf_lancer | 0x02000000 |
| arf_stick_item_to_left_hand | 0x04000000 |
| arf_cyclic | 0x10000000 |
| arf_use_walk_progress | 0x20000000 |
| arf_use_stand_progress | 0x40000000 |
| arf_use_inv_walk_progress | 0x80000000 |
| amf_priority_mask | 0x00000fff |
| amf_rider_rot_bow | 0x00001000 |
| amf_rider_rot_throw | 0x00002000 |
| amf_rider_rot_crossbow | 0x00003000 |
| amf_rider_rot_pistol | 0x00004000 |
| amf_rider_rot_overswing | 0x00005000 |
| amf_rider_rot_thrust | 0x00006000 |
| amf_rider_rot_swing_right | 0x00007000 |
| amf_rider_rot_swing_left | 0x00008000 |
| amf_rider_rot_couched_lance | 0x00009000 |
| amf_rider_rot_shield | 0x0000a000 |
| amf_rider_rot_defend | 0x0000b000 |
| amf_start_instantly | 0x00010000 |
| amf_use_cycle_period | 0x00100000 |
| amf_use_weapon_speed | 0x00200000 |
| amf_use_defend_speed | 0x00400000 |
| amf_accurate_body | 0x00800000 |
| amf_client_prediction | 0x01000000 |
| amf_play | 0x02000000 |
| amf_keep | 0x04000000 |
| amf_restart | 0x08000000 # restart animation even if it is the current ... |
| amf_hide_weapon | 0x10000000 |
| amf_client_owner_prediction | 0x20000000 |
| amf_use_inertia | 0x40000000 |
| amf_continue_to_next | 0x80000000 |
| acf_synch_with_horse | 0x00000001 |
| acf_align_with_ground | 0x00000002 |
| acf_enforce_lowerbody | 0x00000100 |
| acf_enforce_rightside | 0x00000200 |
| acf_enforce_all | 0x00000400 |
| acf_parallels_for_look_slope | 0x00001000 |
| acf_lock_camera | 0x00002000 |
| acf_displace_position | 0x00004000 |
| acf_ignore_slope | 0x00008000 |
| acf_thrust | 0x00010000 |
| acf_right_cut | 0x00020000 |
| acf_left_cut | 0x00040000 |
| acf_overswing | 0x00080000 |
| acf_rot_vertical_mask | 0x00300000 |
| acf_rot_vertical_bow | 0x00100000 |
| acf_rot_vertical_sword | 0x00200000 |
| acf_anim_length_mask | 0xff000000 |
| acf_anim_length_bits | 24 |
| i | int(f * 255.0) |
| i | 1 |
| i | 255 |
| ai | get_byte(a) |
| bi | get_byte(b) |
| ai | get_byte(a) |
| bi | get_byte(b) |
| ci | get_byte(c) |
| di | get_byte(d) |

### header_common.py

| Константа | Значение |
|-----------|----------|
| multiplayer_event_set_item_selection | 0 |
| multiplayer_event_set_bot_selection | 1 |
| multiplayer_event_admin_start_map | 2 |
| multiplayer_event_admin_set_max_num_players | 3 |
| multiplayer_event_admin_set_num_bots_in_team | 4 |
| multiplayer_event_admin_set_friendly_fire | 5 |
| multiplayer_event_admin_set_ghost_mode | 6 |
| multiplayer_event_admin_set_control_block_dir | 7 |
| multiplayer_event_admin_set_add_to_servers_list | 8 |
| multiplayer_event_admin_set_respawn_period | 9 |
| multiplayer_event_admin_set_game_max_minutes | 10 |
| multiplayer_event_admin_set_round_max_seconds | 11 |
| multiplayer_event_admin_set_game_max_points | 12 |
| multiplayer_event_admin_set_point_gained_from_flags | 13 |
| multiplayer_event_admin_set_point_gained_from_capturing_flag | 14 |
| multiplayer_event_admin_set_server_name | 15 |
| multiplayer_event_admin_set_game_password | 16 |
| multiplayer_event_admin_set_team_faction | 17 |
| multiplayer_event_open_admin_panel | 18 |
| multiplayer_event_change_team_no | 19 |
| multiplayer_event_change_troop_id | 20 |
| multiplayer_event_start_new_poll | 21 |
| multiplayer_event_answer_to_poll | 22 |
| multiplayer_event_admin_kick_player | 23 |
| multiplayer_event_admin_ban_player | 24 |
| multiplayer_event_admin_set_num_bots_voteable | 25 |
| multiplayer_event_admin_set_factions_voteable | 26 |
| multiplayer_event_admin_set_maps_voteable | 27 |
| multiplayer_event_admin_set_player_respawn_as_bot | 28 |
| multiplayer_event_admin_set_combat_speed | 29 |
| multiplayer_event_admin_set_respawn_count | 30 |
| multiplayer_event_admin_set_kick_voteable | 31 |
| multiplayer_event_admin_set_ban_voteable | 32 |
| multiplayer_event_admin_set_valid_vote_ratio | 33 |
| multiplayer_event_admin_set_auto_team_balance_limit | 34 |
| multiplayer_event_admin_set_welcome_message | 35 |
| multiplayer_event_admin_set_initial_gold_multiplier | 36 |
| multiplayer_event_admin_set_battle_earnings_multiplier | 37 |
| multiplayer_event_admin_set_round_earnings_multiplier | 38 |
| multiplayer_event_admin_set_melee_friendly_fire | 39 |
| multiplayer_event_admin_set_friendly_fire_damage_self_ratio | 40 |
| multiplayer_event_admin_set_friendly_fire_damage_friend_ratio | 41 |
| multiplayer_event_admin_set_allow_player_banners | 42 |
| multiplayer_event_admin_set_force_default_armor | 43 |
| multiplayer_event_admin_set_anti_cheat | 44 |
| multiplayer_event_open_game_rules | 45 |
| multiplayer_event_offer_duel | 46 |
| multiplayer_event_admin_set_disallow_ranged_weapons | 47 |
| multiplayer_event_other_events | 48 |
| multiplayer_event_other_event_set_bot_purchase | 0 |
| multiplayer_event_other_event_ccoop_lock_companions | 1 |
| multiplayer_event_coop_set_agent_team_and_group | 2 |
| multiplayer_event_other_event_ccoop_count_down_visible | 3 |
| multiplayer_event_other_event_ccoop_count_down_invisible | 4 |
| multiplayer_event_other_spawn_prison_cart | 5 |
| multiplayer_event_other_destroy_prison_cart | 6 |
| multiplayer_event_other_event_ccoop_update_spawn_data_1 | 7 |
| multiplayer_event_other_event_ccoop_update_spawn_data_2 | 8 |
| multiplayer_event_other_event_ccoop_update_spawn_data_3 | 9 |
| multiplayer_event_other_event_ccoop_update_spawn_data_4 | 10 |
| multiplayer_event_other_event_ccoop_update_spawn_data_5 | 11 |
| multiplayer_event_other_event_ccoop_update_spawn_data_6 | 12 |
| multiplayer_event_other_events_change_companion_level | 13 |
| multiplayer_event_admin_set_ccoop_difficulty | 14 |
| multiplayer_event_other_event_unequip_item | 15 |
| multiplayer_event_other_event_equip_item | 16 |
| multiplayer_event_coop_send_drop_assignment_to_server | 17 |
| multiplayer_event_coop_set_agent_team_and_group | 18 |
| multiplayer_event_return_max_num_players | 50 |
| multiplayer_event_return_num_bots_in_team | 51 |
| multiplayer_event_return_friendly_fire | 52 |
| multiplayer_event_return_ghost_mode | 53 |
| multiplayer_event_return_control_block_dir | 54 |
| multiplayer_event_return_combat_speed | 55 |
| multiplayer_event_return_add_to_servers_list | 56 |
| multiplayer_event_return_respawn_period | 57 |
| multiplayer_event_return_game_max_minutes | 58 |
| multiplayer_event_return_round_max_seconds | 59 |
| multiplayer_event_return_game_max_points | 60 |
| multiplayer_event_return_point_gained_from_flags | 61 |
| multiplayer_event_return_point_gained_from_capturing_flag | 62 |
| multiplayer_event_return_server_name | 63 |
| multiplayer_event_return_game_password | 64 |
| multiplayer_event_return_game_type | 65 |
| multiplayer_event_return_confirmation | 66 |
| multiplayer_event_return_rejection | 67 |
| multiplayer_event_show_multiplayer_message | 68 |
| multiplayer_event_draw_this_round | 69 |
| multiplayer_event_set_attached_scene_prop | 70 |
| multiplayer_event_set_team_flag_situation | 71 |
| multiplayer_event_set_team_score | 72 |
| multiplayer_event_set_num_agents_around_flag | 73 |
| multiplayer_event_ask_for_poll | 74 |
| multiplayer_event_change_flag_owner | 75 |
| multiplayer_event_use_item | 76 |
| multiplayer_event_set_scene_prop_open_or_close | 77 |
| multiplayer_event_set_round_start_time | 78 |
| multiplayer_event_force_start_team_selection | 79 |
| multiplayer_event_start_death_mode | 80 |
| multiplayer_event_return_num_bots_voteable | 81 |
| multiplayer_event_return_factions_voteable | 82 |
| multiplayer_event_return_maps_voteable | 83 |
| multiplayer_event_return_next_team_faction | 84 |
| multiplayer_event_return_player_respawn_as_bot | 85 |
| multiplayer_event_set_player_score_kill_death | 86 |
| multiplayer_event_set_day_time | 87 |
| multiplayer_event_return_respawn_count | 88 |
| multiplayer_event_return_player_respawn_spent | 89 |
| multiplayer_event_return_kick_voteable | 90 |
| multiplayer_event_return_ban_voteable | 91 |
| multiplayer_event_return_valid_vote_ratio | 92 |
| multiplayer_event_return_auto_team_balance_limit | 93 |
| multiplayer_event_return_initial_gold_multiplier | 94 |
| multiplayer_event_return_battle_earnings_multiplier | 95 |
| multiplayer_event_return_round_earnings_multiplier | 96 |
| multiplayer_event_return_renaming_server_allowed | 97 |
| multiplayer_event_return_changing_game_type_allowed | 98 |
| multiplayer_event_return_melee_friendly_fire | 99 |
| multiplayer_event_return_friendly_fire_damage_self_ratio | 100 |
| multiplayer_event_return_friendly_fire_damage_friend_ratio | 101 |
| multiplayer_event_return_allow_player_banners | 102 |
| multiplayer_event_return_force_default_armor | 103 |
| multiplayer_event_return_anti_cheat | 104 |
| multiplayer_event_return_open_game_rules | 105 |
| multiplayer_event_return_max_num_bots | 106 |
| multiplayer_event_return_server_mission_timer_while_player_joined | 107 |
| multiplayer_event_show_duel_request | 108 |
| multiplayer_event_start_duel | 109 |
| multiplayer_event_cancel_duel | 110 |
| multiplayer_event_show_server_message | 111 |
| multiplayer_event_return_disallow_ranged_weapons | 112 |
| multiplayer_event_return_set_bot_selection | 113 |
| multiplayer_event_return_team_ratio | 114 |
| multiplayer_event_return_squad_size | 115 |
| multiplayer_event_return_disallow_granades | 116 |
| multiplayer_event_return_sound_at_pos | 117 |
| multiplayer_event_return_enable_cbf_squad_ratio | 118 |
| multiplayer_event_return_cbf_squad_ratio | 119 |
| multiplayer_event_coop_drop_item | 120 |
| multiplayer_event_coop_chest_opened | 121 |
| multiplayer_event_return_ccoop_difficulty | 122 |
| multiplayer_event_ccoop_victory_message | 123 |
| multiplayer_event_ccoop_return_of_the_king | 124 |
| multiplayer_message_type_auto_team_balance_done | 2 |
| multiplayer_message_type_auto_team_balance_next | 3 |
| multiplayer_message_type_capture_the_flag_score | 4 |
| multiplayer_message_type_flag_returned_home | 5 |
| multiplayer_message_type_capture_the_flag_stole | 6 |
| multiplayer_message_type_poll_result | 7 |
| multiplayer_message_type_flag_neutralized | 8 |
| multiplayer_message_type_flag_captured | 9 |
| multiplayer_message_type_flag_is_pulling | 10 |
| multiplayer_message_type_auto_team_balance_no_need | 11 |
| multiplayer_message_type_round_result_in_battle_mode | 12 |
| multiplayer_message_type_round_result_in_siege_mode | 13 |
| multiplayer_message_type_round_draw | 14 |
| multiplayer_message_type_target_destroyed | 15 |
| multiplayer_message_type_defenders_saved_n_targets | 16 |
| multiplayer_message_type_attackers_won_the_round | 17 |
| multiplayer_message_type_start_death_mode | 18 |
| multiplayer_game_type_deathmatch | 0 |
| multiplayer_game_type_team_deathmatch | 1 |
| multiplayer_game_type_battle | 2 |
| multiplayer_game_type_destroy | 3 |
| multiplayer_game_type_capture_the_flag | 4 |
| multiplayer_game_type_headquarters | 5 |
| multiplayer_game_type_siege | 6 |
| multiplayer_game_type_duel | 7 |
| multiplayer_game_type_captain_coop | 8 |
| multiplayer_num_game_types | 9 |
| multiplayer_round_max_seconds_min | 60 |
| multiplayer_round_max_seconds_max | 901 |
| multiplayer_respawn_period_min | 3 |
| multiplayer_respawn_period_max | 31 #can only be 30 seconds max (due to agent deletion aft... |
| multiplayer_siege_mod_defender_team_extra_respawn_time | 27 #It was 20 in 1.113 but it is increased it to 25 in 1.... |
| multiplayer_new_agents_finish_spawning_time | 30 |
| multiplayer_max_possible_player_id | 1000 |
| multi_team_spectator | 2 |
| multi_team_unassigned | multi_team_spectator + 1 |
| multi_data_maps_for_game_type_begin | 0 |
| multi_data_maps_for_game_type_end | multi_data_maps_for_game_type_begin + 30 |
| multi_data_troop_button_indices_begin | multi_data_maps_for_game_type_end |
| multi_data_troop_button_indices_end | multi_data_troop_button_indices_begin + 16 #maximum 16 tr... |
| multi_data_item_button_indices_begin | multi_data_troop_button_indices_end |
| multi_data_item_button_indices_end | multi_data_item_button_indices_begin + 100 #maximum 100 i... |
| multi_data_flag_owner_begin | multi_data_item_button_indices_end |
| multi_data_flag_owner_end | multi_data_flag_owner_begin + 10 #maximum of 10 flags per... |
| multi_data_flag_players_around_begin | multi_data_flag_owner_end |
| multi_data_flag_players_around_end | multi_data_flag_players_around_begin + 10 #maximum of 10 ... |
| multi_data_flag_owned_seconds_begin | multi_data_flag_players_around_end |
| multi_data_flag_owned_seconds_end | multi_data_flag_owned_seconds_begin + 10 #maximum of 10 f... |
| multi_data_flag_pull_code_begin | multi_data_flag_owned_seconds_end |
| multi_data_flag_pull_code_end | multi_data_flag_pull_code_begin + 10 #maximum of 10 flags... |
| multi_data_ccoop_wave_spawn_data_begin | multi_data_flag_pull_code_end |
| multi_data_ccoop_wave_spawn_data_end | multi_data_ccoop_wave_spawn_data_begin + 16 #maximum of 5... |
| multi_data_equipment_holder_begin | multi_data_ccoop_wave_spawn_data_end |
| multi_data_equipment_holder_end | multi_data_equipment_holder_begin + 9 |
| multi_data_player_index_list_begin | multi_data_equipment_holder_end |
| multi_entry_points_for_usable_items_start | 100 |
| multi_entry_points_for_usable_items_end | multi_entry_points_for_usable_items_start + 10 |
| multi_item_class_type_sword | 1 |
| multi_item_class_type_axe | 2 |
| multi_item_class_type_blunt | 3 |
| multi_item_class_type_war_picks | 4 |
| multi_item_class_type_cleavers | 5 |
| multi_item_class_type_two_handed_sword | 6 |
| multi_item_class_type_two_handed_axe | 7 |
| multi_item_class_type_spear | 8 |
| multi_item_class_type_lance | 9 |
| multi_item_class_type_small_shield | 10 |
| multi_item_class_type_large_shield | 11 |
| multi_item_class_type_bow | 12 |
| multi_item_class_type_crossbow | 13 |
| multi_item_class_type_arrow | 14 |
| multi_item_class_type_bolt | 15 |
| multi_item_class_type_throwing | 16 |
| multi_item_class_type_throwing_axe | 17 |
| multi_item_class_type_horse | 18 |
| multi_item_class_type_light_armor | 19 |
| multi_item_class_type_medium_armor | 20 |
| multi_item_class_type_heavy_armor | 21 |
| multi_item_class_type_light_helm | 22 |
| multi_item_class_type_heavy_helm | 23 |
| multi_item_class_type_light_foot | 24 |
| multi_item_class_type_heavy_foot | 25 |
| multi_item_class_type_glove | 26 |
| multi_item_class_type_melee_weapons_begin | multi_item_class_type_sword |
| multi_item_class_type_melee_weapons_end | multi_item_class_type_small_shield |
| multi_item_class_type_ranged_weapons_begin | multi_item_class_type_bow |
| multi_item_class_type_ranged_weapons_end | multi_item_class_type_horse |
| multi_item_class_type_shields_begin | multi_item_class_type_melee_weapons_end |
| multi_item_class_type_shields_end | multi_item_class_type_bow |
| multi_item_class_type_weapons_begin | multi_item_class_type_sword |
| multi_item_class_type_weapons_end | multi_item_class_type_horse |
| multi_item_class_type_horses_begin | multi_item_class_type_weapons_end |
| multi_item_class_type_horses_end | multi_item_class_type_light_armor |
| multi_item_class_type_bodies_begin | multi_item_class_type_horses_end |
| multi_item_class_type_bodies_end | multi_item_class_type_light_helm |
| multi_item_class_type_heads_begin | multi_item_class_type_bodies_end |
| multi_item_class_type_heads_end | multi_item_class_type_light_foot |
| multi_item_class_type_feet_begin | multi_item_class_type_heads_end |
| multi_item_class_type_feet_end | multi_item_class_type_glove |
| multi_item_class_type_gloves_begin | multi_item_class_type_feet_end |
| multi_item_class_type_gloves_end | multi_item_class_type_glove + 1 |
| multi_troop_class_other | 0 |
| multi_troop_class_infantry | 1 |
| multi_troop_class_spearman | 2 |
| multi_troop_class_cavalry | 3 |
| multi_troop_class_archer | 4 |
| multi_troop_class_crossbowman | 5 |
| multi_troop_class_mounted_archer | 6 |
| multi_troop_class_mounted_crossbowman | 7 |
| multi_num_valid_entry_points | 64 |
| multi_num_valid_entry_points_div_2 | 32 |
| multi_battle_round_team_money_add | 500 |
| multi_destroy_save_or_destroy_target_money_add | 100 |
| multi_destroy_target_money_add | 1500 |
| multi_initial_gold_value | 1000 |
| multi_max_gold_that_can_be_stored | 15000 |
| multi_killer_agent_standard_money_add | 150 #(2/3 = 100 for battle & destroy, 3/3 = 150 for siege... |
| multi_killer_agent_loot_percentage_share | 12 #(2/3 = 8% for battle & destroy, 3/3 = 12% for siege, ... |
| multi_dead_agent_loot_percentage_share | 48 #(2/3 = 32% for battle & destroy, 3/3 = 48% for siege,... |
| multi_minimum_gold | 1000 #(same in all modes) |
| multi_minimum_target_health | 1200 |
| multi_max_seconds_flag_can_stay_in_ground | 60 |
| multi_capture_the_flag_score_flag_returning | 1 |
| multi_initial_spawn_point_team_1 | 0 |
| multi_initial_spawn_point_team_2 | 32 |
| multi_base_point_team_1 | 64 |
| multi_base_point_team_2 | 65 |
| multi_siege_flag_point | 66 |
| multi_death_mode_point | 67 |
| multi_headquarters_pole_height | 900 |
| multi_headquarters_flag_height_to_win | 800 #used in sd death mode |
| multi_headquarters_flag_initial_height | 100 #used in sd death mode |
| multi_headquarters_max_distance_sq_to_raise_flags | 1600 #4m * 4m * 100 = 1600 |
| multi_headquarters_distance_sq_to_set_flag | 8100 #9m * 9m * 100 = 8100 |
| multi_headquarters_distance_sq_to_change_flag | 400 #2m * 2m * 100 = 400 |
| multi_headquarters_distance_to_change_flag | 200 #2m * 100 = 200 |
| multi_distance_sq_to_use_belfry | 36 #6m * 6m = 36 (there is no * 100 for this one because ... |
| multi_max_sq_dist_between_agents_to_longer_mof_time | 49 #7m * 7m = 49m |
| min_allowed_flag_height_difference_to_make_score | 50 |
| multiplayer_battle_formula_value_a | 15 |
| multiplayer_battle_formula_value_b | 18000 #think about 18000-20000 if death mod very much hap... |
| multiplayer_spawn_above_opt_enemy_dist_point | 32 #while finding most suitable spawn point if nearest en... |
| multiplayer_spawn_min_enemy_dist_limit | 45 #while finding most suitable spawn point if nearest en... |
| multiplayer_poll_disable_period | 900 #15 minutes |
| multi_distance_to_captain_spaw_point | 15*100 |
| multi_killer_captain_add | 60 |
| multi_captain_recomended_players_max | 16 |
| multi_killer_captain_coop_add | 200 |
| escape_menu_item_height | 40 |
| bignum | 0x40000000000000000000000000000000 |
| op_num_value_bits | 24 + 32 |
| tag_register | 1 |
| tag_variable | 2 |
| tag_string | 3 |
| tag_item | 4 |
| tag_troop | 5 |
| tag_faction | 6 |
| tag_quest | 7 |
| tag_party_tpl | 8 |
| tag_party | 9 |
| tag_scene | 10 |
| tag_mission_tpl | 11 |
| tag_menu | 12 |
| tag_script | 13 |
| tag_particle_sys | 14 |
| tag_scene_prop | 15 |
| tag_sound | 16 |
| tag_local_variable | 17 |
| tag_map_icon | 18 |
| tag_skill | 19 |
| tag_mesh | 20 |
| tag_presentation | 21 |
| tag_quick_string | 22 |
| tag_track | 23 |
| tag_tableau | 24 |
| tag_animation | 25 |
| tags_end | 26 |
| opmask_register | tag_register       << op_num_value_bits |
| opmask_variable | tag_variable       << op_num_value_bits |
| opmask_quest_index | tag_quest          << op_num_value_bits |
| opmask_local_variable | tag_local_variable << op_num_value_bits |
| opmask_quick_string | tag_quick_string   << op_num_value_bits |
| result | -1 |
| num_objects | len(objects) |
| i_object | 0 |
| object_id_lowercase | object_id.lower() |
| object | objects[i_object] |
| result | i_object |
| s0 | 0 |
| s1 | 1 |
| s2 | 2 |
| s3 | 3 |
| s4 | 4 |
| s5 | 5 |
| s6 | 6 |
| s7 | 7 |
| s8 | 8 |
| s9 | 9 |
| s10 | 10 |
| s11 | 11 |
| s12 | 12 |
| s13 | 13 |
| s14 | 14 |
| s15 | 15 |
| s16 | 16 |
| s17 | 17 |
| s18 | 18 |
| s19 | 19 |
| s20 | 20 |
| s21 | 21 |
| s22 | 22 |
| s23 | 23 |
| s24 | 24 |
| s25 | 25 |
| s26 | 26 |
| s27 | 27 |
| s28 | 28 |
| s29 | 29 |
| s30 | 30 |
| s31 | 31 |
| s32 | 32 |
| s33 | 33 |
| s34 | 34 |
| s35 | 35 |
| s36 | 36 |
| s37 | 37 |
| s38 | 38 |
| s39 | 39 |
| s40 | 40 |
| s41 | 41 |
| s42 | 42 |
| s43 | 43 |
| s44 | 44 |
| s45 | 45 |
| s46 | 46 |
| s47 | 47 |
| s48 | 48 |
| s49 | 49 |
| s50 | 50 |
| s51 | 51 |
| s52 | 52 |
| s53 | 53 |
| s54 | 54 |
| s55 | 55 |
| s56 | 56 |
| s57 | 57 |
| s58 | 58 |
| s59 | 59 |
| s60 | 60 |
| s61 | 61 |
| s62 | 62 |
| s63 | 63 |
| s64 | 64 |
| s65 | 65 |
| s66 | 66 |
| s67 | 67 |
| pos0 | 0 |
| pos1 | 1 |
| pos2 | 2 |
| pos3 | 3 |
| pos4 | 4 |
| pos5 | 5 |
| pos6 | 6 |
| pos7 | 7 |
| pos8 | 8 |
| pos9 | 9 |
| pos10 | 10 |
| pos11 | 11 |
| pos12 | 12 |
| pos13 | 13 |
| pos14 | 14 |
| pos15 | 15 |
| pos16 | 16 |
| pos17 | 17 |
| pos18 | 18 |
| pos19 | 19 |
| pos20 | 20 |
| pos21 | 21 |
| pos22 | 22 |
| pos23 | 23 |
| pos24 | 24 |
| pos25 | 25 |
| pos26 | 26 |
| pos27 | 27 |
| pos28 | 28 |
| pos29 | 29 |
| pos30 | 30 |
| pos31 | 31 |
| pos32 | 32 |
| pos33 | 33 |
| pos34 | 34 |
| pos35 | 35 |
| pos36 | 36 |
| pos37 | 37 |
| pos38 | 38 |
| pos39 | 39 |
| pos40 | 40 |
| pos41 | 41 |
| pos42 | 42 |
| pos43 | 43 |
| pos44 | 44 |
| pos45 | 45 |
| pos46 | 46 |
| pos47 | 47 |
| pos48 | 48 |
| pos49 | 49 |
| pos50 | 50 |
| pos51 | 51 |
| pos52 | 52 |
| pos53 | 53 |
| pos54 | 54 |
| pos55 | 55 |
| pos56 | 56 |
| pos57 | 57 |
| pos58 | 58 |
| pos59 | 59 |
| pos60 | 60 |
| pos61 | 61 |
| pos62 | 62 |
| pos63 | 63 |
| pos_belfry_begin | 64 |
| reg0 | opmask_register| 0 |
| reg1 | opmask_register| 1 |
| reg2 | opmask_register| 2 |
| reg3 | opmask_register| 3 |
| reg4 | opmask_register| 4 |
| reg5 | opmask_register| 5 |
| reg6 | opmask_register| 6 |
| reg7 | opmask_register| 7 |
| reg8 | opmask_register| 8 |
| reg9 | opmask_register| 9 |
| reg10 | opmask_register|10 |
| reg11 | opmask_register|11 |
| reg12 | opmask_register|12 |
| reg13 | opmask_register|13 |
| reg14 | opmask_register|14 |
| reg15 | opmask_register|15 |
| reg16 | opmask_register|16 |
| reg17 | opmask_register|17 |
| reg18 | opmask_register|18 |
| reg19 | opmask_register|19 |
| reg20 | opmask_register|20 |
| reg21 | opmask_register|21 |
| reg22 | opmask_register|22 |
| reg23 | opmask_register|23 |
| reg24 | opmask_register|24 |
| reg25 | opmask_register|25 |
| reg26 | opmask_register|26 |
| reg27 | opmask_register|27 |
| reg28 | opmask_register|28 |
| reg29 | opmask_register|29 |
| reg30 | opmask_register|30 |
| reg31 | opmask_register|31 |
| reg32 | opmask_register|32 |
| reg33 | opmask_register|33 |
| reg34 | opmask_register|34 |
| reg35 | opmask_register|35 |
| reg36 | opmask_register|36 |
| reg37 | opmask_register|37 |
| reg38 | opmask_register|38 |
| reg39 | opmask_register|39 |
| reg40 | opmask_register|40 |
| reg41 | opmask_register|41 |
| reg42 | opmask_register|42 |
| reg43 | opmask_register|43 |
| reg44 | opmask_register|44 |
| reg45 | opmask_register|45 |
| reg46 | opmask_register|46 |
| reg47 | opmask_register|47 |
| reg48 | opmask_register|48 |
| reg49 | opmask_register|49 |
| reg50 | opmask_register|50 |
| reg51 | opmask_register|51 |
| reg52 | opmask_register|52 |
| reg53 | opmask_register|53 |
| reg54 | opmask_register|54 |
| reg55 | opmask_register|55 |
| reg56 | opmask_register|56 |
| reg57 | opmask_register|57 |
| reg58 | opmask_register|58 |
| reg59 | opmask_register|59 |
| reg60 | opmask_register|60 |
| reg61 | opmask_register|61 |
| reg62 | opmask_register|62 |
| reg63 | opmask_register|63 |
| reg65 | opmask_register|65 |
| spf_all_teams_are_enemy | 0x00000001, |
| spf_is_horseman | 0x00000002, |
| spf_examine_all_spawn_points | 0x00000004, |
| spf_team_0_spawn_far_from_entry_32 | 0x00000008, |
| spf_team_1_spawn_far_from_entry_0 | 0x00000010, |
| spf_team_1_spawn_far_from_entry_66 | 0x00000020, |
| spf_team_0_spawn_near_entry_0 | 0x00000040, |
| spf_team_0_spawn_near_entry_66 | 0x00000080, |
| spf_team_1_spawn_near_entry_32 | 0x00000100, |
| spf_team_0_walkers_spawn_at_high_points | 0x00000200, |
| spf_team_1_walkers_spawn_at_high_points | 0x00000400, |
| spf_try_to_spawn_close_to_at_least_one_enemy | 0x00000800, |
| spf_care_agent_to_agent_distances_less | 0x00001000, |

### header_dialogs.py

| Константа | Значение |
|-----------|----------|
| speaker_pos | 0 |
| ipt_token_pos | 1 |
| sentence_conditions_pos | 2 |
| text_pos | 3 |
| opt_token_pos | 4 |
| sentence_consequences_pos | 5 |
| anyone | 0x00000fff |
| repeat_for_factions | 0x00001000 |
| repeat_for_parties | 0x00002000 |
| repeat_for_troops | 0x00003000 |
| repeat_for_100 | 0x00004000 |
| repeat_for_1000 | 0x00005000 |
| plyr | 0x00010000 |
| party_tpl | 0x00020000 |
| auto_proceed | 0x00040000 |
| multi_line | 0x00080000 |
| suf_other_bits | 20 |

### header_factions.py

| Константа | Значение |
|-----------|----------|
| ff_always_hide_label | 0x00000001 |
| ff_max_rating_bits | 8 |
| ff_max_rating_mask | 0x0000ff00 |
| r | 100 - rating |
| result | -1 |
| num_factions | len(factions) |
| i_faction | 0 |
| faction | factions[i_faction] |
| result | i_faction |

### header_game_menus.py

| Константа | Значение |
|-----------|----------|
| mnf_join_battle | 0x00000001 #Consider this menu when the player joins a ba... |
| mnf_auto_enter | 0x00000010 #Automatically enter the town with the first m... |
| mnf_enable_hot_keys | 0x00000100 #Enables P,I,C keys |
| mnf_disable_all_keys | 0x00000200 #Disables all keys |
| mnf_scale_picture | 0x00001000 #Scale menu picture to offest screen aspect ratio |

### header_ground_types.py

| Константа | Значение |
|-----------|----------|
| ground_gray_stone | 0 |
| ground_brown_stone | 1 |
| ground_turf | 2 |
| ground_steppe | 3 |
| ground_snow | 4 |
| ground_earth | 5 |
| ground_desert | 6 |
| ground_forest | 7 |
| ground_pebbles | 8 |
| ground_village | 9 |
| ground_path | 10 |

### header_item_modifiers.py

| Константа | Значение |
|-----------|----------|
| imod_plain | 0 |
| imod_cracked | 1 |
| imod_rusty | 2 |
| imod_bent | 3 |
| imod_chipped | 4 |
| imod_battered | 5 |
| imod_poor | 6 |
| imod_crude | 7 |
| imod_old | 8 |
| imod_cheap | 9 |
| imod_fine | 10 |
| imod_well_made | 11 |
| imod_sharp | 12 |
| imod_balanced | 13 |
| imod_tempered | 14 |
| imod_deadly | 15 |
| imod_exquisite | 16 |
| imod_masterwork | 17 |
| imod_heavy | 18 |
| imod_strong | 19 |
| imod_powerful | 20 |
| imod_tattered | 21 |
| imod_ragged | 22 |
| imod_rough | 23 |
| imod_sturdy | 24 |
| imod_thick | 25 |
| imod_hardened | 26 |
| imod_reinforced | 27 |
| imod_superb | 28 |
| imod_lordly | 29 |
| imod_lame | 30 |
| imod_swaybacked | 31 |
| imod_stubborn | 32 |
| imod_timid | 33 |
| imod_meek | 34 |
| imod_spirited | 35 |
| imod_champion | 36 |
| imod_fresh | 37 |
| imod_day_old | 38 |
| imod_two_day_old | 39 |
| imod_smelling | 40 |
| imod_rotten | 41 |
| imod_large_bag | 42 |
| imodbit_plain | 1 |
| imodbit_cracked | 2 |
| imodbit_rusty | 4 |
| imodbit_bent | 8 |
| imodbit_chipped | 16 |
| imodbit_battered | 32 |
| imodbit_poor | 64 |
| imodbit_crude | 128 |
| imodbit_old | 256 |
| imodbit_cheap | 512 |
| imodbit_fine | 1024 |
| imodbit_well_made | 2048 |
| imodbit_sharp | 4096 |
| imodbit_balanced | 8192 |
| imodbit_tempered | 16384 |
| imodbit_deadly | 32768 |
| imodbit_exquisite | 65536 |
| imodbit_masterwork | 131072 |
| imodbit_heavy | 262144 |
| imodbit_strong | 524288 |
| imodbit_powerful | 1048576 |
| imodbit_tattered | 2097152 |
| imodbit_ragged | 4194304 |
| imodbit_rough | 8388608 |
| imodbit_sturdy | 16777216 |
| imodbit_thick | 33554432 |
| imodbit_hardened | 67108864 |
| imodbit_reinforced | 134217728 |
| imodbit_superb | 268435456 |
| imodbit_lordly | 536870912 |
| imodbit_lame | 1073741824 |
| imodbit_swaybacked | 2147483648 |
| imodbit_stubborn | 4294967296 |
| imodbit_timid | 8589934592 |
| imodbit_meek | 17179869184 |
| imodbit_spirited | 34359738368 |
| imodbit_champion | 68719476736 |
| imodbit_fresh | 137438953472 |
| imodbit_day_old | 274877906944 |
| imodbit_two_day_old | 549755813888 |
| imodbit_smelling | 1099511627776 |
| imodbit_rotten | 2199023255552 |
| imodbit_large_bag | 4398046511104 |

### header_items.py

| Константа | Значение |
|-----------|----------|
| itp_type_horse | 0x0000000000000001 |
| itp_type_one_handed_wpn | 0x0000000000000002 |
| itp_type_two_handed_wpn | 0x0000000000000003 |
| itp_type_polearm | 0x0000000000000004 |
| itp_type_arrows | 0x0000000000000005 |
| itp_type_bolts | 0x0000000000000006 |
| itp_type_shield | 0x0000000000000007 |
| itp_type_bow | 0x0000000000000008 |
| itp_type_crossbow | 0x0000000000000009 |
| itp_type_thrown | 0x000000000000000a |
| itp_type_goods | 0x000000000000000b |
| itp_type_head_armor | 0x000000000000000c |
| itp_type_body_armor | 0x000000000000000d |
| itp_type_foot_armor | 0x000000000000000e |
| itp_type_hand_armor | 0x000000000000000f |
| itp_type_pistol | 0x0000000000000010 |
| itp_type_musket | 0x0000000000000011 |
| itp_type_bullets | 0x0000000000000012 |
| itp_type_animal | 0x0000000000000013 |
| itp_type_book | 0x0000000000000014 |
| itp_force_attach_left_hand | 0x0000000000000100 |
| itp_force_attach_right_hand | 0x0000000000000200 |
| itp_force_attach_left_forearm | 0x0000000000000300 |
| itp_attach_armature | 0x0000000000000f00 |
| itp_attachment_mask | 0x0000000000000f00 |
| itp_unique | 0x0000000000001000 |
| itp_always_loot | 0x0000000000002000 |
| itp_no_parry | 0x0000000000004000 |
| itp_default_ammo | 0x0000000000008000 |
| itp_merchandise | 0x0000000000010000 |
| itp_wooden_attack | 0x0000000000020000 |
| itp_wooden_parry | 0x0000000000040000 |
| itp_food | 0x0000000000080000 |
| itp_cant_reload_on_horseback | 0x0000000000100000 |
| itp_two_handed | 0x0000000000200000 |
| itp_primary | 0x0000000000400000 |
| itp_secondary | 0x0000000000800000 |
| itp_covers_legs | 0x0000000001000000 |
| itp_doesnt_cover_hair | 0x0000000001000000 |
| itp_can_penetrate_shield | 0x0000000001000000 |
| itp_consumable | 0x0000000002000000 |
| itp_bonus_against_shield | 0x0000000004000000 |
| itp_penalty_with_shield | 0x0000000008000000 |
| itp_cant_use_on_horseback | 0x0000000010000000 |
| itp_civilian | 0x0000000020000000 |
| itp_next_item_as_melee | 0x0000000020000000 |
| itp_fit_to_head | 0x0000000040000000 |
| itp_offset_lance | 0x0000000040000000 |
| itp_covers_head | 0x0000000080000000 |
| itp_couchable | 0x0000000080000000 |
| itp_crush_through | 0x0000000100000000 |
| itp_remove_item_on_use | 0x0000000400000000 |
| itp_unbalanced | 0x0000000800000000 |
| itp_covers_beard | 0x0000001000000000    #remove beard mesh |
| itp_no_pick_up_from_ground | 0x0000002000000000 |
| itp_can_knock_down | 0x0000004000000000 |
| itp_covers_hair | 0x0000008000000000    #remove hair mesh for armors only |
| itp_force_show_body | 0x0000010000000000 # forces showing body (works on body a... |
| itp_force_show_left_hand | 0x0000020000000000 # forces showing left hand (works on h... |
| itp_force_show_right_hand | 0x0000040000000000 # forces showing right hand (works on ... |
| itp_covers_hair_partially | 0x0000080000000000 |
| itp_extra_penetration | 0x0000100000000000 |
| itp_has_bayonet | 0x0000200000000000 |
| itp_cant_reload_while_moving | 0x0000400000000000 |
| itp_ignore_gravity | 0x0000800000000000 |
| itp_ignore_friction | 0x0001000000000000 |
| itp_is_pike | 0x0002000000000000 |
| itp_offset_musket | 0x0004000000000000 |
| itp_no_blur | 0x0008000000000000 |
| itp_cant_reload_while_moving_mounted | 0x0010000000000000 |
| itp_has_upper_stab | 0x0020000000000000 |
| itp_disable_agent_sounds | 0x0040000000000000 #disable agent related sounds, but not... |
| itp_kill_info_mask | 0x0700000000000000 |
| itp_kill_info_bits | 56 # 0x0700000000000000 |
| ek_item_0 | 0 |
| ek_item_1 | 1 |
| ek_item_2 | 2 |
| ek_item_3 | 3 |
| ek_head | 4 |
| ek_body | 5 |
| ek_foot | 6 |
| ek_gloves | 7 |
| ek_horse | 8 |
| ek_food | 9 |
| max_inventory_items | 96 |
| num_equipment_kinds | ek_food + 1 |
| num_weapon_proficiencies | 7 |
| cut | 0 |
| pierce | 1 |
| blunt | 2 |
| ibf_armor_mask | 0x00000000000000000000000ff |
| ibf_damage_mask | 0x00000000000000000000003ff |
| ibf_10bit_mask | 0x00000000000000000000003ff |
| ibf_head_armor_bits | 0 |
| ibf_body_armor_bits | 8 |
| ibf_leg_armor_bits | 16 |
| ibf_weight_bits | 24 |
| ibf_difficulty_bits | 32 |
| ibf_hitpoints_mask | 0x0000ffff |
| ibf_hitpoints_bits | 40 |
| iwf_swing_damage_bits | 50 |
| iwf_swing_damage_type_bits | 58 |
| iwf_thrust_damage_bits | 60 |
| iwf_thrust_damage_type_bits | 68 |
| iwf_weapon_length_bits | 70 |
| iwf_speed_rating_bits | 80 |
| iwf_shoot_speed_bits | 90 |
| iwf_max_ammo_bits | 100 # use this for shield endurance too? |
| iwf_abundance_bits | 110 |
| iwf_accuracy_bits | 16  #reuse leg_armor for accuracy |
| iwf_damage_type_bits | 8 |
| a | int(4.0 * x) |
| a | ibf_armor_mask & a |
| a | (y >> ibf_weight_bits) & ibf_armor_mask |
| x | ((damage_type << iwf_damage_type_bits) | (damage & ibf_ar... |
| x | ((damage_type << iwf_damage_type_bits) | (damage & ibf_ar... |
| abnd | (y >> iwf_abundance_bits) & ibf_armor_mask |
| abnd | 100 |
| itcf_thrust_onehanded | 0x0000000000000001 |
| itcf_overswing_onehanded | 0x0000000000000002 |
| itcf_slashright_onehanded | 0x0000000000000004 |
| itcf_slashleft_onehanded | 0x0000000000000008 |
| itcf_thrust_twohanded | 0x0000000000000010 |
| itcf_overswing_twohanded | 0x0000000000000020 |
| itcf_slashright_twohanded | 0x0000000000000040 |
| itcf_slashleft_twohanded | 0x0000000000000080 |
| itcf_thrust_polearm | 0x0000000000000100 |
| itcf_overswing_polearm | 0x0000000000000200 |
| itcf_slashright_polearm | 0x0000000000000400 |
| itcf_slashleft_polearm | 0x0000000000000800 |
| itcf_shoot_bow | 0x0000000000001000 |
| itcf_shoot_javelin | 0x0000000000002000 |
| itcf_shoot_crossbow | 0x0000000000004000 |
| itcf_throw_stone | 0x0000000000010000 |
| itcf_throw_knife | 0x0000000000020000 |
| itcf_throw_axe | 0x0000000000030000 |
| itcf_throw_javelin | 0x0000000000040000 |
| itcf_shoot_pistol | 0x0000000000070000 |
| itcf_shoot_musket | 0x0000000000080000 |
| itcf_shoot_mask | 0x00000000000ff000 |
| itcf_horseback_thrust_onehanded | 0x0000000000100000 |
| itcf_horseback_overswing_right_onehanded | 0x0000000000200000 |
| itcf_horseback_overswing_left_onehanded | 0x0000000000400000 |
| itcf_horseback_slashright_onehanded | 0x0000000000800000 |
| itcf_horseback_slashleft_onehanded | 0x0000000001000000 |
| itcf_thrust_onehanded_lance | 0x0000000004000000 |
| itcf_thrust_onehanded_lance_horseback | 0x0000000008000000 |
| itcf_carry_mask | 0x00000007f0000000 |
| itcf_carry_sword_left_hip | 0x0000000010000000 |
| itcf_carry_axe_left_hip | 0x0000000020000000 |
| itcf_carry_dagger_front_left | 0x0000000030000000 |
| itcf_carry_dagger_front_right | 0x0000000040000000 |
| itcf_carry_quiver_front_right | 0x0000000050000000 |
| itcf_carry_quiver_back_right | 0x0000000060000000 |
| itcf_carry_quiver_right_vertical | 0x0000000070000000 |
| itcf_carry_quiver_back | 0x0000000080000000 |
| itcf_carry_revolver_right | 0x0000000090000000 |
| itcf_carry_pistol_front_left | 0x00000000a0000000 |
| itcf_carry_bowcase_left | 0x00000000b0000000 |
| itcf_carry_mace_left_hip | 0x00000000c0000000 |
| itcf_carry_axe_back | 0x0000000100000000 |
| itcf_carry_sword_back | 0x0000000110000000 |
| itcf_carry_kite_shield | 0x0000000120000000 |
| itcf_carry_round_shield | 0x0000000130000000 |
| itcf_carry_buckler_left | 0x0000000140000000 |
| itcf_carry_crossbow_back | 0x0000000150000000 |
| itcf_carry_bow_back | 0x0000000160000000 |
| itcf_carry_spear | 0x0000000170000000 |
| itcf_carry_board_shield | 0x0000000180000000 |
| itcf_carry_katana | 0x0000000210000000 |
| itcf_carry_wakizashi | 0x0000000220000000 |
| itcf_show_holster_when_drawn | 0x0000000800000000 |
| itcf_reload_pistol | 0x0000007000000000 |
| itcf_reload_musket | 0x0000008000000000 |
| itcf_reload_mask | 0x000000f000000000 |
| itcf_parry_forward_onehanded | 0x0000010000000000 |
| itcf_parry_up_onehanded | 0x0000020000000000 |
| itcf_parry_right_onehanded | 0x0000040000000000 |
| itcf_parry_left_onehanded | 0x0000080000000000 |
| itcf_parry_forward_twohanded | 0x0000100000000000 |
| itcf_parry_up_twohanded | 0x0000200000000000 |
| itcf_parry_right_twohanded | 0x0000400000000000 |
| itcf_parry_left_twohanded | 0x0000800000000000 |
| itcf_parry_forward_polearm | 0x0001000000000000 |
| itcf_parry_up_polearm | 0x0002000000000000 |
| itcf_parry_right_polearm | 0x0004000000000000 |
| itcf_parry_left_polearm | 0x0008000000000000 |
| itcf_horseback_slash_polearm | 0x0010000000000000 |
| itcf_overswing_spear | 0x0020000000000000 |
| itcf_overswing_musket | 0x0040000000000000 |
| itcf_thrust_musket | 0x0080000000000000 |
| itcf_force_64_bits | 0x8000000000000000 |
| itc_cleaver | itcf_force_64_bits | (itcf_overswing_onehanded|itcf_slash... |
| itc_dagger | itc_cleaver | itcf_thrust_onehanded |
| itc_parry_onehanded | itcf_force_64_bits | itcf_parry_forward_onehanded| itcf_p... |
| itc_longsword | itc_dagger | itc_parry_onehanded |
| itc_scimitar | itc_cleaver | itc_parry_onehanded |
| itc_parry_two_handed | itcf_force_64_bits | itcf_parry_forward_twohanded | itcf_... |
| itc_cut_two_handed | itcf_force_64_bits | (itcf_slashright_twohanded | itcf_sl... |
| itc_greatsword | itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_t... |
| itc_nodachi | itc_cut_two_handed | itc_parry_two_handed |
| itc_bastardsword | itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_t... |
| itc_morningstar | itc_cut_two_handed |  itc_parry_two_handed |itc_cleaver |
| itc_parry_polearm | itcf_parry_forward_polearm | itcf_parry_up_polearm | itcf... |
| itc_poleaxe | itc_parry_polearm| itcf_overswing_polearm |itcf_thrust_po... |
| itc_staff | itc_parry_polearm| itcf_thrust_onehanded_lance |itcf_thru... |
| itc_spear | itc_parry_polearm| itcf_thrust_onehanded_lance |itcf_thru... |
| itc_cutting_spear | itc_spear|itcf_overswing_polearm |
| itc_pike | itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_... |
| itc_guandao | itc_parry_polearm|itcf_overswing_polearm|itcf_thrust_pole... |
| itc_greatlance | itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_... |
| itc_musket_melee | itc_parry_polearm|itcf_overswing_musket|itcf_thrust_muske... |
| ixmesh_inventory | 0x1000000000000000 |
| ixmesh_flying_ammo | 0x2000000000000000 |
| ixmesh_carry | 0x3000000000000000 |

### header_map_icons.py

| Константа | Значение |
|-----------|----------|
| mcn_no_shadow | 0x00000001 |

### header_meshes.py

| Константа | Значение |
|-----------|----------|
| render_order_plus_1 | 0x00000001 |

### header_mission_templates.py

| Константа | Значение |
|-----------|----------|
| aif_group_bits | 0 |
| aif_group_mask | 0xF |
| aif_start_alarmed | 0x00000010 |
| grc_infantry | 0 |
| grc_archers | 1 |
| grc_cavalry | 2 |
| grc_heroes | 3 |
| grc_everyone | 9 |
| mordr_hold | 0 |
| mordr_follow | 1 |
| mordr_charge | 2 |
| mordr_mount | 3 |
| mordr_dismount | 4 |
| mordr_advance | 5 |
| mordr_fall_back | 6 |
| mordr_stand_closer | 7 |
| mordr_spread_out | 8 |
| mordr_use_blunt_weapons | 9 |
| mordr_use_any_weapon | 10 |
| mordr_stand_ground | 11 |
| mordr_hold_fire | 12 |
| mordr_fire_at_will | 13 |
| mordr_retreat | 14 |
| mordr_use_melee_weapons | 15 |
| mordr_use_ranged_weapons | 16 |
| mordr_fire_at_my_command | 17 |
| mordr_all_fire_now | 18 |
| mordr_left_fire_now | 19 |
| mordr_middle_fire_now | 20 |
| mordr_right_fire_now | 21 |
| mordr_form_1_row | 22 |
| mordr_form_2_row | 23 |
| mordr_form_3_row | 24 |
| mordr_form_4_row | 25 |
| mordr_form_5_row | 26 |
| rordr_free | 0 |
| rordr_mount | 1 |
| rordr_dismount | 2 |
| wordr_use_any_weapon | 0 |
| wordr_use_blunt_weapons | 1 |
| wordr_use_melee_weapons | 2 |
| wordr_use_ranged_weapons | 3 |
| aordr_fire_at_will | 0 |
| aordr_hold_your_fire | 1 |
| aisb_hold | 0 |
| aisb_go_to_pos | 1 |
| aisb_mount | 2 |
| aisb_dismount | 3 |
| aisb_melee | 4 |
| aisb_ranged | 5 |
| aisb_ranged_horseback | 6 |
| aisb_charge_horseback | 7 |
| aisb_maneuver_horseback | 8 |
| aisb_flock | 9 |
| aisb_race | 10 |
| aisb_patrol | 11 |
| aisb_no_enemies | 12 |
| aisb_horse_hold | 13 |
| aisb_horse_run_away | 14 |
| mtef_enemy_party | 0x00000001 |
| mtef_ally_party | 0x00000002 |
| mtef_scene_source | 0x00000004 |
| mtef_conversation_source | 0x00000008 |
| mtef_visitor_source | 0x00000010 |
| mtef_defenders | 0x00000040 |
| mtef_attackers | 0x00000080 |
| mtef_no_leader | 0x00000100 |
| mtef_no_companions | 0x00000200 |
| mtef_no_regulars | 0x00000400 |
| mtef_team_0 | 0x00001000 |
| mtef_team_1 | 0x00002000 |
| mtef_team_2 | 0x00003000 |
| mtef_team_3 | 0x00004000 |
| mtef_team_4 | 0x00005000 |
| mtef_team_5 | 0x00006000 |
| mtef_team_member_2 | 0x00008000 |
| mtef_infantry_first | 0x00010000 |
| mtef_archers_first | 0x00020000 |
| mtef_cavalry_first | 0x00040000 |
| mtef_no_auto_reset | 0x00080000 |
| mtef_reverse_order | 0x01000000 |
| mtef_use_exact_number | 0x02000000 |
| mtef_leader_only | mtef_no_companions | mtef_no_regulars |
| mtef_regulars_only | mtef_no_companions | mtef_no_leader |
| af_override_weapons | 0x0000000f |
| af_override_weapon_0 | 0x00000001 |
| af_override_weapon_1 | 0x00000002 |
| af_override_weapon_2 | 0x00000004 |
| af_override_weapon_3 | 0x00000008 |
| af_override_head | 0x00000010 |
| af_override_body | 0x00000020 |
| af_override_foot | 0x00000040 |
| af_override_gloves | 0x00000080 |
| af_override_horse | 0x00000100 |
| af_override_fullhelm | 0x00000200 |
| af_require_civilian | 0x10000000 |
| af_override_all_but_horse | af_override_weapons | af_override_head | af_override_body... |
| af_override_all | af_override_horse | af_override_all_but_horse |
| af_override_everything | af_override_all | af_override_foot |
| requires_third_party | 0x00000001 |
| mtf_arena_fight | 0x00000001 #identify enemies through team_no |
| mtf_team_fight | 0x00000001 #identify enemies through team_no |
| mtf_battle_mode | 0x00000002 #No inventory access |
| mtf_commit_casualties | 0x00000010 |
| mtf_no_blood | 0x00000100 |
| mtf_synch_inventory | 0x00010000 #Make a backup of player inventory and restore... |
| max_size | 1023 |
| xsize_bits | 12 |
| ysize_bits | 22 |
| mc_loot | 0x0001 |
| mc_imprison_unconscious | 0x0002 |

### header_mission_types.py

| Константа | Значение |
|-----------|----------|
| leave_wo_battle | 0 |
| leave_during_battle | 1 |
| cancel_attack | 2 |
| speak | 3 |
| intend_battle | 4 |
| cancel_reinforce | 5 |
| surrender | 6 |
| stay_back | 7 |
| charge | 8 |
| stay_back_with_ally | 9 |
| charge_with_ally | 10 |

### header_music.py

| Константа | Значение |
|-----------|----------|
| mtf_culture_1 | 0x00000001 |
| mtf_culture_2 | 0x00000002 |
| mtf_culture_3 | 0x00000004 |
| mtf_culture_4 | 0x00000008 |
| mtf_culture_5 | 0x00000010 |
| mtf_culture_6 | 0x00000020 |
| mtf_culture_all | 0x0000003F |
| mtf_looping | 0x00000040 |
| mtf_start_immediately | 0x00000080 |
| mtf_persist_until_finished | 0x00000100 |
| mtf_sit_tavern | 0x00000200 |
| mtf_sit_fight | 0x00000400 |
| mtf_sit_multiplayer_fight | 0x00000800 |
| mtf_sit_ambushed | 0x00001000 |
| mtf_sit_town | 0x00002000 |
| mtf_sit_town_infiltrate | 0x00004000 |
| mtf_sit_killed | 0x00008000 |
| mtf_sit_travel | 0x00010000 |
| mtf_sit_arena | 0x00020000 |
| mtf_sit_siege | 0x00040000 |
| mtf_sit_night | 0x00080000 |
| mtf_sit_day | 0x00100000 |
| mtf_sit_encounter_hostile | 0x00200000 |
| mtf_sit_main_title | 0x00400000 |
| mtf_sit_victorious | 0x00800000 |
| mtf_sit_feast | 0x01000000 |
| mtf_module_track | 0x10000000 ##set this flag for tracks placed under module... |

### header_operations.py

| Константа | Значение |
|-----------|----------|
| call_script | 1 # (call_script,<script_id>), |
| end_try | 3 # deprecated, use try_end instead |
| try_end | 3 # (try_end), |
| try_begin | 4 # (try_begin), |
| else_try_begin | 5 # deprecated, use else_try instead |
| else_try | 5 # (else_try), |
| try_for_range | 6 # Works like a for loop from lower-bound up to (upper-b... |
| try_for_range_backwards | 7	# Same as above but starts from (upper-bound - 1) down-... |
| try_for_parties | 11	# (try_for_parties,<destination>), |
| try_for_agents | 12	# (try_for_agents, <destination>, [<position_no>], [<r... |
| try_for_prop_instances | 16 # (try_for_prop_instances, <destination>, [<scene_prop... |
| try_for_players | 17	# (try_for_players, <destination>, [skip_server]), |
| store_script_param_1 | 21       # (store_script_param_1,<destination>),  --(With... |
| store_script_param_2 | 22       # (store_script_param_2,<destination>),  --(With... |
| store_script_param | 23       # (store_script_param,<destination>,<script_para... |
| ge | 30  # greater than or equal to -- (ge,<value>,<value>), |
| eq | 31  # equal to		      -- (eq,<value>,<value>), |
| gt | 32  # greater than	      -- (gt,<value>,<value>), |
| is_between | 33  # (is_between,<value>,<lower_bound>,<upper_bound>), #... |
| entering_town | 36 # (entering_town,<town_id>), |
| map_free | 37  # (map_free), |
| encountered_party_is_attacker | 39  # (encountered_party_is_attacker), |
| conversation_screen_is_active | 42  # (conversation_screen_active), #used in mission temp... |
| in_meta_mission | 44  # deprecated, do not use. |
| set_player_troop | 47  # (set_player_troop,<troop_id>), |
| store_repeat_object | 50  # stores the index of a repeated dialog option for re... |
| get_operation_set_version | 55  # (get_operation_set_version, <destination>), |
| set_physics_delta_time | 58  # (set_physics_delta_time, <fixed_value>), #Default i... |
| set_result_string | 60  # sets the result string for game scripts that need o... |
| is_camera_in_first_person | 61  # (is_camera_in_first_person), |
| set_camera_in_first_person | 62  # (set_camera_in_first_person, <value>), # 1 = first,... |
| game_key_get_mapped_key_name | 65  # (game_key_get_mapped_key_name, <string_register>, <... |
| key_is_down | 70  # fails if the key is not currently down (key_is_down... |
| key_clicked | 71  # fails if the key is not clicked on the specific fra... |
| game_key_is_down | 72  # fails if the game key is not currently down (key_is... |
| game_key_clicked | 73  # fails if the game key is not clicked on the specifi... |
| mouse_get_position | 75  # (mouse_get_position, <position_no>), #x and y value... |
| omit_key_once | 77  # game omits any bound action for the key once (omit_... |
| clear_omitted_keys | 78  # (clear_omitted_keys), |
| get_global_cloud_amount | 90  # (get_global_cloud_amount, <destination>), #returns ... |
| set_global_cloud_amount | 91  # (set_global_cloud_amount, <value>), #value is clamp... |
| get_global_haze_amount | 92  # (get_global_haze_amount, <destination>), #returns a... |
| set_global_haze_amount | 93  # (set_global_haze_amount, <value>), #value is clampe... |
| hero_can_join | 101 # (hero_can_join, [party_id]), |
| hero_can_join_as_prisoner | 102 # (hero_can_join_as_prisoner, [party_id]), |
| party_can_join | 103 # (party_can_join), |
| party_can_join_as_prisoner | 104 # (party_can_join_as_prisoner), |
| troops_can_join | 105 # (troops_can_join,<value>), |
| troops_can_join_as_prisoner | 106 # (troops_can_join_as_prisoner,<value>), |
| party_can_join_party | 107 # (party_can_join_party, <joiner_party_id>, <host_par... |
| party_end_battle | 108 # (party_end_battle,<party_no>), |
| main_party_has_troop | 110 # (main_party_has_troop,<troop_id>), |
| party_is_in_town | 130 # (party_is_in_town,<party_id_1>,<party_id_2>), |
| party_is_in_any_town | 131 # (party_is_in_any_town,<party_id>), |
| party_is_active | 132 # (party_is_active,<party_id>), |
| player_has_item | 150 # (player_has_item,<item_id>), |
| troop_has_item_equipped | 151 # (troop_has_item_equipped,<troop_id>,<item_id>), |
| troop_is_mounted | 152 # (troop_is_mounted,<troop_id>), |
| troop_is_guarantee_ranged | 153 # (troop_is_guarantee_ranged, <troop_id>), |
| troop_is_guarantee_horse | 154 # (troop_is_guarantee_horse, <troop_id>), |
| check_quest_active | 200 # (check_quest_active,<quest_id>), |
| check_quest_finished | 201 # (check_quest_finished,<quest_id>), |
| check_quest_succeeded | 202 # (check_quest_succeeded,<quest_id>), |
| check_quest_failed | 203 # (check_quest_failed,<quest_id>), |
| check_quest_concluded | 204 # (check_quest_concluded,<quest_id>), |
| is_trial_version | 250 # (is_trial_version), |
| is_edit_mode_enabled | 255 # (is_edit_mode_enabled), |
| options_get_damage_to_player | 260 # (options_get_damage_to_player, <destination>), #0 =... |
| options_set_damage_to_player | 261 # (options_set_damage_to_player, <value>), #0 = 1/4, ... |
| options_get_damage_to_friends | 262 # (options_get_damage_to_friends, <destination>), #0 ... |
| options_set_damage_to_friends | 263 # (options_set_damage_to_friends, <value>), #0 = 1/2,... |
| options_get_combat_ai | 264 # (options_get_combat_ai, <destination>), #0 = good, ... |
| options_set_combat_ai | 265 # (options_set_combat_ai, <value>), #0 = good, 1 = av... |
| options_get_campaign_ai | 266 # (options_get_campaign_ai, <destination>), #0 = good... |
| options_set_campaign_ai | 267 # (options_set_campaign_ai, <value>), #0 = good, 1 = ... |
| options_get_combat_speed | 268 # (options_get_combat_speed, <destination>), #0 = slo... |
| options_set_combat_speed | 269 # (options_set_combat_speed, <value>), #0 = slowest, ... |
| options_get_battle_size | 270 # (options_get_battle_size, <destination>), # returns... |
| options_set_battle_size | 271 # (options_set_battle_size, <value>), # sets battle s... |
| profile_get_banner_id | 350 # (profile_get_banner_id, <destination>), |
| profile_set_banner_id | 351 # (profile_set_banner_id, <value>), |
| get_achievement_stat | 370 # (get_achievement_stat, <destination>, <achievement_... |
| set_achievement_stat | 371 # (set_achievement_stat, <achievement_id>, <stat_inde... |
| unlock_achievement | 372 # (unlock_achievement, <achievement_id>), |
| send_message_to_url | 380 # (send_message_to_url, <string_id>, <encode_url>), #... |
| multiplayer_send_message_to_server | 388 # (multiplayer_send_int_to_server, <message_type>), |
| multiplayer_send_int_to_server | 389 # (multiplayer_send_int_to_server, <message_type>, <v... |
| multiplayer_send_2_int_to_server | 390 # (multiplayer_send_2_int_to_server, <message_type>, ... |
| multiplayer_send_3_int_to_server | 391 # (multiplayer_send_3_int_to_server, <message_type>, ... |
| multiplayer_send_4_int_to_server | 392 # (multiplayer_send_4_int_to_server, <message_type>, ... |
| multiplayer_send_string_to_server | 393 # (multiplayer_send_string_to_server, <message_type>,... |
| multiplayer_send_message_to_player | 394 # (multiplayer_send_message_to_player, <player_id>, <... |
| multiplayer_send_int_to_player | 395 # (multiplayer_send_int_to_player, <player_id>, <mess... |
| multiplayer_send_2_int_to_player | 396 # (multiplayer_send_2_int_to_player, <player_id>, <me... |
| multiplayer_send_3_int_to_player | 397 # (multiplayer_send_3_int_to_player, <player_id>, <me... |
| multiplayer_send_4_int_to_player | 398 # (multiplayer_send_4_int_to_player, <player_id>, <me... |
| multiplayer_send_string_to_player | 399 # (multiplayer_send_string_to_player, <player_id>, <m... |
| get_max_players | 400 # (get_max_players, <destination>), |
| player_is_active | 401 # (player_is_active, <player_id>), |
| player_get_team_no | 402 # (player_get_team_no,  <destination>, <player_id>), |
| player_set_team_no | 403 # (player_get_team_no,  <destination>, <player_id>), |
| player_get_troop_id | 404 # (player_get_troop_id, <destination>, <player_id>), |
| player_set_troop_id | 405 # (player_set_troop_id, <destination>, <player_id>), |
| player_get_agent_id | 406 # (player_get_agent_id, <destination>, <player_id>), |
| player_get_gold | 407 # (player_get_gold, <destination>, <player_id>), |
| player_set_gold | 408 # (player_set_gold, <player_id>, <value>, <max_value>... |
| player_spawn_new_agent | 409 # (player_spawn_new_agent, <player_id>, <entry_point>), |
| player_add_spawn_item | 410 # (player_add_spawn_item, <player_id>, <item_slot_no>... |
| multiplayer_get_my_team | 411 # (multiplayer_get_my_team, <destination>), |
| multiplayer_get_my_troop | 412 # (multiplayer_get_my_troop, <destination>), |
| multiplayer_set_my_troop | 413 # (multiplayer_get_my_troop, <destination>), |
| multiplayer_get_my_gold | 414 # (multiplayer_get_my_gold, <destination>), |
| multiplayer_get_my_player | 415 # (multiplayer_get_my_player, <destination>), |
| multiplayer_clear_scene | 416 # (multiplayer_clear_scene), |
| multiplayer_is_server | 417 # (multiplayer_is_server), |
| multiplayer_is_dedicated_server | 418 # (multiplayer_is_dedicated_server), |
| game_in_multiplayer_mode | 419 # (game_in_multiplayer_mode), |
| multiplayer_make_everyone_enemy | 420 # (multiplayer_make_everyone_enemy), |
| player_control_agent | 421 # (player_control_agent, <player_id>, <agent_id>), |
| player_get_item_id | 422 # (player_get_item_id, <destination>, <player_id>, <i... |
| player_get_banner_id | 423 # (player_get_banner_id, <destination>, <player_id>), |
| game_get_reduce_campaign_ai | 424 # (game_get_reduce_campaign_ai, <destination>), #depr... |
| multiplayer_find_spawn_point | 425 # (multiplayer_find_spawn_point, <destination>, <team... |
| set_spawn_effector_scene_prop_kind | 426 # (set_spawn_effector_scene_prop_kind <team_no> <scen... |
| set_spawn_effector_scene_prop_id | 427 # (set_spawn_effector_scene_prop_id <scene_prop_id>) |
| player_set_is_admin | 429 # (player_set_is_admin, <player_id>, <value>), #value... |
| player_is_admin | 430 # (player_is_admin, <player_id>), |
| player_get_score | 431 # (player_get_score, <destination>, <player_id>), |
| player_set_score | 432 # (player_set_score,<player_id>, <value>), |
| player_get_kill_count | 433 # (player_get_kill_count, <destination>, <player_id>), |
| player_set_kill_count | 434 # (player_set_kill_count,<player_id>, <value>), |
| player_get_death_count | 435 # (player_get_death_count, <destination>, <player_id>), |
| player_set_death_count | 436 # (player_set_death_count, <player_id>, <value>), |
| player_get_ping | 437 # (player_get_ping, <destination>, <player_id>), |
| player_is_busy_with_menus | 438 # (player_is_busy_with_menus, <player_id>), |
| player_get_is_muted | 439 # (player_get_is_muted, <destination>, <player_id>), |
| player_set_is_muted | 440 # (player_set_is_muted, <player_id>, <value>, [mute_f... |
| player_get_unique_id | 441 # (player_get_unique_id, <destination>, <player_id>),... |
| player_get_gender | 442 # (player_get_gender, <destination>, <player_id>), |
| team_get_bot_kill_count | 450 # (team_get_bot_kill_count, <destination>, <team_id>), |
| team_set_bot_kill_count | 451 # (team_get_bot_kill_count, <destination>, <team_id>), |
| team_get_bot_death_count | 452 # (team_get_bot_death_count, <destination>, <team_id>), |
| team_set_bot_death_count | 453 # (team_get_bot_death_count, <destination>, <team_id>), |
| team_get_kill_count | 454 # (team_get_kill_count, <destination>, <team_id>), |
| team_get_score | 455 # (team_get_score, <destination>, <team_id>), |
| team_set_score | 456 # (team_set_score, <team_id>, <value>), |
| team_set_faction | 457 # (team_set_faction, <team_id>, <faction_id>), |
| team_get_faction | 458 # (team_get_faction, <destination>, <team_id>), |
| player_save_picked_up_items_for_next_spawn | 459 # (player_save_picked_up_items_for_next_spawn, <playe... |
| player_get_value_of_original_items | 460 # (player_get_value_of_original_items, <player_id>), ... |
| player_item_slot_is_picked_up | 461 # (player_item_slot_is_picked_up, <player_id>, <item_... |
| kick_player | 465 # (kick_player, <player_id>), |
| ban_player | 466 # (ban_player, <player_id>, <value>, <player_id>), #s... |
| save_ban_info_of_player | 467 # (save_ban_info_of_player, <player_id>), |
| ban_player_using_saved_ban_info | 468 # (ban_player_using_saved_ban_info), |
| start_multiplayer_mission | 470 # (start_multiplayer_mission, <mission_template_id>, ... |
| server_add_message_to_log | 473 # (server_add_message_to_log, <string_id>), |
| server_get_renaming_server_allowed | 475 # (server_get_renaming_server_allowed, <destination>)... |
| server_get_changing_game_type_allowed | 476 # (server_get_changing_game_type_allowed, <destinatio... |
| server_get_combat_speed | 478 # (server_get_combat_speed, <destination>), #0-2 |
| server_set_combat_speed | 479 # (server_set_combat_speed, <value>), #0-2 |
| server_get_friendly_fire | 480 # (server_get_friendly_fire, <destination>), |
| server_set_friendly_fire | 481 # (server_set_friendly_fire, <value>), #0 = off, 1 = on |
| server_get_control_block_dir | 482 # (server_get_control_block_dir, <destination>), |
| server_set_control_block_dir | 483 # (server_set_control_block_dir, <value>), #0 = autom... |
| server_set_password | 484 # (server_set_password, <string_id>), |
| server_get_add_to_game_servers_list | 485 # (server_get_add_to_game_servers_list, <destination>), |
| server_set_add_to_game_servers_list | 486 # (server_set_add_to_game_servers_list, <value>), |
| server_get_ghost_mode | 487 # (server_get_ghost_mode, <destination>), |
| server_set_ghost_mode | 488 # (server_set_ghost_mode, <value>), |
| server_set_name | 489 # (server_set_name, <string_id>), |
| server_get_max_num_players | 490 # (server_get_max_num_players, <destination>), |
| server_set_max_num_players | 491 # (server_set_max_num_players, <value>), |
| server_set_welcome_message | 492 # (server_set_welcome_message, <string_id>), |
| server_get_melee_friendly_fire | 493 # (server_get_melee_friendly_fire, <destination>), |
| server_set_melee_friendly_fire | 494 # (server_set_melee_friendly_fire, <value>), #0 = off... |
| server_get_friendly_fire_damage_self_ratio | 495 # (server_get_friendly_fire_damage_self_ratio, <desti... |
| server_set_friendly_fire_damage_self_ratio | 496 # (server_set_friendly_fire_damage_self_ratio, <value... |
| server_get_friendly_fire_damage_friend_ratio | 497 # (server_get_friendly_fire_damage_friend_ratio, <des... |
| server_set_friendly_fire_damage_friend_ratio | 498 # (server_set_friendly_fire_damage_friend_ratio, <val... |
| server_get_anti_cheat | 499 # (server_get_anti_cheat, <destination>), |
| server_set_anti_cheat | 477 # (server_set_anti_cheat, <value>), #0 = off, 1 = on |
| troop_set_slot | 500 # (troop_set_slot,<troop_id>,<slot_no>,<value>), |
| party_set_slot | 501 # (party_set_slot,<party_id>,<slot_no>,<value>), |
| faction_set_slot | 502 # (faction_set_slot,<faction_id>,<slot_no>,<value>), |
| scene_set_slot | 503 # (scene_set_slot,<scene_id>,<slot_no>,<value>), |
| party_template_set_slot | 504 # (party_template_set_slot,<party_template_id>,<slot_... |
| agent_set_slot | 505 # (agent_set_slot,<agent_id>,<slot_no>,<value>), |
| quest_set_slot | 506 # (quest_set_slot,<quest_id>,<slot_no>,<value>), |
| item_set_slot | 507 # (item_set_slot,<item_id>,<slot_no>,<value>), |
| player_set_slot | 508 # (player_set_slot,<player_id>,<slot_no>,<value>), |
| team_set_slot | 509 # (team_set_slot,<team_id>,<slot_no>,<value>), |
| scene_prop_set_slot | 510 # (scene_prop_set_slot,<scene_prop_instance_id>,<slot... |
| troop_get_slot | 520 # (troop_get_slot,<destination>,<troop_id>,<slot_no>), |
| party_get_slot | 521 # (party_get_slot,<destination>,<party_id>,<slot_no>), |
| faction_get_slot | 522 # (faction_get_slot,<destination>,<faction_id>,<slot_... |
| scene_get_slot | 523 # (scene_get_slot,<destination>,<scene_id>,<slot_no>), |
| party_template_get_slot | 524 # (party_template_get_slot,<destination>,<party_templ... |
| agent_get_slot | 525 # (agent_get_slot,<destination>,<agent_id>,<slot_no>), |
| quest_get_slot | 526 # (quest_get_slot,<destination>,<quest_id>,<slot_no>), |
| item_get_slot | 527 # (item_get_slot,<destination>,<item_id>,<slot_no>), |
| player_get_slot | 528 # (player_get_slot,<destination>,<player_id>,<slot_no>), |
| team_get_slot | 529 # (team_get_slot,<destination>,<player_id>,<slot_no>), |
| scene_prop_get_slot | 530 # (scene_prop_get_slot,<destination>,<scene_prop_inst... |
| troop_slot_eq | 540 # (troop_slot_eq,<troop_id>,<slot_no>,<value>), |
| party_slot_eq | 541 # (party_slot_eq,<party_id>,<slot_no>,<value>), |
| faction_slot_eq | 542 # (faction_slot_eq,<faction_id>,<slot_no>,<value>), |
| scene_slot_eq | 543 # (scene_slot_eq,<scene_id>,<slot_no>,<value>), |
| party_template_slot_eq | 544 # (party_template_slot_eq,<party_template_id>,<slot_n... |
| agent_slot_eq | 545 # (agent_slot_eq,<agent_id>,<slot_no>,<value>), |
| quest_slot_eq | 546 # (quest_slot_eq,<quest_id>,<slot_no>,<value>), |
| item_slot_eq | 547 # (item_slot_eq,<item_id>,<slot_no>,<value>), |
| player_slot_eq | 548 # (player_slot_eq,<player_id>,<slot_no>,<value>), |
| team_slot_eq | 549 # (team_slot_eq,<team_id>,<slot_no>,<value>), |
| scene_prop_slot_eq | 550 # (scene_prop_slot_eq,<scene_prop_instance_id>,<slot_... |
| troop_slot_ge | 560 # (troop_slot_ge,<troop_id>,<slot_no>,<value>), |
| party_slot_ge | 561 # (party_slot_ge,<party_id>,<slot_no>,<value>), |
| faction_slot_ge | 562 # (faction_slot_ge,<faction_id>,<slot_no>,<value>), |
| scene_slot_ge | 563 # (scene_slot_ge,<scene_id>,<slot_no>,<value>), |
| party_template_slot_ge | 564 # (party_template_slot_ge,<party_template_id>,<slot_n... |
| agent_slot_ge | 565 # (agent_slot_ge,<agent_id>,<slot_no>,<value>), |
| quest_slot_ge | 566 # (quest_slot_ge,<quest_id>,<slot_no>,<value>), |
| item_slot_ge | 567 # (item_slot_ge,<item_id>,<slot_no>,<value>), |
| player_slot_ge | 568 # (player_slot_ge,<player_id>,<slot_no>,<value>), |
| team_slot_ge | 569 # (team_slot_ge,<team_id>,<slot_no>,<value>), |
| scene_prop_slot_ge | 570 # (scene_prop_slot_ge,<scene_prop_instance_id>,<slot_... |
| play_sound_at_position | 599 # (play_sound_at_position, <sound_id>, <position_no>,... |
| play_sound | 600 # (play_sound,<sound_id>,[options]), |
| play_track | 601 # (play_track,<track_id>, [options]), # 0 = default, ... |
| play_cue_track | 602 # (play_cue_track,<track_id>), #starts immediately |
| music_set_situation | 603 # (music_set_situation, <situation_type>), |
| music_set_culture | 604 # (music_set_culture, <culture_type>), |
| stop_all_sounds | 609 # (stop_all_sounds, [options]), # 0 = stop only loopi... |
| store_last_sound_channel | 615 # (store_last_sound_channel, <destination>), |
| stop_sound_channel | 616 # (stop_sound_channel, <sound_channel_no>), |
| copy_position | 700 # copies position_no_2 to position_no_1 |
| init_position | 701 # (init_position,<position_no>), |
| get_trigger_object_position | 702 # (get_trigger_object_position,<position_no>), |
| get_angle_between_positions | 705 # (get_angle_between_positions, <destination_fixed_po... |
| position_has_line_of_sight_to_position | 707 # (position_has_line_of_sight_to_position, <position_... |
| get_distance_between_positions | 710 # gets distance in centimeters. # (get_distance_betwe... |
| get_distance_between_positions_in_meters | 711 # gets distance in meters. # (get_distance_between_po... |
| get_sq_distance_between_positions | 712 # gets squared distance in centimeters # (get_sq_dist... |
| get_sq_distance_between_positions_in_meters | 713 # gets squared distance in meters # (get_sq_distance_... |
| position_is_behind_position | 714 # (position_is_behind_position,<position_no_1>,<posit... |
| get_sq_distance_between_position_heights | 715 # gets squared distance in centimeters # (get_sq_dist... |
| position_transform_position_to_parent | 716 # (position_transform_position_to_parent,<dest_positi... |
| position_transform_position_to_local | 717 # (position_transform_position_to_local, <dest_positi... |
| position_copy_rotation | 718 # (position_copy_rotation,<position_no_1>,<position_n... |
| position_copy_origin | 719 # (position_copy_origin,<position_no_1>,<position_no_... |
| position_move_x | 720 # movement is in cms, [0 = local; 1=global] |
| position_move_y | 721 # (position_move_y,<position_no>,<movement>,[value]), |
| position_move_z | 722 # (position_move_z,<position_no>,<movement>,[value]), |
| position_rotate_x | 723 # (position_rotate_x,<position_no>,<angle>), |
| position_rotate_y | 724 # (position_rotate_y,<position_no>,<angle>), |
| position_rotate_z | 725 # (position_rotate_z,<position_no>,<angle>,[use_globa... |
| position_get_x | 726 # (position_get_x,<destination_fixed_point>,<position... |
| position_get_y | 727 # (position_get_y,<destination_fixed_point>,<position... |
| position_get_z | 728 # (position_get_z,<destination_fixed_point>,<position... |
| position_set_x | 729 # (position_set_x,<position_no>,<value_fixed_point>),... |
| position_set_y | 730 # (position_set_y,<position_no>,<value_fixed_point>),... |
| position_set_z | 731 # (position_set_z,<position_no>,<value_fixed_point>),... |
| position_get_scale_x | 735 # (position_get_scale_x,<destination_fixed_point>,<po... |
| position_get_scale_y | 736 # (position_get_scale_y,<destination_fixed_point>,<po... |
| position_get_scale_z | 737 # (position_get_scale_z,<destination_fixed_point>,<po... |
| position_rotate_x_floating | 738 # (position_rotate_x_floating,<position_no>,<angle>),... |
| position_rotate_y_floating | 739 # (position_rotate_y_floating,<position_no>,<angle>),... |
| position_rotate_z_floating | 734 # (position_rotate_z_floating,<position_no>,<angle>),... |
| position_get_rotation_around_z | 740 # (position_get_rotation_around_z,<destination>,<posi... |
| position_normalize_origin | 741 # (position_normalize_origin,<destination_fixed_point... |
| position_get_rotation_around_x | 742 # (position_get_rotation_around_x, <destination>, <po... |
| position_get_rotation_around_y | 743 # (position_get_rotation_around_y, <destination>, <po... |
| position_set_scale_x | 744 # (position_set_scale_x, <position_no>, <value_fixed_... |
| position_set_scale_y | 745 # (position_set_scale_y, <position_no>, <value_fixed_... |
| position_set_scale_z | 746 # (position_set_scale_z, <position_no>, <value_fixed_... |
| position_get_screen_projection | 750 # (position_get_screen_projection, <position_no_1>, <... |
| mouse_get_world_projection | 751 # (mouse_get_world_projection, <position_no_1>, <posi... |
| position_set_z_to_ground_level | 791 # (position_set_z_to_ground_level, <position_no>), #o... |
| position_get_distance_to_terrain | 792 # (position_get_distance_to_terrain, <destination_fix... |
| position_get_distance_to_ground_level | 793 # (position_get_distance_to_ground_level, <destinatio... |
| start_presentation | 900 # (start_presentation, <presentation_id>), |
| start_background_presentation | 901 # (start_background_presentation, <presentation_id>),... |
| presentation_set_duration | 902 # (presentation_set_duration, <duration-in-1/100-seco... |
| is_presentation_active | 903 # (is_presentation_active, <presentation_id), |
| create_text_overlay | 910 # (create_text_overlay, <destination>, <string_id>), ... |
| create_mesh_overlay | 911 # (create_mesh_overlay, <destination>, <mesh_id>), #r... |
| create_button_overlay | 912 # (create_button_overlay, <destination>, <string_id>)... |
| create_image_button_overlay | 913 # (create_image_button_overlay, <destination>, <mesh_... |
| create_slider_overlay | 914 # (create_slider_overlay, <destination>, <min_value>,... |
| create_progress_overlay | 915 # (create_progress_overlay, <destination>, <min_value... |
| create_combo_button_overlay | 916 # (create_combo_button_overlay, <destination>), #retu... |
| create_text_box_overlay | 917 # (create_text_box_overlay, <destination>), #returns ... |
| create_check_box_overlay | 918 # (create_check_box_overlay, <destination>), #returns... |
| create_simple_text_box_overlay | 919 # (create_simple_text_box_overlay, <destination>), #r... |
| overlay_set_text | 920 # (overlay_set_text, <overlay_id>, <string_id>), |
| overlay_set_color | 921 # (overlay_set_color, <overlay_id>, <color>), #color ... |
| overlay_set_alpha | 922 # (overlay_set_alpha, <overlay_id>, <alpha>), #alpha ... |
| overlay_set_hilight_color | 923 # (overlay_set_hilight_color, <overlay_id>, <color>),... |
| overlay_set_hilight_alpha | 924 # (overlay_set_hilight_alpha, <overlay_id>, <alpha>),... |
| overlay_set_size | 925 # (overlay_set_size, <overlay_id>, <position_no>), #p... |
| overlay_set_position | 926 # (overlay_set_position, <overlay_id>, <position_no>)... |
| overlay_set_val | 927 # (overlay_set_val, <overlay_id>, <value>), #can be u... |
| overlay_set_boundaries | 928 # (overlay_set_boundaries, <overlay_id>, <min_value>,... |
| overlay_set_area_size | 929 # (overlay_set_area_size, <overlay_id>, <position_no>... |
| overlay_set_mesh_rotation | 930 # (overlay_set_mesh_rotation, <overlay_id>, <position... |
| overlay_add_item | 931 # (overlay_add_item, <overlay_id>, <string_id>), # ad... |
| overlay_animate_to_color | 932 # (overlay_animate_to_color, <overlay_id>, <duration-... |
| overlay_animate_to_alpha | 933 # (overlay_animate_to_alpha, <overlay_id>, <duration-... |
| overlay_animate_to_highlight_color | 934 # (overlay_animate_to_highlight_color, <overlay_id>, ... |
| overlay_animate_to_highlight_alpha | 935 # (overlay_animate_to_highlight_alpha, <overlay_id>, ... |
| overlay_animate_to_size | 936 # (overlay_animate_to_size, <overlay_id>, <duration-i... |
| overlay_animate_to_position | 937 # (overlay_animate_to_position, <overlay_id>, <durati... |
| create_image_button_overlay_with_tableau_material | 938 # (create_image_button_overlay_with_tableau_material,... |
| create_mesh_overlay_with_tableau_material | 939 # (create_mesh_overlay_with_tableau_material, <destin... |
| create_game_button_overlay | 940 # (create_game_button_overlay, <destination>, <string... |
| create_in_game_button_overlay | 941 # (create_in_game_button_overlay, <destination>, <str... |
| create_number_box_overlay | 942 # (create_number_box_overlay, <destination>, <min_val... |
| create_listbox_overlay | 943 # (create_list_box_overlay, <destination>), #returns ... |
| create_mesh_overlay_with_item_id | 944 # (create_mesh_overlay_with_item_id, <destination>, <... |
| set_container_overlay | 945 # (set_container_overlay, <overlay_id>), #sets the co... |
| overlay_get_position | 946 # (overlay_get_position, <destination>, <overlay_id>), |
| overlay_set_display | 947 # (overlay_set_display, <overlay_id>, <value>), #show... |
| create_combo_label_overlay | 948 # (create_combo_label_overlay, <destination>), #retur... |
| overlay_obtain_focus | 949 # (overlay_obtain_focus, <overlay_id>), #works for te... |
| overlay_set_tooltip | 950 # (overlay_set_tooltip, <overlay_id>, <string_id>), |
| overlay_set_container_overlay | 951 # (overlay_set_container_overlay, <overlay_id>, <cont... |
| overlay_set_additional_render_height | 952 # (overlay_set_additional_render_height, <overlay_id>... |
| overlay_set_material | 956 # (overlay_set_material, <overlay_id>, <string_no>), |
| show_object_details_overlay | 960 # (show_object_details_overlay, <value>), #0 = hide, ... |
| show_item_details | 970 # (show_item_details, <item_id>, <position_no>, <pric... |
| close_item_details | 971 # (close_item_details), |
| show_item_details_with_modifier | 972 # (show_item_details_with_modifier, <item_id>, <item_... |
| context_menu_add_item | 980 # (right_mouse_menu_add_item, <string_id>, <value>), ... |
| auto_save | 985 # (auto_save), |
| allow_ironman | 988 # (allow_ironman, <value>), # 1 = allow, 0 = disallow |
| get_average_game_difficulty | 990 # (get_average_game_difficulty, <destination>), |
| get_level_boundary | 991 # (get_level_boundary, <destination>, <level_no>), |
| all_enemies_defeated | 1003 # (all_enemies_defeated), |
| race_completed_by_player | 1004 # (race_completed_by_player), |
| num_active_teams_le | 1005 # (num_active_teams_le,<value>), |
| main_hero_fallen | 1006 # (main_hero_fallen), |
| neg | 0x80000000	 # (neg|<operation>), |
| this_or_next | 0x40000000	 # (this_or_next|<operation>), |
| lt | neg | ge # less than		-- (lt,<value>,<value>), |
| neq | neg | eq # not equal to		-- (neq,<value>,<value>), |
| le | neg | gt # less or equal to	-- (le,<value>,<value>), |
| finish_party_battle_mode | 1019 # (finish_party_battle_mode), |
| set_party_battle_mode | 1020 # (set_party_battle_mode), |
| set_camera_follow_party | 1021 # (set_camera_follow_party,<party_id>), #Works on ma... |
| start_map_conversation | 1025 # (start_map_conversation,<troop_id>), |
| rest_for_hours | 1030 # (rest_for_hours,<rest_period>,[time_speed],[remain... |
| rest_for_hours_interactive | 1031 # (rest_for_hours_interactive,<rest_period>,[time_sp... |
| add_xp_to_troop | 1062 # (add_xp_to_troop,<value>,[troop_id]), |
| add_gold_as_xp | 1063 # (add_gold_as_xp,<value>,[troop_id]), |
| add_xp_as_reward | 1064 # (add_xp_as_reward,<value>), |
| add_gold_to_party | 1070 # party_id should be different from 0 |
| set_party_creation_random_limits | 1080 # (set_party_creation_random_limits, <min_value>, <m... |
| troop_set_note_available | 1095 # (troop_set_note_available, <troop_id>, <value>), #... |
| faction_set_note_available | 1096 # (faction_set_note_available, <faction_id>, <value>... |
| party_set_note_available | 1097 # (party_set_note_available, <party_id>, <value>), #... |
| quest_set_note_available | 1098 # (quest_set_note_available, <quest_id>, <value>), #... |
| spawn_around_party | 1100 # ID of spawned party is put into reg(0) |
| set_spawn_radius | 1103 # (set_spawn_radius,<value>), |
| display_debug_message | 1104 # (display_debug_message,<string_id>,[hex_colour_cod... |
| display_log_message | 1105 # (display_log_message,<string_id>,[hex_colour_code]), |
| display_message | 1106 # (display_message,<string_id>,[hex_colour_code]), |
| set_show_messages | 1107 # (set_show_messages,<value>), #0 disables window me... |
| add_troop_note_tableau_mesh | 1108 # (add_troop_note_tableau_mesh,<troop_id>,<tableau_m... |
| add_faction_note_tableau_mesh | 1109 # (add_faction_note_tableau_mesh,<faction_id>,<table... |
| add_party_note_tableau_mesh | 1110 # (add_party_note_tableau_mesh,<party_id>,<tableau_m... |
| add_quest_note_tableau_mesh | 1111 # (add_quest_note_tableau_mesh,<quest_id>,<tableau_m... |
| add_info_page_note_tableau_mesh | 1090 # (add_info_page_note_tableau_mesh,<info_page_id>,<t... |
| add_troop_note_from_dialog | 1114 # (add_troop_note_from_dialog,<troop_id>,<note_slot_... |
| add_faction_note_from_dialog | 1115 # (add_faction_note_from_dialog,<faction_id>,<note_s... |
| add_party_note_from_dialog | 1116 # (add_party_note_from_dialog,<party_id>,<note_slot_... |
| add_quest_note_from_dialog | 1112 # (add_quest_note_from_dialog,<quest_id>,<note_slot_... |
| add_info_page_note_from_dialog | 1091 # (add_info_page_note_from_dialog,<info_page_id>,<no... |
| add_troop_note_from_sreg | 1117 # (add_troop_note_from_sreg,<troop_id>,<note_slot_no... |
| add_faction_note_from_sreg | 1118 # (add_faction_note_from_sreg,<faction_id>,<note_slo... |
| add_party_note_from_sreg | 1119 # (add_party_note_from_sreg,<party_id>,<note_slot_no... |
| add_quest_note_from_sreg | 1113 # (add_quest_note_from_sreg,<quest_id>,<note_slot_no... |
| add_info_page_note_from_sreg | 1092 # (add_info_page_note_from_sreg,<info_page_id>,<note... |
| tutorial_box | 1120 # (tutorial_box,<string_id>,<string_id>), #deprecate... |
| dialog_box | 1120 # (dialog_box,<text_string_id>,<title_string_id>), |
| question_box | 1121 # (question_box,<string_id>, [<yes_string_id>], [<no... |
| tutorial_message | 1122 # (tutorial_message,<string_id>, <color>, <auto_clos... |
| tutorial_message_set_position | 1123 # (tutorial_message_set_position, <position_x>, <pos... |
| tutorial_message_set_size | 1124 # (tutorial_message_set_size, <size_x>, <size_y>), |
| tutorial_message_set_center_justify | 1125 # (tutorial_message_set_center_justify, <val>), #set... |
| tutorial_message_set_background | 1126 # (tutorial_message_set_background, <value>), #1 = o... |
| set_tooltip_text | 1130 #  (set_tooltip_text, <string_id>), |
| reset_price_rates | 1170 # (reset_price_rates), |
| set_price_rate_for_item | 1171 # (set_price_rate_for_item,<item_id>,<value_percenta... |
| set_price_rate_for_item_type | 1172 # (set_price_rate_for_item_type,<item_type_id>,<valu... |
| party_join | 1201 # (party_join), |
| party_join_as_prisoner | 1202 # (party_join_as_prisoner), |
| troop_join | 1203 # (troop_join,<troop_id>), |
| troop_join_as_prisoner | 1204 # (troop_join_as_prisoner,<troop_id>), |
| remove_member_from_party | 1210 # (remove_member_from_party,<troop_id>,[party_id]), |
| remove_regular_prisoners | 1211 # (remove_regular_prisoners,<party_id>), |
| remove_troops_from_companions | 1215 # (remove_troops_from_companions,<troop_id>,<value>), |
| remove_troops_from_prisoners | 1216 # (remove_troops_from_prisoners,<troop_id>,<value>), |
| heal_party | 1225 # (heal_party,<party_id>), |
| disable_party | 1230 # (disable_party,<party_id>), |
| enable_party | 1231 # (enable_party,<party_id>), |
| remove_party | 1232 # (remove_party,<party_id>), #remove only active spa... |
| add_companion_party | 1233 # (add_companion_party,<troop_id_hero>), |
| add_troop_to_site | 1250 # (add_troop_to_site,<troop_id>,<scene_id>,<entry_no>), |
| remove_troop_from_site | 1251 # (remove_troop_from_site,<troop_id>,<scene_id>), |
| modify_visitors_at_site | 1261 # (modify_visitors_at_site,<scene_id>), |
| reset_visitors | 1262 # (reset_visitors), |
| set_visitor | 1263 # (set_visitor,<entry_no>,<troop_id>,[<dna>]), |
| set_visitors | 1264 # (set_visitors,<entry_no>,<troop_id>,<number_of_tro... |
| add_visitors_to_current_scene | 1265 # (add_visitors_to_current_scene,<entry_no>,<troop_i... |
| scene_set_day_time | 1266 # (scene_set_day_time, <value>), #value in hours (0-... |
| set_relation | 1270 # (set_relation,<faction_id>,<faction_id>,<value>), |
| faction_set_name | 1275 # (faction_set_name, <faction_id>, <string_id>), |
| faction_set_color | 1276 # (faction_set_color, <faction_id>, <value>), |
| faction_get_color | 1277 # (faction_get_color, <color>, <faction_id>) |
| start_quest | 1280 # (start_quest,<quest_id>), |
| complete_quest | 1281 # (complete_quest,<quest_id>), |
| succeed_quest | 1282 # (succeed_quest,<quest_id>), #also concludes the quest |
| fail_quest | 1283 # (fail_quest,<quest_id>), #also concludes the quest |
| cancel_quest | 1284 # (cancel_quest,<quest_id>), |
| set_quest_progression | 1285 # (set_quest_progression,<quest_id>,<value>), |
| conclude_quest | 1286 # (conclude_quest,<quest_id>), |
| setup_quest_text | 1290 # (setup_quest_text,<quest_id>), |
| setup_quest_giver | 1291 # (setup_quest_giver,<quest_id>, <string_id>), |
| start_encounter | 1300 # (start_encounter,<party_id>), |
| leave_encounter | 1301 # (leave_encounter), |
| encounter_attack | 1302 # (encounter_attack), |
| select_enemy | 1303 # (select_enemy,<value>), |
| set_passage_menu | 1304 # (set_passage_menu,<value>), |
| auto_set_meta_mission_at_end_commited | 1305 # (auto_set_meta_mission_at_end_commited), |
| end_current_battle | 1307 # (end_current_battle), |
| set_mercenary_source_party | 1320 # selects party from which to buy mercenaries |
| set_merchandise_modifier_quality | 1490	        # Quality rate in percentage (average qualit... |
| set_merchandise_max_value | 1491		# (set_merchandise_max_value,<value>), |
| reset_item_probabilities | 1492		        # (reset_item_probabilities), |
| set_item_probability_in_merchandise | 1493	# (set_item_probability_in_merchandise,<itm_id>,<val... |
| troop_set_name | 1501   # (troop_set_name, <troop_id>, <string_no>), |
| troop_set_plural_name | 1502   # (troop_set_plural_name, <troop_id>, <string_no>), |
| troop_set_face_key_from_current_profile | 1503   # (troop_set_face_key_from_current_profile, <troop... |
| troop_set_type | 1505	# (troop_set_type,<troop_id>,<gender>), |
| troop_get_type | 1506   # (troop_get_type,<destination>,<troop_id>), |
| troop_is_hero | 1507   # (troop_is_hero,<troop_id>), |
| troop_is_wounded | 1508   # (troop_is_wounded,<troop_id>), #only for heroes! |
| troop_set_auto_equip | 1509   # (troop_set_auto_equip,<troop_id>,<value>),#disab... |
| troop_ensure_inventory_space | 1510	# (troop_ensure_inventory_space,<troop_id>,<value>), |
| troop_sort_inventory | 1511	# (troop_sort_inventory,<troop_id>), |
| troop_add_merchandise | 1512	# (troop_add_merchandise,<troop_id>,<item_type_id>,<... |
| troop_add_merchandise_with_faction | 1513	# (troop_add_merchandise_with_faction,<troop_id>,<fa... |
| troop_get_xp | 1515   # (troop_get_xp, <destination>, <troop_id>), |
| troop_get_class | 1516   # (troop_get_class, <destination>, <troop_id>), |
| troop_set_class | 1517 # (troop_set_class, <troop_id>, <value>), |
| troop_raise_attribute | 1520	# (troop_raise_attribute,<troop_id>,<attribute_id>,<... |
| troop_raise_skill | 1521	# (troop_raise_skill,<troop_id>,<skill_id>,<value>), |
| troop_raise_proficiency | 1522	# (troop_raise_proficiency,<troop_id>,<proficiency_n... |
| troop_raise_proficiency_linear | 1523	# raises weapon proficiencies linearly without being... |
| troop_add_proficiency_points | 1525   # (troop_add_proficiency_points,<troop_id>,<value>), |
| troop_add_gold | 1528	# (troop_add_gold,<troop_id>,<value>), |
| troop_remove_gold | 1529	# (troop_remove_gold,<troop_id>,<value>), |
| troop_add_item | 1530	# (troop_add_item,<troop_id>,<item_id>,[modifier]), |
| troop_remove_item | 1531	# (troop_remove_item,<troop_id>,<item_id>), |
| troop_clear_inventory | 1532	# (troop_clear_inventory,<troop_id>), |
| troop_equip_items | 1533   # (troop_equip_items,<troop_id>), #equips the item... |
| troop_inventory_slot_set_item_amount | 1534   # (troop_inventory_slot_set_item_amount,<troop_id>... |
| troop_inventory_slot_get_item_amount | 1537   # (troop_inventory_slot_get_item_amount,<destinati... |
| troop_inventory_slot_get_item_max_amount | 1538  # (troop_inventory_slot_get_item_max_amount,<destin... |
| troop_add_items | 1535	# (troop_add_items,<troop_id>,<item_id>,<number>), |
| troop_remove_items | 1536	# puts cost of items to reg0 |
| troop_loot_troop | 1539	# (troop_loot_troop,<target_troop>,<source_troop_id>... |
| troop_get_inventory_capacity | 1540	# (troop_get_inventory_capacity,<destination>,<troop... |
| troop_get_inventory_slot | 1541	# (troop_get_inventory_slot,<destination>,<troop_id>... |
| troop_get_inventory_slot_modifier | 1542	# (troop_get_inventory_slot_modifier,<destination>,<... |
| troop_set_inventory_slot | 1543	# (troop_set_inventory_slot,<troop_id>,<inventory_sl... |
| troop_set_inventory_slot_modifier | 1544	# (troop_set_inventory_slot_modifier,<troop_id>,<inv... |
| troop_set_faction | 1550 # (troop_set_faction,<troop_id>,<faction_id>), |
| troop_set_age | 1555 # (troop_set_age, <troop_id>, <age_slider_pos>),  #E... |
| troop_set_health | 1560	# (troop_set_health,<troop_id>,<relative health (0-1... |
| troop_get_upgrade_troop | 1561   # (troop_get_upgrade_troop,<destination>,<troop_id... |
| item_get_type | 1570   # (item_get_type, <destination>, <item_id>), #retu... |
| party_get_num_companions | 1601	# (party_get_num_companions,<destination>,<party_id>), |
| party_get_num_prisoners | 1602	# (party_get_num_prisoners,<destination>,<party_id>), |
| party_set_flags | 1603   # (party_set_flags, <party_id>, <flag>, <clear_or_... |
| party_set_marshall | 1604   # (party_set_marshal, <party_id>, <value>) |
| party_set_extra_text | 1605   # (party_set_extra_text,<party_id>, <string>) |
| party_set_aggressiveness | 1606   # (party_set_aggressiveness, <party_id>, <number>), |
| party_set_courage | 1607   # (party_set_courage, <party_id>, <number>), |
| party_get_current_terrain | 1608	# (party_get_current_terrain,<destination>,<party_id>), |
| party_get_template_id | 1609	# (party_get_template_id,<destination>,<party_id>), |
| party_add_members | 1610	# (party_add_members,<party_id>,<troop_id>,<number>)... |
| party_add_prisoners | 1611	# (party_add_prisoners,<party_id>,<troop_id>,<number... |
| party_add_leader | 1612	# (party_add_leader,<party_id>,<troop_id>,[<number>]), |
| party_force_add_members | 1613	# (party_force_add_members,<party_id>,<troop_id>,<nu... |
| party_force_add_prisoners | 1614	# (party_force_add_prisoners,<party_id>,<troop_id>,<... |
| party_remove_members | 1615	# stores number removed to reg0 |
| party_remove_prisoners | 1616	# stores number removed to reg0 |
| party_clear | 1617	# (party_clear,<party_id>), |
| party_wound_members | 1618	# (party_wound_members,<party_id>,<troop_id>,<number>), |
| party_remove_members_wounded_first | 1619	# stores number removed to reg0 |
| party_set_faction | 1620	# (party_set_faction,<party_id>,<faction_id>), |
| party_relocate_near_party | 1623	# (party_relocate_near_party,<party_id>,<target_part... |
| party_get_position | 1625	# (party_get_position,<position_no>,<party_id>), |
| party_set_position | 1626	# (party_set_position,<party_id>,<position_no>), |
| map_get_random_position_around_position | 1627	# (map_get_random_position_around_position,<dest_pos... |
| map_get_land_position_around_position | 1628	# (map_get_land_position_around_position,<dest_posit... |
| map_get_water_position_around_position | 1629	# (map_get_water_position_around_position,<dest_posi... |
| party_count_members_of_type | 1630	# (party_count_members_of_type,<destination>,<party_... |
| party_count_companions_of_type | 1631	# (party_count_companions_of_type,<destination>,<par... |
| party_count_prisoners_of_type | 1632	# (party_count_prisoners_of_type,<destination>,<part... |
| party_get_free_companions_capacity | 1633   # (party_get_free_companions_capacity,<destination... |
| party_get_free_prisoners_capacity | 1634   # (party_get_free_prisoners_capacity,<destination>... |
| party_get_ai_initiative | 1638	# (party_get_ai_initiative,<destination>,<party_id>)... |
| party_set_ai_initiative | 1639	# (party_set_ai_initiative,<party_id>,<value>), #val... |
| party_set_ai_behavior | 1640	# (party_set_ai_behavior,<party_id>,<ai_bhvr>), |
| party_set_ai_object | 1641	# (party_set_ai_object,<party_id>,<party_id>), |
| party_set_ai_target_position | 1642	# (party_set_ai_target_position,<party_id>,<position... |
| party_set_ai_patrol_radius | 1643	# (party_set_ai_patrol_radius,<party_id>,<radius_in_... |
| party_ignore_player | 1644   # (party_ignore_player, <party_id>,<duration_in_ho... |
| party_set_bandit_attraction | 1645   # (party_set_bandit_attraction, <party_id>,<attara... |
| party_get_helpfulness | 1646   # (party_get_helpfulness,<destination>,<party_id>), |
| party_set_helpfulness | 1647   # (party_set_helpfulness, <party_id>, <number>), #... |
| party_set_ignore_with_player_party | 1648   # (party_set_ignore_with_player_party, <party_id>,... |
| party_get_ignore_with_player_party | 1649   # (party_get_ignore_with_player_party, <party_id>), |
| party_get_num_companion_stacks | 1650   # (party_get_num_companion_stacks,<destination>,<p... |
| party_get_num_prisoner_stacks | 1651   # (party_get_num_prisoner_stacks, <destination>,<p... |
| party_stack_get_troop_id | 1652   # (party_stack_get_troop_id,      <destination>,<p... |
| party_stack_get_size | 1653   # (party_stack_get_size,          <destination>,<p... |
| party_stack_get_num_wounded | 1654   # (party_stack_get_num_wounded,   <destination>,<p... |
| party_stack_get_troop_dna | 1655   # (party_stack_get_troop_dna,     <destination>,<p... |
| party_prisoner_stack_get_troop_id | 1656   # (party_get_prisoner_stack_troop,<destination>,<p... |
| party_prisoner_stack_get_size | 1657   # (party_get_prisoner_stack_size, <destination>,<p... |
| party_prisoner_stack_get_troop_dna | 1658   # (party_prisoner_stack_get_troop_dna, <destinatio... |
| party_attach_to_party | 1660   # (party_attach_to_party, <party_id>, <party_id to... |
| party_detach | 1661   # (party_detach, <party_id>), |
| party_collect_attachments_to_party | 1662   # (party_collect_attachments_to_party, <party_id>,... |
| party_quick_attach_to_current_battle | 1663   # (party_quick_attach_to_current_battle, <party_id... |
| party_get_cur_town | 1665   # (party_get_cur_town, <destination>, <party_id>), |
| party_leave_cur_battle | 1666   # (party_leave_cur_battle, <party_id>), |
| party_set_next_battle_simulation_time | 1667   # (party_set_next_battle_simulation_time,<party_id... |
| party_set_name | 1669   # (party_set_name, <party_id>, <string_no>), |
| party_add_xp_to_stack | 1670   # (party_add_xp_to_stack, <party_id>, <stack_no>, ... |
| party_get_morale | 1671   # (party_get_morale, <destination>,<party_id>), |
| party_set_morale | 1672   # (party_set_morale, <party_id>, <value>), #value ... |
| party_upgrade_with_xp | 1673   # (party_upgrade_with_xp, <party_id>, <xp_amount>,... |
| party_add_xp | 1674   # (party_add_xp, <party_id>, <xp_amount>), |
| party_add_template | 1675   # (party_add_template, <party_id>, <party_template... |
| party_set_icon | 1676   # (party_set_icon, <party_id>, <map_icon_id>), |
| party_set_banner_icon | 1677   # (party_set_banner_icon, <party_id>, <map_icon_id>), |
| party_add_particle_system | 1678   # (party_add_particle_system, <party_id>, <particl... |
| party_clear_particle_systems | 1679   # (party_clear_particle_systems, <party_id>), |
| party_get_battle_opponent | 1680   # (party_get_battle_opponent, <destination>, <part... |
| party_get_icon | 1681   # (party_get_icon, <destination>, <party_id>), |
| party_set_extra_icon | 1682   # (party_set_extra_icon, <party_id>, <map_icon_id>... |
| party_get_skill_level | 1685   # (party_get_skill_level, <destination>, <party_id... |
| agent_get_speed | 1689   # (agent_get_speed, <position_no>, <agent_id>), #w... |
| get_battle_advantage | 1690   # (get_battle_advantage, <destination>), |
| set_battle_advantage | 1691   # (set_battle_advantage, <value>), |
| agent_refill_wielded_shield_hit_points | 1692   # (agent_refill_wielded_shield_hit_points, <agent_... |
| agent_is_in_special_mode | 1693   # (agent_is_in_special_mode,<agent_id>), |
| party_get_attached_to | 1694   # (party_get_attached_to, <destination>, <party_id>), |
| party_get_num_attached_parties | 1695   # (party_get_num_attached_parties, <destination>, ... |
| party_get_attached_party_with_rank | 1696   # (party_get_attached_party_with_rank, <destinatio... |
| inflict_casualties_to_party_group | 1697   # (inflict_casualties_to_party, <parent_party_id>,... |
| distribute_party_among_party_group | 1698   # (distribute_party_among_party_group, <party_to_b... |
| agent_is_routed | 1699   # (agent_is_routed,<agent_id>), |
| get_player_agent_no | 1700	# (get_player_agent_no,<destination>), |
| get_player_agent_kill_count | 1701	# (get_player_agent_kill_count,<destination>,[get_wo... |
| agent_is_alive | 1702	# (agent_is_alive,<agent_id>), |
| agent_is_wounded | 1703	# (agent_is_wounded,<agent_id>), |
| agent_is_human | 1704	# (agent_is_human,<agent_id>), |
| get_player_agent_own_troop_kill_count | 1705   # (get_player_agent_own_troop_kill_count,<destinat... |
| agent_is_ally | 1706	# (agent_is_ally,<agent_id>), |
| agent_is_non_player | 1707   # (agent_is_non_player, <agent_id>), |
| agent_is_defender | 1708	# (agent_is_defender,<agent_id>), |
| agent_is_active | 1712   # (agent_is_active,<agent_id>), |
| agent_get_look_position | 1709   # (agent_get_look_position, <position_no>, <agent_... |
| agent_get_position | 1710	# (agent_get_position,<position_no>,<agent_id>), |
| agent_set_position | 1711	# (agent_set_position,<agent_id>,<position_no>), |
| agent_set_look_target_agent | 1713 # (agent_set_look_target_agent, <agent_id>, <agent_i... |
| agent_get_horse | 1714	# (agent_get_horse,<destination>,<agent_id>), |
| agent_get_rider | 1715	# (agent_get_rider,<destination>,<agent_id>), |
| agent_get_party_id | 1716	# (agent_get_party_id,<destination>,<agent_id>), |
| agent_get_entry_no | 1717	# (agent_get_entry_no,<destination>,<agent_id>), |
| agent_get_troop_id | 1718	# (agent_get_troop_id,<destination>, <agent_id>), |
| agent_get_item_id | 1719	# (agent_get_item_id,<destination>, <agent_id>), (wo... |
| store_agent_hit_points | 1720	# set absolute to 1 to retrieve actual hps, otherwis... |
| agent_set_hit_points | 1721	# set absolute to 1 if value is absolute, otherwise ... |
| agent_deliver_damage_to_agent | 1722	# (agent_deliver_damage_to_agent, <agent_id_delivere... |
| agent_get_kill_count | 1723   # (agent_get_kill_count,<destination>,<agent_id>,[... |
| agent_get_player_id | 1724   # (agent_get_player_id,<destination>,<agent_id>), |
| agent_set_invulnerable_shield | 1725 # (agent_set_invulnerable_shield, <agent_id>), |
| agent_get_wielded_item | 1726	# (agent_get_wielded_item,<destination>,<agent_id>,<... |
| agent_get_ammo | 1727	# (agent_get_ammo,<destination>,<agent_id>, <value>)... |
| agent_refill_ammo | 1728	# (agent_refill_ammo,<agent_id>), |
| agent_has_item_equipped | 1729	# (agent_has_item_equipped,<agent_id>,<item_id>), |
| agent_set_scripted_destination | 1730	# (agent_set_scripted_destination,<agent_id>,<positi... |
| agent_get_scripted_destination | 1731   # (agent_get_scripted_destination,<position_no>,<a... |
| agent_force_rethink | 1732 # (agent_force_rethink, <agent_id>), |
| agent_set_no_death_knock_down_only | 1733 # (agent_set_no_death_knock_down_only, <agent_id>, <... |
| agent_set_horse_speed_factor | 1734 # (agent_set_horse_speed_factor, <agent_id>, <speed_... |
| agent_clear_scripted_mode | 1735	# (agent_clear_scripted_mode,<agent_id>), |
| agent_set_speed_limit | 1736   # (agent_set_speed_limit,<agent_id>,<speed_limit(k... |
| agent_ai_set_always_attack_in_melee | 1737   # (agent_ai_set_always_attack_in_melee, <agent_id>... |
| agent_get_simple_behavior | 1738   # (agent_get_simple_behavior, <destination>, <agen... |
| agent_get_combat_state | 1739   # (agent_get_combat_state, <destination>, <agent_i... |
| agent_set_animation | 1740   # (agent_set_animation, <agent_id>, <anim_id>, [ch... |
| agent_set_stand_animation | 1741   # (agent_set_stand_action, <agent_id>, <anim_id>), |
| agent_set_walk_forward_animation | 1742   # (agent_set_walk_forward_action, <agent_id>, <ani... |
| agent_set_animation_progress | 1743   # (agent_set_animation_progress, <agent_id>, <valu... |
| agent_set_look_target_position | 1744   # (agent_set_look_target_position, <agent_id>, <po... |
| agent_set_attack_action | 1745   # (agent_set_attack_action, <agent_id>, <value>, <... |
| agent_set_defend_action | 1746   # (agent_set_defend_action, <agent_id>, <value>, <... |
| agent_set_wielded_item | 1747   # (agent_set_wielded_item, <agent_id>, <item_id>), |
| agent_set_scripted_destination_no_attack | 1748	# (agent_set_scripted_destination_no_attack,<agent_i... |
| agent_fade_out | 1749   # (agent_fade_out, <agent_id>), |
| agent_play_sound | 1750   # (agent_play_sound, <agent_id>, <sound_id>), |
| agent_start_running_away | 1751   # (agent_start_running_away, <agent_id>, [position... |
| agent_stop_running_away | 1752   # (agent_stop_run_away, <agent_id>), |
| agent_ai_set_aggressiveness | 1753   # (agent_ai_set_aggressiveness, <agent_id>, <value... |
| agent_set_kick_allowed | 1754   # (agent_set_kick_allowed, <agent_id>, <value>), #... |
| remove_agent | 1755   # (remove_agent, <agent_id>), |
| agent_get_attached_scene_prop | 1756   # (agent_get_attached_scene_prop, <destination>, <... |
| agent_set_attached_scene_prop | 1757   # (agent_set_attached_scene_prop, <agent_id>, <sce... |
| agent_set_attached_scene_prop_x | 1758   # (agent_set_attached_scene_prop_x, <agent_id>, <v... |
| agent_set_attached_scene_prop_z | 1759   # (agent_set_attached_scene_prop_z, <agent_id>, <v... |
| agent_get_time_elapsed_since_removed | 1760   # (agent_get_time_elapsed_since_dead, <destination... |
| agent_get_number_of_enemies_following | 1761   # (agent_get_number_of_enemies_following, <destina... |
| agent_set_no_dynamics | 1762   # (agent_set_no_dynamics, <agent_id>, <value>), #0... |
| agent_get_attack_action | 1763   # (agent_get_attack_action, <destination>, <agent_... |
| agent_get_defend_action | 1764   # (agent_get_defend_action, <destination>, <agent_... |
| agent_get_group | 1765   # (agent_get_group, <destination>, <agent_id>), |
| agent_set_group | 1766   # (agent_set_group, <agent_id>, <value>), |
| agent_get_action_dir | 1767   # (agent_get_action_dir, <destination>, <agent_id>... |
| agent_get_animation | 1768   # (agent_get_animation, <destination>, <agent_id>,... |
| agent_is_in_parried_animation | 1769   # (agent_is_in_parried_animation, <agent_id>), |
| agent_get_team | 1770   # (agent_get_team, <destination>, <agent_id>), |
| agent_set_team | 1771   # (agent_set_team, <agent_id>, <value>), |
| agent_get_class | 1772   # (agent_get_class ,<destination>, <agent_id>), |
| agent_get_division | 1773   # (agent_get_division ,<destination>, <agent_id>), |
| agent_unequip_item | 1774	  # (agent_unequip_item, <agent_id>, <item_id>, [wea... |
| class_is_listening_order | 1775   # (class_is_listening_order, <team_no>, <sub_class>), |
| agent_set_ammo | 1776   # (agent_set_ammo,<agent_id>,<item_id>,<value>), #... |
| agent_add_offer_with_timeout | 1777   # (agent_add_offer_with_timeout, <agent_id>, <agen... |
| agent_check_offer_from_agent | 1778   # (agent_check_offer_from_agent, <agent_id>, <agen... |
| agent_equip_item | 1779	  # (agent_equip_item, <agent_id>, <item_id>, [weapo... |
| entry_point_get_position | 1780   # (entry_point_get_position, <position_no>, <entry... |
| entry_point_set_position | 1781   # (entry_point_set_position, <entry_no>, <position... |
| entry_point_is_auto_generated | 1782  	# (entry_point_is_auto_generated, <entry_no>), |
| agent_set_division | 1783   # (agent_set_division, <agent_id>, <value>), |
| team_get_hold_fire_order | 1784   # (team_get_hold_fire_order, <destination>, <team_... |
| team_get_movement_order | 1785   # (team_get_movement_order, <destination>, <team_n... |
| team_get_riding_order | 1786   # (team_get_riding_order, <destination>, <team_no>... |
| team_get_weapon_usage_order | 1787   # (team_get_weapon_usage_order, <destination>, <te... |
| teams_are_enemies | 1788   # (teams_are_enemies, <team_no>, <team_no_2>), |
| team_give_order | 1790   # (team_give_order, <team_no>, <sub_class>, <order... |
| team_set_order_position | 1791   # (team_set_order_position, <team_no>, <sub_class>... |
| team_get_leader | 1792   # (team_get_leader, <destination>, <team_no>), |
| team_set_leader | 1793   # (team_set_leader, <team_no>, <new_leader_agent_i... |
| team_get_order_position | 1794   # (team_get_order_position, <position_no>, <team_n... |
| team_set_order_listener | 1795   # (team_set_order_listener, <team_no>, <sub_class>... |
| team_set_relation | 1796   # (team_set_relation, <team_no>, <team_no_2>, <val... |
| close_order_menu | 1789   # (close_order_menu), |
| set_rain | 1797   # (set_rain,<rain-type>,<strength>), (rain_type: 1... |
| set_fog_distance | 1798   # (set_fog_distance, <distance_in_meters>, [fog_co... |
| get_scene_boundaries | 1799   # (get_scene_boundaries, <position_min>, <position... |
| scene_prop_enable_after_time | 1800   # (scene_prop_enable_after_time, <scene_prop_id>, ... |
| scene_prop_has_agent_on_it | 1801   # (scene_prop_has_agent_on_it, <scene_prop_id>, <a... |
| agent_clear_relations_with_agents | 1802   # (agent_clear_relations_with_agents, <agent_id>), |
| agent_add_relation_with_agent | 1803   # (agent_add_relation_with_agent, <agent_id>, <age... |
| agent_get_item_slot | 1804   # (agent_get_item_slot, <destination>, <agent_id>,... |
| ai_mesh_face_group_show_hide | 1805   # (ai_mesh_face_group_show_hide, <group_no>, <valu... |
| agent_is_alarmed | 1806   # (agent_is_alarmed, <agent_id>), |
| agent_set_is_alarmed | 1807   # (agent_set_is_alarmed, <agent_id>, <value>), # 1... |
| agent_stop_sound | 1808   # (agent_stop_sound, <agent_id>), |
| agent_set_attached_scene_prop_y | 1809   # (agent_set_attached_scene_prop_y, <agent_id>, <v... |
| scene_prop_get_num_instances | 1810	# (scene_prop_get_num_instances, <destination>, <sce... |
| scene_prop_get_instance | 1811	# (scene_prop_get_instance, <destination>, <scene_pr... |
| scene_prop_get_visibility | 1812   # (scene_prop_get_visibility, <destination>, <scen... |
| scene_prop_set_visibility | 1813   # (scene_prop_set_visibility, <scene_prop_id>, <va... |
| scene_prop_set_hit_points | 1814   # (scene_prop_set_hit_points, <scene_prop_id>, <va... |
| scene_prop_get_hit_points | 1815   # (scene_prop_get_hit_points, <destination>, <scen... |
| scene_prop_get_max_hit_points | 1816   # (scene_prop_get_max_hit_points, <destination>, <... |
| scene_prop_get_team | 1817   # (scene_prop_get_team, <value>, <scene_prop_id>), |
| scene_prop_set_team | 1818   # (scene_prop_set_team, <scene_prop_id>, <value>), |
| scene_prop_set_prune_time | 1819   # (scene_prop_set_prune_time, <scene_prop_id>, <va... |
| scene_prop_set_cur_hit_points | 1820   # (scene_prop_set_cur_hit_points, <scene_prop_id>,... |
| scene_prop_fade_out | 1822   # (scene_prop_fade_out, <scene_prop_id>, <fade_out... |
| scene_prop_fade_in | 1823   # (scene_prop_fade_in, <scene_prop_id>, <fade_in_t... |
| agent_get_ammo_for_slot | 1825	# (agent_get_ammo_for_slot, <destination>, <agent_id... |
| agent_is_in_line_of_sight | 1826 # (agent_is_in_line_of_sight, <agent_id>, <position_... |
| agent_deliver_damage_to_agent_advanced | 1827	# (agent_deliver_damage_to_agent_advanced, <destinat... |
| team_get_gap_distance | 1828   # (team_get_gap_distance, <destination>, <team_no>... |
| add_missile | 1829	# (add_missile, <agent_id>, <starting_position>, <st... |
| scene_item_get_num_instances | 1830	# (scene_item_get_num_instances, <destination>, <ite... |
| scene_item_get_instance | 1831	# (scene_item_get_instance, <destination>, <item_id>... |
| scene_spawned_item_get_num_instances | 1832	# (scene_spawned_item_get_num_instances, <destinatio... |
| scene_spawned_item_get_instance | 1833	# (scene_spawned_item_get_instance, <destination>, <... |
| scene_allows_mounted_units | 1834   # (scene_allows_mounted_units), |
| class_set_name | 1837 # (class_set_name, <sub_class>, <string_id>), |
| prop_instance_is_valid | 1838 # (prop_instance_is_valid, <scene_prop_id>), |
| prop_instance_get_variation_id | 1840	# (prop_instance_get_variation_id, <destination>, <s... |
| prop_instance_get_variation_id_2 | 1841	# (prop_instance_get_variation_id_2, <destination>, ... |
| prop_instance_get_position | 1850	# (prop_instance_get_position, <position_no>, <scene... |
| prop_instance_get_starting_position | 1851	# (prop_instance_get_starting_position, <position_no... |
| prop_instance_get_scale | 1852	# (prop_instance_get_scale, <position_no>, <scene_pr... |
| prop_instance_get_scene_prop_kind | 1853   # (prop_instance_get_scene_prop_type, <destination... |
| prop_instance_set_scale | 1854 # (prop_instance_set_scale, <scene_prop_id>, <value_... |
| prop_instance_set_position | 1855	# (prop_instance_set_position, <scene_prop_id>, <pos... |
| prop_instance_animate_to_position | 1860	# (prop_instance_animate_to_position, <scene_prop_id... |
| prop_instance_stop_animating | 1861	# (prop_instance_stop_animating, <scene_prop_id>), |
| prop_instance_is_animating | 1862   # (prop_instance_is_animating, <destination>, <sce... |
| prop_instance_get_animation_target_position | 1863    # (prop_instance_get_animation_target_position, <... |
| prop_instance_enable_physics | 1864   # (prop_instance_enable_physics, <scene_prop_id>, ... |
| prop_instance_rotate_to_position | 1865	# (prop_instance_rotate_to_position, <scene_prop_id>... |
| prop_instance_initialize_rotation_angles | 1866   # (prop_instance_initialize_rotation_angles, <scen... |
| prop_instance_refill_hit_points | 1870 # (prop_instance_refill_hit_points, <scene_prop_id>), |
| prop_instance_dynamics_set_properties | 1871 # (prop_instance_dynamics_set_properties,<scene_prop... |
| prop_instance_dynamics_set_velocity | 1872 # (prop_instance_dynamics_set_velocity,<scene_prop_i... |
| prop_instance_dynamics_set_omega | 1873 # (prop_instance_dynamics_set_omega,<scene_prop_id>,... |
| prop_instance_dynamics_apply_impulse | 1874 # (prop_instance_dynamics_apply_impulse,<scene_prop_... |
| prop_instance_receive_damage | 1877 # (prop_instance_receive_damage, <scene_prop_id>, <a... |
| prop_instance_intersects_with_prop_instance | 1880 # (prop_instance_intersects_with_prop_instance, <sce... |
| prop_instance_play_sound | 1881 # (prop_instance_play_sound, <scene_prop_id>, <sound... |
| prop_instance_stop_sound | 1882 # (prop_instance_stop_sound, <scene_prop_id>), |
| prop_instance_clear_attached_missiles | 1885 # (prop_instance_clear_attached_missiles, <scene_pro... |
| prop_instance_add_particle_system | 1886 # (prop_instance_add_particle_system, <scene_prop_id... |
| prop_instance_stop_all_particle_systems | 1887 # (prop_instance_stop_all_particle_systems, <scene_p... |
| replace_prop_instance | 1889   # (replace_prop_instance, <scene_prop_id>, <new_sc... |
| replace_scene_props | 1890   # (replace_scene_props, <old_scene_prop_id>,<new_s... |
| replace_scene_items_with_scene_props | 1891   # (replace_scene_items_with_scene_props, <old_item... |
| cast_ray | 1900   # (cast_ray, <destination>, <hit_position_register... |
| set_mission_result | 1906	# (set_mission_result,<value>), |
| finish_mission | 1907	# (finish_mission, <delay_in_seconds>), |
| jump_to_scene | 1910	# (jump_to_scene,<scene_id>,<entry_no>), |
| set_jump_mission | 1911	# (set_jump_mission,<mission_template_id>), |
| set_jump_entry | 1912	# (set_jump_entry,<entry_no>), |
| start_mission_conversation | 1920	# (start_mission_conversation,<troop_id>), |
| add_reinforcements_to_entry | 1930	# (add_reinforcements_to_entry,<mission_template_ent... |
| mission_enable_talk | 1935   # (mission_enable_talk), #can talk with troops dur... |
| mission_disable_talk | 1936   # (mission_disable_talk), #disables talk option fo... |
| mission_tpl_entry_set_override_flags | 1940   # (mission_tpl_entry_set_override_flags, <mission_... |
| mission_tpl_entry_clear_override_items | 1941   # (mission_tpl_entry_clear_override_items, <missio... |
| mission_tpl_entry_add_override_item | 1942   # (mission_tpl_entry_add_override_item, <mission_t... |
| mission_tpl_are_all_agents_spawned | 1943   # (mission_tpl_are_all_agents_spawned), #agents >3... |
| set_current_color | 1950	# red, green, blue: a value of 255 means 100% |
| set_position_delta | 1955	# x, y, z |
| add_point_light | 1960	# (add_point_light,[flicker_magnitude],[flicker_inte... |
| add_point_light_to_entity | 1961	# (add_point_light_to_entity,[flicker_magnitude],[fl... |
| particle_system_add_new | 1965	# (particle_system_add_new,<par_sys_id>,[position_no]), |
| particle_system_emit | 1968	# (particle_system_emit,<par_sys_id>,<value_num_part... |
| particle_system_burst | 1969	# (particle_system_burst,<par_sys_id>,<position_no>,... |
| set_spawn_position | 1970   # (set_spawn_position, <position_no>), |
| spawn_item | 1971   # (spawn_item, <item_kind_id>, <item_modifier>, [s... |
| spawn_agent | 1972	# (spawn_agent,<troop_id>), (stores agent_id in reg0) |
| spawn_horse | 1973	# (spawn_horse,<item_kind_id>, <item_modifier>),  (s... |
| spawn_scene_prop | 1974   # (spawn_scene_prop, <scene_prop_id>),  (stores pr... |
| particle_system_burst_no_sync | 1975	# (particle_system_burst_without_sync,<par_sys_id>,<... |
| spawn_item_without_refill | 1976   # (spawn_item_without_refill, <item_kind_id>, <ite... |
| agent_get_item_cur_ammo | 1977	# (agent_get_item_cur_ammo, <destination>, <agent_id... |
| cur_item_add_mesh | 1964   # (cur_item_add_mesh, <mesh_name_string_no>, [<lod... |
| cur_item_set_material | 1978   # (cur_item_set_material, <string_no>, <sub_mesh_n... |
| cur_tableau_add_tableau_mesh | 1980   # (cur_tableau_add_tableau_mesh, <tableau_material... |
| cur_item_set_tableau_material | 1981   # (cur_item_set_tableu_material, <tableau_material... |
| cur_scene_prop_set_tableau_material | 1982   # (cur_scene_prop_set_tableau_material, <tableau_m... |
| cur_map_icon_set_tableau_material | 1983   # (cur_map_icon_set_tableau_material, <tableau_mat... |
| cur_tableau_render_as_alpha_mask | 1984   # (cur_tableau_render_as_alpha_mask) |
| cur_tableau_set_background_color | 1985   # (cur_tableau_set_background_color, <value>), |
| cur_agent_set_banner_tableau_material | 1986   # (cur_agent_set_banner_tableau_material, <tableau... |
| cur_tableau_set_ambient_light | 1987   # (cur_tableau_set_ambient_light, <red_fixed_point... |
| cur_tableau_set_camera_position | 1988   # (cur_tableau_set_camera_position, <position_no>), |
| cur_tableau_set_camera_parameters | 1989   # (cur_tableau_set_camera_parameters, <is_perspect... |
| cur_tableau_add_point_light | 1990   # (cur_tableau_add_point_light, <map_icon_id>, <po... |
| cur_tableau_add_sun_light | 1991   # (cur_tableau_add_sun_light, <map_icon_id>, <posi... |
| cur_tableau_add_mesh | 1992   # (cur_tableau_add_mesh, <mesh_id>, <position_no>,... |
| cur_tableau_add_mesh_with_vertex_color | 1993   # (cur_tableau_add_mesh_with_vertex_color, <mesh_i... |
| cur_tableau_add_map_icon | 1994   # (cur_tableau_add_map_icon, <map_icon_id>, <posit... |
| cur_tableau_add_troop | 1995   # (cur_tableau_add_troop, <troop_id>, <position_no... |
| cur_tableau_add_horse | 1996   # (cur_tableau_add_horse, <item_id>, <position_no>... |
| cur_tableau_set_override_flags | 1997   # (cur_tableau_set_override_flags, <value>), |
| cur_tableau_clear_override_items | 1998   # (cur_tableau_clear_override_items), |
| cur_tableau_add_override_item | 1999   # (cur_tableau_add_override_item, <item_kind_id>), |
| cur_tableau_add_mesh_with_scale_and_vertex_color | 2000   # (cur_tableau_add_mesh_with_scale_and_vertex_colo... |
| mission_cam_set_mode | 2001   # (mission_cam_set_mode, <mission_cam_mode>, <dura... |
| mission_get_time_speed | 2002   # (mission_get_time_speed, <destination_fixed_poin... |
| mission_set_time_speed | 2003   # (mission_set_time_speed, <value_fixed_point>), #... |
| mission_time_speed_move_to_value | 2004   # (mission_speed_move_to_value, <value_fixed_point... |
| mission_set_duel_mode | 2006   # (mission_set_duel_mode, <value>), #value: 0 = of... |
| mission_cam_set_screen_color | 2008   #(mission_cam_set_screen_color, <value>), #value i... |
| mission_cam_animate_to_screen_color | 2009   #(mission_cam_animate_to_screen_color, <value>, <d... |
| mission_cam_get_position | 2010   # (mission_cam_get_position, <position_register_no>), |
| mission_cam_set_position | 2011   # (mission_cam_set_position, <position_register_no>), |
| mission_cam_animate_to_position | 2012   # (mission_cam_animate_to_position, <position_regi... |
| mission_cam_get_aperture | 2013   # (mission_cam_get_aperture, <destination>), |
| mission_cam_set_aperture | 2014   # (mission_cam_set_aperture, <value>), |
| mission_cam_animate_to_aperture | 2015   # (mission_cam_animate_to_aperture, <value>, <dura... |
| mission_cam_animate_to_position_and_aperture | 2016   # (mission_cam_animate_to_position_and_aperture, <... |
| mission_cam_set_target_agent | 2017   # (mission_cam_set_target_agent, <agent_id>, <valu... |
| mission_cam_clear_target_agent | 2018   # (mission_cam_clear_target_agent), |
| mission_cam_set_animation | 2019   # (mission_cam_set_animation, <anim_id>), |
| talk_info_show | 2020   # (talk_info_show, <hide_or_show>), :0=hide 1=show |
| talk_info_set_relation_bar | 2021   # (talk_info_set_relation_bar, <value>), :set rela... |
| talk_info_set_line | 2022   # (talk_info_set_line, <line_no>, <string_no>) |
| set_background_mesh | 2031   # (set_background_mesh, <mesh_id>), |
| set_game_menu_tableau_mesh | 2032   # (set_game_menu_tableau_mesh, <tableau_material_i... |
| change_screen_return | 2040	# (change_screen_return), |
| change_screen_loot | 2041	# (change_screen_loot, <troop_id>), |
| change_screen_trade | 2042	# (change_screen_trade, <troop_id>), |
| change_screen_exchange_members | 2043	# (change_screen_exchange_members, [0,1 = exchange_l... |
| change_screen_trade_prisoners | 2044	# (change_screen_trade_prisoners), |
| change_screen_buy_mercenaries | 2045	# (change_screen_buy_mercenaries), |
| change_screen_view_character | 2046	# (change_screen_view_character), |
| change_screen_training | 2047	# (change_screen_training), |
| change_screen_mission | 2048	# (change_screen_mission), |
| change_screen_map_conversation | 2049   # (change_screen_map_conversation, <troop_id>), |
| change_screen_exchange_with_party | 2050   # (change_screen_exchange_with_party, <party_id>), |
| change_screen_equip_other | 2051	# (change_screen_equip_other, <troop_id>), |
| change_screen_map | 2052 |
| change_screen_notes | 2053   # (change_screen_notes, <note_type>, <object_id>),... |
| change_screen_quit | 2055   # (change_screen_quit), |
| change_screen_give_members | 2056   # (change_screen_give_members, [party_id]), #if pa... |
| change_screen_controls | 2057   # (change_screen_controls), |
| change_screen_options | 2058   # (change_screen_options), |
| jump_to_menu | 2060	# (jump_to_menu,<menu_id>), |
| disable_menu_option | 2061   # (disable_menu_option), |
| agent_get_damage_modifier | 2065 # (agent_get_damage_modifier, <destination>, <agent_... |
| agent_get_accuracy_modifier | 2066 # (agent_get_accuracy_modifier, <destination>, <agen... |
| agent_get_speed_modifier | 2067 # (agent_get_speed_modifier, <destination>, <agent_i... |
| agent_get_reload_speed_modifier | 2068 # (agent_get_reload_speed_modifier, <destination>, <... |
| agent_get_use_speed_modifier | 2069 # (agent_get_use_speed_modifier, <destination>, <age... |
| store_trigger_param | 2070  # (store_trigger_param, <destination>, <trigger_par... |
| store_trigger_param_1 | 2071  # (store_trigger_param_1,<destination>), |
| store_trigger_param_2 | 2072  # (store_trigger_param_2,<destination>), |
| store_trigger_param_3 | 2073  # (store_trigger_param_3,<destination>), |
| set_trigger_result | 2075  # (set_trigger_result, <value>), |
| agent_get_bone_position | 2076 # (agent_get_bone_position, <position_no>, <agent_no... |
| agent_ai_set_interact_with_player | 2077 # (agent_ai_set_interact_with_player, <agent_no>, <v... |
| agent_ai_get_look_target | 2080 # (agent_ai_get_look_target, <destination>, <agent_i... |
| agent_ai_get_move_target | 2081 # (agent_ai_get_move_target, <destination>, <agent_i... |
| agent_ai_get_behavior_target | 2082 # (agent_ai_get_behavior_target, <destination>, <age... |
| agent_ai_set_can_crouch | 2083 # (agent_ai_set_can_crouch, <agent_id>, <value>), # ... |
| agent_set_max_hit_points | 2090	# set absolute to 1 if value is absolute, otherwise ... |
| agent_set_damage_modifier | 2091   # (agent_set_damage_modifier, <agent_id>, <value>)... |
| agent_set_accuracy_modifier | 2092   # (agent_set_accuracy_modifier, <agent_id>, <value... |
| agent_set_speed_modifier | 2093   # (agent_set_speed_modifier, <agent_id>, <value>),... |
| agent_set_reload_speed_modifier | 2094   # (agent_set_reload_speed_modifier, <agent_id>, <v... |
| agent_set_use_speed_modifier | 2095   # (agent_set_use_speed_modifier, <agent_id>, <valu... |
| agent_set_visibility | 2096   # (agent_set_visibility, <agent_id>, <value>), # 0... |
| agent_get_crouch_mode | 2097   # (agent_get_crouch_mode, <destination>, <agent_id>), |
| agent_set_crouch_mode | 2098   # (agent_set_crouch_mode, <agent_id>, <value>), # 0-1 |
| agent_set_ranged_damage_modifier | 2099   # (agent_set_ranged_damage_modifier, <agent_id>, <... |
| val_lshift | 2100 # (val_lshift, <destination>, <value>), # shifts the... |
| val_rshift | 2101 # (val_rshift, <destination>, <value>), # shifts the... |
| val_add | 2105	#dest, operand ::       dest = dest + operand |
| val_sub | 2106	#dest, operand ::       dest = dest + operand |
| val_mul | 2107	#dest, operand ::       dest = dest * operand |
| val_div | 2108	#dest, operand ::       dest = dest / operand |
| val_mod | 2109	#dest, operand ::       dest = dest mod operand |
| val_min | 2110	#dest, operand ::       dest = min(dest, operand) |
| val_max | 2111	#dest, operand ::       dest = max(dest, operand) |
| val_clamp | 2112	#dest, operand ::       dest = max(min(dest,<upper_b... |
| val_abs | 2113  #dest          ::       dest = abs(dest) |
| val_or | 2114   #dest, operand ::       dest = dest | operand |
| val_and | 2115   #dest, operand ::       dest = dest & operand |
| store_or | 2116   #dest, op1, op2 :      dest = op1 | op2 |
| store_and | 2117   #dest, op1, op2 :      dest = op1 & op2 |
| store_mod | 2119	#dest, op1, op2 :      dest = op1 % op2 |
| store_add | 2120	#dest, op1, op2 :      dest = op1 + op2 |
| store_sub | 2121	#dest, op1, op2 :      dest = op1 - op2 |
| store_mul | 2122	#dest, op1, op2 :      dest = op1 * op2 |
| store_div | 2123	#dest, op1, op2 :      dest = op1 / op2 |
| set_fixed_point_multiplier | 2124 # (set_fixed_point_multiplier, <value>), |
| store_sqrt | 2125  # (store_sqrt, <destination_fixed_point>, <value_fi... |
| store_pow | 2126  # (store_pow, <destination_fixed_point>, <value_fix... |
| store_sin | 2127  # (store_sin, <destination_fixed_point>, <value_fix... |
| store_cos | 2128  # (store_cos, <destination_fixed_point>, <value_fix... |
| store_tan | 2129  # (store_tan, <destination_fixed_point>, <value_fix... |
| convert_to_fixed_point | 2130  # (convert_to_fixed_point, <destination_fixed_point... |
| convert_from_fixed_point | 2131 # (convert_from_fixed_point, <destination>), divides... |
| assign | 2133	# had to put this here so that it can be called from... |
| shuffle_range | 2134	# (shuffle_range,<reg_no>,<reg_no>), |
| store_random | 2135	# deprecated, use store_random_in_range instead. |
| store_random_in_range | 2136	# gets random number in range [range_low,range_high]... |
| store_asin | 2140  # (store_asin, <destination_fixed_point>, <value_fi... |
| store_acos | 2141  # (store_acos, <destination_fixed_point>, <value_fi... |
| store_atan | 2142  # (store_atan, <destination_fixed_point>, <value_fi... |
| store_atan2 | 2143  # (store_atan2, <destination_fixed_point>, <value_f... |
| store_troop_gold | 2149	# (store_troop_gold,<destination>,<troop_id>), |
| store_num_free_stacks | 2154 # (store_num_free_stacks,<destination>,<party_id>), |
| store_num_free_prisoner_stacks | 2155 # (store_num_free_prisoner_stacks,<destination>,<par... |
| store_party_size | 2156	# (store_party_size,<destination>,[party_id]), |
| store_party_size_wo_prisoners | 2157	# (store_party_size_wo_prisoners,<destination>,[part... |
| store_troop_kind_count | 2158 # deprecated, use party_count_members_of_type instead |
| store_num_regular_prisoners | 2159	# (store_mum_regular_prisoners,<destination>,<party_... |
| store_troop_count_companions | 2160	# (store_troop_count_companions,<destination>,<troop... |
| store_troop_count_prisoners | 2161	# (store_troop_count_prisoners,<destination>,<troop_... |
| store_item_kind_count | 2165	# (store_item_kind_count,<destination>,<item_id>,[tr... |
| store_free_inventory_capacity | 2167	# (store_free_inventory_capacity,<destination>,[troo... |
| store_skill_level | 2170	# (store_skill_level,<destination>,<skill_id>,[troop... |
| store_character_level | 2171	# (store_character_level,<destination>,[troop_id]), |
| store_attribute_level | 2172	# (store_attribute_level,<destination>,<troop_id>,<a... |
| store_troop_faction | 2173	# (store_troop_faction,<destination>,<troop_id>), |
| store_faction_of_troop | 2173	# (store_troop_faction,<destination>,<troop_id>), |
| store_troop_health | 2175	# (store_troop_health,<destination>,<troop_id>,[abso... |
| store_proficiency_level | 2176	# (store_proficiency_level,<destination>,<troop_id>,... |
| store_relation | 2190	# (store_relation,<destination>,<faction_id_1>,<fact... |
| set_conversation_speaker_troop | 2197  # (set_conversation_speaker_troop, <troop_id>), |
| set_conversation_speaker_agent | 2198  # (set_conversation_speaker_troop, <agent_id>), |
| store_conversation_agent | 2199 # (store_conversation_agent,<destination>), |
| store_conversation_troop | 2200 # (store_conversation_troop,<destination>), |
| store_partner_faction | 2201 # (store_partner_faction,<destination>), |
| store_encountered_party | 2202 # (store_encountered_party,<destination>), |
| store_encountered_party2 | 2203 # (store_encountered_party2,<destination>), |
| store_faction_of_party | 2204 # (store_faction_of_party, <destination>, <party_id>), |
| set_encountered_party | 2205 # (set_encountered_party,<destination>), |
| store_current_scene | 2211 # (store_current_scene,<destination>), |
| store_zoom_amount | 2220 # (store_zoom_amount, <destination_fixed_point>), |
| set_zoom_amount | 2221 # (set_zoom_amount, <value_fixed_point>), |
| is_zoom_disabled | 2222 # (is_zoom_disabled), |
| store_item_value | 2230 # (store_item_value,<destination>,<item_id>), |
| store_troop_value | 2231 # (store_troop_value,<destination>,<troop_id>), |
| store_partner_quest | 2240 # (store_partner_quest,<destination>), |
| store_random_quest_in_range | 2250 # (store_random_quest_in_range,<destination>,<lower_... |
| store_random_troop_to_raise | 2251 # (store_random_troop_to_raise,<destination>,<lower_... |
| store_random_troop_to_capture | 2252	# (store_random_troop_to_capture,<destination>,<lowe... |
| store_random_party_in_range | 2254	# (store_random_party_in_range,<destination>,<lower_... |
| store01_random_parties_in_range | 2255 # stores two random, different parties in a range to... |
| store_random_horse | 2257	# (store_random_horse,<destination>) |
| store_random_equipment | 2258	# (store_random_equipment,<destination>) |
| store_random_armor | 2259	# (store_random_armor,<destination>) |
| store_quest_number | 2261 # (store_quest_number,<destination>,<quest_id>), |
| store_quest_item | 2262	# (store_quest_item,<destination>,<item_id>), |
| store_quest_troop | 2263	# (store_quest_troop,<destination>,<troop_id>), |
| store_current_hours | 2270 # (store_current_hours,<destination>), |
| store_time_of_day | 2271	# (store_time_of_day,<destination>), |
| store_current_day | 2272	# (store_current_day,<destination>), |
| is_currently_night | 2273	# (is_currently_night), |
| store_distance_to_party_from_party | 2281	# (store_distance_to_party_from_party,<destination>,... |
| get_party_ai_behavior | 2290	# (get_party_ai_behavior,<destination>,<party_id>), |
| get_party_ai_object | 2291	# (get_party_ai_object,<destination>,<party_id>), |
| party_get_ai_target_position | 2292	# (party_get_ai_target_position,<position_no>,<party... |
| get_party_ai_current_behavior | 2293   # (get_party_ai_current_behavior,<destination>,<pa... |
| get_party_ai_current_object | 2294	# (get_party_ai_current_object,<destination>,<party_... |
| store_num_parties_created | 2300	# (store_num_parties_created,<destination>,<party_te... |
| store_num_parties_destroyed | 2301	# (store_num_parties_destroyed,<destination>,<party_... |
| store_num_parties_destroyed_by_player | 2302	# (store_num_parties_destroyed_by_player,<destinatio... |
| store_num_parties_of_template | 2310	# (store_num_parties_of_template,<destination>,<part... |
| store_random_party_of_template | 2311	# fails if no party exists with tempolate_id (expens... |
| str_is_empty | 2318 # (str_is_empty, <string_register>), |
| str_clear | 2319 # (str_clear, <string_register>) |
| str_store_string | 2320	# (str_store_string,<string_register>,<string_id>), |
| str_store_string_reg | 2321	# (str_store_string_reg,<string_register>,<string_no... |
| str_store_troop_name | 2322	# (str_store_troop_name,<string_register>,<troop_id>), |
| str_store_troop_name_plural | 2323	# (str_store_troop_name_plural,<string_register>,<tr... |
| str_store_troop_name_by_count | 2324	# (str_store_troop_name_by_count,<string_register>,<... |
| str_store_item_name | 2325	# (str_store_item_name,<string_register>,<item_id>), |
| str_store_item_name_plural | 2326	# (str_store_item_name_plural,<string_register>,<ite... |
| str_store_item_name_by_count | 2327	# (str_store_item_name_by_count,<string_register>,<i... |
| str_store_party_name | 2330	# (str_store_party_name,<string_register>,<party_id>), |
| str_store_agent_name | 2332	# (str_store_agent_name,<string_register>,<agent_id>), |
| str_store_faction_name | 2335	# (str_store_faction_name,<string_register>,<faction... |
| str_store_quest_name | 2336	# (str_store_quest_name,<string_register>,<quest_id>), |
| str_store_info_page_name | 2337	# (str_store_info_page_name,<string_register>,<info_... |
| str_store_date | 2340 # (str_store_date,<string_register>,<number_of_hours... |
| str_store_troop_name_link | 2341 # (str_store_troop_name_link,<string_register>,<troo... |
| str_store_party_name_link | 2342 # (str_store_party_name_link,<string_register>,<part... |
| str_store_faction_name_link | 2343 # (str_store_faction_name_link,<string_register>,<fa... |
| str_store_quest_name_link | 2344 # (str_store_quest_name_link,<string_register>,<ques... |
| str_store_info_page_name_link | 2345 # (str_store_info_page_name_link,<string_register>,<... |
| str_store_class_name | 2346 # (str_store_class_name,<stribg_register>,<class_id>) |
| str_store_player_username | 2350 # (str_store_player_username,<string_register>,<play... |
| str_store_server_password | 2351 # (str_store_server_password, <string_register>), |
| str_store_server_name | 2352 # (str_store_server_name, <string_register>), |
| str_store_welcome_message | 2353 # (str_store_welcome_message, <string_register>), |
| str_encode_url | 2355 # (str_encode_url, <string_register>), |
| store_remaining_team_no | 2360	# (store_remaining_team_no,<destination>), |
| store_mission_timer_a_msec | 2365	# (store_mission_timer_a_msec,<destination>), |
| store_mission_timer_b_msec | 2366	# (store_mission_timer_b_msec,<destination>), |
| store_mission_timer_c_msec | 2367	# (store_mission_timer_c_msec,<destination>), |
| store_mission_timer_a | 2370	# (store_mission_timer_a,<destination>), |
| store_mission_timer_b | 2371	# (store_mission_timer_b,<destination>), |
| store_mission_timer_c | 2372	# (store_mission_timer_c,<destination>), |
| reset_mission_timer_a | 2375	# (reset_mission_timer_a), |
| reset_mission_timer_b | 2376	# (reset_mission_timer_b), |
| reset_mission_timer_c | 2377	# (reset_mission_timer_c), |
| set_cheer_at_no_enemy | 2379    # (set_cheer_at_no_enemy, <value>), # values:0->d... |
| store_enemy_count | 2380 # (store_enemy_count,<destination>), |
| store_friend_count | 2381 # (store_friend_count,<destination>), |
| store_ally_count | 2382 # (store_ally_count,<destination>), |
| store_defender_count | 2383 # (store_defender_count,<destination>), |
| store_attacker_count | 2384 # (store_attacker_count,<destination>), |
| store_normalized_team_count | 2385 #(store_normalized_team_count,<destination>, <team_n... |
| set_postfx | 2386 |
| set_river_shader_to_mud | 2387 #changes river material for muddy env |
| show_troop_details | 2388 # (show_troop_details, <troop_id>, <position>, <troo... |
| set_skybox | 2389 # (set_skybox, <non_hdr_skybox_index>, <hdr_skybox_i... |
| set_startup_sun_light | 2390 # (set_startup_sun_light, <r>, <g>, <b>)	#changes th... |
| set_startup_ambient_light | 2391 # (set_startup_ambient_light, <r>, <g>, <b>)	#change... |
| set_startup_ground_ambient_light | 2392 # (set_startup_ground_ambient_light, <r>, <g>, <b>)	... |
| rebuild_shadow_map | 2393 # (rebuild_shadow_map), |
| get_startup_sun_light | 2394  # (get_startup_sun_light, <position_no>), |
| get_startup_ambient_light | 2395  # (get_startup_ambient_light, <position_no>), |
| get_startup_ground_ambient_light | 2396 # (get_startup_ground_ambient_light, <position_no>), |
| set_shader_param_int | 2400 # (set_shader_param_int, <parameter_name>, <value>),... |
| set_shader_param_float | 2401 # (set_shader_param_float, <parameter_name>, <value>... |
| set_shader_param_float4 | 2402 # (set_shader_param_float4, <parameter_name>, <value... |
| set_shader_param_float4x4 | 2403 # (set_shader_param_float4x4, <parameter_name>, [0][... |
| prop_instance_deform_to_time | 2610 # (prop_instance_deform_to_time, <prop_instance_no>,... |
| prop_instance_deform_in_range | 2611 # (prop_instance_deform_in_range, <prop_instance_no>... |
| prop_instance_deform_in_cycle_loop | 2612 # (prop_instance_deform_in_cycle_loop, <prop_instanc... |
| prop_instance_get_current_deform_progress | 2615 # (prop_instance_get_current_deform_progress, <desti... |
| prop_instance_get_current_deform_frame | 2616 # (prop_instance_get_current_deform_frame, <destinat... |
| prop_instance_set_material | 2617 # (prop_instance_set_material, <prop_instance_no>, <... |
| agent_ai_get_num_cached_enemies | 2670 # (agent_ai_get_num_cached_enemies, <destination>, <... |
| agent_ai_get_cached_enemy | 2671 # (agent_ai_get_cached_enemy, <destination>, <agent_... |
| item_get_weight | 2700 # (item_get_weight, <destination_fixed_point>, <item... |
| item_get_value | 2701 # (item_get_value, <destination>, <item_kind_no>), #... |
| item_get_difficulty | 2702 # (item_get_difficulty, <destination>, <item_kind_no... |
| item_get_head_armor | 2703 # (item_get_head_armor, <destination>, <item_kind_no... |
| item_get_body_armor | 2704 # (item_get_body_armor, <destination>, <item_kind_no... |
| item_get_leg_armor | 2705 # (item_get_leg_armor, <destination>, <item_kind_no>... |
| item_get_hit_points | 2706 # (item_get_hit_points, <destination>, <item_kind_no... |
| item_get_weapon_length | 2707 # (item_get_weapon_length, <destination>, <item_kind... |
| item_get_speed_rating | 2708 # (item_get_speed_rating, <destination>, <item_kind_... |
| item_get_missile_speed | 2709 # (item_get_missile_speed, <destination>, <item_kind... |
| item_get_max_ammo | 2710 # (item_get_max_ammo, <destination>, <item_kind_no>)... |
| item_get_accuracy | 2711 # (item_get_accuracy, <destination>, <item_kind_no>)... |
| item_get_shield_height | 2712 # (item_get_shield_height, <destination_fixed_point>... |
| item_get_horse_scale | 2713 # (item_get_horse_scale, <destination_fixed_point>, ... |
| item_get_horse_speed | 2714 # (item_get_horse_speed, <destination>, <item_kind_n... |
| item_get_horse_maneuver | 2715 # (item_get_horse_maneuver, <destination>, <item_kin... |
| item_get_food_quality | 2716 # (item_get_food_quality, <destination>, <item_kind_... |
| item_get_abundance | 2717 # (item_get_abundance, <destination>, <item_kind_no>... |
| item_get_thrust_damage | 2718 # (item_get_thrust_damage, <destination>, <item_kind... |
| item_get_thrust_damage_type | 2719 # (item_get_thrust_damage_type, <destination>, <item... |
| item_get_swing_damage | 2720 # (item_get_swing_damage, <destination>, <item_kind_... |
| item_get_swing_damage_type | 2721 # (item_get_swing_damage_type, <destination>, <item_... |
| item_get_horse_charge_damage | 2722 # (item_get_horse_charge_damage, <destination>, <ite... |
| item_has_property | 2723 # (item_has_property, <item_kind_no>, <property>), #... |
| item_has_capability | 2724 # (item_has_capability, <item_kind_no>, <capability>... |
| item_has_modifier | 2725 # (item_has_modifier, <item_kind_no>, <item_modifier... |
| item_has_faction | 2726 # (item_has_faction, <item_kind_no>, <faction_no>), ... |
| str_store_player_face_keys | 2747 # (str_store_player_face_keys, <string_no>, <player_... |
| player_set_face_keys | 2748 # (player_set_face_keys, <player_id>, <string_no>), ... |
| str_store_troop_face_keys | 2750 # (str_store_troop_face_keys, <string_no>, <troop_no... |
| troop_set_face_keys | 2751 # (troop_set_face_keys, <troop_no>, <string_no>, [<a... |
| face_keys_get_hair | 2752 # (face_keys_get_hair, <destination>, <string_no>), ... |
| face_keys_set_hair | 2753 # (face_keys_set_hair, <string_no>, <value>), #Sets ... |
| face_keys_get_beard | 2754 # (face_keys_get_beard, <destination>, <string_no>),... |
| face_keys_set_beard | 2755 # (face_keys_set_beard, <string_no>, <value>), #Sets... |
| face_keys_get_face_texture | 2756 # (face_keys_get_face_texture, <destination>, <strin... |
| face_keys_set_face_texture | 2757 # (face_keys_set_face_texture, <string_no>, <value>)... |
| face_keys_get_hair_texture | 2758 # (face_keys_get_hair_texture, <destination>, <strin... |
| face_keys_set_hair_texture | 2759 # (face_keys_set_hair_texture, <string_no>, <value>)... |
| face_keys_get_hair_color | 2760 # (face_keys_get_hair_color, <destination>, <string_... |
| face_keys_set_hair_color | 2761 # (face_keys_set_hair_color, <string_no>, <value>), ... |
| face_keys_get_age | 2762 # (face_keys_get_age, <destination>, <string_no>), #... |
| face_keys_set_age | 2763 # (face_keys_set_age, <string_no>, <value>), #Sets f... |
| face_keys_get_skin_color | 2764 # (face_keys_get_skin_color, <destination>, <string_... |
| face_keys_set_skin_color | 2765 # (face_keys_set_skin_color, <string_no>, <value>), ... |
| face_keys_get_morph_key | 2766 # (face_keys_get_morph_key, <destination>, <string_n... |
| face_keys_set_morph_key | 2767 # (face_keys_set_morph_key, <string_no>, <key_no>, <... |
| lhs_operations | [try_for_range, |
| global_lhs_operations | [val_lshift, |
| can_fail_operations | [ge, |

### header_particle_systems.py

| Константа | Значение |
|-----------|----------|
| psf_always_emit | 0x0000000002 |
| psf_global_emit_dir | 0x0000000010 |
| psf_emit_at_water_level | 0x0000000020 |
| psf_billboard_2d | 0x0000000100 # up_vec = dir, front rotated towards camera |
| psf_billboard_3d | 0x0000000200 # front_vec point to camera. |
| psf_billboard_drop | 0x0000000300 |
| psf_turn_to_velocity | 0x0000000400 |
| psf_randomize_rotation | 0x0000001000 |
| psf_randomize_size | 0x0000002000 |
| psf_2d_turbulance | 0x0000010000 |
| psf_next_effect_is_lod | 0x0000020000 |

### header_parties.py

| Константа | Значение |
|-----------|----------|
| pf_icon_mask | 0x000000ff |
| pf_disabled | 0x00000100 |
| pf_is_ship | 0x00000200 |
| pf_is_static | 0x00000400 |
| pf_label_small | 0x00000000 |
| pf_label_medium | 0x00001000 |
| pf_label_large | 0x00002000 |
| pf_always_visible | 0x00004000 |
| pf_default_behavior | 0x00010000 |
| pf_auto_remove_in_town | 0x00020000 |
| pf_quest_party | 0x00040000 |
| pf_no_label | 0x00080000 |
| pf_limit_members | 0x00100000 |
| pf_hide_defenders | 0x00200000 |
| pf_show_faction | 0x00400000 |
| pf_dont_attack_civilians | 0x02000000 |
| pf_civilian | 0x04000000 |
| pf_carry_goods_bits | 48 |
| pf_carry_gold_bits | 56 |
| pf_carry_gold_multiplier | 20 |
| pf_carry_goods_mask | 0x00ff000000000000 |
| pf_carry_gold_mask | 0xff00000000000000 |
| pmf_is_prisoner | 0x0001 |
| no_faction | -1 |
| ai_bhvr_hold | 0 |
| ai_bhvr_travel_to_party | 1 |
| ai_bhvr_patrol_location | 2 |
| ai_bhvr_patrol_party | 3 |
| ai_bhvr_track_party | 4 #deprecated, use the alias ai_bhvr_attack_party instead. |
| ai_bhvr_attack_party | 4 |
| ai_bhvr_avoid_party | 5 |
| ai_bhvr_travel_to_point | 6 |
| ai_bhvr_negotiate_party | 7 |
| ai_bhvr_in_town | 8 |
| ai_bhvr_travel_to_ship | 9 |
| ai_bhvr_escort_party | 10 |
| ai_bhvr_driven_by_party | 11 |
| player_loot_share | 10 |
| hero_loot_share | 3 |
| courage_4 | 0x0004 |
| courage_5 | 0x0005 |
| courage_6 | 0x0006 |
| courage_7 | 0x0007 |
| courage_8 | 0x0008 |
| courage_9 | 0x0009 |
| courage_10 | 0x000A |
| courage_11 | 0x000B |
| courage_12 | 0x000C |
| courage_13 | 0x000D |
| courage_14 | 0x000E |
| courage_15 | 0x000F |
| aggressiveness_0 | 0x0000 |
| aggressiveness_1 | 0x0010 |
| aggressiveness_2 | 0x0020 |
| aggressiveness_3 | 0x0030 |
| aggressiveness_4 | 0x0040 |
| aggressiveness_5 | 0x0050 |
| aggressiveness_6 | 0x0060 |
| aggressiveness_7 | 0x0070 |
| aggressiveness_8 | 0x0080 |
| aggressiveness_9 | 0x0090 |
| aggressiveness_10 | 0x00A0 |
| aggressiveness_11 | 0x00B0 |
| aggressiveness_12 | 0x00C0 |
| aggressiveness_13 | 0x00D0 |
| aggressiveness_14 | 0x00E0 |
| aggressiveness_15 | 0x00F0 |
| banditness | 0x0100 |
| soldier_personality | aggressiveness_8 | courage_9 |
| merchant_personality | aggressiveness_0 | courage_7 |
| escorted_merchant_personality | aggressiveness_0 | courage_11 |
| bandit_personality | aggressiveness_3 | courage_8 | banditness |

### header_postfx.py

| Константа | Значение |
|-----------|----------|
| fxf_highhdr | 0x00000001 |

### header_presentations.py

| Константа | Значение |
|-----------|----------|
| tf_left_align | 0x00000004 |
| tf_right_align | 0x00000008 |
| tf_center_justify | 0x00000010 |
| tf_double_space | 0x00000800 |
| tf_vertical_align_center | 0x00001000 |
| tf_scrollable | 0x00002000 |
| tf_single_line | 0x00008000 |
| tf_with_outline | 0x00010000 |
| tf_scrollable_style_2 | 0x00020000 |
| prsntf_read_only | 0x00000001 |
| prsntf_manual_end_only | 0x00000002 |

### header_quests.py

| Константа | Значение |
|-----------|----------|
| qf_show_progression | 0x00000001 |
| qf_random_quest | 0x00000002 |

### header_scene_props.py

| Константа | Значение |
|-----------|----------|
| sokf_type_container | 0x0000000000000005 |
| sokf_type_ai_limiter | 0x0000000000000008 |
| sokf_type_barrier | 0x0000000000000009 |
| sokf_type_barrier_leave | 0x000000000000000a |
| sokf_type_ladder | 0x000000000000000b |
| sokf_type_barrier3d | 0x000000000000000c |
| sokf_type_player_limiter | 0x000000000000000d |
| sokf_type_ai_limiter3d | 0x000000000000000e |
| sokf_type_mask | 0x00000000000000FF |
| sokf_add_fire | 0x0000000000000100 |
| sokf_add_smoke | 0x0000000000000200 |
| sokf_add_light | 0x0000000000000400 |
| sokf_show_hit_point_bar | 0x0000000000000800 |
| sokf_place_at_origin | 0x0000000000001000 |
| sokf_dynamic | 0x0000000000002000 |
| sokf_invisible | 0x0000000000004000 |
| sokf_destructible | 0x0000000000008000 |
| sokf_moveable | 0x0000000000010000 |
| sokf_face_player | 0x0000000000020000 |
| sokf_dynamic_physics | 0x0000000000040000 |
| sokf_missiles_not_attached | 0x0000000000080000 #works only for dynamic mission objects |
| sokf_enforce_shadows | 0x0000000000100000 |
| sokf_dont_move_agent_over | 0x0000000000200000 |
| sokf_handle_as_flora | 0x0000000001000000 |
| sokf_static_movement | 0x0000000002000000 |
| spbf_hit_points_mask | 0x00000000000000FF |
| spbf_hit_points_bits | 20 |
| spbf_init_use_time_mask | 0x00000000000000FF |
| spbf_use_time_bits | 28 |
| spanim_linear | 0 |
| spanim_loop_linear | 4 |

### header_scenes.py

| Константа | Значение |
|-----------|----------|
| scene_name_pos | 0 |
| passages_pos | 8 |
| sf_indoors | 0x00000001   #The scene shouldn't have a skybox and light... |
| sf_force_skybox | 0x00000002   #Force adding a skybox even if indoors flag ... |
| sf_generate | 0x00000100   #Generate terrain by terran-generator |
| sf_randomize | 0x00000200   #Randomize terrain generator key |
| sf_auto_entry_points | 0x00000400   #Automatically create entry points |
| sf_no_horses | 0x00000800   #Horses are not avaible |
| sf_muddy_water | 0x00001000   #Changes the shader of the river mesh |

### header_skills.py

| Константа | Значение |
|-----------|----------|
| sf_base_att_str | 0x000 |
| sf_base_att_agi | 0x001 |
| sf_base_att_int | 0x002 |
| sf_base_att_cha | 0x003 |
| sf_effects_party | 0x010 |
| sf_inactive | 0x100 |
| skl_trade | 0 |
| skl_leadership | 1 |
| skl_prisoner_management | 2 |
| skl_reserved_1 | 3 |
| skl_reserved_2 | 4 |
| skl_reserved_3 | 5 |
| skl_reserved_4 | 6 |
| skl_persuasion | 7 |
| skl_engineer | 8 |
| skl_first_aid | 9 |
| skl_surgery | 10 |
| skl_wound_treatment | 11 |
| skl_inventory_management | 12 |
| skl_spotting | 13 |
| skl_pathfinding | 14 |
| skl_tactics | 15 |
| skl_tracking | 16 |
| skl_trainer | 17 |
| skl_reserved_5 | 18 |
| skl_reserved_6 | 19 |
| skl_reserved_7 | 20 |
| skl_reserved_8 | 21 |
| skl_looting | 22 |
| skl_horse_archery | 23 |
| skl_riding | 24 |
| skl_athletics | 25 |
| skl_shield | 26 |
| skl_weapon_master | 27 |
| skl_reserved_9 | 28 |
| skl_reserved_10 | 29 |
| skl_reserved_11 | 30 |
| skl_reserved_12 | 31 |
| skl_reserved_13 | 32 |
| skl_power_draw | 33 |
| skl_power_throw | 34 |
| skl_power_strike | 35 |
| skl_ironflesh | 36 |
| skl_reserved_14 | 37 |
| skl_reserved_15 | 38 |
| skl_reserved_16 | 39 |
| skl_reserved_17 | 40 |
| skl_reserved_18 | 41 |
| knows_trade_1 | 1 |
| knows_trade_2 | 2 |
| knows_trade_3 | 3 |
| knows_trade_4 | 4 |
| knows_trade_5 | 5 |
| knows_trade_6 | 6 |
| knows_trade_7 | 7 |
| knows_trade_8 | 8 |
| knows_trade_9 | 9 |
| knows_trade_10 | 10 |
| knows_leadership_1 | 16 |
| knows_leadership_2 | 32 |
| knows_leadership_3 | 48 |
| knows_leadership_4 | 64 |
| knows_leadership_5 | 80 |
| knows_leadership_6 | 96 |
| knows_leadership_7 | 112 |
| knows_leadership_8 | 128 |
| knows_leadership_9 | 144 |
| knows_leadership_10 | 160 |
| knows_prisoner_management_1 | 256 |
| knows_prisoner_management_2 | 512 |
| knows_prisoner_management_3 | 768 |
| knows_prisoner_management_4 | 1024 |
| knows_prisoner_management_5 | 1280 |
| knows_prisoner_management_6 | 1536 |
| knows_prisoner_management_7 | 1792 |
| knows_prisoner_management_8 | 2048 |
| knows_prisoner_management_9 | 2304 |
| knows_prisoner_management_10 | 2560 |
| knows_reserved_1_1 | 4096 |
| knows_reserved_1_2 | 8192 |
| knows_reserved_1_3 | 12288 |
| knows_reserved_1_4 | 16384 |
| knows_reserved_1_5 | 20480 |
| knows_reserved_1_6 | 24576 |
| knows_reserved_1_7 | 28672 |
| knows_reserved_1_8 | 32768 |
| knows_reserved_1_9 | 36864 |
| knows_reserved_1_10 | 40960 |
| knows_reserved_2_1 | 65536 |
| knows_reserved_2_2 | 131072 |
| knows_reserved_2_3 | 196608 |
| knows_reserved_2_4 | 262144 |
| knows_reserved_2_5 | 327680 |
| knows_reserved_2_6 | 393216 |
| knows_reserved_2_7 | 458752 |
| knows_reserved_2_8 | 524288 |
| knows_reserved_2_9 | 589824 |
| knows_reserved_2_10 | 655360 |
| knows_reserved_3_1 | 1048576 |
| knows_reserved_3_2 | 2097152 |
| knows_reserved_3_3 | 3145728 |
| knows_reserved_3_4 | 4194304 |
| knows_reserved_3_5 | 5242880 |
| knows_reserved_3_6 | 6291456 |
| knows_reserved_3_7 | 7340032 |
| knows_reserved_3_8 | 8388608 |
| knows_reserved_3_9 | 9437184 |
| knows_reserved_3_10 | 10485760 |
| knows_reserved_4_1 | 16777216 |
| knows_reserved_4_2 | 33554432 |
| knows_reserved_4_3 | 50331648 |
| knows_reserved_4_4 | 67108864 |
| knows_reserved_4_5 | 83886080 |
| knows_reserved_4_6 | 100663296 |
| knows_reserved_4_7 | 117440512 |
| knows_reserved_4_8 | 134217728 |
| knows_reserved_4_9 | 150994944 |
| knows_reserved_4_10 | 167772160 |
| knows_persuasion_1 | 268435456 |
| knows_persuasion_2 | 536870912 |
| knows_persuasion_3 | 805306368 |
| knows_persuasion_4 | 1073741824 |
| knows_persuasion_5 | 1342177280 |
| knows_persuasion_6 | 1610612736 |
| knows_persuasion_7 | 1879048192 |
| knows_persuasion_8 | 2147483648 |
| knows_persuasion_9 | 2415919104 |
| knows_persuasion_10 | 2684354560 |
| knows_engineer_1 | 4294967296 |
| knows_engineer_2 | 8589934592 |
| knows_engineer_3 | 12884901888 |
| knows_engineer_4 | 17179869184 |
| knows_engineer_5 | 21474836480 |
| knows_engineer_6 | 25769803776 |
| knows_engineer_7 | 30064771072 |
| knows_engineer_8 | 34359738368 |
| knows_engineer_9 | 38654705664 |
| knows_engineer_10 | 42949672960 |
| knows_first_aid_1 | 68719476736 |
| knows_first_aid_2 | 137438953472 |
| knows_first_aid_3 | 206158430208 |
| knows_first_aid_4 | 274877906944 |
| knows_first_aid_5 | 343597383680 |
| knows_first_aid_6 | 412316860416 |
| knows_first_aid_7 | 481036337152 |
| knows_first_aid_8 | 549755813888 |
| knows_first_aid_9 | 618475290624 |
| knows_first_aid_10 | 687194767360 |
| knows_surgery_1 | 1099511627776 |
| knows_surgery_2 | 2199023255552 |
| knows_surgery_3 | 3298534883328 |
| knows_surgery_4 | 4398046511104 |
| knows_surgery_5 | 5497558138880 |
| knows_surgery_6 | 6597069766656 |
| knows_surgery_7 | 7696581394432 |
| knows_surgery_8 | 8796093022208 |
| knows_surgery_9 | 9895604649984 |
| knows_surgery_10 | 10995116277760 |
| knows_wound_treatment_1 | 17592186044416 |
| knows_wound_treatment_2 | 35184372088832 |
| knows_wound_treatment_3 | 52776558133248 |
| knows_wound_treatment_4 | 70368744177664 |
| knows_wound_treatment_5 | 87960930222080 |
| knows_wound_treatment_6 | 105553116266496 |
| knows_wound_treatment_7 | 123145302310912 |
| knows_wound_treatment_8 | 140737488355328 |
| knows_wound_treatment_9 | 158329674399744 |
| knows_wound_treatment_10 | 175921860444160 |
| knows_inventory_management_1 | 281474976710656 |
| knows_inventory_management_2 | 562949953421312 |
| knows_inventory_management_3 | 844424930131968 |
| knows_inventory_management_4 | 1125899906842624 |
| knows_inventory_management_5 | 1407374883553280 |
| knows_inventory_management_6 | 1688849860263936 |
| knows_inventory_management_7 | 1970324836974592 |
| knows_inventory_management_8 | 2251799813685248 |
| knows_inventory_management_9 | 2533274790395904 |
| knows_inventory_management_10 | 2814749767106560 |
| knows_spotting_1 | 4503599627370496 |
| knows_spotting_2 | 9007199254740992 |
| knows_spotting_3 | 13510798882111488 |
| knows_spotting_4 | 18014398509481984 |
| knows_spotting_5 | 22517998136852480 |
| knows_spotting_6 | 27021597764222976 |
| knows_spotting_7 | 31525197391593472 |
| knows_spotting_8 | 36028797018963968 |
| knows_spotting_9 | 40532396646334464 |
| knows_spotting_10 | 45035996273704960 |
| knows_pathfinding_1 | 72057594037927936 |
| knows_pathfinding_2 | 144115188075855872 |
| knows_pathfinding_3 | 216172782113783808 |
| knows_pathfinding_4 | 288230376151711744 |
| knows_pathfinding_5 | 360287970189639680 |
| knows_pathfinding_6 | 432345564227567616 |
| knows_pathfinding_7 | 504403158265495552 |
| knows_pathfinding_8 | 576460752303423488 |
| knows_pathfinding_9 | 648518346341351424 |
| knows_pathfinding_10 | 720575940379279360 |
| knows_tactics_1 | 1152921504606846976 |
| knows_tactics_2 | 2305843009213693952 |
| knows_tactics_3 | 3458764513820540928 |
| knows_tactics_4 | 4611686018427387904 |
| knows_tactics_5 | 5764607523034234880 |
| knows_tactics_6 | 6917529027641081856 |
| knows_tactics_7 | 8070450532247928832 |
| knows_tactics_8 | 9223372036854775808 |
| knows_tactics_9 | 10376293541461622784 |
| knows_tactics_10 | 11529215046068469760 |
| knows_tracking_1 | 18446744073709551616 |
| knows_tracking_2 | 36893488147419103232 |
| knows_tracking_3 | 55340232221128654848 |
| knows_tracking_4 | 73786976294838206464 |
| knows_tracking_5 | 92233720368547758080 |
| knows_tracking_6 | 110680464442257309696 |
| knows_tracking_7 | 129127208515966861312 |
| knows_tracking_8 | 147573952589676412928 |
| knows_tracking_9 | 166020696663385964544 |
| knows_tracking_10 | 184467440737095516160 |
| knows_trainer_1 | 295147905179352825856 |
| knows_trainer_2 | 590295810358705651712 |
| knows_trainer_3 | 885443715538058477568 |
| knows_trainer_4 | 1180591620717411303424 |
| knows_trainer_5 | 1475739525896764129280 |
| knows_trainer_6 | 1770887431076116955136 |
| knows_trainer_7 | 2066035336255469780992 |
| knows_trainer_8 | 2361183241434822606848 |
| knows_trainer_9 | 2656331146614175432704 |
| knows_trainer_10 | 2951479051793528258560 |
| knows_reserved_5_1 | 4722366482869645213696 |
| knows_reserved_5_2 | 9444732965739290427392 |
| knows_reserved_5_3 | 14167099448608935641088 |
| knows_reserved_5_4 | 18889465931478580854784 |
| knows_reserved_5_5 | 23611832414348226068480 |
| knows_reserved_5_6 | 28334198897217871282176 |
| knows_reserved_5_7 | 33056565380087516495872 |
| knows_reserved_5_8 | 37778931862957161709568 |
| knows_reserved_5_9 | 42501298345826806923264 |
| knows_reserved_5_10 | 47223664828696452136960 |
| knows_reserved_6_1 | 75557863725914323419136 |
| knows_reserved_6_2 | 151115727451828646838272 |
| knows_reserved_6_3 | 226673591177742970257408 |
| knows_reserved_6_4 | 302231454903657293676544 |
| knows_reserved_6_5 | 377789318629571617095680 |
| knows_reserved_6_6 | 453347182355485940514816 |
| knows_reserved_6_7 | 528905046081400263933952 |
| knows_reserved_6_8 | 604462909807314587353088 |
| knows_reserved_6_9 | 680020773533228910772224 |
| knows_reserved_6_10 | 755578637259143234191360 |
| knows_reserved_7_1 | 1208925819614629174706176 |
| knows_reserved_7_2 | 2417851639229258349412352 |
| knows_reserved_7_3 | 3626777458843887524118528 |
| knows_reserved_7_4 | 4835703278458516698824704 |
| knows_reserved_7_5 | 6044629098073145873530880 |
| knows_reserved_7_6 | 7253554917687775048237056 |
| knows_reserved_7_7 | 8462480737302404222943232 |
| knows_reserved_7_8 | 9671406556917033397649408 |
| knows_reserved_7_9 | 10880332376531662572355584 |
| knows_reserved_7_10 | 12089258196146291747061760 |
| knows_reserved_8_1 | 19342813113834066795298816 |
| knows_reserved_8_2 | 38685626227668133590597632 |
| knows_reserved_8_3 | 58028439341502200385896448 |
| knows_reserved_8_4 | 77371252455336267181195264 |
| knows_reserved_8_5 | 96714065569170333976494080 |
| knows_reserved_8_6 | 116056878683004400771792896 |
| knows_reserved_8_7 | 135399691796838467567091712 |
| knows_reserved_8_8 | 154742504910672534362390528 |
| knows_reserved_8_9 | 174085318024506601157689344 |
| knows_reserved_8_10 | 193428131138340667952988160 |
| knows_looting_1 | 309485009821345068724781056 |
| knows_looting_2 | 618970019642690137449562112 |
| knows_looting_3 | 928455029464035206174343168 |
| knows_looting_4 | 1237940039285380274899124224 |
| knows_looting_5 | 1547425049106725343623905280 |
| knows_looting_6 | 1856910058928070412348686336 |
| knows_looting_7 | 2166395068749415481073467392 |
| knows_looting_8 | 2475880078570760549798248448 |
| knows_looting_9 | 2785365088392105618523029504 |
| knows_looting_10 | 3094850098213450687247810560 |
| knows_horse_archery_1 | 4951760157141521099596496896 |
| knows_horse_archery_2 | 9903520314283042199192993792 |
| knows_horse_archery_3 | 14855280471424563298789490688 |
| knows_horse_archery_4 | 19807040628566084398385987584 |
| knows_horse_archery_5 | 24758800785707605497982484480 |
| knows_horse_archery_6 | 29710560942849126597578981376 |
| knows_horse_archery_7 | 34662321099990647697175478272 |
| knows_horse_archery_8 | 39614081257132168796771975168 |
| knows_horse_archery_9 | 44565841414273689896368472064 |
| knows_horse_archery_10 | 49517601571415210995964968960 |
| knows_riding_1 | 79228162514264337593543950336 |
| knows_riding_2 | 158456325028528675187087900672 |
| knows_riding_3 | 237684487542793012780631851008 |
| knows_riding_4 | 316912650057057350374175801344 |
| knows_riding_5 | 396140812571321687967719751680 |
| knows_riding_6 | 475368975085586025561263702016 |
| knows_riding_7 | 554597137599850363154807652352 |
| knows_riding_8 | 633825300114114700748351602688 |
| knows_riding_9 | 713053462628379038341895553024 |
| knows_riding_10 | 792281625142643375935439503360 |
| knows_athletics_1 | 1267650600228229401496703205376 |
| knows_athletics_2 | 2535301200456458802993406410752 |
| knows_athletics_3 | 3802951800684688204490109616128 |
| knows_athletics_4 | 5070602400912917605986812821504 |
| knows_athletics_5 | 6338253001141147007483516026880 |
| knows_athletics_6 | 7605903601369376408980219232256 |
| knows_athletics_7 | 8873554201597605810476922437632 |
| knows_athletics_8 | 10141204801825835211973625643008 |
| knows_athletics_9 | 11408855402054064613470328848384 |
| knows_athletics_10 | 12676506002282294014967032053760 |
| knows_shield_1 | 20282409603651670423947251286016 |
| knows_shield_2 | 40564819207303340847894502572032 |
| knows_shield_3 | 60847228810955011271841753858048 |
| knows_shield_4 | 81129638414606681695789005144064 |
| knows_shield_5 | 101412048018258352119736256430080 |
| knows_shield_6 | 121694457621910022543683507716096 |
| knows_shield_7 | 141976867225561692967630759002112 |
| knows_shield_8 | 162259276829213363391578010288128 |
| knows_shield_9 | 182541686432865033815525261574144 |
| knows_shield_10 | 202824096036516704239472512860160 |
| knows_weapon_master_1 | 324518553658426726783156020576256 |
| knows_weapon_master_2 | 649037107316853453566312041152512 |
| knows_weapon_master_3 | 973555660975280180349468061728768 |
| knows_weapon_master_4 | 1298074214633706907132624082305024 |
| knows_weapon_master_5 | 1622592768292133633915780102881280 |
| knows_weapon_master_6 | 1947111321950560360698936123457536 |
| knows_weapon_master_7 | 2271629875608987087482092144033792 |
| knows_weapon_master_8 | 2596148429267413814265248164610048 |
| knows_weapon_master_9 | 2920666982925840541048404185186304 |
| knows_weapon_master_10 | 3245185536584267267831560205762560 |
| knows_reserved_9_1 | 5192296858534827628530496329220096 |
| knows_reserved_9_2 | 10384593717069655257060992658440192 |
| knows_reserved_9_3 | 15576890575604482885591488987660288 |
| knows_reserved_9_4 | 20769187434139310514121985316880384 |
| knows_reserved_9_5 | 25961484292674138142652481646100480 |
| knows_reserved_9_6 | 31153781151208965771182977975320576 |
| knows_reserved_9_7 | 36346078009743793399713474304540672 |
| knows_reserved_9_8 | 41538374868278621028243970633760768 |
| knows_reserved_9_9 | 46730671726813448656774466962980864 |
| knows_reserved_9_10 | 51922968585348276285304963292200960 |
| knows_reserved_10_1 | 83076749736557242056487941267521536 |
| knows_reserved_10_2 | 166153499473114484112975882535043072 |
| knows_reserved_10_3 | 249230249209671726169463823802564608 |
| knows_reserved_10_4 | 332306998946228968225951765070086144 |
| knows_reserved_10_5 | 415383748682786210282439706337607680 |
| knows_reserved_10_6 | 498460498419343452338927647605129216 |
| knows_reserved_10_7 | 581537248155900694395415588872650752 |
| knows_reserved_10_8 | 664613997892457936451903530140172288 |
| knows_reserved_10_9 | 747690747629015178508391471407693824 |
| knows_reserved_10_10 | 830767497365572420564879412675215360 |
| knows_reserved_11_1 | 1329227995784915872903807060280344576 |
| knows_reserved_11_2 | 2658455991569831745807614120560689152 |
| knows_reserved_11_3 | 3987683987354747618711421180841033728 |
| knows_reserved_11_4 | 5316911983139663491615228241121378304 |
| knows_reserved_11_5 | 6646139978924579364519035301401722880 |
| knows_reserved_11_6 | 7975367974709495237422842361682067456 |
| knows_reserved_11_7 | 9304595970494411110326649421962412032 |
| knows_reserved_11_8 | 10633823966279326983230456482242756608 |
| knows_reserved_11_9 | 11963051962064242856134263542523101184 |
| knows_reserved_11_10 | 13292279957849158729038070602803445760 |
| knows_reserved_12_1 | 21267647932558653966460912964485513216 |
| knows_reserved_12_2 | 42535295865117307932921825928971026432 |
| knows_reserved_12_3 | 63802943797675961899382738893456539648 |
| knows_reserved_12_4 | 85070591730234615865843651857942052864 |
| knows_reserved_12_5 | 106338239662793269832304564822427566080 |
| knows_reserved_12_6 | 127605887595351923798765477786913079296 |
| knows_reserved_12_7 | 148873535527910577765226390751398592512 |
| knows_reserved_12_8 | 170141183460469231731687303715884105728 |
| knows_reserved_12_9 | 191408831393027885698148216680369618944 |
| knows_reserved_12_10 | 212676479325586539664609129644855132160 |
| knows_reserved_13_1 | 340282366920938463463374607431768211456 |
| knows_reserved_13_2 | 680564733841876926926749214863536422912 |
| knows_reserved_13_3 | 1020847100762815390390123822295304634368 |
| knows_reserved_13_4 | 1361129467683753853853498429727072845824 |
| knows_reserved_13_5 | 1701411834604692317316873037158841057280 |
| knows_reserved_13_6 | 2041694201525630780780247644590609268736 |
| knows_reserved_13_7 | 2381976568446569244243622252022377480192 |
| knows_reserved_13_8 | 2722258935367507707706996859454145691648 |
| knows_reserved_13_9 | 3062541302288446171170371466885913903104 |
| knows_reserved_13_10 | 3402823669209384634633746074317682114560 |
| knows_power_draw_1 | 5444517870735015415413993718908291383296 |
| knows_power_draw_2 | 10889035741470030830827987437816582766592 |
| knows_power_draw_3 | 16333553612205046246241981156724874149888 |
| knows_power_draw_4 | 21778071482940061661655974875633165533184 |
| knows_power_draw_5 | 27222589353675077077069968594541456916480 |
| knows_power_draw_6 | 32667107224410092492483962313449748299776 |
| knows_power_draw_7 | 38111625095145107907897956032358039683072 |
| knows_power_draw_8 | 43556142965880123323311949751266331066368 |
| knows_power_draw_9 | 49000660836615138738725943470174622449664 |
| knows_power_draw_10 | 54445178707350154154139937189082913832960 |
| knows_power_throw_1 | 87112285931760246646623899502532662132736 |
| knows_power_throw_2 | 174224571863520493293247799005065324265472 |
| knows_power_throw_3 | 261336857795280739939871698507597986398208 |
| knows_power_throw_4 | 348449143727040986586495598010130648530944 |
| knows_power_throw_5 | 435561429658801233233119497512663310663680 |
| knows_power_throw_6 | 522673715590561479879743397015195972796416 |
| knows_power_throw_7 | 609786001522321726526367296517728634929152 |
| knows_power_throw_8 | 696898287454081973172991196020261297061888 |
| knows_power_throw_9 | 784010573385842219819615095522793959194624 |
| knows_power_throw_10 | 871122859317602466466238995025326621327360 |
| knows_power_strike_1 | 1393796574908163946345982392040522594123776 |
| knows_power_strike_2 | 2787593149816327892691964784081045188247552 |
| knows_power_strike_3 | 4181389724724491839037947176121567782371328 |
| knows_power_strike_4 | 5575186299632655785383929568162090376495104 |
| knows_power_strike_5 | 6968982874540819731729911960202612970618880 |
| knows_power_strike_6 | 8362779449448983678075894352243135564742656 |
| knows_power_strike_7 | 9756576024357147624421876744283658158866432 |
| knows_power_strike_8 | 11150372599265311570767859136324180752990208 |
| knows_power_strike_9 | 12544169174173475517113841528364703347113984 |
| knows_power_strike_10 | 13937965749081639463459823920405225941237760 |
| knows_ironflesh_1 | 22300745198530623141535718272648361505980416 |
| knows_ironflesh_2 | 44601490397061246283071436545296723011960832 |
| knows_ironflesh_3 | 66902235595591869424607154817945084517941248 |
| knows_ironflesh_4 | 89202980794122492566142873090593446023921664 |
| knows_ironflesh_5 | 111503725992653115707678591363241807529902080 |
| knows_ironflesh_6 | 133804471191183738849214309635890169035882496 |
| knows_ironflesh_7 | 156105216389714361990750027908538530541862912 |
| knows_ironflesh_8 | 178405961588244985132285746181186892047843328 |
| knows_ironflesh_9 | 200706706786775608273821464453835253553823744 |
| knows_ironflesh_10 | 223007451985306231415357182726483615059804160 |
| knows_reserved_14_1 | 356811923176489970264571492362373784095686656 |
| knows_reserved_14_2 | 713623846352979940529142984724747568191373312 |
| knows_reserved_14_3 | 1070435769529469910793714477087121352287059968 |
| knows_reserved_14_4 | 1427247692705959881058285969449495136382746624 |
| knows_reserved_14_5 | 1784059615882449851322857461811868920478433280 |
| knows_reserved_14_6 | 2140871539058939821587428954174242704574119936 |
| knows_reserved_14_7 | 2497683462235429791852000446536616488669806592 |
| knows_reserved_14_8 | 2854495385411919762116571938898990272765493248 |
| knows_reserved_14_9 | 3211307308588409732381143431261364056861179904 |
| knows_reserved_14_10 | 3568119231764899702645714923623737840956866560 |
| knows_reserved_15_1 | 5708990770823839524233143877797980545530986496 |
| knows_reserved_15_2 | 11417981541647679048466287755595961091061972992 |
| knows_reserved_15_3 | 17126972312471518572699431633393941636592959488 |
| knows_reserved_15_4 | 22835963083295358096932575511191922182123945984 |
| knows_reserved_15_5 | 28544953854119197621165719388989902727654932480 |
| knows_reserved_15_6 | 34253944624943037145398863266787883273185918976 |
| knows_reserved_15_7 | 39962935395766876669632007144585863818716905472 |
| knows_reserved_15_8 | 45671926166590716193865151022383844364247891968 |
| knows_reserved_15_9 | 51380916937414555718098294900181824909778878464 |
| knows_reserved_15_10 | 57089907708238395242331438777979805455309864960 |
| knows_reserved_16_1 | 91343852333181432387730302044767688728495783936 |
| knows_reserved_16_2 | 182687704666362864775460604089535377456991567872 |
| knows_reserved_16_3 | 274031556999544297163190906134303066185487351808 |
| knows_reserved_16_4 | 365375409332725729550921208179070754913983135744 |
| knows_reserved_16_5 | 456719261665907161938651510223838443642478919680 |
| knows_reserved_16_6 | 548063113999088594326381812268606132370974703616 |
| knows_reserved_16_7 | 639406966332270026714112114313373821099470487552 |
| knows_reserved_16_8 | 730750818665451459101842416358141509827966271488 |
| knows_reserved_16_9 | 822094670998632891489572718402909198556462055424 |
| knows_reserved_16_10 | 913438523331814323877303020447676887284957839360 |
| knows_reserved_17_1 | 1461501637330902918203684832716283019655932542976 |
| knows_reserved_17_2 | 2923003274661805836407369665432566039311865085952 |
| knows_reserved_17_3 | 4384504911992708754611054498148849058967797628928 |
| knows_reserved_17_4 | 5846006549323611672814739330865132078623730171904 |
| knows_reserved_17_5 | 7307508186654514591018424163581415098279662714880 |
| knows_reserved_17_6 | 8769009823985417509222108996297698117935595257856 |
| knows_reserved_17_7 | 10230511461316320427425793829013981137591527800832 |
| knows_reserved_17_8 | 11692013098647223345629478661730264157247460343808 |
| knows_reserved_17_9 | 13153514735978126263833163494446547176903392886784 |
| knows_reserved_17_10 | 14615016373309029182036848327162830196559325429760 |
| knows_reserved_18_1 | 23384026197294446691258957323460528314494920687616 |
| knows_reserved_18_2 | 46768052394588893382517914646921056628989841375232 |
| knows_reserved_18_3 | 70152078591883340073776871970381584943484762062848 |
| knows_reserved_18_4 | 93536104789177786765035829293842113257979682750464 |
| knows_reserved_18_5 | 116920130986472233456294786617302641572474603438080 |
| knows_reserved_18_6 | 140304157183766680147553743940763169886969524125696 |
| knows_reserved_18_7 | 163688183381061126838812701264223698201464444813312 |
| knows_reserved_18_8 | 187072209578355573530071658587684226515959365500928 |
| knows_reserved_18_9 | 210456235775650020221330615911144754830454286188544 |
| knows_reserved_18_10 | 233840261972944466912589573234605283144949206876160 |
| num_skill_words | 6 |

### header_skins.py

| Константа | Значение |
|-----------|----------|
| voice_die | 0 |
| voice_hit | 1 |
| voice_grunt | 2 |
| voice_grunt_long | 3 |
| voice_yell | 4 |
| voice_warcry | 5 |
| voice_victory | 6 |
| voice_stun | 7 |
| skf_use_morph_key_10 | 0x00000001 |
| skf_use_morph_key_20 | 0x00000002 |
| skf_use_morph_key_30 | 0x00000003 |
| skf_use_morph_key_40 | 0x00000004 |
| skf_use_morph_key_50 | 0x00000005 |
| skf_use_morph_key_60 | 0x00000006 |
| skf_use_morph_key_70 | 0x00000007 |

### header_sounds.py

| Константа | Значение |
|-----------|----------|
| sf_2d | 0x00000001 |
| sf_looping | 0x00000002 |
| sf_start_at_random_pos | 0x00000004 |
| sf_stream_from_hd | 0x00000008 |
| sf_always_send_via_network | 0x00100000 |
| sf_priority_15 | 0x000000f0 |
| sf_priority_14 | 0x000000e0 |
| sf_priority_13 | 0x000000d0 |
| sf_priority_12 | 0x000000c0 |
| sf_priority_11 | 0x000000b0 |
| sf_priority_10 | 0x000000a0 |
| sf_priority_9 | 0x00000090 |
| sf_priority_8 | 0x00000080 |
| sf_priority_7 | 0x00000070 |
| sf_priority_6 | 0x00000060 |
| sf_priority_5 | 0x00000050 |
| sf_priority_4 | 0x00000040 |
| sf_priority_3 | 0x00000030 |
| sf_priority_2 | 0x00000020 |
| sf_priority_1 | 0x00000010 |
| sf_vol_15 | 0x00000f00 |
| sf_vol_14 | 0x00000e00 |
| sf_vol_13 | 0x00000d00 |
| sf_vol_12 | 0x00000c00 |
| sf_vol_11 | 0x00000b00 |
| sf_vol_10 | 0x00000a00 |
| sf_vol_9 | 0x00000900 |
| sf_vol_8 | 0x00000800 |
| sf_vol_7 | 0x00000700 |
| sf_vol_6 | 0x00000600 |
| sf_vol_5 | 0x00000500 |
| sf_vol_4 | 0x00000400 |
| sf_vol_3 | 0x00000300 |
| sf_vol_2 | 0x00000200 |
| sf_vol_1 | 0x00000100 |

### header_strings.py

| Константа | Значение |
|-----------|----------|
| result | -1 |
| num_strings | len(strings) |
| i_string | 0 |
| str | strings[i_string] |
| result | i_string |

### header_tableau_materials.py

*Нет констант*

### header_terrain_types.py

| Константа | Значение |
|-----------|----------|
| rt_water | 0 |
| rt_mountain | 1 |
| rt_steppe | 2 |
| rt_plain | 3 |
| rt_snow | 4 |
| rt_desert | 5 |
| rt_bridge | 7 |
| rt_river | 8 |
| rt_mountain_forest | 9 |
| rt_steppe_forest | 10 |
| rt_forest | 11 |
| rt_snow_forest | 12 |
| rt_desert_forest | 13 |

### header_triggers.py

| Константа | Значение |
|-----------|----------|
| ti_simulate_battle | -5.0 #can only be used in module_simple_triggers |
| ti_on_party_encounter | -6.0 #can only be used in module_simple_triggers |
| ti_question_answered | -8 |
| ti_server_player_joined | -15.0 #can only be used in module_mission_templates triggers |
| ti_on_multiplayer_mission_end | -16.0 |
| ti_before_mission_start | -19.0 #can only be used in module_mission_templates triggers |
| ti_after_mission_start | -20.0 #can only be used in module_mission_templates triggers |
| ti_tab_pressed | -21.0 #can only be used in module_mission_templates triggers |
| ti_inventory_key_pressed | -22.0 #can only be used in module_mission_templates triggers |
| ti_escape_pressed | -23.0 #can only be used in module_mission_templates triggers |
| ti_battle_window_opened | -24.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_spawn | -25.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_killed_or_wounded | -26.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_knocked_down | -27.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_hit | -28.0 #can only be used in module_mission_templates triggers |
| ti_on_player_exit | -29.0 #can only be used in module_mission_templates triggers |
| ti_on_leave_area | -30.0 #can only be used in module_mission_templates triggers |
| ti_on_scene_prop_init | -40.0 #can only be used in module_scene_props triggers |
| ti_on_init_scene_prop | ti_on_scene_prop_init |
| ti_on_scene_prop_hit | -42.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_destroy | -43.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_use | -44.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_is_animating | -45.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_animation_finished | -46.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_start_use | -47.0 #can only be used in module_scene_props triggers |
| ti_on_scene_prop_cancel_use | -48.0 #can only be used in module_scene_props triggers |
| ti_on_init_item | -50.0 #can only be used in module_items triggers |
| ti_on_weapon_attack | -51.0 #can only be used in module_items triggers |
| ti_on_missile_hit | -52.0 #can only be used in module_items triggers |
| ti_on_item_picked_up | -53.0 #can only be used in module_mission_templates triggers |
| ti_on_item_dropped | -54.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_mount | -55.0 #can only be used in module_mission_templates triggers |
| ti_on_agent_dismount | -56.0 #can only be used in module_mission_templates triggers |
| ti_on_item_wielded | -57.0 #can only be used in module_mission_templates triggers |
| ti_on_item_unwielded | -58.0 #can only be used in module_mission_templates triggers |
| ti_on_presentation_load | -60.0 #can only be used in module_presentations triggers |
| ti_on_presentation_run | -61.0 #can only be used in module_presentations triggers |
| ti_on_presentation_event_state_change | -62.0 #can only be used in module_presentations triggers |
| ti_on_presentation_mouse_enter_leave | -63.0 #can only be used in module_presentations triggers |
| ti_on_presentation_mouse_press | -64.0 #can only be used in module_presentations triggers |
| ti_on_init_map_icon | -70.0 #can only be used in module_map_icons triggers |
| ti_on_order_issued | -71.0 #can only be used in module_mission_templates triggers |
| ti_on_switch_to_map | -75.0 |
| ti_scene_prop_deformation_finished | -76.0 #can only be used in module_scene_props triggers |
| ti_on_shield_hit | -80.0 # can only be used in module_items triggers |
| ti_once | 100000000.0 |
| key_1 | 0x02 |
| key_2 | 0x03 |
| key_3 | 0x04 |
| key_4 | 0x05 |
| key_5 | 0x06 |
| key_6 | 0x07 |
| key_7 | 0x08 |
| key_8 | 0x09 |
| key_9 | 0x0a |
| key_0 | 0x0b |
| key_a | 0x1e |
| key_b | 0x30 |
| key_c | 0x2e |
| key_d | 0x20 |
| key_e | 0x12 |
| key_f | 0x21 |
| key_g | 0x22 |
| key_h | 0x23 |
| key_i | 0x17 |
| key_j | 0x24 |
| key_k | 0x25 |
| key_l | 0x26 |
| key_m | 0x32 |
| key_n | 0x31 |
| key_o | 0x18 |
| key_p | 0x19 |
| key_q | 0x10 |
| key_r | 0x13 |
| key_s | 0x1f |
| key_t | 0x14 |
| key_u | 0x16 |
| key_v | 0x2f |
| key_w | 0x11 |
| key_x | 0x2d |
| key_y | 0x15 |
| key_z | 0x2c |
| key_numpad_0 | 0x52 |
| key_numpad_1 | 0x4f |
| key_numpad_2 | 0x50 |
| key_numpad_3 | 0x51 |
| key_numpad_4 | 0x4b |
| key_numpad_5 | 0x4c |
| key_numpad_6 | 0x4d |
| key_numpad_7 | 0x47 |
| key_numpad_8 | 0x48 |
| key_numpad_9 | 0x49 |
| key_num_lock | 0x45 |
| key_numpad_slash | 0xb5 |
| key_numpad_multiply | 0x37 |
| key_numpad_minus | 0x4a |
| key_numpad_plus | 0x4e |
| key_numpad_enter | 0x9c |
| key_numpad_period | 0x53 |
| key_insert | 0xd2 |
| key_delete | 0xd3 |
| key_home | 0xc7 |
| key_end | 0xcf |
| key_page_up | 0xc9 |
| key_page_down | 0xd1 |
| key_up | 0xc8 |
| key_down | 0xd0 |
| key_left | 0xcb |
| key_right | 0xcd |
| key_f1 | 0x3b |
| key_f2 | 0x3c |
| key_f3 | 0x3d |
| key_f4 | 0x3e |
| key_f5 | 0x3f |
| key_f6 | 0x40 |
| key_f7 | 0x41 |
| key_f8 | 0x42 |
| key_f9 | 0x43 |
| key_f10 | 0x44 |
| key_f11 | 0x57 |
| key_f12 | 0x58 |
| key_space | 0x39 |
| key_escape | 0x01 |
| key_enter | 0x1c |
| key_tab | 0x0f |
| key_back_space | 0x0e |
| key_open_braces | 0x1a |
| key_close_braces | 0x1b |
| key_comma | 0x33 |
| key_period | 0x34 |
| key_slash | 0x35 |
| key_back_slash | 0x2b |
| key_equals | 0x0d |
| key_minus | 0x0c |
| key_semicolon | 0x27 |
| key_apostrophe | 0x28 |
| key_tilde | 0x29 |
| key_caps_lock | 0x3a |
| key_left_shift | 0x2a |
| key_right_shift | 0x36 |
| key_left_control | 0x1d |
| key_right_control | 0x9d |
| key_left_alt | 0x38 |
| key_right_alt | 0xb8 |
| key_left_mouse_button | 0xe0 |
| key_right_mouse_button | 0xe1 |
| key_middle_mouse_button | 0xe2 |
| key_mouse_button_4 | 0xe3 |
| key_mouse_button_5 | 0xe4 |
| key_mouse_button_6 | 0xe5 |
| key_mouse_button_7 | 0xe6 |
| key_mouse_button_8 | 0xe7 |
| key_mouse_scroll_up | 0xee |
| key_mouse_scroll_down | 0xef |
| key_xbox_a | 0xf0 |
| key_xbox_b | 0xf1 |
| key_xbox_x | 0xf2 |
| key_xbox_y | 0xf3 |
| key_xbox_dpad_up | 0xf4 |
| key_xbox_dpad_down | 0xf5 |
| key_xbox_dpad_right | 0xf6 |
| key_xbox_dpad_left | 0xf7 |
| key_xbox_start | 0xf8 |
| key_xbox_back | 0xf9 |
| key_xbox_rbumper | 0xfa |
| key_xbox_lbumper | 0xfb |
| key_xbox_ltrigger | 0xfc |
| key_xbox_rtrigger | 0xfd |
| key_xbox_rstick | 0xfe |
| key_xbox_lstick | 0xff |
| gk_move_forward | 0 |
| gk_move_backward | 1 |
| gk_move_left | 2 |
| gk_move_right | 3 |
| gk_action | 4 |
| gk_jump | 5 |
| gk_attack | 6 |
| gk_defend | 7 |
| gk_kick | 8 |
| gk_toggle_weapon_mode | 9 |
| gk_equip_weapon_1 | 10 |
| gk_equip_weapon_2 | 11 |
| gk_equip_weapon_3 | 12 |
| gk_equip_weapon_4 | 13 |
| gk_equip_primary_weapon | 14 |
| gk_equip_secondary_weapon | 15 |
| gk_drop_weapon | 16 |
| gk_sheath_weapon | 17 |
| gk_leave | 18 |
| gk_zoom | 19 |
| gk_view_char | 20 |
| gk_cam_toggle | 21 |
| gk_view_orders | 22 |
| gk_order_1 | 23 |
| gk_order_2 | 24 |
| gk_order_3 | 25 |
| gk_order_4 | 26 |
| gk_order_5 | 27 |
| gk_order_6 | 28 |
| gk_everyone_hear | 29 |
| gk_infantry_hear | 30 |
| gk_archers_hear | 31 |
| gk_cavalry_hear | 32 |
| gk_group0_hear | gk_infantry_hear |
| gk_group1_hear | gk_archers_hear |
| gk_group2_hear | gk_cavalry_hear |
| gk_group3_hear | 33 |
| gk_group4_hear | 34 |
| gk_group5_hear | 35 |
| gk_group6_hear | 36 |
| gk_group7_hear | 37 |
| gk_group8_hear | 38 |
| gk_reverse_order_group | 39 |
| gk_everyone_around_hear | 40 |
| gk_mp_message_all | 41 |
| gk_mp_message_team | 42 |
| gk_character_window | 43 |
| gk_inventory_window | 44 |
| gk_party_window | 45 |
| gk_quests_window | 46 |
| gk_game_log_window | 47 |
| gk_quick_save | 48 |
| gk_crouch | 49 |
| gk_order_7 | 50 |
| gk_order_8 | 51 |
| trigger_check_pos | 0 |
| trigger_delay_pos | 1 |
| trigger_rearm_pos | 2 |
| trigger_conditions_pos | 3 |
| trigger_consequences_pos | 4 |

### header_troops.py

| Константа | Значение |
|-----------|----------|
| tf_male | 0 |
| tf_female | 1 |
| tf_undead | 2 |
| troop_type_mask | 0x0000000f |
| tf_hero | 0x00000010 |
| tf_inactive | 0x00000020 |
| tf_unkillable | 0x00000040 |
| tf_allways_fall_dead | 0x00000080 |
| tf_no_capture_alive | 0x00000100 |
| tf_mounted | 0x00000400 #Troop's movement speed on map is determined b... |
| tf_is_merchant | 0x00001000 #When set, troop does not equip stuff he owns |
| tf_randomize_face | 0x00008000 #randomize face at the beginning of the game. |
| tf_guarantee_boots | 0x00100000 |
| tf_guarantee_armor | 0x00200000 |
| tf_guarantee_helmet | 0x00400000 |
| tf_guarantee_gloves | 0x00800000 |
| tf_guarantee_horse | 0x01000000 |
| tf_guarantee_shield | 0x02000000 |
| tf_guarantee_ranged | 0x04000000 |
| tf_guarantee_polearm | 0x08000000 |
| tf_unmoveable_in_party_window | 0x10000000 |
| ca_strength | 0 |
| ca_agility | 1 |
| ca_intelligence | 2 |
| ca_charisma | 3 |
| wpt_one_handed_weapon | 0 |
| wpt_two_handed_weapon | 1 |
| wpt_polearm | 2 |
| wpt_archery | 3 |
| wpt_crossbow | 4 |
| wpt_throwing | 5 |
| wpt_firearm | 6 |
| courage_4 | 0x0004 |
| courage_5 | 0x0005 |
| courage_6 | 0x0006 |
| courage_7 | 0x0007 |
| courage_8 | 0x0008 |
| courage_9 | 0x0009 |
| courage_10 | 0x000A |
| courage_11 | 0x000B |
| courage_12 | 0x000C |
| courage_13 | 0x000D |
| courage_14 | 0x000E |
| courage_15 | 0x000F |
| aggresiveness_1 | 0x0010 |
| aggresiveness_2 | 0x0020 |
| aggresiveness_3 | 0x0030 |
| aggresiveness_4 | 0x0040 |
| aggresiveness_5 | 0x0050 |
| aggresiveness_6 | 0x0060 |
| aggresiveness_7 | 0x0070 |
| aggresiveness_8 | 0x0080 |
| aggresiveness_9 | 0x0090 |
| aggresiveness_10 | 0x00A0 |
| aggresiveness_11 | 0x00B0 |
| aggresiveness_12 | 0x00C0 |
| aggresiveness_13 | 0x00D0 |
| aggresiveness_14 | 0x00E0 |
| aggresiveness_15 | 0x00F0 |
| is_bandit | 0x0100 |
| tsf_site_id_mask | 0x0000ffff |
| tsf_entry_mask | 0x00ff0000 |
| tsf_entry_bits | 16 |
| str_3 | bignum | 0x00000003 |
| str_4 | bignum | 0x00000004 |
| str_5 | bignum | 0x00000005 |
| str_6 | bignum | 0x00000006 |
| str_7 | bignum | 0x00000007 |
| str_8 | bignum | 0x00000008 |
| str_9 | bignum | 0x00000009 |
| str_10 | bignum | 0x0000000a |
| str_11 | bignum | 0x0000000b |
| str_12 | bignum | 0x0000000c |
| str_13 | bignum | 0x0000000d |
| str_14 | bignum | 0x0000000e |
| str_15 | bignum | 0x0000000f |
| str_16 | bignum | 0x00000010 |
| str_17 | bignum | 0x00000011 |
| str_18 | bignum | 0x00000012 |
| str_19 | bignum | 0x00000013 |
| str_20 | bignum | 0x00000014 |
| str_21 | bignum | 0x00000015 |
| str_22 | bignum | 0x00000016 |
| str_23 | bignum | 0x00000017 |
| str_24 | bignum | 0x00000018 |
| str_25 | bignum | 0x00000019 |
| str_26 | bignum | 0x0000001a |
| str_27 | bignum | 0x0000001b |
| str_28 | bignum | 0x0000001c |
| str_29 | bignum | 0x0000001d |
| str_30 | bignum | 0x0000001e |
| agi_3 | bignum | 0x00000300 |
| agi_4 | bignum | 0x00000400 |
| agi_5 | bignum | 0x00000500 |
| agi_6 | bignum | 0x00000600 |
| agi_7 | bignum | 0x00000700 |
| agi_8 | bignum | 0x00000800 |
| agi_9 | bignum | 0x00000900 |
| agi_10 | bignum | 0x00000a00 |
| agi_11 | bignum | 0x00000b00 |
| agi_12 | bignum | 0x00000c00 |
| agi_13 | bignum | 0x00000d00 |
| agi_14 | bignum | 0x00000e00 |
| agi_15 | bignum | 0x00000f00 |
| agi_16 | bignum | 0x00001000 |
| agi_17 | bignum | 0x00001100 |
| agi_18 | bignum | 0x00001200 |
| agi_19 | bignum | 0x00001300 |
| agi_20 | bignum | 0x00001400 |
| agi_21 | bignum | 0x00001500 |
| agi_22 | bignum | 0x00001600 |
| agi_23 | bignum | 0x00001700 |
| agi_24 | bignum | 0x00001800 |
| agi_25 | bignum | 0x00001900 |
| agi_26 | bignum | 0x00001a00 |
| agi_27 | bignum | 0x00001b00 |
| agi_28 | bignum | 0x00001c00 |
| agi_29 | bignum | 0x00001d00 |
| agi_30 | bignum | 0x00001e00 |
| int_3 | bignum | 0x00030000 |
| int_4 | bignum | 0x00040000 |
| int_5 | bignum | 0x00050000 |
| int_6 | bignum | 0x00060000 |
| int_7 | bignum | 0x00070000 |
| int_8 | bignum | 0x00080000 |
| int_9 | bignum | 0x00090000 |
| int_10 | bignum | 0x000a0000 |
| int_11 | bignum | 0x000b0000 |
| int_12 | bignum | 0x000c0000 |
| int_13 | bignum | 0x000d0000 |
| int_14 | bignum | 0x000e0000 |
| int_15 | bignum | 0x000f0000 |
| int_16 | bignum | 0x00100000 |
| int_17 | bignum | 0x00110000 |
| int_18 | bignum | 0x00120000 |
| int_19 | bignum | 0x00130000 |
| int_20 | bignum | 0x00140000 |
| int_21 | bignum | 0x00150000 |
| int_22 | bignum | 0x00160000 |
| int_23 | bignum | 0x00170000 |
| int_24 | bignum | 0x00180000 |
| int_25 | bignum | 0x00190000 |
| int_26 | bignum | 0x001a0000 |
| int_27 | bignum | 0x001b0000 |
| int_28 | bignum | 0x001c0000 |
| int_29 | bignum | 0x001d0000 |
| int_30 | bignum | 0x001e0000 |
| cha_3 | bignum | 0x03000000 |
| cha_4 | bignum | 0x04000000 |
| cha_5 | bignum | 0x05000000 |
| cha_6 | bignum | 0x06000000 |
| cha_7 | bignum | 0x07000000 |
| cha_8 | bignum | 0x08000000 |
| cha_9 | bignum | 0x09000000 |
| cha_10 | bignum | 0x0a000000 |
| cha_11 | bignum | 0x0b000000 |
| cha_12 | bignum | 0x0c000000 |
| cha_13 | bignum | 0x0d000000 |
| cha_14 | bignum | 0x0e000000 |
| cha_15 | bignum | 0x0f000000 |
| cha_16 | bignum | 0x10000000 |
| cha_17 | bignum | 0x11000000 |
| cha_18 | bignum | 0x12000000 |
| cha_19 | bignum | 0x13000000 |
| cha_20 | bignum | 0x14000000 |
| cha_21 | bignum | 0x15000000 |
| cha_22 | bignum | 0x16000000 |
| cha_23 | bignum | 0x17000000 |
| cha_24 | bignum | 0x18000000 |
| cha_25 | bignum | 0x19000000 |
| cha_26 | bignum | 0x1a000000 |
| cha_27 | bignum | 0x1b000000 |
| cha_28 | bignum | 0x1c000000 |
| cha_29 | bignum | 0x1d000000 |
| cha_30 | bignum | 0x1e000000 |
| level_mask | 0x000000FF |
| level_bits | 32 |
| v | level_mask |
| def_attrib | str_5 | agi_5 | int_4 | cha_4 |
| one_handed_bits | 0 |
| two_handed_bits | 10 |
| polearm_bits | 20 |
| archery_bits | 30 |
| crossbow_bits | 40 |
| throwing_bits | 50 |
| firearm_bits | 60 |
| num_weapon_proficiencies | 7 |
| result | -1 |
| num_troops | len(troops) |
| i_troop | 0 |
| troop | troops[i_troop] |
| result | i_troop |
| troop1_no | find_troop(troops,troop1_id) |
| troop2_no | find_troop(troops,troop2_id) |
| cur_troop | troops[troop1_no] |
| cur_troop_length | len(cur_troop) |
| troop1_no | find_troop(troops,troop1_id) |
| troop2_no | find_troop(troops,troop2_id) |
| troop3_no | find_troop(troops,troop3_id) |
| cur_troop | troops[troop1_no] |
| cur_troop_length | len(cur_troop) |


## 2. СТРУКТУРА ДАННЫХ (TUPLES)

### module_animations.py

- **Имя массива:** `animations`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] ["stand", 0, amf_client_prediction,
#   [3.0, "myanim", 0, 50, arf_cyclic|arf_loop_pos_0_25
  ```

### module_constants.py

*Не удалось определить структуру*

### module_dialogs.py

- **Имя массива:** `dialogs`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] [anyone ,"start", [(store_conversation_troop, "$g_talk_troop"),
                     (store_conversation_agent, "$g_talk_agent"),
                     (store_troop_faction, "$g_talk_troop_faction", "$g_talk_troop"),
#                     (troop_get_slot, "$g_talk_troop_relation", "$g_talk_troop", slot_troop_player_relation),
                     (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
                     (assign, "$g_talk_troop_relation", reg0),
					 
					 #This may be different way to handle persuasion, which might be a little more transparent to the player in its effects
					 #Persuasion will affect the player's relation with the other character -- but only for 1 on 1 conversations
					 (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
					 (assign, "$g_talk_troop_effective_relation", "$g_talk_troop_relation"),
					 (val_add, "$g_talk_troop_effective_relation", ":persuasion"),
					 (try_begin),
						(gt, "$g_talk_troop_effective_relation", 0),
						(store_add, ":persuasion_modifier", 10, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 10),
					 (else_try),
						(lt, "$g_talk_troop_effective_relation", 0),
						(store_sub, ":persuasion_modifier", 20, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 20),
					 (try_end),
					 (val_clamp, "$g_talk_troop_effective_relation", -100, 101), 
					 (try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg3, "$g_talk_troop_effective_relation"),
						(display_message, "str_test_effective_relation_=_reg3"),
					 (try_end),
					 
                     (try_begin),
                       (this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
                       (is_between, "$g_talk_troop", mayors_begin, mayors_end),
                       (party_get_slot, "$g_talk_troop_relation", "$current_town", slot_center_player_relation),
                     (try_end),
                     (store_relation, "$g_talk_troop_faction_relation", "$g_talk_troop_faction", "fac_player_faction"),
                     
                     (assign, "$g_talk_troop_party", "$g_encountered_party"),
                     (try_begin),
                       (troop_slot_ge, "$g_talk_troop", slot_troop_leaded_party, 1),
                       (troop_get_slot, "$g_talk_troop_party", "$g_talk_troop", slot_troop_leaded_party),
                     (try_end),
                     
#                     (assign, "$g_talk_troop_kingdom_relation", 0),
#                     (try_begin),
#                       (gt, "$players_kingdom", 0),
#                       (store_relation, "$g_talk_troop_kingdom_relation", "$g_talk_troop_faction", "$players_kingdom"),
#                     (try_end),


                     
                     (store_current_hours, "$g_current_hours"),
                     (troop_get_slot, "$g_talk_troop_last_talk_time", "$g_talk_troop", slot_troop_last_talk_time),
                     (troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),
                     (store_sub, "$g_time_since_last_talk","$g_current_hours","$g_talk_troop_last_talk_time"),
                     (troop_get_slot, "$g_talk_troop_met", "$g_talk_troop", slot_troop_met),
					 (val_min, "$g_talk_troop_met", 1), #the global variable goes no higher than one
					 (try_begin),
					    (troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
						(troop_set_slot, "$g_talk_troop", slot_troop_met, 1),
						
						#Possible later activations of notes
						(try_begin),
							(is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
						(try_end),
						
					 (try_end),
					 
                     (try_begin),
#                       (this_or_next|eq, "$talk_context", tc_party_encounter),
#                       (this_or_next|eq, "$talk_context", tc_castle_commander),
                       (call_script, "script_party_calculate_strength", "p_collective_enemy",0),
                       (assign, "$g_enemy_strength", reg0),
                       (call_script, "script_party_calculate_strength", "p_main_party",0),
                       (assign, "$g_ally_strength", reg0),
                       (store_mul, "$g_strength_ratio", "$g_ally_strength", 100),
					   (assign, ":enemy_strength", "$g_enemy_strength"), #these two lines added to avoid div by zero error
					   (val_max, ":enemy_strength", 1),
                       (val_div, "$g_strength_ratio", ":enemy_strength"),
                     (try_end),

                     (assign, "$g_comment_found", 0),

					 (assign, "$g_comment_has_rejoinder", 0),
					 (assign, "$g_romantic_comment_made", 0),
					 (assign, "$skip_lord_assumes_argument", 0), #a lord pre-empts a player's issue, ie, when the player is conducting a rebellion
					 (assign, "$bypass_female_vassal_explanation", 0),
					 (assign, "$g_done_wedding_comment", 0),
					 
#					 (assign, "$g_time_to_spare", 0),
					 
					 
                     (try_begin),
                       (troop_is_hero, "$g_talk_troop"),
                       (talk_info_show, 1),
                       (call_script, "script_setup_talk_info"),
                     (try_end),

					 (assign, "$g_last_comment_copied_to_s42", 0),
                     (try_begin),
                       (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
                       (call_script, "script_get_relevant_comment_to_s42"),
                       (assign, "$g_comment_found", reg0),
                     (try_end),

                     (troop_get_type, reg65, "$g_talk_troop"),
                     (try_begin),
                       (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                       (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                       (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                       (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
                       (str_store_string,s67,"@{reg65?My Lady:My Lord}"), #bug fix
                     (else_try),
                       (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                       (str_store_string,s65,"@{reg65?madame:sir}"),
                       (str_store_string,s66,"@{reg65?Madame:Sir}"),
                       (str_store_string,s67,"@{reg65?Madame:Sir}"), #bug fix
                     (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$talk_context"),
						(display_message, "@{!}DEBUG -- Talk context: {reg4}"),
					 (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$g_time_since_last_talk"),
						(display_message, "@{!}DEBUG -- Time since last talk: {reg4}"),
					 (try_end),
					 
					 
					 (try_begin),
						(eq, "$cheat_mode", 0),
						(store_partner_quest, ":quest"),
						(ge, ":quest", 0),
						(str_store_quest_name, s4, ":quest"),
						
					 (try_end),
					 
                     (eq, 1, 0)
  ```

### module_factions.py

- **Имя массива:** `default_kingdom_relations`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```python
  [0] ("outlaws",-0.05)
  [1] ("peasant_rebels", -0.1)
  [2] ("deserters", -0.05)
  [3] ("mountain_bandits", -0.02)
  [4] ("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [
  ```

### module_game_menus.py

- **Имя массива:** `game_menus`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] ("start_game_0",menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Welcome, adventurer, to Mount and Blade: Warband. Before beginning the game you must create your character. Remember that in the traditional medieval society depicted in the game, war and politics are usually dominated by male members of the nobility. That does not however mean that you should not choose to play a female character, or one who is not of noble birth. Male nobles may have a somewhat easier start, but women and commoners can attain all of the same goals -- and in fact may have a much more interesting if more challenging early game.",
    "none",
    [
  ```

### module_info.py

*Не удалось определить структуру*

### module_info_pages.py

*Не удалось определить структуру*

### module_items.py

- **Имя массива:** `items`
- **Количество элементов в кортеже:** 11
- **Структура первого элемента:**
  ```python
  [0] # item_name
  [1] mesh_name
  [2] item_properties
  [3] item_capabilities
  [4] slot_no
  ```

### module_map_icons.py

*Не удалось определить структуру*

### module_meshes.py

*Не удалось определить структуру*

### module_mission_templates.py

- **Имя массива:** `pilgrim_disguise`
- **Количество элементов в кортеже:** 7
- **Структура первого элемента:**
  ```python
  [0] itm_pilgrim_hood
  [1] itm_pilgrim_disguise
  [2] itm_practice_staff
  [3] itm_throwing_daggers]
af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian

multiplayer_server_check_belfry_movement = (
  0
  [4] 0
  ```

### module_music.py

*Не удалось определить структуру*

### module_particle_systems.py

*Не удалось определить структуру*

### module_parties.py

- **Имя массива:** `parties`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```python
  [0] ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)])
  [1] ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1","Sargoth",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.6, 79.7),[
  ```

### module_party_templates.py

*Не удалось определить структуру*

### module_postfx.py

- **Имя массива:** `postfx_params`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] ("default", 0, 0, [125.9922, 1.0588, 1.4510, 9.1765
  ```

### module_presentations.py

*Не удалось определить структуру*

### module_quests.py

*Не удалось определить структуру*

### module_scene_props.py

*Не удалось определить структуру*

### module_scenes.py

- **Имя массива:** `scenes`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [
  ```

### module_scripts.py

*Не удалось определить структуру*

### module_simple_triggers.py

*Не удалось определить структуру*

### module_skills.py

*Не удалось определить структуру*

### module_skins.py

- **Имя массива:** `man_face_keys`
- **Количество элементов в кортеже:** 57
- **Структура первого элемента:**
  ```python
  [0] (20,0, 0.7,-0.6, "Chin Size")
  [1] (260,0, -0.6,1.4, "Chin Shape")
  [2] (10,0,-0.5,0.9, "Chin Forward")
  [3] (240,0,0.9,-0.8, "Jaw Width")
  [4] (210,0,-0.5,1.0, "Jaw Position")
  ```

### module_sounds.py

*Не удалось определить структуру*

### module_strings.py

*Не удалось определить структуру*

### module_tableau_materials.py

*Не удалось определить структуру*

### module_triggers.py

- **Имя массива:** `triggers`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] # Tutorial:
  (0.1, 0, ti_once, [(map_free,0)
  ```

### module_troops.py

- **Имя массива:** `troops`
- **Количество элементов в кортеже:** 1
- **Структура первого элемента:**
  ```python
  [0] ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [
  ```

### module_variables.py

*Не удалось определить структуру*


## 3. РЕЕСТР ГЛОБАЛЬНЫХ ПЕРЕМЕННЫХ

### Использованные глобальные переменные ($var):

- `$Num_log_entries`
- `$ai_battle_tactic`
- `$ai_team_1`
- `$ai_team_1_battle_tactic`
- `$ai_team_2`
- `$ai_team_2_battle_tactic`
- `$all_doors_locked`
- `$any_allies_at_the_last_battle`
- `$arena_bet_amount`
- `$attacker_reinforcement_stage`
- `$attacker_team`
- `$attacker_team_2`
- `$auto_besiege_town`
- `$auto_enter_town`
- `$battle_renown_value`
- `$belfry_num_men_pushing`
- `$belfry_num_slots_positioned`
- `$belfry_positioned`
- `$belfry_rotating_objects_begin`
- `$borcha_arrive_sargoth_as_prisoner`
- `$borcha_asked_for_freedom`
- `$borcha_freed`
- `$cant_leave_encounter`
- `$cant_talk_to_enemy`
- `$captivity_end_menu`
- `$captivity_end_time`
- `$captivity_mode`
- `$capture_screen_shown`
- `$capturer_party`
- `$caravan_escort_destination_town`
- `$caravan_escort_party_id`
- `$caravan_escort_state`
- `$character_gender`
- `$cheat_mode`
- `$cur_belfry_pos`
- `$current_town`
- `$debt_to_merchants_guild`
- `$debug_message_in_queue`
- `$defender_team`
- `$disable_npc_complaints`
- `$do_not_cancel_quest`
- `$escort_merchant_caravan_mode`
- `$g_advantegous_faction`
- `$g_alarm_modula`
- `$g_ally_party`
- `$g_attacker_drawn_weapon`
- `$g_average_center_value_per_faction`
- `$g_bandit_party_for_bounty`
- `$g_battle_allies_dead`
- `$g_battle_allies_ready`
- `$g_battle_allies_routed`
- `$g_battle_allies_wounded`
- `$g_battle_death_mode_started`
- `$g_battle_enemies_dead`
- `$g_battle_enemies_ready`
- `$g_battle_enemies_routed`
- `$g_battle_enemies_wounded`
- `$g_battle_map_archers_order_flag`
- `$g_battle_map_cavalry_order_flag`
- `$g_battle_map_height`
- `$g_battle_map_infantry_order_flag`
- `$g_battle_map_scale`
- `$g_battle_map_width`
- `$g_battle_result`
- `$g_battle_simulation_auto_enter_town_after_battle`
- `$g_battle_simulation_cancel_for_party`
- `$g_battle_us_dead`
- `$g_battle_us_ready`
- `$g_battle_us_routed`
- `$g_battle_us_wounded`
- `$g_battle_waiting_seconds`
- `$g_belligerent_drunk_leaving`
- `$g_castle_requested_by_player`
- `$g_castle_requested_for_troop`
- `$g_ccoop_currently_dropping_item`
- `$g_ccoop_disallow_horses`
- `$g_ccoop_king_troop`
- `$g_center_to_give_to_player`
- `$g_check_autos_at_hour`
- `$g_close_equipment_selection`
- `$g_concession_demanded`
- `$g_confirmation_result`
- `$g_cur_week_half_daily_wage_payments`
- `$g_custom_battle_team1_death_count`
- `$g_custom_battle_team2_death_count`
- `$g_death_mode_part_1_start_time`
- `$g_defender_team`
- `$g_defending_against_siege`
- `$g_disable_condescending_comments`
- `$g_do_not_skip_other_than_current_ai_object`
- `$g_dont_give_fief_to_player_days`
- `$g_dont_give_marshalship_to_player_days`
- `$g_duel_troop`
- `$g_election_date`
- `$g_encountered_party`
- `$g_encountered_party_2`
- `$g_encountered_party_2_faction`
- `$g_encountered_party_2_relation`
- `$g_encountered_party_2_template`
- `$g_encountered_party_faction`
- `$g_encountered_party_relation`
- `$g_encountered_party_template`
- `$g_encountered_party_type`
- `$g_enemy_fit_for_battle`
- `$g_enemy_fit_for_battle_old`
- `$g_enemy_party`
- `$g_enemy_surrenders`
- `$g_engaged_enemy`
- `$g_faction_object_score`
- `$g_formation_group0_selected`
- `$g_formation_group1_selected`
- `$g_formation_group2_selected`
- `$g_formation_group3_selected`
- `$g_formation_group4_selected`
- `$g_formation_group5_selected`
- `$g_formation_group6_selected`
- `$g_formation_group7_selected`
- `$g_formation_group8_selected`
- `$g_friend_fit_for_battle`
- `$g_friend_fit_for_battle_old`
- `$g_gathering_new_started`
- `$g_gathering_reason`
- `$g_give_advantage_to_original_faction`
- `$g_horses_are_avaliable`
- `$g_include_diplo_explanation`
- `$g_infinite_camping`
- `$g_invite_faction`
- `$g_invite_faction_lord`
- `$g_invite_offered_center`
- `$g_is_quick_battle`
- `$g_last_comment_copied_to_s42`
- `$g_last_mission_player_damage`
- `$g_last_rest_center`
- `$g_leave_encounter`
- `$g_lord_long_term_count`
- `$g_main_attacker_agent`
- `$g_main_party_fit_for_battle`
- `$g_main_party_fit_for_battle_old`
- `$g_minister_notification_quest`
- `$g_move_heroes`
- `$g_mp_coop_king_waves`
- `$g_mp_coop_last_king_wave`
- `$g_mp_coop_lord_waves`
- `$g_mt_mode`
- `$g_multiplayer_allow_player_banners`
- `$g_multiplayer_auto_team_balance_limit`
- `$g_multiplayer_ban_voteable`
- `$g_multiplayer_battle_earnings_multiplier`
- `$g_multiplayer_bot_type_1_wanted`
- `$g_multiplayer_bot_type_2_wanted`
- `$g_multiplayer_bot_type_3_wanted`
- `$g_multiplayer_bot_type_4_wanted`
- `$g_multiplayer_ccoop_difficulty`
- `$g_multiplayer_ccoop_difficulty_string_i`
- `$g_multiplayer_ccoop_enable_count_down`
- `$g_multiplayer_ccoop_enemy_respawn_secs`
- `$g_multiplayer_ccoop_move_prison_cart`
- `$g_multiplayer_ccoop_next_wave_start_time`
- `$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots`
- `$g_multiplayer_ccoop_spawn_player_and_squad_counter`
- `$g_multiplayer_ccoop_wave_no`
- `$g_multiplayer_changing_game_type_allowed`
- `$g_multiplayer_disallow_ranged_weapons`
- `$g_multiplayer_duel_start_time`
- `$g_multiplayer_factions_voteable`
- `$g_multiplayer_force_default_armor`
- `$g_multiplayer_game_max_minutes`
- `$g_multiplayer_game_max_points`
- `$g_multiplayer_game_type`
- `$g_multiplayer_initial_gold_multiplier`
- `$g_multiplayer_is_game_type_captain`
- `$g_multiplayer_kick_voteable`
- `$g_multiplayer_maps_voteable`
- `$g_multiplayer_max_num_bots`
- `$g_multiplayer_message_type`
- `$g_multiplayer_message_value_1`
- `$g_multiplayer_message_value_3`
- `$g_multiplayer_mission_end_screen`
- `$g_multiplayer_next_team_1_faction`
- `$g_multiplayer_next_team_2_faction`
- `$g_multiplayer_num_bots_team_1`
- `$g_multiplayer_num_bots_team_2`
- `$g_multiplayer_num_bots_voteable`
- `$g_multiplayer_number_of_respawn_count`
- `$g_multiplayer_player_respawn_as_bot`
- `$g_multiplayer_point_gained_from_capturing_flag`
- `$g_multiplayer_point_gained_from_flags`
- `$g_multiplayer_poll_client_end_time`
- `$g_multiplayer_poll_end_time`
- `$g_multiplayer_poll_ended`
- `$g_multiplayer_poll_no_count`
- `$g_multiplayer_poll_num_sent`
- `$g_multiplayer_poll_running`
- `$g_multiplayer_poll_to_show`
- `$g_multiplayer_poll_value_2_to_show`
- `$g_multiplayer_poll_value_3_to_show`
- `$g_multiplayer_poll_value_to_show`
- `$g_multiplayer_poll_yes_count`
- `$g_multiplayer_ready_for_spawning_agent`
- `$g_multiplayer_renaming_server_allowed`
- `$g_multiplayer_respawn_period`
- `$g_multiplayer_respawn_start_time`
- `$g_multiplayer_round_earnings_multiplier`
- `$g_multiplayer_round_max_seconds`
- `$g_multiplayer_selected_map`
- `$g_multiplayer_show_poll_when_suitable`
- `$g_multiplayer_show_server_rules`
- `$g_multiplayer_stats_chart_opened_manually`
- `$g_multiplayer_team_1_faction`
- `$g_multiplayer_team_1_first_spawn`
- `$g_multiplayer_team_2_faction`
- `$g_multiplayer_team_2_first_spawn`
- `$g_multiplayer_valid_vote_ratio`
- `$g_multiplayer_welcome_message_shown`
- `$g_my_spawn_count`
- `$g_number_of_flags`
- `$g_number_of_targets_destroyed`
- `$g_permitted_to_center`
- `$g_placing_initial_flags`
- `$g_player_banner_granted`
- `$g_player_besiege_town`
- `$g_player_court`
- `$g_player_current_own_troop_kills`
- `$g_player_days_as_marshal`
- `$g_player_debt_to_party_members`
- `$g_player_eligible_feast_center_no`
- `$g_player_follow_army_warnings`
- `$g_player_is_captive`
- `$g_player_luck`
- `$g_player_minister`
- `$g_player_party_icon`
- `$g_player_party_morale_modifier_debt`
- `$g_player_party_morale_modifier_food`
- `$g_player_party_morale_modifier_leadership`
- `$g_player_party_morale_modifier_no_food`
- `$g_player_party_morale_modifier_party_size`
- `$g_player_raiding_village`
- `$g_player_surrenders`
- `$g_pointer_arrow_height_adder`
- `$g_position_to_use_for_replacing_scene_items`
- `$g_presentation_but0_movement`
- `$g_presentation_but0_riding`
- `$g_presentation_but0_weapon_usage`
- `$g_presentation_but1_movement`
- `$g_presentation_but1_riding`
- `$g_presentation_but1_weapon_usage`
- `$g_presentation_but2_movement`
- `$g_presentation_but2_riding`
- `$g_presentation_but2_weapon_usage`
- `$g_presentation_but3_movement`
- `$g_presentation_but3_riding`
- `$g_presentation_but3_weapon_usage`
- `$g_presentation_but4_movement`
- `$g_presentation_but4_riding`
- `$g_presentation_but4_weapon_usage`
- `$g_presentation_but5_movement`
- `$g_presentation_but5_riding`
- `$g_presentation_but5_weapon_usage`
- `$g_presentation_but6_movement`
- `$g_presentation_but6_riding`
- `$g_presentation_but6_weapon_usage`
- `$g_presentation_but7_movement`
- `$g_presentation_but7_riding`
- `$g_presentation_but7_weapon_usage`
- `$g_presentation_but8_movement`
- `$g_presentation_but8_riding`
- `$g_presentation_but8_weapon_usage`
- `$g_presentation_obj_admin_panel_12`
- `$g_presentation_obj_battle_but0`
- `$g_presentation_obj_battle_but1`
- `$g_presentation_obj_battle_but2`
- `$g_presentation_obj_battle_but3`
- `$g_presentation_obj_battle_but4`
- `$g_presentation_obj_battle_but5`
- `$g_presentation_obj_battle_but6`
- `$g_presentation_obj_battle_but7`
- `$g_presentation_obj_battle_but8`
- `$g_presentation_obj_battle_check0`
- `$g_presentation_obj_battle_check1`
- `$g_presentation_obj_battle_check2`
- `$g_presentation_obj_battle_check3`
- `$g_presentation_obj_battle_check4`
- `$g_presentation_obj_battle_check5`
- `$g_presentation_obj_battle_check6`
- `$g_presentation_obj_battle_check7`
- `$g_presentation_obj_battle_check8`
- `$g_presentation_obj_battle_name0`
- `$g_presentation_obj_battle_name1`
- `$g_presentation_obj_battle_name2`
- `$g_presentation_obj_battle_name3`
- `$g_presentation_obj_battle_name4`
- `$g_presentation_obj_battle_name5`
- `$g_presentation_obj_battle_name6`
- `$g_presentation_obj_battle_name7`
- `$g_presentation_obj_battle_name8`
- `$g_presentation_obj_coop_companion_0`
- `$g_presentation_obj_coop_companion_1`
- `$g_presentation_obj_coop_companion_class_0`
- `$g_presentation_obj_coop_companion_class_1`
- `$g_presentation_obj_item_select_12`
- `$g_prison_cart_point`
- `$g_prison_cart_previous_point`
- `$g_prison_heroes`
- `$g_quick_battle_army_1_size`
- `$g_quick_battle_army_2_size`
- `$g_quick_battle_game_type`
- `$g_quick_battle_map`
- `$g_quick_battle_team_0_banner`
- `$g_quick_battle_team_1_banner`
- `$g_quick_battle_team_1_faction`
- `$g_quick_battle_team_2_faction`
- `$g_quick_battle_troop`
- `$g_ransom_offer_party`
- `$g_ransom_offer_rejected`
- `$g_ransom_offer_troop`
- `$g_recalculate_ais`
- `$g_rejoinder_to_last_comment`
- `$g_round_day_time`
- `$g_round_ended`
- `$g_round_finish_time`
- `$g_round_start_time`
- `$g_show_no_more_respawns_remained`
- `$g_siege_method`
- `$g_start_arena_fight_at_nearest_town`
- `$g_start_belligerent_drunk_fight`
- `$g_start_hired_assassin_fight`
- `$g_starting_strength_ally_party`
- `$g_starting_strength_enemy_party`
- `$g_starting_strength_friends`
- `$g_starting_strength_main_party`
- `$g_starting_town`
- `$g_strength_contribution_of_player`
- `$g_talk_troop`
- `$g_talk_troop_faction`
- `$g_talk_troop_faction_relation`
- `$g_talk_troop_met`
- `$g_talk_troop_relation`
- `$g_target_after_gathering`
- `$g_team_balance_next_round`
- `$g_there_is_no_avaliable_centers`
- `$g_total_quests_completed`
- `$g_tournament_bet_placed`
- `$g_tournament_bet_win_amount`
- `$g_tournament_cur_tier`
- `$g_tournament_last_bet_tier`
- `$g_tournament_num_participants_for_fight`
- `$g_tournament_player_team_won`
- `$g_training_ground_ranged_distance`
- `$g_training_ground_training_count`
- `$g_training_ground_training_hardness`
- `$g_training_ground_training_num_enemies`
- `$g_training_ground_training_num_gourds_to_destroy`
- `$g_training_ground_training_scene`
- `$g_training_ground_training_troop_stack_index`
- `$g_training_ground_used_weapon_proficiency`
- `$g_troop_list_no`
- `$g_use_current_ai_object_as_s8`
- `$g_waiting_for_confirmation_to_terminate`
- `$g_wedding_bishop_troop`
- `$g_wedding_bride_troop`
- `$g_wedding_brides_dad_troop`
- `$g_wedding_groom_troop`
- `$g_winner_team`
- `$group0_has_troops`
- `$group1_has_troops`
- `$group2_has_troops`
- `$group3_has_troops`
- `$group4_has_troops`
- `$group5_has_troops`
- `$group6_has_troops`
- `$group7_has_troops`
- `$group8_has_troops`
- `$incriminate_quest_sacrificed_troop`
- `$last_belfry_object_pos`
- `$last_defeated_hero`
- `$last_freed_hero`
- `$log_comment_relation_change`
- `$loot_screen_shown`
- `$marriage_candidate`
- `$marshall_defeated_in_battle`
- `$merchant_offered_quest`
- `$merchant_quest_last_offerer`
- `$new_encounter`
- `$newglob_total_prosperity_from_bandits`
- `$newglob_total_prosperity_from_caravan_trade`
- `$newglob_total_prosperity_from_convergence`
- `$newglob_total_prosperity_from_townloot`
- `$newglob_total_prosperity_from_village_trade`
- `$newglob_total_prosperity_from_villageloot`
- `$newglob_total_prosperity_gains`
- `$newglob_total_prosperity_losses`
- `$npc_grievance_slot`
- `$npc_grievance_string`
- `$npc_is_quitting`
- `$npc_map_talk_context`
- `$npc_praise_not_complaint`
- `$npc_to_rejoin_party`
- `$npc_with_grievance`
- `$npc_with_personality_clash`
- `$npc_with_personality_clash_2`
- `$npc_with_personality_match`
- `$npc_with_political_grievance`
- `$num_center_bandits`
- `$num_log_entries`
- `$num_routed_allies`
- `$num_routed_enemies`
- `$num_routed_us`
- `$number_of_controversial_policy_decisions`
- `$number_of_npc_slots`
- `$number_of_report_to_army_quest_notes`
- `$peak_dark_hunters`
- `$peak_swadian_foragers`
- `$peak_swadian_harassers`
- `$peak_swadian_scouts`
- `$peak_swadian_war_parties`
- `$peak_vaegir_foragers`
- `$peak_vaegir_harassers`
- `$peak_vaegir_scouts`
- `$peak_vaegir_war_parties`
- `$personality_clash_after_24_hrs`
- `$pin_faction`
- `$pin_limit`
- `$pin_number`
- `$pin_party_template`
- `$pin_player_fallen`
- `$player_has_homage`
- `$player_honor`
- `$player_marshal_ai_object`
- `$player_marshal_ai_state`
- `$player_party__regulars`
- `$player_party_contains_regulars`
- `$player_right_to_rule`
- `$playerparty_prebattle_regulars`
- `$players_kingdom`
- `$players_kingdom_days_at_peace`
- `$players_oath_renounced_against_kingdom`
- `$players_oath_renounced_begin_time`
- `$players_oath_renounced_given_center`
- `$pout_party`
- `$pout_town`
- `$qst_bring_back_runaway_serfs_num_parties_fleed`
- `$qst_bring_back_runaway_serfs_num_parties_returned`
- `$qst_bring_back_runaway_serfs_party_1`
- `$qst_bring_back_runaway_serfs_party_2`
- `$qst_bring_back_runaway_serfs_party_3`
- `$qst_capture_conspirators_leave_meeting_counter`
- `$qst_capture_conspirators_num_parties_spawned`
- `$qst_capture_conspirators_num_parties_to_spawn`
- `$qst_capture_conspirators_num_troops_to_capture`
- `$qst_capture_conspirators_party_1`
- `$qst_capture_conspirators_party_2`
- `$qst_capture_conspirators_party_3`
- `$qst_capture_conspirators_party_4`
- `$qst_capture_conspirators_party_5`
- `$qst_capture_conspirators_party_6`
- `$qst_capture_conspirators_party_7`
- `$qst_defend_nobles_against_peasants_noble_party_1`
- `$qst_defend_nobles_against_peasants_noble_party_2`
- `$qst_defend_nobles_against_peasants_noble_party_3`
- `$qst_defend_nobles_against_peasants_noble_party_4`
- `$qst_defend_nobles_against_peasants_noble_party_5`
- `$qst_defend_nobles_against_peasants_noble_party_6`
- `$qst_defend_nobles_against_peasants_noble_party_7`
- `$qst_defend_nobles_against_peasants_noble_party_8`
- `$qst_defend_nobles_against_peasants_num_noble_parties_to_spawn`
- `$qst_defend_nobles_against_peasants_num_nobles_saved`
- `$qst_defend_nobles_against_peasants_num_nobles_to_save`
- `$qst_defend_nobles_against_peasants_num_peasant_parties_to_spawn`
- `$qst_defend_nobles_against_peasants_peasant_party_1`
- `$qst_defend_nobles_against_peasants_peasant_party_2`
- `$qst_defend_nobles_against_peasants_peasant_party_3`
- `$qst_defend_nobles_against_peasants_peasant_party_4`
- `$qst_defend_nobles_against_peasants_peasant_party_5`
- `$qst_defend_nobles_against_peasants_peasant_party_6`
- `$qst_defend_nobles_against_peasants_peasant_party_7`
- `$qst_defend_nobles_against_peasants_peasant_party_8`
- `$qst_deliver_wine_debt`
- `$qst_follow_spy_meeting_counter`
- `$qst_follow_spy_meeting_state`
- `$qst_follow_spy_no_active_parties`
- `$qst_follow_spy_partner_back_in_town`
- `$qst_follow_spy_run_away`
- `$qst_follow_spy_spy_back_in_town`
- `$qst_follow_spy_spy_partners_party`
- `$qst_follow_spy_spy_party`
- `$qst_troublesome_bandits_eliminated`
- `$qst_troublesome_bandits_eliminated_by_player`
- `$romantic_attraction_seed`
- `$routed_party_added`
- `$scene_num_total_gourds_destroyed`
- `$server_mission_timer_while_player_joined`
- `$sneaked_into_town`
- `$spy_item_worn`
- `$spy_quest_troop`
- `$supported_pretender`
- `$supported_pretender_old_faction`
- `$talk_context`
- `$talked_with_merchant`
- `$team_1_flag_scene_prop`
- `$team_2_flag_scene_prop`
- `$temp`
- `$temp_2`
- `$temp_3`
- `$thanked_by_ally_leader`
- `$total_battle_ally_changes`
- `$total_battle_enemy_changes`
- `$total_courtship_quarrel_changes`
- `$total_feast_changes`
- `$total_indictment_changes`
- `$total_joy_battle_changes`
- `$total_no_fief_changes`
- `$total_policy_dispute_changes`
- `$total_political_events`
- `$total_promotion_changes`
- `$total_random_quarrel_changes`
- `$total_relation_adds`
- `$total_relation_changes_through_convergence`
- `$total_relation_subs`
- `$total_vassal_days_on_campaign`
- `$total_vassal_days_responding_to_campaign`
- `$town_entered`
- `$town_nighttime`
- `$waiting_for_arena_fight_result`


## 4. РЕЕСТР ЛОКАЛЬНЫХ РЕГИСТРОВ И СТРОК

### Паттерны использования регистров:

| Регистр | Количество использований |
|---------|-------------------------|
| s1 | 652 |
| s4 | 571 |
| s11 | 417 |
| s5 | 391 |
| s0 | 364 |
| s12 | 351 |
| s14 | 337 |
| s2 | 322 |
| s9 | 291 |
| s3 | 283 |
| s10 | 241 |
| s15 | 206 |
| s8 | 177 |
| s13 | 167 |
| s7 | 137 |
| s16 | 88 |
| s6 | 87 |
| s17 | 87 |
| s65 | 72 |
| s21 | 69 |
| s51 | 39 |
| s50 | 38 |
| s43 | 36 |
| s54 | 28 |
| s18 | 24 |
| s46 | 24 |
| s42 | 20 |
| s32 | 20 |
| s61 | 19 |
| s49 | 15 |
| s62 | 15 |
| s45 | 15 |
| s31 | 15 |
| s66 | 15 |
| s57 | 14 |
| s59 | 14 |
| s47 | 14 |
| s44 | 13 |
| s58 | 12 |
| s63 | 12 |
| s19 | 12 |
| s39 | 11 |
| s56 | 9 |
| s40 | 9 |
| s48 | 9 |
| s24 | 9 |
| s60 | 8 |
| s41 | 8 |
| s22 | 8 |
| s55 | 7 |
