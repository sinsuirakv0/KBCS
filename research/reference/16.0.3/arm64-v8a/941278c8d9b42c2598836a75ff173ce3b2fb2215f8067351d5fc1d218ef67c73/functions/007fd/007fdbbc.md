# 007fdbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fcc58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcc58.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0042.md#compare-251d1c8859eb1e3e9a056396d88d169d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fdbbc",
  "name": "FUN_007fdbbc",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17a9d6f4ea74845a63ea734f45131e6c60515f1828255a4c71dadb460659f759",
  "source_text_sha256": "17a9d6f4ea74845a63ea734f45131e6c60515f1828255a4c71dadb460659f759",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fdbbc",
        "007fdbd3"
      ]
    ],
    "bytes_sha256": "f4ab92155456f15d2d80740e0f31f95b0aa7c7039039757c2c5aa7e857f7a31c",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
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

## 疑似コード / UTF-8 204 bytes

~~~c

void FUN_007fdbbc(long param_1,undefined8 *param_2)

{
  undefined4 uVar1;
  
  uVar1 = *(undefined4 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c7e750;
  *(undefined4 *)(param_2 + 1) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fdbbc"></a> `007fdbbc` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fdbc0"></a> `007fdbc0` | `09 24 00 b0` | adrp x9,0xc7e000 | `FALL_THROUGH`
<a id="insn-007fdbc4"></a> `007fdbc4` | `29 41 1d 91` | add x9,x9,#0x750 | `FALL_THROUGH`
<a id="insn-007fdbc8"></a> `007fdbc8` | `29 00 00 f9` | str x9,[x1] | `FALL_THROUGH`
<a id="insn-007fdbcc"></a> `007fdbcc` | `28 08 00 b9` | str w8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-007fdbd0"></a> `007fdbd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fdbbc`](#insn-007fdbbc) 範囲 `[['007fdbbc', '007fdbd3']]`

## 命令位置別の参照

- [`007fdbc8`](#insn-007fdbc8) → `00c7e750`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fdbc8`](#insn-007fdbc8)

~~~json
{
  "source": "007fdbc8",
  "target": "00c7e750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7e750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
