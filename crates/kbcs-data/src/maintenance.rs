use crate::{
    source,
    store::{self, Database},
};
use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OpenFlags};
use serde_json::{Value, json};
use std::{
    fs,
    path::{Path, PathBuf},
};

const FOLDERS: &[&str] = &["official", "assets", "updates", "user"];
fn resolve(root: &Path, relative: &str) -> Result<PathBuf> {
    source::safe_path(relative)?;
    ensure!(
        FOLDERS.contains(&relative.split('/').next().unwrap_or("")),
        "閲覧対象外の保存先です"
    );
    let base = root.canonicalize()?;
    let path = root.join(relative).canonicalize()?;
    ensure!(
        path.starts_with(&base) && path != base,
        "保存先の外部は操作できません"
    );
    Ok(path)
}
pub fn summary(root: &Path, region: &str) -> Result<Value> {
    let opened = Database::open(root, region);
    let database_error = opened.as_ref().err().map(|v| format!("{v:#}"));
    let database = opened.ok();
    let mut counts = serde_json::Map::new();
    if let Some(db) = &database {
        for table in [
            "unit",
            "form",
            "enemy",
            "stage_entry",
            "asset_reference",
            "source_file",
        ] {
            let count = db
                .connection
                .query_row(&format!("SELECT count(*) FROM {table}"), [], |r| {
                    r.get::<_, i64>(0)
                })
                .ok();
            counts.insert(table.into(), json!(count));
        }
    }
    Ok(
        json!({"storage":crate::storage::space(root),"dataDir":root,"database":store::current_path(root,region).ok(),"databaseError":database_error,"metadata":database.as_ref().and_then(|db|db.metadata().ok()),"counts":counts,"schemaVersion":crate::SCHEMA_VERSION,"importerVersion":crate::IMPORTER_VERSION}),
    )
}
pub fn browse(root: &Path, relative: &str) -> Result<Value> {
    let mut entries = Vec::new();
    let protected = protected_paths(root)?;
    let directory = if relative.is_empty() {
        if root.exists() {
            root.canonicalize()?
        } else {
            root.to_path_buf()
        }
    } else {
        resolve(root, relative)?
    };
    if !directory.exists() {
        return Ok(json!({"path":relative,"entries":entries}));
    }
    ensure!(directory.is_dir(), "フォルダを指定してください");
    for entry in fs::read_dir(directory)? {
        let entry = entry?;
        let name = entry.file_name().to_string_lossy().into_owned();
        if relative.is_empty() && !FOLDERS.contains(&name.as_str()) {
            continue;
        }
        let path = if relative.is_empty() {
            name.clone()
        } else {
            format!("{relative}/{name}")
        };
        let metadata = entry.path().symlink_metadata()?;
        if metadata.is_symlink() {
            continue;
        }
        entries.push(json!({"name":name,"path":path,"directory":metadata.is_dir(),"size":if metadata.is_file(){Some(metadata.len())}else{None},"modified":metadata.modified().ok().and_then(|v|v.duration_since(std::time::UNIX_EPOCH).ok()).map(|v|v.as_secs()),"deletable":can_delete_target(&entry.path(),&path,&protected)}));
    }
    entries.sort_by(|a, b| {
        b["directory"]
            .as_bool()
            .cmp(&a["directory"].as_bool())
            .then_with(|| a["name"].as_str().cmp(&b["name"].as_str()))
    });
    Ok(json!({"path":relative,"entries":entries}))
}
fn protected_paths(root: &Path) -> Result<Vec<PathBuf>> {
    let mut protected = Vec::new();
    let Ok(catalog) = store::catalog(root) else {
        return Ok([root.join("official"), root.join("assets/releases")]
            .into_iter()
            .filter_map(|v| v.canonicalize().ok())
            .collect());
    };
    for region in catalog.regions.keys() {
        let db_path = store::current_path(root, region)?;
        protected.push(db_path.clone());
        if let Ok(db) = Database::open_path(&db_path)
            && let Ok(metadata) = db.metadata()
            && let Some(tag) = metadata.get("release_tag")
        {
            source::safe_path(tag)?;
            protected.push(root.join("assets/releases").join(tag));
            if let Some(origin) = metadata
                .get("origin")
                .filter(|v| !v.starts_with("https://"))
            {
                protected.push(PathBuf::from(origin));
            }
        }
    }
    Ok(protected
        .into_iter()
        .filter_map(|v| v.canonicalize().ok())
        .collect())
}
fn can_delete(root: &Path, relative: &str, protected: &[PathBuf]) -> bool {
    let Ok(target) = resolve(root, relative) else {
        return false;
    };
    can_delete_target(&target, relative, protected)
}
fn can_delete_target(target: &Path, relative: &str, protected: &[PathBuf]) -> bool {
    if relative == "user" || relative.starts_with("user/") {
        return false;
    }
    !protected
        .iter()
        .any(|path| path.starts_with(target) || target.starts_with(path))
}
pub fn delete(root: &Path, relative: &str) -> Result<()> {
    ensure!(
        can_delete(root, relative, &protected_paths(root)?),
        "使用中のDB・原本とユーザーデータは削除できません"
    );
    let target = resolve(root, relative)?;
    if target.is_dir() {
        fs::remove_dir_all(target)?;
    } else {
        fs::remove_file(target)?;
    }
    Ok(())
}
pub fn inspect(root: &Path, relative: &str) -> Result<Value> {
    let path = resolve(root, relative)?;
    let size = path.metadata()?.len();
    ensure!(path.is_file(), "ファイルを指定してください");
    if path.extension().is_some_and(|v| v == "sqlite") {
        let db = Connection::open_with_flags(&path, OpenFlags::SQLITE_OPEN_READ_ONLY)?;
        let mut query=db.prepare("SELECT name,sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")?;
        let tables = query
            .query_map([], |r| {
                Ok(json!({"table":r.get::<_,String>(0)?,"schema":r.get::<_,String>(1)?}))
            })?
            .collect::<rusqlite::Result<Vec<_>>>()?;
        return Ok(json!({"path":relative,"size":size,"tables":tables}));
    }
    if size > 262_144 {
        return Ok(
            json!({"path":relative,"size":size,"note":"大きいファイルはメタデータのみ表示します"}),
        );
    }
    let bytes = fs::read(&path).context("ファイルを読めません")?;
    Ok(
        json!({"path":relative,"size":size,"sha256":source::hash(&bytes),"text":std::str::from_utf8(&bytes).ok()}),
    )
}
pub fn verify(root: &Path, region: &str, progress: impl Fn(String)) -> Result<Value> {
    let db = Database::open(root, region)?;
    store::validate(&db.connection)?;
    let metadata = db.metadata()?;
    let origin = metadata
        .get("release_tag")
        .map(|tag| root.join("assets/releases").join(tag))
        .filter(|v| v.is_dir())
        .or_else(|| {
            metadata
                .get("origin")
                .filter(|v| !v.starts_with("https://"))
                .map(PathBuf::from)
        });
    let mut query=db.connection.prepare("SELECT a.path,a.original_path,a.sha256,a.size,s.bytes FROM asset_reference a LEFT JOIN source_file s ON s.path=a.path ORDER BY a.path")?;
    let mut rows = query.query([])?;
    let mut checked = 0usize;
    let mut failures = 0usize;
    let mut issues = Vec::new();
    while let Some(row) = rows.next()? {
        let logical: String = row.get(0)?;
        let original: String = row.get(1)?;
        let sha: String = row.get(2)?;
        let size = u64::try_from(row.get::<_, i64>(3)?)?;
        source::safe_path(&original)?;
        let stored: Option<Vec<u8>> = row.get(4)?;
        let bytes = stored
            .or_else(|| {
                origin
                    .as_ref()
                    .and_then(|dir| fs::read(dir.join(&original)).ok())
            })
            .or_else(|| fs::read(root.join("assets/objects").join(&sha)).ok());
        if !bytes
            .as_ref()
            .is_some_and(|v| v.len() as u64 == size && source::hash(v) == sha)
        {
            failures += 1;
            if issues.len() < 200 {
                issues.push(json!({"path":logical,"reason":if bytes.is_none(){"原本がありません"}else{"サイズ・SHA不一致"}}));
            }
        }
        checked += 1;
        if checked.is_multiple_of(1000) {
            progress(format!(
                "原本検査: {checked}ファイル / 不足・破損{failures}"
            ));
        }
    }
    Ok(
        json!({"checked":checked,"failures":failures,"issues":issues,"ok":failures==0,"metadata":metadata}),
    )
}

#[test]
fn deletion_stays_in_managed_storage() -> Result<()> {
    let root = std::env::temp_dir().join(format!(
        "kbcs-storage-{}-{}",
        std::process::id(),
        std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)?
            .as_nanos()
    ));
    fs::create_dir_all(root.join("assets/objects"))?;
    fs::create_dir_all(root.join("user"))?;
    fs::write(root.join("assets/objects/unused"), b"cache")?;
    fs::write(root.join("user/formation.sqlite"), b"saved")?;
    assert!(delete(&root, "../outside").is_err());
    assert!(delete(&root, "user/formation.sqlite").is_err());
    assert_eq!(browse(&root, "")?["entries"].as_array().unwrap().len(), 2);
    delete(&root, "assets/objects/unused")?;
    assert!(root.join("user/formation.sqlite").exists());
    ensure!(
        root.canonicalize()?
            .starts_with(std::env::temp_dir().canonicalize()?),
        "試験の削除先が不正です"
    );
    fs::remove_dir_all(root)?;
    Ok(())
}
