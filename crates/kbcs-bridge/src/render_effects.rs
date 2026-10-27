use crate::render::{Command, Cut, Layout};
use serde_json::Value;
use std::{collections::BTreeMap, ffi::c_void, ptr::NonNull};

const PROPERTIES: [&str; 37] = [
    "count",
    "x",
    "y",
    "frame",
    "wait",
    "lifeTime",
    "scale",
    "scaleX",
    "scaleY",
    "angle",
    "angularV",
    "alpha",
    "v",
    "vx",
    "vy",
    "moveAngle",
    "destroyLeft",
    "destroyRight",
    "destroyTop",
    "destroyBottom",
    "z",
    "equallySpaced",
    "startX",
    "startY",
    "startFrame",
    "startWait",
    "startLifeTime",
    "startScale",
    "startScaleX",
    "startScaleY",
    "startAngle",
    "startAngularV",
    "startAlpha",
    "startV",
    "startVx",
    "startVy",
    "startMoveAngle",
];
#[repr(C)]
#[derive(Default, Clone, Copy)]
struct Spec {
    kind: i32,
    base: i32,
    low_base: i32,
    high_base: i32,
    value: f64,
    low: f64,
    high: f64,
    first: i32,
    count: i32,
    group: i32,
}
#[repr(C)]
#[derive(Clone, Copy)]
struct Segment {
    properties: [Spec; 37],
    first: i32,
    count: i32,
}
#[repr(C)]
#[derive(Default, Clone, Copy, Debug, serde::Serialize)]
pub struct Particle {
    pub asset: i32,
    pub front: i32,
    pub kind: i32,
    pub variant: i32,
    pub x: f64,
    pub y: f64,
    pub frame: f64,
    pub scale: f64,
    pub sx: f64,
    pub sy: f64,
    pub angle: f64,
    pub alpha: f64,
    pub spacing: f64,
    pub spacing_min: i32,
    pub spacing_max: i32,
    pub color: [i32; 3],
}
unsafe extern "C" {
    fn kbcs_core_effect_create(
        width: f64,
        classic: i32,
        segments: *const Segment,
        count: i32,
        values: *const f64,
        value_count: i32,
        assets: *const i32,
        lengths: *const i32,
        asset_count: i32,
        seed: u32,
        handle: *mut *mut c_void,
    ) -> u32;
    fn kbcs_core_effect_frame(
        handle: *mut c_void,
        frame: i32,
        output: *mut Particle,
        capacity: i32,
        written: *mut i32,
    ) -> u32;
    fn kbcs_core_effect_destroy(handle: *mut c_void);
    fn kbcs_core_weather_draw(
        layout: *const Layout,
        particle: *const Particle,
        cuts: *const Cut,
        count: i32,
        common: *const Cut,
        common_count: i32,
        sizes: *const i32,
        output: *mut Command,
    ) -> u32;
}
fn number(value: &Value) -> f64 {
    value
        .as_f64()
        .or_else(|| value.as_str().and_then(|s| s.parse().ok()))
        .filter(|v| v.is_finite())
        .unwrap_or(0.)
}
fn base(value: &Value) -> i32 {
    match value["base"].as_str().unwrap_or("") {
        "worldLeft" => 1,
        "worldRight" => 2,
        "worldTop" => 3,
        "worldBottom" => 4,
        "world" => 5,
        "screenRight" => 6,
        "screenBottom" => 7,
        "secondToFrame" => 8,
        "percentToFloat" => 9,
        "percentToAlpha" => 10,
        "animeLength" => 11,
        "animeInterval" => 12,
        "bgImage" => 13,
        "frontChara" => 14,
        _ => 0,
    }
}
pub struct Runtime {
    handle: NonNull<c_void>,
    output: Vec<Particle>,
}
// 所有権を移動できるが、同時操作は許さない。Service側ではMutexで保護する。
unsafe impl Send for Runtime {}
impl Drop for Runtime {
    fn drop(&mut self) {
        unsafe { kbcs_core_effect_destroy(self.handle.as_ptr()) }
    }
}
impl Runtime {
    pub fn new(
        width: f64,
        classic: i32,
        parameters: &[Value],
        lengths: &[i32],
        asset_counts: &[usize],
        seed: u32,
    ) -> Result<Self, u32> {
        if parameters.len() != asset_counts.len() {
            return Err(1);
        }
        let mut segments = Vec::new();
        let mut values = Vec::new();
        let mut groups = BTreeMap::new();
        let mut first = 0;
        for (parameters, count) in parameters.iter().zip(asset_counts) {
            let mut properties = [Spec::default(); 37];
            for (index, name) in PROPERTIES.iter().enumerate() {
                let value = &parameters[name];
                if value.is_null() {
                    continue;
                }
                let group = if value["randGroup"].is_null() {
                    -1
                } else {
                    let key = value["randGroup"].to_string();
                    let next = groups.len() as i32;
                    *groups.entry(key).or_insert(next)
                };
                let mut spec = Spec {
                    kind: 1,
                    base: base(value),
                    value: number(&value["value"]),
                    group,
                    ..Default::default()
                };
                if let Some(list) = value["values"].as_array().filter(|v| !v.is_empty()) {
                    spec.kind = 3;
                    spec.first = values.len() as i32;
                    spec.count = list.len() as i32;
                    values.extend(list.iter().map(number));
                } else if value["min"].is_object() && value["max"].is_object() {
                    spec.kind = 2;
                    spec.low_base = base(&value["min"]);
                    spec.high_base = base(&value["max"]);
                    spec.low = number(&value["min"]["value"]);
                    spec.high = number(&value["max"]["value"]);
                }
                if *name == "equallySpaced" {
                    spec.low = number(&value["pos1"]);
                    spec.high = number(&value["pos2"]);
                }
                properties[index] = spec;
            }
            segments.push(Segment {
                properties,
                first,
                count: *count as i32,
            });
            first += *count as i32;
        }
        if first as usize != lengths.len() {
            return Err(1);
        }
        let assets: Vec<_> = (0..first).collect();
        let mut handle = std::ptr::null_mut();
        let code = unsafe {
            kbcs_core_effect_create(
                width,
                classic,
                segments.as_ptr(),
                segments.len() as i32,
                values.as_ptr(),
                values.len() as i32,
                assets.as_ptr(),
                lengths.as_ptr(),
                lengths.len() as i32,
                seed,
                &mut handle,
            )
        };
        if code != 0 {
            return Err(code);
        }
        NonNull::new(handle)
            .map(|handle| Self {
                handle,
                output: vec![Particle::default(); 16384],
            })
            .ok_or(3)
    }
    // 次のframe呼出まで借用する。大きな出力領域を毎F確保・ゼロ埋めしない。
    pub fn frame(&mut self, frame: i32) -> Result<&[Particle], u32> {
        let mut written = 0;
        let code = unsafe {
            kbcs_core_effect_frame(
                self.handle.as_ptr(),
                frame,
                self.output.as_mut_ptr(),
                self.output.len() as i32,
                &mut written,
            )
        };
        if code != 0 {
            return Err(code);
        }
        self.output.get(..written as usize).ok_or(2)
    }
}
pub fn weather(
    layout: &Layout,
    particle: &Particle,
    cuts: &[Cut],
    common: &[Cut],
    sizes: [i32; 4],
) -> Result<Command, u32> {
    let mut output = Command::default();
    let code = unsafe {
        kbcs_core_weather_draw(
            layout,
            particle,
            cuts.as_ptr(),
            cuts.len() as i32,
            common.as_ptr(),
            common.len() as i32,
            sizes.as_ptr(),
            &mut output,
        )
    };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn scene_clock_reference_vectors() {
    let fixture: Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/scene-effect-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in fixture["cases"].as_array().unwrap() {
        let parameters = case["parameters"].as_array().unwrap();
        let lengths: Vec<i32> = serde_json::from_value(case["lengths"].clone()).unwrap();
        let counts: Vec<usize> = serde_json::from_value(case["counts"].clone()).unwrap();
        let mut runtime = Runtime::new(
            case["width"].as_f64().unwrap(),
            case["classic"].as_i64().unwrap() as i32,
            parameters,
            &lengths,
            &counts,
            0x12345678,
        )
        .unwrap();
        for vector in case["vectors"].as_array().unwrap() {
            let particles = runtime
                .frame(vector["frame"].as_i64().unwrap() as i32)
                .unwrap();
            assert_eq!(particles.len(), vector["count"].as_u64().unwrap() as usize);
            for sample in vector["samples"].as_array().unwrap() {
                let actual =
                    serde_json::to_value(particles[sample["index"].as_u64().unwrap() as usize])
                        .unwrap();
                for (key, expected) in sample["value"].as_object().unwrap() {
                    if let (Some(a), Some(b)) = (actual[key].as_f64(), expected.as_f64()) {
                        assert!(
                            (a - b).abs() < 0.0001,
                            "bg {} frame {} index {} field {}: {} != {}",
                            case["background"],
                            vector["frame"],
                            sample["index"],
                            key,
                            a,
                            b
                        );
                    } else {
                        assert_eq!(actual[key], *expected);
                    }
                }
            }
        }
    }
}
