# 00a0aaec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00a0aaa8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a0a/00a0aaa8.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00a0aaec",
  "name": "FUN_00a0aaec",
  "size": 564,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "318774da2d4363d542683adb9f287c8a7e1b225d93e1c2009fd99976799ca391",
  "source_text_sha256": "318774da2d4363d542683adb9f287c8a7e1b225d93e1c2009fd99976799ca391"
}
~~~

## 呼び出し元

- [00a0b228](../00a0b/00a0b228.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0045d518](../0045d/0045d518.md)
- [0059d170](../0059d/0059d170.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 4160 bytes

~~~c

void FUN_00a0aaec(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  long *plVar9;
  int iVar10;
  int iVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  undefined8 *puVar14;
  
  puVar12 = (undefined8 *)(param_1 + 4);
  FUN_0059d170(param_1 + 2,*puVar12);
  *(undefined8 **)(param_1 + 2) = puVar12;
  *(undefined8 *)(param_1 + 6) = 0;
  *puVar12 = 0;
  uVar1 = FUN_0045d518(param_2);
  *param_1 = uVar1;
  iVar2 = FUN_0045d518(param_2);
  if (0 < iVar2) {
    iVar10 = 0;
    do {
      iVar3 = FUN_0045d518(param_2);
      iVar4 = FUN_0045d518(param_2);
      if (iVar4 != 0) {
        iVar11 = 0;
        do {
                    /* try { // try from 00a0abcc to 00b0abd3 has its CatchHandler @ 00a0d628 */
          iVar5 = FUN_0045d518(param_2);
          uVar1 = FUN_0045d518(param_2);
          puVar8 = (undefined8 *)*puVar12;
          puVar13 = puVar12;
          puVar14 = puVar12;
          if ((undefined8 *)*puVar12 != (undefined8 *)0x0) {
            do {
                    /* try { // try from 00a0ac00 to 00b0ac07 has its CatchHandler @ 00a0d5f0 */
              while (puVar6 = puVar8, puVar14 = puVar6, iVar3 < *(int *)(puVar6 + 4)) {
                puVar8 = (undefined8 *)*puVar6;
                puVar13 = puVar6;
                if ((undefined8 *)*puVar6 == (undefined8 *)0x0) goto LAB_00a0ac24;
              }
              if (iVar3 <= *(int *)(puVar6 + 4)) goto LAB_00a0ac80;
              puVar8 = (undefined8 *)puVar6[1];
            } while ((undefined8 *)puVar6[1] != (undefined8 *)0x0);
            puVar13 = puVar6 + 1;
          }
LAB_00a0ac24:
                    /* try { // try from 00a0ac24 to 00b0ac2b has its CatchHandler @ 00a0d604 */
          puVar6 = (undefined8 *)_Znwm(0x40);
          puVar6[7] = 0;
          puVar6[6] = 0;
          puVar6[5] = puVar6 + 6;
          *puVar6 = 0;
          puVar6[1] = 0;
          puVar6[2] = puVar14;
          *puVar13 = puVar6;
          plVar9 = *(long **)(param_1 + 2);
          *(int *)(puVar6 + 4) = iVar3;
          puVar8 = puVar6;
          if (*plVar9 != 0) {
            *(long *)(param_1 + 2) = *plVar9;
            puVar8 = (undefined8 *)*puVar13;
          }
          FUN_00419064(*(undefined8 *)(param_1 + 4),puVar8);
          *(long *)(param_1 + 6) = *(long *)(param_1 + 6) + 1;
LAB_00a0ac80:
          puVar13 = puVar6 + 6;
          puVar8 = (undefined8 *)*puVar13;
          puVar14 = puVar13;
          if ((undefined8 *)*puVar13 != (undefined8 *)0x0) {
            do {
              while (puVar7 = puVar8, puVar14 = puVar7, iVar5 < *(int *)((long)puVar7 + 0x1c)) {
                puVar8 = (undefined8 *)*puVar7;
                puVar13 = puVar7;
                if ((undefined8 *)*puVar7 == (undefined8 *)0x0) goto LAB_00a0acc4;
              }
              if (iVar5 <= *(int *)((long)puVar7 + 0x1c)) goto LAB_00a0abb0;
              puVar8 = (undefined8 *)puVar7[1];
            } while ((undefined8 *)puVar7[1] != (undefined8 *)0x0);
            puVar13 = puVar7 + 1;
          }
LAB_00a0acc4:
          puVar7 = (undefined8 *)_Znwm(0x28);
          *puVar7 = 0;
          puVar7[1] = 0;
                    /* try { // try from 00a0acdc to 00b0ace3 has its CatchHandler @ 00a0d5b0 */
          puVar7[2] = puVar14;
          *puVar13 = puVar7;
          plVar9 = (long *)puVar6[5];
          *(int *)((long)puVar7 + 0x1c) = iVar5;
          *(undefined4 *)(puVar7 + 4) = 0;
          puVar8 = puVar7;
          if (*plVar9 != 0) {
            puVar6[5] = *plVar9;
            puVar8 = (undefined8 *)*puVar13;
          }
                    /* try { // try from 00a0aba0 to 00b0aba7 has its CatchHandler @ 00a0d5f8 */
          FUN_00419064(puVar6[6],puVar8);
          puVar6[7] = puVar6[7] + 1;
LAB_00a0abb0:
          iVar11 = iVar11 + 1;
          *(undefined4 *)(puVar7 + 4) = uVar1;
        } while (iVar11 != iVar4);
      }
      iVar10 = iVar10 + 1;
    } while (iVar10 != iVar2);
  }
                    /* try { // try from 00a0ad08 to 00b0ad0f has its CatchHandler @ 00a0d5dc */
  return;
}

~~~
