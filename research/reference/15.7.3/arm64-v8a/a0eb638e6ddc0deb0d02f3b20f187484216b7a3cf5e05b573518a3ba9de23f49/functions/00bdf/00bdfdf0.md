# 00bdfdf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-626dfd975f80af16976fbc58e9093082)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfe40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-dbbde60cce5e3f93966e5ae48c8ce255)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdf0",
  "name": "_ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41eb036c171868abec7ffa930c270b2f19a1fa2caca81d93e7d33ba69203e5c3",
  "source_text_sha256": "41eb036c171868abec7ffa930c270b2f19a1fa2caca81d93e7d33ba69203e5c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdf0",
        "00bdfdff"
      ]
    ],
    "bytes_sha256": "1fb52432829a33ccddf0d5d5b2f239fc1a4954407e06fc7471b9f1b7e9f747b1",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b32634](../00b32/00b32634.md)

## 呼び出し先

- [00b3303c](../00b33/00b3303c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 428 bytes

~~~c

void _ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_
               (void)

{
                    /* try { // try from 00bdfdf0 to 00cdfe77 has its CatchHandler @ 00bdff5c */
  (*(code *)
    PTR__ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T__00c1e788
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdf0"></a> `00bdfdf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdf4"></a> `00bdfdf4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bdfdf8"></a> `00bdfdf8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdfdfc"></a> `00bdfdfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdf0`](#insn-00bdfdf0) 範囲 `[['00bdfdf0', '00bdfdff']]`

## 命令位置別の参照

- [`00bdfdf4`](#insn-00bdfdf4) → `00c1e788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfdfc`](#insn-00bdfdfc) → [`00b3303c`](../00b33/00b3303c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3303c` · 推定シンボル `_ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdf4`](#insn-00bdfdf4)

~~~json
{
  "source": "00bdfdf4",
  "target": "00c1e788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e788",
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
  "target": "00b3303c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
