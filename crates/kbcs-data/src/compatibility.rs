use crate::store::Database;
use anyhow::Result;
use rusqlite::OptionalExtension;
use serde_json::Value;
use std::sync::OnceLock;

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
        if source_matches(
            database,
            path,
            source["sha256"].as_str().unwrap_or_default(),
        )? != Some(true)
        {
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
