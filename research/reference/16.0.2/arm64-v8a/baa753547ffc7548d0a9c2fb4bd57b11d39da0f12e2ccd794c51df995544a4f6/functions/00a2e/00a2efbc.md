# 00a2efbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00a2efbc",
  "name": "FUN_00a2efbc",
  "size": 800,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be6d735af67590c0798ff46802c7677a4e8022d588f0299e9b1c2cc265709693",
  "source_text_sha256": "be6d735af67590c0798ff46802c7677a4e8022d588f0299e9b1c2cc265709693"
}
~~~

## 呼び出し元

- [00a26210](../00a26/00a26210.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [0086c30c](../0086c/0086c30c.md)
- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 6515 bytes

~~~c

void FUN_00a2efbc(long *param_1,long *param_2,long *param_3)

{
  int iVar1;
  undefined4 uVar2;
  bool bVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  undefined8 *puVar9;
  long *plVar10;
  
                    /* try { // try from 00a2efd0 to 00b2f137 has its CatchHandler @ 00a2e6c0 */
  if (param_1[2] != 0) {
    puVar5 = (undefined8 *)*param_1;
    plVar10 = param_1 + 1;
    *param_1 = (long)plVar10;
    *(undefined8 *)(*plVar10 + 0x10) = 0;
    param_1[2] = 0;
    *plVar10 = 0;
    puVar4 = (undefined8 *)puVar5[1];
    if (puVar4 != (undefined8 *)0x0) {
      puVar5 = puVar4;
    }
    if (puVar5 == (undefined8 *)0x0) {
      puVar4 = (undefined8 *)0x0;
    }
    else {
      puVar9 = (undefined8 *)puVar5[2];
      if (puVar9 != (undefined8 *)0x0) {
        puVar4 = (undefined8 *)*puVar9;
        if (puVar4 == puVar5) {
          puVar4 = (undefined8 *)puVar9[1];
          *puVar9 = 0;
          while (puVar4 != (undefined8 *)0x0) {
            do {
              puVar9 = puVar4;
              puVar4 = (undefined8 *)*puVar9;
            } while ((undefined8 *)*puVar9 != (undefined8 *)0x0);
            puVar4 = (undefined8 *)puVar9[1];
          }
        }
        else {
          puVar9[1] = 0;
          while (puVar4 != (undefined8 *)0x0) {
            do {
              puVar9 = puVar4;
              puVar4 = (undefined8 *)*puVar9;
            } while ((undefined8 *)*puVar9 != (undefined8 *)0x0);
            puVar4 = (undefined8 *)puVar9[1];
          }
        }
      }
      do {
        puVar4 = puVar9;
        if (param_2 == param_3) break;
        iVar1 = *(int *)((long)param_2 + 0x1c);
        *(int *)((long)puVar5 + 0x1c) = iVar1;
        puVar5[4] = param_2[4];
        plVar8 = (long *)*plVar10;
        plVar6 = plVar10;
        while (plVar7 = plVar6, plVar8 != (long *)0x0) {
          while (plVar6 = plVar8, *(int *)((long)plVar6 + 0x1c) <= iVar1) {
            plVar8 = (long *)plVar6[1];
            if ((long *)plVar6[1] == (long *)0x0) {
              plVar7 = plVar6 + 1;
              goto LAB_00a2f0d8;
            }
          }
          plVar8 = (long *)*plVar6;
        }
LAB_00a2f0d8:
        *puVar5 = 0;
        puVar5[1] = 0;
        puVar5[2] = plVar6;
        *plVar7 = (long)puVar5;
        if (*(long *)*param_1 != 0) {
          *param_1 = *(long *)*param_1;
          puVar5 = (undefined8 *)*plVar7;
        }
        FUN_0043bbe4(param_1[1],puVar5);
        param_1[2] = param_1[2] + 1;
        if (puVar9 == (undefined8 *)0x0) {
          puVar4 = (undefined8 *)0x0;
        }
        else {
          puVar4 = (undefined8 *)puVar9[2];
          if (puVar4 != (undefined8 *)0x0) {
            puVar5 = (undefined8 *)*puVar4;
            if (puVar5 == puVar9) {
              puVar5 = (undefined8 *)puVar4[1];
              *puVar4 = 0;
                    /* try { // try from 00a2f194 to 00b2f2c3 has its CatchHandler @ 00a2e6c0 */
              while (puVar5 != (undefined8 *)0x0) {
                do {
                  puVar4 = puVar5;
                  puVar5 = (undefined8 *)*puVar4;
                } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
                puVar5 = (undefined8 *)puVar4[1];
              }
            }
            else {
              puVar4[1] = 0;
                    /* try { // try from 00a2f170 to 00b2f193 has its CatchHandler @ 00a2fd04 */
              while (puVar5 != (undefined8 *)0x0) {
                do {
                  puVar4 = puVar5;
                  puVar5 = (undefined8 *)*puVar4;
                } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
                puVar5 = (undefined8 *)puVar4[1];
              }
            }
          }
        }
        plVar6 = (long *)param_2[1];
        plVar8 = param_2;
        if ((long *)param_2[1] == (long *)0x0) {
          do {
            param_2 = (long *)plVar8[2];
            bVar3 = (long *)*param_2 != plVar8;
            plVar8 = param_2;
                    /* try { // try from 00a2f138 to 00b2f143 has its CatchHandler @ 00a2fde0 */
          } while (bVar3);
        }
        else {
          do {
            param_2 = plVar6;
            plVar6 = (long *)*param_2;
          } while ((long *)*param_2 != (long *)0x0);
        }
        bVar3 = puVar9 != (undefined8 *)0x0;
        puVar5 = puVar9;
        puVar9 = puVar4;
      } while (bVar3);
      FUN_0086c30c(param_1,puVar5);
      if (puVar4 == (undefined8 *)0x0) goto LAB_00a2f1e0;
      puVar5 = (undefined8 *)puVar4[2];
      while (puVar9 = puVar5, puVar9 != (undefined8 *)0x0) {
        puVar4 = puVar9;
        puVar5 = (undefined8 *)puVar9[2];
      }
    }
    FUN_0086c30c(param_1,puVar4);
  }
LAB_00a2f1e0:
  if (param_2 != param_3) {
    plVar10 = param_1 + 1;
    do {
      puVar5 = (undefined8 *)_Znwm(0x28);
      uVar2 = *(undefined4 *)((long)param_2 + 0x24);
      plVar7 = (long *)*plVar10;
      *(undefined8 *)((long)puVar5 + 0x1c) = *(undefined8 *)((long)param_2 + 0x1c);
      *(undefined4 *)((long)puVar5 + 0x24) = uVar2;
      plVar6 = plVar10;
      plVar8 = plVar10;
      if (plVar7 != (long *)0x0) {
        do {
          while (plVar6 = plVar7, *(int *)((long)plVar6 + 0x1c) <= *(int *)((long)puVar5 + 0x1c)) {
            plVar7 = (long *)plVar6[1];
            if ((long *)plVar6[1] == (long *)0x0) {
              plVar8 = plVar6 + 1;
              goto LAB_00a2f260;
            }
          }
          plVar8 = plVar6;
          plVar7 = (long *)*plVar6;
        } while ((long *)*plVar6 != (long *)0x0);
      }
LAB_00a2f260:
      *puVar5 = 0;
      puVar5[1] = 0;
      puVar5[2] = plVar6;
      *plVar8 = (long)puVar5;
      if (*(long *)*param_1 != 0) {
        *param_1 = *(long *)*param_1;
        puVar5 = (undefined8 *)*plVar8;
      }
      FUN_0043bbe4(param_1[1],puVar5);
      plVar6 = (long *)param_2[1];
      param_1[2] = param_1[2] + 1;
      plVar8 = param_2;
      if (plVar6 == (long *)0x0) {
        do {
          param_2 = (long *)plVar8[2];
          bVar3 = (long *)*param_2 != plVar8;
          plVar8 = param_2;
        } while (bVar3);
      }
      else {
        do {
          param_2 = plVar6;
          plVar6 = (long *)*param_2;
        } while ((long *)*param_2 != (long *)0x0);
      }
    } while (param_2 != param_3);
  }
                    /* try { // try from 00a2f2c4 to 00b2f2cb has its CatchHandler @ 00a2fdd4 */
                    /* try { // try from 00a2f2d0 to 00b2f2e7 has its CatchHandler @ 00a2fcfc */
  return;
}

~~~
