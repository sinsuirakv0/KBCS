# 00bdfbe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfb90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-c489f9b3e85b8051c1a3537847e43d94)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-8dd8b6cd1ce867a8214bc3a11888e80c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbe0",
  "name": "_ZNK10reflection7Service6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5e31f1bf55ea32f8c56c1b249b6e17e872e8d97a231c040076b19c31c268adee",
  "source_text_sha256": "5e31f1bf55ea32f8c56c1b249b6e17e872e8d97a231c040076b19c31c268adee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbe0",
        "00bdfbef"
      ]
    ],
    "bytes_sha256": "3e0d6b7c78d1b4f21000146e0e02d4c6fad172251fead0c45c8f41a6bd682751",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b35404](../00b35/00b35404.md)

## 呼び出し先

- [00b37754](../00b37/00b37754.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZNK10reflection7Service6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK10reflection7Service6VerifyERN11flatbuffers8VerifierE_00c1e6a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfbe0"></a> `00bdfbe0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfbe4"></a> `00bdfbe4` | `11 56 43 f9` | ldr x17,[x16, #0x6a8] | `FALL_THROUGH`
<a id="insn-00bdfbe8"></a> `00bdfbe8` | `10 a2 1a 91` | add x16,x16,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bdfbec"></a> `00bdfbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbe0`](#insn-00bdfbe0) 範囲 `[['00bdfbe0', '00bdfbef']]`

## 命令位置別の参照

- [`00bdfbe4`](#insn-00bdfbe4) → `00c1e6a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfbec`](#insn-00bdfbec) → [`00b37754`](../00b37/00b37754.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b37754` · 推定シンボル `_ZNK10reflection7Service6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbe4`](#insn-00bdfbe4)

~~~json
{
  "source": "00bdfbe4",
  "target": "00c1e6a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e6a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfbec`](#insn-00bdfbec)

~~~json
{
  "source": "00bdfbec",
  "target": "00b37754",
  "target_space": "ram",
  "resolution": "function"
}
~~~
