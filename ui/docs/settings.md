# 起動画面・設定・キー操作（2026-10-30）

ホームの設定→pages/settings。左パネルで見た目・データ管理・キーボード・システム情報を選び、中央へ各設定、右へ版/処理状況を置く。上部の配色を集約し、既存の配色/倍率/線の濃さの保存形式を維持する。

## ブランドと初回取得

提供された1920×1200の2画像をimages/brand/loading-center.pngとloading-top.pngへ保存した。背景は原画のRGB(11,28,63)。中央の画像を原画の244px（高さの20.333333%）上へ動かし、移動後は上寄せ画像へ切り替える。画面比率で不足する部分は同色のCSS背景。updatesの原本取得・展開・変換メッセージを表示し、成功後に閉じる。失敗時はデータ管理への導線を残す。戦闘開始時の本家暗転と分離する。

正方形の提供画像はapp-icon.png。scripts/prepare-brand.ps1が図柄を再作成せず、ICO・tao用RGBA・ICNSへ書式/サイズ変換する。Windowsはbuild.rsのllvm-rcでexeへ埋込み、Macはpackage.pyがResourcesとInfo.plistへ設定してから署名する。

## キー操作

初期配置は上段D/F/G/H/J、下段C/V/B/N/M、財布X、砲Comma、1段の切替Space、オプションEscape、速度I、スニャイパーO、ニャンピュータP。1段では下段の5キーが表示中の5枠を操作し、Spaceで前半/後半を切り替える。2段のSpaceは操作しない。戦闘中に切替可能な3アイテムだけを項目へ出す。

keyboard.jsの操作一覧/正規化を設定・戦闘・試験で共用する。event.codeをlocalStorageのkbcs:battle-keysへ保存し、重複を保存前に検出する。自動リピート・IME・入力欄・Ctrl/Alt/Meta併用を戦闘操作へ通さない。

PC拡張のcontrol=1000+本家のボタン対象番号をC++へ送り、既存release/SE/待機/経済/制限判定へ流す。JS/Rustで直接出撃を確定せず、5表示tickを省略しない。停止0tickの即生産は既存チートの条件だけ。元のARM照合用control=0..10は変更しない。キーボード自体を本家仕様として扱わない。

## データ管理と診断

settings.js→Service→kbcs-data::maintenance。公式DB・原本・キャッシュ・user領域を一覧/閲覧する。表示は150件ずつ、本文は256KiBまで。SQLiteは読取専用のスキーマ表示。使用中のDB/原本とuser領域を削除せず、他の削除も確認画面・サーバー側の保存先検証/更新ロック/戦闘中拒否を通す。

検査はworkerでDB構造・素材索引・実ファイルのサイズ/SHAを調べ、欠損パスを返す。DB再生成は保存原本を使い、強い修復は全ZIPを再取得する。成功した新DBだけをcurrentへ切り替える。

システム情報はMonitor/worker/cache、アプリ/ABI/ルール版、DB/原本の版・件数、OS/CPU/メモリ、ブラウザ/GPUを表示・JSON出力する。ホストメモリとJSヒープを区別し、WebView全体やGPU専用メモリを計測済みとはしない。GPU情報は1回取得し、監視ごとにcontextを作らない。

## 2026-10-30: 初回描画の遮蔽

Serviceは全HTMLのhead先頭へ通常scriptのstartup-boot.jsを挿入する。sessionStorageの初回判定だけを同期で読み、本文を隠し、青背景と中央ロゴを描く。moduleの依存取得が終わったらstartup.jsが不透明な画面を設置して遮蔽属性を外す。最初のフレームでホームを描いてからフェードを始めない。ホームの設定はnative-home-links内へ配置し、他の機能と同じボタン部品を使う。
