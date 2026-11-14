# 00bc4cac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc4cac",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE",
  "size": 2660,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8787444b2718117f158fa761564dd978e5fbf7539d9b661ae207a373857b11f2",
  "source_text_sha256": "8787444b2718117f158fa761564dd978e5fbf7539d9b661ae207a373857b11f2"
}
~~~

## 呼び出し元

- [00c5e910](../00c5e/00c5e910.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5bcc0](../00c5b/00c5bcc0.md)
- [00c5bce0](../00c5b/00c5bce0.md)
- [00c5bd20](../00c5b/00c5bd20.md)
- [00c5bf40](../00c5b/00c5bf40.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c070](../00c5c/00c5c070.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c1d0](../00c5c/00c5c1d0.md)
- [00c5c440](../00c5c/00c5c440.md)
- [00c5ce00](../00c5c/00c5ce00.md)
- [00c5cf90](../00c5c/00c5cf90.md)
- [00c5e9d0](../00c5e/00c5e9d0.md)
- [00c5ea10](../00c5e/00c5ea10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/ConfigUpdate"
"%PG%com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration"
"%PG%com/google/firebase/remoteconfig/CustomSignals$Builder"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfig"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder"
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
"%PG%com/google/firebase/remoteconfig/internal/cpp/JniConfigUpdateListener"
"%s API Initialized"
"Firebase RemoteConfig API Initializing"
"Remote Config"
"config_instance_local"
~~~

## 疑似コード / UTF-8 18077 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE
               (undefined8 *param_1,undefined8 param_2)

{
  byte *pbVar1;
  undefined *puVar2;
  uint *puVar3;
  uint *puVar4;
  long lVar5;
  long lVar6;
  bool bVar7;
  undefined *puVar8;
  uint uVar9;
  int iVar10;
  long *plVar11;
  ulong uVar12;
  long lVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 *local_a8;
  undefined8 *local_a0;
  undefined8 *local_98;
  void *local_90;
  undefined8 uStack_88;
  undefined8 local_80;
  uint *local_78;
  undefined *puStack_70;
  long local_68;
  
  lVar6 = tpidr_el0;
  local_68 = *(long *)(lVar6 + 0x28);
  *param_1 = param_2;
                    /* try { // try from 00bc4ce4 to 00cc5237 has its CatchHandler @ 00bc4ce4
                       catch() { ... } // from try @ 00bc4ce4 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5240 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc53f0 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5588 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5710 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc58ac with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5a44 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5c54 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5cd4 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5d54 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5dd4 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5e90 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5f10 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc5f88 with catch @ 00bc4ce4
                       catch() { ... } // from try @ 00bc6000 with catch @ 00bc4ce4 */
  _ZN8firebase26ReferenceCountedFutureImplC2Em(param_1 + 1,7);
  _ZN8firebase15CleanupNotifierC1Ev(param_1 + 0x27);
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1 + 0x34,1);
  puVar8 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  pbVar1 = (byte *)(param_1 + 0x40);
  puVar2 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 +
           4;
  param_1[0x40] = 0;
  param_1[0x3f] = 0;
  param_1[0x42] = 0;
  param_1[0x41] = 0;
  param_1[0x3c] = 0;
  param_1[0x3b] = 0;
  param_1[0x3e] = 0;
  param_1[0x3d] = 0;
  param_1[0x3a] = 0;
  param_1[0x39] = 0;
  local_78 = (uint *)puVar8;
  puStack_70 = puVar2;
  _ZN8firebase5Mutex7AcquireEv(puVar2);
  _ZN8firebase5Mutex7AcquireEv(puVar2);
  *(int *)puVar8 = *(int *)puVar8 + 1;
  _ZN8firebase5Mutex7ReleaseEv(puVar8 + 4);
  _ZN8firebase8LogDebugEPKcz("Firebase RemoteConfig API Initializing");
  _ZN8firebase19CreateApiIdentifierEPKcPv(&local_90,"Remote Config",param_1);
  if ((*pbVar1 & 1) == 0) {
    pbVar1[0] = 0;
    pbVar1[1] = 0;
  }
  else {
    *(undefined1 *)param_1[0x42] = 0;
    param_1[0x41] = 0;
    if ((*(byte *)(param_1 + 0x40) & 1) != 0) {
      _ZdlPv((void *)param_1[0x42]);
      param_1[0x40] = 0;
    }
  }
  param_1[0x42] = local_80;
  param_1[0x41] = uStack_88;
  *(void **)pbVar1 = local_90;
  plVar11 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  puVar4 = local_78;
  puVar3 = local_78 + 1;
  _ZN8firebase5Mutex7AcquireEv(puVar3);
  uVar9 = *puVar4;
  *puVar4 = uVar9 + 1;
  _ZN8firebase5Mutex7ReleaseEv(puVar3);
  if (uVar9 < 2) {
    uVar15 = *(undefined8 *)*param_1;
    uVar12 = _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject(plVar11,uVar15);
    puVar3 = local_78;
    if ((uVar12 & 1) == 0) {
      puVar4 = local_78 + 1;
      _ZN8firebase5Mutex7AcquireEv(puVar4);
      uVar9 = *puVar3;
      if (uVar9 != 0) {
        *puVar3 = uVar9 - 1;
      }
      _ZN8firebase5Mutex7ReleaseEv(puVar4);
      goto LAB_00bc56d4;
    }
    local_a0 = (undefined8 *)0x0;
    local_98 = (undefined8 *)0x0;
    local_a8 = (undefined8 *)0x0;
    local_a8 = (undefined8 *)_Znwm(0x18);
    puVar2 = PTR__ZN22firebase_remote_config32remote_config_resources_filenameE_00c9c9f0;
    uVar14 = *(undefined8 *)PTR__ZN22firebase_remote_config28remote_config_resources_sizeE_00c9c9e8;
    local_a0 = local_a8 + 3;
    local_a8[1] = PTR__ZN22firebase_remote_config28remote_config_resources_dataE_00c9c9e0;
    *local_a8 = puVar2;
    local_a8[2] = uVar14;
    local_98 = local_a0;
    uVar14 = _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE
                       (plVar11,uVar15,&local_a8);
    _ZNSt6__ndk16vectorIN8firebase8internal12EmbeddedFileENS_9allocatorIS3_EEEC2ERKS6_
              (&local_90,uVar14);
    if (local_a8 != (undefined8 *)0x0) {
      local_a0 = local_a8;
      _ZdlPv(local_a8);
    }
    if ((DAT_01127718 == 0) &&
       (DAT_01127718 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,&local_90,
                                  "com/google/firebase/remoteconfig/internal/cpp/JniConfigUpdateListener"
                                  ,0), DAT_01127718 == 0)) {
LAB_00bc5304:
      if (DAT_01127538 != 0) {
        if (DAT_01127540 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127540 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127538);
        DAT_01127538 = 0;
      }
      if (DAT_011275e0 != 0) {
        if (DAT_011275e8 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_011275e8 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_011275e0);
        DAT_011275e0 = 0;
      }
      if (DAT_01127628 != 0) {
        if (DAT_01127630 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127630 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
                    /* try { // try from 00bc53e8 to 00cc53ef has its CatchHandler @ 00bc651c */
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127628);
                    /* try { // try from 00bc53f0 to 00cc557b has its CatchHandler @ 00bc4ce4 */
        DAT_01127628 = 0;
      }
      if (DAT_01127658 != 0) {
        if (DAT_01127660 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127660 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127658);
        DAT_01127658 = 0;
      }
      if (DAT_01127680 != 0) {
        if (DAT_01127688 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127688 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127680);
        DAT_01127680 = 0;
      }
      if (DAT_011276b8 != 0) {
        if (DAT_011276c0 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_011276c0 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_011276b8);
        DAT_011276b8 = 0;
      }
      if (DAT_011276f8 != 0) {
        if (DAT_01127700 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127700 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_011276f8);
        DAT_011276f8 = 0;
      }
      if (DAT_01127738 != 0) {
        if (DAT_01127740 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127740 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
                    /* try { // try from 00bc557c to 00cc5587 has its CatchHandler @ 00bc6518 */
                    /* try { // try from 00bc5588 to 00cc5707 has its CatchHandler @ 00bc4ce4 */
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127738);
        DAT_01127738 = 0;
      }
      if (DAT_01127758 != 0) {
        if (DAT_01127760 != '\0') {
          (**(code **)(*plVar11 + 0x6c0))(plVar11);
          DAT_01127760 = '\0';
        }
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
        (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127758);
        DAT_01127758 = 0;
      }
      _ZN8firebase4util9TerminateEP7_JNIEnv(plVar11);
      puVar4 = local_78;
      puVar3 = local_78 + 1;
      _ZN8firebase5Mutex7AcquireEv(puVar3);
      uVar9 = *puVar4;
      if (uVar9 != 0) {
        *puVar4 = uVar9 - 1;
      }
      _ZN8firebase5Mutex7ReleaseEv(puVar3);
      bVar7 = true;
    }
    else {
      uVar9 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                        (plVar11,DAT_01127718,&PTR_s_<init>_00c92840,1,&DAT_01127728,
                         "com/google/firebase/remoteconfig/internal/cpp/JniConfigUpdateListener");
      if (DAT_01127720 != '\0' || ((uVar9 ^ 0xffffffff) & 1) != 0) {
LAB_00bc52ac:
        if (DAT_01127718 != 0) {
          if (DAT_01127720 != '\0') {
            (**(code **)(*plVar11 + 0x6c0))(plVar11);
            DAT_01127720 = '\0';
          }
          _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
          (**(code **)(*plVar11 + 0xb0))(plVar11,DAT_01127718);
          DAT_01127718 = 0;
        }
        goto LAB_00bc5304;
      }
      iVar10 = (**(code **)(*plVar11 + 0x6b8))
                         (plVar11,DAT_01127718,&PTR_s_nativeOnUpdate_00c92888,2);
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
      DAT_01127720 = iVar10 == 0;
      if (iVar10 != 0) goto LAB_00bc52ac;
      if (DAT_01127538 == 0) {
        DAT_01127538 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfig",0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127538,&PTR_s_getInstance_00c92498,0x12,&DAT_01127548,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfig");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_011275e0 == 0) {
        DAT_011275e0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfigValue",0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_011275e0,&PTR_s_asLong_00c92648,6,&DAT_011275f0,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfigValue");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_01127628 == 0) {
        DAT_01127628 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo",0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127628,&PTR_s_getFetchTimeMillis_00c926d8,3,&DAT_01127638,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_01127658 == 0) {
        DAT_01127658 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings",0)
        ;
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127658,&PTR_s_getFetchTimeoutInSeconds_00c92720,2,
                          &DAT_01127668,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_01127680 == 0) {
        DAT_01127680 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder"
                                  ,0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127680,&PTR_s_<init>_00c92750,4,&DAT_01127690,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings$Builder");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_011276b8 == 0) {
        DAT_011276b8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/CustomSignals$Builder",0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_011276b8,&PTR_s_<init>_00c927b0,5,&DAT_011276c8,
                          "com/google/firebase/remoteconfig/CustomSignals$Builder");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_011276f8 == 0) {
        DAT_011276f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
                                  ,0);
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_011276f8,&PTR_s_getThrottleEndTimeMillis_00c92828,1,
                          &DAT_01127708,
                          "com/google/firebase/remoteconfig/FirebaseRemoteConfigFetchThrottledException"
                         );
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_01127738 == 0) {
        DAT_01127738 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,"com/google/firebase/remoteconfig/ConfigUpdate",0
                                 );
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127738,&PTR_s_getUpdatedKeys_00c92858,1,&DAT_01127748,
                          "com/google/firebase/remoteconfig/ConfigUpdate");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      if (DAT_01127758 == 0) {
                    /* try { // try from 00bc5238 to 00cc523f has its CatchHandler @ 00bc6520 */
        DAT_01127758 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (plVar11,uVar15,0,
                                  "com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration"
                                  ,0);
                    /* try { // try from 00bc5240 to 00cc53e7 has its CatchHandler @ 00bc4ce4 */
      }
      uVar12 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                         (plVar11,DAT_01127758,&PTR_s_remove_00c92870,1,&DAT_01127768,
                          "com/google/firebase/remoteconfig/ConfigUpdateListenerRegistration");
      if ((uVar12 & 1) == 0) goto LAB_00bc52ac;
      bVar7 = false;
    }
    if (local_90 != (void *)0x0) {
      _ZdlPv(local_90);
    }
    if (bVar7) goto LAB_00bc56d4;
  }
  lVar5 = DAT_01127538;
  uVar15 = _ZNK8firebase3App14GetPlatformAppEv(*param_1);
  lVar13 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                     (plVar11,lVar5,DAT_01127548,uVar15);
  (**(code **)(*plVar11 + 0xb8))(plVar11,uVar15);
  uVar12 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar11);
  lVar5 = 0;
  if ((uVar12 & 1) == 0) {
    lVar5 = lVar13;
  }
  if (lVar5 == 0) {
    _ZN8firebase9LogAssertEPKcz("config_instance_local");
  }
  uVar15 = (**(code **)(*plVar11 + 0xa8))(plVar11,lVar5);
  param_1[0x33] = uVar15;
  (**(code **)(*plVar11 + 0xb8))(plVar11,lVar5);
  _ZN8firebase8LogDebugEPKcz("%s API Initialized","Remote Config");
LAB_00bc56d4:
  _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev(&local_78);
  if (*(long *)(lVar6 + 0x28) == local_68) {
                    /* try { // try from 00bc5708 to 00cc570f has its CatchHandler @ 00bc6514 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
