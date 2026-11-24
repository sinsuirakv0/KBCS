# 00b3bfac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b3afb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3a/00b3afb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0031.md#compare-c7010d0416728bcaae5b52ca5e6c7dd4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3bfac",
  "name": "FUN_00b3bfac",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a711561be0e9413fb360f6317e63e0bda80508af5ec4f8f184b9d33fcf0ab15e",
  "source_text_sha256": "a711561be0e9413fb360f6317e63e0bda80508af5ec4f8f184b9d33fcf0ab15e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3bfac",
        "00b3c08b"
      ]
    ],
    "bytes_sha256": "1427a11e8180102a9de47d12b30ef4f449740a1e1f215c78caba346c73979dde",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00b39f98](../00b39/00b39f98.md)
- [00b3bfac](../00b3b/00b3bfac.md)

## 呼び出し先

- [00b3bfac](../00b3b/00b3bfac.md)
- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1800 bytes

~~~c

void FUN_00b3bfac(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
                    /* try { // try from 00b3bfb4 to 00c3bfc3 has its CatchHandler @ 00b3c0c0 */
                    /* try { // try from 00b3bfc8 to 00c3bfdf has its CatchHandler @ 00b3c0a8 */
  FUN_00b3bfac(param_1,*param_2);
  FUN_00b3bfac(param_1,param_2[1]);
  plVar1 = (long *)param_2[0x18];
  plVar3 = param_2 + 0x14;
  if (plVar1 == plVar3) {
    lVar4 = 0x20;
                    /* try { // try from 00b3bffc to 00c3c027 has its CatchHandler @ 00b3c0d0 */
LAB_00b3c000:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar1;
    goto LAB_00b3c000;
  }
  plVar2 = (long *)param_2[0x12];
  plVar3 = param_2 + 0xe;
  plVar1 = param_2 + 8;
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
LAB_00b3c034:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar2 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar2;
    goto LAB_00b3c034;
  }
  plVar3 = (long *)param_2[0xc];
  if (plVar3 == plVar1) {
    lVar4 = 0x20;
  }
  else {
    if (plVar3 == (long *)0x0) goto LAB_00b3c06c;
    lVar4 = 0x28;
    plVar1 = plVar3;
  }
  (**(code **)(*plVar1 + lVar4))();
LAB_00b3c06c:
                    /* try { // try from 00b3c070 to 00c3c077 has its CatchHandler @ 00b3c07c */
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* catch() { ... } // from try @ 00b3bdc8 with catch @ 00b3c078
                       try { // try from 00b3c078 to 00c3c103 has its CatchHandler @ 00b3bb10 */
    _ZdlPv((void *)param_2[6]);
  }
                    /* catch() { ... } // from try @ 00b3c070 with catch @ 00b3c07c */
  _ZdlPv(param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3bfac"></a> `00b3bfac` | `41 02 00 b4` | cbz x1,0x00b3bff4 | `CONDITIONAL_JUMP`
<a id="insn-00b3bfb0"></a> `00b3bfb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b3bfb4"></a> `00b3bfb4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3bfb8"></a> `00b3bfb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b3bfbc"></a> `00b3bfbc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b3bfc0"></a> `00b3bfc0` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00b3bfc4"></a> `00b3bfc4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b3bfc8"></a> `00b3bfc8` | `f9 ff ff 97` | bl 0x00b3bfac | `UNCONDITIONAL_CALL`
<a id="insn-00b3bfcc"></a> `00b3bfcc` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b3bfd0"></a> `00b3bfd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3bfd4"></a> `00b3bfd4` | `f6 ff ff 97` | bl 0x00b3bfac | `UNCONDITIONAL_CALL`
<a id="insn-00b3bfd8"></a> `00b3bfd8` | `60 62 40 f9` | ldr x0,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00b3bfdc"></a> `00b3bfdc` | `69 82 02 91` | add x9,x19,#0xa0 | `FALL_THROUGH`
<a id="insn-00b3bfe0"></a> `00b3bfe0` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00b3bfe4"></a> `00b3bfe4` | `a0 00 00 54` | b.eq 0x00b3bff8 | `CONDITIONAL_JUMP`
<a id="insn-00b3bfe8"></a> `00b3bfe8` | `20 01 00 b4` | cbz x0,0x00b3c00c | `CONDITIONAL_JUMP`
<a id="insn-00b3bfec"></a> `00b3bfec` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3bff0"></a> `00b3bff0` | `04 00 00 14` | b 0x00b3c000 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3bff4"></a> `00b3bff4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b3bff8"></a> `00b3bff8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3bffc"></a> `00b3bffc` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00b3c000"></a> `00b3c000` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3c004"></a> `00b3c004` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3c008"></a> `00b3c008` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3c00c"></a> `00b3c00c` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00b3c010"></a> `00b3c010` | `69 c2 01 91` | add x9,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00b3c014"></a> `00b3c014` | `74 02 01 91` | add x20,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00b3c018"></a> `00b3c018` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00b3c01c"></a> `00b3c01c` | `80 00 00 54` | b.eq 0x00b3c02c | `CONDITIONAL_JUMP`
<a id="insn-00b3c020"></a> `00b3c020` | `00 01 00 b4` | cbz x0,0x00b3c040 | `CONDITIONAL_JUMP`
<a id="insn-00b3c024"></a> `00b3c024` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3c028"></a> `00b3c028` | `03 00 00 14` | b 0x00b3c034 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3c02c"></a> `00b3c02c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3c030"></a> `00b3c030` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00b3c034"></a> `00b3c034` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3c038"></a> `00b3c038` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3c03c"></a> `00b3c03c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3c040"></a> `00b3c040` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00b3c044"></a> `00b3c044` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00b3c048"></a> `00b3c048` | `80 00 00 54` | b.eq 0x00b3c058 | `CONDITIONAL_JUMP`
<a id="insn-00b3c04c"></a> `00b3c04c` | `00 01 00 b4` | cbz x0,0x00b3c06c | `CONDITIONAL_JUMP`
<a id="insn-00b3c050"></a> `00b3c050` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00b3c054"></a> `00b3c054` | `03 00 00 14` | b 0x00b3c060 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3c058"></a> `00b3c058` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00b3c05c"></a> `00b3c05c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b3c060"></a> `00b3c060` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00b3c064"></a> `00b3c064` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00b3c068"></a> `00b3c068` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b3c06c"></a> `00b3c06c` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b3c070"></a> `00b3c070` | `68 00 00 36` | tbz w8,#0x0,0x00b3c07c | `CONDITIONAL_JUMP`
<a id="insn-00b3c074"></a> `00b3c074` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b3c078"></a> `00b3c078` | `b6 73 04 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b3c07c"></a> `00b3c07c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b3c080"></a> `00b3c080` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3c084"></a> `00b3c084` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b3c088"></a> `00b3c088` | `b2 73 04 14` | b 0x00c58f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3bfac`](#insn-00b3bfac) 範囲 `[['00b3bfac', '00b3bfaf']]`
  - `CONDITIONAL_JUMP` [`00b3bfac`](#insn-00b3bfac) → [`00b3bff4`](#insn-00b3bff4)
  - `FALL_THROUGH` [`00b3bfac`](#insn-00b3bfac) → [`00b3bfb0`](#insn-00b3bfb0)
- ブロック [`00b3bfb0`](#insn-00b3bfb0) 範囲 `[['00b3bfb0', '00b3bfb3']]`
  - `FALL_THROUGH` [`00b3bfb0`](#insn-00b3bfb0) → [`00b3bfb4`](#insn-00b3bfb4)
- ブロック [`00b3bfb4`](#insn-00b3bfb4) 範囲 `[['00b3bfb4', '00b3bfc7']]`
  - `FALL_THROUGH` [`00b3bfc4`](#insn-00b3bfc4) → [`00b3bfc8`](#insn-00b3bfc8)
- ブロック [`00b3bfc8`](#insn-00b3bfc8) 範囲 `[['00b3bfc8', '00b3bfe7']]`
  - `CONDITIONAL_JUMP` [`00b3bfe4`](#insn-00b3bfe4) → [`00b3bff8`](#insn-00b3bff8)
  - `FALL_THROUGH` [`00b3bfe4`](#insn-00b3bfe4) → [`00b3bfe8`](#insn-00b3bfe8)
- ブロック [`00b3bfe8`](#insn-00b3bfe8) 範囲 `[['00b3bfe8', '00b3bfeb']]`
  - `CONDITIONAL_JUMP` [`00b3bfe8`](#insn-00b3bfe8) → [`00b3c00c`](#insn-00b3c00c)
  - `FALL_THROUGH` [`00b3bfe8`](#insn-00b3bfe8) → [`00b3bfec`](#insn-00b3bfec)
- ブロック [`00b3bfec`](#insn-00b3bfec) 範囲 `[['00b3bfec', '00b3bff3']]`
  - `UNCONDITIONAL_JUMP` [`00b3bff0`](#insn-00b3bff0) → [`00b3c000`](#insn-00b3c000)
- ブロック [`00b3bff4`](#insn-00b3bff4) 範囲 `[['00b3bff4', '00b3bff7']]`
- ブロック [`00b3bff8`](#insn-00b3bff8) 範囲 `[['00b3bff8', '00b3bffb']]`
  - `FALL_THROUGH` [`00b3bff8`](#insn-00b3bff8) → [`00b3bffc`](#insn-00b3bffc)
- ブロック [`00b3bffc`](#insn-00b3bffc) 範囲 `[['00b3bffc', '00b3bfff']]`
  - `FALL_THROUGH` [`00b3bffc`](#insn-00b3bffc) → [`00b3c000`](#insn-00b3c000)
- ブロック [`00b3c000`](#insn-00b3c000) 範囲 `[['00b3c000', '00b3c00b']]`
  - `FALL_THROUGH` [`00b3c008`](#insn-00b3c008) → [`00b3c00c`](#insn-00b3c00c)
- ブロック [`00b3c00c`](#insn-00b3c00c) 範囲 `[['00b3c00c', '00b3c01f']]`
  - `CONDITIONAL_JUMP` [`00b3c01c`](#insn-00b3c01c) → [`00b3c02c`](#insn-00b3c02c)
  - `FALL_THROUGH` [`00b3c01c`](#insn-00b3c01c) → [`00b3c020`](#insn-00b3c020)
- ブロック [`00b3c020`](#insn-00b3c020) 範囲 `[['00b3c020', '00b3c023']]`
  - `CONDITIONAL_JUMP` [`00b3c020`](#insn-00b3c020) → [`00b3c040`](#insn-00b3c040)
  - `FALL_THROUGH` [`00b3c020`](#insn-00b3c020) → [`00b3c024`](#insn-00b3c024)
- ブロック [`00b3c024`](#insn-00b3c024) 範囲 `[['00b3c024', '00b3c02b']]`
  - `UNCONDITIONAL_JUMP` [`00b3c028`](#insn-00b3c028) → [`00b3c034`](#insn-00b3c034)
- ブロック [`00b3c02c`](#insn-00b3c02c) 範囲 `[['00b3c02c', '00b3c033']]`
  - `FALL_THROUGH` [`00b3c030`](#insn-00b3c030) → [`00b3c034`](#insn-00b3c034)
- ブロック [`00b3c034`](#insn-00b3c034) 範囲 `[['00b3c034', '00b3c03f']]`
  - `FALL_THROUGH` [`00b3c03c`](#insn-00b3c03c) → [`00b3c040`](#insn-00b3c040)
- ブロック [`00b3c040`](#insn-00b3c040) 範囲 `[['00b3c040', '00b3c04b']]`
  - `CONDITIONAL_JUMP` [`00b3c048`](#insn-00b3c048) → [`00b3c058`](#insn-00b3c058)
  - `FALL_THROUGH` [`00b3c048`](#insn-00b3c048) → [`00b3c04c`](#insn-00b3c04c)
- ブロック [`00b3c04c`](#insn-00b3c04c) 範囲 `[['00b3c04c', '00b3c04f']]`
  - `CONDITIONAL_JUMP` [`00b3c04c`](#insn-00b3c04c) → [`00b3c06c`](#insn-00b3c06c)
  - `FALL_THROUGH` [`00b3c04c`](#insn-00b3c04c) → [`00b3c050`](#insn-00b3c050)
- ブロック [`00b3c050`](#insn-00b3c050) 範囲 `[['00b3c050', '00b3c057']]`
  - `UNCONDITIONAL_JUMP` [`00b3c054`](#insn-00b3c054) → [`00b3c060`](#insn-00b3c060)
- ブロック [`00b3c058`](#insn-00b3c058) 範囲 `[['00b3c058', '00b3c05f']]`
  - `FALL_THROUGH` [`00b3c05c`](#insn-00b3c05c) → [`00b3c060`](#insn-00b3c060)
- ブロック [`00b3c060`](#insn-00b3c060) 範囲 `[['00b3c060', '00b3c06b']]`
  - `FALL_THROUGH` [`00b3c068`](#insn-00b3c068) → [`00b3c06c`](#insn-00b3c06c)
- ブロック [`00b3c06c`](#insn-00b3c06c) 範囲 `[['00b3c06c', '00b3c06f']]`
  - `FALL_THROUGH` [`00b3c06c`](#insn-00b3c06c) → [`00b3c070`](#insn-00b3c070)
- ブロック [`00b3c070`](#insn-00b3c070) 範囲 `[['00b3c070', '00b3c073']]`
  - `CONDITIONAL_JUMP` [`00b3c070`](#insn-00b3c070) → [`00b3c07c`](#insn-00b3c07c)
  - `FALL_THROUGH` [`00b3c070`](#insn-00b3c070) → [`00b3c074`](#insn-00b3c074)
- ブロック [`00b3c074`](#insn-00b3c074) 範囲 `[['00b3c074', '00b3c077']]`
  - `FALL_THROUGH` [`00b3c074`](#insn-00b3c074) → [`00b3c078`](#insn-00b3c078)
- ブロック [`00b3c078`](#insn-00b3c078) 範囲 `[['00b3c078', '00b3c07b']]`
  - `FALL_THROUGH` [`00b3c078`](#insn-00b3c078) → [`00b3c07c`](#insn-00b3c07c)
- ブロック [`00b3c07c`](#insn-00b3c07c) 範囲 `[['00b3c07c', '00b3c08b']]`

## 命令位置別の参照

- [`00b3bfac`](#insn-00b3bfac) → [`00b3bff4`](#insn-00b3bff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfb0`](#insn-00b3bfb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfb4`](#insn-00b3bfb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfc8`](#insn-00b3bfc8) → [`00b3bfac`](#insn-00b3bfac) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bfac` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfd4`](#insn-00b3bfd4) → [`00b3bfac`](#insn-00b3bfac) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bfac` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfe4`](#insn-00b3bfe4) → [`00b3bff8`](#insn-00b3bff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bfe8`](#insn-00b3bfe8) → [`00b3c00c`](#insn-00b3c00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bff0`](#insn-00b3bff0) → [`00b3c000`](#insn-00b3c000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c01c`](#insn-00b3c01c) → [`00b3c02c`](#insn-00b3c02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c020`](#insn-00b3c020) → [`00b3c040`](#insn-00b3c040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c028`](#insn-00b3c028) → [`00b3c034`](#insn-00b3c034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c048`](#insn-00b3c048) → [`00b3c058`](#insn-00b3c058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c04c`](#insn-00b3c04c) → [`00b3c06c`](#insn-00b3c06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c054`](#insn-00b3c054) → [`00b3c060`](#insn-00b3c060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c070`](#insn-00b3c070) → [`00b3c07c`](#insn-00b3c07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c078`](#insn-00b3c078) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b3c080`](#insn-00b3c080) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c084`](#insn-00b3c084) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3c088`](#insn-00b3c088) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3bfac`](#insn-00b3bfac)

~~~json
{
  "source": "00b3bfac",
  "target": "00b3bff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bfb0`](#insn-00b3bfb0)

~~~json
{
  "source": "00b3bfb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bfb4`](#insn-00b3bfb4)

~~~json
{
  "source": "00b3bfb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bfc8`](#insn-00b3bfc8)

~~~json
{
  "source": "00b3bfc8",
  "target": "00b3bfac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bfd4`](#insn-00b3bfd4)

~~~json
{
  "source": "00b3bfd4",
  "target": "00b3bfac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bfe4`](#insn-00b3bfe4)

~~~json
{
  "source": "00b3bfe4",
  "target": "00b3bff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bfe8`](#insn-00b3bfe8)

~~~json
{
  "source": "00b3bfe8",
  "target": "00b3c00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bff0`](#insn-00b3bff0)

~~~json
{
  "source": "00b3bff0",
  "target": "00b3c000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c01c`](#insn-00b3c01c)

~~~json
{
  "source": "00b3c01c",
  "target": "00b3c02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c020`](#insn-00b3c020)

~~~json
{
  "source": "00b3c020",
  "target": "00b3c040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c028`](#insn-00b3c028)

~~~json
{
  "source": "00b3c028",
  "target": "00b3c034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c048`](#insn-00b3c048)

~~~json
{
  "source": "00b3c048",
  "target": "00b3c058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c04c`](#insn-00b3c04c)

~~~json
{
  "source": "00b3c04c",
  "target": "00b3c06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c054`](#insn-00b3c054)

~~~json
{
  "source": "00b3c054",
  "target": "00b3c060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c070`](#insn-00b3c070)

~~~json
{
  "source": "00b3c070",
  "target": "00b3c07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c078`](#insn-00b3c078)

~~~json
{
  "source": "00b3c078",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3c080`](#insn-00b3c080)

~~~json
{
  "source": "00b3c080",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c084`](#insn-00b3c084)

~~~json
{
  "source": "00b3c084",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3c088`](#insn-00b3c088)

~~~json
{
  "source": "00b3c088",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
