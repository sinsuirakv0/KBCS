# 00aaefdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aadfe8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aad/00aadfe8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-367cb6ab98b514684f1dbc801acf3b41)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaefdc",
  "name": "FUN_00aaefdc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eda7ed1bf5acf89ebd162eb84be0b04df805e1e6b83b4cc8513ed303bc7bee42",
  "source_text_sha256": "eda7ed1bf5acf89ebd162eb84be0b04df805e1e6b83b4cc8513ed303bc7bee42",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaefdc",
        "00aaefef"
      ]
    ],
    "bytes_sha256": "fd00e03e6473038d8ef8ddacc6e2662f5e08ef9c22813d9a94e092204b82a99a",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00796a68](../00796/00796a68.md)

## 呼び出し先

- [00b343b0](../00b34/00b343b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 285 bytes

~~~c

void FUN_00aaefdc(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
                    /* catch() { ... } // from try @ 00aaef38 with catch @ 00aaefe4 */
  FUN_00b343b0(param_2,param_3,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaefdc"></a> `00aaefdc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaefe0"></a> `00aaefe0` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00aaefe4"></a> `00aaefe4` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00aaefe8"></a> `00aaefe8` | `e3 03 04 aa` | mov x3,x4 | `FALL_THROUGH`
<a id="insn-00aaefec"></a> `00aaefec` | `f1 14 02 14` | b 0x00b343b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaefdc`](#insn-00aaefdc) 範囲 `[['00aaefdc', '00aaefe3']]`
  - `FALL_THROUGH` [`00aaefe0`](#insn-00aaefe0) → [`00aaefe4`](#insn-00aaefe4)
- ブロック [`00aaefe4`](#insn-00aaefe4) 範囲 `[['00aaefe4', '00aaefef']]`

## 命令位置別の参照

- [`00aaefec`](#insn-00aaefec) → [`00b343b0`](../00b34/00b343b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b343b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaefec`](#insn-00aaefec)

~~~json
{
  "source": "00aaefec",
  "target": "00b343b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
