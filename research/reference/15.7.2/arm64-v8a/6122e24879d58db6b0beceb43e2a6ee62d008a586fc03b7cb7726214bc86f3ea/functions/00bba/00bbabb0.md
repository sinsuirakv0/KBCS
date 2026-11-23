# 00bbabb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-f18c207627830c5b25a0f4141183f3df)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabb0",
  "name": "__cxa_get_globals",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b31a7bcc757042f9fb01ad9497026d16d36b8dcd2765c9129177ceb12335403c",
  "source_text_sha256": "b31a7bcc757042f9fb01ad9497026d16d36b8dcd2765c9129177ceb12335403c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabb0",
        "00bbabd3"
      ]
    ],
    "bytes_sha256": "a398c205ca4d3629f2430435ac1517375c1fdf022a1b9dc5fd985dd882c8badd",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1cd0](../00be1/00be1cd0.md)

## 呼び出し先

- [00bdd3a0](../00bdd/00bdd3a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3712 bytes

~~~c

void __cxa_get_globals(void)

{
                    /* catch() { ... } // from try @ 00bb4d28 with catch @ 00bbabb4 */
                    /* catch() { ... } // from try @ 00bb4948 with catch @ 00bbabb8 */
                    /* catch() { ... } // from try @ 00bb4588 with catch @ 00bbabbc */
  __emutls_get_address(&DAT_00c248a8);
                    /* catch() { ... } // from try @ 00bb9f14 with catch @ 00bbabcc */
                    /* catch() { ... } // from try @ 00bb35b4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3790 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3b20 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb3f40 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb432c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb470c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb4acc with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb4eac with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb528c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb53ec with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5644 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5a04 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb5dc4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6184 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6538 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb68ec with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb6ca0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7054 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7408 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb77b8 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb785c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb790c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb79b8 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7a68 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7d64 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb7fac with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb86bc with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8994 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8b70 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8c24 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8d90 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb8e34 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb910c with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb93e4 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9640 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb99c0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9af0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bb9fa0 with catch @ 00bbabd0
                       catch() { ... } // from try @ 00bba3fc with catch @ 00bbabd0 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabb0"></a> `00bbabb0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbabb4"></a> `00bbabb4` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbabb8"></a> `00bbabb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbabbc"></a> `00bbabbc` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbabc0"></a> `00bbabc0` | `40 e7 34 10` | adr x0,0xc248a8 | `FALL_THROUGH`
<a id="insn-00bbabc4"></a> `00bbabc4` | `f7 89 00 94` | bl 0x00bdd3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbabc8"></a> `00bbabc8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbabcc"></a> `00bbabcc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbabd0"></a> `00bbabd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabb0`](#insn-00bbabb0) 範囲 `[['00bbabb0', '00bbabb3']]`
  - `FALL_THROUGH` [`00bbabb0`](#insn-00bbabb0) → [`00bbabb4`](#insn-00bbabb4)
- ブロック [`00bbabb4`](#insn-00bbabb4) 範囲 `[['00bbabb4', '00bbabb7']]`
  - `FALL_THROUGH` [`00bbabb4`](#insn-00bbabb4) → [`00bbabb8`](#insn-00bbabb8)
- ブロック [`00bbabb8`](#insn-00bbabb8) 範囲 `[['00bbabb8', '00bbabbb']]`
  - `FALL_THROUGH` [`00bbabb8`](#insn-00bbabb8) → [`00bbabbc`](#insn-00bbabbc)
- ブロック [`00bbabbc`](#insn-00bbabbc) 範囲 `[['00bbabbc', '00bbabcb']]`
  - `FALL_THROUGH` [`00bbabc8`](#insn-00bbabc8) → [`00bbabcc`](#insn-00bbabcc)
- ブロック [`00bbabcc`](#insn-00bbabcc) 範囲 `[['00bbabcc', '00bbabcf']]`
  - `FALL_THROUGH` [`00bbabcc`](#insn-00bbabcc) → [`00bbabd0`](#insn-00bbabd0)
- ブロック [`00bbabd0`](#insn-00bbabd0) 範囲 `[['00bbabd0', '00bbabd3']]`

## 命令位置別の参照

- [`00bbabb4`](#insn-00bbabb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc0`](#insn-00bbabc0) → `00c248a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc4`](#insn-00bbabc4) → [`00bdd3a0`](../00bdd/00bdd3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd3a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbabc8`](#insn-00bbabc8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabb4`](#insn-00bbabb4)

~~~json
{
  "source": "00bbabb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabc0`](#insn-00bbabc0)

~~~json
{
  "source": "00bbabc0",
  "target": "00c248a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabc4`](#insn-00bbabc4)

~~~json
{
  "source": "00bbabc4",
  "target": "00bdd3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbabc8`](#insn-00bbabc8)

~~~json
{
  "source": "00bbabc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
