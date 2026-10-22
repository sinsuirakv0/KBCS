# 005baabc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](005baabc.md)

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
  "source_sha256": "c63dc34102e85548b0e56d9d670c9da5879542fab32b17c441fe4da4b2a06a25",
  "source_text_sha256": "c63dc34102e85548b0e56d9d670c9da5879542fab32b17c441fe4da4b2a06a25"
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

## 疑似コード 1/1 / UTF-8 9835 bytes

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
      lVar5 = __dynamic_cast(DAT_00c249b8,&PTR_PTR_00be8d98,&PTR_PTR_00bf4450,0);
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
    local_90 = operator_new(0x40);
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
      lVar5 = __dynamic_cast(DAT_00c249b8,&PTR_PTR_00be8d98,&PTR_PTR_00bf4450,0);
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
    local_90 = operator_new(0x40);
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
