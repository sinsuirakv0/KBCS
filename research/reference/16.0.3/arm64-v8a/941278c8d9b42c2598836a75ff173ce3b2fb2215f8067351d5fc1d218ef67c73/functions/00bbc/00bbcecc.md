# 00bbcecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbbed8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-715d3e632be226da886cee46f8c6e51a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcecc",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8b13a43e87a17ffff4af9f4090a472f3d8cc91a6c10f23c44a412fa9ba7bc68",
  "source_text_sha256": "d8b13a43e87a17ffff4af9f4090a472f3d8cc91a6c10f23c44a412fa9ba7bc68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcecc",
        "00bbcf73"
      ]
    ],
    "bytes_sha256": "3cdf1e43b27e1f406ebcaf37d23497cee2698731e8e4c9dd06cd183452803802",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bdf0](../00c5b/00c5bdf0.md)
- [00c5beb0](../00c5b/00c5beb0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 976 bytes

~~~c

void _ZN8firebase9messaging21UnsubscribeLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
                    /* try { // try from 00bbced0 to 00cbcf5f has its CatchHandler @ 00bbc990 */
  if (DAT_01127420 == 0) {
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbcf60 to 00cbcf83 has its CatchHandler @ 00bbd800 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x80);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbcecc"></a> `00bbcecc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbced0"></a> `00bbced0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbced4"></a> `00bbced4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbced8"></a> `00bbced8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbcedc"></a> `00bbcedc` | `49 2b 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bbcee0"></a> `00bbcee0` | `29 11 42 f9` | ldr x9,[x9, #0x420] | `FALL_THROUGH`
<a id="insn-00bbcee4"></a> `00bbcee4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbcee8"></a> `00bbcee8` | `89 02 00 b4` | cbz x9,0x00bbcf38 | `CONDITIONAL_JUMP`
<a id="insn-00bbceec"></a> `00bbceec` | `09 85 02 94` | bl 0x00c5e310 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcef0"></a> `00bbcef0` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbcef4"></a> `00bbcef4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbcef8"></a> `00bbcef8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcefc"></a> `00bbcefc` | `e9 7a 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf00"></a> `00bbcf00` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcf04"></a> `00bbcf04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcf08"></a> `00bbcf08` | `ea 7a 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf0c"></a> `00bbcf0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcf10"></a> `00bbcf10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcf14"></a> `00bbcf14` | `7f 7b 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf18"></a> `00bbcf18` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcf1c"></a> `00bbcf1c` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcf20"></a> `00bbcf20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbcf24"></a> `00bbcf24` | `e3 7b 02 94` | bl 0x00c5beb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf28"></a> `00bbcf28` | `c1 02 02 91` | add x1,x22,#0x80 | `FALL_THROUGH`
<a id="insn-00bbcf2c"></a> `00bbcf2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcf30"></a> `00bbcf30` | `b0 7b 02 94` | bl 0x00c5bdf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf34"></a> `00bbcf34` | `0c 00 00 14` | b 0x00bbcf64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcf38"></a> `00bbcf38` | `20 b7 ff d0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbcf3c"></a> `00bbcf3c` | `00 4c 26 91` | add x0,x0,#0x993 | `FALL_THROUGH`
<a id="insn-00bbcf40"></a> `00bbcf40` | `58 7c 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf44"></a> `00bbcf44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcf48"></a> `00bbcf48` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbcf4c"></a> `00bbcf4c` | `71 7b 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf50"></a> `00bbcf50` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcf54"></a> `00bbcf54` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcf58"></a> `00bbcf58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbcf5c"></a> `00bbcf5c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbcf60"></a> `00bbcf60` | `48 7b 02 94` | bl 0x00c5bc80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcf64"></a> `00bbcf64` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcf68"></a> `00bbcf68` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcf6c"></a> `00bbcf6c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbcf70"></a> `00bbcf70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcecc`](#insn-00bbcecc) 範囲 `[['00bbcecc', '00bbcecf']]`
  - `FALL_THROUGH` [`00bbcecc`](#insn-00bbcecc) → [`00bbced0`](#insn-00bbced0)
- ブロック [`00bbced0`](#insn-00bbced0) 範囲 `[['00bbced0', '00bbceeb']]`
  - `CONDITIONAL_JUMP` [`00bbcee8`](#insn-00bbcee8) → [`00bbcf38`](#insn-00bbcf38)
  - `FALL_THROUGH` [`00bbcee8`](#insn-00bbcee8) → [`00bbceec`](#insn-00bbceec)
- ブロック [`00bbceec`](#insn-00bbceec) 範囲 `[['00bbceec', '00bbcf37']]`
  - `UNCONDITIONAL_JUMP` [`00bbcf34`](#insn-00bbcf34) → [`00bbcf64`](#insn-00bbcf64)
- ブロック [`00bbcf38`](#insn-00bbcf38) 範囲 `[['00bbcf38', '00bbcf5f']]`
  - `FALL_THROUGH` [`00bbcf5c`](#insn-00bbcf5c) → [`00bbcf60`](#insn-00bbcf60)
- ブロック [`00bbcf60`](#insn-00bbcf60) 範囲 `[['00bbcf60', '00bbcf63']]`
  - `FALL_THROUGH` [`00bbcf60`](#insn-00bbcf60) → [`00bbcf64`](#insn-00bbcf64)
- ブロック [`00bbcf64`](#insn-00bbcf64) 範囲 `[['00bbcf64', '00bbcf73']]`

## 命令位置別の参照

- [`00bbcecc`](#insn-00bbcecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbced0`](#insn-00bbced0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbced4`](#insn-00bbced4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcee0`](#insn-00bbcee0) → `01127420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbcee8`](#insn-00bbcee8) → [`00bbcf38`](#insn-00bbcf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbceec`](#insn-00bbceec) → [`00c5e310`](../00c5e/00c5e310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e310` · 推定シンボル `None` · 推定型 `None`
- [`00bbcefc`](#insn-00bbcefc) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf08`](#insn-00bbcf08) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf14`](#insn-00bbcf14) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf24`](#insn-00bbcf24) → [`00c5beb0`](../00c5b/00c5beb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5beb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf30`](#insn-00bbcf30) → [`00c5bdf0`](../00c5b/00c5bdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdf0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf34`](#insn-00bbcf34) → [`00bbcf64`](#insn-00bbcf64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf3c`](#insn-00bbcf3c) → `002a2993`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcf40`](#insn-00bbcf40) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf4c`](#insn-00bbcf4c) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf60`](#insn-00bbcf60) → [`00c5bc80`](../00c5b/00c5bc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc80` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf64`](#insn-00bbcf64) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcf68`](#insn-00bbcf68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcecc`](#insn-00bbcecc)

~~~json
{
  "source": "00bbcecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbced0`](#insn-00bbced0)

~~~json
{
  "source": "00bbced0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbced4`](#insn-00bbced4)

~~~json
{
  "source": "00bbced4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcee0`](#insn-00bbcee0)

~~~json
{
  "source": "00bbcee0",
  "target": "01127420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127420",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbcee8`](#insn-00bbcee8)

~~~json
{
  "source": "00bbcee8",
  "target": "00bbcf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbceec`](#insn-00bbceec)

~~~json
{
  "source": "00bbceec",
  "target": "00c5e310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcefc`](#insn-00bbcefc)

~~~json
{
  "source": "00bbcefc",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf08`](#insn-00bbcf08)

~~~json
{
  "source": "00bbcf08",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf14`](#insn-00bbcf14)

~~~json
{
  "source": "00bbcf14",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf24`](#insn-00bbcf24)

~~~json
{
  "source": "00bbcf24",
  "target": "00c5beb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf30`](#insn-00bbcf30)

~~~json
{
  "source": "00bbcf30",
  "target": "00c5bdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf34`](#insn-00bbcf34)

~~~json
{
  "source": "00bbcf34",
  "target": "00bbcf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf3c`](#insn-00bbcf3c)

~~~json
{
  "source": "00bbcf3c",
  "target": "002a2993",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2993",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2993",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcf40`](#insn-00bbcf40)

~~~json
{
  "source": "00bbcf40",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf4c`](#insn-00bbcf4c)

~~~json
{
  "source": "00bbcf4c",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf60`](#insn-00bbcf60)

~~~json
{
  "source": "00bbcf60",
  "target": "00c5bc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcf64`](#insn-00bbcf64)

~~~json
{
  "source": "00bbcf64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcf68`](#insn-00bbcf68)

~~~json
{
  "source": "00bbcf68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
