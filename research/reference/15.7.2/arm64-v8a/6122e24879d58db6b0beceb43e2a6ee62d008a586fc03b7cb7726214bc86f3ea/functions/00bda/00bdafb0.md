# 00bdafb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdb060`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb060.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-0fbb6ca83aab9fe733ec0520a3b19ddd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafb0",
  "name": "_ZNSt11logic_errorD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d0fae24e2e4ad5bc1cec8a24419374e4c8683d39170d80c0a725093676eec5d4",
  "source_text_sha256": "d0fae24e2e4ad5bc1cec8a24419374e4c8683d39170d80c0a725093676eec5d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafb0",
        "00bdafbf"
      ]
    ],
    "bytes_sha256": "ead44ba5a62b80a8d15dded7caf12af23a2389864ee9349f5d910958cc1a4603",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbaec8](../00bba/00bbaec8.md)

## 呼び出し先

- [00bbad50](../00bba/00bbad50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 103 bytes

~~~c

void _ZNSt11logic_errorD1Ev(void)

{
  (*(code *)PTR__ZNSt11logic_errorD1Ev_00c1c010)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafb0"></a> `00bdafb0` | `10 02 00 d0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdafb4"></a> `00bdafb4` | `11 0a 40 f9` | ldr x17,[x16, #0x10] | `FALL_THROUGH`
<a id="insn-00bdafb8"></a> `00bdafb8` | `10 42 00 91` | add x16,x16,#0x10 | `FALL_THROUGH`
<a id="insn-00bdafbc"></a> `00bdafbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafb0`](#insn-00bdafb0) 範囲 `[['00bdafb0', '00bdafbf']]`

## 命令位置別の参照

- [`00bdafb4`](#insn-00bdafb4) → `00c1c010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdafbc`](#insn-00bdafbc) → [`00bbad50`](../00bba/00bbad50.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bbad50` · 推定シンボル `_ZNSt11logic_errorD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafb4`](#insn-00bdafb4)

~~~json
{
  "source": "00bdafb4",
  "target": "00c1c010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdafbc`](#insn-00bdafbc)

~~~json
{
  "source": "00bdafbc",
  "target": "00bbad50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
