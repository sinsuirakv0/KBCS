# 00bdeac0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdea10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0018.md#compare-197eabc796e9f6c37016fe0be067c728)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdeb10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-46cc3f56cc47aa74567cba5016040a76)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeac0",
  "name": "_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers8VerifierE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfdf024309d87509754033bf4b0bbbf97ea94fec286847e51799ddfa4adc5a70",
  "source_text_sha256": "bfdf024309d87509754033bf4b0bbbf97ea94fec286847e51799ddfa4adc5a70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeac0",
        "00bdeacf"
      ]
    ],
    "bytes_sha256": "4bc0b79debe0ff94eaaaea7f465728a80c24947b81f08b54db03becda311650b",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b0c894](../00b0c/00b0c894.md)

## 呼び出し先

- [00b0ca14](../00b0c/00b0ca14.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 197 bytes

~~~c

void _ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers8VerifierE(void)

{
  (*(code *)PTR__ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers8VerifierE_00c1ddf0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeac0"></a> `00bdeac0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeac4"></a> `00bdeac4` | `11 fa 46 f9` | ldr x17,[x16, #0xdf0] | `FALL_THROUGH`
<a id="insn-00bdeac8"></a> `00bdeac8` | `10 c2 37 91` | add x16,x16,#0xdf0 | `FALL_THROUGH`
<a id="insn-00bdeacc"></a> `00bdeacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeac0`](#insn-00bdeac0) 範囲 `[['00bdeac0', '00bdeacf']]`

## 命令位置別の参照

- [`00bdeac4`](#insn-00bdeac4) → `00c1ddf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdeacc`](#insn-00bdeacc) → [`00b0ca14`](../00b0c/00b0ca14.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b0ca14` · 推定シンボル `_ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers8VerifierE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeac4`](#insn-00bdeac4)

~~~json
{
  "source": "00bdeac4",
  "target": "00c1ddf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ddf0",
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
  "target": "00b0ca14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
