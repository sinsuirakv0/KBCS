# 00aedde0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aedde0",
  "name": "FUN_00aedde0",
  "size": 2156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce32673c7ce13579c04278ef9a7c6c92fc863faf8ca40208e2a59c5c4c6ef10f",
  "source_text_sha256": "ce32673c7ce13579c04278ef9a7c6c92fc863faf8ca40208e2a59c5c4c6ef10f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043ddd8](../0043d/0043ddd8.md)
- [00442930](../00442/00442930.md)
- [00447ef4](../00447/00447ef4.md)
- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [0048ce54](../0048c/0048ce54.md)
- [005d8bc8](../005d8/005d8bc8.md)
- [008514f8](../00851/008514f8.md)
- [008b6f10](../008b6/008b6f10.md)
- [008b6f18](../008b6/008b6f18.md)
- [008b6fec](../008b6/008b6fec.md)
- [008b7948](../008b7/008b7948.md)
- [008b79c8](../008b7/008b79c8.md)
- [008b9178](../008b9/008b9178.md)
- [008b9298](../008b9/008b9298.md)
- [008b9858](../008b9/008b9858.md)
- [008bacc8](../008ba/008bacc8.md)
- [00a46784](../00a46/00a46784.md)
- [00a468fc](../00a46/00a468fc.md)
- [00a4754c](../00a47/00a4754c.md)
- [00abf604](../00abf/00abf604.md)
- [00ad040c](../00ad0/00ad040c.md)
- [00ad06d8](../00ad0/00ad06d8.md)
- [00aee860](../00aee/00aee860.md)
- [00aee864](../00aee/00aee864.md)
- [00aeea48](../00aee/00aeea48.md)
- [00aeea4c](../00aee/00aeea4c.md)
- [00aeeb2c](../00aee/00aeeb2c.md)
- [00aeeb30](../00aee/00aeeb30.md)
- [00b0965c](../00b09/00b0965c.md)
- [00b3be94](../00b3b/00b3be94.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

## 関連文字列（未確認候補）

~~~text
"array::at"
"slotunlock_medal_txt1"
~~~

## 疑似コード / UTF-8 13872 bytes

~~~c

void FUN_00aedde0(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined1 *puVar1;
  byte bVar2;
  char cVar3;
  long lVar4;
  undefined *puVar5;
  undefined *puVar6;
  undefined **ppuVar7;
  bool bVar8;
  bool bVar9;
  int iVar10;
  int iVar11;
  long lVar12;
  undefined8 uVar13;
  int extraout_var;
  long *plVar14;
  long lVar15;
  ulong uVar16;
  undefined ***pppuVar17;
  undefined8 uVar18;
  long lVar19;
  undefined **local_108 [2];
  void *local_f8;
  undefined **local_f0 [2];
  void *local_e0;
  undefined **local_d8;
  undefined **local_d0;
  long local_c8;
  void *local_c0;
  undefined ***local_b0;
  undefined **local_a0;
  long lStack_98;
  undefined ***local_80;
  long local_70;
  
                    /* try { // try from 00aedde4 to 00bede8b has its CatchHandler @ 00aedb3c */
  lVar4 = tpidr_el0;
  local_70 = *(long *)(lVar4 + 0x28);
  iVar10 = *param_3;
  uVar18 = *param_2;
  lVar19 = *(long *)(param_1 + 8);
  if (iVar10 == 1) {
    if (DAT_00ca4978 == 0) {
      lVar12 = 0;
    }
    else {
      lVar12 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                              &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8d950,0);
    }
    iVar10 = FUN_008b9298(uVar18);
                    /* catch() { ... } // from try @ 00aedf60 with catch @ 00aedefc */
    FUN_008b9298(uVar18);
    FUN_00a4754c(local_f0,0x3f800000,lVar12 + 0x118,iVar10 + 0x49,extraout_var + -0x14,0x93,0x22,
                 0x94,0x95);
    (**(code **)(*local_f0[0] + 0x10))(local_f0[0],1);
    ppuVar7 = local_f0[0];
                    /* try { // try from 00aedf54 to 00bedf5f has its CatchHandler @ 00aee108 */
    FUN_00a468fc(&local_d0,lVar12 + 0x118,0,0,0x77);
    local_a0 = local_d0;
                    /* try { // try from 00aedf60 to 00bee137 has its CatchHandler @ 00aedefc */
    local_d0 = (undefined **)0x0;
    plVar14 = (long *)FUN_00a46784(ppuVar7,&local_a0);
    (**(code **)(*plVar14 + 0x10))(plVar14,1);
    ppuVar7 = local_a0;
    puVar5 = PTR_DAT_00c9b368;
    local_a0 = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      *ppuVar7 = PTR_DAT_00c9b368 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    ppuVar7 = local_d0;
    puVar6 = PTR_DAT_00c9b370;
    local_d0 = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      plVar14 = (long *)ppuVar7[0x16];
      *ppuVar7 = PTR_DAT_00c9b370 + 0x10;
      if ((plVar14 != (long *)0x0) &&
         (lVar15 = FUN_00c53d00(0xffffffffffffffff,plVar14 + 1), lVar15 == 0)) {
        (**(code **)(*plVar14 + 0x10))(plVar14);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
      }
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    local_d0 = local_f0[0];
    local_f0[0] = (undefined **)0x0;
    local_a0 = &PTR_FUN_00c8dcd8;
    lStack_98 = lVar19;
    local_80 = &local_a0;
    FUN_008b6fec(lVar19 + 0x2f38,0x321,iVar10,extraout_var + -0x25,0x93,0x22,&local_d0,&local_a0);
    if (local_80 == &local_a0) {
      lVar15 = 0x20;
      pppuVar17 = &local_a0;
LAB_00aee084:
      (**(code **)((long)*pppuVar17 + lVar15))();
    }
    else if (local_80 != (undefined ***)0x0) {
      lVar15 = 0x28;
      pppuVar17 = local_80;
      goto LAB_00aee084;
    }
    ppuVar7 = local_d0;
    local_d0 = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    FUN_00a4754c(local_108,0x3f800000,lVar12 + 0x118,iVar10 + 0xe6,extraout_var + -0x14,0x93,0x22,
                 0x94,0x95);
    (**(code **)(*local_108[0] + 0x10))(local_108[0],1);
    ppuVar7 = local_108[0];
                    /* catch() { ... } // from try @ 00aedf54 with catch @ 00aee108 */
    FUN_00a468fc(&local_d8,lVar12 + 0x118,0,0,0x92);
    local_d0 = local_d8;
    local_d8 = (undefined **)0x0;
    plVar14 = (long *)FUN_00a46784(ppuVar7,&local_d0);
    (**(code **)(*plVar14 + 0x10))(plVar14,1);
    ppuVar7 = local_d0;
    local_d0 = (undefined **)0x0;
                    /* try { // try from 00aee138 to 00bee20f has its CatchHandler @ 00aee138
                       catch() { ... } // from try @ 00aee138 with catch @ 00aee138
                       catch() { ... } // from try @ 00aee218 with catch @ 00aee138 */
    if (ppuVar7 != (undefined **)0x0) {
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    ppuVar7 = local_d8;
    local_d8 = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      plVar14 = (long *)ppuVar7[0x16];
      *ppuVar7 = puVar6 + 0x10;
      if ((plVar14 != (long *)0x0) &&
         (lVar12 = FUN_00c53d00(0xffffffffffffffff,plVar14 + 1), lVar12 == 0)) {
        (**(code **)(*plVar14 + 0x10))(plVar14);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
      }
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    local_d8 = local_108[0];
    local_b0 = &local_d0;
    cVar3 = *(char *)((long)&DWORD_0039b980 + lVar19);
    local_108[0] = (undefined **)0x0;
    local_d0 = &PTR_FUN_00c8dd58;
    local_c8 = lVar19;
    uVar18 = FUN_008b6fec(lVar19 + 0x2f38,800,iVar10 + 0x9d,extraout_var + -0x25,0x93,0x22,&local_d8
                          ,&local_d0);
                    /* try { // try from 00aee210 to 00bee217 has its CatchHandler @ 00aee304 */
                    /* try { // try from 00aee218 to 00bee333 has its CatchHandler @ 00aee138 */
    bVar8 = false;
    bVar9 = false;
    if (0x2f < (int)((uint)(*(byte *)(lVar19 + 0xcc1e) ^ *(byte *)(lVar19 + 0xcbf6)) << 0x10 |
                     (uint)(*(byte *)(lVar19 + 0xcc1f) ^ *(byte *)(lVar19 + 0xcbf7)) << 0x18 |
                     (uint)(*(byte *)(lVar19 + 0xcc1d) ^ *(byte *)(lVar19 + 0xcbf5)) << 8 |
                    (uint)(*(byte *)(lVar19 + 0xcc1c) ^ *(byte *)(lVar19 + 0xcbf4)))) {
      bVar9 = SBORROW4((int)cVar3,0x13);
      bVar8 = cVar3 + -0x13 < 0;
    }
    FUN_008b6f10(uVar18,bVar8 != bVar9);
    if (local_b0 == &local_d0) {
      lVar19 = 0x20;
      pppuVar17 = &local_d0;
LAB_00aee27c:
      (**(code **)((long)*pppuVar17 + lVar19))();
    }
    else if (local_b0 != (undefined ***)0x0) {
      lVar19 = 0x28;
      pppuVar17 = local_b0;
      goto LAB_00aee27c;
    }
    ppuVar7 = local_d8;
    local_d8 = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
    ppuVar7 = local_108[0];
    local_108[0] = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      plVar14 = (long *)ppuVar7[0x16];
      *ppuVar7 = puVar6 + 0x10;
      if ((plVar14 != (long *)0x0) &&
         (lVar19 = FUN_00c53d00(0xffffffffffffffff,plVar14 + 1), lVar19 == 0)) {
        (**(code **)(*plVar14 + 0x10))(plVar14);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
      }
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
                    /* catch() { ... } // from try @ 00aee210 with catch @ 00aee304 */
      _ZdlPv(ppuVar7);
    }
    ppuVar7 = local_f0[0];
    local_f0[0] = (undefined **)0x0;
    if (ppuVar7 != (undefined **)0x0) {
      plVar14 = (long *)ppuVar7[0x16];
      *ppuVar7 = puVar6 + 0x10;
      if ((plVar14 != (long *)0x0) &&
         (lVar19 = FUN_00c53d00(0xffffffffffffffff,plVar14 + 1), lVar19 == 0)) {
                    /* try { // try from 00aee334 to 00bee37f has its CatchHandler @ 00aee334
                       catch() { ... } // from try @ 00aee334 with catch @ 00aee334
                       catch() { ... } // from try @ 00aee404 with catch @ 00aee334
                       catch() { ... } // from try @ 00aee740 with catch @ 00aee334
                       catch() { ... } // from try @ 00aee8a4 with catch @ 00aee334 */
        (**(code **)(*plVar14 + 0x10))(plVar14);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar14);
      }
      *ppuVar7 = puVar5 + 0x10;
      FUN_005d8bc8(ppuVar7 + 10);
      _ZdlPv(ppuVar7);
    }
  }
  else {
    iVar11 = *param_4;
    if ((iVar10 == 2) && (iVar11 != -1)) {
      uVar13 = FUN_0047acf4();
      FUN_0047cdd4(uVar13,0xb,0);
      if (*(long *)(lVar4 + 0x28) == local_70) {
                    /* try { // try from 00aede8c to 00bede8f has its CatchHandler @ 00aedeb4 */
                    /* catch() { ... } // from try @ 00aedc7c with catch @ 00aede90
                       try { // try from 00aede90 to 00bedefb has its CatchHandler @ 00aedb3c */
                    /* catch() { ... } // from try @ 00aeddb8 with catch @ 00aede98 */
                    /* catch() { ... } // from try @ 00aedb9c with catch @ 00aedea8 */
        FUN_008b9178(uVar18);
        return;
      }
      goto LAB_00aee7e8;
    }
                    /* catch() { ... } // from try @ 00aedbe0 with catch @ 00aedeb4
                       catch() { ... } // from try @ 00aede8c with catch @ 00aedeb4 */
    if ((iVar10 == 5) && (iVar11 != -1)) {
      if (iVar11 == 2) {
        bVar2 = *(byte *)((long)&DWORD_0039b980 + lVar19);
                    /* try { // try from 00aee3e0 to 00bee3eb has its CatchHandler @ 00aee8f8 */
        puVar1 = (undefined1 *)((long)&fde_table_entry_00335f18.initial_loc + lVar19 + 2);
        iVar10 = 0x5a;
                    /* try { // try from 00aee3ec to 00bee3f7 has its CatchHandler @ 00aee8e0 */
        if (*(char *)((long)&fde_table_entry_00338310.data_loc + lVar19) != '\0') {
          iVar10 = 0x2d;
        }
                    /* try { // try from 00aee3f8 to 00bee403 has its CatchHandler @ 00aee8d0 */
        iVar11 = FUN_00b3be94(lVar19 + 0xc400);
                    /* try { // try from 00aee404 to 00bee443 has its CatchHandler @ 00aee334 */
        if (iVar11 < iVar10) {
          *puVar1 = 1;
          *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar19) = 1;
        }
        else {
          if (0x12 < bVar2) {
            if (*(long *)(lVar4 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00442930("array::at");
            }
            goto LAB_00aee7e8;
          }
          lVar12 = lVar19 + (ulong)bVar2 * 8;
                    /* try { // try from 00aee444 to 00bee44b has its CatchHandler @ 00aee8cc */
          if ((*(int *)((long)&QWORD_0039b984 + lVar12) != 1) ||
             (iVar10 = FUN_00abf604(lVar19 + 0x1a80),
             *(int *)((long)&QWORD_0039b984 + lVar12 + 4) <= iVar10)) {
                    /* try { // try from 00aee4e0 to 00bee4ef has its CatchHandler @ 00aee93c */
            *puVar1 = 1;
            *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar19) = 2;
            goto LAB_00aee4e8;
          }
          FUN_0043ddd8(local_108,"slotunlock_medal_txt1");
          FUN_0048ce54(local_f0,local_108);
                    /* try { // try from 00aee470 to 00bee47b has its CatchHandler @ 00aee8b0 */
          FUN_00447ef4(&local_d0,local_f0,0,*(undefined4 *)((long)&QWORD_0039b984 + lVar12 + 4));
          local_80 = &local_a0;
          local_a0 = &PTR_FUN_00c8ddd8;
          uVar18 = FUN_008bacc8(lVar19 + 0x2f08,&local_d0,0,0,4,&local_a0);
          FUN_008b9858(uVar18,0);
          if (local_80 == &local_a0) {
            lVar12 = 0x20;
            pppuVar17 = &local_a0;
LAB_00aee5d8:
            (**(code **)((long)*pppuVar17 + lVar12))();
          }
          else if (local_80 != (undefined ***)0x0) {
            lVar12 = 0x28;
            pppuVar17 = local_80;
            goto LAB_00aee5d8;
          }
          if (((ulong)local_d0 & 1) != 0) {
            _ZdlPv(local_c0);
          }
                    /* try { // try from 00aee60c to 00bee613 has its CatchHandler @ 00aee8f0 */
          if (((ulong)local_f0[0] & 1) != 0) {
            _ZdlPv(local_e0);
          }
          if (((ulong)local_108[0] & 1) != 0) {
            _ZdlPv(local_f8);
          }
        }
LAB_00aee4e8:
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,0x327);
        FUN_008b6f18(uVar18,0);
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,3);
        FUN_008b6f18(uVar18,0);
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,4);
        FUN_008b6f18(uVar18,0);
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,0x325);
        FUN_008b6f18(uVar18,0);
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,0x322);
        FUN_008b6f18(uVar18,0);
                    /* try { // try from 00aee558 to 00bee55f has its CatchHandler @ 00aee924 */
        uVar18 = FUN_008b79c8(lVar19 + 0x2f38,0x323);
        FUN_008b6f18(uVar18,0);
        uVar16 = FUN_00b0965c(lVar19 + 0x3d8);
        if ((uVar16 & 1) != 0) {
          uVar18 = FUN_008b79c8(lVar19 + 0x2f38,0x328);
          FUN_008b6f18(uVar18,0);
        }
      }
      else if (iVar11 == 1) {
        FUN_008514f8();
        FUN_00ad06d8();
      }
      else if (iVar11 == 0) {
        lVar12 = FUN_008514f8();
        *(undefined1 *)(lVar12 + 0x33a5) = 0;
        FUN_008514f8();
        FUN_00ad040c();
      }
LAB_00aee584:
      FUN_008b7948(lVar19 + 0x2f38,0x321);
      FUN_008b7948(lVar19 + 0x2f38,800);
    }
    else {
      if ((iVar10 == 3) && (iVar11 != -1)) {
        uVar18 = FUN_0047acf4();
                    /* try { // try from 00aee380 to 00bee387 has its CatchHandler @ 00aee91c */
        if (*(long *)(lVar4 + 0x28) == local_70) {
          FUN_0047cdd4(uVar18,0xf,0);
          return;
        }
        goto LAB_00aee7e8;
      }
                    /* try { // try from 00aee3b4 to 00bee3c7 has its CatchHandler @ 00aee904 */
      if (iVar10 == 5) goto LAB_00aee584;
    }
  }
  if (*(long *)(lVar4 + 0x28) == local_70) {
                    /* try { // try from 00aee5c8 to 00bee5d7 has its CatchHandler @ 00aee938 */
    return;
  }
LAB_00aee7e8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
