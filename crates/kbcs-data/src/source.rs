use anyhow::{Context, Result, bail, ensure};
use serde::{Deserialize, Serialize, de::DeserializeOwned};
use sha2::{Digest, Sha256};
use std::{
    collections::BTreeMap,
    path::{Component, Path, PathBuf},
    process::Command,
    sync::{
        Mutex,
        atomic::{AtomicBool, AtomicUsize, Ordering},
    },
    time::Duration,
};

#[derive(Clone, Debug, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct Header {
    pub schema_version: u32,
    pub dataset_id: String,
    pub build_id: String,
    pub source_region: String,
    pub version_code: u64,
    pub version_name: String,
}

#[derive(Clone, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Current {
    #[serde(flatten)]
    pub header: Header,
    pub generated_path: String,
    pub manifest_sha256: String,
    pub status: String,
}

#[derive(Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct Descriptor {
    #[serde(default)]
    pub path: String,
    pub sha256: String,
    pub size: u64,
    #[serde(default)]
    pub source_kind: String,
}

#[derive(Deserialize)]
pub struct Manifest {
    pub header: Header,
    pub artifacts: BTreeMap<String, Descriptor>,
    pub inputs: BTreeMap<String, Descriptor>,
}

#[derive(Deserialize)]
pub struct AssetIndex {
    pub header: Header,
    pub files: BTreeMap<String, Descriptor>,
}

#[derive(Deserialize)]
pub struct CharacterIndex {
    pub header: Header,
    pub units: Vec<Character>,
}

#[derive(Deserialize)]
pub struct Character {
    #[serde(default)]
    pub kind: Option<String>,
    pub id: String,
    pub forms: Vec<CharacterForm>,
    #[serde(default)]
    pub aliases: Vec<String>,
}

#[derive(Deserialize)]
pub struct CharacterForm {
    pub name: String,
    pub description: String,
}

pub fn hash(bytes: &[u8]) -> String {
    format!("{:x}", Sha256::digest(bytes))
}

pub fn parse_json<T: DeserializeOwned>(bytes: &[u8]) -> Result<T> {
    Ok(serde_json::from_slice(
        bytes.strip_prefix(&[0xef, 0xbb, 0xbf]).unwrap_or(bytes),
    )?)
}

pub fn safe_path(value: &str) -> Result<&str> {
    ensure!(
        !value.is_empty()
            && !value.contains(['\\', ':', '\0', '?', '#', '%'])
            && value
                .split('/')
                .all(|part| !part.is_empty() && part != "." && part != "..")
            && Path::new(value)
                .components()
                .all(|part| matches!(part, Component::Normal(_))),
        "不正な相対パス: {value}"
    );
    Ok(value)
}

pub fn verify(bytes: &[u8], expected: &Descriptor) -> Result<()> {
    ensure!(
        bytes.len() as u64 == expected.size && hash(bytes) == expected.sha256,
        "サイズ/SHA-256不一致: {}",
        expected.path
    );
    Ok(())
}

enum Location {
    Local(PathBuf),
    Remote(String),
}

// DBに索引だけ保存した画像も、取り込み時のcommit/SHAへ固定して取得する。
pub fn asset(database: &crate::store::Database, root: &Path, logical: &str) -> Result<Vec<u8>> {
    safe_path(logical)?;
    if let Ok((_, _, _, bytes)) = database.source(logical) {
        return Ok(bytes);
    }
    let descriptor = database
        .connection
        .query_row(
            "SELECT original_path,sha256,size,source_kind FROM asset_reference WHERE path=?",
            [logical],
            |row| {
                Ok(Descriptor {
                    path: row.get(0)?,
                    sha256: row.get(1)?,
                    size: row.get::<_, i64>(2)? as u64,
                    source_kind: row.get(3)?,
                })
            },
        )
        .with_context(|| format!("画像の索引なし: {logical}"))?;
    let metadata = database.metadata()?;
    let origin = metadata.get("origin").context("原本の取得元なし")?;
    let revision = metadata.get("revision").context("原本commitなし")?;
    ensure!(
        revision.len() == 40 && revision.bytes().all(|b| b.is_ascii_hexdigit()),
        "不正な原本commit"
    );
    let location = if let Some(repository) = origin.strip_prefix("https://github.com/") {
        let parts: Vec<_> = repository.trim_end_matches('/').split('/').collect();
        ensure!(
            parts.len() == 2
                && parts.iter().all(|p| !p.is_empty()
                    && p.bytes()
                        .all(|b| b.is_ascii_alphanumeric() || b"-_.".contains(&b))),
            "不正な原本URL"
        );
        Location::Remote(format!(
            "https://raw.githubusercontent.com/{}/{revision}",
            parts.join("/")
        ))
    } else {
        Location::Local(Path::new(origin).canonicalize()?)
    };
    let source = Source {
        location,
        agent: ureq::Agent::config_builder()
            .timeout_global(Some(Duration::from_secs(60)))
            .build()
            .into(),
        revision: revision.clone(),
        origin: origin.clone(),
        cache: Some(root.join("assets")),
        previous: None,
    };
    source.checked_named(&descriptor, logical)
}

pub struct Source {
    location: Location,
    agent: ureq::Agent,
    pub revision: String,
    pub origin: String,
    cache: Option<PathBuf>,
    previous: Option<Mutex<crate::store::Database>>,
}

impl Source {
    pub fn open(location: &str) -> Result<Self> {
        let config = ureq::Agent::config_builder()
            .timeout_global(Some(Duration::from_secs(60)))
            .build();
        let agent: ureq::Agent = config.into();
        if location.starts_with("https://github.com/") {
            let path = location
                .trim_start_matches("https://github.com/")
                .trim_end_matches('/');
            let parts: Vec<_> = path.split('/').collect();
            ensure!(
                parts.len() == 2
                    && parts.iter().all(|part| !part.is_empty()
                        && part
                            .chars()
                            .all(|c| c.is_ascii_alphanumeric() || "-_.".contains(c))),
                "GitHubリポジトリURLを指定してください"
            );
            let bytes = agent
                .get(format!("https://api.github.com/repos/{path}/commits/HEAD"))
                .header("User-Agent", "KBCS")
                .call()?
                .body_mut()
                .read_to_vec()?;
            let value: serde_json::Value = parse_json(&bytes)?;
            let revision = value["sha"].as_str().context("commit SHAなし")?.to_owned();
            ensure!(
                revision.len() == 40 && revision.chars().all(|c| c.is_ascii_hexdigit()),
                "不正なcommit SHA"
            );
            Ok(Self {
                location: Location::Remote(format!(
                    "https://raw.githubusercontent.com/{path}/{revision}"
                )),
                agent,
                revision,
                origin: location.into(),
                cache: None,
                previous: None,
            })
        } else {
            let root = Path::new(location)
                .canonicalize()
                .context("assetsフォルダを開けません")?;
            let git = |args: &[&str]| -> Result<String> {
                let output = Command::new("git")
                    .arg("-C")
                    .arg(&root)
                    .args(args)
                    .output()?;
                ensure!(output.status.success(), "Git情報の取得に失敗");
                Ok(String::from_utf8(output.stdout)?.trim().to_owned())
            };
            ensure!(
                git(&["status", "--porcelain", "--untracked-files=no"])?.is_empty(),
                "assetsに未コミット変更があります。確定した原本を指定してください"
            );
            let revision = git(&["rev-parse", "HEAD"])?;
            Ok(Self {
                location: Location::Local(root),
                agent,
                revision,
                origin: location.into(),
                cache: None,
                previous: None,
            })
        }
    }

    pub fn open_cached(location: &str, root: &Path, region: &str) -> Result<Self> {
        let mut source = Self::open(location)?;
        let cache = root.join("assets");
        std::fs::create_dir_all(cache.join("objects"))?;
        source.cache = Some(cache);
        source.previous = crate::store::Database::open(root, region)
            .ok()
            .map(Mutex::new);
        Ok(source)
    }

    fn save_cache(&self, path: &Path, bytes: &[u8]) -> Result<()> {
        static NEXT: AtomicUsize = AtomicUsize::new(0);
        std::fs::create_dir_all(path.parent().context("キャッシュ保存先なし")?)?;
        let temporary = path.with_extension(format!(
            "{}-{}.tmp",
            std::process::id(),
            NEXT.fetch_add(1, Ordering::Relaxed)
        ));
        let result = (|| -> Result<()> {
            std::fs::write(&temporary, bytes)?;
            // キャッシュは検証してから使う。電源断で不完全でも次回取り直せる。
            std::fs::rename(&temporary, path)?;
            Ok(())
        })();
        if result.is_err() {
            let _ = std::fs::remove_file(&temporary);
        }
        result
    }

    pub fn read(&self, name: &str) -> Result<Vec<u8>> {
        safe_path(name)?;
        let path = self
            .cache
            .as_ref()
            .filter(|_| matches!(self.location, Location::Remote(_)))
            .map(|root| {
                root.join("repositories")
                    .join(hash(self.origin.as_bytes()))
                    .join(&self.revision)
                    .join(name)
            });
        if let Some(path) = &path
            && let Ok(bytes) = std::fs::read(path)
        {
            return Ok(bytes);
        }
        let bytes = self.read_original(name)?;
        if let Some(path) = path {
            self.save_cache(&path, &bytes)?;
        }
        Ok(bytes)
    }

    fn read_original(&self, name: &str) -> Result<Vec<u8>> {
        safe_path(name)?;
        match &self.location {
            Location::Local(root) => {
                let path = root
                    .join(name)
                    .canonicalize()
                    .with_context(|| format!("元ファイルなし: {name}"))?;
                ensure!(path.starts_with(root), "assets外への参照");
                Ok(std::fs::read(path)?)
            }
            Location::Remote(base) => Ok(self
                .agent
                .get(format!("{base}/{name}"))
                .call()
                .with_context(|| format!("取得失敗: {name}"))?
                .body_mut()
                .with_config()
                .limit(64 * 1024 * 1024)
                .read_to_vec()
                .with_context(|| format!("原本の受信失敗: {name}"))?),
        }
    }

    pub fn checked(&self, descriptor: &Descriptor) -> Result<Vec<u8>> {
        self.checked_named(descriptor, &descriptor.path)
    }

    pub fn checked_named(&self, descriptor: &Descriptor, logical: &str) -> Result<Vec<u8>> {
        ensure!(
            descriptor.sha256.len() == 64
                && descriptor.sha256.bytes().all(|b| b.is_ascii_hexdigit()),
            "不正な原本SHA-256"
        );
        let path = self
            .cache
            .as_ref()
            .map(|root| root.join("objects").join(&descriptor.sha256));
        let remote = matches!(self.location, Location::Remote(_));
        // ローカルの開発用原本は毎回検証し、変更をキャッシュで隠さない。
        if remote {
            if let Some(path) = &path
                && let Ok(bytes) = std::fs::read(path)
                && verify(&bytes, descriptor).is_ok()
            {
                return Ok(bytes);
            }
            if let Some(previous) = &self.previous {
                let bytes = previous
                    .lock()
                    .map_err(|_| anyhow::anyhow!("保存済み原本のロック失敗"))?
                    .connection
                    .query_row(
                        "SELECT bytes FROM source_file WHERE path=? AND sha256=?",
                        rusqlite::params![logical, descriptor.sha256],
                        |row| row.get::<_, Vec<u8>>(0),
                    )
                    .ok();
                if let Some(bytes) = bytes.filter(|bytes| verify(bytes, descriptor).is_ok()) {
                    if let Some(path) = &path {
                        self.save_cache(path, &bytes)?;
                    }
                    return Ok(bytes);
                }
            }
        }
        let bytes = self.read_original(&descriptor.path)?;
        verify(&bytes, descriptor)?;
        if let Some(path) = path {
            self.save_cache(&path, &bytes)?;
        }
        Ok(bytes)
    }

    pub fn prefetch(
        &self,
        dataset: &Dataset,
        paths: &[String],
        progress: &(impl Fn(String) + Sync),
    ) -> Result<()> {
        if !matches!(self.location, Location::Remote(_)) || self.cache.is_none() {
            return Ok(());
        }
        let next = AtomicUsize::new(0);
        let complete = AtomicUsize::new(0);
        let failed = AtomicBool::new(false);
        std::thread::scope(|scope| {
            let workers: Vec<_> = (0..8.min(paths.len()))
                .map(|_| {
                    scope.spawn(|| -> Result<()> {
                        loop {
                            if failed.load(Ordering::Relaxed) {
                                break;
                            }
                            let index = next.fetch_add(1, Ordering::Relaxed);
                            let Some(path) = paths.get(index) else {
                                break;
                            };
                            let result = dataset
                                .files
                                .get(path)
                                .context("取得対象が索引にありません")
                                .and_then(|descriptor| self.checked_named(descriptor, path));
                            if let Err(error) = result {
                                failed.store(true, Ordering::Relaxed);
                                return Err(error);
                            }
                            let count = complete.fetch_add(1, Ordering::Relaxed) + 1;
                            if count.is_multiple_of(200) || count == paths.len() {
                                progress(format!("原本を保存: {count}/{}", paths.len()));
                            }
                        }
                        Ok(())
                    })
                })
                .collect();
            for worker in workers {
                worker
                    .join()
                    .map_err(|_| anyhow::anyhow!("原本取得workerが終了しました"))??;
            }
            Ok(())
        })
    }

    pub fn dataset(&self, region: &str) -> Result<Dataset> {
        ensure!(
            ["jp", "en", "kr", "tw"].contains(&region),
            "未知のリージョン"
        );
        let current_bytes = self.read(&format!("metadata/{region}/current.json"))?;
        let current: Current = parse_json(&current_bytes)?;
        let header = &current.header;
        ensure!(
            header.schema_version == 1
                && current.status == "verified"
                && header.source_region == region,
            "current形式/状態不一致"
        );
        safe_path(&header.build_id)?;
        safe_path(&header.dataset_id)?;
        ensure!(
            !header.build_id.contains('/') && !header.dataset_id.contains('/'),
            "不正なデータ識別子"
        );
        ensure!(
            current.generated_path == format!("generated/{region}/datasets/{}", header.build_id),
            "生成物パス不一致"
        );
        let manifest_path = format!("{}/manifest.json", current.generated_path);
        let manifest_bytes = self.read(&manifest_path)?;
        ensure!(
            hash(&manifest_bytes) == current.manifest_sha256,
            "manifest SHA不一致"
        );
        let manifest: Manifest = parse_json(&manifest_bytes)?;
        ensure!(&manifest.header == header, "manifest版不一致");
        let mut proofs = vec![
            (format!("metadata/{region}/current.json"), current_bytes),
            (manifest_path, manifest_bytes),
        ];
        let mut read_artifact = |name: &str| -> Result<Vec<u8>> {
            let expected = manifest.artifacts.get(name).context("必須索引なし")?;
            let path = format!("{}/{name}", current.generated_path);
            let bytes = self.read(&path)?;
            verify(&bytes, expected)?;
            proofs.push((path, bytes.clone()));
            Ok(bytes)
        };
        let assets: AssetIndex = parse_json(&read_artifact("indexes/assets.json")?)?;
        let characters: CharacterIndex = parse_json(&read_artifact("site/characters.json")?)?;
        ensure!(
            &assets.header == header && &characters.header == header,
            "索引の版不一致"
        );
        let prefixes = [
            format!("{region}/Local/{}/", header.dataset_id),
            format!("{region}/server/"),
            format!("overrides/{region}/assets/"),
        ];
        for (logical, descriptor) in &assets.files {
            safe_path(logical)?;
            safe_path(&descriptor.path)?;
            ensure!(
                prefixes
                    .iter()
                    .any(|prefix| descriptor.path.starts_with(prefix)),
                "採用元が対象版の外です"
            );
        }
        if characters.units.is_empty() {
            bail!("キャラ索引が空です");
        }
        Ok(Dataset {
            current,
            manifest,
            files: assets.files,
            characters: characters.units,
            proofs,
        })
    }
}

pub struct Dataset {
    pub current: Current,
    pub manifest: Manifest,
    pub files: BTreeMap<String, Descriptor>,
    pub characters: Vec<Character>,
    pub proofs: Vec<(String, Vec<u8>)>,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn original_cache_reuses_database_and_repairs_corruption() -> Result<()> {
        let root = std::env::temp_dir().join(format!(
            "kbcs-original-cache-{}-{}",
            std::process::id(),
            std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)?
                .as_nanos()
        ));
        std::fs::create_dir_all(root.join("objects"))?;
        let result = (|| -> Result<()> {
            let bytes = b"saved original";
            let descriptor = Descriptor {
                path: "jp/server/original.csv".into(),
                sha256: hash(bytes),
                size: bytes.len() as u64,
                source_kind: "server".into(),
            };
            let connection = rusqlite::Connection::open_in_memory()?;
            connection.execute_batch(
                "CREATE TABLE source_file(path TEXT PRIMARY KEY,sha256 TEXT,bytes BLOB)",
            )?;
            connection.execute(
                "INSERT INTO source_file VALUES (?,?,?)",
                rusqlite::params!["Data/unit.csv", descriptor.sha256, bytes.as_slice()],
            )?;
            // 到達不能な接続先でも保存済み原本だけで取得できることを確認する。
            let mut source = Source {
                location: Location::Remote("http://127.0.0.1:1".into()),
                agent: ureq::Agent::new_with_defaults(),
                revision: "test".into(),
                origin: "test".into(),
                cache: Some(root.clone()),
                previous: Some(Mutex::new(crate::store::Database { connection })),
            };
            let path = root.join("objects").join(&descriptor.sha256);
            std::fs::write(&path, b"corrupt")?;
            assert_eq!(source.checked_named(&descriptor, "Data/unit.csv")?, bytes);
            source.previous = None;
            assert_eq!(source.checked_named(&descriptor, "Data/unit.csv")?, bytes);
            assert_eq!(std::fs::read(path)?, bytes);
            let invalid = Descriptor {
                sha256: "../invalid".into(),
                ..descriptor
            };
            assert!(source.checked(&invalid).is_err());
            let connection = rusqlite::Connection::open_in_memory()?;
            connection.execute_batch("CREATE TABLE metadata(key TEXT,value TEXT); CREATE TABLE source_file(path TEXT,original_path TEXT,source_kind TEXT,sha256 TEXT,bytes BLOB); CREATE TABLE asset_reference(path TEXT,original_path TEXT,sha256 TEXT,size INTEGER,source_kind TEXT);")?;
            connection.execute(
                "INSERT INTO metadata VALUES ('origin','https://github.com/unreachable/fixture')",
                [],
            )?;
            connection.execute(
                "INSERT INTO metadata VALUES ('revision',?)",
                ["0".repeat(40)],
            )?;
            connection.execute(
                "INSERT INTO asset_reference VALUES ('Image/img043.png',?,?,?,'local')",
                rusqlite::params![invalid.path, hash(bytes), bytes.len() as i64],
            )?;
            std::fs::create_dir_all(root.join("assets/objects"))?;
            std::fs::write(root.join("assets/objects").join(hash(bytes)), bytes)?;
            let database = crate::store::Database { connection };
            assert_eq!(asset(&database, &root, "Image/img043.png")?, bytes);
            assert!(asset(&database, &root, "../img043.png").is_err());
            Ok(())
        })();
        std::fs::remove_dir_all(root)?;
        result
    }
}
