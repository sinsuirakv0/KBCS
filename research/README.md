# Ghidra解析キャッシュ基盤 v1

最新版の確認・取得、Ghidraの一括抽出、SQLite検索をローカルで実行します。
初期版はユーザー指定の15.7.2、対象は統合APK内のARM64版 `libnative-lib.so` です。
15.7.1の既存MCPプロジェクトは参照用で、切替・再解析・変更を行いません。

## 全関数の参考資料を作成・再開

```powershell
$env:PYTHONPATH = (Resolve-Path research).Path
python -m indexer.complete --config research/.local/config.json --cache <初期キャッシュの絶対パス>
```

初期キャッシュの隣に `-complete` 付きの独立リビジョンを作り、自動解析・全内部関数のデコンパイルを行います。thunkも対象です。解析時間・バッチ時間・1関数の時間上限は0（制限なし）に設定します。メモリ上限と逐次処理は維持し、失敗を無限に再試行しません。
解析状態が変わるため、初期100件の疑似コードはそのまま移植せず完全版で作り直します。完了済みの完全版を再実行した場合は保存済み結果を再利用します。復旧試行もチェックポイントで保持し、同じ設定で失敗分を自動反復しません。明示的な再試行にはrun.pyの --retry-failed を使います。
自動解析の完了状態、プロジェクトZIP、索引、デコンパイルのジャーナルを段階的に保存し、中断後は同じコマンドで再開します。プロセス実行中に同じ完全版を別プロセスから開かないでください。

完了した参考資料は `.local/reference.json` に登録します。以後は長いパスを指定せず、Ghidraを起動せずに検索できます。

```powershell
python research/cli/cache.py stats
python research/cli/cache.py find appUpdateDraw
python research/cli/cache.py strings attack
python research/cli/cache.py code <アドレス>
python research/cli/cache.py callers <アドレス>
python research/cli/cache.py callees <アドレス>
python research/cli/cache.py failures
python research/cli/cache.py external
```

完全版ディレクトリの `catalog.tsv` は全関数・名前・状態・ファイルへの索引、`code/` は関数別の疑似コード、`external-functions.tsv` は外部関数の一覧です。デコンパイル失敗時は理由と命令一覧を `assembly/` に残し、`assembly <アドレス>` でも参照できます。
疑似コードの保存に不要な構文木の転送は無効にし、大きな関数の応答量を抑えます。失敗分だけを構文木なしの標準設定、推論・分割を抑えたconservative設定、読み取り専用データの推論も抑えるminimal設定の順で有限回再試行します。追加設定で復旧した関数はconfidence=lowとして区別します。
WindowsではJVMヒープとは別に、ネイティブデコンパイラのPrivate Bytesを監視します。既定1536MiBを超えた場合は対象の子プロセスだけを停止して記録し、他の関数と復旧処理へ進めます。時間上限の代用ではなく、PCのメモリを使い切らないための保護です。
外部関数の実装は対象SOに含まれません。疑似コードの型・変数名・制御構造はGhidraによる復元であり、意味の確認状態は `unreviewed` として保持します。

## 必要な環境

- Python 3.11以上。追加Pythonパッケージ不要。
- 認証済みGitHub CLI `gh`。Private repositoryへの読取権限。
- Ghidra 12.1.2と対応するJDK。今回の環境はJDK 21。
- 既存APK取得repositoryの `tools/battlecats-cryptor/lib/apktool.jar`。

このディレクトリではなく、リポジトリのルートを作業ディレクトリにします。

```powershell
$env:PYTHONPATH = (Resolve-Path research).Path
New-Item -ItemType Directory -Force research/.local | Out-Null
Copy-Item research/config.example.json research/.local/config.json
# config.jsonのGhidra/JDKパスを環境に合わせる。
python -m indexer.apk --apktool D:/KBC/battlecats-apk/tools/battlecats-cryptor/lib/apktool.jar --java D:/KBC/tools/jdk-21.0.11+10/bin/java.exe
```

APK取得は毎回GitHub上の `jp/version.json` を読みます。版・manifest・SHA-256が一致するローカルAPKは再ダウンロードしません。Releaseがなければworkflow履歴を保存して停止し、workflowを実行しません。

初回解析では取得結果の版番号を使います。既存の同一キャッシュがある場合は再解析しません。

```powershell
$version = Get-Content research/.local/apk/150702/version.json -Raw | ConvertFrom-Json
python -m indexer.run --config research/.local/config.json init-latest --verified "research/.local/apk/$($version.compactVersion)/verified.json" --architecture arm64-v8a
$cache = (Get-ChildItem "research/.local/cache/$($version.versionName)/arm64-v8a" -Directory | Where-Object Name -NotLike "*-complete").FullName
python -m indexer.run --config research/.local/config.json decompile --cache $cache --limit 30
```

`150702` は今回の取得結果の例です。次回は取得コマンドが報告するcompactVersionのフォルダを指定します。
初回の30件と追加70件、合計100件の試験は実施済みです。通常運用は必要な関数だけを指定します。`--limit` のバッチ指定は未保存の別の関数を追加するので、既存キャッシュで再実行すると試験件数が増えます。

```powershell
python research/cli/cache.py --cache $cache find Battle
python research/cli/cache.py --cache $cache strings attack
python research/cli/cache.py --cache $cache pending
python research/cli/cache.py --cache $cache callers 00123456
python research/cli/cache.py --cache $cache callees 00123456
python research/cli/cache.py --cache $cache refs 00123456
python research/cli/cache.py --cache $cache code 00123456 --max-chars 4000
python research/cli/cache.py --cache $cache stats
python -m indexer.run --config research/.local/config.json decompile --cache $cache --address 00123456
```

アドレスは索引の値をそのまま指定します。上記アドレスは書式例です。
検索は既定10件、最大100件。`--limit` はサブコマンドの前に指定します。
疑似コードは既定4000文字に制限します。全文は報告されたローカルファイルを必要時に読みます。
`pending` は失敗も含む未キャッシュ一覧です。失敗の再試行には `decompile --retry-failed` を明示します。
外部関数はデコンパイル対象から除外します。初回100件試験用キャッシュの自動解析は時間上限により未完了でした。完全版では自動解析を完了させてから索引・全件キャッシュを作ります。`stats` の `analysis_timed_out` と `analysis_marked_complete` でも区別できます。

## 既存解析の再利用

`prepare` は既存MCPのプログラムをGZFへ書き出すか、既存のGZFバックアップを受け取ります。
元プロジェクトを保存・切替せず、コピーに対して `-noanalysis` で処理します。

```powershell
python -m indexer.run --config research/.local/config.json prepare --binary D:/path/libnative-lib.so --version 15.7.1 --version-code 1507010 --architecture armeabi-v7a --evidence D:/path/evidence.json --snapshot D:/path/backup.gzf
python -m indexer.run --config research/.local/config.json index --cache D:/path/cache
```

evidence.jsonは `sha256`、`versionName`、`versionCode` と照合根拠を記録します。
Ghidra内の実行ファイルSHA-256とも照合し、パス名だけで版を断定しません。
今回の旧版はバックアップのみで、初期データベースへ取り込みません。

## 保存場所と制約

- `.local/apk/<compactVersion>/`：APK・取得根拠・ライブラリ一覧。
- `.local/cache/<version>/<architecture>/<SO SHA-256>/`：索引、SQLite、疑似コード、計測、プロジェクトZIP、独立プロジェクト。
- `.local/backups/`：既存MCPの参照用バックアップ。
- `ghidra-workspace`：Ghidraの先頭ドット付きパス制約を避ける、`.local/cache`へのjunction。実体は.local内。これもGit除外。

既存MCPのGZFは新規Ghidraプロジェクトへインポートして復元します。新規解析の `backup-project.zip` は `project/` へ展開すると復元できます。稼働中のプロジェクトを上書きせず、コピー先で復旧してください。
一括処理は1プロセスに限定。既定値はJVM 512MB、1関数20秒、自動解析の中止要求600秒、バッチ900秒です。Ghidraが中止要求を処理するまでの遅延はあり得ます。
中断済みの結果はJSONLからSQLiteへ復元されます。保存済み関数はGhidraへ再要求しません。
初期解析後の索引生成で中断した場合は、保存済みプロジェクトを再解析せず再利用します。プロジェクト自体が壊れた場合はログを確認してバックアップから復旧します。
途中のロックファイルは残っていても、OSロックはプロセス終了で解除されます。

詳しい設計は[architecture.md](docs/architecture.md)、実測と環境調査は[initial-report.md](docs/initial-report.md)を参照してください。

全件処理の最終結果は[全関数キャッシュ実測・保存報告](docs/complete-report.md)を参照してください。

## 計算の現版照合

`verify/calculation.py`は既存の完全版キャッシュ・SOと検証済みアセットを読み、体力・攻撃・両方向命中・毒撃・メタルキラー・パーツ補間・章別お宝を局所実行する。既存Ghidraプロジェクトを変更しない。実行方法・条件・限界は[計算照合](../native/kbcs-core/docs/native-calculation.md)。完全な呼出記録はresearch/.local、小さい値のfixtureだけnative/kbcs-core/testsへ保存する。

## ステージの番台別照合

[番台一覧と確認状況](docs/stages/README.md)、[0番台の調査](docs/stages/00000.md)。`verify/stages.py`は40番台分の分類境界と0番台49マップ・324ステージの出現行、冠倍率、出現判定16条件、レア度制限6条件、ボスフラグ3値、通常報酬の比較8条件を現版ARM64へ照合する。配布DB・UIの生成コマンドではない。原本と実行結果の大きい報告は`.local/stages-1572-band0.json`へ保存する。`--publish`で出現判定だけの小さいC++照合用fixtureを更新する。

```powershell
python research/verify/stages.py --assets D:/KBC/KBC-rakv0-assets --python-libs D:/KBC/KBC-rakv0-lab/unit-db/research/python-libs
```

0.1.9の追加照合はverify/enemy_stats.py（同版の敵HP/攻撃・冠・クリスタル）とverify/rewards.py（0番台の通常比較/取得済み分岐）。[共通コアの契約](../native/kbcs-core/docs/stages.md)に条件と制御helper、全件数を記録する。未実装の個体生成/実付与と区別する。

## 0.1.10の追加照合

`verify/rng.py --python-libs <libs>`は明示状態の乱数、個体枠/レイヤー、成功後の間隔/初回出現を局所実行する。`verify/calculation.py`は命中の21段階と攻撃準備を追加。入力契約と未確認境界は[native監査](../native/kbcs-core/docs/audit-20261022.md)、1000番台の再実行と例外は[番台調査](docs/stages/01000.md)。

0.1.11のevent_rewards.pyは1000番台7種のmodeの候補数/比較と重み選択、報酬分類・冠別取得済みバイトを照合する。experience.pyは種別1のXPも検証する。再実行と制御helperは[native設計](../native/kbcs-core/docs/event-rewards.md)。

0.1.12のverify/stage_score.pyは005dd634以降のスコア/閾値/保存更新/結果行を、verify/reward_finish.pyは重み選択後の履歴/付与要求/結果行を局所実行する。[範囲と再実行](../native/kbcs-core/docs/stage-score.md)。

0.1.13はinventory.pyで実所持数の加算・変換・上限、ex_transition.pyで実RNGを含むEX抽選を照合する。event_rewards.pyは専用保存番号、stage_score.pyは保存番号なしのスキップと時計を追加。[関係と制限](../native/kbcs-core/docs/inventory-ex.md)。

0.1.14の[39000番台までの共通入口・実測・未確認範囲](docs/stages/all-bands.md)。stage_source、stage::Row::decode、experience::stageを追加。原本の分類とファイル選択を、専用戦闘ランタイムの完成と混同しない。


[JP15.7.2の音源経路](docs/audio-1572.md)はSound_setting、APK同梱音源、内部保存音源、追加ZIPのURL生成の静的追跡。KBCSのBGM補完と同版原本の採用を区別する。
