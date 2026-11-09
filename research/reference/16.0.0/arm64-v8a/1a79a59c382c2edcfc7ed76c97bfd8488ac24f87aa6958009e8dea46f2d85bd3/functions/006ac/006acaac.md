# 006acaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "006acaac",
  "name": "FUN_006acaac",
  "size": 1136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35cfd09fdffe131baaa881c3199bc1a7cde624f1fdfe13ecc81ff8f27fb7d64a",
  "source_text_sha256": "35cfd09fdffe131baaa881c3199bc1a7cde624f1fdfe13ecc81ff8f27fb7d64a"
}
~~~

## 呼び出し元

- [00996ea0](../00996/00996ea0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467ab0](../00467/00467ab0.md)
- [00467aec](../00467/00467aec.md)
- [00467f14](../00467/00467f14.md)
- [00468878](../00468/00468878.md)
- [00469bc4](../00469/00469bc4.md)
- [0046bd14](../0046b/0046bd14.md)
- [0046c984](../0046c/0046c984.md)
- [0046ca44](../0046c/0046ca44.md)
- [0046e6ec](../0046e/0046e6ec.md)
- [0046e76c](../0046e/0046e76c.md)
- [0046e774](../0046e/0046e774.md)
- [0046e77c](../0046e/0046e77c.md)
- [00470074](../00470/00470074.md)
- [004700ec](../00470/004700ec.md)
- [006acf1c](../006ac/006acf1c.md)
- [006ad3d4](../006ad/006ad3d4.md)
- [006c115c](../006c1/006c115c.md)
- [008514b8](../00851/008514b8.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58210](../00c58/00c58210.md)

## 疑似コード / UTF-8 6866 bytes

~~~c

void FUN_006acaac(char *param_1)

{
  byte *pbVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  undefined8 uVar9;
  long lVar10;
  char *pcVar11;
  undefined8 uVar12;
  int local_70;
  int iStack_6c;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  if (DAT_00ca4578 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c70dc0,0);
  }
  uVar9 = FUN_00467820();
  if (*param_1 == '\0') goto LAB_006acee8;
  if ((param_1[0x4e0] & 1U) == 0) {
    uVar12 = *(undefined8 *)(param_1 + 0x208);
                    /* try { // try from 006acb2c to 007acb33 has its CatchHandler @ 006acda8 */
    FUN_008514b8();
    uVar3 = FUN_0046c984();
    FUN_008514b8();
    uVar4 = FUN_0046ca44();
                    /* try { // try from 006acb54 to 007acb7f has its CatchHandler @ 006acdb0 */
    uVar5 = 0x62;
    if (*(int *)(param_1 + 0x4e8) != 3) {
      uVar5 = 2;
    }
    FUN_00469bc4(uVar9,uVar12,0,0,uVar3,uVar4,uVar5);
    iVar6 = *(int *)(param_1 + 0x4ec);
    if (iVar6 == 1) {
                    /* try { // try from 006acb80 to 007acbf7 has its CatchHandler @ 006aca04 */
      FUN_00467ab0(uVar9,1);
      FUN_00467aec(uVar9,0xab,0x2c,0,0x40);
      lVar10 = FUN_008514b8();
      iVar6 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar10);
      FUN_008514b8();
      uVar5 = FUN_0046c984();
      FUN_008514b8();
      uVar3 = FUN_0046ca44();
      FUN_00467f14(uVar9,0,-iVar6,uVar5,uVar3);
      FUN_00467aec(uVar9,0xff,0xff,0xff,0xff);
                    /* try { // try from 006acbf8 to 007acbff has its CatchHandler @ 006acd38 */
      FUN_00467ab0(uVar9,0);
                    /* try { // try from 006acc04 to 007acc0b has its CatchHandler @ 006acd88 */
      iVar6 = *(int *)(param_1 + 0x4ec);
    }
    FUN_00470074(param_1 + (long)iVar6 * 0xa8 + 0x38,param_1 + (long)iVar6 * 0x38 + 0x188,
                 *(undefined4 *)(param_1 + 0x4f4),0);
    FUN_004700ec(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,0);
    uVar12 = FUN_0046e76c();
    iVar6 = *(int *)(param_1 + 0x4ec);
                    /* try { // try from 006acc48 to 007acc4f has its CatchHandler @ 006acd18 */
    FUN_004700ec(param_1 + (long)iVar6 * 0xa8 + 0x38,1);
    uVar5 = FUN_0046e774();
                    /* try { // try from 006acc5c to 007acc6b has its CatchHandler @ 006acd50 */
                    /* try { // try from 006acc6c to 007acdef has its CatchHandler @ 006aca04 */
    FUN_004700ec(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,1);
    uVar3 = FUN_0046e77c();
    FUN_0046e6ec(uVar12,param_1 + (long)iVar6 * 0xa8 + 0x38,uVar5,uVar3,&local_70);
    FUN_008514b8();
    iVar6 = FUN_0046c984();
    if (iVar6 < 0) {
      iVar6 = iVar6 + 1;
    }
    lVar10 = FUN_008514b8();
    lVar10 = lVar10 + (long)*(int *)(param_1 + 0x4e4) * 0x100;
    pbVar1 = (byte *)(lVar10 + 0x4b278 +
                     (long)(*(int *)(param_1 + 0x4e8) + *(int *)(param_1 + 0x4ec) + 0x33) * 4);
                    /* catch() { ... } // from try @ 006acc48 with catch @ 006acd18 */
    FUN_0046bd14(uVar9,param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,
                 (iVar6 >> 1) - local_70,
                 ((uint)CONCAT12(*(byte *)(lVar10 + 0x4b376) ^ pbVar1[2],
                                 CONCAT11(*(byte *)(lVar10 + 0x4b375) ^ pbVar1[1],
                                          *(byte *)(lVar10 + 0x4b374) ^ *pbVar1)) - iStack_6c) +
                 (uint)(*(byte *)(lVar10 + 0x4b377) ^ pbVar1[3]) * 0x1000000 + 0x1d4);
    iVar6 = *(int *)(param_1 + 0x4f0);
    if (iVar6 < 3) {
      if (iVar6 == 1) {
                    /* try { // try from 006ace80 to 007acf53 has its CatchHandler @ 006ace80
                       catch() { ... } // from try @ 006ace80 with catch @ 006ace80
                       catch() { ... } // from try @ 006acf80 with catch @ 006ace80
                       catch() { ... } // from try @ 006ad0a8 with catch @ 006ace80 */
        FUN_00470074(param_1 + 0x268,param_1 + 0x310,*(undefined4 *)(param_1 + 0x4f8),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        pcVar11 = param_1 + 0x268;
      }
      else {
                    /* catch() { ... } // from try @ 006acbf8 with catch @ 006acd38 */
        if (iVar6 != 2) goto LAB_006acecc;
                    /* catch() { ... } // from try @ 006acc5c with catch @ 006acd50 */
        FUN_00470074(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        pcVar11 = param_1 + 0x380;
      }
      if (iVar7 < 0) {
        iVar7 = iVar7 + 1;
      }
      FUN_0046bd14(uVar9,pcVar11,iVar6 >> 1,iVar7 >> 1);
    }
    else {
                    /* catch() { ... } // from try @ 006acc04 with catch @ 006acd88 */
      if ((iVar6 == 3) || (iVar6 == 4)) {
        FUN_00470074(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
                    /* catch() { ... } // from try @ 006acb2c with catch @ 006acda8 */
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
                    /* catch() { ... } // from try @ 006acb54 with catch @ 006acdb0 */
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        if (iVar7 < 0) {
          iVar7 = iVar7 + 1;
        }
        FUN_0046bd14(uVar9,param_1 + 0x380,iVar6 >> 1,iVar7 >> 1);
        FUN_006c115c(param_1 + 0x460);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469bc4(uVar9,uVar12,(iVar6 >> 1) + -0xd7,0x1f8,0xdc,0x3e,1);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469bc4(uVar9,uVar12,iVar6 >> 1,0x1f8,0xdc,0x3e,2);
        uVar12 = *(undefined8 *)(param_1 + 0x1f8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00468878(uVar9,uVar12,iVar6 >> 1,0x217,0x1a4,5);
      }
    }
LAB_006acecc:
    FUN_006acf1c();
  }
  if ((*(uint *)(param_1 + 0x4f0) | 4) == 4) {
    FUN_006ad3d4(param_1);
  }
LAB_006acee8:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
