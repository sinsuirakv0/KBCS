# 00ae6cfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

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
