# 00aadfe8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aadf78`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aad/00aadf78.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/machine_only_observed-0020.md#compare-1cbe5ae774f9d23b78fdfedf277f6970)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aaefdc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aae/00aaefdc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-367cb6ab98b514684f1dbc801acf3b41)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadfe8",
  "name": "FUN_00aadfe8",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0265eafcfde2f13e7ca7f8285fd33219d10e24128d02a9becd32179d0995a6e",
  "source_text_sha256": "b0265eafcfde2f13e7ca7f8285fd33219d10e24128d02a9becd32179d0995a6e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aadfe8",
        "00aadffb"
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

- [0079668c](../00796/0079668c.md)

## 呼び出し先

- [00b333bc](../00b33/00b333bc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 198 bytes

~~~c

void FUN_00aadfe8(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
                 undefined8 param_5)

{
  FUN_00b333bc(param_2,param_3,param_4,param_5);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aadfe8"></a> `00aadfe8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aadfec"></a> `00aadfec` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00aadff0"></a> `00aadff0` | `e2 03 03 aa` | mov x2,x3 | `FALL_THROUGH`
<a id="insn-00aadff4"></a> `00aadff4` | `e3 03 04 aa` | mov x3,x4 | `FALL_THROUGH`
<a id="insn-00aadff8"></a> `00aadff8` | `f1 14 02 14` | b 0x00b333bc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aadfe8`](#insn-00aadfe8) 範囲 `[['00aadfe8', '00aadffb']]`

## 命令位置別の参照

- [`00aadff8`](#insn-00aadff8) → [`00b333bc`](../00b33/00b333bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b333bc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aadff8`](#insn-00aadff8)

~~~json
{
  "source": "00aadff8",
  "target": "00b333bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
