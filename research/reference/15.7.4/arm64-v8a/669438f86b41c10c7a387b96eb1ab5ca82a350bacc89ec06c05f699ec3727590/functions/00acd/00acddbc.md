# 00acddbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acdd78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0060.md#compare-d97ac59336ad01cf6c8b1e4a2bdb0a0c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acddbc",
  "name": "FUN_00acddbc",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683",
  "source_text_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683"
}
~~~

## 呼び出し元

- [00657e7c](../00657/00657e7c.md)

## 呼び出し先

- [00adccd8](../00adc/00adccd8.md)
- [00bdb240](../00bdb/00bdb240.md)

## 疑似コード / UTF-8 188 bytes

~~~c

void FUN_00acddbc(undefined8 *param_1)

{
  FUN_00adccd8();
  *param_1 = &PTR_FUN_00bf7308;
  memset(param_1 + 0x15,0,0x220);
  *(undefined4 *)(param_1 + 0x59) = 0x3f800000;
  return;
}

~~~
