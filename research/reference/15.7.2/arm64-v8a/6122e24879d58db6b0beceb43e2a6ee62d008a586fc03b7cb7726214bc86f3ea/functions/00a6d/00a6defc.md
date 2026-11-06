# 00a6defc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00a6defc",
  "name": "FUN_00a6defc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f58d058e4443fcb979bfda0854a09ff0afaf8516ce198c9b391ecbdcb15e480",
  "source_text_sha256": "6f58d058e4443fcb979bfda0854a09ff0afaf8516ce198c9b391ecbdcb15e480"
}
~~~

## 呼び出し元

- [00a6db78](../00a6d/00a6db78.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00a6e058](../00a6e/00a6e058.md)
- [00bd6d60](../00bd6/00bd6d60.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 2209 bytes

~~~c

undefined8 * FUN_00a6defc(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 *puVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  ulong uVar8;
  undefined8 *__ptr;
  long *plVar9;
  undefined8 *puVar10;
  long lVar11;
  undefined8 uVar12;
  
  __ptr = (undefined8 *)*param_1;
  puVar10 = (undefined8 *)param_1[1];
  lVar11 = (long)puVar10 - (long)__ptr >> 4;
  uVar1 = lVar11 + 1;
  if (uVar1 >> 0x3c != 0) {
    FUN_00a6e058(param_1);
LAB_00a6e054:
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00a6e230 with catch @ 00a6e054 */
    FUN_0041e380();
  }
  uVar8 = param_1[2] - (long)__ptr >> 3;
  if (uVar8 <= uVar1) {
    uVar8 = uVar1;
  }
  if (0x7fffffffffffffef < (ulong)(param_1[2] - (long)__ptr)) {
    uVar8 = 0xfffffffffffffff;
  }
  if (uVar8 == 0) {
    lVar3 = 0;
  }
  else {
    if (uVar8 >> 0x3c != 0) goto LAB_00a6e054;
    lVar3 = _Znwm(uVar8 << 4);
  }
  lVar4 = param_2[1];
  uVar12 = *param_2;
  puVar2 = (undefined8 *)(lVar3 + lVar11 * 0x10);
  puVar2[1] = lVar4;
  *puVar2 = uVar12;
  if (lVar4 != 0) {
    FUN_00bd6d60(1,lVar4 + 8);
    __ptr = (undefined8 *)*param_1;
    puVar10 = (undefined8 *)param_1[1];
    lVar11 = (long)puVar10 - (long)__ptr >> 4;
  }
  puVar5 = puVar2 + lVar11 * -2;
  puVar6 = __ptr;
  if (__ptr != puVar10) {
    do {
      uVar12 = *puVar6;
      puVar5[1] = puVar6[1];
      *puVar5 = uVar12;
      puVar7 = puVar6 + 2;
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar5 = puVar5 + 2;
      puVar6 = puVar7;
    } while (puVar7 != puVar10);
    do {
      plVar9 = (long *)__ptr[1];
      if ((plVar9 != (long *)0x0) &&
         (lVar4 = FUN_00bd6d90(0xffffffffffffffff,plVar9 + 1), lVar4 == 0)) {
        (**(code **)(*plVar9 + 0x10))(plVar9);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
      }
      __ptr = __ptr + 2;
    } while (__ptr != puVar10);
    __ptr = (undefined8 *)*param_1;
  }
  *param_1 = (long)(puVar2 + lVar11 * -2);
  param_1[1] = (long)(puVar2 + 2);
  param_1[2] = lVar3 + uVar8 * 0x10;
  if (__ptr != (undefined8 *)0x0) {
    _ZdlPv(__ptr);
  }
  return puVar2 + 2;
}

~~~
