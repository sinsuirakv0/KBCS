# 00bdeb7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bde754`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde754.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-ac67ab9dccc68c670e3a1753917b701d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdec18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-d032c60b6705583d97ea0efbdb1200fd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "5a65fda8d4aaae29019ae6371b0c4862da9102b24023117052cd5f35eaafee7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeb7c",
        "00bdf19b"
      ]
    ],
    "bytes_sha256": "b45fa7dc1fc4f16db2940e0fa7539cbaf1f8548f5f6aeeda4cdde6567e0c390d",
    "instruction_count": 392,
    "instruction_bytes": 1568,
    "body_bytes": 1568,
    "indirect": 4,
    "unresolved": 4
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeb7c"></a> `00bdeb7c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bdeb80"></a> `00bdeb80` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeb84"></a> `00bdeb84` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdeb88"></a> `00bdeb88` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdeb8c"></a> `00bdeb8c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdeb90"></a> `00bdeb90` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdeb94"></a> `00bdeb94` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdeb98"></a> `00bdeb98` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00bdeb9c"></a> `00bdeb9c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdeba0"></a> `00bdeba0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdeba4"></a> `00bdeba4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdeba8"></a> `00bdeba8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bdebac"></a> `00bdebac` | `a8 03 1a f8` | stur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bdebb0"></a> `00bdebb0` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdebb4"></a> `00bdebb4` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdebb8"></a> `00bdebb8` | `08 4c 40 f9` | ldr x8,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdebbc"></a> `00bdebbc` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdebc0"></a> `00bdebc0` | `28 2d 00 b4` | cbz x8,0x00bdf164 | `CONDITIONAL_JUMP`
<a id="insn-00bdebc4"></a> `00bdebc4` | `09 01 41 f9` | ldr x9,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdebc8"></a> `00bdebc8` | `e9 2c 00 b4` | cbz x9,0x00bdf164 | `CONDITIONAL_JUMP`
<a id="insn-00bdebcc"></a> `00bdebcc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdebd0"></a> `00bdebd0` | `2c f1 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdebd4"></a> `00bdebd4` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdebd8"></a> `00bdebd8` | `49 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdebdc"></a> `00bdebdc` | `22 a1 46 f9` | ldr x2,[x9, #0xd40] | `FALL_THROUGH`
<a id="insn-00bdebe0"></a> `00bdebe0` | `08 4d 40 f9` | ldr x8,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00bdebe4"></a> `00bdebe4` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdebe8"></a> `00bdebe8` | `e0 1f 00 f9` | str x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdebec"></a> `00bdebec` | `12 e3 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdebf0"></a> `00bdebf0` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdebf4"></a> `00bdebf4` | `80 2b 00 b4` | cbz x0,0x00bdf164 | `CONDITIONAL_JUMP`
<a id="insn-00bdebf8"></a> `00bdebf8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bdebfc"></a> `00bdebfc` | `49 f2 01 94` | bl 0x00c5b520 | `UNCONDITIONAL_CALL`
<a id="insn-00bdec00"></a> `00bdec00` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdec04"></a> `00bdec04` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdec08"></a> `00bdec08` | `ac 5d e6 97` | bl 0x005762b8 | `UNCONDITIONAL_CALL`
<a id="insn-00bdec0c"></a> `00bdec0c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdec10"></a> `00bdec10` | `81 7e 40 93` | sxtw x1,w20 | `FALL_THROUGH`
<a id="insn-00bdec14"></a> `00bdec14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdec18"></a> `00bdec18` | `ae fc 01 94` | bl 0x00c5ded0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdec1c"></a> `00bdec1c` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bdec20"></a> `00bdec20` | `f4 17 00 f9` | str x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdec24"></a> `00bdec24` | `8b 29 00 54` | b.lt 0x00bdf154 | `CONDITIONAL_JUMP`
<a id="insn-00bdec28"></a> `00bdec28` | `eb 05 00 b0` | adrp x11,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdec2c"></a> `00bdec2c` | `6b 31 45 f9` | ldr x11,[x11, #0xa60] | `FALL_THROUGH`
<a id="insn-00bdec30"></a> `00bdec30` | `ea 05 00 b0` | adrp x10,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdec34"></a> `00bdec34` | `4a e5 44 f9` | ldr x10,[x10, #0x9c8] | `FALL_THROUGH`
<a id="insn-00bdec38"></a> `00bdec38` | `e8 e3 03 91` | add x8,sp,#0xf8 | `FALL_THROUGH`
<a id="insn-00bdec3c"></a> `00bdec3c` | `e9 83 01 91` | add x9,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdec40"></a> `00bdec40` | `1c 21 00 91` | add x28,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdec44"></a> `00bdec44` | `28 81 00 91` | add x8,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bdec48"></a> `00bdec48` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdec4c"></a> `00bdec4c` | `68 41 00 91` | add x8,x11,#0x10 | `FALL_THROUGH`
<a id="insn-00bdec50"></a> `00bdec50` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00bdec54"></a> `00bdec54` | `3b 21 00 91` | add x27,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bdec58"></a> `00bdec58` | `36 e1 00 91` | add x22,x9,#0x38 | `FALL_THROUGH`
<a id="insn-00bdec5c"></a> `00bdec5c` | `35 41 01 91` | add x21,x9,#0x50 | `FALL_THROUGH`
<a id="insn-00bdec60"></a> `00bdec60` | `34 a1 01 91` | add x20,x9,#0x68 | `FALL_THROUGH`
<a id="insn-00bdec64"></a> `00bdec64` | `37 01 02 91` | add x23,x9,#0x80 | `FALL_THROUGH`
<a id="insn-00bdec68"></a> `00bdec68` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdec6c"></a> `00bdec6c` | `48 41 00 91` | add x8,x10,#0x10 | `FALL_THROUGH`
<a id="insn-00bdec70"></a> `00bdec70` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdec74"></a> `00bdec74` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdec78"></a> `00bdec78` | `2a f2 01 94` | bl 0x00c5b520 | `UNCONDITIONAL_CALL`
<a id="insn-00bdec7c"></a> `00bdec7c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdec80"></a> `00bdec80` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdec84"></a> `00bdec84` | `e3 03 18 2a` | mov w3,w24 | `FALL_THROUGH`
<a id="insn-00bdec88"></a> `00bdec88` | `eb e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdec8c"></a> `00bdec8c` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdec90"></a> `00bdec90` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdec94"></a> `00bdec94` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdec98"></a> `00bdec98` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdec9c"></a> `00bdec9c` | `08 4d 40 f9` | ldr x8,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeca0"></a> `00bdeca0` | `80 83 03 ad` | stp q0,q0,[x28, #0x70] | `FALL_THROUGH`
<a id="insn-00bdeca4"></a> `00bdeca4` | `80 83 02 ad` | stp q0,q0,[x28, #0x50] | `FALL_THROUGH`
<a id="insn-00bdeca8"></a> `00bdeca8` | `80 83 01 ad` | stp q0,q0,[x28, #0x30] | `FALL_THROUGH`
<a id="insn-00bdecac"></a> `00bdecac` | `80 83 00 ad` | stp q0,q0,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00bdecb0"></a> `00bdecb0` | `80 03 80 3d` | str q0,[x28] | `FALL_THROUGH`
<a id="insn-00bdecb4"></a> `00bdecb4` | `e9 7f 00 f9` | str x9,[sp, #0xf8] | `FALL_THROUGH`
<a id="insn-00bdecb8"></a> `00bdecb8` | `e8 03 19 a9` | stp x8,x0,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdecbc"></a> `00bdecbc` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdecc0"></a> `00bdecc0` | `f0 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdecc4"></a> `00bdecc4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdecc8"></a> `00bdecc8` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdeccc"></a> `00bdeccc` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdecd0"></a> `00bdecd0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bdecd4"></a> `00bdecd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdecd8"></a> `00bdecd8` | `e0 cf 00 f9` | str x0,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00bdecdc"></a> `00bdecdc` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00bdece0"></a> `00bdece0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdece4"></a> `00bdece4` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bdece8"></a> `00bdece8` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bdecec"></a> `00bdecec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdecf0"></a> `00bdecf0` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdecf4"></a> `00bdecf4` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdecf8"></a> `00bdecf8` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdecfc"></a> `00bdecfc` | `e8 6b 59 a9` | ldp x8,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bded00"></a> `00bded00` | `60 83 03 ad` | stp q0,q0,[x27, #0x70] | `FALL_THROUGH`
<a id="insn-00bded04"></a> `00bded04` | `60 83 02 ad` | stp q0,q0,[x27, #0x50] | `FALL_THROUGH`
<a id="insn-00bded08"></a> `00bded08` | `60 83 01 ad` | stp q0,q0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00bded0c"></a> `00bded0c` | `60 83 00 ad` | stp q0,q0,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bded10"></a> `00bded10` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00bded14"></a> `00bded14` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bded18"></a> `00bded18` | `da f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bded1c"></a> `00bded1c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bded20"></a> `00bded20` | `fa 00 00 b4` | cbz x26,0x00bded3c | `CONDITIONAL_JUMP`
<a id="insn-00bded24"></a> `00bded24` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bded28"></a> `00bded28` | `02 e1 46 f9` | ldr x2,[x8, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bded2c"></a> `00bded2c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bded30"></a> `00bded30` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bded34"></a> `00bded34` | `c0 e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bded38"></a> `00bded38` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bded3c"></a> `00bded3c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bded40"></a> `00bded40` | `88 f0 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bded44"></a> `00bded44` | `7a 01 00 b4` | cbz x26,0x00bded70 | `CONDITIONAL_JUMP`
<a id="insn-00bded48"></a> `00bded48` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bded4c"></a> `00bded4c` | `28 01 00 36` | tbz w8,#0x0,0x00bded70 | `CONDITIONAL_JUMP`
<a id="insn-00bded50"></a> `00bded50` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bded54"></a> `00bded54` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bded58"></a> `00bded58` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bded5c"></a> `00bded5c` | `8d f1 01 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bded60"></a> `00bded60` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bded64"></a> `00bded64` | `e8 00 00 37` | tbnz w8,#0x0,0x00bded80 | `CONDITIONAL_JUMP`
<a id="insn-00bded68"></a> `00bded68` | `ff d3 00 79` | strh wzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bded6c"></a> `00bded6c` | `0d 00 00 14` | b 0x00bdeda0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bded70"></a> `00bded70` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bded74"></a> `00bded74` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bded78"></a> `00bded78` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bded7c"></a> `00bded7c` | `68 ff 07 36` | tbz w8,#0x0,0x00bded68 | `CONDITIONAL_JUMP`
<a id="insn-00bded80"></a> `00bded80` | `e8 3f 40 f9` | ldr x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bded84"></a> `00bded84` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bded88"></a> `00bded88` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bded8c"></a> `00bded8c` | `ff 3b 00 f9` | str xzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bded90"></a> `00bded90` | `88 00 00 36` | tbz w8,#0x0,0x00bdeda0 | `CONDITIONAL_JUMP`
<a id="insn-00bded94"></a> `00bded94` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bded98"></a> `00bded98` | `46 e4 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bded9c"></a> `00bded9c` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdeda0"></a> `00bdeda0` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdeda4"></a> `00bdeda4` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdeda8"></a> `00bdeda8` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdedac"></a> `00bdedac` | `68 0b 00 f9` | str x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bdedb0"></a> `00bdedb0` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00bdedb4"></a> `00bdedb4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdedb8"></a> `00bdedb8` | `b2 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdedbc"></a> `00bdedbc` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdedc0"></a> `00bdedc0` | `fa 00 00 b4` | cbz x26,0x00bdeddc | `CONDITIONAL_JUMP`
<a id="insn-00bdedc4"></a> `00bdedc4` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdedc8"></a> `00bdedc8` | `02 f5 46 f9` | ldr x2,[x8, #0xde8] | `FALL_THROUGH`
<a id="insn-00bdedcc"></a> `00bdedcc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdedd0"></a> `00bdedd0` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdedd4"></a> `00bdedd4` | `98 e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdedd8"></a> `00bdedd8` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdeddc"></a> `00bdeddc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdede0"></a> `00bdede0` | `60 f0 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdede4"></a> `00bdede4` | `7a 01 00 b4` | cbz x26,0x00bdee10 | `CONDITIONAL_JUMP`
<a id="insn-00bdede8"></a> `00bdede8` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdedec"></a> `00bdedec` | `28 01 00 36` | tbz w8,#0x0,0x00bdee10 | `CONDITIONAL_JUMP`
<a id="insn-00bdedf0"></a> `00bdedf0` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdedf4"></a> `00bdedf4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdedf8"></a> `00bdedf8` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdedfc"></a> `00bdedfc` | `65 f1 01 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bdee00"></a> `00bdee00` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdee04"></a> `00bdee04` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdee20 | `CONDITIONAL_JUMP`
<a id="insn-00bdee08"></a> `00bdee08` | `ff 03 01 79` | strh wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdee0c"></a> `00bdee0c` | `0d 00 00 14` | b 0x00bdee40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdee10"></a> `00bdee10` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdee14"></a> `00bdee14` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdee18"></a> `00bdee18` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdee1c"></a> `00bdee1c` | `68 ff 07 36` | tbz w8,#0x0,0x00bdee08 | `CONDITIONAL_JUMP`
<a id="insn-00bdee20"></a> `00bdee20` | `e8 4b 40 f9` | ldr x8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdee24"></a> `00bdee24` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdee28"></a> `00bdee28` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdee2c"></a> `00bdee2c` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00bdee30"></a> `00bdee30` | `88 00 00 36` | tbz w8,#0x0,0x00bdee40 | `CONDITIONAL_JUMP`
<a id="insn-00bdee34"></a> `00bdee34` | `e0 4b 40 f9` | ldr x0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdee38"></a> `00bdee38` | `1e e4 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdee3c"></a> `00bdee3c` | `ff 43 00 f9` | str xzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdee40"></a> `00bdee40` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdee44"></a> `00bdee44` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdee48"></a> `00bdee48` | `ea 0b 40 f9` | ldr x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdee4c"></a> `00bdee4c` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdee50"></a> `00bdee50` | `48 09 00 f9` | str x8,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00bdee54"></a> `00bdee54` | `40 01 80 3d` | str q0,[x10] | `FALL_THROUGH`
<a id="insn-00bdee58"></a> `00bdee58` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdee5c"></a> `00bdee5c` | `89 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdee60"></a> `00bdee60` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdee64"></a> `00bdee64` | `fa 00 00 b4` | cbz x26,0x00bdee80 | `CONDITIONAL_JUMP`
<a id="insn-00bdee68"></a> `00bdee68` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdee6c"></a> `00bdee6c` | `02 e9 46 f9` | ldr x2,[x8, #0xdd0] | `FALL_THROUGH`
<a id="insn-00bdee70"></a> `00bdee70` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdee74"></a> `00bdee74` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdee78"></a> `00bdee78` | `6f e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdee7c"></a> `00bdee7c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdee80"></a> `00bdee80` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdee84"></a> `00bdee84` | `37 f0 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdee88"></a> `00bdee88` | `7a 01 00 b4` | cbz x26,0x00bdeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bdee8c"></a> `00bdee8c` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdee90"></a> `00bdee90` | `28 01 00 36` | tbz w8,#0x0,0x00bdeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00bdee94"></a> `00bdee94` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdee98"></a> `00bdee98` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdee9c"></a> `00bdee9c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdeea0"></a> `00bdeea0` | `3c f1 01 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeea4"></a> `00bdeea4` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeea8"></a> `00bdeea8` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdeec4 | `CONDITIONAL_JUMP`
<a id="insn-00bdeeac"></a> `00bdeeac` | `ff 33 01 79` | strh wzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeeb0"></a> `00bdeeb0` | `0d 00 00 14` | b 0x00bdeee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdeeb4"></a> `00bdeeb4` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdeeb8"></a> `00bdeeb8` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdeebc"></a> `00bdeebc` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeec0"></a> `00bdeec0` | `68 ff 07 36` | tbz w8,#0x0,0x00bdeeac | `CONDITIONAL_JUMP`
<a id="insn-00bdeec4"></a> `00bdeec4` | `e8 57 40 f9` | ldr x8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdeec8"></a> `00bdeec8` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdeecc"></a> `00bdeecc` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeed0"></a> `00bdeed0` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdeed4"></a> `00bdeed4` | `88 00 00 36` | tbz w8,#0x0,0x00bdeee4 | `CONDITIONAL_JUMP`
<a id="insn-00bdeed8"></a> `00bdeed8` | `e0 57 40 f9` | ldr x0,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdeedc"></a> `00bdeedc` | `f5 e3 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdeee0"></a> `00bdeee0` | `ff 4f 00 f9` | str xzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdeee4"></a> `00bdeee4` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdeee8"></a> `00bdeee8` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdeeec"></a> `00bdeeec` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdeef0"></a> `00bdeef0` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bdeef4"></a> `00bdeef4` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bdeef8"></a> `00bdeef8` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdeefc"></a> `00bdeefc` | `61 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdef00"></a> `00bdef00` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdef04"></a> `00bdef04` | `fa 00 00 b4` | cbz x26,0x00bdef20 | `CONDITIONAL_JUMP`
<a id="insn-00bdef08"></a> `00bdef08` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdef0c"></a> `00bdef0c` | `02 f1 46 f9` | ldr x2,[x8, #0xde0] | `FALL_THROUGH`
<a id="insn-00bdef10"></a> `00bdef10` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdef14"></a> `00bdef14` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdef18"></a> `00bdef18` | `47 e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdef1c"></a> `00bdef1c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdef20"></a> `00bdef20` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdef24"></a> `00bdef24` | `0f f0 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdef28"></a> `00bdef28` | `7a 01 00 b4` | cbz x26,0x00bdef54 | `CONDITIONAL_JUMP`
<a id="insn-00bdef2c"></a> `00bdef2c` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdef30"></a> `00bdef30` | `28 01 00 36` | tbz w8,#0x0,0x00bdef54 | `CONDITIONAL_JUMP`
<a id="insn-00bdef34"></a> `00bdef34` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdef38"></a> `00bdef38` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdef3c"></a> `00bdef3c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdef40"></a> `00bdef40` | `ec f0 01 94` | bl 0x00c5b2f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdef44"></a> `00bdef44` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdef48"></a> `00bdef48` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdef64 | `CONDITIONAL_JUMP`
<a id="insn-00bdef4c"></a> `00bdef4c` | `ff 63 01 79` | strh wzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdef50"></a> `00bdef50` | `0d 00 00 14` | b 0x00bdef84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdef54"></a> `00bdef54` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdef58"></a> `00bdef58` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdef5c"></a> `00bdef5c` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdef60"></a> `00bdef60` | `68 ff 07 36` | tbz w8,#0x0,0x00bdef4c | `CONDITIONAL_JUMP`
<a id="insn-00bdef64"></a> `00bdef64` | `e8 63 40 f9` | ldr x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdef68"></a> `00bdef68` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdef6c"></a> `00bdef6c` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdef70"></a> `00bdef70` | `ff 5f 00 f9` | str xzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdef74"></a> `00bdef74` | `88 00 00 36` | tbz w8,#0x0,0x00bdef84 | `CONDITIONAL_JUMP`
<a id="insn-00bdef78"></a> `00bdef78` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdef7c"></a> `00bdef7c` | `cd e3 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdef80"></a> `00bdef80` | `ff 5b 00 f9` | str xzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdef84"></a> `00bdef84` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdef88"></a> `00bdef88` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdef8c"></a> `00bdef8c` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdef90"></a> `00bdef90` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdef94"></a> `00bdef94` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bdef98"></a> `00bdef98` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdef9c"></a> `00bdef9c` | `39 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefa0"></a> `00bdefa0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdefa4"></a> `00bdefa4` | `fa 00 00 b4` | cbz x26,0x00bdefc0 | `CONDITIONAL_JUMP`
<a id="insn-00bdefa8"></a> `00bdefa8` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdefac"></a> `00bdefac` | `02 e5 46 f9` | ldr x2,[x8, #0xdc8] | `FALL_THROUGH`
<a id="insn-00bdefb0"></a> `00bdefb0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdefb4"></a> `00bdefb4` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdefb8"></a> `00bdefb8` | `1f e2 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefbc"></a> `00bdefbc` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdefc0"></a> `00bdefc0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdefc4"></a> `00bdefc4` | `e7 ef 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefc8"></a> `00bdefc8` | `7a 01 00 b4` | cbz x26,0x00bdeff4 | `CONDITIONAL_JUMP`
<a id="insn-00bdefcc"></a> `00bdefcc` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdefd0"></a> `00bdefd0` | `28 01 00 36` | tbz w8,#0x0,0x00bdeff4 | `CONDITIONAL_JUMP`
<a id="insn-00bdefd4"></a> `00bdefd4` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdefd8"></a> `00bdefd8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdefdc"></a> `00bdefdc` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdefe0"></a> `00bdefe0` | `ec f0 01 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bdefe4"></a> `00bdefe4` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bdefe8"></a> `00bdefe8` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdf004 | `CONDITIONAL_JUMP`
<a id="insn-00bdefec"></a> `00bdefec` | `ff 93 01 79` | strh wzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bdeff0"></a> `00bdeff0` | `0d 00 00 14` | b 0x00bdf024 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdeff4"></a> `00bdeff4` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdeff8"></a> `00bdeff8` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdeffc"></a> `00bdeffc` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bdf000"></a> `00bdf000` | `68 ff 07 36` | tbz w8,#0x0,0x00bdefec | `CONDITIONAL_JUMP`
<a id="insn-00bdf004"></a> `00bdf004` | `e8 6f 40 f9` | ldr x8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00bdf008"></a> `00bdf008` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdf00c"></a> `00bdf00c` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bdf010"></a> `00bdf010` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bdf014"></a> `00bdf014` | `88 00 00 36` | tbz w8,#0x0,0x00bdf024 | `CONDITIONAL_JUMP`
<a id="insn-00bdf018"></a> `00bdf018` | `e0 6f 40 f9` | ldr x0,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00bdf01c"></a> `00bdf01c` | `a5 e3 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf020"></a> `00bdf020` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00bdf024"></a> `00bdf024` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdf028"></a> `00bdf028` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdf02c"></a> `00bdf02c` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdf030"></a> `00bdf030` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf034"></a> `00bdf034` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00bdf038"></a> `00bdf038` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdf03c"></a> `00bdf03c` | `11 f0 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf040"></a> `00bdf040` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdf044"></a> `00bdf044` | `fa 00 00 b4` | cbz x26,0x00bdf060 | `CONDITIONAL_JUMP`
<a id="insn-00bdf048"></a> `00bdf048` | `28 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdf04c"></a> `00bdf04c` | `02 ed 46 f9` | ldr x2,[x8, #0xdd8] | `FALL_THROUGH`
<a id="insn-00bdf050"></a> `00bdf050` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdf054"></a> `00bdf054` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdf058"></a> `00bdf058` | `f7 e1 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf05c"></a> `00bdf05c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdf060"></a> `00bdf060` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdf064"></a> `00bdf064` | `bf ef 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf068"></a> `00bdf068` | `7a 01 00 b4` | cbz x26,0x00bdf094 | `CONDITIONAL_JUMP`
<a id="insn-00bdf06c"></a> `00bdf06c` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdf070"></a> `00bdf070` | `28 01 00 36` | tbz w8,#0x0,0x00bdf094 | `CONDITIONAL_JUMP`
<a id="insn-00bdf074"></a> `00bdf074` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdf078"></a> `00bdf078` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdf07c"></a> `00bdf07c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdf080"></a> `00bdf080` | `c4 f0 01 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf084"></a> `00bdf084` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdf088"></a> `00bdf088` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdf0a4 | `CONDITIONAL_JUMP`
<a id="insn-00bdf08c"></a> `00bdf08c` | `ff c3 01 79` | strh wzr,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdf090"></a> `00bdf090` | `0d 00 00 14` | b 0x00bdf0c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdf094"></a> `00bdf094` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdf098"></a> `00bdf098` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdf09c"></a> `00bdf09c` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdf0a0"></a> `00bdf0a0` | `68 ff 07 36` | tbz w8,#0x0,0x00bdf08c | `CONDITIONAL_JUMP`
<a id="insn-00bdf0a4"></a> `00bdf0a4` | `e8 7b 40 f9` | ldr x8,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bdf0a8"></a> `00bdf0a8` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdf0ac"></a> `00bdf0ac` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdf0b0"></a> `00bdf0b0` | `ff 77 00 f9` | str xzr,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00bdf0b4"></a> `00bdf0b4` | `88 00 00 36` | tbz w8,#0x0,0x00bdf0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bdf0b8"></a> `00bdf0b8` | `e0 7b 40 f9` | ldr x0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bdf0bc"></a> `00bdf0bc` | `7d e3 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf0c0"></a> `00bdf0c0` | `ff 73 00 f9` | str xzr,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdf0c4"></a> `00bdf0c4` | `79 a6 40 a9` | ldp x25,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdf0c8"></a> `00bdf0c8` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdf0cc"></a> `00bdf0cc` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdf0d0"></a> `00bdf0d0` | `3f 03 09 eb` | cmp x25,x9 | `FALL_THROUGH`
<a id="insn-00bdf0d4"></a> `00bdf0d4` | `e8 0a 00 f9` | str x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf0d8"></a> `00bdf0d8` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-00bdf0dc"></a> `00bdf0dc` | `e0 00 00 54` | b.eq 0x00bdf0f8 | `CONDITIONAL_JUMP`
<a id="insn-00bdf0e0"></a> `00bdf0e0` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdf0e4"></a> `00bdf0e4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdf0e8"></a> `00bdf0e8` | `6e fb 01 94` | bl 0x00c5dea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf0ec"></a> `00bdf0ec` | `28 63 02 91` | add x8,x25,#0x98 | `FALL_THROUGH`
<a id="insn-00bdf0f0"></a> `00bdf0f0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdf0f4"></a> `00bdf0f4` | `04 00 00 14` | b 0x00bdf104 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdf0f8"></a> `00bdf0f8` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdf0fc"></a> `00bdf0fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf100"></a> `00bdf100` | `70 fb 01 94` | bl 0x00c5dec0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf104"></a> `00bdf104` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdf108"></a> `00bdf108` | `9a fa 01 94` | bl 0x00c5db70 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf10c"></a> `00bdf10c` | `e9 05 00 90` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdf110"></a> `00bdf110` | `e8 cb 40 f9` | ldr x8,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdf114"></a> `00bdf114` | `29 31 45 f9` | ldr x9,[x9, #0xa60] | `FALL_THROUGH`
<a id="insn-00bdf118"></a> `00bdf118` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bdf11c"></a> `00bdf11c` | `e9 7f 00 f9` | str x9,[sp, #0xf8] | `FALL_THROUGH`
<a id="insn-00bdf120"></a> `00bdf120` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdf124"></a> `00bdf124` | `d7 ef 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf128"></a> `00bdf128` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdf12c"></a> `00bdf12c` | `e1 cf 40 f9` | ldr x1,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00bdf130"></a> `00bdf130` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdf134"></a> `00bdf134` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf138"></a> `00bdf138` | `e0 e3 03 91` | add x0,sp,#0xf8 | `FALL_THROUGH`
<a id="insn-00bdf13c"></a> `00bdf13c` | `ff cf 00 f9` | str xzr,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00bdf140"></a> `00bdf140` | `90 fa 01 94` | bl 0x00c5db80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf144"></a> `00bdf144` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdf148"></a> `00bdf148` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bdf14c"></a> `00bdf14c` | `1f 01 18 6b` | cmp w8,w24 | `FALL_THROUGH`
<a id="insn-00bdf150"></a> `00bdf150` | `21 d9 ff 54` | b.ne 0x00bdec74 | `CONDITIONAL_JUMP`
<a id="insn-00bdf154"></a> `00bdf154` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdf158"></a> `00bdf158` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdf15c"></a> `00bdf15c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdf160"></a> `00bdf160` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdf164"></a> `00bdf164` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdf168"></a> `00bdf168` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bdf16c"></a> `00bdf16c` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bdf170"></a> `00bdf170` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdf174"></a> `00bdf174` | `21 01 00 54` | b.ne 0x00bdf198 | `CONDITIONAL_JUMP`
<a id="insn-00bdf178"></a> `00bdf178` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00bdf17c"></a> `00bdf17c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdf180"></a> `00bdf180` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdf184"></a> `00bdf184` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdf188"></a> `00bdf188` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf18c"></a> `00bdf18c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf190"></a> `00bdf190` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bdf194"></a> `00bdf194` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdf198"></a> `00bdf198` | `52 e3 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeb7c`](#insn-00bdeb7c) 範囲 `[['00bdeb7c', '00bdeb87']]`
  - `FALL_THROUGH` [`00bdeb84`](#insn-00bdeb84) → [`00bdeb88`](#insn-00bdeb88)
- ブロック [`00bdeb88`](#insn-00bdeb88) 範囲 `[['00bdeb88', '00bdeb8b']]`
  - `FALL_THROUGH` [`00bdeb88`](#insn-00bdeb88) → [`00bdeb8c`](#insn-00bdeb8c)
- ブロック [`00bdeb8c`](#insn-00bdeb8c) 範囲 `[['00bdeb8c', '00bdeb8f']]`
  - `FALL_THROUGH` [`00bdeb8c`](#insn-00bdeb8c) → [`00bdeb90`](#insn-00bdeb90)
- ブロック [`00bdeb90`](#insn-00bdeb90) 範囲 `[['00bdeb90', '00bdebab']]`
  - `FALL_THROUGH` [`00bdeba8`](#insn-00bdeba8) → [`00bdebac`](#insn-00bdebac)
- ブロック [`00bdebac`](#insn-00bdebac) 範囲 `[['00bdebac', '00bdebc3']]`
  - `CONDITIONAL_JUMP` [`00bdebc0`](#insn-00bdebc0) → [`00bdf164`](#insn-00bdf164)
  - `FALL_THROUGH` [`00bdebc0`](#insn-00bdebc0) → [`00bdebc4`](#insn-00bdebc4)
- ブロック [`00bdebc4`](#insn-00bdebc4) 範囲 `[['00bdebc4', '00bdebc7']]`
  - `FALL_THROUGH` [`00bdebc4`](#insn-00bdebc4) → [`00bdebc8`](#insn-00bdebc8)
- ブロック [`00bdebc8`](#insn-00bdebc8) 範囲 `[['00bdebc8', '00bdebcb']]`
  - `CONDITIONAL_JUMP` [`00bdebc8`](#insn-00bdebc8) → [`00bdf164`](#insn-00bdf164)
  - `FALL_THROUGH` [`00bdebc8`](#insn-00bdebc8) → [`00bdebcc`](#insn-00bdebcc)
- ブロック [`00bdebcc`](#insn-00bdebcc) 範囲 `[['00bdebcc', '00bdebcf']]`
  - `FALL_THROUGH` [`00bdebcc`](#insn-00bdebcc) → [`00bdebd0`](#insn-00bdebd0)
- ブロック [`00bdebd0`](#insn-00bdebd0) 範囲 `[['00bdebd0', '00bdebd7']]`
  - `FALL_THROUGH` [`00bdebd4`](#insn-00bdebd4) → [`00bdebd8`](#insn-00bdebd8)
- ブロック [`00bdebd8`](#insn-00bdebd8) 範囲 `[['00bdebd8', '00bdebdb']]`
  - `FALL_THROUGH` [`00bdebd8`](#insn-00bdebd8) → [`00bdebdc`](#insn-00bdebdc)
- ブロック [`00bdebdc`](#insn-00bdebdc) 範囲 `[['00bdebdc', '00bdebf7']]`
  - `CONDITIONAL_JUMP` [`00bdebf4`](#insn-00bdebf4) → [`00bdf164`](#insn-00bdf164)
  - `FALL_THROUGH` [`00bdebf4`](#insn-00bdebf4) → [`00bdebf8`](#insn-00bdebf8)
- ブロック [`00bdebf8`](#insn-00bdebf8) 範囲 `[['00bdebf8', '00bdec27']]`
  - `CONDITIONAL_JUMP` [`00bdec24`](#insn-00bdec24) → [`00bdf154`](#insn-00bdf154)
  - `FALL_THROUGH` [`00bdec24`](#insn-00bdec24) → [`00bdec28`](#insn-00bdec28)
- ブロック [`00bdec28`](#insn-00bdec28) 範囲 `[['00bdec28', '00bdec2f']]`
  - `FALL_THROUGH` [`00bdec2c`](#insn-00bdec2c) → [`00bdec30`](#insn-00bdec30)
- ブロック [`00bdec30`](#insn-00bdec30) 範囲 `[['00bdec30', '00bdec67']]`
  - `FALL_THROUGH` [`00bdec64`](#insn-00bdec64) → [`00bdec68`](#insn-00bdec68)
- ブロック [`00bdec68`](#insn-00bdec68) 範囲 `[['00bdec68', '00bdec73']]`
  - `FALL_THROUGH` [`00bdec70`](#insn-00bdec70) → [`00bdec74`](#insn-00bdec74)
- ブロック [`00bdec74`](#insn-00bdec74) 範囲 `[['00bdec74', '00bdec87']]`
  - `FALL_THROUGH` [`00bdec84`](#insn-00bdec84) → [`00bdec88`](#insn-00bdec88)
- ブロック [`00bdec88`](#insn-00bdec88) 範囲 `[['00bdec88', '00bdec8b']]`
  - `FALL_THROUGH` [`00bdec88`](#insn-00bdec88) → [`00bdec8c`](#insn-00bdec8c)
- ブロック [`00bdec8c`](#insn-00bdec8c) 範囲 `[['00bdec8c', '00bdecc3']]`
  - `FALL_THROUGH` [`00bdecc0`](#insn-00bdecc0) → [`00bdecc4`](#insn-00bdecc4)
- ブロック [`00bdecc4`](#insn-00bdecc4) 範囲 `[['00bdecc4', '00bdecd3']]`
  - `FALL_THROUGH` [`00bdecd0`](#insn-00bdecd0) → [`00bdecd4`](#insn-00bdecd4)
- ブロック [`00bdecd4`](#insn-00bdecd4) 範囲 `[['00bdecd4', '00bdecd7']]`
  - `FALL_THROUGH` [`00bdecd4`](#insn-00bdecd4) → [`00bdecd8`](#insn-00bdecd8)
- ブロック [`00bdecd8`](#insn-00bdecd8) 範囲 `[['00bdecd8', '00bdecf3']]`
  - `FALL_THROUGH` [`00bdecf0`](#insn-00bdecf0) → [`00bdecf4`](#insn-00bdecf4)
- ブロック [`00bdecf4`](#insn-00bdecf4) 範囲 `[['00bdecf4', '00bdecf7']]`
  - `FALL_THROUGH` [`00bdecf4`](#insn-00bdecf4) → [`00bdecf8`](#insn-00bdecf8)
- ブロック [`00bdecf8`](#insn-00bdecf8) 範囲 `[['00bdecf8', '00bded07']]`
  - `FALL_THROUGH` [`00bded04`](#insn-00bded04) → [`00bded08`](#insn-00bded08)
- ブロック [`00bded08`](#insn-00bded08) 範囲 `[['00bded08', '00bded0b']]`
  - `FALL_THROUGH` [`00bded08`](#insn-00bded08) → [`00bded0c`](#insn-00bded0c)
- ブロック [`00bded0c`](#insn-00bded0c) 範囲 `[['00bded0c', '00bded0f']]`
  - `FALL_THROUGH` [`00bded0c`](#insn-00bded0c) → [`00bded10`](#insn-00bded10)
- ブロック [`00bded10`](#insn-00bded10) 範囲 `[['00bded10', '00bded17']]`
  - `FALL_THROUGH` [`00bded14`](#insn-00bded14) → [`00bded18`](#insn-00bded18)
- ブロック [`00bded18`](#insn-00bded18) 範囲 `[['00bded18', '00bded1b']]`
  - `FALL_THROUGH` [`00bded18`](#insn-00bded18) → [`00bded1c`](#insn-00bded1c)
- ブロック [`00bded1c`](#insn-00bded1c) 範囲 `[['00bded1c', '00bded1f']]`
  - `FALL_THROUGH` [`00bded1c`](#insn-00bded1c) → [`00bded20`](#insn-00bded20)
- ブロック [`00bded20`](#insn-00bded20) 範囲 `[['00bded20', '00bded23']]`
  - `CONDITIONAL_JUMP` [`00bded20`](#insn-00bded20) → [`00bded3c`](#insn-00bded3c)
  - `FALL_THROUGH` [`00bded20`](#insn-00bded20) → [`00bded24`](#insn-00bded24)
- ブロック [`00bded24`](#insn-00bded24) 範囲 `[['00bded24', '00bded27']]`
  - `FALL_THROUGH` [`00bded24`](#insn-00bded24) → [`00bded28`](#insn-00bded28)
- ブロック [`00bded28`](#insn-00bded28) 範囲 `[['00bded28', '00bded3b']]`
  - `FALL_THROUGH` [`00bded38`](#insn-00bded38) → [`00bded3c`](#insn-00bded3c)
- ブロック [`00bded3c`](#insn-00bded3c) 範囲 `[['00bded3c', '00bded47']]`
  - `CONDITIONAL_JUMP` [`00bded44`](#insn-00bded44) → [`00bded70`](#insn-00bded70)
  - `FALL_THROUGH` [`00bded44`](#insn-00bded44) → [`00bded48`](#insn-00bded48)
- ブロック [`00bded48`](#insn-00bded48) 範囲 `[['00bded48', '00bded4f']]`
  - `CONDITIONAL_JUMP` [`00bded4c`](#insn-00bded4c) → [`00bded70`](#insn-00bded70)
  - `FALL_THROUGH` [`00bded4c`](#insn-00bded4c) → [`00bded50`](#insn-00bded50)
- ブロック [`00bded50`](#insn-00bded50) 範囲 `[['00bded50', '00bded5f']]`
  - `FALL_THROUGH` [`00bded5c`](#insn-00bded5c) → [`00bded60`](#insn-00bded60)
- ブロック [`00bded60`](#insn-00bded60) 範囲 `[['00bded60', '00bded67']]`
  - `CONDITIONAL_JUMP` [`00bded64`](#insn-00bded64) → [`00bded80`](#insn-00bded80)
  - `FALL_THROUGH` [`00bded64`](#insn-00bded64) → [`00bded68`](#insn-00bded68)
- ブロック [`00bded68`](#insn-00bded68) 範囲 `[['00bded68', '00bded6f']]`
  - `UNCONDITIONAL_JUMP` [`00bded6c`](#insn-00bded6c) → [`00bdeda0`](#insn-00bdeda0)
- ブロック [`00bded70`](#insn-00bded70) 範囲 `[['00bded70', '00bded7f']]`
  - `CONDITIONAL_JUMP` [`00bded7c`](#insn-00bded7c) → [`00bded68`](#insn-00bded68)
  - `FALL_THROUGH` [`00bded7c`](#insn-00bded7c) → [`00bded80`](#insn-00bded80)
- ブロック [`00bded80`](#insn-00bded80) 範囲 `[['00bded80', '00bded93']]`
  - `CONDITIONAL_JUMP` [`00bded90`](#insn-00bded90) → [`00bdeda0`](#insn-00bdeda0)
  - `FALL_THROUGH` [`00bded90`](#insn-00bded90) → [`00bded94`](#insn-00bded94)
- ブロック [`00bded94`](#insn-00bded94) 範囲 `[['00bded94', '00bded97']]`
  - `FALL_THROUGH` [`00bded94`](#insn-00bded94) → [`00bded98`](#insn-00bded98)
- ブロック [`00bded98`](#insn-00bded98) 範囲 `[['00bded98', '00bded9f']]`
  - `FALL_THROUGH` [`00bded9c`](#insn-00bded9c) → [`00bdeda0`](#insn-00bdeda0)
- ブロック [`00bdeda0`](#insn-00bdeda0) 範囲 `[['00bdeda0', '00bdedc3']]`
  - `CONDITIONAL_JUMP` [`00bdedc0`](#insn-00bdedc0) → [`00bdeddc`](#insn-00bdeddc)
  - `FALL_THROUGH` [`00bdedc0`](#insn-00bdedc0) → [`00bdedc4`](#insn-00bdedc4)
- ブロック [`00bdedc4`](#insn-00bdedc4) 範囲 `[['00bdedc4', '00bdedcf']]`
  - `FALL_THROUGH` [`00bdedcc`](#insn-00bdedcc) → [`00bdedd0`](#insn-00bdedd0)
- ブロック [`00bdedd0`](#insn-00bdedd0) 範囲 `[['00bdedd0', '00bdedd3']]`
  - `FALL_THROUGH` [`00bdedd0`](#insn-00bdedd0) → [`00bdedd4`](#insn-00bdedd4)
- ブロック [`00bdedd4`](#insn-00bdedd4) 範囲 `[['00bdedd4', '00bdeddb']]`
  - `FALL_THROUGH` [`00bdedd8`](#insn-00bdedd8) → [`00bdeddc`](#insn-00bdeddc)
- ブロック [`00bdeddc`](#insn-00bdeddc) 範囲 `[['00bdeddc', '00bdede7']]`
  - `CONDITIONAL_JUMP` [`00bdede4`](#insn-00bdede4) → [`00bdee10`](#insn-00bdee10)
  - `FALL_THROUGH` [`00bdede4`](#insn-00bdede4) → [`00bdede8`](#insn-00bdede8)
- ブロック [`00bdede8`](#insn-00bdede8) 範囲 `[['00bdede8', '00bdedef']]`
  - `CONDITIONAL_JUMP` [`00bdedec`](#insn-00bdedec) → [`00bdee10`](#insn-00bdee10)
  - `FALL_THROUGH` [`00bdedec`](#insn-00bdedec) → [`00bdedf0`](#insn-00bdedf0)
- ブロック [`00bdedf0`](#insn-00bdedf0) 範囲 `[['00bdedf0', '00bdee07']]`
  - `CONDITIONAL_JUMP` [`00bdee04`](#insn-00bdee04) → [`00bdee20`](#insn-00bdee20)
  - `FALL_THROUGH` [`00bdee04`](#insn-00bdee04) → [`00bdee08`](#insn-00bdee08)
- ブロック [`00bdee08`](#insn-00bdee08) 範囲 `[['00bdee08', '00bdee0b']]`
  - `FALL_THROUGH` [`00bdee08`](#insn-00bdee08) → [`00bdee0c`](#insn-00bdee0c)
- ブロック [`00bdee0c`](#insn-00bdee0c) 範囲 `[['00bdee0c', '00bdee0f']]`
  - `UNCONDITIONAL_JUMP` [`00bdee0c`](#insn-00bdee0c) → [`00bdee40`](#insn-00bdee40)
- ブロック [`00bdee10`](#insn-00bdee10) 範囲 `[['00bdee10', '00bdee1f']]`
  - `CONDITIONAL_JUMP` [`00bdee1c`](#insn-00bdee1c) → [`00bdee08`](#insn-00bdee08)
  - `FALL_THROUGH` [`00bdee1c`](#insn-00bdee1c) → [`00bdee20`](#insn-00bdee20)
- ブロック [`00bdee20`](#insn-00bdee20) 範囲 `[['00bdee20', '00bdee33']]`
  - `CONDITIONAL_JUMP` [`00bdee30`](#insn-00bdee30) → [`00bdee40`](#insn-00bdee40)
  - `FALL_THROUGH` [`00bdee30`](#insn-00bdee30) → [`00bdee34`](#insn-00bdee34)
- ブロック [`00bdee34`](#insn-00bdee34) 範囲 `[['00bdee34', '00bdee3f']]`
  - `FALL_THROUGH` [`00bdee3c`](#insn-00bdee3c) → [`00bdee40`](#insn-00bdee40)
- ブロック [`00bdee40`](#insn-00bdee40) 範囲 `[['00bdee40', '00bdee67']]`
  - `CONDITIONAL_JUMP` [`00bdee64`](#insn-00bdee64) → [`00bdee80`](#insn-00bdee80)
  - `FALL_THROUGH` [`00bdee64`](#insn-00bdee64) → [`00bdee68`](#insn-00bdee68)
- ブロック [`00bdee68`](#insn-00bdee68) 範囲 `[['00bdee68', '00bdee77']]`
  - `FALL_THROUGH` [`00bdee74`](#insn-00bdee74) → [`00bdee78`](#insn-00bdee78)
- ブロック [`00bdee78`](#insn-00bdee78) 範囲 `[['00bdee78', '00bdee7f']]`
  - `FALL_THROUGH` [`00bdee7c`](#insn-00bdee7c) → [`00bdee80`](#insn-00bdee80)
- ブロック [`00bdee80`](#insn-00bdee80) 範囲 `[['00bdee80', '00bdee87']]`
  - `FALL_THROUGH` [`00bdee84`](#insn-00bdee84) → [`00bdee88`](#insn-00bdee88)
- ブロック [`00bdee88`](#insn-00bdee88) 範囲 `[['00bdee88', '00bdee8b']]`
  - `CONDITIONAL_JUMP` [`00bdee88`](#insn-00bdee88) → [`00bdeeb4`](#insn-00bdeeb4)
  - `FALL_THROUGH` [`00bdee88`](#insn-00bdee88) → [`00bdee8c`](#insn-00bdee8c)
- ブロック [`00bdee8c`](#insn-00bdee8c) 範囲 `[['00bdee8c', '00bdee93']]`
  - `CONDITIONAL_JUMP` [`00bdee90`](#insn-00bdee90) → [`00bdeeb4`](#insn-00bdeeb4)
  - `FALL_THROUGH` [`00bdee90`](#insn-00bdee90) → [`00bdee94`](#insn-00bdee94)
- ブロック [`00bdee94`](#insn-00bdee94) 範囲 `[['00bdee94', '00bdeeab']]`
  - `CONDITIONAL_JUMP` [`00bdeea8`](#insn-00bdeea8) → [`00bdeec4`](#insn-00bdeec4)
  - `FALL_THROUGH` [`00bdeea8`](#insn-00bdeea8) → [`00bdeeac`](#insn-00bdeeac)
- ブロック [`00bdeeac`](#insn-00bdeeac) 範囲 `[['00bdeeac', '00bdeeb3']]`
  - `UNCONDITIONAL_JUMP` [`00bdeeb0`](#insn-00bdeeb0) → [`00bdeee4`](#insn-00bdeee4)
- ブロック [`00bdeeb4`](#insn-00bdeeb4) 範囲 `[['00bdeeb4', '00bdeebf']]`
  - `FALL_THROUGH` [`00bdeebc`](#insn-00bdeebc) → [`00bdeec0`](#insn-00bdeec0)
- ブロック [`00bdeec0`](#insn-00bdeec0) 範囲 `[['00bdeec0', '00bdeec3']]`
  - `CONDITIONAL_JUMP` [`00bdeec0`](#insn-00bdeec0) → [`00bdeeac`](#insn-00bdeeac)
  - `FALL_THROUGH` [`00bdeec0`](#insn-00bdeec0) → [`00bdeec4`](#insn-00bdeec4)
- ブロック [`00bdeec4`](#insn-00bdeec4) 範囲 `[['00bdeec4', '00bdeec7']]`
  - `FALL_THROUGH` [`00bdeec4`](#insn-00bdeec4) → [`00bdeec8`](#insn-00bdeec8)
- ブロック [`00bdeec8`](#insn-00bdeec8) 範囲 `[['00bdeec8', '00bdeecb']]`
  - `FALL_THROUGH` [`00bdeec8`](#insn-00bdeec8) → [`00bdeecc`](#insn-00bdeecc)
- ブロック [`00bdeecc`](#insn-00bdeecc) 範囲 `[['00bdeecc', '00bdeed7']]`
  - `CONDITIONAL_JUMP` [`00bdeed4`](#insn-00bdeed4) → [`00bdeee4`](#insn-00bdeee4)
  - `FALL_THROUGH` [`00bdeed4`](#insn-00bdeed4) → [`00bdeed8`](#insn-00bdeed8)
- ブロック [`00bdeed8`](#insn-00bdeed8) 範囲 `[['00bdeed8', '00bdeee3']]`
  - `FALL_THROUGH` [`00bdeee0`](#insn-00bdeee0) → [`00bdeee4`](#insn-00bdeee4)
- ブロック [`00bdeee4`](#insn-00bdeee4) 範囲 `[['00bdeee4', '00bdeef3']]`
  - `FALL_THROUGH` [`00bdeef0`](#insn-00bdeef0) → [`00bdeef4`](#insn-00bdeef4)
- ブロック [`00bdeef4`](#insn-00bdeef4) 範囲 `[['00bdeef4', '00bdef07']]`
  - `CONDITIONAL_JUMP` [`00bdef04`](#insn-00bdef04) → [`00bdef20`](#insn-00bdef20)
  - `FALL_THROUGH` [`00bdef04`](#insn-00bdef04) → [`00bdef08`](#insn-00bdef08)
- ブロック [`00bdef08`](#insn-00bdef08) 範囲 `[['00bdef08', '00bdef1f']]`
  - `FALL_THROUGH` [`00bdef1c`](#insn-00bdef1c) → [`00bdef20`](#insn-00bdef20)
- ブロック [`00bdef20`](#insn-00bdef20) 範囲 `[['00bdef20', '00bdef2b']]`
  - `CONDITIONAL_JUMP` [`00bdef28`](#insn-00bdef28) → [`00bdef54`](#insn-00bdef54)
  - `FALL_THROUGH` [`00bdef28`](#insn-00bdef28) → [`00bdef2c`](#insn-00bdef2c)
- ブロック [`00bdef2c`](#insn-00bdef2c) 範囲 `[['00bdef2c', '00bdef33']]`
  - `CONDITIONAL_JUMP` [`00bdef30`](#insn-00bdef30) → [`00bdef54`](#insn-00bdef54)
  - `FALL_THROUGH` [`00bdef30`](#insn-00bdef30) → [`00bdef34`](#insn-00bdef34)
- ブロック [`00bdef34`](#insn-00bdef34) 範囲 `[['00bdef34', '00bdef37']]`
  - `FALL_THROUGH` [`00bdef34`](#insn-00bdef34) → [`00bdef38`](#insn-00bdef38)
- ブロック [`00bdef38`](#insn-00bdef38) 範囲 `[['00bdef38', '00bdef4b']]`
  - `CONDITIONAL_JUMP` [`00bdef48`](#insn-00bdef48) → [`00bdef64`](#insn-00bdef64)
  - `FALL_THROUGH` [`00bdef48`](#insn-00bdef48) → [`00bdef4c`](#insn-00bdef4c)
- ブロック [`00bdef4c`](#insn-00bdef4c) 範囲 `[['00bdef4c', '00bdef53']]`
  - `UNCONDITIONAL_JUMP` [`00bdef50`](#insn-00bdef50) → [`00bdef84`](#insn-00bdef84)
- ブロック [`00bdef54`](#insn-00bdef54) 範囲 `[['00bdef54', '00bdef57']]`
  - `FALL_THROUGH` [`00bdef54`](#insn-00bdef54) → [`00bdef58`](#insn-00bdef58)
- ブロック [`00bdef58`](#insn-00bdef58) 範囲 `[['00bdef58', '00bdef63']]`
  - `CONDITIONAL_JUMP` [`00bdef60`](#insn-00bdef60) → [`00bdef4c`](#insn-00bdef4c)
  - `FALL_THROUGH` [`00bdef60`](#insn-00bdef60) → [`00bdef64`](#insn-00bdef64)
- ブロック [`00bdef64`](#insn-00bdef64) 範囲 `[['00bdef64', '00bdef67']]`
  - `FALL_THROUGH` [`00bdef64`](#insn-00bdef64) → [`00bdef68`](#insn-00bdef68)
- ブロック [`00bdef68`](#insn-00bdef68) 範囲 `[['00bdef68', '00bdef6f']]`
  - `FALL_THROUGH` [`00bdef6c`](#insn-00bdef6c) → [`00bdef70`](#insn-00bdef70)
- ブロック [`00bdef70`](#insn-00bdef70) 範囲 `[['00bdef70', '00bdef73']]`
  - `FALL_THROUGH` [`00bdef70`](#insn-00bdef70) → [`00bdef74`](#insn-00bdef74)
- ブロック [`00bdef74`](#insn-00bdef74) 範囲 `[['00bdef74', '00bdef77']]`
  - `CONDITIONAL_JUMP` [`00bdef74`](#insn-00bdef74) → [`00bdef84`](#insn-00bdef84)
  - `FALL_THROUGH` [`00bdef74`](#insn-00bdef74) → [`00bdef78`](#insn-00bdef78)
- ブロック [`00bdef78`](#insn-00bdef78) 範囲 `[['00bdef78', '00bdef7f']]`
  - `FALL_THROUGH` [`00bdef7c`](#insn-00bdef7c) → [`00bdef80`](#insn-00bdef80)
- ブロック [`00bdef80`](#insn-00bdef80) 範囲 `[['00bdef80', '00bdef83']]`
  - `FALL_THROUGH` [`00bdef80`](#insn-00bdef80) → [`00bdef84`](#insn-00bdef84)
- ブロック [`00bdef84`](#insn-00bdef84) 範囲 `[['00bdef84', '00bdefa7']]`
  - `CONDITIONAL_JUMP` [`00bdefa4`](#insn-00bdefa4) → [`00bdefc0`](#insn-00bdefc0)
  - `FALL_THROUGH` [`00bdefa4`](#insn-00bdefa4) → [`00bdefa8`](#insn-00bdefa8)
- ブロック [`00bdefa8`](#insn-00bdefa8) 範囲 `[['00bdefa8', '00bdefbf']]`
  - `FALL_THROUGH` [`00bdefbc`](#insn-00bdefbc) → [`00bdefc0`](#insn-00bdefc0)
- ブロック [`00bdefc0`](#insn-00bdefc0) 範囲 `[['00bdefc0', '00bdefcb']]`
  - `CONDITIONAL_JUMP` [`00bdefc8`](#insn-00bdefc8) → [`00bdeff4`](#insn-00bdeff4)
  - `FALL_THROUGH` [`00bdefc8`](#insn-00bdefc8) → [`00bdefcc`](#insn-00bdefcc)
- ブロック [`00bdefcc`](#insn-00bdefcc) 範囲 `[['00bdefcc', '00bdefcf']]`
  - `FALL_THROUGH` [`00bdefcc`](#insn-00bdefcc) → [`00bdefd0`](#insn-00bdefd0)
- ブロック [`00bdefd0`](#insn-00bdefd0) 範囲 `[['00bdefd0', '00bdefd3']]`
  - `CONDITIONAL_JUMP` [`00bdefd0`](#insn-00bdefd0) → [`00bdeff4`](#insn-00bdeff4)
  - `FALL_THROUGH` [`00bdefd0`](#insn-00bdefd0) → [`00bdefd4`](#insn-00bdefd4)
- ブロック [`00bdefd4`](#insn-00bdefd4) 範囲 `[['00bdefd4', '00bdefe7']]`
  - `FALL_THROUGH` [`00bdefe4`](#insn-00bdefe4) → [`00bdefe8`](#insn-00bdefe8)
- ブロック [`00bdefe8`](#insn-00bdefe8) 範囲 `[['00bdefe8', '00bdefeb']]`
  - `CONDITIONAL_JUMP` [`00bdefe8`](#insn-00bdefe8) → [`00bdf004`](#insn-00bdf004)
  - `FALL_THROUGH` [`00bdefe8`](#insn-00bdefe8) → [`00bdefec`](#insn-00bdefec)
- ブロック [`00bdefec`](#insn-00bdefec) 範囲 `[['00bdefec', '00bdeff3']]`
  - `UNCONDITIONAL_JUMP` [`00bdeff0`](#insn-00bdeff0) → [`00bdf024`](#insn-00bdf024)
- ブロック [`00bdeff4`](#insn-00bdeff4) 範囲 `[['00bdeff4', '00bdf003']]`
  - `CONDITIONAL_JUMP` [`00bdf000`](#insn-00bdf000) → [`00bdefec`](#insn-00bdefec)
  - `FALL_THROUGH` [`00bdf000`](#insn-00bdf000) → [`00bdf004`](#insn-00bdf004)
- ブロック [`00bdf004`](#insn-00bdf004) 範囲 `[['00bdf004', '00bdf00f']]`
  - `FALL_THROUGH` [`00bdf00c`](#insn-00bdf00c) → [`00bdf010`](#insn-00bdf010)
- ブロック [`00bdf010`](#insn-00bdf010) 範囲 `[['00bdf010', '00bdf017']]`
  - `CONDITIONAL_JUMP` [`00bdf014`](#insn-00bdf014) → [`00bdf024`](#insn-00bdf024)
  - `FALL_THROUGH` [`00bdf014`](#insn-00bdf014) → [`00bdf018`](#insn-00bdf018)
- ブロック [`00bdf018`](#insn-00bdf018) 範囲 `[['00bdf018', '00bdf023']]`
  - `FALL_THROUGH` [`00bdf020`](#insn-00bdf020) → [`00bdf024`](#insn-00bdf024)
- ブロック [`00bdf024`](#insn-00bdf024) 範囲 `[['00bdf024', '00bdf027']]`
  - `FALL_THROUGH` [`00bdf024`](#insn-00bdf024) → [`00bdf028`](#insn-00bdf028)
- ブロック [`00bdf028`](#insn-00bdf028) 範囲 `[['00bdf028', '00bdf02b']]`
  - `FALL_THROUGH` [`00bdf028`](#insn-00bdf028) → [`00bdf02c`](#insn-00bdf02c)
- ブロック [`00bdf02c`](#insn-00bdf02c) 範囲 `[['00bdf02c', '00bdf02f']]`
  - `FALL_THROUGH` [`00bdf02c`](#insn-00bdf02c) → [`00bdf030`](#insn-00bdf030)
- ブロック [`00bdf030`](#insn-00bdf030) 範囲 `[['00bdf030', '00bdf033']]`
  - `FALL_THROUGH` [`00bdf030`](#insn-00bdf030) → [`00bdf034`](#insn-00bdf034)
- ブロック [`00bdf034`](#insn-00bdf034) 範囲 `[['00bdf034', '00bdf037']]`
  - `FALL_THROUGH` [`00bdf034`](#insn-00bdf034) → [`00bdf038`](#insn-00bdf038)
- ブロック [`00bdf038`](#insn-00bdf038) 範囲 `[['00bdf038', '00bdf03b']]`
  - `FALL_THROUGH` [`00bdf038`](#insn-00bdf038) → [`00bdf03c`](#insn-00bdf03c)
- ブロック [`00bdf03c`](#insn-00bdf03c) 範囲 `[['00bdf03c', '00bdf047']]`
  - `CONDITIONAL_JUMP` [`00bdf044`](#insn-00bdf044) → [`00bdf060`](#insn-00bdf060)
  - `FALL_THROUGH` [`00bdf044`](#insn-00bdf044) → [`00bdf048`](#insn-00bdf048)
- ブロック [`00bdf048`](#insn-00bdf048) 範囲 `[['00bdf048', '00bdf04b']]`
  - `FALL_THROUGH` [`00bdf048`](#insn-00bdf048) → [`00bdf04c`](#insn-00bdf04c)
- ブロック [`00bdf04c`](#insn-00bdf04c) 範囲 `[['00bdf04c', '00bdf04f']]`
  - `FALL_THROUGH` [`00bdf04c`](#insn-00bdf04c) → [`00bdf050`](#insn-00bdf050)
- ブロック [`00bdf050`](#insn-00bdf050) 範囲 `[['00bdf050', '00bdf053']]`
  - `FALL_THROUGH` [`00bdf050`](#insn-00bdf050) → [`00bdf054`](#insn-00bdf054)
- ブロック [`00bdf054`](#insn-00bdf054) 範囲 `[['00bdf054', '00bdf057']]`
  - `FALL_THROUGH` [`00bdf054`](#insn-00bdf054) → [`00bdf058`](#insn-00bdf058)
- ブロック [`00bdf058`](#insn-00bdf058) 範囲 `[['00bdf058', '00bdf05b']]`
  - `FALL_THROUGH` [`00bdf058`](#insn-00bdf058) → [`00bdf05c`](#insn-00bdf05c)
- ブロック [`00bdf05c`](#insn-00bdf05c) 範囲 `[['00bdf05c', '00bdf05f']]`
  - `FALL_THROUGH` [`00bdf05c`](#insn-00bdf05c) → [`00bdf060`](#insn-00bdf060)
- ブロック [`00bdf060`](#insn-00bdf060) 範囲 `[['00bdf060', '00bdf06b']]`
  - `CONDITIONAL_JUMP` [`00bdf068`](#insn-00bdf068) → [`00bdf094`](#insn-00bdf094)
  - `FALL_THROUGH` [`00bdf068`](#insn-00bdf068) → [`00bdf06c`](#insn-00bdf06c)
- ブロック [`00bdf06c`](#insn-00bdf06c) 範囲 `[['00bdf06c', '00bdf073']]`
  - `CONDITIONAL_JUMP` [`00bdf070`](#insn-00bdf070) → [`00bdf094`](#insn-00bdf094)
  - `FALL_THROUGH` [`00bdf070`](#insn-00bdf070) → [`00bdf074`](#insn-00bdf074)
- ブロック [`00bdf074`](#insn-00bdf074) 範囲 `[['00bdf074', '00bdf08b']]`
  - `CONDITIONAL_JUMP` [`00bdf088`](#insn-00bdf088) → [`00bdf0a4`](#insn-00bdf0a4)
  - `FALL_THROUGH` [`00bdf088`](#insn-00bdf088) → [`00bdf08c`](#insn-00bdf08c)
- ブロック [`00bdf08c`](#insn-00bdf08c) 範囲 `[['00bdf08c', '00bdf093']]`
  - `UNCONDITIONAL_JUMP` [`00bdf090`](#insn-00bdf090) → [`00bdf0c4`](#insn-00bdf0c4)
- ブロック [`00bdf094`](#insn-00bdf094) 範囲 `[['00bdf094', '00bdf0a3']]`
  - `CONDITIONAL_JUMP` [`00bdf0a0`](#insn-00bdf0a0) → [`00bdf08c`](#insn-00bdf08c)
  - `FALL_THROUGH` [`00bdf0a0`](#insn-00bdf0a0) → [`00bdf0a4`](#insn-00bdf0a4)
- ブロック [`00bdf0a4`](#insn-00bdf0a4) 範囲 `[['00bdf0a4', '00bdf0b7']]`
  - `CONDITIONAL_JUMP` [`00bdf0b4`](#insn-00bdf0b4) → [`00bdf0c4`](#insn-00bdf0c4)
  - `FALL_THROUGH` [`00bdf0b4`](#insn-00bdf0b4) → [`00bdf0b8`](#insn-00bdf0b8)
- ブロック [`00bdf0b8`](#insn-00bdf0b8) 範囲 `[['00bdf0b8', '00bdf0c3']]`
  - `FALL_THROUGH` [`00bdf0c0`](#insn-00bdf0c0) → [`00bdf0c4`](#insn-00bdf0c4)
- ブロック [`00bdf0c4`](#insn-00bdf0c4) 範囲 `[['00bdf0c4', '00bdf0df']]`
  - `CONDITIONAL_JUMP` [`00bdf0dc`](#insn-00bdf0dc) → [`00bdf0f8`](#insn-00bdf0f8)
  - `FALL_THROUGH` [`00bdf0dc`](#insn-00bdf0dc) → [`00bdf0e0`](#insn-00bdf0e0)
- ブロック [`00bdf0e0`](#insn-00bdf0e0) 範囲 `[['00bdf0e0', '00bdf0f7']]`
  - `UNCONDITIONAL_JUMP` [`00bdf0f4`](#insn-00bdf0f4) → [`00bdf104`](#insn-00bdf104)
- ブロック [`00bdf0f8`](#insn-00bdf0f8) 範囲 `[['00bdf0f8', '00bdf103']]`
  - `FALL_THROUGH` [`00bdf100`](#insn-00bdf100) → [`00bdf104`](#insn-00bdf104)
- ブロック [`00bdf104`](#insn-00bdf104) 範囲 `[['00bdf104', '00bdf153']]`
  - `CONDITIONAL_JUMP` [`00bdf150`](#insn-00bdf150) → [`00bdec74`](#insn-00bdec74)
  - `FALL_THROUGH` [`00bdf150`](#insn-00bdf150) → [`00bdf154`](#insn-00bdf154)
- ブロック [`00bdf154`](#insn-00bdf154) 範囲 `[['00bdf154', '00bdf163']]`
  - `FALL_THROUGH` [`00bdf160`](#insn-00bdf160) → [`00bdf164`](#insn-00bdf164)
- ブロック [`00bdf164`](#insn-00bdf164) 範囲 `[['00bdf164', '00bdf177']]`
  - `CONDITIONAL_JUMP` [`00bdf174`](#insn-00bdf174) → [`00bdf198`](#insn-00bdf198)
  - `FALL_THROUGH` [`00bdf174`](#insn-00bdf174) → [`00bdf178`](#insn-00bdf178)
- ブロック [`00bdf178`](#insn-00bdf178) 範囲 `[['00bdf178', '00bdf197']]`
- ブロック [`00bdf198`](#insn-00bdf198) 範囲 `[['00bdf198', '00bdf19b']]`

## 命令位置別の参照

- [`00bdeb7c`](#insn-00bdeb7c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb80`](#insn-00bdeb80) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb84`](#insn-00bdeb84) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb88`](#insn-00bdeb88) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb8c`](#insn-00bdeb8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeb90`](#insn-00bdeb90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeba4`](#insn-00bdeba4) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebac`](#insn-00bdebac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebbc`](#insn-00bdebbc) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebc0`](#insn-00bdebc0) → [`00bdf164`](#insn-00bdf164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebc8`](#insn-00bdebc8) → [`00bdf164`](#insn-00bdf164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebd0`](#insn-00bdebd0) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdebd4`](#insn-00bdebd4) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebdc`](#insn-00bdebdc) → `01126d40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdebe8`](#insn-00bdebe8) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebec`](#insn-00bdebec) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdebf0`](#insn-00bdebf0) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebf4`](#insn-00bdebf4) → [`00bdf164`](#insn-00bdf164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdebfc`](#insn-00bdebfc) → [`00c5b520`](../00c5b/00c5b520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b520` · 推定シンボル `None` · 推定型 `None`
- [`00bdec04`](#insn-00bdec04) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec08`](#insn-00bdec08) → [`005762b8`](../00576/005762b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005762b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdec18`](#insn-00bdec18) → [`00c5ded0`](../00c5d/00c5ded0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ded0` · 推定シンボル `None` · 推定型 `None`
- [`00bdec20`](#insn-00bdec20) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec24`](#insn-00bdec24) → [`00bdf154`](#insn-00bdf154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec2c`](#insn-00bdec2c) → `00c9ba60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdec34`](#insn-00bdec34) → `00c9b9c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdec48`](#insn-00bdec48) → `Stack[-0x200]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec68`](#insn-00bdec68) → `00c92910`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdec68`](#insn-00bdec68) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec70`](#insn-00bdec70) → `00c92978`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdec70`](#insn-00bdec70) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec78`](#insn-00bdec78) → [`00c5b520`](../00c5b/00c5b520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b520` · 推定シンボル `None` · 推定型 `None`
- [`00bdec80`](#insn-00bdec80) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec88`](#insn-00bdec88) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdec8c`](#insn-00bdec8c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdec90`](#insn-00bdec90) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeca0`](#insn-00bdeca0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeca4`](#insn-00bdeca4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeca8`](#insn-00bdeca8) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecac`](#insn-00bdecac) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecb0`](#insn-00bdecb0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecb4`](#insn-00bdecb4) → `00c92910`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdecb4`](#insn-00bdecb4) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecb8`](#insn-00bdecb8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecc0`](#insn-00bdecc0) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdecd8`](#insn-00bdecd8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecf0`](#insn-00bdecf0) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecf8`](#insn-00bdecf8) → `00c92978`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdecf8`](#insn-00bdecf8) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdecfc`](#insn-00bdecfc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded00`](#insn-00bded00) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded04`](#insn-00bded04) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded08`](#insn-00bded08) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded0c`](#insn-00bded0c) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded10`](#insn-00bded10) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded18`](#insn-00bded18) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bded20`](#insn-00bded20) → [`00bded3c`](#insn-00bded3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded28`](#insn-00bded28) → `01126dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bded34`](#insn-00bded34) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bded40`](#insn-00bded40) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bded44`](#insn-00bded44) → [`00bded70`](#insn-00bded70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded4c`](#insn-00bded4c) → [`00bded70`](#insn-00bded70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded5c`](#insn-00bded5c) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bded60`](#insn-00bded60) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded64`](#insn-00bded64) → [`00bded80`](#insn-00bded80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded68`](#insn-00bded68) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded6c`](#insn-00bded6c) → [`00bdeda0`](#insn-00bdeda0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded70`](#insn-00bded70) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded74`](#insn-00bded74) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded78`](#insn-00bded78) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded7c`](#insn-00bded7c) → [`00bded68`](#insn-00bded68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded80`](#insn-00bded80) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded88`](#insn-00bded88) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded8c`](#insn-00bded8c) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded90`](#insn-00bded90) → [`00bdeda0`](#insn-00bdeda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded94`](#insn-00bded94) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bded98`](#insn-00bded98) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bded9c`](#insn-00bded9c) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeda0`](#insn-00bdeda0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeda4`](#insn-00bdeda4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeda8`](#insn-00bdeda8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedac`](#insn-00bdedac) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedb0`](#insn-00bdedb0) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedb8`](#insn-00bdedb8) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdedc0`](#insn-00bdedc0) → [`00bdeddc`](#insn-00bdeddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedc8`](#insn-00bdedc8) → `01126de8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdedd4`](#insn-00bdedd4) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdede0`](#insn-00bdede0) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdede4`](#insn-00bdede4) → [`00bdee10`](#insn-00bdee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedec`](#insn-00bdedec) → [`00bdee10`](#insn-00bdee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdedfc`](#insn-00bdedfc) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bdee00`](#insn-00bdee00) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee04`](#insn-00bdee04) → [`00bdee20`](#insn-00bdee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee08`](#insn-00bdee08) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee0c`](#insn-00bdee0c) → [`00bdee40`](#insn-00bdee40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee10`](#insn-00bdee10) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee14`](#insn-00bdee14) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee18`](#insn-00bdee18) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee1c`](#insn-00bdee1c) → [`00bdee08`](#insn-00bdee08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee20`](#insn-00bdee20) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee28`](#insn-00bdee28) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee2c`](#insn-00bdee2c) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee30`](#insn-00bdee30) → [`00bdee40`](#insn-00bdee40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee34`](#insn-00bdee34) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee38`](#insn-00bdee38) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdee3c`](#insn-00bdee3c) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee40`](#insn-00bdee40) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee44`](#insn-00bdee44) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee48`](#insn-00bdee48) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee4c`](#insn-00bdee4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee50`](#insn-00bdee50) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee54`](#insn-00bdee54) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee5c`](#insn-00bdee5c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdee64`](#insn-00bdee64) → [`00bdee80`](#insn-00bdee80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee6c`](#insn-00bdee6c) → `01126dd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdee78`](#insn-00bdee78) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdee84`](#insn-00bdee84) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdee88`](#insn-00bdee88) → [`00bdeeb4`](#insn-00bdeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdee90`](#insn-00bdee90) → [`00bdeeb4`](#insn-00bdeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeea0`](#insn-00bdeea0) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bdeea4`](#insn-00bdeea4) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeea8`](#insn-00bdeea8) → [`00bdeec4`](#insn-00bdeec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeeac`](#insn-00bdeeac) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeeb0`](#insn-00bdeeb0) → [`00bdeee4`](#insn-00bdeee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeeb4`](#insn-00bdeeb4) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeeb8`](#insn-00bdeeb8) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeebc`](#insn-00bdeebc) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeec0`](#insn-00bdeec0) → [`00bdeeac`](#insn-00bdeeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeec4`](#insn-00bdeec4) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeecc`](#insn-00bdeecc) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeed0`](#insn-00bdeed0) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeed4`](#insn-00bdeed4) → [`00bdeee4`](#insn-00bdeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeed8`](#insn-00bdeed8) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeedc`](#insn-00bdeedc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdeee0`](#insn-00bdeee0) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeee4`](#insn-00bdeee4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeee8`](#insn-00bdeee8) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeeec`](#insn-00bdeeec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeef0`](#insn-00bdeef0) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeef4`](#insn-00bdeef4) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeefc`](#insn-00bdeefc) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdef04`](#insn-00bdef04) → [`00bdef20`](#insn-00bdef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef0c`](#insn-00bdef0c) → `01126de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdef18`](#insn-00bdef18) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdef24`](#insn-00bdef24) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdef28`](#insn-00bdef28) → [`00bdef54`](#insn-00bdef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef30`](#insn-00bdef30) → [`00bdef54`](#insn-00bdef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef40`](#insn-00bdef40) → [`00c5b2f0`](../00c5b/00c5b2f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b2f0` · 推定シンボル `None` · 推定型 `None`
- [`00bdef44`](#insn-00bdef44) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef48`](#insn-00bdef48) → [`00bdef64`](#insn-00bdef64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef4c`](#insn-00bdef4c) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef50`](#insn-00bdef50) → [`00bdef84`](#insn-00bdef84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef54`](#insn-00bdef54) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef58`](#insn-00bdef58) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef5c`](#insn-00bdef5c) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef60`](#insn-00bdef60) → [`00bdef4c`](#insn-00bdef4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef64`](#insn-00bdef64) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef6c`](#insn-00bdef6c) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef70`](#insn-00bdef70) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef74`](#insn-00bdef74) → [`00bdef84`](#insn-00bdef84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef78`](#insn-00bdef78) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef7c`](#insn-00bdef7c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdef80`](#insn-00bdef80) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef84`](#insn-00bdef84) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef88`](#insn-00bdef88) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef8c`](#insn-00bdef8c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef90`](#insn-00bdef90) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef94`](#insn-00bdef94) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdef9c`](#insn-00bdef9c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdefa4`](#insn-00bdefa4) → [`00bdefc0`](#insn-00bdefc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefac`](#insn-00bdefac) → `01126dc8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdefb8`](#insn-00bdefb8) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdefc4`](#insn-00bdefc4) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdefc8`](#insn-00bdefc8) → [`00bdeff4`](#insn-00bdeff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefd0`](#insn-00bdefd0) → [`00bdeff4`](#insn-00bdeff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefe0`](#insn-00bdefe0) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bdefe4`](#insn-00bdefe4) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefe8`](#insn-00bdefe8) → [`00bdf004`](#insn-00bdf004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdefec`](#insn-00bdefec) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff0`](#insn-00bdeff0) → [`00bdf024`](#insn-00bdf024) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff4`](#insn-00bdeff4) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeff8`](#insn-00bdeff8) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdeffc`](#insn-00bdeffc) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf000`](#insn-00bdf000) → [`00bdefec`](#insn-00bdefec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf004`](#insn-00bdf004) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf00c`](#insn-00bdf00c) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf010`](#insn-00bdf010) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf014`](#insn-00bdf014) → [`00bdf024`](#insn-00bdf024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf018`](#insn-00bdf018) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf01c`](#insn-00bdf01c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf020`](#insn-00bdf020) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf024`](#insn-00bdf024) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf028`](#insn-00bdf028) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf02c`](#insn-00bdf02c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf030`](#insn-00bdf030) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf034`](#insn-00bdf034) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf03c`](#insn-00bdf03c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdf044`](#insn-00bdf044) → [`00bdf060`](#insn-00bdf060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf04c`](#insn-00bdf04c) → `01126dd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf058`](#insn-00bdf058) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bdf064`](#insn-00bdf064) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf068`](#insn-00bdf068) → [`00bdf094`](#insn-00bdf094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf070`](#insn-00bdf070) → [`00bdf094`](#insn-00bdf094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf080`](#insn-00bdf080) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bdf084`](#insn-00bdf084) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf088`](#insn-00bdf088) → [`00bdf0a4`](#insn-00bdf0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf08c`](#insn-00bdf08c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf090`](#insn-00bdf090) → [`00bdf0c4`](#insn-00bdf0c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf094`](#insn-00bdf094) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf098`](#insn-00bdf098) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf09c`](#insn-00bdf09c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0a0`](#insn-00bdf0a0) → [`00bdf08c`](#insn-00bdf08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0a4`](#insn-00bdf0a4) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0ac`](#insn-00bdf0ac) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0b0`](#insn-00bdf0b0) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0b4`](#insn-00bdf0b4) → [`00bdf0c4`](#insn-00bdf0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0b8`](#insn-00bdf0b8) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0bc`](#insn-00bdf0bc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0c0`](#insn-00bdf0c0) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0c8`](#insn-00bdf0c8) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0cc`](#insn-00bdf0cc) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0d4`](#insn-00bdf0d4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0d8`](#insn-00bdf0d8) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0dc`](#insn-00bdf0dc) → [`00bdf0f8`](#insn-00bdf0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0e8`](#insn-00bdf0e8) → [`00c5dea0`](../00c5d/00c5dea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dea0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf0f4`](#insn-00bdf0f4) → [`00bdf104`](#insn-00bdf104) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf100`](#insn-00bdf100) → [`00c5dec0`](../00c5d/00c5dec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dec0` · 推定シンボル `None` · 推定型 `None`
- [`00bdf108`](#insn-00bdf108) → [`00c5db70`](../00c5d/00c5db70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db70` · 推定シンボル `None` · 推定型 `None`
- [`00bdf110`](#insn-00bdf110) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf114`](#insn-00bdf114) → `00c9ba60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdf11c`](#insn-00bdf11c) → `00c92910`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdf11c`](#insn-00bdf11c) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf124`](#insn-00bdf124) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdf12c`](#insn-00bdf12c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf13c`](#insn-00bdf13c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf140`](#insn-00bdf140) → [`00c5db80`](../00c5d/00c5db80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db80` · 推定シンボル `None` · 推定型 `None`
- [`00bdf144`](#insn-00bdf144) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf150`](#insn-00bdf150) → [`00bdec74`](#insn-00bdec74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf154`](#insn-00bdf154) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf164`](#insn-00bdf164) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf16c`](#insn-00bdf16c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf174`](#insn-00bdf174) → [`00bdf198`](#insn-00bdf198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf17c`](#insn-00bdf17c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf180`](#insn-00bdf180) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf184`](#insn-00bdf184) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf188`](#insn-00bdf188) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf18c`](#insn-00bdf18c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf198`](#insn-00bdf198) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeb7c`](#insn-00bdeb7c)

~~~json
{
  "source": "00bdeb7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb80`](#insn-00bdeb80)

~~~json
{
  "source": "00bdeb80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb84`](#insn-00bdeb84)

~~~json
{
  "source": "00bdeb84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb88`](#insn-00bdeb88)

~~~json
{
  "source": "00bdeb88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb8c`](#insn-00bdeb8c)

~~~json
{
  "source": "00bdeb8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeb90`](#insn-00bdeb90)

~~~json
{
  "source": "00bdeb90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeba4`](#insn-00bdeba4)

~~~json
{
  "source": "00bdeba4",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebac`](#insn-00bdebac)

~~~json
{
  "source": "00bdebac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebbc`](#insn-00bdebbc)

~~~json
{
  "source": "00bdebbc",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebc0`](#insn-00bdebc0)

~~~json
{
  "source": "00bdebc0",
  "target": "00bdf164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebc8`](#insn-00bdebc8)

~~~json
{
  "source": "00bdebc8",
  "target": "00bdf164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebd0`](#insn-00bdebd0)

~~~json
{
  "source": "00bdebd0",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdebd4`](#insn-00bdebd4)

~~~json
{
  "source": "00bdebd4",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebdc`](#insn-00bdebdc)

~~~json
{
  "source": "00bdebdc",
  "target": "01126d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdebe8`](#insn-00bdebe8)

~~~json
{
  "source": "00bdebe8",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebec`](#insn-00bdebec)

~~~json
{
  "source": "00bdebec",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdebf0`](#insn-00bdebf0)

~~~json
{
  "source": "00bdebf0",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebf4`](#insn-00bdebf4)

~~~json
{
  "source": "00bdebf4",
  "target": "00bdf164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdebfc`](#insn-00bdebfc)

~~~json
{
  "source": "00bdebfc",
  "target": "00c5b520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdec04`](#insn-00bdec04)

~~~json
{
  "source": "00bdec04",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec08`](#insn-00bdec08)

~~~json
{
  "source": "00bdec08",
  "target": "005762b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdec18`](#insn-00bdec18)

~~~json
{
  "source": "00bdec18",
  "target": "00c5ded0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdec20`](#insn-00bdec20)

~~~json
{
  "source": "00bdec20",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec24`](#insn-00bdec24)

~~~json
{
  "source": "00bdec24",
  "target": "00bdf154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec2c`](#insn-00bdec2c)

~~~json
{
  "source": "00bdec2c",
  "target": "00c9ba60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdec34`](#insn-00bdec34)

~~~json
{
  "source": "00bdec34",
  "target": "00c9b9c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b9c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdec48`](#insn-00bdec48)

~~~json
{
  "source": "00bdec48",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec68`](#insn-00bdec68)

~~~json
{
  "source": "00bdec68",
  "target": "00c92910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92900",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdec68`](#insn-00bdec68)

~~~json
{
  "source": "00bdec68",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec70`](#insn-00bdec70)

~~~json
{
  "source": "00bdec70",
  "target": "00c92978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92968",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdec70`](#insn-00bdec70)

~~~json
{
  "source": "00bdec70",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec78`](#insn-00bdec78)

~~~json
{
  "source": "00bdec78",
  "target": "00c5b520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdec80`](#insn-00bdec80)

~~~json
{
  "source": "00bdec80",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec88`](#insn-00bdec88)

~~~json
{
  "source": "00bdec88",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdec8c`](#insn-00bdec8c)

~~~json
{
  "source": "00bdec8c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdec90`](#insn-00bdec90)

~~~json
{
  "source": "00bdec90",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeca0`](#insn-00bdeca0)

~~~json
{
  "source": "00bdeca0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeca4`](#insn-00bdeca4)

~~~json
{
  "source": "00bdeca4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeca8`](#insn-00bdeca8)

~~~json
{
  "source": "00bdeca8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecac`](#insn-00bdecac)

~~~json
{
  "source": "00bdecac",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecb0`](#insn-00bdecb0)

~~~json
{
  "source": "00bdecb0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecb4`](#insn-00bdecb4)

~~~json
{
  "source": "00bdecb4",
  "target": "00c92910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92900",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdecb4`](#insn-00bdecb4)

~~~json
{
  "source": "00bdecb4",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecb8`](#insn-00bdecb8)

~~~json
{
  "source": "00bdecb8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecc0`](#insn-00bdecc0)

~~~json
{
  "source": "00bdecc0",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdecd8`](#insn-00bdecd8)

~~~json
{
  "source": "00bdecd8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecf0`](#insn-00bdecf0)

~~~json
{
  "source": "00bdecf0",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecf8`](#insn-00bdecf8)

~~~json
{
  "source": "00bdecf8",
  "target": "00c92978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92968",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdecf8`](#insn-00bdecf8)

~~~json
{
  "source": "00bdecf8",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdecfc`](#insn-00bdecfc)

~~~json
{
  "source": "00bdecfc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded00`](#insn-00bded00)

~~~json
{
  "source": "00bded00",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded04`](#insn-00bded04)

~~~json
{
  "source": "00bded04",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded08`](#insn-00bded08)

~~~json
{
  "source": "00bded08",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded0c`](#insn-00bded0c)

~~~json
{
  "source": "00bded0c",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded10`](#insn-00bded10)

~~~json
{
  "source": "00bded10",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded18`](#insn-00bded18)

~~~json
{
  "source": "00bded18",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded20`](#insn-00bded20)

~~~json
{
  "source": "00bded20",
  "target": "00bded3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded28`](#insn-00bded28)

~~~json
{
  "source": "00bded28",
  "target": "01126dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bded34`](#insn-00bded34)

~~~json
{
  "source": "00bded34",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded40`](#insn-00bded40)

~~~json
{
  "source": "00bded40",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded44`](#insn-00bded44)

~~~json
{
  "source": "00bded44",
  "target": "00bded70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded4c`](#insn-00bded4c)

~~~json
{
  "source": "00bded4c",
  "target": "00bded70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded5c`](#insn-00bded5c)

~~~json
{
  "source": "00bded5c",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded60`](#insn-00bded60)

~~~json
{
  "source": "00bded60",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded64`](#insn-00bded64)

~~~json
{
  "source": "00bded64",
  "target": "00bded80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded68`](#insn-00bded68)

~~~json
{
  "source": "00bded68",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded6c`](#insn-00bded6c)

~~~json
{
  "source": "00bded6c",
  "target": "00bdeda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded70`](#insn-00bded70)

~~~json
{
  "source": "00bded70",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded74`](#insn-00bded74)

~~~json
{
  "source": "00bded74",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded78`](#insn-00bded78)

~~~json
{
  "source": "00bded78",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded7c`](#insn-00bded7c)

~~~json
{
  "source": "00bded7c",
  "target": "00bded68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded80`](#insn-00bded80)

~~~json
{
  "source": "00bded80",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded88`](#insn-00bded88)

~~~json
{
  "source": "00bded88",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded8c`](#insn-00bded8c)

~~~json
{
  "source": "00bded8c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded90`](#insn-00bded90)

~~~json
{
  "source": "00bded90",
  "target": "00bdeda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded94`](#insn-00bded94)

~~~json
{
  "source": "00bded94",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bded98`](#insn-00bded98)

~~~json
{
  "source": "00bded98",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bded9c`](#insn-00bded9c)

~~~json
{
  "source": "00bded9c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeda0`](#insn-00bdeda0)

~~~json
{
  "source": "00bdeda0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeda4`](#insn-00bdeda4)

~~~json
{
  "source": "00bdeda4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeda8`](#insn-00bdeda8)

~~~json
{
  "source": "00bdeda8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedac`](#insn-00bdedac)

~~~json
{
  "source": "00bdedac",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedb0`](#insn-00bdedb0)

~~~json
{
  "source": "00bdedb0",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedb8`](#insn-00bdedb8)

~~~json
{
  "source": "00bdedb8",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdedc0`](#insn-00bdedc0)

~~~json
{
  "source": "00bdedc0",
  "target": "00bdeddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedc8`](#insn-00bdedc8)

~~~json
{
  "source": "00bdedc8",
  "target": "01126de8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126de8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdedd4`](#insn-00bdedd4)

~~~json
{
  "source": "00bdedd4",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdede0`](#insn-00bdede0)

~~~json
{
  "source": "00bdede0",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdede4`](#insn-00bdede4)

~~~json
{
  "source": "00bdede4",
  "target": "00bdee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedec`](#insn-00bdedec)

~~~json
{
  "source": "00bdedec",
  "target": "00bdee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdedfc`](#insn-00bdedfc)

~~~json
{
  "source": "00bdedfc",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdee00`](#insn-00bdee00)

~~~json
{
  "source": "00bdee00",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee04`](#insn-00bdee04)

~~~json
{
  "source": "00bdee04",
  "target": "00bdee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee08`](#insn-00bdee08)

~~~json
{
  "source": "00bdee08",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee0c`](#insn-00bdee0c)

~~~json
{
  "source": "00bdee0c",
  "target": "00bdee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee10`](#insn-00bdee10)

~~~json
{
  "source": "00bdee10",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee14`](#insn-00bdee14)

~~~json
{
  "source": "00bdee14",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee18`](#insn-00bdee18)

~~~json
{
  "source": "00bdee18",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee1c`](#insn-00bdee1c)

~~~json
{
  "source": "00bdee1c",
  "target": "00bdee08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee20`](#insn-00bdee20)

~~~json
{
  "source": "00bdee20",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee28`](#insn-00bdee28)

~~~json
{
  "source": "00bdee28",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee2c`](#insn-00bdee2c)

~~~json
{
  "source": "00bdee2c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee30`](#insn-00bdee30)

~~~json
{
  "source": "00bdee30",
  "target": "00bdee40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee34`](#insn-00bdee34)

~~~json
{
  "source": "00bdee34",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee38`](#insn-00bdee38)

~~~json
{
  "source": "00bdee38",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdee3c`](#insn-00bdee3c)

~~~json
{
  "source": "00bdee3c",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee40`](#insn-00bdee40)

~~~json
{
  "source": "00bdee40",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee44`](#insn-00bdee44)

~~~json
{
  "source": "00bdee44",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee48`](#insn-00bdee48)

~~~json
{
  "source": "00bdee48",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee4c`](#insn-00bdee4c)

~~~json
{
  "source": "00bdee4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee50`](#insn-00bdee50)

~~~json
{
  "source": "00bdee50",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee54`](#insn-00bdee54)

~~~json
{
  "source": "00bdee54",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee5c`](#insn-00bdee5c)

~~~json
{
  "source": "00bdee5c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdee64`](#insn-00bdee64)

~~~json
{
  "source": "00bdee64",
  "target": "00bdee80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee6c`](#insn-00bdee6c)

~~~json
{
  "source": "00bdee6c",
  "target": "01126dd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdee78`](#insn-00bdee78)

~~~json
{
  "source": "00bdee78",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdee84`](#insn-00bdee84)

~~~json
{
  "source": "00bdee84",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdee88`](#insn-00bdee88)

~~~json
{
  "source": "00bdee88",
  "target": "00bdeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdee90`](#insn-00bdee90)

~~~json
{
  "source": "00bdee90",
  "target": "00bdeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeea0`](#insn-00bdeea0)

~~~json
{
  "source": "00bdeea0",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeea4`](#insn-00bdeea4)

~~~json
{
  "source": "00bdeea4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeea8`](#insn-00bdeea8)

~~~json
{
  "source": "00bdeea8",
  "target": "00bdeec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeeac`](#insn-00bdeeac)

~~~json
{
  "source": "00bdeeac",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeeb0`](#insn-00bdeeb0)

~~~json
{
  "source": "00bdeeb0",
  "target": "00bdeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeeb4`](#insn-00bdeeb4)

~~~json
{
  "source": "00bdeeb4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeeb8`](#insn-00bdeeb8)

~~~json
{
  "source": "00bdeeb8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeebc`](#insn-00bdeebc)

~~~json
{
  "source": "00bdeebc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeec0`](#insn-00bdeec0)

~~~json
{
  "source": "00bdeec0",
  "target": "00bdeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeec4`](#insn-00bdeec4)

~~~json
{
  "source": "00bdeec4",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeecc`](#insn-00bdeecc)

~~~json
{
  "source": "00bdeecc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeed0`](#insn-00bdeed0)

~~~json
{
  "source": "00bdeed0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeed4`](#insn-00bdeed4)

~~~json
{
  "source": "00bdeed4",
  "target": "00bdeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeed8`](#insn-00bdeed8)

~~~json
{
  "source": "00bdeed8",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeedc`](#insn-00bdeedc)

~~~json
{
  "source": "00bdeedc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdeee0`](#insn-00bdeee0)

~~~json
{
  "source": "00bdeee0",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeee4`](#insn-00bdeee4)

~~~json
{
  "source": "00bdeee4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeee8`](#insn-00bdeee8)

~~~json
{
  "source": "00bdeee8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeeec`](#insn-00bdeeec)

~~~json
{
  "source": "00bdeeec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeef0`](#insn-00bdeef0)

~~~json
{
  "source": "00bdeef0",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeef4`](#insn-00bdeef4)

~~~json
{
  "source": "00bdeef4",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeefc`](#insn-00bdeefc)

~~~json
{
  "source": "00bdeefc",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef04`](#insn-00bdef04)

~~~json
{
  "source": "00bdef04",
  "target": "00bdef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef0c`](#insn-00bdef0c)

~~~json
{
  "source": "00bdef0c",
  "target": "01126de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdef18`](#insn-00bdef18)

~~~json
{
  "source": "00bdef18",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef24`](#insn-00bdef24)

~~~json
{
  "source": "00bdef24",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef28`](#insn-00bdef28)

~~~json
{
  "source": "00bdef28",
  "target": "00bdef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef30`](#insn-00bdef30)

~~~json
{
  "source": "00bdef30",
  "target": "00bdef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef40`](#insn-00bdef40)

~~~json
{
  "source": "00bdef40",
  "target": "00c5b2f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef44`](#insn-00bdef44)

~~~json
{
  "source": "00bdef44",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef48`](#insn-00bdef48)

~~~json
{
  "source": "00bdef48",
  "target": "00bdef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef4c`](#insn-00bdef4c)

~~~json
{
  "source": "00bdef4c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef50`](#insn-00bdef50)

~~~json
{
  "source": "00bdef50",
  "target": "00bdef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef54`](#insn-00bdef54)

~~~json
{
  "source": "00bdef54",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef58`](#insn-00bdef58)

~~~json
{
  "source": "00bdef58",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef5c`](#insn-00bdef5c)

~~~json
{
  "source": "00bdef5c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef60`](#insn-00bdef60)

~~~json
{
  "source": "00bdef60",
  "target": "00bdef4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef64`](#insn-00bdef64)

~~~json
{
  "source": "00bdef64",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef6c`](#insn-00bdef6c)

~~~json
{
  "source": "00bdef6c",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef70`](#insn-00bdef70)

~~~json
{
  "source": "00bdef70",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef74`](#insn-00bdef74)

~~~json
{
  "source": "00bdef74",
  "target": "00bdef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef78`](#insn-00bdef78)

~~~json
{
  "source": "00bdef78",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef7c`](#insn-00bdef7c)

~~~json
{
  "source": "00bdef7c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdef80`](#insn-00bdef80)

~~~json
{
  "source": "00bdef80",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef84`](#insn-00bdef84)

~~~json
{
  "source": "00bdef84",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef88`](#insn-00bdef88)

~~~json
{
  "source": "00bdef88",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef8c`](#insn-00bdef8c)

~~~json
{
  "source": "00bdef8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef90`](#insn-00bdef90)

~~~json
{
  "source": "00bdef90",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef94`](#insn-00bdef94)

~~~json
{
  "source": "00bdef94",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdef9c`](#insn-00bdef9c)

~~~json
{
  "source": "00bdef9c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdefa4`](#insn-00bdefa4)

~~~json
{
  "source": "00bdefa4",
  "target": "00bdefc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefac`](#insn-00bdefac)

~~~json
{
  "source": "00bdefac",
  "target": "01126dc8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dc8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdefb8`](#insn-00bdefb8)

~~~json
{
  "source": "00bdefb8",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdefc4`](#insn-00bdefc4)

~~~json
{
  "source": "00bdefc4",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdefc8`](#insn-00bdefc8)

~~~json
{
  "source": "00bdefc8",
  "target": "00bdeff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefd0`](#insn-00bdefd0)

~~~json
{
  "source": "00bdefd0",
  "target": "00bdeff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefe0`](#insn-00bdefe0)

~~~json
{
  "source": "00bdefe0",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdefe4`](#insn-00bdefe4)

~~~json
{
  "source": "00bdefe4",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefe8`](#insn-00bdefe8)

~~~json
{
  "source": "00bdefe8",
  "target": "00bdf004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdefec`](#insn-00bdefec)

~~~json
{
  "source": "00bdefec",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeff0`](#insn-00bdeff0)

~~~json
{
  "source": "00bdeff0",
  "target": "00bdf024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeff4`](#insn-00bdeff4)

~~~json
{
  "source": "00bdeff4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeff8`](#insn-00bdeff8)

~~~json
{
  "source": "00bdeff8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdeffc`](#insn-00bdeffc)

~~~json
{
  "source": "00bdeffc",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf000`](#insn-00bdf000)

~~~json
{
  "source": "00bdf000",
  "target": "00bdefec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf004`](#insn-00bdf004)

~~~json
{
  "source": "00bdf004",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf00c`](#insn-00bdf00c)

~~~json
{
  "source": "00bdf00c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf010`](#insn-00bdf010)

~~~json
{
  "source": "00bdf010",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf014`](#insn-00bdf014)

~~~json
{
  "source": "00bdf014",
  "target": "00bdf024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf018`](#insn-00bdf018)

~~~json
{
  "source": "00bdf018",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf01c`](#insn-00bdf01c)

~~~json
{
  "source": "00bdf01c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf020`](#insn-00bdf020)

~~~json
{
  "source": "00bdf020",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf024`](#insn-00bdf024)

~~~json
{
  "source": "00bdf024",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf028`](#insn-00bdf028)

~~~json
{
  "source": "00bdf028",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf02c`](#insn-00bdf02c)

~~~json
{
  "source": "00bdf02c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf030`](#insn-00bdf030)

~~~json
{
  "source": "00bdf030",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf034`](#insn-00bdf034)

~~~json
{
  "source": "00bdf034",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf03c`](#insn-00bdf03c)

~~~json
{
  "source": "00bdf03c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf044`](#insn-00bdf044)

~~~json
{
  "source": "00bdf044",
  "target": "00bdf060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf04c`](#insn-00bdf04c)

~~~json
{
  "source": "00bdf04c",
  "target": "01126dd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf058`](#insn-00bdf058)

~~~json
{
  "source": "00bdf058",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf064`](#insn-00bdf064)

~~~json
{
  "source": "00bdf064",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf068`](#insn-00bdf068)

~~~json
{
  "source": "00bdf068",
  "target": "00bdf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf070`](#insn-00bdf070)

~~~json
{
  "source": "00bdf070",
  "target": "00bdf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf080`](#insn-00bdf080)

~~~json
{
  "source": "00bdf080",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf084`](#insn-00bdf084)

~~~json
{
  "source": "00bdf084",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf088`](#insn-00bdf088)

~~~json
{
  "source": "00bdf088",
  "target": "00bdf0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf08c`](#insn-00bdf08c)

~~~json
{
  "source": "00bdf08c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf090`](#insn-00bdf090)

~~~json
{
  "source": "00bdf090",
  "target": "00bdf0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf094`](#insn-00bdf094)

~~~json
{
  "source": "00bdf094",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf098`](#insn-00bdf098)

~~~json
{
  "source": "00bdf098",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf09c`](#insn-00bdf09c)

~~~json
{
  "source": "00bdf09c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0a0`](#insn-00bdf0a0)

~~~json
{
  "source": "00bdf0a0",
  "target": "00bdf08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0a4`](#insn-00bdf0a4)

~~~json
{
  "source": "00bdf0a4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0ac`](#insn-00bdf0ac)

~~~json
{
  "source": "00bdf0ac",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0b0`](#insn-00bdf0b0)

~~~json
{
  "source": "00bdf0b0",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0b4`](#insn-00bdf0b4)

~~~json
{
  "source": "00bdf0b4",
  "target": "00bdf0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0b8`](#insn-00bdf0b8)

~~~json
{
  "source": "00bdf0b8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0bc`](#insn-00bdf0bc)

~~~json
{
  "source": "00bdf0bc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf0c0`](#insn-00bdf0c0)

~~~json
{
  "source": "00bdf0c0",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0c8`](#insn-00bdf0c8)

~~~json
{
  "source": "00bdf0c8",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0cc`](#insn-00bdf0cc)

~~~json
{
  "source": "00bdf0cc",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0d4`](#insn-00bdf0d4)

~~~json
{
  "source": "00bdf0d4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0d8`](#insn-00bdf0d8)

~~~json
{
  "source": "00bdf0d8",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0dc`](#insn-00bdf0dc)

~~~json
{
  "source": "00bdf0dc",
  "target": "00bdf0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf0e8`](#insn-00bdf0e8)

~~~json
{
  "source": "00bdf0e8",
  "target": "00c5dea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf0f4`](#insn-00bdf0f4)

~~~json
{
  "source": "00bdf0f4",
  "target": "00bdf104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf100`](#insn-00bdf100)

~~~json
{
  "source": "00bdf100",
  "target": "00c5dec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf108`](#insn-00bdf108)

~~~json
{
  "source": "00bdf108",
  "target": "00c5db70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf110`](#insn-00bdf110)

~~~json
{
  "source": "00bdf110",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf114`](#insn-00bdf114)

~~~json
{
  "source": "00bdf114",
  "target": "00c9ba60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdf11c`](#insn-00bdf11c)

~~~json
{
  "source": "00bdf11c",
  "target": "00c92910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92900",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdf11c`](#insn-00bdf11c)

~~~json
{
  "source": "00bdf11c",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf124`](#insn-00bdf124)

~~~json
{
  "source": "00bdf124",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf12c`](#insn-00bdf12c)

~~~json
{
  "source": "00bdf12c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf13c`](#insn-00bdf13c)

~~~json
{
  "source": "00bdf13c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf140`](#insn-00bdf140)

~~~json
{
  "source": "00bdf140",
  "target": "00c5db80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf144`](#insn-00bdf144)

~~~json
{
  "source": "00bdf144",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf150`](#insn-00bdf150)

~~~json
{
  "source": "00bdf150",
  "target": "00bdec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf154`](#insn-00bdf154)

~~~json
{
  "source": "00bdf154",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf164`](#insn-00bdf164)

~~~json
{
  "source": "00bdf164",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf16c`](#insn-00bdf16c)

~~~json
{
  "source": "00bdf16c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf174`](#insn-00bdf174)

~~~json
{
  "source": "00bdf174",
  "target": "00bdf198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf17c`](#insn-00bdf17c)

~~~json
{
  "source": "00bdf17c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf180`](#insn-00bdf180)

~~~json
{
  "source": "00bdf180",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf184`](#insn-00bdf184)

~~~json
{
  "source": "00bdf184",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf188`](#insn-00bdf188)

~~~json
{
  "source": "00bdf188",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf18c`](#insn-00bdf18c)

~~~json
{
  "source": "00bdf18c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf198`](#insn-00bdf198)

~~~json
{
  "source": "00bdf198",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
