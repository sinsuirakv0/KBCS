# 00acbdbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acbdbc",
  "name": "FUN_00acbdbc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b39654d81be393e24180ac8826fa75989ef1ce3c74852f53e70bdf7452fe60d9",
  "source_text_sha256": "b39654d81be393e24180ac8826fa75989ef1ce3c74852f53e70bdf7452fe60d9"
}
~~~

## 呼び出し元

- [00935704](../00935/00935704.md)

## 呼び出し先

- [00acc0e8](../00acc/00acc0e8.md)
- [00acc140](../00acc/00acc140.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00acbdbc(long param_1,long *param_2)

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
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD1Ev_00c8d9c0;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00c53d70(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar4);
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
      FUN_00c53d70(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00acc140(param_1 + 0x40,param_2);
  }
  *(long **)(param_1 + 0x48) = plVar2;
  if (*(long *)(lVar1 + 0x28) == lVar3) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
