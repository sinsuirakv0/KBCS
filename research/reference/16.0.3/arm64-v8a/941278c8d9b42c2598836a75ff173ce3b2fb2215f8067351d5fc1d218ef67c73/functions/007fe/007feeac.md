# 007feeac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fdf48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fdf48.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0043.md#compare-b1fab4775352f7e99bfbc667c1c43f13)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007feeac",
  "name": "FUN_007feeac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df34f5d91230c4c6444ed437c0f05c0eca73bdf2fffaacf4e2b7e28682184053",
  "source_text_sha256": "df34f5d91230c4c6444ed437c0f05c0eca73bdf2fffaacf4e2b7e28682184053",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007feeac",
        "007feeeb"
      ]
    ],
    "bytes_sha256": "8da21db7bd8da4ccfb6ada71744fabd19e7cb338c209c3d1d6c996afdd4ef0c3",
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

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 470 bytes

~~~c

void FUN_007feeac(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
                    /* try { // try from 007feec0 to 008feed3 has its CatchHandler @ 007ff05c */
    uVar2 = *param_2;
    uVar1 = FUN_0047b054();
                    /* try { // try from 007feed4 to 008feee3 has its CatchHandler @ 007ff048 */
    FUN_0047d134(uVar1,0xb,0);
    FUN_008ba17c(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007feeac"></a> `007feeac` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007feeb0"></a> `007feeb0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007feeb4"></a> `007feeb4` | `a1 01 00 54` | b.ne 0x007feee8 | `CONDITIONAL_JUMP`
<a id="insn-007feeb8"></a> `007feeb8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007feebc"></a> `007feebc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007feec0"></a> `007feec0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007feec4"></a> `007feec4` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007feec8"></a> `007feec8` | `63 f0 f1 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-007feecc"></a> `007feecc` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007feed0"></a> `007feed0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007feed4"></a> `007feed4` | `98 f8 f1 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-007feed8"></a> `007feed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007feedc"></a> `007feedc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007feee0"></a> `007feee0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007feee4"></a> `007feee4` | `a6 ec 02 14` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-007feee8"></a> `007feee8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007feeac`](#insn-007feeac) 範囲 `[['007feeac', '007feeb7']]`
  - `CONDITIONAL_JUMP` [`007feeb4`](#insn-007feeb4) → [`007feee8`](#insn-007feee8)
  - `FALL_THROUGH` [`007feeb4`](#insn-007feeb4) → [`007feeb8`](#insn-007feeb8)
- ブロック [`007feeb8`](#insn-007feeb8) 範囲 `[['007feeb8', '007feebf']]`
  - `FALL_THROUGH` [`007feebc`](#insn-007feebc) → [`007feec0`](#insn-007feec0)
- ブロック [`007feec0`](#insn-007feec0) 範囲 `[['007feec0', '007feed3']]`
  - `FALL_THROUGH` [`007feed0`](#insn-007feed0) → [`007feed4`](#insn-007feed4)
- ブロック [`007feed4`](#insn-007feed4) 範囲 `[['007feed4', '007feee7']]`
- ブロック [`007feee8`](#insn-007feee8) 範囲 `[['007feee8', '007feeeb']]`

## 命令位置別の参照

- [`007feeb4`](#insn-007feeb4) → [`007feee8`](#insn-007feee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feeb8`](#insn-007feeb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feebc`](#insn-007feebc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feec8`](#insn-007feec8) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`007feed4`](#insn-007feed4) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`007feedc`](#insn-007feedc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feee0`](#insn-007feee0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007feee4`](#insn-007feee4) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007feeb4`](#insn-007feeb4)

~~~json
{
  "source": "007feeb4",
  "target": "007feee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feeb8`](#insn-007feeb8)

~~~json
{
  "source": "007feeb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feebc`](#insn-007feebc)

~~~json
{
  "source": "007feebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feec8`](#insn-007feec8)

~~~json
{
  "source": "007feec8",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007feed4`](#insn-007feed4)

~~~json
{
  "source": "007feed4",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007feedc`](#insn-007feedc)

~~~json
{
  "source": "007feedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feee0`](#insn-007feee0)

~~~json
{
  "source": "007feee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007feee4`](#insn-007feee4)

~~~json
{
  "source": "007feee4",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
