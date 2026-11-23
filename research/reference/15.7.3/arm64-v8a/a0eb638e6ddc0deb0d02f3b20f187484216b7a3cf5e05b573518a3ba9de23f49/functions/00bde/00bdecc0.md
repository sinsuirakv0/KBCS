# 00bdecc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdec10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-3e37e8e6aec922822c05cd2c4a242878)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bded10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-79bda3ffe73630c81da58d02fbc6509e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdecc0",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "651fe61529a1081231166acbbd4cb8991b259ef5a85fd1c9d8519feb0e80ba25",
  "source_text_sha256": "651fe61529a1081231166acbbd4cb8991b259ef5a85fd1c9d8519feb0e80ba25",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdecc0",
        "00bdeccf"
      ]
    ],
    "bytes_sha256": "fa5304318e620bc786a8b6dc0d948b5d5797b46d97640f93b4d151ffa1dfeeff",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afc5ac](../00afc/00afc5ac.md)
- [00afce40](../00afc/00afce40.md)

## 呼び出し先

- [00afce40](../00afc/00afce40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 437 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE_00c1def0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdecc0"></a> `00bdecc0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdecc4"></a> `00bdecc4` | `11 7a 47 f9` | ldr x17,[x16, #0xef0] | `FALL_THROUGH`
<a id="insn-00bdecc8"></a> `00bdecc8` | `10 c2 3b 91` | add x16,x16,#0xef0 | `FALL_THROUGH`
<a id="insn-00bdeccc"></a> `00bdeccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdecc0`](#insn-00bdecc0) 範囲 `[['00bdecc0', '00bdeccf']]`

## 命令位置別の参照

- [`00bdecc4`](#insn-00bdecc4) → `00c1def0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeccc`](#insn-00bdeccc) → [`00afce40`](../00afc/00afce40.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afce40` · 推定シンボル `_ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdecc4`](#insn-00bdecc4)

~~~json
{
  "source": "00bdecc4",
  "target": "00c1def0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1def0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeccc`](#insn-00bdeccc)

~~~json
{
  "source": "00bdeccc",
  "target": "00afce40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
