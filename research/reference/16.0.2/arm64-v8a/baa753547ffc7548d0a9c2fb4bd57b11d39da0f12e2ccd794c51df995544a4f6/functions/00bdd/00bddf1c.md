# 00bddf1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bddf1c",
  "name": "_ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a70ec06841dbfc28923713cede09460112dd683678d829c96f28d336edfd2f74",
  "source_text_sha256": "a70ec06841dbfc28923713cede09460112dd683678d829c96f28d336edfd2f74"
}
~~~

## 呼び出し元

- [00c5dd20](../00c5d/00c5dd20.md)

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
"%PG%com/google/firebase/auth/GetTokenResult"
"%PG%com/google/firebase/auth/UserInfo"
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

## 疑似コード / UTF-8 3374 bytes

~~~c

undefined8
_ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  
  if (DAT_01126e00 == 0) {
    DAT_01126e00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                    (param_1,DAT_01126e00,&PTR_s_getToken_00c926b0,1,&DAT_01126e10,
                     "com/google/firebase/auth/GetTokenResult");
  if ((uVar1 & 1) != 0) {
    if (DAT_01126e20 == 0) {
      DAT_01126e20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                               (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
    }
    uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                      (param_1,DAT_01126e20,&PTR_s_isAnonymous_00c926c8,0xf,&DAT_01126e30,
                       "com/google/firebase/auth/FirebaseUser");
    if ((uVar1 & 1) != 0) {
      if (DAT_01126eb0 == 0) {
        DAT_01126eb0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (param_1,param_2,0,"com/google/firebase/auth/UserInfo",0);
      }
      uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                        (param_1,DAT_01126eb0,&PTR_s_getUid_00c92830,7,&DAT_01126ec0,
                         "com/google/firebase/auth/UserInfo");
      if ((uVar1 & 1) != 0) {
        if (DAT_01126f00 == 0) {
          DAT_01126f00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                   (param_1,param_2,0,
                                    "com/google/firebase/auth/FirebaseUserMetadata",0);
        }
        uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                          (param_1,DAT_01126f00,&PTR_s_getLastSignInTimestamp_00c928d8,2,
                           &DAT_01126f10,"com/google/firebase/auth/FirebaseUserMetadata");
        if ((uVar1 & 1) != 0) {
          if (DAT_01126f28 == 0) {
            DAT_01126f28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                     (param_1,param_2,0,
                                      "com/google/firebase/auth/UserProfileChangeRequest$Builder",0)
            ;
          }
          uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                            (param_1,DAT_01126f28,&PTR_s_<init>_00c92908,4,&DAT_01126f38,
                             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
          return uVar2;
        }
      }
    }
  }
  return 0;
}

~~~
