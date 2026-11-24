# 00bddf1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdde80`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0085.md#compare-b08f3ad841ff2b04db7243c32c330925)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0098.md#compare-81b8c594ec11562e0c521e3d151b3e67)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
