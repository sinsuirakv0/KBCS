use crate::actor;
#[repr(C)]
#[derive(Clone, Copy, Default)]
pub struct Rules {
    pub encoded: [i32; 4],
    pub attack_rate: i32,
}
#[repr(C)]
pub struct Setup {
    pub kind: i32,
    pub level: i32,
    pub range_level: i32,
    pub attack_level: i32,
    pub treasure: i32,
    pub combo: i32,
    pub status: [i32; 6],
}
#[repr(C)]
pub struct Growth {
    pub kind: i32,
    pub end: i32,
    pub value1: i32,
    pub value2: i32,
    pub easing: i32,
}
pub fn setup(input: &Setup, growth: &[Growth]) -> Result<actor::Actor, u32> {
    if growth.len() > 512 {
        return Err(1);
    }
    let mut out = actor::Actor {
        words: [0; actor::WORDS],
    };
    let code = unsafe {
        kbcs_core_actor_cannon_setup(&mut out, input, growth.as_ptr(), growth.len() as i32)
    };
    if code == 0 { Ok(out) } else { Err(code) }
}
unsafe extern "C" {
    fn kbcs_core_actor_cannon_setup(
        out: *mut actor::Actor,
        input: *const Setup,
        growth: *const Growth,
        count: i32,
    ) -> u32;
}
