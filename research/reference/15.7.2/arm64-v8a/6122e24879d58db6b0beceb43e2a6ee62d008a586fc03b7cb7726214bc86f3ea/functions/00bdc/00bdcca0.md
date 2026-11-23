# 00bdcca0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-fbcabeecafd2378a469fb4d979b93310)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcca0",
  "name": "_ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94a1a2f3238e4be87e14028098cb1a8cb2c6c7c189c811eb1d56e6c55e8bc5f6",
  "source_text_sha256": "94a1a2f3238e4be87e14028098cb1a8cb2c6c7c189c811eb1d56e6c55e8bc5f6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcca0",
        "00bdccaf"
      ]
    ],
    "bytes_sha256": "772531a47c489f1135d32f4b89fae91e635075f479faf95bfe3ea6ad91261912",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e6d3c](../004e6/004e6d3c.md)
- [004e9fdc](../004e9/004e9fdc.md)

## 呼び出し先

- [004e82ac](../004e8/004e82ac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 336 bytes

~~~c

void _ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_(void)

{
                    /* try { // try from 00bdcca0 to 00cdccbf has its CatchHandler @ 00bdd1a4 */
  (*(code *)
    PTR__ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4__00c1ce88
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcca0"></a> `00bdcca0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcca4"></a> `00bdcca4` | `11 46 47 f9` | ldr x17,[x16, #0xe88] | `FALL_THROUGH`
<a id="insn-00bdcca8"></a> `00bdcca8` | `10 22 3a 91` | add x16,x16,#0xe88 | `FALL_THROUGH`
<a id="insn-00bdccac"></a> `00bdccac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcca0`](#insn-00bdcca0) 範囲 `[['00bdcca0', '00bdccaf']]`

## 命令位置別の参照

- [`00bdcca4`](#insn-00bdcca4) → `00c1ce88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccac`](#insn-00bdccac) → [`004e82ac`](../004e8/004e82ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e82ac` · 推定シンボル `_ZN5Botan11BER_Decoder15decode_optionalINS_10ExtensionsEEERS0_RT_NS_8ASN1_TagES6_RKS4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcca4`](#insn-00bdcca4)

~~~json
{
  "source": "00bdcca4",
  "target": "00c1ce88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdccac`](#insn-00bdccac)

~~~json
{
  "source": "00bdccac",
  "target": "004e82ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
