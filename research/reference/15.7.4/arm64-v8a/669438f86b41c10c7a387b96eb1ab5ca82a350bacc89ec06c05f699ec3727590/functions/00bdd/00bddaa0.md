# 00bddaa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdda50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0017.md#compare-b4b4274bd564f35174d7e8db4653621d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a4f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-97f39f98392da08439e3343b45e9a51a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddaa0",
  "name": "_ZN8firebase7VariantaSERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c02045edef5a1e24212788eb0dcd07f8f16d15b9a6e4c89ac671c50d1b279fe4",
  "source_text_sha256": "c02045edef5a1e24212788eb0dcd07f8f16d15b9a6e4c89ac671c50d1b279fe4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddaa0",
        "00bddaaf"
      ]
    ],
    "bytes_sha256": "a1f2c47e4f07ce2338fe2b1facf94d25c5853af936e56d5d330da655330ff48d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00759544](../00759/00759544.md)
- [0076c5e4](../0076c/0076c5e4.md)
- [008460c4](../00846/008460c4.md)
- [0084642c](../00846/0084642c.md)
- [008468c0](../00846/008468c0.md)
- [00846bdc](../00846/00846bdc.md)
- [0085c360](../0085c/0085c360.md)
- [00a45360](../00a45/00a45360.md)
- [00a48a98](../00a48/00a48a98.md)
- [00a496c0](../00a49/00a496c0.md)
- [00a4a284](../00a4a/00a4a284.md)
- [00a4ad68](../00a4a/00a4ad68.md)
- [00a4ec84](../00a4e/00a4ec84.md)
- [00af2504](../00af2/00af2504.md)
- [00b046d0](../00b04/00b046d0.md)
- [00b0490c](../00b04/00b0490c.md)
- [00b04a00](../00b04/00b04a00.md)
- [00b04dc0](../00b04/00b04dc0.md)
- [00b04fa8](../00b04/00b04fa8.md)
- [00b052f8](../00b05/00b052f8.md)
- [00b590b0](../00b59/00b590b0.md)
- [00b6cf14](../00b6c/00b6cf14.md)

## 呼び出し先

- [00b02ec0](../00b02/00b02ec0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZN8firebase7VariantaSERKS0_(void)

{
  (*(code *)PTR__ZN8firebase7VariantaSERKS0__00c1d608)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddaa0"></a> `00bddaa0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddaa4"></a> `00bddaa4` | `11 06 43 f9` | ldr x17,[x16, #0x608] | `FALL_THROUGH`
<a id="insn-00bddaa8"></a> `00bddaa8` | `10 22 18 91` | add x16,x16,#0x608 | `FALL_THROUGH`
<a id="insn-00bddaac"></a> `00bddaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddaa0`](#insn-00bddaa0) 範囲 `[['00bddaa0', '00bddaaf']]`

## 命令位置別の参照

- [`00bddaa4`](#insn-00bddaa4) → `00c1d608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddaac`](#insn-00bddaac) → [`00b02ec0`](../00b02/00b02ec0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b02ec0` · 推定シンボル `_ZN8firebase7VariantaSERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddaa4`](#insn-00bddaa4)

~~~json
{
  "source": "00bddaa4",
  "target": "00c1d608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d608",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddaac`](#insn-00bddaac)

~~~json
{
  "source": "00bddaac",
  "target": "00b02ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
