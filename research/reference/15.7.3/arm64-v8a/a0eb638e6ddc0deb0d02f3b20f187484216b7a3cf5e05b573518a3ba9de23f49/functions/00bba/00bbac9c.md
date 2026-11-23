# 00bbac9c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbabd4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbabd4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3366d56ecb19a51b1da99de8b3b0c84f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbace0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbace0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-8f7e8fe1d2bfa265a2430422e780df2c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbac9c",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "680138874b5c4801104343cc0650f30ac6e261b798b76086a50d518f724c56c7",
  "source_text_sha256": "680138874b5c4801104343cc0650f30ac6e261b798b76086a50d518f724c56c7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbac9c",
        "00bbacbf"
      ]
    ],
    "bytes_sha256": "3765944ad755b44dd4e933c7713aa1949a3de98036627ffbca3603d8b29c125d",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1d90](../00be1/00be1d90.md)

## 呼び出し先

- [00bdd450](../00bdd/00bdd450.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb744c with catch @ 00bbaca0 */
                    /* catch() { ... } // from try @ 00bb7098 with catch @ 00bbaca4 */
                    /* catch() { ... } // from try @ 00bb6ce4 with catch @ 00bbaca8 */
                    /* catch() { ... } // from try @ 00bb6930 with catch @ 00bbacac */
                    /* catch() { ... } // from try @ 00bb657c with catch @ 00bbacb0 */
  __emutls_get_address(&DAT_00c24958);
                    /* catch() { ... } // from try @ 00bb61c8 with catch @ 00bbacb4 */
                    /* catch() { ... } // from try @ 00bb5e08 with catch @ 00bbacb8 */
                    /* catch() { ... } // from try @ 00bb5a48 with catch @ 00bbacbc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbac9c"></a> `00bbac9c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbaca0"></a> `00bbaca0` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbaca4"></a> `00bbaca4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbaca8"></a> `00bbaca8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbacac"></a> `00bbacac` | `60 e5 34 10` | adr x0,0xc24958 | `FALL_THROUGH`
<a id="insn-00bbacb0"></a> `00bbacb0` | `e8 89 00 94` | bl 0x00bdd450 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacb4"></a> `00bbacb4` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbacb8"></a> `00bbacb8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbacbc"></a> `00bbacbc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbac9c`](#insn-00bbac9c) 範囲 `[['00bbac9c', '00bbac9f']]`
  - `FALL_THROUGH` [`00bbac9c`](#insn-00bbac9c) → [`00bbaca0`](#insn-00bbaca0)
- ブロック [`00bbaca0`](#insn-00bbaca0) 範囲 `[['00bbaca0', '00bbaca3']]`
  - `FALL_THROUGH` [`00bbaca0`](#insn-00bbaca0) → [`00bbaca4`](#insn-00bbaca4)
- ブロック [`00bbaca4`](#insn-00bbaca4) 範囲 `[['00bbaca4', '00bbaca7']]`
  - `FALL_THROUGH` [`00bbaca4`](#insn-00bbaca4) → [`00bbaca8`](#insn-00bbaca8)
- ブロック [`00bbaca8`](#insn-00bbaca8) 範囲 `[['00bbaca8', '00bbacab']]`
  - `FALL_THROUGH` [`00bbaca8`](#insn-00bbaca8) → [`00bbacac`](#insn-00bbacac)
- ブロック [`00bbacac`](#insn-00bbacac) 範囲 `[['00bbacac', '00bbacaf']]`
  - `FALL_THROUGH` [`00bbacac`](#insn-00bbacac) → [`00bbacb0`](#insn-00bbacb0)
- ブロック [`00bbacb0`](#insn-00bbacb0) 範囲 `[['00bbacb0', '00bbacb3']]`
  - `FALL_THROUGH` [`00bbacb0`](#insn-00bbacb0) → [`00bbacb4`](#insn-00bbacb4)
- ブロック [`00bbacb4`](#insn-00bbacb4) 範囲 `[['00bbacb4', '00bbacb7']]`
  - `FALL_THROUGH` [`00bbacb4`](#insn-00bbacb4) → [`00bbacb8`](#insn-00bbacb8)
- ブロック [`00bbacb8`](#insn-00bbacb8) 範囲 `[['00bbacb8', '00bbacbb']]`
  - `FALL_THROUGH` [`00bbacb8`](#insn-00bbacb8) → [`00bbacbc`](#insn-00bbacbc)
- ブロック [`00bbacbc`](#insn-00bbacbc) 範囲 `[['00bbacbc', '00bbacbf']]`

## 命令位置別の参照

- [`00bbaca0`](#insn-00bbaca0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacac`](#insn-00bbacac) → `00c24958`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb0`](#insn-00bbacb0) → [`00bdd450`](../00bdd/00bdd450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd450` · 推定シンボル `None` · 推定型 `None`
- [`00bbacb4`](#insn-00bbacb4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbaca0`](#insn-00bbaca0)

~~~json
{
  "source": "00bbaca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacac`](#insn-00bbacac)

~~~json
{
  "source": "00bbacac",
  "target": "00c24958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "00bdd450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacb4`](#insn-00bbacb4)

~~~json
{
  "source": "00bbacb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
