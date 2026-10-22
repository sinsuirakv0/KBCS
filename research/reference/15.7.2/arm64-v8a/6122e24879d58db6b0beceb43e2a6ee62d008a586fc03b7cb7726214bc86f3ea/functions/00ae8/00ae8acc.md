# 00ae8acc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae8acc.md)

## 関数情報

~~~json
{
  "address": "00ae8acc",
  "name": "firebase::util::class_class::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "76ec7e63f2c1fb64d5f488aff85d9fb0cc9ad08756cba17c96f33e941be3d0a6",
  "source_text_sha256": "76ec7e63f2c1fb64d5f488aff85d9fb0cc9ad08756cba17c96f33e941be3d0a6"
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
## 疑似コード 1/1 / UTF-8 591 bytes

~~~c

/* firebase::util::class_class::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::class_class::CacheClassFromFiles(void)

{
  if (DAT_010a0598 == 0) {
                    /* catch() { ... } // from try @ 00ae6b74 with catch @ 00ae8ae8 */
    DAT_010a0598 = FindClassGlobal();
  }
                    /* catch() { ... } // from try @ 00ae6b64 with catch @ 00ae8b08 */
  return DAT_010a0598;
}

~~~
