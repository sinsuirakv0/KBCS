# Android標準書体

JP15.7.2の0055cc34/getFontHandle、0055c994/newTextBitmapと、同版APKのMyActivity→ip0を確認。TextPaintは通常Typeface、default_boldだけdefaultFromStyle(1)、setTextSize、antiAlias=trueを使用する。図鑑の名前30px、効果20pxをArialの太字で代替していた指定を廃止した。

`scripts/sync-android-fonts.py`は固定したAOSP原本をWOFF2へ変換する。欧文はRoboto、日本語はNotoSansCJK-Regular.ttcの日本語face0。字形をサブセット化しない。元SHA・変換後SHA・NOTICEはui/fontsへ保存。Robotoは可変weight100〜900、Noto日本語はregular400。OS固有フォントの代替へ依存せず、CSSの既定書体とCanvasのnativeFontを共用する。Canvasの文字計測/描画と図鑑表示の前にloadNativeFontsを待つ。

AOSP参照:
- https://android.googlesource.com/platform/frameworks/base/+/android16-release/data/fonts/
- https://android.googlesource.com/platform/external/roboto-fonts/+/c50938f329a44707b06b336166c95ec2aa49c331/
- https://android.googlesource.com/platform/external/noto-fonts/+/f1fe27f9777986e0f5973b4e6dda8be9dae49a95/notosanscjk/

これはAndroidの標準書体の固定配布であり、Android全版の同一フォントファイルやSkia/ブラウザの画素一致は主張しない。日本語の太字指定はブラウザの合成太字。通常の本家図鑑文字はweight400。


変換後のcmap（Roboto2,797文字、日本語44,776文字）、hmtx、glyph順とGSUB/GPOS/CFFテーブルは元faceと一致した。WOFF2の出力SHAはsources.jsonに記録し、headの時刻は再生成しない。
