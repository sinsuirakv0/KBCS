# 00abeec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00abeec0.md)

## 関数情報

~~~json
{
  "address": "00abeec0",
  "name": "FUN_00abeec0",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23fc44654b472ac5f31c06ece429d9b0570d4c844596617c4088021215578558",
  "source_text_sha256": "23fc44654b472ac5f31c06ece429d9b0570d4c844596617c4088021215578558"
}
~~~
## 呼び出し元

- [00abe0c4](../00abe/00abe0c4.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 1726 bytes

~~~c

void FUN_00abeec0(undefined8 *param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  void *pvVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  ulong uVar7;
  undefined8 uVar8;
  
  puVar1 = (undefined8 *)param_1[1];
                    /* try { // try from 00abeed8 to 00bbefaf has its CatchHandler @ 00ac52f0 */
  puVar6 = (undefined8 *)*param_1;
  uVar7 = (long)puVar1 - (long)puVar6;
  if (uVar7 < (ulong)(param_1[2] - (long)puVar6)) {
    if (puVar1 == puVar6) {
      puVar2 = (undefined8 *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar7 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
        FUN_0041e380();
      }
      puVar2 = operator_new(uVar7);
      uVar7 = (long)puVar2 + uVar7;
      puVar4 = puVar2;
      puVar5 = puVar6;
      do {
        uVar8 = *puVar5;
        puVar4[1] = puVar5[1];
        *puVar4 = uVar8;
        puVar4[2] = puVar5[2];
        puVar4 = puVar4 + 3;
        *puVar5 = 0;
        puVar5[1] = 0;
        puVar5[2] = 0;
        puVar5 = puVar5 + 3;
      } while (puVar5 != puVar1);
      do {
        pvVar3 = (void *)*puVar6;
        if (pvVar3 != (void *)0x0) {
          puVar6[1] = pvVar3;
          operator_delete(pvVar3);
        }
        puVar6 = puVar6 + 3;
      } while (puVar6 != puVar1);
      puVar6 = (undefined8 *)*param_1;
    }
    *param_1 = puVar2;
    param_1[1] = uVar7;
    param_1[2] = uVar7;
    if (puVar6 != (undefined8 *)0x0) {
      operator_delete(puVar6);
      return;
    }
  }
                    /* try { // try from 00abefcc to 00bbeff7 has its CatchHandler @ 00ac5290 */
  return;
}

~~~
