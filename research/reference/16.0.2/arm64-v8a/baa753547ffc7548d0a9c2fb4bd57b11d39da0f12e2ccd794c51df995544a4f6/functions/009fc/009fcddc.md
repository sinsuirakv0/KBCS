# 009fcddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009fcd88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd88.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0060.md#compare-6e007689f9bacd2ec4b9600c4cbc0a6d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009fdd88`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fd/009fdd88.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0061.md#compare-8ff2524d7df3b65b30b5e334e974d2a9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009fcddc",
  "name": "FUN_009fcddc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1abc089b7310ec21c02925dd36ac809594745dec513a8177a4fa3fee3ec23063",
  "source_text_sha256": "1abc089b7310ec21c02925dd36ac809594745dec513a8177a4fa3fee3ec23063",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009fcddc",
        "009fce4b"
      ]
    ],
    "bytes_sha256": "72b0016f86f91c919c37b6f9a2629c66d25d51a50a5f700b58bfae5cc9f93f0b",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 527 bytes

~~~c

void FUN_009fcddc(undefined8 *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  undefined8 *__ptr;
  
  __ptr = (undefined8 *)*param_1;
  *param_1 = 0;
  if (__ptr == (undefined8 *)0x0) {
    return;
  }
  plVar1 = (long *)__ptr[10];
  plVar2 = __ptr + 6;
  *__ptr = &PTR_FUN_00c8a550;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_009fce3c;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_009fce3c:
  _ZdlPv(__ptr);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009fcddc"></a> `009fcddc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-009fcde0"></a> `009fcde0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fcde4"></a> `009fcde4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-009fcde8"></a> `009fcde8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-009fcdec"></a> `009fcdec` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-009fcdf0"></a> `009fcdf0` | `73 01 00 b4` | cbz x19,0x009fce1c | `CONDITIONAL_JUMP`
<a id="insn-009fcdf4"></a> `009fcdf4` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-009fcdf8"></a> `009fcdf8` | `69 c2 00 91` | add x9,x19,#0x30 | `FALL_THROUGH`
<a id="insn-009fcdfc"></a> `009fcdfc` | `68 14 00 d0` | adrp x8,0xc8a000 | `FALL_THROUGH`
<a id="insn-009fce00"></a> `009fce00` | `08 41 15 91` | add x8,x8,#0x550 | `FALL_THROUGH`
<a id="insn-009fce04"></a> `009fce04` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-009fce08"></a> `009fce08` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-009fce0c"></a> `009fce0c` | `e0 00 00 54` | b.eq 0x009fce28 | `CONDITIONAL_JUMP`
<a id="insn-009fce10"></a> `009fce10` | `60 01 00 b4` | cbz x0,0x009fce3c | `CONDITIONAL_JUMP`
<a id="insn-009fce14"></a> `009fce14` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-009fce18"></a> `009fce18` | `06 00 00 14` | b 0x009fce30 | `UNCONDITIONAL_JUMP`
<a id="insn-009fce1c"></a> `009fce1c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fce20"></a> `009fce20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009fce24"></a> `009fce24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009fce28"></a> `009fce28` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-009fce2c"></a> `009fce2c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-009fce30"></a> `009fce30` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-009fce34"></a> `009fce34` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009fce38"></a> `009fce38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009fce3c"></a> `009fce3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009fce40"></a> `009fce40` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009fce44"></a> `009fce44` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-009fce48"></a> `009fce48` | `4e 6c 09 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009fcddc`](#insn-009fcddc) 範囲 `[['009fcddc', '009fcdf3']]`
  - `CONDITIONAL_JUMP` [`009fcdf0`](#insn-009fcdf0) → [`009fce1c`](#insn-009fce1c)
  - `FALL_THROUGH` [`009fcdf0`](#insn-009fcdf0) → [`009fcdf4`](#insn-009fcdf4)
- ブロック [`009fcdf4`](#insn-009fcdf4) 範囲 `[['009fcdf4', '009fce0f']]`
  - `CONDITIONAL_JUMP` [`009fce0c`](#insn-009fce0c) → [`009fce28`](#insn-009fce28)
  - `FALL_THROUGH` [`009fce0c`](#insn-009fce0c) → [`009fce10`](#insn-009fce10)
- ブロック [`009fce10`](#insn-009fce10) 範囲 `[['009fce10', '009fce13']]`
  - `CONDITIONAL_JUMP` [`009fce10`](#insn-009fce10) → [`009fce3c`](#insn-009fce3c)
  - `FALL_THROUGH` [`009fce10`](#insn-009fce10) → [`009fce14`](#insn-009fce14)
- ブロック [`009fce14`](#insn-009fce14) 範囲 `[['009fce14', '009fce1b']]`
  - `UNCONDITIONAL_JUMP` [`009fce18`](#insn-009fce18) → [`009fce30`](#insn-009fce30)
- ブロック [`009fce1c`](#insn-009fce1c) 範囲 `[['009fce1c', '009fce27']]`
- ブロック [`009fce28`](#insn-009fce28) 範囲 `[['009fce28', '009fce2f']]`
  - `FALL_THROUGH` [`009fce2c`](#insn-009fce2c) → [`009fce30`](#insn-009fce30)
- ブロック [`009fce30`](#insn-009fce30) 範囲 `[['009fce30', '009fce3b']]`
  - `FALL_THROUGH` [`009fce38`](#insn-009fce38) → [`009fce3c`](#insn-009fce3c)
- ブロック [`009fce3c`](#insn-009fce3c) 範囲 `[['009fce3c', '009fce4b']]`

## 命令位置別の参照

- [`009fcddc`](#insn-009fcddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcde0`](#insn-009fcde0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fcdf0`](#insn-009fcdf0) → [`009fce1c`](#insn-009fce1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce08`](#insn-009fce08) → `00c8a550`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009fce0c`](#insn-009fce0c) → [`009fce28`](#insn-009fce28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce10`](#insn-009fce10) → [`009fce3c`](#insn-009fce3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce18`](#insn-009fce18) → [`009fce30`](#insn-009fce30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce1c`](#insn-009fce1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce20`](#insn-009fce20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce40`](#insn-009fce40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce44`](#insn-009fce44) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009fce48`](#insn-009fce48) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009fcddc`](#insn-009fcddc)

~~~json
{
  "source": "009fcddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcde0`](#insn-009fcde0)

~~~json
{
  "source": "009fcde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fcdf0`](#insn-009fcdf0)

~~~json
{
  "source": "009fcdf0",
  "target": "009fce1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce08`](#insn-009fce08)

~~~json
{
  "source": "009fce08",
  "target": "00c8a550",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8a550",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009fce0c`](#insn-009fce0c)

~~~json
{
  "source": "009fce0c",
  "target": "009fce28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce10`](#insn-009fce10)

~~~json
{
  "source": "009fce10",
  "target": "009fce3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce18`](#insn-009fce18)

~~~json
{
  "source": "009fce18",
  "target": "009fce30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce1c`](#insn-009fce1c)

~~~json
{
  "source": "009fce1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce20`](#insn-009fce20)

~~~json
{
  "source": "009fce20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce40`](#insn-009fce40)

~~~json
{
  "source": "009fce40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce44`](#insn-009fce44)

~~~json
{
  "source": "009fce44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009fce48`](#insn-009fce48)

~~~json
{
  "source": "009fce48",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
