# 00ae6cfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae6c34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0059.md#compare-0f5cd94db18507fa81a8f5da13b7ddd8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae6cfc",
  "name": "_ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ffb5b954a2dd3d1aeb86665cf8b0437af8db8da463eda00d7ba58ad13554818",
  "source_text_sha256": "7ffb5b954a2dd3d1aeb86665cf8b0437af8db8da463eda00d7ba58ad13554818"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)
- [00bde060](../00bde/00bde060.md)

## 関連文字列（未確認候補）

~~~text
"%PG%dalvik/system/DexClassLoader"
~~~

## 疑似コード / UTF-8 945 bytes

~~~c

void _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00ae6d0c to 00be6d13 has its CatchHandler @ 00ae878c */
                    /* try { // try from 00ae6d14 to 00be6d27 has its CatchHandler @ 00ae89d4 */
  if (DAT_010a0480 == 0) {
    DAT_010a0480 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"dalvik/system/DexClassLoader",0);
  }
                    /* try { // try from 00ae6d40 to 00be6d47 has its CatchHandler @ 00ae89a0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0480,&PTR_s_<init>_00c0fdc8,2,&DAT_010a0490,
             "dalvik/system/DexClassLoader");
  return;
}

~~~
