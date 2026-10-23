use anyhow::{Result, ensure};
use include_dir::{Dir, include_dir};
use kbcs_data::{import, store::Database};
use serde_json::{Value, json};
use std::{
    collections::BTreeMap,
    path::PathBuf,
    sync::{
        Arc, Mutex,
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
}

type CatalogCache = BTreeMap<String, (PathBuf, Vec<u8>)>;

impl Service {
    pub fn new(root: PathBuf, region: String, source: String) -> Self {
        Self {
            root,
            region,
            source,
            busy: Arc::new(AtomicBool::new(false)),
            progress: Arc::new(Mutex::new(Progress::default())),
            catalog: Arc::new(Mutex::new(BTreeMap::new())),
        }
    }

    pub fn handle(&self, method: &str, path: &str, body: &[u8]) -> Reply {
        match self.route(method, path, body) {
            Ok(reply) => reply,
            Err(error) => Reply::error(error),
        }
    }

    fn route(&self, method: &str, path: &str, body: &[u8]) -> Result<Reply> {
        let url = url::Url::parse(&format!("http://kbcs.localhost{path}"))?;
        let path = url.path();
        if path == "/api/calculate" {
            ensure!(method == "POST", "POSTが必要です");
            ensure!(body.len() <= 1_000_000, "計算入力が大きすぎます");
            let value: Value = serde_json::from_slice(body)?;
            ensure!(
                value
                    .as_object()
                    .is_some_and(|object| object.keys().all(|key| [
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
                json!({"abi":kbcs_bridge::abi_version(),"ruleset":kbcs_bridge::ruleset_version(),
                "stats":statistics.iter().map(|output|output.stages[5]).collect::<Vec<_>>(),
                "legendRewards":rewards,"enemyStats":enemy_statistics,"unitDamage":unit_damage,"enemyDamage":enemy_damage,"metalKiller":metal_killer,"poison":poison,"legendExperience":experience,"stageExperience":stage_experience,"materialDrops":materials}),
            ));
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
                json!({"busy":self.busy.load(Ordering::SeqCst),"message":progress.message,"error":progress.error,"metadata":metadata,"source":self.source}),
            ));
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
        ]
        .contains(&path)
        {
            let category = if path == "/api/motion-effects" {
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
            } else {
                category.to_owned()
            };
            let current = kbcs_data::store::current_path(&self.root, &self.region)?;
            let mut cache = self
                .catalog
                .lock()
                .map_err(|_| anyhow::anyhow!("表示キャッシュロック失敗"))?;
            if cache.get(&key).is_none_or(|(path, _)| path != &current) {
                let database = Database::open_path(&current)?;
                let value = if category == "effects" {
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
                cache.insert(key.clone(), (current, serde_json::to_vec(&value)?));
            }
            return Ok(Reply {
                status: 200,
                mime: "application/json; charset=utf-8",
                bytes: cache
                    .get(&key)
                    .map(|(_, bytes)| bytes.clone())
                    .unwrap_or_default(),
            });
        }
        if let Some(logical) = path.strip_prefix("/api/asset/") {
            kbcs_data::source::safe_path(logical)?;
            let database = Database::open(&self.root, &self.region)?;
            let (_, _, _, bytes) = database.source(logical)?;
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
        std::thread::spawn(move || {
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
        assert_eq!(result["abi"], 2);
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
    // ルートとPODの両方で未知項目を拒否し、DBを開かず検査できる。
    for body in [br#"{"unknown":[]}"#.as_slice(), br#"{"enemyStats":[{"base":0,"rowPercent":100,"crownPercent":100,"crystalMax":0,"crystalTreasure":0,"castleAttack":0,"unknown":1}]}"#] {
        assert_eq!(service.handle("POST", "/api/calculate", body).status, 400);
    }
}
