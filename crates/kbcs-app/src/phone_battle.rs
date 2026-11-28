use anyhow::{Result, ensure};
use serde_json::{Value, json};
use std::{
    collections::VecDeque,
    sync::{
        Condvar, Mutex,
        atomic::{AtomicBool, Ordering},
    },
    time::{Duration, Instant},
};

#[derive(Default)]
pub struct Exchange {
    state: Mutex<State>,
    wake: Condvar,
}

#[derive(Default)]
struct State {
    generation: u64,
    battle: Option<Battle>,
    commands: VecDeque<Value>,
    launch: Option<Instant>,
    error: Option<String>,
    redraw: bool,
}

struct Battle {
    id: String,
    start: Value,
    frame: Value,
    sample: Option<Instant>,
    query: Query,
    local: bool,
}

pub use crate::battle::runtime::Observation as Query;

impl Exchange {
    pub fn reset(&self) {
        let mut state = self.state.lock().unwrap();
        *state = State {
            generation: state.generation.wrapping_add(1),
            ..State::default()
        };
        self.wake.notify_all();
    }

    pub fn generation(&self) -> u64 {
        self.state.lock().unwrap().generation
    }

    pub fn command(&self, value: Value) -> Result<()> {
        let mut state = self.state.lock().unwrap();
        ensure!(state.commands.len() < 32, "スマホの操作が混み合っています");
        match value["type"].as_str() {
            Some("launch") => {
                ensure!(
                    state.battle.is_none() && state.launch.is_none(),
                    "スマホにて出撃準備中です"
                );
                ensure!(value["snapshot"].is_object(), "出撃準備の指定がありません");
                state.launch = Some(Instant::now());
                state.error = None;
            }
            Some("action" | "setting" | "key") => {
                ensure!(
                    state
                        .battle
                        .as_ref()
                        .is_some_and(|battle| value["id"] == battle.id),
                    "スマホの戦闘は終了しました"
                );
            }
            _ => anyhow::bail!("スマホの操作が不正です"),
        }
        state.commands.push_back(value);
        self.wake.notify_one();
        Ok(())
    }

    pub fn commands(&self, active: &AtomicBool) -> VecDeque<Value> {
        let state = self.state.lock().unwrap();
        let (mut state, _) = self
            .wake
            .wait_timeout_while(state, Duration::from_secs(2), |state| {
                state.commands.is_empty() && !state.redraw && active.load(Ordering::Acquire)
            })
            .unwrap();
        if !active.load(Ordering::Acquire) {
            return VecDeque::new();
        }
        let mut commands = std::mem::take(&mut state.commands);
        if std::mem::take(&mut state.redraw) {
            if let Some(battle) = state.battle.as_mut().filter(|battle| battle.local) {
                commands.push_back(json!({"type":"observe","query":{
                    "inspection":battle.query.inspection.take(),"focusActor":battle.query.focus_actor
                }}));
            } else {
                commands.push_back(json!({"type":"observe"}));
            }
        }
        commands
    }

    pub fn register(&self, generation: u64, id: String, start: Value, local: bool) -> Result<()> {
        let mut state = self.state.lock().unwrap();
        ensure!(
            state.generation == generation,
            "スマホの表示先が変更されました"
        );
        ensure!(
            state.battle.is_none(),
            "スマホの戦闘を終了してから出撃してください"
        );
        state.launch = None;
        state.error = None;
        state.commands.clear();
        state.battle = Some(Battle {
            id,
            start,
            frame: Value::Null,
            sample: None,
            query: Query::default(),
            local,
        });
        Ok(())
    }

    pub fn close(&self, id: &str) {
        let mut state = self.state.lock().unwrap();
        if state.battle.as_ref().is_some_and(|battle| battle.id == id) {
            state.battle = None;
            state.commands.clear();
        }
    }

    pub fn fail(&self, message: &str) {
        let mut state = self.state.lock().unwrap();
        state.launch = None;
        state.error = Some(message.chars().take(500).collect());
        state.commands.clear();
    }

    pub fn status(&self, known: Option<&str>) -> Value {
        let mut state = self.state.lock().unwrap();
        if state
            .launch
            .is_some_and(|start| start.elapsed() >= Duration::from_secs(120))
        {
            state.launch = None;
            state.commands.clear();
            state.error = Some("スマホから出撃準備の応答がありません".into());
        }
        let loading = state.launch.is_some()
            || state
                .battle
                .as_ref()
                .is_some_and(|battle| battle.frame.is_null());
        let battle = state
            .battle
            .as_ref()
            .filter(|battle| !battle.frame.is_null());
        json!({"loading":loading,"error":state.error,"id":battle.map(|battle| &battle.id),
            "start":battle.filter(|battle| Some(battle.id.as_str()) != known).map(|battle| &battle.start)})
    }

    pub fn observe(&self, id: &str, query: Query) -> Value {
        let mut state = self.state.lock().unwrap();
        let error = state.error.clone();
        let Some(battle) = state.battle.as_mut().filter(|battle| battle.id == id) else {
            return Value::Null;
        };
        let redraw = query.inspection.is_some() || battle.query.focus_actor != query.focus_actor;
        if query.inspection.is_some() {
            battle.query.inspection = query.inspection;
        }
        battle.query.focus_actor = query.focus_actor;
        let mut frame = battle.frame.clone();
        if error.is_some() {
            frame["error"] = json!(error);
        }
        if redraw {
            state.redraw = true;
            self.wake.notify_one();
        }
        frame
    }

    pub fn query(&self, id: &str) -> Option<Query> {
        let mut state = self.state.lock().unwrap();
        let battle = state.battle.as_mut().filter(|battle| battle.id == id && !battle.local)?;
        let now = Instant::now();
        if battle
            .sample
            .is_some_and(|last| now.duration_since(last) < Duration::from_millis(75))
        {
            return None;
        }
        battle.sample = Some(now);
        Some(Query {
            inspection: battle.query.inspection.take(),
            focus_actor: battle.query.focus_actor,
        })
    }

    pub fn publish(&self, id: &str, mut frame: Value) {
        let mut state = self.state.lock().unwrap();
        if let Some(battle) = state.battle.as_mut().filter(|battle| battle.id == id) {
            if frame["runtime"]["inspection"].is_null() {
                frame["runtime"]["inspection"] =
                    std::mem::take(&mut battle.frame["runtime"]["inspection"]);
            }
            if frame["phoneStats"].is_null() {
                frame["phoneStats"] = std::mem::take(&mut battle.frame["phoneStats"]);
            }
            battle.frame = frame;
        }
    }
}

#[test]
fn local_battle_sends_inspection_to_the_phone() {
    let exchange = Exchange::default();
    exchange
        .register(exchange.generation(), "local".into(), Value::Null, true)
        .unwrap();
    let query = serde_json::from_value(json!({"focusActor":7,"inspection":[
        {"side":0,"group":"present","offset":0,"selected":7,"revision":1}
    ]})).unwrap();
    exchange.observe("local", query);
    let commands = exchange.commands(&AtomicBool::new(true));
    assert_eq!(commands[0]["query"]["focusActor"], 7);
    assert_eq!(commands[0]["query"]["inspection"][0]["revision"], 1);
    assert!(exchange.query("local").is_none());
}

#[test]
fn desktop_observes_only_the_current_prepared_battle() {
    let exchange = Exchange::default();
    let generation = exchange.generation();
    exchange.reset();
    assert!(
        exchange
            .register(generation, "old".into(), Value::Null, false)
            .is_err()
    );
    exchange
        .register(
            exchange.generation(),
            "active".into(),
            json!({"textures":[]}),
            false,
        )
        .unwrap();
    assert_eq!(exchange.status(None)["loading"], true);
    assert!(exchange.status(None)["id"].is_null());
    exchange.publish("active", json!({"state":{"frame":10},"runtime":{}}));
    assert_eq!(exchange.status(None)["id"], "active");
    assert_eq!(
        exchange.observe("active", Query::default())["state"]["frame"],
        10
    );
    assert!(
        exchange
            .command(json!({"type":"action","id":"old","action":"toggle"}))
            .is_err()
    );
    exchange
        .command(json!({"type":"action","id":"active","action":"toggle"}))
        .unwrap();
    assert_eq!(
        exchange.commands(&AtomicBool::new(true))[0]["action"],
        "toggle"
    );
    exchange.close("active");
    assert!(exchange.status(None)["id"].is_null());
}
