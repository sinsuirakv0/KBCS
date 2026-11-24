# 00acfbc0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acebcc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-70082e895d5d4cb49eadb5f0bc0f5956)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfbc0",
  "name": "FUN_00acfbc0",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b17ef6a109212bb1061ad42eb98c34bdb1f04aa9f85109954c103822d689bdef",
  "source_text_sha256": "b17ef6a109212bb1061ad42eb98c34bdb1f04aa9f85109954c103822d689bdef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfbc0",
        "00acfcb7"
      ]
    ],
    "bytes_sha256": "21813474e88bf89fe95f283a42d0fe40931ea76f8e5777820a1422043dee1c95",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005e1694](../005e1/005e1694.md)
- [005e1a10](../005e1/005e1a10.md)
- [005e1b40](../005e1/005e1b40.md)
- [006627dc](../00662/006627dc.md)
- [00662880](../00662/00662880.md)
- [00662924](../00662/00662924.md)
- [007cdea8](../007cd/007cdea8.md)
- [007df87c](../007df/007df87c.md)
- [008c5290](../008c5/008c5290.md)
- [00a431dc](../00a43/00a431dc.md)
- [00a48f48](../00a48/00a48f48.md)
- [00acd634](../00acd/00acd634.md)
- [00ad19bc](../00ad1/00ad19bc.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)
- [00aec024](../00aec/00aec024.md)
- [00aed9f0](../00aed/00aed9f0.md)

## 呼び出し先

- [00676b3c](../00676/00676b3c.md)
- [007bcd04](../007bc/007bcd04.md)
- [008011a8](../00801/008011a8.md)
- [00803674](../00803/00803674.md)
- [00803b14](../00803/00803b14.md)
- [00803c64](../00803/00803c64.md)
- [00803e9c](../00803/00803e9c.md)
- [008524fc](../00852/008524fc.md)
- [00a33a4c](../00a33/00a33a4c.md)
- [00a33e50](../00a33/00a33e50.md)
- [00a33ee0](../00a33/00a33ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1623 bytes

~~~c

int FUN_00acfbc0(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00803b14(0);
  iVar2 = FUN_00803c64();
  iVar3 = FUN_00803e9c();
  iVar4 = 1000000000;
                    /* try { // try from 00acfc04 to 00bcfc37 has its CatchHandler @ 00ad096c */
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a33a4c(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a33ee0(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a33e50(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
    iVar3 = FUN_00803674(0);
    if (iVar3 == -8) {
      lVar6 = FUN_008524fc();
      return *(int *)(lVar6 + 0x33a0);
    }
                    /* try { // try from 00acfc68 to 00bcfc83 has its CatchHandler @ 00ad0904 */
    uVar5 = FUN_00676b3c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
                    /* try { // try from 00acfc84 to 00bcfc8f has its CatchHandler @ 00ad05f8 */
      uVar5 = FUN_007bcd04(param_1,1);
                    /* try { // try from 00acfc90 to 00bcfcaf has its CatchHandler @ 00ad05a4 */
      if ((uVar5 & 1) == 0) goto LAB_00acfc38;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
    }
    iVar4 = FUN_008011a8(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acfc38:
                    /* try { // try from 00acfc38 to 00bcfc43 has its CatchHandler @ 00ad0630 */
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
                    /* try { // try from 00acfcb0 to 00bcfdff has its CatchHandler @ 00acdb7c */
  return iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfbc0"></a> `00acfbc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acfbc4"></a> `00acfbc4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfbc8"></a> `00acfbc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfbcc"></a> `00acfbcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acfbd0"></a> `00acfbd0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acfbd4"></a> `00acfbd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acfbd8"></a> `00acfbd8` | `cf cf f4 97` | bl 0x00803b14 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbdc"></a> `00acfbdc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acfbe0"></a> `00acfbe0` | `21 d0 f4 97` | bl 0x00803c64 | `UNCONDITIONAL_CALL`
<a id="insn-00acfbe4"></a> `00acfbe4` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00acfbe8"></a> `00acfbe8` | `ad d0 f4 97` | bl 0x00803e9c | `UNCONDITIONAL_CALL`
<a id="insn-00acfbec"></a> `00acfbec` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00acfbf0"></a> `00acfbf0` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00acfbf4"></a> `00acfbf4` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acfbf8"></a> `00acfbf8` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfbfc"></a> `00acfbfc` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc00"></a> `00acfc00` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acfc04"></a> `00acfc04` | `16 01 9f 1a` | csel w22,w8,wzr,eq | `FALL_THROUGH`
<a id="insn-00acfc08"></a> `00acfc08` | `91 8f fd 97` | bl 0x00a33a4c | `UNCONDITIONAL_CALL`
<a id="insn-00acfc0c"></a> `00acfc0c` | `00 01 00 36` | tbz w0,#0x0,0x00acfc2c | `CONDITIONAL_JUMP`
<a id="insn-00acfc10"></a> `00acfc10` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acfc14"></a> `00acfc14` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00acfc18"></a> `00acfc18` | `b2 90 fd 97` | bl 0x00a33ee0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc1c"></a> `00acfc1c` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acfc20"></a> `00acfc20` | `c9 02 13 0b` | add w9,w22,w19 | `FALL_THROUGH`
<a id="insn-00acfc24"></a> `00acfc24` | `00 24 08 1b` | madd w0,w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00acfc28"></a> `00acfc28` | `20 00 00 14` | b 0x00acfca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc2c"></a> `00acfc2c` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acfc30"></a> `00acfc30` | `88 90 fd 97` | bl 0x00a33e50 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc34"></a> `00acfc34` | `a0 00 00 36` | tbz w0,#0x0,0x00acfc48 | `CONDITIONAL_JUMP`
<a id="insn-00acfc38"></a> `00acfc38` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acfc3c"></a> `00acfc3c` | `88 4e 08 1b` | madd w8,w20,w8,w19 | `FALL_THROUGH`
<a id="insn-00acfc40"></a> `00acfc40` | `00 01 16 0b` | add w0,w8,w22 | `FALL_THROUGH`
<a id="insn-00acfc44"></a> `00acfc44` | `19 00 00 14` | b 0x00acfca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc48"></a> `00acfc48` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acfc4c"></a> `00acfc4c` | `8a ce f4 97` | bl 0x00803674 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc50"></a> `00acfc50` | `1f 20 00 31` | cmn w0,#0x8 | `FALL_THROUGH`
<a id="insn-00acfc54"></a> `00acfc54` | `81 00 00 54` | b.ne 0x00acfc64 | `CONDITIONAL_JUMP`
<a id="insn-00acfc58"></a> `00acfc58` | `29 0a f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00acfc5c"></a> `00acfc5c` | `00 a0 73 b9` | ldr w0,[x0, #0x33a0] | `FALL_THROUGH`
<a id="insn-00acfc60"></a> `00acfc60` | `12 00 00 14` | b 0x00acfca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc64"></a> `00acfc64` | `08 7b 82 52` | mov w8,#0x13d8 | `FALL_THROUGH`
<a id="insn-00acfc68"></a> `00acfc68` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc6c"></a> `00acfc6c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00acfc70"></a> `00acfc70` | `b3 9b ee 97` | bl 0x00676b3c | `UNCONDITIONAL_CALL`
<a id="insn-00acfc74"></a> `00acfc74` | `80 00 00 36` | tbz w0,#0x0,0x00acfc84 | `CONDITIONAL_JUMP`
<a id="insn-00acfc78"></a> `00acfc78` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acfc7c"></a> `00acfc7c` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-00acfc80"></a> `00acfc80` | `07 00 00 14` | b 0x00acfc9c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfc84"></a> `00acfc84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acfc88"></a> `00acfc88` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acfc8c"></a> `00acfc8c` | `1e b4 f3 97` | bl 0x007bcd04 | `UNCONDITIONAL_CALL`
<a id="insn-00acfc90"></a> `00acfc90` | `40 fd 07 36` | tbz w0,#0x0,0x00acfc38 | `CONDITIONAL_JUMP`
<a id="insn-00acfc94"></a> `00acfc94` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acfc98"></a> `00acfc98` | `81 08 80 52` | mov w1,#0x44 | `FALL_THROUGH`
<a id="insn-00acfc9c"></a> `00acfc9c` | `43 c5 f4 97` | bl 0x008011a8 | `UNCONDITIONAL_CALL`
<a id="insn-00acfca0"></a> `00acfca0` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acfca4"></a> `00acfca4` | `00 7c 08 1b` | mul w0,w0,w8 | `FALL_THROUGH`
<a id="insn-00acfca8"></a> `00acfca8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acfcac"></a> `00acfcac` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acfcb0"></a> `00acfcb0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acfcb4"></a> `00acfcb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfbc0`](#insn-00acfbc0) 範囲 `[['00acfbc0', '00acfc03']]`
  - `FALL_THROUGH` [`00acfc00`](#insn-00acfc00) → [`00acfc04`](#insn-00acfc04)
- ブロック [`00acfc04`](#insn-00acfc04) 範囲 `[['00acfc04', '00acfc0f']]`
  - `CONDITIONAL_JUMP` [`00acfc0c`](#insn-00acfc0c) → [`00acfc2c`](#insn-00acfc2c)
  - `FALL_THROUGH` [`00acfc0c`](#insn-00acfc0c) → [`00acfc10`](#insn-00acfc10)
- ブロック [`00acfc10`](#insn-00acfc10) 範囲 `[['00acfc10', '00acfc2b']]`
  - `UNCONDITIONAL_JUMP` [`00acfc28`](#insn-00acfc28) → [`00acfca8`](#insn-00acfca8)
- ブロック [`00acfc2c`](#insn-00acfc2c) 範囲 `[['00acfc2c', '00acfc37']]`
  - `CONDITIONAL_JUMP` [`00acfc34`](#insn-00acfc34) → [`00acfc48`](#insn-00acfc48)
  - `FALL_THROUGH` [`00acfc34`](#insn-00acfc34) → [`00acfc38`](#insn-00acfc38)
- ブロック [`00acfc38`](#insn-00acfc38) 範囲 `[['00acfc38', '00acfc47']]`
  - `UNCONDITIONAL_JUMP` [`00acfc44`](#insn-00acfc44) → [`00acfca8`](#insn-00acfca8)
- ブロック [`00acfc48`](#insn-00acfc48) 範囲 `[['00acfc48', '00acfc57']]`
  - `CONDITIONAL_JUMP` [`00acfc54`](#insn-00acfc54) → [`00acfc64`](#insn-00acfc64)
  - `FALL_THROUGH` [`00acfc54`](#insn-00acfc54) → [`00acfc58`](#insn-00acfc58)
- ブロック [`00acfc58`](#insn-00acfc58) 範囲 `[['00acfc58', '00acfc63']]`
  - `UNCONDITIONAL_JUMP` [`00acfc60`](#insn-00acfc60) → [`00acfca8`](#insn-00acfca8)
- ブロック [`00acfc64`](#insn-00acfc64) 範囲 `[['00acfc64', '00acfc67']]`
  - `FALL_THROUGH` [`00acfc64`](#insn-00acfc64) → [`00acfc68`](#insn-00acfc68)
- ブロック [`00acfc68`](#insn-00acfc68) 範囲 `[['00acfc68', '00acfc77']]`
  - `CONDITIONAL_JUMP` [`00acfc74`](#insn-00acfc74) → [`00acfc84`](#insn-00acfc84)
  - `FALL_THROUGH` [`00acfc74`](#insn-00acfc74) → [`00acfc78`](#insn-00acfc78)
- ブロック [`00acfc78`](#insn-00acfc78) 範囲 `[['00acfc78', '00acfc83']]`
  - `UNCONDITIONAL_JUMP` [`00acfc80`](#insn-00acfc80) → [`00acfc9c`](#insn-00acfc9c)
- ブロック [`00acfc84`](#insn-00acfc84) 範囲 `[['00acfc84', '00acfc8f']]`
  - `FALL_THROUGH` [`00acfc8c`](#insn-00acfc8c) → [`00acfc90`](#insn-00acfc90)
- ブロック [`00acfc90`](#insn-00acfc90) 範囲 `[['00acfc90', '00acfc93']]`
  - `CONDITIONAL_JUMP` [`00acfc90`](#insn-00acfc90) → [`00acfc38`](#insn-00acfc38)
  - `FALL_THROUGH` [`00acfc90`](#insn-00acfc90) → [`00acfc94`](#insn-00acfc94)
- ブロック [`00acfc94`](#insn-00acfc94) 範囲 `[['00acfc94', '00acfc9b']]`
  - `FALL_THROUGH` [`00acfc98`](#insn-00acfc98) → [`00acfc9c`](#insn-00acfc9c)
- ブロック [`00acfc9c`](#insn-00acfc9c) 範囲 `[['00acfc9c', '00acfca7']]`
  - `FALL_THROUGH` [`00acfca4`](#insn-00acfca4) → [`00acfca8`](#insn-00acfca8)
- ブロック [`00acfca8`](#insn-00acfca8) 範囲 `[['00acfca8', '00acfcaf']]`
  - `FALL_THROUGH` [`00acfcac`](#insn-00acfcac) → [`00acfcb0`](#insn-00acfcb0)
- ブロック [`00acfcb0`](#insn-00acfcb0) 範囲 `[['00acfcb0', '00acfcb7']]`

## 命令位置別の参照

- [`00acfbc0`](#insn-00acfbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc4`](#insn-00acfbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbc8`](#insn-00acfbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfbd8`](#insn-00acfbd8) → [`00803b14`](../00803/00803b14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803b14` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe0`](#insn-00acfbe0) → [`00803c64`](../00803/00803c64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803c64` · 推定シンボル `None` · 推定型 `None`
- [`00acfbe8`](#insn-00acfbe8) → [`00803e9c`](../00803/00803e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803e9c` · 推定シンボル `None` · 推定型 `None`
- [`00acfc08`](#insn-00acfc08) → [`00a33a4c`](../00a33/00a33a4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a33a4c` · 推定シンボル `None` · 推定型 `None`
- [`00acfc0c`](#insn-00acfc0c) → [`00acfc2c`](#insn-00acfc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc18`](#insn-00acfc18) → [`00a33ee0`](../00a33/00a33ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a33ee0` · 推定シンボル `None` · 推定型 `None`
- [`00acfc28`](#insn-00acfc28) → [`00acfca8`](#insn-00acfca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc30`](#insn-00acfc30) → [`00a33e50`](../00a33/00a33e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a33e50` · 推定シンボル `None` · 推定型 `None`
- [`00acfc34`](#insn-00acfc34) → [`00acfc48`](#insn-00acfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc44`](#insn-00acfc44) → [`00acfca8`](#insn-00acfca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc4c`](#insn-00acfc4c) → [`00803674`](../00803/00803674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803674` · 推定シンボル `None` · 推定型 `None`
- [`00acfc54`](#insn-00acfc54) → [`00acfc64`](#insn-00acfc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc58`](#insn-00acfc58) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00acfc60`](#insn-00acfc60) → [`00acfca8`](#insn-00acfca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc70`](#insn-00acfc70) → [`00676b3c`](../00676/00676b3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00676b3c` · 推定シンボル `None` · 推定型 `None`
- [`00acfc74`](#insn-00acfc74) → [`00acfc84`](#insn-00acfc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc80`](#insn-00acfc80) → [`00acfc9c`](#insn-00acfc9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc8c`](#insn-00acfc8c) → [`007bcd04`](../007bc/007bcd04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bcd04` · 推定シンボル `None` · 推定型 `None`
- [`00acfc90`](#insn-00acfc90) → [`00acfc38`](#insn-00acfc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfc9c`](#insn-00acfc9c) → [`008011a8`](../00801/008011a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008011a8` · 推定シンボル `None` · 推定型 `None`
- [`00acfca8`](#insn-00acfca8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcac`](#insn-00acfcac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcb0`](#insn-00acfcb0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfbc0`](#insn-00acfbc0)

~~~json
{
  "source": "00acfbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc4`](#insn-00acfbc4)

~~~json
{
  "source": "00acfbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbc8`](#insn-00acfbc8)

~~~json
{
  "source": "00acfbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfbd8`](#insn-00acfbd8)

~~~json
{
  "source": "00acfbd8",
  "target": "00803b14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbe0`](#insn-00acfbe0)

~~~json
{
  "source": "00acfbe0",
  "target": "00803c64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfbe8`](#insn-00acfbe8)

~~~json
{
  "source": "00acfbe8",
  "target": "00803e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc08`](#insn-00acfc08)

~~~json
{
  "source": "00acfc08",
  "target": "00a33a4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc0c`](#insn-00acfc0c)

~~~json
{
  "source": "00acfc0c",
  "target": "00acfc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc18`](#insn-00acfc18)

~~~json
{
  "source": "00acfc18",
  "target": "00a33ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc28`](#insn-00acfc28)

~~~json
{
  "source": "00acfc28",
  "target": "00acfca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc30`](#insn-00acfc30)

~~~json
{
  "source": "00acfc30",
  "target": "00a33e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc34`](#insn-00acfc34)

~~~json
{
  "source": "00acfc34",
  "target": "00acfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc44`](#insn-00acfc44)

~~~json
{
  "source": "00acfc44",
  "target": "00acfca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc4c`](#insn-00acfc4c)

~~~json
{
  "source": "00acfc4c",
  "target": "00803674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc54`](#insn-00acfc54)

~~~json
{
  "source": "00acfc54",
  "target": "00acfc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc58`](#insn-00acfc58)

~~~json
{
  "source": "00acfc58",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc60`](#insn-00acfc60)

~~~json
{
  "source": "00acfc60",
  "target": "00acfca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc70`](#insn-00acfc70)

~~~json
{
  "source": "00acfc70",
  "target": "00676b3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc74`](#insn-00acfc74)

~~~json
{
  "source": "00acfc74",
  "target": "00acfc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc80`](#insn-00acfc80)

~~~json
{
  "source": "00acfc80",
  "target": "00acfc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc8c`](#insn-00acfc8c)

~~~json
{
  "source": "00acfc8c",
  "target": "007bcd04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfc90`](#insn-00acfc90)

~~~json
{
  "source": "00acfc90",
  "target": "00acfc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfc9c`](#insn-00acfc9c)

~~~json
{
  "source": "00acfc9c",
  "target": "008011a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfca8`](#insn-00acfca8)

~~~json
{
  "source": "00acfca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcac`](#insn-00acfcac)

~~~json
{
  "source": "00acfcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcb0`](#insn-00acfcb0)

~~~json
{
  "source": "00acfcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
