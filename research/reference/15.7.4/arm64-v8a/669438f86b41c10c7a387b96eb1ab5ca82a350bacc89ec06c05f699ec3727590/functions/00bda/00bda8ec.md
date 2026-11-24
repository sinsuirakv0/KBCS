# 00bda8ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bda8ac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-abb5b0dfc5ac87f271bb06272a1a25f0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5733c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0079.md#compare-2ef19e2f9dc44f65a0d279979947550a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda8ec",
  "name": "FUN_00bda8ec",
  "size": 456,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "69f9e3e74fb611672321366f0c09c2616fe86173bf6425ac0c18c8ea78b3f10a",
  "source_text_sha256": "69f9e3e74fb611672321366f0c09c2616fe86173bf6425ac0c18c8ea78b3f10a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda8ec",
        "00bdaab3"
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

- [00bda3c8](../00bda/00bda3c8.md)

## 呼び出し先

- [00bd7760](../00bd7/00bd7760.md)
- [00bd94b0](../00bd9/00bd94b0.md)
- [00bd983c](../00bd9/00bd983c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2598 bytes

~~~c

undefined8
FUN_00bda8ec(undefined8 param_1,ulong param_2,uint *param_3,long param_4,uint *param_5,
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
    }
                    /* try { // try from 00bda978 to 00cda9eb has its CatchHandler @ 00bda978
                       catch() { ... } // from try @ 00bda978 with catch @ 00bda978
                       catch() { ... } // from try @ 00bdaa00 with catch @ 00bda978 */
    if (uVar8 == 0) break;
    puVar1 = (uint *)((long)local_68 + uVar8);
    if ((((*local_68 != 0) &&
         (puVar7 = (uint *)((long)local_68 - (ulong)*local_68), param_3 <= puVar7)) &&
        (puVar7 < puVar9)) && (lVar4 = FUN_00bd7760(param_1,puVar7,param_7), lVar4 == 0)) {
      local_68 = local_68 + 1;
      uVar8 = FUN_00bd94b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x18),0);
                    /* try { // try from 00bda9ec to 00cda9ff has its CatchHandler @ 00bdaabc */
      lVar4 = FUN_00bd94b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x18) & 0xf,0);
                    /* try { // try from 00bdaa00 to 00cdaafb has its CatchHandler @ 00bda978 */
      if ((uVar8 < param_2) && (param_2 <= lVar4 + uVar8)) {
        bVar2 = *(byte *)(param_7 + 0x31);
        param_6[5] = 0;
        puVar9 = local_68;
        if ((bVar2 & 1) != 0) {
          lVar5 = FUN_00bd983c(&local_68,puVar1);
          puVar7 = local_68;
          puVar9 = (uint *)((long)local_68 + lVar5);
          if ((*(byte *)(param_7 + 0x19) != 0xff) &&
             (lVar5 = FUN_00bd94b0(param_1,&local_68,puVar1,*(byte *)(param_7 + 0x19) & 0xf,0),
             lVar5 != 0)) {
            local_68 = puVar7;
            uVar6 = FUN_00bd94b0(param_1,&local_68,puVar1,*(undefined1 *)(param_7 + 0x19),0);
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
<a id="insn-00bda8ec"></a> `00bda8ec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bda8f0"></a> `00bda8f0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bda8f4"></a> `00bda8f4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda8f8"></a> `00bda8f8` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda8fc"></a> `00bda8fc` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda900"></a> `00bda900` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda904"></a> `00bda904` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bda908"></a> `00bda908` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bda90c"></a> `00bda90c` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda910"></a> `00bda910` | `9f 00 00 f1` | cmp x4,#0x0 | `FALL_THROUGH`
<a id="insn-00bda914"></a> `00bda914` | `68 00 02 8b` | add x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00bda918"></a> `00bda918` | `56 00 84 9a` | csel x22,x2,x4,eq | `FALL_THROUGH`
<a id="insn-00bda91c"></a> `00bda91c` | `7f 04 00 b1` | cmn x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bda920"></a> `00bda920` | `1b 11 9f da` | csinv x27,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00bda924"></a> `00bda924` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda928"></a> `00bda928` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda92c"></a> `00bda92c` | `22 0a 00 54` | b.cs 0x00bdaa70 | `CONDITIONAL_JUMP`
<a id="insn-00bda930"></a> `00bda930` | `f5 03 06 aa` | mov x21,x6 | `FALL_THROUGH`
<a id="insn-00bda934"></a> `00bda934` | `f3 03 05 aa` | mov x19,x5 | `FALL_THROUGH`
<a id="insn-00bda938"></a> `00bda938` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bda93c"></a> `00bda93c` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-00bda940"></a> `00bda940` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda944"></a> `00bda944` | `04 00 00 14` | b 0x00bda954 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda948"></a> `00bda948` | `df 02 1b eb` | cmp x22,x27 | `FALL_THROUGH`
<a id="insn-00bda94c"></a> `00bda94c` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda950"></a> `00bda950` | `02 09 00 54` | b.cs 0x00bdaa70 | `CONDITIONAL_JUMP`
<a id="insn-00bda954"></a> `00bda954` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bda958"></a> `00bda958` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bda95c"></a> `00bda95c` | `09 45 40 b8` | ldr w9,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bda960"></a> `00bda960` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda964"></a> `00bda964` | `3f 05 00 31` | cmn w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bda968"></a> `00bda968` | `81 00 00 54` | b.ne 0x00bda978 | `CONDITIONAL_JUMP`
<a id="insn-00bda96c"></a> `00bda96c` | `49 43 40 f8` | ldur x9,[x26, #0x4] | `FALL_THROUGH`
<a id="insn-00bda970"></a> `00bda970` | `48 33 00 91` | add x8,x26,#0xc | `FALL_THROUGH`
<a id="insn-00bda974"></a> `00bda974` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda978"></a> `00bda978` | `c9 07 00 b4` | cbz x9,0x00bdaa70 | `CONDITIONAL_JUMP`
<a id="insn-00bda97c"></a> `00bda97c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bda980"></a> `00bda980` | `16 01 09 8b` | add x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00bda984"></a> `00bda984` | `2a fe ff 34` | cbz w10,0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bda988"></a> `00bda988` | `01 01 0a cb` | sub x1,x8,x10 | `FALL_THROUGH`
<a id="insn-00bda98c"></a> `00bda98c` | `3f 00 17 eb` | cmp x1,x23 | `FALL_THROUGH`
<a id="insn-00bda990"></a> `00bda990` | `c3 fd ff 54` | b.cc 0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bda994"></a> `00bda994` | `3f 00 1b eb` | cmp x1,x27 | `FALL_THROUGH`
<a id="insn-00bda998"></a> `00bda998` | `82 fd ff 54` | b.cs 0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bda99c"></a> `00bda99c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda9a0"></a> `00bda9a0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bda9a4"></a> `00bda9a4` | `6f f3 ff 97` | bl 0x00bd7760 | `UNCONDITIONAL_CALL`
<a id="insn-00bda9a8"></a> `00bda9a8` | `00 fd ff b5` | cbnz x0,0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bda9ac"></a> `00bda9ac` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda9b0"></a> `00bda9b0` | `a3 62 40 39` | ldrb w3,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda9b4"></a> `00bda9b4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda9b8"></a> `00bda9b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda9bc"></a> `00bda9bc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda9c0"></a> `00bda9c0` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda9c4"></a> `00bda9c4` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bda9c8"></a> `00bda9c8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bda9cc"></a> `00bda9cc` | `b9 fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda9d0"></a> `00bda9d0` | `a8 62 40 39` | ldrb w8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bda9d4"></a> `00bda9d4` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bda9d8"></a> `00bda9d8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bda9dc"></a> `00bda9dc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda9e0"></a> `00bda9e0` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bda9e4"></a> `00bda9e4` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bda9e8"></a> `00bda9e8` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bda9ec"></a> `00bda9ec` | `b1 fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda9f0"></a> `00bda9f0` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00bda9f4"></a> `00bda9f4` | `a2 fa ff 54` | b.cs 0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bda9f8"></a> `00bda9f8` | `1c 00 19 8b` | add x28,x0,x25 | `FALL_THROUGH`
<a id="insn-00bda9fc"></a> `00bda9fc` | `9f 03 18 eb` | cmp x28,x24 | `FALL_THROUGH`
<a id="insn-00bdaa00"></a> `00bdaa00` | `43 fa ff 54` | b.cc 0x00bda948 | `CONDITIONAL_JUMP`
<a id="insn-00bdaa04"></a> `00bdaa04` | `a8 c6 40 39` | ldrb w8,[x21, #0x31] | `FALL_THROUGH`
<a id="insn-00bdaa08"></a> `00bdaa08` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdaa0c"></a> `00bdaa0c` | `68 04 00 36` | tbz w8,#0x0,0x00bdaa98 | `CONDITIONAL_JUMP`
<a id="insn-00bdaa10"></a> `00bdaa10` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaa14"></a> `00bdaa14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdaa18"></a> `00bdaa18` | `89 fb ff 97` | bl 0x00bd983c | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa1c"></a> `00bdaa1c` | `a8 66 40 39` | ldrb w8,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bdaa20"></a> `00bdaa20` | `f8 07 40 f9` | ldr x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaa24"></a> `00bdaa24` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00bdaa28"></a> `00bdaa28` | `17 03 00 8b` | add x23,x24,x0 | `FALL_THROUGH`
<a id="insn-00bdaa2c"></a> `00bdaa2c` | `80 03 00 54` | b.eq 0x00bdaa9c | `CONDITIONAL_JUMP`
<a id="insn-00bdaa30"></a> `00bdaa30` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaa34"></a> `00bdaa34` | `03 0d 00 12` | and w3,w8,#0xf | `FALL_THROUGH`
<a id="insn-00bdaa38"></a> `00bdaa38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdaa3c"></a> `00bdaa3c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdaa40"></a> `00bdaa40` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bdaa44"></a> `00bdaa44` | `9b fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa48"></a> `00bdaa48` | `a0 02 00 b4` | cbz x0,0x00bdaa9c | `CONDITIONAL_JUMP`
<a id="insn-00bdaa4c"></a> `00bdaa4c` | `a3 66 40 39` | ldrb w3,[x21, #0x19] | `FALL_THROUGH`
<a id="insn-00bdaa50"></a> `00bdaa50` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bdaa54"></a> `00bdaa54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdaa58"></a> `00bdaa58` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bdaa5c"></a> `00bdaa5c` | `e4 03 1f aa` | mov x4,xzr | `FALL_THROUGH`
<a id="insn-00bdaa60"></a> `00bdaa60` | `f8 07 00 f9` | str x24,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaa64"></a> `00bdaa64` | `93 fa ff 97` | bl 0x00bd94b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa68"></a> `00bdaa68` | `60 16 00 f9` | str x0,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bdaa6c"></a> `00bdaa6c` | `0c 00 00 14` | b 0x00bdaa9c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdaa70"></a> `00bdaa70` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdaa74"></a> `00bdaa74` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bdaa78"></a> `00bdaa78` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bdaa7c"></a> `00bdaa7c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdaa80"></a> `00bdaa80` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdaa84"></a> `00bdaa84` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaa88"></a> `00bdaa88` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaa8c"></a> `00bdaa8c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bdaa90"></a> `00bdaa90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdaa94"></a> `00bdaa94` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdaa98"></a> `00bdaa98` | `f7 07 40 f9` | ldr x23,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdaa9c"></a> `00bdaa9c` | `c8 02 1a cb` | sub x8,x22,x26 | `FALL_THROUGH`
<a id="insn-00bdaaa0"></a> `00bdaaa0` | `77 66 01 a9` | stp x23,x25,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaaa4"></a> `00bdaaa4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaaa8"></a> `00bdaaa8` | `7a 22 00 a9` | stp x26,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdaaac"></a> `00bdaaac` | `7c 12 00 f9` | str x28,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaab0"></a> `00bdaab0` | `f1 ff ff 17` | b 0x00bdaa74 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bda8ec`](#insn-00bda8ec) 範囲 `[['00bda8ec', '00bda92f']]`
  - `CONDITIONAL_JUMP` [`00bda92c`](#insn-00bda92c) → [`00bdaa70`](#insn-00bdaa70)
  - `FALL_THROUGH` [`00bda92c`](#insn-00bda92c) → [`00bda930`](#insn-00bda930)
- ブロック [`00bda930`](#insn-00bda930) 範囲 `[['00bda930', '00bda937']]`
  - `FALL_THROUGH` [`00bda934`](#insn-00bda934) → [`00bda938`](#insn-00bda938)
- ブロック [`00bda938`](#insn-00bda938) 範囲 `[['00bda938', '00bda947']]`
  - `UNCONDITIONAL_JUMP` [`00bda944`](#insn-00bda944) → [`00bda954`](#insn-00bda954)
- ブロック [`00bda948`](#insn-00bda948) 範囲 `[['00bda948', '00bda953']]`
  - `CONDITIONAL_JUMP` [`00bda950`](#insn-00bda950) → [`00bdaa70`](#insn-00bdaa70)
  - `FALL_THROUGH` [`00bda950`](#insn-00bda950) → [`00bda954`](#insn-00bda954)
- ブロック [`00bda954`](#insn-00bda954) 範囲 `[['00bda954', '00bda96b']]`
  - `CONDITIONAL_JUMP` [`00bda968`](#insn-00bda968) → [`00bda978`](#insn-00bda978)
  - `FALL_THROUGH` [`00bda968`](#insn-00bda968) → [`00bda96c`](#insn-00bda96c)
- ブロック [`00bda96c`](#insn-00bda96c) 範囲 `[['00bda96c', '00bda977']]`
  - `FALL_THROUGH` [`00bda974`](#insn-00bda974) → [`00bda978`](#insn-00bda978)
- ブロック [`00bda978`](#insn-00bda978) 範囲 `[['00bda978', '00bda97b']]`
  - `CONDITIONAL_JUMP` [`00bda978`](#insn-00bda978) → [`00bdaa70`](#insn-00bdaa70)
  - `FALL_THROUGH` [`00bda978`](#insn-00bda978) → [`00bda97c`](#insn-00bda97c)
- ブロック [`00bda97c`](#insn-00bda97c) 範囲 `[['00bda97c', '00bda987']]`
  - `CONDITIONAL_JUMP` [`00bda984`](#insn-00bda984) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bda984`](#insn-00bda984) → [`00bda988`](#insn-00bda988)
- ブロック [`00bda988`](#insn-00bda988) 範囲 `[['00bda988', '00bda993']]`
  - `CONDITIONAL_JUMP` [`00bda990`](#insn-00bda990) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bda990`](#insn-00bda990) → [`00bda994`](#insn-00bda994)
- ブロック [`00bda994`](#insn-00bda994) 範囲 `[['00bda994', '00bda99b']]`
  - `CONDITIONAL_JUMP` [`00bda998`](#insn-00bda998) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bda998`](#insn-00bda998) → [`00bda99c`](#insn-00bda99c)
- ブロック [`00bda99c`](#insn-00bda99c) 範囲 `[['00bda99c', '00bda9ab']]`
  - `CONDITIONAL_JUMP` [`00bda9a8`](#insn-00bda9a8) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bda9a8`](#insn-00bda9a8) → [`00bda9ac`](#insn-00bda9ac)
- ブロック [`00bda9ac`](#insn-00bda9ac) 範囲 `[['00bda9ac', '00bda9eb']]`
  - `FALL_THROUGH` [`00bda9e8`](#insn-00bda9e8) → [`00bda9ec`](#insn-00bda9ec)
- ブロック [`00bda9ec`](#insn-00bda9ec) 範囲 `[['00bda9ec', '00bda9f7']]`
  - `CONDITIONAL_JUMP` [`00bda9f4`](#insn-00bda9f4) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bda9f4`](#insn-00bda9f4) → [`00bda9f8`](#insn-00bda9f8)
- ブロック [`00bda9f8`](#insn-00bda9f8) 範囲 `[['00bda9f8', '00bda9ff']]`
  - `FALL_THROUGH` [`00bda9fc`](#insn-00bda9fc) → [`00bdaa00`](#insn-00bdaa00)
- ブロック [`00bdaa00`](#insn-00bdaa00) 範囲 `[['00bdaa00', '00bdaa03']]`
  - `CONDITIONAL_JUMP` [`00bdaa00`](#insn-00bdaa00) → [`00bda948`](#insn-00bda948)
  - `FALL_THROUGH` [`00bdaa00`](#insn-00bdaa00) → [`00bdaa04`](#insn-00bdaa04)
- ブロック [`00bdaa04`](#insn-00bdaa04) 範囲 `[['00bdaa04', '00bdaa0f']]`
  - `CONDITIONAL_JUMP` [`00bdaa0c`](#insn-00bdaa0c) → [`00bdaa98`](#insn-00bdaa98)
  - `FALL_THROUGH` [`00bdaa0c`](#insn-00bdaa0c) → [`00bdaa10`](#insn-00bdaa10)
- ブロック [`00bdaa10`](#insn-00bdaa10) 範囲 `[['00bdaa10', '00bdaa2f']]`
  - `CONDITIONAL_JUMP` [`00bdaa2c`](#insn-00bdaa2c) → [`00bdaa9c`](#insn-00bdaa9c)
  - `FALL_THROUGH` [`00bdaa2c`](#insn-00bdaa2c) → [`00bdaa30`](#insn-00bdaa30)
- ブロック [`00bdaa30`](#insn-00bdaa30) 範囲 `[['00bdaa30', '00bdaa4b']]`
  - `CONDITIONAL_JUMP` [`00bdaa48`](#insn-00bdaa48) → [`00bdaa9c`](#insn-00bdaa9c)
  - `FALL_THROUGH` [`00bdaa48`](#insn-00bdaa48) → [`00bdaa4c`](#insn-00bdaa4c)
- ブロック [`00bdaa4c`](#insn-00bdaa4c) 範囲 `[['00bdaa4c', '00bdaa6f']]`
  - `UNCONDITIONAL_JUMP` [`00bdaa6c`](#insn-00bdaa6c) → [`00bdaa9c`](#insn-00bdaa9c)
- ブロック [`00bdaa70`](#insn-00bdaa70) 範囲 `[['00bdaa70', '00bdaa73']]`
  - `FALL_THROUGH` [`00bdaa70`](#insn-00bdaa70) → [`00bdaa74`](#insn-00bdaa74)
- ブロック [`00bdaa74`](#insn-00bdaa74) 範囲 `[['00bdaa74', '00bdaa97']]`
- ブロック [`00bdaa98`](#insn-00bdaa98) 範囲 `[['00bdaa98', '00bdaa9b']]`
  - `FALL_THROUGH` [`00bdaa98`](#insn-00bdaa98) → [`00bdaa9c`](#insn-00bdaa9c)
- ブロック [`00bdaa9c`](#insn-00bdaa9c) 範囲 `[['00bdaa9c', '00bdaab3']]`
  - `UNCONDITIONAL_JUMP` [`00bdaab0`](#insn-00bdaab0) → [`00bdaa74`](#insn-00bdaa74)

## 命令位置別の参照

- [`00bda8f4`](#insn-00bda8f4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8f8`](#insn-00bda8f8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda8fc`](#insn-00bda8fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda900`](#insn-00bda900) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda904`](#insn-00bda904) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda908`](#insn-00bda908) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda924`](#insn-00bda924) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda92c`](#insn-00bda92c) → [`00bdaa70`](#insn-00bdaa70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda944`](#insn-00bda944) → [`00bda954`](#insn-00bda954) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda94c`](#insn-00bda94c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda950`](#insn-00bda950) → [`00bdaa70`](#insn-00bdaa70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda960`](#insn-00bda960) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda968`](#insn-00bda968) → [`00bda978`](#insn-00bda978) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda974`](#insn-00bda974) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda978`](#insn-00bda978) → [`00bdaa70`](#insn-00bdaa70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda984`](#insn-00bda984) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda990`](#insn-00bda990) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda998`](#insn-00bda998) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9a4`](#insn-00bda9a4) → [`00bd7760`](../00bd7/00bd7760.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd7760` · 推定シンボル `None` · 推定型 `None`
- [`00bda9a8`](#insn-00bda9a8) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9ac`](#insn-00bda9ac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9c8`](#insn-00bda9c8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda9cc`](#insn-00bda9cc) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda9ec`](#insn-00bda9ec) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bda9f4`](#insn-00bda9f4) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa00`](#insn-00bdaa00) → [`00bda948`](#insn-00bda948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa0c`](#insn-00bdaa0c) → [`00bdaa98`](#insn-00bdaa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa18`](#insn-00bdaa18) → [`00bd983c`](../00bd9/00bd983c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd983c` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa20`](#insn-00bdaa20) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa2c`](#insn-00bdaa2c) → [`00bdaa9c`](#insn-00bdaa9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa44`](#insn-00bdaa44) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa48`](#insn-00bdaa48) → [`00bdaa9c`](#insn-00bdaa9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa60`](#insn-00bdaa60) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa64`](#insn-00bdaa64) → [`00bd94b0`](../00bd9/00bd94b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd94b0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa6c`](#insn-00bdaa6c) → [`00bdaa9c`](#insn-00bdaa9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa74`](#insn-00bdaa74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa78`](#insn-00bdaa78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa7c`](#insn-00bdaa7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa80`](#insn-00bdaa80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa84`](#insn-00bdaa84) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa88`](#insn-00bdaa88) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa98`](#insn-00bdaa98) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaab0`](#insn-00bdaab0) → [`00bdaa74`](#insn-00bdaa74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda8f4`](#insn-00bda8f4)

~~~json
{
  "source": "00bda8f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8f8`](#insn-00bda8f8)

~~~json
{
  "source": "00bda8f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda8fc`](#insn-00bda8fc)

~~~json
{
  "source": "00bda8fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda900`](#insn-00bda900)

~~~json
{
  "source": "00bda900",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda904`](#insn-00bda904)

~~~json
{
  "source": "00bda904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda908`](#insn-00bda908)

~~~json
{
  "source": "00bda908",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda924`](#insn-00bda924)

~~~json
{
  "source": "00bda924",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda92c`](#insn-00bda92c)

~~~json
{
  "source": "00bda92c",
  "target": "00bdaa70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda944`](#insn-00bda944)

~~~json
{
  "source": "00bda944",
  "target": "00bda954",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda94c`](#insn-00bda94c)

~~~json
{
  "source": "00bda94c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda950`](#insn-00bda950)

~~~json
{
  "source": "00bda950",
  "target": "00bdaa70",
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
- 参照命令 [`00bda968`](#insn-00bda968)

~~~json
{
  "source": "00bda968",
  "target": "00bda978",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda974`](#insn-00bda974)

~~~json
{
  "source": "00bda974",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda978`](#insn-00bda978)

~~~json
{
  "source": "00bda978",
  "target": "00bdaa70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda984`](#insn-00bda984)

~~~json
{
  "source": "00bda984",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda990`](#insn-00bda990)

~~~json
{
  "source": "00bda990",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda998`](#insn-00bda998)

~~~json
{
  "source": "00bda998",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9a4`](#insn-00bda9a4)

~~~json
{
  "source": "00bda9a4",
  "target": "00bd7760",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9a8`](#insn-00bda9a8)

~~~json
{
  "source": "00bda9a8",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9ac`](#insn-00bda9ac)

~~~json
{
  "source": "00bda9ac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9c8`](#insn-00bda9c8)

~~~json
{
  "source": "00bda9c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda9cc`](#insn-00bda9cc)

~~~json
{
  "source": "00bda9cc",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9ec`](#insn-00bda9ec)

~~~json
{
  "source": "00bda9ec",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda9f4`](#insn-00bda9f4)

~~~json
{
  "source": "00bda9f4",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa00`](#insn-00bdaa00)

~~~json
{
  "source": "00bdaa00",
  "target": "00bda948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa0c`](#insn-00bdaa0c)

~~~json
{
  "source": "00bdaa0c",
  "target": "00bdaa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa18`](#insn-00bdaa18)

~~~json
{
  "source": "00bdaa18",
  "target": "00bd983c",
  "target_space": "ram",
  "resolution": "function"
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
- 参照命令 [`00bdaa2c`](#insn-00bdaa2c)

~~~json
{
  "source": "00bdaa2c",
  "target": "00bdaa9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa44`](#insn-00bdaa44)

~~~json
{
  "source": "00bdaa44",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaa48`](#insn-00bdaa48)

~~~json
{
  "source": "00bdaa48",
  "target": "00bdaa9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa60`](#insn-00bdaa60)

~~~json
{
  "source": "00bdaa60",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa64`](#insn-00bdaa64)

~~~json
{
  "source": "00bdaa64",
  "target": "00bd94b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaa6c`](#insn-00bdaa6c)

~~~json
{
  "source": "00bdaa6c",
  "target": "00bdaa9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa74`](#insn-00bdaa74)

~~~json
{
  "source": "00bdaa74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa78`](#insn-00bdaa78)

~~~json
{
  "source": "00bdaa78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa7c`](#insn-00bdaa7c)

~~~json
{
  "source": "00bdaa7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa80`](#insn-00bdaa80)

~~~json
{
  "source": "00bdaa80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa84`](#insn-00bdaa84)

~~~json
{
  "source": "00bdaa84",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa88`](#insn-00bdaa88)

~~~json
{
  "source": "00bdaa88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa98`](#insn-00bdaa98)

~~~json
{
  "source": "00bdaa98",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaab0`](#insn-00bdaab0)

~~~json
{
  "source": "00bdaab0",
  "target": "00bdaa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
