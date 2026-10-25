use crate::{
    import::read_asset,
    source::{Dataset, Source},
    store::Database,
};
use anyhow::{Context, Result, ensure};
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

fn text(database: &Database, path: &str) -> Result<String> {
    Ok(String::from_utf8(database.source(path)?.3)?)
}
fn basename(path: &str) -> &str {
    path.rsplit('/').next().unwrap_or(path)
}
fn definition(bytes: &[u8]) -> Result<Value> {
    let text = std::str::from_utf8(bytes)?
        .trim_start_matches('\u{feff}')
        .trim();
    // bg1001.jsonの空原本は、追加演出なしとして保存する。
    Ok(if text.is_empty() {
        json!({})
    } else {
        serde_json::from_str(text)?
    })
}
pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &rusqlite::Connection,
    progress: &(impl Fn(String) + Sync),
) -> Result<()> {
    if !dataset.files.contains_key("Data/bg.csv") {
        return Ok(());
    }
    let mut wanted = BTreeSet::new();
    for path in dataset.files.keys() {
        let name = basename(path);
        let castle = ["ec", "wc", "sc", "rc"].iter().any(|prefix| {
            name.strip_prefix(prefix).is_some_and(|v| {
                v.len() == 7 && v.bytes().take(3).all(|b| b.is_ascii_digit()) && v.ends_with(".png")
            })
        });
        if path == "Data/bg.csv"
            || path.starts_with("Data/bg") && path.ends_with(".json")
            || path.starts_with("Data/enemyCastleData") && path.ends_with(".csv")
            || path.ends_with(".png")
                && (name.starts_with("bg")
                    || name.starts_with("nyankoCastle_")
                    || castle
                    || ["bubble02.png", "bubble03_bg040.png"].contains(&name))
            || path.starts_with("ImageData/bg")
                && [".imgcut", ".mamodel", ".maanim"]
                    .iter()
                    .any(|e| path.ends_with(e))
        {
            wanted.insert(path.clone());
        }
    }
    // JSONに明示された依存だけを追加し、制作環境の絶対パスを追わない。
    let definitions: Vec<_> = wanted
        .iter()
        .filter(|p| p.ends_with(".json"))
        .cloned()
        .collect();
    source.prefetch(dataset, &definitions, progress)?;
    for path in definitions {
        let value = definition(&read_asset(source, dataset, connection, &path)?)?;
        for segment in value["data"].as_array().into_iter().flatten() {
            for name in segment["file"]
                .as_object()
                .into_iter()
                .flat_map(|v| v.values())
                .filter_map(Value::as_str)
            {
                ensure!(!name.contains(['/', '\\', ':']), "背景素材名が不正です");
                for prefix in ["ImageData/", "Image/", "Number/"] {
                    let path = format!("{prefix}{name}");
                    if dataset.files.contains_key(&path) {
                        wanted.insert(path);
                        break;
                    }
                }
            }
        }
    }
    let pending = wanted
        .into_iter()
        .filter_map(|path| {
            match connection.query_row(
                "SELECT EXISTS(SELECT 1 FROM source_file WHERE path=?)",
                [&path],
                |r| r.get::<_, bool>(0),
            ) {
                Ok(false) => Some(Ok(path)),
                Ok(true) => None,
                Err(e) => Some(Err(e)),
            }
        })
        .collect::<rusqlite::Result<Vec<_>>>()?;
    source.prefetch(dataset, &pending, progress)?;
    for path in &pending {
        read_asset(source, dataset, connection, path)?;
    }
    progress(format!("ステージ背景・城: {}原本を追加", pending.len()));
    Ok(())
}
pub fn cuts(database: &Database, path: &str) -> Result<Vec<[i32; 4]>> {
    text(database, path)?
        .trim_start_matches('\u{feff}')
        .lines()
        .skip(4)
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            let cells = line
                .split(',')
                .take(4)
                .map(|v| v.trim().parse::<i32>())
                .collect::<std::result::Result<Vec<_>, _>>()?;
            cells
                .try_into()
                .map_err(|_| anyhow::anyhow!("背景の分割列が不足しています"))
        })
        .collect()
}
pub fn numeric_rows(bytes: &[u8]) -> Result<Vec<(usize, Vec<Option<i64>>)>> {
    Ok(crate::stages::rows(bytes, None)?
        .into_iter()
        .map(|(row, _, values)| (row, values))
        .collect())
}
fn numbers(database: &Database, path: &str) -> Result<Vec<Vec<i64>>> {
    Ok(numeric_rows(&database.source(path)?.3)?
        .into_iter()
        .map(|(_, values)| values.into_iter().map(|v| v.unwrap_or(0)).collect())
        .collect())
}
pub fn background(database: &Database, id: i64) -> Result<Value> {
    let row = numbers(database, "Data/bg.csv")?
        .into_iter()
        .find(|row| row.first() == Some(&id))
        .context("背景定義がありません。データを更新してください")?;
    ensure!(row.len() >= 15, "背景定義の列が不足しています");
    let image = row.get(15).copied().filter(|id| *id >= 0).unwrap_or(id);
    let cuts = cuts(database, &format!("ImageData/bg{:02}.imgcut", row[13]))?;
    let mut overlay = if row.len() >= 20 {
        json!({"start":&row[16..19],"end":if row.len()>=24 {&row[20..23]}else{&row[16..19]},"alpha":row[19]})
    } else {
        Value::Null
    };
    let fixed = match id {
        13 => Some(([0, 226, 255], [255, 255, 255], 51)),
        15 => Some(([0, 73, 173], [66, 187, 255], 51)),
        19 => Some(([160, 33, 32], [240, 169, 54], 51)),
        46 | 47 => Some(([255, 255, 255], [255, 255, 255], 67)),
        71 => Some(([145, 45, 5], [235, 160, 60], 51)),
        72 => Some(([0, 35, 125], [0, 0, 0], 51)),
        73 => Some(([15, 30, 120], [60, 135, 5], 51)),
        156 => Some(([255, 255, 255], [255, 255, 255], 51)),
        167 => Some(([175, 104, 104], [137, 104, 88], 76)),
        168 => Some(([49, 73, 97], [68, 75, 77], 76)),
        _ => None,
    };
    if let Some((start, end, alpha)) = fixed {
        overlay = json!({"start":start,"end":end,"alpha":alpha});
    }
    Ok(
        json!({"id":id,"path":format!("Image/bg{image:03}.png"),"colors":[&row[1..4],&row[4..7],&row[7..10],&row[10..13]],"cut":cuts.first(),"top":if row[14]==1 {cuts.get(20)}else{None},"overlay":overlay,"raw":row}),
    )
}
pub fn scene_source(database: &Database, id: i64) -> Result<Value> {
    let mut files = BTreeMap::new();
    let mut names = BTreeSet::new();
    let mut seen = BTreeSet::new();
    let mut next = Some(id);
    files.insert("Data/bg.csv".to_owned(), text(database, "Data/bg.csv")?);
    while let Some(id) = next.take() {
        ensure!(seen.insert(id), "背景定義の参照が循環しています");
        let path = format!("Data/bg{id:03}.json");
        if let Ok(content) = text(database, &path) {
            let value = definition(content.as_bytes())?;
            next = value["id"].as_i64();
            for segment in value["data"].as_array().into_iter().flatten() {
                for name in segment["file"]
                    .as_object()
                    .into_iter()
                    .flat_map(|v| v.values())
                    .filter_map(Value::as_str)
                {
                    names.insert(name.to_owned());
                }
            }
            files.insert(path, content);
        }
    }
    let mut statement=database.connection.prepare("SELECT path FROM source_file WHERE path GLOB 'ImageData/bg*' OR path GLOB 'Image/bg*' OR path GLOB 'Number/bg*' OR path GLOB '*nyankoCastle*' OR path='ImageData/000_a.imgcut'")?;
    let mut paths = statement
        .query_map([], |r| r.get::<_, String>(0))?
        .collect::<rusqlite::Result<BTreeSet<_>>>()?;
    for name in names {
        for prefix in ["ImageData/", "Image/", "Number/"] {
            let path = format!("{prefix}{name}");
            if let Ok(content) = database.source(&path) {
                paths.insert(path.clone());
                if !path.ends_with(".png") {
                    files.insert(path, String::from_utf8(content.3)?);
                }
                break;
            }
        }
    }
    for row in numbers(database, "Data/bg.csv")? {
        if !seen.contains(&row[0]) {
            continue;
        }
        let prefix = format!("ImageData/bg{:02}", row[13]);
        for path in &paths {
            if path.starts_with(&prefix) && !path.ends_with(".png") {
                files.insert(path.clone(), text(database, path)?);
            }
        }
    }
    for set in ["0", "1", "2", "Legend"] {
        let path = format!("Data/enemyCastleData{set}.csv");
        if let Ok(content) = text(database, &path) {
            files.insert(path, content);
        }
    }
    if let Ok(content) = text(database, "ImageData/000_a.imgcut") {
        files.insert("ImageData/000_a.imgcut".into(), content);
    }
    Ok(
        json!({"metadata":database.metadata()?,"background":background(database,id)?,"files":files,"paths":paths}),
    )
}
pub fn music() -> Value {
    serde_json::from_str(
        include_str!("../resources/stage-music.json").trim_start_matches('\u{feff}'),
    )
    .expect("同梱音源索引")
}
pub struct Audio {
    pub mime: &'static str,
    pub bytes: Vec<u8>,
}
pub fn audio(root: &std::path::Path, id: i64) -> Result<Audio> {
    let catalog = music();
    let track = &catalog["tracks"][id.to_string()];
    let url = track["url"].as_str().context("音源未収録です")?;
    let revision = track["revision"]
        .as_str()
        .or_else(|| catalog["revision"].as_str())
        .context("音源版なし")?;
    let (mime, extension) = match track["mime"].as_str() {
        Some("audio/ogg") => ("audio/ogg", "ogg"),
        None | Some("audio/mpeg") => ("audio/mpeg", "mp3"),
        _ => anyhow::bail!("未対応の音源形式です"),
    };
    let valid = |bytes: &[u8]| {
        let header = if extension == "ogg" {
            bytes.starts_with(b"OggS")
        } else {
            bytes.starts_with(b"ID3") || bytes.first() == Some(&0xff)
        };
        header
            && track["size"]
                .as_u64()
                .is_none_or(|size| bytes.len() as u64 == size)
            && track["sha256"]
                .as_str()
                .is_none_or(|sha| crate::source::hash(bytes) == sha)
    };
    let directory = root.join("assets/music").join(revision);
    std::fs::create_dir_all(&directory)?;
    let path = directory.join(format!("{id:03}.{extension}"));
    let receipt = directory.join(format!("{id:03}.sha256"));
    if let Ok(bytes) = std::fs::read(&path)
        && valid(&bytes)
        && (track["sha256"].is_string()
            || std::fs::read_to_string(&receipt)
                .is_ok_and(|sha| sha == crate::source::hash(&bytes)))
    {
        return Ok(Audio { mime, bytes });
    }
    let agent: ureq::Agent = ureq::Agent::config_builder()
        .timeout_global(Some(std::time::Duration::from_secs(60)))
        .build()
        .into();
    let bytes = agent
        .get(url)
        .call()?
        .body_mut()
        .with_config()
        .limit(32 * 1024 * 1024)
        .read_to_vec()?;
    ensure!(
        valid(&bytes),
        "音源の形式・サイズ・SHA-256が一致しません: {id}"
    );
    let temporary = directory.join(format!("{id:03}-{}.tmp", std::process::id()));
    std::fs::write(&temporary, &bytes)?;
    std::fs::rename(temporary, &path)?;
    std::fs::write(receipt, crate::source::hash(&bytes))?;
    Ok(Audio { mime, bytes })
}

pub(crate) fn annotate(stage: &mut Value, series: &str) {
    let index = stage["index"].as_u64().unwrap_or(0) as usize;
    let order: Vec<i64> = (0..46).rev().chain([46, 47, 45, 47, 47, 45, 45]).collect();
    let settings = stage["rawSettings"].as_array();
    let explicit = settings
        .and_then(|a| a.first())
        .and_then(Value::as_str)
        .and_then(|s| s.parse::<i64>().ok())
        .filter(|v| *v >= 0);
    stage["castle"] = json!(explicit.or_else(|| order.get(index).copied()));
    stage["castleSet"] = json!(match series {
        "EOC" | "EOCZ" => 0,
        "ITF" | "ITFZ" => 1,
        "COTC" | "COTCZ" => 2,
        _ => 3,
    });
    let raw = stage["rawRewards"].as_array();
    let get = |i: usize| {
        raw.and_then(|a| a.get(i))
            .and_then(Value::as_str)
            .and_then(|s| s.parse::<i64>().ok())
    };
    let mut tracks = Vec::new();
    if let Some(id) = get(2).filter(|id| *id >= 0) {
        tracks.push(json!({"id":id,"threshold":null}));
    }
    if let (Some(threshold), Some(id)) = (get(3), get(4))
        && threshold > 0
        && threshold < 100
        && Some(id) != get(2)
        && id >= 0
    {
        tracks.push(json!({"id":id,"threshold":threshold}));
    }
    stage["musicTracks"] = json!(tracks);
}

pub fn image_size(database: &Database, path: &str) -> Result<[i32; 2]> {
    let header: Vec<u8> = database.connection.query_row(
        "SELECT substr(bytes,1,24) FROM source_file WHERE path=?",
        [path],
        |row| row.get(0),
    )?;
    ensure!(
        header.len() == 24 && header.starts_with(b"\x89PNG\r\n\x1a\n"),
        "PNGヘッダーが不正です"
    );
    Ok([
        i32::try_from(u32::from_be_bytes(header[16..20].try_into()?))?,
        i32::try_from(u32::from_be_bytes(header[20..24].try_into()?))?,
    ])
}
