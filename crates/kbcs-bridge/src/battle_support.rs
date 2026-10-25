use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct CastleInput {
    pub facility_level: i32,
    pub development_level: i32,
    pub treasure_bonus: i32,
    pub combo_percent: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct CastleOutput {
    pub facility: i32,
    pub development: i32,
    pub before_combo: i32,
    pub maximum: i32,
    pub sniper: i32,
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct SniperInput {
    pub castle_maximum: i32,
    pub metal: i32,
    pub dodge_active: i32,
    pub dodge_chance: i32,
    pub roll: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct SniperOutput {
    pub damage: i32,
    pub knockback: i32,
    pub random_consumed: i32,
    pub dodged: i32,
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct DeployCostInput {
    pub raw: i32,
    pub reduction: i32,
    pub chapter: i32,
    pub multiplier: i32,
    pub fixed: i32,
    pub rarity_rate: i32,
}
#[repr(C)]
#[derive(Clone, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct DeploymentInput {
    pub rarity: i32,
    pub slot: i32,
    pub cost: i32,
    pub mask: i32,
    pub slots: i32,
    pub minimum: i32,
    pub maximum: i32,
    pub group_type: i32,
    pub in_group: i32,
    pub phase: i32,
    pub rarity_limit: i32,
    pub preceding: i32,
}
pub fn deploy_cost(input: &DeployCostInput) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_deploy_cost(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn deployment(input: &DeploymentInput) -> Result<u32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_deployment(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
unsafe extern "C" {
    fn kbcs_core_deploy_cost(input: *const DeployCostInput, output: *mut i32) -> u32;
    fn kbcs_core_deployment(input: *const DeploymentInput, output: *mut u32) -> u32;
    fn kbcs_core_castle_health(input: *const CastleInput, output: *mut CastleOutput) -> u32;
    fn kbcs_core_sniper_hit(input: *const SniperInput, output: *mut SniperOutput) -> u32;
    fn kbcs_core_battle_steps(speed: i32, paused: i32, output: *mut i32) -> u32;
}
pub fn castle(input: &CastleInput) -> Result<CastleOutput, u32> {
    let mut output = CastleOutput::default();
    let code = unsafe { kbcs_core_castle_health(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn sniper(input: &SniperInput) -> Result<SniperOutput, u32> {
    let mut output = SniperOutput::default();
    let code = unsafe { kbcs_core_sniper_hit(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn steps(speed: i32, paused: bool) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_battle_steps(speed, i32::from(paused), &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_support_witnesses() {
    let data: serde_json::Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/battle-support-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in data["castles"].as_array().unwrap() {
        let input = serde_json::from_value(case["input"].clone()).unwrap();
        let output = castle(&input).unwrap();
        assert_eq!(serde_json::json!(output.maximum), case["maximum"]);
        assert_eq!(serde_json::json!(output.sniper), case["sniper"]);
    }
    for case in data["snipers"].as_array().unwrap() {
        let input = serde_json::from_value(case["input"].clone()).unwrap();
        assert_eq!(
            serde_json::to_value(sniper(&input).unwrap()).unwrap(),
            case["output"]
        );
    }
    for case in data["deployments"].as_array().unwrap() {
        let input = serde_json::from_value(case["input"].clone()).unwrap();
        assert_eq!(
            serde_json::json!(deployment(&input).unwrap() == 0),
            case["allowed"],
            "{case}"
        );
    }
    for case in data["costs"].as_array().unwrap() {
        let input = serde_json::from_value(case["input"].clone()).unwrap();
        assert_eq!(
            serde_json::json!(deploy_cost(&input).unwrap()),
            case["cost"],
            "{case}"
        );
    }
    assert_eq!(steps(3, false), Ok(3));
    assert_eq!(steps(3, true), Ok(0));
    assert!(steps(4, false).is_err());
}
