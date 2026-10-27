use crate::{actor, battle_screen, production, render, stage};
use std::ptr::NonNull;

#[repr(C)]
pub struct RewardRules {
    pub enabled: i32,
    pub mode: i32,
    pub count: i32,
    pub acquired: i32,
    pub radar: i32,
    pub chances: [i32; 10],
    pub material_enabled: i32,
    pub material: crate::materials::Input,
    pub win_type: i32,
    pub win_count: i32,
    pub win_sounds: [i32; 32],
    pub lose_type: i32,
    pub lose_count: i32,
    pub lose_sounds: [i32; 32],
    pub music: [i32; 2],
    pub music_threshold: i32,
    pub music_delay: i32,
    pub start_sound: i32,
    pub ex: crate::transition::Input,
    pub ex_count: i32,
    pub ex_choices: [crate::transition::Choice; 32],
}
impl Default for RewardRules {
    fn default() -> Self {
        Self {
            enabled: 0,
            mode: 0,
            count: 0,
            acquired: 0,
            radar: 0,
            chances: [0; 10],
            material_enabled: 0,
            material: crate::materials::Input {
                count: 0.,
                multiplier: 0.,
                miss: 0,
                weights: [0; 16],
            },
            win_type: 0,
            win_count: 0,
            win_sounds: [0; 32],
            lose_type: 0,
            lose_count: 0,
            lose_sounds: [0; 32],
            music: [-1; 2],
            music_threshold: 0,
            music_delay: 0,
            start_sound: -1,
            ex: Default::default(),
            ex_count: 0,
            ex_choices: [Default::default(); 32],
        }
    }
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Rewards {
    pub ready: i32,
    pub winner: i32,
    pub mark: i32,
    pub radar_blocked: i32,
    pub materials: [i32; 16],
    pub seed_before: u32,
    pub seed_after: u32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Music {
    pub id: i32,
    pub serial: i32,
    pub wait: i32,
    pub changed: i32,
    pub started: i32,
    pub delay: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct EndCamera {
    pub left: i32,
    pub zoom: i32,
    pub moving: i32,
    pub width: i32,
    pub rows: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Popup {
    pub index: i32,
    pub count: i32,
    pub phase: i32,
    pub scale_frame: i32,
    pub flash: i32,
    pub wait: i32,
}
#[repr(C)]
#[derive(serde::Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct PopupInput {
    pub viewport: i32,
    pub count: i32,
    pub widths: [i32; 8],
    pub scale_frame: i32,
    pub cut: [i32; 4],
    pub padding: [i32; 2],
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct PopupLayout {
    pub body: [i32; 4],
    pub text_y: i32,
    pub text_x: [i32; 8],
    pub parts: [[i32; 8]; 9],
    pub text_scale: [f32; 8],
}
pub fn popup_layout(input: &PopupInput) -> Result<PopupLayout, u32> {
    let mut out = PopupLayout::default();
    let code = unsafe { kbcs_core_battle_popup_layout(input, &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Ending {
    pub phase: i32,
    pub frame: i32,
    pub panel: i32,
    pub title: [i32; 3],
    pub bar_x: i32,
    pub number_x: i32,
    pub shade: i32,
    pub ready: i32,
    pub button: [i32; 4],
    pub visual_button: [i32; 4],
    pub label: [i32; 4],
    pub pressed: i32,
    pub guard: i32,
    pub action: i32,
    pub popup: Popup,
}

#[repr(C)]
#[derive(Clone, Copy, Default)]
pub struct Orb {
    pub effect: i32,
    pub mask: i32,
    pub values: [i32; 4],
}
#[repr(C)]
pub struct Profile {
    pub definition: actor::Definition,
    pub spawn: production::SpawnRequest,
    pub motion: actor::Motion,
    pub deployment_slot: i32,
    pub cost: i32,
    pub recharge: i32,
    pub recharge_plain: i32,
    pub money_base: i32,
    pub boundary: i32,
    pub death_body_frames: i32,
    pub death_soul_frames: i32,
    pub summon_mode: i32,
    pub raw_attack: [i32; 3],
    pub orb_count: i32,
    pub orbs: [Orb; 8],
    pub price: production::Cost,
}
#[repr(C)]
pub struct Config {
    pub environment: actor::Environment,
    pub screen: battle_screen::Config,
    pub state: battle_screen::State,
    pub clock: actor::Clock,
    pub hit: actor::HitContext,
    pub areas: actor::AreaRules,
    pub waves: actor::WaveRules,
    pub castle_hp: [i32; 2],
    pub enemy_max: i32,
    pub unit_max: i32,
    pub global_min: i32,
    pub global_max: i32,
    pub accounting_level: i32,
    pub death_surge_time: i32,
    pub death_surge_motion: [i32; 2],
    pub guard_enabled: i32,
    pub castle_offsets: [i32; 6],
    pub summon_position: i32,
    pub boss_frames: i32,
    pub castle_y_offset: i32,
    pub effect_clocks: [[i32; 3]; 64],
    pub price_rule: [i32; 4],
    pub rules: Rules,
    pub castle: actor::Actor,
    pub cannon: crate::cannon::Rules,
    pub seed: u32,
}
#[repr(C)]
#[derive(Clone, Copy, Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Rules {
    pub native_kind: i32,
    pub score_type: i32,
    pub time_limit: i32,
    pub bonus: [i32; 32],
    pub rarity_limits: [i32; 6],
    pub slot_rarity: [i32; 10],
    pub total_limit: i32,
    pub extra_rule: [i32; 3],
    pub production_kind: i32,
    pub production_periods: [i32; 6],
    pub recharge_fixed: i32,
    pub cost_chapter: i32,
    pub point: PointRules,
    pub unit_combo_count: i32,
    #[serde(serialize_with = "serialize_unit_combos")]
    pub unit_combos: [UnitCombo; 32],
}
// 未使用の固定長FFI枠を毎回JSONへ展開しない。
fn serialize_unit_combos<S: serde::Serializer>(
    values: &[UnitCombo; 32],
    serializer: S,
) -> Result<S::Ok, S::Error> {
    use serde::ser::SerializeSeq;
    let used = |value: &&UnitCombo| value.values.iter().any(|&v| v != 0);
    let mut sequence = serializer.serialize_seq(Some(values.iter().filter(used).count()))?;
    for value in values.iter().filter(used) {
        sequence.serialize_element(value)?;
    }
    sequence.end()
}
#[repr(C)]
#[derive(Clone, Copy, Default, serde::Serialize)]
pub struct UnitCombo {
    pub unit_id: i32,
    pub values: [i32; 32],
}
#[repr(C)]
#[derive(Clone, Copy, Default, serde::Serialize)]
#[serde(rename_all = "camelCase")]
pub struct PointRules {
    pub kind: i32,
    pub rate: i32,
    pub tier_count: i32,
    pub tiers: [[i32; 2]; 32],
    pub fever_count: i32,
    pub fever: [i32; 10],
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Points {
    pub score: i32,
    pub origin: i32,
    pub wait: i32,
    pub frame: i32,
    pub phase: i32,
    pub ending: i32,
    pub gauge: i32,
}
#[repr(C)]
#[derive(Clone, Copy, serde::Serialize)]
pub struct Extra {
    pub slot: i32,
    pub wait: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Outcome {
    pub mode: i32,
    pub timer: i32,
    pub elapsed: i32,
    pub score: i32,
    pub finished_frame: i32,
    pub reason: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Deployment {
    pub blocked: [i32; 10],
    pub active: [i32; 6],
    pub total: i32,
    pub warning: [i32; 2],
}
#[repr(C)]
#[derive(Clone, Copy, serde::Serialize)]
pub struct Visual {
    pub kind: i32,
    pub side: i32,
    pub slot: i32,
    pub phase: i32,
    pub frame: i32,
    pub x: i32,
    pub y: i32,
    pub layer: i32,
    pub root: [i32; 2],
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Hud {
    pub gauges: [[i32; 5]; 10],
    pub health: [[i32; 3]; 2],
    pub anchors: [[f64; 2]; 2],
    pub scale: f64,
    pub title: [i32; 2],
    pub summons: [[i32; 5]; 10],
}
#[repr(C)]
#[derive(Clone, Copy, serde::Serialize)]
pub struct Sound {
    pub frame: i32,
    pub id: i32,
}
#[repr(C)]
#[derive(Default, serde::Serialize)]
pub struct Computer {
    pub action: i32,
    pub selected: i32,
    pub pending_raw: i32,
    pub cannon_state: i32,
    pub cannon_wait: i32,
    pub candidates: [i32; 10],
    pub choices: [i32; 10],
}
#[repr(C)]
struct RawBattle {
    _private: [u8; 0],
}
pub type Actors = [[actor::Actor; actor::SLOTS]; 2];
pub type ProfileSlots = [[i32; actor::SLOTS]; 2];
pub struct Battle(NonNull<RawBattle>);
// 個別所有のC++状態。アクセスは&mut self/外側のMutexで直列化し、描画へ生ポインタを保持しない。
unsafe impl Send for Battle {}
#[repr(C)]
struct Atlases {
    cuts: [*const render::Cut; 2],
    counts: [i32; 2],
    textures: [i32; 2],
}
impl Battle {
    pub fn points(&self) -> Result<Points, u32> {
        let mut out = Points::default();
        let code = unsafe { kbcs_core_battle_points(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn extras(&self) -> Result<Vec<Extra>, u32> {
        let mut out = std::ptr::null();
        let mut count = 0;
        let code = unsafe { kbcs_core_battle_extras(self.0.as_ptr(), &mut out, &mut count) };
        if code != 0 {
            return Err(code);
        }
        Ok(if count == 0 {
            Vec::new()
        } else {
            unsafe { std::slice::from_raw_parts(out, count as usize) }.to_vec()
        })
    }
    pub fn outcome(&self) -> Result<Outcome, u32> {
        let mut out = Outcome::default();
        let code = unsafe { kbcs_core_battle_result(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn reward_rules(&mut self, input: &RewardRules) -> Result<(), u32> {
        let code = unsafe { kbcs_core_battle_reward_rules(self.0.as_ptr(), input) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn rewards(&self) -> Result<Rewards, u32> {
        let mut out = Rewards::default();
        let code = unsafe { kbcs_core_battle_rewards(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn music(&self) -> Result<Music, u32> {
        let mut out = Music::default();
        let code = unsafe { kbcs_core_battle_music(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn end_camera(&self) -> Result<EndCamera, u32> {
        let mut out = EndCamera::default();
        let code = unsafe { kbcs_core_battle_end_camera(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn ex(&self) -> Result<crate::transition::Output, u32> {
        let mut out = crate::transition::Output::default();
        let code = unsafe { kbcs_core_battle_ex(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn ending(&self) -> Result<Ending, u32> {
        let mut out = Ending::default();
        let code = unsafe { kbcs_core_battle_ending(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn notifications(&mut self, count: i32) -> Result<(), u32> {
        let code = unsafe { kbcs_core_battle_notifications(self.0.as_ptr(), count) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn deployment(&self) -> Result<Deployment, u32> {
        let mut out = Deployment::default();
        let code = unsafe { kbcs_core_battle_deployment(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn prices(&self) -> Result<[i32; 10], u32> {
        let mut out = [0; 10];
        let code = unsafe { kbcs_core_battle_prices(self.0.as_ptr(), out.as_mut_ptr()) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn computer(&self) -> Result<Computer, u32> {
        let mut out = Computer::default();
        let code = unsafe { kbcs_core_battle_computer_state(self.0.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn camera(&mut self, layout: &render::Layout) -> Result<(), u32> {
        let code = unsafe { kbcs_core_battle_camera(self.0.as_ptr(), layout) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn sniper_status(&self) -> Result<[i32; 5], u32> {
        let mut out = [0; 5];
        let code = unsafe { kbcs_core_battle_sniper_status(self.0.as_ptr(), out.as_mut_ptr()) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn cannon_draw(
        &self,
        layout: &render::Layout,
        cuts: &[render::Cut],
        texture: i32,
    ) -> Result<Vec<render::Command>, u32> {
        let paint = Atlases {
            cuts: [cuts.as_ptr(), std::ptr::null()],
            counts: [cuts.len() as i32, 0],
            textures: [texture, -1],
        };
        let mut out = vec![render::Command::default(); 256];
        let mut count = 0;
        let code = unsafe {
            kbcs_core_battle_cannon_draw(
                self.0.as_ptr(),
                layout,
                &paint,
                out.as_mut_ptr(),
                out.len() as i32,
                &mut count,
            )
        };
        if code != 0 {
            return Err(code);
        }
        out.truncate(count as usize);
        Ok(out)
    }
    pub fn hit_draw(
        &self,
        layout: &render::Layout,
        cuts: &[render::Cut],
        texture: i32,
    ) -> Result<Vec<render::Command>, u32> {
        let paint = Atlases {
            cuts: [cuts.as_ptr(), std::ptr::null()],
            counts: [cuts.len() as i32, 0],
            textures: [texture, -1],
        };
        let mut out = vec![render::Command::default(); 224];
        let mut count = 0;
        let code = unsafe {
            kbcs_core_battle_hit_draw(
                self.0.as_ptr(),
                layout,
                &paint,
                out.as_mut_ptr(),
                out.len() as i32,
                &mut count,
            )
        };
        if code != 0 {
            return Err(code);
        }
        out.truncate(count as usize);
        Ok(out)
    }
    pub fn sniper_draw(
        &self,
        layout: &render::Layout,
        cuts: [&[render::Cut]; 2],
        textures: [i32; 2],
    ) -> Result<Vec<render::Command>, u32> {
        let paint = Atlases {
            cuts: cuts.map(|c| c.as_ptr()),
            counts: cuts.map(|c| c.len() as i32),
            textures,
        };
        let mut out = vec![render::Command::default(); 164];
        let mut count = 0;
        let code = unsafe {
            kbcs_core_battle_sniper_draw(
                self.0.as_ptr(),
                layout,
                &paint,
                out.as_mut_ptr(),
                out.len() as i32,
                &mut count,
            )
        };
        if code != 0 {
            return Err(code);
        }
        out.truncate(count as usize);
        Ok(out)
    }

    pub fn top_draw(
        &self,
        cuts: &[render::Cut],
        fever: &[render::Cut],
        textures: [i32; 2],
        title: Option<(render::Cut, i32)>,
    ) -> Result<Vec<render::Command>, u32> {
        let mut out = vec![render::Command::default(); 64];
        let mut count = 0;
        let code = unsafe {
            kbcs_core_battle_top_draw(
                self.0.as_ptr(),
                cuts.as_ptr(),
                cuts.len() as i32,
                fever.as_ptr(),
                fever.len() as i32,
                title.as_ref().map_or(std::ptr::null(), |v| &v.0),
                out.as_mut_ptr(),
                out.len() as i32,
                &mut count,
            )
        };
        if code != 0 {
            return Err(code);
        }
        out.truncate(count as usize);
        for command in &mut out {
            command.texture = if command.texture == 2 {
                title.as_ref().ok_or(1u32)?.1
            } else {
                textures[command.texture as usize]
            };
        }
        let mut overlay = [render::Command::default(), render::Command::default()];
        let code = unsafe {
            kbcs_core_battle_overlay(self.0.as_ptr(), overlay.as_mut_ptr(), 2, &mut count)
        };
        if code != 0 {
            return Err(code);
        }
        out.extend(overlay.into_iter().take(count as usize));
        Ok(out)
    }

    pub fn hud(&self, layout: &render::Layout, point: [i32; 2]) -> Result<Hud, u32> {
        let mut out = Hud::default();
        let code =
            unsafe { kbcs_core_battle_hud(self.0.as_ptr(), layout, point.as_ptr(), &mut out) };
        if code == 0 { Ok(out) } else { Err(code) }
    }
    pub fn new(config: &Config, profiles: &[Profile], rows: &[stage::Row]) -> Result<Self, u32> {
        if profiles.len() > 4096 || rows.len() > 4096 {
            return Err(1);
        }
        let mut raw = std::ptr::null_mut();
        let code = unsafe {
            kbcs_core_battle_create(
                config,
                profiles.as_ptr(),
                profiles.len() as i32,
                rows.as_ptr(),
                rows.len() as i32,
                &mut raw,
            )
        };
        if code != 0 {
            return Err(code);
        }
        NonNull::new(raw).map(Self).ok_or(3)
    }
    pub fn viewport(&mut self, width: i32) -> Result<(), u32> {
        let code = unsafe { kbcs_core_battle_viewport(self.0.as_ptr(), width) };
        if code == 0 { Ok(()) } else { Err(code) }
    }
    pub fn advance(&mut self, input: &battle_screen::Input) -> Result<battle_screen::Frame, u32> {
        let mut state = battle_screen::State::default();
        let mut layout = battle_screen::Layout::default();
        let code =
            unsafe { kbcs_core_battle_advance(self.0.as_ptr(), input, &mut state, &mut layout) };
        if code != 0 {
            Err(code)
        } else {
            Ok(battle_screen::Frame { state, layout })
        }
    }
    pub fn actors(&self) -> Result<(&Actors, &ProfileSlots), u32> {
        let mut actors = std::ptr::null();
        let mut profiles = std::ptr::null();
        let code = unsafe { kbcs_core_battle_actors(self.0.as_ptr(), &mut actors, &mut profiles) };
        if code != 0 {
            return Err(code);
        }
        if actors.is_null() || profiles.is_null() {
            return Err(3);
        }
        Ok(unsafe { (&*actors.cast(), &*profiles.cast()) })
    }
    pub fn visuals(&mut self) -> Result<&[Visual], u32> {
        let mut pointer = std::ptr::null();
        let mut count = 0;
        let code = unsafe { kbcs_core_battle_visuals(self.0.as_ptr(), &mut pointer, &mut count) };
        if code != 0 {
            return Err(code);
        }
        if count == 0 {
            return Ok(&[]);
        }
        if pointer.is_null() || count < 0 {
            return Err(3);
        }
        Ok(unsafe { std::slice::from_raw_parts(pointer, count as usize) })
    }
    pub fn sounds(&self) -> Result<&[Sound], u32> {
        let mut pointer = std::ptr::null();
        let mut count = 0;
        let code = unsafe { kbcs_core_battle_sounds(self.0.as_ptr(), &mut pointer, &mut count) };
        if code != 0 {
            return Err(code);
        }
        if count == 0 {
            return Ok(&[]);
        }
        if pointer.is_null() || count < 0 {
            return Err(3);
        }
        Ok(unsafe { std::slice::from_raw_parts(pointer, count as usize) })
    }
    pub fn diagnostic(&self) -> [i32; 4] {
        let mut out = [0; 4];
        unsafe {
            kbcs_core_battle_error(self.0.as_ptr(), out.as_mut_ptr());
        }
        out
    }
    pub fn production(&self) -> Result<(production::State, u32), u32> {
        let mut state = production::State::default();
        let mut seed = 0;
        let code = unsafe { kbcs_core_battle_production(self.0.as_ptr(), &mut state, &mut seed) };
        if code != 0 {
            Err(code)
        } else {
            Ok((state, seed))
        }
    }
}
impl Drop for Battle {
    fn drop(&mut self) {
        unsafe { kbcs_core_battle_destroy(self.0.as_ptr()) };
    }
}
unsafe extern "C" {
    fn kbcs_core_battle_notifications(battle: *mut RawBattle, count: i32) -> u32;
    fn kbcs_core_battle_popup_layout(input: *const PopupInput, out: *mut PopupLayout) -> u32;
    fn kbcs_core_battle_points(battle: *const RawBattle, out: *mut Points) -> u32;
    fn kbcs_core_battle_extras(
        battle: *const RawBattle,
        out: *mut *const Extra,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_result(battle: *const RawBattle, out: *mut Outcome) -> u32;
    fn kbcs_core_battle_reward_rules(battle: *mut RawBattle, input: *const RewardRules) -> u32;
    fn kbcs_core_battle_rewards(battle: *const RawBattle, out: *mut Rewards) -> u32;
    fn kbcs_core_battle_music(battle: *const RawBattle, out: *mut Music) -> u32;
    fn kbcs_core_battle_end_camera(battle: *const RawBattle, out: *mut EndCamera) -> u32;
    fn kbcs_core_battle_ex(battle: *const RawBattle, out: *mut crate::transition::Output) -> u32;
    fn kbcs_core_battle_ending(battle: *const RawBattle, out: *mut Ending) -> u32;
    fn kbcs_core_battle_deployment(battle: *const RawBattle, out: *mut Deployment) -> u32;
    fn kbcs_core_battle_prices(battle: *const RawBattle, out: *mut i32) -> u32;
    fn kbcs_core_battle_computer_state(battle: *const RawBattle, out: *mut Computer) -> u32;
    fn kbcs_core_battle_hit_draw(
        battle: *const RawBattle,
        layout: *const render::Layout,
        paint: *const Atlases,
        out: *mut render::Command,
        capacity: i32,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_sounds(
        battle: *const RawBattle,
        out: *mut *const Sound,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_cannon_draw(
        battle: *const RawBattle,
        layout: *const render::Layout,
        paint: *const Atlases,
        out: *mut render::Command,
        capacity: i32,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_camera(battle: *mut RawBattle, layout: *const render::Layout) -> u32;
    fn kbcs_core_battle_sniper_status(battle: *const RawBattle, out: *mut i32) -> u32;
    fn kbcs_core_battle_sniper_draw(
        battle: *const RawBattle,
        layout: *const render::Layout,
        paint: *const Atlases,
        out: *mut render::Command,
        capacity: i32,
        count: *mut i32,
    ) -> u32;

    fn kbcs_core_battle_top_draw(
        battle: *const RawBattle,
        cuts: *const render::Cut,
        count: i32,
        fever: *const render::Cut,
        fever_count: i32,
        title: *const render::Cut,
        out: *mut render::Command,
        capacity: i32,
        written: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_overlay(
        battle: *const RawBattle,
        out: *mut render::Command,
        capacity: i32,
        written: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_hud(
        battle: *const RawBattle,
        layout: *const render::Layout,
        point: *const i32,
        out: *mut Hud,
    ) -> u32;
    fn kbcs_core_battle_visuals(
        battle: *mut RawBattle,
        out: *mut *const Visual,
        count: *mut i32,
    ) -> u32;
    fn kbcs_core_battle_error(battle: *const RawBattle, out: *mut i32) -> u32;
    fn kbcs_core_battle_viewport(battle: *mut RawBattle, width: i32) -> u32;
    fn kbcs_core_battle_create(
        config: *const Config,
        profiles: *const Profile,
        count: i32,
        rows: *const stage::Row,
        row_count: i32,
        out: *mut *mut RawBattle,
    ) -> u32;
    fn kbcs_core_battle_destroy(battle: *mut RawBattle);
    fn kbcs_core_battle_advance(
        battle: *mut RawBattle,
        input: *const battle_screen::Input,
        state: *mut battle_screen::State,
        view: *mut battle_screen::Layout,
    ) -> u32;
    fn kbcs_core_battle_actors(
        battle: *const RawBattle,
        actors: *mut *const actor::Actor,
        profiles: *mut *const i32,
    ) -> u32;
    fn kbcs_core_battle_production(
        battle: *const RawBattle,
        state: *mut production::State,
        seed: *mut u32,
    ) -> u32;
}
