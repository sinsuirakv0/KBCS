# 00bd6ccc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bd6ccc",
  "name": "_ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "daddb01462c08847ea69f43ed9ddf5611d959b145820943e293ae6a50e89b2e7",
  "source_text_sha256": "daddb01462c08847ea69f43ed9ddf5611d959b145820943e293ae6a50e89b2e7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/PhoneAuthOptions$Builder"
~~~

## 疑似コード / UTF-8 503 bytes

~~~c

long _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126b78 == 0) {
    DAT_01126b78 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/PhoneAuthOptions$Builder",
                              0);
  }
  return DAT_01126b78;
}

~~~
