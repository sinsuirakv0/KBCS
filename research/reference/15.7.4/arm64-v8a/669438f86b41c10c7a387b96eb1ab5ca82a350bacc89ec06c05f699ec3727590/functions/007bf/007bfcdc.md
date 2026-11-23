# 007bfcdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007bfcdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcdc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0035.md#compare-7d1b96a2169f003bba1bb166db5a3718)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007bfcdc",
  "name": "FUN_007bfcdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef",
  "source_text_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef"
}
~~~

## 呼び出し元

- [0078cd14](../0078c/0078cd14.md)
- [00796d74](../00796/00796d74.md)
- [007da86c](../007da/007da86c.md)
- [007dbc94](../007db/007dbc94.md)
- [007dc0fc](../007dc/007dc0fc.md)
- [009a3648](../009a3/009a3648.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_007bfcdc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~
