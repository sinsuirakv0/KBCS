# 00aebe3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebe3c.md)

## 関数情報

~~~json
{
  "address": "00aebe3c",
  "name": "firebase::util::list::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d8f9cdde7ff09600550b0e76faaa10bba21d0b73ccda56987b21c973808b161",
  "source_text_sha256": "4d8f9cdde7ff09600550b0e76faaa10bba21d0b73ccda56987b21c973808b161"
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
## 疑似コード 1/1 / UTF-8 409 bytes

~~~c

/* firebase::util::list::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*) */

long firebase::util::list::CacheClassFromFiles(_JNIEnv *param_1,_jobject *param_2,vector *param_3)

{
  if (DAT_010a0820 == 0) {
    DAT_010a0820 = FindClassGlobal();
  }
  return DAT_010a0820;
}

~~~
