#[cfg(target_os = "emscripten")]
mod battle;
#[cfg(target_os = "emscripten")]
mod battle_wire;
#[cfg(target_os = "emscripten")]
mod scene;

fn main() {}

#[cfg(target_os = "emscripten")]
mod exports {
    use crate::battle::{
        Prepared, Request, Session,
        runtime::{Observation, encode_mobile},
    };
    use anyhow::{Context, Result};
    use serde::Deserialize;
    use std::{cell::RefCell, time::Instant};

    #[derive(Default)]
    struct Runtime {
        input: Vec<u8>,
        output: Vec<u8>,
        session: Option<Session>,
        attempt: u32,
    }
    thread_local! {
        static RUNTIME: RefCell<Runtime> = RefCell::new(Runtime::default());
    }

    #[unsafe(no_mangle)]
    pub extern "C" fn kbcs_phone_input(length: u32) -> *mut u8 {
        RUNTIME.with_borrow_mut(|state| {
            state.input.resize(length as usize, 0);
            state.input.as_mut_ptr()
        })
    }

    #[unsafe(no_mangle)]
    pub extern "C" fn kbcs_phone_output() -> *const u8 {
        RUNTIME.with_borrow(|state| state.output.as_ptr())
    }

    #[unsafe(no_mangle)]
    pub extern "C" fn kbcs_phone_length() -> u32 {
        RUNTIME.with_borrow(|state| state.output.len() as u32)
    }

    #[unsafe(no_mangle)]
    pub extern "C" fn kbcs_phone_call(operation: u32) -> u32 {
        RUNTIME.with_borrow_mut(|state| match state.call(operation) {
            Ok(output) => {
                state.output = output;
                0
            }
            Err(error) => {
                state.output = format!("{error:#}").into_bytes();
                1
            }
        })
    }

    #[derive(Deserialize)]
    #[serde(rename_all = "camelCase")]
    struct Start {
        prepared: Prepared,
        continue_balance: Option<i64>,
        metadata: serde_json::Value,
    }

    #[derive(Deserialize)]
    struct Update {
        request: Request,
        observation: Option<Observation>,
    }

    impl Runtime {
        fn call(&mut self, operation: u32) -> Result<Vec<u8>> {
            let started = Instant::now();
            if operation == 0 {
                let start: Start = serde_json::from_slice(&self.input)?;
                let mut session = start.prepared.start()?;
                session.set_continue_balance(start.continue_balance);
                self.session = Some(session);
                self.attempt = 1;
                self.input = Vec::new();
                return Ok(serde_json::to_vec(&start.metadata)?);
            }
            let session = self
                .session
                .as_mut()
                .context("スマホの戦闘がまだ始まっていません")?;
            match operation {
                1 => {
                    let mut update: Update = serde_json::from_slice(&self.input)?;
                    let attempt = self.attempt;
                    let mut settlement = None;
                    let mut frame = session.frame(
                        &mut update.request,
                        update.observation.as_ref(),
                        started,
                        |session| {
                            settlement = session.settlement_request(attempt)?;
                            Ok(())
                        },
                    )?;
                    let runtime = frame.runtime.as_mut().unwrap();
                    if let Some([start, end]) = frame.preview {
                        runtime["focusedDrawRange"] = serde_json::json!([start, end]);
                    }
                    if let Some(settlement) = settlement {
                        runtime["settlement"] = serde_json::to_value(settlement)?;
                    }
                    encode_mobile(frame, started)
                }
                2 => Ok(serde_json::to_vec(
                    &session.input(serde_json::from_slice(&self.input)?)?,
                )?),
                3 => {
                    let reply: crate::battle::runtime::SettlementReply =
                        serde_json::from_slice(&self.input)?;
                    if reply.paid.is_some() {
                        self.attempt += 1;
                    }
                    session.apply_settlement(reply)?;
                    Ok(Vec::new())
                }
                4 => Ok(serde_json::to_vec(&crate::battle::runtime::popup_layouts(
                    &self.input,
                )?)?),
                _ => anyhow::bail!("スマホの戦闘操作が不正です"),
            }
        }
    }
}
