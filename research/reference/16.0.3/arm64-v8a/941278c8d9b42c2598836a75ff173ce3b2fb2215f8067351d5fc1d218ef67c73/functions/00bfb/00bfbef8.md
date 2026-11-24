# 00bfbef8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/review-0083.md#review-7025559cc7922b1237dce2a265ea619e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbef8",
  "name": "FUN_00bfbef8",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "002411f15edbde63ef3830eca5af7a6b05b8ee5797951e83d61840165b59ee5b",
  "source_text_sha256": "002411f15edbde63ef3830eca5af7a6b05b8ee5797951e83d61840165b59ee5b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbef8",
        "00bfbf07"
      ]
    ],
    "bytes_sha256": "4ebbb56f37579f8221c377f54e7c8a37511d9acf86acc91a2727da53caea6c54",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 関連文字列（未確認候補）

~~~text
"iostream"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 54 bytes

~~~c

char * FUN_00bfbef8(void)

{
  return "iostream";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbef8"></a> `00bfbef8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbefc"></a> `00bfbefc` | `e0 b5 ff d0` | adrp x0,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bfbf00"></a> `00bfbf00` | `00 7c 39 91` | add x0,x0,#0xe5f | `FALL_THROUGH`
<a id="insn-00bfbf04"></a> `00bfbf04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbef8`](#insn-00bfbef8) 範囲 `[['00bfbef8', '00bfbf07']]`

## 命令位置別の参照

- [`00bfbf00`](#insn-00bfbf00) → `002b9e5f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbf00`](#insn-00bfbf00)

~~~json
{
  "source": "00bfbf00",
  "target": "002b9e5f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9e5f",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "696f73747265616d00",
  "capture_start": "002b9e5f",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
