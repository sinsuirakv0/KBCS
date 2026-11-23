# 00a6aacc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a6aa88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6a/00a6aa88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/no_difference_in_scope-0018.md#compare-12ab52a73127e10ec97a58bd748a6e02)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6aacc",
  "name": "FUN_00a6aacc",
  "size": 12,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2acd81ca2db2029df79739c6f10627326aee9a564caedb25ef22ea3b4ce3693",
  "source_text_sha256": "a2acd81ca2db2029df79739c6f10627326aee9a564caedb25ef22ea3b4ce3693"
}
~~~

## 呼び出し元

- [0075f73c](../0075f/0075f73c.md)
- [008920f8](../00892/008920f8.md)
- [00a1450c](../00a14/00a1450c.md)
- [00a1e2e4](../00a1e/00a1e2e4.md)
- [00a20624](../00a20/00a20624.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 88 bytes

~~~c

void FUN_00a6aacc(long param_1)

{
  *(undefined1 *)(param_1 + 0x3f) = 1;
  return;
}

~~~
