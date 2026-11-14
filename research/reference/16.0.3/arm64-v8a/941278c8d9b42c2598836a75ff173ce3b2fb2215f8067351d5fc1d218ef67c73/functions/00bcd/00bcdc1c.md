# 00bcdc1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcdc1c",
  "name": "_ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f9e6ec1da3372e679310581bc8bd950819dd3081eee0a23a424bc616b90c073",
  "source_text_sha256": "5f9e6ec1da3372e679310581bc8bd950819dd3081eee0a23a424bc616b90c073"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

## 疑似コード / UTF-8 934 bytes

~~~c

void _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bcdc20 to 00ccdc37 has its CatchHandler @ 00bcf968 */
                    /* try { // try from 00bcdc38 to 00ccdc93 has its CatchHandler @ 00bcd634 */
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011278b0,&PTR_s_<init>_00c92bf0,2,&DAT_011278c0,
             "com/google/firebase/auth/internal/cpp/JniAuthStateListener");
  return;
}

~~~
