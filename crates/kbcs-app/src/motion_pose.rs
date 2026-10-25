use anyhow::{Context, Result, ensure};
use kbcs_bridge::render::Model;
use kbcs_data::store::Database;
use serde::Deserialize;
use serde_json::{Value, json};
use std::{collections::BTreeMap, sync::Arc};

#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Input {
    pub kind: String,
    pub id: Value,
    #[serde(default)]
    pub form: u8,
    pub resource: String,
    pub clip: String,
    pub frames: Vec<i32>,
    pub facing: i32,
}
impl Input {
    pub fn key(&self) -> String {
        format!(
            "{}:{}:{}:{}:{}",
            self.kind, self.id, self.form, self.resource, self.clip
        )
    }
}
pub fn resource_model(manifest: &Value, resource: &str, clip: &str) -> Result<Model> {
    ensure!(
        ["body", "soul"].contains(&resource),
        "描画リソースが不正です"
    );
    let body = &manifest[resource];
    let text = |path: &str| {
        manifest["files"]
            .as_array()
            .into_iter()
            .flatten()
            .find(|v| v["path"] == path)
            .and_then(|v| v["text"].as_str())
            .context("描画原本がありません")
    };
    let animations = body["animations"]
        .as_array()
        .context("モーション一覧なし")?;
    let animation = animations
        .iter()
        .find(|v| v["key"] == clip)
        .and_then(|v| v["path"].as_str());
    ensure!(
        animation.is_some() || (clip == "static" && animations.is_empty()),
        "モーションがありません"
    );
    Model::parse(
        text(body["cut"].as_str().context("分割なし")?)?,
        text(body["model"].as_str().context("モデルなし")?)?,
        animation.map(text).transpose()?,
    )
    .map_err(anyhow::Error::msg)
}
pub fn model(database: &Database, region: &str, input: &Input) -> Result<Model> {
    let manifest = if input.kind == "effect" {
        kbcs_data::effects::manifest(database, input.id.as_str().context("演出IDが不正です")?)?
    } else {
        ensure!(
            ["unit", "enemy"].contains(&input.kind.as_str()),
            "描画種別が不正です"
        );
        kbcs_data::motions::manifest(
            database,
            region,
            &input.kind,
            u32::try_from(input.id.as_u64().context("キャラIDが不正です")?)?,
            usize::from(input.form),
        )?
    };
    resource_model(&manifest, &input.resource, &input.clip)
}
pub fn frames(model: Arc<Model>, input: &Input) -> Result<Value> {
    ensure!(
        !input.frames.is_empty()
            && input.frames.len() <= 32
            && input.frames.iter().all(|v| (0..=1000000).contains(v)),
        "表示フレームが範囲外です"
    );
    let mut frames = BTreeMap::new();
    for frame in &input.frames {
        let packets = model
            .pose(*frame, false, true, input.facing)
            .map_err(|code| anyhow::anyhow!("姿勢計算エラー: {code}"))?;
        frames.insert(*frame, packets);
    }
    Ok(json!({"frames":frames,"core":"C++","ruleset":kbcs_bridge::ruleset_version()}))
}
