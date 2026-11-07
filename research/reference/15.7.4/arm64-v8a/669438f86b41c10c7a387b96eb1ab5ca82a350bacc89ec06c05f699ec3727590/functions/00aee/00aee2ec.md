# 00aee2ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00aee1e0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00aee2ec",
  "name": "_ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "203b37b34227200907313abcce279cd0f255059a72c1e78813fd45544f0f32e0",
  "source_text_sha256": "203b37b34227200907313abcce279cd0f255059a72c1e78813fd45544f0f32e0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Object"
~~~

## 疑似コード / UTF-8 588 bytes

~~~c

void _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0a88 == 0) {
    DAT_010a0a88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Object",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0a88,&DAT_002f5e18,1,&DAT_010a0aa0,"java/lang/Object");
  return;
}

~~~
