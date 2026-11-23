# 007fafec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `007fafec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fafec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0013.md#compare-fc02860733667830c9256063c5891077)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fafec",
  "name": "FUN_007fafec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494",
  "source_text_sha256": "c1bd3a7b0aff5d7a4f97e42440eef4951f64b116686ab12ffb1e3c68e1a3c494",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fafec",
        "007faff3"
      ]
    ],
    "bytes_sha256": "74d3eb8a1998bb63dd08fa5ffabbf0ae9cf6de63bc6bf45df32441710325121b",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)

## 呼び出し先

- [007faff8](../007fa/007faff8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007fafec(long param_1)

{
                    /* catch() { ... } // from try @ 007fa778 with catch @ 007faff0 */
  FUN_007faff8(param_1 + 0x18);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fafec"></a> `007fafec` | `00 60 00 91` | add x0,x0,#0x18 | `FALL_THROUGH`
<a id="insn-007faff0"></a> `007faff0` | `02 00 00 14` | b 0x007faff8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fafec`](#insn-007fafec) 範囲 `[['007fafec', '007fafef']]`
  - `FALL_THROUGH` [`007fafec`](#insn-007fafec) → [`007faff0`](#insn-007faff0)
- ブロック [`007faff0`](#insn-007faff0) 範囲 `[['007faff0', '007faff3']]`

## 命令位置別の参照

- [`007faff0`](#insn-007faff0) → [`007faff8`](007faff8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007faff8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007faff0`](#insn-007faff0)

~~~json
{
  "source": "007faff0",
  "target": "007faff8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
