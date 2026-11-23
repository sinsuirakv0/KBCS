# 00bdfaf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdfa40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-aaadc4777319e25f310af3ffd48f6829)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdfb40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-3a4d5c097c505156460602de37d8053f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfaf0",
  "name": "_ZN11flexbuffers7Builder6StringEPKcm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a10a8a7b9856f92924f511400fd71e7be850f062b1aac73bae10fb68519ae54",
  "source_text_sha256": "5a10a8a7b9856f92924f511400fd71e7be850f062b1aac73bae10fb68519ae54",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfaf0",
        "00bdfaff"
      ]
    ],
    "bytes_sha256": "0430cb5cc2041461bae3527024ecf90a38e607408516f495ccc2dcdb94e3d055",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b256a0](../00b25/00b256a0.md)

## 呼び出し先

- [00b33ac4](../00b33/00b33ac4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZN11flexbuffers7Builder6StringEPKcm(void)

{
  (*(code *)PTR__ZN11flexbuffers7Builder6StringEPKcm_00c1e608)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfaf0"></a> `00bdfaf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfaf4"></a> `00bdfaf4` | `11 06 43 f9` | ldr x17,[x16, #0x608] | `FALL_THROUGH`
<a id="insn-00bdfaf8"></a> `00bdfaf8` | `10 22 18 91` | add x16,x16,#0x608 | `FALL_THROUGH`
<a id="insn-00bdfafc"></a> `00bdfafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfaf0`](#insn-00bdfaf0) 範囲 `[['00bdfaf0', '00bdfaff']]`

## 命令位置別の参照

- [`00bdfaf4`](#insn-00bdfaf4) → `00c1e608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfafc`](#insn-00bdfafc) → [`00b33ac4`](../00b33/00b33ac4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b33ac4` · 推定シンボル `_ZN11flexbuffers7Builder6StringEPKcm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfaf4`](#insn-00bdfaf4)

~~~json
{
  "source": "00bdfaf4",
  "target": "00c1e608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e608",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfafc`](#insn-00bdfafc)

~~~json
{
  "source": "00bdfafc",
  "target": "00b33ac4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
