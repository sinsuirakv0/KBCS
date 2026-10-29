# 自動採番と三環境の公開（2026-10-29）

## 呼出しと責務

`.github/workflows/build.yml` の prepare → build（三環境）→ release。prepareだけがmainを更新し、buildとreleaseはprepare.outputs.commitをcheckoutする。元イベントのGITHUB_SHAと自動コミットは異なるため、package.pyのgit HEADとpublish-release.pyのKBCS_RELEASE_COMMITを同じ値へ固定する。ZIP・アプリ内のCARGO_PKG_VERSION・タグのソース・Cargo.lockを一致させる。

prepare-release.pyのselect_versionはX.Y.Zの数値順でkbcs-vタグを比較する。version入力なし、Cargoも既存タグと同じ版ならpatch+1。Cargoが既存タグより新しい場合は明示指定/未公開の予約版として維持する。手動実行のversion入力は現在のCargo以上・既存タグより新しい版だけを許可する。native-v等のタグは数えない。

update_filesはworkspace.package.version、workspace memberだけのCargo.lock、READMEの配布リンク/見出しを更新する。手書きのdocs/releases/VERSION.mdがあれば保持し、なければ三環境へのリンク・ソース取得・前回タグからの比較を含む説明を生成する。日本語はUTF-8 BOM。依存パッケージの版やロック内容は変更しない。

prepareは開始SHAとremote mainを確認し、変更対象を限定してgithub-actions[bot]のコミットをpushする。KBCS-Release-Sourceトレーラーと親SHAを持つ直後のbotコミットは再実行時に再利用する。さらにmainが進んでいたら古い実行からの書込みを中止する。pushはfast-forwardのみ。ビルド失敗でタグがまだなければ予約版を次の修正でも使える。タグ/ドラフト作成後の失敗は同じrunの再実行で復旧し、公開済みの版は上書きしない。

タグ指定の経路はCargoとの一致を確認して採番しない。公開対象以外のイベントではprepare jobをskipし、buildは元イベントのSHAを使う。workflow_dispatchのversionは環境変数で渡し、シェルへ直接展開しない。PRにwrite jobは実行しない。

publish-release.pyは三環境のZIP・checksum・JSONを検証し、指定タグがなければそのSHAへ新規作成する。既存タグは注釈付きタグもcommitまで辿り、異なるSHAなら拒否する。タグ作成後の公開は同じrunで行う。公開途中のドラフト再利用と、GitHub側ZIPのサイズ・digest照合は従来通り。release jobは同じconcurrency groupで直列化する。

GITHUB_TOKENのpushは新たなpushイベントのworkflowを開始しないため、自動コミット/タグを契機に再実行する設計にはしない。参照: [GitHub公式のイベント規則](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow)。

## 検証

`python -m unittest discover -s scripts/tests` はGitHubへ書き込まず、一時的なbare Gitリポジトリで通常のpatch採番、明示版、lock/README/説明、同一run再利用、古いmainからの公開拒否、タグ一致、公開対象外の無変更を確認する。version文字列の不正・巻戻し・再利用も拒否する。

workflowの構文はactionlint、実workspaceの採番後Cargo.lockは隔離したmanifestでcargo metadata --locked --offline --no-depsを確認する。Cargo.lockの版番号によるハッシュ変更後も、OS/コンパイラ別のキャッシュを復元し、Cargo自身に変更依存だけを再構築させる。

ローカル検証は4テスト、actionlint 1.7.12、実workspace三crateを0.1.37に揃えたcargo metadata --locked --offline --no-depsが通過。公開処理はGitHubを模した応答で成功・別コミットの既存タグ・配布先SHA不一致を確認し、検証失敗時に公開しないことを検査する。
