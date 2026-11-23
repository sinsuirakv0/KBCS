# 00baafcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baaf88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0016.md#compare-2294eea507136f6f51529ea6f973a4bf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baafcc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d2d5f11b739a85d4fa5c635368db1415bd51266aca71637165f8618c855addd",
  "source_text_sha256": "9d2d5f11b739a85d4fa5c635368db1415bd51266aca71637165f8618c855addd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1ae0](../00be1/00be1ae0.md)

## 疑似コード / UTF-8 638 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEPwPKw
                   (long param_1,wint_t *param_2,wint_t *param_3)

{
  wint_t *pwVar1;
  wint_t wVar2;
  
  pwVar1 = param_2;
                    /* try { // try from 00baafe8 to 00cab20f has its CatchHandler @ 00baafe8
                       catch() { ... } // from try @ 00baafe8 with catch @ 00baafe8
                       catch() { ... } // from try @ 00bab21c with catch @ 00baafe8 */
  for (; param_2 != param_3; param_2 = param_2 + 1) {
    wVar2 = towupper_l(*param_2,*(__locale_t *)(param_1 + 0x10));
    *param_2 = wVar2;
    pwVar1 = param_3;
  }
  return pwVar1;
}

~~~
