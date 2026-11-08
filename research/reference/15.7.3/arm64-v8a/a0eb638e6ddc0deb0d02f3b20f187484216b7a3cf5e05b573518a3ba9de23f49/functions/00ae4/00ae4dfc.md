# 00ae4dfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ae4dfc",
  "name": "_ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f32f82c073109e2090e54a679c3c93a837c0b6b8a88a2d77d87586b7b6eb406d",
  "source_text_sha256": "f32f82c073109e2090e54a679c3c93a837c0b6b8a88a2d77d87586b7b6eb406d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde020](../00bde/00bde020.md)
- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/ClassLoader"
~~~

## 疑似コード / UTF-8 605 bytes

~~~c

void _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0328 == 0) {
    DAT_010a0328 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/ClassLoader",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0328,&DAT_002f5a58,1,&DAT_010a0348,"java/lang/ClassLoader");
  return;
}

~~~
