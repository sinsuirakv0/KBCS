# 00aeaf9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeaf9c.md)

## 関数情報

~~~json
{
  "address": "00aeaf9c",
  "name": "_ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f97a7fdb5464721e0d58cc6717fef49cdf4b5696451e5185beadacdc91c1ad9",
  "source_text_sha256": "9f97a7fdb5464721e0d58cc6717fef49cdf4b5696451e5185beadacdc91c1ad9"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Integer"
~~~
## 疑似コード 1/1 / UTF-8 433 bytes

~~~c

long _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_010a0770 == 0) {
    DAT_010a0770 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a0770;
}

~~~
