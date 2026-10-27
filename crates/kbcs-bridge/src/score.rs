use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Input {
    pub elapsed: i32,
    pub best: i32,
    pub count: i32,
    pub thresholds: [i32; 10],
}
#[repr(C)]
#[derive(Default, Serialize, Deserialize, Debug, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct Output {
    pub score: i32,
    pub best: i32,
    pub improved: i32,
    pub reward_mask: i32,
}
unsafe extern "C" {
    fn kbcs_core_stage_score(input: *const Input, output: *mut Output) -> u32;
    fn kbcs_core_stage_score_tick(elapsed: i32, phase: i32, output: *mut i32) -> u32;
}
pub fn advance(elapsed: i32, phase: i32) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_stage_score_tick(elapsed, phase, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn event_available(save_id: i32, flag: i32) -> bool {
    // 通常イベントは保存番号なしでこの処理へ進まない。原本ヘッダー2列の上限も反映する。
    (0..200).contains(&save_id) && flag == 1
}
pub fn stage_available(mode: i32, save_id: i32, flag: i32) -> bool {
    // 005dd5b8: 未来編は通常イベントと別の章別保存先を持つ。
    flag == 1 && ((4..=6).contains(&mode) || event_available(save_id, flag))
}
pub fn calculate(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 履歴の保存・実付与は所有ランタイムが行う。ここは数値と要求だけを返す。
    let code = unsafe { kbcs_core_stage_score(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_score_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/score-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let expected: Output = serde_json::from_value(vector.clone()).unwrap();
        assert_eq!(calculate(&input).unwrap(), expected);
    }
    for disabled in fixture["disabled"].as_array().unwrap() {
        assert!(!event_available(
            disabled["saveId"].as_i64().unwrap() as i32,
            1
        ));
    }
    for timer in fixture["timers"].as_array().unwrap() {
        assert_eq!(
            advance(
                timer["elapsed"].as_i64().unwrap() as i32,
                timer["phase"].as_i64().unwrap() as i32
            )
            .unwrap(),
            timer["result"].as_i64().unwrap() as i32
        );
    }
    assert!(event_available(199, 1));
    assert!(!event_available(200, 1));
    assert!(!event_available(0, 0));
    let input = Input {
        elapsed: 0,
        best: 0,
        count: 1,
        thresholds: [-1; 10],
    };
    let mut output = Output {
        score: 37,
        ..Default::default()
    };
    assert_eq!(unsafe { kbcs_core_stage_score(&input, &mut output) }, 1);
    assert_eq!(output.score, 37);
}
