# 00bdeab0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdea60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-7b8a1ff674166294c80550ecd91a131a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0094.md#review-e982fa222faad5ea386b99ead9e993fc)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeab0",
  "name": "_ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0232219020cd7047b94983f72721678bf0288d52afbf7aad07194557fe99c091",
  "source_text_sha256": "0232219020cd7047b94983f72721678bf0288d52afbf7aad07194557fe99c091",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeab0",
        "00bdeabf"
      ]
    ],
    "bytes_sha256": "b36cdfa311a5395553d16b0ab59e566aab061df70ae47a31047a7b8bba192652",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0b670](../00b0b/00b0b670.md)

## 呼び出し先

- [00b0bb00](../00b0b/00b0bb00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

void _ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE_00c1de10)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeab0"></a> `00bdeab0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeab4"></a> `00bdeab4` | `11 0a 47 f9` | ldr x17,[x16, #0xe10] | `FALL_THROUGH`
<a id="insn-00bdeab8"></a> `00bdeab8` | `10 42 38 91` | add x16,x16,#0xe10 | `FALL_THROUGH`
<a id="insn-00bdeabc"></a> `00bdeabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeab0`](#insn-00bdeab0) 範囲 `[['00bdeab0', '00bdeabf']]`

## 命令位置別の参照

- [`00bdeab4`](#insn-00bdeab4) → `00c1de10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeabc`](#insn-00bdeabc) → [`00b0bb00`](../00b0b/00b0bb00.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0bb00` · 推定シンボル `_ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeab4`](#insn-00bdeab4)

~~~json
{
  "source": "00bdeab4",
  "target": "00c1de10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeabc`](#insn-00bdeabc)

~~~json
{
  "source": "00bdeabc",
  "target": "00b0bb00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
