# 00ae9bbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00ae9bbc",
  "name": "_ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea541ba29adefea8596a83311ad2c8d4c836e2d488cc5afd7920bc53d7719f41",
  "source_text_sha256": "ea541ba29adefea8596a83311ad2c8d4c836e2d488cc5afd7920bc53d7719f41"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Date"
~~~

## 疑似コード / UTF-8 696 bytes

~~~c

void _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0650 == 0) {
    DAT_010a0650 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Date",0);
  }
                    /* try { // try from 00ae9c20 to 00be9c5f has its CatchHandler @ 00ae9c98 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0650,&PTR_s_<init>_00c10120,3,&DAT_010a0660,"java/util/Date");
  return;
}

~~~
