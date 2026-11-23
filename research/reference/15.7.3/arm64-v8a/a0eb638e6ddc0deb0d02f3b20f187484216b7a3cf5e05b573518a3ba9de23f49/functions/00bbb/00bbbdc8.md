# 00bbbdc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbbd00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-e94091185e52a6be70a46f45fd78a02c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbbe0c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbe0c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-d209222d6d6441168c05e7571dee1561)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbdc8",
  "name": "FUN_00bbbdc8",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8f85adf2d1d77183254cdffc1891810a24b5a2a61ba3fe02bb27ca0ff3764ee",
  "source_text_sha256": "b8f85adf2d1d77183254cdffc1891810a24b5a2a61ba3fe02bb27ca0ff3764ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbdc8",
        "00bbbebb"
      ]
    ],
    "bytes_sha256": "cd2008e16ffdd7f463898211a798d119a7e9db58ad631353928914f92dd19b71",
    "instruction_count": 61,
    "instruction_bytes": 244,
    "body_bytes": 244,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbbb0c](../00bbb/00bbbb0c.md)

## 呼び出し先

- [00bbbebc](../00bbb/00bbbebc.md)
- [00bdb770](../00bdb/00bdb770.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1347 bytes

~~~c

undefined8 FUN_00bbbdc8(long param_1,long param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  
  puVar2 = PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018;
  puVar1 = PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8;
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
      lVar3 = __dynamic_cast(lVar5,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
                    /* try { // try from 00bbbe78 to 00cbbe7f has its CatchHandler @ 00bbd2e8 */
      if (lVar3 != 0) {
        uVar4 = FUN_00bbbebc(lVar3,param_2);
        return uVar4;
      }
                    /* try { // try from 00bbbea8 to 00cbbebb has its CatchHandler @ 00bbd1ac */
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
<a id="insn-00bbbdc8"></a> `00bbbdc8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbdcc"></a> `00bbbdcc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbbdd0"></a> `00bbbdd0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbdd4"></a> `00bbbdd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbdd8"></a> `00bbbdd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbddc"></a> `00bbbddc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbde0"></a> `00bbbde0` | `14 03 00 90` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbde4"></a> `00bbbde4` | `15 03 00 b0` | adrp x21,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbde8"></a> `00bbbde8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bbbdec"></a> `00bbbdec` | `94 fe 47 f9` | ldr x20,[x20, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbdf0"></a> `00bbbdf0` | `b5 0e 40 f9` | ldr x21,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbdf4"></a> `00bbbdf4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbbdf8"></a> `00bbbdf8` | `13 05 00 b4` | cbz x19,0x00bbbe98 | `CONDITIONAL_JUMP`
<a id="insn-00bbbdfc"></a> `00bbbdfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbe00"></a> `00bbbe00` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbe04"></a> `00bbbe04` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bbbe08"></a> `00bbbe08` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe0c"></a> `00bbbe0c` | `59 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe10"></a> `00bbbe10` | `a0 04 00 b4` | cbz x0,0x00bbbea4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe14"></a> `00bbbe14` | `09 10 40 b9` | ldr w9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe18"></a> `00bbbe18` | `e8 12 40 b9` | ldr w8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe1c"></a> `00bbbe1c` | `3f 01 28 6a` | bics wzr,w9,w8 | `FALL_THROUGH`
<a id="insn-00bbbe20"></a> `00bbbe20` | `c1 03 00 54` | b.ne 0x00bbbe98 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe24"></a> `00bbbe24` | `f6 0e 40 f9` | ldr x22,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe28"></a> `00bbbe28` | `13 0c 40 f9` | ldr x19,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbe2c"></a> `00bbbe2c` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe30"></a> `00bbbe30` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbe34"></a> `00bbbe34` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbbe38"></a> `00bbbe38` | `40 03 00 54` | b.eq 0x00bbbea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe3c"></a> `00bbbe3c` | `e8 02 00 36` | tbz w8,#0x0,0x00bbbe98 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe40"></a> `00bbbe40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbe44"></a> `00bbbe44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbbe48"></a> `00bbbe48` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bbbe4c"></a> `00bbbe4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe50"></a> `00bbbe50` | `48 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe54"></a> `00bbbe54` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbbe58"></a> `00bbbe58` | `00 fd ff b5` | cbnz x0,0x00bbbdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe5c"></a> `00bbbe5c` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbe60"></a> `00bbbe60` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbe64"></a> `00bbbe64` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbe68"></a> `00bbbe68` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbe6c"></a> `00bbbe6c` | `42 18 40 f9` | ldr x2,[x2, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbe70"></a> `00bbbe70` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbe74"></a> `00bbbe74` | `3f 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbe78"></a> `00bbbe78` | `60 01 00 b4` | cbz x0,0x00bbbea4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbe7c"></a> `00bbbe7c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbbe80"></a> `00bbbe80` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbe84"></a> `00bbbe84` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbe88"></a> `00bbbe88` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbe8c"></a> `00bbbe8c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbbe90"></a> `00bbbe90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbe94"></a> `00bbbe94` | `0a 00 00 14` | b 0x00bbbebc | `CALL_TERMINATOR`
<a id="insn-00bbbe98"></a> `00bbbe98` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbe9c"></a> `00bbbe9c` | `02 00 00 14` | b 0x00bbbea4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbea0"></a> `00bbbea0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbea4"></a> `00bbbea4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbea8"></a> `00bbbea8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbeac"></a> `00bbbeac` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbeb0"></a> `00bbbeb0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbbeb4"></a> `00bbbeb4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbeb8"></a> `00bbbeb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbdc8`](#insn-00bbbdc8) 範囲 `[['00bbbdc8', '00bbbdf7']]`
  - `FALL_THROUGH` [`00bbbdf4`](#insn-00bbbdf4) → [`00bbbdf8`](#insn-00bbbdf8)
- ブロック [`00bbbdf8`](#insn-00bbbdf8) 範囲 `[['00bbbdf8', '00bbbdfb']]`
  - `CONDITIONAL_JUMP` [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbe98`](#insn-00bbbe98)
  - `FALL_THROUGH` [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbdfc`](#insn-00bbbdfc)
- ブロック [`00bbbdfc`](#insn-00bbbdfc) 範囲 `[['00bbbdfc', '00bbbe13']]`
  - `CONDITIONAL_JUMP` [`00bbbe10`](#insn-00bbbe10) → [`00bbbea4`](#insn-00bbbea4)
  - `FALL_THROUGH` [`00bbbe10`](#insn-00bbbe10) → [`00bbbe14`](#insn-00bbbe14)
- ブロック [`00bbbe14`](#insn-00bbbe14) 範囲 `[['00bbbe14', '00bbbe23']]`
  - `CONDITIONAL_JUMP` [`00bbbe20`](#insn-00bbbe20) → [`00bbbe98`](#insn-00bbbe98)
  - `FALL_THROUGH` [`00bbbe20`](#insn-00bbbe20) → [`00bbbe24`](#insn-00bbbe24)
- ブロック [`00bbbe24`](#insn-00bbbe24) 範囲 `[['00bbbe24', '00bbbe3b']]`
  - `CONDITIONAL_JUMP` [`00bbbe38`](#insn-00bbbe38) → [`00bbbea0`](#insn-00bbbea0)
  - `FALL_THROUGH` [`00bbbe38`](#insn-00bbbe38) → [`00bbbe3c`](#insn-00bbbe3c)
- ブロック [`00bbbe3c`](#insn-00bbbe3c) 範囲 `[['00bbbe3c', '00bbbe3f']]`
  - `CONDITIONAL_JUMP` [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbe98`](#insn-00bbbe98)
  - `FALL_THROUGH` [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbe40`](#insn-00bbbe40)
- ブロック [`00bbbe40`](#insn-00bbbe40) 範囲 `[['00bbbe40', '00bbbe5b']]`
  - `CONDITIONAL_JUMP` [`00bbbe58`](#insn-00bbbe58) → [`00bbbdf8`](#insn-00bbbdf8)
  - `FALL_THROUGH` [`00bbbe58`](#insn-00bbbe58) → [`00bbbe5c`](#insn-00bbbe5c)
- ブロック [`00bbbe5c`](#insn-00bbbe5c) 範囲 `[['00bbbe5c', '00bbbe77']]`
  - `FALL_THROUGH` [`00bbbe74`](#insn-00bbbe74) → [`00bbbe78`](#insn-00bbbe78)
- ブロック [`00bbbe78`](#insn-00bbbe78) 範囲 `[['00bbbe78', '00bbbe7b']]`
  - `CONDITIONAL_JUMP` [`00bbbe78`](#insn-00bbbe78) → [`00bbbea4`](#insn-00bbbea4)
  - `FALL_THROUGH` [`00bbbe78`](#insn-00bbbe78) → [`00bbbe7c`](#insn-00bbbe7c)
- ブロック [`00bbbe7c`](#insn-00bbbe7c) 範囲 `[['00bbbe7c', '00bbbe97']]`
- ブロック [`00bbbe98`](#insn-00bbbe98) 範囲 `[['00bbbe98', '00bbbe9f']]`
  - `UNCONDITIONAL_JUMP` [`00bbbe9c`](#insn-00bbbe9c) → [`00bbbea4`](#insn-00bbbea4)
- ブロック [`00bbbea0`](#insn-00bbbea0) 範囲 `[['00bbbea0', '00bbbea3']]`
  - `FALL_THROUGH` [`00bbbea0`](#insn-00bbbea0) → [`00bbbea4`](#insn-00bbbea4)
- ブロック [`00bbbea4`](#insn-00bbbea4) 範囲 `[['00bbbea4', '00bbbea7']]`
  - `FALL_THROUGH` [`00bbbea4`](#insn-00bbbea4) → [`00bbbea8`](#insn-00bbbea8)
- ブロック [`00bbbea8`](#insn-00bbbea8) 範囲 `[['00bbbea8', '00bbbebb']]`

## 命令位置別の参照

- [`00bbbdcc`](#insn-00bbbdcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdd0`](#insn-00bbbdd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdd4`](#insn-00bbbdd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdd8`](#insn-00bbbdd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdec`](#insn-00bbbdec) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbdf0`](#insn-00bbbdf0) → `00c1c018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbdf8`](#insn-00bbbdf8) → [`00bbbe98`](#insn-00bbbe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe00`](#insn-00bbbe00) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe04`](#insn-00bbbe04) → `00c16c08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe0c`](#insn-00bbbe0c) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe10`](#insn-00bbbe10) → [`00bbbea4`](#insn-00bbbea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe20`](#insn-00bbbe20) → [`00bbbe98`](#insn-00bbbe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe38`](#insn-00bbbe38) → [`00bbbea0`](#insn-00bbbea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe3c`](#insn-00bbbe3c) → [`00bbbe98`](#insn-00bbbe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe44`](#insn-00bbbe44) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe48`](#insn-00bbbe48) → `00c16c08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe50`](#insn-00bbbe50) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe58`](#insn-00bbbe58) → [`00bbbdf8`](#insn-00bbbdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe68`](#insn-00bbbe68) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe68`](#insn-00bbbe68) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe6c`](#insn-00bbbe6c) → `00c1c030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbe6c`](#insn-00bbbe6c) → `00c16c38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbe74`](#insn-00bbbe74) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe78`](#insn-00bbbe78) → [`00bbbea4`](#insn-00bbbea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe80`](#insn-00bbbe80) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe84`](#insn-00bbbe84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe88`](#insn-00bbbe88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe8c`](#insn-00bbbe8c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe94`](#insn-00bbbe94) → [`00bbbebc`](00bbbebc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbbebc` · 推定シンボル `None` · 推定型 `None`
- [`00bbbe9c`](#insn-00bbbe9c) → [`00bbbea4`](#insn-00bbbea4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbea4`](#insn-00bbbea4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbea8`](#insn-00bbbea8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeac`](#insn-00bbbeac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeb0`](#insn-00bbbeb0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbdcc`](#insn-00bbbdcc)

~~~json
{
  "source": "00bbbdcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdd0`](#insn-00bbbdd0)

~~~json
{
  "source": "00bbbdd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdd4`](#insn-00bbbdd4)

~~~json
{
  "source": "00bbbdd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdd8`](#insn-00bbbdd8)

~~~json
{
  "source": "00bbbdd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdec`](#insn-00bbbdec)

~~~json
{
  "source": "00bbbdec",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbdf0`](#insn-00bbbdf0)

~~~json
{
  "source": "00bbbdf0",
  "target": "00c1c018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbdf8`](#insn-00bbbdf8)

~~~json
{
  "source": "00bbbdf8",
  "target": "00bbbe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe00`](#insn-00bbbe00)

~~~json
{
  "source": "00bbbe00",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe04`](#insn-00bbbe04)

~~~json
{
  "source": "00bbbe04",
  "target": "00c16c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe0c`](#insn-00bbbe0c)

~~~json
{
  "source": "00bbbe0c",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe10`](#insn-00bbbe10)

~~~json
{
  "source": "00bbbe10",
  "target": "00bbbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe20`](#insn-00bbbe20)

~~~json
{
  "source": "00bbbe20",
  "target": "00bbbe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe38`](#insn-00bbbe38)

~~~json
{
  "source": "00bbbe38",
  "target": "00bbbea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe3c`](#insn-00bbbe3c)

~~~json
{
  "source": "00bbbe3c",
  "target": "00bbbe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe44`](#insn-00bbbe44)

~~~json
{
  "source": "00bbbe44",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
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
  "target": "00c16c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c08",
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
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe58`](#insn-00bbbe58)

~~~json
{
  "source": "00bbbe58",
  "target": "00bbbdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe68`](#insn-00bbbe68)

~~~json
{
  "source": "00bbbe68",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe68`](#insn-00bbbe68)

~~~json
{
  "source": "00bbbe68",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe6c`](#insn-00bbbe6c)

~~~json
{
  "source": "00bbbe6c",
  "target": "00c1c030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe6c`](#insn-00bbbe6c)

~~~json
{
  "source": "00bbbe6c",
  "target": "00c16c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbe74`](#insn-00bbbe74)

~~~json
{
  "source": "00bbbe74",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe78`](#insn-00bbbe78)

~~~json
{
  "source": "00bbbe78",
  "target": "00bbbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe80`](#insn-00bbbe80)

~~~json
{
  "source": "00bbbe80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe84`](#insn-00bbbe84)

~~~json
{
  "source": "00bbbe84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe88`](#insn-00bbbe88)

~~~json
{
  "source": "00bbbe88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe8c`](#insn-00bbbe8c)

~~~json
{
  "source": "00bbbe8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbe94`](#insn-00bbbe94)

~~~json
{
  "source": "00bbbe94",
  "target": "00bbbebc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbe9c`](#insn-00bbbe9c)

~~~json
{
  "source": "00bbbe9c",
  "target": "00bbbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbea4`](#insn-00bbbea4)

~~~json
{
  "source": "00bbbea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbea8`](#insn-00bbbea8)

~~~json
{
  "source": "00bbbea8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeac`](#insn-00bbbeac)

~~~json
{
  "source": "00bbbeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeb0`](#insn-00bbbeb0)

~~~json
{
  "source": "00bbbeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
