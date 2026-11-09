# 00ac2ddc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ac2ddc",
  "name": "FUN_00ac2ddc",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ecc5b57878b541972287c66d541f168f265a326858b894ee75fdf8a30c235723",
  "source_text_sha256": "ecc5b57878b541972287c66d541f168f265a326858b894ee75fdf8a30c235723"
}
~~~

## 呼び出し元

- [00ac2f54](../00ac2/00ac2f54.md)

## 呼び出し先

- [006822e4](../00682/006822e4.md)
- [0078dc6c](../0078d/0078dc6c.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)

## 疑似コード / UTF-8 1903 bytes

~~~c

void FUN_00ac2ddc(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[0x8d];
  *param_1 = &PTR_FUN_00c8d020;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
                    /* try { // try from 00ac2e24 to 00bc2e73 has its CatchHandler @ 00ac3114 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x8b];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x89];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x87];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x85];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  FUN_0078dc6c(param_1 + 0x7a);
  FUN_0078dc6c(param_1 + 0x70);
  FUN_0078dc6c(param_1 + 0x66);
  FUN_0078dc6c(param_1 + 0x5c);
  plVar2 = (long *)param_1[0x5b];
  *param_1 = &PTR_FUN_00c74410;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  FUN_006822e4(param_1);
  return;
}

~~~
