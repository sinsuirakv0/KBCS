# 00bdfc0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdec18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-f214658bbb2c92e2b38b2e5228697c05)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "be83eb5fac1eba0e95828060729bb94ccc3c7d3a8984c00e280f8eef853108f8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfc0c",
        "00be022b"
      ]
    ],
    "bytes_sha256": "a207894f06bf9bca756e4128ea9ef81bd0bc456b84db3995ee13a1fcdcea543c",
    "instruction_count": 392,
    "instruction_bytes": 1568,
    "body_bytes": 1568,
    "indirect": 4,
    "unresolved": 4
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfc0c"></a> `00bdfc0c` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bdfc10"></a> `00bdfc10` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfc14"></a> `00bdfc14` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdfc18"></a> `00bdfc18` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfc1c"></a> `00bdfc1c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfc20"></a> `00bdfc20` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfc24"></a> `00bdfc24` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdfc28"></a> `00bdfc28` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00bdfc2c"></a> `00bdfc2c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdfc30"></a> `00bdfc30` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdfc34"></a> `00bdfc34` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdfc38"></a> `00bdfc38` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfc3c"></a> `00bdfc3c` | `a8 03 1a f8` | stur x8,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bdfc40"></a> `00bdfc40` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdfc44"></a> `00bdfc44` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfc48"></a> `00bdfc48` | `08 4c 40 f9` | ldr x8,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfc4c"></a> `00bdfc4c` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfc50"></a> `00bdfc50` | `28 2d 00 b4` | cbz x8,0x00be01f4 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc54"></a> `00bdfc54` | `09 01 41 f9` | ldr x9,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfc58"></a> `00bdfc58` | `e9 2c 00 b4` | cbz x9,0x00be01f4 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc5c"></a> `00bdfc5c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfc60"></a> `00bdfc60` | `30 f1 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc64"></a> `00bdfc64` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfc68"></a> `00bdfc68` | `49 2a 00 90` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdfc6c"></a> `00bdfc6c` | `22 01 47 f9` | ldr x2,[x9, #0xe00] | `FALL_THROUGH`
<a id="insn-00bdfc70"></a> `00bdfc70` | `08 4d 40 f9` | ldr x8,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfc74"></a> `00bdfc74` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bdfc78"></a> `00bdfc78` | `e0 1f 00 f9` | str x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdfc7c"></a> `00bdfc7c` | `c6 df e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc80"></a> `00bdfc80` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfc84"></a> `00bdfc84` | `80 2b 00 b4` | cbz x0,0x00be01f4 | `CONDITIONAL_JUMP`
<a id="insn-00bdfc88"></a> `00bdfc88` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bdfc8c"></a> `00bdfc8c` | `4d f2 01 94` | bl 0x00c5c5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc90"></a> `00bdfc90` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdfc94"></a> `00bdfc94` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfc98"></a> `00bdfc98` | `60 5a e6 97` | bl 0x00576618 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfc9c"></a> `00bdfc9c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdfca0"></a> `00bdfca0` | `81 7e 40 93` | sxtw x1,w20 | `FALL_THROUGH`
<a id="insn-00bdfca4"></a> `00bdfca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdfca8"></a> `00bdfca8` | `b2 fc 01 94` | bl 0x00c5ef70 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfcac"></a> `00bdfcac` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfcb0"></a> `00bdfcb0` | `f4 17 00 f9` | str x20,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdfcb4"></a> `00bdfcb4` | `8b 29 00 54` | b.lt 0x00be01e4 | `CONDITIONAL_JUMP`
<a id="insn-00bdfcb8"></a> `00bdfcb8` | `eb 05 00 b0` | adrp x11,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bdfcbc"></a> `00bdfcbc` | `6b 81 45 f9` | ldr x11,[x11, #0xb00] | `FALL_THROUGH`
<a id="insn-00bdfcc0"></a> `00bdfcc0` | `ea 05 00 b0` | adrp x10,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bdfcc4"></a> `00bdfcc4` | `4a 35 45 f9` | ldr x10,[x10, #0xa68] | `FALL_THROUGH`
<a id="insn-00bdfcc8"></a> `00bdfcc8` | `e8 e3 03 91` | add x8,sp,#0xf8 | `FALL_THROUGH`
<a id="insn-00bdfccc"></a> `00bdfccc` | `e9 83 01 91` | add x9,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bdfcd0"></a> `00bdfcd0` | `1c 21 00 91` | add x28,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfcd4"></a> `00bdfcd4` | `28 81 00 91` | add x8,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bdfcd8"></a> `00bdfcd8` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfcdc"></a> `00bdfcdc` | `68 41 00 91` | add x8,x11,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfce0"></a> `00bdfce0` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00bdfce4"></a> `00bdfce4` | `3b 21 00 91` | add x27,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bdfce8"></a> `00bdfce8` | `36 e1 00 91` | add x22,x9,#0x38 | `FALL_THROUGH`
<a id="insn-00bdfcec"></a> `00bdfcec` | `35 41 01 91` | add x21,x9,#0x50 | `FALL_THROUGH`
<a id="insn-00bdfcf0"></a> `00bdfcf0` | `34 a1 01 91` | add x20,x9,#0x68 | `FALL_THROUGH`
<a id="insn-00bdfcf4"></a> `00bdfcf4` | `37 01 02 91` | add x23,x9,#0x80 | `FALL_THROUGH`
<a id="insn-00bdfcf8"></a> `00bdfcf8` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdfcfc"></a> `00bdfcfc` | `48 41 00 91` | add x8,x10,#0x10 | `FALL_THROUGH`
<a id="insn-00bdfd00"></a> `00bdfd00` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdfd04"></a> `00bdfd04` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdfd08"></a> `00bdfd08` | `2e f2 01 94` | bl 0x00c5c5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd0c"></a> `00bdfd0c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdfd10"></a> `00bdfd10` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfd14"></a> `00bdfd14` | `e3 03 18 2a` | mov w3,w24 | `FALL_THROUGH`
<a id="insn-00bdfd18"></a> `00bdfd18` | `9f df e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd1c"></a> `00bdfd1c` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdfd20"></a> `00bdfd20` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdfd24"></a> `00bdfd24` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdfd28"></a> `00bdfd28` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdfd2c"></a> `00bdfd2c` | `08 4d 40 f9` | ldr x8,[x8, #0x98] | `FALL_THROUGH`
<a id="insn-00bdfd30"></a> `00bdfd30` | `80 83 03 ad` | stp q0,q0,[x28, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfd34"></a> `00bdfd34` | `80 83 02 ad` | stp q0,q0,[x28, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfd38"></a> `00bdfd38` | `80 83 01 ad` | stp q0,q0,[x28, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfd3c"></a> `00bdfd3c` | `80 83 00 ad` | stp q0,q0,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfd40"></a> `00bdfd40` | `80 03 80 3d` | str q0,[x28] | `FALL_THROUGH`
<a id="insn-00bdfd44"></a> `00bdfd44` | `e9 7f 00 f9` | str x9,[sp, #0xf8] | `FALL_THROUGH`
<a id="insn-00bdfd48"></a> `00bdfd48` | `e8 03 19 a9` | stp x8,x0,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdfd4c"></a> `00bdfd4c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfd50"></a> `00bdfd50` | `f4 f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfd54"></a> `00bdfd54` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdfd58"></a> `00bdfd58` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdfd5c"></a> `00bdfd5c` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdfd60"></a> `00bdfd60` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bdfd64"></a> `00bdfd64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfd68"></a> `00bdfd68` | `e0 cf 00 f9` | str x0,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00bdfd6c"></a> `00bdfd6c` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00bdfd70"></a> `00bdfd70` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdfd74"></a> `00bdfd74` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bdfd78"></a> `00bdfd78` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bdfd7c"></a> `00bdfd7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdfd80"></a> `00bdfd80` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bdfd84"></a> `00bdfd84` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdfd88"></a> `00bdfd88` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdfd8c"></a> `00bdfd8c` | `e8 6b 59 a9` | ldp x8,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdfd90"></a> `00bdfd90` | `60 83 03 ad` | stp q0,q0,[x27, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfd94"></a> `00bdfd94` | `60 83 02 ad` | stp q0,q0,[x27, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfd98"></a> `00bdfd98` | `60 83 01 ad` | stp q0,q0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00bdfd9c"></a> `00bdfd9c` | `60 83 00 ad` | stp q0,q0,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfda0"></a> `00bdfda0` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00bdfda4"></a> `00bdfda4` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdfda8"></a> `00bdfda8` | `de f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfdac"></a> `00bdfdac` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdfdb0"></a> `00bdfdb0` | `fa 00 00 b4` | cbz x26,0x00bdfdcc | `CONDITIONAL_JUMP`
<a id="insn-00bdfdb4"></a> `00bdfdb4` | `48 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdfdb8"></a> `00bdfdb8` | `02 41 47 f9` | ldr x2,[x8, #0xe80] | `FALL_THROUGH`
<a id="insn-00bdfdbc"></a> `00bdfdbc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfdc0"></a> `00bdfdc0` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdfdc4"></a> `00bdfdc4` | `74 df e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfdc8"></a> `00bdfdc8` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdfdcc"></a> `00bdfdcc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfdd0"></a> `00bdfdd0` | `8c f0 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfdd4"></a> `00bdfdd4` | `7a 01 00 b4` | cbz x26,0x00bdfe00 | `CONDITIONAL_JUMP`
<a id="insn-00bdfdd8"></a> `00bdfdd8` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfddc"></a> `00bdfddc` | `28 01 00 36` | tbz w8,#0x0,0x00bdfe00 | `CONDITIONAL_JUMP`
<a id="insn-00bdfde0"></a> `00bdfde0` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdfde4"></a> `00bdfde4` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfde8"></a> `00bdfde8` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdfdec"></a> `00bdfdec` | `91 f1 01 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfdf0"></a> `00bdfdf0` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdfdf4"></a> `00bdfdf4` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdfe10 | `CONDITIONAL_JUMP`
<a id="insn-00bdfdf8"></a> `00bdfdf8` | `ff d3 00 79` | strh wzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdfdfc"></a> `00bdfdfc` | `0d 00 00 14` | b 0x00bdfe30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfe00"></a> `00bdfe00` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfe04"></a> `00bdfe04` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdfe08"></a> `00bdfe08` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdfe0c"></a> `00bdfe0c` | `68 ff 07 36` | tbz w8,#0x0,0x00bdfdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe10"></a> `00bdfe10` | `e8 3f 40 f9` | ldr x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bdfe14"></a> `00bdfe14` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdfe18"></a> `00bdfe18` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdfe1c"></a> `00bdfe1c` | `ff 3b 00 f9` | str xzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bdfe20"></a> `00bdfe20` | `88 00 00 36` | tbz w8,#0x0,0x00bdfe30 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe24"></a> `00bdfe24` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bdfe28"></a> `00bdfe28` | `4a e4 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe2c"></a> `00bdfe2c` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdfe30"></a> `00bdfe30` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdfe34"></a> `00bdfe34` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdfe38"></a> `00bdfe38` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdfe3c"></a> `00bdfe3c` | `68 0b 00 f9` | str x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfe40"></a> `00bdfe40` | `60 03 80 3d` | str q0,[x27] | `FALL_THROUGH`
<a id="insn-00bdfe44"></a> `00bdfe44` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdfe48"></a> `00bdfe48` | `b6 f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe4c"></a> `00bdfe4c` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdfe50"></a> `00bdfe50` | `fa 00 00 b4` | cbz x26,0x00bdfe6c | `CONDITIONAL_JUMP`
<a id="insn-00bdfe54"></a> `00bdfe54` | `48 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdfe58"></a> `00bdfe58` | `02 55 47 f9` | ldr x2,[x8, #0xea8] | `FALL_THROUGH`
<a id="insn-00bdfe5c"></a> `00bdfe5c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfe60"></a> `00bdfe60` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdfe64"></a> `00bdfe64` | `4c df e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe68"></a> `00bdfe68` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdfe6c"></a> `00bdfe6c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfe70"></a> `00bdfe70` | `64 f0 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe74"></a> `00bdfe74` | `7a 01 00 b4` | cbz x26,0x00bdfea0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe78"></a> `00bdfe78` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdfe7c"></a> `00bdfe7c` | `28 01 00 36` | tbz w8,#0x0,0x00bdfea0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe80"></a> `00bdfe80` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdfe84"></a> `00bdfe84` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdfe88"></a> `00bdfe88` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdfe8c"></a> `00bdfe8c` | `69 f1 01 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfe90"></a> `00bdfe90` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfe94"></a> `00bdfe94` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdfeb0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfe98"></a> `00bdfe98` | `ff 03 01 79` | strh wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfe9c"></a> `00bdfe9c` | `0d 00 00 14` | b 0x00bdfed0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdfea0"></a> `00bdfea0` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdfea4"></a> `00bdfea4` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdfea8"></a> `00bdfea8` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfeac"></a> `00bdfeac` | `68 ff 07 36` | tbz w8,#0x0,0x00bdfe98 | `CONDITIONAL_JUMP`
<a id="insn-00bdfeb0"></a> `00bdfeb0` | `e8 4b 40 f9` | ldr x8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdfeb4"></a> `00bdfeb4` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdfeb8"></a> `00bdfeb8` | `e8 03 42 39` | ldrb w8,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfebc"></a> `00bdfebc` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00bdfec0"></a> `00bdfec0` | `88 00 00 36` | tbz w8,#0x0,0x00bdfed0 | `CONDITIONAL_JUMP`
<a id="insn-00bdfec4"></a> `00bdfec4` | `e0 4b 40 f9` | ldr x0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdfec8"></a> `00bdfec8` | `22 e4 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfecc"></a> `00bdfecc` | `ff 43 00 f9` | str xzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdfed0"></a> `00bdfed0` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdfed4"></a> `00bdfed4` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdfed8"></a> `00bdfed8` | `ea 0b 40 f9` | ldr x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfedc"></a> `00bdfedc` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdfee0"></a> `00bdfee0` | `48 09 00 f9` | str x8,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00bdfee4"></a> `00bdfee4` | `40 01 80 3d` | str q0,[x10] | `FALL_THROUGH`
<a id="insn-00bdfee8"></a> `00bdfee8` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdfeec"></a> `00bdfeec` | `8d f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdfef0"></a> `00bdfef0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdfef4"></a> `00bdfef4` | `fa 00 00 b4` | cbz x26,0x00bdff10 | `CONDITIONAL_JUMP`
<a id="insn-00bdfef8"></a> `00bdfef8` | `48 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdfefc"></a> `00bdfefc` | `02 49 47 f9` | ldr x2,[x8, #0xe90] | `FALL_THROUGH`
<a id="insn-00bdff00"></a> `00bdff00` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdff04"></a> `00bdff04` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdff08"></a> `00bdff08` | `23 df e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff0c"></a> `00bdff0c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdff10"></a> `00bdff10` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdff14"></a> `00bdff14` | `3b f0 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff18"></a> `00bdff18` | `7a 01 00 b4` | cbz x26,0x00bdff44 | `CONDITIONAL_JUMP`
<a id="insn-00bdff1c"></a> `00bdff1c` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdff20"></a> `00bdff20` | `28 01 00 36` | tbz w8,#0x0,0x00bdff44 | `CONDITIONAL_JUMP`
<a id="insn-00bdff24"></a> `00bdff24` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdff28"></a> `00bdff28` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdff2c"></a> `00bdff2c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdff30"></a> `00bdff30` | `40 f1 01 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff34"></a> `00bdff34` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdff38"></a> `00bdff38` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdff54 | `CONDITIONAL_JUMP`
<a id="insn-00bdff3c"></a> `00bdff3c` | `ff 33 01 79` | strh wzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdff40"></a> `00bdff40` | `0d 00 00 14` | b 0x00bdff74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdff44"></a> `00bdff44` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdff48"></a> `00bdff48` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdff4c"></a> `00bdff4c` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdff50"></a> `00bdff50` | `68 ff 07 36` | tbz w8,#0x0,0x00bdff3c | `CONDITIONAL_JUMP`
<a id="insn-00bdff54"></a> `00bdff54` | `e8 57 40 f9` | ldr x8,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdff58"></a> `00bdff58` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdff5c"></a> `00bdff5c` | `e8 63 42 39` | ldrb w8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdff60"></a> `00bdff60` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdff64"></a> `00bdff64` | `88 00 00 36` | tbz w8,#0x0,0x00bdff74 | `CONDITIONAL_JUMP`
<a id="insn-00bdff68"></a> `00bdff68` | `e0 57 40 f9` | ldr x0,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdff6c"></a> `00bdff6c` | `f9 e3 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff70"></a> `00bdff70` | `ff 4f 00 f9` | str xzr,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00bdff74"></a> `00bdff74` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdff78"></a> `00bdff78` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdff7c"></a> `00bdff7c` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdff80"></a> `00bdff80` | `c8 0a 00 f9` | str x8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bdff84"></a> `00bdff84` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bdff88"></a> `00bdff88` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdff8c"></a> `00bdff8c` | `65 f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdff90"></a> `00bdff90` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdff94"></a> `00bdff94` | `fa 00 00 b4` | cbz x26,0x00bdffb0 | `CONDITIONAL_JUMP`
<a id="insn-00bdff98"></a> `00bdff98` | `48 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdff9c"></a> `00bdff9c` | `02 51 47 f9` | ldr x2,[x8, #0xea0] | `FALL_THROUGH`
<a id="insn-00bdffa0"></a> `00bdffa0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdffa4"></a> `00bdffa4` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdffa8"></a> `00bdffa8` | `fb de e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdffac"></a> `00bdffac` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdffb0"></a> `00bdffb0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdffb4"></a> `00bdffb4` | `13 f0 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdffb8"></a> `00bdffb8` | `7a 01 00 b4` | cbz x26,0x00bdffe4 | `CONDITIONAL_JUMP`
<a id="insn-00bdffbc"></a> `00bdffbc` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdffc0"></a> `00bdffc0` | `28 01 00 36` | tbz w8,#0x0,0x00bdffe4 | `CONDITIONAL_JUMP`
<a id="insn-00bdffc4"></a> `00bdffc4` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bdffc8"></a> `00bdffc8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdffcc"></a> `00bdffcc` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bdffd0"></a> `00bdffd0` | `f0 f0 01 94` | bl 0x00c5c390 | `UNCONDITIONAL_CALL`
<a id="insn-00bdffd4"></a> `00bdffd4` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdffd8"></a> `00bdffd8` | `e8 00 00 37` | tbnz w8,#0x0,0x00bdfff4 | `CONDITIONAL_JUMP`
<a id="insn-00bdffdc"></a> `00bdffdc` | `ff 63 01 79` | strh wzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdffe0"></a> `00bdffe0` | `0d 00 00 14` | b 0x00be0014 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdffe4"></a> `00bdffe4` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdffe8"></a> `00bdffe8` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdffec"></a> `00bdffec` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdfff0"></a> `00bdfff0` | `68 ff 07 36` | tbz w8,#0x0,0x00bdffdc | `CONDITIONAL_JUMP`
<a id="insn-00bdfff4"></a> `00bdfff4` | `e8 63 40 f9` | ldr x8,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdfff8"></a> `00bdfff8` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bdfffc"></a> `00bdfffc` | `e8 c3 42 39` | ldrb w8,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00be0000"></a> `00be0000` | `ff 5f 00 f9` | str xzr,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00be0004"></a> `00be0004` | `88 00 00 36` | tbz w8,#0x0,0x00be0014 | `CONDITIONAL_JUMP`
<a id="insn-00be0008"></a> `00be0008` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00be000c"></a> `00be000c` | `d1 e3 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00be0010"></a> `00be0010` | `ff 5b 00 f9` | str xzr,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00be0014"></a> `00be0014` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00be0018"></a> `00be0018` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00be001c"></a> `00be001c` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00be0020"></a> `00be0020` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00be0024"></a> `00be0024` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00be0028"></a> `00be0028` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00be002c"></a> `00be002c` | `3d f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00be0030"></a> `00be0030` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00be0034"></a> `00be0034` | `fa 00 00 b4` | cbz x26,0x00be0050 | `CONDITIONAL_JUMP`
<a id="insn-00be0038"></a> `00be0038` | `28 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00be003c"></a> `00be003c` | `02 45 47 f9` | ldr x2,[x8, #0xe88] | `FALL_THROUGH`
<a id="insn-00be0040"></a> `00be0040` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be0044"></a> `00be0044` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00be0048"></a> `00be0048` | `d3 de e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00be004c"></a> `00be004c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00be0050"></a> `00be0050` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be0054"></a> `00be0054` | `eb ef 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00be0058"></a> `00be0058` | `7a 01 00 b4` | cbz x26,0x00be0084 | `CONDITIONAL_JUMP`
<a id="insn-00be005c"></a> `00be005c` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00be0060"></a> `00be0060` | `28 01 00 36` | tbz w8,#0x0,0x00be0084 | `CONDITIONAL_JUMP`
<a id="insn-00be0064"></a> `00be0064` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00be0068"></a> `00be0068` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be006c"></a> `00be006c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00be0070"></a> `00be0070` | `f0 f0 01 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00be0074"></a> `00be0074` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00be0078"></a> `00be0078` | `e8 00 00 37` | tbnz w8,#0x0,0x00be0094 | `CONDITIONAL_JUMP`
<a id="insn-00be007c"></a> `00be007c` | `ff 93 01 79` | strh wzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00be0080"></a> `00be0080` | `0d 00 00 14` | b 0x00be00b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0084"></a> `00be0084` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be0088"></a> `00be0088` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00be008c"></a> `00be008c` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00be0090"></a> `00be0090` | `68 ff 07 36` | tbz w8,#0x0,0x00be007c | `CONDITIONAL_JUMP`
<a id="insn-00be0094"></a> `00be0094` | `e8 6f 40 f9` | ldr x8,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00be0098"></a> `00be0098` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00be009c"></a> `00be009c` | `e8 23 43 39` | ldrb w8,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00be00a0"></a> `00be00a0` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00be00a4"></a> `00be00a4` | `88 00 00 36` | tbz w8,#0x0,0x00be00b4 | `CONDITIONAL_JUMP`
<a id="insn-00be00a8"></a> `00be00a8` | `e0 6f 40 f9` | ldr x0,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00be00ac"></a> `00be00ac` | `a9 e3 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00be00b0"></a> `00be00b0` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00be00b4"></a> `00be00b4` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00be00b8"></a> `00be00b8` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00be00bc"></a> `00be00bc` | `e9 6b 59 a9` | ldp x9,x26,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00be00c0"></a> `00be00c0` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00be00c4"></a> `00be00c4` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00be00c8"></a> `00be00c8` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00be00cc"></a> `00be00cc` | `15 f0 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00be00d0"></a> `00be00d0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00be00d4"></a> `00be00d4` | `fa 00 00 b4` | cbz x26,0x00be00f0 | `CONDITIONAL_JUMP`
<a id="insn-00be00d8"></a> `00be00d8` | `28 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00be00dc"></a> `00be00dc` | `02 4d 47 f9` | ldr x2,[x8, #0xe98] | `FALL_THROUGH`
<a id="insn-00be00e0"></a> `00be00e0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be00e4"></a> `00be00e4` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00be00e8"></a> `00be00e8` | `ab de e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00be00ec"></a> `00be00ec` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00be00f0"></a> `00be00f0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be00f4"></a> `00be00f4` | `c3 ef 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00be00f8"></a> `00be00f8` | `7a 01 00 b4` | cbz x26,0x00be0124 | `CONDITIONAL_JUMP`
<a id="insn-00be00fc"></a> `00be00fc` | `08 00 00 52` | eor w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00be0100"></a> `00be0100` | `28 01 00 36` | tbz w8,#0x0,0x00be0124 | `CONDITIONAL_JUMP`
<a id="insn-00be0104"></a> `00be0104` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00be0108"></a> `00be0108` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be010c"></a> `00be010c` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00be0110"></a> `00be0110` | `c8 f0 01 94` | bl 0x00c5c430 | `UNCONDITIONAL_CALL`
<a id="insn-00be0114"></a> `00be0114` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00be0118"></a> `00be0118` | `e8 00 00 37` | tbnz w8,#0x0,0x00be0134 | `CONDITIONAL_JUMP`
<a id="insn-00be011c"></a> `00be011c` | `ff c3 01 79` | strh wzr,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00be0120"></a> `00be0120` | `0d 00 00 14` | b 0x00be0154 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0124"></a> `00be0124` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be0128"></a> `00be0128` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00be012c"></a> `00be012c` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00be0130"></a> `00be0130` | `68 ff 07 36` | tbz w8,#0x0,0x00be011c | `CONDITIONAL_JUMP`
<a id="insn-00be0134"></a> `00be0134` | `e8 7b 40 f9` | ldr x8,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00be0138"></a> `00be0138` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00be013c"></a> `00be013c` | `e8 83 43 39` | ldrb w8,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00be0140"></a> `00be0140` | `ff 77 00 f9` | str xzr,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00be0144"></a> `00be0144` | `88 00 00 36` | tbz w8,#0x0,0x00be0154 | `CONDITIONAL_JUMP`
<a id="insn-00be0148"></a> `00be0148` | `e0 7b 40 f9` | ldr x0,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00be014c"></a> `00be014c` | `81 e3 01 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00be0150"></a> `00be0150` | `ff 73 00 f9` | str xzr,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00be0154"></a> `00be0154` | `79 a6 40 a9` | ldp x25,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00be0158"></a> `00be0158` | `e8 2f 40 f9` | ldr x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00be015c"></a> `00be015c` | `e0 83 c4 3c` | ldur q0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00be0160"></a> `00be0160` | `3f 03 09 eb` | cmp x25,x9 | `FALL_THROUGH`
<a id="insn-00be0164"></a> `00be0164` | `e8 0a 00 f9` | str x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00be0168"></a> `00be0168` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-00be016c"></a> `00be016c` | `e0 00 00 54` | b.eq 0x00be0188 | `CONDITIONAL_JUMP`
<a id="insn-00be0170"></a> `00be0170` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00be0174"></a> `00be0174` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00be0178"></a> `00be0178` | `72 fb 01 94` | bl 0x00c5ef40 | `UNCONDITIONAL_CALL`
<a id="insn-00be017c"></a> `00be017c` | `28 63 02 91` | add x8,x25,#0x98 | `FALL_THROUGH`
<a id="insn-00be0180"></a> `00be0180` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00be0184"></a> `00be0184` | `04 00 00 14` | b 0x00be0194 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0188"></a> `00be0188` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00be018c"></a> `00be018c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00be0190"></a> `00be0190` | `74 fb 01 94` | bl 0x00c5ef60 | `UNCONDITIONAL_CALL`
<a id="insn-00be0194"></a> `00be0194` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00be0198"></a> `00be0198` | `9e fa 01 94` | bl 0x00c5ec10 | `UNCONDITIONAL_CALL`
<a id="insn-00be019c"></a> `00be019c` | `e9 05 00 90` | adrp x9,0xc9c000 | `FALL_THROUGH`
<a id="insn-00be01a0"></a> `00be01a0` | `e8 cb 40 f9` | ldr x8,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00be01a4"></a> `00be01a4` | `29 81 45 f9` | ldr x9,[x9, #0xb00] | `FALL_THROUGH`
<a id="insn-00be01a8"></a> `00be01a8` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00be01ac"></a> `00be01ac` | `e9 7f 00 f9` | str x9,[sp, #0xf8] | `FALL_THROUGH`
<a id="insn-00be01b0"></a> `00be01b0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00be01b4"></a> `00be01b4` | `db ef 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00be01b8"></a> `00be01b8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00be01bc"></a> `00be01bc` | `e1 cf 40 f9` | ldr x1,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00be01c0"></a> `00be01c0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00be01c4"></a> `00be01c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be01c8"></a> `00be01c8` | `e0 e3 03 91` | add x0,sp,#0xf8 | `FALL_THROUGH`
<a id="insn-00be01cc"></a> `00be01cc` | `ff cf 00 f9` | str xzr,[sp, #0x198] | `FALL_THROUGH`
<a id="insn-00be01d0"></a> `00be01d0` | `94 fa 01 94` | bl 0x00c5ec20 | `UNCONDITIONAL_CALL`
<a id="insn-00be01d4"></a> `00be01d4` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00be01d8"></a> `00be01d8` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00be01dc"></a> `00be01dc` | `1f 01 18 6b` | cmp w8,w24 | `FALL_THROUGH`
<a id="insn-00be01e0"></a> `00be01e0` | `21 d9 ff 54` | b.ne 0x00bdfd04 | `CONDITIONAL_JUMP`
<a id="insn-00be01e4"></a> `00be01e4` | `e1 03 43 a9` | ldp x1,x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00be01e8"></a> `00be01e8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00be01ec"></a> `00be01ec` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00be01f0"></a> `00be01f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be01f4"></a> `00be01f4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00be01f8"></a> `00be01f8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00be01fc"></a> `00be01fc` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00be0200"></a> `00be0200` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00be0204"></a> `00be0204` | `21 01 00 54` | b.ne 0x00be0228 | `CONDITIONAL_JUMP`
<a id="insn-00be0208"></a> `00be0208` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00be020c"></a> `00be020c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be0210"></a> `00be0210` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00be0214"></a> `00be0214` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00be0218"></a> `00be0218` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00be021c"></a> `00be021c` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00be0220"></a> `00be0220` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00be0224"></a> `00be0224` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00be0228"></a> `00be0228` | `56 e3 01 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfc0c`](#insn-00bdfc0c) 範囲 `[['00bdfc0c', '00bdfc0f']]`
  - `FALL_THROUGH` [`00bdfc0c`](#insn-00bdfc0c) → [`00bdfc10`](#insn-00bdfc10)
- ブロック [`00bdfc10`](#insn-00bdfc10) 範囲 `[['00bdfc10', '00bdfc2b']]`
  - `FALL_THROUGH` [`00bdfc28`](#insn-00bdfc28) → [`00bdfc2c`](#insn-00bdfc2c)
- ブロック [`00bdfc2c`](#insn-00bdfc2c) 範囲 `[['00bdfc2c', '00bdfc2f']]`
  - `FALL_THROUGH` [`00bdfc2c`](#insn-00bdfc2c) → [`00bdfc30`](#insn-00bdfc30)
- ブロック [`00bdfc30`](#insn-00bdfc30) 範囲 `[['00bdfc30', '00bdfc33']]`
  - `FALL_THROUGH` [`00bdfc30`](#insn-00bdfc30) → [`00bdfc34`](#insn-00bdfc34)
- ブロック [`00bdfc34`](#insn-00bdfc34) 範囲 `[['00bdfc34', '00bdfc3b']]`
  - `FALL_THROUGH` [`00bdfc38`](#insn-00bdfc38) → [`00bdfc3c`](#insn-00bdfc3c)
- ブロック [`00bdfc3c`](#insn-00bdfc3c) 範囲 `[['00bdfc3c', '00bdfc3f']]`
  - `FALL_THROUGH` [`00bdfc3c`](#insn-00bdfc3c) → [`00bdfc40`](#insn-00bdfc40)
- ブロック [`00bdfc40`](#insn-00bdfc40) 範囲 `[['00bdfc40', '00bdfc53']]`
  - `CONDITIONAL_JUMP` [`00bdfc50`](#insn-00bdfc50) → [`00be01f4`](#insn-00be01f4)
  - `FALL_THROUGH` [`00bdfc50`](#insn-00bdfc50) → [`00bdfc54`](#insn-00bdfc54)
- ブロック [`00bdfc54`](#insn-00bdfc54) 範囲 `[['00bdfc54', '00bdfc5b']]`
  - `CONDITIONAL_JUMP` [`00bdfc58`](#insn-00bdfc58) → [`00be01f4`](#insn-00be01f4)
  - `FALL_THROUGH` [`00bdfc58`](#insn-00bdfc58) → [`00bdfc5c`](#insn-00bdfc5c)
- ブロック [`00bdfc5c`](#insn-00bdfc5c) 範囲 `[['00bdfc5c', '00bdfc87']]`
  - `CONDITIONAL_JUMP` [`00bdfc84`](#insn-00bdfc84) → [`00be01f4`](#insn-00be01f4)
  - `FALL_THROUGH` [`00bdfc84`](#insn-00bdfc84) → [`00bdfc88`](#insn-00bdfc88)
- ブロック [`00bdfc88`](#insn-00bdfc88) 範囲 `[['00bdfc88', '00bdfc93']]`
  - `FALL_THROUGH` [`00bdfc90`](#insn-00bdfc90) → [`00bdfc94`](#insn-00bdfc94)
- ブロック [`00bdfc94`](#insn-00bdfc94) 範囲 `[['00bdfc94', '00bdfcb7']]`
  - `CONDITIONAL_JUMP` [`00bdfcb4`](#insn-00bdfcb4) → [`00be01e4`](#insn-00be01e4)
  - `FALL_THROUGH` [`00bdfcb4`](#insn-00bdfcb4) → [`00bdfcb8`](#insn-00bdfcb8)
- ブロック [`00bdfcb8`](#insn-00bdfcb8) 範囲 `[['00bdfcb8', '00bdfccb']]`
  - `FALL_THROUGH` [`00bdfcc8`](#insn-00bdfcc8) → [`00bdfccc`](#insn-00bdfccc)
- ブロック [`00bdfccc`](#insn-00bdfccc) 範囲 `[['00bdfccc', '00bdfceb']]`
  - `FALL_THROUGH` [`00bdfce8`](#insn-00bdfce8) → [`00bdfcec`](#insn-00bdfcec)
- ブロック [`00bdfcec`](#insn-00bdfcec) 範囲 `[['00bdfcec', '00bdfcef']]`
  - `FALL_THROUGH` [`00bdfcec`](#insn-00bdfcec) → [`00bdfcf0`](#insn-00bdfcf0)
- ブロック [`00bdfcf0`](#insn-00bdfcf0) 範囲 `[['00bdfcf0', '00bdfd03']]`
  - `FALL_THROUGH` [`00bdfd00`](#insn-00bdfd00) → [`00bdfd04`](#insn-00bdfd04)
- ブロック [`00bdfd04`](#insn-00bdfd04) 範囲 `[['00bdfd04', '00bdfd27']]`
  - `FALL_THROUGH` [`00bdfd24`](#insn-00bdfd24) → [`00bdfd28`](#insn-00bdfd28)
- ブロック [`00bdfd28`](#insn-00bdfd28) 範囲 `[['00bdfd28', '00bdfd37']]`
  - `FALL_THROUGH` [`00bdfd34`](#insn-00bdfd34) → [`00bdfd38`](#insn-00bdfd38)
- ブロック [`00bdfd38`](#insn-00bdfd38) 範囲 `[['00bdfd38', '00bdfd3b']]`
  - `FALL_THROUGH` [`00bdfd38`](#insn-00bdfd38) → [`00bdfd3c`](#insn-00bdfd3c)
- ブロック [`00bdfd3c`](#insn-00bdfd3c) 範囲 `[['00bdfd3c', '00bdfd57']]`
  - `FALL_THROUGH` [`00bdfd54`](#insn-00bdfd54) → [`00bdfd58`](#insn-00bdfd58)
- ブロック [`00bdfd58`](#insn-00bdfd58) 範囲 `[['00bdfd58', '00bdfd5b']]`
  - `FALL_THROUGH` [`00bdfd58`](#insn-00bdfd58) → [`00bdfd5c`](#insn-00bdfd5c)
- ブロック [`00bdfd5c`](#insn-00bdfd5c) 範囲 `[['00bdfd5c', '00bdfd6b']]`
  - `FALL_THROUGH` [`00bdfd68`](#insn-00bdfd68) → [`00bdfd6c`](#insn-00bdfd6c)
- ブロック [`00bdfd6c`](#insn-00bdfd6c) 範囲 `[['00bdfd6c', '00bdfd6f']]`
  - `FALL_THROUGH` [`00bdfd6c`](#insn-00bdfd6c) → [`00bdfd70`](#insn-00bdfd70)
- ブロック [`00bdfd70`](#insn-00bdfd70) 範囲 `[['00bdfd70', '00bdfd73']]`
  - `FALL_THROUGH` [`00bdfd70`](#insn-00bdfd70) → [`00bdfd74`](#insn-00bdfd74)
- ブロック [`00bdfd74`](#insn-00bdfd74) 範囲 `[['00bdfd74', '00bdfd7b']]`
  - `FALL_THROUGH` [`00bdfd78`](#insn-00bdfd78) → [`00bdfd7c`](#insn-00bdfd7c)
- ブロック [`00bdfd7c`](#insn-00bdfd7c) 範囲 `[['00bdfd7c', '00bdfd7f']]`
  - `FALL_THROUGH` [`00bdfd7c`](#insn-00bdfd7c) → [`00bdfd80`](#insn-00bdfd80)
- ブロック [`00bdfd80`](#insn-00bdfd80) 範囲 `[['00bdfd80', '00bdfd83']]`
  - `FALL_THROUGH` [`00bdfd80`](#insn-00bdfd80) → [`00bdfd84`](#insn-00bdfd84)
- ブロック [`00bdfd84`](#insn-00bdfd84) 範囲 `[['00bdfd84', '00bdfd87']]`
  - `FALL_THROUGH` [`00bdfd84`](#insn-00bdfd84) → [`00bdfd88`](#insn-00bdfd88)
- ブロック [`00bdfd88`](#insn-00bdfd88) 範囲 `[['00bdfd88', '00bdfd8b']]`
  - `FALL_THROUGH` [`00bdfd88`](#insn-00bdfd88) → [`00bdfd8c`](#insn-00bdfd8c)
- ブロック [`00bdfd8c`](#insn-00bdfd8c) 範囲 `[['00bdfd8c', '00bdfdb3']]`
  - `CONDITIONAL_JUMP` [`00bdfdb0`](#insn-00bdfdb0) → [`00bdfdcc`](#insn-00bdfdcc)
  - `FALL_THROUGH` [`00bdfdb0`](#insn-00bdfdb0) → [`00bdfdb4`](#insn-00bdfdb4)
- ブロック [`00bdfdb4`](#insn-00bdfdb4) 範囲 `[['00bdfdb4', '00bdfdc3']]`
  - `FALL_THROUGH` [`00bdfdc0`](#insn-00bdfdc0) → [`00bdfdc4`](#insn-00bdfdc4)
- ブロック [`00bdfdc4`](#insn-00bdfdc4) 範囲 `[['00bdfdc4', '00bdfdcb']]`
  - `FALL_THROUGH` [`00bdfdc8`](#insn-00bdfdc8) → [`00bdfdcc`](#insn-00bdfdcc)
- ブロック [`00bdfdcc`](#insn-00bdfdcc) 範囲 `[['00bdfdcc', '00bdfdd7']]`
  - `CONDITIONAL_JUMP` [`00bdfdd4`](#insn-00bdfdd4) → [`00bdfe00`](#insn-00bdfe00)
  - `FALL_THROUGH` [`00bdfdd4`](#insn-00bdfdd4) → [`00bdfdd8`](#insn-00bdfdd8)
- ブロック [`00bdfdd8`](#insn-00bdfdd8) 範囲 `[['00bdfdd8', '00bdfddf']]`
  - `CONDITIONAL_JUMP` [`00bdfddc`](#insn-00bdfddc) → [`00bdfe00`](#insn-00bdfe00)
  - `FALL_THROUGH` [`00bdfddc`](#insn-00bdfddc) → [`00bdfde0`](#insn-00bdfde0)
- ブロック [`00bdfde0`](#insn-00bdfde0) 範囲 `[['00bdfde0', '00bdfdf7']]`
  - `CONDITIONAL_JUMP` [`00bdfdf4`](#insn-00bdfdf4) → [`00bdfe10`](#insn-00bdfe10)
  - `FALL_THROUGH` [`00bdfdf4`](#insn-00bdfdf4) → [`00bdfdf8`](#insn-00bdfdf8)
- ブロック [`00bdfdf8`](#insn-00bdfdf8) 範囲 `[['00bdfdf8', '00bdfdfb']]`
  - `FALL_THROUGH` [`00bdfdf8`](#insn-00bdfdf8) → [`00bdfdfc`](#insn-00bdfdfc)
- ブロック [`00bdfdfc`](#insn-00bdfdfc) 範囲 `[['00bdfdfc', '00bdfdff']]`
  - `UNCONDITIONAL_JUMP` [`00bdfdfc`](#insn-00bdfdfc) → [`00bdfe30`](#insn-00bdfe30)
- ブロック [`00bdfe00`](#insn-00bdfe00) 範囲 `[['00bdfe00', '00bdfe0f']]`
  - `CONDITIONAL_JUMP` [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfdf8`](#insn-00bdfdf8)
  - `FALL_THROUGH` [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfe10`](#insn-00bdfe10)
- ブロック [`00bdfe10`](#insn-00bdfe10) 範囲 `[['00bdfe10', '00bdfe23']]`
  - `CONDITIONAL_JUMP` [`00bdfe20`](#insn-00bdfe20) → [`00bdfe30`](#insn-00bdfe30)
  - `FALL_THROUGH` [`00bdfe20`](#insn-00bdfe20) → [`00bdfe24`](#insn-00bdfe24)
- ブロック [`00bdfe24`](#insn-00bdfe24) 範囲 `[['00bdfe24', '00bdfe2f']]`
  - `FALL_THROUGH` [`00bdfe2c`](#insn-00bdfe2c) → [`00bdfe30`](#insn-00bdfe30)
- ブロック [`00bdfe30`](#insn-00bdfe30) 範囲 `[['00bdfe30', '00bdfe33']]`
  - `FALL_THROUGH` [`00bdfe30`](#insn-00bdfe30) → [`00bdfe34`](#insn-00bdfe34)
- ブロック [`00bdfe34`](#insn-00bdfe34) 範囲 `[['00bdfe34', '00bdfe37']]`
  - `FALL_THROUGH` [`00bdfe34`](#insn-00bdfe34) → [`00bdfe38`](#insn-00bdfe38)
- ブロック [`00bdfe38`](#insn-00bdfe38) 範囲 `[['00bdfe38', '00bdfe53']]`
  - `CONDITIONAL_JUMP` [`00bdfe50`](#insn-00bdfe50) → [`00bdfe6c`](#insn-00bdfe6c)
  - `FALL_THROUGH` [`00bdfe50`](#insn-00bdfe50) → [`00bdfe54`](#insn-00bdfe54)
- ブロック [`00bdfe54`](#insn-00bdfe54) 範囲 `[['00bdfe54', '00bdfe6b']]`
  - `FALL_THROUGH` [`00bdfe68`](#insn-00bdfe68) → [`00bdfe6c`](#insn-00bdfe6c)
- ブロック [`00bdfe6c`](#insn-00bdfe6c) 範囲 `[['00bdfe6c', '00bdfe6f']]`
  - `FALL_THROUGH` [`00bdfe6c`](#insn-00bdfe6c) → [`00bdfe70`](#insn-00bdfe70)
- ブロック [`00bdfe70`](#insn-00bdfe70) 範囲 `[['00bdfe70', '00bdfe77']]`
  - `CONDITIONAL_JUMP` [`00bdfe74`](#insn-00bdfe74) → [`00bdfea0`](#insn-00bdfea0)
  - `FALL_THROUGH` [`00bdfe74`](#insn-00bdfe74) → [`00bdfe78`](#insn-00bdfe78)
- ブロック [`00bdfe78`](#insn-00bdfe78) 範囲 `[['00bdfe78', '00bdfe7f']]`
  - `CONDITIONAL_JUMP` [`00bdfe7c`](#insn-00bdfe7c) → [`00bdfea0`](#insn-00bdfea0)
  - `FALL_THROUGH` [`00bdfe7c`](#insn-00bdfe7c) → [`00bdfe80`](#insn-00bdfe80)
- ブロック [`00bdfe80`](#insn-00bdfe80) 範囲 `[['00bdfe80', '00bdfe97']]`
  - `CONDITIONAL_JUMP` [`00bdfe94`](#insn-00bdfe94) → [`00bdfeb0`](#insn-00bdfeb0)
  - `FALL_THROUGH` [`00bdfe94`](#insn-00bdfe94) → [`00bdfe98`](#insn-00bdfe98)
- ブロック [`00bdfe98`](#insn-00bdfe98) 範囲 `[['00bdfe98', '00bdfe9f']]`
  - `UNCONDITIONAL_JUMP` [`00bdfe9c`](#insn-00bdfe9c) → [`00bdfed0`](#insn-00bdfed0)
- ブロック [`00bdfea0`](#insn-00bdfea0) 範囲 `[['00bdfea0', '00bdfeaf']]`
  - `CONDITIONAL_JUMP` [`00bdfeac`](#insn-00bdfeac) → [`00bdfe98`](#insn-00bdfe98)
  - `FALL_THROUGH` [`00bdfeac`](#insn-00bdfeac) → [`00bdfeb0`](#insn-00bdfeb0)
- ブロック [`00bdfeb0`](#insn-00bdfeb0) 範囲 `[['00bdfeb0', '00bdfec3']]`
  - `CONDITIONAL_JUMP` [`00bdfec0`](#insn-00bdfec0) → [`00bdfed0`](#insn-00bdfed0)
  - `FALL_THROUGH` [`00bdfec0`](#insn-00bdfec0) → [`00bdfec4`](#insn-00bdfec4)
- ブロック [`00bdfec4`](#insn-00bdfec4) 範囲 `[['00bdfec4', '00bdfecf']]`
  - `FALL_THROUGH` [`00bdfecc`](#insn-00bdfecc) → [`00bdfed0`](#insn-00bdfed0)
- ブロック [`00bdfed0`](#insn-00bdfed0) 範囲 `[['00bdfed0', '00bdfedb']]`
  - `FALL_THROUGH` [`00bdfed8`](#insn-00bdfed8) → [`00bdfedc`](#insn-00bdfedc)
- ブロック [`00bdfedc`](#insn-00bdfedc) 範囲 `[['00bdfedc', '00bdfeeb']]`
  - `FALL_THROUGH` [`00bdfee8`](#insn-00bdfee8) → [`00bdfeec`](#insn-00bdfeec)
- ブロック [`00bdfeec`](#insn-00bdfeec) 範囲 `[['00bdfeec', '00bdfef7']]`
  - `CONDITIONAL_JUMP` [`00bdfef4`](#insn-00bdfef4) → [`00bdff10`](#insn-00bdff10)
  - `FALL_THROUGH` [`00bdfef4`](#insn-00bdfef4) → [`00bdfef8`](#insn-00bdfef8)
- ブロック [`00bdfef8`](#insn-00bdfef8) 範囲 `[['00bdfef8', '00bdff0f']]`
  - `FALL_THROUGH` [`00bdff0c`](#insn-00bdff0c) → [`00bdff10`](#insn-00bdff10)
- ブロック [`00bdff10`](#insn-00bdff10) 範囲 `[['00bdff10', '00bdff1b']]`
  - `CONDITIONAL_JUMP` [`00bdff18`](#insn-00bdff18) → [`00bdff44`](#insn-00bdff44)
  - `FALL_THROUGH` [`00bdff18`](#insn-00bdff18) → [`00bdff1c`](#insn-00bdff1c)
- ブロック [`00bdff1c`](#insn-00bdff1c) 範囲 `[['00bdff1c', '00bdff23']]`
  - `CONDITIONAL_JUMP` [`00bdff20`](#insn-00bdff20) → [`00bdff44`](#insn-00bdff44)
  - `FALL_THROUGH` [`00bdff20`](#insn-00bdff20) → [`00bdff24`](#insn-00bdff24)
- ブロック [`00bdff24`](#insn-00bdff24) 範囲 `[['00bdff24', '00bdff27']]`
  - `FALL_THROUGH` [`00bdff24`](#insn-00bdff24) → [`00bdff28`](#insn-00bdff28)
- ブロック [`00bdff28`](#insn-00bdff28) 範囲 `[['00bdff28', '00bdff2b']]`
  - `FALL_THROUGH` [`00bdff28`](#insn-00bdff28) → [`00bdff2c`](#insn-00bdff2c)
- ブロック [`00bdff2c`](#insn-00bdff2c) 範囲 `[['00bdff2c', '00bdff2f']]`
  - `FALL_THROUGH` [`00bdff2c`](#insn-00bdff2c) → [`00bdff30`](#insn-00bdff30)
- ブロック [`00bdff30`](#insn-00bdff30) 範囲 `[['00bdff30', '00bdff3b']]`
  - `CONDITIONAL_JUMP` [`00bdff38`](#insn-00bdff38) → [`00bdff54`](#insn-00bdff54)
  - `FALL_THROUGH` [`00bdff38`](#insn-00bdff38) → [`00bdff3c`](#insn-00bdff3c)
- ブロック [`00bdff3c`](#insn-00bdff3c) 範囲 `[['00bdff3c', '00bdff43']]`
  - `UNCONDITIONAL_JUMP` [`00bdff40`](#insn-00bdff40) → [`00bdff74`](#insn-00bdff74)
- ブロック [`00bdff44`](#insn-00bdff44) 範囲 `[['00bdff44', '00bdff53']]`
  - `CONDITIONAL_JUMP` [`00bdff50`](#insn-00bdff50) → [`00bdff3c`](#insn-00bdff3c)
  - `FALL_THROUGH` [`00bdff50`](#insn-00bdff50) → [`00bdff54`](#insn-00bdff54)
- ブロック [`00bdff54`](#insn-00bdff54) 範囲 `[['00bdff54', '00bdff57']]`
  - `FALL_THROUGH` [`00bdff54`](#insn-00bdff54) → [`00bdff58`](#insn-00bdff58)
- ブロック [`00bdff58`](#insn-00bdff58) 範囲 `[['00bdff58', '00bdff67']]`
  - `CONDITIONAL_JUMP` [`00bdff64`](#insn-00bdff64) → [`00bdff74`](#insn-00bdff74)
  - `FALL_THROUGH` [`00bdff64`](#insn-00bdff64) → [`00bdff68`](#insn-00bdff68)
- ブロック [`00bdff68`](#insn-00bdff68) 範囲 `[['00bdff68', '00bdff73']]`
  - `FALL_THROUGH` [`00bdff70`](#insn-00bdff70) → [`00bdff74`](#insn-00bdff74)
- ブロック [`00bdff74`](#insn-00bdff74) 範囲 `[['00bdff74', '00bdff97']]`
  - `CONDITIONAL_JUMP` [`00bdff94`](#insn-00bdff94) → [`00bdffb0`](#insn-00bdffb0)
  - `FALL_THROUGH` [`00bdff94`](#insn-00bdff94) → [`00bdff98`](#insn-00bdff98)
- ブロック [`00bdff98`](#insn-00bdff98) 範囲 `[['00bdff98', '00bdff9b']]`
  - `FALL_THROUGH` [`00bdff98`](#insn-00bdff98) → [`00bdff9c`](#insn-00bdff9c)
- ブロック [`00bdff9c`](#insn-00bdff9c) 範囲 `[['00bdff9c', '00bdffaf']]`
  - `FALL_THROUGH` [`00bdffac`](#insn-00bdffac) → [`00bdffb0`](#insn-00bdffb0)
- ブロック [`00bdffb0`](#insn-00bdffb0) 範囲 `[['00bdffb0', '00bdffbb']]`
  - `CONDITIONAL_JUMP` [`00bdffb8`](#insn-00bdffb8) → [`00bdffe4`](#insn-00bdffe4)
  - `FALL_THROUGH` [`00bdffb8`](#insn-00bdffb8) → [`00bdffbc`](#insn-00bdffbc)
- ブロック [`00bdffbc`](#insn-00bdffbc) 範囲 `[['00bdffbc', '00bdffc3']]`
  - `CONDITIONAL_JUMP` [`00bdffc0`](#insn-00bdffc0) → [`00bdffe4`](#insn-00bdffe4)
  - `FALL_THROUGH` [`00bdffc0`](#insn-00bdffc0) → [`00bdffc4`](#insn-00bdffc4)
- ブロック [`00bdffc4`](#insn-00bdffc4) 範囲 `[['00bdffc4', '00bdffcb']]`
  - `FALL_THROUGH` [`00bdffc8`](#insn-00bdffc8) → [`00bdffcc`](#insn-00bdffcc)
- ブロック [`00bdffcc`](#insn-00bdffcc) 範囲 `[['00bdffcc', '00bdffd3']]`
  - `FALL_THROUGH` [`00bdffd0`](#insn-00bdffd0) → [`00bdffd4`](#insn-00bdffd4)
- ブロック [`00bdffd4`](#insn-00bdffd4) 範囲 `[['00bdffd4', '00bdffd7']]`
  - `FALL_THROUGH` [`00bdffd4`](#insn-00bdffd4) → [`00bdffd8`](#insn-00bdffd8)
- ブロック [`00bdffd8`](#insn-00bdffd8) 範囲 `[['00bdffd8', '00bdffdb']]`
  - `CONDITIONAL_JUMP` [`00bdffd8`](#insn-00bdffd8) → [`00bdfff4`](#insn-00bdfff4)
  - `FALL_THROUGH` [`00bdffd8`](#insn-00bdffd8) → [`00bdffdc`](#insn-00bdffdc)
- ブロック [`00bdffdc`](#insn-00bdffdc) 範囲 `[['00bdffdc', '00bdffe3']]`
  - `UNCONDITIONAL_JUMP` [`00bdffe0`](#insn-00bdffe0) → [`00be0014`](#insn-00be0014)
- ブロック [`00bdffe4`](#insn-00bdffe4) 範囲 `[['00bdffe4', '00bdffe7']]`
  - `FALL_THROUGH` [`00bdffe4`](#insn-00bdffe4) → [`00bdffe8`](#insn-00bdffe8)
- ブロック [`00bdffe8`](#insn-00bdffe8) 範囲 `[['00bdffe8', '00bdfff3']]`
  - `CONDITIONAL_JUMP` [`00bdfff0`](#insn-00bdfff0) → [`00bdffdc`](#insn-00bdffdc)
  - `FALL_THROUGH` [`00bdfff0`](#insn-00bdfff0) → [`00bdfff4`](#insn-00bdfff4)
- ブロック [`00bdfff4`](#insn-00bdfff4) 範囲 `[['00bdfff4', '00be0007']]`
  - `CONDITIONAL_JUMP` [`00be0004`](#insn-00be0004) → [`00be0014`](#insn-00be0014)
  - `FALL_THROUGH` [`00be0004`](#insn-00be0004) → [`00be0008`](#insn-00be0008)
- ブロック [`00be0008`](#insn-00be0008) 範囲 `[['00be0008', '00be0013']]`
  - `FALL_THROUGH` [`00be0010`](#insn-00be0010) → [`00be0014`](#insn-00be0014)
- ブロック [`00be0014`](#insn-00be0014) 範囲 `[['00be0014', '00be002f']]`
  - `FALL_THROUGH` [`00be002c`](#insn-00be002c) → [`00be0030`](#insn-00be0030)
- ブロック [`00be0030`](#insn-00be0030) 範囲 `[['00be0030', '00be0033']]`
  - `FALL_THROUGH` [`00be0030`](#insn-00be0030) → [`00be0034`](#insn-00be0034)
- ブロック [`00be0034`](#insn-00be0034) 範囲 `[['00be0034', '00be0037']]`
  - `CONDITIONAL_JUMP` [`00be0034`](#insn-00be0034) → [`00be0050`](#insn-00be0050)
  - `FALL_THROUGH` [`00be0034`](#insn-00be0034) → [`00be0038`](#insn-00be0038)
- ブロック [`00be0038`](#insn-00be0038) 範囲 `[['00be0038', '00be004b']]`
  - `FALL_THROUGH` [`00be0048`](#insn-00be0048) → [`00be004c`](#insn-00be004c)
- ブロック [`00be004c`](#insn-00be004c) 範囲 `[['00be004c', '00be004f']]`
  - `FALL_THROUGH` [`00be004c`](#insn-00be004c) → [`00be0050`](#insn-00be0050)
- ブロック [`00be0050`](#insn-00be0050) 範囲 `[['00be0050', '00be005b']]`
  - `CONDITIONAL_JUMP` [`00be0058`](#insn-00be0058) → [`00be0084`](#insn-00be0084)
  - `FALL_THROUGH` [`00be0058`](#insn-00be0058) → [`00be005c`](#insn-00be005c)
- ブロック [`00be005c`](#insn-00be005c) 範囲 `[['00be005c', '00be0063']]`
  - `CONDITIONAL_JUMP` [`00be0060`](#insn-00be0060) → [`00be0084`](#insn-00be0084)
  - `FALL_THROUGH` [`00be0060`](#insn-00be0060) → [`00be0064`](#insn-00be0064)
- ブロック [`00be0064`](#insn-00be0064) 範囲 `[['00be0064', '00be0073']]`
  - `FALL_THROUGH` [`00be0070`](#insn-00be0070) → [`00be0074`](#insn-00be0074)
- ブロック [`00be0074`](#insn-00be0074) 範囲 `[['00be0074', '00be007b']]`
  - `CONDITIONAL_JUMP` [`00be0078`](#insn-00be0078) → [`00be0094`](#insn-00be0094)
  - `FALL_THROUGH` [`00be0078`](#insn-00be0078) → [`00be007c`](#insn-00be007c)
- ブロック [`00be007c`](#insn-00be007c) 範囲 `[['00be007c', '00be0083']]`
  - `UNCONDITIONAL_JUMP` [`00be0080`](#insn-00be0080) → [`00be00b4`](#insn-00be00b4)
- ブロック [`00be0084`](#insn-00be0084) 範囲 `[['00be0084', '00be008b']]`
  - `FALL_THROUGH` [`00be0088`](#insn-00be0088) → [`00be008c`](#insn-00be008c)
- ブロック [`00be008c`](#insn-00be008c) 範囲 `[['00be008c', '00be008f']]`
  - `FALL_THROUGH` [`00be008c`](#insn-00be008c) → [`00be0090`](#insn-00be0090)
- ブロック [`00be0090`](#insn-00be0090) 範囲 `[['00be0090', '00be0093']]`
  - `CONDITIONAL_JUMP` [`00be0090`](#insn-00be0090) → [`00be007c`](#insn-00be007c)
  - `FALL_THROUGH` [`00be0090`](#insn-00be0090) → [`00be0094`](#insn-00be0094)
- ブロック [`00be0094`](#insn-00be0094) 範囲 `[['00be0094', '00be0097']]`
  - `FALL_THROUGH` [`00be0094`](#insn-00be0094) → [`00be0098`](#insn-00be0098)
- ブロック [`00be0098`](#insn-00be0098) 範囲 `[['00be0098', '00be009b']]`
  - `FALL_THROUGH` [`00be0098`](#insn-00be0098) → [`00be009c`](#insn-00be009c)
- ブロック [`00be009c`](#insn-00be009c) 範囲 `[['00be009c', '00be009f']]`
  - `FALL_THROUGH` [`00be009c`](#insn-00be009c) → [`00be00a0`](#insn-00be00a0)
- ブロック [`00be00a0`](#insn-00be00a0) 範囲 `[['00be00a0', '00be00a7']]`
  - `CONDITIONAL_JUMP` [`00be00a4`](#insn-00be00a4) → [`00be00b4`](#insn-00be00b4)
  - `FALL_THROUGH` [`00be00a4`](#insn-00be00a4) → [`00be00a8`](#insn-00be00a8)
- ブロック [`00be00a8`](#insn-00be00a8) 範囲 `[['00be00a8', '00be00af']]`
  - `FALL_THROUGH` [`00be00ac`](#insn-00be00ac) → [`00be00b0`](#insn-00be00b0)
- ブロック [`00be00b0`](#insn-00be00b0) 範囲 `[['00be00b0', '00be00b3']]`
  - `FALL_THROUGH` [`00be00b0`](#insn-00be00b0) → [`00be00b4`](#insn-00be00b4)
- ブロック [`00be00b4`](#insn-00be00b4) 範囲 `[['00be00b4', '00be00b7']]`
  - `FALL_THROUGH` [`00be00b4`](#insn-00be00b4) → [`00be00b8`](#insn-00be00b8)
- ブロック [`00be00b8`](#insn-00be00b8) 範囲 `[['00be00b8', '00be00bb']]`
  - `FALL_THROUGH` [`00be00b8`](#insn-00be00b8) → [`00be00bc`](#insn-00be00bc)
- ブロック [`00be00bc`](#insn-00be00bc) 範囲 `[['00be00bc', '00be00bf']]`
  - `FALL_THROUGH` [`00be00bc`](#insn-00be00bc) → [`00be00c0`](#insn-00be00c0)
- ブロック [`00be00c0`](#insn-00be00c0) 範囲 `[['00be00c0', '00be00c3']]`
  - `FALL_THROUGH` [`00be00c0`](#insn-00be00c0) → [`00be00c4`](#insn-00be00c4)
- ブロック [`00be00c4`](#insn-00be00c4) 範囲 `[['00be00c4', '00be00d7']]`
  - `CONDITIONAL_JUMP` [`00be00d4`](#insn-00be00d4) → [`00be00f0`](#insn-00be00f0)
  - `FALL_THROUGH` [`00be00d4`](#insn-00be00d4) → [`00be00d8`](#insn-00be00d8)
- ブロック [`00be00d8`](#insn-00be00d8) 範囲 `[['00be00d8', '00be00ef']]`
  - `FALL_THROUGH` [`00be00ec`](#insn-00be00ec) → [`00be00f0`](#insn-00be00f0)
- ブロック [`00be00f0`](#insn-00be00f0) 範囲 `[['00be00f0', '00be00fb']]`
  - `CONDITIONAL_JUMP` [`00be00f8`](#insn-00be00f8) → [`00be0124`](#insn-00be0124)
  - `FALL_THROUGH` [`00be00f8`](#insn-00be00f8) → [`00be00fc`](#insn-00be00fc)
- ブロック [`00be00fc`](#insn-00be00fc) 範囲 `[['00be00fc', '00be0103']]`
  - `CONDITIONAL_JUMP` [`00be0100`](#insn-00be0100) → [`00be0124`](#insn-00be0124)
  - `FALL_THROUGH` [`00be0100`](#insn-00be0100) → [`00be0104`](#insn-00be0104)
- ブロック [`00be0104`](#insn-00be0104) 範囲 `[['00be0104', '00be011b']]`
  - `CONDITIONAL_JUMP` [`00be0118`](#insn-00be0118) → [`00be0134`](#insn-00be0134)
  - `FALL_THROUGH` [`00be0118`](#insn-00be0118) → [`00be011c`](#insn-00be011c)
- ブロック [`00be011c`](#insn-00be011c) 範囲 `[['00be011c', '00be0123']]`
  - `UNCONDITIONAL_JUMP` [`00be0120`](#insn-00be0120) → [`00be0154`](#insn-00be0154)
- ブロック [`00be0124`](#insn-00be0124) 範囲 `[['00be0124', '00be0133']]`
  - `CONDITIONAL_JUMP` [`00be0130`](#insn-00be0130) → [`00be011c`](#insn-00be011c)
  - `FALL_THROUGH` [`00be0130`](#insn-00be0130) → [`00be0134`](#insn-00be0134)
- ブロック [`00be0134`](#insn-00be0134) 範囲 `[['00be0134', '00be0147']]`
  - `CONDITIONAL_JUMP` [`00be0144`](#insn-00be0144) → [`00be0154`](#insn-00be0154)
  - `FALL_THROUGH` [`00be0144`](#insn-00be0144) → [`00be0148`](#insn-00be0148)
- ブロック [`00be0148`](#insn-00be0148) 範囲 `[['00be0148', '00be0153']]`
  - `FALL_THROUGH` [`00be0150`](#insn-00be0150) → [`00be0154`](#insn-00be0154)
- ブロック [`00be0154`](#insn-00be0154) 範囲 `[['00be0154', '00be016f']]`
  - `CONDITIONAL_JUMP` [`00be016c`](#insn-00be016c) → [`00be0188`](#insn-00be0188)
  - `FALL_THROUGH` [`00be016c`](#insn-00be016c) → [`00be0170`](#insn-00be0170)
- ブロック [`00be0170`](#insn-00be0170) 範囲 `[['00be0170', '00be0187']]`
  - `UNCONDITIONAL_JUMP` [`00be0184`](#insn-00be0184) → [`00be0194`](#insn-00be0194)
- ブロック [`00be0188`](#insn-00be0188) 範囲 `[['00be0188', '00be0193']]`
  - `FALL_THROUGH` [`00be0190`](#insn-00be0190) → [`00be0194`](#insn-00be0194)
- ブロック [`00be0194`](#insn-00be0194) 範囲 `[['00be0194', '00be01e3']]`
  - `CONDITIONAL_JUMP` [`00be01e0`](#insn-00be01e0) → [`00bdfd04`](#insn-00bdfd04)
  - `FALL_THROUGH` [`00be01e0`](#insn-00be01e0) → [`00be01e4`](#insn-00be01e4)
- ブロック [`00be01e4`](#insn-00be01e4) 範囲 `[['00be01e4', '00be01f3']]`
  - `FALL_THROUGH` [`00be01f0`](#insn-00be01f0) → [`00be01f4`](#insn-00be01f4)
- ブロック [`00be01f4`](#insn-00be01f4) 範囲 `[['00be01f4', '00be0207']]`
  - `CONDITIONAL_JUMP` [`00be0204`](#insn-00be0204) → [`00be0228`](#insn-00be0228)
  - `FALL_THROUGH` [`00be0204`](#insn-00be0204) → [`00be0208`](#insn-00be0208)
- ブロック [`00be0208`](#insn-00be0208) 範囲 `[['00be0208', '00be0227']]`
- ブロック [`00be0228`](#insn-00be0228) 範囲 `[['00be0228', '00be022b']]`

## 命令位置別の参照

- [`00bdfc0c`](#insn-00bdfc0c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc10`](#insn-00bdfc10) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc14`](#insn-00bdfc14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc18`](#insn-00bdfc18) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc1c`](#insn-00bdfc1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc20`](#insn-00bdfc20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc34`](#insn-00bdfc34) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc3c`](#insn-00bdfc3c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc4c`](#insn-00bdfc4c) → `Stack[-0x1d0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc50`](#insn-00bdfc50) → [`00be01f4`](#insn-00be01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc58`](#insn-00bdfc58) → [`00be01f4`](#insn-00be01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc60`](#insn-00bdfc60) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc64`](#insn-00bdfc64) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc6c`](#insn-00bdfc6c) → `01127e00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfc78`](#insn-00bdfc78) → `Stack[-0x1d8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc7c`](#insn-00bdfc7c) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc80`](#insn-00bdfc80) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc84`](#insn-00bdfc84) → [`00be01f4`](#insn-00be01f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc8c`](#insn-00bdfc8c) → [`00c5c5c0`](../00c5c/00c5c5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc94`](#insn-00bdfc94) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfc98`](#insn-00bdfc98) → [`00576618`](../00576/00576618.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00576618` · 推定シンボル `None` · 推定型 `None`
- [`00bdfca8`](#insn-00bdfca8) → [`00c5ef70`](../00c5e/00c5ef70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ef70` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcb0`](#insn-00bdfcb0) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcb4`](#insn-00bdfcb4) → [`00be01e4`](#insn-00be01e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcbc`](#insn-00bdfcbc) → `00c9cb00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcc4`](#insn-00bdfcc4) → `00c9ca68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcd8`](#insn-00bdfcd8) → `Stack[-0x200]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfcf8`](#insn-00bdfcf8) → `00c939b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdfcf8`](#insn-00bdfcf8) → `Stack[-0x1f0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd00`](#insn-00bdfd00) → `00c93a18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdfd00`](#insn-00bdfd00) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd08`](#insn-00bdfd08) → [`00c5c5c0`](../00c5c/00c5c5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd10`](#insn-00bdfd10) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd18`](#insn-00bdfd18) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd1c`](#insn-00bdfd1c) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd20`](#insn-00bdfd20) → `Stack[-0x1f0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd30`](#insn-00bdfd30) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd34`](#insn-00bdfd34) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd38`](#insn-00bdfd38) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd3c`](#insn-00bdfd3c) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd40`](#insn-00bdfd40) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd44`](#insn-00bdfd44) → `00c939b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdfd44`](#insn-00bdfd44) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd48`](#insn-00bdfd48) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd50`](#insn-00bdfd50) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd68`](#insn-00bdfd68) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd80`](#insn-00bdfd80) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd88`](#insn-00bdfd88) → `00c93a18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdfd88`](#insn-00bdfd88) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd8c`](#insn-00bdfd8c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd90`](#insn-00bdfd90) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd94`](#insn-00bdfd94) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd98`](#insn-00bdfd98) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfd9c`](#insn-00bdfd9c) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfda0`](#insn-00bdfda0) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfda8`](#insn-00bdfda8) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdb0`](#insn-00bdfdb0) → [`00bdfdcc`](#insn-00bdfdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdb8`](#insn-00bdfdb8) → `01127e80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfdc4`](#insn-00bdfdc4) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdd0`](#insn-00bdfdd0) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdd4`](#insn-00bdfdd4) → [`00bdfe00`](#insn-00bdfe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfddc`](#insn-00bdfddc) → [`00bdfe00`](#insn-00bdfe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdec`](#insn-00bdfdec) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdf0`](#insn-00bdfdf0) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdf4`](#insn-00bdfdf4) → [`00bdfe10`](#insn-00bdfe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdf8`](#insn-00bdfdf8) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfdfc`](#insn-00bdfdfc) → [`00bdfe30`](#insn-00bdfe30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe00`](#insn-00bdfe00) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe04`](#insn-00bdfe04) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe08`](#insn-00bdfe08) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe0c`](#insn-00bdfe0c) → [`00bdfdf8`](#insn-00bdfdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe10`](#insn-00bdfe10) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe18`](#insn-00bdfe18) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe1c`](#insn-00bdfe1c) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe20`](#insn-00bdfe20) → [`00bdfe30`](#insn-00bdfe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe24`](#insn-00bdfe24) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe28`](#insn-00bdfe28) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe2c`](#insn-00bdfe2c) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe30`](#insn-00bdfe30) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe34`](#insn-00bdfe34) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe38`](#insn-00bdfe38) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe3c`](#insn-00bdfe3c) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe40`](#insn-00bdfe40) → `Stack[-0x1a8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe48`](#insn-00bdfe48) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe50`](#insn-00bdfe50) → [`00bdfe6c`](#insn-00bdfe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe58`](#insn-00bdfe58) → `01127ea8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdfe64`](#insn-00bdfe64) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe70`](#insn-00bdfe70) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe74`](#insn-00bdfe74) → [`00bdfea0`](#insn-00bdfea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe7c`](#insn-00bdfe7c) → [`00bdfea0`](#insn-00bdfea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe8c`](#insn-00bdfe8c) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe90`](#insn-00bdfe90) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe94`](#insn-00bdfe94) → [`00bdfeb0`](#insn-00bdfeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe98`](#insn-00bdfe98) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfe9c`](#insn-00bdfe9c) → [`00bdfed0`](#insn-00bdfed0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea0`](#insn-00bdfea0) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea4`](#insn-00bdfea4) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfea8`](#insn-00bdfea8) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeac`](#insn-00bdfeac) → [`00bdfe98`](#insn-00bdfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeb0`](#insn-00bdfeb0) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeb8`](#insn-00bdfeb8) → `Stack[-0x190]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfebc`](#insn-00bdfebc) → `Stack[-0x188]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfec0`](#insn-00bdfec0) → [`00bdfed0`](#insn-00bdfed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfec4`](#insn-00bdfec4) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfec8`](#insn-00bdfec8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bdfecc`](#insn-00bdfecc) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfed0`](#insn-00bdfed0) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfed4`](#insn-00bdfed4) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfed8`](#insn-00bdfed8) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfedc`](#insn-00bdfedc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfee0`](#insn-00bdfee0) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfee4`](#insn-00bdfee4) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfeec`](#insn-00bdfeec) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdfef4`](#insn-00bdfef4) → [`00bdff10`](#insn-00bdff10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfefc`](#insn-00bdfefc) → `01127e90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdff08`](#insn-00bdff08) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdff14`](#insn-00bdff14) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdff18`](#insn-00bdff18) → [`00bdff44`](#insn-00bdff44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff20`](#insn-00bdff20) → [`00bdff44`](#insn-00bdff44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff30`](#insn-00bdff30) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00bdff34`](#insn-00bdff34) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff38`](#insn-00bdff38) → [`00bdff54`](#insn-00bdff54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff3c`](#insn-00bdff3c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff40`](#insn-00bdff40) → [`00bdff74`](#insn-00bdff74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff44`](#insn-00bdff44) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff48`](#insn-00bdff48) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff4c`](#insn-00bdff4c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff50`](#insn-00bdff50) → [`00bdff3c`](#insn-00bdff3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff54`](#insn-00bdff54) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff5c`](#insn-00bdff5c) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff60`](#insn-00bdff60) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff64`](#insn-00bdff64) → [`00bdff74`](#insn-00bdff74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff68`](#insn-00bdff68) → `Stack[-0x168]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff6c`](#insn-00bdff6c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bdff70`](#insn-00bdff70) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff74`](#insn-00bdff74) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff78`](#insn-00bdff78) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff7c`](#insn-00bdff7c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff80`](#insn-00bdff80) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff84`](#insn-00bdff84) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff8c`](#insn-00bdff8c) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdff94`](#insn-00bdff94) → [`00bdffb0`](#insn-00bdffb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdff9c`](#insn-00bdff9c) → `01127ea0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdffa8`](#insn-00bdffa8) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb4`](#insn-00bdffb4) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdffb8`](#insn-00bdffb8) → [`00bdffe4`](#insn-00bdffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffc0`](#insn-00bdffc0) → [`00bdffe4`](#insn-00bdffe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffd0`](#insn-00bdffd0) → [`00c5c390`](../00c5c/00c5c390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c390` · 推定シンボル `None` · 推定型 `None`
- [`00bdffd4`](#insn-00bdffd4) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffd8`](#insn-00bdffd8) → [`00bdfff4`](#insn-00bdfff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffdc`](#insn-00bdffdc) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffe0`](#insn-00bdffe0) → [`00be0014`](#insn-00be0014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffe4`](#insn-00bdffe4) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffe8`](#insn-00bdffe8) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdffec`](#insn-00bdffec) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfff0`](#insn-00bdfff0) → [`00bdffdc`](#insn-00bdffdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfff4`](#insn-00bdfff4) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdfffc`](#insn-00bdfffc) → `Stack[-0x160]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0000`](#insn-00be0000) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0004`](#insn-00be0004) → [`00be0014`](#insn-00be0014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0008`](#insn-00be0008) → `Stack[-0x150]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be000c`](#insn-00be000c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00be0010`](#insn-00be0010) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0014`](#insn-00be0014) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0018`](#insn-00be0018) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be001c`](#insn-00be001c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0020`](#insn-00be0020) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0024`](#insn-00be0024) → `Stack[-0x160]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be002c`](#insn-00be002c) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00be0034`](#insn-00be0034) → [`00be0050`](#insn-00be0050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be003c`](#insn-00be003c) → `01127e88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00be0048`](#insn-00be0048) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00be0054`](#insn-00be0054) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00be0058`](#insn-00be0058) → [`00be0084`](#insn-00be0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0060`](#insn-00be0060) → [`00be0084`](#insn-00be0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0070`](#insn-00be0070) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00be0074`](#insn-00be0074) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0078`](#insn-00be0078) → [`00be0094`](#insn-00be0094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be007c`](#insn-00be007c) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0080`](#insn-00be0080) → [`00be00b4`](#insn-00be00b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0084`](#insn-00be0084) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0088`](#insn-00be0088) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be008c`](#insn-00be008c) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0090`](#insn-00be0090) → [`00be007c`](#insn-00be007c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0094`](#insn-00be0094) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be009c`](#insn-00be009c) → `Stack[-0x148]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00a0`](#insn-00be00a0) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00a4`](#insn-00be00a4) → [`00be00b4`](#insn-00be00b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00a8`](#insn-00be00a8) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00ac`](#insn-00be00ac) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00be00b0`](#insn-00be00b0) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00b4`](#insn-00be00b4) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00b8`](#insn-00be00b8) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00bc`](#insn-00be00bc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00c0`](#insn-00be00c0) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00c4`](#insn-00be00c4) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00cc`](#insn-00be00cc) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00be00d4`](#insn-00be00d4) → [`00be00f0`](#insn-00be00f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be00dc`](#insn-00be00dc) → `01127e98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00be00e8`](#insn-00be00e8) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00be00f4`](#insn-00be00f4) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00be00f8`](#insn-00be00f8) → [`00be0124`](#insn-00be0124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0100`](#insn-00be0100) → [`00be0124`](#insn-00be0124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0110`](#insn-00be0110) → [`00c5c430`](../00c5c/00c5c430.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c430` · 推定シンボル `None` · 推定型 `None`
- [`00be0114`](#insn-00be0114) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0118`](#insn-00be0118) → [`00be0134`](#insn-00be0134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be011c`](#insn-00be011c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0120`](#insn-00be0120) → [`00be0154`](#insn-00be0154) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0124`](#insn-00be0124) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0128`](#insn-00be0128) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be012c`](#insn-00be012c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0130`](#insn-00be0130) → [`00be011c`](#insn-00be011c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0134`](#insn-00be0134) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be013c`](#insn-00be013c) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0140`](#insn-00be0140) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0144`](#insn-00be0144) → [`00be0154`](#insn-00be0154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0148`](#insn-00be0148) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be014c`](#insn-00be014c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00be0150`](#insn-00be0150) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0158`](#insn-00be0158) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be015c`](#insn-00be015c) → `Stack[-0x1c8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0164`](#insn-00be0164) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0168`](#insn-00be0168) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be016c`](#insn-00be016c) → [`00be0188`](#insn-00be0188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0178`](#insn-00be0178) → [`00c5ef40`](../00c5e/00c5ef40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ef40` · 推定シンボル `None` · 推定型 `None`
- [`00be0184`](#insn-00be0184) → [`00be0194`](#insn-00be0194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0190`](#insn-00be0190) → [`00c5ef60`](../00c5e/00c5ef60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ef60` · 推定シンボル `None` · 推定型 `None`
- [`00be0198`](#insn-00be0198) → [`00c5ec10`](../00c5e/00c5ec10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec10` · 推定シンボル `None` · 推定型 `None`
- [`00be01a0`](#insn-00be01a0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01a4`](#insn-00be01a4) → `00c9cb00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00be01ac`](#insn-00be01ac) → `00c939b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00be01ac`](#insn-00be01ac) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01b4`](#insn-00be01b4) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00be01bc`](#insn-00be01bc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01cc`](#insn-00be01cc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01d0`](#insn-00be01d0) → [`00c5ec20`](../00c5e/00c5ec20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec20` · 推定シンボル `None` · 推定型 `None`
- [`00be01d4`](#insn-00be01d4) → `Stack[-0x1e8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01e0`](#insn-00be01e0) → [`00bdfd04`](#insn-00bdfd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01e4`](#insn-00be01e4) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01f4`](#insn-00be01f4) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be01fc`](#insn-00be01fc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0204`](#insn-00be0204) → [`00be0228`](#insn-00be0228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be020c`](#insn-00be020c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0210`](#insn-00be0210) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0214`](#insn-00be0214) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0218`](#insn-00be0218) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be021c`](#insn-00be021c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0228`](#insn-00be0228) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfc0c`](#insn-00bdfc0c)

~~~json
{
  "source": "00bdfc0c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc10`](#insn-00bdfc10)

~~~json
{
  "source": "00bdfc10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc14`](#insn-00bdfc14)

~~~json
{
  "source": "00bdfc14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc18`](#insn-00bdfc18)

~~~json
{
  "source": "00bdfc18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc1c`](#insn-00bdfc1c)

~~~json
{
  "source": "00bdfc1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc20`](#insn-00bdfc20)

~~~json
{
  "source": "00bdfc20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc34`](#insn-00bdfc34)

~~~json
{
  "source": "00bdfc34",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc3c`](#insn-00bdfc3c)

~~~json
{
  "source": "00bdfc3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc4c`](#insn-00bdfc4c)

~~~json
{
  "source": "00bdfc4c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc50`](#insn-00bdfc50)

~~~json
{
  "source": "00bdfc50",
  "target": "00be01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc58`](#insn-00bdfc58)

~~~json
{
  "source": "00bdfc58",
  "target": "00be01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc60`](#insn-00bdfc60)

~~~json
{
  "source": "00bdfc60",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc64`](#insn-00bdfc64)

~~~json
{
  "source": "00bdfc64",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc6c`](#insn-00bdfc6c)

~~~json
{
  "source": "00bdfc6c",
  "target": "01127e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfc78`](#insn-00bdfc78)

~~~json
{
  "source": "00bdfc78",
  "target": "Stack[-0x1d8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc7c`](#insn-00bdfc7c)

~~~json
{
  "source": "00bdfc7c",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc80`](#insn-00bdfc80)

~~~json
{
  "source": "00bdfc80",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc84`](#insn-00bdfc84)

~~~json
{
  "source": "00bdfc84",
  "target": "00be01f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc8c`](#insn-00bdfc8c)

~~~json
{
  "source": "00bdfc8c",
  "target": "00c5c5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfc94`](#insn-00bdfc94)

~~~json
{
  "source": "00bdfc94",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfc98`](#insn-00bdfc98)

~~~json
{
  "source": "00bdfc98",
  "target": "00576618",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfca8`](#insn-00bdfca8)

~~~json
{
  "source": "00bdfca8",
  "target": "00c5ef70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfcb0`](#insn-00bdfcb0)

~~~json
{
  "source": "00bdfcb0",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfcb4`](#insn-00bdfcb4)

~~~json
{
  "source": "00bdfcb4",
  "target": "00be01e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfcbc`](#insn-00bdfcbc)

~~~json
{
  "source": "00bdfcbc",
  "target": "00c9cb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cb00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcc4`](#insn-00bdfcc4)

~~~json
{
  "source": "00bdfcc4",
  "target": "00c9ca68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcd8`](#insn-00bdfcd8)

~~~json
{
  "source": "00bdfcd8",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfcf8`](#insn-00bdfcf8)

~~~json
{
  "source": "00bdfcf8",
  "target": "00c939b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c939a0",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdfcf8`](#insn-00bdfcf8)

~~~json
{
  "source": "00bdfcf8",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd00`](#insn-00bdfd00)

~~~json
{
  "source": "00bdfd00",
  "target": "00c93a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93a08",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdfd00`](#insn-00bdfd00)

~~~json
{
  "source": "00bdfd00",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd08`](#insn-00bdfd08)

~~~json
{
  "source": "00bdfd08",
  "target": "00c5c5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd10`](#insn-00bdfd10)

~~~json
{
  "source": "00bdfd10",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd18`](#insn-00bdfd18)

~~~json
{
  "source": "00bdfd18",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd1c`](#insn-00bdfd1c)

~~~json
{
  "source": "00bdfd1c",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd20`](#insn-00bdfd20)

~~~json
{
  "source": "00bdfd20",
  "target": "Stack[-0x1f0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd30`](#insn-00bdfd30)

~~~json
{
  "source": "00bdfd30",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd34`](#insn-00bdfd34)

~~~json
{
  "source": "00bdfd34",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd38`](#insn-00bdfd38)

~~~json
{
  "source": "00bdfd38",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd3c`](#insn-00bdfd3c)

~~~json
{
  "source": "00bdfd3c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd40`](#insn-00bdfd40)

~~~json
{
  "source": "00bdfd40",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd44`](#insn-00bdfd44)

~~~json
{
  "source": "00bdfd44",
  "target": "00c939b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c939a0",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdfd44`](#insn-00bdfd44)

~~~json
{
  "source": "00bdfd44",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd48`](#insn-00bdfd48)

~~~json
{
  "source": "00bdfd48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd50`](#insn-00bdfd50)

~~~json
{
  "source": "00bdfd50",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfd68`](#insn-00bdfd68)

~~~json
{
  "source": "00bdfd68",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd80`](#insn-00bdfd80)

~~~json
{
  "source": "00bdfd80",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd88`](#insn-00bdfd88)

~~~json
{
  "source": "00bdfd88",
  "target": "00c93a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93a08",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdfd88`](#insn-00bdfd88)

~~~json
{
  "source": "00bdfd88",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd8c`](#insn-00bdfd8c)

~~~json
{
  "source": "00bdfd8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd90`](#insn-00bdfd90)

~~~json
{
  "source": "00bdfd90",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd94`](#insn-00bdfd94)

~~~json
{
  "source": "00bdfd94",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd98`](#insn-00bdfd98)

~~~json
{
  "source": "00bdfd98",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfd9c`](#insn-00bdfd9c)

~~~json
{
  "source": "00bdfd9c",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfda0`](#insn-00bdfda0)

~~~json
{
  "source": "00bdfda0",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfda8`](#insn-00bdfda8)

~~~json
{
  "source": "00bdfda8",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfdb0`](#insn-00bdfdb0)

~~~json
{
  "source": "00bdfdb0",
  "target": "00bdfdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdb8`](#insn-00bdfdb8)

~~~json
{
  "source": "00bdfdb8",
  "target": "01127e80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e80",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfdc4`](#insn-00bdfdc4)

~~~json
{
  "source": "00bdfdc4",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfdd0`](#insn-00bdfdd0)

~~~json
{
  "source": "00bdfdd0",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfdd4`](#insn-00bdfdd4)

~~~json
{
  "source": "00bdfdd4",
  "target": "00bdfe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfddc`](#insn-00bdfddc)

~~~json
{
  "source": "00bdfddc",
  "target": "00bdfe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdec`](#insn-00bdfdec)

~~~json
{
  "source": "00bdfdec",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfdf0`](#insn-00bdfdf0)

~~~json
{
  "source": "00bdfdf0",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdf4`](#insn-00bdfdf4)

~~~json
{
  "source": "00bdfdf4",
  "target": "00bdfe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdf8`](#insn-00bdfdf8)

~~~json
{
  "source": "00bdfdf8",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfdfc`](#insn-00bdfdfc)

~~~json
{
  "source": "00bdfdfc",
  "target": "00bdfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe00`](#insn-00bdfe00)

~~~json
{
  "source": "00bdfe00",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe04`](#insn-00bdfe04)

~~~json
{
  "source": "00bdfe04",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe08`](#insn-00bdfe08)

~~~json
{
  "source": "00bdfe08",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe0c`](#insn-00bdfe0c)

~~~json
{
  "source": "00bdfe0c",
  "target": "00bdfdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe10`](#insn-00bdfe10)

~~~json
{
  "source": "00bdfe10",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe18`](#insn-00bdfe18)

~~~json
{
  "source": "00bdfe18",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe1c`](#insn-00bdfe1c)

~~~json
{
  "source": "00bdfe1c",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe20`](#insn-00bdfe20)

~~~json
{
  "source": "00bdfe20",
  "target": "00bdfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe24`](#insn-00bdfe24)

~~~json
{
  "source": "00bdfe24",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe28`](#insn-00bdfe28)

~~~json
{
  "source": "00bdfe28",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe2c`](#insn-00bdfe2c)

~~~json
{
  "source": "00bdfe2c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe30`](#insn-00bdfe30)

~~~json
{
  "source": "00bdfe30",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe34`](#insn-00bdfe34)

~~~json
{
  "source": "00bdfe34",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe38`](#insn-00bdfe38)

~~~json
{
  "source": "00bdfe38",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe3c`](#insn-00bdfe3c)

~~~json
{
  "source": "00bdfe3c",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe40`](#insn-00bdfe40)

~~~json
{
  "source": "00bdfe40",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe48`](#insn-00bdfe48)

~~~json
{
  "source": "00bdfe48",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe50`](#insn-00bdfe50)

~~~json
{
  "source": "00bdfe50",
  "target": "00bdfe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe58`](#insn-00bdfe58)

~~~json
{
  "source": "00bdfe58",
  "target": "01127ea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ea8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdfe64`](#insn-00bdfe64)

~~~json
{
  "source": "00bdfe64",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe70`](#insn-00bdfe70)

~~~json
{
  "source": "00bdfe70",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe74`](#insn-00bdfe74)

~~~json
{
  "source": "00bdfe74",
  "target": "00bdfea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe7c`](#insn-00bdfe7c)

~~~json
{
  "source": "00bdfe7c",
  "target": "00bdfea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe8c`](#insn-00bdfe8c)

~~~json
{
  "source": "00bdfe8c",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfe90`](#insn-00bdfe90)

~~~json
{
  "source": "00bdfe90",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe94`](#insn-00bdfe94)

~~~json
{
  "source": "00bdfe94",
  "target": "00bdfeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe98`](#insn-00bdfe98)

~~~json
{
  "source": "00bdfe98",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfe9c`](#insn-00bdfe9c)

~~~json
{
  "source": "00bdfe9c",
  "target": "00bdfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfea0`](#insn-00bdfea0)

~~~json
{
  "source": "00bdfea0",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfea4`](#insn-00bdfea4)

~~~json
{
  "source": "00bdfea4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfea8`](#insn-00bdfea8)

~~~json
{
  "source": "00bdfea8",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeac`](#insn-00bdfeac)

~~~json
{
  "source": "00bdfeac",
  "target": "00bdfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeb0`](#insn-00bdfeb0)

~~~json
{
  "source": "00bdfeb0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeb8`](#insn-00bdfeb8)

~~~json
{
  "source": "00bdfeb8",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfebc`](#insn-00bdfebc)

~~~json
{
  "source": "00bdfebc",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfec0`](#insn-00bdfec0)

~~~json
{
  "source": "00bdfec0",
  "target": "00bdfed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfec4`](#insn-00bdfec4)

~~~json
{
  "source": "00bdfec4",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfec8`](#insn-00bdfec8)

~~~json
{
  "source": "00bdfec8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfecc`](#insn-00bdfecc)

~~~json
{
  "source": "00bdfecc",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfed0`](#insn-00bdfed0)

~~~json
{
  "source": "00bdfed0",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfed4`](#insn-00bdfed4)

~~~json
{
  "source": "00bdfed4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfed8`](#insn-00bdfed8)

~~~json
{
  "source": "00bdfed8",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfedc`](#insn-00bdfedc)

~~~json
{
  "source": "00bdfedc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfee0`](#insn-00bdfee0)

~~~json
{
  "source": "00bdfee0",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfee4`](#insn-00bdfee4)

~~~json
{
  "source": "00bdfee4",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfeec`](#insn-00bdfeec)

~~~json
{
  "source": "00bdfeec",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdfef4`](#insn-00bdfef4)

~~~json
{
  "source": "00bdfef4",
  "target": "00bdff10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfefc`](#insn-00bdfefc)

~~~json
{
  "source": "00bdfefc",
  "target": "01127e90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdff08`](#insn-00bdff08)

~~~json
{
  "source": "00bdff08",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff14`](#insn-00bdff14)

~~~json
{
  "source": "00bdff14",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff18`](#insn-00bdff18)

~~~json
{
  "source": "00bdff18",
  "target": "00bdff44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff20`](#insn-00bdff20)

~~~json
{
  "source": "00bdff20",
  "target": "00bdff44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff30`](#insn-00bdff30)

~~~json
{
  "source": "00bdff30",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff34`](#insn-00bdff34)

~~~json
{
  "source": "00bdff34",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff38`](#insn-00bdff38)

~~~json
{
  "source": "00bdff38",
  "target": "00bdff54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff3c`](#insn-00bdff3c)

~~~json
{
  "source": "00bdff3c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff40`](#insn-00bdff40)

~~~json
{
  "source": "00bdff40",
  "target": "00bdff74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff44`](#insn-00bdff44)

~~~json
{
  "source": "00bdff44",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff48`](#insn-00bdff48)

~~~json
{
  "source": "00bdff48",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff4c`](#insn-00bdff4c)

~~~json
{
  "source": "00bdff4c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff50`](#insn-00bdff50)

~~~json
{
  "source": "00bdff50",
  "target": "00bdff3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff54`](#insn-00bdff54)

~~~json
{
  "source": "00bdff54",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff5c`](#insn-00bdff5c)

~~~json
{
  "source": "00bdff5c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff60`](#insn-00bdff60)

~~~json
{
  "source": "00bdff60",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff64`](#insn-00bdff64)

~~~json
{
  "source": "00bdff64",
  "target": "00bdff74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff68`](#insn-00bdff68)

~~~json
{
  "source": "00bdff68",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff6c`](#insn-00bdff6c)

~~~json
{
  "source": "00bdff6c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff70`](#insn-00bdff70)

~~~json
{
  "source": "00bdff70",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff74`](#insn-00bdff74)

~~~json
{
  "source": "00bdff74",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff78`](#insn-00bdff78)

~~~json
{
  "source": "00bdff78",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff7c`](#insn-00bdff7c)

~~~json
{
  "source": "00bdff7c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff80`](#insn-00bdff80)

~~~json
{
  "source": "00bdff80",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff84`](#insn-00bdff84)

~~~json
{
  "source": "00bdff84",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff8c`](#insn-00bdff8c)

~~~json
{
  "source": "00bdff8c",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdff94`](#insn-00bdff94)

~~~json
{
  "source": "00bdff94",
  "target": "00bdffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdff9c`](#insn-00bdff9c)

~~~json
{
  "source": "00bdff9c",
  "target": "01127ea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdffa8`](#insn-00bdffa8)

~~~json
{
  "source": "00bdffa8",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdffb4`](#insn-00bdffb4)

~~~json
{
  "source": "00bdffb4",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdffb8`](#insn-00bdffb8)

~~~json
{
  "source": "00bdffb8",
  "target": "00bdffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffc0`](#insn-00bdffc0)

~~~json
{
  "source": "00bdffc0",
  "target": "00bdffe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffd0`](#insn-00bdffd0)

~~~json
{
  "source": "00bdffd0",
  "target": "00c5c390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdffd4`](#insn-00bdffd4)

~~~json
{
  "source": "00bdffd4",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffd8`](#insn-00bdffd8)

~~~json
{
  "source": "00bdffd8",
  "target": "00bdfff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffdc`](#insn-00bdffdc)

~~~json
{
  "source": "00bdffdc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffe0`](#insn-00bdffe0)

~~~json
{
  "source": "00bdffe0",
  "target": "00be0014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffe4`](#insn-00bdffe4)

~~~json
{
  "source": "00bdffe4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffe8`](#insn-00bdffe8)

~~~json
{
  "source": "00bdffe8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdffec`](#insn-00bdffec)

~~~json
{
  "source": "00bdffec",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfff0`](#insn-00bdfff0)

~~~json
{
  "source": "00bdfff0",
  "target": "00bdffdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfff4`](#insn-00bdfff4)

~~~json
{
  "source": "00bdfff4",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdfffc`](#insn-00bdfffc)

~~~json
{
  "source": "00bdfffc",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0000`](#insn-00be0000)

~~~json
{
  "source": "00be0000",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0004`](#insn-00be0004)

~~~json
{
  "source": "00be0004",
  "target": "00be0014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0008`](#insn-00be0008)

~~~json
{
  "source": "00be0008",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be000c`](#insn-00be000c)

~~~json
{
  "source": "00be000c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0010`](#insn-00be0010)

~~~json
{
  "source": "00be0010",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0014`](#insn-00be0014)

~~~json
{
  "source": "00be0014",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0018`](#insn-00be0018)

~~~json
{
  "source": "00be0018",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be001c`](#insn-00be001c)

~~~json
{
  "source": "00be001c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0020`](#insn-00be0020)

~~~json
{
  "source": "00be0020",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0024`](#insn-00be0024)

~~~json
{
  "source": "00be0024",
  "target": "Stack[-0x160]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be002c`](#insn-00be002c)

~~~json
{
  "source": "00be002c",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0034`](#insn-00be0034)

~~~json
{
  "source": "00be0034",
  "target": "00be0050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be003c`](#insn-00be003c)

~~~json
{
  "source": "00be003c",
  "target": "01127e88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00be0048`](#insn-00be0048)

~~~json
{
  "source": "00be0048",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0054`](#insn-00be0054)

~~~json
{
  "source": "00be0054",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0058`](#insn-00be0058)

~~~json
{
  "source": "00be0058",
  "target": "00be0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0060`](#insn-00be0060)

~~~json
{
  "source": "00be0060",
  "target": "00be0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0070`](#insn-00be0070)

~~~json
{
  "source": "00be0070",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0074`](#insn-00be0074)

~~~json
{
  "source": "00be0074",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0078`](#insn-00be0078)

~~~json
{
  "source": "00be0078",
  "target": "00be0094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be007c`](#insn-00be007c)

~~~json
{
  "source": "00be007c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0080`](#insn-00be0080)

~~~json
{
  "source": "00be0080",
  "target": "00be00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0084`](#insn-00be0084)

~~~json
{
  "source": "00be0084",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0088`](#insn-00be0088)

~~~json
{
  "source": "00be0088",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be008c`](#insn-00be008c)

~~~json
{
  "source": "00be008c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0090`](#insn-00be0090)

~~~json
{
  "source": "00be0090",
  "target": "00be007c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0094`](#insn-00be0094)

~~~json
{
  "source": "00be0094",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be009c`](#insn-00be009c)

~~~json
{
  "source": "00be009c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00a0`](#insn-00be00a0)

~~~json
{
  "source": "00be00a0",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00a4`](#insn-00be00a4)

~~~json
{
  "source": "00be00a4",
  "target": "00be00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00a8`](#insn-00be00a8)

~~~json
{
  "source": "00be00a8",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00ac`](#insn-00be00ac)

~~~json
{
  "source": "00be00ac",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00b0`](#insn-00be00b0)

~~~json
{
  "source": "00be00b0",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00b4`](#insn-00be00b4)

~~~json
{
  "source": "00be00b4",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00b8`](#insn-00be00b8)

~~~json
{
  "source": "00be00b8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00bc`](#insn-00be00bc)

~~~json
{
  "source": "00be00bc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00c0`](#insn-00be00c0)

~~~json
{
  "source": "00be00c0",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00c4`](#insn-00be00c4)

~~~json
{
  "source": "00be00c4",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00cc`](#insn-00be00cc)

~~~json
{
  "source": "00be00cc",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00d4`](#insn-00be00d4)

~~~json
{
  "source": "00be00d4",
  "target": "00be00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be00dc`](#insn-00be00dc)

~~~json
{
  "source": "00be00dc",
  "target": "01127e98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00be00e8`](#insn-00be00e8)

~~~json
{
  "source": "00be00e8",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00f4`](#insn-00be00f4)

~~~json
{
  "source": "00be00f4",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be00f8`](#insn-00be00f8)

~~~json
{
  "source": "00be00f8",
  "target": "00be0124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0100`](#insn-00be0100)

~~~json
{
  "source": "00be0100",
  "target": "00be0124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0110`](#insn-00be0110)

~~~json
{
  "source": "00be0110",
  "target": "00c5c430",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0114`](#insn-00be0114)

~~~json
{
  "source": "00be0114",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0118`](#insn-00be0118)

~~~json
{
  "source": "00be0118",
  "target": "00be0134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be011c`](#insn-00be011c)

~~~json
{
  "source": "00be011c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0120`](#insn-00be0120)

~~~json
{
  "source": "00be0120",
  "target": "00be0154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0124`](#insn-00be0124)

~~~json
{
  "source": "00be0124",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0128`](#insn-00be0128)

~~~json
{
  "source": "00be0128",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be012c`](#insn-00be012c)

~~~json
{
  "source": "00be012c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0130`](#insn-00be0130)

~~~json
{
  "source": "00be0130",
  "target": "00be011c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0134`](#insn-00be0134)

~~~json
{
  "source": "00be0134",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be013c`](#insn-00be013c)

~~~json
{
  "source": "00be013c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0140`](#insn-00be0140)

~~~json
{
  "source": "00be0140",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0144`](#insn-00be0144)

~~~json
{
  "source": "00be0144",
  "target": "00be0154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0148`](#insn-00be0148)

~~~json
{
  "source": "00be0148",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be014c`](#insn-00be014c)

~~~json
{
  "source": "00be014c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0150`](#insn-00be0150)

~~~json
{
  "source": "00be0150",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0158`](#insn-00be0158)

~~~json
{
  "source": "00be0158",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be015c`](#insn-00be015c)

~~~json
{
  "source": "00be015c",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0164`](#insn-00be0164)

~~~json
{
  "source": "00be0164",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0168`](#insn-00be0168)

~~~json
{
  "source": "00be0168",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be016c`](#insn-00be016c)

~~~json
{
  "source": "00be016c",
  "target": "00be0188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0178`](#insn-00be0178)

~~~json
{
  "source": "00be0178",
  "target": "00c5ef40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0184`](#insn-00be0184)

~~~json
{
  "source": "00be0184",
  "target": "00be0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0190`](#insn-00be0190)

~~~json
{
  "source": "00be0190",
  "target": "00c5ef60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0198`](#insn-00be0198)

~~~json
{
  "source": "00be0198",
  "target": "00c5ec10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be01a0`](#insn-00be01a0)

~~~json
{
  "source": "00be01a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01a4`](#insn-00be01a4)

~~~json
{
  "source": "00be01a4",
  "target": "00c9cb00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9cb00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00be01ac`](#insn-00be01ac)

~~~json
{
  "source": "00be01ac",
  "target": "00c939b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c939a0",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00be01ac`](#insn-00be01ac)

~~~json
{
  "source": "00be01ac",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01b4`](#insn-00be01b4)

~~~json
{
  "source": "00be01b4",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be01bc`](#insn-00be01bc)

~~~json
{
  "source": "00be01bc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01cc`](#insn-00be01cc)

~~~json
{
  "source": "00be01cc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01d0`](#insn-00be01d0)

~~~json
{
  "source": "00be01d0",
  "target": "00c5ec20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be01d4`](#insn-00be01d4)

~~~json
{
  "source": "00be01d4",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01e0`](#insn-00be01e0)

~~~json
{
  "source": "00be01e0",
  "target": "00bdfd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01e4`](#insn-00be01e4)

~~~json
{
  "source": "00be01e4",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01f4`](#insn-00be01f4)

~~~json
{
  "source": "00be01f4",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be01fc`](#insn-00be01fc)

~~~json
{
  "source": "00be01fc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0204`](#insn-00be0204)

~~~json
{
  "source": "00be0204",
  "target": "00be0228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be020c`](#insn-00be020c)

~~~json
{
  "source": "00be020c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0210`](#insn-00be0210)

~~~json
{
  "source": "00be0210",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0214`](#insn-00be0214)

~~~json
{
  "source": "00be0214",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0218`](#insn-00be0218)

~~~json
{
  "source": "00be0218",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be021c`](#insn-00be021c)

~~~json
{
  "source": "00be021c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0228`](#insn-00be0228)

~~~json
{
  "source": "00be0228",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
