use super::{Row, number, rows};
use crate::{
    import::read_asset,
    model::{csv_rows, plain_text},
    source::{Dataset, Source},
};
use anyhow::{Result, ensure};
use rusqlite::{Connection, params};
use std::collections::{BTreeMap, BTreeSet};

// 現版の分類・ファイル選択と照合した系列。表示IDと元ファイル系列を分ける。
pub(super) const SERIES: &[(&str, &str, i64, i64, &str, &str)] = &[
    ("N", "レジェンドストーリー", 0, 0, "RN", "N"),
    ("S", "イベント", 1000, 1, "RS", "S"),
    ("C", "コラボ", 2000, 2, "RC", "C"),
    ("EX", "EX", 4000, -8, "EX", "RE"),
    ("T", "道場", 6000, 3, "RT", "T"),
    ("V", "塔", 7000, -4, "RV", "V"),
    ("R", "ランキング道場", 11000, 4, "RR", "R"),
    ("M", "その他", 12000, -6, "RM", "M"),
    ("NA", "真レジェンドストーリー", 13000, -9, "RNA", "NA"),
    ("B", "ネコビタン", 14000, -10, "RB", "B"),
    ("D", "レジェンドクエスト", 16000, -11, "RD", "D"),
    ("A", "強襲", 24000, -16, "RA", "A"),
    ("H", "地図", 25000, -17, "RH", "H"),
    ("CA", "コラボ強襲", 27000, -18, "RCA", "CA"),
    ("DM", "魔界編", 30000, -19, "DM", "DM"),
    ("Q", "超獣討伐", 31000, -20, "RQ", "Q"),
    ("L", "地底迷宮", 33000, -21, "L", "L"),
    ("ND", "レジェンドストーリー0", 34000, -22, "RND", "ND"),
    ("SR", "スペシャルルール", 36000, -23, "RSR", "SR"),
    ("G", "にゃんこ道検定", 37000, -24, "G", "G"),
    ("PR", "イベントPt", 39000, -26, "RPR", "PR"),
];

#[derive(Clone)]
struct Plan {
    id: i64,
    series: String,
    index: i64,
    kind: i64,
    mode: i64,
    metadata: String,
    names: String,
    prefix: String,
    chapter: bool,
}
struct Definition {
    rows: Vec<Row>,
    skip: usize,
}

fn chapter_order(stage: usize) -> usize {
    if stage < 46 {
        45 - stage
    } else {
        [46, 47, 45, 47, 47, 45, 45]
            .get(stage - 46)
            .copied()
            .unwrap_or(stage)
    }
}
fn definition_header_count(path: &str) -> Option<usize> {
    let stem = path.strip_prefix("Data/stage")?.strip_suffix(".csv")?;
    if stem.parse::<usize>().is_ok() {
        return Some(1);
    }
    if let Some(rest) = stem.strip_prefix('W')
        && let Some((a, b)) = rest.split_once('_')
        && a.parse::<usize>().is_ok()
        && b.parse::<usize>().is_ok()
    {
        return Some(1);
    }
    if let Some(rest) = stem.strip_prefix("Space") {
        let parts = rest.split('_').collect::<Vec<_>>();
        if parts.first()?.parse::<usize>().is_ok() && parts.last()?.parse::<usize>().is_ok() {
            return Some(if parts.len() == 2 { 1 } else { 2 });
        }
    }
    let (prefix_index, stage) = stem.rsplit_once('_')?;
    if stage.parse::<usize>().is_err() {
        return None;
    }
    let start = prefix_index.find(|c: char| c.is_ascii_digit())?;
    let prefix = &prefix_index[..start];
    if prefix_index[start..].parse::<usize>().is_ok()
        && (prefix == "Z" || SERIES.iter().any(|s| s.4 == prefix))
    {
        Some(2)
    } else {
        None
    }
}
fn target(plan: &Plan, stage: usize) -> Option<String> {
    if plan.series == "D" || plan.series == "L" {
        return None;
    }
    Some(if plan.chapter {
        match plan.series.as_str() {
            "EOC" => format!("Data/stage{stage:02}.csv"),
            "ITF" => format!("Data/stageW{:02}_{stage:02}.csv", plan.mode),
            "COTC" => format!("Data/stageSpace{:02}_{stage:02}.csv", plan.mode),
            "EOCZ" | "ITFZ" | "COTCZ" => format!("Data/stageZ{:02}_{stage:02}.csv", plan.mode),
            _ => format!(
                "Data/stageSpace09_Invasion{}_00.csv",
                if plan.kind == -25 { "_Z" } else { "" }
            ),
        }
    } else {
        format!("Data/stage{}{:03}_{stage:02}.csv", plan.prefix, plan.index)
    })
}

pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &(impl Fn(String) + Sync),
) -> Result<()> {
    if !dataset
        .files
        .keys()
        .any(|p| p.starts_with("Data/MapStageData"))
    {
        return Ok(());
    }
    let region = &dataset.current.header.source_region;
    let load = |path: &str| read_asset(source, dataset, connection, path);
    source.prefetch(
        dataset,
        &dataset
            .files
            .keys()
            .filter(|path| definition_header_count(path).is_some())
            .cloned()
            .collect::<Vec<_>>(),
        progress,
    )?;
    let mut definitions = BTreeMap::new();
    for path in dataset.files.keys() {
        let Some(skip) = definition_header_count(path) else {
            continue;
        };
        let definition = rows(&load(path)?, None)?;
        ensure!(
            definition.len() >= skip && definition[skip - 1].2.len() >= 6,
            "ステージヘッダー欠測: {path}"
        );
        let header = &definition[skip - 1].2;
        let settings = if skip == 2 {
            Some(&definition[0].1)
        } else {
            None
        };
        let terminated = definition.iter().skip(skip).any(|r| number(&r.2, 0) == 0);
        connection.execute(
            "INSERT INTO stage_definition VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            params![
                region,
                path,
                serde_json::to_string(&settings.cloned().unwrap_or_default())?,
                serde_json::to_string(&definition[skip - 1].1)?,
                skip as i64,
                i64::from(terminated),
                number(header, 0),
                number(header, 1),
                number(header, 2),
                number(header, 3),
                number(header, 4),
                number(header, 5),
                number(header, 6),
                number(header, 7),
                number(header, 8),
                if skip == 2 {
                    number(&definition[0].2, 1)
                } else {
                    0
                }
            ],
        )?;
        for (position, (line, cells, v)) in definition.iter().skip(skip).enumerate() {
            if number(v, 0) == 0 {
                break;
            }
            ensure!(number(v, 0) >= 2, "敵ID不正: {path}:{line}");
            let mut parameters: Vec<rusqlite::types::Value> = vec![
                region.clone().into(),
                path.clone().into(),
                (position as i64).into(),
                (*line as i64).into(),
                serde_json::to_string(cells)?.into(),
            ];
            parameters.extend((0..14).map(|c| number(v, c).into()));
            connection.execute(
                "INSERT INTO stage_definition_spawn VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                rusqlite::params_from_iter(parameters),
            )?;
        }
        definitions.insert(
            path.clone(),
            Definition {
                rows: definition,
                skip,
            },
        );
    }
    progress(format!("戦闘定義: {}件", definitions.len()));
    let names: BTreeMap<i64, String> = csv_rows(&load("res/Map_Name.csv")?)?
        .into_iter()
        .filter_map(|r| Some((r.first()?.parse().ok()?, plain_text(r.get(1)?))))
        .collect();
    let options = rows(&load("Data/Map_option.csv")?, Some(19))?;
    let limits = rows(&load("Data/Stage_option.csv")?, Some(9))?;
    let difficulties: BTreeMap<i64, Vec<Option<f64>>> =
        if dataset.files.contains_key("Data/difficulty_level.tsv") {
            String::from_utf8(load("Data/difficulty_level.tsv")?)?
                .trim_start_matches('\u{feff}')
                .lines()
                .filter_map(|line| {
                    let mut f = line.split('\t');
                    Some((f.next()?.parse().ok()?, f.map(|v| v.parse().ok()).collect()))
                })
                .collect()
        } else {
            BTreeMap::new()
        };
    let mut plans = Vec::new();
    for path in dataset.files.keys() {
        let Some(stem) = path
            .strip_prefix("Data/MapStageData")
            .and_then(|p| p.strip_suffix(".csv"))
        else {
            continue;
        };
        let Some((label, index)) = stem.rsplit_once('_') else {
            continue;
        };
        let Some(s) = SERIES.iter().find(|s| s.5 == label) else {
            continue;
        };
        let index: i64 = index.parse()?;
        plans.push(Plan {
            id: s.2 + index,
            series: s.0.into(),
            index,
            kind: s.3,
            mode: if s.0 == "EX" { 99 } else { 3 },
            metadata: path.clone(),
            names: format!(
                "res/StageName_{}_ja.csv",
                if s.0 == "EX" { "RE" } else { s.4 }
            ),
            prefix: s.4.into(),
            chapter: false,
        });
    }
    for (series, base, kind, offset, story) in [
        ("EOC", 3000, -2, 0, 0),
        ("ITF", 3003, -3, 4, 1),
        ("COTC", 3006, -7, 7, 2),
        ("EOCZ", 20000, -12, 0, 0),
        ("ITFZ", 21000, -13, 4, 1),
        ("COTCZ", 22000, -14, 7, 2),
    ] {
        for chapter in 0..3 {
            let metadata = if series == "EOC" {
                "Data/stageNormal0.csv".into()
            } else {
                format!(
                    "Data/stageNormal{story}_{chapter}{}.csv",
                    if kind <= -12 { "_Z" } else { "" }
                )
            };
            if dataset.files.contains_key(&metadata) {
                plans.push(Plan {
                    id: base + chapter,
                    series: series.into(),
                    index: chapter,
                    kind,
                    mode: offset + chapter,
                    metadata,
                    names: format!("res/StageName{story}_ja.csv"),
                    prefix: String::new(),
                    chapter: true,
                });
            }
        }
    }
    for (series, id, kind, suffix) in [("COTCI", 23000, -15, ""), ("COTCZI", 38000, -25, "_Z")] {
        let metadata = format!("Data/stageNormal2_2_Invasion{suffix}.csv");
        if dataset.files.contains_key(&metadata) {
            plans.push(Plan {
                id,
                series: series.into(),
                index: 0,
                kind,
                mode: 9,
                metadata,
                names: "res/StageName2_ja.csv".into(),
                prefix: String::new(),
                chapter: true,
            });
        }
    }
    plans.sort_by_key(|p| p.id);
    let mut total = 0;
    for plan in &plans {
        let mut metadata = rows(&load(&plan.metadata)?, None)?;
        if let Some(end) = metadata
            .iter()
            .enumerate()
            .skip(2)
            .find_map(|(i, r)| (number(&r.2, 0) < 0 && r.2.len() < 5).then_some(i))
        {
            metadata.truncate(end);
        }
        ensure!(metadata.len() >= 2, "マップヘッダー欠測: {}", plan.metadata);
        let option = options.iter().find(|r| number(&r.2, 0) == plan.id);
        let headers = &metadata[0].2;
        let acquisition = headers
            .get(1)
            .copied()
            .flatten()
            .filter(|v| (0..400).contains(v));
        let score = headers
            .get(2)
            .copied()
            .flatten()
            .filter(|v| (0..200).contains(v));
        let fallback = super::series_label(&plan.series);
        let name = names
            .get(&plan.id)
            .cloned()
            .unwrap_or_else(|| format!("{fallback} {}", plan.index + 1));
        connection.execute(
            "INSERT INTO stage_map VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            params![
                region,
                plan.id,
                name,
                plan.metadata,
                serde_json::to_string(&[&metadata[0].1, &metadata[1].1])?,
                serde_json::to_string(&option.map(|r| r.1.clone()).unwrap_or_default())?,
                option.map(|r| r.0 as i64).unwrap_or(0),
                plan.series,
                plan.kind,
                plan.index,
                acquisition,
                score,
                plan.mode
            ],
        )?;
        let crowns = option.map(|r| number(&r.2, 1).max(1)).unwrap_or(1);
        ensure!(crowns <= 4, "冠数未対応: {}/{crowns}", plan.id);
        for crown in 0..crowns {
            let value = option
                .map(|r| number(&r.2, 3 + crown as usize))
                .unwrap_or(100);
            connection.execute(
                "INSERT INTO stage_crown VALUES (?,?,?,?)",
                params![
                    region,
                    plan.id,
                    crown + 1,
                    if value == 0 { 100 + crown * 50 } else { value }
                ],
            )?;
        }
        for (position, (line, cells, v)) in limits
            .iter()
            .filter(|r| number(&r.2, 0) == plan.id)
            .enumerate()
        {
            connection.execute(
                "INSERT INTO stage_limit VALUES (?,?,?,?,?,?,?,?)",
                params![
                    region,
                    plan.id,
                    position as i64,
                    number(v, 1),
                    number(v, 2),
                    number(v, 3),
                    *line as i64,
                    serde_json::to_string(cells)?
                ],
            )?;
        }
        let stage_names = if dataset.files.contains_key(&plan.names) {
            csv_rows(&load(&plan.names)?)?
        } else {
            Vec::new()
        };
        let mut indices: BTreeSet<usize> = (0..metadata.len() - 2).collect();
        if !["D", "L"].contains(&plan.series.as_str()) {
            for stage in 0..if matches!(plan.kind, -15 | -25) {
                1
            } else {
                1000
            } {
                if target(plan, stage).is_some_and(|p| definitions.contains_key(&p)) {
                    indices.insert(stage);
                }
            }
        }
        for index in indices {
            let reward = metadata.get(index + 2);
            let path = target(plan, index).filter(|p| definitions.contains_key(p));
            let definition = path.as_ref().and_then(|p| definitions.get(p));
            let header = definition.map(|d| &d.rows[d.skip - 1].2);
            let settings = definition
                .filter(|d| d.skip == 2)
                .map(|d| &d.rows[0].1)
                .cloned()
                .unwrap_or_default();
            let stage_name = if plan.kind == -15 {
                Some("フィリバスター襲来".into())
            } else if plan.kind == -25 {
                Some("ゾンビフィリバスター襲来".into())
            } else if plan.chapter {
                stage_names
                    .get(chapter_order(index))
                    .and_then(|r| r.first())
                    .cloned()
            } else {
                stage_names
                    .get(plan.index as usize)
                    .and_then(|r| r.get(index))
                    .cloned()
            }
            .filter(|s| !s.trim().is_empty() && !matches!(s.as_str(), "@" | "＠"))
            .unwrap_or_else(|| format!("ステージ {}", index + 1));
            let reward_cells = reward.map(|r| r.1.clone()).unwrap_or_default();
            let energy = reward.and_then(|r| r.2.first().copied().flatten());
            let xp = reward.and_then(|r| r.2.get(1).copied().flatten());
            let value = |c| header.map(|r| number(r, c));
            let no_continue = definition.map(|d| {
                if d.skip == 2 {
                    number(&d.rows[0].2, 1)
                } else {
                    0
                }
            });
            let source_path = path.as_ref().unwrap_or(&plan.metadata);
            connection.execute(
                "INSERT INTO stage VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                params![
                    region,
                    plan.id,
                    index as i64,
                    plain_text(&stage_name),
                    energy,
                    xp,
                    value(0),
                    value(1),
                    value(2),
                    value(3),
                    value(4),
                    value(5),
                    value(6),
                    value(7),
                    value(8),
                    no_continue,
                    difficulties
                        .get(&plan.id)
                        .and_then(|r| r.get(index))
                        .copied()
                        .flatten(),
                    serde_json::to_string(&settings)?,
                    serde_json::to_string(
                        &definition
                            .map(|d| d.rows[d.skip - 1].1.clone())
                            .unwrap_or_default()
                    )?,
                    serde_json::to_string(&reward_cells)?,
                    source_path,
                    reward.map(|r| r.0 as i64).unwrap_or(0)
                ],
            )?;
            connection.execute(
                "INSERT INTO stage_entry VALUES (?,?,?,?,?,?)",
                params![
                    region,
                    plan.id,
                    index as i64,
                    path,
                    i64::from(reward.is_some()),
                    plan.metadata
                ],
            )?;
            if let Some(reward) = reward {
                import_rewards(
                    connection,
                    region,
                    plan.id,
                    index as i64,
                    &reward.2,
                    score.is_some() || (4..=6).contains(&plan.mode),
                    &plan.metadata,
                )?;
            }
            total += 1;
        }
    }
    for path in super::rewards::SOURCES {
        if dataset.files.contains_key(*path) {
            load(path)?;
        }
    }
    super::extras::import(source, dataset, connection)?;
    let mut statement =
        connection.prepare("SELECT DISTINCT item_id FROM stage_reward WHERE region=?")?;
    for id in statement.query_map([region], |r| r.get::<_, i64>(0))? {
        let path = format!("Image/gatyaitemD_{:02}_f.png", id?);
        if dataset.files.contains_key(&path) {
            load(&path)?;
        }
    }
    crate::stage_materials::import(source, dataset, connection)?;
    progress(format!(
        "ステージ: {}マップ / {total}面 / {}戦闘定義",
        plans.len(),
        definitions.len()
    ));
    Ok(())
}

fn import_rewards(
    connection: &Connection,
    region: &str,
    map: i64,
    stage: i64,
    cells: &[Option<i64>],
    score_enabled: bool,
    source_path: &str,
) -> Result<()> {
    let mode = cells.get(8).copied().flatten().unwrap_or(0);
    let columns = if matches!(mode, -3 | -4) {
        std::iter::once(5)
            .chain((9..39).step_by(3))
            .take_while(|&c| cells.get(c).copied().flatten().is_some_and(|v| v >= 0))
            .collect::<Vec<_>>()
    } else {
        let count = if mode < 0 || cells.get(9).copied().flatten().unwrap_or(-1) < 0 {
            1
        } else if cells.get(12).copied().flatten().unwrap_or(-1) < 0 {
            2
        } else {
            3
        };
        [5, 9, 12][..count].to_vec()
    };
    let mut position = 0;
    let mut insert = |column: usize, kind: &str| -> Result<()> {
        if let (Some(comparison), Some(id), Some(amount)) = (
            cells.get(column).copied().flatten(),
            cells.get(column + 1).copied().flatten(),
            cells.get(column + 2).copied().flatten(),
        ) && comparison >= 0
            && id >= 0
            && amount > 0
        {
            connection.execute(
                "INSERT INTO stage_reward VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                params![
                    region,
                    map,
                    stage,
                    position,
                    comparison,
                    id,
                    amount,
                    column as i64,
                    kind,
                    source_path,
                    format!("stage/{stage}/column/{column}")
                ],
            )?;
            position += 1;
        }
        Ok(())
    };
    for column in columns {
        insert(
            column,
            if matches!(mode, -3 | -4) {
                "weight"
            } else {
                "normal"
            },
        )?;
    }
    if score_enabled && number(cells, 15) == 1 {
        for column in (16..46).step_by(3) {
            if cells.get(column).copied().flatten().unwrap_or(-1) < 0 {
                break;
            }
            insert(column, "score")?;
        }
    }
    Ok(())
}
