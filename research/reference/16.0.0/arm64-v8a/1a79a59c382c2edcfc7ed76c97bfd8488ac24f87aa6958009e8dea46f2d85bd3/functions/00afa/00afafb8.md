# 00afafb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0169.md#review-04c5c0fd77a97f423d7acbc65ed9ecdb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb3e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb3e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-a343f2a2741dd1a8707309ed3650cadf)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afafb8",
  "name": "FUN_00afafb8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68a43de458a730a6f8cef2357cafa3f0a71283520c6b1c824fb13b312cb5fb10",
  "source_text_sha256": "68a43de458a730a6f8cef2357cafa3f0a71283520c6b1c824fb13b312cb5fb10",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afafb8",
        "00afafff"
      ]
    ],
    "bytes_sha256": "23ade2071e58153675430aa6171807aa1712a3615c2a3742508b9b7537e2b335",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ea1c](../0070e/0070ea1c.md)
- [007119b0](../00711/007119b0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 377 bytes

~~~c

bool FUN_00afafb8(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afafc0 to 00bfafe3 has its CatchHandler @ 00afb164 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afafe4 to 00bfb2af has its CatchHandler @ 00afaa30 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c54) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afafb8"></a> `00afafb8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afafbc"></a> `00afafbc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afafc0"></a> `00afafc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afafc4"></a> `00afafc4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afafc8"></a> `00afafc8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afafcc"></a> `00afafcc` | `3b 59 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afafd0"></a> `00afafd0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afafd4"></a> `00afafd4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afafd8"></a> `00afafd8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afafdc"></a> `00afafdc` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afafe0"></a> `00afafe0` | `89 8a 89 52` | mov w9,#0x4c54 | `FALL_THROUGH`
<a id="insn-00afafe4"></a> `00afafe4` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afafe8"></a> `00afafe8` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afafec"></a> `00afafec` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afaff0"></a> `00afaff0` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afaff4"></a> `00afaff4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaff8"></a> `00afaff8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afaffc"></a> `00afaffc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afafb8`](#insn-00afafb8) 範囲 `[['00afafb8', '00afafbf']]`
  - `FALL_THROUGH` [`00afafbc`](#insn-00afafbc) → [`00afafc0`](#insn-00afafc0)
- ブロック [`00afafc0`](#insn-00afafc0) 範囲 `[['00afafc0', '00afafe3']]`
  - `FALL_THROUGH` [`00afafe0`](#insn-00afafe0) → [`00afafe4`](#insn-00afafe4)
- ブロック [`00afafe4`](#insn-00afafe4) 範囲 `[['00afafe4', '00afafff']]`

## 命令位置別の参照

- [`00afafb8`](#insn-00afafb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafbc`](#insn-00afafbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafcc`](#insn-00afafcc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afaff4`](#insn-00afaff4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaff8`](#insn-00afaff8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afafb8`](#insn-00afafb8)

~~~json
{
  "source": "00afafb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafbc`](#insn-00afafbc)

~~~json
{
  "source": "00afafbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafcc`](#insn-00afafcc)

~~~json
{
  "source": "00afafcc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaff4`](#insn-00afaff4)

~~~json
{
  "source": "00afaff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaff8`](#insn-00afaff8)

~~~json
{
  "source": "00afaff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
