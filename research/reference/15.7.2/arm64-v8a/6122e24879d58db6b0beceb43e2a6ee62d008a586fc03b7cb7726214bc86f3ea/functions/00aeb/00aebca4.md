# 00aebca4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aebca4.md)

## 関数情報

~~~json
{
  "address": "00aebca4",
  "name": "firebase::util::iterator::CacheMethodIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2f1d4c261ccba22238046eeb3028f6d8fd783921a049558772bf51b84a695ad",
  "source_text_sha256": "d2f1d4c261ccba22238046eeb3028f6d8fd783921a049558772bf51b84a695ad"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~
## 疑似コード 1/1 / UTF-8 670 bytes

~~~c

/* firebase::util::iterator::CacheMethodIds(_JNIEnv*, _jobject*) */

void firebase::util::iterator::CacheMethodIds(_JNIEnv *param_1,_jobject *param_2)

{
                    /* try { // try from 00aebcb0 to 00bebcc3 has its CatchHandler @ 00af19a4 */
  if (DAT_010a07f8 == (_jclass *)0x0) {
                    /* try { // try from 00aebcc4 to 00bebcdb has its CatchHandler @ 00af1978 */
    DAT_010a07f8 = (_jclass *)FindClassGlobal(param_1,param_2,0,"java/util/Iterator",0);
  }
  LookupMethodIds(param_1,DAT_010a07f8,(MethodNameSignature *)&PTR_s_hasNext_00c10390,2,
                  (_jmethodID **)&DAT_010a0808,"java/util/Iterator");
  return;
}

~~~
