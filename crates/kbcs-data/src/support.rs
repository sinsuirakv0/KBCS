use serde::Serialize;
use std::collections::BTreeSet;

#[derive(Clone, Copy, Debug, Default, Eq, PartialEq, Serialize)]
#[serde(rename_all = "camelCase")]
pub enum Support {
    #[default]
    Supported,
    Unsupported,
}

impl Support {
    pub fn is_supported(self) -> bool {
        self == Self::Supported
    }
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Issue {
    pub domain: &'static str,
    pub id: i64,
}

#[derive(Serialize)]
pub struct Precision {
    pub status: &'static str,
    pub issues: BTreeSet<Issue>,
}

// 既知の構造の末尾に追加された有効値だけを別枠で表示する。
pub fn extension_cells(
    row: &[Option<i64>],
    width: usize,
) -> impl Iterator<Item = (usize, i64)> + '_ {
    row.iter()
        .enumerate()
        .skip(width)
        .filter_map(|(column, value)| {
            value
                .filter(|&value| value != 0)
                .map(|value| (column, value))
        })
}

pub fn extension_abilities(
    row: &[Option<i64>],
    width: usize,
) -> impl Iterator<Item = serde_json::Value> + '_ {
    extension_cells(row, width).map(|(column, value)| serde_json::json!({
        "key":format!("unsupported-column-{column}"),"label":format!("未実装の特性（列 {column}）"),
        "support":Support::Unsupported,"column":column,"value":value,
    }))
}

pub fn picture_book_extensions(
    database: &crate::store::Database,
) -> anyhow::Result<Vec<serde_json::Value>> {
    use crate::model::{numeric_rows, required};
    const PATH: &str = "Data/nyankoPictureBookData_EffectAbility.csv";
    if !database.connection.query_row(
        "SELECT EXISTS(SELECT 1 FROM asset_reference WHERE path=?1 UNION ALL SELECT 1 FROM source_file WHERE path=?1)",
        [PATH], |row| row.get::<_, bool>(0),
    )? { return Ok(Vec::new()); }
    let mut extensions = Vec::new();
    for (_, row) in numeric_rows(&database.source(PATH)?.3)? {
        let id = required(&row, 0)?;
        let ability = required(&row, 1)?;
        let talent = required(&row, 3)?;
        required(&row, 6)?;
        if id < 88 {
            continue;
        }
        let support = if ability == -1 && talent == crate::talents::COMBO_UNLOCK {
            Support::Supported
        } else {
            Support::Unsupported
        };
        extensions.push(serde_json::json!({"id":id,"abilityId":ability,"talentId":talent,"support":support,"raw":row}));
    }
    Ok(extensions)
}

#[test]
fn new_nonzero_ability_cells_keep_source_index_and_value() {
    let rows = [Some(7), Some(0), None, Some(-3), Some(42)];
    let effects: Vec<_> = extension_abilities(&rows, 1).collect();
    assert_eq!(effects.len(), 2);
    assert_eq!(effects[0]["support"], "unsupported");
    assert_eq!(effects[0]["column"], 3);
    assert_eq!(effects[0]["value"], -3);
}

impl Precision {
    pub fn checked() -> Self {
        Self {
            status: "exact",
            issues: BTreeSet::new(),
        }
    }

    pub fn note(&mut self, domain: &'static str, id: i64) {
        self.status = "partial";
        self.issues.insert(Issue { domain, id });
    }
}
