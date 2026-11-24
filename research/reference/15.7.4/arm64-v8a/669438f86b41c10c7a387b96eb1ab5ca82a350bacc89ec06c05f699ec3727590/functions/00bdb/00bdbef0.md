# 00bdbef0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbea0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbea0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-fd4f0bafd55e9232abf83c977332f7bc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58940`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-ef8e5373a4e9ae7c06b2910c3fa33bdb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbef0",
  "name": "_ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d04149f870984caeb129c78da08d2e0fe8eb65e114212e9c6107a88d67c04da9",
  "source_text_sha256": "d04149f870984caeb129c78da08d2e0fe8eb65e114212e9c6107a88d67c04da9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbef0",
        "00bdbeff"
      ]
    ],
    "bytes_sha256": "69cb683290305b63699d733b1522dcd7662d65b199b7a61bbc8d767b79f75ad5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00498d9c](../00498/00498d9c.md)
- [0049e3f4](../0049e/0049e3f4.md)
- [004a3d70](../004a3/004a3d70.md)
- [004aa624](../004aa/004aa624.md)
- [004aab0c](../004aa/004aab0c.md)
- [004ab3f4](../004ab/004ab3f4.md)
- [004ade98](../004ad/004ade98.md)
- [004c1804](../004c1/004c1804.md)
- [004c3c00](../004c3/004c3c00.md)
- [004c43dc](../004c4/004c43dc.md)
- [004c8d94](../004c8/004c8d94.md)
- [004ecb70](../004ec/004ecb70.md)

## 呼び出し先

- [0049100c](../00491/0049100c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 245 bytes

~~~c

void _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE(void)

{
  (*(code *)
    PTR__ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1c830
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbef0"></a> `00bdbef0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbef4"></a> `00bdbef4` | `11 1a 44 f9` | ldr x17,[x16, #0x830] | `FALL_THROUGH`
<a id="insn-00bdbef8"></a> `00bdbef8` | `10 c2 20 91` | add x16,x16,#0x830 | `FALL_THROUGH`
<a id="insn-00bdbefc"></a> `00bdbefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbef0`](#insn-00bdbef0) 範囲 `[['00bdbef0', '00bdbeff']]`

## 命令位置別の参照

- [`00bdbef4`](#insn-00bdbef4) → `00c1c830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbefc`](#insn-00bdbefc) → [`0049100c`](../00491/0049100c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0049100c` · 推定シンボル `_ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbef4`](#insn-00bdbef4)

~~~json
{
  "source": "00bdbef4",
  "target": "00c1c830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbefc`](#insn-00bdbefc)

~~~json
{
  "source": "00bdbefc",
  "target": "0049100c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
