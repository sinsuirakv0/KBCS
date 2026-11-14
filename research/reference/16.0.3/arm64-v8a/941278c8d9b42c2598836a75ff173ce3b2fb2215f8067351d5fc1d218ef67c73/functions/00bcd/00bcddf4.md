# 00bcddf4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcddf4",
  "name": "_ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e1dd7da179bf9e86fce94e67f08b88a389b31269f5ef98d5cc1fb27471c35b7",
  "source_text_sha256": "5e1dd7da179bf9e86fce94e67f08b88a389b31269f5ef98d5cc1fb27471c35b7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

## 疑似コード / UTF-8 654 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_011278d8 == 0) {
    DAT_011278d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",param_3);
  }
                    /* try { // try from 00bcde30 to 00ccde47 has its CatchHandler @ 00bcf95c */
  return DAT_011278d8;
}

~~~
