pub mod actor;
pub mod battle;
pub mod battle_screen;
use serde::{Deserialize, Serialize};

pub mod battle_support;
pub mod enemy;
pub mod experience;
pub mod inventory;
pub mod materials;
pub mod motion;
pub mod production;
pub mod random;
pub mod reward;
pub mod score;
pub mod stage;
pub mod stage_source;
pub mod transition;

#[repr(C)]
#[derive(Clone, Copy, Default, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct StatInput {
    pub base: i32,
    pub growth: i32,
    pub treasure: i32,
    pub combo: i32,
    pub talent: i32,
    pub extra: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct StatOutput {
    pub stages: [i64; 6],
}

#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct AttackPreparation {
    pub attack: i32,
    pub kind: i32,
    pub percent: i32,
    pub wave_percent: i32,
}
pub fn prepare_attack(input: &AttackPreparation) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_prepare_attack(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[repr(C)]
#[derive(Clone, Copy, Deserialize)]
#[serde(default, rename_all = "camelCase", deny_unknown_fields)]
pub struct HitInput {
    pub attack: i32,
    pub raw_attack: i32,
    pub critical: i32,
    pub strengthen: i32,
    pub weaken: i32,
    pub savage: i32,
    pub abilities: i32,
    pub fruit: i32,
    pub castle: i32,
    pub castle_breaker: i32,
    pub metal: i32,
    pub blocked: i32,
    pub strong_combo: i32,
    pub massive_combo: i32,
    pub resistant_combo: i32,
    pub witch_combo: i32,
    pub eva_combo: i32,
    pub strong_orb: i32,
    pub massive_orb: i32,
    pub resistant_orb: i32,
    pub attack_orb: i32,
    pub defense_orb: i32,
    pub behemoth_rate: i32,
    pub sage_rate: i32,
    pub base_reduction: i32,
    pub decoration_reduction: i32,
    pub resistance: i32,
    pub immune: i32,
    pub kill_strengthen: i32,
    pub villain_rate: i32,
}
impl Default for HitInput {
    fn default() -> Self {
        Self {
            attack: 0,
            raw_attack: 0,
            critical: 0,
            strengthen: 0,
            weaken: 100,
            savage: 0,
            abilities: 0,
            fruit: 0,
            castle: 0,
            castle_breaker: 0,
            metal: 0,
            blocked: 0,
            strong_combo: 0,
            massive_combo: 0,
            resistant_combo: 0,
            witch_combo: 0,
            eva_combo: 0,
            strong_orb: 0,
            massive_orb: 0,
            resistant_orb: 0,
            attack_orb: 0,
            defense_orb: 0,
            behemoth_rate: 0,
            sage_rate: 0,
            base_reduction: 0,
            decoration_reduction: 0,
            resistance: 0,
            immune: 0,
            kill_strengthen: 0,
            villain_rate: 0,
        }
    }
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct HitOutput {
    pub damage: i64,
    pub stages: [i64; 21],
}
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct DamageInput {
    pub hit: HitInput,
    pub critical_chance: i32,
    pub savage_chance: i32,
    pub force_critical: bool,
    pub force_savage: bool,
}
#[derive(Serialize)]
pub struct DamageOutput {
    pub normal: i64,
    pub selected: HitOutput,
    pub expected: f64,
    pub outcomes: [i64; 4],
}

unsafe extern "C" {
    fn kbcs_core_prepare_attack(input: *const AttackPreparation, output: *mut i32) -> u32;
    fn kbcs_core_abi_version() -> u32;
    fn kbcs_core_ruleset_version() -> u32;
    fn kbcs_core_stat(input: *const StatInput, output: *mut StatOutput) -> u32;
    fn kbcs_core_unit_hit(input: *const HitInput, output: *mut HitOutput) -> u32;
    fn kbcs_core_enemy_hit(input: *const HitInput, output: *mut HitOutput) -> u32;
    fn kbcs_core_unit_metal_killer(hp: i32, percent: i32, output: *mut MetalKillerEvent) -> u32;
    fn kbcs_core_enemy_poison(input: *const PoisonInput, output: *mut PoisonOutput) -> u32;
    fn kbcs_core_expectation(outcomes: *const i64, critical: i32, savage: i32) -> f64;
}
pub fn abi_version() -> u32 {
    unsafe { kbcs_core_abi_version() }
}
pub fn ruleset_version() -> u32 {
    unsafe { kbcs_core_ruleset_version() }
}
pub fn stat(input: &StatInput) -> Result<StatOutput, u32> {
    let mut output = StatOutput::default();
    // PODの借用は呼出中だけ有効。C++はポインタ・状態・所有権を保持しない。
    let code = unsafe { kbcs_core_stat(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
fn calculate_hit(
    input: &HitInput,
    calculate: unsafe extern "C" fn(*const HitInput, *mut HitOutput) -> u32,
) -> Result<HitOutput, u32> {
    let mut output = HitOutput::default();
    let code = unsafe { calculate(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn unit_hit(input: &HitInput) -> Result<HitOutput, u32> {
    calculate_hit(input, kbcs_core_unit_hit)
}
pub fn enemy_hit(input: &HitInput) -> Result<HitOutput, u32> {
    calculate_hit(input, kbcs_core_enemy_hit)
}
pub fn unit_damage(input: &DamageInput) -> Result<DamageOutput, u32> {
    damage(input, unit_hit)
}
pub fn enemy_damage(input: &DamageInput) -> Result<DamageOutput, u32> {
    damage(input, enemy_hit)
}
fn damage(
    input: &DamageInput,
    calculate: fn(&HitInput) -> Result<HitOutput, u32>,
) -> Result<DamageOutput, u32> {
    if !(0..=100).contains(&input.critical_chance) || !(0..=100).contains(&input.savage_chance) {
        return Err(1);
    }
    let mut outcomes = [0; 4];
    for (index, value) in outcomes.iter_mut().enumerate() {
        let mut variant = input.hit;
        variant.critical = i32::from(index & 1 != 0 && input.critical_chance > 0);
        if index & 2 == 0 || input.savage_chance == 0 {
            variant.savage = 0;
        }
        *value = calculate(&variant)?.damage;
    }
    let mut selected = input.hit;
    selected.critical = i32::from(
        input.critical_chance > 0 && (input.force_critical || input.critical_chance == 100),
    );
    if input.savage_chance == 0 || !(input.force_savage || input.savage_chance == 100) {
        selected.savage = 0;
    }
    let expected = unsafe {
        kbcs_core_expectation(
            outcomes.as_ptr(),
            input.critical_chance,
            input.savage_chance,
        )
    };
    Ok(DamageOutput {
        normal: outcomes[0],
        selected: calculate(&selected)?,
        expected,
        outcomes,
    })
}

#[repr(C)]
#[derive(Default)]
struct MetalKillerEvent {
    damage: i64,
    remaining_basis: i32,
}
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct MetalKillerInput {
    pub hp: i32,
    pub percentages: Vec<i32>,
}
#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
pub struct MetalKillerOutput {
    pub damage: Vec<i64>,
    pub remaining_basis: i32,
}
pub fn unit_metal_killer(input: &MetalKillerInput) -> Result<MetalKillerOutput, u32> {
    if input.hp < 0 || input.percentages.len() > 64 {
        return Err(1);
    }
    let mut remaining_basis = input.hp;
    let mut damage = Vec::with_capacity(input.percentages.len());
    for &percent in &input.percentages {
        let mut output = MetalKillerEvent::default();
        let code = unsafe { kbcs_core_unit_metal_killer(remaining_basis, percent, &mut output) };
        if code != 0 {
            return Err(code);
        }
        remaining_basis = output.remaining_basis;
        damage.push(output.damage);
    }
    Ok(MetalKillerOutput {
        damage,
        remaining_basis,
    })
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct PoisonInput {
    pub max_hp: i32,
    pub percent: i32,
    pub resistance: i32,
    pub decoration_reduction: i32,
    pub immune: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct PoisonOutput {
    pub damage: i64,
    pub stages: [i64; 4],
}
pub fn enemy_poison(input: &PoisonInput) -> Result<PoisonOutput, u32> {
    let mut output = PoisonOutput::default();
    let code = unsafe { kbcs_core_enemy_poison(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_witnesses() {
    assert_eq!(abi_version(), 4);
    assert_eq!(ruleset_version(), 1507021);
    let fixture: serde_json::Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/native-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for row in fixture["growth"].as_array().unwrap() {
        let input = StatInput {
            base: row["base"].as_i64().unwrap() as i32,
            growth: row["growth"].as_i64().unwrap() as i32,
            treasure: row["treasure"].as_i64().unwrap() as i32,
            combo: row["combo"].as_i64().unwrap() as i32,
            talent: row["talent"].as_i64().unwrap() as i32,
            extra: row["extra"].as_i64().unwrap() as i32,
        };
        assert_eq!(
            stat(&input).unwrap().stages[5],
            row["result"].as_i64().unwrap()
        );
    }
    for row in fixture["vectors"].as_array().unwrap() {
        let input: HitInput = serde_json::from_value(row["input"].clone()).unwrap();
        let output = (if row["incoming"] == 1 {
            enemy_hit(&input)
        } else {
            unit_hit(&input)
        })
        .unwrap();
        assert_eq!(
            output.damage,
            row["damage"].as_i64().unwrap(),
            "{}",
            row["input"]
        );
        for (stage, value) in row["checkpoints"].as_object().unwrap() {
            assert_eq!(
                output.stages[stage.parse::<usize>().unwrap()],
                value.as_i64().unwrap(),
                "stage {stage}: {}",
                row["input"]
            );
        }
    }
    for row in fixture["preparations"].as_array().unwrap() {
        let input: AttackPreparation = serde_json::from_value(row["input"].clone()).unwrap();
        assert_eq!(
            i64::from(prepare_attack(&input).unwrap()),
            row["result"].as_i64().unwrap()
        );
    }
    for row in fixture["poison"].as_array().unwrap() {
        let input: PoisonInput = serde_json::from_value(row["input"].clone()).unwrap();
        assert_eq!(
            enemy_poison(&input).unwrap().damage,
            row["damage"].as_i64().unwrap()
        );
    }
    for row in fixture["metalKiller"]["vectors"].as_array().unwrap() {
        let input = MetalKillerInput {
            hp: row["hp"].as_i64().unwrap() as i32,
            percentages: serde_json::from_value(row["percentages"].clone()).unwrap(),
        };
        let output = unit_metal_killer(&input).unwrap();
        assert_eq!(
            serde_json::to_value(output).unwrap(),
            serde_json::json!({"damage":row["damage"],"remainingBasis":row["remainingBasis"]})
        );
    }
    let mut value = HitInput {
        attack: 13,
        raw_attack: 8,
        weaken: 57,
        critical: 1,
        strengthen: 17,
        savage: 43,
        abilities: 1,
        fruit: 147,
        strong_combo: 15,
        ..Default::default()
    };
    assert_eq!(unit_hit(&value).unwrap().damage, 44);
    value = HitInput {
        attack: 13,
        abilities: 7,
        fruit: 147,
        ..Default::default()
    };
    assert_eq!(unit_hit(&value).unwrap().damage, 400);
    value = HitInput {
        attack: 13,
        raw_attack: 8,
        metal: 1,
        attack_orb: 500,
        ..Default::default()
    };
    assert_eq!(unit_hit(&value).unwrap().damage, 1);
    value.critical = 1;
    assert_eq!(unit_hit(&value).unwrap().damage, 66);
    assert!(
        stat(&StatInput {
            base: i32::MAX,
            growth: 100000,
            ..Default::default()
        })
        .is_err()
    );
    assert!(
        unit_hit(&HitInput {
            weaken: 101,
            ..Default::default()
        })
        .is_err()
    );
    // FFIを直接呼んでも、失敗時は出力を部分更新しない。
    let invalid_stat = StatInput {
        base: i32::MAX,
        growth: 100000,
        ..Default::default()
    };
    let mut stat_output = StatOutput { stages: [-1; 6] };
    assert_eq!(
        unsafe { kbcs_core_stat(&invalid_stat, &mut stat_output) },
        2
    );
    assert_eq!(stat_output.stages, [-1; 6]);
    let mut hit_output = HitOutput {
        damage: -1,
        stages: [-1; 21],
    };
    let overflowing = HitInput {
        attack: i32::MAX,
        critical: 1,
        ..Default::default()
    };
    assert_eq!(
        unsafe { kbcs_core_unit_hit(&overflowing, &mut hit_output) },
        2
    );
    assert_eq!((hit_output.damage, hit_output.stages), (-1, [-1; 21]));
    for flag in [256, 512, 1024] {
        let input = HitInput {
            attack: 13,
            abilities: flag,
            ..Default::default()
        };
        assert!(matches!(unit_hit(&input), Err(1)));
        assert!(matches!(enemy_hit(&input), Err(1)));
    }
    let mut poison_output = PoisonOutput {
        damage: -1,
        stages: [-1; 4],
    };
    let overflowing = PoisonInput {
        max_hp: i32::MAX,
        percent: 100,
        resistance: 0,
        decoration_reduction: 0,
        immune: 0,
    };
    assert_eq!(
        unsafe { kbcs_core_enemy_poison(&overflowing, &mut poison_output) },
        2
    );
    assert_eq!((poison_output.damage, poison_output.stages), (-1, [-1; 4]));
}

pub mod render;

pub mod render_effects;

pub mod cannon;
