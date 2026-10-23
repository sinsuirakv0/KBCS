# 再開メモ（2026-10-23 / 0.1.17）

その他モーションを通常プレビューへ反映済み。最新は`.local/dist/0.1.17/kbcs.exe`、schema8/importer12、ABI2/ruleset1507021。4817/PID13584。DBは`C:/Users/ABC/AppData/Local/KBCS/official/jp-c59d3381716e75249c6ebda4a38a00da42915248a1e7ee6849af2a1e011769ca.sqlite`。旧snapshotを保持。詳細は[effect-motion-workspace.md](effect-motion-workspace.md)。

味方・敵・その他で同じエンジン。433モデル中386件を解決、47件は素材対応未確認。波動/烈波/爆波の既存一連演出とLv、生き残り・バリア・城バリア・悪魔シールドを追加。ファイル/分割/パーツ操作を流用。テスト18＋compile_fail1、代表16素材と既存演出境界72件、実ブラウザー確認済み。

姿勢評価のC++移植と完全な戦闘状態は残る。外部ホスティング・PC終了は未実施。ソースのGitHub Pushは2026-10-23のユーザー指示で承認済み（再確認不要）。試験4822は停止済み。再開前に新規の指示を確認し、広い追加機能を推測しない。

テスト用Windowsアプリは`.local/dist/0.1.17-app/KBCS.lnk`。選択パーツの黄色い枠は初期OFFで、右の「選択枠を表示」で切り替える。調査はREADME、docs/architecture、docs/data、各領域docsから開始する。Gitへはソース・設計・検証スクリプト/fixtureを含め、ローカルDB・実行ファイル・解析キャッシュは含めない。

---

# 再開メモ（2026-10-23 / 0.1.16）

モーションの初期ワークスペースを公開済み。最新は`.local/dist/0.1.16/kbcs.exe`、schema8/importer10、ABI2/ruleset1507021。通常previewは4817/PID15960。DBは`C:/Users/ABC/AppData/Local/KBCS/official/jp-71e42b90c517b9103aa1a9dcedf592fb2b380646547b6d7f7fcba1f493124423.sqlite`。旧snapshot/ポインタを保持。最新の関数・UI・範囲は[motion-workspace.md](motion-workspace.md)。

- ステージ検索の出現敵列は初期非表示。右の表示設定で切替可能。
- キャラ/敵の再生、1F/10F、反転/ズーム、パーツの個別/子/単独表示、読込原本と分割画像一覧、KB→通常/専用魂を追加。
- モデル2950件・アニメーション11744件・スプライト2950枚をオフライン保持。PNG選択はimgcutの制作PCパスを使わず、現版と同じstemを採る。
- ユーザーは「最近モーションは変わっていないので軽めの検証でよい」と指示。代表6素材120姿勢と実ブラウザーを確認。workspace18＋compile_fail1、clippy、CLI/release、importer10のステージ全件回帰が通過。
- 姿勢評価は既存JSの整数評価器。C++はKB/魂の時計と変位を共用。姿勢C++化と戦闘全状態は今後。既存のnative解析資料は版/SHAを混同せず保全する。
- ブラウザー検証はCUAのみ。Windows Store PythonはAppDataが仮想化されるので、通常DB確認はbundled Pythonを使う。

# 0.1.15までの再開メモ（履歴）

0.1.15で全29系列の閲覧DBとUIを通常保存先へ公開済み。DB完成＋ローカル公開の依頼は完了。GitHubへの書込・外部ホスティングは行っていない。

## 現在の動作版

- `.local/dist/0.1.15/kbcs.exe`、ABI2 / ruleset1507021、schema8 / importer9。
- 通常プレビューは127.0.0.1:4817、PID18548で非表示起動。終了/更新時は実行パス・preview引数・窓を再確認。試験用4820/4821/4822は実行元を確認して停止済み。
- 実使用DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-fb87935b9bee241e538b0222a3c4af6739a54c16d6a47573d1f809a7cb165411.sqlite`。旧DBは保持、前ポインタは`.local/current-before-0.1.15.json`。
- 同版原本6333戦闘定義62488行、一覧1298マップ6476面、報酬12194行、候補関係3088件。未来編144面315スコア報酬、固定編成10preset、本能玉164報酬名/3層アイコンを接続。
- `research/verify/all_stage_database.py`が全定義/原本7631件/一覧メタ/物理列/全報酬を比較。0番台324面2924行も回帰一致。レポートは`research/.local/all-stage-database-0.1.15.json`と`stage-database-0.1.15-band0.json`。
- workspace17件＋compile_fail1、clippy全target、JS構文、release/CLI verify、実ブラウザーを確認。全29系列の検索と候補内ANDは`.local/verify-stage-search.mjs`。本能玉、固定編成、未来編、Pt、L/D切替、ゾンビ襲来を実画面で確認。
- Windows Store版pythonはAppDataを仮想化して通常DBが見えない。通常DB検証では`C:/Users/ABC/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`を使用する。

## 関数と残る範囲

`stages/importer.rs`→全定義/一覧/4種類報酬、`extras.rs`→補助設定/固定編成/候補、`rewards.rs`→本能玉の原本名/アイコン。`search_catalog`→検索索引、`catalog_map`→マップ詳細、`variant`→許可候補。ServiceのstageExperience→bridge→C++で章/内部種別を保つ。設計はdocs/dataとcrates/kbcs-data/docs。

原本にない2面（日本編ゾンビ2/3章の月）は欠測表示、一覧外7定義は未収録の統率力/XPをNULLにして保持。廃止ID1002/未対応進化権10214等の名前を捏造しない。閲覧DB完成と、全戦闘/期間解禁/クエスト抽選/迷宮編成消耗/報酬実付与・セーブの実装完成は区別する。次の実装では保存済み疑似コードの版/ABI/SHAを照合し、専用状態を順に追加する。

## 以前の動作版（0.1.14の記録）

- `.local/dist/0.1.14/kbcs.exe`、ABI2 / ruleset1507021、schema7 / importer8。
- 通常プレビューは0.1.14で127.0.0.1:4817、今回PID19112で非表示起動。終了・更新時は実行パスと引数を再確認する。旧0.1.13/PID14152は実行元・引数・非表示窓を確認し停止/WaitForExit済み。
- 実使用DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-e63a79e7efc54c515d1e9f8ae3a3f9d8b50665ce8b798cf27333139eab0ad1bc.sqlite`。
- 旧DBは保持。切替前ポインタは`.local/current-before-0.1.8.json`。検証用データ`.local/stage-0.1.8`、比較結果`research/.local/stage-database-0.1.8.json`。

- 今回は共通C++/APIの更新で、UIソースは変更していない。旧画面確認画像は`.local/stage-materials-0.1.8.png`。新しい敵基礎値を旧Web表示へ全面接続する作業は残っている。

## 完了した範囲

0番台49マップ・324面・出現2924行・冠196値・原本378件を全件比較。0.1.7のXP、検索と表、冠、左右パネル、共通お宝・施設は維持した。

0.1.8はDropItemの49プロフィール・196冠係数・392回数枠・392重みを保存。素材IDはGatyaitembuyの種別7/スロットを同版の006f308cと16件照合した。抽選回数1568条件、2段階抽選7条件が現版命令と一致。C++のmaterials::plan/pickを共用し、表示は一様独立抽選の理論確率。素材の所持数加算や乱数器全体は未実装。素材は報酬検索へ追加し、詳細の素材表は初期状態で折りたたむ。

009eadc8の待機初期化と敵城行の消費を局所実行し、全324面と境界6条件を確認。loaded列2の負待機を維持、敵城の最初の一致行だけwait=1/spawned=1、生成helper失敗時にも消費する。stage::initializeへ追加した。通常出現のcommit成功時限定規則と混ぜない。敵個体の生成・HP/姿勢や戦闘全体の初期化は未実装。

workspace7テスト、clippy全target、実データ比較、JS構文、BOM、release/CLIを確認。画面はN000の1冠2回/2冠3回、素材確率・期待数、レンガで47マップ312面、画像欠損とconsole警告/エラーなしを確認した。素材名原本は正常なUTF-8で、ターミナルの文字化けを原本破損と誤認しない。

## 0.1.9の追加

- 敵HP/各攻撃：行倍率で四捨五入→冠で切捨て→クリスタル不足分の整数加算。敵城の攻撃だけ冠を除外。enemy_stats.pyで境界48、全2924行×4冠を覆う8416プロフィール。C++のenemy::statとServiceのenemyStatsへ接続。通常Webの合成倍率とは212プロフィールで異なる。
- 0番台通常報酬：kind3/通常フラグ0/特殊分類0/mode−1または1。取得済みの先頭が当選した場合、通常は次候補、レーダーは補助フラグ1/候補なしで打切り。比較乱数は取得済み・レーダーでも消費。境界48、実324面の2592条件。reward::legend_pickとServiceのlegendRewardsへ接続。所持数や取得済み状態の実書込み、レーダー返却は未実装。
- C++へ現版報告の8464敵値/2640報酬選択を再投入して全一致。bridge7+data2+Service1のworkspace10テストとclippy全targetが通過。release/CLI verify、同版DBの継続利用、ループバック待受、埋込UIとBOMも確認。Serviceは共通handleへfixture96条件を直接渡し、全出力・件数・ABI/ruleset・未知キー拒否を確認する。
- 完全な報告はresearch/.local/enemy-stats-1572.jsonとrewards-1572.json。小fixtureだけ追跡。関数関係・入力・制御helper・限界はnative/kbcs-core/docs/stages.md。

## 0.1.10：外部評価と1000番台

- 対応表と関数の関係はnative/kbcs-core/docs/audit-20261022.md。評価の数値カーネルの指摘と、ランタイム未実装を区別した。
- 非0明示シードのxorshift13/17/15をrandom.cppへ追加。範囲1も状態更新する。実命令32段階、個体枠/レイヤー5条件、生成成否後の間隔/seen2条件を確認。生成全体やOSのseed0初期化は対象外。
- Rust tickの結果をPendingSpawnとし、commit(self)で1回消費する。生C ABIも生成数上限/撃破/城を再検証するが、C++所有ランタイムでの候補管理は今後必要。
- 有効な超獣/超賢者/怪人の倍率0を拒否。stat/命中/毒撃は成功時だけ出力へ代入する。攻撃種別param_6=0/1/2の準備を別入口に追加。命中48条件×21段階、準備18条件をnative-vectorsで比較。対象外/呪いの全状態入口、全個体初期化、波動等の伝播は未実装。
- workspace11テスト、compile_fail 1件、clippy全targetが通過。releaseを.local/dist/0.1.10へ配置し、既存DBのCLI verify（importer8/ABI2）成功。通常プレビューを更新した。既存UIとschema7/importer8は変更していない。
- events.pyでS000..S435、メタ1213面/RS定義1215件、出現11024行・有効冠566値を棚卸し。報酬mode7種。孤立定義S268-1/S325-5、数値「.」1セル、数値終端なし206ファイルを原文のまま記録。S279-0の撃破解禁30/90/210も確認。詳細はresearch/docs/stages/01000.md、大きい報告はresearch/.local/stages-1572-band1000.json。DB/UI公開はまだ行わない。

## 0.1.11：1000番台の報酬・XP

- 設計と再実行はnative/kbcs-core/docs/event-rewards.md。event_rewards.pyで候補数決定を含めて9704条件を照合した。通常mode−2/−1/0/1/2はstage_pick、重みmode−3/−4はweight_total→乱数1回→weight_pickを使う。負modeの通常候補数は1。レーダーでも比較乱数を消費する。
- 先頭報酬分類0の保存フラグと分類1/2/3の所持判定を区別してacquiredを解決する。実205IDと境界の分類getter、4分類の所有状態192条件、mode2だけ冠別に使う取得済みバイトgetter/setter8条件を確認。所持判定の全内部状態・特殊フラグ1の格納元は今後。
- XPはkind1で×9/クリア数減衰を通らない。EventInputはclearsなし。6境界と実2426条件を、減衰helperを呼ぶと失敗する設定で照合。共通C++は以降の勉強力/お宝/コンボ/おかめの整数化を共有した。
- 配布版は.local/dist/0.1.11。releaseビルドと実DBのCLI verify（importer8/ABI2）成功。UIの変更はない。
- C++へ通常選択656・正常重み56・XP2426を再投入して全一致。小fixtureは通常60/重み67/XP6。11枠使い切りはネイティブでは乱数を消費して候補なしになるが、製品APIでは拒否。workspace11件とcompile_fail 1件、clippy全targetを維持する。
- mode−2の追加報酬、mode−3の履歴、実付与/所持数、解禁/期間/連戦は未実装。DB/schema/importerとUI公開範囲は0番台のまま。0.1.11は共通計算の更新であり、1000番台全体の完成ではない。

## 0.1.12：スコアと重み確定（2026-10-23）

- 追加セル群は原本15列=1で有効なスコア報酬。309面（mode−2が301/−3が7/−4が1）。game+83e74の計測値からスコアを計算し、oldBest<threshold<=scoreの各枠を原本順に要求する。33境界と実4156条件を局所実行した。elapsedを画面の秒と推測しない。
- score::calculate→kbcs_core_stage_scoreはscore/best/improved/reward_maskを返す。付与helperが1ならスコアの結果行を除外するが最高は更新する。保存更新は要求の処理後。
- reward::weight_finish→kbcs_core_reward_weight_finishはmode−3の初回だけ履歴記録と付与を要求し、既記録ならスキップ（レーダー時打切り）。mode−4は毎回付与要求。履歴は付与前に書き、付与結果1でも重み報酬の結果行を残す。既存treeノードで実getterと本体48条件を実行し、書込み順も確認した。
- 大報告はresearch/.local/stage-score-1572.json、reward-finish-1572.json。小fixtureは34/48件。C++へ4189スコア/48確定を再投入して全一致。workspace12件（bridge9/data2/Service1）とcompile_fail 1件、clippy全targetが通過。
- releaseを.local/dist/0.1.12へ配置。実DBのCLI verifyはimporter8/ABI2で成功し、同じDBを継続利用する。UIソースの変更はない。
- 関数・単位・入力責務はnative/kbcs-core/docs/stage-score.md。新規tree挿入、実所持数の上限/変換/解放、保存先選択、時計の加算元、期間/解禁/連戦は未実装。schema7/importer8とUIは維持。

## 0.1.13：保存先・所持数・時計・EX（2026-10-23）

- 詳細はnative/kbcs-core/docs/inventory-ex.md。通常取得済みはヘッダー列1（0..399）、スコアは列2（0..199）。009a3a30の正規化245条件、実通常報酬9704条件を再確認。元modeで候補数を決定後、保存番号なしの取得済み処理を省く。
- 旧309スコア面のうち8面は処理対象外。有効301面3988条件＋時間境界33、無効8を検証。旧報告はresearch/.local/*-before-save-context.jsonとして保持。旧0.1.12の4156件は保存先を人工的に与えた数値比較であり、有効面数を示さない。
- score::advanceはphase0の受理更新で1加算、30000で飽和。現版24境界を照合。壁時計の秒や外側の速度を確定したものではない。
- inventory::addは通常数値245定義の2205条件、実報酬入口374条件、多段変換2条件を照合。所持数を含む合計への後続倍率も再現。残る30定義の専用処理、通知、特殊キャラ、永続化は未実装。
- transition::selectは追加候補→直接EX確率→当選時の面抽選の順で同じRandomを借用。現版RNGを実行し、1213面×6seedの7278条件、全EX_group選択器340条件、小fixture29件の出力/消費順/更新後seedを比較。
- EX_optionは抽選と別の条件付きRE表差替え。009a3a30は有効フラグ等を確認し、mapの有効面vectorが非空ならRE表を読み、各面membershipが真の行だけ差し替える。有効vectorの生成は未確認。3設定行だけを見て全ステージへ差替えを適用しない。
- 現版報告をC++へ再投入し、所持数2579/通常報酬2656/スコア4021/EX7647件が一致。.local/verify-stage-0.1.13.cppが再投入用。workspace14件とcompile_fail 1件、clippy全targetが通過。
- releaseを.local/dist/0.1.13へ配置し、実使用DBへのCLI verifyが成功（importer8/ABI2）。通常プレビューも同じDBで更新した。
- DBはschema7/importer8の同じsnapshot。UI公開は0番台のまま。S取込みにはEOF終端・「.」・孤立2定義・通常/重み/スコアの区別と保存番号の根拠を必要とし、単純なglob拡大をしない。

## 0.1.14：39000番台まで（2026-10-23）

- research/verify/stage_bands.pyは6333戦闘定義・62488有効出現行、終端含む67911読込行（異なる入力47248）を現版00a06ae4へ照合した。原本hashと物理行をresearch/.local/stage-bands-1572.jsonへ保存。真レジェンドの一覧外5定義、Sの2定義、迷宮113テンプレートを保持。
- stage_sources.pyはID0..39999の40000条件、現在種別168、参照先選択144。クエストは抽選済みRN参照、迷宮は選択済みテンプレート、EXは専用座標を要求。参照元を推測して既定値で埋めない。
- band_experience.pyは全種別と章/EX304境界、実表10788条件。9倍/4回/5の減衰はkind0/−9/−22、章は面から元値生成/13回/14の減衰、他とEXは元値のまま。既存の補正を共有し旧ABI入力は維持する。
- RA068-1/RSR021-2は再出現max<min。原本は非正boundで0、乱数状態を進めずminを保存する。C++/Rust乱数とtick/commitを修正し、実RNG付きの2条件を回帰追加。bound1は消費する。
- C++再投入は出現行47237、ID40000、現在種別168、XP11092で全一致。.local/verify-bands-0.1.14.cpp。小fixtureは出現行106、ID境界91/参照先144/現在種別168、XP304。
- 最終workspace17件とcompile_fail 1件、clippy全target、差分/日本語BOM、配布releaseと実使用DBのCLI verify（importer8/ABI2）が成功。プレビューを0.1.14へ更新し127.0.0.1:4817のみの待受を確認。
- 共通C++: map.cppのdecode/encode/current_kind/row_decode、stage.cppのstage_experience。Rust: stage_source::{decode,encode,current_kind,resolve}、stage::Row::decode、experience::stage。DB schema7/importer8とUI公開範囲は変更しない。

## 次に調べる箇所

1. enemy::statを敵検索/詳細・ステージ個体の表示へ接続する。出現行倍率と冠を保存状態で分けて受け渡し、旧Webの合成倍率へ戻さない。今回まだUIへ全面反映していない。
2. 0番台の報酬005d996cの006e34b0以降の実付与、取得済み保存の冠別格納、レーダー返却、素材所持数加算。通常分岐の結果を全報酬形式へ一般化しない。
3. 009eadc8の残る個体初期化、冠倍率の個体HP/攻撃への適用順、コンテニュー。今回の2区間の検証を全初期化へ拡大解釈しない。
4. 006d6d04のボス2だけの005c1404追加イベント。ボス1/2の衝撃波経路は静的確認済みだがフレーム全体の実行ではない。
5. 1000番台の残る30アイテムの専用処理・特殊キャラ、EX_option有効面vectorの生成、解禁/期間/EX戦闘初期化を確認する。スコア/重みの要求と実付与を混ぜず、別番台を検証済みにしない。

現版はJP15.7.2 ARM64 / 1507021、SO SHAはresearch/docs/stages/README.mdとresearch/.local/reference.jsonで確認する。MCPの旧15.7.1 ARM32、読み取り専用の参照リポジトリ、既存Ghidraプロジェクトを混同・変更しない。GitHubへの書込は個別承認が必要。

## GitHub保存と再起動後の再開

前回の保存先は既存の非公開リポジトリsinsuirakv0/KBCS。0.1.8のソースはmainの1cbd7d6、動作版と検証結果はRelease `kbcs-v0.1.8`へ送信・ハッシュ照合済み。今回の0.1.9〜0.1.14は未コミット・未送信。既存の大容量ネイティブ資料はRelease `native-v15.7.2`を維持する。実使用DBと旧snapshotはローカルに保全し、必要なら同じassets版から再生成できる。

```powershell
./.local/dist/0.1.14/kbcs.exe preview --bind 127.0.0.1:4817 | Out-Host
```

## 再実行

```powershell
$env:CARGO_TARGET_DIR='C:/Temp/kbcs-build-20261021'
$env:PATH='D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin;C:/Users/ABC/.rustup/toolchains/stable-x86_64-pc-windows-gnullvm/bin;'+$env:PATH
cargo test --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
python research/verify/stage_database.py --data-dir D:/KBC/KBCS/.local/stage-0.1.8
python research/verify/materials.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_start.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/enemy_stats.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/rewards.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/rng.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/events.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs
python research/verify/event_rewards.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/experience.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_score.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/reward_finish.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/inventory.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/ex_transition.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_sources.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/stage_bands.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
python research/verify/band_experience.py --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs --publish
./scripts/build.ps1 -LlvmBin 'D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin'
```

cargo fmt後は日本語ファイルのBOMを復元する。起動中の配布exeは上書きせず、対象の検証・停止・WaitForExit後に更新する。0.1.8までの基盤は前回コミット済み。0.1.9〜0.1.14の変更は未送信。今回の変更をreset・削除しない。この再開作業ではcommit・GitHub書込は行っていない。

公開画面の確認画像は`.local/stage-db-0.1.15.png`。DB/実行ファイルのSHAと旧snapshot保全の記録は`.local/publication-0.1.15.json`。

公開確認画像は`.local/motion-workspace-0.1.16.png`。DB/実行ファイルのSHAと旧snapshot保全は`.local/publication-0.1.16.json`。試験用4820/4821は停止済み。
