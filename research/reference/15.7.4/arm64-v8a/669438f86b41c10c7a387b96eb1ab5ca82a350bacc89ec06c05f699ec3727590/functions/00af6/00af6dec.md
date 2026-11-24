# 00af6dec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af6da8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-5f0907476e0f066f39ee859ae3e8f3b3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b56b70`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b56/00b56b70.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-8aeaa2cea8c4858b36d707c558914771)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af6dec",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c36baa881dffca3c1b89128b5208207d18c87e327d9850b41ad67d5fcfdc0750",
  "source_text_sha256": "c36baa881dffca3c1b89128b5208207d18c87e327d9850b41ad67d5fcfdc0750",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af6dec",
        "00af6f1b"
      ]
    ],
    "bytes_sha256": "864e6bb9e78e57d091dd13c2b4bb8fa581a5b01acf240f15ea790fbb257b8a65",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde7f0](../00bde/00bde7f0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdda90](../00bdd/00bdda90.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2173 bytes

~~~c

void _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_
               (ulong *param_1,byte *param_2,undefined1 param_3)

{
  size_t __n;
  byte *__src;
  bool bVar1;
  ulong uVar2;
  byte bVar3;
  ulong uVar4;
  void *__dest;
  
                    /* try { // try from 00af6e00 to 00bf6e0b has its CatchHandler @ 00afefe8 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00af6e0c to 00bf6e27 has its CatchHandler @ 00afef6c */
  __src = *(byte **)(param_2 + 0x10);
  bVar1 = (*param_2 & 1) != 0;
  __n = (ulong)(*param_2 >> 1);
  if (bVar1) {
    __n = *(size_t *)(param_2 + 8);
  }
  if (!bVar1) {
    __src = param_2 + 1;
  }
                    /* try { // try from 00af6e28 to 00bf6eef has its CatchHandler @ 00af5650 */
  if (0xffffffffffffffef < __n + 1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  if (__n + 1 < 0x17) {
    __dest = (void *)((long)param_1 + 1);
    *(char *)param_1 = (char)((int)__n << 1);
    if (__n != 0) goto LAB_00af6e70;
  }
  else {
    uVar4 = __n + 0x11 & 0xfffffffffffffff0;
    __dest = (void *)_Znwm(uVar4);
    param_1[1] = __n;
    param_1[2] = (ulong)__dest;
    *param_1 = uVar4 | 1;
LAB_00af6e70:
    memcpy(__dest,__src,__n);
  }
  *(undefined1 *)((long)__dest + __n) = 0;
  bVar3 = (byte)*param_1;
  if ((bVar3 & 1) == 0) {
    uVar4 = (ulong)(bVar3 >> 1);
    uVar2 = 0x16;
    if (uVar4 != 0x16) goto LAB_00af6ed4;
  }
  else {
    uVar4 = param_1[1];
    uVar2 = (*param_1 & 0xfffffffffffffffe) - 1;
    if (uVar4 != uVar2) goto LAB_00af6ed4;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
            (param_1,uVar2,1,uVar2,uVar2,0,0);
  bVar3 = (byte)*param_1;
LAB_00af6ed4:
  if ((bVar3 & 1) == 0) {
                    /* try { // try from 00af6ef0 to 00bf6f07 has its CatchHandler @ 00b003c0 */
    uVar2 = (long)param_1 + 1;
    *(char *)param_1 = (char)uVar4 * '\x02' + '\x02';
  }
  else {
    uVar2 = param_1[2];
    param_1[1] = uVar4 + 1;
  }
  *(undefined1 *)(uVar2 + uVar4) = param_3;
  ((undefined1 *)(uVar2 + uVar4))[1] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af6dec"></a> `00af6dec` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00af6df0"></a> `00af6df0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6df4"></a> `00af6df4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af6df8"></a> `00af6df8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af6dfc"></a> `00af6dfc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00af6e00"></a> `00af6e00` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00af6e04"></a> `00af6e04` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af6e08"></a> `00af6e08` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00af6e0c"></a> `00af6e0c` | `08 00 40 39` | ldrb w8,[x0] | `FALL_THROUGH`
<a id="insn-00af6e10"></a> `00af6e10` | `09 a8 40 a9` | ldp x9,x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af6e14"></a> `00af6e14` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e18"></a> `00af6e18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e1c"></a> `00af6e1c` | `75 01 89 9a` | csel x21,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00af6e20"></a> `00af6e20` | `a8 06 00 91` | add x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e24"></a> `00af6e24` | `56 15 80 9a` | csinc x22,x10,x0,ne | `FALL_THROUGH`
<a id="insn-00af6e28"></a> `00af6e28` | `1f 41 00 b1` | cmn x8,#0x10 | `FALL_THROUGH`
<a id="insn-00af6e2c"></a> `00af6e2c` | `62 07 00 54` | b.cs 0x00af6f18 | `CONDITIONAL_JUMP`
<a id="insn-00af6e30"></a> `00af6e30` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af6e34"></a> `00af6e34` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00af6e38"></a> `00af6e38` | `c2 00 00 54` | b.cs 0x00af6e50 | `CONDITIONAL_JUMP`
<a id="insn-00af6e3c"></a> `00af6e3c` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e40"></a> `00af6e40` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00af6e44"></a> `00af6e44` | `e8 16 00 38` | strb w8,[x23], #0x1 | `FALL_THROUGH`
<a id="insn-00af6e48"></a> `00af6e48` | `55 01 00 b5` | cbnz x21,0x00af6e70 | `CONDITIONAL_JUMP`
<a id="insn-00af6e4c"></a> `00af6e4c` | `0d 00 00 14` | b 0x00af6e80 | `UNCONDITIONAL_JUMP`
<a id="insn-00af6e50"></a> `00af6e50` | `a8 46 00 91` | add x8,x21,#0x11 | `FALL_THROUGH`
<a id="insn-00af6e54"></a> `00af6e54` | `18 ed 7c 92` | and x24,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00af6e58"></a> `00af6e58` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00af6e5c"></a> `00af6e5c` | `79 90 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00af6e60"></a> `00af6e60` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e64"></a> `00af6e64` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00af6e68"></a> `00af6e68` | `75 82 00 a9` | stp x21,x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af6e6c"></a> `00af6e6c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00af6e70"></a> `00af6e70` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00af6e74"></a> `00af6e74` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00af6e78"></a> `00af6e78` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00af6e7c"></a> `00af6e7c` | `cd 90 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00af6e80"></a> `00af6e80` | `ff 6a 35 38` | strb wzr,[x23, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00af6e84"></a> `00af6e84` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00af6e88"></a> `00af6e88` | `e8 00 00 36` | tbz w8,#0x0,0x00af6ea4 | `CONDITIONAL_JUMP`
<a id="insn-00af6e8c"></a> `00af6e8c` | `69 56 40 a9` | ldp x9,x21,[x19] | `FALL_THROUGH`
<a id="insn-00af6e90"></a> `00af6e90` | `29 f9 7f 92` | and x9,x9,#-0x2 | `FALL_THROUGH`
<a id="insn-00af6e94"></a> `00af6e94` | `21 05 00 d1` | sub x1,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00af6e98"></a> `00af6e98` | `bf 02 01 eb` | cmp x21,x1 | `FALL_THROUGH`
<a id="insn-00af6e9c"></a> `00af6e9c` | `c0 00 00 54` | b.eq 0x00af6eb4 | `CONDITIONAL_JUMP`
<a id="insn-00af6ea0"></a> `00af6ea0` | `0d 00 00 14` | b 0x00af6ed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00af6ea4"></a> `00af6ea4` | `15 fd 41 d3` | lsr x21,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00af6ea8"></a> `00af6ea8` | `c1 02 80 52` | mov w1,#0x16 | `FALL_THROUGH`
<a id="insn-00af6eac"></a> `00af6eac` | `bf 02 01 eb` | cmp x21,x1 | `FALL_THROUGH`
<a id="insn-00af6eb0"></a> `00af6eb0` | `21 01 00 54` | b.ne 0x00af6ed4 | `CONDITIONAL_JUMP`
<a id="insn-00af6eb4"></a> `00af6eb4` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00af6eb8"></a> `00af6eb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af6ebc"></a> `00af6ebc` | `e3 03 01 aa` | mov x3,x1 | `FALL_THROUGH`
<a id="insn-00af6ec0"></a> `00af6ec0` | `e4 03 01 aa` | mov x4,x1 | `FALL_THROUGH`
<a id="insn-00af6ec4"></a> `00af6ec4` | `e5 03 1f aa` | mov x5,xzr | `FALL_THROUGH`
<a id="insn-00af6ec8"></a> `00af6ec8` | `e6 03 1f aa` | mov x6,xzr | `FALL_THROUGH`
<a id="insn-00af6ecc"></a> `00af6ecc` | `f1 9a 03 94` | bl 0x00bdda90 | `UNCONDITIONAL_CALL`
<a id="insn-00af6ed0"></a> `00af6ed0` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00af6ed4"></a> `00af6ed4` | `c8 00 00 36` | tbz w8,#0x0,0x00af6eec | `CONDITIONAL_JUMP`
<a id="insn-00af6ed8"></a> `00af6ed8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00af6edc"></a> `00af6edc` | `a9 06 00 91` | add x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00af6ee0"></a> `00af6ee0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00af6ee4"></a> `00af6ee4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00af6ee8"></a> `00af6ee8` | `04 00 00 14` | b 0x00af6ef8 | `UNCONDITIONAL_JUMP`
<a id="insn-00af6eec"></a> `00af6eec` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00af6ef0"></a> `00af6ef0` | `08 09 00 11` | add w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00af6ef4"></a> `00af6ef4` | `68 16 00 38` | strb w8,[x19], #0x1 | `FALL_THROUGH`
<a id="insn-00af6ef8"></a> `00af6ef8` | `68 02 15 8b` | add x8,x19,x21 | `FALL_THROUGH`
<a id="insn-00af6efc"></a> `00af6efc` | `14 01 00 39` | strb w20,[x8] | `FALL_THROUGH`
<a id="insn-00af6f00"></a> `00af6f00` | `1f 05 00 39` | strb wzr,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00af6f04"></a> `00af6f04` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af6f08"></a> `00af6f08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af6f0c"></a> `00af6f0c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af6f10"></a> `00af6f10` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00af6f14"></a> `00af6f14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af6f18"></a> `00af6f18` | `ea 9c 03 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af6dec`](#insn-00af6dec) 範囲 `[['00af6dec', '00af6dff']]`
  - `FALL_THROUGH` [`00af6dfc`](#insn-00af6dfc) → [`00af6e00`](#insn-00af6e00)
- ブロック [`00af6e00`](#insn-00af6e00) 範囲 `[['00af6e00', '00af6e0b']]`
  - `FALL_THROUGH` [`00af6e08`](#insn-00af6e08) → [`00af6e0c`](#insn-00af6e0c)
- ブロック [`00af6e0c`](#insn-00af6e0c) 範囲 `[['00af6e0c', '00af6e27']]`
  - `FALL_THROUGH` [`00af6e24`](#insn-00af6e24) → [`00af6e28`](#insn-00af6e28)
- ブロック [`00af6e28`](#insn-00af6e28) 範囲 `[['00af6e28', '00af6e2f']]`
  - `CONDITIONAL_JUMP` [`00af6e2c`](#insn-00af6e2c) → [`00af6f18`](#insn-00af6f18)
  - `FALL_THROUGH` [`00af6e2c`](#insn-00af6e2c) → [`00af6e30`](#insn-00af6e30)
- ブロック [`00af6e30`](#insn-00af6e30) 範囲 `[['00af6e30', '00af6e3b']]`
  - `CONDITIONAL_JUMP` [`00af6e38`](#insn-00af6e38) → [`00af6e50`](#insn-00af6e50)
  - `FALL_THROUGH` [`00af6e38`](#insn-00af6e38) → [`00af6e3c`](#insn-00af6e3c)
- ブロック [`00af6e3c`](#insn-00af6e3c) 範囲 `[['00af6e3c', '00af6e4b']]`
  - `CONDITIONAL_JUMP` [`00af6e48`](#insn-00af6e48) → [`00af6e70`](#insn-00af6e70)
  - `FALL_THROUGH` [`00af6e48`](#insn-00af6e48) → [`00af6e4c`](#insn-00af6e4c)
- ブロック [`00af6e4c`](#insn-00af6e4c) 範囲 `[['00af6e4c', '00af6e4f']]`
  - `UNCONDITIONAL_JUMP` [`00af6e4c`](#insn-00af6e4c) → [`00af6e80`](#insn-00af6e80)
- ブロック [`00af6e50`](#insn-00af6e50) 範囲 `[['00af6e50', '00af6e6f']]`
  - `FALL_THROUGH` [`00af6e6c`](#insn-00af6e6c) → [`00af6e70`](#insn-00af6e70)
- ブロック [`00af6e70`](#insn-00af6e70) 範囲 `[['00af6e70', '00af6e7f']]`
  - `FALL_THROUGH` [`00af6e7c`](#insn-00af6e7c) → [`00af6e80`](#insn-00af6e80)
- ブロック [`00af6e80`](#insn-00af6e80) 範囲 `[['00af6e80', '00af6e8b']]`
  - `CONDITIONAL_JUMP` [`00af6e88`](#insn-00af6e88) → [`00af6ea4`](#insn-00af6ea4)
  - `FALL_THROUGH` [`00af6e88`](#insn-00af6e88) → [`00af6e8c`](#insn-00af6e8c)
- ブロック [`00af6e8c`](#insn-00af6e8c) 範囲 `[['00af6e8c', '00af6e9f']]`
  - `CONDITIONAL_JUMP` [`00af6e9c`](#insn-00af6e9c) → [`00af6eb4`](#insn-00af6eb4)
  - `FALL_THROUGH` [`00af6e9c`](#insn-00af6e9c) → [`00af6ea0`](#insn-00af6ea0)
- ブロック [`00af6ea0`](#insn-00af6ea0) 範囲 `[['00af6ea0', '00af6ea3']]`
  - `UNCONDITIONAL_JUMP` [`00af6ea0`](#insn-00af6ea0) → [`00af6ed4`](#insn-00af6ed4)
- ブロック [`00af6ea4`](#insn-00af6ea4) 範囲 `[['00af6ea4', '00af6eb3']]`
  - `CONDITIONAL_JUMP` [`00af6eb0`](#insn-00af6eb0) → [`00af6ed4`](#insn-00af6ed4)
  - `FALL_THROUGH` [`00af6eb0`](#insn-00af6eb0) → [`00af6eb4`](#insn-00af6eb4)
- ブロック [`00af6eb4`](#insn-00af6eb4) 範囲 `[['00af6eb4', '00af6ed3']]`
  - `FALL_THROUGH` [`00af6ed0`](#insn-00af6ed0) → [`00af6ed4`](#insn-00af6ed4)
- ブロック [`00af6ed4`](#insn-00af6ed4) 範囲 `[['00af6ed4', '00af6ed7']]`
  - `CONDITIONAL_JUMP` [`00af6ed4`](#insn-00af6ed4) → [`00af6eec`](#insn-00af6eec)
  - `FALL_THROUGH` [`00af6ed4`](#insn-00af6ed4) → [`00af6ed8`](#insn-00af6ed8)
- ブロック [`00af6ed8`](#insn-00af6ed8) 範囲 `[['00af6ed8', '00af6eeb']]`
  - `UNCONDITIONAL_JUMP` [`00af6ee8`](#insn-00af6ee8) → [`00af6ef8`](#insn-00af6ef8)
- ブロック [`00af6eec`](#insn-00af6eec) 範囲 `[['00af6eec', '00af6eef']]`
  - `FALL_THROUGH` [`00af6eec`](#insn-00af6eec) → [`00af6ef0`](#insn-00af6ef0)
- ブロック [`00af6ef0`](#insn-00af6ef0) 範囲 `[['00af6ef0', '00af6ef7']]`
  - `FALL_THROUGH` [`00af6ef4`](#insn-00af6ef4) → [`00af6ef8`](#insn-00af6ef8)
- ブロック [`00af6ef8`](#insn-00af6ef8) 範囲 `[['00af6ef8', '00af6f17']]`
- ブロック [`00af6f18`](#insn-00af6f18) 範囲 `[['00af6f18', '00af6f1b']]`

## 命令位置別の参照

- [`00af6dec`](#insn-00af6dec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6df0`](#insn-00af6df0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6df4`](#insn-00af6df4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6df8`](#insn-00af6df8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e2c`](#insn-00af6e2c) → [`00af6f18`](#insn-00af6f18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e38`](#insn-00af6e38) → [`00af6e50`](#insn-00af6e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e48`](#insn-00af6e48) → [`00af6e70`](#insn-00af6e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e4c`](#insn-00af6e4c) → [`00af6e80`](#insn-00af6e80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e5c`](#insn-00af6e5c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00af6e7c`](#insn-00af6e7c) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00af6e88`](#insn-00af6e88) → [`00af6ea4`](#insn-00af6ea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6e9c`](#insn-00af6e9c) → [`00af6eb4`](#insn-00af6eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6ea0`](#insn-00af6ea0) → [`00af6ed4`](#insn-00af6ed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6eb0`](#insn-00af6eb0) → [`00af6ed4`](#insn-00af6ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6ecc`](#insn-00af6ecc) → [`00bdda90`](../00bdd/00bdda90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdda90` · 推定シンボル `None` · 推定型 `None`
- [`00af6ed4`](#insn-00af6ed4) → [`00af6eec`](#insn-00af6eec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6ee8`](#insn-00af6ee8) → [`00af6ef8`](#insn-00af6ef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6f04`](#insn-00af6f04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6f08`](#insn-00af6f08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6f0c`](#insn-00af6f0c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af6f18`](#insn-00af6f18) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af6dec`](#insn-00af6dec)

~~~json
{
  "source": "00af6dec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6df0`](#insn-00af6df0)

~~~json
{
  "source": "00af6df0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6df4`](#insn-00af6df4)

~~~json
{
  "source": "00af6df4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6df8`](#insn-00af6df8)

~~~json
{
  "source": "00af6df8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e2c`](#insn-00af6e2c)

~~~json
{
  "source": "00af6e2c",
  "target": "00af6f18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e38`](#insn-00af6e38)

~~~json
{
  "source": "00af6e38",
  "target": "00af6e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e48`](#insn-00af6e48)

~~~json
{
  "source": "00af6e48",
  "target": "00af6e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e4c`](#insn-00af6e4c)

~~~json
{
  "source": "00af6e4c",
  "target": "00af6e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e5c`](#insn-00af6e5c)

~~~json
{
  "source": "00af6e5c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6e7c`](#insn-00af6e7c)

~~~json
{
  "source": "00af6e7c",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6e88`](#insn-00af6e88)

~~~json
{
  "source": "00af6e88",
  "target": "00af6ea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6e9c`](#insn-00af6e9c)

~~~json
{
  "source": "00af6e9c",
  "target": "00af6eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6ea0`](#insn-00af6ea0)

~~~json
{
  "source": "00af6ea0",
  "target": "00af6ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6eb0`](#insn-00af6eb0)

~~~json
{
  "source": "00af6eb0",
  "target": "00af6ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6ecc`](#insn-00af6ecc)

~~~json
{
  "source": "00af6ecc",
  "target": "00bdda90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af6ed4`](#insn-00af6ed4)

~~~json
{
  "source": "00af6ed4",
  "target": "00af6eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6ee8`](#insn-00af6ee8)

~~~json
{
  "source": "00af6ee8",
  "target": "00af6ef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6f04`](#insn-00af6f04)

~~~json
{
  "source": "00af6f04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6f08`](#insn-00af6f08)

~~~json
{
  "source": "00af6f08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6f0c`](#insn-00af6f0c)

~~~json
{
  "source": "00af6f0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af6f18`](#insn-00af6f18)

~~~json
{
  "source": "00af6f18",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
