# 00bdedd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bded80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded80.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-fc61e3e4e074955b45a643ca45e14033)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5b890`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b890.md) · 移動量 `+0x7cac0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-020d44cea7bb911c8e2ceea0955ded47)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedd0",
  "name": "_ZN8firebase17FutureBackingDataD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df82a7753c03e71fce7a899e70c5df3786959c2c860d0fea3655be6ce55d45d7",
  "source_text_sha256": "df82a7753c03e71fce7a899e70c5df3786959c2c860d0fea3655be6ce55d45d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedd0",
        "00bdeddf"
      ]
    ],
    "bytes_sha256": "870d4a8c3792cbecf7301ab6dbb659ef8140b8e1e0a55fd689e9d59f33ff621b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afeb24](../00afe/00afeb24.md)
- [00aff94c](../00aff/00aff94c.md)

## 呼び出し先

- [00afe7a4](../00afe/00afe7a4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 129 bytes

~~~c

void _ZN8firebase17FutureBackingDataD1Ev(void)

{
  (*(code *)PTR__ZN8firebase17FutureBackingDataD1Ev_00c1dfa0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedd0"></a> `00bdedd0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedd4"></a> `00bdedd4` | `11 d2 47 f9` | ldr x17,[x16, #0xfa0] | `FALL_THROUGH`
<a id="insn-00bdedd8"></a> `00bdedd8` | `10 82 3e 91` | add x16,x16,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bdeddc"></a> `00bdeddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedd0`](#insn-00bdedd0) 範囲 `[['00bdedd0', '00bdeddf']]`

## 命令位置別の参照

- [`00bdedd4`](#insn-00bdedd4) → `00c1dfa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeddc`](#insn-00bdeddc) → [`00afe7a4`](../00afe/00afe7a4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afe7a4` · 推定シンボル `_ZN8firebase17FutureBackingDataD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedd4`](#insn-00bdedd4)

~~~json
{
  "source": "00bdedd4",
  "target": "00c1dfa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1dfa0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeddc`](#insn-00bdeddc)

~~~json
{
  "source": "00bdeddc",
  "target": "00afe7a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
