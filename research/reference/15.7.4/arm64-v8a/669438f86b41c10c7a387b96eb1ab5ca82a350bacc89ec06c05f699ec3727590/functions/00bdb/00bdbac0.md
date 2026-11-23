# 00bdbac0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdba70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0013.md#compare-0897549e2bd677981085cbaa5809ec30)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbac0",
  "name": "_ZNK5Botan9X509_Time15readable_stringEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "159f546fff79315d8c71466a0c22f6bbec30bade000a58135908ffa9a38b668d",
  "source_text_sha256": "159f546fff79315d8c71466a0c22f6bbec30bade000a58135908ffa9a38b668d"
}
~~~

## 呼び出し元

- [00485f54](../00485/00485f54.md)
- [0048b804](../0048b/0048b804.md)
- [00501b08](../00501/00501b08.md)

## 呼び出し先

- [0048930c](../00489/0048930c.md)

## 疑似コード / UTF-8 137 bytes

~~~c

void _ZNK5Botan9X509_Time15readable_stringEv(void)

{
  (*(code *)PTR__ZNK5Botan9X509_Time15readable_stringEv_00c1c618)();
  return;
}

~~~
