# 00bdfbd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-4d4e462835acbeaf77d303696c95fab4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbd0",
  "name": "_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ed5b3aad97713711a47c52be059866b4cb21a22029ccade7bb9e3ebad159e94",
  "source_text_sha256": "1ed5b3aad97713711a47c52be059866b4cb21a22029ccade7bb9e3ebad159e94",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbd0",
        "00bdfbdf"
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

- [00b11350](../00b11/00b11350.md)
- [00b115bc](../00b11/00b115bc.md)
- [00b22f20](../00b22/00b22f20.md)
- [00b2aa3c](../00b2a/00b2aa3c.md)
- [00b2b6b0](../00b2b/00b2b6b0.md)
- [00b2c914](../00b2c/00b2c914.md)
- [00b2db64](../00b2d/00b2db64.md)

## 呼び出し先

- [00b3f044](../00b3f/00b3f044.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 690 bytes

~~~c

void _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_
               (void)

{
                    /* catch() { ... } // from try @ 00bdfdb0 with catch @ 00bdfbd4 */
  (*(code *)
    PTR__ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT__00c1e620
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfbd0"></a> `00bdfbd0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfbd4"></a> `00bdfbd4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bdfbd8"></a> `00bdfbd8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bdfbdc"></a> `00bdfbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbd0`](#insn-00bdfbd0) 範囲 `[['00bdfbd0', '00bdfbd3']]`
  - `FALL_THROUGH` [`00bdfbd0`](#insn-00bdfbd0) → [`00bdfbd4`](#insn-00bdfbd4)
- ブロック [`00bdfbd4`](#insn-00bdfbd4) 範囲 `[['00bdfbd4', '00bdfbdf']]`

## 命令位置別の参照

- [`00bdfbd4`](#insn-00bdfbd4) → `00c1e620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfbdc`](#insn-00bdfbdc) → [`00b3f044`](../00b3f/00b3f044.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3f044` · 推定シンボル `_ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE4findIS7_EENS_21__tree_const_iteratorISB_PNS_11__tree_nodeISB_PvEElEERKT_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbd4`](#insn-00bdfbd4)

~~~json
{
  "source": "00bdfbd4",
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
- 参照命令 [`00bdfbdc`](#insn-00bdfbdc)

~~~json
{
  "source": "00bdfbdc",
  "target": "00b3f044",
  "target_space": "ram",
  "resolution": "function"
}
~~~
