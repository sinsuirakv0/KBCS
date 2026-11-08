# 00aeb1ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aeb1ac",
  "name": "_ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26a601e3a61544d234144c63e30e6582f863f1c6848a879b0051b3a7555304a6",
  "source_text_sha256": "26a601e3a61544d234144c63e30e6582f863f1c6848a879b0051b3a7555304a6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Integer"
~~~

## 疑似コード / UTF-8 809 bytes

~~~c

void _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0770 == 0) {
                    /* try { // try from 00aeb1cc to 00beb207 has its CatchHandler @ 00af1a20 */
    DAT_010a0770 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Integer",0);
  }
                    /* try { // try from 00aeb208 to 00beb21b has its CatchHandler @ 00af18c0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0770,&PTR_s_<init>_00c102d0,2,&DAT_010a0780,"java/lang/Integer");
  return;
}

~~~
