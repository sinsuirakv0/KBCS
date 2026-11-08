# 00ae0cec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae0cec",
  "name": "_ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60190da88929e560b7d32ef305749b420f6ea0c80426412ea20299c0ade3cdd8",
  "source_text_sha256": "60190da88929e560b7d32ef305749b420f6ea0c80426412ea20299c0ade3cdd8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~

## 疑似コード / UTF-8 951 bytes

~~~c

long _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a00d8 == 0) {
    DAT_010a00d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus",0);
  }
                    /* try { // try from 00ae0d20 to 00be0f0b has its CatchHandler @ 00ae0d20
                       catch() { ... } // from try @ 00ae0d20 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae0f14 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae0f98 with catch @ 00ae0d20
                       catch() { ... } // from try @ 00ae1004 with catch @ 00ae0d20 */
  return DAT_010a00d8;
}

~~~
