# 00aed3ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aed3ec.md)

## 関数情報

~~~json
{
  "address": "00aed3ec",
  "name": "firebase::util::string::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa4c6744ec6184d3eff86981a2a93fd10a2518a7d3274c6dc87225ae345b9916",
  "source_text_sha256": "aa4c6744ec6184d3eff86981a2a93fd10a2518a7d3274c6dc87225ae345b9916"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/String"
~~~
## 疑似コード 1/1 / UTF-8 405 bytes

~~~c

/* firebase::util::string::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::string::CacheClassFromFiles(void)

{
  if (DAT_010a0910 == 0) {
    DAT_010a0910 = FindClassGlobal();
  }
  return DAT_010a0910;
}

~~~
