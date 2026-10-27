use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy)]
struct Part {
    cells: [i32; 13],
}
#[repr(C)]
#[derive(Clone, Copy, Serialize)]
pub struct Cut {
    pub x: i32,
    pub y: i32,
    pub width: i32,
    pub height: i32,
}
#[repr(C)]
#[derive(Clone, Copy)]
struct Key {
    frame: i32,
    value: i32,
    easing: i32,
    power: i32,
}
#[repr(C)]
#[derive(Clone, Copy)]
struct Track {
    part: i32,
    property: i32,
    repeat: i32,
    first: i32,
    count: i32,
}
#[repr(C)]
struct PoseInput {
    units: [i32; 3],
    frame: i32,
    repeat: i32,
    anchor: i32,
    facing: i32,
    config: [i32; 6],
    root_override: i32,
    root: [f64; 5],
}
#[repr(C)]
#[derive(Default, Clone, Copy, Serialize, Deserialize, Debug, PartialEq)]
pub struct Packet {
    pub part: i32,
    pub cut: i32,
    pub blend: i32,
    pub opacity: f64,
    pub points: [i32; 8],
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct SceneInput {
    pub width: f64,
    pub center: f64,
    pub zoom: f64,
    pub cut_height: i32,
    pub castle: [i32; 3],
    pub focus: i32,
    #[serde(default)]
    pub viewport_width: i32,
    #[serde(default)]
    pub battle_rows: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct Layout {
    pub width: f64,
    pub center: f64,
    pub zoom: f64,
    pub minimum: f64,
    pub top: f64,
    pub bottom: f64,
    pub enemy: [f64; 4],
    pub player_x: f64,
    pub viewport_width: f64,
    pub y_origin: f64,
    pub y_offset: f64,
}
#[repr(C)]
#[derive(Default, Clone, Serialize)]
pub struct Command {
    pub texture: i32,
    pub layer: i32,
    pub count: i32,
    pub blend: i32,
    pub opacity: f64,
    pub points: [f64; 16],
    pub cut: [i32; 4],
    pub colors: [i32; 6],
}
#[repr(C)]
pub struct PaintInput {
    pub scene: SceneInput,
    pub cut: [i32; 4],
    pub top: [i32; 4],
    pub colors: [i32; 12],
    pub overlay: [i32; 7],
    pub self_sizes: [i32; 6],
    pub show_enemy: i32,
    pub show_player: i32,
}
#[repr(C)]
pub struct SpriteInput {
    pub rect: [f64; 4],
    pub angle: f64,
    pub opacity: f64,
    pub texture: i32,
    pub layer: i32,
    pub blend: i32,
    pub cut: [i32; 4],
}
unsafe extern "C" {
    fn kbcs_core_pose_contact(
        input: *const PoseInput,
        parts: *const Part,
        count: i32,
        tracks: *const Track,
        track_count: i32,
        keys: *const Key,
        key_count: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_model_contact(
        input: *const PoseInput,
        parts: *const Part,
        count: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_motion_lengths(
        tracks: *const Track,
        count: i32,
        keys: *const Key,
        key_count: i32,
        out: *mut i32,
    ) -> u32;
    fn kbcs_core_scene_paint(
        input: *const PaintInput,
        layout: *mut Layout,
        output: *mut Command,
        capacity: i32,
        written: *mut i32,
    ) -> u32;
    fn kbcs_core_scene_sprite(
        layout: *const Layout,
        input: *const SpriteInput,
        output: *mut Command,
    ) -> u32;
    fn kbcs_core_scene_transform(
        layout: *const Layout,
        input: *const Command,
        x: f64,
        y: f64,
        angle: f64,
        output: *mut Command,
    ) -> u32;
}
pub fn paint<'a>(
    input: &PaintInput,
    output: &'a mut [Command],
) -> Result<(Layout, &'a [Command]), u32> {
    let mut layout = Layout::default();
    let mut written = 0;
    let code = unsafe {
        kbcs_core_scene_paint(
            input,
            &mut layout,
            output.as_mut_ptr(),
            output.len() as i32,
            &mut written,
        )
    };
    if code != 0 {
        return Err(code);
    }
    Ok((layout, output.get(..written as usize).ok_or(2u32)?))
}
pub fn sprite(layout: &Layout, input: &SpriteInput) -> Result<Command, u32> {
    let mut command = Command::default();
    let code = unsafe { kbcs_core_scene_sprite(layout, input, &mut command) };
    if code == 0 { Ok(command) } else { Err(code) }
}
pub fn transform(
    layout: &Layout,
    input: &Command,
    x: f64,
    y: f64,
    angle: f64,
) -> Result<Command, u32> {
    let mut command = Command::default();
    let code = unsafe { kbcs_core_scene_transform(layout, input, x, y, angle, &mut command) };
    if code == 0 { Ok(command) } else { Err(code) }
}
unsafe extern "C" {
    fn kbcs_core_pose(
        input: *const PoseInput,
        parts: *const Part,
        count: i32,
        cuts: *const Cut,
        cut_count: i32,
        tracks: *const Track,
        track_count: i32,
        keys: *const Key,
        key_count: i32,
        output: *mut Packet,
        written: *mut i32,
    ) -> u32;
    fn kbcs_core_scene_layout(input: *const SceneInput, output: *mut Layout) -> u32;
}
pub fn layout(input: &SceneInput) -> Result<Layout, u32> {
    let mut output = Layout::default();
    let code = unsafe { kbcs_core_scene_layout(input, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
pub struct Model {
    parts: Vec<Part>,
    pub cuts: Vec<Cut>,
    tracks: Vec<Track>,
    keys: Vec<Key>,
    units: [i32; 3],
    configs: Vec<[i32; 6]>,
}
fn columns<const N: usize>(line: &str) -> Result<[i32; N], String> {
    let values = line
        .split(',')
        .take(N)
        .map(|v| {
            v.trim()
                .parse::<i32>()
                .map_err(|_| format!("整数列が不正です: {line}"))
        })
        .collect::<Result<Vec<_>, _>>()?;
    values
        .try_into()
        .map_err(|_| "原本の列数が不足しています".into())
}
fn lines(text: &str) -> Vec<&str> {
    text.trim_start_matches('\u{feff}')
        .lines()
        .map(str::trim)
        .filter(|s| !s.is_empty())
        .collect()
}
fn line<'a>(lines: &[&'a str], cursor: &mut usize) -> Result<&'a str, String> {
    let value = lines
        .get(*cursor)
        .copied()
        .ok_or("原本が途中で終わっています")?;
    *cursor += 1;
    Ok(value)
}
fn count(lines: &[&str], cursor: &mut usize, max: usize) -> Result<usize, String> {
    let value = line(lines, cursor)?
        .parse::<usize>()
        .map_err(|_| "原本の件数が不正です")?;
    if value > max {
        return Err("原本の件数が上限を超えています".into());
    }
    Ok(value)
}
impl Model {
    pub fn clock_lengths(&self) -> Result<[i32; 2], u32> {
        let mut out = [0; 2];
        let code = unsafe {
            kbcs_core_motion_lengths(
                self.tracks.as_ptr(),
                self.tracks.len() as i32,
                self.keys.as_ptr(),
                self.keys.len() as i32,
                out.as_mut_ptr(),
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn parse(
        cut_text: &str,
        model_text: &str,
        animation: Option<&str>,
    ) -> Result<Self, String> {
        let source = lines(cut_text);
        if source.first() != Some(&"[imgcut]") {
            return Err("imgcut形式が不正です".into());
        }
        let mut cursor = 3;
        let n = count(&source, &mut cursor, 8192)?;
        let cuts = (0..n)
            .map(|_| {
                let [x, y, width, height] = columns(line(&source, &mut cursor)?)?;
                Ok(Cut {
                    x,
                    y,
                    width,
                    height,
                })
            })
            .collect::<Result<Vec<_>, String>>()?;
        let source = lines(model_text);
        if !["[modelanim:model]", "[modelanim:model2]", "[mamodel]"]
            .contains(&source.first().copied().unwrap_or(""))
        {
            return Err("mamodel形式が不正です".into());
        }
        let mut cursor = 1;
        let version = count(&source, &mut cursor, 32)?;
        let n = count(&source, &mut cursor, 4096)?;
        let parts = (0..n)
            .map(|_| {
                Ok(Part {
                    cells: columns(line(&source, &mut cursor)?)?,
                })
            })
            .collect::<Result<Vec<_>, String>>()?;
        let units = if version >= 1 {
            columns(line(&source, &mut cursor)?)?
        } else {
            [100, 360, 255]
        };
        let mut configs = Vec::new();
        if version >= 3 {
            let n = count(&source, &mut cursor, 4096)?;
            for _ in 0..n {
                configs.push(columns(line(&source, &mut cursor)?)?);
            }
        }
        let (mut tracks, mut keys) = (Vec::new(), Vec::new());
        if let Some(text) = animation {
            let source = lines(text);
            if ![
                "[modelanim:animation]",
                "[modelanim:animation2]",
                "[maanim]",
            ]
            .contains(&source.first().copied().unwrap_or(""))
            {
                return Err("maanim形式が不正です".into());
            }
            let mut cursor = 2;
            let n = count(&source, &mut cursor, 32768)?;
            for _ in 0..n {
                let [part, property, repeat, _, _] = columns(line(&source, &mut cursor)?)?;
                let n = count(&source, &mut cursor, 262144)?;
                if keys.len() + n > 262144 {
                    return Err("モーションのキーが多すぎます".into());
                }
                tracks.push(Track {
                    part,
                    property,
                    repeat,
                    first: keys.len() as i32,
                    count: n as i32,
                });
                for _ in 0..n {
                    let [frame, value, easing, power] = columns(line(&source, &mut cursor)?)?;
                    keys.push(Key {
                        frame,
                        value,
                        easing,
                        power,
                    });
                }
            }
        }
        Ok(Self {
            parts,
            cuts,
            tracks,
            keys,
            units,
            configs,
        })
    }
    pub fn length(&self) -> i32 {
        self.tracks
            .iter()
            .filter(|track| track.count > 0)
            .map(|track| {
                let first = self.keys[track.first as usize].frame;
                let last = self.keys[(track.first + track.count - 1) as usize].frame;
                last + if first < 0 || track.repeat != 1 {
                    -first
                } else {
                    0
                }
            })
            .max()
            .unwrap_or(0)
            .max(0)
    }
    pub fn pose(
        &self,
        frame: i32,
        repeat: bool,
        anchor: bool,
        facing: i32,
    ) -> Result<Vec<Packet>, u32> {
        self.pose_with_root(frame, repeat, anchor, facing, None)
    }
    pub fn native_point(&self, frame: i32, config_index: usize) -> Result<[i32; 2], u32> {
        let config = *self.configs.get(config_index).ok_or(1u32)?;
        let input = PoseInput {
            units: self.units,
            frame,
            repeat: 0,
            anchor: 0,
            facing: 1,
            config,
            root_override: 0,
            root: [0.; 5],
        };
        let mut out = [0; 2];
        let code = unsafe {
            kbcs_core_pose_contact(
                &input,
                self.parts.as_ptr(),
                self.parts.len() as i32,
                self.tracks.as_ptr(),
                self.tracks.len() as i32,
                self.keys.as_ptr(),
                self.keys.len() as i32,
                out.as_mut_ptr(),
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn contact(&self, config_index: usize) -> Result<[i32; 2], u32> {
        let config = *self.configs.get(config_index).ok_or(1u32)?;
        let input = PoseInput {
            units: self.units,
            frame: 0,
            repeat: 0,
            anchor: 0,
            facing: 1,
            config,
            root_override: 0,
            root: [0.; 5],
        };
        let mut out = [0; 2];
        let code = unsafe {
            kbcs_core_model_contact(
                &input,
                self.parts.as_ptr(),
                self.parts.len() as i32,
                out.as_mut_ptr(),
            )
        };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn pose_config(
        &self,
        frame: i32,
        config_index: usize,
        facing: i32,
    ) -> Result<Vec<Packet>, u32> {
        self.pose_internal(frame, false, true, facing, None, config_index, true)
    }
    pub fn pose_scaled(&self, frame: i32, scale: [i32; 2]) -> Result<Vec<Packet>, u32> {
        let part = &self.parts.first().ok_or(1u32)?.cells;
        self.pose_with_root(
            frame,
            false,
            false,
            1,
            Some([
                1.,
                f64::from(part[8]) * f64::from(scale[0]) / f64::from(self.units[0]) / 1000.,
                f64::from(part[9]) * f64::from(scale[1]) / f64::from(self.units[0]) / 1000.,
                f64::from(part[10]) * 360. / f64::from(self.units[1]),
                f64::from(part[11]) * 255. / f64::from(self.units[2]),
            ]),
        )
    }
    pub fn pose_with_root(
        &self,
        frame: i32,
        repeat: bool,
        anchor: bool,
        facing: i32,
        root: Option<[f64; 5]>,
    ) -> Result<Vec<Packet>, u32> {
        self.pose_internal(frame, repeat, anchor, facing, root, 0, false)
    }
    #[allow(clippy::too_many_arguments)]
    fn pose_internal(
        &self,
        frame: i32,
        repeat: bool,
        anchor: bool,
        facing: i32,
        root: Option<[f64; 5]>,
        config_index: usize,
        native_anchor: bool,
    ) -> Result<Vec<Packet>, u32> {
        let input = PoseInput {
            units: self.units,
            frame,
            repeat: i32::from(repeat),
            anchor: if anchor && self.configs.get(config_index).is_some() {
                if native_anchor { 2 } else { 1 }
            } else {
                0
            },
            facing,
            config: self.configs.get(config_index).copied().unwrap_or_default(),
            root_override: i32::from(root.is_some()),
            root: root.unwrap_or([1., 1., 1., 0., 255.]),
        };
        let mut packets = vec![Packet::default(); self.parts.len()];
        let mut written = 0;
        // バッファの所有者は呼出側。C++は描画デバイスやポインタを保持しない。
        let code = unsafe {
            kbcs_core_pose(
                &input,
                self.parts.as_ptr(),
                self.parts.len() as i32,
                self.cuts.as_ptr(),
                self.cuts.len() as i32,
                self.tracks.as_ptr(),
                self.tracks.len() as i32,
                self.keys.as_ptr(),
                self.keys.len() as i32,
                packets.as_mut_ptr(),
                &mut written,
            )
        };
        if code != 0 {
            return Err(code);
        }
        packets.truncate(written as usize);
        Ok(packets)
    }
}

#[test]
fn integer_pose_reference_vectors() {
    let fixture: serde_json::Value = serde_json::from_str(
        include_str!("../../../native/kbcs-core/tests/pose-vectors.json")
            .trim_start_matches('\u{feff}'),
    )
    .unwrap();
    for case in fixture["cases"].as_array().unwrap() {
        let input = &case["input"];
        let model = Model::parse(
            input["cut"].as_str().unwrap(),
            input["model"].as_str().unwrap(),
            input["animation"].as_str(),
        )
        .unwrap();
        for vector in case["vectors"].as_array().unwrap() {
            let packets = model
                .pose(
                    vector["frame"].as_i64().unwrap() as i32,
                    vector["loop"].as_bool().unwrap(),
                    true,
                    vector["facing"].as_i64().unwrap() as i32,
                )
                .unwrap();
            let expected =
                serde_json::from_value::<Vec<Packet>>(vector["packets"].clone()).unwrap();
            assert_eq!(packets.len(), expected.len());
            for (actual, expected) in packets.iter().zip(expected) {
                assert!((actual.opacity - expected.opacity).abs() < 1e-14);
                let adjusted = Packet {
                    opacity: expected.opacity,
                    ..*actual
                };
                assert_eq!(
                    adjusted, expected,
                    "{} frame {} loop {} facing {}",
                    case["stem"], vector["frame"], vector["loop"], vector["facing"]
                );
            }
        }
    }
}

unsafe extern "C" {
    fn kbcs_core_scene_instance(
        layout: *const Layout,
        input: *const Command,
        x: f64,
        y: f64,
        spacing: f64,
        index: i32,
        output: *mut Command,
    ) -> u32;
}
pub fn instance(
    layout: &Layout,
    input: &Command,
    x: f64,
    y: f64,
    spacing: f64,
    index: i32,
) -> Result<Command, u32> {
    let mut output = Command::default();
    let code =
        unsafe { kbcs_core_scene_instance(layout, input, x, y, spacing, index, &mut output) };
    if code == 0 { Ok(output) } else { Err(code) }
}
