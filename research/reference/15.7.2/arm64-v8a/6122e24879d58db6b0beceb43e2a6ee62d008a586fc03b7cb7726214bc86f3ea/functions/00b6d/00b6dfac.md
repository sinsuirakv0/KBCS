# 00b6dfac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b6dfac",
  "name": "_ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25614b5a77c1835b443f0a8d391ec2f965933507ead2a3698fa1e918a2fdc74b",
  "source_text_sha256": "25614b5a77c1835b443f0a8d391ec2f965933507ead2a3698fa1e918a2fdc74b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

## 疑似コード / UTF-8 695 bytes

~~~c

void _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a19f8 == 0) {
    DAT_010a19f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a19f8,&PTR_s_getLastSignInTimestamp_00c12960,2,&DAT_010a1a08,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~
