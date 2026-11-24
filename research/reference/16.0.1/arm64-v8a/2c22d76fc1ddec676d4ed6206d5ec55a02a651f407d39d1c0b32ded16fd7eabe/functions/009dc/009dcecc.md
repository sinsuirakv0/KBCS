# 009dcecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009dcd30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009dc/009dcd30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0032.md#compare-8d9ca67eb77bfb4bea519b5f8dddb798)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009dcf20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcf20.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0031.md#compare-0e8954012f98d89a1c965178564d1ebe)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70",
  "source_text_sha256": "0d40b5c960214e56f1437329f7ec3c72cdcdad0ccca6ee6a9dbff59013f99e70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dcecc",
        "009dcf97"
      ]
    ],
    "bytes_sha256": "e4e43e646fa3f5413687bb05dd90995e08aa330868447b2820791d28daca205c",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0063acb4](../0063a/0063acb4.md)
- [0063b54c](../0063b/0063b54c.md)
- [0063bc98](../0063b/0063bc98.md)
- [0064ecb8](../0064e/0064ecb8.md)
- [006c0f38](../006c0/006c0f38.md)
- [006c119c](../006c1/006c119c.md)
- [006c2018](../006c2/006c2018.md)
- [006d3e3c](../006d3/006d3e3c.md)
- [006dd264](../006dd/006dd264.md)
- [006de788](../006de/006de788.md)
- [006dea94](../006de/006dea94.md)
- [006e1ea8](../006e1/006e1ea8.md)
- [006e3320](../006e3/006e3320.md)
- [006f24d4](../006f2/006f24d4.md)
- [00769d84](../00769/00769d84.md)
- [008dc120](../008dc/008dc120.md)
- [008e66ac](../008e6/008e66ac.md)
- [008ef9f4](../008ef/008ef9f4.md)
- [008f3044](../008f3/008f3044.md)
- [0098dc08](../0098d/0098dc08.md)
- [00a75dac](../00a75/00a75dac.md)

## 呼び出し先

- [0085b2a4](../0085b/0085b2a4.md)
- [0085b2ac](../0085b/0085b2ac.md)
- [0085b2b4](../0085b/0085b2b4.md)
- [0085b2bc](../0085b/0085b2bc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1529 bytes

~~~c

undefined8 FUN_009dcecc(undefined8 param_1,int param_2,int param_3,int param_4,int param_5)

{
  int iVar1;
  
                    /* try { // try from 009dcee8 to 00adceef has its CatchHandler @ 009dcfd4 */
  iVar1 = FUN_0085b2a4();
  if (param_2 <= iVar1) {
                    /* try { // try from 009dcf04 to 00adcf23 has its CatchHandler @ 009dcfec */
    iVar1 = FUN_0085b2a4(param_1);
    if ((iVar1 <= param_4 + param_2) && (iVar1 = FUN_0085b2ac(param_1), param_3 <= iVar1)) {
      iVar1 = FUN_0085b2ac(param_1);
                    /* try { // try from 009dcf38 to 00adcf3f has its CatchHandler @ 009dcfb0 */
                    /* try { // try from 009dcf54 to 00adcf5b has its CatchHandler @ 009dcf60 */
                    /* catch() { ... } // from try @ 009dcc3c with catch @ 009dcf5c
                       try { // try from 009dcf5c to 00add02f has its CatchHandler @ 009dc934 */
                    /* catch() { ... } // from try @ 009dcc08 with catch @ 009dcf60
                       catch() { ... } // from try @ 009dcf54 with catch @ 009dcf60 */
      if (((iVar1 <= param_5 + param_3) &&
          (((iVar1 = FUN_0085b2b4(param_1), param_2 <= iVar1 &&
            (iVar1 = FUN_0085b2b4(param_1), iVar1 <= param_4 + param_2)) &&
           (iVar1 = FUN_0085b2bc(param_1), param_3 <= iVar1)))) &&
         (iVar1 = FUN_0085b2bc(param_1), iVar1 <= param_5 + param_3)) {
        return 1;
      }
    }
  }
                    /* catch() { ... } // from try @ 009dce44 with catch @ 009dcf78 */
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dcecc"></a> `009dcecc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-009dced0"></a> `009dced0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dced4"></a> `009dced4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dced8"></a> `009dced8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dcedc"></a> `009dcedc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009dcee0"></a> `009dcee0` | `f6 03 04 2a` | mov w22,w4 | `FALL_THROUGH`
<a id="insn-009dcee4"></a> `009dcee4` | `f7 03 03 2a` | mov w23,w3 | `FALL_THROUGH`
<a id="insn-009dcee8"></a> `009dcee8` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-009dceec"></a> `009dceec` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-009dcef0"></a> `009dcef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009dcef4"></a> `009dcef4` | `ec f8 f9 97` | bl 0x0085b2a4 | `UNCONDITIONAL_CALL`
<a id="insn-009dcef8"></a> `009dcef8` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-009dcefc"></a> `009dcefc` | `eb 03 00 54` | b.lt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf00"></a> `009dcf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf04"></a> `009dcf04` | `f7 02 15 0b` | add w23,w23,w21 | `FALL_THROUGH`
<a id="insn-009dcf08"></a> `009dcf08` | `e7 f8 f9 97` | bl 0x0085b2a4 | `UNCONDITIONAL_CALL`
<a id="insn-009dcf0c"></a> `009dcf0c` | `1f 00 17 6b` | cmp w0,w23 | `FALL_THROUGH`
<a id="insn-009dcf10"></a> `009dcf10` | `4c 03 00 54` | b.gt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf14"></a> `009dcf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf18"></a> `009dcf18` | `e5 f8 f9 97` | bl 0x0085b2ac | `UNCONDITIONAL_CALL`
<a id="insn-009dcf1c"></a> `009dcf1c` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-009dcf20"></a> `009dcf20` | `cb 02 00 54` | b.lt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf24"></a> `009dcf24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf28"></a> `009dcf28` | `d6 02 14 0b` | add w22,w22,w20 | `FALL_THROUGH`
<a id="insn-009dcf2c"></a> `009dcf2c` | `e0 f8 f9 97` | bl 0x0085b2ac | `UNCONDITIONAL_CALL`
<a id="insn-009dcf30"></a> `009dcf30` | `1f 00 16 6b` | cmp w0,w22 | `FALL_THROUGH`
<a id="insn-009dcf34"></a> `009dcf34` | `2c 02 00 54` | b.gt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf38"></a> `009dcf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf3c"></a> `009dcf3c` | `de f8 f9 97` | bl 0x0085b2b4 | `UNCONDITIONAL_CALL`
<a id="insn-009dcf40"></a> `009dcf40` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-009dcf44"></a> `009dcf44` | `ab 01 00 54` | b.lt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf48"></a> `009dcf48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf4c"></a> `009dcf4c` | `da f8 f9 97` | bl 0x0085b2b4 | `UNCONDITIONAL_CALL`
<a id="insn-009dcf50"></a> `009dcf50` | `1f 00 17 6b` | cmp w0,w23 | `FALL_THROUGH`
<a id="insn-009dcf54"></a> `009dcf54` | `2c 01 00 54` | b.gt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf58"></a> `009dcf58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf5c"></a> `009dcf5c` | `d8 f8 f9 97` | bl 0x0085b2bc | `UNCONDITIONAL_CALL`
<a id="insn-009dcf60"></a> `009dcf60` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-009dcf64"></a> `009dcf64` | `ab 00 00 54` | b.lt 0x009dcf78 | `CONDITIONAL_JUMP`
<a id="insn-009dcf68"></a> `009dcf68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009dcf6c"></a> `009dcf6c` | `d4 f8 f9 97` | bl 0x0085b2bc | `UNCONDITIONAL_CALL`
<a id="insn-009dcf70"></a> `009dcf70` | `1f 00 16 6b` | cmp w0,w22 | `FALL_THROUGH`
<a id="insn-009dcf74"></a> `009dcf74` | `ed 00 00 54` | b.le 0x009dcf90 | `CONDITIONAL_JUMP`
<a id="insn-009dcf78"></a> `009dcf78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009dcf7c"></a> `009dcf7c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dcf80"></a> `009dcf80` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009dcf84"></a> `009dcf84` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dcf88"></a> `009dcf88` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-009dcf8c"></a> `009dcf8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009dcf90"></a> `009dcf90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009dcf94"></a> `009dcf94` | `fa ff ff 17` | b 0x009dcf7c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`009dcecc`](#insn-009dcecc) 範囲 `[['009dcecc', '009dcee7']]`
  - `FALL_THROUGH` [`009dcee4`](#insn-009dcee4) → [`009dcee8`](#insn-009dcee8)
- ブロック [`009dcee8`](#insn-009dcee8) 範囲 `[['009dcee8', '009dceff']]`
  - `CONDITIONAL_JUMP` [`009dcefc`](#insn-009dcefc) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcefc`](#insn-009dcefc) → [`009dcf00`](#insn-009dcf00)
- ブロック [`009dcf00`](#insn-009dcf00) 範囲 `[['009dcf00', '009dcf03']]`
  - `FALL_THROUGH` [`009dcf00`](#insn-009dcf00) → [`009dcf04`](#insn-009dcf04)
- ブロック [`009dcf04`](#insn-009dcf04) 範囲 `[['009dcf04', '009dcf13']]`
  - `CONDITIONAL_JUMP` [`009dcf10`](#insn-009dcf10) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf10`](#insn-009dcf10) → [`009dcf14`](#insn-009dcf14)
- ブロック [`009dcf14`](#insn-009dcf14) 範囲 `[['009dcf14', '009dcf23']]`
  - `CONDITIONAL_JUMP` [`009dcf20`](#insn-009dcf20) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf20`](#insn-009dcf20) → [`009dcf24`](#insn-009dcf24)
- ブロック [`009dcf24`](#insn-009dcf24) 範囲 `[['009dcf24', '009dcf37']]`
  - `CONDITIONAL_JUMP` [`009dcf34`](#insn-009dcf34) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf34`](#insn-009dcf34) → [`009dcf38`](#insn-009dcf38)
- ブロック [`009dcf38`](#insn-009dcf38) 範囲 `[['009dcf38', '009dcf47']]`
  - `CONDITIONAL_JUMP` [`009dcf44`](#insn-009dcf44) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf44`](#insn-009dcf44) → [`009dcf48`](#insn-009dcf48)
- ブロック [`009dcf48`](#insn-009dcf48) 範囲 `[['009dcf48', '009dcf53']]`
  - `FALL_THROUGH` [`009dcf50`](#insn-009dcf50) → [`009dcf54`](#insn-009dcf54)
- ブロック [`009dcf54`](#insn-009dcf54) 範囲 `[['009dcf54', '009dcf57']]`
  - `CONDITIONAL_JUMP` [`009dcf54`](#insn-009dcf54) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf54`](#insn-009dcf54) → [`009dcf58`](#insn-009dcf58)
- ブロック [`009dcf58`](#insn-009dcf58) 範囲 `[['009dcf58', '009dcf5b']]`
  - `FALL_THROUGH` [`009dcf58`](#insn-009dcf58) → [`009dcf5c`](#insn-009dcf5c)
- ブロック [`009dcf5c`](#insn-009dcf5c) 範囲 `[['009dcf5c', '009dcf5f']]`
  - `FALL_THROUGH` [`009dcf5c`](#insn-009dcf5c) → [`009dcf60`](#insn-009dcf60)
- ブロック [`009dcf60`](#insn-009dcf60) 範囲 `[['009dcf60', '009dcf67']]`
  - `CONDITIONAL_JUMP` [`009dcf64`](#insn-009dcf64) → [`009dcf78`](#insn-009dcf78)
  - `FALL_THROUGH` [`009dcf64`](#insn-009dcf64) → [`009dcf68`](#insn-009dcf68)
- ブロック [`009dcf68`](#insn-009dcf68) 範囲 `[['009dcf68', '009dcf77']]`
  - `CONDITIONAL_JUMP` [`009dcf74`](#insn-009dcf74) → [`009dcf90`](#insn-009dcf90)
  - `FALL_THROUGH` [`009dcf74`](#insn-009dcf74) → [`009dcf78`](#insn-009dcf78)
- ブロック [`009dcf78`](#insn-009dcf78) 範囲 `[['009dcf78', '009dcf7b']]`
  - `FALL_THROUGH` [`009dcf78`](#insn-009dcf78) → [`009dcf7c`](#insn-009dcf7c)
- ブロック [`009dcf7c`](#insn-009dcf7c) 範囲 `[['009dcf7c', '009dcf8f']]`
- ブロック [`009dcf90`](#insn-009dcf90) 範囲 `[['009dcf90', '009dcf97']]`
  - `UNCONDITIONAL_JUMP` [`009dcf94`](#insn-009dcf94) → [`009dcf7c`](#insn-009dcf7c)

## 命令位置別の参照

- [`009dcecc`](#insn-009dcecc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dced0`](#insn-009dced0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dced4`](#insn-009dced4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dced8`](#insn-009dced8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcef4`](#insn-009dcef4) → [`0085b2a4`](../0085b/0085b2a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2a4` · 推定シンボル `None` · 推定型 `None`
- [`009dcefc`](#insn-009dcefc) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf08`](#insn-009dcf08) → [`0085b2a4`](../0085b/0085b2a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2a4` · 推定シンボル `None` · 推定型 `None`
- [`009dcf10`](#insn-009dcf10) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf18`](#insn-009dcf18) → [`0085b2ac`](../0085b/0085b2ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2ac` · 推定シンボル `None` · 推定型 `None`
- [`009dcf20`](#insn-009dcf20) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf2c`](#insn-009dcf2c) → [`0085b2ac`](../0085b/0085b2ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2ac` · 推定シンボル `None` · 推定型 `None`
- [`009dcf34`](#insn-009dcf34) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf3c`](#insn-009dcf3c) → [`0085b2b4`](../0085b/0085b2b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2b4` · 推定シンボル `None` · 推定型 `None`
- [`009dcf44`](#insn-009dcf44) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf4c`](#insn-009dcf4c) → [`0085b2b4`](../0085b/0085b2b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2b4` · 推定シンボル `None` · 推定型 `None`
- [`009dcf54`](#insn-009dcf54) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf5c`](#insn-009dcf5c) → [`0085b2bc`](../0085b/0085b2bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2bc` · 推定シンボル `None` · 推定型 `None`
- [`009dcf64`](#insn-009dcf64) → [`009dcf78`](#insn-009dcf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf6c`](#insn-009dcf6c) → [`0085b2bc`](../0085b/0085b2bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085b2bc` · 推定シンボル `None` · 推定型 `None`
- [`009dcf74`](#insn-009dcf74) → [`009dcf90`](#insn-009dcf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf7c`](#insn-009dcf7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf80`](#insn-009dcf80) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf84`](#insn-009dcf84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf88`](#insn-009dcf88) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dcf94`](#insn-009dcf94) → [`009dcf7c`](#insn-009dcf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dcecc`](#insn-009dcecc)

~~~json
{
  "source": "009dcecc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dced0`](#insn-009dced0)

~~~json
{
  "source": "009dced0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dced4`](#insn-009dced4)

~~~json
{
  "source": "009dced4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dced8`](#insn-009dced8)

~~~json
{
  "source": "009dced8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcef4`](#insn-009dcef4)

~~~json
{
  "source": "009dcef4",
  "target": "0085b2a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcefc`](#insn-009dcefc)

~~~json
{
  "source": "009dcefc",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf08`](#insn-009dcf08)

~~~json
{
  "source": "009dcf08",
  "target": "0085b2a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf10`](#insn-009dcf10)

~~~json
{
  "source": "009dcf10",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf18`](#insn-009dcf18)

~~~json
{
  "source": "009dcf18",
  "target": "0085b2ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf20`](#insn-009dcf20)

~~~json
{
  "source": "009dcf20",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf2c`](#insn-009dcf2c)

~~~json
{
  "source": "009dcf2c",
  "target": "0085b2ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf34`](#insn-009dcf34)

~~~json
{
  "source": "009dcf34",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf3c`](#insn-009dcf3c)

~~~json
{
  "source": "009dcf3c",
  "target": "0085b2b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf44`](#insn-009dcf44)

~~~json
{
  "source": "009dcf44",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf4c`](#insn-009dcf4c)

~~~json
{
  "source": "009dcf4c",
  "target": "0085b2b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf54`](#insn-009dcf54)

~~~json
{
  "source": "009dcf54",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf5c`](#insn-009dcf5c)

~~~json
{
  "source": "009dcf5c",
  "target": "0085b2bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf64`](#insn-009dcf64)

~~~json
{
  "source": "009dcf64",
  "target": "009dcf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf6c`](#insn-009dcf6c)

~~~json
{
  "source": "009dcf6c",
  "target": "0085b2bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dcf74`](#insn-009dcf74)

~~~json
{
  "source": "009dcf74",
  "target": "009dcf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf7c`](#insn-009dcf7c)

~~~json
{
  "source": "009dcf7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf80`](#insn-009dcf80)

~~~json
{
  "source": "009dcf80",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf84`](#insn-009dcf84)

~~~json
{
  "source": "009dcf84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf88`](#insn-009dcf88)

~~~json
{
  "source": "009dcf88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dcf94`](#insn-009dcf94)

~~~json
{
  "source": "009dcf94",
  "target": "009dcf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
