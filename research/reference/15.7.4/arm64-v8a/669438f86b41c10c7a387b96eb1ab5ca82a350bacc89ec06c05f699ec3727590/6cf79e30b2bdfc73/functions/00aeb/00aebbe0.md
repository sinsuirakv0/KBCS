# 00aebbe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aebbe0.md)

## 関数情報

~~~json
{
  "address": "00aebbe0",
  "name": "_ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af22e2f4222f704d323b77d35434a5616f55572928b8d775ef4dc1a5762edf52",
  "source_text_sha256": "af22e2f4222f704d323b77d35434a5616f55572928b8d775ef4dc1a5762edf52"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~
## 疑似コード 1/1 / UTF-8 567 bytes

~~~c

long _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a08f8 == 0) {
                    /* try { // try from 00aebc08 to 00bebc1f has its CatchHandler @ 00af1ad0 */
    DAT_010a08f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",param_3);
  }
  return DAT_010a08f8;
}

~~~
