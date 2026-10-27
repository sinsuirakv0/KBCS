use anyhow::{Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use std::{path::Path, time::Duration};

#[derive(Clone, Copy, Deserialize, Serialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Options {
    pub bgm_level: u8,
    pub se_level: u8,
    pub rows: u8,
}
impl Default for Options {
    fn default() -> Self {
        Self {
            bgm_level: 3,
            se_level: 3,
            rows: 2,
        }
    }
}
impl Options {
    fn validate(&self) -> Result<()> {
        ensure!(
            self.bgm_level <= 3 && self.se_level <= 3 && (1..=2).contains(&self.rows),
            "戦闘設定の範囲が不正です"
        );
        Ok(())
    }
}
pub fn access(root: &Path, update: Option<Options>) -> Result<Options> {
    let folder = root.join("user");
    std::fs::create_dir_all(&folder)?;
    let connection = Connection::open(folder.join("battle-options.sqlite"))?;
    connection.busy_timeout(Duration::from_secs(5))?;
    connection.execute_batch("CREATE TABLE IF NOT EXISTS options(id INTEGER PRIMARY KEY CHECK(id=1), document TEXT NOT NULL)")?;
    if let Some(value) = update {
        value.validate()?;
        connection.execute("INSERT INTO options VALUES(1,?) ON CONFLICT(id) DO UPDATE SET document=excluded.document", params![serde_json::to_string(&value)?])?;
        return Ok(value);
    }
    let text: Option<String> = connection
        .query_row("SELECT document FROM options WHERE id=1", [], |r| r.get(0))
        .optional()?;
    let value = text
        .map(|s| serde_json::from_str::<Options>(&s))
        .transpose()?
        .unwrap_or_default();
    value.validate()?;
    Ok(value)
}
