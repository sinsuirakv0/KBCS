# 00bdfee0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfe90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-27c81f2793be1f96fa93b0b918687baf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-fe25537b64a87cf17a2045e4e83914e2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfee0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19__map_value_compareIS7_SD_SA_Lb1EEENS5_ISD_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2b671761cf7d251c65957eb3b3745c4872afe39df872bcc7ee4cee6bebd3cdb",
  "source_text_sha256": "b2b671761cf7d251c65957eb3b3745c4872afe39df872bcc7ee4cee6bebd3cdb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfee0",
        "00bdfeef"
      ]
    ],
    "bytes_sha256": "e7a37950afeb5e24d3644b003df04195fb61e52c29453b02a56bfa3cd65b767c",
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
- [00b284c4](../00b28/00b284c4.md)

## 呼び出し先

- [00b446a0](../00b44/00b446a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 615 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19__map_value_compareIS7_SD_SA_Lb1EEENS5_ISD_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19__map_value_compareIS7_SD_SA_Lb1EEENS5_ISD_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT__00c1e828
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfee0"></a> `00bdfee0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfee4"></a> `00bdfee4` | `11 16 44 f9` | ldr x17,[x16, #0x828] | `FALL_THROUGH`
<a id="insn-00bdfee8"></a> `00bdfee8` | `10 a2 20 91` | add x16,x16,#0x828 | `FALL_THROUGH`
<a id="insn-00bdfeec"></a> `00bdfeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfee0`](#insn-00bdfee0) 範囲 `[['00bdfee0', '00bdfeef']]`

## 命令位置別の参照

- [`00bdfee4`](#insn-00bdfee4) → `00c1e828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfeec`](#insn-00bdfeec) → [`00b446a0`](../00b44/00b446a0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b446a0` · 推定シンボル `_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3setIS7_NS_4lessIS7_EENS5_IS7_EEEEEENS_19__map_value_compareIS7_SD_SA_Lb1EEENS5_ISD_EEE12__find_equalIS7_EERPNS_16__tree_node_baseIPvEERPNS_15__tree_end_nodeISM_EERKT_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfee4`](#insn-00bdfee4)

~~~json
{
  "source": "00bdfee4",
  "target": "00c1e828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e828",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfeec`](#insn-00bdfeec)

~~~json
{
  "source": "00bdfeec",
  "target": "00b446a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
