# 00aadadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aadadc.md)

## 関数情報

~~~json
{
  "address": "00aadadc",
  "name": "FUN_00aadadc",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55e3c5a4ffd96455772a127e961d2cd1032df82cc75bb0639a9241ae2b331cdc",
  "source_text_sha256": "55e3c5a4ffd96455772a127e961d2cd1032df82cc75bb0639a9241ae2b331cdc"
}
~~~
## 呼び出し元

- [00aac290](../00aac/00aac290.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 1337 bytes

~~~c

undefined8 * FUN_00aadadc(undefined8 *param_1,undefined8 *param_2)

{
  bool bVar1;
  void *pvVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  
  puVar6 = param_2;
  puVar3 = (undefined8 *)param_2[1];
  if ((undefined8 *)param_2[1] == (undefined8 *)0x0) {
    do {
      puVar5 = (undefined8 *)puVar6[2];
      bVar1 = (undefined8 *)*puVar5 != puVar6;
      puVar6 = puVar5;
    } while (bVar1);
  }
  else {
    do {
      puVar5 = puVar3;
      puVar3 = (undefined8 *)*puVar5;
    } while ((undefined8 *)*puVar5 != (undefined8 *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = puVar5;
  }
  param_1[2] = param_1[2] + -1;
  FUN_00471738(param_1[1],param_2);
  puVar6 = (undefined8 *)param_2[5];
  if (puVar6 != (undefined8 *)0x0) {
    puVar4 = (undefined8 *)param_2[6];
    puVar3 = puVar6;
    if (puVar4 != puVar6) {
      do {
        puVar3 = puVar4 + -3;
        pvVar2 = (void *)*puVar3;
        if (pvVar2 != (void *)0x0) {
          puVar4[-2] = pvVar2;
          operator_delete(pvVar2);
        }
        puVar4 = puVar3;
      } while (puVar3 != puVar6);
      puVar3 = (undefined8 *)param_2[5];
    }
    param_2[6] = puVar6;
    operator_delete(puVar3);
  }
  operator_delete(param_2);
  return puVar5;
}

~~~
