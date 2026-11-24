# 00bebed0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00beaedc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beaedc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0013.md#compare-c87963a3e21e631496440d91576976e2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bebed0",
  "name": "FUN_00bebed0",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e38afad6af44b1a5a8f93df770fb865948d7b2dc8ad3fc9602ca750160b57a94",
  "source_text_sha256": "e38afad6af44b1a5a8f93df770fb865948d7b2dc8ad3fc9602ca750160b57a94",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bebed0",
        "00bebff7"
      ]
    ],
    "bytes_sha256": "b5200948dd1e3aaaffd41d55a0a924df7f49c5b1e4216c9b93c1ad07d69f5c43",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be4fb0](../00be4/00be4fb0.md)
- [00bebc10](../00beb/00bebc10.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1767 bytes

~~~c

void FUN_00bebed0(short *param_1,short *param_2,short *param_3,short *param_4,short *param_5)

{
  short sVar1;
  short sVar2;
  short sVar3;
  
  sVar1 = *param_2;
  sVar2 = *param_1;
  sVar3 = *param_3;
  if (sVar1 < sVar2) {
    if (sVar3 < sVar1) {
      *param_1 = sVar3;
    }
    else {
      *param_1 = sVar1;
      *param_2 = sVar2;
      sVar3 = *param_3;
      if (sVar2 <= sVar3) goto LAB_00bebf50;
      *param_2 = sVar3;
    }
    *param_3 = sVar2;
    sVar3 = sVar2;
  }
  else if (sVar3 < sVar1) {
    *param_2 = sVar3;
    *param_3 = sVar1;
    sVar2 = *param_1;
    sVar3 = sVar1;
    if (*param_2 < sVar2) {
      *param_1 = *param_2;
      *param_2 = sVar2;
      sVar3 = *param_3;
    }
  }
LAB_00bebf50:
  if (*param_4 < sVar3) {
    *param_3 = *param_4;
    *param_4 = sVar3;
    sVar3 = *param_2;
    if (*param_3 < sVar3) {
      *param_2 = *param_3;
      *param_3 = sVar3;
      sVar3 = *param_1;
      if (*param_2 < sVar3) {
        *param_1 = *param_2;
        *param_2 = sVar3;
      }
    }
  }
  sVar3 = *param_4;
  if (*param_5 < sVar3) {
    *param_4 = *param_5;
    *param_5 = sVar3;
    sVar3 = *param_3;
    if (*param_4 < sVar3) {
      *param_3 = *param_4;
      *param_4 = sVar3;
      sVar3 = *param_2;
      if (*param_3 < sVar3) {
        *param_2 = *param_3;
        *param_3 = sVar3;
        sVar3 = *param_1;
                    /* try { // try from 00bebfe4 to 00cebfeb has its CatchHandler @ 00bebfec */
        if (*param_2 < sVar3) {
                    /* catch() { ... } // from try @ 00bebfe4 with catch @ 00bebfec
                       try { // try from 00bebfec to 00cec023 has its CatchHandler @ 00bebe80 */
          *param_1 = *param_2;
          *param_2 = sVar3;
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
<a id="insn-00bebed0"></a> `00bebed0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bebed4"></a> `00bebed4` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebed8"></a> `00bebed8` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebedc"></a> `00bebedc` | `4a 00 c0 79` | ldrsh w10,[x2] | `FALL_THROUGH`
<a id="insn-00bebee0"></a> `00bebee0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebee4"></a> `00bebee4` | `aa 00 00 54` | b.ge 0x00bebef8 | `CONDITIONAL_JUMP`
<a id="insn-00bebee8"></a> `00bebee8` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bebeec"></a> `00bebeec` | `ea 01 00 54` | b.ge 0x00bebf28 | `CONDITIONAL_JUMP`
<a id="insn-00bebef0"></a> `00bebef0` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebef4"></a> `00bebef4` | `13 00 00 14` | b 0x00bebf40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebef8"></a> `00bebef8` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bebefc"></a> `00bebefc` | `8a 02 00 54` | b.ge 0x00bebf4c | `CONDITIONAL_JUMP`
<a id="insn-00bebf00"></a> `00bebf00` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00bebf04"></a> `00bebf04` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebf08"></a> `00bebf08` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebf0c"></a> `00bebf0c` | `0a 00 c0 79` | ldrsh w10,[x0] | `FALL_THROUGH`
<a id="insn-00bebf10"></a> `00bebf10` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bebf14"></a> `00bebf14` | `ea 01 00 54` | b.ge 0x00bebf50 | `CONDITIONAL_JUMP`
<a id="insn-00bebf18"></a> `00bebf18` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebf1c"></a> `00bebf1c` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00bebf20"></a> `00bebf20` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebf24"></a> `00bebf24` | `0b 00 00 14` | b 0x00bebf50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebf28"></a> `00bebf28` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebf2c"></a> `00bebf2c` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebf30"></a> `00bebf30` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebf34"></a> `00bebf34` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebf38"></a> `00bebf38` | `ca 00 00 54` | b.ge 0x00bebf50 | `CONDITIONAL_JUMP`
<a id="insn-00bebf3c"></a> `00bebf3c` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebf40"></a> `00bebf40` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00bebf44"></a> `00bebf44` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebf48"></a> `00bebf48` | `02 00 00 14` | b 0x00bebf50 | `UNCONDITIONAL_JUMP`
<a id="insn-00bebf4c"></a> `00bebf4c` | `e8 03 0a 2a` | mov w8,w10 | `FALL_THROUGH`
<a id="insn-00bebf50"></a> `00bebf50` | `69 00 c0 79` | ldrsh w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebf54"></a> `00bebf54` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00bebf58"></a> `00bebf58` | `ea 01 00 54` | b.ge 0x00bebf94 | `CONDITIONAL_JUMP`
<a id="insn-00bebf5c"></a> `00bebf5c` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebf60"></a> `00bebf60` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebf64"></a> `00bebf64` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebf68"></a> `00bebf68` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebf6c"></a> `00bebf6c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebf70"></a> `00bebf70` | `2a 01 00 54` | b.ge 0x00bebf94 | `CONDITIONAL_JUMP`
<a id="insn-00bebf74"></a> `00bebf74` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebf78"></a> `00bebf78` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebf7c"></a> `00bebf7c` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebf80"></a> `00bebf80` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebf84"></a> `00bebf84` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebf88"></a> `00bebf88` | `6a 00 00 54` | b.ge 0x00bebf94 | `CONDITIONAL_JUMP`
<a id="insn-00bebf8c"></a> `00bebf8c` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebf90"></a> `00bebf90` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebf94"></a> `00bebf94` | `88 00 c0 79` | ldrsh w8,[x4] | `FALL_THROUGH`
<a id="insn-00bebf98"></a> `00bebf98` | `69 00 c0 79` | ldrsh w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebf9c"></a> `00bebf9c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebfa0"></a> `00bebfa0` | `aa 02 00 54` | b.ge 0x00bebff4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfa4"></a> `00bebfa4` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebfa8"></a> `00bebfa8` | `89 00 00 79` | strh w9,[x4] | `FALL_THROUGH`
<a id="insn-00bebfac"></a> `00bebfac` | `68 00 c0 79` | ldrsh w8,[x3] | `FALL_THROUGH`
<a id="insn-00bebfb0"></a> `00bebfb0` | `49 00 c0 79` | ldrsh w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebfb4"></a> `00bebfb4` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebfb8"></a> `00bebfb8` | `ea 01 00 54` | b.ge 0x00bebff4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfbc"></a> `00bebfbc` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebfc0"></a> `00bebfc0` | `69 00 00 79` | strh w9,[x3] | `FALL_THROUGH`
<a id="insn-00bebfc4"></a> `00bebfc4` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00bebfc8"></a> `00bebfc8` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebfcc"></a> `00bebfcc` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebfd0"></a> `00bebfd0` | `2a 01 00 54` | b.ge 0x00bebff4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfd4"></a> `00bebfd4` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebfd8"></a> `00bebfd8` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00bebfdc"></a> `00bebfdc` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00bebfe0"></a> `00bebfe0` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00bebfe4"></a> `00bebfe4` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bebfe8"></a> `00bebfe8` | `6a 00 00 54` | b.ge 0x00bebff4 | `CONDITIONAL_JUMP`
<a id="insn-00bebfec"></a> `00bebfec` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00bebff0"></a> `00bebff0` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00bebff4"></a> `00bebff4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bebed0`](#insn-00bebed0) 範囲 `[['00bebed0', '00bebee7']]`
  - `CONDITIONAL_JUMP` [`00bebee4`](#insn-00bebee4) → [`00bebef8`](#insn-00bebef8)
  - `FALL_THROUGH` [`00bebee4`](#insn-00bebee4) → [`00bebee8`](#insn-00bebee8)
- ブロック [`00bebee8`](#insn-00bebee8) 範囲 `[['00bebee8', '00bebeef']]`
  - `CONDITIONAL_JUMP` [`00bebeec`](#insn-00bebeec) → [`00bebf28`](#insn-00bebf28)
  - `FALL_THROUGH` [`00bebeec`](#insn-00bebeec) → [`00bebef0`](#insn-00bebef0)
- ブロック [`00bebef0`](#insn-00bebef0) 範囲 `[['00bebef0', '00bebef7']]`
  - `UNCONDITIONAL_JUMP` [`00bebef4`](#insn-00bebef4) → [`00bebf40`](#insn-00bebf40)
- ブロック [`00bebef8`](#insn-00bebef8) 範囲 `[['00bebef8', '00bebeff']]`
  - `CONDITIONAL_JUMP` [`00bebefc`](#insn-00bebefc) → [`00bebf4c`](#insn-00bebf4c)
  - `FALL_THROUGH` [`00bebefc`](#insn-00bebefc) → [`00bebf00`](#insn-00bebf00)
- ブロック [`00bebf00`](#insn-00bebf00) 範囲 `[['00bebf00', '00bebf17']]`
  - `CONDITIONAL_JUMP` [`00bebf14`](#insn-00bebf14) → [`00bebf50`](#insn-00bebf50)
  - `FALL_THROUGH` [`00bebf14`](#insn-00bebf14) → [`00bebf18`](#insn-00bebf18)
- ブロック [`00bebf18`](#insn-00bebf18) 範囲 `[['00bebf18', '00bebf27']]`
  - `UNCONDITIONAL_JUMP` [`00bebf24`](#insn-00bebf24) → [`00bebf50`](#insn-00bebf50)
- ブロック [`00bebf28`](#insn-00bebf28) 範囲 `[['00bebf28', '00bebf3b']]`
  - `CONDITIONAL_JUMP` [`00bebf38`](#insn-00bebf38) → [`00bebf50`](#insn-00bebf50)
  - `FALL_THROUGH` [`00bebf38`](#insn-00bebf38) → [`00bebf3c`](#insn-00bebf3c)
- ブロック [`00bebf3c`](#insn-00bebf3c) 範囲 `[['00bebf3c', '00bebf3f']]`
  - `FALL_THROUGH` [`00bebf3c`](#insn-00bebf3c) → [`00bebf40`](#insn-00bebf40)
- ブロック [`00bebf40`](#insn-00bebf40) 範囲 `[['00bebf40', '00bebf4b']]`
  - `UNCONDITIONAL_JUMP` [`00bebf48`](#insn-00bebf48) → [`00bebf50`](#insn-00bebf50)
- ブロック [`00bebf4c`](#insn-00bebf4c) 範囲 `[['00bebf4c', '00bebf4f']]`
  - `FALL_THROUGH` [`00bebf4c`](#insn-00bebf4c) → [`00bebf50`](#insn-00bebf50)
- ブロック [`00bebf50`](#insn-00bebf50) 範囲 `[['00bebf50', '00bebf5b']]`
  - `CONDITIONAL_JUMP` [`00bebf58`](#insn-00bebf58) → [`00bebf94`](#insn-00bebf94)
  - `FALL_THROUGH` [`00bebf58`](#insn-00bebf58) → [`00bebf5c`](#insn-00bebf5c)
- ブロック [`00bebf5c`](#insn-00bebf5c) 範囲 `[['00bebf5c', '00bebf73']]`
  - `CONDITIONAL_JUMP` [`00bebf70`](#insn-00bebf70) → [`00bebf94`](#insn-00bebf94)
  - `FALL_THROUGH` [`00bebf70`](#insn-00bebf70) → [`00bebf74`](#insn-00bebf74)
- ブロック [`00bebf74`](#insn-00bebf74) 範囲 `[['00bebf74', '00bebf8b']]`
  - `CONDITIONAL_JUMP` [`00bebf88`](#insn-00bebf88) → [`00bebf94`](#insn-00bebf94)
  - `FALL_THROUGH` [`00bebf88`](#insn-00bebf88) → [`00bebf8c`](#insn-00bebf8c)
- ブロック [`00bebf8c`](#insn-00bebf8c) 範囲 `[['00bebf8c', '00bebf93']]`
  - `FALL_THROUGH` [`00bebf90`](#insn-00bebf90) → [`00bebf94`](#insn-00bebf94)
- ブロック [`00bebf94`](#insn-00bebf94) 範囲 `[['00bebf94', '00bebfa3']]`
  - `CONDITIONAL_JUMP` [`00bebfa0`](#insn-00bebfa0) → [`00bebff4`](#insn-00bebff4)
  - `FALL_THROUGH` [`00bebfa0`](#insn-00bebfa0) → [`00bebfa4`](#insn-00bebfa4)
- ブロック [`00bebfa4`](#insn-00bebfa4) 範囲 `[['00bebfa4', '00bebfbb']]`
  - `CONDITIONAL_JUMP` [`00bebfb8`](#insn-00bebfb8) → [`00bebff4`](#insn-00bebff4)
  - `FALL_THROUGH` [`00bebfb8`](#insn-00bebfb8) → [`00bebfbc`](#insn-00bebfbc)
- ブロック [`00bebfbc`](#insn-00bebfbc) 範囲 `[['00bebfbc', '00bebfd3']]`
  - `CONDITIONAL_JUMP` [`00bebfd0`](#insn-00bebfd0) → [`00bebff4`](#insn-00bebff4)
  - `FALL_THROUGH` [`00bebfd0`](#insn-00bebfd0) → [`00bebfd4`](#insn-00bebfd4)
- ブロック [`00bebfd4`](#insn-00bebfd4) 範囲 `[['00bebfd4', '00bebfe3']]`
  - `FALL_THROUGH` [`00bebfe0`](#insn-00bebfe0) → [`00bebfe4`](#insn-00bebfe4)
- ブロック [`00bebfe4`](#insn-00bebfe4) 範囲 `[['00bebfe4', '00bebfeb']]`
  - `CONDITIONAL_JUMP` [`00bebfe8`](#insn-00bebfe8) → [`00bebff4`](#insn-00bebff4)
  - `FALL_THROUGH` [`00bebfe8`](#insn-00bebfe8) → [`00bebfec`](#insn-00bebfec)
- ブロック [`00bebfec`](#insn-00bebfec) 範囲 `[['00bebfec', '00bebff3']]`
  - `FALL_THROUGH` [`00bebff0`](#insn-00bebff0) → [`00bebff4`](#insn-00bebff4)
- ブロック [`00bebff4`](#insn-00bebff4) 範囲 `[['00bebff4', '00bebff7']]`

## 命令位置別の参照

- [`00bebee4`](#insn-00bebee4) → [`00bebef8`](#insn-00bebef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebeec`](#insn-00bebeec) → [`00bebf28`](#insn-00bebf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebef4`](#insn-00bebef4) → [`00bebf40`](#insn-00bebf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebefc`](#insn-00bebefc) → [`00bebf4c`](#insn-00bebf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf14`](#insn-00bebf14) → [`00bebf50`](#insn-00bebf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf24`](#insn-00bebf24) → [`00bebf50`](#insn-00bebf50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf38`](#insn-00bebf38) → [`00bebf50`](#insn-00bebf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf48`](#insn-00bebf48) → [`00bebf50`](#insn-00bebf50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf58`](#insn-00bebf58) → [`00bebf94`](#insn-00bebf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf70`](#insn-00bebf70) → [`00bebf94`](#insn-00bebf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebf88`](#insn-00bebf88) → [`00bebf94`](#insn-00bebf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfa0`](#insn-00bebfa0) → [`00bebff4`](#insn-00bebff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfb8`](#insn-00bebfb8) → [`00bebff4`](#insn-00bebff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfd0`](#insn-00bebfd0) → [`00bebff4`](#insn-00bebff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bebfe8`](#insn-00bebfe8) → [`00bebff4`](#insn-00bebff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bebee4`](#insn-00bebee4)

~~~json
{
  "source": "00bebee4",
  "target": "00bebef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebeec`](#insn-00bebeec)

~~~json
{
  "source": "00bebeec",
  "target": "00bebf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebef4`](#insn-00bebef4)

~~~json
{
  "source": "00bebef4",
  "target": "00bebf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebefc`](#insn-00bebefc)

~~~json
{
  "source": "00bebefc",
  "target": "00bebf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf14`](#insn-00bebf14)

~~~json
{
  "source": "00bebf14",
  "target": "00bebf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf24`](#insn-00bebf24)

~~~json
{
  "source": "00bebf24",
  "target": "00bebf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf38`](#insn-00bebf38)

~~~json
{
  "source": "00bebf38",
  "target": "00bebf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf48`](#insn-00bebf48)

~~~json
{
  "source": "00bebf48",
  "target": "00bebf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf58`](#insn-00bebf58)

~~~json
{
  "source": "00bebf58",
  "target": "00bebf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf70`](#insn-00bebf70)

~~~json
{
  "source": "00bebf70",
  "target": "00bebf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebf88`](#insn-00bebf88)

~~~json
{
  "source": "00bebf88",
  "target": "00bebf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfa0`](#insn-00bebfa0)

~~~json
{
  "source": "00bebfa0",
  "target": "00bebff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfb8`](#insn-00bebfb8)

~~~json
{
  "source": "00bebfb8",
  "target": "00bebff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfd0`](#insn-00bebfd0)

~~~json
{
  "source": "00bebfd0",
  "target": "00bebff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bebfe8`](#insn-00bebfe8)

~~~json
{
  "source": "00bebfe8",
  "target": "00bebff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
