# 00ae8acc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae8acc.md)

## 関数情報

~~~json
{
  "address": "00ae8acc",
  "name": "_ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69f6d33a6f3731a229dac64a49ec78d55874d2696e2d51e91a00fb1022e6a841",
  "source_text_sha256": "69f6d33a6f3731a229dac64a49ec78d55874d2696e2d51e91a00fb1022e6a841"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Class"
~~~
## 疑似コード 1/1 / UTF-8 628 bytes

~~~c

long _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_010a0598 == 0) {
                    /* catch() { ... } // from try @ 00ae6b74 with catch @ 00ae8ae8 */
    DAT_010a0598 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
                    /* catch() { ... } // from try @ 00ae6b64 with catch @ 00ae8b08 */
  return DAT_010a0598;
}

~~~
