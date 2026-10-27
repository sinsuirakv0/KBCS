use super::*;
use serde_json::Value;

fn array<const N: usize>(value: &Value) -> [i32; N] {
    let values = value.as_array().unwrap();
    assert_eq!(values.len(), N);
    std::array::from_fn(|i| values[i].as_i64().unwrap() as i32)
}
fn sparse(pool: &mut Pool, values: &Value) {
    for value in values.as_array().unwrap() {
        let index = value[0].as_u64().unwrap() as usize;
        pool.0[index / (SLOTS * WORDS)][index / WORDS % SLOTS].words[index % WORDS] =
            value[1].as_i64().unwrap() as i32;
    }
}

#[test]
fn native_actor_states() {
    let waves: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-wave-step-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in waves["records"].as_array().unwrap() {
        let rules: WaveRules = serde_json::from_value(case["rules"].clone()).unwrap();
        let mut waves = Waves::default();
        waves.0.records[0] = serde_json::from_value(case["wave"].clone()).unwrap();
        let mut segments = WaveSegments::default();
        let mut pool = Pool::default();
        sparse(&mut pool, &case["pool"]);
        let environment = Environment {
            unit_modes: [1, 0],
            castle_slot: 50,
            ..Default::default()
        };
        let mut random = Random::new(0x12345678).unwrap();
        let applied = case["applied"] == 1;
        let mut cursor = 0;
        for step in case["steps"].as_array().unwrap() {
            let target = step["frame"].as_i64().unwrap() * 2 + step["phase"].as_i64().unwrap();
            while cursor < target {
                segments
                    .step(
                        if cursor % 2 == 0 {
                            WavePhase::Advance
                        } else {
                            WavePhase::Hit
                        },
                        &mut waves,
                        pool.records_mut(),
                        &environment,
                        &rules,
                        &mut random,
                        &mut |_, _, _| Ok(applied),
                    )
                    .unwrap();
                cursor += 1;
            }
            let mut calls = Vec::new();
            let sounds = segments
                .step(
                    if step["phase"] == 0 {
                        WavePhase::Advance
                    } else {
                        WavePhase::Hit
                    },
                    &mut waves,
                    pool.records_mut(),
                    &environment,
                    &rules,
                    &mut random,
                    &mut |_, _, call| {
                        calls.push(serde_json::to_value(call).unwrap());
                        // 命中本体の返値は原本側と同じ制御値。
                        Ok(applied)
                    },
                )
                .unwrap();
            cursor += 1;
            let mut expected = Pool::default();
            sparse(&mut expected, &step["pool"]);
            assert_eq!(pool.0, expected.0);
            assert_eq!(
                serde_json::to_value(waves.0.records[0]).unwrap(),
                step["wave"]
            );
            assert_eq!(
                serde_json::to_value(segments.records()[0]).unwrap(),
                step["segments"]
            );
            assert_eq!(serde_json::to_value(calls).unwrap(), step["calls"]);
            assert_eq!(
                (0..51)
                    .map(|j| i32::from(waves.0.hits[j][0]))
                    .collect::<Vec<_>>(),
                serde_json::from_value::<Vec<i32>>(step["history"].clone()).unwrap()
            );
            assert_eq!(sounds, step["sounds"].as_i64().unwrap() as i32);
        }
    }
    let hits: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-hit-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in hits["records"].as_array().unwrap() {
        let mut owner = Hits::new().unwrap();
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        let environment: Environment = serde_json::from_value(case["environment"].clone()).unwrap();
        let context: HitContext = serde_json::from_value(case["context"].clone()).unwrap();
        let call: SecondaryHit = serde_json::from_value(case["call"].clone()).unwrap();
        let value = &case["clock"];
        let clock = Clock {
            encoded: array(&value["encoded"]),
            plain: array(&value["plain"]),
            forms: std::array::from_fn(|i| array(&value["forms"][i])),
            kill_orb: array(&value["kill_orb"]),
            kill_threshold: value["kill_threshold"].as_i64().unwrap() as i32,
        };
        let mut notice = [0; 2];
        let mut random = Random::new(0x12345678).unwrap();
        let (applied, events) = owner
            .apply(
                HitState {
                    actors: pool.records_mut(),
                    environment: &environment,
                    clock: &clock,
                    rows: &[],
                    states: &[],
                    guard_enabled: false,
                    notice: &mut notice,
                    random: &mut random,
                },
                &context,
                &call,
            )
            .unwrap();
        assert_eq!(pool.0, expected.0, "{}", case["condition"]);
        assert_eq!(applied, case["applied"].as_i64().unwrap() != 0);
        assert_eq!(random.state(), case["seed"].as_u64().unwrap() as u32);
        let expected_events: Vec<[i32; 2]> =
            serde_json::from_value(case["events"].clone()).unwrap();
        assert_eq!(&events.events[..events.count as usize], expected_events);
        let keys = [
            call.hit.target,
            pool.0[1][call.hit.target as usize].words[240],
        ];
        for (index, kind) in [Reservation::Metal, Reservation::Credits]
            .into_iter()
            .enumerate()
        {
            let expected: Vec<i32> =
                serde_json::from_value(case["reservations"][index].clone()).unwrap();
            assert_eq!(owner.values(kind, keys[index]).unwrap(), expected);
            owner.erase(kind, keys[index]).unwrap();
            assert!(owner.values(kind, keys[index]).unwrap().is_empty());
        }
    }
    let owners: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-owner-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in owners["records"].as_array().unwrap() {
        let side = case["side"].as_u64().unwrap() as usize;
        let mask = case["mask"].as_u64().unwrap();
        let mismatch = case["mismatch"].as_u64().unwrap() as usize;
        let mut areas = Areas::new().unwrap();
        if mask & 2 != 0 {
            let mut pool = Pool::default();
            let words = &mut pool.0[side][1].words;
            words[0] = 2;
            words[3] = 10000 + if side == 1 { 250 } else { -250 };
            words[212] = 1;
            areas
                .append(&AreaEmission {
                    surge_present: 1,
                    surge: Surge {
                        side: (1 - side) as i32,
                        slot: 2,
                        frame: 14,
                        x: 10000,
                        level: 1,
                        ..Default::default()
                    },
                    ..Default::default()
                })
                .unwrap();
            areas
                .step(
                    AreaPhase::Surges,
                    pool.records_mut(),
                    &Environment::default(),
                    &AreaRules::default(),
                    &mut Random::new(0x12345678).unwrap(),
                    &mut |_, _, _| Ok(true),
                )
                .unwrap();
            assert_eq!(areas.counts().unwrap().reflections, 1);
        }
        areas
            .append(&AreaEmission {
                surge_present: i32::from(mask & 1 != 0),
                explosion_present: i32::from(mask & 4 != 0),
                surge: Surge {
                    side: (side ^ mismatch) as i32,
                    slot: 1,
                    level: 1,
                    ..Default::default()
                },
                explosion: Explosion {
                    side: side as i32,
                    slot: 1,
                    ..Default::default()
                },
            })
            .unwrap();
        let mut waves = Waves::default();
        if mask & 8 != 0 {
            waves.0.records[if mismatch != 0 { 199 } else { 0 }] = Wave {
                side: 7,
                slot: (1 + mismatch) as i32,
                state: case["wave_state"].as_i64().unwrap() as i32,
                ..Default::default()
            };
        }
        assert_eq!(
            areas
                .retirement_blocked(&waves, side as i32, 1, case["unit_route"] == 1)
                .unwrap(),
            case["blocked"] == 1
        );
    }
    // callbackのエラー/panic後に所有状態を再利用しない契約を、同じ1試験で確認する。
    for should_panic in [false, true] {
        let mut areas = Areas::new().unwrap();
        areas
            .append(&AreaEmission {
                explosion_present: 1,
                explosion: Explosion {
                    side: 0,
                    slot: 1,
                    x: 10000,
                    ..Default::default()
                },
                ..Default::default()
            })
            .unwrap();
        let mut pool = Pool::default();
        pool.0[1][1].words[0] = 2;
        pool.0[1][1].words[3] = 10000;
        let rules = AreaRules {
            explosion_frames: [1, 2, 1, 2],
            explosion_widths: [800, 500, 400],
            ..Default::default()
        };
        let mut random = Random::new(1).unwrap();
        let result = std::panic::catch_unwind(AssertUnwindSafe(|| {
            areas.step(
                AreaPhase::Explosions,
                pool.records_mut(),
                &Environment::default(),
                &rules,
                &mut random,
                &mut |_, _, _| {
                    assert!(!should_panic, "secondary callback panic");
                    Err(7)
                },
            )
        }));
        if should_panic {
            assert!(result.is_err());
        } else {
            assert_eq!(result.unwrap(), Err(7));
        }
        assert_eq!(
            areas.step(
                AreaPhase::Explosions,
                pool.records_mut(),
                &Environment::default(),
                &rules,
                &mut random,
                &mut |_, _, _| Ok(true)
            ),
            Err(1)
        );
    }
    let secondary: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-secondary-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in secondary["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["pool"]);
        let environment = Environment {
            unit_modes: [1, 0],
            ..Default::default()
        };
        let rules: AreaRules = serde_json::from_value(case["rules"].clone()).unwrap();
        let mut areas = Areas::new().unwrap();
        for value in case["initial"].as_array().unwrap() {
            areas
                .append(&AreaEmission {
                    surge_present: 1,
                    explosion_present: 1,
                    surge: serde_json::from_value(value["surge"].clone()).unwrap(),
                    explosion: serde_json::from_value(value["explosion"].clone()).unwrap(),
                })
                .unwrap();
        }
        let mut random = Random::new(0x12345678).unwrap();
        let mut checkpoints = case["checkpoints"].as_array().unwrap().iter().peekable();
        for frame in 0..case["frames"].as_u64().unwrap() {
            for (phase, action) in [
                AreaPhase::Surges,
                AreaPhase::Reflections,
                AreaPhase::Explosions,
            ]
            .into_iter()
            .enumerate()
            {
                let mut hits = Vec::new();
                areas
                    .step(
                        action,
                        pool.records_mut(),
                        &environment,
                        &rules,
                        &mut random,
                        &mut |actors, random, event| {
                            hits.push(serde_json::to_value(event).unwrap());
                            let other = 1 - event.hit.side as usize;
                            let scenario = case["scenario"].as_u64().unwrap();
                            if scenario % 2 != 0 {
                                actors[other][event.hit.target as usize].words[8] -= 1;
                                random.bounded(1)?;
                            }
                            if scenario == 2 {
                                actors[other][2].words[1] = 14;
                            }
                            Ok(case["applied"] == 1)
                        },
                    )
                    .unwrap();
                let Some(checkpoint) = checkpoints.peek() else {
                    continue;
                };
                if checkpoint["frame"] != frame || checkpoint["phase"] != phase {
                    continue;
                }
                let expected = &checkpoint["state"];
                let mut expected_pool = Pool::default();
                sparse(&mut expected_pool, &case["pool"]);
                sparse(&mut expected_pool, &expected["poolChanges"]);
                assert_eq!(pool.0, expected_pool.0);
                let counts = areas.counts().unwrap();
                let surges: Vec<Value> = (0..counts.surges)
                    .map(|i| {
                        let (record, history) = areas.surge(i).unwrap();
                        let history: Vec<_> = (0..SLOTS)
                            .filter(|j| history.present[*j] != 0)
                            .map(|j| (j, history.cycles[j]))
                            .collect();
                        serde_json::json!({"record":record, "history":history})
                    })
                    .collect();
                let reflections: Vec<_> = (0..counts.reflections)
                    .map(|i| areas.reflection(i).unwrap())
                    .collect();
                let explosions: Vec<Value> = (0..counts.explosions)
                    .map(|i| {
                        let (record, history) = areas.explosion(i).unwrap();
                        let history: Vec<_> = (0..SLOTS)
                            .filter(|j| history.hits[*j].iter().any(|v| *v != 0))
                            .map(|j| (j, history.hits[j]))
                            .collect();
                        serde_json::json!({"record":record, "history":history})
                    })
                    .collect();
                let events: Vec<_> = (0..counts.events)
                    .map(|i| areas.event(i).unwrap())
                    .collect();
                let actual = serde_json::json!({"surges":surges,"reflections":reflections,"explosions":explosions,"events":events,"seed":random.state(),"poolChanges":expected["poolChanges"]});
                assert_eq!(&actual, expected, "frame={frame}, phase={phase}");
                assert_eq!(serde_json::to_value(hits).unwrap(), checkpoint["hits"]);
                checkpoints.next();
            }
        }
        assert!(checkpoints.next().is_none());
    }
    let areas: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-area-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in areas["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["after"]);
        let environment = Environment {
            unit_modes: [1, 0],
            ..Default::default()
        };
        let selected = AttackSelection {
            side: case["side"].as_i64().unwrap() as i32,
            slot: 1,
            hit: case["hit"].as_i64().unwrap() as i32,
            targets: &[],
        };
        let emission: Emission = serde_json::from_value(case["emission"].clone()).unwrap();
        let mut random = Random::new(case["area_seed"].as_u64().unwrap() as u32).unwrap();
        let output = emit_area(
            pool.records(),
            &environment,
            selected,
            &emission,
            &mut random,
        )
        .unwrap();
        assert_eq!(serde_json::to_value(output).unwrap(), case["area"]);
        assert_eq!(u64::from(random.state()), case["seed"]);
    }
    let waves: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-wave-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in waves["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["after"]);
        let side = case["side"].as_i64().unwrap() as i32;
        let environment = Environment {
            unit_modes: [1, 0],
            ..Default::default()
        };
        let selected = AttackSelection {
            side,
            slot: 1,
            hit: case["hit"].as_i64().unwrap() as i32,
            targets: &[],
        };
        let emission: Emission = serde_json::from_value(case["output"].clone()).unwrap();
        let mut random = Random::new(case["direct_seed"].as_u64().unwrap() as u32).unwrap();
        let stale = Wave {
            side: 0,
            slot: 0x6b6b6b6b,
            state: 0,
            frame: 0x6b6b6b6b,
            x: 0x6b6b6b6b,
            level: 0x6b6b6b6b,
            hit: 0x6b6b6b6b,
            flags: [0x6b; 12],
            parameter: 0x6b6b6b6b,
            mini: 0x6b,
            reserved: [0x6b; 3],
        };
        let mut waves = Waves(Box::new(WaveState {
            records: [stale; 200],
            hits: [[0x6b; 200]; SLOTS],
        }));
        for (i, wave) in waves.0.records.iter_mut().enumerate() {
            wave.side = i32::from(i < case["occupied"].as_u64().unwrap() as usize && i % 2 == 0);
            wave.state = i32::from(i < case["occupied"].as_u64().unwrap() as usize && i % 2 == 1);
        }
        let before = waves.0.records;
        let slot = waves
            .emit(
                pool.records(),
                &environment,
                selected,
                &emission,
                &mut random,
            )
            .unwrap();
        assert_eq!(slot, case["spawned"]);
        for (i, (actual, previous)) in waves.0.records.iter().zip(before.iter()).enumerate() {
            if i as i32 != slot {
                assert_eq!(actual, previous);
                continue;
            }
            let mut bytes: Vec<u8> = [
                actual.side,
                actual.slot,
                actual.state,
                actual.frame,
                actual.x,
                actual.level,
                actual.hit,
            ]
            .into_iter()
            .flat_map(i32::to_le_bytes)
            .collect();
            bytes.extend(actual.flags);
            bytes.extend(actual.parameter.to_le_bytes());
            bytes.push(actual.mini);
            bytes.extend(actual.reserved);
            assert_eq!(serde_json::to_value(bytes).unwrap(), case["wave"]);
        }
        for row in &waves.0.hits {
            for (i, value) in row.iter().enumerate() {
                assert_eq!(*value, if i as i32 == slot { 0 } else { 0x6b });
            }
        }
        assert_eq!(u64::from(random.state()), case["seed"]);
    }
    let direct: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-direct-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in direct["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let side = case["side"].as_i64().unwrap() as usize;
        let environment = Environment {
            unit_modes: [1, 0],
            ..Default::default()
        };
        let targets: Vec<i32> = serde_json::from_value(case["targets"].clone()).unwrap();
        let selected = AttackSelection {
            side: side as i32,
            slot: 1,
            hit: case["hit"].as_i64().unwrap() as i32,
            targets: &targets,
        };
        let mut random = Random::new(0x12345678).unwrap();
        let mut events = Vec::new();
        let result = emit_direct(
            pool.records_mut(),
            &environment,
            selected,
            &mut random,
            &mut |actors, random, hit| {
                let mut event = serde_json::to_value(hit).unwrap();
                event["seed"] = random.state().into();
                events.push(event);
                match case["mutation"].as_u64().unwrap() {
                    1 => actors[1 - side][hit.target as usize].words[1] = 14,
                    2 => {
                        let words = &mut actors[side][1].words;
                        words[218] += 1;
                        words[84] = if words[84] != 0 { 0 } else { 10 };
                        random.bounded(1)?;
                    }
                    _ => (),
                }
                Ok(case["applied"] == 1)
            },
        )
        .unwrap();
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
        assert_eq!(serde_json::to_value(events).unwrap(), case["events"]);
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
        assert_eq!(u64::from(random.state()), case["seed"]);
    }
    let attacks: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-attack-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in attacks["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let side = case["side"].as_i64().unwrap() as usize;
        let environment = Environment {
            unit_modes: [1, 0],
            castle_slot: case["castle_slot"].as_i64().unwrap() as i32,
            special_castle: case["special_castle"].as_i64().unwrap() as i32,
            ..Default::default()
        };
        let motion = Motion {
            encoded: [case["length"].as_i64().unwrap() as i32; 8],
            plain: [8; 8],
            soul_frames: 0,
        };
        let mut random = Random::new(0x12345678).unwrap();
        let mut events = Vec::new();
        let result = pool
            .attack(
                &environment,
                side as i32,
                1,
                &motion,
                &mut random,
                &mut |actors, random, selected| {
                    let current = &mut actors[side][1].words;
                    events.push(serde_json::json!({
                        "side": selected.side, "slot": selected.slot, "hit": selected.hit,
                        "targets": selected.targets, "frame": current[2], "wait": current[18],
                        "attacks": current[115], "seed": random.state(),
                    }));
                    match case["callback"].as_u64().unwrap() {
                        1 => current[2] = 0,
                        2 => {
                            current[121] = 0;
                            current[122] = 0;
                        }
                        3 => {
                            random.bounded(1)?;
                        }
                        _ => (),
                    }
                    Ok(())
                },
            )
            .unwrap();
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
        assert_eq!(serde_json::to_value(events).unwrap(), case["events"]);
        assert_eq!(u64::from(random.state()), case["seed"]);
        assert_eq!(result.handled, case["handled"]);
        assert_eq!(result.emitted, case["emitted"]);
    }
    // FFI内の失敗・panicで後続段を動かさず、C ABIを抜けてからpanicを戻す。
    let callback_case = attacks["records"]
        .as_array()
        .unwrap()
        .iter()
        .find(|case| case["emitted"].as_i64().unwrap() > 0)
        .unwrap();
    for panic in [false, true] {
        let mut pool = Pool::default();
        sparse(&mut pool, &callback_case["before"]);
        let mut random = Random::new(0x12345678).unwrap();
        let environment = Environment {
            unit_modes: [1, 0],
            castle_slot: callback_case["castle_slot"].as_i64().unwrap() as i32,
            special_castle: callback_case["special_castle"].as_i64().unwrap() as i32,
            ..Default::default()
        };
        let motion = Motion {
            encoded: [callback_case["length"].as_i64().unwrap() as i32; 8],
            plain: [8; 8],
            soul_frames: 0,
        };
        let mut calls = 0;
        let result = std::panic::catch_unwind(AssertUnwindSafe(|| {
            pool.attack(
                &environment,
                callback_case["side"].as_i64().unwrap() as i32,
                1,
                &motion,
                &mut random,
                &mut |_, _, _| {
                    calls += 1;
                    if panic {
                        panic!("attack callback witness");
                    }
                    Err(77)
                },
            )
        }));
        assert_eq!(calls, 1);
        if panic {
            assert!(result.is_err());
        } else {
            assert!(matches!(result, Ok(Err(77))));
        }
    }
    let waits: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-wait-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in waits["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let environment = Environment {
            unit_modes: [1, 0],
            castle_slot: -1,
            ..Default::default()
        };
        let motion = Motion {
            encoded: [6; 8],
            plain: array(&case["plain"]),
            soul_frames: 0,
        };
        assert_eq!(
            pool.attack_wait(
                &environment,
                case["side"].as_i64().unwrap() as i32,
                1,
                &motion,
                case["blocked"] == 1
            )
            .unwrap(),
            case["handled"] == 1,
        );
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
    }
    let intents: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-intent-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in intents["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let environment = Environment {
            unit_modes: array(&case["unit_modes"]),
            castle_slot: -1,
            ..Default::default()
        };
        assert_eq!(pool.intent(&environment).unwrap(), case["blocked"] == 1);
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
    }
    let retirements: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-retirement-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in retirements["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let side = case["side"].as_i64().unwrap() as usize;
        let mut environment = Environment::default();
        environment.unit_modes[side] = case["mode"].as_i64().unwrap() as i32;
        let input: Retirement = serde_json::from_value(case["input"].clone()).unwrap();
        let result = pool.retire(&environment, side as i32, 1, &input).unwrap();
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
    }
    let deaths: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-enemy-death-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in deaths["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        let input: EnemyDeath = serde_json::from_value(case["input"].clone()).unwrap();
        let cohort: Vec<i32> = serde_json::from_value(case["cohort"].clone()).unwrap();
        let environment = Environment {
            treasures: array(&case["treasures"]),
            combos: array(&case["combos"]),
            ..Default::default()
        };
        let result = pool
            .enemy_knockback(
                &environment,
                case["side"].as_i64().unwrap() as i32,
                1,
                &input,
                &cohort,
            )
            .unwrap();
        let mut expected = Pool::default();
        sparse(&mut expected, &case["after"]);
        assert_eq!(pool.0, expected.0);
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
    }
    let displacements: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-displacement-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in displacements["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        let environment = Environment {
            treasures: array(&case["treasures"]),
            combos: array(&case["combos"]),
            ..Environment::default()
        };
        assert!(
            pool.enemy_displacement(&environment, side as i32, 1, 200)
                .unwrap()
        );
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
    }
    let knockbacks: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-knockback-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in knockbacks["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        let environment = Environment {
            unit_modes: [1, 1],
            ..Environment::default()
        };
        let input: Knockback = serde_json::from_value(case["input"].clone()).unwrap();
        let result = pool
            .unit_knockback(&environment, side as i32, 1, &input)
            .unwrap();
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
    }
    let walks: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-walk-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in walks["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        if let Some(distance) = case["distance"].as_i64() {
            let target = &mut pool.0[1 - side][1].words;
            target[0] = 2;
            target[8] = 100;
            target[3] = 10000
                + if side == 0 {
                    -(distance as i32)
                } else {
                    distance as i32
                };
        }
        let mut environment = Environment::default();
        environment.unit_modes[side] = case["mode"].as_i64().unwrap() as i32;
        assert!(pool.walk(&environment, side as i32, 1).unwrap());
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
    }
    let health: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-health-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in health["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        let slot = case["slot"].as_i64().unwrap() as usize;
        pool.0[side][slot].words = array(&case["before"]);
        let input: Health = serde_json::from_value(case["input"].clone()).unwrap();
        let mut random = Random::new(0x12345678).unwrap();
        let result = pool
            .health(side as i32, slot as i32, &input, &mut random)
            .unwrap();
        assert_eq!(pool.0[side][slot].words, array(&case["after"]));
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
        assert_eq!(u64::from(random.state()), case["seed"]);
    }
    let reactions: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-reaction-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in reactions["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        let environment = Environment {
            unit_modes: array(&case["modes"]),
            castle_slot: 1,
            special_castle: case["special_castle"].as_i64().unwrap() as i32,
            ..Environment::default()
        };
        let input: Reaction = serde_json::from_value(case["input"].clone()).unwrap();
        let mut random = Random::new(0x12345678).unwrap();
        let result = pool
            .react(&environment, side as i32, 1, &input, &mut random)
            .unwrap();
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
        assert_eq!(serde_json::to_value(result).unwrap(), case["output"]);
        assert_eq!(u64::from(random.state()), case["seed"]);
    }
    let loaders: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-loader-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in loaders["records"].as_array().unwrap() {
        let raw: Vec<i32> = case["raw"]
            .as_array()
            .unwrap()
            .iter()
            .map(|v| v.as_i64().unwrap() as i32)
            .collect();
        assert_eq!(
            Definition::from_raw(&raw, case["unit"] == 1).unwrap().cells,
            array(&case["loaded"])
        );
    }
    let protections: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-protection-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in protections["records"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        let result = pool.protect(side as i32, 1).unwrap();
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
        assert_eq!(result.shield_hit, case["shield_hit"]);
        assert_eq!(
            serde_json::to_value(&result.sounds[..result.sound_count as usize]).unwrap(),
            case["sounds"]
        );
        assert_eq!(
            serde_json::to_value(&result.visuals[..result.visual_count as usize]).unwrap(),
            case["visuals"]
        );
    }

    let fixture: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in fixture["begins"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        let slot = case["slot"].as_i64().unwrap() as usize;
        pool.0[side][slot].words = array(&case["before"]);
        let mut environment = Environment::default();
        environment.unit_modes[side] = case["mode"].as_i64().unwrap() as i32;
        pool.begin(&environment, side as i32, slot as i32).unwrap();
        assert_eq!(pool.0[side][slot].words, array(&case["after"]));
    }
    for case in fixture["transitions"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_i64().unwrap() as usize;
        pool.0[side][1].words = array(&case["before"]);
        let mut environment = Environment {
            unit_modes: [1, 0],
            ..Environment::default()
        };
        environment.unit_modes[side] = case["mode"].as_i64().unwrap() as i32;
        let motion = Motion {
            encoded: [5; 8],
            plain: [8; 8],
            soul_frames: 9,
        };
        assert_eq!(
            pool.transition(&environment, side as i32, 1, &motion, 200)
                .unwrap(),
            case["sound"]
        );
        assert_eq!(pool.0[side][1].words, array(&case["after"]));
    }
    for case in fixture["cases"].as_array().unwrap() {
        let source = &case["definition"];
        let mut definition = Definition::from_raw(&[], true).unwrap();
        definition.cells = array(&source["cells"]);
        definition.count = source["count"].as_i64().unwrap() as i32;
        definition.growth = array(&source["growth"]);
        definition.talent_active = array(&source["talent_active"]);
        definition.talent_min_level = array(&source["talent_min_level"]);
        definition.added_targets = source["added_targets"].as_i64().unwrap() as i32;
        definition.orb_enabled = source["orb_enabled"].as_i64().unwrap() as i32;
        definition.orb_present = array(&source["orb_present"]);
        for i in 0..SKILLS {
            definition.talents[i] = array(&source["talents"][i]);
        }
        for i in 0..ORBS {
            definition.orbs[i] = array(&source["orbs"][i]);
        }
        definition.speed_rule = source["speed_rule"].as_i64().unwrap() as i32;
        definition.speed_value = source["speed_value"].as_i64().unwrap() as i32;
        let mut environment: Environment =
            serde_json::from_value(case["environment"].clone()).unwrap();
        let request: SpawnRequest = serde_json::from_value(case["request"].clone()).unwrap();
        let mut pool = Pool::default();
        for (index, source) in case["pool"].as_array().unwrap().iter().enumerate() {
            for entry in source.as_array().unwrap() {
                pool.0[index / SLOTS][index % SLOTS].words[entry[0].as_u64().unwrap() as usize] =
                    entry[1].as_i64().unwrap() as i32;
            }
        }
        let before = pool.0.clone();
        let mut random = Random::new(0x12345678).unwrap();
        let slot = pool
            .initialize(&definition, &mut environment, &request, &mut random)
            .unwrap();
        assert_eq!(i64::from(slot), case["output"]["slot"], "{}", case["name"]);
        assert_eq!(u64::from(random.state()), case["output"]["seed"]);
        assert_eq!(environment.spawned, array(&case["spawned"]));
        if slot > 0 {
            assert_eq!(
                pool.0[request.side as usize][slot as usize].words,
                array(&case["output"]["words"]),
                "{}",
                case["name"]
            );
            pool.0[request.side as usize][slot as usize] =
                before[request.side as usize][slot as usize].clone();
        }
        assert_eq!(pool.0, before);
    }
    for case in fixture["actions"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_u64().unwrap_or(0) as usize;
        if case["kind"] == "roll" {
            let record = &mut pool.0[side][1].words;
            for word in [56, 49, 50, 52, 68, 163, 135, 132, 147, 171, 183, 246] {
                record[word] = case["probability"].as_i64().unwrap() as i32;
            }
            for word in [123, 124, 125] {
                record[word] = case["enabled"].as_i64().unwrap() as i32;
            }
            let mut random = Random::new(0x12345678).unwrap();
            let result = pool
                .roll(
                    side as i32,
                    1,
                    case["hit"].as_i64().unwrap() as i32,
                    &mut random,
                )
                .unwrap();
            assert_eq!(result.0, array(&case["flags"]));
            assert_eq!(u64::from(random.state()), case["seed"]);
        } else if case["kind"] == "contact" {
            let a = &mut pool.0[side][1].words;
            a[0] = 2;
            a[1] = 2;
            a[3] = 10000;
            a[13] = 500;
            let b = &mut pool.0[1 - side][1].words;
            b[0] = 2;
            b[1] = case["action"].as_i64().unwrap() as i32;
            b[3] = 10000 + case["distance"].as_i64().unwrap() as i32;
            b[14] = 200;
            b[15] = -100;
            let result = pool.contact(side as i32, 1, 1, 0, -1, false).unwrap();
            assert_eq!(i32::from(result), case["output"]);
        } else if case["kind"] == "far" {
            let target = case["target"].as_u64().unwrap() as usize;
            let a = &mut pool.0[0][1].words;
            a[0] = 2;
            a[1] = 2;
            a[3] = 10000;
            a[13] = 500;
            for (word, value) in [
                (84, 200),
                (85, 400),
                (199, -200),
                (200, 200),
                (201, 600),
                (202, -600),
                (203, 20),
                (204, 30),
            ] {
                a[word] = value;
            }
            let b = &mut pool.0[1][target].words;
            b[0] = 2;
            b[1] = 2;
            b[3] = 10000 + case["distance"].as_i64().unwrap() as i32;
            let result = pool
                .contact(
                    0,
                    1,
                    target as i32,
                    case["hit"].as_i64().unwrap() as i32,
                    -1,
                    false,
                )
                .unwrap();
            assert_eq!(i32::from(result), case["output"]);
        } else if case["kind"] == "matches" {
            let a = &mut pool.0[side][1].words;
            a[case["field"].as_u64().unwrap() as usize] = 1;
            let cursed = case["cursed"].as_i64().unwrap() as i32;
            a[150] = cursed & 1;
            a[151] = i32::from(cursed & 2 != 0);
            for word in [17, 41, 42, 43, 44, 45, 46, 47, 109, 144, 146, 194] {
                pool.0[1 - side][1].words[word] = case["target_traits"].as_i64().unwrap() as i32;
            }
            let environment = Environment {
                unit_modes: [1, 0],
                ..Default::default()
            };
            assert_eq!(
                i32::from(pool.matches(&environment, side as i32, 1, 1).unwrap()),
                case["output"]
            );
        } else {
            sparse(&mut pool, &case["before"]);
            let environment: Environment =
                serde_json::from_value(case["environment"].clone()).unwrap();
            let context: EffectContext = serde_json::from_value(case["context"].clone()).unwrap();
            let mut random = Random::new(0x12345678).unwrap();
            let result = pool
                .apply_effects(
                    &environment,
                    &context,
                    [side as i32, 1, 1],
                    &array(&case["flags"]),
                    &mut random,
                )
                .unwrap();
            assert_eq!(u64::from(random.state()), case["seed"]);
            let mut expected = Pool::default();
            sparse(&mut expected, &case["after"]);
            assert_eq!(pool.0, expected.0);
            let events: Vec<[i32; 2]> = case["events"]
                .as_array()
                .unwrap()
                .iter()
                .map(array)
                .collect();
            assert_eq!(&result.events[..result.count as usize], events);
        }
    }
    for case in fixture["clocks"].as_array().unwrap() {
        let source = &case["clock"];
        let clock = Clock {
            encoded: array(&source["encoded"]),
            plain: array(&source["plain"]),
            forms: std::array::from_fn(|i| array(&source["forms"][i])),
            kill_orb: array(&source["kill_orb"]),
            kill_threshold: source["kill_threshold"].as_i64().unwrap() as i32,
        };
        let mut pool = Pool::default();
        sparse(&mut pool, &case["before"]);
        for step in case["steps"].as_array().unwrap() {
            pool.clock(&clock).unwrap();
            let mut expected = Pool::default();
            sparse(&mut expected, step);
            assert_eq!(pool.0, expected.0);
        }
    }
    for case in fixture["motions"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_u64().unwrap() as usize;
        let record = &mut pool.0[side][1].words;
        record[0] = 2;
        record[1] = case["action"].as_i64().unwrap() as i32;
        record[2] = case["frame"].as_i64().unwrap() as i32;
        record[128] = case["special"].as_i64().unwrap() as i32;
        record[126] = if record[128] != 0 { 3 } else { -1 };
        let mut expected = pool.0.clone();
        expected[side][1].words[2] = case["output"].as_i64().unwrap() as i32;
        let motion = Motion {
            encoded: [case["length"].as_i64().unwrap() as i32; 8],
            plain: [8; 8],
            soul_frames: 9,
        };
        pool.motion(side as i32, 1, &motion).unwrap();
        assert_eq!(pool.0, expected);
    }
    for case in fixture["resumes"].as_array().unwrap() {
        let mut pool = Pool::default();
        let side = case["side"].as_u64().unwrap() as usize;
        let record = &mut pool.0[side][1].words;
        record[0] = 2;
        record[1] = case["action"].as_i64().unwrap() as i32;
        record[2] = 17;
        record[10] = case["speed"].as_i64().unwrap() as i32;
        record[118] = case["mode"].as_i64().unwrap() as i32;
        let mut expected = pool.0.clone();
        for (index, word) in [1, 2, 10].into_iter().enumerate() {
            expected[side][1].words[word] = case["output"][index].as_i64().unwrap() as i32;
        }
        pool.resume(side as i32, 1).unwrap();
        assert_eq!(pool.0, expected);
    }
    for case in fixture["damages"].as_array().unwrap() {
        let mut pool = Pool::default();
        if case["kind"] == "barrier" {
            let side = case["side"].as_u64().unwrap() as usize;
            pool.0[side][1].words[0] = 2;
            pool.0[side][1].words[130] = 100;
            pool.0[side][1].words[131] = case["barrier_flag"].as_i64().unwrap() as i32;
            let environment = Environment {
                unit_modes: [1, 0],
                castle_slot: -1,
                ..Default::default()
            };
            for (index, amount) in case["amounts"].as_array().unwrap().iter().enumerate() {
                let mut input = Damage {
                    side: side as i32,
                    slot: 1,
                    amount: amount.as_i64().unwrap() as i32,
                    guard_enabled: false,
                    notice: [0; 2],
                };
                pool.damage(&environment, &[], &[], &mut input).unwrap();
                let values: [i32; 5] = array(&case["output"][index]);
                assert_eq!(
                    [19, 112, 130, 131, 162].map(|word| pool.0[side][1].words[word]),
                    values
                );
            }
        } else {
            sparse(&mut pool, &case["before"]);
            let special = case["special"].as_i64().unwrap() as i32;
            let environment = Environment {
                unit_modes: [1, 0],
                castle_slot: 2,
                special_castle: special,
                ..Default::default()
            };
            let rows: Vec<_> = case["rows"]
                .as_array()
                .unwrap()
                .iter()
                .map(|v| stage::Row(array(v)))
                .collect();
            let states: Vec<_> = case["states"]
                .as_array()
                .unwrap()
                .iter()
                .map(|v| stage::State {
                    wait: v["wait"].as_i64().unwrap() as i32,
                    spawned: v["spawned"].as_i64().unwrap() as i32,
                    kills: v["kills"].as_i64().unwrap() as i32,
                })
                .collect();
            let slot = if special != 0 { 2 } else { 0 };
            let mut input = Damage {
                side: 1,
                slot,
                amount: 101,
                guard_enabled: case["guard"].as_i64().unwrap() != 0,
                notice: array(&case["initial_notice"]),
            };
            pool.damage(&environment, &rows, &states, &mut input)
                .unwrap();
            assert_eq!(input.notice, array(&case["notice"]));
            assert_eq!(
                [19, 112, 131, 162].map(|word| pool.0[1][slot as usize].words[word]),
                array(&case["output"])
            );
        }
    }
    let mut raw = [0; 119];
    raw[0] = i32::MAX;
    let mut definition = Definition::from_raw(&raw, true).unwrap();
    definition.growth = [20; 20];
    let mut environment = Environment {
        unit_modes: [1, 0],
        stage_width: 24000,
        ..Default::default()
    };
    let mut random = Random::new(0x12345678).unwrap();
    let mut pool = Pool::default();
    pool.0[0][1].words[20] = 17;
    let before = pool.0.clone();
    assert_eq!(
        pool.initialize(
            &definition,
            &mut environment,
            &SpawnRequest {
                raw: 2,
                level_index: 29,
                ..Default::default()
            },
            &mut random
        ),
        Err(2)
    );
    assert_eq!(pool.0, before);
    assert_eq!(random.state(), 0x12345678);
    assert_eq!(environment.spawned, [0, 0]);
}
