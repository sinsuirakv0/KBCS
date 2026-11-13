# 00beefbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00beefbc",
  "name": "FUN_00beefbc",
  "size": 1052,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "445788f9684eba308d8d0105135e3940b62237923e3326cf5773ece12efeae71",
  "source_text_sha256": "445788f9684eba308d8d0105135e3940b62237923e3326cf5773ece12efeae71"
}
~~~

## 呼び出し元

- [00be86f4](../00be8/00be86f4.md)

## 呼び出し先

- [00bef3d8](../00bef/00bef3d8.md)
- [00c53464](../00c53/00c53464.md)

## 疑似コード / UTF-8 7856 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

bool FUN_00beefbc(undefined8 *param_1,undefined8 *param_2)

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
      iVar2 = FUN_00c53464();
      if (-1 < iVar2) {
        return true;
      }
      param_1[1] = uVar13;
      *param_1 = uVar11;
LAB_00bef3a0:
      param_2[-1] = uVar17;
      param_2[-2] = uVar14;
      return true;
    }
  }
  else {
                    /* try { // try from 00bef030 to 00cef03b has its CatchHandler @ 00bef088 */
    if (uVar4 == 3) {
      uVar17 = param_1[1];
      uVar14 = *param_1;
      uVar13 = param_1[3];
      uVar11 = param_1[2];
      uVar18 = param_2[-1];
      uVar16 = param_2[-2];
      iVar2 = FUN_00c53464();
      if (iVar2 < 0) {
        iVar2 = FUN_00c53464(uVar16,uVar11);
                    /* catch() { ... } // from try @ 00bef030 with catch @ 00bef088 */
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
          iVar2 = FUN_00c53464();
          if (-1 < iVar2) {
            return true;
          }
          param_1[3] = uVar13;
          param_1[2] = uVar11;
        }
        goto LAB_00bef3a0;
      }
      iVar2 = FUN_00c53464(uVar16,uVar11);
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
      iVar2 = FUN_00c53464();
      goto joined_r0x00bef1a8;
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
      iVar2 = FUN_00c53464(uVar11,uVar16);
      puVar7 = param_1;
      local_50 = uVar13;
      uStack_48 = uVar17;
      if (iVar2 < 0) {
        iVar2 = FUN_00c53464(uVar13,uVar11);
        puVar8 = puVar9;
        uVar12 = uVar16;
        uVar15 = uVar18;
        if (-1 < iVar2) {
          param_1[1] = uVar14;
          *param_1 = uVar11;
          param_1[3] = uVar18;
          param_1[2] = uVar16;
          iVar2 = FUN_00c53464(uVar13,uVar16);
          puVar7 = puVar5;
          if (-1 < iVar2) goto LAB_00bef2f8;
        }
LAB_00bef2dc:
                    /* try { // try from 00bef2e0 to 00cef2eb has its CatchHandler @ 00bef780 */
        puVar8[1] = uVar18;
        *puVar8 = uVar16;
        puVar7[1] = uVar17;
        *puVar7 = uVar13;
        local_50 = uVar12;
        uStack_48 = uVar15;
      }
      else {
        iVar2 = FUN_00c53464(uVar13,uVar11);
        if (iVar2 < 0) {
          param_1[5] = uVar14;
          *puVar9 = uVar11;
          param_1[3] = uVar17;
          *puVar5 = uVar13;
          iVar2 = FUN_00c53464(uVar13,uVar16);
          puVar8 = puVar5;
          uVar12 = uVar11;
          uVar15 = uVar14;
          local_50 = uVar11;
          uStack_48 = uVar14;
          if (iVar2 < 0) goto LAB_00bef2dc;
        }
      }
LAB_00bef2f8:
      uVar14 = param_2[-1];
      uVar11 = param_2[-2];
                    /* try { // try from 00bef304 to 00cef327 has its CatchHandler @ 00bef7b8 */
      iVar2 = FUN_00c53464(uVar11,local_50);
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
      iVar2 = FUN_00c53464();
      if (-1 < iVar2) {
        return true;
      }
                    /* try { // try from 00bef33c to 00cef343 has its CatchHandler @ 00bef778 */
      uVar17 = param_1[1];
      uVar13 = *param_1;
      param_1[3] = uVar14;
      param_1[2] = uVar11;
      param_1[5] = uVar18;
      param_1[4] = uVar16;
      iVar2 = FUN_00c53464();
                    /* try { // try from 00bef358 to 00cef3b7 has its CatchHandler @ 00bef808 */
joined_r0x00bef1a8:
      if (iVar2 < 0) {
        param_1[1] = uVar14;
        *param_1 = uVar11;
        param_1[3] = uVar17;
        param_1[2] = uVar13;
        return true;
      }
      return true;
    }
                    /* try { // try from 00bef03c to 00cef0d7 has its CatchHandler @ 00beef94 */
    if (uVar4 == 5) {
      FUN_00bef3d8(param_1,param_1 + 2,param_1 + 4,param_1 + 6,param_2 + -2);
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
  iVar2 = FUN_00c53464(uVar16);
  puVar7 = param_1;
  if (iVar2 < 0) {
    iVar2 = FUN_00c53464(uVar11,uVar16);
    puVar8 = puVar5;
    if (-1 < iVar2) {
      param_1[1] = uVar18;
      *param_1 = uVar16;
      param_1[3] = uVar17;
      param_1[2] = uVar13;
      iVar2 = FUN_00c53464(uVar11);
      puVar7 = puVar9;
      goto joined_r0x00bef1e8;
    }
  }
  else {
    iVar2 = FUN_00c53464(uVar11,uVar16);
    if (-1 < iVar2) goto LAB_00bef1fc;
    param_1[3] = uVar14;
    *puVar9 = uVar11;
    param_1[5] = uVar18;
    *puVar5 = uVar16;
    iVar2 = FUN_00c53464(uVar11,uVar13);
    puVar8 = puVar9;
joined_r0x00bef1e8:
                    /* try { // try from 00bef1e8 to 00cef2df has its CatchHandler @ 00bef1e8
                       catch() { ... } // from try @ 00bef1e8 with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef3b8 with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef5ac with catch @ 00bef1e8
                       catch() { ... } // from try @ 00bef698 with catch @ 00bef1e8 */
    if (-1 < iVar2) goto LAB_00bef1fc;
  }
  puVar7[1] = uVar14;
  *puVar7 = uVar11;
  puVar8[1] = uVar17;
  *puVar8 = uVar13;
LAB_00bef1fc:
  if (param_1 + 6 != param_2) {
    iVar2 = 0;
    lVar10 = 0x30;
    puVar9 = param_1 + 6;
    do {
      uVar13 = puVar9[1];
      uVar11 = *puVar9;
      uVar17 = puVar5[1];
      uVar14 = *puVar5;
      iVar3 = FUN_00c53464();
      lVar6 = lVar10;
      if (iVar3 < 0) {
        do {
          lVar1 = lVar6 + -0x10;
          ((undefined8 *)((long)param_1 + lVar6))[1] = uVar17;
          *(undefined8 *)((long)param_1 + lVar6) = uVar14;
          puVar5 = param_1;
          if (lVar1 == 0) goto LAB_00bef218;
          uVar17 = *(undefined8 *)((long)param_1 + lVar6 + -0x18);
          uVar14 = *(undefined8 *)((long)param_1 + lVar6 + -0x20);
          iVar3 = FUN_00c53464(uVar11);
          lVar6 = lVar1;
        } while (iVar3 < 0);
        puVar5 = (undefined8 *)((long)param_1 + lVar1);
LAB_00bef218:
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
                    /* try { // try from 00bef3b8 to 00cef523 has its CatchHandler @ 00bef1e8 */
  return true;
}

~~~
