use super::*;
use serde_json::Value;

fn number(value: &Value, key: &str, default: i32) -> i32 {
    value[key].as_i64().map_or(default, |v| v as i32)
}
fn fixture() -> Value {
    serde_json::from_str(include_str!(
        "../../../../native/kbcs-core/tests/production-vectors.json"
    ))
    .unwrap()
}

#[test]
fn native_production_witnesses() {
    let mut output = 123;
    let overflow = RechargeInput {
        base: 0,
        talent: 0,
        research_level: 0,
        treasure: i32::MAX,
        combo: 1,
        stage_percent: 100,
        override_frames: -1,
    };
    assert_eq!(
        unsafe { kbcs_core_production_recharge(&overflow, &mut output) },
        2
    );
    assert_eq!(output, 123);
    let fixture = fixture();
    for vector in fixture["recharges"].as_array().unwrap() {
        assert_eq!(
            recharge(&serde_json::from_value::<RechargeInput>(vector["input"].clone()).unwrap()),
            Ok(number(vector, "value", -1))
        );
    }
    for vector in fixture["vectors"].as_array().unwrap() {
        let input = &vector["input"];
        let expected = &vector["output"];
        let mut state = State {
            money: number(input, "money", 100000),
            ..State::default()
        };
        state.wait[2] = number(input, "wait", 0);
        state.maximum[2] = 17;
        state.produced[2] = number(input, "produced", 0);
        let mut generated = Vec::new();
        let mut random = Random::new(0x12345678).unwrap();
        let result = deploy(
            &DeployInput {
                spawn: SpawnRequest {
                    raw: 42,
                    level_index: 36,
                    form: 2,
                    ..SpawnRequest::default()
                },
                slot: 2,
                present: number(input, "present", 1),
                allowed: number(input, "allowed", 1),
                blocked: number(input, "blocked", 0),
                cost: number(input, "cost", 7500),
                recharge: number(input, "recharge", 181),
                reduction: number(input, "reduction", -1),
                recharge_enabled: 1,
                notify_failure: number(input, "notifyFailure", 1),
                ..DeployInput::default()
            },
            &mut state,
            &mut random,
            &mut |request, _| {
                generated.push([
                    request.side,
                    request.raw,
                    request.level_index,
                    request.layer_min,
                    request.layer_max,
                    request.form,
                    request.row,
                ]);
                number(input, "result", 1)
            },
        )
        .unwrap();
        assert_eq!(
            serde_json::to_value(generated).unwrap(),
            expected["generated"],
            "{input}"
        );
        assert_eq!(state.money, number(expected, "money", -1));
        assert_eq!(state.wait[2], number(expected, "wait", -1));
        assert_eq!(state.maximum[2], number(expected, "maximum", -1));
        assert_eq!(state.produced[2], number(expected, "produced", -1));
        assert_eq!(state.last_cost[2], number(expected, "lastCost", -1));
        let sound = expected["calls"]
            .as_array()
            .unwrap()
            .iter()
            .find_map(|v| {
                v.as_array()
                    .filter(|v| v[0] == "sound")
                    .map(|v| v[1].as_i64().unwrap() as i32)
            })
            .unwrap_or(-1);
        assert_eq!(result.sound, sound);
        assert_eq!(random.state(), 0x12345678);
    }
    for vector in fixture["placements"].as_array().unwrap() {
        let mut occupied = [1; 51];
        occupied[number(vector, "free", 0) as usize] = 0;
        let mut random = Random::new(0x12345678).unwrap();
        let output = prepare(
            &SpawnRequest {
                side: number(vector, "side", 0),
                raw: number(vector, "raw", 0),
                level_index: 36,
                form: 2,
                layer_min: number(vector, "low", 0),
                layer_max: number(vector, "high", 0),
                row: 0,
            },
            &Geometry {
                stage_width: 24000,
                castle_slot: number(vector, "castle", -1),
            },
            &occupied,
            &mut random,
        )
        .unwrap();
        assert_eq!(output.slot, number(vector, "slot", 0));
        if output.slot > 0 {
            assert_eq!(
                serde_json::json!([output.x, output.y, output.layer, 36]),
                vector["placement"]
            );
        }
        assert_eq!(u64::from(random.state()), vector["state"].as_u64().unwrap());
    }
    for vector in fixture["boss"].as_array().unwrap() {
        assert_eq!(
            boss_position(
                number(vector, "castleX", 0),
                number(vector, "scale", 0),
                number(vector, "offset", 0)
            ),
            Ok(number(vector, "x", 0))
        );
    }
    for vector in fixture["clocks"].as_array().unwrap() {
        let mut state = State::default();
        state.wait[2] = number(vector, "wait", 0);
        state.maximum[2] = 17;
        let ready = clock(&mut state, &[number(vector, "recharge", 0); 10]).unwrap();
        assert_eq!(state.wait[2], number(vector, "next", 0));
        assert_eq!(state.maximum[2], number(vector, "maximum", 0));
        assert_eq!(ready != 0, vector["ready"].as_bool().unwrap());
    }
}

#[test]
fn native_continuous_generation_and_failure_contract() {
    let fixture: Value = serde_json::from_str(include_str!(
        "../../../../native/kbcs-core/tests/stage-continuous-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let rows = [serde_json::from_value::<stage::Row>(vector["row"].clone()).unwrap()];
        let mut states = [stage::State::default()];
        let mut context = stage::Context {
            max_enemies: 50,
            castle_hp: 100,
            castle_max_hp: 100,
            ..stage::Context::default()
        };
        let mut seen = [0];
        let mut random = Random::new(vector["seed"].as_u64().unwrap() as u32).unwrap();
        let mut occupied = [1; 51];
        if vector["success"].as_bool().unwrap() {
            occupied[1] = 0;
        }
        for step in vector["steps"].as_array().unwrap() {
            let output = enemy_tick(
                &rows,
                &mut states,
                &mut context,
                &mut seen,
                &mut random,
                &mut |request, random| {
                    assert_eq!(request.side, 1);
                    assert_eq!(request.row, 0);
                    assert_eq!(request.raw, 2);
                    prepare(
                        request,
                        &Geometry {
                            stage_width: 24000,
                            castle_slot: -1,
                        },
                        &occupied,
                        random,
                    )
                    .unwrap()
                    .slot
                },
            )
            .unwrap();
            assert_eq!(output.row, 0);
            assert_eq!(output.slot > 0, vector["success"].as_bool().unwrap());
            assert_eq!(
                serde_json::json!([[states[0].wait, states[0].spawned, states[0].kills]]),
                step["states"]
            );
            assert_eq!(
                i64::from(context.global_wait),
                step["globalWait"].as_i64().unwrap()
            );
            assert_eq!(u64::from(random.state()), step["state"].as_u64().unwrap());
            assert_eq!(i64::from(seen[0]), step["seen"].as_i64().unwrap());
        }
    }

    // 生成内部で消費した乱数は失敗でも戻さず、成功後の間隔乱数・seenは進めない。
    let rows = [stage::Row([2, 0, 0, 3, 7, 100, 0, 9, 0, 100, 0, 0, 0, 0])];
    let mut states = [stage::State::default()];
    let mut context = stage::Context {
        max_enemies: 50,
        castle_hp: 100,
        castle_max_hp: 100,
        ..stage::Context::default()
    };
    let mut seen = [0];
    let mut random = Random::new(0x12345678).unwrap();
    let mut expected = Random::new(random.state()).unwrap();
    expected.bounded(10).unwrap();
    let output = enemy_tick(
        &rows,
        &mut states,
        &mut context,
        &mut seen,
        &mut random,
        &mut |_, random| {
            random.bounded(10).unwrap();
            -1
        },
    )
    .unwrap();
    assert_eq!(output.slot, -1);
    assert_eq!(random.state(), expected.state());
    assert_eq!(states[0].spawned, 0);
    assert_eq!(seen, [0]);
    assert_eq!(context.global_wait, -1);

    // 敵城行は生成失敗でも消費、開始時の全体抽選は空の出現表でも行う。
    let initial = start(
        &rows,
        &mut states,
        &Start {
            global_min: 3,
            global_max: 3,
            castle_raw: 2,
        },
        &mut random,
        &mut |_, _| -1,
    )
    .unwrap();
    assert_eq!(initial.0.castle_row, 0);
    assert_eq!(initial.0.global_wait, 3);
    assert_eq!(
        states[0],
        stage::State {
            wait: 1,
            spawned: 1,
            kills: 0
        }
    );
    expected.bounded(1).unwrap();
    assert_eq!(random.state(), expected.state());
    start(
        &[],
        &mut [],
        &Start {
            global_min: 0,
            global_max: 0,
            castle_raw: 0,
        },
        &mut random,
        &mut |_, _| panic!("no actor"),
    )
    .unwrap();
    expected.bounded(1).unwrap();
    assert_eq!(random.state(), expected.state());

    let mut state = State {
        money: 100000,
        ..State::default()
    };
    let before = state.clone();
    let input = DeployInput {
        spawn: SpawnRequest {
            raw: 2,
            ..SpawnRequest::default()
        },
        slot: 0,
        present: 1,
        allowed: 1,
        cost: 7500,
        recharge: 181,
        reduction: -1,
        recharge_enabled: 1,
        ..DeployInput::default()
    };
    let caught = std::panic::catch_unwind(AssertUnwindSafe(|| {
        let _ = deploy(&input, &mut state, &mut random, &mut |_, _| {
            panic!("constructor")
        });
    }));
    assert!(caught.is_err());
    assert_eq!(state, before);
    let unsupported = DeployInput {
        summon_mode: 1,
        ..input
    };
    assert_eq!(
        deploy(&unsupported, &mut state, &mut random, &mut |_, _| panic!(
            "unsupported"
        )),
        Err(4)
    );
    assert_eq!(state, before);
}
