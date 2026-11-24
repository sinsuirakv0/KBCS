# 00acaaa8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acaa38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acaa38.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-cc0307774229d70b4c0de9cccf10fa3b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acba9c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acb/00acba9c.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0006.md#compare-47bf4286e5fc5eee79ca3df72e2faaed)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaaa8",
  "name": "FUN_00acaaa8",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d",
  "source_text_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaaa8",
        "00acab43"
      ]
    ],
    "bytes_sha256": "11d13a5bdf1399d97d247c6ab5c9f4e3514c480122fdaf5e7bd2be00ff58a9fd",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0082fbc4](../0082f/0082fbc4.md)
- [00997090](../00997/00997090.md)

## 呼び出し先

- [004678a0](../00467/004678a0.md)
- [00467b6c](../00467/00467b6c.md)
- [00467f94](../00467/00467f94.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046cac4](../0046c/0046cac4.md)
- [00851550](../00851/00851550.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 603 bytes

~~~c

void FUN_00acaaa8(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0xa0) != '\0') {
    uVar4 = FUN_004678a0();
    iVar1 = *(int *)(param_1 + 0xa4) * 0x14;
    if (0xfe < iVar1) {
      iVar1 = 0xff;
    }
    FUN_00467b6c(uVar4,0,0,0,iVar1);
    lVar5 = FUN_00851550();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_00851550();
    uVar2 = FUN_0046ca04();
    FUN_00851550();
    uVar3 = FUN_0046cac4();
    FUN_00467f94(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acaaa8"></a> `00acaaa8` | `08 80 42 39` | ldrb w8,[x0, #0xa0] | `FALL_THROUGH`
<a id="insn-00acaaac"></a> `00acaaac` | `a8 04 00 34` | cbz w8,0x00acab40 | `CONDITIONAL_JUMP`
<a id="insn-00acaab0"></a> `00acaab0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00acaab4"></a> `00acaab4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaab8"></a> `00acaab8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acaabc"></a> `00acaabc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acaac0"></a> `00acaac0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaac4"></a> `00acaac4` | `77 73 e6 97` | bl 0x004678a0 | `UNCONDITIONAL_CALL`
<a id="insn-00acaac8"></a> `00acaac8` | `68 a6 40 b9` | ldr w8,[x19, #0xa4] | `FALL_THROUGH`
<a id="insn-00acaacc"></a> `00acaacc` | `e9 1f 80 52` | mov w9,#0xff | `FALL_THROUGH`
<a id="insn-00acaad0"></a> `00acaad0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acaad4"></a> `00acaad4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00acaad8"></a> `00acaad8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00acaadc"></a> `00acaadc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acaae0"></a> `00acaae0` | `08 09 08 0b` | add w8,w8,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acaae4"></a> `00acaae4` | `08 75 1e 53` | lsl w8,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acaae8"></a> `00acaae8` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00acaaec"></a> `00acaaec` | `04 b1 89 1a` | csel w4,w8,w9,lt | `FALL_THROUGH`
<a id="insn-00acaaf0"></a> `00acaaf0` | `1f 74 e6 97` | bl 0x00467b6c | `UNCONDITIONAL_CALL`
<a id="insn-00acaaf4"></a> `00acaaf4` | `97 1a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acaaf8"></a> `00acaaf8` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-00acaafc"></a> `00acaafc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00acab00"></a> `00acab00` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acab04"></a> `00acab04` | `f3 03 08 4b` | neg w19,w8 | `FALL_THROUGH`
<a id="insn-00acab08"></a> `00acab08` | `92 1a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acab0c"></a> `00acab0c` | `be 87 e6 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-00acab10"></a> `00acab10` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00acab14"></a> `00acab14` | `8f 1a f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00acab18"></a> `00acab18` | `eb 87 e6 97` | bl 0x0046cac4 | `UNCONDITIONAL_CALL`
<a id="insn-00acab1c"></a> `00acab1c` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-00acab20"></a> `00acab20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acab24"></a> `00acab24` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acab28"></a> `00acab28` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00acab2c"></a> `00acab2c` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00acab30"></a> `00acab30` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acab34"></a> `00acab34` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acab38"></a> `00acab38` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acab3c"></a> `00acab3c` | `16 75 e6 17` | b 0x00467f94 | `CALL_TERMINATOR`
<a id="insn-00acab40"></a> `00acab40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaaa8`](#insn-00acaaa8) 範囲 `[['00acaaa8', '00acaaaf']]`
  - `CONDITIONAL_JUMP` [`00acaaac`](#insn-00acaaac) → [`00acab40`](#insn-00acab40)
  - `FALL_THROUGH` [`00acaaac`](#insn-00acaaac) → [`00acaab0`](#insn-00acaab0)
- ブロック [`00acaab0`](#insn-00acaab0) 範囲 `[['00acaab0', '00acab3f']]`
- ブロック [`00acab40`](#insn-00acab40) 範囲 `[['00acab40', '00acab43']]`

## 命令位置別の参照

- [`00acaaac`](#insn-00acaaac) → [`00acab40`](#insn-00acab40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaab0`](#insn-00acaab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaab4`](#insn-00acaab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaab8`](#insn-00acaab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaac4`](#insn-00acaac4) → [`004678a0`](../00467/004678a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004678a0` · 推定シンボル `None` · 推定型 `None`
- [`00acaaf0`](#insn-00acaaf0) → [`00467b6c`](../00467/00467b6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b6c` · 推定シンボル `None` · 推定型 `None`
- [`00acaaf4`](#insn-00acaaf4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acab00`](#insn-00acab00) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00acab08`](#insn-00acab08) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acab0c`](#insn-00acab0c) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`00acab14`](#insn-00acab14) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00acab18`](#insn-00acab18) → [`0046cac4`](../0046c/0046cac4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cac4` · 推定シンボル `None` · 推定型 `None`
- [`00acab30`](#insn-00acab30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab34`](#insn-00acab34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab38`](#insn-00acab38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acab3c`](#insn-00acab3c) → [`00467f94`](../00467/00467f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f94` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaaac`](#insn-00acaaac)

~~~json
{
  "source": "00acaaac",
  "target": "00acab40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaab0`](#insn-00acaab0)

~~~json
{
  "source": "00acaab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaab4`](#insn-00acaab4)

~~~json
{
  "source": "00acaab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaab8`](#insn-00acaab8)

~~~json
{
  "source": "00acaab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaac4`](#insn-00acaac4)

~~~json
{
  "source": "00acaac4",
  "target": "004678a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaaf0`](#insn-00acaaf0)

~~~json
{
  "source": "00acaaf0",
  "target": "00467b6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaaf4`](#insn-00acaaf4)

~~~json
{
  "source": "00acaaf4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab00`](#insn-00acab00)

~~~json
{
  "source": "00acab00",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "48c26a002c780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acab08`](#insn-00acab08)

~~~json
{
  "source": "00acab08",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab0c`](#insn-00acab0c)

~~~json
{
  "source": "00acab0c",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab14`](#insn-00acab14)

~~~json
{
  "source": "00acab14",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab18`](#insn-00acab18)

~~~json
{
  "source": "00acab18",
  "target": "0046cac4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acab30`](#insn-00acab30)

~~~json
{
  "source": "00acab30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab34`](#insn-00acab34)

~~~json
{
  "source": "00acab34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab38`](#insn-00acab38)

~~~json
{
  "source": "00acab38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acab3c`](#insn-00acab3c)

~~~json
{
  "source": "00acab3c",
  "target": "00467f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
