# 00aec0bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aec1c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aec0bc",
  "name": "_ZN8firebase4util4list11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e8b2c3de0796be6c159616dda405a26eae34a9150fce61fad63093349e59fbe",
  "source_text_sha256": "1e8b2c3de0796be6c159616dda405a26eae34a9150fce61fad63093349e59fbe"
}
~~~

## 呼び出し元

- [00bde5a0](../00bde/00bde5a0.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 204 bytes

~~~c

undefined8 _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (2 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0830)[param_1];
}

~~~
