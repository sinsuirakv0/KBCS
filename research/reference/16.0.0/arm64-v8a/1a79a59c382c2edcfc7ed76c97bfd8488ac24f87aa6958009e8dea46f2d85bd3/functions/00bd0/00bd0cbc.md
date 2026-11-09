# 00bd0cbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd0cbc",
  "name": "_ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "81d95053edf923cbec0b7027e247832931842d02df54a1c05406d0e286603090",
  "source_text_sha256": "81d95053edf923cbec0b7027e247832931842d02df54a1c05406d0e286603090"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuthActionCodeException"
~~~

## 疑似コード / UTF-8 635 bytes

~~~c

long _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
                    /* try { // try from 00bd0ccc to 00cd0ce7 has its CatchHandler @ 00bd65d0 */
  if (DAT_011264c8 == 0) {
    DAT_011264c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
                    /* try { // try from 00bd0ce8 to 00cd0d7f has its CatchHandler @ 00bd075c */
  }
  return DAT_011264c8;
}

~~~
