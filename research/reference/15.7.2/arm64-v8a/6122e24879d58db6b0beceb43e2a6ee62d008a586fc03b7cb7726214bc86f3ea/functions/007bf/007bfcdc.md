# 007bfcdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `007bfcdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bf/007bfcdc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0035.md#compare-066704c4b8ea50aeef92729a00bbe379)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007bfcdc",
  "name": "FUN_007bfcdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef",
  "source_text_sha256": "72f426465452901bfdf6813269710739ad60b1ed753273a40d300277fddc34ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007bfcdc",
        "007bfcef"
      ]
    ],
    "bytes_sha256": "4d6e03c43bbe856918efeac80ee5c1e598febc2ca4dd0b9d4d0e0b02904eeb79",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0078cd14](../0078c/0078cd14.md)
- [00796d74](../00796/00796d74.md)
- [007da86c](../007da/007da86c.md)
- [007dbc94](../007db/007dbc94.md)
- [007dc0fc](../007dc/007dc0fc.md)
- [009a3648](../009a3/009a3648.md)

## 呼び出し先

- [00418c38](../00418/00418c38.md)

## 関連文字列（未確認候補）

~~~text
"vector"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void FUN_007bfcdc(void)

{
                    /* WARNING: Subroutine does not return */
  FUN_00418c38("vector");
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007bfcdc"></a> `007bfcdc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-007bfce0"></a> `007bfce0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007bfce4"></a> `007bfce4` | `40 d7 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-007bfce8"></a> `007bfce8` | `00 28 0c 91` | add x0,x0,#0x30a | `FALL_THROUGH`
<a id="insn-007bfcec"></a> `007bfcec` | `d3 63 f1 97` | bl 0x00418c38 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007bfcdc`](#insn-007bfcdc) 範囲 `[['007bfcdc', '007bfcef']]`

## 命令位置別の参照

- [`007bfcdc`](#insn-007bfcdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007bfce8`](#insn-007bfce8) → `002a730a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`007bfcec`](#insn-007bfcec) → [`00418c38`](../00418/00418c38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c38` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007bfcdc`](#insn-007bfcdc)

~~~json
{
  "source": "007bfcdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007bfce8`](#insn-007bfce8)

~~~json
{
  "source": "007bfce8",
  "target": "002a730a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a730a",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "766563746f7200",
  "capture_start": "002a730a",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007bfcec`](#insn-007bfcec)

~~~json
{
  "source": "007bfcec",
  "target": "00418c38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
