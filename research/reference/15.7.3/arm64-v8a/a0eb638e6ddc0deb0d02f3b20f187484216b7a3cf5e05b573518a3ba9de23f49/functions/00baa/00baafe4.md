# 00baafe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baaf1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/machine_only_observed-0044.md#compare-ec85a3959b19f49ef835fcdc89dbf183)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baafe4",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f",
  "source_text_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1aa0](../00be1/00be1aa0.md)

## 疑似コード / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towlower_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~
