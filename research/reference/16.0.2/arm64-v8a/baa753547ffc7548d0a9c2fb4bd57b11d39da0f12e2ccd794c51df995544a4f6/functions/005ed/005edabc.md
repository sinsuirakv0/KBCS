# 005edabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "005edabc",
  "name": "FUN_005edabc",
  "size": 2900,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "982240f91f06f407dc93a8c8dbebff254bcfebbaccc35a1d065f18de42530cac",
  "source_text_sha256": "982240f91f06f407dc93a8c8dbebff254bcfebbaccc35a1d065f18de42530cac"
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [00442970](../00442/00442970.md)
- [004678a0](../00467/004678a0.md)
- [00467b30](../00467/00467b30.md)
- [00467b6c](../00467/00467b6c.md)
- [00467f5c](../00467/00467f5c.md)
- [00467f94](../00467/00467f94.md)
- [00468c1c](../00468/00468c1c.md)
- [00468fc8](../00468/00468fc8.md)
- [00469c44](../00469/00469c44.md)
- [0046bba8](../0046b/0046bba8.md)
- [0046bd94](../0046b/0046bd94.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046d9b4](../0046d/0046d9b4.md)
- [0046e578](../0046e/0046e578.md)
- [0046e7d0](../0046e/0046e7d0.md)
- [0046e7d8](../0046e/0046e7d8.md)
- [0046e7e0](../0046e/0046e7e0.md)
- [0046f6ac](../0046f/0046f6ac.md)
- [0046f724](../0046f/0046f724.md)
- [004700f4](../00470/004700f4.md)
- [00470120](../00470/00470120.md)
- [0047017c](../00470/0047017c.md)
- [00470184](../00470/00470184.md)
- [0047018c](../00470/0047018c.md)
- [00489f8c](../00489/00489f8c.md)
- [005df114](../005df/005df114.md)
- [005df60c](../005df/005df60c.md)
- [005f01ec](../005f0/005f01ec.md)
- [005f0c10](../005f0/005f0c10.md)
- [005f0d90](../005f0/005f0d90.md)
- [00a64b08](../00a64/00a64b08.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 22137 bytes

~~~c

void FUN_005edabc(long param_1)

{
  int *piVar1;
  uint uVar2;
  uint uVar3;
  uint uVar4;
  long lVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  int iVar10;
  int iVar11;
  int iVar12;
  undefined8 uVar13;
  long lVar14;
  undefined4 uVar15;
  long *plVar16;
  undefined4 uVar17;
  long lVar18;
  ulong uVar19;
  undefined4 uVar20;
  long lVar21;
  undefined4 *puVar22;
  long lVar23;
  undefined8 uVar24;
  ulong uVar25;
  float fVar26;
  float fVar27;
  long local_a8;
  undefined8 local_90;
  long *local_88;
  undefined1 auStack_80 [8];
  long local_78;
  
                    /* try { // try from 005edad8 to 006edb33 has its CatchHandler @ 005ecd50 */
                    /* catch() { ... } // from try @ 005edaa0 with catch @ 005edadc */
  lVar5 = tpidr_el0;
  local_78 = *(long *)(lVar5 + 0x28);
  if (DAT_00ca4a78 == 0) {
    local_a8 = 0;
  }
  else {
                    /* catch() { ... } // from try @ 005eda70 with catch @ 005edb10 */
    local_a8 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                              &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c71a48,0);
  }
  uVar13 = FUN_004678a0();
                    /* catch() { ... } // from try @ 005eda68 with catch @ 005edb28 */
                    /* try { // try from 005edb34 to 006edb37 has its CatchHandler @ 005edcd0 */
                    /* try { // try from 005edb38 to 006edb97 has its CatchHandler @ 005ecd50 */
                    /* catch() { ... } // from try @ 005ed2fc with catch @ 005edb3c */
  FUN_00467b6c(uVar13,0xff,0xff,0xff,0xff);
  iVar6 = FUN_00a64b08();
  if (((((iVar6 == 2) || (iVar6 = FUN_00a64b08(), iVar6 == 0xe)) ||
       (iVar6 = FUN_00a64b08(), iVar6 == 0x1a)) ||
      ((iVar6 = FUN_00a64b08(), iVar6 == 0x1b || (iVar6 = FUN_00a64b08(), iVar6 == 0x22)))) ||
     (iVar6 = FUN_00a64b08(), iVar6 == 0x432)) {
                    /* try { // try from 005edb98 to 006edb9f has its CatchHandler @ 005edc54 */
    lVar23 = 0;
                    /* try { // try from 005edba0 to 006edbb3 has its CatchHandler @ 005edc3c */
    puVar22 = (undefined4 *)((long)&fde_table_entry_00333818.data_loc + param_1);
    do {
      iVar6 = *(int *)((long)&uleb128_00295fd4 + lVar23 + param_1);
      if (iVar6 < 0x191) {
        lVar18 = lVar23 + param_1;
        if ((*(int *)((long)&uleb128_00295fd4 + lVar18 + 8) == 0) ||
           (iVar8 = FUN_00a64b08(), iVar8 == 0xe)) {
          uVar15 = 0xff;
          uVar17 = 0xff;
          uVar20 = 0xff;
LAB_005edbc4:
          *puVar22 = uVar15;
          *(undefined4 *)((long)&fde_table_entry_00333820.initial_loc + param_1) = uVar17;
                    /* try { // try from 005edbd0 to 006edc07 has its CatchHandler @ 005edc08 */
          *(undefined4 *)((long)&fde_table_entry_00333820.data_loc + param_1) = uVar20;
          fVar26 = (float)FUN_0046d9b4((float)iVar6 * 0.45);
          *(int *)((long)&fde_table_entry_00333828.initial_loc + param_1) = (int)(fVar26 * 255.0);
        }
        else {
          uVar4 = *(int *)((long)&uleb128_00295fd4 + lVar18 + 8) - 1;
          if (uVar4 < 6) {
            lVar14 = (ulong)uVar4 * 4;
            uVar15 = *(undefined4 *)(&DAT_002d8690 + lVar14);
            uVar17 = *(undefined4 *)(&DAT_002d86a8 + lVar14);
            uVar20 = *(undefined4 *)(&DAT_002d86c0 + lVar14);
            goto LAB_005edbc4;
          }
        }
        FUN_00467b6c(uVar13,*puVar22,
                     *(undefined4 *)((long)&fde_table_entry_00333820.initial_loc + param_1),
                     *(undefined4 *)((long)&fde_table_entry_00333820.data_loc + param_1),0xff);
                    /* catch() { ... } // from try @ 005edbd0 with catch @ 005edc08
                       try { // try from 005edc08 to 006edc5f has its CatchHandler @ 005ecd50 */
        FUN_00467f5c(uVar13,*(undefined4 *)((long)&fde_table_entry_00333828.initial_loc + param_1));
        iVar6 = *(int *)((long)&uleb128_00295fd4 + lVar18 + -8);
        iVar8 = (int)((ulong)((long)*(int *)(param_1 + 0x84658) * -0x66666667) >> 0x20);
        iVar7 = FUN_0046ca04(param_1);
                    /* catch() { ... } // from try @ 005edba0 with catch @ 005edc3c */
                    /* catch() { ... } // from try @ 005edb98 with catch @ 005edc54 */
        FUN_00467f94(uVar13,((iVar6 + ((iVar8 >> 2) - (iVar8 >> 0x1f))) - iVar7) + 0x3c0,
                     *(undefined4 *)((long)&uleb128_00295fd4 + lVar23 + param_1 + -4),4,4);
                    /* try { // try from 005edc60 to 006edc63 has its CatchHandler @ 005edcd0 */
        FUN_00467f5c(uVar13,0xff);
      }
                    /* try { // try from 005edc64 to 006edcd3 has its CatchHandler @ 005ecd50 */
      lVar23 = lVar23 + 0x14;
    } while (lVar23 != 2000);
  }
                    /* catch() { ... } // from try @ 005edb34 with catch @ 005edcd0
                       catch() { ... } // from try @ 005edc60 with catch @ 005edcd0 */
  iVar6 = FUN_00a64b08();
                    /* try { // try from 005edcd4 to 006edd2b has its CatchHandler @ 005edcd4
                       catch() { ... } // from try @ 005edcd4 with catch @ 005edcd4
                       catch() { ... } // from try @ 005edd80 with catch @ 005edcd4 */
  if ((iVar6 == 0x21) || (iVar6 = FUN_00a64b08(), iVar6 == 0x3a)) {
    puVar22 = (undefined4 *)(&uleb128_00296868 + param_1);
    FUN_00468c1c(uVar13,0x32);
    lVar23 = 0x1e;
    do {
      FUN_00468fc8(uVar13,*(undefined8 *)(local_a8 + 0xc40),puVar22[-1],*puVar22,0x1c);
      lVar23 = lVar23 + -1;
      puVar22 = puVar22 + 4;
    } while (lVar23 != 0);
                    /* try { // try from 005edd2c to 006edd33 has its CatchHandler @ 005eddec */
    FUN_00468c1c(uVar13,0xff);
  }
  iVar6 = FUN_00a64b08();
  if (((iVar6 == 0x29) || (iVar6 = FUN_00a64b08(), iVar6 == 0x4b)) ||
     (iVar6 = FUN_00a64b08(), iVar6 == 0x3f0)) {
    lVar23 = -0x1900;
                    /* try { // try from 005edd64 to 006edd67 has its CatchHandler @ 005eddc4 */
                    /* try { // try from 005edd6c to 006edd7f has its CatchHandler @ 005eddd4 */
    do {
      lVar18 = lVar23 + param_1;
      iVar6 = *(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1908);
      if (iVar6 < 0x1e) {
                    /* catch() { ... } // from try @ 005ede4c with catch @ 005edea4 */
        FUN_00468c1c(uVar13,(iVar6 * 0xff) / 0x1e);
      }
      iVar7 = *(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1900);
                    /* try { // try from 005edd80 to 006ede1b has its CatchHandler @ 005edcd4 */
      uVar24 = *(undefined8 *)(local_a8 + 0x2e0);
      iVar12 = (int)((ulong)((long)*(int *)(param_1 + 0x84658) * -0x66666667) >> 0x20);
      iVar9 = FUN_0046ca04();
      iVar11 = *(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1904);
                    /* catch() { ... } // from try @ 005edd64 with catch @ 005eddc4 */
                    /* catch() { ... } // from try @ 005edd6c with catch @ 005eddd4 */
      lVar14 = FUN_00489f8c(*(undefined8 *)(local_a8 + 0x2e0),
                            *(undefined4 *)(&lsda_exception_table_00296ea4 + lVar18 + 0x190c));
      iVar6 = *(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1910);
      iVar8 = *(int *)(lVar14 + 8);
                    /* catch() { ... } // from try @ 005edd2c with catch @ 005eddec */
      lVar14 = FUN_00489f8c(*(undefined8 *)(local_a8 + 0x2e0),
                            *(undefined4 *)(&lsda_exception_table_00296ea4 + lVar18 + 0x190c));
                    /* catch() { ... } // from try @ 005ede58 with catch @ 005ede1c */
                    /* try { // try from 005ede4c to 006ede57 has its CatchHandler @ 005edea4 */
                    /* try { // try from 005ede58 to 006edef3 has its CatchHandler @ 005ede1c */
      FUN_0046bba8((float)*(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1918),uVar13,uVar24,
                   ((iVar7 / 100 + ((iVar12 >> 2) - (iVar12 >> 0x1f))) - iVar9) + 0x3c4,iVar11 / 100
                   ,(iVar6 * iVar8) / 100,
                   (*(int *)(&lsda_exception_table_00296ea4 + lVar18 + 0x1910) *
                   *(int *)(lVar14 + 0xc)) / 100,5,0,0,5,
                   *(undefined4 *)(&lsda_exception_table_00296ea4 + lVar18 + 0x190c));
      FUN_00468c1c(uVar13,0xff);
      lVar23 = lVar23 + 0x40;
    } while (lVar23 != 0);
  }
  else {
    iVar6 = FUN_00a64b08();
    if (iVar6 == 0x37) {
      FUN_00467b30(uVar13,1);
      lVar23 = 0;
      do {
        piVar1 = (int *)(&uleb128_00295fd0 + lVar23 + param_1);
        uVar4 = piVar1[-1];
        if (-1 < (int)uVar4) {
          uVar3 = uVar4 * 100;
                    /* try { // try from 005edf20 to 006edf2b has its CatchHandler @ 005ee028 */
          iVar6 = uVar3 - 0x125;
          if (-1 < (int)(uVar3 - 300)) {
            iVar6 = uVar3 - 300;
          }
          uVar2 = 100 - (iVar6 >> 3);
          if (uVar4 < 3) {
            uVar2 = (uVar3 & 0xfc) / 3;
          }
                    /* try { // try from 005edf50 to 006edf63 has its CatchHandler @ 005edfe8 */
          lVar18 = FUN_00489f8c(*(undefined8 *)(local_a8 + 0x2e0),0x14);
                    /* try { // try from 005edf64 to 006edfab has its CatchHandler @ 005edef4 */
          iVar8 = *(int *)(lVar18 + 8) * uVar2;
          lVar18 = FUN_00489f8c(*(undefined8 *)(local_a8 + 0x2e0),0x14);
          uVar24 = *(undefined8 *)(local_a8 + 0x2e0);
          iVar6 = *piVar1;
          iVar7 = *(int *)(lVar18 + 0xc) * uVar2;
          iVar11 = (int)((ulong)((long)*(int *)(param_1 + 0x84658) * -0x66666667) >> 0x20);
                    /* try { // try from 005edfac to 006edfb7 has its CatchHandler @ 005edfe4 */
                    /* try { // try from 005edfb8 to 006ee057 has its CatchHandler @ 005edef4 */
          iVar10 = FUN_0046ca04(param_1);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005edfac with catch @ 005edfe4
                        */
          iVar12 = (int)((ulong)((long)iVar8 * -0x51eb851f) >> 0x20);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005edf50 with catch @ 005edfe8
                        */
          iVar9 = (int)((ulong)((long)iVar7 * -0x51eb851f) >> 0x20);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 005edf20 with catch @ 005ee028
                        */
          FUN_00469c44(uVar13,uVar24,
                       ((((iVar12 >> 6) - (iVar12 >> 0x1f)) +
                        iVar6 + ((iVar11 >> 2) - (iVar11 >> 0x1f))) - iVar10) + 0x3c0,
                       piVar1[1] + ((iVar9 >> 6) - (iVar9 >> 0x1f)),iVar8 / 100,iVar7 / 100,0x14);
        }
        lVar23 = lVar23 + 0x14;
                    /* try { // try from 005edef4 to 006edf1f has its CatchHandler @ 005edef4
                       catch(type#1 @ 00000000) { ... } // from try @ 005edef4 with catch @ 005edef4
                       catch(type#1 @ 00000000) { ... } // from try @ 005edf64 with catch @ 005edef4
                       catch(type#1 @ 00000000) { ... } // from try @ 005edfb8 with catch @ 005edef4
                        */
      } while (lVar23 != 2000);
      FUN_00467b30(uVar13,0);
    }
  }
  lVar23 = *(long *)(param_1 + 0x1f78);
  lVar18 = *(long *)(param_1 + 0x1f70);
  if (lVar23 == lVar18) {
LAB_005ee56c:
                    /* try { // try from 005ee574 to 006ee5c7 has its CatchHandler @ 005ee574
                       catch() { ... } // from try @ 005ee574 with catch @ 005ee574
                       catch() { ... } // from try @ 005ee650 with catch @ 005ee574 */
    if (*(long *)(lVar5 + 0x28) == local_78) {
      return;
    }
LAB_005ee60c:
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 005ee058 to 006ee0b3 has its CatchHandler @ 005ee058
                       catch() { ... } // from try @ 005ee058 with catch @ 005ee058
                       catch() { ... } // from try @ 005ee0bc with catch @ 005ee058
                       catch() { ... } // from try @ 005ee110 with catch @ 005ee058
                       catch() { ... } // from try @ 005ee1b4 with catch @ 005ee058 */
  uVar25 = 0;
LAB_005ee0ac:
  lVar14 = lVar18 + uVar25 * 0x70;
                    /* try { // try from 005ee0b4 to 006ee0bb has its CatchHandler @ 005ee1bc */
                    /* try { // try from 005ee0bc to 006ee0fb has its CatchHandler @ 005ee058 */
  if ((*(int *)(lVar14 + 8) == 2) && (*(int *)(lVar14 + 0x10) < 1)) {
    plVar16 = *(long **)(param_1 + 0x1fa8);
    if (plVar16 != (long *)0x0) {
      do {
        if (*(int *)(lVar14 + 4) < (int)plVar16[4]) {
          plVar16 = (long *)*plVar16;
        }
        else {
          if (*(int *)(lVar14 + 4) <= (int)plVar16[4]) goto LAB_005ee100;
          plVar16 = (long *)plVar16[1];
        }
        if (plVar16 == (long *)0x0) break;
      } while( true );
    }
    goto LAB_005ee5a4;
  }
  goto LAB_005ee094;
LAB_005ee100:
                    /* try { // try from 005ee110 to 006ee1a7 has its CatchHandler @ 005ee058 */
  plVar16 = (long *)FUN_005f0d90(local_a8 + 0x16288,auStack_80,plVar16 + 5);
  lVar14 = *plVar16;
  if (lVar14 == 0) goto LAB_005ee5a4;
  uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) * 0x6db6db6db6db6db7;
  if (uVar19 < uVar25 || uVar19 - uVar25 == 0) goto LAB_005ee5c4;
  iVar6 = *(int *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 4);
  if (iVar6 < 0) {
    plVar16 = *(long **)(param_1 + 0x1f90);
    if (plVar16 != (long *)0x0) {
      do {
                    /* try { // try from 005ee4d8 to 006ee573 has its CatchHandler @ 005ee374 */
                    /* catch() { ... } // from try @ 005ee40c with catch @ 005ee4dc
                       catch() { ... } // from try @ 005ee4cc with catch @ 005ee4dc */
        if (iVar6 < (int)plVar16[4]) {
                    /* try { // try from 005ee4cc to 006ee4d7 has its CatchHandler @ 005ee4dc */
          plVar16 = (long *)*plVar16;
        }
        else {
                    /* catch() { ... } // from try @ 005ee3bc with catch @ 005ee4e4 */
          if (iVar6 <= (int)plVar16[4]) goto LAB_005ee4f4;
          plVar16 = (long *)plVar16[1];
                    /* catch() { ... } // from try @ 005ee414 with catch @ 005ee4ec */
        }
        if (plVar16 == (long *)0x0) break;
      } while( true );
    }
    goto LAB_005ee5a4;
  }
  FUN_0046f724(lVar14 + 0x38,local_a8 + 0x2e0);
  goto LAB_005ee154;
LAB_005ee4f4:
  plVar16 = (long *)FUN_005f0c10(local_a8 + 0x16270,auStack_80,plVar16 + 5);
  lVar23 = *plVar16;
  if (lVar23 == 0) goto LAB_005ee5a4;
  local_90 = *(undefined8 *)(lVar23 + 0x38);
  local_88 = *(long **)(lVar23 + 0x40);
  if (local_88 != (long *)0x0) {
    FUN_00c53d70(1,local_88 + 1);
  }
  FUN_0046f6ac(lVar14 + 0x38,&local_90);
  plVar16 = local_88;
  if ((local_88 != (long *)0x0) &&
     (lVar23 = FUN_00c53da0(0xffffffffffffffff,local_88 + 1), lVar23 == 0)) {
    (**(code **)(*plVar16 + 0x10))(plVar16);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar16);
  }
LAB_005ee154:
  uVar24 = FUN_00470120(lVar14 + 0x38,0);
  iVar6 = FUN_0047018c(lVar14 + 0x38);
  uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) * 0x6db6db6db6db6db7;
  if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
    lVar23 = *(long *)(param_1 + 0x1f70) + uVar25 * 0x70;
    fVar27 = *(float *)(lVar23 + 0x20);
    fVar26 = *(float *)(lVar23 + 0x24);
    iVar8 = FUN_0047018c(lVar14 + 0x38);
                    /* try { // try from 005ee1a8 to 006ee1b3 has its CatchHandler @ 005ee1bc */
    uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) * 0x6db6db6db6db6db7;
                    /* try { // try from 005ee1b4 to 006ee243 has its CatchHandler @ 005ee058 */
    if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
                    /* catch() { ... } // from try @ 005ee0b4 with catch @ 005ee1bc
                       catch() { ... } // from try @ 005ee1a8 with catch @ 005ee1bc */
      lVar23 = *(long *)(param_1 + 0x1f70) + uVar25 * 0x70;
                    /* catch() { ... } // from try @ 005ee0fc with catch @ 005ee1c4 */
      FUN_0046e7e0(uVar24,(int)(fVar27 * (float)iVar6 * fVar26),
                   (int)(*(float *)(lVar23 + 0x20) * (float)iVar8 * *(float *)(lVar23 + 0x28)));
      uVar24 = FUN_00470120(lVar14 + 0x38,0);
      iVar6 = FUN_00470184(lVar14 + 0x38);
      uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) * 0x6db6db6db6db6db7
      ;
      if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
        FUN_0046e7d8(uVar24,(int)((*(float *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 0x2c) *
                                  (float)iVar6) / 360.0));
        uVar24 = FUN_00470120(lVar14 + 0x38,0);
        iVar6 = FUN_0047017c(lVar14 + 0x38);
        uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) *
                 0x6db6db6db6db6db7;
        if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
                    /* catch() { ... } // from try @ 005ee2d4 with catch @ 005ee294 */
          FUN_0046e7d0(uVar24,(int)((*(float *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 0x34)
                                    * (float)iVar6) / 255.0));
          uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) *
                   0x6db6db6db6db6db7;
                    /* try { // try from 005ee2c4 to 006ee2d3 has its CatchHandler @ 005ee324 */
          if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
            plVar16 = *(long **)(param_1 + 0x1fc0);
                    /* try { // try from 005ee2d4 to 006ee373 has its CatchHandler @ 005ee294 */
            if (plVar16 != (long *)0x0) {
              iVar6 = *(int *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 4);
              do {
                if (iVar6 < (int)plVar16[4]) {
                  plVar16 = (long *)*plVar16;
                }
                else {
                  if (iVar6 <= (int)plVar16[4]) goto LAB_005ee30c;
                  plVar16 = (long *)plVar16[1];
                }
                if (plVar16 == (long *)0x0) break;
              } while( true );
            }
LAB_005ee5a4:
            if (*(long *)(lVar5 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
              FUN_00442970("map::at:  key not found");
            }
            goto LAB_005ee60c;
          }
        }
      }
    }
  }
LAB_005ee5c4:
                    /* try { // try from 005ee5c8 to 006ee5cf has its CatchHandler @ 005ee6e8 */
                    /* try { // try from 005ee5d4 to 006ee5db has its CatchHandler @ 005ee748 */
  if (*(long *)(lVar5 + 0x28) == local_78) {
    uVar13 = FUN_005f01ec(param_1 + 0x1f70);
    FUN_0046e578(&local_90);
    if (*(long *)(lVar5 + 0x28) == local_78) {
                    /* WARNING: Subroutine does not return */
      FUN_00c53ffc(uVar13);
    }
  }
  goto LAB_005ee60c;
LAB_005ee30c:
  plVar16 = (long *)FUN_005df60c(local_a8 + 0x162a0,auStack_80,plVar16 + 5);
  if (*plVar16 != 0) {
                    /* catch() { ... } // from try @ 005ee2c4 with catch @ 005ee324 */
    uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) * 0x6db6db6db6db6db7;
    if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
      FUN_004700f4(lVar14 + 0x38,*plVar16 + 0x38,
                   *(undefined4 *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 0xc),0);
      lVar23 = *(long *)(param_1 + 0x1f78);
      lVar18 = *(long *)(param_1 + 0x1f70);
                    /* try { // try from 005ee374 to 006ee3bb has its CatchHandler @ 005ee374
                       catch() { ... } // from try @ 005ee374 with catch @ 005ee374
                       catch() { ... } // from try @ 005ee42c with catch @ 005ee374
                       catch() { ... } // from try @ 005ee4d8 with catch @ 005ee374 */
      uVar19 = (lVar23 - lVar18 >> 4) * 0x6db6db6db6db6db7;
      if (uVar25 <= uVar19 && uVar19 - uVar25 != 0) {
        lVar21 = *(long *)(param_1 + 0x1f58) + (long)*(int *)(lVar18 + uVar25 * 0x70) * 2000;
        iVar6 = *(int *)(lVar21 + 0x7c0);
        iVar8 = *(int *)(lVar21 + 0x7c4);
        if (iVar6 <= iVar8) {
          uVar15 = *(undefined4 *)(lVar21 + 0x7c8);
          uVar17 = *(undefined4 *)(lVar21 + 0x7cc);
                    /* try { // try from 005ee3bc to 006ee3ef has its CatchHandler @ 005ee4e4 */
          do {
            uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) *
                     0x6db6db6db6db6db7;
            if (uVar19 < uVar25 || uVar19 - uVar25 == 0) goto LAB_005ee5c4;
            fVar26 = *(float *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 0x18);
            iVar11 = FUN_005df114(param_1 + 0x1f50,0xffffffff,uVar15,uVar17);
                    /* try { // try from 005ee40c to 006ee40f has its CatchHandler @ 005ee4dc */
                    /* try { // try from 005ee414 to 006ee42b has its CatchHandler @ 005ee4ec */
            iVar7 = *(int *)(param_1 + 0x84658);
            iVar12 = FUN_0046ca04(param_1);
                    /* try { // try from 005ee42c to 006ee4cb has its CatchHandler @ 005ee374 */
            uVar19 = (*(long *)(param_1 + 0x1f78) - *(long *)(param_1 + 0x1f70) >> 4) *
                     0x6db6db6db6db6db7;
            if (uVar19 < uVar25 || uVar19 - uVar25 == 0) goto LAB_005ee5c4;
            iVar9 = iVar12 + -0x3bf;
            if (0x3bf < iVar12) {
              iVar9 = iVar12 + -0x3c0;
            }
            FUN_0046bd94(uVar13,lVar14 + 0x38,
                         (int)(((fVar26 + (float)(iVar11 * iVar6)) - (float)(iVar7 / 10)) +
                              (float)(iVar9 >> 1)),
                         (int)*(float *)(*(long *)(param_1 + 0x1f70) + uVar25 * 0x70 + 0x1c));
            iVar6 = iVar6 + 1;
          } while (iVar8 + 1 != iVar6);
          lVar23 = *(long *)(param_1 + 0x1f78);
          lVar18 = *(long *)(param_1 + 0x1f70);
        }
LAB_005ee094:
        uVar25 = uVar25 + 1;
        uVar19 = (lVar23 - lVar18 >> 4) * 0x6db6db6db6db6db7;
        if (uVar19 < uVar25 || uVar19 - uVar25 == 0) goto LAB_005ee56c;
        goto LAB_005ee0ac;
      }
    }
    goto LAB_005ee5c4;
  }
  goto LAB_005ee5a4;
}

~~~
