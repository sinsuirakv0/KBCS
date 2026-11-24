# 00bdfdf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfda0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfda0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-f1a7ea1dae485dcab861a6857dfed27f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-61bdd0dec89bbdb6160162c38e16a78f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdf0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1b579aef6376839f167817ded7f15d60e1a517b5fe566d9f4563cae3d8e2c57",
  "source_text_sha256": "c1b579aef6376839f167817ded7f15d60e1a517b5fe566d9f4563cae3d8e2c57",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdf0",
        "00bdfdff"
      ]
    ],
    "bytes_sha256": "6c1aaa57091937e5177547bac8cc8911e357bc9cca7ffb036316d2d3a81116b1",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b3d788](../00b3d/00b3d788.md)

## 呼び出し先

- [00b3e710](../00b3e/00b3e710.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 383 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEbT0_SB_T__00c1e7b0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdf0"></a> `00bdfdf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdf4"></a> `00bdfdf4` | `11 da 43 f9` | ldr x17,[x16, #0x7b0] | `FALL_THROUGH`
<a id="insn-00bdfdf8"></a> `00bdfdf8` | `10 c2 1e 91` | add x16,x16,#0x7b0 | `FALL_THROUGH`
<a id="insn-00bdfdfc"></a> `00bdfdfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdf0`](#insn-00bdfdf0) 範囲 `[['00bdfdf0', '00bdfdff']]`

## 命令位置別の参照

- [`00bdfdf4`](#insn-00bdfdf4) → `00c1e7b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfdfc`](#insn-00bdfdfc) → [`00b3e710`](../00b3e/00b3e710.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3e710` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEbT0_SB_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdf4`](#insn-00bdfdf4)

~~~json
{
  "source": "00bdfdf4",
  "target": "00c1e7b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e7b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfdfc`](#insn-00bdfdfc)

~~~json
{
  "source": "00bdfdfc",
  "target": "00b3e710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
