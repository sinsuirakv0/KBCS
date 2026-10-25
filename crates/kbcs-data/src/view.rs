use crate::{
    model::{Form, Property},
    store::Database,
};
use anyhow::Result;
use serde_json::{Value, json};
use std::collections::BTreeMap;

fn ability(property: &Property) -> Value {
    let get = |column| {
        property
            .columns
            .iter()
            .position(|&c| c == column)
            .and_then(|index| property.values[index])
    };
    let key = if property.key == "wave" && get(94).is_some_and(|v| v != 0) {
        "mini-wave"
    } else if property.key == "surge" && get(108).is_some_and(|v| v != 0) {
        "mini-surge"
    } else {
        &property.key
    };
    let mut value = json!({"key":key,"label":match key{"wave"=>"波動","mini-wave"=>"小波動","surge"=>"烈波","mini-surge"=>"小烈波",_=>&property.label}});
    for (name, column) in match property.key.as_str() {
        "knockback" => vec![("probability", 24)],
        "stop" => vec![("probability", 25), ("duration", 26)],
        "slow" => vec![("probability", 27), ("duration", 28)],
        "critical" => vec![("probability", 31)],
        "weaken" => vec![("probability", 37), ("duration", 38), ("percent", 39)],
        "survive" => vec![("probability", 42)],
        "barrier" => vec![("probability", 70)],
        "savage" => vec![("probability", 82)],
        "dodge" => vec![("probability", 84), ("duration", 85)],
        "curse" => vec![("probability", 92), ("duration", 93)],
        "shield" => vec![("probability", 95)],
        "blast" => vec![("probability", 113)],
        "wave" => vec![("probability", 35), ("level", 36)],
        "surge" => vec![("probability", 86), ("level", 89)],
        "spirit" => vec![("unitId", 110)],
        "metal-killer" => vec![("percent", 112)],
        "behemoth" => vec![("probability", 106), ("duration", 107)],
        "alternate-respawn" => vec![("percent", 118)],
        _ => vec![],
    } {
        if let Some(number) = get(column) {
            value[name] = json!(number);
        }
    }
    if key.ends_with("-immune") {
        value["resistance"] = json!(100);
    }
    if key == "strengthen" {
        value["health"] = json!(get(40));
        value["power"] = json!(get(41).map(|v| v + 100));
    }
    if key == "savage" {
        value["power"] = json!(get(83).map(|v| v + 100));
    }
    let columns = match property.key.as_str() {
        "surge" => Some((87, 88)),
        "blast" => Some((114, 115)),
        _ => None,
    };
    if let Some((start, width)) = columns
        && let Some((start, width)) = get(start).zip(get(width))
    {
        value["range"] = json!([start as f64 / 4.0, (start + width) as f64 / 4.0]);
    }
    value
}

fn form_value(form: &Form) -> Value {
    let pre = form
        .attacks
        .iter()
        .filter_map(|attack| attack.foreswing)
        .max();
    let targets: Vec<_> = form
        .properties
        .iter()
        .filter(|property| property.key.starts_with("target-") && property.key != "target-only")
        .map(|p| p.key.trim_start_matches("target-"))
        .collect();
    let abilities: Vec<_> = form
        .properties
        .iter()
        .filter(|p| !p.key.starts_with("target-") || p.key == "target-only")
        .map(ability)
        .collect();
    let raw = |index| form.raw.get(index).copied().flatten();
    json!({"name":form.name,"description":form.description,"index":form.index,"code":(["f","c","s","u"][form.index]),"hp":form.hp,"knockbacks":form.knockbacks,"speed":form.speed,"attacks":form.attacks.iter().map(|a|a.damage).collect::<Vec<_>>(),"foreswings":form.attacks.iter().map(|a|a.foreswing).collect::<Vec<_>>(),"attackCycle":form.attack_cycle,"backswing":form.animation_length.zip(pre).map(|(length,pre)|(length-pre).max(0)),"range":form.range,"castleRange":if raw(45).is_some_and(|v|v!=0){raw(44)}else{Some(form.range)},"cost":form.cost,"respawn":form.respawn_raw*2,"attackInterval":form.interval_raw,"attackType":if form.area{"範囲"}else{"単体"},"targets":targets,"abilities":abilities,"icon":form.icon_path,"ranges":form.attacks.iter().filter_map(|a|a.range).filter(|[a,b]|a!=b).map(|[a,b]|[a.min(b),a.max(b)]).collect::<Vec<_>>(),"width":raw(9),"layers":[raw(14),raw(15)]})
}

pub fn catalog(database: &Database, region: &str) -> Result<Value> {
    let metadata = database.metadata()?;
    let mut units = Vec::new();
    let mut growth = Vec::new();
    let mut abilities = BTreeMap::new();
    let combos = crate::combos::read(&database.connection, region)?;
    let combo_effects = crate::combos::effects(&database.connection, region)?;
    for summary in database.search(region, "", false)? {
        let mut forms = Vec::new();
        let mut original = None;
        for index in 0..summary.forms {
            let form = database.form(region, summary.id, index)?;
            let value = form_value(&form);
            for ability in value["abilities"].as_array().into_iter().flatten() {
                abilities.insert(
                    ability["key"].as_str().unwrap_or_default().to_owned(),
                    json!({"key":ability["key"],"label":ability["label"]}),
                );
            }
            if original.is_none() {
                original = Some(form);
            }
            forms.push(value);
        }
        let original = original.ok_or_else(|| anyhow::anyhow!("形態なし"))?;
        growth.push(
            (0..=200)
                .map(|level| {
                    if level == 0 {
                        Some(0)
                    } else {
                        original.growth_percent(level)
                    }
                })
                .collect::<Vec<_>>(),
        );
        let (aliases, kind): (String, String) = database.connection.query_row(
            "SELECT aliases,kind FROM unit WHERE region=? AND id=?",
            rusqlite::params![region, summary.id],
            |row| Ok((row.get(0)?, row.get(1)?)),
        )?;
        let talents = crate::talents::read(&database.connection, region, summary.id)?;
        for talent in &talents {
            if let Some(label) = &talent.effect.label {
                abilities
                    .entry(talent.effect.key.clone())
                    .or_insert_with(|| json!({"key":talent.effect.key,"label":label}));
            }
        }
        let progression = crate::progression::read(&database.connection, region, summary.id)?;
        let acquisition = progression
            .iter()
            .find(|value| value.form == 0)
            .map(|value| json!({"description":value.description,"stages":value.stages}))
            .unwrap_or_else(|| json!({"description":"","stages":[]}));
        let evolution: Vec<_> = progression
            .into_iter()
            .filter(|value| value.form > 0)
            .collect();
        let unit_combos: Vec<_> = combos
            .iter()
            .filter(|combo| {
                combo
                    .members
                    .iter()
                    .any(|member| member.id == summary.id as i64)
            })
            .map(|combo| combo.id)
            .collect();
        units.push(json!({"id":summary.id,"aliases":[aliases],"rarity":summary.rarity,"orbSlots":crate::equipment::capacity(&metadata["version"],summary.id)?,"maxLevel":original.max_level,"plusLevel":original.plus_level,"growth":growth.len()-1,"forms":forms,"talents":talents,"combos":unit_combos,"evolution":evolution,"acquisition":acquisition,"isSpirit":original.is_spirit,"kind":if original.is_spirit{"spirit"}else{&kind}}));
    }
    let mut summoners: BTreeMap<u32, Vec<(u32, usize, String)>> = BTreeMap::new();
    for unit in &units {
        for form in unit["forms"].as_array().into_iter().flatten() {
            for ability in form["abilities"]
                .as_array()
                .into_iter()
                .flatten()
                .filter(|a| a["key"] == "spirit")
            {
                if let (Some(child), Some(parent), Some(index), Some(name)) = (
                    ability["unitId"].as_u64(),
                    unit["id"].as_u64(),
                    form["index"].as_u64(),
                    form["name"].as_str(),
                ) {
                    summoners.entry(child as u32).or_default().push((
                        parent as u32,
                        index as usize,
                        name.into(),
                    ));
                }
            }
        }
    }
    for unit in &mut units {
        if unit["isSpirit"] == true
            && let Some(parents) = unit["id"]
                .as_u64()
                .and_then(|id| summoners.get(&(id as u32)))
        {
            let names = parents
                .iter()
                .map(|(_, index, name)| format!("{name}・第{}形態", index + 1))
                .collect::<Vec<_>>()
                .join(" / ");
            unit["forms"][0]["name"] = json!(format!("精霊（{names}）"));
            if let Some(aliases) = unit["aliases"].as_array_mut() {
                aliases.extend(parents.iter().map(|(_, _, name)| json!(name)));
            }
        }
    }
    let atlas = property_atlas(database, &BTreeMap::new())?;
    let targets: Vec<_> = [
        ("red", "赤い敵"),
        ("floating", "浮いてる敵"),
        ("black", "黒い敵"),
        ("metal", "メタル"),
        ("white", "無属性"),
        ("angel", "天使"),
        ("alien", "エイリアン"),
        ("zombie", "ゾンビ"),
        ("relic", "古代種"),
        ("aku", "悪魔"),
    ]
    .iter()
    .map(|(key, label)| json!({"key":key,"label":label}))
    .collect();
    Ok(
        json!({"schemaVersion":9,"gameVersion":metadata.get("version"),"revision":metadata.get("revision"),"datasetId":metadata.get("dataset_id"),"buildId":metadata.get("build_id"),"imageBase":"/api/asset/","propertyAtlas":atlas,"targets":targets,"abilities":abilities.into_values().collect::<Vec<_>>(),"growth":growth,"units":units,"combos":combos,"comboEffects":combo_effects,"native":{"talents":true}}),
    )
}

pub(crate) fn property_atlas(
    database: &Database,
    extra: &BTreeMap<String, usize>,
) -> Result<Value> {
    let (_, _, _, png) = database.source("Image/img015.png")?;
    anyhow::ensure!(
        png.len() >= 24 && png.starts_with(b"\x89PNG\r\n\x1a\n") && &png[12..16] == b"IHDR",
        "特性アトラスのPNG形式が不正です"
    );
    let width = u32::from_be_bytes(png[16..20].try_into()?);
    let height = u32::from_be_bytes(png[20..24].try_into()?);
    let mut icons: Value = serde_json::from_str(include_str!("../resources/property-icons.json"))?;
    for (key, index) in extra {
        icons[key] = json!(index);
    }
    let (_, _, _, bytes) = database.source("ImageData/img015.imgcut")?;
    let text = std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}');
    let rows: Vec<_> = text
        .lines()
        .skip(4)
        .map(|line| line.split(',').collect::<Vec<_>>())
        .collect();
    let mut rectangles = BTreeMap::new();
    for (key, index) in icons.as_object().into_iter().flatten() {
        if let Some(row) = index.as_u64().and_then(|i| rows.get(i as usize)) {
            let rect = row
                .iter()
                .take(4)
                .map(|v| v.trim().parse::<u32>())
                .collect::<std::result::Result<Vec<_>, _>>()?;
            rectangles.insert(key.clone(), rect);
        }
    }
    for (index, name) in ["基本", "EX", "レア", "激レア", "超激レア", "伝説レア"]
        .iter()
        .enumerate()
    {
        let expected = format!("キャラ詳細画面 {name} 文字");
        if let Some(row) = rows.iter().find(|row| {
            row.get(4).is_some_and(|name| {
                crate::model::normalize_query(name)
                    .split_whitespace()
                    .collect::<Vec<_>>()
                    .join(" ")
                    == crate::model::normalize_query(&expected)
            })
        }) {
            rectangles.insert(
                format!("rarity-{index}"),
                row.iter()
                    .take(4)
                    .map(|v| v.trim().parse::<u32>())
                    .collect::<std::result::Result<Vec<_>, _>>()?,
            );
        }
    }
    Ok(json!({"path":"Image/img015.png","width":width,"height":height,"icons":rectangles}))
}
