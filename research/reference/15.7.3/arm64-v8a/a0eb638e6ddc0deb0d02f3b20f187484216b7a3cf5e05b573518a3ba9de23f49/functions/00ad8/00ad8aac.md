# 00ad8aac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00ad8aac",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3471cf2ef7fd42c683aee2cabf448d3139b677c3e981119ae807b68131347c0",
  "source_text_sha256": "d3471cf2ef7fd42c683aee2cabf448d3139b677c3e981119ae807b68131347c0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00574054](../00574/00574054.md)
- [0057473c](../00574/0057473c.md)
- [00bd6e50](../00bd6/00bd6e50.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 2079 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened
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
  if (DAT_0109fea0 != (long *)0x0) {
    FUN_00566a7c(local_88,param_1,param_3);
    thunk_FUN_0056839c(&local_70,local_88);
    plStack_58 = plStack_68;
    local_60 = local_70;
    local_70 = 0;
    plStack_68 = (long *)0x0;
    FUN_00574054(auStack_48,&local_60);
    plVar2 = plStack_58;
    if ((plStack_58 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,plStack_58 + 1), lVar3 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    plVar2 = plStack_68;
    if ((plStack_68 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,plStack_68 + 1), lVar3 == 0)) {
                    /* try { // try from 00ad8bd4 to 00bd8c03 has its CatchHandler @ 00ad8cf8 */
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if (DAT_0109fea0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8c58;
    }
    (**(code **)(*DAT_0109fea0 + 0x30))(DAT_0109fea0,auStack_48);
    if ((local_40 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,local_40 + 1), lVar3 == 0)) {
      (**(code **)(*local_40 + 0x10))(local_40);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_40);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8c58:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
