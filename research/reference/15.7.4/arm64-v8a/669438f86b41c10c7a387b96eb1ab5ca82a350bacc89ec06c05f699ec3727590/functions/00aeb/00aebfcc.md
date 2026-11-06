# 00aebfcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aebfcc",
  "name": "_ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d3de7de21217c2807f9b01a365e70d5782805fc99550bcfff5a19e3b1beefb9",
  "source_text_sha256": "7d3de7de21217c2807f9b01a365e70d5782805fc99550bcfff5a19e3b1beefb9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/List"
~~~

## 疑似コード / UTF-8 398 bytes

~~~c

long _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0920 == 0) {
    DAT_010a0920 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/List",0);
  }
  return DAT_010a0920;
}

~~~
