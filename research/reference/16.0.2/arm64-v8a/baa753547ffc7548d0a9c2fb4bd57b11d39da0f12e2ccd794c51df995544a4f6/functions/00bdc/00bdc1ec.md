# 00bdc1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdc150`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc150.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-dcc38110ec087c7eaa4083ec534cb016)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdd1e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd1e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-5d7b4745fe1d740da029863c73c8a7b1)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc1ec",
  "name": "_ZN8firebase4auth22FederatedOAuthProvider14ReauthenticateEPNS0_8AuthDataE",
  "size": 584,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edcf12f1d3ac3063578bb0177ad83bc13759eb6c29d8cda096c2c7d542ef03d3",
  "source_text_sha256": "edcf12f1d3ac3063578bb0177ad83bc13759eb6c29d8cda096c2c7d542ef03d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdc1ec",
        "00bdc433"
      ]
    ],
    "bytes_sha256": "4b81d42b623d476a786f489f27793a9f1db6fa34e964a1eb75e55e6e34b933f9",
    "instruction_count": 146,
    "instruction_bytes": 584,
    "body_bytes": 584,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00bdbcd4](../00bdb/00bdbcd4.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab20](../00c5a/00c5ab20.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5bef0](../00c5b/00c5bef0.md)
- [00c5dc30](../00c5d/00c5dc30.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)
- [00c5deb0](../00c5d/00c5deb0.md)
- [00c5ded0](../00c5d/00c5ded0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5124 bytes

~~~c

void _ZN8firebase4auth22FederatedOAuthProvider14ReauthenticateEPNS0_8AuthDataE
               (undefined8 param_1,long param_2,undefined8 *param_3)

{
  long lVar1;
  undefined *puVar2;
  long *plVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_1d0 [16];
  ulong local_1c0 [2];
  void *local_1b0;
  ulong uStack_1a8;
  undefined8 uStack_1a0;
  void *local_198;
  undefined8 *local_190;
  undefined8 uStack_188;
  undefined8 uStack_180;
  undefined8 local_178;
  undefined8 local_170;
  undefined8 uStack_168;
  undefined8 uStack_160;
  undefined8 uStack_158;
  undefined8 local_150;
  undefined8 uStack_148;
  undefined8 local_140;
  undefined8 uStack_138;
  undefined8 local_130;
  undefined8 uStack_128;
  undefined8 uStack_120;
  undefined8 uStack_118;
  undefined8 local_110;
  undefined8 uStack_108;
  undefined8 uStack_100;
  undefined8 uStack_f8;
  undefined8 local_f0;
  undefined8 uStack_e8;
  undefined8 uStack_e0;
  undefined8 uStack_d8;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined8 uStack_c0;
  undefined8 uStack_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined8 uStack_a0;
  undefined8 uStack_98;
  undefined8 local_90;
  undefined1 auStack_80 [16];
  long local_70;
  
  lVar1 = tpidr_el0;
  local_70 = *(long *)(lVar1 + 0x28);
  puVar10 = param_3 + 2;
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_3);
  local_190 = &uStack_188;
  local_90 = 0;
  uStack_a8 = 0;
  local_b0 = 0;
  uStack_98 = 0;
  uStack_a0 = 0;
  uStack_c8 = 0;
  local_d0 = 0;
  uStack_b8 = 0;
  uStack_c0 = 0;
  uStack_e8 = 0;
  local_f0 = 0;
  uStack_d8 = 0;
  uStack_e0 = 0;
  uStack_108 = 0;
  local_110 = 0;
  uStack_f8 = 0;
  uStack_100 = 0;
  uStack_128 = 0;
  uStack_118 = 0;
  uStack_120 = 0;
  uStack_188 = 0;
  uStack_180 = 0;
  uStack_1a8 = 0;
  local_1b0 = (void *)0x0;
  local_198 = (void *)0x0;
  uStack_1a0 = 0;
  local_1c0[1] = 0;
  local_1c0[0] = 0;
  local_178 = 0;
  local_170 = 0;
  local_140 = 0;
  uStack_138 = 0;
  local_130 = 0;
  uStack_160 = 0;
  uStack_168 = 0;
  local_150 = 0;
  uStack_158 = 0;
  uStack_148 = 0;
  _ZN8firebase4auth4UserC2Ev(&uStack_128);
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEiRKS5_
            (auStack_80,puVar10,0x14,local_1c0);
  _ZN8firebase4auth4UserD2Ev(&uStack_128);
  _ZN8firebase4auth10CredentialD2Ev(&local_150);
  _ZN8firebase4auth10CredentialD2Ev(&local_178);
  _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
            (&local_190,uStack_188);
  if ((uStack_1a8 & 1) != 0) {
    _ZdlPv(local_198);
  }
  if ((local_1c0[0] & 1) != 0) {
    _ZdlPv(local_1b0);
  }
  uVar4 = FUN_00bdbcd4(param_3,param_2 + 8);
  uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar3,puVar10,auStack_80);
  if ((uVar5 & 1) == 0) {
    uVar6 = FUN_00497874(plVar3,param_3[0x40],DAT_01126da0,*(undefined8 *)*param_3,uVar4);
    uVar5 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar3,puVar10,auStack_80);
    if ((uVar5 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_1d0,auStack_80);
      uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*param_3);
      lVar8 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_1d0);
      puVar2 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
      ;
      *(undefined8 **)(lVar8 + 0x10) = param_3;
      *(undefined **)(lVar8 + 0x18) = puVar2;
      if ((*(byte *)(param_3 + 0x28) & 1) == 0) {
                    /* try { // try from 00bdc394 to 00cdc39f has its CatchHandler @ 00bded64 */
        lVar9 = (long)param_3 + 0x141;
      }
      else {
        lVar9 = param_3[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar7,uVar6,
                 PTR__ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bb08
                 ,lVar8,lVar9);
                    /* try { // try from 00bdc3bc to 00cdc3db has its CatchHandler @ 00bded48 */
      _ZN8firebase12FutureHandleD2Ev(auStack_1d0);
    }
    (**(code **)(*plVar3 + 0xb8))(plVar3,uVar6);
  }
                    /* try { // try from 00bdc3dc to 00cdc6af has its CatchHandler @ 00bd6fbc */
  (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
  _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,puVar10,auStack_80);
  _ZN8firebase12FutureHandleD2Ev(auStack_80);
  if (*(long *)(lVar1 + 0x28) == local_70) {
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
<a id="insn-00bdc1ec"></a> `00bdc1ec` | `ff 43 07 d1` | sub sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00bdc1f0"></a> `00bdc1f0` | `fc 6f 17 a9` | stp x28,x27,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bdc1f4"></a> `00bdc1f4` | `fa 67 18 a9` | stp x26,x25,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00bdc1f8"></a> `00bdc1f8` | `f8 5f 19 a9` | stp x24,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdc1fc"></a> `00bdc1fc` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bdc200"></a> `00bdc200` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00bdc204"></a> `00bdc204` | `fd 7b 1c a9` | stp x29,x30,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bdc208"></a> `00bdc208` | `fd 03 07 91` | add x29,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-00bdc20c"></a> `00bdc20c` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdc210"></a> `00bdc210` | `69 17 40 f9` | ldr x9,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00bdc214"></a> `00bdc214` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bdc218"></a> `00bdc218` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdc21c"></a> `00bdc21c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdc220"></a> `00bdc220` | `a9 03 1a f8` | stur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bdc224"></a> `00bdc224` | `60 06 41 f8` | ldr x0,[x19], #0x10 | `FALL_THROUGH`
<a id="insn-00bdc228"></a> `00bdc228` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bdc22c"></a> `00bdc22c` | `c9 fb 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc230"></a> `00bdc230` | `f9 43 00 91` | add x25,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdc234"></a> `00bdc234` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdc238"></a> `00bdc238` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdc23c"></a> `00bdc23c` | `28 e3 00 91` | add x8,x25,#0x38 | `FALL_THROUGH`
<a id="insn-00bdc240"></a> `00bdc240` | `38 63 02 91` | add x24,x25,#0x98 | `FALL_THROUGH`
<a id="insn-00bdc244"></a> `00bdc244` | `ff a3 00 f9` | str xzr,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bdc248"></a> `00bdc248` | `e0 03 09 ad` | stp q0,q0,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bdc24c"></a> `00bdc24c` | `e0 03 08 ad` | stp q0,q0,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00bdc250"></a> `00bdc250` | `e0 03 07 ad` | stp q0,q0,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bdc254"></a> `00bdc254` | `e0 03 06 ad` | stp q0,q0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bdc258"></a> `00bdc258` | `e0 03 05 ad` | stp q0,q0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdc25c"></a> `00bdc25c` | `e0 03 04 ad` | stp q0,q0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bdc260"></a> `00bdc260` | `e0 03 03 ad` | stp q0,q0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdc264"></a> `00bdc264` | `e0 03 02 ad` | stp q0,q0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdc268"></a> `00bdc268` | `e0 03 01 ad` | stp q0,q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc26c"></a> `00bdc26c` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc270"></a> `00bdc270` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bdc274"></a> `00bdc274` | `ff 63 00 b9` | str wzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdc278"></a> `00bdc278` | `ff 7f 09 a9` | stp xzr,xzr,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bdc27c"></a> `00bdc27c` | `ff 53 00 f9` | str xzr,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdc280"></a> `00bdc280` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdc284"></a> `00bdc284` | `e0 83 86 3c` | stur q0,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00bdc288"></a> `00bdc288` | `e0 83 87 3c` | stur q0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bdc28c"></a> `00bdc28c` | `ff 8b 00 b9` | str wzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00bdc290"></a> `00bdc290` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bdc294"></a> `00bdc294` | `67 06 02 94` | bl 0x00c5dc30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc298"></a> `00bdc298` | `a8 c3 01 d1` | sub x8,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc29c"></a> `00bdc29c` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdc2a0"></a> `00bdc2a0` | `81 02 80 52` | mov w1,#0x14 | `FALL_THROUGH`
<a id="insn-00bdc2a4"></a> `00bdc2a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdc2a8"></a> `00bdc2a8` | `f9 43 00 91` | add x25,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdc2ac"></a> `00bdc2ac` | `01 07 02 94` | bl 0x00c5deb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2b0"></a> `00bdc2b0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bdc2b4"></a> `00bdc2b4` | `1b fa 01 94` | bl 0x00c5ab20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2b8"></a> `00bdc2b8` | `20 c3 01 91` | add x0,x25,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc2bc"></a> `00bdc2bc` | `05 07 02 94` | bl 0x00c5ded0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2c0"></a> `00bdc2c0` | `20 23 01 91` | add x0,x25,#0x48 | `FALL_THROUGH`
<a id="insn-00bdc2c4"></a> `00bdc2c4` | `03 07 02 94` | bl 0x00c5ded0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2c8"></a> `00bdc2c8` | `e1 27 40 f9` | ldr x1,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bdc2cc"></a> `00bdc2cc` | `20 c3 00 91` | add x0,x25,#0x30 | `FALL_THROUGH`
<a id="insn-00bdc2d0"></a> `00bdc2d0` | `08 ff 01 94` | bl 0x00c5bef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2d4"></a> `00bdc2d4` | `e8 a3 40 39` | ldrb w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bdc2d8"></a> `00bdc2d8` | `68 00 00 36` | tbz w8,#0x0,0x00bdc2e4 | `CONDITIONAL_JUMP`
<a id="insn-00bdc2dc"></a> `00bdc2dc` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bdc2e0"></a> `00bdc2e0` | `28 ef 01 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2e4"></a> `00bdc2e4` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc2e8"></a> `00bdc2e8` | `68 00 00 36` | tbz w8,#0x0,0x00bdc2f4 | `CONDITIONAL_JUMP`
<a id="insn-00bdc2ec"></a> `00bdc2ec` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc2f0"></a> `00bdc2f0` | `24 ef 01 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc2f4"></a> `00bdc2f4` | `e1 22 00 91` | add x1,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bdc2f8"></a> `00bdc2f8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdc2fc"></a> `00bdc2fc` | `76 fe ff 97` | bl 0x00bdbcd4 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc300"></a> `00bdc300` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdc304"></a> `00bdc304` | `a2 c3 01 d1` | sub x2,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc308"></a> `00bdc308` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc30c"></a> `00bdc30c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdc310"></a> `00bdc310` | `a4 06 02 94` | bl 0x00c5dda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc314"></a> `00bdc314` | `00 06 00 37` | tbnz w0,#0x0,0x00bdc3d4 | `CONDITIONAL_JUMP`
<a id="insn-00bdc318"></a> `00bdc318` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdc31c"></a> `00bdc31c` | `c1 02 41 f9` | ldr x1,[x22, #0x200] | `FALL_THROUGH`
<a id="insn-00bdc320"></a> `00bdc320` | `49 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdc324"></a> `00bdc324` | `22 d1 46 f9` | ldr x2,[x9, #0xda0] | `FALL_THROUGH`
<a id="insn-00bdc328"></a> `00bdc328` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bdc32c"></a> `00bdc32c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc330"></a> `00bdc330` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdc334"></a> `00bdc334` | `50 ed e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc338"></a> `00bdc338` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bdc33c"></a> `00bdc33c` | `a2 c3 01 d1` | sub x2,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc340"></a> `00bdc340` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc344"></a> `00bdc344` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdc348"></a> `00bdc348` | `96 06 02 94` | bl 0x00c5dda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc34c"></a> `00bdc34c` | `a0 03 00 37` | tbnz w0,#0x0,0x00bdc3c0 | `CONDITIONAL_JUMP`
<a id="insn-00bdc350"></a> `00bdc350` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bdc354"></a> `00bdc354` | `a1 c3 01 d1` | sub x1,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc358"></a> `00bdc358` | `de fa 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc35c"></a> `00bdc35c` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00bdc360"></a> `00bdc360` | `7c fb 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc364"></a> `00bdc364` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bdc368"></a> `00bdc368` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bdc36c"></a> `00bdc36c` | `fd ee 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc370"></a> `00bdc370` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bdc374"></a> `00bdc374` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdc378"></a> `00bdc378` | `d6 fa 01 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc37c"></a> `00bdc37c` | `e8 05 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdc380"></a> `00bdc380` | `08 79 45 f9` | ldr x8,[x8, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bdc384"></a> `00bdc384` | `56 23 01 a9` | stp x22,x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc388"></a> `00bdc388` | `c8 02 45 39` | ldrb w8,[x22, #0x140] | `FALL_THROUGH`
<a id="insn-00bdc38c"></a> `00bdc38c` | `88 00 00 37` | tbnz w8,#0x0,0x00bdc39c | `CONDITIONAL_JUMP`
<a id="insn-00bdc390"></a> `00bdc390` | `c8 02 05 91` | add x8,x22,#0x140 | `FALL_THROUGH`
<a id="insn-00bdc394"></a> `00bdc394` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdc398"></a> `00bdc398` | `02 00 00 14` | b 0x00bdc3a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdc39c"></a> `00bdc39c` | `c4 aa 40 f9` | ldr x4,[x22, #0x150] | `FALL_THROUGH`
<a id="insn-00bdc3a0"></a> `00bdc3a0` | `e2 05 00 f0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bdc3a4"></a> `00bdc3a4` | `42 84 45 f9` | ldr x2,[x2, #0xb08] | `FALL_THROUGH`
<a id="insn-00bdc3a8"></a> `00bdc3a8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdc3ac"></a> `00bdc3ac` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bdc3b0"></a> `00bdc3b0` | `e3 03 1a aa` | mov x3,x26 | `FALL_THROUGH`
<a id="insn-00bdc3b4"></a> `00bdc3b4` | `17 fb 01 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc3b8"></a> `00bdc3b8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bdc3bc"></a> `00bdc3bc` | `e9 f9 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc3c0"></a> `00bdc3c0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdc3c4"></a> `00bdc3c4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdc3c8"></a> `00bdc3c8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc3cc"></a> `00bdc3cc` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bdc3d0"></a> `00bdc3d0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdc3d4"></a> `00bdc3d4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdc3d8"></a> `00bdc3d8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdc3dc"></a> `00bdc3dc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdc3e0"></a> `00bdc3e0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdc3e4"></a> `00bdc3e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdc3e8"></a> `00bdc3e8` | `a2 c3 01 d1` | sub x2,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc3ec"></a> `00bdc3ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdc3f0"></a> `00bdc3f0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bdc3f4"></a> `00bdc3f4` | `83 06 02 94` | bl 0x00c5de00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc3f8"></a> `00bdc3f8` | `a0 c3 01 d1` | sub x0,x29,#0x70 | `FALL_THROUGH`
<a id="insn-00bdc3fc"></a> `00bdc3fc` | `d9 f9 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdc400"></a> `00bdc400` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00bdc404"></a> `00bdc404` | `a9 03 5a f8` | ldur x9,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00bdc408"></a> `00bdc408` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdc40c"></a> `00bdc40c` | `21 01 00 54` | b.ne 0x00bdc430 | `CONDITIONAL_JUMP`
<a id="insn-00bdc410"></a> `00bdc410` | `fd 7b 5c a9` | ldp x29,x30,[sp, #0x1c0] | `FALL_THROUGH`
<a id="insn-00bdc414"></a> `00bdc414` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-00bdc418"></a> `00bdc418` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-00bdc41c"></a> `00bdc41c` | `f8 5f 59 a9` | ldp x24,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-00bdc420"></a> `00bdc420` | `fa 67 58 a9` | ldp x26,x25,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-00bdc424"></a> `00bdc424` | `fc 6f 57 a9` | ldp x28,x27,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bdc428"></a> `00bdc428` | `ff 43 07 91` | add sp,sp,#0x1d0 | `FALL_THROUGH`
<a id="insn-00bdc42c"></a> `00bdc42c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdc430"></a> `00bdc430` | `e0 ee 01 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdc1ec`](#insn-00bdc1ec) 範囲 `[['00bdc1ec', '00bdc2db']]`
  - `CONDITIONAL_JUMP` [`00bdc2d8`](#insn-00bdc2d8) → [`00bdc2e4`](#insn-00bdc2e4)
  - `FALL_THROUGH` [`00bdc2d8`](#insn-00bdc2d8) → [`00bdc2dc`](#insn-00bdc2dc)
- ブロック [`00bdc2dc`](#insn-00bdc2dc) 範囲 `[['00bdc2dc', '00bdc2e3']]`
  - `FALL_THROUGH` [`00bdc2e0`](#insn-00bdc2e0) → [`00bdc2e4`](#insn-00bdc2e4)
- ブロック [`00bdc2e4`](#insn-00bdc2e4) 範囲 `[['00bdc2e4', '00bdc2eb']]`
  - `CONDITIONAL_JUMP` [`00bdc2e8`](#insn-00bdc2e8) → [`00bdc2f4`](#insn-00bdc2f4)
  - `FALL_THROUGH` [`00bdc2e8`](#insn-00bdc2e8) → [`00bdc2ec`](#insn-00bdc2ec)
- ブロック [`00bdc2ec`](#insn-00bdc2ec) 範囲 `[['00bdc2ec', '00bdc2f3']]`
  - `FALL_THROUGH` [`00bdc2f0`](#insn-00bdc2f0) → [`00bdc2f4`](#insn-00bdc2f4)
- ブロック [`00bdc2f4`](#insn-00bdc2f4) 範囲 `[['00bdc2f4', '00bdc317']]`
  - `CONDITIONAL_JUMP` [`00bdc314`](#insn-00bdc314) → [`00bdc3d4`](#insn-00bdc3d4)
  - `FALL_THROUGH` [`00bdc314`](#insn-00bdc314) → [`00bdc318`](#insn-00bdc318)
- ブロック [`00bdc318`](#insn-00bdc318) 範囲 `[['00bdc318', '00bdc34f']]`
  - `CONDITIONAL_JUMP` [`00bdc34c`](#insn-00bdc34c) → [`00bdc3c0`](#insn-00bdc3c0)
  - `FALL_THROUGH` [`00bdc34c`](#insn-00bdc34c) → [`00bdc350`](#insn-00bdc350)
- ブロック [`00bdc350`](#insn-00bdc350) 範囲 `[['00bdc350', '00bdc38f']]`
  - `CONDITIONAL_JUMP` [`00bdc38c`](#insn-00bdc38c) → [`00bdc39c`](#insn-00bdc39c)
  - `FALL_THROUGH` [`00bdc38c`](#insn-00bdc38c) → [`00bdc390`](#insn-00bdc390)
- ブロック [`00bdc390`](#insn-00bdc390) 範囲 `[['00bdc390', '00bdc393']]`
  - `FALL_THROUGH` [`00bdc390`](#insn-00bdc390) → [`00bdc394`](#insn-00bdc394)
- ブロック [`00bdc394`](#insn-00bdc394) 範囲 `[['00bdc394', '00bdc39b']]`
  - `UNCONDITIONAL_JUMP` [`00bdc398`](#insn-00bdc398) → [`00bdc3a0`](#insn-00bdc3a0)
- ブロック [`00bdc39c`](#insn-00bdc39c) 範囲 `[['00bdc39c', '00bdc39f']]`
  - `FALL_THROUGH` [`00bdc39c`](#insn-00bdc39c) → [`00bdc3a0`](#insn-00bdc3a0)
- ブロック [`00bdc3a0`](#insn-00bdc3a0) 範囲 `[['00bdc3a0', '00bdc3bb']]`
  - `FALL_THROUGH` [`00bdc3b8`](#insn-00bdc3b8) → [`00bdc3bc`](#insn-00bdc3bc)
- ブロック [`00bdc3bc`](#insn-00bdc3bc) 範囲 `[['00bdc3bc', '00bdc3bf']]`
  - `FALL_THROUGH` [`00bdc3bc`](#insn-00bdc3bc) → [`00bdc3c0`](#insn-00bdc3c0)
- ブロック [`00bdc3c0`](#insn-00bdc3c0) 範囲 `[['00bdc3c0', '00bdc3d3']]`
  - `FALL_THROUGH` [`00bdc3d0`](#insn-00bdc3d0) → [`00bdc3d4`](#insn-00bdc3d4)
- ブロック [`00bdc3d4`](#insn-00bdc3d4) 範囲 `[['00bdc3d4', '00bdc3db']]`
  - `FALL_THROUGH` [`00bdc3d8`](#insn-00bdc3d8) → [`00bdc3dc`](#insn-00bdc3dc)
- ブロック [`00bdc3dc`](#insn-00bdc3dc) 範囲 `[['00bdc3dc', '00bdc40f']]`
  - `CONDITIONAL_JUMP` [`00bdc40c`](#insn-00bdc40c) → [`00bdc430`](#insn-00bdc430)
  - `FALL_THROUGH` [`00bdc40c`](#insn-00bdc40c) → [`00bdc410`](#insn-00bdc410)
- ブロック [`00bdc410`](#insn-00bdc410) 範囲 `[['00bdc410', '00bdc42f']]`
- ブロック [`00bdc430`](#insn-00bdc430) 範囲 `[['00bdc430', '00bdc433']]`

## 命令位置別の参照

- [`00bdc1f0`](#insn-00bdc1f0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc1f4`](#insn-00bdc1f4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc1f8`](#insn-00bdc1f8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc1fc`](#insn-00bdc1fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc200`](#insn-00bdc200) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc204`](#insn-00bdc204) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc220`](#insn-00bdc220) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc22c`](#insn-00bdc22c) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdc244`](#insn-00bdc244) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc248`](#insn-00bdc248) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc24c`](#insn-00bdc24c) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc250`](#insn-00bdc250) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc254`](#insn-00bdc254) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc258`](#insn-00bdc258) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc25c`](#insn-00bdc25c) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc260`](#insn-00bdc260) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc264`](#insn-00bdc264) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc268`](#insn-00bdc268) → `Stack[-0x1b0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc26c`](#insn-00bdc26c) → `Stack[-0x1c0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc270`](#insn-00bdc270) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc274`](#insn-00bdc274) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc278`](#insn-00bdc278) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc27c`](#insn-00bdc27c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc280`](#insn-00bdc280) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc284`](#insn-00bdc284) → `Stack[-0x168]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc288`](#insn-00bdc288) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc28c`](#insn-00bdc28c) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc294`](#insn-00bdc294) → [`00c5dc30`](../00c5d/00c5dc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc30` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2ac`](#insn-00bdc2ac) → [`00c5deb0`](../00c5d/00c5deb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5deb0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2b4`](#insn-00bdc2b4) → [`00c5ab20`](../00c5a/00c5ab20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab20` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2bc`](#insn-00bdc2bc) → [`00c5ded0`](../00c5d/00c5ded0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ded0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2c4`](#insn-00bdc2c4) → [`00c5ded0`](../00c5d/00c5ded0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ded0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2c8`](#insn-00bdc2c8) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2d0`](#insn-00bdc2d0) → [`00c5bef0`](../00c5b/00c5bef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bef0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2d4`](#insn-00bdc2d4) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2d8`](#insn-00bdc2d8) → [`00bdc2e4`](#insn-00bdc2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2dc`](#insn-00bdc2dc) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2e0`](#insn-00bdc2e0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2e4`](#insn-00bdc2e4) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2e8`](#insn-00bdc2e8) → [`00bdc2f4`](#insn-00bdc2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2ec`](#insn-00bdc2ec) → `Stack[-0x1b0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2f0`](#insn-00bdc2f0) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bdc2fc`](#insn-00bdc2fc) → [`00bdbcd4`](../00bdb/00bdbcd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbcd4` · 推定シンボル `None` · 推定型 `None`
- [`00bdc310`](#insn-00bdc310) → [`00c5dda0`](../00c5d/00c5dda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dda0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc314`](#insn-00bdc314) → [`00bdc3d4`](#insn-00bdc3d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc324`](#insn-00bdc324) → `01126da0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdc334`](#insn-00bdc334) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdc348`](#insn-00bdc348) → [`00c5dda0`](../00c5d/00c5dda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dda0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc34c`](#insn-00bdc34c) → [`00bdc3c0`](#insn-00bdc3c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc358`](#insn-00bdc358) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc360`](#insn-00bdc360) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdc36c`](#insn-00bdc36c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bdc378`](#insn-00bdc378) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bdc380`](#insn-00bdc380) → `00c9baf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdc384`](#insn-00bdc384) → [`00bd48c8`](../00bd4/00bd48c8.md) · `DATA` · `ANALYSIS` · 関数 `00bd48c8` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bdc38c`](#insn-00bdc38c) → [`00bdc39c`](#insn-00bdc39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc398`](#insn-00bdc398) → [`00bdc3a0`](#insn-00bdc3a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc3a4`](#insn-00bdc3a4) → `00c9bb08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdc3a4`](#insn-00bdc3a4) → [`00bdcc18`](00bdcc18.md) · `PARAM` · `ANALYSIS` · 関数 `00bdcc18` · 推定シンボル `_ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bdc3b4`](#insn-00bdc3b4) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bdc3bc`](#insn-00bdc3bc) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdc3f4`](#insn-00bdc3f4) → [`00c5de00`](../00c5d/00c5de00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de00` · 推定シンボル `None` · 推定型 `None`
- [`00bdc3fc`](#insn-00bdc3fc) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdc404`](#insn-00bdc404) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc40c`](#insn-00bdc40c) → [`00bdc430`](#insn-00bdc430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc410`](#insn-00bdc410) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc414`](#insn-00bdc414) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc418`](#insn-00bdc418) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc41c`](#insn-00bdc41c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc420`](#insn-00bdc420) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc424`](#insn-00bdc424) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc430`](#insn-00bdc430) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdc1f0`](#insn-00bdc1f0)

~~~json
{
  "source": "00bdc1f0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc1f4`](#insn-00bdc1f4)

~~~json
{
  "source": "00bdc1f4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc1f8`](#insn-00bdc1f8)

~~~json
{
  "source": "00bdc1f8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc1fc`](#insn-00bdc1fc)

~~~json
{
  "source": "00bdc1fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc200`](#insn-00bdc200)

~~~json
{
  "source": "00bdc200",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc204`](#insn-00bdc204)

~~~json
{
  "source": "00bdc204",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc220`](#insn-00bdc220)

~~~json
{
  "source": "00bdc220",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc22c`](#insn-00bdc22c)

~~~json
{
  "source": "00bdc22c",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc244`](#insn-00bdc244)

~~~json
{
  "source": "00bdc244",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc248`](#insn-00bdc248)

~~~json
{
  "source": "00bdc248",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc24c`](#insn-00bdc24c)

~~~json
{
  "source": "00bdc24c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc250`](#insn-00bdc250)

~~~json
{
  "source": "00bdc250",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc254`](#insn-00bdc254)

~~~json
{
  "source": "00bdc254",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc258`](#insn-00bdc258)

~~~json
{
  "source": "00bdc258",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc25c`](#insn-00bdc25c)

~~~json
{
  "source": "00bdc25c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc260`](#insn-00bdc260)

~~~json
{
  "source": "00bdc260",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc264`](#insn-00bdc264)

~~~json
{
  "source": "00bdc264",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc268`](#insn-00bdc268)

~~~json
{
  "source": "00bdc268",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc26c`](#insn-00bdc26c)

~~~json
{
  "source": "00bdc26c",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc270`](#insn-00bdc270)

~~~json
{
  "source": "00bdc270",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc274`](#insn-00bdc274)

~~~json
{
  "source": "00bdc274",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc278`](#insn-00bdc278)

~~~json
{
  "source": "00bdc278",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc27c`](#insn-00bdc27c)

~~~json
{
  "source": "00bdc27c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc280`](#insn-00bdc280)

~~~json
{
  "source": "00bdc280",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc284`](#insn-00bdc284)

~~~json
{
  "source": "00bdc284",
  "target": "Stack[-0x168]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc288`](#insn-00bdc288)

~~~json
{
  "source": "00bdc288",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc28c`](#insn-00bdc28c)

~~~json
{
  "source": "00bdc28c",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc294`](#insn-00bdc294)

~~~json
{
  "source": "00bdc294",
  "target": "00c5dc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2ac`](#insn-00bdc2ac)

~~~json
{
  "source": "00bdc2ac",
  "target": "00c5deb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2b4`](#insn-00bdc2b4)

~~~json
{
  "source": "00bdc2b4",
  "target": "00c5ab20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2bc`](#insn-00bdc2bc)

~~~json
{
  "source": "00bdc2bc",
  "target": "00c5ded0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2c4`](#insn-00bdc2c4)

~~~json
{
  "source": "00bdc2c4",
  "target": "00c5ded0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2c8`](#insn-00bdc2c8)

~~~json
{
  "source": "00bdc2c8",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2d0`](#insn-00bdc2d0)

~~~json
{
  "source": "00bdc2d0",
  "target": "00c5bef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2d4`](#insn-00bdc2d4)

~~~json
{
  "source": "00bdc2d4",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2d8`](#insn-00bdc2d8)

~~~json
{
  "source": "00bdc2d8",
  "target": "00bdc2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2dc`](#insn-00bdc2dc)

~~~json
{
  "source": "00bdc2dc",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2e0`](#insn-00bdc2e0)

~~~json
{
  "source": "00bdc2e0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2e4`](#insn-00bdc2e4)

~~~json
{
  "source": "00bdc2e4",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2e8`](#insn-00bdc2e8)

~~~json
{
  "source": "00bdc2e8",
  "target": "00bdc2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2ec`](#insn-00bdc2ec)

~~~json
{
  "source": "00bdc2ec",
  "target": "Stack[-0x1b0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc2f0`](#insn-00bdc2f0)

~~~json
{
  "source": "00bdc2f0",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc2fc`](#insn-00bdc2fc)

~~~json
{
  "source": "00bdc2fc",
  "target": "00bdbcd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc310`](#insn-00bdc310)

~~~json
{
  "source": "00bdc310",
  "target": "00c5dda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc314`](#insn-00bdc314)

~~~json
{
  "source": "00bdc314",
  "target": "00bdc3d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc324`](#insn-00bdc324)

~~~json
{
  "source": "00bdc324",
  "target": "01126da0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126da0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdc334`](#insn-00bdc334)

~~~json
{
  "source": "00bdc334",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc348`](#insn-00bdc348)

~~~json
{
  "source": "00bdc348",
  "target": "00c5dda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc34c`](#insn-00bdc34c)

~~~json
{
  "source": "00bdc34c",
  "target": "00bdc3c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc358`](#insn-00bdc358)

~~~json
{
  "source": "00bdc358",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc360`](#insn-00bdc360)

~~~json
{
  "source": "00bdc360",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc36c`](#insn-00bdc36c)

~~~json
{
  "source": "00bdc36c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc378`](#insn-00bdc378)

~~~json
{
  "source": "00bdc378",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc380`](#insn-00bdc380)

~~~json
{
  "source": "00bdc380",
  "target": "00c9baf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9baf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdc384`](#insn-00bdc384)

~~~json
{
  "source": "00bdc384",
  "target": "00bd48c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc38c`](#insn-00bdc38c)

~~~json
{
  "source": "00bdc38c",
  "target": "00bdc39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc398`](#insn-00bdc398)

~~~json
{
  "source": "00bdc398",
  "target": "00bdc3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc3a4`](#insn-00bdc3a4)

~~~json
{
  "source": "00bdc3a4",
  "target": "00c9bb08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bb08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdc3a4`](#insn-00bdc3a4)

~~~json
{
  "source": "00bdc3a4",
  "target": "00bdcc18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc3b4`](#insn-00bdc3b4)

~~~json
{
  "source": "00bdc3b4",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc3bc`](#insn-00bdc3bc)

~~~json
{
  "source": "00bdc3bc",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc3f4`](#insn-00bdc3f4)

~~~json
{
  "source": "00bdc3f4",
  "target": "00c5de00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc3fc`](#insn-00bdc3fc)

~~~json
{
  "source": "00bdc3fc",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdc404`](#insn-00bdc404)

~~~json
{
  "source": "00bdc404",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc40c`](#insn-00bdc40c)

~~~json
{
  "source": "00bdc40c",
  "target": "00bdc430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc410`](#insn-00bdc410)

~~~json
{
  "source": "00bdc410",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc414`](#insn-00bdc414)

~~~json
{
  "source": "00bdc414",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc418`](#insn-00bdc418)

~~~json
{
  "source": "00bdc418",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc41c`](#insn-00bdc41c)

~~~json
{
  "source": "00bdc41c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc420`](#insn-00bdc420)

~~~json
{
  "source": "00bdc420",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc424`](#insn-00bdc424)

~~~json
{
  "source": "00bdc424",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc430`](#insn-00bdc430)

~~~json
{
  "source": "00bdc430",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
