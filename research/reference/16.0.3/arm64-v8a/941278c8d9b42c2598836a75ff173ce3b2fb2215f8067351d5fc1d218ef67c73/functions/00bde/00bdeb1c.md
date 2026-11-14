# 00bdeb1c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdeb1c",
  "name": "_ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7fdb1802297d41cb868f53b9cd30983154231f43abf96c5b1a7b2b461a8cb1e",
  "source_text_sha256": "c7fdb1802297d41cb868f53b9cd30983154231f43abf96c5b1a7b2b461a8cb1e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

## 疑似コード / UTF-8 662 bytes

~~~c

void _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127ec0 == 0) {
    DAT_01127ec0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127ec0,&DAT_00310298,1,&DAT_01127ee0,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~
