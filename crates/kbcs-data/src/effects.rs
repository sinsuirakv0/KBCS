use crate::{
    import::read_asset,
    motions::descriptor,
    source::{Dataset, Source},
    store::Database,
};
use anyhow::{Context, Result, ensure};
use rusqlite::Connection;
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

// キャラ本体以外のモデルを、同じ版の素材索引から選ぶ。
fn is_character(stem: &str) -> bool {
    stem.split_once('_').is_some_and(|(id, suffix)| {
        !id.is_empty()
            && id.bytes().all(|b| b.is_ascii_digit())
            && ["f", "c", "s", "u", "e", "m"].contains(&suffix)
    })
}

pub(crate) fn import(
    source: &Source,
    dataset: &Dataset,
    connection: &Connection,
    progress: &(impl Fn(String) + Sync),
) -> Result<()> {
    // 定義は全て保存。対応が未確認の画像へ勝手に結合しない。
    let stored: BTreeSet<String> = connection
        .prepare("SELECT path FROM source_file")?
        .query_map([], |r| r.get(0))?
        .collect::<rusqlite::Result<_>>()?;
    let pending: Vec<_> = dataset
        .files
        .keys()
        .filter(|p| {
            !stored.contains(*p)
                && (p.ends_with(".mamodel") || p.ends_with(".maanim") || p.ends_with(".imgcut"))
        })
        .cloned()
        .collect();
    source.prefetch(dataset, &pending, progress)?;
    for path in &pending {
        read_asset(source, dataset, connection, path)?;
    }
    let entries = entries(connection, &dataset.files.keys().cloned().collect(), None)?;
    let images: BTreeSet<_> = entries
        .iter()
        .filter_map(|e| e["image"].as_str().map(str::to_owned))
        .collect();
    source.prefetch(
        dataset,
        &images.iter().cloned().collect::<Vec<_>>(),
        progress,
    )?;
    for path in &images {
        if dataset.release.is_some() {
            continue;
        }
        read_asset(source, dataset, connection, path)?;
    }
    if dataset.files.contains_key("Data/param.tsv") {
        read_asset(source, dataset, connection, "Data/param.tsv")?;
    }
    progress(format!(
        "その他モーション: {}モデル / {}画像",
        entries.len(),
        images.len()
    ));
    Ok(())
}

fn side(stem: &str) -> &'static str {
    // 敵専用でも_eを持たない共通素材を、味方と誤表示しない。
    if !stem.starts_with("skill_") || stem == "skill_demonshield" {
        "other"
    } else if stem.ends_with("_e") {
        "enemy"
    } else {
        "unit"
    }
}

fn label(stem: &str) -> String {
    let key = stem
        .strip_prefix("skill_")
        .unwrap_or(stem)
        .strip_suffix("_e")
        .unwrap_or(stem.strip_prefix("skill_").unwrap_or(stem));
    let name = match key {
        "up" | "strong_attack" => "攻撃力アップ",
        "down" => "攻撃力ダウン",
        "slow" => "動きを遅くする",
        "stop" => "動きを止める",
        "shield" => "生き残り",
        "barrier" => "バリア",
        "guard" => "城バリア",
        "demonshield" => "悪魔シールド",
        "demonsummon" => "悪魔召喚",
        "wave_attack" => "波動",
        "smallwave_attack" => "小波動",
        "wave_invalid" => "波動無効",
        "wave_stop" => "波動ストッパー",
        "volcano" => "烈波",
        "smallvolcano" => "小烈波",
        "explosion" => "爆波",
        "warp" => "ワープ",
        "warp_chara" => "ワープ中のキャラ",
        "curse" => "古代の呪い",
        "attack_invalid" => "攻撃無効",
        "effect_invalid" => "妨害無効",
        "metal_strong" => "メタルキラー",
        "zombie_strong" => "ゾンビキラー",
        "percentage_attack" => "毒撃",
        "recast_decrease" => "再生産遅延",
        "critical" => "クリティカル",
        "boss_welcome" => "ボス出現の衝撃波",
        "rain" => "雨",
        _ => key,
    };
    if side(stem) != "other" {
        format!(
            "{name}（{}）",
            if stem.ends_with("_e") {
                "敵"
            } else {
                "味方"
            }
        )
    } else {
        name.to_owned()
    }
}

fn entries(
    connection: &Connection,
    paths: &BTreeSet<String>,
    selected: Option<&str>,
) -> Result<Vec<Value>> {
    let models: Vec<_> = paths
        .iter()
        .filter(|p| {
            p.ends_with(".mamodel")
                && !is_character(p.rsplit('/').next().unwrap().trim_end_matches(".mamodel"))
        })
        .collect();
    let mut owners: Vec<_> = models
        .iter()
        .flat_map(|p| {
            let stem = p.trim_end_matches(".mamodel");
            [Some(stem), stem.strip_suffix("_e")].into_iter().flatten()
        })
        .collect();
    owners.sort_by_key(|s| std::cmp::Reverse(s.len()));
    owners.dedup();
    let mut animations: BTreeMap<&str, Vec<&String>> = BTreeMap::new();
    for path in paths.iter().filter(|p| p.ends_with(".maanim")) {
        let name = path.trim_end_matches(".maanim");
        if let Some(owner) = owners.iter().find(|stem| {
            name.strip_prefix(**stem).is_some_and(|tail| {
                tail.is_empty() || tail.starts_with('_') || tail.bytes().all(|b| b.is_ascii_digit())
            })
        }) {
            animations.entry(owner).or_default().push(path);
        }
    }
    let cuts: Vec<_> = paths.iter().filter(|p| p.ends_with(".imgcut")).collect();
    let mut result = Vec::new();
    for model in models {
        let full = model.trim_end_matches(".mamodel");
        let (directory, stem) = full.rsplit_once('/').context("モデルのパス不正")?;
        // 所有関係は全モデルで解決し、内容の解析は要求された素材だけに絞る。
        if selected.is_some_and(|id| id != stem) {
            continue;
        }
        let bytes: Vec<u8> =
            connection.query_row("SELECT bytes FROM source_file WHERE path=?", [model], |r| {
                r.get(0)
            })?;
        let text = std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}');
        let lines: Vec<_> = text
            .lines()
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .collect();
        let parts: usize = lines.get(2).context("モデルのパーツ数なし")?.parse()?;
        let mut issue = String::new();
        let cut = if ["critical", "boss_welcome", "rain"].contains(&stem) {
            Some("ImageData/000_a.imgcut".to_owned())
        } else if stem.starts_with("skill_") {
            let ids: BTreeSet<i64> = lines
                .iter()
                .skip(3)
                .take(parts)
                .filter_map(|l| l.split(',').nth(1)?.trim().parse().ok())
                .filter(|id| *id >= 0)
                .collect();
            if ids.len() == 1 {
                Some(format!("ImageData/skill{:03}.imgcut", ids.first().unwrap()))
            } else {
                issue = "画像グループの対応を確認中".into();
                None
            }
        } else {
            cuts.iter()
                .filter(|p| {
                    let base = p.rsplit('/').next().unwrap().trim_end_matches(".imgcut");
                    stem == base
                        || stem
                            .strip_prefix(base)
                            .is_some_and(|tail| tail.starts_with('_'))
                })
                .max_by_key(|p| p.len())
                .map(|p| (*p).clone())
                .or_else(|| {
                    if stem.starts_with("nyankoCastle_001_") {
                        stem.rsplit_once('_')
                            .map(|(base, _)| format!("ImageData/{base}_00.imgcut"))
                    } else {
                        None
                    }
                })
        };
        let cut = cut.filter(|p| paths.contains(p));
        let image = if let Some(cut) = &cut {
            let base = cut
                .rsplit('/')
                .next()
                .context("分割定義のパス不正")?
                .trim_end_matches(".imgcut");
            let bytes: Vec<u8> =
                connection.query_row("SELECT bytes FROM source_file WHERE path=?", [cut], |r| {
                    r.get(0)
                })?;
            let header = std::str::from_utf8(&bytes)?
                .trim_start_matches('\u{feff}')
                .lines()
                .map(str::trim)
                .filter(|s| !s.is_empty())
                .nth(2)
                .unwrap_or("");
            // 同名画像を優先し、なければ索引に実在するヘッダー名だけを採用する。
            [
                format!("{directory}/{base}.png"),
                format!("Image/{base}.png"),
                format!("Number/{base}.png"),
                format!("{directory}/{header}"),
                format!("Image/{header}"),
                format!("Number/{header}"),
            ]
            .into_iter()
            .find(|p| paths.contains(p))
        } else {
            None
        };
        if cut.is_none() && issue.is_empty() {
            issue = "対応する分割定義を確認中".into();
        }
        if image.is_none() && issue.is_empty() {
            issue = "対応する画像を確認中".into();
        }
        let clips = animations.get(full).or_else(|| {
            if stem.starts_with("skill_") {
                full.strip_suffix("_e").and_then(|s| animations.get(s))
            } else {
                None
            }
        });
        let clips: Vec<_> = clips
            .into_iter()
            .flatten()
            .enumerate()
            .map(|(i, p)| {
                let name = p.trim_end_matches(".maanim");
                let suffix = name
                    .strip_prefix(full)
                    .or_else(|| {
                        full.strip_suffix("_e")
                            .and_then(|base| name.strip_prefix(base))
                    })
                    .unwrap_or(name);
                let label = match suffix {
                    "" => "通常",
                    "_breaker" => "ブレイカー",
                    "_destruction" => "破壊",
                    "00" if stem.contains("volcano") => "開始",
                    "01" if stem.contains("volcano") => "継続",
                    "02" if stem.contains("volcano") => "終了",
                    _ => suffix,
                };
                json!({"key":format!("effect-{i}"),"path":p,"name":label})
            })
            .collect();
        result.push(json!({"id":stem,"name":label(stem),"side":side(stem),"category":if stem.starts_with("skill_")||stem.starts_with("battle_")||["critical","boss_welcome"].contains(&stem){"effects"}else{"other"},"model":model,"cut":cut,"image":image,"animations":clips,"parts":parts,"issue":issue}));
    }
    Ok(result)
}

fn stored_entries(database: &Database, selected: Option<&str>) -> Result<Vec<Value>> {
    let mut statement = database
        .connection
        .prepare("SELECT path FROM asset_reference ORDER BY path")?;
    let paths = statement
        .query_map([], |r| r.get::<_, String>(0))?
        .collect::<rusqlite::Result<BTreeSet<_>>>()?;
    entries(&database.connection, &paths, selected)
}

pub fn catalog(database: &Database) -> Result<Value> {
    Ok(json!({"metadata":database.metadata()?,"entries":stored_entries(database, None)?}))
}

pub fn manifest(database: &Database, id: &str) -> Result<Value> {
    let entry = stored_entries(database, Some(id))?
        .into_iter()
        .find(|e| e["id"].as_str() == Some(id))
        .context("その他モーションがありません。DBを更新してください")?;
    ensure!(
        entry["issue"] == "",
        "{}",
        entry["issue"].as_str().unwrap_or("未対応の素材")
    );
    let mut files = BTreeMap::new();
    for (field, role) in [
        ("model", "モデル"),
        ("cut", "分割定義"),
        ("image", "スプライト画像"),
    ] {
        let path = entry[field].as_str().context("素材パスなし")?;
        files.insert(path.to_owned(), descriptor(database, path, role)?);
    }
    for clip in entry["animations"]
        .as_array()
        .context("モーション一覧なし")?
    {
        let path = clip["path"].as_str().context("モーションパスなし")?;
        files.insert(path.to_owned(), descriptor(database, path, "モーション")?);
    }
    let mut config = json!({"waveInterval":4});
    if let Ok((_, _, _, bytes)) = database.source("Data/param.tsv") {
        files.insert(
            "Data/param.tsv".into(),
            descriptor(database, "Data/param.tsv", "演出設定")?,
        );
        let text = std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}');
        let parameters: BTreeMap<_, _> = text.lines().filter_map(|l| l.split_once('\t')).collect();
        for (target, key) in [
            ("smallWaveInterval", "battle_wave_s_inter"),
            ("explosionStart", "battle_explosion_frame1"),
            ("explosionActive", "battle_explosion_frame2"),
            ("explosionEnd", "battle_explosion_frame3"),
            ("explosionInterval", "battle_explosion_frame4"),
        ] {
            if let Some(value) = parameters.get(key) {
                config[target] = json!(value.trim().parse::<i64>()?);
            }
        }
    }
    Ok(
        json!({"schemaVersion":1,"metadata":database.metadata()?,"character":{"kind":"effect","id":id,"name":entry["name"],"stem":id,"deathMotion":false},"body":{"key":"body","stem":id,"image":entry["image"],"cut":entry["cut"],"model":entry["model"],"animations":entry["animations"]},"soul":null,"sequenceConfig":config,"files":files.into_values().collect::<Vec<_>>()}),
    )
}
