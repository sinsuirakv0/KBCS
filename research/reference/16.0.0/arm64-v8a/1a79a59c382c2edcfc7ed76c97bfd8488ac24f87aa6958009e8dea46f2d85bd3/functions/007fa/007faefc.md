# 007faefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007faefc",
  "name": "FUN_007faefc",
  "size": 428,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a3cc31cadc09f8e917d942f1e6c39f44e63b5b2a51cedb72907b910ae2446ef",
  "source_text_sha256": "1a3cc31cadc09f8e917d942f1e6c39f44e63b5b2a51cedb72907b910ae2446ef"
}
~~~

## 呼び出し元

- [007fa950](../007fa/007fa950.md)
- [007fbdc8](../007fb/007fbdc8.md)

## 呼び出し先

- [0047e89c](../0047e/0047e89c.md)
- [00664860](../00664/00664860.md)
- [00744158](../00744/00744158.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 2011 bytes

~~~c

void FUN_007faefc(long *param_1)

{
  undefined4 uVar1;
  long lVar2;
  undefined8 uVar3;
  long *plVar4;
  int iVar5;
  ulong uVar6;
  ulong uVar7;
  long *plVar8;
  long lVar9;
  byte local_68 [16];
  void *local_58;
  undefined8 local_50;
  long *plStack_48;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  lVar9 = *param_1;
  uVar6 = FUN_00744158(lVar9 + 0xbe0,*(undefined4 *)(lVar9 + 0xa24));
  uVar1 = *(undefined4 *)(lVar9 + (long)(int)uVar6 * 4 + 0x49934);
  uVar7 = uVar6;
  if ((DAT_00ca4b38 & 1) == 0) {
    iVar5 = __cxa_guard_acquire(&DAT_00ca4b38);
    uVar7 = uVar6 & 0xffffffff;
    if (iVar5 != 0) {
      DAT_00ca4b08 = 0;
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
      __cxa_guard_release(&DAT_00ca4b38);
      uVar7 = uVar6 & 0xffffffff;
    }
  }
  FUN_00664860(local_68,uVar7,uVar1);
  FUN_0047e89c(&local_50,&DAT_00ca4b00,local_68,PTR_DAT_00c9a8a0,0x1e,1,0,0);
  plVar4 = plStack_48;
  uVar3 = local_50;
  lVar9 = param_1[1];
  local_50 = 0;
  plStack_48 = (long *)0x0;
  plVar8 = *(long **)(lVar9 + 0xca0);
  *(long **)(lVar9 + 0xca0) = plVar4;
  *(undefined8 *)(lVar9 + 0xc98) = uVar3;
  if ((plVar8 != (long *)0x0) && (lVar9 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar9 == 0))
  {
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  plVar4 = plStack_48;
  if ((plStack_48 != (long *)0x0) &&
     (lVar9 = FUN_00c538e0(0xffffffffffffffff,plStack_48 + 1), lVar9 == 0)) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
