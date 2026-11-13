# 006aabac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006aabac",
  "name": "FUN_006aabac",
  "size": 1452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b24f30f72b734d58db7252e990b8923fa0baeb5d9229a5c138b1bdf7220f0de1",
  "source_text_sha256": "b24f30f72b734d58db7252e990b8923fa0baeb5d9229a5c138b1bdf7220f0de1"
}
~~~

## 呼び出し元

- [006ac970](../006ac/006ac970.md)

## 呼び出し先

- [0047e64c](../0047e/0047e64c.md)
- [00851550](../00851/00851550.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 関連文字列（未確認候補）

~~~text
"2.imgcut"
"3.imgcut"
"7.imgcut"
"img022.imgcut"
"img022.png"
"img023.imgcut"
"img023.png"
"img027.imgcut"
"img027.png"
~~~

## 疑似コード / UTF-8 11244 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_006aabac(void)

{
  long lVar1;
  undefined8 uVar2;
  long *plVar3;
  int iVar4;
  long lVar5;
  long lVar6;
  long *plVar7;
  byte local_90;
  undefined5 local_8f;
  char acStack_8a [3];
  char acStack_87 [5];
  undefined1 local_82;
  void *local_80;
  byte local_78;
  char local_77 [8];
  undefined2 local_6f;
  undefined1 local_6d;
  void *local_68;
  undefined8 local_60;
  long *plStack_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  if (DAT_00ca4a78 == 0) {
    lVar5 = 0;
  }
  else {
    lVar5 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c71290,0);
  }
  lVar6 = FUN_00851550();
  if (*(int *)((long)&fde_table_entry_00333fc8.data_loc + lVar6) == 0) {
    if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
                    /* catch() { ... } // from try @ 006aafc8 with catch @ 006ab0ec */
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
    local_6d = 0;
    local_78 = 0x14;
    local_6f = 0x676e;
    local_90 = 0x1a;
    local_77[0] = s_img022_png_002a032e[0];
    local_77[1] = s_img022_png_002a032e[1];
    local_77[2] = s_img022_png_002a032e[2];
    local_77[3] = s_img022_png_002a032e[3];
    local_77[4] = s_img022_png_002a032e[4];
    local_77[5] = s_img022_png_002a032e[5];
    local_77[6] = s_img022_png_002a032e[6];
    local_77[7] = s_img022_png_002a032e[7];
    local_82 = 0;
    local_8f = _DAT_002c1528;
    acStack_8a[0] = s_2_imgcut_002c152d[0];
    acStack_8a[1] = s_2_imgcut_002c152d[1];
    acStack_8a[2] = s_2_imgcut_002c152d[2];
    acStack_87[0] = s_2_imgcut_002c152d[3];
    acStack_87[1] = s_2_imgcut_002c152d[4];
    acStack_87[2] = s_2_imgcut_002c152d[5];
    acStack_87[3] = s_2_imgcut_002c152d[6];
    acStack_87[4] = s_2_imgcut_002c152d[7];
    FUN_0047e64c(&local_60,&DAT_00ca5000,&local_78,&local_90,0x2601);
    plVar3 = plStack_58;
    uVar2 = local_60;
    plVar7 = *(long **)(lVar5 + 0x120);
    local_60 = 0;
    plStack_58 = (long *)0x0;
    *(long **)(lVar5 + 0x120) = plVar3;
    *(undefined8 *)(lVar5 + 0x118) = uVar2;
    if ((plVar7 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar6 == 0)
       ) {
                    /* catch() { ... } // from try @ 006aacf0 with catch @ 006aadcc */
      (**(code **)(*plVar7 + 0x10))(plVar7);
                    /* catch() { ... } // from try @ 006aacd0 with catch @ 006aade0 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    }
    plVar3 = plStack_58;
                    /* catch() { ... } // from try @ 006aa90c with catch @ 006aade8 */
                    /* catch() { ... } // from try @ 006aac98 with catch @ 006aadf8 */
    if ((plStack_58 != (long *)0x0) &&
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,plStack_58 + 1), lVar6 == 0)) {
                    /* catch() { ... } // from try @ 006aac44 with catch @ 006aadfc */
                    /* catch() { ... } // from try @ 006aaabc with catch @ 006aae00 */
                    /* catch() { ... } // from try @ 006aaa60 with catch @ 006aae04 */
                    /* catch() { ... } // from try @ 006aaa0c with catch @ 006aae08 */
      (**(code **)(*plVar3 + 0x10))(plVar3);
                    /* catch() { ... } // from try @ 006aa988 with catch @ 006aae0c */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
    }
    if ((local_90 & 1) != 0) {
                    /* catch() { ... } // from try @ 006aa84c with catch @ 006aaeb8 */
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
                    /* catch() { ... } // from try @ 006aaf84 with catch @ 006ab10c */
    if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
                    /* catch() { ... } // from try @ 006aaf58 with catch @ 006ab12c */
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
    local_6d = 0;
    local_78 = 0x14;
    local_6f = 0x676e;
    local_90 = 0x1a;
    local_77[0] = s_img023_png_002a33e0[0];
    local_77[1] = s_img023_png_002a33e0[1];
    local_77[2] = s_img023_png_002a33e0[2];
    local_77[3] = s_img023_png_002a33e0[3];
    local_77[4] = s_img023_png_002a33e0[4];
    local_77[5] = s_img023_png_002a33e0[5];
    local_77[6] = s_img023_png_002a33e0[6];
    local_77[7] = s_img023_png_002a33e0[7];
    local_82 = 0;
    local_8f = _DAT_0029f27b;
    acStack_8a[0] = s_3_imgcut_0029f280[0];
    acStack_8a[1] = s_3_imgcut_0029f280[1];
    acStack_8a[2] = s_3_imgcut_0029f280[2];
    acStack_87[0] = s_3_imgcut_0029f280[3];
    acStack_87[1] = s_3_imgcut_0029f280[4];
    acStack_87[2] = s_3_imgcut_0029f280[5];
    acStack_87[3] = s_3_imgcut_0029f280[6];
    acStack_87[4] = s_3_imgcut_0029f280[7];
                    /* try { // try from 006aaf24 to 007aaf57 has its CatchHandler @ 006aaf24
                       catch() { ... } // from try @ 006aaf24 with catch @ 006aaf24
                       catch() { ... } // from try @ 006aaff8 with catch @ 006aaf24 */
    FUN_0047e64c(&local_60,&DAT_00ca5000,&local_78,&local_90,0x2601);
  }
  else {
    lVar6 = FUN_00851550();
    if (*(int *)((long)&fde_table_entry_00333fc8.data_loc + lVar6) < 1) goto LAB_006aafb0;
    if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
                    /* try { // try from 006aac44 to 007aac67 has its CatchHandler @ 006aadfc */
    local_6d = 0;
    local_78 = 0x14;
    local_6f = 0x676e;
    local_90 = 0x1a;
    local_77[0] = s_img022_png_002a032e[0];
    local_77[1] = s_img022_png_002a032e[1];
    local_77[2] = s_img022_png_002a032e[2];
    local_77[3] = s_img022_png_002a032e[3];
    local_77[4] = s_img022_png_002a032e[4];
    local_77[5] = s_img022_png_002a032e[5];
    local_77[6] = s_img022_png_002a032e[6];
    local_77[7] = s_img022_png_002a032e[7];
    local_82 = 0;
    local_8f = _DAT_002c1528;
    acStack_8a[0] = s_2_imgcut_002c152d[0];
    acStack_8a[1] = s_2_imgcut_002c152d[1];
    acStack_8a[2] = s_2_imgcut_002c152d[2];
    acStack_87[0] = s_2_imgcut_002c152d[3];
    acStack_87[1] = s_2_imgcut_002c152d[4];
    acStack_87[2] = s_2_imgcut_002c152d[5];
    acStack_87[3] = s_2_imgcut_002c152d[6];
    acStack_87[4] = s_2_imgcut_002c152d[7];
                    /* try { // try from 006aac98 to 007aacbb has its CatchHandler @ 006aadf8 */
    FUN_0047e64c(&local_60,&DAT_00ca5000,&local_78,&local_90,0x2601);
    plVar3 = plStack_58;
    uVar2 = local_60;
    plVar7 = *(long **)(lVar5 + 0x120);
    local_60 = 0;
    plStack_58 = (long *)0x0;
    *(long **)(lVar5 + 0x120) = plVar3;
    *(undefined8 *)(lVar5 + 0x118) = uVar2;
    if ((plVar7 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar6 == 0)
       ) {
                    /* try { // try from 006aacd0 to 007aacd7 has its CatchHandler @ 006aade0 */
      (**(code **)(*plVar7 + 0x10))(plVar7);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
    }
    plVar3 = plStack_58;
                    /* try { // try from 006aacf0 to 007aad23 has its CatchHandler @ 006aadcc */
    if ((plStack_58 != (long *)0x0) &&
       (lVar6 = FUN_00c53da0(0xffffffffffffffff,plStack_58 + 1), lVar6 == 0)) {
      (**(code **)(*plVar3 + 0x10))(plVar3);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
    }
    if ((local_90 & 1) != 0) {
      _ZdlPv(local_80);
    }
    if ((local_78 & 1) != 0) {
      _ZdlPv(local_68);
    }
    if (((DAT_00ca5038 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca5038), iVar4 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
                    /* catch() { ... } // from try @ 006aafe8 with catch @ 006ab090 */
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
    local_6d = 0;
    local_78 = 0x14;
    local_6f = 0x676e;
    local_90 = 0x1a;
    local_77[0] = s_img027_png_002befe6[0];
    local_77[1] = s_img027_png_002befe6[1];
    local_77[2] = s_img027_png_002befe6[2];
    local_77[3] = s_img027_png_002befe6[3];
    local_77[4] = s_img027_png_002befe6[4];
    local_77[5] = s_img027_png_002befe6[5];
    local_77[6] = s_img027_png_002befe6[6];
    local_77[7] = s_img027_png_002befe6[7];
    local_82 = 0;
    local_8f = _DAT_002c01bd;
    acStack_8a[0] = s_7_imgcut_002c01c2[0];
    acStack_8a[1] = s_7_imgcut_002c01c2[1];
    acStack_8a[2] = s_7_imgcut_002c01c2[2];
    acStack_87[0] = s_7_imgcut_002c01c2[3];
    acStack_87[1] = s_7_imgcut_002c01c2[4];
    acStack_87[2] = s_7_imgcut_002c01c2[5];
    acStack_87[3] = s_7_imgcut_002c01c2[6];
    acStack_87[4] = s_7_imgcut_002c01c2[7];
                    /* catch() { ... } // from try @ 006aa8a8 with catch @ 006aaea4 */
    FUN_0047e64c(&local_60,&DAT_00ca5000,&local_78,&local_90,0x2601);
  }
  plVar3 = plStack_58;
  uVar2 = local_60;
  plVar7 = *(long **)(lVar5 + 0x130);
  local_60 = 0;
  plStack_58 = (long *)0x0;
  *(long **)(lVar5 + 0x130) = plVar3;
  *(undefined8 *)(lVar5 + 0x128) = uVar2;
                    /* try { // try from 006aaf58 to 007aaf6b has its CatchHandler @ 006ab12c */
  if ((plVar7 != (long *)0x0) && (lVar5 = FUN_00c53da0(0xffffffffffffffff,plVar7 + 1), lVar5 == 0))
  {
    (**(code **)(*plVar7 + 0x10))(plVar7);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
  }
  plVar3 = plStack_58;
                    /* try { // try from 006aaf84 to 007aaf93 has its CatchHandler @ 006ab10c */
  if ((plStack_58 != (long *)0x0) &&
     (lVar5 = FUN_00c53da0(0xffffffffffffffff,plStack_58 + 1), lVar5 == 0)) {
    (**(code **)(*plVar3 + 0x10))(plVar3);
                    /* try { // try from 006aafe8 to 007aaff7 has its CatchHandler @ 006ab090 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if ((local_78 & 1) != 0) {
    _ZdlPv(local_68);
  }
LAB_006aafb0:
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 006aafc8 to 007aafcf has its CatchHandler @ 006ab0ec */
  return;
}

~~~
