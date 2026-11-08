# 00aeaf3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aeaf3c",
  "name": "_ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5bac7bb43a6c0af641eb42557a79c9cc8a07d69b96d5cbcbcd7c1d9924f1fc29",
  "source_text_sha256": "5bac7bb43a6c0af641eb42557a79c9cc8a07d69b96d5cbcbcd7c1d9924f1fc29"
}
~~~

## 呼び出し元

- [00bde0e0](../00bde/00bde0e0.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0820)[param_1];
}

~~~
