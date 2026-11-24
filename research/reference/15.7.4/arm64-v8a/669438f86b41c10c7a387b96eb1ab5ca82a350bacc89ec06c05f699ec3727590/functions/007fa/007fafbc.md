# 007fafbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007fafbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007fa/007fafbc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0006.md#compare-9ceef298ac5dc59e479a902602bced8c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0058.md#review-93bdbcb08c2b1b40ae9bbf4f5cb793b6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fafbc",
  "name": "FUN_007fafbc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84095a7ab681efad1b2cb362fc49afb7a995f3fb00a007bb2912555b0def033b",
  "source_text_sha256": "84095a7ab681efad1b2cb362fc49afb7a995f3fb00a007bb2912555b0def033b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fafbc",
        "007fafeb"
      ]
    ],
    "bytes_sha256": "7a6cdc684251f27290d5661317468ffbe3a872ddb283c0af2415fe5502d0510f",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb050](../00bdb/00bdb050.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 592 bytes

~~~c

void FUN_007fafbc(undefined8 *param_1)

{
                    /* catch() { ... } // from try @ 007fae88 with catch @ 007fafc8
                       try { // try from 007fafc8 to 008fb12f has its CatchHandler @ 007fa6b0 */
                    /* catch() { ... } // from try @ 007fa800 with catch @ 007fafcc */
                    /* catch() { ... } // from try @ 007fa790 with catch @ 007fafd0 */
  *param_1 = &PTR_FUN_00c00448;
  _ZNSt6__ndk119__shared_weak_countD2Ev();
                    /* catch() { ... } // from try @ 007fa784 with catch @ 007fafe0 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fafbc"></a> `007fafbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fafc0"></a> `007fafc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fafc4"></a> `007fafc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fafc8"></a> `007fafc8` | `28 20 00 d0` | adrp x8,0xc00000 | `FALL_THROUGH`
<a id="insn-007fafcc"></a> `007fafcc` | `08 21 11 91` | add x8,x8,#0x448 | `FALL_THROUGH`
<a id="insn-007fafd0"></a> `007fafd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007fafd4"></a> `007fafd4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007fafd8"></a> `007fafd8` | `1e 80 0f 94` | bl 0x00bdb050 | `UNCONDITIONAL_CALL`
<a id="insn-007fafdc"></a> `007fafdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fafe0"></a> `007fafe0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fafe4"></a> `007fafe4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fafe8"></a> `007fafe8` | `1e 80 0f 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fafbc`](#insn-007fafbc) 範囲 `[['007fafbc', '007fafc7']]`
  - `FALL_THROUGH` [`007fafc4`](#insn-007fafc4) → [`007fafc8`](#insn-007fafc8)
- ブロック [`007fafc8`](#insn-007fafc8) 範囲 `[['007fafc8', '007fafcb']]`
  - `FALL_THROUGH` [`007fafc8`](#insn-007fafc8) → [`007fafcc`](#insn-007fafcc)
- ブロック [`007fafcc`](#insn-007fafcc) 範囲 `[['007fafcc', '007fafcf']]`
  - `FALL_THROUGH` [`007fafcc`](#insn-007fafcc) → [`007fafd0`](#insn-007fafd0)
- ブロック [`007fafd0`](#insn-007fafd0) 範囲 `[['007fafd0', '007fafdf']]`
  - `FALL_THROUGH` [`007fafdc`](#insn-007fafdc) → [`007fafe0`](#insn-007fafe0)
- ブロック [`007fafe0`](#insn-007fafe0) 範囲 `[['007fafe0', '007fafeb']]`

## 命令位置別の参照

- [`007fafbc`](#insn-007fafbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafc0`](#insn-007fafc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafd4`](#insn-007fafd4) → `00c00448`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007fafd8`](#insn-007fafd8) → [`00bdb050`](../00bdb/00bdb050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb050` · 推定シンボル `None` · 推定型 `None`
- [`007fafe0`](#insn-007fafe0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafe4`](#insn-007fafe4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafe8`](#insn-007fafe8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fafbc`](#insn-007fafbc)

~~~json
{
  "source": "007fafbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafc0`](#insn-007fafc0)

~~~json
{
  "source": "007fafc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafd4`](#insn-007fafd4)

~~~json
{
  "source": "007fafd4",
  "target": "00c00448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c00448",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fafd8`](#insn-007fafd8)

~~~json
{
  "source": "007fafd8",
  "target": "00bdb050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fafe0`](#insn-007fafe0)

~~~json
{
  "source": "007fafe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafe4`](#insn-007fafe4)

~~~json
{
  "source": "007fafe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafe8`](#insn-007fafe8)

~~~json
{
  "source": "007fafe8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
