# 004cbdfc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004cbadc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cb/004cbadc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0009.md#compare-80ae920471be812b1b1cb62ca49795e4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cbdfc",
  "name": "FUN_004cbdfc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8d52722b0ef2ca74c4ea4a2e20c54653235568a1de1ee9d776d556c632056a7",
  "source_text_sha256": "c8d52722b0ef2ca74c4ea4a2e20c54653235568a1de1ee9d776d556c632056a7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cbdfc",
        "004cbf6b"
      ],
      [
        "004cbfac",
        "004cbfaf"
      ]
    ],
    "bytes_sha256": "6d862245bea66c248f07788141403f495fb541da7f299b705a4682b50afff8df",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004c162c](../004c1/004c162c.md)
- [0053111c](../00531/0053111c.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59ad0](../00c59/00c59ad0.md)
- [00c59ae0](../00c59/00c59ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2077 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_004cbdfc(long *param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined *puVar4;
  void *pvVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  long lVar8;
  
  lVar1 = tpidr_el0;
  lVar8 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan16MDx_HashFunctionE_00c9bfd8 + 0x10);
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[1] = 0;
  pvVar5 = calloc(0x40,1);
  if (pvVar5 == (void *)0x0) {
    uVar7 = __cxa_allocate_exception(8);
    if (*(long *)(lVar1 + 0x28) == lVar8) {
      _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9be88,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9be90);
    }
  }
  else {
    param_1[2] = (long)pvVar5 + 0x40;
    param_1[3] = (long)pvVar5 + 0x40;
    *(undefined2 *)(param_1 + 6) = 0x101;
    param_1[4] = 0;
    param_1[7] = 8;
    puVar4 = PTR__ZTVN5Botan7SHA_256E_00c9bff0;
    param_1[5] = 0;
    param_1[9] = 0;
    param_1[10] = 0;
    *param_1 = (long)(puVar4 + 0x10);
    param_1[1] = (long)pvVar5;
    param_1[8] = 0;
    puVar6 = calloc(8,4);
    if (puVar6 == (undefined8 *)0x0) {
      uVar7 = __cxa_allocate_exception(8);
      if (*(long *)(lVar1 + 0x28) == lVar8) {
        _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
        __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9be88,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9be90
                   );
      }
    }
    else {
      param_1[4] = 0;
      param_1[5] = 0;
      param_1[8] = (long)puVar6;
      param_1[9] = (long)(puVar6 + 4);
      param_1[10] = (long)(puVar6 + 4);
      uVar3 = _DAT_002c31f0;
      uVar2 = _UNK_002c2d88;
      uVar7 = _DAT_002c2d80;
      puVar6[1] = _UNK_002c31f8;
      *puVar6 = uVar3;
      puVar6[3] = uVar2;
      puVar6[2] = uVar7;
      if (*(long *)(lVar1 + 0x28) == lVar8) {
        return;
      }
    }
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004cbdfc"></a> `004cbdfc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004cbe00"></a> `004cbe00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cbe04"></a> `004cbe04` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cbe08"></a> `004cbe08` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cbe0c"></a> `004cbe0c` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004cbe10"></a> `004cbe10` | `88 3e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbe14"></a> `004cbe14` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004cbe18"></a> `004cbe18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cbe1c"></a> `004cbe1c` | `08 ed 47 f9` | ldr x8,[x8, #0xfd8] | `FALL_THROUGH`
<a id="insn-004cbe20"></a> `004cbe20` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbe24"></a> `004cbe24` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-004cbe28"></a> `004cbe28` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004cbe2c"></a> `004cbe2c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbe30"></a> `004cbe30` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-004cbe34"></a> `004cbe34` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-004cbe38"></a> `004cbe38` | `1f 7c 01 a9` | stp xzr,xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004cbe3c"></a> `004cbe3c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-004cbe40"></a> `004cbe40` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-004cbe44"></a> `004cbe44` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cbe48"></a> `004cbe48` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cbe4c"></a> `004cbe4c` | `21 37 1e 94` | bl 0x00c59ad0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbe50"></a> `004cbe50` | `20 05 00 b4` | cbz x0,0x004cbef4 | `CONDITIONAL_JUMP`
<a id="insn-004cbe54"></a> `004cbe54` | `08 00 01 91` | add x8,x0,#0x40 | `FALL_THROUGH`
<a id="insn-004cbe58"></a> `004cbe58` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-004cbe5c"></a> `004cbe5c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-004cbe60"></a> `004cbe60` | `68 22 01 a9` | stp x8,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cbe64"></a> `004cbe64` | `28 20 80 52` | mov w8,#0x101 | `FALL_THROUGH`
<a id="insn-004cbe68"></a> `004cbe68` | `68 62 00 79` | strh w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-004cbe6c"></a> `004cbe6c` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-004cbe70"></a> `004cbe70` | `bf 0e 02 f8` | str xzr,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-004cbe74"></a> `004cbe74` | `68 1e 00 f9` | str x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-004cbe78"></a> `004cbe78` | `88 3e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbe7c"></a> `004cbe7c` | `08 f9 47 f9` | ldr x8,[x8, #0xff0] | `FALL_THROUGH`
<a id="insn-004cbe80"></a> `004cbe80` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-004cbe84"></a> `004cbe84` | `7f fe 04 a9` | stp xzr,xzr,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-004cbe88"></a> `004cbe88` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004cbe8c"></a> `004cbe8c` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cbe90"></a> `004cbe90` | `68 02 00 a9` | stp x8,x0,[x19] | `FALL_THROUGH`
<a id="insn-004cbe94"></a> `004cbe94` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004cbe98"></a> `004cbe98` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbe9c"></a> `004cbe9c` | `1f 0d 04 f8` | str xzr,[x8, #0x40]! | `FALL_THROUGH`
<a id="insn-004cbea0"></a> `004cbea0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cbea4"></a> `004cbea4` | `0b 37 1e 94` | bl 0x00c59ad0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbea8"></a> `004cbea8` | `40 04 00 b4` | cbz x0,0x004cbf30 | `CONDITIONAL_JUMP`
<a id="insn-004cbeac"></a> `004cbeac` | `08 80 00 91` | add x8,x0,#0x20 | `FALL_THROUGH`
<a id="insn-004cbeb0"></a> `004cbeb0` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-004cbeb4"></a> `004cbeb4` | `60 22 04 a9` | stp x0,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-004cbeb8"></a> `004cbeb8` | `68 2a 00 f9` | str x8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-004cbebc"></a> `004cbebc` | `c8 ef ff 90` | adrp x8,0x2c3000 | `FALL_THROUGH`
<a id="insn-004cbec0"></a> `004cbec0` | `00 7d c0 3d` | ldr q0,[x8, #0x1f0] | `FALL_THROUGH`
<a id="insn-004cbec4"></a> `004cbec4` | `a8 ef ff f0` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-004cbec8"></a> `004cbec8` | `01 61 c3 3d` | ldr q1,[x8, #0xd80] | `FALL_THROUGH`
<a id="insn-004cbecc"></a> `004cbecc` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-004cbed0"></a> `004cbed0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbed4"></a> `004cbed4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbed8"></a> `004cbed8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbedc"></a> `004cbedc` | `81 06 00 54` | b.ne 0x004cbfac | `CONDITIONAL_JUMP`
<a id="insn-004cbee0"></a> `004cbee0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cbee4"></a> `004cbee4` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cbee8"></a> `004cbee8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cbeec"></a> `004cbeec` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004cbef0"></a> `004cbef0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cbef4"></a> `004cbef4` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbef8"></a> `004cbef8` | `26 34 1e 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-004cbefc"></a> `004cbefc` | `f4 03 00 f9` | str x20,[sp] | `FALL_THROUGH`
<a id="insn-004cbf00"></a> `004cbf00` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbf04"></a> `004cbf04` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbf08"></a> `004cbf08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbf0c"></a> `004cbf0c` | `01 05 00 54` | b.ne 0x004cbfac | `CONDITIONAL_JUMP`
<a id="insn-004cbf10"></a> `004cbf10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cbf14"></a> `004cbf14` | `f3 36 1e 94` | bl 0x00c59ae0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbf18"></a> `004cbf18` | `81 3e 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbf1c"></a> `004cbf1c` | `82 3e 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbf20"></a> `004cbf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cbf24"></a> `004cbf24` | `21 44 47 f9` | ldr x1,[x1, #0xe88] | `FALL_THROUGH`
<a id="insn-004cbf28"></a> `004cbf28` | `42 48 47 f9` | ldr x2,[x2, #0xe90] | `FALL_THROUGH`
<a id="insn-004cbf2c"></a> `004cbf2c` | `21 34 1e 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`
<a id="insn-004cbf30"></a> `004cbf30` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbf34"></a> `004cbf34` | `17 34 1e 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-004cbf38"></a> `004cbf38` | `f4 03 00 f9` | str x20,[sp] | `FALL_THROUGH`
<a id="insn-004cbf3c"></a> `004cbf3c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbf40"></a> `004cbf40` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbf44"></a> `004cbf44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbf48"></a> `004cbf48` | `21 03 00 54` | b.ne 0x004cbfac | `CONDITIONAL_JUMP`
<a id="insn-004cbf4c"></a> `004cbf4c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004cbf50"></a> `004cbf50` | `e4 36 1e 94` | bl 0x00c59ae0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbf54"></a> `004cbf54` | `81 3e 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbf58"></a> `004cbf58` | `82 3e 00 90` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbf5c"></a> `004cbf5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cbf60"></a> `004cbf60` | `21 44 47 f9` | ldr x1,[x1, #0xe88] | `FALL_THROUGH`
<a id="insn-004cbf64"></a> `004cbf64` | `42 48 47 f9` | ldr x2,[x2, #0xe90] | `FALL_THROUGH`
<a id="insn-004cbf68"></a> `004cbf68` | `12 34 1e 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`
<a id="insn-004cbfac"></a> `004cbfac` | `f5 33 1e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cbdfc`](#insn-004cbdfc) 範囲 `[['004cbdfc', '004cbe53']]`
  - `CONDITIONAL_JUMP` [`004cbe50`](#insn-004cbe50) → [`004cbef4`](#insn-004cbef4)
  - `FALL_THROUGH` [`004cbe50`](#insn-004cbe50) → [`004cbe54`](#insn-004cbe54)
- ブロック [`004cbe54`](#insn-004cbe54) 範囲 `[['004cbe54', '004cbeab']]`
  - `CONDITIONAL_JUMP` [`004cbea8`](#insn-004cbea8) → [`004cbf30`](#insn-004cbf30)
  - `FALL_THROUGH` [`004cbea8`](#insn-004cbea8) → [`004cbeac`](#insn-004cbeac)
- ブロック [`004cbeac`](#insn-004cbeac) 範囲 `[['004cbeac', '004cbedf']]`
  - `CONDITIONAL_JUMP` [`004cbedc`](#insn-004cbedc) → [`004cbfac`](#insn-004cbfac)
  - `FALL_THROUGH` [`004cbedc`](#insn-004cbedc) → [`004cbee0`](#insn-004cbee0)
- ブロック [`004cbee0`](#insn-004cbee0) 範囲 `[['004cbee0', '004cbef3']]`
- ブロック [`004cbef4`](#insn-004cbef4) 範囲 `[['004cbef4', '004cbf0f']]`
  - `CONDITIONAL_JUMP` [`004cbf0c`](#insn-004cbf0c) → [`004cbfac`](#insn-004cbfac)
  - `FALL_THROUGH` [`004cbf0c`](#insn-004cbf0c) → [`004cbf10`](#insn-004cbf10)
- ブロック [`004cbf10`](#insn-004cbf10) 範囲 `[['004cbf10', '004cbf2f']]`
- ブロック [`004cbf30`](#insn-004cbf30) 範囲 `[['004cbf30', '004cbf4b']]`
  - `CONDITIONAL_JUMP` [`004cbf48`](#insn-004cbf48) → [`004cbfac`](#insn-004cbfac)
  - `FALL_THROUGH` [`004cbf48`](#insn-004cbf48) → [`004cbf4c`](#insn-004cbf4c)
- ブロック [`004cbf4c`](#insn-004cbf4c) 範囲 `[['004cbf4c', '004cbf6b']]`
- ブロック [`004cbfac`](#insn-004cbfac) 範囲 `[['004cbfac', '004cbfaf']]`

## 命令位置別の参照

- [`004cbe00`](#insn-004cbe00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe04`](#insn-004cbe04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe08`](#insn-004cbe08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe1c`](#insn-004cbe1c) → `00c9bfd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbe2c`](#insn-004cbe2c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe30`](#insn-004cbe30) → `00c67d78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004cbe44`](#insn-004cbe44) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe48`](#insn-004cbe48) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe4c`](#insn-004cbe4c) → [`00c59ad0`](../00c59/00c59ad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ad0` · 推定シンボル `None` · 推定型 `None`
- [`004cbe50`](#insn-004cbe50) → [`004cbef4`](#insn-004cbef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe7c`](#insn-004cbe7c) → `00c9bff0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbe8c`](#insn-004cbe8c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbe90`](#insn-004cbe90) → `00c698c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004cbea0`](#insn-004cbea0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbea4`](#insn-004cbea4) → [`00c59ad0`](../00c59/00c59ad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ad0` · 推定シンボル `None` · 推定型 `None`
- [`004cbea8`](#insn-004cbea8) → [`004cbf30`](#insn-004cbf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbec0`](#insn-004cbec0) → `002c31f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbec8`](#insn-004cbec8) → `002c2d80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbed4`](#insn-004cbed4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbedc`](#insn-004cbedc) → [`004cbfac`](#insn-004cbfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbee0`](#insn-004cbee0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbee4`](#insn-004cbee4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbee8`](#insn-004cbee8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbef8`](#insn-004cbef8) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`004cbefc`](#insn-004cbefc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf04`](#insn-004cbf04) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf0c`](#insn-004cbf0c) → [`004cbfac`](#insn-004cbfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf14`](#insn-004cbf14) → [`00c59ae0`](../00c59/00c59ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ae0` · 推定シンボル `None` · 推定型 `None`
- [`004cbf24`](#insn-004cbf24) → `00c9be88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbf24`](#insn-004cbf24) → `00c97738`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`004cbf28`](#insn-004cbf28) → `00c9be90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbf28`](#insn-004cbf28) → [`00c38c34`](../00c38/00c38c34.md) · `PARAM` · `ANALYSIS` · 関数 `00c38c34` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`004cbf2c`](#insn-004cbf2c) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`
- [`004cbf34`](#insn-004cbf34) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`004cbf38`](#insn-004cbf38) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf40`](#insn-004cbf40) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf48`](#insn-004cbf48) → [`004cbfac`](#insn-004cbfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbf50`](#insn-004cbf50) → [`00c59ae0`](../00c59/00c59ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ae0` · 推定シンボル `None` · 推定型 `None`
- [`004cbf60`](#insn-004cbf60) → `00c9be88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbf60`](#insn-004cbf60) → `00c97738`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`004cbf64`](#insn-004cbf64) → `00c9be90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbf64`](#insn-004cbf64) → [`00c38c34`](../00c38/00c38c34.md) · `PARAM` · `ANALYSIS` · 関数 `00c38c34` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`004cbf68`](#insn-004cbf68) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`
- [`004cbfac`](#insn-004cbfac) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cbe00`](#insn-004cbe00)

~~~json
{
  "source": "004cbe00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe04`](#insn-004cbe04)

~~~json
{
  "source": "004cbe04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe08`](#insn-004cbe08)

~~~json
{
  "source": "004cbe08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe1c`](#insn-004cbe1c)

~~~json
{
  "source": "004cbe1c",
  "target": "00c9bfd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bfd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbe2c`](#insn-004cbe2c)

~~~json
{
  "source": "004cbe2c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe30`](#insn-004cbe30)

~~~json
{
  "source": "004cbe30",
  "target": "00c67d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67d68",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004cbe44`](#insn-004cbe44)

~~~json
{
  "source": "004cbe44",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe48`](#insn-004cbe48)

~~~json
{
  "source": "004cbe48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe4c`](#insn-004cbe4c)

~~~json
{
  "source": "004cbe4c",
  "target": "00c59ad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbe50`](#insn-004cbe50)

~~~json
{
  "source": "004cbe50",
  "target": "004cbef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe7c`](#insn-004cbe7c)

~~~json
{
  "source": "004cbe7c",
  "target": "00c9bff0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bff0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbe8c`](#insn-004cbe8c)

~~~json
{
  "source": "004cbe8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbe90`](#insn-004cbe90)

~~~json
{
  "source": "004cbe90",
  "target": "00c698c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c698b8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004cbea0`](#insn-004cbea0)

~~~json
{
  "source": "004cbea0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbea4`](#insn-004cbea4)

~~~json
{
  "source": "004cbea4",
  "target": "00c59ad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbea8`](#insn-004cbea8)

~~~json
{
  "source": "004cbea8",
  "target": "004cbf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbec0`](#insn-004cbec0)

~~~json
{
  "source": "004cbec0",
  "target": "002c31f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbec8`](#insn-004cbec8)

~~~json
{
  "source": "004cbec8",
  "target": "002c2d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbed4`](#insn-004cbed4)

~~~json
{
  "source": "004cbed4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbedc`](#insn-004cbedc)

~~~json
{
  "source": "004cbedc",
  "target": "004cbfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbee0`](#insn-004cbee0)

~~~json
{
  "source": "004cbee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbee4`](#insn-004cbee4)

~~~json
{
  "source": "004cbee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbee8`](#insn-004cbee8)

~~~json
{
  "source": "004cbee8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbef8`](#insn-004cbef8)

~~~json
{
  "source": "004cbef8",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbefc`](#insn-004cbefc)

~~~json
{
  "source": "004cbefc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf04`](#insn-004cbf04)

~~~json
{
  "source": "004cbf04",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf0c`](#insn-004cbf0c)

~~~json
{
  "source": "004cbf0c",
  "target": "004cbfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf14`](#insn-004cbf14)

~~~json
{
  "source": "004cbf14",
  "target": "00c59ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf24`](#insn-004cbf24)

~~~json
{
  "source": "004cbf24",
  "target": "00c9be88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf24`](#insn-004cbf24)

~~~json
{
  "source": "004cbf24",
  "target": "00c97738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c97738",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf28`](#insn-004cbf28)

~~~json
{
  "source": "004cbf28",
  "target": "00c9be90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf28`](#insn-004cbf28)

~~~json
{
  "source": "004cbf28",
  "target": "00c38c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf2c`](#insn-004cbf2c)

~~~json
{
  "source": "004cbf2c",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf34`](#insn-004cbf34)

~~~json
{
  "source": "004cbf34",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf38`](#insn-004cbf38)

~~~json
{
  "source": "004cbf38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf40`](#insn-004cbf40)

~~~json
{
  "source": "004cbf40",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf48`](#insn-004cbf48)

~~~json
{
  "source": "004cbf48",
  "target": "004cbfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbf50`](#insn-004cbf50)

~~~json
{
  "source": "004cbf50",
  "target": "00c59ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf60`](#insn-004cbf60)

~~~json
{
  "source": "004cbf60",
  "target": "00c9be88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf60`](#insn-004cbf60)

~~~json
{
  "source": "004cbf60",
  "target": "00c97738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c97738",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf64`](#insn-004cbf64)

~~~json
{
  "source": "004cbf64",
  "target": "00c9be90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbf64`](#insn-004cbf64)

~~~json
{
  "source": "004cbf64",
  "target": "00c38c34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbf68`](#insn-004cbf68)

~~~json
{
  "source": "004cbf68",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbfac`](#insn-004cbfac)

~~~json
{
  "source": "004cbfac",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
