# 00b6ddbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b6dec8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6dec8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b6ddbc",
  "name": "_ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9cd9d9db9ce601c0a578f597f44728d8c6b6110440d508967f41acd222bdd740",
  "source_text_sha256": "9cd9d9db9ce601c0a578f597f44728d8c6b6110440d508967f41acd222bdd740"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

## 疑似コード / UTF-8 551 bytes

~~~c

long _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
                    /* try { // try from 00b6ddc4 to 00c6de43 has its CatchHandler @ 00b6dd58 */
  if (DAT_010a19f8 == 0) {
    DAT_010a19f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a19f8;
}

~~~
