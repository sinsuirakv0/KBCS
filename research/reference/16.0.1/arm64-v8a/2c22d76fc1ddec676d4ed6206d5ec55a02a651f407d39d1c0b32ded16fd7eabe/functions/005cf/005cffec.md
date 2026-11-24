# 005cffec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005cffac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0016.md#compare-008b366c3523f9475ab4ff8a3793725b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `005d002c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d002c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0016.md#compare-8830544535f1cdefcb044e40e50bf8ce)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005cffec",
  "name": "FUN_005cffec",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1291dbd585dbd90cdd3e44682f2c977966aab8ab04fd37ff777ec80f67d42d71",
  "source_text_sha256": "1291dbd585dbd90cdd3e44682f2c977966aab8ab04fd37ff777ec80f67d42d71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005cffec",
        "005d01a7"
      ],
      [
        "005d01cc",
        "005d01cf"
      ]
    ],
    "bytes_sha256": "de282421c95b7c38d3703bacccbd7f0ce2010f90bcf12d78a24a1391ced86b09",
    "instruction_count": 112,
    "instruction_bytes": 448,
    "body_bytes": 448,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005cf6c0](../005cf/005cf6c0.md)
- [005d69f0](../005d6/005d69f0.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [005d01d0](../005d0/005d01d0.md)
- [005d0370](../005d0/005d0370.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3004 bytes

~~~c

long FUN_005cffec(long *param_1,undefined8 *param_2)

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
      if (0x2aaaaaaaaaaaaaa < uVar10) goto LAB_005d0194;
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
    FUN_005d01d0(param_1,&local_70);
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
    if (*(long *)(lVar2 + 0x28) != local_48) goto LAB_005d01cc;
    FUN_005d0370(param_1);
LAB_005d0194:
    if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      FUN_00440ec0();
    }
  }
LAB_005d01cc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005cffec"></a> `005cffec` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005cfff0"></a> `005cfff0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005cfff4"></a> `005cfff4` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005cfff8"></a> `005cfff8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005cfffc"></a> `005cfffc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005d0000"></a> `005d0000` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-005d0004"></a> `005d0004` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005d0008"></a> `005d0008` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-005d000c"></a> `005d000c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005d0010"></a> `005d0010` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0014"></a> `005d0014` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-005d0018"></a> `005d0018` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d001c"></a> `005d001c` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-005d0020"></a> `005d0020` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-005d0024"></a> `005d0024` | `08 fd 45 93` | asr x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-005d0028"></a> `005d0028` | `17 7d 0b 9b` | mul x23,x8,x11 | `FALL_THROUGH`
<a id="insn-005d002c"></a> `005d002c` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-005d0030"></a> `005d0030` | `48 55 e0 f2` | movk x8,#0x2aa, LSL #48 | `FALL_THROUGH`
<a id="insn-005d0034"></a> `005d0034` | `e9 06 00 91` | add x9,x23,#0x1 | `FALL_THROUGH`
<a id="insn-005d0038"></a> `005d0038` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-005d003c"></a> `005d003c` | `08 0a 00 54` | b.hi 0x005d017c | `CONDITIONAL_JUMP`
<a id="insn-005d0040"></a> `005d0040` | `ec 03 13 aa` | mov x12,x19 | `FALL_THROUGH`
<a id="insn-005d0044"></a> `005d0044` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-005d0048"></a> `005d0048` | `8d 0d 41 f8` | ldr x13,[x12, #0x10]! | `FALL_THROUGH`
<a id="insn-005d004c"></a> `005d004c` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005d0050"></a> `005d0050` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-005d0054"></a> `005d0054` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-005d0058"></a> `005d0058` | `4a fd 45 93` | asr x10,x10,#0x5 | `FALL_THROUGH`
<a id="insn-005d005c"></a> `005d005c` | `ad 2a e0 f2` | movk x13,#0x155, LSL #48 | `FALL_THROUGH`
<a id="insn-005d0060"></a> `005d0060` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-005d0064"></a> `005d0064` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-005d0068"></a> `005d0068` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-005d006c"></a> `005d006c` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-005d0070"></a> `005d0070` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-005d0074"></a> `005d0074` | `36 31 88 9a` | csel x22,x9,x8,cc | `FALL_THROUGH`
<a id="insn-005d0078"></a> `005d0078` | `f6 00 00 b4` | cbz x22,0x005d0094 | `CONDITIONAL_JUMP`
<a id="insn-005d007c"></a> `005d007c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-005d0080"></a> `005d0080` | `a8 08 00 54` | b.hi 0x005d0194 | `CONDITIONAL_JUMP`
<a id="insn-005d0084"></a> `005d0084` | `c8 06 16 8b` | add x8,x22,x22, LSL #0x1 | `FALL_THROUGH`
<a id="insn-005d0088"></a> `005d0088` | `00 e9 7b d3` | lsl x0,x8,#0x5 | `FALL_THROUGH`
<a id="insn-005d008c"></a> `005d008c` | `81 1f 1a 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-005d0090"></a> `005d0090` | `02 00 00 14` | b 0x005d0098 | `UNCONDITIONAL_JUMP`
<a id="insn-005d0094"></a> `005d0094` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-005d0098"></a> `005d0098` | `08 0c 80 52` | mov w8,#0x60 | `FALL_THROUGH`
<a id="insn-005d009c"></a> `005d009c` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-005d00a0"></a> `005d00a0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-005d00a4"></a> `005d00a4` | `e9 02 08 9b` | madd x9,x23,x8,x0 | `FALL_THROUGH`
<a id="insn-005d00a8"></a> `005d00a8` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-005d00ac"></a> `005d00ac` | `8c 52 45 f8` | ldur x12,[x20, #0x55] | `FALL_THROUGH`
<a id="insn-005d00b0"></a> `005d00b0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-005d00b4"></a> `005d00b4` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-005d00b8"></a> `005d00b8` | `20 05 00 ad` | stp q0,q1,[x9] | `FALL_THROUGH`
<a id="insn-005d00bc"></a> `005d00bc` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-005d00c0"></a> `005d00c0` | `2a 19 00 f9` | str x10,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-005d00c4"></a> `005d00c4` | `8a ae 44 a9` | ldp x10,x11,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-005d00c8"></a> `005d00c8` | `20 09 80 3d` | str q0,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-005d00cc"></a> `005d00cc` | `80 82 c3 3c` | ldur q0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-005d00d0"></a> `005d00d0` | `e0 27 00 a9` | stp x0,x9,[sp] | `FALL_THROUGH`
<a id="insn-005d00d4"></a> `005d00d4` | `20 81 83 3c` | stur q0,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-005d00d8"></a> `005d00d8` | `2c 51 05 f8` | stur x12,[x9, #0x55] | `FALL_THROUGH`
<a id="insn-005d00dc"></a> `005d00dc` | `2a ad 04 a9` | stp x10,x11,[x9, #0x48] | `FALL_THROUGH`
<a id="insn-005d00e0"></a> `005d00e0` | `29 81 01 91` | add x9,x9,#0x60 | `FALL_THROUGH`
<a id="insn-005d00e4"></a> `005d00e4` | `9f 7e 02 a9` | stp xzr,xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-005d00e8"></a> `005d00e8` | `9f 7e 04 a9` | stp xzr,xzr,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-005d00ec"></a> `005d00ec` | `9f 7e 03 a9` | stp xzr,xzr,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-005d00f0"></a> `005d00f0` | `e9 23 01 a9` | stp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d00f4"></a> `005d00f4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-005d00f8"></a> `005d00f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d00fc"></a> `005d00fc` | `35 00 00 94` | bl 0x005d01d0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0100"></a> `005d0100` | `f4 db 40 a9` | ldp x20,x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-005d0104"></a> `005d0104` | `73 06 40 f9` | ldr x19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-005d0108"></a> `005d0108` | `02 00 00 14` | b 0x005d0110 | `UNCONDITIONAL_JUMP`
<a id="insn-005d010c"></a> `005d010c` | `f6 0b 40 f9` | ldr x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d0110"></a> `005d0110` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-005d0114"></a> `005d0114` | `80 01 00 54` | b.eq 0x005d0144 | `CONDITIONAL_JUMP`
<a id="insn-005d0118"></a> `005d0118` | `c0 82 5d f8` | ldur x0,[x22, #-0x28] | `FALL_THROUGH`
<a id="insn-005d011c"></a> `005d011c` | `c8 82 01 d1` | sub x8,x22,#0x60 | `FALL_THROUGH`
<a id="insn-005d0120"></a> `005d0120` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005d0124"></a> `005d0124` | `60 00 00 b4` | cbz x0,0x005d0130 | `CONDITIONAL_JUMP`
<a id="insn-005d0128"></a> `005d0128` | `c0 02 1e f8` | stur x0,[x22, #-0x20] | `FALL_THROUGH`
<a id="insn-005d012c"></a> `005d012c` | `61 1f 1a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0130"></a> `005d0130` | `c0 02 5c f8` | ldur x0,[x22, #-0x40] | `FALL_THROUGH`
<a id="insn-005d0134"></a> `005d0134` | `c0 fe ff b4` | cbz x0,0x005d010c | `CONDITIONAL_JUMP`
<a id="insn-005d0138"></a> `005d0138` | `c0 82 1c f8` | stur x0,[x22, #-0x38] | `FALL_THROUGH`
<a id="insn-005d013c"></a> `005d013c` | `5d 1f 1a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0140"></a> `005d0140` | `f3 ff ff 17` | b 0x005d010c | `UNCONDITIONAL_JUMP`
<a id="insn-005d0144"></a> `005d0144` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-005d0148"></a> `005d0148` | `40 00 00 b4` | cbz x0,0x005d0150 | `CONDITIONAL_JUMP`
<a id="insn-005d014c"></a> `005d014c` | `59 1f 1a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-005d0150"></a> `005d0150` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0154"></a> `005d0154` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d0158"></a> `005d0158` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d015c"></a> `005d015c` | `81 03 00 54` | b.ne 0x005d01cc | `CONDITIONAL_JUMP`
<a id="insn-005d0160"></a> `005d0160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d0164"></a> `005d0164` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005d0168"></a> `005d0168` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005d016c"></a> `005d016c` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005d0170"></a> `005d0170` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005d0174"></a> `005d0174` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-005d0178"></a> `005d0178` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005d017c"></a> `005d017c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0180"></a> `005d0180` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d0184"></a> `005d0184` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d0188"></a> `005d0188` | `21 02 00 54` | b.ne 0x005d01cc | `CONDITIONAL_JUMP`
<a id="insn-005d018c"></a> `005d018c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005d0190"></a> `005d0190` | `78 00 00 94` | bl 0x005d0370 | `UNCONDITIONAL_CALL`
<a id="insn-005d0194"></a> `005d0194` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005d0198"></a> `005d0198` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-005d019c"></a> `005d019c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005d01a0"></a> `005d01a0` | `61 01 00 54` | b.ne 0x005d01cc | `CONDITIONAL_JUMP`
<a id="insn-005d01a4"></a> `005d01a4` | `47 c3 f9 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-005d01cc"></a> `005d01cc` | `45 1f 1a 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005cffec`](#insn-005cffec) 範囲 `[['005cffec', '005d003f']]`
  - `CONDITIONAL_JUMP` [`005d003c`](#insn-005d003c) → [`005d017c`](#insn-005d017c)
  - `FALL_THROUGH` [`005d003c`](#insn-005d003c) → [`005d0040`](#insn-005d0040)
- ブロック [`005d0040`](#insn-005d0040) 範囲 `[['005d0040', '005d007b']]`
  - `CONDITIONAL_JUMP` [`005d0078`](#insn-005d0078) → [`005d0094`](#insn-005d0094)
  - `FALL_THROUGH` [`005d0078`](#insn-005d0078) → [`005d007c`](#insn-005d007c)
- ブロック [`005d007c`](#insn-005d007c) 範囲 `[['005d007c', '005d0083']]`
  - `CONDITIONAL_JUMP` [`005d0080`](#insn-005d0080) → [`005d0194`](#insn-005d0194)
  - `FALL_THROUGH` [`005d0080`](#insn-005d0080) → [`005d0084`](#insn-005d0084)
- ブロック [`005d0084`](#insn-005d0084) 範囲 `[['005d0084', '005d0093']]`
  - `UNCONDITIONAL_JUMP` [`005d0090`](#insn-005d0090) → [`005d0098`](#insn-005d0098)
- ブロック [`005d0094`](#insn-005d0094) 範囲 `[['005d0094', '005d0097']]`
  - `FALL_THROUGH` [`005d0094`](#insn-005d0094) → [`005d0098`](#insn-005d0098)
- ブロック [`005d0098`](#insn-005d0098) 範囲 `[['005d0098', '005d010b']]`
  - `UNCONDITIONAL_JUMP` [`005d0108`](#insn-005d0108) → [`005d0110`](#insn-005d0110)
- ブロック [`005d010c`](#insn-005d010c) 範囲 `[['005d010c', '005d010f']]`
  - `FALL_THROUGH` [`005d010c`](#insn-005d010c) → [`005d0110`](#insn-005d0110)
- ブロック [`005d0110`](#insn-005d0110) 範囲 `[['005d0110', '005d0117']]`
  - `CONDITIONAL_JUMP` [`005d0114`](#insn-005d0114) → [`005d0144`](#insn-005d0144)
  - `FALL_THROUGH` [`005d0114`](#insn-005d0114) → [`005d0118`](#insn-005d0118)
- ブロック [`005d0118`](#insn-005d0118) 範囲 `[['005d0118', '005d0127']]`
  - `CONDITIONAL_JUMP` [`005d0124`](#insn-005d0124) → [`005d0130`](#insn-005d0130)
  - `FALL_THROUGH` [`005d0124`](#insn-005d0124) → [`005d0128`](#insn-005d0128)
- ブロック [`005d0128`](#insn-005d0128) 範囲 `[['005d0128', '005d012f']]`
  - `FALL_THROUGH` [`005d012c`](#insn-005d012c) → [`005d0130`](#insn-005d0130)
- ブロック [`005d0130`](#insn-005d0130) 範囲 `[['005d0130', '005d0137']]`
  - `CONDITIONAL_JUMP` [`005d0134`](#insn-005d0134) → [`005d010c`](#insn-005d010c)
  - `FALL_THROUGH` [`005d0134`](#insn-005d0134) → [`005d0138`](#insn-005d0138)
- ブロック [`005d0138`](#insn-005d0138) 範囲 `[['005d0138', '005d0143']]`
  - `UNCONDITIONAL_JUMP` [`005d0140`](#insn-005d0140) → [`005d010c`](#insn-005d010c)
- ブロック [`005d0144`](#insn-005d0144) 範囲 `[['005d0144', '005d014b']]`
  - `CONDITIONAL_JUMP` [`005d0148`](#insn-005d0148) → [`005d0150`](#insn-005d0150)
  - `FALL_THROUGH` [`005d0148`](#insn-005d0148) → [`005d014c`](#insn-005d014c)
- ブロック [`005d014c`](#insn-005d014c) 範囲 `[['005d014c', '005d014f']]`
  - `FALL_THROUGH` [`005d014c`](#insn-005d014c) → [`005d0150`](#insn-005d0150)
- ブロック [`005d0150`](#insn-005d0150) 範囲 `[['005d0150', '005d015f']]`
  - `CONDITIONAL_JUMP` [`005d015c`](#insn-005d015c) → [`005d01cc`](#insn-005d01cc)
  - `FALL_THROUGH` [`005d015c`](#insn-005d015c) → [`005d0160`](#insn-005d0160)
- ブロック [`005d0160`](#insn-005d0160) 範囲 `[['005d0160', '005d017b']]`
- ブロック [`005d017c`](#insn-005d017c) 範囲 `[['005d017c', '005d018b']]`
  - `CONDITIONAL_JUMP` [`005d0188`](#insn-005d0188) → [`005d01cc`](#insn-005d01cc)
  - `FALL_THROUGH` [`005d0188`](#insn-005d0188) → [`005d018c`](#insn-005d018c)
- ブロック [`005d018c`](#insn-005d018c) 範囲 `[['005d018c', '005d0193']]`
  - `FALL_THROUGH` [`005d0190`](#insn-005d0190) → [`005d0194`](#insn-005d0194)
- ブロック [`005d0194`](#insn-005d0194) 範囲 `[['005d0194', '005d01a3']]`
  - `CONDITIONAL_JUMP` [`005d01a0`](#insn-005d01a0) → [`005d01cc`](#insn-005d01cc)
  - `FALL_THROUGH` [`005d01a0`](#insn-005d01a0) → [`005d01a4`](#insn-005d01a4)
- ブロック [`005d01a4`](#insn-005d01a4) 範囲 `[['005d01a4', '005d01a7']]`
- ブロック [`005d01cc`](#insn-005d01cc) 範囲 `[['005d01cc', '005d01cf']]`

## 命令位置別の参照

- [`005cfff0`](#insn-005cfff0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cfff4`](#insn-005cfff4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cfff8`](#insn-005cfff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005cfffc`](#insn-005cfffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0018`](#insn-005d0018) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d003c`](#insn-005d003c) → [`005d017c`](#insn-005d017c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d004c`](#insn-005d004c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0078`](#insn-005d0078) → [`005d0094`](#insn-005d0094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0080`](#insn-005d0080) → [`005d0194`](#insn-005d0194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d008c`](#insn-005d008c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`005d0090`](#insn-005d0090) → [`005d0098`](#insn-005d0098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00d0`](#insn-005d00d0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00f0`](#insn-005d00f0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d00fc`](#insn-005d00fc) → [`005d01d0`](../005d0/005d01d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d01d0` · 推定シンボル `None` · 推定型 `None`
- [`005d0100`](#insn-005d0100) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0108`](#insn-005d0108) → [`005d0110`](#insn-005d0110) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d010c`](#insn-005d010c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0114`](#insn-005d0114) → [`005d0144`](#insn-005d0144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0120`](#insn-005d0120) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0124`](#insn-005d0124) → [`005d0130`](#insn-005d0130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d012c`](#insn-005d012c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005d0134`](#insn-005d0134) → [`005d010c`](#insn-005d010c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d013c`](#insn-005d013c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005d0140`](#insn-005d0140) → [`005d010c`](#insn-005d010c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0144`](#insn-005d0144) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0148`](#insn-005d0148) → [`005d0150`](#insn-005d0150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d014c`](#insn-005d014c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`005d0154`](#insn-005d0154) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d015c`](#insn-005d015c) → [`005d01cc`](#insn-005d01cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0164`](#insn-005d0164) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0168`](#insn-005d0168) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d016c`](#insn-005d016c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0170`](#insn-005d0170) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0180`](#insn-005d0180) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0188`](#insn-005d0188) → [`005d01cc`](#insn-005d01cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d0190`](#insn-005d0190) → [`005d0370`](../005d0/005d0370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005d0370` · 推定シンボル `None` · 推定型 `None`
- [`005d0198`](#insn-005d0198) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d01a0`](#insn-005d01a0) → [`005d01cc`](#insn-005d01cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005d01a4`](#insn-005d01a4) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`005d01cc`](#insn-005d01cc) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005cfff0`](#insn-005cfff0)

~~~json
{
  "source": "005cfff0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cfff4`](#insn-005cfff4)

~~~json
{
  "source": "005cfff4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cfff8`](#insn-005cfff8)

~~~json
{
  "source": "005cfff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005cfffc`](#insn-005cfffc)

~~~json
{
  "source": "005cfffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0018`](#insn-005d0018)

~~~json
{
  "source": "005d0018",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d003c`](#insn-005d003c)

~~~json
{
  "source": "005d003c",
  "target": "005d017c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d004c`](#insn-005d004c)

~~~json
{
  "source": "005d004c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0078`](#insn-005d0078)

~~~json
{
  "source": "005d0078",
  "target": "005d0094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0080`](#insn-005d0080)

~~~json
{
  "source": "005d0080",
  "target": "005d0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d008c`](#insn-005d008c)

~~~json
{
  "source": "005d008c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0090`](#insn-005d0090)

~~~json
{
  "source": "005d0090",
  "target": "005d0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00d0`](#insn-005d00d0)

~~~json
{
  "source": "005d00d0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00f0`](#insn-005d00f0)

~~~json
{
  "source": "005d00f0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d00fc`](#insn-005d00fc)

~~~json
{
  "source": "005d00fc",
  "target": "005d01d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0100`](#insn-005d0100)

~~~json
{
  "source": "005d0100",
  "target": "Stack[-0x68]",
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
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0114`](#insn-005d0114)

~~~json
{
  "source": "005d0114",
  "target": "005d0144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0120`](#insn-005d0120)

~~~json
{
  "source": "005d0120",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0124`](#insn-005d0124)

~~~json
{
  "source": "005d0124",
  "target": "005d0130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d012c`](#insn-005d012c)

~~~json
{
  "source": "005d012c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0134`](#insn-005d0134)

~~~json
{
  "source": "005d0134",
  "target": "005d010c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d013c`](#insn-005d013c)

~~~json
{
  "source": "005d013c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0140`](#insn-005d0140)

~~~json
{
  "source": "005d0140",
  "target": "005d010c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0144`](#insn-005d0144)

~~~json
{
  "source": "005d0144",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0148`](#insn-005d0148)

~~~json
{
  "source": "005d0148",
  "target": "005d0150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d014c`](#insn-005d014c)

~~~json
{
  "source": "005d014c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0154`](#insn-005d0154)

~~~json
{
  "source": "005d0154",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d015c`](#insn-005d015c)

~~~json
{
  "source": "005d015c",
  "target": "005d01cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0164`](#insn-005d0164)

~~~json
{
  "source": "005d0164",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0168`](#insn-005d0168)

~~~json
{
  "source": "005d0168",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d016c`](#insn-005d016c)

~~~json
{
  "source": "005d016c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0170`](#insn-005d0170)

~~~json
{
  "source": "005d0170",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0180`](#insn-005d0180)

~~~json
{
  "source": "005d0180",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0188`](#insn-005d0188)

~~~json
{
  "source": "005d0188",
  "target": "005d01cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d0190`](#insn-005d0190)

~~~json
{
  "source": "005d0190",
  "target": "005d0370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d0198`](#insn-005d0198)

~~~json
{
  "source": "005d0198",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d01a0`](#insn-005d01a0)

~~~json
{
  "source": "005d01a0",
  "target": "005d01cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005d01a4`](#insn-005d01a4)

~~~json
{
  "source": "005d01a4",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005d01cc`](#insn-005d01cc)

~~~json
{
  "source": "005d01cc",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
