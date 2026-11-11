# 00acfcc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00acfcc0",
  "name": "FUN_00acfcc0",
  "size": 1708,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78f24d98e1ff8cef201f50cfbb3721e992eba79d62764adcf5f06869af059de4",
  "source_text_sha256": "78f24d98e1ff8cef201f50cfbb3721e992eba79d62764adcf5f06869af059de4"
}
~~~

## 呼び出し元

- [00ad0958](../00ad0/00ad0958.md)
- [00ad6f4c](../00ad6/00ad6f4c.md)
- [00aec960](../00aec/00aec960.md)

## 呼び出し先

- [004981d0](../00498/004981d0.md)
- [006337e4](../00633/006337e4.md)
- [00666c28](../00666/00666c28.md)
- [00695bac](../00695/00695bac.md)
- [009a2b34](../009a2/009a2b34.md)
- [009df634](../009df/009df634.md)
- [009e0fc0](../009e0/009e0fc0.md)
- [009e2f94](../009e2/009e2f94.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

## 疑似コード / UTF-8 15101 bytes

~~~c

void FUN_00acfcc0(long param_1,ulong param_2)

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
  if (((param_2 & 1) != 0) || (DAT_00ca4620 != iVar8)) {
    DAT_00ca4620 = iVar8;
    if (DAT_00ca4978 == 0) {
      lVar9 = 0;
    }
    else {
      lVar9 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
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
            FUN_009a2b34(lVar9 + 0x318,&local_70);
          }
          else {
            if (((DAT_00ca4f38 & 1) == 0) &&
               (iVar8 = __cxa_guard_acquire(&DAT_00ca4f38), iVar8 != 0)) {
              DAT_00ca4f08 = 0;
              DAT_00ca4f00 = &DAT_00ca4f08;
              DAT_00ca4f28 = 0;
              DAT_00ca4f30 = 0;
              DAT_00ca4f20 = 0;
                    /* try { // try from 00acfffc to 00bd005f has its CatchHandler @ 00acfffc
                       catch() { ... } // from try @ 00acfffc with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad0074 with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad013c with catch @ 00acfffc
                       catch() { ... } // from try @ 00ad01c8 with catch @ 00acfffc */
              DAT_00ca4f10 = 0;
              DAT_00ca4f18 = &DAT_00ca4f20;
              __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
              __cxa_guard_release(&DAT_00ca4f38);
            }
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[-1]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ *pbVar18) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[-2]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ pbVar18[-3]);
            uVar10 = FUN_009e0fc0(param_1 + 0x50,0xffffffff,0xffffffff);
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df634(lVar11,uVar5), lVar11 == 0)) {
              piVar13 = (int *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              piVar13 = (int *)(lVar11 + 4);
            }
            FUN_006337e4(&local_88,&DAT_00ca4f00,
                         "NSt6__ndk110__function6__funcIZN11aDownloader8downloadERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEiiE3$_2NS6_ISB_EEFvbEEE"
                         + (long)*piVar13 * 0x78 + (long)(int)uVar5 * 0x1e0 + param_1 + 0x20,
                         PTR_DAT_00c9aca0,0x1e,0,0,0);
            local_78 = iVar19;
            if (local_88 == 0) {
              FUN_009a2b34(lVar9 + 0x318,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695bac(lVar9 + 0x318,&local_78,&DAT_002c86f5,&local_70,&uStack_71);
              plVar3 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                FUN_00c53cd0(1,local_80 + 1);
              }
              plVar23 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar3;
              if ((plVar23 != (long *)0x0) &&
                 (lVar11 = FUN_00c53d00(0xffffffffffffffff,plVar23 + 1), lVar11 == 0)) {
                (**(code **)(*plVar23 + 0x10))(plVar23);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
              }
            }
          }
          plVar3 = local_80;
          if ((local_80 != (long *)0x0) &&
             (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
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
                    /* try { // try from 00ad0060 to 00bd0073 has its CatchHandler @ 00ad02d0 */
          if ((lVar21 < lVar22) || (lVar2 < lVar21)) {
            uVar10 = *(ulong *)(lVar9 + 0x2f8);
            if (uVar10 != 0) {
              uVar4 = lVar21 + 0xb;
                    /* try { // try from 00ad00fc to 00bd0103 has its CatchHandler @ 00ad02e8 */
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
              if ((plVar23 != (long *)0x0) && (plVar23 = (long *)*plVar23, plVar23 != (long *)0x0))
              {
                do {
                  uVar17 = plVar23[1];
                  if (uVar17 == uVar4) {
                    if (uVar4 == *(uint *)(plVar23 + 2)) {
                      local_88 = 0;
                      local_80 = (long *)0x0;
                      local_70 = (int *)CONCAT44(local_70._4_4_,(int)uVar4);
                      FUN_009a2b34(plVar3,&local_70);
                      plVar23 = local_80;
                      if ((local_80 != (long *)0x0) &&
                         (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
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
                    /* try { // try from 00ad0074 to 00bd00b3 has its CatchHandler @ 00acfffc */
            pbVar18 = (byte *)(param_1 + 0x82a78 + lVar21 * 4);
                    /* try { // try from 00ad00b4 to 00bd00c7 has its CatchHandler @ 00ad02ec */
            uVar5 = (uint)(*(byte *)(param_1 + 0x8385a) ^ pbVar18[2]) << 0x10 |
                    (uint)(*(byte *)(param_1 + 0x8385b) ^ pbVar18[3]) << 0x18 |
                    (uint)(*(byte *)(param_1 + 0x83859) ^ pbVar18[1]) << 8 |
                    (uint)(*(byte *)(param_1 + 0x83858) ^ *pbVar18);
            uVar10 = FUN_009e0fc0(param_1 + 0x50,0xffffffff,0xffffffff);
                    /* try { // try from 00ad00d4 to 00bd00df has its CatchHandler @ 00ad02f4 */
            if ((((uVar10 & 1) == 0) ||
                (lVar11 = FUN_009e2f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar11 == 0)) ||
               (lVar11 = FUN_009df634(lVar11,uVar5), lVar11 == 0)) {
              puVar14 = (undefined4 *)(param_1 + 0x49934 + (long)(int)uVar5 * 4);
            }
            else {
              puVar14 = (undefined4 *)(lVar11 + 4);
            }
                    /* try { // try from 00ad0128 to 00bd013b has its CatchHandler @ 00ad02cc */
            FUN_00666c28(&local_88,uVar5,*puVar14);
                    /* try { // try from 00ad013c to 00bd017b has its CatchHandler @ 00acfffc */
            local_78 = (int)lVar21 + 0xb;
            if (local_88 == 0) {
                    /* try { // try from 00ad01bc to 00bd01c7 has its CatchHandler @ 00ad02e8 */
              FUN_009a2b34(plVar3,&local_78);
            }
            else {
              local_70 = &local_78;
              lVar12 = FUN_00695bac(plVar3,&local_78,&DAT_002c86f5,&local_70,&uStack_71);
              plVar23 = local_80;
              lVar11 = local_88;
              if (local_80 != (long *)0x0) {
                    /* try { // try from 00ad017c to 00bd018f has its CatchHandler @ 00ad02f0 */
                FUN_00c53cd0(1,local_80 + 1);
              }
              plVar20 = *(long **)(lVar12 + 0x20);
              *(long *)(lVar12 + 0x18) = lVar11;
              *(long **)(lVar12 + 0x20) = plVar23;
                    /* try { // try from 00ad0194 to 00bd019f has its CatchHandler @ 00ad02f8 */
              if ((plVar20 != (long *)0x0) &&
                 (lVar11 = FUN_00c53d00(0xffffffffffffffff,plVar20 + 1), lVar11 == 0)) {
                (**(code **)(*plVar20 + 0x10))(plVar20);
                _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar20);
              }
            }
            plVar23 = local_80;
                    /* try { // try from 00ad01c8 to 00bd031f has its CatchHandler @ 00acfffc */
            if ((local_80 != (long *)0x0) &&
               (lVar11 = FUN_00c53d00(0xffffffffffffffff,local_80 + 1), lVar11 == 0)) {
              (**(code **)(*plVar23 + 0x10))(plVar23);
              _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar23);
            }
          }
          bVar1 = lVar21 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1);
          lVar21 = lVar21 + 1;
        } while (bVar1);
      }
    }
  }
  if (((DAT_00ca4f38 & 1) == 0) && (iVar8 = __cxa_guard_acquire(&DAT_00ca4f38), iVar8 != 0)) {
                    /* try { // try from 00ad0320 to 00bd045f has its CatchHandler @ 00ad0320
                       catch() { ... } // from try @ 00ad0320 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0468 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0924 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad0df8 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2028 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2070 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad20c0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad21a0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2268 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad22d0 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2468 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad24c4 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2528 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad25bc with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2610 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2664 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad26b8 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad270c with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad28bc with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2968 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad2ab4 with catch @ 00ad0320
                       catch() { ... } // from try @ 00ad3264 with catch @ 00ad0320 */
    DAT_00ca4f08 = 0;
    DAT_00ca4f00 = &DAT_00ca4f08;
    DAT_00ca4f28 = 0;
    DAT_00ca4f30 = 0;
    DAT_00ca4f20 = 0;
    DAT_00ca4f10 = 0;
    DAT_00ca4f18 = &DAT_00ca4f20;
    __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_00ca4f38);
  }
                    /* catch() { ... } // from try @ 00ad0128 with catch @ 00ad02cc */
                    /* catch() { ... } // from try @ 00ad0060 with catch @ 00ad02d0 */
  if (DAT_00ca4f30 != 0) {
    FUN_004981d0();
  }
                    /* catch() { ... } // from try @ 00ad00fc with catch @ 00ad02e8
                       catch() { ... } // from try @ 00ad01bc with catch @ 00ad02e8 */
                    /* catch() { ... } // from try @ 00ad00b4 with catch @ 00ad02ec */
  if (*(long *)(lVar7 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* catch() { ... } // from try @ 00ad017c with catch @ 00ad02f0 */
                    /* catch() { ... } // from try @ 00ad00d4 with catch @ 00ad02f4 */
                    /* catch() { ... } // from try @ 00ad0194 with catch @ 00ad02f8 */
  return;
}

~~~
