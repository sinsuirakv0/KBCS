# 00aeb1ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aeb1ac.md)

## 関数情報

~~~json
{
  "address": "00aeb1ac",
  "name": "firebase::util::integer_class::CacheMethodIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c723cf57c1ecdc5d3dadc9c215d6b0f333deb6d756d5b45fd78c5d0c0c63a2d",
  "source_text_sha256": "9c723cf57c1ecdc5d3dadc9c215d6b0f333deb6d756d5b45fd78c5d0c0c63a2d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Integer"
~~~
## 疑似コード 1/1 / UTF-8 677 bytes

~~~c

/* firebase::util::integer_class::CacheMethodIds(_JNIEnv*, _jobject*) */

void firebase::util::integer_class::CacheMethodIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0770 == (_jclass *)0x0) {
                    /* try { // try from 00aeb1cc to 00beb207 has its CatchHandler @ 00af1a20 */
    DAT_010a0770 = (_jclass *)FindClassGlobal(param_1,param_2,0,"java/lang/Integer",0);
  }
                    /* try { // try from 00aeb208 to 00beb21b has its CatchHandler @ 00af18c0 */
  LookupMethodIds(param_1,DAT_010a0770,(MethodNameSignature *)&PTR_s_<init>_00c102d0,2,
                  (_jmethodID **)&DAT_010a0780,"java/lang/Integer");
  return;
}

~~~
