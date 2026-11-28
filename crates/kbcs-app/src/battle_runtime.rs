#[cfg(target_os = "emscripten")]
use super::native;
use super::{ActorDrawRanges, Request, Session};
use anyhow::{Result, ensure};
use kbcs_bridge::battle::{Outcome, Rewards};
use serde_json::{Value, json};
use std::time::Instant;

#[derive(serde::Serialize)]
pub struct BattleFrame<'a> {
    #[serde(flatten)]
    pub battle: kbcs_bridge::battle_screen::Frame,
    pub scene: Option<crate::scene::Frame<'a>>,
    #[serde(rename = "coreMs")]
    pub core_ms: f64,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub runtime: Option<Value>,
    #[serde(skip)]
    pub preview: Option<[usize; 2]>,
}

#[derive(Default, serde::Deserialize, serde::Serialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Observation {
    pub inspection: Option<Vec<super::inspector::Query>>,
    pub focus_actor: Option<i32>,
}

#[derive(serde::Deserialize)]
#[serde(deny_unknown_fields)]
pub struct KeyInput {
    pub session: String,
    control: i32,
    cheats: u32,
    #[serde(default)]
    phase: i32,
    #[serde(default)]
    x: i32,
    #[serde(default)]
    y: i32,
}

#[derive(serde::Deserialize, serde::Serialize)]
#[serde(tag = "kind", rename_all = "camelCase", deny_unknown_fields)]
pub enum Settlement {
    Reward { outcome: Outcome, rewards: Rewards },
    Continue { attempt: u32 },
}

#[derive(serde::Deserialize, serde::Serialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct SettlementReply {
    pub paid: Option<bool>,
    pub balance: Option<i64>,
    pub error: Option<String>,
    pub receipt: Option<Value>,
}

pub fn popup_layouts(bytes: &[u8]) -> Result<Vec<kbcs_bridge::battle::PopupLayout>> {
    let inputs: Vec<kbcs_bridge::battle::PopupInput> = serde_json::from_slice(bytes)?;
    ensure!(inputs.len() <= 64, "通知配置が多すぎます");
    inputs
        .iter()
        .map(|input| {
            kbcs_bridge::battle::popup_layout(input).map_err(|c| anyhow::anyhow!("通知配置: {c}"))
        })
        .collect()
}

impl Session {
    #[cfg(target_os = "emscripten")]
    pub fn settlement_request(&self, attempt: u32) -> Result<Option<Settlement>> {
        let outcome = native(self.core.outcome())?;
        if outcome.mode == 0 || self.saved.is_some() {
            return Ok(None);
        }
        if self.data.continue_text.is_some() && outcome.mode == 2 {
            match native(self.core.ending())?.phase {
                0..=2 => return Ok(None),
                3 => {
                    return Ok((native(self.core.continue_view())?.pending != 0)
                        .then_some(Settlement::Continue { attempt }));
                }
                _ => {}
            }
        }
        let rewards = native(self.core.rewards())?;
        Ok((rewards.ready != 0).then_some(Settlement::Reward { outcome, rewards }))
    }

    #[cfg(target_os = "emscripten")]
    pub fn apply_settlement(&mut self, reply: SettlementReply) -> Result<()> {
        if let Some(paid) = reply.paid {
            native(self.core.continue_payment(paid))?;
            self.continue_balance = reply.balance;
            self.continue_error = reply.error.or_else(|| {
                self.data
                    .continue_text
                    .as_ref()
                    .filter(|_| !paid)
                    .map(|(_, error)| error.clone())
            });
        } else {
            if let Some(notifications) = reply
                .receipt
                .as_ref()
                .and_then(|saved| saved["notifications"].as_array())
                .filter(|list| !list.is_empty())
            {
                native(self.core.notifications(notifications.len() as i32))?;
            }
            self.saved = reply.receipt;
            self.receipt_error = reply.error;
        }
        Ok(())
    }

    #[cfg(target_os = "emscripten")]
    pub fn set_continue_balance(&mut self, balance: Option<i64>) {
        self.continue_balance = balance;
    }
}

pub fn encode_mobile(mut frame: BattleFrame<'_>, started: Instant) -> Result<Vec<u8>> {
    let commands = frame
        .scene
        .as_mut()
        .map(|scene| {
            scene.textures = &[];
            std::mem::take(&mut scene.commands)
        })
        .unwrap_or_default();
    crate::battle_wire::encode_mobile(&frame, &commands, started)
}
impl Session {
    pub fn input(&mut self, request: KeyInput) -> Result<Value> {
        let session = self;
        ensure!(
            request.control == 2
                || request.control == 4
                || request.control == 11
                || request.control >= 1000,
            "戦闘キー操作が不正です"
        );
        session
            .core
            .cheats(request.cheats)
            .map_err(|code| anyhow::anyhow!("チート設定: {code}"))?;
        // 描画RPC待ちのキーをUIへ貯めない。論理F・シーン計算を進めず入力だけを処理する。
        let frame = session
            .core
            .advance(&kbcs_bridge::battle_screen::Input {
                control: request.control,
                phase: request.phase,
                x: request.x,
                y: request.y,
                ..Default::default()
            })
            .map_err(|code| anyhow::anyhow!("戦闘キー操作: {code}"))?;
        let sounds = session
            .core
            .sounds()
            .map_err(|code| anyhow::anyhow!("戦闘音源: {code}"))?;
        Ok(json!({"state":frame.state,"layout":frame.layout,"sounds":sounds}))
    }

    pub fn frame<'a>(
        &'a mut self,
        request: &mut Request,
        observation: Option<&Observation>,
        started: Instant,
        settle: impl FnOnce(&mut Self) -> Result<()>,
    ) -> Result<BattleFrame<'a>> {
        let session = self;
        ensure!(
            request.scene.key() == session.data.key,
            "戦闘中のステージ変更はできません"
        );
        session
            .core
            .cheats(request.cheats)
            .map_err(|code| anyhow::anyhow!("チート設定: {code}"))?;
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
        settle(session)?;
        let mut runtime = session.stats(request.compact && !request.debug)?;
        if let Some(query) = request
            .inspection
            .as_ref()
            .or_else(|| observation.and_then(|view| view.inspection.as_ref()))
        {
            runtime["inspection"] = session.inspection(query)?;
        }
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
        if request.debug {
            let extra: Vec<_> = session.core.active_actors().map_err(|code| anyhow::anyhow!("追加個体読取: {code}"))?.into_iter().filter(|value| value.slot >= 51).map(|value| json!({"side":value.side,"slot":value.slot,"words":value.actor.words.as_slice()})).collect();
            if !extra.is_empty() {
                runtime["extraWords"] = json!(extra);
            }
        }
        request.scene.frame = battle.state.frame;
        session.combo_skipped |= request.skip_combos;
        session.ending_camera(&mut request.scene)?;
        // 描画がSceneを借用する前に、同じ配置でHUDを作る。
        let hud_layout = session.layout(&request.scene)?;
        let (hud, hud_json) = session.hud(&hud_layout)?;
        runtime["hud"] = hud_json;
        // 006d6d04は倍速分の論理更新に入る前にコンボの時計を1回だけ進める。
        let combo_frame = battle.state.hud_frame;
        runtime["comboIntro"] = session.combo_intro(combo_frame, request.scene.viewport_width)?;
        let mut ranges = ActorDrawRanges::default();
        if let Some(id) = request
            .focus_actor
            .or_else(|| observation.and_then(|view| view.focus_actor))
            && let Some((actor, value)) = session.focused_actor(id)?
        {
            if actor.retired_frame < 0 {
                ranges.focus = Some((actor.side as usize, actor.slot as usize));
            }
            runtime["focusedActor"] = value;
        }
        let show_health = runtime["result"]["mode"] == 0 || runtime["ending"]["phase"] == 0;
        let frame = session.draw(
            &request.scene,
            combo_frame,
            show_health.then_some(&hud),
            &mut ranges,
        )?;
        Ok(BattleFrame {
            battle,
            scene: Some(frame),
            runtime: Some(runtime),
            core_ms,
            preview: ranges.preview,
        })
    }
}
