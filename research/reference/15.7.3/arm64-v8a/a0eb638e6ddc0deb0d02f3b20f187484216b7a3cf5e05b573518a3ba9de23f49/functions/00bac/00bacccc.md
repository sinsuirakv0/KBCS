# 00bacccc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bacc04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacc04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/detail_skipped-0023.md#compare-b07692bd41d4b44acce04a010ed3d6ad)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacccc",
  "name": "_ZNKSt6__ndk17codecvtIDic9mbstate_tE9do_lengthERS1_PKcS5_m",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8381f350b4a7cad586b8f9fbbf25c841f7eeec8716d6e8ac2dcc7ca00ba221f1",
  "source_text_sha256": "8381f350b4a7cad586b8f9fbbf25c841f7eeec8716d6e8ac2dcc7ca00ba221f1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bacce8](../00bac/00bacce8.md)

## 疑似コード / UTF-8 261 bytes

~~~c

void _ZNKSt6__ndk17codecvtIDic9mbstate_tE9do_lengthERS1_PKcS5_m
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bacce8(param_3,param_4,param_5,0x10ffff,0);
  return;
}

~~~
