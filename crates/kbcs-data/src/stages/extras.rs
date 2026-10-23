use super::{Row, number, rows};
use crate::{
    import::read_asset,
    model::{csv_rows, plain_text},
    source::{Dataset, Source},
};
use anyhow::Result;
use rusqlite::{Connection, params};
use serde_json::{Value, json};
use std::collections::BTreeMap;

pub(super) fn import(source: &Source, dataset: &Dataset, connection: &Connection) -> Result<()> {
    let region = &dataset.current.header.source_region;
    let paths = [
        "Data/SpecialRulesMap.json",
        "Data/SpecialRulesMapOption.json",
        "Data/ScoreBonusMap.json",
        "Data/StagePointRulesMap.json",
        "Data/MapStageDataClearCountReward.json",
        "Data/MapConditions.json",
        "Data/Charagroup.csv",
        "Data/fixed_formation.csv",
        "Data/DemonCastlelimit.csv",
        "Data/stage_conditions.csv",
        "Data/PlayDungeonD_000.csv",
        "Data/RandomDungeon_000.csv",
        "Data/EX_group.csv",
        "Data/EX_lottery.csv",
        "Data/EX_option.csv",
        "Data/PlayStageLimit.csv",
        "res/MapStageLimitMessage.csv",
        "res/localizable.tsv",
    ];
    for path in paths {
        if !dataset.files.contains_key(path) {
            continue;
        }
        let bytes = read_asset(source, dataset, connection, path)?;
        let content = std::str::from_utf8(&bytes)?.trim_start_matches('\u{feff}');
        if path.ends_with(".json") {
            let _: Value = serde_json::from_str(content)?;
        }
        connection.execute(
            "INSERT INTO stage_attachment VALUES (?,?,?)",
            params![region, path, content],
        )?;
    }
    if dataset.files.contains_key("Data/fixed_formation.csv") {
        let bytes = read_asset(source, dataset, connection, "Data/fixed_formation.csv")?;
        for row in csv_rows(&bytes)? {
            if let Some(file) = row
                .get(3)
                .filter(|v| v.ends_with(".json") || v.ends_with(".preset"))
            {
                let path = format!("Data/{file}");
                if dataset.files.contains_key(&path) {
                    let bytes = read_asset(source, dataset, connection, &path)?;
                    let value: Value = serde_json::from_slice(&bytes)?;
                    connection.execute(
                        "INSERT OR IGNORE INTO stage_attachment VALUES (?,?,?)",
                        params![region, path, serde_json::to_string(&value)?],
                    )?;
                }
            }
        }
    }
    let clear_path = "Data/MapStageDataClearCountReward.json";
    if dataset.files.contains_key(clear_path) {
        let raw: Value =
            serde_json::from_slice(&read_asset(source, dataset, connection, clear_path)?)?;
        if let Some(maps) = raw["MapID"].as_object() {
            for (map, stages) in maps {
                let Ok(map) = map.parse::<i64>() else {
                    continue;
                };
                if let Some(stages) = stages.as_object() {
                    for (stage, rewards) in stages {
                        let Ok(stage) = stage.parse::<i64>() else {
                            continue;
                        };
                        let exists: bool=connection.query_row("SELECT EXISTS(SELECT 1 FROM stage WHERE region=? AND map_id=? AND stage_index=?)",params![region,map,stage],|r|r.get(0))?;
                        if !exists {
                            continue;
                        }
                        let mut position: i64=connection.query_row("SELECT coalesce(max(position)+1,0) FROM stage_reward WHERE region=? AND map_id=? AND stage_index=?",params![region,map,stage],|r|r.get(0))?;
                        if let Some(data) = rewards["data"].as_array() {
                            for (index, reward) in data.iter().enumerate() {
                                let id = reward["DropItemID"].as_i64().unwrap_or(-1);
                                let amount = reward["Quantity"].as_i64().unwrap_or(0);
                                if id >= 0 && amount > 0 {
                                    connection.execute(
                                        "INSERT INTO stage_reward VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                                        params![
                                            region,
                                            map,
                                            stage,
                                            position,
                                            index as i64 + 1,
                                            id,
                                            amount,
                                            -1,
                                            "clear",
                                            clear_path,
                                            format!("/MapID/{map}/{stage}/data/{index}")
                                        ],
                                    )?;
                                    position += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    // 候補の範囲と根拠行を保持する。抽選率や実際の選択結果は固定しない。
    for (path, labyrinth) in [
        ("Data/stage_conditions.csv", true),
        ("Data/PlayDungeonD_000.csv", false),
    ] {
        if !dataset.files.contains_key(path) {
            continue;
        }
        let input = rows(&read_asset(source, dataset, connection, path)?, None)?;
        for (order, (line, cells, v)) in input.iter().enumerate() {
            let map = if labyrinth { number(v, 0) } else { 16000 };
            let first = if labyrinth {
                number(v, 1)
            } else {
                order as i64
            };
            let last = if labyrinth {
                number(v, 2)
            } else {
                order as i64
            };
            let lower = number(v, if labyrinth { 3 } else { 2 });
            let upper = number(v, if labyrinth { 4 } else { 3 });
            if first < 0 || last < first || last >= 1000 || lower < 0 || upper < lower {
                continue;
            }
            let mut statement=connection.prepare("SELECT stage_index FROM stage WHERE region=? AND map_id=? AND stage_index BETWEEN ? AND ?")?;
            let stages = statement
                .query_map(params![region, map, first, last], |r| r.get::<_, i64>(0))?
                .collect::<rusqlite::Result<Vec<_>>>()?;
            let mut definitions = Vec::new();
            if labyrinth {
                for index in lower..=upper {
                    let definition = format!("Data/stageL000_{index:02}.csv");
                    let exists: bool = connection.query_row(
                        "SELECT EXISTS(SELECT 1 FROM stage_definition WHERE region=? AND path=?)",
                        params![region, definition],
                        |r| r.get(0),
                    )?;
                    if exists {
                        definitions.push((definition, format!("テンプレート {index}")));
                    }
                }
            } else {
                let mut statement=connection.prepare("SELECT e.definition_path,m.name,s.name FROM stage_entry e JOIN stage s USING(region,map_id,stage_index) JOIN stage_map m ON m.region=e.region AND m.id=e.map_id WHERE e.region=? AND e.map_id BETWEEN ? AND ? AND e.definition_path IS NOT NULL ORDER BY e.map_id,e.stage_index")?;
                definitions = statement
                    .query_map(params![region, lower, upper], |r| {
                        Ok((
                            r.get::<_, String>(0)?,
                            format!("{} / {}", r.get::<_, String>(1)?, r.get::<_, String>(2)?),
                        ))
                    })?
                    .collect::<rusqlite::Result<_>>()?;
            }
            for stage in stages {
                for (position, (definition, name)) in definitions.iter().enumerate() {
                    connection.execute(
                        "INSERT OR IGNORE INTO stage_variant VALUES (?,?,?,?,?,?,?,?,?)",
                        params![
                            region,
                            map,
                            stage,
                            position as i64,
                            definition,
                            name,
                            path,
                            *line as i64,
                            serde_json::to_string(cells)?
                        ],
                    )?;
                }
            }
        }
    }
    Ok(())
}

pub(super) struct Extras {
    numeric: BTreeMap<String, Vec<Row>>,
    csv: BTreeMap<String, Vec<Vec<String>>>,
    text: BTreeMap<String, String>,
    parsed: BTreeMap<String, Value>,
}
impl Extras {
    pub fn read(connection: &Connection, region: &str) -> Result<Self> {
        let mut statement =
            connection.prepare("SELECT path,content FROM stage_attachment WHERE region=?")?;
        let files: BTreeMap<String, String> = statement
            .query_map([region], |r| Ok((r.get(0)?, r.get(1)?)))?
            .collect::<rusqlite::Result<_>>()?;
        let text = files
            .get("res/localizable.tsv")
            .map(|s| {
                s.lines()
                    .filter_map(|l| {
                        let (k, v) = l.split_once('\t')?;
                        Some((k.into(), plain_text(v)))
                    })
                    .collect()
            })
            .unwrap_or_default();
        let parsed = files
            .iter()
            .filter(|(p, _)| p.ends_with(".json") || p.ends_with(".preset"))
            .map(|(p, s)| Ok((p.clone(), serde_json::from_str(s)?)))
            .collect::<Result<_>>()?;
        let numeric = files
            .iter()
            .filter(|(p, _)| {
                [
                    "Data/PlayStageLimit.csv",
                    "Data/DemonCastlelimit.csv",
                    "Data/EX_group.csv",
                    "Data/EX_lottery.csv",
                ]
                .contains(&p.as_str())
            })
            .map(|(p, s)| Ok((p.clone(), rows(s.as_bytes(), None)?)))
            .collect::<Result<_>>()?;
        let csv = files
            .iter()
            .filter(|(p, _)| {
                [
                    "Data/Charagroup.csv",
                    "Data/fixed_formation.csv",
                    "res/MapStageLimitMessage.csv",
                ]
                .contains(&p.as_str())
            })
            .map(|(p, s)| Ok((p.clone(), csv_rows(s.as_bytes())?)))
            .collect::<Result<_>>()?;
        Ok(Self {
            numeric,
            csv,
            text,
            parsed,
        })
    }
    pub fn json(&self, path: &str) -> &Value {
        self.parsed.get(path).unwrap_or(&Value::Null)
    }
    fn label(&self, key: &Value) -> String {
        self.text
            .get(key.as_str().unwrap_or(""))
            .cloned()
            .unwrap_or_default()
    }
    pub fn group(&self, id: i64) -> Result<Option<Value>> {
        let Some(content) = self.csv.get("Data/Charagroup.csv") else {
            return Ok(None);
        };
        for row in content {
            if row.first().and_then(|v| v.parse::<i64>().ok()) == Some(id) {
                return Ok(Some(
                    json!({"id":id,"label":self.text.get(row.get(1).map(String::as_str).unwrap_or("")).cloned().unwrap_or_else(||"キャラ指定".into()),"type":row.get(2).and_then(|v|v.parse::<i64>().ok()).unwrap_or(0),"units":row.iter().skip(3).filter_map(|v|v.parse::<i64>().ok()).filter(|v|*v>=0).collect::<Vec<_>>()}),
                ));
            }
        }
        Ok(None)
    }
    pub fn map(&self, id: i64, headers: &Value) -> Result<Value> {
        let mut result = json!({"rules":[],"conditions":[]});
        if let Some(rule) = self
            .json("Data/SpecialRulesMap.json")
            .pointer(&format!("/MapID/{id}"))
            .cloned()
        {
            let labels = [
                "おこづかい制",
                "生産時間固定",
                "レア度別の編成数制限",
                "レア度別の生産数制限",
                "生産コスト固定",
                "レア度別コスト倍率",
                "レア度別生産時間倍率",
                "生産総数制限",
                "追加生産",
                "にゃんこ砲倍率",
                "移動速度変更",
                "生産条件",
                "フィーバー",
            ];
            result["ruleName"] = json!(self.label(&rule["RuleNameLabel"]));
            result["ruleDescription"] = json!(self.label(&rule["RuleExplanationLabel"]));
            result["rules"]=json!(rule["RuleType"].as_object().map(|values|values.iter().map(|(key,v)|{let index=key.parse::<usize>().unwrap_or(usize::MAX);json!({"id":index,"label":labels.get(index).copied().unwrap_or("特殊ルール"),"parameters":v["Parameters"]})}).collect::<Vec<_>>()).unwrap_or_default());
        }
        if let Some(bonus) = self
            .json("Data/ScoreBonusMap.json")
            .pointer(&format!("/MapID/{id}"))
            .cloned()
        {
            result["scoreBonus"] = json!({"name":self.label(&bonus["BonusNameLabel"]),"description":self.label(&bonus["BonusExplanationLabel"]),"raw":bonus});
        }
        let mut conditions = Vec::new();
        for (column, kind) in [(3, "表示"), (4, "挑戦")] {
            let code = headers
                .get(0)
                .and_then(|v| v.get(column))
                .and_then(|v| v.as_str())
                .and_then(|v| v.trim().parse::<i64>().ok())
                .unwrap_or(0);
            if code != 0 && code != -1 {
                conditions.push(json!({"kind":kind,"code":code,"group":self.json("Data/MapConditions.json").pointer(&format!("/data/{code}"))}));
            }
        }
        if let Some(s) = self.numeric.get("Data/PlayStageLimit.csv") {
            for (_, _, v) in s {
                if number(v, 0) == id {
                    conditions
                        .push(json!({"kind":"挑戦","minStage":number(v,1),"code":number(v,2)}));
                }
            }
        }
        if let Some(content) = self.csv.get("res/MapStageLimitMessage.csv") {
            let messages = content
                .iter()
                .filter_map(|r| {
                    Some((
                        r.first()?.parse::<i64>().ok()?,
                        r.iter()
                            .skip(1)
                            .map(|v| plain_text(v))
                            .collect::<Vec<_>>()
                            .join("\n"),
                    ))
                })
                .collect::<BTreeMap<_, _>>();
            for condition in &mut conditions {
                if let Some(message) = condition["code"].as_i64().and_then(|id| messages.get(&id)) {
                    condition["message"] = json!(message);
                }
            }
        }
        result["conditions"] = json!(conditions);
        Ok(result)
    }
    pub fn stage(&self, map: i64, index: i64) -> Result<Value> {
        let mut result = json!({});
        if let Some(point) = self
            .json("Data/StagePointRulesMap.json")
            .pointer(&format!("/MapID/{map}/StageIndex/{index}"))
            .cloned()
        {
            result["pointRules"] = json!({"name":self.label(&point["PageHeadline"]),"sections":point["RuleHeadlineLabel"].as_array().map(|a|a.iter().enumerate().map(|(i,k)|json!({"name":self.label(k),"description":self.label(&point["RuleExplanationLabel"][i])})).collect::<Vec<_>>()).unwrap_or_default(),"raw":point});
        }
        if let Some(raw) = self
            .json("Data/MapStageDataClearCountReward.json")
            .pointer(&format!("/MapID/{map}/{index}/data"))
            .and_then(Value::as_array)
        {
            result["clearRewards"] = json!(
                raw.iter()
                    .enumerate()
                    .filter_map(|(i, v)| {
                        let id = v["DropItemID"].as_i64()?;
                        let count = v["Quantity"].as_i64()?;
                        if id < 0 || count <= 0 {
                            None
                        } else {
                            Some(json!({"clear":i+1,"id":id,"count":count}))
                        }
                    })
                    .collect::<Vec<_>>()
            );
        }
        if let (Some(groups), Some(lottery)) = (
            self.numeric.get("Data/EX_group.csv"),
            self.numeric.get("Data/EX_lottery.csv"),
        ) {
            for (_, _, v) in groups {
                if number(v, 1) == map && number(v, 2) == index {
                    let mut choices = Vec::new();
                    for column in (3..v.len().saturating_sub(1)).step_by(2) {
                        if let Some(target) = usize::try_from(number(v, column))
                            .ok()
                            .and_then(|i| lottery.get(i))
                        {
                            let native_map = number(&target.2, 0);
                            choices.push(json!({"nativeMap":native_map,"map":format!("EX{:03}",native_map-4000),"stage":number(&target.2,1),"chance":null,"threshold":number(v,column+1)}));
                        }
                    }
                    result["exLottery"] = json!(choices);
                }
            }
        }
        if let Some(s) = self.numeric.get("Data/DemonCastlelimit.csv") {
            for (_, _, v) in s {
                if number(v, 0) == map * 100 + index {
                    result["levelSeal"] =
                        json!({"level":number(v,1),"plus":number(v,2)==1,"enemy":number(v,3)});
                }
            }
        }
        if let Some(s) = self.csv.get("Data/fixed_formation.csv") {
            for row in s {
                if row.first().and_then(|v| v.parse::<i64>().ok()) == Some(map)
                    && row.get(2).and_then(|v| v.parse::<i64>().ok()) == Some(index)
                    && let Some(file) = row.get(3)
                {
                    let value = self.json(&format!("Data/{file}"));
                    let mut choices = Vec::new();
                    if let Some(slots) = value.pointer("/slot/data").and_then(Value::as_object) {
                        for (key, slot) in slots {
                            let mut units = Vec::new();
                            if let Some(characters) = slot["chara"].as_array() {
                                for id in characters.iter().filter_map(integer) {
                                    let character = &value["chara"]["data"][id.to_string()];
                                    units.push(json!({"id":id,"form":integer(&character["evolution"]).map(|v|v-1),"level":integer(&character["level"]),"plus":integer(&character["plus"]).unwrap_or(0)}));
                                }
                            }
                            choices.push(json!({"index":key.parse::<i64>().unwrap_or(0),"cannon":integer(&slot["cannon"]).unwrap_or(0),"units":units}));
                        }
                    }
                    result["formation"] = json!({"selected":row.get(1).and_then(|v|v.parse::<i64>().ok()).unwrap_or(0),"choices":choices});
                }
            }
        }
        Ok(result)
    }
}

fn integer(value: &Value) -> Option<i64> {
    value.as_i64().or_else(|| value.as_str()?.parse().ok())
}
