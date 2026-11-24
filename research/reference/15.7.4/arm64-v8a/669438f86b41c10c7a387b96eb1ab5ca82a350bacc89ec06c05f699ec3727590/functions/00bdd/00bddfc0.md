# 00bddfc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-b7ab06d2ec76604f38e3b9509a0877cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5aa40`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa40.md) · 移動量 `+0x7ca80`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-b213112f2ba4c6e10f783e6ca7c61826)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfc0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fbdb5ae5207b3ee41c7b1c8e87a374435223aa1496391fbd876536b3c0d9f406",
  "source_text_sha256": "fbdb5ae5207b3ee41c7b1c8e87a374435223aa1496391fbd876536b3c0d9f406",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfc0",
        "00bddfcf"
      ]
    ],
    "bytes_sha256": "bb58510c9e749c542285d7422a160abc8a38cfd121f2e2280ecf0f0c5b7b08ce",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2c0c](../00ae2/00ae2c0c.md)
- [00ae2fd4](../00ae2/00ae2fd4.md)
- [00b0067c](../00b00/00b0067c.md)
- [00b01560](../00b01/00b01560.md)
- [00b0df74](../00b0d/00b0df74.md)
- [00b4b6cc](../00b4b/00b4b6cc.md)
- [00b4d248](../00b4d/00b4d248.md)
- [00b4d7ec](../00b4d/00b4d7ec.md)
- [00b4de48](../00b4d/00b4de48.md)
- [00b4e484](../00b4e/00b4e484.md)
- [00b564f4](../00b56/00b564f4.md)
- [00b56820](../00b56/00b56820.md)
- [00b56b4c](../00b56/00b56b4c.md)
- [00b56e78](../00b56/00b56e78.md)
- [00b571a0](../00b57/00b571a0.md)
- [00b57438](../00b57/00b57438.md)
- [00b57b4c](../00b57/00b57b4c.md)
- [00b58108](../00b58/00b58108.md)
- [00b5e288](../00b5e/00b5e288.md)
- [00b5e964](../00b5e/00b5e964.md)
- [00b5eda0](../00b5e/00b5eda0.md)
- [00b5fb88](../00b5f/00b5fb88.md)
- [00b6aae8](../00b6a/00b6aae8.md)
- [00b6c244](../00b6c/00b6c244.md)
- [00b6eef0](../00b6e/00b6eef0.md)
- [00b6fe28](../00b6f/00b6fe28.md)
- [00b70050](../00b70/00b70050.md)
- [00b70b28](../00b70/00b70b28.md)
- [00b70d18](../00b70/00b70d18.md)
- [00b7116c](../00b71/00b7116c.md)
- [00b7135c](../00b71/00b7135c.md)
- [00b71584](../00b71/00b71584.md)

## 呼び出し先

- [00afed40](../00afe/00afed40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E_00c1d898)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfc0"></a> `00bddfc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfc4"></a> `00bddfc4` | `11 4e 44 f9` | ldr x17,[x16, #0x898] | `FALL_THROUGH`
<a id="insn-00bddfc8"></a> `00bddfc8` | `10 62 22 91` | add x16,x16,#0x898 | `FALL_THROUGH`
<a id="insn-00bddfcc"></a> `00bddfcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfc0`](#insn-00bddfc0) 範囲 `[['00bddfc0', '00bddfcf']]`

## 命令位置別の参照

- [`00bddfc4`](#insn-00bddfc4) → `00c1d898`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfcc`](#insn-00bddfcc) → [`00afed40`](../00afe/00afed40.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afed40` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfc4`](#insn-00bddfc4)

~~~json
{
  "source": "00bddfc4",
  "target": "00c1d898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d898",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfcc`](#insn-00bddfcc)

~~~json
{
  "source": "00bddfcc",
  "target": "00afed40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
