# 00bdcbd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcb80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0015.md#compare-07ef421e02efa8da29870a615ae46ce2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbd0",
  "name": "_ZNK5Botan7X509_DN14get_attributesEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a54df21192fc78057b25298f0a17b9d400289262fa0e000b53521a625023e876",
  "source_text_sha256": "a54df21192fc78057b25298f0a17b9d400289262fa0e000b53521a625023e876"
}
~~~

## 呼び出し元

- [004deb5c](../004de/004deb5c.md)
- [004e50d0](../004e5/004e50d0.md)
- [004f1c30](../004f1/004f1c30.md)
- [004f1ecc](../004f1/004f1ecc.md)
- [00503af8](../00503/00503af8.md)

## 呼び出し先

- [004e5c34](../004e5/004e5c34.md)

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZNK5Botan7X509_DN14get_attributesEv(void)

{
  (*(code *)PTR__ZNK5Botan7X509_DN14get_attributesEv_00c1cea0)();
  return;
}

~~~
