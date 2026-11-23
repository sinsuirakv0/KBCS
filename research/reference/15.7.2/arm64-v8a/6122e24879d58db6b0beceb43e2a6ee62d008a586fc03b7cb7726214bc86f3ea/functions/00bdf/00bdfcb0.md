# 00bdfcb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-f0e660fb3b1f96b31100a35e6740a598)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfcb0",
  "name": "_ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "276c69ca709b51d3a9b693e7aab819f3061f0fe4c9840a2b2dbeff4efb4553f9",
  "source_text_sha256": "276c69ca709b51d3a9b693e7aab819f3061f0fe4c9840a2b2dbeff4efb4553f9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfcb0",
        "00bdfcbf"
      ]
    ],
    "bytes_sha256": "aa5e04446460ee8c82f099f139e138faa086757ad704931fb538e6e16dba6104",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b3256c](../00b32/00b3256c.md)

## 呼び出し先

- [00b32e34](../00b32/00b32e34.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 313 bytes

~~~c

void _ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_
               (void)

{
  (*(code *)
    PTR__ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T__00c1e690
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfcb0"></a> `00bdfcb0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfcb4"></a> `00bdfcb4` | `11 4a 43 f9` | ldr x17,[x16, #0x690] | `FALL_THROUGH`
<a id="insn-00bdfcb8"></a> `00bdfcb8` | `10 42 1a 91` | add x16,x16,#0x690 | `FALL_THROUGH`
<a id="insn-00bdfcbc"></a> `00bdfcbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfcb0`](#insn-00bdfcb0) 範囲 `[['00bdfcb0', '00bdfcbf']]`

## 命令位置別の参照

- [`00bdfcb4`](#insn-00bdfcb4) → `00c1e690`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfcbc`](#insn-00bdfcbc) → [`00b32e34`](../00b32/00b32e34.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b32e34` · 推定シンボル `_ZNSt6__ndk118__insertion_sort_3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEvT0_S9_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfcb4`](#insn-00bdfcb4)

~~~json
{
  "source": "00bdfcb4",
  "target": "00c1e690",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e690",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfcbc`](#insn-00bdfcbc)

~~~json
{
  "source": "00bdfcbc",
  "target": "00b32e34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
