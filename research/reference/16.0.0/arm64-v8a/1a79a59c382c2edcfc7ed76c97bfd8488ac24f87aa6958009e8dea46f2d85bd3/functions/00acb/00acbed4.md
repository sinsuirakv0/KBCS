# 00acbed4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbed4",
  "name": "FUN_00acbed4",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45f1e31d99ba938d0b238e954c54b7ebe208c1324b0cea9fc0afb2066453b34e",
  "source_text_sha256": "45f1e31d99ba938d0b238e954c54b7ebe208c1324b0cea9fc0afb2066453b34e"
}
~~~

## 呼び出し元

- [00acbb50](../00acb/00acbb50.md)

## 呼び出し先

- [00440e80](../00440/00440e80.md)
- [00acc030](../00acc/00acc030.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 2122 bytes

~~~c

undefined8 * FUN_00acbed4(long *param_1,undefined8 *param_2)

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
    FUN_00acc030(param_1);
LAB_00acc02c:
                    /* WARNING: Subroutine does not return */
    FUN_00440e80();
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
    if (uVar8 >> 0x3c != 0) goto LAB_00acc02c;
    lVar3 = _Znwm(uVar8 << 4);
  }
  lVar4 = param_2[1];
  uVar12 = *param_2;
  puVar2 = (undefined8 *)(lVar3 + lVar11 * 0x10);
  puVar2[1] = lVar4;
  *puVar2 = uVar12;
  if (lVar4 != 0) {
    FUN_00c538b0(1,lVar4 + 8);
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
         (lVar4 = FUN_00c538e0(0xffffffffffffffff,plVar9 + 1), lVar4 == 0)) {
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
