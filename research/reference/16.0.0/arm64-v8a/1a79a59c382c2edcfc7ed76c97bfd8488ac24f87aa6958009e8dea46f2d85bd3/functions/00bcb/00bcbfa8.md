# 00bcbfa8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcbfa8",
  "name": "_ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "211ae8b90d8a825a56727b64351a80e2f7fd3737342d3be468d1db09c72d47b0",
  "source_text_sha256": "211ae8b90d8a825a56727b64351a80e2f7fd3737342d3be468d1db09c72d47b0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
~~~

## 疑似コード / UTF-8 421 bytes

~~~c

long _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126328 == 0) {
    DAT_01126328 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  return DAT_01126328;
}

~~~
