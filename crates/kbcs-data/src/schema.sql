PRAGMA foreign_keys = ON;
PRAGMA user_version = 8;
CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL) STRICT;
CREATE TABLE source_file (
 path TEXT PRIMARY KEY, original_path TEXT NOT NULL, source_kind TEXT NOT NULL,
 sha256 TEXT NOT NULL, bytes BLOB NOT NULL
) STRICT;
CREATE TABLE asset_reference (
 path TEXT PRIMARY KEY, original_path TEXT NOT NULL, source_kind TEXT NOT NULL,
 sha256 TEXT NOT NULL, size INTEGER NOT NULL
) STRICT;
CREATE TABLE unit (
 region TEXT NOT NULL, id INTEGER NOT NULL, rarity INTEGER NOT NULL,
 aliases TEXT NOT NULL, max_level INTEGER NOT NULL, plus_level INTEGER NOT NULL, is_spirit INTEGER NOT NULL, kind TEXT NOT NULL, PRIMARY KEY(region,id)
) STRICT;
CREATE TABLE growth (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, position INTEGER NOT NULL, rate INTEGER,
 PRIMARY KEY(region,unit_id,position), FOREIGN KEY(region,unit_id) REFERENCES unit(region,id)
) STRICT;
CREATE TABLE talent (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, talent_index INTEGER NOT NULL,
 skill_id INTEGER NOT NULL, max_level INTEGER NOT NULL CHECK(max_level > 0),
 description TEXT NOT NULL, level_limit INTEGER NOT NULL,
 target_mask INTEGER NOT NULL, add_targets INTEGER NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), source_row INTEGER NOT NULL, source_column INTEGER NOT NULL,
 PRIMARY KEY(region,unit_id,talent_index), FOREIGN KEY(region,unit_id) REFERENCES unit(region,id)
) STRICT;
CREATE TABLE talent_level (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, talent_index INTEGER NOT NULL,
 level INTEGER NOT NULL CHECK(level > 0), np INTEGER NOT NULL CHECK(np > 0),
 value0 INTEGER NOT NULL, value1 INTEGER NOT NULL, value2 INTEGER NOT NULL, value3 INTEGER NOT NULL,
 PRIMARY KEY(region,unit_id,talent_index,level), FOREIGN KEY(region,unit_id,talent_index) REFERENCES talent(region,unit_id,talent_index)
) STRICT;
CREATE TABLE form (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 name TEXT NOT NULL, description TEXT NOT NULL, search_text TEXT NOT NULL,
 hp INTEGER NOT NULL, speed INTEGER NOT NULL, range INTEGER NOT NULL,
 cost INTEGER NOT NULL, respawn_raw INTEGER NOT NULL, knockbacks INTEGER NOT NULL,
 interval_raw INTEGER NOT NULL, area INTEGER NOT NULL, attack_cycle INTEGER, animation_length INTEGER,
 source_path TEXT NOT NULL REFERENCES source_file(path), name_source TEXT NOT NULL,
 motion_path TEXT NOT NULL, icon_path TEXT REFERENCES source_file(path), raw_cells TEXT NOT NULL,
 PRIMARY KEY(region,unit_id,form_index), FOREIGN KEY(region,unit_id) REFERENCES unit(region,id)
) STRICT;
CREATE TABLE attack (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL, hit INTEGER NOT NULL,
 damage INTEGER NOT NULL, foreswing INTEGER, ability_enabled INTEGER, range_start INTEGER, range_end INTEGER,
 PRIMARY KEY(region,unit_id,form_index,hit), FOREIGN KEY(region,unit_id,form_index) REFERENCES form(region,unit_id,form_index)
) STRICT;
CREATE TABLE property (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 key TEXT NOT NULL, label TEXT NOT NULL,
 PRIMARY KEY(region,unit_id,form_index,key), FOREIGN KEY(region,unit_id,form_index) REFERENCES form(region,unit_id,form_index)
) STRICT;
CREATE TABLE property_parameter (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 key TEXT NOT NULL, position INTEGER NOT NULL, source_column INTEGER NOT NULL, value INTEGER,
 PRIMARY KEY(region,unit_id,form_index,key,position), FOREIGN KEY(region,unit_id,form_index,key) REFERENCES property(region,unit_id,form_index,key)
) STRICT;
CREATE TABLE progression (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 description TEXT NOT NULL, level INTEGER NOT NULL, xp INTEGER NOT NULL,
 PRIMARY KEY(region,unit_id,form_index), FOREIGN KEY(region,unit_id,form_index) REFERENCES form(region,unit_id,form_index)
) STRICT;
CREATE TABLE combo (
 region TEXT NOT NULL, id INTEGER NOT NULL, type INTEGER NOT NULL, grade INTEGER NOT NULL,
 name TEXT NOT NULL, effect TEXT NOT NULL, PRIMARY KEY(region,id)
) STRICT;
CREATE TABLE combo_member (
 region TEXT NOT NULL, combo_id INTEGER NOT NULL, position INTEGER NOT NULL,
 unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 PRIMARY KEY(region,combo_id,position), FOREIGN KEY(region,combo_id) REFERENCES combo(region,id)
) STRICT;
CREATE TABLE combo_effect (
 region TEXT NOT NULL, type INTEGER NOT NULL, label TEXT NOT NULL, PRIMARY KEY(region,type)
) STRICT;
CREATE TABLE combo_effect_value (
 region TEXT NOT NULL, type INTEGER NOT NULL, grade INTEGER NOT NULL, value INTEGER,
 PRIMARY KEY(region,type,grade), FOREIGN KEY(region,type) REFERENCES combo_effect(region,type)
) STRICT;
CREATE TABLE material (
 region TEXT NOT NULL, id INTEGER NOT NULL, name TEXT NOT NULL, icon_path TEXT REFERENCES source_file(path),
 PRIMARY KEY(region,id)
) STRICT;
CREATE TABLE evolution_material (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL, position INTEGER NOT NULL,
 material_id INTEGER NOT NULL, count INTEGER NOT NULL CHECK(count > 0), source_column INTEGER NOT NULL,
 PRIMARY KEY(region,unit_id,form_index,position), FOREIGN KEY(region,material_id) REFERENCES material(region,id),
 FOREIGN KEY(region,unit_id,form_index) REFERENCES progression(region,unit_id,form_index)
) STRICT;
CREATE TABLE progression_stage (
 region TEXT NOT NULL, unit_id INTEGER NOT NULL, form_index INTEGER NOT NULL,
 position INTEGER NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL,
 series TEXT NOT NULL, map_name TEXT NOT NULL, stage_name TEXT NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), source_row INTEGER NOT NULL,
 PRIMARY KEY(region,unit_id,form_index,map_id,stage_index),
 FOREIGN KEY(region,unit_id,form_index) REFERENCES progression(region,unit_id,form_index)
) STRICT;
CREATE TABLE enemy (
 region TEXT NOT NULL, id INTEGER NOT NULL, name TEXT NOT NULL, description TEXT NOT NULL,
 hp INTEGER NOT NULL, knockbacks INTEGER NOT NULL, speed INTEGER NOT NULL, range INTEGER NOT NULL,
 drop_amount INTEGER NOT NULL, interval_raw INTEGER NOT NULL, area INTEGER NOT NULL,
 attack_cycle INTEGER, animation_length INTEGER, motion_path TEXT NOT NULL,
 icon_path TEXT REFERENCES source_file(path), raw_cells TEXT NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), PRIMARY KEY(region,id)
) STRICT;
CREATE TABLE enemy_attack (
 region TEXT NOT NULL, enemy_id INTEGER NOT NULL, hit INTEGER NOT NULL,
 damage INTEGER NOT NULL, foreswing INTEGER, ability_enabled INTEGER, range_start INTEGER, range_end INTEGER,
 PRIMARY KEY(region,enemy_id,hit), FOREIGN KEY(region,enemy_id) REFERENCES enemy(region,id)
) STRICT;
CREATE TABLE stage_map (
 region TEXT NOT NULL, id INTEGER NOT NULL, name TEXT NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), raw_headers TEXT NOT NULL,
 options_raw TEXT NOT NULL, options_row INTEGER NOT NULL,
 series TEXT NOT NULL, native_kind INTEGER NOT NULL, map_index INTEGER NOT NULL,
 acquisition_id INTEGER, score_id INTEGER, mode INTEGER NOT NULL,
 PRIMARY KEY(region,id)
) STRICT;
CREATE TABLE stage_crown (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, crown INTEGER NOT NULL, multiplier INTEGER NOT NULL,
 PRIMARY KEY(region,map_id,crown), FOREIGN KEY(region,map_id) REFERENCES stage_map(region,id)
) STRICT;
CREATE TABLE stage_limit (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, position INTEGER NOT NULL,
 crown INTEGER NOT NULL, stage_index INTEGER NOT NULL, rarity_mask INTEGER NOT NULL,
 source_row INTEGER NOT NULL, raw_cells TEXT NOT NULL,
 PRIMARY KEY(region,map_id,position), FOREIGN KEY(region,map_id) REFERENCES stage_map(region,id)
) STRICT;
CREATE TABLE stage_definition (
 region TEXT NOT NULL, path TEXT NOT NULL REFERENCES source_file(path),
 settings_raw TEXT NOT NULL, header_raw TEXT NOT NULL, header_count INTEGER NOT NULL,
 numeric_terminator INTEGER NOT NULL, width INTEGER NOT NULL, castle_hp INTEGER NOT NULL,
 spawn_min INTEGER NOT NULL, spawn_max INTEGER NOT NULL, background INTEGER NOT NULL,
 max_enemies INTEGER NOT NULL, castle_raw INTEGER NOT NULL, time_raw INTEGER NOT NULL,
 boss_guard INTEGER NOT NULL, no_continue INTEGER NOT NULL,
 PRIMARY KEY(region,path)
) STRICT;
CREATE TABLE stage (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL, name TEXT NOT NULL,
 energy INTEGER, xp_raw INTEGER, width INTEGER, castle_hp INTEGER,
 spawn_min INTEGER, spawn_max INTEGER, background INTEGER, max_enemies INTEGER,
 castle_raw INTEGER, time_raw INTEGER, boss_guard INTEGER, no_continue INTEGER,
 difficulty REAL, settings_raw TEXT NOT NULL, header_raw TEXT NOT NULL, rewards_raw TEXT NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), metadata_row INTEGER NOT NULL,
 PRIMARY KEY(region,map_id,stage_index), FOREIGN KEY(region,map_id) REFERENCES stage_map(region,id)
) STRICT;
CREATE TABLE stage_entry (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL,
 definition_path TEXT, listed INTEGER NOT NULL, metadata_path TEXT NOT NULL REFERENCES source_file(path),
 PRIMARY KEY(region,map_id,stage_index),
 FOREIGN KEY(region,map_id,stage_index) REFERENCES stage(region,map_id,stage_index),
 FOREIGN KEY(region,definition_path) REFERENCES stage_definition(region,path)
) STRICT;
CREATE TABLE stage_definition_spawn (
 region TEXT NOT NULL, definition_path TEXT NOT NULL, position INTEGER NOT NULL,
 source_row INTEGER NOT NULL, raw_cells TEXT NOT NULL,
 enemy_raw INTEGER NOT NULL, count INTEGER NOT NULL, first_raw INTEGER NOT NULL,
 interval_min_raw INTEGER NOT NULL, interval_max_raw INTEGER NOT NULL, castle INTEGER NOT NULL,
 layer_min INTEGER NOT NULL, layer_max INTEGER NOT NULL, boss INTEGER NOT NULL,
 hp_percent INTEGER NOT NULL, score INTEGER NOT NULL, attack_percent INTEGER NOT NULL,
 after_castle INTEGER NOT NULL, kills INTEGER NOT NULL,
 PRIMARY KEY(region,definition_path,position),
 FOREIGN KEY(region,definition_path) REFERENCES stage_definition(region,path)
) STRICT;
CREATE VIEW stage_spawn AS
 SELECT s.region,s.map_id,s.stage_index,d.position,d.source_row,d.raw_cells,
 d.enemy_raw,d.count,d.first_raw,d.interval_min_raw,d.interval_max_raw,d.castle,
 d.layer_min,d.layer_max,d.boss,d.hp_percent,d.score,d.attack_percent,d.after_castle,d.kills
 FROM stage_entry s JOIN stage_definition_spawn d ON s.region=d.region AND s.definition_path=d.definition_path;
CREATE TABLE stage_reward (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL, position INTEGER NOT NULL,
 comparison INTEGER NOT NULL, item_id INTEGER NOT NULL, amount INTEGER NOT NULL, source_column INTEGER NOT NULL,
 kind TEXT NOT NULL, source_path TEXT NOT NULL REFERENCES source_file(path), source_locator TEXT NOT NULL,
 PRIMARY KEY(region,map_id,stage_index,position),
 FOREIGN KEY(region,map_id,stage_index) REFERENCES stage(region,map_id,stage_index)
) STRICT;
CREATE TABLE stage_variant (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL, position INTEGER NOT NULL,
 definition_path TEXT NOT NULL, name TEXT NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), source_row INTEGER NOT NULL, raw_cells TEXT NOT NULL,
 PRIMARY KEY(region,map_id,stage_index,position),
 FOREIGN KEY(region,map_id,stage_index) REFERENCES stage(region,map_id,stage_index),
 FOREIGN KEY(region,definition_path) REFERENCES stage_definition(region,path)
) STRICT;
CREATE TABLE stage_attachment (
 region TEXT NOT NULL, path TEXT NOT NULL REFERENCES source_file(path), content TEXT NOT NULL,
 PRIMARY KEY(region,path)
) STRICT;
CREATE TABLE stage_material_profile (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, miss INTEGER NOT NULL,
 source_path TEXT NOT NULL REFERENCES source_file(path), source_row INTEGER NOT NULL, raw_cells TEXT NOT NULL,
 PRIMARY KEY(region,map_id), FOREIGN KEY(region,map_id) REFERENCES stage_map(region,id)
) STRICT;
CREATE TABLE stage_material_crown (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, crown INTEGER NOT NULL, multiplier REAL NOT NULL,
 PRIMARY KEY(region,map_id,crown), FOREIGN KEY(region,map_id) REFERENCES stage_material_profile(region,map_id)
) STRICT;
CREATE TABLE stage_material_count (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, stage_index INTEGER NOT NULL, count REAL NOT NULL,
 PRIMARY KEY(region,map_id,stage_index), FOREIGN KEY(region,map_id) REFERENCES stage_material_profile(region,map_id)
) STRICT;
CREATE TABLE stage_material_weight (
 region TEXT NOT NULL, map_id INTEGER NOT NULL, slot INTEGER NOT NULL, item_id INTEGER, weight INTEGER NOT NULL,
 PRIMARY KEY(region,map_id,slot), FOREIGN KEY(region,map_id) REFERENCES stage_material_profile(region,map_id)
) STRICT;
