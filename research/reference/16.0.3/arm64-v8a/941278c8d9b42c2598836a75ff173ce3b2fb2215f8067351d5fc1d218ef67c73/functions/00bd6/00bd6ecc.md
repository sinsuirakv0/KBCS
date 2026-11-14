# 00bd6ecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bd6ecc",
  "name": "_ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d82ba483528237c5527fb4c255dcb1a28c5f1bdc36ff36a1aad2e57a7cacbb52",
  "source_text_sha256": "d82ba483528237c5527fb4c255dcb1a28c5f1bdc36ff36a1aad2e57a7cacbb52"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GoogleAuthProvider"
~~~

## 疑似コード / UTF-8 661 bytes

~~~c

void _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127b88 == 0) {
    DAT_01127b88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GoogleAuthProvider",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127b88,&DAT_00310050,1,&DAT_01127ba0,
             "com/google/firebase/auth/GoogleAuthProvider");
  return;
}

~~~
