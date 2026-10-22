# 007febdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007febdc.md)

## 関数情報

~~~json
{
  "address": "007febdc",
  "name": "FUN_007febdc",
  "size": 1340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97783c166f4a6cfbefa4b50c73bf0de7a562c68389360f8d1991474c7313e865",
  "source_text_sha256": "97783c166f4a6cfbefa4b50c73bf0de7a562c68389360f8d1991474c7313e865"
}
~~~
## 呼び出し元

- [007fe2f0](../007fe/007fe2f0.md)
- [007febdc](../007fe/007febdc.md)

## 呼び出し先

- [007fc484](../007fc/007fc484.md)
- [007fe674](../007fe/007fe674.md)
- [007febdc](../007fe/007febdc.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)

## 疑似コード 1/1 / UTF-8 10170 bytes

~~~c

void FUN_007febdc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                 long param_5,long param_6,undefined8 *param_7,long param_8)

{
  long lVar1;
  long lVar2;
  bool bVar3;
  ulong uVar4;
  ulong uVar5;
  ulong uVar6;
  undefined1 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  long lVar13;
  undefined8 *puVar14;
  undefined8 *puVar15;
  ulong uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 *local_110;
  long local_100;
  undefined8 local_f8;
  undefined8 local_f0;
  undefined8 uStack_e8;
  undefined4 local_e0;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined4 local_c0;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined4 local_a0;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined4 local_80;
  long local_70;
  
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  local_110 = param_3;
  local_100 = param_6;
  if (param_6 != 0) {
    while ((param_8 < local_100 && (param_8 < param_5))) {
      if (param_5 == 0) goto LAB_007ff0e4;
      lVar9 = 0;
      lVar13 = -param_5;
      while( true ) {
        uStack_c8 = param_2[1];
        local_d0 = *param_2;
        local_c0 = *(undefined4 *)(param_2 + 2);
        puVar11 = (undefined8 *)((long)param_1 + lVar9);
        uStack_e8 = puVar11[1];
        local_f0 = *puVar11;
        local_e0 = *(undefined4 *)(puVar11 + 2);
        uVar4 = FUN_007fe674(param_4,&local_d0,&local_f0);
        if ((uVar4 & 1) != 0) break;
        bVar3 = lVar13 == -1;
        lVar13 = lVar13 + 1;
        lVar9 = lVar9 + 0x14;
        if (bVar3) goto LAB_007ff0e4;
      }
      param_5 = -lVar13;
      if (param_5 < local_100) {
        lVar8 = local_100;
        if (local_100 < 0) {
          lVar8 = local_100 + 1;
        }
        lVar8 = lVar8 >> 1;
        puVar15 = (undefined8 *)((long)param_2 + lVar8 * 0x14);
        lVar1 = (long)param_2 + (-lVar9 - (long)param_1);
        puVar10 = param_2;
        if (lVar1 != 0) {
          uVar4 = (lVar1 >> 2) * -0x3333333333333333;
          puVar10 = puVar11;
          do {
            uVar16 = uVar4 >> 1;
            uStack_88 = puVar15[1];
            local_90 = *puVar15;
            local_80 = *(undefined4 *)(puVar15 + 2);
            puVar12 = (undefined8 *)((long)puVar10 + uVar16 * 0x14);
            uStack_a8 = puVar12[1];
            local_b0 = *puVar12;
            local_a0 = *(undefined4 *)(puVar12 + 2);
            uVar5 = FUN_007fe674(param_4,&local_90,&local_b0);
            uVar6 = uVar4 + ~uVar16;
            uVar4 = uVar16;
            if ((uVar5 & 1) == 0) {
              uVar4 = uVar6;
              puVar10 = (undefined8 *)((long)puVar12 + 0x14);
            }
          } while (uVar4 != 0);
        }
        param_5 = ((long)puVar10 + (-lVar9 - (long)param_1) >> 2) * -0x3333333333333333;
      }
      else {
        if (lVar13 == -1) {
          param_1 = (undefined8 *)((long)param_1 + lVar9);
          uVar18 = param_2[1];
          uVar17 = *param_2;
          local_80 = *(undefined4 *)(param_1 + 2);
          uStack_88 = param_1[1];
          local_90 = *param_1;
                    /* try { // try from 007ff078 to 008ff083 has its CatchHandler @ 007ff7e0 */
          *(undefined1 *)(param_1 + 2) = *(undefined1 *)(param_2 + 2);
          param_1[1] = uVar18;
          *param_1 = uVar17;
          param_2[1] = uStack_88;
          *param_2 = local_90;
          *(undefined1 *)(param_2 + 2) = (undefined1)local_80;
          goto LAB_007ff0e4;
        }
        if (param_5 < 0) {
          param_5 = param_5 + 1;
        }
        param_5 = param_5 >> 1;
        local_f8 = *param_4;
        puVar10 = (undefined8 *)((long)param_1 + lVar9 + param_5 * 0x14);
        puVar15 = param_2;
        if (param_2 != local_110) {
          uVar4 = ((long)local_110 - (long)param_2 >> 2) * -0x3333333333333333;
          do {
            uVar5 = uVar4 >> 1;
            puVar12 = (undefined8 *)((long)puVar15 + uVar5 * 0x14);
            local_80 = *(undefined4 *)(puVar12 + 2);
            uStack_88 = puVar12[1];
            local_90 = *puVar12;
            local_a0 = *(undefined4 *)(puVar10 + 2);
            uStack_a8 = puVar10[1];
            local_b0 = *puVar10;
            uVar6 = FUN_007fe674(&local_f8,&local_90,&local_b0);
            uVar4 = uVar4 + ~uVar5;
            puVar12 = (undefined8 *)((long)puVar12 + 0x14);
            if ((uVar6 & 1) == 0) {
              uVar4 = uVar5;
              puVar12 = puVar15;
            }
            puVar15 = puVar12;
          } while (uVar4 != 0);
        }
        lVar8 = ((long)puVar15 - (long)param_2 >> 2) * -0x3333333333333333;
      }
      puVar12 = (undefined8 *)FUN_007fc484(puVar10,param_2,puVar15);
      if (param_5 + lVar8 < (local_100 - (param_5 + lVar8)) - lVar13) {
        FUN_007febdc((long)param_1 + lVar9,puVar10,puVar12,param_4,param_5,lVar8,param_7,param_8);
        puVar10 = puVar15;
        puVar11 = puVar12;
        lVar8 = local_100 - lVar8;
        param_5 = -lVar13 - param_5;
      }
      else {
        FUN_007febdc(puVar12,puVar15,local_110,param_4,-lVar13 - param_5,local_100 - lVar8,param_7,
                     param_8);
        local_110 = puVar12;
      }
      param_2 = puVar10;
      param_1 = puVar11;
      local_100 = lVar8;
      if (lVar8 == 0) goto LAB_007ff0e4;
    }
    if (local_100 < param_5) {
      if (local_110 != param_2) {
        lVar13 = 0;
        do {
          puVar11 = (undefined8 *)((long)param_2 + lVar13);
          puVar10 = (undefined8 *)((long)param_7 + lVar13);
          lVar13 = lVar13 + 0x14;
          uVar18 = puVar11[1];
          uVar17 = *puVar11;
          *(undefined4 *)(puVar10 + 2) = *(undefined4 *)(puVar11 + 2);
          puVar10[1] = uVar18;
          *puVar10 = uVar17;
        } while ((undefined8 *)((long)param_2 + lVar13) != local_110);
        puVar11 = (undefined8 *)((long)param_7 + lVar13);
        while (puVar10 = (undefined8 *)((long)local_110 + -0x14), param_2 != param_1) {
          local_80 = *(undefined4 *)((long)puVar11 + -4);
          uStack_88 = *(undefined8 *)((long)puVar11 + -0xc);
          local_90 = *(undefined8 *)((long)puVar11 + -0x14);
          puVar14 = (undefined8 *)((long)puVar11 + -0x14);
          local_a0 = *(undefined4 *)((long)param_2 + -4);
          uStack_a8 = *(undefined8 *)((long)param_2 + -0xc);
          local_b0 = *(undefined8 *)((long)param_2 + -0x14);
          uVar4 = FUN_007fe674(param_4,&local_90,&local_b0);
          puVar15 = (undefined8 *)((long)param_2 + -0x14);
          puVar12 = (undefined8 *)((long)param_2 + -0x14);
          if ((uVar4 & 1) == 0) {
            puVar15 = param_2;
            puVar11 = puVar14;
            puVar12 = puVar14;
          }
          uVar18 = puVar12[1];
          uVar17 = *puVar12;
          *(undefined1 *)((long)local_110 + -4) = *(undefined1 *)(puVar12 + 2);
          *(undefined8 *)((long)local_110 + -0xc) = uVar18;
          *puVar10 = uVar17;
          param_2 = puVar15;
          local_110 = puVar10;
          if (puVar11 == param_7) goto LAB_007ff0e4;
        }
        lVar13 = 0;
        do {
          puVar15 = (undefined8 *)((long)puVar10 + lVar13);
          lVar9 = lVar13 + -0x14;
          uVar18 = *(undefined8 *)((long)puVar11 + lVar13 + -0xc);
          uVar17 = *(undefined8 *)((long)puVar11 + lVar13 + -0x14);
          *(undefined1 *)(puVar15 + 2) = *(undefined1 *)((long)puVar11 + lVar13 + -4);
          puVar15[1] = uVar18;
          *puVar15 = uVar17;
          lVar13 = lVar9;
        } while ((undefined8 *)((long)puVar11 + lVar9) != param_7);
      }
      goto LAB_007ff0e4;
    }
    if (param_1 == param_2) goto LAB_007ff0e4;
                    /* catch() { ... } // from try @ 007ff140 with catch @ 007fefc8
                       catch() { ... } // from try @ 007ff500 with catch @ 007fefc8
                       catch() { ... } // from try @ 007ff6e4 with catch @ 007fefc8 */
    lVar13 = 0;
    do {
      puVar11 = (undefined8 *)((long)param_1 + lVar13);
      puVar10 = (undefined8 *)((long)param_7 + lVar13);
      lVar13 = lVar13 + 0x14;
      uVar18 = puVar11[1];
      uVar17 = *puVar11;
      *(undefined4 *)(puVar10 + 2) = *(undefined4 *)(puVar11 + 2);
      puVar10[1] = uVar18;
      *puVar10 = uVar17;
    } while ((undefined8 *)((long)param_1 + lVar13) != param_2);
    puVar11 = param_7;
    do {
      if (param_2 == local_110) {
                    /* try { // try from 007ff0dc to 008ff13f has its CatchHandler @ 007ff7f8 */
        memmove(param_1,puVar11,(long)param_7 + (lVar13 - (long)puVar11) + -3);
        break;
      }
      local_80 = *(undefined4 *)(param_2 + 2);
      uStack_88 = param_2[1];
      local_90 = *param_2;
                    /* try { // try from 007ff030 to 008ff033 has its CatchHandler @ 007ff7e4 */
                    /* try { // try from 007ff03c to 008ff077 has its CatchHandler @ 007ff7f0 */
      local_a0 = *(undefined4 *)(puVar11 + 2);
      uStack_a8 = puVar11[1];
      local_b0 = *puVar11;
      uVar4 = FUN_007fe674(param_4,&local_90,&local_b0);
      if ((uVar4 & 1) == 0) {
        uVar7 = *(undefined1 *)(puVar11 + 2);
        puVar10 = (undefined8 *)((long)puVar11 + 0x14);
        uVar18 = puVar11[1];
        uVar17 = *puVar11;
      }
      else {
        uVar7 = *(undefined1 *)(param_2 + 2);
        uVar18 = param_2[1];
        uVar17 = *param_2;
        puVar10 = puVar11;
        param_2 = (undefined8 *)((long)param_2 + 0x14);
      }
      *(undefined1 *)(param_1 + 2) = uVar7;
      param_1[1] = uVar18;
      *param_1 = uVar17;
      param_1 = (undefined8 *)((long)param_1 + 0x14);
      puVar11 = puVar10;
    } while ((undefined8 *)((long)param_7 + lVar13) != puVar10);
  }
LAB_007ff0e4:
  if (*(long *)(lVar2 + 0x28) == local_70) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
