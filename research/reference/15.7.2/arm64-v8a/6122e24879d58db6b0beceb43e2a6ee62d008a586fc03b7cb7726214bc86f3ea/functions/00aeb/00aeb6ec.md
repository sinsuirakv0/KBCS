# 00aeb6ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeb6ec.md)

## 関数情報

~~~json
{
  "address": "00aeb6ec",
  "name": "firebase::util::iterable::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7da3cfece6918e4ed8dce251f602e679324a25cf9fdc7ecc15a5aea6de30a3d0",
  "source_text_sha256": "7da3cfece6918e4ed8dce251f602e679324a25cf9fdc7ecc15a5aea6de30a3d0"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Iterable"
~~~
## 疑似コード 1/1 / UTF-8 434 bytes

~~~c

/* firebase::util::iterable::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*) */

long firebase::util::iterable::CacheClassFromFiles
               (_JNIEnv *param_1,_jobject *param_2,vector *param_3)

{
  if (DAT_010a07d8 == 0) {
    DAT_010a07d8 = FindClassGlobal();
  }
  return DAT_010a07d8;
}

~~~
