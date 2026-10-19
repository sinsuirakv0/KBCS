# 初期構築・実測報告（2026年10月20日）

初期対象は、ユーザーの追加指定により15.7.2とした。15.7.1の既存MCPプロジェクトは参照用バックアップだけを確保し、変更・移動・切替・再解析を行っていない。

## APKとライブラリ

確定版の取得元は `sinsuirakv0/KBC-rakv0-assets` の `jp/version.json`。
アーカイブの取得元は [battlecats-apk Private Release](https://github.com/sinsuirakv0/battlecats-apk/releases/tag/battlecats-jp-history)。READMEとdocs/operations.mdの契約を確認した。

| 項目 | 実値 |
| --- | --- |
| packageName | jp.co.ponos.battlecats |
| versionName / versionCode | 15.7.2 / 1507021 |
| compactVersion | 150702 |
| アーカイブ | battlecats-jp-150702.tar.gz（459,818,856 bytes） |
| アーカイブSHA-256 | c51fa2b1e4938b4f09833a5b8e2f9ca98258c7ae8f714a3e8b96385254099fa4 |
| 統合APK SHA-256 | 7ba6f7d45fa60566936f90b46b7cc789c8f806661b4869f0213101a442a97a04 |
| 対象SO | libnative-lib.so（11,653,952 bytes） |
| ABI / ELF machine | arm64-v8a / 183（AArch64） |
| SO SHA-256 | 6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea |

アーカイブサイズ・Release digest・parts.json・APK hash・manifest三値を照合した。APKが検証済みでローカルに存在する再実行では、ダウンロードを省略することも確認した。
統合app.apkにはARM64の9ライブラリがあり、ARM32ライブラリはない。主対象SOにゲーム本体のJNI入口 `Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw` などを確認した。他のSOは広告・クラッシュ報告等の補助ライブラリで、今回の初期解析対象にはしていない。
アーカイブ内の元 `config.arm64_v8a.apk` にも同じSOが存在し、そのSHA-256は統合APK内のSOと完全一致した。
APK取得workflowの実行、Releaseの更新、GitHubリポジトリへの書込は行っていない。

## Ghidra環境

- Ghidra 12.1.2：`D:/KBC/tools/ghidra_12.1.2_PUBLIC`
- JDK 21：`D:/KBC/tools/jdk-21.0.11+10`
- MCP：GhidraMCP headless 5.15.0、loopback TCP `127.0.0.1:8089`、228ツール。
- 既存プロジェクト：`D:/KBC/KBC-rakv0-lab/unit-db/research/native-v1571/v1571-arm32.gpr`
- 既存プログラム：15.7.1、ARM32、5,473関数。SO SHA-256は `7226cbdf9f9ea9a521b4e4c3a78a72141a31410aa9293a03bb45717d1682ac79`。元Splitのhashとローカルprovenanceを照合した。
- 既存プログラムは解析処理中ではないが、Ghidraのanalyzedフラグはfalse。既存の関数情報があることと完全解析済みであることを区別した。
- 既存プログラムのGZFバックアップ：`.local/backups/initial-20261020.gzf`（17,107,165 bytes）。

利用可能な主要機能は、プログラム・プロジェクト情報、関数検索、呼出関係・参照・文字列、バッチデコンパイル、GZF/GAR出力、Javaスクリプト実行。ツール名の全一覧は `.local/mcp-tool-names.json` に保存した。
スクリプト実行は `GHIDRA_MCP_ALLOW_SCRIPTS` により無効だったため、サーバー設定を変更せず、既存Ghidraインストールのheadless APIをローカルから利用した。
`server_status` のconnected=falseは任意のGhidra Server版管理への接続状態であり、MCP自体の接続失敗ではない。

## 実測

新しいプロジェクトは `.local/cache/15.7.2/arm64-v8a/<SO SHA-256>/project/` に保存した。Ghidraの先頭ドット付き親パス制約を避けるjunctionを経由して開く。
初期自動解析は600秒で中止要求を出し、Ghidraログ上の累計解析時間は689秒だった。GCC例外テーブル・VarnodeContextの警告があり、**自動解析は未完了**。その状態で検出された関数の全件を索引化した。未発見コードまで全て解析済みであるとは判断していない。
スクリプト中のGZF保存はトランザクション制約で失敗したため、保存済みプロジェクトを再利用して索引化し、JVM終了後のプロジェクト全体をZIPでバックアップする方式に修正した。自動解析は繰り返していない。ZIPのCRC検証も通過した。

| 項目 | 実測 |
| --- | --- |
| 全関数 | 25,524（内部25,232、外部292） |
| thunk | 4,232 |
| 内部・非thunk関数 | 21,000 |
| 参照情報 | 521,593件 |
| 関連文字列を持つ参照 | 16,791件 |
| 最終索引抽出時間 | 13.07秒 |
| 索引用JVMの起動・終了込み | 31.61秒（SQLite取込時間は含まない） |
| 索引用JVMピークWorking Set | 約445MiB |
| デコンパイル試験 | 30件＋70件＝100件、成功100、失敗0 |
| デコンパイル時間 | 平均0.0889秒、最大2.549秒／関数 |
| 30件バッチ | 15.09秒、JVMピーク約276MiB |
| 70件バッチ | 25.59秒、JVMピーク約359MiB |
| 保存済みファイル読取 | 平均1.48ms／関数（30ファイル×10回、OSキャッシュあり） |
| 保存済み30関数の再要求 | CLI全体0.97秒、Ghidra要求0件、結果ジャーナル更新なし |

JVMのヒープ上限は512MB、同時処理は1バッチ。メモリ値はJVMだけで、ネイティブデコンパイラ子プロセスやOS全体を含まない。初回自動解析ではJVMで少なくとも約676MiBのWorking Setを観測したが、その初回の最終ピークは記録していない。
サンプルはアドレス順の等間隔抽出で、外部関数とthunkを除外した。大規模な難読化関数等を全て代表する測定ではない。
保存済みファイル読取の測定時には索引更新も進行していたため、速度は参考値。CLIの再要求省略は索引更新完了後に確認した。

| 保存物 | 容量 |
| --- | --- |
| SQLite | 90,546,176 bytes（約86.4MiB） |
| 100関数の疑似コード | 187,766 bytes（約183KiB） |
| 交換用索引JSONL | 71,691,655 bytes（約68.4MiB） |
| プロジェクトZIP | 299,436,257 bytes（約285.6MiB） |
| 稼働用独立プロジェクト | 約285.6MiB |
| キャッシュディレクトリ全体 | 約734MiB（APKは別） |

検索・呼出元/先・参照・文字列・疑似コード上限・未キャッシュ一覧を実データで確認した。SQLite取込中断時のロールバックと、ジャーナル復元/ファイル消失を検証する2件の最小テストも通過した。
計測JSON・検証結果はキャッシュ内の `benchmark.json`、`verification.json`、`*-metrics*.json` に保存した。大量の関数や疑似コードはMCP応答に流していない。

## 構築したファイルと使い方

| ファイル | 役割 |
| --- | --- |
| research/indexer/apk.py | 毎回の確定版確認・APK取得・検証・ABI別SO抽出 |
| research/indexer/run.py | 独立解析、既存コピー再利用、逐次デコンパイル、負荷制限 |
| research/indexer/store.py | SQLite、ハッシュ、状態同期、再開 |
| research/ghidra/ExportCache.java | Ghidra内部の一括索引・要求分だけのデコンパイル |
| research/cli/cache.py | 上限付きローカル検索 |
| research/indexer/test_store.py | 2件の最小テスト |
| research/config.example.json | 外部Ghidra/JDKのパスと負荷上限 |
| research/README.md、各領域のdocs | 手順・設計・関数の関係 |
| .gitignore、AGENTS.md、README.md | ローカル生成物の除外と短い開発方針 |

コマンド例は[research README](../README.md)を参照。通常は `cache.py find/strings/callers/callees/refs/code/pending/stats` だけで調べ、必要な関数のアドレスを `run.py decompile --address` に指定する。

## 推奨方式と拡張

**関数索引は全件保存、疑似コードは必要時に逐次キャッシュ**を推奨する。今回の平均を21,000関数へ単純に掛けても約31分で、複雑な関数・タイムアウト・I/O・再起動の時間はさらに増える。全件事前デコンパイルの実測値ではない。起動の約十数秒が小さな関数の実処理時間より大きいため、必要な関数を小さなバッチにまとめる。
新しい版は版/ABI/SHA別に追加し、既存キャッシュを保存する。次の拡張候補は、バイト列・正規化命令ハッシュ、文字列アンカー、呼出関係を利用した候補対応表。アドレスだけで新旧関数を同一視せず、対応の根拠・確度を保存する。[詳細設計](architecture.md)も参照。
戦闘エンジンやUIは実装していない。将来のシミュレーターはGhidraに依存させず、確認済みの知見を独立した成果物として利用する。

全件処理の最終結果は[全関数キャッシュ実測・保存報告](complete-report.md)を参照してください。
