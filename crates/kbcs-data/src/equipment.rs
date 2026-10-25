use anyhow::{Result, ensure};
use serde_json::Value;
use std::sync::OnceLock;

// 既存DBの再構築を要求せず、採用元SHA付きの同版原本定義を使う。
pub fn capacity(version: &str, unit: u32) -> Result<usize> {
    static DEFINITION: OnceLock<Value> = OnceLock::new();
    let data = DEFINITION.get_or_init(|| {
        serde_json::from_str(include_str!("../resources/unit-equipment-slots.json"))
            .expect("組込みの本能玉スロット定義が不正です")
    });
    ensure!(
        data["version"] == version,
        "本能玉スロット定義と編成の版が異なります"
    );
    Ok(data["entries"][unit.to_string()]["count"]
        .as_u64()
        .unwrap_or(0) as usize)
}
