# 00bdfdc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-1e8e67b5b21fb35f757b160df853850d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-388f0f76b7271d722764c335ed4141b5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdc0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3dede73b89011a106884680c9e7349452a465c70aa918ea06ff9212b22f2e31",
  "source_text_sha256": "c3dede73b89011a106884680c9e7349452a465c70aa918ea06ff9212b22f2e31",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdc0",
        "00bdfdcf"
      ]
    ],
    "bytes_sha256": "741b8439e5a17ba391fa48cebb60660d484f43d93ac41a1e9f7cb2abe3e21489",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b3c460](../00b3c/00b3c460.md)

## 呼び出し先

- [00b3d3e8](../00b3d/00b3d3e8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 377 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEbT0_SB_T__00c1e798
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdc0"></a> `00bdfdc0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdc4"></a> `00bdfdc4` | `11 ce 43 f9` | ldr x17,[x16, #0x798] | `FALL_THROUGH`
<a id="insn-00bdfdc8"></a> `00bdfdc8` | `10 62 1e 91` | add x16,x16,#0x798 | `FALL_THROUGH`
<a id="insn-00bdfdcc"></a> `00bdfdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdc0`](#insn-00bdfdc0) 範囲 `[['00bdfdc0', '00bdfdcf']]`

## 命令位置別の参照

- [`00bdfdc4`](#insn-00bdfdc4) → `00c1e798`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfdcc`](#insn-00bdfdcc) → [`00b3d3e8`](../00b3d/00b3d3e8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3d3e8` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdc4`](#insn-00bdfdc4)

~~~json
{
  "source": "00bdfdc4",
  "target": "00c1e798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e798",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfdcc`](#insn-00bdfdcc)

~~~json
{
  "source": "00bdfdcc",
  "target": "00b3d3e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
