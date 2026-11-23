# 00bda8ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bda7ec`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-1cf76fc2e50dbd9ee92688a2e0e37df9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bda8ec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-abb5b0dfc5ac87f271bb06272a1a25f0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda8ac",
  "name": "FUN_00bda8ac",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "447772f401f406af1b41fbe40de4c0979ae4177cba6cb7bbf71eb95d13367de6",
  "source_text_sha256": "447772f401f406af1b41fbe40de4c0979ae4177cba6cb7bbf71eb95d13367de6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda8ac",
        "00bdaa73"
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

- [00bda388](../00bda/00bda388.md)

## 呼び出し先

- [00bd7720](../00bd7/00bd7720.md)
- [00bd9470](../00bd9/00bd9470.md)
- [00bd97fc](../00bd9/00bd97fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2598 bytes

~~~c

undefined8
FUN_00bda8ac(undefined8 param_1,ulong param_2,uint *param_3,long param_4,uint *param_5,
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
    if (puVar9 <= puVar3) {
      return 0;
    }
    local_68 = puVar3 + 1;
    uVar8 = (ulong)*puVar3;
    if (*puVar3 == 0xffffffff) {
      uVar8 = *(ulong *)(puVar3 + 1);
      local_68 = puVar3 + 3;
                    /* try { // try from 00bda934 to 00cda9a7 has its CatchHandler @ 00bda934
                       catch() { ... } // from try @ 00bda934 with catch @ 00bda934
                       catch() { ... } // from try @ 00bda9bc with catch @ 00bda934 */
    }
    if (uVar8 == 0) break;
    puVar1 = (uint *)((long)local_68 + uVar8);
    if ((((*local_68 != 0) &&
         (puVar7 = (uint *)((long)local_68 - (ulong)*local_68), param_3 <= puVar7)) &&
        (puVar7 < puVar9)) && (lVar4 = FUN_00bd7720(param_1,puVar7,param_7), lVar4 == 0)) {
      local_68 = local_68 + 1;
      uVar8 = FUN_00bd9470(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x18),0);
                    /* try { // try from 00bda9a8 to 00cda9bb has its CatchHandler @ 00bdaa78 */
      lVar4 = FUN_00bd9470(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x18) & 0xf,0);
                    /* try { // try from 00bda9bc to 00cdaab7 has its CatchHandler @ 00bda934 */
      if ((uVar8 < param_2) && (param_2 <= lVar4 + uVar8)) {
        bVar2 = *(byte *)(param_7 + 0x31);
        param_6[5] = 0;
        puVar9 = local_68;
        if ((bVar2 & 1) != 0) {
          lVar5 = FUN_00bd97fc(&local_68,puVar1);
          puVar7 = local_68;
          puVar9 = (uint *)((long)local_68 + lVar5);
          if ((*(byte *)(param_7 + 0x19) != 0xff) &&
             (lVar5 = FUN_00bd9470(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x19) & 0xf,0),
             lVar5 != 0)) {
            local_68 = puVar7;
            uVar6 = FUN_00bd9470(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x19),0);
            param_6[5] = uVar6;
          }
        }
        param_6[2] = puVar9;
        param_6[3] = uVar8;
        *param_6 = puVar3;
        param_6[1] = (long)puVar1 - (long)puVar3;
        param_6[4] = lVar4 + uVar8;
        return 1;
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
<a id="insn-00bda8ac"></a> `00bda8ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bda8b0"></a> `00bda8b0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda8b4"></a> `00bda8b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda8b8"></a> `00bda8b8` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda8bc"></a> `00bda8bc` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda8c0"></a> `00bda8c0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda8c4"></a> `00bda8c4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda8c8"></a> `00bda8c8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda8cc"></a> `00bda8cc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda8d0"></a> `00bda8d0` | `9f 00 00 f1` | cmp x4,#0x0 | `FALL_THROUGH`
<a id="insn-00bda8d4"></a> `00bda8d4` | `68 00 02 8b` | add x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00bda8d8"></a> `00bda8d8` | `56 00 84 9a` | csel x22,x2,x4,eq | `FALL_THROUGH`
<a id="insn-00bda8dc"></a> `00bda8dc` | `7f 04 00 b1` | cmn x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bda8e0"></a> `00bda8e0` | `1b 11 9f da` | csinv x27,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00bda8e4"></a> `00bda8e4` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda8e8"></a> `00bda8e8` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda8ec"></a> `00bda8ec` | `22 0a 00 54` | b.cs 0x00bdaa30 | `CONDITIONAL_JUMP`
<a id="insn-00bda8f0"></a> `00bda8f0` | `f5 03 06 aa` | mov x21,x6 | `FALL_THROUGH`
<a id="insn-00bda8f4"></a> `00bda8f4` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00bda8f8"></a> `00bda8f8` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bda8fc"></a> `00bda8fc` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00bda900"></a> `00bda900` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda904"></a> `00bda904` | `04 00 00 14` | b 0x00bda914 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda908"></a> `00bda908` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda90c"></a> `00bda90c` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda910"></a> `00bda910` | `02 09 00 54` | b.cs 0x00bdaa30 | `CONDITIONAL_JUMP`
<a id="insn-00bda914"></a> `00bda914` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bda918"></a> `00bda918` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bda91c"></a> `00bda91c` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bda920"></a> `00bda920` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda924"></a> `00bda924` | `3f 05 00 31` | cmn w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bda928"></a> `00bda928` | `81 00 00 54` | b.ne 0x00bda938 | `CONDITIONAL_JUMP`
<a id="insn-00bda92c"></a> `00bda92c` | `49 43 40 f8` | ldur x9,[x26, #0x4] | `FALL_THROUGH`
<a id="insn-00bda930"></a> `00bda930` | `48 33 00 91` | add x8,x26,#0xc | `FALL_THROUGH`
<a id="insn-00bda934"></a> `00bda934` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda938"></a> `00bda938` | `c9 07 00 b4` | cbz x9,0x00bdaa30 | `CONDITIONAL_JUMP`
<a id="insn-00bda93c"></a> `00bda93c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bda940"></a> `00bda940` | `16 01 09 8b` | add x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bda944"></a> `00bda944` | `2a fe ff 34` | cbz w10,0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda948"></a> `00bda948` | `01 01 0a cb` | sub x1,x8,x10 | `FALL_THROUGH`
<a id="insn-00bda94c"></a> `00bda94c` | `3f 00 17 eb` | cmp x1,x23 | `FALL_THROUGH`
<a id="insn-00bda950"></a> `00bda950` | `c3 fd ff 54` | b.cc 0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda954"></a> `00bda954` | `3f 00 1b eb` | cmp x1,x27 | `FALL_THROUGH`
<a id="insn-00bda958"></a> `00bda958` | `82 fd ff 54` | b.cs 0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda95c"></a> `00bda95c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda960"></a> `00bda960` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bda964"></a> `00bda964` | `6f f3 ff 97` | bl 0x00bd7720 | `UNCONDITIONAL_CALL`
<a id="insn-00bda968"></a> `00bda968` | `00 fd ff b5` | cbnz x0,0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda96c"></a> `00bda96c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda970"></a> `00bda970` | `a3 62 40 39` | ldrb w3,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda974"></a> `00bda974` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda978"></a> `00bda978` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda97c"></a> `00bda97c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda980"></a> `00bda980` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda984"></a> `00bda984` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bda988"></a> `00bda988` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda98c"></a> `00bda98c` | `b9 fa ff 97` | bl 0x00bd9470 | `UNCONDITIONAL_CALL`
<a id="insn-00bda990"></a> `00bda990` | `a8 62 40 39` | ldrb w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda994"></a> `00bda994` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bda998"></a> `00bda998` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda99c"></a> `00bda99c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda9a0"></a> `00bda9a0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda9a4"></a> `00bda9a4` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda9a8"></a> `00bda9a8` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bda9ac"></a> `00bda9ac` | `b1 fa ff 97` | bl 0x00bd9470 | `UNCONDITIONAL_CALL`
<a id="insn-00bda9b0"></a> `00bda9b0` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bda9b4"></a> `00bda9b4` | `a2 fa ff 54` | b.cs 0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda9b8"></a> `00bda9b8` | `1c 00 19 8b` | add x28,x0,x25 | `FALL_THROUGH`
<a id="insn-00bda9bc"></a> `00bda9bc` | `9f 03 18 eb` | cmp x28,x24 | `FALL_THROUGH`
<a id="insn-00bda9c0"></a> `00bda9c0` | `43 fa ff 54` | b.cc 0x00bda908 | `CONDITIONAL_JUMP`
<a id="insn-00bda9c4"></a> `00bda9c4` | `a8 c6 40 39` | ldrb w8,[x21, #0x31] | `FALL_THROUGH`
<a id="insn-00bda9c8"></a> `00bda9c8` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bda9cc"></a> `00bda9cc` | `68 04 00 36` | tbz w8,#0x0,0x00bdaa58 | `CONDITIONAL_JUMP`
<a id="insn-00bda9d0"></a> `00bda9d0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda9d4"></a> `00bda9d4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bda9d8"></a> `00bda9d8` | `89 fb ff 97` | bl 0x00bd97fc | `UNCONDITIONAL_CALL`
<a id="insn-00bda9dc"></a> `00bda9dc` | `a8 66 40 39` | ldrb w8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bda9e0"></a> `00bda9e0` | `f8 07 40 f9` | ldr x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda9e4"></a> `00bda9e4` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00bda9e8"></a> `00bda9e8` | `17 03 00 8b` | add x23,x24,x0 | `FALL_THROUGH`
<a id="insn-00bda9ec"></a> `00bda9ec` | `80 03 00 54` | b.eq 0x00bdaa5c | `CONDITIONAL_JUMP`
<a id="insn-00bda9f0"></a> `00bda9f0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda9f4"></a> `00bda9f4` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bda9f8"></a> `00bda9f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda9fc"></a> `00bda9fc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdaa00"></a> `00bdaa00` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bdaa04"></a> `00bdaa04` | `9b fa ff 97` | bl 0x00bd9470 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa08"></a> `00bdaa08` | `a0 02 00 b4` | cbz x0,0x00bdaa5c | `CONDITIONAL_JUMP`
<a id="insn-00bdaa0c"></a> `00bdaa0c` | `a3 66 40 39` | ldrb w3,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bdaa10"></a> `00bdaa10` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaa14"></a> `00bdaa14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdaa18"></a> `00bdaa18` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdaa1c"></a> `00bdaa1c` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bdaa20"></a> `00bdaa20` | `f8 07 00 f9` | str x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaa24"></a> `00bdaa24` | `93 fa ff 97` | bl 0x00bd9470 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa28"></a> `00bdaa28` | `60 16 00 f9` | str x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdaa2c"></a> `00bdaa2c` | `0c 00 00 14` | b 0x00bdaa5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdaa30"></a> `00bdaa30` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdaa34"></a> `00bdaa34` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdaa38"></a> `00bdaa38` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdaa3c"></a> `00bdaa3c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdaa40"></a> `00bdaa40` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdaa44"></a> `00bdaa44` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaa48"></a> `00bdaa48` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaa4c"></a> `00bdaa4c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdaa50"></a> `00bdaa50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdaa54"></a> `00bdaa54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdaa58"></a> `00bdaa58` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaa5c"></a> `00bdaa5c` | `c8 02 1a cb` | sub x8,x22,x26 | `FALL_THROUGH`
<a id="insn-00bdaa60"></a> `00bdaa60` | `77 66 01 a9` | stp x23,x25,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaa64"></a> `00bdaa64` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaa68"></a> `00bdaa68` | `7a 22 00 a9` | stp x26,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdaa6c"></a> `00bdaa6c` | `7c 12 00 f9` | str x28,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaa70"></a> `00bdaa70` | `f1 ff ff 17` | b 0x00bdaa34 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bda8ac`](#insn-00bda8ac) 範囲 `[['00bda8ac', '00bda8ef']]`
  - `CONDITIONAL_JUMP` [`00bda8ec`](#insn-00bda8ec) → [`00bdaa30`](#insn-00bdaa30)
  - `FALL_THROUGH` [`00bda8ec`](#insn-00bda8ec) → [`00bda8f0`](#insn-00bda8f0)
- ブロック [`00bda8f0`](#insn-00bda8f0) 範囲 `[['00bda8f0', '00bda8f3']]`
  - `FALL_THROUGH` [`00bda8f0`](#insn-00bda8f0) → [`00bda8f4`](#insn-00bda8f4)
- ブロック [`00bda8f4`](#insn-00bda8f4) 範囲 `[['00bda8f4', '00bda907']]`
  - `UNCONDITIONAL_JUMP` [`00bda904`](#insn-00bda904) → [`00bda914`](#insn-00bda914)
- ブロック [`00bda908`](#insn-00bda908) 範囲 `[['00bda908', '00bda913']]`
  - `CONDITIONAL_JUMP` [`00bda910`](#insn-00bda910) → [`00bdaa30`](#insn-00bdaa30)
  - `FALL_THROUGH` [`00bda910`](#insn-00bda910) → [`00bda914`](#insn-00bda914)
- ブロック [`00bda914`](#insn-00bda914) 範囲 `[['00bda914', '00bda92b']]`
  - `CONDITIONAL_JUMP` [`00bda928`](#insn-00bda928) → [`00bda938`](#insn-00bda938)
  - `FALL_THROUGH` [`00bda928`](#insn-00bda928) → [`00bda92c`](#insn-00bda92c)
- ブロック [`00bda92c`](#insn-00bda92c) 範囲 `[['00bda92c', '00bda933']]`
  - `FALL_THROUGH` [`00bda930`](#insn-00bda930) → [`00bda934`](#insn-00bda934)
- ブロック [`00bda934`](#insn-00bda934) 範囲 `[['00bda934', '00bda937']]`
  - `FALL_THROUGH` [`00bda934`](#insn-00bda934) → [`00bda938`](#insn-00bda938)
- ブロック [`00bda938`](#insn-00bda938) 範囲 `[['00bda938', '00bda93b']]`
  - `CONDITIONAL_JUMP` [`00bda938`](#insn-00bda938) → [`00bdaa30`](#insn-00bdaa30)
  - `FALL_THROUGH` [`00bda938`](#insn-00bda938) → [`00bda93c`](#insn-00bda93c)
- ブロック [`00bda93c`](#insn-00bda93c) 範囲 `[['00bda93c', '00bda947']]`
  - `CONDITIONAL_JUMP` [`00bda944`](#insn-00bda944) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda944`](#insn-00bda944) → [`00bda948`](#insn-00bda948)
- ブロック [`00bda948`](#insn-00bda948) 範囲 `[['00bda948', '00bda953']]`
  - `CONDITIONAL_JUMP` [`00bda950`](#insn-00bda950) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda950`](#insn-00bda950) → [`00bda954`](#insn-00bda954)
- ブロック [`00bda954`](#insn-00bda954) 範囲 `[['00bda954', '00bda95b']]`
  - `CONDITIONAL_JUMP` [`00bda958`](#insn-00bda958) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda958`](#insn-00bda958) → [`00bda95c`](#insn-00bda95c)
- ブロック [`00bda95c`](#insn-00bda95c) 範囲 `[['00bda95c', '00bda96b']]`
  - `CONDITIONAL_JUMP` [`00bda968`](#insn-00bda968) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda968`](#insn-00bda968) → [`00bda96c`](#insn-00bda96c)
- ブロック [`00bda96c`](#insn-00bda96c) 範囲 `[['00bda96c', '00bda9a7']]`
  - `FALL_THROUGH` [`00bda9a4`](#insn-00bda9a4) → [`00bda9a8`](#insn-00bda9a8)
- ブロック [`00bda9a8`](#insn-00bda9a8) 範囲 `[['00bda9a8', '00bda9b7']]`
  - `CONDITIONAL_JUMP` [`00bda9b4`](#insn-00bda9b4) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda9b4`](#insn-00bda9b4) → [`00bda9b8`](#insn-00bda9b8)
- ブロック [`00bda9b8`](#insn-00bda9b8) 範囲 `[['00bda9b8', '00bda9bb']]`
  - `FALL_THROUGH` [`00bda9b8`](#insn-00bda9b8) → [`00bda9bc`](#insn-00bda9bc)
- ブロック [`00bda9bc`](#insn-00bda9bc) 範囲 `[['00bda9bc', '00bda9c3']]`
  - `CONDITIONAL_JUMP` [`00bda9c0`](#insn-00bda9c0) → [`00bda908`](#insn-00bda908)
  - `FALL_THROUGH` [`00bda9c0`](#insn-00bda9c0) → [`00bda9c4`](#insn-00bda9c4)
- ブロック [`00bda9c4`](#insn-00bda9c4) 範囲 `[['00bda9c4', '00bda9cf']]`
  - `CONDITIONAL_JUMP` [`00bda9cc`](#insn-00bda9cc) → [`00bdaa58`](#insn-00bdaa58)
  - `FALL_THROUGH` [`00bda9cc`](#insn-00bda9cc) → [`00bda9d0`](#insn-00bda9d0)
- ブロック [`00bda9d0`](#insn-00bda9d0) 範囲 `[['00bda9d0', '00bda9ef']]`
  - `CONDITIONAL_JUMP` [`00bda9ec`](#insn-00bda9ec) → [`00bdaa5c`](#insn-00bdaa5c)
  - `FALL_THROUGH` [`00bda9ec`](#insn-00bda9ec) → [`00bda9f0`](#insn-00bda9f0)
- ブロック [`00bda9f0`](#insn-00bda9f0) 範囲 `[['00bda9f0', '00bdaa0b']]`
  - `CONDITIONAL_JUMP` [`00bdaa08`](#insn-00bdaa08) → [`00bdaa5c`](#insn-00bdaa5c)
  - `FALL_THROUGH` [`00bdaa08`](#insn-00bdaa08) → [`00bdaa0c`](#insn-00bdaa0c)
- ブロック [`00bdaa0c`](#insn-00bdaa0c) 範囲 `[['00bdaa0c', '00bdaa2f']]`
  - `UNCONDITIONAL_JUMP` [`00bdaa2c`](#insn-00bdaa2c) → [`00bdaa5c`](#insn-00bdaa5c)
- ブロック [`00bdaa30`](#insn-00bdaa30) 範囲 `[['00bdaa30', '00bdaa33']]`
  - `FALL_THROUGH` [`00bdaa30`](#insn-00bdaa30) → [`00bdaa34`](#insn-00bdaa34)
- ブロック [`00bdaa34`](#insn-00bdaa34) 範囲 `[['00bdaa34', '00bdaa57']]`
- ブロック [`00bdaa58`](#insn-00bdaa58) 範囲 `[['00bdaa58', '00bdaa5b']]`
  - `FALL_THROUGH` [`00bdaa58`](#insn-00bdaa58) → [`00bdaa5c`](#insn-00bdaa5c)
- ブロック [`00bdaa5c`](#insn-00bdaa5c) 範囲 `[['00bdaa5c', '00bdaa73']]`
  - `UNCONDITIONAL_JUMP` [`00bdaa70`](#insn-00bdaa70) → [`00bdaa34`](#insn-00bdaa34)

## 命令位置別の参照

- [`00bda8b4`](#insn-00bda8b4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8b8`](#insn-00bda8b8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8bc`](#insn-00bda8bc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8c0`](#insn-00bda8c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8c4`](#insn-00bda8c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8c8`](#insn-00bda8c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8e4`](#insn-00bda8e4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8ec`](#insn-00bda8ec) → [`00bdaa30`](#insn-00bdaa30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda904`](#insn-00bda904) → [`00bda914`](#insn-00bda914) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda90c`](#insn-00bda90c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda910`](#insn-00bda910) → [`00bdaa30`](#insn-00bdaa30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda920`](#insn-00bda920) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda928`](#insn-00bda928) → [`00bda938`](#insn-00bda938) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda934`](#insn-00bda934) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda938`](#insn-00bda938) → [`00bdaa30`](#insn-00bdaa30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda944`](#insn-00bda944) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda950`](#insn-00bda950) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda958`](#insn-00bda958) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda964`](#insn-00bda964) → [`00bd7720`](../00bd7/00bd7720.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd7720` · 推定シンボル `None` · 推定型 `None`
- [`00bda968`](#insn-00bda968) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda96c`](#insn-00bda96c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda988`](#insn-00bda988) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda98c`](#insn-00bda98c) → [`00bd9470`](../00bd9/00bd9470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd9470` · 推定シンボル `None` · 推定型 `None`
- [`00bda9ac`](#insn-00bda9ac) → [`00bd9470`](../00bd9/00bd9470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd9470` · 推定シンボル `None` · 推定型 `None`
- [`00bda9b4`](#insn-00bda9b4) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9c0`](#insn-00bda9c0) → [`00bda908`](#insn-00bda908) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9cc`](#insn-00bda9cc) → [`00bdaa58`](#insn-00bdaa58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9d8`](#insn-00bda9d8) → [`00bd97fc`](../00bd9/00bd97fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd97fc` · 推定シンボル `None` · 推定型 `None`
- [`00bda9e0`](#insn-00bda9e0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9ec`](#insn-00bda9ec) → [`00bdaa5c`](#insn-00bdaa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa04`](#insn-00bdaa04) → [`00bd9470`](../00bd9/00bd9470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd9470` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa08`](#insn-00bdaa08) → [`00bdaa5c`](#insn-00bdaa5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa20`](#insn-00bdaa20) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa24`](#insn-00bdaa24) → [`00bd9470`](../00bd9/00bd9470.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd9470` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa2c`](#insn-00bdaa2c) → [`00bdaa5c`](#insn-00bdaa5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa34`](#insn-00bdaa34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa38`](#insn-00bdaa38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa3c`](#insn-00bdaa3c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa40`](#insn-00bdaa40) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa44`](#insn-00bdaa44) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa48`](#insn-00bdaa48) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa58`](#insn-00bdaa58) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa70`](#insn-00bdaa70) → [`00bdaa34`](#insn-00bdaa34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda8b4`](#insn-00bda8b4)

~~~json
{
  "source": "00bda8b4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8b8`](#insn-00bda8b8)

~~~json
{
  "source": "00bda8b8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8bc`](#insn-00bda8bc)

~~~json
{
  "source": "00bda8bc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8c0`](#insn-00bda8c0)

~~~json
{
  "source": "00bda8c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8c4`](#insn-00bda8c4)

~~~json
{
  "source": "00bda8c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8c8`](#insn-00bda8c8)

~~~json
{
  "source": "00bda8c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8e4`](#insn-00bda8e4)

~~~json
{
  "source": "00bda8e4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8ec`](#insn-00bda8ec)

~~~json
{
  "source": "00bda8ec",
  "target": "00bdaa30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda904`](#insn-00bda904)

~~~json
{
  "source": "00bda904",
  "target": "00bda914",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda90c`](#insn-00bda90c)

~~~json
{
  "source": "00bda90c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda910`](#insn-00bda910)

~~~json
{
  "source": "00bda910",
  "target": "00bdaa30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
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
- 参照命令 [`00bda928`](#insn-00bda928)

~~~json
{
  "source": "00bda928",
  "target": "00bda938",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda934`](#insn-00bda934)

~~~json
{
  "source": "00bda934",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda938`](#insn-00bda938)

~~~json
{
  "source": "00bda938",
  "target": "00bdaa30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda944`](#insn-00bda944)

~~~json
{
  "source": "00bda944",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda950`](#insn-00bda950)

~~~json
{
  "source": "00bda950",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda958`](#insn-00bda958)

~~~json
{
  "source": "00bda958",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda964`](#insn-00bda964)

~~~json
{
  "source": "00bda964",
  "target": "00bd7720",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda968`](#insn-00bda968)

~~~json
{
  "source": "00bda968",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda96c`](#insn-00bda96c)

~~~json
{
  "source": "00bda96c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda988`](#insn-00bda988)

~~~json
{
  "source": "00bda988",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda98c`](#insn-00bda98c)

~~~json
{
  "source": "00bda98c",
  "target": "00bd9470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9ac`](#insn-00bda9ac)

~~~json
{
  "source": "00bda9ac",
  "target": "00bd9470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9b4`](#insn-00bda9b4)

~~~json
{
  "source": "00bda9b4",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9c0`](#insn-00bda9c0)

~~~json
{
  "source": "00bda9c0",
  "target": "00bda908",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9cc`](#insn-00bda9cc)

~~~json
{
  "source": "00bda9cc",
  "target": "00bdaa58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9d8`](#insn-00bda9d8)

~~~json
{
  "source": "00bda9d8",
  "target": "00bd97fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9e0`](#insn-00bda9e0)

~~~json
{
  "source": "00bda9e0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9ec`](#insn-00bda9ec)

~~~json
{
  "source": "00bda9ec",
  "target": "00bdaa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa04`](#insn-00bdaa04)

~~~json
{
  "source": "00bdaa04",
  "target": "00bd9470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaa08`](#insn-00bdaa08)

~~~json
{
  "source": "00bdaa08",
  "target": "00bdaa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa20`](#insn-00bdaa20)

~~~json
{
  "source": "00bdaa20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa24`](#insn-00bdaa24)

~~~json
{
  "source": "00bdaa24",
  "target": "00bd9470",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaa2c`](#insn-00bdaa2c)

~~~json
{
  "source": "00bdaa2c",
  "target": "00bdaa5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa34`](#insn-00bdaa34)

~~~json
{
  "source": "00bdaa34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa38`](#insn-00bdaa38)

~~~json
{
  "source": "00bdaa38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa3c`](#insn-00bdaa3c)

~~~json
{
  "source": "00bdaa3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa40`](#insn-00bdaa40)

~~~json
{
  "source": "00bdaa40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa44`](#insn-00bdaa44)

~~~json
{
  "source": "00bdaa44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa48`](#insn-00bdaa48)

~~~json
{
  "source": "00bdaa48",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa58`](#insn-00bdaa58)

~~~json
{
  "source": "00bdaa58",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa70`](#insn-00bdaa70)

~~~json
{
  "source": "00bdaa70",
  "target": "00bdaa34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
