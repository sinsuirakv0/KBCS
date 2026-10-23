# KBCS — KBC Simulator

にゃんこ大戦争のデータ閲覧・解析・編集・戦闘再現を目指すPC向けネイティブアプリ。JP15.7.2の味方・敵・全29系列のステージをSQLiteへ取り込み、ネットワークなしで検索・詳細閲覧できる。

## 実装済み

- 既存Webの罫線・表・アイコンを使ったPC向けUI。左にページ専用の絞り込み/形態一覧、中央にデータ、右に計算/表示設定、下に小さな情報欄。左右の開閉・幅調整と保存に対応。小さいホームボタン。
- 原本のsize/SHA-256・地域・版・採用元を検証したキャラ取り込み。
- キャラ・レア度・属性・特性アイコン、名前/ID・数値条件の検索、列ソート、形態切替、比較、CSV、原本表示。
- 本能・超本能の検索・数値反映、詳細での個別Lv設定、NP費用表示。
- 入手・進化条件、素材アイコン、にゃんコンボ一覧/5枠編成、成長グラフ、形態比較。
- 敵の検索・詳細・倍率/お宝設定・比較、各データ表のPNG保存。
- その他モーション（波動/小波動・烈波/小烈波・爆波・生き残り・バリア等）の分類/検索、素材単体と一連の演出再生。
- キャラ/敵のモーション再生、1F送り・速度・反転・ズーム、パーツの個別表示/単独表示、読込ファイルと分割画像の一覧、KBから専用/共通の魂への連続再生。
- 全29系列のステージ検索・マップ内一覧・冠切替・敵アイコン・出現条件・出撃制限・通常/重み/スコア/クリア回数報酬・固定編成・EX・特殊ルール・抽選候補の切替・城の開発素材の抽選回数/確率。勉強力/お宝・繰返し・コンボ・おかめを共通C++のXP計算へ反映。
- 章別のお宝99項目、施設10項目の通常Lv/＋値、土台・装飾の種類/Lv。折りたたみ・絞り込み・対象分の一括設定・自動保存。対応する表示補正へ即反映。
- 通常画面はWebと同じ数値表。原本・出典・注意書きは展開して確認。未知の列・空欄を保全。
- 検証済みDBの切替、旧DBの保全、リージョン別の公開ポインタ。
- C++20で体力・攻撃力・両方向の直接命中・メタルキラー・毒撃を計算し、特効・コンボ・土台/装飾を反映。現版ARM64で整数化を照合。出現待機の初期化・tick/commitと素材抽選も共用し、39000番台までのID/現在種別・参照先選択・出現行読込と、章/レジェンド/イベント/EXのXP入口を共用。各番台の専用進行と完全な戦闘の状態更新は未実装。

## Windowsでビルド・起動

Windows 11、WebView2 Runtime、Rust 1.95以上とC/C++20コンパイラが必要。WebView2はシステムのRuntimeを利用し、Electronやブラウザ本体を同梱しない。標準のMSVCターゲットならVisual Studio Build ToolsのC++デスクトップ開発を利用できる。現在の検証環境はRust 1.98.1 `x86_64-pc-windows-gnullvm` とLLVM-MinGW。

LLVM-MinGWを使う場合（パスは環境に合わせる）:

```powershell
./scripts/build.ps1 -LlvmBin 'D:/path/to/llvm-mingw/bin'
./.local/dist/0.1.17/kbcs.exe
```

スクリプトはreleaseビルド、WebView2Loader.dllと必要なMinGWランタイムDLLの同梱を行う。初回はCargo依存パッケージの取得にネットワークが必要。通常のMSVC環境でも `./scripts/build.ps1` で配布フォルダを生成する。MSVCでの実機検証は未実施。

GUIのホーム → データ管理でassetsのGitフォルダ、または `https://github.com/sinsuirakv0/KBC-rakv0-assets` を指定し「データを取り込む / 更新する」。ローカルGitは未コミットの追跡ファイル変更がないものを使用する。HTTP取得は公開リポジトリ向けで最初にcommit SHAを固定する。ネットワーク経路の全件導入の実測状況は[検証報告](docs/plans/initial-foundation.md)を確認する。

CLIでも同じ取り込み・照会を利用できる:

```powershell
./.local/dist/0.1.17/kbcs.exe import --assets '../KBC-rakv0-assets' | Out-Host
./.local/dist/0.1.17/kbcs.exe list --query 'ネコ' | Out-Host
./.local/dist/0.1.17/kbcs.exe show --id 0 --form 2 | Out-Host
./.local/dist/0.1.17/kbcs.exe verify | Out-Host
```

GUI用の実行ファイルはコンソールを作らない。PowerShellからCLI出力を表示する場合は上記のように `| Out-Host` を付ける。

DBの既定保存先は `%LOCALAPPDATA%/KBCS`。`--data-dir` または `KBCS_DATA_DIR` で変更できる。初回取り込み後の閲覧は原本フォルダにもネットワークにも依存しない。公式DB更新は `user/` 領域を一切操作しない。自作データ機能は未実装。

サイド画面で注釈しながら調整するプレビュー:

```powershell
./.local/dist/0.1.17/kbcs.exe preview --bind 127.0.0.1:4817 | Out-Host
```

[キャラ検索プレビュー](http://127.0.0.1:4817/pages/unit-search/) をCodexのブラウザパネルで開く。アプリと同じ埋込みHTML/CSS/JS・SQLiteを使用し、127.0.0.1だけで待ち受ける。通常のGUIはHTTPサーバーを起動せず、アプリ専用プロトコルを使用する。UIだけの変更もRust再ビルドで実行ファイルへ反映する。

検証はコンパイラのPATHを設定した状態で `cargo test --workspace --locked`。テストデータは一時フォルダだけに作成する。

## 構成と資料

|場所|役割|
|---|---|
|`crates/kbcs-app`|WebView2のネイティブホスト・HTTPプレビュー・CLI入口|
|`ui`|既存Webから必要なHTML/CSS/JSのみ再利用した画面|
|`crates/kbcs-data`|原本検証、Rust変換器、SQLite、検索・詳細取得|
|`crates/kbcs-bridge` / `native/kbcs-core`|薄いC ABI、C++20のビルド境界|
|`docs/architecture`|責務と将来の固定ステップ・headless設計|
|`docs/data`|取得元・スキーマ・更新・フィールド対応|
|`docs/research`|既存解析資産への索引|
|`docs/plans`|実装範囲・検証・次の作業|
|`research`|既存のGhidra索引・検索CLI・解析報告（保全）|
|`.local` / `target`|Git除外のローカル生成物・ビルド|

データは [KBC assets](https://github.com/sinsuirakv0/KBC-rakv0-assets) の生成索引と原本を使用し、上流の取得・復号基盤は [battlecats-apk](https://github.com/sinsuirakv0/battlecats-apk)。解釈・配色の参考は [kbc-web](https://github.com/sinsuirakv0/kbc-web)。Webの未完成なDBを確定したゲーム仕様として扱わない。

今後は専用の進行・解禁状態、モーション、C++戦闘コア、自作データ、APK出力、AI制御へ順に拡張する。今回の制限と次の変更箇所は[初期構築](docs/plans/initial-foundation.md)に記録する。

保存済みネイティブ資料は [research/README.md](research/README.md)、[全関数キャッシュ報告](research/docs/complete-report.md)、[Private Releaseの取得手順](research/docs/github-storage.md)を参照。
