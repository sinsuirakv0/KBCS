use crate::{
    import::read_asset,
    model::{Attack, Enemy, animation_length, csv_rows, numeric_rows, plain_text, required},
    source::{Dataset, Source},
    store::Database,
};
use anyhow::{Result, ensure};
use rusqlite::{Connection, params};
use serde::Deserialize;
use serde_json::{Value, json};
use std::{collections::BTreeMap, sync::OnceLock};

type Field = (usize, String, String);
#[derive(Deserialize)]
struct Definitions {
    attributes: Vec<Field>,
    species: Vec<Field>,
    fixed: Vec<Field>,
    immunities: Vec<Field>,
    probabilities: Vec<(usize, String, String, Option<usize>)>,
    castles: Vec<u32>,
    icons: BTreeMap<String, usize>,
}
fn definitions() -> &'static Definitions {
    static DEFINITIONS: OnceLock<Definitions> = OnceLock::new();
    DEFINITIONS.get_or_init(|| {
        serde_json::from_str(include_str!("../resources/enemy-fields.json"))
            .expect("組込みの敵定義が不正です")
    })
}

pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &impl Fn(String),
) -> Result<()> {
    let path = "Data/t_unit.csv";
    if !dataset.files.contains_key(path) {
        return Ok(());
    }
    let region = &dataset.current.header.source_region;
    let bytes = read_asset(source, dataset, connection, "res/Enemyname.tsv")?;
    let names: Vec<_> = std::str::from_utf8(&bytes)?
        .trim_start_matches('\u{feff}')
        .lines()
        .map(|line| line.split('\t').next().unwrap_or("").trim())
        .collect();
    let descriptions = csv_rows(&read_asset(
        source,
        dataset,
        connection,
        "res/EnemyPictureBook_ja.csv",
    )?)?;
    let rows = numeric_rows(&read_asset(source, dataset, connection, path)?)?;
    ensure!(rows.len() > 2, "敵CSVに本体データがありません");
    for (id, (cells, row)) in rows.into_iter().skip(2).enumerate() {
        let name = names
            .get(id)
            .filter(|name| !name.is_empty())
            .map(|name| (*name).to_owned())
            .unwrap_or_else(|| format!("敵 {id}"));
        let description = descriptions
            .get(id)
            .map(|row| {
                row.iter()
                    .skip(1)
                    .map(|text| plain_text(text))
                    .filter(|text| !text.is_empty())
                    .collect::<Vec<_>>()
                    .join("\n")
            })
            .unwrap_or_default();
        let number = |column| row.get(column).copied().flatten().unwrap_or(0);
        let hit_count = if number(55) != 0 {
            if number(56) != 0 { 3 } else { 2 }
        } else {
            1
        };
        let motion = format!("ImageData/{id:03}_e02.maanim");
        let length = if dataset.files.contains_key(&motion) {
            animation_length(&read_asset(source, dataset, connection, &motion)?)?
        } else {
            None
        };
        let foreswings: Vec<_> = [12, 57, 58]
            .into_iter()
            .take(hit_count)
            .map(&number)
            .collect();
        let pre = foreswings.iter().copied().max().unwrap_or(0);
        let cycle = length.map(|length| length.max(pre + number(4) * 2 - 1));
        let icon = format!("Image/enemy_icon_{id:03}.png");
        let icon = if dataset.files.contains_key(&icon) {
            read_asset(source, dataset, connection, &icon)?;
            Some(icon)
        } else {
            None
        };
        connection.execute(
            "INSERT INTO enemy VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            params![
                region,
                id as i64,
                name,
                description,
                required(&row, 0)?,
                required(&row, 1)?,
                required(&row, 2)?,
                required(&row, 5)?,
                required(&row, 6)?,
                required(&row, 4)?,
                number(11) != 0,
                cycle,
                length,
                motion,
                icon,
                serde_json::to_string(&cells)?,
                path
            ],
        )?;
        for (hit, damage) in [3, 55, 56].into_iter().take(hit_count).enumerate() {
            let offset = if hit > 0 && number(95 + (hit - 1) * 3) != 0 {
                96 + (hit - 1) * 3
            } else {
                35
            };
            let value = |column| row.get(column).copied().flatten();
            connection.execute(
                "INSERT INTO enemy_attack VALUES (?,?,?,?,?,?,?,?)",
                params![
                    region,
                    id as i64,
                    hit as i64,
                    required(&row, damage)?,
                    value([12, 57, 58][hit]),
                    value(59 + hit),
                    value(offset),
                    value(offset)
                        .zip(value(offset + 1))
                        .map(|(start, width)| start + width)
                ],
            )?;
        }
        if id % 100 == 0 {
            progress(format!("敵取り込み: {}", id + 1));
        }
    }
    Ok(())
}

pub fn read(connection: &Connection, region: &str) -> Result<Vec<Enemy>> {
    let mut statement=connection.prepare("SELECT id,name,description,hp,knockbacks,speed,range,drop_amount,interval_raw,area,attack_cycle,animation_length,motion_path,icon_path,raw_cells FROM enemy WHERE region=? ORDER BY id")?;
    let records = statement.query_map([region], |row| {
        Ok((
            Enemy {
                id: row.get(0)?,
                name: row.get(1)?,
                description: row.get(2)?,
                hp: row.get(3)?,
                knockbacks: row.get(4)?,
                speed: row.get(5)?,
                range: row.get(6)?,
                drop: row.get(7)?,
                interval_raw: row.get(8)?,
                area: row.get(9)?,
                attack_cycle: row.get(10)?,
                animation_length: row.get(11)?,
                motion_path: row.get(12)?,
                icon_path: row.get(13)?,
                raw_cells: Vec::new(),
                raw: Vec::new(),
                attacks: Vec::new(),
            },
            row.get::<_, String>(14)?,
        ))
    })?;
    let mut result = Vec::new();
    for record in records {
        let (mut enemy, cells) = record?;
        enemy.raw_cells = serde_json::from_str(&cells)?;
        enemy.raw = enemy
            .raw_cells
            .iter()
            .map(|value| value.trim().parse().ok())
            .collect();
        enemy.attacks=connection.prepare("SELECT damage,foreswing,ability_enabled,range_start,range_end FROM enemy_attack WHERE region=? AND enemy_id=? ORDER BY hit")?
            .query_map(params![region,enemy.id],|row|Ok(Attack{damage:row.get(0)?,foreswing:row.get(1)?,ability_enabled:row.get(2)?,range:row.get::<_,Option<i64>>(3)?.zip(row.get(4)?).map(|(start,end)|[start,end])}))?.collect::<rusqlite::Result<_>>()?;
        result.push(enemy);
    }
    Ok(result)
}

fn abilities(row: &[Option<i64>]) -> Vec<Value> {
    let get = |column| row.get(column).copied().flatten().unwrap_or(0);
    let definitions = definitions();
    let mut result: Vec<_> = definitions
        .fixed
        .iter()
        .filter(|(column, _, _)| get(*column) > 0)
        .map(|(_, key, label)| json!({"key":key,"label":label}))
        .collect();
    for (column, key, label, time) in &definitions.probabilities {
        if get(*column) > 0 {
            let mut value = json!({"key":key,"label":label,"probability":get(*column)});
            if let Some(time) = time {
                value["duration"] = json!(get(*time));
            }
            result.push(value);
        }
    }
    for (column, key, label) in &definitions.immunities {
        if get(*column) > 0 {
            result.push(json!({"key":format!("{key}-immune"),"label":format!("{label}無効"),"resistance":100}));
        }
    }
    if get(27) > 0 {
        result.push(json!({"key":if get(86)!=0{"mini-wave"}else{"wave"},"label":if get(86)!=0{"小波動"}else{"波動"},"probability":get(27),"level":get(28)}));
    }
    if get(33) > 0 {
        result.push(
            json!({"key":"strengthen","label":"攻撃力アップ","health":get(32),"power":100+get(33)}),
        );
    }
    if get(43) != 0 {
        result.push(
            json!({"key":"burrow","label":"潜行","count":get(43),"distance":get(44) as f64/4.0}),
        );
    }
    if get(45) != 0 {
        result.push(json!({"key":"revive","label":"蘇生","count":get(45),"duration":get(46),"percent":get(47)}));
    }
    if get(64) > 0 {
        result.push(json!({"key":"enemy-barrier","label":"バリア","hp":get(64)}));
    }
    if get(81) > 0 {
        result.push(json!({"key":if get(102)!=0{"mini-surge"}else{"surge"},"label":if get(102)!=0{"小烈波"}else{"烈波"},"probability":get(81),"level":get(84),"range":[get(82) as f64/4.0,(get(82)+get(83)) as f64/4.0]}));
    }
    if get(87) > 0 {
        result
            .push(json!({"key":"aku-shield","label":"悪魔シールド","hp":get(87),"regen":get(88)}));
    }
    if get(89) > 0 {
        result.push(json!({"key":"death-surge","label":"死亡時烈波","probability":get(89),"level":get(92),"range":[get(90) as f64/4.0,(get(90)+get(91)) as f64/4.0]}));
    }
    for ability in &mut result {
        match ability["key"].as_str().unwrap_or_default() {
            "castle" => ability["power"] = json!(400),
            "weaken" => ability["percent"] = json!(get(31)),
            "savage" => ability["power"] = json!(100 + get(76)),
            "toxic" => ability["percent"] = json!(get(80)),
            "warp" => ability["range"] = json!([get(67) as f64 / 4.0, get(68) as f64 / 4.0]),
            "blast" => {
                ability["range"] =
                    json!([get(107) as f64 / 4.0, (get(107) + get(108)) as f64 / 4.0])
            }
            "delay" => ability["percent"] = json!(get(112)),
            _ => {}
        }
    }
    let widths = [
        Some(get(36)),
        (get(95) != 0).then(|| get(97)),
        (get(98) != 0).then(|| get(100)),
    ];
    if widths.into_iter().flatten().any(|value| value < 0) {
        result.push(json!({"key":"omni","label":"全方位攻撃"}));
    } else if widths.into_iter().flatten().all(|value| value > 0) {
        result.push(json!({"key":"long-range","label":"遠方攻撃"}));
    }
    if get(55) != 0 {
        result.push(json!({"key":"multi-hit","label":"連続攻撃"}));
    }
    result
}

pub fn catalog(database: &Database, region: &str) -> Result<Value> {
    let definitions = definitions();
    let metadata = database.metadata()?;
    let mut enemies = Vec::new();
    let mut options: Vec<Value> = Vec::new();
    for enemy in read(&database.connection, region)? {
        let get = |column| enemy.raw.get(column).copied().flatten().unwrap_or(0);
        let mut attributes: Vec<_> = definitions
            .attributes
            .iter()
            .filter(|(column, _, _)| get(*column) > 0)
            .map(|(_, key, _)| key.clone())
            .collect();
        if definitions.castles.contains(&enemy.id)
            && !attributes.iter().any(|value| value == "base")
        {
            attributes.push("base".into());
        }
        let abilities = abilities(&enemy.raw);
        for ability in &abilities {
            if !options.iter().any(|value| value["key"] == ability["key"]) {
                options.push(json!({"key":ability["key"],"label":ability["label"]}));
            }
        }
        let foreswings: Vec<_> = enemy.attacks.iter().map(|hit| hit.foreswing).collect();
        let pre = foreswings.iter().flatten().copied().max();
        let ranges: Vec<_> = if get(35) != 0 || get(36) != 0 {
            enemy
                .attacks
                .iter()
                .filter_map(|hit| hit.range)
                .map(|[start, end]| [start.min(end), start.max(end)])
                .collect()
        } else {
            Vec::new()
        };
        enemies.push(json!({"id":enemy.id,"name":enemy.name,"description":enemy.description,"hp":enemy.hp,"knockbacks":enemy.knockbacks,"speed":enemy.speed,"range":enemy.range,"drop":enemy.drop,"attackType":if enemy.area{"範囲"}else{"単体"},"attacks":enemy.attacks.iter().map(|hit|hit.damage).collect::<Vec<_>>(),"foreswings":foreswings,"abilityHits":enemy.attacks.iter().map(|hit|hit.ability_enabled).collect::<Vec<_>>(),"attackCycle":enemy.attack_cycle,"backswing":enemy.animation_length.zip(pre).map(|(length,pre)|length-pre),"attackInterval":enemy.interval_raw*2,"icon":enemy.icon_path,"ranges":ranges,"attributes":attributes,"species":definitions.species.iter().filter(|(column,_,_)|get(*column)>0).map(|(_,key,_)|key).collect::<Vec<_>>(),"abilities":abilities,"castleRange":if get(36)!=0{get(35)}else{enemy.range},"width":get(8),"attackLimit":get(50),"star":get(69),"invulnerable":get(49)!=0,"selfDestruct":get(52)==2,"soul":get(54),"deathMotion":get(63)!=0,"motion":null}));
    }
    let choices = |fields: &[Field]| {
        fields
            .iter()
            .map(|(_, key, label)| json!({"key":key,"label":label}))
            .collect::<Vec<_>>()
    };
    Ok(
        json!({"schemaVersion":1,"gameVersion":metadata.get("version"),"revision":metadata.get("revision"),"datasetId":metadata.get("dataset_id"),"buildId":metadata.get("build_id"),"imageBase":"/api/asset/","propertyAtlas":crate::view::property_atlas(database,&definitions.icons)?,"attributes":choices(&definitions.attributes),"species":choices(&definitions.species),"abilities":options,"enemies":enemies}),
    )
}
