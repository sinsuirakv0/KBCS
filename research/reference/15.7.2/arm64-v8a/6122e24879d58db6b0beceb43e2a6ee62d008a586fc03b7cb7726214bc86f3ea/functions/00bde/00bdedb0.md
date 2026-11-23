# 00bdedb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdee60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-e7bef27580ed93b90ea1beba2a1beb05)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedb0",
  "name": "_ZN8firebase19CreateApiIdentifierEPKcPv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e199e599699cb4b7877f9ed1bced4ba70434752b8af47317bf5a81759560e0f",
  "source_text_sha256": "8e199e599699cb4b7877f9ed1bced4ba70434752b8af47317bf5a81759560e0f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedb0",
        "00bdedbf"
      ]
    ],
    "bytes_sha256": "2e11d4654a50c552e7dbcabb777057d27a691e87eced66cbe3b0764aedec7425",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b54a2c](../00b54/00b54a2c.md)
- [00b5ad5c](../00b5a/00b5ad5c.md)

## 呼び出し先

- [00b02648](../00b02/00b02648.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 137 bytes

~~~c

void _ZN8firebase19CreateApiIdentifierEPKcPv(void)

{
  (*(code *)PTR__ZN8firebase19CreateApiIdentifierEPKcPv_00c1df10)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedb0"></a> `00bdedb0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedb4"></a> `00bdedb4` | `11 8a 47 f9` | ldr x17,[x16, #0xf10] | `FALL_THROUGH`
<a id="insn-00bdedb8"></a> `00bdedb8` | `10 42 3c 91` | add x16,x16,#0xf10 | `FALL_THROUGH`
<a id="insn-00bdedbc"></a> `00bdedbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedb0`](#insn-00bdedb0) 範囲 `[['00bdedb0', '00bdedbf']]`

## 命令位置別の参照

- [`00bdedb4`](#insn-00bdedb4) → `00c1df10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdedbc`](#insn-00bdedbc) → [`00b02648`](../00b02/00b02648.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b02648` · 推定シンボル `_ZN8firebase19CreateApiIdentifierEPKcPv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedb4`](#insn-00bdedb4)

~~~json
{
  "source": "00bdedb4",
  "target": "00c1df10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdedbc`](#insn-00bdedbc)

~~~json
{
  "source": "00bdedbc",
  "target": "00b02648",
  "target_space": "ram",
  "resolution": "function"
}
~~~
