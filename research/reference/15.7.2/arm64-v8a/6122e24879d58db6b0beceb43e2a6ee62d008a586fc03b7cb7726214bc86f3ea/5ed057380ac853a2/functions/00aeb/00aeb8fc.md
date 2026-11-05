# 00aeb8fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeb8fc.md)

## 関数情報

~~~json
{
  "address": "00aeb8fc",
  "name": "_ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24a34cb62d7390b0b904c3e7ce2c4255ca15e14ea200d03aa0acf5c0a96b13f8",
  "source_text_sha256": "24a34cb62d7390b0b904c3e7ce2c4255ca15e14ea200d03aa0acf5c0a96b13f8"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Iterable"
~~~
## 疑似コード 1/1 / UTF-8 807 bytes

~~~c

void _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aeb914 to 00beb92b has its CatchHandler @ 00af18e0 */
  if (DAT_010a07d8 == 0) {
                    /* try { // try from 00aeb92c to 00beb93f has its CatchHandler @ 00af18c4 */
    DAT_010a07d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Iterable",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a07d8,&PTR_s_iterator_00c10378,1,&DAT_010a07e8,"java/lang/Iterable");
  return;
}

~~~
