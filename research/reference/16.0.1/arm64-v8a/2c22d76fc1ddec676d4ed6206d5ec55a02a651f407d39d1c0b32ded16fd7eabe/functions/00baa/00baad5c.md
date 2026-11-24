# 00baad5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baa934`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa934.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-7eb2d1c9fa0e15a7614bb2b5759b07a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baadf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baadf8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-8f72f8107d8e4974cdc153759dc03c94)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baad5c",
  "name": "_ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce418a59954d3681a686bdbec2d14d668232bb1afe8e114a60c105c889e0992c",
  "source_text_sha256": "ce418a59954d3681a686bdbec2d14d668232bb1afe8e114a60c105c889e0992c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baad5c",
        "00baaf0b"
      ]
    ],
    "bytes_sha256": "7ac553427fe3353506f6dc3dc7c5ed560137ed0399c1af759040ea4193a0ed82",
    "instruction_count": 108,
    "instruction_bytes": 432,
    "body_bytes": 432,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d040](../00c5d/00c5d040.md)

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5b140](../00c5b/00c5b140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4258 bytes

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
  
                    /* try { // try from 00baad7c to 00caad87 has its CatchHandler @ 00babbb4 */
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar10 = 0x38e38e38e38e38e;
  uVar1 = lVar4 * -0x71c71c71c71c71c7 + 1;
                    /* try { // try from 00baada0 to 00caadab has its CatchHandler @ 00babbb0 */
  if (0x38e38e38e38e38e < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar6 = param_1[2] - *param_1 >> 3;
                    /* try { // try from 00baadcc to 00caadd7 has its CatchHandler @ 00babb64 */
  if ((ulong)(lVar6 * -0x71c71c71c71c71c7) < 0x1c71c71c71c71c7) {
    uVar7 = lVar6 * 0x1c71c71c71c71c72;
    uVar10 = uVar1;
    if (uVar1 <= uVar7) {
      uVar10 = uVar7;
    }
    if (uVar10 == 0) {
      lVar6 = 0;
      goto LAB_00baadf4;
    }
  }
                    /* try { // try from 00baadf0 to 00caadfb has its CatchHandler @ 00babb60 */
  lVar6 = _Znwm(uVar10 * 0x48);
LAB_00baadf4:
  uVar11 = *param_2;
  uVar13 = param_2[3];
  uVar12 = param_2[2];
  puVar5 = (undefined8 *)(lVar6 + lVar4 * 8);
  puVar5[1] = param_2[1];
  *puVar5 = uVar11;
  puVar5[3] = uVar13;
  puVar5[2] = uVar12;
  uVar12 = param_2[5];
  uVar11 = param_2[4];
  puVar5[6] = param_2[6];
  puVar5[5] = uVar12;
  puVar5[4] = uVar11;
                    /* try { // try from 00baae1c to 00caae27 has its CatchHandler @ 00babb14 */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar5 + 7) = *(undefined2 *)(param_2 + 7);
  puVar5[8] = param_2[8];
  pvVar8 = (void *)*param_1;
  pvVar3 = (void *)param_1[1];
  puVar2 = puVar5 + 9;
                    /* try { // try from 00baae38 to 00caae43 has its CatchHandler @ 00babb10 */
  __ptr = pvVar8;
  if (pvVar3 != pvVar8) {
                    /* try { // try from 00baae44 to 00caae63 has its CatchHandler @ 00babe60 */
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
                    /* try { // try from 00baae64 to 00caaed3 has its CatchHandler @ 00bac034 */
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
    }
  }
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
    return;
  }
                    /* try { // try from 00baaef4 to 00caaeff has its CatchHandler @ 00babdbc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baad5c"></a> `00baad5c` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baad60"></a> `00baad60` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baad64"></a> `00baad64` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baad68"></a> `00baad68` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baad6c"></a> `00baad6c` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baad70"></a> `00baad70` | `2a c7 91 d2` | mov x10,#0x8e39 | `FALL_THROUGH`
<a id="insn-00baad74"></a> `00baad74` | `6a 1c a7 f2` | movk x10,#0x38e3, LSL #16 | `FALL_THROUGH`
<a id="insn-00baad78"></a> `00baad78` | `d5 71 9c d2` | mov x21,#0xe38e | `FALL_THROUGH`
<a id="insn-00baad7c"></a> `00baad7c` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00baad80"></a> `00baad80` | `ca 71 dc f2` | movk x10,#0xe38e, LSL #32 | `FALL_THROUGH`
<a id="insn-00baad84"></a> `00baad84` | `15 c7 b1 f2` | movk x21,#0x8e38, LSL #16 | `FALL_THROUGH`
<a id="insn-00baad88"></a> `00baad88` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baad8c"></a> `00baad8c` | `0a c7 f1 f2` | movk x10,#0x8e38, LSL #48 | `FALL_THROUGH`
<a id="insn-00baad90"></a> `00baad90` | `75 1c c7 f2` | movk x21,#0x38e3, LSL #32 | `FALL_THROUGH`
<a id="insn-00baad94"></a> `00baad94` | `16 7d 0a 9b` | mul x22,x8,x10 | `FALL_THROUGH`
<a id="insn-00baad98"></a> `00baad98` | `d5 71 e0 f2` | movk x21,#0x38e, LSL #48 | `FALL_THROUGH`
<a id="insn-00baad9c"></a> `00baad9c` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00baada0"></a> `00baada0` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baada4"></a> `00baada4` | `28 0b 00 54` | b.hi 0x00baaf08 | `CONDITIONAL_JUMP`
<a id="insn-00baada8"></a> `00baada8` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baadac"></a> `00baadac` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baadb0"></a> `00baadb0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00baadb4"></a> `00baadb4` | `69 01 09 cb` | sub x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00baadb8"></a> `00baadb8` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00baadbc"></a> `00baadbc` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00baadc0"></a> `00baadc0` | `ca 38 8e d2` | mov x10,#0x71c6 | `FALL_THROUGH`
<a id="insn-00baadc4"></a> `00baadc4` | `8a e3 b8 f2` | movk x10,#0xc71c, LSL #16 | `FALL_THROUGH`
<a id="insn-00baadc8"></a> `00baadc8` | `2a 8e c3 f2` | movk x10,#0x1c71, LSL #32 | `FALL_THROUGH`
<a id="insn-00baadcc"></a> `00baadcc` | `ea 38 e0 f2` | movk x10,#0x1c7, LSL #48 | `FALL_THROUGH`
<a id="insn-00baadd0"></a> `00baadd0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00baadd4"></a> `00baadd4` | `a8 00 00 54` | b.hi 0x00baade8 | `CONDITIONAL_JUMP`
<a id="insn-00baadd8"></a> `00baadd8` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baaddc"></a> `00baaddc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00baade0"></a> `00baade0` | `15 31 89 9a` | csel x21,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00baade4"></a> `00baade4` | `f5 08 00 b4` | cbz x21,0x00baaf00 | `CONDITIONAL_JUMP`
<a id="insn-00baade8"></a> `00baade8` | `a8 0e 15 8b` | add x8,x21,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00baadec"></a> `00baadec` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baadf0"></a> `00baadf0` | `28 b4 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00baadf4"></a> `00baadf4` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-00baadf8"></a> `00baadf8` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00baadfc"></a> `00baadfc` | `c8 02 09 9b` | madd x8,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00baae00"></a> `00baae00` | `a9 02 09 9b` | madd x9,x21,x9,x0 | `FALL_THROUGH`
<a id="insn-00baae04"></a> `00baae04` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00baae08"></a> `00baae08` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baae0c"></a> `00baae0c` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00baae10"></a> `00baae10` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00baae14"></a> `00baae14` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00baae18"></a> `00baae18` | `8a 72 40 79` | ldrh w10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00baae1c"></a> `00baae1c` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00baae20"></a> `00baae20` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00baae24"></a> `00baae24` | `0a 71 00 79` | strh w10,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00baae28"></a> `00baae28` | `8a 22 40 f9` | ldr x10,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00baae2c"></a> `00baae2c` | `0a 21 00 f9` | str x10,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00baae30"></a> `00baae30` | `6b 36 40 a9` | ldp x11,x13,[x19] | `FALL_THROUGH`
<a id="insn-00baae34"></a> `00baae34` | `0a 21 01 91` | add x10,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00baae38"></a> `00baae38` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00baae3c"></a> `00baae3c` | `20 03 00 54` | b.eq 0x00baaea0 | `CONDITIONAL_JUMP`
<a id="insn-00baae40"></a> `00baae40` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00baae44"></a> `00baae44` | `6b 01 0d cb` | sub x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00baae48"></a> `00baae48` | `ae 01 0c 8b` | add x14,x13,x12 | `FALL_THROUGH`
<a id="insn-00baae4c"></a> `00baae4c` | `c0 81 dc 3c` | ldur q0,[x14, #-0x38] | `FALL_THROUGH`
<a id="insn-00baae50"></a> `00baae50` | `c1 81 db 3c` | ldur q1,[x14, #-0x48] | `FALL_THROUGH`
<a id="insn-00baae54"></a> `00baae54` | `0f 01 0c 8b` | add x15,x8,x12 | `FALL_THROUGH`
<a id="insn-00baae58"></a> `00baae58` | `8c 21 01 d1` | sub x12,x12,#0x48 | `FALL_THROUGH`
<a id="insn-00baae5c"></a> `00baae5c` | `e0 81 9c 3c` | stur q0,[x15, #-0x38] | `FALL_THROUGH`
<a id="insn-00baae60"></a> `00baae60` | `e1 81 9b 3c` | stur q1,[x15, #-0x48] | `FALL_THROUGH`
<a id="insn-00baae64"></a> `00baae64` | `d0 81 5e f8` | ldur x16,[x14, #-0x18] | `FALL_THROUGH`
<a id="insn-00baae68"></a> `00baae68` | `c0 81 dd 3c` | ldur q0,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00baae6c"></a> `00baae6c` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00baae70"></a> `00baae70` | `f0 81 1e f8` | stur x16,[x15, #-0x18] | `FALL_THROUGH`
<a id="insn-00baae74"></a> `00baae74` | `e0 81 9d 3c` | stur q0,[x15, #-0x28] | `FALL_THROUGH`
<a id="insn-00baae78"></a> `00baae78` | `d0 01 5f 78` | ldurh w16,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00baae7c"></a> `00baae7c` | `df 7d 3e a9` | stp xzr,xzr,[x14, #-0x20] | `FALL_THROUGH`
<a id="insn-00baae80"></a> `00baae80` | `df 81 1d f8` | stur xzr,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00baae84"></a> `00baae84` | `f0 01 1f 78` | sturh w16,[x15, #-0x10] | `FALL_THROUGH`
<a id="insn-00baae88"></a> `00baae88` | `ce 81 5f f8` | ldur x14,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00baae8c"></a> `00baae8c` | `ee 81 1f f8` | stur x14,[x15, #-0x8] | `FALL_THROUGH`
<a id="insn-00baae90"></a> `00baae90` | `c1 fd ff 54` | b.ne 0x00baae48 | `CONDITIONAL_JUMP`
<a id="insn-00baae94"></a> `00baae94` | `74 2e 40 a9` | ldp x20,x11,[x19] | `FALL_THROUGH`
<a id="insn-00baae98"></a> `00baae98` | `08 01 0c 8b` | add x8,x8,x12 | `FALL_THROUGH`
<a id="insn-00baae9c"></a> `00baae9c` | `02 00 00 14` | b 0x00baaea4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaea0"></a> `00baaea0` | `f4 03 0b aa` | mov x20,x11 | `FALL_THROUGH`
<a id="insn-00baaea4"></a> `00baaea4` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00baaea8"></a> `00baaea8` | `68 2a 00 a9` | stp x8,x10,[x19] | `FALL_THROUGH`
<a id="insn-00baaeac"></a> `00baaeac` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00baaeb0"></a> `00baaeb0` | `41 01 00 54` | b.ne 0x00baaed8 | `CONDITIONAL_JUMP`
<a id="insn-00baaeb4"></a> `00baaeb4` | `f4 01 00 b4` | cbz x20,0x00baaef0 | `CONDITIONAL_JUMP`
<a id="insn-00baaeb8"></a> `00baaeb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baaebc"></a> `00baaebc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaec0"></a> `00baaec0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaec4"></a> `00baaec4` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00baaec8"></a> `00baaec8` | `fa b3 02 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00baaecc"></a> `00baaecc` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baaed0"></a> `00baaed0` | `eb 03 13 aa` | mov x11,x19 | `FALL_THROUGH`
<a id="insn-00baaed4"></a> `00baaed4` | `00 ff ff 54` | b.eq 0x00baaeb4 | `CONDITIONAL_JUMP`
<a id="insn-00baaed8"></a> `00baaed8` | `68 81 5d 38` | ldurb w8,[x11, #-0x28] | `FALL_THROUGH`
<a id="insn-00baaedc"></a> `00baaedc` | `73 21 01 d1` | sub x19,x11,#0x48 | `FALL_THROUGH`
<a id="insn-00baaee0"></a> `00baaee0` | `68 ff 07 36` | tbz w8,#0x0,0x00baaecc | `CONDITIONAL_JUMP`
<a id="insn-00baaee4"></a> `00baaee4` | `60 81 5e f8` | ldur x0,[x11, #-0x18] | `FALL_THROUGH`
<a id="insn-00baaee8"></a> `00baaee8` | `f2 b3 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00baaeec"></a> `00baaeec` | `f8 ff ff 17` | b 0x00baaecc | `UNCONDITIONAL_JUMP`
<a id="insn-00baaef0"></a> `00baaef0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaef4"></a> `00baaef4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaef8"></a> `00baaef8` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00baaefc"></a> `00baaefc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baaf00"></a> `00baaf00` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00baaf04"></a> `00baaf04` | `bc ff ff 17` | b 0x00baadf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf08"></a> `00baaf08` | `8e c0 02 94` | bl 0x00c5b140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baad5c`](#insn-00baad5c) 範囲 `[['00baad5c', '00baad7b']]`
  - `FALL_THROUGH` [`00baad78`](#insn-00baad78) → [`00baad7c`](#insn-00baad7c)
- ブロック [`00baad7c`](#insn-00baad7c) 範囲 `[['00baad7c', '00baad9f']]`
  - `FALL_THROUGH` [`00baad9c`](#insn-00baad9c) → [`00baada0`](#insn-00baada0)
- ブロック [`00baada0`](#insn-00baada0) 範囲 `[['00baada0', '00baada7']]`
  - `CONDITIONAL_JUMP` [`00baada4`](#insn-00baada4) → [`00baaf08`](#insn-00baaf08)
  - `FALL_THROUGH` [`00baada4`](#insn-00baada4) → [`00baada8`](#insn-00baada8)
- ブロック [`00baada8`](#insn-00baada8) 範囲 `[['00baada8', '00baadcb']]`
  - `FALL_THROUGH` [`00baadc8`](#insn-00baadc8) → [`00baadcc`](#insn-00baadcc)
- ブロック [`00baadcc`](#insn-00baadcc) 範囲 `[['00baadcc', '00baadd7']]`
  - `CONDITIONAL_JUMP` [`00baadd4`](#insn-00baadd4) → [`00baade8`](#insn-00baade8)
  - `FALL_THROUGH` [`00baadd4`](#insn-00baadd4) → [`00baadd8`](#insn-00baadd8)
- ブロック [`00baadd8`](#insn-00baadd8) 範囲 `[['00baadd8', '00baade7']]`
  - `CONDITIONAL_JUMP` [`00baade4`](#insn-00baade4) → [`00baaf00`](#insn-00baaf00)
  - `FALL_THROUGH` [`00baade4`](#insn-00baade4) → [`00baade8`](#insn-00baade8)
- ブロック [`00baade8`](#insn-00baade8) 範囲 `[['00baade8', '00baadef']]`
  - `FALL_THROUGH` [`00baadec`](#insn-00baadec) → [`00baadf0`](#insn-00baadf0)
- ブロック [`00baadf0`](#insn-00baadf0) 範囲 `[['00baadf0', '00baadf3']]`
  - `FALL_THROUGH` [`00baadf0`](#insn-00baadf0) → [`00baadf4`](#insn-00baadf4)
- ブロック [`00baadf4`](#insn-00baadf4) 範囲 `[['00baadf4', '00baae1b']]`
  - `FALL_THROUGH` [`00baae18`](#insn-00baae18) → [`00baae1c`](#insn-00baae1c)
- ブロック [`00baae1c`](#insn-00baae1c) 範囲 `[['00baae1c', '00baae37']]`
  - `FALL_THROUGH` [`00baae34`](#insn-00baae34) → [`00baae38`](#insn-00baae38)
- ブロック [`00baae38`](#insn-00baae38) 範囲 `[['00baae38', '00baae3f']]`
  - `CONDITIONAL_JUMP` [`00baae3c`](#insn-00baae3c) → [`00baaea0`](#insn-00baaea0)
  - `FALL_THROUGH` [`00baae3c`](#insn-00baae3c) → [`00baae40`](#insn-00baae40)
- ブロック [`00baae40`](#insn-00baae40) 範囲 `[['00baae40', '00baae43']]`
  - `FALL_THROUGH` [`00baae40`](#insn-00baae40) → [`00baae44`](#insn-00baae44)
- ブロック [`00baae44`](#insn-00baae44) 範囲 `[['00baae44', '00baae47']]`
  - `FALL_THROUGH` [`00baae44`](#insn-00baae44) → [`00baae48`](#insn-00baae48)
- ブロック [`00baae48`](#insn-00baae48) 範囲 `[['00baae48', '00baae63']]`
  - `FALL_THROUGH` [`00baae60`](#insn-00baae60) → [`00baae64`](#insn-00baae64)
- ブロック [`00baae64`](#insn-00baae64) 範囲 `[['00baae64', '00baae93']]`
  - `CONDITIONAL_JUMP` [`00baae90`](#insn-00baae90) → [`00baae48`](#insn-00baae48)
  - `FALL_THROUGH` [`00baae90`](#insn-00baae90) → [`00baae94`](#insn-00baae94)
- ブロック [`00baae94`](#insn-00baae94) 範囲 `[['00baae94', '00baae9f']]`
  - `UNCONDITIONAL_JUMP` [`00baae9c`](#insn-00baae9c) → [`00baaea4`](#insn-00baaea4)
- ブロック [`00baaea0`](#insn-00baaea0) 範囲 `[['00baaea0', '00baaea3']]`
  - `FALL_THROUGH` [`00baaea0`](#insn-00baaea0) → [`00baaea4`](#insn-00baaea4)
- ブロック [`00baaea4`](#insn-00baaea4) 範囲 `[['00baaea4', '00baaeb3']]`
  - `CONDITIONAL_JUMP` [`00baaeb0`](#insn-00baaeb0) → [`00baaed8`](#insn-00baaed8)
  - `FALL_THROUGH` [`00baaeb0`](#insn-00baaeb0) → [`00baaeb4`](#insn-00baaeb4)
- ブロック [`00baaeb4`](#insn-00baaeb4) 範囲 `[['00baaeb4', '00baaeb7']]`
  - `CONDITIONAL_JUMP` [`00baaeb4`](#insn-00baaeb4) → [`00baaef0`](#insn-00baaef0)
  - `FALL_THROUGH` [`00baaeb4`](#insn-00baaeb4) → [`00baaeb8`](#insn-00baaeb8)
- ブロック [`00baaeb8`](#insn-00baaeb8) 範囲 `[['00baaeb8', '00baaecb']]`
- ブロック [`00baaecc`](#insn-00baaecc) 範囲 `[['00baaecc', '00baaed7']]`
  - `CONDITIONAL_JUMP` [`00baaed4`](#insn-00baaed4) → [`00baaeb4`](#insn-00baaeb4)
  - `FALL_THROUGH` [`00baaed4`](#insn-00baaed4) → [`00baaed8`](#insn-00baaed8)
- ブロック [`00baaed8`](#insn-00baaed8) 範囲 `[['00baaed8', '00baaee3']]`
  - `CONDITIONAL_JUMP` [`00baaee0`](#insn-00baaee0) → [`00baaecc`](#insn-00baaecc)
  - `FALL_THROUGH` [`00baaee0`](#insn-00baaee0) → [`00baaee4`](#insn-00baaee4)
- ブロック [`00baaee4`](#insn-00baaee4) 範囲 `[['00baaee4', '00baaeef']]`
  - `UNCONDITIONAL_JUMP` [`00baaeec`](#insn-00baaeec) → [`00baaecc`](#insn-00baaecc)
- ブロック [`00baaef0`](#insn-00baaef0) 範囲 `[['00baaef0', '00baaef3']]`
  - `FALL_THROUGH` [`00baaef0`](#insn-00baaef0) → [`00baaef4`](#insn-00baaef4)
- ブロック [`00baaef4`](#insn-00baaef4) 範囲 `[['00baaef4', '00baaeff']]`
- ブロック [`00baaf00`](#insn-00baaf00) 範囲 `[['00baaf00', '00baaf07']]`
  - `UNCONDITIONAL_JUMP` [`00baaf04`](#insn-00baaf04) → [`00baadf4`](#insn-00baadf4)
- ブロック [`00baaf08`](#insn-00baaf08) 範囲 `[['00baaf08', '00baaf0b']]`

## 命令位置別の参照

- [`00baad5c`](#insn-00baad5c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad60`](#insn-00baad60) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad64`](#insn-00baad64) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada4`](#insn-00baada4) → [`00baaf08`](#insn-00baaf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd4`](#insn-00baadd4) → [`00baade8`](#insn-00baade8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade4`](#insn-00baade4) → [`00baaf00`](#insn-00baaf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadf0`](#insn-00baadf0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00baae3c`](#insn-00baae3c) → [`00baaea0`](#insn-00baaea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae90`](#insn-00baae90) → [`00baae48`](#insn-00baae48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae9c`](#insn-00baae9c) → [`00baaea4`](#insn-00baaea4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaeb0`](#insn-00baaeb0) → [`00baaed8`](#insn-00baaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaeb4`](#insn-00baaeb4) → [`00baaef0`](#insn-00baaef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaebc`](#insn-00baaebc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaec0`](#insn-00baaec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaec8`](#insn-00baaec8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00baaed4`](#insn-00baaed4) → [`00baaeb4`](#insn-00baaeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaee0`](#insn-00baaee0) → [`00baaecc`](#insn-00baaecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaee8`](#insn-00baaee8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00baaeec`](#insn-00baaeec) → [`00baaecc`](#insn-00baaecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaef0`](#insn-00baaef0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaef4`](#insn-00baaef4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf04`](#insn-00baaf04) → [`00baadf4`](#insn-00baadf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf08`](#insn-00baaf08) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baad5c`](#insn-00baad5c)

~~~json
{
  "source": "00baad5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad60`](#insn-00baad60)

~~~json
{
  "source": "00baad60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad64`](#insn-00baad64)

~~~json
{
  "source": "00baad64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada4`](#insn-00baada4)

~~~json
{
  "source": "00baada4",
  "target": "00baaf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd4`](#insn-00baadd4)

~~~json
{
  "source": "00baadd4",
  "target": "00baade8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade4`](#insn-00baade4)

~~~json
{
  "source": "00baade4",
  "target": "00baaf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadf0`](#insn-00baadf0)

~~~json
{
  "source": "00baadf0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae3c`](#insn-00baae3c)

~~~json
{
  "source": "00baae3c",
  "target": "00baaea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae90`](#insn-00baae90)

~~~json
{
  "source": "00baae90",
  "target": "00baae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae9c`](#insn-00baae9c)

~~~json
{
  "source": "00baae9c",
  "target": "00baaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaeb0`](#insn-00baaeb0)

~~~json
{
  "source": "00baaeb0",
  "target": "00baaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaeb4`](#insn-00baaeb4)

~~~json
{
  "source": "00baaeb4",
  "target": "00baaef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaebc`](#insn-00baaebc)

~~~json
{
  "source": "00baaebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaec0`](#insn-00baaec0)

~~~json
{
  "source": "00baaec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaec8`](#insn-00baaec8)

~~~json
{
  "source": "00baaec8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaed4`](#insn-00baaed4)

~~~json
{
  "source": "00baaed4",
  "target": "00baaeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaee0`](#insn-00baaee0)

~~~json
{
  "source": "00baaee0",
  "target": "00baaecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaee8`](#insn-00baaee8)

~~~json
{
  "source": "00baaee8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaeec`](#insn-00baaeec)

~~~json
{
  "source": "00baaeec",
  "target": "00baaecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaef0`](#insn-00baaef0)

~~~json
{
  "source": "00baaef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaef4`](#insn-00baaef4)

~~~json
{
  "source": "00baaef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf04`](#insn-00baaf04)

~~~json
{
  "source": "00baaf04",
  "target": "00baadf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf08`](#insn-00baaf08)

~~~json
{
  "source": "00baaf08",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
