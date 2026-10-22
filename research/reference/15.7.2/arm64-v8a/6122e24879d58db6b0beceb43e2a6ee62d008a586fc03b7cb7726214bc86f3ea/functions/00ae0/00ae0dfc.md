# 00ae0dfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae0dfc.md)

## 関数情報

~~~json
{
  "address": "00ae0dfc",
  "name": "firebase::analytics::analytics_consent_status::CacheFieldIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58eba5ecc597c5b33e203b9d34d2740b3f35f169c4ca01eb04e95670152d73dd",
  "source_text_sha256": "58eba5ecc597c5b33e203b9d34d2740b3f35f169c4ca01eb04e95670152d73dd"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~
## 疑似コード 1/1 / UTF-8 731 bytes

~~~c

/* firebase::analytics::analytics_consent_status::CacheFieldIds(_JNIEnv*, _jobject*) */

void firebase::analytics::analytics_consent_status::CacheFieldIds
               (_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a0018 == (_jclass *)0x0) {
    DAT_010a0018 = (_jclass *)
                   util::FindClassGlobal
                             (param_1,param_2,0,
                              "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus",0);
  }
  util::LookupFieldIds
            (param_1,DAT_010a0018,(FieldDescriptor *)&PTR_s_GRANTED_00c0fb20,2,
             (_jfieldID **)&DAT_010a0030,
             "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus");
  return;
}

~~~
