use crate::{
    equipment::TARGETS,
    model::{numeric_rows, plain_text, required},
    support::Support,
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use std::{collections::BTreeMap, sync::OnceLock};

const ACQUISITION: &str = "Data/SkillAcquisition.csv";
const COSTS: &str = "Data/SkillLevel.csv";
const DESCRIPTIONS: &str = "res/SkillDescriptions.csv";
pub const COMBO_UNLOCK: i64 = 73;

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
    pub support: Support,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub raw: Option<TalentSource>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub combo_unlock: Option<i64>,
}

impl Talent {
    pub fn numeric(&self) -> bool {
        self.support.is_supported() && self.combo_unlock.is_none()
    }
}

#[derive(Debug, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct TalentSource {
    pub row: usize,
    pub slot: usize,
    pub target_mask: i64,
    pub cells: [i64; 14],
}

pub fn support(id: i64) -> Support {
    if id == COMBO_UNLOCK || definitions().contains_key(&id.to_string()) {
        Support::Supported
    } else {
        Support::Unsupported
    }
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
            for field in column..column + 14 {
                required(&row, field)?;
            }
            let original_max = required(&row, column + 1)?;
            ensure!(original_max >= 0, "本能最大Lvが不正です: {unit_id}/{id}");
            let supported = support(id).is_supported();
            let numeric = supported && id != COMBO_UNLOCK;
            if id == COMBO_UNLOCK {
                ensure!(
                    original_max == 0 && required(&row, column + 2)? >= 0,
                    "コンボ解放本能の形式が不正です: {unit_id}"
                );
            }
            let max_level = if numeric {
                original_max.max(1)
            } else {
                original_max
            };
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
            if !numeric {
                index += 1;
                continue;
            }
            let costs = costs
                .get(&required(&row, column + 11)?)
                .context("本能NP費用IDが未収録です")?;
            ensure!(
                max_level <= costs.len() as i64,
                "本能NP費用のレベルが不足しています"
            );
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
    let mut statement = connection.prepare("SELECT talent_index,skill_id,max_level,description,level_limit,target_mask,add_targets,source_row,source_column FROM talent WHERE region=? AND unit_id=? ORDER BY talent_index")?;
    let mut rows = statement.query(params![region, unit_id])?;
    let mut result = Vec::new();
    let mut acquisition = None;
    while let Some(row) = rows.next()? {
        let index = row.get::<_, u32>(0)? as usize;
        let id: i64 = row.get(1)?;
        let definition = definitions().get(&id.to_string());
        let mut description: String = row.get(3)?;
        let mut name = definition
            .and_then(|value| value.name.clone())
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
                    .filter(|line| !line.is_empty() && !line.contains('%'))
                    .map(str::to_owned)
            })
            .unwrap_or_else(|| {
                if definition.is_some() {
                    format!("本能ID{id}")
                } else {
                    format!("未実装の本能（ID: {id}）")
                }
            });
        let mask: i64 = row.get(5)?;
        let enabled: bool = row.get(6)?;
        let raw = if definition.is_none() {
            if acquisition.is_none() {
                let bytes = source(connection, ACQUISITION)?.context("本能の原本がありません")?;
                acquisition = Some(numeric_rows(without_header(&bytes)?)?);
            }
            let position = row.get::<_, u32>(7)? as usize;
            let column = row.get::<_, u32>(8)? as usize;
            let (_, record) = position
                .checked_sub(2)
                .and_then(|index| acquisition.as_ref()?.get(index))
                .context("未実装本能の原本行がありません")?;
            ensure!(
                required(record, 0)? == i64::from(unit_id)
                    && required(record, column)? == id
                    && column >= 2
                    && (column - 2) % 14 == 0,
                "未実装本能の原本参照が不正です"
            );
            let mut cells = [0; 14];
            for (field, output) in cells.iter_mut().enumerate() {
                *output = required(record, column + field)?;
            }
            Some(TalentSource {
                row: position,
                slot: (column - 2) / 14,
                target_mask: mask,
                cells,
            })
        } else {
            None
        };
        let combo_unlock = if id == COMBO_UNLOCK {
            let raw = raw.as_ref().context("コンボ解放本能の原本がありません")?;
            let combo = raw.cells[2];
            ensure!(
                raw.cells[1] == 0 && combo >= 0,
                "コンボ解放本能の形式が不正です"
            );
            let combo_name: Option<String> = connection
                .query_row(
                    "SELECT name FROM combo WHERE region=? AND id=?",
                    params![region, combo],
                    |row| row.get(0),
                )
                .optional()?;
            name = "にゃんコンボ解放".into();
            description = description.replace(
                "%s",
                &combo_name.unwrap_or_else(|| format!("コンボ {combo}")),
            );
            Some(combo)
        } else {
            None
        };
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
            effect: definition
                .map(|value| value.effect.clone())
                .unwrap_or_else(|| Effect {
                    kind: if combo_unlock.is_some() {
                        "comboUnlock"
                    } else {
                        "unsupported"
                    }
                    .into(),
                    key: format!("talent-{id}"),
                    label: None,
                    fields: None,
                }),
            support: support(id),
            raw,
            combo_unlock,
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn preserves_special_and_unknown_slots_next_to_numeric_talents() -> Result<()> {
        let db = Connection::open_in_memory()?;
        db.execute_batch(include_str!("schema.sql"))?;
        db.execute_batch("INSERT INTO unit VALUES ('jp',358,4,'',60,70,0,'normal'); INSERT INTO combo VALUES ('jp',392,0,0,'骨まで愛して','攻撃力');")?;
        let acquisition = "header\n358,0,31,2,2,20,0,0,0,0,0,0,28,1,-1,0,73,0,392,0,0,0,0,0,0,0,106,10,-1,1,901,3,4,5,6,7,8,9,10,11,106,999,-1,0";
        for (path, bytes) in [
            (ACQUISITION, acquisition.as_bytes()),
            (COSTS, b"id,Lv1,Lv2\n1,15,20".as_slice()),
            (
                DESCRIPTIONS,
                "id,description\n28,攻撃力強化\n106,にゃんコンボを解放<br>「%s」".as_bytes(),
            ),
        ] {
            db.execute(
                "INSERT INTO source_file VALUES (?1,?1,'local','fixture',?2)",
                params![path, bytes],
            )?;
        }
        import(&db, "jp")?;
        let talents = read(&db, "jp", 358)?;
        assert_eq!(talents.len(), 3);
        assert_eq!(talents[0].values, [[2, 0, 0, 0], [20, 0, 0, 0]]);
        assert_eq!(
            (talents[1].max_level, talents[1].combo_unlock),
            (0, Some(392))
        );
        assert!(!talents[1].numeric() && talents[1].description.contains("骨まで愛して"));
        assert_eq!(talents[2].support, Support::Unsupported);
        assert_eq!(talents[2].max_level, 3);
        let raw = talents[2].raw.as_ref().unwrap();
        assert_eq!((raw.slot, raw.cells[2], raw.cells[11]), (2, 4, 999));
        assert!(talents[2].values.is_empty());
        db.execute(
            "UPDATE source_file SET bytes=? WHERE path=?",
            params![
                acquisition
                    .replace("901,3,4,5", "901,3,broken,5")
                    .as_bytes(),
                ACQUISITION
            ],
        )?;
        assert!(import(&db, "jp").is_err());
        Ok(())
    }
}
