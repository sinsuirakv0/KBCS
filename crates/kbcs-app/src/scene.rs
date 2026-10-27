use anyhow::{Context, Result, ensure};
use kbcs_bridge::{
    render::{self, Command, Cut, Model, PaintInput, SceneInput},
    render_effects,
};
use kbcs_data::{stage_media, store::Database};
use serde::{Deserialize, Serialize};
use serde_json::{Value, json};
use std::collections::BTreeSet;

fn yes() -> bool {
    true
}
fn zoom() -> f64 {
    1.
}
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    #[serde(default)]
    pub session: String,
    pub background: i64,
    pub width: f64,
    pub castle: Option<i64>,
    pub castle_set: i32,
    pub enemy_castle: Option<u32>,
    #[serde(default)]
    pub focus: i32,
    pub center: Option<f64>,
    #[serde(default = "zoom")]
    pub zoom: f64,
    #[serde(default)]
    pub frame: i32,
    #[serde(default = "yes")]
    pub show_enemy: bool,
    #[serde(default = "yes")]
    pub show_player: bool,
    #[serde(default = "yes")]
    pub show_effects: bool,
    #[serde(default)]
    pub viewport_width: i32,
    #[serde(default)]
    pub battle_rows: i32,
}
impl Input {
    pub fn key(&self) -> String {
        format!(
            "{}:{}:{:?}:{}:{:?}:{}",
            self.background,
            self.width,
            self.castle,
            self.castle_set,
            self.enemy_castle,
            self.session
        )
    }
}
fn core(code: u32) -> anyhow::Error {
    anyhow::anyhow!("描画コアの入力・計算エラー: {code}")
}
fn array<const N: usize>(value: &Value) -> Result<[i32; N]> {
    value
        .as_array()
        .context("描画の数値配列なし")?
        .iter()
        .map(|n| {
            n.as_i64()
                .and_then(|n| i32::try_from(n).ok())
                .context("描画の整数値が不正です")
        })
        .collect::<Result<Vec<_>>>()?
        .try_into()
        .map_err(|_| anyhow::anyhow!("描画の列数が不正です"))
}
fn parsed_cuts(database: &Database, path: &str) -> Vec<Cut> {
    stage_media::cuts(database, path)
        .unwrap_or_default()
        .into_iter()
        .map(|[x, y, width, height]| Cut {
            x,
            y,
            width,
            height,
        })
        .collect()
}
struct Asset {
    model: Model,
    texture: i32,
}
#[derive(Serialize)]
pub struct Frame<'a> {
    pub layout: render::Layout,
    pub commands: Vec<Command>,
    pub textures: &'a [Option<String>],
    pub animated: bool,
    pub missing: &'a [String],
    pub issues: usize,
    pub frame: i32,
    pub core: &'static str,
    pub ruleset: u32,
    #[serde(rename = "computeMs")]
    pub compute_ms: f64,
}
pub struct Scene {
    paint_buffer: Vec<Command>,
    background: Value,
    source: Value,
    textures: Vec<Option<String>>,
    sizes: Vec<[i32; 2]>,
    castle: [i32; 3],
    assets: Vec<Asset>,
    runtime: Option<render_effects::Runtime>,
    actor: Option<Asset>,
    classic: i32,
    cuts: Vec<Cut>,
    common: Vec<Cut>,
    issues: usize,
    missing: Vec<String>,
}
impl Scene {
    pub fn player_parts(
        &mut self,
        database: &Database,
        cannon: u8,
        base: i32,
        decoration: i32,
    ) -> Result<()> {
        for (index, part, id) in [(2, 3, decoration), (3, 2, base), (4, 0, i32::from(cannon))] {
            let path = format!("Number/nyankoCastle_{part:03}_{id:02}.png");
            self.sizes[index] = stage_media::image_size(database, &path)?;
            self.textures[index] = Some(path);
        }
        Ok(())
    }
    pub fn owned_castle(&mut self) {
        self.actor = None;
    }
    pub fn textures(&self) -> &[Option<String>] {
        &self.textures
    }
    pub fn castle_geometry(&self) -> [i32; 3] {
        self.castle
    }
    pub fn texture(&mut self, path: &str) -> i32 {
        if let Some(index) = self
            .textures
            .iter()
            .position(|p| p.as_deref() == Some(path))
        {
            return index as i32;
        }
        let index = self.textures.len();
        self.textures.push(Some(path.into()));
        index as i32
    }
    pub fn new(database: &Database, input: &Input) -> Result<Self> {
        ensure!(
            input.width.is_finite()
                && input.width > 0.
                && input.width <= 10000000.
                && input.background >= 0
                && (0..=3).contains(&input.castle_set),
            "ステージ描画の指定が不正です"
        );
        let source = stage_media::scene_source(database, input.background)?;
        let background = source["background"].clone();
        let prefix = ["ec", "wc", "sc", "rc"][input.castle_set as usize];
        let castle_image = input
            .castle
            .filter(|_| input.enemy_castle.is_none())
            .map(|id| format!("Image/{prefix}{id:03}.png"));
        let mut textures = vec![
            background["path"].as_str().map(str::to_owned),
            castle_image,
            Some("Number/nyankoCastle_003_00.png".into()),
            Some("Number/nyankoCastle_002_00.png".into()),
            Some("Number/nyankoCastle_000_00.png".into()),
            Some("Image/bubble02.png".into()),
            Some("Image/bubble03_bg040.png".into()),
            Some("Number/000_a.png".into()),
        ];
        let mut missing = Vec::new();
        let sizes = textures
            .iter_mut()
            .enumerate()
            .map(|(index, path)| {
                if let Some(name) = path {
                    match stage_media::image_size(database, name) {
                        Ok(size) => return size,
                        Err(_) => {
                            if index < 5 {
                                missing.push(name.clone());
                            }
                            *path = None;
                        }
                    }
                }
                [0; 2]
            })
            .collect::<Vec<_>>();
        let settings_path = format!(
            "Data/enemyCastleData{}.csv",
            ["0", "1", "2", "Legend"][input.castle_set as usize]
        );
        let settings = source["files"][&settings_path].as_str().unwrap_or("");
        let rows = stage_media::numeric_rows(settings.as_bytes())?
            .into_iter()
            .map(|(_, v)| v)
            .collect::<Vec<_>>();
        let castle = input
            .castle
            .and_then(|id| usize::try_from(id).ok())
            .and_then(|id| rows.get(id))
            .map(|r| {
                [
                    r.first().copied().flatten().unwrap_or(0) as i32,
                    r.get(1).copied().flatten().unwrap_or(0) as i32,
                    r.get(2).copied().flatten().unwrap_or(127) as i32,
                ]
            })
            .unwrap_or([0, 0, 127]);
        let cut_id = background["raw"][13].as_i64().context("背景の分割IDなし")?;
        let cuts = parsed_cuts(database, &format!("ImageData/bg{cut_id:02}.imgcut"));
        let common = parsed_cuts(database, "ImageData/000_a.imgcut");
        let classic = if [
            2, 3, 13, 14, 15, 26, 27, 33, 34, 40, 41, 46, 47, 55, 58, 72, 75, 81, 101, 123, 146,
            169, 197, 1008, 1074,
        ]
        .contains(&input.background)
        {
            input.background as i32
        } else {
            -1
        };
        let mut scene = Self {
            paint_buffer: vec![Command::default(); 16384],
            background,
            source,
            textures,
            sizes,
            castle,
            assets: Vec::new(),
            runtime: None,
            actor: None,
            classic,
            cuts,
            common,
            issues: 0,
            missing,
        };
        if let Some(id) = input.enemy_castle {
            let manifest = kbcs_data::motions::manifest(database, "jp", "enemy", id, 0)?;
            let body = &manifest["body"];
            let animation = body["animations"]
                .as_array()
                .into_iter()
                .flatten()
                .find(|v| v["key"] == "01")
                .or_else(|| body["animations"].as_array()?.first())
                .and_then(|v| v["key"].as_str())
                .unwrap_or("static");
            let image = body["image"]
                .as_str()
                .context("城型キャラの画像なし")?
                .to_owned();
            let model = crate::motion_pose::resource_model(&manifest, "body", animation)?;
            let texture = scene.textures.len() as i32;
            scene.sizes.push(stage_media::image_size(database, &image)?);
            scene.textures.push(Some(image));
            scene.actor = Some(Asset { model, texture });
        }
        Ok(scene)
    }
    fn prepare_effects(&mut self, database: &Database, input: &Input) -> Result<()> {
        if self.runtime.is_some() {
            return Ok(());
        }
        let mut id = input.background;
        let mut seen = BTreeSet::new();
        let data = loop {
            ensure!(seen.insert(id), "背景演出の参照が循環しています");
            let value = self.source["files"][format!("Data/bg{id:03}.json")]
                .as_str()
                .filter(|v| !v.trim().is_empty())
                .map(|text| serde_json::from_str::<Value>(text.trim_start_matches('\u{feff}')))
                .transpose()?
                .unwrap_or_else(|| json!({}));
            if let Some(next) = value["id"].as_i64() {
                id = next;
                continue;
            }
            break value;
        };
        let rows = stage_media::numeric_rows(
            self.source["files"]["Data/bg.csv"]
                .as_str()
                .context("背景原本なし")?
                .as_bytes(),
        )?;
        let cut = rows
            .iter()
            .map(|(_, r)| r)
            .find(|row| row.first().copied().flatten() == Some(id))
            .and_then(|row| row.get(13))
            .copied()
            .flatten()
            .context("背景演出の分割IDなし")?;
        let mut parameters = Vec::new();
        let mut lengths = Vec::new();
        let mut counts = Vec::new();
        for segment in data["data"].as_array().into_iter().flatten() {
            let mut group = Vec::new();
            let resolve = |name: String| -> Result<String> {
                ["ImageData/", "Image/", "Number/"]
                    .into_iter()
                    .map(|p| format!("{p}{name}"))
                    .find(|p| {
                        self.source["paths"]
                            .as_array()
                            .is_some_and(|paths| paths.iter().any(|v| v == p))
                    })
                    .with_context(|| format!("背景素材が未収録です: {name}"))
            };
            if segment["file"].is_object() {
                let file = &segment["file"];
                group.push((
                    resolve(file["image"].as_str().context("演出画像なし")?.into())?,
                    resolve(file["imgcut"].as_str().context("演出分割なし")?.into())?,
                    resolve(file["model"].as_str().context("演出モデルなし")?.into())?,
                    resolve(file["anime"].as_str().context("演出モーションなし")?.into())?,
                ));
            } else {
                let values = segment["model"]["values"]
                    .as_array()
                    .cloned()
                    .unwrap_or_else(|| vec![segment["model"]["value"].clone()]);
                for value in values {
                    let model = value.as_i64().context("演出モデルIDなし")?;
                    group.push((
                        resolve(format!("bg{id:03}.png"))?,
                        resolve(format!("bg{cut:02}.imgcut"))?,
                        resolve(format!("bg{cut:02}_{model:02}.mamodel"))?,
                        resolve(format!("bg{cut:02}_{model:02}.maanim"))?,
                    ));
                }
            }
            counts.push(group.len());
            parameters.push(segment.clone());
            for (image, cut, model, animation) in group {
                let files = &self.source["files"];
                let animation = if animation.ends_with(".mamodel") {
                    self.issues += 1;
                    None
                } else {
                    Some(files[&animation].as_str().context("演出モーション未収録")?)
                };
                let model = Model::parse(
                    files[&cut].as_str().context("演出分割未収録")?,
                    files[&model].as_str().context("演出モデル未収録")?,
                    animation,
                )
                .map_err(anyhow::Error::msg)?;
                lengths.push(model.length());
                let texture = self.textures.len() as i32;
                self.sizes.push(stage_media::image_size(database, &image)?);
                self.textures.push(Some(image));
                self.assets.push(Asset { model, texture });
            }
        }
        self.runtime = Some(
            render_effects::Runtime::new(
                input.width,
                self.classic,
                &parameters,
                &lengths,
                &counts,
                0x12345678,
            )
            .map_err(core)?,
        );
        Ok(())
    }
    pub fn draw(&mut self, database: &Database, input: &Input) -> Result<Frame<'_>> {
        let started = std::time::Instant::now();
        ensure!(
            (0..=1000000).contains(&input.frame),
            "表示フレームが範囲外です"
        );
        let cut = array::<4>(&self.background["cut"])?;
        let colors: Vec<_> = self.background["colors"]
            .as_array()
            .context("背景色なし")?
            .iter()
            .map(array::<3>)
            .collect::<Result<Vec<_>>>()?
            .into_iter()
            .flatten()
            .collect();
        let overlay = if self.background["overlay"].is_object() {
            let value = &self.background["overlay"];
            let start = array::<3>(&value["start"])?;
            let end = array::<3>(&value["end"])?;
            [
                start[0],
                start[1],
                start[2],
                end[0],
                end[1],
                end[2],
                value["alpha"].as_i64().context("重ね色の不透明度なし")? as i32,
            ]
        } else {
            [0, 0, 0, 0, 0, 0, -1]
        };
        let (layout, background_commands) = render::paint(
            &PaintInput {
                scene: SceneInput {
                    width: input.width,
                    center: input.center.unwrap_or(input.width),
                    zoom: input.zoom,
                    cut_height: cut[3],
                    castle: self.castle,
                    focus: input.focus,
                    viewport_width: input.viewport_width,
                    battle_rows: input.battle_rows,
                },
                cut,
                top: array(&self.background["top"]).unwrap_or_default(),
                colors: colors
                    .try_into()
                    .map_err(|_| anyhow::anyhow!("背景色の列数不正"))?,
                overlay,
                self_sizes: [
                    self.sizes[2][0],
                    self.sizes[2][1],
                    self.sizes[3][0],
                    self.sizes[3][1],
                    self.sizes[4][0],
                    self.sizes[4][1],
                ],
                show_enemy: i32::from(input.show_enemy && self.textures[1].is_some()),
                show_player: i32::from(input.show_player),
            },
            &mut self.paint_buffer,
        )
        .map_err(core)?;
        // 原本の描画上限ぶんは所有者が再利用し、有効な命令だけを返す。
        let mut commands = background_commands.to_vec();
        if input.show_enemy
            && let Some(actor) = &self.actor
        {
            let index = commands
                .iter()
                .position(|v| v.layer >= 2 && v.texture >= 2)
                .unwrap_or(commands.len());
            let mut actor_commands = Self::model_commands(
                actor,
                &layout,
                input.frame,
                true,
                true,
                None,
                320.,
                440.,
                0.,
                0..=0,
            )?;
            commands.splice(index..index, actor_commands.drain(..));
        }
        if input.show_effects {
            self.prepare_effects(database, input)?;
            let particles = self
                .runtime
                .as_mut()
                .context("演出状態なし")?
                .frame(input.frame)
                .map_err(core)?;
            let sizes = [
                self.sizes[5][0],
                self.sizes[5][1],
                self.sizes[6][0],
                self.sizes[6][1],
            ];
            for particle in particles {
                if particle.kind != 0 {
                    let command =
                        render_effects::weather(&layout, particle, &self.cuts, &self.common, sizes)
                            .map_err(core)?;
                    if command.count > 0 {
                        commands.push(command);
                    }
                    continue;
                }
                let asset = self
                    .assets
                    .get(particle.asset as usize)
                    .context("演出素材ID不正")?;
                {
                    let mut packets = Self::model_commands(
                        asset,
                        &layout,
                        particle.frame as i32,
                        false,
                        false,
                        Some([
                            particle.scale,
                            particle.sx,
                            particle.sy,
                            particle.angle,
                            particle.alpha,
                        ]),
                        particle.x,
                        particle.y,
                        particle.spacing,
                        particle.spacing_min..=particle.spacing_max,
                    )?;
                    for packet in &mut packets {
                        packet.layer = if particle.front != 0 { 3 } else { 1 };
                    }
                    commands.append(&mut packets);
                }
            }
        }
        commands.sort_by_key(|v| v.layer);
        let animated = self.classic >= 0 || !self.assets.is_empty() || self.actor.is_some();
        Ok(Frame {
            layout,
            commands,
            textures: &self.textures,
            animated,
            missing: &self.missing,
            issues: self.issues,
            frame: input.frame,
            core: "C++",
            ruleset: kbcs_bridge::ruleset_version(),
            compute_ms: started.elapsed().as_secs_f64() * 1000.,
        })
    }
    #[allow(clippy::too_many_arguments)]
    fn model_commands(
        asset: &Asset,
        layout: &render::Layout,
        frame: i32,
        repeat: bool,
        anchor: bool,
        root: Option<[f64; 5]>,
        x: f64,
        y: f64,
        spacing: f64,
        indexes: std::ops::RangeInclusive<i32>,
    ) -> Result<Vec<Command>> {
        if indexes.is_empty() {
            return Ok(Vec::new());
        }
        // 姿勢は間隔配置の全個体で同じ。世界座標変換だけを元の順番で繰り返す。
        let local = asset
            .model
            .pose_with_root(frame, repeat, anchor, 1, root)
            .map_err(core)?
            .into_iter()
            .map(|packet| {
                let cut = asset
                    .model
                    .cuts
                    .get(packet.cut as usize)
                    .context("描画分割ID不正")?;
                let mut command = Command {
                    texture: asset.texture,
                    layer: 2,
                    count: 4,
                    blend: packet.blend,
                    opacity: packet.opacity,
                    cut: [cut.x, cut.y, cut.width, cut.height],
                    ..Default::default()
                };
                for (target, source) in command.points.iter_mut().zip(packet.points) {
                    *target = f64::from(source);
                }
                Ok(command)
            })
            .collect::<Result<Vec<_>>>()?;
        let mut result = Vec::new();
        for index in indexes {
            for command in &local {
                result.push(render::instance(layout, command, x, y, spacing, index).map_err(core)?);
            }
        }
        Ok(result)
    }
}
