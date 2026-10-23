use serde::{Deserialize, Serialize};

#[repr(C)]
#[derive(Clone, Copy, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Definition {
    pub redirect: i32,
    pub factor: i32,
    pub limit: i32,
}
#[repr(C)]
#[derive(Default, Serialize, Deserialize, Debug, PartialEq)]
pub struct Grant {
    pub target: i32,
    pub total: i32,
    pub change: i32,
}
unsafe extern "C" {
    fn kbcs_core_item_add(
        definitions: *const Definition,
        counts: *mut i32,
        count: i32,
        index: i32,
        amount: i32,
        output: *mut Grant,
    ) -> u32;
}
pub fn add(
    definitions: &[Definition],
    counts: &mut [i32],
    index: usize,
    amount: i32,
) -> Result<Grant, u32> {
    if definitions.len() != counts.len() || definitions.len() > 4096 || index >= definitions.len() {
        return Err(1);
    }
    let mut output = Grant::default();
    // 正規化した所持数だけを変更する。原本の保存形式や解放フラグは所有側の責務。
    let code = unsafe {
        kbcs_core_item_add(
            definitions.as_ptr(),
            counts.as_mut_ptr(),
            counts.len() as i32,
            index as i32,
            amount,
            &mut output,
        )
    };
    if code == 0 { Ok(output) } else { Err(code) }
}

#[test]
fn native_inventory_witnesses() {
    let fixture: serde_json::Value = serde_json::from_str(include_str!(
        "../../../native/kbcs-core/tests/inventory-vectors.json"
    ))
    .unwrap();
    let definitions: Vec<Definition> =
        serde_json::from_value(fixture["definitions"].clone()).unwrap();
    for vector in fixture["vectors"].as_array().unwrap() {
        let target = vector["target"].as_u64().unwrap() as usize;
        let mut counts = vec![0; definitions.len()];
        counts[target] = vector["current"].as_i64().unwrap() as i32;
        let output = add(
            &definitions,
            &mut counts,
            vector["index"].as_u64().unwrap() as usize,
            vector["amount"].as_i64().unwrap() as i32,
        )
        .unwrap();
        assert_eq!(output.total, vector["total"].as_i64().unwrap() as i32);
        assert_eq!(output.target as usize, target);
        assert_eq!(counts[target], output.total);
    }
    let mut nested = definitions.clone();
    nested[0].redirect = 1;
    nested[0].factor = 2;
    nested[1].redirect = 6;
    nested[1].factor = 3;
    for vector in fixture["nested"].as_array().unwrap() {
        let mut counts = vec![0; nested.len()];
        counts[6] = vector["current"].as_i64().unwrap() as i32;
        let output = add(&nested, &mut counts, 0, 5).unwrap();
        assert_eq!(output.total, vector["total"].as_i64().unwrap() as i32);
    }
    let cyclic = [Definition {
        redirect: 0,
        factor: 1,
        limit: 9999,
    }];
    let mut counts = [37];
    assert!(matches!(add(&cyclic, &mut counts, 0, 1), Err(1)));
    assert_eq!(counts, [37]);
    let direct = [Definition {
        redirect: -1,
        factor: 1,
        limit: i32::MAX,
    }];
    counts[0] = i32::MAX;
    assert!(matches!(add(&direct, &mut counts, 0, 1), Err(2)));
    assert_eq!(counts, [i32::MAX]);
}
