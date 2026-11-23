# 00bdcfe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcf30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0015.md#compare-94585710efd49528a081cc6e2e54207a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfe0",
  "name": "_ZNK5Botan11X509_Object10BER_encodeEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6051f169e3cc8c10b63beb32697b5cb54918f4df7d3a9f3e52326f2dca4b99d7",
  "source_text_sha256": "6051f169e3cc8c10b63beb32697b5cb54918f4df7d3a9f3e52326f2dca4b99d7"
}
~~~

## 呼び出し元

- [004fc5bc](../004fc/004fc5bc.md)
- [0050168c](../00501/0050168c.md)
- [0050645c](../00506/0050645c.md)
- [00506ee0](../00506/00506ee0.md)

## 呼び出し先

- [004fc4b0](../004fc/004fc4b0.md)

## 疑似コード / UTF-8 133 bytes

~~~c

void _ZNK5Botan11X509_Object10BER_encodeEv(void)

{
  (*(code *)PTR__ZNK5Botan11X509_Object10BER_encodeEv_00c1d080)();
  return;
}

~~~
