# 006cfeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006cfeac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0005.md#compare-2195f49d5b0adf709adc0b60be8f03a2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `006cff44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cf/006cff44.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0032.md#compare-1979f669f4a092c83cf65c8b93035c8c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006cfeec",
  "name": "FUN_006cfeec",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a0d2d54ccded2e173f6a6f4672b2fb5c76b72ec714e4a6bc983da4842e92f45",
  "source_text_sha256": "7a0d2d54ccded2e173f6a6f4672b2fb5c76b72ec714e4a6bc983da4842e92f45",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006cfeec",
        "006d01e3"
      ],
      [
        "006d0248",
        "006d024b"
      ]
    ],
    "bytes_sha256": "e241ef384153e93d83972fbe7ccae2a20de8abc3102f3053ad4615f23cb0c4b1",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006d02a4](../006d0/006d02a4.md)
- [0089bc8c](../0089b/0089bc8c.md)
- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [006d7064](../006d7/006d7064.md)
- [006d7088](../006d7/006d7088.md)
- [006d76a0](../006d7/006d76a0.md)
- [006d777c](../006d7/006d777c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5a870](../00c5a/00c5a870.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5699 bytes

~~~c

void FUN_006cfeec(undefined8 param_1,byte *param_2)

{
  uint uVar1;
  uint uVar2;
  ulong uVar3;
  byte *pbVar4;
  uint uVar5;
  long lVar6;
  undefined *puVar7;
  long *plVar8;
  uint *puVar9;
  uint *puVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  uint *puVar14;
  ulong uVar15;
  ulong local_b0;
  ulong local_a8;
  uint *local_a0;
  byte local_98 [8];
  ulong local_90;
  uint *local_88;
  ulong local_80;
  undefined8 uStack_78;
  void *local_70;
  ulong local_68;
  undefined8 local_60;
  void *pvStack_58;
  long *local_50;
  undefined8 local_48;
  undefined8 uStack_40;
  long local_38;
  
                    /* catch() { ... } // from try @ 006cfe04 with catch @ 006cfef8
                       catch() { ... } // from try @ 006cfec4 with catch @ 006cfef8 */
  lVar6 = tpidr_el0;
  local_38 = *(long *)(lVar6 + 0x28);
                    /* try { // try from 006cff18 to 007cff2f has its CatchHandler @ 006cff18
                       catch() { ... } // from try @ 006cff18 with catch @ 006cff18
                       catch() { ... } // from try @ 006cff38 with catch @ 006cff18 */
  plVar8 = (long *)_Znwm(0x28);
  _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em(plVar8,0);
  puVar7 = PTR__ZTVNSt6__ndk118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EEE_00c9b540;
                    /* try { // try from 006cff30 to 007cff37 has its CatchHandler @ 006cff50 */
                    /* try { // try from 006cff38 to 007cff63 has its CatchHandler @ 006cff18 */
  plVar8[3] = 0x10ffff;
  uVar3 = *(ulong *)(param_2 + 8);
  pbVar4 = *(byte **)(param_2 + 0x10);
  *(undefined4 *)(plVar8 + 4) = 0;
  local_48 = 0;
  uStack_40 = 0;
  *plVar8 = (long)(puVar7 + 0x10);
                    /* catch() { ... } // from try @ 006cff30 with catch @ 006cff50 */
  uStack_78 = 0;
  local_80 = 0;
  local_68 = 0;
  local_70 = (void *)0x0;
  pvStack_58 = (void *)0x0;
  local_60 = 0;
  if ((*param_2 & 1) == 0) {
    pbVar4 = param_2 + 1;
    uVar3 = (ulong)(*param_2 >> 1);
  }
  local_50 = plVar8;
  FUN_006d7088(local_98,&local_80,pbVar4,pbVar4 + uVar3);
  uVar3 = (ulong)(local_98[0] >> 1);
  if ((local_98[0] & 1) != 0) {
    uVar3 = local_90;
  }
  if (0x3ffffffffffffff7 < uVar3) {
    if (*(long *)(lVar6 + 0x28) != local_38) goto LAB_006d0248;
    FUN_006d76a0(&local_b0);
LAB_006d01d0:
    if (*(long *)(lVar6 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      FUN_00440ec0();
    }
    goto LAB_006d0248;
  }
  if (uVar3 < 5) {
    puVar9 = (uint *)((ulong)&local_b0 | 4);
    local_b0 = CONCAT71(local_b0._1_7_,(char)((int)uVar3 << 1));
    if (uVar3 != 0) goto LAB_006cfff8;
  }
  else {
    uVar11 = (uVar3 & 0x3ffffffffffffffe) + 2;
    if ((uVar3 | 1) != 5) {
      uVar11 = uVar3 | 1;
    }
    if (0x3ffffffffffffffe < uVar11) goto LAB_006d01d0;
    puVar9 = (uint *)_Znwm((uVar11 + 1) * 4);
                    /* try { // try from 006cffec to 007d00f3 has its CatchHandler @ 006cffec
                       catch() { ... } // from try @ 006cffec with catch @ 006cffec
                       catch() { ... } // from try @ 006d0100 with catch @ 006cffec */
    local_b0 = uVar11 + 1 | 1;
    local_a8 = uVar3;
    local_a0 = puVar9;
LAB_006cfff8:
    puVar10 = puVar9;
    uVar11 = uVar3;
    if (7 < uVar3) {
      uVar12 = uVar3 & 0x3ffffffffffffff8;
      uVar11 = uVar3 & 7;
      puVar10 = puVar9 + uVar12;
      puVar14 = puVar9 + 4;
      uVar15 = uVar12;
      do {
        uVar15 = uVar15 - 8;
        puVar14[-2] = 0x20;
        puVar14[-1] = 0x20;
        puVar14[-4] = 0x20;
        puVar14[-3] = 0x20;
        puVar14[2] = 0x20;
        puVar14[3] = 0x20;
        puVar14[0] = 0x20;
        puVar14[1] = 0x20;
        puVar14 = puVar14 + 8;
      } while (uVar15 != 0);
      if (uVar3 == uVar12) goto LAB_006d0048;
    }
    do {
      uVar11 = uVar11 - 1;
      *puVar10 = 0x20;
      puVar10 = puVar10 + 1;
    } while (uVar11 != 0);
  }
LAB_006d0048:
  puVar9[uVar3] = 0;
  puVar9 = (uint *)((ulong)local_98 | 4);
  uVar3 = (ulong)(local_98[0] >> 1);
  if ((local_98[0] & 1) != 0) {
    puVar9 = local_88;
    uVar3 = local_90;
  }
  if (uVar3 != 0) {
    lVar13 = uVar3 << 2;
    puVar10 = (uint *)((ulong)&local_b0 | 4);
    if ((local_b0 & 1) != 0) {
      puVar10 = local_a0;
    }
    do {
      uVar5 = *puVar9;
      uVar1 = uVar5 - 0xfee0;
      uVar2 = uVar1;
      if (0x19 < uVar5 - 0xff41) {
        uVar2 = uVar5;
      }
      if (uVar5 - 0xff21 < 0x1a) {
        uVar2 = uVar1;
      }
      if (uVar5 - 0xff10 < 10) {
        uVar2 = uVar1;
      }
      uVar1 = uVar2 + 0x60;
      if (0x55 < uVar2 - 0x3041) {
        uVar1 = uVar2;
      }
      if (uVar2 - 0x41 < 0x1a) {
        uVar1 = uVar2 | 0x20;
      }
      lVar13 = lVar13 + -4;
                    /* try { // try from 006d00f4 to 007d00ff has its CatchHandler @ 006d01a8 */
      *puVar10 = uVar1;
      puVar9 = puVar9 + 1;
      puVar10 = puVar10 + 1;
    } while (lVar13 != 0);
  }
  uVar3 = local_b0 >> 1 & 0x7f;
  puVar9 = (uint *)((ulong)&local_b0 | 4);
  if ((local_b0 & 1) != 0) {
    uVar3 = local_a8;
    puVar9 = local_a0;
  }
  FUN_006d777c(param_1,&local_80,puVar9,puVar9 + uVar3);
  if ((local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_98[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 006d00f4 with catch @ 006d01a8 */
    _ZdlPv(local_88);
  }
  if (local_50 != (long *)0x0) {
    (**(code **)(*local_50 + 8))();
  }
  if ((local_68 & 1) != 0) {
    _ZdlPv(pvStack_58);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar6 + 0x28) == local_38) {
    return;
  }
LAB_006d0248:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006cfeec"></a> `006cfeec` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-006cfef0"></a> `006cfef0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006cfef4"></a> `006cfef4` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-006cfef8"></a> `006cfef8` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-006cfefc"></a> `006cfefc` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-006cff00"></a> `006cff00` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006cff04"></a> `006cff04` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-006cff08"></a> `006cff08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006cff0c"></a> `006cff0c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006cff10"></a> `006cff10` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-006cff14"></a> `006cff14` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006cff18"></a> `006cff18` | `de 1f 16 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-006cff1c"></a> `006cff1c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006cff20"></a> `006cff20` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-006cff24"></a> `006cff24` | `53 2a 16 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-006cff28"></a> `006cff28` | `68 2e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-006cff2c"></a> `006cff2c` | `e9 fd bf 12` | mov w9,#0x10ffff | `FALL_THROUGH`
<a id="insn-006cff30"></a> `006cff30` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-006cff34"></a> `006cff34` | `08 a1 42 f9` | ldr x8,[x8, #0x540] | `FALL_THROUGH`
<a id="insn-006cff38"></a> `006cff38` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-006cff3c"></a> `006cff3c` | `8a a6 40 a9` | ldp x10,x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006cff40"></a> `006cff40` | `bf 22 00 b9` | str wzr,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-006cff44"></a> `006cff44` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006cff48"></a> `006cff48` | `ff ff 06 a9` | stp xzr,xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-006cff4c"></a> `006cff4c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-006cff50"></a> `006cff50` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-006cff54"></a> `006cff54` | `e0 83 01 ad` | stp q0,q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006cff58"></a> `006cff58` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff5c"></a> `006cff5c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff60"></a> `006cff60` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006cff64"></a> `006cff64` | `21 15 94 9a` | csinc x1,x9,x20,ne | `FALL_THROUGH`
<a id="insn-006cff68"></a> `006cff68` | `f5 33 00 f9` | str x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006cff6c"></a> `006cff6c` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-006cff70"></a> `006cff70` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006cff74"></a> `006cff74` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-006cff78"></a> `006cff78` | `22 00 09 8b` | add x2,x1,x9 | `FALL_THROUGH`
<a id="insn-006cff7c"></a> `006cff7c` | `43 1c 00 94` | bl 0x006d7088 | `UNCONDITIONAL_CALL`
<a id="insn-006cff80"></a> `006cff80` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006cff84"></a> `006cff84` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006cff88"></a> `006cff88` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff8c"></a> `006cff8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff90"></a> `006cff90` | `e8 eb 7d b2` | orr x8,xzr,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006cff94"></a> `006cff94` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-006cff98"></a> `006cff98` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-006cff9c"></a> `006cff9c` | `e2 10 00 54` | b.cs 0x006d01b8 | `CONDITIONAL_JUMP`
<a id="insn-006cffa0"></a> `006cffa0` | `9f 16 00 f1` | cmp x20,#0x5 | `FALL_THROUGH`
<a id="insn-006cffa4"></a> `006cffa4` | `e2 00 00 54` | b.cs 0x006cffc0 | `CONDITIONAL_JUMP`
<a id="insn-006cffa8"></a> `006cffa8` | `88 7a 1f 53` | lsl w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-006cffac"></a> `006cffac` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-006cffb0"></a> `006cffb0` | `20 01 7e b2` | orr x0,x9,#0x4 | `FALL_THROUGH`
<a id="insn-006cffb4"></a> `006cffb4` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-006cffb8"></a> `006cffb8` | `14 02 00 b5` | cbnz x20,0x006cfff8 | `CONDITIONAL_JUMP`
<a id="insn-006cffbc"></a> `006cffbc` | `23 00 00 14` | b 0x006d0048 | `UNCONDITIONAL_JUMP`
<a id="insn-006cffc0"></a> `006cffc0` | `88 f2 7f 92` | and x8,x20,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-006cffc4"></a> `006cffc4` | `89 02 40 b2` | orr x9,x20,#0x1 | `FALL_THROUGH`
<a id="insn-006cffc8"></a> `006cffc8` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006cffcc"></a> `006cffcc` | `3f 15 00 f1` | cmp x9,#0x5 | `FALL_THROUGH`
<a id="insn-006cffd0"></a> `006cffd0` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-006cffd4"></a> `006cffd4` | `09 00 f8 92` | mov x9,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-006cffd8"></a> `006cffd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006cffdc"></a> `006cffdc` | `a2 0f 00 54` | b.cs 0x006d01d0 | `CONDITIONAL_JUMP`
<a id="insn-006cffe0"></a> `006cffe0` | `15 05 00 91` | add x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cffe4"></a> `006cffe4` | `a0 f6 7e d3` | lsl x0,x21,#0x2 | `FALL_THROUGH`
<a id="insn-006cffe8"></a> `006cffe8` | `aa 1f 16 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-006cffec"></a> `006cffec` | `a8 02 40 b2` | orr x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-006cfff0"></a> `006cfff0` | `f4 83 00 a9` | stp x20,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006cfff4"></a> `006cfff4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-006cfff8"></a> `006cfff8` | `9f 22 00 f1` | cmp x20,#0x8 | `FALL_THROUGH`
<a id="insn-006cfffc"></a> `006cfffc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-006d0000"></a> `006d0000` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-006d0004"></a> `006d0004` | `a3 01 00 54` | b.cc 0x006d0038 | `CONDITIONAL_JUMP`
<a id="insn-006d0008"></a> `006d0008` | `00 04 01 4f` | movi v0.4S,#0x20 | `FALL_THROUGH`
<a id="insn-006d000c"></a> `006d000c` | `8a ea 7d 92` | and x10,x20,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006d0010"></a> `006d0010` | `89 0a 40 92` | and x9,x20,#0x7 | `FALL_THROUGH`
<a id="insn-006d0014"></a> `006d0014` | `08 08 0a 8b` | add x8,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006d0018"></a> `006d0018` | `0b 40 00 91` | add x11,x0,#0x10 | `FALL_THROUGH`
<a id="insn-006d001c"></a> `006d001c` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-006d0020"></a> `006d0020` | `8c 21 00 f1` | subs x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-006d0024"></a> `006d0024` | `60 81 3f ad` | stp q0,q0,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-006d0028"></a> `006d0028` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-006d002c"></a> `006d002c` | `a1 ff ff 54` | b.ne 0x006d0020 | `CONDITIONAL_JUMP`
<a id="insn-006d0030"></a> `006d0030` | `9f 02 0a eb` | cmp x20,x10 | `FALL_THROUGH`
<a id="insn-006d0034"></a> `006d0034` | `a0 00 00 54` | b.eq 0x006d0048 | `CONDITIONAL_JUMP`
<a id="insn-006d0038"></a> `006d0038` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-006d003c"></a> `006d003c` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-006d0040"></a> `006d0040` | `0a 45 00 b8` | str w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-006d0044"></a> `006d0044` | `c1 ff ff 54` | b.ne 0x006d003c | `CONDITIONAL_JUMP`
<a id="insn-006d0048"></a> `006d0048` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d004c"></a> `006d004c` | `ec 2f 42 a9` | ldp x12,x11,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006d0050"></a> `006d0050` | `1f 78 34 b8` | str wzr,[x0, x20, LSL #0x2] | `FALL_THROUGH`
<a id="insn-006d0054"></a> `006d0054` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006d0058"></a> `006d0058` | `0d fd 41 d3` | lsr x13,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006d005c"></a> `006d005c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006d0060"></a> `006d0060` | `ea 03 40 39` | ldrb w10,[sp] | `FALL_THROUGH`
<a id="insn-006d0064"></a> `006d0064` | `29 01 7e b2` | orr x9,x9,#0x4 | `FALL_THROUGH`
<a id="insn-006d0068"></a> `006d0068` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-006d006c"></a> `006d006c` | `ac 01 8c 9a` | csel x12,x13,x12,eq | `FALL_THROUGH`
<a id="insn-006d0070"></a> `006d0070` | `ed 0b 40 f9` | ldr x13,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d0074"></a> `006d0074` | `29 01 8b 9a` | csel x9,x9,x11,eq | `FALL_THROUGH`
<a id="insn-006d0078"></a> `006d0078` | `4b 01 00 12` | and w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d007c"></a> `006d007c` | `08 01 7e b2` | orr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-006d0080"></a> `006d0080` | `4c 04 00 b4` | cbz x12,0x006d0108 | `CONDITIONAL_JUMP`
<a id="insn-006d0084"></a> `006d0084` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-006d0088"></a> `006d0088` | `8a f5 7e d3` | lsl x10,x12,#0x2 | `FALL_THROUGH`
<a id="insn-006d008c"></a> `006d008c` | `eb e1 9f 12` | mov w11,#0xffff00f0 | `FALL_THROUGH`
<a id="insn-006d0090"></a> `006d0090` | `0c e4 9f 12` | mov w12,#0xffff00df | `FALL_THROUGH`
<a id="insn-006d0094"></a> `006d0094` | `0d 01 8d 9a` | csel x13,x8,x13,eq | `FALL_THROUGH`
<a id="insn-006d0098"></a> `006d0098` | `0e e8 9f 12` | mov w14,#0xffff00bf | `FALL_THROUGH`
<a id="insn-006d009c"></a> `006d009c` | `ef db 9f 12` | mov w15,#0xffff0120 | `FALL_THROUGH`
<a id="insn-006d00a0"></a> `006d00a0` | `10 08 86 12` | mov w16,#0xffffcfbf | `FALL_THROUGH`
<a id="insn-006d00a4"></a> `006d00a4` | `31 45 40 b8` | ldr w17,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-006d00a8"></a> `006d00a8` | `20 02 0e 0b` | add w0,w17,w14 | `FALL_THROUGH`
<a id="insn-006d00ac"></a> `006d00ac` | `21 02 0c 0b` | add w1,w17,w12 | `FALL_THROUGH`
<a id="insn-006d00b0"></a> `006d00b0` | `22 02 0f 0b` | add w2,w17,w15 | `FALL_THROUGH`
<a id="insn-006d00b4"></a> `006d00b4` | `1f 68 00 71` | cmp w0,#0x1a | `FALL_THROUGH`
<a id="insn-006d00b8"></a> `006d00b8` | `20 02 0b 0b` | add w0,w17,w11 | `FALL_THROUGH`
<a id="insn-006d00bc"></a> `006d00bc` | `51 30 91 1a` | csel w17,w2,w17,cc | `FALL_THROUGH`
<a id="insn-006d00c0"></a> `006d00c0` | `3f 64 00 71` | cmp w1,#0x19 | `FALL_THROUGH`
<a id="insn-006d00c4"></a> `006d00c4` | `31 82 82 1a` | csel w17,w17,w2,hi | `FALL_THROUGH`
<a id="insn-006d00c8"></a> `006d00c8` | `1f 24 00 71` | cmp w0,#0x9 | `FALL_THROUGH`
<a id="insn-006d00cc"></a> `006d00cc` | `31 82 82 1a` | csel w17,w17,w2,hi | `FALL_THROUGH`
<a id="insn-006d00d0"></a> `006d00d0` | `20 02 10 0b` | add w0,w17,w16 | `FALL_THROUGH`
<a id="insn-006d00d4"></a> `006d00d4` | `21 06 01 51` | sub w1,w17,#0x41 | `FALL_THROUGH`
<a id="insn-006d00d8"></a> `006d00d8` | `22 82 01 11` | add w2,w17,#0x60 | `FALL_THROUGH`
<a id="insn-006d00dc"></a> `006d00dc` | `1f 58 01 71` | cmp w0,#0x56 | `FALL_THROUGH`
<a id="insn-006d00e0"></a> `006d00e0` | `40 30 91 1a` | csel w0,w2,w17,cc | `FALL_THROUGH`
<a id="insn-006d00e4"></a> `006d00e4` | `31 02 1b 32` | orr w17,w17,#0x20 | `FALL_THROUGH`
<a id="insn-006d00e8"></a> `006d00e8` | `3f 64 00 71` | cmp w1,#0x19 | `FALL_THROUGH`
<a id="insn-006d00ec"></a> `006d00ec` | `11 80 91 1a` | csel w17,w0,w17,hi | `FALL_THROUGH`
<a id="insn-006d00f0"></a> `006d00f0` | `4a 11 00 f1` | subs x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-006d00f4"></a> `006d00f4` | `b1 45 00 b8` | str w17,[x13], #0x4 | `FALL_THROUGH`
<a id="insn-006d00f8"></a> `006d00f8` | `61 fd ff 54` | b.ne 0x006d00a4 | `CONDITIONAL_JUMP`
<a id="insn-006d00fc"></a> `006d00fc` | `ea 03 40 39` | ldrb w10,[sp] | `FALL_THROUGH`
<a id="insn-006d0100"></a> `006d0100` | `ed 0b 40 f9` | ldr x13,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d0104"></a> `006d0104` | `4b 01 00 12` | and w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d0108"></a> `006d0108` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006d010c"></a> `006d010c` | `4a 7d 01 53` | lsr w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d0110"></a> `006d0110` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-006d0114"></a> `006d0114` | `01 01 8d 9a` | csel x1,x8,x13,eq | `FALL_THROUGH`
<a id="insn-006d0118"></a> `006d0118` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-006d011c"></a> `006d011c` | `22 08 08 8b` | add x2,x1,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006d0120"></a> `006d0120` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-006d0124"></a> `006d0124` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-006d0128"></a> `006d0128` | `95 1d 00 94` | bl 0x006d777c | `UNCONDITIONAL_CALL`
<a id="insn-006d012c"></a> `006d012c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006d0130"></a> `006d0130` | `28 03 00 37` | tbnz w8,#0x0,0x006d0194 | `CONDITIONAL_JUMP`
<a id="insn-006d0134"></a> `006d0134` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d0138"></a> `006d0138` | `68 03 00 37` | tbnz w8,#0x0,0x006d01a4 | `CONDITIONAL_JUMP`
<a id="insn-006d013c"></a> `006d013c` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006d0140"></a> `006d0140` | `80 00 00 b4` | cbz x0,0x006d0150 | `CONDITIONAL_JUMP`
<a id="insn-006d0144"></a> `006d0144` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-006d0148"></a> `006d0148` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-006d014c"></a> `006d014c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006d0150"></a> `006d0150` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-006d0154"></a> `006d0154` | `68 00 00 36` | tbz w8,#0x0,0x006d0160 | `CONDITIONAL_JUMP`
<a id="insn-006d0158"></a> `006d0158` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-006d015c"></a> `006d015c` | `55 1f 16 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-006d0160"></a> `006d0160` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006d0164"></a> `006d0164` | `68 00 00 36` | tbz w8,#0x0,0x006d0170 | `CONDITIONAL_JUMP`
<a id="insn-006d0168"></a> `006d0168` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006d016c"></a> `006d016c` | `51 1f 16 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-006d0170"></a> `006d0170` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d0174"></a> `006d0174` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d0178"></a> `006d0178` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d017c"></a> `006d017c` | `61 06 00 54` | b.ne 0x006d0248 | `CONDITIONAL_JUMP`
<a id="insn-006d0180"></a> `006d0180` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-006d0184"></a> `006d0184` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-006d0188"></a> `006d0188` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006d018c"></a> `006d018c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-006d0190"></a> `006d0190` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006d0194"></a> `006d0194` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d0198"></a> `006d0198` | `46 1f 16 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-006d019c"></a> `006d019c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d01a0"></a> `006d01a0` | `e8 fc 07 36` | tbz w8,#0x0,0x006d013c | `CONDITIONAL_JUMP`
<a id="insn-006d01a4"></a> `006d01a4` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006d01a8"></a> `006d01a8` | `42 1f 16 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-006d01ac"></a> `006d01ac` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006d01b0"></a> `006d01b0` | `a0 fc ff b5` | cbnz x0,0x006d0144 | `CONDITIONAL_JUMP`
<a id="insn-006d01b4"></a> `006d01b4` | `e7 ff ff 17` | b 0x006d0150 | `UNCONDITIONAL_JUMP`
<a id="insn-006d01b8"></a> `006d01b8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d01bc"></a> `006d01bc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d01c0"></a> `006d01c0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d01c4"></a> `006d01c4` | `21 04 00 54` | b.ne 0x006d0248 | `CONDITIONAL_JUMP`
<a id="insn-006d01c8"></a> `006d01c8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-006d01cc"></a> `006d01cc` | `35 1d 00 94` | bl 0x006d76a0 | `UNCONDITIONAL_CALL`
<a id="insn-006d01d0"></a> `006d01d0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d01d4"></a> `006d01d4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d01d8"></a> `006d01d8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d01dc"></a> `006d01dc` | `61 03 00 54` | b.ne 0x006d0248 | `CONDITIONAL_JUMP`
<a id="insn-006d01e0"></a> `006d01e0` | `38 c3 f5 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-006d0248"></a> `006d0248` | `26 1f 16 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006cfeec`](#insn-006cfeec) 範囲 `[['006cfeec', '006cfef7']]`
  - `FALL_THROUGH` [`006cfef4`](#insn-006cfef4) → [`006cfef8`](#insn-006cfef8)
- ブロック [`006cfef8`](#insn-006cfef8) 範囲 `[['006cfef8', '006cff17']]`
  - `FALL_THROUGH` [`006cff14`](#insn-006cff14) → [`006cff18`](#insn-006cff18)
- ブロック [`006cff18`](#insn-006cff18) 範囲 `[['006cff18', '006cff2f']]`
  - `FALL_THROUGH` [`006cff2c`](#insn-006cff2c) → [`006cff30`](#insn-006cff30)
- ブロック [`006cff30`](#insn-006cff30) 範囲 `[['006cff30', '006cff37']]`
  - `FALL_THROUGH` [`006cff34`](#insn-006cff34) → [`006cff38`](#insn-006cff38)
- ブロック [`006cff38`](#insn-006cff38) 範囲 `[['006cff38', '006cff4f']]`
  - `FALL_THROUGH` [`006cff4c`](#insn-006cff4c) → [`006cff50`](#insn-006cff50)
- ブロック [`006cff50`](#insn-006cff50) 範囲 `[['006cff50', '006cff9f']]`
  - `CONDITIONAL_JUMP` [`006cff9c`](#insn-006cff9c) → [`006d01b8`](#insn-006d01b8)
  - `FALL_THROUGH` [`006cff9c`](#insn-006cff9c) → [`006cffa0`](#insn-006cffa0)
- ブロック [`006cffa0`](#insn-006cffa0) 範囲 `[['006cffa0', '006cffa7']]`
  - `CONDITIONAL_JUMP` [`006cffa4`](#insn-006cffa4) → [`006cffc0`](#insn-006cffc0)
  - `FALL_THROUGH` [`006cffa4`](#insn-006cffa4) → [`006cffa8`](#insn-006cffa8)
- ブロック [`006cffa8`](#insn-006cffa8) 範囲 `[['006cffa8', '006cffbb']]`
  - `CONDITIONAL_JUMP` [`006cffb8`](#insn-006cffb8) → [`006cfff8`](#insn-006cfff8)
  - `FALL_THROUGH` [`006cffb8`](#insn-006cffb8) → [`006cffbc`](#insn-006cffbc)
- ブロック [`006cffbc`](#insn-006cffbc) 範囲 `[['006cffbc', '006cffbf']]`
  - `UNCONDITIONAL_JUMP` [`006cffbc`](#insn-006cffbc) → [`006d0048`](#insn-006d0048)
- ブロック [`006cffc0`](#insn-006cffc0) 範囲 `[['006cffc0', '006cffdf']]`
  - `CONDITIONAL_JUMP` [`006cffdc`](#insn-006cffdc) → [`006d01d0`](#insn-006d01d0)
  - `FALL_THROUGH` [`006cffdc`](#insn-006cffdc) → [`006cffe0`](#insn-006cffe0)
- ブロック [`006cffe0`](#insn-006cffe0) 範囲 `[['006cffe0', '006cffeb']]`
  - `FALL_THROUGH` [`006cffe8`](#insn-006cffe8) → [`006cffec`](#insn-006cffec)
- ブロック [`006cffec`](#insn-006cffec) 範囲 `[['006cffec', '006cfff7']]`
  - `FALL_THROUGH` [`006cfff4`](#insn-006cfff4) → [`006cfff8`](#insn-006cfff8)
- ブロック [`006cfff8`](#insn-006cfff8) 範囲 `[['006cfff8', '006d0007']]`
  - `CONDITIONAL_JUMP` [`006d0004`](#insn-006d0004) → [`006d0038`](#insn-006d0038)
  - `FALL_THROUGH` [`006d0004`](#insn-006d0004) → [`006d0008`](#insn-006d0008)
- ブロック [`006d0008`](#insn-006d0008) 範囲 `[['006d0008', '006d001f']]`
  - `FALL_THROUGH` [`006d001c`](#insn-006d001c) → [`006d0020`](#insn-006d0020)
- ブロック [`006d0020`](#insn-006d0020) 範囲 `[['006d0020', '006d002f']]`
  - `CONDITIONAL_JUMP` [`006d002c`](#insn-006d002c) → [`006d0020`](#insn-006d0020)
  - `FALL_THROUGH` [`006d002c`](#insn-006d002c) → [`006d0030`](#insn-006d0030)
- ブロック [`006d0030`](#insn-006d0030) 範囲 `[['006d0030', '006d0037']]`
  - `CONDITIONAL_JUMP` [`006d0034`](#insn-006d0034) → [`006d0048`](#insn-006d0048)
  - `FALL_THROUGH` [`006d0034`](#insn-006d0034) → [`006d0038`](#insn-006d0038)
- ブロック [`006d0038`](#insn-006d0038) 範囲 `[['006d0038', '006d003b']]`
  - `FALL_THROUGH` [`006d0038`](#insn-006d0038) → [`006d003c`](#insn-006d003c)
- ブロック [`006d003c`](#insn-006d003c) 範囲 `[['006d003c', '006d0047']]`
  - `CONDITIONAL_JUMP` [`006d0044`](#insn-006d0044) → [`006d003c`](#insn-006d003c)
  - `FALL_THROUGH` [`006d0044`](#insn-006d0044) → [`006d0048`](#insn-006d0048)
- ブロック [`006d0048`](#insn-006d0048) 範囲 `[['006d0048', '006d0083']]`
  - `CONDITIONAL_JUMP` [`006d0080`](#insn-006d0080) → [`006d0108`](#insn-006d0108)
  - `FALL_THROUGH` [`006d0080`](#insn-006d0080) → [`006d0084`](#insn-006d0084)
- ブロック [`006d0084`](#insn-006d0084) 範囲 `[['006d0084', '006d00a3']]`
  - `FALL_THROUGH` [`006d00a0`](#insn-006d00a0) → [`006d00a4`](#insn-006d00a4)
- ブロック [`006d00a4`](#insn-006d00a4) 範囲 `[['006d00a4', '006d00f3']]`
  - `FALL_THROUGH` [`006d00f0`](#insn-006d00f0) → [`006d00f4`](#insn-006d00f4)
- ブロック [`006d00f4`](#insn-006d00f4) 範囲 `[['006d00f4', '006d00fb']]`
  - `CONDITIONAL_JUMP` [`006d00f8`](#insn-006d00f8) → [`006d00a4`](#insn-006d00a4)
  - `FALL_THROUGH` [`006d00f8`](#insn-006d00f8) → [`006d00fc`](#insn-006d00fc)
- ブロック [`006d00fc`](#insn-006d00fc) 範囲 `[['006d00fc', '006d00ff']]`
  - `FALL_THROUGH` [`006d00fc`](#insn-006d00fc) → [`006d0100`](#insn-006d0100)
- ブロック [`006d0100`](#insn-006d0100) 範囲 `[['006d0100', '006d0107']]`
  - `FALL_THROUGH` [`006d0104`](#insn-006d0104) → [`006d0108`](#insn-006d0108)
- ブロック [`006d0108`](#insn-006d0108) 範囲 `[['006d0108', '006d0133']]`
  - `CONDITIONAL_JUMP` [`006d0130`](#insn-006d0130) → [`006d0194`](#insn-006d0194)
  - `FALL_THROUGH` [`006d0130`](#insn-006d0130) → [`006d0134`](#insn-006d0134)
- ブロック [`006d0134`](#insn-006d0134) 範囲 `[['006d0134', '006d013b']]`
  - `CONDITIONAL_JUMP` [`006d0138`](#insn-006d0138) → [`006d01a4`](#insn-006d01a4)
  - `FALL_THROUGH` [`006d0138`](#insn-006d0138) → [`006d013c`](#insn-006d013c)
- ブロック [`006d013c`](#insn-006d013c) 範囲 `[['006d013c', '006d0143']]`
  - `CONDITIONAL_JUMP` [`006d0140`](#insn-006d0140) → [`006d0150`](#insn-006d0150)
  - `FALL_THROUGH` [`006d0140`](#insn-006d0140) → [`006d0144`](#insn-006d0144)
- ブロック [`006d0144`](#insn-006d0144) 範囲 `[['006d0144', '006d014f']]`
  - `FALL_THROUGH` [`006d014c`](#insn-006d014c) → [`006d0150`](#insn-006d0150)
- ブロック [`006d0150`](#insn-006d0150) 範囲 `[['006d0150', '006d0157']]`
  - `CONDITIONAL_JUMP` [`006d0154`](#insn-006d0154) → [`006d0160`](#insn-006d0160)
  - `FALL_THROUGH` [`006d0154`](#insn-006d0154) → [`006d0158`](#insn-006d0158)
- ブロック [`006d0158`](#insn-006d0158) 範囲 `[['006d0158', '006d015f']]`
  - `FALL_THROUGH` [`006d015c`](#insn-006d015c) → [`006d0160`](#insn-006d0160)
- ブロック [`006d0160`](#insn-006d0160) 範囲 `[['006d0160', '006d0167']]`
  - `CONDITIONAL_JUMP` [`006d0164`](#insn-006d0164) → [`006d0170`](#insn-006d0170)
  - `FALL_THROUGH` [`006d0164`](#insn-006d0164) → [`006d0168`](#insn-006d0168)
- ブロック [`006d0168`](#insn-006d0168) 範囲 `[['006d0168', '006d016f']]`
  - `FALL_THROUGH` [`006d016c`](#insn-006d016c) → [`006d0170`](#insn-006d0170)
- ブロック [`006d0170`](#insn-006d0170) 範囲 `[['006d0170', '006d017f']]`
  - `CONDITIONAL_JUMP` [`006d017c`](#insn-006d017c) → [`006d0248`](#insn-006d0248)
  - `FALL_THROUGH` [`006d017c`](#insn-006d017c) → [`006d0180`](#insn-006d0180)
- ブロック [`006d0180`](#insn-006d0180) 範囲 `[['006d0180', '006d0193']]`
- ブロック [`006d0194`](#insn-006d0194) 範囲 `[['006d0194', '006d01a3']]`
  - `CONDITIONAL_JUMP` [`006d01a0`](#insn-006d01a0) → [`006d013c`](#insn-006d013c)
  - `FALL_THROUGH` [`006d01a0`](#insn-006d01a0) → [`006d01a4`](#insn-006d01a4)
- ブロック [`006d01a4`](#insn-006d01a4) 範囲 `[['006d01a4', '006d01a7']]`
  - `FALL_THROUGH` [`006d01a4`](#insn-006d01a4) → [`006d01a8`](#insn-006d01a8)
- ブロック [`006d01a8`](#insn-006d01a8) 範囲 `[['006d01a8', '006d01b3']]`
  - `CONDITIONAL_JUMP` [`006d01b0`](#insn-006d01b0) → [`006d0144`](#insn-006d0144)
  - `FALL_THROUGH` [`006d01b0`](#insn-006d01b0) → [`006d01b4`](#insn-006d01b4)
- ブロック [`006d01b4`](#insn-006d01b4) 範囲 `[['006d01b4', '006d01b7']]`
  - `UNCONDITIONAL_JUMP` [`006d01b4`](#insn-006d01b4) → [`006d0150`](#insn-006d0150)
- ブロック [`006d01b8`](#insn-006d01b8) 範囲 `[['006d01b8', '006d01c7']]`
  - `CONDITIONAL_JUMP` [`006d01c4`](#insn-006d01c4) → [`006d0248`](#insn-006d0248)
  - `FALL_THROUGH` [`006d01c4`](#insn-006d01c4) → [`006d01c8`](#insn-006d01c8)
- ブロック [`006d01c8`](#insn-006d01c8) 範囲 `[['006d01c8', '006d01cf']]`
  - `FALL_THROUGH` [`006d01cc`](#insn-006d01cc) → [`006d01d0`](#insn-006d01d0)
- ブロック [`006d01d0`](#insn-006d01d0) 範囲 `[['006d01d0', '006d01df']]`
  - `CONDITIONAL_JUMP` [`006d01dc`](#insn-006d01dc) → [`006d0248`](#insn-006d0248)
  - `FALL_THROUGH` [`006d01dc`](#insn-006d01dc) → [`006d01e0`](#insn-006d01e0)
- ブロック [`006d01e0`](#insn-006d01e0) 範囲 `[['006d01e0', '006d01e3']]`
- ブロック [`006d0248`](#insn-006d0248) 範囲 `[['006d0248', '006d024b']]`

## 命令位置別の参照

- [`006cfef0`](#insn-006cfef0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfef4`](#insn-006cfef4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfef8`](#insn-006cfef8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff14`](#insn-006cff14) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff18`](#insn-006cff18) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`006cff24`](#insn-006cff24) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`006cff34`](#insn-006cff34) → `00c9b540`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006cff38`](#insn-006cff38) → `0010ffff`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6813]`
- [`006cff48`](#insn-006cff48) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff4c`](#insn-006cff4c) → `00c762a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[96]`
- [`006cff54`](#insn-006cff54) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff60`](#insn-006cff60) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff68`](#insn-006cff68) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff7c`](#insn-006cff7c) → [`006d7088`](../006d7/006d7088.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d7088` · 推定シンボル `None` · 推定型 `None`
- [`006cff80`](#insn-006cff80) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff84`](#insn-006cff84) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff9c`](#insn-006cff9c) → [`006d01b8`](#insn-006d01b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffa4`](#insn-006cffa4) → [`006cffc0`](#insn-006cffc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffb4`](#insn-006cffb4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffb8`](#insn-006cffb8) → [`006cfff8`](#insn-006cfff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffbc`](#insn-006cffbc) → [`006d0048`](#insn-006d0048) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffdc`](#insn-006cffdc) → [`006d01d0`](#insn-006d01d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffe8`](#insn-006cffe8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`006cfff0`](#insn-006cfff0) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfff4`](#insn-006cfff4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0004`](#insn-006d0004) → [`006d0038`](#insn-006d0038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d002c`](#insn-006d002c) → [`006d0020`](#insn-006d0020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0034`](#insn-006d0034) → [`006d0048`](#insn-006d0048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0044`](#insn-006d0044) → [`006d003c`](#insn-006d003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0048`](#insn-006d0048) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d004c`](#insn-006d004c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0060`](#insn-006d0060) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0070`](#insn-006d0070) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0080`](#insn-006d0080) → [`006d0108`](#insn-006d0108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00f8`](#insn-006d00f8) → [`006d00a4`](#insn-006d00a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00fc`](#insn-006d00fc) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0100`](#insn-006d0100) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0108`](#insn-006d0108) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0128`](#insn-006d0128) → [`006d777c`](../006d7/006d777c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d777c` · 推定シンボル `None` · 推定型 `None`
- [`006d012c`](#insn-006d012c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0130`](#insn-006d0130) → [`006d0194`](#insn-006d0194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0134`](#insn-006d0134) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0138`](#insn-006d0138) → [`006d01a4`](#insn-006d01a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d013c`](#insn-006d013c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0140`](#insn-006d0140) → [`006d0150`](#insn-006d0150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0148`](#insn-006d0148) → `00c762a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[96]`
- [`006d014c`](#insn-006d014c) → [`006d7064`](../006d7/006d7064.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `006d7064` · 推定シンボル `None` · 推定型 `None`
- [`006d0150`](#insn-006d0150) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0154`](#insn-006d0154) → [`006d0160`](#insn-006d0160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0158`](#insn-006d0158) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d015c`](#insn-006d015c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`006d0160`](#insn-006d0160) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0164`](#insn-006d0164) → [`006d0170`](#insn-006d0170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0168`](#insn-006d0168) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d016c`](#insn-006d016c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`006d0174`](#insn-006d0174) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d017c`](#insn-006d017c) → [`006d0248`](#insn-006d0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0180`](#insn-006d0180) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0184`](#insn-006d0184) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0188`](#insn-006d0188) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0194`](#insn-006d0194) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0198`](#insn-006d0198) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`006d019c`](#insn-006d019c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01a0`](#insn-006d01a0) → [`006d013c`](#insn-006d013c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01a4`](#insn-006d01a4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01a8`](#insn-006d01a8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`006d01ac`](#insn-006d01ac) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01b0`](#insn-006d01b0) → [`006d0144`](#insn-006d0144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01b4`](#insn-006d01b4) → [`006d0150`](#insn-006d0150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01bc`](#insn-006d01bc) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01c4`](#insn-006d01c4) → [`006d0248`](#insn-006d0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01cc`](#insn-006d01cc) → [`006d76a0`](../006d7/006d76a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d76a0` · 推定シンボル `None` · 推定型 `None`
- [`006d01d4`](#insn-006d01d4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01dc`](#insn-006d01dc) → [`006d0248`](#insn-006d0248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01e0`](#insn-006d01e0) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`006d0248`](#insn-006d0248) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006cfef0`](#insn-006cfef0)

~~~json
{
  "source": "006cfef0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfef4`](#insn-006cfef4)

~~~json
{
  "source": "006cfef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfef8`](#insn-006cfef8)

~~~json
{
  "source": "006cfef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff14`](#insn-006cff14)

~~~json
{
  "source": "006cff14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff18`](#insn-006cff18)

~~~json
{
  "source": "006cff18",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cff24`](#insn-006cff24)

~~~json
{
  "source": "006cff24",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cff34`](#insn-006cff34)

~~~json
{
  "source": "006cff34",
  "target": "00c9b540",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b540",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006cff38`](#insn-006cff38)

~~~json
{
  "source": "006cff38",
  "target": "0010ffff",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "001002f8",
  "offset": 64775,
  "size": 163512,
  "datatype": "Elf64_Sym[6813]",
  "bytes": "0000000000000000000000000000000000000000000000000100000012000000",
  "capture_start": "001002f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006cff48`](#insn-006cff48)

~~~json
{
  "source": "006cff48",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff4c`](#insn-006cff4c)

~~~json
{
  "source": "006cff4c",
  "target": "00c762a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c76290",
  "offset": 16,
  "size": 96,
  "datatype": "undefined1[96]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006cff54`](#insn-006cff54)

~~~json
{
  "source": "006cff54",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff60`](#insn-006cff60)

~~~json
{
  "source": "006cff60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff68`](#insn-006cff68)

~~~json
{
  "source": "006cff68",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff7c`](#insn-006cff7c)

~~~json
{
  "source": "006cff7c",
  "target": "006d7088",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cff80`](#insn-006cff80)

~~~json
{
  "source": "006cff80",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff84`](#insn-006cff84)

~~~json
{
  "source": "006cff84",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff9c`](#insn-006cff9c)

~~~json
{
  "source": "006cff9c",
  "target": "006d01b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffa4`](#insn-006cffa4)

~~~json
{
  "source": "006cffa4",
  "target": "006cffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffb4`](#insn-006cffb4)

~~~json
{
  "source": "006cffb4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffb8`](#insn-006cffb8)

~~~json
{
  "source": "006cffb8",
  "target": "006cfff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffbc`](#insn-006cffbc)

~~~json
{
  "source": "006cffbc",
  "target": "006d0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffdc`](#insn-006cffdc)

~~~json
{
  "source": "006cffdc",
  "target": "006d01d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffe8`](#insn-006cffe8)

~~~json
{
  "source": "006cffe8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cfff0`](#insn-006cfff0)

~~~json
{
  "source": "006cfff0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfff4`](#insn-006cfff4)

~~~json
{
  "source": "006cfff4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0004`](#insn-006d0004)

~~~json
{
  "source": "006d0004",
  "target": "006d0038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d002c`](#insn-006d002c)

~~~json
{
  "source": "006d002c",
  "target": "006d0020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0034`](#insn-006d0034)

~~~json
{
  "source": "006d0034",
  "target": "006d0048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0044`](#insn-006d0044)

~~~json
{
  "source": "006d0044",
  "target": "006d003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0048`](#insn-006d0048)

~~~json
{
  "source": "006d0048",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d004c`](#insn-006d004c)

~~~json
{
  "source": "006d004c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0060`](#insn-006d0060)

~~~json
{
  "source": "006d0060",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0070`](#insn-006d0070)

~~~json
{
  "source": "006d0070",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0080`](#insn-006d0080)

~~~json
{
  "source": "006d0080",
  "target": "006d0108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00f8`](#insn-006d00f8)

~~~json
{
  "source": "006d00f8",
  "target": "006d00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00fc`](#insn-006d00fc)

~~~json
{
  "source": "006d00fc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0100`](#insn-006d0100)

~~~json
{
  "source": "006d0100",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0108`](#insn-006d0108)

~~~json
{
  "source": "006d0108",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0128`](#insn-006d0128)

~~~json
{
  "source": "006d0128",
  "target": "006d777c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d012c`](#insn-006d012c)

~~~json
{
  "source": "006d012c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0130`](#insn-006d0130)

~~~json
{
  "source": "006d0130",
  "target": "006d0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0134`](#insn-006d0134)

~~~json
{
  "source": "006d0134",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0138`](#insn-006d0138)

~~~json
{
  "source": "006d0138",
  "target": "006d01a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d013c`](#insn-006d013c)

~~~json
{
  "source": "006d013c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0140`](#insn-006d0140)

~~~json
{
  "source": "006d0140",
  "target": "006d0150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0148`](#insn-006d0148)

~~~json
{
  "source": "006d0148",
  "target": "00c762a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c76290",
  "offset": 24,
  "size": 96,
  "datatype": "undefined1[96]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006d014c`](#insn-006d014c)

~~~json
{
  "source": "006d014c",
  "target": "006d7064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0150`](#insn-006d0150)

~~~json
{
  "source": "006d0150",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0154`](#insn-006d0154)

~~~json
{
  "source": "006d0154",
  "target": "006d0160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0158`](#insn-006d0158)

~~~json
{
  "source": "006d0158",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d015c`](#insn-006d015c)

~~~json
{
  "source": "006d015c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0160`](#insn-006d0160)

~~~json
{
  "source": "006d0160",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0164`](#insn-006d0164)

~~~json
{
  "source": "006d0164",
  "target": "006d0170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0168`](#insn-006d0168)

~~~json
{
  "source": "006d0168",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d016c`](#insn-006d016c)

~~~json
{
  "source": "006d016c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0174`](#insn-006d0174)

~~~json
{
  "source": "006d0174",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d017c`](#insn-006d017c)

~~~json
{
  "source": "006d017c",
  "target": "006d0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0180`](#insn-006d0180)

~~~json
{
  "source": "006d0180",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0184`](#insn-006d0184)

~~~json
{
  "source": "006d0184",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0188`](#insn-006d0188)

~~~json
{
  "source": "006d0188",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0194`](#insn-006d0194)

~~~json
{
  "source": "006d0194",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0198`](#insn-006d0198)

~~~json
{
  "source": "006d0198",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d019c`](#insn-006d019c)

~~~json
{
  "source": "006d019c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01a0`](#insn-006d01a0)

~~~json
{
  "source": "006d01a0",
  "target": "006d013c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01a4`](#insn-006d01a4)

~~~json
{
  "source": "006d01a4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01a8`](#insn-006d01a8)

~~~json
{
  "source": "006d01a8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d01ac`](#insn-006d01ac)

~~~json
{
  "source": "006d01ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01b0`](#insn-006d01b0)

~~~json
{
  "source": "006d01b0",
  "target": "006d0144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01b4`](#insn-006d01b4)

~~~json
{
  "source": "006d01b4",
  "target": "006d0150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01bc`](#insn-006d01bc)

~~~json
{
  "source": "006d01bc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01c4`](#insn-006d01c4)

~~~json
{
  "source": "006d01c4",
  "target": "006d0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01cc`](#insn-006d01cc)

~~~json
{
  "source": "006d01cc",
  "target": "006d76a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d01d4`](#insn-006d01d4)

~~~json
{
  "source": "006d01d4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01dc`](#insn-006d01dc)

~~~json
{
  "source": "006d01dc",
  "target": "006d0248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01e0`](#insn-006d01e0)

~~~json
{
  "source": "006d01e0",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0248`](#insn-006d0248)

~~~json
{
  "source": "006d0248",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
