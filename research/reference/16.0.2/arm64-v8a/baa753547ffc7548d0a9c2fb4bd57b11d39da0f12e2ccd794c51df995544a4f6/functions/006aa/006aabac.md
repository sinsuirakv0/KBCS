# 006aabac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `006aab54`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006aa/006aab54.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0031.md#compare-3a536f0cada1b332d82466f286a5d7eb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `006aaf5c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006aa/006aaf5c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0033.md#compare-fb0c32209de662464cb8bc235cf6b952)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "b24f30f72b734d58db7252e990b8923fa0baeb5d9229a5c138b1bdf7220f0de1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006aabac",
        "006ab153"
      ],
      [
        "006ab19c",
        "006ab19f"
      ]
    ],
    "bytes_sha256": "ff48a7ac8eb2e1ec07d809039e269e1d824f4f466a31fb12ac748506cc9d7cd4",
    "instruction_count": 363,
    "instruction_bytes": 1452,
    "body_bytes": 1452,
    "indirect": 6,
    "unresolved": 6
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006aabac"></a> `006aabac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-006aabb0"></a> `006aabb0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006aabb4"></a> `006aabb4` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006aabb8"></a> `006aabb8` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-006aabbc"></a> `006aabbc` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006aabc0"></a> `006aabc0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-006aabc4"></a> `006aabc4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006aabc8"></a> `006aabc8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006aabcc"></a> `006aabcc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006aabd0"></a> `006aabd0` | `c8 2f 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-006aabd4"></a> `006aabd4` | `00 3d 45 f9` | ldr x0,[x8, #0xa78] | `FALL_THROUGH`
<a id="insn-006aabd8"></a> `006aabd8` | `20 01 00 b4` | cbz x0,0x006aabfc | `CONDITIONAL_JUMP`
<a id="insn-006aabdc"></a> `006aabdc` | `c1 2d 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-006aabe0"></a> `006aabe0` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-006aabe4"></a> `006aabe4` | `22 2e 00 f0` | adrp x2,0xc71000 | `FALL_THROUGH`
<a id="insn-006aabe8"></a> `006aabe8` | `42 40 0a 91` | add x2,x2,#0x290 | `FALL_THROUGH`
<a id="insn-006aabec"></a> `006aabec` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-006aabf0"></a> `006aabf0` | `bc b6 16 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-006aabf4"></a> `006aabf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006aabf8"></a> `006aabf8` | `02 00 00 14` | b 0x006aac00 | `UNCONDITIONAL_JUMP`
<a id="insn-006aabfc"></a> `006aabfc` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-006aac00"></a> `006aac00` | `77 62 04 91` | add x23,x19,#0x118 | `FALL_THROUGH`
<a id="insn-006aac04"></a> `006aac04` | `53 9a 06 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006aac08"></a> `006aac08` | `88 f9 87 52` | mov w8,#0x3fcc | `FALL_THROUGH`
<a id="insn-006aac0c"></a> `006aac0c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006aac10"></a> `006aac10` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006aac14"></a> `006aac14` | `e8 08 00 34` | cbz w8,0x006aad30 | `CONDITIONAL_JUMP`
<a id="insn-006aac18"></a> `006aac18` | `4e 9a 06 94` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-006aac1c"></a> `006aac1c` | `88 f9 87 52` | mov w8,#0x3fcc | `FALL_THROUGH`
<a id="insn-006aac20"></a> `006aac20` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006aac24"></a> `006aac24` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006aac28"></a> `006aac28` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006aac2c"></a> `006aac2c` | `2b 1c 00 54` | b.lt 0x006aafb0 | `CONDITIONAL_JUMP`
<a id="insn-006aac30"></a> `006aac30` | `d8 2f 00 f0` | adrp x24,0xca5000 | `FALL_THROUGH`
<a id="insn-006aac34"></a> `006aac34` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-006aac38"></a> `006aac38` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aac3c"></a> `006aac3c` | `08 1e 00 36` | tbz w8,#0x0,0x006aaffc | `CONDITIONAL_JUMP`
<a id="insn-006aac40"></a> `006aac40` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-006aac44"></a> `006aac44` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-006aac48"></a> `006aac48` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-006aac4c"></a> `006aac4c` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aac50"></a> `006aac50` | `a8 df ff d0` | adrp x8,0x2a0000 | `FALL_THROUGH`
<a id="insn-006aac54"></a> `006aac54` | `08 b9 0c 91` | add x8,x8,#0x32e | `FALL_THROUGH`
<a id="insn-006aac58"></a> `006aac58` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006aac5c"></a> `006aac5c` | `e9 13 02 78` | sturh w9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-006aac60"></a> `006aac60` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-006aac64"></a> `006aac64` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-006aac68"></a> `006aac68` | `e8 93 01 f8` | stur x8,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-006aac6c"></a> `006aac6c` | `a8 e0 ff f0` | adrp x8,0x2c1000 | `FALL_THROUGH`
<a id="insn-006aac70"></a> `006aac70` | `08 a1 14 91` | add x8,x8,#0x528 | `FALL_THROUGH`
<a id="insn-006aac74"></a> `006aac74` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-006aac78"></a> `006aac78` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-006aac7c"></a> `006aac7c` | `ff 3b 00 39` | strb wzr,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-006aac80"></a> `006aac80` | `e9 13 00 f8` | stur x9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-006aac84"></a> `006aac84` | `e8 63 00 f8` | stur x8,[sp, #0x6] | `FALL_THROUGH`
<a id="insn-006aac88"></a> `006aac88` | `d4 2f 00 f0` | adrp x20,0xca5000 | `FALL_THROUGH`
<a id="insn-006aac8c"></a> `006aac8c` | `94 02 00 91` | add x20,x20,#0x0 | `FALL_THROUGH`
<a id="insn-006aac90"></a> `006aac90` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-006aac94"></a> `006aac94` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006aac98"></a> `006aac98` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-006aac9c"></a> `006aac9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006aaca0"></a> `006aaca0` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-006aaca4"></a> `006aaca4` | `6a 4e f7 97` | bl 0x0047e64c | `UNCONDITIONAL_CALL`
<a id="insn-006aaca8"></a> `006aaca8` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aacac"></a> `006aacac` | `75 92 40 f9` | ldr x21,[x19, #0x120] | `FALL_THROUGH`
<a id="insn-006aacb0"></a> `006aacb0` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aacb4"></a> `006aacb4` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-006aacb8"></a> `006aacb8` | `75 01 00 b4` | cbz x21,0x006aace4 | `CONDITIONAL_JUMP`
<a id="insn-006aacbc"></a> `006aacbc` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006aacc0"></a> `006aacc0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aacc4"></a> `006aacc4` | `37 a4 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aacc8"></a> `006aacc8` | `e0 00 00 b5` | cbnz x0,0x006aace4 | `CONDITIONAL_JUMP`
<a id="insn-006aaccc"></a> `006aaccc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006aacd0"></a> `006aacd0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aacd4"></a> `006aacd4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aacd8"></a> `006aacd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aacdc"></a> `006aacdc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aace0"></a> `006aace0` | `9c b4 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aace4"></a> `006aace4` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-006aace8"></a> `006aace8` | `75 01 00 b4` | cbz x21,0x006aad14 | `CONDITIONAL_JUMP`
<a id="insn-006aacec"></a> `006aacec` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006aacf0"></a> `006aacf0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aacf4"></a> `006aacf4` | `2b a4 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aacf8"></a> `006aacf8` | `e0 00 00 b5` | cbnz x0,0x006aad14 | `CONDITIONAL_JUMP`
<a id="insn-006aacfc"></a> `006aacfc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006aad00"></a> `006aad00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aad04"></a> `006aad04` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aad08"></a> `006aad08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aad0c"></a> `006aad0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aad10"></a> `006aad10` | `90 b4 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aad14"></a> `006aad14` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006aad18"></a> `006aad18` | `c8 08 00 37` | tbnz w8,#0x0,0x006aae30 | `CONDITIONAL_JUMP`
<a id="insn-006aad1c"></a> `006aad1c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aad20"></a> `006aad20` | `08 09 00 37` | tbnz w8,#0x0,0x006aae40 | `CONDITIONAL_JUMP`
<a id="insn-006aad24"></a> `006aad24` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aad28"></a> `006aad28` | `48 09 00 37` | tbnz w8,#0x0,0x006aae50 | `CONDITIONAL_JUMP`
<a id="insn-006aad2c"></a> `006aad2c` | `ca 00 00 14` | b 0x006ab054 | `UNCONDITIONAL_JUMP`
<a id="insn-006aad30"></a> `006aad30` | `d8 2f 00 f0` | adrp x24,0xca5000 | `FALL_THROUGH`
<a id="insn-006aad34"></a> `006aad34` | `18 e3 00 91` | add x24,x24,#0x38 | `FALL_THROUGH`
<a id="insn-006aad38"></a> `006aad38` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aad3c"></a> `006aad3c` | `68 1b 00 36` | tbz w8,#0x0,0x006ab0a8 | `CONDITIONAL_JUMP`
<a id="insn-006aad40"></a> `006aad40` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-006aad44"></a> `006aad44` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-006aad48"></a> `006aad48` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-006aad4c"></a> `006aad4c` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aad50"></a> `006aad50` | `a8 df ff d0` | adrp x8,0x2a0000 | `FALL_THROUGH`
<a id="insn-006aad54"></a> `006aad54` | `08 b9 0c 91` | add x8,x8,#0x32e | `FALL_THROUGH`
<a id="insn-006aad58"></a> `006aad58` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006aad5c"></a> `006aad5c` | `e9 13 02 78` | sturh w9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-006aad60"></a> `006aad60` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-006aad64"></a> `006aad64` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-006aad68"></a> `006aad68` | `e8 93 01 f8` | stur x8,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-006aad6c"></a> `006aad6c` | `a8 e0 ff f0` | adrp x8,0x2c1000 | `FALL_THROUGH`
<a id="insn-006aad70"></a> `006aad70` | `08 a1 14 91` | add x8,x8,#0x528 | `FALL_THROUGH`
<a id="insn-006aad74"></a> `006aad74` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-006aad78"></a> `006aad78` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-006aad7c"></a> `006aad7c` | `ff 3b 00 39` | strb wzr,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-006aad80"></a> `006aad80` | `e9 13 00 f8` | stur x9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-006aad84"></a> `006aad84` | `e8 63 00 f8` | stur x8,[sp, #0x6] | `FALL_THROUGH`
<a id="insn-006aad88"></a> `006aad88` | `d4 2f 00 f0` | adrp x20,0xca5000 | `FALL_THROUGH`
<a id="insn-006aad8c"></a> `006aad8c` | `94 02 00 91` | add x20,x20,#0x0 | `FALL_THROUGH`
<a id="insn-006aad90"></a> `006aad90` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-006aad94"></a> `006aad94` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006aad98"></a> `006aad98` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-006aad9c"></a> `006aad9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006aada0"></a> `006aada0` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-006aada4"></a> `006aada4` | `2a 4e f7 97` | bl 0x0047e64c | `UNCONDITIONAL_CALL`
<a id="insn-006aada8"></a> `006aada8` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aadac"></a> `006aadac` | `75 92 40 f9` | ldr x21,[x19, #0x120] | `FALL_THROUGH`
<a id="insn-006aadb0"></a> `006aadb0` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aadb4"></a> `006aadb4` | `e0 02 80 3d` | str q0,[x23] | `FALL_THROUGH`
<a id="insn-006aadb8"></a> `006aadb8` | `75 01 00 b4` | cbz x21,0x006aade4 | `CONDITIONAL_JUMP`
<a id="insn-006aadbc"></a> `006aadbc` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006aadc0"></a> `006aadc0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aadc4"></a> `006aadc4` | `f7 a3 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aadc8"></a> `006aadc8` | `e0 00 00 b5` | cbnz x0,0x006aade4 | `CONDITIONAL_JUMP`
<a id="insn-006aadcc"></a> `006aadcc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006aadd0"></a> `006aadd0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aadd4"></a> `006aadd4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aadd8"></a> `006aadd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aaddc"></a> `006aaddc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aade0"></a> `006aade0` | `5c b4 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aade4"></a> `006aade4` | `b5 83 5e f8` | ldur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-006aade8"></a> `006aade8` | `75 01 00 b4` | cbz x21,0x006aae14 | `CONDITIONAL_JUMP`
<a id="insn-006aadec"></a> `006aadec` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006aadf0"></a> `006aadf0` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aadf4"></a> `006aadf4` | `eb a3 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aadf8"></a> `006aadf8` | `e0 00 00 b5` | cbnz x0,0x006aae14 | `CONDITIONAL_JUMP`
<a id="insn-006aadfc"></a> `006aadfc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006aae00"></a> `006aae00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aae04"></a> `006aae04` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aae08"></a> `006aae08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aae0c"></a> `006aae0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-006aae10"></a> `006aae10` | `50 b4 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aae14"></a> `006aae14` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006aae18"></a> `006aae18` | `08 05 00 37` | tbnz w8,#0x0,0x006aaeb8 | `CONDITIONAL_JUMP`
<a id="insn-006aae1c"></a> `006aae1c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aae20"></a> `006aae20` | `48 05 00 37` | tbnz w8,#0x0,0x006aaec8 | `CONDITIONAL_JUMP`
<a id="insn-006aae24"></a> `006aae24` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aae28"></a> `006aae28` | `88 05 00 37` | tbnz w8,#0x0,0x006aaed8 | `CONDITIONAL_JUMP`
<a id="insn-006aae2c"></a> `006aae2c` | `b5 00 00 14` | b 0x006ab100 | `UNCONDITIONAL_JUMP`
<a id="insn-006aae30"></a> `006aae30` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006aae34"></a> `006aae34` | `53 b4 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aae38"></a> `006aae38` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aae3c"></a> `006aae3c` | `48 f7 07 36` | tbz w8,#0x0,0x006aad24 | `CONDITIONAL_JUMP`
<a id="insn-006aae40"></a> `006aae40` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006aae44"></a> `006aae44` | `4f b4 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aae48"></a> `006aae48` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aae4c"></a> `006aae4c` | `48 10 00 36` | tbz w8,#0x0,0x006ab054 | `CONDITIONAL_JUMP`
<a id="insn-006aae50"></a> `006aae50` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-006aae54"></a> `006aae54` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-006aae58"></a> `006aae58` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-006aae5c"></a> `006aae5c` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aae60"></a> `006aae60` | `a8 e0 ff 90` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-006aae64"></a> `006aae64` | `08 99 3f 91` | add x8,x8,#0xfe6 | `FALL_THROUGH`
<a id="insn-006aae68"></a> `006aae68` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006aae6c"></a> `006aae6c` | `e9 13 02 78` | sturh w9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-006aae70"></a> `006aae70` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-006aae74"></a> `006aae74` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-006aae78"></a> `006aae78` | `e8 93 01 f8` | stur x8,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-006aae7c"></a> `006aae7c` | `a8 e0 ff d0` | adrp x8,0x2c0000 | `FALL_THROUGH`
<a id="insn-006aae80"></a> `006aae80` | `08 f5 06 91` | add x8,x8,#0x1bd | `FALL_THROUGH`
<a id="insn-006aae84"></a> `006aae84` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-006aae88"></a> `006aae88` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-006aae8c"></a> `006aae8c` | `ff 3b 00 39` | strb wzr,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-006aae90"></a> `006aae90` | `e9 13 00 f8` | stur x9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-006aae94"></a> `006aae94` | `e8 63 00 f8` | stur x8,[sp, #0x6] | `FALL_THROUGH`
<a id="insn-006aae98"></a> `006aae98` | `c0 2f 00 f0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006aae9c"></a> `006aae9c` | `00 00 00 91` | add x0,x0,#0x0 | `FALL_THROUGH`
<a id="insn-006aaea0"></a> `006aaea0` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-006aaea4"></a> `006aaea4` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006aaea8"></a> `006aaea8` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-006aaeac"></a> `006aaeac` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-006aaeb0"></a> `006aaeb0` | `e7 4d f7 97` | bl 0x0047e64c | `UNCONDITIONAL_CALL`
<a id="insn-006aaeb4"></a> `006aaeb4` | `22 00 00 14` | b 0x006aaf3c | `UNCONDITIONAL_JUMP`
<a id="insn-006aaeb8"></a> `006aaeb8` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006aaebc"></a> `006aaebc` | `31 b4 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aaec0"></a> `006aaec0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aaec4"></a> `006aaec4` | `08 fb 07 36` | tbz w8,#0x0,0x006aae24 | `CONDITIONAL_JUMP`
<a id="insn-006aaec8"></a> `006aaec8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006aaecc"></a> `006aaecc` | `2d b4 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aaed0"></a> `006aaed0` | `08 ff df 08` | ldarb w8,[x24] | `FALL_THROUGH`
<a id="insn-006aaed4"></a> `006aaed4` | `68 11 00 36` | tbz w8,#0x0,0x006ab100 | `CONDITIONAL_JUMP`
<a id="insn-006aaed8"></a> `006aaed8` | `88 02 80 52` | mov w8,#0x14 | `FALL_THROUGH`
<a id="insn-006aaedc"></a> `006aaedc` | `c9 ed 8c 52` | mov w9,#0x676e | `FALL_THROUGH`
<a id="insn-006aaee0"></a> `006aaee0` | `ff 8f 00 39` | strb wzr,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-006aaee4"></a> `006aaee4` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aaee8"></a> `006aaee8` | `c8 df ff b0` | adrp x8,0x2a3000 | `FALL_THROUGH`
<a id="insn-006aaeec"></a> `006aaeec` | `08 81 0f 91` | add x8,x8,#0x3e0 | `FALL_THROUGH`
<a id="insn-006aaef0"></a> `006aaef0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006aaef4"></a> `006aaef4` | `e9 13 02 78` | sturh w9,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-006aaef8"></a> `006aaef8` | `49 03 80 52` | mov w9,#0x1a | `FALL_THROUGH`
<a id="insn-006aaefc"></a> `006aaefc` | `e9 03 00 39` | strb w9,[sp] | `FALL_THROUGH`
<a id="insn-006aaf00"></a> `006aaf00` | `e8 93 01 f8` | stur x8,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-006aaf04"></a> `006aaf04` | `a8 df ff b0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-006aaf08"></a> `006aaf08` | `08 ed 09 91` | add x8,x8,#0x27b | `FALL_THROUGH`
<a id="insn-006aaf0c"></a> `006aaf0c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-006aaf10"></a> `006aaf10` | `08 51 40 f8` | ldur x8,[x8, #0x5] | `FALL_THROUGH`
<a id="insn-006aaf14"></a> `006aaf14` | `ff 3b 00 39` | strb wzr,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-006aaf18"></a> `006aaf18` | `e9 13 00 f8` | stur x9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-006aaf1c"></a> `006aaf1c` | `e8 63 00 f8` | stur x8,[sp, #0x6] | `FALL_THROUGH`
<a id="insn-006aaf20"></a> `006aaf20` | `c0 2f 00 f0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006aaf24"></a> `006aaf24` | `00 00 00 91` | add x0,x0,#0x0 | `FALL_THROUGH`
<a id="insn-006aaf28"></a> `006aaf28` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-006aaf2c"></a> `006aaf2c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-006aaf30"></a> `006aaf30` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-006aaf34"></a> `006aaf34` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-006aaf38"></a> `006aaf38` | `c5 4d f7 97` | bl 0x0047e64c | `UNCONDITIONAL_CALL`
<a id="insn-006aaf3c"></a> `006aaf3c` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aaf40"></a> `006aaf40` | `73 9a 40 f9` | ldr x19,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-006aaf44"></a> `006aaf44` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-006aaf48"></a> `006aaf48` | `e0 06 80 3d` | str q0,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-006aaf4c"></a> `006aaf4c` | `73 01 00 b4` | cbz x19,0x006aaf78 | `CONDITIONAL_JUMP`
<a id="insn-006aaf50"></a> `006aaf50` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-006aaf54"></a> `006aaf54` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aaf58"></a> `006aaf58` | `92 a3 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aaf5c"></a> `006aaf5c` | `e0 00 00 b5` | cbnz x0,0x006aaf78 | `CONDITIONAL_JUMP`
<a id="insn-006aaf60"></a> `006aaf60` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-006aaf64"></a> `006aaf64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006aaf68"></a> `006aaf68` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aaf6c"></a> `006aaf6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aaf70"></a> `006aaf70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006aaf74"></a> `006aaf74` | `f7 b3 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aaf78"></a> `006aaf78` | `b3 83 5e f8` | ldur x19,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-006aaf7c"></a> `006aaf7c` | `b3 00 00 b4` | cbz x19,0x006aaf90 | `CONDITIONAL_JUMP`
<a id="insn-006aaf80"></a> `006aaf80` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-006aaf84"></a> `006aaf84` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-006aaf88"></a> `006aaf88` | `86 a3 16 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-006aaf8c"></a> `006aaf8c` | `60 02 00 b4` | cbz x0,0x006aafd8 | `CONDITIONAL_JUMP`
<a id="insn-006aaf90"></a> `006aaf90` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006aaf94"></a> `006aaf94` | `68 00 00 36` | tbz w8,#0x0,0x006aafa0 | `CONDITIONAL_JUMP`
<a id="insn-006aaf98"></a> `006aaf98` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006aaf9c"></a> `006aaf9c` | `f9 b3 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aafa0"></a> `006aafa0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-006aafa4"></a> `006aafa4` | `68 00 00 36` | tbz w8,#0x0,0x006aafb0 | `CONDITIONAL_JUMP`
<a id="insn-006aafa8"></a> `006aafa8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-006aafac"></a> `006aafac` | `f5 b3 16 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-006aafb0"></a> `006aafb0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-006aafb4"></a> `006aafb4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-006aafb8"></a> `006aafb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006aafbc"></a> `006aafbc` | `01 0f 00 54` | b.ne 0x006ab19c | `CONDITIONAL_JUMP`
<a id="insn-006aafc0"></a> `006aafc0` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-006aafc4"></a> `006aafc4` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-006aafc8"></a> `006aafc8` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006aafcc"></a> `006aafcc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006aafd0"></a> `006aafd0` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-006aafd4"></a> `006aafd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006aafd8"></a> `006aafd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-006aafdc"></a> `006aafdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006aafe0"></a> `006aafe0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-006aafe4"></a> `006aafe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-006aafe8"></a> `006aafe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006aafec"></a> `006aafec` | `d9 b3 16 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-006aaff0"></a> `006aaff0` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-006aaff4"></a> `006aaff4` | `28 fd 07 37` | tbnz w8,#0x0,0x006aaf98 | `CONDITIONAL_JUMP`
<a id="insn-006aaff8"></a> `006aaff8` | `ea ff ff 17` | b 0x006aafa0 | `UNCONDITIONAL_JUMP`
<a id="insn-006aaffc"></a> `006aaffc` | `c0 2f 00 f0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab000"></a> `006ab000` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab004"></a> `006ab004` | `c7 b3 16 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-006ab008"></a> `006ab008` | `c0 e1 ff 34` | cbz w0,0x006aac40 | `CONDITIONAL_JUMP`
<a id="insn-006ab00c"></a> `006ab00c` | `c1 2f 00 d0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab010"></a> `006ab010` | `21 00 00 91` | add x1,x1,#0x0 | `FALL_THROUGH`
<a id="insn-006ab014"></a> `006ab014` | `80 ee ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-006ab018"></a> `006ab018` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-006ab01c"></a> `006ab01c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-006ab020"></a> `006ab020` | `c2 2d 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-006ab024"></a> `006ab024` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-006ab028"></a> `006ab028` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-006ab02c"></a> `006ab02c` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-006ab030"></a> `006ab030` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-006ab034"></a> `006ab034` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-006ab038"></a> `006ab038` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-006ab03c"></a> `006ab03c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-006ab040"></a> `006ab040` | `b0 b3 16 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-006ab044"></a> `006ab044` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab048"></a> `006ab048` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab04c"></a> `006ab04c` | `bd b3 16 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-006ab050"></a> `006ab050` | `fc fe ff 17` | b 0x006aac40 | `UNCONDITIONAL_JUMP`
<a id="insn-006ab054"></a> `006ab054` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab058"></a> `006ab058` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab05c"></a> `006ab05c` | `b1 b3 16 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-006ab060"></a> `006ab060` | `80 ef ff 34` | cbz w0,0x006aae50 | `CONDITIONAL_JUMP`
<a id="insn-006ab064"></a> `006ab064` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-006ab068"></a> `006ab068` | `80 ee ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-006ab06c"></a> `006ab06c` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-006ab070"></a> `006ab070` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-006ab074"></a> `006ab074` | `c2 2d 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-006ab078"></a> `006ab078` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-006ab07c"></a> `006ab07c` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-006ab080"></a> `006ab080` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-006ab084"></a> `006ab084` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006ab088"></a> `006ab088` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006ab08c"></a> `006ab08c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-006ab090"></a> `006ab090` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-006ab094"></a> `006ab094` | `9b b3 16 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-006ab098"></a> `006ab098` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab09c"></a> `006ab09c` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab0a0"></a> `006ab0a0` | `a8 b3 16 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-006ab0a4"></a> `006ab0a4` | `6b ff ff 17` | b 0x006aae50 | `UNCONDITIONAL_JUMP`
<a id="insn-006ab0a8"></a> `006ab0a8` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab0ac"></a> `006ab0ac` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab0b0"></a> `006ab0b0` | `9c b3 16 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-006ab0b4"></a> `006ab0b4` | `60 e4 ff 34` | cbz w0,0x006aad40 | `CONDITIONAL_JUMP`
<a id="insn-006ab0b8"></a> `006ab0b8` | `c1 2f 00 d0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab0bc"></a> `006ab0bc` | `21 00 00 91` | add x1,x1,#0x0 | `FALL_THROUGH`
<a id="insn-006ab0c0"></a> `006ab0c0` | `80 ee ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-006ab0c4"></a> `006ab0c4` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-006ab0c8"></a> `006ab0c8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-006ab0cc"></a> `006ab0cc` | `c2 2d 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-006ab0d0"></a> `006ab0d0` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-006ab0d4"></a> `006ab0d4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-006ab0d8"></a> `006ab0d8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-006ab0dc"></a> `006ab0dc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-006ab0e0"></a> `006ab0e0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-006ab0e4"></a> `006ab0e4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-006ab0e8"></a> `006ab0e8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-006ab0ec"></a> `006ab0ec` | `85 b3 16 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-006ab0f0"></a> `006ab0f0` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab0f4"></a> `006ab0f4` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab0f8"></a> `006ab0f8` | `92 b3 16 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-006ab0fc"></a> `006ab0fc` | `11 ff ff 17` | b 0x006aad40 | `UNCONDITIONAL_JUMP`
<a id="insn-006ab100"></a> `006ab100` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab104"></a> `006ab104` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab108"></a> `006ab108` | `86 b3 16 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-006ab10c"></a> `006ab10c` | `60 ee ff 34` | cbz w0,0x006aaed8 | `CONDITIONAL_JUMP`
<a id="insn-006ab110"></a> `006ab110` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-006ab114"></a> `006ab114` | `80 ee ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-006ab118"></a> `006ab118` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-006ab11c"></a> `006ab11c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-006ab120"></a> `006ab120` | `c2 2d 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-006ab124"></a> `006ab124` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-006ab128"></a> `006ab128` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-006ab12c"></a> `006ab12c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-006ab130"></a> `006ab130` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-006ab134"></a> `006ab134` | `9f fe 02 a9` | stp xzr,xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-006ab138"></a> `006ab138` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-006ab13c"></a> `006ab13c` | `9f 22 01 a9` | stp xzr,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-006ab140"></a> `006ab140` | `70 b3 16 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-006ab144"></a> `006ab144` | `c0 2f 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-006ab148"></a> `006ab148` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-006ab14c"></a> `006ab14c` | `7d b3 16 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-006ab150"></a> `006ab150` | `62 ff ff 17` | b 0x006aaed8 | `UNCONDITIONAL_JUMP`
<a id="insn-006ab19c"></a> `006ab19c` | `85 b3 16 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006aabac`](#insn-006aabac) 範囲 `[['006aabac', '006aabdb']]`
  - `CONDITIONAL_JUMP` [`006aabd8`](#insn-006aabd8) → [`006aabfc`](#insn-006aabfc)
  - `FALL_THROUGH` [`006aabd8`](#insn-006aabd8) → [`006aabdc`](#insn-006aabdc)
- ブロック [`006aabdc`](#insn-006aabdc) 範囲 `[['006aabdc', '006aabfb']]`
  - `UNCONDITIONAL_JUMP` [`006aabf8`](#insn-006aabf8) → [`006aac00`](#insn-006aac00)
- ブロック [`006aabfc`](#insn-006aabfc) 範囲 `[['006aabfc', '006aabff']]`
  - `FALL_THROUGH` [`006aabfc`](#insn-006aabfc) → [`006aac00`](#insn-006aac00)
- ブロック [`006aac00`](#insn-006aac00) 範囲 `[['006aac00', '006aac17']]`
  - `CONDITIONAL_JUMP` [`006aac14`](#insn-006aac14) → [`006aad30`](#insn-006aad30)
  - `FALL_THROUGH` [`006aac14`](#insn-006aac14) → [`006aac18`](#insn-006aac18)
- ブロック [`006aac18`](#insn-006aac18) 範囲 `[['006aac18', '006aac2f']]`
  - `CONDITIONAL_JUMP` [`006aac2c`](#insn-006aac2c) → [`006aafb0`](#insn-006aafb0)
  - `FALL_THROUGH` [`006aac2c`](#insn-006aac2c) → [`006aac30`](#insn-006aac30)
- ブロック [`006aac30`](#insn-006aac30) 範囲 `[['006aac30', '006aac3f']]`
  - `CONDITIONAL_JUMP` [`006aac3c`](#insn-006aac3c) → [`006aaffc`](#insn-006aaffc)
  - `FALL_THROUGH` [`006aac3c`](#insn-006aac3c) → [`006aac40`](#insn-006aac40)
- ブロック [`006aac40`](#insn-006aac40) 範囲 `[['006aac40', '006aac43']]`
  - `FALL_THROUGH` [`006aac40`](#insn-006aac40) → [`006aac44`](#insn-006aac44)
- ブロック [`006aac44`](#insn-006aac44) 範囲 `[['006aac44', '006aac97']]`
  - `FALL_THROUGH` [`006aac94`](#insn-006aac94) → [`006aac98`](#insn-006aac98)
- ブロック [`006aac98`](#insn-006aac98) 範囲 `[['006aac98', '006aacbb']]`
  - `CONDITIONAL_JUMP` [`006aacb8`](#insn-006aacb8) → [`006aace4`](#insn-006aace4)
  - `FALL_THROUGH` [`006aacb8`](#insn-006aacb8) → [`006aacbc`](#insn-006aacbc)
- ブロック [`006aacbc`](#insn-006aacbc) 範囲 `[['006aacbc', '006aaccb']]`
  - `CONDITIONAL_JUMP` [`006aacc8`](#insn-006aacc8) → [`006aace4`](#insn-006aace4)
  - `FALL_THROUGH` [`006aacc8`](#insn-006aacc8) → [`006aaccc`](#insn-006aaccc)
- ブロック [`006aaccc`](#insn-006aaccc) 範囲 `[['006aaccc', '006aaccf']]`
  - `FALL_THROUGH` [`006aaccc`](#insn-006aaccc) → [`006aacd0`](#insn-006aacd0)
- ブロック [`006aacd0`](#insn-006aacd0) 範囲 `[['006aacd0', '006aace3']]`
  - `FALL_THROUGH` [`006aace0`](#insn-006aace0) → [`006aace4`](#insn-006aace4)
- ブロック [`006aace4`](#insn-006aace4) 範囲 `[['006aace4', '006aaceb']]`
  - `CONDITIONAL_JUMP` [`006aace8`](#insn-006aace8) → [`006aad14`](#insn-006aad14)
  - `FALL_THROUGH` [`006aace8`](#insn-006aace8) → [`006aacec`](#insn-006aacec)
- ブロック [`006aacec`](#insn-006aacec) 範囲 `[['006aacec', '006aacef']]`
  - `FALL_THROUGH` [`006aacec`](#insn-006aacec) → [`006aacf0`](#insn-006aacf0)
- ブロック [`006aacf0`](#insn-006aacf0) 範囲 `[['006aacf0', '006aacfb']]`
  - `CONDITIONAL_JUMP` [`006aacf8`](#insn-006aacf8) → [`006aad14`](#insn-006aad14)
  - `FALL_THROUGH` [`006aacf8`](#insn-006aacf8) → [`006aacfc`](#insn-006aacfc)
- ブロック [`006aacfc`](#insn-006aacfc) 範囲 `[['006aacfc', '006aad13']]`
  - `FALL_THROUGH` [`006aad10`](#insn-006aad10) → [`006aad14`](#insn-006aad14)
- ブロック [`006aad14`](#insn-006aad14) 範囲 `[['006aad14', '006aad1b']]`
  - `CONDITIONAL_JUMP` [`006aad18`](#insn-006aad18) → [`006aae30`](#insn-006aae30)
  - `FALL_THROUGH` [`006aad18`](#insn-006aad18) → [`006aad1c`](#insn-006aad1c)
- ブロック [`006aad1c`](#insn-006aad1c) 範囲 `[['006aad1c', '006aad23']]`
  - `CONDITIONAL_JUMP` [`006aad20`](#insn-006aad20) → [`006aae40`](#insn-006aae40)
  - `FALL_THROUGH` [`006aad20`](#insn-006aad20) → [`006aad24`](#insn-006aad24)
- ブロック [`006aad24`](#insn-006aad24) 範囲 `[['006aad24', '006aad2b']]`
  - `CONDITIONAL_JUMP` [`006aad28`](#insn-006aad28) → [`006aae50`](#insn-006aae50)
  - `FALL_THROUGH` [`006aad28`](#insn-006aad28) → [`006aad2c`](#insn-006aad2c)
- ブロック [`006aad2c`](#insn-006aad2c) 範囲 `[['006aad2c', '006aad2f']]`
  - `UNCONDITIONAL_JUMP` [`006aad2c`](#insn-006aad2c) → [`006ab054`](#insn-006ab054)
- ブロック [`006aad30`](#insn-006aad30) 範囲 `[['006aad30', '006aad3f']]`
  - `CONDITIONAL_JUMP` [`006aad3c`](#insn-006aad3c) → [`006ab0a8`](#insn-006ab0a8)
  - `FALL_THROUGH` [`006aad3c`](#insn-006aad3c) → [`006aad40`](#insn-006aad40)
- ブロック [`006aad40`](#insn-006aad40) 範囲 `[['006aad40', '006aadbb']]`
  - `CONDITIONAL_JUMP` [`006aadb8`](#insn-006aadb8) → [`006aade4`](#insn-006aade4)
  - `FALL_THROUGH` [`006aadb8`](#insn-006aadb8) → [`006aadbc`](#insn-006aadbc)
- ブロック [`006aadbc`](#insn-006aadbc) 範囲 `[['006aadbc', '006aadcb']]`
  - `CONDITIONAL_JUMP` [`006aadc8`](#insn-006aadc8) → [`006aade4`](#insn-006aade4)
  - `FALL_THROUGH` [`006aadc8`](#insn-006aadc8) → [`006aadcc`](#insn-006aadcc)
- ブロック [`006aadcc`](#insn-006aadcc) 範囲 `[['006aadcc', '006aaddf']]`
  - `FALL_THROUGH` [`006aaddc`](#insn-006aaddc) → [`006aade0`](#insn-006aade0)
- ブロック [`006aade0`](#insn-006aade0) 範囲 `[['006aade0', '006aade3']]`
  - `FALL_THROUGH` [`006aade0`](#insn-006aade0) → [`006aade4`](#insn-006aade4)
- ブロック [`006aade4`](#insn-006aade4) 範囲 `[['006aade4', '006aade7']]`
  - `FALL_THROUGH` [`006aade4`](#insn-006aade4) → [`006aade8`](#insn-006aade8)
- ブロック [`006aade8`](#insn-006aade8) 範囲 `[['006aade8', '006aadeb']]`
  - `CONDITIONAL_JUMP` [`006aade8`](#insn-006aade8) → [`006aae14`](#insn-006aae14)
  - `FALL_THROUGH` [`006aade8`](#insn-006aade8) → [`006aadec`](#insn-006aadec)
- ブロック [`006aadec`](#insn-006aadec) 範囲 `[['006aadec', '006aadf7']]`
  - `FALL_THROUGH` [`006aadf4`](#insn-006aadf4) → [`006aadf8`](#insn-006aadf8)
- ブロック [`006aadf8`](#insn-006aadf8) 範囲 `[['006aadf8', '006aadfb']]`
  - `CONDITIONAL_JUMP` [`006aadf8`](#insn-006aadf8) → [`006aae14`](#insn-006aae14)
  - `FALL_THROUGH` [`006aadf8`](#insn-006aadf8) → [`006aadfc`](#insn-006aadfc)
- ブロック [`006aadfc`](#insn-006aadfc) 範囲 `[['006aadfc', '006aadff']]`
  - `FALL_THROUGH` [`006aadfc`](#insn-006aadfc) → [`006aae00`](#insn-006aae00)
- ブロック [`006aae00`](#insn-006aae00) 範囲 `[['006aae00', '006aae03']]`
  - `FALL_THROUGH` [`006aae00`](#insn-006aae00) → [`006aae04`](#insn-006aae04)
- ブロック [`006aae04`](#insn-006aae04) 範囲 `[['006aae04', '006aae07']]`
  - `FALL_THROUGH` [`006aae04`](#insn-006aae04) → [`006aae08`](#insn-006aae08)
- ブロック [`006aae08`](#insn-006aae08) 範囲 `[['006aae08', '006aae0b']]`
  - `FALL_THROUGH` [`006aae08`](#insn-006aae08) → [`006aae0c`](#insn-006aae0c)
- ブロック [`006aae0c`](#insn-006aae0c) 範囲 `[['006aae0c', '006aae13']]`
  - `FALL_THROUGH` [`006aae10`](#insn-006aae10) → [`006aae14`](#insn-006aae14)
- ブロック [`006aae14`](#insn-006aae14) 範囲 `[['006aae14', '006aae1b']]`
  - `CONDITIONAL_JUMP` [`006aae18`](#insn-006aae18) → [`006aaeb8`](#insn-006aaeb8)
  - `FALL_THROUGH` [`006aae18`](#insn-006aae18) → [`006aae1c`](#insn-006aae1c)
- ブロック [`006aae1c`](#insn-006aae1c) 範囲 `[['006aae1c', '006aae1f']]`
  - `FALL_THROUGH` [`006aae1c`](#insn-006aae1c) → [`006aae20`](#insn-006aae20)
- ブロック [`006aae20`](#insn-006aae20) 範囲 `[['006aae20', '006aae23']]`
  - `CONDITIONAL_JUMP` [`006aae20`](#insn-006aae20) → [`006aaec8`](#insn-006aaec8)
  - `FALL_THROUGH` [`006aae20`](#insn-006aae20) → [`006aae24`](#insn-006aae24)
- ブロック [`006aae24`](#insn-006aae24) 範囲 `[['006aae24', '006aae2b']]`
  - `CONDITIONAL_JUMP` [`006aae28`](#insn-006aae28) → [`006aaed8`](#insn-006aaed8)
  - `FALL_THROUGH` [`006aae28`](#insn-006aae28) → [`006aae2c`](#insn-006aae2c)
- ブロック [`006aae2c`](#insn-006aae2c) 範囲 `[['006aae2c', '006aae2f']]`
  - `UNCONDITIONAL_JUMP` [`006aae2c`](#insn-006aae2c) → [`006ab100`](#insn-006ab100)
- ブロック [`006aae30`](#insn-006aae30) 範囲 `[['006aae30', '006aae3f']]`
  - `CONDITIONAL_JUMP` [`006aae3c`](#insn-006aae3c) → [`006aad24`](#insn-006aad24)
  - `FALL_THROUGH` [`006aae3c`](#insn-006aae3c) → [`006aae40`](#insn-006aae40)
- ブロック [`006aae40`](#insn-006aae40) 範囲 `[['006aae40', '006aae4f']]`
  - `CONDITIONAL_JUMP` [`006aae4c`](#insn-006aae4c) → [`006ab054`](#insn-006ab054)
  - `FALL_THROUGH` [`006aae4c`](#insn-006aae4c) → [`006aae50`](#insn-006aae50)
- ブロック [`006aae50`](#insn-006aae50) 範囲 `[['006aae50', '006aaea3']]`
  - `FALL_THROUGH` [`006aaea0`](#insn-006aaea0) → [`006aaea4`](#insn-006aaea4)
- ブロック [`006aaea4`](#insn-006aaea4) 範囲 `[['006aaea4', '006aaeb7']]`
  - `UNCONDITIONAL_JUMP` [`006aaeb4`](#insn-006aaeb4) → [`006aaf3c`](#insn-006aaf3c)
- ブロック [`006aaeb8`](#insn-006aaeb8) 範囲 `[['006aaeb8', '006aaec7']]`
  - `CONDITIONAL_JUMP` [`006aaec4`](#insn-006aaec4) → [`006aae24`](#insn-006aae24)
  - `FALL_THROUGH` [`006aaec4`](#insn-006aaec4) → [`006aaec8`](#insn-006aaec8)
- ブロック [`006aaec8`](#insn-006aaec8) 範囲 `[['006aaec8', '006aaed7']]`
  - `CONDITIONAL_JUMP` [`006aaed4`](#insn-006aaed4) → [`006ab100`](#insn-006ab100)
  - `FALL_THROUGH` [`006aaed4`](#insn-006aaed4) → [`006aaed8`](#insn-006aaed8)
- ブロック [`006aaed8`](#insn-006aaed8) 範囲 `[['006aaed8', '006aaf23']]`
  - `FALL_THROUGH` [`006aaf20`](#insn-006aaf20) → [`006aaf24`](#insn-006aaf24)
- ブロック [`006aaf24`](#insn-006aaf24) 範囲 `[['006aaf24', '006aaf3b']]`
  - `FALL_THROUGH` [`006aaf38`](#insn-006aaf38) → [`006aaf3c`](#insn-006aaf3c)
- ブロック [`006aaf3c`](#insn-006aaf3c) 範囲 `[['006aaf3c', '006aaf4f']]`
  - `CONDITIONAL_JUMP` [`006aaf4c`](#insn-006aaf4c) → [`006aaf78`](#insn-006aaf78)
  - `FALL_THROUGH` [`006aaf4c`](#insn-006aaf4c) → [`006aaf50`](#insn-006aaf50)
- ブロック [`006aaf50`](#insn-006aaf50) 範囲 `[['006aaf50', '006aaf57']]`
  - `FALL_THROUGH` [`006aaf54`](#insn-006aaf54) → [`006aaf58`](#insn-006aaf58)
- ブロック [`006aaf58`](#insn-006aaf58) 範囲 `[['006aaf58', '006aaf5f']]`
  - `CONDITIONAL_JUMP` [`006aaf5c`](#insn-006aaf5c) → [`006aaf78`](#insn-006aaf78)
  - `FALL_THROUGH` [`006aaf5c`](#insn-006aaf5c) → [`006aaf60`](#insn-006aaf60)
- ブロック [`006aaf60`](#insn-006aaf60) 範囲 `[['006aaf60', '006aaf77']]`
  - `FALL_THROUGH` [`006aaf74`](#insn-006aaf74) → [`006aaf78`](#insn-006aaf78)
- ブロック [`006aaf78`](#insn-006aaf78) 範囲 `[['006aaf78', '006aaf7f']]`
  - `CONDITIONAL_JUMP` [`006aaf7c`](#insn-006aaf7c) → [`006aaf90`](#insn-006aaf90)
  - `FALL_THROUGH` [`006aaf7c`](#insn-006aaf7c) → [`006aaf80`](#insn-006aaf80)
- ブロック [`006aaf80`](#insn-006aaf80) 範囲 `[['006aaf80', '006aaf83']]`
  - `FALL_THROUGH` [`006aaf80`](#insn-006aaf80) → [`006aaf84`](#insn-006aaf84)
- ブロック [`006aaf84`](#insn-006aaf84) 範囲 `[['006aaf84', '006aaf8f']]`
  - `CONDITIONAL_JUMP` [`006aaf8c`](#insn-006aaf8c) → [`006aafd8`](#insn-006aafd8)
  - `FALL_THROUGH` [`006aaf8c`](#insn-006aaf8c) → [`006aaf90`](#insn-006aaf90)
- ブロック [`006aaf90`](#insn-006aaf90) 範囲 `[['006aaf90', '006aaf97']]`
  - `CONDITIONAL_JUMP` [`006aaf94`](#insn-006aaf94) → [`006aafa0`](#insn-006aafa0)
  - `FALL_THROUGH` [`006aaf94`](#insn-006aaf94) → [`006aaf98`](#insn-006aaf98)
- ブロック [`006aaf98`](#insn-006aaf98) 範囲 `[['006aaf98', '006aaf9f']]`
  - `FALL_THROUGH` [`006aaf9c`](#insn-006aaf9c) → [`006aafa0`](#insn-006aafa0)
- ブロック [`006aafa0`](#insn-006aafa0) 範囲 `[['006aafa0', '006aafa7']]`
  - `CONDITIONAL_JUMP` [`006aafa4`](#insn-006aafa4) → [`006aafb0`](#insn-006aafb0)
  - `FALL_THROUGH` [`006aafa4`](#insn-006aafa4) → [`006aafa8`](#insn-006aafa8)
- ブロック [`006aafa8`](#insn-006aafa8) 範囲 `[['006aafa8', '006aafaf']]`
  - `FALL_THROUGH` [`006aafac`](#insn-006aafac) → [`006aafb0`](#insn-006aafb0)
- ブロック [`006aafb0`](#insn-006aafb0) 範囲 `[['006aafb0', '006aafbf']]`
  - `CONDITIONAL_JUMP` [`006aafbc`](#insn-006aafbc) → [`006ab19c`](#insn-006ab19c)
  - `FALL_THROUGH` [`006aafbc`](#insn-006aafbc) → [`006aafc0`](#insn-006aafc0)
- ブロック [`006aafc0`](#insn-006aafc0) 範囲 `[['006aafc0', '006aafc7']]`
  - `FALL_THROUGH` [`006aafc4`](#insn-006aafc4) → [`006aafc8`](#insn-006aafc8)
- ブロック [`006aafc8`](#insn-006aafc8) 範囲 `[['006aafc8', '006aafd7']]`
- ブロック [`006aafd8`](#insn-006aafd8) 範囲 `[['006aafd8', '006aafe7']]`
  - `FALL_THROUGH` [`006aafe4`](#insn-006aafe4) → [`006aafe8`](#insn-006aafe8)
- ブロック [`006aafe8`](#insn-006aafe8) 範囲 `[['006aafe8', '006aaff7']]`
  - `CONDITIONAL_JUMP` [`006aaff4`](#insn-006aaff4) → [`006aaf98`](#insn-006aaf98)
  - `FALL_THROUGH` [`006aaff4`](#insn-006aaff4) → [`006aaff8`](#insn-006aaff8)
- ブロック [`006aaff8`](#insn-006aaff8) 範囲 `[['006aaff8', '006aaffb']]`
  - `UNCONDITIONAL_JUMP` [`006aaff8`](#insn-006aaff8) → [`006aafa0`](#insn-006aafa0)
- ブロック [`006aaffc`](#insn-006aaffc) 範囲 `[['006aaffc', '006ab00b']]`
  - `CONDITIONAL_JUMP` [`006ab008`](#insn-006ab008) → [`006aac40`](#insn-006aac40)
  - `FALL_THROUGH` [`006ab008`](#insn-006ab008) → [`006ab00c`](#insn-006ab00c)
- ブロック [`006ab00c`](#insn-006ab00c) 範囲 `[['006ab00c', '006ab053']]`
  - `UNCONDITIONAL_JUMP` [`006ab050`](#insn-006ab050) → [`006aac40`](#insn-006aac40)
- ブロック [`006ab054`](#insn-006ab054) 範囲 `[['006ab054', '006ab063']]`
  - `CONDITIONAL_JUMP` [`006ab060`](#insn-006ab060) → [`006aae50`](#insn-006aae50)
  - `FALL_THROUGH` [`006ab060`](#insn-006ab060) → [`006ab064`](#insn-006ab064)
- ブロック [`006ab064`](#insn-006ab064) 範囲 `[['006ab064', '006ab08f']]`
  - `FALL_THROUGH` [`006ab08c`](#insn-006ab08c) → [`006ab090`](#insn-006ab090)
- ブロック [`006ab090`](#insn-006ab090) 範囲 `[['006ab090', '006ab0a7']]`
  - `UNCONDITIONAL_JUMP` [`006ab0a4`](#insn-006ab0a4) → [`006aae50`](#insn-006aae50)
- ブロック [`006ab0a8`](#insn-006ab0a8) 範囲 `[['006ab0a8', '006ab0b7']]`
  - `CONDITIONAL_JUMP` [`006ab0b4`](#insn-006ab0b4) → [`006aad40`](#insn-006aad40)
  - `FALL_THROUGH` [`006ab0b4`](#insn-006ab0b4) → [`006ab0b8`](#insn-006ab0b8)
- ブロック [`006ab0b8`](#insn-006ab0b8) 範囲 `[['006ab0b8', '006ab0eb']]`
  - `FALL_THROUGH` [`006ab0e8`](#insn-006ab0e8) → [`006ab0ec`](#insn-006ab0ec)
- ブロック [`006ab0ec`](#insn-006ab0ec) 範囲 `[['006ab0ec', '006ab0ff']]`
  - `UNCONDITIONAL_JUMP` [`006ab0fc`](#insn-006ab0fc) → [`006aad40`](#insn-006aad40)
- ブロック [`006ab100`](#insn-006ab100) 範囲 `[['006ab100', '006ab10b']]`
  - `FALL_THROUGH` [`006ab108`](#insn-006ab108) → [`006ab10c`](#insn-006ab10c)
- ブロック [`006ab10c`](#insn-006ab10c) 範囲 `[['006ab10c', '006ab10f']]`
  - `CONDITIONAL_JUMP` [`006ab10c`](#insn-006ab10c) → [`006aaed8`](#insn-006aaed8)
  - `FALL_THROUGH` [`006ab10c`](#insn-006ab10c) → [`006ab110`](#insn-006ab110)
- ブロック [`006ab110`](#insn-006ab110) 範囲 `[['006ab110', '006ab12b']]`
  - `FALL_THROUGH` [`006ab128`](#insn-006ab128) → [`006ab12c`](#insn-006ab12c)
- ブロック [`006ab12c`](#insn-006ab12c) 範囲 `[['006ab12c', '006ab153']]`
  - `UNCONDITIONAL_JUMP` [`006ab150`](#insn-006ab150) → [`006aaed8`](#insn-006aaed8)
- ブロック [`006ab19c`](#insn-006ab19c) 範囲 `[['006ab19c', '006ab19f']]`

## 命令位置別の参照

- [`006aabb0`](#insn-006aabb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabb4`](#insn-006aabb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabb8`](#insn-006aabb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabbc`](#insn-006aabbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabcc`](#insn-006aabcc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabd4`](#insn-006aabd4) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006aabd8`](#insn-006aabd8) → [`006aabfc`](#insn-006aabfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aabe0`](#insn-006aabe0) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006aabe8`](#insn-006aabe8) → `00c71290`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006aabf0`](#insn-006aabf0) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`006aabf8`](#insn-006aabf8) → [`006aac00`](#insn-006aac00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac04`](#insn-006aac04) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006aac10`](#insn-006aac10) → `00333fcc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006aac14`](#insn-006aac14) → [`006aad30`](#insn-006aad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac18`](#insn-006aac18) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`006aac24`](#insn-006aac24) → `00333fcc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006aac2c`](#insn-006aac2c) → [`006aafb0`](#insn-006aafb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac38`](#insn-006aac38) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aac3c`](#insn-006aac3c) → [`006aaffc`](#insn-006aaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac48`](#insn-006aac48) → `Stack[-0x6d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac4c`](#insn-006aac4c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac58`](#insn-006aac58) → `002a032e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aac5c`](#insn-006aac5c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac64`](#insn-006aac64) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac68`](#insn-006aac68) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac74`](#insn-006aac74) → `002c1528`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac78`](#insn-006aac78) → `002c152d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aac7c`](#insn-006aac7c) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac80`](#insn-006aac80) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac84`](#insn-006aac84) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aac9c`](#insn-006aac9c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006aaca4`](#insn-006aaca4) → [`0047e64c`](../0047e/0047e64c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e64c` · 推定シンボル `None` · 推定型 `None`
- [`006aaca8`](#insn-006aaca8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aacb0`](#insn-006aacb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aacb8`](#insn-006aacb8) → [`006aace4`](#insn-006aace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aacc4`](#insn-006aacc4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aacc8`](#insn-006aacc8) → [`006aace4`](#insn-006aace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aace0`](#insn-006aace0) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aace4`](#insn-006aace4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aace8`](#insn-006aace8) → [`006aad14`](#insn-006aad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aacf4`](#insn-006aacf4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aacf8`](#insn-006aacf8) → [`006aad14`](#insn-006aad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad10`](#insn-006aad10) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aad14`](#insn-006aad14) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad18`](#insn-006aad18) → [`006aae30`](#insn-006aae30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad1c`](#insn-006aad1c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad20`](#insn-006aad20) → [`006aae40`](#insn-006aae40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad24`](#insn-006aad24) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aad28`](#insn-006aad28) → [`006aae50`](#insn-006aae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad2c`](#insn-006aad2c) → [`006ab054`](#insn-006ab054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad38`](#insn-006aad38) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aad3c`](#insn-006aad3c) → [`006ab0a8`](#insn-006ab0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad48`](#insn-006aad48) → `Stack[-0x6d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad4c`](#insn-006aad4c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad58`](#insn-006aad58) → `002a032e`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aad5c`](#insn-006aad5c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad64`](#insn-006aad64) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad68`](#insn-006aad68) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad74`](#insn-006aad74) → `002c1528`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad78`](#insn-006aad78) → `002c152d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aad7c`](#insn-006aad7c) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad80`](#insn-006aad80) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad84`](#insn-006aad84) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aad9c`](#insn-006aad9c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006aada4`](#insn-006aada4) → [`0047e64c`](../0047e/0047e64c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e64c` · 推定シンボル `None` · 推定型 `None`
- [`006aada8`](#insn-006aada8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aadb0`](#insn-006aadb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aadb8`](#insn-006aadb8) → [`006aade4`](#insn-006aade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aadc4`](#insn-006aadc4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aadc8`](#insn-006aadc8) → [`006aade4`](#insn-006aade4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aade0`](#insn-006aade0) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aade4`](#insn-006aade4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aade8`](#insn-006aade8) → [`006aae14`](#insn-006aae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aadf4`](#insn-006aadf4) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aadf8`](#insn-006aadf8) → [`006aae14`](#insn-006aae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae10`](#insn-006aae10) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aae14`](#insn-006aae14) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae18`](#insn-006aae18) → [`006aaeb8`](#insn-006aaeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae1c`](#insn-006aae1c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae20`](#insn-006aae20) → [`006aaec8`](#insn-006aaec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae24`](#insn-006aae24) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aae28`](#insn-006aae28) → [`006aaed8`](#insn-006aaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae2c`](#insn-006aae2c) → [`006ab100`](#insn-006ab100) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae30`](#insn-006aae30) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae34`](#insn-006aae34) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aae38`](#insn-006aae38) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae3c`](#insn-006aae3c) → [`006aad24`](#insn-006aad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae40`](#insn-006aae40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae44`](#insn-006aae44) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aae48`](#insn-006aae48) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aae4c`](#insn-006aae4c) → [`006ab054`](#insn-006ab054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae58`](#insn-006aae58) → `Stack[-0x6d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae5c`](#insn-006aae5c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae68`](#insn-006aae68) → `002befe6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aae6c`](#insn-006aae6c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae74`](#insn-006aae74) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae78`](#insn-006aae78) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae84`](#insn-006aae84) → `002c01bd`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae88`](#insn-006aae88) → `002c01c2`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aae8c`](#insn-006aae8c) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae90`](#insn-006aae90) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae94`](#insn-006aae94) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aae9c`](#insn-006aae9c) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006aaeb0`](#insn-006aaeb0) → [`0047e64c`](../0047e/0047e64c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e64c` · 推定シンボル `None` · 推定型 `None`
- [`006aaeb4`](#insn-006aaeb4) → [`006aaf3c`](#insn-006aaf3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaeb8`](#insn-006aaeb8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaebc`](#insn-006aaebc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aaec0`](#insn-006aaec0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaec4`](#insn-006aaec4) → [`006aae24`](#insn-006aae24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaec8`](#insn-006aaec8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaecc`](#insn-006aaecc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aaed0`](#insn-006aaed0) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006aaed4`](#insn-006aaed4) → [`006ab100`](#insn-006ab100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaee0`](#insn-006aaee0) → `Stack[-0x6d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaee4`](#insn-006aaee4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaef0`](#insn-006aaef0) → `002a33e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aaef4`](#insn-006aaef4) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaefc`](#insn-006aaefc) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf00`](#insn-006aaf00) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf0c`](#insn-006aaf0c) → `0029f27b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf10`](#insn-006aaf10) → `0029f280`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`006aaf14`](#insn-006aaf14) → `Stack[-0x82]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf18`](#insn-006aaf18) → `Stack[-0x8f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf1c`](#insn-006aaf1c) → `Stack[-0x8a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf24`](#insn-006aaf24) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006aaf38`](#insn-006aaf38) → [`0047e64c`](../0047e/0047e64c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e64c` · 推定シンボル `None` · 推定型 `None`
- [`006aaf3c`](#insn-006aaf3c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf44`](#insn-006aaf44) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf4c`](#insn-006aaf4c) → [`006aaf78`](#insn-006aaf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf58`](#insn-006aaf58) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aaf5c`](#insn-006aaf5c) → [`006aaf78`](#insn-006aaf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf74`](#insn-006aaf74) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aaf78`](#insn-006aaf78) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf7c`](#insn-006aaf7c) → [`006aaf90`](#insn-006aaf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf88`](#insn-006aaf88) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`006aaf8c`](#insn-006aaf8c) → [`006aafd8`](#insn-006aafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf90`](#insn-006aaf90) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf94`](#insn-006aaf94) → [`006aafa0`](#insn-006aafa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf98`](#insn-006aaf98) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaf9c`](#insn-006aaf9c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aafa0`](#insn-006aafa0) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafa4`](#insn-006aafa4) → [`006aafb0`](#insn-006aafb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafa8`](#insn-006aafa8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafac`](#insn-006aafac) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`006aafb4`](#insn-006aafb4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafbc`](#insn-006aafbc) → [`006ab19c`](#insn-006ab19c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafc0`](#insn-006aafc0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafc4`](#insn-006aafc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafc8`](#insn-006aafc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafcc`](#insn-006aafcc) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aafec`](#insn-006aafec) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`006aaff0`](#insn-006aaff0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaff4`](#insn-006aaff4) → [`006aaf98`](#insn-006aaf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aaff8`](#insn-006aaff8) → [`006aafa0`](#insn-006aafa0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab000`](#insn-006ab000) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab004`](#insn-006ab004) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`006ab008`](#insn-006ab008) → [`006aac40`](#insn-006aac40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab010`](#insn-006ab010) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab018`](#insn-006ab018) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`006ab024`](#insn-006ab024) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006ab028`](#insn-006ab028) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab02c`](#insn-006ab02c) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab02c`](#insn-006ab02c) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab034`](#insn-006ab034) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab034`](#insn-006ab034) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab038`](#insn-006ab038) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab03c`](#insn-006ab03c) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab03c`](#insn-006ab03c) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab03c`](#insn-006ab03c) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab040`](#insn-006ab040) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`006ab048`](#insn-006ab048) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab04c`](#insn-006ab04c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`006ab050`](#insn-006ab050) → [`006aac40`](#insn-006aac40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab058`](#insn-006ab058) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab05c`](#insn-006ab05c) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`006ab060`](#insn-006ab060) → [`006aae50`](#insn-006aae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab06c`](#insn-006ab06c) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`006ab070`](#insn-006ab070) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab078`](#insn-006ab078) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006ab07c`](#insn-006ab07c) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab07c`](#insn-006ab07c) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab084`](#insn-006ab084) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab088`](#insn-006ab088) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab088`](#insn-006ab088) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab08c`](#insn-006ab08c) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab090`](#insn-006ab090) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab090`](#insn-006ab090) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab090`](#insn-006ab090) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab094`](#insn-006ab094) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`006ab09c`](#insn-006ab09c) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab0a0`](#insn-006ab0a0) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`006ab0a4`](#insn-006ab0a4) → [`006aae50`](#insn-006aae50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab0ac`](#insn-006ab0ac) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab0b0`](#insn-006ab0b0) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`006ab0b4`](#insn-006ab0b4) → [`006aad40`](#insn-006aad40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab0bc`](#insn-006ab0bc) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0c4`](#insn-006ab0c4) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`006ab0d0`](#insn-006ab0d0) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006ab0d4`](#insn-006ab0d4) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0d8`](#insn-006ab0d8) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0d8`](#insn-006ab0d8) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e0`](#insn-006ab0e0) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e0`](#insn-006ab0e0) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e4`](#insn-006ab0e4) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e8`](#insn-006ab0e8) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e8`](#insn-006ab0e8) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0e8`](#insn-006ab0e8) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab0ec`](#insn-006ab0ec) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`006ab0f4`](#insn-006ab0f4) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab0f8`](#insn-006ab0f8) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`006ab0fc`](#insn-006ab0fc) → [`006aad40`](#insn-006aad40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab104`](#insn-006ab104) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab108`](#insn-006ab108) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`006ab10c`](#insn-006ab10c) → [`006aaed8`](#insn-006aaed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab118`](#insn-006ab118) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`006ab11c`](#insn-006ab11c) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab124`](#insn-006ab124) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`006ab128`](#insn-006ab128) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab128`](#insn-006ab128) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab130`](#insn-006ab130) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab134`](#insn-006ab134) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab134`](#insn-006ab134) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab138`](#insn-006ab138) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab13c`](#insn-006ab13c) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab13c`](#insn-006ab13c) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab13c`](#insn-006ab13c) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006ab140`](#insn-006ab140) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`006ab148`](#insn-006ab148) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`006ab14c`](#insn-006ab14c) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`006ab150`](#insn-006ab150) → [`006aaed8`](#insn-006aaed8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ab19c`](#insn-006ab19c) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006aabb0`](#insn-006aabb0)

~~~json
{
  "source": "006aabb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabb4`](#insn-006aabb4)

~~~json
{
  "source": "006aabb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabb8`](#insn-006aabb8)

~~~json
{
  "source": "006aabb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabbc`](#insn-006aabbc)

~~~json
{
  "source": "006aabbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabcc`](#insn-006aabcc)

~~~json
{
  "source": "006aabcc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabd4`](#insn-006aabd4)

~~~json
{
  "source": "006aabd4",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aabd8`](#insn-006aabd8)

~~~json
{
  "source": "006aabd8",
  "target": "006aabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aabe0`](#insn-006aabe0)

~~~json
{
  "source": "006aabe0",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006aabe8`](#insn-006aabe8)

~~~json
{
  "source": "006aabe8",
  "target": "00c71290",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c71290",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006aabf0`](#insn-006aabf0)

~~~json
{
  "source": "006aabf0",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aabf8`](#insn-006aabf8)

~~~json
{
  "source": "006aabf8",
  "target": "006aac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac04`](#insn-006aac04)

~~~json
{
  "source": "006aac04",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aac10`](#insn-006aac10)

~~~json
{
  "source": "006aac10",
  "target": "00333fcc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "bcb76c00dc8d0900",
  "capture_start": "00333fc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aac14`](#insn-006aac14)

~~~json
{
  "source": "006aac14",
  "target": "006aad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac18`](#insn-006aac18)

~~~json
{
  "source": "006aac18",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aac24`](#insn-006aac24)

~~~json
{
  "source": "006aac24",
  "target": "00333fcc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333fc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "bcb76c00dc8d0900",
  "capture_start": "00333fc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aac2c`](#insn-006aac2c)

~~~json
{
  "source": "006aac2c",
  "target": "006aafb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac38`](#insn-006aac38)

~~~json
{
  "source": "006aac38",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aac3c`](#insn-006aac3c)

~~~json
{
  "source": "006aac3c",
  "target": "006aaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac48`](#insn-006aac48)

~~~json
{
  "source": "006aac48",
  "target": "Stack[-0x6d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac4c`](#insn-006aac4c)

~~~json
{
  "source": "006aac4c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac58`](#insn-006aac58)

~~~json
{
  "source": "006aac58",
  "target": "002a032e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a032e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032322e706e6700",
  "capture_start": "002a032e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aac5c`](#insn-006aac5c)

~~~json
{
  "source": "006aac5c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac64`](#insn-006aac64)

~~~json
{
  "source": "006aac64",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac68`](#insn-006aac68)

~~~json
{
  "source": "006aac68",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac74`](#insn-006aac74)

~~~json
{
  "source": "006aac74",
  "target": "002c1528",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac78`](#insn-006aac78)

~~~json
{
  "source": "006aac78",
  "target": "002c152d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c152d",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "322e696d6763757400",
  "capture_start": "002c152d",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aac7c`](#insn-006aac7c)

~~~json
{
  "source": "006aac7c",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac80`](#insn-006aac80)

~~~json
{
  "source": "006aac80",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac84`](#insn-006aac84)

~~~json
{
  "source": "006aac84",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aac9c`](#insn-006aac9c)

~~~json
{
  "source": "006aac9c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aaca4`](#insn-006aaca4)

~~~json
{
  "source": "006aaca4",
  "target": "0047e64c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaca8`](#insn-006aaca8)

~~~json
{
  "source": "006aaca8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aacb0`](#insn-006aacb0)

~~~json
{
  "source": "006aacb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aacb8`](#insn-006aacb8)

~~~json
{
  "source": "006aacb8",
  "target": "006aace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aacc4`](#insn-006aacc4)

~~~json
{
  "source": "006aacc4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aacc8`](#insn-006aacc8)

~~~json
{
  "source": "006aacc8",
  "target": "006aace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aace0`](#insn-006aace0)

~~~json
{
  "source": "006aace0",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aace4`](#insn-006aace4)

~~~json
{
  "source": "006aace4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aace8`](#insn-006aace8)

~~~json
{
  "source": "006aace8",
  "target": "006aad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aacf4`](#insn-006aacf4)

~~~json
{
  "source": "006aacf4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aacf8`](#insn-006aacf8)

~~~json
{
  "source": "006aacf8",
  "target": "006aad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad10`](#insn-006aad10)

~~~json
{
  "source": "006aad10",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aad14`](#insn-006aad14)

~~~json
{
  "source": "006aad14",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad18`](#insn-006aad18)

~~~json
{
  "source": "006aad18",
  "target": "006aae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad1c`](#insn-006aad1c)

~~~json
{
  "source": "006aad1c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad20`](#insn-006aad20)

~~~json
{
  "source": "006aad20",
  "target": "006aae40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad24`](#insn-006aad24)

~~~json
{
  "source": "006aad24",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aad28`](#insn-006aad28)

~~~json
{
  "source": "006aad28",
  "target": "006aae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad2c`](#insn-006aad2c)

~~~json
{
  "source": "006aad2c",
  "target": "006ab054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad38`](#insn-006aad38)

~~~json
{
  "source": "006aad38",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aad3c`](#insn-006aad3c)

~~~json
{
  "source": "006aad3c",
  "target": "006ab0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad48`](#insn-006aad48)

~~~json
{
  "source": "006aad48",
  "target": "Stack[-0x6d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad4c`](#insn-006aad4c)

~~~json
{
  "source": "006aad4c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad58`](#insn-006aad58)

~~~json
{
  "source": "006aad58",
  "target": "002a032e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a032e",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032322e706e6700",
  "capture_start": "002a032e",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aad5c`](#insn-006aad5c)

~~~json
{
  "source": "006aad5c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad64`](#insn-006aad64)

~~~json
{
  "source": "006aad64",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad68`](#insn-006aad68)

~~~json
{
  "source": "006aad68",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad74`](#insn-006aad74)

~~~json
{
  "source": "006aad74",
  "target": "002c1528",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad78`](#insn-006aad78)

~~~json
{
  "source": "006aad78",
  "target": "002c152d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c152d",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "322e696d6763757400",
  "capture_start": "002c152d",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aad7c`](#insn-006aad7c)

~~~json
{
  "source": "006aad7c",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad80`](#insn-006aad80)

~~~json
{
  "source": "006aad80",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad84`](#insn-006aad84)

~~~json
{
  "source": "006aad84",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aad9c`](#insn-006aad9c)

~~~json
{
  "source": "006aad9c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aada4`](#insn-006aada4)

~~~json
{
  "source": "006aada4",
  "target": "0047e64c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aada8`](#insn-006aada8)

~~~json
{
  "source": "006aada8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aadb0`](#insn-006aadb0)

~~~json
{
  "source": "006aadb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aadb8`](#insn-006aadb8)

~~~json
{
  "source": "006aadb8",
  "target": "006aade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aadc4`](#insn-006aadc4)

~~~json
{
  "source": "006aadc4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aadc8`](#insn-006aadc8)

~~~json
{
  "source": "006aadc8",
  "target": "006aade4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aade0`](#insn-006aade0)

~~~json
{
  "source": "006aade0",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aade4`](#insn-006aade4)

~~~json
{
  "source": "006aade4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aade8`](#insn-006aade8)

~~~json
{
  "source": "006aade8",
  "target": "006aae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aadf4`](#insn-006aadf4)

~~~json
{
  "source": "006aadf4",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aadf8`](#insn-006aadf8)

~~~json
{
  "source": "006aadf8",
  "target": "006aae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae10`](#insn-006aae10)

~~~json
{
  "source": "006aae10",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aae14`](#insn-006aae14)

~~~json
{
  "source": "006aae14",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae18`](#insn-006aae18)

~~~json
{
  "source": "006aae18",
  "target": "006aaeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae1c`](#insn-006aae1c)

~~~json
{
  "source": "006aae1c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae20`](#insn-006aae20)

~~~json
{
  "source": "006aae20",
  "target": "006aaec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae24`](#insn-006aae24)

~~~json
{
  "source": "006aae24",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aae28`](#insn-006aae28)

~~~json
{
  "source": "006aae28",
  "target": "006aaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae2c`](#insn-006aae2c)

~~~json
{
  "source": "006aae2c",
  "target": "006ab100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae30`](#insn-006aae30)

~~~json
{
  "source": "006aae30",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae34`](#insn-006aae34)

~~~json
{
  "source": "006aae34",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aae38`](#insn-006aae38)

~~~json
{
  "source": "006aae38",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae3c`](#insn-006aae3c)

~~~json
{
  "source": "006aae3c",
  "target": "006aad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae40`](#insn-006aae40)

~~~json
{
  "source": "006aae40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae44`](#insn-006aae44)

~~~json
{
  "source": "006aae44",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aae48`](#insn-006aae48)

~~~json
{
  "source": "006aae48",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aae4c`](#insn-006aae4c)

~~~json
{
  "source": "006aae4c",
  "target": "006ab054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae58`](#insn-006aae58)

~~~json
{
  "source": "006aae58",
  "target": "Stack[-0x6d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae5c`](#insn-006aae5c)

~~~json
{
  "source": "006aae5c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae68`](#insn-006aae68)

~~~json
{
  "source": "006aae68",
  "target": "002befe6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002befe6",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032372e706e6700",
  "capture_start": "002befe6",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aae6c`](#insn-006aae6c)

~~~json
{
  "source": "006aae6c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae74`](#insn-006aae74)

~~~json
{
  "source": "006aae74",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae78`](#insn-006aae78)

~~~json
{
  "source": "006aae78",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae84`](#insn-006aae84)

~~~json
{
  "source": "006aae84",
  "target": "002c01bd",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae88`](#insn-006aae88)

~~~json
{
  "source": "006aae88",
  "target": "002c01c2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c01c2",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "372e696d6763757400",
  "capture_start": "002c01c2",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aae8c`](#insn-006aae8c)

~~~json
{
  "source": "006aae8c",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae90`](#insn-006aae90)

~~~json
{
  "source": "006aae90",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae94`](#insn-006aae94)

~~~json
{
  "source": "006aae94",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aae9c`](#insn-006aae9c)

~~~json
{
  "source": "006aae9c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aaeb0`](#insn-006aaeb0)

~~~json
{
  "source": "006aaeb0",
  "target": "0047e64c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaeb4`](#insn-006aaeb4)

~~~json
{
  "source": "006aaeb4",
  "target": "006aaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaeb8`](#insn-006aaeb8)

~~~json
{
  "source": "006aaeb8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaebc`](#insn-006aaebc)

~~~json
{
  "source": "006aaebc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaec0`](#insn-006aaec0)

~~~json
{
  "source": "006aaec0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaec4`](#insn-006aaec4)

~~~json
{
  "source": "006aaec4",
  "target": "006aae24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaec8`](#insn-006aaec8)

~~~json
{
  "source": "006aaec8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaecc`](#insn-006aaecc)

~~~json
{
  "source": "006aaecc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaed0`](#insn-006aaed0)

~~~json
{
  "source": "006aaed0",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aaed4`](#insn-006aaed4)

~~~json
{
  "source": "006aaed4",
  "target": "006ab100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaee0`](#insn-006aaee0)

~~~json
{
  "source": "006aaee0",
  "target": "Stack[-0x6d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaee4`](#insn-006aaee4)

~~~json
{
  "source": "006aaee4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaef0`](#insn-006aaef0)

~~~json
{
  "source": "006aaef0",
  "target": "002a33e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a33e0",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "696d673032332e706e6700",
  "capture_start": "002a33e0",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aaef4`](#insn-006aaef4)

~~~json
{
  "source": "006aaef4",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaefc`](#insn-006aaefc)

~~~json
{
  "source": "006aaefc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf00`](#insn-006aaf00)

~~~json
{
  "source": "006aaf00",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf0c`](#insn-006aaf0c)

~~~json
{
  "source": "006aaf0c",
  "target": "0029f27b",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf10`](#insn-006aaf10)

~~~json
{
  "source": "006aaf10",
  "target": "0029f280",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f280",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "332e696d6763757400",
  "capture_start": "0029f280",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006aaf14`](#insn-006aaf14)

~~~json
{
  "source": "006aaf14",
  "target": "Stack[-0x82]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf18`](#insn-006aaf18)

~~~json
{
  "source": "006aaf18",
  "target": "Stack[-0x8f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf1c`](#insn-006aaf1c)

~~~json
{
  "source": "006aaf1c",
  "target": "Stack[-0x8a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf24`](#insn-006aaf24)

~~~json
{
  "source": "006aaf24",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006aaf38`](#insn-006aaf38)

~~~json
{
  "source": "006aaf38",
  "target": "0047e64c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaf3c`](#insn-006aaf3c)

~~~json
{
  "source": "006aaf3c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf44`](#insn-006aaf44)

~~~json
{
  "source": "006aaf44",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf4c`](#insn-006aaf4c)

~~~json
{
  "source": "006aaf4c",
  "target": "006aaf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf58`](#insn-006aaf58)

~~~json
{
  "source": "006aaf58",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaf5c`](#insn-006aaf5c)

~~~json
{
  "source": "006aaf5c",
  "target": "006aaf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf74`](#insn-006aaf74)

~~~json
{
  "source": "006aaf74",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaf78`](#insn-006aaf78)

~~~json
{
  "source": "006aaf78",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf7c`](#insn-006aaf7c)

~~~json
{
  "source": "006aaf7c",
  "target": "006aaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf88`](#insn-006aaf88)

~~~json
{
  "source": "006aaf88",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaf8c`](#insn-006aaf8c)

~~~json
{
  "source": "006aaf8c",
  "target": "006aafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf90`](#insn-006aaf90)

~~~json
{
  "source": "006aaf90",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf94`](#insn-006aaf94)

~~~json
{
  "source": "006aaf94",
  "target": "006aafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf98`](#insn-006aaf98)

~~~json
{
  "source": "006aaf98",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaf9c`](#insn-006aaf9c)

~~~json
{
  "source": "006aaf9c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aafa0`](#insn-006aafa0)

~~~json
{
  "source": "006aafa0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafa4`](#insn-006aafa4)

~~~json
{
  "source": "006aafa4",
  "target": "006aafb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafa8`](#insn-006aafa8)

~~~json
{
  "source": "006aafa8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafac`](#insn-006aafac)

~~~json
{
  "source": "006aafac",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aafb4`](#insn-006aafb4)

~~~json
{
  "source": "006aafb4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafbc`](#insn-006aafbc)

~~~json
{
  "source": "006aafbc",
  "target": "006ab19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafc0`](#insn-006aafc0)

~~~json
{
  "source": "006aafc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafc4`](#insn-006aafc4)

~~~json
{
  "source": "006aafc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafc8`](#insn-006aafc8)

~~~json
{
  "source": "006aafc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafcc`](#insn-006aafcc)

~~~json
{
  "source": "006aafcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aafec`](#insn-006aafec)

~~~json
{
  "source": "006aafec",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aaff0`](#insn-006aaff0)

~~~json
{
  "source": "006aaff0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaff4`](#insn-006aaff4)

~~~json
{
  "source": "006aaff4",
  "target": "006aaf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aaff8`](#insn-006aaff8)

~~~json
{
  "source": "006aaff8",
  "target": "006aafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab000`](#insn-006ab000)

~~~json
{
  "source": "006ab000",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab004`](#insn-006ab004)

~~~json
{
  "source": "006ab004",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab008`](#insn-006ab008)

~~~json
{
  "source": "006ab008",
  "target": "006aac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab010`](#insn-006ab010)

~~~json
{
  "source": "006ab010",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab018`](#insn-006ab018)

~~~json
{
  "source": "006ab018",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab024`](#insn-006ab024)

~~~json
{
  "source": "006ab024",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006ab028`](#insn-006ab028)

~~~json
{
  "source": "006ab028",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab02c`](#insn-006ab02c)

~~~json
{
  "source": "006ab02c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab02c`](#insn-006ab02c)

~~~json
{
  "source": "006ab02c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab034`](#insn-006ab034)

~~~json
{
  "source": "006ab034",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab034`](#insn-006ab034)

~~~json
{
  "source": "006ab034",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab038`](#insn-006ab038)

~~~json
{
  "source": "006ab038",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab03c`](#insn-006ab03c)

~~~json
{
  "source": "006ab03c",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab03c`](#insn-006ab03c)

~~~json
{
  "source": "006ab03c",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab03c`](#insn-006ab03c)

~~~json
{
  "source": "006ab03c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab040`](#insn-006ab040)

~~~json
{
  "source": "006ab040",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab048`](#insn-006ab048)

~~~json
{
  "source": "006ab048",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab04c`](#insn-006ab04c)

~~~json
{
  "source": "006ab04c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab050`](#insn-006ab050)

~~~json
{
  "source": "006ab050",
  "target": "006aac40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab058`](#insn-006ab058)

~~~json
{
  "source": "006ab058",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab05c`](#insn-006ab05c)

~~~json
{
  "source": "006ab05c",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab060`](#insn-006ab060)

~~~json
{
  "source": "006ab060",
  "target": "006aae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab06c`](#insn-006ab06c)

~~~json
{
  "source": "006ab06c",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab070`](#insn-006ab070)

~~~json
{
  "source": "006ab070",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab078`](#insn-006ab078)

~~~json
{
  "source": "006ab078",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006ab07c`](#insn-006ab07c)

~~~json
{
  "source": "006ab07c",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab07c`](#insn-006ab07c)

~~~json
{
  "source": "006ab07c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab084`](#insn-006ab084)

~~~json
{
  "source": "006ab084",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab088`](#insn-006ab088)

~~~json
{
  "source": "006ab088",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab088`](#insn-006ab088)

~~~json
{
  "source": "006ab088",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab08c`](#insn-006ab08c)

~~~json
{
  "source": "006ab08c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab090`](#insn-006ab090)

~~~json
{
  "source": "006ab090",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab090`](#insn-006ab090)

~~~json
{
  "source": "006ab090",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab090`](#insn-006ab090)

~~~json
{
  "source": "006ab090",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab094`](#insn-006ab094)

~~~json
{
  "source": "006ab094",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab09c`](#insn-006ab09c)

~~~json
{
  "source": "006ab09c",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0a0`](#insn-006ab0a0)

~~~json
{
  "source": "006ab0a0",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab0a4`](#insn-006ab0a4)

~~~json
{
  "source": "006ab0a4",
  "target": "006aae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab0ac`](#insn-006ab0ac)

~~~json
{
  "source": "006ab0ac",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0b0`](#insn-006ab0b0)

~~~json
{
  "source": "006ab0b0",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab0b4`](#insn-006ab0b4)

~~~json
{
  "source": "006ab0b4",
  "target": "006aad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab0bc`](#insn-006ab0bc)

~~~json
{
  "source": "006ab0bc",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0c4`](#insn-006ab0c4)

~~~json
{
  "source": "006ab0c4",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab0d0`](#insn-006ab0d0)

~~~json
{
  "source": "006ab0d0",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006ab0d4`](#insn-006ab0d4)

~~~json
{
  "source": "006ab0d4",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0d8`](#insn-006ab0d8)

~~~json
{
  "source": "006ab0d8",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0d8`](#insn-006ab0d8)

~~~json
{
  "source": "006ab0d8",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e0`](#insn-006ab0e0)

~~~json
{
  "source": "006ab0e0",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e0`](#insn-006ab0e0)

~~~json
{
  "source": "006ab0e0",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e4`](#insn-006ab0e4)

~~~json
{
  "source": "006ab0e4",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e8`](#insn-006ab0e8)

~~~json
{
  "source": "006ab0e8",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e8`](#insn-006ab0e8)

~~~json
{
  "source": "006ab0e8",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0e8`](#insn-006ab0e8)

~~~json
{
  "source": "006ab0e8",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0ec`](#insn-006ab0ec)

~~~json
{
  "source": "006ab0ec",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab0f4`](#insn-006ab0f4)

~~~json
{
  "source": "006ab0f4",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab0f8`](#insn-006ab0f8)

~~~json
{
  "source": "006ab0f8",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab0fc`](#insn-006ab0fc)

~~~json
{
  "source": "006ab0fc",
  "target": "006aad40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab104`](#insn-006ab104)

~~~json
{
  "source": "006ab104",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab108`](#insn-006ab108)

~~~json
{
  "source": "006ab108",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab10c`](#insn-006ab10c)

~~~json
{
  "source": "006ab10c",
  "target": "006aaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab118`](#insn-006ab118)

~~~json
{
  "source": "006ab118",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab11c`](#insn-006ab11c)

~~~json
{
  "source": "006ab11c",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab124`](#insn-006ab124)

~~~json
{
  "source": "006ab124",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006ab128`](#insn-006ab128)

~~~json
{
  "source": "006ab128",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab128`](#insn-006ab128)

~~~json
{
  "source": "006ab128",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab130`](#insn-006ab130)

~~~json
{
  "source": "006ab130",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab134`](#insn-006ab134)

~~~json
{
  "source": "006ab134",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab134`](#insn-006ab134)

~~~json
{
  "source": "006ab134",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab138`](#insn-006ab138)

~~~json
{
  "source": "006ab138",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab13c`](#insn-006ab13c)

~~~json
{
  "source": "006ab13c",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab13c`](#insn-006ab13c)

~~~json
{
  "source": "006ab13c",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab13c`](#insn-006ab13c)

~~~json
{
  "source": "006ab13c",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab140`](#insn-006ab140)

~~~json
{
  "source": "006ab140",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab148`](#insn-006ab148)

~~~json
{
  "source": "006ab148",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006ab14c`](#insn-006ab14c)

~~~json
{
  "source": "006ab14c",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ab150`](#insn-006ab150)

~~~json
{
  "source": "006ab150",
  "target": "006aaed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ab19c`](#insn-006ab19c)

~~~json
{
  "source": "006ab19c",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
