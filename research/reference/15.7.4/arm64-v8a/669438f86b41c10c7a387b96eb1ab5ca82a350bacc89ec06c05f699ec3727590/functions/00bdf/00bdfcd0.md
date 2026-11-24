# 00bdfcd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-d7e6c9e9031885d132271eb03dcf5db7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5c6b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6b0.md) · 移動量 `+0x7c9e0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0015.md#compare-9fefcf554e8392d16cce309ba7878c50)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfcd0",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a6eb55d496c4a481bed118efefd6d40bba11f6c510090272c9f956530649bec1",
  "source_text_sha256": "a6eb55d496c4a481bed118efefd6d40bba11f6c510090272c9f956530649bec1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfcd0",
        "00bdfcdf"
      ]
    ],
    "bytes_sha256": "fd8bd8b1dd26854cf83cd2ebcb236d2eeb9f7260b9c4265943d715fb6a87ef6c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1145c](../00b11/00b1145c.md)
- [00b116c8](../00b11/00b116c8.md)
- [00b2302c](../00b23/00b2302c.md)
- [00b2ab48](../00b2a/00b2ab48.md)
- [00b2b7bc](../00b2b/00b2b7bc.md)
- [00b2ca20](../00b2c/00b2ca20.md)
- [00b2dc70](../00b2d/00b2dc70.md)

## 呼び出し先

- [00b3f150](../00b3f/00b3f150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 603 bytes

~~~c

void _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
               (void)

{
  (*(code *)
    PTR__ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT__00c1e720
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfcd0"></a> `00bdfcd0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfcd4"></a> `00bdfcd4` | `11 92 43 f9` | ldr x17,[x16, #0x720] | `FALL_THROUGH`
<a id="insn-00bdfcd8"></a> `00bdfcd8` | `10 82 1c 91` | add x16,x16,#0x720 | `FALL_THROUGH`
<a id="insn-00bdfcdc"></a> `00bdfcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfcd0`](#insn-00bdfcd0) 範囲 `[['00bdfcd0', '00bdfcdf']]`

## 命令位置別の参照

- [`00bdfcd4`](#insn-00bdfcd4) → `00c1e720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcdc`](#insn-00bdfcdc) → [`00b3f150`](../00b3f/00b3f150.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3f150` · 推定シンボル `_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfcd4`](#insn-00bdfcd4)

~~~json
{
  "source": "00bdfcd4",
  "target": "00c1e720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e720",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcdc`](#insn-00bdfcdc)

~~~json
{
  "source": "00bdfcdc",
  "target": "00b3f150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
