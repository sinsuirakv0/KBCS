# 00bd1bfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd1bfc",
  "name": "_ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d58951253f12e54ae690aeecde9e120164f02c349f40974c1d7045b04259c846",
  "source_text_sha256": "d58951253f12e54ae690aeecde9e120164f02c349f40974c1d7045b04259c846"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ac00](../00c5a/00c5ac00.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 250 bytes

~~~c

undefined8 _ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_01126558 + (ulong)param_1 * 8);
}

~~~
