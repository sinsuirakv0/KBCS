# 00accaec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00accaec",
  "name": "FUN_00accaec",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca5480be226db2febdfed61ef3320dd9fc85aff8bc70144bf6964548685bdf32",
  "source_text_sha256": "ca5480be226db2febdfed61ef3320dd9fc85aff8bc70144bf6964548685bdf32"
}
~~~

## 呼び出し元

- [00732374](../00732/00732374.md)
- [007323d0](../00732/007323d0.md)
- [00936950](../00936/00936950.md)
- [009369dc](../00936/009369dc.md)
- [00acd07c](../00acd/00acd07c.md)
- [00acd0dc](../00acd/00acd0dc.md)

## 呼び出し先

- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 1049 bytes

~~~c

void FUN_00accaec(undefined8 *param_1)

{
  void *__ptr;
  long lVar1;
  long *plVar2;
  void *pvVar3;
  void *pvVar4;
  
  pvVar3 = (void *)param_1[8];
  *param_1 = &PTR_FUN_00c8e960;
  if (pvVar3 != (void *)0x0) {
    pvVar4 = (void *)param_1[9];
    __ptr = pvVar3;
    if (pvVar4 != pvVar3) {
      do {
        plVar2 = *(long **)((long)pvVar4 + -8);
        if ((plVar2 != (long *)0x0) &&
           (lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1), lVar1 == 0)) {
          (**(code **)(*plVar2 + 0x10))(plVar2);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
        }
        pvVar4 = (void *)((long)pvVar4 + -0x10);
      } while (pvVar4 != pvVar3);
      __ptr = (void *)param_1[8];
    }
    param_1[9] = pvVar3;
    _ZdlPv(__ptr);
  }
  plVar2 = (long *)param_1[7];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c54d90(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~
