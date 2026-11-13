# 00bd0ebc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd0ebc",
  "name": "_ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "126be4242c4afbf2e0daa33ab79501ada9cb5bd8d8143ed819303ae4d5afc264",
  "source_text_sha256": "126be4242c4afbf2e0daa33ab79501ada9cb5bd8d8143ed819303ae4d5afc264"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/FirebaseApiNotAvailableException"
~~~

## 疑似コード / UTF-8 604 bytes

~~~c

long _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011269a8 == 0) {
                    /* try { // try from 00bd0ee4 to 00cd0eeb has its CatchHandler @ 00bd67c8 */
    DAT_011269a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/FirebaseApiNotAvailableException",0);
  }
  return DAT_011269a8;
}

~~~
