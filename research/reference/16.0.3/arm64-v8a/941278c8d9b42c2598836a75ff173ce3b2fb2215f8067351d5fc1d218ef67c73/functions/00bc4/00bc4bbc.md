# 00bc4bbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc4bbc",
  "name": "_ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eaa88eae6a17a02bd6d2d0631cb44484c33c29bd0a15fd804ae3eb527a4cd41b",
  "source_text_sha256": "eaa88eae6a17a02bd6d2d0631cb44484c33c29bd0a15fd804ae3eb527a4cd41b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 266 bytes

~~~c

undefined8
_ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE
          (uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01127768)[param_1];
}

~~~
