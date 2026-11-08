# 00b4aedc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b4aedc",
  "name": "_ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e537aa33ca5a87f6e85f5d4f62501a622c77413f88ec28b6b4f98259c496a1d9",
  "source_text_sha256": "e537aa33ca5a87f6e85f5d4f62501a622c77413f88ec28b6b4f98259c496a1d9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

## 疑似コード / UTF-8 519 bytes

~~~c

long _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a1018 == 0) {
    DAT_010a1018 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
  return DAT_010a1018;
}

~~~
