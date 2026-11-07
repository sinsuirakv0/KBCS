# 00aec5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aec6d8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec6d8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aec5cc",
  "name": "_ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b1c14d1b0eb8f3f74778d94c46d9089c7aaf3cae1f5896e859644d8b1d3cf5c",
  "source_text_sha256": "1b1c14d1b0eb8f3f74778d94c46d9089c7aaf3cae1f5896e859644d8b1d3cf5c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Map"
~~~

## 疑似コード / UTF-8 460 bytes

~~~c

long _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0878 == 0) {
    DAT_010a0878 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Map",param_3);
  }
  return DAT_010a0878;
}

~~~
