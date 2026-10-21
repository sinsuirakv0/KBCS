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

type CatalogCache = BTreeMap<&'static str, (PathBuf, Vec<u8>)>;

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
                        "unitDamage",
                        "enemyDamage",
                        "metalKiller",
                        "poison",
                        "legendExperience",
                        "materialDrops"
                    ]
                    .contains(&key.as_str()))),
                "未対応の計算項目です"
            );
            let statistics: Vec<kbcs_bridge::StatInput> =
                serde_json::from_value(value.get("stats").cloned().unwrap_or_else(|| json!([])))?;
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
            let materials: Vec<kbcs_bridge::materials::Input> = serde_json::from_value(
                value
                    .get("materialDrops")
                    .cloned()
                    .unwrap_or_else(|| json!([])),
            )?;
            ensure!(
                statistics.len() <= 4000
                    && unit_damage.len() <= 64
                    && enemy_damage.len() <= 64
                    && metal_killer.len() <= 64
                    && poison.len() <= 64
                    && experience.len() <= 64
                    && materials.len() <= 64,
                "計算件数が上限を超えています"
            );
            let error = |code| anyhow::anyhow!("C++計算エラー{code}（1:入力範囲、2:整数上限）");
            let statistics = statistics
                .iter()
                .map(|input| kbcs_bridge::stat(input).map_err(error))
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
            let materials = materials
                .iter()
                .map(|input| kbcs_bridge::materials::plan(input).map_err(error))
                .collect::<Result<Vec<_>>>()?;
            return Ok(Reply::json(
                json!({"abi":kbcs_bridge::abi_version(),"ruleset":kbcs_bridge::ruleset_version(),
                "stats":statistics.iter().map(|output|output.stages[5]).collect::<Vec<_>>(),
                "unitDamage":unit_damage,"enemyDamage":enemy_damage,"metalKiller":metal_killer,"poison":poison,"legendExperience":experience,"materialDrops":materials}),
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
        if path == "/api/catalog" || path == "/api/enemies" || path == "/api/stages" {
            let key = if path == "/api/enemies" {
                "enemies"
            } else if path == "/api/stages" {
                "stages"
            } else {
                "units"
            };
            let current = kbcs_data::store::current_path(&self.root, &self.region)?;
            let mut cache = self
                .catalog
                .lock()
                .map_err(|_| anyhow::anyhow!("表示キャッシュロック失敗"))?;
            if cache.get(key).is_none_or(|(path, _)| path != &current) {
                let database = Database::open_path(&current)?;
                let value = if key == "enemies" {
                    kbcs_data::enemies::catalog(&database, &self.region)?
                } else if key == "stages" {
                    kbcs_data::stages::catalog(&database, &self.region)?
                } else {
                    kbcs_data::view::catalog(&database, &self.region)?
                };
                cache.insert(key, (current, serde_json::to_vec(&value)?));
            }
            return Ok(Reply {
                status: 200,
                mime: "application/json; charset=utf-8",
                bytes: cache
                    .get(key)
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
