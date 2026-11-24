# 007fdccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `007caacc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ca/007caacc.md) · 移動量 `+0x33200`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0007.md#compare-10568035478fe8a3fbfa84e4e453a1ce)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007fdd0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fd/007fdd0c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-58ca30c7f757c0b40dfa43ab93cbfec0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fdccc",
  "name": "FUN_007fdccc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5f1ff53fe86f9b0e57927e0a8bd892630227979e111b36b9d744063ab6d4339",
  "source_text_sha256": "e5f1ff53fe86f9b0e57927e0a8bd892630227979e111b36b9d744063ab6d4339",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fdccc",
        "007fdd13"
      ]
    ],
    "bytes_sha256": "6e5eefb05b14342736dd1d74d58c5097300bd1242a7bb985925db04445256793",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b9134](../008b9/008b9134.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 407 bytes

~~~c

void FUN_007fdccc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar2 = *param_2;
    uVar1 = FUN_0047acb4();
                    /* try { // try from 007fdcf4 to 008fdd3f has its CatchHandler @ 007fe038 */
    FUN_0047cd94(uVar1,0xb,0);
    FUN_008b9134(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fdccc"></a> `007fdccc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007fdcd0"></a> `007fdcd0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007fdcd4"></a> `007fdcd4` | `e1 01 00 54` | b.ne 0x007fdd10 | `CONDITIONAL_JUMP`
<a id="insn-007fdcd8"></a> `007fdcd8` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fdcdc"></a> `007fdcdc` | `a8 01 00 35` | cbnz w8,0x007fdd10 | `CONDITIONAL_JUMP`
<a id="insn-007fdce0"></a> `007fdce0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fdce4"></a> `007fdce4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdce8"></a> `007fdce8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fdcec"></a> `007fdcec` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fdcf0"></a> `007fdcf0` | `f1 f3 f1 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-007fdcf4"></a> `007fdcf4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fdcf8"></a> `007fdcf8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fdcfc"></a> `007fdcfc` | `26 fc f1 97` | bl 0x0047cd94 | `UNCONDITIONAL_CALL`
<a id="insn-007fdd00"></a> `007fdd00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fdd04"></a> `007fdd04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdd08"></a> `007fdd08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fdd0c"></a> `007fdd0c` | `0a ed 02 14` | b 0x008b9134 | `CALL_TERMINATOR`
<a id="insn-007fdd10"></a> `007fdd10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fdccc`](#insn-007fdccc) 範囲 `[['007fdccc', '007fdcd7']]`
  - `CONDITIONAL_JUMP` [`007fdcd4`](#insn-007fdcd4) → [`007fdd10`](#insn-007fdd10)
  - `FALL_THROUGH` [`007fdcd4`](#insn-007fdcd4) → [`007fdcd8`](#insn-007fdcd8)
- ブロック [`007fdcd8`](#insn-007fdcd8) 範囲 `[['007fdcd8', '007fdcdf']]`
  - `CONDITIONAL_JUMP` [`007fdcdc`](#insn-007fdcdc) → [`007fdd10`](#insn-007fdd10)
  - `FALL_THROUGH` [`007fdcdc`](#insn-007fdcdc) → [`007fdce0`](#insn-007fdce0)
- ブロック [`007fdce0`](#insn-007fdce0) 範囲 `[['007fdce0', '007fdcf3']]`
  - `FALL_THROUGH` [`007fdcf0`](#insn-007fdcf0) → [`007fdcf4`](#insn-007fdcf4)
- ブロック [`007fdcf4`](#insn-007fdcf4) 範囲 `[['007fdcf4', '007fdd0f']]`
- ブロック [`007fdd10`](#insn-007fdd10) 範囲 `[['007fdd10', '007fdd13']]`

## 命令位置別の参照

- [`007fdcd4`](#insn-007fdcd4) → [`007fdd10`](#insn-007fdd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdcdc`](#insn-007fdcdc) → [`007fdd10`](#insn-007fdd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdce0`](#insn-007fdce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdce4`](#insn-007fdce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdcf0`](#insn-007fdcf0) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`007fdcfc`](#insn-007fdcfc) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`007fdd04`](#insn-007fdd04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdd08`](#insn-007fdd08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdd0c`](#insn-007fdd0c) → [`008b9134`](../008b9/008b9134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9134` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fdcd4`](#insn-007fdcd4)

~~~json
{
  "source": "007fdcd4",
  "target": "007fdd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdcdc`](#insn-007fdcdc)

~~~json
{
  "source": "007fdcdc",
  "target": "007fdd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdce0`](#insn-007fdce0)

~~~json
{
  "source": "007fdce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdce4`](#insn-007fdce4)

~~~json
{
  "source": "007fdce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdcf0`](#insn-007fdcf0)

~~~json
{
  "source": "007fdcf0",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdcfc`](#insn-007fdcfc)

~~~json
{
  "source": "007fdcfc",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdd04`](#insn-007fdd04)

~~~json
{
  "source": "007fdd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdd08`](#insn-007fdd08)

~~~json
{
  "source": "007fdd08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdd0c`](#insn-007fdd0c)

~~~json
{
  "source": "007fdd0c",
  "target": "008b9134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
