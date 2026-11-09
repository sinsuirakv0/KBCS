use crate::store::Database;
use anyhow::Result;
use rusqlite::OptionalExtension;
use serde_json::Value;
use std::{collections::BTreeMap, sync::OnceLock};

pub fn settings() -> &'static Value {
    static SETTINGS: OnceLock<Value> = OnceLock::new();
    SETTINGS.get_or_init(|| {
        serde_json::from_str(
            include_str!("../../../ui/settings-catalog.js")
                .trim_start_matches('\u{feff}')
                .trim()
                .trim_start_matches("export default ")
                .trim_end_matches(';'),
        )
        .expect("施設・お宝の参照定義")
    })
}

pub fn source_matches(database: &Database, path: &str, expected: &str) -> Result<Option<bool>> {
    let sha: Option<String> = database.connection.query_row(
        "SELECT sha256 FROM asset_reference WHERE path=?1 UNION ALL SELECT sha256 FROM source_file WHERE path=?1 LIMIT 1",
        [path], |row| row.get(0)).optional()?;
    Ok(sha.map(|sha| sha == expected))
}

pub fn parameters_match(database: &Database, expected: &Value) -> Result<bool> {
    let bytes = database.source("Data/param.tsv")?.3;
    let text = std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}');
    let mut values = BTreeMap::new();
    for (key, value) in text.lines().filter_map(|line| line.split_once('\t')) {
        if expected.get(key).is_some() {
            anyhow::ensure!(
                values.insert(key, value.trim().parse::<i64>()?).is_none(),
                "戦闘設定キーの重複: {key}"
            );
        }
    }
    Ok(expected
        .as_object()
        .expect("戦闘設定の参照定義")
        .iter()
        .all(|(key, value)| values.get(key.as_str()).copied() == value.as_i64()))
}

fn facility_rows_match(database: &Database, path: &str, settings: &Value) -> Result<bool> {
    let rows = crate::model::csv_rows(&database.source(path)?.3)?;
    for (position, facility) in settings["facilities"]
        .as_array()
        .expect("施設の参照定義")
        .iter()
        .enumerate()
    {
        let id = (60 + position).to_string();
        if path == "res/GatyaitemName.csv" {
            let Some(row) = rows.get(60 + position) else {
                return Ok(false);
            };
            let description = row
                .iter()
                .skip(1)
                .map(|cell| cell.trim())
                .filter(|cell| !matches!(*cell, "" | "＠" | "@"))
                .collect::<Vec<_>>()
                .join("\n");
            if row.first().map(String::as_str) != facility["name"].as_str()
                || facility["description"] != description
            {
                return Ok(false);
            }
        } else {
            let mut matches = rows.iter().filter(|row| row.get(3) == Some(&id));
            let Some(row) = matches.next() else {
                return Ok(false);
            };
            if matches.next().is_some()
                || row.get(6).map(String::as_str) != Some("2")
                || row.get(7).and_then(|v| v.parse::<usize>().ok()) != Some(position)
            {
                return Ok(false);
            }
        }
    }
    Ok(true)
}

pub fn calculation_version(database: &Database) -> Result<Option<String>> {
    let settings = settings();
    let version = settings["version"].as_str().expect("参照版");
    if database
        .metadata()?
        .get("version")
        .is_some_and(|v| v == version)
    {
        return Ok(Some(version.into()));
    }
    // 版番号だけを緩めず、施設・お宝の全採用元が同じ場合だけ既存定義を使う。
    for (path, source) in settings["sources"].as_object().expect("参照元") {
        let matches = source_matches(
            database,
            path,
            source["sha256"].as_str().unwrap_or_default(),
        )?;
        if matches == Some(true) {
            continue;
        }
        let compatible = if matches.is_none() {
            false
        } else {
            match path.as_str() {
                "Data/param.tsv" => parameters_match(database, &settings["combatParameters"])?,
                "res/GatyaitemName.csv" | "Data/Gatyaitembuy.csv" => {
                    facility_rows_match(database, path, settings)?
                }
                _ => false,
            }
        };
        if !compatible {
            return Ok(None);
        }
    }
    Ok(Some(version.into()))
}

#[test]
fn reference_compatibility_requires_every_source_hash() -> Result<()> {
    let connection = rusqlite::Connection::open_in_memory()?;
    connection.execute_batch("CREATE TABLE metadata(key TEXT,value TEXT); INSERT INTO metadata VALUES('version','different'); CREATE TABLE asset_reference(path TEXT,sha256 TEXT); CREATE TABLE source_file(path TEXT,sha256 TEXT);")?;
    for (path, source) in settings()["sources"].as_object().unwrap() {
        connection.execute(
            "INSERT INTO asset_reference VALUES(?,?)",
            [path.as_str(), source["sha256"].as_str().unwrap()],
        )?;
    }
    let database = Database { connection };
    assert_eq!(calculation_version(&database)?.as_deref(), Some("15.7.2"));
    database.connection.execute(
        "UPDATE asset_reference SET sha256='changed' WHERE path='Data/AbilityData.csv'",
        [],
    )?;
    assert!(calculation_version(&database)?.is_none());
    Ok(())
}
