# 00becda0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00becda0",
  "name": "FUN_00becda0",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6eeb278815534cae5bc56ac05f5389c7eb00277d70b026778243be98758af271",
  "source_text_sha256": "6eeb278815534cae5bc56ac05f5389c7eb00277d70b026778243be98758af271"
}
~~~

## 呼び出し元

- [00be5e28](../00be5/00be5e28.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 6640 bytes

~~~c

int * FUN_00becda0(int *param_1,int *param_2,int *param_3)

{
  bool bVar1;
  int *piVar2;
  ulong uVar3;
  int iVar4;
  int iVar5;
  int *piVar6;
  ulong uVar7;
  long lVar8;
  int *piVar9;
  ulong uVar10;
  long lVar11;
  int *piVar12;
  int *piVar13;
  ulong uVar14;
  int *piVar15;
  int iVar16;
  int iVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 2;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar3 = (uVar7 & 0x3fffffffffffffff) << 1 | 1;
          uVar14 = (uVar7 & 0x3fffffffffffffff) * 2 + 2;
          piVar12 = param_1 + uVar3;
          if ((long)uVar14 < lVar8) {
                    /* try { // try from 00becdfc to 00cece17 has its CatchHandler @ 00becf98 */
            iVar17 = *piVar12;
            iVar4 = piVar12[1];
            iVar16 = iVar17;
            if (iVar17 <= iVar4) {
              iVar16 = iVar4;
            }
            piVar13 = piVar12 + 1;
            if (iVar4 <= iVar17) {
              piVar13 = piVar12;
              uVar14 = uVar3;
            }
          }
          else {
            iVar16 = *piVar12;
            piVar13 = piVar12;
            uVar14 = uVar3;
          }
          iVar17 = param_1[uVar7];
          piVar12 = param_1 + uVar7;
          if (iVar17 <= iVar16) {
            do {
              while( true ) {
                piVar9 = piVar13;
                *piVar12 = iVar16;
                if ((long)uVar10 < (long)uVar14) goto LAB_00becdc8;
                uVar3 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                piVar6 = param_1 + uVar3;
                piVar12 = piVar9;
                if ((long)uVar14 < lVar8) break;
                iVar16 = *piVar6;
                piVar13 = piVar6;
                uVar14 = uVar3;
                if (iVar16 < iVar17) goto LAB_00becdc8;
              }
              iVar4 = *piVar6;
              iVar5 = piVar6[1];
              iVar16 = iVar4;
              if (iVar4 <= iVar5) {
                iVar16 = iVar5;
              }
              piVar13 = piVar6 + 1;
              if (iVar5 <= iVar4) {
                uVar14 = uVar3;
                piVar13 = piVar6;
              }
            } while (iVar17 <= iVar16);
LAB_00becdc8:
            *piVar9 = iVar17;
          }
        }
                    /* try { // try from 00becdcc to 00cecdd7 has its CatchHandler @ 00becf88 */
        bVar1 = 0 < (long)uVar7;
        uVar7 = uVar7 - 1;
      } while (bVar1);
    }
    piVar12 = param_2;
    if (param_2 != param_3) {
      piVar13 = param_1 + 1;
      piVar9 = param_2;
      do {
        iVar16 = *piVar9;
        if (iVar16 < *param_1) {
          *piVar9 = *param_1;
          *param_1 = iVar16;
          if (1 < lVar8) {
            iVar4 = *piVar13;
            iVar17 = iVar4;
            if ((long)param_2 - (long)param_1 == 8) {
              uVar7 = 1;
              piVar12 = piVar13;
            }
            else {
              iVar5 = param_1[2];
              if (iVar4 <= iVar5) {
                iVar17 = iVar5;
              }
              piVar12 = param_1 + 2;
              if (iVar5 <= iVar4) {
                piVar12 = piVar13;
              }
              uVar7 = 1;
              if (iVar4 < iVar5) {
                uVar7 = 2;
              }
            }
            piVar6 = param_1;
            if (iVar16 <= iVar17) {
              do {
                while( true ) {
                  piVar15 = piVar12;
                  *piVar6 = iVar17;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00becebc;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  piVar2 = param_1 + uVar10;
                  piVar6 = piVar15;
                  if ((long)uVar7 < lVar8) break;
                  iVar17 = *piVar2;
                    /* catch() { ... } // from try @ 00becdcc with catch @ 00becf88 */
                  uVar7 = uVar10;
                  piVar12 = piVar2;
                  if (iVar17 < iVar16) goto LAB_00becebc;
                }
                iVar4 = *piVar2;
                iVar5 = piVar2[1];
                iVar17 = iVar4;
                if (iVar4 <= iVar5) {
                  iVar17 = iVar5;
                }
                piVar12 = piVar2 + 1;
                if (iVar5 <= iVar4) {
                  uVar7 = uVar10;
                  piVar12 = piVar2;
                }
              } while (iVar16 <= iVar17);
LAB_00becebc:
              *piVar15 = iVar16;
            }
          }
        }
        piVar9 = piVar9 + 1;
        piVar12 = param_3;
      } while (piVar9 != param_3);
    }
                    /* catch() { ... } // from try @ 00becdfc with catch @ 00becf98 */
    param_3 = piVar12;
    if (1 < lVar8) {
      do {
        iVar16 = *param_1;
        uVar7 = 0;
        piVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          piVar13 = piVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            iVar5 = piVar12[uVar7 + 2];
            iVar4 = piVar12[uVar7 + 1];
            iVar17 = iVar4;
            if (iVar4 <= iVar5) {
              iVar17 = iVar5;
            }
            piVar9 = piVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (iVar5 <= iVar4) {
              piVar9 = piVar13;
              uVar7 = uVar14;
            }
          }
          else {
            iVar17 = *piVar13;
            piVar9 = piVar13;
            uVar7 = uVar14;
          }
          *piVar12 = iVar17;
          piVar12 = piVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (piVar9 == param_2) {
          *piVar9 = iVar16;
        }
        else {
          lVar11 = (long)piVar9 + (4 - (long)param_1) >> 2;
          *piVar9 = *param_2;
          *param_2 = iVar16;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            iVar16 = *piVar9;
            iVar17 = param_1[uVar7];
            piVar12 = param_1 + uVar7;
            if (iVar17 < iVar16) {
              do {
                piVar13 = piVar12;
                *piVar9 = iVar17;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                iVar17 = param_1[uVar7];
                piVar9 = piVar13;
                piVar12 = param_1 + uVar7;
              } while (iVar17 < iVar16);
              *piVar13 = iVar16;
            }
          }
        }
        bVar1 = 2 < lVar8;
        lVar8 = lVar8 + -1;
      } while (bVar1);
    }
  }
  return param_3;
}

~~~
