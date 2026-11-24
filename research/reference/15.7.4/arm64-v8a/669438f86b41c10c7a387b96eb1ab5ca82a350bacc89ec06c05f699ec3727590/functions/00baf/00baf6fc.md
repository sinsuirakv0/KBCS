# 00baf6fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baf6b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-378ef66a7ec1c7b48e3f2aa627b718a3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2c144`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c144.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-5327f67744bd8b53e95444b416dba31a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf6fc",
  "name": "_ZNSt6__ndk115numpunct_bynameIcED0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50",
  "source_text_sha256": "073c302c2409df54ca7c43bbc1a1ae51eeadc21200bb1121eeb63aaa1c094f50",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baf6fc",
        "00baf727"
      ]
    ],
    "bytes_sha256": "01ba29b38a64b1cb190366c6c0291323d818fa7fb9f88c5e09ba2752645b9e75",
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
- [00be1c90](../00be1/00be1c90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 666 bytes

~~~c

void _ZNSt6__ndk115numpunct_bynameIcED0Ev(void *param_1)

{
                    /* try { // try from 00baf700 to 00caf70b has its CatchHandler @ 00baf710 */
                    /* catch() { ... } // from try @ 00baf58c with catch @ 00baf70c
                       try { // try from 00baf70c to 00caf73b has its CatchHandler @ 00baf554 */
                    /* catch() { ... } // from try @ 00baf700 with catch @ 00baf710 */
  _ZNSt6__ndk18numpunctIcED1Ev();
                    /* catch() { ... } // from try @ 00baf5c8 with catch @ 00baf714 */
                    /* catch() { ... } // from try @ 00baf5ec with catch @ 00baf718 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baf6fc"></a> `00baf6fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baf700"></a> `00baf700` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00baf704"></a> `00baf704` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf708"></a> `00baf708` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baf70c"></a> `00baf70c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00baf710"></a> `00baf710` | `60 c9 00 94` | bl 0x00be1c90 | `UNCONDITIONAL_CALL`
<a id="insn-00baf714"></a> `00baf714` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baf718"></a> `00baf718` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf71c"></a> `00baf71c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00baf720"></a> `00baf720` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baf724"></a> `00baf724` | `4f ae 00 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baf6fc`](#insn-00baf6fc) 範囲 `[['00baf6fc', '00baf6ff']]`
  - `FALL_THROUGH` [`00baf6fc`](#insn-00baf6fc) → [`00baf700`](#insn-00baf700)
- ブロック [`00baf700`](#insn-00baf700) 範囲 `[['00baf700', '00baf70b']]`
  - `FALL_THROUGH` [`00baf708`](#insn-00baf708) → [`00baf70c`](#insn-00baf70c)
- ブロック [`00baf70c`](#insn-00baf70c) 範囲 `[['00baf70c', '00baf70f']]`
  - `FALL_THROUGH` [`00baf70c`](#insn-00baf70c) → [`00baf710`](#insn-00baf710)
- ブロック [`00baf710`](#insn-00baf710) 範囲 `[['00baf710', '00baf713']]`
  - `FALL_THROUGH` [`00baf710`](#insn-00baf710) → [`00baf714`](#insn-00baf714)
- ブロック [`00baf714`](#insn-00baf714) 範囲 `[['00baf714', '00baf717']]`
  - `FALL_THROUGH` [`00baf714`](#insn-00baf714) → [`00baf718`](#insn-00baf718)
- ブロック [`00baf718`](#insn-00baf718) 範囲 `[['00baf718', '00baf727']]`

## 命令位置別の参照

- [`00baf700`](#insn-00baf700) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf704`](#insn-00baf704) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf710`](#insn-00baf710) → [`00be1c90`](../00be1/00be1c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1c90` · 推定シンボル `None` · 推定型 `None`
- [`00baf718`](#insn-00baf718) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf71c`](#insn-00baf71c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf724`](#insn-00baf724) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf700`](#insn-00baf700)

~~~json
{
  "source": "00baf700",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf704`](#insn-00baf704)

~~~json
{
  "source": "00baf704",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf710`](#insn-00baf710)

~~~json
{
  "source": "00baf710",
  "target": "00be1c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baf718`](#insn-00baf718)

~~~json
{
  "source": "00baf718",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf71c`](#insn-00baf71c)

~~~json
{
  "source": "00baf71c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf724`](#insn-00baf724)

~~~json
{
  "source": "00baf724",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
