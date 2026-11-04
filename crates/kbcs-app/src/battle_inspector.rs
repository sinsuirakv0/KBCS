use super::{Clip, Session, native};
use anyhow::{Context, Result, ensure};
use kbcs_bridge::battle::Inspection;
use serde::Deserialize;
use serde_json::{Value, json};

#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Query {
    side: i32,
    group: String,
    offset: usize,
    selected: Option<i32>,
    revision: u32,
}

fn page(records: &[Inspection], query: &Query) -> Result<Value> {
    ensure!((0..=1).contains(&query.side), "一覧の陣営が不正です");
    ensure!(
        ["present", "retired", "all"].contains(&query.group.as_str()),
        "一覧の状態が不正です"
    );
    let mut counts = [[0i64; 5]; 2];
    let mut rows = Vec::new();
    let mut total = 0;
    for record in records {
        let count = &mut counts[record.side as usize];
        count[0] += 1;
        count[1] += i64::from(record.retired_frame < 0 && !matches!(record.action, 4 | 21));
        count[2] += i64::from(record.deaths);
        count[3] += i64::from(record.revivals);
        count[4] += i64::from(record.retired_frame >= 0);
    }
    let all = query.group == "all";
    let matches = |record: &&Inspection| {
        record.side == query.side
            && if query.group == "retired" {
                record.retired_frame >= 0
            } else {
                record.retired_frame < 0
            }
    };
    // 「すべて」でも各区分内の生成順は維持し、退場だけを後半へ置く。
    let ordered = records.iter().filter(matches).chain(
        records
            .iter()
            .filter(|record| all && record.side == query.side && record.retired_frame >= 0),
    );
    for record in ordered {
        if total >= query.offset && rows.len() < 64 {
            rows.push(record);
        }
        total += 1;
    }
    let selected = query
        .selected
        .and_then(|id| id.checked_sub(1))
        .and_then(|id| usize::try_from(id).ok())
        .and_then(|index| records.get(index));
    Ok(
        json!({"revision":query.revision,"side":query.side,"group":query.group,"offset":query.offset,"total":total,"counts":counts,"rows":rows,"selected":selected}),
    )
}

fn pose(clip: Option<&Clip>, anchor: bool, frame: i32) -> Result<Value> {
    let Some(clip) = clip else {
        return Ok(Value::Null);
    };
    // 一覧の静止画は0F。戦闘本体と同じC++姿勢・部品・ブレンドを使う。
    let packets = if anchor {
        native(clip.model.pose_config(frame, 0, 1))?
    } else {
        native(clip.model.pose(frame, false, false, 1))?
    };
    Ok(json!({"texture":clip.texture,"packets":packets,"cuts":clip.model.cuts}))
}

impl Session {
    pub fn inspection(&self, queries: &[Query]) -> Result<Value> {
        ensure!(queries.len() <= 2, "一覧の要求数が不正です");
        let records = native(self.core.inspection())?;
        let produced = native(self.core.production())?.0.total;
        let attach = |actor: &mut Value| -> Result<()> {
            let id = actor["id"]
                .as_i64()
                .and_then(|id| i32::try_from(id).ok())
                .context("観測個体IDなし")?;
            actor["attackers"] = json!(native(self.core.inspection_sources(id))?);
            Ok(())
        };
        let values = queries
            .iter()
            .map(|query| -> Result<Value> {
                let mut value = page(records, query)?;
                value["produced"] = json!(produced);
                if let Some(rows) = value["rows"].as_array_mut() {
                    for actor in rows {
                        attach(actor)?;
                    }
                }
                if !value["selected"].is_null() {
                    attach(&mut value["selected"])?;
                }
                Ok(value)
            })
            .collect::<Result<Vec<_>>>()?;
        Ok(json!(values))
    }
    pub fn inspection_assets(&self) -> Result<Value> {
        let profiles = self.models.iter().map(|model| Ok(json!({"character":model.character,"idle":pose(model.clips.get(&1),true,0)?,"kb":pose(model.clips.get(&3),true,0)?,"soul":pose(model.clips.get(&9),false,0)?}))).collect::<Result<Vec<_>>>()?;
        // downの最終静止姿勢。生きた個体の時計は変更しない。
        let bone = self.effects.get(&(6, 0, 0x1258));
        let frame = bone
            .map(|clip| native(clip.model.clock_lengths()).map(|lengths| lengths[1].max(1) - 1))
            .transpose()?
            .unwrap_or(0);
        Ok(json!({"profiles":profiles,"bone":pose(bone,false,frame)?}))
    }
}

#[test]
fn inspection_page_preserves_identity_and_counts() {
    let records: Vec<_> = (0..70)
        .map(|index| Inspection {
            id: index + 1,
            side: index % 2,
            slot: 1,
            serial: index,
            retired_frame: if index < 2 { 10 } else { -1 },
            action: if index == 3 { 14 } else { 0 },
            deaths: i32::from(index == 3),
            revivals: i32::from(index == 5),
            ..Default::default()
        })
        .collect();
    let query = Query {
        side: 1,
        group: "present".into(),
        offset: 0,
        selected: Some(2),
        revision: 8,
    };
    let value = page(&records, &query).unwrap();
    assert_eq!(value["total"], 34);
    assert_eq!(value["rows"][0]["id"], 4);
    assert_eq!(value["selected"]["id"], 2);
    assert_eq!(value["counts"][1], json!([35, 34, 1, 1, 1]));
    let all = page(
        &records,
        &Query {
            group: "all".into(),
            ..query
        },
    )
    .unwrap();
    assert_eq!(all["rows"][0]["id"], 4);
    assert_eq!(all["rows"][34]["id"], 2);
    let query = Query {
        side: 1,
        group: "present".into(),
        offset: 0,
        selected: Some(2),
        revision: 8,
    };
    assert_eq!(
        page(
            &records,
            &Query {
                offset: 100,
                ..query
            }
        )
        .unwrap()["rows"],
        json!([])
    );
}
