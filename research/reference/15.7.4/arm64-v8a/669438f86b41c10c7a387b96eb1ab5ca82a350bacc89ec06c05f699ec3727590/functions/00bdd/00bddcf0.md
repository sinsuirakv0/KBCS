# 00bddcf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddca0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0018.md#compare-deab577b2c619ab89f47a606c4610b5e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcf0",
  "name": "_ZNSt6__ndk19to_stringEx",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2dce9af106d7e5a376dcff40e23a9acac1b34c65fdaf8bde6fa6e1c4e4e04bd8",
  "source_text_sha256": "2dce9af106d7e5a376dcff40e23a9acac1b34c65fdaf8bde6fa6e1c4e4e04bd8"
}
~~~

## 呼び出し元

- [008a2cac](../008a2/008a2cac.md)
- [00ad1238](../00ad1/00ad1238.md)

## 呼び出し先

- [00b7963c](../00b79/00b7963c.md)

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZNSt6__ndk19to_stringEx(void)

{
  (*(code *)PTR__ZNSt6__ndk19to_stringEx_00c1d730)();
  return;
}

~~~
