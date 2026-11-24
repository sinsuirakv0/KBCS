# 00babdec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baadf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-582a8694debe8fdc6812fe4404489e8e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babdec",
  "name": "_ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f7f1396d9a6d420a7fe65f2cf1bf7723b8f50892ac394755180079b9cb721b6",
  "source_text_sha256": "0f7f1396d9a6d420a7fe65f2cf1bf7723b8f50892ac394755180079b9cb721b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babdec",
        "00babf9b"
      ]
    ],
    "bytes_sha256": "30f6249b2d40d271e7604a3389875f5c5010e43e63b08ccf1dbe4142afb6ccce",
    "instruction_count": 108,
    "instruction_bytes": 432,
    "body_bytes": 432,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e0e0](../00c5e/00c5e0e0.md)

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4355 bytes

~~~c

void _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  void *pvVar3;
  long lVar4;
  undefined8 *puVar5;
  long lVar6;
  ulong uVar7;
  void *pvVar8;
  long lVar9;
  void *__ptr;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  
                    /* try { // try from 00babe04 to 00cabe0f has its CatchHandler @ 00bacc14 */
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar10 = 0x38e38e38e38e38e;
  uVar1 = lVar4 * -0x71c71c71c71c71c7 + 1;
                    /* try { // try from 00babe30 to 00cabe3b has its CatchHandler @ 00bacbc8 */
  if (0x38e38e38e38e38e < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar6 = param_1[2] - *param_1 >> 3;
                    /* try { // try from 00babe54 to 00cabe5f has its CatchHandler @ 00bacbc4 */
  if ((ulong)(lVar6 * -0x71c71c71c71c71c7) < 0x1c71c71c71c71c7) {
    uVar7 = lVar6 * 0x1c71c71c71c71c72;
    uVar10 = uVar1;
    if (uVar1 <= uVar7) {
      uVar10 = uVar7;
    }
    if (uVar10 == 0) {
                    /* try { // try from 00babf90 to 00cabf93 has its CatchHandler @ 00bacd90 */
      lVar6 = 0;
      goto LAB_00babe84;
    }
  }
                    /* try { // try from 00babe80 to 00cabe8b has its CatchHandler @ 00bacb78 */
  lVar6 = _Znwm(uVar10 * 0x48);
LAB_00babe84:
  uVar11 = *param_2;
  uVar13 = param_2[3];
  uVar12 = param_2[2];
  puVar5 = (undefined8 *)(lVar6 + lVar4 * 8);
  puVar5[1] = param_2[1];
  *puVar5 = uVar11;
  puVar5[3] = uVar13;
  puVar5[2] = uVar12;
                    /* try { // try from 00babe9c to 00cabea7 has its CatchHandler @ 00bacb74 */
  uVar12 = param_2[5];
  uVar11 = param_2[4];
  puVar5[6] = param_2[6];
  puVar5[5] = uVar12;
  puVar5[4] = uVar11;
                    /* try { // try from 00babea8 to 00cabec7 has its CatchHandler @ 00bacec4 */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar5 + 7) = *(undefined2 *)(param_2 + 7);
  puVar5[8] = param_2[8];
  pvVar8 = (void *)*param_1;
  pvVar3 = (void *)param_1[1];
  puVar2 = puVar5 + 9;
                    /* try { // try from 00babec8 to 00cabf37 has its CatchHandler @ 00bad098 */
  __ptr = pvVar8;
  if (pvVar3 != pvVar8) {
    lVar4 = 0;
    do {
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x38);
      uVar13 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x40);
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x48);
      lVar9 = lVar4 + -0x48;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x30) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x30);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x38) = uVar11;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x40) = uVar13;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x48) = uVar12;
      uVar12 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x20);
      uVar11 = *(undefined8 *)((long)pvVar3 + lVar4 + -0x28);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x18) = *(undefined8 *)((long)pvVar3 + lVar4 + -0x18);
      *(undefined8 *)((long)puVar5 + lVar4 + -0x20) = uVar12;
      *(undefined8 *)((long)puVar5 + lVar4 + -0x28) = uVar11;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x20) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x18) = 0;
      *(undefined8 *)((long)pvVar3 + lVar4 + -0x28) = 0;
      *(undefined2 *)((long)puVar5 + lVar4 + -0x10) = *(undefined2 *)((long)pvVar3 + lVar4 + -0x10);
      *(undefined8 *)((long)puVar5 + lVar4 + -8) = *(undefined8 *)((long)pvVar3 + lVar4 + -8);
      lVar4 = lVar9;
    } while ((long)pvVar8 - (long)pvVar3 != lVar9);
    pvVar8 = (void *)param_1[1];
    puVar5 = (undefined8 *)((long)puVar5 + lVar9);
    __ptr = (void *)*param_1;
  }
  *param_1 = (long)puVar5;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar6 + uVar10 * 0x48;
  while (pvVar3 = pvVar8, pvVar3 != __ptr) {
    pvVar8 = (void *)((long)pvVar3 + -0x48);
    if ((*(byte *)((long)pvVar3 + -0x28) & 1) != 0) {
      _ZdlPv(*(void **)((long)pvVar3 + -0x18));
                    /* try { // try from 00babf7c to 00cabf87 has its CatchHandler @ 00bacdb0 */
    }
  }
  if (__ptr != (void *)0x0) {
                    /* try { // try from 00babf58 to 00cabf63 has its CatchHandler @ 00bace20 */
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babdec"></a> `00babdec` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00babdf0"></a> `00babdf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babdf4"></a> `00babdf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babdf8"></a> `00babdf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00babdfc"></a> `00babdfc` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00babe00"></a> `00babe00` | `2a c7 91 d2` | mov x10,#0x8e39 | `FALL_THROUGH`
<a id="insn-00babe04"></a> `00babe04` | `6a 1c a7 f2` | movk x10,#0x38e3, LSL #16 | `FALL_THROUGH`
<a id="insn-00babe08"></a> `00babe08` | `d5 71 9c d2` | mov x21,#0xe38e | `FALL_THROUGH`
<a id="insn-00babe0c"></a> `00babe0c` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00babe10"></a> `00babe10` | `ca 71 dc f2` | movk x10,#0xe38e, LSL #32 | `FALL_THROUGH`
<a id="insn-00babe14"></a> `00babe14` | `15 c7 b1 f2` | movk x21,#0x8e38, LSL #16 | `FALL_THROUGH`
<a id="insn-00babe18"></a> `00babe18` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00babe1c"></a> `00babe1c` | `0a c7 f1 f2` | movk x10,#0x8e38, LSL #48 | `FALL_THROUGH`
<a id="insn-00babe20"></a> `00babe20` | `75 1c c7 f2` | movk x21,#0x38e3, LSL #32 | `FALL_THROUGH`
<a id="insn-00babe24"></a> `00babe24` | `16 7d 0a 9b` | mul x22,x8,x10 | `FALL_THROUGH`
<a id="insn-00babe28"></a> `00babe28` | `d5 71 e0 f2` | movk x21,#0x38e, LSL #48 | `FALL_THROUGH`
<a id="insn-00babe2c"></a> `00babe2c` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00babe30"></a> `00babe30` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00babe34"></a> `00babe34` | `28 0b 00 54` | b.hi 0x00babf98 | `CONDITIONAL_JUMP`
<a id="insn-00babe38"></a> `00babe38` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00babe3c"></a> `00babe3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babe40"></a> `00babe40` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00babe44"></a> `00babe44` | `69 01 09 cb` | sub x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00babe48"></a> `00babe48` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00babe4c"></a> `00babe4c` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00babe50"></a> `00babe50` | `ca 38 8e d2` | mov x10,#0x71c6 | `FALL_THROUGH`
<a id="insn-00babe54"></a> `00babe54` | `8a e3 b8 f2` | movk x10,#0xc71c, LSL #16 | `FALL_THROUGH`
<a id="insn-00babe58"></a> `00babe58` | `2a 8e c3 f2` | movk x10,#0x1c71, LSL #32 | `FALL_THROUGH`
<a id="insn-00babe5c"></a> `00babe5c` | `ea 38 e0 f2` | movk x10,#0x1c7, LSL #48 | `FALL_THROUGH`
<a id="insn-00babe60"></a> `00babe60` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00babe64"></a> `00babe64` | `a8 00 00 54` | b.hi 0x00babe78 | `CONDITIONAL_JUMP`
<a id="insn-00babe68"></a> `00babe68` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00babe6c"></a> `00babe6c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00babe70"></a> `00babe70` | `15 31 89 9a` | csel x21,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00babe74"></a> `00babe74` | `f5 08 00 b4` | cbz x21,0x00babf90 | `CONDITIONAL_JUMP`
<a id="insn-00babe78"></a> `00babe78` | `a8 0e 15 8b` | add x8,x21,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00babe7c"></a> `00babe7c` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00babe80"></a> `00babe80` | `2c b4 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00babe84"></a> `00babe84` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-00babe88"></a> `00babe88` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00babe8c"></a> `00babe8c` | `c8 02 09 9b` | madd x8,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00babe90"></a> `00babe90` | `a9 02 09 9b` | madd x9,x21,x9,x0 | `FALL_THROUGH`
<a id="insn-00babe94"></a> `00babe94` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00babe98"></a> `00babe98` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00babe9c"></a> `00babe9c` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babea0"></a> `00babea0` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babea4"></a> `00babea4` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babea8"></a> `00babea8` | `8a 72 40 79` | ldrh w10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00babeac"></a> `00babeac` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00babeb0"></a> `00babeb0` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00babeb4"></a> `00babeb4` | `0a 71 00 79` | strh w10,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00babeb8"></a> `00babeb8` | `8a 22 40 f9` | ldr x10,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00babebc"></a> `00babebc` | `0a 21 00 f9` | str x10,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00babec0"></a> `00babec0` | `6b 36 40 a9` | ldp x11,x13,[x19] | `FALL_THROUGH`
<a id="insn-00babec4"></a> `00babec4` | `0a 21 01 91` | add x10,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00babec8"></a> `00babec8` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00babecc"></a> `00babecc` | `20 03 00 54` | b.eq 0x00babf30 | `CONDITIONAL_JUMP`
<a id="insn-00babed0"></a> `00babed0` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00babed4"></a> `00babed4` | `6b 01 0d cb` | sub x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00babed8"></a> `00babed8` | `ae 01 0c 8b` | add x14,x13,x12 | `FALL_THROUGH`
<a id="insn-00babedc"></a> `00babedc` | `c0 81 dc 3c` | ldur q0,[x14, #-0x38] | `FALL_THROUGH`
<a id="insn-00babee0"></a> `00babee0` | `c1 81 db 3c` | ldur q1,[x14, #-0x48] | `FALL_THROUGH`
<a id="insn-00babee4"></a> `00babee4` | `0f 01 0c 8b` | add x15,x8,x12 | `FALL_THROUGH`
<a id="insn-00babee8"></a> `00babee8` | `8c 21 01 d1` | sub x12,x12,#0x48 | `FALL_THROUGH`
<a id="insn-00babeec"></a> `00babeec` | `e0 81 9c 3c` | stur q0,[x15, #-0x38] | `FALL_THROUGH`
<a id="insn-00babef0"></a> `00babef0` | `e1 81 9b 3c` | stur q1,[x15, #-0x48] | `FALL_THROUGH`
<a id="insn-00babef4"></a> `00babef4` | `d0 81 5e f8` | ldur x16,[x14, #-0x18] | `FALL_THROUGH`
<a id="insn-00babef8"></a> `00babef8` | `c0 81 dd 3c` | ldur q0,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00babefc"></a> `00babefc` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00babf00"></a> `00babf00` | `f0 81 1e f8` | stur x16,[x15, #-0x18] | `FALL_THROUGH`
<a id="insn-00babf04"></a> `00babf04` | `e0 81 9d 3c` | stur q0,[x15, #-0x28] | `FALL_THROUGH`
<a id="insn-00babf08"></a> `00babf08` | `d0 01 5f 78` | ldurh w16,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00babf0c"></a> `00babf0c` | `df 7d 3e a9` | stp xzr,xzr,[x14, #-0x20] | `FALL_THROUGH`
<a id="insn-00babf10"></a> `00babf10` | `df 81 1d f8` | stur xzr,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00babf14"></a> `00babf14` | `f0 01 1f 78` | sturh w16,[x15, #-0x10] | `FALL_THROUGH`
<a id="insn-00babf18"></a> `00babf18` | `ce 81 5f f8` | ldur x14,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00babf1c"></a> `00babf1c` | `ee 81 1f f8` | stur x14,[x15, #-0x8] | `FALL_THROUGH`
<a id="insn-00babf20"></a> `00babf20` | `c1 fd ff 54` | b.ne 0x00babed8 | `CONDITIONAL_JUMP`
<a id="insn-00babf24"></a> `00babf24` | `74 2e 40 a9` | ldp x20,x11,[x19] | `FALL_THROUGH`
<a id="insn-00babf28"></a> `00babf28` | `08 01 0c 8b` | add x8,x8,x12 | `FALL_THROUGH`
<a id="insn-00babf2c"></a> `00babf2c` | `02 00 00 14` | b 0x00babf34 | `UNCONDITIONAL_JUMP`
<a id="insn-00babf30"></a> `00babf30` | `f4 03 0b aa` | mov x20,x11 | `FALL_THROUGH`
<a id="insn-00babf34"></a> `00babf34` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00babf38"></a> `00babf38` | `68 2a 00 a9` | stp x8,x10,[x19] | `FALL_THROUGH`
<a id="insn-00babf3c"></a> `00babf3c` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00babf40"></a> `00babf40` | `41 01 00 54` | b.ne 0x00babf68 | `CONDITIONAL_JUMP`
<a id="insn-00babf44"></a> `00babf44` | `f4 01 00 b4` | cbz x20,0x00babf80 | `CONDITIONAL_JUMP`
<a id="insn-00babf48"></a> `00babf48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00babf4c"></a> `00babf4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babf50"></a> `00babf50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babf54"></a> `00babf54` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00babf58"></a> `00babf58` | `fe b3 02 14` | b 0x00c58f50 | `CALL_TERMINATOR`
<a id="insn-00babf5c"></a> `00babf5c` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00babf60"></a> `00babf60` | `eb 03 13 aa` | mov x11,x19 | `FALL_THROUGH`
<a id="insn-00babf64"></a> `00babf64` | `00 ff ff 54` | b.eq 0x00babf44 | `CONDITIONAL_JUMP`
<a id="insn-00babf68"></a> `00babf68` | `68 81 5d 38` | ldurb w8,[x11, #-0x28] | `FALL_THROUGH`
<a id="insn-00babf6c"></a> `00babf6c` | `73 21 01 d1` | sub x19,x11,#0x48 | `FALL_THROUGH`
<a id="insn-00babf70"></a> `00babf70` | `68 ff 07 36` | tbz w8,#0x0,0x00babf5c | `CONDITIONAL_JUMP`
<a id="insn-00babf74"></a> `00babf74` | `60 81 5e f8` | ldur x0,[x11, #-0x18] | `FALL_THROUGH`
<a id="insn-00babf78"></a> `00babf78` | `f6 b3 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00babf7c"></a> `00babf7c` | `f8 ff ff 17` | b 0x00babf5c | `UNCONDITIONAL_JUMP`
<a id="insn-00babf80"></a> `00babf80` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babf84"></a> `00babf84` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babf88"></a> `00babf88` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00babf8c"></a> `00babf8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babf90"></a> `00babf90` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00babf94"></a> `00babf94` | `bc ff ff 17` | b 0x00babe84 | `UNCONDITIONAL_JUMP`
<a id="insn-00babf98"></a> `00babf98` | `92 c0 02 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babdec`](#insn-00babdec) 範囲 `[['00babdec', '00babe03']]`
  - `FALL_THROUGH` [`00babe00`](#insn-00babe00) → [`00babe04`](#insn-00babe04)
- ブロック [`00babe04`](#insn-00babe04) 範囲 `[['00babe04', '00babe2f']]`
  - `FALL_THROUGH` [`00babe2c`](#insn-00babe2c) → [`00babe30`](#insn-00babe30)
- ブロック [`00babe30`](#insn-00babe30) 範囲 `[['00babe30', '00babe37']]`
  - `CONDITIONAL_JUMP` [`00babe34`](#insn-00babe34) → [`00babf98`](#insn-00babf98)
  - `FALL_THROUGH` [`00babe34`](#insn-00babe34) → [`00babe38`](#insn-00babe38)
- ブロック [`00babe38`](#insn-00babe38) 範囲 `[['00babe38', '00babe53']]`
  - `FALL_THROUGH` [`00babe50`](#insn-00babe50) → [`00babe54`](#insn-00babe54)
- ブロック [`00babe54`](#insn-00babe54) 範囲 `[['00babe54', '00babe67']]`
  - `CONDITIONAL_JUMP` [`00babe64`](#insn-00babe64) → [`00babe78`](#insn-00babe78)
  - `FALL_THROUGH` [`00babe64`](#insn-00babe64) → [`00babe68`](#insn-00babe68)
- ブロック [`00babe68`](#insn-00babe68) 範囲 `[['00babe68', '00babe77']]`
  - `CONDITIONAL_JUMP` [`00babe74`](#insn-00babe74) → [`00babf90`](#insn-00babf90)
  - `FALL_THROUGH` [`00babe74`](#insn-00babe74) → [`00babe78`](#insn-00babe78)
- ブロック [`00babe78`](#insn-00babe78) 範囲 `[['00babe78', '00babe7f']]`
  - `FALL_THROUGH` [`00babe7c`](#insn-00babe7c) → [`00babe80`](#insn-00babe80)
- ブロック [`00babe80`](#insn-00babe80) 範囲 `[['00babe80', '00babe83']]`
  - `FALL_THROUGH` [`00babe80`](#insn-00babe80) → [`00babe84`](#insn-00babe84)
- ブロック [`00babe84`](#insn-00babe84) 範囲 `[['00babe84', '00babe9b']]`
  - `FALL_THROUGH` [`00babe98`](#insn-00babe98) → [`00babe9c`](#insn-00babe9c)
- ブロック [`00babe9c`](#insn-00babe9c) 範囲 `[['00babe9c', '00babea7']]`
  - `FALL_THROUGH` [`00babea4`](#insn-00babea4) → [`00babea8`](#insn-00babea8)
- ブロック [`00babea8`](#insn-00babea8) 範囲 `[['00babea8', '00babec7']]`
  - `FALL_THROUGH` [`00babec4`](#insn-00babec4) → [`00babec8`](#insn-00babec8)
- ブロック [`00babec8`](#insn-00babec8) 範囲 `[['00babec8', '00babecf']]`
  - `CONDITIONAL_JUMP` [`00babecc`](#insn-00babecc) → [`00babf30`](#insn-00babf30)
  - `FALL_THROUGH` [`00babecc`](#insn-00babecc) → [`00babed0`](#insn-00babed0)
- ブロック [`00babed0`](#insn-00babed0) 範囲 `[['00babed0', '00babed7']]`
  - `FALL_THROUGH` [`00babed4`](#insn-00babed4) → [`00babed8`](#insn-00babed8)
- ブロック [`00babed8`](#insn-00babed8) 範囲 `[['00babed8', '00babf23']]`
  - `CONDITIONAL_JUMP` [`00babf20`](#insn-00babf20) → [`00babed8`](#insn-00babed8)
  - `FALL_THROUGH` [`00babf20`](#insn-00babf20) → [`00babf24`](#insn-00babf24)
- ブロック [`00babf24`](#insn-00babf24) 範囲 `[['00babf24', '00babf2f']]`
  - `UNCONDITIONAL_JUMP` [`00babf2c`](#insn-00babf2c) → [`00babf34`](#insn-00babf34)
- ブロック [`00babf30`](#insn-00babf30) 範囲 `[['00babf30', '00babf33']]`
  - `FALL_THROUGH` [`00babf30`](#insn-00babf30) → [`00babf34`](#insn-00babf34)
- ブロック [`00babf34`](#insn-00babf34) 範囲 `[['00babf34', '00babf43']]`
  - `CONDITIONAL_JUMP` [`00babf40`](#insn-00babf40) → [`00babf68`](#insn-00babf68)
  - `FALL_THROUGH` [`00babf40`](#insn-00babf40) → [`00babf44`](#insn-00babf44)
- ブロック [`00babf44`](#insn-00babf44) 範囲 `[['00babf44', '00babf47']]`
  - `CONDITIONAL_JUMP` [`00babf44`](#insn-00babf44) → [`00babf80`](#insn-00babf80)
  - `FALL_THROUGH` [`00babf44`](#insn-00babf44) → [`00babf48`](#insn-00babf48)
- ブロック [`00babf48`](#insn-00babf48) 範囲 `[['00babf48', '00babf57']]`
  - `FALL_THROUGH` [`00babf54`](#insn-00babf54) → [`00babf58`](#insn-00babf58)
- ブロック [`00babf58`](#insn-00babf58) 範囲 `[['00babf58', '00babf5b']]`
- ブロック [`00babf5c`](#insn-00babf5c) 範囲 `[['00babf5c', '00babf67']]`
  - `CONDITIONAL_JUMP` [`00babf64`](#insn-00babf64) → [`00babf44`](#insn-00babf44)
  - `FALL_THROUGH` [`00babf64`](#insn-00babf64) → [`00babf68`](#insn-00babf68)
- ブロック [`00babf68`](#insn-00babf68) 範囲 `[['00babf68', '00babf73']]`
  - `CONDITIONAL_JUMP` [`00babf70`](#insn-00babf70) → [`00babf5c`](#insn-00babf5c)
  - `FALL_THROUGH` [`00babf70`](#insn-00babf70) → [`00babf74`](#insn-00babf74)
- ブロック [`00babf74`](#insn-00babf74) 範囲 `[['00babf74', '00babf7b']]`
  - `FALL_THROUGH` [`00babf78`](#insn-00babf78) → [`00babf7c`](#insn-00babf7c)
- ブロック [`00babf7c`](#insn-00babf7c) 範囲 `[['00babf7c', '00babf7f']]`
  - `UNCONDITIONAL_JUMP` [`00babf7c`](#insn-00babf7c) → [`00babf5c`](#insn-00babf5c)
- ブロック [`00babf80`](#insn-00babf80) 範囲 `[['00babf80', '00babf8f']]`
- ブロック [`00babf90`](#insn-00babf90) 範囲 `[['00babf90', '00babf97']]`
  - `UNCONDITIONAL_JUMP` [`00babf94`](#insn-00babf94) → [`00babe84`](#insn-00babe84)
- ブロック [`00babf98`](#insn-00babf98) 範囲 `[['00babf98', '00babf9b']]`

## 命令位置別の参照

- [`00babdec`](#insn-00babdec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babdf0`](#insn-00babdf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babdf4`](#insn-00babdf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe34`](#insn-00babe34) → [`00babf98`](#insn-00babf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe64`](#insn-00babe64) → [`00babe78`](#insn-00babe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe74`](#insn-00babe74) → [`00babf90`](#insn-00babf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe80`](#insn-00babe80) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00babecc`](#insn-00babecc) → [`00babf30`](#insn-00babf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf20`](#insn-00babf20) → [`00babed8`](#insn-00babed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf2c`](#insn-00babf2c) → [`00babf34`](#insn-00babf34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf40`](#insn-00babf40) → [`00babf68`](#insn-00babf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf44`](#insn-00babf44) → [`00babf80`](#insn-00babf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf4c`](#insn-00babf4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf50`](#insn-00babf50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf58`](#insn-00babf58) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00babf64`](#insn-00babf64) → [`00babf44`](#insn-00babf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf70`](#insn-00babf70) → [`00babf5c`](#insn-00babf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf78`](#insn-00babf78) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00babf7c`](#insn-00babf7c) → [`00babf5c`](#insn-00babf5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf80`](#insn-00babf80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf84`](#insn-00babf84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf94`](#insn-00babf94) → [`00babe84`](#insn-00babe84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babf98`](#insn-00babf98) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babdec`](#insn-00babdec)

~~~json
{
  "source": "00babdec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babdf0`](#insn-00babdf0)

~~~json
{
  "source": "00babdf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babdf4`](#insn-00babdf4)

~~~json
{
  "source": "00babdf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe34`](#insn-00babe34)

~~~json
{
  "source": "00babe34",
  "target": "00babf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe64`](#insn-00babe64)

~~~json
{
  "source": "00babe64",
  "target": "00babe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe74`](#insn-00babe74)

~~~json
{
  "source": "00babe74",
  "target": "00babf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe80`](#insn-00babe80)

~~~json
{
  "source": "00babe80",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babecc`](#insn-00babecc)

~~~json
{
  "source": "00babecc",
  "target": "00babf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf20`](#insn-00babf20)

~~~json
{
  "source": "00babf20",
  "target": "00babed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf2c`](#insn-00babf2c)

~~~json
{
  "source": "00babf2c",
  "target": "00babf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf40`](#insn-00babf40)

~~~json
{
  "source": "00babf40",
  "target": "00babf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf44`](#insn-00babf44)

~~~json
{
  "source": "00babf44",
  "target": "00babf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf4c`](#insn-00babf4c)

~~~json
{
  "source": "00babf4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf50`](#insn-00babf50)

~~~json
{
  "source": "00babf50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf58`](#insn-00babf58)

~~~json
{
  "source": "00babf58",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babf64`](#insn-00babf64)

~~~json
{
  "source": "00babf64",
  "target": "00babf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf70`](#insn-00babf70)

~~~json
{
  "source": "00babf70",
  "target": "00babf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf78`](#insn-00babf78)

~~~json
{
  "source": "00babf78",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babf7c`](#insn-00babf7c)

~~~json
{
  "source": "00babf7c",
  "target": "00babf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf80`](#insn-00babf80)

~~~json
{
  "source": "00babf80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf84`](#insn-00babf84)

~~~json
{
  "source": "00babf84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf94`](#insn-00babf94)

~~~json
{
  "source": "00babf94",
  "target": "00babe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babf98`](#insn-00babf98)

~~~json
{
  "source": "00babf98",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
