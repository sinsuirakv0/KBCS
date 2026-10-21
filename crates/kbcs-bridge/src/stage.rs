use serde::Deserialize;

#[repr(C)]
#[derive(Clone, Copy, Debug, Deserialize)]
#[serde(transparent)]
pub struct Row(pub [i32; 14]);

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct State {
    pub wait: i32,
    pub spawned: i32,
    pub kills: i32,
}

#[repr(C)]
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub struct Context {
    pub global_wait: i32,
    pub kill_delta: i32,
    pub active_enemies: i32,
    pub max_enemies: i32,
    pub castle_hp: i32,
    pub castle_max_hp: i32,
    pub castle_damage: i32,
    pub damage_condition: i32,
    pub paused: i32,
    pub global_min: i32,
    pub global_max: i32,
}

unsafe extern "C" {
    fn kbcs_core_stage_initialize(
        rows: *const Row,
        states: *mut State,
        count: i32,
        input: *const Start,
        output: *mut StartOutput,
    ) -> u32;
    fn kbcs_core_stage_tick(
        rows: *const Row,
        states: *mut State,
        count: i32,
        context: *mut Context,
        candidate: *mut i32,
    ) -> u32;
    fn kbcs_core_stage_commit(
        rows: *const Row,
        states: *mut State,
        count: i32,
        context: *mut Context,
        candidate: i32,
        global_roll: i32,
        row_roll: i32,
    ) -> u32;
}

#[repr(C)]
pub struct Start {
    pub global_min: i32,
    pub global_max: i32,
    pub global_roll: i32,
    pub castle_raw: i32,
}
#[repr(C)]
#[derive(Default)]
pub struct StartOutput {
    pub global_wait: i32,
    pub castle_row: i32,
}

pub fn initialize(rows: &[Row], states: &mut [State], input: &Start) -> Result<StartOutput, u32> {
    if rows.len() != states.len() || rows.len() > 4096 {
        return Err(1);
    }
    let mut output = StartOutput::default();
    // 初期化前の状態は読まず、全入力の検査後にだけ書き換える。
    let code = unsafe {
        kbcs_core_stage_initialize(
            rows.as_ptr(),
            states.as_mut_ptr(),
            rows.len() as i32,
            input,
            &mut output,
        )
    };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_stage_start_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/stage-start-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let value = &vector["input"];
        let rows: Vec<Row> = serde_json::from_value(value["rows"].clone()).unwrap();
        let mut states = vec![
            State {
                wait: 999,
                spawned: -1,
                kills: -1
            };
            rows.len()
        ];
        let input = Start {
            global_min: value["minimum"].as_i64().unwrap() as i32,
            global_max: value["maximum"].as_i64().unwrap() as i32,
            global_roll: value["roll"].as_i64().unwrap() as i32,
            castle_raw: if value["modeFlag"].as_i64().unwrap_or(0) == 0 {
                value["castleRaw"].as_i64().unwrap_or(0) as i32
            } else {
                0
            },
        };
        let result = initialize(&rows, &mut states, &input).unwrap();
        let expected: Vec<[i32; 3]> =
            serde_json::from_value(vector["result"]["states"].clone()).unwrap();
        assert_eq!(
            states
                .iter()
                .map(|state| [state.wait, state.spawned, state.kills])
                .collect::<Vec<_>>(),
            expected
        );
        assert_eq!(
            i64::from(result.global_wait),
            vector["result"]["globalWait"].as_i64().unwrap()
        );
        let castle: Vec<i32> =
            serde_json::from_value(vector["result"]["castleRows"].clone()).unwrap();
        assert_eq!(result.castle_row, castle.first().copied().unwrap_or(-1));
        let before = states.clone();
        let invalid = Start {
            global_roll: 99,
            ..input
        };
        assert!(matches!(initialize(&rows, &mut states, &invalid), Err(1)));
        assert_eq!(states, before);
    }
}

pub fn tick(
    rows: &[Row],
    states: &mut [State],
    context: &mut Context,
) -> Result<Option<usize>, u32> {
    if rows.len() != states.len() || rows.len() > 4096 {
        return Err(1);
    }
    let mut candidate = -1;
    // バッファは呼出中だけ借用し、状態の所有権は呼出側に残す。
    let code = unsafe {
        kbcs_core_stage_tick(
            rows.as_ptr(),
            states.as_mut_ptr(),
            rows.len() as i32,
            context,
            &mut candidate,
        )
    };
    if code == 0 {
        Ok((candidate >= 0).then_some(candidate as usize))
    } else {
        Err(code)
    }
}

pub fn commit(
    rows: &[Row],
    states: &mut [State],
    context: &mut Context,
    candidate: usize,
    global_roll: i32,
    row_roll: i32,
) -> Result<(), u32> {
    if rows.len() != states.len() || rows.len() > 4096 || candidate >= rows.len() {
        return Err(1);
    }
    let code = unsafe {
        kbcs_core_stage_commit(
            rows.as_ptr(),
            states.as_mut_ptr(),
            rows.len() as i32,
            context,
            candidate as i32,
            global_roll,
            row_roll,
        )
    };
    if code == 0 { Ok(()) } else { Err(code) }
}

#[test]
fn native_stage_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/stage-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let input = &vector["input"];
        let number = |key: &str, default| input[key].as_i64().map_or(default, |v| v as i32);
        let rows: Vec<Row> = serde_json::from_value(input["rows"].clone()).unwrap();
        let initial: Vec<[i32; 3]> = serde_json::from_value(input["states"].clone()).unwrap();
        let mut states: Vec<State> = initial
            .iter()
            .map(|s| State {
                wait: s[0],
                spawned: s[1],
                kills: s[2],
            })
            .collect();
        let mut context = Context {
            global_wait: number("globalWait", 0),
            kill_delta: number("kills", 0),
            active_enemies: number("active", 0),
            max_enemies: number("maximum", 50),
            castle_hp: number("castleHp", 100),
            castle_max_hp: 100,
            castle_damage: number("castleDamage", 0),
            damage_condition: i32::from(input["damageCondition"] == true),
            paused: i32::from(input["paused"] == true),
            global_min: 3,
            global_max: 7,
        };
        let candidate = tick(&rows, &mut states, &mut context).unwrap();
        let expected_rows: Vec<usize> =
            serde_json::from_value(vector["result"]["spawnedRows"].clone()).unwrap();
        assert_eq!(
            candidate.into_iter().collect::<Vec<_>>(),
            expected_rows,
            "{}",
            input["name"]
        );
        if let Some(index) = candidate
            && number("spawnResult", 0) >= 0
        {
            let maximum = input["randomMaximum"] == true;
            commit(
                &rows,
                &mut states,
                &mut context,
                index,
                if maximum { 4 } else { 0 },
                if maximum {
                    rows[index].0[4] - rows[index].0[3]
                } else {
                    0
                },
            )
            .unwrap();
        }
        let actual: Vec<[i32; 3]> = states
            .iter()
            .map(|s| [s.wait, s.spawned, s.kills])
            .collect();
        assert_eq!(
            serde_json::json!(actual),
            vector["result"]["states"],
            "{}",
            input["name"]
        );
        assert_eq!(
            serde_json::json!(context.global_wait),
            vector["result"]["globalWait"]
        );
        assert_eq!(context.kill_delta, 0);
    }
    // 無効な入力では、部分更新して呼出側の状態を壊さない。
    let rows = [Row([2, 0, 0, 10, 20, 100, 0, 9, 0, 100, 0, 0, 0, 0])];
    let mut states = [State {
        wait: i32::MIN,
        ..Default::default()
    }];
    let mut context = Context {
        max_enemies: 50,
        castle_max_hp: 100,
        global_min: 3,
        global_max: 7,
        ..Default::default()
    };
    let before = (states, context);
    assert_eq!(tick(&rows, &mut states, &mut context), Err(2));
    assert_eq!((states, context), before);
    states[0].wait = 0;
    let before = (states, context);
    assert_eq!(commit(&rows, &mut states, &mut context, 0, 5, 0), Err(1));
    assert_eq!((states, context), before);
}
