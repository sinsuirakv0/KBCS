# 00aedb1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aedb1c",
  "name": "_ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1ccf50e1b1545f3f3d7ff14da6d76808bb626af1c89087d0d3f2e1aaed86d58",
  "source_text_sha256": "a1ccf50e1b1545f3f3d7ff14da6d76808bb626af1c89087d0d3f2e1aaed86d58"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 209 bytes

~~~c

undefined8 _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (2 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0a00)[param_1];
}

~~~
