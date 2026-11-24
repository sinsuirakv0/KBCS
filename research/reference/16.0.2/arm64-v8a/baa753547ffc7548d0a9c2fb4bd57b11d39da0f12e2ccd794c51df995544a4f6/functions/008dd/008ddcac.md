# 008ddcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008ddc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008ddc58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0003.md#compare-f90e0498e996fd8fc5dad56508e3e37b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008dec58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008de/008dec58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0053.md#compare-552cdd07da8b5b5942cca338f664481e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008ddcac",
  "name": "FUN_008ddcac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598",
  "source_text_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008ddcac",
        "008ddd07"
      ]
    ],
    "bytes_sha256": "ecff9335e850dec033cc9ddb1da574ea89e1819b3a626f008f344887f8561104",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008ddff4](../008dd/008ddff4.md)

## 呼び出し先

- [008dc174](../008dc/008dc174.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 464 bytes

~~~c

void FUN_008ddcac(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
                    /* try { // try from 008ddcd8 to 009ddcdf has its CatchHandler @ 008de4a4 */
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dc174(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008ddcac"></a> `008ddcac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-008ddcb0"></a> `008ddcb0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ddcb4"></a> `008ddcb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ddcb8"></a> `008ddcb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-008ddcbc"></a> `008ddcbc` | `09 04 80 b9` | ldrsw x9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-008ddcc0"></a> `008ddcc0` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-008ddcc4"></a> `008ddcc4` | `0a 1c 40 f9` | ldr x10,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-008ddcc8"></a> `008ddcc8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-008ddccc"></a> `008ddccc` | `28 29 28 9b` | smaddl x8,w9,w8,x10 | `FALL_THROUGH`
<a id="insn-008ddcd0"></a> `008ddcd0` | `14 55 40 a9` | ldp x20,x21,[x8] | `FALL_THROUGH`
<a id="insn-008ddcd4"></a> `008ddcd4` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-008ddcd8"></a> `008ddcd8` | `00 01 00 54` | b.eq 0x008ddcf8 | `CONDITIONAL_JUMP`
<a id="insn-008ddcdc"></a> `008ddcdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008ddce0"></a> `008ddce0` | `88 46 80 b8` | ldrsw x8,[x20], #0x4 | `FALL_THROUGH`
<a id="insn-008ddce4"></a> `008ddce4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-008ddce8"></a> `008ddce8` | `20 21 08 8b` | add x0,x9,x8, LSL #0x8 | `FALL_THROUGH`
<a id="insn-008ddcec"></a> `008ddcec` | `22 f9 ff 97` | bl 0x008dc174 | `UNCONDITIONAL_CALL`
<a id="insn-008ddcf0"></a> `008ddcf0` | `9f 02 15 eb` | cmp x20,x21 | `FALL_THROUGH`
<a id="insn-008ddcf4"></a> `008ddcf4` | `61 ff ff 54` | b.ne 0x008ddce0 | `CONDITIONAL_JUMP`
<a id="insn-008ddcf8"></a> `008ddcf8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008ddcfc"></a> `008ddcfc` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008ddd00"></a> `008ddd00` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-008ddd04"></a> `008ddd04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008ddcac`](#insn-008ddcac) 範囲 `[['008ddcac', '008ddcd7']]`
  - `FALL_THROUGH` [`008ddcd4`](#insn-008ddcd4) → [`008ddcd8`](#insn-008ddcd8)
- ブロック [`008ddcd8`](#insn-008ddcd8) 範囲 `[['008ddcd8', '008ddcdb']]`
  - `CONDITIONAL_JUMP` [`008ddcd8`](#insn-008ddcd8) → [`008ddcf8`](#insn-008ddcf8)
  - `FALL_THROUGH` [`008ddcd8`](#insn-008ddcd8) → [`008ddcdc`](#insn-008ddcdc)
- ブロック [`008ddcdc`](#insn-008ddcdc) 範囲 `[['008ddcdc', '008ddcdf']]`
  - `FALL_THROUGH` [`008ddcdc`](#insn-008ddcdc) → [`008ddce0`](#insn-008ddce0)
- ブロック [`008ddce0`](#insn-008ddce0) 範囲 `[['008ddce0', '008ddcf7']]`
  - `CONDITIONAL_JUMP` [`008ddcf4`](#insn-008ddcf4) → [`008ddce0`](#insn-008ddce0)
  - `FALL_THROUGH` [`008ddcf4`](#insn-008ddcf4) → [`008ddcf8`](#insn-008ddcf8)
- ブロック [`008ddcf8`](#insn-008ddcf8) 範囲 `[['008ddcf8', '008ddd07']]`

## 命令位置別の参照

- [`008ddcac`](#insn-008ddcac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcb0`](#insn-008ddcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcb4`](#insn-008ddcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcd8`](#insn-008ddcd8) → [`008ddcf8`](#insn-008ddcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcec`](#insn-008ddcec) → [`008dc174`](../008dc/008dc174.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008dc174` · 推定シンボル `None` · 推定型 `None`
- [`008ddcf4`](#insn-008ddcf4) → [`008ddce0`](#insn-008ddce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcf8`](#insn-008ddcf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddcfc`](#insn-008ddcfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ddd00`](#insn-008ddd00) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008ddcac`](#insn-008ddcac)

~~~json
{
  "source": "008ddcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcb0`](#insn-008ddcb0)

~~~json
{
  "source": "008ddcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcb4`](#insn-008ddcb4)

~~~json
{
  "source": "008ddcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcd8`](#insn-008ddcd8)

~~~json
{
  "source": "008ddcd8",
  "target": "008ddcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcec`](#insn-008ddcec)

~~~json
{
  "source": "008ddcec",
  "target": "008dc174",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ddcf4`](#insn-008ddcf4)

~~~json
{
  "source": "008ddcf4",
  "target": "008ddce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcf8`](#insn-008ddcf8)

~~~json
{
  "source": "008ddcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddcfc`](#insn-008ddcfc)

~~~json
{
  "source": "008ddcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ddd00`](#insn-008ddd00)

~~~json
{
  "source": "008ddd00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
