use crate::service::{Reply, Service, dispatch};
use anyhow::{Context, Result, bail, ensure};
use serde_json::{Value, json};
use std::{
    io::{Read, Write},
    net::{Ipv4Addr, TcpListener},
    path::{Path, PathBuf},
    process::{Command, Stdio},
    sync::{
        Arc, Mutex,
        atomic::{AtomicBool, Ordering},
    },
    time::{Duration, Instant},
};
use tiny_http::{Header, Request, Response, Server};
use url::Url;
#[path = "phone_battle.rs"]
pub mod battle;

const DISPLAY: &str = "/pages/phone-display/";
const COOKIE: &str = "kbcs_phone";
const MAX_BODY: u64 = 1_000_000;
const BATTLE_FRAME_MIME: &str = "application/x-kbcs-battle-frame";

#[derive(Default)]
pub struct Phone {
    link: Mutex<Option<Link>>,
    screen: Arc<Mutex<Option<String>>>,
    pub battle: Arc<battle::Exchange>,
}

struct Link {
    adb: PathBuf,
    device: String,
    port: String,
    url: String,
    active: Arc<AtomicBool>,
    paired: Arc<AtomicBool>,
    opened: bool,
}

impl Phone {
    pub fn companion(&self) -> Self {
        Self {
            battle: self.battle.clone(),
            ..Self::default()
        }
    }

    #[cfg(any(windows, target_os = "macos", test))]
    pub fn navigate(&self, url: &str) {
        let next = sortie_route(url);
        let mut screen = self.screen.lock().unwrap();
        if *screen != next {
            self.battle.reset();
            *screen = next;
        }
    }

    pub fn start(&self, service: &Service) -> Result<()> {
        let mut link = self.link.lock().unwrap();
        if link.as_ref().is_some_and(Link::active) {
            return Ok(());
        }
        if let Some(previous) = link.take() {
            previous.disconnect();
            self.battle.reset();
        }
        let adb = adb_path();
        let device = adb_command(&adb, &["-d", "get-serialno"])
            .context("AndroidをUSBで接続し、端末でUSBデバッグを許可してください")?;
        ensure!(!device.is_empty(), "USB接続のAndroid端末を確認できません");
        let listener = TcpListener::bind((Ipv4Addr::LOCALHOST, 0))?;
        let address = listener.local_addr()?.to_string();
        let port = format!("tcp:{}", listener.local_addr()?.port());
        let server =
            Server::from_listener(listener, None).map_err(|error| anyhow::anyhow!(error))?;
        let active = Arc::new(AtomicBool::new(true));
        let paired = Arc::new(AtomicBool::new(false));
        let mut secret = [0u8; 32];
        getrandom::fill(&mut secret).map_err(|error| anyhow::anyhow!("{error}"))?;
        let ticket = format!("/phone-connect/{}", kbcs_data::source::hash(&secret));
        getrandom::fill(&mut secret).map_err(|error| anyhow::anyhow!("{error}"))?;
        let cookie = format!("{COOKIE}={}", kbcs_data::source::hash(&secret));
        adb_command(
            &adb,
            &["-s", &device, "reverse", "--no-rebind", &port, &port],
        )?;
        let url = format!("http://{address}{ticket}");
        let session = DisplaySession {
            address,
            ticket,
            cookie,
            active: active.clone(),
            paired: paired.clone(),
            screen: self.screen.clone(),
            battle: self.battle.clone(),
            polling: Arc::default(),
        };
        let phone = service.phone_service();
        if let Err(error) = std::thread::Builder::new()
            .name("kbcs-phone-usb".into())
            .spawn(move || session.serve(server, &phone))
        {
            let _ = remove_reverse(&adb, &device, &port);
            return Err(error.into());
        }
        let opened = adb_command(
            &adb,
            &[
                "-s",
                &device,
                "shell",
                "am",
                "start",
                "-a",
                "android.intent.action.VIEW",
                "-d",
                &url,
                "-p",
                "com.android.chrome",
            ],
        )
        .is_ok();
        *link = Some(Link {
            adb,
            device,
            port,
            url,
            active,
            paired,
            opened,
        });
        Ok(())
    }

    pub fn stop(&self) {
        let mut connection = self.link.lock().unwrap();
        if let Some(link) = connection.take() {
            link.disconnect();
        }
        self.battle.reset();
    }

    pub fn status(&self) -> Value {
        let link = self.link.lock().unwrap();
        link.as_ref().filter(|link| link.active()).map_or_else(
            || json!({"active":false}),
            |link| {
                let paired = link.paired.load(Ordering::Acquire);
                json!({"active":true,"paired":paired,"opened":link.opened,
                    "url":(!paired).then_some(&link.url)})
            },
        )
    }
}

impl Link {
    fn active(&self) -> bool {
        self.active.load(Ordering::Acquire)
    }

    fn disconnect(self) {
        self.active.store(false, Ordering::Release);
        // USBが抜けていれば転送も失われる。別のサービスの転送には触れない。
        let _ = remove_reverse(&self.adb, &self.device, &self.port);
    }
}

#[cfg(any(windows, target_os = "macos", test))]
fn sortie_route(url: &str) -> Option<String> {
    let source = Url::parse(url).ok()?;
    if !matches!(
        (source.scheme(), source.host_str()),
        ("kbcs", Some("localhost")) | ("http", Some("kbcs.localhost"))
    ) || source.path() != "/pages/stage-sortie/"
    {
        return None;
    }
    let query = url::form_urlencoded::Serializer::new(String::from("phone=1"))
        .extend_pairs(
            source
                .query_pairs()
                .filter(|(key, _)| matches!(key.as_ref(), "map" | "stage" | "crown")),
        )
        .finish();
    Some(format!("/pages/stage-sortie/?{query}"))
}

struct DisplaySession {
    address: String,
    ticket: String,
    cookie: String,
    active: Arc<AtomicBool>,
    paired: Arc<AtomicBool>,
    screen: Arc<Mutex<Option<String>>>,
    battle: Arc<battle::Exchange>,
    polling: Arc<AtomicBool>,
}

impl DisplaySession {
    fn serve(self, server: Server, service: &Service) {
        while self.active.load(Ordering::Acquire) {
            match server.recv_timeout(Duration::from_millis(200)) {
                Ok(Some(request)) => self.receive(request, service),
                Ok(None) => (),
                Err(_) => break,
            }
        }
        self.active.store(false, Ordering::Release);
    }

    fn receive(&self, mut request: Request, service: &Service) {
        let origin = format!("http://{}", self.address);
        let method = request.method().as_str().to_owned();
        let target = request.url().to_owned();
        if request_header(&request, "Host") != Some(self.address.as_str()) {
            respond(request, 403, Vec::new(), &[]);
            return;
        }
        if !target.starts_with('/') {
            respond(request, 400, Vec::new(), &[]);
            return;
        }
        if method == "GET"
            && target == self.ticket
            && request_header(&request, "Sec-Fetch-Mode").is_none_or(|value| value == "navigate")
            && !self.paired.swap(true, Ordering::AcqRel)
        {
            let cookie = format!("{}; Path=/; HttpOnly; SameSite=Strict", self.cookie);
            // Androidの外部Intentから来た場合も、Cookieを同一オリジンのページ遷移で送る。
            let page = format!(
                "<!doctype html><meta charset=utf-8><title>KBCS</title><script>location.replace('{DISPLAY}')</script>"
            );
            respond(
                request,
                200,
                page.into_bytes(),
                &[
                    ("Content-Type", "text/html; charset=utf-8"),
                    ("Set-Cookie", &cookie),
                    ("Cache-Control", "no-store"),
                ],
            );
            return;
        }
        if request_header(&request, "Origin").is_some_and(|value| value != origin)
            || request_header(&request, "Sec-Fetch-Site") == Some("cross-site")
        {
            respond(request, 403, Vec::new(), &[]);
            return;
        }
        let paired = request_header(&request, "Cookie")
            .is_some_and(|value| value.split(';').any(|part| part.trim() == self.cookie));
        if !paired {
            respond(request, 403, b"KBCS USB pairing is required.".to_vec(), &[]);
            return;
        }
        let Ok(url) = Url::parse(&format!("{origin}{target}")) else {
            respond(request, 400, Vec::new(), &[]);
            return;
        };
        let path = url.path();
        if method == "GET" && path == "/api/phone/screen" {
            let body = serde_json::to_vec(&json!({"route":*self.screen.lock().unwrap()})).unwrap();
            respond(request, 200, body, &[("Content-Type", "application/json")]);
            return;
        }
        if method == "GET" && path == "/api/phone/commands" {
            // 操作待機は戦闘や素材用のワーカーを占有しない。
            if self.polling.swap(true, Ordering::AcqRel) {
                respond(request, 429, Vec::new(), &[]);
                return;
            }
            let (battle, active, polling) = (
                self.battle.clone(),
                self.active.clone(),
                self.polling.clone(),
            );
            std::thread::spawn(move || {
                let commands = battle.commands(&active);
                let body = serde_json::to_vec(&commands).unwrap_or_default();
                polling.store(false, Ordering::Release);
                respond(
                    request,
                    200,
                    body,
                    &[
                        ("Content-Type", "application/json"),
                        ("Cache-Control", "no-store"),
                    ],
                );
            });
            return;
        }
        if !phone_route(&method, path) {
            respond(request, 404, Vec::new(), &[]);
            return;
        }
        let active = self.active.clone();
        let media = (path.starts_with("/api/asset/") || path.starts_with("/api/stage-audio/"))
            && url
                .query_pairs()
                .any(|(key, value)| key == "build" && !value.is_empty());
        let cache = method == "GET"
            && (media || !path.starts_with("/api/") && !path.starts_with("/pages/"));
        dispatch(service, path, move |service, accepted| {
            if !active.load(Ordering::Acquire) {
                respond(request, 410, Vec::new(), &[]);
                return;
            }
            if !accepted {
                service_reply(request, Reply::overloaded(), false);
                return;
            }
            let mut body = Vec::new();
            if request
                .as_reader()
                .take(MAX_BODY + 1)
                .read_to_end(&mut body)
                .is_err()
                || body.len() as u64 > MAX_BODY
            {
                respond(request, 413, Vec::new(), &[]);
                return;
            }
            service_reply(request, service.handle(&method, &target, &body), cache);
        });
    }
}

fn phone_route(method: &str, path: &str) -> bool {
    match method {
        "GET" => {
            matches!(
                path,
                DISPLAY
                    | "/pages/stage-sortie/"
                    | "/api/stages"
                    | "/api/stage-variant"
                    | "/api/enemies"
                    | "/api/catalog"
                    | "/api/motion"
                    | "/api/formations"
                    | "/api/formation-equipment"
                    | "/api/battle-options"
                    | "/api/inventory/catalog"
            ) || path.starts_with("/api/asset/")
                || path.starts_with("/api/stage-audio/")
                || !path.starts_with("/api/")
                    && path.rsplit_once('.').is_some_and(|(_, ext)| {
                        matches!(
                            ext,
                            "js" | "mjs" | "css" | "png" | "svg" | "woff" | "woff2" | "ttf" | "json"
                        )
                    })
                || path == "/phone-runtime/kbcs_phone.wasm"
        }
        "POST" => matches!(
            path,
            "/api/asset-hashes"
                | "/api/stage-scene"
                | "/api/deployment"
                | "/api/battle-support"
                | "/api/battle-info"
                | "/api/battle-popup"
                | "/api/formations"
                | "/api/battle-session"
                | "/api/battle-session/frame"
                | "/api/battle-session/input"
                | "/api/phone/sample"
                | "/api/phone/settle"
                | "/api/phone/failure"
        ),
        "PUT" => path == "/api/battle-options",
        "DELETE" => path == "/api/battle-session",
        _ => false,
    }
}

fn request_header<'a>(request: &'a Request, field: &'static str) -> Option<&'a str> {
    request
        .headers()
        .iter()
        .find(|header| header.field.equiv(field))
        .map(|header| header.value.as_str())
}

fn respond(request: Request, status: u16, body: Vec<u8>, headers: &[(&str, &str)]) {
    let frame = headers.contains(&("Content-Type", BATTLE_FRAME_MIME));
    let body_size = body.len();
    // 長さが確定済みのUSB応答にチャンクの区切りを挟まない。
    let mut response = Response::from_data(body)
        .with_status_code(status)
        .with_chunked_threshold(usize::MAX);
    for (key, value) in headers.iter().copied().chain([
        ("Referrer-Policy", "no-referrer"),
        ("X-Content-Type-Options", "nosniff"),
        ("X-Frame-Options", "SAMEORIGIN"),
    ]) {
        if let Ok(header) = Header::from_bytes(key, value) {
            response.add_header(header);
        }
    }
    if frame {
        // ヘッダーと本文をまとめ、adb reverseで短い先頭の書き込みが先行しないようにする。
        let mut bytes = Vec::with_capacity(body_size + 512);
        if response
            .raw_print(
                &mut bytes,
                request.http_version().clone(),
                request.headers(),
                request.method() == &tiny_http::Method::Head,
                None,
            )
            .is_ok()
        {
            let mut writer = request.into_writer();
            let _ = writer.write_all(&bytes).and_then(|()| writer.flush());
        }
    } else {
        let _ = request.respond(response);
    }
}

fn service_reply(request: Request, reply: Reply, cache: bool) {
    let cache = cache && reply.status == 200;
    let frame = reply.mime == BATTLE_FRAME_MIME;
    let gzip_started = frame.then(Instant::now);
    // 小さいフレームには圧縮の待ち時間を足さない。大きいフレームはChromeのHTTP展開を使う。
    let compressed = if (frame || reply.mime == "application/x-kbcs-battle-setup")
        && reply.bytes.len() > 16 * 1024
        && request_header(&request, "Accept-Encoding").is_some_and(accepts_gzip)
    {
        crate::battle_wire::gzip_if_smaller(&reply.bytes).unwrap_or(None)
    } else {
        None
    };
    let gzip_ms =
        gzip_started.map(|started| format!("{:.3}", started.elapsed().as_secs_f64() * 1000.));
    let headers = [
        ("Content-Type", reply.mime),
        (
            "Cache-Control",
            if cache {
                "private, max-age=3600"
            } else {
                "no-store"
            },
        ),
        ("X-KBCS-Gzip-Ms", gzip_ms.as_deref().unwrap_or_default()),
        ("Content-Encoding", "gzip"),
    ];
    let mut headers = headers;
    let mut header_count = 2;
    if frame { header_count += 1; }
    if compressed.is_some() {
        headers[header_count] = ("Content-Encoding", "gzip");
        header_count += 1;
    }
    respond(
        request,
        reply.status,
        compressed.unwrap_or(reply.bytes),
        &headers[..header_count],
    );
}

fn accepts_gzip(value: &str) -> bool {
    value.split(',').any(|entry| {
        let (coding, quality) = entry.split_once(';').unwrap_or((entry, "q=1"));
        coding.trim().eq_ignore_ascii_case("gzip")
            && quality
                .trim()
                .strip_prefix("q=")
                .and_then(|q| q.parse::<f32>().ok())
                .is_some_and(|q| q > 0. && q <= 1.)
    })
}

fn adb_path() -> PathBuf {
    let name = if cfg!(windows) { "adb.exe" } else { "adb" };
    ["ANDROID_HOME", "ANDROID_SDK_ROOT"]
        .into_iter()
        .filter_map(std::env::var_os)
        .map(PathBuf::from)
        .chain(std::env::var_os("LOCALAPPDATA").map(|path| PathBuf::from(path).join("Android/Sdk")))
        .chain(std::env::var_os("HOME").map(|path| PathBuf::from(path).join("Library/Android/sdk")))
        .map(|sdk| sdk.join("platform-tools").join(name))
        .find(|path| path.is_file())
        .unwrap_or_else(|| PathBuf::from(name))
}

fn remove_reverse(adb: &Path, device: &str, port: &str) -> Result<String> {
    adb_command(adb, &["-s", device, "reverse", "--remove", port])
}

fn adb_command(adb: &Path, args: &[&str]) -> Result<String> {
    let mut command = Command::new(adb);
    command
        .args(args)
        .stdin(Stdio::null())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());
    #[cfg(windows)]
    {
        use std::os::windows::process::CommandExt;
        command.creation_flags(0x08000000);
    }
    let mut child = command
        .spawn()
        .context("Android SDK Platform-Toolsのadbを起動できません")?;
    let timeout = Instant::now() + Duration::from_secs(8);
    while child.try_wait()?.is_none() {
        if Instant::now() >= timeout {
            let _ = child.kill();
            let _ = child.wait();
            bail!("USBデバッグの応答がありません");
        }
        std::thread::sleep(Duration::from_millis(20));
    }
    let output = child.wait_with_output()?;
    let text = String::from_utf8_lossy(&output.stdout);
    let error = String::from_utf8_lossy(&output.stderr);
    ensure!(
        output.status.success() && !text.lines().any(|line| line.starts_with("Error")),
        "adb: {}",
        if error.trim().is_empty() {
            text.trim()
        } else {
            error.trim()
        }
    );
    Ok(text.trim().to_owned())
}

#[test]
fn usb_session_pairs_once_and_exposes_only_battle_pages() {
    use std::{io::Write, net::TcpStream};

    let listener = TcpListener::bind((Ipv4Addr::LOCALHOST, 0)).unwrap();
    let address = listener.local_addr().unwrap();
    let server = Server::from_listener(listener, None).unwrap();
    let active = Arc::new(AtomicBool::new(true));
    let phone = Phone::default();
    let session = DisplaySession {
        address: address.to_string(),
        ticket: "/phone-connect/test-ticket".into(),
        cookie: "kbcs_phone=test-cookie".into(),
        active: active.clone(),
        paired: Arc::default(),
        screen: phone.screen.clone(),
        battle: phone.battle.clone(),
        polling: Arc::default(),
    };
    let task = std::thread::spawn(move || {
        session.serve(
            server,
            &Service::new(PathBuf::new(), "jp".into(), String::new()).phone_service(),
        );
    });
    let request = |path: &str, headers: &str| {
        let mut stream = TcpStream::connect(address).unwrap();
        stream
            .set_read_timeout(Some(Duration::from_secs(5)))
            .unwrap();
        write!(
            stream,
            "GET {path} HTTP/1.0\r\nHost: {address}\r\n{headers}\r\n"
        )
        .unwrap();
        let mut response = String::new();
        stream.read_to_string(&mut response).unwrap();
        response
    };
    let cookie = "Cookie: kbcs_phone=test-cookie\r\n";
    let pairing = request(
        "/phone-connect/test-ticket",
        "Sec-Fetch-Site: cross-site\r\nSec-Fetch-Mode: navigate\r\n",
    );
    assert!(
        pairing.contains("200 OK") && pairing.contains("HttpOnly") && pairing.contains(DISPLAY)
    );
    assert!(accepts_gzip("deflate, gzip, br"));
    assert!(!accepts_gzip("gzip;q=0, br"));
    assert!(request("/phone-connect/test-ticket", "").contains("403"));
    assert!(request("/api/phone/screen", "").contains("403"));
    assert!(request("/api/asset/../../api/status", cookie).contains("404"));
    assert!(
        request(
            "/api/phone/screen",
            &format!("{cookie}Origin: https://example.net\r\n")
        )
        .contains("403")
    );
    let display = request(DISPLAY, cookie);
    assert!(display.contains("phone-standby") && !display.contains("startup-boot.js"));
    let sortie = request("/pages/stage-sortie/?phone=1&map=N000", cookie);
    assert!(sortie.contains("sortie-launch") && !sortie.contains("startup-boot.js"));
    phone.navigate("http://kbcs.localhost/pages/stage-sortie/?map=N000&stage=3&crown=2");
    assert!(request("/api/phone/screen", cookie).contains("phone=1&map=N000&stage=3&crown=2"));
    phone.navigate("kbcs://localhost/pages/settings/");
    assert!(request("/api/phone/screen", cookie).contains("\"route\":null"));
    active.store(false, Ordering::Release);
    task.join().unwrap();
}
