# 00a6dadc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a6dadc",
  "name": "FUN_00a6dadc",
  "size": 1552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "375653e9b3683ddd762f76015aa45d78d43300c7ac356a959dbd6f765cc88477",
  "source_text_sha256": "375653e9b3683ddd762f76015aa45d78d43300c7ac356a959dbd6f765cc88477"
}
~~~

## 呼び出し元

- [00856dec](../00856/00856dec.md)

## 呼び出し先

- [0046c984](../0046c/0046c984.md)
- [0047e89c](../0047e/0047e89c.md)
- [00752b90](../00752/00752b90.md)
- [009cc9e0](../009cc/009cc9e0.md)
- [009d590c](../009d5/009d590c.md)
- [00a6cce4](../00a6c/00a6cce4.md)
- [00ab27e8](../00ab2/00ab27e8.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 9643 bytes

~~~c

void FUN_00a6dadc(long param_1)

{
  int *piVar1;
  long lVar2;
  int iVar3;
  int iVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  long *plVar8;
  long *plVar9;
  undefined8 local_80;
  long *plStack_78;
  long local_68;
  
  plVar8 = DAT_00ca4568;
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  DAT_00ca4568 = DAT_00ca4578;
  DAT_00ca4578 = plVar8;
  uVar5 = _Znwm(0x430);
  FUN_00a6cce4(uVar5,param_1);
  piVar1 = (int *)((long)&fde_table_entry_00332070.data_loc + param_1);
  if (DAT_00ca4578 != (long *)0x0) {
    lVar7 = *DAT_00ca4578;
    DAT_00ca4578 = (long *)uVar5;
    (**(code **)(lVar7 + 8))();
    uVar5 = DAT_00ca4578;
  }
  DAT_00ca4578 = (long *)uVar5;
  FUN_009d590c(param_1);
  lVar7 = -0x3bc0;
  do {
    plVar8 = *(long **)(param_1 + lVar7 + 0x74e0);
    lVar6 = param_1 + 0x3918 + lVar7;
    *(undefined8 *)(lVar6 + 0x3bc8) = 0;
    *(undefined8 *)(lVar6 + 0x3bc0) = 0;
    if ((plVar8 != (long *)0x0) && (lVar6 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar6 == 0)
       ) {
      (**(code **)(*plVar8 + 0x10))(plVar8);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
    }
    lVar7 = lVar7 + 0x10;
  } while (lVar7 != 0);
  *(undefined8 *)((long)&fde_table_entry_00332a20.data_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 2) = 0;
  *piVar1 = 0;
  *(undefined8 *)((long)&fde_table_entry_00335ee0.data_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00335ed8.data_loc + param_1) = 0;
  *(undefined4 *)((long)&fde_table_entry_00335ee8.initial_loc + param_1 + 3) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f90.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f88.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fa0.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333f98.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fb0.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fa8.initial_loc + param_1) = 0;
  *(undefined8 *)((long)&fde_table_entry_00333fb8.initial_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00335ed8.data_loc + param_1 + 3) = 1;
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
                    /* try { // try from 00a6dfc8 to 00b6dfd7 has its CatchHandler @ 00a77ca8 */
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
                    /* try { // try from 00a6dfd8 to 00b6e047 has its CatchHandler @ 00a63e3c */
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330d10.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x2e,0,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7540);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7540) = plVar8;
  *(undefined8 *)(param_1 + 0x7538) = uVar5;
                    /* try { // try from 00a6dc80 to 00b6dc8f has its CatchHandler @ 00a77d48 */
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
                    /* try { // try from 00a6dccc to 00b6dcdb has its CatchHandler @ 00a77d44 */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330d28.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x18,0,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7550);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7550) = plVar8;
  *(undefined8 *)(param_1 + 0x7548) = uVar5;
                    /* try { // try from 00a6dd18 to 00b6dd27 has its CatchHandler @ 00a77d40 */
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
    (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00a6dd64 to 00b6ddbf has its CatchHandler @ 00a77d50 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  FUN_00752b90();
                    /* try { // try from 00a6e048 to 00b6e057 has its CatchHandler @ 00a77d3c */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330e90.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x16,1,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7580);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7580) = plVar8;
  *(undefined8 *)(param_1 + 0x7578) = uVar5;
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
                    /* try { // try from 00a6ddfc to 00b6de0b has its CatchHandler @ 00a77cbc */
    (**(code **)(*plVar8 + 0x10))(plVar8);
                    /* try { // try from 00a6de0c to 00b6de97 has its CatchHandler @ 00a63e3c */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
                    /* try { // try from 00a6e094 to 00b6e0e7 has its CatchHandler @ 00a77d4c */
  if (((DAT_00ca4b38 & 1) == 0) && (iVar4 = __cxa_guard_acquire(&DAT_00ca4b38), iVar4 != 0)) {
    DAT_00ca4b08 = 0;
    DAT_00ca4b00 = &DAT_00ca4b08;
    DAT_00ca4b28 = 0;
    DAT_00ca4b30 = 0;
    DAT_00ca4b20 = 0;
    DAT_00ca4b10 = 0;
    DAT_00ca4b18 = &DAT_00ca4b20;
    __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
    __cxa_guard_release(&DAT_00ca4b38);
  }
  FUN_0047e89c(&local_80,&DAT_00ca4b00,(long)&fde_table_entry_00330ea8.initial_loc + param_1,
               PTR_DAT_00c9a8a0,0x16,1,0,0);
  plVar8 = plStack_78;
  uVar5 = local_80;
  plVar9 = *(long **)(param_1 + 0x7590);
  local_80 = 0;
  plStack_78 = (long *)0x0;
  *(long **)(param_1 + 0x7590) = plVar8;
  *(undefined8 *)(param_1 + 0x7588) = uVar5;
  if ((plVar9 != (long *)0x0) && (lVar7 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar7 == 0))
  {
    (**(code **)(*plVar9 + 0x10))(plVar9);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
  }
  plVar8 = plStack_78;
                    /* try { // try from 00a6de98 to 00b6dea7 has its CatchHandler @ 00a77ca8 */
  if ((plStack_78 != (long *)0x0) &&
     (lVar7 = FUN_00c538e0(0xffffffffffffffff,plStack_78 + 1), lVar7 == 0)) {
                    /* try { // try from 00a6dea8 to 00b6df2f has its CatchHandler @ 00a63e3c */
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  iVar3 = FUN_0046c984(param_1);
  iVar4 = *(int *)(param_1 + 0xcb48);
  *(undefined4 *)((long)&fde_table_entry_00335f38.data_loc + param_1) = 0xe6;
  *(undefined4 *)((long)&fde_table_entry_00333c88.initial_loc + param_1) = 0x58;
  *(undefined8 *)((long)&fde_table_entry_00333c80.initial_loc + param_1) = DAT_002c3df8;
  *piVar1 = iVar4 * -0xe6;
  *(int *)((long)&fde_table_entry_00333c78.data_loc + param_1) = (int)((double)iVar3 * 0.5 + -255.0)
  ;
  *(undefined4 *)(param_1 + (long)iVar4 * 4 + 0xcb4c) = 1;
  FUN_009cc9e0(param_1);
                    /* try { // try from 00a6df30 to 00b6df3f has its CatchHandler @ 00a77ca8 */
  *(bool *)(param_1 + 0x332a24) = 0x1c < *(int *)(param_1 + 0xcb48);
  iVar4 = FUN_0046c984(param_1);
                    /* try { // try from 00a6df40 to 00b6dfc7 has its CatchHandler @ 00a63e3c */
  *(undefined2 *)((long)&fde_table_entry_00338400.data_loc + param_1) = 0;
  if (iVar4 < 0) {
    iVar4 = iVar4 + 1;
  }
  *(undefined1 *)((long)&fde_table_entry_00338320.initial_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00338328.data_loc + param_1) = 0;
  *(undefined1 *)((long)&fde_table_entry_00338338.initial_loc + param_1) = 0;
  *(int *)((long)&fde_table_entry_00332078.data_loc + param_1) = iVar4 >> 1;
  FUN_00ab27e8(param_1);
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
