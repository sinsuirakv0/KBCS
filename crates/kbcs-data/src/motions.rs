use crate::{
    import::read_asset,
    source::{Dataset, Source},
    store::Database,
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, params};
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

// 形態別の共有ID解決は取り込み済みの攻撃パスを正本にする。
pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &(impl Fn(String) + Sync),
) -> Result<()> {
    let mut statement =
        connection.prepare("SELECT motion_path FROM form UNION SELECT motion_path FROM enemy")?;
    let stems = statement
        .query_map([], |r| r.get::<_, String>(0))?
        .collect::<rusqlite::Result<Vec<_>>>()?
        .into_iter()
        .filter_map(|p| {
            p.strip_prefix("ImageData/")?
                .strip_suffix("02.maanim")
                .map(str::to_owned)
        })
        .collect::<BTreeSet<_>>();
    let mut paths = BTreeSet::new();
    for path in dataset.files.keys() {
        let Some(name) = path.strip_prefix("ImageData/") else {
            continue;
        };
        let base = name.split('.').next().unwrap_or("");
        let prefix = base.split('_').take(2).collect::<Vec<_>>().join("_");
        let standard =
            base.is_ascii() && base.len() >= 2 && stems.contains(&base[..base.len() - 2]);
        if (stems.contains(base)
            || stems.contains(&prefix)
            || standard
            || base.starts_with("battle_soul_")
            || base.starts_with("battle_demonsoul_"))
            && [".imgcut", ".mamodel", ".maanim"]
                .iter()
                .any(|ext| path.ends_with(ext))
        {
            paths.insert(path.clone());
        }
    }
    let mut downloads = paths.clone();
    for path in &paths {
        if let Some(stem) = path
            .strip_prefix("ImageData/")
            .and_then(|p| p.strip_suffix(".imgcut"))
        {
            let image = format!("Number/{stem}.png");
            if dataset.files.contains_key(&image) {
                downloads.insert(image);
            }
        }
    }
    source.prefetch(
        dataset,
        &downloads.into_iter().collect::<Vec<_>>(),
        progress,
    )?;
    let mut count = 0;
    for path in paths {
        read_asset(source, dataset, connection, &path)?;
        if let Some(stem) = path
            .strip_prefix("ImageData/")
            .and_then(|p| p.strip_suffix(".imgcut"))
        {
            // 本家005bcea8は%s.pngで結合する。imgcut内の制作PCパスは参照しない。
            let image = format!("Number/{stem}.png");
            if dataset.files.contains_key(&image) && dataset.release.is_none() {
                read_asset(source, dataset, connection, &image)?;
            }
        }
        count += 1;
        if count % 2000 == 0 {
            progress(format!("モーション素材: {count}"));
        }
    }
    progress(format!("モーション素材: {count}定義と参照画像"));
    Ok(())
}

pub(crate) fn descriptor(database: &Database, path: &str, role: &str) -> Result<Value> {
    if path.ends_with(".png") {
        // 画像本体はasset要求で読む。manifestのためにBLOBを複製しない。
        return Ok(database.connection.query_row(
            "SELECT original_path,source_kind,sha256,length(bytes) FROM source_file WHERE path=?1 UNION ALL SELECT original_path,source_kind,sha256,size FROM asset_reference WHERE path=?1 LIMIT 1",
            [path],
            |r| Ok(json!({"path":path,"role":role,"original":r.get::<_,String>(0)?,"sourceKind":r.get::<_,String>(1)?,"sha256":r.get::<_,String>(2)?,"size":r.get::<_,i64>(3)?,"text":null})),
        )?);
    }
    let (original, kind, sha, bytes) = database.source(path)?;
    Ok(
        json!({"path":path,"role":role,"original":original,"sourceKind":kind,"sha256":sha,"size":bytes.len(),"text":if path.ends_with(".png"){None}else{Some(String::from_utf8(bytes)?)}}),
    )
}

pub fn manifest(
    database: &Database,
    region: &str,
    kind: &str,
    id: u32,
    form: usize,
) -> Result<Value> {
    describe(database, region, kind, id, form, true)
}

// 戦闘開始時はファイル本文をJSONへ複製せず、同じ解決済みのパスだけを返す。
pub fn resources(
    database: &Database,
    region: &str,
    kind: &str,
    id: u32,
    form: usize,
) -> Result<Value> {
    describe(database, region, kind, id, form, false)
}

fn describe(
    database: &Database,
    region: &str,
    kind: &str,
    id: u32,
    form: usize,
    include_files: bool,
) -> Result<Value> {
    ensure!(
        kind == "unit" || kind == "enemy",
        "モーション種別が不正です"
    );
    ensure!(form <= 3, "形態番号が不正です");
    let (name, attack, raw, icon): (String, String, String, Option<String>) = if kind == "unit" {
        database.connection.query_row("SELECT name,motion_path,raw_cells,icon_path FROM form WHERE region=? AND unit_id=? AND form_index=?",params![region,id,form as i64],|r|Ok((r.get(0)?,r.get(1)?,r.get(2)?,r.get(3)?)))?
    } else {
        database.connection.query_row(
            "SELECT name,motion_path,raw_cells,icon_path FROM enemy WHERE region=? AND id=?",
            params![region, id],
            |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?, r.get(3)?)),
        )?
    };
    let cells: Vec<String> = serde_json::from_str(&raw)?;
    let get = |column: usize| {
        cells
            .get(column)
            .and_then(|v| v.trim().parse::<i64>().ok())
            .unwrap_or(0)
    };
    let soul = get(if kind == "unit" { 67 } else { 54 });
    let special = get(if kind == "unit" { 69 } else { 63 }) != 0;
    let stem = attack
        .strip_prefix("ImageData/")
        .and_then(|p| p.strip_suffix("02.maanim"))
        .context("攻撃モーションのパスが不正です")?;
    let mut files = BTreeMap::new();
    let body = resource(database, stem, "body", &mut files, include_files)?
        .context("モーション素材が未導入です。データ管理から更新してください")?;
    let common = if soul >= 0 {
        resource(
            database,
            &format!("battle_soul_{soul:03}"),
            "soul",
            &mut files,
            include_files,
        )?
    } else {
        None
    };
    Ok(
        json!({"schemaVersion":1,"metadata":database.metadata()?,"character":{"kind":kind,"id":id,"form":form,"name":name,"icon":icon,"stem":stem,"soulId":soul,"deathMotion":special},"body":body,"soul":common,"files":files.into_values().collect::<Vec<_>>()}),
    )
}

fn resource(
    database: &Database,
    stem: &str,
    key: &str,
    files: &mut BTreeMap<String, Value>,
    include_files: bool,
) -> Result<Option<Value>> {
    let cut = format!("ImageData/{stem}.imgcut");
    let model = format!("ImageData/{stem}.mamodel");
    let exists = |path: &str| -> Result<bool> {
        Ok(database.connection.query_row(
            "SELECT EXISTS(SELECT 1 FROM source_file WHERE path=?1 UNION ALL SELECT 1 FROM asset_reference WHERE path=?1)",
            [path],
            |r| r.get(0),
        )?)
    };
    if !exists(&cut)? || !exists(&model)? {
        return Ok(None);
    }
    let image = format!("Number/{stem}.png");
    ensure!(exists(&image)?, "スプライト画像が未収録です: {image}");
    if include_files {
        files.insert(cut.clone(), descriptor(database, &cut, "分割定義")?);
        files.insert(model.clone(), descriptor(database, &model, "モデル")?);
        files.insert(
            image.clone(),
            descriptor(database, &image, "スプライト画像")?,
        );
    }
    let mut statement = database
        .connection
        .prepare("SELECT path FROM source_file WHERE path GLOB ? ORDER BY path")?;
    let mut animations = Vec::new();
    for path in statement.query_map([format!("ImageData/{stem}*.maanim")], |r| {
        r.get::<_, String>(0)
    })? {
        let path = path?;
        let suffix = path
            .strip_prefix(&format!("ImageData/{stem}"))
            .and_then(|p| p.strip_suffix(".maanim"))
            .context("モーション名不正")?;
        let label = match suffix {
            "00" => "移動",
            "01" => "待機",
            "02" => "攻撃",
            "03" => "KB",
            "04" => "潜行開始",
            "05" => "地中移動",
            "06" => "潜行終了",
            "_soul" => "専用の魂",
            "" => "魂",
            _ => suffix,
        };
        let motion_key = if suffix.is_empty() { "soul" } else { suffix };
        animations.push(json!({"key":motion_key,"name":label,"path":path}));
        if include_files {
            files.insert(path.clone(), descriptor(database, &path, "モーション")?);
        }
    }
    Ok(Some(
        json!({"key":key,"stem":stem,"image":image,"cut":cut,"model":model,"animations":animations}),
    ))
}

// モーション選択に必要な名前と形態だけを読み、数値・本能・コンボを生成しない。
pub fn choices(database: &Database, region: &str, kind: &str) -> Result<Value> {
    ensure!(
        kind == "unit" || kind == "enemy",
        "モーション種別が不正です"
    );
    let mut entries = Vec::new();
    if kind == "unit" {
        let mut statement = database.connection.prepare(
            "SELECT unit_id,form_index,name FROM form WHERE region=? ORDER BY unit_id,form_index",
        )?;
        let rows = statement.query_map([region], |r| {
            Ok((
                r.get::<_, u32>(0)?,
                r.get::<_, u32>(1)?,
                r.get::<_, String>(2)?,
            ))
        })?;
        let mut current = None;
        for row in rows {
            let (id, index, name) = row?;
            if current != Some(id) {
                entries.push(json!({"id":id,"name":name,"forms":[]}));
                current = Some(id);
            }
            entries.last_mut().unwrap()["forms"]
                .as_array_mut()
                .unwrap()
                .push(json!({"index":index,"name":name}));
        }
    } else {
        let mut statement = database
            .connection
            .prepare("SELECT id,name FROM enemy WHERE region=? ORDER BY id")?;
        for row in statement.query_map([region], |r| {
            Ok(json!({"id":r.get::<_,u32>(0)?,"name":r.get::<_,String>(1)?}))
        })? {
            entries.push(row?);
        }
    }
    Ok(json!({"metadata":database.metadata()?,"entries":entries}))
}
