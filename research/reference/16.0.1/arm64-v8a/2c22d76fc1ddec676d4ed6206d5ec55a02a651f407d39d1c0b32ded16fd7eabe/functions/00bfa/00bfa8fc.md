# 00bfa8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfa8fc",
  "name": "FUN_00bfa8fc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39a4b5f099564c1a5a53906ce3ce6ff39142f4b259d2a93e06fd36c28708cf0b",
  "source_text_sha256": "39a4b5f099564c1a5a53906ce3ce6ff39142f4b259d2a93e06fd36c28708cf0b"
}
~~~

## 呼び出し元

- [00bfabf0](../00bfa/00bfabf0.md)

## 呼び出し先

- [00c53d00](../00c53/00c53d00.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c580f0](../00c58/00c580f0.md)
- [00c58380](../00c58/00c58380.md)
- [00c5e250](../00c5e/00c5e250.md)

## 疑似コード / UTF-8 950 bytes

~~~c

void FUN_00bfa8fc(undefined8 *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  long *plVar4;
  undefined8 *puVar5;
  
  puVar1 = (undefined8 *)param_1[4];
  for (puVar5 = (undefined8 *)param_1[3]; puVar5 != puVar1; puVar5 = puVar5 + 2) {
    _ZNSt6__ndk118condition_variable10notify_allEv(*puVar5);
    _ZNSt6__ndk15mutex6unlockEv(puVar5[1]);
  }
  puVar1 = (undefined8 *)param_1[1];
  for (puVar5 = (undefined8 *)*param_1; puVar5 != puVar1; puVar5 = puVar5 + 1) {
    _ZNSt6__ndk117__assoc_sub_state12__make_readyEv(*puVar5);
    plVar4 = (long *)*puVar5;
    lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1);
    if (lVar2 == 0) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
    }
  }
  pvVar3 = (void *)param_1[3];
  if (pvVar3 != (void *)0x0) {
    param_1[4] = pvVar3;
    _ZdlPv(pvVar3);
  }
  pvVar3 = (void *)*param_1;
  if (pvVar3 == (void *)0x0) {
    return;
  }
  param_1[1] = pvVar3;
  _ZdlPv(pvVar3);
  return;
}

~~~
