# 00bccfe0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bccfe0",
  "name": "_ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "818b964c6a1886c4258a06297e6642b1623a1855665db2ccab2e217b4673c033",
  "source_text_sha256": "818b964c6a1886c4258a06297e6642b1623a1855665db2ccab2e217b4673c033"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

## 疑似コード / UTF-8 319 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bccfe8 to 00ccd0f7 has its CatchHandler @ 00bcc640 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01126928)[param_1];
}

~~~
