# 00bd5ecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd5ecc",
  "name": "_ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "40e5dd97aeebde6a2be40f13108dc214cc89d4335b14be71cd829d31155141ac",
  "source_text_sha256": "40e5dd97aeebde6a2be40f13108dc214cc89d4335b14be71cd829d31155141ac"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/TwitterAuthProvider"
~~~

## 疑似コード / UTF-8 452 bytes

~~~c

long _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126708 == 0) {
    DAT_01126708 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/TwitterAuthProvider",0);
  }
  return DAT_01126708;
}

~~~
