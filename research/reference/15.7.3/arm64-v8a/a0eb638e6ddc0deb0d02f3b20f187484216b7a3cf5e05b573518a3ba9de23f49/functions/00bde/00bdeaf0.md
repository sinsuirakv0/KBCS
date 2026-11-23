# 00bdeaf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdea40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-54ed0854f3f330384c48746f06e9ecd4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdeb40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-410e6087a658ee15e912c708ad59b250)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeaf0",
  "name": "_ZNK8firebase3fbs6Client6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c34f31fbf798226784475f8aa393c2c81e47be41038476daf8708aa7adf7281",
  "source_text_sha256": "3c34f31fbf798226784475f8aa393c2c81e47be41038476daf8708aa7adf7281",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeaf0",
        "00bdeaff"
      ]
    ],
    "bytes_sha256": "222e7caf43ce68f2e024571c0c7debe456ffdfd01f7e9236e9c4f2dc041336f8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0ae28](../00b0a/00b0ae28.md)

## 呼び出し先

- [00b0b62c](../00b0b/00b0b62c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 173 bytes

~~~c

void _ZNK8firebase3fbs6Client6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK8firebase3fbs6Client6VerifyERN11flatbuffers8VerifierE_00c1de08)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeaf0"></a> `00bdeaf0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeaf4"></a> `00bdeaf4` | `11 06 47 f9` | ldr x17,[x16, #0xe08] | `FALL_THROUGH`
<a id="insn-00bdeaf8"></a> `00bdeaf8` | `10 22 38 91` | add x16,x16,#0xe08 | `FALL_THROUGH`
<a id="insn-00bdeafc"></a> `00bdeafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeaf0`](#insn-00bdeaf0) 範囲 `[['00bdeaf0', '00bdeaff']]`

## 命令位置別の参照

- [`00bdeaf4`](#insn-00bdeaf4) → `00c1de08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeafc`](#insn-00bdeafc) → [`00b0b62c`](../00b0b/00b0b62c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0b62c` · 推定シンボル `_ZNK8firebase3fbs6Client6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeaf4`](#insn-00bdeaf4)

~~~json
{
  "source": "00bdeaf4",
  "target": "00c1de08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdeafc`](#insn-00bdeafc)

~~~json
{
  "source": "00bdeafc",
  "target": "00b0b62c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
