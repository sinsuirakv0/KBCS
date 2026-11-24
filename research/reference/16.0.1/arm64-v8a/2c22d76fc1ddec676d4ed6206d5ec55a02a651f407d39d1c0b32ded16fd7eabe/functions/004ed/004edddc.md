# 004edddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004edd9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0010.md#compare-03fb37f3d6da0f89d46e4efd5c186610)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ede1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ed/004ede1c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0010.md#compare-9e1f05c877635fea91b551bad5e0a219)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004edddc",
  "name": "_ZN5Botan5PKCS88load_keyERNS_10DataSourceE",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "adcd1d9a7ad21fc53a5dcc9e93970791a5e0303dc4d3af1f922acabcbb3d0af5",
  "source_text_sha256": "adcd1d9a7ad21fc53a5dcc9e93970791a5e0303dc4d3af1f922acabcbb3d0af5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004edddc",
        "004ede63"
      ],
      [
        "004edeb0",
        "004edeb3"
      ]
    ],
    "bytes_sha256": "66daec4e60e7159ea82b5e800683ed5795f06819fd59839215097fbb9ad4adce",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59640](../00c59/00c59640.md)

## 呼び出し先

- [004ecd10](../004ec/004ecd10.md)
- [00545970](../00545/00545970.md)
- [00545974](../00545/00545974.md)
- [00c57ee0](../00c57/00c57ee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 771 bytes

~~~c

void _ZN5Botan5PKCS88load_keyERNS_10DataSourceE(undefined8 param_1)

{
  long lVar1;
  undefined ***pppuVar2;
  long lVar3;
  undefined **local_60 [4];
  long *local_40;
  long local_28;
  
  local_40 = (long *)local_60;
  pppuVar2 = local_60;
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_60[0] = &PTR_FUN_00c6a5b0;
  FUN_004ecd10(param_1,local_60,0);
  if ((undefined ***)local_40 == local_60) {
    lVar3 = 0x20;
  }
  else {
    if (local_40 == (long *)0x0) goto LAB_004ede44;
    lVar3 = 0x28;
    pppuVar2 = (undefined ***)local_40;
  }
  (**(code **)((long)*pppuVar2 + lVar3))();
LAB_004ede44:
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004edddc"></a> `004edddc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004edde0"></a> `004edde0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004edde4"></a> `004edde4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004edde8"></a> `004edde8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004eddec"></a> `004eddec` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004eddf0"></a> `004eddf0` | `ea 3b 00 b0` | adrp x10,0xc6a000 | `FALL_THROUGH`
<a id="insn-004eddf4"></a> `004eddf4` | `4a c1 16 91` | add x10,x10,#0x5b0 | `FALL_THROUGH`
<a id="insn-004eddf8"></a> `004eddf8` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004eddfc"></a> `004eddfc` | `f3 03 00 91` | mov x19,sp | `FALL_THROUGH`
<a id="insn-004ede00"></a> `004ede00` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ede04"></a> `004ede04` | `ea 03 00 f9` | str x10,[sp] | `FALL_THROUGH`
<a id="insn-004ede08"></a> `004ede08` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ede0c"></a> `004ede0c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004ede10"></a> `004ede10` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004ede14"></a> `004ede14` | `bf fb ff 97` | bl 0x004ecd10 | `UNCONDITIONAL_CALL`
<a id="insn-004ede18"></a> `004ede18` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004ede1c"></a> `004ede1c` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-004ede20"></a> `004ede20` | `80 00 00 54` | b.eq 0x004ede30 | `CONDITIONAL_JUMP`
<a id="insn-004ede24"></a> `004ede24` | `00 01 00 b4` | cbz x0,0x004ede44 | `CONDITIONAL_JUMP`
<a id="insn-004ede28"></a> `004ede28` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-004ede2c"></a> `004ede2c` | `03 00 00 14` | b 0x004ede38 | `UNCONDITIONAL_JUMP`
<a id="insn-004ede30"></a> `004ede30` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-004ede34"></a> `004ede34` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004ede38"></a> `004ede38` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-004ede3c"></a> `004ede3c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004ede40"></a> `004ede40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004ede44"></a> `004ede44` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004ede48"></a> `004ede48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004ede4c"></a> `004ede4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004ede50"></a> `004ede50` | `01 03 00 54` | b.ne 0x004edeb0 | `CONDITIONAL_JUMP`
<a id="insn-004ede54"></a> `004ede54` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004ede58"></a> `004ede58` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004ede5c"></a> `004ede5c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004ede60"></a> `004ede60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004edeb0"></a> `004edeb0` | `0c a8 1d 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004edddc`](#insn-004edddc) 範囲 `[['004edddc', '004ede23']]`
  - `CONDITIONAL_JUMP` [`004ede20`](#insn-004ede20) → [`004ede30`](#insn-004ede30)
  - `FALL_THROUGH` [`004ede20`](#insn-004ede20) → [`004ede24`](#insn-004ede24)
- ブロック [`004ede24`](#insn-004ede24) 範囲 `[['004ede24', '004ede27']]`
  - `CONDITIONAL_JUMP` [`004ede24`](#insn-004ede24) → [`004ede44`](#insn-004ede44)
  - `FALL_THROUGH` [`004ede24`](#insn-004ede24) → [`004ede28`](#insn-004ede28)
- ブロック [`004ede28`](#insn-004ede28) 範囲 `[['004ede28', '004ede2f']]`
  - `UNCONDITIONAL_JUMP` [`004ede2c`](#insn-004ede2c) → [`004ede38`](#insn-004ede38)
- ブロック [`004ede30`](#insn-004ede30) 範囲 `[['004ede30', '004ede37']]`
  - `FALL_THROUGH` [`004ede34`](#insn-004ede34) → [`004ede38`](#insn-004ede38)
- ブロック [`004ede38`](#insn-004ede38) 範囲 `[['004ede38', '004ede43']]`
  - `FALL_THROUGH` [`004ede40`](#insn-004ede40) → [`004ede44`](#insn-004ede44)
- ブロック [`004ede44`](#insn-004ede44) 範囲 `[['004ede44', '004ede53']]`
  - `CONDITIONAL_JUMP` [`004ede50`](#insn-004ede50) → [`004edeb0`](#insn-004edeb0)
  - `FALL_THROUGH` [`004ede50`](#insn-004ede50) → [`004ede54`](#insn-004ede54)
- ブロック [`004ede54`](#insn-004ede54) 範囲 `[['004ede54', '004ede63']]`
- ブロック [`004edeb0`](#insn-004edeb0) 範囲 `[['004edeb0', '004edeb3']]`

## 命令位置別の参照

- [`004edde0`](#insn-004edde0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004edde4`](#insn-004edde4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede00`](#insn-004ede00) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede04`](#insn-004ede04) → `00c6a5b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004ede04`](#insn-004ede04) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede08`](#insn-004ede08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede14`](#insn-004ede14) → [`004ecd10`](../004ec/004ecd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004ecd10` · 推定シンボル `None` · 推定型 `None`
- [`004ede18`](#insn-004ede18) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede20`](#insn-004ede20) → [`004ede30`](#insn-004ede30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede24`](#insn-004ede24) → [`004ede44`](#insn-004ede44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede2c`](#insn-004ede2c) → [`004ede38`](#insn-004ede38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede38`](#insn-004ede38) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede3c`](#insn-004ede3c) → `00c6a5d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004ede3c`](#insn-004ede3c) → `00c6a5d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`004ede40`](#insn-004ede40) → [`00545970`](../00545/00545970.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00545970` · 推定シンボル `None` · 推定型 `None`
- [`004ede40`](#insn-004ede40) → [`00545974`](../00545/00545974.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00545974` · 推定シンボル `None` · 推定型 `None`
- [`004ede48`](#insn-004ede48) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede50`](#insn-004ede50) → [`004edeb0`](#insn-004edeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede54`](#insn-004ede54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004ede58`](#insn-004ede58) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004edeb0`](#insn-004edeb0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004edde0`](#insn-004edde0)

~~~json
{
  "source": "004edde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004edde4`](#insn-004edde4)

~~~json
{
  "source": "004edde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede00`](#insn-004ede00)

~~~json
{
  "source": "004ede00",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede04`](#insn-004ede04)

~~~json
{
  "source": "004ede04",
  "target": "00c6a5b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a5b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ede04`](#insn-004ede04)

~~~json
{
  "source": "004ede04",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede08`](#insn-004ede08)

~~~json
{
  "source": "004ede08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede14`](#insn-004ede14)

~~~json
{
  "source": "004ede14",
  "target": "004ecd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ede18`](#insn-004ede18)

~~~json
{
  "source": "004ede18",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede20`](#insn-004ede20)

~~~json
{
  "source": "004ede20",
  "target": "004ede30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede24`](#insn-004ede24)

~~~json
{
  "source": "004ede24",
  "target": "004ede44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede2c`](#insn-004ede2c)

~~~json
{
  "source": "004ede2c",
  "target": "004ede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede38`](#insn-004ede38)

~~~json
{
  "source": "004ede38",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede3c`](#insn-004ede3c)

~~~json
{
  "source": "004ede3c",
  "target": "00c6a5d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a5d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ede3c`](#insn-004ede3c)

~~~json
{
  "source": "004ede3c",
  "target": "00c6a5d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c6a5d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004ede40`](#insn-004ede40)

~~~json
{
  "source": "004ede40",
  "target": "00545970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ede40`](#insn-004ede40)

~~~json
{
  "source": "004ede40",
  "target": "00545974",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004ede48`](#insn-004ede48)

~~~json
{
  "source": "004ede48",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede50`](#insn-004ede50)

~~~json
{
  "source": "004ede50",
  "target": "004edeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede54`](#insn-004ede54)

~~~json
{
  "source": "004ede54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004ede58`](#insn-004ede58)

~~~json
{
  "source": "004ede58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004edeb0`](#insn-004edeb0)

~~~json
{
  "source": "004edeb0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
