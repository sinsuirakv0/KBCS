# 00bce0bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bce0bc",
  "name": "_ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE",
  "size": 560,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7b2d6a3c31beef0d422c044a1bb93727e8710579ecbf7c8c7af847d78ef94ab",
  "source_text_sha256": "c7b2d6a3c31beef0d422c044a1bb93727e8710579ecbf7c8c7af847d78ef94ab"
}
~~~

## 呼び出し元

- [00c5ece0](../00c5e/00c5ece0.md)

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5c000](../00c5c/00c5c000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

## 疑似コード / UTF-8 4074 bytes

~~~c

bool _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  int iVar1;
  ulong uVar2;
  
  if (DAT_011277e8 == 0) {
                    /* try { // try from 00bce0ec to 00cce0f7 has its CatchHandler @ 00bcfa6c */
                    /* try { // try from 00bce0f8 to 00cce18b has its CatchHandler @ 00bcd634 */
    DAT_011277e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                    (param_1,DAT_011277e8,&PTR_s_getInstance_00c92a28,0x12,&DAT_011277f8,
                     "com/google/firebase/auth/FirebaseAuth");
  if ((uVar2 & 1) != 0) {
    if (DAT_01127890 == 0) {
      DAT_01127890 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                               (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult"
                                ,0);
    }
    uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                      (param_1,DAT_01127890,&PTR_s_getSignInMethods_00c92bd8,1,&DAT_011278a0,
                       "com/google/firebase/auth/SignInMethodQueryResult");
                    /* try { // try from 00bce18c to 00cce197 has its CatchHandler @ 00bcfa0c */
                    /* try { // try from 00bce1b4 to 00cce1cf has its CatchHandler @ 00bcfa1c */
                    /* try { // try from 00bce1d0 to 00cce313 has its CatchHandler @ 00bcd634 */
    if ((((uVar2 & 1) != 0) &&
        (((DAT_011278b0 != 0 ||
          (DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                    (param_1,param_2,param_3,
                                     "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0)
          , DAT_011278b0 != 0)) &&
         (uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                            (param_1,DAT_011278b0,&PTR_s_<init>_00c92bf0,2,&DAT_011278c0,
                             "com/google/firebase/auth/internal/cpp/JniAuthStateListener"),
         (uVar2 & 1) != 0)))) && (DAT_011278b8 == '\0')) {
      iVar1 = (**(code **)(*param_1 + 0x6b8))
                        (param_1,DAT_011278b0,&PTR_s_nativeOnAuthStateChanged_00c92c50,1);
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
      DAT_011278b8 = iVar1 == 0;
      if (((iVar1 == 0) &&
          ((DAT_011278d8 != 0 ||
           (DAT_011278d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                     (param_1,param_2,param_3,
                                      "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0),
           DAT_011278d8 != 0)))) &&
         ((uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                             (param_1,DAT_011278d8,&PTR_s_<init>_00c92c20,2,&DAT_011278e8,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener"),
          (uVar2 & 1) != 0 && (DAT_011278e0 == '\0')))) {
        iVar1 = (**(code **)(*param_1 + 0x6b8))
                          (param_1,DAT_011278d8,&PTR_s_nativeOnIdTokenChanged_00c92c68,1);
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
        DAT_011278e0 = iVar1 == 0;
        return iVar1 == 0;
      }
    }
  }
  return false;
}

~~~
