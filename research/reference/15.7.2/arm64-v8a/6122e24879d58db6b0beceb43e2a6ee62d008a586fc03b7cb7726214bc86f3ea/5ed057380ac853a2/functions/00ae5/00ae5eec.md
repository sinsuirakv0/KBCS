# 00ae5eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae5eec.md)

## 関数情報

~~~json
{
  "address": "00ae5eec",
  "name": "_ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "391c300875eed64a553cab3611e0c5e1ebdb6785d10e9b908ae73232d332a788",
  "source_text_sha256": "391c300875eed64a553cab3611e0c5e1ebdb6785d10e9b908ae73232d332a788"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri$Builder"
~~~
## 疑似コード 1/1 / UTF-8 627 bytes

~~~c

long _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
                    /* catch() { ... } // from try @ 00ae5c64 with catch @ 00ae5eec */
                    /* catch() { ... } // from try @ 00ae5bfc with catch @ 00ae5ef0 */
  if (DAT_010a0338 == 0) {
    DAT_010a0338 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0338;
}

~~~
