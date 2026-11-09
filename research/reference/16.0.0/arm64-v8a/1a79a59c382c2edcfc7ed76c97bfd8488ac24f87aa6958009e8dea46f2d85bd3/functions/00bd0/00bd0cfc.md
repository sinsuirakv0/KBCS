# 00bd0cfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bd0cfc",
  "name": "_ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a5ab2d529eaaf89847df29a3b6bc0352a9c1867e33d0fb8736c2f1f088b8eb7",
  "source_text_sha256": "5a5ab2d529eaaf89847df29a3b6bc0352a9c1867e33d0fb8736c2f1f088b8eb7"
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

## 疑似コード / UTF-8 557 bytes

~~~c

long _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_011264c8 == 0) {
    DAT_011264c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/FirebaseAuthActionCodeException",param_3);
  }
  return DAT_011264c8;
}

~~~
