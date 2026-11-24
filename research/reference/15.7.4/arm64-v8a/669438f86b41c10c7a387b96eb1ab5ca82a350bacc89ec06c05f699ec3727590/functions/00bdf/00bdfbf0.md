# 00bdfbf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfba0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0022.md#compare-b6800159ae289363c739af3e795eb39d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-cd9d837f918bdd6c5913a6021cbc9b77)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfbf0",
  "name": "_ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "692bb0a171237239a64fc90e0da7f590c4d7d3f4ffba59fa99b042e6845f536c",
  "source_text_sha256": "692bb0a171237239a64fc90e0da7f590c4d7d3f4ffba59fa99b042e6845f536c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfbf0",
        "00bdfbff"
      ]
    ],
    "bytes_sha256": "33f837475e34ee5327a66d8d5b37963a7261632c8732ffdc8865b5b9834bad21",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b35b04](../00b35/00b35b04.md)
- [00b36174](../00b36/00b36174.md)
- [00b36c24](../00b36/00b36c24.md)
- [00b37754](../00b37/00b37754.md)
- [00b37d1c](../00b37/00b37d1c.md)

## 呼び出し先

- [00b369b0](../00b36/00b369b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 175 bytes

~~~c

void _ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE_00c1e6b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfbf0"></a> `00bdfbf0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfbf4"></a> `00bdfbf4` | `11 5a 43 f9` | ldr x17,[x16, #0x6b0] | `FALL_THROUGH`
<a id="insn-00bdfbf8"></a> `00bdfbf8` | `10 c2 1a 91` | add x16,x16,#0x6b0 | `FALL_THROUGH`
<a id="insn-00bdfbfc"></a> `00bdfbfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfbf0`](#insn-00bdfbf0) 範囲 `[['00bdfbf0', '00bdfbff']]`

## 命令位置別の参照

- [`00bdfbf4`](#insn-00bdfbf4) → `00c1e6b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfbfc`](#insn-00bdfbfc) → [`00b369b0`](../00b36/00b369b0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b369b0` · 推定シンボル `_ZNK10reflection8KeyValue6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfbf4`](#insn-00bdfbf4)

~~~json
{
  "source": "00bdfbf4",
  "target": "00c1e6b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e6b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfbfc`](#insn-00bdfbfc)

~~~json
{
  "source": "00bdfbfc",
  "target": "00b369b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
