# 007fdbdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007fcc78`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007fc/007fcc78.md) · 移動量 `+0xf64`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0042.md#compare-af747bba64d836444054b741f4b6ea6a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fdbdc",
  "name": "FUN_007fdbdc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e4960e8c0b48b304aec8886ff5110f32c6769b1f09a340d2b54f902c77a7064",
  "source_text_sha256": "0e4960e8c0b48b304aec8886ff5110f32c6769b1f09a340d2b54f902c77a7064",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fdbdc",
        "007fdc8b"
      ]
    ],
    "bytes_sha256": "8116a5ee3a7792e084d630896efbbf48d4d7e5ee0554b87afb095f27026f2eae",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
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
- [008524fc](../00852/008524fc.md)
- [008ba17c](../008ba/008ba17c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 897 bytes

~~~c

void FUN_007fdbdc(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined4 uVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  if ((*param_3 == 2) && (*param_4 != -1)) {
    uVar4 = *param_2;
    uVar2 = FUN_0047b054();
    FUN_0047d134(uVar2,0xb,0);
    FUN_008ba17c(uVar4);
    return;
  }
  if ((*param_3 == 5) && (*param_4 == 0)) {
    lVar3 = FUN_008524fc();
    *(int *)((long)&fde_table_entry_00333de0.initial_loc + lVar3) =
         *(int *)((long)&fde_table_entry_00333de0.initial_loc + lVar3) + 1;
    lVar3 = FUN_008524fc();
    *(undefined4 *)((long)&fde_table_entry_00335f48.initial_loc + lVar3) = 0;
    lVar3 = FUN_008524fc();
    uVar1 = *(undefined4 *)(param_1 + 8);
    *(undefined4 *)(&uleb128_0029a6d8 + lVar3) = 0;
    lVar3 = FUN_008524fc();
    *(undefined4 *)((long)&fde_table_entry_00336eb0.initial_loc + lVar3) = uVar1;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fdbdc"></a> `007fdbdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fdbe0"></a> `007fdbe0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdbe4"></a> `007fdbe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fdbe8"></a> `007fdbe8` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-007fdbec"></a> `007fdbec` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-007fdbf0"></a> `007fdbf0` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-007fdbf4"></a> `007fdbf4` | `81 01 00 54` | b.ne 0x007fdc24 | `CONDITIONAL_JUMP`
<a id="insn-007fdbf8"></a> `007fdbf8` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-007fdbfc"></a> `007fdbfc` | `40 01 00 54` | b.eq 0x007fdc24 | `CONDITIONAL_JUMP`
<a id="insn-007fdc00"></a> `007fdc00` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-007fdc04"></a> `007fdc04` | `14 f5 f1 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-007fdc08"></a> `007fdc08` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-007fdc0c"></a> `007fdc0c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-007fdc10"></a> `007fdc10` | `49 fd f1 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-007fdc14"></a> `007fdc14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fdc18"></a> `007fdc18` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdc1c"></a> `007fdc1c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fdc20"></a> `007fdc20` | `57 f1 02 14` | b 0x008ba17c | `CALL_TERMINATOR`
<a id="insn-007fdc24"></a> `007fdc24` | `3f 15 00 71` | cmp w9,#0x5 | `FALL_THROUGH`
<a id="insn-007fdc28"></a> `007fdc28` | `c1 02 00 54` | b.ne 0x007fdc80 | `CONDITIONAL_JUMP`
<a id="insn-007fdc2c"></a> `007fdc2c` | `a8 02 00 35` | cbnz w8,0x007fdc80 | `CONDITIONAL_JUMP`
<a id="insn-007fdc30"></a> `007fdc30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007fdc34"></a> `007fdc34` | `32 52 01 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-007fdc38"></a> `007fdc38` | `08 bc 87 52` | mov w8,#0x3de0 | `FALL_THROUGH`
<a id="insn-007fdc3c"></a> `007fdc3c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-007fdc40"></a> `007fdc40` | `09 68 68 b8` | ldr w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007fdc44"></a> `007fdc44` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-007fdc48"></a> `007fdc48` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007fdc4c"></a> `007fdc4c` | `2c 52 01 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-007fdc50"></a> `007fdc50` | `08 e9 8b 52` | mov w8,#0x5f48 | `FALL_THROUGH`
<a id="insn-007fdc54"></a> `007fdc54` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-007fdc58"></a> `007fdc58` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007fdc5c"></a> `007fdc5c` | `28 52 01 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-007fdc60"></a> `007fdc60` | `08 db 94 52` | mov w8,#0xa6d8 | `FALL_THROUGH`
<a id="insn-007fdc64"></a> `007fdc64` | `73 0a 40 b9` | ldr w19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007fdc68"></a> `007fdc68` | `28 05 a0 72` | movk w8,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-007fdc6c"></a> `007fdc6c` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007fdc70"></a> `007fdc70` | `23 52 01 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-007fdc74"></a> `007fdc74` | `08 d6 8d 52` | mov w8,#0x6eb0 | `FALL_THROUGH`
<a id="insn-007fdc78"></a> `007fdc78` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-007fdc7c"></a> `007fdc7c` | `13 68 28 b8` | str w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007fdc80"></a> `007fdc80` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fdc84"></a> `007fdc84` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fdc88"></a> `007fdc88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fdbdc`](#insn-007fdbdc) 範囲 `[['007fdbdc', '007fdbf7']]`
  - `CONDITIONAL_JUMP` [`007fdbf4`](#insn-007fdbf4) → [`007fdc24`](#insn-007fdc24)
  - `FALL_THROUGH` [`007fdbf4`](#insn-007fdbf4) → [`007fdbf8`](#insn-007fdbf8)
- ブロック [`007fdbf8`](#insn-007fdbf8) 範囲 `[['007fdbf8', '007fdbff']]`
  - `CONDITIONAL_JUMP` [`007fdbfc`](#insn-007fdbfc) → [`007fdc24`](#insn-007fdc24)
  - `FALL_THROUGH` [`007fdbfc`](#insn-007fdbfc) → [`007fdc00`](#insn-007fdc00)
- ブロック [`007fdc00`](#insn-007fdc00) 範囲 `[['007fdc00', '007fdc23']]`
- ブロック [`007fdc24`](#insn-007fdc24) 範囲 `[['007fdc24', '007fdc2b']]`
  - `CONDITIONAL_JUMP` [`007fdc28`](#insn-007fdc28) → [`007fdc80`](#insn-007fdc80)
  - `FALL_THROUGH` [`007fdc28`](#insn-007fdc28) → [`007fdc2c`](#insn-007fdc2c)
- ブロック [`007fdc2c`](#insn-007fdc2c) 範囲 `[['007fdc2c', '007fdc2f']]`
  - `CONDITIONAL_JUMP` [`007fdc2c`](#insn-007fdc2c) → [`007fdc80`](#insn-007fdc80)
  - `FALL_THROUGH` [`007fdc2c`](#insn-007fdc2c) → [`007fdc30`](#insn-007fdc30)
- ブロック [`007fdc30`](#insn-007fdc30) 範囲 `[['007fdc30', '007fdc7f']]`
  - `FALL_THROUGH` [`007fdc7c`](#insn-007fdc7c) → [`007fdc80`](#insn-007fdc80)
- ブロック [`007fdc80`](#insn-007fdc80) 範囲 `[['007fdc80', '007fdc8b']]`

## 命令位置別の参照

- [`007fdbdc`](#insn-007fdbdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdbe0`](#insn-007fdbe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdbf4`](#insn-007fdbf4) → [`007fdc24`](#insn-007fdc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdbfc`](#insn-007fdbfc) → [`007fdc24`](#insn-007fdc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc04`](#insn-007fdc04) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`007fdc10`](#insn-007fdc10) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`007fdc18`](#insn-007fdc18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc1c`](#insn-007fdc1c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc20`](#insn-007fdc20) → [`008ba17c`](../008ba/008ba17c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008ba17c` · 推定シンボル `None` · 推定型 `None`
- [`007fdc28`](#insn-007fdc28) → [`007fdc80`](#insn-007fdc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc2c`](#insn-007fdc2c) → [`007fdc80`](#insn-007fdc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc34`](#insn-007fdc34) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`007fdc40`](#insn-007fdc40) → `00333de0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fdc48`](#insn-007fdc48) → `00333de0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fdc4c`](#insn-007fdc4c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`007fdc58`](#insn-007fdc58) → `00335f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fdc5c`](#insn-007fdc5c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`007fdc6c`](#insn-007fdc6c) → `0029a6d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`007fdc70`](#insn-007fdc70) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`007fdc7c`](#insn-007fdc7c) → `00336eb0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`007fdc80`](#insn-007fdc80) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fdc84`](#insn-007fdc84) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fdbdc`](#insn-007fdbdc)

~~~json
{
  "source": "007fdbdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdbe0`](#insn-007fdbe0)

~~~json
{
  "source": "007fdbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdbf4`](#insn-007fdbf4)

~~~json
{
  "source": "007fdbf4",
  "target": "007fdc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdbfc`](#insn-007fdbfc)

~~~json
{
  "source": "007fdbfc",
  "target": "007fdc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc04`](#insn-007fdc04)

~~~json
{
  "source": "007fdc04",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc10`](#insn-007fdc10)

~~~json
{
  "source": "007fdc10",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc18`](#insn-007fdc18)

~~~json
{
  "source": "007fdc18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc1c`](#insn-007fdc1c)

~~~json
{
  "source": "007fdc1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc20`](#insn-007fdc20)

~~~json
{
  "source": "007fdc20",
  "target": "008ba17c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc28`](#insn-007fdc28)

~~~json
{
  "source": "007fdc28",
  "target": "007fdc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc2c`](#insn-007fdc2c)

~~~json
{
  "source": "007fdc2c",
  "target": "007fdc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc34`](#insn-007fdc34)

~~~json
{
  "source": "007fdc34",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc40`](#insn-007fdc40)

~~~json
{
  "source": "007fdc40",
  "target": "00333de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333de0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1c6a6b00e8840900",
  "capture_start": "00333de0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fdc48`](#insn-007fdc48)

~~~json
{
  "source": "007fdc48",
  "target": "00333de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333de0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "1c6a6b00e8840900",
  "capture_start": "00333de0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fdc4c`](#insn-007fdc4c)

~~~json
{
  "source": "007fdc4c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc58`](#insn-007fdc58)

~~~json
{
  "source": "007fdc58",
  "target": "00335f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f48",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "646c750010fe0900",
  "capture_start": "00335f48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fdc5c`](#insn-007fdc5c)

~~~json
{
  "source": "007fdc5c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc6c`](#insn-007fdc6c)

~~~json
{
  "source": "007fdc6c",
  "target": "0029a6d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a6d8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0029a6d8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fdc70`](#insn-007fdc70)

~~~json
{
  "source": "007fdc70",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fdc7c`](#insn-007fdc7c)

~~~json
{
  "source": "007fdc7c",
  "target": "00336eb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336eb0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c7b78003c310a00",
  "capture_start": "00336eb0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`007fdc80`](#insn-007fdc80)

~~~json
{
  "source": "007fdc80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fdc84`](#insn-007fdc84)

~~~json
{
  "source": "007fdc84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
