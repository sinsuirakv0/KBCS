# 005baabc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `005baabc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ba/005baabc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0024.md#compare-2ca096dfef23524da9f908e1eb67ab14)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005baabc",
  "name": "FUN_005baabc",
  "size": 1276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afcdd951f3cca5d01149a80cb50e4b45c8dbbd15a0e4948d7dded3a17e7dd05d",
  "source_text_sha256": "afcdd951f3cca5d01149a80cb50e4b45c8dbbd15a0e4948d7dded3a17e7dd05d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005baabc",
        "005bafb7"
      ]
    ],
    "bytes_sha256": "5e44f4af4f74e56ab6a795ab8a19fa46b5f29d7d250b5ec25d6ba8d8078c0fb9",
    "instruction_count": 319,
    "instruction_bytes": 1276,
    "body_bytes": 1276,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005b8d90](../005b8/005b8d90.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00449aec](../00449/00449aec.md)
- [00449bac](../00449/00449bac.md)
- [0044bf2c](../0044b/0044bf2c.md)
- [005ba8bc](../005ba/005ba8bc.md)
- [005ba9c0](../005ba/005ba9c0.md)
- [0081f580](../0081f/0081f580.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb6c0](../00bdb/00bdb6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9798 bytes

~~~c

void FUN_005baabc(ulong param_1,int *param_2,int param_3,undefined4 param_4)

{
  int iVar1;
  long lVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  undefined8 *puVar6;
  int *piVar7;
  undefined8 *puVar8;
  int *piVar9;
  int *piVar10;
  float fVar11;
  float fVar12;
  undefined1 uStack_91;
  int *local_90;
  undefined8 local_88;
  undefined8 *local_80 [3];
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  fVar11 = (float)param_1;
  switch(param_4) {
  case 1:
    param_1 = (ulong)(uint)(fVar11 * 960.0);
    break;
  case 2:
                    /* try { // try from 005bacd0 to 006bad07 has its CatchHandler @ 005ba430 */
    param_1 = (ulong)(uint)(fVar11 + (float)*param_2 / -10.0);
    break;
  case 3:
                    /* try { // try from 005bac88 to 006baccf has its CatchHandler @ 005bafa4 */
    lVar5 = FUN_0081f580();
    fVar12 = (float)(*param_2 + *(int *)(lVar5 + 0x9ee48)) / 10.0;
    goto LAB_005baf80;
  case 4:
    lVar5 = FUN_0081f580();
    iVar4 = *(int *)(BYTE_ARRAY_0032f999 + lVar5 + 0xf);
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    lVar5 = FUN_0081f580();
    iVar1 = 0;
    if (*(int *)(lVar5 + 0x83e6c) != 0) {
      iVar1 = ((iVar4 >> 1) * 100 + 50000) / *(int *)(lVar5 + 0x83e6c);
    }
    fVar12 = (float)((param_2[1] - iVar1) + 0x1e0);
    goto LAB_005baf80;
  case 5:
    lVar5 = FUN_0081f580();
    iVar4 = *(int *)(BYTE_ARRAY_0032f999 + lVar5 + 0xf);
    FUN_0081f580();
    iVar3 = FUN_00449bac();
    lVar5 = FUN_0081f580();
    iVar1 = 0;
    if (*(int *)(lVar5 + 0x83e6c) != 0) {
      iVar1 = (iVar3 * 100 + -52000) / *(int *)(lVar5 + 0x83e6c);
    }
    fVar12 = (float)((iVar1 - iVar4) + 0x208);
    goto LAB_005baf80;
  case 7:
    FUN_0081f580();
    iVar4 = FUN_00449aec();
    goto LAB_005bace4;
  case 9:
    FUN_0081f580();
    iVar4 = FUN_00449bac();
LAB_005bace4:
    fVar12 = (float)iVar4;
    goto LAB_005baf80;
  case 0xb:
    param_1 = (ulong)(uint)(fVar11 + 1.0);
    break;
  case 0xc:
                    /* try { // try from 005bad08 to 006bad13 has its CatchHandler @ 005baf78 */
    param_1 = (ulong)(uint)(fVar11 + 2.0);
    break;
  case 0xd:
    param_1 = (ulong)(uint)(fVar11 / 30.0);
    break;
  case 0xf:
    param_1 = (ulong)(uint)(fVar11 * 255.0);
  case 0xe:
    param_1 = (ulong)(uint)((float)param_1 / 100.0);
    break;
  case 0x10:
    if (DAT_00c249b8 == 0) {
      lVar5 = 0;
    }
    else {
      lVar5 = __dynamic_cast(DAT_00c249b8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8d98,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00bf4450,0);
    }
    piVar9 = *(int **)(param_2 + 0x1c);
    piVar7 = param_2 + 0x1c;
    while (piVar10 = piVar7, piVar9 != (int *)0x0) {
      while (local_90 = piVar9, piVar7 = local_90, local_90[8] <= param_3) {
        if (param_3 <= local_90[8]) goto LAB_005baef0;
        piVar9 = *(int **)(local_90 + 2);
        if (*(int **)(local_90 + 2) == (int *)0x0) {
          piVar10 = local_90 + 2;
          goto LAB_005bae8c;
        }
      }
                    /* try { // try from 005bae60 to 006bae6b has its CatchHandler @ 005baf5c */
      piVar9 = *(int **)local_90;
    }
LAB_005bae8c:
                    /* try { // try from 005bae8c to 006bae97 has its CatchHandler @ 005baf58 */
    local_90 = (int *)_Znwm(0x40);
    local_90[8] = param_3;
    local_90[0xc] = 0;
    local_90[0xd] = 0;
    local_90[0xe] = 0;
    local_90[0xf] = 0;
    local_90[10] = 0;
    local_90[0xb] = 0;
                    /* try { // try from 005baeb8 to 006baec3 has its CatchHandler @ 005baf54 */
    local_90[0] = 0;
    local_90[1] = 0;
    local_90[2] = 0;
    local_90[3] = 0;
    *(int **)(local_90 + 4) = piVar7;
    *(int **)piVar10 = local_90;
                    /* try { // try from 005baec4 to 006baf03 has its CatchHandler @ 005ba430 */
    piVar7 = local_90;
    if (**(long **)(param_2 + 0x1a) != 0) {
      *(long *)(param_2 + 0x1a) = **(long **)(param_2 + 0x1a);
      piVar7 = *(int **)piVar10;
    }
    FUN_00419064(*(undefined8 *)(param_2 + 0x1c),piVar7);
    *(long *)(param_2 + 0x1e) = *(long *)(param_2 + 0x1e) + 1;
LAB_005baef0:
    local_90 = local_90 + 10;
    puVar6 = (undefined8 *)FUN_005ba8bc(lVar5 + 0x16120,&local_88);
                    /* try { // try from 005baf04 to 006baf13 has its CatchHandler @ 005bafcc */
    puVar8 = (undefined8 *)*puVar6;
    if ((undefined8 *)*puVar6 == (undefined8 *)0x0) {
                    /* try { // try from 005baf18 to 006baf4f has its CatchHandler @ 005bafa8 */
      FUN_005ba9c0(local_80,lVar5 + 0x16120,&DAT_002b6fa5,&local_90,&uStack_91);
      *local_80[0] = 0;
      local_80[0][1] = 0;
      local_80[0][2] = local_88;
      *puVar6 = local_80[0];
      puVar8 = local_80[0];
      if (**(long **)(lVar5 + 0x16120) != 0) {
        *(long *)(lVar5 + 0x16120) = **(long **)(lVar5 + 0x16120);
                    /* catch() { ... } // from try @ 005bad80 with catch @ 005baf50
                       try { // try from 005baf50 to 006bb02f has its CatchHandler @ 005ba430 */
                    /* catch() { ... } // from try @ 005baeb8 with catch @ 005baf54 */
        puVar8 = (undefined8 *)*puVar6;
      }
                    /* catch() { ... } // from try @ 005bae8c with catch @ 005baf58 */
                    /* catch() { ... } // from try @ 005bae60 with catch @ 005baf5c */
      FUN_00419064(*(undefined8 *)(lVar5 + 0x16128),puVar8);
                    /* catch() { ... } // from try @ 005bae34 with catch @ 005baf60 */
                    /* catch() { ... } // from try @ 005bae08 with catch @ 005baf64 */
                    /* catch() { ... } // from try @ 005bad5c with catch @ 005baf68 */
      *(long *)(lVar5 + 0x16130) = *(long *)(lVar5 + 0x16130) + 1;
      puVar8 = local_80[0];
    }
    goto LAB_005baf70;
  case 0x11:
    if (DAT_00c249b8 == 0) {
      lVar5 = 0;
    }
    else {
      lVar5 = __dynamic_cast(DAT_00c249b8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8d98,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00bf4450,0);
    }
    piVar9 = *(int **)(param_2 + 0x1c);
    piVar7 = param_2 + 0x1c;
    while (piVar10 = piVar7, piVar9 != (int *)0x0) {
                    /* try { // try from 005bad44 to 006bad4f has its CatchHandler @ 005baf6c */
      while (local_90 = piVar9, piVar7 = local_90, local_90[8] <= param_3) {
        if (param_3 <= local_90[8]) goto LAB_005badc4;
        piVar9 = *(int **)(local_90 + 2);
        if (*(int **)(local_90 + 2) == (int *)0x0) {
                    /* try { // try from 005bad5c to 006bad67 has its CatchHandler @ 005baf68 */
          piVar10 = local_90 + 2;
          goto LAB_005bad60;
        }
      }
      piVar9 = *(int **)local_90;
    }
LAB_005bad60:
    local_90 = (int *)_Znwm(0x40);
    local_90[8] = param_3;
                    /* try { // try from 005bad80 to 006bad8b has its CatchHandler @ 005baf50 */
    local_90[0xc] = 0;
    local_90[0xd] = 0;
    local_90[0xe] = 0;
    local_90[0xf] = 0;
    local_90[10] = 0;
    local_90[0xb] = 0;
    local_90[0] = 0;
    local_90[1] = 0;
    local_90[2] = 0;
    local_90[3] = 0;
    *(int **)(local_90 + 4) = piVar7;
    *(int **)piVar10 = local_90;
                    /* try { // try from 005bad98 to 006bada3 has its CatchHandler @ 005bafe0 */
    piVar7 = local_90;
    if (**(long **)(param_2 + 0x1a) != 0) {
      *(long *)(param_2 + 0x1a) = **(long **)(param_2 + 0x1a);
      piVar7 = *(int **)piVar10;
    }
                    /* try { // try from 005badb0 to 006badbb has its CatchHandler @ 005bafdc */
    FUN_00419064(*(undefined8 *)(param_2 + 0x1c),piVar7);
    *(long *)(param_2 + 0x1e) = *(long *)(param_2 + 0x1e) + 1;
LAB_005badc4:
    local_90 = local_90 + 10;
    puVar6 = (undefined8 *)FUN_005ba8bc(lVar5 + 0x16120,&local_88);
    puVar8 = (undefined8 *)*puVar6;
    if ((undefined8 *)*puVar6 == (undefined8 *)0x0) {
      FUN_005ba9c0(local_80,lVar5 + 0x16120,&DAT_002b6fa5,&local_90,&uStack_91);
                    /* try { // try from 005bae08 to 006bae13 has its CatchHandler @ 005baf64 */
      *local_80[0] = 0;
      local_80[0][1] = 0;
      local_80[0][2] = local_88;
      *puVar6 = local_80[0];
      puVar8 = local_80[0];
      if (**(long **)(lVar5 + 0x16120) != 0) {
        *(long *)(lVar5 + 0x16120) = **(long **)(lVar5 + 0x16120);
        puVar8 = (undefined8 *)*puVar6;
      }
      FUN_00419064(*(undefined8 *)(lVar5 + 0x16128),puVar8);
                    /* try { // try from 005bae34 to 006bae3f has its CatchHandler @ 005baf60 */
      *(long *)(lVar5 + 0x16130) = *(long *)(lVar5 + 0x16130) + 1;
      puVar8 = local_80[0];
    }
LAB_005baf70:
                    /* catch() { ... } // from try @ 005baab0 with catch @ 005baf70 */
                    /* catch() { ... } // from try @ 005ba7b0 with catch @ 005baf74 */
    iVar4 = FUN_0044bf2c(puVar8 + 7);
                    /* catch() { ... } // from try @ 005bad08 with catch @ 005baf78 */
    fVar12 = (float)iVar4;
                    /* catch() { ... } // from try @ 005ba620 with catch @ 005baf7c */
LAB_005baf80:
    param_1 = (ulong)(uint)(fVar12 + fVar11);
  }
                    /* catch() { ... } // from try @ 005ba614 with catch @ 005baf84 */
                    /* catch() { ... } // from try @ 005ba608 with catch @ 005baf8c */
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 005ba5fc with catch @ 005baf94 */
                    /* catch() { ... } // from try @ 005ba5ec with catch @ 005baf9c */
                    /* catch() { ... } // from try @ 005bac88 with catch @ 005bafa4 */
                    /* catch() { ... } // from try @ 005baf18 with catch @ 005bafa8 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(param_1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005baabc"></a> `005baabc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-005baac0"></a> `005baac0` | `e8 23 00 fd` | str d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005baac4"></a> `005baac4` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005baac8"></a> `005baac8` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005baacc"></a> `005baacc` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005baad0"></a> `005baad0` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005baad4"></a> `005baad4` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005baad8"></a> `005baad8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-005baadc"></a> `005baadc` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005baae0"></a> `005baae0` | `48 04 00 51` | sub w8,w2,#0x1 | `FALL_THROUGH`
<a id="insn-005baae4"></a> `005baae4` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005baae8"></a> `005baae8` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-005baaec"></a> `005baaec` | `a9 83 1e f8` | stur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-005baaf0"></a> `005baaf0` | `a8 24 00 54` | b.hi 0x005baf84 | `CONDITIONAL_JUMP`
<a id="insn-005baaf4"></a> `005baaf4` | `69 e8 ff 90` | adrp x9,0x2c6000 | `FALL_THROUGH`
<a id="insn-005baaf8"></a> `005baaf8` | `29 a1 2e 91` | add x9,x9,#0xba8 | `FALL_THROUGH`
<a id="insn-005baafc"></a> `005baafc` | `8a 00 00 10` | adr x10,0x5bab0c | `FALL_THROUGH`
<a id="insn-005bab00"></a> `005bab00` | `2b 79 68 78` | ldrh w11,[x9, x8, LSL #0x1] | `FALL_THROUGH`
<a id="insn-005bab04"></a> `005bab04` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-005bab08"></a> `005bab08` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-005bab0c"></a> `005bab0c` | `08 8e a8 52` | mov w8,#0x44700000 | `FALL_THROUGH`
<a id="insn-005bab10"></a> `005bab10` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005bab14"></a> `005bab14` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bab18"></a> `005bab18` | `1b 01 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bab1c"></a> `005bab1c` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bab20"></a> `005bab20` | `48 33 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-005bab24"></a> `005bab24` | `08 dd 44 f9` | ldr x8,[x8, #0x9b8] | `FALL_THROUGH`
<a id="insn-005bab28"></a> `005bab28` | `68 0f 00 b4` | cbz x8,0x005bad14 | `CONDITIONAL_JUMP`
<a id="insn-005bab2c"></a> `005bab2c` | `69 31 00 d0` | adrp x9,0xbe8000 | `FALL_THROUGH`
<a id="insn-005bab30"></a> `005bab30` | `29 61 36 91` | add x9,x9,#0xd98 | `FALL_THROUGH`
<a id="insn-005bab34"></a> `005bab34` | `c2 31 00 d0` | adrp x2,0xbf4000 | `FALL_THROUGH`
<a id="insn-005bab38"></a> `005bab38` | `42 40 11 91` | add x2,x2,#0x450 | `FALL_THROUGH`
<a id="insn-005bab3c"></a> `005bab3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005bab40"></a> `005bab40` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005bab44"></a> `005bab44` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-005bab48"></a> `005bab48` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-005bab4c"></a> `005bab4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-005bab50"></a> `005bab50` | `dc 82 18 94` | bl 0x00bdb6c0 | `UNCONDITIONAL_CALL`
<a id="insn-005bab54"></a> `005bab54` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-005bab58"></a> `005bab58` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005bab5c"></a> `005bab5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005bab60"></a> `005bab60` | `6e 00 00 14` | b 0x005bad18 | `UNCONDITIONAL_JUMP`
<a id="insn-005bab64"></a> `005bab64` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bab68"></a> `005bab68` | `86 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bab6c"></a> `005bab6c` | `08 35 9f 52` | mov w8,#0xf9a8 | `FALL_THROUGH`
<a id="insn-005bab70"></a> `005bab70` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-005bab74"></a> `005bab74` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005bab78"></a> `005bab78` | `82 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bab7c"></a> `005bab7c` | `0c 3c fa 97` | bl 0x00449bac | `UNCONDITIONAL_CALL`
<a id="insn-005bab80"></a> `005bab80` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-005bab84"></a> `005bab84` | `e9 63 99 12` | mov w9,#0xffff34e0 | `FALL_THROUGH`
<a id="insn-005bab88"></a> `005bab88` | `14 24 08 1b` | madd w20,w0,w8,w9 | `FALL_THROUGH`
<a id="insn-005bab8c"></a> `005bab8c` | `7d 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bab90"></a> `005bab90` | `88 cd 87 52` | mov w8,#0x3e6c | `FALL_THROUGH`
<a id="insn-005bab94"></a> `005bab94` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005bab98"></a> `005bab98` | `08 01 a0 72` | movk w8,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-005bab9c"></a> `005bab9c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005baba0"></a> `005baba0` | `88 0e c8 1a` | sdiv w8,w20,w8 | `FALL_THROUGH`
<a id="insn-005baba4"></a> `005baba4` | `08 01 13 4b` | sub w8,w8,w19 | `FALL_THROUGH`
<a id="insn-005baba8"></a> `005baba8` | `08 21 08 11` | add w8,w8,#0x208 | `FALL_THROUGH`
<a id="insn-005babac"></a> `005babac` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005babb0"></a> `005babb0` | `f4 00 00 14` | b 0x005baf80 | `UNCONDITIONAL_JUMP`
<a id="insn-005babb4"></a> `005babb4` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005babb8"></a> `005babb8` | `48 33 00 d0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-005babbc"></a> `005babbc` | `08 dd 44 f9` | ldr x8,[x8, #0x9b8] | `FALL_THROUGH`
<a id="insn-005babc0"></a> `005babc0` | `08 14 00 b4` | cbz x8,0x005bae40 | `CONDITIONAL_JUMP`
<a id="insn-005babc4"></a> `005babc4` | `69 31 00 d0` | adrp x9,0xbe8000 | `FALL_THROUGH`
<a id="insn-005babc8"></a> `005babc8` | `29 61 36 91` | add x9,x9,#0xd98 | `FALL_THROUGH`
<a id="insn-005babcc"></a> `005babcc` | `c2 31 00 d0` | adrp x2,0xbf4000 | `FALL_THROUGH`
<a id="insn-005babd0"></a> `005babd0` | `42 40 11 91` | add x2,x2,#0x450 | `FALL_THROUGH`
<a id="insn-005babd4"></a> `005babd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005babd8"></a> `005babd8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005babdc"></a> `005babdc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-005babe0"></a> `005babe0` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-005babe4"></a> `005babe4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-005babe8"></a> `005babe8` | `b6 82 18 94` | bl 0x00bdb6c0 | `UNCONDITIONAL_CALL`
<a id="insn-005babec"></a> `005babec` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-005babf0"></a> `005babf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005babf4"></a> `005babf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005babf8"></a> `005babf8` | `93 00 00 14` | b 0x005bae44 | `UNCONDITIONAL_JUMP`
<a id="insn-005babfc"></a> `005babfc` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bac00"></a> `005bac00` | `60 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bac04"></a> `005bac04` | `ba 3b fa 97` | bl 0x00449aec | `UNCONDITIONAL_CALL`
<a id="insn-005bac08"></a> `005bac08` | `37 00 00 14` | b 0x005bace4 | `UNCONDITIONAL_JUMP`
<a id="insn-005bac0c"></a> `005bac0c` | `e8 6f a8 52` | mov w8,#0x437f0000 | `FALL_THROUGH`
<a id="insn-005bac10"></a> `005bac10` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005bac14"></a> `005bac14` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bac18"></a> `005bac18` | `08 59 a8 52` | mov w8,#0x42c80000 | `FALL_THROUGH`
<a id="insn-005bac1c"></a> `005bac1c` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005bac20"></a> `005bac20` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bac24"></a> `005bac24` | `d8 00 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bac28"></a> `005bac28` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bac2c"></a> `005bac2c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005bac30"></a> `005bac30` | `54 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bac34"></a> `005bac34` | `08 35 9f 52` | mov w8,#0xf9a8 | `FALL_THROUGH`
<a id="insn-005bac38"></a> `005bac38` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-005bac3c"></a> `005bac3c` | `0a 6a 98 52` | mov w10,#0xc350 | `FALL_THROUGH`
<a id="insn-005bac40"></a> `005bac40` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-005bac44"></a> `005bac44` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005bac48"></a> `005bac48` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-005bac4c"></a> `005bac4c` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-005bac50"></a> `005bac50` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-005bac54"></a> `005bac54` | `14 29 09 1b` | madd w20,w8,w9,w10 | `FALL_THROUGH`
<a id="insn-005bac58"></a> `005bac58` | `4a 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bac5c"></a> `005bac5c` | `88 cd 87 52` | mov w8,#0x3e6c | `FALL_THROUGH`
<a id="insn-005bac60"></a> `005bac60` | `69 06 40 b9` | ldr w9,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-005bac64"></a> `005bac64` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005bac68"></a> `005bac68` | `08 01 a0 72` | movk w8,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-005bac6c"></a> `005bac6c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005bac70"></a> `005bac70` | `88 0e c8 1a` | sdiv w8,w20,w8 | `FALL_THROUGH`
<a id="insn-005bac74"></a> `005bac74` | `28 01 08 4b` | sub w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005bac78"></a> `005bac78` | `08 81 07 11` | add w8,w8,#0x1e0 | `FALL_THROUGH`
<a id="insn-005bac7c"></a> `005bac7c` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005bac80"></a> `005bac80` | `c0 00 00 14` | b 0x005baf80 | `UNCONDITIONAL_JUMP`
<a id="insn-005bac84"></a> `005bac84` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bac88"></a> `005bac88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005bac8c"></a> `005bac8c` | `3d 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bac90"></a> `005bac90` | `08 c9 9d 52` | mov w8,#0xee48 | `FALL_THROUGH`
<a id="insn-005bac94"></a> `005bac94` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-005bac98"></a> `005bac98` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-005bac9c"></a> `005bac9c` | `28 01 a0 72` | movk w8,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-005baca0"></a> `005baca0` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005baca4"></a> `005baca4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005baca8"></a> `005baca8` | `28 01 08 0b` | add w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005bacac"></a> `005bacac` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005bacb0"></a> `005bacb0` | `21 18 22 1e` | fdiv s1,s1,s2 | `FALL_THROUGH`
<a id="insn-005bacb4"></a> `005bacb4` | `b3 00 00 14` | b 0x005baf80 | `UNCONDITIONAL_JUMP`
<a id="insn-005bacb8"></a> `005bacb8` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-005bacbc"></a> `005bacbc` | `02 90 74 1e` | fmov d2,-0x3fdc000000000000 | `FALL_THROUGH`
<a id="insn-005bacc0"></a> `005bacc0` | `00 c0 22 1e` | fcvt d0,s0 | `FALL_THROUGH`
<a id="insn-005bacc4"></a> `005bacc4` | `01 01 62 1e` | scvtf d1,w8 | `FALL_THROUGH`
<a id="insn-005bacc8"></a> `005bacc8` | `21 18 62 1e` | fdiv d1,d1,d2 | `FALL_THROUGH`
<a id="insn-005baccc"></a> `005baccc` | `00 28 61 1e` | fadd d0,d0,d1 | `FALL_THROUGH`
<a id="insn-005bacd0"></a> `005bacd0` | `00 40 62 1e` | fcvt s0,d0 | `FALL_THROUGH`
<a id="insn-005bacd4"></a> `005bacd4` | `ac 00 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bacd8"></a> `005bacd8` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005bacdc"></a> `005bacdc` | `29 92 09 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-005bace0"></a> `005bace0` | `b3 3b fa 97` | bl 0x00449bac | `UNCONDITIONAL_CALL`
<a id="insn-005bace4"></a> `005bace4` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005bace8"></a> `005bace8` | `01 00 22 1e` | scvtf s1,w0 | `FALL_THROUGH`
<a id="insn-005bacec"></a> `005bacec` | `a5 00 00 14` | b 0x005baf80 | `UNCONDITIONAL_JUMP`
<a id="insn-005bacf0"></a> `005bacf0` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-005bacf4"></a> `005bacf4` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bacf8"></a> `005bacf8` | `a3 00 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bacfc"></a> `005bacfc` | `01 d0 27 1e` | fmov s1,0x41f00000 | `FALL_THROUGH`
<a id="insn-005bad00"></a> `005bad00` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bad04"></a> `005bad04` | `a0 00 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bad08"></a> `005bad08` | `01 10 20 1e` | fmov s1,0x40000000 | `FALL_THROUGH`
<a id="insn-005bad0c"></a> `005bad0c` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005bad10"></a> `005bad10` | `9d 00 00 14` | b 0x005baf84 | `UNCONDITIONAL_JUMP`
<a id="insn-005bad14"></a> `005bad14` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-005bad18"></a> `005bad18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005bad1c"></a> `005bad1c` | `16 24 8c 52` | mov w22,#0x6120 | `FALL_THROUGH`
<a id="insn-005bad20"></a> `005bad20` | `e8 0e 47 f8` | ldr x8,[x23, #0x70]! | `FALL_THROUGH`
<a id="insn-005bad24"></a> `005bad24` | `36 00 a0 72` | movk w22,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-005bad28"></a> `005bad28` | `c8 00 00 b5` | cbnz x8,0x005bad40 | `CONDITIONAL_JUMP`
<a id="insn-005bad2c"></a> `005bad2c` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-005bad30"></a> `005bad30` | `0c 00 00 14` | b 0x005bad60 | `UNCONDITIONAL_JUMP`
<a id="insn-005bad34"></a> `005bad34` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-005bad38"></a> `005bad38` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-005bad3c"></a> `005bad3c` | `28 01 00 b4` | cbz x8,0x005bad60 | `CONDITIONAL_JUMP`
<a id="insn-005bad40"></a> `005bad40` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-005bad44"></a> `005bad44` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-005bad48"></a> `005bad48` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-005bad4c"></a> `005bad4c` | `4c ff ff 54` | b.gt 0x005bad34 | `CONDITIONAL_JUMP`
<a id="insn-005bad50"></a> `005bad50` | `aa 03 00 54` | b.ge 0x005badc4 | `CONDITIONAL_JUMP`
<a id="insn-005bad54"></a> `005bad54` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005bad58"></a> `005bad58` | `48 ff ff b5` | cbnz x8,0x005bad40 | `CONDITIONAL_JUMP`
<a id="insn-005bad5c"></a> `005bad5c` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-005bad60"></a> `005bad60` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-005bad64"></a> `005bad64` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-005bad68"></a> `005bad68` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-005bad6c"></a> `005bad6c` | `fa 03 01 2a` | mov w26,w1 | `FALL_THROUGH`
<a id="insn-005bad70"></a> `005bad70` | `74 80 18 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-005bad74"></a> `005bad74` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-005bad78"></a> `005bad78` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005bad7c"></a> `005bad7c` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-005bad80"></a> `005bad80` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-005bad84"></a> `005bad84` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-005bad88"></a> `005bad88` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-005bad8c"></a> `005bad8c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-005bad90"></a> `005bad90` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-005bad94"></a> `005bad94` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-005bad98"></a> `005bad98` | `09 37 40 f9` | ldr x9,[x24, #0x68] | `FALL_THROUGH`
<a id="insn-005bad9c"></a> `005bad9c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005bada0"></a> `005bada0` | `69 00 00 b4` | cbz x9,0x005badac | `CONDITIONAL_JUMP`
<a id="insn-005bada4"></a> `005bada4` | `09 35 00 f9` | str x9,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-005bada8"></a> `005bada8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005badac"></a> `005badac` | `00 39 40 f9` | ldr x0,[x8, #0x70] | `FALL_THROUGH`
<a id="insn-005badb0"></a> `005badb0` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-005badb4"></a> `005badb4` | `ac 78 f9 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-005badb8"></a> `005badb8` | `e8 3e 40 f9` | ldr x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005badbc"></a> `005badbc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005badc0"></a> `005badc0` | `e8 3e 00 f9` | str x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005badc4"></a> `005badc4` | `82 a2 00 91` | add x2,x20,#0x28 | `FALL_THROUGH`
<a id="insn-005badc8"></a> `005badc8` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005badcc"></a> `005badcc` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-005badd0"></a> `005badd0` | `e2 0b 00 f9` | str x2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005badd4"></a> `005badd4` | `ba fe ff 97` | bl 0x005ba8bc | `UNCONDITIONAL_CALL`
<a id="insn-005badd8"></a> `005badd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-005baddc"></a> `005baddc` | `a8 0c 00 b5` | cbnz x8,0x005baf70 | `CONDITIONAL_JUMP`
<a id="insn-005bade0"></a> `005bade0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005bade4"></a> `005bade4` | `e1 e7 ff 90` | adrp x1,0x2b6000 | `FALL_THROUGH`
<a id="insn-005bade8"></a> `005bade8` | `21 94 3e 91` | add x1,x1,#0xfa5 | `FALL_THROUGH`
<a id="insn-005badec"></a> `005badec` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-005badf0"></a> `005badf0` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005badf4"></a> `005badf4` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-005badf8"></a> `005badf8` | `e3 3f 00 91` | add x3,sp,#0xf | `FALL_THROUGH`
<a id="insn-005badfc"></a> `005badfc` | `77 5a 40 91` | add x23,x19,#0x16, LSL #12 | `FALL_THROUGH`
<a id="insn-005bae00"></a> `005bae00` | `f0 fe ff 97` | bl 0x005ba9c0 | `UNCONDITIONAL_CALL`
<a id="insn-005bae04"></a> `005bae04` | `e8 87 41 a9` | ldp x8,x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005bae08"></a> `005bae08` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-005bae0c"></a> `005bae0c` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-005bae10"></a> `005bae10` | `81 02 00 f9` | str x1,[x20] | `FALL_THROUGH`
<a id="insn-005bae14"></a> `005bae14` | `68 6a 76 f8` | ldr x8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005bae18"></a> `005bae18` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-005bae1c"></a> `005bae1c` | `68 00 00 b4` | cbz x8,0x005bae28 | `CONDITIONAL_JUMP`
<a id="insn-005bae20"></a> `005bae20` | `68 6a 36 f8` | str x8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005bae24"></a> `005bae24` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-005bae28"></a> `005bae28` | `e0 96 40 f9` | ldr x0,[x23, #0x128] | `FALL_THROUGH`
<a id="insn-005bae2c"></a> `005bae2c` | `8e 78 f9 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-005bae30"></a> `005bae30` | `e8 9a 40 f9` | ldr x8,[x23, #0x130] | `FALL_THROUGH`
<a id="insn-005bae34"></a> `005bae34` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005bae38"></a> `005bae38` | `e8 9a 00 f9` | str x8,[x23, #0x130] | `FALL_THROUGH`
<a id="insn-005bae3c"></a> `005bae3c` | `4c 00 00 14` | b 0x005baf6c | `UNCONDITIONAL_JUMP`
<a id="insn-005bae40"></a> `005bae40` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-005bae44"></a> `005bae44` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005bae48"></a> `005bae48` | `16 24 8c 52` | mov w22,#0x6120 | `FALL_THROUGH`
<a id="insn-005bae4c"></a> `005bae4c` | `e8 0e 47 f8` | ldr x8,[x23, #0x70]! | `FALL_THROUGH`
<a id="insn-005bae50"></a> `005bae50` | `36 00 a0 72` | movk w22,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-005bae54"></a> `005bae54` | `c8 00 00 b5` | cbnz x8,0x005bae6c | `CONDITIONAL_JUMP`
<a id="insn-005bae58"></a> `005bae58` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-005bae5c"></a> `005bae5c` | `0c 00 00 14` | b 0x005bae8c | `UNCONDITIONAL_JUMP`
<a id="insn-005bae60"></a> `005bae60` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-005bae64"></a> `005bae64` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-005bae68"></a> `005bae68` | `28 01 00 b4` | cbz x8,0x005bae8c | `CONDITIONAL_JUMP`
<a id="insn-005bae6c"></a> `005bae6c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-005bae70"></a> `005bae70` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-005bae74"></a> `005bae74` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-005bae78"></a> `005bae78` | `4c ff ff 54` | b.gt 0x005bae60 | `CONDITIONAL_JUMP`
<a id="insn-005bae7c"></a> `005bae7c` | `aa 03 00 54` | b.ge 0x005baef0 | `CONDITIONAL_JUMP`
<a id="insn-005bae80"></a> `005bae80` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005bae84"></a> `005bae84` | `48 ff ff b5` | cbnz x8,0x005bae6c | `CONDITIONAL_JUMP`
<a id="insn-005bae88"></a> `005bae88` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-005bae8c"></a> `005bae8c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-005bae90"></a> `005bae90` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-005bae94"></a> `005bae94` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-005bae98"></a> `005bae98` | `fa 03 01 2a` | mov w26,w1 | `FALL_THROUGH`
<a id="insn-005bae9c"></a> `005bae9c` | `29 80 18 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-005baea0"></a> `005baea0` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-005baea4"></a> `005baea4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005baea8"></a> `005baea8` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-005baeac"></a> `005baeac` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-005baeb0"></a> `005baeb0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-005baeb4"></a> `005baeb4` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-005baeb8"></a> `005baeb8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-005baebc"></a> `005baebc` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-005baec0"></a> `005baec0` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-005baec4"></a> `005baec4` | `09 37 40 f9` | ldr x9,[x24, #0x68] | `FALL_THROUGH`
<a id="insn-005baec8"></a> `005baec8` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005baecc"></a> `005baecc` | `69 00 00 b4` | cbz x9,0x005baed8 | `CONDITIONAL_JUMP`
<a id="insn-005baed0"></a> `005baed0` | `09 35 00 f9` | str x9,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-005baed4"></a> `005baed4` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005baed8"></a> `005baed8` | `00 39 40 f9` | ldr x0,[x8, #0x70] | `FALL_THROUGH`
<a id="insn-005baedc"></a> `005baedc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-005baee0"></a> `005baee0` | `61 78 f9 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-005baee4"></a> `005baee4` | `e8 3e 40 f9` | ldr x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005baee8"></a> `005baee8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005baeec"></a> `005baeec` | `e8 3e 00 f9` | str x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005baef0"></a> `005baef0` | `82 a2 00 91` | add x2,x20,#0x28 | `FALL_THROUGH`
<a id="insn-005baef4"></a> `005baef4` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005baef8"></a> `005baef8` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-005baefc"></a> `005baefc` | `e2 0b 00 f9` | str x2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005baf00"></a> `005baf00` | `6f fe ff 97` | bl 0x005ba8bc | `UNCONDITIONAL_CALL`
<a id="insn-005baf04"></a> `005baf04` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-005baf08"></a> `005baf08` | `48 03 00 b5` | cbnz x8,0x005baf70 | `CONDITIONAL_JUMP`
<a id="insn-005baf0c"></a> `005baf0c` | `e1 e7 ff 90` | adrp x1,0x2b6000 | `FALL_THROUGH`
<a id="insn-005baf10"></a> `005baf10` | `21 94 3e 91` | add x1,x1,#0xfa5 | `FALL_THROUGH`
<a id="insn-005baf14"></a> `005baf14` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-005baf18"></a> `005baf18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005baf1c"></a> `005baf1c` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005baf20"></a> `005baf20` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-005baf24"></a> `005baf24` | `e3 3f 00 91` | add x3,sp,#0xf | `FALL_THROUGH`
<a id="insn-005baf28"></a> `005baf28` | `74 5a 40 91` | add x20,x19,#0x16, LSL #12 | `FALL_THROUGH`
<a id="insn-005baf2c"></a> `005baf2c` | `a5 fe ff 97` | bl 0x005ba9c0 | `UNCONDITIONAL_CALL`
<a id="insn-005baf30"></a> `005baf30` | `e9 87 41 a9` | ldp x9,x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005baf34"></a> `005baf34` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-005baf38"></a> `005baf38` | `29 08 00 f9` | str x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-005baf3c"></a> `005baf3c` | `e1 02 00 f9` | str x1,[x23] | `FALL_THROUGH`
<a id="insn-005baf40"></a> `005baf40` | `69 6a 76 f8` | ldr x9,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005baf44"></a> `005baf44` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005baf48"></a> `005baf48` | `89 00 00 b4` | cbz x9,0x005baf58 | `CONDITIONAL_JUMP`
<a id="insn-005baf4c"></a> `005baf4c` | `69 6a 36 f8` | str x9,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005baf50"></a> `005baf50` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-005baf54"></a> `005baf54` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005baf58"></a> `005baf58` | `80 96 40 f9` | ldr x0,[x20, #0x128] | `FALL_THROUGH`
<a id="insn-005baf5c"></a> `005baf5c` | `42 78 f9 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-005baf60"></a> `005baf60` | `88 9a 40 f9` | ldr x8,[x20, #0x130] | `FALL_THROUGH`
<a id="insn-005baf64"></a> `005baf64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005baf68"></a> `005baf68` | `88 9a 00 f9` | str x8,[x20, #0x130] | `FALL_THROUGH`
<a id="insn-005baf6c"></a> `005baf6c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005baf70"></a> `005baf70` | `00 e1 00 91` | add x0,x8,#0x38 | `FALL_THROUGH`
<a id="insn-005baf74"></a> `005baf74` | `ee 43 fa 97` | bl 0x0044bf2c | `UNCONDITIONAL_CALL`
<a id="insn-005baf78"></a> `005baf78` | `01 00 22 1e` | scvtf s1,w0 | `FALL_THROUGH`
<a id="insn-005baf7c"></a> `005baf7c` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005baf80"></a> `005baf80` | `20 28 28 1e` | fadd s0,s1,s8 | `FALL_THROUGH`
<a id="insn-005baf84"></a> `005baf84` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005baf88"></a> `005baf88` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-005baf8c"></a> `005baf8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005baf90"></a> `005baf90` | `21 01 00 54` | b.ne 0x005bafb4 | `CONDITIONAL_JUMP`
<a id="insn-005baf94"></a> `005baf94` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005baf98"></a> `005baf98` | `e8 23 40 fd` | ldr d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005baf9c"></a> `005baf9c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005bafa0"></a> `005bafa0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005bafa4"></a> `005bafa4` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005bafa8"></a> `005bafa8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005bafac"></a> `005bafac` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-005bafb0"></a> `005bafb0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005bafb4"></a> `005bafb4` | `f7 7f 18 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005baabc`](#insn-005baabc) 範囲 `[['005baabc', '005baaf3']]`
  - `CONDITIONAL_JUMP` [`005baaf0`](#insn-005baaf0) → [`005baf84`](#insn-005baf84)
  - `FALL_THROUGH` [`005baaf0`](#insn-005baaf0) → [`005baaf4`](#insn-005baaf4)
- ブロック [`005baaf4`](#insn-005baaf4) 範囲 `[['005baaf4', '005bab07']]`
  - `FALL_THROUGH` [`005bab04`](#insn-005bab04) → [`005bab08`](#insn-005bab08)
- ブロック [`005bab08`](#insn-005bab08) 範囲 `[['005bab08', '005bab0b']]`
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bab0c`](#insn-005bab0c)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bacb8`](#insn-005bacb8)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bac84`](#insn-005bac84)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bac28`](#insn-005bac28)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bab64`](#insn-005bab64)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005baf84`](#insn-005baf84)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005babfc`](#insn-005babfc)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bacd8`](#insn-005bacd8)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bacf0`](#insn-005bacf0)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bad08`](#insn-005bad08)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bacfc`](#insn-005bacfc)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bac18`](#insn-005bac18)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bac0c`](#insn-005bac0c)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005babb4`](#insn-005babb4)
  - `COMPUTED_JUMP` [`005bab08`](#insn-005bab08) → [`005bab1c`](#insn-005bab1c)
- ブロック [`005bab0c`](#insn-005bab0c) 範囲 `[['005bab0c', '005bab1b']]`
  - `UNCONDITIONAL_JUMP` [`005bab18`](#insn-005bab18) → [`005baf84`](#insn-005baf84)
- ブロック [`005bab1c`](#insn-005bab1c) 範囲 `[['005bab1c', '005bab2b']]`
  - `CONDITIONAL_JUMP` [`005bab28`](#insn-005bab28) → [`005bad14`](#insn-005bad14)
  - `FALL_THROUGH` [`005bab28`](#insn-005bab28) → [`005bab2c`](#insn-005bab2c)
- ブロック [`005bab2c`](#insn-005bab2c) 範囲 `[['005bab2c', '005bab63']]`
  - `UNCONDITIONAL_JUMP` [`005bab60`](#insn-005bab60) → [`005bad18`](#insn-005bad18)
- ブロック [`005bab64`](#insn-005bab64) 範囲 `[['005bab64', '005babb3']]`
  - `UNCONDITIONAL_JUMP` [`005babb0`](#insn-005babb0) → [`005baf80`](#insn-005baf80)
- ブロック [`005babb4`](#insn-005babb4) 範囲 `[['005babb4', '005babc3']]`
  - `CONDITIONAL_JUMP` [`005babc0`](#insn-005babc0) → [`005bae40`](#insn-005bae40)
  - `FALL_THROUGH` [`005babc0`](#insn-005babc0) → [`005babc4`](#insn-005babc4)
- ブロック [`005babc4`](#insn-005babc4) 範囲 `[['005babc4', '005babfb']]`
  - `UNCONDITIONAL_JUMP` [`005babf8`](#insn-005babf8) → [`005bae44`](#insn-005bae44)
- ブロック [`005babfc`](#insn-005babfc) 範囲 `[['005babfc', '005bac0b']]`
  - `UNCONDITIONAL_JUMP` [`005bac08`](#insn-005bac08) → [`005bace4`](#insn-005bace4)
- ブロック [`005bac0c`](#insn-005bac0c) 範囲 `[['005bac0c', '005bac17']]`
  - `FALL_THROUGH` [`005bac14`](#insn-005bac14) → [`005bac18`](#insn-005bac18)
- ブロック [`005bac18`](#insn-005bac18) 範囲 `[['005bac18', '005bac27']]`
  - `UNCONDITIONAL_JUMP` [`005bac24`](#insn-005bac24) → [`005baf84`](#insn-005baf84)
- ブロック [`005bac28`](#insn-005bac28) 範囲 `[['005bac28', '005bac83']]`
  - `UNCONDITIONAL_JUMP` [`005bac80`](#insn-005bac80) → [`005baf80`](#insn-005baf80)
- ブロック [`005bac84`](#insn-005bac84) 範囲 `[['005bac84', '005bac87']]`
  - `FALL_THROUGH` [`005bac84`](#insn-005bac84) → [`005bac88`](#insn-005bac88)
- ブロック [`005bac88`](#insn-005bac88) 範囲 `[['005bac88', '005bacb7']]`
  - `UNCONDITIONAL_JUMP` [`005bacb4`](#insn-005bacb4) → [`005baf80`](#insn-005baf80)
- ブロック [`005bacb8`](#insn-005bacb8) 範囲 `[['005bacb8', '005baccf']]`
  - `FALL_THROUGH` [`005baccc`](#insn-005baccc) → [`005bacd0`](#insn-005bacd0)
- ブロック [`005bacd0`](#insn-005bacd0) 範囲 `[['005bacd0', '005bacd7']]`
  - `UNCONDITIONAL_JUMP` [`005bacd4`](#insn-005bacd4) → [`005baf84`](#insn-005baf84)
- ブロック [`005bacd8`](#insn-005bacd8) 範囲 `[['005bacd8', '005bace3']]`
  - `FALL_THROUGH` [`005bace0`](#insn-005bace0) → [`005bace4`](#insn-005bace4)
- ブロック [`005bace4`](#insn-005bace4) 範囲 `[['005bace4', '005bacef']]`
  - `UNCONDITIONAL_JUMP` [`005bacec`](#insn-005bacec) → [`005baf80`](#insn-005baf80)
- ブロック [`005bacf0`](#insn-005bacf0) 範囲 `[['005bacf0', '005bacfb']]`
  - `UNCONDITIONAL_JUMP` [`005bacf8`](#insn-005bacf8) → [`005baf84`](#insn-005baf84)
- ブロック [`005bacfc`](#insn-005bacfc) 範囲 `[['005bacfc', '005bad07']]`
  - `UNCONDITIONAL_JUMP` [`005bad04`](#insn-005bad04) → [`005baf84`](#insn-005baf84)
- ブロック [`005bad08`](#insn-005bad08) 範囲 `[['005bad08', '005bad13']]`
  - `UNCONDITIONAL_JUMP` [`005bad10`](#insn-005bad10) → [`005baf84`](#insn-005baf84)
- ブロック [`005bad14`](#insn-005bad14) 範囲 `[['005bad14', '005bad17']]`
  - `FALL_THROUGH` [`005bad14`](#insn-005bad14) → [`005bad18`](#insn-005bad18)
- ブロック [`005bad18`](#insn-005bad18) 範囲 `[['005bad18', '005bad2b']]`
  - `CONDITIONAL_JUMP` [`005bad28`](#insn-005bad28) → [`005bad40`](#insn-005bad40)
  - `FALL_THROUGH` [`005bad28`](#insn-005bad28) → [`005bad2c`](#insn-005bad2c)
- ブロック [`005bad2c`](#insn-005bad2c) 範囲 `[['005bad2c', '005bad33']]`
  - `UNCONDITIONAL_JUMP` [`005bad30`](#insn-005bad30) → [`005bad60`](#insn-005bad60)
- ブロック [`005bad34`](#insn-005bad34) 範囲 `[['005bad34', '005bad3f']]`
  - `CONDITIONAL_JUMP` [`005bad3c`](#insn-005bad3c) → [`005bad60`](#insn-005bad60)
  - `FALL_THROUGH` [`005bad3c`](#insn-005bad3c) → [`005bad40`](#insn-005bad40)
- ブロック [`005bad40`](#insn-005bad40) 範囲 `[['005bad40', '005bad43']]`
  - `FALL_THROUGH` [`005bad40`](#insn-005bad40) → [`005bad44`](#insn-005bad44)
- ブロック [`005bad44`](#insn-005bad44) 範囲 `[['005bad44', '005bad4f']]`
  - `CONDITIONAL_JUMP` [`005bad4c`](#insn-005bad4c) → [`005bad34`](#insn-005bad34)
  - `FALL_THROUGH` [`005bad4c`](#insn-005bad4c) → [`005bad50`](#insn-005bad50)
- ブロック [`005bad50`](#insn-005bad50) 範囲 `[['005bad50', '005bad53']]`
  - `CONDITIONAL_JUMP` [`005bad50`](#insn-005bad50) → [`005badc4`](#insn-005badc4)
  - `FALL_THROUGH` [`005bad50`](#insn-005bad50) → [`005bad54`](#insn-005bad54)
- ブロック [`005bad54`](#insn-005bad54) 範囲 `[['005bad54', '005bad5b']]`
  - `CONDITIONAL_JUMP` [`005bad58`](#insn-005bad58) → [`005bad40`](#insn-005bad40)
  - `FALL_THROUGH` [`005bad58`](#insn-005bad58) → [`005bad5c`](#insn-005bad5c)
- ブロック [`005bad5c`](#insn-005bad5c) 範囲 `[['005bad5c', '005bad5f']]`
  - `FALL_THROUGH` [`005bad5c`](#insn-005bad5c) → [`005bad60`](#insn-005bad60)
- ブロック [`005bad60`](#insn-005bad60) 範囲 `[['005bad60', '005bad7f']]`
  - `FALL_THROUGH` [`005bad7c`](#insn-005bad7c) → [`005bad80`](#insn-005bad80)
- ブロック [`005bad80`](#insn-005bad80) 範囲 `[['005bad80', '005bad97']]`
  - `FALL_THROUGH` [`005bad94`](#insn-005bad94) → [`005bad98`](#insn-005bad98)
- ブロック [`005bad98`](#insn-005bad98) 範囲 `[['005bad98', '005bada3']]`
  - `CONDITIONAL_JUMP` [`005bada0`](#insn-005bada0) → [`005badac`](#insn-005badac)
  - `FALL_THROUGH` [`005bada0`](#insn-005bada0) → [`005bada4`](#insn-005bada4)
- ブロック [`005bada4`](#insn-005bada4) 範囲 `[['005bada4', '005badab']]`
  - `FALL_THROUGH` [`005bada8`](#insn-005bada8) → [`005badac`](#insn-005badac)
- ブロック [`005badac`](#insn-005badac) 範囲 `[['005badac', '005badaf']]`
  - `FALL_THROUGH` [`005badac`](#insn-005badac) → [`005badb0`](#insn-005badb0)
- ブロック [`005badb0`](#insn-005badb0) 範囲 `[['005badb0', '005badc3']]`
  - `FALL_THROUGH` [`005badc0`](#insn-005badc0) → [`005badc4`](#insn-005badc4)
- ブロック [`005badc4`](#insn-005badc4) 範囲 `[['005badc4', '005baddf']]`
  - `CONDITIONAL_JUMP` [`005baddc`](#insn-005baddc) → [`005baf70`](#insn-005baf70)
  - `FALL_THROUGH` [`005baddc`](#insn-005baddc) → [`005bade0`](#insn-005bade0)
- ブロック [`005bade0`](#insn-005bade0) 範囲 `[['005bade0', '005bae07']]`
  - `FALL_THROUGH` [`005bae04`](#insn-005bae04) → [`005bae08`](#insn-005bae08)
- ブロック [`005bae08`](#insn-005bae08) 範囲 `[['005bae08', '005bae1f']]`
  - `CONDITIONAL_JUMP` [`005bae1c`](#insn-005bae1c) → [`005bae28`](#insn-005bae28)
  - `FALL_THROUGH` [`005bae1c`](#insn-005bae1c) → [`005bae20`](#insn-005bae20)
- ブロック [`005bae20`](#insn-005bae20) 範囲 `[['005bae20', '005bae27']]`
  - `FALL_THROUGH` [`005bae24`](#insn-005bae24) → [`005bae28`](#insn-005bae28)
- ブロック [`005bae28`](#insn-005bae28) 範囲 `[['005bae28', '005bae33']]`
  - `FALL_THROUGH` [`005bae30`](#insn-005bae30) → [`005bae34`](#insn-005bae34)
- ブロック [`005bae34`](#insn-005bae34) 範囲 `[['005bae34', '005bae3f']]`
  - `UNCONDITIONAL_JUMP` [`005bae3c`](#insn-005bae3c) → [`005baf6c`](#insn-005baf6c)
- ブロック [`005bae40`](#insn-005bae40) 範囲 `[['005bae40', '005bae43']]`
  - `FALL_THROUGH` [`005bae40`](#insn-005bae40) → [`005bae44`](#insn-005bae44)
- ブロック [`005bae44`](#insn-005bae44) 範囲 `[['005bae44', '005bae57']]`
  - `CONDITIONAL_JUMP` [`005bae54`](#insn-005bae54) → [`005bae6c`](#insn-005bae6c)
  - `FALL_THROUGH` [`005bae54`](#insn-005bae54) → [`005bae58`](#insn-005bae58)
- ブロック [`005bae58`](#insn-005bae58) 範囲 `[['005bae58', '005bae5f']]`
  - `UNCONDITIONAL_JUMP` [`005bae5c`](#insn-005bae5c) → [`005bae8c`](#insn-005bae8c)
- ブロック [`005bae60`](#insn-005bae60) 範囲 `[['005bae60', '005bae6b']]`
  - `CONDITIONAL_JUMP` [`005bae68`](#insn-005bae68) → [`005bae8c`](#insn-005bae8c)
  - `FALL_THROUGH` [`005bae68`](#insn-005bae68) → [`005bae6c`](#insn-005bae6c)
- ブロック [`005bae6c`](#insn-005bae6c) 範囲 `[['005bae6c', '005bae7b']]`
  - `CONDITIONAL_JUMP` [`005bae78`](#insn-005bae78) → [`005bae60`](#insn-005bae60)
  - `FALL_THROUGH` [`005bae78`](#insn-005bae78) → [`005bae7c`](#insn-005bae7c)
- ブロック [`005bae7c`](#insn-005bae7c) 範囲 `[['005bae7c', '005bae7f']]`
  - `CONDITIONAL_JUMP` [`005bae7c`](#insn-005bae7c) → [`005baef0`](#insn-005baef0)
  - `FALL_THROUGH` [`005bae7c`](#insn-005bae7c) → [`005bae80`](#insn-005bae80)
- ブロック [`005bae80`](#insn-005bae80) 範囲 `[['005bae80', '005bae87']]`
  - `CONDITIONAL_JUMP` [`005bae84`](#insn-005bae84) → [`005bae6c`](#insn-005bae6c)
  - `FALL_THROUGH` [`005bae84`](#insn-005bae84) → [`005bae88`](#insn-005bae88)
- ブロック [`005bae88`](#insn-005bae88) 範囲 `[['005bae88', '005bae8b']]`
  - `FALL_THROUGH` [`005bae88`](#insn-005bae88) → [`005bae8c`](#insn-005bae8c)
- ブロック [`005bae8c`](#insn-005bae8c) 範囲 `[['005bae8c', '005baeb7']]`
  - `FALL_THROUGH` [`005baeb4`](#insn-005baeb4) → [`005baeb8`](#insn-005baeb8)
- ブロック [`005baeb8`](#insn-005baeb8) 範囲 `[['005baeb8', '005baec3']]`
  - `FALL_THROUGH` [`005baec0`](#insn-005baec0) → [`005baec4`](#insn-005baec4)
- ブロック [`005baec4`](#insn-005baec4) 範囲 `[['005baec4', '005baecf']]`
  - `CONDITIONAL_JUMP` [`005baecc`](#insn-005baecc) → [`005baed8`](#insn-005baed8)
  - `FALL_THROUGH` [`005baecc`](#insn-005baecc) → [`005baed0`](#insn-005baed0)
- ブロック [`005baed0`](#insn-005baed0) 範囲 `[['005baed0', '005baed7']]`
  - `FALL_THROUGH` [`005baed4`](#insn-005baed4) → [`005baed8`](#insn-005baed8)
- ブロック [`005baed8`](#insn-005baed8) 範囲 `[['005baed8', '005baeef']]`
  - `FALL_THROUGH` [`005baeec`](#insn-005baeec) → [`005baef0`](#insn-005baef0)
- ブロック [`005baef0`](#insn-005baef0) 範囲 `[['005baef0', '005baf03']]`
  - `FALL_THROUGH` [`005baf00`](#insn-005baf00) → [`005baf04`](#insn-005baf04)
- ブロック [`005baf04`](#insn-005baf04) 範囲 `[['005baf04', '005baf0b']]`
  - `CONDITIONAL_JUMP` [`005baf08`](#insn-005baf08) → [`005baf70`](#insn-005baf70)
  - `FALL_THROUGH` [`005baf08`](#insn-005baf08) → [`005baf0c`](#insn-005baf0c)
- ブロック [`005baf0c`](#insn-005baf0c) 範囲 `[['005baf0c', '005baf17']]`
  - `FALL_THROUGH` [`005baf14`](#insn-005baf14) → [`005baf18`](#insn-005baf18)
- ブロック [`005baf18`](#insn-005baf18) 範囲 `[['005baf18', '005baf4b']]`
  - `CONDITIONAL_JUMP` [`005baf48`](#insn-005baf48) → [`005baf58`](#insn-005baf58)
  - `FALL_THROUGH` [`005baf48`](#insn-005baf48) → [`005baf4c`](#insn-005baf4c)
- ブロック [`005baf4c`](#insn-005baf4c) 範囲 `[['005baf4c', '005baf4f']]`
  - `FALL_THROUGH` [`005baf4c`](#insn-005baf4c) → [`005baf50`](#insn-005baf50)
- ブロック [`005baf50`](#insn-005baf50) 範囲 `[['005baf50', '005baf53']]`
  - `FALL_THROUGH` [`005baf50`](#insn-005baf50) → [`005baf54`](#insn-005baf54)
- ブロック [`005baf54`](#insn-005baf54) 範囲 `[['005baf54', '005baf57']]`
  - `FALL_THROUGH` [`005baf54`](#insn-005baf54) → [`005baf58`](#insn-005baf58)
- ブロック [`005baf58`](#insn-005baf58) 範囲 `[['005baf58', '005baf5b']]`
  - `FALL_THROUGH` [`005baf58`](#insn-005baf58) → [`005baf5c`](#insn-005baf5c)
- ブロック [`005baf5c`](#insn-005baf5c) 範囲 `[['005baf5c', '005baf5f']]`
  - `FALL_THROUGH` [`005baf5c`](#insn-005baf5c) → [`005baf60`](#insn-005baf60)
- ブロック [`005baf60`](#insn-005baf60) 範囲 `[['005baf60', '005baf63']]`
  - `FALL_THROUGH` [`005baf60`](#insn-005baf60) → [`005baf64`](#insn-005baf64)
- ブロック [`005baf64`](#insn-005baf64) 範囲 `[['005baf64', '005baf67']]`
  - `FALL_THROUGH` [`005baf64`](#insn-005baf64) → [`005baf68`](#insn-005baf68)
- ブロック [`005baf68`](#insn-005baf68) 範囲 `[['005baf68', '005baf6b']]`
  - `FALL_THROUGH` [`005baf68`](#insn-005baf68) → [`005baf6c`](#insn-005baf6c)
- ブロック [`005baf6c`](#insn-005baf6c) 範囲 `[['005baf6c', '005baf6f']]`
  - `FALL_THROUGH` [`005baf6c`](#insn-005baf6c) → [`005baf70`](#insn-005baf70)
- ブロック [`005baf70`](#insn-005baf70) 範囲 `[['005baf70', '005baf73']]`
  - `FALL_THROUGH` [`005baf70`](#insn-005baf70) → [`005baf74`](#insn-005baf74)
- ブロック [`005baf74`](#insn-005baf74) 範囲 `[['005baf74', '005baf77']]`
  - `FALL_THROUGH` [`005baf74`](#insn-005baf74) → [`005baf78`](#insn-005baf78)
- ブロック [`005baf78`](#insn-005baf78) 範囲 `[['005baf78', '005baf7b']]`
  - `FALL_THROUGH` [`005baf78`](#insn-005baf78) → [`005baf7c`](#insn-005baf7c)
- ブロック [`005baf7c`](#insn-005baf7c) 範囲 `[['005baf7c', '005baf7f']]`
  - `FALL_THROUGH` [`005baf7c`](#insn-005baf7c) → [`005baf80`](#insn-005baf80)
- ブロック [`005baf80`](#insn-005baf80) 範囲 `[['005baf80', '005baf83']]`
  - `FALL_THROUGH` [`005baf80`](#insn-005baf80) → [`005baf84`](#insn-005baf84)
- ブロック [`005baf84`](#insn-005baf84) 範囲 `[['005baf84', '005baf8b']]`
  - `FALL_THROUGH` [`005baf88`](#insn-005baf88) → [`005baf8c`](#insn-005baf8c)
- ブロック [`005baf8c`](#insn-005baf8c) 範囲 `[['005baf8c', '005baf93']]`
  - `CONDITIONAL_JUMP` [`005baf90`](#insn-005baf90) → [`005bafb4`](#insn-005bafb4)
  - `FALL_THROUGH` [`005baf90`](#insn-005baf90) → [`005baf94`](#insn-005baf94)
- ブロック [`005baf94`](#insn-005baf94) 範囲 `[['005baf94', '005baf9b']]`
  - `FALL_THROUGH` [`005baf98`](#insn-005baf98) → [`005baf9c`](#insn-005baf9c)
- ブロック [`005baf9c`](#insn-005baf9c) 範囲 `[['005baf9c', '005bafa3']]`
  - `FALL_THROUGH` [`005bafa0`](#insn-005bafa0) → [`005bafa4`](#insn-005bafa4)
- ブロック [`005bafa4`](#insn-005bafa4) 範囲 `[['005bafa4', '005bafa7']]`
  - `FALL_THROUGH` [`005bafa4`](#insn-005bafa4) → [`005bafa8`](#insn-005bafa8)
- ブロック [`005bafa8`](#insn-005bafa8) 範囲 `[['005bafa8', '005bafb3']]`
- ブロック [`005bafb4`](#insn-005bafb4) 範囲 `[['005bafb4', '005bafb7']]`

## 命令位置別の参照

- [`005baac0`](#insn-005baac0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baac4`](#insn-005baac4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baac8`](#insn-005baac8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baacc`](#insn-005baacc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baad0`](#insn-005baad0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baad4`](#insn-005baad4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baaec`](#insn-005baaec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baaf0`](#insn-005baaf0) → [`005baf84`](#insn-005baf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bab00`](#insn-005bab00) → `002c6ba8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::switchdataD_002c6ba8` · 推定型 `ushort`
- [`005bab08`](#insn-005bab08) → [`005bab0c`](#insn-005bab0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_1` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bacb8`](#insn-005bacb8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_2` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bac84`](#insn-005bac84) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_3` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bac28`](#insn-005bac28) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_4` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bab64`](#insn-005bab64) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_5` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005baf84`](#insn-005baf84) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005babfc`](#insn-005babfc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_7` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bacd8`](#insn-005bacd8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_9` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bacf0`](#insn-005bacf0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_b` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bad08`](#insn-005bad08) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_c` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bacfc`](#insn-005bacfc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_d` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bac18`](#insn-005bac18) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_e` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bac0c`](#insn-005bac0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_f` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005babb4`](#insn-005babb4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_10` · 推定型 `None`
- [`005bab08`](#insn-005bab08) → [`005bab1c`](#insn-005bab1c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_11` · 推定型 `None`
- [`005bab18`](#insn-005bab18) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bab24`](#insn-005bab24) → `00c249b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005bab28`](#insn-005bab28) → [`005bad14`](#insn-005bad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bab38`](#insn-005bab38) → `00bf4450`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005bab48`](#insn-005bab48) → `00be8d98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005bab50`](#insn-005bab50) → [`00bdb6c0`](../00bdb/00bdb6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6c0` · 推定シンボル `None` · 推定型 `None`
- [`005bab60`](#insn-005bab60) → [`005bad18`](#insn-005bad18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bab68`](#insn-005bab68) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bab74`](#insn-005bab74) → `0032f9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`005bab78`](#insn-005bab78) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bab7c`](#insn-005bab7c) → [`00449bac`](../00449/00449bac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bac` · 推定シンボル `None` · 推定型 `None`
- [`005bab8c`](#insn-005bab8c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005babb0`](#insn-005babb0) → [`005baf80`](#insn-005baf80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005babbc`](#insn-005babbc) → `00c249b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005babc0`](#insn-005babc0) → [`005bae40`](#insn-005bae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005babd0`](#insn-005babd0) → `00bf4450`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005babe0`](#insn-005babe0) → `00be8d98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005babe8`](#insn-005babe8) → [`00bdb6c0`](../00bdb/00bdb6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6c0` · 推定シンボル `None` · 推定型 `None`
- [`005babf8`](#insn-005babf8) → [`005bae44`](#insn-005bae44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bac00`](#insn-005bac00) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bac04`](#insn-005bac04) → [`00449aec`](../00449/00449aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449aec` · 推定シンボル `None` · 推定型 `None`
- [`005bac08`](#insn-005bac08) → [`005bace4`](#insn-005bace4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bac24`](#insn-005bac24) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bac30`](#insn-005bac30) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bac44`](#insn-005bac44) → `0032f9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`005bac58`](#insn-005bac58) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bac80`](#insn-005bac80) → [`005baf80`](#insn-005baf80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bac8c`](#insn-005bac8c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bacb4`](#insn-005bacb4) → [`005baf80`](#insn-005baf80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bacd4`](#insn-005bacd4) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bacdc`](#insn-005bacdc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`005bace0`](#insn-005bace0) → [`00449bac`](../00449/00449bac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bac` · 推定シンボル `None` · 推定型 `None`
- [`005bacec`](#insn-005bacec) → [`005baf80`](#insn-005baf80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bacf8`](#insn-005bacf8) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bad04`](#insn-005bad04) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bad10`](#insn-005bad10) → [`005baf84`](#insn-005baf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005bab08::caseD_6` · 推定型 `None`
- [`005bad28`](#insn-005bad28) → [`005bad40`](#insn-005bad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad30`](#insn-005bad30) → [`005bad60`](#insn-005bad60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad3c`](#insn-005bad3c) → [`005bad60`](#insn-005bad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad4c`](#insn-005bad4c) → [`005bad34`](#insn-005bad34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad50`](#insn-005bad50) → [`005badc4`](#insn-005badc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad58`](#insn-005bad58) → [`005bad40`](#insn-005bad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bad70`](#insn-005bad70) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`005bada0`](#insn-005bada0) → [`005badac`](#insn-005badac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005badb4`](#insn-005badb4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`005badd0`](#insn-005badd0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005badd4`](#insn-005badd4) → [`005ba8bc`](005ba8bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ba8bc` · 推定シンボル `None` · 推定型 `None`
- [`005baddc`](#insn-005baddc) → [`005baf70`](#insn-005baf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bade8`](#insn-005bade8) → `002b6fa5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae00`](#insn-005bae00) → [`005ba9c0`](005ba9c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ba9c0` · 推定シンボル `None` · 推定型 `None`
- [`005bae04`](#insn-005bae04) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae1c`](#insn-005bae1c) → [`005bae28`](#insn-005bae28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae2c`](#insn-005bae2c) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`005bae3c`](#insn-005bae3c) → [`005baf6c`](#insn-005baf6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae54`](#insn-005bae54) → [`005bae6c`](#insn-005bae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae5c`](#insn-005bae5c) → [`005bae8c`](#insn-005bae8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae68`](#insn-005bae68) → [`005bae8c`](#insn-005bae8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae78`](#insn-005bae78) → [`005bae60`](#insn-005bae60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae7c`](#insn-005bae7c) → [`005baef0`](#insn-005baef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae84`](#insn-005bae84) → [`005bae6c`](#insn-005bae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bae9c`](#insn-005bae9c) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`005baecc`](#insn-005baecc) → [`005baed8`](#insn-005baed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baee0`](#insn-005baee0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`005baefc`](#insn-005baefc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf00`](#insn-005baf00) → [`005ba8bc`](005ba8bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ba8bc` · 推定シンボル `None` · 推定型 `None`
- [`005baf08`](#insn-005baf08) → [`005baf70`](#insn-005baf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf10`](#insn-005baf10) → `002b6fa5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf2c`](#insn-005baf2c) → [`005ba9c0`](005ba9c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ba9c0` · 推定シンボル `None` · 推定型 `None`
- [`005baf30`](#insn-005baf30) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf48`](#insn-005baf48) → [`005baf58`](#insn-005baf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf5c`](#insn-005baf5c) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`005baf6c`](#insn-005baf6c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf74`](#insn-005baf74) → [`0044bf2c`](../0044b/0044bf2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044bf2c` · 推定シンボル `None` · 推定型 `None`
- [`005baf88`](#insn-005baf88) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf90`](#insn-005baf90) → [`005bafb4`](#insn-005bafb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf94`](#insn-005baf94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf98`](#insn-005baf98) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baf9c`](#insn-005baf9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafa0`](#insn-005bafa0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafa4`](#insn-005bafa4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafa8`](#insn-005bafa8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bafb4`](#insn-005bafb4) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005baac0`](#insn-005baac0)

~~~json
{
  "source": "005baac0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baac4`](#insn-005baac4)

~~~json
{
  "source": "005baac4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baac8`](#insn-005baac8)

~~~json
{
  "source": "005baac8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baacc`](#insn-005baacc)

~~~json
{
  "source": "005baacc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baad0`](#insn-005baad0)

~~~json
{
  "source": "005baad0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baad4`](#insn-005baad4)

~~~json
{
  "source": "005baad4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baaec`](#insn-005baaec)

~~~json
{
  "source": "005baaec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baaf0`](#insn-005baaf0)

~~~json
{
  "source": "005baaf0",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab00`](#insn-005bab00)

~~~json
{
  "source": "005bab00",
  "target": "002c6ba8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c6ba8",
  "offset": 0,
  "size": 2,
  "datatype": "ushort",
  "bytes": "0000",
  "capture_start": "002c6ba8",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bab0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bacb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bac28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bab64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005babfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bacd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bac0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005babb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab08`](#insn-005bab08)

~~~json
{
  "source": "005bab08",
  "target": "005bab1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab18`](#insn-005bab18)

~~~json
{
  "source": "005bab18",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab24`](#insn-005bab24)

~~~json
{
  "source": "005bab24",
  "target": "00c249b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005bab28`](#insn-005bab28)

~~~json
{
  "source": "005bab28",
  "target": "005bad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab38`](#insn-005bab38)

~~~json
{
  "source": "005bab38",
  "target": "00bf4450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf4450",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005bab48`](#insn-005bab48)

~~~json
{
  "source": "005bab48",
  "target": "00be8d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8d98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005bab50`](#insn-005bab50)

~~~json
{
  "source": "005bab50",
  "target": "00bdb6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bab60`](#insn-005bab60)

~~~json
{
  "source": "005bab60",
  "target": "005bad18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bab68`](#insn-005bab68)

~~~json
{
  "source": "005bab68",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bab74`](#insn-005bab74)

~~~json
{
  "source": "005bab74",
  "target": "0032f9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bab78`](#insn-005bab78)

~~~json
{
  "source": "005bab78",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bab7c`](#insn-005bab7c)

~~~json
{
  "source": "005bab7c",
  "target": "00449bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bab8c`](#insn-005bab8c)

~~~json
{
  "source": "005bab8c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005babb0`](#insn-005babb0)

~~~json
{
  "source": "005babb0",
  "target": "005baf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005babbc`](#insn-005babbc)

~~~json
{
  "source": "005babbc",
  "target": "00c249b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005babc0`](#insn-005babc0)

~~~json
{
  "source": "005babc0",
  "target": "005bae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005babd0`](#insn-005babd0)

~~~json
{
  "source": "005babd0",
  "target": "00bf4450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf4450",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005babe0`](#insn-005babe0)

~~~json
{
  "source": "005babe0",
  "target": "00be8d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8d98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005babe8`](#insn-005babe8)

~~~json
{
  "source": "005babe8",
  "target": "00bdb6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005babf8`](#insn-005babf8)

~~~json
{
  "source": "005babf8",
  "target": "005bae44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bac00`](#insn-005bac00)

~~~json
{
  "source": "005bac00",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bac04`](#insn-005bac04)

~~~json
{
  "source": "005bac04",
  "target": "00449aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bac08`](#insn-005bac08)

~~~json
{
  "source": "005bac08",
  "target": "005bace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bac24`](#insn-005bac24)

~~~json
{
  "source": "005bac24",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bac30`](#insn-005bac30)

~~~json
{
  "source": "005bac30",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bac44`](#insn-005bac44)

~~~json
{
  "source": "005bac44",
  "target": "0032f9a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032f999",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e10440c1d109e029d04540c1f10440e00dedd000000",
  "capture_start": "0032f999",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005bac58`](#insn-005bac58)

~~~json
{
  "source": "005bac58",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bac80`](#insn-005bac80)

~~~json
{
  "source": "005bac80",
  "target": "005baf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bac8c`](#insn-005bac8c)

~~~json
{
  "source": "005bac8c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bacb4`](#insn-005bacb4)

~~~json
{
  "source": "005bacb4",
  "target": "005baf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bacd4`](#insn-005bacd4)

~~~json
{
  "source": "005bacd4",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bacdc`](#insn-005bacdc)

~~~json
{
  "source": "005bacdc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bace0`](#insn-005bace0)

~~~json
{
  "source": "005bace0",
  "target": "00449bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bacec`](#insn-005bacec)

~~~json
{
  "source": "005bacec",
  "target": "005baf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bacf8`](#insn-005bacf8)

~~~json
{
  "source": "005bacf8",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad04`](#insn-005bad04)

~~~json
{
  "source": "005bad04",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad10`](#insn-005bad10)

~~~json
{
  "source": "005bad10",
  "target": "005baf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad28`](#insn-005bad28)

~~~json
{
  "source": "005bad28",
  "target": "005bad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad30`](#insn-005bad30)

~~~json
{
  "source": "005bad30",
  "target": "005bad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad3c`](#insn-005bad3c)

~~~json
{
  "source": "005bad3c",
  "target": "005bad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad4c`](#insn-005bad4c)

~~~json
{
  "source": "005bad4c",
  "target": "005bad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad50`](#insn-005bad50)

~~~json
{
  "source": "005bad50",
  "target": "005badc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad58`](#insn-005bad58)

~~~json
{
  "source": "005bad58",
  "target": "005bad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bad70`](#insn-005bad70)

~~~json
{
  "source": "005bad70",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bada0`](#insn-005bada0)

~~~json
{
  "source": "005bada0",
  "target": "005badac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005badb4`](#insn-005badb4)

~~~json
{
  "source": "005badb4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005badd0`](#insn-005badd0)

~~~json
{
  "source": "005badd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005badd4`](#insn-005badd4)

~~~json
{
  "source": "005badd4",
  "target": "005ba8bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baddc`](#insn-005baddc)

~~~json
{
  "source": "005baddc",
  "target": "005baf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bade8`](#insn-005bade8)

~~~json
{
  "source": "005bade8",
  "target": "002b6fa5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae00`](#insn-005bae00)

~~~json
{
  "source": "005bae00",
  "target": "005ba9c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bae04`](#insn-005bae04)

~~~json
{
  "source": "005bae04",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae1c`](#insn-005bae1c)

~~~json
{
  "source": "005bae1c",
  "target": "005bae28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae2c`](#insn-005bae2c)

~~~json
{
  "source": "005bae2c",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bae3c`](#insn-005bae3c)

~~~json
{
  "source": "005bae3c",
  "target": "005baf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae54`](#insn-005bae54)

~~~json
{
  "source": "005bae54",
  "target": "005bae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae5c`](#insn-005bae5c)

~~~json
{
  "source": "005bae5c",
  "target": "005bae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae68`](#insn-005bae68)

~~~json
{
  "source": "005bae68",
  "target": "005bae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae78`](#insn-005bae78)

~~~json
{
  "source": "005bae78",
  "target": "005bae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae7c`](#insn-005bae7c)

~~~json
{
  "source": "005bae7c",
  "target": "005baef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae84`](#insn-005bae84)

~~~json
{
  "source": "005bae84",
  "target": "005bae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bae9c`](#insn-005bae9c)

~~~json
{
  "source": "005bae9c",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baecc`](#insn-005baecc)

~~~json
{
  "source": "005baecc",
  "target": "005baed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baee0`](#insn-005baee0)

~~~json
{
  "source": "005baee0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baefc`](#insn-005baefc)

~~~json
{
  "source": "005baefc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf00`](#insn-005baf00)

~~~json
{
  "source": "005baf00",
  "target": "005ba8bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf08`](#insn-005baf08)

~~~json
{
  "source": "005baf08",
  "target": "005baf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf10`](#insn-005baf10)

~~~json
{
  "source": "005baf10",
  "target": "002b6fa5",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf2c`](#insn-005baf2c)

~~~json
{
  "source": "005baf2c",
  "target": "005ba9c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf30`](#insn-005baf30)

~~~json
{
  "source": "005baf30",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf48`](#insn-005baf48)

~~~json
{
  "source": "005baf48",
  "target": "005baf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf5c`](#insn-005baf5c)

~~~json
{
  "source": "005baf5c",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf6c`](#insn-005baf6c)

~~~json
{
  "source": "005baf6c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf74`](#insn-005baf74)

~~~json
{
  "source": "005baf74",
  "target": "0044bf2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005baf88`](#insn-005baf88)

~~~json
{
  "source": "005baf88",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf90`](#insn-005baf90)

~~~json
{
  "source": "005baf90",
  "target": "005bafb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf94`](#insn-005baf94)

~~~json
{
  "source": "005baf94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf98`](#insn-005baf98)

~~~json
{
  "source": "005baf98",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baf9c`](#insn-005baf9c)

~~~json
{
  "source": "005baf9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafa0`](#insn-005bafa0)

~~~json
{
  "source": "005bafa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafa4`](#insn-005bafa4)

~~~json
{
  "source": "005bafa4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafa8`](#insn-005bafa8)

~~~json
{
  "source": "005bafa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bafb4`](#insn-005bafb4)

~~~json
{
  "source": "005bafb4",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
