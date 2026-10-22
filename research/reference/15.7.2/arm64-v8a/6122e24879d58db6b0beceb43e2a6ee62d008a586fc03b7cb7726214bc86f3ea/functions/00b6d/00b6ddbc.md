# 00b6ddbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b6ddbc.md)

## 関数情報

~~~json
{
  "address": "00b6ddbc",
  "name": "firebase::auth::metadata::CacheClassFromFiles",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09c1f660692545fe991ce6e07668db4f96e3228f40aad820923df85f29d02ea7",
  "source_text_sha256": "09c1f660692545fe991ce6e07668db4f96e3228f40aad820923df85f29d02ea7"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~
## 疑似コード 1/1 / UTF-8 513 bytes

~~~c

/* firebase::auth::metadata::CacheClassFromFiles(_JNIEnv*, _jobject*,
   std::__ndk1::vector<firebase::internal::EmbeddedFile,
   std::__ndk1::allocator<firebase::internal::EmbeddedFile> > const*,
   firebase::util::ClassRequirement) */

long firebase::auth::metadata::CacheClassFromFiles(void)

{
                    /* try { // try from 00b6ddc4 to 00c6de43 has its CatchHandler @ 00b6dd58 */
  if (DAT_010a19f8 == 0) {
    DAT_010a19f8 = util::FindClassGlobal();
  }
  return DAT_010a19f8;
}

~~~
