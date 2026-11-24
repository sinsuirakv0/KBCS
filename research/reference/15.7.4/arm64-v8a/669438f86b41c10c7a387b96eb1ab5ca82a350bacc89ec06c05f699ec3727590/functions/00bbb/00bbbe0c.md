# 00bbbe0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbbdc8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-d209222d6d6441168c05e7571dee1561)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c38854`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c38854.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-4a05f047102c7bc22ac48cd473ba37de)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbe0c",
  "name": "FUN_00bbbe0c",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97e55b9bb733a0587a8602cb3fd49961dc308f1eb225d9a7822ca891104bebe6",
  "source_text_sha256": "97e55b9bb733a0587a8602cb3fd49961dc308f1eb225d9a7822ca891104bebe6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbe0c",
        "00bbbeff"
      ]
    ],
    "bytes_sha256": "d600faa1c0b8bb62885ed866525295f9ea637da133f1a78f8116799cbee0f16c",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbbb50](../00bbb/00bbbb50.md)

## 呼び出し先

- [00bbbf00](../00bbb/00bbbf00.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1347 bytes

~~~c

undefined8 FUN_00bbbe0c(long param_1,long param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  
  puVar2 = PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c068;
  puVar1 = PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048;
  while( true ) {
    if (param_2 == 0) {
      return 0;
    }
    lVar3 = __dynamic_cast(param_2,puVar1,puVar2,0);
    if (lVar3 == 0) {
      return 0;
    }
    if ((*(uint *)(lVar3 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) != 0) {
      return 0;
    }
    lVar5 = *(long *)(param_1 + 0x18);
    param_2 = *(long *)(lVar3 + 0x18);
    if (*(long *)(lVar5 + 8) == *(long *)(param_2 + 8)) break;
    if ((*(uint *)(param_1 + 0x10) & 1) == 0) {
      return 0;
    }
    param_1 = __dynamic_cast(lVar5,puVar1,puVar2,0);
    if (param_1 == 0) {
      lVar3 = __dynamic_cast(lVar5,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c080,0);
                    /* try { // try from 00bbbebc to 00cbbec3 has its CatchHandler @ 00bbd32c */
      if (lVar3 != 0) {
        uVar4 = FUN_00bbbf00(lVar3,param_2);
        return uVar4;
      }
                    /* try { // try from 00bbbeec to 00cbbeff has its CatchHandler @ 00bbd1f0 */
      return 0;
    }
  }
  return 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbe0c"></a> `00bbbe0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbe10"></a> `00bbbe10` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbbe14"></a> `00bbbe14` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe18"></a> `00bbbe18` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbe1c"></a> `00bbbe1c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbe20"></a> `00bbbe20` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbe24"></a> `00bbbe24` | `14 03 00 b0` | adrp x20,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbe28"></a> `00bbbe28` | `15 03 00 b0` | adrp x21,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbe2c"></a> `00bbbe2c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbbe30"></a> `00bbbe30` | `94 26 40 f9` | ldr x20,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bbbe34"></a> `00bbbe34` | `b5 36 40 f9` | ldr x21,[x21, #0x68] | `FALL_THROUGH`
<a id="insn-00bbbe38"></a> `00bbbe38` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbbe3c"></a> `00bbbe3c` | `13 05 00 b4` | cbz x19,0x00bbbedc | `CONDITIONAL_JUMP`
<a id="insn-00bbbe40"></a> `00bbbe40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe44"></a> `00bbbe44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbe48"></a> `00bbbe48` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bbbe4c"></a> `00bbbe4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe50"></a> `00bbbe50` | `5c 7e 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe54"></a> `00bbbe54` | `a0 04 00 b4` | cbz x0,0x00bbbee8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe58"></a> `00bbbe58` | `09 10 40 b9` | ldr w9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe5c"></a> `00bbbe5c` | `e8 12 40 b9` | ldr w8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe60"></a> `00bbbe60` | `3f 01 28 6a` | bics wzr,w9,w8 | `FALL_THROUGH`
<a id="insn-00bbbe64"></a> `00bbbe64` | `c1 03 00 54` | b.ne 0x00bbbedc | `CONDITIONAL_JUMP`
<a id="insn-00bbbe68"></a> `00bbbe68` | `f6 0e 40 f9` | ldr x22,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe6c"></a> `00bbbe6c` | `13 0c 40 f9` | ldr x19,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe70"></a> `00bbbe70` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe74"></a> `00bbbe74` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe78"></a> `00bbbe78` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbbe7c"></a> `00bbbe7c` | `40 03 00 54` | b.eq 0x00bbbee4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe80"></a> `00bbbe80` | `e8 02 00 36` | tbz w8,#0x0,0x00bbbedc | `CONDITIONAL_JUMP`
<a id="insn-00bbbe84"></a> `00bbbe84` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbe88"></a> `00bbbe88` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbe8c"></a> `00bbbe8c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bbbe90"></a> `00bbbe90` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe94"></a> `00bbbe94` | `4b 7e 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe98"></a> `00bbbe98` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbbe9c"></a> `00bbbe9c` | `00 fd ff b5` | cbnz x0,0x00bbbe3c | `CONDITIONAL_JUMP`
<a id="insn-00bbbea0"></a> `00bbbea0` | `01 03 00 b0` | adrp x1,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbea4"></a> `00bbbea4` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbea8"></a> `00bbbea8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbeac"></a> `00bbbeac` | `21 24 40 f9` | ldr x1,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbbeb0"></a> `00bbbeb0` | `42 40 40 f9` | ldr x2,[x2, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbeb4"></a> `00bbbeb4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbeb8"></a> `00bbbeb8` | `42 7e 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbebc"></a> `00bbbebc` | `60 01 00 b4` | cbz x0,0x00bbbee8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbec0"></a> `00bbbec0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbbec4"></a> `00bbbec4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbec8"></a> `00bbbec8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbecc"></a> `00bbbecc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbed0"></a> `00bbbed0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbbed4"></a> `00bbbed4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbed8"></a> `00bbbed8` | `0a 00 00 14` | b 0x00bbbf00 | `CALL_TERMINATOR`
<a id="insn-00bbbedc"></a> `00bbbedc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbee0"></a> `00bbbee0` | `02 00 00 14` | b 0x00bbbee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbee4"></a> `00bbbee4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbee8"></a> `00bbbee8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbeec"></a> `00bbbeec` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbef0"></a> `00bbbef0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbef4"></a> `00bbbef4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbbef8"></a> `00bbbef8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbefc"></a> `00bbbefc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbe0c`](#insn-00bbbe0c) 範囲 `[['00bbbe0c', '00bbbe3b']]`
  - `FALL_THROUGH` [`00bbbe38`](#insn-00bbbe38) → [`00bbbe3c`](#insn-00bbbe3c)
- ブロック [`00bbbe3c`](#insn-00bbbe3c) 範囲 `[['00bbbe3c', '00bbbe3f']]`
  - `CONDITIONAL_JUMP` [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbedc`](#insn-00bbbedc)
  - `FALL_THROUGH` [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbe40`](#insn-00bbbe40)
- ブロック [`00bbbe40`](#insn-00bbbe40) 範囲 `[['00bbbe40', '00bbbe57']]`
  - `CONDITIONAL_JUMP` [`00bbbe54`](#insn-00bbbe54) → [`00bbbee8`](#insn-00bbbee8)
  - `FALL_THROUGH` [`00bbbe54`](#insn-00bbbe54) → [`00bbbe58`](#insn-00bbbe58)
- ブロック [`00bbbe58`](#insn-00bbbe58) 範囲 `[['00bbbe58', '00bbbe67']]`
  - `CONDITIONAL_JUMP` [`00bbbe64`](#insn-00bbbe64) → [`00bbbedc`](#insn-00bbbedc)
  - `FALL_THROUGH` [`00bbbe64`](#insn-00bbbe64) → [`00bbbe68`](#insn-00bbbe68)
- ブロック [`00bbbe68`](#insn-00bbbe68) 範囲 `[['00bbbe68', '00bbbe7f']]`
  - `CONDITIONAL_JUMP` [`00bbbe7c`](#insn-00bbbe7c) → [`00bbbee4`](#insn-00bbbee4)
  - `FALL_THROUGH` [`00bbbe7c`](#insn-00bbbe7c) → [`00bbbe80`](#insn-00bbbe80)
- ブロック [`00bbbe80`](#insn-00bbbe80) 範囲 `[['00bbbe80', '00bbbe83']]`
  - `CONDITIONAL_JUMP` [`00bbbe80`](#insn-00bbbe80) → [`00bbbedc`](#insn-00bbbedc)
  - `FALL_THROUGH` [`00bbbe80`](#insn-00bbbe80) → [`00bbbe84`](#insn-00bbbe84)
- ブロック [`00bbbe84`](#insn-00bbbe84) 範囲 `[['00bbbe84', '00bbbe9f']]`
  - `CONDITIONAL_JUMP` [`00bbbe9c`](#insn-00bbbe9c) → [`00bbbe3c`](#insn-00bbbe3c)
  - `FALL_THROUGH` [`00bbbe9c`](#insn-00bbbe9c) → [`00bbbea0`](#insn-00bbbea0)
- ブロック [`00bbbea0`](#insn-00bbbea0) 範囲 `[['00bbbea0', '00bbbebb']]`
  - `FALL_THROUGH` [`00bbbeb8`](#insn-00bbbeb8) → [`00bbbebc`](#insn-00bbbebc)
- ブロック [`00bbbebc`](#insn-00bbbebc) 範囲 `[['00bbbebc', '00bbbebf']]`
  - `CONDITIONAL_JUMP` [`00bbbebc`](#insn-00bbbebc) → [`00bbbee8`](#insn-00bbbee8)
  - `FALL_THROUGH` [`00bbbebc`](#insn-00bbbebc) → [`00bbbec0`](#insn-00bbbec0)
- ブロック [`00bbbec0`](#insn-00bbbec0) 範囲 `[['00bbbec0', '00bbbedb']]`
- ブロック [`00bbbedc`](#insn-00bbbedc) 範囲 `[['00bbbedc', '00bbbee3']]`
  - `UNCONDITIONAL_JUMP` [`00bbbee0`](#insn-00bbbee0) → [`00bbbee8`](#insn-00bbbee8)
- ブロック [`00bbbee4`](#insn-00bbbee4) 範囲 `[['00bbbee4', '00bbbee7']]`
  - `FALL_THROUGH` [`00bbbee4`](#insn-00bbbee4) → [`00bbbee8`](#insn-00bbbee8)
- ブロック [`00bbbee8`](#insn-00bbbee8) 範囲 `[['00bbbee8', '00bbbeeb']]`
  - `FALL_THROUGH` [`00bbbee8`](#insn-00bbbee8) → [`00bbbeec`](#insn-00bbbeec)
- ブロック [`00bbbeec`](#insn-00bbbeec) 範囲 `[['00bbbeec', '00bbbeff']]`

## 命令位置別の参照

- [`00bbbe10`](#insn-00bbbe10) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe14`](#insn-00bbbe14) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe18`](#insn-00bbbe18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe1c`](#insn-00bbbe1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe30`](#insn-00bbbe30) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe34`](#insn-00bbbe34) → `00c1c068`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbedc`](#insn-00bbbedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe44`](#insn-00bbbe44) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe48`](#insn-00bbbe48) → `00c16c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe50`](#insn-00bbbe50) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe54`](#insn-00bbbe54) → [`00bbbee8`](#insn-00bbbee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe64`](#insn-00bbbe64) → [`00bbbedc`](#insn-00bbbedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe7c`](#insn-00bbbe7c) → [`00bbbee4`](#insn-00bbbee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe80`](#insn-00bbbe80) → [`00bbbedc`](#insn-00bbbedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe88`](#insn-00bbbe88) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe8c`](#insn-00bbbe8c) → `00c16c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe94`](#insn-00bbbe94) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe9c`](#insn-00bbbe9c) → [`00bbbe3c`](#insn-00bbbe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeac`](#insn-00bbbeac) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbeac`](#insn-00bbbeac) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbeb0`](#insn-00bbbeb0) → `00c1c080`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbeb0`](#insn-00bbbeb0) → `00c16c88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbeb8`](#insn-00bbbeb8) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbebc`](#insn-00bbbebc) → [`00bbbee8`](#insn-00bbbee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbec4`](#insn-00bbbec4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbec8`](#insn-00bbbec8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbecc`](#insn-00bbbecc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbed0`](#insn-00bbbed0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbed8`](#insn-00bbbed8) → [`00bbbf00`](00bbbf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbbf00` · 推定シンボル `None` · 推定型 `None`
- [`00bbbee0`](#insn-00bbbee0) → [`00bbbee8`](#insn-00bbbee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbee8`](#insn-00bbbee8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeec`](#insn-00bbbeec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbef0`](#insn-00bbbef0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbef4`](#insn-00bbbef4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbe10`](#insn-00bbbe10)

~~~json
{
  "source": "00bbbe10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe14`](#insn-00bbbe14)

~~~json
{
  "source": "00bbbe14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe18`](#insn-00bbbe18)

~~~json
{
  "source": "00bbbe18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe1c`](#insn-00bbbe1c)

~~~json
{
  "source": "00bbbe1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe30`](#insn-00bbbe30)

~~~json
{
  "source": "00bbbe30",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe34`](#insn-00bbbe34)

~~~json
{
  "source": "00bbbe34",
  "target": "00c1c068",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c068",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe3c`](#insn-00bbbe3c)

~~~json
{
  "source": "00bbbe3c",
  "target": "00bbbedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe44`](#insn-00bbbe44)

~~~json
{
  "source": "00bbbe44",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe48`](#insn-00bbbe48)

~~~json
{
  "source": "00bbbe48",
  "target": "00c16c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe50`](#insn-00bbbe50)

~~~json
{
  "source": "00bbbe50",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe54`](#insn-00bbbe54)

~~~json
{
  "source": "00bbbe54",
  "target": "00bbbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe64`](#insn-00bbbe64)

~~~json
{
  "source": "00bbbe64",
  "target": "00bbbedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe7c`](#insn-00bbbe7c)

~~~json
{
  "source": "00bbbe7c",
  "target": "00bbbee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe80`](#insn-00bbbe80)

~~~json
{
  "source": "00bbbe80",
  "target": "00bbbedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe88`](#insn-00bbbe88)

~~~json
{
  "source": "00bbbe88",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe8c`](#insn-00bbbe8c)

~~~json
{
  "source": "00bbbe8c",
  "target": "00c16c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe94`](#insn-00bbbe94)

~~~json
{
  "source": "00bbbe94",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe9c`](#insn-00bbbe9c)

~~~json
{
  "source": "00bbbe9c",
  "target": "00bbbe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeac`](#insn-00bbbeac)

~~~json
{
  "source": "00bbbeac",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbeac`](#insn-00bbbeac)

~~~json
{
  "source": "00bbbeac",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbeb0`](#insn-00bbbeb0)

~~~json
{
  "source": "00bbbeb0",
  "target": "00c1c080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c080",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbeb0`](#insn-00bbbeb0)

~~~json
{
  "source": "00bbbeb0",
  "target": "00c16c88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbeb8`](#insn-00bbbeb8)

~~~json
{
  "source": "00bbbeb8",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbebc`](#insn-00bbbebc)

~~~json
{
  "source": "00bbbebc",
  "target": "00bbbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbec4`](#insn-00bbbec4)

~~~json
{
  "source": "00bbbec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbec8`](#insn-00bbbec8)

~~~json
{
  "source": "00bbbec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbecc`](#insn-00bbbecc)

~~~json
{
  "source": "00bbbecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbed0`](#insn-00bbbed0)

~~~json
{
  "source": "00bbbed0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbed8`](#insn-00bbbed8)

~~~json
{
  "source": "00bbbed8",
  "target": "00bbbf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbee0`](#insn-00bbbee0)

~~~json
{
  "source": "00bbbee0",
  "target": "00bbbee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbee8`](#insn-00bbbee8)

~~~json
{
  "source": "00bbbee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeec`](#insn-00bbbeec)

~~~json
{
  "source": "00bbbeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbef0`](#insn-00bbbef0)

~~~json
{
  "source": "00bbbef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbef4`](#insn-00bbbef4)

~~~json
{
  "source": "00bbbef4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
