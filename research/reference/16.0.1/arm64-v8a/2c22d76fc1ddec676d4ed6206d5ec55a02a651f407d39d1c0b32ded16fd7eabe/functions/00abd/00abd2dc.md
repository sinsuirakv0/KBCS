# 00abd2dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abd0e0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd0e0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-7322b9c5dbb03530a848ae399f9db236)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abd34c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abd/00abd34c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-cee898b4b5345ca0444fcf6a15a522a7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abd2dc",
  "name": "FUN_00abd2dc",
  "size": 968,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07db65f7a8420cd9c72f940cd68facdbd0816d7548852814497763b73d03212c",
  "source_text_sha256": "07db65f7a8420cd9c72f940cd68facdbd0816d7548852814497763b73d03212c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abd2dc",
        "00abd69f"
      ],
      [
        "00abd6f4",
        "00abd6f7"
      ]
    ],
    "bytes_sha256": "6c76e69c997734e143e28e603301f6aa6023b6801247a0d9b77dcd4bcfa4eeab",
    "instruction_count": 242,
    "instruction_bytes": 968,
    "body_bytes": 968,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abe7f8](../00abe/00abe7f8.md)
- [00ac1d40](../00ac1/00ac1d40.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0046da48](../0046d/0046da48.md)
- [00470840](../00470/00470840.md)
- [0049f3f0](../0049f/0049f3f0.md)
- [00615cd0](../00615/00615cd0.md)
- [00800378](../00800/00800378.md)
- [0080062c](../00800/0080062c.md)
- [008056ec](../00805/008056ec.md)
- [0080b3c8](../0080b/0080b3c8.md)
- [008514f8](../00851/008514f8.md)
- [00860588](../00860/00860588.md)
- [00a65dec](../00a65/00a65dec.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6993 bytes

~~~c

undefined4 FUN_00abd2dc(long param_1)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  int iVar9;
  undefined8 uVar10;
  ulong uVar11;
  void *__dest;
  undefined8 *puVar12;
  ulong uVar13;
  ulong uVar14;
  undefined8 *extraout_x8;
  undefined8 *puVar15;
  ulong uVar16;
  void *pvVar17;
  undefined4 *puVar18;
  long lVar19;
  void *local_a0;
  void *pvStack_98;
  undefined8 local_90;
  undefined8 *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  if (*(int *)(param_1 + 0x38) == -1) {
LAB_00abd328:
    local_80 = (undefined8 *)0x0;
    local_78 = (undefined8 *)0x0;
    lVar19 = *(long *)(param_1 + 8);
    local_70 = (undefined8 *)0x0;
    if (*(long *)(param_1 + 0x10) == lVar19) {
      uVar7 = 1;
    }
    else {
      uVar11 = 0;
      do {
        if (-1 < *(int *)(lVar19 + uVar11 * 4)) {
          local_a0 = (void *)0x0;
          pvStack_98 = (void *)0x0;
          local_90 = 0;
          if (local_78 < local_70) {
            *local_78 = 0;
            local_78[1] = 0;
            local_78[2] = 0;
            local_78[1] = 0;
            *local_78 = 0;
            local_78[2] = 0;
            local_78 = local_78 + 3;
          }
          else {
            local_78 = (undefined8 *)FUN_00615cd0(&local_80,&local_a0);
            if (local_a0 != (void *)0x0) {
              pvStack_98 = local_a0;
              _ZdlPv(local_a0);
            }
          }
        }
        puVar12 = local_78;
        if (local_78 == local_80) {
          if (*(long *)(lVar3 + 0x28) != local_68) goto LAB_00abd6f4;
          FUN_0080b3c8(&local_80);
          goto LAB_00abd650;
        }
        if ((ulong)(*(long *)(param_1 + 0x10) - *(long *)(param_1 + 8) >> 2) <= uVar11) {
          if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_0049f3f0((long *)(param_1 + 8));
          }
          goto LAB_00abd6f4;
        }
        uVar7 = FUN_0046da48(*(undefined4 *)(*(long *)(param_1 + 8) + uVar11 * 4));
        puVar2 = (undefined4 *)puVar12[-2];
        if (puVar2 < (undefined4 *)puVar12[-1]) {
          puVar18 = puVar2 + 1;
          *puVar2 = uVar7;
        }
        else {
          puVar15 = puVar12 + -3;
          pvVar17 = (void *)*puVar15;
          lVar19 = (long)puVar2 - (long)pvVar17 >> 2;
          uVar14 = lVar19 + 1;
          if (uVar14 >> 0x3e != 0) goto LAB_00abd66c;
          uVar13 = (long)puVar12[-1] - (long)pvVar17;
          uVar16 = (long)uVar13 >> 1;
          if (uVar16 <= uVar14) {
            uVar16 = uVar14;
          }
          if (0x7ffffffffffffffb < uVar13) {
            uVar16 = 0x3fffffffffffffff;
          }
          if (uVar16 == 0) {
            __dest = (void *)0x0;
          }
          else {
            if (uVar16 >> 0x3e != 0) {
              if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                FUN_00440ec0();
              }
              goto LAB_00abd6f4;
            }
            __dest = (void *)_Znwm(uVar16 << 2);
                    /* try { // try from 00abd45c to 00bbd603 has its CatchHandler @ 00abd45c
                       catch() { ... } // from try @ 00abd45c with catch @ 00abd45c
                       catch() { ... } // from try @ 00abd6f8 with catch @ 00abd45c */
          }
          puVar1 = (undefined4 *)((long)__dest + lVar19 * 4);
          puVar18 = puVar1 + 1;
          *puVar1 = uVar7;
          memcpy(__dest,pvVar17,(long)puVar2 - (long)pvVar17);
          puVar12[-3] = __dest;
          puVar12[-2] = puVar18;
          puVar12[-1] = (void *)((long)__dest + uVar16 * 4);
          if (pvVar17 != (void *)0x0) {
            _ZdlPv(pvVar17);
          }
        }
        puVar12[-2] = puVar18;
        uVar11 = uVar11 + 1;
        lVar19 = *(long *)(param_1 + 8);
      } while (uVar11 < (ulong)(*(long *)(param_1 + 0x10) - lVar19 >> 2));
      puVar12 = local_80;
      if (local_78 != local_80) {
        uVar11 = 0;
        do {
          uVar14 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
          if (uVar14 < uVar11 || uVar14 - uVar11 == 0) goto LAB_00abd650;
          lVar19 = local_80[uVar11 * 3];
          if ((local_80 + uVar11 * 3)[1] == lVar19) {
LAB_00abd580:
            uVar7 = 0;
            puVar12 = local_78;
            puVar15 = local_78;
            puVar5 = local_80;
            goto joined_r0x00abd5a8;
          }
          uVar14 = 0;
          while( true ) {
            uVar7 = *(undefined4 *)(lVar19 + uVar14 * 4);
            uVar8 = FUN_00800378(uVar7);
            uVar7 = FUN_0080062c(uVar7);
            iVar9 = *(int *)(param_1 + 0x3c);
            if (iVar9 == -1) {
              iVar9 = FUN_008056ec(uVar8,uVar7);
              iVar9 = iVar9 + -1;
            }
            iVar9 = FUN_00a65dec(uVar8,uVar7,iVar9,*(undefined4 *)(param_1 + 0x40),0);
            uVar16 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
            if (iVar9 != 0) break;
            if (uVar16 < uVar11 || uVar16 - uVar11 == 0) goto LAB_00abd650;
            uVar14 = uVar14 + 1;
            lVar19 = local_80[uVar11 * 3];
            if ((ulong)((local_80 + uVar11 * 3)[1] - lVar19 >> 2) <= uVar14) goto LAB_00abd580;
          }
          uVar11 = uVar11 + 1;
          puVar12 = local_78;
        } while (uVar11 <= uVar16 && uVar16 - uVar11 != 0);
      }
      uVar7 = 1;
      puVar15 = puVar12;
      puVar5 = local_80;
      if (local_80 != (undefined8 *)0x0) {
joined_r0x00abd5a8:
        while (puVar4 = puVar12, puVar6 = local_80, puVar4 != local_80) {
          puVar12 = puVar4 + -3;
          pvVar17 = (void *)*puVar12;
          puVar15 = puVar5;
          local_80 = puVar6;
          if (pvVar17 != (void *)0x0) {
            puVar4[-2] = pvVar17;
            local_80 = puVar5;
            _ZdlPv(pvVar17);
            puVar15 = local_80;
            puVar5 = local_80;
            local_80 = puVar6;
          }
        }
        local_78 = local_80;
        local_80 = puVar5;
        _ZdlPv(puVar15);
      }
    }
  }
  else {
    uVar10 = FUN_008514f8();
    uVar11 = FUN_00860588(uVar10,*(undefined4 *)(param_1 + 0x38));
    if ((uVar11 & 1) != 0) goto LAB_00abd328;
    uVar7 = 0;
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00abd604 to 00bbd6f7 has its CatchHandler @ 00abd7b8 */
    return uVar7;
  }
LAB_00abd6f4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_00abd650:
  if (*(long *)(lVar3 + 0x28) == local_68) {
    FUN_0080b3c8(&local_80);
    puVar15 = extraout_x8;
LAB_00abd66c:
    if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      FUN_00470840(puVar15);
    }
  }
  goto LAB_00abd6f4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abd2dc"></a> `00abd2dc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abd2e0"></a> `00abd2e0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abd2e4"></a> `00abd2e4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abd2e8"></a> `00abd2e8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abd2ec"></a> `00abd2ec` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abd2f0"></a> `00abd2f0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abd2f4"></a> `00abd2f4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abd2f8"></a> `00abd2f8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00abd2fc"></a> `00abd2fc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abd300"></a> `00abd300` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abd304"></a> `00abd304` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abd308"></a> `00abd308` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd30c"></a> `00abd30c` | `08 38 40 b9` | ldr w8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abd310"></a> `00abd310` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abd314"></a> `00abd314` | `a0 00 00 54` | b.eq 0x00abd328 | `CONDITIONAL_JUMP`
<a id="insn-00abd318"></a> `00abd318` | `78 50 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abd31c"></a> `00abd31c` | `61 3a 40 b9` | ldr w1,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abd320"></a> `00abd320` | `9a 8c f6 97` | bl 0x00860588 | `UNCONDITIONAL_CALL`
<a id="insn-00abd324"></a> `00abd324` | `a0 12 00 36` | tbz w0,#0x0,0x00abd578 | `CONDITIONAL_JUMP`
<a id="insn-00abd328"></a> `00abd328` | `ea 03 13 aa` | mov x10,x19 | `FALL_THROUGH`
<a id="insn-00abd32c"></a> `00abd32c` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abd330"></a> `00abd330` | `48 a5 c0 a9` | ldp x8,x9,[x10, #0x8]! | `FALL_THROUGH`
<a id="insn-00abd334"></a> `00abd334` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd338"></a> `00abd338` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abd33c"></a> `00abd33c` | `80 12 00 54` | b.eq 0x00abd58c | `CONDITIONAL_JUMP`
<a id="insn-00abd340"></a> `00abd340` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00abd344"></a> `00abd344` | `1c 00 f8 92` | mov x28,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00abd348"></a> `00abd348` | `ea 5b 00 a9` | stp x10,x22,[sp] | `FALL_THROUGH`
<a id="insn-00abd34c"></a> `00abd34c` | `08 00 00 14` | b 0x00abd36c | `UNCONDITIONAL_JUMP`
<a id="insn-00abd350"></a> `00abd350` | `20 47 00 b8` | str w0,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00abd354"></a> `00abd354` | `b9 02 1f f8` | stur x25,[x21, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd358"></a> `00abd358` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00abd35c"></a> `00abd35c` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abd360"></a> `00abd360` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abd364"></a> `00abd364` | `5f 0b 89 eb` | cmp x26,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abd368"></a> `00abd368` | `a2 09 00 54` | b.cs 0x00abd49c | `CONDITIONAL_JUMP`
<a id="insn-00abd36c"></a> `00abd36c` | `08 79 7a b8` | ldr w8,[x8, x26, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abd370"></a> `00abd370` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd374"></a> `00abd374` | `28 03 f8 37` | tbnz w8,#0x1f,0x00abd3d8 | `CONDITIONAL_JUMP`
<a id="insn-00abd378"></a> `00abd378` | `a8 03 5f f8` | ldur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd37c"></a> `00abd37c` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd380"></a> `00abd380` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd384"></a> `00abd384` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00abd388"></a> `00abd388` | `42 01 00 54` | b.cs 0x00abd3b0 | `CONDITIONAL_JUMP`
<a id="insn-00abd38c"></a> `00abd38c` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00abd390"></a> `00abd390` | `bf 0a 00 f9` | str xzr,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00abd394"></a> `00abd394` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd398"></a> `00abd398` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00abd39c"></a> `00abd39c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd3a0"></a> `00abd3a0` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00abd3a4"></a> `00abd3a4` | `b5 62 00 91` | add x21,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00abd3a8"></a> `00abd3a8` | `b5 83 1e f8` | stur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd3ac"></a> `00abd3ac` | `0b 00 00 14` | b 0x00abd3d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd3b0"></a> `00abd3b0` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abd3b4"></a> `00abd3b4` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00abd3b8"></a> `00abd3b8` | `46 62 ed 97` | bl 0x00615cd0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd3bc"></a> `00abd3bc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abd3c0"></a> `00abd3c0` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd3c4"></a> `00abd3c4` | `b5 83 1e f8` | stur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd3c8"></a> `00abd3c8` | `80 00 00 b4` | cbz x0,0x00abd3d8 | `CONDITIONAL_JUMP`
<a id="insn-00abd3cc"></a> `00abd3cc` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abd3d0"></a> `00abd3d0` | `b8 6a 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd3d4"></a> `00abd3d4` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd3d8"></a> `00abd3d8` | `a8 03 5e f8` | ldur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abd3dc"></a> `00abd3dc` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00abd3e0"></a> `00abd3e0` | `a0 12 00 54` | b.eq 0x00abd634 | `CONDITIONAL_JUMP`
<a id="insn-00abd3e4"></a> `00abd3e4` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abd3e8"></a> `00abd3e8` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abd3ec"></a> `00abd3ec` | `5f 0b 89 eb` | cmp x26,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abd3f0"></a> `00abd3f0` | `42 11 00 54` | b.cs 0x00abd618 | `CONDITIONAL_JUMP`
<a id="insn-00abd3f4"></a> `00abd3f4` | `00 79 7a b8` | ldr w0,[x8, x26, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abd3f8"></a> `00abd3f8` | `94 c1 e6 97` | bl 0x0046da48 | `UNCONDITIONAL_CALL`
<a id="insn-00abd3fc"></a> `00abd3fc` | `b9 26 7f a9` | ldp x25,x9,[x21, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd400"></a> `00abd400` | `3f 03 09 eb` | cmp x25,x9 | `FALL_THROUGH`
<a id="insn-00abd404"></a> `00abd404` | `63 fa ff 54` | b.cc 0x00abd350 | `CONDITIONAL_JUMP`
<a id="insn-00abd408"></a> `00abd408` | `a8 62 00 d1` | sub x8,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00abd40c"></a> `00abd40c` | `16 01 40 f9` | ldr x22,[x8] | `FALL_THROUGH`
<a id="insn-00abd410"></a> `00abd410` | `37 03 16 cb` | sub x23,x25,x22 | `FALL_THROUGH`
<a id="insn-00abd414"></a> `00abd414` | `f9 fe 42 93` | asr x25,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00abd418"></a> `00abd418` | `2a 07 00 91` | add x10,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abd41c"></a> `00abd41c` | `4b fd 7e d3` | lsr x11,x10,#0x3e | `FALL_THROUGH`
<a id="insn-00abd420"></a> `00abd420` | `6b 12 00 b5` | cbnz x11,0x00abd66c | `CONDITIONAL_JUMP`
<a id="insn-00abd424"></a> `00abd424` | `28 01 16 cb` | sub x8,x9,x22 | `FALL_THROUGH`
<a id="insn-00abd428"></a> `00abd428` | `09 fd 41 93` | asr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abd42c"></a> `00abd42c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00abd430"></a> `00abd430` | `29 81 8a 9a` | csel x9,x9,x10,hi | `FALL_THROUGH`
<a id="insn-00abd434"></a> `00abd434` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00abd438"></a> `00abd438` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00abd43c"></a> `00abd43c` | `34 31 9c 9a` | csel x20,x9,x28,cc | `FALL_THROUGH`
<a id="insn-00abd440"></a> `00abd440` | `34 01 00 b4` | cbz x20,0x00abd464 | `CONDITIONAL_JUMP`
<a id="insn-00abd444"></a> `00abd444` | `88 fe 7e d3` | lsr x8,x20,#0x3e | `FALL_THROUGH`
<a id="insn-00abd448"></a> `00abd448` | `08 12 00 b5` | cbnz x8,0x00abd688 | `CONDITIONAL_JUMP`
<a id="insn-00abd44c"></a> `00abd44c` | `fb 03 00 2a` | mov w27,w0 | `FALL_THROUGH`
<a id="insn-00abd450"></a> `00abd450` | `80 f6 7e d3` | lsl x0,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00abd454"></a> `00abd454` | `8f 6a 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00abd458"></a> `00abd458` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00abd45c"></a> `00abd45c` | `e0 03 1b 2a` | mov w0,w27 | `FALL_THROUGH`
<a id="insn-00abd460"></a> `00abd460` | `02 00 00 14` | b 0x00abd468 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd464"></a> `00abd464` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00abd468"></a> `00abd468` | `19 0b 19 8b` | add x25,x24,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abd46c"></a> `00abd46c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00abd470"></a> `00abd470` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00abd474"></a> `00abd474` | `14 0b 14 8b` | add x20,x24,x20, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00abd478"></a> `00abd478` | `20 47 00 b8` | str w0,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00abd47c"></a> `00abd47c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00abd480"></a> `00abd480` | `e0 6a 06 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00abd484"></a> `00abd484` | `b8 e6 3e a9` | stp x24,x25,[x21, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd488"></a> `00abd488` | `b4 82 1f f8` | stur x20,[x21, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd48c"></a> `00abd48c` | `56 f6 ff b4` | cbz x22,0x00abd354 | `CONDITIONAL_JUMP`
<a id="insn-00abd490"></a> `00abd490` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00abd494"></a> `00abd494` | `87 6a 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd498"></a> `00abd498` | `af ff ff 17` | b 0x00abd354 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd49c"></a> `00abd49c` | `b4 03 7e a9` | ldp x20,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abd4a0"></a> `00abd4a0` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00abd4a4"></a> `00abd4a4` | `80 07 00 54` | b.eq 0x00abd594 | `CONDITIONAL_JUMP`
<a id="insn-00abd4a8"></a> `00abd4a8` | `f7 f3 01 b2` | orr x23,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abd4ac"></a> `00abd4ac` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00abd4b0"></a> `00abd4b0` | `18 03 80 52` | mov w24,#0x18 | `FALL_THROUGH`
<a id="insn-00abd4b4"></a> `00abd4b4` | `77 55 95 f2` | movk x23,#0xaaab | `FALL_THROUGH`
<a id="insn-00abd4b8"></a> `00abd4b8` | `08 00 14 cb` | sub x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00abd4bc"></a> `00abd4bc` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00abd4c0"></a> `00abd4c0` | `08 7d 17 9b` | mul x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00abd4c4"></a> `00abd4c4` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00abd4c8"></a> `00abd4c8` | `49 0c 00 54` | b.ls 0x00abd650 | `CONDITIONAL_JUMP`
<a id="insn-00abd4cc"></a> `00abd4cc` | `c8 52 18 9b` | madd x8,x22,x24,x20 | `FALL_THROUGH`
<a id="insn-00abd4d0"></a> `00abd4d0` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abd4d4"></a> `00abd4d4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00abd4d8"></a> `00abd4d8` | `40 05 00 54` | b.eq 0x00abd580 | `CONDITIONAL_JUMP`
<a id="insn-00abd4dc"></a> `00abd4dc` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00abd4e0"></a> `00abd4e0` | `15 79 7a b8` | ldr w21,[x8, x26, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abd4e4"></a> `00abd4e4` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abd4e8"></a> `00abd4e8` | `a4 0b f5 97` | bl 0x00800378 | `UNCONDITIONAL_CALL`
<a id="insn-00abd4ec"></a> `00abd4ec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abd4f0"></a> `00abd4f0` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abd4f4"></a> `00abd4f4` | `4e 0c f5 97` | bl 0x0080062c | `UNCONDITIONAL_CALL`
<a id="insn-00abd4f8"></a> `00abd4f8` | `62 3e 40 b9` | ldr w2,[x19, #0x3c] | `FALL_THROUGH`
<a id="insn-00abd4fc"></a> `00abd4fc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00abd500"></a> `00abd500` | `5f 04 00 31` | cmn w2,#0x1 | `FALL_THROUGH`
<a id="insn-00abd504"></a> `00abd504` | `a1 00 00 54` | b.ne 0x00abd518 | `CONDITIONAL_JUMP`
<a id="insn-00abd508"></a> `00abd508` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00abd50c"></a> `00abd50c` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00abd510"></a> `00abd510` | `77 20 f5 97` | bl 0x008056ec | `UNCONDITIONAL_CALL`
<a id="insn-00abd514"></a> `00abd514` | `02 04 00 51` | sub w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abd518"></a> `00abd518` | `63 42 40 b9` | ldr w3,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00abd51c"></a> `00abd51c` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00abd520"></a> `00abd520` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00abd524"></a> `00abd524` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abd528"></a> `00abd528` | `31 a2 fe 97` | bl 0x00a65dec | `UNCONDITIONAL_CALL`
<a id="insn-00abd52c"></a> `00abd52c` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-00abd530"></a> `00abd530` | `b4 03 7e a9` | ldp x20,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abd534"></a> `00abd534` | `09 00 14 cb` | sub x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00abd538"></a> `00abd538` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00abd53c"></a> `00abd53c` | `29 7d 17 9b` | mul x9,x9,x23 | `FALL_THROUGH`
<a id="insn-00abd540"></a> `00abd540` | `48 01 00 35` | cbnz w8,0x00abd568 | `CONDITIONAL_JUMP`
<a id="insn-00abd544"></a> `00abd544` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00abd548"></a> `00abd548` | `49 08 00 54` | b.ls 0x00abd650 | `CONDITIONAL_JUMP`
<a id="insn-00abd54c"></a> `00abd54c` | `c8 52 18 9b` | madd x8,x22,x24,x20 | `FALL_THROUGH`
<a id="insn-00abd550"></a> `00abd550` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00abd554"></a> `00abd554` | `08 25 40 a9` | ldp x8,x9,[x8] | `FALL_THROUGH`
<a id="insn-00abd558"></a> `00abd558` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00abd55c"></a> `00abd55c` | `5f 0b 89 eb` | cmp x26,x9, ASR #0x2 | `FALL_THROUGH`
<a id="insn-00abd560"></a> `00abd560` | `03 fc ff 54` | b.cc 0x00abd4e0 | `CONDITIONAL_JUMP`
<a id="insn-00abd564"></a> `00abd564` | `07 00 00 14` | b 0x00abd580 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd568"></a> `00abd568` | `d6 06 00 91` | add x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00abd56c"></a> `00abd56c` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00abd570"></a> `00abd570` | `48 fa ff 54` | b.hi 0x00abd4b8 | `CONDITIONAL_JUMP`
<a id="insn-00abd574"></a> `00abd574` | `09 00 00 14` | b 0x00abd598 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd578"></a> `00abd578` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00abd57c"></a> `00abd57c` | `1a 00 00 14` | b 0x00abd5e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd580"></a> `00abd580` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd584"></a> `00abd584` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00abd588"></a> `00abd588` | `07 00 00 14` | b 0x00abd5a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd58c"></a> `00abd58c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00abd590"></a> `00abd590` | `15 00 00 14` | b 0x00abd5e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd594"></a> `00abd594` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abd598"></a> `00abd598` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd59c"></a> `00abd59c` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00abd5a0"></a> `00abd5a0` | `34 02 00 b4` | cbz x20,0x00abd5e4 | `CONDITIONAL_JUMP`
<a id="insn-00abd5a4"></a> `00abd5a4` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00abd5a8"></a> `00abd5a8` | `a0 01 00 54` | b.eq 0x00abd5dc | `CONDITIONAL_JUMP`
<a id="insn-00abd5ac"></a> `00abd5ac` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abd5b0"></a> `00abd5b0` | `04 00 00 14` | b 0x00abd5c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd5b4"></a> `00abd5b4` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00abd5b8"></a> `00abd5b8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abd5bc"></a> `00abd5bc` | `e0 00 00 54` | b.eq 0x00abd5d8 | `CONDITIONAL_JUMP`
<a id="insn-00abd5c0"></a> `00abd5c0` | `a8 8e 5e f8` | ldr x8,[x21, #-0x18]! | `FALL_THROUGH`
<a id="insn-00abd5c4"></a> `00abd5c4` | `88 ff ff b4` | cbz x8,0x00abd5b4 | `CONDITIONAL_JUMP`
<a id="insn-00abd5c8"></a> `00abd5c8` | `08 00 1f f8` | stur x8,[x0, #-0x10] | `FALL_THROUGH`
<a id="insn-00abd5cc"></a> `00abd5cc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00abd5d0"></a> `00abd5d0` | `38 6a 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd5d4"></a> `00abd5d4` | `f8 ff ff 17` | b 0x00abd5b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abd5d8"></a> `00abd5d8` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00abd5dc"></a> `00abd5dc` | `b4 83 1e f8` | stur x20,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00abd5e0"></a> `00abd5e0` | `34 6a 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00abd5e4"></a> `00abd5e4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00abd5e8"></a> `00abd5e8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd5ec"></a> `00abd5ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abd5f0"></a> `00abd5f0` | `21 08 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd5f4"></a> `00abd5f4` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00abd5f8"></a> `00abd5f8` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00abd5fc"></a> `00abd5fc` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abd600"></a> `00abd600` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abd604"></a> `00abd604` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abd608"></a> `00abd608` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abd60c"></a> `00abd60c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abd610"></a> `00abd610` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00abd614"></a> `00abd614` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abd618"></a> `00abd618` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd61c"></a> `00abd61c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abd620"></a> `00abd620` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd624"></a> `00abd624` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abd628"></a> `00abd628` | `61 06 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd62c"></a> `00abd62c` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00abd630"></a> `00abd630` | `70 87 e7 97` | bl 0x0049f3f0 | `CALL_TERMINATOR`
<a id="insn-00abd634"></a> `00abd634` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd638"></a> `00abd638` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abd63c"></a> `00abd63c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd640"></a> `00abd640` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abd644"></a> `00abd644` | `81 05 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd648"></a> `00abd648` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abd64c"></a> `00abd64c` | `5f 37 f5 97` | bl 0x0080b3c8 | `UNCONDITIONAL_CALL`
<a id="insn-00abd650"></a> `00abd650` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd654"></a> `00abd654` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abd658"></a> `00abd658` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd65c"></a> `00abd65c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abd660"></a> `00abd660` | `a1 04 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd664"></a> `00abd664` | `a0 83 00 d1` | sub x0,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00abd668"></a> `00abd668` | `58 37 f5 97` | bl 0x0080b3c8 | `UNCONDITIONAL_CALL`
<a id="insn-00abd66c"></a> `00abd66c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd670"></a> `00abd670` | `29 15 40 f9` | ldr x9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abd674"></a> `00abd674` | `aa 83 5f f8` | ldur x10,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd678"></a> `00abd678` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00abd67c"></a> `00abd67c` | `c1 03 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd680"></a> `00abd680` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00abd684"></a> `00abd684` | `6f cc e6 97` | bl 0x00470840 | `CALL_TERMINATOR`
<a id="insn-00abd688"></a> `00abd688` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abd68c"></a> `00abd68c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00abd690"></a> `00abd690` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abd694"></a> `00abd694` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abd698"></a> `00abd698` | `e1 02 00 54` | b.ne 0x00abd6f4 | `CONDITIONAL_JUMP`
<a id="insn-00abd69c"></a> `00abd69c` | `09 0e e6 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-00abd6f4"></a> `00abd6f4` | `fb 69 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abd2dc`](#insn-00abd2dc) 範囲 `[['00abd2dc', '00abd317']]`
  - `CONDITIONAL_JUMP` [`00abd314`](#insn-00abd314) → [`00abd328`](#insn-00abd328)
  - `FALL_THROUGH` [`00abd314`](#insn-00abd314) → [`00abd318`](#insn-00abd318)
- ブロック [`00abd318`](#insn-00abd318) 範囲 `[['00abd318', '00abd327']]`
  - `CONDITIONAL_JUMP` [`00abd324`](#insn-00abd324) → [`00abd578`](#insn-00abd578)
  - `FALL_THROUGH` [`00abd324`](#insn-00abd324) → [`00abd328`](#insn-00abd328)
- ブロック [`00abd328`](#insn-00abd328) 範囲 `[['00abd328', '00abd33f']]`
  - `CONDITIONAL_JUMP` [`00abd33c`](#insn-00abd33c) → [`00abd58c`](#insn-00abd58c)
  - `FALL_THROUGH` [`00abd33c`](#insn-00abd33c) → [`00abd340`](#insn-00abd340)
- ブロック [`00abd340`](#insn-00abd340) 範囲 `[['00abd340', '00abd34f']]`
  - `UNCONDITIONAL_JUMP` [`00abd34c`](#insn-00abd34c) → [`00abd36c`](#insn-00abd36c)
- ブロック [`00abd350`](#insn-00abd350) 範囲 `[['00abd350', '00abd353']]`
  - `FALL_THROUGH` [`00abd350`](#insn-00abd350) → [`00abd354`](#insn-00abd354)
- ブロック [`00abd354`](#insn-00abd354) 範囲 `[['00abd354', '00abd36b']]`
  - `CONDITIONAL_JUMP` [`00abd368`](#insn-00abd368) → [`00abd49c`](#insn-00abd49c)
  - `FALL_THROUGH` [`00abd368`](#insn-00abd368) → [`00abd36c`](#insn-00abd36c)
- ブロック [`00abd36c`](#insn-00abd36c) 範囲 `[['00abd36c', '00abd377']]`
  - `CONDITIONAL_JUMP` [`00abd374`](#insn-00abd374) → [`00abd3d8`](#insn-00abd3d8)
  - `FALL_THROUGH` [`00abd374`](#insn-00abd374) → [`00abd378`](#insn-00abd378)
- ブロック [`00abd378`](#insn-00abd378) 範囲 `[['00abd378', '00abd38b']]`
  - `CONDITIONAL_JUMP` [`00abd388`](#insn-00abd388) → [`00abd3b0`](#insn-00abd3b0)
  - `FALL_THROUGH` [`00abd388`](#insn-00abd388) → [`00abd38c`](#insn-00abd38c)
- ブロック [`00abd38c`](#insn-00abd38c) 範囲 `[['00abd38c', '00abd3af']]`
  - `UNCONDITIONAL_JUMP` [`00abd3ac`](#insn-00abd3ac) → [`00abd3d8`](#insn-00abd3d8)
- ブロック [`00abd3b0`](#insn-00abd3b0) 範囲 `[['00abd3b0', '00abd3cb']]`
  - `CONDITIONAL_JUMP` [`00abd3c8`](#insn-00abd3c8) → [`00abd3d8`](#insn-00abd3d8)
  - `FALL_THROUGH` [`00abd3c8`](#insn-00abd3c8) → [`00abd3cc`](#insn-00abd3cc)
- ブロック [`00abd3cc`](#insn-00abd3cc) 範囲 `[['00abd3cc', '00abd3d7']]`
  - `FALL_THROUGH` [`00abd3d4`](#insn-00abd3d4) → [`00abd3d8`](#insn-00abd3d8)
- ブロック [`00abd3d8`](#insn-00abd3d8) 範囲 `[['00abd3d8', '00abd3e3']]`
  - `CONDITIONAL_JUMP` [`00abd3e0`](#insn-00abd3e0) → [`00abd634`](#insn-00abd634)
  - `FALL_THROUGH` [`00abd3e0`](#insn-00abd3e0) → [`00abd3e4`](#insn-00abd3e4)
- ブロック [`00abd3e4`](#insn-00abd3e4) 範囲 `[['00abd3e4', '00abd3f3']]`
  - `CONDITIONAL_JUMP` [`00abd3f0`](#insn-00abd3f0) → [`00abd618`](#insn-00abd618)
  - `FALL_THROUGH` [`00abd3f0`](#insn-00abd3f0) → [`00abd3f4`](#insn-00abd3f4)
- ブロック [`00abd3f4`](#insn-00abd3f4) 範囲 `[['00abd3f4', '00abd407']]`
  - `CONDITIONAL_JUMP` [`00abd404`](#insn-00abd404) → [`00abd350`](#insn-00abd350)
  - `FALL_THROUGH` [`00abd404`](#insn-00abd404) → [`00abd408`](#insn-00abd408)
- ブロック [`00abd408`](#insn-00abd408) 範囲 `[['00abd408', '00abd423']]`
  - `CONDITIONAL_JUMP` [`00abd420`](#insn-00abd420) → [`00abd66c`](#insn-00abd66c)
  - `FALL_THROUGH` [`00abd420`](#insn-00abd420) → [`00abd424`](#insn-00abd424)
- ブロック [`00abd424`](#insn-00abd424) 範囲 `[['00abd424', '00abd443']]`
  - `CONDITIONAL_JUMP` [`00abd440`](#insn-00abd440) → [`00abd464`](#insn-00abd464)
  - `FALL_THROUGH` [`00abd440`](#insn-00abd440) → [`00abd444`](#insn-00abd444)
- ブロック [`00abd444`](#insn-00abd444) 範囲 `[['00abd444', '00abd44b']]`
  - `CONDITIONAL_JUMP` [`00abd448`](#insn-00abd448) → [`00abd688`](#insn-00abd688)
  - `FALL_THROUGH` [`00abd448`](#insn-00abd448) → [`00abd44c`](#insn-00abd44c)
- ブロック [`00abd44c`](#insn-00abd44c) 範囲 `[['00abd44c', '00abd45b']]`
  - `FALL_THROUGH` [`00abd458`](#insn-00abd458) → [`00abd45c`](#insn-00abd45c)
- ブロック [`00abd45c`](#insn-00abd45c) 範囲 `[['00abd45c', '00abd463']]`
  - `UNCONDITIONAL_JUMP` [`00abd460`](#insn-00abd460) → [`00abd468`](#insn-00abd468)
- ブロック [`00abd464`](#insn-00abd464) 範囲 `[['00abd464', '00abd467']]`
  - `FALL_THROUGH` [`00abd464`](#insn-00abd464) → [`00abd468`](#insn-00abd468)
- ブロック [`00abd468`](#insn-00abd468) 範囲 `[['00abd468', '00abd48f']]`
  - `CONDITIONAL_JUMP` [`00abd48c`](#insn-00abd48c) → [`00abd354`](#insn-00abd354)
  - `FALL_THROUGH` [`00abd48c`](#insn-00abd48c) → [`00abd490`](#insn-00abd490)
- ブロック [`00abd490`](#insn-00abd490) 範囲 `[['00abd490', '00abd49b']]`
  - `UNCONDITIONAL_JUMP` [`00abd498`](#insn-00abd498) → [`00abd354`](#insn-00abd354)
- ブロック [`00abd49c`](#insn-00abd49c) 範囲 `[['00abd49c', '00abd4a7']]`
  - `CONDITIONAL_JUMP` [`00abd4a4`](#insn-00abd4a4) → [`00abd594`](#insn-00abd594)
  - `FALL_THROUGH` [`00abd4a4`](#insn-00abd4a4) → [`00abd4a8`](#insn-00abd4a8)
- ブロック [`00abd4a8`](#insn-00abd4a8) 範囲 `[['00abd4a8', '00abd4b7']]`
  - `FALL_THROUGH` [`00abd4b4`](#insn-00abd4b4) → [`00abd4b8`](#insn-00abd4b8)
- ブロック [`00abd4b8`](#insn-00abd4b8) 範囲 `[['00abd4b8', '00abd4cb']]`
  - `CONDITIONAL_JUMP` [`00abd4c8`](#insn-00abd4c8) → [`00abd650`](#insn-00abd650)
  - `FALL_THROUGH` [`00abd4c8`](#insn-00abd4c8) → [`00abd4cc`](#insn-00abd4cc)
- ブロック [`00abd4cc`](#insn-00abd4cc) 範囲 `[['00abd4cc', '00abd4db']]`
  - `CONDITIONAL_JUMP` [`00abd4d8`](#insn-00abd4d8) → [`00abd580`](#insn-00abd580)
  - `FALL_THROUGH` [`00abd4d8`](#insn-00abd4d8) → [`00abd4dc`](#insn-00abd4dc)
- ブロック [`00abd4dc`](#insn-00abd4dc) 範囲 `[['00abd4dc', '00abd4df']]`
  - `FALL_THROUGH` [`00abd4dc`](#insn-00abd4dc) → [`00abd4e0`](#insn-00abd4e0)
- ブロック [`00abd4e0`](#insn-00abd4e0) 範囲 `[['00abd4e0', '00abd507']]`
  - `CONDITIONAL_JUMP` [`00abd504`](#insn-00abd504) → [`00abd518`](#insn-00abd518)
  - `FALL_THROUGH` [`00abd504`](#insn-00abd504) → [`00abd508`](#insn-00abd508)
- ブロック [`00abd508`](#insn-00abd508) 範囲 `[['00abd508', '00abd517']]`
  - `FALL_THROUGH` [`00abd514`](#insn-00abd514) → [`00abd518`](#insn-00abd518)
- ブロック [`00abd518`](#insn-00abd518) 範囲 `[['00abd518', '00abd543']]`
  - `CONDITIONAL_JUMP` [`00abd540`](#insn-00abd540) → [`00abd568`](#insn-00abd568)
  - `FALL_THROUGH` [`00abd540`](#insn-00abd540) → [`00abd544`](#insn-00abd544)
- ブロック [`00abd544`](#insn-00abd544) 範囲 `[['00abd544', '00abd54b']]`
  - `CONDITIONAL_JUMP` [`00abd548`](#insn-00abd548) → [`00abd650`](#insn-00abd650)
  - `FALL_THROUGH` [`00abd548`](#insn-00abd548) → [`00abd54c`](#insn-00abd54c)
- ブロック [`00abd54c`](#insn-00abd54c) 範囲 `[['00abd54c', '00abd563']]`
  - `CONDITIONAL_JUMP` [`00abd560`](#insn-00abd560) → [`00abd4e0`](#insn-00abd4e0)
  - `FALL_THROUGH` [`00abd560`](#insn-00abd560) → [`00abd564`](#insn-00abd564)
- ブロック [`00abd564`](#insn-00abd564) 範囲 `[['00abd564', '00abd567']]`
  - `UNCONDITIONAL_JUMP` [`00abd564`](#insn-00abd564) → [`00abd580`](#insn-00abd580)
- ブロック [`00abd568`](#insn-00abd568) 範囲 `[['00abd568', '00abd573']]`
  - `CONDITIONAL_JUMP` [`00abd570`](#insn-00abd570) → [`00abd4b8`](#insn-00abd4b8)
  - `FALL_THROUGH` [`00abd570`](#insn-00abd570) → [`00abd574`](#insn-00abd574)
- ブロック [`00abd574`](#insn-00abd574) 範囲 `[['00abd574', '00abd577']]`
  - `UNCONDITIONAL_JUMP` [`00abd574`](#insn-00abd574) → [`00abd598`](#insn-00abd598)
- ブロック [`00abd578`](#insn-00abd578) 範囲 `[['00abd578', '00abd57f']]`
  - `UNCONDITIONAL_JUMP` [`00abd57c`](#insn-00abd57c) → [`00abd5e4`](#insn-00abd5e4)
- ブロック [`00abd580`](#insn-00abd580) 範囲 `[['00abd580', '00abd58b']]`
  - `UNCONDITIONAL_JUMP` [`00abd588`](#insn-00abd588) → [`00abd5a4`](#insn-00abd5a4)
- ブロック [`00abd58c`](#insn-00abd58c) 範囲 `[['00abd58c', '00abd593']]`
  - `UNCONDITIONAL_JUMP` [`00abd590`](#insn-00abd590) → [`00abd5e4`](#insn-00abd5e4)
- ブロック [`00abd594`](#insn-00abd594) 範囲 `[['00abd594', '00abd597']]`
  - `FALL_THROUGH` [`00abd594`](#insn-00abd594) → [`00abd598`](#insn-00abd598)
- ブロック [`00abd598`](#insn-00abd598) 範囲 `[['00abd598', '00abd5a3']]`
  - `CONDITIONAL_JUMP` [`00abd5a0`](#insn-00abd5a0) → [`00abd5e4`](#insn-00abd5e4)
  - `FALL_THROUGH` [`00abd5a0`](#insn-00abd5a0) → [`00abd5a4`](#insn-00abd5a4)
- ブロック [`00abd5a4`](#insn-00abd5a4) 範囲 `[['00abd5a4', '00abd5ab']]`
  - `CONDITIONAL_JUMP` [`00abd5a8`](#insn-00abd5a8) → [`00abd5dc`](#insn-00abd5dc)
  - `FALL_THROUGH` [`00abd5a8`](#insn-00abd5a8) → [`00abd5ac`](#insn-00abd5ac)
- ブロック [`00abd5ac`](#insn-00abd5ac) 範囲 `[['00abd5ac', '00abd5b3']]`
  - `UNCONDITIONAL_JUMP` [`00abd5b0`](#insn-00abd5b0) → [`00abd5c0`](#insn-00abd5c0)
- ブロック [`00abd5b4`](#insn-00abd5b4) 範囲 `[['00abd5b4', '00abd5bf']]`
  - `CONDITIONAL_JUMP` [`00abd5bc`](#insn-00abd5bc) → [`00abd5d8`](#insn-00abd5d8)
  - `FALL_THROUGH` [`00abd5bc`](#insn-00abd5bc) → [`00abd5c0`](#insn-00abd5c0)
- ブロック [`00abd5c0`](#insn-00abd5c0) 範囲 `[['00abd5c0', '00abd5c7']]`
  - `CONDITIONAL_JUMP` [`00abd5c4`](#insn-00abd5c4) → [`00abd5b4`](#insn-00abd5b4)
  - `FALL_THROUGH` [`00abd5c4`](#insn-00abd5c4) → [`00abd5c8`](#insn-00abd5c8)
- ブロック [`00abd5c8`](#insn-00abd5c8) 範囲 `[['00abd5c8', '00abd5d7']]`
  - `UNCONDITIONAL_JUMP` [`00abd5d4`](#insn-00abd5d4) → [`00abd5b4`](#insn-00abd5b4)
- ブロック [`00abd5d8`](#insn-00abd5d8) 範囲 `[['00abd5d8', '00abd5db']]`
  - `FALL_THROUGH` [`00abd5d8`](#insn-00abd5d8) → [`00abd5dc`](#insn-00abd5dc)
- ブロック [`00abd5dc`](#insn-00abd5dc) 範囲 `[['00abd5dc', '00abd5e3']]`
  - `FALL_THROUGH` [`00abd5e0`](#insn-00abd5e0) → [`00abd5e4`](#insn-00abd5e4)
- ブロック [`00abd5e4`](#insn-00abd5e4) 範囲 `[['00abd5e4', '00abd5f3']]`
  - `CONDITIONAL_JUMP` [`00abd5f0`](#insn-00abd5f0) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd5f0`](#insn-00abd5f0) → [`00abd5f4`](#insn-00abd5f4)
- ブロック [`00abd5f4`](#insn-00abd5f4) 範囲 `[['00abd5f4', '00abd603']]`
  - `FALL_THROUGH` [`00abd600`](#insn-00abd600) → [`00abd604`](#insn-00abd604)
- ブロック [`00abd604`](#insn-00abd604) 範囲 `[['00abd604', '00abd617']]`
- ブロック [`00abd618`](#insn-00abd618) 範囲 `[['00abd618', '00abd62b']]`
  - `CONDITIONAL_JUMP` [`00abd628`](#insn-00abd628) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd628`](#insn-00abd628) → [`00abd62c`](#insn-00abd62c)
- ブロック [`00abd62c`](#insn-00abd62c) 範囲 `[['00abd62c', '00abd633']]`
- ブロック [`00abd634`](#insn-00abd634) 範囲 `[['00abd634', '00abd647']]`
  - `CONDITIONAL_JUMP` [`00abd644`](#insn-00abd644) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd644`](#insn-00abd644) → [`00abd648`](#insn-00abd648)
- ブロック [`00abd648`](#insn-00abd648) 範囲 `[['00abd648', '00abd64f']]`
  - `FALL_THROUGH` [`00abd64c`](#insn-00abd64c) → [`00abd650`](#insn-00abd650)
- ブロック [`00abd650`](#insn-00abd650) 範囲 `[['00abd650', '00abd663']]`
  - `CONDITIONAL_JUMP` [`00abd660`](#insn-00abd660) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd660`](#insn-00abd660) → [`00abd664`](#insn-00abd664)
- ブロック [`00abd664`](#insn-00abd664) 範囲 `[['00abd664', '00abd66b']]`
  - `FALL_THROUGH` [`00abd668`](#insn-00abd668) → [`00abd66c`](#insn-00abd66c)
- ブロック [`00abd66c`](#insn-00abd66c) 範囲 `[['00abd66c', '00abd67f']]`
  - `CONDITIONAL_JUMP` [`00abd67c`](#insn-00abd67c) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd67c`](#insn-00abd67c) → [`00abd680`](#insn-00abd680)
- ブロック [`00abd680`](#insn-00abd680) 範囲 `[['00abd680', '00abd687']]`
- ブロック [`00abd688`](#insn-00abd688) 範囲 `[['00abd688', '00abd69b']]`
  - `CONDITIONAL_JUMP` [`00abd698`](#insn-00abd698) → [`00abd6f4`](#insn-00abd6f4)
  - `FALL_THROUGH` [`00abd698`](#insn-00abd698) → [`00abd69c`](#insn-00abd69c)
- ブロック [`00abd69c`](#insn-00abd69c) 範囲 `[['00abd69c', '00abd69f']]`
- ブロック [`00abd6f4`](#insn-00abd6f4) 範囲 `[['00abd6f4', '00abd6f7']]`

## 命令位置別の参照

- [`00abd2e0`](#insn-00abd2e0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd2e4`](#insn-00abd2e4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd2e8`](#insn-00abd2e8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd2ec`](#insn-00abd2ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd2f0`](#insn-00abd2f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd2f4`](#insn-00abd2f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd308`](#insn-00abd308) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd314`](#insn-00abd314) → [`00abd328`](#insn-00abd328) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd318`](#insn-00abd318) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abd320`](#insn-00abd320) → [`00860588`](../00860/00860588.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00860588` · 推定シンボル `None` · 推定型 `None`
- [`00abd324`](#insn-00abd324) → [`00abd578`](#insn-00abd578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd32c`](#insn-00abd32c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd334`](#insn-00abd334) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd33c`](#insn-00abd33c) → [`00abd58c`](#insn-00abd58c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd348`](#insn-00abd348) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd34c`](#insn-00abd34c) → [`00abd36c`](#insn-00abd36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd368`](#insn-00abd368) → [`00abd49c`](#insn-00abd49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd370`](#insn-00abd370) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd374`](#insn-00abd374) → [`00abd3d8`](#insn-00abd3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd378`](#insn-00abd378) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd37c`](#insn-00abd37c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd380`](#insn-00abd380) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd388`](#insn-00abd388) → [`00abd3b0`](#insn-00abd3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd394`](#insn-00abd394) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd39c`](#insn-00abd39c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3a8`](#insn-00abd3a8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3ac`](#insn-00abd3ac) → [`00abd3d8`](#insn-00abd3d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3b8`](#insn-00abd3b8) → [`00615cd0`](../00615/00615cd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00615cd0` · 推定シンボル `None` · 推定型 `None`
- [`00abd3c0`](#insn-00abd3c0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3c4`](#insn-00abd3c4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3c8`](#insn-00abd3c8) → [`00abd3d8`](#insn-00abd3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3cc`](#insn-00abd3cc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3d0`](#insn-00abd3d0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd3d4`](#insn-00abd3d4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3d8`](#insn-00abd3d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3e0`](#insn-00abd3e0) → [`00abd634`](#insn-00abd634) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3f0`](#insn-00abd3f0) → [`00abd618`](#insn-00abd618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd3f8`](#insn-00abd3f8) → [`0046da48`](../0046d/0046da48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046da48` · 推定シンボル `None` · 推定型 `None`
- [`00abd404`](#insn-00abd404) → [`00abd350`](#insn-00abd350) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd420`](#insn-00abd420) → [`00abd66c`](#insn-00abd66c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd440`](#insn-00abd440) → [`00abd464`](#insn-00abd464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd448`](#insn-00abd448) → [`00abd688`](#insn-00abd688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd454`](#insn-00abd454) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00abd460`](#insn-00abd460) → [`00abd468`](#insn-00abd468) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd480`](#insn-00abd480) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00abd48c`](#insn-00abd48c) → [`00abd354`](#insn-00abd354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd494`](#insn-00abd494) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd498`](#insn-00abd498) → [`00abd354`](#insn-00abd354) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd49c`](#insn-00abd49c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd4a4`](#insn-00abd4a4) → [`00abd594`](#insn-00abd594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd4c8`](#insn-00abd4c8) → [`00abd650`](#insn-00abd650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd4d8`](#insn-00abd4d8) → [`00abd580`](#insn-00abd580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd4e8`](#insn-00abd4e8) → [`00800378`](../00800/00800378.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800378` · 推定シンボル `None` · 推定型 `None`
- [`00abd4f4`](#insn-00abd4f4) → [`0080062c`](../00800/0080062c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080062c` · 推定シンボル `None` · 推定型 `None`
- [`00abd504`](#insn-00abd504) → [`00abd518`](#insn-00abd518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd510`](#insn-00abd510) → [`008056ec`](../00805/008056ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008056ec` · 推定シンボル `None` · 推定型 `None`
- [`00abd528`](#insn-00abd528) → [`00a65dec`](../00a65/00a65dec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a65dec` · 推定シンボル `None` · 推定型 `None`
- [`00abd530`](#insn-00abd530) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd540`](#insn-00abd540) → [`00abd568`](#insn-00abd568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd548`](#insn-00abd548) → [`00abd650`](#insn-00abd650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd560`](#insn-00abd560) → [`00abd4e0`](#insn-00abd4e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd564`](#insn-00abd564) → [`00abd580`](#insn-00abd580) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd570`](#insn-00abd570) → [`00abd4b8`](#insn-00abd4b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd574`](#insn-00abd574) → [`00abd598`](#insn-00abd598) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd57c`](#insn-00abd57c) → [`00abd5e4`](#insn-00abd5e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd580`](#insn-00abd580) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd588`](#insn-00abd588) → [`00abd5a4`](#insn-00abd5a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd590`](#insn-00abd590) → [`00abd5e4`](#insn-00abd5e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd598`](#insn-00abd598) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5a0`](#insn-00abd5a0) → [`00abd5e4`](#insn-00abd5e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5a8`](#insn-00abd5a8) → [`00abd5dc`](#insn-00abd5dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5b0`](#insn-00abd5b0) → [`00abd5c0`](#insn-00abd5c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5bc`](#insn-00abd5bc) → [`00abd5d8`](#insn-00abd5d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5c4`](#insn-00abd5c4) → [`00abd5b4`](#insn-00abd5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5d0`](#insn-00abd5d0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd5d4`](#insn-00abd5d4) → [`00abd5b4`](#insn-00abd5b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5d8`](#insn-00abd5d8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5dc`](#insn-00abd5dc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5e0`](#insn-00abd5e0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00abd5e8`](#insn-00abd5e8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5f0`](#insn-00abd5f0) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5f8`](#insn-00abd5f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd5fc`](#insn-00abd5fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd600`](#insn-00abd600) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd604`](#insn-00abd604) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd608`](#insn-00abd608) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd60c`](#insn-00abd60c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd618`](#insn-00abd618) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd620`](#insn-00abd620) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd628`](#insn-00abd628) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd62c`](#insn-00abd62c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd630`](#insn-00abd630) → [`0049f3f0`](../0049f/0049f3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0049f3f0` · 推定シンボル `None` · 推定型 `None`
- [`00abd634`](#insn-00abd634) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd63c`](#insn-00abd63c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd644`](#insn-00abd644) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd64c`](#insn-00abd64c) → [`0080b3c8`](../0080b/0080b3c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080b3c8` · 推定シンボル `None` · 推定型 `None`
- [`00abd650`](#insn-00abd650) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd658`](#insn-00abd658) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd660`](#insn-00abd660) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd668`](#insn-00abd668) → [`0080b3c8`](../0080b/0080b3c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080b3c8` · 推定シンボル `None` · 推定型 `None`
- [`00abd66c`](#insn-00abd66c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd674`](#insn-00abd674) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd67c`](#insn-00abd67c) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd684`](#insn-00abd684) → [`00470840`](../00470/00470840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470840` · 推定シンボル `None` · 推定型 `None`
- [`00abd688`](#insn-00abd688) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd690`](#insn-00abd690) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd698`](#insn-00abd698) → [`00abd6f4`](#insn-00abd6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd69c`](#insn-00abd69c) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`00abd6f4`](#insn-00abd6f4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abd2e0`](#insn-00abd2e0)

~~~json
{
  "source": "00abd2e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd2e4`](#insn-00abd2e4)

~~~json
{
  "source": "00abd2e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd2e8`](#insn-00abd2e8)

~~~json
{
  "source": "00abd2e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd2ec`](#insn-00abd2ec)

~~~json
{
  "source": "00abd2ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd2f0`](#insn-00abd2f0)

~~~json
{
  "source": "00abd2f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd2f4`](#insn-00abd2f4)

~~~json
{
  "source": "00abd2f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd308`](#insn-00abd308)

~~~json
{
  "source": "00abd308",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd314`](#insn-00abd314)

~~~json
{
  "source": "00abd314",
  "target": "00abd328",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd318`](#insn-00abd318)

~~~json
{
  "source": "00abd318",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd320`](#insn-00abd320)

~~~json
{
  "source": "00abd320",
  "target": "00860588",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd324`](#insn-00abd324)

~~~json
{
  "source": "00abd324",
  "target": "00abd578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd32c`](#insn-00abd32c)

~~~json
{
  "source": "00abd32c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd334`](#insn-00abd334)

~~~json
{
  "source": "00abd334",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd33c`](#insn-00abd33c)

~~~json
{
  "source": "00abd33c",
  "target": "00abd58c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd348`](#insn-00abd348)

~~~json
{
  "source": "00abd348",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd34c`](#insn-00abd34c)

~~~json
{
  "source": "00abd34c",
  "target": "00abd36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd368`](#insn-00abd368)

~~~json
{
  "source": "00abd368",
  "target": "00abd49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd370`](#insn-00abd370)

~~~json
{
  "source": "00abd370",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd374`](#insn-00abd374)

~~~json
{
  "source": "00abd374",
  "target": "00abd3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd378`](#insn-00abd378)

~~~json
{
  "source": "00abd378",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd37c`](#insn-00abd37c)

~~~json
{
  "source": "00abd37c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd380`](#insn-00abd380)

~~~json
{
  "source": "00abd380",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd388`](#insn-00abd388)

~~~json
{
  "source": "00abd388",
  "target": "00abd3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd394`](#insn-00abd394)

~~~json
{
  "source": "00abd394",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd39c`](#insn-00abd39c)

~~~json
{
  "source": "00abd39c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3a8`](#insn-00abd3a8)

~~~json
{
  "source": "00abd3a8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3ac`](#insn-00abd3ac)

~~~json
{
  "source": "00abd3ac",
  "target": "00abd3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3b8`](#insn-00abd3b8)

~~~json
{
  "source": "00abd3b8",
  "target": "00615cd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd3c0`](#insn-00abd3c0)

~~~json
{
  "source": "00abd3c0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3c4`](#insn-00abd3c4)

~~~json
{
  "source": "00abd3c4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3c8`](#insn-00abd3c8)

~~~json
{
  "source": "00abd3c8",
  "target": "00abd3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3cc`](#insn-00abd3cc)

~~~json
{
  "source": "00abd3cc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3d0`](#insn-00abd3d0)

~~~json
{
  "source": "00abd3d0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd3d4`](#insn-00abd3d4)

~~~json
{
  "source": "00abd3d4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3d8`](#insn-00abd3d8)

~~~json
{
  "source": "00abd3d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3e0`](#insn-00abd3e0)

~~~json
{
  "source": "00abd3e0",
  "target": "00abd634",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3f0`](#insn-00abd3f0)

~~~json
{
  "source": "00abd3f0",
  "target": "00abd618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd3f8`](#insn-00abd3f8)

~~~json
{
  "source": "00abd3f8",
  "target": "0046da48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd404`](#insn-00abd404)

~~~json
{
  "source": "00abd404",
  "target": "00abd350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd420`](#insn-00abd420)

~~~json
{
  "source": "00abd420",
  "target": "00abd66c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd440`](#insn-00abd440)

~~~json
{
  "source": "00abd440",
  "target": "00abd464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd448`](#insn-00abd448)

~~~json
{
  "source": "00abd448",
  "target": "00abd688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd454`](#insn-00abd454)

~~~json
{
  "source": "00abd454",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd460`](#insn-00abd460)

~~~json
{
  "source": "00abd460",
  "target": "00abd468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd480`](#insn-00abd480)

~~~json
{
  "source": "00abd480",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd48c`](#insn-00abd48c)

~~~json
{
  "source": "00abd48c",
  "target": "00abd354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd494`](#insn-00abd494)

~~~json
{
  "source": "00abd494",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd498`](#insn-00abd498)

~~~json
{
  "source": "00abd498",
  "target": "00abd354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd49c`](#insn-00abd49c)

~~~json
{
  "source": "00abd49c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd4a4`](#insn-00abd4a4)

~~~json
{
  "source": "00abd4a4",
  "target": "00abd594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd4c8`](#insn-00abd4c8)

~~~json
{
  "source": "00abd4c8",
  "target": "00abd650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd4d8`](#insn-00abd4d8)

~~~json
{
  "source": "00abd4d8",
  "target": "00abd580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd4e8`](#insn-00abd4e8)

~~~json
{
  "source": "00abd4e8",
  "target": "00800378",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd4f4`](#insn-00abd4f4)

~~~json
{
  "source": "00abd4f4",
  "target": "0080062c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd504`](#insn-00abd504)

~~~json
{
  "source": "00abd504",
  "target": "00abd518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd510`](#insn-00abd510)

~~~json
{
  "source": "00abd510",
  "target": "008056ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd528`](#insn-00abd528)

~~~json
{
  "source": "00abd528",
  "target": "00a65dec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd530`](#insn-00abd530)

~~~json
{
  "source": "00abd530",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd540`](#insn-00abd540)

~~~json
{
  "source": "00abd540",
  "target": "00abd568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd548`](#insn-00abd548)

~~~json
{
  "source": "00abd548",
  "target": "00abd650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd560`](#insn-00abd560)

~~~json
{
  "source": "00abd560",
  "target": "00abd4e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd564`](#insn-00abd564)

~~~json
{
  "source": "00abd564",
  "target": "00abd580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd570`](#insn-00abd570)

~~~json
{
  "source": "00abd570",
  "target": "00abd4b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd574`](#insn-00abd574)

~~~json
{
  "source": "00abd574",
  "target": "00abd598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd57c`](#insn-00abd57c)

~~~json
{
  "source": "00abd57c",
  "target": "00abd5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd580`](#insn-00abd580)

~~~json
{
  "source": "00abd580",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd588`](#insn-00abd588)

~~~json
{
  "source": "00abd588",
  "target": "00abd5a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd590`](#insn-00abd590)

~~~json
{
  "source": "00abd590",
  "target": "00abd5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd598`](#insn-00abd598)

~~~json
{
  "source": "00abd598",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5a0`](#insn-00abd5a0)

~~~json
{
  "source": "00abd5a0",
  "target": "00abd5e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5a8`](#insn-00abd5a8)

~~~json
{
  "source": "00abd5a8",
  "target": "00abd5dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5b0`](#insn-00abd5b0)

~~~json
{
  "source": "00abd5b0",
  "target": "00abd5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5bc`](#insn-00abd5bc)

~~~json
{
  "source": "00abd5bc",
  "target": "00abd5d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5c4`](#insn-00abd5c4)

~~~json
{
  "source": "00abd5c4",
  "target": "00abd5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5d0`](#insn-00abd5d0)

~~~json
{
  "source": "00abd5d0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd5d4`](#insn-00abd5d4)

~~~json
{
  "source": "00abd5d4",
  "target": "00abd5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5d8`](#insn-00abd5d8)

~~~json
{
  "source": "00abd5d8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5dc`](#insn-00abd5dc)

~~~json
{
  "source": "00abd5dc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5e0`](#insn-00abd5e0)

~~~json
{
  "source": "00abd5e0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd5e8`](#insn-00abd5e8)

~~~json
{
  "source": "00abd5e8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5f0`](#insn-00abd5f0)

~~~json
{
  "source": "00abd5f0",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5f8`](#insn-00abd5f8)

~~~json
{
  "source": "00abd5f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd5fc`](#insn-00abd5fc)

~~~json
{
  "source": "00abd5fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd600`](#insn-00abd600)

~~~json
{
  "source": "00abd600",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd604`](#insn-00abd604)

~~~json
{
  "source": "00abd604",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd608`](#insn-00abd608)

~~~json
{
  "source": "00abd608",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd60c`](#insn-00abd60c)

~~~json
{
  "source": "00abd60c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd618`](#insn-00abd618)

~~~json
{
  "source": "00abd618",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd620`](#insn-00abd620)

~~~json
{
  "source": "00abd620",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd628`](#insn-00abd628)

~~~json
{
  "source": "00abd628",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd62c`](#insn-00abd62c)

~~~json
{
  "source": "00abd62c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd630`](#insn-00abd630)

~~~json
{
  "source": "00abd630",
  "target": "0049f3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd634`](#insn-00abd634)

~~~json
{
  "source": "00abd634",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd63c`](#insn-00abd63c)

~~~json
{
  "source": "00abd63c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd644`](#insn-00abd644)

~~~json
{
  "source": "00abd644",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd64c`](#insn-00abd64c)

~~~json
{
  "source": "00abd64c",
  "target": "0080b3c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd650`](#insn-00abd650)

~~~json
{
  "source": "00abd650",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd658`](#insn-00abd658)

~~~json
{
  "source": "00abd658",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd660`](#insn-00abd660)

~~~json
{
  "source": "00abd660",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd668`](#insn-00abd668)

~~~json
{
  "source": "00abd668",
  "target": "0080b3c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd66c`](#insn-00abd66c)

~~~json
{
  "source": "00abd66c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd674`](#insn-00abd674)

~~~json
{
  "source": "00abd674",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd67c`](#insn-00abd67c)

~~~json
{
  "source": "00abd67c",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd684`](#insn-00abd684)

~~~json
{
  "source": "00abd684",
  "target": "00470840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd688`](#insn-00abd688)

~~~json
{
  "source": "00abd688",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd690`](#insn-00abd690)

~~~json
{
  "source": "00abd690",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd698`](#insn-00abd698)

~~~json
{
  "source": "00abd698",
  "target": "00abd6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd69c`](#insn-00abd69c)

~~~json
{
  "source": "00abd69c",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd6f4`](#insn-00abd6f4)

~~~json
{
  "source": "00abd6f4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
