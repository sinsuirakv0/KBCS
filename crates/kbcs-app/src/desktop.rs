use crate::service::Service;
use anyhow::Result;
use std::path::PathBuf;
use tao::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoopBuilder},
    window::WindowBuilder,
};
use wry::{NewWindowResponse, WebContext, WebViewBuilder};

const BATTLE_HELP: &str =
    "https://kbc-rakv0.pages.dev/information/appli/battlecats/help/index.html";
fn open_battle_help(url: &str) {
    if url == BATTLE_HELP {
        // 対象を固定し、外部ヘルプだけを既定のブラウザで開く。
        #[cfg(windows)]
        {
            use std::os::windows::process::CommandExt;
            let _ = std::process::Command::new("explorer.exe")
                .arg(BATTLE_HELP)
                .creation_flags(0x08000000)
                .spawn();
        }
        #[cfg(target_os = "macos")]
        let _ = std::process::Command::new("/usr/bin/open")
            .arg(BATTLE_HELP)
            .spawn();
    }
}

pub fn run(root: PathBuf, region: String, source: String) -> Result<()> {
    start(root, region, source, false)
}

pub fn check(root: PathBuf, region: String, source: String) -> Result<()> {
    start(root, region, source, true)
}

fn start(root: PathBuf, region: String, source: String, check: bool) -> Result<()> {
    let event_loop = EventLoopBuilder::<i32>::with_user_event().build();
    let update_exit = event_loop.create_proxy();
    if check {
        let timeout = update_exit.clone();
        std::thread::spawn(move || {
            std::thread::sleep(std::time::Duration::from_secs(40));
            let _ = timeout.send_event(2);
        });
    }
    let window = WindowBuilder::new()
        .with_visible(!check)
        .with_title("KBCS")
        .with_inner_size(tao::dpi::LogicalSize::new(1180.0, 820.0))
        .with_min_inner_size(tao::dpi::LogicalSize::new(760.0, 520.0))
        .build(&event_loop)?;
    let mut service = Service::new(root.clone(), region, source);
    service.desktop = true;
    if !check {
        service.start_updates();
    }
    let mut context = WebContext::new(Some(root.join("webview")));
    let builder = WebViewBuilder::new_with_web_context(&mut context);
    #[cfg(target_os = "macos")]
    let builder = {
        use wry::WebViewBuilderExtDarwin;
        // WKWebViewはdata_directoryを使わない。保存先別の安定した識別子を使う。
        let hash = kbcs_data::source::hash(root.to_string_lossy().as_bytes());
        let mut identifier = [0u8; 16];
        for (index, byte) in identifier.iter_mut().enumerate() {
            *byte = u8::from_str_radix(&hash[index * 2..index * 2 + 2], 16).unwrap();
        }
        builder.with_data_store_identifier(identifier)
    };
    let webview = builder
        .with_initialization_script(if check { DESKTOP_CHECK } else { "" })
        .with_asynchronous_custom_protocol("kbcs".into(), move |_, request, responder| {
            let path = request.uri().path().to_owned();
            crate::service::dispatch(&service, &path, move |service, accepted| {
                let path = request
                    .uri()
                    .path_and_query()
                    .map_or("/", |value| value.as_str());
                let reply = if accepted {
                    service.handle(request.method().as_str(), path, request.body())
                } else {
                    crate::service::Reply::overloaded()
                };
                let response = wry::http::Response::builder()
                    .status(reply.status)
                    .header("Content-Type", reply.mime)
                    .header("X-Content-Type-Options", "nosniff")
                    .body(reply.bytes)
                    .unwrap();
                responder.respond(response);
            });
        })
        .with_ipc_handler({
            move |request| {
                if request.body() == "kbcs:restart-for-update" {
                    let _ = update_exit.send_event(0);
                } else if check
                    && let Some(result) = request.body().strip_prefix("kbcs:desktop-check:")
                {
                    eprintln!("KBCS desktop check: {result}");
                    let ok = serde_json::from_str::<serde_json::Value>(result)
                        .is_ok_and(|value| value["ok"] == true);
                    let _ = update_exit.send_event(if ok { 0 } else { 1 });
                }
            }
        })
        .with_new_window_req_handler(|url, _| {
            open_battle_help(&url);
            NewWindowResponse::Deny
        })
        .with_navigation_handler(|url| {
            open_battle_help(&url);
            url.starts_with("http://kbcs.localhost/") || url.starts_with("kbcs://localhost/")
        })
        .with_on_page_load_handler(|event, url| {
            if matches!(event, wry::PageLoadEvent::Finished) {
                eprintln!("KBCS UI loaded: {url}");
            }
        })
        .with_url("kbcs://localhost/")
        .build(&window)?;
    event_loop.run(move |event, _, control_flow| {
        let _ = &webview;
        *control_flow = ControlFlow::Wait;
        if let Event::UserEvent(code) = event {
            *control_flow = ControlFlow::ExitWithCode(code);
        }
        if let Event::WindowEvent {
            event: WindowEvent::CloseRequested,
            ..
        } = event
        {
            *control_flow = ControlFlow::Exit;
        }
    });
}

// 画面操作をせず、実際のWebViewで同梱module・PNG・POST本文・C++入口を確認する。
const DESKTOP_CHECK: &str = r#"
window.addEventListener('DOMContentLoaded', async () => {
  try {
    const {createSessionId} = await import('/src/shared/browser/session-id.js');
    const id = createSessionId();
    if (!/^[0-9a-f-]{36}$/.test(id)) throw Error('session id');
    const response = await fetch('/api/motion-timeline', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({soulFrames:2,specialFrames:3})});
    if (!response.ok || !(await response.json()).frames.length) throw Error('native POST');
    const image = await fetch('/images/kbc-logo.png');
    if (!image.ok || new Uint8Array(await image.arrayBuffer())[0] !== 137) throw Error('image');
    if (!document.createElement('canvas').getContext('webgl')) throw Error('WebGL');
    window.ipc.postMessage('kbcs:desktop-check:'+JSON.stringify({ok:true}));
  } catch (error) {
    window.ipc.postMessage('kbcs:desktop-check:'+JSON.stringify({ok:false,error:String(error)}));
  }
}, {once:true});
"#;
