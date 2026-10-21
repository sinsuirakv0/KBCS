use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    pub base: i32,
    pub clears: i32,
    pub study_level: i32,
    pub treasure: i32,
    pub combo: i32,
    pub okame: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct Output {
    pub stages: [i64; 5],
}

unsafe extern "C" {
    fn kbcs_core_legend_experience(input: *const Input, output: *mut Output) -> u32;
}
pub fn legend(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 固定幅の入出力を呼出中だけ借用する。
    let code = unsafe { kbcs_core_legend_experience(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_experience_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/experience-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let expected: [i64; 5] = serde_json::from_value(vector["stages"].clone()).unwrap();
        assert_eq!(legend(&input).unwrap().stages, expected);
        input.base = i32::MAX;
        assert!(matches!(legend(&input), Err(2)));
        input.study_level = 0;
        assert!(matches!(legend(&input), Err(1)));
    }
}
