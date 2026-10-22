# 00b5cebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b5cebc.md)

## 関数情報

~~~json
{
  "address": "00b5cebc",
  "name": "firebase::auth::signinmethodquery::CacheFieldIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f5a22df87c7fa4c3bb83b472e29ce65c000ab17eeedf353723e67805ca964d4",
  "source_text_sha256": "2f5a22df87c7fa4c3bb83b472e29ce65c000ab17eeedf353723e67805ca964d4"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
~~~
## 疑似コード 1/1 / UTF-8 638 bytes

~~~c

/* firebase::auth::signinmethodquery::CacheFieldIds(_JNIEnv*, _jobject*) */

void firebase::auth::signinmethodquery::CacheFieldIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a13c8 == (_jclass *)0x0) {
    DAT_010a13c8 = (_jclass *)
                   util::FindClassGlobal
                             (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult",0
                             );
  }
  util::LookupFieldIds
            (param_1,DAT_010a13c8,(FieldDescriptor *)&DAT_002f9220,1,(_jfieldID **)&DAT_010a13e0,
             "com/google/firebase/auth/SignInMethodQueryResult");
  return;
}

~~~
