use super::*;
use serde_json::Value;

fn fixture() -> Value {
    serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/battle-traits-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap()
}

#[test]
fn equipment_matches_arm64_grade_and_sum_witnesses() {
    let fixture: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/equipment-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    let items = fixture["list"]["ID"].as_array().unwrap();
    for case in fixture["cases"].as_array().unwrap() {
        let (orbs, grades): (Vec<_>, Vec<_>) = case["ids"]
            .as_array()
            .unwrap()
            .iter()
            .map(|id| {
                let item = &items[id.as_u64().unwrap() as usize - 30000];
                let mut values = [0; 4];
                for (out, value) in values.iter_mut().zip(item["value"].as_array().unwrap()) {
                    *out = value.as_i64().unwrap() as i32;
                }
                (
                    Orb {
                        effect: item["content"].as_i64().unwrap() as i32,
                        mask: item["attribute"].as_u64().map_or(0, |bit| 1 << bit),
                        values,
                    },
                    item["gradeID"].as_i64().unwrap() as i32,
                )
            })
            .unzip();
        let mut definition = actor::Definition::from_raw(&[0; 119], true).unwrap();
        equipment(&orbs, &grades, &mut definition).unwrap();
        for result in case["results"].as_array().unwrap() {
            let effect = result[0].as_u64().unwrap() as usize;
            assert_eq!(
                definition.orb_present[effect],
                result[2].as_i64().unwrap() as i32
            );
            if effect >= 5 {
                let values: Vec<i32> = serde_json::from_value(result[1].clone()).unwrap();
                assert_eq!(definition.orbs[effect][..values.len()], values);
            }
        }
    }
}
fn config() -> Config {
    // 全フィールドが整数/浮動小数点のC POD。必須の状態だけ明示する。
    let mut c: Config = unsafe { std::mem::zeroed() };
    c.seed = 1572;
    c.environment.unit_modes = [1, 0];
    c.environment.stage_width = 20000;
    c.environment.castle_slot = -1;
    c.environment.castle_x = 3200;
    c.environment.castle_scale = 100;
    c.environment.stage_kind = 3;
    c.environment.crown = 100;
    c.environment.hp_percent = 100;
    c.environment.attack_percent = 100;
    c.screen.speed = 2;
    c.screen.fixed_money = 0;
    c.screen.viewport_width = 960;
    c.state.rows = 2;
    c.state.intro = 24;
    c.state.holding = -1;
    c.state.pending_control = -1;
    c.state.description_item = -1;
    c.castle_hp = [1000000; 2];
    c.enemy_max = 50;
    c.unit_max = 50;
    c.rules.total_limit = -1;
    c.red_gauge_frames = 15;
    c.waves.motion_frames = [13; 2];
    c.cannon.encoded = [-1; 4];
    c
}
fn profile(raw: &[i32], side: i32, id: i32) -> Profile {
    let mut p: Profile = unsafe { std::mem::zeroed() };
    p.definition = actor::Definition::from_raw(raw, side == 0).unwrap();
    p.definition.growth = [100; 20];
    p.spawn = production::SpawnRequest {
        side,
        raw: id,
        ..Default::default()
    };
    p.deployment_slot = if side == 0 { 0 } else { -1 };
    p.motion.encoded = [30; 8];
    p.motion.plain = [30; 8];
    p.motion.soul_frames = 30;
    p.death_soul_frames = 30;
    p.recharge = 600;
    p.recharge_plain = 600;
    p
}
// C++所有個体へテスト時だけ入力を注入する。Rustの借用参照とは同時に保持しない。
fn edit(battle: &mut Battle, side: usize, slot: usize, f: impl FnOnce(&mut [i32; 251])) {
    let mut actors = std::ptr::null();
    let mut profiles = std::ptr::null();
    assert_eq!(
        unsafe { kbcs_core_battle_actors(battle.0.as_ptr(), &mut actors, &mut profiles) },
        0
    );
    unsafe { f(&mut (*actors.cast_mut().add(side * 51 + slot)).words) };
}
fn tick(battle: &mut Battle, ticks: i32) {
    battle
        .advance(&battle_screen::Input {
            ticks,
            ..Default::default()
        })
        .unwrap();
}

#[test]
fn native_frame_marks_and_enemy_castle_are_connected() {
    let mut battle = Battle::new(&config(), &[], &[]).unwrap();
    for side in 0..2 {
        for slot in 0..51 {
            edit(&mut battle, side, slot, |w| {
                w[107] = 1;
                w[131] = 2;
                w[191] = 2;
                w[114] = 7;
            });
        }
    }
    for _ in 0..2 {
        tick(&mut battle, 1);
        let (actors, _) = battle.actors().unwrap();
        for (side, army) in actors.iter().enumerate() {
            for actor in army {
                assert_eq!(
                    (
                        actor.words[107],
                        actor.words[131],
                        actor.words[191],
                        actor.words[114]
                    ),
                    (i32::from(side == 0), 0, 0, 7)
                );
            }
        }
    }
    let data = fixture();
    let raw: Vec<i32> = serde_json::from_value(data["castleEnemy"].clone()).unwrap();
    let row: [i32; 14] = serde_json::from_value(data["castleRow"].clone()).unwrap();
    let mut c = config();
    c.environment.special_castle = 787;
    c.environment.castle_slot = 1;
    let mut battle = Battle::new(&c, &[profile(&raw, 1, 787)], &[stage::Row(row)]).unwrap();
    for _ in 0..60 {
        tick(&mut battle, 10);
    }
    assert_eq!(
        battle
            .active_actors()
            .unwrap()
            .iter()
            .filter(|a| a.side == 1 && a.slot > 0)
            .count(),
        1
    );
}

#[test]
fn enemy_castle_breaker_flows_from_raw_to_owned_hp() {
    let data = fixture();
    let mut raw: Vec<i32> = serde_json::from_value(data["breakerEnemy"].clone()).unwrap();
    let mut damages = Vec::new();
    for enabled in [0, 1] {
        raw[26] = enabled;
        let mut battle = Battle::new(
            &config(),
            &[profile(&raw, 1, 37)],
            &[stage::Row([
                37, 1, 0, 1000, 1000, 100, 0, 0, 0, 100, 0, 100, 0, 0,
            ])],
        )
        .unwrap();
        tick(&mut battle, 1);
        assert_eq!(battle.actors().unwrap().0[1][1].words[59], enabled);
        edit(&mut battle, 1, 1, |w| w[3] = 16800);
        for _ in 0..120 {
            tick(&mut battle, 1);
            let hp = battle.actors().unwrap().0[0][0].words[8];
            if hp < 1000000 {
                damages.push(1000000 - hp);
                break;
            }
        }
    }
    assert_eq!(damages, [2637, 10548]);
}

#[test]
fn native_production_delay_vectors() {
    unsafe extern "C" {
        fn kbcs_core_production_delay(
            recharge: i32,
            rate: i32,
            frames: i32,
            wait: *mut i32,
            maximum: *mut i32,
            red: *mut i32,
        ) -> u32;
    }
    for case in fixture()["delays"].as_array().unwrap() {
        let v: Vec<i32> = serde_json::from_value(case["input"].clone()).unwrap();
        let (mut wait, mut maximum, mut red) = (v[2], v[3], v[4]);
        assert_eq!(
            unsafe {
                kbcs_core_production_delay(v[0], v[1], 15, &mut wait, &mut maximum, &mut red)
            },
            0
        );
        let expected: Vec<i32> = serde_json::from_value(case["output"].clone()).unwrap();
        assert_eq!([wait, maximum, red].as_slice(), expected);
    }
}

#[test]
fn production_delay_reaches_owned_wait_and_red_hud() {
    // 高HP・攻撃0の制御対象へ、実敵プロフィールの遅延確率/率だけを注入する。
    let mut raw = vec![0; 119];
    for (column, value) in [
        (0, 1000000),
        (1, 1),
        (4, 1),
        (5, 100),
        (7, 300),
        (13, 1),
        (63, 1),
        (110, -1),
    ] {
        raw[column] = value;
    }
    let enemy: Vec<i32> = serde_json::from_value(fixture()["breakerEnemy"].clone()).unwrap();
    let mut c = config();
    c.screen.present[0] = 1;
    c.unit_max = 1;
    c.hit.effects.target_count = 1;
    c.hit.effects.scenario_level = 1;
    c.effect_clocks[0] = [0x16560, 30, 30];
    let mut battle = Battle::new(
        &c,
        &[profile(&raw, 0, 2), profile(&enemy, 1, 37)],
        &[stage::Row([
            37, 1, 0, 1000, 1000, 100, 0, 0, 0, 100, 0, 100, 0, 0,
        ])],
    )
    .unwrap();
    battle
        .advance(&battle_screen::Input {
            control: 1000,
            ticks: 6,
            ..Default::default()
        })
        .unwrap();
    assert!(battle.actors().unwrap().0[0][1].words[0] >= 2);
    for _ in 0..10 {
        tick(&mut battle, 10);
    }
    assert_eq!(
        battle.warning().unwrap(),
        [
            1,
            if c.screen.viewport_width > 0 {
                c.screen.viewport_width / 2
            } else {
                480
            },
            220
        ]
    );
    let x = battle.actors().unwrap().0[0][1].words[3];
    edit(&mut battle, 1, 1, |w| {
        w[1] = 0;
        w[2] = 0;
        w[3] = x - 100;
        w[11] = 1;
        w[246] = 100;
        w[247] = 50;
    });
    for _ in 0..120 {
        let before = battle.production().unwrap().0.wait[0];
        tick(&mut battle, 1);
        let production = battle.production().unwrap().0;
        if production.wait[0] > before {
            assert_eq!(production.maximum[0], before);
            let hud = battle
                .hud(
                    &render::Layout {
                        zoom: 1.,
                        ..Default::default()
                    },
                    [0, 0],
                )
                .unwrap();
            assert!(
                hud.gauges[0][4] > hud.gauges[0][3],
                "red must cover delayed progress"
            );
            return;
        }
    }
    panic!("production delay did not reach the owned runtime");
}

#[test]
fn cannon_cheat_recharges_without_interrupting_the_shot() {
    let mut c = config();
    c.state.cannon = 500;
    c.cannon.encoded = [30; 4];
    c.castle.words[6] = 12;
    c.castle.words[29] = 1;
    let mut battle = Battle::new(&c, &[], &[]).unwrap();
    battle.cheats(16).unwrap();
    assert_eq!(
        battle
            .advance(&battle_screen::Input::default())
            .unwrap()
            .state
            .cannon,
        0
    );
    battle
        .advance(&battle_screen::Input {
            control: 1101,
            ticks: 6,
            ..Default::default()
        })
        .unwrap();
    let (actors, _) = battle.actors().unwrap();
    assert_ne!(actors[0][0].words[9], 0);
    assert_eq!(actors[0][0].words[12], 0);
    let shots = actors[0][0].words[13];
    battle
        .advance(&battle_screen::Input {
            control: 1101,
            ticks: 6,
            ..Default::default()
        })
        .unwrap();
    assert_eq!(battle.actors().unwrap().0[0][0].words[13], shots);
    assert!(battle.cheats(32).is_err());
    battle
        .advance(&battle_screen::Input {
            ticks: 12,
            ..Default::default()
        })
        .unwrap();
    let sounds: Vec<_> = battle.sounds().unwrap().iter().map(|v| v.id).collect();
    let stop = sounds.iter().position(|&id| id == !25).unwrap();
    let wave = sounds.iter().position(|&id| id == 26).unwrap();
    assert!(stop < wave);
}

#[test]
fn defeat_title_finishes_moving_before_the_hint_opens() {
    let mut battle = Battle::new(&config(), &[], &[]).unwrap();
    battle.hints(&[7], &[3], 3).unwrap();
    edit(&mut battle, 0, 0, |w| w[8] = 0);
    for _ in 0..300 {
        tick(&mut battle, 1);
        let e = battle.ending().unwrap();
        if e.phase == 2 && e.frame == 80 {
            break;
        }
    }
    let e = battle.ending().unwrap();
    assert_eq!((e.phase, e.frame, e.title[1]), (2, 80, 242));
    for step in 1..=10 {
        tick(&mut battle, 1);
        let e = battle.ending().unwrap();
        assert_eq!(e.title[1], 242 - step * 10);
        assert_eq!(battle.hint().unwrap().id, if step == 10 { 7 } else { -1 });
    }
    assert_eq!(battle.hint().unwrap().panel[2], 0);
    tick(&mut battle, 1);
    assert!(battle.sounds().unwrap().iter().any(|v| v.id == 42));
    tick(&mut battle, 3);
    assert_eq!(battle.ending().unwrap().title[1], 142);
    assert_eq!(battle.hint().unwrap().panel[2], 690);
    assert_eq!(battle.hint().unwrap().ready, 1);
}

#[test]
fn warp_visuals_follow_actor_phase_and_layer() {
    let mut battle = Battle::new(&config(), &[], &[]).unwrap();
    for side in 0..2 {
        for (action, phase) in [
            (18, Some(0x2b98)),
            (19, None),
            (20, Some(0x2bd0)),
            (4, None),
        ] {
            edit(&mut battle, side, 1, |w| {
                w[0] = 2;
                w[1] = action;
                w[2] = 7;
                w[3] = 8000;
                w[4] = 4400;
                w[5] = 3;
            });
            let rows: Vec<_> = battle
                .visuals()
                .unwrap()
                .iter()
                .filter(|v| v.kind == 11 && v.side == side as i32)
                .collect();
            assert_eq!(rows.len(), usize::from(phase.is_some()));
            if let Some(phase) = phase {
                assert_eq!(
                    (rows[0].phase, rows[0].frame, rows[0].x, rows[0].y),
                    (phase, 7, 800, 102)
                );
            }
        }
        edit(&mut battle, side, 1, |w| w[0] = 0);
        assert!(
            !battle
                .visuals()
                .unwrap()
                .iter()
                .any(|v| v.kind == 11 && v.side == side as i32)
        );
    }
}

#[test]
fn inspector_tracks_revival_retirement_and_reused_slots_without_rng() {
    let raw: Vec<i32> = serde_json::from_value(fixture()["breakerEnemy"].clone()).unwrap();
    let mut c = config();
    c.enemy_max = 1;
    let mut battle = Battle::new(
        &c,
        &[profile(&raw, 1, 37)],
        &[stage::Row([
            37, 0, 0, 1, 1, 100, 0, 0, 0, 100, 0, 100, 0, 0,
        ])],
    )
    .unwrap();
    tick(&mut battle, 1);
    let first = battle.inspection().unwrap()[0];
    assert_eq!(
        (first.id, first.side, first.slot, first.retired_frame),
        (1, 1, 1, -1)
    );
    let seed = battle.production().unwrap().1;
    for _ in 0..3 {
        assert_eq!(battle.inspection().unwrap()[0].serial, first.serial);
    }
    assert_eq!(battle.production().unwrap().1, seed);
    edit(&mut battle, 1, 1, |w| {
        w[1] = 14;
        w[2] = 0;
        w[205] = 1;
    });
    tick(&mut battle, 1);
    assert_eq!(
        (
            battle.inspection().unwrap()[0].action,
            battle.inspection().unwrap()[0].revivals
        ),
        (15, 1)
    );
    edit(&mut battle, 1, 1, |w| {
        w[1] = 4;
        w[2] = 1000;
        w[205] = 0;
    });
    tick(&mut battle, 1);
    assert!(battle.inspection().unwrap()[0].retired_frame >= 0);
    assert_eq!(
        battle.inspection().unwrap()[0].last_frame,
        battle.inspection().unwrap()[0].retired_frame
    );
    let retired = battle.inspection().unwrap()[0];
    tick(&mut battle, 1);
    let records = battle.inspection().unwrap();
    assert_eq!(records.len(), 2);
    assert_eq!((records[0].id, records[1].id, records[1].slot), (1, 2, 1));
    assert_ne!(records[1].serial, first.serial);
    assert_eq!(records[0].revivals, 1);
    assert_eq!(
        (records[0].last_frame, records[0].animation),
        (retired.last_frame, retired.animation)
    );
}

#[test]
fn inspector_keeps_both_damage_sources_and_discards_barrier_absorption() {
    // 既存の原本照合済みネコ定義から、攻撃元を2体に制御する。
    let data: Value = serde_json::from_str(
        include_str!("../../../../native/kbcs-core/tests/actor-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    let cat: Vec<i32> =
        serde_json::from_value(data["cases"][0]["definition"]["cells"].clone()).unwrap();
    for protected in [false, true] {
        let mut first = profile(&cat, 0, 2);
        first.definition.cells = cat.clone().try_into().unwrap();
        let mut second = profile(&cat, 0, 3);
        second.definition.cells = cat.clone().try_into().unwrap();
        second.deployment_slot = 1;
        let raw: Vec<i32> = serde_json::from_value(fixture()["breakerEnemy"].clone()).unwrap();
        let mut enemy = profile(&raw, 1, 37);
        enemy.definition.cells[3] = 0;
        enemy.definition.cells[15] = 1;
        let mut c = config();
        c.screen.present[0] = 1;
        c.screen.present[1] = 1;
        c.enemy_max = 1;
        c.hit.effects.target_count = 1;
        c.hit.effects.scenario_level = 1;
        for (index, phase) in [0x2328, 0x2360, 0x2398].into_iter().enumerate() {
            c.effect_clocks[index] = [phase, 30, 30];
        }
        let mut battle = Battle::new(
            &c,
            &[first, second, enemy],
            &[stage::Row([
                37, 1, 0, 1000, 1000, 100, 0, 0, 0, 100, 0, 100, 0, 0,
            ])],
        )
        .unwrap();
        battle.cheats(5).unwrap();
        for control in [1000, 1001] {
            battle
                .advance(&battle_screen::Input {
                    control,
                    ticks: 6,
                    ..Default::default()
                })
                .unwrap();
        }
        let allies: Vec<_> = battle
            .inspection()
            .unwrap()
            .iter()
            .filter(|actor| actor.side == 0)
            .copied()
            .collect();
        assert_eq!(allies.len(), 2);
        for slot in [1, 2] {
            edit(&mut battle, 0, slot, |w| {
                w[3] = 8100;
                w[1] = 0;
                w[2] = 0;
            });
        }
        edit(&mut battle, 1, 1, |w| {
            w[3] = 8000;
            w[1] = 0;
            w[2] = 0;
            w[7] = 2;
            w[8] = 2;
            w[130] = if protected { 1000 } else { 0 };
        });
        let victim = battle
            .inspection()
            .unwrap()
            .iter()
            .find(|actor| actor.side == 1)
            .unwrap()
            .id;
        if protected {
            tick(&mut battle, 30);
            assert_eq!(battle.actors().unwrap().0[1][1].words[8], 2);
            assert!(battle.inspection_sources(victim).unwrap().is_empty());
            edit(&mut battle, 0, 1, |w| {
                w[1] = 0;
                w[61] = 10000;
            });
            edit(&mut battle, 0, 2, |w| {
                w[1] = 0;
                w[2] = 0;
            });
            edit(&mut battle, 1, 1, |w| {
                w[130] = 0;
                w[7] = 1;
                w[8] = 1;
            });
        }
        for _ in 0..90 {
            tick(&mut battle, 1);
            if battle
                .inspection()
                .unwrap()
                .iter()
                .any(|actor| actor.id == victim && actor.deaths > 0)
            {
                break;
            }
        }
        let sources = battle.inspection_sources(victim).unwrap();
        let ids: Vec<_> = sources.iter().map(|source| source.actor_id).collect();
        assert_eq!(
            ids,
            if protected {
                vec![allies[1].id]
            } else {
                vec![allies[0].id, allies[1].id]
            }
        );
        assert!(
            sources
                .iter()
                .all(|source| source.kind == 1 && source.side == 0 && source.reserved > 0)
        );
        assert!(sources.iter().all(|source| source.profile
            == if source.actor_id == allies[0].id {
                0
            } else {
                1
            }));
    }
}
