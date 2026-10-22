# 00aecd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecd1c.md)

## 関数情報

~~~json
{
  "address": "00aecd1c",
  "name": "firebase::util::set::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f25df8e2a6f72b82d5f08f465a2718290445d1ed521cc8ab58a3488d60d1436",
  "source_text_sha256": "3f25df8e2a6f72b82d5f08f465a2718290445d1ed521cc8ab58a3488d60d1436"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~
## 疑似コード 1/1 / UTF-8 439 bytes

~~~c

/* firebase::util::set::CacheClass(_JNIEnv*, _jobject*, firebase::util::ClassRequirement) */

long firebase::util::set::CacheClass(undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00aecd28 to 00bedab3 has its CatchHandler @ 00aeadc8 */
  if (DAT_010a08c8 == 0) {
    DAT_010a08c8 = FindClassGlobal(param_1,param_2,0,"java/util/Set",param_3);
  }
  return DAT_010a08c8;
}

~~~
