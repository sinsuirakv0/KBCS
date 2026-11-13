# 00bc1fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bc1fec",
  "name": "_ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b",
  "source_text_sha256": "55fcac3e8b2a9914a42096a091da98be5623082a6b0b300b639778f5587bb62b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
~~~

## 疑似コード / UTF-8 711 bytes

~~~c

long _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bc1ff4 to 00cc1ffb has its CatchHandler @ 00bc2214 */
                    /* try { // try from 00bc1ffc to 00cc200f has its CatchHandler @ 00bc21a8 */
  if (DAT_01126620 == 0) {
    DAT_01126620 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/remoteconfig/FirebaseRemoteConfigValue",0);
  }
  return DAT_01126620;
}

~~~
