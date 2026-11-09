use crate::{formations::Member, model::Form, store::Database, talents::Talent};
use anyhow::{Context, Result, ensure};
use serde::{Deserialize, Serialize};
use std::{
    collections::{BTreeMap, BTreeSet},
    sync::OnceLock,
};

pub const FIRST_ID: u32 = 30_000;
pub const EFFECT_COUNT: u32 = 26;
const SLOT_PATH: &str = "Data/equipmentslot.csv";
const TARGET_COLUMNS: [usize; 12] = [10, 16, 17, 18, 20, 21, 22, 78, 19, 54, 76, 96];
pub const TARGETS: [&str; 12] = [
    "red", "floating", "black", "metal", "angel", "alien", "zombie", "relic", "white", "witch",
    "eva", "aku",
];

#[derive(Clone, Copy)]
struct SlotCode {
    count: usize,
    conditions: [i64; 2],
}

#[derive(Deserialize)]
struct SlotDefinition {
    version: String,
    entries: BTreeMap<u32, EmbeddedSlot>,
}

#[derive(Deserialize)]
struct EmbeddedSlot {
    count: usize,
    conditions: Vec<Option<i64>>,
}

fn slot_code(count: usize, conditions: &[Option<i64>]) -> Result<SlotCode> {
    ensure!(
        count <= 2 && conditions.len() <= 2,
        "本能玉の枠数が不正です"
    );
    let mut codes = [0; 2];
    for (code, value) in codes.iter_mut().zip(conditions) {
        *code = value.unwrap_or(0);
    }
    Ok(SlotCode {
        count,
        conditions: codes,
    })
}

fn embedded_slots(version: &str) -> Result<&'static BTreeMap<u32, EmbeddedSlot>> {
    static DEFINITION: OnceLock<SlotDefinition> = OnceLock::new();
    let data = DEFINITION.get_or_init(|| {
        serde_json::from_str(include_str!("../resources/unit-equipment-slots.json"))
            .expect("組込みの本能玉スロット定義が不正です")
    });
    ensure!(
        data.version == version,
        "本能玉スロット定義と編成の版が異なります"
    );
    Ok(&data.entries)
}

fn slots(database: &Database) -> Result<BTreeMap<u32, SlotCode>> {
    if database.stored_source(SLOT_PATH)?.is_some()
        || database.connection.query_row(
            "SELECT EXISTS(SELECT 1 FROM asset_reference WHERE path=?)",
            [SLOT_PATH],
            |row| row.get::<_, bool>(0),
        )?
    {
        let mut entries = BTreeMap::new();
        for (_, row) in crate::model::numeric_rows(&database.source(SLOT_PATH)?.3)? {
            let id = u32::try_from(crate::model::required(&row, 0)?)?;
            let count = usize::try_from(crate::model::required(&row, 1)?)?;
            ensure!(
                entries.insert(id, slot_code(count, &row[2..])?).is_none(),
                "本能玉枠のキャラIDが重複しています"
            );
        }
        return Ok(entries);
    }
    embedded_slots(&database.metadata()?["version"])?
        .iter()
        .map(|(&id, slot)| Ok((id, slot_code(slot.count, &slot.conditions)?)))
        .collect()
}

pub fn capacities(database: &Database) -> Result<BTreeMap<u32, usize>> {
    Ok(slots(database)?
        .into_iter()
        .map(|(id, slot)| (id, slot.count))
        .collect())
}

pub fn capacity(version: &str, unit: u32) -> Result<usize> {
    Ok(embedded_slots(version)?
        .get(&unit)
        .map_or(0, |slot| slot.count))
}

#[derive(Debug, Deserialize, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Orb {
    #[serde(rename = "gradeID")]
    pub grade: u32,
    pub content: u32,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub attribute: Option<usize>,
    pub value: Vec<i32>,
}

impl Orb {
    pub fn supported(&self) -> bool {
        self.content < EFFECT_COUNT && self.grade <= 4
    }
}

#[derive(Deserialize)]
struct EquipmentList {
    #[serde(rename = "ID")]
    items: Vec<Orb>,
}

pub struct Catalog {
    items: Vec<Orb>,
    masks: Vec<u32>,
    slots: BTreeMap<u32, SlotCode>,
}

impl Catalog {
    pub fn read(database: &Database) -> Result<Self> {
        let mut catalog = Self::parse(
            &database.source("Data/equipmentlist.json")?.3,
            &database.source("Data/equipment_attribute.csv")?.3,
        )?;
        catalog.slots = slots(database)?;
        Ok(catalog)
    }

    pub fn parse(list: &[u8], attributes: &[u8]) -> Result<Self> {
        let list = list.strip_prefix(b"\xef\xbb\xbf").unwrap_or(list);
        let EquipmentList { items } = serde_json::from_slice(list)?;
        let mut masks = Vec::new();
        for (_, row) in crate::model::numeric_rows(attributes)? {
            ensure!(
                (12..=13).contains(&row.len()),
                "本能玉の属性定義の列数が不正です"
            );
            let mut mask = 0;
            for (bit, enabled) in row[..12].iter().enumerate() {
                match enabled {
                    Some(1) => mask |= 1 << bit,
                    Some(0) => {}
                    _ => anyhow::bail!("本能玉の属性ビットが不正です"),
                }
            }
            masks.push(mask);
        }
        let mut keys = BTreeSet::new();
        for item in &items {
            ensure!(
                item.attribute.is_none_or(|index| index < masks.len()),
                "本能玉の属性が範囲外です"
            );
            ensure!(
                keys.insert((item.content, item.attribute, item.grade)),
                "本能玉の種類と等級が重複しています"
            );
            if !item.supported() {
                continue;
            }
            let fields = if matches!(item.content, 2 | 9 | 10 | 13 | 16) {
                2
            } else {
                1
            };
            ensure!(item.value.len() == fields, "本能玉の効果値の列数が不正です");
            if item.content < 5 {
                ensure!(
                    item.attribute
                        .and_then(|a| masks.get(a))
                        .is_some_and(|&mask| mask != 0),
                    "本能玉の属性が範囲外です"
                );
            } else {
                ensure!(
                    item.attribute.is_none(),
                    "属性を持たない本能玉に属性が指定されています"
                );
            }
        }
        Ok(Self {
            items,
            masks,
            slots: BTreeMap::new(),
        })
    }

    pub fn items(&self) -> &[Orb] {
        &self.items
    }

    pub fn get(&self, id: u32) -> Result<&Orb> {
        id.checked_sub(FIRST_ID)
            .and_then(|index| self.items.get(index as usize))
            .with_context(|| format!("本能玉ID {id} が未収録です"))
    }

    pub fn mask(&self, orb: &Orb) -> u32 {
        orb.attribute.map_or(0, |index| self.masks[index])
    }

    pub fn capacity(&self, unit: u32) -> usize {
        self.slots.get(&unit).map_or(0, |slot| slot.count)
    }

    pub fn eligibility(
        &self,
        member: &Member,
        form: &Form,
        talents: &[Talent],
    ) -> Result<Eligibility> {
        let column = |index| form.raw.get(index).copied().flatten().unwrap_or(0);
        let mut targets = 0;
        for (bit, index) in TARGET_COLUMNS.into_iter().enumerate() {
            if column(index) != 0 {
                targets |= 1 << bit;
            }
        }
        let mut enhanced = [column(23) != 0, column(30) != 0, column(29) != 0];
        let mut surge_immune = column(91) != 0;
        let mut recharge = column(118);
        for talent in talents {
            let level = member.active_talent_level(form, talent);
            if level == 0 {
                continue;
            }
            let values = talent.values.get(level - 1).context("本能レベル範囲外")?;
            match talent.id {
                5 => enhanced[0] = true,
                7 => enhanced[1] = true,
                6 => enhanced[2] = true,
                55 => surge_immune = true,
                72 => recharge += values[0],
                _ => {}
            }
            targets |= target_mask(talent);
        }
        let form_locked = form.index < 2;
        let slot_states = self
            .slots
            .get(&member.unit_id)
            .into_iter()
            .flat_map(|slot| {
                slot.conditions[..slot.count].iter().map(|&code| {
                    let minimum_level = if code == 1 { 60 } else { 0 };
                    SlotState {
                        unlocked: matches!(code, 0 | 1)
                            && !form_locked
                            && member.total_level() >= minimum_level,
                        minimum_level,
                        unsupported_condition: (!matches!(code, 0 | 1)).then_some(code),
                    }
                })
            })
            .collect();
        Ok(Eligibility {
            form_locked,
            targets,
            enhanced,
            surge_immune,
            recharge,
            slots: slot_states,
        })
    }

    pub fn selection(&self, eligibility: &Eligibility) -> Selection {
        let allowed = self
            .items
            .iter()
            .enumerate()
            .filter(|(_, orb)| eligibility.allows(orb, self.mask(orb)))
            .map(|(index, _)| FIRST_ID + index as u32)
            .collect();
        Selection {
            allowed,
            form_locked: eligibility.form_locked,
            slots: eligibility.slots.clone(),
        }
    }
}

pub fn target_mask(talent: &Talent) -> u32 {
    TARGETS
        .iter()
        .enumerate()
        .filter(|&(_, key)| talent.targets.iter().any(|target| target == key))
        .fold(0, |mask, (bit, _)| mask | (1 << bit))
}

#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct SlotState {
    pub unlocked: bool,
    pub minimum_level: u32,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub unsupported_condition: Option<i64>,
}

pub struct Eligibility {
    form_locked: bool,
    targets: u32,
    enhanced: [bool; 3],
    surge_immune: bool,
    recharge: i64,
    pub slots: Vec<SlotState>,
}

impl Eligibility {
    // 0065f258の能力と属性を、編成で選んだ実効形態について評価する。
    pub fn allows(&self, orb: &Orb, mask: u32) -> bool {
        orb.supported()
            && !self.form_locked
            && match orb.content {
                2..=4 => self.enhanced[(orb.content - 2) as usize] && self.targets & mask != 0,
                17 => !self.surge_immune,
                19 => self.recharge <= 0,
                _ => true,
            }
    }

    pub fn active(&self, slot: usize, orb: &Orb, mask: u32) -> bool {
        self.slots.get(slot).is_some_and(|state| state.unlocked) && self.allows(orb, mask)
    }
}

#[derive(Serialize)]
#[serde(rename_all = "camelCase")]
pub struct Selection {
    allowed: Vec<u32>,
    form_locked: bool,
    slots: Vec<SlotState>,
}

#[cfg(test)]
mod tests {
    use super::*;

    fn catalog_fixture() -> (Catalog, serde_json::Value) {
        let fixture: serde_json::Value = serde_json::from_str(
            include_str!("../../../native/kbcs-core/tests/equipment-vectors.json")
                .trim_start_matches('\u{feff}'),
        )
        .unwrap();
        let catalog = Catalog::parse(
            &serde_json::to_vec(&fixture["list"]).unwrap(),
            fixture["attributes"].as_str().unwrap().as_bytes(),
        )
        .unwrap();
        (catalog, fixture)
    }

    #[test]
    fn reads_all_original_ids_and_attributes() {
        let (catalog, fixture) = catalog_fixture();
        assert_eq!(catalog.items().len(), 310);
        let effects: BTreeSet<_> = catalog.items().iter().map(|orb| orb.content).collect();
        assert_eq!(effects, (0..26).collect());
        for (index, item) in fixture["list"]["ID"].as_array().unwrap().iter().enumerate() {
            assert_eq!(
                serde_json::to_value(catalog.get(FIRST_ID + index as u32).unwrap()).unwrap(),
                *item
            );
        }
        assert!(catalog.get(29999).is_err() && catalog.get(30310).is_err());
        assert_eq!(
            catalog.masks,
            (0..12).map(|bit| 1 << bit).chain([0]).collect::<Vec<_>>()
        );
        assert!(
            catalog
                .items()
                .iter()
                .filter(|orb| orb.attribute == Some(3))
                .all(|orb| orb.content == 1)
        );
    }

    #[test]
    fn candidates_follow_ability_form_talent_and_individual_slot() {
        let (mut catalog, _) = catalog_fixture();
        for id in [32, 42] {
            let slot = &embedded_slots("15.7.2").unwrap()[&id];
            catalog
                .slots
                .insert(id, slot_code(slot.count, &slot.conditions).unwrap());
        }
        let mut member = Member {
            unit_id: 42,
            form: 2,
            level: 59,
            plus: 0,
            talents: BTreeMap::new(),
            orbs: vec![None, Some(30074)],
        };
        let mut form = Form {
            region: "jp".into(),
            unit_id: 42,
            index: 2,
            name: String::new(),
            description: String::new(),
            rarity: 4,
            max_level: 60,
            plus_level: 70,
            is_spirit: false,
            icon_path: None,
            hp: 100,
            speed: 0,
            range: 0,
            cost: 0,
            respawn_raw: 0,
            knockbacks: 1,
            interval_raw: 0,
            area: false,
            attack_cycle: None,
            animation_length: None,
            attacks: vec![],
            properties: vec![],
            raw: vec![None; 119],
            raw_cells: vec![],
            growth: vec![],
            source_path: String::new(),
            name_source: String::new(),
            motion_path: String::new(),
        };
        let allowed = |member: &Member, form: &Form, talents: &[Talent], effect, attribute| {
            let orb = catalog
                .items()
                .iter()
                .find(|o| o.content == effect && o.attribute == attribute)
                .unwrap();
            catalog
                .eligibility(member, form, talents)
                .unwrap()
                .allows(orb, catalog.mask(orb))
        };
        form.raw[10] = Some(1);
        assert!(!allowed(&member, &form, &[], 3, Some(0)));
        assert!(allowed(&member, &form, &[], 0, Some(5)));
        for (column, effect) in [(23, 2), (30, 3), (29, 4)] {
            form.raw[column] = Some(1);
            assert!(allowed(&member, &form, &[], effect, Some(0)));
            assert!(!allowed(&member, &form, &[], effect, Some(5)));
        }
        form.raw[20] = Some(1);
        assert!(allowed(&member, &form, &[], 3, Some(4)));
        assert!(!allowed(&member, &form, &[], 3, Some(5)));
        assert!(!catalog.eligibility(&member, &form, &[]).unwrap().slots[1].unlocked);
        let talents = [Talent {
            combo_unlock: None,
            support: crate::support::Support::Supported,
            raw: None,
            id: 7,
            index: 0,
            name: String::new(),
            max_level: 1,
            description: String::new(),
            limit: 1,
            costs: vec![1],
            effect: crate::talents::Effect {
                kind: "ability".into(),
                key: "massive".into(),
                label: None,
                fields: None,
            },
            values: vec![[1, 0, 0, 0]],
            targets: vec!["alien".into()],
        }];
        member.talents.insert(0, 1);
        form.raw[30] = None;
        assert!(!allowed(&member, &form, &talents, 3, Some(5)));
        member.plus = 1;
        assert!(allowed(&member, &form, &talents, 3, Some(5)));
        assert!(catalog.eligibility(&member, &form, &talents).unwrap().slots[1].unlocked);
        assert_eq!(member.orbs, vec![None, Some(30074)]);
        member.talents.clear();
        assert!(!allowed(&member, &form, &talents, 3, Some(0)));
        form.index = 3;
        form.raw[30] = Some(1);
        assert!(allowed(&member, &form, &talents, 3, Some(0)));
        form.raw[91] = Some(1);
        form.raw[118] = Some(10);
        assert!(!allowed(&member, &form, &[], 17, None));
        assert!(!allowed(&member, &form, &[], 19, None));
        assert!(allowed(&member, &form, &[], 10, None));
        member.unit_id = 32;
        assert_eq!(
            catalog
                .eligibility(&member, &form, &[])
                .unwrap()
                .slots
                .len(),
            1
        );
        form.index = 1;
        assert!(!catalog.eligibility(&member, &form, &[]).unwrap().slots[0].unlocked);
    }
}
