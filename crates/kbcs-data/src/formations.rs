use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, params};
use serde::{Deserialize, Serialize};
use serde_json::{Value, json};
use std::{collections::BTreeMap, path::Path, time::Duration};

#[derive(Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Member {
    pub unit_id: u32,
    pub form: u8,
    pub level: u16,
    pub plus: u16,
    pub talents: BTreeMap<u32, u16>,
    pub orbs: Vec<Option<u32>>,
}
#[derive(Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Cannon {
    pub id: u8,
    pub level: u8,
    #[serde(rename = "developmentLevel", default = "maximum_development")]
    pub development_level: u8,
}
fn maximum_development() -> u8 {
    30
}
#[derive(Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Document {
    pub format: String,
    pub schema_version: u32,
    pub region: String,
    pub game_version: String,
    pub name: String,
    pub slot_name: String,
    pub slots: [Option<Member>; 10],
    pub cannon: Cannon,
    pub profile: Value,
}
impl Document {
    pub fn validate(&self, region: &str) -> Result<()> {
        self.validate_capacity(region, |id| {
            crate::equipment::capacity(&self.game_version, id)
        })
    }
    pub fn validate_with_database(
        &self,
        region: &str,
        database: &crate::store::Database,
    ) -> Result<()> {
        let equipment = crate::equipment::capacities(database)?;
        self.validate_capacity(region, |id| Ok(equipment.get(&id).copied().unwrap_or(0)))
    }
    fn validate_capacity(
        &self,
        region: &str,
        capacity: impl Fn(u32) -> Result<usize>,
    ) -> Result<()> {
        ensure!(
            self.format == "kbcs-formation" && self.schema_version == 1,
            "未対応の編成ファイル形式です"
        );
        ensure!(self.region == region, "編成ファイルの地域が一致しません");
        ensure!(
            !self.name.trim().is_empty()
                && self.name.chars().count() <= 120
                && self.slot_name.chars().count() <= 120,
            "編成名・スロット名が不正です"
        );
        ensure!(
            self.cannon.id <= 7
                && self.cannon.level <= 30
                && (1..=30).contains(&self.cannon.development_level),
            "城砲の設定が不正です"
        );
        let mut ids = std::collections::BTreeSet::new();
        for member in self.slots.iter().flatten() {
            ensure!(
                member.form <= 3 && member.level > 0 && ids.insert(member.unit_id),
                "キャラ設定が不正、または同じキャラが重複しています"
            );
            ensure!(
                member.talents.len() <= 64 && member.orbs.len() <= capacity(member.unit_id)?,
                "キャラの設定数が範囲外です"
            );
        }
        ensure!(
            self.profile["schemaVersion"] == 1 && self.profile["cannon"].is_object(),
            "お宝・施設設定の形式が不正です"
        );
        let treasures = self.profile["treasures"]
            .as_object()
            .context("お宝設定がありません")?;
        ensure!(
            treasures.len() <= 1000
                && treasures
                    .values()
                    .all(|n| n.as_u64().is_some_and(|v| v <= 100)),
            "お宝の発動率が不正です"
        );
        let facilities = self.profile["facilities"]
            .as_object()
            .context("施設設定がありません")?;
        ensure!(
            facilities.len() <= 100
                && facilities
                    .values()
                    .all(|v| v["level"].as_u64().is_some_and(|n| n > 0 && n <= 1000)
                        && v["plus"].as_u64().is_some_and(|n| n <= 1000)),
            "施設レベルが不正です"
        );
        for part in ["base", "decoration"] {
            let value = &self.profile["cannon"][part];
            ensure!(
                value["id"].as_u64().is_some_and(|n| n <= 7)
                    && value["level"].as_u64().is_some_and(|n| n <= 20),
                "土台・装飾の設定が不正です"
            );
        }
        Ok(())
    }
}
#[derive(Deserialize)]
#[serde(deny_unknown_fields)]
pub struct WriteInput {
    pub id: Option<i64>,
    pub revision: Option<i64>,
    pub document: Document,
}
pub struct Store(Connection, std::path::PathBuf);
impl Store {
    pub fn list(&self, region: &str) -> Result<Value> {
        let mut query=self.0.prepare("SELECT id,revision,json_extract(document,'$.name'),json_extract(document,'$.slotName') FROM formation WHERE region=? ORDER BY id")?;
        let entries=query.query_map([region],|row|Ok(json!({"id":row.get::<_,i64>(0)?,"revision":row.get::<_,i64>(1)?,"name":row.get::<_,String>(2)?,"slotName":row.get::<_,String>(3)?})))?.collect::<rusqlite::Result<Vec<_>>>()?;
        Ok(json!({"entries":entries}))
    }
    pub fn open(root: &Path) -> Result<Self> {
        let directory = root.join("user");
        std::fs::create_dir_all(&directory)?;
        let connection = Connection::open(directory.join("formations.sqlite"))?;
        connection.busy_timeout(Duration::from_secs(5))?;
        let version: i32 = connection.query_row("PRAGMA user_version", [], |r| r.get(0))?;
        ensure!(version == 0 || version == 1, "未対応の編成DB形式です");
        connection.execute_batch("PRAGMA journal_mode=WAL; CREATE TABLE IF NOT EXISTS formation(id INTEGER PRIMARY KEY,region TEXT NOT NULL,revision INTEGER NOT NULL,document TEXT NOT NULL CHECK(json_valid(document)),updated_at INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS formation_region ON formation(region,id); PRAGMA user_version=1;")?;
        Ok(Self(connection, root.to_path_buf()))
    }
    pub fn read(&self, region: &str, current: Option<i64>, direction: i32) -> Result<Value> {
        ensure!((-1..=1).contains(&direction), "編成の切替方向が不正です");
        let count: i64 = self.0.query_row(
            "SELECT count(*) FROM formation WHERE region=?",
            [region],
            |r| r.get(0),
        )?;
        let id = if let Some(current) = current {
            match direction {
                -1 => self
                    .0
                    .query_row(
                        "SELECT id FROM formation WHERE region=? AND id<? ORDER BY id DESC LIMIT 1",
                        params![region, current],
                        |r| r.get::<_, i64>(0),
                    )
                    .optional()?,
                1 => self
                    .0
                    .query_row(
                        "SELECT id FROM formation WHERE region=? AND id>? ORDER BY id LIMIT 1",
                        params![region, current],
                        |r| r.get::<_, i64>(0),
                    )
                    .optional()?,
                _ => self
                    .0
                    .query_row(
                        "SELECT id FROM formation WHERE region=? AND id=?",
                        params![region, current],
                        |r| r.get::<_, i64>(0),
                    )
                    .optional()?,
            }
        } else {
            None
        };
        let id = match id {
            Some(id) => Some(id),
            None => self
                .0
                .query_row(
                    if direction < 0 {
                        "SELECT id FROM formation WHERE region=? ORDER BY id DESC LIMIT 1"
                    } else {
                        "SELECT id FROM formation WHERE region=? ORDER BY id LIMIT 1"
                    },
                    [region],
                    |r| r.get::<_, i64>(0),
                )
                .optional()?,
        };
        let Some(id) = id else {
            return Ok(json!({"entry":null,"count":count}));
        };
        let (revision, text, updated): (i64, String, i64) = self.0.query_row(
            "SELECT revision,document,updated_at FROM formation WHERE region=? AND id=?",
            params![region, id],
            |r| Ok((r.get(0)?, r.get(1)?, r.get(2)?)),
        )?;
        let index: i64 = self.0.query_row(
            "SELECT count(*) FROM formation WHERE region=? AND id<=?",
            params![region, id],
            |r| r.get(0),
        )?;
        Ok(
            json!({"count":count,"index":index,"entry":{"id":id,"revision":revision,"updatedAt":updated,"document":serde_json::from_str::<Value>(&text)?}}),
        )
    }
    pub fn write(&self, region: &str, input: &WriteInput) -> Result<Value> {
        if let Ok(database) = crate::store::Database::open(&self.1, region) {
            input.document.validate_with_database(region, &database)?;
        } else {
            input.document.validate(region)?;
        }
        let text = serde_json::to_string(&input.document)?;
        let id = if let Some(id) = input.id {
            let revision = input.revision.context("編成の保存版がありません")?;
            ensure!(self.0.execute("UPDATE formation SET revision=revision+1,document=?,updated_at=unixepoch() WHERE region=? AND id=? AND revision=?",params![text,region,id,revision])?==1,"別の画面で編成が変更されています。再読込してから保存してください");
            id
        } else {
            ensure!(
                input.revision.is_none(),
                "新しい編成に保存版は指定できません"
            );
            self.0.execute("INSERT INTO formation(region,revision,document,updated_at) VALUES(?,1,?,unixepoch())",params![region,text])?;
            self.0.last_insert_rowid()
        };
        self.read(region, Some(id), 0)
    }
}
#[test]
fn persistence_isolation_and_revision_conflict() -> Result<()> {
    let root = std::env::temp_dir().join(format!(
        "kbcs-formations-{}-{}",
        std::process::id(),
        std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)?
            .as_nanos()
    ));
    let result = (|| -> Result<()> {
        let store = Store::open(&root)?;
        let value = json!({"format":"kbcs-formation","schemaVersion":1,"region":"jp","gameVersion":"15.7.2","name":"検証","slotName":"出撃1","slots":[null,null,null,null,null,null,null,null,null,null],"cannon":{"id":0,"level":0},"profile":{"schemaVersion":1,"cannon":{"base":{"id":0,"level":0},"decoration":{"id":0,"level":0}},"treasures":{"a":100},"facilities":{"research":{"level":20,"plus":10}}}});
        let mut equipment_document: Document = serde_json::from_value(value.clone())?;
        equipment_document.slots[0] = Some(Member {
            unit_id: 42,
            form: 2,
            level: 60,
            plus: 0,
            talents: BTreeMap::new(),
            orbs: vec![None, None],
        });
        equipment_document.validate("jp")?;
        equipment_document.slots[0]
            .as_mut()
            .unwrap()
            .orbs
            .push(None);
        assert!(equipment_document.validate("jp").is_err());
        equipment_document.slots[0].as_mut().unwrap().unit_id = 5;
        equipment_document.slots[0].as_mut().unwrap().orbs = vec![None];
        assert!(equipment_document.validate("jp").is_err());
        let mut input: WriteInput =
            serde_json::from_value(json!({"id":null,"revision":null,"document":value}))?;
        assert_eq!(input.document.cannon.development_level, 30);
        let first = store.write("jp", &input)?;
        input.document.name = "独立".into();
        let second = store.write("jp", &input)?;
        assert_eq!(store.list("jp")?["entries"].as_array().unwrap().len(), 2);
        let id = first["entry"]["id"].as_i64().unwrap();
        input.id = Some(id);
        input.revision = Some(1);
        input.document.profile["treasures"]["a"] = json!(0);
        store.write("jp", &input)?;
        assert!(store.write("jp", &input).is_err());
        assert_eq!(
            store.read("jp", Some(second["entry"]["id"].as_i64().unwrap()), 0)?["entry"]["document"]
                ["profile"]["treasures"]["a"],
            100
        );
        assert_eq!(
            store.read("jp", Some(second["entry"]["id"].as_i64().unwrap()), 1)?["entry"]["id"],
            id
        );
        drop(store);
        let store = Store::open(&root)?;
        assert_eq!(store.read("jp", Some(id), 0)?["entry"]["revision"], 2);
        assert_eq!(store.read("en", None, 0)?["count"], 0);
        input.document.schema_version = 2;
        assert!(store.write("jp", &input).is_err());
        Ok(())
    })();
    std::fs::remove_dir_all(root)?;
    result
}
