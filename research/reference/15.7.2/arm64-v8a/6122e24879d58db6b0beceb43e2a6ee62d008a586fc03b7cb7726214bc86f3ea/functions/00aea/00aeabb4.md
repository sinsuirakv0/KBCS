# 00aeabb4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeabb4.md)

## 関数情報

~~~json
{
  "address": "00aeabb4",
  "name": "firebase::util::hash_map::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e739bb092f58f6c70645e26ba34606023f9797feabb7d4c72743b1de9d2d066a",
  "source_text_sha256": "e739bb092f58f6c70645e26ba34606023f9797feabb7d4c72743b1de9d2d066a"
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
## 疑似コード 1/1 / UTF-8 409 bytes

~~~c

/* firebase::util::hash_map::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::hash_map::CacheClassFromFiles(void)

{
  if (DAT_010a0750 == 0) {
    DAT_010a0750 = FindClassGlobal();
  }
  return DAT_010a0750;
}

~~~
