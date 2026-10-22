# 00aebec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebec0.md)

## 関数情報

~~~json
{
  "address": "00aebec0",
  "name": "firebase::util::list::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a7a442e8996c34257d2034e14e437aa262f7950a9cee08f82bc5c7bdb0eed41a",
  "source_text_sha256": "a7a442e8996c34257d2034e14e437aa262f7950a9cee08f82bc5c7bdb0eed41a"
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
## 疑似コード 1/1 / UTF-8 282 bytes

~~~c

/* firebase::util::list::CacheClass(_JNIEnv*, _jobject*) */

long firebase::util::list::CacheClass(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0820 == 0) {
    DAT_010a0820 = FindClassGlobal(param_1,param_2,0,"java/util/List",0);
  }
  return DAT_010a0820;
}

~~~
