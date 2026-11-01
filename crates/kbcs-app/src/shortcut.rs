use anyhow::{Context, Result, ensure};
use serde::Serialize;
use std::path::{Path, PathBuf};

#[derive(Serialize)]
pub struct Shortcut {
    path: PathBuf,
    created: bool,
}

pub fn ensure_once(root: PathBuf) {
    std::thread::spawn(move || {
        let marker = root.join("user/desktop-shortcut.json");
        if marker.exists() {
            return;
        }
        // 一時配置のアプリは対象にせず、失敗で起動やデータ取得を止めない。
        if let Ok(shortcut) = create()
            && std::fs::create_dir_all(marker.parent().unwrap()).is_ok()
        {
            let _ = std::fs::write(marker, serde_json::to_vec(&shortcut).unwrap());
        }
    });
}

pub fn create() -> Result<Shortcut> {
    let executable = std::env::current_exe().context("アプリの保存先を取得できません")?;
    platform(&executable)
}

#[cfg(windows)]
fn platform(executable: &Path) -> Result<Shortcut> {
    use std::os::windows::process::CommandExt;
    // パスは環境変数で渡す。ユーザーのパスをPowerShellコードへ埋め込まない。
    let script = r#"
$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$target=[Environment]::GetEnvironmentVariable('KBCS_SHORTCUT_TARGET')
$desktop=[Environment]::GetFolderPath('DesktopDirectory')
$path=[IO.Path]::Combine($desktop,'KBCS.lnk')
$shell=New-Object -ComObject WScript.Shell
$shortcut=$shell.CreateShortcut($path)
$exists=Test-Path -LiteralPath $path
if($exists -and $shortcut.TargetPath -ne $target){throw '同名の別のショートカットが存在します。'}
if(-not $exists){
 $shortcut.TargetPath=$target
 $shortcut.WorkingDirectory=[IO.Path]::GetDirectoryName($target)
 $shortcut.IconLocation=$target+',0'
 $shortcut.Description='KBCS'
 $shortcut.Save()
}
@{path=$path;created=(-not $exists)}|ConvertTo-Json -Compress
"#;
    let output = std::process::Command::new("powershell.exe")
        .args(["-NoProfile", "-NonInteractive", "-Command", script])
        .env("KBCS_SHORTCUT_TARGET", executable)
        .creation_flags(0x08000000)
        .output()
        .context("ショートカット作成を開始できません")?;
    ensure!(
        output.status.success(),
        "ショートカット作成に失敗しました: {}",
        String::from_utf8_lossy(&output.stderr).trim()
    );
    let value: serde_json::Value = serde_json::from_slice(&output.stdout)?;
    Ok(Shortcut {
        path: PathBuf::from(
            value["path"]
                .as_str()
                .context("デスクトップ保存先がありません")?,
        ),
        created: value["created"] == true,
    })
}

#[cfg(target_os = "macos")]
fn platform(executable: &Path) -> Result<Shortcut> {
    let app = executable
        .ancestors()
        .find(|p| p.extension().is_some_and(|ext| ext == "app"))
        .context("KBCS.appから起動してください")?;
    ensure!(
        !app.components()
            .any(|part| part.as_os_str() == "AppTranslocation"),
        "KBCS.appをアプリケーションへ移動してから追加してください"
    );
    let desktop = PathBuf::from(std::env::var_os("HOME").context("ホームフォルダがありません")?)
        .join("Desktop");
    ensure!(desktop.is_dir(), "デスクトップがありません");
    let path = desktop.join("KBCS.app");
    if std::fs::symlink_metadata(&path).is_ok() {
        ensure!(
            std::fs::read_link(&path).ok().as_deref() == Some(app),
            "デスクトップに同名の別の項目が存在します"
        );
        return Ok(Shortcut {
            path,
            created: false,
        });
    }
    std::os::unix::fs::symlink(app, &path).context("デスクトップに追加できません")?;
    Ok(Shortcut {
        path,
        created: true,
    })
}

#[cfg(not(any(windows, target_os = "macos")))]
fn platform(_: &Path) -> Result<Shortcut> {
    anyhow::bail!("WindowsまたはmacOSで使用してください")
}
