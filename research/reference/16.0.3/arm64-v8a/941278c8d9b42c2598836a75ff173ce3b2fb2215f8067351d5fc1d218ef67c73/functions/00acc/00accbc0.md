# 00accbc0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00accbc0",
  "name": "FUN_00accbc0",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "63a8f838853dc1f6c67889319d67b91977f9607c2c10f3d6c5f5f5185f415bf6",
  "source_text_sha256": "63a8f838853dc1f6c67889319d67b91977f9607c2c10f3d6c5f5f5185f415bf6"
}
~~~

## 呼び出し元

- [00936b10](../00936/00936b10.md)

## 呼び出し先

- [00c54d60](../00c54/00c54d60.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 1010 bytes

~~~c

void FUN_00accbc0(long param_1,undefined8 param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  long lVar5;
  long lVar6;
  long lVar7;
  
  lVar5 = tpidr_el0;
  lVar7 = *(long *)(lVar5 + 0x28);
  if (*(char *)(param_1 + 0x28) != '\0') {
    puVar3 = *(undefined8 **)(param_1 + 0x48);
    for (puVar1 = *(undefined8 **)(param_1 + 0x40); puVar1 != puVar3; puVar1 = puVar1 + 2) {
      puVar2 = (undefined8 *)*puVar1;
      plVar4 = (long *)puVar1[1];
      if (plVar4 != (long *)0x0) {
        FUN_00c54d60(1,plVar4 + 1);
      }
      (**(code **)*puVar2)(puVar2,param_2);
      if ((plVar4 != (long *)0x0) &&
         (lVar6 = FUN_00c54d90(0xffffffffffffffff,plVar4 + 1), lVar6 == 0)) {
        (**(code **)(*plVar4 + 0x10))(plVar4);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
      }
    }
  }
  if (*(long *)(lVar5 + 0x28) == lVar7) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
