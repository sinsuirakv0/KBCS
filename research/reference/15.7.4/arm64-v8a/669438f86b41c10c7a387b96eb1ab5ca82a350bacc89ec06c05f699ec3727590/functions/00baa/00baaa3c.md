# 00baaa3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baa9f8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa9f8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0016.md#compare-dcc7374beb6ecb83c8bbf9e5b1b41785)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaa3c",
  "name": "_ZNSt6__ndk112ctype_bynameIwED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "317cefbb9f0fbbbb4aaa4cc5f9d3cf30b1d25a3fede2369ebf22590870e70cf9",
  "source_text_sha256": "317cefbb9f0fbbbb4aaa4cc5f9d3cf30b1d25a3fede2369ebf22590870e70cf9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00be1a40](../00be1/00be1a40.md)

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZNSt6__ndk112ctype_bynameIwED0Ev(void *param_1)

{
  _ZNSt6__ndk112ctype_bynameIwED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~
