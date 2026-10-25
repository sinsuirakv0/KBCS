#![cfg_attr(windows, windows_subsystem = "windows")]

#[cfg(windows)]
mod desktop;
mod motion_pose;
mod scene;
mod service;

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
        Some("verify") => {
            let database = Database::open(&root, &region)?;
            kbcs_data::store::validate(&database.connection)?;
            println!("{}", serde_json::to_string_pretty(&database.metadata()?)?);
            println!("C++ ABI: {}", kbcs_bridge::abi_version());
        }
        Some("--help") | Some("help") => println!(
            "kbcs [import|list|show|verify|catalog|motion|scene|preview] [--assets PATH_OR_GITHUB_URL] [--data-dir PATH] [--region jp] [--query TEXT] [--id N] [--form 0..3]\nコマンド省略でGUIを起動します。"
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
                let value = scenes.get_mut(&key).unwrap().draw(&database, &input)?;
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
                Some("stages") => kbcs_data::stages::catalog(&database, &region)?,
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
