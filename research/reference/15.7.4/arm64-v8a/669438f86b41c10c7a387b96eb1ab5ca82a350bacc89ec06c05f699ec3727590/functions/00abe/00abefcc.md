# 00abefcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00abef88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abef88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-a2ed9f6b1d71406432092c80b6cbbe67)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b1ea5c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1e/00b1ea5c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0014.md#compare-49112d6b45ec84757c93a6c296253fa3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abefcc",
  "name": "FUN_00abefcc",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eed80c529ded132fc061ad5c3047d0b8fca4416a91d897be52bf61de01d359e6",
  "source_text_sha256": "eed80c529ded132fc061ad5c3047d0b8fca4416a91d897be52bf61de01d359e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abefcc",
        "00abf0bf"
      ],
      [
        "00abf0c8",
        "00abf0db"
      ]
    ],
    "bytes_sha256": "e77c02aee352a8047439ca6052fc18507eab5c47d77573b45680e88dfed9d10a",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abe1d0](../00abe/00abe1d0.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2063 bytes

~~~c

void FUN_00abefcc(long *param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  void *__ptr;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *__ptr_00;
  ulong uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00abefd8 to 00bbf003 has its CatchHandler @ 00ac529c */
  puVar1 = (undefined8 *)param_1[1];
  __ptr_00 = (undefined8 *)*param_1;
  uVar5 = (long)puVar1 - (long)__ptr_00;
  if (uVar5 < (ulong)(param_1[2] - (long)__ptr_00)) {
    if (puVar1 == __ptr_00) {
      puVar2 = (undefined8 *)0x0;
    }
    else {
                    /* try { // try from 00abf010 to 00bbf04b has its CatchHandler @ 00ac4f6c */
      if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar5 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
        FUN_0041e380();
      }
      puVar2 = (undefined8 *)_Znwm(uVar5);
      uVar5 = (long)puVar2 + uVar5;
      puVar3 = puVar2;
      puVar4 = __ptr_00;
      do {
        uVar6 = *puVar4;
        puVar3[1] = puVar4[1];
        *puVar3 = uVar6;
        puVar3[2] = puVar4[2];
                    /* try { // try from 00abf050 to 00bbf067 has its CatchHandler @ 00ac5268 */
        puVar3 = puVar3 + 3;
        *puVar4 = 0;
        puVar4[1] = 0;
        puVar4[2] = 0;
        puVar4 = puVar4 + 3;
      } while (puVar4 != puVar1);
      do {
        __ptr = (void *)*__ptr_00;
        if (__ptr != (void *)0x0) {
          __ptr_00[1] = __ptr;
          _ZdlPv(__ptr);
        }
        __ptr_00 = __ptr_00 + 3;
                    /* try { // try from 00abf070 to 00bbf09b has its CatchHandler @ 00ac4f58 */
      } while (__ptr_00 != puVar1);
      __ptr_00 = (undefined8 *)*param_1;
    }
    *param_1 = (long)puVar2;
    param_1[1] = uVar5;
    param_1[2] = uVar5;
                    /* try { // try from 00abf0a0 to 00bbf0bb has its CatchHandler @ 00ac5268 */
    if (__ptr_00 != (undefined8 *)0x0) {
      _ZdlPv(__ptr_00);
      return;
    }
  }
                    /* try { // try from 00abf0c8 to 00bbf0ff has its CatchHandler @ 00ac4f64 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abefcc"></a> `00abefcc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00abefd0"></a> `00abefd0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abefd4"></a> `00abefd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abefd8"></a> `00abefd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abefdc"></a> `00abefdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abefe0"></a> `00abefe0` | `17 a0 40 a9` | ldp x23,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00abefe4"></a> `00abefe4` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00abefe8"></a> `00abefe8` | `08 01 13 cb` | sub x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00abefec"></a> `00abefec` | `f5 02 13 cb` | sub x21,x23,x19 | `FALL_THROUGH`
<a id="insn-00abeff0"></a> `00abeff0` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00abeff4"></a> `00abeff4` | `a9 06 00 54` | b.ls 0x00abf0c8 | `CONDITIONAL_JUMP`
<a id="insn-00abeff8"></a> `00abeff8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abeffc"></a> `00abeffc` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00abf000"></a> `00abf000` | `a0 04 00 54` | b.eq 0x00abf094 | `CONDITIONAL_JUMP`
<a id="insn-00abf004"></a> `00abf004` | `a8 fe 43 93` | asr x8,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00abf008"></a> `00abf008` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abf00c"></a> `00abf00c` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abf010"></a> `00abf010` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abf014"></a> `00abf014` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abf018"></a> `00abf018` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abf01c"></a> `00abf01c` | `49 55 e1 f2` | movk x9,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00abf020"></a> `00abf020` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abf024"></a> `00abf024` | `c2 04 00 54` | b.cs 0x00abf0bc | `CONDITIONAL_JUMP`
<a id="insn-00abf028"></a> `00abf028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abf02c"></a> `00abf02c` | `05 70 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00abf030"></a> `00abf030` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00abf034"></a> `00abf034` | `15 00 15 8b` | add x21,x0,x21 | `FALL_THROUGH`
<a id="insn-00abf038"></a> `00abf038` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abf03c"></a> `00abf03c` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-00abf040"></a> `00abf040` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abf044"></a> `00abf044` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00abf048"></a> `00abf048` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abf04c"></a> `00abf04c` | `0a 09 00 f9` | str x10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abf050"></a> `00abf050` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00abf054"></a> `00abf054` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00abf058"></a> `00abf058` | `3f 09 00 f9` | str xzr,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abf05c"></a> `00abf05c` | `29 61 00 91` | add x9,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00abf060"></a> `00abf060` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00abf064"></a> `00abf064` | `e1 fe ff 54` | b.ne 0x00abf040 | `CONDITIONAL_JUMP`
<a id="insn-00abf068"></a> `00abf068` | `04 00 00 14` | b 0x00abf078 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf06c"></a> `00abf06c` | `73 62 00 91` | add x19,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00abf070"></a> `00abf070` | `7f 02 17 eb` | cmp x19,x23 | `FALL_THROUGH`
<a id="insn-00abf074"></a> `00abf074` | `c0 00 00 54` | b.eq 0x00abf08c | `CONDITIONAL_JUMP`
<a id="insn-00abf078"></a> `00abf078` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00abf07c"></a> `00abf07c` | `80 ff ff b4` | cbz x0,0x00abf06c | `CONDITIONAL_JUMP`
<a id="insn-00abf080"></a> `00abf080` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abf084"></a> `00abf084` | `f7 6f 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00abf088"></a> `00abf088` | `f9 ff ff 17` | b 0x00abf06c | `UNCONDITIONAL_JUMP`
<a id="insn-00abf08c"></a> `00abf08c` | `93 02 40 f9` | ldr x19,[x20] | `FALL_THROUGH`
<a id="insn-00abf090"></a> `00abf090` | `02 00 00 14` | b 0x00abf098 | `UNCONDITIONAL_JUMP`
<a id="insn-00abf094"></a> `00abf094` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00abf098"></a> `00abf098` | `96 56 00 a9` | stp x22,x21,[x20] | `FALL_THROUGH`
<a id="insn-00abf09c"></a> `00abf09c` | `95 0a 00 f9` | str x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abf0a0"></a> `00abf0a0` | `53 01 00 b4` | cbz x19,0x00abf0c8 | `CONDITIONAL_JUMP`
<a id="insn-00abf0a4"></a> `00abf0a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abf0a8"></a> `00abf0a8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0ac"></a> `00abf0ac` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abf0b0"></a> `00abf0b0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0b4"></a> `00abf0b4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00abf0b8"></a> `00abf0b8` | `ea 6f 04 14` | b 0x00bdb060 | `CALL_TERMINATOR`
<a id="insn-00abf0bc"></a> `00abf0bc` | `b1 7c e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00abf0c8"></a> `00abf0c8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abf0cc"></a> `00abf0cc` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abf0d0"></a> `00abf0d0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abf0d4"></a> `00abf0d4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00abf0d8"></a> `00abf0d8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abefcc`](#insn-00abefcc) 範囲 `[['00abefcc', '00abefd7']]`
  - `FALL_THROUGH` [`00abefd4`](#insn-00abefd4) → [`00abefd8`](#insn-00abefd8)
- ブロック [`00abefd8`](#insn-00abefd8) 範囲 `[['00abefd8', '00abeff7']]`
  - `CONDITIONAL_JUMP` [`00abeff4`](#insn-00abeff4) → [`00abf0c8`](#insn-00abf0c8)
  - `FALL_THROUGH` [`00abeff4`](#insn-00abeff4) → [`00abeff8`](#insn-00abeff8)
- ブロック [`00abeff8`](#insn-00abeff8) 範囲 `[['00abeff8', '00abf003']]`
  - `CONDITIONAL_JUMP` [`00abf000`](#insn-00abf000) → [`00abf094`](#insn-00abf094)
  - `FALL_THROUGH` [`00abf000`](#insn-00abf000) → [`00abf004`](#insn-00abf004)
- ブロック [`00abf004`](#insn-00abf004) 範囲 `[['00abf004', '00abf00f']]`
  - `FALL_THROUGH` [`00abf00c`](#insn-00abf00c) → [`00abf010`](#insn-00abf010)
- ブロック [`00abf010`](#insn-00abf010) 範囲 `[['00abf010', '00abf027']]`
  - `CONDITIONAL_JUMP` [`00abf024`](#insn-00abf024) → [`00abf0bc`](#insn-00abf0bc)
  - `FALL_THROUGH` [`00abf024`](#insn-00abf024) → [`00abf028`](#insn-00abf028)
- ブロック [`00abf028`](#insn-00abf028) 範囲 `[['00abf028', '00abf03f']]`
  - `FALL_THROUGH` [`00abf03c`](#insn-00abf03c) → [`00abf040`](#insn-00abf040)
- ブロック [`00abf040`](#insn-00abf040) 範囲 `[['00abf040', '00abf04f']]`
  - `FALL_THROUGH` [`00abf04c`](#insn-00abf04c) → [`00abf050`](#insn-00abf050)
- ブロック [`00abf050`](#insn-00abf050) 範囲 `[['00abf050', '00abf067']]`
  - `CONDITIONAL_JUMP` [`00abf064`](#insn-00abf064) → [`00abf040`](#insn-00abf040)
  - `FALL_THROUGH` [`00abf064`](#insn-00abf064) → [`00abf068`](#insn-00abf068)
- ブロック [`00abf068`](#insn-00abf068) 範囲 `[['00abf068', '00abf06b']]`
  - `UNCONDITIONAL_JUMP` [`00abf068`](#insn-00abf068) → [`00abf078`](#insn-00abf078)
- ブロック [`00abf06c`](#insn-00abf06c) 範囲 `[['00abf06c', '00abf06f']]`
  - `FALL_THROUGH` [`00abf06c`](#insn-00abf06c) → [`00abf070`](#insn-00abf070)
- ブロック [`00abf070`](#insn-00abf070) 範囲 `[['00abf070', '00abf077']]`
  - `CONDITIONAL_JUMP` [`00abf074`](#insn-00abf074) → [`00abf08c`](#insn-00abf08c)
  - `FALL_THROUGH` [`00abf074`](#insn-00abf074) → [`00abf078`](#insn-00abf078)
- ブロック [`00abf078`](#insn-00abf078) 範囲 `[['00abf078', '00abf07f']]`
  - `CONDITIONAL_JUMP` [`00abf07c`](#insn-00abf07c) → [`00abf06c`](#insn-00abf06c)
  - `FALL_THROUGH` [`00abf07c`](#insn-00abf07c) → [`00abf080`](#insn-00abf080)
- ブロック [`00abf080`](#insn-00abf080) 範囲 `[['00abf080', '00abf08b']]`
  - `UNCONDITIONAL_JUMP` [`00abf088`](#insn-00abf088) → [`00abf06c`](#insn-00abf06c)
- ブロック [`00abf08c`](#insn-00abf08c) 範囲 `[['00abf08c', '00abf093']]`
  - `UNCONDITIONAL_JUMP` [`00abf090`](#insn-00abf090) → [`00abf098`](#insn-00abf098)
- ブロック [`00abf094`](#insn-00abf094) 範囲 `[['00abf094', '00abf097']]`
  - `FALL_THROUGH` [`00abf094`](#insn-00abf094) → [`00abf098`](#insn-00abf098)
- ブロック [`00abf098`](#insn-00abf098) 範囲 `[['00abf098', '00abf09f']]`
  - `FALL_THROUGH` [`00abf09c`](#insn-00abf09c) → [`00abf0a0`](#insn-00abf0a0)
- ブロック [`00abf0a0`](#insn-00abf0a0) 範囲 `[['00abf0a0', '00abf0a3']]`
  - `CONDITIONAL_JUMP` [`00abf0a0`](#insn-00abf0a0) → [`00abf0c8`](#insn-00abf0c8)
  - `FALL_THROUGH` [`00abf0a0`](#insn-00abf0a0) → [`00abf0a4`](#insn-00abf0a4)
- ブロック [`00abf0a4`](#insn-00abf0a4) 範囲 `[['00abf0a4', '00abf0bb']]`
- ブロック [`00abf0bc`](#insn-00abf0bc) 範囲 `[['00abf0bc', '00abf0bf']]`
- ブロック [`00abf0c8`](#insn-00abf0c8) 範囲 `[['00abf0c8', '00abf0db']]`

## 命令位置別の参照

- [`00abefcc`](#insn-00abefcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefd0`](#insn-00abefd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefd4`](#insn-00abefd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefd8`](#insn-00abefd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeff4`](#insn-00abeff4) → [`00abf0c8`](#insn-00abf0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf000`](#insn-00abf000) → [`00abf094`](#insn-00abf094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf024`](#insn-00abf024) → [`00abf0bc`](#insn-00abf0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf02c`](#insn-00abf02c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00abf064`](#insn-00abf064) → [`00abf040`](#insn-00abf040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf068`](#insn-00abf068) → [`00abf078`](#insn-00abf078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf074`](#insn-00abf074) → [`00abf08c`](#insn-00abf08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf07c`](#insn-00abf07c) → [`00abf06c`](#insn-00abf06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf084`](#insn-00abf084) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00abf088`](#insn-00abf088) → [`00abf06c`](#insn-00abf06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf090`](#insn-00abf090) → [`00abf098`](#insn-00abf098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a0`](#insn-00abf0a0) → [`00abf0c8`](#insn-00abf0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0a8`](#insn-00abf0a8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0ac`](#insn-00abf0ac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0b0`](#insn-00abf0b0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0b4`](#insn-00abf0b4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0b8`](#insn-00abf0b8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00abf0bc`](#insn-00abf0bc) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00abf0c8`](#insn-00abf0c8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0cc`](#insn-00abf0cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0d0`](#insn-00abf0d0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abf0d4`](#insn-00abf0d4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abefcc`](#insn-00abefcc)

~~~json
{
  "source": "00abefcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefd0`](#insn-00abefd0)

~~~json
{
  "source": "00abefd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefd4`](#insn-00abefd4)

~~~json
{
  "source": "00abefd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefd8`](#insn-00abefd8)

~~~json
{
  "source": "00abefd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeff4`](#insn-00abeff4)

~~~json
{
  "source": "00abeff4",
  "target": "00abf0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf000`](#insn-00abf000)

~~~json
{
  "source": "00abf000",
  "target": "00abf094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf024`](#insn-00abf024)

~~~json
{
  "source": "00abf024",
  "target": "00abf0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf02c`](#insn-00abf02c)

~~~json
{
  "source": "00abf02c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf064`](#insn-00abf064)

~~~json
{
  "source": "00abf064",
  "target": "00abf040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf068`](#insn-00abf068)

~~~json
{
  "source": "00abf068",
  "target": "00abf078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf074`](#insn-00abf074)

~~~json
{
  "source": "00abf074",
  "target": "00abf08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf07c`](#insn-00abf07c)

~~~json
{
  "source": "00abf07c",
  "target": "00abf06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf084`](#insn-00abf084)

~~~json
{
  "source": "00abf084",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf088`](#insn-00abf088)

~~~json
{
  "source": "00abf088",
  "target": "00abf06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf090`](#insn-00abf090)

~~~json
{
  "source": "00abf090",
  "target": "00abf098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a0`](#insn-00abf0a0)

~~~json
{
  "source": "00abf0a0",
  "target": "00abf0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0a8`](#insn-00abf0a8)

~~~json
{
  "source": "00abf0a8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0ac`](#insn-00abf0ac)

~~~json
{
  "source": "00abf0ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0b0`](#insn-00abf0b0)

~~~json
{
  "source": "00abf0b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0b4`](#insn-00abf0b4)

~~~json
{
  "source": "00abf0b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0b8`](#insn-00abf0b8)

~~~json
{
  "source": "00abf0b8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0bc`](#insn-00abf0bc)

~~~json
{
  "source": "00abf0bc",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abf0c8`](#insn-00abf0c8)

~~~json
{
  "source": "00abf0c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0cc`](#insn-00abf0cc)

~~~json
{
  "source": "00abf0cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0d0`](#insn-00abf0d0)

~~~json
{
  "source": "00abf0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abf0d4`](#insn-00abf0d4)

~~~json
{
  "source": "00abf0d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
