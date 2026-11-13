# 00bd5cbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd5cbc",
  "name": "_ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "394daf7043d4b73f879c7c53fc4c973dde0d8e002438513526ab68ba632b3615",
  "source_text_sha256": "394daf7043d4b73f879c7c53fc4c973dde0d8e002438513526ab68ba632b3615"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GoogleAuthProvider"
~~~

## 疑似コード / UTF-8 533 bytes

~~~c

long _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01126bc8 == 0) {
    DAT_01126bc8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GoogleAuthProvider",
                              param_3);
  }
  return DAT_01126bc8;
}

~~~
