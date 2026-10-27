use anyhow::{Context, Result, ensure};
use rusqlite::{Connection, OptionalExtension, Transaction, params};
use serde::{Deserialize, Serialize};
use serde_json::{Value, json};
use std::{collections::BTreeMap, path::Path, time::Duration};

pub struct Store(Connection);
#[derive(Clone, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Character {
    pub unit_id: i32,
    pub owned: bool,
    pub level: i32,
    pub plus: i32,
    pub third: bool,
    pub fourth: bool,
}
#[derive(Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct CharacterGrant {
    pub before: Character,
    pub after: Character,
    pub gift: Option<String>,
    pub seen: bool,
}
#[derive(Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Grant {
    pub id: i32,
    pub amount: i64,
    pub source: String,
    #[serde(default)]
    pub claim: Option<String>,
    #[serde(default)]
    pub notification: Option<String>,
    #[serde(default)]
    pub character: Option<CharacterGrant>,
}
#[derive(Deserialize)]
#[serde(rename_all = "camelCase", deny_unknown_fields)]
pub struct Display {
    pub id: i32,
    pub count: i64,
}
impl Store {
    pub fn open(root: &Path) -> Result<Self> {
        std::fs::create_dir_all(root.join("user"))?;
        Self::connection(Connection::open(root.join("user/inventory.sqlite"))?)
    }
    pub fn memory() -> Result<Self> {
        Self::connection(Connection::open_in_memory()?)
    }
    fn connection(connection: Connection) -> Result<Self> {
        connection.busy_timeout(Duration::from_secs(5))?;
        connection.execute_batch("PRAGMA foreign_keys=ON;
          CREATE TABLE IF NOT EXISTS item(id INTEGER PRIMARY KEY,display_count INTEGER NOT NULL DEFAULT 0 CHECK(display_count>=0),earned INTEGER NOT NULL DEFAULT 0 CHECK(earned>=0));
          CREATE TABLE IF NOT EXISTS record(key TEXT PRIMARY KEY,value INTEGER NOT NULL);
          CREATE TABLE IF NOT EXISTS claim(key TEXT PRIMARY KEY);
          CREATE TABLE IF NOT EXISTS battle(id INTEGER PRIMARY KEY AUTOINCREMENT,result TEXT);")?;
        connection.execute_batch("CREATE TABLE IF NOT EXISTS character(unit_id INTEGER PRIMARY KEY,document TEXT NOT NULL);")?;
        Ok(Self(connection))
    }
    pub fn begin(&self) -> Result<i64> {
        self.0.execute("INSERT INTO battle DEFAULT VALUES", [])?;
        Ok(self.0.last_insert_rowid())
    }
    pub fn record(&self, key: &str) -> Result<i32> {
        Ok(self
            .0
            .query_row("SELECT value FROM record WHERE key=?", [key], |r| r.get(0))
            .optional()?
            .unwrap_or(0))
    }
    pub fn claimed(&self, key: &str) -> Result<bool> {
        Ok(self.0.query_row(
            "SELECT EXISTS(SELECT 1 FROM claim WHERE key=?)",
            [key],
            |r| r.get(0),
        )?)
    }
    pub fn update_display(&self, value: &Display) -> Result<()> {
        ensure!(
            value.id >= 0 && (0..=9_007_199_254_740_991).contains(&value.count),
            "表示数の範囲が不正です"
        );
        self.0.execute("INSERT INTO item(id,display_count) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET display_count=excluded.display_count", params![value.id,value.count])?;
        Ok(())
    }
    pub fn items(&self) -> Result<Value> {
        let mut query = self
            .0
            .prepare("SELECT id,display_count,earned FROM item ORDER BY id")?;
        Ok(json!(query.query_map([], |r| Ok(json!({"id":r.get::<_,i32>(0)?,"displayCount":r.get::<_,i64>(1)?,"earned":r.get::<_,i64>(2)?})))?.collect::<rusqlite::Result<Vec<_>>>()?))
    }
    pub fn character(&self, unit: i32) -> Result<Character> {
        read_character(&self.0, unit)
    }
    pub fn characters(&self) -> Result<Value> {
        let mut query = self
            .0
            .prepare("SELECT document FROM character ORDER BY unit_id")?;
        let rows = query
            .query_map([], |r| r.get::<_, String>(0))?
            .collect::<rusqlite::Result<Vec<_>>>()?;
        Ok(json!(
            rows.iter()
                .map(|row| serde_json::from_str::<Value>(row))
                .collect::<serde_json::Result<Vec<_>>>()?
        ))
    }
    // 結果と累計・表示数・初回取得旗を同じトランザクションで確定する。
    pub fn finish(
        &mut self,
        battle: i64,
        mut result: Value,
        grants: &[Grant],
        records: &[(String, i32)],
    ) -> Result<Value> {
        let tx = self.0.transaction()?;
        let saved: Option<String> = tx
            .query_row("SELECT result FROM battle WHERE id=?", [battle], |r| {
                r.get(0)
            })
            .context("戦闘の保存番号がありません")?;
        if let Some(saved) = saved {
            return Ok(serde_json::from_str(&saved)?);
        }
        let mut rows = Vec::new();
        let mut notifications = Vec::new();
        for grant in grants {
            ensure!(grant.id >= 0 && grant.amount >= 0, "報酬の範囲が不正です");
            if let Some(key) = &grant.claim
                && tx.execute("INSERT OR IGNORE INTO claim VALUES(?)", [key])? == 0
            {
                continue;
            }
            if let Some(change) = &grant.character {
                ensure!(
                    read_character(&tx, change.before.unit_id)? == change.before,
                    "キャラの所持状態が更新されました"
                );
                if let Some(gift) = &change.gift {
                    let seen: bool = tx.query_row(
                        "SELECT EXISTS(SELECT 1 FROM claim WHERE key=?)",
                        [gift],
                        |r| r.get(0),
                    )?;
                    ensure!(seen == change.seen, "キャラの入手状態が更新されました");
                    tx.execute("INSERT OR IGNORE INTO claim VALUES(?)", [gift])?;
                }
                tx.execute("INSERT INTO character VALUES(?,?) ON CONFLICT(unit_id) DO UPDATE SET document=excluded.document",params![change.after.unit_id,serde_json::to_string(&change.after)?])?;
            }
            let (before, earned): (i64, i64) = tx
                .query_row(
                    "SELECT display_count,earned FROM item WHERE id=?",
                    [grant.id],
                    |r| Ok((r.get(0)?, r.get(1)?)),
                )
                .optional()?
                .unwrap_or_default();
            let after = before
                .checked_add(grant.amount)
                .context("表示数の上限を超えました")?;
            let total = earned
                .checked_add(grant.amount)
                .context("獲得累計の上限を超えました")?;
            ensure!(
                after <= 9_007_199_254_740_991 && total <= 9_007_199_254_740_991,
                "持ち物の上限を超えました"
            );
            if grant.amount > 0 {
                tx.execute("INSERT INTO item VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET display_count=excluded.display_count,earned=excluded.earned",params![grant.id,after,total])?;
                rows.push(json!({"id":grant.id,"amount":grant.amount,"before":before,"after":after,"earned":total,"source":grant.source}));
            }
            if let Some(message) = &grant.notification {
                notifications.push(
                    message
                        .replace("${itemNum1}", &before.to_string())
                        .replace("${itemNum2}", &after.to_string()),
                );
            }
        }
        for (key, value) in records {
            set_record(&tx, key, *value)?;
        }
        result["rewards"] = json!(rows);
        result["notifications"] = json!(notifications);
        tx.execute(
            "UPDATE battle SET result=? WHERE id=?",
            params![serde_json::to_string(&result)?, battle],
        )?;
        tx.commit()?;
        Ok(result)
    }
}
fn read_character(connection: &Connection, unit: i32) -> Result<Character> {
    let value: Option<String> = connection
        .query_row(
            "SELECT document FROM character WHERE unit_id=?",
            [unit],
            |r| r.get(0),
        )
        .optional()?;
    Ok(if let Some(value) = value {
        serde_json::from_str(&value)?
    } else {
        Character {
            unit_id: unit,
            owned: false,
            level: 1,
            plus: 0,
            third: false,
            fourth: false,
        }
    })
}
fn set_record(tx: &Transaction<'_>, key: &str, value: i32) -> Result<()> {
    if key.starts_with("clear:") {
        tx.execute(
            "INSERT INTO record VALUES(?,1) ON CONFLICT(key) DO UPDATE SET value=value+1",
            [key],
        )?;
    } else {
        tx.execute("INSERT INTO record VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=max(value,excluded.value)",params![key,value])?;
    }
    Ok(())
}

pub fn definitions(database: &crate::store::Database) -> Result<Vec<Vec<i32>>> {
    // 009a311c: 見出しを除き、コメント列12以降は数値として読まない。
    crate::model::csv_rows(&database.source("Data/Gatyaitembuy.csv")?.3)?
        .into_iter()
        .skip(1)
        .map(|row| {
            row.into_iter()
                .take(12)
                .map(|cell| cell.parse().context("アイテム定義の不正なセル"))
                .collect()
        })
        .collect()
}
pub fn catalog(database: &crate::store::Database) -> Result<Value> {
    let names = crate::model::csv_rows(&database.source("res/GatyaitemName.csv")?.3)?;
    let mut items = BTreeMap::new();
    for (internal, definition) in definitions(database)?.iter().enumerate() {
        let id = definition[3];
        if id < 0 {
            continue;
        }
        let name = names
            .get(internal)
            .and_then(|row| row.first())
            .map(String::as_str)
            .unwrap_or("")
            .trim();
        if name.is_empty() {
            continue;
        }
        let path = format!("Image/gatyaitemD_{id:02}_f.png");
        let exists=database.connection.query_row("SELECT EXISTS(SELECT 1 FROM source_file WHERE path=? UNION SELECT 1 FROM asset_reference WHERE path=?)",[&path,&path],|r|r.get::<_,bool>(0))?;
        items.insert(id,json!({"id":id,"name":crate::model::plain_text(name),"icon":if exists {Some(path)}else{None}}));
    }
    let equipment = crate::stages::equipment_catalog(database)?;
    for item in equipment["items"]
        .as_array()
        .context("本能玉一覧がありません")?
    {
        items.insert(
            item["id"].as_i64().context("報酬IDなし")? as i32,
            item.clone(),
        );
    }
    let buy = crate::model::numeric_rows(&database.source("Data/unitbuy.csv")?.3)?;
    let make_character = |id, unit, form| -> Result<Value> {
        let limit = buy
            .get(unit as usize)
            .and_then(|r| r.1.get(19))
            .copied()
            .flatten()
            .context("キャラの上限なし")?;
        character(database, id, unit, form, limit)
    };
    // drop_charaは見出し付き。既存の入手経路と同じく先頭行を除く。
    for values in crate::model::csv_rows(&database.source("Data/drop_chara.csv")?.3)?
        .into_iter()
        .skip(1)
    {
        let id = values.first().context("入手報酬IDなし")?.parse::<i64>()?;
        let unit = values.get(2).context("入手キャラIDなし")?.parse::<i64>()?;
        if id >= 0 && unit >= 0 {
            let mut value = make_character(id, unit, 0)?;
            value["rewardKind"] = json!(i32::from(id >= 1100));
            value["gift"] = json!(format!("gift:{}", values[1]));
            items.insert(id as i32, value);
        }
    }
    for (unit, (_, values)) in buy.iter().enumerate() {
        for (column, form, kind) in [(23, 2, 2), (24, 3, 3)] {
            if let Some(id) = values
                .get(column)
                .copied()
                .flatten()
                .filter(|id| (10000..30000).contains(id))
            {
                let mut value = make_character(id, unit as i64, form)?;
                value["rewardKind"] = json!(kind);
                items.insert(id as i32, value);
            }
        }
    }
    let mut valkyrie = make_character(1002, 27, 0)?;
    valkyrie["gift"] = json!("gift:1002-special");
    valkyrie["rewardKind"] = json!(0);
    items.insert(1002, valkyrie);
    Ok(json!({"items":items.into_values().collect::<Vec<_>>()}))
}
fn character(
    database: &crate::store::Database,
    id: i64,
    unit: i64,
    form: i32,
    limit: i64,
) -> Result<Value> {
    let value:Option<(String,Option<String>)>=database.connection.query_row("SELECT name,icon_path FROM form WHERE unit_id=? ORDER BY form_index=? DESC,form_index LIMIT 1",params![unit,form],|r|Ok((r.get(0)?,r.get(1)?))).optional()?;
    let (name, icon) = value.unwrap_or_else(|| (format!("キャラ {unit}"), None));
    let (unit_name,rarity):(String,i32)=database.connection.query_row("SELECT f.name,u.rarity FROM form f JOIN unit u ON u.id=f.unit_id AND u.region=f.region WHERE f.unit_id=? AND f.form_index=0",[unit],|r|Ok((r.get(0)?,r.get(1)?)))?;
    Ok(
        json!({"id":id,"name":if form>=2 {format!("第{}形態進化権：{name}",form+1)}else{name},"icon":icon,"unit":unit,"form":form,"unitName":unit_name,"rarity":rarity,"limit":limit}),
    )
}

#[test]
fn atomic_receipt_and_display_are_independent() {
    let mut store = Store::memory().unwrap();
    let id = store.begin().unwrap();
    store.update_display(&Display { id: 1, count: 12 }).unwrap();
    let grants = [Grant {
        id: 1,
        amount: 3,
        source: "drop".into(),
        claim: Some("first".into()),
        notification: Some("${itemNum1} → ${itemNum2}".into()),
        character: None,
    }];
    let first = store
        .finish(id, json!({"mode":1}), &grants, &[("clears".into(), 1)])
        .unwrap();
    assert_eq!(first["rewards"][0]["before"], 12);
    assert_eq!(first["rewards"][0]["earned"], 3);
    assert_eq!(first["notifications"][0], "12 → 15");
    assert_eq!(store.finish(id, json!({}), &grants, &[]).unwrap(), first);
    let second = store.begin().unwrap();
    assert_eq!(
        store.finish(second, json!({}), &grants, &[]).unwrap()["rewards"],
        json!([])
    );
    store.update_display(&Display { id: 1, count: 0 }).unwrap();
    assert_eq!(store.items().unwrap()[0]["earned"], 3);
    let before = store.character(60).unwrap();
    let mut after = before.clone();
    after.owned = true;
    let id = store.begin().unwrap();
    let grant = Grant {
        id: 1100,
        amount: 1,
        source: "drop".into(),
        claim: None,
        notification: Some("first".into()),
        character: Some(CharacterGrant {
            before,
            after: after.clone(),
            gift: Some("gift:3".into()),
            seen: false,
        }),
    };
    store.finish(id, json!({}), &[grant], &[]).unwrap();
    assert!(store.claimed("gift:3").unwrap());
    assert!(store.character(60).unwrap() == after);
    let id = store.begin().unwrap();
    let grant = Grant {
        id: 1005,
        amount: 0,
        source: "drop".into(),
        claim: None,
        notification: None,
        character: Some(CharacterGrant {
            before: after.clone(),
            after: after.clone(),
            gift: Some("gift:3".into()),
            seen: true,
        }),
    };
    let result = store.finish(id, json!({}), &[grant], &[]).unwrap();
    assert_eq!(result["rewards"], json!([]));
    assert_eq!(result["notifications"], json!([]));
    assert!(store.character(60).unwrap() == after);
}
