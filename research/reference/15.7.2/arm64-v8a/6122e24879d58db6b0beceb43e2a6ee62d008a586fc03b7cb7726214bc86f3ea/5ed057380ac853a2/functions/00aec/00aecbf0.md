# 00aecbf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecbf0.md)

## 関数情報

~~~json
{
  "address": "00aecbf0",
  "name": "_ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a8d6c18995fbc6850ffa1fecead8c587fd0217b2ef9e24301ba43a054a19f5f",
  "source_text_sha256": "2a8d6c18995fbc6850ffa1fecead8c587fd0217b2ef9e24301ba43a054a19f5f"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~
## 疑似コード 1/1 / UTF-8 635 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08a8 == 0) {
    DAT_010a08a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"android/os/ParcelFileDescriptor",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a08a8,&DAT_002f5d88,1,&DAT_010a08c0,"android/os/ParcelFileDescriptor");
  return;
}

~~~
