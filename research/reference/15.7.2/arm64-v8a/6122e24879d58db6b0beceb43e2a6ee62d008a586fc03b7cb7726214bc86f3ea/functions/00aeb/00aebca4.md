# 00aebca4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aebca4",
  "name": "_ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5aa4a5bf8c3d7e5983d3be90916d25247fcb31adef954068a37200aa30075d27",
  "source_text_sha256": "5aa4a5bf8c3d7e5983d3be90916d25247fcb31adef954068a37200aa30075d27"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

## 疑似コード / UTF-8 806 bytes

~~~c

void _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aebcb0 to 00bebcc3 has its CatchHandler @ 00af19a4 */
  if (DAT_010a07f8 == 0) {
                    /* try { // try from 00aebcc4 to 00bebcdb has its CatchHandler @ 00af1978 */
    DAT_010a07f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a07f8,&PTR_s_hasNext_00c10390,2,&DAT_010a0808,"java/util/Iterator");
  return;
}

~~~
