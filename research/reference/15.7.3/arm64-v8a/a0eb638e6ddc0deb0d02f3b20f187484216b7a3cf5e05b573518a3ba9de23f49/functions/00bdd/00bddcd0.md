# 00bddcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-a53d5f8825a80d9e1f98e5b6ba19976d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddd20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-4000b6c1690d4905acd9feb6015fe751)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcd0",
  "name": "_ZN8firebase4auth22FederatedOAuthProviderC1ERKNS0_26FederatedOAuthProviderDataE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a1d6425418cbc81700b743c3b419567856b47c19bfbb182ebc95bcb79360f24",
  "source_text_sha256": "5a1d6425418cbc81700b743c3b419567856b47c19bfbb182ebc95bcb79360f24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcd0",
        "00bddcdf"
      ]
    ],
    "bytes_sha256": "f4a90578632c4a4a4d228bfe4fe719c3b96cc6934d90a7b0dddf37b6f8510c7f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad44ec](../00ad4/00ad44ec.md)

## 呼び出し先

- [00b6bc48](../00b6b/00b6bc48.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 222 bytes

~~~c

void _ZN8firebase4auth22FederatedOAuthProviderC1ERKNS0_26FederatedOAuthProviderDataE(void)

{
  (*(code *)
    PTR__ZN8firebase4auth22FederatedOAuthProviderC1ERKNS0_26FederatedOAuthProviderDataE_00c1d6f8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcd0"></a> `00bddcd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcd4"></a> `00bddcd4` | `11 7e 43 f9` | ldr x17,[x16, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bddcd8"></a> `00bddcd8` | `10 e2 1b 91` | add x16,x16,#0x6f8 | `FALL_THROUGH`
<a id="insn-00bddcdc"></a> `00bddcdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcd0`](#insn-00bddcd0) 範囲 `[['00bddcd0', '00bddcdf']]`

## 命令位置別の参照

- [`00bddcd4`](#insn-00bddcd4) → `00c1d6f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcdc`](#insn-00bddcdc) → [`00b6bc48`](../00b6b/00b6bc48.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6bc48` · 推定シンボル `_ZN8firebase4auth22FederatedOAuthProviderC1ERKNS0_26FederatedOAuthProviderDataE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcd4`](#insn-00bddcd4)

~~~json
{
  "source": "00bddcd4",
  "target": "00c1d6f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6f8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcdc`](#insn-00bddcdc)

~~~json
{
  "source": "00bddcdc",
  "target": "00b6bc48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
