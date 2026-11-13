# 00bd0dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd0dbc",
  "name": "_ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "226858018ad0edb158a39eea0630294f444949ef8e58d1286a938f09bad5b0ff",
  "source_text_sha256": "226858018ad0edb158a39eea0630294f444949ef8e58d1286a938f09bad5b0ff"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

## 疑似コード / UTF-8 244 bytes

~~~c

undefined8 _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_011269a0 + (ulong)param_1 * 8);
}

~~~
