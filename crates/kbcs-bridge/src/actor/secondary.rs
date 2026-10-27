use super::*;
use std::ptr::NonNull;

#[repr(C)]
#[derive(Debug, serde::Serialize, serde::Deserialize)]
pub struct SecondaryHit {
    pub hit: DirectHit,
    pub attack_type: i32,
}
#[repr(C)]
#[derive(Default, serde::Deserialize)]
pub struct AreaRules {
    pub summon_sound_frame: i32,
    pub summon_frame: i32,
    pub summon_motion: [i32; 2],
    pub explosion_frames: [i32; 4],
    pub explosion_widths: [i32; 3],
    pub explosion_damage: [i32; 3],
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct Reflection {
    pub side: i32,
    pub slot: i32,
    pub state: i32,
    pub frame: i32,
    pub x: i32,
    pub level: i32,
    pub offset: i32,
    pub span: i32,
    pub mini: u8,
    pub reserved: [u8; 3],
}
#[repr(C)]
pub struct AreaHistory {
    pub cycles: [i32; SLOTS],
    pub present: [u8; SLOTS],
}
#[repr(C)]
pub struct ExplosionHistory {
    pub hits: [[u8; 5]; SLOTS],
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct AreaCounts {
    pub surges: i32,
    pub reflections: i32,
    pub explosions: i32,
    pub events: i32,
}
#[repr(C)]
#[derive(Default, Debug, serde::Serialize)]
pub struct AreaEvent {
    pub kind: i32,
    pub value: i32,
}
#[repr(i32)]
#[derive(Clone, Copy)]
pub enum AreaPhase {
    Surges,
    Reflections,
    Explosions,
}
#[repr(C)]
struct RawAreas {
    _private: [u8; 0],
}
pub struct Areas(NonNull<RawAreas>);
impl Areas {
    pub fn new() -> Result<Self, u32> {
        let mut raw = std::ptr::null_mut();
        let code = unsafe { kbcs_core_actor_areas_create(&mut raw) };
        if code != 0 {
            return Err(code);
        }
        NonNull::new(raw).map(Self).ok_or(3)
    }
    pub fn append(&mut self, emission: &AreaEmission) -> Result<(), u32> {
        checked(unsafe { kbcs_core_actor_areas_append(self.0.as_ptr(), emission) })
    }
    pub fn counts(&self) -> Result<AreaCounts, u32> {
        let mut out = AreaCounts::default();
        checked(unsafe { kbcs_core_actor_areas_counts(self.0.as_ptr(), &mut out) })?;
        Ok(out)
    }
    pub fn retirement_blocked(
        &self,
        waves: &Waves,
        side: i32,
        slot: i32,
        unit_route: bool,
    ) -> Result<bool, u32> {
        let mut out = 0;
        checked(unsafe {
            kbcs_core_actor_areas_retirement_blocked(
                self.0.as_ptr(),
                waves.0.as_ref(),
                side,
                slot,
                i32::from(unit_route),
                &mut out,
            )
        })?;
        Ok(out != 0)
    }
    pub fn surge(&self, index: i32) -> Result<(Surge, AreaHistory), u32> {
        let mut out = Surge::default();
        let mut history = AreaHistory {
            cycles: [0; SLOTS],
            present: [0; SLOTS],
        };
        checked(unsafe {
            kbcs_core_actor_areas_surge(self.0.as_ptr(), index, &mut out, &mut history)
        })?;
        Ok((out, history))
    }
    pub fn reflection(&self, index: i32) -> Result<Reflection, u32> {
        let mut out = Reflection::default();
        checked(unsafe { kbcs_core_actor_areas_reflection(self.0.as_ptr(), index, &mut out) })?;
        Ok(out)
    }
    pub fn explosion(&self, index: i32) -> Result<(Explosion, ExplosionHistory), u32> {
        let mut out = Explosion::default();
        let mut history = ExplosionHistory {
            hits: [[0; 5]; SLOTS],
        };
        checked(unsafe {
            kbcs_core_actor_areas_explosion(self.0.as_ptr(), index, &mut out, &mut history)
        })?;
        Ok((out, history))
    }
    pub fn event(&self, index: i32) -> Result<AreaEvent, u32> {
        let mut out = AreaEvent::default();
        checked(unsafe { kbcs_core_actor_areas_event(self.0.as_ptr(), index, &mut out) })?;
        Ok(out)
    }
    pub fn step<F>(
        &mut self,
        phase: AreaPhase,
        actors: &mut [[Actor; SLOTS]; 2],
        environment: &Environment,
        rules: &AreaRules,
        random: &mut Random,
        sink: &mut F,
    ) -> Result<(), u32>
    where
        F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, &SecondaryHit) -> Result<bool, u32>,
    {
        let mut hook = AttackHook { sink, panic: None };
        let code = unsafe {
            kbcs_core_actor_areas_step(
                self.0.as_ptr(),
                phase as i32,
                actors.as_mut_ptr(),
                environment,
                rules,
                random.state_mut(),
                apply_hit::<F, SecondaryHit>,
                (&mut hook as *mut AttackHook<'_, F>).cast(),
            )
        };
        if let Some(panic) = hook.panic {
            std::panic::resume_unwind(panic);
        }
        checked(code)
    }
}
impl Drop for Areas {
    fn drop(&mut self) {
        unsafe { kbcs_core_actor_areas_destroy(self.0.as_ptr()) };
    }
}
fn checked(code: u32) -> Result<(), u32> {
    if code == 0 { Ok(()) } else { Err(code) }
}
type SecondarySink = unsafe extern "C" fn(
    *mut c_void,
    *mut [Actor; SLOTS],
    *mut u32,
    *const SecondaryHit,
    *mut i32,
) -> u32;
unsafe extern "C" {
    fn kbcs_core_actor_areas_create(out: *mut *mut RawAreas) -> u32;
    fn kbcs_core_actor_areas_destroy(areas: *mut RawAreas);
    fn kbcs_core_actor_areas_append(areas: *mut RawAreas, emission: *const AreaEmission) -> u32;
    fn kbcs_core_actor_areas_counts(areas: *const RawAreas, out: *mut AreaCounts) -> u32;
    fn kbcs_core_actor_areas_retirement_blocked(
        areas: *const RawAreas,
        waves: *const WaveState,
        side: i32,
        slot: i32,
        unit_route: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_actor_areas_surge(
        areas: *const RawAreas,
        index: i32,
        out: *mut Surge,
        history: *mut AreaHistory,
    ) -> u32;
    fn kbcs_core_actor_areas_reflection(
        areas: *const RawAreas,
        index: i32,
        out: *mut Reflection,
    ) -> u32;
    fn kbcs_core_actor_areas_explosion(
        areas: *const RawAreas,
        index: i32,
        out: *mut Explosion,
        history: *mut ExplosionHistory,
    ) -> u32;
    fn kbcs_core_actor_areas_event(areas: *const RawAreas, index: i32, out: *mut AreaEvent) -> u32;
    fn kbcs_core_actor_areas_step(
        areas: *mut RawAreas,
        phase: i32,
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        rules: *const AreaRules,
        seed: *mut u32,
        sink: SecondarySink,
        user: *mut c_void,
    ) -> u32;
}
