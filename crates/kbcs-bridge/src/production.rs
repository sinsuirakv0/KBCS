use crate::{random::Random, stage};
use serde::Deserialize;
use std::{any::Any, ffi::c_void, panic::AssertUnwindSafe};

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, Deserialize, PartialEq, Eq)]
pub struct SpawnRequest {
    pub side: i32,
    pub raw: i32,
    pub level_index: i32,
    pub layer_min: i32,
    pub layer_max: i32,
    pub form: i32,
    pub row: i32,
}
#[repr(C)]
#[derive(Clone, Copy, Default)]
pub struct Cost {
    pub enabled: i32,
    pub raw: i32,
    pub talent: i32,
    pub chapter: i32,
    pub multiplier: i32,
    pub fixed: i32,
    pub rarity_rate: i32,
    pub orb_rate: i32,
    pub orb_enabled: i32,
    pub combo_count: i32,
    pub combos: [i32; 32],
}
#[repr(C)]
pub struct Geometry {
    pub stage_width: i32,
    pub castle_slot: i32,
}
#[repr(C)]
#[derive(Deserialize)]
pub struct RechargeInput {
    pub base: i32,
    pub talent: i32,
    pub research_level: i32,
    pub treasure: i32,
    pub combo: i32,
    pub stage_percent: i32,
    pub override_frames: i32,
}
#[repr(C)]
#[derive(Debug, Default, PartialEq, Eq)]
pub struct Placement {
    pub slot: i32,
    pub unit_id: i32,
    pub x: i32,
    pub y: i32,
    pub layer: i32,
}
#[repr(C)]
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub struct State {
    pub money: i32,
    pub wait: [i32; 10],
    pub maximum: [i32; 10],
    pub produced: [i32; 10],
    pub last_cost: [i32; 10],
    pub total: i32,
}
#[repr(C)]
#[derive(Default)]
pub struct DeployInput {
    pub spawn: SpawnRequest,
    pub slot: i32,
    pub present: i32,
    pub allowed: i32,
    pub blocked: i32,
    pub summon_mode: i32,
    pub cost: i32,
    pub recharge: i32,
    // -1は短縮なし。0以上は原本の条件判定を通った短縮率。
    pub reduction: i32,
    pub recharge_enabled: i32,
    pub notify_failure: i32,
}
#[repr(C)]
#[derive(Debug, Default, PartialEq, Eq)]
pub struct DeployOutput {
    pub slot: i32,
    pub sound: i32,
}
#[repr(C)]
#[derive(Debug, Default, PartialEq, Eq)]
pub struct EnemyOutput {
    pub row: i32,
    pub slot: i32,
}
pub struct Start {
    pub global_min: i32,
    pub global_max: i32,
    pub castle_raw: i32,
}

type Constructor = unsafe extern "C" fn(*mut c_void, *const SpawnRequest, *mut u32) -> i32;
unsafe extern "C" {
    fn kbcs_core_spawn_prepare(
        request: *const SpawnRequest,
        geometry: *const Geometry,
        occupied: *const i32,
        seed: *mut u32,
        out: *mut Placement,
    ) -> u32;
    fn kbcs_core_spawn_boss_position(x: i32, scale: i32, offset: i32, out: *mut i32) -> u32;
    fn kbcs_core_production_recharge(input: *const RechargeInput, out: *mut i32) -> u32;
    fn kbcs_core_production_deploy(
        input: *const DeployInput,
        state: *mut State,
        seed: *mut u32,
        construct: Constructor,
        user: *mut c_void,
        out: *mut DeployOutput,
    ) -> u32;
    fn kbcs_core_production_clock(state: *mut State, recharge: *const i32, ready: *mut u32) -> u32;
    fn kbcs_core_production_enemy(
        rows: *const stage::Row,
        states: *mut stage::State,
        count: i32,
        context: *mut stage::Context,
        seed: *mut u32,
        seen: *mut i32,
        seen_count: i32,
        construct: Constructor,
        user: *mut c_void,
        out: *mut EnemyOutput,
    ) -> u32;
    fn kbcs_core_production_start(
        rows: *const stage::Row,
        states: *mut stage::State,
        count: i32,
        global_min: i32,
        global_max: i32,
        castle_raw: i32,
        seed: *mut u32,
        construct: Constructor,
        user: *mut c_void,
        out: *mut stage::StartOutput,
        spawn: *mut EnemyOutput,
    ) -> u32;
}

pub fn prepare(
    request: &SpawnRequest,
    geometry: &Geometry,
    occupied: &[i32; 51],
    random: &mut Random,
) -> Result<Placement, u32> {
    let mut output = Placement::default();
    let code = unsafe {
        kbcs_core_spawn_prepare(
            request,
            geometry,
            occupied.as_ptr(),
            random.state_mut(),
            &mut output,
        )
    };
    result(code, output)
}
pub fn boss_position(x: i32, scale: i32, offset: i32) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_spawn_boss_position(x, scale, offset, &mut output) };
    result(code, output)
}
pub fn clock(state: &mut State, recharge: &[i32; 10]) -> Result<u32, u32> {
    let mut ready = 0;
    let code = unsafe { kbcs_core_production_clock(state, recharge.as_ptr(), &mut ready) };
    result(code, ready)
}
pub fn recharge(input: &RechargeInput) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_production_recharge(input, &mut output) };
    result(code, output)
}

struct Hook<'a, F> {
    constructor: &'a mut F,
    panic: Option<Box<dyn Any + Send>>,
}
unsafe extern "C" fn invoke<F>(
    user: *mut c_void,
    request: *const SpawnRequest,
    seed: *mut u32,
) -> i32
where
    F: FnMut(&SpawnRequest, &mut Random) -> i32,
{
    // C++が同期呼出中だけ借用する。RustのpanicをC ABIの外へ伝播させない。
    let hook = unsafe { &mut *user.cast::<Hook<'_, F>>() };
    let mut random = Random::new(unsafe { *seed }).expect("validated seed");
    let value = std::panic::catch_unwind(AssertUnwindSafe(|| {
        (hook.constructor)(unsafe { &*request }, &mut random)
    }));
    unsafe { *seed = random.state() };
    match value {
        Ok(slot) => slot,
        Err(panic) => {
            hook.panic = Some(panic);
            -1
        }
    }
}
fn construct<F, T>(
    constructor: &mut F,
    call: impl FnOnce(Constructor, *mut c_void) -> (u32, T),
) -> Result<T, u32>
where
    F: FnMut(&SpawnRequest, &mut Random) -> i32,
{
    let mut hook = Hook {
        constructor,
        panic: None,
    };
    let (code, output) = call(invoke::<F>, (&mut hook as *mut Hook<'_, F>).cast());
    if let Some(panic) = hook.panic {
        std::panic::resume_unwind(panic);
    }
    result(code, output)
}
fn result<T>(code: u32, output: T) -> Result<T, u32> {
    if code == 0 { Ok(output) } else { Err(code) }
}

pub fn deploy(
    input: &DeployInput,
    state: &mut State,
    random: &mut Random,
    constructor: &mut impl FnMut(&SpawnRequest, &mut Random) -> i32,
) -> Result<DeployOutput, u32> {
    construct(constructor, |callback, user| {
        let mut output = DeployOutput::default();
        let code = unsafe {
            kbcs_core_production_deploy(
                input,
                state,
                random.state_mut(),
                callback,
                user,
                &mut output,
            )
        };
        (code, output)
    })
}

pub fn enemy_tick(
    rows: &[stage::Row],
    states: &mut [stage::State],
    context: &mut stage::Context,
    seen: &mut [i32],
    random: &mut Random,
    constructor: &mut impl FnMut(&SpawnRequest, &mut Random) -> i32,
) -> Result<EnemyOutput, u32> {
    if rows.len() != states.len() || rows.len() > 4096 || seen.len() > i32::MAX as usize {
        return Err(1);
    }
    construct(constructor, |callback, user| {
        let mut output = EnemyOutput::default();
        let code = unsafe {
            kbcs_core_production_enemy(
                rows.as_ptr(),
                states.as_mut_ptr(),
                rows.len() as i32,
                context,
                random.state_mut(),
                seen.as_mut_ptr(),
                seen.len() as i32,
                callback,
                user,
                &mut output,
            )
        };
        (code, output)
    })
}

pub fn start(
    rows: &[stage::Row],
    states: &mut [stage::State],
    input: &Start,
    random: &mut Random,
    constructor: &mut impl FnMut(&SpawnRequest, &mut Random) -> i32,
) -> Result<(stage::StartOutput, EnemyOutput), u32> {
    if rows.len() != states.len() || rows.len() > 4096 {
        return Err(1);
    }
    construct(constructor, |callback, user| {
        let mut output = stage::StartOutput::default();
        let mut spawn = EnemyOutput::default();
        let code = unsafe {
            kbcs_core_production_start(
                rows.as_ptr(),
                states.as_mut_ptr(),
                rows.len() as i32,
                input.global_min,
                input.global_max,
                input.castle_raw,
                random.state_mut(),
                callback,
                user,
                &mut output,
                &mut spawn,
            )
        };
        (code, (output, spawn))
    })
}

#[cfg(test)]
mod tests;
