# 00bddbb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-22ee7fb7ab7de091bd80df9a7fa42808)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a620`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a620.md) · 移動量 `+0x7ca70`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-85a06401b3bf3e1aa07b3aa39079990d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddbb0",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fb17be8149817543864fff29d87e836764c433c586ff5cccfc11c8c6d8872ca",
  "source_text_sha256": "1fb17be8149817543864fff29d87e836764c433c586ff5cccfc11c8c6d8872ca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddbb0",
        "00bddbbf"
      ]
    ],
    "bytes_sha256": "61c9143b4a323f285aba449853d8571d6cd45d338ee97a08d7e78398e24886bc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008480dc](../00848/008480dc.md)

## 呼び出し先

- [00b5faf0](../00b5f/00b5faf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(void)

{
  (*(code *)PTR__ZN8firebase4auth4Auth7SignOutEv_00c1d690)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddbb0"></a> `00bddbb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddbb4"></a> `00bddbb4` | `11 4a 43 f9` | ldr x17,[x16, #0x690] | `FALL_THROUGH`
<a id="insn-00bddbb8"></a> `00bddbb8` | `10 42 1a 91` | add x16,x16,#0x690 | `FALL_THROUGH`
<a id="insn-00bddbbc"></a> `00bddbbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddbb0`](#insn-00bddbb0) 範囲 `[['00bddbb0', '00bddbbf']]`

## 命令位置別の参照

- [`00bddbb4`](#insn-00bddbb4) → `00c1d690`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbbc`](#insn-00bddbbc) → [`00b5faf0`](../00b5f/00b5faf0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b5faf0` · 推定シンボル `_ZN8firebase4auth4Auth7SignOutEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddbb4`](#insn-00bddbb4)

~~~json
{
  "source": "00bddbb4",
  "target": "00c1d690",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d690",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbbc`](#insn-00bddbbc)

~~~json
{
  "source": "00bddbbc",
  "target": "00b5faf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
