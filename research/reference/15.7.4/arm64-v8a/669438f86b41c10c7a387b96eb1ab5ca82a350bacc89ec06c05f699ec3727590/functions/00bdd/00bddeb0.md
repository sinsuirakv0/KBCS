# 00bddeb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdde60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-f4a467087af933ebac4b1eab27dfcfa1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a910`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-9795f8642704e3ea02b4d945a32477ad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddeb0",
  "name": "_ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dd0f22109c37d7db0bc9b4a297799f981fcc48d9df6a3941f70556b602bec28d",
  "source_text_sha256": "dd0f22109c37d7db0bc9b4a297799f981fcc48d9df6a3941f70556b602bec28d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddeb0",
        "00bddebf"
      ]
    ],
    "bytes_sha256": "2bd5ff8891bc94512e766e93acd2f5766bdcc74d46b6f9a1da2bd01d8fb67f69",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae02f0](../00ae0/00ae02f0.md)
- [00b49f30](../00b49/00b49f30.md)
- [00b4ecb4](../00b4e/00b4ecb4.md)
- [00b4fff0](../00b4f/00b4fff0.md)
- [00b52318](../00b52/00b52318.md)
- [00b55670](../00b55/00b55670.md)
- [00b563d0](../00b56/00b563d0.md)
- [00b5bd94](../00b5b/00b5bd94.md)
- [00b5bfbc](../00b5b/00b5bfbc.md)
- [00b5c4fc](../00b5c/00b5c4fc.md)
- [00b5c5f4](../00b5c/00b5c5f4.md)
- [00b5c6ec](../00b5c/00b5c6ec.md)
- [00b71e00](../00b71/00b71e00.md)

## 呼び出し先

- [00ae04ac](../00ae0/00ae04ac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 189 bytes

~~~c

void _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(void)

{
  (*(code *)PTR__ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv_00c1d810)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddeb0"></a> `00bddeb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddeb4"></a> `00bddeb4` | `11 0a 44 f9` | ldr x17,[x16, #0x810] | `FALL_THROUGH`
<a id="insn-00bddeb8"></a> `00bddeb8` | `10 42 20 91` | add x16,x16,#0x810 | `FALL_THROUGH`
<a id="insn-00bddebc"></a> `00bddebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddeb0`](#insn-00bddeb0) 範囲 `[['00bddeb0', '00bddebf']]`

## 命令位置別の参照

- [`00bddeb4`](#insn-00bddeb4) → `00c1d810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddebc`](#insn-00bddebc) → [`00ae04ac`](../00ae0/00ae04ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae04ac` · 推定シンボル `_ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddeb4`](#insn-00bddeb4)

~~~json
{
  "source": "00bddeb4",
  "target": "00c1d810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddebc`](#insn-00bddebc)

~~~json
{
  "source": "00bddebc",
  "target": "00ae04ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
