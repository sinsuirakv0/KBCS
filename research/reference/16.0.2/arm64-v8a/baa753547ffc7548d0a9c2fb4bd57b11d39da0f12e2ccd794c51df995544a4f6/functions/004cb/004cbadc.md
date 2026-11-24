# 004cbadc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004cba9c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0009.md#compare-49a146afe99110ce662ab7132081894c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004cbdfc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004cb/004cbdfc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0009.md#compare-80ae920471be812b1b1cb62ca49795e4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004cbadc",
  "name": "FUN_004cbadc",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac60836151a9c6309bad750ccce6a04e3d895912e15085e6d631feba598b93d2",
  "source_text_sha256": "ac60836151a9c6309bad750ccce6a04e3d895912e15085e6d631feba598b93d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004cbadc",
        "004cbc4b"
      ],
      [
        "004cbc8c",
        "004cbc8f"
      ]
    ],
    "bytes_sha256": "58c2b08c964b1075724f0813c3cf780f527bebe46a183c2d4a49346eb2641b07",
    "instruction_count": 93,
    "instruction_bytes": 372,
    "body_bytes": 372,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004c130c](../004c1/004c130c.md)
- [00530dfc](../00530/00530dfc.md)

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58b00](../00c58/00c58b00.md)
- [00c58b10](../00c58/00c58b10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2077 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_004cbadc(long *param_1)

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
  *param_1 = (long)(PTR__ZTVN5Botan16MDx_HashFunctionE_00c9b008 + 0x10);
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[1] = 0;
  pvVar5 = calloc(0x40,1);
  if (pvVar5 == (void *)0x0) {
    uVar7 = __cxa_allocate_exception(8);
    if (*(long *)(lVar1 + 0x28) == lVar8) {
      _ZNSt9bad_allocC1Ev();
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9aeb8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9aec0);
    }
  }
  else {
    param_1[2] = (long)pvVar5 + 0x40;
    param_1[3] = (long)pvVar5 + 0x40;
    *(undefined2 *)(param_1 + 6) = 0x101;
    param_1[4] = 0;
    param_1[7] = 8;
    puVar4 = PTR__ZTVN5Botan7SHA_256E_00c9b020;
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
        __cxa_throw(uVar7,PTR__ZTISt9bad_alloc_00c9aeb8,PTR__ZNSt20bad_array_new_lengthD1Ev_00c9aec0
                   );
      }
    }
    else {
      param_1[4] = 0;
      param_1[5] = 0;
      param_1[8] = (long)puVar6;
      param_1[9] = (long)(puVar6 + 4);
      param_1[10] = (long)(puVar6 + 4);
      uVar3 = _DAT_002c31a0;
      uVar2 = _UNK_002c2d38;
      uVar7 = _DAT_002c2d30;
      puVar6[1] = _UNK_002c31a8;
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
<a id="insn-004cbadc"></a> `004cbadc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004cbae0"></a> `004cbae0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cbae4"></a> `004cbae4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cbae8"></a> `004cbae8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cbaec"></a> `004cbaec` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004cbaf0"></a> `004cbaf0` | `88 3e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbaf4"></a> `004cbaf4` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004cbaf8"></a> `004cbaf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cbafc"></a> `004cbafc` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004cbb00"></a> `004cbb00` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbb04"></a> `004cbb04` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-004cbb08"></a> `004cbb08` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004cbb0c"></a> `004cbb0c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbb10"></a> `004cbb10` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-004cbb14"></a> `004cbb14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-004cbb18"></a> `004cbb18` | `1f 7c 01 a9` | stp xzr,xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004cbb1c"></a> `004cbb1c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-004cbb20"></a> `004cbb20` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-004cbb24"></a> `004cbb24` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cbb28"></a> `004cbb28` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cbb2c"></a> `004cbb2c` | `f5 33 1e 94` | bl 0x00c58b00 | `UNCONDITIONAL_CALL`
<a id="insn-004cbb30"></a> `004cbb30` | `20 05 00 b4` | cbz x0,0x004cbbd4 | `CONDITIONAL_JUMP`
<a id="insn-004cbb34"></a> `004cbb34` | `08 00 01 91` | add x8,x0,#0x40 | `FALL_THROUGH`
<a id="insn-004cbb38"></a> `004cbb38` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-004cbb3c"></a> `004cbb3c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-004cbb40"></a> `004cbb40` | `68 22 01 a9` | stp x8,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004cbb44"></a> `004cbb44` | `28 20 80 52` | mov w8,#0x101 | `FALL_THROUGH`
<a id="insn-004cbb48"></a> `004cbb48` | `68 62 00 79` | strh w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-004cbb4c"></a> `004cbb4c` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-004cbb50"></a> `004cbb50` | `bf 0e 02 f8` | str xzr,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-004cbb54"></a> `004cbb54` | `68 1e 00 f9` | str x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-004cbb58"></a> `004cbb58` | `88 3e 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004cbb5c"></a> `004cbb5c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004cbb60"></a> `004cbb60` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-004cbb64"></a> `004cbb64` | `7f fe 04 a9` | stp xzr,xzr,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-004cbb68"></a> `004cbb68` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004cbb6c"></a> `004cbb6c` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004cbb70"></a> `004cbb70` | `68 02 00 a9` | stp x8,x0,[x19] | `FALL_THROUGH`
<a id="insn-004cbb74"></a> `004cbb74` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004cbb78"></a> `004cbb78` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbb7c"></a> `004cbb7c` | `1f 0d 04 f8` | str xzr,[x8, #0x40]! | `FALL_THROUGH`
<a id="insn-004cbb80"></a> `004cbb80` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004cbb84"></a> `004cbb84` | `df 33 1e 94` | bl 0x00c58b00 | `UNCONDITIONAL_CALL`
<a id="insn-004cbb88"></a> `004cbb88` | `40 04 00 b4` | cbz x0,0x004cbc10 | `CONDITIONAL_JUMP`
<a id="insn-004cbb8c"></a> `004cbb8c` | `08 80 00 91` | add x8,x0,#0x20 | `FALL_THROUGH`
<a id="insn-004cbb90"></a> `004cbb90` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-004cbb94"></a> `004cbb94` | `60 22 04 a9` | stp x0,x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-004cbb98"></a> `004cbb98` | `68 2a 00 f9` | str x8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-004cbb9c"></a> `004cbb9c` | `c8 ef ff 90` | adrp x8,0x2c3000 | `FALL_THROUGH`
<a id="insn-004cbba0"></a> `004cbba0` | `00 69 c0 3d` | ldr q0,[x8, #0x1a0] | `FALL_THROUGH`
<a id="insn-004cbba4"></a> `004cbba4` | `a8 ef ff f0` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-004cbba8"></a> `004cbba8` | `01 4d c3 3d` | ldr q1,[x8, #0xd30] | `FALL_THROUGH`
<a id="insn-004cbbac"></a> `004cbbac` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-004cbbb0"></a> `004cbbb0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbbb4"></a> `004cbbb4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbbb8"></a> `004cbbb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbbbc"></a> `004cbbbc` | `81 06 00 54` | b.ne 0x004cbc8c | `CONDITIONAL_JUMP`
<a id="insn-004cbbc0"></a> `004cbbc0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004cbbc4"></a> `004cbbc4` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004cbbc8"></a> `004cbbc8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004cbbcc"></a> `004cbbcc` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004cbbd0"></a> `004cbbd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cbbd4"></a> `004cbbd4` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbbd8"></a> `004cbbd8` | `fa 30 1e 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbbdc"></a> `004cbbdc` | `f4 03 00 f9` | str x20,[sp] | `FALL_THROUGH`
<a id="insn-004cbbe0"></a> `004cbbe0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbbe4"></a> `004cbbe4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbbe8"></a> `004cbbe8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbbec"></a> `004cbbec` | `01 05 00 54` | b.ne 0x004cbc8c | `CONDITIONAL_JUMP`
<a id="insn-004cbbf0"></a> `004cbbf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004cbbf4"></a> `004cbbf4` | `c7 33 1e 94` | bl 0x00c58b10 | `UNCONDITIONAL_CALL`
<a id="insn-004cbbf8"></a> `004cbbf8` | `61 3e 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004cbbfc"></a> `004cbbfc` | `62 3e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-004cbc00"></a> `004cbc00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004cbc04"></a> `004cbc04` | `21 5c 47 f9` | ldr x1,[x1, #0xeb8] | `FALL_THROUGH`
<a id="insn-004cbc08"></a> `004cbc08` | `42 60 47 f9` | ldr x2,[x2, #0xec0] | `FALL_THROUGH`
<a id="insn-004cbc0c"></a> `004cbc0c` | `f5 30 1e 94` | bl 0x00c57fe0 | `CALL_TERMINATOR`
<a id="insn-004cbc10"></a> `004cbc10` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-004cbc14"></a> `004cbc14` | `eb 30 1e 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004cbc18"></a> `004cbc18` | `f4 03 00 f9` | str x20,[sp] | `FALL_THROUGH`
<a id="insn-004cbc1c"></a> `004cbc1c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004cbc20"></a> `004cbc20` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004cbc24"></a> `004cbc24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004cbc28"></a> `004cbc28` | `21 03 00 54` | b.ne 0x004cbc8c | `CONDITIONAL_JUMP`
<a id="insn-004cbc2c"></a> `004cbc2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004cbc30"></a> `004cbc30` | `b8 33 1e 94` | bl 0x00c58b10 | `UNCONDITIONAL_CALL`
<a id="insn-004cbc34"></a> `004cbc34` | `61 3e 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004cbc38"></a> `004cbc38` | `62 3e 00 f0` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-004cbc3c"></a> `004cbc3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004cbc40"></a> `004cbc40` | `21 5c 47 f9` | ldr x1,[x1, #0xeb8] | `FALL_THROUGH`
<a id="insn-004cbc44"></a> `004cbc44` | `42 60 47 f9` | ldr x2,[x2, #0xec0] | `FALL_THROUGH`
<a id="insn-004cbc48"></a> `004cbc48` | `e6 30 1e 94` | bl 0x00c57fe0 | `CALL_TERMINATOR`
<a id="insn-004cbc8c"></a> `004cbc8c` | `c9 30 1e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004cbadc`](#insn-004cbadc) 範囲 `[['004cbadc', '004cbb33']]`
  - `CONDITIONAL_JUMP` [`004cbb30`](#insn-004cbb30) → [`004cbbd4`](#insn-004cbbd4)
  - `FALL_THROUGH` [`004cbb30`](#insn-004cbb30) → [`004cbb34`](#insn-004cbb34)
- ブロック [`004cbb34`](#insn-004cbb34) 範囲 `[['004cbb34', '004cbb8b']]`
  - `CONDITIONAL_JUMP` [`004cbb88`](#insn-004cbb88) → [`004cbc10`](#insn-004cbc10)
  - `FALL_THROUGH` [`004cbb88`](#insn-004cbb88) → [`004cbb8c`](#insn-004cbb8c)
- ブロック [`004cbb8c`](#insn-004cbb8c) 範囲 `[['004cbb8c', '004cbbbf']]`
  - `CONDITIONAL_JUMP` [`004cbbbc`](#insn-004cbbbc) → [`004cbc8c`](#insn-004cbc8c)
  - `FALL_THROUGH` [`004cbbbc`](#insn-004cbbbc) → [`004cbbc0`](#insn-004cbbc0)
- ブロック [`004cbbc0`](#insn-004cbbc0) 範囲 `[['004cbbc0', '004cbbd3']]`
- ブロック [`004cbbd4`](#insn-004cbbd4) 範囲 `[['004cbbd4', '004cbbef']]`
  - `CONDITIONAL_JUMP` [`004cbbec`](#insn-004cbbec) → [`004cbc8c`](#insn-004cbc8c)
  - `FALL_THROUGH` [`004cbbec`](#insn-004cbbec) → [`004cbbf0`](#insn-004cbbf0)
- ブロック [`004cbbf0`](#insn-004cbbf0) 範囲 `[['004cbbf0', '004cbc0f']]`
- ブロック [`004cbc10`](#insn-004cbc10) 範囲 `[['004cbc10', '004cbc2b']]`
  - `CONDITIONAL_JUMP` [`004cbc28`](#insn-004cbc28) → [`004cbc8c`](#insn-004cbc8c)
  - `FALL_THROUGH` [`004cbc28`](#insn-004cbc28) → [`004cbc2c`](#insn-004cbc2c)
- ブロック [`004cbc2c`](#insn-004cbc2c) 範囲 `[['004cbc2c', '004cbc4b']]`
- ブロック [`004cbc8c`](#insn-004cbc8c) 範囲 `[['004cbc8c', '004cbc8f']]`

## 命令位置別の参照

- [`004cbae0`](#insn-004cbae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbae4`](#insn-004cbae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbae8`](#insn-004cbae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbafc`](#insn-004cbafc) → `00c9b008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbb0c`](#insn-004cbb0c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb10`](#insn-004cbb10) → `00c66da8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004cbb24`](#insn-004cbb24) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb28`](#insn-004cbb28) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb2c`](#insn-004cbb2c) → [`00c58b00`](../00c58/00c58b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b00` · 推定シンボル `None` · 推定型 `None`
- [`004cbb30`](#insn-004cbb30) → [`004cbbd4`](#insn-004cbbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb5c`](#insn-004cbb5c) → `00c9b020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbb6c`](#insn-004cbb6c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb70`](#insn-004cbb70) → `00c688f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004cbb80`](#insn-004cbb80) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbb84`](#insn-004cbb84) → [`00c58b00`](../00c58/00c58b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b00` · 推定シンボル `None` · 推定型 `None`
- [`004cbb88`](#insn-004cbb88) → [`004cbc10`](#insn-004cbc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbba0`](#insn-004cbba0) → `002c31a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbba8`](#insn-004cbba8) → `002c2d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbb4`](#insn-004cbbb4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbbc`](#insn-004cbbbc) → [`004cbc8c`](#insn-004cbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbc0`](#insn-004cbbc0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbc4`](#insn-004cbbc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbc8`](#insn-004cbbc8) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbd8`](#insn-004cbbd8) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004cbbdc`](#insn-004cbbdc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbe4`](#insn-004cbbe4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbec`](#insn-004cbbec) → [`004cbc8c`](#insn-004cbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbbf4`](#insn-004cbbf4) → [`00c58b10`](../00c58/00c58b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b10` · 推定シンボル `None` · 推定型 `None`
- [`004cbc04`](#insn-004cbc04) → `00c9aeb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbc04`](#insn-004cbc04) → `00c96768`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`004cbc08`](#insn-004cbc08) → `00c9aec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbc08`](#insn-004cbc08) → [`00c37c40`](../00c37/00c37c40.md) · `PARAM` · `ANALYSIS` · 関数 `00c37c40` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`004cbc0c`](#insn-004cbc0c) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`004cbc14`](#insn-004cbc14) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004cbc18`](#insn-004cbc18) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbc20`](#insn-004cbc20) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbc28`](#insn-004cbc28) → [`004cbc8c`](#insn-004cbc8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cbc30`](#insn-004cbc30) → [`00c58b10`](../00c58/00c58b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b10` · 推定シンボル `None` · 推定型 `None`
- [`004cbc40`](#insn-004cbc40) → `00c9aeb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbc40`](#insn-004cbc40) → `00c96768`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTISt9bad_alloc` · 推定型 `pointer __((offset(0x10)))`
- [`004cbc44`](#insn-004cbc44) → `00c9aec0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004cbc44`](#insn-004cbc44) → [`00c37c40`](../00c37/00c37c40.md) · `PARAM` · `ANALYSIS` · 関数 `00c37c40` · 推定シンボル `_ZNSt20bad_array_new_lengthD1Ev` · 推定型 `None`
- [`004cbc48`](#insn-004cbc48) → [`00c57fe0`](../00c57/00c57fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fe0` · 推定シンボル `None` · 推定型 `None`
- [`004cbc8c`](#insn-004cbc8c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cbae0`](#insn-004cbae0)

~~~json
{
  "source": "004cbae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbae4`](#insn-004cbae4)

~~~json
{
  "source": "004cbae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbae8`](#insn-004cbae8)

~~~json
{
  "source": "004cbae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbafc`](#insn-004cbafc)

~~~json
{
  "source": "004cbafc",
  "target": "00c9b008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbb0c`](#insn-004cbb0c)

~~~json
{
  "source": "004cbb0c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb10`](#insn-004cbb10)

~~~json
{
  "source": "004cbb10",
  "target": "00c66da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66d98",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004cbb24`](#insn-004cbb24)

~~~json
{
  "source": "004cbb24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb28`](#insn-004cbb28)

~~~json
{
  "source": "004cbb28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb2c`](#insn-004cbb2c)

~~~json
{
  "source": "004cbb2c",
  "target": "00c58b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbb30`](#insn-004cbb30)

~~~json
{
  "source": "004cbb30",
  "target": "004cbbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb5c`](#insn-004cbb5c)

~~~json
{
  "source": "004cbb5c",
  "target": "00c9b020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b020",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbb6c`](#insn-004cbb6c)

~~~json
{
  "source": "004cbb6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb70`](#insn-004cbb70)

~~~json
{
  "source": "004cbb70",
  "target": "00c688f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c688e8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004cbb80`](#insn-004cbb80)

~~~json
{
  "source": "004cbb80",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbb84`](#insn-004cbb84)

~~~json
{
  "source": "004cbb84",
  "target": "00c58b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbb88`](#insn-004cbb88)

~~~json
{
  "source": "004cbb88",
  "target": "004cbc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbba0`](#insn-004cbba0)

~~~json
{
  "source": "004cbba0",
  "target": "002c31a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbba8`](#insn-004cbba8)

~~~json
{
  "source": "004cbba8",
  "target": "002c2d30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbb4`](#insn-004cbbb4)

~~~json
{
  "source": "004cbbb4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbbc`](#insn-004cbbbc)

~~~json
{
  "source": "004cbbbc",
  "target": "004cbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbc0`](#insn-004cbbc0)

~~~json
{
  "source": "004cbbc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbc4`](#insn-004cbbc4)

~~~json
{
  "source": "004cbbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbc8`](#insn-004cbbc8)

~~~json
{
  "source": "004cbbc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbd8`](#insn-004cbbd8)

~~~json
{
  "source": "004cbbd8",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbbdc`](#insn-004cbbdc)

~~~json
{
  "source": "004cbbdc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbe4`](#insn-004cbbe4)

~~~json
{
  "source": "004cbbe4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbec`](#insn-004cbbec)

~~~json
{
  "source": "004cbbec",
  "target": "004cbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbbf4`](#insn-004cbbf4)

~~~json
{
  "source": "004cbbf4",
  "target": "00c58b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc04`](#insn-004cbc04)

~~~json
{
  "source": "004cbc04",
  "target": "00c9aeb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aeb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc04`](#insn-004cbc04)

~~~json
{
  "source": "004cbc04",
  "target": "00c96768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c96768",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc08`](#insn-004cbc08)

~~~json
{
  "source": "004cbc08",
  "target": "00c9aec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aec0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc08`](#insn-004cbc08)

~~~json
{
  "source": "004cbc08",
  "target": "00c37c40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc0c`](#insn-004cbc0c)

~~~json
{
  "source": "004cbc0c",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc14`](#insn-004cbc14)

~~~json
{
  "source": "004cbc14",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc18`](#insn-004cbc18)

~~~json
{
  "source": "004cbc18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbc20`](#insn-004cbc20)

~~~json
{
  "source": "004cbc20",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbc28`](#insn-004cbc28)

~~~json
{
  "source": "004cbc28",
  "target": "004cbc8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cbc30`](#insn-004cbc30)

~~~json
{
  "source": "004cbc30",
  "target": "00c58b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc40`](#insn-004cbc40)

~~~json
{
  "source": "004cbc40",
  "target": "00c9aeb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aeb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc40`](#insn-004cbc40)

~~~json
{
  "source": "004cbc40",
  "target": "00c96768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c96768",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc44`](#insn-004cbc44)

~~~json
{
  "source": "004cbc44",
  "target": "00c9aec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aec0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004cbc44`](#insn-004cbc44)

~~~json
{
  "source": "004cbc44",
  "target": "00c37c40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc48`](#insn-004cbc48)

~~~json
{
  "source": "004cbc48",
  "target": "00c57fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004cbc8c`](#insn-004cbc8c)

~~~json
{
  "source": "004cbc8c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
