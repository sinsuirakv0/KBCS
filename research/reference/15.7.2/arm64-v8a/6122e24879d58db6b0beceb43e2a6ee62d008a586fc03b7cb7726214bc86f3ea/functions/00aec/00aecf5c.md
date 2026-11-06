# 00aecf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aecf5c",
  "name": "_ZN8firebase4util3set11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00192ea0942ea6a740fe855789d8a01bc509ea7fa31d1df2af701ac5c3c0b0ef",
  "source_text_sha256": "00192ea0942ea6a740fe855789d8a01bc509ea7fa31d1df2af701ac5c3c0b0ef"
}
~~~

## 呼び出し元

- [00bde580](../00bde/00bde580.md)

## 呼び出し先

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 203 bytes

~~~c

undefined8 _ZN8firebase4util3set11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a08d8)[param_1];
}

~~~
