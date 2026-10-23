use serde::{Deserialize, Serialize};
#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    pub elapsed: i32,
    pub soul_frames: i32,
    pub special_frames: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct Output {
    pub phase: i32,
    pub frame: i32,
    pub x: f64,
    pub y: f64,
}
unsafe extern "C" {
    fn kbcs_core_motion_playback(input: *const Input, output: *mut Output) -> u32;
}
pub fn timeline(soul_frames: i32, special_frames: i32) -> Result<Vec<Output>, u32> {
    if !(0..=30000).contains(&soul_frames) || !(0..=30000).contains(&special_frames) {
        return Err(1);
    }
    let length = 24 + soul_frames.max(special_frames).max(1);
    let mut result = Vec::with_capacity(length as usize + 1);
    for elapsed in 0..=length {
        let mut out = Output::default();
        // 出力は呼出中だけ借用し、状態を保持しない。
        let code = unsafe {
            kbcs_core_motion_playback(
                &Input {
                    elapsed,
                    soul_frames,
                    special_frames,
                },
                &mut out,
            )
        };
        if code != 0 {
            return Err(code);
        }
        result.push(out);
    }
    Ok(result)
}
#[test]
fn playback_boundaries() {
    let frames = timeline(49, 81).unwrap();
    assert_eq!(
        (
            frames[23].phase,
            frames[24].phase,
            frames[104].phase,
            frames[105].phase
        ),
        (0, 1, 1, 2)
    );
    assert_eq!((frames[1].x, frames[1].y, frames[23].y), (6.0, -12.5, 0.0));
    assert_eq!(timeline(0, 0).unwrap().len(), 26);
    assert!(timeline(-1, 0).is_err());
}

#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct TimelineInput {
    pub soul_frames: i32,
    pub special_frames: i32,
}
