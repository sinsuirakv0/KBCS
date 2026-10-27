use crate::{production::SpawnRequest, random::Random, stage};

use std::{any::Any, ffi::c_void, panic::AssertUnwindSafe};

pub const WORDS: usize = 251;
pub const COLUMNS: usize = 119;
pub const SKILLS: usize = 73;
pub const ORBS: usize = 32;
pub const SLOTS: usize = 51;

mod secondary;
pub use secondary::*;
mod hit;
pub use hit::*;
mod wave;
pub use wave::*;

// 006e9c88の抽選順。命中後の効果適用・耐性判定とは分離する。
#[derive(Clone, Copy)]
#[repr(usize)]
pub enum Proc {
    Critical,
    Knockback,
    Stop,
    Slow,
    Weaken,
    Savage,
    Warp,
    BarrierBreaker,
    Curse,
    Poison,
    ShieldBreaker,
    ProductionDelay,
}
#[derive(Debug, PartialEq, Eq)]
pub struct AttackRoll(pub [i32; 12]);
impl AttackRoll {
    pub fn active(&self, effect: Proc) -> bool {
        self.0[effect as usize] != 0
    }
}

#[repr(C)]
#[derive(Default, serde::Deserialize)]
pub struct EffectContext {
    pub fruit: i32,
    // 0063a050の200/202/204/206。鈍足・停止・弱体・呪いの1/10000軽減。
    pub base_reductions: [i32; 4],
    pub sage: [i32; 11],
    pub notifications: i32,
    pub target_count: i32,
    pub scenario_level: i32,
}
#[repr(C)]
#[derive(Default, Debug)]
pub struct EffectEvents {
    pub count: i32,
    pub events: [[i32; 2]; 16],
}
#[repr(C)]
pub struct Clock {
    pub encoded: [i32; 4],
    pub plain: [i32; 4],
    pub forms: [[i32; SLOTS]; 2],
    pub kill_orb: [i32; SLOTS],
    pub kill_threshold: i32,
}
#[repr(C)]
#[derive(Default, serde::Deserialize)]
pub struct Motion {
    pub encoded: [i32; 8],
    pub plain: [i32; 8],
    pub soul_frames: i32,
}
#[repr(C)]
#[derive(Default, Debug)]
pub struct Protection {
    pub shield_hit: i32,
    pub sound_count: i32,
    pub sounds: [i32; 2],
    pub visual_count: i32,
    // 種別（0:バリア、1:盾）、内部X/Y、ブレイカーの印。描画プールへの登録は別。
    pub visuals: [[i32; 4]; 2],
}
#[repr(C)]
#[derive(serde::Deserialize)]
pub struct Health {
    pub deployment_slot: i32,
    pub cooldown: i32,
    pub preserve_enemy_castle: i32,
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct HealthResult {
    pub previous_hp: i32,
    pub delay_slot: i32,
    pub delay_frames: i32,
    pub delay_x: i32,
    pub delay_y: i32,
    pub sound: i32,
}
#[repr(C)]
#[derive(serde::Deserialize)]
pub struct Reaction {
    pub previous_hp: i32,
    pub death_visual_available: i32,
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct ReactionResult {
    pub sound_count: i32,
    pub sounds: [i32; 2],
    pub death_visual: i32,
    pub death_x: i32,
    pub death_y: i32,
}
#[repr(C)]
#[derive(serde::Deserialize)]
pub struct Knockback {
    pub boundary: i32,
    pub cost: i32,
    pub quiet: i32,
    pub game_mode: i32,
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct KnockbackResult {
    pub handled: i32,
    pub refund: i32,
    pub sound: i32,
}
pub struct Damage {
    pub side: i32,
    pub slot: i32,
    pub amount: i32,
    pub guard_enabled: bool,
    pub notice: [i32; 2],
}
#[repr(C)]
struct DamageContext {
    guard_enabled: i32,
    notice: [i32; 2],
    rows: *const stage::Row,
    states: *const stage::State,
    count: i32,
}
#[derive(Clone, Copy)]
#[repr(usize)]
pub enum Effect {
    Knockback,
    Stop,
    Slow,
    Weaken,
    Warp,
    Curse,
    ProductionDelay,
}

#[repr(C)]
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Actor {
    pub words: [i32; WORDS],
}
impl Default for Actor {
    fn default() -> Self {
        Self { words: [0; WORDS] }
    }
}

#[repr(C)]
#[derive(Clone)]
pub struct Definition {
    pub cells: [i32; COLUMNS],
    pub count: i32,
    pub growth: [i32; 20],
    pub talents: [[i32; 4]; SKILLS],
    pub talent_active: [i32; SKILLS],
    pub talent_min_level: [i32; SKILLS],
    pub added_targets: i32,
    pub orb_enabled: i32,
    pub orbs: [[i32; 4]; ORBS],
    pub orb_present: [i32; ORBS],
    pub speed_rule: i32,
    pub speed_value: i32,
}
impl Definition {
    pub fn from_raw(raw: &[i32], unit: bool) -> Result<Self, u32> {
        let count = i32::try_from(raw.len()).map_err(|_| 1_u32)?;
        let mut value = Self {
            cells: [0; COLUMNS],
            count: count.min(if unit { 119 } else { 113 }),
            growth: [0; 20],
            talents: [[0; 4]; SKILLS],
            talent_active: [0; SKILLS],
            talent_min_level: [0; SKILLS],
            added_targets: 0,
            orb_enabled: 0,
            orbs: [[0; 4]; ORBS],
            orb_present: [0; ORBS],
            speed_rule: 0,
            speed_value: 0,
        };
        let code = unsafe {
            kbcs_core_actor_load(
                raw.as_ptr(),
                count,
                i32::from(unit),
                value.cells.as_mut_ptr(),
            )
        };
        if code == 0 { Ok(value) } else { Err(code) }
    }
}

#[repr(C)]
#[derive(Clone, Default, serde::Deserialize)]
pub struct Environment {
    pub unit_modes: [i32; 2],
    pub stage_width: i32,
    pub castle_slot: i32,
    pub castle_x: i32,
    pub castle_scale: i32,
    pub castle_offset: i32,
    pub stage_kind: i32,
    pub zombie: i32,
    pub chapter_rate: i32,
    pub crown: i32,
    pub hp_percent: i32,
    pub attack_percent: i32,
    pub crystal_max: [i32; 5],
    pub crystal: [i32; 5],
    pub treasures: [i32; 32],
    pub combos: [i32; 32],
    pub orb_stage: i32,
    pub talents_disabled: i32,
    pub parameters: [i32; 2],
    pub spawned: [i32; 2],
    pub spawn_row: [i32; 14],
    pub special_castle: i32,
}

#[repr(C)]
#[derive(Clone, Copy, Default, serde::Deserialize)]
pub struct EnemyDeath {
    pub boundary: i32,
    pub quiet: i32,
    pub game_mode: i32,
    pub money_base: i32,
    pub accounting_level: i32,
    pub score_enabled: i32,
    pub notifications: i32,
    pub money_disabled: i32,
    pub recording: i32,
    pub timer: i32,
    pub limit: i32,
    pub score: i32,
    pub cohort_present: i32,
}
#[repr(C)]
struct EnemyDeathContext {
    input: EnemyDeath,
    cohort_count: i32,
    cohort: *const i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct EnemyDeathResult {
    pub score_display: u64,
    pub handled: i32,
    pub money: i32,
    pub selected_bonus_slot: i32,
    pub bonus_visual_slot: i32,
    pub erase_cohort: i32,
    pub cohort_serial: i32,
    pub score: i32,
    pub score_updated: i32,
    pub record_requested: i32,
    pub record_values: [i32; 2],
    pub sound: i32,
}

#[repr(C)]
#[derive(Default, serde::Deserialize)]
pub struct Retirement {
    pub blocked: i32,
    pub body_frames: i32,
    pub soul_frames: i32,
    pub production_slot: i32,
    pub cannon_base: i32,
    pub cannon_remaining: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct RetirementResult {
    pub handled: i32,
    pub removed: i32,
    pub death_notice: i32,
    pub reset_production: i32,
    pub production_slot: i32,
    pub cannon_remaining: i32,
}

#[repr(C)]
struct RawAttackSelection {
    side: i32,
    slot: i32,
    hit: i32,
    count: i32,
    targets: [i32; SLOTS],
}
impl RawAttackSelection {
    fn new(selection: AttackSelection<'_>) -> Result<Self, u32> {
        if selection.targets.len() > SLOTS {
            return Err(1);
        }
        let mut raw = Self {
            side: selection.side,
            slot: selection.slot,
            hit: selection.hit,
            count: selection.targets.len() as i32,
            targets: [0; SLOTS],
        };
        raw.targets[..selection.targets.len()].copy_from_slice(selection.targets);
        Ok(raw)
    }
}
pub struct AttackSelection<'a> {
    pub side: i32,
    pub slot: i32,
    pub hit: i32,
    pub targets: &'a [i32],
}
#[repr(C)]
#[derive(Default)]
pub struct AttackResult {
    pub handled: i32,
    pub emitted: i32,
}
#[repr(C)]
#[derive(Clone, Copy, Debug, serde::Serialize, serde::Deserialize)]
pub struct DirectHit {
    pub side: i32,
    pub slot: i32,
    pub target: i32,
    pub hit: i32,
    pub kind: i32,
    pub parameter: i32,
    pub rate: i32,
    pub flags: [i32; 12],
}
#[repr(C)]
#[derive(Default, serde::Serialize, serde::Deserialize)]
pub struct Emission {
    pub flags: [i32; 12],
    pub parameter: i32,
}
#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, serde::Serialize, serde::Deserialize)]
pub struct Surge {
    pub side: i32,
    pub slot: i32,
    pub frame: i32,
    pub x: i32,
    pub level: i32,
    pub hit: i32,
    pub flags: [u8; 12],
    pub parameter: i32,
    pub mini: u8,
    pub reserved: [u8; 3],
    pub kind: i32,
}
#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, serde::Serialize, serde::Deserialize)]
pub struct Explosion {
    pub side: i32,
    pub slot: i32,
    pub frame: i32,
    pub x: i32,
    pub hit: i32,
    pub flags: [u8; 12],
    pub parameter: i32,
}
#[repr(C)]
#[derive(Debug, Default, serde::Serialize)]
pub struct AreaEmission {
    pub surge_present: i32,
    pub explosion_present: i32,
    pub surge: Surge,
    pub explosion: Explosion,
}
// 直接命中→波動の後。同じRNGを使い、次の攻撃段の前に生成記録を登録する。
pub fn emit_area(
    actors: &[[Actor; SLOTS]; 2],
    environment: &Environment,
    source: AttackSelection<'_>,
    emission: &Emission,
    random: &mut Random,
) -> Result<AreaEmission, u32> {
    let raw = RawAttackSelection::new(source)?;
    let mut out = AreaEmission::default();
    let code = unsafe {
        kbcs_core_actor_emit_area(
            actors.as_ptr(),
            environment,
            &raw,
            emission,
            random.state_mut(),
            &mut out,
        )
    };
    if code == 0 { Ok(out) } else { Err(code) }
}
#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq, serde::Serialize, serde::Deserialize)]
pub struct Wave {
    pub side: i32,
    pub slot: i32,
    pub state: i32,
    pub frame: i32,
    pub x: i32,
    pub level: i32,
    pub hit: i32,
    pub flags: [u8; 12],
    pub parameter: i32,
    pub mini: u8,
    pub reserved: [u8; 3],
}
#[repr(C)]
struct WaveState {
    records: [Wave; 200],
    hits: [[u8; 200]; SLOTS],
}
pub struct Waves(Box<WaveState>);
impl Default for Waves {
    fn default() -> Self {
        Self(Box::new(WaveState {
            records: [Wave::default(); 200],
            hits: [[0; 200]; SLOTS],
        }))
    }
}
impl Waves {
    pub fn records(&self) -> &[Wave; 200] {
        &self.0.records
    }
    pub fn emit(
        &mut self,
        actors: &[[Actor; SLOTS]; 2],
        environment: &Environment,
        source: AttackSelection<'_>,
        emission: &Emission,
        random: &mut Random,
    ) -> Result<i32, u32> {
        let raw = RawAttackSelection::new(source)?;
        let mut slot = -1;
        let code = unsafe {
            kbcs_core_actor_emit_wave(
                actors.as_ptr(),
                environment,
                &raw,
                emission,
                self.0.as_mut(),
                random.state_mut(),
                &mut slot,
            )
        };
        if code == 0 { Ok(slot) } else { Err(code) }
    }
}
type HitSink = unsafe extern "C" fn(
    *mut c_void,
    *mut [Actor; SLOTS],
    *mut u32,
    *const DirectHit,
    *mut i32,
) -> u32;
type AttackSink = unsafe extern "C" fn(
    *mut c_void,
    *mut [Actor; SLOTS],
    *mut u32,
    *const RawAttackSelection,
) -> u32;
struct AttackHook<'a, F> {
    sink: &'a mut F,
    panic: Option<Box<dyn Any + Send>>,
}
unsafe extern "C" fn apply_hit<F, H>(
    user: *mut c_void,
    actors: *mut [Actor; SLOTS],
    seed: *mut u32,
    hit: *const H,
    applied: *mut i32,
) -> u32
where
    F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, &H) -> Result<bool, u32>,
{
    let hook = unsafe { &mut *user.cast::<AttackHook<'_, F>>() };
    let mut random = match Random::new(unsafe { *seed }) {
        Ok(value) => value,
        Err(code) => return code,
    };
    let result = std::panic::catch_unwind(AssertUnwindSafe(|| {
        (hook.sink)(
            unsafe { &mut *actors.cast::<[[Actor; SLOTS]; 2]>() },
            &mut random,
            unsafe { &*hit },
        )
    }));
    unsafe { *seed = random.state() };
    match result {
        Ok(Ok(value)) => {
            unsafe { *applied = i32::from(value) };
            0
        }
        Ok(Err(code)) => {
            if code == 0 {
                1
            } else {
                code
            }
        }
        Err(panic) => {
            hook.panic = Some(panic);
            u32::MAX
        }
    }
}
// attackの同期callback内でも、同じ個体プールとRNGをそのまま再借用できる。
pub fn emit_direct<F>(
    actors: &mut [[Actor; SLOTS]; 2],
    environment: &Environment,
    selection: AttackSelection<'_>,
    random: &mut Random,
    sink: &mut F,
) -> Result<Emission, u32>
where
    F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, &DirectHit) -> Result<bool, u32>,
{
    let raw = RawAttackSelection::new(selection)?;
    let mut hook = AttackHook { sink, panic: None };
    let mut out = Emission::default();
    let code = unsafe {
        kbcs_core_actor_emit_direct(
            actors.as_mut_ptr(),
            environment,
            &raw,
            random.state_mut(),
            apply_hit::<F, DirectHit>,
            (&mut hook as *mut AttackHook<'_, F>).cast(),
            &mut out,
        )
    };
    if let Some(panic) = hook.panic {
        std::panic::resume_unwind(panic);
    }
    if code == 0 { Ok(out) } else { Err(code) }
}
unsafe extern "C" fn emit_attack<F>(
    user: *mut c_void,
    actors: *mut [Actor; SLOTS],
    seed: *mut u32,
    raw: *const RawAttackSelection,
) -> u32
where
    F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, AttackSelection<'_>) -> Result<(), u32>,
{
    let hook = unsafe { &mut *user.cast::<AttackHook<'_, F>>() };
    let raw = unsafe { &*raw };
    if !(1..=51).contains(&raw.count) {
        return 1;
    }
    let mut random = match Random::new(unsafe { *seed }) {
        Ok(value) => value,
        Err(code) => return code,
    };
    // C++が状態を触らない同期呼出の間だけ再借用し、panicをC ABIの外へ出さない。
    let result = std::panic::catch_unwind(AssertUnwindSafe(|| {
        (hook.sink)(
            unsafe { &mut *actors.cast::<[[Actor; SLOTS]; 2]>() },
            &mut random,
            AttackSelection {
                side: raw.side,
                slot: raw.slot,
                hit: raw.hit,
                targets: &raw.targets[..raw.count as usize],
            },
        )
    }));
    unsafe { *seed = random.state() };
    match result {
        Ok(Ok(())) => 0,
        Ok(Err(code)) => {
            if code == 0 {
                1
            } else {
                code
            }
        }
        Err(panic) => {
            hook.panic = Some(panic);
            u32::MAX
        }
    }
}

pub struct Pool(Box<[[Actor; SLOTS]; 2]>);
impl Default for Pool {
    fn default() -> Self {
        Self(Box::new(std::array::from_fn(|_| {
            std::array::from_fn(|_| Actor::default())
        })))
    }
}
impl Pool {
    pub fn attack<F>(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        motion: &Motion,
        random: &mut Random,
        sink: &mut F,
    ) -> Result<AttackResult, u32>
    where
        F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, AttackSelection<'_>) -> Result<(), u32>,
    {
        let mut hook = AttackHook { sink, panic: None };
        let mut out = AttackResult::default();
        let code = unsafe {
            kbcs_core_actor_attack(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                motion,
                random.state_mut(),
                emit_attack::<F>,
                (&mut hook as *mut AttackHook<'_, F>).cast(),
                &mut out,
            )
        };
        if let Some(panic) = hook.panic {
            std::panic::resume_unwind(panic);
        }
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn attack_wait(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        motion: &Motion,
        burrow_blocked: bool,
    ) -> Result<bool, u32> {
        let mut handled = 0;
        let code = unsafe {
            kbcs_core_actor_attack_wait(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                motion,
                i32::from(burrow_blocked),
                &mut handled,
            )
        };
        if code == 0 {
            Ok(handled != 0)
        } else {
            Err(code)
        }
    }
    pub fn intent(&mut self, environment: &Environment) -> Result<bool, u32> {
        let mut blocked = 0;
        let code =
            unsafe { kbcs_core_actor_intent(self.0.as_mut_ptr(), environment, &mut blocked) };
        if code == 0 {
            Ok(blocked != 0)
        } else {
            Err(code)
        }
    }
    pub fn retire(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        input: &Retirement,
    ) -> Result<RetirementResult, u32> {
        let mut out = RetirementResult::default();
        let code = unsafe {
            kbcs_core_actor_retire(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                input,
                &mut out,
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    // 寄与者の生成通番は原本の順序・重複を保ち、呼出中だけ借用する。
    pub fn enemy_knockback(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        input: &EnemyDeath,
        cohort: &[i32],
    ) -> Result<EnemyDeathResult, u32> {
        let context = EnemyDeathContext {
            input: *input,
            cohort_count: i32::try_from(cohort.len()).map_err(|_| 1_u32)?,
            cohort: cohort.as_ptr(),
        };
        let mut out = EnemyDeathResult::default();
        let code = unsafe {
            kbcs_core_actor_enemy_knockback(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                &context,
                &mut out,
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn records(&self) -> &[[Actor; SLOTS]; 2] {
        &self.0
    }
    pub fn records_mut(&mut self) -> &mut [[Actor; SLOTS]; 2] {
        &mut self.0
    }
    pub fn enemy_displacement(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        boundary: i32,
    ) -> Result<bool, u32> {
        let mut handled = 0;
        let code = unsafe {
            kbcs_core_actor_enemy_displacement(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                boundary,
                &mut handled,
            )
        };
        if code == 0 {
            Ok(handled != 0)
        } else {
            Err(code)
        }
    }
    pub fn unit_knockback(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        input: &Knockback,
    ) -> Result<KnockbackResult, u32> {
        let mut out = KnockbackResult::default();
        let code = unsafe {
            kbcs_core_actor_unit_knockback(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                input,
                &mut out,
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn walk(&mut self, environment: &Environment, side: i32, slot: i32) -> Result<bool, u32> {
        let mut handled = 0;
        let code = unsafe {
            kbcs_core_actor_walk(self.0.as_mut_ptr(), environment, side, slot, &mut handled)
        };
        if code == 0 {
            Ok(handled != 0)
        } else {
            Err(code)
        }
    }
    pub fn begin(&mut self, environment: &Environment, side: i32, slot: i32) -> Result<(), u32> {
        let code = unsafe { kbcs_core_actor_begin(self.0.as_mut_ptr(), environment, side, slot) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn react(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        input: &Reaction,
        random: &mut Random,
    ) -> Result<ReactionResult, u32> {
        let mut out = ReactionResult::default();
        let code = unsafe {
            kbcs_core_actor_react(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                input,
                random.state_mut(),
                &mut out,
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn health(
        &mut self,
        side: i32,
        slot: i32,
        input: &Health,
        random: &mut Random,
    ) -> Result<HealthResult, u32> {
        let mut out = HealthResult::default();
        let code = unsafe {
            kbcs_core_actor_health(
                self.0.as_mut_ptr(),
                side,
                slot,
                input,
                random.state_mut(),
                &mut out,
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn protect(&mut self, side: i32, slot: i32) -> Result<Protection, u32> {
        let mut out = Protection::default();
        let code = unsafe { kbcs_core_actor_protect(self.0.as_mut_ptr(), side, slot, &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn damage(
        &mut self,
        environment: &Environment,
        rows: &[stage::Row],
        states: &[stage::State],
        input: &mut Damage,
    ) -> Result<(), u32> {
        if rows.len() != states.len() {
            return Err(1);
        }
        let mut context = DamageContext {
            guard_enabled: i32::from(input.guard_enabled),
            notice: input.notice,
            rows: rows.as_ptr(),
            states: states.as_ptr(),
            count: i32::try_from(rows.len()).map_err(|_| 1_u32)?,
        };
        let code = unsafe {
            kbcs_core_actor_damage(
                self.0.as_mut_ptr(),
                environment,
                &mut context,
                input.side,
                input.slot,
                input.amount,
            )
        };
        if code == 0 {
            input.notice = context.notice;
            Ok(())
        } else {
            Err(code)
        }
    }
    pub fn transition(
        &mut self,
        environment: &Environment,
        side: i32,
        slot: i32,
        motion: &Motion,
        boundary: i32,
    ) -> Result<i32, u32> {
        let mut sound = -1;
        let code = unsafe {
            kbcs_core_actor_transition(
                self.0.as_mut_ptr(),
                environment,
                side,
                slot,
                motion,
                boundary,
                &mut sound,
            )
        };
        if code == 0 { Ok(sound) } else { Err(code) }
    }
    pub fn motion(&mut self, side: i32, slot: i32, motion: &Motion) -> Result<(), u32> {
        let code = unsafe { kbcs_core_actor_motion(self.0.as_mut_ptr(), side, slot, motion) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn resume(&mut self, side: i32, slot: i32) -> Result<(), u32> {
        let code = unsafe { kbcs_core_actor_resume(self.0.as_mut_ptr(), side, slot) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn clock(&mut self, clock: &Clock) -> Result<(), u32> {
        let code = unsafe { kbcs_core_actor_clock(self.0.as_mut_ptr(), clock) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn matches(
        &self,
        environment: &Environment,
        side: i32,
        slot: i32,
        target: i32,
    ) -> Result<bool, u32> {
        let mut out = 0;
        let code = unsafe {
            kbcs_core_actor_matches(self.0.as_ptr(), environment, side, slot, target, &mut out)
        };
        if code == 0 { Ok(out != 0) } else { Err(code) }
    }
    pub fn roll(
        &self,
        side: i32,
        slot: i32,
        hit: i32,
        random: &mut Random,
    ) -> Result<AttackRoll, u32> {
        let mut flags = [0; 12];
        let code = unsafe {
            kbcs_core_actor_roll(
                self.0.as_ptr(),
                side,
                slot,
                hit,
                random.state_mut(),
                flags.as_mut_ptr(),
            )
        };
        if code == 0 {
            Ok(AttackRoll(flags))
        } else {
            Err(code)
        }
    }
    pub fn contact(
        &self,
        side: i32,
        slot: i32,
        target: i32,
        hit: i32,
        castle_slot: i32,
        special_castle: bool,
    ) -> Result<bool, u32> {
        let mut out = 0;
        let code = unsafe {
            kbcs_core_actor_contact(
                self.0.as_ptr(),
                side,
                slot,
                target,
                hit,
                castle_slot,
                i32::from(special_castle),
                &mut out,
            )
        };
        if code == 0 { Ok(out != 0) } else { Err(code) }
    }
    pub fn apply_effects(
        &mut self,
        environment: &Environment,
        context: &EffectContext,
        source: [i32; 3],
        flags: &[i32; 7],
        random: &mut Random,
    ) -> Result<EffectEvents, u32> {
        let mut events = EffectEvents::default();
        let code = unsafe {
            kbcs_core_actor_effects(
                self.0.as_mut_ptr(),
                environment,
                context,
                source[0],
                source[1],
                source[2],
                flags.as_ptr(),
                random.state_mut(),
                &mut events,
            )
        };
        if code == 0 { Ok(events) } else { Err(code) }
    }
    // 生成に失敗したエラーは戦闘を停止する。正常な満員(-1)と区別する。
    pub fn initialize(
        &mut self,
        definition: &Definition,
        environment: &mut Environment,
        request: &SpawnRequest,
        random: &mut Random,
    ) -> Result<i32, u32> {
        let mut slot = -1;
        let code = unsafe {
            kbcs_core_actor_initialize(
                definition,
                environment,
                self.0.as_mut_ptr(),
                request,
                random.state_mut(),
                &mut slot,
            )
        };
        if code == 0 { Ok(slot) } else { Err(code) }
    }
}

unsafe extern "C" {
    fn kbcs_core_actor_emit_area(
        actors: *const [Actor; SLOTS],
        environment: *const Environment,
        source: *const RawAttackSelection,
        emission: *const Emission,
        seed: *mut u32,
        out: *mut AreaEmission,
    ) -> u32;
    fn kbcs_core_actor_emit_wave(
        actors: *const [Actor; SLOTS],
        environment: *const Environment,
        source: *const RawAttackSelection,
        emission: *const Emission,
        waves: *mut WaveState,
        seed: *mut u32,
        slot: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_emit_direct(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        selection: *const RawAttackSelection,
        seed: *mut u32,
        sink: HitSink,
        user: *mut c_void,
        out: *mut Emission,
    ) -> u32;
    fn kbcs_core_actor_attack(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        motion: *const Motion,
        seed: *mut u32,
        sink: AttackSink,
        user: *mut c_void,
        out: *mut AttackResult,
    ) -> u32;
    fn kbcs_core_actor_attack_wait(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        motion: *const Motion,
        burrow_blocked: i32,
        handled: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_intent(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        blocked: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_retire(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        input: *const Retirement,
        out: *mut RetirementResult,
    ) -> u32;
    fn kbcs_core_actor_enemy_knockback(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        input: *const EnemyDeathContext,
        out: *mut EnemyDeathResult,
    ) -> u32;
    fn kbcs_core_actor_enemy_displacement(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        boundary: i32,
        handled: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_unit_knockback(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        input: *const Knockback,
        out: *mut KnockbackResult,
    ) -> u32;
    fn kbcs_core_actor_walk(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        handled: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_begin(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
    ) -> u32;
    fn kbcs_core_actor_transition(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        motion: *const Motion,
        boundary: i32,
        sound: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_react(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        input: *const Reaction,
        seed: *mut u32,
        out: *mut ReactionResult,
    ) -> u32;
    fn kbcs_core_actor_health(
        actors: *mut [Actor; SLOTS],
        side: i32,
        slot: i32,
        input: *const Health,
        seed: *mut u32,
        out: *mut HealthResult,
    ) -> u32;
    fn kbcs_core_actor_protect(
        actors: *mut [Actor; SLOTS],
        side: i32,
        slot: i32,
        out: *mut Protection,
    ) -> u32;
    fn kbcs_core_actor_damage(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        context: *mut DamageContext,
        side: i32,
        slot: i32,
        amount: i32,
    ) -> u32;
    fn kbcs_core_actor_motion(
        actors: *mut [Actor; SLOTS],
        side: i32,
        slot: i32,
        motion: *const Motion,
    ) -> u32;
    fn kbcs_core_actor_resume(actors: *mut [Actor; SLOTS], side: i32, slot: i32) -> u32;
    fn kbcs_core_actor_clock(actors: *mut [Actor; SLOTS], clock: *const Clock) -> u32;
    fn kbcs_core_actor_matches(
        actors: *const [Actor; SLOTS],
        environment: *const Environment,
        side: i32,
        slot: i32,
        target: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_effects(
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        context: *const EffectContext,
        side: i32,
        slot: i32,
        target: i32,
        flags: *const i32,
        seed: *mut u32,
        out: *mut EffectEvents,
    ) -> u32;
    fn kbcs_core_actor_roll(
        actors: *const [Actor; SLOTS],
        side: i32,
        slot: i32,
        hit: i32,
        seed: *mut u32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_contact(
        actors: *const [Actor; SLOTS],
        side: i32,
        slot: i32,
        target: i32,
        hit: i32,
        castle_slot: i32,
        special_castle: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_load(raw: *const i32, count: i32, unit: i32, out: *mut i32) -> u32;
    fn kbcs_core_actor_initialize(
        definition: *const Definition,
        environment: *mut Environment,
        actors: *mut [Actor; SLOTS],
        request: *const SpawnRequest,
        seed: *mut u32,
        slot: *mut i32,
    ) -> u32;
}

#[cfg(test)]
mod tests;
