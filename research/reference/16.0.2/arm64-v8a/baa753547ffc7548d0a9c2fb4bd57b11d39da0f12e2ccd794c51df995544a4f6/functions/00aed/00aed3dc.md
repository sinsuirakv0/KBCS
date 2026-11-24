# 00aed3dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0080.md#review-62f66a7437aae4688f0fbcb4c95da57f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0042.md#review-62f66a7437aae4688f0fbcb4c95da57f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed3dc",
  "name": "FUN_00aed3dc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e",
  "source_text_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed3dc",
        "00aed3f7"
      ]
    ],
    "bytes_sha256": "137e96582eade7331bbad1403119761887f380560317d17fbf005322dda4cdf9",
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

## 疑似コード / UTF-8 383 bytes

~~~c

long FUN_00aed3dc(long param_1,long param_2)

{
                    /* try { // try from 00aed3e8 to 00bed3f3 has its CatchHandler @ 00aed5a4 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9pasteSlotEvE3$_0") {
    param_1 = 0;
  }
                    /* try { // try from 00aed3f4 to 00bed58b has its CatchHandler @ 00aed16c */
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed3dc"></a> `00aed3dc` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00aed3e0"></a> `00aed3e0` | `c9 c0 ff f0` | adrp x9,0x308000 | `FALL_THROUGH`
<a id="insn-00aed3e4"></a> `00aed3e4` | `29 85 09 91` | add x9,x9,#0x261 | `FALL_THROUGH`
<a id="insn-00aed3e8"></a> `00aed3e8` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00aed3ec"></a> `00aed3ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aed3f0"></a> `00aed3f0` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-00aed3f4"></a> `00aed3f4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed3dc`](#insn-00aed3dc) 範囲 `[['00aed3dc', '00aed3e7']]`
  - `FALL_THROUGH` [`00aed3e4`](#insn-00aed3e4) → [`00aed3e8`](#insn-00aed3e8)
- ブロック [`00aed3e8`](#insn-00aed3e8) 範囲 `[['00aed3e8', '00aed3f3']]`
  - `FALL_THROUGH` [`00aed3f0`](#insn-00aed3f0) → [`00aed3f4`](#insn-00aed3f4)
- ブロック [`00aed3f4`](#insn-00aed3f4) 範囲 `[['00aed3f4', '00aed3f7']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

