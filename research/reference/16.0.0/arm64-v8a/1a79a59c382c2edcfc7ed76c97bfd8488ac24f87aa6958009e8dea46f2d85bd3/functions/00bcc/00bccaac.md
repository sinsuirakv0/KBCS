# 00bccaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bccaac",
  "name": "_ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c549cd155bb6e870de0031ca56b28f72ca41427dd340d542d81b6b5ce2a3f7e",
  "source_text_sha256": "5c549cd155bb6e870de0031ca56b28f72ca41427dd340d542d81b6b5ce2a3f7e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)
- [00c5ab30](../00c5a/00c5ab30.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

## 疑似コード / UTF-8 843 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126418 == 0) {
    DAT_01126418 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0);
  }
                    /* try { // try from 00bccb04 to 00cccb1b has its CatchHandler @ 00bce700 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126418,&PTR_s_<init>_00c91780,2,&DAT_01126428,
             "com/google/firebase/auth/internal/cpp/JniIdTokenListener");
  return;
}

~~~
