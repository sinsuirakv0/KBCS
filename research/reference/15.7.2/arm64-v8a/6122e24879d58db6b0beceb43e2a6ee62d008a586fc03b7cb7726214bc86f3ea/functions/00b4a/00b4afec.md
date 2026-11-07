# 00b4afec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b4b0f8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0f8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b4afec",
  "name": "_ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2dcba016422c37eba8a4cc7b071a5d9ea7b09013204c6ab10ba8fc1d8cb1e7cc",
  "source_text_sha256": "2dcba016422c37eba8a4cc7b071a5d9ea7b09013204c6ab10ba8fc1d8cb1e7cc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

## 疑似コード / UTF-8 1037 bytes

~~~c

void _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00b4b000 to 00c4b00b has its CatchHandler @ 00b4b140 */
  if (DAT_010a0f58 == 0) {
    DAT_010a0f58 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
                    /* try { // try from 00b4b030 to 00c4b03b has its CatchHandler @ 00b4b13c */
                    /* try { // try from 00b4b054 to 00c4b05f has its CatchHandler @ 00b4b138 */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0f58,&DAT_002f8900,1,&DAT_010a0f70,
             "com/google/firebase/messaging/cpp/RegistrationIntentService");
  return;
}

~~~
