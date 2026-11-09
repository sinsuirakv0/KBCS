# 00acfac4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acfac4",
  "name": "FUN_00acfac4",
  "size": 1708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcbe1e6c9b4f54b2f752ce68ae1648ba26930ca30257599641fef53fc17f5fa0",
  "source_text_sha256": "fcbe1e6c9b4f54b2f752ce68ae1648ba26930ca30257599641fef53fc17f5fa0"
}
~~~

## 呼び出し元

- [00ad075c](../00ad0/00ad075c.md)
- [00ad6d50](../00ad6/00ad6d50.md)
- [00aec538](../00aec/00aec538.md)

## 呼び出し先

- [00498190](../00498/00498190.md)
- [006337a4](../00633/006337a4.md)
- [00666be8](../00666/00666be8.md)
- [00695b6c](../00695/00695b6c.md)
- [009a2998](../009a2/009a2998.md)
- [009df498](../009df/009df498.md)
- [009e0e24](../009e0/009e0e24.md)
- [009e2df8](../009e2/009e2df8.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58210](../00c58/00c58210.md)

## 疑似コード / UTF-8 13156 bytes

~~~c

void FUN_00acfac4(long param_1,ulong param_2)

{
  bool bVar1;
  long lVar2;
  long *plVar3;
  ulong uVar4;
  uint uVar5;
  ulong uVar6;
  long lVar7;
  int iVar8;
  long lVar9;
  ulong uVar10;
  long lVar11;
  long lVar12;
  int *piVar13;
  undefined4 *puVar14;
  ulong uVar15;
  ulong uVar16;
  ulong uVar17;
  byte *pbVar18;
  int iVar19;
  long *plVar20;
  long lVar21;
  long lVar22;
  long *plVar23;
  undefined2 uVar24;
  undefined8 uVar25;
  long local_88;
  long *local_80;
  int local_78;
  undefined1 uStack_71;
  int *local_70;
  long local_68;
  
  lVar7 = tpidr_el0;
  local_68 = *(long *)(lVar7 + 0x28);
  iVar8 = *(int *)((long)&fde_table_entry_00333a28.initial_loc + param_1);
  if (((param_2 & 1) != 0) || (DAT_00ca4220 != iVar8)) {
    DAT_00ca4220 = iVar8;
    if (DAT_00ca4578 == 0) {
      lVar9 = 0;
    }
    else {
      lVar9 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d550,0);
    }
    if (*(int *)((long)&fde_table_entry_00333f48.data_loc + param_1) == 3) {
      pbVar18 = (byte *)(param_1 + 0x82a7b);
      iVar19 = 0;
      lVar2 = (long)iVar8 + 5;
      lVar22 = (long)iVar8 + -5;
      lVar21 = 0x378;
      do {
        if (((uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
             (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
             (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
            (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3])) != 0xffffffff) {
          if ((iVar19 < (int)lVar22) || ((int)lVar2 < iVar19)) {
            local_88 = 0;
            local_80 = (long *)0x0;
            local_70 = (int *)CONCAT44(local_70._4_4_,iVar19);
            FUN_009a2998(lVar9 + 0x318,&local_70);
          }
          else {
            if (((DAT_00ca4b38 & 1) == 0) &&
               (iVar8 = __cxa_guard_acquire(&DAT_00ca4b38), iVar8 != 0)) {
              DAT_00ca4b08 = 0;
              DAT_00ca4b00 = &DAT_00ca4b08;
              DAT_00ca4b28 = 0;
              DAT_00ca4b30 = 0;
              DAT_00ca4b20 = 0;
              DAT_00ca4b10 = 0;
              DAT_00ca4b18 = &DAT_00ca4b20;
              __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
              __cxa_guard_release(&DAT_00ca4b38);
            }
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3]);
            uVar10 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df498(lVar11,uVar5), lVar11 == 0)) {
              piVar13 = (int *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              piVar13 = (int *)(lVar11 + 4);
            }
            FUN_006337a4(&local_88,&DAT_00ca4b00,
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                         + (long)*piVar13 * 0x78 + (long)(int)uVar5 * 0x1e0 + param_1 + 0x60,
                         PTR_DAT_00c9a8a0,0x1e,0,0,0);
            local_78 = iVar19;
            if (local_88 == 0) {
              FUN_009a2998(lVar9 + 0x318,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695b6c(lVar9 + 0x318,&local_78,&DAT_002c86b5,&local_70,&uStack_71);
              plVar3 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c538b0(1,local_80 + 1);
              }
              plVar23 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar3;
              if ((plVar23 != (long *)0x0) &&
                 (lVar11 = FUN_00c538e0(0xffffffffffffffff,plVar23 + 1), lVar11 == 0)) {
                (**(code **)(*plVar23 + 0x10))(plVar23);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
              }
            }
          }
          plVar3 = local_80;
          if ((local_80 != (long *)0x0) &&
             (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
            (**(code **)(*plVar3 + 0x10))(plVar3);
            _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
          }
          iVar19 = iVar19 + 1;
        }
        lVar21 = lVar21 + -1;
        pbVar18 = pbVar18 + 4;
      } while (lVar21 != 0);
      if (-1 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1)) {
        plVar3 = (long *)(lVar9 + 0x2f0);
        lVar21 = 0;
        do {
                    /* try { // try from 00acfe60 to 00bcfec3 has its CatchHandler @ 00acfe60
                       catch() { ... } // from try @ 00acfe60 with catch @ 00acfe60
                       catch() { ... } // from try @ 00acfed8 with catch @ 00acfe60
                       catch() { ... } // from try @ 00acffa0 with catch @ 00acfe60
                       catch() { ... } // from try @ 00ad002c with catch @ 00acfe60 */
          if ((lVar21 < lVar22) || (lVar2 < lVar21)) {
            uVar10 = *(ulong *)(lVar9 + 0x2f8);
            if (uVar10 != 0) {
              uVar4 = lVar21 + 0xb;
              uVar25 = CONCAT17(POPCOUNT((char)(uVar10 >> 0x38)),
                                CONCAT16(POPCOUNT((char)(uVar10 >> 0x30)),
                                         CONCAT15(POPCOUNT((char)(uVar10 >> 0x28)),
                                                  CONCAT14(POPCOUNT((char)(uVar10 >> 0x20)),
                                                           CONCAT13(POPCOUNT((char)(uVar10 >> 0x18))
                                                                    ,CONCAT12(POPCOUNT((char)(uVar10
                                                                                             >> 0x10
                                                  )),CONCAT11(POPCOUNT((char)(uVar10 >> 8)),
                                                              POPCOUNT((char)uVar10))))))));
              uVar24 = NEON_uaddlv(uVar25,1);
              uVar15 = CONCAT62((int6)((ulong)uVar25 >> 0x10),uVar24) & 0xffffffff;
              if (uVar15 < 2) {
                    /* try { // try from 00acff18 to 00bcff2b has its CatchHandler @ 00ad0150 */
                uVar16 = uVar10 + 0x7fffffff & uVar4;
              }
              else {
                uVar16 = uVar4;
                if (uVar10 <= uVar4) {
                  uVar16 = 0;
                  if (uVar10 != 0) {
                    uVar16 = uVar4 / uVar10;
                  }
                  uVar16 = uVar4 - uVar16 * uVar10;
                }
              }
              plVar23 = *(long **)(*plVar3 + uVar16 * 8);
                    /* try { // try from 00ad0020 to 00bd002b has its CatchHandler @ 00ad014c */
              if ((plVar23 != (long *)0x0) && (plVar23 = (long *)*plVar23, plVar23 != (long *)0x0))
              {
                do {
                  uVar17 = plVar23[1];
                  if (uVar17 == uVar4) {
                    /* try { // try from 00ad002c to 00bd0183 has its CatchHandler @ 00acfe60 */
                    if (uVar4 == *(uint *)(plVar23 + 2)) {
                      local_88 = 0;
                      local_80 = (long *)0x0;
                      local_70 = (int *)CONCAT44(local_70._4_4_,(int)uVar4);
                      FUN_009a2998(plVar3,&local_70);
                      plVar23 = local_80;
                      if ((local_80 != (long *)0x0) &&
                         (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
                        (**(code **)(*plVar23 + 0x10))(plVar23);
                        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
                      }
                      break;
                    }
                  }
                  else {
                    if (uVar15 < 2) {
                      uVar17 = uVar17 & uVar10 - 1;
                    }
                    else if (uVar10 <= uVar17) {
                      uVar6 = 0;
                      if (uVar10 != 0) {
                        uVar6 = uVar17 / uVar10;
                      }
                      uVar17 = uVar17 - uVar6 * uVar10;
                    }
                    if (uVar17 != uVar16) break;
                  }
                  plVar23 = (long *)*plVar23;
                } while (plVar23 != (long *)0x0);
              }
            }
          }
          else {
            pbVar18 = (byte *)(param_1 + 0x82a78 + lVar21 * 4);
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[2]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ pbVar18[3]) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[1]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ *pbVar18);
            uVar10 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
                    /* try { // try from 00acfec4 to 00bcfed7 has its CatchHandler @ 00ad0134 */
                    /* try { // try from 00acfed8 to 00bcff17 has its CatchHandler @ 00acfe60 */
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df498(lVar11,uVar5), lVar11 == 0)) {
              puVar14 = (undefined4 *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              puVar14 = (undefined4 *)(lVar11 + 4);
            }
                    /* try { // try from 00acff38 to 00bcff43 has its CatchHandler @ 00ad0158 */
            FUN_00666be8(&local_88,uVar5,*puVar14);
            local_78 = (int)lVar21 + 0xb;
            if (local_88 == 0) {
              FUN_009a2998(plVar3,&local_78);
            }
            else {
              local_70 = &local_78;
                    /* try { // try from 00acff60 to 00bcff67 has its CatchHandler @ 00ad014c */
              lVar12 = FUN_00695b6c(plVar3,&local_78,&DAT_002c86b5,&local_70,&uStack_71);
              plVar23 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c538b0(1,local_80 + 1);
              }
              plVar20 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar23;
                    /* try { // try from 00acff8c to 00bcff9f has its CatchHandler @ 00ad0130 */
              if ((plVar20 != (long *)0x0) &&
                 (lVar11 = FUN_00c538e0(0xffffffffffffffff,plVar20 + 1), lVar11 == 0)) {
                    /* try { // try from 00acffa0 to 00bcffdf has its CatchHandler @ 00acfe60 */
                (**(code **)(*plVar20 + 0x10))(plVar20);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar20);
              }
            }
            plVar23 = local_80;
            if ((local_80 != (long *)0x0) &&
               (lVar11 = FUN_00c538e0(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
                    /* try { // try from 00acffe0 to 00bcfff3 has its CatchHandler @ 00ad0154 */
              (**(code **)(*plVar23 + 0x10))(plVar23);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
                    /* try { // try from 00acfff8 to 00bd0003 has its CatchHandler @ 00ad015c */
            }
          }
          bVar1 = lVar21 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1);
          lVar21 = lVar21 + 1;
        } while (bVar1);
      }
    }
  }
  if (((DAT_00ca4b38 & 1) == 0) && (iVar8 = __cxa_guard_acquire(&DAT_00ca4b38), iVar8 != 0)) {
                    /* catch() { ... } // from try @ 00acff8c with catch @ 00ad0130 */
                    /* catch() { ... } // from try @ 00acfec4 with catch @ 00ad0134 */
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
                    /* catch() { ... } // from try @ 00acff60 with catch @ 00ad014c
                       catch() { ... } // from try @ 00ad0020 with catch @ 00ad014c */
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
                    /* catch() { ... } // from try @ 00acff18 with catch @ 00ad0150 */
    DAT_00ca4b20 = 0;
                    /* catch() { ... } // from try @ 00acffe0 with catch @ 00ad0154 */
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
                    /* catch() { ... } // from try @ 00acff38 with catch @ 00ad0158 */
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
                    /* catch() { ... } // from try @ 00acfff8 with catch @ 00ad015c */
    __cxa_guard_release(&DAT_00ca4b38);
  }
  if (DAT_00ca4b30 != 0) {
    FUN_00498190();
  }
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
