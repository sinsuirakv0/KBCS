# 00acddbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acddbc",
  "name": "FUN_00acddbc",
  "size": 1924,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c0d01a028e3e1109b55b8c45c1274be226d2e14db90ea0f7305b7ffdc2dd64e",
  "source_text_sha256": "2c0d01a028e3e1109b55b8c45c1274be226d2e14db90ea0f7305b7ffdc2dd64e"
}
~~~

## 呼び出し元

- [0092e43c](../0092e/0092e43c.md)
- [0093249c](../00932/0093249c.md)
- [0093c1ac](../0093c/0093c1ac.md)
- [00a6731c](../00a67/00a6731c.md)
- [00a68ac0](../00a68/00a68ac0.md)
- [00a69030](../00a69/00a69030.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0081f580](../0081f/0081f580.md)
- [008321a8](../00832/008321a8.md)
- [00bd6e50](../00bd6/00bd6e50.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdafb0](../00bda/00bdafb0.md)
- [00bdafd0](../00bda/00bdafd0.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"0.imgcut"
"2.imgcut"
"4.imgcut"
"6.imgcut"
"7.imgcut"
"9.imgcut"
"img002.imgcut"
"img002.png"
"img006.imgcut"
"img006.png"
"img007.imgcut"
"img007.png"
"img009.imgcut"
"img009.png"
"img010.imgcut"
"img010.png"
"img024.imgcut"
"img024.png"
~~~

## 疑似コード / UTF-8 12190 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acddbc(long param_1,uint param_2)

{
  long lVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  int iVar6;
  long lVar7;
  long *plVar8;
  long *plVar9;
  long lVar10;
  byte local_88;
  undefined5 local_87;
  char acStack_82 [3];
  char acStack_7f [5];
  undefined1 local_7a;
  void *local_78;
  byte local_70;
  undefined7 uStack_6f;
  char cStack_68;
  undefined2 uStack_67;
  undefined1 uStack_65;
  undefined4 uStack_64;
  void *local_60;
  undefined8 local_50;
  long *plStack_48;
  long local_38;
  
  lVar3 = tpidr_el0;
  lVar1 = param_1 + 0xa8;
  local_38 = *(long *)(lVar3 + 0x28);
  lVar10 = (long)(int)param_2 * 0x10;
  if ((param_2 < 0x10) && (lVar7 = *(long *)(lVar1 + lVar10), lVar7 != 0)) goto LAB_00ace28c;
  if ((int)param_2 < 4) {
    if ((int)param_2 < 2) {
      if (param_2 == 0) {
        if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
          DAT_00c25008 = 0;
          DAT_00c25000 = &DAT_00c25008;
          DAT_00c25028 = 0;
          DAT_00c25030 = 0;
          DAT_00c25020 = 0;
          DAT_00c25010 = 0;
          DAT_00c25018 = &DAT_00c25020;
          __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
          __cxa_guard_release(&DAT_00c25038);
        }
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img006_png_002a5895._0_8_;
        cStack_68 = SUB81(s_img006_png_002a5895._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_002a17ff;
        acStack_82[0] = s_6_imgcut_002a1804[0];
        acStack_82[1] = s_6_imgcut_002a1804[1];
        acStack_82[2] = s_6_imgcut_002a1804[2];
        acStack_7f[0] = s_6_imgcut_002a1804[3];
        acStack_7f[1] = s_6_imgcut_002a1804[4];
        acStack_7f[2] = s_6_imgcut_002a1804[5];
        acStack_7f[3] = s_6_imgcut_002a1804[6];
        acStack_7f[4] = s_6_imgcut_002a1804[7];
        FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
      }
      else {
        if (param_2 != 1) goto LAB_00ace288;
        if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
          DAT_00c25008 = 0;
          DAT_00c25000 = &DAT_00c25008;
          DAT_00c25028 = 0;
          DAT_00c25030 = 0;
          DAT_00c25020 = 0;
          DAT_00c25010 = 0;
          DAT_00c25018 = &DAT_00c25020;
          __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
          __cxa_guard_release(&DAT_00c25038);
        }
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img007_png_00292bc8._0_8_;
        cStack_68 = SUB81(s_img007_png_00292bc8._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_002ab947;
        acStack_82[0] = s_7_imgcut_002ab94c[0];
        acStack_82[1] = s_7_imgcut_002ab94c[1];
        acStack_82[2] = s_7_imgcut_002ab94c[2];
        acStack_7f[0] = s_7_imgcut_002ab94c[3];
        acStack_7f[1] = s_7_imgcut_002ab94c[4];
        acStack_7f[2] = s_7_imgcut_002ab94c[5];
        acStack_7f[3] = s_7_imgcut_002ab94c[6];
        acStack_7f[4] = s_7_imgcut_002ab94c[7];
        FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
      }
      goto LAB_00ace210;
    }
    if (param_2 == 2) {
      FUN_0081f580();
      FUN_008321a8(&local_70);
      uVar5 = CONCAT44(uStack_64,CONCAT13(uStack_65,CONCAT21(uStack_67,cStack_68)));
      uVar4 = CONCAT71(uStack_6f,local_70);
      local_70 = 0;
      uStack_6f = 0;
      cStack_68 = '\0';
      uStack_67 = 0;
      uStack_65 = 0;
      uStack_64 = 0;
      plVar8 = *(long **)(param_1 + 0xd0);
      *(undefined8 *)(param_1 + 0xd0) = uVar5;
      *(undefined8 *)(param_1 + 200) = uVar4;
      if ((plVar8 != (long *)0x0) &&
         (lVar7 = FUN_00bd6e50(0xffffffffffffffff,plVar8 + 1), lVar7 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
      plVar8 = (long *)CONCAT44(uStack_64,CONCAT13(uStack_65,CONCAT21(uStack_67,cStack_68)));
      if ((plVar8 != (long *)0x0) &&
         (lVar7 = FUN_00bd6e50(0xffffffffffffffff,plVar8 + 1), lVar7 == 0)) {
        (**(code **)(*plVar8 + 0x10))(plVar8);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
      }
    }
    else if (param_2 == 3) {
      if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
        DAT_00c25008 = 0;
        DAT_00c25000 = &DAT_00c25008;
        DAT_00c25028 = 0;
        DAT_00c25030 = 0;
        DAT_00c25020 = 0;
        DAT_00c25010 = 0;
        DAT_00c25018 = &DAT_00c25020;
        __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
        __cxa_guard_release(&DAT_00c25038);
      }
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img009_png_002a26ec._0_8_;
      cStack_68 = SUB81(s_img009_png_002a26ec._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_00295d41;
      acStack_82[0] = s_9_imgcut_00295d46[0];
      acStack_82[1] = s_9_imgcut_00295d46[1];
      acStack_82[2] = s_9_imgcut_00295d46[2];
      acStack_7f[0] = s_9_imgcut_00295d46[3];
      acStack_7f[1] = s_9_imgcut_00295d46[4];
      acStack_7f[2] = s_9_imgcut_00295d46[5];
      acStack_7f[3] = s_9_imgcut_00295d46[6];
      acStack_7f[4] = s_9_imgcut_00295d46[7];
      FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
      goto LAB_00ace210;
    }
  }
  else {
    if ((int)param_2 < 0xf) {
      if (param_2 == 4) {
        if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
          DAT_00c25008 = 0;
          DAT_00c25000 = &DAT_00c25008;
          DAT_00c25028 = 0;
          DAT_00c25030 = 0;
          DAT_00c25020 = 0;
          DAT_00c25010 = 0;
          DAT_00c25018 = &DAT_00c25020;
          __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
          __cxa_guard_release(&DAT_00c25038);
        }
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img010_png_002abaad._0_8_;
        cStack_68 = SUB81(s_img010_png_002abaad._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_00295e20;
        acStack_82[0] = s_0_imgcut_00295e25[0];
        acStack_82[1] = s_0_imgcut_00295e25[1];
        acStack_82[2] = s_0_imgcut_00295e25[2];
        acStack_7f[0] = s_0_imgcut_00295e25[3];
        acStack_7f[1] = s_0_imgcut_00295e25[4];
        acStack_7f[2] = s_0_imgcut_00295e25[5];
        acStack_7f[3] = s_0_imgcut_00295e25[6];
        acStack_7f[4] = s_0_imgcut_00295e25[7];
        FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
      }
      else {
        if (param_2 != 5) goto LAB_00ace288;
        if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
          DAT_00c25008 = 0;
          DAT_00c25000 = &DAT_00c25008;
          DAT_00c25028 = 0;
          DAT_00c25030 = 0;
          DAT_00c25020 = 0;
          DAT_00c25010 = 0;
          DAT_00c25018 = &DAT_00c25020;
          __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
          __cxa_guard_release(&DAT_00c25038);
        }
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img024_png_002adc4c._0_8_;
        cStack_68 = SUB81(s_img024_png_002adc4c._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_00299ff5;
        acStack_82[0] = s_4_imgcut_00299ffa[0];
        acStack_82[1] = s_4_imgcut_00299ffa[1];
        acStack_82[2] = s_4_imgcut_00299ffa[2];
        acStack_7f[0] = s_4_imgcut_00299ffa[3];
        acStack_7f[1] = s_4_imgcut_00299ffa[4];
        acStack_7f[2] = s_4_imgcut_00299ffa[5];
        acStack_7f[3] = s_4_imgcut_00299ffa[6];
        acStack_7f[4] = s_4_imgcut_00299ffa[7];
        FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
      }
    }
    else if (param_2 == 0xf) {
      if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
        DAT_00c25008 = 0;
        DAT_00c25000 = &DAT_00c25008;
        DAT_00c25028 = 0;
        DAT_00c25030 = 0;
        DAT_00c25020 = 0;
        DAT_00c25010 = 0;
        DAT_00c25018 = &DAT_00c25020;
        __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
        __cxa_guard_release(&DAT_00c25038);
      }
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
                    /* try { // try from 00ace1d0 to 00bcee2f has its CatchHandler @ 00ace1d0
                       catch() { ... } // from try @ 00ace1d0 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00acee3c with catch @ 00ace1d0
                       catch() { ... } // from try @ 00acfd18 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad0358 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad065c with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad084c with catch @ 00ace1d0 */
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img002_png_002983aa._0_8_;
      cStack_68 = SUB81(s_img002_png_002983aa._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_002a5e77;
      acStack_82[0] = s_2_imgcut_002a5e7c[0];
      acStack_82[1] = s_2_imgcut_002a5e7c[1];
      acStack_82[2] = s_2_imgcut_002a5e7c[2];
      acStack_7f[0] = s_2_imgcut_002a5e7c[3];
      acStack_7f[1] = s_2_imgcut_002a5e7c[4];
      acStack_7f[2] = s_2_imgcut_002a5e7c[5];
      acStack_7f[3] = s_2_imgcut_002a5e7c[6];
      acStack_7f[4] = s_2_imgcut_002a5e7c[7];
      FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
    }
    else {
      if (param_2 != 0x15) goto LAB_00ace288;
      if (((DAT_00c25038 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c25038), iVar6 != 0)) {
        DAT_00c25008 = 0;
        DAT_00c25000 = &DAT_00c25008;
        DAT_00c25028 = 0;
        DAT_00c25030 = 0;
        DAT_00c25020 = 0;
        DAT_00c25010 = 0;
        DAT_00c25018 = &DAT_00c25020;
        __cxa_atexit(FUN_0045bedc,&DAT_00c25000,&PTR_LOOP_00be5f80);
        __cxa_guard_release(&DAT_00c25038);
      }
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img006_png_002a5895._0_8_;
      cStack_68 = SUB81(s_img006_png_002a5895._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_002a17ff;
      acStack_82[0] = s_6_imgcut_002a1804[0];
      acStack_82[1] = s_6_imgcut_002a1804[1];
      acStack_82[2] = s_6_imgcut_002a1804[2];
      acStack_7f[0] = s_6_imgcut_002a1804[3];
      acStack_7f[1] = s_6_imgcut_002a1804[4];
      acStack_7f[2] = s_6_imgcut_002a1804[5];
      acStack_7f[3] = s_6_imgcut_002a1804[6];
      acStack_7f[4] = s_6_imgcut_002a1804[7];
      FUN_0045b734(&local_50,&DAT_00c25000,&local_70,&local_88,0x2601);
    }
LAB_00ace210:
    plVar8 = plStack_48;
    uVar4 = local_50;
    puVar2 = (undefined8 *)(lVar1 + (long)(int)param_2 * 0x10);
    local_50 = 0;
    plStack_48 = (long *)0x0;
    plVar9 = (long *)puVar2[1];
    puVar2[1] = plVar8;
    *puVar2 = uVar4;
    if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00bd6e50(0xffffffffffffffff,plVar9 + 1), lVar7 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    plVar8 = plStack_48;
    if ((plStack_48 != (long *)0x0) &&
       (lVar7 = FUN_00bd6e50(0xffffffffffffffff,plStack_48 + 1), lVar7 == 0)) {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    if ((local_88 & 1) != 0) {
      _ZdlPv(local_78);
    }
    if ((local_70 & 1) != 0) {
      _ZdlPv(local_60);
    }
  }
LAB_00ace288:
  lVar7 = *(long *)(lVar1 + lVar10);
LAB_00ace28c:
  if (*(long *)(lVar3 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(lVar7);
  }
  return;
}

~~~
