# 007cbdac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007cbdac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cb/007cbdac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0037.md#compare-d92fff3b07c4c969731920b04fc555a8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fefac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fefac.md) · 移動量 `+0x33200`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0036.md#compare-dbb9244205af4fe027f216bde2ba34c2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007cbdac",
  "name": "FUN_007cbdac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ab2accf7eb7fdeea749ff2dbbb47c62c103a48a3a729e7b54c25075f43471d7",
  "source_text_sha256": "7ab2accf7eb7fdeea749ff2dbbb47c62c103a48a3a729e7b54c25075f43471d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007cbdac",
        "007cbdeb"
      ]
    ],
    "bytes_sha256": "a52f7cf8650c0c16226e3017de242fbdf05e1e4fb77128b27ec3f164de0239aa",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 329 bytes

~~~c

void FUN_007cbdac(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)param_1[2];
  *param_1 = &PTR_FUN_00bffff8;
  if (__ptr != (void *)0x0) {
    param_1[3] = __ptr;
    _ZdlPv(__ptr);
  }
                    /* try { // try from 007cbde8 to 008cbe0f has its CatchHandler @ 007cde44 */
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007cbdac"></a> `007cbdac` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007cbdb0"></a> `007cbdb0` | `a9 21 00 90` | adrp x9,0xbff000 | `FALL_THROUGH`
<a id="insn-007cbdb4"></a> `007cbdb4` | `29 e1 3f 91` | add x9,x9,#0xff8 | `FALL_THROUGH`
<a id="insn-007cbdb8"></a> `007cbdb8` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-007cbdbc"></a> `007cbdbc` | `68 01 00 b4` | cbz x8,0x007cbde8 | `CONDITIONAL_JUMP`
<a id="insn-007cbdc0"></a> `007cbdc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007cbdc4"></a> `007cbdc4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cbdc8"></a> `007cbdc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007cbdcc"></a> `007cbdcc` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-007cbdd0"></a> `007cbdd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007cbdd4"></a> `007cbdd4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007cbdd8"></a> `007cbdd8` | `a2 3c 10 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-007cbddc"></a> `007cbddc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007cbde0"></a> `007cbde0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007cbde4"></a> `007cbde4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007cbde8"></a> `007cbde8` | `9e 3c 10 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007cbdac`](#insn-007cbdac) 範囲 `[['007cbdac', '007cbdbf']]`
  - `CONDITIONAL_JUMP` [`007cbdbc`](#insn-007cbdbc) → [`007cbde8`](#insn-007cbde8)
  - `FALL_THROUGH` [`007cbdbc`](#insn-007cbdbc) → [`007cbdc0`](#insn-007cbdc0)
- ブロック [`007cbdc0`](#insn-007cbdc0) 範囲 `[['007cbdc0', '007cbde7']]`
  - `FALL_THROUGH` [`007cbde4`](#insn-007cbde4) → [`007cbde8`](#insn-007cbde8)
- ブロック [`007cbde8`](#insn-007cbde8) 範囲 `[['007cbde8', '007cbdeb']]`

## 命令位置別の参照

- [`007cbdb8`](#insn-007cbdb8) → `00bffff8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007cbdbc`](#insn-007cbdbc) → [`007cbde8`](#insn-007cbde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbdc0`](#insn-007cbdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbdc4`](#insn-007cbdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbdd8`](#insn-007cbdd8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`007cbde0`](#insn-007cbde0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbde4`](#insn-007cbde4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007cbde8`](#insn-007cbde8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007cbdb8`](#insn-007cbdb8)

~~~json
{
  "source": "007cbdb8",
  "target": "00bffff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bffff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007cbdbc`](#insn-007cbdbc)

~~~json
{
  "source": "007cbdbc",
  "target": "007cbde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbdc0`](#insn-007cbdc0)

~~~json
{
  "source": "007cbdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbdc4`](#insn-007cbdc4)

~~~json
{
  "source": "007cbdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbdd8`](#insn-007cbdd8)

~~~json
{
  "source": "007cbdd8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007cbde0`](#insn-007cbde0)

~~~json
{
  "source": "007cbde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbde4`](#insn-007cbde4)

~~~json
{
  "source": "007cbde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007cbde8`](#insn-007cbde8)

~~~json
{
  "source": "007cbde8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
