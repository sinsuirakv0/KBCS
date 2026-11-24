# 007feeec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0067.md#review-ba54f0f6345426e0445e93d729babe80)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007feeec",
  "name": "FUN_007feeec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a0260f4b6b5c41e61ef793e15d4ac6b2e964beb4c5b5e517911fc30ae1a536f2",
  "source_text_sha256": "a0260f4b6b5c41e61ef793e15d4ac6b2e964beb4c5b5e517911fc30ae1a536f2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007feeec",
        "007fef07"
      ]
    ],
    "bytes_sha256": "7639582cdd48b4e15bbbe0dcee9f5133ee90a81c8c54366bc8ee8c3d0eadcfec",
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

## 疑似コード / UTF-8 287 bytes

~~~c

long FUN_007feeec(long param_1,long param_2)

{
  param_1 = param_1 + 8;
                    /* try { // try from 007fef00 to 008fef1b has its CatchHandler @ 007ff000 */
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9MapUpdateEvE4$_69") {
    param_1 = 0;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007feeec"></a> `007feeec` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-007feef0"></a> `007feef0` | `69 d7 ff b0` | adrp x9,0x2eb000 | `FALL_THROUGH`
<a id="insn-007feef4"></a> `007feef4` | `29 69 2f 91` | add x9,x9,#0xbda | `FALL_THROUGH`
<a id="insn-007feef8"></a> `007feef8` | `0a 20 00 91` | add x10,x0,#0x8 | `FALL_THROUGH`
<a id="insn-007feefc"></a> `007feefc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007fef00"></a> `007fef00` | `40 01 9f 9a` | csel x0,x10,xzr,eq | `FALL_THROUGH`
<a id="insn-007fef04"></a> `007fef04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007feeec`](#insn-007feeec) 範囲 `[['007feeec', '007feeff']]`
  - `FALL_THROUGH` [`007feefc`](#insn-007feefc) → [`007fef00`](#insn-007fef00)
- ブロック [`007fef00`](#insn-007fef00) 範囲 `[['007fef00', '007fef07']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

