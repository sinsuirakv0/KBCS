# 007fceec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `007fceac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fc/007fceac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-f02afaafc676724848456c153559ced8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fcf44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcf44.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-5144fa25c0f2cbf2a5efbaf33c0532a3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fceec",
  "name": "FUN_007fceec",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98929e462ee168ecbee88f9f0c263baeec3d2ba4dfcb743c32affb13f0d1ddc5",
  "source_text_sha256": "98929e462ee168ecbee88f9f0c263baeec3d2ba4dfcb743c32affb13f0d1ddc5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fceec",
        "007fcf57"
      ]
    ],
    "bytes_sha256": "7b219e3577992e102d5b0f9885b444ebcdfea8142308f3c8595bb3348e55e83c",
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

void FUN_007fceec(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

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
<a id="insn-007fceec"></a> `007fceec` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-007fcef0"></a> `007fcef0` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fcef4"></a> `007fcef4` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-007fcef8"></a> `007fcef8` | `e1 01 00 54` | b.ne 0x007fcf34 | `CONDITIONAL_JUMP`
<a id="insn-007fcefc"></a> `007fcefc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-007fcf00"></a> `007fcf00` | `a8 02 00 54` | b.hi 0x007fcf54 | `CONDITIONAL_JUMP`
<a id="insn-007fcf04"></a> `007fcf04` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fcf08"></a> `007fcf08` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcf0c"></a> `007fcf0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fcf10"></a> `007fcf10` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fcf14"></a> `007fcf14` | `78 f7 f1 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-007fcf18"></a> `007fcf18` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fcf1c"></a> `007fcf1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fcf20"></a> `007fcf20` | `ad ff f1 97` | bl 0x0047cdd4 | `UNCONDITIONAL_CALL`
<a id="insn-007fcf24"></a> `007fcf24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fcf28"></a> `007fcf28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcf2c"></a> `007fcf2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fcf30"></a> `007fcf30` | `92 f0 02 14` | b 0x008b9178 | `CALL_TERMINATOR`
<a id="insn-007fcf34"></a> `007fcf34` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-007fcf38"></a> `007fcf38` | `e1 00 00 54` | b.ne 0x007fcf54 | `CONDITIONAL_JUMP`
<a id="insn-007fcf3c"></a> `007fcf3c` | `c8 00 00 35` | cbnz w8,0x007fcf54 | `CONDITIONAL_JUMP`
<a id="insn-007fcf40"></a> `007fcf40` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fcf44"></a> `007fcf44` | `01 10 40 b9` | ldr w1,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-007fcf48"></a> `007fcf48` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-007fcf4c"></a> `007fcf4c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007fcf50"></a> `007fcf50` | `56 cb ff 17` | b 0x007efca8 | `CALL_TERMINATOR`
<a id="insn-007fcf54"></a> `007fcf54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fceec`](#insn-007fceec) 範囲 `[['007fceec', '007fcefb']]`
  - `CONDITIONAL_JUMP` [`007fcef8`](#insn-007fcef8) → [`007fcf34`](#insn-007fcf34)
  - `FALL_THROUGH` [`007fcef8`](#insn-007fcef8) → [`007fcefc`](#insn-007fcefc)
- ブロック [`007fcefc`](#insn-007fcefc) 範囲 `[['007fcefc', '007fcf03']]`
  - `CONDITIONAL_JUMP` [`007fcf00`](#insn-007fcf00) → [`007fcf54`](#insn-007fcf54)
  - `FALL_THROUGH` [`007fcf00`](#insn-007fcf00) → [`007fcf04`](#insn-007fcf04)
- ブロック [`007fcf04`](#insn-007fcf04) 範囲 `[['007fcf04', '007fcf33']]`
- ブロック [`007fcf34`](#insn-007fcf34) 範囲 `[['007fcf34', '007fcf3b']]`
  - `CONDITIONAL_JUMP` [`007fcf38`](#insn-007fcf38) → [`007fcf54`](#insn-007fcf54)
  - `FALL_THROUGH` [`007fcf38`](#insn-007fcf38) → [`007fcf3c`](#insn-007fcf3c)
- ブロック [`007fcf3c`](#insn-007fcf3c) 範囲 `[['007fcf3c', '007fcf3f']]`
  - `CONDITIONAL_JUMP` [`007fcf3c`](#insn-007fcf3c) → [`007fcf54`](#insn-007fcf54)
  - `FALL_THROUGH` [`007fcf3c`](#insn-007fcf3c) → [`007fcf40`](#insn-007fcf40)
- ブロック [`007fcf40`](#insn-007fcf40) 範囲 `[['007fcf40', '007fcf53']]`
- ブロック [`007fcf54`](#insn-007fcf54) 範囲 `[['007fcf54', '007fcf57']]`

## 命令位置別の参照

- [`007fcef8`](#insn-007fcef8) → [`007fcf34`](#insn-007fcf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf00`](#insn-007fcf00) → [`007fcf54`](#insn-007fcf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf04`](#insn-007fcf04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf08`](#insn-007fcf08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf14`](#insn-007fcf14) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`007fcf20`](#insn-007fcf20) → [`0047cdd4`](../0047c/0047cdd4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cdd4` · 推定シンボル `None` · 推定型 `None`
- [`007fcf28`](#insn-007fcf28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf2c`](#insn-007fcf2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf30`](#insn-007fcf30) → [`008b9178`](../008b9/008b9178.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9178` · 推定シンボル `None` · 推定型 `None`
- [`007fcf38`](#insn-007fcf38) → [`007fcf54`](#insn-007fcf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf3c`](#insn-007fcf3c) → [`007fcf54`](#insn-007fcf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcf50`](#insn-007fcf50) → [`007efca8`](../007ef/007efca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007efca8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fcef8`](#insn-007fcef8)

~~~json
{
  "source": "007fcef8",
  "target": "007fcf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf00`](#insn-007fcf00)

~~~json
{
  "source": "007fcf00",
  "target": "007fcf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf04`](#insn-007fcf04)

~~~json
{
  "source": "007fcf04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf08`](#insn-007fcf08)

~~~json
{
  "source": "007fcf08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf14`](#insn-007fcf14)

~~~json
{
  "source": "007fcf14",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcf20`](#insn-007fcf20)

~~~json
{
  "source": "007fcf20",
  "target": "0047cdd4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcf28`](#insn-007fcf28)

~~~json
{
  "source": "007fcf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf2c`](#insn-007fcf2c)

~~~json
{
  "source": "007fcf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf30`](#insn-007fcf30)

~~~json
{
  "source": "007fcf30",
  "target": "008b9178",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcf38`](#insn-007fcf38)

~~~json
{
  "source": "007fcf38",
  "target": "007fcf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf3c`](#insn-007fcf3c)

~~~json
{
  "source": "007fcf3c",
  "target": "007fcf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcf50`](#insn-007fcf50)

~~~json
{
  "source": "007fcf50",
  "target": "007efca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
