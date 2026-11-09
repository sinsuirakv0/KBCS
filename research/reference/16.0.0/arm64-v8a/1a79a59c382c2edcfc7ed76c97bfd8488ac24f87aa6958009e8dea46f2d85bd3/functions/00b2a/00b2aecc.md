# 00b2aecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b2aecc",
  "name": "FUN_00b2aecc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc897cb049238b99bc42715bfe810d78a09f3c7a7621ac26a2a9d5027542af4a",
  "source_text_sha256": "fc897cb049238b99bc42715bfe810d78a09f3c7a7621ac26a2a9d5027542af4a"
}
~~~

## 呼び出し元

- [00b2ac48](../00b2a/00b2ac48.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 1681 bytes

~~~c

void FUN_00b2aecc(undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  void *__ptr;
  undefined8 *puVar4;
  undefined8 uVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  
  puVar6 = (undefined8 *)*param_1;
  puVar2 = (undefined8 *)param_1[1];
  puVar1 = (undefined8 *)((long)puVar6 + (param_2[1] - (long)puVar2));
  puVar3 = puVar1;
  puVar7 = puVar6;
  if (puVar2 != puVar6) {
    do {
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = 0;
      uVar5 = *puVar7;
      puVar3[1] = puVar7[1];
      *puVar3 = uVar5;
      puVar3[2] = puVar7[2];
      *puVar7 = 0;
      puVar7[1] = 0;
      puVar7[2] = 0;
      puVar7 = puVar7 + 3;
      puVar3 = puVar3 + 3;
    } while (puVar7 != puVar2);
    do {
      puVar7 = (undefined8 *)*puVar6;
      if (puVar7 != (undefined8 *)0x0) {
        puVar4 = (undefined8 *)puVar6[1];
        puVar3 = puVar7;
        if (puVar4 != puVar7) {
          do {
            puVar3 = puVar4 + -3;
            __ptr = (void *)*puVar3;
            if (__ptr != (void *)0x0) {
              puVar4[-2] = __ptr;
              _ZdlPv(__ptr);
            }
            puVar4 = puVar3;
          } while (puVar3 != puVar7);
          puVar3 = (undefined8 *)*puVar6;
        }
        puVar6[1] = puVar7;
        _ZdlPv(puVar3);
      }
      puVar6 = puVar6 + 3;
    } while (puVar6 != puVar2);
  }
  param_2[1] = puVar1;
  uVar5 = *param_1;
  *param_1 = puVar1;
  param_1[1] = uVar5;
  param_2[1] = uVar5;
  uVar5 = param_1[1];
  param_1[1] = param_2[2];
  param_2[2] = uVar5;
  uVar5 = param_1[2];
  param_1[2] = param_2[3];
  param_2[3] = uVar5;
  *param_2 = param_2[1];
  return;
}

~~~
