# 00ae0cac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00ae0cac.md)

## 関数情報

~~~json
{
  "address": "00ae0cac",
  "name": "_ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "692ed032d2374547aaea0609d88e7ab30a5c1423b96a336fad3a6c280c87d137",
  "source_text_sha256": "692ed032d2374547aaea0609d88e7ab30a5c1423b96a336fad3a6c280c87d137"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~
## 疑似コード 1/1 / UTF-8 449 bytes

~~~c

long _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0118 == 0) {
    DAT_010a0118 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0118;
}

~~~
