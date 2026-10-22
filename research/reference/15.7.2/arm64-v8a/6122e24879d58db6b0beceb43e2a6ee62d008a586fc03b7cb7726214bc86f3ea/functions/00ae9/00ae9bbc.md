# 00ae9bbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae9bbc.md)

## 関数情報

~~~json
{
  "address": "00ae9bbc",
  "name": "firebase::util::date::CacheMethodIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07978679dc252c93525fffdee2d6b9c41ed7d2d09fe1fc22b6e5667774caeecf",
  "source_text_sha256": "07978679dc252c93525fffdee2d6b9c41ed7d2d09fe1fc22b6e5667774caeecf"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Date"
~~~
## 疑似コード 1/1 / UTF-8 555 bytes

~~~c

/* firebase::util::date::CacheMethodIds(_JNIEnv*, _jobject*) */

void firebase::util::date::CacheMethodIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0650 == (_jclass *)0x0) {
    DAT_010a0650 = (_jclass *)FindClassGlobal(param_1,param_2,0,"java/util/Date",0);
  }
                    /* try { // try from 00ae9c20 to 00be9c5f has its CatchHandler @ 00ae9c98 */
  LookupMethodIds(param_1,DAT_010a0650,(MethodNameSignature *)&PTR_s_<init>_00c10120,3,
                  (_jmethodID **)&DAT_010a0660,"java/util/Date");
  return;
}

~~~
