# 00b4aedc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b4aedc.md)

## 関数情報

~~~json
{
  "address": "00b4aedc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c343783ae64d748d46c737facda25cfed08608f552bc9f3cbe4eaf2d43d93781",
  "source_text_sha256": "c343783ae64d748d46c737facda25cfed08608f552bc9f3cbe4eaf2d43d93781"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~
## 疑似コード 1/1 / UTF-8 1344 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae3c with catch @ 00b4aedc
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae1c with catch @ 00b4aee0
                        */
  if (DAT_010a1058 == 0) {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4adf8 with catch @ 00b4aef8
                        */
    DAT_010a1058 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",param_3)
    ;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4add4 with catch @ 00b4af10
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae84 with catch @ 00b4af18
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00b4ae54 with catch @ 00b4af1c
                        */
  return DAT_010a1058;
}

~~~
