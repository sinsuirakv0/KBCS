# 00bbbed8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbe3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-7ccb268ef4c03666833291ce30fc360a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbcecc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcecc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-715d3e632be226da886cee46f8c6e51a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbed8",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98d104f0860671496990d0c0691ba6f6d7eb71a33f7dc945089ebe985fc45cb8",
  "source_text_sha256": "98d104f0860671496990d0c0691ba6f6d7eb71a33f7dc945089ebe985fc45cb8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbed8",
        "00bbbf7f"
      ]
    ],
    "bytes_sha256": "73c47593d3d59b2d80e3f7d675231d902d5cbf9cec93683737428378ba681531",
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

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ae20](../00c5a/00c5ae20.md)
- [00c5aee0](../00c5a/00c5aee0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5d340](../00c5d/00c5d340.md)

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
  
                    /* try { // try from 00bbbedc to 00cbbf6b has its CatchHandler @ 00bbb99c */
  if (DAT_01126460 == 0) {
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbbf6c to 00cbbf8f has its CatchHandler @ 00bbc80c */
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
<a id="insn-00bbbed8"></a> `00bbbed8` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbbedc"></a> `00bbbedc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbee0"></a> `00bbbee0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbee4"></a> `00bbbee4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbbee8"></a> `00bbbee8` | `49 2b 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbeec"></a> `00bbbeec` | `29 31 42 f9` | ldr x9,[x9, #0x460] | `FALL_THROUGH`
<a id="insn-00bbbef0"></a> `00bbbef0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bbbef4"></a> `00bbbef4` | `89 02 00 b4` | cbz x9,0x00bbbf44 | `CONDITIONAL_JUMP`
<a id="insn-00bbbef8"></a> `00bbbef8` | `12 85 02 94` | bl 0x00c5d340 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbefc"></a> `00bbbefc` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbf00"></a> `00bbbf00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbbf04"></a> `00bbbf04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbf08"></a> `00bbbf08` | `f2 7a 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf0c"></a> `00bbbf0c` | `96 2a 40 f9` | ldr x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bbbf10"></a> `00bbbf10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbf14"></a> `00bbbf14` | `f3 7a 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf18"></a> `00bbbf18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbf1c"></a> `00bbbf1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbbf20"></a> `00bbbf20` | `88 7b 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf24"></a> `00bbbf24` | `74 c2 00 91` | add x20,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbf28"></a> `00bbbf28` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbf2c"></a> `00bbbf2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbf30"></a> `00bbbf30` | `ec 7b 02 94` | bl 0x00c5aee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf34"></a> `00bbbf34` | `c1 02 02 91` | add x1,x22,#0x80 | `FALL_THROUGH`
<a id="insn-00bbbf38"></a> `00bbbf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbf3c"></a> `00bbbf3c` | `b9 7b 02 94` | bl 0x00c5ae20 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf40"></a> `00bbbf40` | `0c 00 00 14` | b 0x00bbbf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbf44"></a> `00bbbf44` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbbf48"></a> `00bbbf48` | `00 20 23 91` | add x0,x0,#0x8c8 | `FALL_THROUGH`
<a id="insn-00bbbf4c"></a> `00bbbf4c` | `61 7c 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf50"></a> `00bbbf50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbbf54"></a> `00bbbf54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbbf58"></a> `00bbbf58` | `7a 7b 02 94` | bl 0x00c5ad40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf5c"></a> `00bbbf5c` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bbbf60"></a> `00bbbf60` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbf64"></a> `00bbbf64` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbbf68"></a> `00bbbf68` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbbf6c"></a> `00bbbf6c` | `51 7b 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbf70"></a> `00bbbf70` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbf74"></a> `00bbbf74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf78"></a> `00bbbf78` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbbf7c"></a> `00bbbf7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbed8`](#insn-00bbbed8) 範囲 `[['00bbbed8', '00bbbedb']]`
  - `FALL_THROUGH` [`00bbbed8`](#insn-00bbbed8) → [`00bbbedc`](#insn-00bbbedc)
- ブロック [`00bbbedc`](#insn-00bbbedc) 範囲 `[['00bbbedc', '00bbbef7']]`
  - `CONDITIONAL_JUMP` [`00bbbef4`](#insn-00bbbef4) → [`00bbbf44`](#insn-00bbbf44)
  - `FALL_THROUGH` [`00bbbef4`](#insn-00bbbef4) → [`00bbbef8`](#insn-00bbbef8)
- ブロック [`00bbbef8`](#insn-00bbbef8) 範囲 `[['00bbbef8', '00bbbf43']]`
  - `UNCONDITIONAL_JUMP` [`00bbbf40`](#insn-00bbbf40) → [`00bbbf70`](#insn-00bbbf70)
- ブロック [`00bbbf44`](#insn-00bbbf44) 範囲 `[['00bbbf44', '00bbbf6b']]`
  - `FALL_THROUGH` [`00bbbf68`](#insn-00bbbf68) → [`00bbbf6c`](#insn-00bbbf6c)
- ブロック [`00bbbf6c`](#insn-00bbbf6c) 範囲 `[['00bbbf6c', '00bbbf6f']]`
  - `FALL_THROUGH` [`00bbbf6c`](#insn-00bbbf6c) → [`00bbbf70`](#insn-00bbbf70)
- ブロック [`00bbbf70`](#insn-00bbbf70) 範囲 `[['00bbbf70', '00bbbf7f']]`

## 命令位置別の参照

- [`00bbbed8`](#insn-00bbbed8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbedc`](#insn-00bbbedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbee0`](#insn-00bbbee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbeec`](#insn-00bbbeec) → `01126460`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbef4`](#insn-00bbbef4) → [`00bbbf44`](#insn-00bbbf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbef8`](#insn-00bbbef8) → [`00c5d340`](../00c5d/00c5d340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d340` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf08`](#insn-00bbbf08) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf14`](#insn-00bbbf14) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf20`](#insn-00bbbf20) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf30`](#insn-00bbbf30) → [`00c5aee0`](../00c5a/00c5aee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aee0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf3c`](#insn-00bbbf3c) → [`00c5ae20`](../00c5a/00c5ae20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae20` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf40`](#insn-00bbbf40) → [`00bbbf70`](#insn-00bbbf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf48`](#insn-00bbbf48) → `002a28c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbbf4c`](#insn-00bbbf4c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf58`](#insn-00bbbf58) → [`00c5ad40`](../00c5a/00c5ad40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad40` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf6c`](#insn-00bbbf6c) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf70`](#insn-00bbbf70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf74`](#insn-00bbbf74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbed8`](#insn-00bbbed8)

~~~json
{
  "source": "00bbbed8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbedc`](#insn-00bbbedc)

~~~json
{
  "source": "00bbbedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbee0`](#insn-00bbbee0)

~~~json
{
  "source": "00bbbee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbeec`](#insn-00bbbeec)

~~~json
{
  "source": "00bbbeec",
  "target": "01126460",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126460",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbef4`](#insn-00bbbef4)

~~~json
{
  "source": "00bbbef4",
  "target": "00bbbf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbef8`](#insn-00bbbef8)

~~~json
{
  "source": "00bbbef8",
  "target": "00c5d340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf08`](#insn-00bbbf08)

~~~json
{
  "source": "00bbbf08",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf14`](#insn-00bbbf14)

~~~json
{
  "source": "00bbbf14",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf20`](#insn-00bbbf20)

~~~json
{
  "source": "00bbbf20",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf30`](#insn-00bbbf30)

~~~json
{
  "source": "00bbbf30",
  "target": "00c5aee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf3c`](#insn-00bbbf3c)

~~~json
{
  "source": "00bbbf3c",
  "target": "00c5ae20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf40`](#insn-00bbbf40)

~~~json
{
  "source": "00bbbf40",
  "target": "00bbbf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf48`](#insn-00bbbf48)

~~~json
{
  "source": "00bbbf48",
  "target": "002a28c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a28c8",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a28c8",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbbf4c`](#insn-00bbbf4c)

~~~json
{
  "source": "00bbbf4c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf58`](#insn-00bbbf58)

~~~json
{
  "source": "00bbbf58",
  "target": "00c5ad40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf6c`](#insn-00bbbf6c)

~~~json
{
  "source": "00bbbf6c",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbf70`](#insn-00bbbf70)

~~~json
{
  "source": "00bbbf70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf74`](#insn-00bbbf74)

~~~json
{
  "source": "00bbbf74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
