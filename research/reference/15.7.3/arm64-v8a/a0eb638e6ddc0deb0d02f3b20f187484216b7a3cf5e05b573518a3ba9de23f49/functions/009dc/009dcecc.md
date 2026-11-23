# 009dcecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `009dcecc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009dc/009dcecc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0007.md#compare-1112eb0b8eaafea1862b4c6dba855653)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `009dcf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009dc/009dcf10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0001.md#compare-a8773a8877e2595cae60573cf7fe459f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dcecc",
  "name": "FUN_009dcecc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d",
  "source_text_sha256": "aecd03fc9fc09a1bbfd1d7270baee75e9de85b1c79f3e5cf02c9b89f59167f3d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009dcecc",
        "009dcedf"
      ]
    ],
    "bytes_sha256": "dfdba0f7a6b2db6d92a23f9faede606ebdc03c30ccbb4f2afbc8cb5aae6d4719",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009dcca0](../009dc/009dcca0.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 206 bytes

~~~c

void FUN_009dcecc(void)

{
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 009d9d58 with catch @ 009dcedc */
  FUN_00418c38("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009dcecc"></a> `009dcecc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-009dced0"></a> `009dced0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009dced4"></a> `009dced4` | `40 c6 ff f0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-009dced8"></a> `009dced8` | `00 0c 0c 91` | add x0,x0,#0x303 | `FALL_THROUGH`
<a id="insn-009dcedc"></a> `009dcedc` | `57 ef e8 97` | bl 0x00418c38 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009dcecc`](#insn-009dcecc) 範囲 `[['009dcecc', '009dcedb']]`
  - `FALL_THROUGH` [`009dced8`](#insn-009dced8) → [`009dcedc`](#insn-009dcedc)
- ブロック [`009dcedc`](#insn-009dcedc) 範囲 `[['009dcedc', '009dcedf']]`

## 命令位置別の参照

- [`009dcecc`](#insn-009dcecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dced8`](#insn-009dced8) → `002a7303`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009dcedc`](#insn-009dcedc) → [`00418c38`](../00418/00418c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c38` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dcecc`](#insn-009dcecc)

~~~json
{
  "source": "009dcecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dced8`](#insn-009dced8)

~~~json
{
  "source": "009dced8",
  "target": "002a7303",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7303",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002a7303",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009dcedc`](#insn-009dcedc)

~~~json
{
  "source": "009dcedc",
  "target": "00418c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
