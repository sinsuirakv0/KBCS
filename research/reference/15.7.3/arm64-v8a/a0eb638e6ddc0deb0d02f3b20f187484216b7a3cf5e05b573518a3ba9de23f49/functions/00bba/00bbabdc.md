# 00bbabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbab14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0010.md#compare-acd312b093b3105b48154d4149274a5a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabdc",
  "name": "_ZSt14set_unexpectedPFvvE",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696",
  "source_text_sha256": "2528d91edbbb2871e2d91662c615e20378ae582b14e3fa1dc9fc7031f3acc696"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd6d90](../00bd6/00bd6d90.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void _ZSt14set_unexpectedPFvvE(code *param_1)

{
  code *pcVar1;
  
  pcVar1 = FUN_00bbabbc;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  FUN_00bd6d90(pcVar1,PTR___cxa_unexpected_handler_00c1bfa8);
                    /* catch() { ... } // from try @ 00bb3784 with catch @ 00bbac04 */
  return;
}

~~~
