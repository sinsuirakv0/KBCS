# 00aadadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "e0520f0ed24694dba4947e4de7c44a4919f746e1495f16d974f406c5079e1e7e",
  "source_text_sha256": "e0520f0ed24694dba4947e4de7c44a4919f746e1495f16d974f406c5079e1e7e"
}
~~~

## 呼び出し元

- [00aac290](../00aac/00aac290.md)

## 呼び出し先

- [00471738](../00471/00471738.md)
- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 1251 bytes

~~~c

undefined8 * FUN_00aadadc(undefined8 *param_1,undefined8 *param_2)

{
  bool bVar1;
  void *__ptr;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  puVar5 = param_2;
  puVar2 = (undefined8 *)param_2[1];
  if ((undefined8 *)param_2[1] == (undefined8 *)0x0) {
    do {
      puVar4 = (undefined8 *)puVar5[2];
      bVar1 = (undefined8 *)*puVar4 != puVar5;
      puVar5 = puVar4;
    } while (bVar1);
  }
  else {
    do {
      puVar4 = puVar2;
      puVar2 = (undefined8 *)*puVar4;
    } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
  }
  if ((void *)*param_1 == param_2) {
    *param_1 = puVar4;
  }
  param_1[2] = param_1[2] + -1;
  FUN_00471738(param_1[1],param_2);
  puVar5 = (undefined8 *)param_2[5];
  if (puVar5 != (undefined8 *)0x0) {
    puVar3 = (undefined8 *)param_2[6];
    puVar2 = puVar5;
    if (puVar3 != puVar5) {
      do {
        puVar2 = puVar3 + -3;
        __ptr = (void *)*puVar2;
        if (__ptr != (void *)0x0) {
          puVar3[-2] = __ptr;
          _ZdlPv(__ptr);
        }
        puVar3 = puVar2;
      } while (puVar2 != puVar5);
      puVar2 = (undefined8 *)param_2[5];
    }
    param_2[6] = puVar5;
    _ZdlPv(puVar2);
  }
  _ZdlPv(param_2);
  return puVar4;
}

~~~
