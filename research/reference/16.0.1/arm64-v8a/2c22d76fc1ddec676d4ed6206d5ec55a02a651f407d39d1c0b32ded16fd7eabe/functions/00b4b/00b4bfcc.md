# 00b4bfcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b4bfcc",
  "name": "_ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37e63ac54e774efd27292c01a7d24b8253cce8f19519b327f67e652f876da48b",
  "source_text_sha256": "37e63ac54e774efd27292c01a7d24b8253cce8f19519b327f67e652f876da48b"
}
~~~

## 呼び出し元

- [00c5b560](../00c5b/00c5b560.md)

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01125bc8)[param_1];
}

~~~
