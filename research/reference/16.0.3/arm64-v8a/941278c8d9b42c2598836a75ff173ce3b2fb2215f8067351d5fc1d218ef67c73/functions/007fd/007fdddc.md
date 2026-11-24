# 007fdddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fce78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fce78.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0042.md#compare-3dfa2f6de2acfeaef2485a3b2fd67428)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fdddc",
  "name": "FUN_007fdddc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7fed0d5bb22ff303c7a57dca9b8ee4610d7c696592b1a6a67e0855cc24508186",
  "source_text_sha256": "7fed0d5bb22ff303c7a57dca9b8ee4610d7c696592b1a6a67e0855cc24508186",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fdddc",
        "007fde23"
      ]
    ],
    "bytes_sha256": "22b711e15a83e2c36e752574f12742f3bb7d625043e7b852421b9f679f7d8515",
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

- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 310 bytes

~~~c

void FUN_007fdddc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if ((*param_3 == 2) && (*param_4 == 0)) {
    uVar2 = *param_2;
    uVar1 = FUN_0047b054();
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
<a id="insn-007fdddc"></a> `007fdddc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-007fdde0"></a> `007fdde0` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-007fdde4"></a> `007fdde4` | `e1 01 00 54` | b.ne 0x007fde20 | `CONDITIONAL_JUMP`
<a id="insn-007fdde8"></a> `007fdde8` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fddec"></a> `007fddec` | `a8 01 00 35` | cbnz w8,0x007fde20 | `CONDITIONAL_JUMP`
<a id="insn-007fddf0"></a> `007fddf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fddf4"></a> `007fddf4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fddf8"></a> `007fddf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fddfc"></a> `007fddfc` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fde00"></a> `007fde00` | `95 f4 f1 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-007fde04"></a> `007fde04` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fde08"></a> `007fde08` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fde0c"></a> `007fde0c` | `ca fc f1 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-007fde10"></a> `007fde10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fde14"></a> `007fde14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fde18"></a> `007fde18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fde1c"></a> `007fde1c` | `d8 f0 02 14` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-007fde20"></a> `007fde20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fdddc`](#insn-007fdddc) 範囲 `[['007fdddc', '007fdde7']]`
  - `CONDITIONAL_JUMP` [`007fdde4`](#insn-007fdde4) → [`007fde20`](#insn-007fde20)
  - `FALL_THROUGH` [`007fdde4`](#insn-007fdde4) → [`007fdde8`](#insn-007fdde8)
- ブロック [`007fdde8`](#insn-007fdde8) 範囲 `[['007fdde8', '007fddef']]`
  - `CONDITIONAL_JUMP` [`007fddec`](#insn-007fddec) → [`007fde20`](#insn-007fde20)
  - `FALL_THROUGH` [`007fddec`](#insn-007fddec) → [`007fddf0`](#insn-007fddf0)
- ブロック [`007fddf0`](#insn-007fddf0) 範囲 `[['007fddf0', '007fde1f']]`
- ブロック [`007fde20`](#insn-007fde20) 範囲 `[['007fde20', '007fde23']]`

## 命令位置別の参照

- [`007fdde4`](#insn-007fdde4) → [`007fde20`](#insn-007fde20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fddec`](#insn-007fddec) → [`007fde20`](#insn-007fde20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fddf0`](#insn-007fddf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fddf4`](#insn-007fddf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fde00`](#insn-007fde00) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`007fde0c`](#insn-007fde0c) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`007fde14`](#insn-007fde14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fde18`](#insn-007fde18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fde1c`](#insn-007fde1c) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fdde4`](#insn-007fdde4)

~~~json
{
  "source": "007fdde4",
  "target": "007fde20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fddec`](#insn-007fddec)

~~~json
{
  "source": "007fddec",
  "target": "007fde20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fddf0`](#insn-007fddf0)

~~~json
{
  "source": "007fddf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fddf4`](#insn-007fddf4)

~~~json
{
  "source": "007fddf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fde00`](#insn-007fde00)

~~~json
{
  "source": "007fde00",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fde0c`](#insn-007fde0c)

~~~json
{
  "source": "007fde0c",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fde14`](#insn-007fde14)

~~~json
{
  "source": "007fde14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fde18`](#insn-007fde18)

~~~json
{
  "source": "007fde18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fde1c`](#insn-007fde1c)

~~~json
{
  "source": "007fde1c",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
