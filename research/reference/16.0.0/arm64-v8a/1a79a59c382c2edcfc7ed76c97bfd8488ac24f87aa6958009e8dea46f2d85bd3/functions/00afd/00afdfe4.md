# 00afdfe4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afdfe4",
  "name": "FUN_00afdfe4",
  "size": 1756,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d568da2dd08dc66494d2b86f87d2dd7062cdbf8af16e6470f11eb27758ea22d6",
  "source_text_sha256": "d568da2dd08dc66494d2b86f87d2dd7062cdbf8af16e6470f11eb27758ea22d6"
}
~~~

## 呼び出し元

- [005bc78c](../005bc/005bc78c.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [00689c7c](../00689/00689c7c.md)
- [007bbbec](../007bb/007bbbec.md)
- [007bbc70](../007bb/007bbc70.md)
- [007efb3c](../007ef/007efb3c.md)
- [00801d4c](../00801/00801d4c.md)
- [00802678](../00802/00802678.md)
- [00802b18](../00802/00802b18.md)
- [00802ea0](../00802/00802ea0.md)
- [008514b8](../00851/008514b8.md)
- [008c2ce0](../008c2/008c2ce0.md)
- [00a64340](../00a64/00a64340.md)
- [00ab9080](../00ab9/00ab9080.md)
- [00ab92d4](../00ab9/00ab92d4.md)
- [00afe6c0](../00afe/00afe6c0.md)

## 疑似コード / UTF-8 6987 bytes

~~~c

ulong FUN_00afdfe4(int param_1,int param_2,int param_3,uint param_4,int param_5)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  ulong uVar7;
  long lVar8;
  ulong uVar9;
  undefined8 uVar11;
  long lVar12;
  uint uVar13;
  uleb128 *puVar10;
  
  lVar6 = FUN_008514b8();
  uVar7 = FUN_005e73e0(lVar6 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar7 & 1) != 0) {
    if ((int)param_4 < 1) {
      lVar6 = 0;
    }
    else {
      lVar6 = FUN_008514b8();
      lVar6 = (long)*(int *)(lVar6 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6d0)
              * 100;
      if (param_4 != 1) {
        uVar13 = 1;
        do {
          FUN_008514b8();
          if (uVar13 < 200) {
            lVar8 = FUN_008514b8();
            iVar4 = *(int *)(lVar8 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6d0);
            lVar8 = FUN_008514b8();
            lVar6 = lVar6 + (long)*(int *)(&DAT_00454bb4 +
                                          lVar8 + (long)param_2 * 0x50 +
                                          (ulong)((uVar13 & 0xff) / 10) * 4) * (long)iVar4;
          }
          uVar13 = uVar13 + 1;
        } while (param_4 != uVar13);
      }
      lVar6 = (lVar6 + 0x32) / 100;
    }
    lVar8 = FUN_008514b8();
    iVar4 = FUN_00ab9080(&uleb128_0029a6e0 + lVar8,9);
    lVar8 = FUN_008514b8();
    iVar5 = FUN_008c2ce0(&DAT_0044dd00 + lVar8,1,param_2);
    uVar7 = (((lVar6 * iVar4) / 100 + lVar6) * (long)(iVar5 + 100)) / 100;
    iVar4 = FUN_00afe6c0(param_1,param_2,param_3,0x20,0);
    if (1 < param_3) {
      iVar5 = FUN_00802678(0);
      if (iVar5 == 0) {
LAB_00afe25c:
        uVar11 = 9;
      }
      else {
        FUN_008514b8();
        uVar9 = FUN_007bbbec();
        if ((uVar9 & 1) != 0) goto LAB_00afe25c;
        iVar5 = FUN_00802678(0);
        if (iVar5 != -9) {
          FUN_008514b8();
          uVar9 = FUN_007bbc70();
          if ((uVar9 & 1) == 0) {
            FUN_008514b8();
            uVar9 = FUN_007efb3c();
            if ((uVar9 & 1) == 0) goto LAB_00afe640;
          }
        }
        uVar11 = 0x10;
      }
      lVar6 = FUN_008514b8();
      iVar5 = FUN_00689c7c(lVar6 + 0x1648,param_2,uVar11,0,0);
      iVar4 = iVar5 + iVar4;
    }
LAB_00afe640:
    if (0 < iVar4) {
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    iVar4 = FUN_00afe6c0(param_1,param_2,param_3,0x47,0);
    if (0 < iVar4) {
      uVar7 = (long)(uVar7 * (iVar4 + 100)) / 100;
    }
    goto LAB_00afe69c;
  }
  lVar6 = FUN_008514b8();
  if ((*(int *)((long)&fde_table_entry_00333970.data_loc + lVar6) < 3) &&
     (lVar6 = FUN_008514b8(),
     (*(byte *)((long)&fde_table_entry_003380e8.initial_loc + lVar6) & 1) == 0)) {
    lVar8 = FUN_008514b8();
    lVar6 = (long)param_2 + 2;
    iVar4 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x17f8);
    lVar8 = FUN_008514b8();
    lVar12 = ((long)*(int *)(PTR_DAT_00c9b270 +
                            (long)*(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) * 4) +
             10) * (long)iVar4 + 5;
    lVar8 = SUB168(SEXT816(lVar12) * SEXT816(0x6666666666666667),8);
    lVar12 = lVar12 / 10 + (lVar12 >> 0x3f);
LAB_00afe33c:
    uVar7 = lVar12 - (lVar8 >> 0x3f);
  }
  else {
    lVar6 = FUN_008514b8();
    iVar4 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar6);
    lVar8 = FUN_008514b8();
    lVar6 = (long)param_2 + 2;
    iVar5 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x17f8);
    lVar8 = FUN_008514b8();
    iVar1 = FUN_00a64340(*(long *)(lVar8 + 0x9f6b8) + (long)param_5 * 0x38);
    uVar7 = ((long)iVar5 * (long)iVar1 + 0x32) / 100;
    if (iVar4 == 3) {
      lVar8 = FUN_008514b8();
      uVar2 = FUN_00802b18(0);
      uVar3 = FUN_00802ea0();
      iVar4 = FUN_00801d4c((long)&fde_table_entry_00337310.initial_loc + lVar8,uVar2,uVar3);
      lVar12 = uVar7 * (long)iVar4;
      lVar8 = SUB168(SEXT816(lVar12) * ZEXT816(0xa3d70a3d70a3d70b),8);
      lVar12 = lVar12 / 100 + (lVar12 >> 0x3f);
      goto LAB_00afe33c;
    }
  }
  lVar8 = FUN_008514b8();
  uVar9 = FUN_005e73e0(lVar8 + 0x2958);
  lVar8 = FUN_008514b8();
  if ((uVar9 & 1) == 0) {
    if (*(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x1840) == 0) goto LAB_00afe3c0;
LAB_00afe390:
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) != 0))
    goto LAB_00afe3c0;
    lVar6 = FUN_008514b8();
    iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x10);
    lVar6 = FUN_008514b8();
    puVar10 = &uleb128_0029a6e0 + lVar6;
    uVar11 = 0x10;
  }
  else {
    if (*(int *)(lVar8 + lVar6 * 0x770 + 0x9f724) != 0) goto LAB_00afe390;
LAB_00afe3c0:
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    lVar8 = FUN_008514b8();
    if ((uVar9 & 1) == 0) {
      iVar4 = *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x1840);
    }
    else {
      iVar4 = *(int *)(lVar8 + lVar6 * 0x770 + 0x9f724);
    }
    if (iVar4 != 0) {
      lVar8 = FUN_008514b8();
      uVar9 = FUN_005e73e0(lVar8 + 0x2958);
      if (((uVar9 & 1) == 0) &&
         (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 1)
         ) {
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x12);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x12;
        goto LAB_00afe5b8;
      }
    }
    lVar8 = FUN_008514b8();
    uVar9 = FUN_005e73e0(lVar8 + 0x2958);
    if (((uVar9 & 1) == 0) &&
       (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 2))
    {
      lVar6 = FUN_008514b8();
      iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x16);
      lVar6 = FUN_008514b8();
      puVar10 = &uleb128_0029a6e0 + lVar6;
      uVar11 = 0x16;
    }
    else {
      lVar8 = FUN_008514b8();
      uVar9 = FUN_005e73e0(lVar8 + 0x2958);
      if (((uVar9 & 1) == 0) &&
         (lVar8 = FUN_008514b8(), *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) == 3)
         ) {
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x17);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x17;
      }
      else {
        lVar8 = FUN_008514b8();
        uVar9 = FUN_005e73e0(lVar8 + 0x2958);
        if (((uVar9 & 1) != 0) ||
           (lVar8 = FUN_008514b8(),
           *(int *)((long)__DT_JMPREL + lVar8 + lVar6 * 0x1c4 + 0x190c) != 4)) goto LAB_00afe69c;
        lVar6 = FUN_008514b8();
        iVar4 = FUN_00ab92d4(&uleb128_0029a6e0 + lVar6,0x18);
        lVar6 = FUN_008514b8();
        puVar10 = &uleb128_0029a6e0 + lVar6;
        uVar11 = 0x18;
      }
    }
  }
LAB_00afe5b8:
  iVar5 = FUN_00ab9080(puVar10,uVar11);
  uVar7 = (long)(uVar7 * (long)(iVar4 - iVar5)) / 100 + uVar7;
LAB_00afe69c:
  return uVar7 & 0xffffffff;
}

~~~
