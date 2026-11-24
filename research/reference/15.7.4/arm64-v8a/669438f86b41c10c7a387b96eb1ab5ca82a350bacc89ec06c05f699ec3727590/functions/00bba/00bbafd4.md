# 00bbafd4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaf90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaf90.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-726d460294396abf0baa1f1b89537954)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37a1c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a1c.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-29495acf8f1f2ed4711340fcbbcca61b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafd4",
  "name": "_ZNSt12length_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a574187e8e657dcd6789b89616a66bac3c60637a6084ba6382fabd225757976c",
  "source_text_sha256": "a574187e8e657dcd6789b89616a66bac3c60637a6084ba6382fabd225757976c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafd4",
        "00bbafff"
      ]
    ],
    "bytes_sha256": "b7f743c0dfd04675e41e074ddbcc985cff23339723204b2934befe66772fe590",
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

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZNSt12length_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
                    /* try { // try from 00bbaff0 to 00cbaffb has its CatchHandler @ 00bbb8d4 */
                    /* try { // try from 00bbaffc to 00cbb00b has its CatchHandler @ 00bbb89c */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbafd4"></a> `00bbafd4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbafd8"></a> `00bbafd8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbafdc"></a> `00bbafdc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbafe0"></a> `00bbafe0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbafe4"></a> `00bbafe4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbafe8"></a> `00bbafe8` | `32 80 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbafec"></a> `00bbafec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbaff0"></a> `00bbaff0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaff4"></a> `00bbaff4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbaff8"></a> `00bbaff8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbaffc"></a> `00bbaffc` | `19 80 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafd4`](#insn-00bbafd4) 範囲 `[['00bbafd4', '00bbafef']]`
  - `FALL_THROUGH` [`00bbafec`](#insn-00bbafec) → [`00bbaff0`](#insn-00bbaff0)
- ブロック [`00bbaff0`](#insn-00bbaff0) 範囲 `[['00bbaff0', '00bbaffb']]`
  - `FALL_THROUGH` [`00bbaff8`](#insn-00bbaff8) → [`00bbaffc`](#insn-00bbaffc)
- ブロック [`00bbaffc`](#insn-00bbaffc) 範囲 `[['00bbaffc', '00bbafff']]`

## 命令位置別の参照

- [`00bbafd8`](#insn-00bbafd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafdc`](#insn-00bbafdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafe8`](#insn-00bbafe8) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff0`](#insn-00bbaff0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff4`](#insn-00bbaff4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbaffc`](#insn-00bbaffc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbafd8`](#insn-00bbafd8)

~~~json
{
  "source": "00bbafd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafdc`](#insn-00bbafdc)

~~~json
{
  "source": "00bbafdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafe8`](#insn-00bbafe8)

~~~json
{
  "source": "00bbafe8",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaff0`](#insn-00bbaff0)

~~~json
{
  "source": "00bbaff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaff4`](#insn-00bbaff4)

~~~json
{
  "source": "00bbaff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbaffc`](#insn-00bbaffc)

~~~json
{
  "source": "00bbaffc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
