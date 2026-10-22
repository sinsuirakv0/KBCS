# 00aebdfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebdfc.md)

## 関数情報

~~~json
{
  "address": "00aebdfc",
  "name": "firebase::util::list::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f5121c75732a332da47bf5f9de8931a8ad23ad015fa0091ee5ef67482e5413e",
  "source_text_sha256": "1f5121c75732a332da47bf5f9de8931a8ad23ad015fa0091ee5ef67482e5413e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/List"
~~~
## 疑似コード 1/1 / UTF-8 401 bytes

~~~c

/* firebase::util::list::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::list::CacheClassFromFiles(void)

{
  if (DAT_010a0820 == 0) {
    DAT_010a0820 = FindClassGlobal();
  }
  return DAT_010a0820;
}

~~~
