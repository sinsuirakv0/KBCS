# 00bcda2c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcda2c",
  "name": "_ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d73a5b9d16031d14cb2ec468b14e433ea6b644b19be76c3220898145f05207ae",
  "source_text_sha256": "d73a5b9d16031d14cb2ec468b14e433ea6b644b19be76c3220898145f05207ae"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

## 疑似コード / UTF-8 458 bytes

~~~c

long _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011278b0;
}

~~~
