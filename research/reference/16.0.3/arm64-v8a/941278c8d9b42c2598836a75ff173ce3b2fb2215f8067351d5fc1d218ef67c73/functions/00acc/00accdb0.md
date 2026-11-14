# 00accdb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00accdb0",
  "name": "FUN_00accdb0",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a913480e9ec37ca6678394d680ed3ef69d2f88e98a9742ed7b53a230e49c8f1e",
  "source_text_sha256": "a913480e9ec37ca6678394d680ed3ef69d2f88e98a9742ed7b53a230e49c8f1e"
}
~~~

## 呼び出し元

- [009366b0](../00936/009366b0.md)

## 呼び出し先

- [00acd0dc](../00acd/00acd0dc.md)
- [00acd134](../00acd/00acd134.md)
- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 1437 bytes

~~~c

void FUN_00accdb0(long param_1,long *param_2)

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
  *plVar2 = (long)&PTR__ZNSt6__ndk119__shared_weak_countD1Ev_00c8e990;
  plVar4 = plVar2 + 1;
  *plVar4 = 0;
  plVar2[2] = 0;
  plVar2[3] = param_1;
  FUN_00c54d60(1,plVar4);
  plVar5 = *(long **)(lVar6 + 0x38);
  *(long *)(lVar6 + 0x30) = param_1;
  *(long **)(lVar6 + 0x38) = plVar2;
  if ((plVar5 != (long *)0x0) && (lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar5 + 1), lVar6 == 0))
  {
    (**(code **)(*plVar5 + 0x10))(plVar5);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
  }
  lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar4);
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
      FUN_00c54d60(1,lVar6 + 8);
    }
    plVar2 = plVar2 + 2;
  }
  else {
    plVar2 = (long *)FUN_00acd134(param_1 + 0x40,param_2);
  }
  *(long **)(param_1 + 0x48) = plVar2;
  if (*(long *)(lVar1 + 0x28) == lVar3) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
