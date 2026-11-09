# 009bcbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009bcbbc",
  "name": "FUN_009bcbbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3",
  "source_text_sha256": "e4bb5a9451b5b72c2b72a279309ccca3f833c3f59d5befce0641d8e08568ffe3"
}
~~~

## 呼び出し元

- [009bd99c](../009bd/009bd99c.md)
- [009bdae4](../009bd/009bdae4.md)

## 呼び出し先

- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)

## 疑似コード / UTF-8 1708 bytes

~~~c

void FUN_009bcbbc(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[1];
                    /* try { // try from 009bcbd0 to 00abcccb has its CatchHandler @ 009bc884 */
  *param_1 = 0;
  param_1[1] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[3];
  param_1[2] = 0;
  param_1[3] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[5];
  param_1[4] = 0;
  param_1[5] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[7];
  param_1[6] = 0;
  param_1[7] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[9];
  param_1[8] = 0;
  param_1[9] = 0;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c538e0(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
                    /* try { // try from 009bcccc to 00abcce3 has its CatchHandler @ 009bda34 */
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    return;
  }
  return;
}

~~~
