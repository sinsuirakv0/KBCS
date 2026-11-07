# 00a6dbbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00a6db78`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6db78.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00a6dbbc",
  "name": "FUN_00a6dbbc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88d366e54be122f0f7f08cc0105f0285e511d6d6f41c24ca43bda97500aee09e",
  "source_text_sha256": "88d366e54be122f0f7f08cc0105f0285e511d6d6f41c24ca43bda97500aee09e"
}
~~~

## 呼び出し元

- [00900ae0](../00900/00900ae0.md)

## 呼び出し先

- [00a6dee8](../00a6d/00a6dee8.md)
- [00a6df40](../00a6d/00a6df40.md)
- [00bd6e60](../00bd6/00bd6e60.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00a6dbbc(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long lVar6;
  
  lVar1 = tpidr_el0;
  lVar3 = *(long *)(lVar1 + 0x28);
  lVar6 = *param_2;
  plVar2 = (long *)_Znwm(0x20);
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD2Ev_00c0ded0;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00bd6e60(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00bd6e90(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00bd6e90(0xffffffffffffffff,plVar4);
  if (lVar6 == 0) {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = *(long **)(param_1 + 0x48);
  if (plVar2 < *(long **)(param_1 + 0x50)) {
    lVar6 = param_2[1];
    *plVar2 = *param_2;
    plVar2[1] = lVar6;
    if (lVar6 != 0) {
      FUN_00bd6e60(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00a6df40(param_1 + 0x40,param_2);
  }
  *(long **)(param_1 + 0x48) = plVar2;
  if (*(long *)(lVar1 + 0x28) == lVar3) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
