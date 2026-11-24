# 00bdefa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdef50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-4a5a3072cbf6c8d22a0879612ea1784e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5ba50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md) · 移動量 `+0x7cab0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-308fb0c0a102c08e004483495a59504a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefa0",
  "name": "_Znam",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bea15461be96060a9e07dcbd66d7baa575f2229c97e023aff511ec4868be9836",
  "source_text_sha256": "bea15461be96060a9e07dcbd66d7baa575f2229c97e023aff511ec4868be9836",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefa0",
        "00bdefaf"
      ]
    ],
    "bytes_sha256": "7f1c56509f5c65657645c4d62d0cb65ffb7be3bdd18050f78bf4ef4704061b13",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b035c0](../00b03/00b035c0.md)
- [00b2e634](../00b2e/00b2e634.md)
- [00b47c5c](../00b47/00b47c5c.md)
- [00b47d4c](../00b47/00b47d4c.md)
- [00b57438](../00b57/00b57438.md)
- [00b590b0](../00b59/00b590b0.md)
- [00bd4ee0](../00bd4/00bd4ee0.md)

## 呼び出し先

- [00bdaf10](../00bda/00bdaf10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 69 bytes

~~~c

void _Znam(void)

{
  (*(code *)PTR__Znam_00c1e088)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefa0"></a> `00bdefa0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefa4"></a> `00bdefa4` | `11 46 40 f9` | ldr x17,[x16, #0x88] | `FALL_THROUGH`
<a id="insn-00bdefa8"></a> `00bdefa8` | `10 22 02 91` | add x16,x16,#0x88 | `FALL_THROUGH`
<a id="insn-00bdefac"></a> `00bdefac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefa0`](#insn-00bdefa0) 範囲 `[['00bdefa0', '00bdefaf']]`

## 命令位置別の参照

- [`00bdefa4`](#insn-00bdefa4) → `00c1e088`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefac`](#insn-00bdefac) → [`00bdaf10`](../00bda/00bdaf10.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bdaf10` · 推定シンボル `_Znam` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefa4`](#insn-00bdefa4)

~~~json
{
  "source": "00bdefa4",
  "target": "00c1e088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e088",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefac`](#insn-00bdefac)

~~~json
{
  "source": "00bdefac",
  "target": "00bdaf10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
