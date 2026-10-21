use anyhow::{Context, Result, bail, ensure};
use serde::{Deserialize, Serialize, de::DeserializeOwned};
use sha2::{Digest, Sha256};
use std::{
    collections::BTreeMap,
    path::{Component, Path, PathBuf},
    process::Command,
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

pub struct Source {
    location: Location,
    agent: ureq::Agent,
    pub revision: String,
    pub origin: String,
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
            })
        }
    }

    pub fn read(&self, name: &str) -> Result<Vec<u8>> {
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
                .read_to_vec()?),
        }
    }

    pub fn checked(&self, descriptor: &Descriptor) -> Result<Vec<u8>> {
        let bytes = self.read(&descriptor.path)?;
        verify(&bytes, descriptor)?;
        Ok(bytes)
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
