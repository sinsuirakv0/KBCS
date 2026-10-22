# 00aaca8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aaca8c.md)

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
  "source_sha256": "e30646737289ffcb8f235662f5214634b2513df83c2ba04158fc4a76f92c4026",
  "source_text_sha256": "e30646737289ffcb8f235662f5214634b2513df83c2ba04158fc4a76f92c4026"
}
~~~
## 呼び出し元

- [00aaaedc](../00aaa/00aaaedc.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00aaca64](../00aac/00aaca64.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 2365 bytes

~~~c

undefined8 * FUN_00aaca8c(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  
  lVar4 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar4 * -0x5555555555555555 + 1;
  if (0xaaaaaaaaaaaaaaa < uVar1) {
    FUN_00aaca64(param_1);
LAB_00aacc14:
                    /* WARNING: Subroutine does not return */
    FUN_0041e380();
  }
  lVar8 = param_1[2] - *param_1 >> 3;
  uVar10 = lVar8 * 0x5555555555555556;
  if (uVar10 < uVar1 || uVar10 - uVar1 == 0) {
    uVar10 = uVar1;
  }
  if (0x555555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
    uVar10 = 0xaaaaaaaaaaaaaaa;
  }
  if (uVar10 == 0) {
    pvVar2 = (void *)0x0;
  }
  else {
    if (0xaaaaaaaaaaaaaaa < uVar10) goto LAB_00aacc14;
    pvVar2 = operator_new(uVar10 * 0x18);
  }
  uVar14 = param_2[1];
  uVar13 = *param_2;
  *param_2 = 0;
  param_2[1] = 0;
  puVar6 = (undefined8 *)((long)pvVar2 + lVar4 * 8);
  uVar9 = param_2[2];
  param_2[2] = 0;
  puVar12 = (undefined8 *)*param_1;
  puVar11 = (undefined8 *)param_1[1];
  lVar8 = (long)puVar11 - (long)puVar12;
  puVar6[1] = uVar14;
  *puVar6 = uVar13;
  puVar6[2] = uVar9;
  if ((long)puVar11 - (long)puVar12 != 0) {
    puVar5 = (undefined8 *)
             ((long)pvVar2 + lVar4 * 8 + ((long)puVar11 - (long)puVar12 >> 3) * -8 + 0x10);
    puVar7 = puVar12;
    do {
      *puVar5 = 0;
      uVar9 = *puVar7;
      puVar5[-1] = puVar7[1];
      puVar5[-2] = uVar9;
      *puVar5 = puVar7[2];
      *puVar7 = 0;
      puVar7[1] = 0;
      puVar7[2] = 0;
      puVar7 = puVar7 + 3;
      puVar5 = puVar5 + 3;
    } while (puVar7 != puVar11);
    do {
      pvVar3 = (void *)*puVar12;
      if (pvVar3 != (void *)0x0) {
        puVar12[1] = pvVar3;
        operator_delete(pvVar3);
      }
      puVar12 = puVar12 + 3;
    } while (puVar12 != puVar11);
    puVar11 = (undefined8 *)*param_1;
  }
  *param_1 = (long)puVar6 - lVar8;
  param_1[1] = (long)(puVar6 + 3);
  param_1[2] = (long)((long)pvVar2 + uVar10 * 0x18);
  if (puVar11 != (undefined8 *)0x0) {
    operator_delete(puVar11);
  }
  return puVar6 + 3;
}

~~~
