use super::*;

#[repr(C)]
#[derive(Default, Debug, Clone, Copy, serde::Deserialize, serde::Serialize)]
pub struct WaveSegment {
    pub frame: i32,
    pub x: i32,
}
#[repr(C)]
#[derive(serde::Deserialize)]
pub struct WaveRules {
    pub small_interval: i32,
    pub small_start: i32,
    pub small_end: i32,
    pub motion_frames: [i32; 2],
    pub game_mode: i32,
}
#[repr(i32)]
#[derive(Clone, Copy)]
pub enum WavePhase {
    Advance,
    Hit,
}
#[repr(C)]
struct RawSegments {
    records: [[WaveSegment; 6]; 200],
}
pub struct WaveSegments(Box<RawSegments>);
impl Default for WaveSegments {
    fn default() -> Self {
        Self(Box::new(RawSegments {
            records: [[WaveSegment::default(); 6]; 200],
        }))
    }
}
impl WaveSegments {
    pub fn records(&self) -> &[[WaveSegment; 6]; 200] {
        &self.0.records
    }
    // 生成→区間減算/遮断→候補→命中の二つの入口を原本順に呼ぶ。
    #[allow(clippy::too_many_arguments)]
    pub fn step<F>(
        &mut self,
        phase: WavePhase,
        waves: &mut Waves,
        actors: &mut [[Actor; SLOTS]; 2],
        environment: &Environment,
        rules: &WaveRules,
        random: &mut Random,
        sink: &mut F,
    ) -> Result<i32, u32>
    where
        F: FnMut(&mut [[Actor; SLOTS]; 2], &mut Random, &SecondaryHit) -> Result<bool, u32>,
    {
        let mut hook = AttackHook { sink, panic: None };
        let mut sounds = 0;
        let code = unsafe {
            kbcs_core_actor_waves_step(
                phase as i32,
                waves.0.as_mut(),
                self.0.as_mut(),
                actors.as_mut_ptr(),
                environment,
                rules,
                random.state_mut(),
                apply_hit::<F, SecondaryHit>,
                (&mut hook as *mut AttackHook<'_, F>).cast(),
                &mut sounds,
            )
        };
        if let Some(panic) = hook.panic {
            std::panic::resume_unwind(panic);
        }
        if code != 0 { Err(code) } else { Ok(sounds) }
    }
}
unsafe extern "C" {
    fn kbcs_core_actor_waves_step(
        phase: i32,
        waves: *mut WaveState,
        segments: *mut RawSegments,
        actors: *mut [Actor; SLOTS],
        environment: *const Environment,
        rules: *const WaveRules,
        seed: *mut u32,
        sink: unsafe extern "C" fn(
            *mut c_void,
            *mut [Actor; SLOTS],
            *mut u32,
            *const SecondaryHit,
            *mut i32,
        ) -> u32,
        user: *mut c_void,
        sounds: *mut i32,
    ) -> u32;
}
