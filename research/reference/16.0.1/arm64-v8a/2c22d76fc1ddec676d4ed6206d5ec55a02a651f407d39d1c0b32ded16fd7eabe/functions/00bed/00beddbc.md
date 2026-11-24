# 00beddbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0085.md#review-92ce3807030cf3a4aa6ece279acc2ee5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0044.md#review-92ce3807030cf3a4aa6ece279acc2ee5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beddbc",
  "name": "FUN_00beddbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e4cbe5139261a7dcf0713b92a00a6b4d988bc649f884444f08214384b14359c",
  "source_text_sha256": "0e4cbe5139261a7dcf0713b92a00a6b4d988bc649f884444f08214384b14359c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beddbc",
        "00bedee3"
      ]
    ],
    "bytes_sha256": "f8f1254738e345e86b10579253658224786fe5f1e21a43e34379cd1a22852dc9",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be7110](../00be7/00be7110.md)
- [00bedb1c](../00bed/00bedb1c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00beddbc(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
                    /* try { // try from 00bedde0 to 00cedf3b has its CatchHandler @ 00bedde0
                       catch() { ... } // from try @ 00bedde0 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bedf88 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee064 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee130 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee258 with catch @ 00bedde0
                       catch() { ... } // from try @ 00bee4bc with catch @ 00bedde0 */
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00bede3c;
      *param_2 = uVar3;
    }
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00bede3c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar3 = *param_1;
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
  if (*param_5 < uVar3) {
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar3 = *param_3;
    if (*param_4 < uVar3) {
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar3 = *param_2;
      if (*param_3 < uVar3) {
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar3 = *param_1;
        if (*param_2 < uVar3) {
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00beddbc"></a> `00beddbc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beddc0"></a> `00beddc0` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00beddc4"></a> `00beddc4` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beddc8"></a> `00beddc8` | `4a 00 40 f9` | ldr x10,[x2] | `FALL_THROUGH`
<a id="insn-00beddcc"></a> `00beddcc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beddd0"></a> `00beddd0` | `a2 00 00 54` | b.cs 0x00bedde4 | `CONDITIONAL_JUMP`
<a id="insn-00beddd4"></a> `00beddd4` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00beddd8"></a> `00beddd8` | `e2 01 00 54` | b.cs 0x00bede14 | `CONDITIONAL_JUMP`
<a id="insn-00bedddc"></a> `00bedddc` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bedde0"></a> `00bedde0` | `13 00 00 14` | b 0x00bede2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bedde4"></a> `00bedde4` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00bedde8"></a> `00bedde8` | `82 02 00 54` | b.cs 0x00bede38 | `CONDITIONAL_JUMP`
<a id="insn-00beddec"></a> `00beddec` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00beddf0"></a> `00beddf0` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00beddf4"></a> `00beddf4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00beddf8"></a> `00beddf8` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-00beddfc"></a> `00beddfc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bede00"></a> `00bede00` | `e2 01 00 54` | b.cs 0x00bede3c | `CONDITIONAL_JUMP`
<a id="insn-00bede04"></a> `00bede04` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bede08"></a> `00bede08` | `2a 00 00 f9` | str x10,[x1] | `FALL_THROUGH`
<a id="insn-00bede0c"></a> `00bede0c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bede10"></a> `00bede10` | `0b 00 00 14` | b 0x00bede3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bede14"></a> `00bede14` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bede18"></a> `00bede18` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00bede1c"></a> `00bede1c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bede20"></a> `00bede20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bede24"></a> `00bede24` | `c2 00 00 54` | b.cs 0x00bede3c | `CONDITIONAL_JUMP`
<a id="insn-00bede28"></a> `00bede28` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00bede2c"></a> `00bede2c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bede30"></a> `00bede30` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00bede34"></a> `00bede34` | `02 00 00 14` | b 0x00bede3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bede38"></a> `00bede38` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00bede3c"></a> `00bede3c` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00bede40"></a> `00bede40` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bede44"></a> `00bede44` | `e2 01 00 54` | b.cs 0x00bede80 | `CONDITIONAL_JUMP`
<a id="insn-00bede48"></a> `00bede48` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00bede4c"></a> `00bede4c` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00bede50"></a> `00bede50` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bede54"></a> `00bede54` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bede58"></a> `00bede58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bede5c"></a> `00bede5c` | `22 01 00 54` | b.cs 0x00bede80 | `CONDITIONAL_JUMP`
<a id="insn-00bede60"></a> `00bede60` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00bede64"></a> `00bede64` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00bede68"></a> `00bede68` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bede6c"></a> `00bede6c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bede70"></a> `00bede70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bede74"></a> `00bede74` | `62 00 00 54` | b.cs 0x00bede80 | `CONDITIONAL_JUMP`
<a id="insn-00bede78"></a> `00bede78` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bede7c"></a> `00bede7c` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00bede80"></a> `00bede80` | `88 00 40 f9` | ldr x8,[x4] | `FALL_THROUGH`
<a id="insn-00bede84"></a> `00bede84` | `69 00 40 f9` | ldr x9,[x3] | `FALL_THROUGH`
<a id="insn-00bede88"></a> `00bede88` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bede8c"></a> `00bede8c` | `a2 02 00 54` | b.cs 0x00bedee0 | `CONDITIONAL_JUMP`
<a id="insn-00bede90"></a> `00bede90` | `68 00 00 f9` | str x8,[x3] | `FALL_THROUGH`
<a id="insn-00bede94"></a> `00bede94` | `89 00 00 f9` | str x9,[x4] | `FALL_THROUGH`
<a id="insn-00bede98"></a> `00bede98` | `68 00 40 f9` | ldr x8,[x3] | `FALL_THROUGH`
<a id="insn-00bede9c"></a> `00bede9c` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00bedea0"></a> `00bedea0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bedea4"></a> `00bedea4` | `e2 01 00 54` | b.cs 0x00bedee0 | `CONDITIONAL_JUMP`
<a id="insn-00bedea8"></a> `00bedea8` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00bedeac"></a> `00bedeac` | `69 00 00 f9` | str x9,[x3] | `FALL_THROUGH`
<a id="insn-00bedeb0"></a> `00bedeb0` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bedeb4"></a> `00bedeb4` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bedeb8"></a> `00bedeb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bedebc"></a> `00bedebc` | `22 01 00 54` | b.cs 0x00bedee0 | `CONDITIONAL_JUMP`
<a id="insn-00bedec0"></a> `00bedec0` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00bedec4"></a> `00bedec4` | `49 00 00 f9` | str x9,[x2] | `FALL_THROUGH`
<a id="insn-00bedec8"></a> `00bedec8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bedecc"></a> `00bedecc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00beded0"></a> `00beded0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00beded4"></a> `00beded4` | `62 00 00 54` | b.cs 0x00bedee0 | `CONDITIONAL_JUMP`
<a id="insn-00beded8"></a> `00beded8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bededc"></a> `00bededc` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-00bedee0"></a> `00bedee0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beddbc`](#insn-00beddbc) 範囲 `[['00beddbc', '00beddd3']]`
  - `CONDITIONAL_JUMP` [`00beddd0`](#insn-00beddd0) → [`00bedde4`](#insn-00bedde4)
  - `FALL_THROUGH` [`00beddd0`](#insn-00beddd0) → [`00beddd4`](#insn-00beddd4)
- ブロック [`00beddd4`](#insn-00beddd4) 範囲 `[['00beddd4', '00bedddb']]`
  - `CONDITIONAL_JUMP` [`00beddd8`](#insn-00beddd8) → [`00bede14`](#insn-00bede14)
  - `FALL_THROUGH` [`00beddd8`](#insn-00beddd8) → [`00bedddc`](#insn-00bedddc)
- ブロック [`00bedddc`](#insn-00bedddc) 範囲 `[['00bedddc', '00bedddf']]`
  - `FALL_THROUGH` [`00bedddc`](#insn-00bedddc) → [`00bedde0`](#insn-00bedde0)
- ブロック [`00bedde0`](#insn-00bedde0) 範囲 `[['00bedde0', '00bedde3']]`
  - `UNCONDITIONAL_JUMP` [`00bedde0`](#insn-00bedde0) → [`00bede2c`](#insn-00bede2c)
- ブロック [`00bedde4`](#insn-00bedde4) 範囲 `[['00bedde4', '00beddeb']]`
  - `CONDITIONAL_JUMP` [`00bedde8`](#insn-00bedde8) → [`00bede38`](#insn-00bede38)
  - `FALL_THROUGH` [`00bedde8`](#insn-00bedde8) → [`00beddec`](#insn-00beddec)
- ブロック [`00beddec`](#insn-00beddec) 範囲 `[['00beddec', '00bede03']]`
  - `CONDITIONAL_JUMP` [`00bede00`](#insn-00bede00) → [`00bede3c`](#insn-00bede3c)
  - `FALL_THROUGH` [`00bede00`](#insn-00bede00) → [`00bede04`](#insn-00bede04)
- ブロック [`00bede04`](#insn-00bede04) 範囲 `[['00bede04', '00bede13']]`
  - `UNCONDITIONAL_JUMP` [`00bede10`](#insn-00bede10) → [`00bede3c`](#insn-00bede3c)
- ブロック [`00bede14`](#insn-00bede14) 範囲 `[['00bede14', '00bede27']]`
  - `CONDITIONAL_JUMP` [`00bede24`](#insn-00bede24) → [`00bede3c`](#insn-00bede3c)
  - `FALL_THROUGH` [`00bede24`](#insn-00bede24) → [`00bede28`](#insn-00bede28)
- ブロック [`00bede28`](#insn-00bede28) 範囲 `[['00bede28', '00bede2b']]`
  - `FALL_THROUGH` [`00bede28`](#insn-00bede28) → [`00bede2c`](#insn-00bede2c)
- ブロック [`00bede2c`](#insn-00bede2c) 範囲 `[['00bede2c', '00bede37']]`
  - `UNCONDITIONAL_JUMP` [`00bede34`](#insn-00bede34) → [`00bede3c`](#insn-00bede3c)
- ブロック [`00bede38`](#insn-00bede38) 範囲 `[['00bede38', '00bede3b']]`
  - `FALL_THROUGH` [`00bede38`](#insn-00bede38) → [`00bede3c`](#insn-00bede3c)
- ブロック [`00bede3c`](#insn-00bede3c) 範囲 `[['00bede3c', '00bede47']]`
  - `CONDITIONAL_JUMP` [`00bede44`](#insn-00bede44) → [`00bede80`](#insn-00bede80)
  - `FALL_THROUGH` [`00bede44`](#insn-00bede44) → [`00bede48`](#insn-00bede48)
- ブロック [`00bede48`](#insn-00bede48) 範囲 `[['00bede48', '00bede5f']]`
  - `CONDITIONAL_JUMP` [`00bede5c`](#insn-00bede5c) → [`00bede80`](#insn-00bede80)
  - `FALL_THROUGH` [`00bede5c`](#insn-00bede5c) → [`00bede60`](#insn-00bede60)
- ブロック [`00bede60`](#insn-00bede60) 範囲 `[['00bede60', '00bede77']]`
  - `CONDITIONAL_JUMP` [`00bede74`](#insn-00bede74) → [`00bede80`](#insn-00bede80)
  - `FALL_THROUGH` [`00bede74`](#insn-00bede74) → [`00bede78`](#insn-00bede78)
- ブロック [`00bede78`](#insn-00bede78) 範囲 `[['00bede78', '00bede7f']]`
  - `FALL_THROUGH` [`00bede7c`](#insn-00bede7c) → [`00bede80`](#insn-00bede80)
- ブロック [`00bede80`](#insn-00bede80) 範囲 `[['00bede80', '00bede8f']]`
  - `CONDITIONAL_JUMP` [`00bede8c`](#insn-00bede8c) → [`00bedee0`](#insn-00bedee0)
  - `FALL_THROUGH` [`00bede8c`](#insn-00bede8c) → [`00bede90`](#insn-00bede90)
- ブロック [`00bede90`](#insn-00bede90) 範囲 `[['00bede90', '00bedea7']]`
  - `CONDITIONAL_JUMP` [`00bedea4`](#insn-00bedea4) → [`00bedee0`](#insn-00bedee0)
  - `FALL_THROUGH` [`00bedea4`](#insn-00bedea4) → [`00bedea8`](#insn-00bedea8)
- ブロック [`00bedea8`](#insn-00bedea8) 範囲 `[['00bedea8', '00bedebf']]`
  - `CONDITIONAL_JUMP` [`00bedebc`](#insn-00bedebc) → [`00bedee0`](#insn-00bedee0)
  - `FALL_THROUGH` [`00bedebc`](#insn-00bedebc) → [`00bedec0`](#insn-00bedec0)
- ブロック [`00bedec0`](#insn-00bedec0) 範囲 `[['00bedec0', '00beded7']]`
  - `CONDITIONAL_JUMP` [`00beded4`](#insn-00beded4) → [`00bedee0`](#insn-00bedee0)
  - `FALL_THROUGH` [`00beded4`](#insn-00beded4) → [`00beded8`](#insn-00beded8)
- ブロック [`00beded8`](#insn-00beded8) 範囲 `[['00beded8', '00bededf']]`
  - `FALL_THROUGH` [`00bededc`](#insn-00bededc) → [`00bedee0`](#insn-00bedee0)
- ブロック [`00bedee0`](#insn-00bedee0) 範囲 `[['00bedee0', '00bedee3']]`

## 命令位置別の参照

- [`00beddd0`](#insn-00beddd0) → [`00bedde4`](#insn-00bedde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beddd8`](#insn-00beddd8) → [`00bede14`](#insn-00bede14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedde0`](#insn-00bedde0) → [`00bede2c`](#insn-00bede2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedde8`](#insn-00bedde8) → [`00bede38`](#insn-00bede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede00`](#insn-00bede00) → [`00bede3c`](#insn-00bede3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede10`](#insn-00bede10) → [`00bede3c`](#insn-00bede3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede24`](#insn-00bede24) → [`00bede3c`](#insn-00bede3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede34`](#insn-00bede34) → [`00bede3c`](#insn-00bede3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede44`](#insn-00bede44) → [`00bede80`](#insn-00bede80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede5c`](#insn-00bede5c) → [`00bede80`](#insn-00bede80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede74`](#insn-00bede74) → [`00bede80`](#insn-00bede80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bede8c`](#insn-00bede8c) → [`00bedee0`](#insn-00bedee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedea4`](#insn-00bedea4) → [`00bedee0`](#insn-00bedee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bedebc`](#insn-00bedebc) → [`00bedee0`](#insn-00bedee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beded4`](#insn-00beded4) → [`00bedee0`](#insn-00bedee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beddd0`](#insn-00beddd0)

~~~json
{
  "source": "00beddd0",
  "target": "00bedde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beddd8`](#insn-00beddd8)

~~~json
{
  "source": "00beddd8",
  "target": "00bede14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedde0`](#insn-00bedde0)

~~~json
{
  "source": "00bedde0",
  "target": "00bede2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedde8`](#insn-00bedde8)

~~~json
{
  "source": "00bedde8",
  "target": "00bede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede00`](#insn-00bede00)

~~~json
{
  "source": "00bede00",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede10`](#insn-00bede10)

~~~json
{
  "source": "00bede10",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede24`](#insn-00bede24)

~~~json
{
  "source": "00bede24",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede34`](#insn-00bede34)

~~~json
{
  "source": "00bede34",
  "target": "00bede3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede44`](#insn-00bede44)

~~~json
{
  "source": "00bede44",
  "target": "00bede80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede5c`](#insn-00bede5c)

~~~json
{
  "source": "00bede5c",
  "target": "00bede80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede74`](#insn-00bede74)

~~~json
{
  "source": "00bede74",
  "target": "00bede80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bede8c`](#insn-00bede8c)

~~~json
{
  "source": "00bede8c",
  "target": "00bedee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedea4`](#insn-00bedea4)

~~~json
{
  "source": "00bedea4",
  "target": "00bedee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bedebc`](#insn-00bedebc)

~~~json
{
  "source": "00bedebc",
  "target": "00bedee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beded4`](#insn-00beded4)

~~~json
{
  "source": "00beded4",
  "target": "00bedee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
