# 🗺️ WARBRAND CODE MAP

Auto-generated analysis of Warband Module System v1.171

============================================================


## 1. КОНСТАНТЫ И ИДЕНТИФИКАТОРЫ

### ID_animations.py

| Константа | Значение |
|-----------|----------|
| anim_stand | 0 |
| anim_stand_man | 1 |
| anim_stand_player_first_person | 2 |
| anim_jump | 3 |
| anim_jump_loop | 4 |
| anim_jump_end | 5 |
| anim_jump_end_hard | 6 |
| anim_stand_unarmed | 7 |
| anim_stand_single | 8 |
| anim_stand_greatsword | 9 |
| anim_stand_staff | 10 |
| anim_stand_crossbow | 11 |
| anim_turn_right | 12 |
| anim_turn_left | 13 |
| anim_turn_right_single | 14 |
| anim_turn_left_single | 15 |
| anim_turn_right_staff | 16 |
| anim_turn_left_staff | 17 |
| anim_turn_right_greatsword | 18 |
| anim_turn_left_greatsword | 19 |
| anim_prepare_kick_0 | 20 |
| anim_prepare_kick_1 | 21 |
| anim_prepare_kick_2 | 22 |
| anim_prepare_kick_3 | 23 |
| anim_kick_right_leg | 24 |
| anim_kick_left_leg | 25 |
| anim_run_forward | 26 |
| anim_run_forward_onehanded | 27 |
| anim_run_forward_staff | 28 |
| anim_run_forward_greatsword | 29 |
| anim_run_forward_hips_right | 30 |
| anim_run_forward_hips_left | 31 |
| anim_run_forward_right | 32 |
| anim_run_forward_right_onehanded | 33 |
| anim_run_forward_right_staff | 34 |
| anim_run_forward_right_greatsword | 35 |
| anim_run_forward_right_hips_right | 36 |
| anim_run_forward_right_hips_left | 37 |
| anim_run_forward_left | 38 |
| anim_run_forward_left_onehanded | 39 |
| anim_run_forward_left_staff | 40 |
| anim_run_forward_left_greatsword | 41 |
| anim_run_forward_left_hips_right | 42 |
| anim_run_forward_left_hips_left | 43 |
| anim_run_backward | 44 |
| anim_run_backward_onehanded | 45 |
| anim_run_backward_staff | 46 |
| anim_run_backward_greatsword | 47 |
| anim_run_backward_hips_right | 48 |
| anim_run_backward_hips_left | 49 |
| ... | (ещё 620 констант) |

### ID_factions.py

| Константа | Значение |
|-----------|----------|
| fac_no_faction | 0 |
| fac_commoners | 1 |
| fac_outlaws | 2 |
| fac_neutral | 3 |
| fac_innocents | 4 |
| fac_merchants | 5 |
| fac_dark_knights | 6 |
| fac_culture_1 | 7 |
| fac_culture_2 | 8 |
| fac_culture_3 | 9 |
| fac_culture_4 | 10 |
| fac_culture_5 | 11 |
| fac_culture_6 | 12 |
| fac_player_faction | 13 |
| fac_player_supporters_faction | 14 |
| fac_kingdom_1 | 15 |
| fac_kingdom_2 | 16 |
| fac_kingdom_3 | 17 |
| fac_kingdom_4 | 18 |
| fac_kingdom_5 | 19 |
| fac_kingdom_6 | 20 |
| fac_kingdoms_end | 21 |
| fac_robber_knights | 22 |
| fac_khergits | 23 |
| fac_black_khergits | 24 |
| fac_manhunters | 25 |
| fac_deserters | 26 |
| fac_mountain_bandits | 27 |
| fac_forest_bandits | 28 |
| fac_undeads | 29 |
| fac_slavers | 30 |
| fac_peasant_rebels | 31 |
| fac_noble_refugees | 32 |
| fac_ccoop_all_stars | 33 |

### ID_info_pages.py

| Константа | Значение |
|-----------|----------|
| ip_morale | 0 |
| ip_economy | 1 |
| ip_courtship | 2 |
| ip_politics | 3 |
| ip_character_backgrounds | 4 |
| ip_military_campaigns | 5 |

### ID_items.py

| Константа | Значение |
|-----------|----------|
| itm_no_item | 0 |
| itm_tutorial_spear | 1 |
| itm_tutorial_club | 2 |
| itm_tutorial_battle_axe | 3 |
| itm_tutorial_arrows | 4 |
| itm_tutorial_bolts | 5 |
| itm_tutorial_short_bow | 6 |
| itm_tutorial_crossbow | 7 |
| itm_tutorial_throwing_daggers | 8 |
| itm_tutorial_saddle_horse | 9 |
| itm_tutorial_shield | 10 |
| itm_tutorial_staff_no_attack | 11 |
| itm_tutorial_staff | 12 |
| itm_tutorial_sword | 13 |
| itm_tutorial_axe | 14 |
| itm_tutorial_dagger | 15 |
| itm_horse_meat | 16 |
| itm_practice_sword | 17 |
| itm_heavy_practice_sword | 18 |
| itm_practice_dagger | 19 |
| itm_practice_axe | 20 |
| itm_arena_axe | 21 |
| itm_arena_sword | 22 |
| itm_arena_sword_two_handed | 23 |
| itm_arena_lance | 24 |
| itm_practice_staff | 25 |
| itm_practice_lance | 26 |
| itm_practice_shield | 27 |
| itm_practice_bow | 28 |
| itm_practice_crossbow | 29 |
| itm_practice_javelin | 30 |
| itm_practice_javelin_melee | 31 |
| itm_practice_throwing_daggers | 32 |
| itm_practice_throwing_daggers_100_amount | 33 |
| itm_practice_horse | 34 |
| itm_practice_arrows | 35 |
| itm_practice_bolts | 36 |
| itm_practice_arrows_10_amount | 37 |
| itm_practice_arrows_100_amount | 38 |
| itm_practice_bolts_9_amount | 39 |
| itm_practice_boots | 40 |
| itm_red_tourney_armor | 41 |
| itm_blue_tourney_armor | 42 |
| itm_green_tourney_armor | 43 |
| itm_gold_tourney_armor | 44 |
| itm_red_tourney_helmet | 45 |
| itm_blue_tourney_helmet | 46 |
| itm_green_tourney_helmet | 47 |
| itm_gold_tourney_helmet | 48 |
| itm_arena_shield_red | 49 |
| ... | (ещё 570 констант) |

### ID_map_icons.py

| Константа | Значение |
|-----------|----------|
| icon_player | 0 |
| icon_player_horseman | 1 |
| icon_gray_knight | 2 |
| icon_vaegir_knight | 3 |
| icon_flagbearer_a | 4 |
| icon_flagbearer_b | 5 |
| icon_peasant | 6 |
| icon_khergit | 7 |
| icon_khergit_horseman_b | 8 |
| icon_axeman | 9 |
| icon_woman | 10 |
| icon_woman_b | 11 |
| icon_town | 12 |
| icon_town_steppe | 13 |
| icon_town_desert | 14 |
| icon_village_a | 15 |
| icon_village_b | 16 |
| icon_village_c | 17 |
| icon_village_burnt_a | 18 |
| icon_village_deserted_a | 19 |
| icon_village_burnt_b | 20 |
| icon_village_deserted_b | 21 |
| icon_village_burnt_c | 22 |
| icon_village_deserted_c | 23 |
| icon_village_snow_a | 24 |
| icon_village_snow_burnt_a | 25 |
| icon_village_snow_deserted_a | 26 |
| icon_camp | 27 |
| icon_ship | 28 |
| icon_ship_on_land | 29 |
| icon_castle_a | 30 |
| icon_castle_b | 31 |
| icon_castle_c | 32 |
| icon_castle_d | 33 |
| icon_town_snow | 34 |
| icon_castle_snow_a | 35 |
| icon_castle_snow_b | 36 |
| icon_mule | 37 |
| icon_cattle | 38 |
| icon_training_ground | 39 |
| icon_bridge_a | 40 |
| icon_bridge_b | 41 |
| icon_bridge_snow_a | 42 |
| icon_custom_banner_01 | 43 |
| icon_custom_banner_02 | 44 |
| icon_custom_banner_03 | 45 |
| icon_banner_01 | 46 |
| icon_banner_02 | 47 |
| icon_banner_03 | 48 |
| icon_banner_04 | 49 |
| ... | (ещё 139 констант) |

### ID_menus.py

| Константа | Значение |
|-----------|----------|
| menu_start_game_0 | 0 |
| menu_start_phase_2 | 1 |
| menu_start_game_3 | 2 |
| menu_tutorial | 3 |
| menu_reports | 4 |
| menu_custom_battle_scene | 5 |
| menu_custom_battle_end | 6 |
| menu_start_game_1 | 7 |
| menu_start_character_1 | 8 |
| menu_start_character_2 | 9 |
| menu_start_character_3 | 10 |
| menu_start_character_4 | 11 |
| menu_choose_skill | 12 |
| menu_past_life_explanation | 13 |
| menu_auto_return | 14 |
| menu_morale_report | 15 |
| menu_courtship_relations | 16 |
| menu_lord_relations | 17 |
| menu_companion_report | 18 |
| menu_faction_orders | 19 |
| menu_character_report | 20 |
| menu_party_size_report | 21 |
| menu_faction_relations_report | 22 |
| menu_camp | 23 |
| menu_camp_cheat | 24 |
| menu_cheat_find_item | 25 |
| menu_cheat_change_weather | 26 |
| menu_camp_action | 27 |
| menu_camp_recruit_prisoners | 28 |
| menu_camp_no_prisoners | 29 |
| menu_camp_action_read_book | 30 |
| menu_camp_action_read_book_start | 31 |
| menu_retirement_verify | 32 |
| menu_end_game | 33 |
| menu_cattle_herd | 34 |
| menu_cattle_herd_kill | 35 |
| menu_cattle_herd_kill_end | 36 |
| menu_arena_duel_fight | 37 |
| menu_arena_duel_conclusion | 38 |
| menu_simple_encounter | 39 |
| menu_encounter_retreat_confirm | 40 |
| menu_encounter_retreat | 41 |
| menu_order_attack_begin | 42 |
| menu_order_attack_2 | 43 |
| menu_battle_debrief | 44 |
| menu_total_victory | 45 |
| menu_enemy_slipped_away | 46 |
| menu_total_defeat | 47 |
| menu_permanent_damage | 48 |
| menu_pre_join | 49 |
| ... | (ещё 167 констант) |

### ID_meshes.py

| Константа | Значение |
|-----------|----------|
| mesh_pic_bandits | 0 |
| mesh_pic_mb_warrior_1 | 1 |
| mesh_pic_messenger | 2 |
| mesh_pic_prisoner_man | 3 |
| mesh_pic_prisoner_fem | 4 |
| mesh_pic_prisoner_wilderness | 5 |
| mesh_pic_siege_sighted | 6 |
| mesh_pic_siege_sighted_fem | 7 |
| mesh_pic_camp | 8 |
| mesh_pic_payment | 9 |
| mesh_pic_escape_1 | 10 |
| mesh_pic_escape_1_fem | 11 |
| mesh_pic_victory | 12 |
| mesh_pic_defeat | 13 |
| mesh_pic_wounded | 14 |
| mesh_pic_wounded_fem | 15 |
| mesh_pic_steppe_bandits | 16 |
| mesh_pic_mountain_bandits | 17 |
| mesh_pic_sea_raiders | 18 |
| mesh_pic_deserters | 19 |
| mesh_pic_forest_bandits | 20 |
| mesh_pic_cattle | 21 |
| mesh_pic_looted_village | 22 |
| mesh_pic_village_p | 23 |
| mesh_pic_village_s | 24 |
| mesh_pic_village_w | 25 |
| mesh_pic_recruits | 26 |
| mesh_pic_arms_swadian | 27 |
| mesh_pic_arms_vaegir | 28 |
| mesh_pic_arms_khergit | 29 |
| mesh_pic_arms_nord | 30 |
| mesh_pic_arms_rhodok | 31 |
| mesh_pic_sarranid_arms | 32 |
| mesh_pic_castle1 | 33 |
| mesh_pic_castledes | 34 |
| mesh_pic_castlesnow | 35 |
| mesh_pic_charge | 36 |
| mesh_pic_khergit | 37 |
| mesh_pic_nord | 38 |
| mesh_pic_rhodock | 39 |
| mesh_pic_sally_out | 40 |
| mesh_pic_siege_attack | 41 |
| mesh_pic_swad | 42 |
| mesh_pic_town1 | 43 |
| mesh_pic_towndes | 44 |
| mesh_pic_townriot | 45 |
| mesh_pic_townsnow | 46 |
| mesh_pic_vaegir | 47 |
| mesh_pic_villageriot | 48 |
| mesh_pic_sarranid_encounter | 49 |
| ... | (ещё 505 констант) |

### ID_mission_templates.py

| Константа | Значение |
|-----------|----------|
| mst_town_default | 0 |
| mst_conversation_encounter | 1 |
| mst_town_center | 2 |
| mst_village_center | 3 |
| mst_bandits_at_night | 4 |
| mst_village_training | 5 |
| mst_visit_town_castle | 6 |
| mst_back_alley_kill_local_merchant | 7 |
| mst_back_alley_revolt | 8 |
| mst_lead_charge | 9 |
| mst_village_attack_bandits | 10 |
| mst_village_raid | 11 |
| mst_besiege_inner_battle_castle | 12 |
| mst_besiege_inner_battle_town_center | 13 |
| mst_castle_attack_walls_defenders_sally | 14 |
| mst_castle_attack_walls_belfry | 15 |
| mst_castle_attack_walls_ladder | 16 |
| mst_castle_visit | 17 |
| mst_training_ground_trainer_talk | 18 |
| mst_training_ground_trainer_training | 19 |
| mst_training_ground_training | 20 |
| mst_sneak_caught_fight | 21 |
| mst_ai_training | 22 |
| mst_camera_test | 23 |
| mst_arena_melee_fight | 24 |
| mst_arena_challenge_fight | 25 |
| mst_duel_with_lord | 26 |
| mst_wedding | 27 |
| mst_tutorial_training_ground | 28 |
| mst_tutorial_1 | 29 |
| mst_tutorial_2 | 30 |
| mst_tutorial_3 | 31 |
| mst_tutorial_3_2 | 32 |
| mst_tutorial_4 | 33 |
| mst_tutorial_5 | 34 |
| mst_quick_battle_battle | 35 |
| mst_quick_battle_siege | 36 |
| mst_multiplayer_dm | 37 |
| mst_multiplayer_tdm | 38 |
| mst_multiplayer_hq | 39 |
| mst_multiplayer_cf | 40 |
| mst_multiplayer_sg | 41 |
| mst_multiplayer_bt | 42 |
| mst_multiplayer_fd | 43 |
| mst_multiplayer_ccoop | 44 |
| mst_bandit_lair | 45 |
| mst_alley_fight | 46 |
| mst_meeting_merchant | 47 |
| mst_town_fight | 48 |
| mst_multiplayer_duel | 49 |

### ID_music.py

| Константа | Значение |
|-----------|----------|
| track_bogus | 0 |
| track_mount_and_blade_title_screen | 1 |
| track_ambushed_by_neutral | 2 |
| track_ambushed_by_khergit | 3 |
| track_ambushed_by_nord | 4 |
| track_ambushed_by_rhodok | 5 |
| track_ambushed_by_swadian | 6 |
| track_ambushed_by_vaegir | 7 |
| track_ambushed_by_sarranid | 8 |
| track_arena_1 | 9 |
| track_armorer | 10 |
| track_bandit_fight | 11 |
| track_calm_night_1 | 12 |
| track_captured | 13 |
| track_defeated_by_neutral | 14 |
| track_defeated_by_neutral_2 | 15 |
| track_defeated_by_neutral_3 | 16 |
| track_empty_village | 17 |
| track_encounter_hostile_nords | 18 |
| track_escape | 19 |
| track_fight_1 | 20 |
| track_fight_2 | 21 |
| track_fight_3 | 22 |
| track_fight_as_khergit | 23 |
| track_fight_4 | 24 |
| track_fight_as_nord | 25 |
| track_fight_as_rhodok | 26 |
| track_fight_as_vaegir | 27 |
| track_fight_while_mounted_1 | 28 |
| track_fight_while_mounted_2 | 29 |
| track_fight_while_mounted_3 | 30 |
| track_infiltration_khergit | 31 |
| track_killed_by_khergit | 32 |
| track_killed_by_swadian | 33 |
| track_lords_hall_khergit | 34 |
| track_lords_hall_nord | 35 |
| track_lords_hall_swadian | 36 |
| track_lords_hall_rhodok | 37 |
| track_lords_hall_vaegir | 38 |
| track_mounted_snow_terrain_calm | 39 |
| track_neutral_infiltration | 40 |
| track_outdoor_beautiful_land | 41 |
| track_retreat | 42 |
| track_seige_neutral | 43 |
| track_enter_the_juggernaut | 44 |
| track_siege_attempt | 45 |
| track_crazy_battle_music | 46 |
| track_tavern_1 | 47 |
| track_tavern_2 | 48 |
| track_town_neutral | 49 |
| ... | (ещё 24 констант) |

### ID_particle_systems.py

| Константа | Значение |
|-----------|----------|
| psys_game_rain | 0 |
| psys_game_snow | 1 |
| psys_game_blood | 2 |
| psys_game_blood_2 | 3 |
| psys_game_hoof_dust | 4 |
| psys_game_hoof_dust_snow | 5 |
| psys_game_hoof_dust_mud | 6 |
| psys_game_water_splash_1 | 7 |
| psys_game_water_splash_2 | 8 |
| psys_game_water_splash_3 | 9 |
| psys_torch_fire | 10 |
| psys_fire_glow_1 | 11 |
| psys_fire_glow_fixed | 12 |
| psys_torch_smoke | 13 |
| psys_flue_smoke_short | 14 |
| psys_flue_smoke_tall | 15 |
| psys_war_smoke_tall | 16 |
| psys_ladder_dust_6m | 17 |
| psys_ladder_dust_8m | 18 |
| psys_ladder_dust_10m | 19 |
| psys_ladder_dust_12m | 20 |
| psys_ladder_dust_14m | 21 |
| psys_ladder_straw_6m | 22 |
| psys_ladder_straw_8m | 23 |
| psys_ladder_straw_10m | 24 |
| psys_ladder_straw_12m | 25 |
| psys_ladder_straw_14m | 26 |
| psys_torch_fire_sparks | 27 |
| psys_fire_sparks_1 | 28 |
| psys_pistol_smoke | 29 |
| psys_brazier_fire_1 | 30 |
| psys_cooking_fire_1 | 31 |
| psys_cooking_smoke | 32 |
| psys_food_steam | 33 |
| psys_candle_light | 34 |
| psys_candle_light_small | 35 |
| psys_lamp_fire | 36 |
| psys_dummy_smoke | 37 |
| psys_dummy_straw | 38 |
| psys_dummy_smoke_big | 39 |
| psys_dummy_straw_big | 40 |
| psys_gourd_smoke | 41 |
| psys_gourd_piece_1 | 42 |
| psys_gourd_piece_2 | 43 |
| psys_fire_fly_1 | 44 |
| psys_bug_fly_1 | 45 |
| psys_moon_beam_1 | 46 |
| psys_moon_beam_paricle_1 | 47 |
| psys_night_smoke_1 | 48 |
| psys_fireplace_fire_small | 49 |
| ... | (ещё 10 констант) |

### ID_parties.py

| Константа | Значение |
|-----------|----------|
| p_main_party | 0 |
| p_temp_party | 1 |
| p_camp_bandits | 2 |
| p_temp_party_2 | 3 |
| p_temp_casualties | 4 |
| p_temp_casualties_2 | 5 |
| p_temp_casualties_3 | 6 |
| p_temp_wounded | 7 |
| p_temp_killed | 8 |
| p_main_party_backup | 9 |
| p_encountered_party_backup | 10 |
| p_collective_friends_backup | 11 |
| p_player_casualties | 12 |
| p_enemy_casualties | 13 |
| p_ally_casualties | 14 |
| p_collective_enemy | 15 |
| p_collective_ally | 16 |
| p_collective_friends | 17 |
| p_total_enemy_casualties | 18 |
| p_routed_enemies | 19 |
| p_zendar | 20 |
| p_town_1 | 21 |
| p_town_2 | 22 |
| p_town_3 | 23 |
| p_town_4 | 24 |
| p_town_5 | 25 |
| p_town_6 | 26 |
| p_town_7 | 27 |
| p_town_8 | 28 |
| p_town_9 | 29 |
| p_town_10 | 30 |
| p_town_11 | 31 |
| p_town_12 | 32 |
| p_town_13 | 33 |
| p_town_14 | 34 |
| p_town_15 | 35 |
| p_town_16 | 36 |
| p_town_17 | 37 |
| p_town_18 | 38 |
| p_town_19 | 39 |
| p_town_20 | 40 |
| p_town_21 | 41 |
| p_town_22 | 42 |
| p_castle_1 | 43 |
| p_castle_2 | 44 |
| p_castle_3 | 45 |
| p_castle_4 | 46 |
| p_castle_5 | 47 |
| p_castle_6 | 48 |
| p_castle_7 | 49 |
| ... | (ещё 190 констант) |

### ID_party_templates.py

| Константа | Значение |
|-----------|----------|
| pt_none | 0 |
| pt_rescued_prisoners | 1 |
| pt_enemy | 2 |
| pt_hero_party | 3 |
| pt_village_defenders | 4 |
| pt_cattle_herd | 5 |
| pt_looters | 6 |
| pt_manhunters | 7 |
| pt_steppe_bandits | 8 |
| pt_taiga_bandits | 9 |
| pt_desert_bandits | 10 |
| pt_forest_bandits | 11 |
| pt_mountain_bandits | 12 |
| pt_sea_raiders | 13 |
| pt_deserters | 14 |
| pt_merchant_caravan | 15 |
| pt_troublesome_bandits | 16 |
| pt_bandits_awaiting_ransom | 17 |
| pt_kidnapped_girl | 18 |
| pt_village_farmers | 19 |
| pt_spy_partners | 20 |
| pt_runaway_serfs | 21 |
| pt_spy | 22 |
| pt_sacrificed_messenger | 23 |
| pt_forager_party | 24 |
| pt_scout_party | 25 |
| pt_patrol_party | 26 |
| pt_messenger_party | 27 |
| pt_raider_party | 28 |
| pt_raider_captives | 29 |
| pt_kingdom_caravan_party | 30 |
| pt_prisoner_train_party | 31 |
| pt_default_prisoners | 32 |
| pt_routed_warriors | 33 |
| pt_center_reinforcements | 34 |
| pt_kingdom_hero_party | 35 |
| pt_kingdom_1_reinforcements_a | 36 |
| pt_kingdom_1_reinforcements_b | 37 |
| pt_kingdom_1_reinforcements_c | 38 |
| pt_kingdom_2_reinforcements_a | 39 |
| pt_kingdom_2_reinforcements_b | 40 |
| pt_kingdom_2_reinforcements_c | 41 |
| pt_kingdom_3_reinforcements_a | 42 |
| pt_kingdom_3_reinforcements_b | 43 |
| pt_kingdom_3_reinforcements_c | 44 |
| pt_kingdom_4_reinforcements_a | 45 |
| pt_kingdom_4_reinforcements_b | 46 |
| pt_kingdom_4_reinforcements_c | 47 |
| pt_kingdom_5_reinforcements_a | 48 |
| pt_kingdom_5_reinforcements_b | 49 |
| ... | (ещё 13 констант) |

### ID_postfx_params.py

| Константа | Значение |
|-----------|----------|
| pfx_default | 0 |
| pfx_map_params | 1 |
| pfx_indoors | 2 |
| pfx_sunset | 3 |
| pfx_night | 4 |
| pfx_sunny | 5 |
| pfx_cloudy | 6 |
| pfx_overcast | 7 |
| pfx_high_contrast | 8 |

### ID_presentations.py

| Константа | Значение |
|-----------|----------|
| prsnt_game_credits | 0 |
| prsnt_game_profile_banner_selection | 1 |
| prsnt_game_custom_battle_designer | 2 |
| prsnt_game_multiplayer_admin_panel | 3 |
| prsnt_multiplayer_welcome_message | 4 |
| prsnt_multiplayer_team_select | 5 |
| prsnt_multiplayer_troop_select | 6 |
| prsnt_multiplayer_item_select | 7 |
| prsnt_multiplayer_message_1 | 8 |
| prsnt_multiplayer_message_2 | 9 |
| prsnt_multiplayer_message_3 | 10 |
| prsnt_multiplayer_round_time_counter | 11 |
| prsnt_multiplayer_team_score_display | 12 |
| prsnt_multiplayer_flag_projection_display | 13 |
| prsnt_multiplayer_flag_projection_display_bt | 14 |
| prsnt_multiplayer_destructible_targets_display | 15 |
| prsnt_multiplayer_respawn_time_counter | 16 |
| prsnt_multiplayer_stats_chart | 17 |
| prsnt_multiplayer_stats_chart_deathmatch | 18 |
| prsnt_multiplayer_escape_menu | 19 |
| prsnt_multiplayer_poll_menu | 20 |
| prsnt_multiplayer_show_players_list | 21 |
| prsnt_multiplayer_show_maps_list | 22 |
| prsnt_multiplayer_show_factions_list | 23 |
| prsnt_multiplayer_show_number_of_bots_list | 24 |
| prsnt_multiplayer_poll | 25 |
| prsnt_tutorial_show_mouse_movement | 26 |
| prsnt_name_kingdom | 27 |
| prsnt_banner_selection | 28 |
| prsnt_custom_banner | 29 |
| prsnt_banner_charge_positioning | 30 |
| prsnt_banner_charge_selection | 31 |
| prsnt_banner_background_selection | 32 |
| prsnt_banner_flag_type_selection | 33 |
| prsnt_banner_flag_map_type_selection | 34 |
| prsnt_color_selection | 35 |
| prsnt_marshall_selection | 36 |
| prsnt_battle | 37 |
| prsnt_sliders | 38 |
| prsnt_arena_training | 39 |
| prsnt_retirement | 40 |
| prsnt_budget_report | 41 |
| prsnt_game_before_quit | 42 |
| prsnt_multiplayer_duel_start_counter | 43 |
| prsnt_multiplayer_flag_projection_display_ccoop | 44 |
| prsnt_multiplayer_flag_projection_display_ccoop_wave | 45 |
| prsnt_coop_assign_drop_to_group_member | 46 |
| prsnt_multiplayer_ccoop_next_wave_time_counter | 47 |
| prsnt_multiplayer_ccoop_victory_message | 48 |

### ID_quests.py

| Константа | Значение |
|-----------|----------|
| qst_deliver_message | 0 |
| qst_deliver_message_to_enemy_lord | 1 |
| qst_raise_troops | 2 |
| qst_escort_lady | 3 |
| qst_deal_with_bandits_at_lords_village | 4 |
| qst_collect_taxes | 5 |
| qst_hunt_down_fugitive | 6 |
| qst_kill_local_merchant | 7 |
| qst_bring_back_runaway_serfs | 8 |
| qst_follow_spy | 9 |
| qst_capture_enemy_hero | 10 |
| qst_lend_companion | 11 |
| qst_collect_debt | 12 |
| qst_incriminate_loyal_commander | 13 |
| qst_meet_spy_in_enemy_town | 14 |
| qst_capture_prisoners | 15 |
| qst_lend_surgeon | 16 |
| qst_follow_army | 17 |
| qst_report_to_army | 18 |
| qst_deliver_cattle_to_army | 19 |
| qst_join_siege_with_army | 20 |
| qst_screen_army | 21 |
| qst_scout_waypoints | 22 |
| qst_rescue_lord_by_replace | 23 |
| qst_deliver_message_to_prisoner_lord | 24 |
| qst_duel_for_lady | 25 |
| qst_duel_courtship_rival | 26 |
| qst_duel_avenge_insult | 27 |
| qst_move_cattle_herd | 28 |
| qst_escort_merchant_caravan | 29 |
| qst_deliver_wine | 30 |
| qst_troublesome_bandits | 31 |
| qst_kidnapped_girl | 32 |
| qst_persuade_lords_to_make_peace | 33 |
| qst_deal_with_looters | 34 |
| qst_deal_with_night_bandits | 35 |
| qst_deliver_grain | 36 |
| qst_deliver_cattle | 37 |
| qst_train_peasants_against_bandits | 38 |
| qst_eliminate_bandits_infesting_village | 39 |
| qst_visit_lady | 40 |
| qst_formal_marriage_proposal | 41 |
| qst_obtain_liege_blessing | 42 |
| qst_wed_betrothed | 43 |
| qst_wed_betrothed_female | 44 |
| qst_join_faction | 45 |
| qst_rebel_against_kingdom | 46 |
| qst_consult_with_minister | 47 |
| qst_organize_feast | 48 |
| qst_resolve_dispute | 49 |
| ... | (ещё 132 констант) |

### ID_scene_props.py

| Константа | Значение |
|-----------|----------|
| spr_invalid_object | 0 |
| spr_inventory | 1 |
| spr_empty | 2 |
| spr_chest_a | 3 |
| spr_container_small_chest | 4 |
| spr_container_chest_b | 5 |
| spr_container_chest_c | 6 |
| spr_player_chest | 7 |
| spr_locked_player_chest | 8 |
| spr_light_sun | 9 |
| spr_light | 10 |
| spr_light_red | 11 |
| spr_light_night | 12 |
| spr_torch | 13 |
| spr_torch_night | 14 |
| spr_barrier_20m | 15 |
| spr_barrier_16m | 16 |
| spr_barrier_8m | 17 |
| spr_barrier_4m | 18 |
| spr_barrier_2m | 19 |
| spr_exit_4m | 20 |
| spr_exit_8m | 21 |
| spr_exit_16m | 22 |
| spr_ai_limiter_2m | 23 |
| spr_ai_limiter_4m | 24 |
| spr_ai_limiter_8m | 25 |
| spr_ai_limiter_16m | 26 |
| spr_Shield | 27 |
| spr_shelves | 28 |
| spr_table_tavern | 29 |
| spr_table_castle_a | 30 |
| spr_chair_castle_a | 31 |
| spr_pillow_a | 32 |
| spr_pillow_b | 33 |
| spr_pillow_c | 34 |
| spr_interior_castle_g_square_keep_b | 35 |
| spr_carpet_with_pillows_a | 36 |
| spr_carpet_with_pillows_b | 37 |
| spr_table_round_a | 38 |
| spr_table_round_b | 39 |
| spr_fireplace_b | 40 |
| spr_fireplace_c | 41 |
| spr_sofa_a | 42 |
| spr_sofa_b | 43 |
| spr_ewer_a | 44 |
| spr_end_table_a | 45 |
| spr_fake_houses_steppe_a | 46 |
| spr_fake_houses_steppe_b | 47 |
| spr_fake_houses_steppe_c | 48 |
| spr_boat_destroy | 49 |
| ... | (ещё 996 констант) |

### ID_scenes.py

| Константа | Значение |
|-----------|----------|
| scn_random_scene | 0 |
| scn_conversation_scene | 1 |
| scn_water | 2 |
| scn_random_scene_steppe | 3 |
| scn_random_scene_plain | 4 |
| scn_random_scene_snow | 5 |
| scn_random_scene_desert | 6 |
| scn_random_scene_steppe_forest | 7 |
| scn_random_scene_plain_forest | 8 |
| scn_random_scene_snow_forest | 9 |
| scn_random_scene_desert_forest | 10 |
| scn_camp_scene | 11 |
| scn_camp_scene_horse_track | 12 |
| scn_four_ways_inn | 13 |
| scn_test_scene | 14 |
| scn_quick_battle_1 | 15 |
| scn_quick_battle_2 | 16 |
| scn_quick_battle_3 | 17 |
| scn_quick_battle_4 | 18 |
| scn_quick_battle_5 | 19 |
| scn_quick_battle_6 | 20 |
| scn_quick_battle_7 | 21 |
| scn_salt_mine | 22 |
| scn_novice_ground | 23 |
| scn_zendar_arena | 24 |
| scn_dhorak_keep | 25 |
| scn_reserved4 | 26 |
| scn_reserved5 | 27 |
| scn_reserved6 | 28 |
| scn_reserved7 | 29 |
| scn_reserved8 | 30 |
| scn_reserved9 | 31 |
| scn_reserved10 | 32 |
| scn_reserved11 | 33 |
| scn_reserved12 | 34 |
| scn_training_ground | 35 |
| scn_tutorial_1 | 36 |
| scn_tutorial_2 | 37 |
| scn_tutorial_3 | 38 |
| scn_tutorial_4 | 39 |
| scn_tutorial_5 | 40 |
| scn_training_ground_horse_track_1 | 41 |
| scn_training_ground_horse_track_2 | 42 |
| scn_training_ground_horse_track_3 | 43 |
| scn_training_ground_horse_track_4 | 44 |
| scn_training_ground_horse_track_5 | 45 |
| scn_training_ground_ranged_melee_1 | 46 |
| scn_training_ground_ranged_melee_2 | 47 |
| scn_training_ground_ranged_melee_3 | 48 |
| scn_training_ground_ranged_melee_4 | 49 |
| ... | (ещё 504 констант) |

### ID_scripts.py

| Константа | Значение |
|-----------|----------|
| script_game_start | 0 |
| script_game_get_use_string | 1 |
| script_game_quick_start | 2 |
| script_get_army_size_from_slider_value | 3 |
| script_spawn_quick_battle_army | 4 |
| script_player_arrived | 5 |
| script_game_set_multiplayer_mission_end | 6 |
| script_game_enable_cheat_menu | 7 |
| script_game_get_console_command | 8 |
| script_game_event_party_encounter | 9 |
| script_game_event_simulate_battle | 10 |
| script_game_event_battle_end | 11 |
| script_order_best_besieger_party_to_guard_center | 12 |
| script_game_get_item_buy_price_factor | 13 |
| script_game_get_item_sell_price_factor | 14 |
| script_get_trade_penalty | 15 |
| script_game_event_buy_item | 16 |
| script_game_event_sell_item | 17 |
| script_start_wedding_cutscene | 18 |
| script_game_get_troop_wage | 19 |
| script_game_get_total_wage | 20 |
| script_game_get_join_cost | 21 |
| script_game_get_upgrade_xp | 22 |
| script_game_get_upgrade_cost | 23 |
| script_game_get_prisoner_price | 24 |
| script_game_check_prisoner_can_be_sold | 25 |
| script_game_get_morale_of_troops_from_faction | 26 |
| script_game_event_detect_party | 27 |
| script_game_event_undetect_party | 28 |
| script_game_get_statistics_line | 29 |
| script_game_get_date_text | 30 |
| script_game_get_money_text | 31 |
| script_game_get_party_companion_limit | 32 |
| script_game_reset_player_party_name | 33 |
| script_game_get_troop_note | 34 |
| script_game_get_center_note | 35 |
| script_game_get_faction_note | 36 |
| script_game_get_quest_note | 37 |
| script_game_get_info_page_note | 38 |
| script_game_get_scene_name | 39 |
| script_game_get_mission_template_name | 40 |
| script_add_kill_death_counts | 41 |
| script_warn_player_about_auto_team_balance | 42 |
| script_check_team_balance | 43 |
| script_check_creating_ladder_dust_effect | 44 |
| script_money_management_after_agent_death | 45 |
| script_initialize_aristocracy | 46 |
| script_initialize_trade_routes | 47 |
| script_initialize_faction_troop_types | 48 |
| script_initialize_item_info | 49 |
| ... | (ещё 560 констант) |

### ID_skills.py

| Константа | Значение |
|-----------|----------|
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

### ID_sounds.py

| Константа | Значение |
|-----------|----------|
| snd_click | 0 |
| snd_tutorial_1 | 1 |
| snd_tutorial_2 | 2 |
| snd_gong | 3 |
| snd_quest_taken | 4 |
| snd_quest_completed | 5 |
| snd_quest_succeeded | 6 |
| snd_quest_concluded | 7 |
| snd_quest_failed | 8 |
| snd_quest_cancelled | 9 |
| snd_rain | 10 |
| snd_money_received | 11 |
| snd_money_paid | 12 |
| snd_sword_clash_1 | 13 |
| snd_sword_clash_2 | 14 |
| snd_sword_clash_3 | 15 |
| snd_sword_swing | 16 |
| snd_footstep_grass | 17 |
| snd_footstep_wood | 18 |
| snd_footstep_water | 19 |
| snd_footstep_horse | 20 |
| snd_footstep_horse_1b | 21 |
| snd_footstep_horse_1f | 22 |
| snd_footstep_horse_2b | 23 |
| snd_footstep_horse_2f | 24 |
| snd_footstep_horse_3b | 25 |
| snd_footstep_horse_3f | 26 |
| snd_footstep_horse_4b | 27 |
| snd_footstep_horse_4f | 28 |
| snd_footstep_horse_5b | 29 |
| snd_footstep_horse_5f | 30 |
| snd_jump_begin | 31 |
| snd_jump_end | 32 |
| snd_jump_begin_water | 33 |
| snd_jump_end_water | 34 |
| snd_horse_jump_begin | 35 |
| snd_horse_jump_end | 36 |
| snd_horse_jump_begin_water | 37 |
| snd_horse_jump_end_water | 38 |
| snd_release_bow | 39 |
| snd_release_crossbow | 40 |
| snd_throw_javelin | 41 |
| snd_throw_axe | 42 |
| snd_throw_knife | 43 |
| snd_throw_stone | 44 |
| snd_reload_crossbow | 45 |
| snd_reload_crossbow_continue | 46 |
| snd_pull_bow | 47 |
| snd_pull_arrow | 48 |
| snd_arrow_pass_by | 49 |
| ... | (ещё 150 констант) |

### ID_strings.py

| Константа | Значение |
|-----------|----------|
| str_no_string | 0 |
| str_empty_string | 1 |
| str_yes | 2 |
| str_no | 3 |
| str_blank_string | 4 |
| str_error_string | 5 |
| str_noone | 6 |
| str_s0 | 7 |
| str_blank_s1 | 8 |
| str_reg1 | 9 |
| str_s50_comma_s51 | 10 |
| str_s50_and_s51 | 11 |
| str_s52_comma_s51 | 12 |
| str_s52_and_s51 | 13 |
| str_s5_s_party | 14 |
| str_given_by_s1_at_s2 | 15 |
| str_given_by_s1_in_wilderness | 16 |
| str_s7_raiders | 17 |
| str_bandits_eliminated_by_another | 18 |
| str_msg_battle_won | 19 |
| str_tutorial_map1 | 20 |
| str_change_color_1 | 21 |
| str_change_color_2 | 22 |
| str_change_background | 23 |
| str_change_flag_type | 24 |
| str_change_map_flag_type | 25 |
| str_randomize | 26 |
| str_sample_banner | 27 |
| str_sample_map_banner | 28 |
| str_number_of_charges | 29 |
| str_change_charge_1 | 30 |
| str_change_charge_1_color | 31 |
| str_change_charge_2 | 32 |
| str_change_charge_2_color | 33 |
| str_change_charge_3 | 34 |
| str_change_charge_3_color | 35 |
| str_change_charge_4 | 36 |
| str_change_charge_4_color | 37 |
| str_change_charge_position | 38 |
| str_choose_position | 39 |
| str_choose_charge | 40 |
| str_choose_background | 41 |
| str_choose_flag_type | 42 |
| str_choose_map_flag_type | 43 |
| str_choose_color | 44 |
| str_accept | 45 |
| str_charge_no_1 | 46 |
| str_charge_no_2 | 47 |
| str_charge_no_3 | 48 |
| str_charge_no_4 | 49 |
| ... | (ещё 3368 констант) |

### ID_tableau_materials.py

| Константа | Значение |
|-----------|----------|
| tableau_game_character_sheet | 0 |
| tableau_game_inventory_window | 1 |
| tableau_game_profile_window | 2 |
| tableau_game_party_window | 3 |
| tableau_game_troop_label_banner | 4 |
| tableau_round_shield_1 | 5 |
| tableau_round_shield_2 | 6 |
| tableau_round_shield_3 | 7 |
| tableau_round_shield_4 | 8 |
| tableau_round_shield_5 | 9 |
| tableau_small_round_shield_1 | 10 |
| tableau_small_round_shield_2 | 11 |
| tableau_small_round_shield_3 | 12 |
| tableau_kite_shield_1 | 13 |
| tableau_kite_shield_2 | 14 |
| tableau_kite_shield_3 | 15 |
| tableau_kite_shield_4 | 16 |
| tableau_heater_shield_1 | 17 |
| tableau_heater_shield_2 | 18 |
| tableau_pavise_shield_1 | 19 |
| tableau_pavise_shield_2 | 20 |
| tableau_heraldic_armor_a | 21 |
| tableau_heraldic_armor_b | 22 |
| tableau_heraldic_armor_c | 23 |
| tableau_heraldic_armor_d | 24 |
| tableau_troop_note_alpha_mask | 25 |
| tableau_troop_note_color | 26 |
| tableau_troop_character_alpha_mask | 27 |
| tableau_troop_character_color | 28 |
| tableau_troop_inventory_alpha_mask | 29 |
| tableau_troop_inventory_color | 30 |
| tableau_troop_profile_alpha_mask | 31 |
| tableau_troop_profile_color | 32 |
| tableau_troop_party_alpha_mask | 33 |
| tableau_troop_party_color | 34 |
| tableau_troop_note_mesh | 35 |
| tableau_center_note_mesh | 36 |
| tableau_faction_note_mesh_for_menu | 37 |
| tableau_faction_note_mesh | 38 |
| tableau_faction_note_mesh_banner | 39 |
| tableau_2_factions_mesh | 40 |
| tableau_color_picker | 41 |
| tableau_custom_banner_square_no_mesh | 42 |
| tableau_custom_banner_default | 43 |
| tableau_custom_banner_tall | 44 |
| tableau_custom_banner_square | 45 |
| tableau_custom_banner_short | 46 |
| tableau_background_selection | 47 |
| tableau_positioning_selection | 48 |
| tableau_retired_troop_alpha_mask | 49 |
| ... | (ещё 5 констант) |

### ID_troops.py

| Константа | Значение |
|-----------|----------|
| trp_player | 0 |
| trp_multiplayer_profile_troop_male | 1 |
| trp_multiplayer_profile_troop_female | 2 |
| trp_temp_troop | 3 |
| trp_find_item_cheat | 4 |
| trp_random_town_sequence | 5 |
| trp_tournament_participants | 6 |
| trp_tutorial_maceman | 7 |
| trp_tutorial_archer | 8 |
| trp_tutorial_swordsman | 9 |
| trp_novice_fighter | 10 |
| trp_regular_fighter | 11 |
| trp_veteran_fighter | 12 |
| trp_champion_fighter | 13 |
| trp_arena_training_fighter_1 | 14 |
| trp_arena_training_fighter_2 | 15 |
| trp_arena_training_fighter_3 | 16 |
| trp_arena_training_fighter_4 | 17 |
| trp_arena_training_fighter_5 | 18 |
| trp_arena_training_fighter_6 | 19 |
| trp_arena_training_fighter_7 | 20 |
| trp_arena_training_fighter_8 | 21 |
| trp_arena_training_fighter_9 | 22 |
| trp_arena_training_fighter_10 | 23 |
| trp_cattle | 24 |
| trp_farmer | 25 |
| trp_townsman | 26 |
| trp_watchman | 27 |
| trp_caravan_guard | 28 |
| trp_mercenary_swordsman | 29 |
| trp_hired_blade | 30 |
| trp_mercenary_crossbowman | 31 |
| trp_mercenary_horseman | 32 |
| trp_mercenary_cavalry | 33 |
| trp_mercenaries_end | 34 |
| trp_swadian_recruit | 35 |
| trp_swadian_militia | 36 |
| trp_swadian_footman | 37 |
| trp_swadian_infantry | 38 |
| trp_swadian_sergeant | 39 |
| trp_swadian_skirmisher | 40 |
| trp_swadian_crossbowman | 41 |
| trp_swadian_sharpshooter | 42 |
| trp_swadian_man_at_arms | 43 |
| trp_swadian_knight | 44 |
| trp_swadian_messenger | 45 |
| trp_swadian_deserter | 46 |
| trp_swadian_prison_guard | 47 |
| trp_swadian_castle_guard | 48 |
| trp_vaegir_recruit | 49 |
| ... | (ещё 1022 констант) |

### header_animations.py

| Константа | Значение |
|-----------|----------|
| arf_blend_in_0 | 1 |
| arf_blend_in_1 | 2 |
| arf_blend_in_2 | 3 |
| arf_blend_in_3 | 4 |
| arf_blend_in_4 | 5 |
| arf_blend_in_5 | 6 |
| arf_blend_in_6 | 7 |
| arf_blend_in_7 | 8 |
| arf_blend_in_8 | 9 |
| arf_blend_in_9 | 10 |
| arf_blend_in_10 | 11 |
| arf_blend_in_11 | 12 |
| arf_blend_in_12 | 13 |
| arf_blend_in_13 | 14 |
| arf_blend_in_14 | 15 |
| arf_blend_in_15 | 16 |
| arf_blend_in_16 | 17 |
| arf_blend_in_17 | 18 |
| arf_blend_in_18 | 19 |
| arf_blend_in_19 | 20 |
| arf_blend_in_20 | 21 |
| arf_blend_in_21 | 22 |
| arf_blend_in_22 | 23 |
| arf_blend_in_23 | 24 |
| arf_blend_in_24 | 25 |
| arf_blend_in_25 | 26 |
| arf_blend_in_26 | 27 |
| arf_blend_in_27 | 28 |
| arf_blend_in_28 | 29 |
| arf_blend_in_29 | 30 |
| arf_blend_in_30 | 31 |
| arf_blend_in_31 | 32 |
| arf_blend_in_32 | 33 |
| arf_blend_in_48 | 49 |
| arf_blend_in_64 | 65 |
| arf_blend_in_128 | 129 |
| arf_blend_in_254 | 255 |
| arf_make_walk_sound | 256 |
| arf_make_custom_sound | 512 |
| arf_two_handed_blade | 16777216 |
| arf_lancer | 33554432 |
| arf_stick_item_to_left_hand | 67108864 |
| arf_cyclic | 268435456 |
| arf_use_walk_progress | 536870912 |
| arf_use_stand_progress | 1073741824 |
| arf_use_inv_walk_progress | 2147483648 |
| amf_priority_mask | 4095 |
| amf_rider_rot_bow | 4096 |
| amf_rider_rot_throw | 8192 |
| amf_rider_rot_crossbow | 12288 |
| ... | (ещё 39 констант) |

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
| ... | (ещё 486 констант) |

### header_dialogs.py

| Константа | Значение |
|-----------|----------|
| speaker_pos | 0 |
| ipt_token_pos | 1 |
| sentence_conditions_pos | 2 |
| text_pos | 3 |
| opt_token_pos | 4 |
| sentence_consequences_pos | 5 |
| anyone | 4095 |
| repeat_for_factions | 4096 |
| repeat_for_parties | 8192 |
| repeat_for_troops | 12288 |
| repeat_for_100 | 16384 |
| repeat_for_1000 | 20480 |
| plyr | 65536 |
| party_tpl | 131072 |
| auto_proceed | 262144 |
| multi_line | 524288 |
| suf_other_bits | 20 |

### header_factions.py

| Константа | Значение |
|-----------|----------|
| ff_always_hide_label | 1 |
| ff_max_rating_bits | 8 |
| ff_max_rating_mask | 65280 |

### header_game_menus.py

| Константа | Значение |
|-----------|----------|
| mnf_join_battle | 1 |
| mnf_auto_enter | 16 |
| mnf_enable_hot_keys | 256 |
| mnf_disable_all_keys | 512 |
| mnf_scale_picture | 4096 |

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
| ... | (ещё 36 констант) |

### header_items.py

| Константа | Значение |
|-----------|----------|
| itp_type_horse | 1 |
| itp_type_one_handed_wpn | 2 |
| itp_type_two_handed_wpn | 3 |
| itp_type_polearm | 4 |
| itp_type_arrows | 5 |
| itp_type_bolts | 6 |
| itp_type_shield | 7 |
| itp_type_bow | 8 |
| itp_type_crossbow | 9 |
| itp_type_thrown | 10 |
| itp_type_goods | 11 |
| itp_type_head_armor | 12 |
| itp_type_body_armor | 13 |
| itp_type_foot_armor | 14 |
| itp_type_hand_armor | 15 |
| itp_type_pistol | 16 |
| itp_type_musket | 17 |
| itp_type_bullets | 18 |
| itp_type_animal | 19 |
| itp_type_book | 20 |
| itp_force_attach_left_hand | 256 |
| itp_force_attach_right_hand | 512 |
| itp_force_attach_left_forearm | 768 |
| itp_attach_armature | 3840 |
| itp_attachment_mask | 3840 |
| itp_unique | 4096 |
| itp_always_loot | 8192 |
| itp_no_parry | 16384 |
| itp_default_ammo | 32768 |
| itp_merchandise | 65536 |
| itp_wooden_attack | 131072 |
| itp_wooden_parry | 262144 |
| itp_food | 524288 |
| itp_cant_reload_on_horseback | 1048576 |
| itp_two_handed | 2097152 |
| itp_primary | 4194304 |
| itp_secondary | 8388608 |
| itp_covers_legs | 16777216 |
| itp_doesnt_cover_hair | 16777216 |
| itp_can_penetrate_shield | 16777216 |
| itp_consumable | 33554432 |
| itp_bonus_against_shield | 67108864 |
| itp_penalty_with_shield | 134217728 |
| itp_cant_use_on_horseback | 268435456 |
| itp_civilian | 536870912 |
| itp_next_item_as_melee | 536870912 |
| itp_fit_to_head | 1073741824 |
| itp_offset_lance | 1073741824 |
| itp_covers_head | 2147483648 |
| itp_couchable | 2147483648 |
| ... | (ещё 158 констант) |

### header_map_icons.py

| Константа | Значение |
|-----------|----------|
| mcn_no_shadow | 1 |

### header_meshes.py

| Константа | Значение |
|-----------|----------|
| render_order_plus_1 | 1 |

### header_mission_templates.py

| Константа | Значение |
|-----------|----------|
| aif_group_bits | 0 |
| aif_group_mask | 15 |
| aif_start_alarmed | 16 |
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
| ... | (ещё 61 констант) |

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
| mtf_culture_1 | 1 |
| mtf_culture_2 | 2 |
| mtf_culture_3 | 4 |
| mtf_culture_4 | 8 |
| mtf_culture_5 | 16 |
| mtf_culture_6 | 32 |
| mtf_culture_all | 63 |
| mtf_looping | 64 |
| mtf_start_immediately | 128 |
| mtf_persist_until_finished | 256 |
| mtf_sit_tavern | 512 |
| mtf_sit_fight | 1024 |
| mtf_sit_multiplayer_fight | 2048 |
| mtf_sit_ambushed | 4096 |
| mtf_sit_town | 8192 |
| mtf_sit_town_infiltrate | 16384 |
| mtf_sit_killed | 32768 |
| mtf_sit_travel | 65536 |
| mtf_sit_arena | 131072 |
| mtf_sit_siege | 262144 |
| mtf_sit_night | 524288 |
| mtf_sit_day | 1048576 |
| mtf_sit_encounter_hostile | 2097152 |
| mtf_sit_main_title | 4194304 |
| mtf_sit_victorious | 8388608 |
| mtf_sit_feast | 16777216 |
| mtf_module_track | 268435456 |

### header_operations.py

| Константа | Значение |
|-----------|----------|
| call_script | 1 |
| end_try | 3 |
| try_end | 3 |
| try_begin | 4 |
| else_try_begin | 5 |
| else_try | 5 |
| try_for_range | 6 |
| try_for_range_backwards | 7 |
| try_for_parties | 11 |
| try_for_agents | 12 |
| try_for_prop_instances | 16 |
| try_for_players | 17 |
| store_script_param_1 | 21 |
| store_script_param_2 | 22 |
| store_script_param | 23 |
| ge | 30 |
| eq | 31 |
| gt | 32 |
| is_between | 33 |
| entering_town | 36 |
| map_free | 37 |
| encountered_party_is_attacker | 39 |
| conversation_screen_is_active | 42 |
| in_meta_mission | 44 |
| set_player_troop | 47 |
| store_repeat_object | 50 |
| get_operation_set_version | 55 |
| set_physics_delta_time | 58 |
| set_result_string | 60 |
| is_camera_in_first_person | 61 |
| set_camera_in_first_person | 62 |
| game_key_get_mapped_key_name | 65 |
| key_is_down | 70 |
| key_clicked | 71 |
| game_key_is_down | 72 |
| game_key_clicked | 73 |
| mouse_get_position | 75 |
| omit_key_once | 77 |
| clear_omitted_keys | 78 |
| get_global_cloud_amount | 90 |
| set_global_cloud_amount | 91 |
| get_global_haze_amount | 92 |
| set_global_haze_amount | 93 |
| hero_can_join | 101 |
| hero_can_join_as_prisoner | 102 |
| party_can_join | 103 |
| party_can_join_as_prisoner | 104 |
| troops_can_join | 105 |
| troops_can_join_as_prisoner | 106 |
| party_can_join_party | 107 |
| ... | (ещё 1016 констант) |

### header_particle_systems.py

| Константа | Значение |
|-----------|----------|
| psf_always_emit | 2 |
| psf_global_emit_dir | 16 |
| psf_emit_at_water_level | 32 |
| psf_billboard_2d | 256 |
| psf_billboard_3d | 512 |
| psf_billboard_drop | 768 |
| psf_turn_to_velocity | 1024 |
| psf_randomize_rotation | 4096 |
| psf_randomize_size | 8192 |
| psf_2d_turbulance | 65536 |
| psf_next_effect_is_lod | 131072 |

### header_parties.py

| Константа | Значение |
|-----------|----------|
| pf_icon_mask | 255 |
| pf_disabled | 256 |
| pf_is_ship | 512 |
| pf_is_static | 1024 |
| pf_label_small | 0 |
| pf_label_medium | 4096 |
| pf_label_large | 8192 |
| pf_always_visible | 16384 |
| pf_default_behavior | 65536 |
| pf_auto_remove_in_town | 131072 |
| pf_quest_party | 262144 |
| pf_no_label | 524288 |
| pf_limit_members | 1048576 |
| pf_hide_defenders | 2097152 |
| pf_show_faction | 4194304 |
| pf_dont_attack_civilians | 33554432 |
| pf_civilian | 67108864 |
| pf_carry_goods_bits | 48 |
| pf_carry_gold_bits | 56 |
| pf_carry_gold_multiplier | 20 |
| pf_carry_goods_mask | 71776119061217280 |
| pf_carry_gold_mask | 18374686479671623680 |
| pmf_is_prisoner | 1 |
| no_faction | -1 |
| ai_bhvr_hold | 0 |
| ai_bhvr_travel_to_party | 1 |
| ai_bhvr_patrol_location | 2 |
| ai_bhvr_patrol_party | 3 |
| ai_bhvr_track_party | 4 |
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
| courage_4 | 4 |
| courage_5 | 5 |
| courage_6 | 6 |
| courage_7 | 7 |
| courage_8 | 8 |
| courage_9 | 9 |
| courage_10 | 10 |
| courage_11 | 11 |
| courage_12 | 12 |
| courage_13 | 13 |
| courage_14 | 14 |
| ... | (ещё 22 констант) |

### header_postfx.py

| Константа | Значение |
|-----------|----------|
| fxf_highhdr | 1 |

### header_presentations.py

| Константа | Значение |
|-----------|----------|
| tf_left_align | 4 |
| tf_right_align | 8 |
| tf_center_justify | 16 |
| tf_double_space | 2048 |
| tf_vertical_align_center | 4096 |
| tf_scrollable | 8192 |
| tf_single_line | 32768 |
| tf_with_outline | 65536 |
| tf_scrollable_style_2 | 131072 |
| prsntf_read_only | 1 |
| prsntf_manual_end_only | 2 |

### header_quests.py

| Константа | Значение |
|-----------|----------|
| qf_show_progression | 1 |
| qf_random_quest | 2 |

### header_scene_props.py

| Константа | Значение |
|-----------|----------|
| sokf_type_container | 5 |
| sokf_type_ai_limiter | 8 |
| sokf_type_barrier | 9 |
| sokf_type_barrier_leave | 10 |
| sokf_type_ladder | 11 |
| sokf_type_barrier3d | 12 |
| sokf_type_player_limiter | 13 |
| sokf_type_ai_limiter3d | 14 |
| sokf_type_mask | 255 |
| sokf_add_fire | 256 |
| sokf_add_smoke | 512 |
| sokf_add_light | 1024 |
| sokf_show_hit_point_bar | 2048 |
| sokf_place_at_origin | 4096 |
| sokf_dynamic | 8192 |
| sokf_invisible | 16384 |
| sokf_destructible | 32768 |
| sokf_moveable | 65536 |
| sokf_face_player | 131072 |
| sokf_dynamic_physics | 262144 |
| sokf_missiles_not_attached | 524288 |
| sokf_enforce_shadows | 1048576 |
| sokf_dont_move_agent_over | 2097152 |
| sokf_handle_as_flora | 16777216 |
| sokf_static_movement | 33554432 |
| spbf_hit_points_mask | 255 |
| spbf_hit_points_bits | 20 |
| spbf_init_use_time_mask | 255 |
| spbf_use_time_bits | 28 |
| spanim_linear | 0 |
| spanim_loop_linear | 4 |

### header_scenes.py

| Константа | Значение |
|-----------|----------|
| scene_name_pos | 0 |
| passages_pos | 8 |
| sf_indoors | 1 |
| sf_force_skybox | 2 |
| sf_generate | 256 |
| sf_randomize | 512 |
| sf_auto_entry_points | 1024 |
| sf_no_horses | 2048 |
| sf_muddy_water | 4096 |

### header_skills.py

| Константа | Значение |
|-----------|----------|
| sf_base_att_str | 0 |
| sf_base_att_agi | 1 |
| sf_base_att_int | 2 |
| sf_base_att_cha | 3 |
| sf_effects_party | 16 |
| sf_inactive | 256 |
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
| ... | (ещё 419 констант) |

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
| skf_use_morph_key_10 | 1 |
| skf_use_morph_key_20 | 2 |
| skf_use_morph_key_30 | 3 |
| skf_use_morph_key_40 | 4 |
| skf_use_morph_key_50 | 5 |
| skf_use_morph_key_60 | 6 |
| skf_use_morph_key_70 | 7 |

### header_sounds.py

| Константа | Значение |
|-----------|----------|
| sf_2d | 1 |
| sf_looping | 2 |
| sf_start_at_random_pos | 4 |
| sf_stream_from_hd | 8 |
| sf_always_send_via_network | 1048576 |
| sf_priority_15 | 240 |
| sf_priority_14 | 224 |
| sf_priority_13 | 208 |
| sf_priority_12 | 192 |
| sf_priority_11 | 176 |
| sf_priority_10 | 160 |
| sf_priority_9 | 144 |
| sf_priority_8 | 128 |
| sf_priority_7 | 112 |
| sf_priority_6 | 96 |
| sf_priority_5 | 80 |
| sf_priority_4 | 64 |
| sf_priority_3 | 48 |
| sf_priority_2 | 32 |
| sf_priority_1 | 16 |
| sf_vol_15 | 3840 |
| sf_vol_14 | 3584 |
| sf_vol_13 | 3328 |
| sf_vol_12 | 3072 |
| sf_vol_11 | 2816 |
| sf_vol_10 | 2560 |
| sf_vol_9 | 2304 |
| sf_vol_8 | 2048 |
| sf_vol_7 | 1792 |
| sf_vol_6 | 1536 |
| sf_vol_5 | 1280 |
| sf_vol_4 | 1024 |
| sf_vol_3 | 768 |
| sf_vol_2 | 512 |
| sf_vol_1 | 256 |

### header_strings.py

*Нет констант*

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
| ti_simulate_battle | -5.0 |
| ti_on_party_encounter | -6.0 |
| ti_question_answered | -8 |
| ti_server_player_joined | -15.0 |
| ti_on_multiplayer_mission_end | -16.0 |
| ti_before_mission_start | -19.0 |
| ti_after_mission_start | -20.0 |
| ti_tab_pressed | -21.0 |
| ti_inventory_key_pressed | -22.0 |
| ti_escape_pressed | -23.0 |
| ti_battle_window_opened | -24.0 |
| ti_on_agent_spawn | -25.0 |
| ti_on_agent_killed_or_wounded | -26.0 |
| ti_on_agent_knocked_down | -27.0 |
| ti_on_agent_hit | -28.0 |
| ti_on_player_exit | -29.0 |
| ti_on_leave_area | -30.0 |
| ti_on_scene_prop_init | -40.0 |
| ti_on_init_scene_prop | ti_on_scene_prop_init |
| ti_on_scene_prop_hit | -42.0 |
| ti_on_scene_prop_destroy | -43.0 |
| ti_on_scene_prop_use | -44.0 |
| ti_on_scene_prop_is_animating | -45.0 |
| ti_on_scene_prop_animation_finished | -46.0 |
| ti_on_scene_prop_start_use | -47.0 |
| ti_on_scene_prop_cancel_use | -48.0 |
| ti_on_init_item | -50.0 |
| ti_on_weapon_attack | -51.0 |
| ti_on_missile_hit | -52.0 |
| ti_on_item_picked_up | -53.0 |
| ti_on_item_dropped | -54.0 |
| ti_on_agent_mount | -55.0 |
| ti_on_agent_dismount | -56.0 |
| ti_on_item_wielded | -57.0 |
| ti_on_item_unwielded | -58.0 |
| ti_on_presentation_load | -60.0 |
| ti_on_presentation_run | -61.0 |
| ti_on_presentation_event_state_change | -62.0 |
| ti_on_presentation_mouse_enter_leave | -63.0 |
| ti_on_presentation_mouse_press | -64.0 |
| ti_on_init_map_icon | -70.0 |
| ti_on_order_issued | -71.0 |
| ti_on_switch_to_map | -75.0 |
| ti_scene_prop_deformation_finished | -76.0 |
| ti_on_shield_hit | -80.0 |
| ti_once | 100000000.0 |
| key_1 | 2 |
| key_2 | 3 |
| key_3 | 4 |
| key_4 | 5 |
| ... | (ещё 180 констант) |

### header_troops.py

*Нет констант*


## 2. СТРУКТУРА ДАННЫХ (TUPLES)

### module_animations.py

- **Имя массива:** `animations`
- **Количество элементов в кортеже:** 7
- **Структура первого элемента:**
  ```
  [0] const:stand
  [1] const:0
  [2] var:amf_client_prediction
  [3] nested[8]
  [4] nested[8]
  [5] nested[8]
  [6] nested[8]
  ```

### module_constants.py

*Не удалось определить структуру*

### module_dialogs.py

- **Имя массива:** `dialogs`
- **Количество элементов в кортеже:** 6
- **Структура первого элемента:**
  ```
  [0] var:anyone
  [1] const:start
  [2] nested[106]
  [3] const:{!}Warning: This line is never displayed. It is ju
  [4] const:close_window
  [5] nested[0]
  ```

### module_factions.py

- **Имя массива:** `default_kingdom_relations`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] const:outlaws
  [1] UnaryOp
  ```

### module_game_menus.py

- **Имя массива:** `game_menus`
- **Количество элементов в кортеже:** 6
- **Структура первого элемента:**
  ```
  [0] const:start_game_0
  [1] expr:BitOr
  [2] const:Welcome, adventurer, to Mount and Blade: Warband. 
  [3] const:none
  [4] nested[0]
  [5] nested[2]
  ```

### module_info.py

*Не удалось определить структуру*

### module_info_pages.py

- **Имя массива:** `info_pages`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] const:morale
  [1] const:Morale
  [2] const:Morale represents the ability and willingness of t
  ```

### module_items.py

- **Имя массива:** `items`
- **Количество элементов в кортеже:** 8
- **Структура первого элемента:**
  ```
  [0] const:no_item
  [1] const:INVALID ITEM
  [2] nested[1]
  [3] expr:BitOr
  [4] var:itc_longsword
  [5] const:3
  [6] expr:BitOr
  [7] var:imodbits_none
  ```

### module_map_icons.py

- **Имя массива:** `map_icons`
- **Количество элементов в кортеже:** 8
- **Структура первого элемента:**
  ```
  [0] const:player
  [1] const:0
  [2] const:player
  [3] var:avatar_scale
  [4] var:snd_footstep_grass
  [5] const:0.15
  [6] const:0.173
  [7] const:0
  ```

### module_meshes.py

- **Имя массива:** `meshes`
- **Количество элементов в кортеже:** 12
- **Структура первого элемента:**
  ```
  [0] const:pic_bandits
  [1] const:0
  [2] const:pic_bandits
  [3] const:0
  [4] const:0
  [5] const:0
  [6] const:0
  [7] const:0
  [8] const:0
  [9] const:1
  ... (2 more elements)
  ```

### module_mission_templates.py

*Не удалось определить структуру*

### module_music.py

- **Имя массива:** `tracks`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] const:bogus
  [1] const:cant_find_this.ogg
  [2] const:0
  [3] const:0
  ```

### module_particle_systems.py

- **Имя массива:** `particle_systems`
- **Количество элементов в кортеже:** 24
- **Структура первого элемента:**
  ```
  [0] const:game_rain
  [1] expr:BitOr
  [2] const:prtcl_rain
  [3] const:500
  [4] const:0.5
  [5] const:0.33
  [6] const:1.0
  [7] const:10.0
  [8] const:0.0
  [9] nested[2]
  ... (14 more elements)
  ```

### module_parties.py

- **Имя массива:** `parties`
- **Количество элементов в кортеже:** 11
- **Структура первого элемента:**
  ```
  [0] const:main_party
  [1] const:Main Party
  [2] expr:BitOr
  [3] var:no_menu
  [4] var:pt_none
  [5] var:fac_player_faction
  [6] const:0
  [7] var:ai_bhvr_hold
  [8] const:0
  [9] nested[2]
  ... (1 more elements)
  ```

### module_party_templates.py

- **Имя массива:** `party_templates`
- **Количество элементов в кортеже:** 7
- **Структура первого элемента:**
  ```
  [0] const:none
  [1] const:none
  [2] var:icon_gray_knight
  [3] const:0
  [4] var:fac_commoners
  [5] var:merchant_personality
  [6] nested[0]
  ```

### module_postfx.py

- **Имя массива:** `postfx_params`
- **Количество элементов в кортеже:** 6
- **Структура первого элемента:**
  ```
  [0] const:default
  [1] const:0
  [2] const:0
  [3] nested[4]
  [4] nested[4]
  [5] nested[4]
  ```

### module_presentations.py

- **Имя массива:** `presentations`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] const:game_credits
  [1] var:prsntf_read_only
  [2] var:mesh_load_window
  [3] nested[2]
  ```

### module_quests.py

- **Имя массива:** `quests`
- **Количество элементов в кортеже:** 4
- **Структура первого элемента:**
  ```
  [0] const:deliver_message
  [1] const:Deliver Message to {s13}
  [2] var:qf_random_quest
  [3] const:{!}{s9} asked you to take a message to {s13}. {s13
  ```

### module_scene_props.py

- **Имя массива:** `scene_props`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] const:invalid_object
  [1] const:0
  [2] const:question_mark
  [3] const:0
  [4] nested[0]
  ```

### module_scenes.py

- **Имя массива:** `scenes`
- **Количество элементов в кортеже:** 10
- **Структура первого элемента:**
  ```
  [0] const:random_scene
  [1] expr:BitOr
  [2] const:none
  [3] const:none
  [4] nested[2]
  [5] nested[2]
  [6] UnaryOp
  [7] const:0x300028000003e8fa0000034e00004b34000059be
  [8] nested[0]
  [9] nested[0]
  ```

### module_scripts.py

- **Имя массива:** `scripts`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] const:game_start
  [1] nested[675]
  ```

### module_simple_triggers.py

- **Имя массива:** `simple_triggers`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] var:ti_on_party_encounter
  [1] nested[0]
  ```

### module_skills.py

- **Имя массива:** `skills`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] const:trade
  [1] const:Trade
  [2] expr:BitOr
  [3] const:10
  [4] const:Every level of this skill reduces your trade penal
  ```

### module_skins.py

- **Имя массива:** `man_face_keys`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] const:20
  [1] const:0
  [2] const:0.7
  [3] UnaryOp
  [4] const:Chin Size
  ```

### module_sounds.py

- **Имя массива:** `sounds`
- **Количество элементов в кортеже:** 3
- **Структура первого элемента:**
  ```
  [0] const:click
  [1] expr:BitOr
  [2] nested[1]
  ```

### module_strings.py

- **Имя массива:** `strings`
- **Количество элементов в кортеже:** 2
- **Структура первого элемента:**
  ```
  [0] const:no_string
  [1] const:NO STRING!
  ```

### module_tableau_materials.py

- **Имя массива:** `tableaus`
- **Количество элементов в кортеже:** 10
- **Структура первого элемента:**
  ```
  [0] const:game_character_sheet
  [1] const:0
  [2] const:tableau_with_transparency
  [3] const:1024
  [4] const:1024
  [5] const:0
  [6] const:0
  [7] const:266
  [8] const:532
  [9] nested[13]
  ```

### module_triggers.py

- **Имя массива:** `triggers`
- **Количество элементов в кортеже:** 5
- **Структура первого элемента:**
  ```
  [0] const:0.1
  [1] const:0
  [2] var:ti_once
  [3] nested[1]
  [4] nested[1]
  ```

### module_troops.py

- **Имя массива:** `troops`
- **Количество элементов в кортеже:** 12
- **Структура первого элемента:**
  ```
  [0] const:player
  [1] const:Player
  [2] const:Player
  [3] expr:BitOr
  [4] var:no_scene
  [5] var:reserved
  [6] var:fac_player_faction
  [7] nested[0]
  [8] expr:BitOr
  [9] call:wp(...)
  ... (2 more elements)
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
- `$auto_menu`
- `$battle_renown_value`
- `$belfry_num_men_pushing`
- `$belfry_num_slots_positioned`
- `$belfry_positioned`
- `$belfry_rotating_objects_begin`
- `$borcha_arrive_sargoth_as_prisoner`
- `$borcha_asked_for_freedom`
- `$borcha_freed`
- `$bug_fix_version`
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
- `$disable_local_histories`
- `$disable_npc_complaints`
- `$disable_sisterly_advice`
- `$do_not_cancel_quest`
- `$escort_merchant_caravan_mode`
- `$g_advantegous_faction`
- `$g_alarm_modula`
- `$g_ally_party`
- `$g_apply_budget_report_to_gold`
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
- `$g_camp_mode`
- `$g_castle_requested_by_player`
- `$g_castle_requested_for_troop`
- `$g_ccoop_currently_dropping_item`
- `$g_ccoop_disallow_horses`
- `$g_ccoop_king_troop`
- `$g_center_taken_by_player_faction`
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
- `$g_force_peace_faction_1`
- `$g_force_peace_faction_2`
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
- `$g_half_payment_checkpoint`
- `$g_horses_are_avaliable`
- `$g_include_diplo_explanation`
- `$g_infinite_camping`
- `$g_invite_faction`
- `$g_invite_faction_lord`
- `$g_invite_offered_center`
- `$g_is_quick_battle`
- `$g_last_comment_copied_to_s42`
- `$g_last_half_payment_check_day`
- `$g_last_mission_player_damage`
- `$g_last_report_control_day`
- `$g_last_rest_center`
- `$g_last_rest_payment_until`
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
- `$g_notification_menu_var1`
- `$g_notification_menu_var2`
- `$g_number_of_flags`
- `$g_number_of_targets_destroyed`
- `$g_one_faction_left_notification_shown`
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
- `$g_player_icon_state`
- `$g_player_is_captive`
- `$g_player_luck`
- `$g_player_minister`
- `$g_player_party_icon`
- `$g_player_party_morale_modifier_debt`
- `$g_player_party_morale_modifier_food`
- `$g_player_party_morale_modifier_leadership`
- `$g_player_party_morale_modifier_no_food`
- `$g_player_party_morale_modifier_party_size`
- `$g_player_raid_complete`
- `$g_player_raiding_village`
- `$g_player_reading_book`
- `$g_player_surrenders`
- `$g_player_tournament_placement`
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
- `$g_presentation_input`
- `$g_presentation_lines_to_display_begin`
- `$g_presentation_lines_to_display_end`
- `$g_presentation_marshall_selection_1_vote`
- `$g_presentation_marshall_selection_2_vote`
- `$g_presentation_marshall_selection_ended`
- `$g_presentation_marshall_selection_max_renown_1`
- `$g_presentation_marshall_selection_max_renown_1_troop`
- `$g_presentation_marshall_selection_max_renown_2`
- `$g_presentation_marshall_selection_max_renown_2_troop`
- `$g_presentation_marshall_selection_max_renown_3`
- `$g_presentation_marshall_selection_max_renown_3_troop`
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
- `$g_prisoner_recruit_last_time`
- `$g_prisoner_recruit_size`
- `$g_prisoner_recruit_troop_id`
- `$g_quick_battle_army_1_size`
- `$g_quick_battle_army_2_size`
- `$g_quick_battle_game_type`
- `$g_quick_battle_map`
- `$g_quick_battle_team_0_banner`
- `$g_quick_battle_team_1_banner`
- `$g_quick_battle_team_1_faction`
- `$g_quick_battle_team_2_faction`
- `$g_quick_battle_troop`
- `$g_random_army_quest`
- `$g_ransom_offer_party`
- `$g_ransom_offer_rejected`
- `$g_ransom_offer_troop`
- `$g_recalculate_ais`
- `$g_rejoinder_to_last_comment`
- `$g_reset_mission_participation`
- `$g_round_day_time`
- `$g_round_ended`
- `$g_round_finish_time`
- `$g_round_start_time`
- `$g_show_no_more_respawns_remained`
- `$g_siege_force_wait`
- `$g_siege_method`
- `$g_siege_method_finish_hours`
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
- `$g_time_to_spare`
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
- `$lady_flirtation_location`
- `$last_belfry_object_pos`
- `$last_defeated_hero`
- `$last_freed_hero`
- `$log_comment_relation_change`
- `$loot_screen_shown`
- `$marriage_candidate`
- `$marshall_defeated_in_battle`
- `$mercenary_service_next_renew_day`
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
- `$next_center_will_be_fired`
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
- `$npc_with_sisterly_advice`
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
- `$qst_collect_taxes_currently_collecting`
- `$qst_collect_taxes_halve_taxes`
- `$qst_collect_taxes_hourly_income`
- `$qst_collect_taxes_menu_counter`
- `$qst_collect_taxes_total_hours`
- `$qst_collect_taxes_unrest_counter`
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
- `$qst_kill_local_merchant_center`
- `$qst_scout_waypoints_wp_1`
- `$qst_scout_waypoints_wp_1_visited`
- `$qst_scout_waypoints_wp_2`
- `$qst_scout_waypoints_wp_2_visited`
- `$qst_scout_waypoints_wp_3`
- `$qst_scout_waypoints_wp_3_visited`
- `$qst_train_peasants_against_bandits_currently_training`
- `$qst_train_peasants_against_bandits_num_hours_trained`
- `$qst_troublesome_bandits_eliminated`
- `$qst_troublesome_bandits_eliminated_by_player`
- `$quest_auto_menu`
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
- `$training_ground_position_changed`
- `$waiting_for_arena_fight_result`

**Всего уникальных глобальных переменных:** 584


## 4. РЕЕСТР ЛОКАЛЬНЫХ РЕГИСТРОВ И СТРОК

### Паттерны использования регистров:

| Регистр | Количество использований |
|---------|-------------------------|
| s1 | 482 |
| s0 | 360 |
| s4 | 259 |
| s2 | 227 |
| s5 | 221 |
| s11 | 198 |
| s14 | 193 |
| s3 | 191 |
| s8 | 126 |
| s10 | 121 |
| s12 | 108 |
| s9 | 106 |
| s15 | 104 |
| s7 | 82 |
| s6 | 47 |
| s13 | 43 |


---

**Сгенерировано:** 52 файлов констант, 30 файлов данных, 33 файлов обработки

**Базовая директория:** `Vanilla Module System v1.171`
