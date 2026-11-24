# 00beffb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beefbc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-9c0d6da22fed632bc8792a5d87d095a5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beffb0",
  "name": "FUN_00beffb0",
  "size": 1052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02ceca23a4c1f4809972bbd5acd4907f6f39a3fd1a148b2f10f3d925d5eb7712",
  "source_text_sha256": "02ceca23a4c1f4809972bbd5acd4907f6f39a3fd1a148b2f10f3d925d5eb7712",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beffb0",
        "00bf03cb"
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

- [00be96e8](../00be9/00be96e8.md)

## 呼び出し先

- [00bf03cc](../00bf0/00bf03cc.md)
- [00c54458](../00c54/00c54458.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7856 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

bool FUN_00beffb0(undefined8 *param_1,undefined8 *param_2)

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
      iVar2 = FUN_00c54458();
      if (-1 < iVar2) {
        return true;
      }
      param_1[1] = uVar13;
      *param_1 = uVar11;
LAB_00bf0394:
      param_2[-1] = uVar17;
      param_2[-2] = uVar14;
      return true;
    }
  }
  else {
                    /* try { // try from 00bf0024 to 00cf002f has its CatchHandler @ 00bf007c */
    if (uVar4 == 3) {
      uVar17 = param_1[1];
      uVar14 = *param_1;
      uVar13 = param_1[3];
      uVar11 = param_1[2];
      uVar18 = param_2[-1];
      uVar16 = param_2[-2];
      iVar2 = FUN_00c54458();
      if (iVar2 < 0) {
        iVar2 = FUN_00c54458(uVar16,uVar11);
                    /* catch() { ... } // from try @ 00bf0024 with catch @ 00bf007c */
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
          iVar2 = FUN_00c54458();
          if (-1 < iVar2) {
            return true;
          }
          param_1[3] = uVar13;
          param_1[2] = uVar11;
        }
        goto LAB_00bf0394;
      }
      iVar2 = FUN_00c54458(uVar16,uVar11);
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
      iVar2 = FUN_00c54458();
      goto joined_r0x00bf019c;
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
      iVar2 = FUN_00c54458(uVar11,uVar16);
      puVar7 = param_1;
      local_50 = uVar13;
      uStack_48 = uVar17;
      if (iVar2 < 0) {
        iVar2 = FUN_00c54458(uVar13,uVar11);
        puVar8 = puVar9;
        uVar12 = uVar16;
        uVar15 = uVar18;
        if (-1 < iVar2) {
          param_1[1] = uVar14;
          *param_1 = uVar11;
          param_1[3] = uVar18;
          param_1[2] = uVar16;
          iVar2 = FUN_00c54458(uVar13,uVar16);
          puVar7 = puVar5;
          if (-1 < iVar2) goto LAB_00bf02ec;
        }
LAB_00bf02d0:
                    /* try { // try from 00bf02d4 to 00cf02df has its CatchHandler @ 00bf0774 */
        puVar8[1] = uVar18;
        *puVar8 = uVar16;
        puVar7[1] = uVar17;
        *puVar7 = uVar13;
        local_50 = uVar12;
        uStack_48 = uVar15;
      }
      else {
        iVar2 = FUN_00c54458(uVar13,uVar11);
        if (iVar2 < 0) {
          param_1[5] = uVar14;
          *puVar9 = uVar11;
          param_1[3] = uVar17;
          *puVar5 = uVar13;
          iVar2 = FUN_00c54458(uVar13,uVar16);
          puVar8 = puVar5;
          uVar12 = uVar11;
          uVar15 = uVar14;
          local_50 = uVar11;
          uStack_48 = uVar14;
          if (iVar2 < 0) goto LAB_00bf02d0;
        }
      }
LAB_00bf02ec:
      uVar14 = param_2[-1];
      uVar11 = param_2[-2];
                    /* try { // try from 00bf02f8 to 00cf031b has its CatchHandler @ 00bf07ac */
      iVar2 = FUN_00c54458(uVar11,local_50);
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
      iVar2 = FUN_00c54458();
      if (-1 < iVar2) {
        return true;
      }
                    /* try { // try from 00bf0330 to 00cf0337 has its CatchHandler @ 00bf076c */
      uVar17 = param_1[1];
      uVar13 = *param_1;
      param_1[3] = uVar14;
      param_1[2] = uVar11;
      param_1[5] = uVar18;
      param_1[4] = uVar16;
      iVar2 = FUN_00c54458();
                    /* try { // try from 00bf034c to 00cf03ab has its CatchHandler @ 00bf07fc */
joined_r0x00bf019c:
      if (iVar2 < 0) {
        param_1[1] = uVar14;
        *param_1 = uVar11;
        param_1[3] = uVar17;
        param_1[2] = uVar13;
        return true;
      }
      return true;
    }
                    /* try { // try from 00bf0030 to 00cf00cb has its CatchHandler @ 00beff88 */
    if (uVar4 == 5) {
      FUN_00bf03cc(param_1,param_1 + 2,param_1 + 4,param_1 + 6,param_2 + -2);
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
  iVar2 = FUN_00c54458(uVar16);
  puVar7 = param_1;
  if (iVar2 < 0) {
    iVar2 = FUN_00c54458(uVar11,uVar16);
    puVar8 = puVar5;
    if (-1 < iVar2) {
      param_1[1] = uVar18;
      *param_1 = uVar16;
      param_1[3] = uVar17;
      param_1[2] = uVar13;
      iVar2 = FUN_00c54458(uVar11);
      puVar7 = puVar9;
      goto joined_r0x00bf01dc;
    }
  }
  else {
    iVar2 = FUN_00c54458(uVar11,uVar16);
    if (-1 < iVar2) goto LAB_00bf01f0;
    param_1[3] = uVar14;
    *puVar9 = uVar11;
    param_1[5] = uVar18;
    *puVar5 = uVar16;
    iVar2 = FUN_00c54458(uVar11,uVar13);
    puVar8 = puVar9;
joined_r0x00bf01dc:
                    /* try { // try from 00bf01dc to 00cf02d3 has its CatchHandler @ 00bf01dc
                       catch() { ... } // from try @ 00bf01dc with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf03ac with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf05a0 with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf068c with catch @ 00bf01dc */
    if (-1 < iVar2) goto LAB_00bf01f0;
  }
  puVar7[1] = uVar14;
  *puVar7 = uVar11;
  puVar8[1] = uVar17;
  *puVar8 = uVar13;
LAB_00bf01f0:
  if (param_1 + 6 != param_2) {
    iVar2 = 0;
    lVar10 = 0x30;
    puVar9 = param_1 + 6;
    do {
      uVar13 = puVar9[1];
      uVar11 = *puVar9;
      uVar17 = puVar5[1];
      uVar14 = *puVar5;
      iVar3 = FUN_00c54458();
      lVar6 = lVar10;
      if (iVar3 < 0) {
        do {
          lVar1 = lVar6 + -0x10;
          ((undefined8 *)((long)param_1 + lVar6))[1] = uVar17;
          *(undefined8 *)((long)param_1 + lVar6) = uVar14;
          puVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bf020c;
          uVar17 = *(undefined8 *)((long)param_1 + lVar6 + -0x18);
          uVar14 = *(undefined8 *)((long)param_1 + lVar6 + -0x20);
          iVar3 = FUN_00c54458(uVar11);
          lVar6 = lVar1;
        } while (iVar3 < 0);
        puVar5 = (undefined8 *)((long)param_1 + lVar1);
LAB_00bf020c:
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
                    /* try { // try from 00bf03ac to 00cf0517 has its CatchHandler @ 00bf01dc */
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beffb0"></a> `00beffb0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beffb4"></a> `00beffb4` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00beffb8"></a> `00beffb8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00beffbc"></a> `00beffbc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00beffc0"></a> `00beffc0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00beffc4"></a> `00beffc4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00beffc8"></a> `00beffc8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00beffcc"></a> `00beffcc` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beffd0"></a> `00beffd0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00beffd4"></a> `00beffd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00beffd8"></a> `00beffd8` | `08 fd 44 93` | asr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beffdc"></a> `00beffdc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beffe0"></a> `00beffe0` | `0c 02 00 54` | b.gt 0x00bf0020 | `CONDITIONAL_JUMP`
<a id="insn-00beffe4"></a> `00beffe4` | `c3 1d 00 54` | b.cc 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00beffe8"></a> `00beffe8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beffec"></a> `00beffec` | `21 05 00 54` | b.ne 0x00bf0090 | `CONDITIONAL_JUMP`
<a id="insn-00befff0"></a> `00befff0` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00befff4"></a> `00befff4` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00befff8"></a> `00befff8` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befffc"></a> `00befffc` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0000"></a> `00bf0000` | `16 91 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0004"></a> `00bf0004` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0008"></a> `00bf0008` | `aa 1c 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf000c"></a> `00bf000c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0010"></a> `00bf0010` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0014"></a> `00bf0014` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf0018"></a> `00bf0018` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf001c"></a> `00bf001c` | `de 00 00 14` | b 0x00bf0394 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0020"></a> `00bf0020` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bf0024"></a> `00bf0024` | `80 01 00 54` | b.eq 0x00bf0054 | `CONDITIONAL_JUMP`
<a id="insn-00bf0028"></a> `00bf0028` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bf002c"></a> `00bf002c` | `20 06 00 54` | b.eq 0x00bf00f0 | `CONDITIONAL_JUMP`
<a id="insn-00bf0030"></a> `00bf0030` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bf0034"></a> `00bf0034` | `e1 02 00 54` | b.ne 0x00bf0090 | `CONDITIONAL_JUMP`
<a id="insn-00bf0038"></a> `00bf0038` | `84 42 00 d1` | sub x4,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bf003c"></a> `00bf003c` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bf0040"></a> `00bf0040` | `62 82 00 91` | add x2,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bf0044"></a> `00bf0044` | `63 c2 00 91` | add x3,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bf0048"></a> `00bf0048` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf004c"></a> `00bf004c` | `e0 00 00 94` | bl 0x00bf03cc | `UNCONDITIONAL_CALL`
<a id="insn-00bf0050"></a> `00bf0050` | `d3 00 00 14` | b 0x00bf039c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0054"></a> `00bf0054` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf0058"></a> `00bf0058` | `82 02 df 3c` | ldur q2,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf005c"></a> `00bf005c` | `e2 07 80 3d` | str q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0060"></a> `00bf0060` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0064"></a> `00bf0064` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf0068"></a> `00bf0068` | `fc 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf006c"></a> `00bf006c` | `c0 07 f8 36` | tbz w0,#0x1f,0x00bf0164 | `CONDITIONAL_JUMP`
<a id="insn-00bf0070"></a> `00bf0070` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0074"></a> `00bf0074` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0078"></a> `00bf0078` | `f8 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf007c"></a> `00bf007c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0080"></a> `00bf0080` | `2a 17 00 54` | b.ge 0x00bf0364 | `CONDITIONAL_JUMP`
<a id="insn-00bf0084"></a> `00bf0084` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0088"></a> `00bf0088` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf008c"></a> `00bf008c` | `c0 00 00 14` | b 0x00bf038c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0090"></a> `00bf0090` | `61 0a 40 ad` | ldp q1,q2,[x19] | `FALL_THROUGH`
<a id="insn-00bf0094"></a> `00bf0094` | `75 82 00 91` | add x21,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bf0098"></a> `00bf0098` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bf009c"></a> `00bf009c` | `76 42 00 91` | add x22,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bf00a0"></a> `00bf00a0` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf00a4"></a> `00bf00a4` | `40 1c a2 4e` | mov v0.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00bf00a8"></a> `00bf00a8` | `e1 0b 00 ad` | stp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00bf00ac"></a> `00bf00ac` | `eb 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf00b0"></a> `00bf00b0` | `e0 07 f8 36` | tbz w0,#0x1f,0x00bf01ac | `CONDITIONAL_JUMP`
<a id="insn-00bf00b4"></a> `00bf00b4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf00b8"></a> `00bf00b8` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf00bc"></a> `00bf00bc` | `e7 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf00c0"></a> `00bf00c0` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bf00c4"></a> `00bf00c4` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bf00c8"></a> `00bf00c8` | `c0 08 f8 37` | tbnz w0,#0x1f,0x00bf01e0 | `CONDITIONAL_JUMP`
<a id="insn-00bf00cc"></a> `00bf00cc` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf00d0"></a> `00bf00d0` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bf00d4"></a> `00bf00d4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf00d8"></a> `00bf00d8` | `e0 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf00dc"></a> `00bf00dc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf00e0"></a> `00bf00e0` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bf00e4"></a> `00bf00e4` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bf00e8"></a> `00bf00e8` | `cb 07 00 54` | b.lt 0x00bf01e0 | `CONDITIONAL_JUMP`
<a id="insn-00bf00ec"></a> `00bf00ec` | `41 00 00 14` | b 0x00bf01f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf00f0"></a> `00bf00f0` | `62 02 40 ad` | ldp q2,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf00f4"></a> `00bf00f4` | `75 42 00 91` | add x21,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00bf00f8"></a> `00bf00f8` | `61 0a c0 3d` | ldr q1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bf00fc"></a> `00bf00fc` | `76 82 00 91` | add x22,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00bf0100"></a> `00bf0100` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0104"></a> `00bf0104` | `41 1c a2 4e` | mov v1.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00bf0108"></a> `00bf0108` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf010c"></a> `00bf010c` | `e2 03 80 3d` | str q2,[sp] | `FALL_THROUGH`
<a id="insn-00bf0110"></a> `00bf0110` | `d2 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0114"></a> `00bf0114` | `e0 0b f8 36` | tbz w0,#0x1f,0x00bf0290 | `CONDITIONAL_JUMP`
<a id="insn-00bf0118"></a> `00bf0118` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf011c"></a> `00bf011c` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0120"></a> `00bf0120` | `ce 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0124"></a> `00bf0124` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf0128"></a> `00bf0128` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bf012c"></a> `00bf012c` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bf0130"></a> `00bf0130` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bf0134"></a> `00bf0134` | `e0 0c f8 37` | tbnz w0,#0x1f,0x00bf02d0 | `CONDITIONAL_JUMP`
<a id="insn-00bf0138"></a> `00bf0138` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf013c"></a> `00bf013c` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bf0140"></a> `00bf0140` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf0144"></a> `00bf0144` | `c5 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0148"></a> `00bf0148` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf014c"></a> `00bf014c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0150"></a> `00bf0150` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bf0154"></a> `00bf0154` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bf0158"></a> `00bf0158` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bf015c"></a> `00bf015c` | `ab 0b 00 54` | b.lt 0x00bf02d0 | `CONDITIONAL_JUMP`
<a id="insn-00bf0160"></a> `00bf0160` | `61 00 00 14` | b 0x00bf02e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0164"></a> `00bf0164` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0168"></a> `00bf0168` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf016c"></a> `00bf016c` | `bb 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0170"></a> `00bf0170` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0174"></a> `00bf0174` | `4a 11 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0178"></a> `00bf0178` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf017c"></a> `00bf017c` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0180"></a> `00bf0180` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0184"></a> `00bf0184` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0188"></a> `00bf0188` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf018c"></a> `00bf018c` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0190"></a> `00bf0190` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0194"></a> `00bf0194` | `b1 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0198"></a> `00bf0198` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf019c"></a> `00bf019c` | `0a 10 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf01a0"></a> `00bf01a0` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf01a4"></a> `00bf01a4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf01a8"></a> `00bf01a8` | `6c 00 00 14` | b 0x00bf0358 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf01ac"></a> `00bf01ac` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf01b0"></a> `00bf01b0` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf01b4"></a> `00bf01b4` | `a9 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf01b8"></a> `00bf01b8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf01bc"></a> `00bf01bc` | `aa 01 00 54` | b.ge 0x00bf01f0 | `CONDITIONAL_JUMP`
<a id="insn-00bf01c0"></a> `00bf01c0` | `e1 0b 40 ad` | ldp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00bf01c4"></a> `00bf01c4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf01c8"></a> `00bf01c8` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bf01cc"></a> `00bf01cc` | `a2 02 80 3d` | str q2,[x21] | `FALL_THROUGH`
<a id="insn-00bf01d0"></a> `00bf01d0` | `a2 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf01d4"></a> `00bf01d4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bf01d8"></a> `00bf01d8` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00bf01dc"></a> `00bf01dc` | `a0 00 f8 36` | tbz w0,#0x1f,0x00bf01f0 | `CONDITIONAL_JUMP`
<a id="insn-00bf01e0"></a> `00bf01e0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf01e4"></a> `00bf01e4` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bf01e8"></a> `00bf01e8` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf01ec"></a> `00bf01ec` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00bf01f0"></a> `00bf01f0` | `76 c2 00 91` | add x22,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bf01f4"></a> `00bf01f4` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00bf01f8"></a> `00bf01f8` | `20 0d 00 54` | b.eq 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf01fc"></a> `00bf01fc` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bf0200"></a> `00bf0200` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00bf0204"></a> `00bf0204` | `0d 00 00 14` | b 0x00bf0238 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0208"></a> `00bf0208` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bf020c"></a> `00bf020c` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0210"></a> `00bf0210` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0214"></a> `00bf0214` | `ff 22 00 71` | cmp w23,#0x8 | `FALL_THROUGH`
<a id="insn-00bf0218"></a> `00bf0218` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bf021c"></a> `00bf021c` | `00 0d 00 54` | b.eq 0x00bf03bc | `CONDITIONAL_JUMP`
<a id="insn-00bf0220"></a> `00bf0220` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bf0224"></a> `00bf0224` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bf0228"></a> `00bf0228` | `18 43 00 91` | add x24,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00bf022c"></a> `00bf022c` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bf0230"></a> `00bf0230` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bf0234"></a> `00bf0234` | `40 0b 00 54` | b.eq 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0238"></a> `00bf0238` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00bf023c"></a> `00bf023c` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00bf0240"></a> `00bf0240` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0244"></a> `00bf0244` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0248"></a> `00bf0248` | `84 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf024c"></a> `00bf024c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0250"></a> `00bf0250` | `8a fe ff 54` | b.ge 0x00bf0220 | `CONDITIONAL_JUMP`
<a id="insn-00bf0254"></a> `00bf0254` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0258"></a> `00bf0258` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00bf025c"></a> `00bf025c` | `15 41 00 f1` | subs x21,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bf0260"></a> `00bf0260` | `60 6a a8 3c` | str q0,[x19,x8] | `FALL_THROUGH`
<a id="insn-00bf0264"></a> `00bf0264` | `20 fd ff 54` | b.eq 0x00bf0208 | `CONDITIONAL_JUMP`
<a id="insn-00bf0268"></a> `00bf0268` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bf026c"></a> `00bf026c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0270"></a> `00bf0270` | `01 01 de 3c` | ldur q1,[x8, #-0x20] | `FALL_THROUGH`
<a id="insn-00bf0274"></a> `00bf0274` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0278"></a> `00bf0278` | `78 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf027c"></a> `00bf027c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0280"></a> `00bf0280` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bf0284"></a> `00bf0284` | `c0 fe ff 37` | tbnz w0,#0x1f,0x00bf025c | `CONDITIONAL_JUMP`
<a id="insn-00bf0288"></a> `00bf0288` | `68 02 15 8b` | add x8,x19,x21 | `FALL_THROUGH`
<a id="insn-00bf028c"></a> `00bf028c` | `e0 ff ff 17` | b 0x00bf020c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0290"></a> `00bf0290` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0294"></a> `00bf0294` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0298"></a> `00bf0298` | `70 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf029c"></a> `00bf029c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf02a0"></a> `00bf02a0` | `2a 02 00 54` | b.ge 0x00bf02e4 | `CONDITIONAL_JUMP`
<a id="insn-00bf02a4"></a> `00bf02a4` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02a8"></a> `00bf02a8` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf02ac"></a> `00bf02ac` | `c1 02 80 3d` | str q1,[x22] | `FALL_THROUGH`
<a id="insn-00bf02b0"></a> `00bf02b0` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf02b4"></a> `00bf02b4` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00bf02b8"></a> `00bf02b8` | `68 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf02bc"></a> `00bf02bc` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf02c0"></a> `00bf02c0` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02c4"></a> `00bf02c4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bf02c8"></a> `00bf02c8` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00bf02cc"></a> `00bf02cc` | `00 01 f8 36` | tbz w0,#0x1f,0x00bf02ec | `CONDITIONAL_JUMP`
<a id="insn-00bf02d0"></a> `00bf02d0` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf02d4"></a> `00bf02d4` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02d8"></a> `00bf02d8` | `21 01 80 3d` | str q1,[x9] | `FALL_THROUGH`
<a id="insn-00bf02dc"></a> `00bf02dc` | `02 01 80 3d` | str q2,[x8] | `FALL_THROUGH`
<a id="insn-00bf02e0"></a> `00bf02e0` | `03 00 00 14` | b 0x00bf02ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bf02e4"></a> `00bf02e4` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf02e8"></a> `00bf02e8` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02ec"></a> `00bf02ec` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02f0"></a> `00bf02f0` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf02f4"></a> `00bf02f4` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf02f8"></a> `00bf02f8` | `58 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf02fc"></a> `00bf02fc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0300"></a> `00bf0300` | `ea 04 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0304"></a> `00bf0304` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0308"></a> `00bf0308` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00bf030c"></a> `00bf030c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0310"></a> `00bf0310` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0314"></a> `00bf0314` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00bf0318"></a> `00bf0318` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00bf031c"></a> `00bf031c` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0320"></a> `00bf0320` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0324"></a> `00bf0324` | `4d 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0328"></a> `00bf0328` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf032c"></a> `00bf032c` | `8a 03 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0330"></a> `00bf0330` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00bf0334"></a> `00bf0334` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0338"></a> `00bf0338` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf033c"></a> `00bf033c` | `60 8a 00 ad` | stp q0,q2,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0340"></a> `00bf0340` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0344"></a> `00bf0344` | `45 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0348"></a> `00bf0348` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf034c"></a> `00bf034c` | `8a 02 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0350"></a> `00bf0350` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0354"></a> `00bf0354` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0358"></a> `00bf0358` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf035c"></a> `00bf035c` | `61 02 00 ad` | stp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00bf0360"></a> `00bf0360` | `10 00 00 14` | b 0x00bf03a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0364"></a> `00bf0364` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0368"></a> `00bf0368` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00bf036c"></a> `00bf036c` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00bf0370"></a> `00bf0370` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0374"></a> `00bf0374` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0378"></a> `00bf0378` | `38 90 01 94` | bl 0x00c54458 | `UNCONDITIONAL_CALL`
<a id="insn-00bf037c"></a> `00bf037c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00bf0380"></a> `00bf0380` | `ea 00 00 54` | b.ge 0x00bf039c | `CONDITIONAL_JUMP`
<a id="insn-00bf0384"></a> `00bf0384` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0388"></a> `00bf0388` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf038c"></a> `00bf038c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bf0390"></a> `00bf0390` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0394"></a> `00bf0394` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00bf0398"></a> `00bf0398` | `02 00 00 14` | b 0x00bf03a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf039c"></a> `00bf039c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bf03a0"></a> `00bf03a0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf03a4"></a> `00bf03a4` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf03a8"></a> `00bf03a8` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf03ac"></a> `00bf03ac` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf03b0"></a> `00bf03b0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf03b4"></a> `00bf03b4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf03b8"></a> `00bf03b8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf03bc"></a> `00bf03bc` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bf03c0"></a> `00bf03c0` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bf03c4"></a> `00bf03c4` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bf03c8"></a> `00bf03c8` | `f6 ff ff 17` | b 0x00bf03a0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beffb0`](#insn-00beffb0) 範囲 `[['00beffb0', '00beffe3']]`
  - `CONDITIONAL_JUMP` [`00beffe0`](#insn-00beffe0) → [`00bf0020`](#insn-00bf0020)
  - `FALL_THROUGH` [`00beffe0`](#insn-00beffe0) → [`00beffe4`](#insn-00beffe4)
- ブロック [`00beffe4`](#insn-00beffe4) 範囲 `[['00beffe4', '00beffe7']]`
  - `CONDITIONAL_JUMP` [`00beffe4`](#insn-00beffe4) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00beffe4`](#insn-00beffe4) → [`00beffe8`](#insn-00beffe8)
- ブロック [`00beffe8`](#insn-00beffe8) 範囲 `[['00beffe8', '00beffef']]`
  - `CONDITIONAL_JUMP` [`00beffec`](#insn-00beffec) → [`00bf0090`](#insn-00bf0090)
  - `FALL_THROUGH` [`00beffec`](#insn-00beffec) → [`00befff0`](#insn-00befff0)
- ブロック [`00befff0`](#insn-00befff0) 範囲 `[['00befff0', '00bf000b']]`
  - `CONDITIONAL_JUMP` [`00bf0008`](#insn-00bf0008) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf0008`](#insn-00bf0008) → [`00bf000c`](#insn-00bf000c)
- ブロック [`00bf000c`](#insn-00bf000c) 範囲 `[['00bf000c', '00bf001f']]`
  - `UNCONDITIONAL_JUMP` [`00bf001c`](#insn-00bf001c) → [`00bf0394`](#insn-00bf0394)
- ブロック [`00bf0020`](#insn-00bf0020) 範囲 `[['00bf0020', '00bf0023']]`
  - `FALL_THROUGH` [`00bf0020`](#insn-00bf0020) → [`00bf0024`](#insn-00bf0024)
- ブロック [`00bf0024`](#insn-00bf0024) 範囲 `[['00bf0024', '00bf0027']]`
  - `CONDITIONAL_JUMP` [`00bf0024`](#insn-00bf0024) → [`00bf0054`](#insn-00bf0054)
  - `FALL_THROUGH` [`00bf0024`](#insn-00bf0024) → [`00bf0028`](#insn-00bf0028)
- ブロック [`00bf0028`](#insn-00bf0028) 範囲 `[['00bf0028', '00bf002f']]`
  - `CONDITIONAL_JUMP` [`00bf002c`](#insn-00bf002c) → [`00bf00f0`](#insn-00bf00f0)
  - `FALL_THROUGH` [`00bf002c`](#insn-00bf002c) → [`00bf0030`](#insn-00bf0030)
- ブロック [`00bf0030`](#insn-00bf0030) 範囲 `[['00bf0030', '00bf0037']]`
  - `CONDITIONAL_JUMP` [`00bf0034`](#insn-00bf0034) → [`00bf0090`](#insn-00bf0090)
  - `FALL_THROUGH` [`00bf0034`](#insn-00bf0034) → [`00bf0038`](#insn-00bf0038)
- ブロック [`00bf0038`](#insn-00bf0038) 範囲 `[['00bf0038', '00bf0053']]`
  - `UNCONDITIONAL_JUMP` [`00bf0050`](#insn-00bf0050) → [`00bf039c`](#insn-00bf039c)
- ブロック [`00bf0054`](#insn-00bf0054) 範囲 `[['00bf0054', '00bf006f']]`
  - `CONDITIONAL_JUMP` [`00bf006c`](#insn-00bf006c) → [`00bf0164`](#insn-00bf0164)
  - `FALL_THROUGH` [`00bf006c`](#insn-00bf006c) → [`00bf0070`](#insn-00bf0070)
- ブロック [`00bf0070`](#insn-00bf0070) 範囲 `[['00bf0070', '00bf007b']]`
  - `FALL_THROUGH` [`00bf0078`](#insn-00bf0078) → [`00bf007c`](#insn-00bf007c)
- ブロック [`00bf007c`](#insn-00bf007c) 範囲 `[['00bf007c', '00bf0083']]`
  - `CONDITIONAL_JUMP` [`00bf0080`](#insn-00bf0080) → [`00bf0364`](#insn-00bf0364)
  - `FALL_THROUGH` [`00bf0080`](#insn-00bf0080) → [`00bf0084`](#insn-00bf0084)
- ブロック [`00bf0084`](#insn-00bf0084) 範囲 `[['00bf0084', '00bf008f']]`
  - `UNCONDITIONAL_JUMP` [`00bf008c`](#insn-00bf008c) → [`00bf038c`](#insn-00bf038c)
- ブロック [`00bf0090`](#insn-00bf0090) 範囲 `[['00bf0090', '00bf00b3']]`
  - `CONDITIONAL_JUMP` [`00bf00b0`](#insn-00bf00b0) → [`00bf01ac`](#insn-00bf01ac)
  - `FALL_THROUGH` [`00bf00b0`](#insn-00bf00b0) → [`00bf00b4`](#insn-00bf00b4)
- ブロック [`00bf00b4`](#insn-00bf00b4) 範囲 `[['00bf00b4', '00bf00cb']]`
  - `CONDITIONAL_JUMP` [`00bf00c8`](#insn-00bf00c8) → [`00bf01e0`](#insn-00bf01e0)
  - `FALL_THROUGH` [`00bf00c8`](#insn-00bf00c8) → [`00bf00cc`](#insn-00bf00cc)
- ブロック [`00bf00cc`](#insn-00bf00cc) 範囲 `[['00bf00cc', '00bf00eb']]`
  - `CONDITIONAL_JUMP` [`00bf00e8`](#insn-00bf00e8) → [`00bf01e0`](#insn-00bf01e0)
  - `FALL_THROUGH` [`00bf00e8`](#insn-00bf00e8) → [`00bf00ec`](#insn-00bf00ec)
- ブロック [`00bf00ec`](#insn-00bf00ec) 範囲 `[['00bf00ec', '00bf00ef']]`
  - `UNCONDITIONAL_JUMP` [`00bf00ec`](#insn-00bf00ec) → [`00bf01f0`](#insn-00bf01f0)
- ブロック [`00bf00f0`](#insn-00bf00f0) 範囲 `[['00bf00f0', '00bf0117']]`
  - `CONDITIONAL_JUMP` [`00bf0114`](#insn-00bf0114) → [`00bf0290`](#insn-00bf0290)
  - `FALL_THROUGH` [`00bf0114`](#insn-00bf0114) → [`00bf0118`](#insn-00bf0118)
- ブロック [`00bf0118`](#insn-00bf0118) 範囲 `[['00bf0118', '00bf0137']]`
  - `CONDITIONAL_JUMP` [`00bf0134`](#insn-00bf0134) → [`00bf02d0`](#insn-00bf02d0)
  - `FALL_THROUGH` [`00bf0134`](#insn-00bf0134) → [`00bf0138`](#insn-00bf0138)
- ブロック [`00bf0138`](#insn-00bf0138) 範囲 `[['00bf0138', '00bf015f']]`
  - `CONDITIONAL_JUMP` [`00bf015c`](#insn-00bf015c) → [`00bf02d0`](#insn-00bf02d0)
  - `FALL_THROUGH` [`00bf015c`](#insn-00bf015c) → [`00bf0160`](#insn-00bf0160)
- ブロック [`00bf0160`](#insn-00bf0160) 範囲 `[['00bf0160', '00bf0163']]`
  - `UNCONDITIONAL_JUMP` [`00bf0160`](#insn-00bf0160) → [`00bf02e4`](#insn-00bf02e4)
- ブロック [`00bf0164`](#insn-00bf0164) 範囲 `[['00bf0164', '00bf0177']]`
  - `CONDITIONAL_JUMP` [`00bf0174`](#insn-00bf0174) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf0174`](#insn-00bf0174) → [`00bf0178`](#insn-00bf0178)
- ブロック [`00bf0178`](#insn-00bf0178) 範囲 `[['00bf0178', '00bf019f']]`
  - `CONDITIONAL_JUMP` [`00bf019c`](#insn-00bf019c) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf019c`](#insn-00bf019c) → [`00bf01a0`](#insn-00bf01a0)
- ブロック [`00bf01a0`](#insn-00bf01a0) 範囲 `[['00bf01a0', '00bf01ab']]`
  - `UNCONDITIONAL_JUMP` [`00bf01a8`](#insn-00bf01a8) → [`00bf0358`](#insn-00bf0358)
- ブロック [`00bf01ac`](#insn-00bf01ac) 範囲 `[['00bf01ac', '00bf01bf']]`
  - `CONDITIONAL_JUMP` [`00bf01bc`](#insn-00bf01bc) → [`00bf01f0`](#insn-00bf01f0)
  - `FALL_THROUGH` [`00bf01bc`](#insn-00bf01bc) → [`00bf01c0`](#insn-00bf01c0)
- ブロック [`00bf01c0`](#insn-00bf01c0) 範囲 `[['00bf01c0', '00bf01db']]`
  - `FALL_THROUGH` [`00bf01d8`](#insn-00bf01d8) → [`00bf01dc`](#insn-00bf01dc)
- ブロック [`00bf01dc`](#insn-00bf01dc) 範囲 `[['00bf01dc', '00bf01df']]`
  - `CONDITIONAL_JUMP` [`00bf01dc`](#insn-00bf01dc) → [`00bf01f0`](#insn-00bf01f0)
  - `FALL_THROUGH` [`00bf01dc`](#insn-00bf01dc) → [`00bf01e0`](#insn-00bf01e0)
- ブロック [`00bf01e0`](#insn-00bf01e0) 範囲 `[['00bf01e0', '00bf01ef']]`
  - `FALL_THROUGH` [`00bf01ec`](#insn-00bf01ec) → [`00bf01f0`](#insn-00bf01f0)
- ブロック [`00bf01f0`](#insn-00bf01f0) 範囲 `[['00bf01f0', '00bf01fb']]`
  - `CONDITIONAL_JUMP` [`00bf01f8`](#insn-00bf01f8) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf01f8`](#insn-00bf01f8) → [`00bf01fc`](#insn-00bf01fc)
- ブロック [`00bf01fc`](#insn-00bf01fc) 範囲 `[['00bf01fc', '00bf0207']]`
  - `UNCONDITIONAL_JUMP` [`00bf0204`](#insn-00bf0204) → [`00bf0238`](#insn-00bf0238)
- ブロック [`00bf0208`](#insn-00bf0208) 範囲 `[['00bf0208', '00bf020b']]`
  - `FALL_THROUGH` [`00bf0208`](#insn-00bf0208) → [`00bf020c`](#insn-00bf020c)
- ブロック [`00bf020c`](#insn-00bf020c) 範囲 `[['00bf020c', '00bf021f']]`
  - `CONDITIONAL_JUMP` [`00bf021c`](#insn-00bf021c) → [`00bf03bc`](#insn-00bf03bc)
  - `FALL_THROUGH` [`00bf021c`](#insn-00bf021c) → [`00bf0220`](#insn-00bf0220)
- ブロック [`00bf0220`](#insn-00bf0220) 範囲 `[['00bf0220', '00bf0237']]`
  - `CONDITIONAL_JUMP` [`00bf0234`](#insn-00bf0234) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf0234`](#insn-00bf0234) → [`00bf0238`](#insn-00bf0238)
- ブロック [`00bf0238`](#insn-00bf0238) 範囲 `[['00bf0238', '00bf0253']]`
  - `CONDITIONAL_JUMP` [`00bf0250`](#insn-00bf0250) → [`00bf0220`](#insn-00bf0220)
  - `FALL_THROUGH` [`00bf0250`](#insn-00bf0250) → [`00bf0254`](#insn-00bf0254)
- ブロック [`00bf0254`](#insn-00bf0254) 範囲 `[['00bf0254', '00bf025b']]`
  - `FALL_THROUGH` [`00bf0258`](#insn-00bf0258) → [`00bf025c`](#insn-00bf025c)
- ブロック [`00bf025c`](#insn-00bf025c) 範囲 `[['00bf025c', '00bf0267']]`
  - `CONDITIONAL_JUMP` [`00bf0264`](#insn-00bf0264) → [`00bf0208`](#insn-00bf0208)
  - `FALL_THROUGH` [`00bf0264`](#insn-00bf0264) → [`00bf0268`](#insn-00bf0268)
- ブロック [`00bf0268`](#insn-00bf0268) 範囲 `[['00bf0268', '00bf0287']]`
  - `CONDITIONAL_JUMP` [`00bf0284`](#insn-00bf0284) → [`00bf025c`](#insn-00bf025c)
  - `FALL_THROUGH` [`00bf0284`](#insn-00bf0284) → [`00bf0288`](#insn-00bf0288)
- ブロック [`00bf0288`](#insn-00bf0288) 範囲 `[['00bf0288', '00bf028f']]`
  - `UNCONDITIONAL_JUMP` [`00bf028c`](#insn-00bf028c) → [`00bf020c`](#insn-00bf020c)
- ブロック [`00bf0290`](#insn-00bf0290) 範囲 `[['00bf0290', '00bf02a3']]`
  - `CONDITIONAL_JUMP` [`00bf02a0`](#insn-00bf02a0) → [`00bf02e4`](#insn-00bf02e4)
  - `FALL_THROUGH` [`00bf02a0`](#insn-00bf02a0) → [`00bf02a4`](#insn-00bf02a4)
- ブロック [`00bf02a4`](#insn-00bf02a4) 範囲 `[['00bf02a4', '00bf02cf']]`
  - `CONDITIONAL_JUMP` [`00bf02cc`](#insn-00bf02cc) → [`00bf02ec`](#insn-00bf02ec)
  - `FALL_THROUGH` [`00bf02cc`](#insn-00bf02cc) → [`00bf02d0`](#insn-00bf02d0)
- ブロック [`00bf02d0`](#insn-00bf02d0) 範囲 `[['00bf02d0', '00bf02d3']]`
  - `FALL_THROUGH` [`00bf02d0`](#insn-00bf02d0) → [`00bf02d4`](#insn-00bf02d4)
- ブロック [`00bf02d4`](#insn-00bf02d4) 範囲 `[['00bf02d4', '00bf02e3']]`
  - `UNCONDITIONAL_JUMP` [`00bf02e0`](#insn-00bf02e0) → [`00bf02ec`](#insn-00bf02ec)
- ブロック [`00bf02e4`](#insn-00bf02e4) 範囲 `[['00bf02e4', '00bf02eb']]`
  - `FALL_THROUGH` [`00bf02e8`](#insn-00bf02e8) → [`00bf02ec`](#insn-00bf02ec)
- ブロック [`00bf02ec`](#insn-00bf02ec) 範囲 `[['00bf02ec', '00bf02f7']]`
  - `FALL_THROUGH` [`00bf02f4`](#insn-00bf02f4) → [`00bf02f8`](#insn-00bf02f8)
- ブロック [`00bf02f8`](#insn-00bf02f8) 範囲 `[['00bf02f8', '00bf0303']]`
  - `CONDITIONAL_JUMP` [`00bf0300`](#insn-00bf0300) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf0300`](#insn-00bf0300) → [`00bf0304`](#insn-00bf0304)
- ブロック [`00bf0304`](#insn-00bf0304) 範囲 `[['00bf0304', '00bf032f']]`
  - `CONDITIONAL_JUMP` [`00bf032c`](#insn-00bf032c) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf032c`](#insn-00bf032c) → [`00bf0330`](#insn-00bf0330)
- ブロック [`00bf0330`](#insn-00bf0330) 範囲 `[['00bf0330', '00bf034b']]`
  - `FALL_THROUGH` [`00bf0348`](#insn-00bf0348) → [`00bf034c`](#insn-00bf034c)
- ブロック [`00bf034c`](#insn-00bf034c) 範囲 `[['00bf034c', '00bf034f']]`
  - `CONDITIONAL_JUMP` [`00bf034c`](#insn-00bf034c) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf034c`](#insn-00bf034c) → [`00bf0350`](#insn-00bf0350)
- ブロック [`00bf0350`](#insn-00bf0350) 範囲 `[['00bf0350', '00bf0357']]`
  - `FALL_THROUGH` [`00bf0354`](#insn-00bf0354) → [`00bf0358`](#insn-00bf0358)
- ブロック [`00bf0358`](#insn-00bf0358) 範囲 `[['00bf0358', '00bf0363']]`
  - `UNCONDITIONAL_JUMP` [`00bf0360`](#insn-00bf0360) → [`00bf03a0`](#insn-00bf03a0)
- ブロック [`00bf0364`](#insn-00bf0364) 範囲 `[['00bf0364', '00bf0383']]`
  - `CONDITIONAL_JUMP` [`00bf0380`](#insn-00bf0380) → [`00bf039c`](#insn-00bf039c)
  - `FALL_THROUGH` [`00bf0380`](#insn-00bf0380) → [`00bf0384`](#insn-00bf0384)
- ブロック [`00bf0384`](#insn-00bf0384) 範囲 `[['00bf0384', '00bf038b']]`
  - `FALL_THROUGH` [`00bf0388`](#insn-00bf0388) → [`00bf038c`](#insn-00bf038c)
- ブロック [`00bf038c`](#insn-00bf038c) 範囲 `[['00bf038c', '00bf0393']]`
  - `FALL_THROUGH` [`00bf0390`](#insn-00bf0390) → [`00bf0394`](#insn-00bf0394)
- ブロック [`00bf0394`](#insn-00bf0394) 範囲 `[['00bf0394', '00bf039b']]`
  - `UNCONDITIONAL_JUMP` [`00bf0398`](#insn-00bf0398) → [`00bf03a0`](#insn-00bf03a0)
- ブロック [`00bf039c`](#insn-00bf039c) 範囲 `[['00bf039c', '00bf039f']]`
  - `FALL_THROUGH` [`00bf039c`](#insn-00bf039c) → [`00bf03a0`](#insn-00bf03a0)
- ブロック [`00bf03a0`](#insn-00bf03a0) 範囲 `[['00bf03a0', '00bf03ab']]`
  - `FALL_THROUGH` [`00bf03a8`](#insn-00bf03a8) → [`00bf03ac`](#insn-00bf03ac)
- ブロック [`00bf03ac`](#insn-00bf03ac) 範囲 `[['00bf03ac', '00bf03bb']]`
- ブロック [`00bf03bc`](#insn-00bf03bc) 範囲 `[['00bf03bc', '00bf03cb']]`
  - `UNCONDITIONAL_JUMP` [`00bf03c8`](#insn-00bf03c8) → [`00bf03a0`](#insn-00bf03a0)

## 命令位置別の参照

- [`00beffb8`](#insn-00beffb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffbc`](#insn-00beffbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffc0`](#insn-00beffc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffc4`](#insn-00beffc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffe0`](#insn-00beffe0) → [`00bf0020`](#insn-00bf0020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffe4`](#insn-00beffe4) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beffec`](#insn-00beffec) → [`00bf0090`](#insn-00bf0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befff8`](#insn-00befff8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befffc`](#insn-00befffc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0000`](#insn-00bf0000) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0008`](#insn-00bf0008) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf000c`](#insn-00bf000c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0018`](#insn-00bf0018) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf001c`](#insn-00bf001c) → [`00bf0394`](#insn-00bf0394) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0024`](#insn-00bf0024) → [`00bf0054`](#insn-00bf0054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf002c`](#insn-00bf002c) → [`00bf00f0`](#insn-00bf00f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0034`](#insn-00bf0034) → [`00bf0090`](#insn-00bf0090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf004c`](#insn-00bf004c) → [`00bf03cc`](../00bf0/00bf03cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf03cc` · 推定シンボル `None` · 推定型 `None`
- [`00bf0050`](#insn-00bf0050) → [`00bf039c`](#insn-00bf039c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf005c`](#insn-00bf005c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0060`](#insn-00bf0060) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0064`](#insn-00bf0064) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0068`](#insn-00bf0068) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf006c`](#insn-00bf006c) → [`00bf0164`](#insn-00bf0164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0070`](#insn-00bf0070) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0074`](#insn-00bf0074) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0078`](#insn-00bf0078) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0080`](#insn-00bf0080) → [`00bf0364`](#insn-00bf0364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0084`](#insn-00bf0084) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf008c`](#insn-00bf008c) → [`00bf038c`](#insn-00bf038c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00a0`](#insn-00bf00a0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00a8`](#insn-00bf00a8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00ac`](#insn-00bf00ac) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf00b0`](#insn-00bf00b0) → [`00bf01ac`](#insn-00bf01ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00b4`](#insn-00bf00b4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00b8`](#insn-00bf00b8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00bc`](#insn-00bf00bc) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf00c8`](#insn-00bf00c8) → [`00bf01e0`](#insn-00bf01e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00cc`](#insn-00bf00cc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00d4`](#insn-00bf00d4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00d8`](#insn-00bf00d8) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf00e8`](#insn-00bf00e8) → [`00bf01e0`](#insn-00bf01e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf00ec`](#insn-00bf00ec) → [`00bf01f0`](#insn-00bf01f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0100`](#insn-00bf0100) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0108`](#insn-00bf0108) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf010c`](#insn-00bf010c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0110`](#insn-00bf0110) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0114`](#insn-00bf0114) → [`00bf0290`](#insn-00bf0290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0118`](#insn-00bf0118) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf011c`](#insn-00bf011c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0120`](#insn-00bf0120) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0124`](#insn-00bf0124) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0134`](#insn-00bf0134) → [`00bf02d0`](#insn-00bf02d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0138`](#insn-00bf0138) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0140`](#insn-00bf0140) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0144`](#insn-00bf0144) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0148`](#insn-00bf0148) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf015c`](#insn-00bf015c) → [`00bf02d0`](#insn-00bf02d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0160`](#insn-00bf0160) → [`00bf02e4`](#insn-00bf02e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0164`](#insn-00bf0164) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0168`](#insn-00bf0168) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf016c`](#insn-00bf016c) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0174`](#insn-00bf0174) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0178`](#insn-00bf0178) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0180`](#insn-00bf0180) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf018c`](#insn-00bf018c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0190`](#insn-00bf0190) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0194`](#insn-00bf0194) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf019c`](#insn-00bf019c) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01a0`](#insn-00bf01a0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01a4`](#insn-00bf01a4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01a8`](#insn-00bf01a8) → [`00bf0358`](#insn-00bf0358) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01ac`](#insn-00bf01ac) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01b0`](#insn-00bf01b0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01b4`](#insn-00bf01b4) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf01bc`](#insn-00bf01bc) → [`00bf01f0`](#insn-00bf01f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01c0`](#insn-00bf01c0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01c4`](#insn-00bf01c4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01d0`](#insn-00bf01d0) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf01dc`](#insn-00bf01dc) → [`00bf01f0`](#insn-00bf01f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01e0`](#insn-00bf01e0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01e8`](#insn-00bf01e8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf01f8`](#insn-00bf01f8) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0204`](#insn-00bf0204) → [`00bf0238`](#insn-00bf0238) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0210`](#insn-00bf0210) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf021c`](#insn-00bf021c) → [`00bf03bc`](#insn-00bf03bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0234`](#insn-00bf0234) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0240`](#insn-00bf0240) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0244`](#insn-00bf0244) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0248`](#insn-00bf0248) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0250`](#insn-00bf0250) → [`00bf0220`](#insn-00bf0220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0254`](#insn-00bf0254) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0264`](#insn-00bf0264) → [`00bf0208`](#insn-00bf0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf026c`](#insn-00bf026c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0274`](#insn-00bf0274) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0278`](#insn-00bf0278) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf027c`](#insn-00bf027c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0284`](#insn-00bf0284) → [`00bf025c`](#insn-00bf025c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf028c`](#insn-00bf028c) → [`00bf020c`](#insn-00bf020c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0290`](#insn-00bf0290) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0294`](#insn-00bf0294) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0298`](#insn-00bf0298) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf02a0`](#insn-00bf02a0) → [`00bf02e4`](#insn-00bf02e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02a4`](#insn-00bf02a4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02a8`](#insn-00bf02a8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02b0`](#insn-00bf02b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02b8`](#insn-00bf02b8) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf02bc`](#insn-00bf02bc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02c0`](#insn-00bf02c0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02cc`](#insn-00bf02cc) → [`00bf02ec`](#insn-00bf02ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02d0`](#insn-00bf02d0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02d4`](#insn-00bf02d4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02e0`](#insn-00bf02e0) → [`00bf02ec`](#insn-00bf02ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02e4`](#insn-00bf02e4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02e8`](#insn-00bf02e8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02f0`](#insn-00bf02f0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02f4`](#insn-00bf02f4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf02f8`](#insn-00bf02f8) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0300`](#insn-00bf0300) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0304`](#insn-00bf0304) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf030c`](#insn-00bf030c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf031c`](#insn-00bf031c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0320`](#insn-00bf0320) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0324`](#insn-00bf0324) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf032c`](#insn-00bf032c) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0334`](#insn-00bf0334) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0338`](#insn-00bf0338) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0340`](#insn-00bf0340) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0344`](#insn-00bf0344) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf034c`](#insn-00bf034c) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0350`](#insn-00bf0350) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0354`](#insn-00bf0354) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0360`](#insn-00bf0360) → [`00bf03a0`](#insn-00bf03a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0364`](#insn-00bf0364) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0368`](#insn-00bf0368) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0374`](#insn-00bf0374) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0378`](#insn-00bf0378) → [`00c54458`](../00c54/00c54458.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54458` · 推定シンボル `None` · 推定型 `None`
- [`00bf0380`](#insn-00bf0380) → [`00bf039c`](#insn-00bf039c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0384`](#insn-00bf0384) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf038c`](#insn-00bf038c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0398`](#insn-00bf0398) → [`00bf03a0`](#insn-00bf03a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf03a0`](#insn-00bf03a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf03a4`](#insn-00bf03a4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf03a8`](#insn-00bf03a8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf03ac`](#insn-00bf03ac) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf03c8`](#insn-00bf03c8) → [`00bf03a0`](#insn-00bf03a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beffb8`](#insn-00beffb8)

~~~json
{
  "source": "00beffb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffbc`](#insn-00beffbc)

~~~json
{
  "source": "00beffbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffc0`](#insn-00beffc0)

~~~json
{
  "source": "00beffc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffc4`](#insn-00beffc4)

~~~json
{
  "source": "00beffc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffe0`](#insn-00beffe0)

~~~json
{
  "source": "00beffe0",
  "target": "00bf0020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffe4`](#insn-00beffe4)

~~~json
{
  "source": "00beffe4",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beffec`](#insn-00beffec)

~~~json
{
  "source": "00beffec",
  "target": "00bf0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befff8`](#insn-00befff8)

~~~json
{
  "source": "00befff8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befffc`](#insn-00befffc)

~~~json
{
  "source": "00befffc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0000`](#insn-00bf0000)

~~~json
{
  "source": "00bf0000",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0008`](#insn-00bf0008)

~~~json
{
  "source": "00bf0008",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf000c`](#insn-00bf000c)

~~~json
{
  "source": "00bf000c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0018`](#insn-00bf0018)

~~~json
{
  "source": "00bf0018",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf001c`](#insn-00bf001c)

~~~json
{
  "source": "00bf001c",
  "target": "00bf0394",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0024`](#insn-00bf0024)

~~~json
{
  "source": "00bf0024",
  "target": "00bf0054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf002c`](#insn-00bf002c)

~~~json
{
  "source": "00bf002c",
  "target": "00bf00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0034`](#insn-00bf0034)

~~~json
{
  "source": "00bf0034",
  "target": "00bf0090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf004c`](#insn-00bf004c)

~~~json
{
  "source": "00bf004c",
  "target": "00bf03cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0050`](#insn-00bf0050)

~~~json
{
  "source": "00bf0050",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf005c`](#insn-00bf005c)

~~~json
{
  "source": "00bf005c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0060`](#insn-00bf0060)

~~~json
{
  "source": "00bf0060",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0064`](#insn-00bf0064)

~~~json
{
  "source": "00bf0064",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0068`](#insn-00bf0068)

~~~json
{
  "source": "00bf0068",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf006c`](#insn-00bf006c)

~~~json
{
  "source": "00bf006c",
  "target": "00bf0164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0070`](#insn-00bf0070)

~~~json
{
  "source": "00bf0070",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0074`](#insn-00bf0074)

~~~json
{
  "source": "00bf0074",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0078`](#insn-00bf0078)

~~~json
{
  "source": "00bf0078",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0080`](#insn-00bf0080)

~~~json
{
  "source": "00bf0080",
  "target": "00bf0364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0084`](#insn-00bf0084)

~~~json
{
  "source": "00bf0084",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf008c`](#insn-00bf008c)

~~~json
{
  "source": "00bf008c",
  "target": "00bf038c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00a0`](#insn-00bf00a0)

~~~json
{
  "source": "00bf00a0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00a8`](#insn-00bf00a8)

~~~json
{
  "source": "00bf00a8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00ac`](#insn-00bf00ac)

~~~json
{
  "source": "00bf00ac",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf00b0`](#insn-00bf00b0)

~~~json
{
  "source": "00bf00b0",
  "target": "00bf01ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00b4`](#insn-00bf00b4)

~~~json
{
  "source": "00bf00b4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00b8`](#insn-00bf00b8)

~~~json
{
  "source": "00bf00b8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00bc`](#insn-00bf00bc)

~~~json
{
  "source": "00bf00bc",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf00c8`](#insn-00bf00c8)

~~~json
{
  "source": "00bf00c8",
  "target": "00bf01e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00cc`](#insn-00bf00cc)

~~~json
{
  "source": "00bf00cc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00d4`](#insn-00bf00d4)

~~~json
{
  "source": "00bf00d4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00d8`](#insn-00bf00d8)

~~~json
{
  "source": "00bf00d8",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf00e8`](#insn-00bf00e8)

~~~json
{
  "source": "00bf00e8",
  "target": "00bf01e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf00ec`](#insn-00bf00ec)

~~~json
{
  "source": "00bf00ec",
  "target": "00bf01f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0100`](#insn-00bf0100)

~~~json
{
  "source": "00bf0100",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0108`](#insn-00bf0108)

~~~json
{
  "source": "00bf0108",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf010c`](#insn-00bf010c)

~~~json
{
  "source": "00bf010c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0110`](#insn-00bf0110)

~~~json
{
  "source": "00bf0110",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0114`](#insn-00bf0114)

~~~json
{
  "source": "00bf0114",
  "target": "00bf0290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0118`](#insn-00bf0118)

~~~json
{
  "source": "00bf0118",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf011c`](#insn-00bf011c)

~~~json
{
  "source": "00bf011c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0120`](#insn-00bf0120)

~~~json
{
  "source": "00bf0120",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0124`](#insn-00bf0124)

~~~json
{
  "source": "00bf0124",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0134`](#insn-00bf0134)

~~~json
{
  "source": "00bf0134",
  "target": "00bf02d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0138`](#insn-00bf0138)

~~~json
{
  "source": "00bf0138",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0140`](#insn-00bf0140)

~~~json
{
  "source": "00bf0140",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0144`](#insn-00bf0144)

~~~json
{
  "source": "00bf0144",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0148`](#insn-00bf0148)

~~~json
{
  "source": "00bf0148",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf015c`](#insn-00bf015c)

~~~json
{
  "source": "00bf015c",
  "target": "00bf02d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0160`](#insn-00bf0160)

~~~json
{
  "source": "00bf0160",
  "target": "00bf02e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0164`](#insn-00bf0164)

~~~json
{
  "source": "00bf0164",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0168`](#insn-00bf0168)

~~~json
{
  "source": "00bf0168",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf016c`](#insn-00bf016c)

~~~json
{
  "source": "00bf016c",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0174`](#insn-00bf0174)

~~~json
{
  "source": "00bf0174",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0178`](#insn-00bf0178)

~~~json
{
  "source": "00bf0178",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0180`](#insn-00bf0180)

~~~json
{
  "source": "00bf0180",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf018c`](#insn-00bf018c)

~~~json
{
  "source": "00bf018c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0190`](#insn-00bf0190)

~~~json
{
  "source": "00bf0190",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0194`](#insn-00bf0194)

~~~json
{
  "source": "00bf0194",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf019c`](#insn-00bf019c)

~~~json
{
  "source": "00bf019c",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01a0`](#insn-00bf01a0)

~~~json
{
  "source": "00bf01a0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01a4`](#insn-00bf01a4)

~~~json
{
  "source": "00bf01a4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01a8`](#insn-00bf01a8)

~~~json
{
  "source": "00bf01a8",
  "target": "00bf0358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01ac`](#insn-00bf01ac)

~~~json
{
  "source": "00bf01ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01b0`](#insn-00bf01b0)

~~~json
{
  "source": "00bf01b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01b4`](#insn-00bf01b4)

~~~json
{
  "source": "00bf01b4",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf01bc`](#insn-00bf01bc)

~~~json
{
  "source": "00bf01bc",
  "target": "00bf01f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01c0`](#insn-00bf01c0)

~~~json
{
  "source": "00bf01c0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01c4`](#insn-00bf01c4)

~~~json
{
  "source": "00bf01c4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01d0`](#insn-00bf01d0)

~~~json
{
  "source": "00bf01d0",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf01dc`](#insn-00bf01dc)

~~~json
{
  "source": "00bf01dc",
  "target": "00bf01f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01e0`](#insn-00bf01e0)

~~~json
{
  "source": "00bf01e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01e8`](#insn-00bf01e8)

~~~json
{
  "source": "00bf01e8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf01f8`](#insn-00bf01f8)

~~~json
{
  "source": "00bf01f8",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0204`](#insn-00bf0204)

~~~json
{
  "source": "00bf0204",
  "target": "00bf0238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0210`](#insn-00bf0210)

~~~json
{
  "source": "00bf0210",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf021c`](#insn-00bf021c)

~~~json
{
  "source": "00bf021c",
  "target": "00bf03bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0234`](#insn-00bf0234)

~~~json
{
  "source": "00bf0234",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0240`](#insn-00bf0240)

~~~json
{
  "source": "00bf0240",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0244`](#insn-00bf0244)

~~~json
{
  "source": "00bf0244",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0248`](#insn-00bf0248)

~~~json
{
  "source": "00bf0248",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0250`](#insn-00bf0250)

~~~json
{
  "source": "00bf0250",
  "target": "00bf0220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0254`](#insn-00bf0254)

~~~json
{
  "source": "00bf0254",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0264`](#insn-00bf0264)

~~~json
{
  "source": "00bf0264",
  "target": "00bf0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf026c`](#insn-00bf026c)

~~~json
{
  "source": "00bf026c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0274`](#insn-00bf0274)

~~~json
{
  "source": "00bf0274",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0278`](#insn-00bf0278)

~~~json
{
  "source": "00bf0278",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf027c`](#insn-00bf027c)

~~~json
{
  "source": "00bf027c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0284`](#insn-00bf0284)

~~~json
{
  "source": "00bf0284",
  "target": "00bf025c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf028c`](#insn-00bf028c)

~~~json
{
  "source": "00bf028c",
  "target": "00bf020c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0290`](#insn-00bf0290)

~~~json
{
  "source": "00bf0290",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0294`](#insn-00bf0294)

~~~json
{
  "source": "00bf0294",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0298`](#insn-00bf0298)

~~~json
{
  "source": "00bf0298",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf02a0`](#insn-00bf02a0)

~~~json
{
  "source": "00bf02a0",
  "target": "00bf02e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02a4`](#insn-00bf02a4)

~~~json
{
  "source": "00bf02a4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02a8`](#insn-00bf02a8)

~~~json
{
  "source": "00bf02a8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02b0`](#insn-00bf02b0)

~~~json
{
  "source": "00bf02b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02b8`](#insn-00bf02b8)

~~~json
{
  "source": "00bf02b8",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf02bc`](#insn-00bf02bc)

~~~json
{
  "source": "00bf02bc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02c0`](#insn-00bf02c0)

~~~json
{
  "source": "00bf02c0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02cc`](#insn-00bf02cc)

~~~json
{
  "source": "00bf02cc",
  "target": "00bf02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02d0`](#insn-00bf02d0)

~~~json
{
  "source": "00bf02d0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02d4`](#insn-00bf02d4)

~~~json
{
  "source": "00bf02d4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02e0`](#insn-00bf02e0)

~~~json
{
  "source": "00bf02e0",
  "target": "00bf02ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02e4`](#insn-00bf02e4)

~~~json
{
  "source": "00bf02e4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02e8`](#insn-00bf02e8)

~~~json
{
  "source": "00bf02e8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02f0`](#insn-00bf02f0)

~~~json
{
  "source": "00bf02f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02f4`](#insn-00bf02f4)

~~~json
{
  "source": "00bf02f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf02f8`](#insn-00bf02f8)

~~~json
{
  "source": "00bf02f8",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0300`](#insn-00bf0300)

~~~json
{
  "source": "00bf0300",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0304`](#insn-00bf0304)

~~~json
{
  "source": "00bf0304",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf030c`](#insn-00bf030c)

~~~json
{
  "source": "00bf030c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf031c`](#insn-00bf031c)

~~~json
{
  "source": "00bf031c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0320`](#insn-00bf0320)

~~~json
{
  "source": "00bf0320",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0324`](#insn-00bf0324)

~~~json
{
  "source": "00bf0324",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf032c`](#insn-00bf032c)

~~~json
{
  "source": "00bf032c",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0334`](#insn-00bf0334)

~~~json
{
  "source": "00bf0334",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0338`](#insn-00bf0338)

~~~json
{
  "source": "00bf0338",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0340`](#insn-00bf0340)

~~~json
{
  "source": "00bf0340",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0344`](#insn-00bf0344)

~~~json
{
  "source": "00bf0344",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf034c`](#insn-00bf034c)

~~~json
{
  "source": "00bf034c",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0350`](#insn-00bf0350)

~~~json
{
  "source": "00bf0350",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0354`](#insn-00bf0354)

~~~json
{
  "source": "00bf0354",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0360`](#insn-00bf0360)

~~~json
{
  "source": "00bf0360",
  "target": "00bf03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0364`](#insn-00bf0364)

~~~json
{
  "source": "00bf0364",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0368`](#insn-00bf0368)

~~~json
{
  "source": "00bf0368",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0374`](#insn-00bf0374)

~~~json
{
  "source": "00bf0374",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0378`](#insn-00bf0378)

~~~json
{
  "source": "00bf0378",
  "target": "00c54458",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0380`](#insn-00bf0380)

~~~json
{
  "source": "00bf0380",
  "target": "00bf039c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0384`](#insn-00bf0384)

~~~json
{
  "source": "00bf0384",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf038c`](#insn-00bf038c)

~~~json
{
  "source": "00bf038c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0398`](#insn-00bf0398)

~~~json
{
  "source": "00bf0398",
  "target": "00bf03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf03a0`](#insn-00bf03a0)

~~~json
{
  "source": "00bf03a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf03a4`](#insn-00bf03a4)

~~~json
{
  "source": "00bf03a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf03a8`](#insn-00bf03a8)

~~~json
{
  "source": "00bf03a8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf03ac`](#insn-00bf03ac)

~~~json
{
  "source": "00bf03ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf03c8`](#insn-00bf03c8)

~~~json
{
  "source": "00bf03c8",
  "target": "00bf03a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
