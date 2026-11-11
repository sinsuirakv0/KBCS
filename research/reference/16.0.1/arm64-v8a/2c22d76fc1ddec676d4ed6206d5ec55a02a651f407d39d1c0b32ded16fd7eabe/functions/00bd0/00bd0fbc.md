# 00bd0fbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bd0fbc",
  "name": "_ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a204969b5e00d4544d4797b02427fbc7ace04d6188b6782f7d4532321d6cedf2",
  "source_text_sha256": "a204969b5e00d4544d4797b02427fbc7ace04d6188b6782f7d4532321d6cedf2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 255 bytes

~~~c

undefined8 _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_011268b8 + (ulong)param_1 * 8);
}

~~~
