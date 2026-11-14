# 00bec6dc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bec6dc",
  "name": "FUN_00bec6dc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "788d69b12ea34b9ef40418d28e65e9bf8736a0f4b22584429c9f9154f5dbbc03",
  "source_text_sha256": "788d69b12ea34b9ef40418d28e65e9bf8736a0f4b22584429c9f9154f5dbbc03"
}
~~~

## 呼び出し元

- [00be56ec](../00be5/00be56ec.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 6265 bytes

~~~c

ushort * FUN_00bec6dc(ushort *param_1,ushort *param_2,ushort *param_3)

{
  ushort *puVar1;
  ulong uVar2;
  ushort uVar3;
  ushort uVar4;
  bool bVar5;
  ushort *puVar6;
  ulong uVar7;
  long lVar8;
  ushort *puVar9;
  ulong uVar10;
  long lVar11;
  ushort *puVar12;
  ushort *puVar13;
  ulong uVar14;
  ushort uVar15;
  ushort *puVar16;
  ushort uVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 1;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar2 = uVar7 << 1 | 1;
          uVar14 = uVar7 * 2 + 2;
          puVar12 = param_1 + uVar2;
          if ((long)uVar14 < lVar8) {
            uVar15 = *puVar12;
            uVar3 = puVar12[1];
            uVar17 = uVar15;
            if (uVar15 <= uVar3) {
              uVar17 = uVar3;
            }
            puVar13 = puVar12 + 1;
            if (uVar3 <= uVar15) {
              puVar13 = puVar12;
              uVar14 = uVar2;
            }
          }
          else {
            uVar17 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar2;
          }
          uVar15 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if (uVar15 <= uVar17) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar17;
                if ((long)uVar10 < (long)uVar14) goto LAB_00bec704;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar17 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar17 < uVar15) goto LAB_00bec704;
              }
              uVar3 = *puVar6;
              uVar4 = puVar6[1];
              uVar17 = uVar3;
              if (uVar3 <= uVar4) {
                uVar17 = uVar4;
              }
              puVar13 = puVar6 + 1;
              if (uVar4 <= uVar3) {
                uVar14 = uVar2;
                puVar13 = puVar6;
              }
            } while (uVar15 <= uVar17);
LAB_00bec704:
            *puVar9 = uVar15;
          }
        }
        bVar5 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar5);
    }
    puVar12 = param_2;
    if (param_2 != param_3) {
      puVar13 = param_1 + 1;
      puVar9 = param_2;
      do {
        uVar17 = *puVar9;
        if (uVar17 < *param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar17;
          if (1 < lVar8) {
            uVar15 = *puVar13;
            if ((long)param_2 - (long)param_1 == 4) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar3 = param_1[2];
              bVar5 = uVar3 <= uVar15;
              if (uVar15 <= uVar3) {
                uVar15 = uVar3;
              }
              puVar12 = param_1 + 2;
              if (bVar5) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if (!bVar5) {
                uVar7 = 2;
              }
            }
            puVar6 = param_1;
            if (uVar17 <= uVar15) {
              do {
                while( true ) {
                  puVar16 = puVar12;
                  *puVar6 = uVar15;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00bec7f8;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar16;
                  if ((long)uVar7 < lVar8) break;
                  uVar15 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar15 < uVar17) goto LAB_00bec7f8;
                }
                uVar3 = *puVar1;
                uVar4 = puVar1[1];
                uVar15 = uVar3;
                if (uVar3 <= uVar4) {
                  uVar15 = uVar4;
                }
                puVar12 = puVar1 + 1;
                if (uVar4 <= uVar3) {
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                }
              } while (uVar17 <= uVar15);
LAB_00bec7f8:
              *puVar16 = uVar17;
            }
          }
        }
        puVar9 = puVar9 + 1;
        puVar12 = param_3;
      } while (puVar9 != param_3);
    }
    param_3 = puVar12;
    if (1 < lVar8) {
      do {
        uVar17 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar3 = puVar12[uVar7 + 2];
            uVar4 = puVar12[uVar7 + 1];
            uVar15 = uVar4;
            if (uVar4 <= uVar3) {
              uVar15 = uVar3;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (uVar3 <= uVar4) {
              puVar9 = puVar13;
              uVar7 = uVar14;
            }
          }
          else {
            uVar15 = *puVar13;
            puVar9 = puVar13;
            uVar7 = uVar14;
          }
          *puVar12 = uVar15;
          puVar12 = puVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar9 == param_2) {
          *puVar9 = uVar17;
        }
        else {
          lVar11 = (long)puVar9 + (2 - (long)param_1) >> 1;
          *puVar9 = *param_2;
          *param_2 = uVar17;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar17 = *puVar9;
            uVar15 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if (uVar15 < uVar17) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar15;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar15 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while (uVar15 < uVar17);
              *puVar13 = uVar17;
            }
          }
        }
        bVar5 = 2 < lVar8;
        lVar8 = lVar8 + -1;
      } while (bVar5);
    }
  }
  return param_3;
}

~~~
