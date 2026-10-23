use super::*;

pub const SOURCES: &[&str] = &[
    "Data/equipmentlist.json",
    "Data/equipmentgrade.csv",
    "res/equipment_explonation.tsv",
    "Image/equipment_attribute.png",
    "Image/equipment_effect.png",
    "Image/equipment_grade.png",
    "ImageData/equipment_attribute.imgcut",
    "ImageData/equipment_effect.imgcut",
    "ImageData/equipment_grade.imgcut",
];

// 報酬IDから本能玉の定義を選び、原本の名前と重ね描き用矩形を返す。
pub fn decorate(database: &Database, rewards: &mut BTreeMap<String, Value>) -> Result<()> {
    if !database.connection.query_row(
        "SELECT EXISTS(SELECT 1 FROM source_file WHERE path=?)",
        [SOURCES[0]],
        |r| r.get::<_, bool>(0),
    )? {
        return Ok(());
    }
    let read = |path: &str| -> Result<Vec<u8>> { Ok(database.source(path)?.3) };
    let equipment: Value = serde_json::from_slice(&read(SOURCES[0])?)?;
    let grades = csv_rows(&read(SOURCES[1])?)?
        .into_iter()
        .filter(|row| row.first().is_some_and(|v| v.trim().parse::<i64>().is_ok()))
        .collect::<Vec<_>>();
    let description = String::from_utf8(read(SOURCES[2])?)?;
    let names = description
        .trim_start_matches('\u{feff}')
        .lines()
        .map(|l| l.split('\t').next().unwrap_or(""))
        .collect::<Vec<_>>();
    let mut atlases = Vec::new();
    for kind in ["attribute", "effect", "grade"] {
        let path = format!("Image/equipment_{kind}.png");
        let png = read(&path)?;
        anyhow::ensure!(
            png.len() >= 24 && png.starts_with(b"\x89PNG\r\n\x1a\n"),
            "本能玉アイコンのPNG形式不正"
        );
        let width = u32::from_be_bytes(png[16..20].try_into()?);
        let height = u32::from_be_bytes(png[20..24].try_into()?);
        let cut = String::from_utf8(read(&format!("ImageData/equipment_{kind}.imgcut"))?)?;
        let cells = csv_rows(
            cut.trim_start_matches('\u{feff}')
                .lines()
                .skip(4)
                .collect::<Vec<_>>()
                .join("\n")
                .as_bytes(),
        )?;
        let mut rows = Vec::new();
        for cell in cells {
            let rect = cell
                .iter()
                .take(4)
                .map(|v| v.parse::<u32>())
                .collect::<std::result::Result<Vec<_>, _>>()?;
            anyhow::ensure!(rect.len() == 4, "本能玉の切抜き矩形欠測");
            rows.push((
                json!({"path":path,"width":width,"height":height,"rect":rect}),
                cell.get(4).cloned().unwrap_or_default(),
            ));
        }
        atlases.push(rows);
    }
    for (id, reward) in rewards {
        let Some(index) = id
            .parse::<usize>()
            .ok()
            .and_then(|id| id.checked_sub(30000))
        else {
            continue;
        };
        let Some(item) = equipment["ID"].as_array().and_then(|a| a.get(index)) else {
            continue;
        };
        let grade = item["gradeID"].as_u64().context("本能玉ランク欠測")? as usize;
        let effect = item["content"].as_u64().context("本能玉効果欠測")? as usize;
        let attribute = item["attribute"].as_u64().unwrap_or(12) as usize;
        let grade_name = grades
            .get(grade)
            .and_then(|r| r.get(3))
            .context("本能玉ランク名欠測")?;
        let attribute_name = if attribute == 12 {
            ""
        } else {
            atlases[0]
                .get(attribute)
                .context("本能玉属性欠測")?
                .1
                .as_str()
        };
        let name = names
            .get(effect)
            .context("本能玉効果名欠測")?
            .replacen("%@", grade_name, 1)
            .replacen("%@", attribute_name, 1);
        reward["name"] = json!(format!("本能玉 {}", crate::model::plain_text(&name)));
        reward["equipment"] = item.clone();
        reward["layers"] = json!(
            [
                atlases[0].get(attribute),
                atlases[1].get(effect),
                atlases[2].get(grade)
            ]
            .into_iter()
            .flatten()
            .map(|r| r.0.clone())
            .collect::<Vec<_>>()
        );
    }
    Ok(())
}
