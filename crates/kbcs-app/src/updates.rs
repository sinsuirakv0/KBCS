use anyhow::{Context, Result, ensure};
use kbcs_data::{
    import,
    releases::{self, DataRelease, Release},
    store::Database,
};
use serde_json::{Value, json};
use std::{
    fs,
    path::{Path, PathBuf},
    sync::{
        Arc, Mutex,
        atomic::{AtomicBool, Ordering},
    },
};

#[cfg(target_os = "macos")]
#[path = "updates_macos.rs"]
mod macos;
#[cfg(target_os = "macos")]
use macos::{apply as apply_files, prepare as prepare_app};

#[derive(Default)]
struct State {
    checking: bool,
    checked: bool,
    data: Option<DataRelease>,
    app: Option<Release>,
    data_error: Option<String>,
    app_error: Option<String>,
    job: String,
    message: String,
    error: Option<String>,
    app_directory: Option<PathBuf>,
}

pub struct Manager {
    root: PathBuf,
    region: String,
    state: Mutex<State>,
    pub busy: AtomicBool,
    startup_claimed: AtomicBool,
}

impl Manager {
    pub fn new(root: PathBuf, region: String) -> Self {
        let state = State {
            error: fs::read_to_string(root.join("updates/apply-error.txt")).ok(),
            ..State::default()
        };
        Self {
            root,
            region,
            state: Mutex::new(state),
            busy: AtomicBool::new(false),
            startup_claimed: AtomicBool::new(false),
        }
    }

    pub fn check(self: &Arc<Self>, first_run: bool) {
        {
            let mut state = self.state.lock().unwrap();
            if state.checking {
                return;
            }
            state.checking = true;
            state.data_error = None;
            state.app_error = None;
        }
        let manager = self.clone();
        std::thread::spawn(move || {
            let data = releases::latest_data(&manager.region);
            let metadata = Database::open(&manager.root, &manager.region)
                .and_then(|db| db.metadata())
                .ok();
            let missing = data_missing(&manager.root, metadata.as_ref());
            let has_data = {
                let mut state = manager.state.lock().unwrap();
                match data {
                    Ok(data) => state.data = Some(data),
                    Err(error) => state.data_error = Some(format!("{error:#}")),
                }
                state.data.is_some()
            };
            if first_run && missing && has_data {
                let _ = manager.start("data");
            }
            let app = releases::latest_app();
            let mut state = manager.state.lock().unwrap();
            match app {
                Ok(app) => state.app = app,
                Err(error) => state.app_error = Some(format!("{error:#}")),
            }
            state.checking = false;
            state.checked = true;
        });
    }

    pub fn status(&self, desktop: bool) -> Value {
        let metadata = Database::open(&self.root, &self.region)
            .and_then(|db| db.metadata())
            .ok();
        let state = self.state.lock().unwrap();
        let missing = data_missing(&self.root, metadata.as_ref());
        let data = state.data.as_ref().map(|data| {
            let local_version = metadata.as_ref().and_then(|m| m.get("version_code")).and_then(|v| v.parse::<u64>().ok());
            let local_tag = metadata.as_ref().and_then(|m| m.get("release_tag"));
            let local_published = metadata.as_ref().and_then(|m| m.get("release_published"));
            let available = local_version.is_none_or(|v| v <= data.manifest.header.version_code)
                && (missing || (local_tag.is_none_or(|tag| tag != &data.manifest.tag)
                && local_published.is_none_or(|published| published < &data.release.published_at)));
            json!({"version":data.manifest.header.version_name,"tag":data.release.tag_name,
                "available":available,"missing":missing,
                "size":data.manifest.archives.values().map(|a|a.size).sum::<u64>(),
                "localVersion":metadata.as_ref().and_then(|m|m.get("version")),"url":data.release.html_url})
        });
        let app = state.app.as_ref().map(|release| json!({
            "version":releases::app_version(&release.tag_name).map(|v|v.to_string()),
            "available":releases::app_version(&release.tag_name).is_some_and(|v| v > semver_current()),
            "url":release.html_url,"ready":state.app_directory.is_some(),
        }));
        json!({"checking":state.checking,"checked":state.checked,"busy":self.busy.load(Ordering::SeqCst),
            "startupPending":!self.startup_claimed.load(Ordering::SeqCst),
            "data":data,"app":app,"currentVersion":env!("CARGO_PKG_VERSION"),"desktop":desktop,
            "dataError":state.data_error,"appError":state.app_error,
            "job":state.job,"message":state.message,"error":state.error})
    }

    pub fn claim_startup(&self) -> bool {
        !self.startup_claimed.swap(true, Ordering::SeqCst)
    }

    pub fn start(self: &Arc<Self>, kind: &str) -> Result<()> {
        ensure!(matches!(kind, "data" | "app"), "更新対象が不正です");
        ensure!(
            self.busy
                .compare_exchange(false, true, Ordering::SeqCst, Ordering::SeqCst)
                .is_ok(),
            "更新中です"
        );
        {
            let mut state = self.state.lock().unwrap();
            state.job = kind.into();
            state.message = "配布情報の確認".into();
            state.error = None;
        }
        let manager = self.clone();
        let kind = kind.to_owned();
        std::thread::spawn(move || {
            let result = manager.perform(&kind);
            let mut state = manager.state.lock().unwrap();
            if let Err(error) = result {
                state.error = Some(format!("{error:#}"));
            }
            manager.busy.store(false, Ordering::SeqCst);
        });
        Ok(())
    }

    fn perform(&self, kind: &str) -> Result<()> {
        fs::create_dir_all(&self.root)?;
        let progress = |message| {
            self.state.lock().unwrap().message = message;
        };
        if kind == "data" {
            let cached = self.state.lock().unwrap().data.clone();
            let data = match cached {
                Some(data) => data,
                None => releases::latest_data(&self.region)?,
            };
            let directory = releases::install_data(&data, &self.root, &progress)?;
            let report = import::import(
                directory.to_str().context("保存先の文字コード不正")?,
                &self.root,
                &self.region,
                progress,
            )?;
            let mut state = self.state.lock().unwrap();
            state.data = Some(data);
            state.message = format!(
                "データv{}を導入しました（{}キャラ / {}形態）",
                report.version, report.units, report.forms
            );
        } else {
            let cached = self.state.lock().unwrap().app.clone();
            let app = match cached {
                Some(app) => app,
                None => releases::latest_app()?.context("本体リリースがありません")?,
            };
            ensure!(
                releases::app_version(&app.tag_name).is_some_and(|v| v > semver_current()),
                "KBCSは最新です"
            );
            let directory = prepare_app(&app, &self.root, &progress)?;
            let mut state = self.state.lock().unwrap();
            state.app = Some(app);
            state.app_directory = Some(directory);
            state.message =
                "本体のダウンロードが完了しました。「再起動して更新」で適用できます".into();
        }
        Ok(())
    }

    pub fn apply(&self) -> Result<()> {
        ensure!(!self.busy.load(Ordering::SeqCst), "更新処理中です");
        let source = self
            .state
            .lock()
            .unwrap()
            .app_directory
            .clone()
            .context("本体が未取得です")?;
        let target = std::env::current_exe()?.canonicalize()?;
        #[cfg(target_os = "macos")]
        let target = macos::bundle(&target)?;
        let plan = ApplyPlan {
            source: source.canonicalize()?,
            target,
            root: self.root.canonicalize()?,
            region: self.region.clone(),
            parent: std::process::id(),
        };
        let path = self.root.join("updates/apply.json");
        fs::write(&path, serde_json::to_vec(&plan)?)?;
        #[cfg(not(target_os = "macos"))]
        let helper = plan.source.join("kbcs.exe");
        #[cfg(target_os = "macos")]
        let helper = macos::executable(&plan.source);
        let mut command = std::process::Command::new(helper);
        command.arg("apply-update").arg("--plan").arg(path);
        #[cfg(windows)]
        {
            use std::os::windows::process::CommandExt;
            command.creation_flags(0x08000000);
        }
        command.spawn().context("更新プログラムを起動できません")?;
        Ok(())
    }
}

fn semver_current() -> kbcs_data::releases::Version {
    kbcs_data::releases::Version::parse(env!("CARGO_PKG_VERSION")).expect("本体の版")
}

fn data_missing(
    root: &Path,
    metadata: Option<&std::collections::BTreeMap<String, String>>,
) -> bool {
    let Some(metadata) = metadata else {
        return true;
    };
    let Some(tag) = metadata.get("release_tag") else {
        return false;
    };
    let managed = kbcs_data::source::safe_path(tag).is_ok()
        && !tag.contains('/')
        && root
            .join("assets/releases")
            .join(tag)
            .join("release.json")
            .is_file();
    let original = metadata
        .get("origin")
        .is_some_and(|origin| Path::new(origin).join("release.json").is_file());
    !managed && !original
}

#[cfg(not(target_os = "macos"))]
fn prepare_app(app: &Release, root: &Path, progress: &impl Fn(String)) -> Result<PathBuf> {
    let _lock = releases::lock(&root.join("download.lock"))?;
    let asset = releases::app_asset(app)?;
    let archive = releases::download(asset, &root.join("updates/downloads"), progress)?;
    let directory = root.join("updates").join(&app.tag_name);
    if directory.exists() {
        fs::remove_dir_all(&directory)?;
    }
    fs::create_dir_all(&directory)?;
    let files = releases::extract(&archive, &directory, None, 512 * 1024 * 1024, 128, progress)?;
    let exe = files
        .keys()
        .find(|path| path.rsplit('/').next() == Some("kbcs.exe"))
        .context("本体ZIPにkbcs.exeがありません")?;
    let folder = directory
        .join(exe)
        .parent()
        .context("本体フォルダなし")?
        .to_owned();
    ensure!(
        fs::read(folder.join("kbcs.exe"))?.starts_with(b"MZ"),
        "Windows実行ファイルが不正です"
    );
    let installable: Vec<_> = files
        .values()
        .filter(|file| {
            directory.join(&file.path).parent() == Some(folder.as_path())
                && Path::new(&file.path)
                    .extension()
                    .is_some_and(|ext| ext == "exe" || ext == "dll")
        })
        .map(|file| kbcs_data::source::Descriptor {
            path: Path::new(&file.path)
                .file_name()
                .unwrap()
                .to_string_lossy()
                .into_owned(),
            ..file.clone()
        })
        .collect();
    fs::write(
        folder.join(".kbcs-update-files.json"),
        serde_json::to_vec(&installable)?,
    )?;
    Ok(folder)
}

#[derive(serde::Serialize, serde::Deserialize)]
struct ApplyPlan {
    source: PathBuf,
    target: PathBuf,
    root: PathBuf,
    region: String,
    parent: u32,
}

pub fn apply_from_plan(path: &Path) -> Result<()> {
    let plan: ApplyPlan = serde_json::from_slice(&fs::read(path)?)?;
    #[cfg(not(target_os = "macos"))]
    ensure!(
        plan.target
            .file_name()
            .is_some_and(|name| name == "kbcs.exe"),
        "更新先の本体名が不正です"
    );
    #[cfg(target_os = "macos")]
    ensure!(
        macos::bundle(&macos::executable(&plan.target))? == plan.target && plan.target.is_dir(),
        "更新先のアプリが不正です"
    );
    ensure!(
        plan.target.is_absolute() && plan.target != std::env::current_exe()?,
        "更新後の起動先が不正です"
    );
    let result = apply_files(&plan);
    if let Err(error) = &result {
        fs::write(
            plan.root.join("updates/apply-error.txt"),
            format!("{error:#}"),
        )?;
    } else {
        let _ = fs::remove_file(plan.root.join("updates/apply-error.txt"));
    }
    #[cfg(not(target_os = "macos"))]
    let mut command = std::process::Command::new(&plan.target);
    #[cfg(target_os = "macos")]
    let mut command = {
        let mut command = std::process::Command::new("/usr/bin/open");
        command.arg("-n").arg(&plan.target).arg("--args");
        command
    };
    command
        .arg("--data-dir")
        .arg(&plan.root)
        .arg("--region")
        .arg(&plan.region);
    #[cfg(windows)]
    {
        use std::os::windows::process::CommandExt;
        command.creation_flags(0x08000000);
    }
    command.spawn().context("更新後のKBCSを起動できません")?;
    result
}

#[cfg(not(target_os = "macos"))]
fn apply_files(plan: &ApplyPlan) -> Result<()> {
    let current = std::env::current_exe()?.canonicalize()?;
    ensure!(
        current == plan.source.join("kbcs.exe").canonicalize()?
            && plan.source.starts_with(plan.root.join("updates"))
            && plan
                .target
                .file_name()
                .is_some_and(|name| name == "kbcs.exe"),
        "更新元・更新先が不正です"
    );
    let _lock = releases::lock(&plan.root.join("updates/apply.lock"))?;
    #[cfg(windows)]
    unsafe {
        use windows_sys::Win32::System::Threading::{
            OpenProcess, PROCESS_SYNCHRONIZE, WaitForSingleObject,
        };
        let process = OpenProcess(PROCESS_SYNCHRONIZE, 0, plan.parent);
        if !process.is_null() {
            let waited = WaitForSingleObject(process, 120_000);
            windows_sys::Win32::Foundation::CloseHandle(process);
            ensure!(waited == 0, "KBCSの終了を待てませんでした");
        }
    }
    let target = plan.target.parent().context("更新先フォルダなし")?;
    ensure!(target != plan.source, "更新元と更新先が同じです");
    let backup = plan.root.join("updates/rollback");
    fs::create_dir_all(&backup)?;
    let descriptors: Vec<kbcs_data::source::Descriptor> =
        serde_json::from_slice(&fs::read(plan.source.join(".kbcs-update-files.json"))?)?;
    ensure!(
        descriptors.iter().any(|file| file.path == "kbcs.exe"),
        "更新する本体がありません"
    );
    for descriptor in &descriptors {
        kbcs_data::source::safe_path(&descriptor.path)?;
        ensure!(
            !descriptor.path.contains('/')
                && Path::new(&descriptor.path)
                    .extension()
                    .is_some_and(|ext| ext == "exe" || ext == "dll"),
            "更新対象のパス不正"
        );
        kbcs_data::source::verify(&fs::read(plan.source.join(&descriptor.path))?, descriptor)?;
    }
    let files = descriptors
        .iter()
        .map(|file| plan.source.join(&file.path))
        .collect();
    replace_files(files, target, &backup)
}

#[cfg(any(not(target_os = "macos"), test))]
fn replace_files(files: Vec<PathBuf>, target: &Path, backup: &Path) -> Result<()> {
    let mut replaced: Vec<(PathBuf, Option<PathBuf>)> = Vec::new();
    let result = (|| -> Result<()> {
        for source in files {
            let name = source.file_name().context("更新ファイル名なし")?;
            let destination = target.join(name);
            let old = if destination.exists() {
                let old = backup.join(name);
                fs::copy(&destination, &old)?;
                Some(old)
            } else {
                None
            };
            replaced.push((destination.clone(), old));
            fs::copy(source, destination)?;
        }
        Ok(())
    })();
    if result.is_err() {
        for (destination, old) in replaced.iter().rev() {
            if let Some(old) = old {
                let _ = fs::copy(old, destination);
            } else {
                let _ = fs::remove_file(destination);
            }
        }
    }
    result
}

#[test]
fn replacement_rolls_back_all_files_on_error() -> Result<()> {
    let root = std::env::temp_dir().join(format!("kbcs-updater-{}", std::process::id()));
    let source = root.join("source");
    let target = root.join("target");
    let backup = root.join("backup");
    for directory in [&source, &target, &backup] {
        fs::create_dir_all(directory)?;
    }
    let result = (|| -> Result<()> {
        fs::write(source.join("kbcs.exe"), b"new")?;
        fs::write(source.join("new.dll"), b"added")?;
        fs::write(target.join("kbcs.exe"), b"old")?;
        assert!(
            replace_files(
                vec![
                    source.join("kbcs.exe"),
                    source.join("new.dll"),
                    source.join("missing.dll")
                ],
                &target,
                &backup
            )
            .is_err()
        );
        assert_eq!(fs::read(target.join("kbcs.exe"))?, b"old");
        assert!(!target.join("new.dll").exists());
        replace_files(
            vec![source.join("kbcs.exe"), source.join("new.dll")],
            &target,
            &backup,
        )?;
        assert_eq!(fs::read(target.join("kbcs.exe"))?, b"new");
        Ok(())
    })();
    fs::remove_dir_all(root)?;
    result
}
