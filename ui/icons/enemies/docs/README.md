# 敵用の補完アイコン

2026-10-14にybcの敵検索で対応する項目を確認し、次の3画像をそのまま採用した。生成画像・推測した合成画像は使わない。

| ファイル | 用途 | 取得元 | SHA-256 |
| --- | --- | --- | --- |
| `base.png` | 敵城 | https://ybcecho.vercel.app/img/iconSite/Base.png | `750443d577f508762a346ed2a12bf6eb981cde9762ae1ee8d690d77e96af202b` |
| `burrow.png` | 潜行 | https://ybcecho.vercel.app/img/iconSite/Burrow.png | `a62ff3146e1a980c476115f5982e329100fdab20835cd43ea3373f028101ca74` |
| `revive.png` | 蘇生 | https://ybcecho.vercel.app/img/iconSite/Revive.png | `c95bd7c0ed178b230466529843a844935daaea5206b8d43fdb1e8b2b33e53d15` |

JDBにもBurrow/Revive画像がある。潜行のPNGはybcと同一。蘇生はPNGのバイト列が異なるため、このサイトではybcの画像を正本にする。

ゲーム側のimgcutラベルを探索した範囲では、この3項目用の図鑑アイコンを確認できなかった。復活・城のキャラ本体画像や演出は存在するが、特性アイコンと混同しない。

悪党は本家 `img015.imgcut` の384番「怪人(金)」に対応する。ybcの悪党選択も `img015_384.png` を使うことを確認したため、補完PNGを作らず既存アトラスから表示する。切り出しの知見はlabのenemy-db/docsへ記録する。

`shared/game/enemies.js` が3枚をViteから読み、`propertyImages`として共通表示部品へ渡す。ビルドには参照する画像だけを含め、この資料は配信しない。
