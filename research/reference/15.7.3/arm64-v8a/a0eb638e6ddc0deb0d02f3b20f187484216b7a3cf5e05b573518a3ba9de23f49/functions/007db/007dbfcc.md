# 007dbfcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "007dbfcc",
  "name": "FUN_007dbfcc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "91b7774a1b1b884a42551e58eafbe65bdf49e46052cce7df4ba56f0beb6eefb4",
  "source_text_sha256": "91b7774a1b1b884a42551e58eafbe65bdf49e46052cce7df4ba56f0beb6eefb4"
}
~~~

## 呼び出し元

- [007db2f0](../007db/007db2f0.md)

## 呼び出し先

- [007bfcc8](../007bf/007bfcc8.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb160](../00bdb/00bdb160.md)

## 疑似コード / UTF-8 4217 bytes

~~~c

void FUN_007dbfcc(undefined8 *param_1,void *param_2,long param_3,ulong param_4)

{
  void *__src;
  ulong uVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  void *pvVar4;
  long lVar5;
  size_t sVar6;
  ulong uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  void *pvVar10;
  undefined1 auVar11 [16];
  
  uVar7 = param_1[2];
  pvVar10 = (void *)*param_1;
  if (param_4 <= (ulong)((long)(uVar7 - (long)pvVar10) >> 4)) {
    sVar6 = (long)param_1[1] - (long)pvVar10;
    pvVar4 = param_2;
    if (((ulong)((long)sVar6 >> 4) < param_4) &&
       (pvVar4 = (void *)((long)param_2 + sVar6), (void *)param_1[1] != pvVar10)) {
                    /* try { // try from 007dc0a8 to 008dc0af has its CatchHandler @ 007dd318 */
      memmove(pvVar10,param_2,sVar6);
      pvVar10 = (void *)param_1[1];
    }
    sVar6 = param_3 - (long)pvVar4;
    if (sVar6 != 0) {
      memmove(pvVar10,pvVar4,sVar6);
    }
LAB_007dc0d8:
                    /* try { // try from 007dc0dc to 008dc0e3 has its CatchHandler @ 007dd5a0 */
    param_1[1] = (long)pvVar10 + sVar6;
    return;
  }
  lVar5 = param_3;
  if (pvVar10 != (void *)0x0) {
    param_1[1] = pvVar10;
    _ZdlPv(pvVar10);
    uVar7 = 0;
    *param_1 = 0;
    param_1[1] = 0;
    param_1[2] = 0;
  }
  if (param_4 >> 0x3c == 0) {
    uVar1 = (long)uVar7 >> 3;
    if ((ulong)((long)uVar7 >> 3) <= param_4) {
      uVar1 = param_4;
    }
                    /* try { // try from 007dc03c to 008dc047 has its CatchHandler @ 007dd388 */
    if (0x7fffffffffffffef < uVar7) {
      uVar1 = 0xfffffffffffffff;
    }
    if (uVar1 >> 0x3c == 0) {
      pvVar10 = (void *)_Znwm(uVar1 * 0x10);
      sVar6 = param_3 - (long)param_2;
                    /* try { // try from 007dc068 to 008dc083 has its CatchHandler @ 007dd350 */
      *param_1 = pvVar10;
      param_1[1] = pvVar10;
      param_1[2] = (void *)((long)pvVar10 + uVar1 * 0x10);
      if (sVar6 != 0) {
        memcpy(pvVar10,param_2,sVar6);
      }
      goto LAB_007dc0d8;
    }
  }
                    /* try { // try from 007dc0f8 to 008dc0ff has its CatchHandler @ 007dd59c */
  auVar11 = FUN_007bfcc8(param_1);
  pvVar4 = auVar11._8_8_;
  puVar2 = auVar11._0_8_;
  uVar7 = puVar2[2];
  pvVar10 = (void *)*puVar2;
  if ((ulong)((long)(uVar7 - (long)pvVar10) >> 3) < param_4) {
    if (pvVar10 != (void *)0x0) {
      puVar2[1] = pvVar10;
      _ZdlPv(pvVar10);
      uVar7 = 0;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = 0;
    }
    if (param_4 >> 0x3d == 0) {
      uVar1 = (long)uVar7 >> 2;
      if ((ulong)((long)uVar7 >> 2) <= param_4) {
        uVar1 = param_4;
      }
      if (0x7ffffffffffffff7 < uVar7) {
        uVar1 = 0x1fffffffffffffff;
      }
      if (uVar1 >> 0x3d == 0) {
        pvVar10 = (void *)_Znwm(uVar1 * 8);
        sVar6 = lVar5 - (long)pvVar4;
        *puVar2 = pvVar10;
        puVar2[1] = pvVar10;
        puVar2[2] = (void *)((long)pvVar10 + uVar1 * 8);
        if (sVar6 != 0) {
          memcpy(pvVar10,pvVar4,sVar6);
        }
        goto LAB_007dc208;
      }
    }
    auVar11 = FUN_007bfcdc(puVar2);
    puVar2 = auVar11._8_8_;
    if (puVar2 == (undefined8 *)0x0) {
      return;
    }
    FUN_007dc22c(auVar11._0_8_,*puVar2);
    FUN_007dc22c(auVar11._0_8_,puVar2[1]);
    puVar9 = (undefined8 *)puVar2[5];
    if (puVar9 != (undefined8 *)0x0) {
      puVar8 = (undefined8 *)puVar2[6];
      puVar3 = puVar9;
      if (puVar8 != puVar9) {
        do {
          puVar3 = puVar8 + -5;
          pvVar10 = (void *)*puVar3;
          if (pvVar10 != (void *)0x0) {
            puVar8[-4] = pvVar10;
            _ZdlPv(pvVar10);
          }
          puVar8 = puVar3;
        } while (puVar3 != puVar9);
        puVar3 = (undefined8 *)puVar2[5];
      }
      puVar2[6] = puVar9;
      _ZdlPv(puVar3);
    }
    _ZdlPv(puVar2);
    return;
  }
  sVar6 = (long)puVar2[1] - (long)pvVar10;
  __src = pvVar4;
  if (((ulong)((long)sVar6 >> 3) < param_4) &&
     (__src = (void *)((long)pvVar4 + sVar6), (void *)puVar2[1] != pvVar10)) {
    memmove(pvVar10,pvVar4,sVar6);
    pvVar10 = (void *)puVar2[1];
  }
  sVar6 = lVar5 - (long)__src;
  if (sVar6 != 0) {
    memmove(pvVar10,__src,sVar6);
  }
LAB_007dc208:
  puVar2[1] = (long)pvVar10 + sVar6;
  return;
}

~~~
