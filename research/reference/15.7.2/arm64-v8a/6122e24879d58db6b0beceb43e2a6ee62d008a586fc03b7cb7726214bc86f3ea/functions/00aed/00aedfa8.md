# 00aedfa8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aedfa8",
  "name": "_ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0e8e6c8738e2fc024be2ab1c3c72cd69eca064105d4f1d1987a747a358b51b8",
  "source_text_sha256": "d0e8e6c8738e2fc024be2ab1c3c72cd69eca064105d4f1d1987a747a358b51b8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Object"
~~~

## 疑似コード / UTF-8 402 bytes

~~~c

long _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0988 == 0) {
    DAT_010a0988 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Object",0);
  }
  return DAT_010a0988;
}

~~~
