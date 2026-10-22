# 00aebe7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebe7c.md)

## 関数情報

~~~json
{
  "address": "00aebe7c",
  "name": "firebase::util::list::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63fd5d68f7bc37d852f30135de8049cb650ad3f991f0dd350e8a9486bc8da012",
  "source_text_sha256": "63fd5d68f7bc37d852f30135de8049cb650ad3f991f0dd350e8a9486bc8da012"
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
## 疑似コード 1/1 / UTF-8 442 bytes

~~~c

/* firebase::util::list::CacheClass(_JNIEnv*, _jobject*, firebase::util::ClassRequirement) */

long firebase::util::list::CacheClass(undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0820 == 0) {
                    /* try { // try from 00aebe9c to 00bebeaf has its CatchHandler @ 00af1bd4 */
    DAT_010a0820 = FindClassGlobal(param_1,param_2,0,"java/util/List",param_3);
  }
  return DAT_010a0820;
}

~~~
