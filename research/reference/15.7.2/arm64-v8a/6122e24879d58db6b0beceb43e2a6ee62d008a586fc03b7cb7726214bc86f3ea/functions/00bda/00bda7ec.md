# 00bda7ec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bda8ac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-1cf76fc2e50dbd9ee92688a2e0e37df9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda7ec",
  "name": "FUN_00bda7ec",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "502a53eca6ac0f884da7445243f2be61b0a11fa5e3a50655be4319934419cc61",
  "source_text_sha256": "502a53eca6ac0f884da7445243f2be61b0a11fa5e3a50655be4319934419cc61",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda7ec",
        "00bda9b3"
      ]
    ],
    "bytes_sha256": "25974cc79929aa27e32d261cc8ce8f119503ce1d8903073bb91c9f05b229e56c",
    "instruction_count": 114,
    "instruction_bytes": 456,
    "body_bytes": 456,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bda2c8](../00bda/00bda2c8.md)

## 呼び出し先

- [00bd7660](../00bd7/00bd7660.md)
- [00bd93b0](../00bd9/00bd93b0.md)
- [00bd973c](../00bd9/00bd973c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2772 bytes

~~~c

undefined8
FUN_00bda7ec(undefined8 param_1,ulong param_2,uint *param_3,long param_4,uint *param_5,
            undefined8 *param_6,long param_7)

{
  uint *puVar1;
  byte bVar2;
  uint *puVar3;
  long lVar4;
  long lVar5;
  undefined8 uVar6;
  uint *puVar7;
  ulong uVar8;
  uint *puVar9;
  uint *local_68;
  
  puVar9 = (uint *)(param_4 + (long)param_3);
  puVar1 = param_3;
  if (param_5 != (uint *)0x0) {
    puVar1 = param_5;
  }
  if (param_4 == -1) {
    puVar9 = (uint *)0xffffffffffffffff;
  }
  while( true ) {
    puVar3 = puVar1;
                    /* catch() { ... } // from try @ 00bda720 with catch @ 00bda82c */
    if (puVar9 <= puVar3) {
      return 0;
    }
    local_68 = puVar3 + 1;
    uVar8 = (ulong)*puVar3;
    if (*puVar3 == 0xffffffff) {
                    /* try { // try from 00bda86c to 00cda8df has its CatchHandler @ 00bda86c
                       catch() { ... } // from try @ 00bda86c with catch @ 00bda86c
                       catch() { ... } // from try @ 00bda8f4 with catch @ 00bda86c */
      uVar8 = *(ulong *)(puVar3 + 1);
      local_68 = puVar3 + 3;
    }
    if (uVar8 == 0) break;
    puVar1 = (uint *)((long)local_68 + uVar8);
    if ((((*local_68 != 0) &&
         (puVar7 = (uint *)((long)local_68 - (ulong)*local_68), param_3 <= puVar7)) &&
        (puVar7 < puVar9)) && (lVar4 = FUN_00bd7660(param_1,puVar7,param_7), lVar4 == 0)) {
      local_68 = local_68 + 1;
      uVar8 = FUN_00bd93b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x18),0);
                    /* try { // try from 00bda8e0 to 00cda8f3 has its CatchHandler @ 00bda9b0 */
      lVar4 = FUN_00bd93b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x18) & 0xf,0);
                    /* try { // try from 00bda8f4 to 00cda9ef has its CatchHandler @ 00bda86c */
      if ((uVar8 < param_2) && (param_2 <= lVar4 + uVar8)) {
        bVar2 = *(byte *)(param_7 + 0x31);
        param_6[5] = 0;
        puVar9 = local_68;
        if ((bVar2 & 1) != 0) {
          lVar5 = FUN_00bd973c(&local_68,puVar1);
          puVar7 = local_68;
          puVar9 = (uint *)((long)local_68 + lVar5);
          if ((*(byte *)(param_7 + 0x19) != 0xff) &&
             (lVar5 = FUN_00bd93b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x19) & 0xf,0),
             lVar5 != 0)) {
            local_68 = puVar7;
            uVar6 = FUN_00bd93b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x19),0);
            param_6[5] = uVar6;
          }
        }
        param_6[2] = puVar9;
        param_6[3] = uVar8;
        *param_6 = puVar3;
        param_6[1] = (long)puVar1 - (long)puVar3;
        param_6[4] = lVar4 + uVar8;
        return 1;
                    /* catch() { ... } // from try @ 00bda8e0 with catch @ 00bda9b0 */
      }
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bda7ec"></a> `00bda7ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bda7f0"></a> `00bda7f0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda7f4"></a> `00bda7f4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7f8"></a> `00bda7f8` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda7fc"></a> `00bda7fc` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda800"></a> `00bda800` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda804"></a> `00bda804` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda808"></a> `00bda808` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda80c"></a> `00bda80c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda810"></a> `00bda810` | `9f 00 00 f1` | cmp x4,#0x0 | `FALL_THROUGH`
<a id="insn-00bda814"></a> `00bda814` | `68 00 02 8b` | add x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00bda818"></a> `00bda818` | `56 00 84 9a` | csel x22,x2,x4,eq | `FALL_THROUGH`
<a id="insn-00bda81c"></a> `00bda81c` | `7f 04 00 b1` | cmn x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bda820"></a> `00bda820` | `1b 11 9f da` | csinv x27,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00bda824"></a> `00bda824` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda828"></a> `00bda828` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda82c"></a> `00bda82c` | `22 0a 00 54` | b.cs 0x00bda970 | `CONDITIONAL_JUMP`
<a id="insn-00bda830"></a> `00bda830` | `f5 03 06 aa` | mov x21,x6 | `FALL_THROUGH`
<a id="insn-00bda834"></a> `00bda834` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00bda838"></a> `00bda838` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bda83c"></a> `00bda83c` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00bda840"></a> `00bda840` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda844"></a> `00bda844` | `04 00 00 14` | b 0x00bda854 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda848"></a> `00bda848` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda84c"></a> `00bda84c` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda850"></a> `00bda850` | `02 09 00 54` | b.cs 0x00bda970 | `CONDITIONAL_JUMP`
<a id="insn-00bda854"></a> `00bda854` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bda858"></a> `00bda858` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bda85c"></a> `00bda85c` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bda860"></a> `00bda860` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda864"></a> `00bda864` | `3f 05 00 31` | cmn w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bda868"></a> `00bda868` | `81 00 00 54` | b.ne 0x00bda878 | `CONDITIONAL_JUMP`
<a id="insn-00bda86c"></a> `00bda86c` | `49 43 40 f8` | ldur x9,[x26, #0x4] | `FALL_THROUGH`
<a id="insn-00bda870"></a> `00bda870` | `48 33 00 91` | add x8,x26,#0xc | `FALL_THROUGH`
<a id="insn-00bda874"></a> `00bda874` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda878"></a> `00bda878` | `c9 07 00 b4` | cbz x9,0x00bda970 | `CONDITIONAL_JUMP`
<a id="insn-00bda87c"></a> `00bda87c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bda880"></a> `00bda880` | `16 01 09 8b` | add x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bda884"></a> `00bda884` | `2a fe ff 34` | cbz w10,0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda888"></a> `00bda888` | `01 01 0a cb` | sub x1,x8,x10 | `FALL_THROUGH`
<a id="insn-00bda88c"></a> `00bda88c` | `3f 00 17 eb` | cmp x1,x23 | `FALL_THROUGH`
<a id="insn-00bda890"></a> `00bda890` | `c3 fd ff 54` | b.cc 0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda894"></a> `00bda894` | `3f 00 1b eb` | cmp x1,x27 | `FALL_THROUGH`
<a id="insn-00bda898"></a> `00bda898` | `82 fd ff 54` | b.cs 0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda89c"></a> `00bda89c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda8a0"></a> `00bda8a0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bda8a4"></a> `00bda8a4` | `6f f3 ff 97` | bl 0x00bd7660 | `UNCONDITIONAL_CALL`
<a id="insn-00bda8a8"></a> `00bda8a8` | `00 fd ff b5` | cbnz x0,0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda8ac"></a> `00bda8ac` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda8b0"></a> `00bda8b0` | `a3 62 40 39` | ldrb w3,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda8b4"></a> `00bda8b4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda8b8"></a> `00bda8b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda8bc"></a> `00bda8bc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda8c0"></a> `00bda8c0` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda8c4"></a> `00bda8c4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bda8c8"></a> `00bda8c8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda8cc"></a> `00bda8cc` | `b9 fa ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda8d0"></a> `00bda8d0` | `a8 62 40 39` | ldrb w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda8d4"></a> `00bda8d4` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bda8d8"></a> `00bda8d8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda8dc"></a> `00bda8dc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda8e0"></a> `00bda8e0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda8e4"></a> `00bda8e4` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda8e8"></a> `00bda8e8` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bda8ec"></a> `00bda8ec` | `b1 fa ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda8f0"></a> `00bda8f0` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bda8f4"></a> `00bda8f4` | `a2 fa ff 54` | b.cs 0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda8f8"></a> `00bda8f8` | `1c 00 19 8b` | add x28,x0,x25 | `FALL_THROUGH`
<a id="insn-00bda8fc"></a> `00bda8fc` | `9f 03 18 eb` | cmp x28,x24 | `FALL_THROUGH`
<a id="insn-00bda900"></a> `00bda900` | `43 fa ff 54` | b.cc 0x00bda848 | `CONDITIONAL_JUMP`
<a id="insn-00bda904"></a> `00bda904` | `a8 c6 40 39` | ldrb w8,[x21, #0x31] | `FALL_THROUGH`
<a id="insn-00bda908"></a> `00bda908` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bda90c"></a> `00bda90c` | `68 04 00 36` | tbz w8,#0x0,0x00bda998 | `CONDITIONAL_JUMP`
<a id="insn-00bda910"></a> `00bda910` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda914"></a> `00bda914` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bda918"></a> `00bda918` | `89 fb ff 97` | bl 0x00bd973c | `UNCONDITIONAL_CALL`
<a id="insn-00bda91c"></a> `00bda91c` | `a8 66 40 39` | ldrb w8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bda920"></a> `00bda920` | `f8 07 40 f9` | ldr x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda924"></a> `00bda924` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00bda928"></a> `00bda928` | `17 03 00 8b` | add x23,x24,x0 | `FALL_THROUGH`
<a id="insn-00bda92c"></a> `00bda92c` | `80 03 00 54` | b.eq 0x00bda99c | `CONDITIONAL_JUMP`
<a id="insn-00bda930"></a> `00bda930` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda934"></a> `00bda934` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bda938"></a> `00bda938` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda93c"></a> `00bda93c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda940"></a> `00bda940` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda944"></a> `00bda944` | `9b fa ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda948"></a> `00bda948` | `a0 02 00 b4` | cbz x0,0x00bda99c | `CONDITIONAL_JUMP`
<a id="insn-00bda94c"></a> `00bda94c` | `a3 66 40 39` | ldrb w3,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bda950"></a> `00bda950` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda954"></a> `00bda954` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda958"></a> `00bda958` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda95c"></a> `00bda95c` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda960"></a> `00bda960` | `f8 07 00 f9` | str x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda964"></a> `00bda964` | `93 fa ff 97` | bl 0x00bd93b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda968"></a> `00bda968` | `60 16 00 f9` | str x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bda96c"></a> `00bda96c` | `0c 00 00 14` | b 0x00bda99c | `UNCONDITIONAL_JUMP`
<a id="insn-00bda970"></a> `00bda970` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bda974"></a> `00bda974` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda978"></a> `00bda978` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda97c"></a> `00bda97c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda980"></a> `00bda980` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda984"></a> `00bda984` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda988"></a> `00bda988` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda98c"></a> `00bda98c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda990"></a> `00bda990` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bda994"></a> `00bda994` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bda998"></a> `00bda998` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda99c"></a> `00bda99c` | `c8 02 1a cb` | sub x8,x22,x26 | `FALL_THROUGH`
<a id="insn-00bda9a0"></a> `00bda9a0` | `77 66 01 a9` | stp x23,x25,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bda9a4"></a> `00bda9a4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bda9a8"></a> `00bda9a8` | `7a 22 00 a9` | stp x26,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bda9ac"></a> `00bda9ac` | `7c 12 00 f9` | str x28,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bda9b0"></a> `00bda9b0` | `f1 ff ff 17` | b 0x00bda974 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bda7ec`](#insn-00bda7ec) 範囲 `[['00bda7ec', '00bda82b']]`
  - `FALL_THROUGH` [`00bda828`](#insn-00bda828) → [`00bda82c`](#insn-00bda82c)
- ブロック [`00bda82c`](#insn-00bda82c) 範囲 `[['00bda82c', '00bda82f']]`
  - `CONDITIONAL_JUMP` [`00bda82c`](#insn-00bda82c) → [`00bda970`](#insn-00bda970)
  - `FALL_THROUGH` [`00bda82c`](#insn-00bda82c) → [`00bda830`](#insn-00bda830)
- ブロック [`00bda830`](#insn-00bda830) 範囲 `[['00bda830', '00bda847']]`
  - `UNCONDITIONAL_JUMP` [`00bda844`](#insn-00bda844) → [`00bda854`](#insn-00bda854)
- ブロック [`00bda848`](#insn-00bda848) 範囲 `[['00bda848', '00bda853']]`
  - `CONDITIONAL_JUMP` [`00bda850`](#insn-00bda850) → [`00bda970`](#insn-00bda970)
  - `FALL_THROUGH` [`00bda850`](#insn-00bda850) → [`00bda854`](#insn-00bda854)
- ブロック [`00bda854`](#insn-00bda854) 範囲 `[['00bda854', '00bda86b']]`
  - `CONDITIONAL_JUMP` [`00bda868`](#insn-00bda868) → [`00bda878`](#insn-00bda878)
  - `FALL_THROUGH` [`00bda868`](#insn-00bda868) → [`00bda86c`](#insn-00bda86c)
- ブロック [`00bda86c`](#insn-00bda86c) 範囲 `[['00bda86c', '00bda877']]`
  - `FALL_THROUGH` [`00bda874`](#insn-00bda874) → [`00bda878`](#insn-00bda878)
- ブロック [`00bda878`](#insn-00bda878) 範囲 `[['00bda878', '00bda87b']]`
  - `CONDITIONAL_JUMP` [`00bda878`](#insn-00bda878) → [`00bda970`](#insn-00bda970)
  - `FALL_THROUGH` [`00bda878`](#insn-00bda878) → [`00bda87c`](#insn-00bda87c)
- ブロック [`00bda87c`](#insn-00bda87c) 範囲 `[['00bda87c', '00bda887']]`
  - `CONDITIONAL_JUMP` [`00bda884`](#insn-00bda884) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda884`](#insn-00bda884) → [`00bda888`](#insn-00bda888)
- ブロック [`00bda888`](#insn-00bda888) 範囲 `[['00bda888', '00bda893']]`
  - `CONDITIONAL_JUMP` [`00bda890`](#insn-00bda890) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda890`](#insn-00bda890) → [`00bda894`](#insn-00bda894)
- ブロック [`00bda894`](#insn-00bda894) 範囲 `[['00bda894', '00bda89b']]`
  - `CONDITIONAL_JUMP` [`00bda898`](#insn-00bda898) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda898`](#insn-00bda898) → [`00bda89c`](#insn-00bda89c)
- ブロック [`00bda89c`](#insn-00bda89c) 範囲 `[['00bda89c', '00bda8ab']]`
  - `CONDITIONAL_JUMP` [`00bda8a8`](#insn-00bda8a8) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda8a8`](#insn-00bda8a8) → [`00bda8ac`](#insn-00bda8ac)
- ブロック [`00bda8ac`](#insn-00bda8ac) 範囲 `[['00bda8ac', '00bda8df']]`
  - `FALL_THROUGH` [`00bda8dc`](#insn-00bda8dc) → [`00bda8e0`](#insn-00bda8e0)
- ブロック [`00bda8e0`](#insn-00bda8e0) 範囲 `[['00bda8e0', '00bda8f3']]`
  - `FALL_THROUGH` [`00bda8f0`](#insn-00bda8f0) → [`00bda8f4`](#insn-00bda8f4)
- ブロック [`00bda8f4`](#insn-00bda8f4) 範囲 `[['00bda8f4', '00bda8f7']]`
  - `CONDITIONAL_JUMP` [`00bda8f4`](#insn-00bda8f4) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda8f4`](#insn-00bda8f4) → [`00bda8f8`](#insn-00bda8f8)
- ブロック [`00bda8f8`](#insn-00bda8f8) 範囲 `[['00bda8f8', '00bda903']]`
  - `CONDITIONAL_JUMP` [`00bda900`](#insn-00bda900) → [`00bda848`](#insn-00bda848)
  - `FALL_THROUGH` [`00bda900`](#insn-00bda900) → [`00bda904`](#insn-00bda904)
- ブロック [`00bda904`](#insn-00bda904) 範囲 `[['00bda904', '00bda90f']]`
  - `CONDITIONAL_JUMP` [`00bda90c`](#insn-00bda90c) → [`00bda998`](#insn-00bda998)
  - `FALL_THROUGH` [`00bda90c`](#insn-00bda90c) → [`00bda910`](#insn-00bda910)
- ブロック [`00bda910`](#insn-00bda910) 範囲 `[['00bda910', '00bda92f']]`
  - `CONDITIONAL_JUMP` [`00bda92c`](#insn-00bda92c) → [`00bda99c`](#insn-00bda99c)
  - `FALL_THROUGH` [`00bda92c`](#insn-00bda92c) → [`00bda930`](#insn-00bda930)
- ブロック [`00bda930`](#insn-00bda930) 範囲 `[['00bda930', '00bda94b']]`
  - `CONDITIONAL_JUMP` [`00bda948`](#insn-00bda948) → [`00bda99c`](#insn-00bda99c)
  - `FALL_THROUGH` [`00bda948`](#insn-00bda948) → [`00bda94c`](#insn-00bda94c)
- ブロック [`00bda94c`](#insn-00bda94c) 範囲 `[['00bda94c', '00bda96f']]`
  - `UNCONDITIONAL_JUMP` [`00bda96c`](#insn-00bda96c) → [`00bda99c`](#insn-00bda99c)
- ブロック [`00bda970`](#insn-00bda970) 範囲 `[['00bda970', '00bda973']]`
  - `FALL_THROUGH` [`00bda970`](#insn-00bda970) → [`00bda974`](#insn-00bda974)
- ブロック [`00bda974`](#insn-00bda974) 範囲 `[['00bda974', '00bda997']]`
- ブロック [`00bda998`](#insn-00bda998) 範囲 `[['00bda998', '00bda99b']]`
  - `FALL_THROUGH` [`00bda998`](#insn-00bda998) → [`00bda99c`](#insn-00bda99c)
- ブロック [`00bda99c`](#insn-00bda99c) 範囲 `[['00bda99c', '00bda9af']]`
  - `FALL_THROUGH` [`00bda9ac`](#insn-00bda9ac) → [`00bda9b0`](#insn-00bda9b0)
- ブロック [`00bda9b0`](#insn-00bda9b0) 範囲 `[['00bda9b0', '00bda9b3']]`
  - `UNCONDITIONAL_JUMP` [`00bda9b0`](#insn-00bda9b0) → [`00bda974`](#insn-00bda974)

## 命令位置別の参照

- [`00bda7f4`](#insn-00bda7f4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7f8`](#insn-00bda7f8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7fc`](#insn-00bda7fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda800`](#insn-00bda800) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda804`](#insn-00bda804) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda808`](#insn-00bda808) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda824`](#insn-00bda824) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda82c`](#insn-00bda82c) → [`00bda970`](#insn-00bda970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda844`](#insn-00bda844) → [`00bda854`](#insn-00bda854) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda84c`](#insn-00bda84c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda850`](#insn-00bda850) → [`00bda970`](#insn-00bda970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda860`](#insn-00bda860) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda868`](#insn-00bda868) → [`00bda878`](#insn-00bda878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda874`](#insn-00bda874) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda878`](#insn-00bda878) → [`00bda970`](#insn-00bda970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda884`](#insn-00bda884) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda890`](#insn-00bda890) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda898`](#insn-00bda898) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8a4`](#insn-00bda8a4) → [`00bd7660`](../00bd7/00bd7660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd7660` · 推定シンボル `None` · 推定型 `None`
- [`00bda8a8`](#insn-00bda8a8) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8ac`](#insn-00bda8ac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8c8`](#insn-00bda8c8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8cc`](#insn-00bda8cc) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda8ec`](#insn-00bda8ec) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda8f4`](#insn-00bda8f4) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda900`](#insn-00bda900) → [`00bda848`](#insn-00bda848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda90c`](#insn-00bda90c) → [`00bda998`](#insn-00bda998) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda918`](#insn-00bda918) → [`00bd973c`](../00bd9/00bd973c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd973c` · 推定シンボル `None` · 推定型 `None`
- [`00bda920`](#insn-00bda920) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda92c`](#insn-00bda92c) → [`00bda99c`](#insn-00bda99c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda944`](#insn-00bda944) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda948`](#insn-00bda948) → [`00bda99c`](#insn-00bda99c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda960`](#insn-00bda960) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda964`](#insn-00bda964) → [`00bd93b0`](../00bd9/00bd93b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd93b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda96c`](#insn-00bda96c) → [`00bda99c`](#insn-00bda99c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda974`](#insn-00bda974) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda978`](#insn-00bda978) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda97c`](#insn-00bda97c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda980`](#insn-00bda980) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda984`](#insn-00bda984) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda988`](#insn-00bda988) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda998`](#insn-00bda998) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9b0`](#insn-00bda9b0) → [`00bda974`](#insn-00bda974) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda7f4`](#insn-00bda7f4)

~~~json
{
  "source": "00bda7f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7f8`](#insn-00bda7f8)

~~~json
{
  "source": "00bda7f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7fc`](#insn-00bda7fc)

~~~json
{
  "source": "00bda7fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda800`](#insn-00bda800)

~~~json
{
  "source": "00bda800",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda804`](#insn-00bda804)

~~~json
{
  "source": "00bda804",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda808`](#insn-00bda808)

~~~json
{
  "source": "00bda808",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda824`](#insn-00bda824)

~~~json
{
  "source": "00bda824",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda82c`](#insn-00bda82c)

~~~json
{
  "source": "00bda82c",
  "target": "00bda970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda844`](#insn-00bda844)

~~~json
{
  "source": "00bda844",
  "target": "00bda854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda84c`](#insn-00bda84c)

~~~json
{
  "source": "00bda84c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda850`](#insn-00bda850)

~~~json
{
  "source": "00bda850",
  "target": "00bda970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda860`](#insn-00bda860)

~~~json
{
  "source": "00bda860",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda868`](#insn-00bda868)

~~~json
{
  "source": "00bda868",
  "target": "00bda878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda874`](#insn-00bda874)

~~~json
{
  "source": "00bda874",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda878`](#insn-00bda878)

~~~json
{
  "source": "00bda878",
  "target": "00bda970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda884`](#insn-00bda884)

~~~json
{
  "source": "00bda884",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda890`](#insn-00bda890)

~~~json
{
  "source": "00bda890",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda898`](#insn-00bda898)

~~~json
{
  "source": "00bda898",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8a4`](#insn-00bda8a4)

~~~json
{
  "source": "00bda8a4",
  "target": "00bd7660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8a8`](#insn-00bda8a8)

~~~json
{
  "source": "00bda8a8",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8ac`](#insn-00bda8ac)

~~~json
{
  "source": "00bda8ac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8c8`](#insn-00bda8c8)

~~~json
{
  "source": "00bda8c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8cc`](#insn-00bda8cc)

~~~json
{
  "source": "00bda8cc",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8ec`](#insn-00bda8ec)

~~~json
{
  "source": "00bda8ec",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda8f4`](#insn-00bda8f4)

~~~json
{
  "source": "00bda8f4",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda900`](#insn-00bda900)

~~~json
{
  "source": "00bda900",
  "target": "00bda848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda90c`](#insn-00bda90c)

~~~json
{
  "source": "00bda90c",
  "target": "00bda998",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda918`](#insn-00bda918)

~~~json
{
  "source": "00bda918",
  "target": "00bd973c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda920`](#insn-00bda920)

~~~json
{
  "source": "00bda920",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda92c`](#insn-00bda92c)

~~~json
{
  "source": "00bda92c",
  "target": "00bda99c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda944`](#insn-00bda944)

~~~json
{
  "source": "00bda944",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda948`](#insn-00bda948)

~~~json
{
  "source": "00bda948",
  "target": "00bda99c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda960`](#insn-00bda960)

~~~json
{
  "source": "00bda960",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda964`](#insn-00bda964)

~~~json
{
  "source": "00bda964",
  "target": "00bd93b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda96c`](#insn-00bda96c)

~~~json
{
  "source": "00bda96c",
  "target": "00bda99c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda974`](#insn-00bda974)

~~~json
{
  "source": "00bda974",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda978`](#insn-00bda978)

~~~json
{
  "source": "00bda978",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda97c`](#insn-00bda97c)

~~~json
{
  "source": "00bda97c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda980`](#insn-00bda980)

~~~json
{
  "source": "00bda980",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda984`](#insn-00bda984)

~~~json
{
  "source": "00bda984",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda988`](#insn-00bda988)

~~~json
{
  "source": "00bda988",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda998`](#insn-00bda998)

~~~json
{
  "source": "00bda998",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9b0`](#insn-00bda9b0)

~~~json
{
  "source": "00bda9b0",
  "target": "00bda974",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
