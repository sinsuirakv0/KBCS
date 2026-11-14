# 00bd7bec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bd7bec",
  "name": "_ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afd301ef1ad8d504fe29963f0a6a938afc13aea3bf389a73c45a31b797b2ac1e",
  "source_text_sha256": "afd301ef1ad8d504fe29963f0a6a938afc13aea3bf389a73c45a31b797b2ac1e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%java/util/concurrent/TimeUnit"
~~~

## 疑似コード / UTF-8 645 bytes

~~~c

void _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127c18 == 0) {
    DAT_01127c18 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/concurrent/TimeUnit",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127c18,&PTR_s_MILLISECONDS_00c93318,1,&DAT_01127c30,
             "java/util/concurrent/TimeUnit");
  return;
}

~~~
