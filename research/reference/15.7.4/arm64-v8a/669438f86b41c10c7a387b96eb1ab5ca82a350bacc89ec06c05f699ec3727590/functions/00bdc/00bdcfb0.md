# 00bdcfb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcf60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-7d98b5415a53da75a5934291fc06b636)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59a00`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59a00.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0010.md#compare-ce93f85e4e47f69db27093055ae539f1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfb0",
  "name": "_ZNK5Botan10Extensions10extensionsEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3192197c28941503674bdd9b8fcecf84c968059591ec07a086d363f994d1124",
  "source_text_sha256": "e3192197c28941503674bdd9b8fcecf84c968059591ec07a086d363f994d1124",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfb0",
        "00bdcfbf"
      ]
    ],
    "bytes_sha256": "190d8c462a4e8a7fe8591f21afa164a07d9ca317bb6d27463eb3274c7d78d7c0",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [004f4030](../004f4/004f4030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZNK5Botan10Extensions10extensionsEv(void)

{
  (*(code *)PTR__ZNK5Botan10Extensions10extensionsEv_00c1d090)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfb0"></a> `00bdcfb0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfb4"></a> `00bdcfb4` | `11 4a 40 f9` | ldr x17,[x16, #0x90] | `FALL_THROUGH`
<a id="insn-00bdcfb8"></a> `00bdcfb8` | `10 42 02 91` | add x16,x16,#0x90 | `FALL_THROUGH`
<a id="insn-00bdcfbc"></a> `00bdcfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfb0`](#insn-00bdcfb0) 範囲 `[['00bdcfb0', '00bdcfbf']]`

## 命令位置別の参照

- [`00bdcfb4`](#insn-00bdcfb4) → `00c1d090`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfbc`](#insn-00bdcfbc) → [`004f4030`](../004f4/004f4030.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f4030` · 推定シンボル `_ZNK5Botan10Extensions10extensionsEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfb4`](#insn-00bdcfb4)

~~~json
{
  "source": "00bdcfb4",
  "target": "00c1d090",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d090",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfbc`](#insn-00bdcfbc)

~~~json
{
  "source": "00bdcfbc",
  "target": "004f4030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
