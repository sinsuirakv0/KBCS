use anyhow::{Context, Result, bail};
use serde::{Deserialize, Serialize};
use unicode_normalization::UnicodeNormalization;

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Attack {
    pub damage: i64,
    pub foreswing: Option<i64>,
    pub ability_enabled: Option<i64>,
    pub range: Option<[i64; 2]>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Property {
    pub key: String,
    pub label: String,
    pub columns: Vec<usize>,
    pub values: Vec<Option<i64>>,
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Form {
    pub region: String,
    pub unit_id: u32,
    pub index: usize,
    pub name: String,
    pub description: String,
    pub rarity: i64,
    pub max_level: i64,
    pub plus_level: i64,
    pub is_spirit: bool,
    pub icon_path: Option<String>,
    pub hp: i64,
    pub speed: i64,
    pub range: i64,
    pub cost: i64,
    pub respawn_raw: i64,
    pub knockbacks: i64,
    pub interval_raw: i64,
    pub area: bool,
    pub attack_cycle: Option<i64>,
    pub animation_length: Option<i64>,
    pub attacks: Vec<Attack>,
    pub properties: Vec<Property>,
    pub raw: Vec<Option<i64>>,
    pub raw_cells: Vec<String>,
    pub growth: Vec<Option<i64>>,
    pub source_path: String,
    pub name_source: String,
    pub motion_path: String,
}

#[derive(Clone, Debug)]
pub struct UnitSummary {
    pub id: u32,
    pub name: String,
    pub forms: usize,
    pub rarity: i64,
}

#[derive(Debug, Serialize)]
pub struct Enemy {
    pub id: u32,
    pub name: String,
    pub description: String,
    pub hp: i64,
    pub knockbacks: i64,
    pub speed: i64,
    pub range: i64,
    pub drop: i64,
    pub interval_raw: i64,
    pub area: bool,
    pub attack_cycle: Option<i64>,
    pub animation_length: Option<i64>,
    pub motion_path: String,
    pub icon_path: Option<String>,
    pub raw_cells: Vec<String>,
    pub raw: Vec<Option<i64>>,
    pub attacks: Vec<Attack>,
}

pub fn normalize_query(value: &str) -> String {
    value
        .nfkc()
        .flat_map(char::to_lowercase)
        .collect::<String>()
        .chars()
        .map(|c| {
            if ('ァ'..='ヶ').contains(&c) {
                char::from_u32(c as u32 - 0x60).unwrap_or(c)
            } else {
                c
            }
        })
        .collect()
}

pub type NumericRow = (Vec<String>, Vec<Option<i64>>);

pub fn csv_rows(bytes: &[u8]) -> Result<Vec<Vec<String>>> {
    let text = std::str::from_utf8(bytes)?.trim_start_matches('\u{feff}');
    let mut reader = csv::ReaderBuilder::new()
        .has_headers(false)
        .flexible(true)
        .from_reader(text.as_bytes());
    let mut rows = Vec::new();
    for record in reader.records() {
        let record = record?;
        if record.iter().any(|cell| !cell.trim().is_empty()) {
            rows.push(record.iter().map(str::to_owned).collect());
        }
    }
    Ok(rows)
}

pub fn plain_text(text: &str) -> String {
    let text = text
        .replace("<br>", "\n")
        .replace("<br/>", "\n")
        .replace("<br />", "\n");
    let mut in_tag = false;
    text.chars()
        .filter(|&character| match character {
            '<' => {
                in_tag = true;
                false
            }
            '>' => {
                in_tag = false;
                false
            }
            _ => !in_tag,
        })
        .collect::<String>()
        .trim()
        .into()
}

pub fn numeric_rows(bytes: &[u8]) -> Result<Vec<NumericRow>> {
    let text = std::str::from_utf8(bytes)?.trim_start_matches('\u{feff}');
    let cleaned = text
        .lines()
        .map(|line| line.split_once("//").map_or(line, |(before, _)| before))
        .collect::<Vec<_>>()
        .join("\n");
    let mut rows = Vec::new();
    for cells in csv_rows(cleaned.as_bytes())? {
        let values = cells
            .iter()
            .map(|cell| {
                if cell.trim().is_empty() {
                    Ok(None)
                } else {
                    cell.trim()
                        .parse::<i64>()
                        .with_context(|| format!("数値CSVの不正なセル: {cell}"))
                        .map(Some)
                }
            })
            .collect::<Result<Vec<_>>>()?;
        rows.push((cells, values));
    }
    Ok(rows)
}

pub fn required(row: &[Option<i64>], column: usize) -> Result<i64> {
    row.get(column)
        .copied()
        .flatten()
        .with_context(|| format!("必須列が未収録: {column}"))
}

pub fn animation_length(bytes: &[u8]) -> Result<Option<i64>> {
    let text = std::str::from_utf8(bytes)?
        .trim_start_matches('\u{feff}')
        .trim();
    if text.is_empty() {
        return Ok(None);
    }
    let lines: Vec<_> = text.lines().collect();
    if !matches!(
        lines.first().copied(),
        Some("[modelanim:animation]") | Some("[modelanim:animation2]")
    ) {
        bail!("未知のモーション形式");
    }
    let line = |index: usize| -> Result<&str> {
        lines.get(index).copied().context("モーションが途中で終了")
    };
    let tracks: usize = line(2)?.trim().parse()?;
    let mut cursor = 3;
    let mut last = 0;
    for _ in 0..tracks {
        cursor += 1;
        let count: usize = line(cursor)?.trim().parse()?;
        cursor += 1;
        for _ in 0..count {
            let frame: i64 = line(cursor)?
                .split(',')
                .next()
                .context("フレームなし")?
                .trim()
                .parse()?;
            last = last.max(frame);
            cursor += 1;
        }
    }
    Ok(Some(last + 1))
}

impl Form {
    pub fn growth_percent(&self, level: usize) -> Option<i64> {
        if !(1..=200).contains(&level) {
            return None;
        }
        let mut percent = 100 - self.growth.first().copied().flatten()?;
        for current in 1..=level {
            percent += self
                .growth
                .get((current - 1) / 10)
                .copied()
                .flatten()
                .unwrap_or(0);
        }
        Some(percent)
    }
}
