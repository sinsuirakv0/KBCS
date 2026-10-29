use crate::{
    model::{csv_rows, numeric_rows},
    store::Database,
};
use anyhow::{Context, Result};
use rusqlite::{OptionalExtension, params};
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

type Row = (usize, Vec<String>, Vec<Option<i64>>);
pub(super) fn number(row: &[Option<i64>], column: usize) -> i64 {
    row.get(column).copied().flatten().unwrap_or(0)
}

// 元行番号・空欄・未収録列を保持する。注記は原本bytesにも残す。
pub(super) fn rows(bytes: &[u8], columns: Option<usize>) -> Result<Vec<Row>> {
    let mut result = Vec::new();
    for (index, line) in std::str::from_utf8(bytes)?
        .trim_start_matches('\u{feff}')
        .lines()
        .enumerate()
    {
        let line = line.split_once("//").map_or(line, |(line, _)| line).trim();
        if line
            .split(',')
            .next()
            .unwrap_or("")
            .trim()
            .parse::<i64>()
            .is_err()
        {
            continue;
        }
        for cells in csv_rows(line.as_bytes())? {
            let values = cells
                .iter()
                .take(columns.unwrap_or(cells.len()))
                .map(|cell| {
                    let cell = cell.trim();
                    if cell.is_empty() {
                        Ok(None)
                    } else if cell == "." {
                        Ok(Some(0))
                    } else {
                        Ok(Some(cell.parse::<i64>().with_context(|| {
                            format!("数値セル不正: 行{} {cell}", index + 1)
                        })?))
                    }
                })
                .collect::<Result<Vec<_>>>()?;
            result.push((index + 1, cells, values));
        }
    }
    Ok(result)
}

mod extras;
mod importer;
mod rewards;
pub(crate) use importer::import;

fn series_label(series: &str) -> &str {
    importer::SERIES
        .iter()
        .find(|s| s.0 == series)
        .map(|s| s.1)
        .unwrap_or(match series {
            "EOC" => "日本編",
            "ITF" => "未来編",
            "COTC" => "宇宙編",
            "EOCZ" => "日本編（ゾンビ）",
            "ITFZ" => "未来編（ゾンビ）",
            "COTCZ" => "宇宙編（ゾンビ）",
            "COTCI" => "宇宙編 襲来",
            "COTCZI" => "宇宙編 ゾンビ襲来",
            _ => series,
        })
}
fn map_key(series: &str, index: i64) -> String {
    if ["EOC", "ITF", "COTC", "EOCZ", "ITFZ", "COTCZ"].contains(&series) {
        format!("{series}{}", index + 1)
    } else if series == "COTCI" {
        "COTC-I".into()
    } else if series == "COTCZI" {
        "COTCZ-I".into()
    } else {
        format!("{series}{index:03}")
    }
}

fn raw(text: String) -> Result<Value> {
    Ok(serde_json::from_str(&text)?)
}

pub fn catalog(database: &Database, region: &str) -> Result<Value> {
    catalog_map(database, region, None)
}

pub fn catalog_map(database: &Database, region: &str, selected: Option<&str>) -> Result<Value> {
    catalog_selection(database, region, selected, None, false)
}

fn catalog_selection(
    database: &Database,
    region: &str,
    selected: Option<&str>,
    selected_stage: Option<i64>,
    summary: bool,
) -> Result<Value> {
    let connection = &database.connection;
    let metadata = database.metadata()?;
    let extras = extras::Extras::read(connection, region)?;
    let selected_id = if let Some(key) = selected {
        let mut query = connection
            .prepare_cached("SELECT id,series,map_index FROM stage_map WHERE region=?")?;
        let ids = query
            .query_map([region], |r| {
                Ok((
                    r.get::<_, i64>(0)?,
                    r.get::<_, String>(1)?,
                    r.get::<_, i64>(2)?,
                ))
            })?
            .collect::<rusqlite::Result<Vec<_>>>()?;
        Some(
            ids.into_iter()
                .find(|(_, series, index)| map_key(series, *index) == key)
                .context("マップが見つかりません")?
                .0,
        )
    } else {
        None
    };
    let mut definition_summaries = BTreeMap::new();
    let mut summary_statement=connection.prepare_cached("SELECT d.path,d.width,d.background,json_group_array(s.enemy_raw-2) FILTER(WHERE s.enemy_raw IS NOT NULL),coalesce(max(s.after_castle!=0),0),coalesce(max(s.kills!=0),0),coalesce(max(s.attack_percent!=0 AND s.attack_percent!=s.hp_percent),0),d.no_continue,d.boss_guard,d.time_raw,d.castle_raw FROM stage_definition d LEFT JOIN stage_definition_spawn s ON d.region=s.region AND d.path=s.definition_path WHERE d.region=?1 AND (?2 IS NULL OR d.path IN (SELECT definition_path FROM stage_entry WHERE region=?1 AND map_id=?2 AND (?3 IS NULL OR stage_index=?3) UNION SELECT definition_path FROM stage_variant WHERE region=?1 AND map_id=?2 AND (?3 IS NULL OR stage_index=?3))) GROUP BY d.path")?;
    for row in summary_statement.query_map(params![region, selected_id, selected_stage], |r| {
        Ok((
            r.get::<_, String>(0)?,
            r.get::<_, i64>(1)?,
            r.get::<_, i64>(2)?,
            r.get::<_, String>(3)?,
            r.get::<_, bool>(4)?,
            r.get::<_, bool>(5)?,
            r.get::<_, bool>(6)?,
            r.get::<_, i64>(7)?,
            r.get::<_, i64>(8)?,
            r.get::<_, i64>(9)?,
            r.get::<_, i64>(10)?,
        ))
    })? {
        let (
            path,
            width,
            background,
            enemies,
            after,
            kills,
            split,
            no_continue,
            guard,
            time,
            castle,
        ) = row?;
        let enemies = serde_json::from_str::<Vec<i64>>(&enemies)?
            .into_iter()
            .collect::<BTreeSet<_>>();
        definition_summaries.insert(
            path,
            json!({"width":width,"background":background,"enemies":enemies,"flags":([(after,"afterCastle"),(kills,"kills"),(split,"splitMultiplier"),(no_continue==1,"noContinue"),(guard==1,"bossGuard"),(time>0,"timeLimit"),(castle>1,"enemyCastle")].into_iter().filter_map(|(a,k)|a.then_some(k)).collect::<Vec<_>>())}),
        );
    }
    let mut maps = Vec::new();
    let mut stages = Vec::new();
    let mut statement=connection.prepare_cached("SELECT id,name,source_path,raw_headers,options_raw,options_row,series,native_kind,map_index,acquisition_id,score_id,mode FROM stage_map WHERE region=? ORDER BY id")?;
    let entries = statement.query_map([region], |row| {
        Ok((
            row.get::<_, i64>(0)?,
            row.get::<_, String>(1)?,
            row.get::<_, String>(2)?,
            row.get::<_, String>(3)?,
            row.get::<_, String>(4)?,
            row.get::<_, i64>(5)?,
            row.get::<_, String>(6)?,
            row.get::<_, i64>(7)?,
            row.get::<_, i64>(8)?,
            row.get::<_, Option<i64>>(9)?,
            row.get::<_, Option<i64>>(10)?,
            row.get::<_, i64>(11)?,
        ))
    })?;
    for entry in entries {
        let (
            id,
            name,
            path,
            headers,
            options,
            option_row,
            series,
            kind,
            map_index,
            acquisition_id,
            score_id,
            mode,
        ) = entry?;
        let key = map_key(&series, map_index);
        if selected.is_some_and(|s| s != key) {
            continue;
        }
        let materials = crate::stage_materials::read(connection, region, id)?;
        let mut statement = connection.prepare_cached(
            "SELECT multiplier FROM stage_crown WHERE region=? AND map_id=? ORDER BY crown",
        )?;
        let stars = statement
            .query_map(params![region, id], |row| row.get::<_, i64>(0))?
            .collect::<rusqlite::Result<Vec<_>>>()?;
        let mut statement=connection.prepare_cached("SELECT crown,stage_index,rarity_mask,source_row,raw_cells FROM stage_limit WHERE region=? AND map_id=? ORDER BY position")?;
        let mut limits=statement.query_map(params![region,id],|row| Ok(json!({"crown":row.get::<_,i64>(0)?,"stage":row.get::<_,i64>(1)?,"rarities":row.get::<_,i64>(2)?,"sourceRow":row.get::<_,i64>(3)?,"raw":row.get::<_,String>(4)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
        for limit in &mut limits {
            let cells: Vec<String> =
                serde_json::from_str(limit["raw"].as_str().context("制限原値不正")?)?;
            let value = |index| {
                cells
                    .get(index)
                    .and_then(|v: &String| v.trim().parse::<i64>().ok())
                    .unwrap_or(0)
            };
            limit["maxUnits"] = json!(value(4));
            limit["slots"] = json!(value(5));
            limit["minCost"] = json!(value(6));
            limit["maxCost"] = json!(value(7));
            limit["group"] = json!(extras.group(value(8))?);
        }
        let mut stage_ids = Vec::new();
        let mut statement=connection.prepare_cached("SELECT stage_index,name,energy,xp_raw,width,castle_hp,spawn_min,spawn_max,background,max_enemies,castle_raw,time_raw,boss_guard,no_continue,difficulty,settings_raw,header_raw,rewards_raw,source_path,metadata_row FROM stage WHERE region=? AND map_id=? ORDER BY stage_index")?;
        let entries = statement.query_map(params![region, id], |row| {
            let numbers = (2..14)
                .map(|column| row.get::<_, Option<i64>>(column))
                .collect::<rusqlite::Result<Vec<_>>>()?;
            Ok((
                row.get::<_, i64>(0)?,
                row.get::<_, String>(1)?,
                numbers,
                row.get::<_, Option<f64>>(14)?,
                (15..19)
                    .map(|column| row.get::<_, String>(column))
                    .collect::<rusqlite::Result<Vec<_>>>()?,
                row.get::<_, i64>(19)?,
            ))
        })?;
        for entry in entries {
            let (index, name, n, difficulty, text, metadata_row) = entry?;
            if selected_stage.is_some_and(|value| value != index) {
                continue;
            }
            let stage_id = format!("{key}-{index}");
            stage_ids.push(stage_id.clone());
            let mut spawns = Vec::new();
            let mut enemies = BTreeSet::new();
            let mut flags = BTreeSet::new();
            if !summary {
                let mut statement=connection.prepare_cached("SELECT source_row,raw_cells,enemy_raw,count,first_raw,interval_min_raw,interval_max_raw,castle,layer_min,layer_max,boss,hp_percent,score,attack_percent,after_castle,kills FROM stage_spawn WHERE region=? AND map_id=? AND stage_index=? ORDER BY position")?;
                let rows = statement.query_map(
                    params![region, if summary { -1 } else { id }, index],
                    |row| {
                        Ok((
                            row.get::<_, i64>(0)?,
                            row.get::<_, String>(1)?,
                            (2..16)
                                .map(|column| row.get::<_, i32>(column))
                                .collect::<rusqlite::Result<Vec<_>>>()?,
                        ))
                    },
                )?;
                for row in rows {
                    let (source_row, cells, v) = row?;
                    let mut loaded = v.clone();
                    for column in [2, 3, 4] {
                        loaded[column] = loaded[column]
                            .checked_mul(2)
                            .context("出現待機の整数上限")?;
                    }
                    let health = if series == "EOC" {
                        [100, 150, 400][map_index as usize]
                    } else {
                        v[9]
                    };
                    let attack = if series == "EOC" {
                        health
                    } else if v[11] != 0 {
                        v[11]
                    } else {
                        v[9]
                    };
                    if attack != health {
                        flags.insert("splitMultiplier");
                    }
                    if v[12] != 0 {
                        flags.insert("afterCastle");
                    }
                    if v[13] != 0 {
                        flags.insert("kills");
                    }
                    enemies.insert(v[0] - 2);
                    spawns.push(json!({"enemy":v[0]-2,"count":v[1],"first":loaded[2],"interval":[loaded[3],loaded[4]],"castle":v[5],"layers":[v[6],v[7]],"boss":v[8],"health":health,"attack":attack,"score":v[10],"afterCastle":v[12]!=0,"kills":v[13],"native":loaded,"raw":raw(cells)?,"sourceRow":source_row}));
                }
            }
            let mut statement=connection.prepare_cached("SELECT comparison,item_id,amount,source_column,kind,source_path,source_locator FROM stage_reward WHERE region=? AND map_id=? AND stage_index=? ORDER BY position")?;
            let drops=statement.query_map(params![region,id,index],|row|Ok(json!({"weight":row.get::<_,i64>(0)?,"chance":null,"id":row.get::<_,i64>(1)?,"count":row.get::<_,i64>(2)?,"sourceColumn":row.get::<_,i64>(3)?,"kind":row.get::<_,String>(4)?,"source":row.get::<_,String>(5)?,"sourceLocator":row.get::<_,String>(6)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
            if limits
                .iter()
                .any(|limit| limit["stage"].as_i64().is_some_and(|v| v < 0 || v == index))
            {
                flags.insert("restriction");
            }
            if n[11] == Some(1) {
                flags.insert("noContinue");
            }
            if n[10] == Some(1) {
                flags.insert("bossGuard");
            }
            if n[8].is_some_and(|v| v > 1) {
                flags.insert("enemyCastle");
            }
            if n[9].is_some_and(|v| v > 0) {
                flags.insert("timeLimit");
            }
            let reward_raw = raw(text[2].clone())?;
            let reward_numbers: Vec<Option<i64>> =
                serde_json::from_value::<Vec<String>>(reward_raw.clone())?
                    .iter()
                    .map(|value| value.parse().ok())
                    .collect();
            let mut music = vec![number(&reward_numbers, 2)];
            if number(&reward_numbers, 3) > 0
                && number(&reward_numbers, 3) < 100
                && number(&reward_numbers, 4) != music[0]
            {
                music.push(number(&reward_numbers, 4));
                flags.insert("musicChange");
            }
            stages.push(json!({"id":stage_id,"map":key,"index":index,"name":name,"energy":n[0],"xp":n[1],"width":n[2],"castleHealth":n[3],"spawnInterval":[n[4],n[5]],"background":n[6],"maxEnemies":n[7].map(|v|v.min(50)),"enemyCastle":if n[8].is_some_and(|v|v>1) {n[8].map(|v|v-2)}else{None},"timeLimit":n[9].map(|v|v*1800),"bossGuard":n[10]==Some(1),"noContinue":n[11]==Some(1),"difficulty":difficulty,"spawns":spawns,"enemies":enemies,"flags":flags,"music":music,"rewards":drops.iter().map(|drop|drop["id"].clone()).collect::<Vec<_>>(),"drops":drops.iter().filter(|d|d["kind"]=="normal" || d["kind"]=="weight").collect::<Vec<_>>(),"scoreRewards":drops.iter().filter(|d|d["kind"]=="score").map(|d|json!({"id":d["id"],"count":d["count"],"score":d["weight"]})).collect::<Vec<_>>(),"clearRewards":[],"rewardMode":number(&reward_numbers,8),"rewardOnce":reward_numbers.last().copied().flatten(),"source":text[3],"metadataRow":metadata_row,"rawSettings":raw(text[0].clone())?,"rawHeader":raw(text[1].clone())?,"rawRewards":reward_raw}));
        }
        for stage in stages.iter_mut().filter(|s| s["map"] == key) {
            let index = stage["index"].as_i64().context("面番号欠測")?;
            stage["nativeMode"] = json!(mode);
            stage["nativeKind"] = json!(kind);
            stage["scoreMode"] = json!(["R", "T", "PR"].contains(&series.as_str()));
            stage["damageCondition"] = json!(
                stage["scoreMode"] == true || stage["timeLimit"].as_i64().is_some_and(|v| v > 0)
            );
            let (definition,listed):(Option<String>,i64)=connection.query_row("SELECT definition_path,listed FROM stage_entry WHERE region=? AND map_id=? AND stage_index=?",params![region,id,index],|r|Ok((r.get(0)?,r.get(1)?)))?;
            if summary
                && let Some(info) = definition
                    .as_ref()
                    .and_then(|p| definition_summaries.get(p))
            {
                stage["enemies"] = info["enemies"].clone();
                for flag in info["flags"].as_array().into_iter().flatten() {
                    add_flag(stage, flag.as_str().context("フラグ不正")?, false)?;
                }
            }
            stage["listed"] = json!(listed != 0);
            let mut statement=connection.prepare_cached("SELECT definition_path,name,position FROM stage_variant WHERE region=? AND map_id=? AND stage_index=? ORDER BY position")?;
            let variants=statement.query_map(params![region,id,index],|r|Ok(json!({"source":r.get::<_,String>(0)?,"name":r.get::<_,String>(1)?,"index":r.get::<_,i64>(2)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
            stage["missing"] = json!(definition.is_none() && variants.is_empty());
            if !variants.is_empty() {
                stage["patterns"] = json!(
                    variants
                        .iter()
                        .filter_map(|v| v["source"]
                            .as_str()
                            .and_then(|p| definition_summaries.get(p)))
                        .map(|v| {
                            let mut p = v.clone();
                            let mut flags = stage["flags"].as_array().cloned().unwrap_or_default();
                            for flag in p["flags"].as_array().into_iter().flatten() {
                                if !flags.contains(flag) {
                                    flags.push(flag.clone());
                                }
                            }
                            p["flags"] = json!(flags);
                            p
                        })
                        .collect::<Vec<_>>()
                );
                let enemies = stage["patterns"]
                    .as_array()
                    .into_iter()
                    .flatten()
                    .flat_map(|p| {
                        p["enemies"]
                            .as_array()
                            .into_iter()
                            .flatten()
                            .filter_map(Value::as_i64)
                    })
                    .collect::<BTreeSet<_>>();
                stage["enemies"] = json!(enemies);
                stage["variants"] = json!(variants);
                stage["patternLabel"] = json!(if series == "L" {
                    "テンプレート"
                } else {
                    "参照候補"
                });
            }
            let extra = extras.stage(id, index)?;
            for (k, v) in extra.as_object().context("ステージ補助設定不正")? {
                stage[k] = v.clone();
            }
            if let Some(items) = stage["clearRewards"].as_array().cloned() {
                for item in items {
                    let rewards = stage["rewards"].as_array_mut().context("報酬索引不正")?;
                    if !rewards.contains(&item["id"]) {
                        rewards.push(item["id"].clone());
                    }
                }
            }
            if let Some(raw) = stage["rawSettings"].as_array() {
                let values = raw
                    .iter()
                    .map(|v| v.as_str().unwrap_or("").trim().parse::<i64>().unwrap_or(0))
                    .collect::<Vec<_>>();
                if values.get(2).is_some_and(|v| *v > 0) {
                    let ex_id = 4000 + values.get(3).copied().unwrap_or(0);
                    stage["ex"] = json!({"chance":values[2],"nativeMap":ex_id,"map":format!("EX{:03}",ex_id-4000),"min":values.get(4).copied().unwrap_or(0),"max":values.get(5).copied().unwrap_or(0)});
                }
            }
            let random_pattern = !stage["variants"].is_null();
            if random_pattern {
                add_flag(stage, "randomPattern", true)?;
            }
            for (field, label) in [
                ("formation", "formation"),
                ("pointRules", "pointRule"),
                ("levelSeal", "levelSeal"),
                ("ex", "ex"),
                ("exLottery", "ex"),
            ] {
                if !stage[field].is_null() {
                    add_flag(stage, label, true)?;
                }
            }
            for (active, label) in [
                (definition.is_none() && !random_pattern, "missing"),
                (listed != 1, "unlisted"),
            ] {
                if active {
                    add_flag(stage, label, true)?;
                }
            }
            let pattern_flags = stage["patterns"]
                .as_array()
                .into_iter()
                .flatten()
                .flat_map(|p| {
                    p["flags"]
                        .as_array()
                        .into_iter()
                        .flatten()
                        .filter_map(Value::as_str)
                })
                .map(String::from)
                .collect::<BTreeSet<_>>();
            for flag in pattern_flags {
                add_flag(stage, &flag, false)?;
            }
        }
        maps.push(json!({"key":key,"series":series,"number":map_index,"nativeId":id,"name":name,"stars":stars,"limits":limits,"materials":materials,"stages":stage_ids,"rules":[],"conditions":[],"source":path,"rawHeaders":raw(headers.clone())?,"acquisitionId":acquisition_id,"scoreId":score_id,"nativeKind":kind,"nativeMode":mode,"rawOptions":raw(options)?,"optionsRow":option_row}));
    }
    for map in &mut maps {
        let extra = extras.map(
            map["nativeId"].as_i64().context("マップID欠測")?,
            &map["rawHeaders"],
        )?;
        for (k, v) in extra.as_object().context("マップ補助設定不正")? {
            map[k] = v.clone();
        }
        let values = map["rawOptions"]
            .as_array()
            .map(|a| {
                a.iter()
                    .map(|v| v.as_str().unwrap_or("").trim().parse::<i64>().unwrap_or(0))
                    .collect::<Vec<_>>()
            })
            .unwrap_or_default();
        map["clearLimit"] = json!(values.get(9).copied().unwrap_or(0));
        map["interval"] = json!(values.get(11).copied().unwrap_or(0));
        map["abyss"] = json!(values.get(2) == Some(&1));
        map["hiddenAfterClear"] = json!(values.get(14).is_some_and(|v| *v > 0));
    }
    for map in &maps {
        for stage in stages.iter_mut().filter(|s| s["map"] == map["key"]) {
            if map["rules"].as_array().is_some_and(|v| !v.is_empty()) {
                add_flag(stage, "specialRule", true)?;
            }
            if map["abyss"] == true {
                add_flag(stage, "abyss", true)?;
            }
        }
        if let Some(items) = map.pointer("/materials/items").and_then(Value::as_array) {
            for stage in stages.iter_mut().filter(|stage| stage["map"] == map["key"]) {
                let rewards = stage["rewards"].as_array_mut().context("報酬配列不正")?;
                for item in items {
                    if !rewards.contains(&item["id"]) {
                        rewards.push(item["id"].clone());
                    }
                }
            }
        }
    }
    let (_, _, _, bytes) = database.source("res/GatyaitemName.csv")?;
    let names = csv_rows(&bytes)?;
    let mut rewards = BTreeMap::new();
    for stage in &stages {
        for reward in stage["rewards"].as_array().context("報酬配列不正")? {
            let id = reward.as_i64().context("報酬ID欠測")?;
            let icon = format!("Image/gatyaitemD_{id:02}_f.png");
            let exists: bool = connection.query_row(
                "SELECT EXISTS(SELECT 1 FROM source_file WHERE path=?)",
                [&icon],
                |row| row.get(0),
            )?;
            let name = names
                .get(id as usize)
                .and_then(|row| row.first())
                .cloned()
                .unwrap_or_else(|| format!("報酬 {id}"));
            rewards.entry(id.to_string()).or_insert_with(
                || json!({"id":id,"name":name,"icon":if exists {Some(icon)}else{None}}),
            );
        }
    }
    // アイテム名の配列へキャラ報酬IDを当てず、原本の対応表で結ぶ。
    let (_, _, _, bytes) = database.source("Data/drop_chara.csv")?;
    for (_, _, values) in rows(&bytes, None)? {
        let id = number(&values, 0).to_string();
        if let Some(reward) = rewards.get_mut(&id) {
            let unit = number(&values, 2);
            let name: Option<String> = connection
                .query_row(
                    "SELECT name FROM form WHERE region=? AND unit_id=? AND form_index=0",
                    params![region, unit],
                    |row| row.get(0),
                )
                .optional()?;
            *reward = json!({"id":number(&values,0),"name":name.unwrap_or_else(||format!("キャラ {unit}")),"unit":unit,"form":0});
        }
    }
    let (_, _, _, bytes) = database.source("Data/unitbuy.csv")?;
    for (unit, (_, values)) in numeric_rows(&bytes)?.into_iter().enumerate() {
        let id = number(&values, 23);
        if id < 10000 {
            continue;
        }
        if let Some(reward) = rewards.get_mut(&id.to_string()) {
            let name: Option<String> = connection.query_row(
                "SELECT name FROM form WHERE region=? AND unit_id=? ORDER BY form_index=2 DESC,form_index LIMIT 1",
                params![region,unit as i64],|row|row.get(0),
            ).optional()?;
            *reward = json!({"id":id,"name":format!("第3形態進化権：{}",name.unwrap_or_else(||format!("キャラ {unit}"))),"unit":unit,"form":2,"evolution":true});
        }
    }
    rewards::decorate(database, &mut rewards)?;
    for stage in &mut stages {
        let series = maps
            .iter()
            .find(|map| map["key"] == stage["map"])
            .and_then(|map| map["series"].as_str())
            .unwrap_or("");
        crate::stage_media::annotate(stage, series);
    }
    Ok(
        json!({"schemaVersion":2,"gameVersion":metadata.get("version"),"calculationVersion":crate::compatibility::calculation_version(database)?,"revision":metadata.get("revision"),"buildId":metadata.get("build_id"),"imageBase":"/api/asset/","scope":{"bands":maps.iter().filter_map(|m|m["nativeId"].as_i64()).map(|id|id/1000*1000).collect::<BTreeSet<_>>(),"nativeVersion":"15.7.2"},"series":maps.iter().filter_map(|m|m["series"].as_str()).collect::<BTreeSet<_>>().into_iter().map(|s|json!({"id":s,"label":series_label(s)})).collect::<Vec<_>>(),"maps":maps,"stages":stages,"rewards":rewards,"musicCatalog":crate::stage_media::music_catalog(database)?}),
    )
}

// 候補の数値は元の戦闘定義から取得し、選択した面の報酬・統率力と合成する。
pub fn variant(
    database: &Database,
    region: &str,
    map: &str,
    index: i64,
    path: &str,
) -> Result<Value> {
    let mut value = catalog_selection(database, region, Some(map), Some(index), false)?;
    let map_id = value["maps"]
        .as_array()
        .and_then(|v| v.first())
        .and_then(|v| v["nativeId"].as_i64())
        .context("マップが見つかりません")?;
    let name: String=database.connection.query_row("SELECT name FROM stage_variant WHERE region=? AND map_id=? AND stage_index=? AND definition_path=?",params![region,map_id,index,path],|r|r.get(0)).optional()?.context("このステージの候補ではありません")?;
    let series = value["maps"][0]["series"].as_str().unwrap_or("").to_owned();
    let stage = value["stages"]
        .as_array_mut()
        .and_then(|a| a.iter_mut().find(|s| s["index"] == index))
        .context("ステージが見つかりません")?;
    let definition = definition(database, region, path)?;
    for (key, v) in definition.as_object().context("戦闘定義不正")? {
        stage[key] = v.clone();
    }
    let dynamic = [
        "missing",
        "noContinue",
        "bossGuard",
        "enemyCastle",
        "timeLimit",
        "splitMultiplier",
        "kills",
        "afterCastle",
        "animatedBackground",
    ];
    let mut flags = stage["flags"].as_array().cloned().unwrap_or_default();
    flags.retain(|v| !dynamic.contains(&v.as_str().unwrap_or("")));
    for (condition, name) in [
        (stage["noContinue"] == true, "noContinue"),
        (stage["bossGuard"] == true, "bossGuard"),
        (!stage["enemyCastle"].is_null(), "enemyCastle"),
        (stage["timeLimit"].as_i64().unwrap_or(0) > 0, "timeLimit"),
    ] {
        if condition {
            flags.push(json!(name));
        }
    }
    for (field, name) in [("kills", "kills"), ("afterCastle", "afterCastle")] {
        if stage["spawns"]
            .as_array()
            .into_iter()
            .flatten()
            .any(|s| s[field] == true || s[field].as_i64().unwrap_or(0) > 0)
        {
            flags.push(json!(name));
        }
    }
    if stage["spawns"]
        .as_array()
        .into_iter()
        .flatten()
        .any(|s| s["health"] != s["attack"])
    {
        flags.push(json!("splitMultiplier"));
    }
    stage["flags"] = json!(flags);
    stage["damageCondition"] =
        json!(stage["scoreMode"] == true || stage["timeLimit"].as_i64().unwrap_or(0) > 0);
    stage["missing"] = json!(false);
    stage["patternSource"] = json!(path);
    stage["patternName"] = json!(name);
    crate::stage_media::annotate(stage, &series);
    Ok(stage.clone())
}

fn definition(database: &Database, region: &str, path: &str) -> Result<Value> {
    let connection = &database.connection;
    let (settings,header,n)=connection.query_row("SELECT settings_raw,header_raw,width,castle_hp,spawn_min,spawn_max,background,max_enemies,castle_raw,time_raw,boss_guard,no_continue FROM stage_definition WHERE region=? AND path=?",params![region,path],|r|Ok((r.get::<_,String>(0)?,r.get::<_,String>(1)?,(2..12).map(|i|r.get::<_,i64>(i)).collect::<rusqlite::Result<Vec<_>>>()?)))?;
    let mut statement=connection.prepare_cached("SELECT source_row,raw_cells,enemy_raw,count,first_raw,interval_min_raw,interval_max_raw,castle,layer_min,layer_max,boss,hp_percent,score,attack_percent,after_castle,kills FROM stage_definition_spawn WHERE region=? AND definition_path=? ORDER BY position")?;
    let entries = statement.query_map(params![region, path], |r| {
        Ok((
            r.get::<_, i64>(0)?,
            r.get::<_, String>(1)?,
            (2..16)
                .map(|i| r.get::<_, i32>(i))
                .collect::<rusqlite::Result<Vec<_>>>()?,
        ))
    })?;
    let mut spawns = Vec::new();
    let mut enemies = BTreeSet::new();
    for row in entries {
        let (line, raw_cells, v) = row?;
        let mut loaded = v.clone();
        for column in [2, 3, 4] {
            loaded[column] = loaded[column]
                .checked_mul(2)
                .context("出現待機の整数上限")?;
        }
        enemies.insert(v[0] - 2);
        spawns.push(json!({"enemy":v[0]-2,"count":v[1],"first":loaded[2],"interval":[loaded[3],loaded[4]],"castle":v[5],"layers":[v[6],v[7]],"boss":v[8],"health":v[9],"attack":if v[11]!=0 {v[11]} else {v[9]},"score":v[10],"afterCastle":v[12]!=0,"kills":v[13],"native":loaded,"raw":raw(raw_cells)?,"sourceRow":line}));
    }
    Ok(
        json!({"source":path,"rawSettings":raw(settings)?,"rawHeader":raw(header)?,"width":n[0],"castleHealth":n[1],"spawnInterval":[n[2],n[3]],"background":n[4],"maxEnemies":n[5].min(50),"enemyCastle":if n[6]>1 {Some(n[6]-2)} else {None},"timeLimit":n[7]*1800,"bossGuard":n[8]==1,"noContinue":n[9]==1,"spawns":spawns,"enemies":enemies}),
    )
}

pub fn search_catalog(database: &Database, region: &str) -> Result<Value> {
    let mut value = catalog_selection(database, region, None, None, true)?;
    if let Some(stages) = value["stages"].as_array_mut() {
        for stage in stages {
            if let Some(object) = stage.as_object_mut() {
                for key in [
                    "spawns",
                    "rawHeader",
                    "rawSettings",
                    "rawRewards",
                    "source",
                    "metadataRow",
                ] {
                    object.remove(key);
                }
            }
        }
    }
    Ok(value)
}

fn add_flag(stage: &mut Value, label: &str, common: bool) -> Result<()> {
    let flag = json!(label);
    let flags = stage["flags"]
        .as_array_mut()
        .context("ステージフラグ不正")?;
    if !flags.contains(&flag) {
        flags.push(flag.clone());
    }
    if common && let Some(patterns) = stage["patterns"].as_array_mut() {
        for pattern in patterns {
            let flags = pattern["flags"].as_array_mut().context("候補フラグ不正")?;
            if !flags.contains(&flag) {
                flags.push(flag.clone());
            }
        }
    }
    Ok(())
}

// 編成と報酬表示で、同じ原本の本能玉ID・名称・3層アイコンを使う。
pub fn equipment_catalog(database: &Database) -> Result<Value> {
    let raw: Value = serde_json::from_slice(&database.source("Data/equipmentlist.json")?.3)?;
    let mut items = raw["ID"]
        .as_array()
        .context("本能玉の定義なし")?
        .iter()
        .enumerate()
        .map(|(index, _)| ((30000 + index).to_string(), json!({"id":30000+index})))
        .collect::<BTreeMap<_, _>>();
    rewards::decorate(database, &mut items)?;
    Ok(json!({"items":items.into_values().collect::<Vec<_>>()}))
}
