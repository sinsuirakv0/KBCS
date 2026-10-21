use crate::{
    import::read_asset,
    model::{csv_rows, numeric_rows, plain_text, required},
    source::{Dataset, Source},
};
use anyhow::{Context, Result};
use rusqlite::{Connection, params};
use serde::Serialize;
use std::collections::BTreeMap;

const GROUPS: &[(&str, i64)] = &[
    ("N", 0),
    ("S", 1),
    ("C", 2),
    ("CH", 3),
    ("E", 4),
    ("RE", 4),
    ("T", 6),
    ("V", 7),
    ("R", 11),
    ("M", 12),
    ("NA", 13),
    ("B", 14),
    ("NB", 14),
    ("D", 16),
    ("A", 24),
    ("RA", 24),
    ("H", 25),
    ("CA", 27),
    ("DM", 30),
    ("Q", 31),
    ("PR", 39),
    ("L", 33),
    ("ND", 34),
    ("SR", 36),
    ("G", 37),
];

#[derive(Clone, Debug, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Stage {
    pub map: i64,
    pub stage: usize,
    pub series: String,
    pub map_name: String,
    pub stage_name: String,
    #[serde(skip)]
    source_path: String,
    #[serde(skip)]
    source_row: usize,
}

#[derive(Debug, Serialize)]
pub struct Material {
    pub id: i64,
    pub name: String,
    pub icon: Option<String>,
    pub count: i64,
}

#[derive(Debug, Serialize)]
pub struct Progression {
    pub form: usize,
    pub description: String,
    pub level: i64,
    pub xp: i64,
    pub materials: Vec<Material>,
    pub stages: Vec<Stage>,
}

fn load(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    path: &str,
) -> Result<Vec<u8>> {
    if dataset.files.contains_key(path) {
        read_asset(source, dataset, connection, path)
    } else {
        Ok(Vec::new())
    }
}

fn clean(text: &str) -> String {
    let text = plain_text(text);
    if matches!(text.as_str(), "@" | "＠") {
        String::new()
    } else {
        text
    }
}

fn add_stage(stages: &mut Vec<Stage>, entry: &Stage) {
    if !stages
        .iter()
        .any(|value| value.map == entry.map && value.stage == entry.stage)
    {
        stages.push(entry.clone());
    }
}

fn stage_rows(bytes: &[u8]) -> Result<Vec<(usize, Vec<Option<i64>>)>> {
    let mut rows = Vec::new();
    for (index, line) in std::str::from_utf8(bytes)?
        .trim_start_matches('\u{feff}')
        .lines()
        .enumerate()
    {
        let line = line
            .split_once("//")
            .map_or(line, |(value, _)| value)
            .trim();
        // 実データの末尾にある、CSVではないアイテム番号の説明だけを除外する。
        if line.is_empty() || (!line.contains(',') && line.parse::<i64>().is_err()) {
            continue;
        }
        for (_, row) in numeric_rows(line.as_bytes())? {
            rows.push((index + 1, row));
        }
    }
    Ok(rows)
}

pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &impl Fn(String),
) -> Result<()> {
    let region = &dataset.current.header.source_region;
    let book = csv_rows(&load(
        source,
        dataset,
        connection,
        "res/nyankoPictureBook_ja.csv",
    )?)?;
    let items = csv_rows(&load(source, dataset, connection, "res/GatyaitemName.csv")?)?;
    let maps: BTreeMap<i64, String> =
        csv_rows(&load(source, dataset, connection, "res/Map_Name.csv")?)?
            .into_iter()
            .map(|row| {
                Ok((
                    row[0].parse()?,
                    row.get(1).cloned().context("マップ名がありません")?,
                ))
            })
            .collect::<Result<_>>()?;
    let mut names = BTreeMap::new();
    let mut rewards: BTreeMap<i64, Vec<Stage>> = BTreeMap::new();
    let mut count = 0;
    for path in dataset.files.keys() {
        let Some((group, map)) = path
            .strip_prefix("Data/MapStageData")
            .and_then(|rest| rest.strip_suffix(".csv"))
            .and_then(|rest| rest.rsplit_once('_'))
        else {
            continue;
        };
        let Some((_, group_id)) = GROUPS.iter().find(|(key, _)| *key == group) else {
            continue;
        };
        let map: usize = map.parse()?;
        let map_id = group_id * 1000 + map as i64;
        let names_path = format!(
            "res/StageName_{}_ja.csv",
            if ["RE", "DM", "L", "G"].contains(&group) {
                group.into()
            } else {
                format!("R{group}")
            }
        );
        if !names.contains_key(&names_path) {
            names.insert(
                names_path.clone(),
                csv_rows(&load(source, dataset, connection, &names_path)?)?,
            );
        }
        for (stage, (source_row, row)) in
            stage_rows(&read_asset(source, dataset, connection, path)?)?
                .into_iter()
                .skip(2)
                .enumerate()
        {
            if row.len() > 15 && row[8..15].iter().all(|value| *value == Some(-2)) {
                continue;
            }
            let number = |column| row.get(column).copied().flatten().unwrap_or(0);
            let entry = Stage {
                map: map_id,
                stage,
                series: match group {
                    "N" => "レジェンドストーリー",
                    "NA" => "真レジェンドストーリー",
                    "ND" => "ゼロレジェンドストーリー",
                    _ => "",
                }
                .into(),
                map_name: maps
                    .get(&map_id)
                    .cloned()
                    .unwrap_or_else(|| format!("マップ {map_id}")),
                stage_name: names[&names_path]
                    .get(map)
                    .and_then(|row| row.get(stage))
                    .map(|text| clean(text))
                    .filter(|name| !name.is_empty())
                    .unwrap_or_else(|| format!("ステージ {}", stage + 1)),
                source_path: path.clone(),
                source_row,
            };
            // 追加報酬と通常報酬だけを扱い、時刻報酬を通常ドロップへ混ぜない。
            for column in std::iter::once(5).chain((9..row.len().saturating_sub(3)).step_by(3)) {
                let id = number(column + 1);
                if number(column) > 0 && id > 0 && number(column + 2) > 0 {
                    add_stage(rewards.entry(id).or_default(), &entry);
                }
            }
        }
        count += 1;
        if count % 100 == 0 {
            progress(format!("入手・進化ステージ: {count}"));
        }
    }
    let drop_bytes = load(source, dataset, connection, "Data/drop_chara.csv")?;
    let drop_text = std::str::from_utf8(&drop_bytes)?;
    let mut drops: BTreeMap<i64, Vec<Stage>> = BTreeMap::new();
    for (_, row) in numeric_rows(
        drop_text
            .split_once('\n')
            .map_or("", |(_, body)| body)
            .as_bytes(),
    )? {
        if required(&row, 0)? < 0 {
            continue;
        }
        if let Some(stages) = rewards.get(&required(&row, 0)?) {
            for stage in stages {
                add_stage(drops.entry(required(&row, 2)?).or_default(), stage);
            }
        }
    }
    let buy = numeric_rows(&read_asset(
        source,
        dataset,
        connection,
        "Data/unitbuy.csv",
    )?)?;
    for unit in &dataset.characters {
        let id: usize = unit.id.parse()?;
        let settings = &buy.get(id).context("unitbuyにIDなし")?.1;
        for form in 0..unit.forms.len() {
            let description = book
                .get(id)
                .map(|row| {
                    row.iter()
                        .skip(form * 3)
                        .take(3)
                        .map(|text| clean(text))
                        .filter(|text| !text.is_empty())
                        .collect::<Vec<_>>()
                        .join("\n")
                })
                .unwrap_or_default();
            let level = match form {
                0 => 0,
                1 => required(settings, 21)?.max(0),
                2 => required(settings, 25)?.max(required(settings, 20)?).max(0),
                _ => required(settings, 26)?.max(0),
            };
            let xp = if form < 2 {
                0
            } else {
                required(settings, if form == 2 { 27 } else { 38 })?
            };
            connection.execute(
                "INSERT INTO progression VALUES (?,?,?,?,?,?)",
                params![region, id as i64, form as i64, description, level, xp],
            )?;
            let stages = match form {
                0 => drops.get(&(id as i64)),
                2 => rewards.get(&required(settings, 23)?),
                _ => None,
            };
            for (position, stage) in stages.into_iter().flatten().enumerate() {
                connection.execute(
                    "INSERT INTO progression_stage VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    params![
                        region,
                        id as i64,
                        form as i64,
                        position as i64,
                        stage.map,
                        stage.stage as i64,
                        stage.series,
                        stage.map_name,
                        stage.stage_name,
                        stage.source_path,
                        stage.source_row as i64
                    ],
                )?;
            }
            if form < 2 {
                continue;
            }
            for slot in 0..5 {
                let column = (if form == 2 { 28 } else { 39 }) + slot * 2;
                let count = required(settings, column + 1)?;
                if count <= 0 {
                    continue;
                }
                let item = required(settings, column)?;
                let name = items
                    .get(item as usize)
                    .and_then(|row| row.first())
                    .filter(|name| !name.is_empty())
                    .cloned()
                    .unwrap_or_else(|| format!("アイテム {item}"));
                let icon = format!("Image/gatyaitemD_{item:02}_f.png");
                let icon = if dataset.files.contains_key(&icon) {
                    let retained: bool = connection.query_row(
                        "SELECT EXISTS(SELECT 1 FROM source_file WHERE path=?)",
                        [&icon],
                        |row| row.get(0),
                    )?;
                    if !retained {
                        read_asset(source, dataset, connection, &icon)?;
                    }
                    Some(icon)
                } else {
                    None
                };
                connection.execute(
                    "INSERT OR IGNORE INTO material VALUES (?,?,?,?)",
                    params![region, item, name, icon],
                )?;
                connection.execute(
                    "INSERT INTO evolution_material VALUES (?,?,?,?,?,?,?)",
                    params![
                        region,
                        id as i64,
                        form as i64,
                        slot as i64,
                        item,
                        count,
                        column as i64
                    ],
                )?;
            }
        }
    }
    Ok(())
}

pub fn read(connection: &Connection, region: &str, id: u32) -> Result<Vec<Progression>> {
    let mut statement = connection.prepare("SELECT form_index,description,level,xp FROM progression WHERE region=? AND unit_id=? ORDER BY form_index")?;
    let mut rows = statement.query(params![region, id])?;
    let mut result = Vec::new();
    while let Some(row) = rows.next()? {
        let form: u32 = row.get(0)?;
        let materials = connection.prepare("SELECT m.id,m.name,m.icon_path,e.count FROM evolution_material e JOIN material m ON m.region=e.region AND m.id=e.material_id WHERE e.region=? AND e.unit_id=? AND e.form_index=? ORDER BY e.position")?
            .query_map(params![region,id,form],|row|Ok(Material{id:row.get(0)?,name:row.get(1)?,icon:row.get(2)?,count:row.get(3)?}))?.collect::<rusqlite::Result<_>>()?;
        let stages = connection.prepare("SELECT map_id,stage_index,series,map_name,stage_name,source_path,source_row FROM progression_stage WHERE region=? AND unit_id=? AND form_index=? ORDER BY position")?
            .query_map(params![region,id,form],|row|Ok(Stage{map:row.get(0)?,stage:row.get::<_,u32>(1)? as usize,series:row.get(2)?,map_name:row.get(3)?,stage_name:row.get(4)?,source_path:row.get(5)?,source_row:row.get::<_,u32>(6)? as usize}))?.collect::<rusqlite::Result<_>>()?;
        result.push(Progression {
            form: form as usize,
            description: row.get(1)?,
            level: row.get(2)?,
            xp: row.get(3)?,
            materials,
            stages,
        });
    }
    Ok(result)
}
