# 00beab5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00beab5c",
  "name": "FUN_00beab5c",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bcc16b1a25919ea5b407fcaacf9bdaf581746e48d1f8329c8419114ad85d1c06",
  "source_text_sha256": "bcc16b1a25919ea5b407fcaacf9bdaf581746e48d1f8329c8419114ad85d1c06"
}
~~~

## 呼び出し元

- [00be3a30](../00be3/00be3a30.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 6477 bytes

~~~c

uint * FUN_00beab5c(uint *param_1,uint *param_2,uint *param_3)

{
  uint *puVar1;
  ulong uVar2;
  uint uVar3;
  uint uVar4;
  bool bVar5;
  uint *puVar6;
  ulong uVar7;
  long lVar8;
  uint *puVar9;
  ulong uVar10;
  long lVar11;
  uint *puVar12;
  uint *puVar13;
  ulong uVar14;
  uint *puVar15;
  uint uVar16;
  uint uVar17;
  
  if (param_1 != param_2) {
    lVar8 = (long)param_2 - (long)param_1 >> 2;
    if (1 < lVar8) {
      uVar10 = lVar8 - 2U >> 1;
      uVar7 = uVar10;
      do {
        if ((long)uVar7 <= (long)uVar10) {
          uVar2 = (uVar7 & 0x3fffffffffffffff) << 1 | 1;
          uVar14 = (uVar7 & 0x3fffffffffffffff) * 2 + 2;
          puVar12 = param_1 + uVar2;
          if ((long)uVar14 < lVar8) {
            uVar17 = *puVar12;
            uVar3 = puVar12[1];
            uVar16 = uVar17;
            if (uVar17 <= uVar3) {
              uVar16 = uVar3;
            }
            puVar13 = puVar12 + 1;
            if (uVar3 <= uVar17) {
              puVar13 = puVar12;
              uVar14 = uVar2;
            }
          }
          else {
            uVar16 = *puVar12;
            puVar13 = puVar12;
            uVar14 = uVar2;
          }
          uVar17 = param_1[uVar7];
          puVar12 = param_1 + uVar7;
          if (uVar17 <= uVar16) {
            do {
              while( true ) {
                puVar9 = puVar13;
                *puVar12 = uVar16;
                if ((long)uVar10 < (long)uVar14) goto LAB_00beab84;
                uVar2 = uVar14 << 1 | 1;
                uVar14 = uVar14 * 2 + 2;
                puVar6 = param_1 + uVar2;
                puVar12 = puVar9;
                if ((long)uVar14 < lVar8) break;
                uVar16 = *puVar6;
                puVar13 = puVar6;
                uVar14 = uVar2;
                if (uVar16 < uVar17) goto LAB_00beab84;
              }
              uVar3 = *puVar6;
              uVar4 = puVar6[1];
              uVar16 = uVar3;
              if (uVar3 <= uVar4) {
                uVar16 = uVar4;
              }
              puVar13 = puVar6 + 1;
              if (uVar4 <= uVar3) {
                uVar14 = uVar2;
                puVar13 = puVar6;
              }
            } while (uVar17 <= uVar16);
LAB_00beab84:
            *puVar9 = uVar17;
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
        uVar16 = *puVar9;
        if (uVar16 < *param_1) {
          *puVar9 = *param_1;
          *param_1 = uVar16;
          if (1 < lVar8) {
            uVar17 = *puVar13;
            if ((long)param_2 - (long)param_1 == 8) {
              uVar7 = 1;
              puVar12 = puVar13;
            }
            else {
              uVar3 = param_1[2];
              bVar5 = uVar3 <= uVar17;
              if (uVar17 <= uVar3) {
                uVar17 = uVar3;
              }
              puVar12 = param_1 + 2;
                    /* try { // try from 00beacd4 to 00cead07 has its CatchHandler @ 00beb310 */
              if (bVar5) {
                puVar12 = puVar13;
              }
              uVar7 = 1;
              if (!bVar5) {
                uVar7 = 2;
              }
            }
            puVar6 = param_1;
            if (uVar16 <= uVar17) {
              do {
                while( true ) {
                  puVar15 = puVar12;
                  *puVar6 = uVar17;
                  if ((long)(lVar8 - 2U >> 1) < (long)uVar7) goto LAB_00beac78;
                  uVar10 = uVar7 << 1 | 1;
                  uVar7 = uVar7 * 2 + 2;
                  puVar1 = param_1 + uVar10;
                  puVar6 = puVar15;
                  if ((long)uVar7 < lVar8) break;
                  uVar17 = *puVar1;
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                  if (uVar17 < uVar16) goto LAB_00beac78;
                }
                uVar3 = *puVar1;
                uVar4 = puVar1[1];
                uVar17 = uVar3;
                if (uVar3 <= uVar4) {
                  uVar17 = uVar4;
                }
                puVar12 = puVar1 + 1;
                if (uVar4 <= uVar3) {
                  uVar7 = uVar10;
                  puVar12 = puVar1;
                }
                    /* try { // try from 00bead08 to 00ceaf23 has its CatchHandler @ 00be231c */
              } while (uVar16 <= uVar17);
LAB_00beac78:
              *puVar15 = uVar16;
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
        uVar16 = *param_1;
        uVar7 = 0;
        puVar12 = param_1;
        do {
          uVar14 = uVar7 << 1 | 1;
          uVar10 = uVar7 * 2 + 2;
          puVar13 = puVar12 + uVar7 + 1;
          if ((long)uVar10 < lVar8) {
            uVar4 = puVar12[uVar7 + 2];
            uVar3 = puVar12[uVar7 + 1];
            uVar17 = uVar3;
            if (uVar3 <= uVar4) {
              uVar17 = uVar4;
            }
            puVar9 = puVar12 + uVar7 + 2;
            uVar7 = uVar10;
            if (uVar4 <= uVar3) {
              puVar9 = puVar13;
              uVar7 = uVar14;
            }
          }
          else {
            uVar17 = *puVar13;
            puVar9 = puVar13;
            uVar7 = uVar14;
          }
          *puVar12 = uVar17;
          puVar12 = puVar9;
        } while ((long)uVar7 <= (long)(lVar8 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar9 == param_2) {
          *puVar9 = uVar16;
        }
        else {
          lVar11 = (long)puVar9 + (4 - (long)param_1) >> 2;
          *puVar9 = *param_2;
          *param_2 = uVar16;
          if (1 < lVar11) {
            uVar7 = lVar11 - 2U >> 1;
            uVar16 = *puVar9;
            uVar17 = param_1[uVar7];
            puVar12 = param_1 + uVar7;
            if (uVar17 < uVar16) {
              do {
                puVar13 = puVar12;
                *puVar9 = uVar17;
                if (uVar7 == 0) break;
                uVar7 = uVar7 - 1 >> 1;
                uVar17 = param_1[uVar7];
                puVar9 = puVar13;
                puVar12 = param_1 + uVar7;
              } while (uVar17 < uVar16);
              *puVar13 = uVar16;
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
