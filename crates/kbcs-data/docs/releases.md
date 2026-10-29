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
