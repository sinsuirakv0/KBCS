use crate::model::plain_text;
use crate::model::{numeric_rows, required};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use std::{collections::BTreeMap, sync::OnceLock};

const ACQUISITION: &str = "Data/SkillAcquisition.csv";
const COSTS: &str = "Data/SkillLevel.csv";
const DESCRIPTIONS: &str = "res/SkillDescriptions.csv";
const TARGETS: [&str; 12] = [
    "red", "floating", "black", "metal", "angel", "alien", "zombie", "relic", "white", "eva",
    "witch", "aku",
];

#[derive(Clone, Debug, Deserialize, Serialize)]
pub struct Effect {
    pub kind: String,
    pub key: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub label: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub fields: Option<Vec<String>>,
}

#[derive(Deserialize)]
struct Definition {
    name: Option<String>,
    effect: Effect,
}

#[derive(Debug, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Talent {
    pub id: i64,
    pub index: usize,
    pub name: String,
    pub max_level: usize,
    pub description: String,
    pub limit: i64,
    pub costs: Vec<i64>,
    pub effect: Effect,
    pub values: Vec<[i64; 4]>,
    pub targets: Vec<String>,
}

fn definitions() -> &'static BTreeMap<String, Definition> {
    static DEFINITIONS: OnceLock<BTreeMap<String, Definition>> = OnceLock::new();
    DEFINITIONS.get_or_init(|| {
        serde_json::from_str(include_str!("../resources/talent-effects.json"))
            .expect("組込みの本能定義が不正です")
    })
}

fn source(connection: &Connection, path: &str) -> Result<Option<Vec<u8>>> {
    Ok(connection
        .query_row(
            "SELECT bytes FROM source_file WHERE path=?",
            [path],
            |row| row.get(0),
        )
        .optional()?)
}

fn without_header(bytes: &[u8]) -> Result<&[u8]> {
    let text = std::str::from_utf8(bytes)?.trim_start_matches('\u{feff}');
    Ok(text
        .split_once('\n')
        .context("本能CSVのヘッダーがありません")?
        .1
        .as_bytes())
}

pub(crate) fn import(connection: &Connection, region: &str) -> Result<()> {
    let Some(acquisition) = source(connection, ACQUISITION)? else {
        return Ok(());
    };
    let costs = source(connection, COSTS)?.context("本能NP費用の原本がありません")?;
    let descriptions = source(connection, DESCRIPTIONS)?.context("本能説明の原本がありません")?;
    let costs: BTreeMap<i64, Vec<Option<i64>>> = numeric_rows(without_header(&costs)?)?
        .into_iter()
        .map(|(_, row)| Ok((required(&row, 0)?, row[1..].to_vec())))
        .collect::<Result<_>>()?;
    let mut reader = csv::ReaderBuilder::new()
        .flexible(true)
        .from_reader(descriptions.as_slice());
    let descriptions: BTreeMap<i64, String> = reader
        .records()
        .map(|record| {
            let record = record?;
            Ok((
                record.get(0).context("本能説明IDがありません")?.parse()?,
                plain_text(record.get(1).context("本能説明がありません")?),
            ))
        })
        .collect::<Result<_>>()?;
    for (position, (_, row)) in numeric_rows(without_header(&acquisition)?)?
        .into_iter()
        .enumerate()
    {
        let unit_id = required(&row, 0)?;
        ensure!(
            row.len() >= 2 && (row.len() - 2) % 14 == 0,
            "本能CSVの列数が不正です: {unit_id}"
        );
        let mut index: i64 = connection.query_row(
            "SELECT count(*) FROM talent WHERE region=? AND unit_id=?",
            params![region, unit_id],
            |row| row.get(0),
        )?;
        for column in (2..row.len()).step_by(14) {
            let id = required(&row, column)?;
            if id <= 0 {
                continue;
            }
            ensure!(
                definitions().contains_key(&id.to_string()),
                "未対応の本能ID: {id}"
            );
            let max_level = required(&row, column + 1)?.max(1);
            let costs = costs
                .get(&required(&row, column + 11)?)
                .context("本能NP費用IDが未収録です")?;
            ensure!(
                max_level <= costs.len() as i64,
                "本能NP費用のレベルが不足しています"
            );
            let description = descriptions
                .get(&required(&row, column + 10)?)
                .cloned()
                .unwrap_or_default();
            connection.execute(
                "INSERT INTO talent VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                params![
                    region,
                    unit_id,
                    index,
                    id,
                    max_level,
                    description,
                    required(&row, column + 13)?,
                    required(&row, 1)?,
                    required(&row, column + 12)? > 0,
                    ACQUISITION,
                    position as i64 + 2,
                    column as i64
                ],
            )?;
            for level in 1..=max_level {
                let mut values = [0i64; 4];
                for (field, value) in values.iter_mut().enumerate() {
                    let first = required(&row, column + 2 + field * 2)?;
                    let last = required(&row, column + 3 + field * 2)?;
                    // Webと同じく差分の補間をゼロ方向へ整数化する。
                    *value = if max_level == 1 {
                        last
                    } else {
                        first + (last - first) * (level - 1) / (max_level - 1)
                    };
                }
                let np = costs[level as usize - 1].context("本能NP費用が空欄です")?;
                ensure!(np > 0, "本能NP費用が不正です");
                connection.execute(
                    "INSERT INTO talent_level VALUES (?,?,?,?,?,?,?,?,?)",
                    params![
                        region, unit_id, index, level, np, values[0], values[1], values[2],
                        values[3]
                    ],
                )?;
            }
            index += 1;
        }
    }
    Ok(())
}

pub fn read(connection: &Connection, region: &str, unit_id: u32) -> Result<Vec<Talent>> {
    let mut statement = connection.prepare("SELECT talent_index,skill_id,max_level,description,level_limit,target_mask,add_targets FROM talent WHERE region=? AND unit_id=? ORDER BY talent_index")?;
    let mut rows = statement.query(params![region, unit_id])?;
    let mut result = Vec::new();
    while let Some(row) = rows.next()? {
        let index = row.get::<_, u32>(0)? as usize;
        let id: i64 = row.get(1)?;
        let definition = definitions()
            .get(&id.to_string())
            .context("本能定義が未収録です")?;
        let description: String = row.get(3)?;
        let name = definition
            .name
            .clone()
            .or_else(|| {
                description
                    .split_once('「')
                    .and_then(|(_, rest)| rest.split_once('」'))
                    .map(|(name, _)| name.to_owned())
            })
            .or_else(|| {
                description
                    .lines()
                    .next()
                    .filter(|line| !line.is_empty())
                    .map(str::to_owned)
            })
            .unwrap_or_else(|| format!("本能ID{id}"));
        let mask: i64 = row.get(5)?;
        let enabled: bool = row.get(6)?;
        let steps: Vec<(i64, [i64; 4])> = connection.prepare("SELECT np,value0,value1,value2,value3 FROM talent_level WHERE region=? AND unit_id=? AND talent_index=? ORDER BY level")?
            .query_map(params![region, unit_id, index as i64], |row| Ok((row.get(0)?, [row.get(1)?, row.get(2)?, row.get(3)?, row.get(4)?])))?
            .collect::<rusqlite::Result<_>>()?;
        result.push(Talent {
            id,
            index,
            name,
            max_level: row.get::<_, u32>(2)? as usize,
            description,
            limit: row.get(4)?,
            costs: steps.iter().map(|(np, _)| *np).collect(),
            effect: definition.effect.clone(),
            values: steps.into_iter().map(|(_, values)| values).collect(),
            targets: TARGETS
                .iter()
                .enumerate()
                .filter(|(bit, _)| enabled && mask & (1 << bit) != 0)
                .map(|(_, key)| (*key).into())
                .collect(),
        });
    }
    Ok(result)
}
