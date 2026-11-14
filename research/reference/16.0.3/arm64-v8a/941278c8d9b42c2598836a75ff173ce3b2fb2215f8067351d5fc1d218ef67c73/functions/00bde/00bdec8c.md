# 00bdec8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdec8c",
  "name": "_ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06e0cda50a760d681fc3de3376299c7d09dd7ec6c3c5d5f89cb5b3409e5d4f24",
  "source_text_sha256": "06e0cda50a760d681fc3de3376299c7d09dd7ec6c3c5d5f89cb5b3409e5d4f24"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

## 疑似コード / UTF-8 503 bytes

~~~c

long _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127ee8 == 0) {
    DAT_01127ee8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/UserProfileChangeRequest$Builder",0);
  }
  return DAT_01127ee8;
}

~~~
