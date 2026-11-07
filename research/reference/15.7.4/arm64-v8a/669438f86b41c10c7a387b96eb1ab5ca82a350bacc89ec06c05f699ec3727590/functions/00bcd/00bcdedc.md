# 00bcdedc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bcddd0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcddd0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bcdedc",
  "name": "FUN_00bcdedc",
  "size": 848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d83a6f8459b23917cf3412cbd2396f933e0c9ccf10c735314896dc757d8ff22",
  "source_text_sha256": "9d83a6f8459b23917cf3412cbd2396f933e0c9ccf10c735314896dc757d8ff22"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc82d4](../00bc8/00bc82d4.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 6096 bytes

~~~c

void FUN_00bcdedc(long param_1,undefined8 *param_2)

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
                    /* try { // try from 00bcdf40 to 00ccdf5b has its CatchHandler @ 00bce588 */
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
                    /* try { // try from 00bcdfc8 to 00ccdfe3 has its CatchHandler @ 00bce584 */
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
    FUN_00bc82d4(param_1 + 0x10,param_2);
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
                    /* try { // try from 00bce050 to 00cce06b has its CatchHandler @ 00bce580 */
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
                    /* try { // try from 00bce0c8 to 00cce0e3 has its CatchHandler @ 00bce598 */
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
                    /* try { // try from 00bce140 to 00cce15b has its CatchHandler @ 00bce594 */
      if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
        (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      }
      lVar2 = lVar2 + -8;
      puVar8 = puVar8 + 1;
    } while (lVar2 != 0);
  }
                    /* try { // try from 00bce15c to 00cce237 has its CatchHandler @ 00bcde00 */
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
