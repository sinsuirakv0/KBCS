# 004bbecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bbbac`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-fd5b2c1c3a60ab7d0bf09dc3b169ced8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bbecc",
  "name": "FUN_004bbecc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3efdc80386d9acf97fd9a152dca3856c19e4031ffe4a3d7d947df2f709b28d8f",
  "source_text_sha256": "3efdc80386d9acf97fd9a152dca3856c19e4031ffe4a3d7d947df2f709b28d8f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bbecc",
        "004bbf83"
      ],
      [
        "004bbfd0",
        "004bbfd3"
      ]
    ],
    "bytes_sha256": "b13e87099671c209434433f7ad81277028e91dcafb192a31b3d83e485ae69444",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004b6a88](../004b6/004b6a88.md)
- [004b9c5c](../004b9/004b9c5c.md)
- [004ba7f8](../004ba/004ba7f8.md)
- [004de268](../004de/004de268.md)

## 呼び出し先

- [0043e138](../0043e/0043e138.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59710](../00c59/00c59710.md)

## 関連文字列（未確認候補）

~~~text
"bigint_divop divide by zero"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 972 bytes

~~~c

ulong FUN_004bbecc(long param_1,ulong param_2,uint param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined1 auStack_50 [24];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if (param_3 == 0) {
    uVar3 = __cxa_allocate_exception(0x20);
    FUN_0043e138(auStack_50,"bigint_divop divide by zero");
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar3,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar3,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9bdd0,FUN_00535bc8);
    }
  }
  else if (*(long *)(lVar2 + 0x28) == local_38) {
    uVar1 = 0;
    if ((ulong)param_3 != 0) {
      uVar1 = (param_2 & 0xffffffff | param_1 << 0x20) / (ulong)param_3;
    }
    return uVar1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bbecc"></a> `004bbecc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004bbed0"></a> `004bbed0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bbed4"></a> `004bbed4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bbed8"></a> `004bbed8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bbedc"></a> `004bbedc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004bbee0"></a> `004bbee0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bbee4"></a> `004bbee4` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbee8"></a> `004bbee8` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbeec"></a> `004bbeec` | `c2 01 00 34` | cbz w2,0x004bbf24 | `CONDITIONAL_JUMP`
<a id="insn-004bbef0"></a> `004bbef0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbef4"></a> `004bbef4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbef8"></a> `004bbef8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bbefc"></a> `004bbefc` | `a1 06 00 54` | b.ne 0x004bbfd0 | `CONDITIONAL_JUMP`
<a id="insn-004bbf00"></a> `004bbf00` | `e8 03 01 2a` | mov w8,w1 | `FALL_THROUGH`
<a id="insn-004bbf04"></a> `004bbf04` | `e9 03 02 2a` | mov w9,w2 | `FALL_THROUGH`
<a id="insn-004bbf08"></a> `004bbf08` | `08 81 00 aa` | orr x8,x8,x0, LSL #0x20 | `FALL_THROUGH`
<a id="insn-004bbf0c"></a> `004bbf0c` | `00 09 c9 9a` | udiv x0,x8,x9 | `FALL_THROUGH`
<a id="insn-004bbf10"></a> `004bbf10` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bbf14"></a> `004bbf14` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bbf18"></a> `004bbf18` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bbf1c"></a> `004bbf1c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004bbf20"></a> `004bbf20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bbf24"></a> `004bbf24` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004bbf28"></a> `004bbf28` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bbf2c"></a> `004bbf2c` | `19 74 1e 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-004bbf30"></a> `004bbf30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bbf34"></a> `004bbf34` | `c1 ef ff b0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-004bbf38"></a> `004bbf38` | `21 cc 3a 91` | add x1,x1,#0xeb3 | `FALL_THROUGH`
<a id="insn-004bbf3c"></a> `004bbf3c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004bbf40"></a> `004bbf40` | `7e 08 fe 97` | bl 0x0043e138 | `UNCONDITIONAL_CALL`
<a id="insn-004bbf44"></a> `004bbf44` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004bbf48"></a> `004bbf48` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004bbf4c"></a> `004bbf4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bbf50"></a> `004bbf50` | `f0 75 1e 94` | bl 0x00c59710 | `UNCONDITIONAL_CALL`
<a id="insn-004bbf54"></a> `004bbf54` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bbf58"></a> `004bbf58` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbf5c"></a> `004bbf5c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbf60"></a> `004bbf60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bbf64"></a> `004bbf64` | `61 03 00 54` | b.ne 0x004bbfd0 | `CONDITIONAL_JUMP`
<a id="insn-004bbf68"></a> `004bbf68` | `01 3f 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-004bbf6c"></a> `004bbf6c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004bbf70"></a> `004bbf70` | `c2 e2 3c 10` | adr x2,0x535bc8 | `FALL_THROUGH`
<a id="insn-004bbf74"></a> `004bbf74` | `21 e8 46 f9` | ldr x1,[x1, #0xdd0] | `FALL_THROUGH`
<a id="insn-004bbf78"></a> `004bbf78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bbf7c"></a> `004bbf7c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004bbf80"></a> `004bbf80` | `0c 74 1e 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`
<a id="insn-004bbfd0"></a> `004bbfd0` | `ec 73 1e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bbecc`](#insn-004bbecc) 範囲 `[['004bbecc', '004bbeef']]`
  - `CONDITIONAL_JUMP` [`004bbeec`](#insn-004bbeec) → [`004bbf24`](#insn-004bbf24)
  - `FALL_THROUGH` [`004bbeec`](#insn-004bbeec) → [`004bbef0`](#insn-004bbef0)
- ブロック [`004bbef0`](#insn-004bbef0) 範囲 `[['004bbef0', '004bbeff']]`
  - `CONDITIONAL_JUMP` [`004bbefc`](#insn-004bbefc) → [`004bbfd0`](#insn-004bbfd0)
  - `FALL_THROUGH` [`004bbefc`](#insn-004bbefc) → [`004bbf00`](#insn-004bbf00)
- ブロック [`004bbf00`](#insn-004bbf00) 範囲 `[['004bbf00', '004bbf23']]`
- ブロック [`004bbf24`](#insn-004bbf24) 範囲 `[['004bbf24', '004bbf67']]`
  - `CONDITIONAL_JUMP` [`004bbf64`](#insn-004bbf64) → [`004bbfd0`](#insn-004bbfd0)
  - `FALL_THROUGH` [`004bbf64`](#insn-004bbf64) → [`004bbf68`](#insn-004bbf68)
- ブロック [`004bbf68`](#insn-004bbf68) 範囲 `[['004bbf68', '004bbf83']]`
- ブロック [`004bbfd0`](#insn-004bbfd0) 範囲 `[['004bbfd0', '004bbfd3']]`

## 命令位置別の参照

- [`004bbed0`](#insn-004bbed0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbed4`](#insn-004bbed4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbed8`](#insn-004bbed8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbee8`](#insn-004bbee8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbeec`](#insn-004bbeec) → [`004bbf24`](#insn-004bbf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbef4`](#insn-004bbef4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbefc`](#insn-004bbefc) → [`004bbfd0`](#insn-004bbfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf10`](#insn-004bbf10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf14`](#insn-004bbf14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf18`](#insn-004bbf18) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf28`](#insn-004bbf28) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf2c`](#insn-004bbf2c) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`004bbf38`](#insn-004bbf38) → `002b4eb3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bbf40`](#insn-004bbf40) → [`0043e138`](../0043e/0043e138.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043e138` · 推定シンボル `None` · 推定型 `None`
- [`004bbf50`](#insn-004bbf50) → [`00c59710`](../00c59/00c59710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59710` · 推定シンボル `None` · 推定型 `None`
- [`004bbf54`](#insn-004bbf54) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf5c`](#insn-004bbf5c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf64`](#insn-004bbf64) → [`004bbfd0`](#insn-004bbfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbf70`](#insn-004bbf70) → [`00535bc8`](../00535/00535bc8.md) · `PARAM` · `ANALYSIS` · 関数 `00535bc8` · 推定シンボル `None` · 推定型 `None`
- [`004bbf74`](#insn-004bbf74) → `00c9bdd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004bbf74`](#insn-004bbf74) → `00c67348`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan16Invalid_ArgumentE` · 推定型 `pointer __((offset(0x10)))`
- [`004bbf80`](#insn-004bbf80) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`
- [`004bbfd0`](#insn-004bbfd0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bbed0`](#insn-004bbed0)

~~~json
{
  "source": "004bbed0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbed4`](#insn-004bbed4)

~~~json
{
  "source": "004bbed4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbed8`](#insn-004bbed8)

~~~json
{
  "source": "004bbed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbee8`](#insn-004bbee8)

~~~json
{
  "source": "004bbee8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbeec`](#insn-004bbeec)

~~~json
{
  "source": "004bbeec",
  "target": "004bbf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbef4`](#insn-004bbef4)

~~~json
{
  "source": "004bbef4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbefc`](#insn-004bbefc)

~~~json
{
  "source": "004bbefc",
  "target": "004bbfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf10`](#insn-004bbf10)

~~~json
{
  "source": "004bbf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf14`](#insn-004bbf14)

~~~json
{
  "source": "004bbf14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf18`](#insn-004bbf18)

~~~json
{
  "source": "004bbf18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf28`](#insn-004bbf28)

~~~json
{
  "source": "004bbf28",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf2c`](#insn-004bbf2c)

~~~json
{
  "source": "004bbf2c",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbf38`](#insn-004bbf38)

~~~json
{
  "source": "004bbf38",
  "target": "002b4eb3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4eb3",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "626967696e745f6469766f7020646976696465206279207a65726f00",
  "capture_start": "002b4eb3",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbf40`](#insn-004bbf40)

~~~json
{
  "source": "004bbf40",
  "target": "0043e138",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbf50`](#insn-004bbf50)

~~~json
{
  "source": "004bbf50",
  "target": "00c59710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbf54`](#insn-004bbf54)

~~~json
{
  "source": "004bbf54",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf5c`](#insn-004bbf5c)

~~~json
{
  "source": "004bbf5c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf64`](#insn-004bbf64)

~~~json
{
  "source": "004bbf64",
  "target": "004bbfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbf70`](#insn-004bbf70)

~~~json
{
  "source": "004bbf70",
  "target": "00535bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbf74`](#insn-004bbf74)

~~~json
{
  "source": "004bbf74",
  "target": "00c9bdd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bdd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bbf74`](#insn-004bbf74)

~~~json
{
  "source": "004bbf74",
  "target": "00c67348",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67348",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bbf80`](#insn-004bbf80)

~~~json
{
  "source": "004bbf80",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbfd0`](#insn-004bbfd0)

~~~json
{
  "source": "004bbfd0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
