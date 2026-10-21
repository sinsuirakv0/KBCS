# 再開メモ（2026-10-22更新）

ユーザーの継続指示で0.1.8まで進め、素材抽選と開始時の待機・敵城行の初期化を追加した。次は0番台の通常報酬取得・敵城個体の補正・ボス2イベントを確認し、残る分岐を整理してから1000番台へ進む。

## 動作版

- `.local/dist/0.1.8/kbcs.exe`、ABI2 / ruleset1507021、schema7 / importer8。
- 通常プレビューは127.0.0.1:4817。当日の停止前PIDは17848。ユーザーのGitHub保存・PC終了依頼に従い、送信確認後に停止する。再起動後は下記コマンドで起動し直す。PIDを再利用せず、実行パスと引数を確認する。
- 実使用DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-e63a79e7efc54c515d1e9f8ae3a3f9d8b50665ce8b798cf27333139eab0ad1bc.sqlite`。
- 旧DBは保持。切替前ポインタは`.local/current-before-0.1.8.json`。検証用データ`.local/stage-0.1.8`、比較結果`research/.local/stage-database-0.1.8.json`。

- 候補版4818/PID19012は停止済み。ブラウザは通常版のN000・1冠・素材表を展開。確認画像`.local/stage-materials-0.1.8.png`。

## 完了した範囲

0番台49マップ・324面・出現2924行・冠196値・原本378件を全件比較。0.1.7のXP、検索と表、冠、左右パネル、共通お宝・施設は維持した。

0.1.8はDropItemの49プロフィール・196冠係数・392回数枠・392重みを保存。素材IDはGatyaitembuyの種別7/スロットを同版の006f308cと16件照合した。抽選回数1568条件、2段階抽選7条件が現版命令と一致。C++のmaterials::plan/pickを共用し、表示は一様独立抽選の理論確率。素材の所持数加算や乱数器全体は未実装。素材は報酬検索へ追加し、詳細の素材表は初期状態で折りたたむ。

009eadc8の待機初期化と敵城行の消費を局所実行し、全324面と境界6条件を確認。loaded列2の負待機を維持、敵城の最初の一致行だけwait=1/spawned=1、生成helper失敗時にも消費する。stage::initializeへ追加した。通常出現のcommit成功時限定規則と混ぜない。敵個体の生成・HP/姿勢や戦闘全体の初期化は未実装。

workspace7テスト、clippy全target、実データ比較、JS構文、BOM、release/CLIを確認。画面はN000の1冠2回/2冠3回、素材確率・期待数、レンガで47マップ312面、画像欠損とconsole警告/エラーなしを確認した。素材名原本は正常なUTF-8で、ターミナルの文字化けを原本破損と誤認しない。

## 次に調べる箇所

1. 0番台の報酬本体005d996c、0x5dc158以降の取得済み状態・初回/繰返し・付与。通常報酬は候補と元比較値だけを保持し、最終確率を推測しない。素材の実付与も別途確認する。
2. 009eadc8の残る個体初期化、冠倍率の個体HP/攻撃への適用順、コンテニュー。今回の2区間の検証を全初期化へ拡大解釈しない。
3. 006d6d04のボス2だけの005c1404追加イベント。ボス1/2の衝撃波経路は静的確認済みだがフレーム全体の実行ではない。
4. 0番台の残る分岐を整理してから1000番台へ進む。他番台を検証済みとして一括公開しない。

現版はJP15.7.2 ARM64 / 1507021、SO SHAはresearch/docs/stages/README.mdとresearch/.local/reference.jsonで確認する。MCPの旧15.7.1 ARM32、読み取り専用の参照リポジトリ、既存Ghidraプロジェクトを混同・変更しない。GitHubへの書込は個別承認が必要。

## GitHub保存と再起動後の再開

保存先は既存の非公開リポジトリsinsuirakv0/KBCS。ソースはmain、動作版と今回の検証結果の保存先はRelease `kbcs-v0.1.8`。既存の大容量ネイティブ資料はRelease `native-v15.7.2`を維持する。実使用DBと旧snapshotはローカルに保全し、必要なら同じassets版から再生成できる。

```powershell
./.local/dist/0.1.8/kbcs.exe preview --bind 127.0.0.1:4817 | Out-Host
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
./scripts/build.ps1 -LlvmBin 'D:/KBC/KBC-LINEbot-v2/.tools/llvm-mingw-20260922-ucrt-x86_64/bin'
```

cargo fmt後は日本語ファイルのBOMを復元する。起動中の配布exeは上書きせず、対象の検証・停止・WaitForExit後に更新する。基盤の多くが従来からuntrackedなので既存変更をreset・削除しない。commit・GitHub書込は行っていない。
