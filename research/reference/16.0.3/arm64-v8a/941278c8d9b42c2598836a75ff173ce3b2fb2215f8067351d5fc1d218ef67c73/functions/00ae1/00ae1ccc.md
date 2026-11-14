# 00ae1ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00ae1ccc",
  "name": "FUN_00ae1ccc",
  "size": 1240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aff7bef09f9b9300b90041133426ca68c21fdc8b7edb44f740e320d31a0c28b5",
  "source_text_sha256": "aff7bef09f9b9300b90041133426ca68c21fdc8b7edb44f740e320d31a0c28b5"
}
~~~

## 呼び出し元

- [0094826c](../00948/0094826c.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)

## 呼び出し先

- [0047e96c](../0047e/0047e96c.md)
- [0048d1b4](../0048d/0048d1b4.md)
- [00666154](../00666/00666154.md)
- [008b7f44](../008b7/008b7f44.md)
- [008b89cc](../008b8/008b89cc.md)
- [009e0634](../009e0/009e0634.md)
- [009e1fc0](../009e1/009e1fc0.md)
- [009e3f94](../009e3/009e3f94.md)
- [00ad0558](../00ad0/00ad0558.md)
- [00ad085c](../00ad0/00ad085c.md)
- [00ad7aec](../00ad7/00ad7aec.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58ed0](../00c58/00c58ed0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596b0](../00c59/00c596b0.md)

## 関連文字列（未確認候補）

~~~text
"uni.imgcut"
~~~

## 疑似コード / UTF-8 7795 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00ae1ccc(long param_1,int param_2)

{
  int *piVar1;
  long lVar2;
  byte *pbVar3;
  char cVar4;
  uint uVar5;
  int iVar6;
  uint uVar7;
  long lVar8;
  long *plVar9;
  int iVar10;
  ulong uVar11;
  long lVar12;
  undefined8 uVar13;
  undefined4 uVar14;
  long lVar15;
  undefined4 *puVar16;
  long lVar17;
  long lVar18;
  char *pcVar19;
  fde_table_entry *pfVar20;
  long *plVar21;
  byte local_e8 [11];
  undefined1 local_dd;
  void *local_d8;
  byte local_d0 [16];
  void *local_c0;
  byte local_b8 [8];
  undefined1 local_b0;
  void *local_a8;
  ulong local_a0;
  long *plStack_98;
  void *local_90;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
                    /* catch() { ... } // from try @ 00ae13e4 with catch @ 00ae1cdc */
                    /* catch() { ... } // from try @ 00ae159c with catch @ 00ae1ce8 */
                    /* catch() { ... } // from try @ 00ae1558 with catch @ 00ae1cec */
  lVar8 = tpidr_el0;
                    /* catch() { ... } // from try @ 00ae1628 with catch @ 00ae1cf0 */
                    /* catch() { ... } // from try @ 00ae16bc with catch @ 00ae1cf4 */
                    /* catch() { ... } // from try @ 00ae171c with catch @ 00ae1cf8 */
                    /* catch() { ... } // from try @ 00ae18bc with catch @ 00ae1cfc */
  piVar1 = (int *)((long)&QWORD_0039b978 + param_1 + 4);
                    /* catch() { ... } // from try @ 00ae1760 with catch @ 00ae1d00 */
  local_68 = *(long *)(lVar8 + 0x28);
  lVar18 = 0;
                    /* catch() { ... } // from try @ 00ae1a1c with catch @ 00ae1d18 */
  cVar4 = *(char *)((long)&fde_0039b980 + param_1);
  iVar10 = *piVar1 + param_2 + (int)cVar4;
  iVar6 = 0;
  if (cVar4 != 0) {
    iVar6 = iVar10 / (int)cVar4;
  }
                    /* catch() { ... } // from try @ 00ae1c5c with catch @ 00ae1d30
                       catch() { ... } // from try @ 00ae1c90 with catch @ 00ae1d30 */
  lVar2 = param_1 + 0xc5b8;
                    /* catch() { ... } // from try @ 00ae1c40 with catch @ 00ae1d38
                       catch() { ... } // from try @ 00ae1c78 with catch @ 00ae1d38 */
  *(undefined1 *)(param_1 + 0x11a4) = 1;
                    /* catch() { ... } // from try @ 00ae1938 with catch @ 00ae1d40 */
                    /* catch() { ... } // from try @ 00ae17e0 with catch @ 00ae1d44 */
  *piVar1 = iVar10 - iVar6 * cVar4;
  do {
    lVar17 = lVar18 + (long)*piVar1 * 0x2c;
    lVar15 = lVar2 + (long)*piVar1 * 0x2c;
    lVar12 = lVar2 + lVar17;
    uVar5 = (uint)(*(byte *)(lVar15 + 0x2a) ^ *(byte *)(lVar12 + 2)) << 0x10 |
            (uint)(*(byte *)(lVar15 + 0x2b) ^ *(byte *)(lVar12 + 3)) << 0x18 |
            (uint)(*(byte *)(lVar15 + 0x29) ^ *(byte *)(lVar12 + 1)) << 8 |
            (uint)(*(byte *)(lVar15 + 0x28) ^ *(byte *)(lVar2 + lVar17));
    uVar7 = uVar5 - 2;
    if ((int)uVar5 < 2) {
      uVar14 = 0;
    }
    else {
      uVar11 = FUN_009e1fc0(param_1 + 0x50,0xffffffff,0xffffffff);
      if ((((uVar11 & 1) == 0) ||
          (lVar12 = FUN_009e3f94(param_1 + 0x50,0xffffffff,0xffffffff), lVar12 == 0)) ||
         (lVar12 = FUN_009e0634(lVar12,uVar7), lVar12 == 0)) {
        puVar16 = (undefined4 *)(param_1 + 0x49934 + (ulong)uVar7 * 4);
      }
      else {
        puVar16 = (undefined4 *)(lVar12 + 4);
      }
      uVar14 = *puVar16;
    }
    *(undefined4 *)((long)&fde_table_entry_003339b8.initial_loc + lVar18 + param_1) = uVar14;
    lVar18 = lVar18 + 4;
  } while (lVar18 != 0x28);
  if (DAT_00ca5a38 == 0) {
    lVar18 = 0;
  }
  else {
    lVar18 = __dynamic_cast(DAT_00ca5a38,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c66ef8,
                            &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8e9f0,0);
  }
  lVar12 = 0;
  pfVar20 = &fde_table_entry_003339b8;
  pcVar19 = (char *)((ulong)local_e8 | 1);
  lVar15 = 0xc5b8;
  do {
    lVar17 = lVar2 + (long)*piVar1 * 0x2c;
    pbVar3 = (byte *)(param_1 + lVar15 + (long)*piVar1 * 0x2c);
    uVar5 = (uint)(*(byte *)(lVar17 + 0x2a) ^ pbVar3[2]) << 0x10 |
            (uint)(*(byte *)(lVar17 + 0x2b) ^ pbVar3[3]) << 0x18 |
            (uint)(*(byte *)(lVar17 + 0x29) ^ pbVar3[1]) << 8 |
            (uint)(*(byte *)(lVar17 + 0x28) ^ *pbVar3);
    if (uVar5 == 0xffffffff) {
      if (((DAT_00ca5ff8 & 1) == 0) && (iVar10 = __cxa_guard_acquire(&DAT_00ca5ff8), iVar10 != 0)) {
        DAT_00ca5fc8 = 0;
        DAT_00ca5fc0 = &DAT_00ca5fc8;
        DAT_00ca5fe8 = 0;
        DAT_00ca5ff0 = 0;
        DAT_00ca5fe0 = 0;
        DAT_00ca5fd0 = 0;
        DAT_00ca5fd8 = &DAT_00ca5fe0;
        __cxa_atexit(FUN_0047f114,&DAT_00ca5fc0,&PTR_LOOP_00c64030);
        __cxa_guard_release(&DAT_00ca5ff8);
      }
      local_b0 = 0;
      local_b8[0] = 0xe;
      *(undefined4 *)((ulong)local_b8 | 1) = 0x2e696e75;
      *(undefined4 *)((long)((ulong)local_b8 | 1) + 3) = 0x676e702e;
      FUN_0048d1b4(&local_a0,local_b8);
      uVar13 = s_uni_imgcut_002caba4._0_8_;
      local_dd = 0;
      local_e8[0] = 0x14;
      pcVar19[8] = 'u';
      pcVar19[9] = 't';
      *(undefined8 *)pcVar19 = uVar13;
      FUN_0048d1b4(local_d0,local_e8);
      FUN_0047e96c(&local_80,&DAT_00ca5fc0,&local_a0,local_d0,0x2601);
      plVar9 = plStack_78;
      uVar13 = local_80;
      local_80 = 0;
      plStack_78 = (long *)0x0;
      lVar17 = lVar18 + lVar12;
      plVar21 = *(long **)(lVar17 + 0x348);
      *(long **)(lVar17 + 0x348) = plVar9;
      *(undefined8 *)(lVar17 + 0x340) = uVar13;
      plVar9 = plStack_78;
      if ((plVar21 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar21 + 1), plVar9 = plStack_78, lVar17 == 0))
      {
        (**(code **)(*plVar21 + 0x10))(plVar21);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar21);
        plVar9 = plStack_78;
      }
      plStack_78 = plVar9;
      if ((plVar9 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar17 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      if ((local_d0[0] & 1) != 0) {
        _ZdlPv(local_c0);
      }
      if ((local_e8[0] & 1) != 0) {
        _ZdlPv(local_d8);
      }
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
      if ((local_b8[0] & 1) != 0) {
        _ZdlPv(local_a8);
      }
    }
    else {
      FUN_00666154(&local_a0,uVar5 - 2,*(undefined4 *)((long)&pfVar20->initial_loc + param_1),0);
      plVar9 = plStack_98;
      uVar11 = local_a0;
      local_a0 = 0;
      plStack_98 = (long *)0x0;
      lVar17 = lVar18 + lVar12;
      plVar21 = *(long **)(lVar17 + 0x348);
      *(long **)(lVar17 + 0x348) = plVar9;
      *(ulong *)(lVar17 + 0x340) = uVar11;
      plVar9 = plStack_98;
      if ((plVar21 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar21 + 1), plVar9 = plStack_98, lVar17 == 0))
      {
        (**(code **)(*plVar21 + 0x10))(plVar21);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar21);
        plVar9 = plStack_98;
      }
      plStack_98 = plVar9;
      if ((plVar9 != (long *)0x0) &&
         (lVar17 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar17 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
    }
    lVar12 = lVar12 + 0x10;
    pfVar20 = (fde_table_entry *)&pfVar20->data_loc;
    lVar15 = lVar15 + 4;
  } while (lVar12 != 0xa0);
  FUN_00ad085c(lVar18);
  FUN_00ad0558(param_1);
  uVar13 = FUN_008b89cc(param_1 + 0x2f38,0x324);
  iVar10 = FUN_00ad7aec(param_1);
  FUN_008b7f44(uVar13,iVar10 == 3);
  if (*(long *)(lVar8 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
