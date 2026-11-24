# 007ffeac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fef48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fe/007fef48.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0043.md#compare-aeb1b5c4c82ced2f3cfcc15056001e57)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffeac",
  "name": "FUN_007ffeac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57fe2703dbb9f392a55e9a15bc0466b5a74d6d95d5e055020f278b499ab5f9d2",
  "source_text_sha256": "57fe2703dbb9f392a55e9a15bc0466b5a74d6d95d5e055020f278b499ab5f9d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007ffeac",
        "007ffebb"
      ]
    ],
    "bytes_sha256": "318158c967174a91e319e76c51e91f8d08a4bd4027dfdd161220d15c815e195d",
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void FUN_007ffeac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c7efc0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007ffeac"></a> `007ffeac` | `e8 23 00 f0` | adrp x8,0xc7e000 | `FALL_THROUGH`
<a id="insn-007ffeb0"></a> `007ffeb0` | `08 01 3f 91` | add x8,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-007ffeb4"></a> `007ffeb4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-007ffeb8"></a> `007ffeb8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007ffeac`](#insn-007ffeac) 範囲 `[['007ffeac', '007ffebb']]`

## 命令位置別の参照

- [`007ffeb4`](#insn-007ffeb4) → `00c7efc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007ffeb4`](#insn-007ffeb4)

~~~json
{
  "source": "007ffeb4",
  "target": "00c7efc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7efc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
