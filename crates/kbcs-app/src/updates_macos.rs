use super::ApplyPlan;
use anyhow::{Context, Result, ensure};
use kbcs_data::{
    releases::{self, Release},
    source::{self, Descriptor},
};
use std::{
    fs,
    path::{Path, PathBuf},
    process::Command,
    time::{Duration, Instant},
};

pub(super) fn executable(bundle: &Path) -> PathBuf {
    bundle.join("Contents/MacOS/kbcs")
}

pub(super) fn bundle(executable: &Path) -> Result<PathBuf> {
    let bundle = executable
        .ancestors()
        .nth(3)
        .context("アプリの保存先が不明です")?;
    ensure!(
        bundle.extension().is_some_and(|ext| ext == "app")
            && self::executable(bundle) == executable,
        "KBCS.appをアプリケーションフォルダへ移動して起動してください"
    );
    Ok(bundle.to_owned())
}

fn verify_bundle(bundle: &Path) -> Result<()> {
    let bytes = fs::read(executable(bundle))?;
    let cpu = if cfg!(target_arch = "aarch64") {
        0x0100000cu32
    } else {
        0x01000007u32
    };
    ensure!(
        bytes.starts_with(&[0xcf, 0xfa, 0xed, 0xfe]) && bytes.get(4..8) == Some(&cpu.to_le_bytes()),
        "MacのCPUに対応しない実行ファイルです"
    );
    ensure!(
        Command::new("/usr/bin/codesign")
            .args(["--verify", "--deep", "--strict"])
            .arg(bundle)
            .status()?
            .success(),
        "アプリの署名検証に失敗しました"
    );
    Ok(())
}

pub(super) fn prepare(app: &Release, root: &Path, progress: &impl Fn(String)) -> Result<PathBuf> {
    let _lock = releases::lock(&root.join("download.lock"))?;
    let archive = releases::download(
        releases::app_asset(app)?,
        &root.join("updates/downloads"),
        progress,
    )?;
    let directory = root.join("updates").join(&app.tag_name);
    if directory.exists() {
        fs::remove_dir_all(&directory)?;
    }
    fs::create_dir_all(&directory)?;
    // .appの外に検証索引を置き、署名済みバンドルを変更しない。
    let files = releases::extract(
        &archive,
        &directory,
        Some("KBCS.app"),
        512 * 1024 * 1024,
        128,
        progress,
    )?;
    let bundle = directory.join("KBCS.app");
    verify_bundle(&bundle)?;
    let descriptors: Vec<_> = files
        .into_values()
        .map(|file| Descriptor {
            path: file.path.strip_prefix("KBCS.app/").unwrap().into(),
            ..file
        })
        .collect();
    fs::write(
        directory.join(".kbcs-update-files.json"),
        serde_json::to_vec(&descriptors)?,
    )?;
    Ok(bundle)
}

pub(super) fn apply(plan: &ApplyPlan) -> Result<()> {
    ensure!(
        std::env::current_exe()?.canonicalize()? == executable(&plan.source).canonicalize()?
            && plan.source.starts_with(plan.root.join("updates"))
            && plan.source != plan.target
            && bundle(&executable(&plan.target))? == plan.target
            && plan.target.is_dir(),
        "更新元・更新先が不正です"
    );
    let _lock = releases::lock(&plan.root.join("updates/apply.lock"))?;
    ensure!(
        plan.parent > 1 && plan.parent != std::process::id(),
        "待機するプロセスが不正です"
    );
    let started = Instant::now();
    loop {
        // 親が終了してからバンドルを交換する。EPERMは終了扱いにしない。
        if unsafe { libc::kill(plan.parent.try_into()?, 0) } != 0 {
            let error = std::io::Error::last_os_error();
            if error.raw_os_error() == Some(libc::ESRCH) {
                break;
            }
            return Err(error.into());
        }
        ensure!(
            started.elapsed() < Duration::from_secs(120),
            "KBCSの終了を待てませんでした"
        );
        std::thread::sleep(Duration::from_millis(50));
    }
    let descriptors: Vec<Descriptor> = serde_json::from_slice(&fs::read(
        plan.source
            .parent()
            .context("更新元フォルダなし")?
            .join(".kbcs-update-files.json"),
    )?)?;
    ensure!(
        descriptors
            .iter()
            .any(|file| file.path == "Contents/MacOS/kbcs"),
        "本体がありません"
    );
    let parent = plan.target.parent().context("更新先フォルダなし")?;
    let staging = parent.join(format!(".kbcs-update-{}.app", std::process::id()));
    let backup = parent.join(format!(".kbcs-rollback-{}.app", std::process::id()));
    ensure!(!backup.exists(), "前回の復旧用アプリが残っています");
    fs::create_dir(&staging)
        .context("更新先へ書き込めません。KBCS.appを~/Applicationsへ移動してください")?;
    let result = (|| -> Result<()> {
        for file in &descriptors {
            source::safe_path(&file.path)?;
            ensure!(
                file.path.starts_with("Contents/"),
                "バンドル内のパスが不正です"
            );
            let source = plan.source.join(&file.path).canonicalize()?;
            ensure!(source.starts_with(&plan.source), "更新元の範囲外です");
            source::verify(&fs::read(&source)?, file)?;
            let target = staging.join(&file.path);
            fs::create_dir_all(target.parent().context("コピー先なし")?)?;
            fs::copy(source, target)?;
        }
        verify_bundle(&staging)?;
        fs::rename(&plan.target, &backup)?;
        if let Err(error) = fs::rename(&staging, &plan.target) {
            fs::rename(&backup, &plan.target)
                .context("旧版の復旧に失敗しました。復旧用アプリを保持しています")?;
            return Err(error.into());
        }
        // 成功済みの旧版だけを削除する。失敗時の復旧用アプリは残す。
        let _ = fs::remove_dir_all(&backup);
        Ok(())
    })();
    if staging.exists() {
        let _ = fs::remove_dir_all(&staging);
    }
    result
}
