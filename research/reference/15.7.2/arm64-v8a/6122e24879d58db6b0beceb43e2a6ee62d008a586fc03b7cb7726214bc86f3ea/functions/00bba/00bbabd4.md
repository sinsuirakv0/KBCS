# 00bbabd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbac9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac9c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3366d56ecb19a51b1da99de8b3b0c84f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabd4",
  "name": "__cxa_get_globals_fast",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "454f2618440951def784c9f3f68bcb87c5cc95ede6b9665b02bfa21a225ab47c",
  "source_text_sha256": "454f2618440951def784c9f3f68bcb87c5cc95ede6b9665b02bfa21a225ab47c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabd4",
        "00bbabf7"
      ]
    ],
    "bytes_sha256": "530e71fdb3c577c9ab9876a01376299e69c4496476db0a09059f530a701daa75",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1ce0](../00be1/00be1ce0.md)

## 呼び出し先

- [00bdd3a0](../00bdd/00bdd3a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 786 bytes

~~~c

void __cxa_get_globals_fast(void)

{
                    /* catch() { ... } // from try @ 00bb7384 with catch @ 00bbabd8 */
                    /* catch() { ... } // from try @ 00bb6fd0 with catch @ 00bbabdc */
                    /* catch() { ... } // from try @ 00bb6c1c with catch @ 00bbabe0 */
                    /* catch() { ... } // from try @ 00bb6868 with catch @ 00bbabe4 */
                    /* catch() { ... } // from try @ 00bb64b4 with catch @ 00bbabe8 */
  __emutls_get_address(&DAT_00c248a8);
                    /* catch() { ... } // from try @ 00bb6100 with catch @ 00bbabec */
                    /* catch() { ... } // from try @ 00bb5d40 with catch @ 00bbabf0 */
                    /* catch() { ... } // from try @ 00bb5980 with catch @ 00bbabf4 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabd4"></a> `00bbabd4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbabd8"></a> `00bbabd8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbabdc"></a> `00bbabdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbabe0"></a> `00bbabe0` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbabe4"></a> `00bbabe4` | `20 e6 34 10` | adr x0,0xc248a8 | `FALL_THROUGH`
<a id="insn-00bbabe8"></a> `00bbabe8` | `ee 89 00 94` | bl 0x00bdd3a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbabec"></a> `00bbabec` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbabf0"></a> `00bbabf0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbabf4"></a> `00bbabf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabd4`](#insn-00bbabd4) 範囲 `[['00bbabd4', '00bbabd7']]`
  - `FALL_THROUGH` [`00bbabd4`](#insn-00bbabd4) → [`00bbabd8`](#insn-00bbabd8)
- ブロック [`00bbabd8`](#insn-00bbabd8) 範囲 `[['00bbabd8', '00bbabdb']]`
  - `FALL_THROUGH` [`00bbabd8`](#insn-00bbabd8) → [`00bbabdc`](#insn-00bbabdc)
- ブロック [`00bbabdc`](#insn-00bbabdc) 範囲 `[['00bbabdc', '00bbabdf']]`
  - `FALL_THROUGH` [`00bbabdc`](#insn-00bbabdc) → [`00bbabe0`](#insn-00bbabe0)
- ブロック [`00bbabe0`](#insn-00bbabe0) 範囲 `[['00bbabe0', '00bbabe3']]`
  - `FALL_THROUGH` [`00bbabe0`](#insn-00bbabe0) → [`00bbabe4`](#insn-00bbabe4)
- ブロック [`00bbabe4`](#insn-00bbabe4) 範囲 `[['00bbabe4', '00bbabe7']]`
  - `FALL_THROUGH` [`00bbabe4`](#insn-00bbabe4) → [`00bbabe8`](#insn-00bbabe8)
- ブロック [`00bbabe8`](#insn-00bbabe8) 範囲 `[['00bbabe8', '00bbabeb']]`
  - `FALL_THROUGH` [`00bbabe8`](#insn-00bbabe8) → [`00bbabec`](#insn-00bbabec)
- ブロック [`00bbabec`](#insn-00bbabec) 範囲 `[['00bbabec', '00bbabef']]`
  - `FALL_THROUGH` [`00bbabec`](#insn-00bbabec) → [`00bbabf0`](#insn-00bbabf0)
- ブロック [`00bbabf0`](#insn-00bbabf0) 範囲 `[['00bbabf0', '00bbabf3']]`
  - `FALL_THROUGH` [`00bbabf0`](#insn-00bbabf0) → [`00bbabf4`](#insn-00bbabf4)
- ブロック [`00bbabf4`](#insn-00bbabf4) 範囲 `[['00bbabf4', '00bbabf7']]`

## 命令位置別の参照

- [`00bbabd8`](#insn-00bbabd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabe4`](#insn-00bbabe4) → `00c248a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabe8`](#insn-00bbabe8) → [`00bdd3a0`](../00bdd/00bdd3a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd3a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbabec`](#insn-00bbabec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabd8`](#insn-00bbabd8)

~~~json
{
  "source": "00bbabd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabe4`](#insn-00bbabe4)

~~~json
{
  "source": "00bbabe4",
  "target": "00c248a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabe8`](#insn-00bbabe8)

~~~json
{
  "source": "00bbabe8",
  "target": "00bdd3a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbabec`](#insn-00bbabec)

~~~json
{
  "source": "00bbabec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
