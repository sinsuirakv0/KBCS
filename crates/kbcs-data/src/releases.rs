use crate::source::{Descriptor, Header, hash, parse_json, safe_path};
use anyhow::{Context, Result, ensure};
pub use semver::Version;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs::{self, File, OpenOptions},
    io::{Read, Write},
    path::{Path, PathBuf},
    time::Duration,
};

pub const DATA_REPOSITORY: &str = "sinsuirakv0/KBC-rakv0-assets";
pub const APP_REPOSITORY: &str = "sinsuirakv0/KBCS";

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Asset {
    pub name: String,
    pub size: u64,
    pub browser_download_url: String,
    pub digest: Option<String>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Release {
    pub tag_name: String,
    pub published_at: String,
    pub html_url: String,
    pub draft: bool,
    pub assets: Vec<Asset>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Archive {
    pub file: String,
    pub size: u64,
    pub sha256: String,
    pub file_count: usize,
    pub uncompressed_size: u64,
    pub url: String,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Manifest {
    pub schema_version: u32,
    pub header: Header,
    pub revision: String,
    pub repository: String,
    pub tag: String,
    pub archives: BTreeMap<String, Archive>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct DataRelease {
    pub release: Release,
    pub manifest: Manifest,
}

#[derive(Serialize, Deserialize)]
pub struct Installed {
    pub release: DataRelease,
    pub files: BTreeMap<String, Descriptor>,
}

fn agent(timeout: Duration) -> ureq::Agent {
    ureq::Agent::config_builder()
        .timeout_global(Some(timeout))
        .timeout_connect(Some(Duration::from_secs(20)))
        .timeout_recv_response(Some(Duration::from_secs(60)))
        // recv_bodyは無通信時間ではなく本文全体の期限。大容量ZIPはglobalだけで制限する。
        .timeout_recv_body(None)
        .build()
        .into()
}

fn json<T: serde::de::DeserializeOwned>(url: &str) -> Result<T> {
    let bytes = agent(Duration::from_secs(30))
        .get(url)
        .header("User-Agent", "KBCS")
        .header("Accept", "application/vnd.github+json")
        .call()?
        .body_mut()
        .with_config()
        .limit(8 * 1024 * 1024)
        .read_to_vec()?;
    parse_json(&bytes)
}

fn list(repository: &str) -> Result<Vec<Release>> {
    json(&format!(
        "https://api.github.com/repos/{repository}/releases?per_page=100"
    ))
}

fn asset_url(url: &str, repository: &str, tag: &str, name: &str) -> Result<()> {
    safe_path(tag)?;
    safe_path(name)?;
    ensure!(!tag.contains('/') && !name.contains('/'), "不正な配布名");
    ensure!(
        url == format!("https://github.com/{repository}/releases/download/{tag}/{name}"),
        "配布URLがリリースと一致しません"
    );
    Ok(())
}

pub fn latest_data(region: &str) -> Result<DataRelease> {
    ensure!(["jp", "en", "kr", "tw"].contains(&region), "未知の地域");
    let prefix = format!("integrated-{region}-");
    let release = list(DATA_REPOSITORY)?
        .into_iter()
        .filter(|r| !r.draft && r.tag_name.starts_with(&prefix))
        .max_by(|a, b| a.published_at.cmp(&b.published_at))
        .context("統合データの公開リリースがありません")?;
    let asset = release
        .assets
        .iter()
        .find(|a| a.name == "manifest.json")
        .context("統合データのmanifest.jsonがありません")?;
    asset_url(
        &asset.browser_download_url,
        DATA_REPOSITORY,
        &release.tag_name,
        &asset.name,
    )?;
    let bytes = agent(Duration::from_secs(30))
        .get(&asset.browser_download_url)
        .call()?
        .body_mut()
        .with_config()
        .limit(1024 * 1024)
        .read_to_vec()?;
    check_bytes(&bytes, asset.size, digest(asset)?)?;
    let manifest: Manifest = parse_json(&bytes)?;
    validate_manifest(&manifest, &release, region)?;
    Ok(DataRelease { release, manifest })
}

fn validate_manifest(manifest: &Manifest, release: &Release, region: &str) -> Result<()> {
    ensure!(
        manifest.schema_version == 1
            && manifest.header.schema_version == 1
            && manifest.repository == DATA_REPOSITORY
            && manifest.tag == release.tag_name
            && manifest.header.source_region == region,
        "統合データの版・地域・形式が一致しません"
    );
    ensure!(
        manifest.revision.len() == 40 && manifest.revision.bytes().all(|b| b.is_ascii_hexdigit()),
        "不正な原本commit"
    );
    // 公開manifestの全ZIPを対象とする。未知の追加フォルダも同じ契約で検証する。
    ensure!(
        !manifest.archives.is_empty() && manifest.archives.len() <= 64,
        "ZIP一覧が不正です"
    );
    for folder in [
        "Data",
        "res",
        "Image",
        "ImageData",
        "Unit",
        "Map",
        "Number",
        "assets",
        "music",
        "Download",
    ] {
        ensure!(
            manifest.archives.contains_key(folder),
            "必須ZIPがありません: {folder}"
        );
    }
    for (folder, archive) in &manifest.archives {
        safe_path(folder)?;
        ensure!(
            !folder.contains('/')
                && archive.file == format!("{folder}.zip")
                && archive.size > 0
                && archive.uncompressed_size <= 8 * 1024 * 1024 * 1024
                && archive.file_count <= 500_000,
            "ZIP定義が不正です: {folder}"
        );
        asset_url(
            &archive.url,
            DATA_REPOSITORY,
            &release.tag_name,
            &archive.file,
        )?;
        let asset = release
            .assets
            .iter()
            .find(|a| a.name == archive.file)
            .context("manifestのZIPがリリースにありません")?;
        ensure!(
            asset.size == archive.size && digest(asset)? == archive.sha256,
            "ZIPの配布情報が一致しません"
        );
    }
    Ok(())
}

pub fn app_version(tag: &str) -> Option<semver::Version> {
    semver::Version::parse(tag.strip_prefix("kbcs-v")?).ok()
}

pub fn latest_app() -> Result<Option<Release>> {
    Ok(latest_app_for(
        list(APP_REPOSITORY)?,
        std::env::consts::OS,
        std::env::consts::ARCH,
    ))
}

fn latest_app_for(releases: Vec<Release>, os: &str, architecture: &str) -> Option<Release> {
    // 本体の開発版は公開対象。native-v等の解析資料は対象外。
    releases
        .into_iter()
        .filter(|r| {
            !r.draft
                && app_version(&r.tag_name).is_some()
                && app_asset_name(&r.tag_name, os, architecture).is_ok_and(|name| {
                    r.assets
                        .iter()
                        .any(|a| a.name == name && a.size > 0 && digest(a).is_ok())
                })
        })
        .max_by_key(|r| app_version(&r.tag_name))
}

pub fn app_asset_name(tag: &str, os: &str, architecture: &str) -> Result<String> {
    let version = app_version(tag).context("本体の版が不正です")?;
    let platform = match (os, architecture) {
        ("windows", "x86_64") => "windows-x64",
        ("macos", "aarch64") => "macos-arm64",
        ("macos", "x86_64") => "macos-x64",
        _ => anyhow::bail!("本体更新は未対応の環境です: {os}/{architecture}"),
    };
    Ok(format!("KBCS-{version}-{platform}.zip"))
}

pub fn app_asset(release: &Release) -> Result<&Asset> {
    let name = app_asset_name(
        &release.tag_name,
        std::env::consts::OS,
        std::env::consts::ARCH,
    )?;
    let asset = release
        .assets
        .iter()
        .find(|a| a.name == name)
        .with_context(|| format!("この環境用のZIPがありません: {name}"))?;
    asset_url(
        &asset.browser_download_url,
        APP_REPOSITORY,
        &release.tag_name,
        &asset.name,
    )?;
    digest(asset)?;
    Ok(asset)
}

pub fn digest(asset: &Asset) -> Result<&str> {
    let sha = asset
        .digest
        .as_deref()
        .and_then(|v| v.strip_prefix("sha256:"))
        .context("配布ファイルのSHA-256がありません")?;
    ensure!(
        sha.len() == 64 && sha.bytes().all(|b| b.is_ascii_hexdigit()),
        "不正なSHA-256"
    );
    Ok(sha)
}

fn check_bytes(bytes: &[u8], size: u64, sha: &str) -> Result<()> {
    ensure!(
        bytes.len() as u64 == size && hash(bytes) == sha,
        "サイズ・SHA-256が一致しません"
    );
    Ok(())
}

fn file_hash(path: &Path) -> Result<(u64, String)> {
    let mut file = File::open(path)?;
    let mut hasher = Sha256::new();
    let mut count = 0;
    let mut buffer = vec![0; 128 * 1024];
    loop {
        let length = file.read(&mut buffer)?;
        if length == 0 {
            break;
        }
        hasher.update(&buffer[..length]);
        count += length as u64;
    }
    Ok((count, format!("{:x}", hasher.finalize())))
}

pub fn download(asset: &Asset, directory: &Path, progress: &impl Fn(String)) -> Result<PathBuf> {
    download_with_agent(
        asset,
        directory,
        progress,
        &agent(Duration::from_secs(1800)),
    )
}

fn retryable(error: &ureq::Error) -> bool {
    match error {
        ureq::Error::Timeout(_)
        | ureq::Error::HostNotFound
        | ureq::Error::ConnectionFailed
        | ureq::Error::StatusCode(408 | 429 | 500..=599) => true,
        ureq::Error::Io(error) => matches!(
            error.kind(),
            std::io::ErrorKind::TimedOut
                | std::io::ErrorKind::UnexpectedEof
                | std::io::ErrorKind::ConnectionAborted
                | std::io::ErrorKind::ConnectionReset
                | std::io::ErrorKind::ConnectionRefused
                | std::io::ErrorKind::NotConnected
                | std::io::ErrorKind::Interrupted
                | std::io::ErrorKind::BrokenPipe
        ),
        _ => false,
    }
}

fn download_with_agent(
    asset: &Asset,
    directory: &Path,
    progress: &impl Fn(String),
    agent: &ureq::Agent,
) -> Result<PathBuf> {
    let sha = digest(asset)?;
    fs::create_dir_all(directory)?;
    let path = directory.join(format!("{sha}.zip"));
    if file_hash(&path).is_ok_and(|(size, value)| size == asset.size && value == sha) {
        progress(format!("取得済み: {}", asset.name));
        return Ok(path);
    }
    let temporary = path.with_extension("part");
    for attempt in 1..=3 {
        let result = (|| -> Result<()> {
            let mut response = agent
                .get(&asset.browser_download_url)
                .header("User-Agent", "KBCS")
                .call()?;
            let mut reader = response.body_mut().as_reader();
            let mut file = File::create(&temporary)?;
            let mut hasher = Sha256::new();
            let mut received = 0;
            let mut reported = std::time::Instant::now();
            let mut buffer = vec![0; 128 * 1024];
            loop {
                // 通信エラーだけを再試行し、ディスク書込みや検証失敗は繰り返さない。
                let length = reader.read(&mut buffer).map_err(ureq::Error::from)?;
                if length == 0 {
                    if received < asset.size {
                        return Err(ureq::Error::Io(std::io::Error::new(
                            std::io::ErrorKind::UnexpectedEof,
                            "ZIPの受信中に接続が終了しました",
                        ))
                        .into());
                    }
                    break;
                }
                received += length as u64;
                ensure!(received <= asset.size, "配布サイズを超過しました");
                file.write_all(&buffer[..length])?;
                hasher.update(&buffer[..length]);
                if reported.elapsed() >= Duration::from_millis(250) {
                    progress(format!(
                        "ダウンロード: {} / {:.1} / {:.1} MB",
                        asset.name,
                        received as f64 / 1048576.,
                        asset.size as f64 / 1048576.
                    ));
                    reported = std::time::Instant::now();
                }
            }
            ensure!(
                received == asset.size && format!("{:x}", hasher.finalize()) == sha,
                "ダウンロードのサイズ・SHA-256不一致: {}",
                asset.name
            );
            file.sync_all()?;
            drop(file);
            fs::rename(&temporary, &path)?;
            Ok(())
        })();
        match result {
            Ok(()) => return Ok(path),
            Err(error) => {
                let _ = fs::remove_file(&temporary);
                if attempt == 3 || !error.downcast_ref::<ureq::Error>().is_some_and(retryable) {
                    return Err(error).with_context(|| {
                        format!(
                            "ダウンロードに失敗しました: {}（{attempt}/3回）",
                            asset.name
                        )
                    });
                }
                progress(format!(
                    "通信を再試行します（{}/3回）: {} / {error}",
                    attempt + 1,
                    asset.name
                ));
                std::thread::sleep(Duration::from_secs(attempt));
            }
        }
    }
    unreachable!()
}

// Windowsでも別名へ正規化されないパスだけを許可し、symlinkは展開しない。
fn zip_path(name: &str) -> Result<&str> {
    safe_path(name)?;
    for part in name.split('/') {
        let stem = part
            .split('.')
            .next()
            .unwrap_or_default()
            .to_ascii_uppercase();
        ensure!(
            !part.ends_with(['.', ' '])
                && !part.contains(['<', '>', '"', '|', '*'])
                && !part.chars().any(char::is_control)
                && !["CON", "PRN", "AUX", "NUL"].contains(&stem.as_str())
                && !(stem.len() == 4
                    && (stem.starts_with("COM") || stem.starts_with("LPT"))
                    && matches!(stem.as_bytes()[3], b'1'..=b'9')),
            "不正なZIPパス: {name}"
        );
    }
    Ok(name)
}

pub fn extract(
    path: &Path,
    target: &Path,
    folder: Option<&str>,
    max_bytes: u64,
    max_files: usize,
    progress: &impl Fn(String),
) -> Result<BTreeMap<String, Descriptor>> {
    let mut zip = zip::ZipArchive::new(File::open(path)?)?;
    ensure!(
        zip.len() <= max_files.saturating_mul(2).max(64),
        "ZIPの項目数が多すぎます"
    );
    let mut files = BTreeMap::new();
    let mut names = BTreeSet::new();
    let mut total = 0u64;
    let mut buffer = vec![0; 128 * 1024];
    for index in 0..zip.len() {
        let mut entry = zip.by_index(index)?;
        let name = entry.name()?.trim_end_matches('/').to_owned();
        zip_path(&name)?;
        ensure!(
            entry
                .unix_mode()
                .is_none_or(|mode| mode & 0o170000 != 0o120000),
            "ZIPのリンクは使えません"
        );
        if let Some(folder) = folder {
            ensure!(
                name == folder || name.starts_with(&format!("{folder}/")),
                "ZIPのフォルダが一致しません"
            );
        }
        ensure!(
            names.insert(name.to_lowercase()),
            "ZIPのパスが重複しています: {name}"
        );
        if entry.is_dir() {
            continue;
        }
        total = total.checked_add(entry.size()).context("ZIPサイズ超過")?;
        ensure!(
            total <= max_bytes && files.len() < max_files,
            "ZIPの展開量を超過しました"
        );
        let destination = target.join(&name);
        fs::create_dir_all(destination.parent().context("展開先なし")?)?;
        let mut output = OpenOptions::new()
            .write(true)
            .create_new(true)
            .open(&destination)?;
        let mut hasher = Sha256::new();
        let mut written = 0;
        loop {
            let length = entry.read(&mut buffer)?;
            if length == 0 {
                break;
            }
            written += length as u64;
            ensure!(written <= entry.size(), "ZIP内容サイズ超過");
            output.write_all(&buffer[..length])?;
            hasher.update(&buffer[..length]);
        }
        ensure!(written == entry.size(), "ZIPが途中で終了しました");
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            // 実行可否だけを引き継ぎ、setuid等の特殊権限は採用しない。
            let mode = if entry.unix_mode().unwrap_or(0) & 0o111 != 0 {
                0o755
            } else {
                0o644
            };
            output.set_permissions(fs::Permissions::from_mode(mode))?;
        }
        files.insert(
            name.clone(),
            Descriptor {
                path: name,
                size: written,
                sha256: format!("{:x}", hasher.finalize()),
                source_kind: "integrated".into(),
            },
        );
        if files.len() % 1000 == 0 {
            progress(format!(
                "展開: {} / {}ファイル",
                folder.unwrap_or("KBCS"),
                files.len()
            ));
        }
    }
    Ok(files)
}

pub fn install_data(
    data: &DataRelease,
    root: &Path,
    progress: &(impl Fn(String) + Sync),
) -> Result<PathBuf> {
    install_data_mode(data, root, progress, false)
}
pub fn repair_data(
    data: &DataRelease,
    root: &Path,
    progress: &(impl Fn(String) + Sync),
) -> Result<PathBuf> {
    install_data_mode(data, root, progress, true)
}
fn install_data_mode(
    data: &DataRelease,
    root: &Path,
    progress: &(impl Fn(String) + Sync),
    force: bool,
) -> Result<PathBuf> {
    validate_manifest(
        &data.manifest,
        &data.release,
        &data.manifest.header.source_region,
    )?;
    let directory = root.join("assets/releases");
    fs::create_dir_all(&directory)?;
    let _lock = lock(&root.join("download.lock"))?;
    let destination = directory.join(&data.release.tag_name);
    if let Ok(installed) = installed(&destination) {
        ensure!(
            installed.release.manifest.revision == data.manifest.revision,
            "同じ版の原本が変更されています"
        );
        let complete = !force
            && installed
                .files
                .iter()
                .all(|(name, descriptor)| source_path_is_complete(&destination, name, descriptor));
        if complete {
            return Ok(destination);
        }
        progress("不足・破損した原本を再取得します".into());
    }
    let unpacked = data
        .manifest
        .archives
        .values()
        .map(|v| v.uncompressed_size)
        .try_fold(0u64, |total, size| {
            total.checked_add(size).context("展開容量の上限超過")
        })?;
    let archive = data
        .manifest
        .archives
        .values()
        .map(|v| v.size)
        .max()
        .unwrap_or(0);
    crate::storage::require(
        root,
        unpacked
            .saturating_add(archive)
            .saturating_add(512 * 1024 * 1024),
    )?;
    let pending = directory.join(format!(".pending-{}", data.release.tag_name));
    // この処理だけが所有する中間フォルダ。公開済みデータは失敗時も維持する。
    if pending.exists() {
        fs::remove_dir_all(&pending)?;
    }
    fs::create_dir(&pending)?;
    let result = (|| -> Result<()> {
        let mut files = BTreeMap::new();
        for (position, (folder, archive)) in data.manifest.archives.iter().enumerate() {
            progress(format!(
                "ZIP {}/{}: {}",
                position + 1,
                data.manifest.archives.len(),
                archive.file
            ));
            let asset = data
                .release
                .assets
                .iter()
                .find(|a| a.name == archive.file)
                .context("配布ファイルなし")?;
            let path = download(asset, &root.join("updates/downloads"), progress)?;
            let extracted = extract(
                &path,
                &pending,
                Some(folder),
                archive.uncompressed_size,
                archive.file_count,
                progress,
            )?;
            ensure!(
                extracted.len() == archive.file_count
                    && extracted.values().map(|d| d.size).sum::<u64>() == archive.uncompressed_size,
                "ZIPの展開件数・サイズ不一致: {folder}"
            );
            files.extend(extracted);
            // 展開済み原本を保持し、巨大ZIPの二重保存で初回の空き容量を圧迫しない。
            fs::remove_file(path)?;
        }
        let installed = Installed {
            release: data.clone(),
            files,
        };
        let bytes = serde_json::to_vec(&installed)?;
        let mut file = File::create(pending.join("release.json"))?;
        file.write_all(&bytes)?;
        file.sync_all()?;
        drop(file);
        let backup = directory.join(format!(
            ".replaced-{}-{}",
            data.release.tag_name,
            std::process::id()
        ));
        ensure!(
            directory.canonicalize()?.starts_with(root.canonicalize()?),
            "原本保存先が管理フォルダ外です"
        );
        if destination.exists() {
            fs::rename(&destination, &backup)?;
        }
        if let Err(error) = fs::rename(&pending, &destination) {
            if backup.exists() {
                let _ = fs::rename(&backup, &destination);
            }
            return Err(error.into());
        }
        if backup.exists() {
            ensure!(
                backup
                    .canonicalize()?
                    .starts_with(directory.canonicalize()?),
                "削除先が原本保存先の外部です"
            );
            fs::remove_dir_all(&backup)?;
        }
        Ok(())
    })();
    if result.is_err() {
        let _ = fs::remove_dir_all(&pending);
    }
    result?;
    Ok(destination)
}

fn source_path_is_complete(root: &Path, name: &str, descriptor: &Descriptor) -> bool {
    if crate::source::safe_path(name).is_err() {
        return false;
    }
    root.join(name)
        .metadata()
        .is_ok_and(|value| value.is_file() && value.len() == descriptor.size)
}

pub fn installed(directory: &Path) -> Result<Installed> {
    parse_json(&fs::read(directory.join("release.json"))?)
}

pub fn lock(path: &Path) -> Result<File> {
    let file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .truncate(false)
        .open(path)?;
    // ファイルの有無ではなくOSの排他を使う。異常終了後も次回の更新を妨げない。
    file.try_lock()
        .context("別のKBCSが更新中です。終了後に再試行してください")?;
    Ok(file)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn partial_releases_select_latest_available_platform() {
        let make_release = |version: &str, platforms: &[&str], draft: bool| Release {
            tag_name: format!("kbcs-v{version}"),
            published_at: String::new(),
            html_url: String::new(),
            draft,
            assets: platforms
                .iter()
                .map(|platform| Asset {
                    name: format!("KBCS-{version}-{platform}.zip"),
                    size: 1,
                    browser_download_url: String::new(),
                    digest: Some(format!("sha256:{}", "a".repeat(64))),
                })
                .collect(),
        };
        let mut releases = vec![
            make_release(
                "0.1.37",
                &["windows-x64", "macos-arm64", "macos-x64"],
                false,
            ),
            make_release("0.1.38", &["windows-x64"], false),
            make_release("0.1.39", &["macos-arm64"], true),
            make_release("0.1.40", &["windows-x64"], false),
        ];
        releases[3].assets[0].digest = None;
        for (os, architecture, expected) in [
            ("windows", "x86_64", "kbcs-v0.1.38"),
            ("macos", "aarch64", "kbcs-v0.1.37"),
            ("macos", "x86_64", "kbcs-v0.1.37"),
        ] {
            assert_eq!(
                latest_app_for(releases.clone(), os, architecture)
                    .unwrap()
                    .tag_name,
                expected
            );
        }
        releases[1] = make_release("0.1.38", &["windows-x64", "macos-arm64"], false);
        assert_eq!(
            latest_app_for(releases, "macos", "aarch64")
                .unwrap()
                .tag_name,
            "kbcs-v0.1.38"
        );
    }

    fn serve_body(bytes: Vec<u8>) -> Result<(String, std::thread::JoinHandle<()>)> {
        let size = bytes.len();
        serve_responses(size, vec![(bytes, Duration::ZERO)])
    }

    fn serve_responses(
        size: usize,
        responses: Vec<(Vec<u8>, Duration)>,
    ) -> Result<(String, std::thread::JoinHandle<()>)> {
        let listener = std::net::TcpListener::bind("127.0.0.1:0")?;
        let url = format!("http://{}/fixture.zip", listener.local_addr()?);
        let worker = std::thread::spawn(move || {
            for (bytes, delay) in responses {
                let (mut stream, _) = listener.accept().unwrap();
                stream
                    .set_read_timeout(Some(Duration::from_secs(5)))
                    .unwrap();
                let mut request = [0; 4096];
                let _ = stream.read(&mut request);
                write!(
                    stream,
                    "HTTP/1.1 200 OK\r\nContent-Length: {size}\r\nConnection: close\r\n\r\n"
                )
                .unwrap();
                for chunk in bytes.chunks(16 * 1024) {
                    std::thread::sleep(delay);
                    if stream.write_all(chunk).is_err() {
                        break;
                    }
                }
            }
        });
        Ok((url, worker))
    }

    #[test]
    fn download_allows_slow_body_and_retries_interrupted_transfer() -> Result<()> {
        let root = std::env::temp_dir().join(format!("kbcs-slow-download-{}", std::process::id()));
        let result = (|| -> Result<()> {
            let bytes = vec![42; 64 * 1024];
            // 旧120秒の条件を短縮して再現。継続受信しても本文全体の期限で失敗する。
            let legacy: ureq::Agent = ureq::Agent::config_builder()
                .timeout_global(Some(Duration::from_secs(5)))
                .timeout_recv_body(Some(Duration::from_millis(200)))
                .build()
                .into();
            let (url, worker) = serve_responses(
                bytes.len(),
                vec![(bytes.clone(), Duration::from_millis(80))],
            )?;
            let error = legacy
                .get(&url)
                .call()?
                .body_mut()
                .as_reader()
                .read_to_end(&mut Vec::new())
                .unwrap_err();
            // 期限までの中間受信量はOSや実行タイミングによって0bytesにもなる。
            // 本文期限の発火を確認し、取得結果と再試行は後段で検査する。
            assert!(matches!(
                ureq::Error::from(error),
                ureq::Error::Timeout(ureq::Timeout::RecvBody)
            ));
            worker.join().unwrap();

            // 最初の接続は途中で切れ、次は旧期限より長く受信して完了する。
            let (url, worker) = serve_responses(
                bytes.len(),
                vec![
                    (bytes[..1024].to_vec(), Duration::ZERO),
                    (bytes.clone(), Duration::from_millis(100)),
                ],
            )?;
            let asset = Asset {
                name: "slow.zip".into(),
                size: bytes.len() as u64,
                browser_download_url: url,
                digest: Some(format!("sha256:{}", hash(&bytes))),
            };
            let retries = std::cell::Cell::new(0);
            let path = download_with_agent(
                &asset,
                &root,
                &|message| {
                    if message.starts_with("通信を再試行") {
                        retries.set(retries.get() + 1);
                    }
                },
                &agent(Duration::from_secs(5)),
            )?;
            worker.join().unwrap();
            assert_eq!(fs::read(&path)?, bytes);
            assert_eq!(retries.get(), 1);
            fs::remove_file(&path)?;

            let (url, worker) = serve_responses(bytes.len(), vec![(vec![42], Duration::ZERO); 3])?;
            let asset = Asset {
                browser_download_url: url,
                ..asset
            };
            let error = download_with_agent(&asset, &root, &|_| {}, &agent(Duration::from_secs(5)))
                .unwrap_err();
            worker.join().unwrap();
            assert!(error.to_string().contains("3/3回"));
            assert!(!path.exists());
            assert!(!path.with_extension("part").exists());
            Ok(())
        })();
        if root.exists() {
            fs::remove_dir_all(root)?;
        }
        result
    }

    #[test]
    fn streaming_download_reuses_only_verified_files() -> Result<()> {
        let root = std::env::temp_dir().join(format!("kbcs-download-{}", std::process::id()));
        let result = (|| -> Result<()> {
            let bytes = vec![42; 256 * 1024];
            let (url, worker) = serve_body(bytes.clone())?;
            let mut asset = Asset {
                name: "fixture.zip".into(),
                size: bytes.len() as u64,
                browser_download_url: url,
                digest: Some(format!("sha256:{}", hash(&bytes))),
            };
            let path = download(&asset, &root, &|_| {})?;
            worker.join().unwrap();
            assert_eq!(fs::read(&path)?, bytes);
            asset.browser_download_url = "http://127.0.0.1:1/offline".into();
            assert_eq!(download(&asset, &root, &|_| {})?, path);
            let (url, worker) = serve_body(vec![7; bytes.len()])?;
            asset.browser_download_url = url;
            fs::write(&path, b"corrupt cache")?;
            let retries = std::cell::Cell::new(0);
            assert!(
                download(&asset, &root, &|message| {
                    if message.starts_with("通信を再試行") {
                        retries.set(retries.get() + 1);
                    }
                })
                .is_err()
            );
            worker.join().unwrap();
            assert_eq!(retries.get(), 0);
            assert!(!path.with_extension("part").exists());
            Ok(())
        })();
        if root.exists() {
            fs::remove_dir_all(root)?;
        }
        result
    }
    #[test]
    fn versions_and_archive_paths() {
        assert!(app_version("native-v15.7.2").is_none());
        assert!(app_version("kbcs-v0.1.10") > app_version("kbcs-v0.1.9"));
        for (os, arch, platform) in [
            ("windows", "x86_64", "windows-x64"),
            ("macos", "aarch64", "macos-arm64"),
            ("macos", "x86_64", "macos-x64"),
        ] {
            assert_eq!(
                app_asset_name("kbcs-v0.1.35", os, arch).unwrap(),
                format!("KBCS-0.1.35-{platform}.zip")
            );
        }
        assert!(app_asset_name("kbcs-v0.1.35", "macos", "x86").is_err());
        for path in [
            "../out",
            "Data/C:foo",
            "Data\\x",
            "Data/NUL.txt",
            "Data/name.",
        ] {
            assert!(zip_path(path).is_err(), "{path}");
        }
        assert!(zip_path("res/Unit_Explanation1_ja.csv").is_ok());
    }

    #[test]
    fn zip_bounds_hashes_and_process_lock() -> Result<()> {
        let root = std::env::temp_dir().join(format!("kbcs-zip-{}", std::process::id()));
        fs::create_dir_all(&root)?;
        let result = (|| -> Result<()> {
            let path = root.join("fixture.zip");
            let mut writer = zip::ZipWriter::new(File::create(&path)?);
            writer.start_file(
                "Data/value.csv",
                zip::write::SimpleFileOptions::default().unix_permissions(0o755),
            )?;
            writer.write_all(b"1,2,3")?;
            writer.finish()?;
            let files = extract(&path, &root.join("good"), Some("Data"), 5, 1, &|_| {})?;
            assert_eq!(files["Data/value.csv"].sha256, hash(b"1,2,3"));
            #[cfg(unix)]
            {
                use std::os::unix::fs::PermissionsExt;
                assert_eq!(
                    fs::metadata(root.join("good/Data/value.csv"))?
                        .permissions()
                        .mode()
                        & 0o777,
                    0o755
                );
            }
            assert!(extract(&path, &root.join("oversize"), Some("Data"), 4, 1, &|_| {}).is_err());
            assert!(extract(&path, &root.join("wrong"), Some("Unit"), 5, 1, &|_| {}).is_err());
            let lock_path = root.join("download.lock");
            let locked = lock(&lock_path)?;
            assert!(lock(&lock_path).is_err());
            drop(locked);
            assert!(lock(&lock_path).is_ok());
            Ok(())
        })();
        fs::remove_dir_all(root)?;
        result
    }
}
