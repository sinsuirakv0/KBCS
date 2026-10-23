use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Deserialize, Debug, PartialEq)]
#[serde(deny_unknown_fields)]
pub struct Input {
    pub count: i32,
    pub mode: i32,
    pub acquired: i32,
    pub radar: i32,
    pub chances: [i32; 3],
    pub rolls: [i32; 3],
}
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct StageContext {
    pub mode: i32,
    pub save_id: i32,
    pub acquired: i32,
    pub radar: i32,
    pub chances: [i32; 3],
    pub rolls: [i32; 3],
}
pub fn prepare_stage_input(context: &StageContext) -> Result<Option<Input>, u32> {
    if !(-2..=2).contains(&context.mode)
        || context.save_id < -1
        || !(0..=1).contains(&context.acquired)
        || !(0..=1).contains(&context.radar)
        || context.rolls.iter().any(|roll| !(0..100).contains(roll))
    {
        return Err(1);
    }
    if context.chances[0] == -1 {
        return Ok(None);
    }
    let count = if context.mode < 0 || context.chances[1] < 0 {
        1
    } else if context.chances[2] < 0 {
        2
    } else {
        3
    };
    let mut chances = [0; 3];
    for (index, value) in chances.iter_mut().enumerate().take(count) {
        if !(0..=100).contains(&context.chances[index]) {
            return Err(1);
        }
        *value = context.chances[index];
    }
    // 保存番号なしでは取得済み判定を省く。候補数は元modeから先に決める。
    let enabled = (0..400).contains(&context.save_id);
    Ok(Some(Input {
        count: count as i32,
        mode: if !enabled && (context.mode == 1 || context.mode == 2) {
            0
        } else {
            context.mode
        },
        acquired: context.acquired,
        radar: context.radar,
        chances,
        rolls: context.rolls,
    }))
}
#[repr(C)]
#[derive(Default, Serialize, Deserialize, Debug, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct Output {
    pub winner: i32,
    pub consumed: i32,
    pub mark_acquired: i32,
    pub radar_blocked: i32,
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct WeightedFinishInput {
    pub mode: i32,
    pub seen: i32,
    pub radar: i32,
    pub winner: i32,
}
#[repr(C)]
#[derive(Default, Serialize, Deserialize, Debug, PartialEq)]
#[serde(rename_all = "camelCase")]
pub struct WeightedFinishOutput {
    pub grant_column: i32,
    pub mark_history: i32,
    pub radar_blocked: i32,
}
unsafe extern "C" {
    fn kbcs_core_legend_reward_pick(input: *const Input, output: *mut Output) -> u32;
    fn kbcs_core_stage_reward_pick(input: *const Input, output: *mut Output) -> u32;
    fn kbcs_core_reward_weight_total(weights: *const i32, count: i32, total: *mut i32) -> u32;
    fn kbcs_core_reward_weight_pick(
        weights: *const i32,
        count: i32,
        roll: i32,
        winner: *mut i32,
    ) -> u32;
    fn kbcs_core_reward_weight_finish(
        input: *const WeightedFinishInput,
        output: *mut WeightedFinishOutput,
    ) -> u32;
}
pub fn weight_finish(input: &WeightedFinishInput) -> Result<WeightedFinishOutput, u32> {
    let mut output = WeightedFinishOutput::default();
    // 選択後だけ呼び、履歴・付与・結果行の順序は所有ランタイムが管理する。
    let code = unsafe { kbcs_core_reward_weight_finish(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn stage_pick(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 候補数と、報酬種別に対応する取得済み状態を解決してから渡す。
    let code = unsafe { kbcs_core_stage_reward_pick(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn weight_total(weights: &[i32]) -> Result<i32, u32> {
    if weights.len() > 10 {
        return Err(1);
    }
    let mut total = 0;
    let code = unsafe {
        kbcs_core_reward_weight_total(weights.as_ptr(), weights.len() as i32, &mut total)
    };
    if code == 0 { Ok(total) } else { Err(code) }
}
pub fn weight_pick(weights: &[i32], roll: i32) -> Result<usize, u32> {
    if weights.len() > 10 {
        return Err(1);
    }
    let mut winner = 0;
    let code = unsafe {
        kbcs_core_reward_weight_pick(weights.as_ptr(), weights.len() as i32, roll, &mut winner)
    };
    if code == 0 {
        Ok(winner as usize)
    } else {
        Err(code)
    }
}
pub fn legend_pick(input: &Input) -> Result<Output, u32> {
    let mut output = Output::default();
    // 抽選値を借用し、所持数と取得済み状態の書込みは呼出側へ返す。
    let code = unsafe { kbcs_core_legend_reward_pick(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_reward_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/reward-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let expected: Output = serde_json::from_value(vector.clone()).unwrap();
        assert_eq!(legend_pick(&input).unwrap(), expected);
        input.mode = 2;
        let mut output = Output {
            winner: 99,
            ..Output::default()
        };
        assert_eq!(
            unsafe { kbcs_core_legend_reward_pick(&input, &mut output) },
            1
        );
        assert_eq!(output.winner, 99);
    }
    let events: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/event-reward-vectors.json"
    ))
    .unwrap();
    for vector in events["vectors"].as_array().unwrap() {
        let input: Input = serde_json::from_value(vector["input"].clone()).unwrap();
        let context: StageContext = serde_json::from_value(vector["context"].clone()).unwrap();
        assert_eq!(prepare_stage_input(&context).unwrap().unwrap(), input);
        let expected: Output = serde_json::from_value(vector.clone()).unwrap();
        assert_eq!(stage_pick(&input).unwrap(), expected);
    }
    for vector in events["headerNormalizations"].as_array().unwrap() {
        if vector["kind"] != "acquisition" {
            continue;
        }
        let context = StageContext {
            mode: 1,
            save_id: vector["raw"].as_i64().unwrap() as i32,
            acquired: 0,
            radar: 0,
            chances: [100, -1, -1],
            rolls: [0; 3],
        };
        let input = prepare_stage_input(&context).unwrap().unwrap();
        assert_eq!(input.mode, if vector["resolved"] == -1 { 0 } else { 1 });
    }
    for vector in events["weighted"].as_array().unwrap() {
        let weights: Vec<i32> = serde_json::from_value(vector["weights"].clone()).unwrap();
        if weights.len() == 11 {
            assert_eq!(weight_total(&weights), Err(1));
            continue;
        }
        let total = vector["total"].as_i64().unwrap() as i32;
        assert_eq!(weight_total(&weights).unwrap(), total);
        assert_eq!(
            weight_pick(&weights, vector["roll"].as_i64().unwrap() as i32).unwrap(),
            vector["winner"].as_u64().unwrap() as usize
        );
        assert_eq!(weight_pick(&weights, total), Err(1));
    }
    assert_eq!(weight_total(&[0, 0]), Err(1));
    assert_eq!(weight_total(&[-1, 2]), Err(1));
    assert_eq!(weight_total(&[i32::MAX, 1]), Err(2));
    let invalid = Input {
        count: 2,
        mode: -2,
        acquired: 0,
        radar: 0,
        chances: [100; 3],
        rolls: [0; 3],
    };
    assert!(matches!(stage_pick(&invalid), Err(1)));
    let finish: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/reward-finish-vectors.json"
    ))
    .unwrap();
    for vector in finish["vectors"].as_array().unwrap() {
        let input: WeightedFinishInput = serde_json::from_value(vector["input"].clone()).unwrap();
        let expected: WeightedFinishOutput = serde_json::from_value(vector.clone()).unwrap();
        assert_eq!(weight_finish(&input).unwrap(), expected);
    }
}
