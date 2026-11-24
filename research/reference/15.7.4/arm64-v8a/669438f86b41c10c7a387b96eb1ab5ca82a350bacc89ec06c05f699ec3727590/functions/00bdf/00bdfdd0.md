# 00bdfdd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfd80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-52461e93fd628cd9801bff7119d8ebe4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-c18d8a0a3a8768b6a969f326752bff0a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdd0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a2ed35390aff70ab5754b42daaff7ff20670d67c6f09f264609af76c201ee29",
  "source_text_sha256": "7a2ed35390aff70ab5754b42daaff7ff20670d67c6f09f264609af76c201ee29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdd0",
        "00bdfddf"
      ]
    ],
    "bytes_sha256": "9e5025e776a2939b06309e97b551f8d39cbe904f351bcf0f1d0f081d24960ba6",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b39e10](../00b39/00b39e10.md)

## 呼び出し先

- [00b3ad98](../00b3a/00b3ad98.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 379 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEbT0_SB_T__00c1e7a0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdd0"></a> `00bdfdd0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdd4"></a> `00bdfdd4` | `11 d2 43 f9` | ldr x17,[x16, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bdfdd8"></a> `00bdfdd8` | `10 82 1e 91` | add x16,x16,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bdfddc"></a> `00bdfddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdd0`](#insn-00bdfdd0) 範囲 `[['00bdfdd0', '00bdfddf']]`

## 命令位置別の参照

- [`00bdfdd4`](#insn-00bdfdd4) → `00c1e7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfddc`](#insn-00bdfddc) → [`00b3ad98`](../00b3a/00b3ad98.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3ad98` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdd4`](#insn-00bdfdd4)

~~~json
{
  "source": "00bdfdd4",
  "target": "00c1e7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfddc`](#insn-00bdfddc)

~~~json
{
  "source": "00bdfddc",
  "target": "00b3ad98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
