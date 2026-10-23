use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    pub base: i32,
    pub row_percent: i32,
    pub crown_percent: i32,
    pub crystal_max: i32,
    pub crystal_treasure: i32,
    pub castle_attack: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct Output {
    pub stages: [i64; 3],
}
unsafe extern "C" {
    fn kbcs_core_enemy_stat(input: *const Input, output: *mut Output) -> u32;
}
pub fn stat(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 入出力は呼出中だけ借用し、コアは状態を保持しない。
    let code = unsafe { kbcs_core_enemy_stat(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_enemy_stat_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/enemy-stat-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let expected: [i64; 3] = serde_json::from_value(vector["stages"].clone()).unwrap();
        assert_eq!(stat(&input).unwrap().stages, expected);
        input.base = i32::MAX;
        input.row_percent = 1000000;
        let mut output = Output { stages: [-1; 3] };
        assert_eq!(unsafe { kbcs_core_enemy_stat(&input, &mut output) }, 2);
        assert_eq!(output.stages, [-1; 3]);
        input.crystal_treasure = -1;
        assert!(matches!(stat(&input), Err(1)));
    }
}
