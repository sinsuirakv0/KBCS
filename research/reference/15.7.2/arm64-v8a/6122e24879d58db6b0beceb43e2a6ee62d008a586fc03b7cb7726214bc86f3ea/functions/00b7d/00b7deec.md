# 00b7deec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0021.md#review-cb3d8233e005a777efdf13ab5943a75c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7deec",
  "name": "FUN_00b7deec",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c299d01d83e58df18a64ab0438a55e8b0ea9408207c8ecce7704a2ba6dc4d19a",
  "source_text_sha256": "c299d01d83e58df18a64ab0438a55e8b0ea9408207c8ecce7704a2ba6dc4d19a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7deec",
        "00b7defb"
      ]
    ],
    "bytes_sha256": "c71baf7bbae9857e57ee4ab97e6440227bcb98401ace6d71990dbd6024a866f4",
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

char * FUN_00b7deec(void)

{
  return "iostream";
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7deec"></a> `00b7deec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00b7def0"></a> `00b7def0` | `60 b9 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00b7def4"></a> `00b7def4` | `00 e0 03 91` | add x0,x0,#0xf8 | `FALL_THROUGH`
<a id="insn-00b7def8"></a> `00b7def8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7deec`](#insn-00b7deec) 範囲 `[['00b7deec', '00b7defb']]`

## 命令位置別の参照

- [`00b7def4`](#insn-00b7def4) → `002a90f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7def4`](#insn-00b7def4)

~~~json
{
  "source": "00b7def4",
  "target": "002a90f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a90f8",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "696f73747265616d00",
  "capture_start": "002a90f8",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
