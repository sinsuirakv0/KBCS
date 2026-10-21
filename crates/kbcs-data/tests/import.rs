use anyhow::Result;
use kbcs_data::{
    import,
    model::{animation_length, numeric_rows},
    source::{hash, safe_path},
    store::Database,
};
use serde_json::{Value, json};
use std::{
    fs,
    path::{Path, PathBuf},
    process::Command,
    time::{SystemTime, UNIX_EPOCH},
};

struct Fixture(PathBuf);
impl Drop for Fixture {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.0);
    }
}

fn write(root: &Path, name: &str, bytes: &[u8]) -> Result<()> {
    let path = root.join(name);
    fs::create_dir_all(path.parent().unwrap())?;
    fs::write(path, bytes)?;
    Ok(())
}

fn git(root: &Path, arguments: &[&str]) {
    assert!(
        Command::new("git")
            .arg("-C")
            .arg(root)
            .args(arguments)
            .output()
            .unwrap()
            .status
            .success()
    );
}

fn commit(root: &Path) {
    git(root, &["add", "."]);
    git(
        root,
        &[
            "-c",
            "user.name=KBCS fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "-qm",
            "fixture",
        ],
    );
}

fn source(root: &Path, region: &str) -> Result<()> {
    let header = json!({"schemaVersion":1,"datasetId":"fixture","buildId":"fixture-build","sourceRegion":region,"versionCode":1,"versionName":"fixture"});
    let mut settings = vec!["0"; 63];
    for (column, value) in [
        (20, "30"),
        (21, "10"),
        (23, "1000"),
        (25, "20"),
        (27, "12345"),
        (28, "1"),
        (29, "2"),
        (30, "2"),
        (31, "1"),
    ] {
        settings[column] = value;
    }
    settings[61] = "-1";
    settings[62] = "-1";
    let mut enemy = vec!["0"; 113];
    for (column, value) in [
        (0, "90"),
        (1, "3"),
        (2, "8"),
        (3, "8"),
        (4, "17"),
        (5, "140"),
        (6, "15"),
        (12, "8"),
        (37, "1"),
        (50, "-1"),
        (59, "1"),
    ] {
        enemy[column] = value;
    }
    let reserved = vec!["0"; 113].join(",");
    let mut unit_row = "100,3,10,8,15,140,50,75,0,320,0,0,0,8"
        .split(',')
        .collect::<Vec<_>>();
    unit_row.resize(119, "");
    unit_row[118] = "50";
    let data = [
        ("Data/t_unit.csv",[reserved.clone(),reserved.clone(),enemy.join(","),reserved].join("\n")),
        ("res/Enemyname.tsv","わんこ".into()),
        ("res/EnemyPictureBook_ja.csv","名前,説明<br>検証".into()),
        ("ImageData/000_e02.maanim","[modelanim:animation]\n1\n1\n0,0\n2\n-1,0\n46,0".into()),
        ("Data/unitbuy.csv", settings.join(",")),
        ("Data/unitlevel.csv", vec!["100"; 20].join(",")),
        (
            "Data/unit001.csv",
            ["100,3,10,8,15,140,50,75,0,320,0,0,0,8".to_owned(),"100,3,10,8,15,140,50,75,0,320,0,0,0,8".to_owned(),unit_row.join(",")].join("\n"),
        ),
        (
            "Data/SkillAcquisition.csv",
            "ID,typeID,skills\n0,1,27,3,10,5,0,0,0,0,0,0,1,1,-1,0,70,1,0,20,0,0,0,0,0,0,2,1,1,1"
                .into(),
        ),
        ("Data/SkillLevel.csv", "id,levels\n1,5,10,15".into()),
        (
            "res/SkillDescriptions.csv",
            "id,text\n1,速度<br>検証\n2,攻撃力".into(),
        ),
        ("res/nyankoPictureBook_ja.csv","\"日本編,第1章\",条件<br>確認,@,Lv10で進化,@,@,合計Lv30到達後,必要XPと素材,@".into()),
        ("res/GatyaitemName.csv","アイテム0\n実1\n種2\n素材3".into()),
        ("res/Map_Name.csv","0,検証レジェンド\n24000,検証マップ\n39000,検証PR".into()),
        ("res/StageName_RN_ja.csv","出現行の検証".into()),
        ("Data/Map_option.csv","ID,冠数\n0,4,0,100,150,200,300,0,0,0,0,0,0,0,0,0,0,0,0,末尾の説明".into()),
        ("Data/Stage_option.csv","0,3,-1,6,0,0,0,0,0".into()),
        ("Data/difficulty_level.tsv","0\t1.2".into()),
        ("Data/DropItem.csv","0,0.75,1,1,1,3,3,3,3,3,3,3,3,60,13,0,13,13".into()),
        ("Data/Gatyaitembuy.csv","0,0,1,0,1,0,7,0\n0,0,1,1,1,0,7,1\n0,0,1,2,1,0,7,2\n0,0,1,3,1,0,7,3".into()),
        ("Data/MapStageDataN_000.csv","1,0\n0\n50,3040,31,90,4,30,1,2,-1,-1".into()),
        ("Data/stageRN000_00.csv","6,0,0,0,0,0\n5800,500000,1,1,10,8,0,0,0,0\n2,0,-7,3,9,300,0,9,2,0,0,-17,1,3,\n2,1,0,1,1,100,0,9,0,100\n0,\n2,999".into()),
        ("res/StageName_RA_ja.csv","第1ステージ,第2ステージ,時刻報酬".into()),
        ("res/StageName_RPR_ja.csv","PR入手先".into()),
        ("Data/MapStageDataPR_000.csv","1,0\n0\n0,0,0,0,0,100,1000,1,-1,-1".into()),
        ("Data/MapStageDataA_000.csv","1,0\n0\n0,0,0,0,0,100,1000,1,0,50,1000,1,0\n0,0,0,0,0,100,1000,1,0\n0,0,0,0,0,100,1000,1,-2,-2,-2,-2,-2,-2,-2,0\n 1：末尾の説明".into()),
        ("Data/drop_chara.csv","reward,save,id\n1000,1,0".into()),
        ("Data/NyancomboData.csv","0,0,0,0,1,-1,-1,-1,-1,-1,-1,-1,-1,0,0\n0,-1,0,0,1,-1,-1,-1,-1,-1,-1,-1,-1,0,0".into()),
        ("res/Nyancombo_ja.csv","検証コンボ\n無効なコンボ".into()),
        ("res/Nyancombo1_ja.csv","攻撃力アップ".into()),
        ("res/Nyancombo2_ja.csv","【小】".into()),
        ("Data/NyancomboParam.tsv","10\t15\t20".into()),
    ];
    let mut files = serde_json::Map::new();
    for (logical, content) in data {
        let path = format!("{region}/Local/fixture/{logical}");
        write(root, &path, content.as_bytes())?;
        files.insert(logical.into(),json!({"path":path,"size":content.len(),"sha256":hash(content.as_bytes()),"sourceKind":"local"}));
    }
    let artifacts = [
        (
            "indexes/assets.json",
            json!({"header":header,"files":files}),
        ),
        (
            "site/characters.json",
            json!({"header":header,"units":[{"id":"000","forms":[{"name":"ネコ","description":"検証用"},{"name":"ネコ2","description":"第2"},{"name":"ネコ3","description":"第3"}]}]}),
        ),
    ];
    let generated = format!("generated/{region}/datasets/fixture-build");
    let mut descriptors = serde_json::Map::new();
    for (name, value) in artifacts {
        let bytes = serde_json::to_vec(&value)?;
        write(root, &format!("{generated}/{name}"), &bytes)?;
        descriptors.insert(
            name.into(),
            json!({"size":bytes.len(),"sha256":hash(&bytes)}),
        );
    }
    let manifest =
        serde_json::to_vec(&json!({"header":header,"artifacts":descriptors,"inputs":{}}))?;
    write(root, &format!("{generated}/manifest.json"), &manifest)?;
    let mut current = header;
    current["status"] = json!("verified");
    current["generatedPath"] = json!(generated);
    current["manifestSha256"] = json!(hash(&manifest));
    write(
        root,
        &format!("metadata/{region}/current.json"),
        &serde_json::to_vec(&current)?,
    )?;
    Ok(())
}

#[test]
fn import_is_offline_repeatable_region_safe_and_preserves_old_db_on_failure() -> Result<()> {
    let temporary = Fixture(std::env::temp_dir().join(format!(
        "kbcs-test-{}-{}",
        std::process::id(),
        SystemTime::now().duration_since(UNIX_EPOCH)?.as_nanos()
    )));
    let assets = temporary.0.join("assets");
    let root = temporary.0.join("data");
    fs::create_dir_all(&assets)?;
    git(&assets, &["init", "-q"]);
    source(&assets, "jp")?;
    source(&assets, "en")?;
    commit(&assets);
    let first = import::import(assets.to_str().unwrap(), &root, "jp", |_| {})?;
    let old = Database::open(&root, "jp")?;
    assert_eq!(old.search("jp", "ねこ", false)?.len(), 1);
    assert_eq!(old.search("jp", "０００", false)?.len(), 1);
    let form = old.form("jp", 0, 0)?;
    assert_eq!(form.raw.get(13), Some(&Some(8)));
    assert_eq!(form.raw.get(14), None);
    assert_eq!(form.attack_cycle, None);
    let talents = kbcs_data::talents::read(&old.connection, "jp", 0)?;
    assert_eq!(talents.len(), 2);
    assert_eq!(
        talents[0].values,
        [[10, 0, 0, 0], [8, 0, 0, 0], [5, 0, 0, 0]]
    );
    assert_eq!(talents[0].costs, [5, 10, 15]);
    assert_eq!(talents[0].description, "速度\n検証");
    assert_eq!(talents[1].values, [[20, 0, 0, 0]]);
    assert_eq!(talents[1].targets, ["red"]);
    assert_eq!(talents[1].limit, 1);
    let progression = kbcs_data::progression::read(&old.connection, "jp", 0)?;
    assert_eq!(progression[0].description, "日本編,第1章\n条件\n確認");
    assert_eq!(progression[0].stages.len(), 3);
    assert_eq!(progression[2].stages.len(), 3);
    assert_eq!(progression[0].stages[2].map, 39000);
    assert_eq!(progression[2].stages[1].stage_name, "第2ステージ");
    assert_eq!(progression[1].level, 10);
    assert_eq!((progression[2].level, progression[2].xp), (30, 12345));
    assert_eq!(
        progression[2]
            .materials
            .iter()
            .map(|material| (material.id, material.count))
            .collect::<Vec<_>>(),
        [(1, 2), (2, 1)]
    );
    assert!(progression[2].materials[0].icon.is_none());
    let combos = kbcs_data::combos::read(&old.connection, "jp")?;
    let enemies = kbcs_data::enemies::read(&old.connection, "jp")?;
    assert_eq!(enemies.len(), 2);
    assert_eq!(
        (enemies[0].id, enemies[0].hp, enemies[0].attack_cycle),
        (0, 90, Some(47))
    );
    assert_eq!(enemies[0].attacks[0].damage, 8);
    assert_eq!(enemies[0].description, "説明\n検証");
    assert_eq!(enemies[1].name, "敵 1");
    assert_eq!(enemies[1].attack_cycle, None);
    let stages = kbcs_data::stages::catalog(&old, "jp")?;
    assert_eq!(stages["maps"][0]["stars"], json!([100, 150, 200, 300]));
    assert_eq!(stages["maps"][0]["limits"][0]["rarities"], 6);
    let stage = &stages["stages"][0];
    assert_eq!(stage["spawns"].as_array().unwrap().len(), 2);
    let spawn = &stage["spawns"][0];
    assert_eq!(
        spawn["native"],
        json!([2, 0, -14, 6, 18, 300, 0, 9, 2, 0, 0, -17, 1, 3])
    );
    assert_eq!(spawn["health"], 0);
    assert_eq!(spawn["attack"], -17);
    assert_eq!(spawn["sourceRow"], 3);
    assert_eq!(spawn["raw"][14], "");
    assert_eq!(stage["drops"][0]["chance"], Value::Null);
    assert_eq!(stage["drops"][0]["weight"], 30);
    assert_eq!(stage["metadataRow"], 3);
    assert_eq!(stage["difficulty"], 1.2);
    let materials = &stages["maps"][0]["materials"];
    assert_eq!(materials["multipliers"], json!([0.75, 1.0, 1.0, 1.0]));
    assert_eq!(materials["counts"].as_array().unwrap().len(), 8);
    assert_eq!(
        materials["weights"],
        json!([13, 0, 13, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    );
    assert_eq!(materials["items"][1]["id"], 2);
    assert_eq!(materials["sourceRow"], 1);
    assert!(stage["rewards"].as_array().unwrap().contains(&json!(2)));
    assert_eq!(stages["rewards"]["3"]["name"], "素材3");
    assert_eq!(combos.len(), 1);
    assert_eq!(combos[0].effect, "攻撃力アップ【小】");
    assert_eq!(
        kbcs_data::combos::effects(&old.connection, "jp")?[0].values,
        [10, 15, 20]
    );
    assert_eq!((combos[0].members[0].id, combos[0].members[0].form), (0, 1));
    assert!(
        !form
            .properties
            .iter()
            .any(|property| property.key == "spirit")
    );
    let alternate_form = old.form("jp", 0, 2)?;
    let alternate = alternate_form
        .properties
        .iter()
        .find(|property| property.key == "alternate-respawn")
        .unwrap();
    assert_eq!(alternate.columns, [118]);
    assert_eq!(alternate.values, [Some(50)]);
    assert_eq!(
        first.database,
        import::import(assets.to_str().unwrap(), &root, "jp", |_| {})?.database
    );
    import::import(assets.to_str().unwrap(), &root, "en", |_| {})?;
    let before = fs::read(root.join("current.json"))?;
    let catalog: Value = serde_json::from_slice(&before)?;
    assert!(catalog["regions"]["jp"] != catalog["regions"]["en"]);
    write(&assets, "jp/Local/fixture/Data/unit001.csv", b"CORRUPTED")?;
    commit(&assets);
    assert!(import::import(assets.to_str().unwrap(), &root, "jp", |_| {}).is_err());
    assert_eq!(before, fs::read(root.join("current.json"))?);
    assert_eq!(old.form("jp", 0, 0)?.hp, 100);
    fs::rename(&assets, temporary.0.join("assets-offline"))?;
    assert_eq!(Database::open(&root, "jp")?.form("jp", 0, 0)?.hp, 100);
    Ok(())
}

#[test]
fn raw_columns_and_paths_do_not_silently_change() -> Result<()> {
    assert_eq!(
        animation_length(b"[modelanim:animation]\n1\n1\n0,0\n2\n-1,0\n2,0")?,
        Some(3)
    );
    let rows = numeric_rows(b"0,,7, // comment\n-1,2,3\n")?;
    assert_eq!(rows[0].1, vec![Some(0), None, Some(7), None]);
    assert!(numeric_rows(b"0,unknown").is_err());
    for path in ["../outside", "a/../b", "C:/x", "a\\b", "a//b"] {
        assert!(safe_path(path).is_err());
    }
    Ok(())
}
