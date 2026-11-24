# 00bbe9bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbe594`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0010.md#compare-d87880d461b4594c30281f97ee492f14)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbea58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbea58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-04ed4d6d85f6a7e83550978cc17d073c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbe9bc",
  "name": "_ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsISB_E9referenceEEE5valueEvE4typeESB_SB_",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2352179e5f58277dee78c34a929d4ce7a032cb2ac735ba71cbb6478e1f6b727",
  "source_text_sha256": "d2352179e5f58277dee78c34a929d4ce7a032cb2ac735ba71cbb6478e1f6b727",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbe9bc",
        "00bbec1b"
      ]
    ],
    "bytes_sha256": "81f4311878880060ff6e1ed9b9ff552b19b068db2987bf4f5c566772c30821fc",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d570](../00c5d/00c5d570.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5ad10](../00c5a/00c5ad10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5174 bytes

~~~c

void _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_traitsISB_E9referenceEEE5valueEvE4typeESB_SB_
               (undefined8 *param_1,undefined8 *param_2,ulong *param_3)

{
  undefined8 *puVar1;
  undefined1 *puVar2;
  ulong uVar3;
  undefined1 *puVar4;
  undefined1 *puVar5;
  undefined1 *puVar6;
  undefined1 *puVar7;
  ulong uVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  ulong uVar11;
  ulong uVar12;
  ulong uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  
  puVar7 = (undefined1 *)*param_2;
  uVar3 = param_1[2];
  puVar2 = (undefined1 *)*param_1;
  uVar13 = (long)*param_3 - (long)puVar7;
  if (uVar3 - (long)puVar2 < uVar13) {
    if (puVar2 != (undefined1 *)0x0) {
      param_1[1] = puVar2;
      _ZdlPv(puVar2);
      uVar3 = 0;
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
    }
    if ((long)uVar13 < 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
    if (uVar3 < 0x3fffffffffffffff) {
      if (uVar13 <= uVar3 << 1) {
        uVar13 = uVar3 << 1;
      }
    }
    else {
      uVar13 = 0x7fffffffffffffff;
    }
    puVar7 = (undefined1 *)_Znwm(uVar13);
    *param_1 = puVar7;
    param_1[1] = puVar7;
    param_1[2] = puVar7 + uVar13;
    puVar2 = (undefined1 *)*param_2;
    puVar4 = (undefined1 *)*param_3;
    uVar13 = (long)puVar4 - (long)puVar2;
    if (uVar13 != 0) {
      puVar6 = puVar7;
      if ((0x1f < uVar13) && ((puVar4 <= puVar7 || (puVar7 + uVar13 <= puVar2)))) {
        uVar8 = uVar13 & 0xffffffffffffffe0;
        puVar10 = (undefined8 *)(puVar2 + 0x10);
        puVar6 = puVar7 + uVar8;
        puVar2 = puVar2 + uVar8;
        puVar9 = (undefined8 *)(puVar7 + 0x10);
        uVar3 = uVar8;
        do {
          puVar1 = puVar10 + -1;
          uVar14 = puVar10[-2];
          uVar16 = puVar10[1];
          uVar15 = *puVar10;
          puVar10 = puVar10 + 4;
          uVar3 = uVar3 - 0x20;
          puVar9[-1] = *puVar1;
          puVar9[-2] = uVar14;
          puVar9[1] = uVar16;
          *puVar9 = uVar15;
          puVar9 = puVar9 + 4;
        } while (uVar3 != 0);
        puVar7 = puVar6;
        if (uVar13 == uVar8) goto LAB_00bbeaf8;
      }
      do {
        puVar5 = puVar2 + 1;
        puVar7 = puVar6 + 1;
        *puVar6 = *puVar2;
        puVar2 = puVar5;
        puVar6 = puVar7;
      } while (puVar4 != puVar5);
    }
LAB_00bbeaf8:
    param_1[1] = puVar7;
    return;
  }
  uVar3 = param_1[1] - (long)puVar2;
  puVar4 = puVar7 + (uVar3 & 0xffffffff);
  if (uVar13 <= uVar3) {
    puVar4 = (undefined1 *)*param_3;
  }
  uVar8 = (long)puVar4 - (long)puVar7;
  if (uVar8 != 0) {
    puVar6 = puVar2;
    if ((0x1f < uVar8) && ((puVar4 <= puVar2 || (puVar4 + ((long)puVar2 - (long)puVar7) <= puVar7)))
       ) {
      uVar11 = uVar8 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar2 + 0x10);
      puVar2 = puVar2 + uVar11;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar12 = uVar11;
      do {
        puVar1 = puVar9 + -1;
        uVar14 = puVar9[-2];
        uVar16 = puVar9[1];
        uVar15 = *puVar9;
        uVar12 = uVar12 - 0x20;
        puVar9 = puVar9 + 4;
        puVar10[-1] = *puVar1;
        puVar10[-2] = uVar14;
        puVar10[1] = uVar16;
        *puVar10 = uVar15;
        puVar10 = puVar10 + 4;
                    /* try { // try from 00bbeb4c to 00cbeb67 has its CatchHandler @ 00bbf3e4 */
      } while (uVar12 != 0);
      puVar6 = puVar2;
      puVar7 = puVar7 + uVar11;
      if (uVar11 == uVar8) goto LAB_00bbeb68;
    }
    do {
      puVar5 = puVar7 + 1;
      puVar2 = puVar6 + 1;
      *puVar6 = *puVar7;
      puVar6 = puVar2;
      puVar7 = puVar5;
    } while (puVar4 != puVar5);
  }
LAB_00bbeb68:
                    /* try { // try from 00bbeb68 to 00cbec2b has its CatchHandler @ 00bbe7f8 */
  if (uVar13 <= uVar3) {
    param_1[1] = puVar2;
    return;
  }
  puVar6 = (undefined1 *)*param_3;
  puVar7 = (undefined1 *)param_1[1];
  uVar13 = (long)puVar6 - (long)puVar4;
  puVar2 = puVar7;
  if (uVar13 != 0) {
    if ((0x1f < uVar13) && ((puVar6 <= puVar7 || (puVar7 + uVar13 <= puVar4)))) {
      uVar8 = uVar13 & 0xffffffffffffffe0;
      puVar10 = (undefined8 *)(puVar4 + 0x10);
      puVar2 = puVar7 + uVar8;
      puVar4 = puVar4 + uVar8;
      puVar9 = (undefined8 *)(puVar7 + 0x10);
      uVar3 = uVar8;
      do {
        puVar1 = puVar10 + -1;
        uVar14 = puVar10[-2];
        uVar16 = puVar10[1];
        uVar15 = *puVar10;
        puVar10 = puVar10 + 4;
        uVar3 = uVar3 - 0x20;
        puVar9[-1] = *puVar1;
        puVar9[-2] = uVar14;
        puVar9[1] = uVar16;
        *puVar9 = uVar15;
        puVar9 = puVar9 + 4;
      } while (uVar3 != 0);
      puVar7 = puVar2;
      if (uVar8 == uVar13) goto LAB_00bbec00;
    }
    do {
      puVar5 = puVar4 + 1;
      puVar2 = puVar7 + 1;
      *puVar7 = *puVar4;
      puVar4 = puVar5;
      puVar7 = puVar2;
    } while (puVar6 != puVar5);
  }
LAB_00bbec00:
  param_1[1] = puVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbe9bc"></a> `00bbe9bc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbe9c0"></a> `00bbe9c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe9c4"></a> `00bbe9c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbe9c8"></a> `00bbe9c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe9cc"></a> `00bbe9cc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbe9d0"></a> `00bbe9d0` | `2c 00 40 f9` | ldr x12,[x1] | `FALL_THROUGH`
<a id="insn-00bbe9d4"></a> `00bbe9d4` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00bbe9d8"></a> `00bbe9d8` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe9dc"></a> `00bbe9dc` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bbe9e0"></a> `00bbe9e0` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bbe9e4"></a> `00bbe9e4` | `56 01 0c cb` | sub x22,x10,x12 | `FALL_THROUGH`
<a id="insn-00bbe9e8"></a> `00bbe9e8` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbe9ec"></a> `00bbe9ec` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbe9f0"></a> `00bbe9f0` | `09 02 00 54` | b.ls 0x00bbea30 | `CONDITIONAL_JUMP`
<a id="insn-00bbe9f4"></a> `00bbe9f4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbe9f8"></a> `00bbe9f8` | `c0 00 00 b4` | cbz x0,0x00bbea10 | `CONDITIONAL_JUMP`
<a id="insn-00bbe9fc"></a> `00bbe9fc` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbea00"></a> `00bbea00` | `2c 65 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbea04"></a> `00bbea04` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbea08"></a> `00bbea08` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bbea0c"></a> `00bbea0c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbea10"></a> `00bbea10` | `36 10 f8 b7` | tbnz x22,#0x3f,0x00bbec14 | `CONDITIONAL_JUMP`
<a id="insn-00bbea14"></a> `00bbea14` | `e9 f3 7f b2` | orr x9,xzr,#0x3ffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bbea18"></a> `00bbea18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbea1c"></a> `00bbea1c` | `08 02 00 54` | b.hi 0x00bbea5c | `CONDITIONAL_JUMP`
<a id="insn-00bbea20"></a> `00bbea20` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbea24"></a> `00bbea24` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bbea28"></a> `00bbea28` | `d6 32 88 9a` | csel x22,x22,x8,cc | `FALL_THROUGH`
<a id="insn-00bbea2c"></a> `00bbea2c` | `0d 00 00 14` | b 0x00bbea60 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbea30"></a> `00bbea30` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbea34"></a> `00bbea34` | `09 01 00 cb` | sub x9,x8,x0 | `FALL_THROUGH`
<a id="insn-00bbea38"></a> `00bbea38` | `88 41 29 8b` | add x8,x12,w9, UXTW  | `FALL_THROUGH`
<a id="insn-00bbea3c"></a> `00bbea3c` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbea40"></a> `00bbea40` | `08 81 8a 9a` | csel x8,x8,x10,hi | `FALL_THROUGH`
<a id="insn-00bbea44"></a> `00bbea44` | `0b 01 0c eb` | subs x11,x8,x12 | `FALL_THROUGH`
<a id="insn-00bbea48"></a> `00bbea48` | `00 09 00 54` | b.eq 0x00bbeb68 | `CONDITIONAL_JUMP`
<a id="insn-00bbea4c"></a> `00bbea4c` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbea50"></a> `00bbea50` | `82 05 00 54` | b.cs 0x00bbeb00 | `CONDITIONAL_JUMP`
<a id="insn-00bbea54"></a> `00bbea54` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbea58"></a> `00bbea58` | `40 00 00 14` | b 0x00bbeb58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbea5c"></a> `00bbea5c` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bbea60"></a> `00bbea60` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbea64"></a> `00bbea64` | `0b 65 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbea68"></a> `00bbea68` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-00bbea6c"></a> `00bbea6c` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00bbea70"></a> `00bbea70` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbea74"></a> `00bbea74` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bbea78"></a> `00bbea78` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbea7c"></a> `00bbea7c` | `0b 01 09 eb` | subs x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbea80"></a> `00bbea80` | `a0 03 00 54` | b.eq 0x00bbeaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbea84"></a> `00bbea84` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbea88"></a> `00bbea88` | `a3 02 00 54` | b.cc 0x00bbeadc | `CONDITIONAL_JUMP`
<a id="insn-00bbea8c"></a> `00bbea8c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbea90"></a> `00bbea90` | `82 00 00 54` | b.cs 0x00bbeaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bbea94"></a> `00bbea94` | `0a 00 0b 8b` | add x10,x0,x11 | `FALL_THROUGH`
<a id="insn-00bbea98"></a> `00bbea98` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbea9c"></a> `00bbea9c` | `03 02 00 54` | b.cc 0x00bbeadc | `CONDITIONAL_JUMP`
<a id="insn-00bbeaa0"></a> `00bbeaa0` | `6c e9 7b 92` | and x12,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbeaa4"></a> `00bbeaa4` | `2d 41 00 91` | add x13,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeaa8"></a> `00bbeaa8` | `0a 00 0c 8b` | add x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00bbeaac"></a> `00bbeaac` | `29 01 0c 8b` | add x9,x9,x12 | `FALL_THROUGH`
<a id="insn-00bbeab0"></a> `00bbeab0` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeab4"></a> `00bbeab4` | `ef 03 0c aa` | mov x15,x12 | `FALL_THROUGH`
<a id="insn-00bbeab8"></a> `00bbeab8` | `a0 85 7f ad` | ldp q0,q1,[x13, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbeabc"></a> `00bbeabc` | `ad 81 00 91` | add x13,x13,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeac0"></a> `00bbeac0` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeac4"></a> `00bbeac4` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbeac8"></a> `00bbeac8` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeacc"></a> `00bbeacc` | `61 ff ff 54` | b.ne 0x00bbeab8 | `CONDITIONAL_JUMP`
<a id="insn-00bbead0"></a> `00bbead0` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbead4"></a> `00bbead4` | `e0 03 0a aa` | mov x0,x10 | `FALL_THROUGH`
<a id="insn-00bbead8"></a> `00bbead8` | `00 01 00 54` | b.eq 0x00bbeaf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbeadc"></a> `00bbeadc` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbeae0"></a> `00bbeae0` | `2b 15 40 38` | ldrb w11,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00bbeae4"></a> `00bbeae4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbeae8"></a> `00bbeae8` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbeaec"></a> `00bbeaec` | `a1 ff ff 54` | b.ne 0x00bbeae0 | `CONDITIONAL_JUMP`
<a id="insn-00bbeaf0"></a> `00bbeaf0` | `02 00 00 14` | b 0x00bbeaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeaf4"></a> `00bbeaf4` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00bbeaf8"></a> `00bbeaf8` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeafc"></a> `00bbeafc` | `42 00 00 14` | b 0x00bbec04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb00"></a> `00bbeb00` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bbeb04"></a> `00bbeb04` | `e2 00 00 54` | b.cs 0x00bbeb20 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb08"></a> `00bbeb08` | `0a 00 0c cb` | sub x10,x0,x12 | `FALL_THROUGH`
<a id="insn-00bbeb0c"></a> `00bbeb0c` | `0a 01 0a 8b` | add x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00bbeb10"></a> `00bbeb10` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00bbeb14"></a> `00bbeb14` | `69 00 00 54` | b.ls 0x00bbeb20 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb18"></a> `00bbeb18` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbeb1c"></a> `00bbeb1c` | `0f 00 00 14` | b 0x00bbeb58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb20"></a> `00bbeb20` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbeb24"></a> `00bbeb24` | `0e 40 00 91` | add x14,x0,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeb28"></a> `00bbeb28` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00bbeb2c"></a> `00bbeb2c` | `00 00 0d 8b` | add x0,x0,x13 | `FALL_THROUGH`
<a id="insn-00bbeb30"></a> `00bbeb30` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeb34"></a> `00bbeb34` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00bbeb38"></a> `00bbeb38` | `80 85 7f ad` | ldp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbeb3c"></a> `00bbeb3c` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeb40"></a> `00bbeb40` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeb44"></a> `00bbeb44` | `c0 85 3f ad` | stp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbeb48"></a> `00bbeb48` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeb4c"></a> `00bbeb4c` | `61 ff ff 54` | b.ne 0x00bbeb38 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb50"></a> `00bbeb50` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bbeb54"></a> `00bbeb54` | `a0 00 00 54` | b.eq 0x00bbeb68 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb58"></a> `00bbeb58` | `4b 15 40 38` | ldrb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbeb5c"></a> `00bbeb5c` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00bbeb60"></a> `00bbeb60` | `0b 14 00 38` | strb w11,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00bbeb64"></a> `00bbeb64` | `a1 ff ff 54` | b.ne 0x00bbeb58 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb68"></a> `00bbeb68` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bbeb6c"></a> `00bbeb6c` | `29 01 00 54` | b.ls 0x00bbeb90 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb70"></a> `00bbeb70` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbeb74"></a> `00bbeb74` | `6c 06 40 f9` | ldr x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeb78"></a> `00bbeb78` | `2b 01 08 eb` | subs x11,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbeb7c"></a> `00bbeb7c` | `20 04 00 54` | b.eq 0x00bbec00 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb80"></a> `00bbeb80` | `7f 81 00 f1` | cmp x11,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeb84"></a> `00bbeb84` | `a2 00 00 54` | b.cs 0x00bbeb98 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb88"></a> `00bbeb88` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbeb8c"></a> `00bbeb8c` | `18 00 00 14` | b 0x00bbebec | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb90"></a> `00bbeb90` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeb94"></a> `00bbeb94` | `1c 00 00 14` | b 0x00bbec04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb98"></a> `00bbeb98` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bbeb9c"></a> `00bbeb9c` | `c9 00 00 54` | b.ls 0x00bbebb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbeba0"></a> `00bbeba0` | `8a 01 0b 8b` | add x10,x12,x11 | `FALL_THROUGH`
<a id="insn-00bbeba4"></a> `00bbeba4` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00bbeba8"></a> `00bbeba8` | `69 00 00 54` | b.ls 0x00bbebb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbebac"></a> `00bbebac` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bbebb0"></a> `00bbebb0` | `0f 00 00 14` | b 0x00bbebec | `UNCONDITIONAL_JUMP`
<a id="insn-00bbebb4"></a> `00bbebb4` | `6d e9 7b 92` | and x13,x11,#-0x20 | `FALL_THROUGH`
<a id="insn-00bbebb8"></a> `00bbebb8` | `0e 41 00 91` | add x14,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbebbc"></a> `00bbebbc` | `8a 01 0d 8b` | add x10,x12,x13 | `FALL_THROUGH`
<a id="insn-00bbebc0"></a> `00bbebc0` | `08 01 0d 8b` | add x8,x8,x13 | `FALL_THROUGH`
<a id="insn-00bbebc4"></a> `00bbebc4` | `8c 41 00 91` | add x12,x12,#0x10 | `FALL_THROUGH`
<a id="insn-00bbebc8"></a> `00bbebc8` | `ef 03 0d aa` | mov x15,x13 | `FALL_THROUGH`
<a id="insn-00bbebcc"></a> `00bbebcc` | `c0 85 7f ad` | ldp q0,q1,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbebd0"></a> `00bbebd0` | `ce 81 00 91` | add x14,x14,#0x20 | `FALL_THROUGH`
<a id="insn-00bbebd4"></a> `00bbebd4` | `ef 81 00 f1` | subs x15,x15,#0x20 | `FALL_THROUGH`
<a id="insn-00bbebd8"></a> `00bbebd8` | `80 85 3f ad` | stp q0,q1,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbebdc"></a> `00bbebdc` | `8c 81 00 91` | add x12,x12,#0x20 | `FALL_THROUGH`
<a id="insn-00bbebe0"></a> `00bbebe0` | `61 ff ff 54` | b.ne 0x00bbebcc | `CONDITIONAL_JUMP`
<a id="insn-00bbebe4"></a> `00bbebe4` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00bbebe8"></a> `00bbebe8` | `a0 00 00 54` | b.eq 0x00bbebfc | `CONDITIONAL_JUMP`
<a id="insn-00bbebec"></a> `00bbebec` | `0b 15 40 38` | ldrb w11,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00bbebf0"></a> `00bbebf0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbebf4"></a> `00bbebf4` | `4b 15 00 38` | strb w11,[x10], #0x1 | `FALL_THROUGH`
<a id="insn-00bbebf8"></a> `00bbebf8` | `a1 ff ff 54` | b.ne 0x00bbebec | `CONDITIONAL_JUMP`
<a id="insn-00bbebfc"></a> `00bbebfc` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bbec00"></a> `00bbec00` | `6c 06 00 f9` | str x12,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec04"></a> `00bbec04` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbec08"></a> `00bbec08` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbec0c"></a> `00bbec0c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbec10"></a> `00bbec10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbec14"></a> `00bbec14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbec18"></a> `00bbec18` | `3e 70 02 94` | bl 0x00c5ad10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbe9bc`](#insn-00bbe9bc) 範囲 `[['00bbe9bc', '00bbe9f3']]`
  - `CONDITIONAL_JUMP` [`00bbe9f0`](#insn-00bbe9f0) → [`00bbea30`](#insn-00bbea30)
  - `FALL_THROUGH` [`00bbe9f0`](#insn-00bbe9f0) → [`00bbe9f4`](#insn-00bbe9f4)
- ブロック [`00bbe9f4`](#insn-00bbe9f4) 範囲 `[['00bbe9f4', '00bbe9fb']]`
  - `CONDITIONAL_JUMP` [`00bbe9f8`](#insn-00bbe9f8) → [`00bbea10`](#insn-00bbea10)
  - `FALL_THROUGH` [`00bbe9f8`](#insn-00bbe9f8) → [`00bbe9fc`](#insn-00bbe9fc)
- ブロック [`00bbe9fc`](#insn-00bbe9fc) 範囲 `[['00bbe9fc', '00bbea0f']]`
  - `FALL_THROUGH` [`00bbea0c`](#insn-00bbea0c) → [`00bbea10`](#insn-00bbea10)
- ブロック [`00bbea10`](#insn-00bbea10) 範囲 `[['00bbea10', '00bbea13']]`
  - `CONDITIONAL_JUMP` [`00bbea10`](#insn-00bbea10) → [`00bbec14`](#insn-00bbec14)
  - `FALL_THROUGH` [`00bbea10`](#insn-00bbea10) → [`00bbea14`](#insn-00bbea14)
- ブロック [`00bbea14`](#insn-00bbea14) 範囲 `[['00bbea14', '00bbea1f']]`
  - `CONDITIONAL_JUMP` [`00bbea1c`](#insn-00bbea1c) → [`00bbea5c`](#insn-00bbea5c)
  - `FALL_THROUGH` [`00bbea1c`](#insn-00bbea1c) → [`00bbea20`](#insn-00bbea20)
- ブロック [`00bbea20`](#insn-00bbea20) 範囲 `[['00bbea20', '00bbea2f']]`
  - `UNCONDITIONAL_JUMP` [`00bbea2c`](#insn-00bbea2c) → [`00bbea60`](#insn-00bbea60)
- ブロック [`00bbea30`](#insn-00bbea30) 範囲 `[['00bbea30', '00bbea4b']]`
  - `CONDITIONAL_JUMP` [`00bbea48`](#insn-00bbea48) → [`00bbeb68`](#insn-00bbeb68)
  - `FALL_THROUGH` [`00bbea48`](#insn-00bbea48) → [`00bbea4c`](#insn-00bbea4c)
- ブロック [`00bbea4c`](#insn-00bbea4c) 範囲 `[['00bbea4c', '00bbea53']]`
  - `CONDITIONAL_JUMP` [`00bbea50`](#insn-00bbea50) → [`00bbeb00`](#insn-00bbeb00)
  - `FALL_THROUGH` [`00bbea50`](#insn-00bbea50) → [`00bbea54`](#insn-00bbea54)
- ブロック [`00bbea54`](#insn-00bbea54) 範囲 `[['00bbea54', '00bbea5b']]`
  - `UNCONDITIONAL_JUMP` [`00bbea58`](#insn-00bbea58) → [`00bbeb58`](#insn-00bbeb58)
- ブロック [`00bbea5c`](#insn-00bbea5c) 範囲 `[['00bbea5c', '00bbea5f']]`
  - `FALL_THROUGH` [`00bbea5c`](#insn-00bbea5c) → [`00bbea60`](#insn-00bbea60)
- ブロック [`00bbea60`](#insn-00bbea60) 範囲 `[['00bbea60', '00bbea83']]`
  - `CONDITIONAL_JUMP` [`00bbea80`](#insn-00bbea80) → [`00bbeaf4`](#insn-00bbeaf4)
  - `FALL_THROUGH` [`00bbea80`](#insn-00bbea80) → [`00bbea84`](#insn-00bbea84)
- ブロック [`00bbea84`](#insn-00bbea84) 範囲 `[['00bbea84', '00bbea8b']]`
  - `CONDITIONAL_JUMP` [`00bbea88`](#insn-00bbea88) → [`00bbeadc`](#insn-00bbeadc)
  - `FALL_THROUGH` [`00bbea88`](#insn-00bbea88) → [`00bbea8c`](#insn-00bbea8c)
- ブロック [`00bbea8c`](#insn-00bbea8c) 範囲 `[['00bbea8c', '00bbea93']]`
  - `CONDITIONAL_JUMP` [`00bbea90`](#insn-00bbea90) → [`00bbeaa0`](#insn-00bbeaa0)
  - `FALL_THROUGH` [`00bbea90`](#insn-00bbea90) → [`00bbea94`](#insn-00bbea94)
- ブロック [`00bbea94`](#insn-00bbea94) 範囲 `[['00bbea94', '00bbea9f']]`
  - `CONDITIONAL_JUMP` [`00bbea9c`](#insn-00bbea9c) → [`00bbeadc`](#insn-00bbeadc)
  - `FALL_THROUGH` [`00bbea9c`](#insn-00bbea9c) → [`00bbeaa0`](#insn-00bbeaa0)
- ブロック [`00bbeaa0`](#insn-00bbeaa0) 範囲 `[['00bbeaa0', '00bbeab7']]`
  - `FALL_THROUGH` [`00bbeab4`](#insn-00bbeab4) → [`00bbeab8`](#insn-00bbeab8)
- ブロック [`00bbeab8`](#insn-00bbeab8) 範囲 `[['00bbeab8', '00bbeacf']]`
  - `CONDITIONAL_JUMP` [`00bbeacc`](#insn-00bbeacc) → [`00bbeab8`](#insn-00bbeab8)
  - `FALL_THROUGH` [`00bbeacc`](#insn-00bbeacc) → [`00bbead0`](#insn-00bbead0)
- ブロック [`00bbead0`](#insn-00bbead0) 範囲 `[['00bbead0', '00bbeadb']]`
  - `CONDITIONAL_JUMP` [`00bbead8`](#insn-00bbead8) → [`00bbeaf8`](#insn-00bbeaf8)
  - `FALL_THROUGH` [`00bbead8`](#insn-00bbead8) → [`00bbeadc`](#insn-00bbeadc)
- ブロック [`00bbeadc`](#insn-00bbeadc) 範囲 `[['00bbeadc', '00bbeadf']]`
  - `FALL_THROUGH` [`00bbeadc`](#insn-00bbeadc) → [`00bbeae0`](#insn-00bbeae0)
- ブロック [`00bbeae0`](#insn-00bbeae0) 範囲 `[['00bbeae0', '00bbeaef']]`
  - `CONDITIONAL_JUMP` [`00bbeaec`](#insn-00bbeaec) → [`00bbeae0`](#insn-00bbeae0)
  - `FALL_THROUGH` [`00bbeaec`](#insn-00bbeaec) → [`00bbeaf0`](#insn-00bbeaf0)
- ブロック [`00bbeaf0`](#insn-00bbeaf0) 範囲 `[['00bbeaf0', '00bbeaf3']]`
  - `UNCONDITIONAL_JUMP` [`00bbeaf0`](#insn-00bbeaf0) → [`00bbeaf8`](#insn-00bbeaf8)
- ブロック [`00bbeaf4`](#insn-00bbeaf4) 範囲 `[['00bbeaf4', '00bbeaf7']]`
  - `FALL_THROUGH` [`00bbeaf4`](#insn-00bbeaf4) → [`00bbeaf8`](#insn-00bbeaf8)
- ブロック [`00bbeaf8`](#insn-00bbeaf8) 範囲 `[['00bbeaf8', '00bbeaff']]`
  - `UNCONDITIONAL_JUMP` [`00bbeafc`](#insn-00bbeafc) → [`00bbec04`](#insn-00bbec04)
- ブロック [`00bbeb00`](#insn-00bbeb00) 範囲 `[['00bbeb00', '00bbeb07']]`
  - `CONDITIONAL_JUMP` [`00bbeb04`](#insn-00bbeb04) → [`00bbeb20`](#insn-00bbeb20)
  - `FALL_THROUGH` [`00bbeb04`](#insn-00bbeb04) → [`00bbeb08`](#insn-00bbeb08)
- ブロック [`00bbeb08`](#insn-00bbeb08) 範囲 `[['00bbeb08', '00bbeb17']]`
  - `CONDITIONAL_JUMP` [`00bbeb14`](#insn-00bbeb14) → [`00bbeb20`](#insn-00bbeb20)
  - `FALL_THROUGH` [`00bbeb14`](#insn-00bbeb14) → [`00bbeb18`](#insn-00bbeb18)
- ブロック [`00bbeb18`](#insn-00bbeb18) 範囲 `[['00bbeb18', '00bbeb1f']]`
  - `UNCONDITIONAL_JUMP` [`00bbeb1c`](#insn-00bbeb1c) → [`00bbeb58`](#insn-00bbeb58)
- ブロック [`00bbeb20`](#insn-00bbeb20) 範囲 `[['00bbeb20', '00bbeb37']]`
  - `FALL_THROUGH` [`00bbeb34`](#insn-00bbeb34) → [`00bbeb38`](#insn-00bbeb38)
- ブロック [`00bbeb38`](#insn-00bbeb38) 範囲 `[['00bbeb38', '00bbeb4b']]`
  - `FALL_THROUGH` [`00bbeb48`](#insn-00bbeb48) → [`00bbeb4c`](#insn-00bbeb4c)
- ブロック [`00bbeb4c`](#insn-00bbeb4c) 範囲 `[['00bbeb4c', '00bbeb4f']]`
  - `CONDITIONAL_JUMP` [`00bbeb4c`](#insn-00bbeb4c) → [`00bbeb38`](#insn-00bbeb38)
  - `FALL_THROUGH` [`00bbeb4c`](#insn-00bbeb4c) → [`00bbeb50`](#insn-00bbeb50)
- ブロック [`00bbeb50`](#insn-00bbeb50) 範囲 `[['00bbeb50', '00bbeb57']]`
  - `CONDITIONAL_JUMP` [`00bbeb54`](#insn-00bbeb54) → [`00bbeb68`](#insn-00bbeb68)
  - `FALL_THROUGH` [`00bbeb54`](#insn-00bbeb54) → [`00bbeb58`](#insn-00bbeb58)
- ブロック [`00bbeb58`](#insn-00bbeb58) 範囲 `[['00bbeb58', '00bbeb67']]`
  - `CONDITIONAL_JUMP` [`00bbeb64`](#insn-00bbeb64) → [`00bbeb58`](#insn-00bbeb58)
  - `FALL_THROUGH` [`00bbeb64`](#insn-00bbeb64) → [`00bbeb68`](#insn-00bbeb68)
- ブロック [`00bbeb68`](#insn-00bbeb68) 範囲 `[['00bbeb68', '00bbeb6f']]`
  - `CONDITIONAL_JUMP` [`00bbeb6c`](#insn-00bbeb6c) → [`00bbeb90`](#insn-00bbeb90)
  - `FALL_THROUGH` [`00bbeb6c`](#insn-00bbeb6c) → [`00bbeb70`](#insn-00bbeb70)
- ブロック [`00bbeb70`](#insn-00bbeb70) 範囲 `[['00bbeb70', '00bbeb7f']]`
  - `CONDITIONAL_JUMP` [`00bbeb7c`](#insn-00bbeb7c) → [`00bbec00`](#insn-00bbec00)
  - `FALL_THROUGH` [`00bbeb7c`](#insn-00bbeb7c) → [`00bbeb80`](#insn-00bbeb80)
- ブロック [`00bbeb80`](#insn-00bbeb80) 範囲 `[['00bbeb80', '00bbeb87']]`
  - `CONDITIONAL_JUMP` [`00bbeb84`](#insn-00bbeb84) → [`00bbeb98`](#insn-00bbeb98)
  - `FALL_THROUGH` [`00bbeb84`](#insn-00bbeb84) → [`00bbeb88`](#insn-00bbeb88)
- ブロック [`00bbeb88`](#insn-00bbeb88) 範囲 `[['00bbeb88', '00bbeb8f']]`
  - `UNCONDITIONAL_JUMP` [`00bbeb8c`](#insn-00bbeb8c) → [`00bbebec`](#insn-00bbebec)
- ブロック [`00bbeb90`](#insn-00bbeb90) 範囲 `[['00bbeb90', '00bbeb97']]`
  - `UNCONDITIONAL_JUMP` [`00bbeb94`](#insn-00bbeb94) → [`00bbec04`](#insn-00bbec04)
- ブロック [`00bbeb98`](#insn-00bbeb98) 範囲 `[['00bbeb98', '00bbeb9f']]`
  - `CONDITIONAL_JUMP` [`00bbeb9c`](#insn-00bbeb9c) → [`00bbebb4`](#insn-00bbebb4)
  - `FALL_THROUGH` [`00bbeb9c`](#insn-00bbeb9c) → [`00bbeba0`](#insn-00bbeba0)
- ブロック [`00bbeba0`](#insn-00bbeba0) 範囲 `[['00bbeba0', '00bbebab']]`
  - `CONDITIONAL_JUMP` [`00bbeba8`](#insn-00bbeba8) → [`00bbebb4`](#insn-00bbebb4)
  - `FALL_THROUGH` [`00bbeba8`](#insn-00bbeba8) → [`00bbebac`](#insn-00bbebac)
- ブロック [`00bbebac`](#insn-00bbebac) 範囲 `[['00bbebac', '00bbebb3']]`
  - `UNCONDITIONAL_JUMP` [`00bbebb0`](#insn-00bbebb0) → [`00bbebec`](#insn-00bbebec)
- ブロック [`00bbebb4`](#insn-00bbebb4) 範囲 `[['00bbebb4', '00bbebcb']]`
  - `FALL_THROUGH` [`00bbebc8`](#insn-00bbebc8) → [`00bbebcc`](#insn-00bbebcc)
- ブロック [`00bbebcc`](#insn-00bbebcc) 範囲 `[['00bbebcc', '00bbebe3']]`
  - `CONDITIONAL_JUMP` [`00bbebe0`](#insn-00bbebe0) → [`00bbebcc`](#insn-00bbebcc)
  - `FALL_THROUGH` [`00bbebe0`](#insn-00bbebe0) → [`00bbebe4`](#insn-00bbebe4)
- ブロック [`00bbebe4`](#insn-00bbebe4) 範囲 `[['00bbebe4', '00bbebeb']]`
  - `CONDITIONAL_JUMP` [`00bbebe8`](#insn-00bbebe8) → [`00bbebfc`](#insn-00bbebfc)
  - `FALL_THROUGH` [`00bbebe8`](#insn-00bbebe8) → [`00bbebec`](#insn-00bbebec)
- ブロック [`00bbebec`](#insn-00bbebec) 範囲 `[['00bbebec', '00bbebfb']]`
  - `CONDITIONAL_JUMP` [`00bbebf8`](#insn-00bbebf8) → [`00bbebec`](#insn-00bbebec)
  - `FALL_THROUGH` [`00bbebf8`](#insn-00bbebf8) → [`00bbebfc`](#insn-00bbebfc)
- ブロック [`00bbebfc`](#insn-00bbebfc) 範囲 `[['00bbebfc', '00bbebff']]`
  - `FALL_THROUGH` [`00bbebfc`](#insn-00bbebfc) → [`00bbec00`](#insn-00bbec00)
- ブロック [`00bbec00`](#insn-00bbec00) 範囲 `[['00bbec00', '00bbec03']]`
  - `FALL_THROUGH` [`00bbec00`](#insn-00bbec00) → [`00bbec04`](#insn-00bbec04)
- ブロック [`00bbec04`](#insn-00bbec04) 範囲 `[['00bbec04', '00bbec13']]`
- ブロック [`00bbec14`](#insn-00bbec14) 範囲 `[['00bbec14', '00bbec1b']]`

## 命令位置別の参照

- [`00bbe9bc`](#insn-00bbe9bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe9c0`](#insn-00bbe9c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe9c4`](#insn-00bbe9c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe9f0`](#insn-00bbe9f0) → [`00bbea30`](#insn-00bbea30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe9f8`](#insn-00bbe9f8) → [`00bbea10`](#insn-00bbea10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea00`](#insn-00bbea00) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbea10`](#insn-00bbea10) → [`00bbec14`](#insn-00bbec14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea1c`](#insn-00bbea1c) → [`00bbea5c`](#insn-00bbea5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea2c`](#insn-00bbea2c) → [`00bbea60`](#insn-00bbea60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea48`](#insn-00bbea48) → [`00bbeb68`](#insn-00bbeb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea50`](#insn-00bbea50) → [`00bbeb00`](#insn-00bbeb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea58`](#insn-00bbea58) → [`00bbeb58`](#insn-00bbeb58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea64`](#insn-00bbea64) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bbea80`](#insn-00bbea80) → [`00bbeaf4`](#insn-00bbeaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea88`](#insn-00bbea88) → [`00bbeadc`](#insn-00bbeadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea90`](#insn-00bbea90) → [`00bbeaa0`](#insn-00bbeaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea9c`](#insn-00bbea9c) → [`00bbeadc`](#insn-00bbeadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeacc`](#insn-00bbeacc) → [`00bbeab8`](#insn-00bbeab8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbead8`](#insn-00bbead8) → [`00bbeaf8`](#insn-00bbeaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeaec`](#insn-00bbeaec) → [`00bbeae0`](#insn-00bbeae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeaf0`](#insn-00bbeaf0) → [`00bbeaf8`](#insn-00bbeaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeafc`](#insn-00bbeafc) → [`00bbec04`](#insn-00bbec04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb04`](#insn-00bbeb04) → [`00bbeb20`](#insn-00bbeb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb14`](#insn-00bbeb14) → [`00bbeb20`](#insn-00bbeb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb1c`](#insn-00bbeb1c) → [`00bbeb58`](#insn-00bbeb58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb4c`](#insn-00bbeb4c) → [`00bbeb38`](#insn-00bbeb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb54`](#insn-00bbeb54) → [`00bbeb68`](#insn-00bbeb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb64`](#insn-00bbeb64) → [`00bbeb58`](#insn-00bbeb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb6c`](#insn-00bbeb6c) → [`00bbeb90`](#insn-00bbeb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb7c`](#insn-00bbeb7c) → [`00bbec00`](#insn-00bbec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb84`](#insn-00bbeb84) → [`00bbeb98`](#insn-00bbeb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb8c`](#insn-00bbeb8c) → [`00bbebec`](#insn-00bbebec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb94`](#insn-00bbeb94) → [`00bbec04`](#insn-00bbec04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb9c`](#insn-00bbeb9c) → [`00bbebb4`](#insn-00bbebb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeba8`](#insn-00bbeba8) → [`00bbebb4`](#insn-00bbebb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebb0`](#insn-00bbebb0) → [`00bbebec`](#insn-00bbebec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebe0`](#insn-00bbebe0) → [`00bbebcc`](#insn-00bbebcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebe8`](#insn-00bbebe8) → [`00bbebfc`](#insn-00bbebfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebf8`](#insn-00bbebf8) → [`00bbebec`](#insn-00bbebec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec04`](#insn-00bbec04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec08`](#insn-00bbec08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec18`](#insn-00bbec18) → [`00c5ad10`](../00c5a/00c5ad10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbe9bc`](#insn-00bbe9bc)

~~~json
{
  "source": "00bbe9bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe9c0`](#insn-00bbe9c0)

~~~json
{
  "source": "00bbe9c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe9c4`](#insn-00bbe9c4)

~~~json
{
  "source": "00bbe9c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe9f0`](#insn-00bbe9f0)

~~~json
{
  "source": "00bbe9f0",
  "target": "00bbea30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe9f8`](#insn-00bbe9f8)

~~~json
{
  "source": "00bbe9f8",
  "target": "00bbea10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea00`](#insn-00bbea00)

~~~json
{
  "source": "00bbea00",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbea10`](#insn-00bbea10)

~~~json
{
  "source": "00bbea10",
  "target": "00bbec14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea1c`](#insn-00bbea1c)

~~~json
{
  "source": "00bbea1c",
  "target": "00bbea5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea2c`](#insn-00bbea2c)

~~~json
{
  "source": "00bbea2c",
  "target": "00bbea60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea48`](#insn-00bbea48)

~~~json
{
  "source": "00bbea48",
  "target": "00bbeb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea50`](#insn-00bbea50)

~~~json
{
  "source": "00bbea50",
  "target": "00bbeb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea58`](#insn-00bbea58)

~~~json
{
  "source": "00bbea58",
  "target": "00bbeb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea64`](#insn-00bbea64)

~~~json
{
  "source": "00bbea64",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbea80`](#insn-00bbea80)

~~~json
{
  "source": "00bbea80",
  "target": "00bbeaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea88`](#insn-00bbea88)

~~~json
{
  "source": "00bbea88",
  "target": "00bbeadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea90`](#insn-00bbea90)

~~~json
{
  "source": "00bbea90",
  "target": "00bbeaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea9c`](#insn-00bbea9c)

~~~json
{
  "source": "00bbea9c",
  "target": "00bbeadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeacc`](#insn-00bbeacc)

~~~json
{
  "source": "00bbeacc",
  "target": "00bbeab8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbead8`](#insn-00bbead8)

~~~json
{
  "source": "00bbead8",
  "target": "00bbeaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeaec`](#insn-00bbeaec)

~~~json
{
  "source": "00bbeaec",
  "target": "00bbeae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeaf0`](#insn-00bbeaf0)

~~~json
{
  "source": "00bbeaf0",
  "target": "00bbeaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeafc`](#insn-00bbeafc)

~~~json
{
  "source": "00bbeafc",
  "target": "00bbec04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb04`](#insn-00bbeb04)

~~~json
{
  "source": "00bbeb04",
  "target": "00bbeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb14`](#insn-00bbeb14)

~~~json
{
  "source": "00bbeb14",
  "target": "00bbeb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb1c`](#insn-00bbeb1c)

~~~json
{
  "source": "00bbeb1c",
  "target": "00bbeb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb4c`](#insn-00bbeb4c)

~~~json
{
  "source": "00bbeb4c",
  "target": "00bbeb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb54`](#insn-00bbeb54)

~~~json
{
  "source": "00bbeb54",
  "target": "00bbeb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb64`](#insn-00bbeb64)

~~~json
{
  "source": "00bbeb64",
  "target": "00bbeb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb6c`](#insn-00bbeb6c)

~~~json
{
  "source": "00bbeb6c",
  "target": "00bbeb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb7c`](#insn-00bbeb7c)

~~~json
{
  "source": "00bbeb7c",
  "target": "00bbec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb84`](#insn-00bbeb84)

~~~json
{
  "source": "00bbeb84",
  "target": "00bbeb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb8c`](#insn-00bbeb8c)

~~~json
{
  "source": "00bbeb8c",
  "target": "00bbebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb94`](#insn-00bbeb94)

~~~json
{
  "source": "00bbeb94",
  "target": "00bbec04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb9c`](#insn-00bbeb9c)

~~~json
{
  "source": "00bbeb9c",
  "target": "00bbebb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeba8`](#insn-00bbeba8)

~~~json
{
  "source": "00bbeba8",
  "target": "00bbebb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebb0`](#insn-00bbebb0)

~~~json
{
  "source": "00bbebb0",
  "target": "00bbebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebe0`](#insn-00bbebe0)

~~~json
{
  "source": "00bbebe0",
  "target": "00bbebcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebe8`](#insn-00bbebe8)

~~~json
{
  "source": "00bbebe8",
  "target": "00bbebfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebf8`](#insn-00bbebf8)

~~~json
{
  "source": "00bbebf8",
  "target": "00bbebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec04`](#insn-00bbec04)

~~~json
{
  "source": "00bbec04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec08`](#insn-00bbec08)

~~~json
{
  "source": "00bbec08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec18`](#insn-00bbec18)

~~~json
{
  "source": "00bbec18",
  "target": "00c5ad10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
