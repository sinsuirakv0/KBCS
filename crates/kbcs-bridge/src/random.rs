pub struct Random {
    state: u32,
}
unsafe extern "C" {
    fn kbcs_core_random_bounded(state: *mut u32, bound: i32, output: *mut i32) -> u32;
}
impl Random {
    pub fn new(seed: u32) -> Result<Self, u32> {
        if seed == 0 {
            Err(1)
        } else {
            Ok(Self { state: seed })
        }
    }
    pub fn state(&self) -> u32 {
        self.state
    }
    pub(crate) fn state_mut(&mut self) -> &mut u32 {
        &mut self.state
    }
    pub fn bounded(&mut self, bound: i32) -> Result<i32, u32> {
        let mut value = 0;
        // 個体枠・レイヤー・間隔で同じ所有状態を順番に使う。範囲1も省略しない。
        let code = unsafe { kbcs_core_random_bounded(&mut self.state, bound, &mut value) };
        if code == 0 { Ok(value) } else { Err(code) }
    }
}
#[test]
fn native_random_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/random-vectors.json"
    ))
    .unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let mut random = Random::new(vector["seed"].as_u64().unwrap() as u32).unwrap();
        for step in vector["steps"].as_array().unwrap() {
            assert_eq!(
                i64::from(
                    random
                        .bounded(step["bound"].as_i64().unwrap() as i32)
                        .unwrap()
                ),
                step["value"].as_i64().unwrap()
            );
            assert_eq!(u64::from(random.state()), step["state"].as_u64().unwrap());
        }
        let before = random.state();
        assert_eq!(random.bounded(0), Ok(0));
        assert_eq!(random.state(), before);
    }
    for vector in fixture["inverted"].as_array().unwrap() {
        use crate::stage::{Context, Row, State, tick};
        let row: Row = serde_json::from_value(vector["row"].clone()).unwrap();
        let rows = [row];
        let mut states = [State::default()];
        let mut context = Context {
            global_wait: 0,
            kill_delta: 0,
            active_enemies: 0,
            max_enemies: 50,
            castle_hp: 100,
            castle_max_hp: 100,
            castle_damage: 0,
            damage_condition: 0,
            paused: 0,
            global_min: 3,
            global_max: 7,
        };
        let mut random = Random::new(vector["seed"].as_u64().unwrap() as u32).unwrap();
        let candidate = tick(&rows, &mut states, &mut context).unwrap().unwrap();
        let global = random.bounded(5).unwrap();
        let interval = random.bounded(row.0[4] - row.0[3] + 1).unwrap();
        candidate.commit(global, interval).unwrap();
        assert_eq!(u64::from(random.state()), vector["state"].as_u64().unwrap());
        assert_eq!(states[0].wait, row.0[3]);
        assert_eq!(states[0].spawned, 1);
        assert_eq!(
            i64::from(context.global_wait),
            vector["result"]["globalWait"].as_i64().unwrap()
        );
    }
    assert!(matches!(Random::new(0), Err(1)));
}
