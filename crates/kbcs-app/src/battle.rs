use anyhow::{Context, Result, ensure};
use kbcs_bridge::{actor, battle, battle_screen, production, render, stage};
use kbcs_data::{formations::Document, store::Database};
use serde::Deserialize;
use serde_json::{Value, json};
use std::collections::{BTreeMap, BTreeSet};

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Start {
    pub snapshot: Value,
    pub config: battle_screen::Config,
    pub state: battle_screen::State,
    pub scene: crate::scene::Input,
}
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Request {
    pub session: String,
    pub input: battle_screen::Input,
    pub scene: crate::scene::Input,
    #[serde(default)]
    pub packed: bool,
    #[serde(default)]
    pub debug: bool,
    #[serde(default)]
    pub compressed: bool,
}
pub struct Clip {
    pub model: render::Model,
    pub texture: i32,
}
pub struct MotionSet {
    pub death_frames: i32,
    pub clips: BTreeMap<i32, Clip>,
    pub name: String,
}
pub struct Session {
    pub database: Database,
    pub scene: crate::scene::Scene,
    pub core: battle::Battle,
    pub models: Vec<MotionSet>,
    pub effects: BTreeMap<(i32, i32, i32), Clip>,
    pub key: String,
    pub title: Value,
    receipt: crate::battle_rewards::Receipt,
    cannon_clips: BTreeMap<i32, Clip>,
    cannon_cuts: Vec<render::Cut>,
    cannon_texture: i32,
    castle_slot: i32,
    sniper_cuts: [Vec<render::Cut>; 2],
    sniper_textures: [i32; 2],
    top_cuts: [Vec<render::Cut>; 2],
    top_textures: [i32; 2],
    title_draw: Option<(render::Cut, i32)>,
    rules: battle::Rules,
}
fn integer(value: &Value) -> Result<i32> {
    value
        .as_i64()
        .and_then(|n| i32::try_from(n).ok())
        .context("戦闘の整数入力がありません")
}
fn native<T>(value: std::result::Result<T, u32>) -> Result<T> {
    value.map_err(|code| anyhow::anyhow!("戦闘コア: {code}"))
}
fn text(db: &Database, path: &str) -> Result<String> {
    Ok(String::from_utf8(db.source(path)?.3)?
        .trim_start_matches('\u{feff}')
        .into())
}
fn catalog() -> Result<Value> {
    Ok(serde_json::from_str(
        include_str!("../../../ui/settings-catalog.js")
            .trim_start_matches('\u{feff}')
            .trim()
            .strip_prefix("export default ")
            .context("設定定義が不正です")?
            .trim_end_matches(';'),
    )?)
}
fn inputs() -> Result<Value> {
    Ok(serde_json::from_str(
        include_str!("../../kbcs-data/resources/battle-inputs.json").trim_start_matches('\u{feff}'),
    )?)
}
// 原本のatoi同様、整数接頭辞の後の注記を値へ含めない。
fn cells(raw: &[String]) -> Result<Vec<i32>> {
    raw.iter()
        .map(|s| {
            let s = s.trim();
            let count = s
                .bytes()
                .enumerate()
                .take_while(|(i, c)| c.is_ascii_digit() || *i == 0 && (*c == b'-' || *c == b'+'))
                .count();
            if count == 0 {
                Ok(0)
            } else {
                Ok(s[..count].parse()?)
            }
        })
        .collect()
}
fn load_model(
    db: &Database,
    cut: &str,
    model: &str,
    animation: Option<&str>,
) -> Result<render::Model> {
    let a = animation.map(|path| text(db, path)).transpose()?;
    render::Model::parse(&text(db, cut)?, &text(db, model)?, a.as_deref())
        .map_err(anyhow::Error::msg)
}
fn motion(
    db: &Database,
    scene: &mut crate::scene::Scene,
    region: &str,
    side: i32,
    id: u32,
    form: usize,
    revive: i32,
) -> Result<(actor::Motion, i32, i32, MotionSet)> {
    let manifest = kbcs_data::motions::manifest(
        db,
        region,
        if side == 0 { "unit" } else { "enemy" },
        id,
        form,
    )?;
    let mut motion = actor::Motion::default();
    let mut clips = BTreeMap::new();
    let mut body_frames = 0;
    let mut death_frames = 0;
    let resource = &manifest["body"];
    let cut = resource["cut"].as_str().context("分割原本なし")?;
    let model = resource["model"].as_str().context("モデル原本なし")?;
    let base = load_model(db, cut, model, None)?;
    let boundary = native(base.contact(if side == 0 { 1 } else { 0 }))?[0];
    for (resource, soul) in [(&manifest["body"], false), (&manifest["soul"], true)] {
        if resource.is_null() {
            continue;
        }
        let image = resource["image"].as_str().context("画像原本なし")?;
        let texture = scene.texture(image);
        let cut = resource["cut"].as_str().context("分割原本なし")?;
        let model = resource["model"].as_str().context("モデル原本なし")?;
        for animation in resource["animations"]
            .as_array()
            .context("モーション一覧なし")?
        {
            let key = animation["key"].as_str().context("モーション番号なし")?;
            let index = if soul {
                9
            } else {
                match key {
                    "_soul" => 8,
                    "_entry" => 7,
                    "_zombie00" => 4,
                    "_zombie01" => 5,
                    "_zombie02" => 6,
                    _ => {
                        let Ok(index) = key.parse::<i32>() else {
                            continue;
                        };
                        index
                    }
                }
            };
            let m = load_model(db, cut, model, animation["path"].as_str())?;
            let lengths = native(m.clock_lengths())?;
            if index == 9 {
                death_frames = lengths[0];
            } else if index == 8 {
                body_frames = lengths[0];
            } else if (0..8).contains(&index) {
                motion.encoded[index as usize] = lengths[0];
                motion.plain[index as usize] = lengths[1];
            }
            clips.insert(index, Clip { model: m, texture });
        }
    }
    if revive >= 0 {
        // 009f560c: 復帰はbattle_entry、通常死亡はbattle_soul。共通の時計にしない。
        let stem = format!("battle_entry_{revive:03}");
        let model = load_model(
            db,
            &format!("ImageData/{stem}.imgcut"),
            &format!("ImageData/{stem}.mamodel"),
            Some(&format!("ImageData/{stem}.maanim")),
        )?;
        motion.soul_frames = native(model.clock_lengths())?[0];
        let texture = scene.texture(&format!("Number/{stem}.png"));
        clips.insert(10, Clip { model, texture });
    }
    Ok((
        motion,
        boundary,
        body_frames,
        MotionSet {
            death_frames,
            clips,
            name: manifest["character"]["name"].as_str().unwrap_or("").into(),
        },
    ))
}
impl Session {
    pub fn new(
        root: &std::path::Path,
        region: &str,
        start: Start,
        persist_rewards: bool,
    ) -> Result<Self> {
        let database = Database::open(root, region)?;
        let metadata = database.metadata()?;
        let snapshot = &start.snapshot;
        let settings = catalog()?;
        let constants = inputs()?;
        for (path, source) in constants["sources"]
            .as_object()
            .context("戦闘入力の出典なし")?
        {
            if let Ok((_, _, sha, _)) = database.source(path) {
                ensure!(
                    source["sha256"] == sha,
                    "戦闘入力の原本SHAが一致しません: {path}"
                );
            }
        }
        for source in constants["clocks"]
            .as_object()
            .context("効果時計なし")?
            .values()
        {
            if let Some(path) = source["path"].as_str()
                && let Ok((_, _, sha, _)) = database.source(path)
            {
                ensure!(
                    source["source"]["sha256"] == sha,
                    "効果時計の原本SHAが一致しません: {path}"
                );
            }
        }
        ensure!(
            metadata.get("version").map(String::as_str) == Some("15.7.2")
                && snapshot["buildId"].as_str() == metadata.get("build_id").map(String::as_str),
            "戦闘入力とDBの版が一致しません"
        );
        let document: Document = serde_json::from_value(snapshot["formation"].clone())?;
        document.validate(region)?;
        let map_key = snapshot["map"]["key"].as_str().context("マップIDなし")?;
        let data = if let Some(path) = snapshot["stage"]["patternSource"].as_str() {
            kbcs_data::stages::variant(
                &database,
                region,
                map_key,
                i64::from(integer(&snapshot["stage"]["index"])?),
                path,
            )?
        } else {
            kbcs_data::stages::catalog_map(&database, region, Some(map_key))?
        };
        let map = &data["maps"][0];
        let stage = data["stages"]
            .as_array()
            .context("ステージなし")?
            .iter()
            .find(|s| s["index"] == snapshot["stage"]["index"])
            .context("面が見つかりません")?;
        ensure!(
            stage["source"] == snapshot["stage"]["source"],
            "ステージ原本が一致しません"
        );
        let width = integer(&stage["width"])?
            .checked_mul(4)
            .context("幅の範囲外")?;
        let kind = integer(&map["nativeMode"])?;
        let crown = integer(&snapshot["crown"])?;
        let mut environment = actor::Environment {
            unit_modes: [1, 0],
            stage_width: width,
            castle_slot: -1,
            stage_kind: kind,
            zombie: i32::from(map["series"].as_str().is_some_and(|s| s.ends_with('Z'))),
            chapter_rate: if kind < 3 {
                [0, 5, 30][integer(&map["number"])? as usize]
            } else {
                0
            },
            crown: integer(&map["stars"][crown as usize - 1])?,
            hp_percent: 100,
            attack_percent: 100,
            orb_stage: match integer(&map["nativeKind"])? {
                0 => 9,
                -9 => 16,
                _ => 0,
            },
            ..Default::default()
        };
        let mut hit = actor::HitContext::default();
        for item in settings["treasures"].as_array().context("お宝定義なし")? {
            let id = item["id"].as_str().context("お宝IDなし")?;
            let effect = integer(&item["effectType"])? as usize;
            ensure!(effect < 32, "お宝種別範囲外");
            if integer(&item["effectFlag"])? != 0
                && integer(&item["chapter"])? - 1 + [0, 4, 7][integer(&item["campaign"])? as usize]
                    != kind
            {
                continue;
            }
            let quality = integer(&document.profile["treasures"][id])?;
            let maximum = integer(&item["maximumEffect"])?;
            environment.treasures[effect] += if maximum == 0 {
                quality
            } else {
                quality * maximum / 100
            };
            hit.fruit_rates[effect] += quality;
        }
        environment.crystal = [
            environment.treasures[16],
            environment.treasures[18],
            environment.treasures[22],
            environment.treasures[22],
            environment.treasures[22],
        ];
        environment.crystal_max = [
            600,
            1500,
            if (7..=9).contains(&kind) { 1000 } else { 0 },
            if (7..=9).contains(&kind) { 1000 } else { 0 },
            if (7..=9).contains(&kind) { 1000 } else { 0 },
        ];
        let combo_groups = kbcs_data::combos::target_groups(&database.connection)?;
        let mut unit_combos: BTreeMap<i32, [i32; 32]> = BTreeMap::new();
        let mut cost_combos = Vec::new();
        let effects = kbcs_data::combos::effects(&database.connection, region)?;
        for combo in kbcs_data::combos::read(&database.connection, region)? {
            if combo.members.iter().all(|m| {
                document.slots[..5]
                    .iter()
                    .flatten()
                    .any(|p| p.unit_id as i64 == m.id && p.form as i64 >= m.form)
            }) {
                let effect = effects
                    .iter()
                    .find(|e| e.index == combo.kind)
                    .context("コンボ効果なし")?;
                ensure!((0..32).contains(&combo.kind), "コンボ範囲外");
                let value = i32::try_from(
                    *effect
                        .values
                        .get(combo.grade as usize)
                        .context("コンボ等級なし")?,
                )?;
                if combo.kind == 27 {
                    cost_combos.push((combo.group, value));
                }
                if combo.group == -1 {
                    environment.combos[combo.kind as usize] += value;
                } else if let Some(units) = combo_groups.get(&combo.group) {
                    for &unit in units {
                        unit_combos.entry(unit).or_insert([0; 32])[combo.kind as usize] += value;
                    }
                }
            }
        }
        let parameter = |name: &str| integer(&constants["parameters"][name]);
        environment.parameters = [
            parameter("battle_af_death_volcano_distance")?,
            parameter("battle_af_death_volcano_width")?,
        ];
        hit.parameters = [
            parameter("battle_wave_s_st")?,
            parameter("battle_super_beast_hunter")?,
            parameter("battle_super_sage_hunter_damage1")?,
            parameter("battle_super_beast_hunter_df")?,
            parameter("battle_super_sage_hunter_damage2")?,
        ];
        for (i, key) in [
            "weaken",
            "freeze",
            "slow",
            "curse",
            "knockback",
            "weaken",
            "freeze",
            "slow",
            "curse",
            "knockback",
            "warp",
        ]
        .iter()
        .enumerate()
        {
            hit.effects.sage[i] = parameter(&format!(
                "battle_super_sage_{}{key}",
                if i >= 5 { "hunter_" } else { "" }
            ))?;
        }
        // 土台・装飾は選択Lvの率へ解決済み。内部getterの代用キーは1へ統一する。
        hit.effects.scenario_level = 1;
        const TARGETS: [&str; 12] = [
            "red", "floating", "black", "metal", "alien", "angel", "zombie", "relic", "white",
            "witch", "eva", "aku",
        ];
        for part in ["base", "decoration"] {
            let selected = &document.profile["cannon"][part];
            let id = integer(&selected["id"])?;
            let level = integer(&selected["level"])? as usize;
            if id == 0 {
                continue;
            }
            let definition = settings["cannonParts"][part]
                .as_array()
                .context("城パーツ定義なし")?
                .iter()
                .find(|v| v["id"] == id)
                .context("城パーツなし")?;
            let rate = integer(&definition["rates"][level])?;
            let name = definition["effect"].as_str().context("パーツ種別なし")?;
            if part == "base" {
                hit.base_reductions[TARGETS
                    .iter()
                    .position(|v| *v == name)
                    .context("土台属性なし")?] = rate;
            } else {
                match name {
                    "slow" => hit.effects.base_reductions[0] = rate,
                    "stop" => hit.effects.base_reductions[1] = rate,
                    "weaken" => hit.effects.base_reductions[2] = rate,
                    "curse" => hit.effects.base_reductions[3] = rate,
                    "wave" => hit.decoration_reductions[0] = rate,
                    "surge" => hit.decoration_reductions[1] = rate,
                    "toxic" => hit.decoration_reductions[2] = rate,
                    _ => anyhow::bail!("装飾種別なし"),
                }
            }
        }
        let facility = |id: &str| -> Result<i32> {
            let v = &document.profile["facilities"][id];
            Ok(integer(&v["level"])? + integer(&v["plus"])? - 1)
        };
        let clock_length =
            |address: &str, index: usize| integer(&constants["clocks"][address]["lengths"][index]);
        let mut clock = actor::Clock {
            encoded: [0; 4],
            plain: [0; 4],
            forms: [[0; 51]; 2],
            kill_orb: [0; 51],
            kill_threshold: parameter("battle_powerup_kill_enemy")?,
        };
        for (i, address) in ["0x1de8", "0x1988", "0x1a68", "0x2168"].iter().enumerate() {
            clock.encoded[i] = clock_length(address, 0)?;
            clock.plain[i] = clock_length(address, 1)?;
        }
        let mut scene = crate::scene::Scene::new(&database, &start.scene)?;
        let mut sniper_cuts = [Vec::new(), Vec::new()];
        let mut sniper_textures = [-1; 2];
        {
            for (i, image, cut) in [
                (0, "Image/img043.png", "ImageData/img043.imgcut"),
                (1, "Number/000_a.png", "ImageData/000_a.imgcut"),
            ] {
                if i == 0 && start.config.items & (1 << 5) == 0 {
                    continue;
                }
                sniper_textures[i] = scene.texture(image);
                sniper_cuts[i] = kbcs_data::stage_media::cuts(&database, cut)?
                    .into_iter()
                    .map(|[x, y, width, height]| render::Cut {
                        x,
                        y,
                        width,
                        height,
                    })
                    .collect();
            }
        }

        let mut profiles = Vec::new();
        let mut models = Vec::new();
        scene.owned_castle();
        environment.castle_x = 3200;
        environment.castle_scale = scene.castle_geometry()[2];
        environment.castle_offset = scene.castle_geometry()[0];
        let rule = |id: i32| {
            map["rules"]
                .as_array()
                .and_then(|rules| rules.iter().find(|r| r["id"] == id))
                .map(|r| &r["parameters"])
        };
        let native_kind = integer(&map["nativeKind"])?;
        let mut rules = battle::Rules {
            native_kind,
            score_type: if matches!(native_kind, 3 | 4) {
                1
            } else if stage["scoreRewards"]
                .as_array()
                .is_some_and(|v| !v.is_empty())
                && kbcs_bridge::score::stage_available(
                    integer(&map["nativeMode"])?,
                    map["scoreId"].as_i64().unwrap_or(-1) as i32,
                    1,
                )
            {
                2
            } else {
                0
            },
            time_limit: stage["timeLimit"]
                .as_i64()
                .map(i32::try_from)
                .transpose()?
                .unwrap_or(0),
            total_limit: rule(7).map(|v| integer(&v[0])).transpose()?.unwrap_or(-1),
            production_kind: parameter("battle_af_condition_production_type")?,
            recharge_fixed: i32::from(rule(1).is_some()),
            cost_chapter: if kind < 3 {
                integer(&map["number"])?
            } else {
                1
            },
            ..Default::default()
        };
        ensure!(
            unit_combos.len() <= rules.unit_combos.len(),
            "対象限定コンボのキャラ数が多すぎます"
        );
        rules.unit_combo_count = unit_combos.len() as i32;
        for (out, (&unit_id, &values)) in rules.unit_combos.iter_mut().zip(&unit_combos) {
            *out = battle::UnitCombo { unit_id, values };
        }
        for (i, out) in rules.production_periods.iter_mut().enumerate() {
            *out = parameter(&format!("battle_af_condition_production_{i}"))?;
        }
        if let Some(parameters) = rule(8) {
            let values = parameters.as_array().context("追加生産ルールの列なし")?;
            ensure!(values.len() == 3, "追加生産ルールの列数不正");
            for (out, value) in rules.extra_rule.iter_mut().zip(values) {
                *out = integer(value)?;
            }
        }
        if let Some(point) = stage["pointRules"]["raw"].as_object() {
            let bytes = kbcs_data::source::asset(&database, root, "Data/PointStageSettings.json")?;
            let point_maps: Value =
                serde_json::from_str(std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}'))?;
            let map_id = integer(&map["nativeId"])?;
            ensure!(
                point_maps["PointID"]
                    .as_object()
                    .is_some_and(|points| points.values().any(|v| v["MapID"]
                        .as_array()
                        .is_some_and(|maps| maps.iter().any(|m| *m == map_id)))),
                "イベントPtのマップ対応なし"
            );
            rules.score_type = 3;
            rules.point.kind = integer(&point["RuleType"])?;
            let values = point["Parameters"]
                .as_array()
                .context("イベントPtの列なし")?;
            ensure!(
                values.len() >= 3 && values.len() % 2 == 1,
                "イベントPtの列数不正"
            );
            rules.point.rate = integer(&values[0])?;
            let mut tiers = BTreeMap::new();
            for pair in values[1..].as_chunks::<2>().0 {
                tiers.insert(integer(&pair[1])?, integer(&pair[0])?);
            }
            ensure!(
                tiers.len() <= rules.point.tiers.len(),
                "イベントPtの区間が多すぎます"
            );
            rules.point.tier_count = tiers.len() as i32;
            for (out, (threshold, rate)) in rules.point.tiers.iter_mut().zip(tiers) {
                *out = [threshold, rate];
            }
            if let Some(parameters) = rule(12) {
                let values = parameters.as_array().context("フィーバーの列なし")?;
                ensure!((3..=10).contains(&values.len()), "フィーバーの列数不正");
                rules.point.fever_count = values.len() as i32;
                for (out, value) in rules.point.fever.iter_mut().zip(values) {
                    *out = integer(value)?;
                }
            }
        }
        if let Some(parameters) = rule(3) {
            let values = parameters.as_array().context("同時出撃制限の列なし")?;
            ensure!(values.len() == 6, "同時出撃制限の列数不正");
            for (out, value) in rules.rarity_limits.iter_mut().zip(values) {
                *out = integer(value)?;
            }
        }
        if let Some(types) = map["scoreBonus"]["raw"]["BonusType"].as_object() {
            hit.effects.notifications = 1;
            for (key, value) in types {
                let index: usize = key.parse()?;
                ensure!(index < rules.bonus.len(), "スコアボーナス種別範囲外");
                rules.bonus[index] = integer(&value["Parameters"][0])?;
            }
        }
        let cannon_id = i32::from(document.cannon.id);
        scene.player_parts(
            &database,
            document.cannon.id,
            integer(&document.profile["cannon"]["base"]["id"])?,
            integer(&document.profile["cannon"]["decoration"]["id"])?,
        )?;
        let cannon_rows = constants["cannon"]["status"]
            .as_array()
            .context("城砲の定義なし")?;
        let status = cannon_rows
            .iter()
            .find(|row| row[0] == cannon_id)
            .context("選択した城砲の定義なし")?;
        let status: [i32; 6] = status
            .as_array()
            .context("城砲の列なし")?
            .iter()
            .skip(1)
            .take(6)
            .map(integer)
            .collect::<Result<Vec<_>>>()?
            .try_into()
            .map_err(|_| anyhow::anyhow!("城砲の列数不足"))?;
        let cannon_growth = constants["cannon"]["growth"]
            .as_array()
            .context("城砲の成長表なし")?
            .iter()
            .filter(|row| row[0] == cannon_id)
            .map(|row| {
                Ok(kbcs_bridge::cannon::Growth {
                    kind: integer(&row[1])?,
                    end: integer(&row[2])?,
                    value1: integer(&row[3])?,
                    value2: integer(&row[4])?,
                    easing: integer(&row[5])?,
                })
            })
            .collect::<Result<Vec<_>>>()?;
        let castle = native(kbcs_bridge::cannon::setup(
            &kbcs_bridge::cannon::Setup {
                kind: cannon_id,
                level: i32::from(document.cannon.level.max(1)),
                range_level: facility("cannonRange")?,
                attack_level: facility("cannonAttack")?,
                treasure: environment.treasures[2],
                combo: environment.combos[6],
                status,
            },
            &cannon_growth,
        ))?;
        let mut cannon_rules = kbcs_bridge::cannon::Rules {
            encoded: [-1, -1, -1, clock_length("0x30d8", 0)?],
            attack_rate: rule(9)
                .map(|p| p.get(0).context("砲攻撃補正なし").and_then(integer))
                .transpose()?
                .unwrap_or(100),
        };
        let mut cannon_clips = BTreeMap::new();
        let cannon_cuts = kbcs_data::stage_media::cuts(
            &database,
            &format!("ImageData/nyankoCastle_001_{cannon_id:02}_00.imgcut"),
        )?
        .into_iter()
        .map(|[x, y, width, height]| render::Cut {
            x,
            y,
            width,
            height,
        })
        .collect();
        let cannon_texture =
            scene.texture(&format!("Number/nyankoCastle_001_{cannon_id:02}_00.png"));

        for phase in 0..3 {
            let stem = format!("nyankoCastle_001_{cannon_id:02}_{phase:02}");
            let animation = format!("ImageData/{stem}.maanim");
            if !database.connection.query_row(
                "SELECT EXISTS(SELECT 1 FROM asset_reference WHERE path=?1)",
                [&animation],
                |row| row.get::<_, bool>(0),
            )? {
                break;
            }
            let model = load_model(
                &database,
                &format!("ImageData/nyankoCastle_001_{cannon_id:02}_00.imgcut"),
                &format!("ImageData/{stem}.mamodel"),
                Some(&animation),
            )?;
            cannon_rules.encoded[phase] = native(model.clock_lengths())?[0];
            let texture = scene.texture(&format!("Number/nyankoCastle_001_{cannon_id:02}_00.png"));
            cannon_clips.insert(phase as i32, Clip { model, texture });
        }
        let equipment: Value = serde_json::from_str(&text(&database, "Data/equipmentlist.json")?)?;
        let mut members: Vec<_> = document
            .slots
            .iter()
            .enumerate()
            .filter_map(|(slot, member)| member.clone().map(|member| (slot, member)))
            .collect();
        if cannon_id == 2 {
            members.push((
                10,
                kbcs_data::formations::Member {
                    unit_id: u32::try_from(castle.words[26])?,
                    form: 0,
                    level: 1,
                    plus: 0,
                    talents: BTreeMap::new(),
                    orbs: Vec::new(),
                },
            ));
        }
        for (slot, member) in members.clone() {
            let parent = database.form(region, member.unit_id, member.form as usize)?;
            if let Some(id) = parent.raw.get(110).copied().flatten().filter(|id| *id >= 0) {
                let child = database.form(region, u32::try_from(id)?, 0)?;
                let level = (i64::from(member.level) + i64::from(member.plus))
                    .min(child.max_level + child.plus_level);
                members.push((
                    slot + 11,
                    kbcs_data::formations::Member {
                        unit_id: id as u32,
                        form: 0,
                        level: level.min(child.max_level) as u16,
                        plus: (level - child.max_level).max(0) as u16,
                        talents: BTreeMap::new(),
                        orbs: Vec::new(),
                    },
                ));
            }
        }
        for (slot, member) in &members {
            let slot = *slot;
            let form = database.form(region, member.unit_id, member.form as usize)?;
            if slot < 10 {
                rules.slot_rarity[slot] = i32::try_from(form.rarity)?;
            }
            ensure!(
                member.level as i64 <= form.max_level && member.plus as i64 <= form.plus_level,
                "キャラレベル範囲外"
            );
            let mut definition =
                native(actor::Definition::from_raw(&cells(&form.raw_cells)?, true))?;
            for (target, rate) in definition.growth.iter_mut().zip(form.growth.iter()) {
                *target = i32::try_from(rate.context("成長値なし")?)?;
            }
            for talent in kbcs_data::talents::read(&database.connection, region, member.unit_id)? {
                let level = member
                    .talents
                    .get(&(talent.index as u32))
                    .copied()
                    .unwrap_or(0) as usize;
                if level == 0 || form.rarity == 4 && member.level < 60 && talent.limit > 0 {
                    continue;
                }
                ensure!(
                    level <= talent.max_level && (0..73).contains(&talent.id),
                    "本能レベル範囲外"
                );
                let id = talent.id as usize;
                definition.talent_active[id] = 1;
                for i in 0..4 {
                    definition.talents[id][i] = i32::try_from(talent.values[level - 1][i])?;
                }
                for target in &talent.targets {
                    definition.added_targets |= 1
                        << TARGETS
                            .iter()
                            .position(|v| v == target)
                            .context("本能属性なし")?;
                }
            }
            let mut orbs = [battle::Orb::default(); 8];
            let mut orb_count = 0;
            for id in member.orbs.iter().flatten() {
                let entry = equipment["ID"]
                    .get(id.checked_sub(30000).context("本能玉ID範囲外")? as usize)
                    .context("本能玉なし")?;
                {
                    let effect = integer(&entry["content"])? as usize;
                    ensure!(effect < 32 && orb_count < 8, "本能玉範囲外");
                    let mut values = [0; 4];
                    for (i, value) in entry["value"]
                        .as_array()
                        .context("本能玉効果なし")?
                        .iter()
                        .enumerate()
                    {
                        ensure!(i < 4, "本能玉列範囲外");
                        values[i] = integer(value)?;
                        definition.orbs[effect][i] += values[i];
                    }
                    definition.orb_present[effect] = 1;
                    let mask = integer(
                        &constants["equipmentMasks"][integer(&entry["attribute"])? as usize],
                    )?;
                    orbs[orb_count] = battle::Orb {
                        effect: effect as i32,
                        mask,
                        values,
                    };
                    orb_count += 1;
                }
            }
            definition.orb_enabled = i32::from(orb_count > 0);
            let (motion, boundary, death_body_frames, model) = motion(
                &database,
                &mut scene,
                region,
                0,
                member.unit_id,
                member.form as usize,
                definition.cells[66],
            )?;
            let spawn = production::SpawnRequest {
                side: 0,
                raw: member.unit_id as i32 + 2,
                level_index: i32::from(member.level) + i32::from(member.plus) - 1,
                layer_min: definition.cells[14],
                layer_max: definition.cells[15],
                form: i32::from(member.form),
                row: 0,
            };
            let mut recharge_input = production::RechargeInput {
                base: definition.cells[7],
                talent: if member.form >= 2 {
                    definition.talents[26][0]
                } else {
                    0
                },
                research_level: facility("research")?,
                treasure: environment.treasures[11],
                combo: environment.combos[11]
                    + unit_combos
                        .get(&(member.unit_id as i32))
                        .map_or(0, |v| v[11]),
                stage_percent: rule(6)
                    .map(|v| integer(&v[form.rarity as usize]))
                    .transpose()?
                    .unwrap_or(100),
                override_frames: rule(1).map(|v| integer(&v[0])).transpose()?.unwrap_or(-1),
            };
            let recharge = native(production::recharge(&recharge_input))?;
            recharge_input.stage_percent = 100;
            recharge_input.override_frames = -1;
            let recharge_plain = native(production::recharge(&recharge_input))?;
            let raw_attack = [
                definition.cells[3],
                definition.cells[59],
                definition.cells[60],
            ];
            let mut price = production::Cost {
                enabled: 1,
                raw: definition.cells[6],
                talent: if member.form >= 2
                    && i32::from(member.level) + i32::from(member.plus)
                        >= definition.talent_min_level[25]
                {
                    definition.talents[25][0]
                } else {
                    0
                },
                chapter: rules.cost_chapter,
                fixed: rule(4).map(|v| integer(&v[0])).transpose()?.unwrap_or(-1),
                rarity_rate: rule(5)
                    .map(|v| integer(&v[form.rarity as usize]))
                    .transpose()?
                    .unwrap_or(100),
                orb_rate: definition.orbs[22][0],
                ..Default::default()
            };
            for &(group, value) in &cost_combos {
                if group != -1
                    && !combo_groups
                        .get(&group)
                        .is_some_and(|units| units.contains(&(member.unit_id as i32)))
                {
                    continue;
                }
                ensure!(
                    (price.combo_count as usize) < price.combos.len(),
                    "生産コストコンボが多すぎます"
                );
                price.combos[price.combo_count as usize] = value;
                price.combo_count += 1;
            }
            profiles.push(battle::Profile {
                price,
                definition,
                spawn,
                motion,
                deployment_slot: if slot < 10 { slot as i32 } else { -1 },
                cost: if slot < 10 {
                    start.config.costs[slot] * 100
                } else {
                    0
                },
                recharge,
                recharge_plain,
                money_base: 0,
                boundary: width - boundary * 20,
                death_body_frames,
                death_soul_frames: model.death_frames,
                summon_mode: i32::from(slot < 10 && form.is_spirit),
                raw_attack,
                orb_count: orb_count as i32,
                orbs,
            });
            models.push(model);
        }
        let mut rows = Vec::new();
        let mut ids = BTreeSet::new();
        for row in stage["spawns"].as_array().context("出現行なし")? {
            let cells: [i32; 14] = serde_json::from_value(row["native"].clone())?;
            ids.insert(cells[0] - 2);
            rows.push(stage::Row(cells));
        }
        if let Some(id) = stage["enemyCastle"].as_i64() {
            ids.insert(id as i32);
            environment.special_castle = id as i32 + 2;
            environment.castle_slot = 1;
        }
        let enemies = kbcs_data::enemies::read(&database.connection, region)?;
        for id in ids {
            ensure!(id >= 0, "敵ID範囲外");
            let enemy = enemies
                .iter()
                .find(|e| e.id == id as u32)
                .context("敵原本なし")?;
            let definition = native(actor::Definition::from_raw(
                &cells(&enemy.raw_cells)?,
                false,
            ))?;
            let (motion, boundary, death_body_frames, model) = motion(
                &database,
                &mut scene,
                region,
                1,
                id as u32,
                0,
                definition.cells[53],
            )?;
            let money_base = definition.cells[6];
            profiles.push(battle::Profile {
                definition,
                spawn: production::SpawnRequest {
                    side: 1,
                    raw: id + 2,
                    row: 0,
                    ..Default::default()
                },
                motion,
                deployment_slot: -1,
                cost: 0,
                recharge: 0,
                recharge_plain: 0,
                money_base,
                boundary: boundary * 10,
                death_body_frames,
                death_soul_frames: model.death_frames,
                summon_mode: 0,
                raw_attack: [0; 3],
                orb_count: 0,
                orbs: [battle::Orb::default(); 8],
                price: production::Cost::default(),
            });
            models.push(model);
        }
        let config = battle::Config {
            environment,
            screen: start.config,
            state: start.state,
            clock,
            hit,
            areas: actor::AreaRules {
                summon_sound_frame: parameter("battle_demon_summon_se_frame")?,
                summon_frame: parameter("battle_demon_summon_frame")?,
                summon_motion: [clock_length("0x29d8", 0)?, clock_length("0x2a10", 0)?],
                explosion_frames: [
                    parameter("battle_explosion_frame1")?,
                    parameter("battle_explosion_frame2")?,
                    parameter("battle_explosion_frame3")?,
                    parameter("battle_explosion_frame4")?,
                ],
                explosion_widths: [
                    parameter("battle_explosion_width1")?,
                    parameter("battle_explosion_width2")?,
                    parameter("battle_explosion_width3")?,
                ],
                explosion_damage: [
                    parameter("battle_explosion_damage1")?,
                    parameter("battle_explosion_damage2")?,
                    parameter("battle_explosion_damage3")?,
                ],
            },
            waves: actor::WaveRules {
                small_interval: parameter("battle_wave_s_inter")?,
                small_start: parameter("battle_wave_s_frame1")?,
                small_end: parameter("battle_wave_s_frame2")?,
                motion_frames: [clock_length("0x30d8", 0)?, clock_length("0x3148", 0)?],
                game_mode: 0,
            },
            castle_hp: [
                integer(&snapshot["castle"]["maximum"])?,
                integer(&stage["castleHealth"])?,
            ],
            enemy_max: integer(&stage["maxEnemies"])?.clamp(1, 50),
            unit_max: integer(&snapshot["deployment"]["maxUnits"])?.max(0),
            global_min: integer(&stage["spawnInterval"][0])?,
            global_max: integer(&stage["spawnInterval"][1])?,
            accounting_level: facility("accounting")?,
            death_surge_time: parameter("battle_death_volcano_time")?,
            death_surge_motion: [clock_length("0x27f8", 0)?, clock_length("0x2830", 0)?],
            guard_enabled: i32::from(stage["bossGuard"] == true),
            castle_offsets: [
                parameter("battle_castle_x0")?,
                parameter("battle_castle_y0")?,
                parameter("battle_castle_x1")?,
                parameter("battle_castle_y1")?,
                parameter("battle_castle_x2")?,
                parameter("battle_castle_y2")?,
            ],
            summon_position: parameter("summon_position")?,
            boss_frames: clock_length("0x1040", 1)?,
            castle_y_offset: scene.castle_geometry()[1],
            effect_clocks: {
                let mut values = [[0; 3]; 64];
                for (out, (key, clock)) in values
                    .iter_mut()
                    .zip(constants["clocks"].as_object().context("演出時計なし")?)
                {
                    *out = [
                        i32::from_str_radix(key.trim_start_matches("0x"), 16)?,
                        integer(&clock["lengths"][0])?,
                        integer(&clock["lengths"][1])?,
                    ];
                }
                values
            },
            price_rule: {
                let mut values = [0; 4];
                if let Some(rule) = rule(11) {
                    let parameters = rule.as_array().context("生産価格ルールなし")?;
                    ensure!(
                        (1..=3).contains(&parameters.len()),
                        "生産価格ルールの列数不正"
                    );
                    values[0] = parameters.len() as i32;
                    for (out, parameter) in values[1..].iter_mut().zip(parameters) {
                        *out = integer(parameter)?;
                    }
                }
                values
            },
            rules,
            castle,
            cannon: cannon_rules,
            seed: u32::try_from(integer(&snapshot["seed"])?)?,
        };
        let mut effects = BTreeMap::new();
        let effect_catalog = kbcs_data::effects::catalog(&database)?;
        for (kind, name) in [
            (0, "skill_wave_attack"),
            (1, "skill_smallwave_attack"),
            (2, "skill_volcano"),
            (3, "skill_smallvolcano"),
            (4, "skill_explosion"),
        ] {
            for side in 0..2 {
                let id = format!("{name}{}", if side == 1 { "_e" } else { "" });
                let entry = effect_catalog["entries"]
                    .as_array()
                    .context("効果一覧なし")?
                    .iter()
                    .find(|e| e["id"] == id)
                    .context("戦闘効果モデルなし")?;
                let cut = entry["cut"].as_str().context("効果分割なし")?;
                let model = entry["model"].as_str().context("効果モデルなし")?;
                let texture = scene.texture(entry["image"].as_str().context("効果画像なし")?);
                for (phase, animation) in entry["animations"]
                    .as_array()
                    .context("効果モーションなし")?
                    .iter()
                    .enumerate()
                {
                    let model = load_model(&database, cut, model, animation["path"].as_str())?;
                    effects.insert((kind, side, phase as i32), Clip { model, texture });
                }
            }
        }
        // 009f560cで対応を確認した時計から、共通演出モデルを登録する。
        for (offset, clock) in constants["clocks"].as_object().context("演出時計なし")? {
            let animation = clock["path"].as_str().context("演出ファイルなし")?;
            let entry = effect_catalog["entries"]
                .as_array()
                .context("効果一覧なし")?
                .iter()
                .find(|e| {
                    e["animations"]
                        .as_array()
                        .is_some_and(|a| a.iter().any(|v| v["path"] == animation))
                })
                .with_context(|| format!("演出のモデルなし: {animation}"))?;
            let model = load_model(
                &database,
                entry["cut"].as_str().context("演出分割なし")?,
                entry["model"].as_str().context("演出モデルなし")?,
                Some(animation),
            )?;
            let texture = scene.texture(entry["image"].as_str().context("演出画像なし")?);
            let phase = i32::from_str_radix(offset.trim_start_matches("0x"), 16)?;
            effects.insert((6, 0, phase), Clip { model, texture });
        }
        let mut core = native(battle::Battle::new(&config, &profiles, &rows))?;
        let (receipt, reward_rules) = crate::battle_rewards::Receipt::new(
            root,
            region,
            persist_rewards,
            &database,
            map,
            stage,
            crown,
            facility("study")? + 1,
            config.environment.treasures[6],
            config.environment.combos[13],
            config.screen.items as u32,
        )?;
        native(core.reward_rules(&reward_rules))?;
        let title = kbcs_data::stage_media::battle_title(&database, map, stage)?;
        let title_draw = title["image"]
            .as_str()
            .map(|path| -> Result<_> {
                let [x, y, width, height]: [i32; 4] = serde_json::from_value(title["cut"].clone())?;
                Ok((
                    render::Cut {
                        x,
                        y,
                        width,
                        height,
                    },
                    scene.texture(path),
                ))
            })
            .transpose()?;
        let mut top_cuts = [Vec::new(), Vec::new()];
        let mut top_textures = [-1; 2];
        for (i, stem) in ["img001_ja", "FeverEffect"].iter().enumerate() {
            if i == 0 && matches!(rules.score_type, 1 | 3) || i == 1 && rules.point.fever_count >= 3
            {
                top_cuts[i] =
                    kbcs_data::stage_media::cuts(&database, &format!("ImageData/{stem}.imgcut"))?
                        .into_iter()
                        .map(|[x, y, width, height]| render::Cut {
                            x,
                            y,
                            width,
                            height,
                        })
                        .collect();
                top_textures[i] = scene.texture(&format!("Image/{stem}.png"));
            }
        }
        Ok(Self {
            database,
            scene,
            core,
            rules,
            models,
            effects,
            key: start.scene.key(),
            title,
            receipt,
            cannon_clips,
            cannon_cuts,
            cannon_texture,
            castle_slot: config.environment.castle_slot,
            sniper_cuts,
            sniper_textures,
            top_cuts,
            top_textures,
            title_draw,
        })
    }
    pub fn draw(&mut self, input: &crate::scene::Input) -> Result<crate::scene::Frame<'_>> {
        let visuals = native(self.core.visuals())?.to_vec();
        let (actors, profiles) = native(self.core.actors())?;
        let mut frame = self
            .scene
            .draw(&self.database, input)
            .context("戦闘背景の描画")?;
        let mut order = Vec::new();
        // 006ddfb8は敵→味方の枠順で集め、レイヤーの小さい順に選択する。
        for side in [1, 0] {
            for (slot, actor) in actors[side].iter().enumerate().skip(1) {
                if actor.words[0] != 0 {
                    order.push((side, slot));
                }
            }
        }
        for i in 0..order.len() {
            let mut first = i;
            for j in i + 1..order.len() {
                if actors[order[j].0][order[j].1].words[5]
                    < actors[order[first].0][order[first].1].words[5]
                {
                    first = j;
                }
            }
            order.swap(i, first);
        }
        let mut commands = Vec::new();
        for (side, slot) in order {
            let words = &actors[side][slot].words;
            let model = self
                .models
                .get(profiles[side][slot] as usize)
                .context("個体モデルなし")?;
            let action = words[1];
            let clip = match action {
                0 => 0,
                1 | 16 | 18 | 19 | 20 => 1,
                2 => 2,
                3 | 5 | 6 | 17 => 3,
                7 => 0,
                10 => 7,
                11 => 4,
                12 => 5,
                13 => 6,
                4 | 21 => 8,
                _ => continue,
            };
            if let Some(asset) = model.clips.get(&clip) {
                paint_clip(
                    &mut commands,
                    asset,
                    &frame.layout,
                    if action == 7 { 0 } else { words[2] },
                    f64::from(words[3] / 10),
                    f64::from(words[4] / 10 + words[5] * 4 - if clip == 9 { 97 } else { 0 }),
                    clip != 9,
                )
                .with_context(|| {
                    format!(
                        "{}: side={side}, slot={slot}, action={action}, frame={}",
                        model.name, words[2]
                    )
                })?;
            } else if action != 4 && action != 21 && action != 10 {
                anyhow::bail!("{}: 行動{action}のモーション{clip}がありません", model.name)
            }
            if action == 10
                && let Some(entry) = model.clips.get(&10)
            {
                let point = model
                    .clips
                    .get(&7)
                    .map(|clip| native(clip.model.native_point(words[2], 0)))
                    .transpose()?
                    .unwrap_or([0; 2]);
                paint_clip(
                    &mut commands,
                    entry,
                    &frame.layout,
                    words[2],
                    f64::from(words[3] / 10 + point[0]),
                    f64::from(words[4] / 10 + words[5] * 4),
                    false,
                )?;
            }
            if (action == 4 || action == 21)
                && let Some(soul) = model.clips.get(&9)
            {
                paint_clip(
                    &mut commands,
                    soul,
                    &frame.layout,
                    words[2],
                    f64::from(words[3] / 10),
                    f64::from(words[4] / 10 + words[5] * 4 - 97),
                    false,
                )?;
            }
            let belonging = |v: &&battle::Visual| v.side == side as i32 && v.slot == slot as i32;
            for value in visuals
                .iter()
                .filter(belonging)
                .filter(|v| v.kind == 7)
                .chain(
                    visuals
                        .iter()
                        .filter(belonging)
                        .filter(|v| (0..=3).contains(&v.kind)),
                )
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 9))
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 4))
            {
                let asset = self
                    .effects
                    .get(&(
                        if value.kind == 7 || value.kind == 9 {
                            6
                        } else {
                            value.kind
                        },
                        if value.kind == 7 || value.kind == 9 {
                            0
                        } else {
                            value.side
                        },
                        value.phase,
                    ))
                    .context("効果描画モデルなし")?;
                paint_clip(
                    &mut commands,
                    asset,
                    &frame.layout,
                    value.frame,
                    f64::from(value.x),
                    f64::from(value.y),
                    false,
                )?;
            }
        }
        commands.extend(native(self.core.sniper_draw(
            &frame.layout,
            [&self.sniper_cuts[0], &self.sniper_cuts[1]],
            self.sniper_textures,
        ))?);
        commands.extend(native(self.core.hit_draw(
            &frame.layout,
            &self.sniper_cuts[1],
            self.sniper_textures[1],
        ))?);
        for value in visuals.iter().filter(|v| v.kind == 6) {
            let asset = self
                .effects
                .get(&(6, 0, value.phase))
                .context("共通演出モデルなし")?;
            paint_clip(
                &mut commands,
                asset,
                &frame.layout,
                value.frame,
                f64::from(value.x),
                f64::from(value.y),
                false,
            )?;
        }
        if [1, 3, 9, 12].contains(&actors[0][0].words[9]) {
            commands.extend(native(self.core.cannon_draw(
                &frame.layout,
                &self.cannon_cuts,
                self.cannon_texture,
            ))?);
        }
        for value in visuals.iter().filter(|v| v.kind == 5) {
            if let Some(asset) = self.cannon_clips.get(&value.phase) {
                let packets = native(asset.model.pose_scaled(value.frame, value.root))?;
                paint_packets(
                    &mut commands,
                    asset,
                    &frame.layout,
                    &packets,
                    f64::from(value.x),
                    f64::from(value.y),
                )?;
            }
        }
        for value in visuals.iter().filter(|v| v.kind == 8) {
            let asset = self
                .effects
                .get(&(6, 0, value.phase))
                .context("ボス演出モデルなし")?;
            paint_clip(
                &mut commands,
                asset,
                &frame.layout,
                value.frame,
                f64::from(value.x),
                f64::from(value.y),
                false,
            )?;
        }
        let at = frame
            .commands
            .iter()
            .position(|c| c.layer > 2)
            .unwrap_or(frame.commands.len());
        frame.commands.splice(at..at, commands);
        if matches!(self.rules.score_type, 1 | 3) {
            frame.commands.extend(native(self.core.top_draw(
                &self.top_cuts[0],
                &self.top_cuts[1],
                self.top_textures,
                self.title_draw,
            ))?);
        } else {
            // 通常ステージも終了帯の乗算を背景と同じ描画先へ適用する。
            frame.commands.extend(native(self.core.top_draw(
                &self.sniper_cuts[1],
                &[],
                self.sniper_textures,
                self.title_draw,
            ))?);
        }
        frame.animated = true;
        Ok(frame)
    }
    pub fn settle(&mut self) -> Result<()> {
        let first = self.receipt.saved.is_none();
        self.receipt.settle(&self.core);
        if first && let Some(saved) = &self.receipt.saved {
            native(
                self.core
                    .notifications(saved["notifications"].as_array().map_or(0, Vec::len) as i32),
            )?;
        }
        Ok(())
    }
    pub fn ending_camera(&self, input: &mut crate::scene::Input) -> Result<()> {
        let camera = native(self.core.end_camera())?;
        if camera.width > 0 {
            input.zoom = f64::from(camera.zoom / 100) / 100.;
            input.center = Some(f64::from(camera.left) / 10. + 480. / input.zoom);
            input.focus = 4;
        }
        Ok(())
    }
    pub fn stats(&self) -> Result<Value> {
        let (actors, profiles) = native(self.core.actors())?;
        let (production, seed) = native(self.core.production())?;
        let count = |side: usize| actors[side][1..].iter().filter(|a| a.words[0] != 0).count();
        let mut units = Vec::new();
        for side in 0..2 {
            for slot in 1..51 {
                let a = &actors[side][slot].words;
                if a[0] != 0 {
                    units.push(json!({"side":side,"slot":slot,"profile":profiles[side][slot],"raw":a[0],"layer":a[5],"frame":a[2],"action":a[1],"hp":a[8],"maximum":a[7],"x":a[3],"y":a[4],"serial":a[240]}));
                }
            }
        }
        Ok(
            json!({"ex":native(self.core.ex())?,"endCamera":native(self.core.end_camera())?,"music":native(self.core.music())?,"ending":native(self.core.ending())?,"receipt":self.receipt.saved,"receiptError":self.receipt.error,"rewardRolls":native(self.core.rewards())?,"units":count(0),"enemies":count(1),"castleHp":[actors[0][0].words[8],actors[1][0].words[8]],"wait":production.wait,"maximum":production.maximum,"costs":native(self.core.prices())?,"produced":production.produced,"extras":native(self.core.extras())?,"points":native(self.core.points())?,"lastCosts":production.last_cost,"seed":seed,"actors":units,"cannon":[actors[0][0].words[9],actors[0][0].words[10],actors[0][0].words[13]],"sniper":native(self.core.sniper_status())?,"computer":native(self.core.computer())?,"sounds":native(self.core.sounds())?,"result":native(self.core.outcome())?,"deployment":native(self.core.deployment())?,"rules":self.rules}),
        )
    }
    pub fn layout(&self, input: &crate::scene::Input) -> Result<render::Layout> {
        native(render::layout(&render::SceneInput {
            width: input.width,
            center: input.center.unwrap_or(input.width),
            zoom: input.zoom,
            cut_height: 510,
            castle: self.scene.castle_geometry(),
            focus: input.focus,
            viewport_width: input.viewport_width,
            battle_rows: input.battle_rows,
        }))
    }
    pub fn hud(&self, layout: &render::Layout) -> Result<battle::Hud> {
        let (actors, profiles) = native(self.core.actors())?;
        let point = usize::try_from(self.castle_slot)
            .ok()
            .filter(|&slot| slot > 0 && slot < 51)
            .and_then(|slot| {
                self.models
                    .get(profiles[1][slot] as usize)
                    .map(|model| (model, actors[1][slot].words[2]))
            })
            .map(|(model, frame)| {
                model
                    .clips
                    .get(&1)
                    .map(|clip| native(clip.model.native_point(frame, 1)))
                    .transpose()
            })
            .transpose()?
            .flatten()
            .unwrap_or([0; 2]);
        native(self.core.hud(layout, point))
    }
}

#[allow(clippy::too_many_arguments)]
fn paint_clip(
    commands: &mut Vec<render::Command>,
    asset: &Clip,
    layout: &render::Layout,
    frame: i32,
    x: f64,
    y: f64,
    anchor: bool,
) -> Result<()> {
    let local = if anchor {
        native(asset.model.pose_config(frame, 0, 1))?
    } else {
        native(asset.model.pose(frame, false, false, 1))?
    };
    paint_packets(commands, asset, layout, &local, x, y)
}
fn paint_packets(
    commands: &mut Vec<render::Command>,
    asset: &Clip,
    layout: &render::Layout,
    packets: &[render::Packet],
    x: f64,
    y: f64,
) -> Result<()> {
    for packet in packets {
        let cut = asset
            .model
            .cuts
            .get(packet.cut as usize)
            .context("画像の分割IDなし")?;
        let mut command = render::Command {
            texture: asset.texture,
            layer: 2,
            count: 4,
            blend: packet.blend,
            opacity: packet.opacity,
            cut: [cut.x, cut.y, cut.width, cut.height],
            ..Default::default()
        };
        for (to, from) in command.points.iter_mut().zip(packet.points) {
            *to = f64::from(from);
        }
        commands.push(native(render::transform(layout, &command, x, y, 0.))?);
    }
    Ok(())
}
