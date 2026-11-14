# 00bcdaf0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcdaf0",
  "name": "_ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64286d87977ec6eb99b347a841d6870299eba27b3e1b88cce9ed6a14d3a8da0f",
  "source_text_sha256": "64286d87977ec6eb99b347a841d6870299eba27b3e1b88cce9ed6a14d3a8da0f"
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

## 疑似コード / UTF-8 497 bytes

~~~c

long _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  return DAT_011278b0;
}

~~~
