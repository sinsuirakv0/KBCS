# 00bdfbb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfb00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0021.md#compare-6fe71f246703b60fa896adc3df75fd5f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbb0",
  "name": "_ZNK11flatbuffers10Definition19SerializeAttributesEPNS_17FlatBufferBuilderERKNS_6ParserE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "165e266b1aa1f7a2dab9583ab170415fd69fc244d9c87801ad018b97f0a1ae19",
  "source_text_sha256": "165e266b1aa1f7a2dab9583ab170415fd69fc244d9c87801ad018b97f0a1ae19"
}
~~~

## 呼び出し元

- [00b291bc](../00b29/00b291bc.md)
- [00b29458](../00b29/00b29458.md)
- [00b2976c](../00b29/00b2976c.md)
- [00b29a24](../00b29/00b29a24.md)
- [00b2b664](../00b2b/00b2b664.md)

## 呼び出し先

- [00b29c10](../00b29/00b29c10.md)

## 疑似コード / UTF-8 243 bytes

~~~c

void _ZNK11flatbuffers10Definition19SerializeAttributesEPNS_17FlatBufferBuilderERKNS_6ParserE(void)

{
  (*(code *)
    PTR__ZNK11flatbuffers10Definition19SerializeAttributesEPNS_17FlatBufferBuilderERKNS_6ParserE_00c1e668
  )();
  return;
}

~~~
