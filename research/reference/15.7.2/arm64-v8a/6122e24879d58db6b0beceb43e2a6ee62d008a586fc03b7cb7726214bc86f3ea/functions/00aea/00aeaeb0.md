# 00aeaeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeaeb0.md)

## 関数情報

~~~json
{
  "address": "00aeaeb0",
  "name": "firebase::util::hash_map::CacheFieldIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "beac5ca7c57513b833413b421dd954fb8032dcfa7a99a37fc098115e59c0d640",
  "source_text_sha256": "beac5ca7c57513b833413b421dd954fb8032dcfa7a99a37fc098115e59c0d640"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~
## 疑似コード 1/1 / UTF-8 453 bytes

~~~c

/* firebase::util::hash_map::CacheFieldIds(_JNIEnv*, _jobject*) */

void firebase::util::hash_map::CacheFieldIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0750 == (_jclass *)0x0) {
    DAT_010a0750 = (_jclass *)FindClassGlobal(param_1,param_2,0,"java/util/HashMap",0);
  }
  LookupFieldIds(param_1,DAT_010a0750,(FieldDescriptor *)&DAT_002f5cc8,1,(_jfieldID **)&DAT_010a0768
                 ,"java/util/HashMap");
  return;
}

~~~
