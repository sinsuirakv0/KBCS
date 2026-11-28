use anyhow::{Context, Result, ensure};
use kbcs_bridge::{battle, battle_screen, render, stage};
#[cfg(not(target_os = "emscripten"))]
use kbcs_bridge::{actor, production};
#[cfg(not(target_os = "emscripten"))]
use kbcs_data::{equipment, formations::Document, store::Database};
use serde::{Deserialize, Serialize};
use serde_json::{Value, json};
#[cfg(not(target_os = "emscripten"))]
use kbcs_data::inventory::CONTINUE_CAT_FOOD_COST as CONTINUE_COST;
#[cfg(target_os = "emscripten")]
const CONTINUE_COST: i64 = 30;
use std::collections::{BTreeMap, BTreeSet, HashMap, VecDeque};
#[path = "battle_inspector.rs"]
pub(super) mod inspector;
#[path = "battle_runtime.rs"]
pub mod runtime;

#[cfg(not(target_os = "emscripten"))]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Start {
    pub snapshot: Value,
    pub config: battle_screen::Config,
    pub state: battle_screen::State,
    pub scene: crate::scene::Input,
    #[serde(default)]
    pub require_exact: bool,
}

#[cfg(not(target_os = "emscripten"))]
fn set_sortie_speed(
    snapshot: &Value,
    screen: &mut battle_screen::Config,
    state: &mut battle_screen::State,
) {
    // ボタンは常設し、持ち込みの有無で開始倍率と切替上限を決める。
    let equipped = snapshot["items"]["speedup"].as_bool() == Some(true);
    screen.items |= 1;
    screen.speed = if equipped && snapshot["speed"] == 3 {
        3
    } else {
        2
    };
    state.items_on = (state.items_on & !1) | i32::from(equipped);
    state.speed_mode = if equipped { screen.speed - 1 } else { 0 };
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
    #[serde(default)]
    pub cheats: u32,
    #[serde(default)]
    pub skip_combos: bool,
    #[serde(default)]
    pub inspection: Option<Vec<inspector::Query>>,
    pub focus_actor: Option<i32>,
    pub phone_stats: Option<Value>,
    #[serde(default)]
    pub compact: bool,
}
#[derive(Default)]
pub struct ActorDrawRanges {
    pub focus: Option<(usize, usize)>,
    pub preview: Option<[usize; 2]>,
}
#[derive(Serialize, Deserialize)]
pub struct Clip {
    pub model: render::Model,
    pub texture: i32,
}
#[derive(Serialize, Deserialize)]
pub struct MotionSet {
    pub death_frames: i32,
    pub clips: BTreeMap<i32, Clip>,
    pub name: String,
    pub character: Value,
}
#[derive(Serialize, Deserialize)]
pub struct Prepared {
    pub scene: crate::scene::Scene,
    pub data: BattleData,
    config: battle::Config,
    profiles: Vec<battle::Profile>,
    rows: Vec<stage::Row>,
    hint_candidates: Vec<i32>,
    hint_lengths: Vec<i32>,
    reward_rules: battle::RewardRules,
    continue_policy: battle::ContinuePolicy,
}

#[derive(Serialize, Deserialize)]
pub struct BattleData {
    pub models: Vec<MotionSet>,
    #[serde(with = "effect_entries")]
    effects: BTreeMap<(i32, i32, i32), Clip>,
    pub key: String,
    pub title: Value,
    pub stage_sounds: Vec<i32>,
    pub stage_music: [i32; 2],
    combos: Vec<Value>,
    defeat_hints: Vec<Vec<String>>,
    boss_hp: Option<String>,
    continue_notice: Option<String>,
    continue_text: Option<(Vec<String>, String)>,
    cannon_clips: BTreeMap<i32, Clip>,
    cannon_cuts: Vec<render::Cut>,
    cannon_texture: i32,
    range_cuts: Vec<render::Cut>,
    range_texture: i32,
    castle_slot: i32,
    orb_icons: [Vec<[i32; 2]>; 10],
    sniper_cuts: [Vec<render::Cut>; 2],
    sniper_textures: [i32; 2],
    top_cuts: [Vec<render::Cut>; 2],
    top_textures: [i32; 2],
    title_draw: Option<(render::Cut, i32)>,
    precision: Value,
}

impl BattleData {
    pub fn active_combo_ids(&self) -> Vec<i64> {
        self.combos.iter().filter_map(|combo| combo["id"].as_i64()).collect()
    }
}

mod effect_entries {
    use super::*;

    type Entries = BTreeMap<(i32, i32, i32), Clip>;
    pub fn serialize<S: serde::Serializer>(value: &Entries, serializer: S) -> Result<S::Ok, S::Error> {
        serializer.collect_seq(value)
    }
    pub fn deserialize<'de, D: serde::Deserializer<'de>>(deserializer: D) -> Result<Entries, D::Error> {
        Ok(Vec::<((i32, i32, i32), Clip)>::deserialize(deserializer)?.into_iter().collect())
    }
}

pub struct Session {
    pub scene: crate::scene::Scene,
    pub core: battle::Battle,
    pub data: BattleData,
    rules: battle::Rules,
    pub combo_skipped: bool,
    pub saved: Option<Value>,
    pub receipt_error: Option<String>,
    continue_balance: Option<i64>,
    continue_error: Option<String>,
    continues_on_camera: i32,
    ending_camera_applied: bool,
    poses: PoseCache,
}

impl Prepared {
    pub fn start(mut self) -> Result<Session> {
        self.scene.restore_effects()?;
        let mut core = native(battle::Battle::new(&self.config, &self.profiles, &self.rows))?;
        native(core.hints(
            &self.hint_candidates,
            &self.hint_lengths,
            self.data.defeat_hints.first().map_or(0, |lines| lines.len() as i32),
        ))?;
        native(core.reward_rules(&self.reward_rules))?;
        native(core.continue_policy(self.continue_policy))?;
        Ok(Session {
            scene: self.scene,
            core,
            data: self.data,
            rules: self.config.rules,
            combo_skipped: false,
            saved: None,
            receipt_error: None,
            continue_balance: None,
            continue_error: None,
            continues_on_camera: 0,
            ending_camera_applied: false,
            poses: PoseCache::default(),
        })
    }
}

#[cfg(not(target_os = "emscripten"))]
fn integer(value: &Value) -> Result<i32> {
    value
        .as_i64()
        .and_then(|n| i32::try_from(n).ok())
        .context("戦闘の整数入力がありません")
}
fn native<T>(value: std::result::Result<T, u32>) -> Result<T> {
    value.map_err(|code| anyhow::anyhow!("戦闘コア: {code}"))
}

#[cfg(not(target_os = "emscripten"))]
fn text(db: &Database, path: &str) -> Result<String> {
    Ok(String::from_utf8(db.source(path)?.3)?
        .trim_start_matches('\u{feff}')
        .into())
}
#[cfg(not(target_os = "emscripten"))]
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
#[cfg(not(target_os = "emscripten"))]
fn inputs() -> Result<Value> {
    Ok(serde_json::from_str(
        include_str!("../../kbcs-data/resources/battle-inputs.json").trim_start_matches('\u{feff}'),
    )?)
}
// 原本のatoi同様、整数接頭辞の後の注記を値へ含めない。
#[cfg(not(target_os = "emscripten"))]
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
#[cfg(not(target_os = "emscripten"))]
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
#[cfg(not(target_os = "emscripten"))]
fn motion(
    db: &Database,
    scene: &mut crate::scene::Scene,
    region: &str,
    side: i32,
    id: u32,
    form: usize,
    revive: i32,
) -> Result<(actor::Motion, i32, i32, MotionSet)> {
    let manifest = kbcs_data::motions::resources(
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
        let cut_text = text(db, cut)?;
        let model_text = text(db, model)?;
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
            let animation = animation["path"]
                .as_str()
                .map(|path| text(db, path))
                .transpose()?;
            let m = render::Model::parse(&cut_text, &model_text, animation.as_deref())
                .map_err(anyhow::Error::msg)?;
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
            character: manifest["character"].clone(),
        },
    ))
}
impl Session {
    #[cfg(not(target_os = "emscripten"))]
    pub fn prepare(
        root: &std::path::Path,
        region: &str,
        start: Start,
        persist_rewards: bool,
    ) -> Result<(Prepared, crate::battle_rewards::Receipt)> {
        let database = Database::open(root, region)?;
        let metadata = database.metadata()?;
        let snapshot = &start.snapshot;
        let settings = catalog()?;
        let constants = inputs()?;
        for (path, source) in constants["sources"]
            .as_object()
            .context("戦闘入力の出典なし")?
        {
            if let Some(matches) = kbcs_data::compatibility::source_matches(
                &database,
                path,
                source["sha256"].as_str().context("入力SHAなし")?,
            )? {
                ensure!(
                    matches
                        || path == "Data/param.tsv"
                            && kbcs_data::compatibility::parameters_match(
                                &database,
                                &constants["parameters"]
                            )?,
                    "戦闘入力の原本SHAまたは参照値が一致しません: {path}"
                );
            }
        }
        for source in constants["clocks"]
            .as_object()
            .context("効果時計なし")?
            .values()
        {
            if let Some(path) = source["path"].as_str()
                && let Some(matches) = kbcs_data::compatibility::source_matches(
                    &database,
                    path,
                    source["source"]["sha256"].as_str().context("時計SHAなし")?,
                )?
            {
                ensure!(matches, "効果時計の原本SHAが一致しません: {path}");
            }
        }
        ensure!(
            kbcs_data::compatibility::calculation_version(&database)?.is_some()
                && (snapshot["version"].is_null()
                    || snapshot["version"].as_str() == metadata.get("version").map(String::as_str))
                && snapshot["buildId"].as_str() == metadata.get("build_id").map(String::as_str),
            "戦闘入力とDBの版が一致しません"
        );
        let mut document: Document = serde_json::from_value(snapshot["formation"].clone())?;
        let equipment = equipment::Catalog::read(&database)?;
        document.validate_with_equipment(region, &equipment)?;
        for member in document.slots.iter_mut().flatten() {
            member.form = member.effective_form(&database, region)?.index as u8;
        }
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
        let mut precision = kbcs_data::support::Precision::checked();
        if metadata.get("version").map(String::as_str) != settings["version"].as_str() {
            precision.note("ruleset", kbcs_bridge::ruleset_version().into());
        }
        for rule in map["rules"].as_array().into_iter().flatten() {
            if rule["support"] == "unsupported" {
                precision.note(
                    "stageRule",
                    rule["id"].as_i64().context("特殊ルールIDが不正です")?,
                );
            }
        }
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
                -8 if map["number"] == 68 => 16,
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
        let mut active_combos = Vec::new();
        let effects = kbcs_data::combos::effects(&database.connection, region)?;
        for combo in kbcs_data::combos::read(&database.connection, region)? {
            if combo.members.iter().all(|m| {
                document.slots[..5]
                    .iter()
                    .flatten()
                    .any(|p| p.unit_id as i64 == m.id && p.form as i64 >= m.form)
            }) {
                if !combo.support.is_supported() {
                    precision.note("combo", combo.id);
                    continue;
                }
                if !combo.unlocked(|unlock| {
                    document.slots.iter().flatten().any(|member| {
                        member.unit_id == unlock.unit_id
                            && member.total_level() >= unlock.minimum_level
                            && member
                                .talents
                                .get(&(unlock.talent_index as u32))
                                .is_some_and(|&level| level > 0)
                    })
                }) {
                    continue;
                }
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
                active_combos.push(combo);
            }
        }
        let parameter = |name: &str| integer(&constants["parameters"][name]);
        // 0088fde0は構成数でstable_sortする。同数ならCSVの順を保つ。
        active_combos.sort_by_key(|combo| combo.members.len());
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
        // 008cfcf0はマップ・冠・面が固定編成の行と一致する場合に集計値を抑止する。
        let fixed_formation = stage["formation"]["selected"].as_i64() == Some(i64::from(crown) - 1);
        let mut orb_icons: [Vec<[i32; 2]>; 10] = Default::default();
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
            for (column, _) in kbcs_data::support::extension_cells(&form.raw, 119) {
                precision.note("unitColumn", column as i64);
            }
            let mut definition = native(actor::Definition::from_raw(
                &cells(&form.raw_cells[..form.raw_cells.len().min(119)])?,
                true,
            ))?;
            for (target, rate) in definition.growth.iter_mut().zip(form.growth.iter()) {
                *target = i32::try_from(rate.context("成長値なし")?)?;
            }
            let talents = kbcs_data::talents::read(&database.connection, region, member.unit_id)?;
            for talent in &talents {
                if !talent.support.is_supported()
                    && form.index >= 2
                    && member
                        .talents
                        .get(&(talent.index as u32))
                        .is_some_and(|&level| level > 0)
                {
                    precision.note("talent", talent.id);
                }
                let level = member.active_talent_level(&form, talent);
                if level == 0 {
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
                definition.added_targets |= equipment::target_mask(talent) as i32;
            }
            let mut orbs = [battle::Orb::default(); 8];
            let mut grades = [0; 8];
            let mut orb_count = 0;
            if !fixed_formation && member.orbs.iter().any(Option::is_some) {
                let eligible = equipment.eligibility(member, &form, &talents)?;
                for (index, id) in member.orbs.iter().enumerate() {
                    let Some(id) = id else { continue };
                    let orb = equipment.get(*id)?;
                    if form.index >= 2
                        && let Some(condition) = eligible
                            .slots
                            .get(index)
                            .and_then(|slot| slot.unsupported_condition)
                    {
                        precision.note("equipmentSlot", condition);
                    }
                    if !orb.supported()
                        && eligible.slots.get(index).is_some_and(|slot| slot.unlocked)
                    {
                        precision.note("equipment", i64::from(orb.content));
                    }
                    let mask = equipment.mask(orb);
                    if !eligible.active(index, orb, mask) {
                        continue;
                    }
                    let mut values = [0; 4];
                    values[..orb.value.len()].copy_from_slice(&orb.value);
                    orbs[orb_count] = battle::Orb {
                        effect: i32::try_from(orb.content)?,
                        mask: mask as i32,
                        values,
                    };
                    grades[orb_count] = i32::try_from(orb.grade)?;
                    if let Some(icons) = orb_icons.get_mut(slot) {
                        icons.push([orb.attribute.map_or(12, |value| value as i32), orbs[orb_count].effect]);
                    }
                    orb_count += 1;
                }
            }
            native(battle::equipment(
                &orbs[..orb_count],
                &grades[..orb_count],
                &mut definition,
            ))?;
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
            for (column, _) in kbcs_data::support::extension_cells(&enemy.raw, 113) {
                precision.note("enemyColumn", column as i64);
            }
            let definition = native(actor::Definition::from_raw(
                &cells(&enemy.raw_cells[..enemy.raw_cells.len().min(113)])?,
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
        let mut screen = start.config;
        let mut state = start.state;
        set_sortie_speed(snapshot, &mut screen, &mut state);
        let config = battle::Config {
            environment,
            screen,
            state,
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
            // 006db434の9019f4呼出は未収録キーに15を返す。
            red_gauge_frames: constants["parameters"]["battle_red_gauge_frame"]
                .as_i64()
                .unwrap_or(15) as i32,
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
            seed: snapshot["seed"]
                .as_u64()
                .and_then(|value| u32::try_from(value).ok())
                .filter(|&value| value != 0)
                .context("戦闘乱数のシードが不正です")?,
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
            let entries = effect_catalog["entries"]
                .as_array()
                .context("効果一覧なし")?;
            let uses_animation = |entry: &&Value| {
                entry["animations"]
                    .as_array()
                    .is_some_and(|a| a.iter().any(|v| v["path"] == animation))
            };
            // 005d4824の陣営別モデル。敵側は味方用の画像グループへ代替しない。
            let reflection_model = matches!(offset.as_str(), "0x29d8" | "0x2a10")
                .then(|| animation.replace(".maanim", ".mamodel"));
            let entry = entries
                .iter()
                .filter(uses_animation)
                .find(|entry| {
                    reflection_model
                        .as_ref()
                        .is_none_or(|model| entry["model"] == model.as_str())
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
        ensure!(
            !start.require_exact || precision.issues.is_empty(),
            "精度指定により戦闘を開始できません: {}",
            serde_json::to_string(&precision)?
        );
        let hints = kbcs_data::model::csv_rows(&database.source("res/Lose_ja.csv")?.3)?;
        let groups: Vec<i32> = hints
            .iter()
            .map(|row| row[0].parse().context("敗北ヒントの分類が不正です"))
            .collect::<Result<_>>()?;
        let settings =
            kbcs_data::model::numeric_rows(&database.source("Data/LoseTextSetting.csv")?.3)?
                .into_iter()
                .map(|row| {
                    row.1
                        .into_iter()
                        .map(|cell| {
                            i32::try_from(cell.context("敗北ヒントの条件がありません")?)
                                .context("敗北ヒントの条件範囲が不正です")
                        })
                        .collect::<Result<Vec<_>>>()
                })
                .collect::<Result<Vec<_>>>()?;
        let context = battle::HintContext {
            mode: integer(&map["nativeMode"])?,
            map_id: integer(&map["nativeId"])?,
            stage: integer(&stage["index"])?,
            crown: crown - 1,
            special: i32::from(
                map["nativeKind"] == -19 || map["nativeKind"] == -8 && map["number"] == 42,
            ),
            progress: 1,
            cosmos: 1,
        };
        // ユーザー指定の全章解放・進行済み状態。選択とRNGは所有C++へ渡す。
        let candidates = native(battle::hint_candidates(&context, &groups, &settings))?;
        let defeat_hints: Vec<Vec<String>> = hints
            .into_iter()
            .map(|row| {
                row.into_iter()
                    .skip(1)
                    .take_while(|cell| cell != "＠")
                    .collect()
            })
            .collect();
        let lengths: Vec<i32> = candidates
            .iter()
            .map(|&id| defeat_hints[id as usize].len() as i32)
            .collect();
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
        let stage_sounds = std::iter::once(reward_rules.start_sound)
            .chain(
                reward_rules
                    .win_sounds
                    .into_iter()
                    .take(reward_rules.win_count as usize),
            )
            .chain(
                reward_rules
                    .lose_sounds
                    .into_iter()
                    .take(reward_rules.lose_count as usize),
            )
            .filter(|id| *id >= 0)
            .collect();
        let continue_policy = if stage["noContinue"] == true {
            battle::ContinuePolicy::Forbidden
        } else if persist_rewards && !matches!(rules.score_type, 1 | 3) {
            battle::ContinuePolicy::Offer
        } else {
            battle::ContinuePolicy::Hint
        };
        let (continue_text, continue_notice) =
            if matches!(continue_policy, battle::ContinuePolicy::Hint) {
                (None, None)
            } else {
                // 005eb040 / 005ecde0: Warning2の行0が不足、行2が復活確認、行122が禁止の文面。
                let bytes = kbcs_data::source::asset(&database, root, "res/Warning2_ja.csv")?;
                let warnings = kbcs_data::model::csv_rows(&bytes)?;
                let warning = |index: usize| {
                    warnings
                        .get(index)
                        .filter(|row| !row.is_empty())
                        .with_context(|| format!("Warning2の原本文面がありません。行番号 {index}"))
                };
                if matches!(continue_policy, battle::ContinuePolicy::Forbidden) {
                    (None, Some(warning(122)?[0].clone()))
                } else {
                    let lines = warning(2)?
                        .iter()
                        .take_while(|line| line.as_str() != "＠")
                        .cloned()
                        .collect();
                    (Some((lines, warning(0)?[0].clone())), None)
                }
            };
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
        let range_cuts = kbcs_data::stage_media::cuts(&database, "ImageData/img002_ja.imgcut")?
            .into_iter()
            .take(2)
            .map(|[x, y, width, height]| render::Cut {
                x,
                y,
                width,
                height,
            })
            .collect();
        let range_texture = scene.texture("Image/img002_ja.png");
        let mut top_cuts = [Vec::new(), Vec::new()];
        let mut top_textures = [-1; 2];
        for (i, stem) in ["img001_ja", "FeverEffect"].iter().enumerate() {
            if i == 0 || rules.point.fever_count >= 3 {
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
        // 出撃時に背景演出の画像索引まで確定し、戦闘フレームからDB参照を外す。
        scene.prepare_effects(&database, &start.scene)?;
        let data = BattleData {
            precision: serde_json::to_value(precision)?,
            models,
            effects,
            key: start.scene.key(),
            title,
            stage_sounds,
            stage_music: reward_rules.music,
            combos: active_combos.into_iter().map(serde_json::to_value).collect::<Result<_, _>>()?,
            defeat_hints,
            boss_hp: receipt.text("boss_hp").ok().map(str::to_owned),
            continue_notice,
            continue_text,
            cannon_clips,
            cannon_cuts,
            cannon_texture,
            range_cuts,
            range_texture,
            castle_slot: config.environment.castle_slot,
            orb_icons,
            sniper_cuts,
            sniper_textures,
            top_cuts,
            top_textures,
            title_draw,
        };
        Ok((Prepared {
            scene,
            data,
            config,
            profiles,
            rows,
            hint_candidates: candidates,
            hint_lengths: lengths,
            reward_rules,
            continue_policy,
        }, receipt))
    }
    pub fn draw(
        &mut self,
        input: &crate::scene::Input,
        combo_frame: i32,
        health: Option<&battle::Hud>,
        ranges: &mut ActorDrawRanges,
    ) -> Result<crate::scene::Frame<'_>> {
        let intro = self.combo_layout(combo_frame, input.viewport_width)?;
        let visuals = native(self.core.visuals())?.to_vec();
        let (actors, _) = native(self.core.actors())?;
        let references = native(self.core.active_actors())?;
        let mut frame = self
            .scene
            .draw_with_castle_state(input, actors[0][0].words[1])
            .context("戦闘背景の描画")?;
        let mut order = Vec::new();
        for side in [1, 0] {
            order.extend(
                references
                    .iter()
                    .filter(|value| value.side == side && value.slot > 0),
            );
        }
        // 原本の選択ソートを維持し、同じレイヤーの順序を変えない。
        for i in 0..order.len() {
            let mut first = i;
            for j in i + 1..order.len() {
                if order[j].actor.words[5] < order[first].actor.words[5] {
                    first = j;
                }
            }
            order.swap(i, first);
        }
        let mut commands = Vec::new();
        commands.extend(native(self.core.cannon_range_draw(
            &frame.layout,
            &self.data.range_cuts,
            self.data.range_texture,
        ))?);
        for value in order {
            let (side, slot) = (value.side, value.slot);
            let start = commands.len();
            let words = &value.actor.words;
            let model = self.data
                .models
                .get(value.profile as usize)
                .context("個体モデルなし")?;
            let action = words[1];
            let clip = match action {
                0 | 7 => Some(0),
                1 | 16 | 18 | 20 => Some(1),
                2 => Some(2),
                3 | 5 | 6 | 17 => Some(3),
                10 => Some(7),
                11 => Some(4),
                12 => Some(5),
                13 => Some(6),
                4 => Some(8),
                _ => None,
            };
            let bone = visuals
                .iter()
                .find(|v| v.kind == 12 && v.side == side as i32 && v.slot == slot as i32);
            let asset = if let Some(bone) = bone {
                Some(
                    self.data.effects
                        .get(&(6, 0, bone.phase))
                        .context("蘇生待ちの骨モデルなし")?,
                )
            } else {
                clip.and_then(|clip| model.clips.get(&clip))
            };
            // 蘇生待ち14も共通の骨を描き、所有する二次演出の走査を継続する。
            if let Some(asset) = asset {
                if matches!(action, 18 | 20) {
                    let warp = self.data
                        .effects
                        .get(&(6, 0, if action == 18 { 0x2c08 } else { 0x2c40 }))
                        .context("ワープ制御モデルなし")?;
                    paint_warp(
                        &mut commands,
                        asset,
                        warp,
                        &frame.layout,
                        words[2],
                        [words[3] / 10, words[4] / 10 + words[5] * 4],
                        side == 0,
                    )?;
                } else {
                    paint_clip(
                        &mut self.poses,
                        &mut commands,
                        asset,
                        &frame.layout,
                        if action == 7 && bone.is_none() {
                            0
                        } else {
                            words[2]
                        },
                        f64::from(words[3] / 10),
                        f64::from(words[4] / 10 + words[5] * 4),
                        bone.is_none(),
                    )
                    .with_context(|| {
                        format!(
                            "{}: side={side}, slot={slot}, action={action}, frame={}",
                            model.name, words[2]
                        )
                    })?;
                }
            } else if let Some(clip) = clip
                && action != 4
                && action != 10
            {
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
                    &mut self.poses,
                    &mut commands,
                    entry,
                    &frame.layout,
                    words[2],
                    f64::from(words[3] / 10 + point[0]),
                    f64::from(words[4] / 10 + words[5] * 4),
                    false,
                )?;
            }
            if action == 4
                && let Some(soul) = model.clips.get(&9)
            {
                paint_clip(
                    &mut self.poses,
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
            if ranges.focus == Some((side, slot)) && commands.len() > start {
                ranges.preview = Some([start, commands.len()]);
            }
            for value in visuals
                .iter()
                .filter(belonging)
                .filter(|v| v.kind == 13)
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 11))
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 10))
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 7))
                .chain(
                    visuals
                        .iter()
                        .filter(belonging)
                        .filter(|v| (0..=3).contains(&v.kind)),
                )
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 9))
                .chain(visuals.iter().filter(belonging).filter(|v| v.kind == 4))
            {
                let asset = self.data
                    .effects
                    .get(&(
                        if matches!(value.kind, 7 | 9 | 10 | 11 | 13) {
                            6
                        } else {
                            value.kind
                        },
                        if matches!(value.kind, 7 | 9 | 10 | 11 | 13) {
                            0
                        } else {
                            value.side
                        },
                        value.phase,
                    ))
                    .context("効果描画モデルなし")?;
                let offset = if value.kind == 11 && side == 0 {
                    let idle = &model
                        .clips
                        .get(&1)
                        .context("ワープ中の待機モデルなし")?
                        .model;
                    native(idle.native_point(words[2], 1))?[0]
                        - native(idle.native_point(words[2], 0))?[0]
                } else {
                    0
                };
                paint_clip(
                    &mut self.poses,
                    &mut commands,
                    asset,
                    &frame.layout,
                    value.frame,
                    f64::from(value.x + offset),
                    f64::from(value.y),
                    false,
                )?;
            }
        }
        commands.extend(native(self.core.sniper_draw(
            &frame.layout,
            [&self.data.sniper_cuts[0], &self.data.sniper_cuts[1]],
            self.data.sniper_textures,
        ))?);
        commands.extend(native(self.core.hit_draw(
            &frame.layout,
            &self.data.sniper_cuts[1],
            self.data.sniper_textures[1],
        ))?);
        for value in visuals.iter().filter(|v| v.kind == 6) {
            let asset = self.data
                .effects
                .get(&(6, 0, value.phase))
                .context("共通演出モデルなし")?;
            paint_clip(
                &mut self.poses,
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
                &self.data.cannon_cuts,
                self.data.cannon_texture,
            ))?);
        }
        for value in visuals.iter().filter(|v| v.kind == 5) {
            if let Some(asset) = self.data.cannon_clips.get(&value.phase) {
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
            let asset = self.data
                .effects
                .get(&(6, 0, value.phase))
                .context("ボス演出モデルなし")?;
            paint_clip(
                &mut self.poses,
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
        if let Some(preview) = &mut ranges.preview {
            *preview = preview.map(|index| index + at);
        }
        frame.commands.splice(at..at, commands);
        // 16.0.3の0070af68〜0070b4b4。城体力をステージ名・上部表示より先に合成する。
        if let Some(hud) = health {
            draw_castle_health(
                &mut frame.commands,
                hud,
                self.data.castle_slot > 0,
                &self.data.top_cuts[0],
                self.data.top_textures[0],
            )?;
        }
        frame.commands.extend(native(self.core.top_draw(
            &self.data.top_cuts[0],
            &self.data.top_cuts[1],
            self.data.top_textures,
            self.data.title_draw,
            input.safe_left,
        ))?);
        if intro.index >= 0 {
            // 007082e8から呼ばれる005fb4e8の乗算帯を残り時間の後に合成する。
            let [x, y, w, h] = intro.band.map(f64::from);
            frame.commands.push(render::Command {
                texture: -2,
                layer: 11,
                count: 4,
                blend: 2,
                opacity: 1.,
                points: [
                    x,
                    y,
                    x,
                    y + h,
                    x + w,
                    y + h,
                    x + w,
                    y,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                    0.,
                ],
                colors: [40, 40, 77, 0, 0, 0],
                ..Default::default()
            });
        }
        frame.animated = true;
        Ok(frame)
    }
    #[cfg(not(target_os = "emscripten"))]
    pub fn settle(&mut self, receipt: &mut crate::battle_rewards::Receipt) -> Result<()> {
        let outcome = native(self.core.outcome())?;
        if let Some((_, insufficient)) = &self.data.continue_text
            && outcome.mode == 2
        {
            match native(self.core.ending())?.phase {
                0..=2 => return Ok(()),
                3 => {
                    let pending = native(self.core.continue_view())?.pending != 0;
                    if pending {
                        let payment = receipt.spend_continue_cat_food();
                        let paid = payment.as_ref().is_ok_and(|&paid| paid);
                        // Sessionのロック内で、受理待ちの1操作につき一度だけ支払う。
                        native(self.core.continue_payment(paid))?;
                        self.continue_error = match payment {
                            Ok(true) => None,
                            Ok(false) => Some(insufficient.clone()),
                            Err(error) => {
                                Some(format!("ネコカンを消費できませんでした。{error:#}"))
                            }
                        };
                    }
                    if pending || (self.continue_balance.is_none() && self.continue_error.is_none())
                    {
                        match receipt.cat_food_display() {
                            Ok(balance) => self.continue_balance = Some(balance),
                            Err(error) => {
                                self.continue_error.get_or_insert_with(|| {
                                    format!("ネコカンの所持数を読み込めませんでした。{error:#}")
                                });
                            }
                        }
                    }
                    return Ok(());
                }
                _ => {}
            }
        }
        self.continue_balance = None;
        self.continue_error = None;
        // 保存側へは戦闘ハンドルを渡さず、確定した数値だけを渡す。
        let saved = receipt.settle(&outcome, || native(self.core.rewards()));
        if saved
            && let Some(notifications) = receipt
                .saved
                .as_ref()
                .and_then(|saved| saved["notifications"].as_array())
            && !notifications.is_empty()
        {
            native(self.core.notifications(notifications.len() as i32))?;
        }
        if saved {
            self.saved.clone_from(&receipt.saved);
        }
        if self.receipt_error != receipt.error {
            self.receipt_error.clone_from(&receipt.error);
        }
        Ok(())
    }
    pub fn ending_camera(&mut self, input: &mut crate::scene::Input) -> Result<()> {
        let camera = native(self.core.end_camera())?;
        let continues = native(self.core.continue_view())?.resumes;
        if continues != self.continues_on_camera {
            self.continues_on_camera = continues;
            self.ending_camera_applied = false;
        }
        let limits = native(self.core.camera_limits())?;
        input.battle_slide = limits.slide;
        input.battle_rows = limits.rows;
        let moving = limits.automatic;
        if camera.width > 0 && (!self.ending_camera_applied || moving) {
            self.ending_camera_applied = !moving;
            input.zoom = f64::from(camera.zoom) / 10000.;
            input.center = Some(f64::from(camera.left) / 10. + 480. / input.zoom);
            input.focus = 4;
        }
        Ok(())
    }
    pub fn stats(&self, compact: bool) -> Result<Value> {
        let references = native(self.core.active_actors())?;
        let (production, seed) = native(self.core.production())?;
        let count = |side: usize| {
            references
                .iter()
                .filter(|value| value.side == side && value.slot > 0)
                .count()
        };
        let hint = native(self.core.hint())?;
        let hint_lines = self.data.defeat_hints.get(hint.id as usize);
        let ending = native(self.core.ending())?;
        let camera_limits = native(self.core.camera_limits())?;
        let boss_line = native(self.core.defeat_boss_hp())?
            .map(|hp| {
                self.data.boss_hp.as_deref()
                    .context("ボス残り体力の原本文面がありません")
                    .map(|label| format!("{label}{hp}%"))
            })
            .transpose()?;
        let continue_prompt = if ending.phase == 3
            && let Some((lines, _)) = &self.data.continue_text
            && native(self.core.outcome())?.mode == 2
        {
            let mut lines = lines.clone();
            if let Some(boss) = &boss_line
                && let Some(last_line) = lines.last_mut()
            {
                last_line.push_str(&format!("({boss})"));
            }
            json!({"layout":native(self.core.continue_view())?,"cost":CONTINUE_COST,"balance":self.continue_balance,"error":self.continue_error,"lines":lines})
        } else {
            Value::Null
        };
        let mut view = json!({
            "defeatHint": {"layout":hint,"lines":hint_lines},
            "ex": native(self.core.ex())?,
            "endingHudSlide": camera_limits.slide,
            "endCameraActive": camera_limits.automatic,
            "cameraMaximum": camera_limits.maximum,
            "music": native(self.core.music())?,
            "ending": ending,
            "endingMap": native(self.core.ending_map())?,
            "continuePrompt": continue_prompt,
            "continueNotice": self.data.continue_notice,
            "defeatBossHp": boss_line,
            "receipt": self.saved,
            "receiptError": self.receipt_error,
            "units": count(0),
            "enemies": count(1),
            "precision": self.data.precision,
            "wait": production.wait,
            "costs": native(self.core.prices())?,
            "extras": native(self.core.extras())?,
            "points": native(self.core.points())?,
            "sounds": native(self.core.sounds())?,
            "result": native(self.core.outcome())?,
            "deployment": native(self.core.deployment())?,
            "rules": self.rules,
        });
        if !compact {
            let (actors, _) = native(self.core.actors())?;
            let units: Vec<_> = references.iter().filter(|value|value.slot > 0).map(|value| {
                let a = &value.actor.words;
                json!({"side":value.side,"slot":value.slot,"profile":value.profile,"raw":a[0],"layer":a[5],"frame":a[2],"action":a[1],"hp":a[8],"maximum":a[7],"x":a[3],"y":a[4],"serial":a[240]})
            }).collect();
            let diagnostic = json!({
                "endCamera":native(self.core.end_camera())?, "noContinue":self.data.continue_notice.is_some(),
                "rewardRolls":native(self.core.rewards())?, "castleHp":[actors[0][0].words[8], actors[1][0].words[8]],
                "maximum":production.maximum, "produced":production.produced, "lastCosts":production.last_cost,
                "seed":seed, "actors":units, "cannon":[actors[0][0].words[9], actors[0][0].words[10], actors[0][0].words[13]],
                "sniper":native(self.core.sniper_status())?, "computer":native(self.core.computer())?,
            });
            if let Value::Object(fields) = diagnostic {
                view.as_object_mut()
                    .expect("戦闘表示オブジェクト")
                    .extend(fields);
            }
        }
        Ok(view)
    }
    pub fn layout(&self, input: &crate::scene::Input) -> Result<render::Layout> {
        native(render::battle_layout(
            &render::SceneInput {
                width: input.width,
                center: input.center.unwrap_or(input.width),
                zoom: input.zoom,
                cut_height: 510,
                castle: self.scene.castle_geometry(),
                focus: input.focus,
                viewport_width: input.viewport_width,
                battle_rows: input.battle_rows,
            },
            input.battle_slide,
        ))
    }
    pub fn combo_intro(&self, frame: i32, width: i32) -> Result<Value> {
        let layout = self.combo_layout(frame, width)?;
        let combo = usize::try_from(layout.index)
            .ok()
            .and_then(|index| self.data.combos.get(index));
        Ok(json!({"layout":layout,"combo":combo}))
    }
    fn combo_layout(&self, frame: i32, width: i32) -> Result<kbcs_bridge::interface::ComboIntro> {
        let groups = self.data
            .combos
            .iter()
            .map(|combo| i32::try_from(combo["group"].as_i64().unwrap_or_default()))
            .collect::<Result<Vec<_>, _>>()?;
        let count = if self.combo_skipped || native(self.core.outcome())?.mode != 0 {
            &[][..]
        } else {
            &groups[..]
        };
        native(kbcs_bridge::interface::combo_intro(
            frame,
            if width == 0 { 960 } else { width },
            count,
        ))
    }
    pub fn hud(&self, layout: &render::Layout) -> Result<(battle::Hud, Value)> {
        let (actors, profiles) = native(self.core.actors())?;
        let point = usize::try_from(self.data.castle_slot)
            .ok()
            .filter(|&slot| slot > 0 && slot < 51)
            .and_then(|slot| {
                self.data.models
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
        let hud = native(self.core.hud(layout, point))?;
        let mut value = serde_json::to_value(&hud)?;
        if self.data.castle_slot > 0 {
            value["specialEnemyCastle"] = json!(true);
        }
        value["warning"] = json!(native(self.core.warning())?);
        if self.data.orb_icons.iter().any(|icons| !icons.is_empty()) {
            let masks = native(self.core.orb_visibility())?;
            let visible = self.data.orb_icons.iter().zip(masks).map(|(icons, mask)| {
                icons.iter().enumerate().filter_map(move |(index, icon)| {
                    (mask & (1 << index) != 0).then_some(icon)
                }).collect::<Vec<_>>()
            }).collect::<Vec<_>>();
            value["orbIcons"] = json!(visible);
        }
        Ok((hud, value))
    }
}

fn draw_castle_health(
    commands: &mut Vec<render::Command>,
    hud: &battle::Hud,
    special_enemy: bool,
    cuts: &[render::Cut],
    texture: i32,
) -> Result<()> {
    let cut = |id| cuts.get(id).context("城体力の分割定義がありません");
    let digits = |value: i32| {
        value
            .max(0)
            .to_string()
            .bytes()
            .map(|digit| 57 + usize::from(digit - b'0'))
            .collect::<Vec<_>>()
    };
    let scale = hud.scale;
    for (side, (&[anchor, y], &[hp, maximum, unknown])) in
        hud.anchors.iter().zip(&hud.health).enumerate()
    {
        let (numerator, denominator) = if unknown != 0 {
            (vec![108; 7], vec![108; 7])
        } else {
            (digits(hp), digits(maximum))
        };
        let mut slash = anchor;
        if side == 1 && special_enemy {
            let digit = cut(if unknown != 0 { 108 } else { 57 })?;
            slash += denominator.len() as f64 * f64::from(digit.width) * scale;
        }
        let mut glyph = |id, x, width, height| -> Result<()> {
            let &render::Cut {
                x: sx,
                y: sy,
                width: sw,
                height: sh,
            } = cut(id)?;
            let mut command = render::Command {
                texture,
                layer: 10,
                count: 4,
                opacity: 1.,
                cut: [sx, sy, sw, sh],
                ..Default::default()
            };
            command.points[..8].copy_from_slice(&[x, y, x, y + height, x + width, y + height, x + width, y]);
            commands.push(command);
            Ok(())
        };
        let mut x = slash;
        for &id in numerator.iter().rev() {
            let part = cut(id)?;
            let width = f64::from(part.width) * scale;
            x -= width;
            glyph(id, x, width, f64::from(part.height) * scale)?;
        }
        x = slash + 18. * scale;
        for id in denominator {
            let part = cut(id)?;
            let width = f64::from(part.width) * scale;
            glyph(id, x, width, f64::from(part.height) * scale)?;
            x += width;
        }
        glyph(67, slash, 18. * scale, 18. * scale)?;
    }
    Ok(())
}

type PoseKey = (usize, i32, bool);

#[derive(Default)]
struct PoseCache {
    packets: HashMap<PoseKey, Vec<render::Packet>>,
    order: VecDeque<PoseKey>,
    bytes: usize,
}

#[allow(clippy::too_many_arguments)]
fn paint_clip(
    cache: &mut PoseCache,
    commands: &mut Vec<render::Command>,
    asset: &Clip,
    layout: &render::Layout,
    frame: i32,
    x: f64,
    y: f64,
    anchor: bool,
) -> Result<()> {
    const LIMIT: usize = 4 * 1024 * 1024;
    // モデルは戦闘開始後に入れ替えない。位置・ズームはキャッシュ後に適用する。
    let key = (std::ptr::from_ref(asset) as usize, frame, anchor);
    if let Some(local) = cache.packets.get(&key) {
        return paint_packets(commands, asset, layout, local, x, y);
    }
    let local = if anchor {
        native(asset.model.pose_config(frame, 0, 1))?
    } else {
        native(asset.model.pose(frame, false, false, 1))?
    };
    paint_packets(commands, asset, layout, &local, x, y)?;
    let size = local.capacity() * size_of::<render::Packet>();
    if size <= LIMIT {
        while cache.order.len() >= 1024 || cache.bytes + size > LIMIT {
            if let Some(oldest) = cache.order.pop_front()
                && let Some(value) = cache.packets.remove(&oldest)
            {
                cache.bytes -= value.capacity() * size_of::<render::Packet>();
            }
        }
        cache.bytes += size;
        cache.order.push_back(key);
        cache.packets.insert(key, local);
    }
    Ok(())
}
fn paint_warp(
    commands: &mut Vec<render::Command>,
    asset: &Clip,
    warp: &Clip,
    layout: &render::Layout,
    frame: i32,
    origin: [i32; 2],
    unit: bool,
) -> Result<()> {
    let shape = native(warp.model.warp_pose(frame))?;
    if shape.alpha <= 0 {
        return Ok(());
    }
    let base = native(asset.model.native_point(frame, 0))?;
    let pivot = native(asset.model.native_point(frame, usize::from(unit)))?;
    let raw = native(asset.model.pose(frame, false, false, 1))?;
    let packets = native(render::warp_packets(
        &shape,
        [base[0], base[1], pivot[0], pivot[1]],
        origin,
        &raw,
    ))?;
    paint_packets(commands, asset, layout, &packets, 0., 0.)
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

#[cfg(test)]
mod tests {
    #[test]
    fn sortie_speed_overrides_stale_battle_inputs() {
        use super::{battle_screen, json, set_sortie_speed};

        for (equipped, speed, expected) in [
            (None, 3, (8, 2, 0)),
            (Some(false), 3, (8, 2, 0)),
            (Some(true), 2, (9, 2, 1)),
            (Some(true), 3, (9, 3, 2)),
        ] {
            let mut screen = battle_screen::Config {
                items: 9,
                speed: 3,
                ..Default::default()
            };
            let mut state = battle_screen::State {
                items_on: 9,
                speed_mode: 2,
                ..Default::default()
            };
            let items = equipped.map_or_else(|| json!({}), |value| json!({"speedup":value}));
            set_sortie_speed(
                &json!({"items":items,"speed":speed}),
                &mut screen,
                &mut state,
            );
            assert_eq!(screen.items, 9);
            assert_eq!((state.items_on, screen.speed, state.speed_mode), expected);
        }
    }

    #[test]
    fn native_effect_bindings() {
        let fixture: serde_json::Value = serde_json::from_str(
            include_str!("../../../native/kbcs-core/tests/effect-state-vectors.json")
                .trim_start_matches('\u{feff}'),
        )
        .unwrap();
        let input = super::inputs().unwrap();
        for (phase, path) in fixture["bindings"].as_object().unwrap() {
            assert_eq!(&input["clocks"][phase]["path"], path);
        }
    }
}
