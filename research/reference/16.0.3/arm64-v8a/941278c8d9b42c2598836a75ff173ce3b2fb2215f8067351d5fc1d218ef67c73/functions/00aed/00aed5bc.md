# 00aed5bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aec5c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec5c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0067.md#compare-b6ecf6f4f0769635cbd9cf6f30034a6d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed5bc",
  "name": "FUN_00aed5bc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ae2a36994eec5eb70190b1a5fde2c70cd58c0224006e448b6e05a80a74baf3d",
  "source_text_sha256": "4ae2a36994eec5eb70190b1a5fde2c70cd58c0224006e448b6e05a80a74baf3d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed5bc",
        "00aed5df"
      ]
    ],
    "bytes_sha256": "c6c099ad7e8a5aab4bb5e8d8d918cca4d94ad4aaeda967c26277eff70ad07807",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00aed33c](../00aed/00aed33c.md)
- [00c58f50](../00c58/00c58f50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 87 bytes

~~~c

void FUN_00aed5bc(void *param_1)

{
  FUN_00aed33c();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed5bc"></a> `00aed5bc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aed5c0"></a> `00aed5c0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed5c4"></a> `00aed5c4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aed5c8"></a> `00aed5c8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aed5cc"></a> `00aed5cc` | `5c ff ff 97` | bl 0x00aed33c | `UNCONDITIONAL_CALL`
<a id="insn-00aed5d0"></a> `00aed5d0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed5d4"></a> `00aed5d4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed5d8"></a> `00aed5d8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed5dc"></a> `00aed5dc` | `5d ae 05 14` | b 0x00c58f50 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed5bc`](#insn-00aed5bc) 範囲 `[['00aed5bc', '00aed5df']]`

## 命令位置別の参照

- [`00aed5bc`](#insn-00aed5bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5c0`](#insn-00aed5c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5cc`](#insn-00aed5cc) → [`00aed33c`](00aed33c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aed33c` · 推定シンボル `None` · 推定型 `None`
- [`00aed5d4`](#insn-00aed5d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5d8`](#insn-00aed5d8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed5dc`](#insn-00aed5dc) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed5bc`](#insn-00aed5bc)

~~~json
{
  "source": "00aed5bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5c0`](#insn-00aed5c0)

~~~json
{
  "source": "00aed5c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5cc`](#insn-00aed5cc)

~~~json
{
  "source": "00aed5cc",
  "target": "00aed33c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed5d4`](#insn-00aed5d4)

~~~json
{
  "source": "00aed5d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5d8`](#insn-00aed5d8)

~~~json
{
  "source": "00aed5d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed5dc`](#insn-00aed5dc)

~~~json
{
  "source": "00aed5dc",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
