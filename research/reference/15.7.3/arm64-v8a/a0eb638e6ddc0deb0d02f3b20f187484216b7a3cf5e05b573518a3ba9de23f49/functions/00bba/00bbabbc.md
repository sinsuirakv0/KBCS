# 00bbabbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbaaf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0078.md#compare-82f26159aaf0038f9ada00043b253df8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabbc",
  "name": "FUN_00bbabbc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a",
  "source_text_sha256": "8b8622db1d8e450b225c0c01ccff765112b1570972b07fbae74fe7d1f56cca8a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)

## 関連文字列（未確認候補）

~~~text
"unexpected"
~~~

## 疑似コード / UTF-8 426 bytes

~~~c

void FUN_00bbabbc(void)

{
                    /* catch() { ... } // from try @ 00bb7bb4 with catch @ 00bbabc0 */
                    /* catch() { ... } // from try @ 00bb3764 with catch @ 00bbabc4 */
                    /* catch() { ... } // from try @ 00bb3770 with catch @ 00bbabd4 */
  PTR_s_uncaught_00c24950 = s_unexpected_002a11af;
                    /* WARNING: Subroutine does not return */
  _ZSt9terminatev();
}

~~~
