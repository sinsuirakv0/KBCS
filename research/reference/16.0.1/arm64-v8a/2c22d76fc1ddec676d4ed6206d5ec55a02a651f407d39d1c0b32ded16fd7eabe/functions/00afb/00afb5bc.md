# 00afb5bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afb194`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afb/00afb194.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-9f2e7735b7e196c2d14eb4fc16d3d37a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afb658`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afb/00afb658.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-91cedfab9d429fc2533c33a00ec7dde8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb5bc",
  "name": "FUN_00afb5bc",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2305d76a39a8c579edceddec0441b6d5c0e27ceadaa8ed17e74434a3df24dbbc",
  "source_text_sha256": "2305d76a39a8c579edceddec0441b6d5c0e27ceadaa8ed17e74434a3df24dbbc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb5bc",
        "00afb753"
      ]
    ],
    "bytes_sha256": "a65d062985595ac49428ce78d9eda8127c46236b23674147bf761182668cd75c",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005f3a70](../005f3/005f3a70.md)
- [005fb93c](../005fb/005fb93c.md)
- [00700af8](../00700/00700af8.md)
- [0070ea5c](../0070e/0070ea5c.md)
- [007119f0](../00711/007119f0.md)
- [00716d90](../00716/00716d90.md)

## 呼び出し先

- [005e0300](../005e0/005e0300.md)
- [005e08d8](../005e0/005e08d8.md)
- [005e0920](../005e0/005e0920.md)
- [005e09a0](../005e0/005e09a0.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2194 bytes

~~~c

void FUN_00afb5bc(int param_1,int param_2,int param_3)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  
  if (param_1 == 1) {
    uVar2 = FUN_005e08d8();
    if ((uVar2 & 1) == 0) {
                    /* try { // try from 00afb604 to 00bfb60f has its CatchHandler @ 00afc974 */
      if (param_2 != 0) goto LAB_00afb638;
    }
    else {
      iVar1 = FUN_005e0920();
      if (iVar1 != param_2) goto LAB_00afb638;
    }
    uVar2 = FUN_005e09a0();
    if ((uVar2 & 1) != 0) {
                    /* try { // try from 00afb614 to 00bfb62b has its CatchHandler @ 00afc970 */
      lVar3 = FUN_008514f8();
                    /* try { // try from 00afb62c to 00bfb68f has its CatchHandler @ 00afb44c */
      FUN_005e0300(lVar3 + 0x980,1);
      return;
    }
  }
LAB_00afb638:
  lVar3 = FUN_008514f8();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84914) = *(int *)(lVar3 + 0x84914) + param_3;
  lVar3 = FUN_008514f8();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84a88) = *(int *)(lVar3 + 0x84a88) + param_3;
  lVar3 = FUN_008514f8();
                    /* try { // try from 00afb690 to 00bfb69b has its CatchHandler @ 00afcb50 */
                    /* try { // try from 00afb69c to 00bfb6af has its CatchHandler @ 00afcb30 */
                    /* try { // try from 00afb6c8 to 00bfb6d7 has its CatchHandler @ 00afcb10 */
                    /* try { // try from 00afb6f0 to 00bfb707 has its CatchHandler @ 00afcad4 */
  if (((0 < *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad0)) &&
      (lVar3 = FUN_008514f8(),
      *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad0) < param_3)) &&
     (lVar3 = FUN_008514f8(),
     *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad4) == 0)) {
    lVar3 = FUN_008514f8();
                    /* try { // try from 00afb708 to 00bfb75f has its CatchHandler @ 00afb44c */
    *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad4) = 1;
  }
  lVar3 = FUN_008514f8();
  *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b50) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afb5bc"></a> `00afb5bc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afb5c0"></a> `00afb5c0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb5c4"></a> `00afb5c4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb5c8"></a> `00afb5c8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afb5cc"></a> `00afb5cc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afb5d0"></a> `00afb5d0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afb5d4"></a> `00afb5d4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afb5d8"></a> `00afb5d8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afb5dc"></a> `00afb5dc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afb5e0"></a> `00afb5e0` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00afb5e4"></a> `00afb5e4` | `a1 02 00 54` | b.ne 0x00afb638 | `CONDITIONAL_JUMP`
<a id="insn-00afb5e8"></a> `00afb5e8` | `bc 94 eb 97` | bl 0x005e08d8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb5ec"></a> `00afb5ec` | `a0 00 00 36` | tbz w0,#0x0,0x00afb600 | `CONDITIONAL_JUMP`
<a id="insn-00afb5f0"></a> `00afb5f0` | `cc 94 eb 97` | bl 0x005e0920 | `UNCONDITIONAL_CALL`
<a id="insn-00afb5f4"></a> `00afb5f4` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00afb5f8"></a> `00afb5f8` | `a0 00 00 54` | b.eq 0x00afb60c | `CONDITIONAL_JUMP`
<a id="insn-00afb5fc"></a> `00afb5fc` | `0f 00 00 14` | b 0x00afb638 | `UNCONDITIONAL_JUMP`
<a id="insn-00afb600"></a> `00afb600` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afb604"></a> `00afb604` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00afb608"></a> `00afb608` | `81 01 00 54` | b.ne 0x00afb638 | `CONDITIONAL_JUMP`
<a id="insn-00afb60c"></a> `00afb60c` | `e5 94 eb 97` | bl 0x005e09a0 | `UNCONDITIONAL_CALL`
<a id="insn-00afb610"></a> `00afb610` | `40 01 00 36` | tbz w0,#0x0,0x00afb638 | `CONDITIONAL_JUMP`
<a id="insn-00afb614"></a> `00afb614` | `b9 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb618"></a> `00afb618` | `00 00 26 91` | add x0,x0,#0x980 | `FALL_THROUGH`
<a id="insn-00afb61c"></a> `00afb61c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afb620"></a> `00afb620` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afb624"></a> `00afb624` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb628"></a> `00afb628` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afb62c"></a> `00afb62c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb630"></a> `00afb630` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afb634"></a> `00afb634` | `33 93 eb 17` | b 0x005e0300 | `CALL_TERMINATOR`
<a id="insn-00afb638"></a> `00afb638` | `b0 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb63c"></a> `00afb63c` | `98 00 99 52` | mov w24,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb640"></a> `00afb640` | `99 7d 80 52` | mov w25,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb644"></a> `00afb644` | `89 22 89 52` | mov w9,#0x4914 | `FALL_THROUGH`
<a id="insn-00afb648"></a> `00afb648` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00afb64c"></a> `00afb64c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb650"></a> `00afb650` | `97 7e 40 93` | sxtw x23,w20 | `FALL_THROUGH`
<a id="insn-00afb654"></a> `00afb654` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00afb658"></a> `00afb658` | `b6 7e 40 93` | sxtw x22,w21 | `FALL_THROUGH`
<a id="insn-00afb65c"></a> `00afb65c` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb660"></a> `00afb660` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afb664"></a> `00afb664` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb668"></a> `00afb668` | `a4 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb66c"></a> `00afb66c` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00afb670"></a> `00afb670` | `09 51 89 52` | mov w9,#0x4a88 | `FALL_THROUGH`
<a id="insn-00afb674"></a> `00afb674` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00afb678"></a> `00afb678` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb67c"></a> `00afb67c` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb680"></a> `00afb680` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00afb684"></a> `00afb684` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb688"></a> `00afb688` | `9c 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb68c"></a> `00afb68c` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00afb690"></a> `00afb690` | `09 5a 89 52` | mov w9,#0x4ad0 | `FALL_THROUGH`
<a id="insn-00afb694"></a> `00afb694` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00afb698"></a> `00afb698` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb69c"></a> `00afb69c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb6a0"></a> `00afb6a0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afb6a4"></a> `00afb6a4` | `ab 03 00 54` | b.lt 0x00afb718 | `CONDITIONAL_JUMP`
<a id="insn-00afb6a8"></a> `00afb6a8` | `94 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb6ac"></a> `00afb6ac` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb6b0"></a> `00afb6b0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb6b4"></a> `00afb6b4` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb6b8"></a> `00afb6b8` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb6bc"></a> `00afb6bc` | `09 5a 89 52` | mov w9,#0x4ad0 | `FALL_THROUGH`
<a id="insn-00afb6c0"></a> `00afb6c0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb6c4"></a> `00afb6c4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb6c8"></a> `00afb6c8` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afb6cc"></a> `00afb6cc` | `6a 02 00 54` | b.ge 0x00afb718 | `CONDITIONAL_JUMP`
<a id="insn-00afb6d0"></a> `00afb6d0` | `8a 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb6d4"></a> `00afb6d4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb6d8"></a> `00afb6d8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb6dc"></a> `00afb6dc` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb6e0"></a> `00afb6e0` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb6e4"></a> `00afb6e4` | `89 5a 89 52` | mov w9,#0x4ad4 | `FALL_THROUGH`
<a id="insn-00afb6e8"></a> `00afb6e8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb6ec"></a> `00afb6ec` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb6f0"></a> `00afb6f0` | `48 01 00 35` | cbnz w8,0x00afb718 | `CONDITIONAL_JUMP`
<a id="insn-00afb6f4"></a> `00afb6f4` | `81 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb6f8"></a> `00afb6f8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb6fc"></a> `00afb6fc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb700"></a> `00afb700` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afb704"></a> `00afb704` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb708"></a> `00afb708` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb70c"></a> `00afb70c` | `89 5a 89 52` | mov w9,#0x4ad4 | `FALL_THROUGH`
<a id="insn-00afb710"></a> `00afb710` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb714"></a> `00afb714` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb718"></a> `00afb718` | `78 57 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afb71c"></a> `00afb71c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afb720"></a> `00afb720` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afb724"></a> `00afb724` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afb728"></a> `00afb728` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00afb72c"></a> `00afb72c` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00afb730"></a> `00afb730` | `09 6a 89 52` | mov w9,#0x4b50 | `FALL_THROUGH`
<a id="insn-00afb734"></a> `00afb734` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afb738"></a> `00afb738` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afb73c"></a> `00afb73c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afb740"></a> `00afb740` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afb744"></a> `00afb744` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afb748"></a> `00afb748` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb74c"></a> `00afb74c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afb750"></a> `00afb750` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb5bc`](#insn-00afb5bc) 範囲 `[['00afb5bc', '00afb5e7']]`
  - `CONDITIONAL_JUMP` [`00afb5e4`](#insn-00afb5e4) → [`00afb638`](#insn-00afb638)
  - `FALL_THROUGH` [`00afb5e4`](#insn-00afb5e4) → [`00afb5e8`](#insn-00afb5e8)
- ブロック [`00afb5e8`](#insn-00afb5e8) 範囲 `[['00afb5e8', '00afb5ef']]`
  - `CONDITIONAL_JUMP` [`00afb5ec`](#insn-00afb5ec) → [`00afb600`](#insn-00afb600)
  - `FALL_THROUGH` [`00afb5ec`](#insn-00afb5ec) → [`00afb5f0`](#insn-00afb5f0)
- ブロック [`00afb5f0`](#insn-00afb5f0) 範囲 `[['00afb5f0', '00afb5fb']]`
  - `CONDITIONAL_JUMP` [`00afb5f8`](#insn-00afb5f8) → [`00afb60c`](#insn-00afb60c)
  - `FALL_THROUGH` [`00afb5f8`](#insn-00afb5f8) → [`00afb5fc`](#insn-00afb5fc)
- ブロック [`00afb5fc`](#insn-00afb5fc) 範囲 `[['00afb5fc', '00afb5ff']]`
  - `UNCONDITIONAL_JUMP` [`00afb5fc`](#insn-00afb5fc) → [`00afb638`](#insn-00afb638)
- ブロック [`00afb600`](#insn-00afb600) 範囲 `[['00afb600', '00afb603']]`
  - `FALL_THROUGH` [`00afb600`](#insn-00afb600) → [`00afb604`](#insn-00afb604)
- ブロック [`00afb604`](#insn-00afb604) 範囲 `[['00afb604', '00afb60b']]`
  - `CONDITIONAL_JUMP` [`00afb608`](#insn-00afb608) → [`00afb638`](#insn-00afb638)
  - `FALL_THROUGH` [`00afb608`](#insn-00afb608) → [`00afb60c`](#insn-00afb60c)
- ブロック [`00afb60c`](#insn-00afb60c) 範囲 `[['00afb60c', '00afb613']]`
  - `CONDITIONAL_JUMP` [`00afb610`](#insn-00afb610) → [`00afb638`](#insn-00afb638)
  - `FALL_THROUGH` [`00afb610`](#insn-00afb610) → [`00afb614`](#insn-00afb614)
- ブロック [`00afb614`](#insn-00afb614) 範囲 `[['00afb614', '00afb62b']]`
  - `FALL_THROUGH` [`00afb628`](#insn-00afb628) → [`00afb62c`](#insn-00afb62c)
- ブロック [`00afb62c`](#insn-00afb62c) 範囲 `[['00afb62c', '00afb637']]`
- ブロック [`00afb638`](#insn-00afb638) 範囲 `[['00afb638', '00afb68f']]`
  - `FALL_THROUGH` [`00afb68c`](#insn-00afb68c) → [`00afb690`](#insn-00afb690)
- ブロック [`00afb690`](#insn-00afb690) 範囲 `[['00afb690', '00afb69b']]`
  - `FALL_THROUGH` [`00afb698`](#insn-00afb698) → [`00afb69c`](#insn-00afb69c)
- ブロック [`00afb69c`](#insn-00afb69c) 範囲 `[['00afb69c', '00afb6a7']]`
  - `CONDITIONAL_JUMP` [`00afb6a4`](#insn-00afb6a4) → [`00afb718`](#insn-00afb718)
  - `FALL_THROUGH` [`00afb6a4`](#insn-00afb6a4) → [`00afb6a8`](#insn-00afb6a8)
- ブロック [`00afb6a8`](#insn-00afb6a8) 範囲 `[['00afb6a8', '00afb6c7']]`
  - `FALL_THROUGH` [`00afb6c4`](#insn-00afb6c4) → [`00afb6c8`](#insn-00afb6c8)
- ブロック [`00afb6c8`](#insn-00afb6c8) 範囲 `[['00afb6c8', '00afb6cf']]`
  - `CONDITIONAL_JUMP` [`00afb6cc`](#insn-00afb6cc) → [`00afb718`](#insn-00afb718)
  - `FALL_THROUGH` [`00afb6cc`](#insn-00afb6cc) → [`00afb6d0`](#insn-00afb6d0)
- ブロック [`00afb6d0`](#insn-00afb6d0) 範囲 `[['00afb6d0', '00afb6ef']]`
  - `FALL_THROUGH` [`00afb6ec`](#insn-00afb6ec) → [`00afb6f0`](#insn-00afb6f0)
- ブロック [`00afb6f0`](#insn-00afb6f0) 範囲 `[['00afb6f0', '00afb6f3']]`
  - `CONDITIONAL_JUMP` [`00afb6f0`](#insn-00afb6f0) → [`00afb718`](#insn-00afb718)
  - `FALL_THROUGH` [`00afb6f0`](#insn-00afb6f0) → [`00afb6f4`](#insn-00afb6f4)
- ブロック [`00afb6f4`](#insn-00afb6f4) 範囲 `[['00afb6f4', '00afb707']]`
  - `FALL_THROUGH` [`00afb704`](#insn-00afb704) → [`00afb708`](#insn-00afb708)
- ブロック [`00afb708`](#insn-00afb708) 範囲 `[['00afb708', '00afb717']]`
  - `FALL_THROUGH` [`00afb714`](#insn-00afb714) → [`00afb718`](#insn-00afb718)
- ブロック [`00afb718`](#insn-00afb718) 範囲 `[['00afb718', '00afb753']]`

## 命令位置別の参照

- [`00afb5bc`](#insn-00afb5bc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5c0`](#insn-00afb5c0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5c4`](#insn-00afb5c4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5c8`](#insn-00afb5c8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5cc`](#insn-00afb5cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5e4`](#insn-00afb5e4) → [`00afb638`](#insn-00afb638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5e8`](#insn-00afb5e8) → [`005e08d8`](../005e0/005e08d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e08d8` · 推定シンボル `None` · 推定型 `None`
- [`00afb5ec`](#insn-00afb5ec) → [`00afb600`](#insn-00afb600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5f0`](#insn-00afb5f0) → [`005e0920`](../005e0/005e0920.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0920` · 推定シンボル `None` · 推定型 `None`
- [`00afb5f8`](#insn-00afb5f8) → [`00afb60c`](#insn-00afb60c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb5fc`](#insn-00afb5fc) → [`00afb638`](#insn-00afb638) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb608`](#insn-00afb608) → [`00afb638`](#insn-00afb638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb60c`](#insn-00afb60c) → [`005e09a0`](../005e0/005e09a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e09a0` · 推定シンボル `None` · 推定型 `None`
- [`00afb610`](#insn-00afb610) → [`00afb638`](#insn-00afb638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb614`](#insn-00afb614) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb620`](#insn-00afb620) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb624`](#insn-00afb624) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb628`](#insn-00afb628) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb62c`](#insn-00afb62c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb630`](#insn-00afb630) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb634`](#insn-00afb634) → [`005e0300`](../005e0/005e0300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0300` · 推定シンボル `None` · 推定型 `None`
- [`00afb638`](#insn-00afb638) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb668`](#insn-00afb668) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb688`](#insn-00afb688) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb6a4`](#insn-00afb6a4) → [`00afb718`](#insn-00afb718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6a8`](#insn-00afb6a8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb6cc`](#insn-00afb6cc) → [`00afb718`](#insn-00afb718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6d0`](#insn-00afb6d0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb6f0`](#insn-00afb6f0) → [`00afb718`](#insn-00afb718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb6f4`](#insn-00afb6f4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb718`](#insn-00afb718) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afb73c`](#insn-00afb73c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb740`](#insn-00afb740) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb744`](#insn-00afb744) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb748`](#insn-00afb748) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb74c`](#insn-00afb74c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb5bc`](#insn-00afb5bc)

~~~json
{
  "source": "00afb5bc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5c0`](#insn-00afb5c0)

~~~json
{
  "source": "00afb5c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5c4`](#insn-00afb5c4)

~~~json
{
  "source": "00afb5c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5c8`](#insn-00afb5c8)

~~~json
{
  "source": "00afb5c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5cc`](#insn-00afb5cc)

~~~json
{
  "source": "00afb5cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5e4`](#insn-00afb5e4)

~~~json
{
  "source": "00afb5e4",
  "target": "00afb638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5e8`](#insn-00afb5e8)

~~~json
{
  "source": "00afb5e8",
  "target": "005e08d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb5ec`](#insn-00afb5ec)

~~~json
{
  "source": "00afb5ec",
  "target": "00afb600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5f0`](#insn-00afb5f0)

~~~json
{
  "source": "00afb5f0",
  "target": "005e0920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb5f8`](#insn-00afb5f8)

~~~json
{
  "source": "00afb5f8",
  "target": "00afb60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb5fc`](#insn-00afb5fc)

~~~json
{
  "source": "00afb5fc",
  "target": "00afb638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb608`](#insn-00afb608)

~~~json
{
  "source": "00afb608",
  "target": "00afb638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb60c`](#insn-00afb60c)

~~~json
{
  "source": "00afb60c",
  "target": "005e09a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb610`](#insn-00afb610)

~~~json
{
  "source": "00afb610",
  "target": "00afb638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb614`](#insn-00afb614)

~~~json
{
  "source": "00afb614",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb620`](#insn-00afb620)

~~~json
{
  "source": "00afb620",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb624`](#insn-00afb624)

~~~json
{
  "source": "00afb624",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb628`](#insn-00afb628)

~~~json
{
  "source": "00afb628",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb62c`](#insn-00afb62c)

~~~json
{
  "source": "00afb62c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb630`](#insn-00afb630)

~~~json
{
  "source": "00afb630",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb634`](#insn-00afb634)

~~~json
{
  "source": "00afb634",
  "target": "005e0300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb638`](#insn-00afb638)

~~~json
{
  "source": "00afb638",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb668`](#insn-00afb668)

~~~json
{
  "source": "00afb668",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb688`](#insn-00afb688)

~~~json
{
  "source": "00afb688",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb6a4`](#insn-00afb6a4)

~~~json
{
  "source": "00afb6a4",
  "target": "00afb718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6a8`](#insn-00afb6a8)

~~~json
{
  "source": "00afb6a8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb6cc`](#insn-00afb6cc)

~~~json
{
  "source": "00afb6cc",
  "target": "00afb718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6d0`](#insn-00afb6d0)

~~~json
{
  "source": "00afb6d0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb6f0`](#insn-00afb6f0)

~~~json
{
  "source": "00afb6f0",
  "target": "00afb718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb6f4`](#insn-00afb6f4)

~~~json
{
  "source": "00afb6f4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb718`](#insn-00afb718)

~~~json
{
  "source": "00afb718",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afb73c`](#insn-00afb73c)

~~~json
{
  "source": "00afb73c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb740`](#insn-00afb740)

~~~json
{
  "source": "00afb740",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb744`](#insn-00afb744)

~~~json
{
  "source": "00afb744",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb748`](#insn-00afb748)

~~~json
{
  "source": "00afb748",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb74c`](#insn-00afb74c)

~~~json
{
  "source": "00afb74c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
