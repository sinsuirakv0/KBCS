# 00aaca8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00aacb98`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacb98.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00aaca8c",
  "name": "FUN_00aaca8c",
  "size": 396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "af12fae4c51b0e25cab138ca6f378406fbcf92c3d7a9e956e07998974aa3c916",
  "source_text_sha256": "af12fae4c51b0e25cab138ca6f378406fbcf92c3d7a9e956e07998974aa3c916"
}
~~~

## 呼び出し元

- [00aaaedc](../00aaa/00aaaedc.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aaca64](../00aac/00aaca64.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 2188 bytes

~~~c

undefined8 * FUN_00aaca8c(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  long lVar2;
  void *__ptr;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 uVar8;
  ulong uVar9;
  undefined8 *__ptr_00;
  undefined8 *puVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  
  lVar3 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar3 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
    FUN_00aaca64(param_1);
LAB_00aacc14:
                    /* WARNING: Subroutine does not return */
    FUN_0041e380();
  }
  lVar7 = param_1[2] - *param_1 >> 3;
  uVar9 = lVar7 * 0x5555555555555556;
  if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
    uVar9 = uVar1;
  }
  if (0x555555555555554 < (ulong)(lVar7 * -0x5555555555555555)) {
    uVar9 = 0xaaaaaaaaaaaaaaa;
  }
  if (uVar9 == 0) {
    lVar7 = 0;
  }
  else {
    if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00aacc14;
    lVar7 = _Znwm(uVar9 * 0x18);
  }
  uVar12 = param_2[1];
  uVar11 = *param_2;
  *param_2 = 0;
  param_2[1] = 0;
  puVar5 = (undefined8 *)(lVar7 + lVar3 * 8);
  uVar8 = param_2[2];
  param_2[2] = 0;
  puVar10 = (undefined8 *)*param_1;
  __ptr_00 = (undefined8 *)param_1[1];
  lVar2 = (long)__ptr_00 - (long)puVar10;
  puVar5[1] = uVar12;
  *puVar5 = uVar11;
  puVar5[2] = uVar8;
  if ((long)__ptr_00 - (long)puVar10 != 0) {
    puVar4 = (undefined8 *)(lVar3 * 8 + ((long)__ptr_00 - (long)puVar10 >> 3) * -8 + lVar7 + 0x10);
    puVar6 = puVar10;
    do {
      *puVar4 = 0;
      uVar8 = *puVar6;
      puVar4[-1] = puVar6[1];
      puVar4[-2] = uVar8;
      *puVar4 = puVar6[2];
      *puVar6 = 0;
      puVar6[1] = 0;
      puVar6[2] = 0;
      puVar6 = puVar6 + 3;
      puVar4 = puVar4 + 3;
    } while (puVar6 != __ptr_00);
    do {
      __ptr = (void *)*puVar10;
      if (__ptr != (void *)0x0) {
        puVar10[1] = __ptr;
        _ZdlPv(__ptr);
      }
      puVar10 = puVar10 + 3;
    } while (puVar10 != __ptr_00);
    __ptr_00 = (undefined8 *)*param_1;
  }
  *param_1 = (long)puVar5 - lVar2;
  param_1[1] = (long)(puVar5 + 3);
  param_1[2] = lVar7 + uVar9 * 0x18;
  if (__ptr_00 != (undefined8 *)0x0) {
    _ZdlPv(__ptr_00);
  }
  return puVar5 + 3;
}

~~~
