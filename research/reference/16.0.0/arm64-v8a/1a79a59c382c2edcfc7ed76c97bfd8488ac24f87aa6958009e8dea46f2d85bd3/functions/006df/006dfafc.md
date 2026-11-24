# 006dfafc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006b5d40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5d40.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0030.md#compare-d85ccdff9ba1cde053364e622b040c75)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006dfb3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfb3c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0021.md#compare-6cc4b64e18c6b00f0195b459efe200af)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dfafc",
  "name": "FUN_006dfafc",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "794589466efc653df72ecff127872efd03fccb0b08fc3de3485f0f8373dfc0a6",
  "source_text_sha256": "794589466efc653df72ecff127872efd03fccb0b08fc3de3485f0f8373dfc0a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006dfafc",
        "006dfbeb"
      ]
    ],
    "bytes_sha256": "094e5829dd9ed68b0c32c62bebed8f464cb177cf53bb35e1a8f8cc7bc300c10c",
    "instruction_count": 60,
    "instruction_bytes": 240,
    "body_bytes": 240,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006f2494](../006f2/006f2494.md)
- [00716d50](../00716/00716d50.md)
- [008c5c08](../008c5/008c5c08.md)
- [009470d0](../00947/009470d0.md)
- [009d0184](../009d0/009d0184.md)
- [00aeab6c](../00aea/00aeab6c.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00470800](../00470/00470800.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1392 bytes

~~~c

void FUN_006dfafc(undefined8 *param_1,undefined4 *param_2)

{
  ulong uVar1;
  undefined4 *puVar2;
  undefined4 *puVar3;
  void *__dest;
  ulong uVar4;
  ulong uVar5;
  void *__src;
  long lVar6;
  undefined4 *puVar7;
  
  puVar3 = (undefined4 *)param_1[1];
  if (puVar3 < (undefined4 *)param_1[2]) {
    puVar7 = puVar3 + 1;
    *puVar3 = *param_2;
  }
  else {
    __src = (void *)*param_1;
    lVar6 = (long)puVar3 - (long)__src >> 2;
    uVar1 = lVar6 + 1;
    if (uVar1 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470800(param_1);
    }
    uVar4 = (long)param_1[2] - (long)__src;
    uVar5 = (long)uVar4 >> 1;
    if (uVar5 <= uVar1) {
      uVar5 = uVar1;
    }
    if (0x7ffffffffffffffb < uVar4) {
      uVar5 = 0x3fffffffffffffff;
    }
    if (uVar5 == 0) {
      __dest = (void *)0x0;
    }
    else {
      if (uVar5 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
        FUN_00440e80();
      }
      __dest = (void *)_Znwm(uVar5 << 2);
    }
    puVar2 = (undefined4 *)((long)__dest + lVar6 * 4);
    puVar7 = puVar2 + 1;
    *puVar2 = *param_2;
    memcpy(__dest,__src,(long)puVar3 - (long)__src);
    *param_1 = __dest;
    param_1[1] = puVar7;
    param_1[2] = (void *)((long)__dest + uVar5 * 4);
    if (__src != (void *)0x0) {
      _ZdlPv(__src);
    }
  }
  param_1[1] = puVar7;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006dfafc"></a> `006dfafc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-006dfb00"></a> `006dfb00` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dfb04"></a> `006dfb04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dfb08"></a> `006dfb08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dfb0c"></a> `006dfb0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006dfb10"></a> `006dfb10` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006dfb14"></a> `006dfb14` | `17 a0 40 a9` | ldp x23,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-006dfb18"></a> `006dfb18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006dfb1c"></a> `006dfb1c` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-006dfb20"></a> `006dfb20` | `82 00 00 54` | b.cs 0x006dfb30 | `CONDITIONAL_JUMP`
<a id="insn-006dfb24"></a> `006dfb24` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-006dfb28"></a> `006dfb28` | `e8 46 00 b8` | str w8,[x23], #0x4 | `FALL_THROUGH`
<a id="insn-006dfb2c"></a> `006dfb2c` | `26 00 00 14` | b 0x006dfbc4 | `UNCONDITIONAL_JUMP`
<a id="insn-006dfb30"></a> `006dfb30` | `74 02 40 f9` | ldr x20,[x19] | `FALL_THROUGH`
<a id="insn-006dfb34"></a> `006dfb34` | `f5 02 14 cb` | sub x21,x23,x20 | `FALL_THROUGH`
<a id="insn-006dfb38"></a> `006dfb38` | `b7 fe 42 93` | asr x23,x21,#0x2 | `FALL_THROUGH`
<a id="insn-006dfb3c"></a> `006dfb3c` | `e9 06 00 91` | add x9,x23,#0x1 | `FALL_THROUGH`
<a id="insn-006dfb40"></a> `006dfb40` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-006dfb44"></a> `006dfb44` | `ea 04 00 b5` | cbnz x10,0x006dfbe0 | `CONDITIONAL_JUMP`
<a id="insn-006dfb48"></a> `006dfb48` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-006dfb4c"></a> `006dfb4c` | `eb f3 7e b2` | orr x11,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-006dfb50"></a> `006dfb50` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006dfb54"></a> `006dfb54` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-006dfb58"></a> `006dfb58` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-006dfb5c"></a> `006dfb5c` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-006dfb60"></a> `006dfb60` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-006dfb64"></a> `006dfb64` | `38 31 88 9a` | csel x24,x9,x8,cc | `FALL_THROUGH`
<a id="insn-006dfb68"></a> `006dfb68` | `38 01 00 b4` | cbz x24,0x006dfb8c | `CONDITIONAL_JUMP`
<a id="insn-006dfb6c"></a> `006dfb6c` | `08 ff 7e d3` | lsr x8,x24,#0x3e | `FALL_THROUGH`
<a id="insn-006dfb70"></a> `006dfb70` | `c8 03 00 b5` | cbnz x8,0x006dfbe8 | `CONDITIONAL_JUMP`
<a id="insn-006dfb74"></a> `006dfb74` | `00 f7 7e d3` | lsl x0,x24,#0x2 | `FALL_THROUGH`
<a id="insn-006dfb78"></a> `006dfb78` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-006dfb7c"></a> `006dfb7c` | `c5 df 15 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-006dfb80"></a> `006dfb80` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-006dfb84"></a> `006dfb84` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-006dfb88"></a> `006dfb88` | `02 00 00 14` | b 0x006dfb90 | `UNCONDITIONAL_JUMP`
<a id="insn-006dfb8c"></a> `006dfb8c` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-006dfb90"></a> `006dfb90` | `d7 0a 17 8b` | add x23,x22,x23, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006dfb94"></a> `006dfb94` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-006dfb98"></a> `006dfb98` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-006dfb9c"></a> `006dfb9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006dfba0"></a> `006dfba0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-006dfba4"></a> `006dfba4` | `d8 0a 18 8b` | add x24,x22,x24, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006dfba8"></a> `006dfba8` | `e8 46 00 b8` | str w8,[x23], #0x4 | `FALL_THROUGH`
<a id="insn-006dfbac"></a> `006dfbac` | `15 e0 15 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-006dfbb0"></a> `006dfbb0` | `76 5e 00 a9` | stp x22,x23,[x19] | `FALL_THROUGH`
<a id="insn-006dfbb4"></a> `006dfbb4` | `78 0a 00 f9` | str x24,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-006dfbb8"></a> `006dfbb8` | `74 00 00 b4` | cbz x20,0x006dfbc4 | `CONDITIONAL_JUMP`
<a id="insn-006dfbbc"></a> `006dfbbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006dfbc0"></a> `006dfbc0` | `bc df 15 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006dfbc4"></a> `006dfbc4` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-006dfbc8"></a> `006dfbc8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006dfbcc"></a> `006dfbcc` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006dfbd0"></a> `006dfbd0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006dfbd4"></a> `006dfbd4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006dfbd8"></a> `006dfbd8` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-006dfbdc"></a> `006dfbdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006dfbe0"></a> `006dfbe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006dfbe4"></a> `006dfbe4` | `07 43 f6 97` | bl 0x00470800 | `CALL_TERMINATOR`
<a id="insn-006dfbe8"></a> `006dfbe8` | `a6 84 f5 97` | bl 0x00440e80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006dfafc`](#insn-006dfafc) 範囲 `[['006dfafc', '006dfb23']]`
  - `CONDITIONAL_JUMP` [`006dfb20`](#insn-006dfb20) → [`006dfb30`](#insn-006dfb30)
  - `FALL_THROUGH` [`006dfb20`](#insn-006dfb20) → [`006dfb24`](#insn-006dfb24)
- ブロック [`006dfb24`](#insn-006dfb24) 範囲 `[['006dfb24', '006dfb2f']]`
  - `UNCONDITIONAL_JUMP` [`006dfb2c`](#insn-006dfb2c) → [`006dfbc4`](#insn-006dfbc4)
- ブロック [`006dfb30`](#insn-006dfb30) 範囲 `[['006dfb30', '006dfb47']]`
  - `CONDITIONAL_JUMP` [`006dfb44`](#insn-006dfb44) → [`006dfbe0`](#insn-006dfbe0)
  - `FALL_THROUGH` [`006dfb44`](#insn-006dfb44) → [`006dfb48`](#insn-006dfb48)
- ブロック [`006dfb48`](#insn-006dfb48) 範囲 `[['006dfb48', '006dfb6b']]`
  - `CONDITIONAL_JUMP` [`006dfb68`](#insn-006dfb68) → [`006dfb8c`](#insn-006dfb8c)
  - `FALL_THROUGH` [`006dfb68`](#insn-006dfb68) → [`006dfb6c`](#insn-006dfb6c)
- ブロック [`006dfb6c`](#insn-006dfb6c) 範囲 `[['006dfb6c', '006dfb73']]`
  - `CONDITIONAL_JUMP` [`006dfb70`](#insn-006dfb70) → [`006dfbe8`](#insn-006dfbe8)
  - `FALL_THROUGH` [`006dfb70`](#insn-006dfb70) → [`006dfb74`](#insn-006dfb74)
- ブロック [`006dfb74`](#insn-006dfb74) 範囲 `[['006dfb74', '006dfb8b']]`
  - `UNCONDITIONAL_JUMP` [`006dfb88`](#insn-006dfb88) → [`006dfb90`](#insn-006dfb90)
- ブロック [`006dfb8c`](#insn-006dfb8c) 範囲 `[['006dfb8c', '006dfb8f']]`
  - `FALL_THROUGH` [`006dfb8c`](#insn-006dfb8c) → [`006dfb90`](#insn-006dfb90)
- ブロック [`006dfb90`](#insn-006dfb90) 範囲 `[['006dfb90', '006dfbbb']]`
  - `CONDITIONAL_JUMP` [`006dfbb8`](#insn-006dfbb8) → [`006dfbc4`](#insn-006dfbc4)
  - `FALL_THROUGH` [`006dfbb8`](#insn-006dfbb8) → [`006dfbbc`](#insn-006dfbbc)
- ブロック [`006dfbbc`](#insn-006dfbbc) 範囲 `[['006dfbbc', '006dfbc3']]`
  - `FALL_THROUGH` [`006dfbc0`](#insn-006dfbc0) → [`006dfbc4`](#insn-006dfbc4)
- ブロック [`006dfbc4`](#insn-006dfbc4) 範囲 `[['006dfbc4', '006dfbdf']]`
- ブロック [`006dfbe0`](#insn-006dfbe0) 範囲 `[['006dfbe0', '006dfbe7']]`
- ブロック [`006dfbe8`](#insn-006dfbe8) 範囲 `[['006dfbe8', '006dfbeb']]`

## 命令位置別の参照

- [`006dfafc`](#insn-006dfafc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb00`](#insn-006dfb00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb04`](#insn-006dfb04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb08`](#insn-006dfb08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb0c`](#insn-006dfb0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb20`](#insn-006dfb20) → [`006dfb30`](#insn-006dfb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb2c`](#insn-006dfb2c) → [`006dfbc4`](#insn-006dfbc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb44`](#insn-006dfb44) → [`006dfbe0`](#insn-006dfbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb68`](#insn-006dfb68) → [`006dfb8c`](#insn-006dfb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb70`](#insn-006dfb70) → [`006dfbe8`](#insn-006dfbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfb7c`](#insn-006dfb7c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`006dfb88`](#insn-006dfb88) → [`006dfb90`](#insn-006dfb90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbac`](#insn-006dfbac) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`006dfbb8`](#insn-006dfbb8) → [`006dfbc4`](#insn-006dfbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbc0`](#insn-006dfbc0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`006dfbc8`](#insn-006dfbc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbcc`](#insn-006dfbcc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbd0`](#insn-006dfbd0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbd4`](#insn-006dfbd4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbd8`](#insn-006dfbd8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006dfbe4`](#insn-006dfbe4) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`
- [`006dfbe8`](#insn-006dfbe8) → [`00440e80`](../00440/00440e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440e80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006dfafc`](#insn-006dfafc)

~~~json
{
  "source": "006dfafc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb00`](#insn-006dfb00)

~~~json
{
  "source": "006dfb00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb04`](#insn-006dfb04)

~~~json
{
  "source": "006dfb04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb08`](#insn-006dfb08)

~~~json
{
  "source": "006dfb08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb0c`](#insn-006dfb0c)

~~~json
{
  "source": "006dfb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb20`](#insn-006dfb20)

~~~json
{
  "source": "006dfb20",
  "target": "006dfb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb2c`](#insn-006dfb2c)

~~~json
{
  "source": "006dfb2c",
  "target": "006dfbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb44`](#insn-006dfb44)

~~~json
{
  "source": "006dfb44",
  "target": "006dfbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb68`](#insn-006dfb68)

~~~json
{
  "source": "006dfb68",
  "target": "006dfb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb70`](#insn-006dfb70)

~~~json
{
  "source": "006dfb70",
  "target": "006dfbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfb7c`](#insn-006dfb7c)

~~~json
{
  "source": "006dfb7c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfb88`](#insn-006dfb88)

~~~json
{
  "source": "006dfb88",
  "target": "006dfb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbac`](#insn-006dfbac)

~~~json
{
  "source": "006dfbac",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfbb8`](#insn-006dfbb8)

~~~json
{
  "source": "006dfbb8",
  "target": "006dfbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbc0`](#insn-006dfbc0)

~~~json
{
  "source": "006dfbc0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfbc8`](#insn-006dfbc8)

~~~json
{
  "source": "006dfbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbcc`](#insn-006dfbcc)

~~~json
{
  "source": "006dfbcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbd0`](#insn-006dfbd0)

~~~json
{
  "source": "006dfbd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbd4`](#insn-006dfbd4)

~~~json
{
  "source": "006dfbd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbd8`](#insn-006dfbd8)

~~~json
{
  "source": "006dfbd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006dfbe4`](#insn-006dfbe4)

~~~json
{
  "source": "006dfbe4",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006dfbe8`](#insn-006dfbe8)

~~~json
{
  "source": "006dfbe8",
  "target": "00440e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
