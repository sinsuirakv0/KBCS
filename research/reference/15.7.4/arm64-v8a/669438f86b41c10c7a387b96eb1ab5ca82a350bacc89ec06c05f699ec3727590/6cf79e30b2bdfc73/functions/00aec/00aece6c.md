# 00aece6c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aece6c.md)

## 関数情報

~~~json
{
  "address": "00aece6c",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d2a7a8d6d1a5e6137129af2d4a848570abd4aa4a7cdffd164217c6b00df862d",
  "source_text_sha256": "2d2a7a8d6d1a5e6137129af2d4a848570abd4aa4a7cdffd164217c6b00df862d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~
## 疑似コード 1/1 / UTF-8 396 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a09c8 == 0) {
    DAT_010a09c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  return DAT_010a09c8;
}

~~~
