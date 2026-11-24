# 00beefbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beef20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-90d3fd7760b63ddb696647b22258fc13)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00beffb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-9c0d6da22fed632bc8792a5d87d095a5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beefbc",
  "name": "FUN_00beefbc",
  "size": 1052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "445788f9684eba308d8d0105135e3940b62237923e3326cf5773ece12efeae71",
  "source_text_sha256": "445788f9684eba308d8d0105135e3940b62237923e3326cf5773ece12efeae71",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beefbc",
        "00bef3d7"
      ]
    ],
    "bytes_sha256": "6119c3c7a2d77cf321a8f95982d9facda7ceb27880bb9c00eaa01390355e4aaf",
    "instruction_count": 263,
    "instruction_bytes": 1052,
    "body_bytes": 1052,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be86f4](../00be8/00be86f4.md)

## 呼び出し先

- [00bef3d8](../00bef/00bef3d8.md)
- [00c53464](../00c53/00c53464.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7856 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

bool FUN_00beefbc(undefined8 *param_1,undefined8 *param_2)

{
  long lVar1;
  int iVar2;
  int iVar3;
  ulong uVar4;
  undefined8 *puVar5;
  long lVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 local_50;
  undefined8 uStack_48;
  
  uVar4 = (long)param_2 - (long)param_1 >> 4;
  if ((long)uVar4 < 3) {
    if (uVar4 < 2) {
      return true;
    }
    if (uVar4 == 2) {
      uVar13 = param_2[-1];
      uVar11 = param_2[-2];
      uVar17 = param_1[1];
      uVar14 = *param_1;
      iVar2 = FUN_00c53464();
      if (-1 < iVar2) {
        return true;
      }
      param_1[1] = uVar13;
      *param_1 = uVar11;
LAB_00bef3a0:
      param_2[-1] = uVar17;
      param_2[-2] = uVar14;
      return true;
    }
  }
  else {
                    /* try { // try from 00bef030 to 00cef03b has its CatchHandler @ 00bef088 */
    if (uVar4 == 3) {
      uVar17 = param_1[1];
      uVar14 = *param_1;
      uVar13 = param_1[3];
      uVar11 = param_1[2];
      uVar18 = param_2[-1];
      uVar16 = param_2[-2];
      iVar2 = FUN_00c53464();
      if (iVar2 < 0) {
        iVar2 = FUN_00c53464(uVar16,uVar11);
                    /* catch() { ... } // from try @ 00bef030 with catch @ 00bef088 */
        if (iVar2 < 0) {
          param_1[1] = uVar18;
          *param_1 = uVar16;
        }
        else {
          param_1[1] = uVar13;
          *param_1 = uVar11;
          param_1[3] = uVar17;
          param_1[2] = uVar14;
          uVar13 = param_2[-1];
          uVar11 = param_2[-2];
          iVar2 = FUN_00c53464();
          if (-1 < iVar2) {
            return true;
          }
          param_1[3] = uVar13;
          param_1[2] = uVar11;
        }
        goto LAB_00bef3a0;
      }
      iVar2 = FUN_00c53464(uVar16,uVar11);
      if (-1 < iVar2) {
        return true;
      }
      param_1[3] = uVar18;
      param_1[2] = uVar16;
      param_2[-1] = uVar13;
      param_2[-2] = uVar11;
      uVar17 = param_1[1];
      uVar13 = *param_1;
      uVar14 = param_1[3];
      uVar11 = param_1[2];
      iVar2 = FUN_00c53464();
      goto joined_r0x00bef1a8;
    }
    if (uVar4 == 4) {
      uVar18 = param_1[1];
      uVar16 = *param_1;
      uVar14 = param_1[3];
      uVar11 = param_1[2];
      puVar5 = param_1 + 2;
      uVar17 = param_1[5];
      uVar13 = param_1[4];
      puVar9 = param_1 + 4;
      iVar2 = FUN_00c53464(uVar11,uVar16);
      puVar7 = param_1;
      local_50 = uVar13;
      uStack_48 = uVar17;
      if (iVar2 < 0) {
        iVar2 = FUN_00c53464(uVar13,uVar11);
        puVar8 = puVar9;
        uVar12 = uVar16;
        uVar15 = uVar18;
        if (-1 < iVar2) {
          param_1[1] = uVar14;
          *param_1 = uVar11;
          param_1[3] = uVar18;
          param_1[2] = uVar16;
          iVar2 = FUN_00c53464(uVar13,uVar16);
          puVar7 = puVar5;
          if (-1 < iVar2) goto LAB_00bef2f8;
        }
LAB_00bef2dc:
                    /* try { // try from 00bef2e0 to 00cef2eb has its CatchHandler @ 00bef780 */
        puVar8[1] = uVar18;
        *puVar8 = uVar16;
        puVar7[1] = uVar17;
        *puVar7 = uVar13;
        local_50 = uVar12;
        uStack_48 = uVar15;
      }
      else {
        iVar2 = FUN_00c53464(uVar13,uVar11);
        if (iVar2 < 0) {
          param_1[5] = uVar14;
          *puVar9 = uVar11;
          param_1[3] = uVar17;
          *puVar5 = uVar13;
          iVar2 = FUN_00c53464(uVar13,uVar16);
          puVar8 = puVar5;
          uVar12 = uVar11;
          uVar15 = uVar14;
          local_50 = uVar11;
          uStack_48 = uVar14;
          if (iVar2 < 0) goto LAB_00bef2dc;
        }
      }
LAB_00bef2f8:
      uVar14 = param_2[-1];
      uVar11 = param_2[-2];
                    /* try { // try from 00bef304 to 00cef327 has its CatchHandler @ 00bef7b8 */
      iVar2 = FUN_00c53464(uVar11,local_50);
      if (-1 < iVar2) {
        return true;
      }
      param_1[5] = uVar14;
      *puVar9 = uVar11;
      param_2[-1] = uStack_48;
      param_2[-2] = local_50;
      uVar14 = param_1[5];
      uVar11 = *puVar9;
      uVar18 = param_1[3];
      uVar16 = *puVar5;
      iVar2 = FUN_00c53464();
      if (-1 < iVar2) {
        return true;
      }
                    /* try { // try from 00bef33c to 00cef343 has its CatchHandler @ 00bef778 */
      uVar17 = param_1[1];
      uVar13 = *param_1;
      param_1[3] = uVar14;
      param_1[2] = uVar11;
      param_1[5] = uVar18;
      param_1[4] = uVar16;
      iVar2 = FUN_00c53464();
                    /* try { // try from 00bef358 to 00cef3b7 has its CatchHandler @ 00bef808 */
joined_r0x00bef1a8:
      if (iVar2 < 0) {
        param_1[1] = uVar14;
        *param_1 = uVar11;
        param_1[3] = uVar17;
        param_1[2] = uVar13;
        return true;
      }
      return true;
    }
                    /* try { // try from 00bef03c to 00cef0d7 has its CatchHandler @ 00beef94 */
    if (uVar4 == 5) {
      FUN_00bef3d8(param_1,param_1 + 2,param_1 + 4,param_1 + 6,param_2 + -2);
      return true;
    }
  }
  uVar17 = param_1[1];
  uVar13 = *param_1;
  uVar18 = param_1[3];
  uVar16 = param_1[2];
  puVar5 = param_1 + 4;
  uVar14 = param_1[5];
  uVar11 = param_1[4];
  puVar9 = param_1 + 2;
  iVar2 = FUN_00c53464(uVar16);
  puVar7 = param_1;
  if (iVar2 < 0) {
    iVar2 = FUN_00c53464(uVar11,uVar16);
    puVar8 = puVar5;
    if (-1 < iVar2) {
      param_1[1] = uVar18;
      *param_1 = uVar16;
      param_1[3] = uVar17;
      param_1[2] = uVar13;
      iVar2 = FUN_00c53464(uVar11);
      puVar7 = puVar9;
      goto joined_r0x00bef1e8;
    }
  }
  else {
    iVar2 = FUN_00c53464(uVar11,uVar16);
    if (-1 < iVar2) goto LAB_00bef1fc;
    param_1[3] = uVar14;
    *puVar9 = uVar11;
    param_1[5] = uVar18;
    *puVar5 = uVar16;
    iVar2 = FUN_00c53464(uVar11,uVar13);
    puVar8 = puVar9;
joined_r0x00bef1e8:
                    /* try { // try from 00bef1e8 to 00cef2df has its CatchHandler @ 00bef1e8
                       catch() { ... } // from try @ 00bef1e8 with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef3b8 with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef5ac with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef698 with catch @ 00bef1e8 */
    if (-1 < iVar2) goto LAB_00bef1fc;
  }
  puVar7[1] = uVar14;
  *puVar7 = uVar11;
  puVar8[1] = uVar17;
  *puVar8 = uVar13;
LAB_00bef1fc:
  if (param_1 + 6 != param_2) {
    iVar2 = 0;
    lVar10 = 0x30;
    puVar9 = param_1 + 6;
    do {
      uVar13 = puVar9[1];
      uVar11 = *puVar9;
      uVar17 = puVar5[1];
      uVar14 = *puVar5;
      iVar3 = FUN_00c53464();
      lVar6 = lVar10;
      if (iVar3 < 0) {
        do {
          lVar1 = lVar6 + -0x10;
          ((undefined8 *)((long)param_1 + lVar6))[1] = uVar17;
          *(undefined8 *)((long)param_1 + lVar6) = uVar14;
          puVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bef218;
          uVar17 = *(undefined8 *)((long)param_1 + lVar6 + -0x18);
          uVar14 = *(undefined8 *)((long)param_1 + lVar6 + -0x20);
          iVar3 = FUN_00c53464(uVar11);
          lVar6 = lVar1;
        } while (iVar3 < 0);
        puVar5 = (undefined8 *)((long)param_1 + lVar1);
LAB_00bef218:
        iVar2 = iVar2 + 1;
        puVar5[1] = uVar13;
        *puVar5 = uVar11;
        if (iVar2 == 8) {
          return puVar9 + 2 == param_2;
        }
      }
      puVar7 = puVar9 + 2;
      lVar10 = lVar10 + 0x10;
      puVar5 = puVar9;
      puVar9 = puVar7;
    } while (puVar7 != param_2);
  }
                    /* try { // try from 00bef3b8 to 00cef523 has its CatchHandler @ 00bef1e8 */
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beefbc"></a> `00beefbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beefc0"></a> `00beefc0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00beefc4"></a> `00beefc4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00beefc8"></a> `00beefc8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00beefcc"></a> `00beefcc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00beefd0"></a> `00beefd0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00beefd4"></a> `00beefd4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00beefd8"></a> `00beefd8` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beefdc"></a> `00beefdc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00beefe0"></a> `00beefe0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00beefe4"></a> `00beefe4` | `08 fd 44 93` | asr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beefe8"></a> `00beefe8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beefec"></a> `00beefec` | `0c 02 00 54` | b.gt 0x00bef02c | `CONDITIONAL_JUMP`
<a id="insn-00beeff0"></a> `00beeff0` | `c3 1d 00 54` | b.cc 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00beeff4"></a> `00beeff4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeff8"></a> `00beeff8` | `21 05 00 54` | b.ne 0x00bef09c | `CONDITIONAL_JUMP`
<a id="insn-00beeffc"></a> `00beeffc` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef000"></a> `00bef000` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00bef004"></a> `00bef004` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef008"></a> `00bef008` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef00c"></a> `00bef00c` | `16 91 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef010"></a> `00bef010` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef014"></a> `00bef014` | `aa 1c 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef018"></a> `00bef018` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef01c"></a> `00bef01c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bef020"></a> `00bef020` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef024"></a> `00bef024` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef028"></a> `00bef028` | `de 00 00 14` | b 0x00bef3a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef02c"></a> `00bef02c` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bef030"></a> `00bef030` | `80 01 00 54` | b.eq 0x00bef060 | `CONDITIONAL_JUMP`
<a id="insn-00bef034"></a> `00bef034` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bef038"></a> `00bef038` | `20 06 00 54` | b.eq 0x00bef0fc | `CONDITIONAL_JUMP`
<a id="insn-00bef03c"></a> `00bef03c` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bef040"></a> `00bef040` | `e1 02 00 54` | b.ne 0x00bef09c | `CONDITIONAL_JUMP`
<a id="insn-00bef044"></a> `00bef044` | `84 42 00 d1` | sub x4,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bef048"></a> `00bef048` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bef04c"></a> `00bef04c` | `62 82 00 91` | add x2,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bef050"></a> `00bef050` | `63 c2 00 91` | add x3,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bef054"></a> `00bef054` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bef058"></a> `00bef058` | `e0 00 00 94` | bl 0x00bef3d8 | `UNCONDITIONAL_CALL`
<a id="insn-00bef05c"></a> `00bef05c` | `d3 00 00 14` | b 0x00bef3a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef060"></a> `00bef060` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef064"></a> `00bef064` | `82 02 df 3c` | ldur q2,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef068"></a> `00bef068` | `e2 07 80 3d` | str q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef06c"></a> `00bef06c` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef070"></a> `00bef070` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef074"></a> `00bef074` | `fc 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef078"></a> `00bef078` | `c0 07 f8 36` | tbz w0,#0x1f,0x00bef170 | `CONDITIONAL_JUMP`
<a id="insn-00bef07c"></a> `00bef07c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef080"></a> `00bef080` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef084"></a> `00bef084` | `f8 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef088"></a> `00bef088` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef08c"></a> `00bef08c` | `2a 17 00 54` | b.ge 0x00bef370 | `CONDITIONAL_JUMP`
<a id="insn-00bef090"></a> `00bef090` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef094"></a> `00bef094` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef098"></a> `00bef098` | `c0 00 00 14` | b 0x00bef398 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef09c"></a> `00bef09c` | `61 0a 40 ad` | ldp q1,q2,[x19] | `FALL_THROUGH`
<a id="insn-00bef0a0"></a> `00bef0a0` | `75 82 00 91` | add x21,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bef0a4"></a> `00bef0a4` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bef0a8"></a> `00bef0a8` | `76 42 00 91` | add x22,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bef0ac"></a> `00bef0ac` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef0b0"></a> `00bef0b0` | `40 1c a2 4e` | mov v0.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00bef0b4"></a> `00bef0b4` | `e1 0b 00 ad` | stp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00bef0b8"></a> `00bef0b8` | `eb 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef0bc"></a> `00bef0bc` | `e0 07 f8 36` | tbz w0,#0x1f,0x00bef1b8 | `CONDITIONAL_JUMP`
<a id="insn-00bef0c0"></a> `00bef0c0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef0c4"></a> `00bef0c4` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef0c8"></a> `00bef0c8` | `e7 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef0cc"></a> `00bef0cc` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bef0d0"></a> `00bef0d0` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bef0d4"></a> `00bef0d4` | `c0 08 f8 37` | tbnz w0,#0x1f,0x00bef1ec | `CONDITIONAL_JUMP`
<a id="insn-00bef0d8"></a> `00bef0d8` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00bef0dc"></a> `00bef0dc` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bef0e0"></a> `00bef0e0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef0e4"></a> `00bef0e4` | `e0 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef0e8"></a> `00bef0e8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef0ec"></a> `00bef0ec` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bef0f0"></a> `00bef0f0` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bef0f4"></a> `00bef0f4` | `cb 07 00 54` | b.lt 0x00bef1ec | `CONDITIONAL_JUMP`
<a id="insn-00bef0f8"></a> `00bef0f8` | `41 00 00 14` | b 0x00bef1fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bef0fc"></a> `00bef0fc` | `62 02 40 ad` | ldp q2,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef100"></a> `00bef100` | `75 42 00 91` | add x21,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bef104"></a> `00bef104` | `61 0a c0 3d` | ldr q1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bef108"></a> `00bef108` | `76 82 00 91` | add x22,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bef10c"></a> `00bef10c` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef110"></a> `00bef110` | `41 1c a2 4e` | mov v1.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00bef114"></a> `00bef114` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef118"></a> `00bef118` | `e2 03 80 3d` | str q2,[sp] | `FALL_THROUGH`
<a id="insn-00bef11c"></a> `00bef11c` | `d2 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef120"></a> `00bef120` | `e0 0b f8 36` | tbz w0,#0x1f,0x00bef29c | `CONDITIONAL_JUMP`
<a id="insn-00bef124"></a> `00bef124` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef128"></a> `00bef128` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef12c"></a> `00bef12c` | `ce 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef130"></a> `00bef130` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef134"></a> `00bef134` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bef138"></a> `00bef138` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bef13c"></a> `00bef13c` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bef140"></a> `00bef140` | `e0 0c f8 37` | tbnz w0,#0x1f,0x00bef2dc | `CONDITIONAL_JUMP`
<a id="insn-00bef144"></a> `00bef144` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef148"></a> `00bef148` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bef14c"></a> `00bef14c` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00bef150"></a> `00bef150` | `c5 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef154"></a> `00bef154` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef158"></a> `00bef158` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef15c"></a> `00bef15c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bef160"></a> `00bef160` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bef164"></a> `00bef164` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bef168"></a> `00bef168` | `ab 0b 00 54` | b.lt 0x00bef2dc | `CONDITIONAL_JUMP`
<a id="insn-00bef16c"></a> `00bef16c` | `61 00 00 14` | b 0x00bef2f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef170"></a> `00bef170` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef174"></a> `00bef174` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef178"></a> `00bef178` | `bb 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef17c"></a> `00bef17c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef180"></a> `00bef180` | `4a 11 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef184"></a> `00bef184` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef188"></a> `00bef188` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bef18c"></a> `00bef18c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef190"></a> `00bef190` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef194"></a> `00bef194` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef198"></a> `00bef198` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef19c"></a> `00bef19c` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef1a0"></a> `00bef1a0` | `b1 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef1a4"></a> `00bef1a4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef1a8"></a> `00bef1a8` | `0a 10 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef1ac"></a> `00bef1ac` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef1b0"></a> `00bef1b0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef1b4"></a> `00bef1b4` | `6c 00 00 14` | b 0x00bef364 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef1b8"></a> `00bef1b8` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef1bc"></a> `00bef1bc` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef1c0"></a> `00bef1c0` | `a9 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef1c4"></a> `00bef1c4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef1c8"></a> `00bef1c8` | `aa 01 00 54` | b.ge 0x00bef1fc | `CONDITIONAL_JUMP`
<a id="insn-00bef1cc"></a> `00bef1cc` | `e1 0b 40 ad` | ldp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00bef1d0"></a> `00bef1d0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef1d4"></a> `00bef1d4` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bef1d8"></a> `00bef1d8` | `a2 02 80 3d` | str q2,[x21] | `FALL_THROUGH`
<a id="insn-00bef1dc"></a> `00bef1dc` | `a2 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef1e0"></a> `00bef1e0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bef1e4"></a> `00bef1e4` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bef1e8"></a> `00bef1e8` | `a0 00 f8 36` | tbz w0,#0x1f,0x00bef1fc | `CONDITIONAL_JUMP`
<a id="insn-00bef1ec"></a> `00bef1ec` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef1f0"></a> `00bef1f0` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bef1f4"></a> `00bef1f4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bef1f8"></a> `00bef1f8` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00bef1fc"></a> `00bef1fc` | `76 c2 00 91` | add x22,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bef200"></a> `00bef200` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00bef204"></a> `00bef204` | `20 0d 00 54` | b.eq 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef208"></a> `00bef208` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bef20c"></a> `00bef20c` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00bef210"></a> `00bef210` | `0d 00 00 14` | b 0x00bef244 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef214"></a> `00bef214` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bef218"></a> `00bef218` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bef21c"></a> `00bef21c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef220"></a> `00bef220` | `ff 22 00 71` | cmp w23,#0x8 | `FALL_THROUGH`
<a id="insn-00bef224"></a> `00bef224` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bef228"></a> `00bef228` | `00 0d 00 54` | b.eq 0x00bef3c8 | `CONDITIONAL_JUMP`
<a id="insn-00bef22c"></a> `00bef22c` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bef230"></a> `00bef230` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bef234"></a> `00bef234` | `18 43 00 91` | add x24,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00bef238"></a> `00bef238` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bef23c"></a> `00bef23c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bef240"></a> `00bef240` | `40 0b 00 54` | b.eq 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef244"></a> `00bef244` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00bef248"></a> `00bef248` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00bef24c"></a> `00bef24c` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef250"></a> `00bef250` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef254"></a> `00bef254` | `84 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef258"></a> `00bef258` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef25c"></a> `00bef25c` | `8a fe ff 54` | b.ge 0x00bef22c | `CONDITIONAL_JUMP`
<a id="insn-00bef260"></a> `00bef260` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef264"></a> `00bef264` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00bef268"></a> `00bef268` | `15 41 00 f1` | subs x21,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bef26c"></a> `00bef26c` | `60 6a a8 3c` | str q0,[x19,x8] | `FALL_THROUGH`
<a id="insn-00bef270"></a> `00bef270` | `20 fd ff 54` | b.eq 0x00bef214 | `CONDITIONAL_JUMP`
<a id="insn-00bef274"></a> `00bef274` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bef278"></a> `00bef278` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef27c"></a> `00bef27c` | `01 01 de 3c` | ldur q1,[x8, #-0x20] | `FALL_THROUGH`
<a id="insn-00bef280"></a> `00bef280` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef284"></a> `00bef284` | `78 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef288"></a> `00bef288` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef28c"></a> `00bef28c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bef290"></a> `00bef290` | `c0 fe ff 37` | tbnz w0,#0x1f,0x00bef268 | `CONDITIONAL_JUMP`
<a id="insn-00bef294"></a> `00bef294` | `68 02 15 8b` | add x8,x19,x21 | `FALL_THROUGH`
<a id="insn-00bef298"></a> `00bef298` | `e0 ff ff 17` | b 0x00bef218 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef29c"></a> `00bef29c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef2a0"></a> `00bef2a0` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2a4"></a> `00bef2a4` | `70 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef2a8"></a> `00bef2a8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef2ac"></a> `00bef2ac` | `2a 02 00 54` | b.ge 0x00bef2f0 | `CONDITIONAL_JUMP`
<a id="insn-00bef2b0"></a> `00bef2b0` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2b4"></a> `00bef2b4` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef2b8"></a> `00bef2b8` | `c1 02 80 3d` | str q1,[x22] | `FALL_THROUGH`
<a id="insn-00bef2bc"></a> `00bef2bc` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef2c0"></a> `00bef2c0` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bef2c4"></a> `00bef2c4` | `68 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef2c8"></a> `00bef2c8` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef2cc"></a> `00bef2cc` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2d0"></a> `00bef2d0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bef2d4"></a> `00bef2d4` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bef2d8"></a> `00bef2d8` | `00 01 f8 36` | tbz w0,#0x1f,0x00bef2f8 | `CONDITIONAL_JUMP`
<a id="insn-00bef2dc"></a> `00bef2dc` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef2e0"></a> `00bef2e0` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2e4"></a> `00bef2e4` | `21 01 80 3d` | str q1,[x9] | `FALL_THROUGH`
<a id="insn-00bef2e8"></a> `00bef2e8` | `02 01 80 3d` | str q2,[x8] | `FALL_THROUGH`
<a id="insn-00bef2ec"></a> `00bef2ec` | `03 00 00 14` | b 0x00bef2f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bef2f0"></a> `00bef2f0` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef2f4"></a> `00bef2f4` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2f8"></a> `00bef2f8` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef2fc"></a> `00bef2fc` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef300"></a> `00bef300` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef304"></a> `00bef304` | `58 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef308"></a> `00bef308` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef30c"></a> `00bef30c` | `ea 04 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef310"></a> `00bef310` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef314"></a> `00bef314` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bef318"></a> `00bef318` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef31c"></a> `00bef31c` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef320"></a> `00bef320` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00bef324"></a> `00bef324` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00bef328"></a> `00bef328` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef32c"></a> `00bef32c` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef330"></a> `00bef330` | `4d 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef334"></a> `00bef334` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef338"></a> `00bef338` | `8a 03 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef33c"></a> `00bef33c` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00bef340"></a> `00bef340` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef344"></a> `00bef344` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef348"></a> `00bef348` | `60 8a 00 ad` | stp q0,q2,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bef34c"></a> `00bef34c` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef350"></a> `00bef350` | `45 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef354"></a> `00bef354` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef358"></a> `00bef358` | `8a 02 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef35c"></a> `00bef35c` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef360"></a> `00bef360` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bef364"></a> `00bef364` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bef368"></a> `00bef368` | `61 02 00 ad` | stp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bef36c"></a> `00bef36c` | `10 00 00 14` | b 0x00bef3ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bef370"></a> `00bef370` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef374"></a> `00bef374` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bef378"></a> `00bef378` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bef37c"></a> `00bef37c` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef380"></a> `00bef380` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef384"></a> `00bef384` | `38 90 01 94` | bl 0x00c53464 | `UNCONDITIONAL_CALL`
<a id="insn-00bef388"></a> `00bef388` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bef38c"></a> `00bef38c` | `ea 00 00 54` | b.ge 0x00bef3a8 | `CONDITIONAL_JUMP`
<a id="insn-00bef390"></a> `00bef390` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef394"></a> `00bef394` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bef398"></a> `00bef398` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bef39c"></a> `00bef39c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bef3a0"></a> `00bef3a0` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bef3a4"></a> `00bef3a4` | `02 00 00 14` | b 0x00bef3ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bef3a8"></a> `00bef3a8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bef3ac"></a> `00bef3ac` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bef3b0"></a> `00bef3b0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bef3b4"></a> `00bef3b4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bef3b8"></a> `00bef3b8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bef3bc"></a> `00bef3bc` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bef3c0"></a> `00bef3c0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bef3c4"></a> `00bef3c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bef3c8"></a> `00bef3c8` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bef3cc"></a> `00bef3cc` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bef3d0"></a> `00bef3d0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bef3d4"></a> `00bef3d4` | `f6 ff ff 17` | b 0x00bef3ac | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beefbc`](#insn-00beefbc) 範囲 `[['00beefbc', '00beefef']]`
  - `CONDITIONAL_JUMP` [`00beefec`](#insn-00beefec) → [`00bef02c`](#insn-00bef02c)
  - `FALL_THROUGH` [`00beefec`](#insn-00beefec) → [`00beeff0`](#insn-00beeff0)
- ブロック [`00beeff0`](#insn-00beeff0) 範囲 `[['00beeff0', '00beeff3']]`
  - `CONDITIONAL_JUMP` [`00beeff0`](#insn-00beeff0) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00beeff0`](#insn-00beeff0) → [`00beeff4`](#insn-00beeff4)
- ブロック [`00beeff4`](#insn-00beeff4) 範囲 `[['00beeff4', '00beeffb']]`
  - `CONDITIONAL_JUMP` [`00beeff8`](#insn-00beeff8) → [`00bef09c`](#insn-00bef09c)
  - `FALL_THROUGH` [`00beeff8`](#insn-00beeff8) → [`00beeffc`](#insn-00beeffc)
- ブロック [`00beeffc`](#insn-00beeffc) 範囲 `[['00beeffc', '00bef017']]`
  - `CONDITIONAL_JUMP` [`00bef014`](#insn-00bef014) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef014`](#insn-00bef014) → [`00bef018`](#insn-00bef018)
- ブロック [`00bef018`](#insn-00bef018) 範囲 `[['00bef018', '00bef02b']]`
  - `UNCONDITIONAL_JUMP` [`00bef028`](#insn-00bef028) → [`00bef3a0`](#insn-00bef3a0)
- ブロック [`00bef02c`](#insn-00bef02c) 範囲 `[['00bef02c', '00bef02f']]`
  - `FALL_THROUGH` [`00bef02c`](#insn-00bef02c) → [`00bef030`](#insn-00bef030)
- ブロック [`00bef030`](#insn-00bef030) 範囲 `[['00bef030', '00bef033']]`
  - `CONDITIONAL_JUMP` [`00bef030`](#insn-00bef030) → [`00bef060`](#insn-00bef060)
  - `FALL_THROUGH` [`00bef030`](#insn-00bef030) → [`00bef034`](#insn-00bef034)
- ブロック [`00bef034`](#insn-00bef034) 範囲 `[['00bef034', '00bef03b']]`
  - `CONDITIONAL_JUMP` [`00bef038`](#insn-00bef038) → [`00bef0fc`](#insn-00bef0fc)
  - `FALL_THROUGH` [`00bef038`](#insn-00bef038) → [`00bef03c`](#insn-00bef03c)
- ブロック [`00bef03c`](#insn-00bef03c) 範囲 `[['00bef03c', '00bef043']]`
  - `CONDITIONAL_JUMP` [`00bef040`](#insn-00bef040) → [`00bef09c`](#insn-00bef09c)
  - `FALL_THROUGH` [`00bef040`](#insn-00bef040) → [`00bef044`](#insn-00bef044)
- ブロック [`00bef044`](#insn-00bef044) 範囲 `[['00bef044', '00bef05f']]`
  - `UNCONDITIONAL_JUMP` [`00bef05c`](#insn-00bef05c) → [`00bef3a8`](#insn-00bef3a8)
- ブロック [`00bef060`](#insn-00bef060) 範囲 `[['00bef060', '00bef07b']]`
  - `CONDITIONAL_JUMP` [`00bef078`](#insn-00bef078) → [`00bef170`](#insn-00bef170)
  - `FALL_THROUGH` [`00bef078`](#insn-00bef078) → [`00bef07c`](#insn-00bef07c)
- ブロック [`00bef07c`](#insn-00bef07c) 範囲 `[['00bef07c', '00bef087']]`
  - `FALL_THROUGH` [`00bef084`](#insn-00bef084) → [`00bef088`](#insn-00bef088)
- ブロック [`00bef088`](#insn-00bef088) 範囲 `[['00bef088', '00bef08f']]`
  - `CONDITIONAL_JUMP` [`00bef08c`](#insn-00bef08c) → [`00bef370`](#insn-00bef370)
  - `FALL_THROUGH` [`00bef08c`](#insn-00bef08c) → [`00bef090`](#insn-00bef090)
- ブロック [`00bef090`](#insn-00bef090) 範囲 `[['00bef090', '00bef09b']]`
  - `UNCONDITIONAL_JUMP` [`00bef098`](#insn-00bef098) → [`00bef398`](#insn-00bef398)
- ブロック [`00bef09c`](#insn-00bef09c) 範囲 `[['00bef09c', '00bef0bf']]`
  - `CONDITIONAL_JUMP` [`00bef0bc`](#insn-00bef0bc) → [`00bef1b8`](#insn-00bef1b8)
  - `FALL_THROUGH` [`00bef0bc`](#insn-00bef0bc) → [`00bef0c0`](#insn-00bef0c0)
- ブロック [`00bef0c0`](#insn-00bef0c0) 範囲 `[['00bef0c0', '00bef0d7']]`
  - `CONDITIONAL_JUMP` [`00bef0d4`](#insn-00bef0d4) → [`00bef1ec`](#insn-00bef1ec)
  - `FALL_THROUGH` [`00bef0d4`](#insn-00bef0d4) → [`00bef0d8`](#insn-00bef0d8)
- ブロック [`00bef0d8`](#insn-00bef0d8) 範囲 `[['00bef0d8', '00bef0f7']]`
  - `CONDITIONAL_JUMP` [`00bef0f4`](#insn-00bef0f4) → [`00bef1ec`](#insn-00bef1ec)
  - `FALL_THROUGH` [`00bef0f4`](#insn-00bef0f4) → [`00bef0f8`](#insn-00bef0f8)
- ブロック [`00bef0f8`](#insn-00bef0f8) 範囲 `[['00bef0f8', '00bef0fb']]`
  - `UNCONDITIONAL_JUMP` [`00bef0f8`](#insn-00bef0f8) → [`00bef1fc`](#insn-00bef1fc)
- ブロック [`00bef0fc`](#insn-00bef0fc) 範囲 `[['00bef0fc', '00bef123']]`
  - `CONDITIONAL_JUMP` [`00bef120`](#insn-00bef120) → [`00bef29c`](#insn-00bef29c)
  - `FALL_THROUGH` [`00bef120`](#insn-00bef120) → [`00bef124`](#insn-00bef124)
- ブロック [`00bef124`](#insn-00bef124) 範囲 `[['00bef124', '00bef143']]`
  - `CONDITIONAL_JUMP` [`00bef140`](#insn-00bef140) → [`00bef2dc`](#insn-00bef2dc)
  - `FALL_THROUGH` [`00bef140`](#insn-00bef140) → [`00bef144`](#insn-00bef144)
- ブロック [`00bef144`](#insn-00bef144) 範囲 `[['00bef144', '00bef16b']]`
  - `CONDITIONAL_JUMP` [`00bef168`](#insn-00bef168) → [`00bef2dc`](#insn-00bef2dc)
  - `FALL_THROUGH` [`00bef168`](#insn-00bef168) → [`00bef16c`](#insn-00bef16c)
- ブロック [`00bef16c`](#insn-00bef16c) 範囲 `[['00bef16c', '00bef16f']]`
  - `UNCONDITIONAL_JUMP` [`00bef16c`](#insn-00bef16c) → [`00bef2f0`](#insn-00bef2f0)
- ブロック [`00bef170`](#insn-00bef170) 範囲 `[['00bef170', '00bef183']]`
  - `CONDITIONAL_JUMP` [`00bef180`](#insn-00bef180) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef180`](#insn-00bef180) → [`00bef184`](#insn-00bef184)
- ブロック [`00bef184`](#insn-00bef184) 範囲 `[['00bef184', '00bef1ab']]`
  - `CONDITIONAL_JUMP` [`00bef1a8`](#insn-00bef1a8) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef1a8`](#insn-00bef1a8) → [`00bef1ac`](#insn-00bef1ac)
- ブロック [`00bef1ac`](#insn-00bef1ac) 範囲 `[['00bef1ac', '00bef1b7']]`
  - `UNCONDITIONAL_JUMP` [`00bef1b4`](#insn-00bef1b4) → [`00bef364`](#insn-00bef364)
- ブロック [`00bef1b8`](#insn-00bef1b8) 範囲 `[['00bef1b8', '00bef1cb']]`
  - `CONDITIONAL_JUMP` [`00bef1c8`](#insn-00bef1c8) → [`00bef1fc`](#insn-00bef1fc)
  - `FALL_THROUGH` [`00bef1c8`](#insn-00bef1c8) → [`00bef1cc`](#insn-00bef1cc)
- ブロック [`00bef1cc`](#insn-00bef1cc) 範囲 `[['00bef1cc', '00bef1e7']]`
  - `FALL_THROUGH` [`00bef1e4`](#insn-00bef1e4) → [`00bef1e8`](#insn-00bef1e8)
- ブロック [`00bef1e8`](#insn-00bef1e8) 範囲 `[['00bef1e8', '00bef1eb']]`
  - `CONDITIONAL_JUMP` [`00bef1e8`](#insn-00bef1e8) → [`00bef1fc`](#insn-00bef1fc)
  - `FALL_THROUGH` [`00bef1e8`](#insn-00bef1e8) → [`00bef1ec`](#insn-00bef1ec)
- ブロック [`00bef1ec`](#insn-00bef1ec) 範囲 `[['00bef1ec', '00bef1fb']]`
  - `FALL_THROUGH` [`00bef1f8`](#insn-00bef1f8) → [`00bef1fc`](#insn-00bef1fc)
- ブロック [`00bef1fc`](#insn-00bef1fc) 範囲 `[['00bef1fc', '00bef207']]`
  - `CONDITIONAL_JUMP` [`00bef204`](#insn-00bef204) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef204`](#insn-00bef204) → [`00bef208`](#insn-00bef208)
- ブロック [`00bef208`](#insn-00bef208) 範囲 `[['00bef208', '00bef213']]`
  - `UNCONDITIONAL_JUMP` [`00bef210`](#insn-00bef210) → [`00bef244`](#insn-00bef244)
- ブロック [`00bef214`](#insn-00bef214) 範囲 `[['00bef214', '00bef217']]`
  - `FALL_THROUGH` [`00bef214`](#insn-00bef214) → [`00bef218`](#insn-00bef218)
- ブロック [`00bef218`](#insn-00bef218) 範囲 `[['00bef218', '00bef22b']]`
  - `CONDITIONAL_JUMP` [`00bef228`](#insn-00bef228) → [`00bef3c8`](#insn-00bef3c8)
  - `FALL_THROUGH` [`00bef228`](#insn-00bef228) → [`00bef22c`](#insn-00bef22c)
- ブロック [`00bef22c`](#insn-00bef22c) 範囲 `[['00bef22c', '00bef243']]`
  - `CONDITIONAL_JUMP` [`00bef240`](#insn-00bef240) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef240`](#insn-00bef240) → [`00bef244`](#insn-00bef244)
- ブロック [`00bef244`](#insn-00bef244) 範囲 `[['00bef244', '00bef25f']]`
  - `CONDITIONAL_JUMP` [`00bef25c`](#insn-00bef25c) → [`00bef22c`](#insn-00bef22c)
  - `FALL_THROUGH` [`00bef25c`](#insn-00bef25c) → [`00bef260`](#insn-00bef260)
- ブロック [`00bef260`](#insn-00bef260) 範囲 `[['00bef260', '00bef267']]`
  - `FALL_THROUGH` [`00bef264`](#insn-00bef264) → [`00bef268`](#insn-00bef268)
- ブロック [`00bef268`](#insn-00bef268) 範囲 `[['00bef268', '00bef273']]`
  - `CONDITIONAL_JUMP` [`00bef270`](#insn-00bef270) → [`00bef214`](#insn-00bef214)
  - `FALL_THROUGH` [`00bef270`](#insn-00bef270) → [`00bef274`](#insn-00bef274)
- ブロック [`00bef274`](#insn-00bef274) 範囲 `[['00bef274', '00bef293']]`
  - `CONDITIONAL_JUMP` [`00bef290`](#insn-00bef290) → [`00bef268`](#insn-00bef268)
  - `FALL_THROUGH` [`00bef290`](#insn-00bef290) → [`00bef294`](#insn-00bef294)
- ブロック [`00bef294`](#insn-00bef294) 範囲 `[['00bef294', '00bef29b']]`
  - `UNCONDITIONAL_JUMP` [`00bef298`](#insn-00bef298) → [`00bef218`](#insn-00bef218)
- ブロック [`00bef29c`](#insn-00bef29c) 範囲 `[['00bef29c', '00bef2af']]`
  - `CONDITIONAL_JUMP` [`00bef2ac`](#insn-00bef2ac) → [`00bef2f0`](#insn-00bef2f0)
  - `FALL_THROUGH` [`00bef2ac`](#insn-00bef2ac) → [`00bef2b0`](#insn-00bef2b0)
- ブロック [`00bef2b0`](#insn-00bef2b0) 範囲 `[['00bef2b0', '00bef2db']]`
  - `CONDITIONAL_JUMP` [`00bef2d8`](#insn-00bef2d8) → [`00bef2f8`](#insn-00bef2f8)
  - `FALL_THROUGH` [`00bef2d8`](#insn-00bef2d8) → [`00bef2dc`](#insn-00bef2dc)
- ブロック [`00bef2dc`](#insn-00bef2dc) 範囲 `[['00bef2dc', '00bef2df']]`
  - `FALL_THROUGH` [`00bef2dc`](#insn-00bef2dc) → [`00bef2e0`](#insn-00bef2e0)
- ブロック [`00bef2e0`](#insn-00bef2e0) 範囲 `[['00bef2e0', '00bef2ef']]`
  - `UNCONDITIONAL_JUMP` [`00bef2ec`](#insn-00bef2ec) → [`00bef2f8`](#insn-00bef2f8)
- ブロック [`00bef2f0`](#insn-00bef2f0) 範囲 `[['00bef2f0', '00bef2f7']]`
  - `FALL_THROUGH` [`00bef2f4`](#insn-00bef2f4) → [`00bef2f8`](#insn-00bef2f8)
- ブロック [`00bef2f8`](#insn-00bef2f8) 範囲 `[['00bef2f8', '00bef303']]`
  - `FALL_THROUGH` [`00bef300`](#insn-00bef300) → [`00bef304`](#insn-00bef304)
- ブロック [`00bef304`](#insn-00bef304) 範囲 `[['00bef304', '00bef30f']]`
  - `CONDITIONAL_JUMP` [`00bef30c`](#insn-00bef30c) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef30c`](#insn-00bef30c) → [`00bef310`](#insn-00bef310)
- ブロック [`00bef310`](#insn-00bef310) 範囲 `[['00bef310', '00bef33b']]`
  - `CONDITIONAL_JUMP` [`00bef338`](#insn-00bef338) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef338`](#insn-00bef338) → [`00bef33c`](#insn-00bef33c)
- ブロック [`00bef33c`](#insn-00bef33c) 範囲 `[['00bef33c', '00bef357']]`
  - `FALL_THROUGH` [`00bef354`](#insn-00bef354) → [`00bef358`](#insn-00bef358)
- ブロック [`00bef358`](#insn-00bef358) 範囲 `[['00bef358', '00bef35b']]`
  - `CONDITIONAL_JUMP` [`00bef358`](#insn-00bef358) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef358`](#insn-00bef358) → [`00bef35c`](#insn-00bef35c)
- ブロック [`00bef35c`](#insn-00bef35c) 範囲 `[['00bef35c', '00bef363']]`
  - `FALL_THROUGH` [`00bef360`](#insn-00bef360) → [`00bef364`](#insn-00bef364)
- ブロック [`00bef364`](#insn-00bef364) 範囲 `[['00bef364', '00bef36f']]`
  - `UNCONDITIONAL_JUMP` [`00bef36c`](#insn-00bef36c) → [`00bef3ac`](#insn-00bef3ac)
- ブロック [`00bef370`](#insn-00bef370) 範囲 `[['00bef370', '00bef38f']]`
  - `CONDITIONAL_JUMP` [`00bef38c`](#insn-00bef38c) → [`00bef3a8`](#insn-00bef3a8)
  - `FALL_THROUGH` [`00bef38c`](#insn-00bef38c) → [`00bef390`](#insn-00bef390)
- ブロック [`00bef390`](#insn-00bef390) 範囲 `[['00bef390', '00bef397']]`
  - `FALL_THROUGH` [`00bef394`](#insn-00bef394) → [`00bef398`](#insn-00bef398)
- ブロック [`00bef398`](#insn-00bef398) 範囲 `[['00bef398', '00bef39f']]`
  - `FALL_THROUGH` [`00bef39c`](#insn-00bef39c) → [`00bef3a0`](#insn-00bef3a0)
- ブロック [`00bef3a0`](#insn-00bef3a0) 範囲 `[['00bef3a0', '00bef3a7']]`
  - `UNCONDITIONAL_JUMP` [`00bef3a4`](#insn-00bef3a4) → [`00bef3ac`](#insn-00bef3ac)
- ブロック [`00bef3a8`](#insn-00bef3a8) 範囲 `[['00bef3a8', '00bef3ab']]`
  - `FALL_THROUGH` [`00bef3a8`](#insn-00bef3a8) → [`00bef3ac`](#insn-00bef3ac)
- ブロック [`00bef3ac`](#insn-00bef3ac) 範囲 `[['00bef3ac', '00bef3b7']]`
  - `FALL_THROUGH` [`00bef3b4`](#insn-00bef3b4) → [`00bef3b8`](#insn-00bef3b8)
- ブロック [`00bef3b8`](#insn-00bef3b8) 範囲 `[['00bef3b8', '00bef3c7']]`
- ブロック [`00bef3c8`](#insn-00bef3c8) 範囲 `[['00bef3c8', '00bef3d7']]`
  - `UNCONDITIONAL_JUMP` [`00bef3d4`](#insn-00bef3d4) → [`00bef3ac`](#insn-00bef3ac)

## 命令位置別の参照

- [`00beefc4`](#insn-00beefc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefc8`](#insn-00beefc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefcc`](#insn-00beefcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefd0`](#insn-00beefd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beefec`](#insn-00beefec) → [`00bef02c`](#insn-00bef02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeff0`](#insn-00beeff0) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeff8`](#insn-00beeff8) → [`00bef09c`](#insn-00bef09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef004`](#insn-00bef004) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef008`](#insn-00bef008) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef00c`](#insn-00bef00c) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef014`](#insn-00bef014) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef018`](#insn-00bef018) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef024`](#insn-00bef024) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef028`](#insn-00bef028) → [`00bef3a0`](#insn-00bef3a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef030`](#insn-00bef030) → [`00bef060`](#insn-00bef060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef038`](#insn-00bef038) → [`00bef0fc`](#insn-00bef0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef040`](#insn-00bef040) → [`00bef09c`](#insn-00bef09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef058`](#insn-00bef058) → [`00bef3d8`](../00bef/00bef3d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bef3d8` · 推定シンボル `None` · 推定型 `None`
- [`00bef05c`](#insn-00bef05c) → [`00bef3a8`](#insn-00bef3a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef068`](#insn-00bef068) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef06c`](#insn-00bef06c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef070`](#insn-00bef070) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef074`](#insn-00bef074) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef078`](#insn-00bef078) → [`00bef170`](#insn-00bef170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef07c`](#insn-00bef07c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef080`](#insn-00bef080) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef084`](#insn-00bef084) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef08c`](#insn-00bef08c) → [`00bef370`](#insn-00bef370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef090`](#insn-00bef090) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef098`](#insn-00bef098) → [`00bef398`](#insn-00bef398) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0ac`](#insn-00bef0ac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0b4`](#insn-00bef0b4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0b8`](#insn-00bef0b8) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef0bc`](#insn-00bef0bc) → [`00bef1b8`](#insn-00bef1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0c0`](#insn-00bef0c0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0c4`](#insn-00bef0c4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0c8`](#insn-00bef0c8) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef0d4`](#insn-00bef0d4) → [`00bef1ec`](#insn-00bef1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0d8`](#insn-00bef0d8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0e0`](#insn-00bef0e0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0e4`](#insn-00bef0e4) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef0f4`](#insn-00bef0f4) → [`00bef1ec`](#insn-00bef1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef0f8`](#insn-00bef0f8) → [`00bef1fc`](#insn-00bef1fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef10c`](#insn-00bef10c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef114`](#insn-00bef114) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef118`](#insn-00bef118) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef11c`](#insn-00bef11c) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef120`](#insn-00bef120) → [`00bef29c`](#insn-00bef29c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef124`](#insn-00bef124) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef128`](#insn-00bef128) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef12c`](#insn-00bef12c) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef130`](#insn-00bef130) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef140`](#insn-00bef140) → [`00bef2dc`](#insn-00bef2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef144`](#insn-00bef144) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef14c`](#insn-00bef14c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef150`](#insn-00bef150) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef154`](#insn-00bef154) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef168`](#insn-00bef168) → [`00bef2dc`](#insn-00bef2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef16c`](#insn-00bef16c) → [`00bef2f0`](#insn-00bef2f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef170`](#insn-00bef170) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef174`](#insn-00bef174) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef178`](#insn-00bef178) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef180`](#insn-00bef180) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef184`](#insn-00bef184) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef18c`](#insn-00bef18c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef198`](#insn-00bef198) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef19c`](#insn-00bef19c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1a0`](#insn-00bef1a0) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef1a8`](#insn-00bef1a8) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1ac`](#insn-00bef1ac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1b0`](#insn-00bef1b0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1b4`](#insn-00bef1b4) → [`00bef364`](#insn-00bef364) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1b8`](#insn-00bef1b8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1bc`](#insn-00bef1bc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1c0`](#insn-00bef1c0) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef1c8`](#insn-00bef1c8) → [`00bef1fc`](#insn-00bef1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1cc`](#insn-00bef1cc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1d0`](#insn-00bef1d0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1dc`](#insn-00bef1dc) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef1e8`](#insn-00bef1e8) → [`00bef1fc`](#insn-00bef1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1ec`](#insn-00bef1ec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef1f4`](#insn-00bef1f4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef204`](#insn-00bef204) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef210`](#insn-00bef210) → [`00bef244`](#insn-00bef244) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef21c`](#insn-00bef21c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef228`](#insn-00bef228) → [`00bef3c8`](#insn-00bef3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef240`](#insn-00bef240) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef24c`](#insn-00bef24c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef250`](#insn-00bef250) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef254`](#insn-00bef254) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef25c`](#insn-00bef25c) → [`00bef22c`](#insn-00bef22c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef260`](#insn-00bef260) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef270`](#insn-00bef270) → [`00bef214`](#insn-00bef214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef278`](#insn-00bef278) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef280`](#insn-00bef280) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef284`](#insn-00bef284) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef288`](#insn-00bef288) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef290`](#insn-00bef290) → [`00bef268`](#insn-00bef268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef298`](#insn-00bef298) → [`00bef218`](#insn-00bef218) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef29c`](#insn-00bef29c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2a0`](#insn-00bef2a0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2a4`](#insn-00bef2a4) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef2ac`](#insn-00bef2ac) → [`00bef2f0`](#insn-00bef2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2b0`](#insn-00bef2b0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2b4`](#insn-00bef2b4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2bc`](#insn-00bef2bc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2c4`](#insn-00bef2c4) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef2c8`](#insn-00bef2c8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2cc`](#insn-00bef2cc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2d8`](#insn-00bef2d8) → [`00bef2f8`](#insn-00bef2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2dc`](#insn-00bef2dc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2e0`](#insn-00bef2e0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2ec`](#insn-00bef2ec) → [`00bef2f8`](#insn-00bef2f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2f0`](#insn-00bef2f0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2f4`](#insn-00bef2f4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef2fc`](#insn-00bef2fc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef300`](#insn-00bef300) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef304`](#insn-00bef304) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef30c`](#insn-00bef30c) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef310`](#insn-00bef310) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef318`](#insn-00bef318) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef328`](#insn-00bef328) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef32c`](#insn-00bef32c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef330`](#insn-00bef330) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef338`](#insn-00bef338) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef340`](#insn-00bef340) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef344`](#insn-00bef344) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef34c`](#insn-00bef34c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef350`](#insn-00bef350) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef358`](#insn-00bef358) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef35c`](#insn-00bef35c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef360`](#insn-00bef360) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef36c`](#insn-00bef36c) → [`00bef3ac`](#insn-00bef3ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef370`](#insn-00bef370) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef374`](#insn-00bef374) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef380`](#insn-00bef380) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef384`](#insn-00bef384) → [`00c53464`](../00c53/00c53464.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53464` · 推定シンボル `None` · 推定型 `None`
- [`00bef38c`](#insn-00bef38c) → [`00bef3a8`](#insn-00bef3a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef390`](#insn-00bef390) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef398`](#insn-00bef398) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3a4`](#insn-00bef3a4) → [`00bef3ac`](#insn-00bef3ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3ac`](#insn-00bef3ac) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3b0`](#insn-00bef3b0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3b4`](#insn-00bef3b4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3b8`](#insn-00bef3b8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bef3d4`](#insn-00bef3d4) → [`00bef3ac`](#insn-00bef3ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beefc4`](#insn-00beefc4)

~~~json
{
  "source": "00beefc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefc8`](#insn-00beefc8)

~~~json
{
  "source": "00beefc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefcc`](#insn-00beefcc)

~~~json
{
  "source": "00beefcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefd0`](#insn-00beefd0)

~~~json
{
  "source": "00beefd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beefec`](#insn-00beefec)

~~~json
{
  "source": "00beefec",
  "target": "00bef02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeff0`](#insn-00beeff0)

~~~json
{
  "source": "00beeff0",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeff8`](#insn-00beeff8)

~~~json
{
  "source": "00beeff8",
  "target": "00bef09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef004`](#insn-00bef004)

~~~json
{
  "source": "00bef004",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef008`](#insn-00bef008)

~~~json
{
  "source": "00bef008",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef00c`](#insn-00bef00c)

~~~json
{
  "source": "00bef00c",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef014`](#insn-00bef014)

~~~json
{
  "source": "00bef014",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef018`](#insn-00bef018)

~~~json
{
  "source": "00bef018",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef024`](#insn-00bef024)

~~~json
{
  "source": "00bef024",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef028`](#insn-00bef028)

~~~json
{
  "source": "00bef028",
  "target": "00bef3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef030`](#insn-00bef030)

~~~json
{
  "source": "00bef030",
  "target": "00bef060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef038`](#insn-00bef038)

~~~json
{
  "source": "00bef038",
  "target": "00bef0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef040`](#insn-00bef040)

~~~json
{
  "source": "00bef040",
  "target": "00bef09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef058`](#insn-00bef058)

~~~json
{
  "source": "00bef058",
  "target": "00bef3d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef05c`](#insn-00bef05c)

~~~json
{
  "source": "00bef05c",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef068`](#insn-00bef068)

~~~json
{
  "source": "00bef068",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef06c`](#insn-00bef06c)

~~~json
{
  "source": "00bef06c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef070`](#insn-00bef070)

~~~json
{
  "source": "00bef070",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef074`](#insn-00bef074)

~~~json
{
  "source": "00bef074",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef078`](#insn-00bef078)

~~~json
{
  "source": "00bef078",
  "target": "00bef170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef07c`](#insn-00bef07c)

~~~json
{
  "source": "00bef07c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef080`](#insn-00bef080)

~~~json
{
  "source": "00bef080",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef084`](#insn-00bef084)

~~~json
{
  "source": "00bef084",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef08c`](#insn-00bef08c)

~~~json
{
  "source": "00bef08c",
  "target": "00bef370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef090`](#insn-00bef090)

~~~json
{
  "source": "00bef090",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef098`](#insn-00bef098)

~~~json
{
  "source": "00bef098",
  "target": "00bef398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0ac`](#insn-00bef0ac)

~~~json
{
  "source": "00bef0ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0b4`](#insn-00bef0b4)

~~~json
{
  "source": "00bef0b4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0b8`](#insn-00bef0b8)

~~~json
{
  "source": "00bef0b8",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef0bc`](#insn-00bef0bc)

~~~json
{
  "source": "00bef0bc",
  "target": "00bef1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0c0`](#insn-00bef0c0)

~~~json
{
  "source": "00bef0c0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0c4`](#insn-00bef0c4)

~~~json
{
  "source": "00bef0c4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0c8`](#insn-00bef0c8)

~~~json
{
  "source": "00bef0c8",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef0d4`](#insn-00bef0d4)

~~~json
{
  "source": "00bef0d4",
  "target": "00bef1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0d8`](#insn-00bef0d8)

~~~json
{
  "source": "00bef0d8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0e0`](#insn-00bef0e0)

~~~json
{
  "source": "00bef0e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0e4`](#insn-00bef0e4)

~~~json
{
  "source": "00bef0e4",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef0f4`](#insn-00bef0f4)

~~~json
{
  "source": "00bef0f4",
  "target": "00bef1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef0f8`](#insn-00bef0f8)

~~~json
{
  "source": "00bef0f8",
  "target": "00bef1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef10c`](#insn-00bef10c)

~~~json
{
  "source": "00bef10c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef114`](#insn-00bef114)

~~~json
{
  "source": "00bef114",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef118`](#insn-00bef118)

~~~json
{
  "source": "00bef118",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef11c`](#insn-00bef11c)

~~~json
{
  "source": "00bef11c",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef120`](#insn-00bef120)

~~~json
{
  "source": "00bef120",
  "target": "00bef29c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef124`](#insn-00bef124)

~~~json
{
  "source": "00bef124",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef128`](#insn-00bef128)

~~~json
{
  "source": "00bef128",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef12c`](#insn-00bef12c)

~~~json
{
  "source": "00bef12c",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef130`](#insn-00bef130)

~~~json
{
  "source": "00bef130",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef140`](#insn-00bef140)

~~~json
{
  "source": "00bef140",
  "target": "00bef2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef144`](#insn-00bef144)

~~~json
{
  "source": "00bef144",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef14c`](#insn-00bef14c)

~~~json
{
  "source": "00bef14c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef150`](#insn-00bef150)

~~~json
{
  "source": "00bef150",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef154`](#insn-00bef154)

~~~json
{
  "source": "00bef154",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef168`](#insn-00bef168)

~~~json
{
  "source": "00bef168",
  "target": "00bef2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef16c`](#insn-00bef16c)

~~~json
{
  "source": "00bef16c",
  "target": "00bef2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef170`](#insn-00bef170)

~~~json
{
  "source": "00bef170",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef174`](#insn-00bef174)

~~~json
{
  "source": "00bef174",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef178`](#insn-00bef178)

~~~json
{
  "source": "00bef178",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef180`](#insn-00bef180)

~~~json
{
  "source": "00bef180",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef184`](#insn-00bef184)

~~~json
{
  "source": "00bef184",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef18c`](#insn-00bef18c)

~~~json
{
  "source": "00bef18c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef198`](#insn-00bef198)

~~~json
{
  "source": "00bef198",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef19c`](#insn-00bef19c)

~~~json
{
  "source": "00bef19c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1a0`](#insn-00bef1a0)

~~~json
{
  "source": "00bef1a0",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef1a8`](#insn-00bef1a8)

~~~json
{
  "source": "00bef1a8",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1ac`](#insn-00bef1ac)

~~~json
{
  "source": "00bef1ac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1b0`](#insn-00bef1b0)

~~~json
{
  "source": "00bef1b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1b4`](#insn-00bef1b4)

~~~json
{
  "source": "00bef1b4",
  "target": "00bef364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1b8`](#insn-00bef1b8)

~~~json
{
  "source": "00bef1b8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1bc`](#insn-00bef1bc)

~~~json
{
  "source": "00bef1bc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1c0`](#insn-00bef1c0)

~~~json
{
  "source": "00bef1c0",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef1c8`](#insn-00bef1c8)

~~~json
{
  "source": "00bef1c8",
  "target": "00bef1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1cc`](#insn-00bef1cc)

~~~json
{
  "source": "00bef1cc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1d0`](#insn-00bef1d0)

~~~json
{
  "source": "00bef1d0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1dc`](#insn-00bef1dc)

~~~json
{
  "source": "00bef1dc",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef1e8`](#insn-00bef1e8)

~~~json
{
  "source": "00bef1e8",
  "target": "00bef1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1ec`](#insn-00bef1ec)

~~~json
{
  "source": "00bef1ec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef1f4`](#insn-00bef1f4)

~~~json
{
  "source": "00bef1f4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef204`](#insn-00bef204)

~~~json
{
  "source": "00bef204",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef210`](#insn-00bef210)

~~~json
{
  "source": "00bef210",
  "target": "00bef244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef21c`](#insn-00bef21c)

~~~json
{
  "source": "00bef21c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef228`](#insn-00bef228)

~~~json
{
  "source": "00bef228",
  "target": "00bef3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef240`](#insn-00bef240)

~~~json
{
  "source": "00bef240",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef24c`](#insn-00bef24c)

~~~json
{
  "source": "00bef24c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef250`](#insn-00bef250)

~~~json
{
  "source": "00bef250",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef254`](#insn-00bef254)

~~~json
{
  "source": "00bef254",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef25c`](#insn-00bef25c)

~~~json
{
  "source": "00bef25c",
  "target": "00bef22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef260`](#insn-00bef260)

~~~json
{
  "source": "00bef260",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef270`](#insn-00bef270)

~~~json
{
  "source": "00bef270",
  "target": "00bef214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef278`](#insn-00bef278)

~~~json
{
  "source": "00bef278",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef280`](#insn-00bef280)

~~~json
{
  "source": "00bef280",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef284`](#insn-00bef284)

~~~json
{
  "source": "00bef284",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef288`](#insn-00bef288)

~~~json
{
  "source": "00bef288",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef290`](#insn-00bef290)

~~~json
{
  "source": "00bef290",
  "target": "00bef268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef298`](#insn-00bef298)

~~~json
{
  "source": "00bef298",
  "target": "00bef218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef29c`](#insn-00bef29c)

~~~json
{
  "source": "00bef29c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2a0`](#insn-00bef2a0)

~~~json
{
  "source": "00bef2a0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2a4`](#insn-00bef2a4)

~~~json
{
  "source": "00bef2a4",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef2ac`](#insn-00bef2ac)

~~~json
{
  "source": "00bef2ac",
  "target": "00bef2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2b0`](#insn-00bef2b0)

~~~json
{
  "source": "00bef2b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2b4`](#insn-00bef2b4)

~~~json
{
  "source": "00bef2b4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2bc`](#insn-00bef2bc)

~~~json
{
  "source": "00bef2bc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2c4`](#insn-00bef2c4)

~~~json
{
  "source": "00bef2c4",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef2c8`](#insn-00bef2c8)

~~~json
{
  "source": "00bef2c8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2cc`](#insn-00bef2cc)

~~~json
{
  "source": "00bef2cc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2d8`](#insn-00bef2d8)

~~~json
{
  "source": "00bef2d8",
  "target": "00bef2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2dc`](#insn-00bef2dc)

~~~json
{
  "source": "00bef2dc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2e0`](#insn-00bef2e0)

~~~json
{
  "source": "00bef2e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2ec`](#insn-00bef2ec)

~~~json
{
  "source": "00bef2ec",
  "target": "00bef2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2f0`](#insn-00bef2f0)

~~~json
{
  "source": "00bef2f0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2f4`](#insn-00bef2f4)

~~~json
{
  "source": "00bef2f4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef2fc`](#insn-00bef2fc)

~~~json
{
  "source": "00bef2fc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef300`](#insn-00bef300)

~~~json
{
  "source": "00bef300",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef304`](#insn-00bef304)

~~~json
{
  "source": "00bef304",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef30c`](#insn-00bef30c)

~~~json
{
  "source": "00bef30c",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef310`](#insn-00bef310)

~~~json
{
  "source": "00bef310",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef318`](#insn-00bef318)

~~~json
{
  "source": "00bef318",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef328`](#insn-00bef328)

~~~json
{
  "source": "00bef328",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef32c`](#insn-00bef32c)

~~~json
{
  "source": "00bef32c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef330`](#insn-00bef330)

~~~json
{
  "source": "00bef330",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef338`](#insn-00bef338)

~~~json
{
  "source": "00bef338",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef340`](#insn-00bef340)

~~~json
{
  "source": "00bef340",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef344`](#insn-00bef344)

~~~json
{
  "source": "00bef344",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef34c`](#insn-00bef34c)

~~~json
{
  "source": "00bef34c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef350`](#insn-00bef350)

~~~json
{
  "source": "00bef350",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef358`](#insn-00bef358)

~~~json
{
  "source": "00bef358",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef35c`](#insn-00bef35c)

~~~json
{
  "source": "00bef35c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef360`](#insn-00bef360)

~~~json
{
  "source": "00bef360",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef36c`](#insn-00bef36c)

~~~json
{
  "source": "00bef36c",
  "target": "00bef3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef370`](#insn-00bef370)

~~~json
{
  "source": "00bef370",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef374`](#insn-00bef374)

~~~json
{
  "source": "00bef374",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef380`](#insn-00bef380)

~~~json
{
  "source": "00bef380",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef384`](#insn-00bef384)

~~~json
{
  "source": "00bef384",
  "target": "00c53464",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bef38c`](#insn-00bef38c)

~~~json
{
  "source": "00bef38c",
  "target": "00bef3a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef390`](#insn-00bef390)

~~~json
{
  "source": "00bef390",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef398`](#insn-00bef398)

~~~json
{
  "source": "00bef398",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3a4`](#insn-00bef3a4)

~~~json
{
  "source": "00bef3a4",
  "target": "00bef3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3ac`](#insn-00bef3ac)

~~~json
{
  "source": "00bef3ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3b0`](#insn-00bef3b0)

~~~json
{
  "source": "00bef3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3b4`](#insn-00bef3b4)

~~~json
{
  "source": "00bef3b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3b8`](#insn-00bef3b8)

~~~json
{
  "source": "00bef3b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bef3d4`](#insn-00bef3d4)

~~~json
{
  "source": "00bef3d4",
  "target": "00bef3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
