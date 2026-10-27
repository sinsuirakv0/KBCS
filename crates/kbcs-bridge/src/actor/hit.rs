use super::*;
use std::ptr::NonNull;

#[repr(C)]
#[derive(Default, serde::Deserialize)]
pub struct HitContext {
    pub effects: EffectContext,
    pub form: i32,
    pub raw_attack: [i32; 3],
    pub targeted_orbs: [[i32; 2]; 5],
    pub fruit_rates: [i32; 32],
    pub orbs: [[i32; 4]; ORBS],
    pub orb_present: [i32; ORBS],
    pub parameters: [i32; 5],
    pub base_reductions: [i32; 12],
    pub decoration_reductions: [i32; 3],
}

#[repr(i32)]
#[derive(Clone, Copy)]
pub enum Reservation {
    Metal,
    Credits,
}
#[repr(C)]
struct RawHits {
    _private: [u8; 0],
}
pub struct Hits(NonNull<RawHits>);
pub struct HitState<'a> {
    pub actors: &'a mut [[Actor; SLOTS]; 2],
    pub environment: &'a Environment,
    pub clock: &'a Clock,
    pub rows: &'a [stage::Row],
    pub states: &'a [stage::State],
    pub guard_enabled: bool,
    pub notice: &'a mut [i32; 2],
    pub random: &'a mut Random,
}
impl Hits {
    pub fn new() -> Result<Self, u32> {
        let mut raw = std::ptr::null_mut();
        let code = unsafe { kbcs_core_actor_hits_create(&mut raw) };
        if code != 0 {
            return Err(code);
        }
        NonNull::new(raw).map(Self).ok_or(3)
    }
    pub fn apply(
        &mut self,
        state: HitState<'_>,
        context: &HitContext,
        call: &SecondaryHit,
    ) -> Result<(bool, EffectEvents), u32> {
        if state.rows.len() != state.states.len() || state.rows.len() > i32::MAX as usize {
            return Err(1);
        }
        let mut damage = DamageContext {
            guard_enabled: i32::from(state.guard_enabled),
            notice: *state.notice,
            rows: state.rows.as_ptr(),
            states: state.states.as_ptr(),
            count: state.rows.len() as i32,
        };
        let mut applied = 0;
        let mut events = EffectEvents::default();
        let code = unsafe {
            kbcs_core_actor_hit(
                self.0.as_ptr(),
                state.actors.as_mut_ptr(),
                state.environment,
                context,
                state.clock,
                &mut damage,
                call,
                state.random.state_mut(),
                &mut applied,
                &mut events,
            )
        };
        if code != 0 {
            return Err(code);
        }
        *state.notice = damage.notice;
        Ok((applied != 0, events))
    }
    pub fn values(&self, kind: Reservation, key: i32) -> Result<Vec<i32>, u32> {
        let mut count = 0;
        let code = unsafe {
            kbcs_core_actor_hits_values(
                self.0.as_ptr(),
                kind as i32,
                key,
                std::ptr::null_mut(),
                0,
                &mut count,
            )
        };
        if code != 0 {
            return Err(code);
        }
        let mut values = vec![0; count as usize];
        let code = unsafe {
            kbcs_core_actor_hits_values(
                self.0.as_ptr(),
                kind as i32,
                key,
                values.as_mut_ptr(),
                count,
                &mut count,
            )
        };
        if code != 0 { Err(code) } else { Ok(values) }
    }
    pub fn erase(&mut self, kind: Reservation, key: i32) -> Result<(), u32> {
        let code = unsafe { kbcs_core_actor_hits_erase(self.0.as_ptr(), kind as i32, key) };
        if code != 0 { Err(code) } else { Ok(()) }
    }
}
impl Drop for Hits {
    fn drop(&mut self) {
        unsafe { kbcs_core_actor_hits_destroy(self.0.as_ptr()) };
    }
}
unsafe extern "C" {
    fn kbcs_core_actor_hits_create(out: *mut *mut RawHits) -> u32;
    fn kbcs_core_actor_hits_destroy(owner: *mut RawHits);
    fn kbcs_core_actor_hits_values(
        owner: *const RawHits,
        kind: i32,
        key: i32,
        values: *mut i32,
        capacity: i32,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_hits_erase(owner: *mut RawHits, kind: i32, key: i32) -> u32;
    fn kbcs_core_actor_hit(
        owner: *mut RawHits,
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        context: *const HitContext,
        clock: *const Clock,
        damage: *mut DamageContext,
        call: *const SecondaryHit,
        seed: *mut u32,
        applied: *mut i32,
        events: *mut EffectEvents,
    ) -> u32;
}
