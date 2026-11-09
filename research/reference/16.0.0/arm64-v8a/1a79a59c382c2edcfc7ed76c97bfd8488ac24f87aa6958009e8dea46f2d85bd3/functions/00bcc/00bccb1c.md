# 00bccb1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bccb1c",
  "name": "_ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef9fcdbad72f14d9140fd777c4e2c38a0e65f242e5a4449899385b298f3c44cb",
  "source_text_sha256": "ef9fcdbad72f14d9140fd777c4e2c38a0e65f242e5a4449899385b298f3c44cb"
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

## 疑似コード / UTF-8 319 bytes

~~~c

undefined8 _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* try { // try from 00bccb1c to 00cccbcf has its CatchHandler @ 00bcc3d4 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01126428)[param_1];
}

~~~
