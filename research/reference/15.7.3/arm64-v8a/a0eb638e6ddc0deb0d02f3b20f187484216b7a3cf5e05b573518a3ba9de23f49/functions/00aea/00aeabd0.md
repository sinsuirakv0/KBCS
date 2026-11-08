# 00aeabd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aeabd0",
  "name": "_ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a0b2012c6cf57fee1433e8920629465f8c026e2659c5ac204290968707e7c18",
  "source_text_sha256": "9a0b2012c6cf57fee1433e8920629465f8c026e2659c5ac204290968707e7c18"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde020](../00bde/00bde020.md)
- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Float"
~~~

## 疑似コード / UTF-8 689 bytes

~~~c

void _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a07e8 == 0) {
    DAT_010a07e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Float",0);
  }
                    /* try { // try from 00aeac14 to 00beadc7 has its CatchHandler @ 00aeaa38 */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a07e8,&DAT_002f5cb0,1,&DAT_010a0808,"java/lang/Float");
  return;
}

~~~
