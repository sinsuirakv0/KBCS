use anyhow::{Result, ensure};
use serde_json::Value;
use std::sync::OnceLock;

pub fn capacities(
    database: &crate::store::Database,
) -> Result<std::collections::BTreeMap<u32, usize>> {
    let metadata = database.metadata()?;
    let path = "Data/equipmentslot.csv";
    let bytes = if let Ok((_, _, _, bytes)) = database.source(path) {
        Some(bytes)
    } else if database.connection.query_row(
        "SELECT EXISTS(SELECT 1 FROM asset_reference WHERE path=?)",
        [path],
        |row| row.get::<_, bool>(0),
    )? {
        let root = database
            .connection
            .path()
            .and_then(|path| std::path::Path::new(path).parent())
            .and_then(|path| path.parent())
            .ok_or_else(|| anyhow::anyhow!("公式DBの保存先がありません"))?;
        Some(crate::source::asset(database, root, path)?)
    } else {
        None
    };
    if let Some(bytes) = bytes {
        let mut entries = std::collections::BTreeMap::new();
        for (_, row) in crate::model::numeric_rows(&bytes)? {
            let id = u32::try_from(crate::model::required(&row, 0)?)?;
            let count = usize::try_from(crate::model::required(&row, 1)?)?;
            ensure!(
                count <= 2 && entries.insert(id, count).is_none(),
                "本能玉の枠数・キャラIDが不正です"
            );
        }
        return Ok(entries);
    }
    let mut entries = std::collections::BTreeMap::new();
    for unit in database.search(&metadata["region"], "", false)? {
        entries.insert(unit.id, capacity(&metadata["version"], unit.id)?);
    }
    Ok(entries)
}

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
