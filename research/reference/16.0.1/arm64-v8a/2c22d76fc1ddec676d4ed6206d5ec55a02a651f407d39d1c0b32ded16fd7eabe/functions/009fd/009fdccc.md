# 009fdccc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009fdccc",
  "name": "FUN_009fdccc",
  "size": 712,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cb0b20f0d4f71347146e8d396449a7a129770a3e5f43dde0f524354350596b4c",
  "source_text_sha256": "cb0b20f0d4f71347146e8d396449a7a129770a3e5f43dde0f524354350596b4c"
}
~~~

## 呼び出し元

- [009f92c8](../009f9/009f92c8.md)
- [009fdccc](../009fd/009fdccc.md)
- [009fdf94](../009fd/009fdf94.md)

## 呼び出し先

- [009fdccc](../009fd/009fdccc.md)
- [009fdf94](../009fd/009fdf94.md)
- [009fe20c](../009fe/009fe20c.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 5052 bytes

~~~c

void FUN_009fdccc(undefined8 *param_1,undefined8 *param_2,ulong param_3,undefined8 *param_4,
                 long param_5)

{
  undefined4 uVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined4 uVar7;
  undefined8 uVar8;
  int iVar9;
  long lVar10;
  ulong uVar11;
  undefined8 *puVar12;
  long lVar13;
  undefined8 *puVar14;
  
  lVar2 = tpidr_el0;
  lVar3 = *(long *)(lVar2 + 0x28);
  if (1 < param_3) {
    if (param_3 == 2) {
      if (*(int *)(param_2 + -1) < *(int *)((long)param_1 + 4)) {
        uVar8 = *param_1;
        uVar7 = *(undefined4 *)((long)param_2 + -4);
        *param_1 = *(undefined8 *)((long)param_2 + -0xc);
        uVar1 = *(undefined4 *)(param_1 + 1);
        *(undefined4 *)(param_1 + 1) = uVar7;
        *(undefined8 *)((long)param_2 + -0xc) = uVar8;
        *(undefined4 *)((long)param_2 + -4) = uVar1;
      }
    }
    else if ((long)param_3 < 0x81) {
      if ((param_1 != param_2) && ((undefined8 *)((long)param_1 + 0xc) != param_2)) {
        lVar4 = 0;
        puVar6 = (undefined8 *)((long)param_1 + 0xc);
        puVar5 = param_1;
        do {
          puVar12 = puVar6;
          uVar8 = *puVar12;
          iVar9 = (int)((ulong)uVar8 >> 0x20);
          if (iVar9 < *(int *)((long)puVar5 + 4)) {
            uVar7 = *(undefined4 *)((long)puVar5 + 0x14);
            lVar13 = lVar4;
            do {
              lVar10 = lVar13;
              puVar6 = (undefined8 *)((long)param_1 + lVar10);
              *(undefined8 *)((long)puVar6 + 0xc) = *puVar6;
              *(undefined4 *)((long)puVar6 + 0x14) = *(undefined4 *)(puVar6 + 1);
              puVar5 = param_1;
              if (lVar10 == 0) goto LAB_009fdd98;
              lVar13 = lVar10 + -0xc;
            } while (iVar9 < *(int *)(puVar6 + -1));
            puVar5 = (undefined8 *)((long)param_1 + lVar10);
LAB_009fdd98:
            *puVar5 = uVar8;
            *(undefined4 *)(puVar5 + 1) = uVar7;
          }
          lVar4 = lVar4 + 0xc;
          puVar6 = (undefined8 *)((long)puVar12 + 0xc);
          puVar5 = puVar12;
        } while ((undefined8 *)((long)puVar12 + 0xc) != param_2);
      }
    }
    else {
      uVar11 = param_3 >> 1;
      lVar4 = (long)param_1 + uVar11 * 0xc;
      lVar13 = param_3 - uVar11;
      if (param_5 < (long)param_3) {
        FUN_009fdccc(param_1,lVar4,uVar11);
        FUN_009fdccc(lVar4,param_2,lVar13,param_4,param_5);
        if (*(long *)(lVar2 + 0x28) == lVar3) {
          FUN_009fe20c(param_1,lVar4,param_2,uVar11,lVar13,param_4,param_5);
          return;
        }
        goto LAB_009fdf90;
      }
                    /* try { // try from 009fdeac to 00afdebb has its CatchHandler @ 009fe4e4 */
      FUN_009fdf94(param_1,lVar4,uVar11);
      puVar12 = (undefined8 *)((long)param_4 + uVar11 * 0xc);
      FUN_009fdf94(lVar4,param_2,lVar13,puVar12);
                    /* try { // try from 009fded4 to 00afdedf has its CatchHandler @ 009fe3e0 */
      puVar5 = (undefined8 *)((long)param_4 + param_3 * 0xc);
      puVar6 = puVar12;
      do {
                    /* try { // try from 009fdf00 to 00afdf07 has its CatchHandler @ 009fe3bc */
        if (puVar6 == puVar5) {
          if (param_4 != puVar12) {
            lVar4 = 0;
            do {
              puVar6 = (undefined8 *)((long)param_4 + lVar4);
              puVar5 = (undefined8 *)((long)param_1 + lVar4);
              lVar4 = lVar4 + 0xc;
              uVar8 = *puVar6;
              *(undefined4 *)(puVar5 + 1) = *(undefined4 *)(puVar6 + 1);
              *puVar5 = uVar8;
            } while ((undefined8 *)((long)param_4 + lVar4) != puVar12);
          }
          goto LAB_009fdd00;
        }
                    /* try { // try from 009fdf08 to 00afdfab has its CatchHandler @ 009fd500 */
        if (*(int *)((long)puVar6 + 4) < *(int *)((long)param_4 + 4)) {
          uVar7 = *(undefined4 *)(puVar6 + 1);
          uVar8 = *puVar6;
          puVar6 = (undefined8 *)((long)puVar6 + 0xc);
          puVar14 = param_4;
        }
        else {
          uVar7 = *(undefined4 *)(param_4 + 1);
          puVar14 = (undefined8 *)((long)param_4 + 0xc);
          uVar8 = *param_4;
        }
        *(undefined4 *)(param_1 + 1) = uVar7;
        *param_1 = uVar8;
                    /* try { // try from 009fdef0 to 00afdefb has its CatchHandler @ 009fe3cc */
        param_1 = (undefined8 *)((long)param_1 + 0xc);
        param_4 = puVar14;
      } while (puVar14 != puVar12);
      if (puVar6 != puVar5) {
        lVar4 = 0;
        do {
          puVar12 = (undefined8 *)((long)puVar6 + lVar4);
          puVar14 = (undefined8 *)((long)param_1 + lVar4);
          lVar4 = lVar4 + 0xc;
          uVar8 = *puVar12;
          *(undefined4 *)(puVar14 + 1) = *(undefined4 *)(puVar12 + 1);
          *puVar14 = uVar8;
        } while ((undefined8 *)((long)puVar6 + lVar4) != puVar5);
      }
    }
  }
LAB_009fdd00:
  if (*(long *)(lVar2 + 0x28) == lVar3) {
    return;
  }
LAB_009fdf90:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
