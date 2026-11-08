# 00aea7ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aea7ec",
  "name": "_ZN8firebase4util4file11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2417ebbd3b90ab5e11daa1d3bc8270dec7dbd47d9e3d0ae212a522abfb9945c6",
  "source_text_sha256": "2417ebbd3b90ab5e11daa1d3bc8270dec7dbd47d9e3d0ae212a522abfb9945c6"
}
~~~

## 呼び出し元

- [00bde640](../00bde/00bde640.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 204 bytes

~~~c

undefined8 _ZN8firebase4util4file11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (7 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a07a0)[param_1];
}

~~~
