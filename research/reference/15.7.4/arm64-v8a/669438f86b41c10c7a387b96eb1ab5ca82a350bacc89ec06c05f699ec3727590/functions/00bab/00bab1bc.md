# 00bab1bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bab178`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab178.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0016.md#compare-d2b1fc00ee923d02f33d779dfcac0bd1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab1bc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528",
  "source_text_sha256": "45fe53473140a7dc77d77db6c65ec0b224ebf891d9e2247b683882857a220528"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1580](../00be1/00be1580.md)
- [00be1b10](../00be1/00be1b10.md)

## 疑似コード / UTF-8 449 bytes

~~~c

int _ZNKSt6__ndk112ctype_bynameIwE9do_narrowEwc(long param_1,wint_t param_2,int param_3)

{
  int iVar1;
  __locale_t __dataset;
  
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  iVar1 = wctob(param_2);
  if (__dataset != (__locale_t)0x0) {
    uselocale(__dataset);
  }
  if (iVar1 != -1) {
    param_3 = iVar1;
  }
                    /* try { // try from 00bab210 to 00cab21b has its CatchHandler @ 00bab494 */
  return param_3;
}

~~~
