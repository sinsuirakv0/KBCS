# 00b4aacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b4aacc.md)

## 関数情報

~~~json
{
  "address": "00b4aacc",
  "name": "firebase::messaging::firebase_messaging::CacheClass",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f0c717c97494af8750118a03708a843a1a5bb3adb0f27b02afac92777b3cd7b",
  "source_text_sha256": "7f0c717c97494af8750118a03708a843a1a5bb3adb0f27b02afac92777b3cd7b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~
## 疑似コード 1/1 / UTF-8 690 bytes

~~~c

/* firebase::messaging::firebase_messaging::CacheClass(_JNIEnv*, _jobject*) */

long firebase::messaging::firebase_messaging::CacheClass(_JNIEnv *param_1,_jobject *param_2)

{
                    /* try { // try from 00b4aae0 to 00c4aaeb has its CatchHandler @ 00b4ac38 */
  if (DAT_010a0ef8 == 0) {
                    /* try { // try from 00b4aaec to 00c4ab0b has its CatchHandler @ 00b4ace8 */
    DAT_010a0ef8 = util::FindClassGlobal
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
  }
                    /* try { // try from 00b4ab0c to 00c4ab27 has its CatchHandler @ 00b4acdc */
  return DAT_010a0ef8;
}

~~~
