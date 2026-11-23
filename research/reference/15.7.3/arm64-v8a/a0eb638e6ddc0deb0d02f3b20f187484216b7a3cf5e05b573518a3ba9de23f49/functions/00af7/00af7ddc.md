# 00af7ddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af7d14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7d14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-2f79d57820c779a046ba41c0cd8d3bca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af7e20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af7/00af7e20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-12e8fbcb2cce9b173f947845c0649050)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af7ddc",
  "name": "_ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_",
  "size": 352,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d2be82af3f607f9c527e591875f8cfbc4ec055e7dcc8313dc7c7eca030bd1b1",
  "source_text_sha256": "5d2be82af3f607f9c527e591875f8cfbc4ec055e7dcc8313dc7c7eca030bd1b1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af7ddc",
        "00af7f3b"
      ]
    ],
    "bytes_sha256": "9ea45b26814909043077f1ada6511466bc94f8e0ca015efb240c39259bff6695",
    "instruction_count": 88,
    "instruction_bytes": 352,
    "body_bytes": 352,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde780](../00bde/00bde780.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3473 bytes

~~~c

void _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_
               (long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  byte bVar3;
  byte *pbVar4;
  long lVar5;
  byte *pbVar6;
  long lVar7;
  ulong uVar8;
  undefined8 *puVar9;
  byte *pbVar10;
  byte *__ptr;
  ulong uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  
                    /* try { // try from 00af7df8 to 00bf7e5b has its CatchHandler @ 00af560c */
  lVar5 = param_1[1] - *param_1 >> 3;
  uVar11 = 0xaaaaaaaaaaaaaaa;
  uVar1 = lVar5 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  lVar7 = param_1[2] - *param_1 >> 3;
  if ((ulong)(lVar7 * -0x5555555555555555) < 0x555555555555555) {
    uVar8 = lVar7 * 0x5555555555555556;
    uVar11 = uVar1;
    if (uVar1 <= uVar8) {
      uVar11 = uVar8;
    }
    if (uVar11 == 0) {
      lVar7 = 0;
                    /* try { // try from 00af7f34 to 00bf7f4f has its CatchHandler @ 00aff1e4 */
      goto LAB_00af7e60;
    }
  }
                    /* try { // try from 00af7e5c to 00bf7e5f has its CatchHandler @ 00b0037c */
  lVar7 = _Znwm(uVar11 * 0x18);
LAB_00af7e60:
  uVar13 = param_2[1];
  uVar12 = *param_2;
  puVar9 = (undefined8 *)(lVar7 + lVar5 * 8);
  puVar9[2] = param_2[2];
  puVar9[1] = uVar13;
  *puVar9 = uVar12;
  param_2[1] = 0;
  param_2[2] = 0;
  *param_2 = 0;
  pbVar6 = (byte *)*param_1;
  pbVar10 = (byte *)param_1[1];
  puVar2 = puVar9 + 3;
  __ptr = pbVar6;
  if (pbVar10 != pbVar6) {
    do {
      uVar13 = *(undefined8 *)(pbVar10 + -0x10);
      uVar12 = *(undefined8 *)(pbVar10 + -0x18);
                    /* try { // try from 00af7ea0 to 00bf7eab has its CatchHandler @ 00aff238 */
      puVar9[-1] = *(undefined8 *)(pbVar10 + -8);
      puVar9[-2] = uVar13;
      puVar9[-3] = uVar12;
      pbVar10[-0x10] = 0;
      pbVar10[-0xf] = 0;
      pbVar10[-0xe] = 0;
      pbVar10[-0xd] = 0;
      pbVar10[-0xc] = 0;
      pbVar10[-0xb] = 0;
      pbVar10[-10] = 0;
      pbVar10[-9] = 0;
      pbVar10[-8] = 0;
      pbVar10[-7] = 0;
      pbVar10[-6] = 0;
      pbVar10[-5] = 0;
      pbVar10[-4] = 0;
      pbVar10[-3] = 0;
      pbVar10[-2] = 0;
      pbVar10[-1] = 0;
      pbVar10[-0x18] = 0;
      pbVar10[-0x17] = 0;
      pbVar10[-0x16] = 0;
      pbVar10[-0x15] = 0;
      pbVar10[-0x14] = 0;
      pbVar10[-0x13] = 0;
      pbVar10[-0x12] = 0;
      pbVar10[-0x11] = 0;
                    /* try { // try from 00af7eb0 to 00bf7ecb has its CatchHandler @ 00aff1fc */
      pbVar10 = pbVar10 + -0x18;
      puVar9 = puVar9 + -3;
    } while (pbVar6 != pbVar10);
    pbVar6 = (byte *)param_1[1];
    __ptr = (byte *)*param_1;
  }
                    /* try { // try from 00af7ed0 to 00bf7edf has its CatchHandler @ 00b0037c */
  *param_1 = (long)puVar9;
  param_1[1] = (long)puVar2;
  param_1[2] = lVar7 + uVar11 * 0x18;
  if (pbVar6 != __ptr) {
    bVar3 = pbVar6[-0x18];
    pbVar10 = pbVar6 + -0x18;
    while( true ) {
      pbVar4 = pbVar10;
      if ((bVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar6 + -8));
      }
      if (__ptr == pbVar4) break;
      bVar3 = pbVar4[-0x18];
      pbVar10 = pbVar4 + -0x18;
      pbVar6 = pbVar4;
    }
  }
  if (__ptr != (byte *)0x0) {
    _ZdlPv(__ptr);
    return;
  }
                    /* try { // try from 00af7f24 to 00bf7f2f has its CatchHandler @ 00aff1f8 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af7ddc"></a> `00af7ddc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af7de0"></a> `00af7de0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7de4"></a> `00af7de4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7de8"></a> `00af7de8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00af7dec"></a> `00af7dec` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00af7df0"></a> `00af7df0` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00af7df4"></a> `00af7df4` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00af7df8"></a> `00af7df8` | `f5 f3 01 b2` | orr x21,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00af7dfc"></a> `00af7dfc` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00af7e00"></a> `00af7e00` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00af7e04"></a> `00af7e04` | `16 7d 0a 9b` | mul x22,x8,x10 | `FALL_THROUGH`
<a id="insn-00af7e08"></a> `00af7e08` | `55 55 e1 f2` | movk x21,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00af7e0c"></a> `00af7e0c` | `c8 06 00 91` | add x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00af7e10"></a> `00af7e10` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00af7e14"></a> `00af7e14` | `28 09 00 54` | b.hi 0x00af7f38 | `CONDITIONAL_JUMP`
<a id="insn-00af7e18"></a> `00af7e18` | `0b 08 40 f9` | ldr x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00af7e1c"></a> `00af7e1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af7e20"></a> `00af7e20` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00af7e24"></a> `00af7e24` | `69 01 09 cb` | sub x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00af7e28"></a> `00af7e28` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00af7e2c"></a> `00af7e2c` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00af7e30"></a> `00af7e30` | `ea f3 00 b2` | orr x10,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00af7e34"></a> `00af7e34` | `8a aa 8a f2` | movk x10,#0x5554 | `FALL_THROUGH`
<a id="insn-00af7e38"></a> `00af7e38` | `aa aa e0 f2` | movk x10,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00af7e3c"></a> `00af7e3c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00af7e40"></a> `00af7e40` | `a8 00 00 54` | b.hi 0x00af7e54 | `CONDITIONAL_JUMP`
<a id="insn-00af7e44"></a> `00af7e44` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00af7e48"></a> `00af7e48` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00af7e4c"></a> `00af7e4c` | `15 31 89 9a` | csel x21,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00af7e50"></a> `00af7e50` | `15 07 00 b4` | cbz x21,0x00af7f30 | `CONDITIONAL_JUMP`
<a id="insn-00af7e54"></a> `00af7e54` | `a8 06 15 8b` | add x8,x21,x21, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00af7e58"></a> `00af7e58` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00af7e5c"></a> `00af7e5c` | `65 8c 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00af7e60"></a> `00af7e60` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00af7e64"></a> `00af7e64` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-00af7e68"></a> `00af7e68` | `09 03 80 52` | mov w9,#0x18 | `FALL_THROUGH`
<a id="insn-00af7e6c"></a> `00af7e6c` | `ca 02 09 9b` | madd x10,x22,x9,x0 | `FALL_THROUGH`
<a id="insn-00af7e70"></a> `00af7e70` | `48 09 00 f9` | str x8,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00af7e74"></a> `00af7e74` | `40 01 80 3d` | str q0,[x10] | `FALL_THROUGH`
<a id="insn-00af7e78"></a> `00af7e78` | `9f fe 00 a9` | stp xzr,xzr,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00af7e7c"></a> `00af7e7c` | `9f 02 00 f9` | str xzr,[x20] | `FALL_THROUGH`
<a id="insn-00af7e80"></a> `00af7e80` | `68 32 40 a9` | ldp x8,x12,[x19] | `FALL_THROUGH`
<a id="insn-00af7e84"></a> `00af7e84` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00af7e88"></a> `00af7e88` | `a9 02 09 9b` | madd x9,x21,x9,x0 | `FALL_THROUGH`
<a id="insn-00af7e8c"></a> `00af7e8c` | `4b 61 00 91` | add x11,x10,#0x18 | `FALL_THROUGH`
<a id="insn-00af7e90"></a> `00af7e90` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00af7e94"></a> `00af7e94` | `a0 01 00 54` | b.eq 0x00af7ec8 | `CONDITIONAL_JUMP`
<a id="insn-00af7e98"></a> `00af7e98` | `8d 81 5f f8` | ldur x13,[x12, #-0x8] | `FALL_THROUGH`
<a id="insn-00af7e9c"></a> `00af7e9c` | `80 81 de 3c` | ldur q0,[x12, #-0x18] | `FALL_THROUGH`
<a id="insn-00af7ea0"></a> `00af7ea0` | `4d 81 1f f8` | stur x13,[x10, #-0x8] | `FALL_THROUGH`
<a id="insn-00af7ea4"></a> `00af7ea4` | `40 81 9e 3c` | stur q0,[x10, #-0x18] | `FALL_THROUGH`
<a id="insn-00af7ea8"></a> `00af7ea8` | `9f 7d 3f a9` | stp xzr,xzr,[x12, #-0x10] | `FALL_THROUGH`
<a id="insn-00af7eac"></a> `00af7eac` | `9f 81 1e f8` | stur xzr,[x12, #-0x18] | `FALL_THROUGH`
<a id="insn-00af7eb0"></a> `00af7eb0` | `8c 61 00 d1` | sub x12,x12,#0x18 | `FALL_THROUGH`
<a id="insn-00af7eb4"></a> `00af7eb4` | `1f 01 0c eb` | cmp x8,x12 | `FALL_THROUGH`
<a id="insn-00af7eb8"></a> `00af7eb8` | `4a 61 00 d1` | sub x10,x10,#0x18 | `FALL_THROUGH`
<a id="insn-00af7ebc"></a> `00af7ebc` | `e1 fe ff 54` | b.ne 0x00af7e98 | `CONDITIONAL_JUMP`
<a id="insn-00af7ec0"></a> `00af7ec0` | `74 22 40 a9` | ldp x20,x8,[x19] | `FALL_THROUGH`
<a id="insn-00af7ec4"></a> `00af7ec4` | `02 00 00 14` | b 0x00af7ecc | `UNCONDITIONAL_JUMP`
<a id="insn-00af7ec8"></a> `00af7ec8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00af7ecc"></a> `00af7ecc` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00af7ed0"></a> `00af7ed0` | `6a 2e 00 a9` | stp x10,x11,[x19] | `FALL_THROUGH`
<a id="insn-00af7ed4"></a> `00af7ed4` | `69 0a 00 f9` | str x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00af7ed8"></a> `00af7ed8` | `80 01 00 54` | b.eq 0x00af7f08 | `CONDITIONAL_JUMP`
<a id="insn-00af7edc"></a> `00af7edc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00af7ee0"></a> `00af7ee0` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00af7ee4"></a> `00af7ee4` | `c9 00 00 37` | tbnz w9,#0x0,0x00af7efc | `CONDITIONAL_JUMP`
<a id="insn-00af7ee8"></a> `00af7ee8` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00af7eec"></a> `00af7eec` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00af7ef0"></a> `00af7ef0` | `c0 00 00 54` | b.eq 0x00af7f08 | `CONDITIONAL_JUMP`
<a id="insn-00af7ef4"></a> `00af7ef4` | `69 8e 5e 38` | ldrb w9,[x19, #-0x18]! | `FALL_THROUGH`
<a id="insn-00af7ef8"></a> `00af7ef8` | `89 ff 07 36` | tbz w9,#0x0,0x00af7ee8 | `CONDITIONAL_JUMP`
<a id="insn-00af7efc"></a> `00af7efc` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00af7f00"></a> `00af7f00` | `44 8c 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00af7f04"></a> `00af7f04` | `f9 ff ff 17` | b 0x00af7ee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00af7f08"></a> `00af7f08` | `d4 00 00 b4` | cbz x20,0x00af7f20 | `CONDITIONAL_JUMP`
<a id="insn-00af7f0c"></a> `00af7f0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af7f10"></a> `00af7f10` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7f14"></a> `00af7f14` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7f18"></a> `00af7f18` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af7f1c"></a> `00af7f1c` | `3d 8c 03 14` | b 0x00bdb010 | `CALL_TERMINATOR`
<a id="insn-00af7f20"></a> `00af7f20` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af7f24"></a> `00af7f24` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af7f28"></a> `00af7f28` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af7f2c"></a> `00af7f2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af7f30"></a> `00af7f30` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00af7f34"></a> `00af7f34` | `cb ff ff 17` | b 0x00af7e60 | `UNCONDITIONAL_JUMP`
<a id="insn-00af7f38"></a> `00af7f38` | `ce 98 03 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af7ddc`](#insn-00af7ddc) 範囲 `[['00af7ddc', '00af7df7']]`
  - `FALL_THROUGH` [`00af7df4`](#insn-00af7df4) → [`00af7df8`](#insn-00af7df8)
- ブロック [`00af7df8`](#insn-00af7df8) 範囲 `[['00af7df8', '00af7e17']]`
  - `CONDITIONAL_JUMP` [`00af7e14`](#insn-00af7e14) → [`00af7f38`](#insn-00af7f38)
  - `FALL_THROUGH` [`00af7e14`](#insn-00af7e14) → [`00af7e18`](#insn-00af7e18)
- ブロック [`00af7e18`](#insn-00af7e18) 範囲 `[['00af7e18', '00af7e43']]`
  - `CONDITIONAL_JUMP` [`00af7e40`](#insn-00af7e40) → [`00af7e54`](#insn-00af7e54)
  - `FALL_THROUGH` [`00af7e40`](#insn-00af7e40) → [`00af7e44`](#insn-00af7e44)
- ブロック [`00af7e44`](#insn-00af7e44) 範囲 `[['00af7e44', '00af7e53']]`
  - `CONDITIONAL_JUMP` [`00af7e50`](#insn-00af7e50) → [`00af7f30`](#insn-00af7f30)
  - `FALL_THROUGH` [`00af7e50`](#insn-00af7e50) → [`00af7e54`](#insn-00af7e54)
- ブロック [`00af7e54`](#insn-00af7e54) 範囲 `[['00af7e54', '00af7e5b']]`
  - `FALL_THROUGH` [`00af7e58`](#insn-00af7e58) → [`00af7e5c`](#insn-00af7e5c)
- ブロック [`00af7e5c`](#insn-00af7e5c) 範囲 `[['00af7e5c', '00af7e5f']]`
  - `FALL_THROUGH` [`00af7e5c`](#insn-00af7e5c) → [`00af7e60`](#insn-00af7e60)
- ブロック [`00af7e60`](#insn-00af7e60) 範囲 `[['00af7e60', '00af7e97']]`
  - `CONDITIONAL_JUMP` [`00af7e94`](#insn-00af7e94) → [`00af7ec8`](#insn-00af7ec8)
  - `FALL_THROUGH` [`00af7e94`](#insn-00af7e94) → [`00af7e98`](#insn-00af7e98)
- ブロック [`00af7e98`](#insn-00af7e98) 範囲 `[['00af7e98', '00af7e9f']]`
  - `FALL_THROUGH` [`00af7e9c`](#insn-00af7e9c) → [`00af7ea0`](#insn-00af7ea0)
- ブロック [`00af7ea0`](#insn-00af7ea0) 範囲 `[['00af7ea0', '00af7eaf']]`
  - `FALL_THROUGH` [`00af7eac`](#insn-00af7eac) → [`00af7eb0`](#insn-00af7eb0)
- ブロック [`00af7eb0`](#insn-00af7eb0) 範囲 `[['00af7eb0', '00af7ebf']]`
  - `CONDITIONAL_JUMP` [`00af7ebc`](#insn-00af7ebc) → [`00af7e98`](#insn-00af7e98)
  - `FALL_THROUGH` [`00af7ebc`](#insn-00af7ebc) → [`00af7ec0`](#insn-00af7ec0)
- ブロック [`00af7ec0`](#insn-00af7ec0) 範囲 `[['00af7ec0', '00af7ec7']]`
  - `UNCONDITIONAL_JUMP` [`00af7ec4`](#insn-00af7ec4) → [`00af7ecc`](#insn-00af7ecc)
- ブロック [`00af7ec8`](#insn-00af7ec8) 範囲 `[['00af7ec8', '00af7ecb']]`
  - `FALL_THROUGH` [`00af7ec8`](#insn-00af7ec8) → [`00af7ecc`](#insn-00af7ecc)
- ブロック [`00af7ecc`](#insn-00af7ecc) 範囲 `[['00af7ecc', '00af7ecf']]`
  - `FALL_THROUGH` [`00af7ecc`](#insn-00af7ecc) → [`00af7ed0`](#insn-00af7ed0)
- ブロック [`00af7ed0`](#insn-00af7ed0) 範囲 `[['00af7ed0', '00af7edb']]`
  - `CONDITIONAL_JUMP` [`00af7ed8`](#insn-00af7ed8) → [`00af7f08`](#insn-00af7f08)
  - `FALL_THROUGH` [`00af7ed8`](#insn-00af7ed8) → [`00af7edc`](#insn-00af7edc)
- ブロック [`00af7edc`](#insn-00af7edc) 範囲 `[['00af7edc', '00af7ee7']]`
  - `CONDITIONAL_JUMP` [`00af7ee4`](#insn-00af7ee4) → [`00af7efc`](#insn-00af7efc)
  - `FALL_THROUGH` [`00af7ee4`](#insn-00af7ee4) → [`00af7ee8`](#insn-00af7ee8)
- ブロック [`00af7ee8`](#insn-00af7ee8) 範囲 `[['00af7ee8', '00af7ef3']]`
  - `CONDITIONAL_JUMP` [`00af7ef0`](#insn-00af7ef0) → [`00af7f08`](#insn-00af7f08)
  - `FALL_THROUGH` [`00af7ef0`](#insn-00af7ef0) → [`00af7ef4`](#insn-00af7ef4)
- ブロック [`00af7ef4`](#insn-00af7ef4) 範囲 `[['00af7ef4', '00af7efb']]`
  - `CONDITIONAL_JUMP` [`00af7ef8`](#insn-00af7ef8) → [`00af7ee8`](#insn-00af7ee8)
  - `FALL_THROUGH` [`00af7ef8`](#insn-00af7ef8) → [`00af7efc`](#insn-00af7efc)
- ブロック [`00af7efc`](#insn-00af7efc) 範囲 `[['00af7efc', '00af7f07']]`
  - `UNCONDITIONAL_JUMP` [`00af7f04`](#insn-00af7f04) → [`00af7ee8`](#insn-00af7ee8)
- ブロック [`00af7f08`](#insn-00af7f08) 範囲 `[['00af7f08', '00af7f0b']]`
  - `CONDITIONAL_JUMP` [`00af7f08`](#insn-00af7f08) → [`00af7f20`](#insn-00af7f20)
  - `FALL_THROUGH` [`00af7f08`](#insn-00af7f08) → [`00af7f0c`](#insn-00af7f0c)
- ブロック [`00af7f0c`](#insn-00af7f0c) 範囲 `[['00af7f0c', '00af7f1f']]`
- ブロック [`00af7f20`](#insn-00af7f20) 範囲 `[['00af7f20', '00af7f23']]`
  - `FALL_THROUGH` [`00af7f20`](#insn-00af7f20) → [`00af7f24`](#insn-00af7f24)
- ブロック [`00af7f24`](#insn-00af7f24) 範囲 `[['00af7f24', '00af7f2f']]`
- ブロック [`00af7f30`](#insn-00af7f30) 範囲 `[['00af7f30', '00af7f33']]`
  - `FALL_THROUGH` [`00af7f30`](#insn-00af7f30) → [`00af7f34`](#insn-00af7f34)
- ブロック [`00af7f34`](#insn-00af7f34) 範囲 `[['00af7f34', '00af7f37']]`
  - `UNCONDITIONAL_JUMP` [`00af7f34`](#insn-00af7f34) → [`00af7e60`](#insn-00af7e60)
- ブロック [`00af7f38`](#insn-00af7f38) 範囲 `[['00af7f38', '00af7f3b']]`

## 命令位置別の参照

- [`00af7ddc`](#insn-00af7ddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7de0`](#insn-00af7de0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7de4`](#insn-00af7de4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e14`](#insn-00af7e14) → [`00af7f38`](#insn-00af7f38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e40`](#insn-00af7e40) → [`00af7e54`](#insn-00af7e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e50`](#insn-00af7e50) → [`00af7f30`](#insn-00af7f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7e5c`](#insn-00af7e5c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00af7e94`](#insn-00af7e94) → [`00af7ec8`](#insn-00af7ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ebc`](#insn-00af7ebc) → [`00af7e98`](#insn-00af7e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ec4`](#insn-00af7ec4) → [`00af7ecc`](#insn-00af7ecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ed8`](#insn-00af7ed8) → [`00af7f08`](#insn-00af7f08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ee4`](#insn-00af7ee4) → [`00af7efc`](#insn-00af7efc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ef0`](#insn-00af7ef0) → [`00af7f08`](#insn-00af7f08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7ef8`](#insn-00af7ef8) → [`00af7ee8`](#insn-00af7ee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f00`](#insn-00af7f00) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00af7f04`](#insn-00af7f04) → [`00af7ee8`](#insn-00af7ee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f08`](#insn-00af7f08) → [`00af7f20`](#insn-00af7f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f10`](#insn-00af7f10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f14`](#insn-00af7f14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f1c`](#insn-00af7f1c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00af7f20`](#insn-00af7f20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f24`](#insn-00af7f24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f34`](#insn-00af7f34) → [`00af7e60`](#insn-00af7e60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af7f38`](#insn-00af7f38) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af7ddc`](#insn-00af7ddc)

~~~json
{
  "source": "00af7ddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7de0`](#insn-00af7de0)

~~~json
{
  "source": "00af7de0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7de4`](#insn-00af7de4)

~~~json
{
  "source": "00af7de4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e14`](#insn-00af7e14)

~~~json
{
  "source": "00af7e14",
  "target": "00af7f38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e40`](#insn-00af7e40)

~~~json
{
  "source": "00af7e40",
  "target": "00af7e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e50`](#insn-00af7e50)

~~~json
{
  "source": "00af7e50",
  "target": "00af7f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7e5c`](#insn-00af7e5c)

~~~json
{
  "source": "00af7e5c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7e94`](#insn-00af7e94)

~~~json
{
  "source": "00af7e94",
  "target": "00af7ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ebc`](#insn-00af7ebc)

~~~json
{
  "source": "00af7ebc",
  "target": "00af7e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ec4`](#insn-00af7ec4)

~~~json
{
  "source": "00af7ec4",
  "target": "00af7ecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ed8`](#insn-00af7ed8)

~~~json
{
  "source": "00af7ed8",
  "target": "00af7f08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ee4`](#insn-00af7ee4)

~~~json
{
  "source": "00af7ee4",
  "target": "00af7efc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ef0`](#insn-00af7ef0)

~~~json
{
  "source": "00af7ef0",
  "target": "00af7f08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7ef8`](#insn-00af7ef8)

~~~json
{
  "source": "00af7ef8",
  "target": "00af7ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f00`](#insn-00af7f00)

~~~json
{
  "source": "00af7f00",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7f04`](#insn-00af7f04)

~~~json
{
  "source": "00af7f04",
  "target": "00af7ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f08`](#insn-00af7f08)

~~~json
{
  "source": "00af7f08",
  "target": "00af7f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f10`](#insn-00af7f10)

~~~json
{
  "source": "00af7f10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f14`](#insn-00af7f14)

~~~json
{
  "source": "00af7f14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f1c`](#insn-00af7f1c)

~~~json
{
  "source": "00af7f1c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af7f20`](#insn-00af7f20)

~~~json
{
  "source": "00af7f20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f24`](#insn-00af7f24)

~~~json
{
  "source": "00af7f24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f34`](#insn-00af7f34)

~~~json
{
  "source": "00af7f34",
  "target": "00af7e60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af7f38`](#insn-00af7f38)

~~~json
{
  "source": "00af7f38",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
