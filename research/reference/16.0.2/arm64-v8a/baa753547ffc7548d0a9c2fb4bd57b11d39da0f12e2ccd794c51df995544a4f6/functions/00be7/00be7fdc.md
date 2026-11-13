# 00be7fdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00be7fdc",
  "name": "FUN_00be7fdc",
  "size": 1784,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64de1a167d806e3bf2b1467068996b7c43fa886fff0e3fa74eb67ae8beb5ffa0",
  "source_text_sha256": "64de1a167d806e3bf2b1467068996b7c43fa886fff0e3fa74eb67ae8beb5ffa0"
}
~~~

## 呼び出し元

- [00be7fbc](../00be7/00be7fbc.md)
- [00be7fdc](../00be7/00be7fdc.md)

## 呼び出し先

- [00be7fdc](../00be7/00be7fdc.md)
- [00bee91c](../00bee/00bee91c.md)
- [00beebbc](../00bee/00beebbc.md)
- [00beece4](../00bee/00beece4.md)

## 疑似コード / UTF-8 11350 bytes

~~~c

void FUN_00be7fdc(double *param_1,double *param_2,undefined1 param_3,long param_4,ulong param_5)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  double *pdVar4;
  long lVar5;
  double *pdVar6;
  double *pdVar7;
  double *pdVar8;
  long lVar9;
  double *pdVar10;
  double *pdVar11;
  double dVar12;
  double dVar13;
  double dVar14;
  double dVar15;
  double dVar16;
  undefined1 local_34 [4];
  
  param_5 = param_5 & 0xffffffff;
  local_34[0] = param_3;
LAB_00be8010:
  do {
    pdVar6 = param_1;
    uVar3 = (long)param_2 - (long)pdVar6 >> 3;
    if ((long)uVar3 < 3) {
      if (uVar3 < 2) {
        return;
      }
      if (uVar3 == 2) {
        dVar14 = *pdVar6;
        if (param_2[-1] < dVar14) {
          *pdVar6 = param_2[-1];
          param_2[-1] = dVar14;
          return;
        }
        return;
      }
    }
    else {
      if (uVar3 == 3) {
        dVar14 = *pdVar6;
        dVar13 = pdVar6[1];
        dVar15 = param_2[-1];
        if (dVar13 < dVar14) {
          if (dVar13 <= dVar15) {
            *pdVar6 = dVar13;
            pdVar6[1] = dVar14;
            if (dVar14 <= param_2[-1]) {
              return;
            }
            pdVar6[1] = param_2[-1];
          }
          else {
            *pdVar6 = dVar15;
          }
          param_2[-1] = dVar14;
          return;
        }
        if (dVar15 < dVar13) {
          pdVar6[1] = dVar15;
          param_2[-1] = dVar13;
          dVar14 = *pdVar6;
          if (pdVar6[1] < dVar14) {
            *pdVar6 = pdVar6[1];
            pdVar6[1] = dVar14;
            return;
          }
          return;
        }
        return;
      }
      if (uVar3 == 4) {
        dVar13 = *pdVar6;
        pdVar8 = pdVar6 + 1;
        dVar14 = *pdVar8;
        pdVar7 = pdVar6 + 2;
        dVar15 = *pdVar7;
        pdVar4 = pdVar6;
        if (dVar13 <= dVar14) {
          dVar12 = dVar15;
                    /* try { // try from 00be85ec to 00ce85f7 has its CatchHandler @ 00bea2f8 */
          if (dVar14 <= dVar15) goto LAB_00be8664;
          *pdVar8 = dVar15;
          *pdVar7 = dVar14;
          pdVar10 = pdVar8;
          dVar16 = dVar14;
joined_r0x00be8608:
          dVar12 = dVar14;
          if (dVar13 <= dVar15) goto LAB_00be8664;
        }
        else {
          pdVar10 = pdVar7;
          dVar16 = dVar13;
          if (dVar14 <= dVar15) {
            *pdVar6 = dVar14;
            pdVar6[1] = dVar13;
            dVar14 = dVar15;
            pdVar4 = pdVar8;
            goto joined_r0x00be8608;
          }
        }
        *pdVar4 = dVar15;
        *pdVar10 = dVar13;
        dVar12 = dVar16;
LAB_00be8664:
        if (dVar12 <= param_2[-1]) {
          return;
        }
        *pdVar7 = param_2[-1];
        param_2[-1] = dVar12;
        dVar14 = *pdVar7;
        dVar13 = *pdVar8;
        if (dVar14 < dVar13) {
          dVar15 = *pdVar6;
          pdVar6[1] = dVar14;
          pdVar6[2] = dVar13;
          if (dVar14 < dVar15) {
            *pdVar6 = dVar14;
            pdVar6[1] = dVar15;
            return;
          }
          return;
        }
        return;
      }
      if (uVar3 == 5) {
                    /* try { // try from 00be849c to 00ce84bf has its CatchHandler @ 00bea2fc */
        FUN_00beebbc(pdVar6,pdVar6 + 1,pdVar6 + 2,pdVar6 + 3,param_2 + -1);
        return;
      }
    }
    if ((long)uVar3 < 0x18) {
      pdVar4 = pdVar6 + 1;
      if ((param_5 & 1) == 0) {
        if (pdVar6 != param_2 && pdVar4 != param_2) {
          do {
            pdVar8 = pdVar4;
            dVar13 = *pdVar6;
            dVar14 = pdVar6[1];
            pdVar6 = pdVar8;
                    /* try { // try from 00be863c to 00ce86cb has its CatchHandler @ 00bea3ac */
            if (dVar14 < dVar13) {
              do {
                *pdVar6 = dVar13;
                dVar13 = pdVar6[-2];
                pdVar6 = pdVar6 + -1;
              } while (dVar14 < dVar13);
              *pdVar6 = dVar14;
            }
            pdVar4 = pdVar8 + 1;
            pdVar6 = pdVar8;
          } while (pdVar8 + 1 != param_2);
          return;
        }
        return;
      }
      if (pdVar6 == param_2 || pdVar4 == param_2) {
        return;
      }
      lVar5 = 0;
      pdVar8 = pdVar6;
      do {
        pdVar7 = pdVar4;
        dVar13 = *pdVar8;
        dVar14 = pdVar8[1];
        lVar1 = lVar5;
        if (dVar14 < dVar13) {
          do {
            lVar9 = lVar1;
            *(double *)((long)pdVar6 + lVar9 + 8) = dVar13;
            pdVar4 = pdVar6;
            if (lVar9 == 0) goto LAB_00be8554;
            dVar13 = *(double *)((long)pdVar6 + lVar9 + -8);
            lVar1 = lVar9 + -8;
          } while (dVar14 < dVar13);
          pdVar4 = (double *)((long)pdVar6 + lVar9);
LAB_00be8554:
          *pdVar4 = dVar14;
        }
        pdVar4 = pdVar7 + 1;
        lVar5 = lVar5 + 8;
        pdVar8 = pdVar7;
        if (pdVar4 == param_2) {
          return;
        }
      } while( true );
    }
    if (param_4 == 0) {
      if (pdVar6 != param_2) {
        FUN_00beece4(pdVar6,param_2,param_2,local_34);
        return;
      }
      return;
    }
    dVar14 = param_2[-1];
    pdVar4 = pdVar6 + (uVar3 >> 1);
    if (uVar3 < 0x81) {
      dVar15 = *pdVar6;
      dVar13 = *pdVar4;
      if (dVar13 <= dVar15) {
        if (dVar14 < dVar15) {
          *pdVar6 = dVar14;
          param_2[-1] = dVar15;
          dVar14 = *pdVar4;
          if (*pdVar6 < dVar14) {
            *pdVar4 = *pdVar6;
            *pdVar6 = dVar14;
          }
        }
      }
      else {
        if (dVar15 <= dVar14) {
          *pdVar4 = dVar15;
          *pdVar6 = dVar13;
          if (dVar13 <= param_2[-1]) goto LAB_00be8290;
          *pdVar6 = param_2[-1];
        }
        else {
          *pdVar4 = dVar14;
        }
        param_2[-1] = dVar13;
      }
    }
    else {
      dVar15 = *pdVar4;
      dVar13 = *pdVar6;
      if (dVar13 <= dVar15) {
        if (dVar14 < dVar15) {
          *pdVar4 = dVar14;
          param_2[-1] = dVar15;
          dVar14 = *pdVar6;
          if (*pdVar4 < dVar14) {
            *pdVar6 = *pdVar4;
            *pdVar4 = dVar14;
          }
        }
      }
      else {
        if (dVar15 <= dVar14) {
          *pdVar6 = dVar15;
          *pdVar4 = dVar13;
          if (dVar13 <= param_2[-1]) goto LAB_00be8124;
          *pdVar4 = param_2[-1];
        }
        else {
          *pdVar6 = dVar14;
        }
        param_2[-1] = dVar13;
      }
LAB_00be8124:
      dVar14 = pdVar6[1];
      dVar15 = param_2[-2];
      pdVar8 = pdVar4 + -1;
      dVar13 = *pdVar8;
      if (dVar14 <= dVar13) {
        if (dVar15 < dVar13) {
          *pdVar8 = dVar15;
          param_2[-2] = dVar13;
          dVar14 = pdVar6[1];
          if (*pdVar8 < dVar14) {
            pdVar6[1] = *pdVar8;
            *pdVar8 = dVar14;
          }
        }
      }
      else {
        if (dVar13 <= dVar15) {
          pdVar6[1] = dVar13;
          *pdVar8 = dVar14;
          if (dVar14 <= param_2[-2]) goto LAB_00be81b4;
          *pdVar8 = param_2[-2];
        }
        else {
          pdVar6[1] = dVar15;
        }
        param_2[-2] = dVar14;
      }
LAB_00be81b4:
      pdVar7 = pdVar4 + 1;
      dVar13 = *pdVar7;
      dVar14 = pdVar6[2];
      dVar15 = param_2[-3];
      if (dVar14 <= dVar13) {
        if (dVar15 < dVar13) {
          *pdVar7 = dVar15;
          param_2[-3] = dVar13;
          dVar14 = pdVar6[2];
          if (*pdVar7 < dVar14) {
            pdVar6[2] = *pdVar7;
            *pdVar7 = dVar14;
          }
        }
      }
      else {
        if (dVar13 <= dVar15) {
          pdVar6[2] = dVar13;
          *pdVar7 = dVar14;
          if (dVar14 <= param_2[-3]) goto LAB_00be8220;
          *pdVar7 = param_2[-3];
        }
        else {
          pdVar6[2] = dVar15;
        }
        param_2[-3] = dVar14;
      }
LAB_00be8220:
      dVar14 = *pdVar4;
      dVar13 = *pdVar8;
      dVar15 = *pdVar7;
      if (dVar13 <= dVar14) {
        if (dVar15 < dVar14) {
          *pdVar7 = dVar14;
          *pdVar4 = dVar15;
          pdVar7 = pdVar4;
          dVar14 = dVar15;
          dVar12 = dVar13;
          if (dVar15 < dVar13) goto LAB_00be827c;
        }
      }
      else {
        dVar12 = dVar14;
        if (dVar14 <= dVar15) {
          *pdVar8 = dVar14;
          *pdVar4 = dVar13;
          pdVar8 = pdVar4;
          dVar14 = dVar13;
          dVar12 = dVar15;
          if (dVar13 <= dVar15) goto LAB_00be8284;
        }
LAB_00be827c:
        *pdVar8 = dVar15;
        *pdVar7 = dVar13;
        dVar14 = dVar12;
      }
LAB_00be8284:
      dVar13 = *pdVar6;
      *pdVar6 = dVar14;
      *pdVar4 = dVar13;
    }
LAB_00be8290:
    dVar14 = *pdVar6;
    param_4 = param_4 + -1;
    param_1 = pdVar6;
    if (((param_5 & 1) != 0) || (pdVar6[-1] < dVar14)) {
      lVar5 = 0;
      do {
        lVar1 = lVar5 + 8;
        dVar13 = *(double *)((long)pdVar6 + lVar5 + 8);
        lVar5 = lVar1;
      } while (dVar13 < dVar14);
      pdVar4 = (double *)((long)pdVar6 + lVar1);
      pdVar8 = param_2;
      if (lVar1 == 8) {
        do {
          if (pdVar8 <= pdVar4) break;
          pdVar8 = pdVar8 + -1;
        } while (dVar14 <= *pdVar8);
      }
      else {
        do {
          pdVar8 = pdVar8 + -1;
        } while (dVar14 <= *pdVar8);
      }
      if (pdVar4 < pdVar8) {
        dVar15 = *pdVar8;
        pdVar10 = pdVar4;
        pdVar11 = pdVar8;
        do {
          *pdVar10 = dVar15;
          *pdVar11 = dVar13;
          do {
            pdVar7 = pdVar10;
            pdVar10 = pdVar7 + 1;
            dVar13 = *pdVar10;
          } while (dVar13 < dVar14);
          do {
            pdVar11 = pdVar11 + -1;
            dVar15 = *pdVar11;
          } while (dVar14 <= dVar15);
        } while (pdVar10 < pdVar11);
      }
      else {
        pdVar7 = pdVar4 + -1;
      }
      if (pdVar7 != pdVar6) {
        *pdVar6 = *pdVar7;
      }
      *pdVar7 = dVar14;
      if (pdVar4 < pdVar8) {
LAB_00be838c:
        FUN_00be7fdc(pdVar6,pdVar7);
        param_5 = 0;
        param_1 = pdVar7 + 1;
      }
      else {
        uVar3 = FUN_00bee91c(pdVar6,pdVar7);
        uVar2 = FUN_00bee91c(pdVar7 + 1,param_2);
        if ((uVar2 & 1) == 0) {
          param_1 = pdVar7 + 1;
          if ((uVar3 & 1) == 0) goto LAB_00be838c;
        }
        else {
          param_2 = pdVar7;
          if ((uVar3 & 1) != 0) {
            return;
          }
        }
      }
      goto LAB_00be8010;
    }
    if (param_2[-1] <= dVar14) {
      do {
        param_1 = param_1 + 1;
        if (param_2 <= param_1) break;
      } while (*param_1 <= dVar14);
    }
    else {
      do {
        param_1 = param_1 + 1;
      } while (*param_1 <= dVar14);
    }
    pdVar4 = param_2;
    if (param_1 < param_2) {
      do {
        pdVar4 = pdVar4 + -1;
      } while (dVar14 < *pdVar4);
    }
    if (param_1 < pdVar4) {
      dVar13 = *param_1;
      dVar15 = *pdVar4;
      do {
        *param_1 = dVar15;
        *pdVar4 = dVar13;
        do {
          param_1 = param_1 + 1;
          dVar13 = *param_1;
        } while (dVar13 <= dVar14);
        do {
          pdVar4 = pdVar4 + -1;
          dVar15 = *pdVar4;
        } while (dVar14 < dVar15);
      } while (param_1 < pdVar4);
    }
    pdVar4 = param_1 + -1;
    if (pdVar4 != pdVar6) {
      *pdVar6 = *pdVar4;
    }
    param_5 = 0;
    *pdVar4 = dVar14;
  } while( true );
}

~~~
