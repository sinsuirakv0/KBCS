# 00bdfbb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-971c0e82089e415b498e34389debb8b0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-f41a9a157717a8b985f02ec68a6afd81)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbb0",
  "name": "_ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4c6f25ca58b5603a6f1e3afb5d98a93dd7fd83075f7446c2dec329b7c5a3a5c",
  "source_text_sha256": "b4c6f25ca58b5603a6f1e3afb5d98a93dd7fd83075f7446c2dec329b7c5a3a5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbb0",
        "00bdfbbf"
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

- [00b2c8fc](../00b2c/00b2c8fc.md)
- [00b2c9a0](../00b2c/00b2c9a0.md)

## 呼び出し先

- [00b35404](../00b35/00b35404.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 171 bytes

~~~c

void _ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE_00c1e690)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfbb0"></a> `00bdfbb0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfbb4"></a> `00bdfbb4` | `11 4a 43 f9` | ldr x17,[x16, #0x690] | `FALL_THROUGH`
<a id="insn-00bdfbb8"></a> `00bdfbb8` | `10 42 1a 91` | add x16,x16,#0x690 | `FALL_THROUGH`
<a id="insn-00bdfbbc"></a> `00bdfbbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbb0`](#insn-00bdfbb0) 範囲 `[['00bdfbb0', '00bdfbbf']]`

## 命令位置別の参照

- [`00bdfbb4`](#insn-00bdfbb4) → `00c1e690`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfbbc`](#insn-00bdfbbc) → [`00b35404`](../00b35/00b35404.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b35404` · 推定シンボル `_ZNK10reflection6Schema6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbb4`](#insn-00bdfbb4)

~~~json
{
  "source": "00bdfbb4",
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
- 参照命令 [`00bdfbbc`](#insn-00bdfbbc)

~~~json
{
  "source": "00bdfbbc",
  "target": "00b35404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
