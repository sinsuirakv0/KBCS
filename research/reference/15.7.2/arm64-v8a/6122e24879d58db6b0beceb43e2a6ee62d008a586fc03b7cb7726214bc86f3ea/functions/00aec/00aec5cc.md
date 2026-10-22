# 00aec5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aec5cc.md)

## 関数情報

~~~json
{
  "address": "00aec5cc",
  "name": "firebase::util::map::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "754173cff32f4f66a2d6f631f302686fb9fd86d73c14d15027b1dcd540557773",
  "source_text_sha256": "754173cff32f4f66a2d6f631f302686fb9fd86d73c14d15027b1dcd540557773"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Map"
~~~
## 疑似コード 1/1 / UTF-8 341 bytes

~~~c

/* firebase::util::map::CacheClass(_JNIEnv*, _jobject*, firebase::util::ClassRequirement) */

long firebase::util::map::CacheClass(undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0878 == 0) {
    DAT_010a0878 = FindClassGlobal(param_1,param_2,0,"java/util/Map",param_3);
  }
  return DAT_010a0878;
}

~~~
