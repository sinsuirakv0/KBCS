# 00bbace0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac9c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-8f7e8fe1d2bfa265a2430422e780df2c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37728`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37728.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-fa4b4d751032a0ea6e049ac5c0094013)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbace0",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f4ff2f89d9b652fda7a5978b4731454daade64a1b801b48d17bd5d4b38353565",
  "source_text_sha256": "f4ff2f89d9b652fda7a5978b4731454daade64a1b801b48d17bd5d4b38353565",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbace0",
        "00bbad03"
      ]
    ],
    "bytes_sha256": "519d689e527d94d966c5743859654e9198e7b0ec22edd3124267902ef8c86cbf",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1de0](../00be1/00be1de0.md)

## 呼び出し先

- [00bdd4a0](../00bdd/00bdd4a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb7490 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb70dc with catch @ 00bbace8 */
                    /* catch() { ... } // from try @ 00bb6d28 with catch @ 00bbacec */
                    /* catch() { ... } // from try @ 00bb6974 with catch @ 00bbacf0 */
                    /* catch() { ... } // from try @ 00bb65c0 with catch @ 00bbacf4 */
  __emutls_get_address(&DAT_00c249a8);
                    /* catch() { ... } // from try @ 00bb620c with catch @ 00bbacf8 */
                    /* catch() { ... } // from try @ 00bb5e4c with catch @ 00bbacfc */
                    /* catch() { ... } // from try @ 00bb5a8c with catch @ 00bbad00 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbace0"></a> `00bbace0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbace8"></a> `00bbace8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbacec"></a> `00bbacec` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbacf0"></a> `00bbacf0` | `c0 e5 34 10` | adr x0,0xc249a8 | `FALL_THROUGH`
<a id="insn-00bbacf4"></a> `00bbacf4` | `eb 89 00 94` | bl 0x00bdd4a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacf8"></a> `00bbacf8` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbacfc"></a> `00bbacfc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbad00"></a> `00bbad00` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbace0`](#insn-00bbace0) 範囲 `[['00bbace0', '00bbace3']]`
  - `FALL_THROUGH` [`00bbace0`](#insn-00bbace0) → [`00bbace4`](#insn-00bbace4)
- ブロック [`00bbace4`](#insn-00bbace4) 範囲 `[['00bbace4', '00bbace7']]`
  - `FALL_THROUGH` [`00bbace4`](#insn-00bbace4) → [`00bbace8`](#insn-00bbace8)
- ブロック [`00bbace8`](#insn-00bbace8) 範囲 `[['00bbace8', '00bbaceb']]`
  - `FALL_THROUGH` [`00bbace8`](#insn-00bbace8) → [`00bbacec`](#insn-00bbacec)
- ブロック [`00bbacec`](#insn-00bbacec) 範囲 `[['00bbacec', '00bbacef']]`
  - `FALL_THROUGH` [`00bbacec`](#insn-00bbacec) → [`00bbacf0`](#insn-00bbacf0)
- ブロック [`00bbacf0`](#insn-00bbacf0) 範囲 `[['00bbacf0', '00bbacf3']]`
  - `FALL_THROUGH` [`00bbacf0`](#insn-00bbacf0) → [`00bbacf4`](#insn-00bbacf4)
- ブロック [`00bbacf4`](#insn-00bbacf4) 範囲 `[['00bbacf4', '00bbacf7']]`
  - `FALL_THROUGH` [`00bbacf4`](#insn-00bbacf4) → [`00bbacf8`](#insn-00bbacf8)
- ブロック [`00bbacf8`](#insn-00bbacf8) 範囲 `[['00bbacf8', '00bbacfb']]`
  - `FALL_THROUGH` [`00bbacf8`](#insn-00bbacf8) → [`00bbacfc`](#insn-00bbacfc)
- ブロック [`00bbacfc`](#insn-00bbacfc) 範囲 `[['00bbacfc', '00bbacff']]`
  - `FALL_THROUGH` [`00bbacfc`](#insn-00bbacfc) → [`00bbad00`](#insn-00bbad00)
- ブロック [`00bbad00`](#insn-00bbad00) 範囲 `[['00bbad00', '00bbad03']]`

## 命令位置別の参照

- [`00bbace4`](#insn-00bbace4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf0`](#insn-00bbacf0) → `00c249a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf4`](#insn-00bbacf4) → [`00bdd4a0`](../00bdd/00bdd4a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd4a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbacf8`](#insn-00bbacf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbace4`](#insn-00bbace4)

~~~json
{
  "source": "00bbace4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacf0`](#insn-00bbacf0)

~~~json
{
  "source": "00bbacf0",
  "target": "00c249a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacf4`](#insn-00bbacf4)

~~~json
{
  "source": "00bbacf4",
  "target": "00bdd4a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacf8`](#insn-00bbacf8)

~~~json
{
  "source": "00bbacf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
