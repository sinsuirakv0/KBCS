use crate::{
    import::read_asset,
    model::{csv_rows, numeric_rows},
    source::{Dataset, Source},
    store::Database,
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

type Row = (usize, Vec<String>, Vec<Option<i64>>);
fn number(row: &[Option<i64>], column: usize) -> i64 {
    row.get(column).copied().flatten().unwrap_or(0)
}

// 元行番号・空欄・未収録列を保持する。注記は原本bytesにも残す。
fn rows(bytes: &[u8], columns: Option<usize>) -> Result<Vec<Row>> {
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
            let selected = cells
                .iter()
                .take(columns.unwrap_or(cells.len()))
                .cloned()
                .collect::<Vec<_>>()
                .join(",");
            let values = numeric_rows(selected.as_bytes())?
                .into_iter()
                .next()
                .context("数値行欠測")?
                .1;
            result.push((index + 1, cells, values));
        }
    }
    Ok(result)
}

pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &impl Fn(String),
) -> Result<()> {
    let paths: Vec<_> = dataset
        .files
        .keys()
        .filter_map(|path| {
            path.strip_prefix("Data/MapStageDataN_")?
                .strip_suffix(".csv")?
                .parse::<i64>()
                .ok()
                .map(|id| (id, path))
        })
        .collect();
    if paths.is_empty() {
        return Ok(());
    }
    let region = &dataset.current.header.source_region;
    let names: BTreeMap<i64, String> = csv_rows(&read_asset(
        source,
        dataset,
        connection,
        "res/Map_Name.csv",
    )?)?
    .into_iter()
    .map(|row| {
        Ok((
            row.first().context("マップID欠測")?.parse()?,
            row.get(1).context("マップ名欠測")?.clone(),
        ))
    })
    .collect::<Result<_>>()?;
    let stage_names = csv_rows(&read_asset(
        source,
        dataset,
        connection,
        "res/StageName_RN_ja.csv",
    )?)?;
    let options = rows(
        &read_asset(source, dataset, connection, "Data/Map_option.csv")?,
        Some(19),
    )?;
    let limits = rows(
        &read_asset(source, dataset, connection, "Data/Stage_option.csv")?,
        Some(9),
    )?;
    let difficulty_path = "Data/difficulty_level.tsv";
    let difficulties: BTreeMap<i64, Vec<Option<f64>>> =
        if dataset.files.contains_key(difficulty_path) {
            let bytes = read_asset(source, dataset, connection, difficulty_path)?;
            std::str::from_utf8(&bytes)?
                .trim_start_matches('\u{feff}')
                .lines()
                .filter_map(|line| {
                    let mut fields = line.split('\t');
                    Some((
                        fields.next()?.parse().ok()?,
                        fields.map(|value| value.parse().ok()).collect(),
                    ))
                })
                .collect()
        } else {
            BTreeMap::new()
        };
    let mut total = 0;
    for (id, path) in paths {
        ensure!((0..1000).contains(&id), "0番台の範囲外です: {path}");
        let metadata = rows(&read_asset(source, dataset, connection, path)?, None)?;
        ensure!(metadata.len() >= 2, "マップヘッダー欠測: {path}");
        let matching: Vec<_> = options
            .iter()
            .filter(|(_, _, values)| number(values, 0) == id)
            .collect();
        ensure!(matching.len() == 1, "マップ設定の欠測・重複: {id}");
        let (option_row, option_cells, option) = matching[0];
        let name = names
            .get(&id)
            .cloned()
            .unwrap_or_else(|| format!("マップ {id}"));
        connection.execute(
            "INSERT INTO stage_map VALUES (?,?,?,?,?,?,?)",
            params![
                region,
                id,
                name,
                path,
                serde_json::to_string(&[&metadata[0].1, &metadata[1].1])?,
                serde_json::to_string(option_cells)?,
                *option_row as i64,
            ],
        )?;
        let crowns = number(option, 1);
        ensure!((1..=4).contains(&crowns), "未対応の冠数: {id}/{crowns}");
        for crown in 0..crowns {
            let raw = number(option, 3 + crown as usize);
            let multiplier = if raw != 0 { raw } else { 100 + crown * 50 };
            connection.execute(
                "INSERT INTO stage_crown VALUES (?,?,?,?)",
                params![region, id, crown + 1, multiplier],
            )?;
        }
        for (position, (line, cells, values)) in limits
            .iter()
            .filter(|(_, _, values)| number(values, 0) == id)
            .enumerate()
        {
            connection.execute(
                "INSERT INTO stage_limit VALUES (?,?,?,?,?,?,?,?)",
                params![
                    region,
                    id,
                    position as i64,
                    number(values, 1),
                    number(values, 2),
                    number(values, 3),
                    *line as i64,
                    serde_json::to_string(cells)?
                ],
            )?;
        }
        for (index, (metadata_row, metadata_cells, reward)) in metadata.iter().skip(2).enumerate() {
            let source_path = format!("Data/stageRN{id:03}_{index:02}.csv");
            let definition = rows(
                &read_asset(source, dataset, connection, &source_path)?,
                None,
            )?;
            ensure!(
                definition.len() >= 3 && definition[0].2.len() >= 6 && definition[1].2.len() >= 6,
                "ステージヘッダー欠測: {source_path}"
            );
            let settings = &definition[0].2;
            let header = &definition[1].2;
            let name = stage_names
                .get(id as usize)
                .and_then(|row| row.get(index))
                .cloned()
                .unwrap_or_else(|| format!("ステージ {}", index + 1));
            let difficulty = difficulties
                .get(&id)
                .and_then(|row| row.get(index))
                .copied()
                .flatten();
            connection.execute(
                "INSERT INTO stage VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                params![
                    region,
                    id,
                    index as i64,
                    name,
                    number(reward, 0),
                    number(reward, 1),
                    number(header, 0),
                    number(header, 1),
                    number(header, 2),
                    number(header, 3),
                    number(header, 4),
                    number(header, 5),
                    number(header, 6),
                    number(header, 7),
                    number(header, 8),
                    number(settings, 1),
                    difficulty,
                    serde_json::to_string(&definition[0].1)?,
                    serde_json::to_string(&definition[1].1)?,
                    serde_json::to_string(metadata_cells)?,
                    source_path,
                    *metadata_row as i64
                ],
            )?;
            let mut terminated = false;
            for (position, (line, cells, values)) in definition.iter().skip(2).enumerate() {
                if number(values, 0) == 0 {
                    terminated = true;
                    break;
                }
                ensure!(number(values, 0) >= 2, "敵ID不正: {source_path}:{line}");
                let mut parameters: Vec<rusqlite::types::Value> = vec![
                    region.clone().into(),
                    id.into(),
                    (index as i64).into(),
                    (position as i64).into(),
                    (*line as i64).into(),
                    serde_json::to_string(cells)?.into(),
                ];
                parameters.extend((0..14).map(|column| number(values, column).into()));
                connection.execute(
                    "INSERT INTO stage_spawn VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    rusqlite::params_from_iter(parameters),
                )?;
            }
            ensure!(terminated, "出現行の終端欠測: {source_path}");
            for (position, column) in std::iter::once(5)
                .chain((9..reward.len().saturating_sub(3)).step_by(3))
                .enumerate()
            {
                if number(reward, column) <= 0
                    || number(reward, column + 1) < 0
                    || number(reward, column + 2) <= 0
                {
                    continue;
                }
                connection.execute(
                    "INSERT INTO stage_reward VALUES (?,?,?,?,?,?,?,?)",
                    params![
                        region,
                        id,
                        index as i64,
                        position as i64,
                        number(reward, column),
                        number(reward, column + 1),
                        number(reward, column + 2),
                        column as i64
                    ],
                )?;
            }
            total += 1;
        }
    }
    // 報酬画像も検証済み原本として保存し、オフラインで表示する。
    let mut statement =
        connection.prepare("SELECT DISTINCT item_id FROM stage_reward WHERE region=?")?;
    let rewards = statement
        .query_map([region], |row| row.get::<_, i64>(0))?
        .collect::<rusqlite::Result<Vec<_>>>()?;
    for id in rewards {
        let path = format!("Image/gatyaitemD_{id:02}_f.png");
        if dataset.files.contains_key(&path) {
            read_asset(source, dataset, connection, &path)?;
        }
    }
    crate::stage_materials::import(source, dataset, connection)?;
    progress(format!("0番台ステージ: {total}"));
    Ok(())
}

fn raw(text: String) -> Result<Value> {
    Ok(serde_json::from_str(&text)?)
}

pub fn catalog(database: &Database, region: &str) -> Result<Value> {
    let connection = &database.connection;
    let metadata = database.metadata()?;
    let mut maps = Vec::new();
    let mut stages = Vec::new();
    let mut statement=connection.prepare("SELECT id,name,source_path,raw_headers,options_raw,options_row FROM stage_map WHERE region=? ORDER BY id")?;
    let entries = statement.query_map([region], |row| {
        Ok((
            row.get::<_, i64>(0)?,
            row.get::<_, String>(1)?,
            row.get::<_, String>(2)?,
            row.get::<_, String>(3)?,
            row.get::<_, String>(4)?,
            row.get::<_, i64>(5)?,
        ))
    })?;
    for entry in entries {
        let (id, name, path, headers, options, option_row) = entry?;
        let key = format!("N{id:03}");
        let materials = crate::stage_materials::read(connection, region, id)?;
        let mut statement = connection.prepare(
            "SELECT multiplier FROM stage_crown WHERE region=? AND map_id=? ORDER BY crown",
        )?;
        let stars = statement
            .query_map(params![region, id], |row| row.get::<_, i64>(0))?
            .collect::<rusqlite::Result<Vec<_>>>()?;
        let mut statement=connection.prepare("SELECT crown,stage_index,rarity_mask,source_row,raw_cells FROM stage_limit WHERE region=? AND map_id=? ORDER BY position")?;
        let limits=statement.query_map(params![region,id],|row| Ok(json!({"crown":row.get::<_,i64>(0)?,"stage":row.get::<_,i64>(1)?,"rarities":row.get::<_,i64>(2)?,"sourceRow":row.get::<_,i64>(3)?,"raw":row.get::<_,String>(4)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
        let mut stage_ids = Vec::new();
        let mut statement=connection.prepare("SELECT stage_index,name,energy,xp_raw,width,castle_hp,spawn_min,spawn_max,background,max_enemies,castle_raw,time_raw,boss_guard,no_continue,difficulty,settings_raw,header_raw,rewards_raw,source_path,metadata_row FROM stage WHERE region=? AND map_id=? ORDER BY stage_index")?;
        let entries = statement.query_map(params![region, id], |row| {
            let numbers = (2..14)
                .map(|column| row.get::<_, i64>(column))
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
            let stage_id = format!("{key}-{index}");
            stage_ids.push(stage_id.clone());
            let mut statement=connection.prepare("SELECT source_row,raw_cells,enemy_raw,count,first_raw,interval_min_raw,interval_max_raw,castle,layer_min,layer_max,boss,hp_percent,score,attack_percent,after_castle,kills FROM stage_spawn WHERE region=? AND map_id=? AND stage_index=? ORDER BY position")?;
            let rows = statement.query_map(params![region, id, index], |row| {
                Ok((
                    row.get::<_, i64>(0)?,
                    row.get::<_, String>(1)?,
                    (2..16)
                        .map(|column| row.get::<_, i32>(column))
                        .collect::<rusqlite::Result<Vec<_>>>()?,
                ))
            })?;
            let mut spawns = Vec::new();
            let mut enemies = BTreeSet::new();
            let mut flags = BTreeSet::new();
            for row in rows {
                let (source_row, cells, v) = row?;
                let mut loaded = v.clone();
                for column in [2, 3, 4] {
                    loaded[column] = loaded[column]
                        .checked_mul(2)
                        .context("出現待機の整数上限")?;
                }
                let attack = if v[11] != 0 { v[11] } else { v[9] };
                if attack != v[9] {
                    flags.insert("splitMultiplier");
                }
                if v[12] != 0 {
                    flags.insert("afterCastle");
                }
                if v[13] != 0 {
                    flags.insert("kills");
                }
                enemies.insert(v[0] - 2);
                spawns.push(json!({"enemy":v[0]-2,"count":v[1],"first":loaded[2],"interval":[loaded[3],loaded[4]],"castle":v[5],"layers":[v[6],v[7]],"boss":v[8],"health":v[9],"attack":attack,"score":v[10],"afterCastle":v[12]!=0,"kills":v[13],"native":loaded,"raw":raw(cells)?,"sourceRow":source_row}));
            }
            let mut statement=connection.prepare("SELECT comparison,item_id,amount,source_column FROM stage_reward WHERE region=? AND map_id=? AND stage_index=? ORDER BY position")?;
            let drops=statement.query_map(params![region,id,index],|row|Ok(json!({"weight":row.get::<_,i64>(0)?,"chance":null,"id":row.get::<_,i64>(1)?,"count":row.get::<_,i64>(2)?,"sourceColumn":row.get::<_,i64>(3)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
            if !limits.is_empty() {
                flags.insert("restriction");
            }
            if n[11] == 1 {
                flags.insert("noContinue");
            }
            if n[10] == 1 {
                flags.insert("bossGuard");
            }
            if n[8] > 1 {
                flags.insert("enemyCastle");
            }
            if n[9] > 0 {
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
            stages.push(json!({"id":stage_id,"map":key,"index":index,"name":name,"energy":n[0],"xp":n[1],"width":n[2],"castleHealth":n[3],"spawnInterval":[n[4],n[5]],"background":n[6],"maxEnemies":n[7].min(50),"enemyCastle":if n[8]>1 {Some(n[8]-2)}else{None},"timeLimit":n[9]*1800,"bossGuard":n[10]==1,"noContinue":n[11]==1,"difficulty":difficulty,"spawns":spawns,"enemies":enemies,"flags":flags,"music":music,"rewards":drops.iter().map(|drop|drop["id"].clone()).collect::<Vec<_>>(),"drops":drops,"scoreRewards":[],"clearRewards":[],"rewardMode":number(&reward_numbers,8),"rewardOnce":reward_numbers.last().copied().flatten(),"source":text[3],"metadataRow":metadata_row,"rawSettings":raw(text[0].clone())?,"rawHeader":raw(text[1].clone())?,"rawRewards":reward_raw}));
        }
        maps.push(json!({"key":key,"series":"N","number":id,"nativeId":id,"name":name,"stars":stars,"limits":limits,"materials":materials,"stages":stage_ids,"rules":[],"conditions":[],"source":path,"rawHeaders":raw(headers)?,"rawOptions":raw(options)?,"optionsRow":option_row}));
    }
    for map in &maps {
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
    Ok(
        json!({"schemaVersion":1,"gameVersion":metadata.get("version"),"revision":metadata.get("revision"),"buildId":metadata.get("build_id"),"imageBase":"/api/asset/","scope":{"bands":[0],"nativeVersion":"15.7.2"},"series":[{"id":"N","label":"レジェンドストーリー"}],"maps":maps,"stages":stages,"rewards":rewards}),
    )
}
