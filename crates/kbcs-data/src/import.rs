use crate::{
    IMPORTER_VERSION,
    model::{Attack, Form, Property, animation_length, numeric_rows, required},
    source::{Dataset, Source, hash},
    store::{self, Database},
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use std::{
    fs::{self, File, OpenOptions},
    io::Write,
    path::{Path, PathBuf},
    time::{SystemTime, UNIX_EPOCH},
};

pub const PROPERTY_FIELDS: &[(usize, &str, &str, &[usize])] = &[
    (10, "target-red", "対象: 赤い敵", &[10]),
    (16, "target-floating", "対象: 浮いてる敵", &[16]),
    (17, "target-black", "対象: 黒い敵", &[17]),
    (18, "target-metal", "対象: メタル", &[18]),
    (19, "target-white", "対象: 無属性", &[19]),
    (20, "target-angel", "対象: 天使", &[20]),
    (21, "target-alien", "対象: エイリアン", &[21]),
    (22, "target-zombie", "対象: ゾンビ", &[22]),
    (78, "target-relic", "対象: 古代種", &[78]),
    (96, "target-aku", "対象: 悪魔", &[96]),
    (23, "strong", "めっぽう強い", &[23]),
    (29, "resistant", "打たれ強い", &[29]),
    (30, "massive", "超ダメージ", &[30]),
    (32, "target-only", "ターゲット限定", &[32]),
    (33, "money", "撃破時お金2倍", &[33]),
    (34, "castle", "城破壊", &[34]),
    (43, "metal-body", "メタル", &[43]),
    (46, "wave-immune", "波動無効", &[46]),
    (47, "wave-block", "波動ストッパー", &[47]),
    (48, "knockback-immune", "ふっとばす無効", &[48]),
    (49, "stop-immune", "止める無効", &[49]),
    (50, "slow-immune", "遅くする無効", &[50]),
    (51, "weaken-immune", "攻撃力ダウン無効", &[51]),
    (52, "zombie-killer", "ゾンビキラー", &[52]),
    (53, "witch-killer", "魔女キラー", &[53]),
    (56, "shock-immune", "衝撃波無効", &[56]),
    (75, "warp-immune", "ワープ無効", &[75]),
    (77, "eva-killer", "使徒キラー", &[77]),
    (79, "curse-immune", "古代の呪い無効", &[79]),
    (80, "super-resistant", "超打たれ強い", &[80]),
    (81, "extreme", "極ダメージ", &[81]),
    (90, "toxic-immune", "毒撃無効", &[90]),
    (91, "surge-immune", "烈波無効", &[91]),
    (97, "colossus", "超生命体特効", &[97]),
    (98, "soul-killer", "魂攻撃", &[98]),
    (105, "behemoth", "超獣特効", &[105, 106, 107]),
    (109, "surge-counter", "烈波反射", &[109]),
    (111, "sage", "超賢者特効", &[111]),
    (116, "blast-immune", "爆波無効", &[116]),
    (117, "delay-immune", "再生産遅延無効", &[117]),
    (118, "alternate-respawn", "2回生産ごと再生産短縮", &[118]),
    (24, "knockback", "ふっとばす", &[24]),
    (25, "stop", "動きを止める", &[25, 26]),
    (27, "slow", "動きを遅くする", &[27, 28]),
    (31, "critical", "クリティカル", &[31]),
    (37, "weaken", "攻撃力ダウン", &[37, 38, 39]),
    (42, "survive", "生き残る", &[42]),
    (70, "barrier", "バリアブレイカー", &[70]),
    (82, "savage", "渾身の一撃", &[82, 83]),
    (84, "dodge", "攻撃無効", &[84, 85]),
    (92, "curse", "呪い", &[92, 93]),
    (95, "shield", "シールドブレイカー", &[95]),
    (113, "blast", "爆波", &[113, 114, 115]),
    (35, "wave", "波動 / 小波動", &[35, 36, 94]),
    (86, "surge", "烈波 / 小烈波", &[86, 87, 88, 89, 108]),
    (41, "strengthen", "体力低下時攻撃力アップ", &[40, 41]),
    (112, "metal-killer", "メタルキラー", &[112]),
];

pub fn properties(row: &[Option<i64>]) -> Vec<Property> {
    let get = |column| row.get(column).copied().flatten();
    let mut result: Vec<_> = PROPERTY_FIELDS
        .iter()
        .filter(|(column, _, _, _)| get(*column).is_some_and(|value| value > 0))
        .map(|(_, key, label, columns)| Property {
            key: (*key).into(),
            label: (*label).into(),
            columns: columns.to_vec(),
            values: columns.iter().map(|&column| get(column)).collect(),
        })
        .collect();
    let mut add = |key: &str, label: &str, columns: Vec<usize>| {
        result.push(Property {
            key: key.into(),
            label: label.into(),
            values: columns.iter().map(|&column| get(column)).collect(),
            columns,
        });
    };
    if get(110).is_some_and(|value| value >= 0) {
        add("spirit", "精霊召喚", vec![110]);
    }
    if get(58) == Some(2) {
        add("self-destruct", "自爆", vec![58]);
    }
    if get(59).is_some_and(|v| v > 0) || get(60).is_some_and(|v| v > 0) {
        add("multi-hit", "連続攻撃", vec![3, 59, 60]);
    }
    let mut widths = vec![45];
    if get(99).is_some_and(|v| v != 0) {
        widths.push(101);
    }
    if get(102).is_some_and(|v| v != 0) {
        widths.push(104);
    }
    if widths.iter().any(|&c| get(c).is_some_and(|v| v < 0)) {
        add("omni", "全方位攻撃", widths);
    } else if widths.iter().all(|&c| get(c).is_some_and(|v| v > 0)) {
        add("long-range", "遠方攻撃", widths);
    }
    result
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ImportReport {
    pub region: String,
    pub version: String,
    pub units: usize,
    pub forms: usize,
    pub revision: String,
    pub database: PathBuf,
}

pub fn import(
    location: &str,
    root: &Path,
    region: &str,
    progress: impl Fn(String) + Sync,
) -> Result<ImportReport> {
    run_import(location, root, region, progress, false)
}

pub fn rebuild(
    location: &str,
    root: &Path,
    region: &str,
    progress: impl Fn(String) + Sync,
) -> Result<ImportReport> {
    run_import(location, root, region, progress, true)
}
fn run_import(
    location: &str,
    root: &Path,
    region: &str,
    progress: impl Fn(String) + Sync,
    rebuild: bool,
) -> Result<ImportReport> {
    fs::create_dir_all(root.join("official"))?;
    let lock_path = root.join("update.lock");
    let mut lock_file = crate::releases::lock(&lock_path)?;
    lock_file.set_len(0)?;
    writeln!(lock_file, "{}", std::process::id())?;
    progress("データソース・採用元の検証".into());
    let integrated;
    let location = if location == crate::DEFAULT_SOURCE {
        let release = crate::releases::latest_data(region)?;
        integrated = crate::releases::install_data(&release, root, &progress)?;
        integrated.to_str().context("原本保存先の文字コード不正")?
    } else {
        location
    };
    let source = Source::open_cached(location, root, region)?;
    let mut dataset = source.import_dataset(root, region)?;
    let header = dataset.current.header.clone();
    let identity = hash(
        format!(
            "{}:{}:{}:{}",
            source.revision, header.build_id, dataset.current.manifest_sha256, IMPORTER_VERSION
        )
        .as_bytes(),
    );
    let prefix = format!("{region}-{identity}");
    let filename = if rebuild {
        format!(
            "{prefix}-{}.sqlite",
            SystemTime::now().duration_since(UNIX_EPOCH)?.as_nanos()
        )
    } else {
        store::catalog(root)?
            .regions
            .get(region)
            .filter(|v| {
                v.starts_with(&prefix) && v.ends_with(".sqlite") && !v.contains(['/', '\\', ':'])
            })
            .cloned()
            .unwrap_or_else(|| format!("{prefix}.sqlite"))
    };
    let final_path = root.join("official").join(&filename);
    let unique = SystemTime::now().duration_since(UNIX_EPOCH)?.as_nanos();
    let temporary = root
        .join("official")
        .join(format!("pending-{}-{unique}.sqlite", std::process::id()));
    let result = (|| -> Result<ImportReport> {
        if final_path.exists() {
            // 既に公開検証済みの同一snapshotは再走査しない。手動検証はverifyで行う。
            let database = Database::open_path(&final_path)?;
            ensure!(
                database
                    .metadata()?
                    .get("importer_version")
                    .is_some_and(|v| v == IMPORTER_VERSION),
                "保存済みDBの変換器版が不一致です"
            );
            progress("データは最新です。保存済みデータを再利用します".into());
        } else {
            if dataset.characters.is_empty() {
                dataset.characters = source.integrated_characters(&dataset.files)?;
            }
            let previous_size = store::current_path(root, region)
                .ok()
                .and_then(|path| path.metadata().ok())
                .map_or(0, |value| value.len());
            crate::storage::require(
                root,
                (512 * 1024 * 1024).max(previous_size.saturating_mul(2)),
            )?;
            let mut connection = Connection::open(&temporary)?;
            connection.execute_batch(include_str!("schema.sql"))?;
            connection.execute_batch("PRAGMA cache_size=-32768")?;
            let transaction = connection.transaction()?;
            let mut count = 0;
            build(&source, &dataset, &transaction, &progress, &mut count)?;
            transaction.commit()?;
            store::validate(&connection)?;
            connection.close().map_err(|(_, error)| error)?;
            OpenOptions::new()
                .write(true)
                .open(&temporary)?
                .sync_all()?;
            fs::rename(&temporary, &final_path)?;
        }
        let database = Database::open_path(&final_path)?;
        let units: u32 = database
            .connection
            .query_row("SELECT count(*) FROM unit", [], |row| row.get(0))?;
        let forms: u32 = database
            .connection
            .query_row("SELECT count(*) FROM form", [], |row| row.get(0))?;
        // 完成済みDBだけを公開し、旧DBと自作データ領域は変更しない。
        let mut catalog = store::catalog(root)?;
        catalog.regions.insert(region.into(), filename);
        let pointer = root.join(format!("current-{unique}.tmp"));
        let mut file = File::create(&pointer)?;
        file.write_all(&serde_json::to_vec_pretty(&catalog)?)?;
        file.sync_all()?;
        drop(file);
        fs::rename(&pointer, root.join("current.json"))?;
        progress(format!("完了: {units}キャラ / {forms}形態"));
        Ok(ImportReport {
            region: region.into(),
            version: header.version_name.clone(),
            units: units as usize,
            forms: forms as usize,
            revision: source.revision.clone(),
            database: final_path.clone(),
        })
    })();
    if result.is_err() {
        let _ = fs::remove_file(&temporary);
    }
    result.map_err(|error|{
        if matches!(error.downcast_ref::<rusqlite::Error>(),Some(rusqlite::Error::SqliteFailure(info,_)) if info.code==rusqlite::ErrorCode::DiskFull) {
            error.context(format!("DB生成中に空き容量が不足しました。保存先: {} / 空き: {} bytes",root.display(),crate::storage::space(root).and_then(|v|v["available"].as_u64()).unwrap_or(0)))
        }else{error}
    })
}

fn retain(
    connection: &Connection,
    path: &str,
    original: &str,
    kind: &str,
    bytes: &[u8],
) -> Result<()> {
    connection.execute(
        "INSERT OR IGNORE INTO source_file VALUES (?,?,?,?,?)",
        params![path, original, kind, hash(bytes), bytes],
    )?;
    Ok(())
}

pub(crate) fn read_asset(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    path: &str,
) -> Result<Vec<u8>> {
    // 同一の取り込み中に検証・保存済みの原本を再取得しない。
    if let Some(bytes) = connection
        .query_row(
            "SELECT bytes FROM source_file WHERE path=?",
            [path],
            |row| row.get(0),
        )
        .optional()?
    {
        return Ok(bytes);
    }
    let descriptor = dataset
        .files
        .get(path)
        .with_context(|| format!("採用元に必須ファイルがありません: {path}"))?;
    let bytes = source.checked_named(descriptor, path)?;
    retain(
        connection,
        path,
        &descriptor.path,
        &descriptor.source_kind,
        &bytes,
    )?;
    Ok(bytes)
}

fn build(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &(impl Fn(String) + Sync),
    form_count: &mut usize,
) -> Result<()> {
    if dataset.release.is_some() {
        let paths = dataset
            .files
            .keys()
            .filter(|path| path.starts_with("Data/") || path.starts_with("res/"))
            .cloned()
            .collect::<Vec<_>>();
        source.prefetch(dataset, &paths, progress)?;
    }
    let header = &dataset.current.header;
    let region = &header.source_region;
    for (key, value) in [
        ("region", region.as_str()),
        ("version", header.version_name.as_str()),
        ("revision", source.revision.as_str()),
        ("origin", source.origin.as_str()),
        ("dataset_id", header.dataset_id.as_str()),
        ("build_id", header.build_id.as_str()),
        ("importer_version", IMPORTER_VERSION),
        ("interpretation", "kbc-web schema 9 / KBCS raw-first 5"),
    ] {
        connection.execute("INSERT INTO metadata VALUES (?,?)", [key, value])?;
    }
    connection.execute(
        "INSERT INTO metadata VALUES ('version_code',?)",
        [header.version_code.to_string()],
    )?;
    if let Some((tag, published)) = &dataset.release {
        connection.execute("INSERT INTO metadata VALUES ('release_tag',?)", [tag])?;
        connection.execute(
            "INSERT INTO metadata VALUES ('release_published',?)",
            [published],
        )?;
    }
    for (path, bytes) in &dataset.proofs {
        retain(connection, path, path, "generated", bytes)?;
    }
    for (logical, descriptor) in &dataset.files {
        connection.execute(
            "INSERT INTO asset_reference VALUES (?,?,?,?,?)",
            params![
                logical,
                descriptor.path,
                descriptor.source_kind,
                descriptor.sha256,
                i64::try_from(descriptor.size)?
            ],
        )?;
    }
    for (name, descriptor) in &dataset.manifest.inputs {
        ensure!(
            descriptor.path == format!("overrides/{region}/characters/{name}"),
            "補完の参照元が不正です"
        );
        let bytes = source.checked(descriptor)?;
        retain(
            connection,
            &descriptor.path,
            &descriptor.path,
            "override",
            &bytes,
        )?;
    }
    let buy = numeric_rows(&read_asset(
        source,
        dataset,
        connection,
        "Data/unitbuy.csv",
    )?)?;
    let growth = numeric_rows(&read_asset(
        source,
        dataset,
        connection,
        "Data/unitlevel.csv",
    )?)?;
    // 表示用の解釈とは別に原本を保存し、後続の再解釈へ渡す。
    for path in [
        "Data/SkillAcquisition.csv",
        "Data/SkillLevel.csv",
        "res/SkillDescriptions.csv",
        "Image/img015.png",
        "ImageData/img015.imgcut",
    ] {
        if dataset.files.contains_key(path) {
            read_asset(source, dataset, connection, path)?;
        }
    }
    for (position, unit) in dataset.characters.iter().enumerate() {
        let id: u32 = unit.id.parse()?;
        ensure!(
            !unit.forms.is_empty() && unit.forms.len() <= 4,
            "未知の形態数: {id}"
        );
        let settings = &buy.get(id as usize).context("unitbuyにIDなし")?.1;
        let rates = &growth.get(id as usize).context("unitlevelにIDなし")?.1;
        let rarity = required(settings, 13)?;
        connection.execute(
            "INSERT INTO unit VALUES (?,?,?,?,?,?,?,?)",
            params![
                region,
                id,
                rarity,
                unit.aliases.join(" "),
                required(settings, 50)?,
                required(settings, 51)?,
                false,
                unit.kind.as_deref().unwrap_or("normal")
            ],
        )?;
        for (index, rate) in rates.iter().enumerate() {
            connection.execute(
                "INSERT INTO growth VALUES (?,?,?,?)",
                params![region, id, index as i64, rate],
            )?;
        }
        let path = format!("Data/unit{:03}.csv", id + 1);
        let rows = numeric_rows(&read_asset(source, dataset, connection, &path)?)?;
        let explanation = format!("res/Unit_Explanation{}_ja.csv", id + 1);
        let explanations = if dataset.files.contains_key(&explanation) {
            crate::model::csv_rows(&read_asset(source, dataset, connection, &explanation)?)?
        } else {
            Vec::new()
        };
        ensure!(rows.len() >= unit.forms.len(), "数値CSVより多い形態: {id}");
        for (index, identity) in unit.forms.iter().enumerate() {
            let (cells, row) = &rows[index];
            let value = |column| row.get(column).copied().flatten();
            let code = ["f", "c", "s", "u"][index];
            let shared = if index < 2 {
                settings
                    .get(61 + index)
                    .copied()
                    .flatten()
                    .filter(|&id| id >= 0)
            } else {
                None
            };
            let asset_id = shared.unwrap_or(id as i64);
            let motion_code = if shared.is_some() { "m" } else { code };
            let motion_path = format!("ImageData/{asset_id:03}_{motion_code}02.maanim");
            let length = if dataset.files.contains_key(&motion_path) {
                animation_length(&read_asset(source, dataset, connection, &motion_path)?)?
            } else {
                None
            };
            let mut attacks = Vec::new();
            for (hit, damage_column) in [3, 59, 60].iter().enumerate() {
                let damage = value(*damage_column);
                if hit > 0 && !damage.is_some_and(|v| v > 0) {
                    continue;
                }
                let range_columns = if hit == 1 && value(99).is_some_and(|v| v != 0) {
                    (100, 101)
                } else if hit == 2 && value(102).is_some_and(|v| v != 0) {
                    (103, 104)
                } else {
                    (44, 45)
                };
                attacks.push(Attack {
                    damage: damage.context("第1攻撃値なし")?,
                    foreswing: value([13, 61, 62][hit]),
                    ability_enabled: value(63 + hit),
                    range: value(range_columns.0)
                        .zip(value(range_columns.1))
                        .map(|(start, width)| [start, start + width]),
                });
            }
            let pre = [value(13), value(61), value(62)]
                .into_iter()
                .flatten()
                .max()
                .context("攻撃発生なし")?;
            let interval = required(row, 4)?;
            let suffix = if shared.is_some() {
                format!("_m0{index}.png")
            } else {
                format!("_{code}00.png")
            };
            let icon = format!("Unit/uni{asset_id:03}{suffix}");
            let icon_path = if dataset.files.contains_key(&icon) {
                read_asset(source, dataset, connection, &icon)?;
                Some(icon)
            } else {
                None
            };
            let form = Form {
                region: region.clone(),
                unit_id: id,
                index,
                name: identity.name.clone(),
                description: explanations
                    .get(index)
                    .map(|cells| {
                        cells
                            .iter()
                            .skip(1)
                            .take(3)
                            .map(|value| crate::model::plain_text(value))
                            .filter(|value| !value.is_empty())
                            .collect::<Vec<_>>()
                            .join("\n")
                    })
                    .filter(|value| !value.is_empty())
                    .unwrap_or_else(|| identity.description.clone()),
                rarity,
                max_level: required(settings, 50)?,
                plus_level: required(settings, 51)?,
                is_spirit: false,
                icon_path,
                hp: required(row, 0)?,
                speed: required(row, 2)?,
                range: required(row, 5)?,
                cost: required(row, 6)?,
                respawn_raw: required(row, 7)?,
                knockbacks: required(row, 1)?,
                interval_raw: interval,
                area: required(row, 12)? != 0,
                attack_cycle: length.map(|length| (pre + interval * 2 - 1).max(length)),
                animation_length: length,
                attacks,
                properties: properties(row),
                raw: row.clone(),
                raw_cells: cells.clone(),
                growth: rates.clone(),
                source_path: path.clone(),
                name_source: if dataset.current.generated_path.starts_with("integrated/") {
                    explanation.clone()
                } else {
                    format!("{}/site/characters.json", dataset.current.generated_path)
                },
                motion_path,
            };
            store::insert_form(connection, &form, &unit.aliases.join(" "))?;
            *form_count += 1;
        }
        if position % 50 == 0 {
            progress(format!(
                "キャラ取り込み: {}/{}",
                position + 1,
                dataset.characters.len()
            ));
        }
    }
    connection.execute("UPDATE unit SET is_spirit=1 WHERE (region,id) IN (SELECT region,value FROM property_parameter WHERE key='spirit' AND position=0)", [])?;
    crate::talents::import(connection, region)?;
    crate::progression::import(source, dataset, connection, progress)?;
    crate::combos::import(source, dataset, connection)?;
    crate::enemies::import(source, dataset, connection, progress)?;
    crate::stages::import(source, dataset, connection, progress)?;
    crate::motions::import(source, dataset, connection, progress)?;
    crate::effects::import(source, dataset, connection, progress)?;
    crate::stage_media::import(source, dataset, connection, progress)?;
    ensure!(*form_count > 0, "取り込み結果が空です");
    Ok(())
}
