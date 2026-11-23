# 00a6dedc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a6dedc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6dedc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0020.md#compare-c69c471ab4de32ef7d4d4d04910e3ab7)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6dedc",
  "name": "FUN_00a6dedc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a88d014430c51ae05405a27c242db37130c1510b3ba258099fc9f896b4880179",
  "source_text_sha256": "a88d014430c51ae05405a27c242db37130c1510b3ba258099fc9f896b4880179"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 233 bytes

~~~c

long FUN_00a6dedc(long param_1,long param_2)

{
  param_1 = param_1 + 0x18;
  if (*(char **)(param_2 + 8) !=
      "NSt6__ndk110shared_ptrI6UIViewE27__shared_ptr_default_deleteIS1_S1_EE") {
    param_1 = 0;
  }
  return param_1;
}

~~~
