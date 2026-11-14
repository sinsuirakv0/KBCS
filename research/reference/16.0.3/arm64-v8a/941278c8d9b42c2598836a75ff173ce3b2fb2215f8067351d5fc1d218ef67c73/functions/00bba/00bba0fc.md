# 00bba0fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bba0fc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "306dab41f782aee7f8d8494ff37003f746be6660f1b287b3fc248da2bc475948",
  "source_text_sha256": "306dab41f782aee7f8d8494ff37003f746be6660f1b287b3fc248da2bc475948"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

## 疑似コード / UTF-8 954 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* catch() { ... } // from try @ 00bb9f90 with catch @ 00bba100 */
  if (DAT_011273d8 == 0) {
                    /* catch() { ... } // from try @ 00bb9968 with catch @ 00bba118 */
                    /* catch() { ... } // from try @ 00bb9950 with catch @ 00bba11c */
                    /* catch() { ... } // from try @ 00bb9a08 with catch @ 00bba124 */
    DAT_011273d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
                    /* catch() { ... } // from try @ 00bb9ec4 with catch @ 00bba13c */
  return DAT_011273d8;
}

~~~
