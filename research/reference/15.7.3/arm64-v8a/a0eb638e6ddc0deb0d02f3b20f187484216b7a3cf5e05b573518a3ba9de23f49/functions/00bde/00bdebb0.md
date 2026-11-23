# 00bdebb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdeb00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-ab357e3324cc19ddfd0c3a799a2a81d2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdec00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-6c54be6cea233eacc1f41b72d5aee46b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebb0",
  "name": "_ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aa4c3303ee0a5973770f98372128fced5142c3354004a5c957abbe40349850e",
  "source_text_sha256": "7aa4c3303ee0a5973770f98372128fced5142c3354004a5c957abbe40349850e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebb0",
        "00bdebbf"
      ]
    ],
    "bytes_sha256": "cf791693e99f8403f320b3c32dcf5777ecc22197bffc830a5a0179716393546c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0a478](../00b0a/00b0a478.md)
- [00b0d178](../00b0d/00b0d178.md)
- [00b3fc88](../00b3f/00b3fc88.md)

## 呼び出し先

- [00b0d178](../00b0d/00b0d178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 345 bytes

~~~c

void _ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE_00c1de68
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebb0"></a> `00bdebb0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdebb4"></a> `00bdebb4` | `11 36 47 f9` | ldr x17,[x16, #0xe68] | `FALL_THROUGH`
<a id="insn-00bdebb8"></a> `00bdebb8` | `10 a2 39 91` | add x16,x16,#0xe68 | `FALL_THROUGH`
<a id="insn-00bdebbc"></a> `00bdebbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebb0`](#insn-00bdebb0) 範囲 `[['00bdebb0', '00bdebbf']]`

## 命令位置別の参照

- [`00bdebb4`](#insn-00bdebb4) → `00c1de68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdebbc`](#insn-00bdebbc) → [`00b0d178`](../00b0d/00b0d178.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0d178` · 推定シンボル `_ZNSt6__ndk16__treeINS_4pairImmEEN11flexbuffers7Builder19StringOffsetCompareENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebb4`](#insn-00bdebb4)

~~~json
{
  "source": "00bdebb4",
  "target": "00c1de68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdebbc`](#insn-00bdebbc)

~~~json
{
  "source": "00bdebbc",
  "target": "00b0d178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
