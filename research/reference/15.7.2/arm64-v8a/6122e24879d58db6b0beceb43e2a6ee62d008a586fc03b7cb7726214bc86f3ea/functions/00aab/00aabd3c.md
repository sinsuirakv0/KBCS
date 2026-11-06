# 00aabd3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00aabd3c",
  "name": "FUN_00aabd3c",
  "size": 1164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba93b90c370b5ae14008eaeb6a90fde7690019dfc276752ae97f42c3f2558129",
  "source_text_sha256": "ba93b90c370b5ae14008eaeb6a90fde7690019dfc276752ae97f42c3f2558129"
}
~~~

## 呼び出し元

- [00aab67c](../00aab/00aab67c.md)
- [00aad8d8](../00aad/00aad8d8.md)
- [00aada14](../00aad/00aada14.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [004253b4](../00425/004253b4.md)
- [0045b734](../0045b/0045b734.md)
- [00469f7c](../00469/00469f7c.md)
- [0063fa4c](../0063f/0063fa4c.md)
- [0081f580](../0081f/0081f580.md)
- [00883d2c](../00883/00883d2c.md)
- [008847e4](../00884/008847e4.md)
- [00a25194](../00a25/00a25194.md)
- [00a25380](../00a25/00a25380.md)
- [00aab3c0](../00aab/00aab3c0.md)
- [00aab518](../00aab/00aab518.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"array::at"
"backstage_reset1"
"uni.imgcut"
~~~

## 疑似コード / UTF-8 5984 bytes

~~~c

void FUN_00aabd3c(long param_1,long param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long *plVar5;
  int iVar6;
  long *plVar7;
  long lVar8;
  undefined8 uVar9;
  uint uVar10;
  ulong uVar11;
  long lVar12;
  long *plVar13;
  long *plVar14;
  undefined8 *puVar15;
  long lVar16;
  char *pcVar17;
  byte local_b0;
  undefined7 uStack_af;
  char cStack_a8;
  undefined7 uStack_a7;
  char local_a0;
  undefined1 uStack_9f;
  undefined6 uStack_9e;
  byte local_98 [11];
  undefined1 local_8d;
  void *local_88;
  ulong local_80;
  long *plStack_78;
  void *local_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  *(undefined4 *)(param_1 + 0x48) = param_3;
  plVar7 = (long *)FUN_00aab518(param_1,param_3,0xffffffff,0,0);
  lVar8 = *plVar7;
  if (plVar7[1] == lVar8) {
    uVar11 = 0;
  }
  else {
    lVar12 = 0;
    plVar14 = (long *)(param_2 + 8);
    lVar16 = -10;
    do {
      FUN_0063fa4c(&local_80,*(undefined4 *)(lVar8 + lVar12),((undefined4 *)(lVar8 + lVar12))[1],0);
      plVar5 = plStack_78;
      uVar11 = local_80;
      if (lVar16 == 0) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      plVar13 = (long *)*plVar14;
      local_80 = 0;
      plStack_78 = (long *)0x0;
      *plVar14 = (long)plVar5;
      plVar14[-1] = uVar11;
      plVar5 = plStack_78;
      if ((plVar13 != (long *)0x0) &&
         (lVar8 = FUN_00bd6d90(0xffffffffffffffff,plVar13 + 1), plVar5 = plStack_78, lVar8 == 0)) {
        (**(code **)(*plVar13 + 0x10))(plVar13);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
        plVar5 = plStack_78;
      }
      plStack_78 = plVar5;
      if ((plVar5 != (long *)0x0) &&
         (lVar8 = FUN_00bd6d90(0xffffffffffffffff,plVar5 + 1), lVar8 == 0)) {
        (**(code **)(*plVar5 + 0x10))(plVar5);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
      }
      lVar8 = *plVar7;
      uVar1 = lVar16 + 0xb;
      lVar16 = lVar16 + 1;
      plVar14 = plVar14 + 2;
      lVar12 = lVar12 + 8;
      uVar11 = plVar7[1] - lVar8 >> 3;
    } while (uVar1 < uVar11);
  }
  uVar9 = s_uni_imgcut_002a77c6._0_8_;
  uVar10 = (uint)uVar11;
  if ((int)uVar10 < 10) {
    if (uVar10 < 0xb) {
      uVar10 = 10;
    }
    pcVar17 = (char *)((ulong)local_98 | 1);
    lVar8 = -(uVar11 & 0xffffffff);
    puVar15 = (undefined8 *)(param_2 + (uVar11 & 0xffffffff) * 0x10 + 8);
    do {
      if (((DAT_00c24f78 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c24f78), iVar6 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      plStack_78 = (long *)((ulong)plStack_78 & 0xffffffffffffff00);
      local_80 = CONCAT71(local_80._1_7_,0xe);
      local_98[0] = 0x14;
      *(undefined4 *)((ulong)&local_80 | 1) = 0x2e696e75;
      *(undefined4 *)((long)((ulong)&local_80 | 1) + 3) = 0x676e702e;
      pcVar17[8] = 'u';
      pcVar17[9] = 't';
      *(undefined8 *)pcVar17 = uVar9;
      local_8d = 0;
      FUN_0045b734(&local_b0,&DAT_00c24f40,&local_80,local_98,0x2601);
      if (-(ulong)uVar10 == lVar8) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      uVar4 = CONCAT71(uStack_a7,cStack_a8);
      uVar3 = CONCAT71(uStack_af,local_b0);
      plVar7 = (long *)*puVar15;
      local_b0 = 0;
      uStack_af = 0;
      cStack_a8 = '\0';
      uStack_a7 = 0;
      *puVar15 = uVar4;
      puVar15[-1] = uVar3;
      if ((plVar7 == (long *)0x0) ||
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), lVar16 != 0)) {
        plVar7 = (long *)CONCAT71(uStack_a7,cStack_a8);
      }
      else {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        plVar7 = (long *)CONCAT71(uStack_a7,cStack_a8);
      }
      if ((plVar7 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), lVar16 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      if ((local_98[0] & 1) != 0) {
        _ZdlPv(local_88);
      }
      if ((local_80 & 1) != 0) {
        _ZdlPv(local_70);
      }
      lVar8 = lVar8 + -1;
      puVar15 = puVar15 + 2;
    } while (lVar8 != -10);
  }
  lVar8 = FUN_0081f580();
  uVar9 = FUN_008847e4(lVar8 + 0x2e48,0x329);
  iVar6 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar9,1 < iVar6);
  lVar8 = FUN_0081f580();
  uVar9 = FUN_008847e4(lVar8 + 0x2e48,0x32a);
  iVar6 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar9,1 < iVar6);
  lVar8 = FUN_0081f580();
  FUN_00a25194(lVar8 + 0x2f88,0x66);
  lVar8 = FUN_0081f580();
  uStack_9f = 0;
  local_b0 = 0x20;
  uStack_a7 = (undefined7)s_backstage_reset1_002951bc._8_8_;
  local_a0 = SUB81(s_backstage_reset1_002951bc._8_8_,7);
  uStack_af = (undefined7)s_backstage_reset1_002951bc._0_8_;
  cStack_a8 = SUB81(s_backstage_reset1_002951bc._0_8_,7);
  FUN_00469f7c(local_98,&local_b0);
  FUN_004253b4(&local_80,local_98,0,*(int *)(param_1 + 0x48) + 1);
  FUN_00a25380(lVar8 + 0x2f88,0x66,&local_80,0x1e,0);
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    _ZdlPv(local_88);
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_9e,CONCAT11(uStack_9f,local_a0)));
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
LAB_00aac28c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
