use crate::service::Service;
use anyhow::Result;
use std::path::PathBuf;
use tao::{
    event::{Event, WindowEvent},
    event_loop::{ControlFlow, EventLoop},
    window::WindowBuilder,
};
use wry::{NewWindowResponse, WebContext, WebViewBuilder};

const BATTLE_HELP: &str =
    "https://kbc-rakv0.pages.dev/information/appli/battlecats/help/index.html";
fn open_battle_help(url: &str) {
    if url == BATTLE_HELP {
        use std::os::windows::process::CommandExt;
        // 対象を固定し、外部ヘルプだけを既定のブラウザで開く。
        let _ = std::process::Command::new("explorer.exe")
            .arg(BATTLE_HELP)
            .creation_flags(0x08000000)
            .spawn();
    }
}

pub fn run(root: PathBuf, region: String, source: String) -> Result<()> {
    let event_loop = EventLoop::new();
    let window = WindowBuilder::new()
        .with_title("KBCS")
        .with_inner_size(tao::dpi::LogicalSize::new(1180.0, 820.0))
        .with_min_inner_size(tao::dpi::LogicalSize::new(760.0, 520.0))
        .build(&event_loop)?;
    let service = Service::new(root.clone(), region, source);
    let mut context = WebContext::new(Some(root.join("webview")));
    let webview = WebViewBuilder::new_with_web_context(&mut context)
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
        if let Event::WindowEvent {
            event: WindowEvent::CloseRequested,
            ..
        } = event
        {
            *control_flow = ControlFlow::Exit;
        }
    });
}
