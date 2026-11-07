# 00aedd0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aedc00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aedd0c",
  "name": "_ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "34330fcfe4bc5c2cfbc90a6a876cf9e8ed1369225e36abb7b8ee7ef0b6d2e055",
  "source_text_sha256": "34330fcfe4bc5c2cfbc90a6a876cf9e8ed1369225e36abb7b8ee7ef0b6d2e055"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~

## 疑似コード / UTF-8 398 bytes

~~~c

long _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a60 == 0) {
    DAT_010a0a60 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/net/Uri",0);
  }
  return DAT_010a0a60;
}

~~~
