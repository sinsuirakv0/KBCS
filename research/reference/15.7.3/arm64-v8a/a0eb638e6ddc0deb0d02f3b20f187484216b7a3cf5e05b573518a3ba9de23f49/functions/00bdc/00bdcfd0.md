# 00bdcfd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcf20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-4446c1fd1b98460560f04a81badf0aa5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdd020`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd020.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-ddad27928b268e376b733083bb812ec6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcfd0",
  "name": "_ZN5Botan11BER_Decoder24decode_optional_implicitINS_15AlternativeNameEEERS0_RT_NS_8ASN1_TagES6_S6_S6_RKS4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7f6cafd0c197d72ec94803b31fb25e5d38785708effe86108fb5fa004103ecc",
  "source_text_sha256": "f7f6cafd0c197d72ec94803b31fb25e5d38785708effe86108fb5fa004103ecc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcfd0",
        "00bdcfdf"
      ]
    ],
    "bytes_sha256": "a02293d4300e552f081428e39a407ce7333458cd07ad6dbfb98fc235147a4071",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004fb978](../004fb/004fb978.md)

## 呼び出し先

- [004fbbe8](../004fb/004fbbe8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 295 bytes

~~~c

void _ZN5Botan11BER_Decoder24decode_optional_implicitINS_15AlternativeNameEEERS0_RT_NS_8ASN1_TagES6_S6_S6_RKS4_
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BER_Decoder24decode_optional_implicitINS_15AlternativeNameEEERS0_RT_NS_8ASN1_TagES6_S6_S6_RKS4__00c1d078
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcfd0"></a> `00bdcfd0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcfd4"></a> `00bdcfd4` | `11 3e 40 f9` | ldr x17,[x16, #0x78] | `FALL_THROUGH`
<a id="insn-00bdcfd8"></a> `00bdcfd8` | `10 e2 01 91` | add x16,x16,#0x78 | `FALL_THROUGH`
<a id="insn-00bdcfdc"></a> `00bdcfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcfd0`](#insn-00bdcfd0) 範囲 `[['00bdcfd0', '00bdcfdf']]`

## 命令位置別の参照

- [`00bdcfd4`](#insn-00bdcfd4) → `00c1d078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcfdc`](#insn-00bdcfdc) → [`004fbbe8`](../004fb/004fbbe8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004fbbe8` · 推定シンボル `_ZN5Botan11BER_Decoder24decode_optional_implicitINS_15AlternativeNameEEERS0_RT_NS_8ASN1_TagES6_S6_S6_RKS4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcfd4`](#insn-00bdcfd4)

~~~json
{
  "source": "00bdcfd4",
  "target": "00c1d078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d078",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcfdc`](#insn-00bdcfdc)

~~~json
{
  "source": "00bdcfdc",
  "target": "004fbbe8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
