# 00b4aacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b4aacc",
  "name": "_ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b344c9721096906b5004fe0d447d2cc2b40e93d44dcceb9c856bbfc6098b2355",
  "source_text_sha256": "b344c9721096906b5004fe0d447d2cc2b40e93d44dcceb9c856bbfc6098b2355"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

## 疑似コード / UTF-8 763 bytes

~~~c

long _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00b4aae0 to 00c4aaeb has its CatchHandler @ 00b4ac38 */
  if (DAT_010a0ef8 == 0) {
                    /* try { // try from 00b4aaec to 00c4ab0b has its CatchHandler @ 00b4ace8 */
    DAT_010a0ef8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
  }
                    /* try { // try from 00b4ab0c to 00c4ab27 has its CatchHandler @ 00b4acdc */
  return DAT_010a0ef8;
}

~~~
