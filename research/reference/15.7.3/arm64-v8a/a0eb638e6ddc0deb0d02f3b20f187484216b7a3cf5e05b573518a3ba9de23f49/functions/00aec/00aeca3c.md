# 00aeca3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aeca3c",
  "name": "_ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f489dc50192cf4083a41a4d14ef01ce8e2b52d056f35fbdbf33a94ff7fdec14",
  "source_text_sha256": "9f489dc50192cf4083a41a4d14ef01ce8e2b52d056f35fbdbf33a94ff7fdec14"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

## 疑似コード / UTF-8 692 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00aeca48 to 00beca57 has its CatchHandler @ 00af1aec */
  if (DAT_010a0968 == 0) {
                    /* try { // try from 00aeca58 to 00becacb has its CatchHandler @ 00aeadc8 */
    DAT_010a0968 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",param_3);
  }
  return DAT_010a0968;
}

~~~
