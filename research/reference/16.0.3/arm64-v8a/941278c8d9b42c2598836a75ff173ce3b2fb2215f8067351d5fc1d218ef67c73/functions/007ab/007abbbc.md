# 007abbbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007abbbc",
  "name": "FUN_007abbbc",
  "size": 900,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "19d668c379a93b05b8cc13e68240bb4ceaedfa279ec66ad8a48a9dcea4f15b20",
  "source_text_sha256": "19d668c379a93b05b8cc13e68240bb4ceaedfa279ec66ad8a48a9dcea4f15b20"
}
~~~

## 呼び出し元

- [007ab86c](../007ab/007ab86c.md)

## 呼び出し先

- [00598e94](../00598/00598e94.md)
- [00599054](../00599/00599054.md)
- [0059bc68](../0059b/0059bc68.md)
- [00796258](../00796/00796258.md)
- [00796290](../00796/00796290.md)
- [007afbac](../007af/007afbac.md)
- [007afef8](../007af/007afef8.md)
- [007b027c](../007b0/007b027c.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 関連文字列（未確認候補）

~~~text
"¨{"
~~~

## 疑似コード / UTF-8 5415 bytes

~~~c

void FUN_007abbbc(undefined8 param_1,long *param_2,long *param_3)

{
  long lVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 **ppuVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 local_f8;
  long *local_f0;
  undefined8 local_e8;
  long *local_e0;
  undefined1 uStack_d1;
  long local_d0 [4];
  long *local_b0;
  long local_a0 [4];
  long *local_80;
  undefined8 *local_70 [4];
  undefined8 **local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  puVar2 = (undefined8 *)_Znwm(0x38);
  puVar2[6] = 0;
  puVar2[1] = 0;
  *puVar2 = 0;
  puVar2[3] = 0;
  puVar2[2] = 0;
  puVar2[5] = 0;
  puVar2[4] = 0;
  FUN_0059bc68();
  *puVar2 = &PTR_FUN_00c6fd38;
  local_70[0] = puVar2;
  FUN_007afbac(&local_e8,&uStack_d1,local_70);
  puVar2 = local_70[0];
  local_70[0] = (undefined8 *)0x0;
  if (puVar2 != (undefined8 *)0x0) {
    *puVar2 = &PTR_FUN_00c6eac0;
    if ((*(byte *)(puVar2 + 4) & 1) != 0) {
      _ZdlPv((void *)puVar2[6]);
    }
    if ((*(byte *)(puVar2 + 1) & 1) != 0) {
      _ZdlPv((void *)puVar2[3]);
    }
    _ZdlPv(puVar2);
  }
  uVar5 = local_e8;
  plVar3 = (long *)param_2[4];
  local_80 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_2) {
      local_80 = local_a0;
      (**(code **)(*param_2 + 0x18))(param_2,local_a0);
    }
    else {
      local_80 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_50 = (undefined8 **)0x0;
  ppuVar4 = (undefined8 **)_Znwm(0x40);
  *ppuVar4 = &PTR_FUN_00c7b938;
  puVar2 = (undefined8 *)0x0;
  if (local_80 == (long *)0x0) {
LAB_007abcf0:
    ppuVar4[6] = puVar2;
  }
  else {
    if (local_80 != local_a0) {
      puVar2 = (undefined8 *)(**(code **)(*local_80 + 0x10))();
      goto LAB_007abcf0;
    }
    ppuVar4[6] = ppuVar4 + 2;
    (**(code **)(local_a0[0] + 0x18))(local_a0);
  }
  local_50 = ppuVar4;
  FUN_00598e94(uVar5,local_70);
  if (local_50 == local_70) {
    lVar6 = 0x20;
    ppuVar4 = local_70;
LAB_007abd40:
                    /* try { // try from 007abd48 to 008abd5b has its CatchHandler @ 007ac8a4 */
    (**(code **)((long)*ppuVar4 + lVar6))();
  }
  else if (local_50 != (undefined8 **)0x0) {
    lVar6 = 0x28;
    ppuVar4 = local_50;
    goto LAB_007abd40;
  }
  if (local_80 == local_a0) {
    lVar6 = 0x20;
                    /* try { // try from 007abd6c to 008abd77 has its CatchHandler @ 007ac89c */
    plVar3 = local_a0;
LAB_007abd70:
    (**(code **)(*plVar3 + lVar6))();
  }
  else {
                    /* try { // try from 007abd5c to 008abd67 has its CatchHandler @ 007ac8a0 */
    if (local_80 != (long *)0x0) {
      lVar6 = 0x28;
      plVar3 = local_80;
      goto LAB_007abd70;
    }
  }
  uVar5 = local_e8;
  plVar3 = (long *)param_3[4];
  local_b0 = (long *)0x0;
  if (plVar3 != (long *)0x0) {
    if (plVar3 == param_3) {
      local_b0 = local_d0;
      (**(code **)(*param_3 + 0x18))(param_3,local_d0);
    }
    else {
      local_b0 = (long *)(**(code **)(*plVar3 + 0x10))();
    }
  }
  local_50 = (undefined8 **)0x0;
                    /* try { // try from 007abdc4 to 008abdd7 has its CatchHandler @ 007ac8c0 */
  ppuVar4 = (undefined8 **)_Znwm(0x40);
                    /* try { // try from 007abdd8 to 008abde3 has its CatchHandler @ 007ac8bc */
  *ppuVar4 = &PTR_FUN_00c7b9b8;
                    /* try { // try from 007abde4 to 008abdef has its CatchHandler @ 007ac8ac */
  puVar2 = (undefined8 *)0x0;
  if (local_b0 == (long *)0x0) {
LAB_007abe00:
    ppuVar4[6] = puVar2;
  }
  else {
    if (local_b0 != local_d0) {
      puVar2 = (undefined8 *)(**(code **)(*local_b0 + 0x10))();
      goto LAB_007abe00;
    }
    ppuVar4[6] = ppuVar4 + 2;
    (**(code **)(local_d0[0] + 0x18))(local_d0);
  }
  local_50 = ppuVar4;
  FUN_00599054(uVar5,local_70);
  if (local_50 == local_70) {
    lVar6 = 0x20;
    ppuVar4 = local_70;
LAB_007abe50:
                    /* try { // try from 007abe58 to 008abe63 has its CatchHandler @ 007ac8bc */
    (**(code **)((long)*ppuVar4 + lVar6))();
  }
  else if (local_50 != (undefined8 **)0x0) {
    lVar6 = 0x28;
    ppuVar4 = local_50;
                    /* try { // try from 007abe44 to 008abe57 has its CatchHandler @ 007ac8c0 */
    goto LAB_007abe50;
  }
                    /* try { // try from 007abe64 to 008abe6f has its CatchHandler @ 007ac8ac */
  if (local_b0 == local_d0) {
    lVar6 = 0x20;
    plVar3 = local_d0;
  }
  else {
    if (local_b0 == (long *)0x0) goto LAB_007abe8c;
    lVar6 = 0x28;
    plVar3 = local_b0;
  }
  (**(code **)(*plVar3 + lVar6))();
LAB_007abe8c:
  uVar5 = FUN_00796258();
  local_f8 = local_e8;
  local_f0 = local_e0;
  if (local_e0 != (long *)0x0) {
                    /* try { // try from 007abe9c to 008abf2b has its CatchHandler @ 007ac8c8 */
    FUN_00c54d60(1,local_e0 + 1);
  }
  FUN_00796290(uVar5,&local_f8);
  plVar3 = local_f0;
  if ((local_f0 != (long *)0x0) &&
     (lVar6 = FUN_00c54d90(0xffffffffffffffff,local_f0 + 1), lVar6 == 0)) {
    (**(code **)(*plVar3 + 0x10))(plVar3);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
  }
  if ((local_e0 != (long *)0x0) &&
     (lVar6 = FUN_00c54d90(0xffffffffffffffff,local_e0 + 1), lVar6 == 0)) {
    (**(code **)(*local_e0 + 0x10))(local_e0);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_e0);
  }
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
