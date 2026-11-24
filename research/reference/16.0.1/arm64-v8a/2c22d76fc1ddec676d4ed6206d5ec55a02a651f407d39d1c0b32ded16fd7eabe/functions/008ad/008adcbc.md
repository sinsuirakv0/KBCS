# 008adcbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0073.md#review-b17b9168866eaf8ca1fb40e2d1123024)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0033.md#review-b17b9168866eaf8ca1fb40e2d1123024)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008adcbc",
  "name": "FUN_008adcbc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "769df90688d74d78c2c5fe3e722ec92f619257940795aae03a4cb1f8423297a3",
  "source_text_sha256": "769df90688d74d78c2c5fe3e722ec92f619257940795aae03a4cb1f8423297a3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008adcbc",
        "008adcd7"
      ]
    ],
    "bytes_sha256": "b7e91312e7880398618683a9c9bd35b62d851d2109ac51ceb4e5d3e154a2980c",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 616 bytes

~~~c

long FUN_008adcbc(long param_1,long param_2)

{
                    /* catch() { ... } // from try @ 008ada2c with catch @ 008adcbc */
                    /* catch() { ... } // from try @ 008ada24 with catch @ 008adcc4 */
  param_1 = param_1 + 8;
                    /* catch() { ... } // from try @ 008ada80 with catch @ 008adccc */
  if (*(char **)(param_2 + 8) !=
      "ZZN17MyUtilityListener22nekokanBrowserFunctionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEENK3$_1clEN10NyankoClub6ResultEiEUlP9NewDialog20NewDialogChangeStateiE0_"
     ) {
    param_1 = 0;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008adcbc"></a> `008adcbc` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-008adcc0"></a> `008adcc0` | `49 d2 ff d0` | adrp x9,0x2f7000 | `FALL_THROUGH`
<a id="insn-008adcc4"></a> `008adcc4` | `29 41 31 91` | add x9,x9,#0xc50 | `FALL_THROUGH`
<a id="insn-008adcc8"></a> `008adcc8` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-008adccc"></a> `008adccc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008adcd0"></a> `008adcd0` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-008adcd4"></a> `008adcd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008adcbc`](#insn-008adcbc) 範囲 `[['008adcbc', '008adcc3']]`
  - `FALL_THROUGH` [`008adcc0`](#insn-008adcc0) → [`008adcc4`](#insn-008adcc4)
- ブロック [`008adcc4`](#insn-008adcc4) 範囲 `[['008adcc4', '008adccb']]`
  - `FALL_THROUGH` [`008adcc8`](#insn-008adcc8) → [`008adccc`](#insn-008adccc)
- ブロック [`008adccc`](#insn-008adccc) 範囲 `[['008adccc', '008adcd7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

