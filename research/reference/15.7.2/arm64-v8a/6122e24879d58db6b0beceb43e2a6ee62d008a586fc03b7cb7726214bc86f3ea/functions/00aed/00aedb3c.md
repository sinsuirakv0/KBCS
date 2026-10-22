# 00aedb3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aedb3c.md)

## 関数情報

~~~json
{
  "address": "00aedb3c",
  "name": "firebase::util::uri::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc0b1ba9e392c84ff6f7403129f676c84b10b9819ea2cdba18e401bab548f44e",
  "source_text_sha256": "cc0b1ba9e392c84ff6f7403129f676c84b10b9819ea2cdba18e401bab548f44e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~
## 疑似コード 1/1 / UTF-8 399 bytes

~~~c

/* firebase::util::uri::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::uri::CacheClassFromFiles(void)

{
  if (DAT_010a0960 == 0) {
    DAT_010a0960 = FindClassGlobal();
  }
  return DAT_010a0960;
}

~~~
