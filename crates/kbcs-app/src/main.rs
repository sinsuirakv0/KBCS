#![cfg_attr(windows, windows_subsystem = "windows")]

mod battle;
mod battle_rewards;
mod battle_wire;
mod cache;
#[cfg(windows)]
mod desktop;
mod motion_pose;
mod runtime;
mod scene;
mod service;
mod workers;

use anyhow::{Context, Result};
use kbcs_data::{import, store::Database};
use std::path::PathBuf;

#[cfg(windows)]
#[link(name = "kernel32")]
unsafe extern "system" {
    fn AttachConsole(process_id: u32) -> i32;
}

fn default_data_dir() -> PathBuf {
    std::env::var_os("KBCS_DATA_DIR")
        .map(PathBuf::from)
        .unwrap_or_else(|| {
            std::env::var_os("LOCALAPPDATA")
                .map(PathBuf::from)
                .unwrap_or_else(|| PathBuf::from(".local"))
                .join("KBCS")
        })
}

fn main() -> Result<()> {
    let arguments: Vec<String> = std::env::args().skip(1).collect();
    #[cfg(windows)]
    if !arguments.is_empty() {
        // CLIだけ親のコンソールへ接続し、GUI起動時は余分な窓を作らない。
        unsafe {
            AttachConsole(u32::MAX);
        }
    }
    let option = |key: &str| {
        arguments
            .iter()
            .position(|argument| argument == key)
            .and_then(|index| arguments.get(index + 1))
            .cloned()
    };
    let root = option("--data-dir")
        .map(PathBuf::from)
        .unwrap_or_else(default_data_dir);
    let region = option("--region").unwrap_or_else(|| "jp".into());
    let source = option("--assets").unwrap_or_else(|| kbcs_data::DEFAULT_SOURCE.into());
    match arguments.first().map(String::as_str) {
        Some("import") => println!(
            "{}",
            serde_json::to_string_pretty(&import::import(
                &source,
                &root,
                &region,
                |message| eprintln!("{message}")
            )?)?
        ),
        Some("list") => {
            let database = Database::open(&root, &region)?;
            for unit in database.search(&region, &option("--query").unwrap_or_default(), false)? {
                println!("{}\t{}\t{}形態", unit.id, unit.name, unit.forms);
            }
        }
        Some("show") => {
            let database = Database::open(&root, &region)?;
            let id = option("--id").context("--idが必要です")?.parse()?;
            let form = option("--form").unwrap_or_else(|| "0".into()).parse()?;
            println!(
                "{}",
                serde_json::to_string_pretty(&database.form(&region, id, form)?)?
            );
        }
        Some("battle-replay") => {
            let input: serde_json::Value = serde_json::from_str(
                std::fs::read_to_string(option("--input").context("--inputが必要です")?)?
                    .trim_start_matches('\u{feff}'),
            )?;
            let mut service = service::Service::new(root, region, source);
            service.persist_rewards = false;
            let reply = service.handle(
                "POST",
                "/api/battle-session",
                &serde_json::to_vec(&input["start"])?,
            );
            anyhow::ensure!(
                reply.status == 200,
                "{}",
                String::from_utf8_lossy(&reply.bytes)
            );
            if arguments.iter().any(|s| s == "--validate-assets") {
                let start: serde_json::Value = serde_json::from_slice(&reply.bytes)?;
                for path in start["textures"]
                    .as_array()
                    .context("画像一覧なし")?
                    .iter()
                    .chain(start["title"].get("image"))
                {
                    // 予約済みの空テクスチャ枠は取得対象に含めない。
                    if path.is_null() {
                        continue;
                    }
                    let path = path.as_str().context("画像パスなし")?;
                    let image = service.handle("GET", &format!("/api/asset/{path}"), &[]);
                    anyhow::ensure!(
                        image.status == 200 && image.bytes.starts_with(b"\x89PNG\r\n\x1a\n"),
                        "戦闘画像: {path}: {}",
                        String::from_utf8_lossy(&image.bytes[..image.bytes.len().min(200)])
                    );
                }
            }
            let mut results = Vec::new();
            for (index, request) in input["requests"]
                .as_array()
                .context("requestsが必要です")?
                .iter()
                .enumerate()
            {
                let reply = service.handle(
                    "POST",
                    "/api/battle-session/frame",
                    &serde_json::to_vec(request)?,
                );
                anyhow::ensure!(
                    reply.status == 200,
                    "request {index}: {} / previous {}",
                    String::from_utf8_lossy(&reply.bytes),
                    results
                        .last()
                        .map(|value: &serde_json::Value| value["state"]["frame"].to_string())
                        .unwrap_or_default()
                );
                let mut frame: serde_json::Value = serde_json::from_slice(&reply.bytes)?;
                let count = frame["scene"]["commands"].as_array().map_or(0, Vec::len);
                frame["scene"] = serde_json::json!({"commands":count});
                results.push(frame);
            }
            println!("{}", serde_json::to_string(&results)?);
        }
        Some("verify") => {
            let database = Database::open(&root, &region)?;
            kbcs_data::store::validate(&database.connection)?;
            println!("{}", serde_json::to_string_pretty(&database.metadata()?)?);
            println!("C++ ABI: {}", kbcs_bridge::abi_version());
        }
        Some("--help") | Some("help") => println!(
            "kbcs [import|list|show|verify|catalog|motion|scene|preview|battle-replay] [--assets PATH_OR_GITHUB_URL] [--data-dir PATH] [--region jp] [--query TEXT] [--id N] [--form 0..3]\nコマンド省略でGUIを起動します。"
        ),
        Some("preview") => service::serve(
            root,
            region,
            source,
            &option("--bind").unwrap_or_else(|| "127.0.0.1:4817".into()),
        )?,
        Some("scene") => {
            let database = Database::open(&root, &region)?;
            let inputs: Vec<scene::Input> = serde_json::from_slice(&std::fs::read(
                option("--input").context("--inputに描画条件のJSON配列を指定してください")?,
            )?)?;
            let mut scenes = std::collections::BTreeMap::new();
            for input in inputs {
                let key = input.key();
                if !scenes.contains_key(&key) {
                    scenes.insert(key.clone(), scene::Scene::new(&database, &input)?);
                }
                let value =
                    serde_json::to_value(scenes.get_mut(&key).unwrap().draw(&database, &input)?)?;
                let value = if arguments.iter().any(|s| s == "--summary") {
                    serde_json::json!({"background":input.background,"frame":input.frame,
                        "commands":value["commands"].as_array().map(Vec::len),
                        "missing":value["missing"],"issues":value["issues"],"core":value["core"]})
                } else {
                    value
                };
                println!("{}", serde_json::to_string(&value)?);
                if scenes.len() > 16 {
                    scenes.clear();
                }
            }
        }
        Some("motion") => {
            let database = Database::open(&root, &region)?;
            let value = if option("--kind").as_deref() == Some("effect") {
                kbcs_data::effects::manifest(
                    &database,
                    &option("--id").unwrap_or_else(|| "skill_wave_attack".into()),
                )?
            } else {
                kbcs_data::motions::manifest(
                    &database,
                    &region,
                    &option("--kind").unwrap_or_else(|| "unit".into()),
                    option("--id").unwrap_or_else(|| "0".into()).parse()?,
                    option("--form").unwrap_or_else(|| "0".into()).parse()?,
                )?
            };
            println!("{}", serde_json::to_string(&value)?);
        }
        Some("catalog") => {
            let database = Database::open(&root, &region)?;
            let value = match option("--kind").as_deref() {
                None | Some("units") => kbcs_data::view::catalog(&database, &region)?,
                Some("enemies") => kbcs_data::enemies::catalog(&database, &region)?,
                Some("stages") => {
                    kbcs_data::stages::catalog_map(&database, &region, option("--map").as_deref())?
                }
                Some("stage-index") => kbcs_data::stages::search_catalog(&database, &region)?,
                Some("effects") => kbcs_data::effects::catalog(&database)?,
                Some(value) => anyhow::bail!("未知のデータ種別: {value}"),
            };
            println!("{}", serde_json::to_string(&value)?);
        }
        Some(value) if !value.starts_with("--") => anyhow::bail!("未知のコマンド: {value}"),
        _ => {
            #[cfg(windows)]
            desktop::run(root, region, source)?;
            #[cfg(not(windows))]
            anyhow::bail!("GUIは現在Windows専用です。previewコマンドでブラウザから閲覧できます");
        }
    }
    Ok(())
}
