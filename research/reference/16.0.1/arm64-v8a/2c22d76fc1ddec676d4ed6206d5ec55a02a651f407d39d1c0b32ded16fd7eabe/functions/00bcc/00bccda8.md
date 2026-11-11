# 00bccda8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bccda8",
  "name": "_ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c57563c06547892f6b01a59fb822524dcc33838dfdeb649f5d0878ee5fd5820e",
  "source_text_sha256": "c57563c06547892f6b01a59fb822524dcc33838dfdeb649f5d0878ee5fd5820e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

## 疑似コード / UTF-8 699 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126818 == 0) {
                    /* try { // try from 00bccdcc to 00cccde3 has its CatchHandler @ 00bce8f8 */
    DAT_01126818 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0);
  }
                    /* try { // try from 00bccde4 to 00ccce8f has its CatchHandler @ 00bcc5d0 */
  return DAT_01126818;
}

~~~
