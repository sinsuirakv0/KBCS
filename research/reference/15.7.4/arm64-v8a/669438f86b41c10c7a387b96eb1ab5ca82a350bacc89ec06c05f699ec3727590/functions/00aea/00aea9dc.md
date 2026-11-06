# 00aea9dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aea9dc",
  "name": "_ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b19bf8cb188980fa85ff5f048db4ced5b24a8411bc19abf6b18c9689fb87eba",
  "source_text_sha256": "7b19bf8cb188980fa85ff5f048db4ced5b24a8411bc19abf6b18c9689fb87eba"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Float"
~~~

## 疑似コード / UTF-8 423 bytes

~~~c

long _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0828 == 0) {
    DAT_010a0828 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Float",0);
  }
  return DAT_010a0828;
}

~~~
