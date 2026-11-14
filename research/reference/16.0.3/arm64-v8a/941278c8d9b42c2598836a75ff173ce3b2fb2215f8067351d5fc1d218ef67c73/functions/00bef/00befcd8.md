# 00befcd8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00befcd8",
  "name": "FUN_00befcd8",
  "size": 728,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4066c7fca1553ea07b4ebdc6ed7d2cd74bac00463506fce16f7b38ddc8142d69",
  "source_text_sha256": "4066c7fca1553ea07b4ebdc6ed7d2cd74bac00463506fce16f7b38ddc8142d69"
}
~~~

## 呼び出し元

- [00be8fd0](../00be8/00be8fd0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 4728 bytes

~~~c

double * FUN_00befcd8(double *param_1,double *param_2,double *param_3)

{
  bool bVar1;
  ulong uVar2;
  long lVar3;
  double *pdVar4;
  double *pdVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  double *pdVar11;
  double *pdVar12;
  double dVar13;
  double dVar14;
  
  if (param_1 != param_2) {
    lVar3 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar3) {
      uVar7 = lVar3 - 2U >> 1;
      uVar10 = uVar7;
      do {
        if ((long)uVar10 <= (long)uVar7) {
          uVar9 = (uVar10 & 0x1fffffffffffffff) << 1 | 1;
          uVar8 = (uVar10 & 0x1fffffffffffffff) * 2 + 2;
          pdVar5 = param_1 + uVar9;
          if (((long)uVar8 < lVar3) && (*pdVar5 < pdVar5[1])) {
            uVar9 = uVar8;
            pdVar5 = pdVar5 + 1;
          }
          dVar14 = *pdVar5;
          dVar13 = param_1[uVar10];
          pdVar4 = param_1 + uVar10;
          if (dVar13 <= dVar14) {
            do {
              pdVar12 = pdVar5;
              *pdVar4 = dVar14;
              if ((long)uVar7 < (long)uVar9) break;
              uVar2 = uVar9 << 1 | 1;
              uVar8 = uVar9 * 2 + 2;
              pdVar5 = param_1 + uVar2;
              uVar9 = uVar2;
              if (((long)uVar8 < lVar3) && (*pdVar5 < pdVar5[1])) {
                uVar9 = uVar8;
                pdVar5 = pdVar5 + 1;
              }
              dVar14 = *pdVar5;
              pdVar4 = pdVar12;
            } while (dVar13 <= dVar14);
            *pdVar12 = dVar13;
          }
        }
        bVar1 = 0 < (long)uVar10;
        uVar10 = uVar10 - 1;
      } while (bVar1);
    }
    pdVar5 = param_2;
    if (param_2 != param_3) {
      pdVar4 = param_2;
      do {
        dVar13 = *pdVar4;
        if (dVar13 < *param_1) {
          *pdVar4 = *param_1;
          *param_1 = dVar13;
          if (1 < lVar3) {
            if (((long)param_2 - (long)param_1 == 0x10) || (param_1[2] <= param_1[1])) {
              uVar10 = 1;
              pdVar5 = param_1 + 1;
            }
            else {
              uVar10 = 2;
              pdVar5 = param_1 + 2;
            }
            dVar14 = *pdVar5;
            pdVar12 = param_1;
            if (dVar13 <= dVar14) {
              do {
                pdVar11 = pdVar5;
                *pdVar12 = dVar14;
                if ((long)(lVar3 - 2U >> 1) < (long)uVar10) break;
                uVar8 = uVar10 << 1 | 1;
                uVar7 = uVar10 * 2 + 2;
                pdVar5 = param_1 + uVar8;
                uVar10 = uVar8;
                if (((long)uVar7 < lVar3) && (*pdVar5 < pdVar5[1])) {
                  uVar10 = uVar7;
                  pdVar5 = pdVar5 + 1;
                }
                dVar14 = *pdVar5;
                pdVar12 = pdVar11;
              } while (dVar13 <= dVar14);
              *pdVar11 = dVar13;
            }
          }
        }
        pdVar4 = pdVar4 + 1;
        pdVar5 = param_3;
      } while (pdVar4 != param_3);
    }
    param_3 = pdVar5;
    if (1 < lVar3) {
      do {
        dVar13 = *param_1;
        pdVar5 = param_1;
        uVar10 = 0;
        do {
          uVar8 = uVar10 << 1 | 1;
          uVar7 = uVar10 * 2 + 2;
          pdVar4 = pdVar5 + uVar10 + 1;
          if (((long)uVar7 < lVar3) && (pdVar5[uVar10 + 1] < pdVar5[uVar10 + 2])) {
            pdVar4 = pdVar5 + uVar10 + 2;
            uVar8 = uVar7;
          }
          *pdVar5 = *pdVar4;
          pdVar5 = pdVar4;
          uVar10 = uVar8;
        } while ((long)uVar8 <= (long)(lVar3 - 2U >> 1));
        param_2 = param_2 + -1;
        if (pdVar4 == param_2) {
LAB_00befec8:
          *pdVar4 = dVar13;
        }
        else {
          lVar6 = (long)pdVar4 + (8 - (long)param_1) >> 3;
          *pdVar4 = *param_2;
          *param_2 = dVar13;
          if (1 < lVar6) {
            uVar10 = lVar6 - 2U >> 1;
            dVar13 = *pdVar4;
            dVar14 = param_1[uVar10];
            pdVar12 = param_1 + uVar10;
            if (dVar14 < dVar13) {
              do {
                pdVar4 = pdVar12;
                    /* try { // try from 00beff88 to 00cf0023 has its CatchHandler @ 00beff88
                       catch() { ... } // from try @ 00beff88 with catch @ 00beff88
                       catch() { ... } // from try @ 00bf0030 with catch @ 00beff88 */
                *pdVar5 = dVar14;
                if (uVar10 == 0) break;
                uVar10 = uVar10 - 1 >> 1;
                dVar14 = param_1[uVar10];
                pdVar5 = pdVar4;
                pdVar12 = param_1 + uVar10;
              } while (dVar14 < dVar13);
              goto LAB_00befec8;
            }
          }
        }
        bVar1 = 2 < lVar3;
        lVar3 = lVar3 + -1;
      } while (bVar1);
    }
  }
  return param_3;
}

~~~
