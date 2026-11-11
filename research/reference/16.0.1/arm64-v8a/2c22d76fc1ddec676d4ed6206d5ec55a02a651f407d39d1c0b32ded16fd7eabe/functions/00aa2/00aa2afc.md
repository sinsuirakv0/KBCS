# 00aa2afc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aa2afc",
  "name": "FUN_00aa2afc",
  "size": 500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca950bf56df8f3f30f01aa64a817e2c7634f94799edb6fc9b3693cf81ea171ee",
  "source_text_sha256": "ca950bf56df8f3f30f01aa64a817e2c7634f94799edb6fc9b3693cf81ea171ee"
}
~~~

## 呼び出し元

- [00a261bc](../00a26/00a261bc.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [00480118](../00480/00480118.md)
- [00480178](../00480/00480178.md)
- [004801d8](../00480/004801d8.md)
- [0086be6c](../0086b/0086be6c.md)
- [00c57e90](../00c57/00c57e90.md)

## 疑似コード / UTF-8 3100 bytes

~~~c

void FUN_00aa2afc(long param_1,undefined8 param_2)

{
  char cVar1;
  short sVar2;
  int iVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long *plVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  int iVar10;
  undefined8 *puVar11;
  
  puVar9 = (undefined8 *)(param_1 + 0x20);
  plVar7 = (long *)(param_1 + 0x18);
  FUN_0086be6c(plVar7,*puVar9);
  *puVar9 = 0;
  *(undefined8 *)(param_1 + 0x28) = 0;
  *(undefined8 **)(param_1 + 0x18) = puVar9;
  sVar2 = FUN_00480178(param_2);
  if (0 < sVar2) {
    iVar10 = 0;
    do {
      iVar3 = FUN_004801d8(param_2);
      cVar1 = FUN_00480118(param_2);
      puVar5 = (undefined8 *)*puVar9;
      puVar8 = puVar9;
      puVar11 = puVar9;
      if ((undefined8 *)*puVar9 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar8 = puVar4, iVar3 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar11 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aa2be8;
          }
          if (iVar3 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00aa2c38;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar11 = puVar4 + 1;
      }
LAB_00aa2be8:
      puVar4 = (undefined8 *)_Znwm(0x28);
      puVar4[4] = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar8;
      *puVar11 = puVar4;
      plVar6 = (long *)*plVar7;
      *(int *)((long)puVar4 + 0x1c) = iVar3;
      puVar5 = puVar4;
      if (*plVar6 != 0) {
        *plVar7 = *plVar6;
        puVar5 = (undefined8 *)*puVar11;
      }
      FUN_0043bba4(*(undefined8 *)(param_1 + 0x20),puVar5);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aa2c38:
      *(int *)(puVar4 + 4) = (int)cVar1;
      cVar1 = FUN_00480118(param_2);
      puVar5 = (undefined8 *)*puVar9;
      puVar8 = puVar9;
      puVar11 = puVar9;
      if ((undefined8 *)*puVar9 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar8 = puVar4, iVar3 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar11 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00aa2c90;
          }
          if (iVar3 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00aa2b74;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar11 = puVar4 + 1;
      }
LAB_00aa2c90:
      puVar4 = (undefined8 *)_Znwm(0x28);
      puVar4[4] = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar8;
      *puVar11 = puVar4;
      plVar6 = (long *)*plVar7;
      *(int *)((long)puVar4 + 0x1c) = iVar3;
      puVar5 = puVar4;
      if (*plVar6 != 0) {
        *plVar7 = *plVar6;
        puVar5 = (undefined8 *)*puVar11;
      }
      FUN_0043bba4(*(undefined8 *)(param_1 + 0x20),puVar5);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aa2b74:
      iVar10 = iVar10 + 1;
      *(int *)((long)puVar4 + 0x24) = (int)cVar1;
    } while (iVar10 != sVar2);
  }
  return;
}

~~~
