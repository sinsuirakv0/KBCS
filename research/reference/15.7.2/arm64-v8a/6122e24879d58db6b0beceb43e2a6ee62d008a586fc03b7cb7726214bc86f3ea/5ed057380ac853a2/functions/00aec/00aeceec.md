# 00aeceec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeceec.md)

## 関数情報

~~~json
{
  "address": "00aeceec",
  "name": "_ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb607c5c64be3697534b81a67304c303bce48e3268806769de7a442c9b8bc19e",
  "source_text_sha256": "fb607c5c64be3697534b81a67304c303bce48e3268806769de7a442c9b8bc19e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~
## 疑似コード 1/1 / UTF-8 598 bytes

~~~c

void _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a08c8 == 0) {
    DAT_010a08c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a08c8,&PTR_s_iterator_00c10498,1,&DAT_010a08d8,"java/util/Set");
  return;
}

~~~
