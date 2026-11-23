# 00bdced0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/alignment_unresolved-0005.md#compare-e280f79ba33b3d9f4a4e3232e7814100)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdced0",
  "name": "_ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e45d01be62f49d0d9610d9635b6e340880827b8b74c2880caeb793e1c121f17c",
  "source_text_sha256": "e45d01be62f49d0d9610d9635b6e340880827b8b74c2880caeb793e1c121f17c"
}
~~~

## 呼び出し元

- [004ec8c8](../004ec/004ec8c8.md)
- [004fdfd8](../004fd/004fdfd8.md)

## 呼び出し先

- [004eca70](../004ec/004eca70.md)

## 疑似コード / UTF-8 282 bytes

~~~c

void _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv(void)

{
                    /* try { // try from 00bdced4 to 00cdceeb has its CatchHandler @ 00bdd2ac */
  (*(code *)PTR__ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv_00c1d020)();
  return;
}

~~~
