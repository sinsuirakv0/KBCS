# 00ae8fbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae8ef4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8ef4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/alignment_unresolved-0002.md#compare-34c98597aa57630cde69083508cadbc8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae8fbc",
  "name": "_ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afd278ceab4fe7bea908ff490e1acf86c120fd74b87594e6a7752c6bf656682d",
  "source_text_sha256": "afd278ceab4fe7bea908ff490e1acf86c120fd74b87594e6a7752c6bf656682d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/content/ContentResolver"
~~~

## 疑似コード / UTF-8 1014 bytes

~~~c

long _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* catch() { ... } // from try @ 00ae7084 with catch @ 00ae8fd0 */
  if (DAT_010a0680 == 0) {
                    /* catch() { ... } // from try @ 00ae8530 with catch @ 00ae8fd8 */
                    /* catch() { ... } // from try @ 00ae70b8 with catch @ 00ae8fdc */
                    /* catch() { ... } // from try @ 00ae7158 with catch @ 00ae8fe4 */
    DAT_010a0680 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/content/ContentResolver",param_3);
  }
                    /* catch() { ... } // from try @ 00ae70c8 with catch @ 00ae8ff0 */
                    /* catch() { ... } // from try @ 00ae7198 with catch @ 00ae8ff8 */
  return DAT_010a0680;
}

~~~
