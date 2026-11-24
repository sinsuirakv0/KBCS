# 00acecc4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acec54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-6e96ab1f045a37aabe83793aa548a767)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00acfcb8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acf/00acfcb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-2b73b940e45842bb8a8ba65f7dfddceb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acecc4",
  "name": "FUN_00acecc4",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538",
  "source_text_sha256": "46d7825ed8862a692534b7efda42b64319c4084dadc162868aa438f8990dc538",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acecc4",
        "00acee5b"
      ],
      [
        "00acee8c",
        "00acee8f"
      ]
    ],
    "bytes_sha256": "165fe9192b749640ade59a522acc27ab2b1a4d6d5fab5470fa1011d9830cc3b4",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0066242c](../00662/0066242c.md)
- [006624d0](../00662/006624d0.md)
- [00662574](../00662/00662574.md)
- [007ccf44](../007cc/007ccf44.md)
- [007de918](../007de/007de918.md)
- [008c42e4](../008c4/008c42e4.md)
- [00a47f54](../00a47/00a47f54.md)
- [00acc640](../00acc/00acc640.md)
- [00acee90](../00ace/00acee90.md)
- [00acf228](../00acf/00acf228.md)
- [00ad09c8](../00ad0/00ad09c8.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00802710](../00802/00802710.md)
- [00aeae8c](../00aea/00aeae8c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2554 bytes

~~~c

uint FUN_00acecc4(long param_1,int param_2)

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
  
                    /* try { // try from 00acecd8 to 00bcece3 has its CatchHandler @ 00acf64c */
                    /* try { // try from 00acece4 to 00bced03 has its CatchHandler @ 00acf5f8 */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar5 = FUN_00802710(0);
                    /* try { // try from 00aced04 to 00bcee53 has its CatchHandler @ 00accbd0 */
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
                    /* try { // try from 00acee54 to 00bcee6f has its CatchHandler @ 00acf5e4 */
                    /* WARNING: Subroutine does not return */
            FUN_00470880(&local_80);
          }
          goto LAB_00acee8c;
        }
        __dest = (void *)_Znwm(__n);
        memcpy(__dest,__src,__n);
        if (pvVar1 != __src) {
          sVar7 = 0;
          do {
            if (*(int *)((long)__dest + sVar7) == param_2) {
              _ZdlPv(__dest);
              uVar6 = 1;
              goto LAB_00acee14;
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
      uVar6 = FUN_00aeae8c(param_1,param_2);
      uVar6 = ~uVar6 >> 0x1f;
      goto LAB_00acee14;
    }
  }
  uVar6 = 0;
LAB_00acee14:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar6;
  }
LAB_00acee8c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acecc4"></a> `00acecc4` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acecc8"></a> `00acecc8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aceccc"></a> `00aceccc` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acecd0"></a> `00acecd0` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acecd4"></a> `00acecd4` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acecd8"></a> `00acecd8` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acecdc"></a> `00acecdc` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acece0"></a> `00acece0` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acece4"></a> `00acece4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acece8"></a> `00acece8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acecec"></a> `00acecec` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acecf0"></a> `00acecf0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acecf4"></a> `00acecf4` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00acecf8"></a> `00acecf8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acecfc"></a> `00acecfc` | `85 ce f4 97` | bl 0x00802710 | `UNCONDITIONAL_CALL`
<a id="insn-00aced00"></a> `00aced00` | `08 64 00 11` | add w8,w0,#0x19 | `FALL_THROUGH`
<a id="insn-00aced04"></a> `00aced04` | `1f 51 00 71` | cmp w8,#0x14 | `FALL_THROUGH`
<a id="insn-00aced08"></a> `00aced08` | `a2 00 00 54` | b.cs 0x00aced1c | `CONDITIONAL_JUMP`
<a id="insn-00aced0c"></a> `00aced0c` | `29 80 8f 52` | mov w9,#0x7c01 | `FALL_THROUGH`
<a id="insn-00aced10"></a> `00aced10` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00aced14"></a> `00aced14` | `28 25 c8 1a` | lsr w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aced18"></a> `00aced18` | `c8 07 00 37` | tbnz w8,#0x0,0x00acee10 | `CONDITIONAL_JUMP`
<a id="insn-00aced1c"></a> `00aced1c` | `9b e2 59 f9` | ldr x27,[x20, #0x33c0] | `FALL_THROUGH`
<a id="insn-00aced20"></a> `00aced20` | `08 79 86 52` | mov w8,#0x33c8 | `FALL_THROUGH`
<a id="insn-00aced24"></a> `00aced24` | `9a 02 08 8b` | add x26,x20,x8 | `FALL_THROUGH`
<a id="insn-00aced28"></a> `00aced28` | `7f 03 1a eb` | cmp x27,x26 | `FALL_THROUGH`
<a id="insn-00aced2c"></a> `00aced2c` | `e0 05 00 54` | b.eq 0x00acede8 | `CONDITIONAL_JUMP`
<a id="insn-00aced30"></a> `00aced30` | `f9 23 00 91` | add x25,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aced34"></a> `00aced34` | `04 00 00 14` | b 0x00aced44 | `UNCONDITIONAL_JUMP`
<a id="insn-00aced38"></a> `00aced38` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00aced3c"></a> `00aced3c` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00aced40"></a> `00aced40` | `40 05 00 54` | b.eq 0x00acede8 | `CONDITIONAL_JUMP`
<a id="insn-00aced44"></a> `00aced44` | `77 f3 42 a9` | ldp x23,x28,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00aced48"></a> `00aced48` | `68 43 40 79` | ldrh w8,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00aced4c"></a> `00aced4c` | `3f 7f 01 a9` | stp xzr,xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00aced50"></a> `00aced50` | `e8 13 00 79` | strh w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aced54"></a> `00aced54` | `95 03 17 eb` | subs x21,x28,x23 | `FALL_THROUGH`
<a id="insn-00aced58"></a> `00aced58` | `3f 83 00 f8` | stur xzr,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00aced5c"></a> `00aced5c` | `60 02 00 54` | b.eq 0x00aceda8 | `CONDITIONAL_JUMP`
<a id="insn-00aced60"></a> `00aced60` | `35 07 f8 b7` | tbnz x21,#0x3f,0x00acee44 | `CONDITIONAL_JUMP`
<a id="insn-00aced64"></a> `00aced64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aced68"></a> `00aced68` | `7e 24 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aced6c"></a> `00aced6c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00aced70"></a> `00aced70` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aced74"></a> `00aced74` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aced78"></a> `00aced78` | `d6 24 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aced7c"></a> `00aced7c` | `9f 03 17 eb` | cmp x28,x23 | `FALL_THROUGH`
<a id="insn-00aced80"></a> `00aced80` | `00 01 00 54` | b.eq 0x00aceda0 | `CONDITIONAL_JUMP`
<a id="insn-00aced84"></a> `00aced84` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00aced88"></a> `00aced88` | `c9 6a 68 b8` | ldr w9,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aced8c"></a> `00aced8c` | `3f 01 13 6b` | cmp w9,w19 | `FALL_THROUGH`
<a id="insn-00aced90"></a> `00aced90` | `40 02 00 54` | b.eq 0x00acedd8 | `CONDITIONAL_JUMP`
<a id="insn-00aced94"></a> `00aced94` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00aced98"></a> `00aced98` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00aced9c"></a> `00aced9c` | `61 ff ff 54` | b.ne 0x00aced88 | `CONDITIONAL_JUMP`
<a id="insn-00aceda0"></a> `00aceda0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aceda4"></a> `00aceda4` | `77 24 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aceda8"></a> `00aceda8` | `69 07 40 f9` | ldr x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00acedac"></a> `00acedac` | `a9 00 00 b4` | cbz x9,0x00acedc0 | `CONDITIONAL_JUMP`
<a id="insn-00acedb0"></a> `00acedb0` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00acedb4"></a> `00acedb4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00acedb8"></a> `00acedb8` | `c9 ff ff b5` | cbnz x9,0x00acedb0 | `CONDITIONAL_JUMP`
<a id="insn-00acedbc"></a> `00acedbc` | `df ff ff 17` | b 0x00aced38 | `UNCONDITIONAL_JUMP`
<a id="insn-00acedc0"></a> `00acedc0` | `68 0b 40 f9` | ldr x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00acedc4"></a> `00acedc4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00acedc8"></a> `00acedc8` | `3f 01 1b eb` | cmp x9,x27 | `FALL_THROUGH`
<a id="insn-00acedcc"></a> `00acedcc` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00acedd0"></a> `00acedd0` | `81 ff ff 54` | b.ne 0x00acedc0 | `CONDITIONAL_JUMP`
<a id="insn-00acedd4"></a> `00acedd4` | `d9 ff ff 17` | b 0x00aced38 | `UNCONDITIONAL_JUMP`
<a id="insn-00acedd8"></a> `00acedd8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aceddc"></a> `00aceddc` | `69 24 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00acede0"></a> `00acede0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00acede4"></a> `00acede4` | `0c 00 00 14` | b 0x00acee14 | `UNCONDITIONAL_JUMP`
<a id="insn-00acede8"></a> `00acede8` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00acedec"></a> `00acedec` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acedf0"></a> `00acedf0` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00acedf4"></a> `00acedf4` | `eb 00 00 54` | b.lt 0x00acee10 | `CONDITIONAL_JUMP`
<a id="insn-00acedf8"></a> `00acedf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acedfc"></a> `00acedfc` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00acee00"></a> `00acee00` | `23 70 00 94` | bl 0x00aeae8c | `UNCONDITIONAL_CALL`
<a id="insn-00acee04"></a> `00acee04` | `e8 03 20 2a` | mvn w8,w0 | `FALL_THROUGH`
<a id="insn-00acee08"></a> `00acee08` | `00 7d 1f 53` | lsr w0,w8,#0x1f | `FALL_THROUGH`
<a id="insn-00acee0c"></a> `00acee0c` | `02 00 00 14` | b 0x00acee14 | `UNCONDITIONAL_JUMP`
<a id="insn-00acee10"></a> `00acee10` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acee14"></a> `00acee14` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acee18"></a> `00acee18` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acee1c"></a> `00acee1c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acee20"></a> `00acee20` | `61 03 00 54` | b.ne 0x00acee8c | `CONDITIONAL_JUMP`
<a id="insn-00acee24"></a> `00acee24` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acee28"></a> `00acee28` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acee2c"></a> `00acee2c` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acee30"></a> `00acee30` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acee34"></a> `00acee34` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acee38"></a> `00acee38` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acee3c"></a> `00acee3c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acee40"></a> `00acee40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acee44"></a> `00acee44` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00acee48"></a> `00acee48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acee4c"></a> `00acee4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acee50"></a> `00acee50` | `e1 01 00 54` | b.ne 0x00acee8c | `CONDITIONAL_JUMP`
<a id="insn-00acee54"></a> `00acee54` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00acee58"></a> `00acee58` | `8a 86 e6 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-00acee8c"></a> `00acee8c` | `49 24 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acecc4`](#insn-00acecc4) 範囲 `[['00acecc4', '00acecd7']]`
  - `FALL_THROUGH` [`00acecd4`](#insn-00acecd4) → [`00acecd8`](#insn-00acecd8)
- ブロック [`00acecd8`](#insn-00acecd8) 範囲 `[['00acecd8', '00acece3']]`
  - `FALL_THROUGH` [`00acece0`](#insn-00acece0) → [`00acece4`](#insn-00acece4)
- ブロック [`00acece4`](#insn-00acece4) 範囲 `[['00acece4', '00aced03']]`
  - `FALL_THROUGH` [`00aced00`](#insn-00aced00) → [`00aced04`](#insn-00aced04)
- ブロック [`00aced04`](#insn-00aced04) 範囲 `[['00aced04', '00aced0b']]`
  - `CONDITIONAL_JUMP` [`00aced08`](#insn-00aced08) → [`00aced1c`](#insn-00aced1c)
  - `FALL_THROUGH` [`00aced08`](#insn-00aced08) → [`00aced0c`](#insn-00aced0c)
- ブロック [`00aced0c`](#insn-00aced0c) 範囲 `[['00aced0c', '00aced1b']]`
  - `CONDITIONAL_JUMP` [`00aced18`](#insn-00aced18) → [`00acee10`](#insn-00acee10)
  - `FALL_THROUGH` [`00aced18`](#insn-00aced18) → [`00aced1c`](#insn-00aced1c)
- ブロック [`00aced1c`](#insn-00aced1c) 範囲 `[['00aced1c', '00aced2f']]`
  - `CONDITIONAL_JUMP` [`00aced2c`](#insn-00aced2c) → [`00acede8`](#insn-00acede8)
  - `FALL_THROUGH` [`00aced2c`](#insn-00aced2c) → [`00aced30`](#insn-00aced30)
- ブロック [`00aced30`](#insn-00aced30) 範囲 `[['00aced30', '00aced37']]`
  - `UNCONDITIONAL_JUMP` [`00aced34`](#insn-00aced34) → [`00aced44`](#insn-00aced44)
- ブロック [`00aced38`](#insn-00aced38) 範囲 `[['00aced38', '00aced43']]`
  - `CONDITIONAL_JUMP` [`00aced40`](#insn-00aced40) → [`00acede8`](#insn-00acede8)
  - `FALL_THROUGH` [`00aced40`](#insn-00aced40) → [`00aced44`](#insn-00aced44)
- ブロック [`00aced44`](#insn-00aced44) 範囲 `[['00aced44', '00aced5f']]`
  - `CONDITIONAL_JUMP` [`00aced5c`](#insn-00aced5c) → [`00aceda8`](#insn-00aceda8)
  - `FALL_THROUGH` [`00aced5c`](#insn-00aced5c) → [`00aced60`](#insn-00aced60)
- ブロック [`00aced60`](#insn-00aced60) 範囲 `[['00aced60', '00aced63']]`
  - `CONDITIONAL_JUMP` [`00aced60`](#insn-00aced60) → [`00acee44`](#insn-00acee44)
  - `FALL_THROUGH` [`00aced60`](#insn-00aced60) → [`00aced64`](#insn-00aced64)
- ブロック [`00aced64`](#insn-00aced64) 範囲 `[['00aced64', '00aced83']]`
  - `CONDITIONAL_JUMP` [`00aced80`](#insn-00aced80) → [`00aceda0`](#insn-00aceda0)
  - `FALL_THROUGH` [`00aced80`](#insn-00aced80) → [`00aced84`](#insn-00aced84)
- ブロック [`00aced84`](#insn-00aced84) 範囲 `[['00aced84', '00aced87']]`
  - `FALL_THROUGH` [`00aced84`](#insn-00aced84) → [`00aced88`](#insn-00aced88)
- ブロック [`00aced88`](#insn-00aced88) 範囲 `[['00aced88', '00aced93']]`
  - `CONDITIONAL_JUMP` [`00aced90`](#insn-00aced90) → [`00acedd8`](#insn-00acedd8)
  - `FALL_THROUGH` [`00aced90`](#insn-00aced90) → [`00aced94`](#insn-00aced94)
- ブロック [`00aced94`](#insn-00aced94) 範囲 `[['00aced94', '00aced9f']]`
  - `CONDITIONAL_JUMP` [`00aced9c`](#insn-00aced9c) → [`00aced88`](#insn-00aced88)
  - `FALL_THROUGH` [`00aced9c`](#insn-00aced9c) → [`00aceda0`](#insn-00aceda0)
- ブロック [`00aceda0`](#insn-00aceda0) 範囲 `[['00aceda0', '00aceda7']]`
  - `FALL_THROUGH` [`00aceda4`](#insn-00aceda4) → [`00aceda8`](#insn-00aceda8)
- ブロック [`00aceda8`](#insn-00aceda8) 範囲 `[['00aceda8', '00acedaf']]`
  - `CONDITIONAL_JUMP` [`00acedac`](#insn-00acedac) → [`00acedc0`](#insn-00acedc0)
  - `FALL_THROUGH` [`00acedac`](#insn-00acedac) → [`00acedb0`](#insn-00acedb0)
- ブロック [`00acedb0`](#insn-00acedb0) 範囲 `[['00acedb0', '00acedbb']]`
  - `CONDITIONAL_JUMP` [`00acedb8`](#insn-00acedb8) → [`00acedb0`](#insn-00acedb0)
  - `FALL_THROUGH` [`00acedb8`](#insn-00acedb8) → [`00acedbc`](#insn-00acedbc)
- ブロック [`00acedbc`](#insn-00acedbc) 範囲 `[['00acedbc', '00acedbf']]`
  - `UNCONDITIONAL_JUMP` [`00acedbc`](#insn-00acedbc) → [`00aced38`](#insn-00aced38)
- ブロック [`00acedc0`](#insn-00acedc0) 範囲 `[['00acedc0', '00acedd3']]`
  - `CONDITIONAL_JUMP` [`00acedd0`](#insn-00acedd0) → [`00acedc0`](#insn-00acedc0)
  - `FALL_THROUGH` [`00acedd0`](#insn-00acedd0) → [`00acedd4`](#insn-00acedd4)
- ブロック [`00acedd4`](#insn-00acedd4) 範囲 `[['00acedd4', '00acedd7']]`
  - `UNCONDITIONAL_JUMP` [`00acedd4`](#insn-00acedd4) → [`00aced38`](#insn-00aced38)
- ブロック [`00acedd8`](#insn-00acedd8) 範囲 `[['00acedd8', '00acede7']]`
  - `UNCONDITIONAL_JUMP` [`00acede4`](#insn-00acede4) → [`00acee14`](#insn-00acee14)
- ブロック [`00acede8`](#insn-00acede8) 範囲 `[['00acede8', '00acedf7']]`
  - `CONDITIONAL_JUMP` [`00acedf4`](#insn-00acedf4) → [`00acee10`](#insn-00acee10)
  - `FALL_THROUGH` [`00acedf4`](#insn-00acedf4) → [`00acedf8`](#insn-00acedf8)
- ブロック [`00acedf8`](#insn-00acedf8) 範囲 `[['00acedf8', '00acee0f']]`
  - `UNCONDITIONAL_JUMP` [`00acee0c`](#insn-00acee0c) → [`00acee14`](#insn-00acee14)
- ブロック [`00acee10`](#insn-00acee10) 範囲 `[['00acee10', '00acee13']]`
  - `FALL_THROUGH` [`00acee10`](#insn-00acee10) → [`00acee14`](#insn-00acee14)
- ブロック [`00acee14`](#insn-00acee14) 範囲 `[['00acee14', '00acee23']]`
  - `CONDITIONAL_JUMP` [`00acee20`](#insn-00acee20) → [`00acee8c`](#insn-00acee8c)
  - `FALL_THROUGH` [`00acee20`](#insn-00acee20) → [`00acee24`](#insn-00acee24)
- ブロック [`00acee24`](#insn-00acee24) 範囲 `[['00acee24', '00acee43']]`
- ブロック [`00acee44`](#insn-00acee44) 範囲 `[['00acee44', '00acee53']]`
  - `CONDITIONAL_JUMP` [`00acee50`](#insn-00acee50) → [`00acee8c`](#insn-00acee8c)
  - `FALL_THROUGH` [`00acee50`](#insn-00acee50) → [`00acee54`](#insn-00acee54)
- ブロック [`00acee54`](#insn-00acee54) 範囲 `[['00acee54', '00acee5b']]`
- ブロック [`00acee8c`](#insn-00acee8c) 範囲 `[['00acee8c', '00acee8f']]`

## 命令位置別の参照

- [`00acecc8`](#insn-00acecc8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceccc`](#insn-00aceccc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecd0`](#insn-00acecd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecd4`](#insn-00acecd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecd8`](#insn-00acecd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecdc`](#insn-00acecdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecf8`](#insn-00acecf8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acecfc`](#insn-00acecfc) → [`00802710`](../00802/00802710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802710` · 推定シンボル `None` · 推定型 `None`
- [`00aced08`](#insn-00aced08) → [`00aced1c`](#insn-00aced1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced18`](#insn-00aced18) → [`00acee10`](#insn-00acee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced2c`](#insn-00aced2c) → [`00acede8`](#insn-00acede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced34`](#insn-00aced34) → [`00aced44`](#insn-00aced44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced40`](#insn-00aced40) → [`00acede8`](#insn-00acede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced4c`](#insn-00aced4c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced50`](#insn-00aced50) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced58`](#insn-00aced58) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced5c`](#insn-00aced5c) → [`00aceda8`](#insn-00aceda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced60`](#insn-00aced60) → [`00acee44`](#insn-00acee44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced68`](#insn-00aced68) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aced78`](#insn-00aced78) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aced80`](#insn-00aced80) → [`00aceda0`](#insn-00aceda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced90`](#insn-00aced90) → [`00acedd8`](#insn-00acedd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aced9c`](#insn-00aced9c) → [`00aced88`](#insn-00aced88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceda4`](#insn-00aceda4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00acedac`](#insn-00acedac) → [`00acedc0`](#insn-00acedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedb8`](#insn-00acedb8) → [`00acedb0`](#insn-00acedb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedbc`](#insn-00acedbc) → [`00aced38`](#insn-00aced38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedd0`](#insn-00acedd0) → [`00acedc0`](#insn-00acedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedd4`](#insn-00acedd4) → [`00aced38`](#insn-00aced38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceddc`](#insn-00aceddc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00acede4`](#insn-00acede4) → [`00acee14`](#insn-00acee14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acedf4`](#insn-00acedf4) → [`00acee10`](#insn-00acee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee00`](#insn-00acee00) → [`00aeae8c`](../00aea/00aeae8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aeae8c` · 推定シンボル `None` · 推定型 `None`
- [`00acee0c`](#insn-00acee0c) → [`00acee14`](#insn-00acee14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee18`](#insn-00acee18) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee20`](#insn-00acee20) → [`00acee8c`](#insn-00acee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee24`](#insn-00acee24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee28`](#insn-00acee28) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee2c`](#insn-00acee2c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee30`](#insn-00acee30) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee34`](#insn-00acee34) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee38`](#insn-00acee38) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee48`](#insn-00acee48) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee50`](#insn-00acee50) → [`00acee8c`](#insn-00acee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acee58`](#insn-00acee58) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`00acee8c`](#insn-00acee8c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acecc8`](#insn-00acecc8)

~~~json
{
  "source": "00acecc8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceccc`](#insn-00aceccc)

~~~json
{
  "source": "00aceccc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecd0`](#insn-00acecd0)

~~~json
{
  "source": "00acecd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecd4`](#insn-00acecd4)

~~~json
{
  "source": "00acecd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecd8`](#insn-00acecd8)

~~~json
{
  "source": "00acecd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecdc`](#insn-00acecdc)

~~~json
{
  "source": "00acecdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecf8`](#insn-00acecf8)

~~~json
{
  "source": "00acecf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acecfc`](#insn-00acecfc)

~~~json
{
  "source": "00acecfc",
  "target": "00802710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced08`](#insn-00aced08)

~~~json
{
  "source": "00aced08",
  "target": "00aced1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced18`](#insn-00aced18)

~~~json
{
  "source": "00aced18",
  "target": "00acee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced2c`](#insn-00aced2c)

~~~json
{
  "source": "00aced2c",
  "target": "00acede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced34`](#insn-00aced34)

~~~json
{
  "source": "00aced34",
  "target": "00aced44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced40`](#insn-00aced40)

~~~json
{
  "source": "00aced40",
  "target": "00acede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced4c`](#insn-00aced4c)

~~~json
{
  "source": "00aced4c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced50`](#insn-00aced50)

~~~json
{
  "source": "00aced50",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced58`](#insn-00aced58)

~~~json
{
  "source": "00aced58",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced5c`](#insn-00aced5c)

~~~json
{
  "source": "00aced5c",
  "target": "00aceda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced60`](#insn-00aced60)

~~~json
{
  "source": "00aced60",
  "target": "00acee44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced68`](#insn-00aced68)

~~~json
{
  "source": "00aced68",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced78`](#insn-00aced78)

~~~json
{
  "source": "00aced78",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aced80`](#insn-00aced80)

~~~json
{
  "source": "00aced80",
  "target": "00aceda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced90`](#insn-00aced90)

~~~json
{
  "source": "00aced90",
  "target": "00acedd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aced9c`](#insn-00aced9c)

~~~json
{
  "source": "00aced9c",
  "target": "00aced88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceda4`](#insn-00aceda4)

~~~json
{
  "source": "00aceda4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acedac`](#insn-00acedac)

~~~json
{
  "source": "00acedac",
  "target": "00acedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedb8`](#insn-00acedb8)

~~~json
{
  "source": "00acedb8",
  "target": "00acedb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedbc`](#insn-00acedbc)

~~~json
{
  "source": "00acedbc",
  "target": "00aced38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedd0`](#insn-00acedd0)

~~~json
{
  "source": "00acedd0",
  "target": "00acedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedd4`](#insn-00acedd4)

~~~json
{
  "source": "00acedd4",
  "target": "00aced38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceddc`](#insn-00aceddc)

~~~json
{
  "source": "00aceddc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acede4`](#insn-00acede4)

~~~json
{
  "source": "00acede4",
  "target": "00acee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acedf4`](#insn-00acedf4)

~~~json
{
  "source": "00acedf4",
  "target": "00acee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee00`](#insn-00acee00)

~~~json
{
  "source": "00acee00",
  "target": "00aeae8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee0c`](#insn-00acee0c)

~~~json
{
  "source": "00acee0c",
  "target": "00acee14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee18`](#insn-00acee18)

~~~json
{
  "source": "00acee18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee20`](#insn-00acee20)

~~~json
{
  "source": "00acee20",
  "target": "00acee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee24`](#insn-00acee24)

~~~json
{
  "source": "00acee24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee28`](#insn-00acee28)

~~~json
{
  "source": "00acee28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee2c`](#insn-00acee2c)

~~~json
{
  "source": "00acee2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee30`](#insn-00acee30)

~~~json
{
  "source": "00acee30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee34`](#insn-00acee34)

~~~json
{
  "source": "00acee34",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee38`](#insn-00acee38)

~~~json
{
  "source": "00acee38",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee48`](#insn-00acee48)

~~~json
{
  "source": "00acee48",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee50`](#insn-00acee50)

~~~json
{
  "source": "00acee50",
  "target": "00acee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acee58`](#insn-00acee58)

~~~json
{
  "source": "00acee58",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acee8c`](#insn-00acee8c)

~~~json
{
  "source": "00acee8c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
