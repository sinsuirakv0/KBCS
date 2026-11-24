# 005cffac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `005ab2e0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md) · 移動量 `+0x24ccc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0023.md#compare-86c4f8b328df755e92faa0534f69ee55)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `005cffec`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cf/005cffec.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0016.md#compare-008b366c3523f9475ab4ff8a3793725b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cffac",
  "name": "FUN_005cffac",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35abbc265dad066581446cc9b41d9786a4c225f69acaa07263708ba6a3e5cb24",
  "source_text_sha256": "35abbc265dad066581446cc9b41d9786a4c225f69acaa07263708ba6a3e5cb24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cffac",
        "005d0167"
      ],
      [
        "005d018c",
        "005d018f"
      ]
    ],
    "bytes_sha256": "ffb70534993596ca7c1bcf484b22697396931e3cf7719908b5c05dc7374938fd",
    "instruction_count": 112,
    "instruction_bytes": 448,
    "body_bytes": 448,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cf680](../005cf/005cf680.md)
- [005d69b0](../005d6/005d69b0.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [005d0190](../005d0/005d0190.md)
- [005d0330](../005d0/005d0330.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3004 bytes

~~~c

long FUN_005cffac(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  void *pvVar6;
  long lVar7;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  void *local_70;
  undefined8 *local_68;
  undefined8 *local_60;
  void *pvStack_58;
  long *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  lVar7 = param_1[1] - *param_1 >> 5;
  uVar1 = lVar7 * -0x5555555555555555 + 1;
  if (uVar1 < 0x2aaaaaaaaaaaaab) {
    local_50 = param_1 + 2;
    lVar8 = *local_50 - *param_1 >> 5;
    uVar10 = lVar8 * 0x5555555555555556;
    if (uVar10 < uVar1 || uVar10 - uVar1 == 0) {
      uVar10 = uVar1;
    }
    if (0x155555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      uVar10 = 0x2aaaaaaaaaaaaaa;
    }
    if (uVar10 == 0) {
      local_70 = (void *)0x0;
    }
    else {
      if (0x2aaaaaaaaaaaaaa < uVar10) goto LAB_005d0154;
      local_70 = (void *)_Znwm(uVar10 * 0x60);
    }
    uVar12 = *param_2;
    uVar14 = param_2[3];
    uVar13 = param_2[2];
    local_68 = (undefined8 *)((long)local_70 + lVar7 * 0x20);
    uVar9 = param_2[6];
    uVar11 = *(undefined8 *)((long)param_2 + 0x55);
    pvStack_58 = (void *)((long)local_70 + uVar10 * 0x60);
    local_68[1] = param_2[1];
    *local_68 = uVar12;
    local_68[3] = uVar14;
    local_68[2] = uVar13;
    uVar14 = param_2[5];
    uVar13 = param_2[4];
    local_68[6] = uVar9;
    uVar9 = param_2[9];
    uVar12 = param_2[10];
    local_68[5] = uVar14;
    local_68[4] = uVar13;
    uVar13 = param_2[7];
    local_68[8] = param_2[8];
    local_68[7] = uVar13;
    *(undefined8 *)((long)local_68 + 0x55) = uVar11;
    local_68[9] = uVar9;
    local_68[10] = uVar12;
    local_60 = local_68 + 0xc;
    param_2[4] = 0;
    param_2[5] = 0;
    param_2[8] = 0;
    param_2[9] = 0;
    param_2[6] = 0;
    param_2[7] = 0;
    FUN_005d0190(param_1,&local_70);
    puVar3 = local_68;
    lVar7 = param_1[1];
    while (puVar4 = local_60, local_60 != puVar3) {
      pvVar6 = (void *)local_60[-5];
      puVar5 = local_60 + -0xc;
      if (pvVar6 != (void *)0x0) {
        local_60[-4] = pvVar6;
        local_60 = local_60 + -0xc;
        _ZdlPv(pvVar6);
        puVar5 = local_60;
      }
      local_60 = puVar5;
      pvVar6 = (void *)puVar4[-8];
      if (pvVar6 != (void *)0x0) {
        puVar4[-7] = pvVar6;
        _ZdlPv(pvVar6);
      }
    }
    if (local_70 != (void *)0x0) {
      _ZdlPv(local_70);
    }
    if (*(long *)(lVar2 + 0x28) == local_48) {
      return lVar7;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != local_48) goto LAB_005d018c;
    FUN_005d0330(param_1);
LAB_005d0154:
    if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      FUN_00440e80();
    }
  }
LAB_005d018c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cffac"></a> `005cffac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005cffb0"></a> `005cffb0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cffb4"></a> `005cffb4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005cffb8"></a> `005cffb8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cffbc"></a> `005cffbc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005cffc0"></a> `005cffc0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-005cffc4"></a> `005cffc4` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005cffc8"></a> `005cffc8` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-005cffcc"></a> `005cffcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005cffd0"></a> `005cffd0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005cffd4"></a> `005cffd4` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-005cffd8"></a> `005cffd8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005cffdc"></a> `005cffdc` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-005cffe0"></a> `005cffe0` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-005cffe4"></a> `005cffe4` | `08 fd 45 93` | asr x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-005cffe8"></a> `005cffe8` | `17 7d 0b 9b` | mul x23,x8,x11 | `FALL_THROUGH`
<a id="insn-005cffec"></a> `005cffec` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-005cfff0"></a> `005cfff0` | `48 55 e0 f2` | movk x8,#0x2aa, LSL #48 | `FALL_THROUGH`
<a id="insn-005cfff4"></a> `005cfff4` | `e9 06 00 91` | add x9,x23,#0x1 | `FALL_THROUGH`
<a id="insn-005cfff8"></a> `005cfff8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-005cfffc"></a> `005cfffc` | `08 0a 00 54` | b.hi 0x005d013c | `CONDITIONAL_JUMP`
<a id="insn-005d0000"></a> `005d0000` | `ec 03 13 aa` | mov x12,x19 | `FALL_THROUGH`
<a id="insn-005d0004"></a> `005d0004` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-005d0008"></a> `005d0008` | `8d 0d 41 f8` | ldr x13,[x12, #0x10]! | `FALL_THROUGH`
<a id="insn-005d000c"></a> `005d000c` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005d0010"></a> `005d0010` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-005d0014"></a> `005d0014` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-005d0018"></a> `005d0018` | `4a fd 45 93` | asr x10,x10,#0x5 | `FALL_THROUGH`
<a id="insn-005d001c"></a> `005d001c` | `ad 2a e0 f2` | movk x13,#0x155, LSL #48 | `FALL_THROUGH`
<a id="insn-005d0020"></a> `005d0020` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-005d0024"></a> `005d0024` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005d0028"></a> `005d0028` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-005d002c"></a> `005d002c` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-005d0030"></a> `005d0030` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-005d0034"></a> `005d0034` | `36 31 88 9a` | csel x22,x9,x8,cc | `FALL_THROUGH`
<a id="insn-005d0038"></a> `005d0038` | `f6 00 00 b4` | cbz x22,0x005d0054 | `CONDITIONAL_JUMP`
<a id="insn-005d003c"></a> `005d003c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-005d0040"></a> `005d0040` | `a8 08 00 54` | b.hi 0x005d0154 | `CONDITIONAL_JUMP`
<a id="insn-005d0044"></a> `005d0044` | `c8 06 16 8b` | add x8,x22,x22, LSL #0x1 | `FALL_THROUGH`
<a id="insn-005d0048"></a> `005d0048` | `00 e9 7b d3` | lsl x0,x8,#0x5 | `FALL_THROUGH`
<a id="insn-005d004c"></a> `005d004c` | `91 1e 1a 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-005d0050"></a> `005d0050` | `02 00 00 14` | b 0x005d0058 | `UNCONDITIONAL_JUMP`
<a id="insn-005d0054"></a> `005d0054` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-005d0058"></a> `005d0058` | `08 0c 80 52` | mov w8,#0x60 | `FALL_THROUGH`
<a id="insn-005d005c"></a> `005d005c` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-005d0060"></a> `005d0060` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-005d0064"></a> `005d0064` | `e9 02 08 9b` | madd x9,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-005d0068"></a> `005d0068` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-005d006c"></a> `005d006c` | `8c 52 45 f8` | ldur x12,[x20, #0x55] | `FALL_THROUGH`
<a id="insn-005d0070"></a> `005d0070` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-005d0074"></a> `005d0074` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-005d0078"></a> `005d0078` | `20 05 00 ad` | stp q0,q1,[x9] | `FALL_THROUGH`
<a id="insn-005d007c"></a> `005d007c` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-005d0080"></a> `005d0080` | `2a 19 00 f9` | str x10,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-005d0084"></a> `005d0084` | `8a ae 44 a9` | ldp x10,x11,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-005d0088"></a> `005d0088` | `20 09 80 3d` | str q0,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-005d008c"></a> `005d008c` | `80 82 c3 3c` | ldur q0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005d0090"></a> `005d0090` | `e0 27 00 a9` | stp x0,x9,[sp] | `FALL_THROUGH`
<a id="insn-005d0094"></a> `005d0094` | `20 81 83 3c` | stur q0,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-005d0098"></a> `005d0098` | `2c 51 05 f8` | stur x12,[x9, #0x55] | `FALL_THROUGH`
<a id="insn-005d009c"></a> `005d009c` | `2a ad 04 a9` | stp x10,x11,[x9, #0x48] | `FALL_THROUGH`
<a id="insn-005d00a0"></a> `005d00a0` | `29 81 01 91` | add x9,x9,#0x60 | `FALL_THROUGH`
<a id="insn-005d00a4"></a> `005d00a4` | `9f 7e 02 a9` | stp xzr,xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-005d00a8"></a> `005d00a8` | `9f 7e 04 a9` | stp xzr,xzr,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-005d00ac"></a> `005d00ac` | `9f 7e 03 a9` | stp xzr,xzr,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-005d00b0"></a> `005d00b0` | `e9 23 01 a9` | stp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d00b4"></a> `005d00b4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-005d00b8"></a> `005d00b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d00bc"></a> `005d00bc` | `35 00 00 94` | bl 0x005d0190 | `UNCONDITIONAL_CALL`
<a id="insn-005d00c0"></a> `005d00c0` | `f4 db 40 a9` | ldp x20,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005d00c4"></a> `005d00c4` | `73 06 40 f9` | ldr x19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-005d00c8"></a> `005d00c8` | `02 00 00 14` | b 0x005d00d0 | `UNCONDITIONAL_JUMP`
<a id="insn-005d00cc"></a> `005d00cc` | `f6 0b 40 f9` | ldr x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d00d0"></a> `005d00d0` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-005d00d4"></a> `005d00d4` | `80 01 00 54` | b.eq 0x005d0104 | `CONDITIONAL_JUMP`
<a id="insn-005d00d8"></a> `005d00d8` | `c0 82 5d f8` | ldur x0,[x22, #-0x28] | `FALL_THROUGH`
<a id="insn-005d00dc"></a> `005d00dc` | `c8 82 01 d1` | sub x8,x22,#0x60 | `FALL_THROUGH`
<a id="insn-005d00e0"></a> `005d00e0` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d00e4"></a> `005d00e4` | `60 00 00 b4` | cbz x0,0x005d00f0 | `CONDITIONAL_JUMP`
<a id="insn-005d00e8"></a> `005d00e8` | `c0 02 1e f8` | stur x0,[x22, #-0x20] | `FALL_THROUGH`
<a id="insn-005d00ec"></a> `005d00ec` | `71 1e 1a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-005d00f0"></a> `005d00f0` | `c0 02 5c f8` | ldur x0,[x22, #-0x40] | `FALL_THROUGH`
<a id="insn-005d00f4"></a> `005d00f4` | `c0 fe ff b4` | cbz x0,0x005d00cc | `CONDITIONAL_JUMP`
<a id="insn-005d00f8"></a> `005d00f8` | `c0 82 1c f8` | stur x0,[x22, #-0x38] | `FALL_THROUGH`
<a id="insn-005d00fc"></a> `005d00fc` | `6d 1e 1a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0100"></a> `005d0100` | `f3 ff ff 17` | b 0x005d00cc | `UNCONDITIONAL_JUMP`
<a id="insn-005d0104"></a> `005d0104` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-005d0108"></a> `005d0108` | `40 00 00 b4` | cbz x0,0x005d0110 | `CONDITIONAL_JUMP`
<a id="insn-005d010c"></a> `005d010c` | `69 1e 1a 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0110"></a> `005d0110` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0114"></a> `005d0114` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d0118"></a> `005d0118` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d011c"></a> `005d011c` | `81 03 00 54` | b.ne 0x005d018c | `CONDITIONAL_JUMP`
<a id="insn-005d0120"></a> `005d0120` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d0124"></a> `005d0124` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005d0128"></a> `005d0128` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005d012c"></a> `005d012c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005d0130"></a> `005d0130` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005d0134"></a> `005d0134` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005d0138"></a> `005d0138` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005d013c"></a> `005d013c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0140"></a> `005d0140` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d0144"></a> `005d0144` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d0148"></a> `005d0148` | `21 02 00 54` | b.ne 0x005d018c | `CONDITIONAL_JUMP`
<a id="insn-005d014c"></a> `005d014c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d0150"></a> `005d0150` | `78 00 00 94` | bl 0x005d0330 | `UNCONDITIONAL_CALL`
<a id="insn-005d0154"></a> `005d0154` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0158"></a> `005d0158` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d015c"></a> `005d015c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d0160"></a> `005d0160` | `61 01 00 54` | b.ne 0x005d018c | `CONDITIONAL_JUMP`
<a id="insn-005d0164"></a> `005d0164` | `47 c3 f9 97` | bl 0x00440e80 | `CALL_TERMINATOR`
<a id="insn-005d018c"></a> `005d018c` | `55 1e 1a 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cffac`](#insn-005cffac) 範囲 `[['005cffac', '005cffff']]`
  - `CONDITIONAL_JUMP` [`005cfffc`](#insn-005cfffc) → [`005d013c`](#insn-005d013c)
  - `FALL_THROUGH` [`005cfffc`](#insn-005cfffc) → [`005d0000`](#insn-005d0000)
- ブロック [`005d0000`](#insn-005d0000) 範囲 `[['005d0000', '005d003b']]`
  - `CONDITIONAL_JUMP` [`005d0038`](#insn-005d0038) → [`005d0054`](#insn-005d0054)
  - `FALL_THROUGH` [`005d0038`](#insn-005d0038) → [`005d003c`](#insn-005d003c)
- ブロック [`005d003c`](#insn-005d003c) 範囲 `[['005d003c', '005d0043']]`
  - `CONDITIONAL_JUMP` [`005d0040`](#insn-005d0040) → [`005d0154`](#insn-005d0154)
  - `FALL_THROUGH` [`005d0040`](#insn-005d0040) → [`005d0044`](#insn-005d0044)
- ブロック [`005d0044`](#insn-005d0044) 範囲 `[['005d0044', '005d0053']]`
  - `UNCONDITIONAL_JUMP` [`005d0050`](#insn-005d0050) → [`005d0058`](#insn-005d0058)
- ブロック [`005d0054`](#insn-005d0054) 範囲 `[['005d0054', '005d0057']]`
  - `FALL_THROUGH` [`005d0054`](#insn-005d0054) → [`005d0058`](#insn-005d0058)
- ブロック [`005d0058`](#insn-005d0058) 範囲 `[['005d0058', '005d00cb']]`
  - `UNCONDITIONAL_JUMP` [`005d00c8`](#insn-005d00c8) → [`005d00d0`](#insn-005d00d0)
- ブロック [`005d00cc`](#insn-005d00cc) 範囲 `[['005d00cc', '005d00cf']]`
  - `FALL_THROUGH` [`005d00cc`](#insn-005d00cc) → [`005d00d0`](#insn-005d00d0)
- ブロック [`005d00d0`](#insn-005d00d0) 範囲 `[['005d00d0', '005d00d7']]`
  - `CONDITIONAL_JUMP` [`005d00d4`](#insn-005d00d4) → [`005d0104`](#insn-005d0104)
  - `FALL_THROUGH` [`005d00d4`](#insn-005d00d4) → [`005d00d8`](#insn-005d00d8)
- ブロック [`005d00d8`](#insn-005d00d8) 範囲 `[['005d00d8', '005d00e7']]`
  - `CONDITIONAL_JUMP` [`005d00e4`](#insn-005d00e4) → [`005d00f0`](#insn-005d00f0)
  - `FALL_THROUGH` [`005d00e4`](#insn-005d00e4) → [`005d00e8`](#insn-005d00e8)
- ブロック [`005d00e8`](#insn-005d00e8) 範囲 `[['005d00e8', '005d00ef']]`
  - `FALL_THROUGH` [`005d00ec`](#insn-005d00ec) → [`005d00f0`](#insn-005d00f0)
- ブロック [`005d00f0`](#insn-005d00f0) 範囲 `[['005d00f0', '005d00f7']]`
  - `CONDITIONAL_JUMP` [`005d00f4`](#insn-005d00f4) → [`005d00cc`](#insn-005d00cc)
  - `FALL_THROUGH` [`005d00f4`](#insn-005d00f4) → [`005d00f8`](#insn-005d00f8)
- ブロック [`005d00f8`](#insn-005d00f8) 範囲 `[['005d00f8', '005d0103']]`
  - `UNCONDITIONAL_JUMP` [`005d0100`](#insn-005d0100) → [`005d00cc`](#insn-005d00cc)
- ブロック [`005d0104`](#insn-005d0104) 範囲 `[['005d0104', '005d010b']]`
  - `CONDITIONAL_JUMP` [`005d0108`](#insn-005d0108) → [`005d0110`](#insn-005d0110)
  - `FALL_THROUGH` [`005d0108`](#insn-005d0108) → [`005d010c`](#insn-005d010c)
- ブロック [`005d010c`](#insn-005d010c) 範囲 `[['005d010c', '005d010f']]`
  - `FALL_THROUGH` [`005d010c`](#insn-005d010c) → [`005d0110`](#insn-005d0110)
- ブロック [`005d0110`](#insn-005d0110) 範囲 `[['005d0110', '005d011f']]`
  - `CONDITIONAL_JUMP` [`005d011c`](#insn-005d011c) → [`005d018c`](#insn-005d018c)
  - `FALL_THROUGH` [`005d011c`](#insn-005d011c) → [`005d0120`](#insn-005d0120)
- ブロック [`005d0120`](#insn-005d0120) 範囲 `[['005d0120', '005d013b']]`
- ブロック [`005d013c`](#insn-005d013c) 範囲 `[['005d013c', '005d014b']]`
  - `CONDITIONAL_JUMP` [`005d0148`](#insn-005d0148) → [`005d018c`](#insn-005d018c)
  - `FALL_THROUGH` [`005d0148`](#insn-005d0148) → [`005d014c`](#insn-005d014c)
- ブロック [`005d014c`](#insn-005d014c) 範囲 `[['005d014c', '005d0153']]`
  - `FALL_THROUGH` [`005d0150`](#insn-005d0150) → [`005d0154`](#insn-005d0154)
- ブロック [`005d0154`](#insn-005d0154) 範囲 `[['005d0154', '005d0163']]`
  - `CONDITIONAL_JUMP` [`005d0160`](#insn-005d0160) → [`005d018c`](#insn-005d018c)
  - `FALL_THROUGH` [`005d0160`](#insn-005d0160) → [`005d0164`](#insn-005d0164)
- ブロック [`005d0164`](#insn-005d0164) 範囲 `[['005d0164', '005d0167']]`
- ブロック [`005d018c`](#insn-005d018c) 範囲 `[['005d018c', '005d018f']]`

## 命令位置別の参照

- [`005cffb0`](#insn-005cffb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cffb4`](#insn-005cffb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cffb8`](#insn-005cffb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cffbc`](#insn-005cffbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cffd8`](#insn-005cffd8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cfffc`](#insn-005cfffc) → [`005d013c`](#insn-005d013c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d000c`](#insn-005d000c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0038`](#insn-005d0038) → [`005d0054`](#insn-005d0054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0040`](#insn-005d0040) → [`005d0154`](#insn-005d0154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d004c`](#insn-005d004c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`005d0050`](#insn-005d0050) → [`005d0058`](#insn-005d0058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0090`](#insn-005d0090) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00b0`](#insn-005d00b0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00bc`](#insn-005d00bc) → [`005d0190`](../005d0/005d0190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d0190` · 推定シンボル `None` · 推定型 `None`
- [`005d00c0`](#insn-005d00c0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00c8`](#insn-005d00c8) → [`005d00d0`](#insn-005d00d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00cc`](#insn-005d00cc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00d4`](#insn-005d00d4) → [`005d0104`](#insn-005d0104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00e0`](#insn-005d00e0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00e4`](#insn-005d00e4) → [`005d00f0`](#insn-005d00f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00ec`](#insn-005d00ec) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`005d00f4`](#insn-005d00f4) → [`005d00cc`](#insn-005d00cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00fc`](#insn-005d00fc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`005d0100`](#insn-005d0100) → [`005d00cc`](#insn-005d00cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0104`](#insn-005d0104) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0108`](#insn-005d0108) → [`005d0110`](#insn-005d0110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d010c`](#insn-005d010c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`005d0114`](#insn-005d0114) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d011c`](#insn-005d011c) → [`005d018c`](#insn-005d018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0124`](#insn-005d0124) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0128`](#insn-005d0128) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d012c`](#insn-005d012c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0130`](#insn-005d0130) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0140`](#insn-005d0140) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0148`](#insn-005d0148) → [`005d018c`](#insn-005d018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0150`](#insn-005d0150) → [`005d0330`](../005d0/005d0330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d0330` · 推定シンボル `None` · 推定型 `None`
- [`005d0158`](#insn-005d0158) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0160`](#insn-005d0160) → [`005d018c`](#insn-005d018c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0164`](#insn-005d0164) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`
- [`005d018c`](#insn-005d018c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cffb0`](#insn-005cffb0)

~~~json
{
  "source": "005cffb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cffb4`](#insn-005cffb4)

~~~json
{
  "source": "005cffb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cffb8`](#insn-005cffb8)

~~~json
{
  "source": "005cffb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cffbc`](#insn-005cffbc)

~~~json
{
  "source": "005cffbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cffd8`](#insn-005cffd8)

~~~json
{
  "source": "005cffd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cfffc`](#insn-005cfffc)

~~~json
{
  "source": "005cfffc",
  "target": "005d013c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d000c`](#insn-005d000c)

~~~json
{
  "source": "005d000c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0038`](#insn-005d0038)

~~~json
{
  "source": "005d0038",
  "target": "005d0054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0040`](#insn-005d0040)

~~~json
{
  "source": "005d0040",
  "target": "005d0154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d004c`](#insn-005d004c)

~~~json
{
  "source": "005d004c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0050`](#insn-005d0050)

~~~json
{
  "source": "005d0050",
  "target": "005d0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0090`](#insn-005d0090)

~~~json
{
  "source": "005d0090",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00b0`](#insn-005d00b0)

~~~json
{
  "source": "005d00b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00bc`](#insn-005d00bc)

~~~json
{
  "source": "005d00bc",
  "target": "005d0190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d00c0`](#insn-005d00c0)

~~~json
{
  "source": "005d00c0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00c8`](#insn-005d00c8)

~~~json
{
  "source": "005d00c8",
  "target": "005d00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00cc`](#insn-005d00cc)

~~~json
{
  "source": "005d00cc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00d4`](#insn-005d00d4)

~~~json
{
  "source": "005d00d4",
  "target": "005d0104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00e0`](#insn-005d00e0)

~~~json
{
  "source": "005d00e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00e4`](#insn-005d00e4)

~~~json
{
  "source": "005d00e4",
  "target": "005d00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00ec`](#insn-005d00ec)

~~~json
{
  "source": "005d00ec",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d00f4`](#insn-005d00f4)

~~~json
{
  "source": "005d00f4",
  "target": "005d00cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00fc`](#insn-005d00fc)

~~~json
{
  "source": "005d00fc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0100`](#insn-005d0100)

~~~json
{
  "source": "005d0100",
  "target": "005d00cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0104`](#insn-005d0104)

~~~json
{
  "source": "005d0104",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0108`](#insn-005d0108)

~~~json
{
  "source": "005d0108",
  "target": "005d0110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d010c`](#insn-005d010c)

~~~json
{
  "source": "005d010c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0114`](#insn-005d0114)

~~~json
{
  "source": "005d0114",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d011c`](#insn-005d011c)

~~~json
{
  "source": "005d011c",
  "target": "005d018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0124`](#insn-005d0124)

~~~json
{
  "source": "005d0124",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0128`](#insn-005d0128)

~~~json
{
  "source": "005d0128",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d012c`](#insn-005d012c)

~~~json
{
  "source": "005d012c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0130`](#insn-005d0130)

~~~json
{
  "source": "005d0130",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0140`](#insn-005d0140)

~~~json
{
  "source": "005d0140",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0148`](#insn-005d0148)

~~~json
{
  "source": "005d0148",
  "target": "005d018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0150`](#insn-005d0150)

~~~json
{
  "source": "005d0150",
  "target": "005d0330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0158`](#insn-005d0158)

~~~json
{
  "source": "005d0158",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0160`](#insn-005d0160)

~~~json
{
  "source": "005d0160",
  "target": "005d018c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0164`](#insn-005d0164)

~~~json
{
  "source": "005d0164",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d018c`](#insn-005d018c)

~~~json
{
  "source": "005d018c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
