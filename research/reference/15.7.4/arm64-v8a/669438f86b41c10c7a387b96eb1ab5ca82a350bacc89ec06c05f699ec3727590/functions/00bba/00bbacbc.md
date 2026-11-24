# 00bbacbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-032a52407464e967f54561dcc9d26c08)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37704`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37704.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-fef07a9ba35b3d9a9e7e349dab0c37fe)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacbc",
  "name": "__cxa_get_globals",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "998c20d0a12841ce6181cf7234e24858eab4c86da47408bb0a3e0fc8674f0045",
  "source_text_sha256": "998c20d0a12841ce6181cf7234e24858eab4c86da47408bb0a3e0fc8674f0045",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacbc",
        "00bbacdf"
      ]
    ],
    "bytes_sha256": "484d27b001d9eaca13f90d423741c734e85e94865ed2ad4a970712545a4a0f2f",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1dd0](../00be1/00be1dd0.md)

## 呼び出し先

- [00bdd4a0](../00bdd/00bdd4a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3712 bytes

~~~c

void __cxa_get_globals(void)

{
                    /* catch() { ... } // from try @ 00bb4e34 with catch @ 00bbacc0 */
                    /* catch() { ... } // from try @ 00bb4a54 with catch @ 00bbacc4 */
                    /* catch() { ... } // from try @ 00bb4694 with catch @ 00bbacc8 */
  __emutls_get_address(&DAT_00c249a8);
                    /* catch() { ... } // from try @ 00bba020 with catch @ 00bbacd8 */
                    /* catch() { ... } // from try @ 00bb36c0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb389c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb3c2c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb404c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4438 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4818 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4bd8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb4fb8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5398 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb54f8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5750 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5b10 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb5ed0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6290 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6644 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb69f8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb6dac with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7160 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7514 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb78c4 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7968 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7a18 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7ac4 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7b74 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb7e70 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb80b8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb87c8 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8aa0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8c7c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8d30 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8e9c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb8f40 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9218 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb94f0 with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb974c with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9acc with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bb9bfc with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bba0ac with catch @ 00bbacdc
                       catch() { ... } // from try @ 00bba508 with catch @ 00bbacdc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacbc"></a> `00bbacbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbacc0"></a> `00bbacc0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbacc4"></a> `00bbacc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbacc8"></a> `00bbacc8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbaccc"></a> `00bbaccc` | `e0 e6 34 10` | adr x0,0xc249a8 | `FALL_THROUGH`
<a id="insn-00bbacd0"></a> `00bbacd0` | `f4 89 00 94` | bl 0x00bdd4a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacd4"></a> `00bbacd4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbacd8"></a> `00bbacd8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbacdc"></a> `00bbacdc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacbc`](#insn-00bbacbc) 範囲 `[['00bbacbc', '00bbacbf']]`
  - `FALL_THROUGH` [`00bbacbc`](#insn-00bbacbc) → [`00bbacc0`](#insn-00bbacc0)
- ブロック [`00bbacc0`](#insn-00bbacc0) 範囲 `[['00bbacc0', '00bbacc3']]`
  - `FALL_THROUGH` [`00bbacc0`](#insn-00bbacc0) → [`00bbacc4`](#insn-00bbacc4)
- ブロック [`00bbacc4`](#insn-00bbacc4) 範囲 `[['00bbacc4', '00bbacc7']]`
  - `FALL_THROUGH` [`00bbacc4`](#insn-00bbacc4) → [`00bbacc8`](#insn-00bbacc8)
- ブロック [`00bbacc8`](#insn-00bbacc8) 範囲 `[['00bbacc8', '00bbacd7']]`
  - `FALL_THROUGH` [`00bbacd4`](#insn-00bbacd4) → [`00bbacd8`](#insn-00bbacd8)
- ブロック [`00bbacd8`](#insn-00bbacd8) 範囲 `[['00bbacd8', '00bbacdb']]`
  - `FALL_THROUGH` [`00bbacd8`](#insn-00bbacd8) → [`00bbacdc`](#insn-00bbacdc)
- ブロック [`00bbacdc`](#insn-00bbacdc) 範囲 `[['00bbacdc', '00bbacdf']]`

## 命令位置別の参照

- [`00bbacc0`](#insn-00bbacc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaccc`](#insn-00bbaccc) → `00c249a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd0`](#insn-00bbacd0) → [`00bdd4a0`](../00bdd/00bdd4a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd4a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd4`](#insn-00bbacd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacc0`](#insn-00bbacc0)

~~~json
{
  "source": "00bbacc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaccc`](#insn-00bbaccc)

~~~json
{
  "source": "00bbaccc",
  "target": "00c249a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacd0`](#insn-00bbacd0)

~~~json
{
  "source": "00bbacd0",
  "target": "00bdd4a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacd4`](#insn-00bbacd4)

~~~json
{
  "source": "00bbacd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
