# 00aedb9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aedb9c.md)

## 関数情報

~~~json
{
  "address": "00aedb9c",
  "name": "_ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3178e408f4ef7ecaf0917f74ceaf212229f0adc298e9d0223f156785a3ad2533",
  "source_text_sha256": "3178e408f4ef7ecaf0917f74ceaf212229f0adc298e9d0223f156785a3ad2533"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~
## 疑似コード 1/1 / UTF-8 597 bytes

~~~c

void _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a30 == 0) {
    DAT_010a0a30 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0a30,&DAT_002f5de8,1,&DAT_010a0a58,"java/lang/Throwable");
  return;
}

~~~
