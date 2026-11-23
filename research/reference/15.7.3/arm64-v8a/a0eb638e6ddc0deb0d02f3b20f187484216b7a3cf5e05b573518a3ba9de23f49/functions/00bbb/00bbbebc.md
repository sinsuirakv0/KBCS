# 00bbbebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbbdf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbdf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-3b1f84eabf155dd64ab9f697c72c793f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbbf00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbf00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0011.md#compare-17b80e4494298f80c475a97ebe82c51d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbebc",
  "name": "FUN_00bbbebc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "990dba8617a3ac3f718cd16b1e8b674585aa62bec85232c00bb0ad5d72ed4520",
  "source_text_sha256": "990dba8617a3ac3f718cd16b1e8b674585aa62bec85232c00bb0ad5d72ed4520",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbebc",
        "00bbbf5b"
      ]
    ],
    "bytes_sha256": "8874e2e40cbab61605d7fc724e802a753e39aece80a04a0766de76095c8d80fa",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbbb0c](../00bbb/00bbbb0c.md)
- [00bbbdc8](../00bbb/00bbbdc8.md)

## 呼び出し先

- [00bdb770](../00bdb/00bdb770.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 999 bytes

~~~c

bool FUN_00bbbebc(long param_1,long param_2)

{
  bool bVar1;
  long lVar2;
  
  if (param_2 != 0) {
                    /* try { // try from 00bbbef4 to 00cbbefb has its CatchHandler @ 00bbd38c */
    lVar2 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
    bVar1 = false;
    if (lVar2 != 0) {
                    /* try { // try from 00bbbf00 to 00cbbf0f has its CatchHandler @ 00bbd370 */
      if (((*(uint *)(lVar2 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) == 0) &&
         (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar2 + 0x18) + 8))) {
        bVar1 = *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar2 + 0x20) + 8);
      }
      else {
                    /* try { // try from 00bbbf24 to 00cbbf2b has its CatchHandler @ 00bbd1a8 */
        bVar1 = false;
      }
    }
    return bVar1;
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbebc"></a> `00bbbebc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbbec0"></a> `00bbbec0` | `c1 03 00 b4` | cbz x1,0x00bbbf38 | `CONDITIONAL_JUMP`
<a id="insn-00bbbec4"></a> `00bbbec4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbec8"></a> `00bbbec8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bbbecc"></a> `00bbbecc` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbed0"></a> `00bbbed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbed4"></a> `00bbbed4` | `08 03 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbed8"></a> `00bbbed8` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbedc"></a> `00bbbedc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbee0"></a> `00bbbee0` | `08 fd 47 f9` | ldr x8,[x8, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbee4"></a> `00bbbee4` | `42 18 40 f9` | ldr x2,[x2, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbee8"></a> `00bbbee8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbbeec"></a> `00bbbeec` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbef0"></a> `00bbbef0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bbbef4"></a> `00bbbef4` | `1f 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbef8"></a> `00bbbef8` | `80 01 00 b4` | cbz x0,0x00bbbf28 | `CONDITIONAL_JUMP`
<a id="insn-00bbbefc"></a> `00bbbefc` | `68 12 40 b9` | ldr w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf00"></a> `00bbbf00` | `09 10 40 b9` | ldr w9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf04"></a> `00bbbf04` | `3f 01 28 6a` | bics wzr,w9,w8 | `FALL_THROUGH`
<a id="insn-00bbbf08"></a> `00bbbf08` | `e1 00 00 54` | b.ne 0x00bbbf24 | `CONDITIONAL_JUMP`
<a id="insn-00bbbf0c"></a> `00bbbf0c` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbf10"></a> `00bbbf10` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbf14"></a> `00bbbf14` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbf18"></a> `00bbbf18` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbf1c"></a> `00bbbf1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbf20"></a> `00bbbf20` | `00 01 00 54` | b.eq 0x00bbbf40 | `CONDITIONAL_JUMP`
<a id="insn-00bbbf24"></a> `00bbbf24` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbf28"></a> `00bbbf28` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf2c"></a> `00bbbf2c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bbbf30"></a> `00bbbf30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbf34"></a> `00bbbf34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbf38"></a> `00bbbf38` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbf3c"></a> `00bbbf3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbf40"></a> `00bbbf40` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbf44"></a> `00bbbf44` | `09 10 40 f9` | ldr x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbf48"></a> `00bbbf48` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbf4c"></a> `00bbbf4c` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbf50"></a> `00bbbf50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbf54"></a> `00bbbf54` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbf58"></a> `00bbbf58` | `f4 ff ff 17` | b 0x00bbbf28 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbebc`](#insn-00bbbebc) 範囲 `[['00bbbebc', '00bbbec3']]`
  - `CONDITIONAL_JUMP` [`00bbbec0`](#insn-00bbbec0) → [`00bbbf38`](#insn-00bbbf38)
  - `FALL_THROUGH` [`00bbbec0`](#insn-00bbbec0) → [`00bbbec4`](#insn-00bbbec4)
- ブロック [`00bbbec4`](#insn-00bbbec4) 範囲 `[['00bbbec4', '00bbbef3']]`
  - `FALL_THROUGH` [`00bbbef0`](#insn-00bbbef0) → [`00bbbef4`](#insn-00bbbef4)
- ブロック [`00bbbef4`](#insn-00bbbef4) 範囲 `[['00bbbef4', '00bbbefb']]`
  - `CONDITIONAL_JUMP` [`00bbbef8`](#insn-00bbbef8) → [`00bbbf28`](#insn-00bbbf28)
  - `FALL_THROUGH` [`00bbbef8`](#insn-00bbbef8) → [`00bbbefc`](#insn-00bbbefc)
- ブロック [`00bbbefc`](#insn-00bbbefc) 範囲 `[['00bbbefc', '00bbbeff']]`
  - `FALL_THROUGH` [`00bbbefc`](#insn-00bbbefc) → [`00bbbf00`](#insn-00bbbf00)
- ブロック [`00bbbf00`](#insn-00bbbf00) 範囲 `[['00bbbf00', '00bbbf0b']]`
  - `CONDITIONAL_JUMP` [`00bbbf08`](#insn-00bbbf08) → [`00bbbf24`](#insn-00bbbf24)
  - `FALL_THROUGH` [`00bbbf08`](#insn-00bbbf08) → [`00bbbf0c`](#insn-00bbbf0c)
- ブロック [`00bbbf0c`](#insn-00bbbf0c) 範囲 `[['00bbbf0c', '00bbbf23']]`
  - `CONDITIONAL_JUMP` [`00bbbf20`](#insn-00bbbf20) → [`00bbbf40`](#insn-00bbbf40)
  - `FALL_THROUGH` [`00bbbf20`](#insn-00bbbf20) → [`00bbbf24`](#insn-00bbbf24)
- ブロック [`00bbbf24`](#insn-00bbbf24) 範囲 `[['00bbbf24', '00bbbf27']]`
  - `FALL_THROUGH` [`00bbbf24`](#insn-00bbbf24) → [`00bbbf28`](#insn-00bbbf28)
- ブロック [`00bbbf28`](#insn-00bbbf28) 範囲 `[['00bbbf28', '00bbbf37']]`
- ブロック [`00bbbf38`](#insn-00bbbf38) 範囲 `[['00bbbf38', '00bbbf3f']]`
- ブロック [`00bbbf40`](#insn-00bbbf40) 範囲 `[['00bbbf40', '00bbbf5b']]`
  - `UNCONDITIONAL_JUMP` [`00bbbf58`](#insn-00bbbf58) → [`00bbbf28`](#insn-00bbbf28)

## 命令位置別の参照

- [`00bbbec0`](#insn-00bbbec0) → [`00bbbf38`](#insn-00bbbf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbec8`](#insn-00bbbec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbecc`](#insn-00bbbecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbee0`](#insn-00bbbee0) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbee4`](#insn-00bbbee4) → `00c1c030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbee4`](#insn-00bbbee4) → `00c16c38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbef0`](#insn-00bbbef0) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbef4`](#insn-00bbbef4) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbef8`](#insn-00bbbef8) → [`00bbbf28`](#insn-00bbbf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf08`](#insn-00bbbf08) → [`00bbbf24`](#insn-00bbbf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf20`](#insn-00bbbf20) → [`00bbbf40`](#insn-00bbbf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf28`](#insn-00bbbf28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf2c`](#insn-00bbbf2c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf58`](#insn-00bbbf58) → [`00bbbf28`](#insn-00bbbf28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbec0`](#insn-00bbbec0)

~~~json
{
  "source": "00bbbec0",
  "target": "00bbbf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbec8`](#insn-00bbbec8)

~~~json
{
  "source": "00bbbec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbecc`](#insn-00bbbecc)

~~~json
{
  "source": "00bbbecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbee0`](#insn-00bbbee0)

~~~json
{
  "source": "00bbbee0",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbee4`](#insn-00bbbee4)

~~~json
{
  "source": "00bbbee4",
  "target": "00c1c030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbee4`](#insn-00bbbee4)

~~~json
{
  "source": "00bbbee4",
  "target": "00c16c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbef0`](#insn-00bbbef0)

~~~json
{
  "source": "00bbbef0",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbef4`](#insn-00bbbef4)

~~~json
{
  "source": "00bbbef4",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbef8`](#insn-00bbbef8)

~~~json
{
  "source": "00bbbef8",
  "target": "00bbbf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf08`](#insn-00bbbf08)

~~~json
{
  "source": "00bbbf08",
  "target": "00bbbf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf20`](#insn-00bbbf20)

~~~json
{
  "source": "00bbbf20",
  "target": "00bbbf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf28`](#insn-00bbbf28)

~~~json
{
  "source": "00bbbf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf2c`](#insn-00bbbf2c)

~~~json
{
  "source": "00bbbf2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf58`](#insn-00bbbf58)

~~~json
{
  "source": "00bbbf58",
  "target": "00bbbf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
