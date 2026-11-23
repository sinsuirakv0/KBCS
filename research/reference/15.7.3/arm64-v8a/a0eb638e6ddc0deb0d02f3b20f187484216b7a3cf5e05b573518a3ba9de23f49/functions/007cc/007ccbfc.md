# 007ccbfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `007ccbfc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007cc/007ccbfc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0027.md#compare-40c005c1a4357332b1106211261d2fc0)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `007ccbfc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cc/007ccbfc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0027.md#compare-6f2e6cc257ec73621d3cc5c4c5a95a6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ccbfc",
  "name": "FUN_007ccbfc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "733e96490926b75617b5b251f9387b93186e9cc132d450689c643591894ac870",
  "source_text_sha256": "733e96490926b75617b5b251f9387b93186e9cc132d450689c643591894ac870",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ccbfc",
        "007ccd6f"
      ]
    ],
    "bytes_sha256": "06966933800231ef15ec363793e78a8c94710043c5ae87221a0b45fdf14e61a0",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0079653c](../00796/0079653c.md)

## 呼び出し先

- [00bdb1f0](../00bdb/00bdb1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2602 bytes

~~~c

void FUN_007ccbfc(long *param_1,ulong param_2,ulong param_3)

{
  ulong *puVar1;
  uint uVar2;
  ulong uVar3;
  ulong uVar4;
  ulong uVar5;
  ulong *puVar6;
  size_t __n;
  
  uVar3 = param_1[1];
  uVar4 = uVar3 + param_2;
  param_1[1] = uVar4;
                    /* try { // try from 007ccc0c to 008ccc17 has its CatchHandler @ 007cda74 */
                    /* try { // try from 007ccc1c to 008ccc33 has its CatchHandler @ 007cda70 */
  if ((uVar3 == 0) || (0x3f < (uVar4 - 1 ^ uVar3 - 1))) {
    uVar5 = 0;
    if (0x40 < uVar4) {
      uVar5 = uVar4 - 1 >> 6;
    }
                    /* try { // try from 007ccc34 to 008ccca7 has its CatchHandler @ 007c86d0 */
    *(undefined8 *)(*param_1 + uVar5 * 8) = 0;
  }
  if (param_2 != 0) {
    puVar1 = (ulong *)(*param_1 + (uVar3 >> 6) * 8);
    uVar2 = (uint)uVar3 & 0x3f;
    puVar6 = puVar1;
    if ((param_3 & 1) == 0) {
      if ((uVar3 & 0x3f) != 0) {
        uVar5 = (ulong)(0x40 - uVar2);
        uVar4 = uVar5;
        if (param_2 <= uVar5) {
          uVar4 = param_2;
        }
                    /* try { // try from 007ccd00 to 008ccd27 has its CatchHandler @ 007cdaf0 */
        param_2 = param_2 - uVar4;
        puVar6 = puVar1 + 1;
        *puVar1 = *puVar1 & (0xffffffffffffffffU >> (uVar5 - uVar4 & 0x3f) & -1L << (uVar3 & 0x3f) ^
                            0xffffffffffffffff);
      }
      __n = (param_2 >> 6) * 8;
      if (0x3f < param_2) {
                    /* try { // try from 007ccd28 to 008ccfa7 has its CatchHandler @ 007c86d0 */
        memset(puVar6,0,__n);
      }
      if ((param_2 & 0x3f) == 0) {
        return;
      }
      uVar4 = puVar6[param_2 >> 6] &
              (0xffffffffffffffffU >> (-(param_2 & 0x3f) & 0x3f) ^ 0xffffffffffffffff);
    }
    else {
      if ((uVar3 & 0x3f) != 0) {
        uVar5 = (ulong)(0x40 - uVar2);
        uVar4 = uVar5;
        if (param_2 <= uVar5) {
          uVar4 = param_2;
        }
        param_2 = param_2 - uVar4;
        puVar6 = puVar1 + 1;
        *puVar1 = *puVar1 | 0xffffffffffffffffU >> (uVar5 - uVar4 & 0x3f) & -1L << (uVar3 & 0x3f);
      }
      __n = (param_2 >> 6) * 8;
      if (0x3f < param_2) {
                    /* try { // try from 007ccca8 to 008cccb3 has its CatchHandler @ 007cda6c */
                    /* try { // try from 007cccb4 to 008cccff has its CatchHandler @ 007c86d0 */
        memset(puVar6,0xff,__n);
      }
      if ((param_2 & 0x3f) == 0) {
        return;
      }
      uVar4 = puVar6[param_2 >> 6] | 0xffffffffffffffffU >> (-(param_2 & 0x3f) & 0x3f);
    }
    *(ulong *)((long)puVar6 + __n) = uVar4;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ccbfc"></a> `007ccbfc` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007ccc00"></a> `007ccc00` | `09 01 01 8b` | add x9,x8,x1 | `FALL_THROUGH`
<a id="insn-007ccc04"></a> `007ccc04` | `09 04 00 f9` | str x9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007ccc08"></a> `007ccc08` | `c8 00 00 b4` | cbz x8,0x007ccc20 | `CONDITIONAL_JUMP`
<a id="insn-007ccc0c"></a> `007ccc0c` | `0a 05 00 d1` | sub x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-007ccc10"></a> `007ccc10` | `2b 05 00 d1` | sub x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-007ccc14"></a> `007ccc14` | `6a 01 0a ca` | eor x10,x11,x10 | `FALL_THROUGH`
<a id="insn-007ccc18"></a> `007ccc18` | `5f 01 01 f1` | cmp x10,#0x40 | `FALL_THROUGH`
<a id="insn-007ccc1c"></a> `007ccc1c` | `e3 00 00 54` | b.cc 0x007ccc38 | `CONDITIONAL_JUMP`
<a id="insn-007ccc20"></a> `007ccc20` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-007ccc24"></a> `007ccc24` | `0b 00 40 f9` | ldr x11,[x0] | `FALL_THROUGH`
<a id="insn-007ccc28"></a> `007ccc28` | `3f 05 01 f1` | cmp x9,#0x41 | `FALL_THROUGH`
<a id="insn-007ccc2c"></a> `007ccc2c` | `4a fd 46 d3` | lsr x10,x10,#0x6 | `FALL_THROUGH`
<a id="insn-007ccc30"></a> `007ccc30` | `e9 33 8a 9a` | csel x9,xzr,x10,cc | `FALL_THROUGH`
<a id="insn-007ccc34"></a> `007ccc34` | `7f 79 29 f8` | str xzr,[x11, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-007ccc38"></a> `007ccc38` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-007ccc3c"></a> `007ccc3c` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ccc40"></a> `007ccc40` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ccc44"></a> `007ccc44` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007ccc48"></a> `007ccc48` | `c1 08 00 b4` | cbz x1,0x007ccd60 | `CONDITIONAL_JUMP`
<a id="insn-007ccc4c"></a> `007ccc4c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-007ccc50"></a> `007ccc50` | `0a fd 46 d3` | lsr x10,x8,#0x6 | `FALL_THROUGH`
<a id="insn-007ccc54"></a> `007ccc54` | `33 0d 0a 8b` | add x19,x9,x10, LSL #0x3 | `FALL_THROUGH`
<a id="insn-007ccc58"></a> `007ccc58` | `09 15 00 12` | and w9,w8,#0x3f | `FALL_THROUGH`
<a id="insn-007ccc5c"></a> `007ccc5c` | `22 04 00 36` | tbz w2,#0x0,0x007ccce0 | `CONDITIONAL_JUMP`
<a id="insn-007ccc60"></a> `007ccc60` | `c9 01 00 34` | cbz w9,0x007ccc98 | `CONDITIONAL_JUMP`
<a id="insn-007ccc64"></a> `007ccc64` | `0a 08 80 52` | mov w10,#0x40 | `FALL_THROUGH`
<a id="insn-007ccc68"></a> `007ccc68` | `0b 00 80 92` | mov x11,#-0x1 | `FALL_THROUGH`
<a id="insn-007ccc6c"></a> `007ccc6c` | `49 01 09 4b` | sub w9,w10,w9 | `FALL_THROUGH`
<a id="insn-007ccc70"></a> `007ccc70` | `68 21 c8 9a` | lsl x8,x11,x8 | `FALL_THROUGH`
<a id="insn-007ccc74"></a> `007ccc74` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-007ccc78"></a> `007ccc78` | `2a 31 81 9a` | csel x10,x9,x1,cc | `FALL_THROUGH`
<a id="insn-007ccc7c"></a> `007ccc7c` | `29 01 0a cb` | sub x9,x9,x10 | `FALL_THROUGH`
<a id="insn-007ccc80"></a> `007ccc80` | `21 00 0a cb` | sub x1,x1,x10 | `FALL_THROUGH`
<a id="insn-007ccc84"></a> `007ccc84` | `69 25 c9 9a` | lsr x9,x11,x9 | `FALL_THROUGH`
<a id="insn-007ccc88"></a> `007ccc88` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-007ccc8c"></a> `007ccc8c` | `28 01 08 8a` | and x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007ccc90"></a> `007ccc90` | `68 01 08 aa` | orr x8,x11,x8 | `FALL_THROUGH`
<a id="insn-007ccc94"></a> `007ccc94` | `68 86 00 f8` | str x8,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-007ccc98"></a> `007ccc98` | `28 fc 46 d3` | lsr x8,x1,#0x6 | `FALL_THROUGH`
<a id="insn-007ccc9c"></a> `007ccc9c` | `3f 00 01 f1` | cmp x1,#0x40 | `FALL_THROUGH`
<a id="insn-007ccca0"></a> `007ccca0` | `14 f1 7d d3` | lsl x20,x8,#0x3 | `FALL_THROUGH`
<a id="insn-007ccca4"></a> `007ccca4` | `e3 00 00 54` | b.cc 0x007cccc0 | `CONDITIONAL_JUMP`
<a id="insn-007ccca8"></a> `007ccca8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007cccac"></a> `007cccac` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007cccb0"></a> `007cccb0` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-007cccb4"></a> `007cccb4` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007cccb8"></a> `007cccb8` | `4e 39 10 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-007cccbc"></a> `007cccbc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007cccc0"></a> `007cccc0` | `28 14 40 f2` | ands x8,x1,#0x3f | `FALL_THROUGH`
<a id="insn-007cccc4"></a> `007cccc4` | `e0 04 00 54` | b.eq 0x007ccd60 | `CONDITIONAL_JUMP`
<a id="insn-007cccc8"></a> `007cccc8` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-007ccccc"></a> `007ccccc` | `09 00 80 92` | mov x9,#-0x1 | `FALL_THROUGH`
<a id="insn-007cccd0"></a> `007cccd0` | `28 25 c8 9a` | lsr x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007cccd4"></a> `007cccd4` | `69 6a 74 f8` | ldr x9,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007cccd8"></a> `007cccd8` | `28 01 08 aa` | orr x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007cccdc"></a> `007cccdc` | `20 00 00 14` | b 0x007ccd5c | `UNCONDITIONAL_JUMP`
<a id="insn-007ccce0"></a> `007ccce0` | `c9 01 00 34` | cbz w9,0x007ccd18 | `CONDITIONAL_JUMP`
<a id="insn-007ccce4"></a> `007ccce4` | `0a 08 80 52` | mov w10,#0x40 | `FALL_THROUGH`
<a id="insn-007ccce8"></a> `007ccce8` | `0b 00 80 92` | mov x11,#-0x1 | `FALL_THROUGH`
<a id="insn-007cccec"></a> `007cccec` | `49 01 09 4b` | sub w9,w10,w9 | `FALL_THROUGH`
<a id="insn-007cccf0"></a> `007cccf0` | `68 21 c8 9a` | lsl x8,x11,x8 | `FALL_THROUGH`
<a id="insn-007cccf4"></a> `007cccf4` | `3f 01 01 eb` | cmp x9,x1 | `FALL_THROUGH`
<a id="insn-007cccf8"></a> `007cccf8` | `2a 31 81 9a` | csel x10,x9,x1,cc | `FALL_THROUGH`
<a id="insn-007cccfc"></a> `007cccfc` | `29 01 0a cb` | sub x9,x9,x10 | `FALL_THROUGH`
<a id="insn-007ccd00"></a> `007ccd00` | `21 00 0a cb` | sub x1,x1,x10 | `FALL_THROUGH`
<a id="insn-007ccd04"></a> `007ccd04` | `69 25 c9 9a` | lsr x9,x11,x9 | `FALL_THROUGH`
<a id="insn-007ccd08"></a> `007ccd08` | `6b 02 40 f9` | ldr x11,[x19] | `FALL_THROUGH`
<a id="insn-007ccd0c"></a> `007ccd0c` | `28 01 08 8a` | and x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007ccd10"></a> `007ccd10` | `68 01 28 8a` | bic x8,x11,x8 | `FALL_THROUGH`
<a id="insn-007ccd14"></a> `007ccd14` | `68 86 00 f8` | str x8,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-007ccd18"></a> `007ccd18` | `28 fc 46 d3` | lsr x8,x1,#0x6 | `FALL_THROUGH`
<a id="insn-007ccd1c"></a> `007ccd1c` | `3f 00 01 f1` | cmp x1,#0x40 | `FALL_THROUGH`
<a id="insn-007ccd20"></a> `007ccd20` | `14 f1 7d d3` | lsl x20,x8,#0x3 | `FALL_THROUGH`
<a id="insn-007ccd24"></a> `007ccd24` | `e3 00 00 54` | b.cc 0x007ccd40 | `CONDITIONAL_JUMP`
<a id="insn-007ccd28"></a> `007ccd28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007ccd2c"></a> `007ccd2c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-007ccd30"></a> `007ccd30` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-007ccd34"></a> `007ccd34` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-007ccd38"></a> `007ccd38` | `2e 39 10 94` | bl 0x00bdb1f0 | `UNCONDITIONAL_CALL`
<a id="insn-007ccd3c"></a> `007ccd3c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-007ccd40"></a> `007ccd40` | `28 14 40 f2` | ands x8,x1,#0x3f | `FALL_THROUGH`
<a id="insn-007ccd44"></a> `007ccd44` | `e0 00 00 54` | b.eq 0x007ccd60 | `CONDITIONAL_JUMP`
<a id="insn-007ccd48"></a> `007ccd48` | `e8 03 08 cb` | neg x8,x8 | `FALL_THROUGH`
<a id="insn-007ccd4c"></a> `007ccd4c` | `09 00 80 92` | mov x9,#-0x1 | `FALL_THROUGH`
<a id="insn-007ccd50"></a> `007ccd50` | `28 25 c8 9a` | lsr x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007ccd54"></a> `007ccd54` | `69 6a 74 f8` | ldr x9,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ccd58"></a> `007ccd58` | `28 01 28 8a` | bic x8,x9,x8 | `FALL_THROUGH`
<a id="insn-007ccd5c"></a> `007ccd5c` | `68 6a 34 f8` | str x8,[x19, x20, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007ccd60"></a> `007ccd60` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007ccd64"></a> `007ccd64` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007ccd68"></a> `007ccd68` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-007ccd6c"></a> `007ccd6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ccbfc`](#insn-007ccbfc) 範囲 `[['007ccbfc', '007ccc0b']]`
  - `CONDITIONAL_JUMP` [`007ccc08`](#insn-007ccc08) → [`007ccc20`](#insn-007ccc20)
  - `FALL_THROUGH` [`007ccc08`](#insn-007ccc08) → [`007ccc0c`](#insn-007ccc0c)
- ブロック [`007ccc0c`](#insn-007ccc0c) 範囲 `[['007ccc0c', '007ccc1b']]`
  - `FALL_THROUGH` [`007ccc18`](#insn-007ccc18) → [`007ccc1c`](#insn-007ccc1c)
- ブロック [`007ccc1c`](#insn-007ccc1c) 範囲 `[['007ccc1c', '007ccc1f']]`
  - `CONDITIONAL_JUMP` [`007ccc1c`](#insn-007ccc1c) → [`007ccc38`](#insn-007ccc38)
  - `FALL_THROUGH` [`007ccc1c`](#insn-007ccc1c) → [`007ccc20`](#insn-007ccc20)
- ブロック [`007ccc20`](#insn-007ccc20) 範囲 `[['007ccc20', '007ccc33']]`
  - `FALL_THROUGH` [`007ccc30`](#insn-007ccc30) → [`007ccc34`](#insn-007ccc34)
- ブロック [`007ccc34`](#insn-007ccc34) 範囲 `[['007ccc34', '007ccc37']]`
  - `FALL_THROUGH` [`007ccc34`](#insn-007ccc34) → [`007ccc38`](#insn-007ccc38)
- ブロック [`007ccc38`](#insn-007ccc38) 範囲 `[['007ccc38', '007ccc4b']]`
  - `CONDITIONAL_JUMP` [`007ccc48`](#insn-007ccc48) → [`007ccd60`](#insn-007ccd60)
  - `FALL_THROUGH` [`007ccc48`](#insn-007ccc48) → [`007ccc4c`](#insn-007ccc4c)
- ブロック [`007ccc4c`](#insn-007ccc4c) 範囲 `[['007ccc4c', '007ccc5f']]`
  - `CONDITIONAL_JUMP` [`007ccc5c`](#insn-007ccc5c) → [`007ccce0`](#insn-007ccce0)
  - `FALL_THROUGH` [`007ccc5c`](#insn-007ccc5c) → [`007ccc60`](#insn-007ccc60)
- ブロック [`007ccc60`](#insn-007ccc60) 範囲 `[['007ccc60', '007ccc63']]`
  - `CONDITIONAL_JUMP` [`007ccc60`](#insn-007ccc60) → [`007ccc98`](#insn-007ccc98)
  - `FALL_THROUGH` [`007ccc60`](#insn-007ccc60) → [`007ccc64`](#insn-007ccc64)
- ブロック [`007ccc64`](#insn-007ccc64) 範囲 `[['007ccc64', '007ccc97']]`
  - `FALL_THROUGH` [`007ccc94`](#insn-007ccc94) → [`007ccc98`](#insn-007ccc98)
- ブロック [`007ccc98`](#insn-007ccc98) 範囲 `[['007ccc98', '007ccca7']]`
  - `CONDITIONAL_JUMP` [`007ccca4`](#insn-007ccca4) → [`007cccc0`](#insn-007cccc0)
  - `FALL_THROUGH` [`007ccca4`](#insn-007ccca4) → [`007ccca8`](#insn-007ccca8)
- ブロック [`007ccca8`](#insn-007ccca8) 範囲 `[['007ccca8', '007cccb3']]`
  - `FALL_THROUGH` [`007cccb0`](#insn-007cccb0) → [`007cccb4`](#insn-007cccb4)
- ブロック [`007cccb4`](#insn-007cccb4) 範囲 `[['007cccb4', '007cccbf']]`
  - `FALL_THROUGH` [`007cccbc`](#insn-007cccbc) → [`007cccc0`](#insn-007cccc0)
- ブロック [`007cccc0`](#insn-007cccc0) 範囲 `[['007cccc0', '007cccc7']]`
  - `CONDITIONAL_JUMP` [`007cccc4`](#insn-007cccc4) → [`007ccd60`](#insn-007ccd60)
  - `FALL_THROUGH` [`007cccc4`](#insn-007cccc4) → [`007cccc8`](#insn-007cccc8)
- ブロック [`007cccc8`](#insn-007cccc8) 範囲 `[['007cccc8', '007cccdf']]`
  - `UNCONDITIONAL_JUMP` [`007cccdc`](#insn-007cccdc) → [`007ccd5c`](#insn-007ccd5c)
- ブロック [`007ccce0`](#insn-007ccce0) 範囲 `[['007ccce0', '007ccce3']]`
  - `CONDITIONAL_JUMP` [`007ccce0`](#insn-007ccce0) → [`007ccd18`](#insn-007ccd18)
  - `FALL_THROUGH` [`007ccce0`](#insn-007ccce0) → [`007ccce4`](#insn-007ccce4)
- ブロック [`007ccce4`](#insn-007ccce4) 範囲 `[['007ccce4', '007cccff']]`
  - `FALL_THROUGH` [`007cccfc`](#insn-007cccfc) → [`007ccd00`](#insn-007ccd00)
- ブロック [`007ccd00`](#insn-007ccd00) 範囲 `[['007ccd00', '007ccd17']]`
  - `FALL_THROUGH` [`007ccd14`](#insn-007ccd14) → [`007ccd18`](#insn-007ccd18)
- ブロック [`007ccd18`](#insn-007ccd18) 範囲 `[['007ccd18', '007ccd27']]`
  - `CONDITIONAL_JUMP` [`007ccd24`](#insn-007ccd24) → [`007ccd40`](#insn-007ccd40)
  - `FALL_THROUGH` [`007ccd24`](#insn-007ccd24) → [`007ccd28`](#insn-007ccd28)
- ブロック [`007ccd28`](#insn-007ccd28) 範囲 `[['007ccd28', '007ccd3f']]`
  - `FALL_THROUGH` [`007ccd3c`](#insn-007ccd3c) → [`007ccd40`](#insn-007ccd40)
- ブロック [`007ccd40`](#insn-007ccd40) 範囲 `[['007ccd40', '007ccd47']]`
  - `CONDITIONAL_JUMP` [`007ccd44`](#insn-007ccd44) → [`007ccd60`](#insn-007ccd60)
  - `FALL_THROUGH` [`007ccd44`](#insn-007ccd44) → [`007ccd48`](#insn-007ccd48)
- ブロック [`007ccd48`](#insn-007ccd48) 範囲 `[['007ccd48', '007ccd5b']]`
  - `FALL_THROUGH` [`007ccd58`](#insn-007ccd58) → [`007ccd5c`](#insn-007ccd5c)
- ブロック [`007ccd5c`](#insn-007ccd5c) 範囲 `[['007ccd5c', '007ccd5f']]`
  - `FALL_THROUGH` [`007ccd5c`](#insn-007ccd5c) → [`007ccd60`](#insn-007ccd60)
- ブロック [`007ccd60`](#insn-007ccd60) 範囲 `[['007ccd60', '007ccd6f']]`

## 命令位置別の参照

- [`007ccc08`](#insn-007ccc08) → [`007ccc20`](#insn-007ccc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc1c`](#insn-007ccc1c) → [`007ccc38`](#insn-007ccc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc38`](#insn-007ccc38) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc3c`](#insn-007ccc3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc40`](#insn-007ccc40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc48`](#insn-007ccc48) → [`007ccd60`](#insn-007ccd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc5c`](#insn-007ccc5c) → [`007ccce0`](#insn-007ccce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccc60`](#insn-007ccc60) → [`007ccc98`](#insn-007ccc98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccca4`](#insn-007ccca4) → [`007cccc0`](#insn-007cccc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cccb8`](#insn-007cccb8) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`007cccc4`](#insn-007cccc4) → [`007ccd60`](#insn-007ccd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cccdc`](#insn-007cccdc) → [`007ccd5c`](#insn-007ccd5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccce0`](#insn-007ccce0) → [`007ccd18`](#insn-007ccd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccd24`](#insn-007ccd24) → [`007ccd40`](#insn-007ccd40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccd38`](#insn-007ccd38) → [`00bdb1f0`](../00bdb/00bdb1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1f0` · 推定シンボル `None` · 推定型 `None`
- [`007ccd44`](#insn-007ccd44) → [`007ccd60`](#insn-007ccd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccd60`](#insn-007ccd60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccd64`](#insn-007ccd64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007ccd68`](#insn-007ccd68) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ccc08`](#insn-007ccc08)

~~~json
{
  "source": "007ccc08",
  "target": "007ccc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc1c`](#insn-007ccc1c)

~~~json
{
  "source": "007ccc1c",
  "target": "007ccc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc38`](#insn-007ccc38)

~~~json
{
  "source": "007ccc38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc3c`](#insn-007ccc3c)

~~~json
{
  "source": "007ccc3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc40`](#insn-007ccc40)

~~~json
{
  "source": "007ccc40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc48`](#insn-007ccc48)

~~~json
{
  "source": "007ccc48",
  "target": "007ccd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc5c`](#insn-007ccc5c)

~~~json
{
  "source": "007ccc5c",
  "target": "007ccce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccc60`](#insn-007ccc60)

~~~json
{
  "source": "007ccc60",
  "target": "007ccc98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccca4`](#insn-007ccca4)

~~~json
{
  "source": "007ccca4",
  "target": "007cccc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cccb8`](#insn-007cccb8)

~~~json
{
  "source": "007cccb8",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cccc4`](#insn-007cccc4)

~~~json
{
  "source": "007cccc4",
  "target": "007ccd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cccdc`](#insn-007cccdc)

~~~json
{
  "source": "007cccdc",
  "target": "007ccd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccce0`](#insn-007ccce0)

~~~json
{
  "source": "007ccce0",
  "target": "007ccd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccd24`](#insn-007ccd24)

~~~json
{
  "source": "007ccd24",
  "target": "007ccd40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccd38`](#insn-007ccd38)

~~~json
{
  "source": "007ccd38",
  "target": "00bdb1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007ccd44`](#insn-007ccd44)

~~~json
{
  "source": "007ccd44",
  "target": "007ccd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccd60`](#insn-007ccd60)

~~~json
{
  "source": "007ccd60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccd64`](#insn-007ccd64)

~~~json
{
  "source": "007ccd64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007ccd68`](#insn-007ccd68)

~~~json
{
  "source": "007ccd68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
