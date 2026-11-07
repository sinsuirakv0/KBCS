# 00aebad4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aebbe0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aebad4",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ac9a91b6ee60a445597b5493d385438b76184d6b4500ab2ad25fe2c60deeb6f",
  "source_text_sha256": "0ac9a91b6ee60a445597b5493d385438b76184d6b4500ab2ad25fe2c60deeb6f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

## 疑似コード / UTF-8 470 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a07f8 == 0) {
    DAT_010a07f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",param_3);
  }
  return DAT_010a07f8;
}

~~~
