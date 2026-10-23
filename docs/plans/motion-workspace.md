# モーションワークスペース（0.1.16公開済み）

2026-10-23。依頼はステージ検索の出現敵列の初期非表示と、Webより詳しいモーションUI。ユーザー追補に従い、変更の少ない形式/補間は既存の解析済み実装を再利用し、検証を代表素材に絞った。

## 公開物

- `.local/dist/0.1.16/kbcs.exe` / schema8 / importer10 / ABI2。
- 通常DB：`C:/Users/ABC/AppData/Local/KBCS/official/jp-71e42b90c517b9103aa1a9dcedf592fb2b380646547b6d7f7fcba1f493124423.sqlite`。旧DBと`.local/current-before-0.1.16.json`を保持。
- プレビュー127.0.0.1:4817、PID15960で非表示起動。停止/更新時は実行元・引数・MainWindowHandle0を再確認する。
- 全29系列1298マップ6476面を維持。本体/共通魂のモデル2950件、maanim11744件、Number PNG2950枚を保存。取り込み対象の定義は17644件。source_file全体は他機能のcutも含む。

## 関数とUI

motions::importはform/enemyのmotion_pathから共有ID/タマゴmを解決済みのstemを使用。現版005bcea8と同じくNumber/{stem}.pngを選び、imgcut中の制作PCパスは無視して原文を保持する。model/cut/全maanim/共通魂を原本hash検証付きで保存する。motions::manifestとCLI motionは同じsource_file一覧を返す。

左はキャラ/形態とパーツ・ファイル・分割画像、中央WebGL、右はパーツ現在値/キー/モデル設定点、下は30FPSの時計。非表示は描画packetだけを外し、親子変換を残す。個別/子まとめて/単独表示、画面選択、ドラッグ、拡縮、反転、キー移動、1F/10F送り、原本表示、PNG/分割画像保存に対応。URL操作欄は置かない。

KB→魂はC++motion.cppの24F体力KB→共通/専用魂の最大長→退場。GET motionとPOST motion-timelineを通じて、通常魂と_soul専用を別セットで扱う。余分な上昇/フェードを重ねない。移植元はreadonlyのsave/motion/frontend、ファイルSHAはui/src/features/motion/upstream.json。詳しい設計は同領域docs。

## 検証と限界

代表6素材（000f/045c/347c/351e/魂000/魂007）、120姿勢、1350描画部品を簡易確認。C++の時計境界1テスト、既存DB取り込み2テストへ制作PCパスの回帰を追加し、Service既存試験へAPIの正常/負値/未知項目を追加。workspace18＋compile_fail1、clippy全target、release、CLI verifyを確認。

実ブラウザーで1F、Hキー表示切替、パーツ非表示で描画数2→1、元model表示、10分割画像、分割保存ボタン、通常KB→魂24F、347c専用魂12パーツ、敵0再生を確認。最終公開先でconsole警告/エラーなし。ステージDB全件照合もimporter10で通過し、古いデータを壊していない。

姿勢/補間は既存JavaScript評価器のまま。C++移植、全戦闘の死亡/蘇生/参照待ち/KB限界は残る。現版17kファイルを全命令照合したとは主張しない。ユーザーの軽めの検証方針を維持する。

公開確認画像は`.local/motion-workspace-0.1.16.png`。DB/実行ファイルのSHAと旧snapshot保全は`.local/publication-0.1.16.json`。試験用4820/4821は停止済み。
