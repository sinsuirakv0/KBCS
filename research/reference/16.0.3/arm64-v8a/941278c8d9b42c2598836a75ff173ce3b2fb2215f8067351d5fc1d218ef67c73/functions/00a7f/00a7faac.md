# 00a7faac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a7eab8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7e/00a7eab8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0064.md#compare-feebc591d69df4596ba91505e8b25698)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7faac",
  "name": "FUN_00a7faac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a775e1265f8f3ba8d138be4d9c89107367a69c61bba23ea7804677201c8076b4",
  "source_text_sha256": "a775e1265f8f3ba8d138be4d9c89107367a69c61bba23ea7804677201c8076b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7faac",
        "00a7fabb"
      ]
    ],
    "bytes_sha256": "93fb62da2069a5aabe5086358a19639abad3a26c4dd5bf5d8a4bf625b2f14f1f",
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

void FUN_00a7faac(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c8d1c0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7faac"></a> `00a7faac` | `68 10 00 d0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00a7fab0"></a> `00a7fab0` | `08 01 07 91` | add x8,x8,#0x1c0 | `FALL_THROUGH`
<a id="insn-00a7fab4"></a> `00a7fab4` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00a7fab8"></a> `00a7fab8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7faac`](#insn-00a7faac) 範囲 `[['00a7faac', '00a7fabb']]`

## 命令位置別の参照

- [`00a7fab4`](#insn-00a7fab4) → `00c8d1c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7fab4`](#insn-00a7fab4)

~~~json
{
  "source": "00a7fab4",
  "target": "00c8d1c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d1c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
