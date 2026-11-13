# 00b4afcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b4afcc",
  "name": "_ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d858d16aa5a9850159f2ac06a5824871f5d0c6c8ee901b99baa266402ea5aff",
  "source_text_sha256": "1d858d16aa5a9850159f2ac06a5824871f5d0c6c8ee901b99baa266402ea5aff"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~

## 疑似コード / UTF-8 421 bytes

~~~c

long _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01125c10 == 0) {
    DAT_01125c10 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/HashMap",0);
  }
  return DAT_01125c10;
}

~~~
