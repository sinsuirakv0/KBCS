# 005dfbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "1d317fb04276940003416c668cf19ea244d4d01814ca827f87bc7fcc1f907609"
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
