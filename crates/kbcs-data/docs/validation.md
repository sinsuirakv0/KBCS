# 欠損検査・再生成・管理（2026-10-30）

schema8を維持し変換器を14へ更新。旧変換器のsnapshotは更新確認で再生成対象とし、同じ原本版でも古いDBを最新として固定しない。

- motions::validateは公開対象の形態について、攻撃maanimから同じstemのモデル/分割/Number画像へ辿れるかをDB公開前に検査する。未使用の行を架空の素材で埋めない。モーション一覧の実在モデルと戦闘に必要な攻撃の有無は別条件。
- 背景のimage_size/scene_sourceは索引のみの原本取得を共用する。存在する背景JSON/必須分割の取得失敗を空データへ変えず、論理パスを返す。
- source::assetは原本の移設/欠損時だけ固定SHAのキャッシュへ戻れる。存在する原本の破損を隠さず、開発用Source::checked_namedの変更検出を維持する。
- releases::install_dataはrelease.jsonだけで完了とせず、全ファイルの存在/サイズも確認する。欠損時とrepair_dataでは再取得する。全ZIPの検証/展開後に差し替え、差替え失敗時は旧フォルダへ戻す。同サイズの破損は明示検査のSHA比較で検出する。
- import::rebuildは新しい名前で生成し、成功後にcurrentを切り替える。次の通常importは同じidentityの現在DBを再利用できる。編成/持ち物は別DB。
- maintenance::summary/browse/inspect/delete/verifyは設定とCLIで共用。保存先の内側だけを操作し、使用中のDB/原本・user領域を削除から保護する。検査はsource_file→ローカル原本→SHAキャッシュを調べ、上限200件の問題一覧と全問題件数を返す。通常起動で全画像のSHAを繰り返さない。

## 持ち物画像の根拠

JP15.7.2 ARM64（SO SHA6122e248…）の009a311c→006f53b8はGatyaitembuy.csvの列11を構造体+0x38へ保存。006f3104は内部行番号が275未満なら、imgID=−1は内部行番号、それ以外はimgIDを返す。0061c4e8はその値でgatyaitemD_%02d_f.pngを選ぶ。

公開報酬ID（列3）を画像番号に使っていた誤りを訂正した。名前は内部行、保存/集計は公開報酬ID、画像は内部行とimgIDの上書き。XP/NP・チケット・特殊アイテムに共通。見た目から対応を推測していない。

Apple Siliconのネコモヒカン/背景7・139・1057の壊れた保存一式は未取得。Windowsの同版原本検証と欠損/移設の回帰を、Mac実機で原因を確定したことと混同しない。

## 容量不足

実データの隔離生成中、Dドライブの残量約76MBでSQLite DiskFull(13)を確認した。未完成DBを公開せず、検証先をCの専用一時領域へ移した。storage::space/requireはWindowsのGetDiskFreeSpaceExWとMacのstatvfsを共用入口にする。ZIP展開前に展開容量＋最大ZIP＋DB用余裕、DB新規生成前に少なくとも512MiB（旧DBの2倍が大きければその値）を確認する。検査時の空き容量は変動するため、生成中のDiskFullも保存先/残量つきで返す。設定のデータ管理・システム情報にも保存先の空きを表示する。

## 今回の検証結果

- Windows x64のreleaseビルド、Rust43件＋compile_fail1件、workspace/all-targets clippy（-D warnings）、JS3本/構文24ファイルが成功。既存C++警告11件は継続。提供PNG3枚は原画とバイト一致し、ICO/ICNSのサイズとWindowsのPEリソースを検査した。
- ローカルJP15.7.4統合原本（40bc155e…）から隔離DBを生成し、882キャラ・2618形態・792敵・6476ステージ・54338素材索引を保持。必須モーション参照の2176形態、全54338素材のサイズ/SHA検査は不足/破損0件。DBは226963456bytes。生成194.893秒、全SHA検査333.316秒（同時にreleaseビルドが動作した環境、ZIP取得/展開時間を含まない）。全SHA検査は明示操作時のみ。
- ネコモヒカン（0/形態2）の画像/モデル/分割/4モーションと魂を含むmanifestを取得。背景7/139/1057は0F/30Fの6条件で描画要求のmissing=[]、issues=0。Windowsから保存原本を解決した結果であり、Mac実機の表示一致の証明とはしない。
- 管理APIの実サーバー経由で設定/画像/JS、summary/storage/system/inventoryを取得。現在DBの削除要求とパストラバーサルを400で拒否し、元DBの存在を確認した。原本006f3104の画像番号は15条件を同版ARM64と照合した。
- 検証記録はresearch/.local/settings-{import-report,real-verification,integrity,api-verification,inventory-native,source-graph}.json。検証DBとWindows確認用アプリはC:/Users/ABC/AppData/Local/Temp/KBCS-settings-20261030/{data,review}。既存AppDataと参照原本は変更していない。Macのビルド/実機確認はこのWindows環境では未実施。

最終Windows確認用の5ファイル構成（exe＋4DLL）で非表示WebView2起動検査がexit0。最終exe内のstartup/keyboard/settings/HTMLを実サーバーから読み、作業ツリーとバイト一致を確認した。結果はresearch/.local/settings-final-package.json。UIの見た目を実画面で確認したという意味ではない。
