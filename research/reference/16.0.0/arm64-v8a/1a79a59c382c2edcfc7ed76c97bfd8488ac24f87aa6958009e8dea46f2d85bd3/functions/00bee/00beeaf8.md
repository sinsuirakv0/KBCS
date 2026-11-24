# 00beeaf8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0175.md#review-10f693d08acc36e4c28a95f09b14ba1c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beef20`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-292af319030447cbb838a4d952403c3f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beeaf8",
  "name": "FUN_00beeaf8",
  "size": 1052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d66c6b1ecb9443b5cae2c5c7db3bf501d7d5dc9b62f06f42c52b582eb4888859",
  "source_text_sha256": "d66c6b1ecb9443b5cae2c5c7db3bf501d7d5dc9b62f06f42c52b582eb4888859",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beeaf8",
        "00beef13"
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

- [00be8230](../00be8/00be8230.md)

## 呼び出し先

- [00beef14](../00bee/00beef14.md)
- [00c52fa0](../00c52/00c52fa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7856 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

bool FUN_00beeaf8(undefined8 *param_1,undefined8 *param_2)

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
      iVar2 = FUN_00c52fa0();
      if (-1 < iVar2) {
        return true;
      }
      param_1[1] = uVar13;
      *param_1 = uVar11;
LAB_00beeedc:
      param_2[-1] = uVar17;
      param_2[-2] = uVar14;
      return true;
    }
  }
  else {
                    /* try { // try from 00beeb6c to 00ceeb77 has its CatchHandler @ 00beebc4 */
    if (uVar4 == 3) {
      uVar17 = param_1[1];
      uVar14 = *param_1;
      uVar13 = param_1[3];
      uVar11 = param_1[2];
      uVar18 = param_2[-1];
      uVar16 = param_2[-2];
      iVar2 = FUN_00c52fa0();
      if (iVar2 < 0) {
        iVar2 = FUN_00c52fa0(uVar16,uVar11);
                    /* catch() { ... } // from try @ 00beeb6c with catch @ 00beebc4 */
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
          iVar2 = FUN_00c52fa0();
          if (-1 < iVar2) {
            return true;
          }
          param_1[3] = uVar13;
          param_1[2] = uVar11;
        }
        goto LAB_00beeedc;
      }
      iVar2 = FUN_00c52fa0(uVar16,uVar11);
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
      iVar2 = FUN_00c52fa0();
      goto joined_r0x00beece4;
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
      iVar2 = FUN_00c52fa0(uVar11,uVar16);
      puVar7 = param_1;
      local_50 = uVar13;
      uStack_48 = uVar17;
      if (iVar2 < 0) {
        iVar2 = FUN_00c52fa0(uVar13,uVar11);
        puVar8 = puVar9;
        uVar12 = uVar16;
        uVar15 = uVar18;
        if (-1 < iVar2) {
          param_1[1] = uVar14;
          *param_1 = uVar11;
          param_1[3] = uVar18;
          param_1[2] = uVar16;
          iVar2 = FUN_00c52fa0(uVar13,uVar16);
          puVar7 = puVar5;
          if (-1 < iVar2) goto LAB_00beee34;
        }
LAB_00beee18:
                    /* try { // try from 00beee1c to 00ceee27 has its CatchHandler @ 00bef2bc */
        puVar8[1] = uVar18;
        *puVar8 = uVar16;
        puVar7[1] = uVar17;
        *puVar7 = uVar13;
        local_50 = uVar12;
        uStack_48 = uVar15;
      }
      else {
        iVar2 = FUN_00c52fa0(uVar13,uVar11);
        if (iVar2 < 0) {
          param_1[5] = uVar14;
          *puVar9 = uVar11;
          param_1[3] = uVar17;
          *puVar5 = uVar13;
          iVar2 = FUN_00c52fa0(uVar13,uVar16);
          puVar8 = puVar5;
          uVar12 = uVar11;
          uVar15 = uVar14;
          local_50 = uVar11;
          uStack_48 = uVar14;
          if (iVar2 < 0) goto LAB_00beee18;
        }
      }
LAB_00beee34:
      uVar14 = param_2[-1];
      uVar11 = param_2[-2];
                    /* try { // try from 00beee40 to 00ceee63 has its CatchHandler @ 00bef2f4 */
      iVar2 = FUN_00c52fa0(uVar11,local_50);
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
      iVar2 = FUN_00c52fa0();
      if (-1 < iVar2) {
        return true;
      }
                    /* try { // try from 00beee78 to 00ceee7f has its CatchHandler @ 00bef2b4 */
      uVar17 = param_1[1];
      uVar13 = *param_1;
      param_1[3] = uVar14;
      param_1[2] = uVar11;
      param_1[5] = uVar18;
      param_1[4] = uVar16;
      iVar2 = FUN_00c52fa0();
                    /* try { // try from 00beee94 to 00ceeef3 has its CatchHandler @ 00bef344 */
joined_r0x00beece4:
      if (iVar2 < 0) {
        param_1[1] = uVar14;
        *param_1 = uVar11;
        param_1[3] = uVar17;
        param_1[2] = uVar13;
        return true;
      }
      return true;
    }
                    /* try { // try from 00beeb78 to 00ceec13 has its CatchHandler @ 00beead0 */
    if (uVar4 == 5) {
      FUN_00beef14(param_1,param_1 + 2,param_1 + 4,param_1 + 6,param_2 + -2);
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
  iVar2 = FUN_00c52fa0(uVar16);
  puVar7 = param_1;
  if (iVar2 < 0) {
    iVar2 = FUN_00c52fa0(uVar11,uVar16);
    puVar8 = puVar5;
    if (-1 < iVar2) {
      param_1[1] = uVar18;
      *param_1 = uVar16;
      param_1[3] = uVar17;
      param_1[2] = uVar13;
      iVar2 = FUN_00c52fa0(uVar11);
      puVar7 = puVar9;
      goto joined_r0x00beed24;
    }
  }
  else {
    iVar2 = FUN_00c52fa0(uVar11,uVar16);
    if (-1 < iVar2) goto LAB_00beed38;
    param_1[3] = uVar14;
    *puVar9 = uVar11;
    param_1[5] = uVar18;
    *puVar5 = uVar16;
    iVar2 = FUN_00c52fa0(uVar11,uVar13);
    puVar8 = puVar9;
joined_r0x00beed24:
                    /* try { // try from 00beed24 to 00ceee1b has its CatchHandler @ 00beed24
                       catch() { ... } // from try @ 00beed24 with catch @ 00beed24
                       catch() { ... } // from try @ 00beeef4 with catch @ 00beed24
                       catch() { ... } // from try @ 00bef0e8 with catch @ 00beed24
                       catch() { ... } // from try @ 00bef1d4 with catch @ 00beed24 */
    if (-1 < iVar2) goto LAB_00beed38;
  }
  puVar7[1] = uVar14;
  *puVar7 = uVar11;
  puVar8[1] = uVar17;
  *puVar8 = uVar13;
LAB_00beed38:
  if (param_1 + 6 != param_2) {
    iVar2 = 0;
    lVar10 = 0x30;
    puVar9 = param_1 + 6;
    do {
      uVar13 = puVar9[1];
      uVar11 = *puVar9;
      uVar17 = puVar5[1];
      uVar14 = *puVar5;
      iVar3 = FUN_00c52fa0();
      lVar6 = lVar10;
      if (iVar3 < 0) {
        do {
          lVar1 = lVar6 + -0x10;
          ((undefined8 *)((long)param_1 + lVar6))[1] = uVar17;
          *(undefined8 *)((long)param_1 + lVar6) = uVar14;
          puVar5 = param_1;
          if (lVar1 == 0) goto LAB_00beed54;
          uVar17 = *(undefined8 *)((long)param_1 + lVar6 + -0x18);
          uVar14 = *(undefined8 *)((long)param_1 + lVar6 + -0x20);
          iVar3 = FUN_00c52fa0(uVar11);
          lVar6 = lVar1;
        } while (iVar3 < 0);
        puVar5 = (undefined8 *)((long)param_1 + lVar1);
LAB_00beed54:
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
                    /* try { // try from 00beeef4 to 00cef05f has its CatchHandler @ 00beed24 */
  return true;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beeaf8"></a> `00beeaf8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00beeafc"></a> `00beeafc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00beeb00"></a> `00beeb00` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00beeb04"></a> `00beeb04` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00beeb08"></a> `00beeb08` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00beeb0c"></a> `00beeb0c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00beeb10"></a> `00beeb10` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00beeb14"></a> `00beeb14` | `28 00 00 cb` | sub x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00beeb18"></a> `00beeb18` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00beeb1c"></a> `00beeb1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00beeb20"></a> `00beeb20` | `08 fd 44 93` | asr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beeb24"></a> `00beeb24` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeb28"></a> `00beeb28` | `0c 02 00 54` | b.gt 0x00beeb68 | `CONDITIONAL_JUMP`
<a id="insn-00beeb2c"></a> `00beeb2c` | `c3 1d 00 54` | b.cc 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beeb30"></a> `00beeb30` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00beeb34"></a> `00beeb34` | `21 05 00 54` | b.ne 0x00beebd8 | `CONDITIONAL_JUMP`
<a id="insn-00beeb38"></a> `00beeb38` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeb3c"></a> `00beeb3c` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00beeb40"></a> `00beeb40` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beeb44"></a> `00beeb44` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeb48"></a> `00beeb48` | `16 91 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beeb4c"></a> `00beeb4c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beeb50"></a> `00beeb50` | `aa 1c 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beeb54"></a> `00beeb54` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beeb58"></a> `00beeb58` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beeb5c"></a> `00beeb5c` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00beeb60"></a> `00beeb60` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeb64"></a> `00beeb64` | `de 00 00 14` | b 0x00beeedc | `UNCONDITIONAL_JUMP`
<a id="insn-00beeb68"></a> `00beeb68` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00beeb6c"></a> `00beeb6c` | `80 01 00 54` | b.eq 0x00beeb9c | `CONDITIONAL_JUMP`
<a id="insn-00beeb70"></a> `00beeb70` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00beeb74"></a> `00beeb74` | `20 06 00 54` | b.eq 0x00beec38 | `CONDITIONAL_JUMP`
<a id="insn-00beeb78"></a> `00beeb78` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00beeb7c"></a> `00beeb7c` | `e1 02 00 54` | b.ne 0x00beebd8 | `CONDITIONAL_JUMP`
<a id="insn-00beeb80"></a> `00beeb80` | `84 42 00 d1` | sub x4,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00beeb84"></a> `00beeb84` | `61 42 00 91` | add x1,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00beeb88"></a> `00beeb88` | `62 82 00 91` | add x2,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00beeb8c"></a> `00beeb8c` | `63 c2 00 91` | add x3,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00beeb90"></a> `00beeb90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00beeb94"></a> `00beeb94` | `e0 00 00 94` | bl 0x00beef14 | `UNCONDITIONAL_CALL`
<a id="insn-00beeb98"></a> `00beeb98` | `d3 00 00 14` | b 0x00beeee4 | `UNCONDITIONAL_JUMP`
<a id="insn-00beeb9c"></a> `00beeb9c` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00beeba0"></a> `00beeba0` | `82 02 df 3c` | ldur q2,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeba4"></a> `00beeba4` | `e2 07 80 3d` | str q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beeba8"></a> `00beeba8` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beebac"></a> `00beebac` | `e1 03 80 3d` | str q1,[sp] | `FALL_THROUGH`
<a id="insn-00beebb0"></a> `00beebb0` | `fc 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beebb4"></a> `00beebb4` | `c0 07 f8 36` | tbz w0,#0x1f,0x00beecac | `CONDITIONAL_JUMP`
<a id="insn-00beebb8"></a> `00beebb8` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beebbc"></a> `00beebbc` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beebc0"></a> `00beebc0` | `f8 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beebc4"></a> `00beebc4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beebc8"></a> `00beebc8` | `2a 17 00 54` | b.ge 0x00beeeac | `CONDITIONAL_JUMP`
<a id="insn-00beebcc"></a> `00beebcc` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beebd0"></a> `00beebd0` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00beebd4"></a> `00beebd4` | `c0 00 00 14` | b 0x00beeed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00beebd8"></a> `00beebd8` | `61 0a 40 ad` | ldp q1,q2,[x19] | `FALL_THROUGH`
<a id="insn-00beebdc"></a> `00beebdc` | `75 82 00 91` | add x21,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00beebe0"></a> `00beebe0` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00beebe4"></a> `00beebe4` | `76 42 00 91` | add x22,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00beebe8"></a> `00beebe8` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beebec"></a> `00beebec` | `40 1c a2 4e` | mov v0.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00beebf0"></a> `00beebf0` | `e1 0b 00 ad` | stp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00beebf4"></a> `00beebf4` | `eb 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beebf8"></a> `00beebf8` | `e0 07 f8 36` | tbz w0,#0x1f,0x00beecf4 | `CONDITIONAL_JUMP`
<a id="insn-00beebfc"></a> `00beebfc` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beec00"></a> `00beec00` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beec04"></a> `00beec04` | `e7 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beec08"></a> `00beec08` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00beec0c"></a> `00beec0c` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00beec10"></a> `00beec10` | `c0 08 f8 37` | tbnz w0,#0x1f,0x00beed28 | `CONDITIONAL_JUMP`
<a id="insn-00beec14"></a> `00beec14` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00beec18"></a> `00beec18` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00beec1c"></a> `00beec1c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beec20"></a> `00beec20` | `e0 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beec24"></a> `00beec24` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beec28"></a> `00beec28` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00beec2c"></a> `00beec2c` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00beec30"></a> `00beec30` | `cb 07 00 54` | b.lt 0x00beed28 | `CONDITIONAL_JUMP`
<a id="insn-00beec34"></a> `00beec34` | `41 00 00 14` | b 0x00beed38 | `UNCONDITIONAL_JUMP`
<a id="insn-00beec38"></a> `00beec38` | `62 02 40 ad` | ldp q2,q0,[x19] | `FALL_THROUGH`
<a id="insn-00beec3c"></a> `00beec3c` | `75 42 00 91` | add x21,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00beec40"></a> `00beec40` | `61 0a c0 3d` | ldr q1,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00beec44"></a> `00beec44` | `76 82 00 91` | add x22,x19,#0x20 | `FALL_THROUGH`
<a id="insn-00beec48"></a> `00beec48` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beec4c"></a> `00beec4c` | `41 1c a2 4e` | mov v1.16B,v2.16B | `FALL_THROUGH`
<a id="insn-00beec50"></a> `00beec50` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beec54"></a> `00beec54` | `e2 03 80 3d` | str q2,[sp] | `FALL_THROUGH`
<a id="insn-00beec58"></a> `00beec58` | `d2 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beec5c"></a> `00beec5c` | `e0 0b f8 36` | tbz w0,#0x1f,0x00beedd8 | `CONDITIONAL_JUMP`
<a id="insn-00beec60"></a> `00beec60` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beec64"></a> `00beec64` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beec68"></a> `00beec68` | `ce 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beec6c"></a> `00beec6c` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00beec70"></a> `00beec70` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00beec74"></a> `00beec74` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00beec78"></a> `00beec78` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00beec7c"></a> `00beec7c` | `e0 0c f8 37` | tbnz w0,#0x1f,0x00beee18 | `CONDITIONAL_JUMP`
<a id="insn-00beec80"></a> `00beec80` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beec84"></a> `00beec84` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00beec88"></a> `00beec88` | `e1 03 40 ad` | ldp q1,q0,[sp] | `FALL_THROUGH`
<a id="insn-00beec8c"></a> `00beec8c` | `c5 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beec90"></a> `00beec90` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00beec94"></a> `00beec94` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beec98"></a> `00beec98` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00beec9c"></a> `00beec9c` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00beeca0"></a> `00beeca0` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00beeca4"></a> `00beeca4` | `ab 0b 00 54` | b.lt 0x00beee18 | `CONDITIONAL_JUMP`
<a id="insn-00beeca8"></a> `00beeca8` | `61 00 00 14` | b 0x00beee2c | `UNCONDITIONAL_JUMP`
<a id="insn-00beecac"></a> `00beecac` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beecb0"></a> `00beecb0` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beecb4"></a> `00beecb4` | `bb 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beecb8"></a> `00beecb8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beecbc"></a> `00beecbc` | `4a 11 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beecc0"></a> `00beecc0` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beecc4"></a> `00beecc4` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00beecc8"></a> `00beecc8` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeccc"></a> `00beeccc` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beecd0"></a> `00beecd0` | `61 02 40 ad` | ldp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00beecd4"></a> `00beecd4` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beecd8"></a> `00beecd8` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beecdc"></a> `00beecdc` | `b1 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beece0"></a> `00beece0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beece4"></a> `00beece4` | `0a 10 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beece8"></a> `00beece8` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beecec"></a> `00beecec` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beecf0"></a> `00beecf0` | `6c 00 00 14` | b 0x00beeea0 | `UNCONDITIONAL_JUMP`
<a id="insn-00beecf4"></a> `00beecf4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beecf8"></a> `00beecf8` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beecfc"></a> `00beecfc` | `a9 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beed00"></a> `00beed00` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beed04"></a> `00beed04` | `aa 01 00 54` | b.ge 0x00beed38 | `CONDITIONAL_JUMP`
<a id="insn-00beed08"></a> `00beed08` | `e1 0b 40 ad` | ldp q1,q2,[sp] | `FALL_THROUGH`
<a id="insn-00beed0c"></a> `00beed0c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beed10"></a> `00beed10` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00beed14"></a> `00beed14` | `a2 02 80 3d` | str q2,[x21] | `FALL_THROUGH`
<a id="insn-00beed18"></a> `00beed18` | `a2 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beed1c"></a> `00beed1c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00beed20"></a> `00beed20` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00beed24"></a> `00beed24` | `a0 00 f8 36` | tbz w0,#0x1f,0x00beed38 | `CONDITIONAL_JUMP`
<a id="insn-00beed28"></a> `00beed28` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beed2c"></a> `00beed2c` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00beed30"></a> `00beed30` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00beed34"></a> `00beed34` | `20 01 80 3d` | str q0,[x9] | `FALL_THROUGH`
<a id="insn-00beed38"></a> `00beed38` | `76 c2 00 91` | add x22,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00beed3c"></a> `00beed3c` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00beed40"></a> `00beed40` | `20 0d 00 54` | b.eq 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beed44"></a> `00beed44` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00beed48"></a> `00beed48` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00beed4c"></a> `00beed4c` | `0d 00 00 14` | b 0x00beed80 | `UNCONDITIONAL_JUMP`
<a id="insn-00beed50"></a> `00beed50` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00beed54"></a> `00beed54` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00beed58"></a> `00beed58` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beed5c"></a> `00beed5c` | `ff 22 00 71` | cmp w23,#0x8 | `FALL_THROUGH`
<a id="insn-00beed60"></a> `00beed60` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00beed64"></a> `00beed64` | `00 0d 00 54` | b.eq 0x00beef04 | `CONDITIONAL_JUMP`
<a id="insn-00beed68"></a> `00beed68` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00beed6c"></a> `00beed6c` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00beed70"></a> `00beed70` | `18 43 00 91` | add x24,x24,#0x10 | `FALL_THROUGH`
<a id="insn-00beed74"></a> `00beed74` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00beed78"></a> `00beed78` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00beed7c"></a> `00beed7c` | `40 0b 00 54` | b.eq 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beed80"></a> `00beed80` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00beed84"></a> `00beed84` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00beed88"></a> `00beed88` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beed8c"></a> `00beed8c` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beed90"></a> `00beed90` | `84 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beed94"></a> `00beed94` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beed98"></a> `00beed98` | `8a fe ff 54` | b.ge 0x00beed68 | `CONDITIONAL_JUMP`
<a id="insn-00beed9c"></a> `00beed9c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeda0"></a> `00beeda0` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00beeda4"></a> `00beeda4` | `15 41 00 f1` | subs x21,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00beeda8"></a> `00beeda8` | `60 6a a8 3c` | str q0,[x19,x8] | `FALL_THROUGH`
<a id="insn-00beedac"></a> `00beedac` | `20 fd ff 54` | b.eq 0x00beed50 | `CONDITIONAL_JUMP`
<a id="insn-00beedb0"></a> `00beedb0` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00beedb4"></a> `00beedb4` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beedb8"></a> `00beedb8` | `01 01 de 3c` | ldur q1,[x8, #-0x20] | `FALL_THROUGH`
<a id="insn-00beedbc"></a> `00beedbc` | `a1 03 9f 3c` | stur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beedc0"></a> `00beedc0` | `78 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beedc4"></a> `00beedc4` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beedc8"></a> `00beedc8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00beedcc"></a> `00beedcc` | `c0 fe ff 37` | tbnz w0,#0x1f,0x00beeda4 | `CONDITIONAL_JUMP`
<a id="insn-00beedd0"></a> `00beedd0` | `68 02 15 8b` | add x8,x19,x21 | `FALL_THROUGH`
<a id="insn-00beedd4"></a> `00beedd4` | `e0 ff ff 17` | b 0x00beed54 | `UNCONDITIONAL_JUMP`
<a id="insn-00beedd8"></a> `00beedd8` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beeddc"></a> `00beeddc` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beede0"></a> `00beede0` | `70 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beede4"></a> `00beede4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beede8"></a> `00beede8` | `2a 02 00 54` | b.ge 0x00beee2c | `CONDITIONAL_JUMP`
<a id="insn-00beedec"></a> `00beedec` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beedf0"></a> `00beedf0` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beedf4"></a> `00beedf4` | `c1 02 80 3d` | str q1,[x22] | `FALL_THROUGH`
<a id="insn-00beedf8"></a> `00beedf8` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00beedfc"></a> `00beedfc` | `a0 02 80 3d` | str q0,[x21] | `FALL_THROUGH`
<a id="insn-00beee00"></a> `00beee00` | `68 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beee04"></a> `00beee04` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00beee08"></a> `00beee08` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee0c"></a> `00beee0c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00beee10"></a> `00beee10` | `e9 03 15 aa` | mov x9,x21 | `FALL_THROUGH`
<a id="insn-00beee14"></a> `00beee14` | `00 01 f8 36` | tbz w0,#0x1f,0x00beee34 | `CONDITIONAL_JUMP`
<a id="insn-00beee18"></a> `00beee18` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee1c"></a> `00beee1c` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee20"></a> `00beee20` | `21 01 80 3d` | str q1,[x9] | `FALL_THROUGH`
<a id="insn-00beee24"></a> `00beee24` | `02 01 80 3d` | str q2,[x8] | `FALL_THROUGH`
<a id="insn-00beee28"></a> `00beee28` | `03 00 00 14` | b 0x00beee34 | `UNCONDITIONAL_JUMP`
<a id="insn-00beee2c"></a> `00beee2c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee30"></a> `00beee30` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee34"></a> `00beee34` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee38"></a> `00beee38` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee3c"></a> `00beee3c` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee40"></a> `00beee40` | `58 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beee44"></a> `00beee44` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beee48"></a> `00beee48` | `ea 04 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beee4c"></a> `00beee4c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee50"></a> `00beee50` | `c0 02 80 3d` | str q0,[x22] | `FALL_THROUGH`
<a id="insn-00beee54"></a> `00beee54` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee58"></a> `00beee58` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee5c"></a> `00beee5c` | `c0 02 c0 3d` | ldr q0,[x22] | `FALL_THROUGH`
<a id="insn-00beee60"></a> `00beee60` | `a1 02 c0 3d` | ldr q1,[x21] | `FALL_THROUGH`
<a id="insn-00beee64"></a> `00beee64` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee68"></a> `00beee68` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee6c"></a> `00beee6c` | `4d 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beee70"></a> `00beee70` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beee74"></a> `00beee74` | `8a 03 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beee78"></a> `00beee78` | `61 02 c0 3d` | ldr q1,[x19] | `FALL_THROUGH`
<a id="insn-00beee7c"></a> `00beee7c` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee80"></a> `00beee80` | `e2 07 c0 3d` | ldr q2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee84"></a> `00beee84` | `60 8a 00 ad` | stp q0,q2,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00beee88"></a> `00beee88` | `e1 07 80 3d` | str q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beee8c"></a> `00beee8c` | `45 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beee90"></a> `00beee90` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beee94"></a> `00beee94` | `8a 02 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beee98"></a> `00beee98` | `a1 03 df 3c` | ldur q1,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beee9c"></a> `00beee9c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00beeea0"></a> `00beeea0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beeea4"></a> `00beeea4` | `61 02 00 ad` | stp q1,q0,[x19] | `FALL_THROUGH`
<a id="insn-00beeea8"></a> `00beeea8` | `10 00 00 14` | b 0x00beeee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beeeac"></a> `00beeeac` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeeb0"></a> `00beeeb0` | `e1 03 c0 3d` | ldr q1,[sp] | `FALL_THROUGH`
<a id="insn-00beeeb4"></a> `00beeeb4` | `60 06 00 ad` | stp q0,q1,[x19] | `FALL_THROUGH`
<a id="insn-00beeeb8"></a> `00beeeb8` | `80 02 df 3c` | ldur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeebc"></a> `00beeebc` | `a0 03 9f 3c` | stur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeec0"></a> `00beeec0` | `38 90 01 94` | bl 0x00c52fa0 | `UNCONDITIONAL_CALL`
<a id="insn-00beeec4"></a> `00beeec4` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00beeec8"></a> `00beeec8` | `ea 00 00 54` | b.ge 0x00beeee4 | `CONDITIONAL_JUMP`
<a id="insn-00beeecc"></a> `00beeecc` | `a0 03 df 3c` | ldur q0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeed0"></a> `00beeed0` | `60 06 80 3d` | str q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00beeed4"></a> `00beeed4` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00beeed8"></a> `00beeed8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beeedc"></a> `00beeedc` | `80 02 9f 3c` | stur q0,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00beeee0"></a> `00beeee0` | `02 00 00 14` | b 0x00beeee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00beeee4"></a> `00beeee4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00beeee8"></a> `00beeee8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00beeeec"></a> `00beeeec` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00beeef0"></a> `00beeef0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00beeef4"></a> `00beeef4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00beeef8"></a> `00beeef8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00beeefc"></a> `00beeefc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00beef00"></a> `00beef00` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00beef04"></a> `00beef04` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00beef08"></a> `00beef08` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00beef0c"></a> `00beef0c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00beef10"></a> `00beef10` | `f6 ff ff 17` | b 0x00beeee8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00beeaf8`](#insn-00beeaf8) 範囲 `[['00beeaf8', '00beeb2b']]`
  - `CONDITIONAL_JUMP` [`00beeb28`](#insn-00beeb28) → [`00beeb68`](#insn-00beeb68)
  - `FALL_THROUGH` [`00beeb28`](#insn-00beeb28) → [`00beeb2c`](#insn-00beeb2c)
- ブロック [`00beeb2c`](#insn-00beeb2c) 範囲 `[['00beeb2c', '00beeb2f']]`
  - `CONDITIONAL_JUMP` [`00beeb2c`](#insn-00beeb2c) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beeb2c`](#insn-00beeb2c) → [`00beeb30`](#insn-00beeb30)
- ブロック [`00beeb30`](#insn-00beeb30) 範囲 `[['00beeb30', '00beeb37']]`
  - `CONDITIONAL_JUMP` [`00beeb34`](#insn-00beeb34) → [`00beebd8`](#insn-00beebd8)
  - `FALL_THROUGH` [`00beeb34`](#insn-00beeb34) → [`00beeb38`](#insn-00beeb38)
- ブロック [`00beeb38`](#insn-00beeb38) 範囲 `[['00beeb38', '00beeb53']]`
  - `CONDITIONAL_JUMP` [`00beeb50`](#insn-00beeb50) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beeb50`](#insn-00beeb50) → [`00beeb54`](#insn-00beeb54)
- ブロック [`00beeb54`](#insn-00beeb54) 範囲 `[['00beeb54', '00beeb67']]`
  - `UNCONDITIONAL_JUMP` [`00beeb64`](#insn-00beeb64) → [`00beeedc`](#insn-00beeedc)
- ブロック [`00beeb68`](#insn-00beeb68) 範囲 `[['00beeb68', '00beeb6b']]`
  - `FALL_THROUGH` [`00beeb68`](#insn-00beeb68) → [`00beeb6c`](#insn-00beeb6c)
- ブロック [`00beeb6c`](#insn-00beeb6c) 範囲 `[['00beeb6c', '00beeb6f']]`
  - `CONDITIONAL_JUMP` [`00beeb6c`](#insn-00beeb6c) → [`00beeb9c`](#insn-00beeb9c)
  - `FALL_THROUGH` [`00beeb6c`](#insn-00beeb6c) → [`00beeb70`](#insn-00beeb70)
- ブロック [`00beeb70`](#insn-00beeb70) 範囲 `[['00beeb70', '00beeb77']]`
  - `CONDITIONAL_JUMP` [`00beeb74`](#insn-00beeb74) → [`00beec38`](#insn-00beec38)
  - `FALL_THROUGH` [`00beeb74`](#insn-00beeb74) → [`00beeb78`](#insn-00beeb78)
- ブロック [`00beeb78`](#insn-00beeb78) 範囲 `[['00beeb78', '00beeb7f']]`
  - `CONDITIONAL_JUMP` [`00beeb7c`](#insn-00beeb7c) → [`00beebd8`](#insn-00beebd8)
  - `FALL_THROUGH` [`00beeb7c`](#insn-00beeb7c) → [`00beeb80`](#insn-00beeb80)
- ブロック [`00beeb80`](#insn-00beeb80) 範囲 `[['00beeb80', '00beeb9b']]`
  - `UNCONDITIONAL_JUMP` [`00beeb98`](#insn-00beeb98) → [`00beeee4`](#insn-00beeee4)
- ブロック [`00beeb9c`](#insn-00beeb9c) 範囲 `[['00beeb9c', '00beebb7']]`
  - `CONDITIONAL_JUMP` [`00beebb4`](#insn-00beebb4) → [`00beecac`](#insn-00beecac)
  - `FALL_THROUGH` [`00beebb4`](#insn-00beebb4) → [`00beebb8`](#insn-00beebb8)
- ブロック [`00beebb8`](#insn-00beebb8) 範囲 `[['00beebb8', '00beebc3']]`
  - `FALL_THROUGH` [`00beebc0`](#insn-00beebc0) → [`00beebc4`](#insn-00beebc4)
- ブロック [`00beebc4`](#insn-00beebc4) 範囲 `[['00beebc4', '00beebcb']]`
  - `CONDITIONAL_JUMP` [`00beebc8`](#insn-00beebc8) → [`00beeeac`](#insn-00beeeac)
  - `FALL_THROUGH` [`00beebc8`](#insn-00beebc8) → [`00beebcc`](#insn-00beebcc)
- ブロック [`00beebcc`](#insn-00beebcc) 範囲 `[['00beebcc', '00beebd7']]`
  - `UNCONDITIONAL_JUMP` [`00beebd4`](#insn-00beebd4) → [`00beeed4`](#insn-00beeed4)
- ブロック [`00beebd8`](#insn-00beebd8) 範囲 `[['00beebd8', '00beebfb']]`
  - `CONDITIONAL_JUMP` [`00beebf8`](#insn-00beebf8) → [`00beecf4`](#insn-00beecf4)
  - `FALL_THROUGH` [`00beebf8`](#insn-00beebf8) → [`00beebfc`](#insn-00beebfc)
- ブロック [`00beebfc`](#insn-00beebfc) 範囲 `[['00beebfc', '00beec13']]`
  - `CONDITIONAL_JUMP` [`00beec10`](#insn-00beec10) → [`00beed28`](#insn-00beed28)
  - `FALL_THROUGH` [`00beec10`](#insn-00beec10) → [`00beec14`](#insn-00beec14)
- ブロック [`00beec14`](#insn-00beec14) 範囲 `[['00beec14', '00beec33']]`
  - `CONDITIONAL_JUMP` [`00beec30`](#insn-00beec30) → [`00beed28`](#insn-00beed28)
  - `FALL_THROUGH` [`00beec30`](#insn-00beec30) → [`00beec34`](#insn-00beec34)
- ブロック [`00beec34`](#insn-00beec34) 範囲 `[['00beec34', '00beec37']]`
  - `UNCONDITIONAL_JUMP` [`00beec34`](#insn-00beec34) → [`00beed38`](#insn-00beed38)
- ブロック [`00beec38`](#insn-00beec38) 範囲 `[['00beec38', '00beec5f']]`
  - `CONDITIONAL_JUMP` [`00beec5c`](#insn-00beec5c) → [`00beedd8`](#insn-00beedd8)
  - `FALL_THROUGH` [`00beec5c`](#insn-00beec5c) → [`00beec60`](#insn-00beec60)
- ブロック [`00beec60`](#insn-00beec60) 範囲 `[['00beec60', '00beec7f']]`
  - `CONDITIONAL_JUMP` [`00beec7c`](#insn-00beec7c) → [`00beee18`](#insn-00beee18)
  - `FALL_THROUGH` [`00beec7c`](#insn-00beec7c) → [`00beec80`](#insn-00beec80)
- ブロック [`00beec80`](#insn-00beec80) 範囲 `[['00beec80', '00beeca7']]`
  - `CONDITIONAL_JUMP` [`00beeca4`](#insn-00beeca4) → [`00beee18`](#insn-00beee18)
  - `FALL_THROUGH` [`00beeca4`](#insn-00beeca4) → [`00beeca8`](#insn-00beeca8)
- ブロック [`00beeca8`](#insn-00beeca8) 範囲 `[['00beeca8', '00beecab']]`
  - `UNCONDITIONAL_JUMP` [`00beeca8`](#insn-00beeca8) → [`00beee2c`](#insn-00beee2c)
- ブロック [`00beecac`](#insn-00beecac) 範囲 `[['00beecac', '00beecbf']]`
  - `CONDITIONAL_JUMP` [`00beecbc`](#insn-00beecbc) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beecbc`](#insn-00beecbc) → [`00beecc0`](#insn-00beecc0)
- ブロック [`00beecc0`](#insn-00beecc0) 範囲 `[['00beecc0', '00beece7']]`
  - `CONDITIONAL_JUMP` [`00beece4`](#insn-00beece4) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beece4`](#insn-00beece4) → [`00beece8`](#insn-00beece8)
- ブロック [`00beece8`](#insn-00beece8) 範囲 `[['00beece8', '00beecf3']]`
  - `UNCONDITIONAL_JUMP` [`00beecf0`](#insn-00beecf0) → [`00beeea0`](#insn-00beeea0)
- ブロック [`00beecf4`](#insn-00beecf4) 範囲 `[['00beecf4', '00beed07']]`
  - `CONDITIONAL_JUMP` [`00beed04`](#insn-00beed04) → [`00beed38`](#insn-00beed38)
  - `FALL_THROUGH` [`00beed04`](#insn-00beed04) → [`00beed08`](#insn-00beed08)
- ブロック [`00beed08`](#insn-00beed08) 範囲 `[['00beed08', '00beed23']]`
  - `FALL_THROUGH` [`00beed20`](#insn-00beed20) → [`00beed24`](#insn-00beed24)
- ブロック [`00beed24`](#insn-00beed24) 範囲 `[['00beed24', '00beed27']]`
  - `CONDITIONAL_JUMP` [`00beed24`](#insn-00beed24) → [`00beed38`](#insn-00beed38)
  - `FALL_THROUGH` [`00beed24`](#insn-00beed24) → [`00beed28`](#insn-00beed28)
- ブロック [`00beed28`](#insn-00beed28) 範囲 `[['00beed28', '00beed37']]`
  - `FALL_THROUGH` [`00beed34`](#insn-00beed34) → [`00beed38`](#insn-00beed38)
- ブロック [`00beed38`](#insn-00beed38) 範囲 `[['00beed38', '00beed43']]`
  - `CONDITIONAL_JUMP` [`00beed40`](#insn-00beed40) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beed40`](#insn-00beed40) → [`00beed44`](#insn-00beed44)
- ブロック [`00beed44`](#insn-00beed44) 範囲 `[['00beed44', '00beed4f']]`
  - `UNCONDITIONAL_JUMP` [`00beed4c`](#insn-00beed4c) → [`00beed80`](#insn-00beed80)
- ブロック [`00beed50`](#insn-00beed50) 範囲 `[['00beed50', '00beed53']]`
  - `FALL_THROUGH` [`00beed50`](#insn-00beed50) → [`00beed54`](#insn-00beed54)
- ブロック [`00beed54`](#insn-00beed54) 範囲 `[['00beed54', '00beed67']]`
  - `CONDITIONAL_JUMP` [`00beed64`](#insn-00beed64) → [`00beef04`](#insn-00beef04)
  - `FALL_THROUGH` [`00beed64`](#insn-00beed64) → [`00beed68`](#insn-00beed68)
- ブロック [`00beed68`](#insn-00beed68) 範囲 `[['00beed68', '00beed7f']]`
  - `CONDITIONAL_JUMP` [`00beed7c`](#insn-00beed7c) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beed7c`](#insn-00beed7c) → [`00beed80`](#insn-00beed80)
- ブロック [`00beed80`](#insn-00beed80) 範囲 `[['00beed80', '00beed9b']]`
  - `CONDITIONAL_JUMP` [`00beed98`](#insn-00beed98) → [`00beed68`](#insn-00beed68)
  - `FALL_THROUGH` [`00beed98`](#insn-00beed98) → [`00beed9c`](#insn-00beed9c)
- ブロック [`00beed9c`](#insn-00beed9c) 範囲 `[['00beed9c', '00beeda3']]`
  - `FALL_THROUGH` [`00beeda0`](#insn-00beeda0) → [`00beeda4`](#insn-00beeda4)
- ブロック [`00beeda4`](#insn-00beeda4) 範囲 `[['00beeda4', '00beedaf']]`
  - `CONDITIONAL_JUMP` [`00beedac`](#insn-00beedac) → [`00beed50`](#insn-00beed50)
  - `FALL_THROUGH` [`00beedac`](#insn-00beedac) → [`00beedb0`](#insn-00beedb0)
- ブロック [`00beedb0`](#insn-00beedb0) 範囲 `[['00beedb0', '00beedcf']]`
  - `CONDITIONAL_JUMP` [`00beedcc`](#insn-00beedcc) → [`00beeda4`](#insn-00beeda4)
  - `FALL_THROUGH` [`00beedcc`](#insn-00beedcc) → [`00beedd0`](#insn-00beedd0)
- ブロック [`00beedd0`](#insn-00beedd0) 範囲 `[['00beedd0', '00beedd7']]`
  - `UNCONDITIONAL_JUMP` [`00beedd4`](#insn-00beedd4) → [`00beed54`](#insn-00beed54)
- ブロック [`00beedd8`](#insn-00beedd8) 範囲 `[['00beedd8', '00beedeb']]`
  - `CONDITIONAL_JUMP` [`00beede8`](#insn-00beede8) → [`00beee2c`](#insn-00beee2c)
  - `FALL_THROUGH` [`00beede8`](#insn-00beede8) → [`00beedec`](#insn-00beedec)
- ブロック [`00beedec`](#insn-00beedec) 範囲 `[['00beedec', '00beee17']]`
  - `CONDITIONAL_JUMP` [`00beee14`](#insn-00beee14) → [`00beee34`](#insn-00beee34)
  - `FALL_THROUGH` [`00beee14`](#insn-00beee14) → [`00beee18`](#insn-00beee18)
- ブロック [`00beee18`](#insn-00beee18) 範囲 `[['00beee18', '00beee1b']]`
  - `FALL_THROUGH` [`00beee18`](#insn-00beee18) → [`00beee1c`](#insn-00beee1c)
- ブロック [`00beee1c`](#insn-00beee1c) 範囲 `[['00beee1c', '00beee2b']]`
  - `UNCONDITIONAL_JUMP` [`00beee28`](#insn-00beee28) → [`00beee34`](#insn-00beee34)
- ブロック [`00beee2c`](#insn-00beee2c) 範囲 `[['00beee2c', '00beee33']]`
  - `FALL_THROUGH` [`00beee30`](#insn-00beee30) → [`00beee34`](#insn-00beee34)
- ブロック [`00beee34`](#insn-00beee34) 範囲 `[['00beee34', '00beee3f']]`
  - `FALL_THROUGH` [`00beee3c`](#insn-00beee3c) → [`00beee40`](#insn-00beee40)
- ブロック [`00beee40`](#insn-00beee40) 範囲 `[['00beee40', '00beee4b']]`
  - `CONDITIONAL_JUMP` [`00beee48`](#insn-00beee48) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beee48`](#insn-00beee48) → [`00beee4c`](#insn-00beee4c)
- ブロック [`00beee4c`](#insn-00beee4c) 範囲 `[['00beee4c', '00beee77']]`
  - `CONDITIONAL_JUMP` [`00beee74`](#insn-00beee74) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beee74`](#insn-00beee74) → [`00beee78`](#insn-00beee78)
- ブロック [`00beee78`](#insn-00beee78) 範囲 `[['00beee78', '00beee93']]`
  - `FALL_THROUGH` [`00beee90`](#insn-00beee90) → [`00beee94`](#insn-00beee94)
- ブロック [`00beee94`](#insn-00beee94) 範囲 `[['00beee94', '00beee97']]`
  - `CONDITIONAL_JUMP` [`00beee94`](#insn-00beee94) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beee94`](#insn-00beee94) → [`00beee98`](#insn-00beee98)
- ブロック [`00beee98`](#insn-00beee98) 範囲 `[['00beee98', '00beee9f']]`
  - `FALL_THROUGH` [`00beee9c`](#insn-00beee9c) → [`00beeea0`](#insn-00beeea0)
- ブロック [`00beeea0`](#insn-00beeea0) 範囲 `[['00beeea0', '00beeeab']]`
  - `UNCONDITIONAL_JUMP` [`00beeea8`](#insn-00beeea8) → [`00beeee8`](#insn-00beeee8)
- ブロック [`00beeeac`](#insn-00beeeac) 範囲 `[['00beeeac', '00beeecb']]`
  - `CONDITIONAL_JUMP` [`00beeec8`](#insn-00beeec8) → [`00beeee4`](#insn-00beeee4)
  - `FALL_THROUGH` [`00beeec8`](#insn-00beeec8) → [`00beeecc`](#insn-00beeecc)
- ブロック [`00beeecc`](#insn-00beeecc) 範囲 `[['00beeecc', '00beeed3']]`
  - `FALL_THROUGH` [`00beeed0`](#insn-00beeed0) → [`00beeed4`](#insn-00beeed4)
- ブロック [`00beeed4`](#insn-00beeed4) 範囲 `[['00beeed4', '00beeedb']]`
  - `FALL_THROUGH` [`00beeed8`](#insn-00beeed8) → [`00beeedc`](#insn-00beeedc)
- ブロック [`00beeedc`](#insn-00beeedc) 範囲 `[['00beeedc', '00beeee3']]`
  - `UNCONDITIONAL_JUMP` [`00beeee0`](#insn-00beeee0) → [`00beeee8`](#insn-00beeee8)
- ブロック [`00beeee4`](#insn-00beeee4) 範囲 `[['00beeee4', '00beeee7']]`
  - `FALL_THROUGH` [`00beeee4`](#insn-00beeee4) → [`00beeee8`](#insn-00beeee8)
- ブロック [`00beeee8`](#insn-00beeee8) 範囲 `[['00beeee8', '00beeef3']]`
  - `FALL_THROUGH` [`00beeef0`](#insn-00beeef0) → [`00beeef4`](#insn-00beeef4)
- ブロック [`00beeef4`](#insn-00beeef4) 範囲 `[['00beeef4', '00beef03']]`
- ブロック [`00beef04`](#insn-00beef04) 範囲 `[['00beef04', '00beef13']]`
  - `UNCONDITIONAL_JUMP` [`00beef10`](#insn-00beef10) → [`00beeee8`](#insn-00beeee8)

## 命令位置別の参照

- [`00beeb00`](#insn-00beeb00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb04`](#insn-00beeb04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb08`](#insn-00beeb08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb0c`](#insn-00beeb0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb28`](#insn-00beeb28) → [`00beeb68`](#insn-00beeb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb2c`](#insn-00beeb2c) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb34`](#insn-00beeb34) → [`00beebd8`](#insn-00beebd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb40`](#insn-00beeb40) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb44`](#insn-00beeb44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb48`](#insn-00beeb48) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beeb50`](#insn-00beeb50) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb54`](#insn-00beeb54) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb60`](#insn-00beeb60) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb64`](#insn-00beeb64) → [`00beeedc`](#insn-00beeedc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb6c`](#insn-00beeb6c) → [`00beeb9c`](#insn-00beeb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb74`](#insn-00beeb74) → [`00beec38`](#insn-00beec38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb7c`](#insn-00beeb7c) → [`00beebd8`](#insn-00beebd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeb94`](#insn-00beeb94) → [`00beef14`](00beef14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00beef14` · 推定シンボル `None` · 推定型 `None`
- [`00beeb98`](#insn-00beeb98) → [`00beeee4`](#insn-00beeee4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeba4`](#insn-00beeba4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeba8`](#insn-00beeba8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebac`](#insn-00beebac) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebb0`](#insn-00beebb0) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beebb4`](#insn-00beebb4) → [`00beecac`](#insn-00beecac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebb8`](#insn-00beebb8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebbc`](#insn-00beebbc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebc0`](#insn-00beebc0) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beebc8`](#insn-00beebc8) → [`00beeeac`](#insn-00beeeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebcc`](#insn-00beebcc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebd4`](#insn-00beebd4) → [`00beeed4`](#insn-00beeed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebe8`](#insn-00beebe8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebf0`](#insn-00beebf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebf4`](#insn-00beebf4) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beebf8`](#insn-00beebf8) → [`00beecf4`](#insn-00beecf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beebfc`](#insn-00beebfc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec00`](#insn-00beec00) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec04`](#insn-00beec04) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beec10`](#insn-00beec10) → [`00beed28`](#insn-00beed28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec14`](#insn-00beec14) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec1c`](#insn-00beec1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec20`](#insn-00beec20) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beec30`](#insn-00beec30) → [`00beed28`](#insn-00beed28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec34`](#insn-00beec34) → [`00beed38`](#insn-00beed38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec48`](#insn-00beec48) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec50`](#insn-00beec50) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec54`](#insn-00beec54) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec58`](#insn-00beec58) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beec5c`](#insn-00beec5c) → [`00beedd8`](#insn-00beedd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec60`](#insn-00beec60) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec64`](#insn-00beec64) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec68`](#insn-00beec68) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beec6c`](#insn-00beec6c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec7c`](#insn-00beec7c) → [`00beee18`](#insn-00beee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec80`](#insn-00beec80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec88`](#insn-00beec88) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beec8c`](#insn-00beec8c) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beec90`](#insn-00beec90) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeca4`](#insn-00beeca4) → [`00beee18`](#insn-00beee18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeca8`](#insn-00beeca8) → [`00beee2c`](#insn-00beee2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecac`](#insn-00beecac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecb0`](#insn-00beecb0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecb4`](#insn-00beecb4) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beecbc`](#insn-00beecbc) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecc0`](#insn-00beecc0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecc8`](#insn-00beecc8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecd4`](#insn-00beecd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecd8`](#insn-00beecd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecdc`](#insn-00beecdc) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beece4`](#insn-00beece4) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beece8`](#insn-00beece8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecec`](#insn-00beecec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecf0`](#insn-00beecf0) → [`00beeea0`](#insn-00beeea0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecf4`](#insn-00beecf4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecf8`](#insn-00beecf8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beecfc`](#insn-00beecfc) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beed04`](#insn-00beed04) → [`00beed38`](#insn-00beed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed08`](#insn-00beed08) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed0c`](#insn-00beed0c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed18`](#insn-00beed18) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beed24`](#insn-00beed24) → [`00beed38`](#insn-00beed38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed28`](#insn-00beed28) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed30`](#insn-00beed30) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed40`](#insn-00beed40) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed4c`](#insn-00beed4c) → [`00beed80`](#insn-00beed80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed58`](#insn-00beed58) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed64`](#insn-00beed64) → [`00beef04`](#insn-00beef04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed7c`](#insn-00beed7c) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed88`](#insn-00beed88) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed8c`](#insn-00beed8c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed90`](#insn-00beed90) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beed98`](#insn-00beed98) → [`00beed68`](#insn-00beed68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beed9c`](#insn-00beed9c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedac`](#insn-00beedac) → [`00beed50`](#insn-00beed50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedb4`](#insn-00beedb4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedbc`](#insn-00beedbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedc0`](#insn-00beedc0) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beedc4`](#insn-00beedc4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedcc`](#insn-00beedcc) → [`00beeda4`](#insn-00beeda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedd4`](#insn-00beedd4) → [`00beed54`](#insn-00beed54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedd8`](#insn-00beedd8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeddc`](#insn-00beeddc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beede0`](#insn-00beede0) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beede8`](#insn-00beede8) → [`00beee2c`](#insn-00beee2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedec`](#insn-00beedec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedf0`](#insn-00beedf0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beedf8`](#insn-00beedf8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee00`](#insn-00beee00) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beee04`](#insn-00beee04) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee08`](#insn-00beee08) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee14`](#insn-00beee14) → [`00beee34`](#insn-00beee34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee18`](#insn-00beee18) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee1c`](#insn-00beee1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee28`](#insn-00beee28) → [`00beee34`](#insn-00beee34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee2c`](#insn-00beee2c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee30`](#insn-00beee30) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee38`](#insn-00beee38) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee3c`](#insn-00beee3c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee40`](#insn-00beee40) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beee48`](#insn-00beee48) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee4c`](#insn-00beee4c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee54`](#insn-00beee54) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee64`](#insn-00beee64) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee68`](#insn-00beee68) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee6c`](#insn-00beee6c) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beee74`](#insn-00beee74) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee7c`](#insn-00beee7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee80`](#insn-00beee80) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee88`](#insn-00beee88) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee8c`](#insn-00beee8c) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beee94`](#insn-00beee94) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee98`](#insn-00beee98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beee9c`](#insn-00beee9c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeea8`](#insn-00beeea8) → [`00beeee8`](#insn-00beeee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeac`](#insn-00beeeac) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeb0`](#insn-00beeeb0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeebc`](#insn-00beeebc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeec0`](#insn-00beeec0) → [`00c52fa0`](../00c52/00c52fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c52fa0` · 推定シンボル `None` · 推定型 `None`
- [`00beeec8`](#insn-00beeec8) → [`00beeee4`](#insn-00beeee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeecc`](#insn-00beeecc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeed4`](#insn-00beeed4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeee0`](#insn-00beeee0) → [`00beeee8`](#insn-00beeee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeee8`](#insn-00beeee8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeeec`](#insn-00beeeec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeef0`](#insn-00beeef0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beeef4`](#insn-00beeef4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beef10`](#insn-00beef10) → [`00beeee8`](#insn-00beeee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beeb00`](#insn-00beeb00)

~~~json
{
  "source": "00beeb00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb04`](#insn-00beeb04)

~~~json
{
  "source": "00beeb04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb08`](#insn-00beeb08)

~~~json
{
  "source": "00beeb08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb0c`](#insn-00beeb0c)

~~~json
{
  "source": "00beeb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb28`](#insn-00beeb28)

~~~json
{
  "source": "00beeb28",
  "target": "00beeb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb2c`](#insn-00beeb2c)

~~~json
{
  "source": "00beeb2c",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb34`](#insn-00beeb34)

~~~json
{
  "source": "00beeb34",
  "target": "00beebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb40`](#insn-00beeb40)

~~~json
{
  "source": "00beeb40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb44`](#insn-00beeb44)

~~~json
{
  "source": "00beeb44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb48`](#insn-00beeb48)

~~~json
{
  "source": "00beeb48",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beeb50`](#insn-00beeb50)

~~~json
{
  "source": "00beeb50",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb54`](#insn-00beeb54)

~~~json
{
  "source": "00beeb54",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb60`](#insn-00beeb60)

~~~json
{
  "source": "00beeb60",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb64`](#insn-00beeb64)

~~~json
{
  "source": "00beeb64",
  "target": "00beeedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb6c`](#insn-00beeb6c)

~~~json
{
  "source": "00beeb6c",
  "target": "00beeb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb74`](#insn-00beeb74)

~~~json
{
  "source": "00beeb74",
  "target": "00beec38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb7c`](#insn-00beeb7c)

~~~json
{
  "source": "00beeb7c",
  "target": "00beebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeb94`](#insn-00beeb94)

~~~json
{
  "source": "00beeb94",
  "target": "00beef14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beeb98`](#insn-00beeb98)

~~~json
{
  "source": "00beeb98",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeba4`](#insn-00beeba4)

~~~json
{
  "source": "00beeba4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeba8`](#insn-00beeba8)

~~~json
{
  "source": "00beeba8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebac`](#insn-00beebac)

~~~json
{
  "source": "00beebac",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebb0`](#insn-00beebb0)

~~~json
{
  "source": "00beebb0",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beebb4`](#insn-00beebb4)

~~~json
{
  "source": "00beebb4",
  "target": "00beecac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebb8`](#insn-00beebb8)

~~~json
{
  "source": "00beebb8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebbc`](#insn-00beebbc)

~~~json
{
  "source": "00beebbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebc0`](#insn-00beebc0)

~~~json
{
  "source": "00beebc0",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beebc8`](#insn-00beebc8)

~~~json
{
  "source": "00beebc8",
  "target": "00beeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebcc`](#insn-00beebcc)

~~~json
{
  "source": "00beebcc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebd4`](#insn-00beebd4)

~~~json
{
  "source": "00beebd4",
  "target": "00beeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebe8`](#insn-00beebe8)

~~~json
{
  "source": "00beebe8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebf0`](#insn-00beebf0)

~~~json
{
  "source": "00beebf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebf4`](#insn-00beebf4)

~~~json
{
  "source": "00beebf4",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beebf8`](#insn-00beebf8)

~~~json
{
  "source": "00beebf8",
  "target": "00beecf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beebfc`](#insn-00beebfc)

~~~json
{
  "source": "00beebfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec00`](#insn-00beec00)

~~~json
{
  "source": "00beec00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec04`](#insn-00beec04)

~~~json
{
  "source": "00beec04",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec10`](#insn-00beec10)

~~~json
{
  "source": "00beec10",
  "target": "00beed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec14`](#insn-00beec14)

~~~json
{
  "source": "00beec14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec1c`](#insn-00beec1c)

~~~json
{
  "source": "00beec1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec20`](#insn-00beec20)

~~~json
{
  "source": "00beec20",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec30`](#insn-00beec30)

~~~json
{
  "source": "00beec30",
  "target": "00beed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec34`](#insn-00beec34)

~~~json
{
  "source": "00beec34",
  "target": "00beed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec48`](#insn-00beec48)

~~~json
{
  "source": "00beec48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec50`](#insn-00beec50)

~~~json
{
  "source": "00beec50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec54`](#insn-00beec54)

~~~json
{
  "source": "00beec54",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec58`](#insn-00beec58)

~~~json
{
  "source": "00beec58",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec5c`](#insn-00beec5c)

~~~json
{
  "source": "00beec5c",
  "target": "00beedd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec60`](#insn-00beec60)

~~~json
{
  "source": "00beec60",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec64`](#insn-00beec64)

~~~json
{
  "source": "00beec64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec68`](#insn-00beec68)

~~~json
{
  "source": "00beec68",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec6c`](#insn-00beec6c)

~~~json
{
  "source": "00beec6c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec7c`](#insn-00beec7c)

~~~json
{
  "source": "00beec7c",
  "target": "00beee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec80`](#insn-00beec80)

~~~json
{
  "source": "00beec80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec88`](#insn-00beec88)

~~~json
{
  "source": "00beec88",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beec8c`](#insn-00beec8c)

~~~json
{
  "source": "00beec8c",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beec90`](#insn-00beec90)

~~~json
{
  "source": "00beec90",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeca4`](#insn-00beeca4)

~~~json
{
  "source": "00beeca4",
  "target": "00beee18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeca8`](#insn-00beeca8)

~~~json
{
  "source": "00beeca8",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecac`](#insn-00beecac)

~~~json
{
  "source": "00beecac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecb0`](#insn-00beecb0)

~~~json
{
  "source": "00beecb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecb4`](#insn-00beecb4)

~~~json
{
  "source": "00beecb4",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beecbc`](#insn-00beecbc)

~~~json
{
  "source": "00beecbc",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecc0`](#insn-00beecc0)

~~~json
{
  "source": "00beecc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecc8`](#insn-00beecc8)

~~~json
{
  "source": "00beecc8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecd4`](#insn-00beecd4)

~~~json
{
  "source": "00beecd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecd8`](#insn-00beecd8)

~~~json
{
  "source": "00beecd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecdc`](#insn-00beecdc)

~~~json
{
  "source": "00beecdc",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beece4`](#insn-00beece4)

~~~json
{
  "source": "00beece4",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beece8`](#insn-00beece8)

~~~json
{
  "source": "00beece8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecec`](#insn-00beecec)

~~~json
{
  "source": "00beecec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecf0`](#insn-00beecf0)

~~~json
{
  "source": "00beecf0",
  "target": "00beeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecf4`](#insn-00beecf4)

~~~json
{
  "source": "00beecf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecf8`](#insn-00beecf8)

~~~json
{
  "source": "00beecf8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beecfc`](#insn-00beecfc)

~~~json
{
  "source": "00beecfc",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beed04`](#insn-00beed04)

~~~json
{
  "source": "00beed04",
  "target": "00beed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed08`](#insn-00beed08)

~~~json
{
  "source": "00beed08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed0c`](#insn-00beed0c)

~~~json
{
  "source": "00beed0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed18`](#insn-00beed18)

~~~json
{
  "source": "00beed18",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beed24`](#insn-00beed24)

~~~json
{
  "source": "00beed24",
  "target": "00beed38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed28`](#insn-00beed28)

~~~json
{
  "source": "00beed28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed30`](#insn-00beed30)

~~~json
{
  "source": "00beed30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed40`](#insn-00beed40)

~~~json
{
  "source": "00beed40",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed4c`](#insn-00beed4c)

~~~json
{
  "source": "00beed4c",
  "target": "00beed80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed58`](#insn-00beed58)

~~~json
{
  "source": "00beed58",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed64`](#insn-00beed64)

~~~json
{
  "source": "00beed64",
  "target": "00beef04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed7c`](#insn-00beed7c)

~~~json
{
  "source": "00beed7c",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed88`](#insn-00beed88)

~~~json
{
  "source": "00beed88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed8c`](#insn-00beed8c)

~~~json
{
  "source": "00beed8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed90`](#insn-00beed90)

~~~json
{
  "source": "00beed90",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beed98`](#insn-00beed98)

~~~json
{
  "source": "00beed98",
  "target": "00beed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beed9c`](#insn-00beed9c)

~~~json
{
  "source": "00beed9c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedac`](#insn-00beedac)

~~~json
{
  "source": "00beedac",
  "target": "00beed50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedb4`](#insn-00beedb4)

~~~json
{
  "source": "00beedb4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedbc`](#insn-00beedbc)

~~~json
{
  "source": "00beedbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedc0`](#insn-00beedc0)

~~~json
{
  "source": "00beedc0",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beedc4`](#insn-00beedc4)

~~~json
{
  "source": "00beedc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedcc`](#insn-00beedcc)

~~~json
{
  "source": "00beedcc",
  "target": "00beeda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedd4`](#insn-00beedd4)

~~~json
{
  "source": "00beedd4",
  "target": "00beed54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedd8`](#insn-00beedd8)

~~~json
{
  "source": "00beedd8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeddc`](#insn-00beeddc)

~~~json
{
  "source": "00beeddc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beede0`](#insn-00beede0)

~~~json
{
  "source": "00beede0",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beede8`](#insn-00beede8)

~~~json
{
  "source": "00beede8",
  "target": "00beee2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedec`](#insn-00beedec)

~~~json
{
  "source": "00beedec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedf0`](#insn-00beedf0)

~~~json
{
  "source": "00beedf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beedf8`](#insn-00beedf8)

~~~json
{
  "source": "00beedf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee00`](#insn-00beee00)

~~~json
{
  "source": "00beee00",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beee04`](#insn-00beee04)

~~~json
{
  "source": "00beee04",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee08`](#insn-00beee08)

~~~json
{
  "source": "00beee08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee14`](#insn-00beee14)

~~~json
{
  "source": "00beee14",
  "target": "00beee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee18`](#insn-00beee18)

~~~json
{
  "source": "00beee18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee1c`](#insn-00beee1c)

~~~json
{
  "source": "00beee1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee28`](#insn-00beee28)

~~~json
{
  "source": "00beee28",
  "target": "00beee34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee2c`](#insn-00beee2c)

~~~json
{
  "source": "00beee2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee30`](#insn-00beee30)

~~~json
{
  "source": "00beee30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee38`](#insn-00beee38)

~~~json
{
  "source": "00beee38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee3c`](#insn-00beee3c)

~~~json
{
  "source": "00beee3c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee40`](#insn-00beee40)

~~~json
{
  "source": "00beee40",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beee48`](#insn-00beee48)

~~~json
{
  "source": "00beee48",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee4c`](#insn-00beee4c)

~~~json
{
  "source": "00beee4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee54`](#insn-00beee54)

~~~json
{
  "source": "00beee54",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee64`](#insn-00beee64)

~~~json
{
  "source": "00beee64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee68`](#insn-00beee68)

~~~json
{
  "source": "00beee68",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee6c`](#insn-00beee6c)

~~~json
{
  "source": "00beee6c",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beee74`](#insn-00beee74)

~~~json
{
  "source": "00beee74",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee7c`](#insn-00beee7c)

~~~json
{
  "source": "00beee7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee80`](#insn-00beee80)

~~~json
{
  "source": "00beee80",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee88`](#insn-00beee88)

~~~json
{
  "source": "00beee88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee8c`](#insn-00beee8c)

~~~json
{
  "source": "00beee8c",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beee94`](#insn-00beee94)

~~~json
{
  "source": "00beee94",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee98`](#insn-00beee98)

~~~json
{
  "source": "00beee98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beee9c`](#insn-00beee9c)

~~~json
{
  "source": "00beee9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeea8`](#insn-00beeea8)

~~~json
{
  "source": "00beeea8",
  "target": "00beeee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeac`](#insn-00beeeac)

~~~json
{
  "source": "00beeeac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeb0`](#insn-00beeeb0)

~~~json
{
  "source": "00beeeb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeebc`](#insn-00beeebc)

~~~json
{
  "source": "00beeebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeec0`](#insn-00beeec0)

~~~json
{
  "source": "00beeec0",
  "target": "00c52fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00beeec8`](#insn-00beeec8)

~~~json
{
  "source": "00beeec8",
  "target": "00beeee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeecc`](#insn-00beeecc)

~~~json
{
  "source": "00beeecc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeed4`](#insn-00beeed4)

~~~json
{
  "source": "00beeed4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeee0`](#insn-00beeee0)

~~~json
{
  "source": "00beeee0",
  "target": "00beeee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeee8`](#insn-00beeee8)

~~~json
{
  "source": "00beeee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeeec`](#insn-00beeeec)

~~~json
{
  "source": "00beeeec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeef0`](#insn-00beeef0)

~~~json
{
  "source": "00beeef0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beeef4`](#insn-00beeef4)

~~~json
{
  "source": "00beeef4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beef10`](#insn-00beef10)

~~~json
{
  "source": "00beef10",
  "target": "00beeee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
