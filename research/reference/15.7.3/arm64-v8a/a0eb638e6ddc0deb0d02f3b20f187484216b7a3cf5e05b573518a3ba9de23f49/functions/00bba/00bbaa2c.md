# 00bbaa2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bba964`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0078.md#compare-3e33183f14e253a74a4465eeb69e7434)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaa2c",
  "name": "FUN_00bbaa2c",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b",
  "source_text_sha256": "3c4a59b84a0dec90c688fdb2338a13d3aed80cdc07faf334dbb6d99edda8781b"
}
~~~

## 呼び出し元

- [00bba9a0](../00bba/00bba9a0.md)
- [00bd5144](../00bd5/00bd5144.md)
- [00bd524c](../00bd5/00bd524c.md)
- [00bd5414](../00bd5/00bd5414.md)
- [00bd56c4](../00bd5/00bd56c4.md)
- [00bd5a94](../00bd5/00bd5a94.md)
- [00bd6030](../00bd6/00bd6030.md)
- [00bd63f4](../00bd6/00bd63f4.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)

## 関連文字列（未確認候補）

~~~text
"terminate_handler unexpectedly returned"
~~~

## 疑似コード / UTF-8 264 bytes

~~~c

void FUN_00bbaa2c(code *param_1)

{
                    /* catch() { ... } // from try @ 00bb3920 with catch @ 00bbaa30 */
  (*param_1)();
                    /* WARNING: Subroutine does not return */
  FUN_00bbb158("terminate_handler unexpectedly returned");
}

~~~
