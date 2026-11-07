# 00ad8dcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00ad8ed8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8ed8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00ad8dcc",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdClosed",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df2c72a698f12fc132547e945a99e341eadf5b2cfa1d3015cb98b903609bfb30",
  "source_text_sha256": "df2c72a698f12fc132547e945a99e341eadf5b2cfa1d3015cb98b903609bfb30"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00574054](../00574/00574054.md)
- [0057473c](../00574/0057473c.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 2273 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdClosed
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  byte local_88 [16];
  void *local_78;
  undefined8 local_70;
  long *plStack_68;
  undefined8 local_60;
  long *plStack_58;
  undefined1 auStack_48 [8];
  long *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fe10 != (long *)0x0) {
    FUN_00566a7c(local_88,param_1,param_3);
    thunk_FUN_0056839c(&local_70,local_88);
    plStack_58 = plStack_68;
    local_60 = local_70;
    local_70 = 0;
    plStack_68 = (long *)0x0;
    FUN_00574054(auStack_48,&local_60);
    plVar2 = plStack_58;
    if ((plStack_58 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,plStack_58 + 1), lVar3 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    plVar2 = plStack_68;
    if ((plStack_68 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,plStack_68 + 1), lVar3 == 0)) {
                    /* try { // try from 00ad8ef4 to 00bd8f37 has its CatchHandler @ 00ad8fb0 */
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if (DAT_0109fe10 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8f78;
    }
                    /* try { // try from 00ad8e90 to 00bd8ebf has its CatchHandler @ 00ad8fb4 */
    (**(code **)(*DAT_0109fe10 + 0x30))(DAT_0109fe10,auStack_48);
    if ((local_40 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,local_40 + 1), lVar3 == 0)) {
      (**(code **)(*local_40 + 0x10))(local_40);
                    /* try { // try from 00ad8ec0 to 00bd8ef3 has its CatchHandler @ 00ad8d28 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_40);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8f78:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
