# 00bdfc0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdfc0c",
  "name": "_ZNK8firebase4auth4User13provider_dataEv",
  "size": 1568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be83eb5fac1eba0e95828060729bb94ccc3c7d3a8984c00e280f8eef853108f8",
  "source_text_sha256": "be83eb5fac1eba0e95828060729bb94ccc3c7d3a8984c00e280f8eef853108f8"
}
~~~

## 呼び出し元

- [00c5bb50](../00c5b/00c5bb50.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00576618](../00576/00576618.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c390](../00c5c/00c5c390.md)
- [00c5c430](../00c5c/00c5c430.md)
- [00c5c5c0](../00c5c/00c5c5c0.md)
- [00c5ec10](../00c5e/00c5ec10.md)
- [00c5ec20](../00c5e/00c5ec20.md)
- [00c5ef40](../00c5e/00c5ef40.md)
- [00c5ef60](../00c5e/00c5ef60.md)
- [00c5ef70](../00c5e/00c5ef70.md)

## 疑似コード / UTF-8 15789 bytes

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
  
                    /* catch() { ... } // from try @ 00bde774 with catch @ 00bdfc10 */
                    /* catch() { ... } // from try @ 00bddd20 with catch @ 00bdfc2c */
                    /* catch() { ... } // from try @ 00bddd14 with catch @ 00bdfc30 */
  lVar3 = tpidr_el0;
                    /* catch() { ... } // from try @ 00bddd04 with catch @ 00bdfc34 */
  local_70 = *(long *)(lVar3 + 0x28);
                    /* catch() { ... } // from try @ 00bddcf8 with catch @ 00bdfc3c */
                    /* catch() { ... } // from try @ 00bdd7e0 with catch @ 00bdfc40 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  puVar12 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar12 != (undefined8 *)0x0) && (puVar12[0x40] != 0)) {
                    /* catch() { ... } // from try @ 00bd9130 with catch @ 00bdfc5c */
    plVar7 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*puVar12);
    lVar8 = FUN_00497b94(plVar7,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01127e00);
    if (lVar8 != 0) {
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
                    /* catch() { ... } // from try @ 00bd9110 with catch @ 00bdfc94 */
      iVar5 = FUN_00576618(plVar7,lVar8,uVar9);
      _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm
                (param_1,(long)iVar5);
      if (0 < iVar5) {
                    /* catch() { ... } // from try @ 00bd90d8 with catch @ 00bdfccc */
        puVar1 = PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9cb00 + 0x10;
        iVar13 = 0;
                    /* catch() { ... } // from try @ 00bd90b4 with catch @ 00bdfcec */
                    /* catch() { ... } // from try @ 00bddb3c with catch @ 00bdfcf0 */
        puVar2 = PTR__ZTVN8firebase4auth17UserInfoInterfaceE_00c9ca68 + 0x10;
        do {
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
          uVar9 = FUN_00497b94(plVar7,lVar8,uVar9,iVar13);
                    /* catch() { ... } // from try @ 00bdd910 with catch @ 00bdfd28 */
          local_80 = *(undefined8 **)(param_2 + 0x98);
          uStack_98 = 0;
          local_a0 = 0;
          uStack_88 = 0;
          uStack_90 = 0;
          uStack_b8 = 0;
          local_c0 = 0;
          uStack_a8 = 0;
          uStack_b0 = 0;
                    /* catch() { ... } // from try @ 00bdd904 with catch @ 00bdfd38 */
          uStack_d8 = 0;
          local_e0 = 0;
          uStack_c8 = 0;
          uStack_d0 = 0;
                    /* catch() { ... } // from try @ 00bdd3b0 with catch @ 00bdfd3c */
          uStack_f8 = 0;
          local_100 = 0;
          uStack_e8 = 0;
          uStack_f0 = 0;
          uStack_108 = 0;
          local_110 = 0;
          local_118 = puVar1;
          local_78 = uVar9;
          plVar10 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*local_80);
                    /* catch() { ... } // from try @ 00bdd388 with catch @ 00bdfd58 */
                    /* catch() { ... } // from try @ 00bda1f0 with catch @ 00bdfd5c */
          local_78 = (**(code **)(*plVar10 + 0xa8))(plVar10,uVar9);
                    /* catch() { ... } // from try @ 00bda288 with catch @ 00bdfd6c */
                    /* catch() { ... } // from try @ 00bda248 with catch @ 00bdfd70 */
                    /* catch() { ... } // from try @ 00bda1c8 with catch @ 00bdfd74 */
                    /* catch() { ... } // from try @ 00bda19c with catch @ 00bdfd7c */
          (**(code **)(*plVar10 + 0xb8))(plVar10,uVar9);
          lVar4 = local_78;
                    /* catch() { ... } // from try @ 00bda15c with catch @ 00bdfd80 */
                    /* catch() { ... } // from try @ 00bd9eb4 with catch @ 00bdfd84 */
                    /* catch() { ... } // from try @ 00bd9e5c with catch @ 00bdfd88 */
                    /* catch() { ... } // from try @ 00bd9f54 with catch @ 00bdfd8c */
          uStack_130 = 0;
          local_138 = (undefined1 *)0x0;
          local_120 = (undefined1 *)0x0;
          local_128 = 0;
          puStack_150 = (undefined1 *)0x0;
          uStack_158 = 0;
          uStack_140 = 0;
          local_148 = 0;
          uStack_170 = 0;
          local_178 = 0;
          local_160 = 0;
          local_168 = (undefined1 *)0x0;
          uStack_190 = 0;
          local_198 = (undefined1 *)0x0;
          local_180 = (undefined1 *)0x0;
          local_188 = 0;
          uStack_1a0 = 0;
          local_1a8 = 0;
          local_1b0 = puVar2;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bd9f38 with catch @ 00bdfdc4 */
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127e80);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
          if ((local_1a8 & 1) != 0) {
            *local_198 = 0;
            uStack_1a0 = 0;
            if ((local_1a8 & 1) != 0) {
              _ZdlPv(local_198);
            }
          }
          lVar4 = local_78;
                    /* catch() { ... } // from try @ 00bd9ee4 with catch @ 00bdfe34 */
                    /* catch() { ... } // from try @ 00bdda14 with catch @ 00bdfe38 */
          local_198 = (undefined1 *)local_1b8;
          uStack_1a0 = uStack_1c0;
          local_1a8 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bdd98c with catch @ 00bdfe54 */
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127ea8);
          }
                    /* catch() { ... } // from try @ 00bdd70c with catch @ 00bdfe70 */
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
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
                    /* catch() { ... } // from try @ 00bdd6a4 with catch @ 00bdfedc */
          local_180 = (undefined1 *)local_1b8;
          local_188 = uStack_1c0;
          uStack_190 = local_1c8;
                    /* catch() { ... } // from try @ 00bdb504 with catch @ 00bdfeec */
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127e90);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
          }
          else {
                    /* catch() { ... } // from try @ 00bdb4e4 with catch @ 00bdff24 */
                    /* catch() { ... } // from try @ 00bdcc4c with catch @ 00bdff28 */
                    /* catch() { ... } // from try @ 00bdc758 with catch @ 00bdff2c */
                    /* catch() { ... } // from try @ 00bdd6b4 with catch @ 00bdff30
                       catch() { ... } // from try @ 00bdee78 with catch @ 00bdff30 */
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
          }
          if ((local_178 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bd9194 with catch @ 00bdff58 */
            *local_168 = 0;
            uStack_170 = 0;
            if ((local_178 & 1) != 0) {
              _ZdlPv(local_168);
            }
          }
          lVar4 = local_78;
          local_168 = (undefined1 *)local_1b8;
          uStack_170 = uStack_1c0;
          local_178 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
                    /* catch() { ... } // from try @ 00bd9184 with catch @ 00bdff9c */
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127ea0);
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
                    /* catch() { ... } // from try @ 00bd9178 with catch @ 00bdffbc */
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
                    /* catch() { ... } // from try @ 00bdcb58 with catch @ 00bdffe4 */
            uStack_1c0 = 0;
            local_1b8 = 0;
                    /* catch() { ... } // from try @ 00bd9950 with catch @ 00bdffe8 */
            local_1c8 = 0;
          }
          else {
                    /* catch() { ... } // from try @ 00bd9934 with catch @ 00bdffcc */
            _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
                    /* catch() { ... } // from try @ 00bdcb7c with catch @ 00bdffd4 */
                    /* catch() { ... } // from try @ 00bdcb70 with catch @ 00bdffd8 */
          }
          if ((local_160 & 1) != 0) {
            *puStack_150 = 0;
            uStack_158 = 0;
            if ((local_160 & 1) != 0) {
              _ZdlPv(puStack_150);
            }
          }
          lVar4 = local_78;
          puStack_150 = (undefined1 *)local_1b8;
          uStack_158 = uStack_1c0;
          local_160 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
                    /* catch() { ... } // from try @ 00bd98b4 with catch @ 00be0030 */
                    /* catch() { ... } // from try @ 00bdac38 with catch @ 00be0034 */
          lVar11 = 0;
          if (lVar4 != 0) {
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127e88);
                    /* catch() { ... } // from try @ 00bdac2c with catch @ 00be004c */
          }
          uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar9);
          if ((lVar11 == 0) || (((uVar6 ^ 1) & 1) == 0)) {
            uStack_1c0 = 0;
            local_1b8 = 0;
            local_1c8 = 0;
                    /* catch() { ... } // from try @ 00bd9be8 with catch @ 00be008c
                       catch() { ... } // from try @ 00bd9c58 with catch @ 00be008c */
          }
          else {
            _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_1c8,uVar9,lVar11);
                    /* catch() { ... } // from try @ 00bdabf8 with catch @ 00be0074 */
          }
                    /* catch() { ... } // from try @ 00bd9a4c with catch @ 00be0090
                       catch() { ... } // from try @ 00bd9abc with catch @ 00be0090 */
          if ((local_148 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bd96e0 with catch @ 00be0094
                       catch() { ... } // from try @ 00bd974c with catch @ 00be0094 */
                    /* catch() { ... } // from try @ 00bdc8b4 with catch @ 00be0098
                       catch() { ... } // from try @ 00bdc924 with catch @ 00be0098 */
            *local_138 = 0;
                    /* catch() { ... } // from try @ 00bd9484 with catch @ 00be009c
                       catch() { ... } // from try @ 00bd94f4 with catch @ 00be009c */
                    /* catch() { ... } // from try @ 00bd92b4 with catch @ 00be00a0
                       catch() { ... } // from try @ 00bd9324 with catch @ 00be00a0 */
            uStack_140 = 0;
            if ((local_148 & 1) != 0) {
              _ZdlPv(local_138);
                    /* catch() { ... } // from try @ 00bd887c with catch @ 00be00b0
                       catch() { ... } // from try @ 00bd8e08 with catch @ 00be00b0 */
            }
          }
                    /* catch() { ... } // from try @ 00bd8ce8 with catch @ 00be00b4 */
          lVar4 = local_78;
                    /* catch() { ... } // from try @ 00bd8dc8 with catch @ 00be00b8 */
                    /* catch() { ... } // from try @ 00bd8bf0 with catch @ 00be00bc */
                    /* catch() { ... } // from try @ 00bd8820 with catch @ 00be00c0 */
          local_138 = (undefined1 *)local_1b8;
                    /* catch() { ... } // from try @ 00bd8924 with catch @ 00be00c4 */
          uStack_140 = uStack_1c0;
          local_148 = local_1c8;
          uVar9 = _ZNK8firebase3App9GetJNIEnvEv(*local_80);
          lVar11 = 0;
          if (lVar4 != 0) {
            lVar11 = FUN_00497b94(uVar9,lVar4,DAT_01127e98);
          }
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
          local_118 = PTR__ZTVN8firebase4auth22AndroidWrappedUserInfoE_00c9cb00 + 0x10;
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
