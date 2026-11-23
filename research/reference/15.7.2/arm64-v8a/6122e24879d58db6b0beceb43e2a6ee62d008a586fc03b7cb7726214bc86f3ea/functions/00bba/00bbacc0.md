# 00bbacc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-7c1b69988c49deb7304d69d3005a2263)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacc0",
  "name": "_ZNSt9bad_allocD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6af7d0c3110e34206d6d7ada97c2c873817a21f7d59673a9b448ef725ed276c1",
  "source_text_sha256": "6af7d0c3110e34206d6d7ada97c2c873817a21f7d59673a9b448ef725ed276c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacc0",
        "00bbaceb"
      ]
    ],
    "bytes_sha256": "b856f36529acb4c5bc7b3db3117c6804e0311c289ffce84ed3370aa0714dcfe1",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdbb00](../00bdb/00bdbb00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 983 bytes

~~~c

void _ZNSt9bad_allocD0Ev(void *param_1)

{
                    /* catch() { ... } // from try @ 00bb6e48 with catch @ 00bbacc4 */
                    /* catch() { ... } // from try @ 00bb6a94 with catch @ 00bbacc8 */
                    /* catch() { ... } // from try @ 00bb6a7c with catch @ 00bbaccc */
                    /* catch() { ... } // from try @ 00bb66c8 with catch @ 00bbacd0 */
                    /* catch() { ... } // from try @ 00bb66e0 with catch @ 00bbacd4 */
  _ZNSt20bad_array_new_lengthD1Ev();
                    /* catch() { ... } // from try @ 00bb6314 with catch @ 00bbacd8 */
                    /* catch() { ... } // from try @ 00bb632c with catch @ 00bbacdc */
                    /* catch() { ... } // from try @ 00bb5f78 with catch @ 00bbace0 */
                    /* catch() { ... } // from try @ 00bb5f60 with catch @ 00bbace4 */
                    /* catch() { ... } // from try @ 00bb5bb8 with catch @ 00bbace8 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacc0"></a> `00bbacc0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbacc4"></a> `00bbacc4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbacc8"></a> `00bbacc8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaccc"></a> `00bbaccc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbacd0"></a> `00bbacd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbacd4"></a> `00bbacd4` | `8b 83 00 94` | bl 0x00bdbb00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbacd8"></a> `00bbacd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbacdc"></a> `00bbacdc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbace0"></a> `00bbace0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbace4"></a> `00bbace4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbace8"></a> `00bbace8` | `9e 80 00 14` | b 0x00bdaf60 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacc0`](#insn-00bbacc0) 範囲 `[['00bbacc0', '00bbacc3']]`
  - `FALL_THROUGH` [`00bbacc0`](#insn-00bbacc0) → [`00bbacc4`](#insn-00bbacc4)
- ブロック [`00bbacc4`](#insn-00bbacc4) 範囲 `[['00bbacc4', '00bbacc7']]`
  - `FALL_THROUGH` [`00bbacc4`](#insn-00bbacc4) → [`00bbacc8`](#insn-00bbacc8)
- ブロック [`00bbacc8`](#insn-00bbacc8) 範囲 `[['00bbacc8', '00bbaccb']]`
  - `FALL_THROUGH` [`00bbacc8`](#insn-00bbacc8) → [`00bbaccc`](#insn-00bbaccc)
- ブロック [`00bbaccc`](#insn-00bbaccc) 範囲 `[['00bbaccc', '00bbaccf']]`
  - `FALL_THROUGH` [`00bbaccc`](#insn-00bbaccc) → [`00bbacd0`](#insn-00bbacd0)
- ブロック [`00bbacd0`](#insn-00bbacd0) 範囲 `[['00bbacd0', '00bbacd3']]`
  - `FALL_THROUGH` [`00bbacd0`](#insn-00bbacd0) → [`00bbacd4`](#insn-00bbacd4)
- ブロック [`00bbacd4`](#insn-00bbacd4) 範囲 `[['00bbacd4', '00bbacd7']]`
  - `FALL_THROUGH` [`00bbacd4`](#insn-00bbacd4) → [`00bbacd8`](#insn-00bbacd8)
- ブロック [`00bbacd8`](#insn-00bbacd8) 範囲 `[['00bbacd8', '00bbacdb']]`
  - `FALL_THROUGH` [`00bbacd8`](#insn-00bbacd8) → [`00bbacdc`](#insn-00bbacdc)
- ブロック [`00bbacdc`](#insn-00bbacdc) 範囲 `[['00bbacdc', '00bbacdf']]`
  - `FALL_THROUGH` [`00bbacdc`](#insn-00bbacdc) → [`00bbace0`](#insn-00bbace0)
- ブロック [`00bbace0`](#insn-00bbace0) 範囲 `[['00bbace0', '00bbace3']]`
  - `FALL_THROUGH` [`00bbace0`](#insn-00bbace0) → [`00bbace4`](#insn-00bbace4)
- ブロック [`00bbace4`](#insn-00bbace4) 範囲 `[['00bbace4', '00bbace7']]`
  - `FALL_THROUGH` [`00bbace4`](#insn-00bbace4) → [`00bbace8`](#insn-00bbace8)
- ブロック [`00bbace8`](#insn-00bbace8) 範囲 `[['00bbace8', '00bbaceb']]`

## 命令位置別の参照

- [`00bbacc4`](#insn-00bbacc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacc8`](#insn-00bbacc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbacd4`](#insn-00bbacd4) → [`00bdbb00`](../00bdb/00bdbb00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbb00` · 推定シンボル `None` · 推定型 `None`
- [`00bbacdc`](#insn-00bbacdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbace0`](#insn-00bbace0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbace8`](#insn-00bbace8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacc4`](#insn-00bbacc4)

~~~json
{
  "source": "00bbacc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacc8`](#insn-00bbacc8)

~~~json
{
  "source": "00bbacc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbacd4`](#insn-00bbacd4)

~~~json
{
  "source": "00bbacd4",
  "target": "00bdbb00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbacdc`](#insn-00bbacdc)

~~~json
{
  "source": "00bbacdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbace0`](#insn-00bbace0)

~~~json
{
  "source": "00bbace0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbace8`](#insn-00bbace8)

~~~json
{
  "source": "00bbace8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
