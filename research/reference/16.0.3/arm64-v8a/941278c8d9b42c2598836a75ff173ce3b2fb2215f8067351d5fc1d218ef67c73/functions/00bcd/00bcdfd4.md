# 00bcdfd4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcdfd4",
  "name": "_ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2aaa0a17fdf0c562c53af59a487d5a9a54c8a50738a32206f05354acf769a464",
  "source_text_sha256": "2aaa0a17fdf0c562c53af59a487d5a9a54c8a50738a32206f05354acf769a464"
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

## 疑似コード / UTF-8 319 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bcdfdc to 00cce0eb has its CatchHandler @ 00bcd634 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_011278e8)[param_1];
}

~~~
