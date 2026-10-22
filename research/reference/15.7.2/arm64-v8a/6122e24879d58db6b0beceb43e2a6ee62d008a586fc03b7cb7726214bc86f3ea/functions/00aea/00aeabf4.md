# 00aeabf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeabf4.md)

## 関数情報

~~~json
{
  "address": "00aeabf4",
  "name": "firebase::util::hash_map::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1acb6e6eec6835a6149f1e3f770e97dd2ad139162e0175b802bed12575fd142b",
  "source_text_sha256": "1acb6e6eec6835a6149f1e3f770e97dd2ad139162e0175b802bed12575fd142b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~
## 疑似コード 1/1 / UTF-8 532 bytes

~~~c

/* firebase::util::hash_map::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*) */

long firebase::util::hash_map::CacheClassFromFiles
               (_JNIEnv *param_1,_jobject *param_2,vector *param_3)

{
  if (DAT_010a0750 == 0) {
                    /* try { // try from 00aeac14 to 00beadc7 has its CatchHandler @ 00aeaa38 */
    DAT_010a0750 = FindClassGlobal();
  }
  return DAT_010a0750;
}

~~~
