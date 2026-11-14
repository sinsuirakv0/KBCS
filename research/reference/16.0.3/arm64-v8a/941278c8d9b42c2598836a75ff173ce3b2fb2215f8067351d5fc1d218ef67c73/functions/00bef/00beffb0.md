# 00beffb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00beffb0",
  "name": "FUN_00beffb0",
  "size": 1052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02ceca23a4c1f4809972bbd5acd4907f6f39a3fd1a148b2f10f3d925d5eb7712",
  "source_text_sha256": "02ceca23a4c1f4809972bbd5acd4907f6f39a3fd1a148b2f10f3d925d5eb7712"
}
~~~

## 呼び出し元

- [00be96e8](../00be9/00be96e8.md)

## 呼び出し先

- [00bf03cc](../00bf0/00bf03cc.md)
- [00c54458](../00c54/00c54458.md)

## 疑似コード / UTF-8 7856 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

bool FUN_00beffb0(undefined8 *param_1,undefined8 *param_2)

{
  long lVar1;
  int iVar2;
  int iVar3;
  ulong uVar4;
  undefined8 *puVar5;
  long lVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long lVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  undefined8 uVar17;
  undefined8 uVar18;
  undefined8 local_50;
  undefined8 uStack_48;
  
  uVar4 = (long)param_2 - (long)param_1 >> 4;
  if ((long)uVar4 < 3) {
    if (uVar4 < 2) {
      return true;
    }
    if (uVar4 == 2) {
      uVar13 = param_2[-1];
      uVar11 = param_2[-2];
      uVar17 = param_1[1];
      uVar14 = *param_1;
      iVar2 = FUN_00c54458();
      if (-1 < iVar2) {
        return true;
      }
      param_1[1] = uVar13;
      *param_1 = uVar11;
LAB_00bf0394:
      param_2[-1] = uVar17;
      param_2[-2] = uVar14;
      return true;
    }
  }
  else {
                    /* try { // try from 00bf0024 to 00cf002f has its CatchHandler @ 00bf007c */
    if (uVar4 == 3) {
      uVar17 = param_1[1];
      uVar14 = *param_1;
      uVar13 = param_1[3];
      uVar11 = param_1[2];
      uVar18 = param_2[-1];
      uVar16 = param_2[-2];
      iVar2 = FUN_00c54458();
      if (iVar2 < 0) {
        iVar2 = FUN_00c54458(uVar16,uVar11);
                    /* catch() { ... } // from try @ 00bf0024 with catch @ 00bf007c */
        if (iVar2 < 0) {
          param_1[1] = uVar18;
          *param_1 = uVar16;
        }
        else {
          param_1[1] = uVar13;
          *param_1 = uVar11;
          param_1[3] = uVar17;
          param_1[2] = uVar14;
          uVar13 = param_2[-1];
          uVar11 = param_2[-2];
          iVar2 = FUN_00c54458();
          if (-1 < iVar2) {
            return true;
          }
          param_1[3] = uVar13;
          param_1[2] = uVar11;
        }
        goto LAB_00bf0394;
      }
      iVar2 = FUN_00c54458(uVar16,uVar11);
      if (-1 < iVar2) {
        return true;
      }
      param_1[3] = uVar18;
      param_1[2] = uVar16;
      param_2[-1] = uVar13;
      param_2[-2] = uVar11;
      uVar17 = param_1[1];
      uVar13 = *param_1;
      uVar14 = param_1[3];
      uVar11 = param_1[2];
      iVar2 = FUN_00c54458();
      goto joined_r0x00bf019c;
    }
    if (uVar4 == 4) {
      uVar18 = param_1[1];
      uVar16 = *param_1;
      uVar14 = param_1[3];
      uVar11 = param_1[2];
      puVar5 = param_1 + 2;
      uVar17 = param_1[5];
      uVar13 = param_1[4];
      puVar9 = param_1 + 4;
      iVar2 = FUN_00c54458(uVar11,uVar16);
      puVar7 = param_1;
      local_50 = uVar13;
      uStack_48 = uVar17;
      if (iVar2 < 0) {
        iVar2 = FUN_00c54458(uVar13,uVar11);
        puVar8 = puVar9;
        uVar12 = uVar16;
        uVar15 = uVar18;
        if (-1 < iVar2) {
          param_1[1] = uVar14;
          *param_1 = uVar11;
          param_1[3] = uVar18;
          param_1[2] = uVar16;
          iVar2 = FUN_00c54458(uVar13,uVar16);
          puVar7 = puVar5;
          if (-1 < iVar2) goto LAB_00bf02ec;
        }
LAB_00bf02d0:
                    /* try { // try from 00bf02d4 to 00cf02df has its CatchHandler @ 00bf0774 */
        puVar8[1] = uVar18;
        *puVar8 = uVar16;
        puVar7[1] = uVar17;
        *puVar7 = uVar13;
        local_50 = uVar12;
        uStack_48 = uVar15;
      }
      else {
        iVar2 = FUN_00c54458(uVar13,uVar11);
        if (iVar2 < 0) {
          param_1[5] = uVar14;
          *puVar9 = uVar11;
          param_1[3] = uVar17;
          *puVar5 = uVar13;
          iVar2 = FUN_00c54458(uVar13,uVar16);
          puVar8 = puVar5;
          uVar12 = uVar11;
          uVar15 = uVar14;
          local_50 = uVar11;
          uStack_48 = uVar14;
          if (iVar2 < 0) goto LAB_00bf02d0;
        }
      }
LAB_00bf02ec:
      uVar14 = param_2[-1];
      uVar11 = param_2[-2];
                    /* try { // try from 00bf02f8 to 00cf031b has its CatchHandler @ 00bf07ac */
      iVar2 = FUN_00c54458(uVar11,local_50);
      if (-1 < iVar2) {
        return true;
      }
      param_1[5] = uVar14;
      *puVar9 = uVar11;
      param_2[-1] = uStack_48;
      param_2[-2] = local_50;
      uVar14 = param_1[5];
      uVar11 = *puVar9;
      uVar18 = param_1[3];
      uVar16 = *puVar5;
      iVar2 = FUN_00c54458();
      if (-1 < iVar2) {
        return true;
      }
                    /* try { // try from 00bf0330 to 00cf0337 has its CatchHandler @ 00bf076c */
      uVar17 = param_1[1];
      uVar13 = *param_1;
      param_1[3] = uVar14;
      param_1[2] = uVar11;
      param_1[5] = uVar18;
      param_1[4] = uVar16;
      iVar2 = FUN_00c54458();
                    /* try { // try from 00bf034c to 00cf03ab has its CatchHandler @ 00bf07fc */
joined_r0x00bf019c:
      if (iVar2 < 0) {
        param_1[1] = uVar14;
        *param_1 = uVar11;
        param_1[3] = uVar17;
        param_1[2] = uVar13;
        return true;
      }
      return true;
    }
                    /* try { // try from 00bf0030 to 00cf00cb has its CatchHandler @ 00beff88 */
    if (uVar4 == 5) {
      FUN_00bf03cc(param_1,param_1 + 2,param_1 + 4,param_1 + 6,param_2 + -2);
      return true;
    }
  }
  uVar17 = param_1[1];
  uVar13 = *param_1;
  uVar18 = param_1[3];
  uVar16 = param_1[2];
  puVar5 = param_1 + 4;
  uVar14 = param_1[5];
  uVar11 = param_1[4];
  puVar9 = param_1 + 2;
  iVar2 = FUN_00c54458(uVar16);
  puVar7 = param_1;
  if (iVar2 < 0) {
    iVar2 = FUN_00c54458(uVar11,uVar16);
    puVar8 = puVar5;
    if (-1 < iVar2) {
      param_1[1] = uVar18;
      *param_1 = uVar16;
      param_1[3] = uVar17;
      param_1[2] = uVar13;
      iVar2 = FUN_00c54458(uVar11);
      puVar7 = puVar9;
      goto joined_r0x00bf01dc;
    }
  }
  else {
    iVar2 = FUN_00c54458(uVar11,uVar16);
    if (-1 < iVar2) goto LAB_00bf01f0;
    param_1[3] = uVar14;
    *puVar9 = uVar11;
    param_1[5] = uVar18;
    *puVar5 = uVar16;
    iVar2 = FUN_00c54458(uVar11,uVar13);
    puVar8 = puVar9;
joined_r0x00bf01dc:
                    /* try { // try from 00bf01dc to 00cf02d3 has its CatchHandler @ 00bf01dc
                       catch() { ... } // from try @ 00bf01dc with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf03ac with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf05a0 with catch @ 00bf01dc
                       catch() { ... } // from try @ 00bf068c with catch @ 00bf01dc */
    if (-1 < iVar2) goto LAB_00bf01f0;
  }
  puVar7[1] = uVar14;
  *puVar7 = uVar11;
  puVar8[1] = uVar17;
  *puVar8 = uVar13;
LAB_00bf01f0:
  if (param_1 + 6 != param_2) {
    iVar2 = 0;
    lVar10 = 0x30;
    puVar9 = param_1 + 6;
    do {
      uVar13 = puVar9[1];
      uVar11 = *puVar9;
      uVar17 = puVar5[1];
      uVar14 = *puVar5;
      iVar3 = FUN_00c54458();
      lVar6 = lVar10;
      if (iVar3 < 0) {
        do {
          lVar1 = lVar6 + -0x10;
          ((undefined8 *)((long)param_1 + lVar6))[1] = uVar17;
          *(undefined8 *)((long)param_1 + lVar6) = uVar14;
          puVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bf020c;
          uVar17 = *(undefined8 *)((long)param_1 + lVar6 + -0x18);
          uVar14 = *(undefined8 *)((long)param_1 + lVar6 + -0x20);
          iVar3 = FUN_00c54458(uVar11);
          lVar6 = lVar1;
        } while (iVar3 < 0);
        puVar5 = (undefined8 *)((long)param_1 + lVar1);
LAB_00bf020c:
        iVar2 = iVar2 + 1;
        puVar5[1] = uVar13;
        *puVar5 = uVar11;
        if (iVar2 == 8) {
          return puVar9 + 2 == param_2;
        }
      }
      puVar7 = puVar9 + 2;
      lVar10 = lVar10 + 0x10;
      puVar5 = puVar9;
      puVar9 = puVar7;
    } while (puVar7 != param_2);
  }
                    /* try { // try from 00bf03ac to 00cf0517 has its CatchHandler @ 00bf01dc */
  return true;
}

~~~
