# 00c4bddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00c4bddc",
  "name": "FUN_00c4bddc",
  "size": 848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0a3edf36b0a9f72d1ebd9a73cfe212c5f7495b727e7a2434b2e119c8ae99119",
  "source_text_sha256": "e0a3edf36b0a9f72d1ebd9a73cfe212c5f7495b727e7a2434b2e119c8ae99119"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c461d4](../00c46/00c461d4.md)
- [00c5b140](../00c5b/00c5b140.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

## 疑似コード / UTF-8 5514 bytes

~~~c

void FUN_00c4bddc(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  long lVar3;
  ulong uVar4;
  size_t sVar5;
  long lVar6;
  long *plVar7;
  undefined8 *puVar8;
  
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 8U) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 1000;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined8 *)((long)pvVar1 + lVar2) = 0x7365726975716572;
  lVar3 = param_2[1];
  lVar6 = *(long *)(param_1 + 0x18);
  lVar2 = lVar3 + 8;
  param_2[1] = lVar2;
  if (lVar6 != 0) {
    uVar4 = lVar3 + 9;
    pvVar1 = (void *)*param_2;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar3 + 0x3e9;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
    FUN_00c461d4(param_1 + 0x10,param_2);
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
    lVar2 = param_2[1];
  }
  uVar4 = lVar2 + 1;
  pvVar1 = (void *)*param_2;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x7b;
  if (*(long *)(param_1 + 0x28) != 0) {
    puVar8 = *(undefined8 **)(param_1 + 0x20);
    lVar2 = *(long *)(param_1 + 0x28) << 3;
    do {
      plVar7 = (long *)*puVar8;
      (**(code **)(*plVar7 + 0x20))(plVar7,param_2);
      if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
        (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      }
      lVar2 = lVar2 + -8;
      puVar8 = puVar8 + 1;
    } while (lVar2 != 0);
  }
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x7d;
  return;
}

~~~
