# 00bedee4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bedee4",
  "name": "FUN_00bedee4",
  "size": 764,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77c445730ef6cd745f4b0c98e722e6f23b74f933477fe05b959fabb3e29dd76f",
  "source_text_sha256": "77c445730ef6cd745f4b0c98e722e6f23b74f933477fe05b959fabb3e29dd76f"
}
~~~

## 呼び出し元

- [00be7110](../00be7/00be7110.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 7468 bytes

~~~c

ulong * FUN_00bedee4(ulong *param_1,ulong *param_2,ulong *param_3)

{
  ulong *puVar1;
  bool bVar2;
  ulong uVar3;
  ulong *puVar4;
  ulong uVar5;
  long lVar6;
  ulong *puVar7;
  ulong uVar8;
  long lVar9;
  ulong *puVar10;
  ulong *puVar11;
  ulong uVar12;
  ulong uVar13;
  ulong uVar14;
  ulong *puVar15;
  ulong uVar16;
  ulong uVar17;
  
  if (param_1 != param_2) {
    lVar6 = (long)param_2 - (long)param_1 >> 3;
    if (1 < lVar6) {
      uVar8 = lVar6 - 2U >> 1;
      uVar13 = uVar8;
      do {
        if ((long)uVar13 <= (long)uVar8) {
          uVar12 = (uVar13 & 0x1fffffffffffffff) << 1 | 1;
          uVar5 = (uVar13 & 0x1fffffffffffffff) * 2 + 2;
          puVar10 = param_1 + uVar12;
                    /* try { // try from 00bedf3c to 00cedf43 has its CatchHandler @ 00bee74c */
          if ((long)uVar5 < lVar6) {
            uVar16 = *puVar10;
                    /* try { // try from 00bedf48 to 00cedf5f has its CatchHandler @ 00bee744 */
            uVar3 = puVar10[1];
            uVar14 = uVar16;
            if (uVar16 <= uVar3) {
              uVar14 = uVar3;
            }
            puVar11 = puVar10 + 1;
            if (uVar3 <= uVar16) {
              puVar11 = puVar10;
              uVar5 = uVar12;
            }
          }
          else {
            uVar14 = *puVar10;
            puVar11 = puVar10;
            uVar5 = uVar12;
          }
          uVar12 = param_1[uVar13];
                    /* try { // try from 00bedf6c to 00cedf87 has its CatchHandler @ 00bee7b4 */
          puVar10 = param_1 + uVar13;
          if (uVar12 <= uVar14) {
            do {
              while( true ) {
                puVar7 = puVar11;
                *puVar10 = uVar14;
                if ((long)uVar8 < (long)uVar5) goto LAB_00bedf0c;
                uVar3 = uVar5 << 1 | 1;
                uVar5 = uVar5 * 2 + 2;
                puVar4 = param_1 + uVar3;
                puVar10 = puVar7;
                if ((long)uVar5 < lVar6) break;
                uVar14 = *puVar4;
                puVar11 = puVar4;
                uVar5 = uVar3;
                if (uVar14 < uVar12) goto LAB_00bedf0c;
              }
              uVar17 = *puVar4;
              uVar16 = puVar4[1];
                    /* try { // try from 00bedf88 to 00cee03f has its CatchHandler @ 00bedde0 */
              uVar14 = uVar17;
              if (uVar17 <= uVar16) {
                uVar14 = uVar16;
              }
              puVar11 = puVar4 + 1;
              if (uVar16 <= uVar17) {
                uVar5 = uVar3;
                puVar11 = puVar4;
              }
            } while (uVar12 <= uVar14);
LAB_00bedf0c:
            *puVar7 = uVar12;
          }
        }
        bVar2 = 0 < (long)uVar13;
        uVar13 = uVar13 - 1;
      } while (bVar2);
    }
    puVar10 = param_2;
    if (param_2 != param_3) {
      puVar11 = param_1 + 1;
      puVar7 = param_2;
      do {
        uVar13 = *puVar7;
        if (uVar13 < *param_1) {
          *puVar7 = *param_1;
          *param_1 = uVar13;
          if (1 < lVar6) {
            uVar8 = *puVar11;
            if ((long)param_2 - (long)param_1 == 0x10) {
                    /* try { // try from 00bee040 to 00cee063 has its CatchHandler @ 00bee704 */
              uVar5 = 1;
              puVar10 = puVar11;
            }
            else {
              uVar5 = param_1[2];
              bVar2 = uVar5 <= uVar8;
              if (uVar8 <= uVar5) {
                uVar8 = uVar5;
              }
              puVar10 = param_1 + 2;
              if (bVar2) {
                puVar10 = puVar11;
              }
              uVar5 = 1;
              if (!bVar2) {
                uVar5 = 2;
              }
            }
                    /* try { // try from 00bee064 to 00cee0b3 has its CatchHandler @ 00bedde0 */
            puVar4 = param_1;
            if (uVar13 <= uVar8) {
              do {
                while( true ) {
                  puVar15 = puVar10;
                  *puVar4 = uVar8;
                  if ((long)(lVar6 - 2U >> 1) < (long)uVar5) goto LAB_00bee000;
                  uVar12 = uVar5 << 1 | 1;
                    /* try { // try from 00bee0b4 to 00cee0db has its CatchHandler @ 00bee6fc */
                  uVar5 = uVar5 * 2 + 2;
                  puVar1 = param_1 + uVar12;
                  puVar4 = puVar15;
                  if ((long)uVar5 < lVar6) break;
                  uVar8 = *puVar1;
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                  if (uVar8 < uVar13) goto LAB_00bee000;
                }
                uVar3 = *puVar1;
                uVar14 = puVar1[1];
                uVar8 = uVar3;
                if (uVar3 <= uVar14) {
                  uVar8 = uVar14;
                }
                puVar10 = puVar1 + 1;
                if (uVar14 <= uVar3) {
                  uVar5 = uVar12;
                  puVar10 = puVar1;
                }
              } while (uVar13 <= uVar8);
LAB_00bee000:
              *puVar15 = uVar13;
            }
          }
        }
        puVar7 = puVar7 + 1;
        puVar10 = param_3;
      } while (puVar7 != param_3);
    }
    param_3 = puVar10;
    if (1 < lVar6) {
      do {
        uVar8 = *param_1;
        uVar13 = 0;
        puVar10 = param_1;
                    /* try { // try from 00bee114 to 00cee12f has its CatchHandler @ 00bee794 */
        do {
          uVar12 = uVar13 << 1 | 1;
          uVar5 = uVar13 * 2 + 2;
          puVar11 = puVar10 + uVar13 + 1;
          if ((long)uVar5 < lVar6) {
            uVar3 = puVar10[uVar13 + 2];
            uVar16 = puVar10[uVar13 + 1];
            uVar14 = uVar16;
            if (uVar16 <= uVar3) {
              uVar14 = uVar3;
            }
            puVar7 = puVar10 + uVar13 + 2;
            uVar13 = uVar5;
            if (uVar3 <= uVar16) {
              puVar7 = puVar11;
              uVar13 = uVar12;
            }
          }
          else {
            uVar14 = *puVar11;
            puVar7 = puVar11;
            uVar13 = uVar12;
          }
                    /* try { // try from 00bee130 to 00cee1db has its CatchHandler @ 00bedde0 */
          *puVar10 = uVar14;
          puVar10 = puVar7;
        } while ((long)uVar13 <= (long)(lVar6 - 2U >> 1));
        param_2 = param_2 + -1;
        if (puVar7 == param_2) {
          *puVar7 = uVar8;
        }
        else {
          lVar9 = (long)puVar7 + (8 - (long)param_1) >> 3;
          *puVar7 = *param_2;
          *param_2 = uVar8;
          if (1 < lVar9) {
            uVar13 = lVar9 - 2U >> 1;
            uVar8 = *puVar7;
            uVar5 = param_1[uVar13];
            puVar10 = param_1 + uVar13;
            if (uVar5 < uVar8) {
              do {
                puVar11 = puVar10;
                *puVar7 = uVar5;
                if (uVar13 == 0) break;
                uVar13 = uVar13 - 1 >> 1;
                uVar5 = param_1[uVar13];
                puVar7 = puVar11;
                puVar10 = param_1 + uVar13;
              } while (uVar5 < uVar8);
              *puVar11 = uVar8;
                    /* try { // try from 00bee1dc to 00cee257 has its CatchHandler @ 00bee754 */
            }
          }
        }
                    /* try { // try from 00bee0f4 to 00cee10b has its CatchHandler @ 00bee6ec */
        bVar2 = 2 < lVar6;
        lVar6 = lVar6 + -1;
      } while (bVar2);
    }
  }
                    /* try { // try from 00bee0e8 to 00cee0ef has its CatchHandler @ 00bee6f4 */
  return param_3;
}

~~~
