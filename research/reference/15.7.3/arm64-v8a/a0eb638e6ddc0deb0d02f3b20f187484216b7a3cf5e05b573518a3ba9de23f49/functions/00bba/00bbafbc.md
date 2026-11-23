# 00bbafbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbaef4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaef4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0006.md#compare-331fe9bd2b0e366392bd2127bdf714bf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbb000`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-e8ef04253a8b34e7fe39eb6209456445)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafbc",
  "name": "_ZNSt12out_of_rangeD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "595813dfd06b7b691e9da135fa51997e37e13bd0b2e5738f89fa7647d52d9dea",
  "source_text_sha256": "595813dfd06b7b691e9da135fa51997e37e13bd0b2e5738f89fa7647d52d9dea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafbc",
        "00bbafe7"
      ]
    ],
    "bytes_sha256": "2a9664d312f881cf66734f8982791eff56cb35ffa260a12de817aa8e7c4d048b",
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

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb200](../00bdb/00bdb200.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 205 bytes

~~~c

void _ZNSt12out_of_rangeD0Ev(void *param_1)

{
                    /* try { // try from 00bbafc8 to 00cbafdb has its CatchHandler @ 00bbb840 */
  _ZNSt11logic_errorD1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbafbc"></a> `00bbafbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbafc0"></a> `00bbafc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbafc4"></a> `00bbafc4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbafc8"></a> `00bbafc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbafcc"></a> `00bbafcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbafd0"></a> `00bbafd0` | `8c 80 00 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafd4"></a> `00bbafd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafd8"></a> `00bbafd8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbafdc"></a> `00bbafdc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbafe0"></a> `00bbafe0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbafe4"></a> `00bbafe4` | `0b 80 00 14` | b 0x00bdb010 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafbc`](#insn-00bbafbc) 範囲 `[['00bbafbc', '00bbafc7']]`
  - `FALL_THROUGH` [`00bbafc4`](#insn-00bbafc4) → [`00bbafc8`](#insn-00bbafc8)
- ブロック [`00bbafc8`](#insn-00bbafc8) 範囲 `[['00bbafc8', '00bbafe7']]`

## 命令位置別の参照

- [`00bbafc0`](#insn-00bbafc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafc4`](#insn-00bbafc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafd0`](#insn-00bbafd0) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00bbafd8`](#insn-00bbafd8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafdc`](#insn-00bbafdc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafe4`](#insn-00bbafe4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbafc0`](#insn-00bbafc0)

~~~json
{
  "source": "00bbafc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafc4`](#insn-00bbafc4)

~~~json
{
  "source": "00bbafc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafd0`](#insn-00bbafd0)

~~~json
{
  "source": "00bbafd0",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbafd8`](#insn-00bbafd8)

~~~json
{
  "source": "00bbafd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafdc`](#insn-00bbafdc)

~~~json
{
  "source": "00bbafdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafe4`](#insn-00bbafe4)

~~~json
{
  "source": "00bbafe4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
