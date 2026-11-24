# 00af5ccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af5c88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-ae9c9d0508853699c943e8e7015429ea)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b55a50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55a50.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-1f9cdde13c050e843cfcc1d34a201caf)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5ccc",
  "name": "_ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ced2c64190f39fb3bb0136b08365f0188b3c03c2fee3805cd2a27a8049278a9",
  "source_text_sha256": "6ced2c64190f39fb3bb0136b08365f0188b3c03c2fee3805cd2a27a8049278a9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5ccc",
        "00af5cf7"
      ]
    ],
    "bytes_sha256": "10b3bfce774f79c615944eff9c0c4c09566cf9b0b1f0ea8c48298a7d4a5c418d",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 582 bytes

~~~c

undefined8
_ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_
          (long *param_1,undefined8 param_2,undefined8 param_3)

{
                    /* try { // try from 00af5cd0 to 00bf5cd7 has its CatchHandler @ 00affbec */
                    /* try { // try from 00af5cdc to 00bf5ce3 has its CatchHandler @ 00affbe0 */
  (**(code **)(*param_1 + 0xb8))();
                    /* try { // try from 00af5ce8 to 00bf5cef has its CatchHandler @ 00affbd4 */
                    /* try { // try from 00af5cf4 to 00bf5cfb has its CatchHandler @ 00affbc8 */
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5ccc"></a> `00af5ccc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af5cd0"></a> `00af5cd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5cd4"></a> `00af5cd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af5cd8"></a> `00af5cd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00af5cdc"></a> `00af5cdc` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00af5ce0"></a> `00af5ce0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af5ce4"></a> `00af5ce4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5ce8"></a> `00af5ce8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5cec"></a> `00af5cec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5cf0"></a> `00af5cf0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af5cf4"></a> `00af5cf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af5ccc`](#insn-00af5ccc) 範囲 `[['00af5ccc', '00af5ccf']]`
  - `FALL_THROUGH` [`00af5ccc`](#insn-00af5ccc) → [`00af5cd0`](#insn-00af5cd0)
- ブロック [`00af5cd0`](#insn-00af5cd0) 範囲 `[['00af5cd0', '00af5cdb']]`
  - `FALL_THROUGH` [`00af5cd8`](#insn-00af5cd8) → [`00af5cdc`](#insn-00af5cdc)
- ブロック [`00af5cdc`](#insn-00af5cdc) 範囲 `[['00af5cdc', '00af5ce7']]`
  - `FALL_THROUGH` [`00af5ce4`](#insn-00af5ce4) → [`00af5ce8`](#insn-00af5ce8)
- ブロック [`00af5ce8`](#insn-00af5ce8) 範囲 `[['00af5ce8', '00af5cf3']]`
  - `FALL_THROUGH` [`00af5cf0`](#insn-00af5cf0) → [`00af5cf4`](#insn-00af5cf4)
- ブロック [`00af5cf4`](#insn-00af5cf4) 範囲 `[['00af5cf4', '00af5cf7']]`

## 命令位置別の参照

- [`00af5ccc`](#insn-00af5ccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5cd0`](#insn-00af5cd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ce8`](#insn-00af5ce8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5ccc`](#insn-00af5ccc)

~~~json
{
  "source": "00af5ccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5cd0`](#insn-00af5cd0)

~~~json
{
  "source": "00af5cd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ce8`](#insn-00af5ce8)

~~~json
{
  "source": "00af5ce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
