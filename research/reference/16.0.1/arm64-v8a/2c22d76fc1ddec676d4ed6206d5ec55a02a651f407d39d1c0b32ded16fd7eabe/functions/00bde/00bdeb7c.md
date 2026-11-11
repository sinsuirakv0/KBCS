# 00bdeb7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bdeb7c",
  "name": "_ZNK8firebase4auth4User13provider_dataEv",
  "size": 1568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a65fda8d4aaae29019ae6371b0c4862da9102b24023117052cd5f35eaafee7c",
  "source_text_sha256": "5a65fda8d4aaae29019ae6371b0c4862da9102b24023117052cd5f35eaafee7c"
}
~~~

## 呼び出し元

- [00c5aab0](../00c5a/00c5aab0.md)

## 呼び出し先

- [00497834](../00497/00497834.md)
- [005762b8](../00576/005762b8.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b2f0](../00c5b/00c5b2f0.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b520](../00c5b/00c5b520.md)
- [00c5db70](../00c5d/00c5db70.md)
- [00c5db80](../00c5d/00c5db80.md)
- [00c5dea0](../00c5d/00c5dea0.md)
- [00c5dec0](../00c5d/00c5dec0.md)
- [00c5ded0](../00c5d/00c5ded0.md)

## 疑似コード / UTF-8 16137 bytes

~~~c

void _ZNK8firebase4auth4User13provider_dataEv(undefined8 *param_1,long param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  long lVar3;
  long lVar4;
  int iVar5;
  uint uVar6;
  long *plVar7;
  long lVar8;
  undefined8 uVar9;
  long *plVar10;
  long lVar11;
  undefined8 *puVar12;
  int iVar13;
  undefined8 local_1c8;
  undefined8 uStack_1c0;
  undefined8 local_1b8;
  undefined *local_1b0;
  ulong local_1a8;
  undefined8 uStack_1a0;
  undefined1 *local_198;
  ulong uStack_190;
  undefined8 local_188;
  undefined1 *local_180;
  ulong local_178;
  undefined8 uStack_170;
  undefined1 *local_168;
  ulong local_160;
  undefined8 uStack_158;
  undefined1 *puStack_150;
  ulong local_148;
  undefined8 uStack_140;
  undefined1 *local_138;
  ulong uStack_130;
  undefined8 local_128;
  undefined1 *local_120;
  undefined *local_118;
  undefined8 local_110;
  undefined8 uStack_108;
  undefined8 local_100;
  undefined8 uStack_f8;
  undefined8 uStack_f0;
  undefined8 uStack_e8;
  undefined8 local_e0;
  undefined8 uStack_d8;
  undefined8 uStack_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 uStack_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 uStack_90;
  undefined8 uStack_88;
  undefined8 *local_80;
  long local_78;
  long local_70;
  
                    /* catch() { ... } // from try @ 00bdd920 with catch @ 00bdeb88 */
                    /* catch() { ... } // from try @ 00bdd6f0 with catch @ 00bdeb8c */
                    /* catch() { ... } // from try @ 00bdd940 with catch @ 00bdeb90 */
  lVar3 = tpidr_el0;
  local_70 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00bdd710 with catch @ 00bdebac */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  puVar12 = *(undefined8 **)(param_2 + 0x98);
                    /* catch() { ... } // from try @ 00bdccbc with catch @ 00bdebc8 */
  if ((puVar12 != (undefined8 *)0x0) && (puVar12[0x40] != 0)) {
                    /* catch() { ... } // from try @ 00bdccb0 with catch @ 00bdebcc */
                    /* catch() { ... } // from try @ 00bdcca0 with catch @ 00bdebd0 */
    plVar7 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*puVar12);
                    /* catch() { ... } // from try @ 00bdcc94 with catch @ 00bdebd8 */
                    /* catch() { ... } // from try @ 00bdc77c with catch @ 00bdebdc */
    lVar8 = FUN_00497834(plVar7,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d40);
    if (lVar8 != 0) {
                    /* catch() { ... } // from try @ 00bd80cc with catch @ 00bdebf8 */
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
      iVar5 = FUN_005762b8(plVar7,lVar8,uVar9);
      _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm
                (param_1,(long)iVar5);
      if (0 < iVar5) {
                    /* catch() { ... } // from try @ 00bd80ac with catch @ 00bdec30 */
        puVar1 = PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9ba60 + 0x10;
        iVar13 = 0;
                    /* catch() { ... } // from try @ 00bd8074 with catch @ 00bdec68 */
        puVar2 = PTR__ZTVN8firebase4auth17UserInfoInterfaceE_00c9b9c8 + 0x10;
        do {
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
                    /* catch() { ... } // from try @ 00bd8050 with catch @ 00bdec88 */
          uVar9 = FUN_00497834(plVar7,lVar8,uVar9,iVar13);
                    /* catch() { ... } // from try @ 00bdcad8 with catch @ 00bdec8c */
          local_80 = *(undefined8 **)(param_2 + 0x98);
          uStack_98 = 0;
          local_a0 = 0;
          uStack_88 = 0;
          uStack_90 = 0;
          uStack_b8 = 0;
          local_c0 = 0;
          uStack_a8 = 0;
          uStack_b0 = 0;
          uStack_d8 = 0;
          local_e0 = 0;
          uStack_c8 = 0;
          uStack_d0 = 0;
          uStack_f8 = 0;
          local_100 = 0;
          uStack_e8 = 0;
          uStack_f0 = 0;
          uStack_108 = 0;
          local_110 = 0;
          local_118 = puVar1;
          local_78 = uVar9;
          plVar10 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*local_80);
                    /* catch() { ... } // from try @ 00bdc8ac with catch @ 00bdecc4 */
                    /* catch() { ... } // from try @ 00bdc8a0 with catch @ 00bdecd4 */
          local_78 = (**(code **)(*plVar10 + 0xa8))(plVar10,uVar9);
                    /* catch() { ... } // from try @ 00bdc34c with catch @ 00bdecd8 */
          (**(code **)(*plVar10 + 0xb8))(plVar10,uVar9);
          lVar4 = local_78;
                    /* catch() { ... } // from try @ 00bdc324 with catch @ 00bdecf4 */
                    /* catch() { ... } // from try @ 00bd918c with catch @ 00bdecf8 */
          uStack_130 = 0;
          local_138 = (undefined1 *)0x0;
          local_120 = (undefined1 *)0x0;
          local_128 = 0;
          puStack_150 = (undefined1 *)0x0;
          uStack_158 = 0;
          uStack_140 = 0;
          local_148 = 0;
                    /* catch() { ... } // from try @ 00bd9224 with catch @ 00bded08 */
          uStack_170 = 0;
          local_178 = 0;
          local_160 = 0;
          local_168 = (undefined1 *)0x0;
                    /* catch() { ... } // from try @ 00bd91e4 with catch @ 00bded0c */
          uStack_190 = 0;
          local_198 = (undefined1 *)0x0;
          local_180 = (undefined1 *)0x0;
          local_188 = 0;
                    /* catch() { ... } // from try @ 00bd9164 with catch @ 00bded10 */
          uStack_1a0 = 0;
          local_1a8 = 0;
          local_1b0 = puVar2;
                    /* catch() { ... } // from try @ 00bd9138 with catch @ 00bded18 */
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
                    /* catch() { ... } // from try @ 00bd90f8 with catch @ 00bded1c */
                    /* catch() { ... } // from try @ 00bd8e50 with catch @ 00bded20 */
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bd8df8 with catch @ 00bded24 */
                    /* catch() { ... } // from try @ 00bd8ef0 with catch @ 00bded28 */
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126dc0);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
                    /* catch() { ... } // from try @ 00bd8ed4 with catch @ 00bded60 */
          }
          if ((local_1a8 & 1) != 0) {
            *local_198 = 0;
            uStack_1a0 = 0;
            if ((local_1a8 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bd8ea0 with catch @ 00bded98 */
              _ZdlPv(local_198);
            }
          }
          lVar4 = local_78;
          local_198 = (undefined1 *)local_1b8;
          uStack_1a0 = uStack_1c0;
          local_1a8 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bd8e80 with catch @ 00bdedd0 */
                    /* catch() { ... } // from try @ 00bdc9b0 with catch @ 00bdedd4 */
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126de8);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
                    /* catch() { ... } // from try @ 00bdc928 with catch @ 00bdedf0 */
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
          if ((uStack_190 & 1) != 0) {
            *local_180 = 0;
            local_188 = 0;
            if ((uStack_190 & 1) != 0) {
              _ZdlPv(local_180);
            }
          }
          lVar4 = local_78;
          local_180 = (undefined1 *)local_1b8;
          local_188 = uStack_1c0;
          uStack_190 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bdc640 with catch @ 00bdee78 */
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126dd0);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
                    /* catch() { ... } // from try @ 00bda4a0 with catch @ 00bdee88 */
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
                    /* catch() { ... } // from try @ 00bda480 with catch @ 00bdeec0 */
          if ((local_178 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bdbbe8 with catch @ 00bdeec4 */
                    /* catch() { ... } // from try @ 00bdb6f4 with catch @ 00bdeec8 */
            *local_168 = 0;
                    /* catch() { ... } // from try @ 00bdc650 with catch @ 00bdeecc
                       catch() { ... } // from try @ 00bdde14 with catch @ 00bdeecc */
            uStack_170 = 0;
            if ((local_178 & 1) != 0) {
              _ZdlPv(local_168);
            }
          }
          lVar4 = local_78;
          local_168 = (undefined1 *)local_1b8;
                    /* catch() { ... } // from try @ 00bd8130 with catch @ 00bdeef4 */
          uStack_170 = uStack_1c0;
          local_178 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126de0);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
                    /* catch() { ... } // from try @ 00bd8114 with catch @ 00bdef58 */
            local_1c8 = 0;
          }
          else {
                    /* catch() { ... } // from try @ 00bd8120 with catch @ 00bdef38 */
            _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
          if ((local_160 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bd88d0 with catch @ 00bdef68 */
            *puStack_150 = 0;
                    /* catch() { ... } // from try @ 00bdbb18 with catch @ 00bdef70 */
            uStack_158 = 0;
                    /* catch() { ... } // from try @ 00bdbb0c with catch @ 00bdef74 */
            if ((local_160 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bdbb00 with catch @ 00bdef78 */
              _ZdlPv(puStack_150);
                    /* catch() { ... } // from try @ 00bdbaf4 with catch @ 00bdef80 */
            }
          }
                    /* catch() { ... } // from try @ 00bd88ec with catch @ 00bdef84 */
          lVar4 = local_78;
          puStack_150 = (undefined1 *)local_1b8;
          uStack_158 = uStack_1c0;
          local_160 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126dc8);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
                    /* catch() { ... } // from try @ 00bd8850 with catch @ 00bdefcc */
                    /* catch() { ... } // from try @ 00bd9bd4 with catch @ 00bdefd0 */
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
                    /* catch() { ... } // from try @ 00bd9bc8 with catch @ 00bdefe8 */
          }
          if ((local_148 & 1) != 0) {
            *local_138 = 0;
                    /* catch() { ... } // from try @ 00bd9b94 with catch @ 00bdf010 */
            uStack_140 = 0;
            if ((local_148 & 1) != 0) {
              _ZdlPv(local_138);
            }
          }
          lVar4 = local_78;
                    /* catch() { ... } // from try @ 00bd8b84 with catch @ 00bdf028
                       catch() { ... } // from try @ 00bd8bf4 with catch @ 00bdf028 */
                    /* catch() { ... } // from try @ 00bd89e8 with catch @ 00bdf02c
                       catch() { ... } // from try @ 00bd8a58 with catch @ 00bdf02c */
                    /* catch() { ... } // from try @ 00bd867c with catch @ 00bdf030
                       catch() { ... } // from try @ 00bd86e8 with catch @ 00bdf030 */
          local_138 = (undefined1 *)local_1b8;
                    /* catch() { ... } // from try @ 00bdb850 with catch @ 00bdf034
                       catch() { ... } // from try @ 00bdb8c0 with catch @ 00bdf034 */
          uStack_140 = uStack_1c0;
          local_148 = local_1c8;
                    /* catch() { ... } // from try @ 00bd8420 with catch @ 00bdf038
                       catch() { ... } // from try @ 00bd8490 with catch @ 00bdf038 */
                    /* catch() { ... } // from try @ 00bd8250 with catch @ 00bdf03c
                       catch() { ... } // from try @ 00bd82c0 with catch @ 00bdf03c */
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bd7818 with catch @ 00bdf04c
                       catch() { ... } // from try @ 00bd7da4 with catch @ 00bdf04c */
                    /* catch() { ... } // from try @ 00bd7c84 with catch @ 00bdf050 */
                    /* catch() { ... } // from try @ 00bd7d64 with catch @ 00bdf054 */
                    /* catch() { ... } // from try @ 00bd7b8c with catch @ 00bdf058 */
            lVar11 = FUN_00497834(uVar9,lVar4,DAT_01126dd8);
                    /* catch() { ... } // from try @ 00bd77bc with catch @ 00bdf05c */
          }
                    /* catch() { ... } // from try @ 00bd78c0 with catch @ 00bdf060 */
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
          if ((uStack_130 & 1) != 0) {
            *local_120 = 0;
            local_128 = 0;
            if ((uStack_130 & 1) != 0) {
              _ZdlPv(local_120);
            }
          }
          lVar11 = param_1[1];
          local_120 = (undefined1 *)local_1b8;
          local_128 = uStack_1c0;
          uStack_130 = local_1c8;
          if (lVar11 == param_1[2]) {
            _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_
                      (param_1,&local_1b0);
          }
          else {
            _ZN8firebase4auth17UserInfoInterfaceC2ERKS1_(lVar11,&local_1b0);
            param_1[1] = lVar11 + 0x98;
          }
          _ZN8firebase4auth17UserInfoInterfaceD2Ev(&local_1b0);
          local_118 = PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9ba60 + 0x10;
          plVar10 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*local_80);
          (**(code **)(*plVar10 + 0xb0))(plVar10,local_78);
          local_78 = 0;
          _ZN8firebase4auth17UserInfoInterfaceD2Ev(&local_118);
          iVar13 = iVar13 + 1;
        } while (iVar5 != iVar13);
      }
      (**(code **)(*plVar7 + 0xb8))(plVar7,lVar8);
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_70) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
