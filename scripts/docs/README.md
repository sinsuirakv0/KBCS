# 生成・同期

sync-ui.pyはkbc-webの必要なHTML/CSS/ES modulesをコピーし、ネイティブの状態保存・配置・計算接続だけを小さいアダプタで変更する。元ファイルのSHAはui/upstream.jsonへ残す。参照元は編集しない。

sync-settings.pyはKBC-rakv0-assetsの検証済みcurrent→manifest→assets索引を検証し、採用元23ファイルのsize/SHAを検査する。treasureDataの効果定義とTreasure3の先頭11行から9章99グループを生成。AbilityDataの列2/3から通常Lv/＋上限、GatyaitemNameの60〜69から名前・説明を得る。Gatyaitembuyの効果種別2・施設IDも照合し、施設10件の順序を検証する。青玉PNGも採用元を検証して同梱する。

    python scripts/sync-settings.py D:/KBC/KBC-rakv0-assets
    python scripts/sync-ui.py D:/KBC/kbc-web D:/KBC/KBC-rakv0-lab/unit-db

settings-catalog.jsはASCIIで生成し、原本のパス/SHA、manifestと索引のSHA、ゲーム版・buildIdを保持する。未知の行数・索引の不整合は生成を失敗させる。DB更新とは別に定義を更新・照合する。通常起動にPythonや元checkoutは不要。

build.ps1は同梱uiをRustへ埋め込み、WebView2LoaderとMinGW依存を配布先へコピーする。UIだけの更新も再ビルドする。

0.1.6：sync-settingsはparam.tsvとCC_BaseParts_growth / CC_DecoParts_growthを追加し、26原本を検証する。easing=0・非減少・1/10000の範囲を明示検査し、未対応の曲線を黙って解釈しない。出典descriptorをsettings-catalog.jsへ保持する。


sync-equipment.py <assetsフォルダ> はresearch/verify/stages.Assetsの検証を共用してequipmentslot.csvを採用し、キャラ別の最大枠と元解放条件列をkbcs-data/resources/unit-equipment-slots.jsonへ保存する。版・buildId・元パス・SHAを保持し、UIカタログと編成保存時の検査が同じ定義を使う。通常アプリの起動時に原本取得やDB再構築を行う機能ではない。

sync-battle-ui.py <assets>は検証済みJP15.7.2からHUDのimgcutと採用元SHAをui/images/native-battle/manifest.jsonへ同期する。HUDのPNG本体もsize/SHA-256を検証して同じフォルダへ同梱する。既存DBに未収録でも再取り込みせず利用できる。キャラ画像は既存asset APIを使う。


0.1.30のsync-battle-ui.pyはimg001_ja/img002_ja/mapicon/uni/img100_ja/img015の6PNG、各imgcut、GatyaitemName.csvの6アイテム説明とlocalizable.tsvの通常スピード説明を検証して同期する。uniだけUnit/、他はImage/。生成manifestは版/buildId・元パス・SHAを持つ。不要なアトラスは同期対象へ加えない。


sync-stage-music.py --revision <40桁SHA> はGitHub assetsの固定commitからcurrent/manifest/assets index/Sound_settingを検証し、APK同梱BGM18件を既存補完索引へ加える。size/SHA、元パス、曲ごとのrevision、MIMEとloopを保持。大きい索引の生成用キャッシュはresearch/.local/music-indexで、配布物へ含めない。公式DBを書き換えるスクリプトではない。

## 2026-10-28: 出撃準備ボタン

sync-battle-ui.pyのアトラスへimg031_jaを追加し、以前に追加された結果/通知画像も再生成時に保持する。007802c0のcontext+0x138と007acf88のdrawからcut10/11を採用した。コピーしたPNG・imgcutの出典/size/SHAはnative-battle/manifest.jsonへ保存する。原本は変更しない。配置と局所ARM比較はui/docs/stage-sortie.mdとresearch/verify/sortie_ui.pyを参照する。


## 2026-10-29: 自動ビルド・配布

setup-windows-ci.ps1が検証済みLLVM-MinGW 20260922をSHA確認後に導入する。package.pyはビルド済みtargetをWindows x64/Mac arm64/Mac x64用ZIPへまとめ、CPU種別・単独起動・SHAを検査する。UIとresearchの生成は実行しない。workflow・署名・本体更新との命名契約は[ビルド設計](../../crates/kbcs-app/docs/build.md)を参照。

publish-release.pyは全CPUの版/commit/ZIP-SHAとアップロード先のSHAを照合後、タグのドラフトを公開開発版へ変更する。公開済みリリースは更新しない。
