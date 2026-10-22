# 00aeceec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeceec.md)

## 関数情報

~~~json
{
  "address": "00aeceec",
  "name": "firebase::util::set::CacheMethodIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f4aeaf7823872125c4251c1cef1088693d23ece308381354091285173f27865",
  "source_text_sha256": "6f4aeaf7823872125c4251c1cef1088693d23ece308381354091285173f27865"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~
## 疑似コード 1/1 / UTF-8 455 bytes

~~~c

/* firebase::util::set::CacheMethodIds(_JNIEnv*, _jobject*) */

void firebase::util::set::CacheMethodIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a08c8 == (_jclass *)0x0) {
    DAT_010a08c8 = (_jclass *)FindClassGlobal(param_1,param_2,0,"java/util/Set",0);
  }
  LookupMethodIds(param_1,DAT_010a08c8,(MethodNameSignature *)&PTR_s_iterator_00c10498,1,
                  (_jmethodID **)&DAT_010a08d8,"java/util/Set");
  return;
}

~~~
