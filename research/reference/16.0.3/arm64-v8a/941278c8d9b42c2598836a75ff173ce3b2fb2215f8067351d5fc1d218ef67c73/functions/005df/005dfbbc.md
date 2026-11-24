# 005dfbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `005df80c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005df/005df80c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0025.md#compare-1d7735079e364173250134ce8578e67c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dfbbc",
  "name": "FUN_005dfbbc",
  "size": 1276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d317fb04276940003416c668cf19ea244d4d01814ca827f87bc7fcc1f907609",
  "source_text_sha256": "1d317fb04276940003416c668cf19ea244d4d01814ca827f87bc7fcc1f907609",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005dfbbc",
        "005e00b7"
      ]
    ],
    "bytes_sha256": "2e76e67be3eae883bff03d53b0b30879427cda70745b81d2960fd994e8b9129d",
    "instruction_count": 319,
    "instruction_bytes": 1276,
    "body_bytes": 1276,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005dde90](../005dd/005dde90.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [0046f164](../0046f/0046f164.md)
- [005df9bc](../005df/005df9bc.md)
- [005dfac0](../005df/005dfac0.md)
- [008524fc](../00852/008524fc.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596b0](../00c59/00c596b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7970 bytes

~~~c

void FUN_005dfbbc(ulong param_1,int *param_2,int param_3,undefined4 param_4)

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
  
                    /* try { // try from 005dfbcc to 006dfbd7 has its CatchHandler @ 005e0124 */
                    /* try { // try from 005dfbd8 to 006dfc0b has its CatchHandler @ 005dfa3c */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  fVar11 = (float)param_1;
  switch(param_4) {
  case 1:
                    /* try { // try from 005dfc0c to 006dfc13 has its CatchHandler @ 005e011c */
                    /* try { // try from 005dfc14 to 006dfc23 has its CatchHandler @ 005e0118 */
    param_1 = (ulong)(uint)(fVar11 * 960.0);
    break;
  case 2:
                    /* try { // try from 005dfdd0 to 006dfddb has its CatchHandler @ 005e010c */
    param_1 = (ulong)(uint)(fVar11 + (float)*param_2 / -10.0);
    break;
  case 3:
    lVar5 = FUN_008524fc();
    fVar12 = (float)(*param_2 + *(int *)(lVar5 + 0x9f690)) / 10.0;
    goto LAB_005e0080;
  case 4:
    lVar5 = FUN_008524fc();
    iVar4 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    lVar5 = FUN_008524fc();
                    /* try { // try from 005dfd60 to 006dfd73 has its CatchHandler @ 005e0114 */
    iVar1 = 0;
    if (*(int *)(lVar5 + 0x846b4) != 0) {
      iVar1 = ((iVar4 >> 1) * 100 + 50000) / *(int *)(lVar5 + 0x846b4);
    }
    fVar12 = (float)((param_2[1] - iVar1) + 0x1e0);
    goto LAB_005e0080;
  case 5:
    lVar5 = FUN_008524fc();
    iVar4 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_008524fc();
    iVar3 = FUN_0046cde4();
                    /* try { // try from 005dfc84 to 006dfc8f has its CatchHandler @ 005e0110 */
    lVar5 = FUN_008524fc();
    iVar1 = 0;
    if (*(int *)(lVar5 + 0x846b4) != 0) {
      iVar1 = (iVar3 * 100 + -52000) / *(int *)(lVar5 + 0x846b4);
    }
    fVar12 = (float)((iVar1 - iVar4) + 0x208);
    goto LAB_005e0080;
  case 7:
    FUN_008524fc();
    iVar4 = FUN_0046cd24();
    goto LAB_005dfde4;
  case 9:
    FUN_008524fc();
    iVar4 = FUN_0046cde4();
LAB_005dfde4:
    fVar12 = (float)iVar4;
    goto LAB_005e0080;
  case 0xb:
    param_1 = (ulong)(uint)(fVar11 + 1.0);
    break;
  case 0xc:
    param_1 = (ulong)(uint)(fVar11 + 2.0);
    break;
  case 0xd:
    param_1 = (ulong)(uint)(fVar11 / 30.0);
    break;
  case 0xf:
                    /* try { // try from 005dfd14 to 006dfd57 has its CatchHandler @ 005e0128 */
    param_1 = (ulong)(uint)(fVar11 * 255.0);
  case 0xe:
    param_1 = (ulong)(uint)((float)param_1 / 100.0);
    break;
  case 0x10:
    if (DAT_00ca5a38 == 0) {
      lVar5 = 0;
    }
    else {
      lVar5 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c72a18,0);
    }
    piVar9 = *(int **)(param_2 + 0x1c);
    piVar7 = param_2 + 0x1c;
    while (piVar10 = piVar7, piVar9 != (int *)0x0) {
      while (local_90 = piVar9, piVar7 = local_90, local_90[8] <= param_3) {
        if (param_3 <= local_90[8]) goto LAB_005dfff0;
        piVar9 = *(int **)(local_90 + 2);
        if (*(int **)(local_90 + 2) == (int *)0x0) {
          piVar10 = local_90 + 2;
          goto LAB_005dff8c;
        }
      }
      piVar9 = *(int **)local_90;
                    /* try { // try from 005dff68 to 006e009f has its CatchHandler @ 005e012c */
    }
LAB_005dff8c:
    local_90 = (int *)_Znwm(0x40);
    local_90[8] = param_3;
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
    piVar7 = local_90;
    if (**(long **)(param_2 + 0x1a) != 0) {
      *(long *)(param_2 + 0x1a) = **(long **)(param_2 + 0x1a);
      piVar7 = *(int **)piVar10;
    }
    FUN_0043bf04(*(undefined8 *)(param_2 + 0x1c),piVar7);
    *(long *)(param_2 + 0x1e) = *(long *)(param_2 + 0x1e) + 1;
LAB_005dfff0:
    local_90 = local_90 + 10;
    puVar6 = (undefined8 *)FUN_005df9bc(lVar5 + 0x162a0,&local_88);
    puVar8 = (undefined8 *)*puVar6;
    if ((undefined8 *)*puVar6 == (undefined8 *)0x0) {
      FUN_005dfac0(local_80,lVar5 + 0x162a0,&DAT_002c8785,&local_90,&uStack_91);
      *local_80[0] = 0;
      local_80[0][1] = 0;
      local_80[0][2] = local_88;
      *puVar6 = local_80[0];
      puVar8 = local_80[0];
      if (**(long **)(lVar5 + 0x162a0) != 0) {
        *(long *)(lVar5 + 0x162a0) = **(long **)(lVar5 + 0x162a0);
        puVar8 = (undefined8 *)*puVar6;
      }
      FUN_0043bf04(*(undefined8 *)(lVar5 + 0x162a8),puVar8);
      *(long *)(lVar5 + 0x162b0) = *(long *)(lVar5 + 0x162b0) + 1;
      puVar8 = local_80[0];
    }
    goto LAB_005e0070;
  case 0x11:
    if (DAT_00ca5a38 == 0) {
      lVar5 = 0;
    }
    else {
      lVar5 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c72a18,0);
    }
    piVar9 = *(int **)(param_2 + 0x1c);
    piVar7 = param_2 + 0x1c;
    while (piVar10 = piVar7, piVar9 != (int *)0x0) {
      while (local_90 = piVar9, piVar7 = local_90, local_90[8] <= param_3) {
        if (param_3 <= local_90[8]) goto LAB_005dfec4;
        piVar9 = *(int **)(local_90 + 2);
        if (*(int **)(local_90 + 2) == (int *)0x0) {
          piVar10 = local_90 + 2;
          goto LAB_005dfe60;
        }
      }
      piVar9 = *(int **)local_90;
    }
LAB_005dfe60:
                    /* try { // try from 005dfe60 to 006dfea7 has its CatchHandler @ 005e0128 */
    local_90 = (int *)_Znwm(0x40);
    local_90[8] = param_3;
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
    piVar7 = local_90;
    if (**(long **)(param_2 + 0x1a) != 0) {
      *(long *)(param_2 + 0x1a) = **(long **)(param_2 + 0x1a);
      piVar7 = *(int **)piVar10;
    }
    FUN_0043bf04(*(undefined8 *)(param_2 + 0x1c),piVar7);
    *(long *)(param_2 + 0x1e) = *(long *)(param_2 + 0x1e) + 1;
LAB_005dfec4:
    local_90 = local_90 + 10;
    puVar6 = (undefined8 *)FUN_005df9bc(lVar5 + 0x162a0,&local_88);
    puVar8 = (undefined8 *)*puVar6;
    if ((undefined8 *)*puVar6 == (undefined8 *)0x0) {
                    /* try { // try from 005dfee0 to 006dfeeb has its CatchHandler @ 005e0108 */
      FUN_005dfac0(local_80,lVar5 + 0x162a0,&DAT_002c8785,&local_90,&uStack_91);
      *local_80[0] = 0;
      local_80[0][1] = 0;
      local_80[0][2] = local_88;
                    /* try { // try from 005dff10 to 006dff1b has its CatchHandler @ 005e0104 */
      *puVar6 = local_80[0];
      puVar8 = local_80[0];
      if (**(long **)(lVar5 + 0x162a0) != 0) {
        *(long *)(lVar5 + 0x162a0) = **(long **)(lVar5 + 0x162a0);
        puVar8 = (undefined8 *)*puVar6;
      }
      FUN_0043bf04(*(undefined8 *)(lVar5 + 0x162a8),puVar8);
      *(long *)(lVar5 + 0x162b0) = *(long *)(lVar5 + 0x162b0) + 1;
      puVar8 = local_80[0];
    }
LAB_005e0070:
    iVar4 = FUN_0046f164(puVar8 + 7);
    fVar12 = (float)iVar4;
LAB_005e0080:
    param_1 = (ulong)(uint)(fVar12 + fVar11);
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 005e00a0 to 006e015b has its CatchHandler @ 005dfa3c */
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
<a id="insn-005dfbbc"></a> `005dfbbc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-005dfbc0"></a> `005dfbc0` | `e8 23 00 fd` | str d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005dfbc4"></a> `005dfbc4` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005dfbc8"></a> `005dfbc8` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005dfbcc"></a> `005dfbcc` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005dfbd0"></a> `005dfbd0` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005dfbd4"></a> `005dfbd4` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005dfbd8"></a> `005dfbd8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-005dfbdc"></a> `005dfbdc` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-005dfbe0"></a> `005dfbe0` | `48 04 00 51` | sub w8,w2,#0x1 | `FALL_THROUGH`
<a id="insn-005dfbe4"></a> `005dfbe4` | `a9 16 40 f9` | ldr x9,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005dfbe8"></a> `005dfbe8` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-005dfbec"></a> `005dfbec` | `a9 83 1e f8` | stur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-005dfbf0"></a> `005dfbf0` | `a8 24 00 54` | b.hi 0x005e0084 | `CONDITIONAL_JUMP`
<a id="insn-005dfbf4"></a> `005dfbf4` | `c9 e7 ff b0` | adrp x9,0x2d8000 | `FALL_THROUGH`
<a id="insn-005dfbf8"></a> `005dfbf8` | `29 51 1a 91` | add x9,x9,#0x694 | `FALL_THROUGH`
<a id="insn-005dfbfc"></a> `005dfbfc` | `8a 00 00 10` | adr x10,0x5dfc0c | `FALL_THROUGH`
<a id="insn-005dfc00"></a> `005dfc00` | `2b 79 68 78` | ldrh w11,[x9, x8, LSL #0x1] | `FALL_THROUGH`
<a id="insn-005dfc04"></a> `005dfc04` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-005dfc08"></a> `005dfc08` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-005dfc0c"></a> `005dfc0c` | `08 8e a8 52` | mov w8,#0x44700000 | `FALL_THROUGH`
<a id="insn-005dfc10"></a> `005dfc10` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005dfc14"></a> `005dfc14` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfc18"></a> `005dfc18` | `1b 01 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfc1c"></a> `005dfc1c` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfc20"></a> `005dfc20` | `28 36 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-005dfc24"></a> `005dfc24` | `08 1d 45 f9` | ldr x8,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-005dfc28"></a> `005dfc28` | `68 0f 00 b4` | cbz x8,0x005dfe14 | `CONDITIONAL_JUMP`
<a id="insn-005dfc2c"></a> `005dfc2c` | `29 34 00 f0` | adrp x9,0xc66000 | `FALL_THROUGH`
<a id="insn-005dfc30"></a> `005dfc30` | `29 e1 3b 91` | add x9,x9,#0xef8 | `FALL_THROUGH`
<a id="insn-005dfc34"></a> `005dfc34` | `82 34 00 f0` | adrp x2,0xc72000 | `FALL_THROUGH`
<a id="insn-005dfc38"></a> `005dfc38` | `42 60 28 91` | add x2,x2,#0xa18 | `FALL_THROUGH`
<a id="insn-005dfc3c"></a> `005dfc3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dfc40"></a> `005dfc40` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005dfc44"></a> `005dfc44` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-005dfc48"></a> `005dfc48` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-005dfc4c"></a> `005dfc4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-005dfc50"></a> `005dfc50` | `98 e6 19 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-005dfc54"></a> `005dfc54` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-005dfc58"></a> `005dfc58` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005dfc5c"></a> `005dfc5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005dfc60"></a> `005dfc60` | `6e 00 00 14` | b 0x005dfe18 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfc64"></a> `005dfc64` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfc68"></a> `005dfc68` | `25 ca 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfc6c"></a> `005dfc6c` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-005dfc70"></a> `005dfc70` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfc74"></a> `005dfc74` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dfc78"></a> `005dfc78` | `21 ca 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfc7c"></a> `005dfc7c` | `5a 34 fa 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-005dfc80"></a> `005dfc80` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-005dfc84"></a> `005dfc84` | `e9 63 99 12` | mov w9,#0xffff34e0 | `FALL_THROUGH`
<a id="insn-005dfc88"></a> `005dfc88` | `14 24 08 1b` | madd w20,w0,w8,w9 | `FALL_THROUGH`
<a id="insn-005dfc8c"></a> `005dfc8c` | `1c ca 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfc90"></a> `005dfc90` | `88 d6 88 52` | mov w8,#0x46b4 | `FALL_THROUGH`
<a id="insn-005dfc94"></a> `005dfc94` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005dfc98"></a> `005dfc98` | `08 01 a0 72` | movk w8,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfc9c"></a> `005dfc9c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dfca0"></a> `005dfca0` | `88 0e c8 1a` | sdiv w8,w20,w8 | `FALL_THROUGH`
<a id="insn-005dfca4"></a> `005dfca4` | `08 01 13 4b` | sub w8,w8,w19 | `FALL_THROUGH`
<a id="insn-005dfca8"></a> `005dfca8` | `08 21 08 11` | add w8,w8,#0x208 | `FALL_THROUGH`
<a id="insn-005dfcac"></a> `005dfcac` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005dfcb0"></a> `005dfcb0` | `f4 00 00 14` | b 0x005e0080 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfcb4"></a> `005dfcb4` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfcb8"></a> `005dfcb8` | `28 36 00 d0` | adrp x8,0xca5000 | `FALL_THROUGH`
<a id="insn-005dfcbc"></a> `005dfcbc` | `08 1d 45 f9` | ldr x8,[x8, #0xa38] | `FALL_THROUGH`
<a id="insn-005dfcc0"></a> `005dfcc0` | `08 14 00 b4` | cbz x8,0x005dff40 | `CONDITIONAL_JUMP`
<a id="insn-005dfcc4"></a> `005dfcc4` | `29 34 00 f0` | adrp x9,0xc66000 | `FALL_THROUGH`
<a id="insn-005dfcc8"></a> `005dfcc8` | `29 e1 3b 91` | add x9,x9,#0xef8 | `FALL_THROUGH`
<a id="insn-005dfccc"></a> `005dfccc` | `82 34 00 f0` | adrp x2,0xc72000 | `FALL_THROUGH`
<a id="insn-005dfcd0"></a> `005dfcd0` | `42 60 28 91` | add x2,x2,#0xa18 | `FALL_THROUGH`
<a id="insn-005dfcd4"></a> `005dfcd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dfcd8"></a> `005dfcd8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-005dfcdc"></a> `005dfcdc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-005dfce0"></a> `005dfce0` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-005dfce4"></a> `005dfce4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-005dfce8"></a> `005dfce8` | `72 e6 19 94` | bl 0x00c596b0 | `UNCONDITIONAL_CALL`
<a id="insn-005dfcec"></a> `005dfcec` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-005dfcf0"></a> `005dfcf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005dfcf4"></a> `005dfcf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-005dfcf8"></a> `005dfcf8` | `93 00 00 14` | b 0x005dff44 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfcfc"></a> `005dfcfc` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfd00"></a> `005dfd00` | `ff c9 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfd04"></a> `005dfd04` | `08 34 fa 97` | bl 0x0046cd24 | `UNCONDITIONAL_CALL`
<a id="insn-005dfd08"></a> `005dfd08` | `37 00 00 14` | b 0x005dfde4 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfd0c"></a> `005dfd0c` | `e8 6f a8 52` | mov w8,#0x437f0000 | `FALL_THROUGH`
<a id="insn-005dfd10"></a> `005dfd10` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005dfd14"></a> `005dfd14` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfd18"></a> `005dfd18` | `08 59 a8 52` | mov w8,#0x42c80000 | `FALL_THROUGH`
<a id="insn-005dfd1c"></a> `005dfd1c` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-005dfd20"></a> `005dfd20` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfd24"></a> `005dfd24` | `d8 00 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfd28"></a> `005dfd28` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfd2c"></a> `005dfd2c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005dfd30"></a> `005dfd30` | `f3 c9 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfd34"></a> `005dfd34` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-005dfd38"></a> `005dfd38` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-005dfd3c"></a> `005dfd3c` | `0a 6a 98 52` | mov w10,#0xc350 | `FALL_THROUGH`
<a id="insn-005dfd40"></a> `005dfd40` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfd44"></a> `005dfd44` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dfd48"></a> `005dfd48` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-005dfd4c"></a> `005dfd4c` | `08 a5 88 1a` | cinc w8,w8,lt | `FALL_THROUGH`
<a id="insn-005dfd50"></a> `005dfd50` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-005dfd54"></a> `005dfd54` | `14 29 09 1b` | madd w20,w8,w9,w10 | `FALL_THROUGH`
<a id="insn-005dfd58"></a> `005dfd58` | `e9 c9 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfd5c"></a> `005dfd5c` | `88 d6 88 52` | mov w8,#0x46b4 | `FALL_THROUGH`
<a id="insn-005dfd60"></a> `005dfd60` | `69 06 40 b9` | ldr w9,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-005dfd64"></a> `005dfd64` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005dfd68"></a> `005dfd68` | `08 01 a0 72` | movk w8,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfd6c"></a> `005dfd6c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dfd70"></a> `005dfd70` | `88 0e c8 1a` | sdiv w8,w20,w8 | `FALL_THROUGH`
<a id="insn-005dfd74"></a> `005dfd74` | `28 01 08 4b` | sub w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005dfd78"></a> `005dfd78` | `08 81 07 11` | add w8,w8,#0x1e0 | `FALL_THROUGH`
<a id="insn-005dfd7c"></a> `005dfd7c` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005dfd80"></a> `005dfd80` | `c0 00 00 14` | b 0x005e0080 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfd84"></a> `005dfd84` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfd88"></a> `005dfd88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005dfd8c"></a> `005dfd8c` | `dc c9 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfd90"></a> `005dfd90` | `08 d2 9e 52` | mov w8,#0xf690 | `FALL_THROUGH`
<a id="insn-005dfd94"></a> `005dfd94` | `69 02 40 b9` | ldr w9,[x19] | `FALL_THROUGH`
<a id="insn-005dfd98"></a> `005dfd98` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-005dfd9c"></a> `005dfd9c` | `28 01 a0 72` | movk w8,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfda0"></a> `005dfda0` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005dfda4"></a> `005dfda4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dfda8"></a> `005dfda8` | `28 01 08 0b` | add w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005dfdac"></a> `005dfdac` | `01 01 22 1e` | scvtf s1,w8 | `FALL_THROUGH`
<a id="insn-005dfdb0"></a> `005dfdb0` | `21 18 22 1e` | fdiv s1,s1,s2 | `FALL_THROUGH`
<a id="insn-005dfdb4"></a> `005dfdb4` | `b3 00 00 14` | b 0x005e0080 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfdb8"></a> `005dfdb8` | `08 00 40 b9` | ldr w8,[x0] | `FALL_THROUGH`
<a id="insn-005dfdbc"></a> `005dfdbc` | `02 90 74 1e` | fmov d2,-0x3fdc000000000000 | `FALL_THROUGH`
<a id="insn-005dfdc0"></a> `005dfdc0` | `00 c0 22 1e` | fcvt d0,s0 | `FALL_THROUGH`
<a id="insn-005dfdc4"></a> `005dfdc4` | `01 01 62 1e` | scvtf d1,w8 | `FALL_THROUGH`
<a id="insn-005dfdc8"></a> `005dfdc8` | `21 18 62 1e` | fdiv d1,d1,d2 | `FALL_THROUGH`
<a id="insn-005dfdcc"></a> `005dfdcc` | `00 28 61 1e` | fadd d0,d0,d1 | `FALL_THROUGH`
<a id="insn-005dfdd0"></a> `005dfdd0` | `00 40 62 1e` | fcvt s0,d0 | `FALL_THROUGH`
<a id="insn-005dfdd4"></a> `005dfdd4` | `ac 00 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfdd8"></a> `005dfdd8` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-005dfddc"></a> `005dfddc` | `c8 c9 09 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-005dfde0"></a> `005dfde0` | `01 34 fa 97` | bl 0x0046cde4 | `UNCONDITIONAL_CALL`
<a id="insn-005dfde4"></a> `005dfde4` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005dfde8"></a> `005dfde8` | `01 00 22 1e` | scvtf s1,w0 | `FALL_THROUGH`
<a id="insn-005dfdec"></a> `005dfdec` | `a5 00 00 14` | b 0x005e0080 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfdf0"></a> `005dfdf0` | `01 10 2e 1e` | fmov s1,0x3f800000 | `FALL_THROUGH`
<a id="insn-005dfdf4"></a> `005dfdf4` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfdf8"></a> `005dfdf8` | `a3 00 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfdfc"></a> `005dfdfc` | `01 d0 27 1e` | fmov s1,0x41f00000 | `FALL_THROUGH`
<a id="insn-005dfe00"></a> `005dfe00` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfe04"></a> `005dfe04` | `a0 00 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfe08"></a> `005dfe08` | `01 10 20 1e` | fmov s1,0x40000000 | `FALL_THROUGH`
<a id="insn-005dfe0c"></a> `005dfe0c` | `00 28 21 1e` | fadd s0,s0,s1 | `FALL_THROUGH`
<a id="insn-005dfe10"></a> `005dfe10` | `9d 00 00 14` | b 0x005e0084 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfe14"></a> `005dfe14` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-005dfe18"></a> `005dfe18` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005dfe1c"></a> `005dfe1c` | `16 54 8c 52` | mov w22,#0x62a0 | `FALL_THROUGH`
<a id="insn-005dfe20"></a> `005dfe20` | `e8 0e 47 f8` | ldr x8,[x23, #0x70]! | `FALL_THROUGH`
<a id="insn-005dfe24"></a> `005dfe24` | `36 00 a0 72` | movk w22,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-005dfe28"></a> `005dfe28` | `c8 00 00 b5` | cbnz x8,0x005dfe40 | `CONDITIONAL_JUMP`
<a id="insn-005dfe2c"></a> `005dfe2c` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-005dfe30"></a> `005dfe30` | `0c 00 00 14` | b 0x005dfe60 | `UNCONDITIONAL_JUMP`
<a id="insn-005dfe34"></a> `005dfe34` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-005dfe38"></a> `005dfe38` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-005dfe3c"></a> `005dfe3c` | `28 01 00 b4` | cbz x8,0x005dfe60 | `CONDITIONAL_JUMP`
<a id="insn-005dfe40"></a> `005dfe40` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-005dfe44"></a> `005dfe44` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-005dfe48"></a> `005dfe48` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-005dfe4c"></a> `005dfe4c` | `4c ff ff 54` | b.gt 0x005dfe34 | `CONDITIONAL_JUMP`
<a id="insn-005dfe50"></a> `005dfe50` | `aa 03 00 54` | b.ge 0x005dfec4 | `CONDITIONAL_JUMP`
<a id="insn-005dfe54"></a> `005dfe54` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005dfe58"></a> `005dfe58` | `48 ff ff b5` | cbnz x8,0x005dfe40 | `CONDITIONAL_JUMP`
<a id="insn-005dfe5c"></a> `005dfe5c` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe60"></a> `005dfe60` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-005dfe64"></a> `005dfe64` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-005dfe68"></a> `005dfe68` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-005dfe6c"></a> `005dfe6c` | `fa 03 01 2a` | mov w26,w1 | `FALL_THROUGH`
<a id="insn-005dfe70"></a> `005dfe70` | `30 e4 19 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe74"></a> `005dfe74` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-005dfe78"></a> `005dfe78` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dfe7c"></a> `005dfe7c` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-005dfe80"></a> `005dfe80` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-005dfe84"></a> `005dfe84` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-005dfe88"></a> `005dfe88` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-005dfe8c"></a> `005dfe8c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-005dfe90"></a> `005dfe90` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-005dfe94"></a> `005dfe94` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-005dfe98"></a> `005dfe98` | `09 37 40 f9` | ldr x9,[x24, #0x68] | `FALL_THROUGH`
<a id="insn-005dfe9c"></a> `005dfe9c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005dfea0"></a> `005dfea0` | `69 00 00 b4` | cbz x9,0x005dfeac | `CONDITIONAL_JUMP`
<a id="insn-005dfea4"></a> `005dfea4` | `09 35 00 f9` | str x9,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-005dfea8"></a> `005dfea8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005dfeac"></a> `005dfeac` | `00 39 40 f9` | ldr x0,[x8, #0x70] | `FALL_THROUGH`
<a id="insn-005dfeb0"></a> `005dfeb0` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-005dfeb4"></a> `005dfeb4` | `14 70 f9 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-005dfeb8"></a> `005dfeb8` | `e8 3e 40 f9` | ldr x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005dfebc"></a> `005dfebc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005dfec0"></a> `005dfec0` | `e8 3e 00 f9` | str x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005dfec4"></a> `005dfec4` | `82 a2 00 91` | add x2,x20,#0x28 | `FALL_THROUGH`
<a id="insn-005dfec8"></a> `005dfec8` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005dfecc"></a> `005dfecc` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-005dfed0"></a> `005dfed0` | `e2 0b 00 f9` | str x2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dfed4"></a> `005dfed4` | `ba fe ff 97` | bl 0x005df9bc | `UNCONDITIONAL_CALL`
<a id="insn-005dfed8"></a> `005dfed8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-005dfedc"></a> `005dfedc` | `a8 0c 00 b5` | cbnz x8,0x005e0070 | `CONDITIONAL_JUMP`
<a id="insn-005dfee0"></a> `005dfee0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dfee4"></a> `005dfee4` | `41 e7 ff b0` | adrp x1,0x2c8000 | `FALL_THROUGH`
<a id="insn-005dfee8"></a> `005dfee8` | `21 14 1e 91` | add x1,x1,#0x785 | `FALL_THROUGH`
<a id="insn-005dfeec"></a> `005dfeec` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-005dfef0"></a> `005dfef0` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005dfef4"></a> `005dfef4` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-005dfef8"></a> `005dfef8` | `e3 3f 00 91` | add x3,sp,#0xf | `FALL_THROUGH`
<a id="insn-005dfefc"></a> `005dfefc` | `77 5a 40 91` | add x23,x19,#0x16, LSL #12 | `FALL_THROUGH`
<a id="insn-005dff00"></a> `005dff00` | `f0 fe ff 97` | bl 0x005dfac0 | `UNCONDITIONAL_CALL`
<a id="insn-005dff04"></a> `005dff04` | `e8 87 41 a9` | ldp x8,x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005dff08"></a> `005dff08` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-005dff0c"></a> `005dff0c` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-005dff10"></a> `005dff10` | `81 02 00 f9` | str x1,[x20] | `FALL_THROUGH`
<a id="insn-005dff14"></a> `005dff14` | `68 6a 76 f8` | ldr x8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dff18"></a> `005dff18` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-005dff1c"></a> `005dff1c` | `68 00 00 b4` | cbz x8,0x005dff28 | `CONDITIONAL_JUMP`
<a id="insn-005dff20"></a> `005dff20` | `68 6a 36 f8` | str x8,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005dff24"></a> `005dff24` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-005dff28"></a> `005dff28` | `e0 56 41 f9` | ldr x0,[x23, #0x2a8] | `FALL_THROUGH`
<a id="insn-005dff2c"></a> `005dff2c` | `f6 6f f9 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-005dff30"></a> `005dff30` | `e8 5a 41 f9` | ldr x8,[x23, #0x2b0] | `FALL_THROUGH`
<a id="insn-005dff34"></a> `005dff34` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005dff38"></a> `005dff38` | `e8 5a 01 f9` | str x8,[x23, #0x2b0] | `FALL_THROUGH`
<a id="insn-005dff3c"></a> `005dff3c` | `4c 00 00 14` | b 0x005e006c | `UNCONDITIONAL_JUMP`
<a id="insn-005dff40"></a> `005dff40` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-005dff44"></a> `005dff44` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005dff48"></a> `005dff48` | `16 54 8c 52` | mov w22,#0x62a0 | `FALL_THROUGH`
<a id="insn-005dff4c"></a> `005dff4c` | `e8 0e 47 f8` | ldr x8,[x23, #0x70]! | `FALL_THROUGH`
<a id="insn-005dff50"></a> `005dff50` | `36 00 a0 72` | movk w22,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-005dff54"></a> `005dff54` | `c8 00 00 b5` | cbnz x8,0x005dff6c | `CONDITIONAL_JUMP`
<a id="insn-005dff58"></a> `005dff58` | `f4 03 17 aa` | mov x20,x23 | `FALL_THROUGH`
<a id="insn-005dff5c"></a> `005dff5c` | `0c 00 00 14` | b 0x005dff8c | `UNCONDITIONAL_JUMP`
<a id="insn-005dff60"></a> `005dff60` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-005dff64"></a> `005dff64` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-005dff68"></a> `005dff68` | `28 01 00 b4` | cbz x8,0x005dff8c | `CONDITIONAL_JUMP`
<a id="insn-005dff6c"></a> `005dff6c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-005dff70"></a> `005dff70` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-005dff74"></a> `005dff74` | `1f 01 01 6b` | cmp w8,w1 | `FALL_THROUGH`
<a id="insn-005dff78"></a> `005dff78` | `4c ff ff 54` | b.gt 0x005dff60 | `CONDITIONAL_JUMP`
<a id="insn-005dff7c"></a> `005dff7c` | `aa 03 00 54` | b.ge 0x005dfff0 | `CONDITIONAL_JUMP`
<a id="insn-005dff80"></a> `005dff80` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005dff84"></a> `005dff84` | `48 ff ff b5` | cbnz x8,0x005dff6c | `CONDITIONAL_JUMP`
<a id="insn-005dff88"></a> `005dff88` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-005dff8c"></a> `005dff8c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-005dff90"></a> `005dff90` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-005dff94"></a> `005dff94` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-005dff98"></a> `005dff98` | `fa 03 01 2a` | mov w26,w1 | `FALL_THROUGH`
<a id="insn-005dff9c"></a> `005dff9c` | `e5 e3 19 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-005dffa0"></a> `005dffa0` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-005dffa4"></a> `005dffa4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dffa8"></a> `005dffa8` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-005dffac"></a> `005dffac` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-005dffb0"></a> `005dffb0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-005dffb4"></a> `005dffb4` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-005dffb8"></a> `005dffb8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-005dffbc"></a> `005dffbc` | `19 08 00 f9` | str x25,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-005dffc0"></a> `005dffc0` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-005dffc4"></a> `005dffc4` | `09 37 40 f9` | ldr x9,[x24, #0x68] | `FALL_THROUGH`
<a id="insn-005dffc8"></a> `005dffc8` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005dffcc"></a> `005dffcc` | `69 00 00 b4` | cbz x9,0x005dffd8 | `CONDITIONAL_JUMP`
<a id="insn-005dffd0"></a> `005dffd0` | `09 35 00 f9` | str x9,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-005dffd4"></a> `005dffd4` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005dffd8"></a> `005dffd8` | `00 39 40 f9` | ldr x0,[x8, #0x70] | `FALL_THROUGH`
<a id="insn-005dffdc"></a> `005dffdc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-005dffe0"></a> `005dffe0` | `c9 6f f9 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-005dffe4"></a> `005dffe4` | `e8 3e 40 f9` | ldr x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005dffe8"></a> `005dffe8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005dffec"></a> `005dffec` | `e8 3e 00 f9` | str x8,[x23, #0x78] | `FALL_THROUGH`
<a id="insn-005dfff0"></a> `005dfff0` | `82 a2 00 91` | add x2,x20,#0x28 | `FALL_THROUGH`
<a id="insn-005dfff4"></a> `005dfff4` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005dfff8"></a> `005dfff8` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-005dfffc"></a> `005dfffc` | `e2 0b 00 f9` | str x2,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005e0000"></a> `005e0000` | `6f fe ff 97` | bl 0x005df9bc | `UNCONDITIONAL_CALL`
<a id="insn-005e0004"></a> `005e0004` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-005e0008"></a> `005e0008` | `48 03 00 b5` | cbnz x8,0x005e0070 | `CONDITIONAL_JUMP`
<a id="insn-005e000c"></a> `005e000c` | `41 e7 ff 90` | adrp x1,0x2c8000 | `FALL_THROUGH`
<a id="insn-005e0010"></a> `005e0010` | `21 14 1e 91` | add x1,x1,#0x785 | `FALL_THROUGH`
<a id="insn-005e0014"></a> `005e0014` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-005e0018"></a> `005e0018` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-005e001c"></a> `005e001c` | `60 02 16 8b` | add x0,x19,x22 | `FALL_THROUGH`
<a id="insn-005e0020"></a> `005e0020` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-005e0024"></a> `005e0024` | `e3 3f 00 91` | add x3,sp,#0xf | `FALL_THROUGH`
<a id="insn-005e0028"></a> `005e0028` | `74 5a 40 91` | add x20,x19,#0x16, LSL #12 | `FALL_THROUGH`
<a id="insn-005e002c"></a> `005e002c` | `a5 fe ff 97` | bl 0x005dfac0 | `UNCONDITIONAL_CALL`
<a id="insn-005e0030"></a> `005e0030` | `e9 87 41 a9` | ldp x9,x1,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-005e0034"></a> `005e0034` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-005e0038"></a> `005e0038` | `29 08 00 f9` | str x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-005e003c"></a> `005e003c` | `e1 02 00 f9` | str x1,[x23] | `FALL_THROUGH`
<a id="insn-005e0040"></a> `005e0040` | `69 6a 76 f8` | ldr x9,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005e0044"></a> `005e0044` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-005e0048"></a> `005e0048` | `89 00 00 b4` | cbz x9,0x005e0058 | `CONDITIONAL_JUMP`
<a id="insn-005e004c"></a> `005e004c` | `69 6a 36 f8` | str x9,[x19, x22, LSL #0x0] | `FALL_THROUGH`
<a id="insn-005e0050"></a> `005e0050` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-005e0054"></a> `005e0054` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-005e0058"></a> `005e0058` | `80 56 41 f9` | ldr x0,[x20, #0x2a8] | `FALL_THROUGH`
<a id="insn-005e005c"></a> `005e005c` | `aa 6f f9 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-005e0060"></a> `005e0060` | `88 5a 41 f9` | ldr x8,[x20, #0x2b0] | `FALL_THROUGH`
<a id="insn-005e0064"></a> `005e0064` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005e0068"></a> `005e0068` | `88 5a 01 f9` | str x8,[x20, #0x2b0] | `FALL_THROUGH`
<a id="insn-005e006c"></a> `005e006c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005e0070"></a> `005e0070` | `00 e1 00 91` | add x0,x8,#0x38 | `FALL_THROUGH`
<a id="insn-005e0074"></a> `005e0074` | `3c 3c fa 97` | bl 0x0046f164 | `UNCONDITIONAL_CALL`
<a id="insn-005e0078"></a> `005e0078` | `01 00 22 1e` | scvtf s1,w0 | `FALL_THROUGH`
<a id="insn-005e007c"></a> `005e007c` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-005e0080"></a> `005e0080` | `20 28 28 1e` | fadd s0,s1,s8 | `FALL_THROUGH`
<a id="insn-005e0084"></a> `005e0084` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-005e0088"></a> `005e0088` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-005e008c"></a> `005e008c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-005e0090"></a> `005e0090` | `21 01 00 54` | b.ne 0x005e00b4 | `CONDITIONAL_JUMP`
<a id="insn-005e0094"></a> `005e0094` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-005e0098"></a> `005e0098` | `e8 23 40 fd` | ldr d8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-005e009c"></a> `005e009c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-005e00a0"></a> `005e00a0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-005e00a4"></a> `005e00a4` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-005e00a8"></a> `005e00a8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-005e00ac"></a> `005e00ac` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-005e00b0"></a> `005e00b0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005e00b4"></a> `005e00b4` | `b3 e3 19 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005dfbbc`](#insn-005dfbbc) 範囲 `[['005dfbbc', '005dfbcb']]`
  - `FALL_THROUGH` [`005dfbc8`](#insn-005dfbc8) → [`005dfbcc`](#insn-005dfbcc)
- ブロック [`005dfbcc`](#insn-005dfbcc) 範囲 `[['005dfbcc', '005dfbd7']]`
  - `FALL_THROUGH` [`005dfbd4`](#insn-005dfbd4) → [`005dfbd8`](#insn-005dfbd8)
- ブロック [`005dfbd8`](#insn-005dfbd8) 範囲 `[['005dfbd8', '005dfbf3']]`
  - `CONDITIONAL_JUMP` [`005dfbf0`](#insn-005dfbf0) → [`005e0084`](#insn-005e0084)
  - `FALL_THROUGH` [`005dfbf0`](#insn-005dfbf0) → [`005dfbf4`](#insn-005dfbf4)
- ブロック [`005dfbf4`](#insn-005dfbf4) 範囲 `[['005dfbf4', '005dfc07']]`
  - `FALL_THROUGH` [`005dfc04`](#insn-005dfc04) → [`005dfc08`](#insn-005dfc08)
- ブロック [`005dfc08`](#insn-005dfc08) 範囲 `[['005dfc08', '005dfc0b']]`
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfc0c`](#insn-005dfc0c)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfdb8`](#insn-005dfdb8)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfd84`](#insn-005dfd84)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfd28`](#insn-005dfd28)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfc64`](#insn-005dfc64)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005e0084`](#insn-005e0084)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfcfc`](#insn-005dfcfc)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfdd8`](#insn-005dfdd8)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfdf0`](#insn-005dfdf0)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfe08`](#insn-005dfe08)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfdfc`](#insn-005dfdfc)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfd18`](#insn-005dfd18)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfd0c`](#insn-005dfd0c)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfcb4`](#insn-005dfcb4)
  - `COMPUTED_JUMP` [`005dfc08`](#insn-005dfc08) → [`005dfc1c`](#insn-005dfc1c)
- ブロック [`005dfc0c`](#insn-005dfc0c) 範囲 `[['005dfc0c', '005dfc13']]`
  - `FALL_THROUGH` [`005dfc10`](#insn-005dfc10) → [`005dfc14`](#insn-005dfc14)
- ブロック [`005dfc14`](#insn-005dfc14) 範囲 `[['005dfc14', '005dfc1b']]`
  - `UNCONDITIONAL_JUMP` [`005dfc18`](#insn-005dfc18) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfc1c`](#insn-005dfc1c) 範囲 `[['005dfc1c', '005dfc2b']]`
  - `CONDITIONAL_JUMP` [`005dfc28`](#insn-005dfc28) → [`005dfe14`](#insn-005dfe14)
  - `FALL_THROUGH` [`005dfc28`](#insn-005dfc28) → [`005dfc2c`](#insn-005dfc2c)
- ブロック [`005dfc2c`](#insn-005dfc2c) 範囲 `[['005dfc2c', '005dfc63']]`
  - `UNCONDITIONAL_JUMP` [`005dfc60`](#insn-005dfc60) → [`005dfe18`](#insn-005dfe18)
- ブロック [`005dfc64`](#insn-005dfc64) 範囲 `[['005dfc64', '005dfc83']]`
  - `FALL_THROUGH` [`005dfc80`](#insn-005dfc80) → [`005dfc84`](#insn-005dfc84)
- ブロック [`005dfc84`](#insn-005dfc84) 範囲 `[['005dfc84', '005dfcb3']]`
  - `UNCONDITIONAL_JUMP` [`005dfcb0`](#insn-005dfcb0) → [`005e0080`](#insn-005e0080)
- ブロック [`005dfcb4`](#insn-005dfcb4) 範囲 `[['005dfcb4', '005dfcc3']]`
  - `CONDITIONAL_JUMP` [`005dfcc0`](#insn-005dfcc0) → [`005dff40`](#insn-005dff40)
  - `FALL_THROUGH` [`005dfcc0`](#insn-005dfcc0) → [`005dfcc4`](#insn-005dfcc4)
- ブロック [`005dfcc4`](#insn-005dfcc4) 範囲 `[['005dfcc4', '005dfcfb']]`
  - `UNCONDITIONAL_JUMP` [`005dfcf8`](#insn-005dfcf8) → [`005dff44`](#insn-005dff44)
- ブロック [`005dfcfc`](#insn-005dfcfc) 範囲 `[['005dfcfc', '005dfd0b']]`
  - `UNCONDITIONAL_JUMP` [`005dfd08`](#insn-005dfd08) → [`005dfde4`](#insn-005dfde4)
- ブロック [`005dfd0c`](#insn-005dfd0c) 範囲 `[['005dfd0c', '005dfd13']]`
  - `FALL_THROUGH` [`005dfd10`](#insn-005dfd10) → [`005dfd14`](#insn-005dfd14)
- ブロック [`005dfd14`](#insn-005dfd14) 範囲 `[['005dfd14', '005dfd17']]`
  - `FALL_THROUGH` [`005dfd14`](#insn-005dfd14) → [`005dfd18`](#insn-005dfd18)
- ブロック [`005dfd18`](#insn-005dfd18) 範囲 `[['005dfd18', '005dfd27']]`
  - `UNCONDITIONAL_JUMP` [`005dfd24`](#insn-005dfd24) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfd28`](#insn-005dfd28) 範囲 `[['005dfd28', '005dfd5f']]`
  - `FALL_THROUGH` [`005dfd5c`](#insn-005dfd5c) → [`005dfd60`](#insn-005dfd60)
- ブロック [`005dfd60`](#insn-005dfd60) 範囲 `[['005dfd60', '005dfd83']]`
  - `UNCONDITIONAL_JUMP` [`005dfd80`](#insn-005dfd80) → [`005e0080`](#insn-005e0080)
- ブロック [`005dfd84`](#insn-005dfd84) 範囲 `[['005dfd84', '005dfdb7']]`
  - `UNCONDITIONAL_JUMP` [`005dfdb4`](#insn-005dfdb4) → [`005e0080`](#insn-005e0080)
- ブロック [`005dfdb8`](#insn-005dfdb8) 範囲 `[['005dfdb8', '005dfdcf']]`
  - `FALL_THROUGH` [`005dfdcc`](#insn-005dfdcc) → [`005dfdd0`](#insn-005dfdd0)
- ブロック [`005dfdd0`](#insn-005dfdd0) 範囲 `[['005dfdd0', '005dfdd7']]`
  - `UNCONDITIONAL_JUMP` [`005dfdd4`](#insn-005dfdd4) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfdd8`](#insn-005dfdd8) 範囲 `[['005dfdd8', '005dfde3']]`
  - `FALL_THROUGH` [`005dfde0`](#insn-005dfde0) → [`005dfde4`](#insn-005dfde4)
- ブロック [`005dfde4`](#insn-005dfde4) 範囲 `[['005dfde4', '005dfdef']]`
  - `UNCONDITIONAL_JUMP` [`005dfdec`](#insn-005dfdec) → [`005e0080`](#insn-005e0080)
- ブロック [`005dfdf0`](#insn-005dfdf0) 範囲 `[['005dfdf0', '005dfdfb']]`
  - `UNCONDITIONAL_JUMP` [`005dfdf8`](#insn-005dfdf8) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfdfc`](#insn-005dfdfc) 範囲 `[['005dfdfc', '005dfe07']]`
  - `UNCONDITIONAL_JUMP` [`005dfe04`](#insn-005dfe04) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfe08`](#insn-005dfe08) 範囲 `[['005dfe08', '005dfe13']]`
  - `UNCONDITIONAL_JUMP` [`005dfe10`](#insn-005dfe10) → [`005e0084`](#insn-005e0084)
- ブロック [`005dfe14`](#insn-005dfe14) 範囲 `[['005dfe14', '005dfe17']]`
  - `FALL_THROUGH` [`005dfe14`](#insn-005dfe14) → [`005dfe18`](#insn-005dfe18)
- ブロック [`005dfe18`](#insn-005dfe18) 範囲 `[['005dfe18', '005dfe2b']]`
  - `CONDITIONAL_JUMP` [`005dfe28`](#insn-005dfe28) → [`005dfe40`](#insn-005dfe40)
  - `FALL_THROUGH` [`005dfe28`](#insn-005dfe28) → [`005dfe2c`](#insn-005dfe2c)
- ブロック [`005dfe2c`](#insn-005dfe2c) 範囲 `[['005dfe2c', '005dfe33']]`
  - `UNCONDITIONAL_JUMP` [`005dfe30`](#insn-005dfe30) → [`005dfe60`](#insn-005dfe60)
- ブロック [`005dfe34`](#insn-005dfe34) 範囲 `[['005dfe34', '005dfe3f']]`
  - `CONDITIONAL_JUMP` [`005dfe3c`](#insn-005dfe3c) → [`005dfe60`](#insn-005dfe60)
  - `FALL_THROUGH` [`005dfe3c`](#insn-005dfe3c) → [`005dfe40`](#insn-005dfe40)
- ブロック [`005dfe40`](#insn-005dfe40) 範囲 `[['005dfe40', '005dfe4f']]`
  - `CONDITIONAL_JUMP` [`005dfe4c`](#insn-005dfe4c) → [`005dfe34`](#insn-005dfe34)
  - `FALL_THROUGH` [`005dfe4c`](#insn-005dfe4c) → [`005dfe50`](#insn-005dfe50)
- ブロック [`005dfe50`](#insn-005dfe50) 範囲 `[['005dfe50', '005dfe53']]`
  - `CONDITIONAL_JUMP` [`005dfe50`](#insn-005dfe50) → [`005dfec4`](#insn-005dfec4)
  - `FALL_THROUGH` [`005dfe50`](#insn-005dfe50) → [`005dfe54`](#insn-005dfe54)
- ブロック [`005dfe54`](#insn-005dfe54) 範囲 `[['005dfe54', '005dfe5b']]`
  - `CONDITIONAL_JUMP` [`005dfe58`](#insn-005dfe58) → [`005dfe40`](#insn-005dfe40)
  - `FALL_THROUGH` [`005dfe58`](#insn-005dfe58) → [`005dfe5c`](#insn-005dfe5c)
- ブロック [`005dfe5c`](#insn-005dfe5c) 範囲 `[['005dfe5c', '005dfe5f']]`
  - `FALL_THROUGH` [`005dfe5c`](#insn-005dfe5c) → [`005dfe60`](#insn-005dfe60)
- ブロック [`005dfe60`](#insn-005dfe60) 範囲 `[['005dfe60', '005dfea3']]`
  - `CONDITIONAL_JUMP` [`005dfea0`](#insn-005dfea0) → [`005dfeac`](#insn-005dfeac)
  - `FALL_THROUGH` [`005dfea0`](#insn-005dfea0) → [`005dfea4`](#insn-005dfea4)
- ブロック [`005dfea4`](#insn-005dfea4) 範囲 `[['005dfea4', '005dfeab']]`
  - `FALL_THROUGH` [`005dfea8`](#insn-005dfea8) → [`005dfeac`](#insn-005dfeac)
- ブロック [`005dfeac`](#insn-005dfeac) 範囲 `[['005dfeac', '005dfec3']]`
  - `FALL_THROUGH` [`005dfec0`](#insn-005dfec0) → [`005dfec4`](#insn-005dfec4)
- ブロック [`005dfec4`](#insn-005dfec4) 範囲 `[['005dfec4', '005dfedf']]`
  - `CONDITIONAL_JUMP` [`005dfedc`](#insn-005dfedc) → [`005e0070`](#insn-005e0070)
  - `FALL_THROUGH` [`005dfedc`](#insn-005dfedc) → [`005dfee0`](#insn-005dfee0)
- ブロック [`005dfee0`](#insn-005dfee0) 範囲 `[['005dfee0', '005dff0f']]`
  - `FALL_THROUGH` [`005dff0c`](#insn-005dff0c) → [`005dff10`](#insn-005dff10)
- ブロック [`005dff10`](#insn-005dff10) 範囲 `[['005dff10', '005dff1f']]`
  - `CONDITIONAL_JUMP` [`005dff1c`](#insn-005dff1c) → [`005dff28`](#insn-005dff28)
  - `FALL_THROUGH` [`005dff1c`](#insn-005dff1c) → [`005dff20`](#insn-005dff20)
- ブロック [`005dff20`](#insn-005dff20) 範囲 `[['005dff20', '005dff27']]`
  - `FALL_THROUGH` [`005dff24`](#insn-005dff24) → [`005dff28`](#insn-005dff28)
- ブロック [`005dff28`](#insn-005dff28) 範囲 `[['005dff28', '005dff3f']]`
  - `UNCONDITIONAL_JUMP` [`005dff3c`](#insn-005dff3c) → [`005e006c`](#insn-005e006c)
- ブロック [`005dff40`](#insn-005dff40) 範囲 `[['005dff40', '005dff43']]`
  - `FALL_THROUGH` [`005dff40`](#insn-005dff40) → [`005dff44`](#insn-005dff44)
- ブロック [`005dff44`](#insn-005dff44) 範囲 `[['005dff44', '005dff57']]`
  - `CONDITIONAL_JUMP` [`005dff54`](#insn-005dff54) → [`005dff6c`](#insn-005dff6c)
  - `FALL_THROUGH` [`005dff54`](#insn-005dff54) → [`005dff58`](#insn-005dff58)
- ブロック [`005dff58`](#insn-005dff58) 範囲 `[['005dff58', '005dff5f']]`
  - `UNCONDITIONAL_JUMP` [`005dff5c`](#insn-005dff5c) → [`005dff8c`](#insn-005dff8c)
- ブロック [`005dff60`](#insn-005dff60) 範囲 `[['005dff60', '005dff67']]`
  - `FALL_THROUGH` [`005dff64`](#insn-005dff64) → [`005dff68`](#insn-005dff68)
- ブロック [`005dff68`](#insn-005dff68) 範囲 `[['005dff68', '005dff6b']]`
  - `CONDITIONAL_JUMP` [`005dff68`](#insn-005dff68) → [`005dff8c`](#insn-005dff8c)
  - `FALL_THROUGH` [`005dff68`](#insn-005dff68) → [`005dff6c`](#insn-005dff6c)
- ブロック [`005dff6c`](#insn-005dff6c) 範囲 `[['005dff6c', '005dff7b']]`
  - `CONDITIONAL_JUMP` [`005dff78`](#insn-005dff78) → [`005dff60`](#insn-005dff60)
  - `FALL_THROUGH` [`005dff78`](#insn-005dff78) → [`005dff7c`](#insn-005dff7c)
- ブロック [`005dff7c`](#insn-005dff7c) 範囲 `[['005dff7c', '005dff7f']]`
  - `CONDITIONAL_JUMP` [`005dff7c`](#insn-005dff7c) → [`005dfff0`](#insn-005dfff0)
  - `FALL_THROUGH` [`005dff7c`](#insn-005dff7c) → [`005dff80`](#insn-005dff80)
- ブロック [`005dff80`](#insn-005dff80) 範囲 `[['005dff80', '005dff87']]`
  - `CONDITIONAL_JUMP` [`005dff84`](#insn-005dff84) → [`005dff6c`](#insn-005dff6c)
  - `FALL_THROUGH` [`005dff84`](#insn-005dff84) → [`005dff88`](#insn-005dff88)
- ブロック [`005dff88`](#insn-005dff88) 範囲 `[['005dff88', '005dff8b']]`
  - `FALL_THROUGH` [`005dff88`](#insn-005dff88) → [`005dff8c`](#insn-005dff8c)
- ブロック [`005dff8c`](#insn-005dff8c) 範囲 `[['005dff8c', '005dffcf']]`
  - `CONDITIONAL_JUMP` [`005dffcc`](#insn-005dffcc) → [`005dffd8`](#insn-005dffd8)
  - `FALL_THROUGH` [`005dffcc`](#insn-005dffcc) → [`005dffd0`](#insn-005dffd0)
- ブロック [`005dffd0`](#insn-005dffd0) 範囲 `[['005dffd0', '005dffd7']]`
  - `FALL_THROUGH` [`005dffd4`](#insn-005dffd4) → [`005dffd8`](#insn-005dffd8)
- ブロック [`005dffd8`](#insn-005dffd8) 範囲 `[['005dffd8', '005dffef']]`
  - `FALL_THROUGH` [`005dffec`](#insn-005dffec) → [`005dfff0`](#insn-005dfff0)
- ブロック [`005dfff0`](#insn-005dfff0) 範囲 `[['005dfff0', '005e000b']]`
  - `CONDITIONAL_JUMP` [`005e0008`](#insn-005e0008) → [`005e0070`](#insn-005e0070)
  - `FALL_THROUGH` [`005e0008`](#insn-005e0008) → [`005e000c`](#insn-005e000c)
- ブロック [`005e000c`](#insn-005e000c) 範囲 `[['005e000c', '005e004b']]`
  - `CONDITIONAL_JUMP` [`005e0048`](#insn-005e0048) → [`005e0058`](#insn-005e0058)
  - `FALL_THROUGH` [`005e0048`](#insn-005e0048) → [`005e004c`](#insn-005e004c)
- ブロック [`005e004c`](#insn-005e004c) 範囲 `[['005e004c', '005e0057']]`
  - `FALL_THROUGH` [`005e0054`](#insn-005e0054) → [`005e0058`](#insn-005e0058)
- ブロック [`005e0058`](#insn-005e0058) 範囲 `[['005e0058', '005e006b']]`
  - `FALL_THROUGH` [`005e0068`](#insn-005e0068) → [`005e006c`](#insn-005e006c)
- ブロック [`005e006c`](#insn-005e006c) 範囲 `[['005e006c', '005e006f']]`
  - `FALL_THROUGH` [`005e006c`](#insn-005e006c) → [`005e0070`](#insn-005e0070)
- ブロック [`005e0070`](#insn-005e0070) 範囲 `[['005e0070', '005e007f']]`
  - `FALL_THROUGH` [`005e007c`](#insn-005e007c) → [`005e0080`](#insn-005e0080)
- ブロック [`005e0080`](#insn-005e0080) 範囲 `[['005e0080', '005e0083']]`
  - `FALL_THROUGH` [`005e0080`](#insn-005e0080) → [`005e0084`](#insn-005e0084)
- ブロック [`005e0084`](#insn-005e0084) 範囲 `[['005e0084', '005e0093']]`
  - `CONDITIONAL_JUMP` [`005e0090`](#insn-005e0090) → [`005e00b4`](#insn-005e00b4)
  - `FALL_THROUGH` [`005e0090`](#insn-005e0090) → [`005e0094`](#insn-005e0094)
- ブロック [`005e0094`](#insn-005e0094) 範囲 `[['005e0094', '005e009f']]`
  - `FALL_THROUGH` [`005e009c`](#insn-005e009c) → [`005e00a0`](#insn-005e00a0)
- ブロック [`005e00a0`](#insn-005e00a0) 範囲 `[['005e00a0', '005e00b3']]`
- ブロック [`005e00b4`](#insn-005e00b4) 範囲 `[['005e00b4', '005e00b7']]`

## 命令位置別の参照

- [`005dfbc0`](#insn-005dfbc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbc4`](#insn-005dfbc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbc8`](#insn-005dfbc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbcc`](#insn-005dfbcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbd0`](#insn-005dfbd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbd4`](#insn-005dfbd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbec`](#insn-005dfbec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfbf0`](#insn-005dfbf0) → [`005e0084`](#insn-005e0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfc00`](#insn-005dfc00) → `002d8694`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::switchdataD_002d8694` · 推定型 `ushort`
- [`005dfc08`](#insn-005dfc08) → [`005dfc0c`](#insn-005dfc0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_1` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfdb8`](#insn-005dfdb8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_2` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfd84`](#insn-005dfd84) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_3` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfd28`](#insn-005dfd28) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_4` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfc64`](#insn-005dfc64) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_5` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005e0084`](#insn-005e0084) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfcfc`](#insn-005dfcfc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_7` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfdd8`](#insn-005dfdd8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_9` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfdf0`](#insn-005dfdf0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_b` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfe08`](#insn-005dfe08) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_c` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfdfc`](#insn-005dfdfc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_d` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfd18`](#insn-005dfd18) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_e` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfd0c`](#insn-005dfd0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_f` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfcb4`](#insn-005dfcb4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_10` · 推定型 `None`
- [`005dfc08`](#insn-005dfc08) → [`005dfc1c`](#insn-005dfc1c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_11` · 推定型 `None`
- [`005dfc18`](#insn-005dfc18) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfc24`](#insn-005dfc24) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfc28`](#insn-005dfc28) → [`005dfe14`](#insn-005dfe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfc38`](#insn-005dfc38) → `00c72a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005dfc48`](#insn-005dfc48) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005dfc50`](#insn-005dfc50) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`005dfc60`](#insn-005dfc60) → [`005dfe18`](#insn-005dfe18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfc68`](#insn-005dfc68) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfc74`](#insn-005dfc74) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`005dfc78`](#insn-005dfc78) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfc7c`](#insn-005dfc7c) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`005dfc8c`](#insn-005dfc8c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfcb0`](#insn-005dfcb0) → [`005e0080`](#insn-005e0080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfcbc`](#insn-005dfcbc) → `00ca5a38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`005dfcc0`](#insn-005dfcc0) → [`005dff40`](#insn-005dff40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfcd0`](#insn-005dfcd0) → `00c72a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005dfce0`](#insn-005dfce0) → `00c66ef8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`005dfce8`](#insn-005dfce8) → [`00c596b0`](../00c59/00c596b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596b0` · 推定シンボル `None` · 推定型 `None`
- [`005dfcf8`](#insn-005dfcf8) → [`005dff44`](#insn-005dff44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd00`](#insn-005dfd00) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfd04`](#insn-005dfd04) → [`0046cd24`](../0046c/0046cd24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cd24` · 推定シンボル `None` · 推定型 `None`
- [`005dfd08`](#insn-005dfd08) → [`005dfde4`](#insn-005dfde4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd24`](#insn-005dfd24) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfd30`](#insn-005dfd30) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfd44`](#insn-005dfd44) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`005dfd58`](#insn-005dfd58) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfd80`](#insn-005dfd80) → [`005e0080`](#insn-005e0080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfd8c`](#insn-005dfd8c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfdb4`](#insn-005dfdb4) → [`005e0080`](#insn-005e0080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdd4`](#insn-005dfdd4) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfddc`](#insn-005dfddc) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`005dfde0`](#insn-005dfde0) → [`0046cde4`](../0046c/0046cde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cde4` · 推定シンボル `None` · 推定型 `None`
- [`005dfdec`](#insn-005dfdec) → [`005e0080`](#insn-005e0080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf8`](#insn-005dfdf8) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfe04`](#insn-005dfe04) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfe10`](#insn-005dfe10) → [`005e0084`](#insn-005e0084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_005dfc08::caseD_6` · 推定型 `None`
- [`005dfe28`](#insn-005dfe28) → [`005dfe40`](#insn-005dfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe30`](#insn-005dfe30) → [`005dfe60`](#insn-005dfe60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe3c`](#insn-005dfe3c) → [`005dfe60`](#insn-005dfe60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe4c`](#insn-005dfe4c) → [`005dfe34`](#insn-005dfe34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe50`](#insn-005dfe50) → [`005dfec4`](#insn-005dfec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe58`](#insn-005dfe58) → [`005dfe40`](#insn-005dfe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe70`](#insn-005dfe70) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`005dfea0`](#insn-005dfea0) → [`005dfeac`](#insn-005dfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfeb4`](#insn-005dfeb4) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`005dfed0`](#insn-005dfed0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfed4`](#insn-005dfed4) → [`005df9bc`](005df9bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005df9bc` · 推定シンボル `None` · 推定型 `None`
- [`005dfedc`](#insn-005dfedc) → [`005e0070`](#insn-005e0070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfee8`](#insn-005dfee8) → `002c8785`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff00`](#insn-005dff00) → [`005dfac0`](005dfac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005dfac0` · 推定シンボル `None` · 推定型 `None`
- [`005dff04`](#insn-005dff04) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff1c`](#insn-005dff1c) → [`005dff28`](#insn-005dff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff2c`](#insn-005dff2c) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`005dff3c`](#insn-005dff3c) → [`005e006c`](#insn-005e006c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff54`](#insn-005dff54) → [`005dff6c`](#insn-005dff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff5c`](#insn-005dff5c) → [`005dff8c`](#insn-005dff8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff68`](#insn-005dff68) → [`005dff8c`](#insn-005dff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff78`](#insn-005dff78) → [`005dff60`](#insn-005dff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff7c`](#insn-005dff7c) → [`005dfff0`](#insn-005dfff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff84`](#insn-005dff84) → [`005dff6c`](#insn-005dff6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dff9c`](#insn-005dff9c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`005dffcc`](#insn-005dffcc) → [`005dffd8`](#insn-005dffd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dffe0`](#insn-005dffe0) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`005dfffc`](#insn-005dfffc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0000`](#insn-005e0000) → [`005df9bc`](005df9bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005df9bc` · 推定シンボル `None` · 推定型 `None`
- [`005e0008`](#insn-005e0008) → [`005e0070`](#insn-005e0070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0010`](#insn-005e0010) → `002c8785`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e002c`](#insn-005e002c) → [`005dfac0`](005dfac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005dfac0` · 推定シンボル `None` · 推定型 `None`
- [`005e0030`](#insn-005e0030) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0048`](#insn-005e0048) → [`005e0058`](#insn-005e0058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e005c`](#insn-005e005c) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`005e006c`](#insn-005e006c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0074`](#insn-005e0074) → [`0046f164`](../0046f/0046f164.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046f164` · 推定シンボル `None` · 推定型 `None`
- [`005e0088`](#insn-005e0088) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0090`](#insn-005e0090) → [`005e00b4`](#insn-005e00b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0094`](#insn-005e0094) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e0098`](#insn-005e0098) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e009c`](#insn-005e009c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e00a0`](#insn-005e00a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e00a4`](#insn-005e00a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e00a8`](#insn-005e00a8) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005e00b4`](#insn-005e00b4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005dfbc0`](#insn-005dfbc0)

~~~json
{
  "source": "005dfbc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbc4`](#insn-005dfbc4)

~~~json
{
  "source": "005dfbc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbc8`](#insn-005dfbc8)

~~~json
{
  "source": "005dfbc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbcc`](#insn-005dfbcc)

~~~json
{
  "source": "005dfbcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbd0`](#insn-005dfbd0)

~~~json
{
  "source": "005dfbd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbd4`](#insn-005dfbd4)

~~~json
{
  "source": "005dfbd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbec`](#insn-005dfbec)

~~~json
{
  "source": "005dfbec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfbf0`](#insn-005dfbf0)

~~~json
{
  "source": "005dfbf0",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc00`](#insn-005dfc00)

~~~json
{
  "source": "005dfc00",
  "target": "002d8694",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002d8694",
  "offset": 0,
  "size": 2,
  "datatype": "ushort",
  "bytes": "0000",
  "capture_start": "002d8694",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfd28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc08`](#insn-005dfc08)

~~~json
{
  "source": "005dfc08",
  "target": "005dfc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc18`](#insn-005dfc18)

~~~json
{
  "source": "005dfc18",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc24`](#insn-005dfc24)

~~~json
{
  "source": "005dfc24",
  "target": "00ca5a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5a38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfc28`](#insn-005dfc28)

~~~json
{
  "source": "005dfc28",
  "target": "005dfe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc38`](#insn-005dfc38)

~~~json
{
  "source": "005dfc38",
  "target": "00c72a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c72a18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005dfc48`](#insn-005dfc48)

~~~json
{
  "source": "005dfc48",
  "target": "00c66ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66ef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005dfc50`](#insn-005dfc50)

~~~json
{
  "source": "005dfc50",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfc60`](#insn-005dfc60)

~~~json
{
  "source": "005dfc60",
  "target": "005dfe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfc68`](#insn-005dfc68)

~~~json
{
  "source": "005dfc68",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfc74`](#insn-005dfc74)

~~~json
{
  "source": "005dfc74",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c36a0094780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfc78`](#insn-005dfc78)

~~~json
{
  "source": "005dfc78",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfc7c`](#insn-005dfc7c)

~~~json
{
  "source": "005dfc7c",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfc8c`](#insn-005dfc8c)

~~~json
{
  "source": "005dfc8c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfcb0`](#insn-005dfcb0)

~~~json
{
  "source": "005dfcb0",
  "target": "005e0080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfcbc`](#insn-005dfcbc)

~~~json
{
  "source": "005dfcbc",
  "target": "00ca5a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5a38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`005dfcc0`](#insn-005dfcc0)

~~~json
{
  "source": "005dfcc0",
  "target": "005dff40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfcd0`](#insn-005dfcd0)

~~~json
{
  "source": "005dfcd0",
  "target": "00c72a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c72a18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005dfce0`](#insn-005dfce0)

~~~json
{
  "source": "005dfce0",
  "target": "00c66ef8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66ef8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`005dfce8`](#insn-005dfce8)

~~~json
{
  "source": "005dfce8",
  "target": "00c596b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfcf8`](#insn-005dfcf8)

~~~json
{
  "source": "005dfcf8",
  "target": "005dff44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd00`](#insn-005dfd00)

~~~json
{
  "source": "005dfd00",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfd04`](#insn-005dfd04)

~~~json
{
  "source": "005dfd04",
  "target": "0046cd24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfd08`](#insn-005dfd08)

~~~json
{
  "source": "005dfd08",
  "target": "005dfde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd24`](#insn-005dfd24)

~~~json
{
  "source": "005dfd24",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd30`](#insn-005dfd30)

~~~json
{
  "source": "005dfd30",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfd44`](#insn-005dfd44)

~~~json
{
  "source": "005dfd44",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "f4c36a0094780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`005dfd58`](#insn-005dfd58)

~~~json
{
  "source": "005dfd58",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfd80`](#insn-005dfd80)

~~~json
{
  "source": "005dfd80",
  "target": "005e0080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfd8c`](#insn-005dfd8c)

~~~json
{
  "source": "005dfd8c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfdb4`](#insn-005dfdb4)

~~~json
{
  "source": "005dfdb4",
  "target": "005e0080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdd4`](#insn-005dfdd4)

~~~json
{
  "source": "005dfdd4",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfddc`](#insn-005dfddc)

~~~json
{
  "source": "005dfddc",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfde0`](#insn-005dfde0)

~~~json
{
  "source": "005dfde0",
  "target": "0046cde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfdec`](#insn-005dfdec)

~~~json
{
  "source": "005dfdec",
  "target": "005e0080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf8`](#insn-005dfdf8)

~~~json
{
  "source": "005dfdf8",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe04`](#insn-005dfe04)

~~~json
{
  "source": "005dfe04",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe10`](#insn-005dfe10)

~~~json
{
  "source": "005dfe10",
  "target": "005e0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe28`](#insn-005dfe28)

~~~json
{
  "source": "005dfe28",
  "target": "005dfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe30`](#insn-005dfe30)

~~~json
{
  "source": "005dfe30",
  "target": "005dfe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe3c`](#insn-005dfe3c)

~~~json
{
  "source": "005dfe3c",
  "target": "005dfe60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe4c`](#insn-005dfe4c)

~~~json
{
  "source": "005dfe4c",
  "target": "005dfe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe50`](#insn-005dfe50)

~~~json
{
  "source": "005dfe50",
  "target": "005dfec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe58`](#insn-005dfe58)

~~~json
{
  "source": "005dfe58",
  "target": "005dfe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe70`](#insn-005dfe70)

~~~json
{
  "source": "005dfe70",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfea0`](#insn-005dfea0)

~~~json
{
  "source": "005dfea0",
  "target": "005dfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfeb4`](#insn-005dfeb4)

~~~json
{
  "source": "005dfeb4",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfed0`](#insn-005dfed0)

~~~json
{
  "source": "005dfed0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfed4`](#insn-005dfed4)

~~~json
{
  "source": "005dfed4",
  "target": "005df9bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfedc`](#insn-005dfedc)

~~~json
{
  "source": "005dfedc",
  "target": "005e0070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfee8`](#insn-005dfee8)

~~~json
{
  "source": "005dfee8",
  "target": "002c8785",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff00`](#insn-005dff00)

~~~json
{
  "source": "005dff00",
  "target": "005dfac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff04`](#insn-005dff04)

~~~json
{
  "source": "005dff04",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff1c`](#insn-005dff1c)

~~~json
{
  "source": "005dff1c",
  "target": "005dff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff2c`](#insn-005dff2c)

~~~json
{
  "source": "005dff2c",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dff3c`](#insn-005dff3c)

~~~json
{
  "source": "005dff3c",
  "target": "005e006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff54`](#insn-005dff54)

~~~json
{
  "source": "005dff54",
  "target": "005dff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff5c`](#insn-005dff5c)

~~~json
{
  "source": "005dff5c",
  "target": "005dff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff68`](#insn-005dff68)

~~~json
{
  "source": "005dff68",
  "target": "005dff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff78`](#insn-005dff78)

~~~json
{
  "source": "005dff78",
  "target": "005dff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff7c`](#insn-005dff7c)

~~~json
{
  "source": "005dff7c",
  "target": "005dfff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff84`](#insn-005dff84)

~~~json
{
  "source": "005dff84",
  "target": "005dff6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dff9c`](#insn-005dff9c)

~~~json
{
  "source": "005dff9c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dffcc`](#insn-005dffcc)

~~~json
{
  "source": "005dffcc",
  "target": "005dffd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dffe0`](#insn-005dffe0)

~~~json
{
  "source": "005dffe0",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfffc`](#insn-005dfffc)

~~~json
{
  "source": "005dfffc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0000`](#insn-005e0000)

~~~json
{
  "source": "005e0000",
  "target": "005df9bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005e0008`](#insn-005e0008)

~~~json
{
  "source": "005e0008",
  "target": "005e0070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0010`](#insn-005e0010)

~~~json
{
  "source": "005e0010",
  "target": "002c8785",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e002c`](#insn-005e002c)

~~~json
{
  "source": "005e002c",
  "target": "005dfac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005e0030`](#insn-005e0030)

~~~json
{
  "source": "005e0030",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0048`](#insn-005e0048)

~~~json
{
  "source": "005e0048",
  "target": "005e0058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e005c`](#insn-005e005c)

~~~json
{
  "source": "005e005c",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005e006c`](#insn-005e006c)

~~~json
{
  "source": "005e006c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0074`](#insn-005e0074)

~~~json
{
  "source": "005e0074",
  "target": "0046f164",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005e0088`](#insn-005e0088)

~~~json
{
  "source": "005e0088",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0090`](#insn-005e0090)

~~~json
{
  "source": "005e0090",
  "target": "005e00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0094`](#insn-005e0094)

~~~json
{
  "source": "005e0094",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e0098`](#insn-005e0098)

~~~json
{
  "source": "005e0098",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e009c`](#insn-005e009c)

~~~json
{
  "source": "005e009c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e00a0`](#insn-005e00a0)

~~~json
{
  "source": "005e00a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e00a4`](#insn-005e00a4)

~~~json
{
  "source": "005e00a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e00a8`](#insn-005e00a8)

~~~json
{
  "source": "005e00a8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005e00b4`](#insn-005e00b4)

~~~json
{
  "source": "005e00b4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
