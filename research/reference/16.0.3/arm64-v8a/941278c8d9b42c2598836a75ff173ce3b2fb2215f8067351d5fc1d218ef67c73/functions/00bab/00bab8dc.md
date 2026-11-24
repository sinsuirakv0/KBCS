# 00bab8dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baa8e8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baa8e8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-b267ab2ca0fb77895f865cc387c2b909)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab8dc",
  "name": "_ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_",
  "size": 696,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b82ee4374b4a8df2df81cb57bc53ee6ec8e387aa799b012a657bad02d1d566f3",
  "source_text_sha256": "b82ee4374b4a8df2df81cb57bc53ee6ec8e387aa799b012a657bad02d1d566f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bab8dc",
        "00babb93"
      ]
    ],
    "bytes_sha256": "5caccbd96f705d0771b5de22a73e5fd0cf89ee3f828078d612c26b82eae6bbd1",
    "instruction_count": 174,
    "instruction_bytes": 696,
    "body_bytes": 696,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dc10](../00c5d/00c5dc10.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6404 bytes

~~~c

void _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_
               (ulong *param_1,undefined8 *param_2)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  undefined8 *puVar10;
  byte *pbVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  
                    /* try { // try from 00bab8ec to 00cab8f7 has its CatchHandler @ 00bacf14 */
  puVar10 = (undefined8 *)param_1[2];
                    /* try { // try from 00bab8f8 to 00cab917 has its CatchHandler @ 00bad0c4 */
  if (puVar10 == (undefined8 *)param_1[3]) {
    puVar6 = (undefined8 *)*param_1;
    puVar9 = (undefined8 *)param_1[1];
    if (puVar9 < puVar6 || (long)puVar9 - (long)puVar6 == 0) {
                    /* try { // try from 00bab9e8 to 00cab9f3 has its CatchHandler @ 00bacfb0 */
      lVar4 = (long)param_1[3] - (long)puVar6;
      uVar5 = (lVar4 >> 3) * 0x1c71c71c71c71c72;
      if (lVar4 == 0) {
        uVar5 = 1;
      }
                    /* try { // try from 00baba14 to 00caba1f has its CatchHandler @ 00bacf70 */
      if (0x38e38e38e38e38e < uVar5) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      uVar2 = _Znwm(uVar5 * 0x48);
      lVar4 = (long)puVar10 - (long)puVar9;
      puVar7 = (undefined8 *)(uVar2 + (uVar5 >> 2) * 0x48);
                    /* try { // try from 00baba38 to 00caba43 has its CatchHandler @ 00bacf60 */
      puVar8 = puVar7;
      if (lVar4 != 0) {
        lVar3 = 0;
                    /* try { // try from 00baba64 to 00caba6f has its CatchHandler @ 00bacf20 */
        puVar10 = puVar7;
        do {
          puVar6 = (undefined8 *)((long)puVar9 + lVar3);
          uVar12 = *puVar6;
          uVar14 = puVar6[3];
          uVar13 = puVar6[2];
          lVar1 = uVar2 + (uVar5 >> 2) * 0x48 + lVar3;
          lVar3 = lVar3 + 0x48;
                    /* try { // try from 00baba88 to 00caba93 has its CatchHandler @ 00bacf10 */
          puVar10[1] = puVar6[1];
          *puVar10 = uVar12;
          puVar10[3] = uVar14;
          puVar10[2] = uVar13;
          uVar13 = puVar6[5];
          uVar12 = puVar6[4];
                    /* try { // try from 00baba94 to 00cabab3 has its CatchHandler @ 00bad0c0 */
          *(undefined8 *)(lVar1 + 0x30) = puVar6[6];
          *(undefined8 *)(lVar1 + 0x28) = uVar13;
          *(undefined8 *)(lVar1 + 0x20) = uVar12;
          puVar6[5] = 0;
          puVar6[6] = 0;
          puVar6[4] = 0;
          *(undefined2 *)(lVar1 + 0x38) = *(undefined2 *)(puVar6 + 7);
          *(undefined8 *)(lVar1 + 0x40) = puVar6[8];
                    /* try { // try from 00babab4 to 00cabaeb has its CatchHandler @ 00bad130 */
          puVar10 = (undefined8 *)(lVar1 + 0x48);
        } while ((lVar4 >> 3) * 8 - lVar3 != 0);
        puVar6 = (undefined8 *)*param_1;
        puVar9 = (undefined8 *)param_1[1];
        puVar10 = (undefined8 *)param_1[2];
        puVar8 = (undefined8 *)((long)puVar7 + lVar4);
      }
      *param_1 = uVar2;
      param_1[1] = (ulong)puVar7;
      param_1[2] = (ulong)puVar8;
      param_1[3] = uVar2 + uVar5 * 0x48;
      while (puVar8 = puVar10, puVar8 != puVar9) {
        puVar10 = puVar8 + -9;
        if ((*(byte *)(puVar8 + -5) & 1) != 0) {
          _ZdlPv((void *)puVar8[-3]);
        }
      }
      if (puVar6 != (undefined8 *)0x0) {
        _ZdlPv(puVar6);
      }
    }
    else {
                    /* try { // try from 00bab918 to 00cab94f has its CatchHandler @ 00bad134 */
      lVar3 = ((long)puVar9 - (long)puVar6 >> 3) * -0x71c71c71c71c71c7;
      lVar4 = lVar3 + 2;
      if (-1 < lVar3 + 1) {
        lVar4 = lVar3 + 1;
      }
      lVar4 = lVar4 >> 1;
      if (puVar9 == puVar10) {
        puVar6 = puVar9 + lVar4 * -9;
      }
      else {
        do {
          uVar12 = *(undefined8 *)((long)puVar9 + 10);
          uVar14 = puVar9[1];
          uVar13 = *puVar9;
          puVar6 = puVar9 + lVar4 * -9;
                    /* try { // try from 00bab9a8 to 00cab9ab has its CatchHandler @ 00bad000 */
          *(undefined8 *)((long)puVar6 + 0x12) = *(undefined8 *)((long)puVar9 + 0x12);
          *(undefined8 *)((long)puVar6 + 10) = uVar12;
          puVar6[1] = uVar14;
          *puVar6 = uVar13;
          pbVar11 = (byte *)(puVar6 + 4);
          if ((*pbVar11 & 1) == 0) {
            *(undefined1 *)((long)puVar6 + 0x21) = 0;
            *pbVar11 = 0;
          }
          else {
            *(undefined1 *)puVar6[6] = 0;
            puVar6[5] = 0;
                    /* try { // try from 00bab9c8 to 00cab9d3 has its CatchHandler @ 00bacfc0 */
            if ((*pbVar11 & 1) != 0) {
              _ZdlPv((void *)puVar6[6]);
              puVar9[lVar4 * -9 + 4] = 0;
            }
          }
          uVar13 = puVar9[5];
          uVar12 = puVar9[4];
          puVar6[6] = puVar9[6];
                    /* try { // try from 00bab970 to 00cab97b has its CatchHandler @ 00bad070 */
          puVar6[5] = uVar13;
          *(undefined8 *)pbVar11 = uVar12;
          puVar9[5] = 0;
          puVar9[6] = 0;
          puVar9[4] = 0;
          *(undefined2 *)(puVar9 + lVar4 * -9 + 7) = *(undefined2 *)(puVar9 + 7);
          puVar6 = puVar9 + 9;
          puVar9[lVar4 * -9 + 8] = puVar9[8];
          puVar9 = puVar6;
                    /* try { // try from 00bab994 to 00cab99f has its CatchHandler @ 00bad060 */
        } while (puVar10 != puVar6);
        puVar10 = (undefined8 *)param_1[1];
        puVar6 = puVar6 + lVar4 * -9;
      }
      param_1[1] = (ulong)(puVar10 + lVar4 * -9);
      param_1[2] = (ulong)puVar6;
    }
  }
  puVar10 = (undefined8 *)param_1[2];
  uVar12 = *param_2;
  uVar14 = param_2[3];
  uVar13 = param_2[2];
  puVar10[1] = param_2[1];
  *puVar10 = uVar12;
  puVar10[3] = uVar14;
  puVar10[2] = uVar13;
  uVar13 = param_2[5];
  uVar12 = param_2[4];
                    /* try { // try from 00babb28 to 00cabb2b has its CatchHandler @ 00bace2c */
  puVar10[6] = param_2[6];
  puVar10[5] = uVar13;
  puVar10[4] = uVar12;
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar10 + 7) = *(undefined2 *)(param_2 + 7);
  puVar10[8] = param_2[8];
  param_1[2] = param_1[2] + 0x48;
                    /* try { // try from 00babb68 to 00cabb7b has its CatchHandler @ 00bacb48 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bab8dc"></a> `00bab8dc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bab8e0"></a> `00bab8e0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab8e4"></a> `00bab8e4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab8e8"></a> `00bab8e8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab8ec"></a> `00bab8ec` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab8f0"></a> `00bab8f0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bab8f4"></a> `00bab8f4` | `18 20 41 a9` | ldp x24,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bab8f8"></a> `00bab8f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bab8fc"></a> `00bab8fc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bab900"></a> `00bab900` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bab904"></a> `00bab904` | `81 10 00 54` | b.ne 0x00babb14 | `CONDITIONAL_JUMP`
<a id="insn-00bab908"></a> `00bab908` | `75 5e 40 a9` | ldp x21,x23,[x19] | `FALL_THROUGH`
<a id="insn-00bab90c"></a> `00bab90c` | `e9 02 15 eb` | subs x9,x23,x21 | `FALL_THROUGH`
<a id="insn-00bab910"></a> `00bab910` | `89 06 00 54` | b.ls 0x00bab9e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab914"></a> `00bab914` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bab918"></a> `00bab918` | `29 c7 91 d2` | mov x9,#0x8e39 | `FALL_THROUGH`
<a id="insn-00bab91c"></a> `00bab91c` | `69 1c a7 f2` | movk x9,#0x38e3, LSL #16 | `FALL_THROUGH`
<a id="insn-00bab920"></a> `00bab920` | `c9 71 dc f2` | movk x9,#0xe38e, LSL #32 | `FALL_THROUGH`
<a id="insn-00bab924"></a> `00bab924` | `09 c7 f1 f2` | movk x9,#0x8e38, LSL #48 | `FALL_THROUGH`
<a id="insn-00bab928"></a> `00bab928` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bab92c"></a> `00bab92c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab930"></a> `00bab930` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bab934"></a> `00bab934` | `3f 01 00 f1` | cmp x9,#0x0 | `FALL_THROUGH`
<a id="insn-00bab938"></a> `00bab938` | `48 b5 88 9a` | csinc x8,x10,x8,lt | `FALL_THROUGH`
<a id="insn-00bab93c"></a> `00bab93c` | `08 fd 41 93` | asr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab940"></a> `00bab940` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00bab944"></a> `00bab944` | `f5 03 08 cb` | neg x21,x8 | `FALL_THROUGH`
<a id="insn-00bab948"></a> `00bab948` | `80 0c 00 54` | b.eq 0x00babad8 | `CONDITIONAL_JUMP`
<a id="insn-00bab94c"></a> `00bab94c` | `a8 0e 15 8b` | add x8,x21,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bab950"></a> `00bab950` | `16 f1 7d d3` | lsl x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bab954"></a> `00bab954` | `11 00 00 14` | b 0x00bab998 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab958"></a> `00bab958` | `1f 85 00 39` | strb wzr,[x8, #0x21] | `FALL_THROUGH`
<a id="insn-00bab95c"></a> `00bab95c` | `3f 03 00 39` | strb wzr,[x25] | `FALL_THROUGH`
<a id="insn-00bab960"></a> `00bab960` | `e8 1a 40 f9` | ldr x8,[x23, #0x30] | `FALL_THROUGH`
<a id="insn-00bab964"></a> `00bab964` | `e0 0a c0 3d` | ldr q0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00bab968"></a> `00bab968` | `e9 02 16 8b` | add x9,x23,x22 | `FALL_THROUGH`
<a id="insn-00bab96c"></a> `00bab96c` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bab970"></a> `00bab970` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00bab974"></a> `00bab974` | `e8 72 40 79` | ldrh w8,[x23, #0x38] | `FALL_THROUGH`
<a id="insn-00bab978"></a> `00bab978` | `ff fe 02 a9` | stp xzr,xzr,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bab97c"></a> `00bab97c` | `ff 12 00 f9` | str xzr,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00bab980"></a> `00bab980` | `28 71 00 79` | strh w8,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-00bab984"></a> `00bab984` | `e8 22 40 f9` | ldr x8,[x23, #0x40] | `FALL_THROUGH`
<a id="insn-00bab988"></a> `00bab988` | `f7 22 01 91` | add x23,x23,#0x48 | `FALL_THROUGH`
<a id="insn-00bab98c"></a> `00bab98c` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bab990"></a> `00bab990` | `28 21 00 f9` | str x8,[x9, #0x40] | `FALL_THROUGH`
<a id="insn-00bab994"></a> `00bab994` | `a0 09 00 54` | b.eq 0x00babac8 | `CONDITIONAL_JUMP`
<a id="insn-00bab998"></a> `00bab998` | `e0 a2 c0 3c` | ldur q0,[x23, #0xa] | `FALL_THROUGH`
<a id="insn-00bab99c"></a> `00bab99c` | `e1 02 c0 3d` | ldr q1,[x23] | `FALL_THROUGH`
<a id="insn-00bab9a0"></a> `00bab9a0` | `e8 02 16 8b` | add x8,x23,x22 | `FALL_THROUGH`
<a id="insn-00bab9a4"></a> `00bab9a4` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00bab9a8"></a> `00bab9a8` | `00 a1 80 3c` | stur q0,[x8, #0xa] | `FALL_THROUGH`
<a id="insn-00bab9ac"></a> `00bab9ac` | `01 01 80 3d` | str q1,[x8] | `FALL_THROUGH`
<a id="insn-00bab9b0"></a> `00bab9b0` | `29 0f 42 38` | ldrb w9,[x25, #0x20]! | `FALL_THROUGH`
<a id="insn-00bab9b4"></a> `00bab9b4` | `29 fd 07 36` | tbz w9,#0x0,0x00bab958 | `CONDITIONAL_JUMP`
<a id="insn-00bab9b8"></a> `00bab9b8` | `09 19 40 f9` | ldr x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bab9bc"></a> `00bab9bc` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00bab9c0"></a> `00bab9c0` | `1f 15 00 f9` | str xzr,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bab9c4"></a> `00bab9c4` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bab9c8"></a> `00bab9c8` | `c9 fc 07 36` | tbz w9,#0x0,0x00bab960 | `CONDITIONAL_JUMP`
<a id="insn-00bab9cc"></a> `00bab9cc` | `00 19 40 f9` | ldr x0,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bab9d0"></a> `00bab9d0` | `60 b5 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab9d4"></a> `00bab9d4` | `e8 02 16 8b` | add x8,x23,x22 | `FALL_THROUGH`
<a id="insn-00bab9d8"></a> `00bab9d8` | `1f 11 00 f9` | str xzr,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bab9dc"></a> `00bab9dc` | `e1 ff ff 17` | b 0x00bab960 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab9e0"></a> `00bab9e0` | `49 8e 83 d2` | mov x9,#0x1c72 | `FALL_THROUGH`
<a id="insn-00bab9e4"></a> `00bab9e4` | `e9 38 ae f2` | movk x9,#0x71c7, LSL #16 | `FALL_THROUGH`
<a id="insn-00bab9e8"></a> `00bab9e8` | `08 01 15 eb` | subs x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bab9ec"></a> `00bab9ec` | `89 e3 d8 f2` | movk x9,#0xc71c, LSL #32 | `FALL_THROUGH`
<a id="insn-00bab9f0"></a> `00bab9f0` | `29 8e e3 f2` | movk x9,#0x1c71, LSL #48 | `FALL_THROUGH`
<a id="insn-00bab9f4"></a> `00bab9f4` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bab9f8"></a> `00bab9f8` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bab9fc"></a> `00bab9fc` | `e9 71 9c d2` | mov x9,#0xe38f | `FALL_THROUGH`
<a id="insn-00baba00"></a> `00baba00` | `09 c7 b1 f2` | movk x9,#0x8e38, LSL #16 | `FALL_THROUGH`
<a id="insn-00baba04"></a> `00baba04` | `69 1c c7 f2` | movk x9,#0x38e3, LSL #32 | `FALL_THROUGH`
<a id="insn-00baba08"></a> `00baba08` | `08 15 9f 9a` | csinc x8,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00baba0c"></a> `00baba0c` | `c9 71 e0 f2` | movk x9,#0x38e, LSL #48 | `FALL_THROUGH`
<a id="insn-00baba10"></a> `00baba10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baba14"></a> `00baba14` | `e2 0b 00 54` | b.cs 0x00babb90 | `CONDITIONAL_JUMP`
<a id="insn-00baba18"></a> `00baba18` | `19 fd 42 d3` | lsr x25,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00baba1c"></a> `00baba1c` | `08 0d 08 8b` | add x8,x8,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00baba20"></a> `00baba20` | `16 f1 7d d3` | lsl x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baba24"></a> `00baba24` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baba28"></a> `00baba28` | `42 b5 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00baba2c"></a> `00baba2c` | `08 09 80 52` | mov w8,#0x48 | `FALL_THROUGH`
<a id="insn-00baba30"></a> `00baba30` | `0a 03 17 eb` | subs x10,x24,x23 | `FALL_THROUGH`
<a id="insn-00baba34"></a> `00baba34` | `29 03 08 9b` | madd x9,x25,x8,x0 | `FALL_THROUGH`
<a id="insn-00baba38"></a> `00baba38` | `08 00 16 8b` | add x8,x0,x22 | `FALL_THROUGH`
<a id="insn-00baba3c"></a> `00baba3c` | `c0 05 00 54` | b.eq 0x00babaf4 | `CONDITIONAL_JUMP`
<a id="insn-00baba40"></a> `00baba40` | `2d c7 91 d2` | mov x13,#0x8e39 | `FALL_THROUGH`
<a id="insn-00baba44"></a> `00baba44` | `6d 1c a7 f2` | movk x13,#0x38e3, LSL #16 | `FALL_THROUGH`
<a id="insn-00baba48"></a> `00baba48` | `cd 71 dc f2` | movk x13,#0xe38e, LSL #32 | `FALL_THROUGH`
<a id="insn-00baba4c"></a> `00baba4c` | `4c fd 43 93` | asr x12,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00baba50"></a> `00baba50` | `0d c7 f1 f2` | movk x13,#0x8e38, LSL #48 | `FALL_THROUGH`
<a id="insn-00baba54"></a> `00baba54` | `8c 7d 0d 9b` | mul x12,x12,x13 | `FALL_THROUGH`
<a id="insn-00baba58"></a> `00baba58` | `0e 09 80 52` | mov w14,#0x48 | `FALL_THROUGH`
<a id="insn-00baba5c"></a> `00baba5c` | `8c 0d 0c 8b` | add x12,x12,x12, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00baba60"></a> `00baba60` | `eb 03 1f aa` | mov x11,xzr | `FALL_THROUGH`
<a id="insn-00baba64"></a> `00baba64` | `2a 01 0a 8b` | add x10,x9,x10 | `FALL_THROUGH`
<a id="insn-00baba68"></a> `00baba68` | `8c f1 7d d3` | lsl x12,x12,#0x3 | `FALL_THROUGH`
<a id="insn-00baba6c"></a> `00baba6c` | `2d 03 0e 9b` | madd x13,x25,x14,x0 | `FALL_THROUGH`
<a id="insn-00baba70"></a> `00baba70` | `ee 03 09 aa` | mov x14,x9 | `FALL_THROUGH`
<a id="insn-00baba74"></a> `00baba74` | `ef 02 0b 8b` | add x15,x23,x11 | `FALL_THROUGH`
<a id="insn-00baba78"></a> `00baba78` | `e0 05 40 ad` | ldp q0,q1,[x15] | `FALL_THROUGH`
<a id="insn-00baba7c"></a> `00baba7c` | `b0 01 0b 8b` | add x16,x13,x11 | `FALL_THROUGH`
<a id="insn-00baba80"></a> `00baba80` | `6b 21 01 91` | add x11,x11,#0x48 | `FALL_THROUGH`
<a id="insn-00baba84"></a> `00baba84` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00baba88"></a> `00baba88` | `c0 05 00 ad` | stp q0,q1,[x14] | `FALL_THROUGH`
<a id="insn-00baba8c"></a> `00baba8c` | `ee 19 40 f9` | ldr x14,[x15, #0x30] | `FALL_THROUGH`
<a id="insn-00baba90"></a> `00baba90` | `e0 09 c0 3d` | ldr q0,[x15, #0x20] | `FALL_THROUGH`
<a id="insn-00baba94"></a> `00baba94` | `0e 1a 00 f9` | str x14,[x16, #0x30] | `FALL_THROUGH`
<a id="insn-00baba98"></a> `00baba98` | `00 0a 80 3d` | str q0,[x16, #0x20] | `FALL_THROUGH`
<a id="insn-00baba9c"></a> `00baba9c` | `ee 71 40 79` | ldrh w14,[x15, #0x38] | `FALL_THROUGH`
<a id="insn-00babaa0"></a> `00babaa0` | `ff fd 02 a9` | stp xzr,xzr,[x15, #0x28] | `FALL_THROUGH`
<a id="insn-00babaa4"></a> `00babaa4` | `ff 11 00 f9` | str xzr,[x15, #0x20] | `FALL_THROUGH`
<a id="insn-00babaa8"></a> `00babaa8` | `0e 72 00 79` | strh w14,[x16, #0x38] | `FALL_THROUGH`
<a id="insn-00babaac"></a> `00babaac` | `ee 21 40 f9` | ldr x14,[x15, #0x40] | `FALL_THROUGH`
<a id="insn-00babab0"></a> `00babab0` | `0e 22 00 f9` | str x14,[x16, #0x40] | `FALL_THROUGH`
<a id="insn-00babab4"></a> `00babab4` | `0e 22 01 91` | add x14,x16,#0x48 | `FALL_THROUGH`
<a id="insn-00babab8"></a> `00babab8` | `e1 fd ff 54` | b.ne 0x00baba74 | `CONDITIONAL_JUMP`
<a id="insn-00bababc"></a> `00bababc` | `75 5e 40 a9` | ldp x21,x23,[x19] | `FALL_THROUGH`
<a id="insn-00babac0"></a> `00babac0` | `78 0a 40 f9` | ldr x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babac4"></a> `00babac4` | `0d 00 00 14` | b 0x00babaf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00babac8"></a> `00babac8` | `78 06 40 f9` | ldr x24,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00babacc"></a> `00babacc` | `08 09 80 52` | mov w8,#0x48 | `FALL_THROUGH`
<a id="insn-00babad0"></a> `00babad0` | `a8 5e 08 9b` | madd x8,x21,x8,x23 | `FALL_THROUGH`
<a id="insn-00babad4"></a> `00babad4` | `04 00 00 14` | b 0x00babae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00babad8"></a> `00babad8` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00babadc"></a> `00babadc` | `08 fd 09 9b` | mneg x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00babae0"></a> `00babae0` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00babae4"></a> `00babae4` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00babae8"></a> `00babae8` | `a9 62 09 9b` | madd x9,x21,x9,x24 | `FALL_THROUGH`
<a id="insn-00babaec"></a> `00babaec` | `69 a2 00 a9` | stp x9,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00babaf0"></a> `00babaf0` | `09 00 00 14` | b 0x00babb14 | `UNCONDITIONAL_JUMP`
<a id="insn-00babaf4"></a> `00babaf4` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00babaf8"></a> `00babaf8` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00babafc"></a> `00babafc` | `60 26 00 a9` | stp x0,x9,[x19] | `FALL_THROUGH`
<a id="insn-00babb00"></a> `00babb00` | `6a 22 01 a9` | stp x10,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babb04"></a> `00babb04` | `a1 03 00 54` | b.ne 0x00babb78 | `CONDITIONAL_JUMP`
<a id="insn-00babb08"></a> `00babb08` | `75 00 00 b4` | cbz x21,0x00babb14 | `CONDITIONAL_JUMP`
<a id="insn-00babb0c"></a> `00babb0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00babb10"></a> `00babb10` | `10 b5 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00babb14"></a> `00babb14` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babb18"></a> `00babb18` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-00babb1c"></a> `00babb1c` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00babb20"></a> `00babb20` | `89 1a 40 f9` | ldr x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00babb24"></a> `00babb24` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babb28"></a> `00babb28` | `09 19 00 f9` | str x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babb2c"></a> `00babb2c` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babb30"></a> `00babb30` | `89 72 40 79` | ldrh w9,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00babb34"></a> `00babb34` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00babb38"></a> `00babb38` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babb3c"></a> `00babb3c` | `09 71 00 79` | strh w9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00babb40"></a> `00babb40` | `89 22 40 f9` | ldr x9,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00babb44"></a> `00babb44` | `09 21 00 f9` | str x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00babb48"></a> `00babb48` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babb4c"></a> `00babb4c` | `08 21 01 91` | add x8,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00babb50"></a> `00babb50` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babb54"></a> `00babb54` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babb58"></a> `00babb58` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babb5c"></a> `00babb5c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb60"></a> `00babb60` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb64"></a> `00babb64` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00babb68"></a> `00babb68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babb6c"></a> `00babb6c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00babb70"></a> `00babb70` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-00babb74"></a> `00babb74` | `a0 fc ff 54` | b.eq 0x00babb08 | `CONDITIONAL_JUMP`
<a id="insn-00babb78"></a> `00babb78` | `08 83 5d 38` | ldurb w8,[x24, #-0x28] | `FALL_THROUGH`
<a id="insn-00babb7c"></a> `00babb7c` | `16 23 01 d1` | sub x22,x24,#0x48 | `FALL_THROUGH`
<a id="insn-00babb80"></a> `00babb80` | `68 ff 07 36` | tbz w8,#0x0,0x00babb6c | `CONDITIONAL_JUMP`
<a id="insn-00babb84"></a> `00babb84` | `00 83 5e f8` | ldur x0,[x24, #-0x18] | `FALL_THROUGH`
<a id="insn-00babb88"></a> `00babb88` | `f2 b4 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00babb8c"></a> `00babb8c` | `f8 ff ff 17` | b 0x00babb6c | `UNCONDITIONAL_JUMP`
<a id="insn-00babb90"></a> `00babb90` | `94 c1 02 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bab8dc`](#insn-00bab8dc) 範囲 `[['00bab8dc', '00bab8eb']]`
  - `FALL_THROUGH` [`00bab8e8`](#insn-00bab8e8) → [`00bab8ec`](#insn-00bab8ec)
- ブロック [`00bab8ec`](#insn-00bab8ec) 範囲 `[['00bab8ec', '00bab8f7']]`
  - `FALL_THROUGH` [`00bab8f4`](#insn-00bab8f4) → [`00bab8f8`](#insn-00bab8f8)
- ブロック [`00bab8f8`](#insn-00bab8f8) 範囲 `[['00bab8f8', '00bab907']]`
  - `CONDITIONAL_JUMP` [`00bab904`](#insn-00bab904) → [`00babb14`](#insn-00babb14)
  - `FALL_THROUGH` [`00bab904`](#insn-00bab904) → [`00bab908`](#insn-00bab908)
- ブロック [`00bab908`](#insn-00bab908) 範囲 `[['00bab908', '00bab913']]`
  - `CONDITIONAL_JUMP` [`00bab910`](#insn-00bab910) → [`00bab9e0`](#insn-00bab9e0)
  - `FALL_THROUGH` [`00bab910`](#insn-00bab910) → [`00bab914`](#insn-00bab914)
- ブロック [`00bab914`](#insn-00bab914) 範囲 `[['00bab914', '00bab917']]`
  - `FALL_THROUGH` [`00bab914`](#insn-00bab914) → [`00bab918`](#insn-00bab918)
- ブロック [`00bab918`](#insn-00bab918) 範囲 `[['00bab918', '00bab94b']]`
  - `CONDITIONAL_JUMP` [`00bab948`](#insn-00bab948) → [`00babad8`](#insn-00babad8)
  - `FALL_THROUGH` [`00bab948`](#insn-00bab948) → [`00bab94c`](#insn-00bab94c)
- ブロック [`00bab94c`](#insn-00bab94c) 範囲 `[['00bab94c', '00bab957']]`
  - `UNCONDITIONAL_JUMP` [`00bab954`](#insn-00bab954) → [`00bab998`](#insn-00bab998)
- ブロック [`00bab958`](#insn-00bab958) 範囲 `[['00bab958', '00bab95f']]`
  - `FALL_THROUGH` [`00bab95c`](#insn-00bab95c) → [`00bab960`](#insn-00bab960)
- ブロック [`00bab960`](#insn-00bab960) 範囲 `[['00bab960', '00bab96f']]`
  - `FALL_THROUGH` [`00bab96c`](#insn-00bab96c) → [`00bab970`](#insn-00bab970)
- ブロック [`00bab970`](#insn-00bab970) 範囲 `[['00bab970', '00bab993']]`
  - `FALL_THROUGH` [`00bab990`](#insn-00bab990) → [`00bab994`](#insn-00bab994)
- ブロック [`00bab994`](#insn-00bab994) 範囲 `[['00bab994', '00bab997']]`
  - `CONDITIONAL_JUMP` [`00bab994`](#insn-00bab994) → [`00babac8`](#insn-00babac8)
  - `FALL_THROUGH` [`00bab994`](#insn-00bab994) → [`00bab998`](#insn-00bab998)
- ブロック [`00bab998`](#insn-00bab998) 範囲 `[['00bab998', '00bab9a7']]`
  - `FALL_THROUGH` [`00bab9a4`](#insn-00bab9a4) → [`00bab9a8`](#insn-00bab9a8)
- ブロック [`00bab9a8`](#insn-00bab9a8) 範囲 `[['00bab9a8', '00bab9b7']]`
  - `CONDITIONAL_JUMP` [`00bab9b4`](#insn-00bab9b4) → [`00bab958`](#insn-00bab958)
  - `FALL_THROUGH` [`00bab9b4`](#insn-00bab9b4) → [`00bab9b8`](#insn-00bab9b8)
- ブロック [`00bab9b8`](#insn-00bab9b8) 範囲 `[['00bab9b8', '00bab9c7']]`
  - `FALL_THROUGH` [`00bab9c4`](#insn-00bab9c4) → [`00bab9c8`](#insn-00bab9c8)
- ブロック [`00bab9c8`](#insn-00bab9c8) 範囲 `[['00bab9c8', '00bab9cb']]`
  - `CONDITIONAL_JUMP` [`00bab9c8`](#insn-00bab9c8) → [`00bab960`](#insn-00bab960)
  - `FALL_THROUGH` [`00bab9c8`](#insn-00bab9c8) → [`00bab9cc`](#insn-00bab9cc)
- ブロック [`00bab9cc`](#insn-00bab9cc) 範囲 `[['00bab9cc', '00bab9df']]`
  - `UNCONDITIONAL_JUMP` [`00bab9dc`](#insn-00bab9dc) → [`00bab960`](#insn-00bab960)
- ブロック [`00bab9e0`](#insn-00bab9e0) 範囲 `[['00bab9e0', '00bab9e7']]`
  - `FALL_THROUGH` [`00bab9e4`](#insn-00bab9e4) → [`00bab9e8`](#insn-00bab9e8)
- ブロック [`00bab9e8`](#insn-00bab9e8) 範囲 `[['00bab9e8', '00baba13']]`
  - `FALL_THROUGH` [`00baba10`](#insn-00baba10) → [`00baba14`](#insn-00baba14)
- ブロック [`00baba14`](#insn-00baba14) 範囲 `[['00baba14', '00baba17']]`
  - `CONDITIONAL_JUMP` [`00baba14`](#insn-00baba14) → [`00babb90`](#insn-00babb90)
  - `FALL_THROUGH` [`00baba14`](#insn-00baba14) → [`00baba18`](#insn-00baba18)
- ブロック [`00baba18`](#insn-00baba18) 範囲 `[['00baba18', '00baba37']]`
  - `FALL_THROUGH` [`00baba34`](#insn-00baba34) → [`00baba38`](#insn-00baba38)
- ブロック [`00baba38`](#insn-00baba38) 範囲 `[['00baba38', '00baba3f']]`
  - `CONDITIONAL_JUMP` [`00baba3c`](#insn-00baba3c) → [`00babaf4`](#insn-00babaf4)
  - `FALL_THROUGH` [`00baba3c`](#insn-00baba3c) → [`00baba40`](#insn-00baba40)
- ブロック [`00baba40`](#insn-00baba40) 範囲 `[['00baba40', '00baba63']]`
  - `FALL_THROUGH` [`00baba60`](#insn-00baba60) → [`00baba64`](#insn-00baba64)
- ブロック [`00baba64`](#insn-00baba64) 範囲 `[['00baba64', '00baba73']]`
  - `FALL_THROUGH` [`00baba70`](#insn-00baba70) → [`00baba74`](#insn-00baba74)
- ブロック [`00baba74`](#insn-00baba74) 範囲 `[['00baba74', '00baba87']]`
  - `FALL_THROUGH` [`00baba84`](#insn-00baba84) → [`00baba88`](#insn-00baba88)
- ブロック [`00baba88`](#insn-00baba88) 範囲 `[['00baba88', '00baba93']]`
  - `FALL_THROUGH` [`00baba90`](#insn-00baba90) → [`00baba94`](#insn-00baba94)
- ブロック [`00baba94`](#insn-00baba94) 範囲 `[['00baba94', '00babab3']]`
  - `FALL_THROUGH` [`00babab0`](#insn-00babab0) → [`00babab4`](#insn-00babab4)
- ブロック [`00babab4`](#insn-00babab4) 範囲 `[['00babab4', '00bababb']]`
  - `CONDITIONAL_JUMP` [`00babab8`](#insn-00babab8) → [`00baba74`](#insn-00baba74)
  - `FALL_THROUGH` [`00babab8`](#insn-00babab8) → [`00bababc`](#insn-00bababc)
- ブロック [`00bababc`](#insn-00bababc) 範囲 `[['00bababc', '00babac7']]`
  - `UNCONDITIONAL_JUMP` [`00babac4`](#insn-00babac4) → [`00babaf8`](#insn-00babaf8)
- ブロック [`00babac8`](#insn-00babac8) 範囲 `[['00babac8', '00babad7']]`
  - `UNCONDITIONAL_JUMP` [`00babad4`](#insn-00babad4) → [`00babae4`](#insn-00babae4)
- ブロック [`00babad8`](#insn-00babad8) 範囲 `[['00babad8', '00babae3']]`
  - `FALL_THROUGH` [`00babae0`](#insn-00babae0) → [`00babae4`](#insn-00babae4)
- ブロック [`00babae4`](#insn-00babae4) 範囲 `[['00babae4', '00babaf3']]`
  - `UNCONDITIONAL_JUMP` [`00babaf0`](#insn-00babaf0) → [`00babb14`](#insn-00babb14)
- ブロック [`00babaf4`](#insn-00babaf4) 範囲 `[['00babaf4', '00babaf7']]`
  - `FALL_THROUGH` [`00babaf4`](#insn-00babaf4) → [`00babaf8`](#insn-00babaf8)
- ブロック [`00babaf8`](#insn-00babaf8) 範囲 `[['00babaf8', '00babb07']]`
  - `CONDITIONAL_JUMP` [`00babb04`](#insn-00babb04) → [`00babb78`](#insn-00babb78)
  - `FALL_THROUGH` [`00babb04`](#insn-00babb04) → [`00babb08`](#insn-00babb08)
- ブロック [`00babb08`](#insn-00babb08) 範囲 `[['00babb08', '00babb0b']]`
  - `CONDITIONAL_JUMP` [`00babb08`](#insn-00babb08) → [`00babb14`](#insn-00babb14)
  - `FALL_THROUGH` [`00babb08`](#insn-00babb08) → [`00babb0c`](#insn-00babb0c)
- ブロック [`00babb0c`](#insn-00babb0c) 範囲 `[['00babb0c', '00babb13']]`
  - `FALL_THROUGH` [`00babb10`](#insn-00babb10) → [`00babb14`](#insn-00babb14)
- ブロック [`00babb14`](#insn-00babb14) 範囲 `[['00babb14', '00babb27']]`
  - `FALL_THROUGH` [`00babb24`](#insn-00babb24) → [`00babb28`](#insn-00babb28)
- ブロック [`00babb28`](#insn-00babb28) 範囲 `[['00babb28', '00babb67']]`
  - `FALL_THROUGH` [`00babb64`](#insn-00babb64) → [`00babb68`](#insn-00babb68)
- ブロック [`00babb68`](#insn-00babb68) 範囲 `[['00babb68', '00babb6b']]`
- ブロック [`00babb6c`](#insn-00babb6c) 範囲 `[['00babb6c', '00babb77']]`
  - `CONDITIONAL_JUMP` [`00babb74`](#insn-00babb74) → [`00babb08`](#insn-00babb08)
  - `FALL_THROUGH` [`00babb74`](#insn-00babb74) → [`00babb78`](#insn-00babb78)
- ブロック [`00babb78`](#insn-00babb78) 範囲 `[['00babb78', '00babb83']]`
  - `CONDITIONAL_JUMP` [`00babb80`](#insn-00babb80) → [`00babb6c`](#insn-00babb6c)
  - `FALL_THROUGH` [`00babb80`](#insn-00babb80) → [`00babb84`](#insn-00babb84)
- ブロック [`00babb84`](#insn-00babb84) 範囲 `[['00babb84', '00babb8f']]`
  - `UNCONDITIONAL_JUMP` [`00babb8c`](#insn-00babb8c) → [`00babb6c`](#insn-00babb6c)
- ブロック [`00babb90`](#insn-00babb90) 範囲 `[['00babb90', '00babb93']]`

## 命令位置別の参照

- [`00bab8dc`](#insn-00bab8dc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8e0`](#insn-00bab8e0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8e4`](#insn-00bab8e4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8e8`](#insn-00bab8e8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8ec`](#insn-00bab8ec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab904`](#insn-00bab904) → [`00babb14`](#insn-00babb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab910`](#insn-00bab910) → [`00bab9e0`](#insn-00bab9e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab948`](#insn-00bab948) → [`00babad8`](#insn-00babad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab954`](#insn-00bab954) → [`00bab998`](#insn-00bab998) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab994`](#insn-00bab994) → [`00babac8`](#insn-00babac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9b4`](#insn-00bab9b4) → [`00bab958`](#insn-00bab958) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9c8`](#insn-00bab9c8) → [`00bab960`](#insn-00bab960) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9d0`](#insn-00bab9d0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bab9dc`](#insn-00bab9dc) → [`00bab960`](#insn-00bab960) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba14`](#insn-00baba14) → [`00babb90`](#insn-00babb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba28`](#insn-00baba28) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00baba3c`](#insn-00baba3c) → [`00babaf4`](#insn-00babaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babab8`](#insn-00babab8) → [`00baba74`](#insn-00baba74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babac4`](#insn-00babac4) → [`00babaf8`](#insn-00babaf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babad4`](#insn-00babad4) → [`00babae4`](#insn-00babae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babaf0`](#insn-00babaf0) → [`00babb14`](#insn-00babb14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb04`](#insn-00babb04) → [`00babb78`](#insn-00babb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb08`](#insn-00babb08) → [`00babb14`](#insn-00babb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb10`](#insn-00babb10) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00babb54`](#insn-00babb54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb58`](#insn-00babb58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb5c`](#insn-00babb5c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb60`](#insn-00babb60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb74`](#insn-00babb74) → [`00babb08`](#insn-00babb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb80`](#insn-00babb80) → [`00babb6c`](#insn-00babb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb88`](#insn-00babb88) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00babb8c`](#insn-00babb8c) → [`00babb6c`](#insn-00babb6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb90`](#insn-00babb90) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab8dc`](#insn-00bab8dc)

~~~json
{
  "source": "00bab8dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8e0`](#insn-00bab8e0)

~~~json
{
  "source": "00bab8e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8e4`](#insn-00bab8e4)

~~~json
{
  "source": "00bab8e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8e8`](#insn-00bab8e8)

~~~json
{
  "source": "00bab8e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8ec`](#insn-00bab8ec)

~~~json
{
  "source": "00bab8ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab904`](#insn-00bab904)

~~~json
{
  "source": "00bab904",
  "target": "00babb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab910`](#insn-00bab910)

~~~json
{
  "source": "00bab910",
  "target": "00bab9e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab948`](#insn-00bab948)

~~~json
{
  "source": "00bab948",
  "target": "00babad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab954`](#insn-00bab954)

~~~json
{
  "source": "00bab954",
  "target": "00bab998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab994`](#insn-00bab994)

~~~json
{
  "source": "00bab994",
  "target": "00babac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9b4`](#insn-00bab9b4)

~~~json
{
  "source": "00bab9b4",
  "target": "00bab958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9c8`](#insn-00bab9c8)

~~~json
{
  "source": "00bab9c8",
  "target": "00bab960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9d0`](#insn-00bab9d0)

~~~json
{
  "source": "00bab9d0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab9dc`](#insn-00bab9dc)

~~~json
{
  "source": "00bab9dc",
  "target": "00bab960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba14`](#insn-00baba14)

~~~json
{
  "source": "00baba14",
  "target": "00babb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba28`](#insn-00baba28)

~~~json
{
  "source": "00baba28",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baba3c`](#insn-00baba3c)

~~~json
{
  "source": "00baba3c",
  "target": "00babaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babab8`](#insn-00babab8)

~~~json
{
  "source": "00babab8",
  "target": "00baba74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babac4`](#insn-00babac4)

~~~json
{
  "source": "00babac4",
  "target": "00babaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babad4`](#insn-00babad4)

~~~json
{
  "source": "00babad4",
  "target": "00babae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babaf0`](#insn-00babaf0)

~~~json
{
  "source": "00babaf0",
  "target": "00babb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb04`](#insn-00babb04)

~~~json
{
  "source": "00babb04",
  "target": "00babb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb08`](#insn-00babb08)

~~~json
{
  "source": "00babb08",
  "target": "00babb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb10`](#insn-00babb10)

~~~json
{
  "source": "00babb10",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb54`](#insn-00babb54)

~~~json
{
  "source": "00babb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb58`](#insn-00babb58)

~~~json
{
  "source": "00babb58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb5c`](#insn-00babb5c)

~~~json
{
  "source": "00babb5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb60`](#insn-00babb60)

~~~json
{
  "source": "00babb60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb74`](#insn-00babb74)

~~~json
{
  "source": "00babb74",
  "target": "00babb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb80`](#insn-00babb80)

~~~json
{
  "source": "00babb80",
  "target": "00babb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb88`](#insn-00babb88)

~~~json
{
  "source": "00babb88",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb8c`](#insn-00babb8c)

~~~json
{
  "source": "00babb8c",
  "target": "00babb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb90`](#insn-00babb90)

~~~json
{
  "source": "00babb90",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
