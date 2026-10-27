use crate::random::Random;
use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy, Default, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    pub chance: i32,
    pub map_index: i32,
    pub minimum: i32,
    pub maximum: i32,
    pub group_present: i32,
}
#[repr(C)]
#[derive(Clone, Copy, Default, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Choice {
    pub group: i32,
    pub threshold: i32,
    pub map_index: i32,
    pub stage: i32,
}
#[repr(C)]
#[derive(Default, Deserialize, Serialize, Debug, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct Output {
    pub group: i32,
    pub source: i32,
    pub map_index: i32,
    pub stage: i32,
    pub consumed: i32,
    pub bounds: [i32; 3],
    pub rolls: [i32; 3],
}
unsafe extern "C" {
    fn kbcs_core_stage_ex(
        input: *const Input,
        choices: *const Choice,
        count: i32,
        state: *mut u32,
        output: *mut Output,
    ) -> u32;
}
pub fn select(input: &Input, choices: &[Choice], random: &mut Random) -> Result<Output, u32> {
    if choices.len() > 32 {
        return Err(1);
    }
    let mut output = Output::default();
    // 状態をコピーして検査・抽選し、成功時だけ乱数状態もまとめて確定する。
    let code = unsafe {
        kbcs_core_stage_ex(
            input,
            choices.as_ptr(),
            choices.len() as i32,
            random.state_mut(),
            &mut output,
        )
    };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_ex_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/ex-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let choices: Vec<Choice> = serde_json::from_value(vector["choices"].clone()).unwrap();
        let expected: Output = serde_json::from_value(vector.clone()).unwrap();
        let mut random = Random::new(vector["seed"].as_u64().unwrap() as u32).unwrap();
        assert_eq!(select(&input, &choices, &mut random).unwrap(), expected);
        assert_eq!(
            u64::from(random.state()),
            vector["stateAfter"].as_u64().unwrap()
        );
        let before = random.state();
        input.chance = 101;
        assert!(matches!(select(&input, &choices, &mut random), Err(1)));
        assert_eq!(random.state(), before);
    }
}
