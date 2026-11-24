# 007fcdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007fcd54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fcd54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0042.md#compare-1cc40ed378dc97cb0bcdcc2d2611a320)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `007fdd10`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007fd/007fdd10.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0042.md#compare-39dc7809d02dffef817b2525f2316763)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fcdac",
  "name": "FUN_007fcdac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a45293e678cfde40b16028c351e3e152c36c30b13c02327b90401b607c7efa3",
  "source_text_sha256": "2a45293e678cfde40b16028c351e3e152c36c30b13c02327b90401b607c7efa3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fcdac",
        "007fcdf3"
      ]
    ],
    "bytes_sha256": "1752d762e107d88182fe9819fd0798b2543e0c81e0869eab2d34c10bef5cd7c1",
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

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b91d0](../008b9/008b91d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 310 bytes

~~~c

void FUN_007fcdac(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar2 = *param_2;
    uVar1 = FUN_0047ad34();
    FUN_0047ce14(uVar1,0xb,0);
    FUN_008b91d0(uVar2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fcdac"></a> `007fcdac` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007fcdb0"></a> `007fcdb0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007fcdb4"></a> `007fcdb4` | `e1 01 00 54` | b.ne 0x007fcdf0 | `CONDITIONAL_JUMP`
<a id="insn-007fcdb8"></a> `007fcdb8` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fcdbc"></a> `007fcdbc` | `a8 01 00 35` | cbnz w8,0x007fcdf0 | `CONDITIONAL_JUMP`
<a id="insn-007fcdc0"></a> `007fcdc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fcdc4"></a> `007fcdc4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcdc8"></a> `007fcdc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fcdcc"></a> `007fcdcc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fcdd0"></a> `007fcdd0` | `d9 f7 f1 97` | bl 0x0047ad34 | `UNCONDITIONAL_CALL`
<a id="insn-007fcdd4"></a> `007fcdd4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fcdd8"></a> `007fcdd8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fcddc"></a> `007fcddc` | `0e 00 f2 97` | bl 0x0047ce14 | `UNCONDITIONAL_CALL`
<a id="insn-007fcde0"></a> `007fcde0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fcde4"></a> `007fcde4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fcde8"></a> `007fcde8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fcdec"></a> `007fcdec` | `f9 f0 02 14` | b 0x008b91d0 | `CALL_TERMINATOR`
<a id="insn-007fcdf0"></a> `007fcdf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fcdac`](#insn-007fcdac) 範囲 `[['007fcdac', '007fcdb7']]`
  - `CONDITIONAL_JUMP` [`007fcdb4`](#insn-007fcdb4) → [`007fcdf0`](#insn-007fcdf0)
  - `FALL_THROUGH` [`007fcdb4`](#insn-007fcdb4) → [`007fcdb8`](#insn-007fcdb8)
- ブロック [`007fcdb8`](#insn-007fcdb8) 範囲 `[['007fcdb8', '007fcdbf']]`
  - `CONDITIONAL_JUMP` [`007fcdbc`](#insn-007fcdbc) → [`007fcdf0`](#insn-007fcdf0)
  - `FALL_THROUGH` [`007fcdbc`](#insn-007fcdbc) → [`007fcdc0`](#insn-007fcdc0)
- ブロック [`007fcdc0`](#insn-007fcdc0) 範囲 `[['007fcdc0', '007fcdef']]`
- ブロック [`007fcdf0`](#insn-007fcdf0) 範囲 `[['007fcdf0', '007fcdf3']]`

## 命令位置別の参照

- [`007fcdb4`](#insn-007fcdb4) → [`007fcdf0`](#insn-007fcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcdbc`](#insn-007fcdbc) → [`007fcdf0`](#insn-007fcdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcdc0`](#insn-007fcdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcdc4`](#insn-007fcdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcdd0`](#insn-007fcdd0) → [`0047ad34`](../0047a/0047ad34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ad34` · 推定シンボル `None` · 推定型 `None`
- [`007fcddc`](#insn-007fcddc) → [`0047ce14`](../0047c/0047ce14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ce14` · 推定シンボル `None` · 推定型 `None`
- [`007fcde4`](#insn-007fcde4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcde8`](#insn-007fcde8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fcdec`](#insn-007fcdec) → [`008b91d0`](../008b9/008b91d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b91d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fcdb4`](#insn-007fcdb4)

~~~json
{
  "source": "007fcdb4",
  "target": "007fcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcdbc`](#insn-007fcdbc)

~~~json
{
  "source": "007fcdbc",
  "target": "007fcdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcdc0`](#insn-007fcdc0)

~~~json
{
  "source": "007fcdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcdc4`](#insn-007fcdc4)

~~~json
{
  "source": "007fcdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcdd0`](#insn-007fcdd0)

~~~json
{
  "source": "007fcdd0",
  "target": "0047ad34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcddc`](#insn-007fcddc)

~~~json
{
  "source": "007fcddc",
  "target": "0047ce14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcde4`](#insn-007fcde4)

~~~json
{
  "source": "007fcde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcde8`](#insn-007fcde8)

~~~json
{
  "source": "007fcde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fcdec`](#insn-007fcdec)

~~~json
{
  "source": "007fcdec",
  "target": "008b91d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
