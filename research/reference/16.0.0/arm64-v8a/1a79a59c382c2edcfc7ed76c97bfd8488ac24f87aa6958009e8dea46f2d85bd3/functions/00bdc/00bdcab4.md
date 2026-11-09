# 00bdcab4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bdcab4",
  "name": "_ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a24bc387d213ac2c9d0435bad669f4544fe0ded83f5ad061c6e1ef928a409fce",
  "source_text_sha256": "a24bc387d213ac2c9d0435bad669f4544fe0ded83f5ad061c6e1ef928a409fce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

## 疑似コード / UTF-8 738 bytes

~~~c

long _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00bdcab4 to 00cdcabf has its CatchHandler @ 00bde9d0 */
                    /* try { // try from 00bdcac0 to 00cdcad7 has its CatchHandler @ 00bde9cc */
  if (DAT_01126900 == 0) {
                    /* try { // try from 00bdcad8 to 00cdd4f3 has its CatchHandler @ 00bd6d50 */
    DAT_01126900 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  return DAT_01126900;
}

~~~
