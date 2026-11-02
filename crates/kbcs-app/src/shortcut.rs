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

// COMのインターフェイスより長く保持し、この呼出で初期化した分だけを解放する。
#[cfg(windows)]
struct ComApartment(bool);
#[cfg(windows)]
impl ComApartment {
    fn new() -> Result<Self> {
        use windows::Win32::{
            Foundation::RPC_E_CHANGED_MODE,
            System::Com::{COINIT_APARTMENTTHREADED, CoInitializeEx},
        };
        let status = unsafe { CoInitializeEx(None, COINIT_APARTMENTTHREADED) };
        if status != RPC_E_CHANGED_MODE {
            status
                .ok()
                .context("ショートカット用COMを初期化できません")?;
        }
        Ok(Self(status.is_ok()))
    }
}
#[cfg(windows)]
impl Drop for ComApartment {
    fn drop(&mut self) {
        if self.0 {
            unsafe { windows::Win32::System::Com::CoUninitialize() };
        }
    }
}

#[cfg(windows)]
fn shell_link(path: Option<&Path>) -> Result<windows::Win32::UI::Shell::IShellLinkW> {
    use windows::{
        Win32::{
            System::Com::{CLSCTX_INPROC_SERVER, CoCreateInstance, IPersistFile, STGM_READ},
            UI::Shell::{IShellLinkW, ShellLink},
        },
        core::{HSTRING, Interface},
    };
    let link: IShellLinkW = unsafe { CoCreateInstance(&ShellLink, None, CLSCTX_INPROC_SERVER) }?;
    if let Some(path) = path {
        unsafe {
            link.cast::<IPersistFile>()?
                .Load(&HSTRING::from(shell_path(path)), STGM_READ)
        }?;
    }
    Ok(link)
}

#[cfg(windows)]
fn link_text(read: impl FnOnce(&mut [u16]) -> windows::core::Result<()>) -> Result<String> {
    let mut text = vec![0; 32768];
    read(&mut text)?;
    let length = text
        .iter()
        .position(|&ch| ch == 0)
        .context("ショートカットの文字列が長すぎます")?;
    Ok(String::from_utf16(&text[..length])?)
}

#[cfg(windows)]
fn windows_shortcut(executable: &Path, root: &Path, directory: Option<&Path>) -> Result<Shortcut> {
    use windows::{
        Win32::{
            System::Com::{CoTaskMemFree, IPersistFile},
            UI::Shell::{FOLDERID_Desktop, KF_FLAG_DEFAULT, SHGetKnownFolderPath, SLGP_RAWPATH},
        },
        core::{HSTRING, Interface},
    };
    let _apartment = ComApartment::new()?;
    let desktop = if let Some(directory) = directory {
        directory.to_owned()
    } else {
        let path = unsafe { SHGetKnownFolderPath(&FOLDERID_Desktop, KF_FLAG_DEFAULT, None) }?;
        let text = unsafe { path.to_string() };
        unsafe { CoTaskMemFree(Some(path.0.cast())) };
        PathBuf::from(text?)
    };
    ensure!(desktop.is_dir(), "デスクトップがありません");
    // 8.3短縮名・拡張接頭辞をShellへ渡す前に実在する保存先へ揃える。
    let desktop = desktop.canonicalize()?;
    let executable = executable.canonicalize()?;
    let path = desktop.join("KBCS.lnk");
    let exists = path.try_exists()?;
    let link =
        shell_link(exists.then_some(path.as_path())).context("ショートカットを開けません")?;
    let target = shell_path(&executable);
    if exists {
        let previous = link_text(|text| unsafe {
            link.GetPath(text, std::ptr::null_mut(), SLGP_RAWPATH.0 as u32)
        })?;
        let description = link_text(|text| unsafe { link.GetDescription(text) })?;
        ensure!(
            Path::new(&previous)
                .canonicalize()
                .is_ok_and(|previous| previous == executable)
                || description == "KBCS",
            "同名の別のショートカットが存在します"
        );
    }
    let arguments = format!(
        "--data-dir {}",
        quote_argument(&shell_path(&root.canonicalize()?))
    );
    let parent = executable
        .parent()
        .context("アプリの保存先に親フォルダがありません")?;
    // WScript.Shellはシステムの文字コード外のパスを拒む。リンクの全項目をUTF-16で渡す。
    unsafe {
        link.SetPath(&HSTRING::from(target.clone()))
            .context("リンクの起動先を設定できません")?;
        link.SetArguments(&HSTRING::from(arguments))?;
        link.SetWorkingDirectory(&HSTRING::from(shell_path(parent)))?;
        link.SetIconLocation(&HSTRING::from(target), 0)?;
        link.SetDescription(&HSTRING::from("KBCS"))?;
        link.cast::<IPersistFile>()?
            .Save(&HSTRING::from(shell_path(&path)), true)
            .context("デスクトップに追加できません")?;
    }
    Ok(Shortcut {
        path,
        created: !exists,
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
    use windows::{
        Win32::{
            Storage::FileSystem::GetShortPathNameW, System::Com::IPersistFile,
            UI::Shell::SLGP_RAWPATH,
        },
        core::{HSTRING, Interface},
    };
    let root = std::env::temp_dir()
        .join(format!("kbcs-shortcut-{}", std::process::id()))
        .join("日本語 space 🐱");
    std::fs::create_dir_all(&root).unwrap();
    let old = root.join("old.exe");
    std::fs::write(&old, b"test").unwrap();
    // CIのTEMPはRUNNER~1を含む。短縮名の有無に依存せず両表記で同じ保存先を使う。
    let mut buffer = vec![0; 32768];
    let length = unsafe { GetShortPathNameW(&HSTRING::from(shell_path(&root)), Some(&mut buffer)) };
    assert!(length > 0 && (length as usize) < buffer.len());
    let short_root = PathBuf::from(String::from_utf16(&buffer[..length as usize]).unwrap());
    assert!(
        windows_shortcut(&short_root.join("old.exe"), &short_root, Some(&short_root))
            .unwrap()
            .created
    );
    {
        let _apartment = ComApartment::new().unwrap();
        let link = shell_link(Some(&root.join("KBCS.lnk"))).unwrap();
        assert_eq!(
            Path::new(
                &link_text(|text| unsafe {
                    link.GetPath(text, std::ptr::null_mut(), SLGP_RAWPATH.0 as u32)
                })
                .unwrap()
            )
            .canonicalize()
            .unwrap(),
            old.canonicalize().unwrap()
        );
        // 説明による管理判定がなくても同じ実行先のリンクを更新できる。
        unsafe {
            link.SetDescription(&HSTRING::from("")).unwrap();
            link.cast::<IPersistFile>()
                .unwrap()
                .Save(&HSTRING::from(shell_path(&root.join("KBCS.lnk"))), true)
                .unwrap();
        }
    }
    assert!(!windows_shortcut(&old, &root, Some(&root)).unwrap().created);
    let executable = std::env::current_exe().unwrap();
    let repaired = windows_shortcut(&executable, &short_root, Some(&short_root)).unwrap();
    assert!(!repaired.created);
    let _apartment = ComApartment::new().unwrap();
    let link = shell_link(Some(&repaired.path)).unwrap();
    assert_eq!(
        Path::new(
            &link_text(|text| unsafe {
                link.GetPath(text, std::ptr::null_mut(), SLGP_RAWPATH.0 as u32)
            })
            .unwrap()
        )
        .canonicalize()
        .unwrap(),
        executable.canonicalize().unwrap()
    );
    assert_eq!(
        Path::new(&link_text(|text| unsafe { link.GetWorkingDirectory(text) }).unwrap())
            .canonicalize()
            .unwrap(),
        executable.parent().unwrap().canonicalize().unwrap()
    );
    assert_eq!(
        link_text(|text| unsafe { link.GetArguments(text) }).unwrap(),
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
