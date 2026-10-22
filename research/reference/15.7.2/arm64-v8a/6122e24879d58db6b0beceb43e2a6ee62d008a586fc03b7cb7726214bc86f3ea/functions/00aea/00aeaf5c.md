# 00aeaf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeaf5c.md)

## 関数情報

~~~json
{
  "address": "00aeaf5c",
  "name": "firebase::util::integer_class::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "320c0e7a92ada85efd0e98305fa0372a60c8c801f3fce4492bebbdd191491389",
  "source_text_sha256": "320c0e7a92ada85efd0e98305fa0372a60c8c801f3fce4492bebbdd191491389"
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
## 疑似コード 1/1 / UTF-8 419 bytes

~~~c

/* firebase::util::integer_class::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::util::integer_class::CacheClassFromFiles(void)

{
  if (DAT_010a0770 == 0) {
    DAT_010a0770 = FindClassGlobal();
  }
  return DAT_010a0770;
}

~~~
