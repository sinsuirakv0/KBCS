use crate::{
    import::read_asset,
    model::{csv_rows, numeric_rows, required},
    source::{Dataset, Source},
    support::Support,
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, params};
use serde::Serialize;

#[derive(Debug, Serialize)]
pub struct Member {
    pub id: i64,
    pub form: i64,
}

#[derive(Debug, Serialize)]
pub struct Combo {
    pub id: i64,
    #[serde(rename = "type")]
    pub kind: i64,
    pub grade: i64,
    pub group: i64,
    #[serde(rename = "groupName")]
    pub group_name: String,
    pub active: bool,
    pub condition: i64,
    pub support: Support,
    pub unlock: Vec<Unlock>,
    pub name: String,
    pub effect: String,
    pub members: Vec<Member>,
}

#[derive(Debug, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Unlock {
    pub unit_id: u32,
    pub talent_index: usize,
    pub minimum_level: u32,
}

impl Combo {
    pub fn unlocked(&self, mut purchased: impl FnMut(&Unlock) -> bool) -> bool {
        self.support.is_supported() && (self.active || self.unlock.iter().any(&mut purchased))
    }
}

#[derive(Debug, Serialize)]
pub struct ComboEffect {
    pub index: i64,
    pub label: String,
    pub values: Vec<i64>,
}

pub(crate) fn import(source: &Source, dataset: &Dataset, connection: &Connection) -> Result<()> {
    let path = "Data/NyancomboData.csv";
    if !dataset.files.contains_key(path) {
        return Ok(());
    }
    let region = &dataset.current.header.source_region;
    let mut texts = Vec::new();
    for path in [
        "res/Nyancombo_ja.csv",
        "res/Nyancombo1_ja.csv",
        "res/Nyancombo2_ja.csv",
    ] {
        texts.push(csv_rows(&read_asset(source, dataset, connection, path)?)?);
    }
    let path_params = "Data/NyancomboParam.tsv";
    if dataset.files.contains_key(path_params) {
        let bytes = read_asset(source, dataset, connection, path_params)?;
        let text = std::str::from_utf8(&bytes)?.replace('\t', ",");
        for (index, (_, values)) in numeric_rows(text.as_bytes())?.into_iter().enumerate() {
            let label = texts[1]
                .get(index)
                .and_then(|row| row.first())
                .cloned()
                .unwrap_or_default();
            connection.execute(
                "INSERT INTO combo_effect VALUES (?,?,?)",
                params![region, index as i64, label],
            )?;
            for (grade, value) in values.into_iter().enumerate() {
                connection.execute(
                    "INSERT INTO combo_effect_value VALUES (?,?,?,?)",
                    params![region, index as i64, grade as i64, value],
                )?;
            }
        }
    }
    for (id, (_, row)) in numeric_rows(&read_asset(source, dataset, connection, path)?)?
        .into_iter()
        .enumerate()
    {
        if required(&row, 1)? < 0 {
            continue;
        }
        let kind = required(&row, 13)?;
        let grade = required(&row, 14)?;
        let text = |table: usize, index: usize| {
            texts[table]
                .get(index)
                .and_then(|row| row.first())
                .cloned()
                .unwrap_or_default()
        };
        let name = text(0, id);
        let name = if name.is_empty() {
            format!("にゃんコンボ {id}")
        } else {
            name
        };
        let effect = text(1, kind as usize) + &text(2, grade as usize);
        connection.execute(
            "INSERT INTO combo VALUES (?,?,?,?,?,?)",
            params![region, id as i64, kind, grade, name, effect],
        )?;
        for position in 0..5 {
            let column = 3 + position * 2;
            let member = required(&row, column)?;
            if member >= 0 {
                connection.execute(
                    "INSERT INTO combo_member VALUES (?,?,?,?,?)",
                    params![
                        region,
                        id as i64,
                        position as i64,
                        member,
                        required(&row, column + 1)?
                    ],
                )?;
            }
        }
    }
    Ok(())
}

// 009e4e14はtype3の明示リストだけを対象限定コンボへ使う。
pub fn target_groups(connection: &Connection) -> Result<std::collections::BTreeMap<i64, Vec<i32>>> {
    let bytes: Vec<u8> = connection.query_row(
        "SELECT bytes FROM source_file WHERE path='Data/Charagroup.csv'",
        [],
        |row| row.get(0),
    )?;
    let mut groups = std::collections::BTreeMap::new();
    for row in csv_rows(&bytes)? {
        if row.get(2).map(String::as_str) != Some("3") {
            continue;
        }
        let id = row[0].parse()?;
        let units = row
            .iter()
            .skip(3)
            .map(|v| Ok(v.parse()?))
            .collect::<Result<Vec<i32>>>()?;
        groups.insert(id, units);
    }
    Ok(groups)
}

pub fn read(connection: &Connection, region: &str) -> Result<Vec<Combo>> {
    let source = |path| -> Result<Vec<u8>> {
        Ok(connection.query_row(
            "SELECT bytes FROM source_file WHERE path=?",
            [path],
            |row| row.get(0),
        )?)
    };
    let localization = String::from_utf8(source("res/localizable.tsv")?)?;
    let localized: std::collections::BTreeMap<_, _> = localization
        .lines()
        .filter_map(|line| line.split_once('\t'))
        .collect();
    let group_names: std::collections::BTreeMap<i64, String> =
        csv_rows(&source("Data/Charagroup.csv")?)?
            .into_iter()
            .filter_map(|row| {
                Some((
                    row.first()?.parse().ok()?,
                    localized.get(row.get(1)?.as_str())?.to_string(),
                ))
            })
            .collect();
    let bytes: Vec<u8> = connection.query_row(
        "SELECT bytes FROM source_file WHERE path='Data/NyancomboData.csv'",
        [],
        |row| row.get(0),
    )?;
    let source_rows = numeric_rows(&bytes)?
        .into_iter()
        .map(|(_, row)| Ok((required(&row, 1)?, required(&row, 2)?)))
        .collect::<Result<Vec<_>>>()?;
    let mut unlocks = std::collections::BTreeMap::<i64, Vec<Unlock>>::new();
    let mut units =
        connection.prepare("SELECT DISTINCT unit_id FROM talent WHERE region=? AND skill_id=?")?;
    for unit in units.query_map(params![region, crate::talents::COMBO_UNLOCK], |row| {
        row.get::<_, u32>(0)
    })? {
        let unit_id = unit?;
        if let Some((combo, talent)) = crate::talents::read(connection, region, unit_id)?
            .into_iter()
            .find_map(|talent| talent.combo_unlock.map(|combo| (combo, talent)))
        {
            ensure!(
                source_rows
                    .get(combo as usize)
                    .is_some_and(|(condition, _)| *condition == 7),
                "本能{}のコンボ解放先 {combo} が不正です",
                talent.id
            );
            unlocks.entry(combo).or_default().push(Unlock {
                unit_id,
                talent_index: talent.index,
                minimum_level: if talent.limit > 0 { 60 } else { 0 },
            });
        }
    }
    let mut statement = connection
        .prepare("SELECT id,type,grade,name,effect FROM combo WHERE region=? ORDER BY id")?;
    let mut rows = statement.query([region])?;
    let mut result = Vec::new();
    while let Some(row) = rows.next()? {
        let id: i64 = row.get(0)?;
        let kind: i64 = row.get(1)?;
        let grade: i64 = row.get(2)?;
        ensure!(
            kind >= 0 && grade >= 0,
            "コンボの効果IDまたは等級が不正です: {id}"
        );
        let &(condition, group) = source_rows.get(id as usize).context("コンボ原本行なし")?;
        let support = if (0..=28).contains(&kind)
            && (matches!(condition, 1 | 4 | 5 | 6 | 10001 | 10002 | 10003)
                || condition == 7 && unlocks.contains_key(&id))
        {
            Support::Supported
        } else {
            Support::Unsupported
        };
        let members=connection.prepare("SELECT unit_id,form_index FROM combo_member WHERE region=? AND combo_id=? ORDER BY position")?
            .query_map(params![region,id],|row|Ok(Member{id:row.get(0)?,form:row.get(1)?}))?.collect::<rusqlite::Result<_>>()?;
        result.push(Combo {
            id,
            kind,
            grade,
            group,
            group_name: group_names.get(&group).cloned().unwrap_or_default(),
            active: support.is_supported() && condition != 7,
            condition,
            support,
            unlock: unlocks.remove(&id).unwrap_or_default(),
            name: row.get(3)?,
            effect: row.get(4)?,
            members,
        });
    }
    Ok(result)
}

pub fn effects(connection: &Connection, region: &str) -> Result<Vec<ComboEffect>> {
    let mut statement =
        connection.prepare("SELECT type,label FROM combo_effect WHERE region=? ORDER BY type")?;
    let mut rows = statement.query([region])?;
    let mut result = Vec::new();
    while let Some(row) = rows.next()? {
        let index: i64 = row.get(0)?;
        let values = connection
            .prepare(
                "SELECT value FROM combo_effect_value WHERE region=? AND type=? ORDER BY grade",
            )?
            .query_map(params![region, index], |row| {
                Ok(row.get::<_, Option<i64>>(0)?.unwrap_or(0))
            })?
            .collect::<rusqlite::Result<_>>()?;
        result.push(ComboEffect {
            index,
            label: row.get(1)?,
            values,
        });
    }
    Ok(result)
}
