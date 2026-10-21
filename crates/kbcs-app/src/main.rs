#![cfg_attr(windows, windows_subsystem = "windows")]

#[cfg(windows)]
mod desktop;
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
    let source = option("--assets").unwrap_or_else(|| "../KBC-rakv0-assets".into());
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
            "kbcs [import|list|show|verify|catalog|preview] [--assets PATH_OR_GITHUB_URL] [--data-dir PATH] [--region jp] [--query TEXT] [--id N] [--form 0..3]\nコマンド省略でGUIを起動します。"
        ),
        Some("preview") => service::serve(
            root,
            region,
            source,
            &option("--bind").unwrap_or_else(|| "127.0.0.1:4817".into()),
        )?,
        Some("catalog") => {
            let database = Database::open(&root, &region)?;
            let value = match option("--kind").as_deref() {
                None | Some("units") => kbcs_data::view::catalog(&database, &region)?,
                Some("enemies") => kbcs_data::enemies::catalog(&database, &region)?,
                Some("stages") => kbcs_data::stages::catalog(&database, &region)?,
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
