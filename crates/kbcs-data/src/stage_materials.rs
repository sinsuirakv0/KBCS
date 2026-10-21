use crate::{
    import::read_asset,
    model::csv_rows,
    source::{Dataset, Source},
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde_json::{Value, json};
use std::collections::BTreeMap;

pub(crate) fn import(source: &Source, dataset: &Dataset, connection: &Connection) -> Result<()> {
    let path = "Data/DropItem.csv";
    if !dataset.files.contains_key(path) {
        return Ok(());
    }
    let region = &dataset.current.header.source_region;
    let items = csv_rows(&read_asset(
        source,
        dataset,
        connection,
        "Data/Gatyaitembuy.csv",
    )?)?;
    let mut ids = BTreeMap::new();
    // 現版006f53b8の列6/7と006f308cの種別7・スロット検索を使用する。
    for (id, row) in items
        .iter()
        .filter(|row| {
            row.first()
                .is_some_and(|value| value.parse::<i64>().is_ok())
        })
        .enumerate()
    {
        if row.get(6).is_some_and(|value| value == "7") {
            let slot: i64 = row.get(7).context("素材スロット欠測")?.parse()?;
            ensure!(
                ids.insert(slot, id as i64).is_none(),
                "素材スロット重複: {slot}"
            );
        }
    }
    for (line, text) in std::str::from_utf8(&read_asset(source, dataset, connection, path)?)?
        .trim_start_matches('\u{feff}')
        .lines()
        .enumerate()
    {
        let Some(cells) = csv_rows(text.as_bytes())?.into_iter().next() else {
            continue;
        };
        let Some(id) = cells.first().and_then(|value| value.parse::<i64>().ok()) else {
            continue;
        };
        let included: bool = connection.query_row(
            "SELECT EXISTS(SELECT 1 FROM stage_map WHERE region=? AND id=?)",
            params![region, id],
            |row| row.get(0),
        )?;
        if !included {
            continue;
        }
        ensure!(
            (14..=30).contains(&cells.len()),
            "素材列数が未対応です: {path}:{}",
            line + 1
        );
        let integer = |column: usize| -> Result<i64> { Ok(cells[column].trim().parse()?) };
        let miss = integer(13)?;
        ensure!((0..=100).contains(&miss), "素材ハズレ値が範囲外です");
        connection.execute(
            "INSERT INTO stage_material_profile VALUES (?,?,?,?,?,?)",
            params![
                region,
                id,
                miss,
                path,
                (line + 1) as i64,
                serde_json::to_string(&cells)?
            ],
        )?;
        for (column, cell) in cells.iter().enumerate().take(13).skip(1) {
            let value: f32 = if cell.trim().is_empty() {
                0.0
            } else {
                cell.trim().parse()?
            };
            ensure!(value.is_finite() && value >= 0.0, "素材係数が不正です");
            if column < 5 {
                connection.execute(
                    "INSERT INTO stage_material_crown VALUES (?,?,?,?)",
                    params![region, id, column as i64, f64::from(value)],
                )?;
            } else {
                connection.execute(
                    "INSERT INTO stage_material_count VALUES (?,?,?,?)",
                    params![region, id, (column - 5) as i64, f64::from(value)],
                )?;
            }
        }
        for column in 14..cells.len() {
            let slot = (column - 14) as i64;
            let weight = integer(column)?;
            ensure!(
                weight >= 0 && weight <= i64::from(i32::MAX),
                "素材重みが範囲外です"
            );
            let item = ids.get(&slot).copied();
            ensure!(
                weight == 0 || item.is_some(),
                "素材IDが見つかりません: {slot}"
            );
            connection.execute(
                "INSERT INTO stage_material_weight VALUES (?,?,?,?,?)",
                params![region, id, slot, item, weight],
            )?;
            if let Some(item) = item.filter(|_| weight > 0) {
                let icon = format!("Image/gatyaitemD_{item:02}_f.png");
                if dataset.files.contains_key(&icon) {
                    read_asset(source, dataset, connection, &icon)?;
                }
            }
        }
    }
    Ok(())
}

pub(crate) fn read(connection: &Connection, region: &str, id: i64) -> Result<Option<Value>> {
    let Some((miss,line,cells))=connection.query_row("SELECT miss,source_row,raw_cells FROM stage_material_profile WHERE region=? AND map_id=?",params![region,id],|row|Ok((row.get::<_,i32>(0)?,row.get::<_,i64>(1)?,row.get::<_,String>(2)?))).optional()? else {return Ok(None);};
    let mut statement = connection.prepare(
        "SELECT multiplier FROM stage_material_crown WHERE region=? AND map_id=? ORDER BY crown",
    )?;
    let multipliers = statement
        .query_map(params![region, id], |row| row.get::<_, f32>(0))?
        .collect::<rusqlite::Result<Vec<_>>>()?;
    let mut statement = connection.prepare(
        "SELECT count FROM stage_material_count WHERE region=? AND map_id=? ORDER BY stage_index",
    )?;
    let counts = statement
        .query_map(params![region, id], |row| row.get::<_, f32>(0))?
        .collect::<rusqlite::Result<Vec<_>>>()?;
    let mut statement=connection.prepare("SELECT slot,item_id,weight FROM stage_material_weight WHERE region=? AND map_id=? ORDER BY slot")?;
    let rows = statement.query_map(params![region, id], |row| {
        Ok((
            row.get::<_, i64>(0)?,
            row.get::<_, Option<i64>>(1)?,
            row.get::<_, i32>(2)?,
        ))
    })?;
    let mut weights = [0; 16];
    let mut items = Vec::new();
    for row in rows {
        let (slot, item, weight) = row?;
        ensure!((0..16).contains(&slot), "素材スロットが範囲外です");
        weights[slot as usize] = weight;
        if weight > 0 {
            items.push(json!({"id":item.context("素材ID欠測")?,"slot":slot,"weight":weight}));
        }
    }
    Ok(Some(
        json!({"multipliers":multipliers,"counts":counts,"weights":weights,"miss":miss,"items":items,"source":"Data/DropItem.csv","sourceRow":line,"raw":serde_json::from_str::<Value>(&cells)?}),
    ))
}
