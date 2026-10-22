# 00acdcf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acdcf4.md)

## 関数情報

~~~json
{
  "address": "00acdcf4",
  "name": "FUN_00acdcf4",
  "size": 1924,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3535afd9e4dbc002c21a1591f3a9f18a58e2cf63587e7d1a0ddca20170e12dd1",
  "source_text_sha256": "3535afd9e4dbc002c21a1591f3a9f18a58e2cf63587e7d1a0ddca20170e12dd1"
}
~~~
## 呼び出し元

- [0092e43c](../0092e/0092e43c.md)
- [00932074](../00932/00932074.md)
- [0093249c](../00932/0093249c.md)
- [00934148](../00934/00934148.md)
- [00934fe8](../00934/00934fe8.md)
- [00935ba4](../00935/00935ba4.md)
- [00a6731c](../00a67/00a6731c.md)
- [00a68ac0](../00a68/00a68ac0.md)
- [00a69030](../00a69/00a69030.md)

## 呼び出し先

- [0045b734](../0045b/0045b734.md)
- [0081f580](../0081f/0081f580.md)
- [008321a8](../00832/008321a8.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

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
## 疑似コード 1/1 / UTF-8 12721 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acdcf4(long param_1,uint param_2)

{
  long lVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  int iVar6;
  long lVar7;
  __shared_weak_count *p_Var8;
  __shared_weak_count *this;
  long lVar9;
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
  __shared_weak_count *p_Stack_48;
  long local_38;
  
  lVar3 = tpidr_el0;
  lVar1 = param_1 + 0xa8;
  local_38 = *(long *)(lVar3 + 0x28);
  lVar9 = (long)(int)param_2 * 0x10;
  if ((param_2 < 0x10) && (lVar7 = *(long *)(lVar1 + lVar9), lVar7 != 0)) goto LAB_00ace1c4;
  if ((int)param_2 < 4) {
    if ((int)param_2 < 2) {
      if (param_2 == 0) {
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
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img006_png_002a589c._0_8_;
        cStack_68 = SUB81(s_img006_png_002a589c._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_002a1772;
        acStack_82[0] = s_6_imgcut_002a1777[0];
        acStack_82[1] = s_6_imgcut_002a1777[1];
        acStack_82[2] = s_6_imgcut_002a1777[2];
        acStack_7f[0] = s_6_imgcut_002a1777[3];
        acStack_7f[1] = s_6_imgcut_002a1777[4];
        acStack_7f[2] = s_6_imgcut_002a1777[5];
        acStack_7f[3] = s_6_imgcut_002a1777[6];
        acStack_7f[4] = s_6_imgcut_002a1777[7];
        FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
      }
      else {
        if (param_2 != 1) goto LAB_00ace1c0;
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
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img007_png_00292b3b._0_8_;
        cStack_68 = SUB81(s_img007_png_00292b3b._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_002ab941;
        acStack_82[0] = s_7_imgcut_002ab946[0];
        acStack_82[1] = s_7_imgcut_002ab946[1];
        acStack_82[2] = s_7_imgcut_002ab946[2];
        acStack_7f[0] = s_7_imgcut_002ab946[3];
        acStack_7f[1] = s_7_imgcut_002ab946[4];
        acStack_7f[2] = s_7_imgcut_002ab946[5];
        acStack_7f[3] = s_7_imgcut_002ab946[6];
        acStack_7f[4] = s_7_imgcut_002ab946[7];
        FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
      }
      goto LAB_00ace148;
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
      p_Var8 = *(__shared_weak_count **)(param_1 + 0xd0);
      *(undefined8 *)(param_1 + 0xd0) = uVar5;
      *(undefined8 *)(param_1 + 200) = uVar4;
      if ((p_Var8 != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Var8 + 8), lVar7 == 0)) {
        (**(code **)(*(long *)p_Var8 + 0x10))(p_Var8);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var8);
      }
      p_Var8 = (__shared_weak_count *)
               CONCAT44(uStack_64,CONCAT13(uStack_65,CONCAT21(uStack_67,cStack_68)));
      if ((p_Var8 != (__shared_weak_count *)0x0) &&
         (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Var8 + 8), lVar7 == 0)) {
        (**(code **)(*(long *)p_Var8 + 0x10))(p_Var8);
        std::__ndk1::__shared_weak_count::__release_weak(p_Var8);
      }
    }
    else if (param_2 == 3) {
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
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img009_png_002a26f3._0_8_;
      cStack_68 = SUB81(s_img009_png_002a26f3._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_00295cb4;
      acStack_82[0] = s_9_imgcut_00295cb9[0];
      acStack_82[1] = s_9_imgcut_00295cb9[1];
      acStack_82[2] = s_9_imgcut_00295cb9[2];
      acStack_7f[0] = s_9_imgcut_00295cb9[3];
      acStack_7f[1] = s_9_imgcut_00295cb9[4];
      acStack_7f[2] = s_9_imgcut_00295cb9[5];
      acStack_7f[3] = s_9_imgcut_00295cb9[6];
      acStack_7f[4] = s_9_imgcut_00295cb9[7];
      FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
      goto LAB_00ace148;
    }
  }
  else {
    if ((int)param_2 < 0xf) {
      if (param_2 == 4) {
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
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img010_png_002abaa7._0_8_;
        cStack_68 = SUB81(s_img010_png_002abaa7._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_00295d93;
        acStack_82[0] = s_0_imgcut_00295d98[0];
        acStack_82[1] = s_0_imgcut_00295d98[1];
        acStack_82[2] = s_0_imgcut_00295d98[2];
        acStack_7f[0] = s_0_imgcut_00295d98[3];
        acStack_7f[1] = s_0_imgcut_00295d98[4];
        acStack_7f[2] = s_0_imgcut_00295d98[5];
        acStack_7f[3] = s_0_imgcut_00295d98[6];
        acStack_7f[4] = s_0_imgcut_00295d98[7];
        FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
      }
      else {
        if (param_2 != 5) goto LAB_00ace1c0;
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
        uStack_65 = 0;
        local_70 = 0x14;
        uStack_67 = 0x676e;
        local_88 = 0x1a;
        uStack_6f = (undefined7)s_img024_png_002adce0._0_8_;
        cStack_68 = SUB81(s_img024_png_002adce0._0_8_,7);
        local_7a = 0;
        local_87 = _DAT_00299f68;
        acStack_82[0] = s_4_imgcut_00299f6d[0];
        acStack_82[1] = s_4_imgcut_00299f6d[1];
        acStack_82[2] = s_4_imgcut_00299f6d[2];
        acStack_7f[0] = s_4_imgcut_00299f6d[3];
        acStack_7f[1] = s_4_imgcut_00299f6d[4];
        acStack_7f[2] = s_4_imgcut_00299f6d[5];
        acStack_7f[3] = s_4_imgcut_00299f6d[6];
        acStack_7f[4] = s_4_imgcut_00299f6d[7];
        FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
      }
    }
    else if (param_2 == 0xf) {
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
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img002_png_0029831d._0_8_;
      cStack_68 = SUB81(s_img002_png_0029831d._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_002a5e7e;
      acStack_82[0] = s_2_imgcut_002a5e83[0];
      acStack_82[1] = s_2_imgcut_002a5e83[1];
      acStack_82[2] = s_2_imgcut_002a5e83[2];
      acStack_7f[0] = s_2_imgcut_002a5e83[3];
      acStack_7f[1] = s_2_imgcut_002a5e83[4];
      acStack_7f[2] = s_2_imgcut_002a5e83[5];
      acStack_7f[3] = s_2_imgcut_002a5e83[6];
      acStack_7f[4] = s_2_imgcut_002a5e83[7];
      FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
    }
    else {
      if (param_2 != 0x15) goto LAB_00ace1c0;
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
      uStack_65 = 0;
      local_70 = 0x14;
      uStack_67 = 0x676e;
      local_88 = 0x1a;
      uStack_6f = (undefined7)s_img006_png_002a589c._0_8_;
      cStack_68 = SUB81(s_img006_png_002a589c._0_8_,7);
      local_7a = 0;
      local_87 = _DAT_002a1772;
      acStack_82[0] = s_6_imgcut_002a1777[0];
      acStack_82[1] = s_6_imgcut_002a1777[1];
      acStack_82[2] = s_6_imgcut_002a1777[2];
      acStack_7f[0] = s_6_imgcut_002a1777[3];
      acStack_7f[1] = s_6_imgcut_002a1777[4];
      acStack_7f[2] = s_6_imgcut_002a1777[5];
      acStack_7f[3] = s_6_imgcut_002a1777[6];
      acStack_7f[4] = s_6_imgcut_002a1777[7];
      FUN_0045b734(&local_50,&DAT_00c24f40,&local_70,&local_88,0x2601);
    }
LAB_00ace148:
    p_Var8 = p_Stack_48;
    uVar4 = local_50;
    puVar2 = (undefined8 *)(lVar1 + (long)(int)param_2 * 0x10);
    local_50 = 0;
    p_Stack_48 = (__shared_weak_count *)0x0;
    this = (__shared_weak_count *)puVar2[1];
    puVar2[1] = p_Var8;
    *puVar2 = uVar4;
    if ((this != (__shared_weak_count *)0x0) &&
       (lVar7 = FUN_00bd6d90(0xffffffffffffffff,this + 8), lVar7 == 0)) {
      (**(code **)(*(long *)this + 0x10))(this);
      std::__ndk1::__shared_weak_count::__release_weak(this);
    }
    p_Var8 = p_Stack_48;
    if ((p_Stack_48 != (__shared_weak_count *)0x0) &&
       (lVar7 = FUN_00bd6d90(0xffffffffffffffff,p_Stack_48 + 8), lVar7 == 0)) {
      (**(code **)(*(long *)p_Var8 + 0x10))(p_Var8);
      std::__ndk1::__shared_weak_count::__release_weak(p_Var8);
    }
    if ((local_88 & 1) != 0) {
      operator_delete(local_78);
    }
    if ((local_70 & 1) != 0) {
      operator_delete(local_60);
    }
  }
LAB_00ace1c0:
  lVar7 = *(long *)(lVar1 + lVar9);
LAB_00ace1c4:
                    /* try { // try from 00ace1d0 to 00bcee2f has its CatchHandler @ 00ace1d0
                       catch() { ... } // from try @ 00ace1d0 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00acee3c with catch @ 00ace1d0
                       catch() { ... } // from try @ 00acfd18 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad0358 with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad065c with catch @ 00ace1d0
                       catch() { ... } // from try @ 00ad084c with catch @ 00ace1d0 */
  if (*(long *)(lVar3 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(lVar7);
  }
  return;
}

~~~
