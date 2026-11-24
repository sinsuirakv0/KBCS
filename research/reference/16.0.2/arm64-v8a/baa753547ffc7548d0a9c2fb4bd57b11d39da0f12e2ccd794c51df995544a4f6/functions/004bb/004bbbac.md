# 004bbbac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004bbb6c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0008.md#compare-955d90c2fe55c550376382be79e5f69b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004bbecc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004bb/004bbecc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-fd5b2c1c3a60ab7d0bf09dc3b169ced8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "FUN_004bbbac",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac",
  "source_text_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bbbac",
        "004bbc63"
      ],
      [
        "004bbcb0",
        "004bbcb3"
      ]
    ],
    "bytes_sha256": "4a5e7d8eefed1a04e245add3e1192393e3b5b5d26d95467322cc11312de850c4",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004b6768](../004b6/004b6768.md)
- [004b993c](../004b9/004b993c.md)
- [004ba4d8](../004ba/004ba4d8.md)
- [004ddf48](../004dd/004ddf48.md)

## 呼び出し先

- [0043de18](../0043d/0043de18.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58740](../00c58/00c58740.md)

## 関連文字列（未確認候補）

~~~text
"bigint_divop divide by zero"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 972 bytes

~~~c

ulong FUN_004bbbac(long param_1,ulong param_2,uint param_3)

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
    FUN_0043de18(auStack_50,"bigint_divop divide by zero");
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar3,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar3,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9ae00,FUN_005358a8);
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
<a id="insn-004bbbac"></a> `004bbbac` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004bbbb0"></a> `004bbbb0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bbbb4"></a> `004bbbb4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bbbb8"></a> `004bbbb8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bbbbc"></a> `004bbbbc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004bbbc0"></a> `004bbbc0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bbbc4"></a> `004bbbc4` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbbc8"></a> `004bbbc8` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbbcc"></a> `004bbbcc` | `c2 01 00 34` | cbz w2,0x004bbc04 | `CONDITIONAL_JUMP`
<a id="insn-004bbbd0"></a> `004bbbd0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbbd4"></a> `004bbbd4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbbd8"></a> `004bbbd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bbbdc"></a> `004bbbdc` | `a1 06 00 54` | b.ne 0x004bbcb0 | `CONDITIONAL_JUMP`
<a id="insn-004bbbe0"></a> `004bbbe0` | `e8 03 01 2a` | mov w8,w1 | `FALL_THROUGH`
<a id="insn-004bbbe4"></a> `004bbbe4` | `e9 03 02 2a` | mov w9,w2 | `FALL_THROUGH`
<a id="insn-004bbbe8"></a> `004bbbe8` | `08 81 00 aa` | orr x8,x8,x0, LSL #0x20 | `FALL_THROUGH`
<a id="insn-004bbbec"></a> `004bbbec` | `00 09 c9 9a` | udiv x0,x8,x9 | `FALL_THROUGH`
<a id="insn-004bbbf0"></a> `004bbbf0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bbbf4"></a> `004bbbf4` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bbbf8"></a> `004bbbf8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bbbfc"></a> `004bbbfc` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004bbc00"></a> `004bbc00` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bbc04"></a> `004bbc04` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004bbc08"></a> `004bbc08` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bbc0c"></a> `004bbc0c` | `ed 70 1e 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004bbc10"></a> `004bbc10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bbc14"></a> `004bbc14` | `c1 ef ff b0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-004bbc18"></a> `004bbc18` | `21 54 37 91` | add x1,x1,#0xdd5 | `FALL_THROUGH`
<a id="insn-004bbc1c"></a> `004bbc1c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004bbc20"></a> `004bbc20` | `7e 08 fe 97` | bl 0x0043de18 | `UNCONDITIONAL_CALL`
<a id="insn-004bbc24"></a> `004bbc24` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004bbc28"></a> `004bbc28` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004bbc2c"></a> `004bbc2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bbc30"></a> `004bbc30` | `c4 72 1e 94` | bl 0x00c58740 | `UNCONDITIONAL_CALL`
<a id="insn-004bbc34"></a> `004bbc34` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bbc38"></a> `004bbc38` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004bbc3c"></a> `004bbc3c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bbc40"></a> `004bbc40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bbc44"></a> `004bbc44` | `61 03 00 54` | b.ne 0x004bbcb0 | `CONDITIONAL_JUMP`
<a id="insn-004bbc48"></a> `004bbc48` | `e1 3e 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004bbc4c"></a> `004bbc4c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004bbc50"></a> `004bbc50` | `c2 e2 3c 10` | adr x2,0x5358a8 | `FALL_THROUGH`
<a id="insn-004bbc54"></a> `004bbc54` | `21 00 47 f9` | ldr x1,[x1, #0xe00] | `FALL_THROUGH`
<a id="insn-004bbc58"></a> `004bbc58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bbc5c"></a> `004bbc5c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004bbc60"></a> `004bbc60` | `e0 70 1e 94` | bl 0x00c57fe0 | `CALL_TERMINATOR`
<a id="insn-004bbcb0"></a> `004bbcb0` | `c0 70 1e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bbbac`](#insn-004bbbac) 範囲 `[['004bbbac', '004bbbcf']]`
  - `CONDITIONAL_JUMP` [`004bbbcc`](#insn-004bbbcc) → [`004bbc04`](#insn-004bbc04)
  - `FALL_THROUGH` [`004bbbcc`](#insn-004bbbcc) → [`004bbbd0`](#insn-004bbbd0)
- ブロック [`004bbbd0`](#insn-004bbbd0) 範囲 `[['004bbbd0', '004bbbdf']]`
  - `CONDITIONAL_JUMP` [`004bbbdc`](#insn-004bbbdc) → [`004bbcb0`](#insn-004bbcb0)
  - `FALL_THROUGH` [`004bbbdc`](#insn-004bbbdc) → [`004bbbe0`](#insn-004bbbe0)
- ブロック [`004bbbe0`](#insn-004bbbe0) 範囲 `[['004bbbe0', '004bbc03']]`
- ブロック [`004bbc04`](#insn-004bbc04) 範囲 `[['004bbc04', '004bbc47']]`
  - `CONDITIONAL_JUMP` [`004bbc44`](#insn-004bbc44) → [`004bbcb0`](#insn-004bbcb0)
  - `FALL_THROUGH` [`004bbc44`](#insn-004bbc44) → [`004bbc48`](#insn-004bbc48)
- ブロック [`004bbc48`](#insn-004bbc48) 範囲 `[['004bbc48', '004bbc63']]`
- ブロック [`004bbcb0`](#insn-004bbcb0) 範囲 `[['004bbcb0', '004bbcb3']]`

## 命令位置別の参照

- [`004bbbb0`](#insn-004bbbb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbb4`](#insn-004bbbb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbb8`](#insn-004bbbb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbc8`](#insn-004bbbc8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbcc`](#insn-004bbbcc) → [`004bbc04`](#insn-004bbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbd4`](#insn-004bbbd4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbdc`](#insn-004bbbdc) → [`004bbcb0`](#insn-004bbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbf0`](#insn-004bbbf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbf4`](#insn-004bbbf4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbbf8`](#insn-004bbbf8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc08`](#insn-004bbc08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc0c`](#insn-004bbc0c) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004bbc18`](#insn-004bbc18) → `002b4dd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bbc20`](#insn-004bbc20) → [`0043de18`](../0043d/0043de18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043de18` · 推定シンボル `None` · 推定型 `None`
- [`004bbc30`](#insn-004bbc30) → [`00c58740`](../00c58/00c58740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58740` · 推定シンボル `None` · 推定型 `None`
- [`004bbc34`](#insn-004bbc34) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc3c`](#insn-004bbc3c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc44`](#insn-004bbc44) → [`004bbcb0`](#insn-004bbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bbc50`](#insn-004bbc50) → [`005358a8`](../00535/005358a8.md) · `PARAM` · `ANALYSIS` · 関数 `005358a8` · 推定シンボル `None` · 推定型 `None`
- [`004bbc54`](#insn-004bbc54) → `00c9ae00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004bbc54`](#insn-004bbc54) → `00c66378`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan16Invalid_ArgumentE` · 推定型 `pointer __((offset(0x10)))`
- [`004bbc60`](#insn-004bbc60) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`004bbcb0`](#insn-004bbcb0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bbbb0`](#insn-004bbbb0)

~~~json
{
  "source": "004bbbb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbb4`](#insn-004bbbb4)

~~~json
{
  "source": "004bbbb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbb8`](#insn-004bbbb8)

~~~json
{
  "source": "004bbbb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbc8`](#insn-004bbbc8)

~~~json
{
  "source": "004bbbc8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbcc`](#insn-004bbbcc)

~~~json
{
  "source": "004bbbcc",
  "target": "004bbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbd4`](#insn-004bbbd4)

~~~json
{
  "source": "004bbbd4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbdc`](#insn-004bbbdc)

~~~json
{
  "source": "004bbbdc",
  "target": "004bbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbf0`](#insn-004bbbf0)

~~~json
{
  "source": "004bbbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbf4`](#insn-004bbbf4)

~~~json
{
  "source": "004bbbf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbbf8`](#insn-004bbbf8)

~~~json
{
  "source": "004bbbf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc08`](#insn-004bbc08)

~~~json
{
  "source": "004bbc08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc0c`](#insn-004bbc0c)

~~~json
{
  "source": "004bbc0c",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbc18`](#insn-004bbc18)

~~~json
{
  "source": "004bbc18",
  "target": "002b4dd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4dd5",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "626967696e745f6469766f7020646976696465206279207a65726f00",
  "capture_start": "002b4dd5",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bbc20`](#insn-004bbc20)

~~~json
{
  "source": "004bbc20",
  "target": "0043de18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbc30`](#insn-004bbc30)

~~~json
{
  "source": "004bbc30",
  "target": "00c58740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbc34`](#insn-004bbc34)

~~~json
{
  "source": "004bbc34",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc3c`](#insn-004bbc3c)

~~~json
{
  "source": "004bbc3c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc44`](#insn-004bbc44)

~~~json
{
  "source": "004bbc44",
  "target": "004bbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bbc50`](#insn-004bbc50)

~~~json
{
  "source": "004bbc50",
  "target": "005358a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbc54`](#insn-004bbc54)

~~~json
{
  "source": "004bbc54",
  "target": "00c9ae00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ae00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bbc54`](#insn-004bbc54)

~~~json
{
  "source": "004bbc54",
  "target": "00c66378",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66378",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bbc60`](#insn-004bbc60)

~~~json
{
  "source": "004bbc60",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bbcb0`](#insn-004bbcb0)

~~~json
{
  "source": "004bbcb0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
