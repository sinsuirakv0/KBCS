use crate::cache::Cache;
use anyhow::{Context, Result, ensure};
use include_dir::{Dir, include_dir};
use kbcs_data::{import, store::Database};
use serde_json::{Value, json};
use std::{
    collections::BTreeMap,
    path::PathBuf,
    sync::{
        Arc, Mutex, Weak,
        atomic::{AtomicBool, Ordering},
    },
};

static UI: Dir<'_> = include_dir!("$CARGO_MANIFEST_DIR/../../ui");

pub struct Reply {
    pub status: u16,
    pub mime: &'static str,
    pub bytes: Vec<u8>,
}
impl Reply {
    fn battle(
        mut frame: BattleFrame<'_>,
        packed: Option<(std::time::Instant, bool)>,
    ) -> Result<Self> {
        if let Some((started, compressed)) = packed {
            let commands = frame
                .scene
                .as_mut()
                .map(|scene| std::mem::take(&mut scene.commands))
                .unwrap_or_default();
            return Ok(Self {
                status: 200,
                mime: "application/x-kbcs-battle-frame",
                bytes: crate::battle_wire::encode(&frame, &commands, started, compressed)?,
            });
        }
        Self::serialized(&frame)
    }
    fn serialized(value: &impl serde::Serialize) -> Result<Self> {
        Ok(Self {
            status: 200,
            mime: "application/json; charset=utf-8",
            bytes: serde_json::to_vec(value)?,
        })
    }
    pub fn overloaded() -> Self {
        Self {
            status: 503,
            mime: "application/json",
            bytes: br#"{"error":"Requests are busy; retry shortly"}"#.to_vec(),
        }
    }
    fn json(value: Value) -> Self {
        Self {
            status: 200,
            mime: "application/json; charset=utf-8",
            bytes: serde_json::to_vec(&value).unwrap_or_default(),
        }
    }
    fn error(error: anyhow::Error) -> Self {
        let mut reply = Self::json(json!({"error":format!("{error:#}")}));
        reply.status = 400;
        reply
    }
}

#[derive(Default)]
struct Progress {
    message: String,
    error: Option<String>,
}

#[derive(Clone)]
pub struct Service {
    pub root: PathBuf,
    pub region: String,
    source: String,
    busy: Arc<AtomicBool>,
    progress: Arc<Mutex<Progress>>,
    catalog: Arc<Mutex<CatalogCache>>,
    scenes: Arc<Mutex<Cache<SceneSlot>>>,
    audio: Arc<Mutex<BTreeMap<i64, Weak<Mutex<()>>>>>,
    poses: Arc<Mutex<Cache<ModelSlot>>>,
    battles: Arc<Mutex<BTreeMap<String, BattleSlot>>>,
    pub persist_rewards: bool,
    pub workers: Arc<crate::workers::Workers>,
    runtime: Arc<Mutex<crate::runtime::Monitor>>,
}

type CatalogCache = Cache<(PathBuf, Vec<u8>)>;
type SceneSlot = Slot<(Database, crate::scene::Scene)>;
type ModelSlot = Slot<Arc<kbcs_bridge::render::Model>>;
type BattleSlot = Arc<Mutex<crate::battle::Session>>;

#[derive(serde::Deserialize)]
#[serde(deny_unknown_fields)]
struct BattleRequest {
    battle: kbcs_bridge::battle_screen::Request,
    scene: Option<crate::scene::Input>,
    #[serde(default)]
    cached: bool,
    #[serde(default)]
    packed: bool,
    #[serde(default)]
    compressed: bool,
}
struct BattleResult<'a> {
    frame: &'a kbcs_bridge::battle_screen::Frame,
    core_ms: f64,
    packed: Option<(std::time::Instant, bool)>,
}
#[derive(serde::Serialize)]
struct BattleFrame<'a> {
    #[serde(flatten)]
    battle: &'a kbcs_bridge::battle_screen::Frame,
    scene: Option<crate::scene::Frame<'a>>,
    #[serde(rename = "coreMs")]
    core_ms: f64,
    #[serde(skip_serializing_if = "Option::is_none")]
    runtime: Option<Value>,
}

type Slot<T> = Arc<Mutex<Option<T>>>;
fn cache_slot<T>(cache: &Mutex<Cache<Slot<T>>>, key: String) -> Result<Slot<T>> {
    let mut cache = cache
        .lock()
        .map_err(|_| anyhow::anyhow!("キャッシュのロック失敗"))?;
    if let Some(slot) = cache.get(&key) {
        return Ok(slot.clone());
    }
    let slot = Arc::new(Mutex::new(None));
    cache.insert(key, slot.clone(), 0);
    Ok(slot)
}
pub fn dispatch(service: &Service, path: &str, job: impl FnOnce(Service, bool) + Send + 'static) {
    let workers = service.workers.clone();
    let service = service.clone();
    workers.submit(path, move |accepted| job(service, accepted));
}

impl Service {
    pub fn new(root: PathBuf, region: String, source: String) -> Self {
        Self {
            root,
            region,
            source,
            busy: Arc::new(AtomicBool::new(false)),
            progress: Arc::new(Mutex::new(Progress::default())),
            catalog: Arc::new(Mutex::new(Cache::new(128, 128 * 1024 * 1024))),
            scenes: Arc::new(Mutex::new(Cache::new(16, usize::MAX))),
            audio: Arc::new(Mutex::new(BTreeMap::new())),
            poses: Arc::new(Mutex::new(Cache::new(64, usize::MAX))),
            battles: Arc::new(Mutex::new(BTreeMap::new())),
            persist_rewards: true,
            workers: Arc::new(crate::workers::Workers::new()),
            runtime: Arc::new(Mutex::new(crate::runtime::Monitor::default())),
        }
    }

    pub fn handle(&self, method: &str, path: &str, body: &[u8]) -> Reply {
        match self.route(method, path, body) {
            Ok(reply) => reply,
            Err(error) => Reply::error(error),
        }
    }

    fn scene_reply(
        &self,
        input: &crate::scene::Input,
        battle: Option<BattleResult<'_>>,
    ) -> Result<Reply> {
        let current = kbcs_data::store::current_path(&self.root, &self.region)?;
        let key = format!("{}:{}", current.display(), input.key());
        let slot = cache_slot(&self.scenes, key)?;
        let mut cached = slot
            .lock()
            .map_err(|_| anyhow::anyhow!("描画状態のロック失敗"))?;
        if cached.is_none() {
            // 同じsnapshotの読取専用接続はシーンと共用し、毎F開き直さない。
            let database = Database::open_path(&current)?;
            let scene = crate::scene::Scene::new(&database, input)?;
            *cached = Some((database, scene));
        }
        let (database, scene) = cached.as_mut().unwrap();
        let reply = scene.draw(database, input).and_then(|frame| match battle {
            Some(battle) => Reply::battle(
                BattleFrame {
                    battle: battle.frame,
                    scene: Some(frame),
                    core_ms: battle.core_ms,
                    runtime: None,
                },
                battle.packed,
            ),
            None => Reply::serialized(&frame),
        });
        if reply.is_err() {
            *cached = None;
        }
        reply
    }

    fn route(&self, method: &str, path: &str, body: &[u8]) -> Result<Reply> {
        let url = url::Url::parse(&format!("http://kbcs.localhost{path}"))?;
        let path = url.path();
        if path == "/api/runtime" {
            let mut value = self
                .runtime
                .lock()
                .map_err(|_| anyhow::anyhow!("計測のロック失敗"))?
                .sample();
            value["workers"] = self.workers.summary();
            value["caches"] = json!({"scene":self.scenes.lock().unwrap().summary(),"model":self.poses.lock().unwrap().summary(),"catalog":self.catalog.lock().unwrap().summary()});
            return Ok(Reply::json(value));
        }
        if path == "/api/battle-options" {
            ensure!(
                method == "GET" || method == "PUT",
                "戦闘設定の操作が不正です"
            );
            ensure!(body.len() <= 1024, "戦闘設定が大きすぎます");
            let update = if method == "PUT" {
                Some(serde_json::from_slice(body)?)
            } else {
                None
            };
            return Reply::serialized(&kbcs_data::battle_options::access(&self.root, update)?);
        }
        if path == "/api/inventory" {
            ensure!(method == "GET" || method == "PUT", "持ち物の操作が不正です");
            ensure!(body.len() <= 1024, "持ち物の入力が大きすぎます");
            let store = kbcs_data::inventory::Store::open(&self.root)?;
            if method == "PUT" {
                store.update_display(&serde_json::from_slice(body)?)?;
            }
            return Ok(Reply::json(
                json!({"items":store.items()?,"characters":store.characters()?}),
            ));
        }
        if path == "/api/battle-popup" {
            ensure!(
                method == "POST" && body.len() <= 16384,
                "通知配置の入力が不正です"
            );
            let inputs: Vec<kbcs_bridge::battle::PopupInput> = serde_json::from_slice(body)?;
            ensure!(inputs.len() <= 5, "通知配置が多すぎます");
            let values = inputs
                .iter()
                .map(|input| {
                    kbcs_bridge::battle::popup_layout(input)
                        .map_err(|c| anyhow::anyhow!("通知配置: {c}"))
                })
                .collect::<Result<Vec<_>>>()?;
            return Reply::serialized(&values);
        }
        if path == "/api/inventory/catalog" {
            ensure!(method == "GET", "持ち物の操作が不正です");
            return Ok(Reply::json(kbcs_data::inventory::catalog(
                &Database::open(&self.root, &self.region)?,
            )?));
        }
        if path == "/api/battle-session" {
            if method == "DELETE" {
                let id = url
                    .query_pairs()
                    .find(|(key, _)| key == "session")
                    .context("戦闘IDなし")?
                    .1
                    .into_owned();
                self.battles
                    .lock()
                    .map_err(|_| anyhow::anyhow!("戦闘ロック失敗"))?
                    .remove(&id);
                return Ok(Reply::json(json!({"closed":true})));
            }
            ensure!(
                method == "POST" && body.len() <= 1_000_000,
                "戦闘開始入力が不正です"
            );
            let request: crate::battle::Start = serde_json::from_slice(body)?;
            let id = request.scene.session.clone();
            ensure!(!id.is_empty() && id.len() <= 128, "戦闘ID不正");
            let session = crate::battle::Session::new(
                &self.root,
                &self.region,
                request,
                self.persist_rewards,
            )?;
            let stats = session.stats()?;
            let textures = session.scene.textures().to_vec();
            let title = session.title.clone();
            let mut battles = self
                .battles
                .lock()
                .map_err(|_| anyhow::anyhow!("戦闘ロック失敗"))?;
            ensure!(
                battles.len() < 8 && !battles.contains_key(&id),
                "戦闘を閉じてから開始してください"
            );
            battles.insert(id.clone(), Arc::new(Mutex::new(session)));
            return Ok(Reply::json(
                json!({"session":id,"runtime":stats,"textures":textures,"title":title}),
            ));
        }
        if path == "/api/battle-session/frame" {
            let started = std::time::Instant::now();
            ensure!(
                method == "POST" && body.len() <= 32768,
                "戦闘入力が不正です"
            );
            let mut request: crate::battle::Request = serde_json::from_slice(body)?;
            let session = self
                .battles
                .lock()
                .map_err(|_| anyhow::anyhow!("戦闘ロック失敗"))?
                .get(&request.session)
                .cloned()
                .context("戦闘が終了しています")?;
            let mut session = session
                .lock()
                .map_err(|_| anyhow::anyhow!("戦闘更新ロック失敗"))?;
            ensure!(
                request.scene.key() == session.key,
                "戦闘中のステージ変更はできません"
            );
            session
                .core
                .viewport(request.scene.viewport_width)
                .map_err(|code| anyhow::anyhow!("画面幅: {code}"))?;
            session.ending_camera(&mut request.scene)?;
            let camera = session.layout(&request.scene)?;
            session
                .core
                .camera(&camera)
                .map_err(|code| anyhow::anyhow!("戦闘カメラ: {code}"))?;
            let battle = session.core.advance(&request.input).map_err(|code| {
                anyhow::anyhow!(
                    "戦闘更新: {code} / frame,phase,side,slot={:?}",
                    session.core.diagnostic()
                )
            })?;
            let core_ms = started.elapsed().as_secs_f64() * 1000.;
            session.settle()?;
            let mut runtime = session.stats()?;
            if request.debug {
                let (actors, _) = session
                    .core
                    .actors()
                    .map_err(|code| anyhow::anyhow!("個体読取: {code}"))?;
                runtime["words"] = json!(
                    actors
                        .iter()
                        .map(|side| side
                            .iter()
                            .map(|actor| actor.words.as_slice())
                            .collect::<Vec<_>>())
                        .collect::<Vec<_>>()
                );
            }
            if request.debug {
                runtime["visuals"] = serde_json::to_value(
                    session
                        .core
                        .visuals()
                        .map_err(|code| anyhow::anyhow!("効果読取: {code}"))?,
                )?;
            }
            request.scene.frame = battle.state.frame;
            request.scene.battle_rows = battle.state.rows;
            session.ending_camera(&mut request.scene)?;
            // 描画がSceneを借用する前に、同じ配置でHUDを作る。
            let hud_layout = session.layout(&request.scene)?;
            runtime["hud"] = serde_json::to_value(session.hud(&hud_layout)?)?;
            let frame = session.draw(&request.scene)?;
            return Reply::battle(
                BattleFrame {
                    battle: &battle,
                    scene: Some(frame),
                    core_ms,
                    runtime: Some(runtime),
                },
                request.packed.then_some((started, request.compressed)),
            );
        }
        if path == "/api/battle-screen" {
            ensure!(
                method == "POST" && body.len() <= 16384,
                "戦闘画面の入力が不正です"
            );
            let request: kbcs_bridge::battle_screen::Request = serde_json::from_slice(body)?;
            let result = kbcs_bridge::battle_screen::frame(&request)
                .map_err(|code| anyhow::anyhow!("戦闘画面の入力・計算エラー: {code}"))?;
            return Reply::serialized(&result);
        }
        if path == "/api/battle-frame" {
            let request_started = std::time::Instant::now();
            ensure!(
                method == "POST" && body.len() <= 32768,
                "戦闘フレームの入力が不正です"
            );
            let mut request: BattleRequest = serde_json::from_slice(body)?;
            let started = std::time::Instant::now();
            let battle = kbcs_bridge::battle_screen::frame(&request.battle)
                .map_err(|code| anyhow::anyhow!("戦闘画面の入力・計算エラー: {code}"))?;
            let core_ms = started.elapsed().as_secs_f64() * 1000.;
            if request.cached && battle.state.rows == request.battle.state.rows {
                request.scene = None;
            }
            if let Some(scene) = &mut request.scene {
                // 確定した論理F・段数を描く。未来の背景を先読みして乱数を進めない。
                scene.frame = battle.state.frame;
                scene.battle_rows = battle.state.rows;
                scene.viewport_width = request.battle.config.viewport_width;
                return self.scene_reply(
                    scene,
                    Some(BattleResult {
                        frame: &battle,
                        core_ms,
                        packed: request
                            .packed
                            .then_some((request_started, request.compressed)),
                    }),
                );
            }
            return Reply::battle(
                BattleFrame {
                    battle: &battle,
                    scene: None,
                    core_ms,
                    runtime: None,
                },
                request
                    .packed
                    .then_some((request_started, request.compressed)),
            );
        }
        if path == "/api/battle-support" {
            ensure!(
                method == "POST" && body.len() <= 4096,
                "戦闘補助の入力が不正です"
            );
            let input: kbcs_bridge::battle_support::CastleInput = serde_json::from_slice(body)?;
            let result = kbcs_bridge::battle_support::castle(&input)
                .map_err(|code| anyhow::anyhow!("城体力の入力・計算エラー: {code}"))?;
            return Ok(Reply::json(serde_json::to_value(result)?));
        }
        if path == "/api/deployment" {
            ensure!(
                method == "POST" && body.len() <= 65536,
                "出撃制限の入力が不正です"
            );
            #[derive(serde::Deserialize)]
            #[serde(deny_unknown_fields)]
            struct DeploymentRequest {
                costs: Vec<kbcs_bridge::battle_support::DeployCostInput>,
                checks: Vec<kbcs_bridge::battle_support::DeploymentInput>,
            }
            let input: DeploymentRequest = serde_json::from_slice(body)?;
            ensure!(
                input.costs.len() <= 10 && input.checks.len() <= 20,
                "出撃制限の件数が不正です"
            );
            let costs = input
                .costs
                .iter()
                .map(kbcs_bridge::battle_support::deploy_cost)
                .collect::<Result<Vec<_>, _>>()
                .map_err(|code| anyhow::anyhow!("生産コストの入力エラー: {code}"))?;
            let checks = input
                .checks
                .iter()
                .map(|check| {
                    let mut check = check.clone();
                    check.cost = *costs
                        .get(check.slot as usize)
                        .context("出撃枠のコストがありません")?;
                    kbcs_bridge::battle_support::deployment(&check)
                        .map_err(|code| anyhow::anyhow!("出撃制限の入力エラー: {code}"))
                })
                .collect::<Result<Vec<_>>>()?;
            return Ok(Reply::json(json!({"costs":costs,"checks":checks})));
        }
        if path == "/api/formations" {
            let store = kbcs_data::formations::Store::open(&self.root)?;
            if method == "POST" {
                ensure!(body.len() <= 1_000_000, "編成ファイルが大きすぎます");
                let input: kbcs_data::formations::WriteInput = serde_json::from_slice(body)?;
                return Ok(Reply::json(store.write(&self.region, &input)?));
            }
            ensure!(method == "GET", "未対応の編成操作です");
            let query = url.query_pairs().collect::<BTreeMap<_, _>>();
            if query.get("list").is_some_and(|value| value == "1") {
                return Ok(Reply::json(store.list(&self.region)?));
            }
            let current = query.get("current").map(|v| v.parse::<i64>()).transpose()?;
            let direction = query
                .get("direction")
                .map(|v| v.parse::<i32>())
                .transpose()?
                .unwrap_or(0);
            return Ok(Reply::json(store.read(&self.region, current, direction)?));
        }
        if path == "/api/formation-equipment" {
            ensure!(method == "GET", "GETが必要です");
            return Ok(Reply::json(kbcs_data::stages::equipment_catalog(
                &Database::open(&self.root, &self.region)?,
            )?));
        }
        if path == "/api/calculate" {
            ensure!(method == "POST", "POSTが必要です");
            ensure!(body.len() <= 1_000_000, "計算入力が大きすぎます");
            let value: Value = serde_json::from_slice(body)?;
            ensure!(
                value
                    .as_object()
                    .is_some_and(|object| object.keys().all(|key| [
                        "rewardPolicies",
                        "stats",
                        "enemyStats",
                        "legendRewards",
                        "unitDamage",
                        "enemyDamage",
                        "metalKiller",
                        "poison",
                        "legendExperience",
                        "stageExperience",
                        "materialDrops"
                    ]
                    .contains(&key.as_str()))),
                "未対応の計算項目です"
            );
            let policies: Vec<kbcs_bridge::reward::PolicyInput> = serde_json::from_value(
                value
                    .get("rewardPolicies")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            ensure!(policies.len() <= 128, "報酬条件が多すぎます");
            let policies = policies
                .iter()
                .map(|input| {
                    kbcs_bridge::reward::policy(input)
                        .map_err(|code| anyhow::anyhow!("報酬条件の入力不正: {code}"))
                })
                .collect::<Result<Vec<_>>>()?;
            let statistics: Vec<kbcs_bridge::StatInput> =
                serde_json::from_value(value.get("stats").cloned().unwrap_or_else(|| json!([])))?;
            let enemy_statistics: Vec<kbcs_bridge::enemy::Input> = serde_json::from_value(
                value
                    .get("enemyStats")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let rewards: Vec<kbcs_bridge::reward::Input> = serde_json::from_value(
                value
                    .get("legendRewards")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let unit_damage: Vec<kbcs_bridge::DamageInput> = serde_json::from_value(
                value
                    .get("unitDamage")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let enemy_damage: Vec<kbcs_bridge::DamageInput> = serde_json::from_value(
                value
                    .get("enemyDamage")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let metal_killer: Vec<kbcs_bridge::MetalKillerInput> = serde_json::from_value(
                value
                    .get("metalKiller")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let poison: Vec<kbcs_bridge::PoisonInput> =
                serde_json::from_value(value.get("poison").cloned().unwrap_or_else(|| json!([])))?;
            let experience: Vec<kbcs_bridge::experience::Input> = serde_json::from_value(
                value
                    .get("legendExperience")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            let stage_experience: Vec<kbcs_bridge::experience::StageInput> =
                serde_json::from_value(
                    value
                        .get("stageExperience")
                        .cloned()
                        .unwrap_or_else(|| json!([])),
                )?;
            let materials: Vec<kbcs_bridge::materials::Input> = serde_json::from_value(
                value
                    .get("materialDrops")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            ensure!(
                statistics.len() <= 4000
                    && enemy_statistics.len() <= 4000
                    && rewards.len() <= 64
                    && unit_damage.len() <= 64
                    && enemy_damage.len() <= 64
                    && metal_killer.len() <= 64
                    && poison.len() <= 64
                    && experience.len() <= 64
                    && stage_experience.len() <= 64
                    && materials.len() <= 64,
                "計算件数が上限を超えています"
            );
            let error = |code| anyhow::anyhow!("C++計算エラー{code}（1:入力範囲、2:整数上限）");
            let statistics = statistics
                .iter()
                .map(|input| kbcs_bridge::stat(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let enemy_statistics = enemy_statistics
                .iter()
                .map(|input| kbcs_bridge::enemy::stat(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let rewards = rewards
                .iter()
                .map(|input| kbcs_bridge::reward::legend_pick(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let unit_damage = unit_damage
                .iter()
                .map(|input| kbcs_bridge::unit_damage(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let enemy_damage = enemy_damage
                .iter()
                .map(|input| kbcs_bridge::enemy_damage(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let metal_killer = metal_killer
                .iter()
                .map(|input| kbcs_bridge::unit_metal_killer(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let poison = poison
                .iter()
                .map(|input| kbcs_bridge::enemy_poison(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let experience = experience
                .iter()
                .map(|input| kbcs_bridge::experience::legend(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let stage_experience = stage_experience
                .iter()
                .map(|input| kbcs_bridge::experience::stage(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            let materials = materials
                .iter()
                .map(|input| kbcs_bridge::materials::plan(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            return Ok(Reply::json(
                json!({"rewardPolicies":policies,"abi":kbcs_bridge::abi_version(),"ruleset":kbcs_bridge::ruleset_version(),
                "stats":statistics.iter().map(|output|output.stages[5]).collect::<Vec<_>>(),
                "legendRewards":rewards,"enemyStats":enemy_statistics,"unitDamage":unit_damage,"enemyDamage":enemy_damage,"metalKiller":metal_killer,"poison":poison,"legendExperience":experience,"stageExperience":stage_experience,"materialDrops":materials}),
            ));
        }

        if path == "/api/asset-hashes" {
            ensure!(
                method == "POST" && body.len() <= 16384,
                "原本照合の要求が不正です"
            );
            let paths: Vec<String> = serde_json::from_slice(body)?;
            ensure!(paths.len() <= 64, "原本照合の件数が多すぎます");
            let database =
                Database::open_path(&kbcs_data::store::current_path(&self.root, &self.region)?)?;
            let mut statement = database
                .connection
                .prepare("SELECT sha256 FROM asset_reference WHERE path=?")?;
            let hashes = paths
                .into_iter()
                .map(|path| {
                    let hash: String = statement.query_row([&path], |row| row.get(0))?;
                    Ok((path, hash))
                })
                .collect::<Result<BTreeMap<_, _>>>()?;
            return Ok(Reply::json(json!(hashes)));
        }
        if path == "/api/stage-scene" {
            ensure!(
                method == "POST" && body.len() <= 16384,
                "ステージ描画の要求が不正です"
            );
            let input: crate::scene::Input = serde_json::from_slice(body)?;
            return self.scene_reply(&input, None);
        }

        if path == "/api/import" {
            ensure!(method == "POST", "POSTが必要です");
            let value: Value = serde_json::from_slice(body)?;
            let location = value["source"].as_str().unwrap_or(&self.source).to_owned();
            ensure!(
                self.busy
                    .compare_exchange(false, true, Ordering::SeqCst, Ordering::SeqCst)
                    .is_ok(),
                "更新中です"
            );
            *self
                .progress
                .lock()
                .map_err(|_| anyhow::anyhow!("進捗ロック失敗"))? = Progress {
                message: "取り込み中".into(),
                error: None,
            };
            let service = self.clone();
            std::thread::spawn(move || {
                let result = import::import(&location, &service.root, &service.region, |message| {
                    if let Ok(mut progress) = service.progress.lock() {
                        progress.message = message;
                    }
                });
                if let Ok(mut progress) = service.progress.lock() {
                    match result {
                        Ok(report) => {
                            progress.message = format!(
                                "v{} / {}キャラ / {}形態",
                                report.version, report.units, report.forms
                            );
                            if let Ok(mut cache) = service.catalog.lock() {
                                cache.clear();
                            }
                        }
                        Err(error) => progress.error = Some(format!("{error:#}")),
                    }
                }
                service.busy.store(false, Ordering::SeqCst);
            });
            return Ok(Reply::json(json!({"accepted":true})));
        }
        if path == "/api/motion-timeline" {
            ensure!(method == "POST", "POSTが必要です");
            let input: kbcs_bridge::motion::TimelineInput = serde_json::from_slice(body)?;
            let frames = kbcs_bridge::motion::timeline(input.soul_frames, input.special_frames)
                .map_err(|c| anyhow::anyhow!("モーション時計の入力不正: {c}"))?;
            return Ok(Reply::json(json!({"frames":frames})));
        }
        if path == "/api/motion-pose" {
            ensure!(
                method == "POST" && body.len() <= 16384,
                "描画入力が不正です"
            );
            let input: crate::motion_pose::Input = serde_json::from_slice(body)?;
            ensure!(
                !input.frames.is_empty() && input.frames.len() <= 32,
                "表示フレームが範囲外です"
            );
            let current = kbcs_data::store::current_path(&self.root, &self.region)?;
            let database = Database::open_path(&current)?;
            let key = format!("{}:{}", current.display(), input.key());
            let slot = cache_slot(&self.poses, key)?;
            let model = {
                let mut cached = slot
                    .lock()
                    .map_err(|_| anyhow::anyhow!("モデルのロック失敗"))?;
                if cached.is_none() {
                    *cached = Some(Arc::new(crate::motion_pose::model(
                        &database,
                        &self.region,
                        &input,
                    )?));
                }
                cached.as_ref().unwrap().clone()
            };
            return Ok(Reply::json(crate::motion_pose::frames(model, &input)?));
        }
        ensure!(method == "GET", "未対応の操作です");
        if path == "/api/status" {
            let metadata = Database::open(&self.root, &self.region)
                .and_then(|db| db.metadata())
                .ok();
            let progress = self
                .progress
                .lock()
                .map_err(|_| anyhow::anyhow!("進捗ロック失敗"))?;
            return Ok(Reply::json(
                json!({"busy":self.busy.load(Ordering::SeqCst),"message":progress.message,"error":progress.error,"metadata":metadata,"source":self.source,"updateSource":kbcs_data::DEFAULT_SOURCE,"dataDir":self.root,"assetDir":self.root.join("assets")}),
            ));
        }
        if let Some(id) = path.strip_prefix("/api/stage-audio/") {
            let id = id
                .strip_suffix(".mp3")
                .or_else(|| id.strip_suffix(".ogg"))
                .unwrap_or(id)
                .parse::<i64>()?;
            let slot = {
                let mut pending = self
                    .audio
                    .lock()
                    .map_err(|_| anyhow::anyhow!("音源一覧のロック失敗"))?;
                pending.retain(|_, slot| slot.strong_count() > 0);
                let slot = pending
                    .get(&id)
                    .and_then(Weak::upgrade)
                    .unwrap_or_else(|| Arc::new(Mutex::new(())));
                pending.insert(id, Arc::downgrade(&slot));
                slot
            };
            let _audio = slot
                .lock()
                .map_err(|_| anyhow::anyhow!("音源のロック失敗"))?;
            let audio = kbcs_data::stage_media::audio(&self.root, id)?;
            return Ok(Reply {
                status: 200,
                mime: audio.mime,
                bytes: audio.bytes,
            });
        }
        if path == "/api/motion" {
            let get = |key: &str| {
                url.query_pairs()
                    .find(|(k, _)| k == key)
                    .map(|(_, v)| v.into_owned())
            };
            let database = Database::open(&self.root, &self.region)?;
            if get("kind").as_deref() == Some("effect") {
                return Ok(Reply::json(kbcs_data::effects::manifest(
                    &database,
                    &get("id").unwrap_or_else(|| "skill_wave_attack".into()),
                )?));
            }
            return Ok(Reply::json(kbcs_data::motions::manifest(
                &database,
                &self.region,
                &get("kind").unwrap_or_else(|| "unit".into()),
                get("id").unwrap_or_else(|| "0".into()).parse()?,
                get("form").unwrap_or_else(|| "0".into()).parse()?,
            )?));
        }
        if path == "/api/stage-variant" {
            let get = |key: &str| {
                url.query_pairs()
                    .find(|(k, _)| k == key)
                    .map(|(_, v)| v.into_owned())
                    .ok_or_else(|| anyhow::anyhow!("{key}が必要です"))
            };
            let database = Database::open(&self.root, &self.region)?;
            return Ok(Reply::json(kbcs_data::stages::variant(
                &database,
                &self.region,
                &get("map")?,
                get("stage")?.parse()?,
                &get("source")?,
            )?));
        }
        if [
            "/api/catalog",
            "/api/enemies",
            "/api/stages",
            "/api/motion-effects",
            "/api/motion-choices",
        ]
        .contains(&path)
        {
            let motion_kind = url
                .query_pairs()
                .find(|(key, _)| key == "kind")
                .map(|(_, value)| value.into_owned())
                .unwrap_or_else(|| "unit".into());
            let category = if path == "/api/motion-choices" {
                "motion-choices"
            } else if path == "/api/motion-effects" {
                "effects"
            } else if path == "/api/enemies" {
                "enemies"
            } else if path == "/api/stages" {
                "stages"
            } else {
                "units"
            };
            let map = url
                .query_pairs()
                .find(|(k, _)| k == "map")
                .map(|(_, v)| v.into_owned());
            let key = if category == "stages" {
                format!("stages/{}", map.as_deref().unwrap_or("index"))
            } else if category == "motion-choices" {
                format!("motion-choices/{motion_kind}")
            } else {
                category.to_owned()
            };
            let current = kbcs_data::store::current_path(&self.root, &self.region)?;
            let cached = self
                .catalog
                .lock()
                .map_err(|_| anyhow::anyhow!("表示キャッシュロック失敗"))?
                .get(&key)
                .filter(|(path, _)| path == &current)
                .map(|(_, bytes)| bytes.clone());
            if let Some(bytes) = cached {
                return Ok(Reply {
                    status: 200,
                    mime: "application/json; charset=utf-8",
                    bytes,
                });
            }
            // 重い生成中は共有ロックを保持しない。別カタログの取得を妨げない。
            let database = Database::open_path(&current)?;
            let value = if category == "motion-choices" {
                kbcs_data::motions::choices(&database, &self.region, &motion_kind)?
            } else if category == "effects" {
                kbcs_data::effects::catalog(&database)?
            } else if category == "enemies" {
                kbcs_data::enemies::catalog(&database, &self.region)?
            } else if category == "stages" {
                if let Some(map) = map.as_deref() {
                    kbcs_data::stages::catalog_map(&database, &self.region, Some(map))?
                } else {
                    kbcs_data::stages::search_catalog(&database, &self.region)?
                }
            } else {
                kbcs_data::view::catalog(&database, &self.region)?
            };
            let bytes = serde_json::to_vec(&value)?;
            self.catalog
                .lock()
                .map_err(|_| anyhow::anyhow!("表示キャッシュロック失敗"))?
                .insert(key, (current, bytes.clone()), bytes.len());
            return Ok(Reply {
                status: 200,
                mime: "application/json; charset=utf-8",
                bytes,
            });
        }
        if let Some(logical) = path.strip_prefix("/api/asset/") {
            kbcs_data::source::safe_path(logical)?;
            let database = Database::open(&self.root, &self.region)?;
            let bytes = kbcs_data::source::asset(&database, &self.root, logical)?;
            return Ok(Reply {
                status: 200,
                mime: if logical.ends_with(".png") {
                    "image/png"
                } else {
                    "text/plain; charset=utf-8"
                },
                bytes,
            });
        }
        if path == "/api/source" {
            let id = url
                .query_pairs()
                .find(|(key, _)| key == "id")
                .map(|(_, value)| value.parse::<u32>())
                .transpose()?
                .unwrap_or(0);
            let database = Database::open(&self.root, &self.region)?;
            let logical = format!("Data/unit{:03}.csv", id + 1);
            let (original, kind, sha, bytes) = database.source(&logical)?;
            return Ok(Reply::json(
                json!({"metadata":database.metadata()?,"logical":logical,"original":original,"sourceKind":kind,"sha256":sha,"text":String::from_utf8_lossy(&bytes)}),
            ));
        }
        let name = if path.ends_with('/') {
            format!("{}index.html", path.trim_start_matches('/'))
        } else {
            path.trim_start_matches('/').to_owned()
        };
        if let Some(file) = UI.get_file(&name) {
            let mime = match name.rsplit('.').next().unwrap_or_default() {
                "html" => "text/html; charset=utf-8",
                "js" => "text/javascript; charset=utf-8",
                "css" => "text/css; charset=utf-8",
                "png" => "image/png",
                "json" => "application/json; charset=utf-8",
                _ => "application/octet-stream",
            };
            return Ok(Reply {
                status: 200,
                mime,
                bytes: file.contents().to_vec(),
            });
        }
        Ok(Reply{status:404,mime:"text/html; charset=utf-8",bytes:"<!doctype html><meta charset=utf-8><link rel=stylesheet href=/src/shared/ui/site.css><main class=page-main><h1>未実装</h1><a href=/>ホームへ</a></main>".as_bytes().to_vec()})
    }
}

pub fn serve(root: PathBuf, region: String, source: String, bind: &str) -> Result<()> {
    let address: std::net::SocketAddr = bind.parse()?;
    ensure!(
        address.ip().is_loopback(),
        "プレビューはループバックアドレスに限定します"
    );
    let server = tiny_http::Server::http(address).map_err(|error| anyhow::anyhow!("{error}"))?;
    let service = Service::new(root, region, source);
    println!("KBCS preview: http://{bind}/");
    for mut request in server.incoming_requests() {
        let service = service.clone();
        let path = request.url().to_owned();
        dispatch(&service, &path, move |service, accepted| {
            if !accepted {
                let _ =
                    request.respond(tiny_http::Response::from_string("Busy").with_status_code(503));
                return;
            }
            let mut body = Vec::new();
            if let Err(error) = request.as_reader().take(1024 * 1024).read_to_end(&mut body) {
                eprintln!("{error}");
                return;
            }
            let origin = request
                .headers()
                .iter()
                .find(|header| header.field.equiv("Origin"))
                .map(|header| header.value.as_str());
            let reply = if request.method().as_str() == "POST"
                && origin.is_some_and(|value| value != format!("http://{address}"))
            {
                Reply {
                    status: 403,
                    mime: "text/plain",
                    bytes: b"Forbidden origin".to_vec(),
                }
            } else {
                service.handle(request.method().as_str(), request.url(), &body)
            };
            let response = tiny_http::Response::from_data(reply.bytes)
                .with_status_code(reply.status)
                .with_header(tiny_http::Header::from_bytes("Content-Type", reply.mime).unwrap())
                .with_header(
                    tiny_http::Header::from_bytes("X-Content-Type-Options", "nosniff").unwrap(),
                );
            let _ = request.respond(response);
        });
    }
    Ok(())
}

use std::io::Read;

#[test]
fn native_calculation_service_contract() {
    let options_root =
        std::env::temp_dir().join(format!("kbcs-battle-options-{}", std::process::id()));
    let options_service = Service::new(options_root.clone(), "jp".into(), String::new());
    assert_eq!(
        options_service
            .handle("GET", "/api/battle-options", b"")
            .status,
        200
    );
    let options = br#"{"bgmLevel":0,"seLevel":1,"rows":1}"#;
    assert_eq!(
        options_service
            .handle("PUT", "/api/battle-options", options)
            .status,
        200
    );
    let reopened = Service::new(options_root.clone(), "jp".into(), String::new());
    let saved = reopened.handle("GET", "/api/battle-options", b"");
    assert_eq!(
        serde_json::from_slice::<Value>(&saved.bytes).unwrap(),
        serde_json::from_slice::<Value>(options).unwrap()
    );
    assert_eq!(
        reopened
            .handle(
                "PUT",
                "/api/battle-options",
                br#"{"bgmLevel":4,"seLevel":1,"rows":1}"#
            )
            .status,
        400
    );
    assert_eq!(
        reopened
            .handle(
                "PUT",
                "/api/battle-options",
                br#"{"bgmLevel":0,"seLevel":1,"rows":1,"unknown":1}"#
            )
            .status,
        400
    );
    // 自分で作った試験用SQLiteだけを閉じて削除する。
    drop(reopened);
    drop(options_service);
    std::fs::remove_file(options_root.join("user/battle-options.sqlite")).unwrap();
    std::fs::remove_dir(options_root.join("user")).unwrap();
    std::fs::remove_dir(options_root).unwrap();
    let service = Service::new(PathBuf::new(), "jp".into(), String::new());
    for (key, fixture) in [
        (
            "enemyStats",
            include_str!("../../../native/kbcs-core/tests/enemy-stat-vectors.json"),
        ),
        (
            "legendRewards",
            include_str!("../../../native/kbcs-core/tests/reward-vectors.json"),
        ),
        (
            "stageExperience",
            include_str!("../../../native/kbcs-core/tests/band-experience-vectors.json"),
        ),
    ] {
        let fixture: Value = serde_json::from_str(fixture).unwrap();
        let rows = &fixture["vectors"].as_array().unwrap()
            [..fixture["vectors"].as_array().unwrap().len().min(64)];
        let body = serde_json::to_vec(
            &json!({key:rows.iter().map(|row| &row["input"]).collect::<Vec<_>>()}),
        )
        .unwrap();
        let reply = service.handle("POST", "/api/calculate", &body);
        assert_eq!(reply.status, 200);
        let result: Value = serde_json::from_slice(&reply.bytes).unwrap();
        assert_eq!(result["abi"], 4);
        assert_eq!(result["ruleset"], 1507021);
        assert_eq!(result[key].as_array().unwrap().len(), rows.len());
        for (row, output) in rows.iter().zip(result[key].as_array().unwrap()) {
            if key == "enemyStats" || key == "stageExperience" {
                assert_eq!(output["stages"], row["stages"]);
            } else {
                for field in ["winner", "consumed", "markAcquired", "radarBlocked"] {
                    assert_eq!(output[field], row[field]);
                }
            }
        }
    }
    let reply = service.handle(
        "POST",
        "/api/motion-timeline",
        br#"{"soulFrames":49,"specialFrames":81}"#,
    );
    assert_eq!(reply.status, 200);
    let result: Value = serde_json::from_slice(&reply.bytes).unwrap();
    assert_eq!(result["frames"].as_array().unwrap().len(), 106);
    assert_eq!(result["frames"][24]["phase"], 1);
    assert_eq!(result["frames"][105]["phase"], 2);
    for body in [
        br#"{"soulFrames":-1,"specialFrames":0}"#.as_slice(),
        br#"{"soulFrames":1,"specialFrames":1,"unknown":1}"#,
    ] {
        assert_eq!(
            service.handle("POST", "/api/motion-timeline", body).status,
            400
        );
    }
    let reply = service.handle(
        "POST",
        "/api/motion-pose",
        br#"{"kind":"unit","id":0,"resource":"body","clip":"02","frames":[],"facing":1}"#,
    );
    assert_eq!(reply.status, 400);
    assert!(
        serde_json::from_slice::<Value>(&reply.bytes).unwrap()["error"]
            .as_str()
            .unwrap()
            .contains("表示フレーム")
    );
    // ルートとPODの両方で未知項目を拒否し、DBを開かず検査できる。
    for body in [br#"{"unknown":[]}"#.as_slice(), br#"{"enemyStats":[{"base":0,"rowPercent":100,"crownPercent":100,"crystalMax":0,"crystalTreasure":0,"castleAttack":0,"unknown":1}]}"#] {
        assert_eq!(service.handle("POST", "/api/calculate", body).status, 400);
    }
}
