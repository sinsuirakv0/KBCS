use anyhow::{Result, ensure};
use serde_json::{Value, json};
use std::path::Path;

pub fn space(path: &Path) -> Option<Value> {
    let mut directory = path;
    while !directory.exists() {
        directory = directory.parent()?;
    }
    #[cfg(windows)]
    unsafe {
        use std::os::windows::ffi::OsStrExt;
        #[link(name = "kernel32")]
        unsafe extern "system" {
            fn GetDiskFreeSpaceExW(
                path: *const u16,
                available: *mut u64,
                total: *mut u64,
                free: *mut u64,
            ) -> i32;
        }
        let name: Vec<u16> = directory.as_os_str().encode_wide().chain(Some(0)).collect();
        let (mut available, mut total, mut free) = (0, 0, 0);
        if GetDiskFreeSpaceExW(name.as_ptr(), &mut available, &mut total, &mut free) != 0 {
            return Some(json!({"available":available,"total":total}));
        }
    }
    #[cfg(target_os = "macos")]
    unsafe {
        use std::os::unix::ffi::OsStrExt;
        let name = std::ffi::CString::new(directory.as_os_str().as_bytes()).ok()?;
        let mut info: libc::statvfs = std::mem::zeroed();
        if libc::statvfs(name.as_ptr(), &mut info) == 0 {
            return Some(
                json!({"available":u64::from(info.f_bavail).saturating_mul(info.f_frsize),"total":u64::from(info.f_blocks).saturating_mul(info.f_frsize)}),
            );
        }
    }
    None
}
pub fn require(path: &Path, needed: u64) -> Result<()> {
    if let Some(available) = space(path).and_then(|v| v["available"].as_u64()) {
        ensure!(
            available >= needed,
            "保存先の空き容量が不足しています。必要 約{:.2}GiB / 空き 約{:.2}GiB: {}",
            needed as f64 / 1_073_741_824.,
            available as f64 / 1_073_741_824.,
            path.display()
        );
    }
    Ok(())
}
