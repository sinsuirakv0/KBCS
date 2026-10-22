# 00b4afec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b4afec.md)

## 関数情報

~~~json
{
  "address": "00b4afec",
  "name": "firebase::messaging::registration_intent_service::CacheFieldIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "450257f19bdce174cecab4cf0835075efe9cce2dd370609eefb9048867f8a4c9",
  "source_text_sha256": "450257f19bdce174cecab4cf0835075efe9cce2dd370609eefb9048867f8a4c9"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~
## 疑似コード 1/1 / UTF-8 1002 bytes

~~~c

/* firebase::messaging::registration_intent_service::CacheFieldIds(_JNIEnv*, _jobject*) */

void firebase::messaging::registration_intent_service::CacheFieldIds
               (_JNIEnv *param_1,_jobject *param_2)

{
                    /* try { // try from 00b4b000 to 00c4b00b has its CatchHandler @ 00b4b140 */
  if (DAT_010a0f58 == (_jclass *)0x0) {
    DAT_010a0f58 = (_jclass *)
                   util::FindClassGlobal
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
                    /* try { // try from 00b4b030 to 00c4b03b has its CatchHandler @ 00b4b13c */
                    /* try { // try from 00b4b054 to 00c4b05f has its CatchHandler @ 00b4b138 */
  util::LookupFieldIds
            (param_1,DAT_010a0f58,(FieldDescriptor *)&DAT_002f8900,1,(_jfieldID **)&DAT_010a0f70,
             "com/google/firebase/messaging/cpp/RegistrationIntentService");
  return;
}

~~~
