# GitHub原本の永続保存（0.1.20 / 2026-10-24）

ユーザーは作成済みReleases DBではなく、既存assetsリポジトリの原本をAppDataへ保存する方式を指定した。通常の取得元をDEFAULT_SOURCEへ向け、原本をassets/objects/SHA256へ保存する。索引は取得元/commitごとに保存する。exe/アプリ版をデータidentityへ混ぜず、同じsnapshotは再生成/全件整合性走査を省く。新規DBの公開前検証とverify CLIは維持する。

変更があった原本だけをネットワーク取得する。旧DB内の同じパス/SHAの原本も検証して再利用できる。ステージ定義とモーションの既知の取得対象は最大8並列。取得失敗時は残りキューを停止し、成功分のキャッシュは残す。SHA/size不一致のキャッシュは採用せず、旧DBまたは固定commitから復旧する。ローカル手動取り込みはキャッシュで元フォルダ変更を隠さない。

保存場所は通常C:/Users/ABC/AppData/Local/KBCS。assetsが原本キャッシュ、officialが構築済みSQLite、current.jsonが公開ポインタ。KBCS_DATA_DIR/--data-dirによる上書きは従来どおり。通常画面は取得ボタンと保存先、手動取り込みは折りたたみとした。初回に存在しない素材の転送・新しい原本/変換器版のDB構築は引き続き必要。

## 確認

既存19＋キャッシュの回帰1件＝workspace20テスト、compile_fail1件、clippy全target警告なし、変更JS構文を通過。新試験は到達不能な通信先で、壊れたキャッシュから既存DBの原本を復元し、DB参照を外した後も保存ファイルを再利用できること、不正SHA拒否を確認する。既存取り込み試験の原本不正時の旧DB保全・地域分離・オフライン閲覧も維持した。

実DBのコピーを.local/update-cache-proofへ置き、通常保存先と稼働中の更新には干渉しなかった。同じローカル原本/既存DBの確認は0.1.19の8.157秒→0.1.20の1.955秒（各1回、参考値）。実GitHub HEAD db586c92df34ab54f4417a03fa1553a4faeac134を解決し、原本索引の取得とUI更新を完了。続くキャッシュ利用の更新確認は1.150秒。DB SHAとcurrent.jsonのbytesは不変、update.lock解放を確認。初回空の保存先での全素材取得時間と、ネットワーク障害を含む全件の並列取得は未実測。

画面ではJP15.7.2、882キャラ/2177形態、保存先、エラーなしを確認。API/CLIのログは.local/github-cache-update-proof.jsonとupdate-reuse-proof.json。公開記録は.local/publication-0.1.20.json。テスト用プレビューは4827/PID9264。通常の既存プレビュー/アプリと進行中の取り込みは終了していない。GitHubの書込やworkflow実行は行っていない。
