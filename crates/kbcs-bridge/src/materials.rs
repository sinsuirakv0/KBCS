use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Input {
    pub count: f32,
    pub multiplier: f32,
    pub miss: i32,
    pub weights: [i32; 16],
}
#[repr(C)]
#[derive(Clone, Copy, Default, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Chance {
    pub chance: f64,
    pub at_least_one: f64,
    pub expected: f64,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct Output {
    pub draws: i32,
    pub miss: f64,
    pub none: f64,
    pub items: [Chance; 16],
}
unsafe extern "C" {
    fn kbcs_core_material_plan(input: *const Input, output: *mut Output) -> u32;
    fn kbcs_core_material_pick(
        input: *const Input,
        miss_roll: i32,
        weight_roll: i32,
        slot: *mut i32,
    ) -> u32;
}
pub fn plan(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 呼出中だけ固定幅の入力と出力を借用する。
    let code = unsafe { kbcs_core_material_plan(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn pick(input: &Input, miss_roll: i32, weight_roll: Option<i32>) -> Result<Option<usize>, u32> {
    let mut slot = -1;
    let code =
        unsafe { kbcs_core_material_pick(input, miss_roll, weight_roll.unwrap_or(-1), &mut slot) };
    if code == 0 {
        Ok((slot >= 0).then_some(slot as usize))
    } else {
        Err(code)
    }
}

#[test]
fn native_material_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/material-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let value = &vector["input"];
        let mut weights: Vec<i32> = serde_json::from_value(value["weights"].clone()).unwrap();
        weights.resize(16, 0);
        let mut input = Input {
            count: value["count"].as_f64().unwrap() as f32,
            multiplier: value["multiplier"].as_f64().unwrap() as f32,
            miss: value["miss"].as_i64().unwrap() as i32,
            weights: weights.try_into().unwrap(),
        };
        let planned = plan(&input).unwrap();
        assert_eq!(i64::from(planned.draws), vector["draws"].as_i64().unwrap());
        let calls: Vec<[i32; 2]> = serde_json::from_value(vector["calls"].clone()).unwrap();
        let mut cursor = 0;
        let mut counts = [0; 16];
        for _ in 0..planned.draws {
            let [bound, miss] = calls[cursor];
            cursor += 1;
            assert_eq!(bound, 100);
            let weight = if miss >= input.miss {
                let [bound, roll] = calls[cursor];
                cursor += 1;
                assert_eq!(bound, input.weights.iter().sum::<i32>());
                Some(roll)
            } else {
                None
            };
            if let Some(slot) = pick(&input, miss, weight).unwrap() {
                counts[slot] += 1;
            }
        }
        assert_eq!(cursor, calls.len());
        let expected: [i32; 16] = serde_json::from_value(vector["counts"].clone()).unwrap();
        assert_eq!(counts, expected);
        if input.miss == 60 {
            assert!((planned.items[0].chance - 2.0 / 15.0).abs() < 1e-12);
            assert!((planned.items[0].at_least_one - 56.0 / 225.0).abs() < 1e-12);
            assert!((planned.none - 0.36).abs() < 1e-12);
        }
        input.weights = [i32::MAX; 16];
        assert!(matches!(plan(&input), Err(2)));
    }
}
