# 005bcdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `005bcdec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcdec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/no_difference_in_scope-0004.md#compare-ff1577116ccc668330a3995ef5ee52f5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005bcdec",
  "name": "FUN_005bcdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758",
  "source_text_sha256": "9d5aaa47432c3d651ab9917043ad384985d81d7dca96828ca01ecc03b7379758"
}
~~~

## 呼び出し元

- [006ee6c8](../006ee/006ee6c8.md)
- [009f4ab8](../009f4/009f4ab8.md)
- [009f5650](../009f5/009f5650.md)

## 呼び出し先

- [005bc280](../005bc/005bc280.md)

## 疑似コード / UTF-8 95 bytes

~~~c

bool FUN_005bcdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005bc280();
  return iVar1 != -1;
}

~~~
