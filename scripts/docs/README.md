# 生成・同期

sync-ui.pyはkbc-webの必要なHTML/CSS/ES modulesをコピーし、ネイティブの状態保存・配置・計算接続だけを小さいアダプタで変更する。元ファイルのSHAはui/upstream.jsonへ残す。参照元は編集しない。

sync-settings.pyはKBC-rakv0-assetsの検証済みcurrent→manifest→assets索引を検証し、採用元23ファイルのsize/SHAを検査する。treasureDataの効果定義とTreasure3の先頭11行から9章99グループを生成。AbilityDataの列2/3から通常Lv/＋上限、GatyaitemNameの60〜69から名前・説明を得る。Gatyaitembuyの効果種別2・施設IDも照合し、施設10件の順序を検証する。青玉PNGも採用元を検証して同梱する。

    python scripts/sync-settings.py D:/KBC/KBC-rakv0-assets
    python scripts/sync-ui.py D:/KBC/kbc-web D:/KBC/KBC-rakv0-lab/unit-db

settings-catalog.jsはASCIIで生成し、原本のパス/SHA、manifestと索引のSHA、ゲーム版・buildIdを保持する。未知の行数・索引の不整合は生成を失敗させる。DB更新とは別に定義を更新・照合する。通常起動にPythonや元checkoutは不要。

build.ps1は同梱uiをRustへ埋め込み、WebView2LoaderとMinGW依存を配布先へコピーする。UIだけの更新も再ビルドする。

0.1.6：sync-settingsはparam.tsvとCC_BaseParts_growth / CC_DecoParts_growthを追加し、26原本を検証する。easing=0・非減少・1/10000の範囲を明示検査し、未対応の曲線を黙って解釈しない。出典descriptorをsettings-catalog.jsへ保持する。
