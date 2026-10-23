use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Default, Deserialize, Serialize, Debug, PartialEq)]
pub struct Identity {
    pub kind: i32,
    pub index: i32,
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct CurrentKind {
    pub mode: i32,
    pub selected_kind: i32,
    pub zombie: i32,
    pub invasion: i32,
    pub invasion_zombie: i32,
    pub ignore: i32,
    pub ex_override: i32,
    pub ex_marker: i32,
}
unsafe extern "C" {
    fn kbcs_core_stage_current_kind(input: *const CurrentKind, output: *mut i32) -> u32;
    fn kbcs_core_map_decode(id: i32, output: *mut Identity) -> u32;
    fn kbcs_core_map_encode(input: *const Identity, output: *mut i32) -> u32;
}
pub fn decode(id: i32) -> Result<Identity, u32> {
    let mut output = Identity::default();
    let code = unsafe { kbcs_core_map_decode(id, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub fn encode(input: &Identity) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_map_encode(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

pub fn current_kind(input: &CurrentKind) -> Result<i32, u32> {
    let mut output = 0;
    let code = unsafe { kbcs_core_stage_current_kind(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Context {
    pub mode: i32,
    pub kind: i32,
    pub index: i32,
    pub stage: i32,
    pub battle: i32,
    pub zombie: i32,
    pub invasion: i32,
    pub invasion_zombie: i32,
    pub quest_reference: Option<i32>,
    pub labyrinth_template: Option<i32>,
    pub ex_index: i32,
    pub ex_stage: i32,
}

pub fn resolve(context: &Context) -> Result<String, u32> {
    let c = context;
    if !(0..1000).contains(&c.index)
        || !(0..100).contains(&c.stage)
        || [c.battle, c.zombie, c.invasion, c.invasion_zombie]
            .iter()
            .any(|v| !(0..=1).contains(v))
    {
        return Err(1);
    }
    if c.mode == 99 && c.battle == 1 && c.kind == -8 {
        if !(0..1000).contains(&c.ex_index) || !(0..100).contains(&c.ex_stage) {
            return Err(1);
        }
        return Ok(format!(
            "Data/stageEX{:03}_{:02}.csv",
            c.ex_index, c.ex_stage
        ));
    }
    if c.mode != 3 {
        if c.battle != 1 || !(0..=9).contains(&c.mode) {
            return Err(1);
        }
        // 原本はゾンビ、宇宙襲来、宇宙ゾンビ襲来の順で優先する。
        if c.zombie != 0 {
            return Ok(format!("Data/stageZ{:02}_{:02}.csv", c.mode, c.stage));
        }
        if c.invasion != 0 {
            return Ok(format!("Data/stageSpace{:02}_Invasion_00.csv", c.mode));
        }
        if c.invasion_zombie != 0 {
            return Ok(format!("Data/stageSpace{:02}_Invasion_Z_00.csv", c.mode));
        }
        return match (c.kind, c.mode) {
            (-2, 0..=2) => Ok(format!("Data/stage{:02}.csv", c.stage)),
            (-3, 4..=6) => Ok(format!("Data/stageW{:02}_{:02}.csv", c.mode, c.stage)),
            (-7, 7..=9) => Ok(format!("Data/stageSpace{:02}_{:02}.csv", c.mode, c.stage)),
            _ => Err(1),
        };
    }
    if c.zombie != 0 || c.invasion != 0 || c.invasion_zombie != 0 {
        return Err(1);
    }
    let (prefix, index, stage) = match c.kind {
        0 => ("RN", c.index, c.stage),
        1 => ("RS", c.index, c.stage),
        2 => ("RC", c.index, c.stage),
        3 => ("RT", c.index, c.stage),
        4 if c.battle == 1 => ("RR", c.index, c.stage),
        -4 => ("RV", c.index, c.stage),
        -6 => ("RM", c.index, c.stage),
        -8 if c.battle == 0 => ("EX", c.index, c.stage),
        -9 => ("RNA", c.index, c.stage),
        -10 => ("RB", c.index, c.stage),
        -11 if c.battle == 1 => {
            // 抽選済みの参照元を必須にし、クエスト番号から推測しない。
            let reference = c
                .quest_reference
                .filter(|v| (0..100000).contains(v))
                .ok_or(1u32)?;
            ("RN", reference / 100, reference % 100)
        }
        -16 => ("RA", c.index, c.stage),
        -17 => ("RH", c.index, c.stage),
        -18 => ("RCA", c.index, c.stage),
        -19 => ("DM", c.index, c.stage),
        -20 => ("RQ", c.index, c.stage),
        -21 => {
            let template = c
                .labyrinth_template
                .filter(|v| (0..1000).contains(v))
                .ok_or(1u32)?;
            ("L", c.index, template)
        }
        -22 => ("RND", c.index, c.stage),
        -23 => ("RSR", c.index, c.stage),
        -24 => ("G", c.index, c.stage),
        -26 => ("RPR", c.index, c.stage),
        _ => return Err(1),
    };
    Ok(format!("Data/stage{prefix}{index:03}_{stage:02}.csv"))
}

#[test]
fn native_stage_source_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/stage-source-vectors.json"
    ))
    .unwrap();
    for vector in fixture["mapping"].as_array().unwrap() {
        let id = vector["id"].as_i64().unwrap() as i32;
        let identity = decode(id).unwrap();
        assert_eq!(identity.kind, vector["kind"].as_i64().unwrap() as i32);
        assert_eq!(identity.index, vector["index"].as_i64().unwrap() as i32);
        if identity.kind != -1 {
            assert_eq!(encode(&identity).unwrap(), id);
        }
    }
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut context: Context = serde_json::from_value(vector["context"].clone()).unwrap();
        assert_eq!(
            resolve(&context).unwrap(),
            format!("Data/{}", vector["file"].as_str().unwrap())
        );
        if context.kind == -11 {
            context.quest_reference = None;
            assert!(resolve(&context).is_err());
        } else if context.kind == -21 {
            context.labyrinth_template = None;
            assert!(resolve(&context).is_err());
        }
    }
    for vector in fixture["current"].as_array().unwrap() {
        let mut value = vector.clone();
        value.as_object_mut().unwrap().remove("kind");
        let input: CurrentKind = serde_json::from_value(value).unwrap();
        assert_eq!(
            current_kind(&input).unwrap(),
            vector["kind"].as_i64().unwrap() as i32
        );
    }
    assert!(decode(-1).is_err());
    assert!(decode(40000).is_err());
    assert!(encode(&Identity { kind: -2, index: 3 }).is_err());
}
