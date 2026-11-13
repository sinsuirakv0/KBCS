# 00aede7c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aede7c",
  "name": "FUN_00aede7c",
  "size": 2156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c082b65a417f3ea377f7eda10f5fbfc1dbf14063d967a20bd48bc6615af8ea84",
  "source_text_sha256": "c082b65a417f3ea377f7eda10f5fbfc1dbf14063d967a20bd48bc6615af8ea84"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043de18](../0043d/0043de18.md)
- [00442970](../00442/00442970.md)
- [00447f34](../00447/00447f34.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [0048ce94](../0048c/0048ce94.md)
- [005d8c08](../005d8/005d8c08.md)
- [00851550](../00851/00851550.md)
- [008b6f68](../008b6/008b6f68.md)
- [008b6f70](../008b6/008b6f70.md)
- [008b7044](../008b7/008b7044.md)
- [008b79a0](../008b7/008b79a0.md)
- [008b7a20](../008b7/008b7a20.md)
- [008b91d0](../008b9/008b91d0.md)
- [008b92f0](../008b9/008b92f0.md)
- [008b98b0](../008b9/008b98b0.md)
- [008bad20](../008ba/008bad20.md)
- [00a467d8](../00a46/00a467d8.md)
- [00a46950](../00a46/00a46950.md)
- [00a475a0](../00a47/00a475a0.md)
- [00abf674](../00abf/00abf674.md)
- [00ad047c](../00ad0/00ad047c.md)
- [00ad0748](../00ad0/00ad0748.md)
- [00aee8fc](../00aee/00aee8fc.md)
- [00aee900](../00aee/00aee900.md)
- [00aeeae4](../00aee/00aeeae4.md)
- [00aeeae8](../00aee/00aeeae8.md)
- [00aeebc8](../00aee/00aeebc8.md)
- [00aeebcc](../00aee/00aeebcc.md)
- [00b096f8](../00b09/00b096f8.md)
- [00b3bf30](../00b3b/00b3bf30.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"array::at"
"slotunlock_medal_txt1"
~~~

## 疑似コード / UTF-8 13837 bytes

~~~c

void FUN_00aede7c(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined1 *puVar1;
  byte bVar2;
  long lVar3;
  undefined *puVar4;
  undefined *puVar5;
  undefined **ppuVar6;
  bool bVar7;
  bool bVar8;
  int iVar9;
  int iVar10;
  long lVar11;
  undefined8 uVar12;
  int extraout_var;
  long *plVar13;
  long lVar14;
  ulong uVar15;
  undefined ***pppuVar16;
  undefined8 uVar17;
  long lVar18;
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
  
  lVar3 = tpidr_el0;
  local_70 = *(long *)(lVar3 + 0x28);
  iVar9 = *param_3;
  uVar17 = *param_2;
  lVar18 = *(long *)(param_1 + 8);
  if (iVar9 == 1) {
    if (DAT_00ca4a78 == 0) {
      lVar11 = 0;
    }
    else {
                    /* try { // try from 00aedee0 to 00bedee3 has its CatchHandler @ 00aedf08 */
                    /* catch() { ... } // from try @ 00aedcd0 with catch @ 00aedee4
                       try { // try from 00aedee4 to 00bedf4f has its CatchHandler @ 00aedb90 */
      lVar11 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                              &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
                    /* catch() { ... } // from try @ 00aede0c with catch @ 00aedeec */
    }
    iVar9 = FUN_008b92f0(uVar17);
    FUN_008b92f0(uVar17);
                    /* try { // try from 00aedfa8 to 00bedfb3 has its CatchHandler @ 00aee15c */
                    /* try { // try from 00aedfb4 to 00bee18b has its CatchHandler @ 00aedf50 */
    FUN_00a475a0(local_f0,0x3f800000,lVar11 + 0x118,iVar9 + 0x49,extraout_var + -0x14,0x93,0x22,0x94
                 ,0x95);
    (**(code **)(*local_f0[0] + 0x10))(local_f0[0],1);
    ppuVar6 = local_f0[0];
    FUN_00a46950(&local_d0,lVar11 + 0x118,0,0,0x77);
    local_a0 = local_d0;
    local_d0 = (undefined **)0x0;
    plVar13 = (long *)FUN_00a467d8(ppuVar6,&local_a0);
    (**(code **)(*plVar13 + 0x10))(plVar13,1);
    ppuVar6 = local_a0;
    puVar4 = PTR_DAT_00c9b438;
    local_a0 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      *ppuVar6 = PTR_DAT_00c9b438 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    ppuVar6 = local_d0;
    puVar5 = PTR_DAT_00c9b440;
    local_d0 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      plVar13 = (long *)ppuVar6[0x16];
      *ppuVar6 = PTR_DAT_00c9b440 + 0x10;
      if ((plVar13 != (long *)0x0) &&
         (lVar14 = FUN_00c53da0(0xffffffffffffffff,plVar13 + 1), lVar14 == 0)) {
        (**(code **)(*plVar13 + 0x10))(plVar13);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
      }
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    local_d0 = local_f0[0];
    local_f0[0] = (undefined **)0x0;
    local_a0 = &PTR_FUN_00c8dda8;
    lStack_98 = lVar18;
    local_80 = &local_a0;
    FUN_008b7044(lVar18 + 0x2f38,0x321,iVar9,extraout_var + -0x25,0x93,0x22,&local_d0,&local_a0);
    if (local_80 == &local_a0) {
      lVar14 = 0x20;
      pppuVar16 = &local_a0;
LAB_00aee120:
      (**(code **)((long)*pppuVar16 + lVar14))();
    }
    else if (local_80 != (undefined ***)0x0) {
      lVar14 = 0x28;
      pppuVar16 = local_80;
      goto LAB_00aee120;
    }
    ppuVar6 = local_d0;
    local_d0 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
                    /* catch() { ... } // from try @ 00aedfa8 with catch @ 00aee15c */
    FUN_00a475a0(local_108,0x3f800000,lVar11 + 0x118,iVar9 + 0xe6,extraout_var + -0x14,0x93,0x22,
                 0x94,0x95);
    (**(code **)(*local_108[0] + 0x10))(local_108[0],1);
    ppuVar6 = local_108[0];
                    /* try { // try from 00aee18c to 00bee263 has its CatchHandler @ 00aee18c
                       catch() { ... } // from try @ 00aee18c with catch @ 00aee18c
                       catch() { ... } // from try @ 00aee26c with catch @ 00aee18c */
    FUN_00a46950(&local_d8,lVar11 + 0x118,0,0,0x92);
    local_d0 = local_d8;
    local_d8 = (undefined **)0x0;
    plVar13 = (long *)FUN_00a467d8(ppuVar6,&local_d0);
    (**(code **)(*plVar13 + 0x10))(plVar13,1);
    ppuVar6 = local_d0;
    local_d0 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    ppuVar6 = local_d8;
    local_d8 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      plVar13 = (long *)ppuVar6[0x16];
      *ppuVar6 = puVar5 + 0x10;
      if ((plVar13 != (long *)0x0) &&
         (lVar11 = FUN_00c53da0(0xffffffffffffffff,plVar13 + 1), lVar11 == 0)) {
        (**(code **)(*plVar13 + 0x10))(plVar13);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
      }
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    local_d8 = local_108[0];
    local_b0 = &local_d0;
                    /* try { // try from 00aee264 to 00bee26b has its CatchHandler @ 00aee358 */
    bVar2 = BYTE_ARRAY_0039b979[lVar18 + 7];
    local_108[0] = (undefined **)0x0;
                    /* try { // try from 00aee26c to 00bee387 has its CatchHandler @ 00aee18c */
    local_d0 = &PTR_FUN_00c8de28;
    local_c8 = lVar18;
    uVar17 = FUN_008b7044(lVar18 + 0x2f38,800,iVar9 + 0x9d,extraout_var + -0x25,0x93,0x22,&local_d8,
                          &local_d0);
    bVar7 = false;
    bVar8 = false;
    if (0x2f < (int)((uint)(*(byte *)(lVar18 + 0xcc1e) ^ *(byte *)(lVar18 + 0xcbf6)) << 0x10 |
                     (uint)(*(byte *)(lVar18 + 0xcc1f) ^ *(byte *)(lVar18 + 0xcbf7)) << 0x18 |
                     (uint)(*(byte *)(lVar18 + 0xcc1d) ^ *(byte *)(lVar18 + 0xcbf5)) << 8 |
                    (uint)(*(byte *)(lVar18 + 0xcc1c) ^ *(byte *)(lVar18 + 0xcbf4)))) {
      bVar8 = SBORROW4((int)(char)bVar2,0x13);
      bVar7 = (char)bVar2 + -0x13 < 0;
    }
    FUN_008b6f68(uVar17,bVar7 != bVar8);
    if (local_b0 == &local_d0) {
      lVar18 = 0x20;
      pppuVar16 = &local_d0;
LAB_00aee318:
      (**(code **)((long)*pppuVar16 + lVar18))();
    }
    else if (local_b0 != (undefined ***)0x0) {
      lVar18 = 0x28;
      pppuVar16 = local_b0;
      goto LAB_00aee318;
    }
    ppuVar6 = local_d8;
    local_d8 = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    ppuVar6 = local_108[0];
    local_108[0] = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      plVar13 = (long *)ppuVar6[0x16];
                    /* catch() { ... } // from try @ 00aee264 with catch @ 00aee358 */
      *ppuVar6 = puVar5 + 0x10;
      if ((plVar13 != (long *)0x0) &&
         (lVar18 = FUN_00c53da0(0xffffffffffffffff,plVar13 + 1), lVar18 == 0)) {
        (**(code **)(*plVar13 + 0x10))(plVar13);
                    /* try { // try from 00aee388 to 00bee3d3 has its CatchHandler @ 00aee388
                       catch() { ... } // from try @ 00aee388 with catch @ 00aee388
                       catch() { ... } // from try @ 00aee458 with catch @ 00aee388
                       catch() { ... } // from try @ 00aee794 with catch @ 00aee388
                       catch() { ... } // from try @ 00aee8f8 with catch @ 00aee388 */
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
      }
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
    ppuVar6 = local_f0[0];
    local_f0[0] = (undefined **)0x0;
    if (ppuVar6 != (undefined **)0x0) {
      plVar13 = (long *)ppuVar6[0x16];
      *ppuVar6 = puVar5 + 0x10;
      if ((plVar13 != (long *)0x0) &&
         (lVar18 = FUN_00c53da0(0xffffffffffffffff,plVar13 + 1), lVar18 == 0)) {
                    /* try { // try from 00aee3d4 to 00bee3db has its CatchHandler @ 00aee970 */
        (**(code **)(*plVar13 + 0x10))(plVar13);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
      }
      *ppuVar6 = puVar4 + 0x10;
      FUN_005d8c08(ppuVar6 + 10);
      _ZdlPv(ppuVar6);
    }
  }
  else {
    iVar10 = *param_4;
                    /* catch() { ... } // from try @ 00aedbf0 with catch @ 00aedefc */
    if ((iVar9 == 2) && (iVar10 != -1)) {
      uVar12 = FUN_0047ad34();
                    /* catch() { ... } // from try @ 00aedc34 with catch @ 00aedf08
                       catch() { ... } // from try @ 00aedee0 with catch @ 00aedf08 */
      FUN_0047ce14(uVar12,0xb,0);
      if (*(long *)(lVar3 + 0x28) == local_70) {
        FUN_008b91d0(uVar17);
        return;
      }
      goto LAB_00aee884;
    }
                    /* catch() { ... } // from try @ 00aedfb4 with catch @ 00aedf50 */
    if ((iVar9 == 5) && (iVar10 != -1)) {
      if (iVar10 == 2) {
        bVar2 = BYTE_ARRAY_0039b979[lVar18 + 7];
        puVar1 = (undefined1 *)((long)&fde_table_entry_00335f18.initial_loc + lVar18 + 2);
        iVar9 = 0x5a;
        if (*(char *)((long)&fde_table_entry_00338310.data_loc + lVar18) != '\0') {
          iVar9 = 0x2d;
        }
                    /* try { // try from 00aee498 to 00bee49f has its CatchHandler @ 00aee920 */
        iVar10 = FUN_00b3bf30(lVar18 + 0xc400);
        if (iVar10 < iVar9) {
          *puVar1 = 1;
          *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar18) = 1;
        }
        else {
          if (0x12 < bVar2) {
                    /* try { // try from 00aee6d0 to 00bee6d7 has its CatchHandler @ 00aee8fc */
            if (*(long *)(lVar3 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
              FUN_00442970("array::at");
            }
            goto LAB_00aee884;
          }
          lVar11 = lVar18 + (ulong)bVar2 * 8;
                    /* try { // try from 00aee4c4 to 00bee4cf has its CatchHandler @ 00aee904 */
          if ((*(int *)(BYTE_ARRAY_0039b979 + lVar11 + 0xb) != 1) ||
             (iVar9 = FUN_00abf674(lVar18 + 0x1a80),
             *(int *)(BYTE_ARRAY_0039b979 + lVar11 + 0xf) <= iVar9)) {
            *puVar1 = 1;
            *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar18) = 2;
            goto LAB_00aee584;
          }
          FUN_0043de18(local_108,"slotunlock_medal_txt1");
          FUN_0048ce94(local_f0,local_108);
          FUN_00447f34(&local_d0,local_f0,0,*(undefined4 *)(BYTE_ARRAY_0039b979 + lVar11 + 0xf));
          local_80 = &local_a0;
          local_a0 = &PTR_FUN_00c8dea8;
                    /* try { // try from 00aee534 to 00bee543 has its CatchHandler @ 00aee990 */
          uVar17 = FUN_008bad20(lVar18 + 0x2f08,&local_d0,0,0,4,&local_a0);
          FUN_008b98b0(uVar17,0);
          if (local_80 == &local_a0) {
            lVar11 = 0x20;
            pppuVar16 = &local_a0;
LAB_00aee674:
            (**(code **)((long)*pppuVar16 + lVar11))();
          }
          else if (local_80 != (undefined ***)0x0) {
            lVar11 = 0x28;
            pppuVar16 = local_80;
            goto LAB_00aee674;
          }
          if (((ulong)local_d0 & 1) != 0) {
            _ZdlPv(local_c0);
          }
          if (((ulong)local_f0[0] & 1) != 0) {
                    /* try { // try from 00aee6ac to 00bee6b7 has its CatchHandler @ 00aee954 */
            _ZdlPv(local_e0);
          }
          if (((ulong)local_108[0] & 1) != 0) {
            _ZdlPv(local_f8);
          }
        }
LAB_00aee584:
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,0x327);
        FUN_008b6f70(uVar17,0);
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,3);
                    /* try { // try from 00aee5ac to 00bee5b3 has its CatchHandler @ 00aee978 */
        FUN_008b6f70(uVar17,0);
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,4);
        FUN_008b6f70(uVar17,0);
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,0x325);
        FUN_008b6f70(uVar17,0);
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,0x322);
        FUN_008b6f70(uVar17,0);
        uVar17 = FUN_008b7a20(lVar18 + 0x2f38,0x323);
        FUN_008b6f70(uVar17,0);
        uVar15 = FUN_00b096f8(lVar18 + 0x3d8);
        if ((uVar15 & 1) != 0) {
          uVar17 = FUN_008b7a20(lVar18 + 0x2f38,0x328);
                    /* try { // try from 00aee61c to 00bee62b has its CatchHandler @ 00aee98c */
          FUN_008b6f70(uVar17,0);
        }
      }
      else if (iVar10 == 1) {
        FUN_00851550();
        FUN_00ad0748();
      }
      else if (iVar10 == 0) {
        lVar11 = FUN_00851550();
        *(undefined1 *)(lVar11 + 0x33a5) = 0;
        FUN_00851550();
        FUN_00ad047c();
      }
LAB_00aee620:
      FUN_008b79a0(lVar18 + 0x2f38,0x321);
      FUN_008b79a0(lVar18 + 0x2f38,800);
    }
    else {
                    /* try { // try from 00aee408 to 00bee41b has its CatchHandler @ 00aee958 */
      if ((iVar9 == 3) && (iVar10 != -1)) {
        uVar17 = FUN_0047ad34();
        if (*(long *)(lVar3 + 0x28) == local_70) {
                    /* try { // try from 00aee434 to 00bee43f has its CatchHandler @ 00aee94c */
                    /* try { // try from 00aee440 to 00bee44b has its CatchHandler @ 00aee934 */
                    /* try { // try from 00aee44c to 00bee457 has its CatchHandler @ 00aee924 */
          FUN_0047ce14(uVar17,0xf,0);
          return;
        }
        goto LAB_00aee884;
      }
      if (iVar9 == 5) goto LAB_00aee620;
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_70) {
                    /* try { // try from 00aee660 to 00bee667 has its CatchHandler @ 00aee944 */
    return;
  }
LAB_00aee884:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
