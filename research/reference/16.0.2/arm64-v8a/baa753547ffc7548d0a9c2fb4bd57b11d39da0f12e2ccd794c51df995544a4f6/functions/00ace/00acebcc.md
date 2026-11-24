# 00acebcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aceb5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00aceb5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-5c2b10d5954148e001ef5fff822fe59e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acfbc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfbc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-70082e895d5d4cb49eadb5f0bc0f5956)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acebcc",
  "name": "FUN_00acebcc",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "030c2731cfc8b82a3d55ebaab2a9d50ed20a08d4e052d1aa88c1b6f5b6f0bc67",
  "source_text_sha256": "030c2731cfc8b82a3d55ebaab2a9d50ed20a08d4e052d1aa88c1b6f5b6f0bc67",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acebcc",
        "00acecc3"
      ]
    ],
    "bytes_sha256": "50e238f9d0a492336bec2ac563c42a2a77721d3bd6a1dc9db65afc123eb30da8",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005e12e4](../005e1/005e12e4.md)
- [005e1660](../005e1/005e1660.md)
- [005e1790](../005e1/005e1790.md)
- [0066242c](../00662/0066242c.md)
- [006624d0](../00662/006624d0.md)
- [00662574](../00662/00662574.md)
- [007ccf44](../007cc/007ccf44.md)
- [007de918](../007de/007de918.md)
- [008c42e4](../008c4/008c42e4.md)
- [00a421e8](../00a42/00a421e8.md)
- [00a47f54](../00a47/00a47f54.md)
- [00acc640](../00acc/00acc640.md)
- [00ad09c8](../00ad0/00ad09c8.md)
- [00ad6fbc](../00ad6/00ad6fbc.md)
- [00aeb030](../00aeb/00aeb030.md)
- [00aec9fc](../00aec/00aec9fc.md)

## 呼び出し先

- [0067678c](../00676/0067678c.md)
- [007bbda0](../007bb/007bbda0.md)
- [00800244](../00800/00800244.md)
- [00802710](../00802/00802710.md)
- [00802bb0](../00802/00802bb0.md)
- [00802d00](../00802/00802d00.md)
- [00802f38](../00802/00802f38.md)
- [00851550](../00851/00851550.md)
- [00a32a58](../00a32/00a32a58.md)
- [00a32e5c](../00a32/00a32e5c.md)
- [00a32eec](../00a32/00a32eec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1332 bytes

~~~c

int FUN_00acebcc(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00802bb0(0);
  iVar2 = FUN_00802d00();
  iVar3 = FUN_00802f38();
  iVar4 = 1000000000;
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a32a58(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a32eec(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a32e5c(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
                    /* try { // try from 00acec58 to 00bcec8b has its CatchHandler @ 00acf9c0 */
    iVar3 = FUN_00802710(0);
    if (iVar3 == -8) {
      lVar6 = FUN_00851550();
      return *(int *)(lVar6 + 0x33a0);
    }
    uVar5 = FUN_0067678c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
      uVar5 = FUN_007bbda0(param_1,1);
      if ((uVar5 & 1) == 0) goto LAB_00acec44;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
                    /* try { // try from 00acec8c to 00bcec97 has its CatchHandler @ 00acf684 */
    }
    iVar4 = FUN_00800244(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acec44:
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
                    /* try { // try from 00acecbc to 00bcecd7 has its CatchHandler @ 00acf958 */
  return iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acebcc"></a> `00acebcc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acebd0"></a> `00acebd0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acebd4"></a> `00acebd4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acebd8"></a> `00acebd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acebdc"></a> `00acebdc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acebe0"></a> `00acebe0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acebe4"></a> `00acebe4` | `f3 cf f4 97` | bl 0x00802bb0 | `UNCONDITIONAL_CALL`
<a id="insn-00acebe8"></a> `00acebe8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acebec"></a> `00acebec` | `45 d0 f4 97` | bl 0x00802d00 | `UNCONDITIONAL_CALL`
<a id="insn-00acebf0"></a> `00acebf0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00acebf4"></a> `00acebf4` | `d1 d0 f4 97` | bl 0x00802f38 | `UNCONDITIONAL_CALL`
<a id="insn-00acebf8"></a> `00acebf8` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00acebfc"></a> `00acebfc` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00acec00"></a> `00acec00` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acec04"></a> `00acec04` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acec08"></a> `00acec08` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acec0c"></a> `00acec0c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acec10"></a> `00acec10` | `16 01 9f 1a` | csel w22,w8,wzr,eq | `FALL_THROUGH`
<a id="insn-00acec14"></a> `00acec14` | `91 8f fd 97` | bl 0x00a32a58 | `UNCONDITIONAL_CALL`
<a id="insn-00acec18"></a> `00acec18` | `00 01 00 36` | tbz w0,#0x0,0x00acec38 | `CONDITIONAL_JUMP`
<a id="insn-00acec1c"></a> `00acec1c` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acec20"></a> `00acec20` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00acec24"></a> `00acec24` | `b2 90 fd 97` | bl 0x00a32eec | `UNCONDITIONAL_CALL`
<a id="insn-00acec28"></a> `00acec28` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acec2c"></a> `00acec2c` | `c9 02 13 0b` | add w9,w22,w19 | `FALL_THROUGH`
<a id="insn-00acec30"></a> `00acec30` | `00 24 08 1b` | madd w0,w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00acec34"></a> `00acec34` | `20 00 00 14` | b 0x00acecb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec38"></a> `00acec38` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acec3c"></a> `00acec3c` | `88 90 fd 97` | bl 0x00a32e5c | `UNCONDITIONAL_CALL`
<a id="insn-00acec40"></a> `00acec40` | `a0 00 00 36` | tbz w0,#0x0,0x00acec54 | `CONDITIONAL_JUMP`
<a id="insn-00acec44"></a> `00acec44` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acec48"></a> `00acec48` | `88 4e 08 1b` | madd w8,w20,w8,w19 | `FALL_THROUGH`
<a id="insn-00acec4c"></a> `00acec4c` | `00 01 16 0b` | add w0,w8,w22 | `FALL_THROUGH`
<a id="insn-00acec50"></a> `00acec50` | `19 00 00 14` | b 0x00acecb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec54"></a> `00acec54` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acec58"></a> `00acec58` | `ae ce f4 97` | bl 0x00802710 | `UNCONDITIONAL_CALL`
<a id="insn-00acec5c"></a> `00acec5c` | `1f 20 00 31` | cmn w0,#0x8 | `FALL_THROUGH`
<a id="insn-00acec60"></a> `00acec60` | `81 00 00 54` | b.ne 0x00acec70 | `CONDITIONAL_JUMP`
<a id="insn-00acec64"></a> `00acec64` | `3b 0a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acec68"></a> `00acec68` | `00 a0 73 b9` | ldr w0,[x0, #0x33a0] | `FALL_THROUGH`
<a id="insn-00acec6c"></a> `00acec6c` | `12 00 00 14` | b 0x00acecb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec70"></a> `00acec70` | `08 7b 82 52` | mov w8,#0x13d8 | `FALL_THROUGH`
<a id="insn-00acec74"></a> `00acec74` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acec78"></a> `00acec78` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00acec7c"></a> `00acec7c` | `c4 9e ee 97` | bl 0x0067678c | `UNCONDITIONAL_CALL`
<a id="insn-00acec80"></a> `00acec80` | `80 00 00 36` | tbz w0,#0x0,0x00acec90 | `CONDITIONAL_JUMP`
<a id="insn-00acec84"></a> `00acec84` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acec88"></a> `00acec88` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-00acec8c"></a> `00acec8c` | `07 00 00 14` | b 0x00aceca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec90"></a> `00acec90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acec94"></a> `00acec94` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acec98"></a> `00acec98` | `42 b4 f3 97` | bl 0x007bbda0 | `UNCONDITIONAL_CALL`
<a id="insn-00acec9c"></a> `00acec9c` | `40 fd 07 36` | tbz w0,#0x0,0x00acec44 | `CONDITIONAL_JUMP`
<a id="insn-00aceca0"></a> `00aceca0` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00aceca4"></a> `00aceca4` | `81 08 80 52` | mov w1,#0x44 | `FALL_THROUGH`
<a id="insn-00aceca8"></a> `00aceca8` | `67 c5 f4 97` | bl 0x00800244 | `UNCONDITIONAL_CALL`
<a id="insn-00acecac"></a> `00acecac` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acecb0"></a> `00acecb0` | `00 7c 08 1b` | mul w0,w0,w8 | `FALL_THROUGH`
<a id="insn-00acecb4"></a> `00acecb4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acecb8"></a> `00acecb8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acecbc"></a> `00acecbc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acecc0"></a> `00acecc0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acebcc`](#insn-00acebcc) 範囲 `[['00acebcc', '00acec1b']]`
  - `CONDITIONAL_JUMP` [`00acec18`](#insn-00acec18) → [`00acec38`](#insn-00acec38)
  - `FALL_THROUGH` [`00acec18`](#insn-00acec18) → [`00acec1c`](#insn-00acec1c)
- ブロック [`00acec1c`](#insn-00acec1c) 範囲 `[['00acec1c', '00acec37']]`
  - `UNCONDITIONAL_JUMP` [`00acec34`](#insn-00acec34) → [`00acecb4`](#insn-00acecb4)
- ブロック [`00acec38`](#insn-00acec38) 範囲 `[['00acec38', '00acec43']]`
  - `CONDITIONAL_JUMP` [`00acec40`](#insn-00acec40) → [`00acec54`](#insn-00acec54)
  - `FALL_THROUGH` [`00acec40`](#insn-00acec40) → [`00acec44`](#insn-00acec44)
- ブロック [`00acec44`](#insn-00acec44) 範囲 `[['00acec44', '00acec53']]`
  - `UNCONDITIONAL_JUMP` [`00acec50`](#insn-00acec50) → [`00acecb4`](#insn-00acecb4)
- ブロック [`00acec54`](#insn-00acec54) 範囲 `[['00acec54', '00acec57']]`
  - `FALL_THROUGH` [`00acec54`](#insn-00acec54) → [`00acec58`](#insn-00acec58)
- ブロック [`00acec58`](#insn-00acec58) 範囲 `[['00acec58', '00acec63']]`
  - `CONDITIONAL_JUMP` [`00acec60`](#insn-00acec60) → [`00acec70`](#insn-00acec70)
  - `FALL_THROUGH` [`00acec60`](#insn-00acec60) → [`00acec64`](#insn-00acec64)
- ブロック [`00acec64`](#insn-00acec64) 範囲 `[['00acec64', '00acec6f']]`
  - `UNCONDITIONAL_JUMP` [`00acec6c`](#insn-00acec6c) → [`00acecb4`](#insn-00acecb4)
- ブロック [`00acec70`](#insn-00acec70) 範囲 `[['00acec70', '00acec83']]`
  - `CONDITIONAL_JUMP` [`00acec80`](#insn-00acec80) → [`00acec90`](#insn-00acec90)
  - `FALL_THROUGH` [`00acec80`](#insn-00acec80) → [`00acec84`](#insn-00acec84)
- ブロック [`00acec84`](#insn-00acec84) 範囲 `[['00acec84', '00acec8b']]`
  - `FALL_THROUGH` [`00acec88`](#insn-00acec88) → [`00acec8c`](#insn-00acec8c)
- ブロック [`00acec8c`](#insn-00acec8c) 範囲 `[['00acec8c', '00acec8f']]`
  - `UNCONDITIONAL_JUMP` [`00acec8c`](#insn-00acec8c) → [`00aceca8`](#insn-00aceca8)
- ブロック [`00acec90`](#insn-00acec90) 範囲 `[['00acec90', '00acec9f']]`
  - `CONDITIONAL_JUMP` [`00acec9c`](#insn-00acec9c) → [`00acec44`](#insn-00acec44)
  - `FALL_THROUGH` [`00acec9c`](#insn-00acec9c) → [`00aceca0`](#insn-00aceca0)
- ブロック [`00aceca0`](#insn-00aceca0) 範囲 `[['00aceca0', '00aceca7']]`
  - `FALL_THROUGH` [`00aceca4`](#insn-00aceca4) → [`00aceca8`](#insn-00aceca8)
- ブロック [`00aceca8`](#insn-00aceca8) 範囲 `[['00aceca8', '00acecb3']]`
  - `FALL_THROUGH` [`00acecb0`](#insn-00acecb0) → [`00acecb4`](#insn-00acecb4)
- ブロック [`00acecb4`](#insn-00acecb4) 範囲 `[['00acecb4', '00acecbb']]`
  - `FALL_THROUGH` [`00acecb8`](#insn-00acecb8) → [`00acecbc`](#insn-00acecbc)
- ブロック [`00acecbc`](#insn-00acecbc) 範囲 `[['00acecbc', '00acecc3']]`

## 命令位置別の参照

- [`00acebcc`](#insn-00acebcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebd0`](#insn-00acebd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebd4`](#insn-00acebd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebe4`](#insn-00acebe4) → [`00802bb0`](../00802/00802bb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802bb0` · 推定シンボル `None` · 推定型 `None`
- [`00acebec`](#insn-00acebec) → [`00802d00`](../00802/00802d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802d00` · 推定シンボル `None` · 推定型 `None`
- [`00acebf4`](#insn-00acebf4) → [`00802f38`](../00802/00802f38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802f38` · 推定シンボル `None` · 推定型 `None`
- [`00acec14`](#insn-00acec14) → [`00a32a58`](../00a32/00a32a58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32a58` · 推定シンボル `None` · 推定型 `None`
- [`00acec18`](#insn-00acec18) → [`00acec38`](#insn-00acec38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec24`](#insn-00acec24) → [`00a32eec`](../00a32/00a32eec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32eec` · 推定シンボル `None` · 推定型 `None`
- [`00acec34`](#insn-00acec34) → [`00acecb4`](#insn-00acecb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec3c`](#insn-00acec3c) → [`00a32e5c`](../00a32/00a32e5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32e5c` · 推定シンボル `None` · 推定型 `None`
- [`00acec40`](#insn-00acec40) → [`00acec54`](#insn-00acec54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec50`](#insn-00acec50) → [`00acecb4`](#insn-00acecb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec58`](#insn-00acec58) → [`00802710`](../00802/00802710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802710` · 推定シンボル `None` · 推定型 `None`
- [`00acec60`](#insn-00acec60) → [`00acec70`](#insn-00acec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec64`](#insn-00acec64) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acec6c`](#insn-00acec6c) → [`00acecb4`](#insn-00acecb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec7c`](#insn-00acec7c) → [`0067678c`](../00676/0067678c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067678c` · 推定シンボル `None` · 推定型 `None`
- [`00acec80`](#insn-00acec80) → [`00acec90`](#insn-00acec90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec8c`](#insn-00acec8c) → [`00aceca8`](#insn-00aceca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec98`](#insn-00acec98) → [`007bbda0`](../007bb/007bbda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bbda0` · 推定シンボル `None` · 推定型 `None`
- [`00acec9c`](#insn-00acec9c) → [`00acec44`](#insn-00acec44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceca8`](#insn-00aceca8) → [`00800244`](../00800/00800244.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800244` · 推定シンボル `None` · 推定型 `None`
- [`00acecb4`](#insn-00acecb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecb8`](#insn-00acecb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecbc`](#insn-00acecbc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acebcc`](#insn-00acebcc)

~~~json
{
  "source": "00acebcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebd0`](#insn-00acebd0)

~~~json
{
  "source": "00acebd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebd4`](#insn-00acebd4)

~~~json
{
  "source": "00acebd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebe4`](#insn-00acebe4)

~~~json
{
  "source": "00acebe4",
  "target": "00802bb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebec`](#insn-00acebec)

~~~json
{
  "source": "00acebec",
  "target": "00802d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebf4`](#insn-00acebf4)

~~~json
{
  "source": "00acebf4",
  "target": "00802f38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec14`](#insn-00acec14)

~~~json
{
  "source": "00acec14",
  "target": "00a32a58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec18`](#insn-00acec18)

~~~json
{
  "source": "00acec18",
  "target": "00acec38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec24`](#insn-00acec24)

~~~json
{
  "source": "00acec24",
  "target": "00a32eec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec34`](#insn-00acec34)

~~~json
{
  "source": "00acec34",
  "target": "00acecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec3c`](#insn-00acec3c)

~~~json
{
  "source": "00acec3c",
  "target": "00a32e5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec40`](#insn-00acec40)

~~~json
{
  "source": "00acec40",
  "target": "00acec54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec50`](#insn-00acec50)

~~~json
{
  "source": "00acec50",
  "target": "00acecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec58`](#insn-00acec58)

~~~json
{
  "source": "00acec58",
  "target": "00802710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec60`](#insn-00acec60)

~~~json
{
  "source": "00acec60",
  "target": "00acec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec64`](#insn-00acec64)

~~~json
{
  "source": "00acec64",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec6c`](#insn-00acec6c)

~~~json
{
  "source": "00acec6c",
  "target": "00acecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec7c`](#insn-00acec7c)

~~~json
{
  "source": "00acec7c",
  "target": "0067678c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec80`](#insn-00acec80)

~~~json
{
  "source": "00acec80",
  "target": "00acec90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec8c`](#insn-00acec8c)

~~~json
{
  "source": "00acec8c",
  "target": "00aceca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec98`](#insn-00acec98)

~~~json
{
  "source": "00acec98",
  "target": "007bbda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec9c`](#insn-00acec9c)

~~~json
{
  "source": "00acec9c",
  "target": "00acec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceca8`](#insn-00aceca8)

~~~json
{
  "source": "00aceca8",
  "target": "00800244",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acecb4`](#insn-00acecb4)

~~~json
{
  "source": "00acecb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecb8`](#insn-00acecb8)

~~~json
{
  "source": "00acecb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecbc`](#insn-00acecbc)

~~~json
{
  "source": "00acecbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
