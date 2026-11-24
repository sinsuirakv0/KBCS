# 00bdeac0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdea70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea70.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-1f850651223054aff5bb20e7e20a2bd8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-7ed7b0d0f8b1d071c4fd8a2699d22fe0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeac0",
  "name": "_ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a9e1a4043cfdf1c906b00165ff41f97e80b331ee0950a319faec156fbd5b567",
  "source_text_sha256": "9a9e1a4043cfdf1c906b00165ff41f97e80b331ee0950a319faec156fbd5b567",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeac0",
        "00bdeacf"
      ]
    ],
    "bytes_sha256": "b3ce79123d009f6a0a75ee2970d2841452a342e978e188be9da384c681204543",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0beec](../00b0b/00b0beec.md)

## 呼び出し先

- [00b0c14c](../00b0c/00b0c14c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 185 bytes

~~~c

void _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE_00c1de18)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeac0"></a> `00bdeac0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeac4"></a> `00bdeac4` | `11 0e 47 f9` | ldr x17,[x16, #0xe18] | `FALL_THROUGH`
<a id="insn-00bdeac8"></a> `00bdeac8` | `10 62 38 91` | add x16,x16,#0xe18 | `FALL_THROUGH`
<a id="insn-00bdeacc"></a> `00bdeacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeac0`](#insn-00bdeac0) 範囲 `[['00bdeac0', '00bdeacf']]`

## 命令位置別の参照

- [`00bdeac4`](#insn-00bdeac4) → `00c1de18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeacc`](#insn-00bdeacc) → [`00b0c14c`](../00b0c/00b0c14c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0c14c` · 推定シンボル `_ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeac4`](#insn-00bdeac4)

~~~json
{
  "source": "00bdeac4",
  "target": "00c1de18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeacc`](#insn-00bdeacc)

~~~json
{
  "source": "00bdeacc",
  "target": "00b0c14c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
