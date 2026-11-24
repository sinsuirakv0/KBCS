# 00bdfad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfa80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-4bd9c17beaeef202f90afd9b89c7c1dc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c470`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c470.md) · 移動量 `+0x7c9a0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0015.md#compare-e9abb2f7ac60493363c11c19ddbee3d6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfad0",
  "name": "_ZN11flatbuffers9PosixPathEPKc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54fe9d017021241c87090d4a7df28b7f40ae85f396f654fec4d94e10680c91d4",
  "source_text_sha256": "54fe9d017021241c87090d4a7df28b7f40ae85f396f654fec4d94e10680c91d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfad0",
        "00bdfadf"
      ]
    ],
    "bytes_sha256": "13968e645e2f8233fe249c78349a561e7c9cda174b917a4b648135842ac0ef54",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b26b28](../00b26/00b26b28.md)

## 呼び出し先

- [00b47568](../00b47/00b47568.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 119 bytes

~~~c

void _ZN11flatbuffers9PosixPathEPKc(void)

{
  (*(code *)PTR__ZN11flatbuffers9PosixPathEPKc_00c1e620)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfad0"></a> `00bdfad0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfad4"></a> `00bdfad4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bdfad8"></a> `00bdfad8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bdfadc"></a> `00bdfadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfad0`](#insn-00bdfad0) 範囲 `[['00bdfad0', '00bdfadf']]`

## 命令位置別の参照

- [`00bdfad4`](#insn-00bdfad4) → `00c1e620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfadc`](#insn-00bdfadc) → [`00b47568`](../00b47/00b47568.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b47568` · 推定シンボル `_ZN11flatbuffers9PosixPathEPKc` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfad4`](#insn-00bdfad4)

~~~json
{
  "source": "00bdfad4",
  "target": "00c1e620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfadc`](#insn-00bdfadc)

~~~json
{
  "source": "00bdfadc",
  "target": "00b47568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
