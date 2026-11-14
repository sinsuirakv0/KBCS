# 00b4dcbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b4dcbc",
  "name": "_ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f8ef49b0f30b2e6696905add74d8e97ad4de50b283701c7497fb349c03c0f1e",
  "source_text_sha256": "1f8ef49b0f30b2e6696905add74d8e97ad4de50b283701c7497fb349c03c0f1e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

## 疑似コード / UTF-8 595 bytes

~~~c

long _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00b4dcc4 to 00c4f373 has its CatchHandler @ 00b48f48 */
  if (DAT_01126d28 == 0) {
    DAT_01126d28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",param_3);
  }
  return DAT_01126d28;
}

~~~
