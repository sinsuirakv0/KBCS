# 007fcfdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fcf9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fcf9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-cf83274dd6522ede69d6cca498e5b84e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fd034`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fd/007fd034.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-fb2723544eb4e5dda9e4c49feef7a523)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fcfdc",
  "name": "FUN_007fcfdc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a109c46f4c557aa0e4e98bc4669cd1080940389109232a1c9dc24c919c1a8e42",
  "source_text_sha256": "a109c46f4c557aa0e4e98bc4669cd1080940389109232a1c9dc24c919c1a8e42",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fcfdc",
        "007fd047"
      ]
    ],
    "bytes_sha256": "57de4733c077a792dd00b3623a472e1a2cdfe576d0fb7305cbf770d173acc428",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [007efca8](../007ef/007efca8.md)
- [008b9178](../008b9/008b9178.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 471 bytes

~~~c

void FUN_007fcfdc(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    if (*param_4 < 2) {
      uVar2 = *param_2;
      uVar1 = FUN_0047acf4();
      FUN_0047cdd4(uVar1,0xb,0);
      FUN_008b9178(uVar2);
      return;
    }
  }
  else if ((*param_3 == 5) && (*param_4 == 0)) {
    FUN_007efca8(*(undefined8 *)(param_1 + 8),*(undefined4 *)(param_1 + 0x10),0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fcfdc"></a> `007fcfdc` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-007fcfe0"></a> `007fcfe0` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fcfe4"></a> `007fcfe4` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-007fcfe8"></a> `007fcfe8` | `e1 01 00 54` | b.ne 0x007fd024 | `CONDITIONAL_JUMP`
<a id="insn-007fcfec"></a> `007fcfec` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-007fcff0"></a> `007fcff0` | `a8 02 00 54` | b.hi 0x007fd044 | `CONDITIONAL_JUMP`
<a id="insn-007fcff4"></a> `007fcff4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fcff8"></a> `007fcff8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcffc"></a> `007fcffc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fd000"></a> `007fd000` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fd004"></a> `007fd004` | `3c f7 f1 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-007fd008"></a> `007fd008` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fd00c"></a> `007fd00c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fd010"></a> `007fd010` | `71 ff f1 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-007fd014"></a> `007fd014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fd018"></a> `007fd018` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fd01c"></a> `007fd01c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fd020"></a> `007fd020` | `56 f0 02 14` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-007fd024"></a> `007fd024` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-007fd028"></a> `007fd028` | `e1 00 00 54` | b.ne 0x007fd044 | `CONDITIONAL_JUMP`
<a id="insn-007fd02c"></a> `007fd02c` | `c8 00 00 35` | cbnz w8,0x007fd044 | `CONDITIONAL_JUMP`
<a id="insn-007fd030"></a> `007fd030` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fd034"></a> `007fd034` | `01 10 40 b9` | ldr w1,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007fd038"></a> `007fd038` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-007fd03c"></a> `007fd03c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007fd040"></a> `007fd040` | `1a cb ff 17` | b 0x007efca8 | `CALL_TERMINATOR`
<a id="insn-007fd044"></a> `007fd044` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fcfdc`](#insn-007fcfdc) 範囲 `[['007fcfdc', '007fcfeb']]`
  - `CONDITIONAL_JUMP` [`007fcfe8`](#insn-007fcfe8) → [`007fd024`](#insn-007fd024)
  - `FALL_THROUGH` [`007fcfe8`](#insn-007fcfe8) → [`007fcfec`](#insn-007fcfec)
- ブロック [`007fcfec`](#insn-007fcfec) 範囲 `[['007fcfec', '007fcff3']]`
  - `CONDITIONAL_JUMP` [`007fcff0`](#insn-007fcff0) → [`007fd044`](#insn-007fd044)
  - `FALL_THROUGH` [`007fcff0`](#insn-007fcff0) → [`007fcff4`](#insn-007fcff4)
- ブロック [`007fcff4`](#insn-007fcff4) 範囲 `[['007fcff4', '007fd023']]`
- ブロック [`007fd024`](#insn-007fd024) 範囲 `[['007fd024', '007fd02b']]`
  - `CONDITIONAL_JUMP` [`007fd028`](#insn-007fd028) → [`007fd044`](#insn-007fd044)
  - `FALL_THROUGH` [`007fd028`](#insn-007fd028) → [`007fd02c`](#insn-007fd02c)
- ブロック [`007fd02c`](#insn-007fd02c) 範囲 `[['007fd02c', '007fd02f']]`
  - `CONDITIONAL_JUMP` [`007fd02c`](#insn-007fd02c) → [`007fd044`](#insn-007fd044)
  - `FALL_THROUGH` [`007fd02c`](#insn-007fd02c) → [`007fd030`](#insn-007fd030)
- ブロック [`007fd030`](#insn-007fd030) 範囲 `[['007fd030', '007fd043']]`
- ブロック [`007fd044`](#insn-007fd044) 範囲 `[['007fd044', '007fd047']]`

## 命令位置別の参照

- [`007fcfe8`](#insn-007fcfe8) → [`007fd024`](#insn-007fd024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcff0`](#insn-007fcff0) → [`007fd044`](#insn-007fd044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcff4`](#insn-007fcff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcff8`](#insn-007fcff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fd004`](#insn-007fd004) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`007fd010`](#insn-007fd010) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`007fd018`](#insn-007fd018) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fd01c`](#insn-007fd01c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fd020`](#insn-007fd020) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`
- [`007fd028`](#insn-007fd028) → [`007fd044`](#insn-007fd044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fd02c`](#insn-007fd02c) → [`007fd044`](#insn-007fd044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fd040`](#insn-007fd040) → [`007efca8`](../007ef/007efca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007efca8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fcfe8`](#insn-007fcfe8)

~~~json
{
  "source": "007fcfe8",
  "target": "007fd024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcff0`](#insn-007fcff0)

~~~json
{
  "source": "007fcff0",
  "target": "007fd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcff4`](#insn-007fcff4)

~~~json
{
  "source": "007fcff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcff8`](#insn-007fcff8)

~~~json
{
  "source": "007fcff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fd004`](#insn-007fd004)

~~~json
{
  "source": "007fd004",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fd010`](#insn-007fd010)

~~~json
{
  "source": "007fd010",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fd018`](#insn-007fd018)

~~~json
{
  "source": "007fd018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fd01c`](#insn-007fd01c)

~~~json
{
  "source": "007fd01c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fd020`](#insn-007fd020)

~~~json
{
  "source": "007fd020",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fd028`](#insn-007fd028)

~~~json
{
  "source": "007fd028",
  "target": "007fd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fd02c`](#insn-007fd02c)

~~~json
{
  "source": "007fd02c",
  "target": "007fd044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fd040`](#insn-007fd040)

~~~json
{
  "source": "007fd040",
  "target": "007efca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
