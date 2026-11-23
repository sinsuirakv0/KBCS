# 00bdcdb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/alignment_unresolved-0005.md#compare-65a2f67c31b1f8192fed2791220ff90b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdb0",
  "name": "_ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5244bc4111b04157be017952fe9d706323a19e73b91b1cade6720d855794cd21",
  "source_text_sha256": "5244bc4111b04157be017952fe9d706323a19e73b91b1cade6720d855794cd21"
}
~~~

## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)

## 呼び出し先

- [004e85ec](../004e8/004e85ec.md)

## 疑似コード / UTF-8 193 bytes

~~~c

void _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE(void)

{
  (*(code *)PTR__ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE_00c1cf90)();
  return;
}

~~~
