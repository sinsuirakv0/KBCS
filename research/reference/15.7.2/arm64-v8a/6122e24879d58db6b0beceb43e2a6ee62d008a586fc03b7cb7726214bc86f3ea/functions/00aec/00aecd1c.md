# 00aecd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aecd1c",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0554a05f96dc9ecd50eee59ceff7c09d54aec73eeecf21b2e06062f3c7622c6a",
  "source_text_sha256": "0554a05f96dc9ecd50eee59ceff7c09d54aec73eeecf21b2e06062f3c7622c6a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

## 疑似コード / UTF-8 557 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00aecd28 to 00bedab3 has its CatchHandler @ 00aeadc8 */
  if (DAT_010a08c8 == 0) {
    DAT_010a08c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",param_3);
  }
  return DAT_010a08c8;
}

~~~
