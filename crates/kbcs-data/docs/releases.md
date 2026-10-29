# 統合リリースの原本（2026-10-29）

`releases::latest_data`はKBC-rakv0-assetsの公開済み`integrated-<region>-*`を公開日時で選び、manifest.json自身と、manifestに載る全ZIPのsize/SHA-256をGitHubのasset metadataと照合する。最初の対象は`integrated-jp-1507040-3-1`、ゲーム15.7.4、原本commit `40bc155ebbc2b096a4a2123028e08cdb075b5383`。

このリリースはData/Download/Image/ImageData/Map/Number/Unit/assets/music/resの10 ZIP。各ZIPには同名のトップフォルダが含まれる。従来のjp/Local/<datasetId>/、jp/server、生成済みcharacters.jsonを要求しない。

`install_data`→`download`→`extract`の順。downloadはストリーム受信し、サイズとSHAを満たしてからキャッシュを確定する。extractはパス逸脱・Windowsの予約名・symlink・重複・展開量超過を拒否し、各ファイルのSHAを計算する。展開件数/総サイズをmanifestと比較し、全ZIP成功後に採用元一覧とリリース情報をrelease.jsonへ保存してフォルダを公開する。展開済みZIPは削除して二重保存を避ける。原本は`<data-dir>/assets/releases/<tag>/`、途中は同じ親の`.pending-<tag>/`。既存の公開フォルダを上書きしない。

`Source::open`はrelease.jsonのあるフォルダをGitなしで開く。`integrated_dataset`はres/Unit_Explanation*_ja.csvから名前/説明を取り、Data/unit*.csvに実在する行数までを形態とする。例: ID736は説明3行・能力2行であり、第3形態を作らない。説明の元ファイルは全行保存する。以前のWeb補完別称/海外版補完は新ZIPの原本に含まれず、旧生成物から黙って混ぜない。

取り込みの公式schema8/importer13は維持する。原本commit/buildId/manifestの識別が異なるため新snapshotを作成し、成功時だけcurrent.jsonを切り替える。metadataにrelease_tag/release_publishedを追加する。編成・持ち物・設定は従来のuser領域を維持する。名前の出典は実際の説明CSV。従来Git原本のSource::dataset経路も残す。

画像は`source::asset`がDBの採用元SHAと展開済み原本を検証して読む。`stage_media::audio`は同じDBのassets/sndNNN→music/sndNNNを優先し、ない曲だけ旧固定索引へ戻す。CAFの既存PCM→WAV変換を共用する。`music_catalog`も原本の音源索引を合成し、ステージ情報の「未収録」判定を更新する。

`releases::lock`はstd::fs::File::try_lockによるOS排他。download.lock/update.lockはファイルが残っても異常終了後に再取得できる。ファイルを削除して排他を解除する運用は不要。中間フォルダの削除はこの排他を取得してから行う。

新しいデータの採用は、15.7.2の保存済みARM64と15.7.4の全戦闘分岐が一致することの証明ではない。ネイティブ関数の参照版を自動で15.7.4へ変更しない。

## 版固定参照の接続

本能玉枠はequipment::capacitiesが採用済みData/equipmentslot.csvを読む。DBに原本bytesがない場合もasset_referenceとsource::assetの検証済み原本へ戻れるため、旧snapshotの再構築を要求しない。viewのorbSlots、編成Storeの保存、戦闘Documentの検査が同じ表を使う。単独Document::validateは同版の旧組込み定義を維持し、公式DBがある呼出元はvalidate_with_databaseを使う。

compatibility::calculation_versionはsettings-catalogの全27採用元SHAを公式索引と比較し、一致する場合だけ参照版15.7.2を返す。キャラ/ステージカタログはgameVersionとcalculationVersionを分離する。キャラ詳細・XP・城体力は後者で既存定義の適用可否を判断する。戦闘開始は現在buildId、（指定時の）snapshot.versionとDBを照合し、別途全戦闘入力・効果時計SHAを照合する。

戦闘UIも版番号だけで拒否せず、異なるbuildId/版では既存の画像・imgcut・音設定の全採用元SHA照合を行う。15.7.4では設定27件、戦闘入力4件、全効果時計、UI27件が同一だった。新しいゲームの全ARM64ロジックの一致を示す値ではない。旧編成は記録を一括変更せず、現在DBに対して検査して出撃snapshotへ解決する。編集保存時だけgameVersionを現在DBへ更新する。


0.1.36: app_asset_nameがWindows x64/Mac arm64/Mac x64の配布名を選ぶ。latest_appは当該環境用のZIPを持つkbcs-v版だけを比較する。extractはUnixの実行ビットを保持し、Macの更新用実行ファイルを再起動できるようにする。データZIPと同じストリーム検証・パス拒否を共用し、symlink/setuid等は採用しない。3環境の命名・起動検査はアプリ領域のbuild.mdを参照。

## 2026-10-29: 取り込み時の重複処理

取り込みは原本ZIPの展開とは別に、CSVの正規化、出典の保持、モーション/ステージ/報酬等のSQLite索引構築、整合性検査、完成snapshotの公開を行う。

統合リリースのモーション画像は展開先に存在するため、motions/effectsで画像BLOBを再保存しない。asset_referenceのパス/サイズ/SHAを用い、source::assetが実際の要求時に読み取り・照合する。Database::sourceもDBのdata-dirから同じ本文へ戻れる。legacy Git経路は従来のBLOB保存を継続。PNG descriptorと存在検査は索引だけでも動作する。旧DBのBLOBもそのまま利用でき、schema8/importer13の解釈は変えず、容量削減だけのための強制再取り込みは行わない。

read_assetは同じトランザクションですでに検証・保持した原本を再利用し、再取得・再ハッシュを避ける。新規DB構築中のSQLiteページキャッシュは32MiB。正式なassets/releases配下の管理済みデータでは、manifestから先に完成DBの識別を求め、同一DBがあれば全キャラ説明/能力CSVの再走査を省く。外部の開発用原本は従来通り内容を検証し、変更をキャッシュで隠さない。

motions::resourcesはmanifestと同じbody/soul/animationのパスを、ファイル本文なしで返す。戦闘開始前の画像取得とRust Sessionはこちらを使う。資料閲覧用manifestは全文を維持。Sessionは各モデルのcut/model本文を一度読み、各clipのC++パースへ共用する。戦闘計算やモーション時計は変更しない。

統合ZIP由来のテキスト原本は、最大8並列で準備し、SHAを確認した内容を取り込み中だけ共有する。CSV/JSON/モーション定義に限定した128MiB上限のメモリキャッシュで、名前の読取・正規化・モーションの各工程による再オープン/再ハッシュを避ける。容量に入るものだけを先読みし、画像は対象外。Git作業ツリーの毎回検証、通常のasset要求時のSHA照合、次回取り込みでの再検証は維持する。DBへの書込み・解釈の順序は変えない。

隔離済み15.7.4原本の全件変換で112.549秒、完成DB再利用で0.549秒。DBは480,440,320→226,963,456bytes。unit/form/enemy/stage/asset_reference/talent/talent_levelの件数は旧DBと一致。通常キャラの未使用形態を隠したcatalogは882キャラ/2177形態（精霊を含む）。同一入力の30/60/90Fで旧版とstate/runtime/layout/sceneが一致し、RNGも一致。0tickの通常/即生産では味方数0/1/2、frameとui_frameは0のまま。APIの本文付き/パスのみのmanifestは同じbody/soul等を返し、例ID94の応答は9184→1328bytes。これらは単一環境の参考値で、ZIP取得/展開時間や実画面の検証を含まない。記録は.local/fix-verification.jsonと.local/fix-api-verification.json。

## 2026-10-29: 大容量ZIPの受信期限と通信再試行

Apple Silicon版の初回取得で報告された `timeout: receive body` を調査。固定依存ureq 3.4.2のconfig.rs/timings.rsでは、timeout_recv_bodyは各readの無通信時間ではなく、応答ヘッダー受信から本文全体を読み終えるまでの期限。従来は全体1800秒とは別に本文120秒を設定していたため、継続受信していても2分で中断した。現行Number ZIPは約224.8MiBであり、回線速度によりこの期限へ到達する。Windows/Macの共通Rust処理で、ARM64固有の原因とは確認していない。

agentは接続20秒・応答ヘッダー60秒を設定し、本文だけの短い期限を外す。JSON/manifestは全体30秒、downloadはZIPごと・試行ごとに全体1800秒。無期限待機にはしない。download_with_agentを共用し、タイムアウト・接続切断/途中EOF・一時的な接続失敗・HTTP 408/429/5xxだけを最大3試行（待機1秒→2秒）で再取得する。通信のreadエラーだけをureq::Errorへ戻し、ローカル書込み/容量/SHA検証失敗を通信障害として繰り返さない。対象名と試行回数を進捗・最終エラーへ含める。本体ZIPも同じ関数を利用する。

受信失敗のpartは破棄し、そのZIPの先頭から再取得する。HTTP Rangeによる中断位置再開は未実装。検証済みキャッシュの再利用と、成功時だけrenameする契約を維持する。install_data全体が失敗した場合のpending削除・既存DB維持も変更しない。最終失敗後は既存のホーム「データ管理」から再試行でき、lockファイルの手動削除は不要。

ローカルHTTP試験で旧本文期限を短縮して再現し、遅延受信の成功、途中切断からの再取得、3回失敗での打切り/part削除を確認した。SHA不一致は再試行せず、既存のサイズ/SHA検証と完成キャッシュ再利用の試験も通過。kbcs-dataのreleaseテスト11件とworkspace/all-targetsのrelease clippy（-D warnings）が通過。Mac実機の通信試験は含まない。

## 2026-10-29: Intel Mac CIの通信試験

Actions run 40862502160のmacos-x64は、コンパイル後のdownload_allows_slow_body_and_retries_interrupted_transferで失敗した。旧本文期限によるRecvBodyエラーは正しく発生していたが、期限前にpartialへ必ず1byte以上返ると仮定した追加assertが失敗。中間受信量はOSのバッファリングや実行タイミングに依存し、空であることはタイムアウトの誤りを意味しない。その量のassertを削除し、RecvBodyそのものの判定を残す。後段の低速取得の全bytes/SHA一致、切断後の1回再取得、3試行での打切り/part削除、破損時は再試行しない検査を維持する。アプリの取得処理・期限・リトライ条件とworkflowは変更しない。
