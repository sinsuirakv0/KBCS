# 00ae7cac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae7cac.md)

## 関数情報

~~~json
{
  "address": "00ae7cac",
  "name": "_ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20aedbcdd840631dc89cb6100e882e4a166023c8198884646e429365434d0316",
  "source_text_sha256": "20aedbcdd840631dc89cb6100e882e4a166023c8198884646e429365434d0316"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Boolean"
~~~
## 疑似コード 1/1 / UTF-8 475 bytes

~~~c

long _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a04c0 == 0) {
    DAT_010a04c0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Boolean",param_3);
  }
  return DAT_010a04c0;
}

~~~
