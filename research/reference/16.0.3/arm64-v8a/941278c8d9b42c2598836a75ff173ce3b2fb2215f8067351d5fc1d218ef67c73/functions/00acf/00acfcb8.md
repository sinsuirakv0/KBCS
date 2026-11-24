# 00acfcb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acecc4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acecc4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-2b73b940e45842bb8a8ba65f7dfddceb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfcb8",
  "name": "FUN_00acfcb8",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eac2ab26bdba2150fc189f5005ecb5567dd68ff48dabb818ffeac94f73d6f1bc",
  "source_text_sha256": "eac2ab26bdba2150fc189f5005ecb5567dd68ff48dabb818ffeac94f73d6f1bc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfcb8",
        "00acfe4f"
      ],
      [
        "00acfe80",
        "00acfe83"
      ]
    ],
    "bytes_sha256": "c07341ec0a3e6d946b2f2a02465d3d56bcc3a691792373273c763ffea8ddd89f",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006627dc](../00662/006627dc.md)
- [00662880](../00662/00662880.md)
- [00662924](../00662/00662924.md)
- [007cdea8](../007cd/007cdea8.md)
- [007df87c](../007df/007df87c.md)
- [008c5290](../008c5/008c5290.md)
- [00a48f48](../00a48/00a48f48.md)
- [00acd634](../00acd/00acd634.md)
- [00acfe84](../00acf/00acfe84.md)
- [00ad021c](../00ad0/00ad021c.md)
- [00ad19bc](../00ad1/00ad19bc.md)

## 呼び出し先

- [00470ba0](../00470/00470ba0.md)
- [00803674](../00803/00803674.md)
- [00aebe80](../00aeb/00aebe80.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2360 bytes

~~~c

uint FUN_00acfcb8(long param_1,int param_2)

{
  void *__src;
  void *pvVar1;
  size_t __n;
  long lVar2;
  long *plVar3;
  bool bVar4;
  int iVar5;
  uint uVar6;
  void *__dest;
  size_t sVar7;
  long *plVar8;
  long *plVar9;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar5 = FUN_00803674(0);
  if ((0x13 < iVar5 + 0x19U) || ((0x87c01U >> (ulong)(iVar5 + 0x19U & 0x1f) & 1) == 0)) {
    plVar8 = *(long **)(param_1 + 0x33c0);
    while (plVar8 != (long *)(param_1 + 0x33c8)) {
      __src = (void *)plVar8[5];
      pvVar1 = (void *)plVar8[6];
      local_78 = 0;
      uStack_70 = 0;
      __n = (long)pvVar1 - (long)__src;
      local_80 = 0;
      if (__n != 0) {
        if ((long)__n < 0) {
          if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470ba0(&local_80);
          }
          goto LAB_00acfe80;
        }
        __dest = (void *)_Znwm(__n);
        memcpy(__dest,__src,__n);
        if (pvVar1 != __src) {
          sVar7 = 0;
          do {
            if (*(int *)((long)__dest + sVar7) == param_2) {
              _ZdlPv(__dest);
              uVar6 = 1;
              goto LAB_00acfe08;
            }
            sVar7 = sVar7 + 4;
          } while (__n != sVar7);
        }
        _ZdlPv(__dest);
      }
      plVar3 = (long *)plVar8[1];
      plVar9 = plVar8;
      if ((long *)plVar8[1] == (long *)0x0) {
        do {
          plVar8 = (long *)plVar9[2];
          bVar4 = (long *)*plVar8 != plVar9;
          plVar9 = plVar8;
        } while (bVar4);
      }
      else {
        do {
          plVar8 = plVar3;
          plVar3 = (long *)*plVar8;
        } while ((long *)*plVar8 != (long *)0x0);
      }
    }
    if (999999999 < param_2) {
      uVar6 = FUN_00aebe80(param_1,param_2);
      uVar6 = ~uVar6 >> 0x1f;
                    /* try { // try from 00acfe00 to 00bcfe1b has its CatchHandler @ 00ad0590 */
      goto LAB_00acfe08;
    }
  }
  uVar6 = 0;
LAB_00acfe08:
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00acfe1c to 00bd09f3 has its CatchHandler @ 00acdb7c */
    return uVar6;
  }
LAB_00acfe80:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfcb8"></a> `00acfcb8` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acfcbc"></a> `00acfcbc` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfcc0"></a> `00acfcc0` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acfcc4"></a> `00acfcc4` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfcc8"></a> `00acfcc8` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acfccc"></a> `00acfccc` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfcd0"></a> `00acfcd0` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acfcd4"></a> `00acfcd4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acfcd8"></a> `00acfcd8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfcdc"></a> `00acfcdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acfce0"></a> `00acfce0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acfce4"></a> `00acfce4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acfce8"></a> `00acfce8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acfcec"></a> `00acfcec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfcf0"></a> `00acfcf0` | `61 ce f4 97` | bl 0x00803674 | `UNCONDITIONAL_CALL`
<a id="insn-00acfcf4"></a> `00acfcf4` | `08 64 00 11` | add w8,w0,#0x19 | `FALL_THROUGH`
<a id="insn-00acfcf8"></a> `00acfcf8` | `1f 51 00 71` | cmp w8,#0x14 | `FALL_THROUGH`
<a id="insn-00acfcfc"></a> `00acfcfc` | `a2 00 00 54` | b.cs 0x00acfd10 | `CONDITIONAL_JUMP`
<a id="insn-00acfd00"></a> `00acfd00` | `29 80 8f 52` | mov w9,#0x7c01 | `FALL_THROUGH`
<a id="insn-00acfd04"></a> `00acfd04` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfd08"></a> `00acfd08` | `28 25 c8 1a` | lsr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00acfd0c"></a> `00acfd0c` | `c8 07 00 37` | tbnz w8,#0x0,0x00acfe04 | `CONDITIONAL_JUMP`
<a id="insn-00acfd10"></a> `00acfd10` | `9b e2 59 f9` | ldr x27,[x20, #0x33c0] | `FALL_THROUGH`
<a id="insn-00acfd14"></a> `00acfd14` | `08 79 86 52` | mov w8,#0x33c8 | `FALL_THROUGH`
<a id="insn-00acfd18"></a> `00acfd18` | `9a 02 08 8b` | add x26,x20,x8 | `FALL_THROUGH`
<a id="insn-00acfd1c"></a> `00acfd1c` | `7f 03 1a eb` | cmp x27,x26 | `FALL_THROUGH`
<a id="insn-00acfd20"></a> `00acfd20` | `e0 05 00 54` | b.eq 0x00acfddc | `CONDITIONAL_JUMP`
<a id="insn-00acfd24"></a> `00acfd24` | `f9 23 00 91` | add x25,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00acfd28"></a> `00acfd28` | `04 00 00 14` | b 0x00acfd38 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfd2c"></a> `00acfd2c` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00acfd30"></a> `00acfd30` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00acfd34"></a> `00acfd34` | `40 05 00 54` | b.eq 0x00acfddc | `CONDITIONAL_JUMP`
<a id="insn-00acfd38"></a> `00acfd38` | `77 f3 42 a9` | ldp x23,x28,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00acfd3c"></a> `00acfd3c` | `68 43 40 79` | ldrh w8,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00acfd40"></a> `00acfd40` | `3f 7f 01 a9` | stp xzr,xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00acfd44"></a> `00acfd44` | `e8 13 00 79` | strh w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acfd48"></a> `00acfd48` | `95 03 17 eb` | subs x21,x28,x23 | `FALL_THROUGH`
<a id="insn-00acfd4c"></a> `00acfd4c` | `3f 83 00 f8` | stur xzr,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00acfd50"></a> `00acfd50` | `60 02 00 54` | b.eq 0x00acfd9c | `CONDITIONAL_JUMP`
<a id="insn-00acfd54"></a> `00acfd54` | `35 07 f8 b7` | tbnz x21,#0x3f,0x00acfe38 | `CONDITIONAL_JUMP`
<a id="insn-00acfd58"></a> `00acfd58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acfd5c"></a> `00acfd5c` | `75 24 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd60"></a> `00acfd60` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00acfd64"></a> `00acfd64` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00acfd68"></a> `00acfd68` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00acfd6c"></a> `00acfd6c` | `cd 24 06 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd70"></a> `00acfd70` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-00acfd74"></a> `00acfd74` | `00 01 00 54` | b.eq 0x00acfd94 | `CONDITIONAL_JUMP`
<a id="insn-00acfd78"></a> `00acfd78` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00acfd7c"></a> `00acfd7c` | `c9 6a 68 b8` | ldr w9,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acfd80"></a> `00acfd80` | `3f 01 13 6b` | cmp w9,w19 | `FALL_THROUGH`
<a id="insn-00acfd84"></a> `00acfd84` | `40 02 00 54` | b.eq 0x00acfdcc | `CONDITIONAL_JUMP`
<a id="insn-00acfd88"></a> `00acfd88` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00acfd8c"></a> `00acfd8c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00acfd90"></a> `00acfd90` | `61 ff ff 54` | b.ne 0x00acfd7c | `CONDITIONAL_JUMP`
<a id="insn-00acfd94"></a> `00acfd94` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acfd98"></a> `00acfd98` | `6e 24 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acfd9c"></a> `00acfd9c` | `69 07 40 f9` | ldr x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00acfda0"></a> `00acfda0` | `a9 00 00 b4` | cbz x9,0x00acfdb4 | `CONDITIONAL_JUMP`
<a id="insn-00acfda4"></a> `00acfda4` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00acfda8"></a> `00acfda8` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00acfdac"></a> `00acfdac` | `c9 ff ff b5` | cbnz x9,0x00acfda4 | `CONDITIONAL_JUMP`
<a id="insn-00acfdb0"></a> `00acfdb0` | `df ff ff 17` | b 0x00acfd2c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfdb4"></a> `00acfdb4` | `68 0b 40 f9` | ldr x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00acfdb8"></a> `00acfdb8` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00acfdbc"></a> `00acfdbc` | `3f 01 1b eb` | cmp x9,x27 | `FALL_THROUGH`
<a id="insn-00acfdc0"></a> `00acfdc0` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00acfdc4"></a> `00acfdc4` | `81 ff ff 54` | b.ne 0x00acfdb4 | `CONDITIONAL_JUMP`
<a id="insn-00acfdc8"></a> `00acfdc8` | `d9 ff ff 17` | b 0x00acfd2c | `UNCONDITIONAL_JUMP`
<a id="insn-00acfdcc"></a> `00acfdcc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acfdd0"></a> `00acfdd0` | `60 24 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00acfdd4"></a> `00acfdd4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acfdd8"></a> `00acfdd8` | `0c 00 00 14` | b 0x00acfe08 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfddc"></a> `00acfddc` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00acfde0"></a> `00acfde0` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfde4"></a> `00acfde4` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00acfde8"></a> `00acfde8` | `eb 00 00 54` | b.lt 0x00acfe04 | `CONDITIONAL_JUMP`
<a id="insn-00acfdec"></a> `00acfdec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acfdf0"></a> `00acfdf0` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00acfdf4"></a> `00acfdf4` | `23 70 00 94` | bl 0x00aebe80 | `UNCONDITIONAL_CALL`
<a id="insn-00acfdf8"></a> `00acfdf8` | `e8 03 20 2a` | mvn w8,w0 | `FALL_THROUGH`
<a id="insn-00acfdfc"></a> `00acfdfc` | `00 7d 1f 53` | lsr w0,w8,#0x1f | `FALL_THROUGH`
<a id="insn-00acfe00"></a> `00acfe00` | `02 00 00 14` | b 0x00acfe08 | `UNCONDITIONAL_JUMP`
<a id="insn-00acfe04"></a> `00acfe04` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acfe08"></a> `00acfe08` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acfe0c"></a> `00acfe0c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfe10"></a> `00acfe10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfe14"></a> `00acfe14` | `61 03 00 54` | b.ne 0x00acfe80 | `CONDITIONAL_JUMP`
<a id="insn-00acfe18"></a> `00acfe18` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acfe1c"></a> `00acfe1c` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acfe20"></a> `00acfe20` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acfe24"></a> `00acfe24` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acfe28"></a> `00acfe28` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acfe2c"></a> `00acfe2c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acfe30"></a> `00acfe30` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acfe34"></a> `00acfe34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acfe38"></a> `00acfe38` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acfe3c"></a> `00acfe3c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfe40"></a> `00acfe40` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acfe44"></a> `00acfe44` | `e1 01 00 54` | b.ne 0x00acfe80 | `CONDITIONAL_JUMP`
<a id="insn-00acfe48"></a> `00acfe48` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00acfe4c"></a> `00acfe4c` | `55 83 e6 97` | bl 0x00470ba0 | `CALL_TERMINATOR`
<a id="insn-00acfe80"></a> `00acfe80` | `40 24 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfcb8`](#insn-00acfcb8) 範囲 `[['00acfcb8', '00acfcff']]`
  - `CONDITIONAL_JUMP` [`00acfcfc`](#insn-00acfcfc) → [`00acfd10`](#insn-00acfd10)
  - `FALL_THROUGH` [`00acfcfc`](#insn-00acfcfc) → [`00acfd00`](#insn-00acfd00)
- ブロック [`00acfd00`](#insn-00acfd00) 範囲 `[['00acfd00', '00acfd0f']]`
  - `CONDITIONAL_JUMP` [`00acfd0c`](#insn-00acfd0c) → [`00acfe04`](#insn-00acfe04)
  - `FALL_THROUGH` [`00acfd0c`](#insn-00acfd0c) → [`00acfd10`](#insn-00acfd10)
- ブロック [`00acfd10`](#insn-00acfd10) 範囲 `[['00acfd10', '00acfd23']]`
  - `CONDITIONAL_JUMP` [`00acfd20`](#insn-00acfd20) → [`00acfddc`](#insn-00acfddc)
  - `FALL_THROUGH` [`00acfd20`](#insn-00acfd20) → [`00acfd24`](#insn-00acfd24)
- ブロック [`00acfd24`](#insn-00acfd24) 範囲 `[['00acfd24', '00acfd2b']]`
  - `UNCONDITIONAL_JUMP` [`00acfd28`](#insn-00acfd28) → [`00acfd38`](#insn-00acfd38)
- ブロック [`00acfd2c`](#insn-00acfd2c) 範囲 `[['00acfd2c', '00acfd37']]`
  - `CONDITIONAL_JUMP` [`00acfd34`](#insn-00acfd34) → [`00acfddc`](#insn-00acfddc)
  - `FALL_THROUGH` [`00acfd34`](#insn-00acfd34) → [`00acfd38`](#insn-00acfd38)
- ブロック [`00acfd38`](#insn-00acfd38) 範囲 `[['00acfd38', '00acfd53']]`
  - `CONDITIONAL_JUMP` [`00acfd50`](#insn-00acfd50) → [`00acfd9c`](#insn-00acfd9c)
  - `FALL_THROUGH` [`00acfd50`](#insn-00acfd50) → [`00acfd54`](#insn-00acfd54)
- ブロック [`00acfd54`](#insn-00acfd54) 範囲 `[['00acfd54', '00acfd57']]`
  - `CONDITIONAL_JUMP` [`00acfd54`](#insn-00acfd54) → [`00acfe38`](#insn-00acfe38)
  - `FALL_THROUGH` [`00acfd54`](#insn-00acfd54) → [`00acfd58`](#insn-00acfd58)
- ブロック [`00acfd58`](#insn-00acfd58) 範囲 `[['00acfd58', '00acfd77']]`
  - `CONDITIONAL_JUMP` [`00acfd74`](#insn-00acfd74) → [`00acfd94`](#insn-00acfd94)
  - `FALL_THROUGH` [`00acfd74`](#insn-00acfd74) → [`00acfd78`](#insn-00acfd78)
- ブロック [`00acfd78`](#insn-00acfd78) 範囲 `[['00acfd78', '00acfd7b']]`
  - `FALL_THROUGH` [`00acfd78`](#insn-00acfd78) → [`00acfd7c`](#insn-00acfd7c)
- ブロック [`00acfd7c`](#insn-00acfd7c) 範囲 `[['00acfd7c', '00acfd87']]`
  - `CONDITIONAL_JUMP` [`00acfd84`](#insn-00acfd84) → [`00acfdcc`](#insn-00acfdcc)
  - `FALL_THROUGH` [`00acfd84`](#insn-00acfd84) → [`00acfd88`](#insn-00acfd88)
- ブロック [`00acfd88`](#insn-00acfd88) 範囲 `[['00acfd88', '00acfd93']]`
  - `CONDITIONAL_JUMP` [`00acfd90`](#insn-00acfd90) → [`00acfd7c`](#insn-00acfd7c)
  - `FALL_THROUGH` [`00acfd90`](#insn-00acfd90) → [`00acfd94`](#insn-00acfd94)
- ブロック [`00acfd94`](#insn-00acfd94) 範囲 `[['00acfd94', '00acfd9b']]`
  - `FALL_THROUGH` [`00acfd98`](#insn-00acfd98) → [`00acfd9c`](#insn-00acfd9c)
- ブロック [`00acfd9c`](#insn-00acfd9c) 範囲 `[['00acfd9c', '00acfda3']]`
  - `CONDITIONAL_JUMP` [`00acfda0`](#insn-00acfda0) → [`00acfdb4`](#insn-00acfdb4)
  - `FALL_THROUGH` [`00acfda0`](#insn-00acfda0) → [`00acfda4`](#insn-00acfda4)
- ブロック [`00acfda4`](#insn-00acfda4) 範囲 `[['00acfda4', '00acfdaf']]`
  - `CONDITIONAL_JUMP` [`00acfdac`](#insn-00acfdac) → [`00acfda4`](#insn-00acfda4)
  - `FALL_THROUGH` [`00acfdac`](#insn-00acfdac) → [`00acfdb0`](#insn-00acfdb0)
- ブロック [`00acfdb0`](#insn-00acfdb0) 範囲 `[['00acfdb0', '00acfdb3']]`
  - `UNCONDITIONAL_JUMP` [`00acfdb0`](#insn-00acfdb0) → [`00acfd2c`](#insn-00acfd2c)
- ブロック [`00acfdb4`](#insn-00acfdb4) 範囲 `[['00acfdb4', '00acfdc7']]`
  - `CONDITIONAL_JUMP` [`00acfdc4`](#insn-00acfdc4) → [`00acfdb4`](#insn-00acfdb4)
  - `FALL_THROUGH` [`00acfdc4`](#insn-00acfdc4) → [`00acfdc8`](#insn-00acfdc8)
- ブロック [`00acfdc8`](#insn-00acfdc8) 範囲 `[['00acfdc8', '00acfdcb']]`
  - `UNCONDITIONAL_JUMP` [`00acfdc8`](#insn-00acfdc8) → [`00acfd2c`](#insn-00acfd2c)
- ブロック [`00acfdcc`](#insn-00acfdcc) 範囲 `[['00acfdcc', '00acfddb']]`
  - `UNCONDITIONAL_JUMP` [`00acfdd8`](#insn-00acfdd8) → [`00acfe08`](#insn-00acfe08)
- ブロック [`00acfddc`](#insn-00acfddc) 範囲 `[['00acfddc', '00acfdeb']]`
  - `CONDITIONAL_JUMP` [`00acfde8`](#insn-00acfde8) → [`00acfe04`](#insn-00acfe04)
  - `FALL_THROUGH` [`00acfde8`](#insn-00acfde8) → [`00acfdec`](#insn-00acfdec)
- ブロック [`00acfdec`](#insn-00acfdec) 範囲 `[['00acfdec', '00acfdff']]`
  - `FALL_THROUGH` [`00acfdfc`](#insn-00acfdfc) → [`00acfe00`](#insn-00acfe00)
- ブロック [`00acfe00`](#insn-00acfe00) 範囲 `[['00acfe00', '00acfe03']]`
  - `UNCONDITIONAL_JUMP` [`00acfe00`](#insn-00acfe00) → [`00acfe08`](#insn-00acfe08)
- ブロック [`00acfe04`](#insn-00acfe04) 範囲 `[['00acfe04', '00acfe07']]`
  - `FALL_THROUGH` [`00acfe04`](#insn-00acfe04) → [`00acfe08`](#insn-00acfe08)
- ブロック [`00acfe08`](#insn-00acfe08) 範囲 `[['00acfe08', '00acfe17']]`
  - `CONDITIONAL_JUMP` [`00acfe14`](#insn-00acfe14) → [`00acfe80`](#insn-00acfe80)
  - `FALL_THROUGH` [`00acfe14`](#insn-00acfe14) → [`00acfe18`](#insn-00acfe18)
- ブロック [`00acfe18`](#insn-00acfe18) 範囲 `[['00acfe18', '00acfe1b']]`
  - `FALL_THROUGH` [`00acfe18`](#insn-00acfe18) → [`00acfe1c`](#insn-00acfe1c)
- ブロック [`00acfe1c`](#insn-00acfe1c) 範囲 `[['00acfe1c', '00acfe37']]`
- ブロック [`00acfe38`](#insn-00acfe38) 範囲 `[['00acfe38', '00acfe47']]`
  - `CONDITIONAL_JUMP` [`00acfe44`](#insn-00acfe44) → [`00acfe80`](#insn-00acfe80)
  - `FALL_THROUGH` [`00acfe44`](#insn-00acfe44) → [`00acfe48`](#insn-00acfe48)
- ブロック [`00acfe48`](#insn-00acfe48) 範囲 `[['00acfe48', '00acfe4f']]`
- ブロック [`00acfe80`](#insn-00acfe80) 範囲 `[['00acfe80', '00acfe83']]`

## 命令位置別の参照

- [`00acfcbc`](#insn-00acfcbc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc0`](#insn-00acfcc0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc4`](#insn-00acfcc4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcc8`](#insn-00acfcc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfccc`](#insn-00acfccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcd0`](#insn-00acfcd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcec`](#insn-00acfcec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfcf0`](#insn-00acfcf0) → [`00803674`](../00803/00803674.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00803674` · 推定シンボル `None` · 推定型 `None`
- [`00acfcfc`](#insn-00acfcfc) → [`00acfd10`](#insn-00acfd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd0c`](#insn-00acfd0c) → [`00acfe04`](#insn-00acfe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd20`](#insn-00acfd20) → [`00acfddc`](#insn-00acfddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd28`](#insn-00acfd28) → [`00acfd38`](#insn-00acfd38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd34`](#insn-00acfd34) → [`00acfddc`](#insn-00acfddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd40`](#insn-00acfd40) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd44`](#insn-00acfd44) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd4c`](#insn-00acfd4c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd50`](#insn-00acfd50) → [`00acfd9c`](#insn-00acfd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd54`](#insn-00acfd54) → [`00acfe38`](#insn-00acfe38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd5c`](#insn-00acfd5c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00acfd6c`](#insn-00acfd6c) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`00acfd74`](#insn-00acfd74) → [`00acfd94`](#insn-00acfd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd84`](#insn-00acfd84) → [`00acfdcc`](#insn-00acfdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd90`](#insn-00acfd90) → [`00acfd7c`](#insn-00acfd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfd98`](#insn-00acfd98) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acfda0`](#insn-00acfda0) → [`00acfdb4`](#insn-00acfdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdac`](#insn-00acfdac) → [`00acfda4`](#insn-00acfda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdb0`](#insn-00acfdb0) → [`00acfd2c`](#insn-00acfd2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdc4`](#insn-00acfdc4) → [`00acfdb4`](#insn-00acfdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdc8`](#insn-00acfdc8) → [`00acfd2c`](#insn-00acfd2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdd0`](#insn-00acfdd0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00acfdd8`](#insn-00acfdd8) → [`00acfe08`](#insn-00acfe08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfde8`](#insn-00acfde8) → [`00acfe04`](#insn-00acfe04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfdf4`](#insn-00acfdf4) → [`00aebe80`](../00aeb/00aebe80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aebe80` · 推定シンボル `None` · 推定型 `None`
- [`00acfe00`](#insn-00acfe00) → [`00acfe08`](#insn-00acfe08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe0c`](#insn-00acfe0c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe14`](#insn-00acfe14) → [`00acfe80`](#insn-00acfe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe18`](#insn-00acfe18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe1c`](#insn-00acfe1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe20`](#insn-00acfe20) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe24`](#insn-00acfe24) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe28`](#insn-00acfe28) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe2c`](#insn-00acfe2c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe3c`](#insn-00acfe3c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe44`](#insn-00acfe44) → [`00acfe80`](#insn-00acfe80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe4c`](#insn-00acfe4c) → [`00470ba0`](../00470/00470ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470ba0` · 推定シンボル `None` · 推定型 `None`
- [`00acfe80`](#insn-00acfe80) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfcbc`](#insn-00acfcbc)

~~~json
{
  "source": "00acfcbc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc0`](#insn-00acfcc0)

~~~json
{
  "source": "00acfcc0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc4`](#insn-00acfcc4)

~~~json
{
  "source": "00acfcc4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcc8`](#insn-00acfcc8)

~~~json
{
  "source": "00acfcc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfccc`](#insn-00acfccc)

~~~json
{
  "source": "00acfccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcd0`](#insn-00acfcd0)

~~~json
{
  "source": "00acfcd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcec`](#insn-00acfcec)

~~~json
{
  "source": "00acfcec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfcf0`](#insn-00acfcf0)

~~~json
{
  "source": "00acfcf0",
  "target": "00803674",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfcfc`](#insn-00acfcfc)

~~~json
{
  "source": "00acfcfc",
  "target": "00acfd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd0c`](#insn-00acfd0c)

~~~json
{
  "source": "00acfd0c",
  "target": "00acfe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd20`](#insn-00acfd20)

~~~json
{
  "source": "00acfd20",
  "target": "00acfddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd28`](#insn-00acfd28)

~~~json
{
  "source": "00acfd28",
  "target": "00acfd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd34`](#insn-00acfd34)

~~~json
{
  "source": "00acfd34",
  "target": "00acfddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd40`](#insn-00acfd40)

~~~json
{
  "source": "00acfd40",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd44`](#insn-00acfd44)

~~~json
{
  "source": "00acfd44",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd4c`](#insn-00acfd4c)

~~~json
{
  "source": "00acfd4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd50`](#insn-00acfd50)

~~~json
{
  "source": "00acfd50",
  "target": "00acfd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd54`](#insn-00acfd54)

~~~json
{
  "source": "00acfd54",
  "target": "00acfe38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd5c`](#insn-00acfd5c)

~~~json
{
  "source": "00acfd5c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd6c`](#insn-00acfd6c)

~~~json
{
  "source": "00acfd6c",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfd74`](#insn-00acfd74)

~~~json
{
  "source": "00acfd74",
  "target": "00acfd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd84`](#insn-00acfd84)

~~~json
{
  "source": "00acfd84",
  "target": "00acfdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd90`](#insn-00acfd90)

~~~json
{
  "source": "00acfd90",
  "target": "00acfd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfd98`](#insn-00acfd98)

~~~json
{
  "source": "00acfd98",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfda0`](#insn-00acfda0)

~~~json
{
  "source": "00acfda0",
  "target": "00acfdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdac`](#insn-00acfdac)

~~~json
{
  "source": "00acfdac",
  "target": "00acfda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdb0`](#insn-00acfdb0)

~~~json
{
  "source": "00acfdb0",
  "target": "00acfd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdc4`](#insn-00acfdc4)

~~~json
{
  "source": "00acfdc4",
  "target": "00acfdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdc8`](#insn-00acfdc8)

~~~json
{
  "source": "00acfdc8",
  "target": "00acfd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdd0`](#insn-00acfdd0)

~~~json
{
  "source": "00acfdd0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfdd8`](#insn-00acfdd8)

~~~json
{
  "source": "00acfdd8",
  "target": "00acfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfde8`](#insn-00acfde8)

~~~json
{
  "source": "00acfde8",
  "target": "00acfe04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfdf4`](#insn-00acfdf4)

~~~json
{
  "source": "00acfdf4",
  "target": "00aebe80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe00`](#insn-00acfe00)

~~~json
{
  "source": "00acfe00",
  "target": "00acfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe0c`](#insn-00acfe0c)

~~~json
{
  "source": "00acfe0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe14`](#insn-00acfe14)

~~~json
{
  "source": "00acfe14",
  "target": "00acfe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe18`](#insn-00acfe18)

~~~json
{
  "source": "00acfe18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe1c`](#insn-00acfe1c)

~~~json
{
  "source": "00acfe1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe20`](#insn-00acfe20)

~~~json
{
  "source": "00acfe20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe24`](#insn-00acfe24)

~~~json
{
  "source": "00acfe24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe28`](#insn-00acfe28)

~~~json
{
  "source": "00acfe28",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe2c`](#insn-00acfe2c)

~~~json
{
  "source": "00acfe2c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe3c`](#insn-00acfe3c)

~~~json
{
  "source": "00acfe3c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe44`](#insn-00acfe44)

~~~json
{
  "source": "00acfe44",
  "target": "00acfe80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe4c`](#insn-00acfe4c)

~~~json
{
  "source": "00acfe4c",
  "target": "00470ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfe80`](#insn-00acfe80)

~~~json
{
  "source": "00acfe80",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
