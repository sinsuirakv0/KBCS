# 00aecbf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aecbf0.md)

## 関数情報

~~~json
{
  "address": "00aecbf0",
  "name": "firebase::util::parcel_file_descriptor::CacheFieldIds",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33aa0d46c2eeb5c09a56d0631eec9caedd564b75881212ee69f081db0465ec9b",
  "source_text_sha256": "33aa0d46c2eeb5c09a56d0631eec9caedd564b75881212ee69f081db0465ec9b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"android/os/ParcelFileDescriptor"
~~~
## 疑似コード 1/1 / UTF-8 515 bytes

~~~c

/* firebase::util::parcel_file_descriptor::CacheFieldIds(_JNIEnv*, _jobject*) */

void firebase::util::parcel_file_descriptor::CacheFieldIds(_JNIEnv *param_1,_jobject *param_2)

{
  if (DAT_010a08a8 == (_jclass *)0x0) {
    DAT_010a08a8 = (_jclass *)FindClassGlobal(param_1,param_2,0,"android/os/ParcelFileDescriptor",0)
    ;
  }
  LookupFieldIds(param_1,DAT_010a08a8,(FieldDescriptor *)&DAT_002f5d88,1,(_jfieldID **)&DAT_010a08c0
                 ,"android/os/ParcelFileDescriptor");
  return;
}

~~~
