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
            // ユーザーが削除したリンクは復活させず、残っている管理リンクだけ更新する。
            let present = std::fs::read(&marker)
                .ok()
                .and_then(|bytes| serde_json::from_slice::<serde_json::Value>(&bytes).ok())
                .and_then(|value| value["path"].as_str().map(PathBuf::from))
                .is_some_and(|path| path.exists());
            if !present {
                return;
            }
        }
        // 一時配置のアプリは対象にせず、失敗で起動やデータ取得を止めない。
        if let Ok(shortcut) = create(&root)
            && std::fs::create_dir_all(marker.parent().unwrap()).is_ok()
        {
            let _ = std::fs::write(marker, serde_json::to_vec(&shortcut).unwrap());
        }
    });
}

pub fn create(root: &Path) -> Result<Shortcut> {
    let executable = std::env::current_exe().context("アプリの保存先を取得できません")?;
    platform(&executable, root)
}

#[cfg(windows)]
fn platform(executable: &Path, root: &Path) -> Result<Shortcut> {
    windows_shortcut(executable, root, None)
}

#[cfg(windows)]
fn windows_shortcut(executable: &Path, root: &Path, directory: Option<&Path>) -> Result<Shortcut> {
    use std::os::windows::process::CommandExt;
    // パスは環境変数で渡す。ユーザーのパスをPowerShellコードへ埋め込まない。
    let script = r#"
$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$target=[Environment]::GetEnvironmentVariable('KBCS_SHORTCUT_TARGET')
$arguments=[Environment]::GetEnvironmentVariable('KBCS_SHORTCUT_ARGUMENTS')
$desktop=[Environment]::GetEnvironmentVariable('KBCS_SHORTCUT_DIRECTORY')
if(-not $desktop){$desktop=[Environment]::GetFolderPath('DesktopDirectory')}
$path=[IO.Path]::Combine($desktop,'KBCS.lnk')
$shell=New-Object -ComObject WScript.Shell
$shortcut=$shell.CreateShortcut($path)
$exists=Test-Path -LiteralPath $path
if($exists -and $shortcut.TargetPath -ne $target -and $shortcut.Description -ne 'KBCS'){throw '同名の別のショートカットが存在します。'}
 $shortcut.TargetPath=$target
 $shortcut.Arguments=$arguments
 $shortcut.WorkingDirectory=[IO.Path]::GetDirectoryName($target)
 $shortcut.IconLocation=$target+',0'
 $shortcut.Description='KBCS'
 $shortcut.Save()
@{path=$path;created=(-not $exists)}|ConvertTo-Json -Compress
"#;
    let output = std::process::Command::new("powershell.exe")
        .args(["-NoProfile", "-NonInteractive", "-Command", script])
        .env("KBCS_SHORTCUT_TARGET", shell_path(executable))
        .env(
            "KBCS_SHORTCUT_DIRECTORY",
            directory.unwrap_or(Path::new("")),
        )
        .env(
            "KBCS_SHORTCUT_ARGUMENTS",
            format!(
                "--data-dir {}",
                quote_argument(&shell_path(&root.canonicalize()?))
            ),
        )
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

#[cfg(windows)]
fn shell_path(path: &Path) -> String {
    let text = path.to_string_lossy();
    if let Some(network) = text.strip_prefix(r"\\?\UNC\") {
        format!(r"\\{network}")
    } else {
        text.strip_prefix(r"\\?\").unwrap_or(&text).to_owned()
    }
}

#[cfg(windows)]
fn quote_argument(value: &str) -> String {
    // Windowsのargv規則。末尾の区切り文字が閉じ引用符を消費しないようにする。
    let mut out = String::from("\"");
    let mut slashes = 0;
    for ch in value.chars() {
        if ch == '\\' {
            slashes += 1;
            continue;
        }
        out.extend(std::iter::repeat_n(
            '\\',
            if ch == '"' { slashes * 2 + 1 } else { slashes },
        ));
        slashes = 0;
        out.push(ch);
    }
    out.extend(std::iter::repeat_n('\\', slashes * 2));
    out.push('"');
    out
}

#[cfg(target_os = "macos")]
fn platform(executable: &Path, _root: &Path) -> Result<Shortcut> {
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
fn platform(_: &Path, _: &Path) -> Result<Shortcut> {
    anyhow::bail!("WindowsまたはmacOSで使用してください")
}

#[cfg(all(test, windows))]
#[test]
fn managed_shortcut_refreshes_target_and_preserves_data_directory() {
    use std::os::windows::process::CommandExt;
    let root = std::env::temp_dir()
        .join(format!("kbcs-shortcut-{}", std::process::id()))
        .join("日本語 space");
    std::fs::create_dir_all(&root).unwrap();
    let old = root.join("old.exe");
    std::fs::write(&old, b"test").unwrap();
    assert!(windows_shortcut(&old, &root, Some(&root)).unwrap().created);
    let executable = std::env::current_exe().unwrap();
    let repaired = windows_shortcut(&executable, &root, Some(&root)).unwrap();
    assert!(!repaired.created);
    let output=std::process::Command::new("powershell.exe").args(["-NoProfile","-NonInteractive","-Command",r#"
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$s=(New-Object -ComObject WScript.Shell).CreateShortcut($env:KBCS_SHORTCUT_TEST)
@{target=$s.TargetPath;arguments=$s.Arguments;directory=$s.WorkingDirectory}|ConvertTo-Json -Compress
"#]).env("KBCS_SHORTCUT_TEST",&repaired.path).creation_flags(0x08000000).output().unwrap();
    assert!(output.status.success());
    let value: serde_json::Value = serde_json::from_slice(&output.stdout).unwrap();
    assert_eq!(value["target"], shell_path(&executable));
    assert_eq!(value["directory"], shell_path(executable.parent().unwrap()));
    assert_eq!(
        value["arguments"],
        format!(
            "--data-dir {}",
            quote_argument(&shell_path(&root.canonicalize().unwrap()))
        )
    );
    assert_eq!(quote_argument(r"C:\"), "\"C:\\\\\"");
    std::fs::remove_file(repaired.path).unwrap();
    std::fs::remove_file(old).unwrap();
    std::fs::remove_dir(&root).unwrap();
    std::fs::remove_dir(root.parent().unwrap()).unwrap();
}
