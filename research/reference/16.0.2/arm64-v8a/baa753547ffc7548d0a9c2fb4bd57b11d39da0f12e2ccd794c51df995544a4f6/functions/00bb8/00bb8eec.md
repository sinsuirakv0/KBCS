# 00bb8eec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bb8eec",
  "name": "_ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aae575e987bdd6dd3b631535da33bfbc8fbfc8744b83e4ac1a9c6ca11c7264f7",
  "source_text_sha256": "aae575e987bdd6dd3b631535da33bfbc8fbfc8744b83e4ac1a9c6ca11c7264f7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

## 疑似コード / UTF-8 814 bytes

~~~c

void _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011263a8 == 0) {
    DAT_011263a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
  }
                    /* try { // try from 00bb8f54 to 00cb8f67 has its CatchHandler @ 00bb90f0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011263a8,&PTR_s_isAutoInitEnabled_00c91390,0xb,&DAT_011263b8,
             "com/google/firebase/messaging/FirebaseMessaging");
  return;
}

~~~
