# 00aedbbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aedbbc.md)

## 関数情報

~~~json
{
  "address": "00aedbbc",
  "name": "firebase::util::uri::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d462e9b2fd2cb5f563dae2c1409fe4e8319a3b2e1d351efd4d726c19de63512",
  "source_text_sha256": "1d462e9b2fd2cb5f563dae2c1409fe4e8319a3b2e1d351efd4d726c19de63512"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/net/Uri"
~~~
## 疑似コード 1/1 / UTF-8 343 bytes

~~~c

/* firebase::util::uri::CacheClass(_JNIEnv*, _jobject*, firebase::util::ClassRequirement) */

long firebase::util::uri::CacheClass(undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_010a0960 == 0) {
    DAT_010a0960 = FindClassGlobal(param_1,param_2,0,"android/net/Uri",param_3);
  }
  return DAT_010a0960;
}

~~~
