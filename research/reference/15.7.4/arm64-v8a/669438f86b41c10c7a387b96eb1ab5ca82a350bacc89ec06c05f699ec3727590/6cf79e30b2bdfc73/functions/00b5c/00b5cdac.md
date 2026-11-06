# 00b5cdac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00b5cdac.md)

## 関数情報

~~~json
{
  "address": "00b5cdac",
  "name": "_ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a8d0758722b284965fb843cddb73ad2fec3b84d6ca6f34ebe23c25e35015bead",
  "source_text_sha256": "a8d0758722b284965fb843cddb73ad2fec3b84d6ca6f34ebe23c25e35015bead"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
~~~
## 疑似コード 1/1 / UTF-8 545 bytes

~~~c

long _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a14c8 == 0) {
    DAT_010a14c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult",
                              param_3);
  }
  return DAT_010a14c8;
}

~~~
