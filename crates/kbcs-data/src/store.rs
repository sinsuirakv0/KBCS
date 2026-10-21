use crate::{
    SCHEMA_VERSION,
    model::{Attack, Form, Property, UnitSummary, normalize_query},
    source::parse_json,
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OpenFlags, params};
use serde::{Deserialize, Serialize};
use std::{
    collections::BTreeMap,
    path::{Path, PathBuf},
};

#[derive(Default, Serialize, Deserialize)]
pub struct Catalog {
    pub regions: BTreeMap<String, String>,
}

pub fn catalog(root: &Path) -> Result<Catalog> {
    let path = root.join("current.json");
    if !path.exists() {
        return Ok(Catalog::default());
    }
    parse_json(&std::fs::read(path)?)
}

pub fn current_path(root: &Path, region: &str) -> Result<PathBuf> {
    let name = catalog(root)?
        .regions
        .get(region)
        .cloned()
        .context("DB未導入です。ホームからデータを取り込んでください")?;
    ensure!(
        name.ends_with(".sqlite") && !name.contains(['/', '\\', ':']) && !name.starts_with('.'),
        "不正なDB参照"
    );
    Ok(root.join("official").join(name))
}

pub fn validate(connection: &Connection) -> Result<()> {
    ensure!(
        connection.query_row("PRAGMA user_version", [], |row| row.get::<_, i32>(0))?
            == SCHEMA_VERSION,
        "未対応のDBスキーマです。現在の変換器で再取り込みしてください"
    );
    let integrity: String = connection.query_row("PRAGMA integrity_check", [], |row| row.get(0))?;
    ensure!(integrity == "ok", "DB整合性エラー: {integrity}");
    ensure!(
        !connection.prepare("PRAGMA foreign_key_check")?.exists([])?,
        "DB参照整合性エラー"
    );
    ensure!(
        connection.query_row("SELECT count(*) FROM form", [], |row| row.get::<_, i64>(0))? > 0,
        "キャラ形態が空です"
    );
    Ok(())
}

pub struct Database {
    pub connection: Connection,
}

impl Database {
    pub fn open(root: &Path, region: &str) -> Result<Self> {
        Self::open_path(&current_path(root, region)?)
    }

    pub fn open_path(path: &Path) -> Result<Self> {
        let connection = Connection::open_with_flags(
            path,
            OpenFlags::SQLITE_OPEN_READ_ONLY | OpenFlags::SQLITE_OPEN_NO_MUTEX,
        )?;
        ensure!(
            connection.query_row("PRAGMA user_version", [], |row| row.get::<_, i32>(0))?
                == SCHEMA_VERSION,
            "未対応のDBスキーマです。再取り込みが必要です"
        );
        Ok(Self { connection })
    }

    pub fn metadata(&self) -> Result<BTreeMap<String, String>> {
        Ok(self
            .connection
            .prepare("SELECT key,value FROM metadata ORDER BY key")?
            .query_map([], |row| Ok((row.get(0)?, row.get(1)?)))?
            .collect::<rusqlite::Result<_>>()?)
    }

    pub fn search(&self, region: &str, query: &str, descending: bool) -> Result<Vec<UnitSummary>> {
        let query = normalize_query(query);
        let tokens: Vec<_> = query.split_whitespace().collect();
        let ids = tokens
            .iter()
            .map(|value| value.parse::<u32>())
            .collect::<std::result::Result<Vec<_>, _>>()
            .ok()
            .filter(|values| !values.is_empty());
        let mut statement = self.connection.prepare("SELECT u.id,u.rarity,(SELECT name FROM form n WHERE n.region=u.region AND n.unit_id=u.id ORDER BY form_index LIMIT 1),(SELECT count(*) FROM form n WHERE n.region=u.region AND n.unit_id=u.id),group_concat(f.search_text,' ') FROM unit u JOIN form f ON f.region=u.region AND f.unit_id=u.id WHERE u.region=? GROUP BY u.id ORDER BY u.id")?;
        let mut rows = statement.query([region])?;
        let mut results = Vec::new();
        while let Some(row) = rows.next()? {
            let id: u32 = row.get(0)?;
            let text: String = row.get(4)?;
            let matches = if let Some(ids) = &ids {
                ids.contains(&id)
            } else {
                tokens.iter().all(|token| text.contains(token))
            };
            if matches {
                results.push(UnitSummary {
                    id,
                    rarity: row.get(1)?,
                    name: row.get(2)?,
                    forms: row.get::<_, u32>(3)? as usize,
                });
            }
        }
        if descending {
            results.reverse();
        }
        Ok(results)
    }

    pub fn form(&self, region: &str, id: u32, index: usize) -> Result<Form> {
        let mut form = self.connection.query_row("SELECT f.name,f.description,u.rarity,f.hp,f.speed,f.range,f.cost,f.respawn_raw,f.knockbacks,f.interval_raw,f.area,f.attack_cycle,f.animation_length,f.source_path,f.name_source,f.motion_path,f.raw_cells,u.max_level,u.plus_level,u.is_spirit,f.icon_path FROM form f JOIN unit u ON u.region=f.region AND u.id=f.unit_id WHERE f.region=? AND f.unit_id=? AND f.form_index=?", params![region,id,index as i64], |row| Ok(Form {
            region: region.into(), unit_id: id, index, name: row.get(0)?, description: row.get(1)?, rarity: row.get(2)?, max_level: row.get(17)?, plus_level: row.get(18)?, is_spirit: row.get(19)?, icon_path: row.get(20)?, hp: row.get(3)?, speed: row.get(4)?, range: row.get(5)?, cost: row.get(6)?, respawn_raw: row.get(7)?, knockbacks: row.get(8)?, interval_raw: row.get(9)?, area: row.get(10)?, attack_cycle: row.get(11)?, animation_length: row.get(12)?, source_path: row.get(13)?, name_source: row.get(14)?, motion_path: row.get(15)?, raw_cells: Vec::new(), raw: Vec::new(), attacks: Vec::new(), properties: Vec::new(), growth: Vec::new(),
        }))?;
        let cells: String = self.connection.query_row(
            "SELECT raw_cells FROM form WHERE region=? AND unit_id=? AND form_index=?",
            params![region, id, index as i64],
            |row| row.get(0),
        )?;
        form.raw_cells = serde_json::from_str(&cells)?;
        form.raw = form
            .raw_cells
            .iter()
            .map(|cell| cell.trim().parse::<i64>().ok())
            .collect();
        form.attacks = self.connection.prepare("SELECT damage,foreswing,ability_enabled,range_start,range_end FROM attack WHERE region=? AND unit_id=? AND form_index=? ORDER BY hit")?.query_map(params![region,id,index as i64], |row| {
            let start: Option<i64> = row.get(3)?;
            let end: Option<i64> = row.get(4)?;
            Ok(Attack { damage: row.get(0)?, foreswing: row.get(1)?, ability_enabled: row.get(2)?, range: start.zip(end).map(|(a,b)| [a,b]) })
        })?.collect::<rusqlite::Result<_>>()?;
        form.growth = self
            .connection
            .prepare("SELECT rate FROM growth WHERE region=? AND unit_id=? ORDER BY position")?
            .query_map(params![region, id], |row| row.get(0))?
            .collect::<rusqlite::Result<_>>()?;
        let properties: Vec<(String, String)> = self.connection.prepare("SELECT key,label FROM property WHERE region=? AND unit_id=? AND form_index=? ORDER BY key")?.query_map(params![region,id,index as i64], |row| Ok((row.get(0)?,row.get(1)?)))?.collect::<rusqlite::Result<_>>()?;
        for (key, label) in properties {
            let values: Vec<(u32, Option<i64>)> = self.connection.prepare("SELECT source_column,value FROM property_parameter WHERE region=? AND unit_id=? AND form_index=? AND key=? ORDER BY position")?.query_map(params![region,id,index as i64,&key], |row| Ok((row.get(0)?,row.get(1)?)))?.collect::<rusqlite::Result<_>>()?;
            form.properties.push(Property {
                key,
                label,
                columns: values.iter().map(|value| value.0 as usize).collect(),
                values: values.iter().map(|value| value.1).collect(),
            });
        }
        Ok(form)
    }

    pub fn source(&self, path: &str) -> Result<(String, String, String, Vec<u8>)> {
        Ok(self.connection.query_row(
            "SELECT original_path,source_kind,sha256,bytes FROM source_file WHERE path=?",
            [path],
            |row| Ok((row.get(0)?, row.get(1)?, row.get(2)?, row.get(3)?)),
        )?)
    }
}

pub(crate) fn insert_form(connection: &Connection, form: &Form, aliases: &str) -> Result<()> {
    let search = normalize_query(&format!("{} {} {aliases}", form.name, form.description));
    connection.execute(
        "INSERT INTO form VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        params![
            form.region,
            form.unit_id,
            form.index as i64,
            form.name,
            form.description,
            search,
            form.hp,
            form.speed,
            form.range,
            form.cost,
            form.respawn_raw,
            form.knockbacks,
            form.interval_raw,
            form.area,
            form.attack_cycle,
            form.animation_length,
            form.source_path,
            form.name_source,
            form.motion_path,
            form.icon_path,
            serde_json::to_string(&form.raw_cells)?
        ],
    )?;
    for (hit, attack) in form.attacks.iter().enumerate() {
        connection.execute(
            "INSERT INTO attack VALUES (?,?,?,?,?,?,?,?,?)",
            params![
                form.region,
                form.unit_id,
                form.index as i64,
                hit as i64,
                attack.damage,
                attack.foreswing,
                attack.ability_enabled,
                attack.range.map(|value| value[0]),
                attack.range.map(|value| value[1])
            ],
        )?;
    }
    for property in &form.properties {
        connection.execute(
            "INSERT INTO property VALUES (?,?,?,?,?)",
            params![
                form.region,
                form.unit_id,
                form.index as i64,
                property.key,
                property.label
            ],
        )?;
        for (position, (&column, &value)) in
            property.columns.iter().zip(&property.values).enumerate()
        {
            connection.execute(
                "INSERT INTO property_parameter VALUES (?,?,?,?,?,?,?)",
                params![
                    form.region,
                    form.unit_id,
                    form.index as i64,
                    property.key,
                    position as i64,
                    column as i64,
                    value
                ],
            )?;
        }
    }
    Ok(())
}
