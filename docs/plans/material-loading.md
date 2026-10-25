# 素材読込の改善（0.1.19 / 2026-10-23）

## 原因と変更

モーション画面は対象に関係なく味方詳細・敵詳細・その他の全カタログをPromise.allで待っていた。数値や本能、コンボの構築が素材表示を阻害する。motions::choices→/api/motion-choicesでID/名前/形態だけを返し、viewerは選択中の種類の一覧とmanifestを並行取得する。別の種類は初めて選んだときだけ取得する。

その他素材のmanifestも毎回433モデルの内容を解析していた。effects::entriesは全モデルの最長所有関係を維持しつつ、選択された素材だけmodel/cutを読む。motions::descriptorはPNGについてメタデータとlength(bytes)だけを読む。画像本体をmanifest用に複製しない。

viewerはmanifestを16件、解析済みモデルとデコード画像を8件/見積32MiBまで再利用する。画像RGBAと原本sizeで見積もるため、JSオブジェクトを含む厳密な使用量上限ではない。GPU textureは従来どおり切替時に解放する。ページ再読込でキャッシュは破棄される。DB切替後はページを再読込する。詳細はui/src/features/motion/docs/README.md。

## 確認

同じDBと波動素材のCLIを各版3回実行し、起動/JSON化を含む中央値は旧版0.755秒→新版0.112秒（約85%短縮）。これはOSキャッシュがある状態の対象素材取得時間であり、全画面の初回表示時間ではない。新しいexeの最初の実行は1.272秒だった。全素材一覧の生成自体は今回大幅には短縮していない。

波動manifest、ネコmanifest、全433素材の一覧JSONを旧版と比較して一致。既存19テスト＋compile_fail1、全target clippy警告なし、変更JS構文を通過した。既存取り込み試験内で軽量選択肢の形態と不正kind拒否も検査する。実画面で433素材・味方882キャラ・敵792体、形態切替、種類切替と再選択、フレーム表示を確認しconsole警告/エラーなし。

DB/schema8/importer12・素材原本・モーション評価式は変更していない。修正版は.local/dist/0.1.19/KBCS.lnk、検証プレビューは127.0.0.1:4826（PID5636）。旧4817と利用中アプリは維持した。測定結果は.local/material-loading-before.json、material-loading-after.json、material-warm-comparison.json。今回のGitHub送信は行っていない。
