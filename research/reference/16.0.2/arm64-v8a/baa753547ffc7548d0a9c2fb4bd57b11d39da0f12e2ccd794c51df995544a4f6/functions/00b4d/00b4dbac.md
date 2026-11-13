# 00b4dbac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b4dbac",
  "name": "_ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "463fcd7d434be28a9f46068f2dda534c979ddb3e4330e8b79cef38d3b7a7eea6",
  "source_text_sha256": "463fcd7d434be28a9f46068f2dda534c979ddb3e4330e8b79cef38d3b7a7eea6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Throwable"
~~~

## 疑似コード / UTF-8 424 bytes

~~~c

long _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125df0 == 0) {
    DAT_01125df0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
  return DAT_01125df0;
}

~~~
