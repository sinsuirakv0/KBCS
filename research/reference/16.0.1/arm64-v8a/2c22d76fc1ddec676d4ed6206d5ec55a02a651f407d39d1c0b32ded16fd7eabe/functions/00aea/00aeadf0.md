# 00aeadf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aea9c8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-a6edaefc67bf775e37cab602357349e8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aeae8c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aea/00aeae8c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-e1b0fcc73a843cf0ffcd73fe04a10d4d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeadf0",
  "name": "FUN_00aeadf0",
  "size": 368,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac52751192b8c558cac494945e4265f5dcc828c158cc1caf0bb077bebaa03f21",
  "source_text_sha256": "ac52751192b8c558cac494945e4265f5dcc828c158cc1caf0bb077bebaa03f21",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeadf0",
        "00aeaf5b"
      ],
      [
        "00aeaf90",
        "00aeaf93"
      ]
    ],
    "bytes_sha256": "2a3d37501686b36d2a4493082937932470325e4ad7c7971f1aff74dac2643b8c",
    "instruction_count": 92,
    "instruction_bytes": 368,
    "body_bytes": 368,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00acec54](../00ace/00acec54.md)
- [00acee20](../00ace/00acee20.md)
- [00acf1b8](../00acf/00acf1b8.md)

## 呼び出し先

- [00470840](../00470/00470840.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)
- [00c58450](../00c58/00c58450.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4033 bytes

~~~c

int FUN_00aeadf0(long param_1,int param_2)

{
  void *__src;
  size_t __n;
  long lVar1;
  long *plVar2;
  bool bVar3;
  wchar_t *__s;
  wchar_t *pwVar4;
  int iVar5;
  wchar_t *pwVar6;
  long *plVar7;
  long *plVar8;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  plVar7 = *(long **)(param_1 + 0x33c0);
  if (plVar7 == (long *)(param_1 + 0x33c8)) {
    iVar5 = -1;
                    /* catch() { ... } // from try @ 00aeaa30 with catch @ 00aeaf00 */
  }
  else {
    do {
      __src = (void *)plVar7[5];
      iVar5 = (int)(short)plVar7[4];
      local_78 = 0;
      uStack_70 = 0;
      __n = plVar7[6] - (long)__src;
      local_80 = 0;
      if (__n == 0) {
        pwVar6 = (wchar_t *)0x0;
                    /* try { // try from 00aeae98 to 00beae9b has its CatchHandler @ 00aeaf1c */
        __s = (wchar_t *)0x0;
      }
      else {
        if ((long)__n < 0) {
                    /* catch() { ... } // from try @ 00aeab90 with catch @ 00aeaf48 */
                    /* catch() { ... } // from try @ 00aeabf0 with catch @ 00aeaf4c */
                    /* catch() { ... } // from try @ 00aeab20 with catch @ 00aeaf50 */
          if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_00470840(&local_80);
          }
          goto LAB_00aeaf90;
        }
        __s = (wchar_t *)_Znwm(__n);
        pwVar6 = (wchar_t *)((long)__s + __n);
        memcpy(__s,__src,__n);
      }
                    /* try { // try from 00aeaeac to 00beaeaf has its CatchHandler @ 00aeaed4 */
      pwVar4 = wmemchr(__s,param_2 + L'\xc4653600',(long)pwVar6 - (long)__s >> 2);
      if (__s != (wchar_t *)0x0) {
                    /* try { // try from 00aeaec0 to 00beaec3 has its CatchHandler @ 00aeaecc */
                    /* catch() { ... } // from try @ 00aead14 with catch @ 00aeaec4
                       try { // try from 00aeaec4 to 00beaf83 has its CatchHandler @ 00aea974 */
        _ZdlPv(__s);
      }
                    /* catch() { ... } // from try @ 00aeaca8 with catch @ 00aeaec8 */
      if (pwVar4 != (wchar_t *)0x0 && pwVar4 != pwVar6) goto LAB_00aeaf0c;
                    /* catch() { ... } // from try @ 00aead60 with catch @ 00aeaecc
                       catch() { ... } // from try @ 00aeaec0 with catch @ 00aeaecc */
                    /* catch() { ... } // from try @ 00aeaac0 with catch @ 00aeaed0 */
      plVar2 = (long *)plVar7[1];
      plVar8 = plVar7;
      if ((long *)plVar7[1] == (long *)0x0) {
        do {
          plVar7 = (long *)plVar8[2];
                    /* catch() { ... } // from try @ 00aeaa88 with catch @ 00aeaeec */
          bVar3 = (long *)*plVar7 != plVar8;
          plVar8 = plVar7;
                    /* catch() { ... } // from try @ 00aeaa3c with catch @ 00aeaef0 */
        } while (bVar3);
      }
      else {
        do {
                    /* catch() { ... } // from try @ 00aeacf4 with catch @ 00aeaed4
                       catch() { ... } // from try @ 00aeaeac with catch @ 00aeaed4 */
          plVar7 = plVar2;
          plVar2 = (long *)*plVar7;
        } while ((long *)*plVar7 != (long *)0x0);
      }
    } while (plVar7 != (long *)(param_1 + 0x33c8));
    iVar5 = -1;
  }
LAB_00aeaf0c:
                    /* catch() { ... } // from try @ 00aeac38 with catch @ 00aeaf10 */
                    /* catch() { ... } // from try @ 00aeaa20 with catch @ 00aeaf14 */
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aeac84 with catch @ 00aeaf1c
                       catch() { ... } // from try @ 00aeae98 with catch @ 00aeaf1c */
                    /* catch() { ... } // from try @ 00aea9f4 with catch @ 00aeaf20 */
                    /* catch() { ... } // from try @ 00aea9c0 with catch @ 00aeaf3c */
    return iVar5;
  }
LAB_00aeaf90:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeadf0"></a> `00aeadf0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aeadf4"></a> `00aeadf4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeadf8"></a> `00aeadf8` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeadfc"></a> `00aeadfc` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeae00"></a> `00aeae00` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeae04"></a> `00aeae04` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeae08"></a> `00aeae08` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aeae0c"></a> `00aeae0c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aeae10"></a> `00aeae10` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aeae14"></a> `00aeae14` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aeae18"></a> `00aeae18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeae1c"></a> `00aeae1c` | `08 79 86 52` | mov w8,#0x33c8 | `FALL_THROUGH`
<a id="insn-00aeae20"></a> `00aeae20` | `1c e0 59 f9` | ldr x28,[x0, #0x33c0] | `FALL_THROUGH`
<a id="insn-00aeae24"></a> `00aeae24` | `1a 00 08 8b` | add x26,x0,x8 | `FALL_THROUGH`
<a id="insn-00aeae28"></a> `00aeae28` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00aeae2c"></a> `00aeae2c` | `80 06 00 54` | b.eq 0x00aeaefc | `CONDITIONAL_JUMP`
<a id="insn-00aeae30"></a> `00aeae30` | `1b c0 86 52` | mov w27,#0x3600 | `FALL_THROUGH`
<a id="insn-00aeae34"></a> `00aeae34` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aeae38"></a> `00aeae38` | `f9 23 00 91` | add x25,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aeae3c"></a> `00aeae3c` | `bb 8c b8 72` | movk w27,#0xc465, LSL #16 | `FALL_THROUGH`
<a id="insn-00aeae40"></a> `00aeae40` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00aeae44"></a> `00aeae44` | `04 00 00 14` | b 0x00aeae54 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeae48"></a> `00aeae48` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00aeae4c"></a> `00aeae4c` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aeae50"></a> `00aeae50` | `a0 05 00 54` | b.eq 0x00aeaf04 | `CONDITIONAL_JUMP`
<a id="insn-00aeae54"></a> `00aeae54` | `96 a3 42 a9` | ldp x22,x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00aeae58"></a> `00aeae58` | `94 43 c0 79` | ldrsh w20,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00aeae5c"></a> `00aeae5c` | `3f 7f 01 a9` | stp xzr,xzr,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00aeae60"></a> `00aeae60` | `f4 13 00 79` | strh w20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aeae64"></a> `00aeae64` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00aeae68"></a> `00aeae68` | `3f 83 00 f8` | stur xzr,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00aeae6c"></a> `00aeae6c` | `40 01 00 54` | b.eq 0x00aeae94 | `CONDITIONAL_JUMP`
<a id="insn-00aeae70"></a> `00aeae70` | `97 06 f8 b7` | tbnz x23,#0x3f,0x00aeaf40 | `CONDITIONAL_JUMP`
<a id="insn-00aeae74"></a> `00aeae74` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aeae78"></a> `00aeae78` | `06 b4 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeae7c"></a> `00aeae7c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aeae80"></a> `00aeae80` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aeae84"></a> `00aeae84` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aeae88"></a> `00aeae88` | `18 00 17 8b` | add x24,x0,x23 | `FALL_THROUGH`
<a id="insn-00aeae8c"></a> `00aeae8c` | `5d b4 05 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00aeae90"></a> `00aeae90` | `03 00 00 14` | b 0x00aeae9c | `UNCONDITIONAL_JUMP`
<a id="insn-00aeae94"></a> `00aeae94` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00aeae98"></a> `00aeae98` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aeae9c"></a> `00aeae9c` | `08 03 15 cb` | sub x8,x24,x21 | `FALL_THROUGH`
<a id="insn-00aeaea0"></a> `00aeaea0` | `61 02 1b 0b` | add w1,w19,w27 | `FALL_THROUGH`
<a id="insn-00aeaea4"></a> `00aeaea4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aeaea8"></a> `00aeaea8` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aeaeac"></a> `00aeaeac` | `69 b5 05 94` | bl 0x00c58450 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaeb0"></a> `00aeaeb0` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00aeaeb4"></a> `00aeaeb4` | `04 10 58 fa` | ccmp x0,x24,#0x4,ne | `FALL_THROUGH`
<a id="insn-00aeaeb8"></a> `00aeaeb8` | `f6 17 9f 1a` | cset w22,eq | `FALL_THROUGH`
<a id="insn-00aeaebc"></a> `00aeaebc` | `75 00 00 b4` | cbz x21,0x00aeaec8 | `CONDITIONAL_JUMP`
<a id="insn-00aeaec0"></a> `00aeaec0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aeaec4"></a> `00aeaec4` | `fb b3 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaec8"></a> `00aeaec8` | `16 02 00 34` | cbz w22,0x00aeaf08 | `CONDITIONAL_JUMP`
<a id="insn-00aeaecc"></a> `00aeaecc` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00aeaed0"></a> `00aeaed0` | `a9 00 00 b4` | cbz x9,0x00aeaee4 | `CONDITIONAL_JUMP`
<a id="insn-00aeaed4"></a> `00aeaed4` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aeaed8"></a> `00aeaed8` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aeaedc"></a> `00aeaedc` | `c9 ff ff b5` | cbnz x9,0x00aeaed4 | `CONDITIONAL_JUMP`
<a id="insn-00aeaee0"></a> `00aeaee0` | `da ff ff 17` | b 0x00aeae48 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaee4"></a> `00aeaee4` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaee8"></a> `00aeaee8` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00aeaeec"></a> `00aeaeec` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00aeaef0"></a> `00aeaef0` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aeaef4"></a> `00aeaef4` | `81 ff ff 54` | b.ne 0x00aeaee4 | `CONDITIONAL_JUMP`
<a id="insn-00aeaef8"></a> `00aeaef8` | `d4 ff ff 17` | b 0x00aeae48 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaefc"></a> `00aeaefc` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aeaf00"></a> `00aeaf00` | `03 00 00 14` | b 0x00aeaf0c | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaf04"></a> `00aeaf04` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aeaf08"></a> `00aeaf08` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00aeaf0c"></a> `00aeaf0c` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aeaf10"></a> `00aeaf10` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeaf14"></a> `00aeaf14` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeaf18"></a> `00aeaf18` | `c1 03 00 54` | b.ne 0x00aeaf90 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf1c"></a> `00aeaf1c` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00aeaf20"></a> `00aeaf20` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aeaf24"></a> `00aeaf24` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aeaf28"></a> `00aeaf28` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aeaf2c"></a> `00aeaf2c` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aeaf30"></a> `00aeaf30` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aeaf34"></a> `00aeaf34` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aeaf38"></a> `00aeaf38` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aeaf3c"></a> `00aeaf3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aeaf40"></a> `00aeaf40` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aeaf44"></a> `00aeaf44` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aeaf48"></a> `00aeaf48` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aeaf4c"></a> `00aeaf4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aeaf50"></a> `00aeaf50` | `01 02 00 54` | b.ne 0x00aeaf90 | `CONDITIONAL_JUMP`
<a id="insn-00aeaf54"></a> `00aeaf54` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00aeaf58"></a> `00aeaf58` | `3a 16 e6 97` | bl 0x00470840 | `CALL_TERMINATOR`
<a id="insn-00aeaf90"></a> `00aeaf90` | `d4 b3 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeadf0`](#insn-00aeadf0) 範囲 `[['00aeadf0', '00aeae2f']]`
  - `CONDITIONAL_JUMP` [`00aeae2c`](#insn-00aeae2c) → [`00aeaefc`](#insn-00aeaefc)
  - `FALL_THROUGH` [`00aeae2c`](#insn-00aeae2c) → [`00aeae30`](#insn-00aeae30)
- ブロック [`00aeae30`](#insn-00aeae30) 範囲 `[['00aeae30', '00aeae47']]`
  - `UNCONDITIONAL_JUMP` [`00aeae44`](#insn-00aeae44) → [`00aeae54`](#insn-00aeae54)
- ブロック [`00aeae48`](#insn-00aeae48) 範囲 `[['00aeae48', '00aeae53']]`
  - `CONDITIONAL_JUMP` [`00aeae50`](#insn-00aeae50) → [`00aeaf04`](#insn-00aeaf04)
  - `FALL_THROUGH` [`00aeae50`](#insn-00aeae50) → [`00aeae54`](#insn-00aeae54)
- ブロック [`00aeae54`](#insn-00aeae54) 範囲 `[['00aeae54', '00aeae6f']]`
  - `CONDITIONAL_JUMP` [`00aeae6c`](#insn-00aeae6c) → [`00aeae94`](#insn-00aeae94)
  - `FALL_THROUGH` [`00aeae6c`](#insn-00aeae6c) → [`00aeae70`](#insn-00aeae70)
- ブロック [`00aeae70`](#insn-00aeae70) 範囲 `[['00aeae70', '00aeae73']]`
  - `CONDITIONAL_JUMP` [`00aeae70`](#insn-00aeae70) → [`00aeaf40`](#insn-00aeaf40)
  - `FALL_THROUGH` [`00aeae70`](#insn-00aeae70) → [`00aeae74`](#insn-00aeae74)
- ブロック [`00aeae74`](#insn-00aeae74) 範囲 `[['00aeae74', '00aeae93']]`
  - `UNCONDITIONAL_JUMP` [`00aeae90`](#insn-00aeae90) → [`00aeae9c`](#insn-00aeae9c)
- ブロック [`00aeae94`](#insn-00aeae94) 範囲 `[['00aeae94', '00aeae97']]`
  - `FALL_THROUGH` [`00aeae94`](#insn-00aeae94) → [`00aeae98`](#insn-00aeae98)
- ブロック [`00aeae98`](#insn-00aeae98) 範囲 `[['00aeae98', '00aeae9b']]`
  - `FALL_THROUGH` [`00aeae98`](#insn-00aeae98) → [`00aeae9c`](#insn-00aeae9c)
- ブロック [`00aeae9c`](#insn-00aeae9c) 範囲 `[['00aeae9c', '00aeaeab']]`
  - `FALL_THROUGH` [`00aeaea8`](#insn-00aeaea8) → [`00aeaeac`](#insn-00aeaeac)
- ブロック [`00aeaeac`](#insn-00aeaeac) 範囲 `[['00aeaeac', '00aeaebf']]`
  - `CONDITIONAL_JUMP` [`00aeaebc`](#insn-00aeaebc) → [`00aeaec8`](#insn-00aeaec8)
  - `FALL_THROUGH` [`00aeaebc`](#insn-00aeaebc) → [`00aeaec0`](#insn-00aeaec0)
- ブロック [`00aeaec0`](#insn-00aeaec0) 範囲 `[['00aeaec0', '00aeaec3']]`
  - `FALL_THROUGH` [`00aeaec0`](#insn-00aeaec0) → [`00aeaec4`](#insn-00aeaec4)
- ブロック [`00aeaec4`](#insn-00aeaec4) 範囲 `[['00aeaec4', '00aeaec7']]`
  - `FALL_THROUGH` [`00aeaec4`](#insn-00aeaec4) → [`00aeaec8`](#insn-00aeaec8)
- ブロック [`00aeaec8`](#insn-00aeaec8) 範囲 `[['00aeaec8', '00aeaecb']]`
  - `CONDITIONAL_JUMP` [`00aeaec8`](#insn-00aeaec8) → [`00aeaf08`](#insn-00aeaf08)
  - `FALL_THROUGH` [`00aeaec8`](#insn-00aeaec8) → [`00aeaecc`](#insn-00aeaecc)
- ブロック [`00aeaecc`](#insn-00aeaecc) 範囲 `[['00aeaecc', '00aeaecf']]`
  - `FALL_THROUGH` [`00aeaecc`](#insn-00aeaecc) → [`00aeaed0`](#insn-00aeaed0)
- ブロック [`00aeaed0`](#insn-00aeaed0) 範囲 `[['00aeaed0', '00aeaed3']]`
  - `CONDITIONAL_JUMP` [`00aeaed0`](#insn-00aeaed0) → [`00aeaee4`](#insn-00aeaee4)
  - `FALL_THROUGH` [`00aeaed0`](#insn-00aeaed0) → [`00aeaed4`](#insn-00aeaed4)
- ブロック [`00aeaed4`](#insn-00aeaed4) 範囲 `[['00aeaed4', '00aeaedf']]`
  - `CONDITIONAL_JUMP` [`00aeaedc`](#insn-00aeaedc) → [`00aeaed4`](#insn-00aeaed4)
  - `FALL_THROUGH` [`00aeaedc`](#insn-00aeaedc) → [`00aeaee0`](#insn-00aeaee0)
- ブロック [`00aeaee0`](#insn-00aeaee0) 範囲 `[['00aeaee0', '00aeaee3']]`
  - `UNCONDITIONAL_JUMP` [`00aeaee0`](#insn-00aeaee0) → [`00aeae48`](#insn-00aeae48)
- ブロック [`00aeaee4`](#insn-00aeaee4) 範囲 `[['00aeaee4', '00aeaeeb']]`
  - `FALL_THROUGH` [`00aeaee8`](#insn-00aeaee8) → [`00aeaeec`](#insn-00aeaeec)
- ブロック [`00aeaeec`](#insn-00aeaeec) 範囲 `[['00aeaeec', '00aeaeef']]`
  - `FALL_THROUGH` [`00aeaeec`](#insn-00aeaeec) → [`00aeaef0`](#insn-00aeaef0)
- ブロック [`00aeaef0`](#insn-00aeaef0) 範囲 `[['00aeaef0', '00aeaef7']]`
  - `CONDITIONAL_JUMP` [`00aeaef4`](#insn-00aeaef4) → [`00aeaee4`](#insn-00aeaee4)
  - `FALL_THROUGH` [`00aeaef4`](#insn-00aeaef4) → [`00aeaef8`](#insn-00aeaef8)
- ブロック [`00aeaef8`](#insn-00aeaef8) 範囲 `[['00aeaef8', '00aeaefb']]`
  - `UNCONDITIONAL_JUMP` [`00aeaef8`](#insn-00aeaef8) → [`00aeae48`](#insn-00aeae48)
- ブロック [`00aeaefc`](#insn-00aeaefc) 範囲 `[['00aeaefc', '00aeaeff']]`
  - `FALL_THROUGH` [`00aeaefc`](#insn-00aeaefc) → [`00aeaf00`](#insn-00aeaf00)
- ブロック [`00aeaf00`](#insn-00aeaf00) 範囲 `[['00aeaf00', '00aeaf03']]`
  - `UNCONDITIONAL_JUMP` [`00aeaf00`](#insn-00aeaf00) → [`00aeaf0c`](#insn-00aeaf0c)
- ブロック [`00aeaf04`](#insn-00aeaf04) 範囲 `[['00aeaf04', '00aeaf07']]`
  - `FALL_THROUGH` [`00aeaf04`](#insn-00aeaf04) → [`00aeaf08`](#insn-00aeaf08)
- ブロック [`00aeaf08`](#insn-00aeaf08) 範囲 `[['00aeaf08', '00aeaf0b']]`
  - `FALL_THROUGH` [`00aeaf08`](#insn-00aeaf08) → [`00aeaf0c`](#insn-00aeaf0c)
- ブロック [`00aeaf0c`](#insn-00aeaf0c) 範囲 `[['00aeaf0c', '00aeaf0f']]`
  - `FALL_THROUGH` [`00aeaf0c`](#insn-00aeaf0c) → [`00aeaf10`](#insn-00aeaf10)
- ブロック [`00aeaf10`](#insn-00aeaf10) 範囲 `[['00aeaf10', '00aeaf13']]`
  - `FALL_THROUGH` [`00aeaf10`](#insn-00aeaf10) → [`00aeaf14`](#insn-00aeaf14)
- ブロック [`00aeaf14`](#insn-00aeaf14) 範囲 `[['00aeaf14', '00aeaf1b']]`
  - `CONDITIONAL_JUMP` [`00aeaf18`](#insn-00aeaf18) → [`00aeaf90`](#insn-00aeaf90)
  - `FALL_THROUGH` [`00aeaf18`](#insn-00aeaf18) → [`00aeaf1c`](#insn-00aeaf1c)
- ブロック [`00aeaf1c`](#insn-00aeaf1c) 範囲 `[['00aeaf1c', '00aeaf1f']]`
  - `FALL_THROUGH` [`00aeaf1c`](#insn-00aeaf1c) → [`00aeaf20`](#insn-00aeaf20)
- ブロック [`00aeaf20`](#insn-00aeaf20) 範囲 `[['00aeaf20', '00aeaf3b']]`
  - `FALL_THROUGH` [`00aeaf38`](#insn-00aeaf38) → [`00aeaf3c`](#insn-00aeaf3c)
- ブロック [`00aeaf3c`](#insn-00aeaf3c) 範囲 `[['00aeaf3c', '00aeaf3f']]`
- ブロック [`00aeaf40`](#insn-00aeaf40) 範囲 `[['00aeaf40', '00aeaf47']]`
  - `FALL_THROUGH` [`00aeaf44`](#insn-00aeaf44) → [`00aeaf48`](#insn-00aeaf48)
- ブロック [`00aeaf48`](#insn-00aeaf48) 範囲 `[['00aeaf48', '00aeaf4b']]`
  - `FALL_THROUGH` [`00aeaf48`](#insn-00aeaf48) → [`00aeaf4c`](#insn-00aeaf4c)
- ブロック [`00aeaf4c`](#insn-00aeaf4c) 範囲 `[['00aeaf4c', '00aeaf4f']]`
  - `FALL_THROUGH` [`00aeaf4c`](#insn-00aeaf4c) → [`00aeaf50`](#insn-00aeaf50)
- ブロック [`00aeaf50`](#insn-00aeaf50) 範囲 `[['00aeaf50', '00aeaf53']]`
  - `CONDITIONAL_JUMP` [`00aeaf50`](#insn-00aeaf50) → [`00aeaf90`](#insn-00aeaf90)
  - `FALL_THROUGH` [`00aeaf50`](#insn-00aeaf50) → [`00aeaf54`](#insn-00aeaf54)
- ブロック [`00aeaf54`](#insn-00aeaf54) 範囲 `[['00aeaf54', '00aeaf5b']]`
- ブロック [`00aeaf90`](#insn-00aeaf90) 範囲 `[['00aeaf90', '00aeaf93']]`

## 命令位置別の参照

- [`00aeadf4`](#insn-00aeadf4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeadf8`](#insn-00aeadf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeadfc`](#insn-00aeadfc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae00`](#insn-00aeae00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae04`](#insn-00aeae04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae08`](#insn-00aeae08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae18`](#insn-00aeae18) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae2c`](#insn-00aeae2c) → [`00aeaefc`](#insn-00aeaefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae40`](#insn-00aeae40) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae44`](#insn-00aeae44) → [`00aeae54`](#insn-00aeae54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae50`](#insn-00aeae50) → [`00aeaf04`](#insn-00aeaf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae5c`](#insn-00aeae5c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae60`](#insn-00aeae60) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae68`](#insn-00aeae68) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae6c`](#insn-00aeae6c) → [`00aeae94`](#insn-00aeae94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae70`](#insn-00aeae70) → [`00aeaf40`](#insn-00aeaf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae78`](#insn-00aeae78) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aeae8c`](#insn-00aeae8c) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00aeae90`](#insn-00aeae90) → [`00aeae9c`](#insn-00aeae9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaeac`](#insn-00aeaeac) → [`00c58450`](../00c58/00c58450.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58450` · 推定シンボル `None` · 推定型 `None`
- [`00aeaebc`](#insn-00aeaebc) → [`00aeaec8`](#insn-00aeaec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaec4`](#insn-00aeaec4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aeaec8`](#insn-00aeaec8) → [`00aeaf08`](#insn-00aeaf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaed0`](#insn-00aeaed0) → [`00aeaee4`](#insn-00aeaee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaedc`](#insn-00aeaedc) → [`00aeaed4`](#insn-00aeaed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaee0`](#insn-00aeaee0) → [`00aeae48`](#insn-00aeae48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaef4`](#insn-00aeaef4) → [`00aeaee4`](#insn-00aeaee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaef8`](#insn-00aeaef8) → [`00aeae48`](#insn-00aeae48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf00`](#insn-00aeaf00) → [`00aeaf0c`](#insn-00aeaf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf08`](#insn-00aeaf08) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf10`](#insn-00aeaf10) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf18`](#insn-00aeaf18) → [`00aeaf90`](#insn-00aeaf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf20`](#insn-00aeaf20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf24`](#insn-00aeaf24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf28`](#insn-00aeaf28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf2c`](#insn-00aeaf2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf30`](#insn-00aeaf30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf34`](#insn-00aeaf34) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf40`](#insn-00aeaf40) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf48`](#insn-00aeaf48) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf50`](#insn-00aeaf50) → [`00aeaf90`](#insn-00aeaf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf58`](#insn-00aeaf58) → [`00470840`](../00470/00470840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470840` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf90`](#insn-00aeaf90) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeadf4`](#insn-00aeadf4)

~~~json
{
  "source": "00aeadf4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeadf8`](#insn-00aeadf8)

~~~json
{
  "source": "00aeadf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeadfc`](#insn-00aeadfc)

~~~json
{
  "source": "00aeadfc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae00`](#insn-00aeae00)

~~~json
{
  "source": "00aeae00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae04`](#insn-00aeae04)

~~~json
{
  "source": "00aeae04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae08`](#insn-00aeae08)

~~~json
{
  "source": "00aeae08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae18`](#insn-00aeae18)

~~~json
{
  "source": "00aeae18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae2c`](#insn-00aeae2c)

~~~json
{
  "source": "00aeae2c",
  "target": "00aeaefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae40`](#insn-00aeae40)

~~~json
{
  "source": "00aeae40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae44`](#insn-00aeae44)

~~~json
{
  "source": "00aeae44",
  "target": "00aeae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae50`](#insn-00aeae50)

~~~json
{
  "source": "00aeae50",
  "target": "00aeaf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae5c`](#insn-00aeae5c)

~~~json
{
  "source": "00aeae5c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae60`](#insn-00aeae60)

~~~json
{
  "source": "00aeae60",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae68`](#insn-00aeae68)

~~~json
{
  "source": "00aeae68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae6c`](#insn-00aeae6c)

~~~json
{
  "source": "00aeae6c",
  "target": "00aeae94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae70`](#insn-00aeae70)

~~~json
{
  "source": "00aeae70",
  "target": "00aeaf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae78`](#insn-00aeae78)

~~~json
{
  "source": "00aeae78",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeae8c`](#insn-00aeae8c)

~~~json
{
  "source": "00aeae8c",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeae90`](#insn-00aeae90)

~~~json
{
  "source": "00aeae90",
  "target": "00aeae9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaeac`](#insn-00aeaeac)

~~~json
{
  "source": "00aeaeac",
  "target": "00c58450",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaebc`](#insn-00aeaebc)

~~~json
{
  "source": "00aeaebc",
  "target": "00aeaec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaec4`](#insn-00aeaec4)

~~~json
{
  "source": "00aeaec4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaec8`](#insn-00aeaec8)

~~~json
{
  "source": "00aeaec8",
  "target": "00aeaf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaed0`](#insn-00aeaed0)

~~~json
{
  "source": "00aeaed0",
  "target": "00aeaee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaedc`](#insn-00aeaedc)

~~~json
{
  "source": "00aeaedc",
  "target": "00aeaed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaee0`](#insn-00aeaee0)

~~~json
{
  "source": "00aeaee0",
  "target": "00aeae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaef4`](#insn-00aeaef4)

~~~json
{
  "source": "00aeaef4",
  "target": "00aeaee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaef8`](#insn-00aeaef8)

~~~json
{
  "source": "00aeaef8",
  "target": "00aeae48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf00`](#insn-00aeaf00)

~~~json
{
  "source": "00aeaf00",
  "target": "00aeaf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf08`](#insn-00aeaf08)

~~~json
{
  "source": "00aeaf08",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf10`](#insn-00aeaf10)

~~~json
{
  "source": "00aeaf10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf18`](#insn-00aeaf18)

~~~json
{
  "source": "00aeaf18",
  "target": "00aeaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf20`](#insn-00aeaf20)

~~~json
{
  "source": "00aeaf20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf24`](#insn-00aeaf24)

~~~json
{
  "source": "00aeaf24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf28`](#insn-00aeaf28)

~~~json
{
  "source": "00aeaf28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf2c`](#insn-00aeaf2c)

~~~json
{
  "source": "00aeaf2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf30`](#insn-00aeaf30)

~~~json
{
  "source": "00aeaf30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf34`](#insn-00aeaf34)

~~~json
{
  "source": "00aeaf34",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf40`](#insn-00aeaf40)

~~~json
{
  "source": "00aeaf40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf48`](#insn-00aeaf48)

~~~json
{
  "source": "00aeaf48",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf50`](#insn-00aeaf50)

~~~json
{
  "source": "00aeaf50",
  "target": "00aeaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf58`](#insn-00aeaf58)

~~~json
{
  "source": "00aeaf58",
  "target": "00470840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf90`](#insn-00aeaf90)

~~~json
{
  "source": "00aeaf90",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
