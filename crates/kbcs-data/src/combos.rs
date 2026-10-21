use crate::{
    import::read_asset,
    model::{csv_rows, numeric_rows, required},
    source::{Dataset, Source},
};
use anyhow::Result;
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
    pub active: bool,
    pub name: String,
    pub effect: String,
    pub members: Vec<Member>,
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

pub fn read(connection: &Connection, region: &str) -> Result<Vec<Combo>> {
    let mut statement = connection
        .prepare("SELECT id,type,grade,name,effect FROM combo WHERE region=? ORDER BY id")?;
    let mut rows = statement.query([region])?;
    let mut result = Vec::new();
    while let Some(row) = rows.next()? {
        let id: i64 = row.get(0)?;
        let members=connection.prepare("SELECT unit_id,form_index FROM combo_member WHERE region=? AND combo_id=? ORDER BY position")?
            .query_map(params![region,id],|row|Ok(Member{id:row.get(0)?,form:row.get(1)?}))?.collect::<rusqlite::Result<_>>()?;
        result.push(Combo {
            id,
            kind: row.get(1)?,
            grade: row.get(2)?,
            active: true,
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
