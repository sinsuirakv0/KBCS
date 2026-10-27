use anyhow::{Context, Result, ensure};
use kbcs_bridge::{battle, experience, inventory, reward, score};
use kbcs_data::{
    inventory::{CharacterGrant, Grant, Store},
    store::Database,
};
use serde_json::{Value, json};

pub struct Receipt {
    store: Store,
    id: i64,
    stage: Value,
    map: Value,
    key: String,
    claim: String,
    score_key: String,
    clears: i32,
    best: i32,
    xp: experience::StageInput,
    items: Vec<(i32, i64)>,
    material_ids: [i32; 16],
    item_ids: Vec<i32>,
    item_definitions: Vec<inventory::Definition>,
    entries: std::collections::BTreeMap<i32, Value>,
    text: std::collections::BTreeMap<String, String>,
    pub saved: Option<Value>,
    pub error: Option<String>,
    retry: Option<std::time::Instant>,
}
fn int(value: &Value) -> Result<i32> {
    value
        .as_i64()
        .and_then(|n| i32::try_from(n).ok())
        .context("報酬の整数値がありません")
}
fn cell(raw: &[Value], column: usize) -> Result<i32> {
    let text = raw
        .get(column)
        .and_then(Value::as_str)
        .unwrap_or("-1")
        .split("//")
        .next()
        .unwrap_or("")
        .trim();
    // 末尾カンマで残る空欄は未定義の追加候補。存在しない列と同じ扱い。
    if text.is_empty() {
        return Ok(-1);
    }
    text.parse().context("報酬の原本セルが不正です")
}
impl Receipt {
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        root: &std::path::Path,
        region: &str,
        persist: bool,
        db: &Database,
        map: &Value,
        stage: &Value,
        crown: i32,
        study: i32,
        treasure: i32,
        combo: i32,
        items: u32,
    ) -> Result<(Self, battle::RewardRules)> {
        let store = if persist {
            Store::open(root)?
        } else {
            Store::memory()?
        };
        let entries: std::collections::BTreeMap<i32, Value> =
            kbcs_data::inventory::catalog(db)?["items"]
                .as_array()
                .context("報酬一覧なし")?
                .iter()
                .map(|v| Ok((int(&v["id"])?, v.clone())))
                .collect::<Result<_>>()?;
        let key = format!("{region}:{}:{}:{crown}", map["nativeId"], stage["index"]);
        let clears = store.record(&format!("clear:{key}"))?;
        let raw = stage["rawRewards"]
            .as_array()
            .context("報酬原本がありません")?;
        let mode = int(&stage["rewardMode"])?;
        let save = map["acquisitionId"].as_i64().unwrap_or(-1) as i32;
        let policy = reward::policy(&reward::PolicyInput {
            mode,
            save_id: save,
            reward_id: cell(raw, 6)?,
            crown,
        })
        .map_err(|c| anyhow::anyhow!("報酬条件: {c}"))?;
        let claim = match policy["tracking"].as_str().unwrap_or("none") {
            "ownership" => String::new(),
            "history" => format!("history:{region}:{}:{}", map["nativeId"], stage["index"]),
            "crown" | "shared" => format!(
                "reward:{region}:{}:{save}:{}:{}",
                map["nativeKind"], stage["index"], policy["slot"]
            ),
            _ => String::new(),
        };
        let acquired = if policy["tracking"] == "ownership" {
            let entry = entries
                .get(&cell(raw, 6)?)
                .context("入手判定の報酬定義なし")?;
            if let Some(gift) = entry["gift"].as_str() {
                store.claimed(gift)?
            } else {
                let character = store.character(int(&entry["unit"])?)?;
                match int(&entry["rewardKind"])? {
                    2 => character.third,
                    3 => character.fourth,
                    _ => false,
                }
            }
        } else if claim.is_empty() {
            false
        } else {
            store.claimed(&claim)?
        };
        let mut rules = battle::RewardRules {
            mode,
            radar: i32::from(items & 2 != 0),
            acquired: i32::from(acquired),
            ..Default::default()
        };
        let events: Value = serde_json::from_slice(&kbcs_data::source::asset(
            db,
            root,
            "Data/eventDisplayData.json",
        )?)?;
        let event = &events["MapSet"][map["nativeId"].to_string()];
        rules.music = [cell(raw, 2)?, cell(raw, 4)?];
        rules.music_threshold = cell(raw, 3)?;
        rules.music_delay = event["BattleBGMPlayTiming"].as_i64().unwrap_or(0) as i32;
        rules.start_sound = event["BattleStartSE"].as_i64().unwrap_or(-1) as i32;
        let settings = stage["rawSettings"]
            .as_array()
            .context("ステージ設定なし")?;
        rules.ex.chance = cell(settings, 2)?.max(0);
        if rules.ex.chance > 0 {
            rules.ex.map_index = cell(settings, 3)?;
            rules.ex.minimum = cell(settings, 4)?;
            rules.ex.maximum = cell(settings, 5)?;
        }
        let groups = kbcs_data::model::numeric_rows(&db.source("Data/EX_group.csv")?.3)?;
        let lottery = kbcs_data::model::numeric_rows(&db.source("Data/EX_lottery.csv")?.3)?;
        for (_, values) in groups {
            if values.get(1).copied().flatten() != map["nativeId"].as_i64()
                || values.get(2).copied().flatten() != stage["index"].as_i64()
            {
                continue;
            }
            rules.ex.group_present = 1;
            for column in (3..values.len().saturating_sub(1)).step_by(2) {
                let group = values[column].unwrap_or(-1);
                if group < 0 {
                    continue;
                }
                let target = &lottery.get(group as usize).context("EX候補がありません")?.1;
                let index = rules.ex_count as usize;
                ensure!(index < 32, "EX候補が多すぎます");
                rules.ex_choices[index] = kbcs_bridge::transition::Choice {
                    group: group as i32,
                    threshold: values[column + 1].context("EX閾値なし")? as i32,
                    map_index: (target.first().copied().flatten().context("EXマップなし")? - 4000)
                        as i32,
                    stage: target.get(1).copied().flatten().context("EX面なし")? as i32,
                };
                rules.ex_count += 1;
            }
            break;
        }
        for (prefix, kind, count, values) in [
            (
                "Win",
                &mut rules.win_type,
                &mut rules.win_count,
                &mut rules.win_sounds,
            ),
            (
                "Lose",
                &mut rules.lose_type,
                &mut rules.lose_count,
                &mut rules.lose_sounds,
            ),
        ] {
            *kind = event[format!("BattleFinish{prefix}SEtype")]
                .as_i64()
                .unwrap_or(0) as i32;
            if let Some(sounds) = event[format!("BattleFinish{prefix}SE")].as_array() {
                ensure!(sounds.len() <= 32, "終了SEが多すぎます");
                *count = sounds.len() as i32;
                for (target, value) in values.iter_mut().zip(sounds) {
                    *target = int(value)?;
                }
            }
        }
        let mut candidates = Vec::new();
        if mode >= -2 {
            let context = reward::StageContext {
                mode,
                save_id: save,
                acquired: rules.acquired,
                radar: rules.radar,
                chances: [cell(raw, 5)?, cell(raw, 9)?, cell(raw, 12)?],
                rolls: [0; 3],
            };
            if let Some(input) = reward::prepare_stage_input(&context)
                .map_err(|c| anyhow::anyhow!("報酬入力: {c}"))?
            {
                rules.enabled = 1;
                rules.mode = input.mode;
                rules.count = input.count;
                rules.chances[..3].copy_from_slice(&input.chances);
                for i in 0..input.count as usize {
                    let column = [6, 10, 13][i];
                    candidates.push((cell(raw, column)?, i64::from(cell(raw, column + 1)?)));
                }
            }
        } else {
            for i in 0..10 {
                let column = if i == 0 { 5 } else { i * 3 + 6 };
                let weight = cell(raw, column)?;
                if weight < 0 {
                    break;
                }
                rules.chances[i] = weight;
                rules.count += 1;
                candidates.push((cell(raw, column + 1)?, i64::from(cell(raw, column + 2)?)));
            }
            if rules.count > 0 {
                rules.enabled = 1;
            }
        }
        let mut material_ids = [-1; 16];
        let definitions = kbcs_data::inventory::definitions(db)?;
        let mut item_ids = Vec::with_capacity(definitions.len());
        let mut item_definitions = Vec::with_capacity(definitions.len());
        for row in &definitions {
            let value = |index: usize| -> Result<i32> {
                row.get(index).copied().context("アイテム定義なし")
            };
            item_ids.push(value(3)?);
            // 表示数はユーザー設定。原本の変換だけを増分へ適用し、所持上限とは分離する。
            item_definitions.push(inventory::Definition {
                redirect: value(8)?,
                factor: value(4)?,
                limit: i32::MAX,
            });
        }
        if let Some(material) = map["materials"].as_object() {
            let index = int(&stage["index"])? as usize;
            if let Some(count) = material["counts"].get(index).and_then(Value::as_f64) {
                rules.material_enabled = 1;
                rules.material.count = count as f32;
                rules.material.multiplier = material["multipliers"][crown as usize - 1]
                    .as_f64()
                    .context("素材の冠倍率なし")?
                    as f32;
                rules.material.miss = int(&material["miss"])?;
                rules.material.weights = serde_json::from_value(material["weights"].clone())?;
                for item in material["items"].as_array().context("素材一覧なし")? {
                    let slot = int(&item["slot"])? as usize;
                    let index = int(&item["id"])? as usize;
                    material_ids[slot] = definitions
                        .get(index)
                        .and_then(|r| r.get(3))
                        .copied()
                        .context("素材の報酬IDなし")?
                        as i32;
                }
            }
        }
        let mut score_key = format!(
            "score:{region}:{}:{}:{}",
            map["nativeKind"], map["scoreId"], stage["index"]
        );
        if (4..=6).contains(&int(&map["nativeMode"])?) {
            score_key = format!(
                "chapter-score:{region}:{}:{}",
                map["nativeMode"], stage["index"]
            );
        }
        if matches!(map["nativeKind"].as_i64(), Some(3 | 4 | -26)) {
            score_key = format!("best:{key}");
        }
        let best = store.record(&score_key)?;
        let xp = experience::StageInput {
            mode: int(&map["nativeMode"])?,
            kind: int(&map["nativeKind"])?,
            stage: int(&stage["index"])?,
            base: stage["xp"].as_i64().unwrap_or(0) as i32,
            clears,
            study_level: study,
            treasure,
            combo,
            okame: i32::from(items & 16 != 0),
        };
        // 開始時に検査し、勝利後の入力不備で保存を止めない。
        experience::stage(&xp).map_err(|c| anyhow::anyhow!("経験値入力: {c}"))?;
        let id = store.begin()?;
        let bytes = kbcs_data::source::asset(db, root, "res/localizable.tsv")?;
        let text = std::str::from_utf8(&bytes)?
            .trim_start_matches('\u{feff}')
            .lines()
            .filter_map(|line| line.split_once('\t'))
            .map(|(key, value)| (key.to_string(), value.to_string()))
            .collect();
        Ok((
            Self {
                store,
                id,
                stage: stage.clone(),
                map: map.clone(),
                key,
                claim,
                score_key,
                clears,
                best,
                xp,
                items: candidates,
                material_ids,
                item_ids,
                item_definitions,
                entries,
                text,
                saved: None,
                error: None,
                retry: None,
            },
            rules,
        ))
    }
    pub fn settle(&mut self, core: &battle::Battle) {
        if self.saved.is_some() || self.retry.is_some_and(|t| t.elapsed().as_secs() < 2) {
            return;
        }
        let result = self.finish(core);
        if let Err(error) = result {
            self.error = Some(format!("{error:#}"));
            self.retry = Some(std::time::Instant::now());
        }
    }
    fn finish(&mut self, core: &battle::Battle) -> Result<()> {
        let outcome = core
            .outcome()
            .map_err(|c| anyhow::anyhow!("勝敗取得: {c}"))?;
        if outcome.mode == 0 {
            return Ok(());
        }
        let rewards = core
            .rewards()
            .map_err(|c| anyhow::anyhow!("報酬取得: {c}"))?;
        ensure!(rewards.ready != 0, "報酬計算が完了していません");
        let mut grants = Vec::new();
        let mut records = Vec::new();
        let mut push = |id, amount, source: &str, claim| {
            grants.push(Grant {
                id,
                amount,
                source: source.into(),
                claim,
                notification: None,
                character: None,
            })
        };
        if outcome.mode == 1 {
            let xp = experience::stage(&self.xp)
                .map_err(|c| anyhow::anyhow!("経験値: {c}"))?
                .stages[4];
            push(6, xp, "experience", None);
            if rewards.winner >= 0 {
                let (id, count) = self.items[rewards.winner as usize];
                push(
                    id,
                    count,
                    "drop",
                    (rewards.mark != 0 && !self.claim.is_empty()).then(|| self.claim.clone()),
                );
            }
            for (slot, count) in rewards
                .materials
                .iter()
                .enumerate()
                .filter(|(_, n)| **n > 0)
            {
                push(self.material_ids[slot], i64::from(*count), "material", None);
            }
            if self.stage["scoreRewards"]
                .as_array()
                .is_some_and(|a| !a.is_empty())
                && score::stage_available(
                    int(&self.map["nativeMode"])?,
                    self.map["scoreId"].as_i64().unwrap_or(-1) as i32,
                    1,
                )
            {
                let rows = self.stage["scoreRewards"].as_array().unwrap();
                let mut thresholds = [0; 10];
                ensure!(rows.len() <= 10, "スコア報酬が多すぎます");
                for (i, row) in rows.iter().enumerate() {
                    thresholds[i] = int(&row["score"])?;
                }
                let result = score::calculate(&score::Input {
                    elapsed: outcome.elapsed,
                    best: self.best,
                    count: rows.len() as i32,
                    thresholds,
                })
                .map_err(|c| anyhow::anyhow!("スコア報酬: {c}"))?;
                for (i, row) in rows.iter().enumerate() {
                    if result.reward_mask & (1 << i) != 0 {
                        push(
                            int(&row["id"])?,
                            i64::from(int(&row["count"])?),
                            "score",
                            Some(format!("{}:{i}", self.score_key)),
                        );
                    }
                }
                records.push((self.score_key.clone(), result.best));
            }
            for row in self.stage["clearRewards"].as_array().into_iter().flatten() {
                if int(&row["clear"])? == self.clears + 1 {
                    push(
                        int(&row["id"])?,
                        i64::from(int(&row["count"])?),
                        "clear",
                        Some(format!("clear-reward:{}:{}", self.key, self.clears + 1)),
                    );
                }
            }
            records.push((format!("clear:{}", self.key), self.clears.saturating_add(1)));
        }
        if outcome.mode == 4 || self.map["nativeKind"] == -26 {
            records.push((format!("best:{}", self.key), outcome.score));
        }
        let mut characters = std::collections::BTreeMap::new();
        let mut gifts = std::collections::BTreeSet::new();
        for grant in &mut grants {
            // 入手旗は報酬IDではなくdrop_charaの保存番号で共有する。
            if let Some(entry) = self
                .entries
                .get(&grant.id)
                .filter(|v| v["unit"].is_number())
            {
                let unit = int(&entry["unit"])?;
                let kind = int(&entry["rewardKind"])?;
                let before = characters
                    .entry(unit)
                    .or_insert(self.store.character(unit)?)
                    .clone();
                let gift = entry["gift"].as_str().map(str::to_owned);
                let seen = if let Some(key) = &gift {
                    gifts.contains(key) || self.store.claimed(key)?
                } else {
                    false
                };
                let output = inventory::character(&inventory::CharacterInput {
                    kind,
                    seen: i32::from(seen),
                    plus: before.plus,
                    limit: int(&entry["limit"])?,
                    third: i32::from(before.third),
                    fourth: i32::from(before.fourth),
                })
                .map_err(|c| anyhow::anyhow!("キャラ入手: {c}"))?;
                let mut after = before.clone();
                after.owned |= output.result == 2;
                after.plus = output.plus;
                after.third = output.third != 0;
                after.fourth = output.fourth != 0;
                grant.amount = i64::from(matches!(output.result, 2 | 6));
                if output.result == 2 || output.result == 6 {
                    let title = self.text(if grant.source == "score" {
                        "score_reward"
                    } else {
                        "drop_reward"
                    })?;
                    let rarity = self.text(&format!("drop_rarity_{}", int(&entry["rarity"])?))?;
                    let template = self.text(match output.result {
                        2 => "drop_popup_chara_first",
                        _ if kind == 3 => "drop_popup_chara_third_evolve2",
                        _ => "drop_popup_chara_third_evolve",
                    })?;
                    grant.notification = Some(format_native(
                        template,
                        &[
                            title,
                            rarity,
                            entry["unitName"].as_str().context("キャラ名なし")?,
                        ],
                    )?);
                }
                if let Some(key) = &gift {
                    gifts.insert(key.clone());
                }
                characters.insert(unit, after.clone());
                grant.character = Some(CharacterGrant {
                    before,
                    after,
                    gift,
                    seen,
                });
            }
            if !matches!(grant.source.as_str(), "experience" | "material")
                && (self.item_ids.contains(&grant.id) || grant.id >= 30000)
            {
                let get = |key: &str| {
                    self.text
                        .get(key)
                        .with_context(|| format!("通知の原本文言なし: {key}"))
                };
                let title = get(if grant.source == "score" {
                    "score_reward"
                } else if grant.source == "clear" {
                    "backstage_result1"
                } else {
                    "drop_reward"
                })?
                .replace("%d", &(self.clears + 1).to_string());
                let name = self
                    .entries
                    .get(&grant.id)
                    .and_then(|v| v["name"].as_str())
                    .context("報酬の原本名なし")?;
                let template = get(if matches!(grant.id, 6 | 207 | 247) {
                    "drop_popup_xp"
                } else {
                    "drop_popup_item"
                })?;
                grant.notification = Some(
                    template
                        .replace("${rewardName}", &title)
                        .replace("${itemName}", name)
                        .replace("${itemNum}", &grant.amount.to_string())
                        .replace(
                            "${itemPossession}",
                            if self
                                .item_ids
                                .iter()
                                .position(|id| *id == grant.id)
                                .is_some_and(|index| matches!(index, 6 | 22))
                            {
                                ""
                            } else {
                                get("item_possession")?
                            },
                        ),
                );
            }
            if let Some(index) = self.item_ids.iter().position(|id| *id == grant.id)
                && self.item_definitions[index].redirect >= 0
            {
                let mut counts = vec![0; self.item_ids.len()];
                let converted = inventory::add(
                    &self.item_definitions,
                    &mut counts,
                    index,
                    i32::try_from(grant.amount)?,
                )
                .map_err(|c| anyhow::anyhow!("報酬変換: {c}"))?;
                grant.id = self.item_ids[converted.target as usize];
                ensure!(grant.id >= 0, "変換先の報酬IDがありません");
                grant.amount = i64::from(converted.change);
            }
        }
        // 005e82fc: 非0の城素材を番号順に4種類ずつ、2種類で改行する。
        let materials: Vec<usize> = grants
            .iter()
            .enumerate()
            .filter(|(_, g)| g.source == "material")
            .map(|(i, _)| i)
            .collect();
        for group in materials.chunks(4) {
            let mut message = self.text("Castle_material_drop00")?.to_string();
            for (position, index) in group.iter().enumerate() {
                let grant = &grants[*index];
                let name = self
                    .entries
                    .get(&grant.id)
                    .and_then(|v| v["name"].as_str())
                    .context("素材名なし")?;
                message.push_str(&format!(
                    " {name}{}{}",
                    self.text("Castle_material_drop01")?,
                    grant.amount
                ));
                if position % 2 == 1 {
                    message.push_str("<br>");
                }
            }
            grants[group[0]].notification = Some(message);
        }
        let receipt = json!({"mode":outcome.mode,"reason":outcome.reason,"score":outcome.score,"elapsed":outcome.elapsed,"radarBlocked":rewards.radar_blocked!=0,"stageName":self.stage["name"],"map":self.map["key"],"stage":self.stage["index"],"previousBest":self.best,"newRecord":outcome.score>self.best});
        self.saved = Some(self.store.finish(self.id, receipt, &grants, &records)?);
        self.error = None;
        Ok(())
    }
    fn text(&self, key: &str) -> Result<&str> {
        self.text
            .get(key)
            .map(String::as_str)
            .with_context(|| format!("通知の原本文言なし: {key}"))
    }
}

// 置換後の文字列を再解釈せず、原本の位置指定書式だけを一度走査する。
fn format_native(template: &str, values: &[&str]) -> Result<String> {
    let mut output = String::new();
    let mut rest = template;
    for value in values {
        let position = rest.find("%@").context("通知書式の引数が不足しています")?;
        output.push_str(&rest[..position]);
        output.push_str(value);
        rest = &rest[position + 2..];
    }
    ensure!(!rest.contains("%@"), "通知書式の引数が余っています");
    output.push_str(rest);
    Ok(output)
}

#[test]
fn source_reward_contract() {
    assert_eq!(cell(&[json!("100"), json!("")], 1).unwrap(), -1);
    assert_eq!(cell(&[json!("100")], 12).unwrap(), -1);
    assert!(cell(&[json!("invalid")], 0).is_err());
    assert_eq!(
        format_native("%@<br>%@", &["%@", "name"]).unwrap(),
        "%@<br>name"
    );
}
