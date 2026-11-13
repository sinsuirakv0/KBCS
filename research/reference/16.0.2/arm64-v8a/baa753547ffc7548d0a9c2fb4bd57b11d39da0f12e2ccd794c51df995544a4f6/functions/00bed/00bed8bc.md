# 00bed8bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bed8bc",
  "name": "FUN_00bed8bc",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "504bddb99ace1ca42837ff29eae25d2f3325c7a30dc7cdefe5e9b80c772091da",
  "source_text_sha256": "504bddb99ace1ca42837ff29eae25d2f3325c7a30dc7cdefe5e9b80c772091da"
}
~~~

## 呼び出し元

- [00be6a94](../00be6/00be6a94.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 7008 bytes

~~~c

long * FUN_00bed8bc(long *param_1,long *param_2,long *param_3)

{
  bool bVar1;
  long *plVar2;
  ulong uVar3;
  long lVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  long *plVar8;
  ulong uVar9;
  long *plVar10;
  long *plVar11;
  ulong uVar12;
  long lVar13;
  long lVar14;
  long *plVar15;
  long lVar16;
  
  if (param_1 != param_2) {
    lVar7 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar7) {
      uVar9 = lVar7 - 2U >> 1;
      uVar6 = uVar9;
      do {
        if ((long)uVar6 <= (long)uVar9) {
          uVar3 = (uVar6 & 0x1fffffffffffffff) << 1 | 1;
          uVar12 = (uVar6 & 0x1fffffffffffffff) * 2 + 2;
          plVar10 = param_1 + uVar3;
          if ((long)uVar12 < lVar7) {
            lVar16 = *plVar10;
            lVar4 = plVar10[1];
            lVar13 = lVar16;
            if (lVar16 <= lVar4) {
              lVar13 = lVar4;
            }
            plVar11 = plVar10 + 1;
            if (lVar4 <= lVar16) {
              plVar11 = plVar10;
              uVar12 = uVar3;
            }
          }
          else {
            lVar13 = *plVar10;
            plVar11 = plVar10;
            uVar12 = uVar3;
          }
          lVar4 = param_1[uVar6];
          plVar10 = param_1 + uVar6;
          if (lVar4 <= lVar13) {
            do {
              while( true ) {
                plVar8 = plVar11;
                *plVar10 = lVar13;
                if ((long)uVar9 < (long)uVar12) goto LAB_00bed8e4;
                uVar3 = uVar12 << 1 | 1;
                uVar12 = uVar12 * 2 + 2;
                plVar5 = param_1 + uVar3;
                plVar10 = plVar8;
                if ((long)uVar12 < lVar7) break;
                lVar13 = *plVar5;
                plVar11 = plVar5;
                uVar12 = uVar3;
                if (lVar13 < lVar4) goto LAB_00bed8e4;
              }
              lVar14 = *plVar5;
              lVar16 = plVar5[1];
              lVar13 = lVar14;
              if (lVar14 <= lVar16) {
                lVar13 = lVar16;
              }
              plVar11 = plVar5 + 1;
              if (lVar16 <= lVar14) {
                uVar12 = uVar3;
                plVar11 = plVar5;
              }
            } while (lVar4 <= lVar13);
LAB_00bed8e4:
            *plVar8 = lVar4;
          }
        }
        bVar1 = 0 < (long)uVar6;
        uVar6 = uVar6 - 1;
      } while (bVar1);
    }
    plVar10 = param_2;
    if (param_2 != param_3) {
      plVar11 = param_1 + 1;
      plVar8 = param_2;
      do {
        lVar13 = *plVar8;
                    /* try { // try from 00bed9ec to 00ceda8f has its CatchHandler @ 00bed9ec
                       catch() { ... } // from try @ 00bed9ec with catch @ 00bed9ec
                       catch() { ... } // from try @ 00bedafc with catch @ 00bed9ec
                       catch() { ... } // from try @ 00bedcbc with catch @ 00bed9ec */
        if (lVar13 < *param_1) {
          *plVar8 = *param_1;
          *param_1 = lVar13;
          if (1 < lVar7) {
            lVar16 = *plVar11;
            lVar4 = lVar16;
            if ((long)param_2 - (long)param_1 == 0x10) {
              uVar6 = 1;
              plVar10 = plVar11;
            }
            else {
              lVar14 = param_1[2];
              if (lVar16 <= lVar14) {
                lVar4 = lVar14;
              }
              plVar10 = param_1 + 2;
              if (lVar14 <= lVar16) {
                plVar10 = plVar11;
              }
              uVar6 = 1;
              if (lVar16 < lVar14) {
                uVar6 = 2;
              }
            }
            plVar5 = param_1;
            if (lVar13 <= lVar4) {
              do {
                while( true ) {
                  plVar15 = plVar10;
                  *plVar5 = lVar4;
                  if ((long)(lVar7 - 2U >> 1) < (long)uVar6) goto LAB_00bed9d8;
                  uVar9 = uVar6 << 1 | 1;
                  uVar6 = uVar6 * 2 + 2;
                    /* try { // try from 00beda90 to 00ceda9b has its CatchHandler @ 00bedd44 */
                  plVar2 = param_1 + uVar9;
                  plVar5 = plVar15;
                  if ((long)uVar6 < lVar7) break;
                    /* try { // try from 00beda9c to 00cedabf has its CatchHandler @ 00bedde0 */
                  lVar4 = *plVar2;
                  uVar6 = uVar9;
                  plVar10 = plVar2;
                  if (lVar4 < lVar13) goto LAB_00bed9d8;
                }
                lVar14 = *plVar2;
                lVar16 = plVar2[1];
                lVar4 = lVar14;
                if (lVar14 <= lVar16) {
                  lVar4 = lVar16;
                }
                plVar10 = plVar2 + 1;
                if (lVar16 <= lVar14) {
                  uVar6 = uVar9;
                  plVar10 = plVar2;
                }
              } while (lVar13 <= lVar4);
LAB_00bed9d8:
              *plVar15 = lVar13;
            }
          }
        }
        plVar8 = plVar8 + 1;
        plVar10 = param_3;
      } while (plVar8 != param_3);
    }
    param_3 = plVar10;
    if (1 < lVar7) {
      do {
                    /* try { // try from 00bedad8 to 00cedafb has its CatchHandler @ 00bedd54 */
        lVar13 = *param_1;
        uVar6 = 0;
        plVar10 = param_1;
        do {
          uVar12 = uVar6 << 1 | 1;
          uVar9 = uVar6 * 2 + 2;
          plVar11 = plVar10 + uVar6 + 1;
          if ((long)uVar9 < lVar7) {
            lVar16 = plVar10[uVar6 + 2];
            lVar14 = plVar10[uVar6 + 1];
                    /* try { // try from 00bedafc to 00cedcb3 has its CatchHandler @ 00bed9ec */
            lVar4 = lVar14;
            if (lVar14 <= lVar16) {
              lVar4 = lVar16;
            }
            plVar8 = plVar10 + uVar6 + 2;
            uVar6 = uVar9;
            if (lVar16 <= lVar14) {
              plVar8 = plVar11;
              uVar6 = uVar12;
            }
          }
          else {
            lVar4 = *plVar11;
            plVar8 = plVar11;
            uVar6 = uVar12;
          }
          *plVar10 = lVar4;
          plVar10 = plVar8;
        } while ((long)uVar6 <= (long)(lVar7 - 2U >> 1));
        param_2 = param_2 + -1;
        if (plVar8 == param_2) {
          *plVar8 = lVar13;
        }
        else {
          lVar4 = (long)plVar8 + (8 - (long)param_1) >> 3;
          *plVar8 = *param_2;
          *param_2 = lVar13;
          if (1 < lVar4) {
            uVar6 = lVar4 - 2U >> 1;
            lVar13 = *plVar8;
            lVar4 = param_1[uVar6];
            plVar10 = param_1 + uVar6;
            if (lVar4 < lVar13) {
              do {
                plVar11 = plVar10;
                *plVar8 = lVar4;
                if (uVar6 == 0) break;
                uVar6 = uVar6 - 1 >> 1;
                lVar4 = param_1[uVar6];
                plVar8 = plVar11;
                plVar10 = param_1 + uVar6;
              } while (lVar4 < lVar13);
              *plVar11 = lVar13;
            }
          }
        }
        bVar1 = 2 < lVar7;
        lVar7 = lVar7 + -1;
      } while (bVar1);
    }
  }
  return param_3;
}

~~~
