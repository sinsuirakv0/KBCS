use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ComboDefinition {
    pub units: [i32; 5],
    pub forms: [i32; 5],
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ComboSelection {
    pub team: [i32; 10],
    pub forms: [i32; 10],
    pub locked: [i32; 10],
    pub selected: i32,
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct ComboPlan {
    pub first: [i32; 5],
    pub slots: [i32; 10],
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct ComboIntro {
    pub index: i32,
    pub age: i32,
    pub blink: i32,
    pub band: [i32; 4],
    pub text_x: i32,
    pub text_y: [i32; 3],
    pub skip: [i32; 2],
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct ComboRow {
    pub panel: [i32; 4],
    pub name: [i32; 2],
    pub effect: [i32; 2],
    pub group: [i32; 2],
    pub icons: [[i32; 4]; 5],
}
#[repr(C)]
#[derive(Default, Serialize)]
pub struct ComboDialog {
    pub window: [i32; 4],
    pub confirm: [i32; 4],
    pub close: [i32; 4],
}
#[repr(C)]
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct UnitInfoInput {
    pub center: i32,
    pub y: i32,
    pub form: i32,
    pub attributes: [i32; 10],
    #[serde(deserialize_with = "deserialize_flags")]
    pub abilities: [i32; 88],
    #[serde(deserialize_with = "deserialize_flags")]
    pub talents: [i32; 88],
    pub new_attributes: [i32; 10],
    pub orbs: i32,
}
#[repr(C)]
#[derive(Serialize)]
pub struct UnitInfoLayout {
    pub count: i32,
    #[serde(serialize_with = "serialize_sprites")]
    pub sprites: [[i32; 4]; 192],
    pub orb_count: i32,
    pub orbs: [[i32; 2]; 8],
}
fn deserialize_flags<'de, D: serde::Deserializer<'de>>(
    deserializer: D,
) -> Result<[i32; 88], D::Error> {
    Vec::<i32>::deserialize(deserializer)?
        .try_into()
        .map_err(|_| serde::de::Error::custom("特性フラグは88件必要です"))
}
fn serialize_sprites<S: serde::Serializer>(
    sprites: &[[i32; 4]; 192],
    serializer: S,
) -> Result<S::Ok, S::Error> {
    sprites.as_slice().serialize(serializer)
}
unsafe extern "C" {
    fn kbcs_core_combo_plan(
        combos: *const ComboDefinition,
        count: i32,
        selection: *const ComboSelection,
        output: *mut ComboPlan,
    ) -> u32;
    fn kbcs_core_combo_intro(
        frame: i32,
        width: i32,
        count: i32,
        groups: *const i32,
        output: *mut ComboIntro,
    ) -> u32;
    fn kbcs_core_combo_row(width: i32, row: i32, grouped: i32, output: *mut ComboRow) -> u32;
    fn kbcs_core_combo_dialog(width: i32, phase: i32, output: *mut ComboDialog) -> u32;
    fn kbcs_core_unit_info(input: *const UnitInfoInput, output: *mut UnitInfoLayout) -> u32;
}
pub fn combo_plan(
    combos: &[ComboDefinition],
    selection: &ComboSelection,
) -> Result<ComboPlan, u32> {
    let count = i32::try_from(combos.len()).map_err(|_| 1u32)?;
    let mut out = ComboPlan::default();
    let code = unsafe { kbcs_core_combo_plan(combos.as_ptr(), count, selection, &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}
pub fn combo_intro(frame: i32, width: i32, groups: &[i32]) -> Result<ComboIntro, u32> {
    let count = i32::try_from(groups.len()).map_err(|_| 1u32)?;
    let mut out = ComboIntro::default();
    let code = unsafe { kbcs_core_combo_intro(frame, width, count, groups.as_ptr(), &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}
pub fn combo_row(width: i32, row: i32, grouped: bool) -> Result<ComboRow, u32> {
    let mut out = ComboRow::default();
    let code = unsafe { kbcs_core_combo_row(width, row, i32::from(grouped), &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}
pub fn unit_info(input: &UnitInfoInput) -> Result<UnitInfoLayout, u32> {
    let mut out = UnitInfoLayout {
        count: 0,
        sprites: [[0; 4]; 192],
        orb_count: 0,
        orbs: [[0; 2]; 8],
    };
    let code = unsafe { kbcs_core_unit_info(input, &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}
pub fn combo_dialog(width: i32, phase: i32) -> Result<ComboDialog, u32> {
    let mut out = ComboDialog::default();
    let code = unsafe { kbcs_core_combo_dialog(width, phase, &mut out) };
    if code == 0 { Ok(out) } else { Err(code) }
}

#[cfg(test)]
mod tests {
    use super::*;
    use serde_json::{Value, json};
    fn fixture(value: &str) -> Value {
        serde_json::from_str(value.trim_start_matches('\u{feff}')).unwrap()
    }
    #[test]
    fn native_combo_and_information_vectors() {
        let plan = fixture(include_str!(
            "../../../native/kbcs-core/tests/formation-combo-vectors.json"
        ));
        for row in plan["cases"].as_array().unwrap() {
            let definitions: Vec<ComboDefinition> =
                serde_json::from_value(row["combos"].clone()).unwrap();
            let selection = serde_json::from_value(row["selection"].clone()).unwrap();
            let result = combo_plan(&definitions, &selection).unwrap();
            assert_eq!(json!(result.first), row["first"]);
            assert_eq!(json!(result.slots), row["slots"]);
        }
        let intro = fixture(include_str!(
            "../../../native/kbcs-core/tests/combo-intro-vectors.json"
        ));
        for row in intro["cases"].as_array().unwrap() {
            let groups: Vec<i32> = serde_json::from_value(row["groups"].clone()).unwrap();
            assert_eq!(
                json!(combo_intro(row["frame"].as_i64().unwrap() as i32, 1188, &groups).unwrap()),
                row["layout"]
            );
        }
        let info = fixture(include_str!(
            "../../../native/kbcs-core/tests/battle-info-vectors.json"
        ));
        for row in info["cases"].as_array().unwrap() {
            let input = UnitInfoInput {
                center: 594,
                y: 159,
                form: row["form"].as_i64().unwrap() as i32,
                attributes: serde_json::from_value(row["attributes"].clone()).unwrap(),
                abilities: deserialize_flags(row["abilities"].clone()).unwrap(),
                talents: deserialize_flags(row["talents"].clone()).unwrap(),
                new_attributes: serde_json::from_value(row["new_attributes"].clone()).unwrap(),
                orbs: 0,
            };
            let result = unit_info(&input).unwrap();
            assert_eq!(
                json!(&result.sprites[..result.count as usize]),
                row["sprites"]
            );
        }
    }
}
