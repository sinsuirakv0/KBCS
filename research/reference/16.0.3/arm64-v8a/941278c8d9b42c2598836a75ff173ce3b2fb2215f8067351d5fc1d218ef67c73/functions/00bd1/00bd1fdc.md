# 00bd1fdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bd1fdc",
  "name": "_ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "318d0e10861e39da27fd9d1c9718f50fe1dcaa553a0f6cb94c483f13e3b0b7ef",
  "source_text_sha256": "318d0e10861e39da27fd9d1c9718f50fe1dcaa553a0f6cb94c483f13e3b0b7ef"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
~~~

## 疑似コード / UTF-8 929 bytes

~~~c

void _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bd1fe0 to 00cd1fe3 has its CatchHandler @ 00bd77ac */
  if (DAT_01127968 == 0) {
    DAT_01127968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/FirebaseApiNotAvailableException",0);
                    /* try { // try from 00bd2018 to 00cd205f has its CatchHandler @ 00bd7898 */
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01127968,&DAT_0030fdb0,1,&DAT_01127978,
             "com/google/firebase/FirebaseApiNotAvailableException");
  return;
}

~~~
