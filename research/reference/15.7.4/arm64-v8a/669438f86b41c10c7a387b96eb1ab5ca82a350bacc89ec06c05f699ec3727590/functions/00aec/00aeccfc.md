# 00aeccfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aecbf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aeccfc",
  "name": "_ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c52a06d8280f22c6c4169319413b116d07db936773fdce0e80ab7f4caab910b3",
  "source_text_sha256": "c52a06d8280f22c6c4169319413b116d07db936773fdce0e80ab7f4caab910b3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~

## 疑似コード / UTF-8 732 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aecd00 to 00becd6b has its CatchHandler @ 00af1a7c */
  if (DAT_010a09a8 == 0) {
    DAT_010a09a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a09a8,&DAT_002f5d88,1,&DAT_010a09c0,"android/os/ParcelFileDescriptor");
  return;
}

~~~
