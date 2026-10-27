use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Default, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Config {
    pub worker_level: i32,
    pub wallet_level: i32,
    pub attack_level: i32,
    pub charge_level: i32,
    pub chapter: i32,
    pub income_treasure: i32,
    pub wallet_treasure: i32,
    pub charge_treasure: i32,
    pub speed_treasure: i32,
    pub income_combo: i32,
    pub wallet_combo: i32,
    pub charge_combo: i32,
    pub charge_start_combo: i32,
    pub items: i32,
    pub speed: i32,
    pub fixed_money: i32,
    pub costs: [i32; 10],
    pub present: [i32; 10],
    pub blocked: [i32; 10],
    #[serde(default)]
    pub viewport_width: i32,
    #[serde(default)]
    pub description_lines: [i32; 10],
}
#[repr(C)]
#[derive(Clone, Default, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct State {
    pub frame: i32,
    pub intro: i32,
    pub rows: i32,
    pub page: i32,
    pub page_frame: i32,
    pub page_direction: i32,
    pub paused: i32,
    pub money: i32,
    pub worker: i32,
    pub cannon: i32,
    pub holding: i32,
    pub hold_frames: i32,
    pub pointer_down: i32,
    pub pointer_x: i32,
    pub pointer_y: i32,
    pub guard: i32,
    pub pending_control: i32,
    pub items_on: i32,
    pub request_slot: i32,
    pub request_cannon: i32,
    pub ui_frame: i32,
    pub speed_mode: i32,
    pub wallet_flash: i32,
    pub description_item: i32,
    pub description_wait: i32,
    pub start_x: i32,
    pub start_y: i32,
    pub gesture: i32,
    pub page_step: i32,
    pub request_action: i32,
    pub bgm_level: i32,
    pub se_level: i32,
    pub vibration_on: i32,
    pub info_mode: i32,
    pub info_slot: i32,
    pub saved_rows: i32,
    pub hud_frame: i32,
    #[serde(default)]
    pub battle_mode: i32,
}
#[repr(C)]
#[derive(Clone, Default, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Input {
    pub ticks: i32,
    pub phase: i32,
    pub x: i32,
    pub y: i32,
    pub control: i32,
}
#[repr(C)]
#[derive(Clone, Default, Debug, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct Layout {
    pub slots: [[i32; 4]; 10],
    pub labels: [[i32; 2]; 10],
    pub modes: [i32; 10],
    pub order: [i32; 10],
    pub scene_y: i32,
    pub wallet_max: i32,
    pub income: i32,
    pub upgrade_cost: i32,
    pub cannon_max: i32,
    pub cannon_initial: i32,
    pub cannon_gauge: i32,
    pub fade_count: i32,
    pub fade_sizes: [i32; 21],
    pub fade: [[i32; 8]; 21],
    pub controls: [[i32; 5]; 8],
    pub item_icons: [[i32; 5]; 6],
    pub pause_icon: [i32; 4],
    pub money_base: i32,
    pub speed_value: i32,
    pub cannon_base: i32,
    pub cannon_label: i32,
    pub cannon_bands: i32,
    pub wallet_base: i32,
    pub info_box: [i32; 4],
    pub description_box: [i32; 4],
    pub description_arrow: [i32; 6],
    pub menu_count: i32,
    pub menu_sprites: [[i32; 6]; 24],
}

#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Request {
    pub config: Config,
    pub state: State,
    pub input: Input,
}
#[derive(Serialize)]
pub struct Frame {
    pub state: State,
    pub layout: Layout,
}
unsafe extern "C" {
    fn kbcs_core_battle_screen_step(
        config: *const Config,
        state: *const State,
        input: *const Input,
        out: *mut State,
        layout: *mut Layout,
    ) -> u32;
}
pub fn frame(request: &Request) -> Result<Frame, u32> {
    let mut state = State::default();
    let mut layout = Layout::default();
    let code = unsafe {
        kbcs_core_battle_screen_step(
            &request.config,
            &request.state,
            &request.input,
            &mut state,
            &mut layout,
        )
    };
    if code == 0 {
        Ok(Frame { state, layout })
    } else {
        Err(code)
    }
}

#[test]
fn native_screen_witnesses() {
    let data: serde_json::Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/battle-screen-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    let config = Config {
        speed: 3,
        fixed_money: -1,
        ..Config::default()
    };
    let base = State {
        intro: 24,
        rows: 2,
        holding: -1,
        pending_control: -1,
        ..State::default()
    };
    let call = |config: Config, state: State, input: Input| {
        frame(&Request {
            config,
            state,
            input,
        })
        .unwrap()
    };
    for case in data["fade"].as_array().unwrap() {
        let value = call(
            config.clone(),
            State {
                intro: case["frame"].as_i64().unwrap() as i32,
                ..base.clone()
            },
            Input::default(),
        );
        let polygons = case["polygons"].as_array().unwrap();
        assert_eq!(value.layout.fade_count as usize, polygons.len());
        for (i, p) in polygons.iter().enumerate() {
            let expected: Vec<i32> = serde_json::from_value(p.clone()).unwrap();
            assert_eq!(&value.layout.fade[i][..expected.len()], expected);
        }
    }
    for case in data["economy"].as_array().unwrap() {
        let level = case["level"].as_i64().unwrap() as i32;
        let combo = case["combo"].as_i64().unwrap() as i32;
        let value = call(
            Config {
                worker_level: level,
                wallet_level: level,
                income_treasure: 300,
                wallet_treasure: 300000,
                income_combo: combo,
                wallet_combo: combo,
                ..config.clone()
            },
            State {
                worker: case["worker"].as_i64().unwrap() as i32,
                ..base.clone()
            },
            Input::default(),
        );
        assert_eq!(
            value.layout.wallet_max,
            case["walletMax"].as_i64().unwrap() as i32
        );
        assert_eq!(value.layout.income, case["income"].as_i64().unwrap() as i32);
        assert_eq!(
            value.layout.upgrade_cost,
            case["upgrade"].as_i64().unwrap() as i32
        );
    }
    for case in data["charges"].as_array().unwrap() {
        let get = |key: &str| case[key].as_i64().unwrap() as i32;
        let value = call(
            Config {
                attack_level: get("attack"),
                charge_level: get("charge"),
                chapter: get("chapter"),
                speed_treasure: get("speed"),
                charge_treasure: get("treasure"),
                charge_combo: get("combo"),
                ..config.clone()
            },
            base.clone(),
            Input::default(),
        );
        assert_eq!(value.layout.cannon_max, get("maximum"));
    }
    for case in data["pages"].as_array().unwrap() {
        for native in case["states"].as_array().unwrap() {
            let page = native[0].as_i64().unwrap() as i32;
            let f = native[5].as_i64().unwrap() as i32;
            let value = call(
                config.clone(),
                State {
                    rows: 1,
                    page,
                    page_frame: f,
                    page_direction: case["direction"].as_i64().unwrap() as i32,
                    ..base.clone()
                },
                Input::default(),
            );
            if f > 0 {
                assert_eq!(
                    value.layout.labels[0][1] - 544,
                    native[if page == 0 { 1 } else { 2 }].as_i64().unwrap() as i32
                );
                assert_eq!(
                    value.layout.labels[5][1] - 544,
                    native[if page == 0 { 2 } else { 1 }].as_i64().unwrap() as i32
                );
            }
        }
    }
    let enabled = Config {
        present: [1; 10],
        ..config.clone()
    };
    for case in data["hits"].as_array().unwrap() {
        let value = call(
            enabled.clone(),
            base.clone(),
            Input {
                ticks: 6,
                phase: 2,
                x: case["point"][0].as_i64().unwrap() as i32,
                y: case["point"][1].as_i64().unwrap() as i32,
                ..Input::default()
            },
        );
        assert_eq!(
            i32::from(value.state.request_slot == 0),
            case["inside"].as_i64().unwrap() as i32
        );
    }
    let released = call(
        enabled.clone(),
        base.clone(),
        Input {
            ticks: 1,
            phase: 2,
            x: 160,
            y: 450,
            ..Input::default()
        },
    );
    assert_eq!(released.state.request_slot, -1);
    let before = call(
        enabled.clone(),
        released.state,
        Input {
            ticks: 4,
            ..Input::default()
        },
    );
    assert_eq!(before.state.request_slot, -1);
    let after = call(
        enabled.clone(),
        before.state,
        Input {
            ticks: 1,
            ..Input::default()
        },
    );
    assert_eq!(after.state.request_slot, 0);
    assert_eq!(after.state.money, 6 * 25);
    let down = call(
        enabled.clone(),
        base.clone(),
        Input {
            ticks: 1,
            phase: 1,
            x: 160,
            y: 450,
            ..Input::default()
        },
    );
    let held = call(
        enabled.clone(),
        down.state,
        Input {
            ticks: 14,
            ..Input::default()
        },
    );
    assert_eq!(held.state.hold_frames, 14);
    let up = call(
        enabled.clone(),
        held.state,
        Input {
            ticks: 6,
            phase: 2,
            x: 160,
            y: 450,
            ..Input::default()
        },
    );
    assert_eq!(up.state.request_slot, -1);
    let paused = call(
        enabled.clone(),
        State {
            paused: 1,
            ..base.clone()
        },
        Input {
            ticks: 30,
            ..Input::default()
        },
    );
    assert_eq!(paused.state.frame, 0);
    let sped = call(
        Config {
            items: 1,
            ..enabled.clone()
        },
        State {
            items_on: 1,
            speed_mode: 2,
            ..base.clone()
        },
        Input {
            ticks: 1,
            ..Input::default()
        },
    );
    assert_eq!(sped.state.frame, 3);
    let controls: serde_json::Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/battle-controls-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in controls["swipes"].as_array().unwrap() {
        let delta: [i32; 2] = serde_json::from_value(case["delta"].clone()).unwrap();
        let result = call(
            config.clone(),
            State {
                rows: 1,
                pointer_down: 1,
                start_x: 500,
                start_y: 570,
                description_item: -1,
                ..base.clone()
            },
            Input {
                ticks: 1,
                phase: 4,
                x: 500 + delta[0],
                y: 570 + delta[1],
                ..Input::default()
            },
        );
        assert_eq!(
            i32::from(result.state.page_frame > 0),
            case["active"].as_i64().unwrap() as i32
        );
        if result.state.page_frame > 0 {
            assert_eq!(
                result.state.page_direction,
                case["direction"].as_i64().unwrap() as i32
            );
            assert_eq!(result.state.request_slot, -1);
        }
    }
    for case in controls["pause"].as_array().unwrap() {
        let result = call(
            Config {
                viewport_width: case["width"].as_i64().unwrap() as i32,
                ..config.clone()
            },
            State {
                paused: 1,
                ..base.clone()
            },
            Input::default(),
        );
        for (actual, expected) in result
            .layout
            .menu_sprites
            .iter()
            .zip(case["sprites"].as_array().unwrap())
        {
            let values: Vec<i32> = serde_json::from_value(expected.clone()).unwrap();
            assert_eq!(&actual[1..4], &values[..3]);
            if values[3] != 0 {
                assert_eq!(&actual[4..], &values[3..]);
            }
        }
    }
    let mut speed_state = State {
        items_on: 1,
        speed_mode: 1,
        ..base.clone()
    };
    for expected in [2, 0, 1] {
        let result = call(
            Config {
                items: 1,
                ..config.clone()
            },
            speed_state,
            Input {
                control: 5,
                ..Input::default()
            },
        );
        assert_eq!(result.state.speed_mode, expected);
        assert_eq!(
            result.layout.speed_value,
            if expected == 0 { 1 } else { expected + 1 }
        );
        speed_state = result.state;
    }
    for case in controls["camera"].as_array().unwrap() {
        let rows = case["rows"].as_i64().unwrap() as i32;
        let result = call(
            config.clone(),
            State {
                rows,
                ..base.clone()
            },
            Input::default(),
        );
        assert_eq!(
            result.layout.scene_y,
            case["offset"].as_i64().unwrap() as i32
        );
        let camera = crate::render::layout(&crate::render::SceneInput {
            width: 10000.,
            center: 4000.,
            zoom: 1.,
            cut_height: 510,
            castle: [0; 3],
            focus: 0,
            viewport_width: 1280,
            battle_rows: rows,
        })
        .unwrap();
        assert_eq!(camera.y_offset, case["offset"].as_f64().unwrap());
        assert_eq!(camera.bottom, 640. + camera.y_offset);
    }

    for case in controls["money"].as_array().unwrap() {
        let value = call(
            config.clone(),
            State {
                wallet_flash: case["timer"].as_i64().unwrap() as i32,
                ..base.clone()
            },
            Input::default(),
        );
        assert_eq!(
            value.layout.money_base,
            case["base"].as_i64().unwrap() as i32
        );
    }
    let menu_press = call(
        config.clone(),
        base.clone(),
        Input {
            ticks: 1,
            phase: 2,
            x: 10,
            y: 10,
            ..Input::default()
        },
    );
    assert_eq!(menu_press.state.paused, 0);
    let menu_open = call(
        config.clone(),
        menu_press.state,
        Input {
            ticks: 5,
            ..Input::default()
        },
    );
    assert_eq!(menu_open.state.paused, 1);
    let frame_before = menu_open.state.frame;
    let close = call(
        config.clone(),
        menu_open.state,
        Input {
            ticks: 6,
            phase: 2,
            x: 700,
            y: 150,
            ..Input::default()
        },
    );
    assert_eq!(close.state.paused, 0);
    assert_eq!(close.state.frame, frame_before);

    for case in controls["ready"].as_array().unwrap() {
        let flash = case["flash"].as_i64().unwrap() as i32;
        let result = call(
            config.clone(),
            State {
                cannon: 0,
                hud_frame: flash * 3,
                ..base.clone()
            },
            Input::default(),
        );
        let mut actual = Vec::new();
        if result.layout.cannon_base >= 0 {
            actual.push(vec![result.layout.cannon_base, 814, 510]);
        }
        for band in 0..result.layout.cannon_bands {
            actual.push(vec![
                11 + band,
                814,
                if band == 9 { 510 } else { 628 - band * 12 },
            ]);
        }
        actual.push(vec![result.layout.cannon_label, 831, 581]);
        assert_eq!(
            actual,
            serde_json::from_value::<Vec<Vec<i32>>>(case["cuts"].clone()).unwrap()
        );
    }
    let maximum = call(
        config.clone(),
        State {
            worker: 7,
            ..base.clone()
        },
        Input::default(),
    );
    assert_eq!(
        maximum.layout.wallet_base,
        controls["walletMax"][0][0].as_i64().unwrap() as i32
    );
    for hud_frame in 0..6 {
        assert_eq!(
            call(
                config.clone(),
                State {
                    worker: 7,
                    hud_frame,
                    ..base.clone()
                },
                Input::default()
            )
            .layout
            .wallet_base,
            maximum.layout.wallet_base
        );
    }
    let description = call(
        Config {
            items: 32,
            ..config.clone()
        },
        base.clone(),
        Input {
            ticks: 1,
            phase: 1,
            x: 925,
            y: 80,
            ..Input::default()
        },
    );
    assert_eq!(description.state.description_wait, 4);
    assert_eq!(description.layout.description_arrow[1], 118);
    let info = call(
        config.clone(),
        State {
            paused: 1,
            rows: 1,
            ..base.clone()
        },
        Input {
            ticks: 6,
            phase: 2,
            x: 30,
            y: 580,
            ..Input::default()
        },
    );
    assert_eq!(
        (info.state.info_mode, info.state.rows, info.state.frame),
        (1, 2, base.frame)
    );
    let finish = call(
        config.clone(),
        info.state,
        Input {
            ticks: 6,
            phase: 2,
            x: 30,
            y: 580,
            ..Input::default()
        },
    );
    assert_eq!(
        (
            finish.state.info_mode,
            finish.state.rows,
            finish.state.paused
        ),
        (0, 1, 0)
    );
    for level in 0..4 {
        let result = call(
            config.clone(),
            State {
                paused: 1,
                bgm_level: level,
                se_level: level,
                ..base.clone()
            },
            Input::default(),
        );
        for (control, key) in [(2, "volumeBgm"), (3, "volumeSe")] {
            let x = result.layout.controls[control][1];
            let icon = result
                .layout
                .menu_sprites
                .iter()
                .take(result.layout.menu_count as usize)
                .find(|sprite| sprite[2] == x && sprite[3] == 242 && sprite[4] == 52)
                .unwrap();
            assert_eq!(
                icon[1],
                controls[key][level as usize].as_i64().unwrap() as i32
            );
        }
    }
    // 3倍の設定を維持して、手動では指定した論理Fだけを進める。
    let stepped = call(
        config.clone(),
        State {
            speed_mode: 2,
            cannon: 100,
            ..base.clone()
        },
        Input {
            control: 10,
            ticks: 1,
            ..Input::default()
        },
    );
    assert_eq!(
        (
            stepped.state.frame,
            stepped.state.cannon,
            stepped.state.speed_mode
        ),
        (1, 99, 2)
    );
    let batch = call(
        config.clone(),
        stepped.state,
        Input {
            control: 10,
            ticks: 10,
            ..Input::default()
        },
    );
    assert_eq!(
        (
            batch.state.frame,
            batch.state.cannon,
            batch.state.speed_mode
        ),
        (11, 89, 2)
    );
}
