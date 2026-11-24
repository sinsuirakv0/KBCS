# 006cfeac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006a6d68`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 移動量 `+0x29144`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0029.md#compare-8e478c0bcb8edc87e25e71de142f690b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006cfeec`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cf/006cfeec.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0005.md#compare-2195f49d5b0adf709adc0b60be8f03a2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006cfeac",
  "name": "FUN_006cfeac",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83c2bad6ad02b305a040f2aa9dee142b94f15fd398bc390b5f7115a76434a6e5",
  "source_text_sha256": "83c2bad6ad02b305a040f2aa9dee142b94f15fd398bc390b5f7115a76434a6e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006cfeac",
        "006d01a3"
      ],
      [
        "006d0208",
        "006d020b"
      ]
    ],
    "bytes_sha256": "2772cf09d8e734d6770b4a44a826862f4210a567e2b89563834aaacf11863a7f",
    "instruction_count": 191,
    "instruction_bytes": 764,
    "body_bytes": 764,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006d0264](../006d0/006d0264.md)
- [0089c00c](../0089c/0089c00c.md)
- [00b1f000](../00b1f/00b1f000.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [006d7024](../006d7/006d7024.md)
- [006d7048](../006d7/006d7048.md)
- [006d7660](../006d7/006d7660.md)
- [006d773c](../006d7/006d773c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a470](../00c5a/00c5a470.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5699 bytes

~~~c

void FUN_006cfeac(undefined8 param_1,byte *param_2)

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
  
                    /* catch() { ... } // from try @ 006cfdc4 with catch @ 006cfeb8
                       catch() { ... } // from try @ 006cfe84 with catch @ 006cfeb8 */
  lVar6 = tpidr_el0;
  local_38 = *(long *)(lVar6 + 0x28);
                    /* try { // try from 006cfed8 to 007cfeef has its CatchHandler @ 006cfed8
                       catch() { ... } // from try @ 006cfed8 with catch @ 006cfed8
                       catch() { ... } // from try @ 006cfef8 with catch @ 006cfed8 */
  plVar8 = (long *)_Znwm(0x28);
  _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em(plVar8,0);
  puVar7 = PTR__ZTVNSt6__ndk118codecvt_utf8_utf16IwLm1114111ELNS_12codecvt_modeE0EEE_00c9b140;
                    /* try { // try from 006cfef0 to 007cfef7 has its CatchHandler @ 006cff10 */
                    /* try { // try from 006cfef8 to 007cff23 has its CatchHandler @ 006cfed8 */
  plVar8[3] = 0x10ffff;
  uVar3 = *(ulong *)(param_2 + 8);
  pbVar4 = *(byte **)(param_2 + 0x10);
  *(undefined4 *)(plVar8 + 4) = 0;
  local_48 = 0;
  uStack_40 = 0;
  *plVar8 = (long)(puVar7 + 0x10);
                    /* catch() { ... } // from try @ 006cfef0 with catch @ 006cff10 */
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
  FUN_006d7048(local_98,&local_80,pbVar4,pbVar4 + uVar3);
  uVar3 = (ulong)(local_98[0] >> 1);
  if ((local_98[0] & 1) != 0) {
    uVar3 = local_90;
  }
  if (0x3ffffffffffffff7 < uVar3) {
    if (*(long *)(lVar6 + 0x28) != local_38) goto LAB_006d0208;
    FUN_006d7660(&local_b0);
LAB_006d0190:
    if (*(long *)(lVar6 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      FUN_00440e80();
    }
    goto LAB_006d0208;
  }
  if (uVar3 < 5) {
    puVar9 = (uint *)((ulong)&local_b0 | 4);
    local_b0 = CONCAT71(local_b0._1_7_,(char)((int)uVar3 << 1));
    if (uVar3 != 0) goto LAB_006cffb8;
  }
  else {
    uVar11 = (uVar3 & 0x3ffffffffffffffe) + 2;
    if ((uVar3 | 1) != 5) {
      uVar11 = uVar3 | 1;
    }
    if (0x3ffffffffffffffe < uVar11) goto LAB_006d0190;
    puVar9 = (uint *)_Znwm((uVar11 + 1) * 4);
                    /* try { // try from 006cffac to 007d00b3 has its CatchHandler @ 006cffac
                       catch() { ... } // from try @ 006cffac with catch @ 006cffac
                       catch() { ... } // from try @ 006d00c0 with catch @ 006cffac */
    local_b0 = uVar11 + 1 | 1;
    local_a8 = uVar3;
    local_a0 = puVar9;
LAB_006cffb8:
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
      if (uVar3 == uVar12) goto LAB_006d0008;
    }
    do {
      uVar11 = uVar11 - 1;
      *puVar10 = 0x20;
      puVar10 = puVar10 + 1;
    } while (uVar11 != 0);
  }
LAB_006d0008:
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
                    /* try { // try from 006d00b4 to 007d00bf has its CatchHandler @ 006d0168 */
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
  FUN_006d773c(param_1,&local_80,puVar9,puVar9 + uVar3);
  if ((local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_98[0] & 1) != 0) {
                    /* catch() { ... } // from try @ 006d00b4 with catch @ 006d0168 */
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
LAB_006d0208:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006cfeac"></a> `006cfeac` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-006cfeb0"></a> `006cfeb0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006cfeb4"></a> `006cfeb4` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-006cfeb8"></a> `006cfeb8` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-006cfebc"></a> `006cfebc` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-006cfec0"></a> `006cfec0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006cfec4"></a> `006cfec4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-006cfec8"></a> `006cfec8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006cfecc"></a> `006cfecc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006cfed0"></a> `006cfed0` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-006cfed4"></a> `006cfed4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006cfed8"></a> `006cfed8` | `ee 1e 16 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-006cfedc"></a> `006cfedc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006cfee0"></a> `006cfee0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-006cfee4"></a> `006cfee4` | `63 29 16 94` | bl 0x00c5a470 | `UNCONDITIONAL_CALL`
<a id="insn-006cfee8"></a> `006cfee8` | `68 2e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-006cfeec"></a> `006cfeec` | `e9 fd bf 12` | mov w9,#0x10ffff | `FALL_THROUGH`
<a id="insn-006cfef0"></a> `006cfef0` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-006cfef4"></a> `006cfef4` | `08 a1 40 f9` | ldr x8,[x8, #0x140] | `FALL_THROUGH`
<a id="insn-006cfef8"></a> `006cfef8` | `a9 0e 00 f9` | str x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-006cfefc"></a> `006cfefc` | `8a a6 40 a9` | ldp x10,x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006cff00"></a> `006cff00` | `bf 22 00 b9` | str wzr,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-006cff04"></a> `006cff04` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-006cff08"></a> `006cff08` | `ff ff 06 a9` | stp xzr,xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-006cff0c"></a> `006cff0c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-006cff10"></a> `006cff10` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-006cff14"></a> `006cff14` | `e0 83 01 ad` | stp q0,q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006cff18"></a> `006cff18` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff1c"></a> `006cff1c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff20"></a> `006cff20` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006cff24"></a> `006cff24` | `21 15 94 9a` | csinc x1,x9,x20,ne | `FALL_THROUGH`
<a id="insn-006cff28"></a> `006cff28` | `f5 33 00 f9` | str x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006cff2c"></a> `006cff2c` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-006cff30"></a> `006cff30` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006cff34"></a> `006cff34` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-006cff38"></a> `006cff38` | `22 00 09 8b` | add x2,x1,x9 | `FALL_THROUGH`
<a id="insn-006cff3c"></a> `006cff3c` | `43 1c 00 94` | bl 0x006d7048 | `UNCONDITIONAL_CALL`
<a id="insn-006cff40"></a> `006cff40` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006cff44"></a> `006cff44` | `e9 13 40 f9` | ldr x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006cff48"></a> `006cff48` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff4c"></a> `006cff4c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006cff50"></a> `006cff50` | `e8 eb 7d b2` | orr x8,xzr,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006cff54"></a> `006cff54` | `54 01 89 9a` | csel x20,x10,x9,eq | `FALL_THROUGH`
<a id="insn-006cff58"></a> `006cff58` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-006cff5c"></a> `006cff5c` | `e2 10 00 54` | b.cs 0x006d0178 | `CONDITIONAL_JUMP`
<a id="insn-006cff60"></a> `006cff60` | `9f 16 00 f1` | cmp x20,#0x5 | `FALL_THROUGH`
<a id="insn-006cff64"></a> `006cff64` | `e2 00 00 54` | b.cs 0x006cff80 | `CONDITIONAL_JUMP`
<a id="insn-006cff68"></a> `006cff68` | `88 7a 1f 53` | lsl w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-006cff6c"></a> `006cff6c` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-006cff70"></a> `006cff70` | `20 01 7e b2` | orr x0,x9,#0x4 | `FALL_THROUGH`
<a id="insn-006cff74"></a> `006cff74` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-006cff78"></a> `006cff78` | `14 02 00 b5` | cbnz x20,0x006cffb8 | `CONDITIONAL_JUMP`
<a id="insn-006cff7c"></a> `006cff7c` | `23 00 00 14` | b 0x006d0008 | `UNCONDITIONAL_JUMP`
<a id="insn-006cff80"></a> `006cff80` | `88 f2 7f 92` | and x8,x20,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-006cff84"></a> `006cff84` | `89 02 40 b2` | orr x9,x20,#0x1 | `FALL_THROUGH`
<a id="insn-006cff88"></a> `006cff88` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006cff8c"></a> `006cff8c` | `3f 15 00 f1` | cmp x9,#0x5 | `FALL_THROUGH`
<a id="insn-006cff90"></a> `006cff90` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-006cff94"></a> `006cff94` | `09 00 f8 92` | mov x9,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-006cff98"></a> `006cff98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006cff9c"></a> `006cff9c` | `a2 0f 00 54` | b.cs 0x006d0190 | `CONDITIONAL_JUMP`
<a id="insn-006cffa0"></a> `006cffa0` | `15 05 00 91` | add x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006cffa4"></a> `006cffa4` | `a0 f6 7e d3` | lsl x0,x21,#0x2 | `FALL_THROUGH`
<a id="insn-006cffa8"></a> `006cffa8` | `ba 1e 16 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-006cffac"></a> `006cffac` | `a8 02 40 b2` | orr x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-006cffb0"></a> `006cffb0` | `f4 83 00 a9` | stp x20,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006cffb4"></a> `006cffb4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-006cffb8"></a> `006cffb8` | `9f 22 00 f1` | cmp x20,#0x8 | `FALL_THROUGH`
<a id="insn-006cffbc"></a> `006cffbc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-006cffc0"></a> `006cffc0` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-006cffc4"></a> `006cffc4` | `a3 01 00 54` | b.cc 0x006cfff8 | `CONDITIONAL_JUMP`
<a id="insn-006cffc8"></a> `006cffc8` | `00 04 01 4f` | movi v0.4S,#0x20 | `FALL_THROUGH`
<a id="insn-006cffcc"></a> `006cffcc` | `8a ea 7d 92` | and x10,x20,#0x3ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-006cffd0"></a> `006cffd0` | `89 0a 40 92` | and x9,x20,#0x7 | `FALL_THROUGH`
<a id="insn-006cffd4"></a> `006cffd4` | `08 08 0a 8b` | add x8,x0,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006cffd8"></a> `006cffd8` | `0b 40 00 91` | add x11,x0,#0x10 | `FALL_THROUGH`
<a id="insn-006cffdc"></a> `006cffdc` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-006cffe0"></a> `006cffe0` | `8c 21 00 f1` | subs x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-006cffe4"></a> `006cffe4` | `60 81 3f ad` | stp q0,q0,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-006cffe8"></a> `006cffe8` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-006cffec"></a> `006cffec` | `a1 ff ff 54` | b.ne 0x006cffe0 | `CONDITIONAL_JUMP`
<a id="insn-006cfff0"></a> `006cfff0` | `9f 02 0a eb` | cmp x20,x10 | `FALL_THROUGH`
<a id="insn-006cfff4"></a> `006cfff4` | `a0 00 00 54` | b.eq 0x006d0008 | `CONDITIONAL_JUMP`
<a id="insn-006cfff8"></a> `006cfff8` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-006cfffc"></a> `006cfffc` | `29 05 00 f1` | subs x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-006d0000"></a> `006d0000` | `0a 45 00 b8` | str w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-006d0004"></a> `006d0004` | `c1 ff ff 54` | b.ne 0x006cfffc | `CONDITIONAL_JUMP`
<a id="insn-006d0008"></a> `006d0008` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d000c"></a> `006d000c` | `ec 2f 42 a9` | ldp x12,x11,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006d0010"></a> `006d0010` | `1f 78 34 b8` | str wzr,[x0, x20, LSL #0x2] | `FALL_THROUGH`
<a id="insn-006d0014"></a> `006d0014` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006d0018"></a> `006d0018` | `0d fd 41 d3` | lsr x13,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006d001c"></a> `006d001c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-006d0020"></a> `006d0020` | `ea 03 40 39` | ldrb w10,[sp] | `FALL_THROUGH`
<a id="insn-006d0024"></a> `006d0024` | `29 01 7e b2` | orr x9,x9,#0x4 | `FALL_THROUGH`
<a id="insn-006d0028"></a> `006d0028` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-006d002c"></a> `006d002c` | `ac 01 8c 9a` | csel x12,x13,x12,eq | `FALL_THROUGH`
<a id="insn-006d0030"></a> `006d0030` | `ed 0b 40 f9` | ldr x13,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d0034"></a> `006d0034` | `29 01 8b 9a` | csel x9,x9,x11,eq | `FALL_THROUGH`
<a id="insn-006d0038"></a> `006d0038` | `4b 01 00 12` | and w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d003c"></a> `006d003c` | `08 01 7e b2` | orr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-006d0040"></a> `006d0040` | `4c 04 00 b4` | cbz x12,0x006d00c8 | `CONDITIONAL_JUMP`
<a id="insn-006d0044"></a> `006d0044` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-006d0048"></a> `006d0048` | `8a f5 7e d3` | lsl x10,x12,#0x2 | `FALL_THROUGH`
<a id="insn-006d004c"></a> `006d004c` | `eb e1 9f 12` | mov w11,#0xffff00f0 | `FALL_THROUGH`
<a id="insn-006d0050"></a> `006d0050` | `0c e4 9f 12` | mov w12,#0xffff00df | `FALL_THROUGH`
<a id="insn-006d0054"></a> `006d0054` | `0d 01 8d 9a` | csel x13,x8,x13,eq | `FALL_THROUGH`
<a id="insn-006d0058"></a> `006d0058` | `0e e8 9f 12` | mov w14,#0xffff00bf | `FALL_THROUGH`
<a id="insn-006d005c"></a> `006d005c` | `ef db 9f 12` | mov w15,#0xffff0120 | `FALL_THROUGH`
<a id="insn-006d0060"></a> `006d0060` | `10 08 86 12` | mov w16,#0xffffcfbf | `FALL_THROUGH`
<a id="insn-006d0064"></a> `006d0064` | `31 45 40 b8` | ldr w17,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-006d0068"></a> `006d0068` | `20 02 0e 0b` | add w0,w17,w14 | `FALL_THROUGH`
<a id="insn-006d006c"></a> `006d006c` | `21 02 0c 0b` | add w1,w17,w12 | `FALL_THROUGH`
<a id="insn-006d0070"></a> `006d0070` | `22 02 0f 0b` | add w2,w17,w15 | `FALL_THROUGH`
<a id="insn-006d0074"></a> `006d0074` | `1f 68 00 71` | cmp w0,#0x1a | `FALL_THROUGH`
<a id="insn-006d0078"></a> `006d0078` | `20 02 0b 0b` | add w0,w17,w11 | `FALL_THROUGH`
<a id="insn-006d007c"></a> `006d007c` | `51 30 91 1a` | csel w17,w2,w17,cc | `FALL_THROUGH`
<a id="insn-006d0080"></a> `006d0080` | `3f 64 00 71` | cmp w1,#0x19 | `FALL_THROUGH`
<a id="insn-006d0084"></a> `006d0084` | `31 82 82 1a` | csel w17,w17,w2,hi | `FALL_THROUGH`
<a id="insn-006d0088"></a> `006d0088` | `1f 24 00 71` | cmp w0,#0x9 | `FALL_THROUGH`
<a id="insn-006d008c"></a> `006d008c` | `31 82 82 1a` | csel w17,w17,w2,hi | `FALL_THROUGH`
<a id="insn-006d0090"></a> `006d0090` | `20 02 10 0b` | add w0,w17,w16 | `FALL_THROUGH`
<a id="insn-006d0094"></a> `006d0094` | `21 06 01 51` | sub w1,w17,#0x41 | `FALL_THROUGH`
<a id="insn-006d0098"></a> `006d0098` | `22 82 01 11` | add w2,w17,#0x60 | `FALL_THROUGH`
<a id="insn-006d009c"></a> `006d009c` | `1f 58 01 71` | cmp w0,#0x56 | `FALL_THROUGH`
<a id="insn-006d00a0"></a> `006d00a0` | `40 30 91 1a` | csel w0,w2,w17,cc | `FALL_THROUGH`
<a id="insn-006d00a4"></a> `006d00a4` | `31 02 1b 32` | orr w17,w17,#0x20 | `FALL_THROUGH`
<a id="insn-006d00a8"></a> `006d00a8` | `3f 64 00 71` | cmp w1,#0x19 | `FALL_THROUGH`
<a id="insn-006d00ac"></a> `006d00ac` | `11 80 91 1a` | csel w17,w0,w17,hi | `FALL_THROUGH`
<a id="insn-006d00b0"></a> `006d00b0` | `4a 11 00 f1` | subs x10,x10,#0x4 | `FALL_THROUGH`
<a id="insn-006d00b4"></a> `006d00b4` | `b1 45 00 b8` | str w17,[x13], #0x4 | `FALL_THROUGH`
<a id="insn-006d00b8"></a> `006d00b8` | `61 fd ff 54` | b.ne 0x006d0064 | `CONDITIONAL_JUMP`
<a id="insn-006d00bc"></a> `006d00bc` | `ea 03 40 39` | ldrb w10,[sp] | `FALL_THROUGH`
<a id="insn-006d00c0"></a> `006d00c0` | `ed 0b 40 f9` | ldr x13,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d00c4"></a> `006d00c4` | `4b 01 00 12` | and w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d00c8"></a> `006d00c8` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006d00cc"></a> `006d00cc` | `4a 7d 01 53` | lsr w10,w10,#0x1 | `FALL_THROUGH`
<a id="insn-006d00d0"></a> `006d00d0` | `7f 01 00 71` | cmp w11,#0x0 | `FALL_THROUGH`
<a id="insn-006d00d4"></a> `006d00d4` | `01 01 8d 9a` | csel x1,x8,x13,eq | `FALL_THROUGH`
<a id="insn-006d00d8"></a> `006d00d8` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-006d00dc"></a> `006d00dc` | `22 08 08 8b` | add x2,x1,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006d00e0"></a> `006d00e0` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-006d00e4"></a> `006d00e4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-006d00e8"></a> `006d00e8` | `95 1d 00 94` | bl 0x006d773c | `UNCONDITIONAL_CALL`
<a id="insn-006d00ec"></a> `006d00ec` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006d00f0"></a> `006d00f0` | `28 03 00 37` | tbnz w8,#0x0,0x006d0154 | `CONDITIONAL_JUMP`
<a id="insn-006d00f4"></a> `006d00f4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d00f8"></a> `006d00f8` | `68 03 00 37` | tbnz w8,#0x0,0x006d0164 | `CONDITIONAL_JUMP`
<a id="insn-006d00fc"></a> `006d00fc` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006d0100"></a> `006d0100` | `80 00 00 b4` | cbz x0,0x006d0110 | `CONDITIONAL_JUMP`
<a id="insn-006d0104"></a> `006d0104` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-006d0108"></a> `006d0108` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-006d010c"></a> `006d010c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006d0110"></a> `006d0110` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-006d0114"></a> `006d0114` | `68 00 00 36` | tbz w8,#0x0,0x006d0120 | `CONDITIONAL_JUMP`
<a id="insn-006d0118"></a> `006d0118` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-006d011c"></a> `006d011c` | `65 1e 16 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006d0120"></a> `006d0120` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006d0124"></a> `006d0124` | `68 00 00 36` | tbz w8,#0x0,0x006d0130 | `CONDITIONAL_JUMP`
<a id="insn-006d0128"></a> `006d0128` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006d012c"></a> `006d012c` | `61 1e 16 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006d0130"></a> `006d0130` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d0134"></a> `006d0134` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d0138"></a> `006d0138` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d013c"></a> `006d013c` | `61 06 00 54` | b.ne 0x006d0208 | `CONDITIONAL_JUMP`
<a id="insn-006d0140"></a> `006d0140` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-006d0144"></a> `006d0144` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-006d0148"></a> `006d0148` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006d014c"></a> `006d014c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-006d0150"></a> `006d0150` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006d0154"></a> `006d0154` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006d0158"></a> `006d0158` | `56 1e 16 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006d015c"></a> `006d015c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006d0160"></a> `006d0160` | `e8 fc 07 36` | tbz w8,#0x0,0x006d00fc | `CONDITIONAL_JUMP`
<a id="insn-006d0164"></a> `006d0164` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006d0168"></a> `006d0168` | `52 1e 16 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006d016c"></a> `006d016c` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006d0170"></a> `006d0170` | `a0 fc ff b5` | cbnz x0,0x006d0104 | `CONDITIONAL_JUMP`
<a id="insn-006d0174"></a> `006d0174` | `e7 ff ff 17` | b 0x006d0110 | `UNCONDITIONAL_JUMP`
<a id="insn-006d0178"></a> `006d0178` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d017c"></a> `006d017c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d0180"></a> `006d0180` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d0184"></a> `006d0184` | `21 04 00 54` | b.ne 0x006d0208 | `CONDITIONAL_JUMP`
<a id="insn-006d0188"></a> `006d0188` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-006d018c"></a> `006d018c` | `35 1d 00 94` | bl 0x006d7660 | `UNCONDITIONAL_CALL`
<a id="insn-006d0190"></a> `006d0190` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006d0194"></a> `006d0194` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006d0198"></a> `006d0198` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006d019c"></a> `006d019c` | `61 03 00 54` | b.ne 0x006d0208 | `CONDITIONAL_JUMP`
<a id="insn-006d01a0"></a> `006d01a0` | `38 c3 f5 97` | bl 0x00440e80 | `CALL_TERMINATOR`
<a id="insn-006d0208"></a> `006d0208` | `36 1e 16 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006cfeac`](#insn-006cfeac) 範囲 `[['006cfeac', '006cfeb7']]`
  - `FALL_THROUGH` [`006cfeb4`](#insn-006cfeb4) → [`006cfeb8`](#insn-006cfeb8)
- ブロック [`006cfeb8`](#insn-006cfeb8) 範囲 `[['006cfeb8', '006cfed7']]`
  - `FALL_THROUGH` [`006cfed4`](#insn-006cfed4) → [`006cfed8`](#insn-006cfed8)
- ブロック [`006cfed8`](#insn-006cfed8) 範囲 `[['006cfed8', '006cfeef']]`
  - `FALL_THROUGH` [`006cfeec`](#insn-006cfeec) → [`006cfef0`](#insn-006cfef0)
- ブロック [`006cfef0`](#insn-006cfef0) 範囲 `[['006cfef0', '006cfef7']]`
  - `FALL_THROUGH` [`006cfef4`](#insn-006cfef4) → [`006cfef8`](#insn-006cfef8)
- ブロック [`006cfef8`](#insn-006cfef8) 範囲 `[['006cfef8', '006cff0f']]`
  - `FALL_THROUGH` [`006cff0c`](#insn-006cff0c) → [`006cff10`](#insn-006cff10)
- ブロック [`006cff10`](#insn-006cff10) 範囲 `[['006cff10', '006cff5f']]`
  - `CONDITIONAL_JUMP` [`006cff5c`](#insn-006cff5c) → [`006d0178`](#insn-006d0178)
  - `FALL_THROUGH` [`006cff5c`](#insn-006cff5c) → [`006cff60`](#insn-006cff60)
- ブロック [`006cff60`](#insn-006cff60) 範囲 `[['006cff60', '006cff67']]`
  - `CONDITIONAL_JUMP` [`006cff64`](#insn-006cff64) → [`006cff80`](#insn-006cff80)
  - `FALL_THROUGH` [`006cff64`](#insn-006cff64) → [`006cff68`](#insn-006cff68)
- ブロック [`006cff68`](#insn-006cff68) 範囲 `[['006cff68', '006cff7b']]`
  - `CONDITIONAL_JUMP` [`006cff78`](#insn-006cff78) → [`006cffb8`](#insn-006cffb8)
  - `FALL_THROUGH` [`006cff78`](#insn-006cff78) → [`006cff7c`](#insn-006cff7c)
- ブロック [`006cff7c`](#insn-006cff7c) 範囲 `[['006cff7c', '006cff7f']]`
  - `UNCONDITIONAL_JUMP` [`006cff7c`](#insn-006cff7c) → [`006d0008`](#insn-006d0008)
- ブロック [`006cff80`](#insn-006cff80) 範囲 `[['006cff80', '006cff9f']]`
  - `CONDITIONAL_JUMP` [`006cff9c`](#insn-006cff9c) → [`006d0190`](#insn-006d0190)
  - `FALL_THROUGH` [`006cff9c`](#insn-006cff9c) → [`006cffa0`](#insn-006cffa0)
- ブロック [`006cffa0`](#insn-006cffa0) 範囲 `[['006cffa0', '006cffab']]`
  - `FALL_THROUGH` [`006cffa8`](#insn-006cffa8) → [`006cffac`](#insn-006cffac)
- ブロック [`006cffac`](#insn-006cffac) 範囲 `[['006cffac', '006cffb7']]`
  - `FALL_THROUGH` [`006cffb4`](#insn-006cffb4) → [`006cffb8`](#insn-006cffb8)
- ブロック [`006cffb8`](#insn-006cffb8) 範囲 `[['006cffb8', '006cffc7']]`
  - `CONDITIONAL_JUMP` [`006cffc4`](#insn-006cffc4) → [`006cfff8`](#insn-006cfff8)
  - `FALL_THROUGH` [`006cffc4`](#insn-006cffc4) → [`006cffc8`](#insn-006cffc8)
- ブロック [`006cffc8`](#insn-006cffc8) 範囲 `[['006cffc8', '006cffdf']]`
  - `FALL_THROUGH` [`006cffdc`](#insn-006cffdc) → [`006cffe0`](#insn-006cffe0)
- ブロック [`006cffe0`](#insn-006cffe0) 範囲 `[['006cffe0', '006cffef']]`
  - `CONDITIONAL_JUMP` [`006cffec`](#insn-006cffec) → [`006cffe0`](#insn-006cffe0)
  - `FALL_THROUGH` [`006cffec`](#insn-006cffec) → [`006cfff0`](#insn-006cfff0)
- ブロック [`006cfff0`](#insn-006cfff0) 範囲 `[['006cfff0', '006cfff7']]`
  - `CONDITIONAL_JUMP` [`006cfff4`](#insn-006cfff4) → [`006d0008`](#insn-006d0008)
  - `FALL_THROUGH` [`006cfff4`](#insn-006cfff4) → [`006cfff8`](#insn-006cfff8)
- ブロック [`006cfff8`](#insn-006cfff8) 範囲 `[['006cfff8', '006cfffb']]`
  - `FALL_THROUGH` [`006cfff8`](#insn-006cfff8) → [`006cfffc`](#insn-006cfffc)
- ブロック [`006cfffc`](#insn-006cfffc) 範囲 `[['006cfffc', '006d0007']]`
  - `CONDITIONAL_JUMP` [`006d0004`](#insn-006d0004) → [`006cfffc`](#insn-006cfffc)
  - `FALL_THROUGH` [`006d0004`](#insn-006d0004) → [`006d0008`](#insn-006d0008)
- ブロック [`006d0008`](#insn-006d0008) 範囲 `[['006d0008', '006d0043']]`
  - `CONDITIONAL_JUMP` [`006d0040`](#insn-006d0040) → [`006d00c8`](#insn-006d00c8)
  - `FALL_THROUGH` [`006d0040`](#insn-006d0040) → [`006d0044`](#insn-006d0044)
- ブロック [`006d0044`](#insn-006d0044) 範囲 `[['006d0044', '006d0063']]`
  - `FALL_THROUGH` [`006d0060`](#insn-006d0060) → [`006d0064`](#insn-006d0064)
- ブロック [`006d0064`](#insn-006d0064) 範囲 `[['006d0064', '006d00b3']]`
  - `FALL_THROUGH` [`006d00b0`](#insn-006d00b0) → [`006d00b4`](#insn-006d00b4)
- ブロック [`006d00b4`](#insn-006d00b4) 範囲 `[['006d00b4', '006d00bb']]`
  - `CONDITIONAL_JUMP` [`006d00b8`](#insn-006d00b8) → [`006d0064`](#insn-006d0064)
  - `FALL_THROUGH` [`006d00b8`](#insn-006d00b8) → [`006d00bc`](#insn-006d00bc)
- ブロック [`006d00bc`](#insn-006d00bc) 範囲 `[['006d00bc', '006d00bf']]`
  - `FALL_THROUGH` [`006d00bc`](#insn-006d00bc) → [`006d00c0`](#insn-006d00c0)
- ブロック [`006d00c0`](#insn-006d00c0) 範囲 `[['006d00c0', '006d00c7']]`
  - `FALL_THROUGH` [`006d00c4`](#insn-006d00c4) → [`006d00c8`](#insn-006d00c8)
- ブロック [`006d00c8`](#insn-006d00c8) 範囲 `[['006d00c8', '006d00f3']]`
  - `CONDITIONAL_JUMP` [`006d00f0`](#insn-006d00f0) → [`006d0154`](#insn-006d0154)
  - `FALL_THROUGH` [`006d00f0`](#insn-006d00f0) → [`006d00f4`](#insn-006d00f4)
- ブロック [`006d00f4`](#insn-006d00f4) 範囲 `[['006d00f4', '006d00fb']]`
  - `CONDITIONAL_JUMP` [`006d00f8`](#insn-006d00f8) → [`006d0164`](#insn-006d0164)
  - `FALL_THROUGH` [`006d00f8`](#insn-006d00f8) → [`006d00fc`](#insn-006d00fc)
- ブロック [`006d00fc`](#insn-006d00fc) 範囲 `[['006d00fc', '006d0103']]`
  - `CONDITIONAL_JUMP` [`006d0100`](#insn-006d0100) → [`006d0110`](#insn-006d0110)
  - `FALL_THROUGH` [`006d0100`](#insn-006d0100) → [`006d0104`](#insn-006d0104)
- ブロック [`006d0104`](#insn-006d0104) 範囲 `[['006d0104', '006d010f']]`
  - `FALL_THROUGH` [`006d010c`](#insn-006d010c) → [`006d0110`](#insn-006d0110)
- ブロック [`006d0110`](#insn-006d0110) 範囲 `[['006d0110', '006d0117']]`
  - `CONDITIONAL_JUMP` [`006d0114`](#insn-006d0114) → [`006d0120`](#insn-006d0120)
  - `FALL_THROUGH` [`006d0114`](#insn-006d0114) → [`006d0118`](#insn-006d0118)
- ブロック [`006d0118`](#insn-006d0118) 範囲 `[['006d0118', '006d011f']]`
  - `FALL_THROUGH` [`006d011c`](#insn-006d011c) → [`006d0120`](#insn-006d0120)
- ブロック [`006d0120`](#insn-006d0120) 範囲 `[['006d0120', '006d0127']]`
  - `CONDITIONAL_JUMP` [`006d0124`](#insn-006d0124) → [`006d0130`](#insn-006d0130)
  - `FALL_THROUGH` [`006d0124`](#insn-006d0124) → [`006d0128`](#insn-006d0128)
- ブロック [`006d0128`](#insn-006d0128) 範囲 `[['006d0128', '006d012f']]`
  - `FALL_THROUGH` [`006d012c`](#insn-006d012c) → [`006d0130`](#insn-006d0130)
- ブロック [`006d0130`](#insn-006d0130) 範囲 `[['006d0130', '006d013f']]`
  - `CONDITIONAL_JUMP` [`006d013c`](#insn-006d013c) → [`006d0208`](#insn-006d0208)
  - `FALL_THROUGH` [`006d013c`](#insn-006d013c) → [`006d0140`](#insn-006d0140)
- ブロック [`006d0140`](#insn-006d0140) 範囲 `[['006d0140', '006d0153']]`
- ブロック [`006d0154`](#insn-006d0154) 範囲 `[['006d0154', '006d0163']]`
  - `CONDITIONAL_JUMP` [`006d0160`](#insn-006d0160) → [`006d00fc`](#insn-006d00fc)
  - `FALL_THROUGH` [`006d0160`](#insn-006d0160) → [`006d0164`](#insn-006d0164)
- ブロック [`006d0164`](#insn-006d0164) 範囲 `[['006d0164', '006d0167']]`
  - `FALL_THROUGH` [`006d0164`](#insn-006d0164) → [`006d0168`](#insn-006d0168)
- ブロック [`006d0168`](#insn-006d0168) 範囲 `[['006d0168', '006d0173']]`
  - `CONDITIONAL_JUMP` [`006d0170`](#insn-006d0170) → [`006d0104`](#insn-006d0104)
  - `FALL_THROUGH` [`006d0170`](#insn-006d0170) → [`006d0174`](#insn-006d0174)
- ブロック [`006d0174`](#insn-006d0174) 範囲 `[['006d0174', '006d0177']]`
  - `UNCONDITIONAL_JUMP` [`006d0174`](#insn-006d0174) → [`006d0110`](#insn-006d0110)
- ブロック [`006d0178`](#insn-006d0178) 範囲 `[['006d0178', '006d0187']]`
  - `CONDITIONAL_JUMP` [`006d0184`](#insn-006d0184) → [`006d0208`](#insn-006d0208)
  - `FALL_THROUGH` [`006d0184`](#insn-006d0184) → [`006d0188`](#insn-006d0188)
- ブロック [`006d0188`](#insn-006d0188) 範囲 `[['006d0188', '006d018f']]`
  - `FALL_THROUGH` [`006d018c`](#insn-006d018c) → [`006d0190`](#insn-006d0190)
- ブロック [`006d0190`](#insn-006d0190) 範囲 `[['006d0190', '006d019f']]`
  - `CONDITIONAL_JUMP` [`006d019c`](#insn-006d019c) → [`006d0208`](#insn-006d0208)
  - `FALL_THROUGH` [`006d019c`](#insn-006d019c) → [`006d01a0`](#insn-006d01a0)
- ブロック [`006d01a0`](#insn-006d01a0) 範囲 `[['006d01a0', '006d01a3']]`
- ブロック [`006d0208`](#insn-006d0208) 範囲 `[['006d0208', '006d020b']]`

## 命令位置別の参照

- [`006cfeb0`](#insn-006cfeb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfeb4`](#insn-006cfeb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfeb8`](#insn-006cfeb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfed4`](#insn-006cfed4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfed8`](#insn-006cfed8) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`006cfee4`](#insn-006cfee4) → [`00c5a470`](../00c5a/00c5a470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a470` · 推定シンボル `None` · 推定型 `None`
- [`006cfef4`](#insn-006cfef4) → `00c9b140`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006cfef8`](#insn-006cfef8) → `0010ffff`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Sym[6813]`
- [`006cff08`](#insn-006cff08) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff0c`](#insn-006cff0c) → `00c75ea0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[96]`
- [`006cff14`](#insn-006cff14) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff20`](#insn-006cff20) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff28`](#insn-006cff28) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff3c`](#insn-006cff3c) → [`006d7048`](../006d7/006d7048.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d7048` · 推定シンボル `None` · 推定型 `None`
- [`006cff40`](#insn-006cff40) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff44`](#insn-006cff44) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff5c`](#insn-006cff5c) → [`006d0178`](#insn-006d0178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff64`](#insn-006cff64) → [`006cff80`](#insn-006cff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff74`](#insn-006cff74) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff78`](#insn-006cff78) → [`006cffb8`](#insn-006cffb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff7c`](#insn-006cff7c) → [`006d0008`](#insn-006d0008) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cff9c`](#insn-006cff9c) → [`006d0190`](#insn-006d0190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffa8`](#insn-006cffa8) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`006cffb0`](#insn-006cffb0) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffb4`](#insn-006cffb4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffc4`](#insn-006cffc4) → [`006cfff8`](#insn-006cfff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cffec`](#insn-006cffec) → [`006cffe0`](#insn-006cffe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006cfff4`](#insn-006cfff4) → [`006d0008`](#insn-006d0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0004`](#insn-006d0004) → [`006cfffc`](#insn-006cfffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0008`](#insn-006d0008) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d000c`](#insn-006d000c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0020`](#insn-006d0020) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0030`](#insn-006d0030) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0040`](#insn-006d0040) → [`006d00c8`](#insn-006d00c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00b8`](#insn-006d00b8) → [`006d0064`](#insn-006d0064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00bc`](#insn-006d00bc) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00c0`](#insn-006d00c0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00c8`](#insn-006d00c8) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00e8`](#insn-006d00e8) → [`006d773c`](../006d7/006d773c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d773c` · 推定シンボル `None` · 推定型 `None`
- [`006d00ec`](#insn-006d00ec) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00f0`](#insn-006d00f0) → [`006d0154`](#insn-006d0154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00f4`](#insn-006d00f4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00f8`](#insn-006d00f8) → [`006d0164`](#insn-006d0164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d00fc`](#insn-006d00fc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0100`](#insn-006d0100) → [`006d0110`](#insn-006d0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0108`](#insn-006d0108) → `00c75ea8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[96]`
- [`006d010c`](#insn-006d010c) → [`006d7024`](../006d7/006d7024.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `006d7024` · 推定シンボル `None` · 推定型 `None`
- [`006d0110`](#insn-006d0110) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0114`](#insn-006d0114) → [`006d0120`](#insn-006d0120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0118`](#insn-006d0118) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d011c`](#insn-006d011c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`006d0120`](#insn-006d0120) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0124`](#insn-006d0124) → [`006d0130`](#insn-006d0130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0128`](#insn-006d0128) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d012c`](#insn-006d012c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`006d0134`](#insn-006d0134) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d013c`](#insn-006d013c) → [`006d0208`](#insn-006d0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0140`](#insn-006d0140) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0144`](#insn-006d0144) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0148`](#insn-006d0148) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0154`](#insn-006d0154) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0158`](#insn-006d0158) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`006d015c`](#insn-006d015c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0160`](#insn-006d0160) → [`006d00fc`](#insn-006d00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0164`](#insn-006d0164) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0168`](#insn-006d0168) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`006d016c`](#insn-006d016c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0170`](#insn-006d0170) → [`006d0104`](#insn-006d0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0174`](#insn-006d0174) → [`006d0110`](#insn-006d0110) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d017c`](#insn-006d017c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d0184`](#insn-006d0184) → [`006d0208`](#insn-006d0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d018c`](#insn-006d018c) → [`006d7660`](../006d7/006d7660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006d7660` · 推定シンボル `None` · 推定型 `None`
- [`006d0194`](#insn-006d0194) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d019c`](#insn-006d019c) → [`006d0208`](#insn-006d0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006d01a0`](#insn-006d01a0) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`
- [`006d0208`](#insn-006d0208) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006cfeb0`](#insn-006cfeb0)

~~~json
{
  "source": "006cfeb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfeb4`](#insn-006cfeb4)

~~~json
{
  "source": "006cfeb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfeb8`](#insn-006cfeb8)

~~~json
{
  "source": "006cfeb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfed4`](#insn-006cfed4)

~~~json
{
  "source": "006cfed4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfed8`](#insn-006cfed8)

~~~json
{
  "source": "006cfed8",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cfee4`](#insn-006cfee4)

~~~json
{
  "source": "006cfee4",
  "target": "00c5a470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cfef4`](#insn-006cfef4)

~~~json
{
  "source": "006cfef4",
  "target": "00c9b140",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b140",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006cfef8`](#insn-006cfef8)

~~~json
{
  "source": "006cfef8",
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
- 参照命令 [`006cff08`](#insn-006cff08)

~~~json
{
  "source": "006cff08",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff0c`](#insn-006cff0c)

~~~json
{
  "source": "006cff0c",
  "target": "00c75ea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c75e90",
  "offset": 16,
  "size": 96,
  "datatype": "undefined1[96]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006cff14`](#insn-006cff14)

~~~json
{
  "source": "006cff14",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff20`](#insn-006cff20)

~~~json
{
  "source": "006cff20",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff28`](#insn-006cff28)

~~~json
{
  "source": "006cff28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff3c`](#insn-006cff3c)

~~~json
{
  "source": "006cff3c",
  "target": "006d7048",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cff40`](#insn-006cff40)

~~~json
{
  "source": "006cff40",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff44`](#insn-006cff44)

~~~json
{
  "source": "006cff44",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff5c`](#insn-006cff5c)

~~~json
{
  "source": "006cff5c",
  "target": "006d0178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff64`](#insn-006cff64)

~~~json
{
  "source": "006cff64",
  "target": "006cff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff74`](#insn-006cff74)

~~~json
{
  "source": "006cff74",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff78`](#insn-006cff78)

~~~json
{
  "source": "006cff78",
  "target": "006cffb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff7c`](#insn-006cff7c)

~~~json
{
  "source": "006cff7c",
  "target": "006d0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cff9c`](#insn-006cff9c)

~~~json
{
  "source": "006cff9c",
  "target": "006d0190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffa8`](#insn-006cffa8)

~~~json
{
  "source": "006cffa8",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006cffb0`](#insn-006cffb0)

~~~json
{
  "source": "006cffb0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
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
- 参照命令 [`006cffc4`](#insn-006cffc4)

~~~json
{
  "source": "006cffc4",
  "target": "006cfff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cffec`](#insn-006cffec)

~~~json
{
  "source": "006cffec",
  "target": "006cffe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006cfff4`](#insn-006cfff4)

~~~json
{
  "source": "006cfff4",
  "target": "006d0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0004`](#insn-006d0004)

~~~json
{
  "source": "006d0004",
  "target": "006cfffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0008`](#insn-006d0008)

~~~json
{
  "source": "006d0008",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d000c`](#insn-006d000c)

~~~json
{
  "source": "006d000c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0020`](#insn-006d0020)

~~~json
{
  "source": "006d0020",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0030`](#insn-006d0030)

~~~json
{
  "source": "006d0030",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0040`](#insn-006d0040)

~~~json
{
  "source": "006d0040",
  "target": "006d00c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00b8`](#insn-006d00b8)

~~~json
{
  "source": "006d00b8",
  "target": "006d0064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00bc`](#insn-006d00bc)

~~~json
{
  "source": "006d00bc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00c0`](#insn-006d00c0)

~~~json
{
  "source": "006d00c0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00c8`](#insn-006d00c8)

~~~json
{
  "source": "006d00c8",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00e8`](#insn-006d00e8)

~~~json
{
  "source": "006d00e8",
  "target": "006d773c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d00ec`](#insn-006d00ec)

~~~json
{
  "source": "006d00ec",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00f0`](#insn-006d00f0)

~~~json
{
  "source": "006d00f0",
  "target": "006d0154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00f4`](#insn-006d00f4)

~~~json
{
  "source": "006d00f4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00f8`](#insn-006d00f8)

~~~json
{
  "source": "006d00f8",
  "target": "006d0164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d00fc`](#insn-006d00fc)

~~~json
{
  "source": "006d00fc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0100`](#insn-006d0100)

~~~json
{
  "source": "006d0100",
  "target": "006d0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0108`](#insn-006d0108)

~~~json
{
  "source": "006d0108",
  "target": "00c75ea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c75e90",
  "offset": 24,
  "size": 96,
  "datatype": "undefined1[96]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`006d010c`](#insn-006d010c)

~~~json
{
  "source": "006d010c",
  "target": "006d7024",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0110`](#insn-006d0110)

~~~json
{
  "source": "006d0110",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0114`](#insn-006d0114)

~~~json
{
  "source": "006d0114",
  "target": "006d0120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0118`](#insn-006d0118)

~~~json
{
  "source": "006d0118",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d011c`](#insn-006d011c)

~~~json
{
  "source": "006d011c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0120`](#insn-006d0120)

~~~json
{
  "source": "006d0120",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0124`](#insn-006d0124)

~~~json
{
  "source": "006d0124",
  "target": "006d0130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0128`](#insn-006d0128)

~~~json
{
  "source": "006d0128",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d012c`](#insn-006d012c)

~~~json
{
  "source": "006d012c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0134`](#insn-006d0134)

~~~json
{
  "source": "006d0134",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d013c`](#insn-006d013c)

~~~json
{
  "source": "006d013c",
  "target": "006d0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0140`](#insn-006d0140)

~~~json
{
  "source": "006d0140",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0144`](#insn-006d0144)

~~~json
{
  "source": "006d0144",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0148`](#insn-006d0148)

~~~json
{
  "source": "006d0148",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0154`](#insn-006d0154)

~~~json
{
  "source": "006d0154",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0158`](#insn-006d0158)

~~~json
{
  "source": "006d0158",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d015c`](#insn-006d015c)

~~~json
{
  "source": "006d015c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0160`](#insn-006d0160)

~~~json
{
  "source": "006d0160",
  "target": "006d00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0164`](#insn-006d0164)

~~~json
{
  "source": "006d0164",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0168`](#insn-006d0168)

~~~json
{
  "source": "006d0168",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d016c`](#insn-006d016c)

~~~json
{
  "source": "006d016c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0170`](#insn-006d0170)

~~~json
{
  "source": "006d0170",
  "target": "006d0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0174`](#insn-006d0174)

~~~json
{
  "source": "006d0174",
  "target": "006d0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d017c`](#insn-006d017c)

~~~json
{
  "source": "006d017c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d0184`](#insn-006d0184)

~~~json
{
  "source": "006d0184",
  "target": "006d0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d018c`](#insn-006d018c)

~~~json
{
  "source": "006d018c",
  "target": "006d7660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0194`](#insn-006d0194)

~~~json
{
  "source": "006d0194",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d019c`](#insn-006d019c)

~~~json
{
  "source": "006d019c",
  "target": "006d0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006d01a0`](#insn-006d01a0)

~~~json
{
  "source": "006d01a0",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006d0208`](#insn-006d0208)

~~~json
{
  "source": "006d0208",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
