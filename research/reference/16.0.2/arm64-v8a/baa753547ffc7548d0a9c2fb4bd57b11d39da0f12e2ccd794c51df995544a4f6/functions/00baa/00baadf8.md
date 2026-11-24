# 00baadf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baad5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baad5c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-8f72f8107d8e4974cdc153759dc03c94)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00babdec`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babdec.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-582a8694debe8fdc6812fe4404489e8e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baadf8",
  "name": "_ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10431d987574dde46092a933516d6754526d9b30b45170d1e1cbc3ccab55bbd2",
  "source_text_sha256": "10431d987574dde46092a933516d6754526d9b30b45170d1e1cbc3ccab55bbd2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baadf8",
        "00baafa7"
      ]
    ],
    "bytes_sha256": "db8925f716d6d5470347ab0bef8087c85d6ee92b22fb27f3d97f1ced6862fad0",
    "instruction_count": 108,
    "instruction_bytes": 432,
    "body_bytes": 432,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d110](../00c5d/00c5d110.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b210](../00c5b/00c5b210.md)

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
  
                    /* try { // try from 00baae10 to 00caae1b has its CatchHandler @ 00babc20 */
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar10 = 0x38e38e38e38e38e;
  uVar1 = lVar4 * -0x71c71c71c71c71c7 + 1;
                    /* try { // try from 00baae3c to 00caae47 has its CatchHandler @ 00babbd4 */
  if (0x38e38e38e38e38e < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar6 = param_1[2] - *param_1 >> 3;
                    /* try { // try from 00baae60 to 00caae6b has its CatchHandler @ 00babbd0 */
  if ((ulong)(lVar6 * -0x71c71c71c71c71c7) < 0x1c71c71c71c71c7) {
    uVar7 = lVar6 * 0x1c71c71c71c71c72;
    uVar10 = uVar1;
    if (uVar1 <= uVar7) {
      uVar10 = uVar7;
    }
    if (uVar10 == 0) {
                    /* try { // try from 00baaf9c to 00caaf9f has its CatchHandler @ 00babd9c */
      lVar6 = 0;
      goto LAB_00baae90;
    }
  }
                    /* try { // try from 00baae8c to 00caae97 has its CatchHandler @ 00babb84 */
  lVar6 = _Znwm(uVar10 * 0x48);
LAB_00baae90:
  uVar11 = *param_2;
  uVar13 = param_2[3];
  uVar12 = param_2[2];
  puVar5 = (undefined8 *)(lVar6 + lVar4 * 8);
  puVar5[1] = param_2[1];
  *puVar5 = uVar11;
  puVar5[3] = uVar13;
  puVar5[2] = uVar12;
                    /* try { // try from 00baaea8 to 00caaeb3 has its CatchHandler @ 00babb80 */
  uVar12 = param_2[5];
  uVar11 = param_2[4];
  puVar5[6] = param_2[6];
  puVar5[5] = uVar12;
  puVar5[4] = uVar11;
                    /* try { // try from 00baaeb4 to 00caaed3 has its CatchHandler @ 00babed0 */
  param_2[5] = 0;
  param_2[6] = 0;
  param_2[4] = 0;
  *(undefined2 *)(puVar5 + 7) = *(undefined2 *)(param_2 + 7);
  puVar5[8] = param_2[8];
  pvVar8 = (void *)*param_1;
  pvVar3 = (void *)param_1[1];
  puVar2 = puVar5 + 9;
                    /* try { // try from 00baaed4 to 00caaf43 has its CatchHandler @ 00bac0a4 */
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
                    /* try { // try from 00baaf88 to 00caaf93 has its CatchHandler @ 00babdbc */
    }
  }
  if (__ptr != (void *)0x0) {
                    /* try { // try from 00baaf64 to 00caaf6f has its CatchHandler @ 00babe2c */
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
<a id="insn-00baadf8"></a> `00baadf8` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00baadfc"></a> `00baadfc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baae00"></a> `00baae00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baae04"></a> `00baae04` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00baae08"></a> `00baae08` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00baae0c"></a> `00baae0c` | `2a c7 91 d2` | mov x10,#0x8e39 | `FALL_THROUGH`
<a id="insn-00baae10"></a> `00baae10` | `6a 1c a7 f2` | movk x10,#0x38e3, LSL #16 | `FALL_THROUGH`
<a id="insn-00baae14"></a> `00baae14` | `d5 71 9c d2` | mov x21,#0xe38e | `FALL_THROUGH`
<a id="insn-00baae18"></a> `00baae18` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00baae1c"></a> `00baae1c` | `ca 71 dc f2` | movk x10,#0xe38e, LSL #32 | `FALL_THROUGH`
<a id="insn-00baae20"></a> `00baae20` | `15 c7 b1 f2` | movk x21,#0x8e38, LSL #16 | `FALL_THROUGH`
<a id="insn-00baae24"></a> `00baae24` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baae28"></a> `00baae28` | `0a c7 f1 f2` | movk x10,#0x8e38, LSL #48 | `FALL_THROUGH`
<a id="insn-00baae2c"></a> `00baae2c` | `75 1c c7 f2` | movk x21,#0x38e3, LSL #32 | `FALL_THROUGH`
<a id="insn-00baae30"></a> `00baae30` | `16 7d 0a 9b` | mul x22,x8,x10 | `FALL_THROUGH`
<a id="insn-00baae34"></a> `00baae34` | `d5 71 e0 f2` | movk x21,#0x38e, LSL #48 | `FALL_THROUGH`
<a id="insn-00baae38"></a> `00baae38` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00baae3c"></a> `00baae3c` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baae40"></a> `00baae40` | `28 0b 00 54` | b.hi 0x00baafa4 | `CONDITIONAL_JUMP`
<a id="insn-00baae44"></a> `00baae44` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baae48"></a> `00baae48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baae4c"></a> `00baae4c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00baae50"></a> `00baae50` | `69 01 09 cb` | sub x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00baae54"></a> `00baae54` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00baae58"></a> `00baae58` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00baae5c"></a> `00baae5c` | `ca 38 8e d2` | mov x10,#0x71c6 | `FALL_THROUGH`
<a id="insn-00baae60"></a> `00baae60` | `8a e3 b8 f2` | movk x10,#0xc71c, LSL #16 | `FALL_THROUGH`
<a id="insn-00baae64"></a> `00baae64` | `2a 8e c3 f2` | movk x10,#0x1c71, LSL #32 | `FALL_THROUGH`
<a id="insn-00baae68"></a> `00baae68` | `ea 38 e0 f2` | movk x10,#0x1c7, LSL #48 | `FALL_THROUGH`
<a id="insn-00baae6c"></a> `00baae6c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00baae70"></a> `00baae70` | `a8 00 00 54` | b.hi 0x00baae84 | `CONDITIONAL_JUMP`
<a id="insn-00baae74"></a> `00baae74` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00baae78"></a> `00baae78` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00baae7c"></a> `00baae7c` | `15 31 89 9a` | csel x21,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00baae80"></a> `00baae80` | `f5 08 00 b4` | cbz x21,0x00baaf9c | `CONDITIONAL_JUMP`
<a id="insn-00baae84"></a> `00baae84` | `a8 0e 15 8b` | add x8,x21,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00baae88"></a> `00baae88` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00baae8c"></a> `00baae8c` | `35 b4 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00baae90"></a> `00baae90` | `80 06 40 ad` | ldp q0,q1,[x20] | `FALL_THROUGH`
<a id="insn-00baae94"></a> `00baae94` | `09 09 80 52` | mov w9,#0x48 | `FALL_THROUGH`
<a id="insn-00baae98"></a> `00baae98` | `c8 02 09 9b` | madd x8,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00baae9c"></a> `00baae9c` | `a9 02 09 9b` | madd x9,x21,x9,x0 | `FALL_THROUGH`
<a id="insn-00baaea0"></a> `00baaea0` | `00 05 00 ad` | stp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00baaea4"></a> `00baaea4` | `8a 1a 40 f9` | ldr x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00baaea8"></a> `00baaea8` | `80 0a c0 3d` | ldr q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00baaeac"></a> `00baaeac` | `0a 19 00 f9` | str x10,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00baaeb0"></a> `00baaeb0` | `00 09 80 3d` | str q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00baaeb4"></a> `00baaeb4` | `8a 72 40 79` | ldrh w10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00baaeb8"></a> `00baaeb8` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00baaebc"></a> `00baaebc` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00baaec0"></a> `00baaec0` | `0a 71 00 79` | strh w10,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00baaec4"></a> `00baaec4` | `8a 22 40 f9` | ldr x10,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00baaec8"></a> `00baaec8` | `0a 21 00 f9` | str x10,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00baaecc"></a> `00baaecc` | `6b 36 40 a9` | ldp x11,x13,[x19] | `FALL_THROUGH`
<a id="insn-00baaed0"></a> `00baaed0` | `0a 21 01 91` | add x10,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00baaed4"></a> `00baaed4` | `bf 01 0b eb` | cmp x13,x11 | `FALL_THROUGH`
<a id="insn-00baaed8"></a> `00baaed8` | `20 03 00 54` | b.eq 0x00baaf3c | `CONDITIONAL_JUMP`
<a id="insn-00baaedc"></a> `00baaedc` | `ec 03 1f aa` | mov x12,xzr | `FALL_THROUGH`
<a id="insn-00baaee0"></a> `00baaee0` | `6b 01 0d cb` | sub x11,x11,x13 | `FALL_THROUGH`
<a id="insn-00baaee4"></a> `00baaee4` | `ae 01 0c 8b` | add x14,x13,x12 | `FALL_THROUGH`
<a id="insn-00baaee8"></a> `00baaee8` | `c0 81 dc 3c` | ldur q0,[x14, #-0x38] | `FALL_THROUGH`
<a id="insn-00baaeec"></a> `00baaeec` | `c1 81 db 3c` | ldur q1,[x14, #-0x48] | `FALL_THROUGH`
<a id="insn-00baaef0"></a> `00baaef0` | `0f 01 0c 8b` | add x15,x8,x12 | `FALL_THROUGH`
<a id="insn-00baaef4"></a> `00baaef4` | `8c 21 01 d1` | sub x12,x12,#0x48 | `FALL_THROUGH`
<a id="insn-00baaef8"></a> `00baaef8` | `e0 81 9c 3c` | stur q0,[x15, #-0x38] | `FALL_THROUGH`
<a id="insn-00baaefc"></a> `00baaefc` | `e1 81 9b 3c` | stur q1,[x15, #-0x48] | `FALL_THROUGH`
<a id="insn-00baaf00"></a> `00baaf00` | `d0 81 5e f8` | ldur x16,[x14, #-0x18] | `FALL_THROUGH`
<a id="insn-00baaf04"></a> `00baaf04` | `c0 81 dd 3c` | ldur q0,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00baaf08"></a> `00baaf08` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00baaf0c"></a> `00baaf0c` | `f0 81 1e f8` | stur x16,[x15, #-0x18] | `FALL_THROUGH`
<a id="insn-00baaf10"></a> `00baaf10` | `e0 81 9d 3c` | stur q0,[x15, #-0x28] | `FALL_THROUGH`
<a id="insn-00baaf14"></a> `00baaf14` | `d0 01 5f 78` | ldurh w16,[x14, #-0x10] | `FALL_THROUGH`
<a id="insn-00baaf18"></a> `00baaf18` | `df 7d 3e a9` | stp xzr,xzr,[x14, #-0x20] | `FALL_THROUGH`
<a id="insn-00baaf1c"></a> `00baaf1c` | `df 81 1d f8` | stur xzr,[x14, #-0x28] | `FALL_THROUGH`
<a id="insn-00baaf20"></a> `00baaf20` | `f0 01 1f 78` | sturh w16,[x15, #-0x10] | `FALL_THROUGH`
<a id="insn-00baaf24"></a> `00baaf24` | `ce 81 5f f8` | ldur x14,[x14, #-0x8] | `FALL_THROUGH`
<a id="insn-00baaf28"></a> `00baaf28` | `ee 81 1f f8` | stur x14,[x15, #-0x8] | `FALL_THROUGH`
<a id="insn-00baaf2c"></a> `00baaf2c` | `c1 fd ff 54` | b.ne 0x00baaee4 | `CONDITIONAL_JUMP`
<a id="insn-00baaf30"></a> `00baaf30` | `74 2e 40 a9` | ldp x20,x11,[x19] | `FALL_THROUGH`
<a id="insn-00baaf34"></a> `00baaf34` | `08 01 0c 8b` | add x8,x8,x12 | `FALL_THROUGH`
<a id="insn-00baaf38"></a> `00baaf38` | `02 00 00 14` | b 0x00baaf40 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf3c"></a> `00baaf3c` | `f4 03 0b aa` | mov x20,x11 | `FALL_THROUGH`
<a id="insn-00baaf40"></a> `00baaf40` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00baaf44"></a> `00baaf44` | `68 2a 00 a9` | stp x8,x10,[x19] | `FALL_THROUGH`
<a id="insn-00baaf48"></a> `00baaf48` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf4c"></a> `00baaf4c` | `41 01 00 54` | b.ne 0x00baaf74 | `CONDITIONAL_JUMP`
<a id="insn-00baaf50"></a> `00baaf50` | `f4 01 00 b4` | cbz x20,0x00baaf8c | `CONDITIONAL_JUMP`
<a id="insn-00baaf54"></a> `00baaf54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00baaf58"></a> `00baaf58` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf5c"></a> `00baaf5c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf60"></a> `00baaf60` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00baaf64"></a> `00baaf64` | `07 b4 02 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00baaf68"></a> `00baaf68` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00baaf6c"></a> `00baaf6c` | `eb 03 13 aa` | mov x11,x19 | `FALL_THROUGH`
<a id="insn-00baaf70"></a> `00baaf70` | `00 ff ff 54` | b.eq 0x00baaf50 | `CONDITIONAL_JUMP`
<a id="insn-00baaf74"></a> `00baaf74` | `68 81 5d 38` | ldurb w8,[x11, #-0x28] | `FALL_THROUGH`
<a id="insn-00baaf78"></a> `00baaf78` | `73 21 01 d1` | sub x19,x11,#0x48 | `FALL_THROUGH`
<a id="insn-00baaf7c"></a> `00baaf7c` | `68 ff 07 36` | tbz w8,#0x0,0x00baaf68 | `CONDITIONAL_JUMP`
<a id="insn-00baaf80"></a> `00baaf80` | `60 81 5e f8` | ldur x0,[x11, #-0x18] | `FALL_THROUGH`
<a id="insn-00baaf84"></a> `00baaf84` | `ff b3 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf88"></a> `00baaf88` | `f8 ff ff 17` | b 0x00baaf68 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf8c"></a> `00baaf8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf90"></a> `00baaf90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf94"></a> `00baaf94` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00baaf98"></a> `00baaf98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baaf9c"></a> `00baaf9c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00baafa0"></a> `00baafa0` | `bc ff ff 17` | b 0x00baae90 | `UNCONDITIONAL_JUMP`
<a id="insn-00baafa4"></a> `00baafa4` | `9b c0 02 94` | bl 0x00c5b210 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baadf8`](#insn-00baadf8) 範囲 `[['00baadf8', '00baae0f']]`
  - `FALL_THROUGH` [`00baae0c`](#insn-00baae0c) → [`00baae10`](#insn-00baae10)
- ブロック [`00baae10`](#insn-00baae10) 範囲 `[['00baae10', '00baae3b']]`
  - `FALL_THROUGH` [`00baae38`](#insn-00baae38) → [`00baae3c`](#insn-00baae3c)
- ブロック [`00baae3c`](#insn-00baae3c) 範囲 `[['00baae3c', '00baae43']]`
  - `CONDITIONAL_JUMP` [`00baae40`](#insn-00baae40) → [`00baafa4`](#insn-00baafa4)
  - `FALL_THROUGH` [`00baae40`](#insn-00baae40) → [`00baae44`](#insn-00baae44)
- ブロック [`00baae44`](#insn-00baae44) 範囲 `[['00baae44', '00baae5f']]`
  - `FALL_THROUGH` [`00baae5c`](#insn-00baae5c) → [`00baae60`](#insn-00baae60)
- ブロック [`00baae60`](#insn-00baae60) 範囲 `[['00baae60', '00baae73']]`
  - `CONDITIONAL_JUMP` [`00baae70`](#insn-00baae70) → [`00baae84`](#insn-00baae84)
  - `FALL_THROUGH` [`00baae70`](#insn-00baae70) → [`00baae74`](#insn-00baae74)
- ブロック [`00baae74`](#insn-00baae74) 範囲 `[['00baae74', '00baae83']]`
  - `CONDITIONAL_JUMP` [`00baae80`](#insn-00baae80) → [`00baaf9c`](#insn-00baaf9c)
  - `FALL_THROUGH` [`00baae80`](#insn-00baae80) → [`00baae84`](#insn-00baae84)
- ブロック [`00baae84`](#insn-00baae84) 範囲 `[['00baae84', '00baae8b']]`
  - `FALL_THROUGH` [`00baae88`](#insn-00baae88) → [`00baae8c`](#insn-00baae8c)
- ブロック [`00baae8c`](#insn-00baae8c) 範囲 `[['00baae8c', '00baae8f']]`
  - `FALL_THROUGH` [`00baae8c`](#insn-00baae8c) → [`00baae90`](#insn-00baae90)
- ブロック [`00baae90`](#insn-00baae90) 範囲 `[['00baae90', '00baaea7']]`
  - `FALL_THROUGH` [`00baaea4`](#insn-00baaea4) → [`00baaea8`](#insn-00baaea8)
- ブロック [`00baaea8`](#insn-00baaea8) 範囲 `[['00baaea8', '00baaeb3']]`
  - `FALL_THROUGH` [`00baaeb0`](#insn-00baaeb0) → [`00baaeb4`](#insn-00baaeb4)
- ブロック [`00baaeb4`](#insn-00baaeb4) 範囲 `[['00baaeb4', '00baaed3']]`
  - `FALL_THROUGH` [`00baaed0`](#insn-00baaed0) → [`00baaed4`](#insn-00baaed4)
- ブロック [`00baaed4`](#insn-00baaed4) 範囲 `[['00baaed4', '00baaedb']]`
  - `CONDITIONAL_JUMP` [`00baaed8`](#insn-00baaed8) → [`00baaf3c`](#insn-00baaf3c)
  - `FALL_THROUGH` [`00baaed8`](#insn-00baaed8) → [`00baaedc`](#insn-00baaedc)
- ブロック [`00baaedc`](#insn-00baaedc) 範囲 `[['00baaedc', '00baaee3']]`
  - `FALL_THROUGH` [`00baaee0`](#insn-00baaee0) → [`00baaee4`](#insn-00baaee4)
- ブロック [`00baaee4`](#insn-00baaee4) 範囲 `[['00baaee4', '00baaf2f']]`
  - `CONDITIONAL_JUMP` [`00baaf2c`](#insn-00baaf2c) → [`00baaee4`](#insn-00baaee4)
  - `FALL_THROUGH` [`00baaf2c`](#insn-00baaf2c) → [`00baaf30`](#insn-00baaf30)
- ブロック [`00baaf30`](#insn-00baaf30) 範囲 `[['00baaf30', '00baaf3b']]`
  - `UNCONDITIONAL_JUMP` [`00baaf38`](#insn-00baaf38) → [`00baaf40`](#insn-00baaf40)
- ブロック [`00baaf3c`](#insn-00baaf3c) 範囲 `[['00baaf3c', '00baaf3f']]`
  - `FALL_THROUGH` [`00baaf3c`](#insn-00baaf3c) → [`00baaf40`](#insn-00baaf40)
- ブロック [`00baaf40`](#insn-00baaf40) 範囲 `[['00baaf40', '00baaf4f']]`
  - `CONDITIONAL_JUMP` [`00baaf4c`](#insn-00baaf4c) → [`00baaf74`](#insn-00baaf74)
  - `FALL_THROUGH` [`00baaf4c`](#insn-00baaf4c) → [`00baaf50`](#insn-00baaf50)
- ブロック [`00baaf50`](#insn-00baaf50) 範囲 `[['00baaf50', '00baaf53']]`
  - `CONDITIONAL_JUMP` [`00baaf50`](#insn-00baaf50) → [`00baaf8c`](#insn-00baaf8c)
  - `FALL_THROUGH` [`00baaf50`](#insn-00baaf50) → [`00baaf54`](#insn-00baaf54)
- ブロック [`00baaf54`](#insn-00baaf54) 範囲 `[['00baaf54', '00baaf63']]`
  - `FALL_THROUGH` [`00baaf60`](#insn-00baaf60) → [`00baaf64`](#insn-00baaf64)
- ブロック [`00baaf64`](#insn-00baaf64) 範囲 `[['00baaf64', '00baaf67']]`
- ブロック [`00baaf68`](#insn-00baaf68) 範囲 `[['00baaf68', '00baaf73']]`
  - `CONDITIONAL_JUMP` [`00baaf70`](#insn-00baaf70) → [`00baaf50`](#insn-00baaf50)
  - `FALL_THROUGH` [`00baaf70`](#insn-00baaf70) → [`00baaf74`](#insn-00baaf74)
- ブロック [`00baaf74`](#insn-00baaf74) 範囲 `[['00baaf74', '00baaf7f']]`
  - `CONDITIONAL_JUMP` [`00baaf7c`](#insn-00baaf7c) → [`00baaf68`](#insn-00baaf68)
  - `FALL_THROUGH` [`00baaf7c`](#insn-00baaf7c) → [`00baaf80`](#insn-00baaf80)
- ブロック [`00baaf80`](#insn-00baaf80) 範囲 `[['00baaf80', '00baaf87']]`
  - `FALL_THROUGH` [`00baaf84`](#insn-00baaf84) → [`00baaf88`](#insn-00baaf88)
- ブロック [`00baaf88`](#insn-00baaf88) 範囲 `[['00baaf88', '00baaf8b']]`
  - `UNCONDITIONAL_JUMP` [`00baaf88`](#insn-00baaf88) → [`00baaf68`](#insn-00baaf68)
- ブロック [`00baaf8c`](#insn-00baaf8c) 範囲 `[['00baaf8c', '00baaf9b']]`
- ブロック [`00baaf9c`](#insn-00baaf9c) 範囲 `[['00baaf9c', '00baafa3']]`
  - `UNCONDITIONAL_JUMP` [`00baafa0`](#insn-00baafa0) → [`00baae90`](#insn-00baae90)
- ブロック [`00baafa4`](#insn-00baafa4) 範囲 `[['00baafa4', '00baafa7']]`

## 命令位置別の参照

- [`00baadf8`](#insn-00baadf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadfc`](#insn-00baadfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae00`](#insn-00baae00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae40`](#insn-00baae40) → [`00baafa4`](#insn-00baafa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae70`](#insn-00baae70) → [`00baae84`](#insn-00baae84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae80`](#insn-00baae80) → [`00baaf9c`](#insn-00baaf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae8c`](#insn-00baae8c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00baaed8`](#insn-00baaed8) → [`00baaf3c`](#insn-00baaf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf2c`](#insn-00baaf2c) → [`00baaee4`](#insn-00baaee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf38`](#insn-00baaf38) → [`00baaf40`](#insn-00baaf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf4c`](#insn-00baaf4c) → [`00baaf74`](#insn-00baaf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf50`](#insn-00baaf50) → [`00baaf8c`](#insn-00baaf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf58`](#insn-00baaf58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf5c`](#insn-00baaf5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf64`](#insn-00baaf64) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00baaf70`](#insn-00baaf70) → [`00baaf50`](#insn-00baaf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf7c`](#insn-00baaf7c) → [`00baaf68`](#insn-00baaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf84`](#insn-00baaf84) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00baaf88`](#insn-00baaf88) → [`00baaf68`](#insn-00baaf68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf8c`](#insn-00baaf8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf90`](#insn-00baaf90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa0`](#insn-00baafa0) → [`00baae90`](#insn-00baae90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa4`](#insn-00baafa4) → [`00c5b210`](../00c5b/00c5b210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b210` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baadf8`](#insn-00baadf8)

~~~json
{
  "source": "00baadf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadfc`](#insn-00baadfc)

~~~json
{
  "source": "00baadfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae00`](#insn-00baae00)

~~~json
{
  "source": "00baae00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae40`](#insn-00baae40)

~~~json
{
  "source": "00baae40",
  "target": "00baafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae70`](#insn-00baae70)

~~~json
{
  "source": "00baae70",
  "target": "00baae84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae80`](#insn-00baae80)

~~~json
{
  "source": "00baae80",
  "target": "00baaf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae8c`](#insn-00baae8c)

~~~json
{
  "source": "00baae8c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaed8`](#insn-00baaed8)

~~~json
{
  "source": "00baaed8",
  "target": "00baaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf2c`](#insn-00baaf2c)

~~~json
{
  "source": "00baaf2c",
  "target": "00baaee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf38`](#insn-00baaf38)

~~~json
{
  "source": "00baaf38",
  "target": "00baaf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf4c`](#insn-00baaf4c)

~~~json
{
  "source": "00baaf4c",
  "target": "00baaf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf50`](#insn-00baaf50)

~~~json
{
  "source": "00baaf50",
  "target": "00baaf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf58`](#insn-00baaf58)

~~~json
{
  "source": "00baaf58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf5c`](#insn-00baaf5c)

~~~json
{
  "source": "00baaf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf64`](#insn-00baaf64)

~~~json
{
  "source": "00baaf64",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf70`](#insn-00baaf70)

~~~json
{
  "source": "00baaf70",
  "target": "00baaf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf7c`](#insn-00baaf7c)

~~~json
{
  "source": "00baaf7c",
  "target": "00baaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf84`](#insn-00baaf84)

~~~json
{
  "source": "00baaf84",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf88`](#insn-00baaf88)

~~~json
{
  "source": "00baaf88",
  "target": "00baaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf8c`](#insn-00baaf8c)

~~~json
{
  "source": "00baaf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf90`](#insn-00baaf90)

~~~json
{
  "source": "00baaf90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa0`](#insn-00baafa0)

~~~json
{
  "source": "00baafa0",
  "target": "00baae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa4`](#insn-00baafa4)

~~~json
{
  "source": "00baafa4",
  "target": "00c5b210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
