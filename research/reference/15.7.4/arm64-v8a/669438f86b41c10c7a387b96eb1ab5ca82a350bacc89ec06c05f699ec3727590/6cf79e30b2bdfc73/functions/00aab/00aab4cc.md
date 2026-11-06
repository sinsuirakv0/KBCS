# 00aab4cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aab4cc.md)

## 関数情報

~~~json
{
  "address": "00aab4cc",
  "name": "FUN_00aab4cc",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f74a065afa1414dee1142f80120cb7d9034f1aa46d7a2af01268fe3cdc66c26",
  "source_text_sha256": "9f74a065afa1414dee1142f80120cb7d9034f1aa46d7a2af01268fe3cdc66c26"
}
~~~
## 呼び出し元

- [005d996c](../005d9/005d996c.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007acf88](../007ac/007acf88.md)
- [00a7268c](../00a72/00a7268c.md)
- [00a788d0](../00a78/00a788d0.md)
- [00aabe48](../00aab/00aabe48.md)
- [00aad9e4](../00aad/00aad9e4.md)
- [00aadb20](../00aad/00aadb20.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード 1/1 / UTF-8 1824 bytes

~~~c

int FUN_00aab4cc(long param_1,int param_2,int param_3,int param_4)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  long *plVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
    puVar2 = *(undefined8 **)(param_1 + 0x20);
  }
  else {
    puVar2 = *(undefined8 **)(param_1 + 0x20);
  }
  if (puVar2 != (undefined8 *)0x0) {
    param_4 = param_2 * 1000 + param_3 * 10 + param_4;
    puVar4 = puVar2;
    do {
      if (*(int *)(puVar4 + 4) <= param_4) {
        if (param_4 <= *(int *)(puVar4 + 4)) goto LAB_00aab56c;
        puVar4 = puVar4 + 1;
      }
      puVar4 = (undefined8 *)*puVar4;
    } while (puVar4 != (undefined8 *)0x0);
  }
  return 0;
LAB_00aab56c:
  puVar4 = puVar2;
  if (param_4 < *(int *)(puVar4 + 4)) {
    puVar2 = (undefined8 *)*puVar4;
    puVar5 = puVar4;
    if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aab5a0;
    goto LAB_00aab56c;
  }
  if (param_4 <= *(int *)(puVar4 + 4)) goto LAB_00aab5f8;
  puVar2 = (undefined8 *)puVar4[1];
  if ((undefined8 *)puVar4[1] == (undefined8 *)0x0) {
    puVar5 = puVar4 + 1;
LAB_00aab5a0:
    puVar1 = (undefined8 *)_Znwm(0x40);
    puVar1[6] = 0;
    puVar1[7] = 0;
    puVar1[5] = 0;
    *puVar1 = 0;
    puVar1[1] = 0;
    puVar1[2] = puVar4;
    *puVar5 = puVar1;
    plVar3 = *(long **)(param_1 + 0x18);
    *(int *)(puVar1 + 4) = param_4;
    puVar2 = puVar1;
    if (*plVar3 != 0) {
      *(long *)(param_1 + 0x18) = *plVar3;
      puVar2 = (undefined8 *)*puVar5;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar2);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
    puVar4 = puVar1;
LAB_00aab5f8:
    return (int)((ulong)(puVar4[6] - puVar4[5]) >> 3) * -0x55555555;
  }
  goto LAB_00aab56c;
}

~~~
