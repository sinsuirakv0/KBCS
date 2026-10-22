# 00aedfa8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aedfa8.md)

## 関数情報

~~~json
{
  "address": "00aedfa8",
  "name": "firebase::util::object::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff9966cc1789e201515ec5c1d3a8153d47c403ccd7b71c97fe2e94e061e5a536",
  "source_text_sha256": "ff9966cc1789e201515ec5c1d3a8153d47c403ccd7b71c97fe2e94e061e5a536"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Object"
~~~
## 疑似コード 1/1 / UTF-8 288 bytes

~~~c

/* firebase::util::object::CacheClass(_JNIEnv*, _jobject*) */

long firebase::util::object::CacheClass(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0988 == 0) {
    DAT_010a0988 = FindClassGlobal(param_1,param_2,0,"java/lang/Object",0);
  }
  return DAT_010a0988;
}

~~~
