# 007adedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007adedc",
  "name": "FUN_007adedc",
  "size": 960,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08afd7b3bc3f89ea555783d7e6c8924f315d95a26312006d197caf3f65840b4a",
  "source_text_sha256": "08afd7b3bc3f89ea555783d7e6c8924f315d95a26312006d197caf3f65840b4a"
}
~~~

## 呼び出し元

- [007add18](../007ad/007add18.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00598af4](../00598/00598af4.md)
- [00598cb4](../00598/00598cb4.md)
- [005a4fd8](../005a4/005a4fd8.md)
- [00795de4](../00795/00795de4.md)
- [00795e1c](../00795/00795e1c.md)
- [007afefc](../007af/007afefc.md)
- [007b0248](../007b0/007b0248.md)
- [007b04b4](../007b0/007b04b4.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"t{"
~~~

## 疑似コード / UTF-8 5598 bytes

~~~c

void FUN_007adedc(undefined8 param_1,ulong *param_2,long *param_3,long *param_4)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  ulong *puVar4;
  ulong uVar5;
  undefined8 uVar6;
  long lVar7;
  undefined8 local_108;
  long *local_100;
  undefined8 *local_f8;
  undefined8 local_f0;
  long *local_e8;
  long local_e0 [4];
  long *local_c0;
  long local_b0 [4];
  long *local_90;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong *local_60;
  long local_48;
  
                    /* catch() { ... } // from try @ 007ae07c with catch @ 007adef0
                       catch() { ... } // from try @ 007ae9b0 with catch @ 007adef0
                       catch() { ... } // from try @ 007aec04 with catch @ 007adef0 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)_Znwm(0x50);
  if ((*param_2 & 1) == 0) {
    uStack_78 = param_2[1];
    local_80 = *param_2;
    local_70 = (void *)param_2[2];
  }
  else {
    FUN_0043bae0(&local_80,param_2[2],param_2[1]);
  }
  FUN_005a4fd8(puVar2,&local_80);
  local_f8 = puVar2;
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  FUN_007afefc(&local_f0,&local_80,&local_f8);
  puVar2 = local_f8;
  local_f8 = (undefined8 *)0x0;
  if (puVar2 != (undefined8 *)0x0) {
    if ((*(byte *)(puVar2 + 7) & 1) != 0) {
      _ZdlPv((void *)puVar2[9]);
    }
                    /* try { // try from 007adf8c to 008adf93 has its CatchHandler @ 007aef4c */
                    /* try { // try from 007adf94 to 008adf9f has its CatchHandler @ 007aef34 */
    *puVar2 = &PTR_FUN_00c6d620;
    if ((*(byte *)(puVar2 + 4) & 1) != 0) {
                    /* try { // try from 007adfa4 to 008adfab has its CatchHandler @ 007aef24 */
      _ZdlPv((void *)puVar2[6]);
    }
    if ((*(byte *)(puVar2 + 1) & 1) != 0) {
      _ZdlPv((void *)puVar2[3]);
    }
    _ZdlPv(puVar2);
  }
  uVar6 = local_f0;
  plVar3 = (long *)param_3[4];
  local_90 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_3) {
      local_90 = local_b0;
      (**(code **)(*param_3 + 0x18))(param_3,local_b0);
    }
    else {
      local_90 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_60 = (ulong *)0x0;
                    /* try { // try from 007ae00c to 008ae017 has its CatchHandler @ 007aeeb0 */
  puVar4 = (ulong *)_Znwm(0x40);
  *puVar4 = (ulong)&PTR_FUN_00c7a698;
  uVar5 = 0;
  if (local_90 == (long *)0x0) {
LAB_007ae048:
    puVar4[6] = uVar5;
  }
  else {
    if (local_90 != local_b0) {
      uVar5 = (**(code **)(*local_90 + 0x10))();
      goto LAB_007ae048;
    }
    puVar4[6] = (ulong)(puVar4 + 2);
                    /* try { // try from 007ae058 to 008ae06b has its CatchHandler @ 007aee84 */
    (**(code **)(local_b0[0] + 0x18))(local_b0);
  }
                    /* try { // try from 007ae06c to 008ae07b has its CatchHandler @ 007aee70 */
  local_60 = puVar4;
  FUN_00598af4(uVar6,&local_80);
                    /* try { // try from 007ae07c to 008ae277 has its CatchHandler @ 007adef0 */
  if (local_60 == &local_80) {
    lVar7 = 0x20;
    puVar4 = &local_80;
LAB_007ae098:
    (**(code **)(*puVar4 + lVar7))();
  }
  else if (local_60 != (ulong *)0x0) {
    lVar7 = 0x28;
    puVar4 = local_60;
    goto LAB_007ae098;
  }
  if (local_90 == local_b0) {
    lVar7 = 0x20;
    plVar3 = local_b0;
LAB_007ae0c8:
    (**(code **)(*plVar3 + lVar7))();
  }
  else if (local_90 != (long *)0x0) {
    lVar7 = 0x28;
    plVar3 = local_90;
    goto LAB_007ae0c8;
  }
  uVar6 = local_f0;
  plVar3 = (long *)param_4[4];
  local_c0 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_4) {
      local_c0 = local_e0;
      (**(code **)(*param_4 + 0x18))(param_4,local_e0);
    }
    else {
      local_c0 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_60 = (ulong *)0x0;
  puVar4 = (ulong *)_Znwm(0x40);
  *puVar4 = (ulong)&PTR_FUN_00c7a718;
  uVar5 = 0;
  if (local_c0 == (long *)0x0) {
LAB_007ae158:
    puVar4[6] = uVar5;
  }
  else {
    if (local_c0 != local_e0) {
      uVar5 = (**(code **)(*local_c0 + 0x10))();
      goto LAB_007ae158;
    }
    puVar4[6] = (ulong)(puVar4 + 2);
    (**(code **)(local_e0[0] + 0x18))(local_e0);
  }
  local_60 = puVar4;
  FUN_00598cb4(uVar6,&local_80);
  if (local_60 == &local_80) {
    lVar7 = 0x20;
    puVar4 = &local_80;
LAB_007ae1a8:
    (**(code **)(*puVar4 + lVar7))();
  }
  else if (local_60 != (ulong *)0x0) {
    lVar7 = 0x28;
    puVar4 = local_60;
    goto LAB_007ae1a8;
  }
  if (local_c0 == local_e0) {
    lVar7 = 0x20;
    plVar3 = local_e0;
  }
  else {
    if (local_c0 == (long *)0x0) goto LAB_007ae1e4;
    lVar7 = 0x28;
    plVar3 = local_c0;
  }
  (**(code **)(*plVar3 + lVar7))();
LAB_007ae1e4:
  uVar6 = FUN_00795de4();
  local_108 = local_f0;
  local_100 = local_e8;
  if (local_e8 != (long *)0x0) {
    FUN_00c538b0(1,local_e8 + 1);
  }
  FUN_00795e1c(uVar6,&local_108);
  plVar3 = local_100;
  if ((local_100 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,local_100 + 1), lVar7 == 0)) {
    (**(code **)(*plVar3 + 0x10))(plVar3);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
  }
  if ((local_e8 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,local_e8 + 1), lVar7 == 0)) {
    (**(code **)(*local_e8 + 0x10))(local_e8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_e8);
  }
                    /* try { // try from 007ae278 to 008ae27b has its CatchHandler @ 007aeff8 */
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
