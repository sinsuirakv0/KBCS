fn main() {
    println!("cargo:rerun-if-changed=../../ui");
    println!("cargo:rerun-if-changed=assets");
    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("windows") {
        let output = std::path::PathBuf::from(std::env::var_os("OUT_DIR").unwrap());
        let icon = std::path::PathBuf::from(std::env::var_os("CARGO_MANIFEST_DIR").unwrap())
            .join("assets/app.ico");
        let resource = output.join("app.rc");
        let binary = output.join("app.res");
        std::fs::write(
            &resource,
            format!("1 ICON \"{}\"\n", icon.to_string_lossy().replace('\\', "/")),
        )
        .unwrap();
        let status = std::process::Command::new("llvm-rc")
            .arg("/FO")
            .arg(&binary)
            .arg(&resource)
            .status()
            .expect("llvm-rc is required");
        assert!(status.success(), "application icon compilation failed");
        println!("cargo:rustc-link-arg-bin=kbcs={}", binary.display());
    }
}
