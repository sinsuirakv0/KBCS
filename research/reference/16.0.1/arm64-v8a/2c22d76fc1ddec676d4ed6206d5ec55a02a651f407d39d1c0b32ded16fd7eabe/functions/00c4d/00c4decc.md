# 00c4decc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4daa4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0045.md#compare-57b8ebae5c9b2111dd43639bbdcda4eb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4df68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4df68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0045.md#compare-b1c59125ea0502b98a9f12b4fe5cea8f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4decc",
  "name": "FUN_00c4decc",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7472d3ae3451744060e35c8cc01ac7fa8882ddceb4bacf21d8d36fcdca157c76",
  "source_text_sha256": "7472d3ae3451744060e35c8cc01ac7fa8882ddceb4bacf21d8d36fcdca157c76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4decc",
        "00c4e037"
      ]
    ],
    "bytes_sha256": "203e2a02bf63950cebe6389c806492cad08b1369d8fbd3a64d39d290c8687671",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58000](../00c58/00c58000.md)
- [00c5a0a0](../00c5a/00c5a0a0.md)
- [00c5b140](../00c5b/00c5b140.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2108 bytes

~~~c

void FUN_00c4decc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  long lVar3;
  size_t __size;
  size_t sVar4;
  void *__src;
  long *plVar5;
  
  plVar5 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar5 + 0x20))(plVar5);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 2U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e2;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined2 *)((long)pvVar2 + lVar3) = 0x2820;
  lVar3 = param_2[1] + 2;
  param_2[1] = lVar3;
  sVar4 = *(size_t *)(param_1 + 0x20);
  if (sVar4 != 0) {
    __src = *(void **)(param_1 + 0x18);
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar3 + sVar4) {
      __size = param_2[2] * 2;
      uVar1 = lVar3 + sVar4 + 0x3e0;
      if (__size < uVar1 || __size - uVar1 == 0) {
        __size = uVar1;
      }
      param_2[2] = __size;
      pvVar2 = realloc(pvVar2,__size);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar3 = param_2[1];
    }
    memcpy((void *)((long)pvVar2 + lVar3),__src,sVar4);
    lVar3 = param_2[1] + sVar4;
    param_2[1] = lVar3;
  }
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e1;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x29;
  param_2[1] = param_2[1] + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4decc"></a> `00c4decc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4ded0"></a> `00c4ded0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4ded4"></a> `00c4ded4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ded8"></a> `00c4ded8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4dedc"></a> `00c4dedc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4dee0"></a> `00c4dee0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c4dee4"></a> `00c4dee4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4dee8"></a> `00c4dee8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4deec"></a> `00c4deec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4def0"></a> `00c4def0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4def4"></a> `00c4def4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4def8"></a> `00c4def8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4defc"></a> `00c4defc` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00c4df00"></a> `00c4df00` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4df04"></a> `00c4df04` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4df08"></a> `00c4df08` | `c0 00 00 54` | b.eq 0x00c4df20 | `CONDITIONAL_JUMP`
<a id="insn-00c4df0c"></a> `00c4df0c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c4df10"></a> `00c4df10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c4df14"></a> `00c4df14` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4df18"></a> `00c4df18` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4df1c"></a> `00c4df1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4df20"></a> `00c4df20` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4df24"></a> `00c4df24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4df28"></a> `00c4df28` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4df2c"></a> `00c4df2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4df30"></a> `00c4df30` | `49 01 00 54` | b.ls 0x00c4df58 | `CONDITIONAL_JUMP`
<a id="insn-00c4df34"></a> `00c4df34` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4df38"></a> `00c4df38` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00c4df3c"></a> `00c4df3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4df40"></a> `00c4df40` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4df44"></a> `00c4df44` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4df48"></a> `00c4df48` | `56 30 00 94` | bl 0x00c5a0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4df4c"></a> `00c4df4c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4df50"></a> `00c4df50` | `e0 06 00 b4` | cbz x0,0x00c4e02c | `CONDITIONAL_JUMP`
<a id="insn-00c4df54"></a> `00c4df54` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4df58"></a> `00c4df58` | `09 04 85 52` | mov w9,#0x2820 | `FALL_THROUGH`
<a id="insn-00c4df5c"></a> `00c4df5c` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c4df60"></a> `00c4df60` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4df64"></a> `00c4df64` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4df68"></a> `00c4df68` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4df6c"></a> `00c4df6c` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00c4df70"></a> `00c4df70` | `f5 02 00 b4` | cbz x21,0x00c4dfcc | `CONDITIONAL_JUMP`
<a id="insn-00c4df74"></a> `00c4df74` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4df78"></a> `00c4df78` | `09 01 15 8b` | add x9,x8,x21 | `FALL_THROUGH`
<a id="insn-00c4df7c"></a> `00c4df7c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c4df80"></a> `00c4df80` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4df84"></a> `00c4df84` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4df88"></a> `00c4df88` | `49 01 00 54` | b.ls 0x00c4dfb0 | `CONDITIONAL_JUMP`
<a id="insn-00c4df8c"></a> `00c4df8c` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4df90"></a> `00c4df90` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00c4df94"></a> `00c4df94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c4df98"></a> `00c4df98` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00c4df9c"></a> `00c4df9c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4dfa0"></a> `00c4dfa0` | `40 30 00 94` | bl 0x00c5a0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4dfa4"></a> `00c4dfa4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4dfa8"></a> `00c4dfa8` | `60 04 00 b4` | cbz x0,0x00c4e034 | `CONDITIONAL_JUMP`
<a id="insn-00c4dfac"></a> `00c4dfac` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4dfb0"></a> `00c4dfb0` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00c4dfb4"></a> `00c4dfb4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00c4dfb8"></a> `00c4dfb8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00c4dfbc"></a> `00c4dfbc` | `11 28 00 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00c4dfc0"></a> `00c4dfc0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4dfc4"></a> `00c4dfc4` | `08 01 15 8b` | add x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00c4dfc8"></a> `00c4dfc8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4dfcc"></a> `00c4dfcc` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4dfd0"></a> `00c4dfd0` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4dfd4"></a> `00c4dfd4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4dfd8"></a> `00c4dfd8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4dfdc"></a> `00c4dfdc` | `49 01 00 54` | b.ls 0x00c4e004 | `CONDITIONAL_JUMP`
<a id="insn-00c4dfe0"></a> `00c4dfe0` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c4dfe4"></a> `00c4dfe4` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4dfe8"></a> `00c4dfe8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4dfec"></a> `00c4dfec` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4dff0"></a> `00c4dff0` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4dff4"></a> `00c4dff4` | `2b 30 00 94` | bl 0x00c5a0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4dff8"></a> `00c4dff8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4dffc"></a> `00c4dffc` | `a0 01 00 b4` | cbz x0,0x00c4e030 | `CONDITIONAL_JUMP`
<a id="insn-00c4e000"></a> `00c4e000` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4e004"></a> `00c4e004` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00c4e008"></a> `00c4e008` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4e00c"></a> `00c4e00c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4e010"></a> `00c4e010` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4e014"></a> `00c4e014` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4e018"></a> `00c4e018` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4e01c"></a> `00c4e01c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4e020"></a> `00c4e020` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4e024"></a> `00c4e024` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4e028"></a> `00c4e028` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4e02c"></a> `00c4e02c` | `45 34 00 94` | bl 0x00c5b140 | `CALL_TERMINATOR`
<a id="insn-00c4e030"></a> `00c4e030` | `44 34 00 94` | bl 0x00c5b140 | `CALL_TERMINATOR`
<a id="insn-00c4e034"></a> `00c4e034` | `43 34 00 94` | bl 0x00c5b140 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4decc`](#insn-00c4decc) 範囲 `[['00c4decc', '00c4df0b']]`
  - `CONDITIONAL_JUMP` [`00c4df08`](#insn-00c4df08) → [`00c4df20`](#insn-00c4df20)
  - `FALL_THROUGH` [`00c4df08`](#insn-00c4df08) → [`00c4df0c`](#insn-00c4df0c)
- ブロック [`00c4df0c`](#insn-00c4df0c) 範囲 `[['00c4df0c', '00c4df1f']]`
  - `FALL_THROUGH` [`00c4df1c`](#insn-00c4df1c) → [`00c4df20`](#insn-00c4df20)
- ブロック [`00c4df20`](#insn-00c4df20) 範囲 `[['00c4df20', '00c4df33']]`
  - `CONDITIONAL_JUMP` [`00c4df30`](#insn-00c4df30) → [`00c4df58`](#insn-00c4df58)
  - `FALL_THROUGH` [`00c4df30`](#insn-00c4df30) → [`00c4df34`](#insn-00c4df34)
- ブロック [`00c4df34`](#insn-00c4df34) 範囲 `[['00c4df34', '00c4df53']]`
  - `CONDITIONAL_JUMP` [`00c4df50`](#insn-00c4df50) → [`00c4e02c`](#insn-00c4e02c)
  - `FALL_THROUGH` [`00c4df50`](#insn-00c4df50) → [`00c4df54`](#insn-00c4df54)
- ブロック [`00c4df54`](#insn-00c4df54) 範囲 `[['00c4df54', '00c4df57']]`
  - `FALL_THROUGH` [`00c4df54`](#insn-00c4df54) → [`00c4df58`](#insn-00c4df58)
- ブロック [`00c4df58`](#insn-00c4df58) 範囲 `[['00c4df58', '00c4df73']]`
  - `CONDITIONAL_JUMP` [`00c4df70`](#insn-00c4df70) → [`00c4dfcc`](#insn-00c4dfcc)
  - `FALL_THROUGH` [`00c4df70`](#insn-00c4df70) → [`00c4df74`](#insn-00c4df74)
- ブロック [`00c4df74`](#insn-00c4df74) 範囲 `[['00c4df74', '00c4df8b']]`
  - `CONDITIONAL_JUMP` [`00c4df88`](#insn-00c4df88) → [`00c4dfb0`](#insn-00c4dfb0)
  - `FALL_THROUGH` [`00c4df88`](#insn-00c4df88) → [`00c4df8c`](#insn-00c4df8c)
- ブロック [`00c4df8c`](#insn-00c4df8c) 範囲 `[['00c4df8c', '00c4dfab']]`
  - `CONDITIONAL_JUMP` [`00c4dfa8`](#insn-00c4dfa8) → [`00c4e034`](#insn-00c4e034)
  - `FALL_THROUGH` [`00c4dfa8`](#insn-00c4dfa8) → [`00c4dfac`](#insn-00c4dfac)
- ブロック [`00c4dfac`](#insn-00c4dfac) 範囲 `[['00c4dfac', '00c4dfaf']]`
  - `FALL_THROUGH` [`00c4dfac`](#insn-00c4dfac) → [`00c4dfb0`](#insn-00c4dfb0)
- ブロック [`00c4dfb0`](#insn-00c4dfb0) 範囲 `[['00c4dfb0', '00c4dfcb']]`
  - `FALL_THROUGH` [`00c4dfc8`](#insn-00c4dfc8) → [`00c4dfcc`](#insn-00c4dfcc)
- ブロック [`00c4dfcc`](#insn-00c4dfcc) 範囲 `[['00c4dfcc', '00c4dfdf']]`
  - `CONDITIONAL_JUMP` [`00c4dfdc`](#insn-00c4dfdc) → [`00c4e004`](#insn-00c4e004)
  - `FALL_THROUGH` [`00c4dfdc`](#insn-00c4dfdc) → [`00c4dfe0`](#insn-00c4dfe0)
- ブロック [`00c4dfe0`](#insn-00c4dfe0) 範囲 `[['00c4dfe0', '00c4dfff']]`
  - `CONDITIONAL_JUMP` [`00c4dffc`](#insn-00c4dffc) → [`00c4e030`](#insn-00c4e030)
  - `FALL_THROUGH` [`00c4dffc`](#insn-00c4dffc) → [`00c4e000`](#insn-00c4e000)
- ブロック [`00c4e000`](#insn-00c4e000) 範囲 `[['00c4e000', '00c4e003']]`
  - `FALL_THROUGH` [`00c4e000`](#insn-00c4e000) → [`00c4e004`](#insn-00c4e004)
- ブロック [`00c4e004`](#insn-00c4e004) 範囲 `[['00c4e004', '00c4e02b']]`
- ブロック [`00c4e02c`](#insn-00c4e02c) 範囲 `[['00c4e02c', '00c4e02f']]`
- ブロック [`00c4e030`](#insn-00c4e030) 範囲 `[['00c4e030', '00c4e033']]`
- ブロック [`00c4e034`](#insn-00c4e034) 範囲 `[['00c4e034', '00c4e037']]`

## 命令位置別の参照

- [`00c4ded0`](#insn-00c4ded0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ded4`](#insn-00c4ded4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ded8`](#insn-00c4ded8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4df08`](#insn-00c4df08) → [`00c4df20`](#insn-00c4df20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4df30`](#insn-00c4df30) → [`00c4df58`](#insn-00c4df58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4df48`](#insn-00c4df48) → [`00c5a0a0`](../00c5a/00c5a0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0a0` · 推定シンボル `None` · 推定型 `None`
- [`00c4df50`](#insn-00c4df50) → [`00c4e02c`](#insn-00c4e02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4df70`](#insn-00c4df70) → [`00c4dfcc`](#insn-00c4dfcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4df88`](#insn-00c4df88) → [`00c4dfb0`](#insn-00c4dfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4dfa0`](#insn-00c4dfa0) → [`00c5a0a0`](../00c5a/00c5a0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0a0` · 推定シンボル `None` · 推定型 `None`
- [`00c4dfa8`](#insn-00c4dfa8) → [`00c4e034`](#insn-00c4e034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4dfbc`](#insn-00c4dfbc) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00c4dfdc`](#insn-00c4dfdc) → [`00c4e004`](#insn-00c4e004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4dff4`](#insn-00c4dff4) → [`00c5a0a0`](../00c5a/00c5a0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0a0` · 推定シンボル `None` · 推定型 `None`
- [`00c4dffc`](#insn-00c4dffc) → [`00c4e030`](#insn-00c4e030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4e018`](#insn-00c4e018) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4e01c`](#insn-00c4e01c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4e020`](#insn-00c4e020) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4e02c`](#insn-00c4e02c) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4e030`](#insn-00c4e030) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4e034`](#insn-00c4e034) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4ded0`](#insn-00c4ded0)

~~~json
{
  "source": "00c4ded0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ded4`](#insn-00c4ded4)

~~~json
{
  "source": "00c4ded4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ded8`](#insn-00c4ded8)

~~~json
{
  "source": "00c4ded8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4df08`](#insn-00c4df08)

~~~json
{
  "source": "00c4df08",
  "target": "00c4df20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4df30`](#insn-00c4df30)

~~~json
{
  "source": "00c4df30",
  "target": "00c4df58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4df48`](#insn-00c4df48)

~~~json
{
  "source": "00c4df48",
  "target": "00c5a0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4df50`](#insn-00c4df50)

~~~json
{
  "source": "00c4df50",
  "target": "00c4e02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4df70`](#insn-00c4df70)

~~~json
{
  "source": "00c4df70",
  "target": "00c4dfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4df88`](#insn-00c4df88)

~~~json
{
  "source": "00c4df88",
  "target": "00c4dfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4dfa0`](#insn-00c4dfa0)

~~~json
{
  "source": "00c4dfa0",
  "target": "00c5a0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4dfa8`](#insn-00c4dfa8)

~~~json
{
  "source": "00c4dfa8",
  "target": "00c4e034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4dfbc`](#insn-00c4dfbc)

~~~json
{
  "source": "00c4dfbc",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4dfdc`](#insn-00c4dfdc)

~~~json
{
  "source": "00c4dfdc",
  "target": "00c4e004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4dff4`](#insn-00c4dff4)

~~~json
{
  "source": "00c4dff4",
  "target": "00c5a0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4dffc`](#insn-00c4dffc)

~~~json
{
  "source": "00c4dffc",
  "target": "00c4e030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4e018`](#insn-00c4e018)

~~~json
{
  "source": "00c4e018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4e01c`](#insn-00c4e01c)

~~~json
{
  "source": "00c4e01c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4e020`](#insn-00c4e020)

~~~json
{
  "source": "00c4e020",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4e02c`](#insn-00c4e02c)

~~~json
{
  "source": "00c4e02c",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4e030`](#insn-00c4e030)

~~~json
{
  "source": "00c4e030",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4e034`](#insn-00c4e034)

~~~json
{
  "source": "00c4e034",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
