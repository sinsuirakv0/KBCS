# 00bc5fdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bc5fdc",
  "name": "FUN_00bc5fdc",
  "size": 852,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "461851f9a14e893071ec627cd161c9efc926b9f801de5ea372b5ceecd34943de",
  "source_text_sha256": "461851f9a14e893071ec627cd161c9efc926b9f801de5ea372b5ceecd34943de"
}
~~~

## 呼び出し元

- [00bc2ec8](../00bc2/00bc2ec8.md)

## 呼び出し先

- [00bbde18](../00bbd/00bbde18.md)
- [00bbff2c](../00bbf/00bbff2c.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 6851 bytes

~~~c

undefined8 * FUN_00bc5fdc(long *param_1)

{
  long *__src;
  long lVar1;
  long lVar2;
  long lVar3;
  long *__ptr;
  undefined8 *puVar4;
  byte *pbVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  long lVar10;
  long *plVar11;
  void *pvVar12;
  undefined1 uVar13;
  byte *pbVar14;
  size_t __n;
  long lVar15;
  byte *pbVar16;
  undefined8 *puVar17;
  undefined1 auVar18 [16];
  
  lVar2 = FUN_00bbde18();
  if ((lVar2 != 0) && (lVar3 = FUN_00bc2ec8(param_1), lVar3 != 0)) {
    pbVar16 = (byte *)*param_1;
    pbVar5 = (byte *)param_1[1];
    pbVar14 = pbVar16;
    if ((pbVar16 != pbVar5) && (*pbVar16 == 0x6e)) {
      pbVar14 = pbVar16 + 1;
      *param_1 = (long)pbVar14;
    }
    if (pbVar5 != pbVar14) {
      if (*pbVar14 - 0x3a < 0xfffffff6) {
        pbVar16 = (byte *)0x0;
        lVar10 = 0;
      }
      else {
        do {
          pbVar8 = pbVar14;
          if (*pbVar14 - 0x3a < 0xfffffff6) break;
          pbVar14 = pbVar14 + 1;
                    /* try { // try from 00bc6084 to 00cc608b has its CatchHandler @ 00bc8ae8 */
          *param_1 = (long)pbVar14;
          pbVar8 = pbVar5;
        } while (pbVar14 != pbVar5);
        lVar10 = (long)pbVar8 - (long)pbVar16;
        pbVar14 = pbVar8;
      }
      if (pbVar14 != pbVar5) {
        lVar7 = param_1[2];
        lVar1 = param_1[3];
        __src = param_1 + 5;
                    /* try { // try from 00bc60c8 to 00cc60d3 has its CatchHandler @ 00bc8538 */
        do {
          if (*pbVar14 != 0x5f) {
                    /* try { // try from 00bc6228 to 00cc6233 has its CatchHandler @ 00bc8504 */
            if ((pbVar14 == pbVar5) || (*pbVar14 != 0x70)) {
                    /* try { // try from 00bc6244 to 00cc6257 has its CatchHandler @ 00bc84d8 */
              uVar13 = 0;
            }
            else {
              pbVar14 = pbVar14 + 1;
              uVar13 = 1;
                    /* try { // try from 00bc6234 to 00cc6243 has its CatchHandler @ 00bc84f0 */
              *param_1 = (long)pbVar14;
            }
            if (pbVar14 == pbVar5) {
              return (undefined8 *)0x0;
            }
            if (*pbVar14 != 0x45) {
              return (undefined8 *)0x0;
            }
            *param_1 = (long)(pbVar14 + 1);
            auVar18 = FUN_00bbff2c(param_1,lVar1 - lVar7 >> 3);
            pvVar12 = (void *)param_1[0x266];
            lVar7 = *(long *)((long)pvVar12 + 8);
            puVar4 = pvVar12;
            if (lVar7 - 4000U < 0xfffffffffffff010) {
              puVar4 = malloc(0x1000);
              if (puVar4 == (void *)0x0) goto LAB_00bc6324;
              lVar7 = 0;
              *puVar4 = pvVar12;
              puVar4[1] = 0;
              param_1[0x266] = (long)puVar4;
            }
            *(long *)((long)puVar4 + 8) = lVar7 + 0x50;
            puVar17 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
            *puVar17 = &PTR_FUN_00c18e88;
            *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 0x3b;
            *(undefined1 (*) [16])((long)puVar4 + lVar7 + 0x40) = auVar18;
                    /* try { // try from 00bc62e4 to 00cc62ef has its CatchHandler @ 00bc8964 */
            *(undefined1 *)((long)puVar4 + lVar7 + 0x50) = uVar13;
            *(ushort *)((long)puVar4 + lVar7 + 0x19) =
                 *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
            *(long *)((long)puVar4 + lVar7 + 0x20) = lVar2;
            *(long *)((long)puVar4 + lVar7 + 0x28) = lVar3;
            *(byte **)((long)puVar4 + lVar7 + 0x30) = pbVar16;
            *(long *)((long)puVar4 + lVar7 + 0x38) = lVar10;
            return puVar17;
          }
          pbVar14 = pbVar14 + 1;
          *param_1 = (long)pbVar14;
          if ((pbVar5 == pbVar14) || (pbVar8 = pbVar14, *pbVar14 - 0x3a < 0xfffffff6)) {
            pbVar14 = (byte *)0x0;
            lVar15 = 0;
          }
          else {
            do {
              pbVar9 = pbVar8;
              if (*pbVar8 - 0x3a < 0xfffffff6) break;
              pbVar8 = pbVar8 + 1;
              *param_1 = (long)pbVar8;
              pbVar9 = pbVar5;
            } while (pbVar8 != pbVar5);
            lVar15 = (long)pbVar9 - (long)pbVar14;
          }
          pvVar12 = (void *)param_1[0x266];
          lVar6 = *(long *)((long)pvVar12 + 8);
                    /* try { // try from 00bc61bc to 00cc61cb has its CatchHandler @ 00bc8d04 */
          puVar4 = pvVar12;
          if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
            puVar4 = malloc(0x1000);
            if (puVar4 == (void *)0x0) {
LAB_00bc6324:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar6 = 0;
            *puVar4 = pvVar12;
            puVar4[1] = 0;
                    /* try { // try from 00bc60d4 to 00cc60e3 has its CatchHandler @ 00bc8524 */
            param_1[0x266] = (long)puVar4;
          }
                    /* try { // try from 00bc60e4 to 00cc60f7 has its CatchHandler @ 00bc850c */
          *(long *)((long)puVar4 + 8) = lVar6 + 0x20;
          puVar17 = (undefined8 *)((long)puVar4 + lVar6 + 0x10);
          *puVar17 = &PTR_FUN_00c17848;
          *(byte **)((long)puVar4 + lVar6 + 0x20) = pbVar14;
          *(undefined1 *)((long)puVar4 + lVar6 + 0x18) = 8;
          *(long *)((long)puVar4 + lVar6 + 0x28) = lVar15;
          *(ushort *)((long)puVar4 + lVar6 + 0x19) =
               *(ushort *)((long)puVar4 + lVar6 + 0x19) & 0xf000 | 0x540;
          plVar11 = (long *)param_1[3];
          if (plVar11 == (long *)param_1[4]) {
            __ptr = (long *)param_1[2];
            __n = (long)plVar11 - (long)__ptr;
            if (__ptr == __src) {
              pvVar12 = malloc(__n * 2);
                    /* try { // try from 00bc61e0 to 00cc61e7 has its CatchHandler @ 00bc8ae8 */
              if (pvVar12 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
              if (plVar11 != __src) {
                memcpy(pvVar12,__src,__n);
              }
              param_1[2] = (long)pvVar12;
            }
            else {
              pvVar12 = realloc(__ptr,__n * 2);
              param_1[2] = (long)pvVar12;
              if (pvVar12 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
            }
            plVar11 = (long *)((long)pvVar12 + __n);
            param_1[4] = (long)((long)pvVar12 + ((long)__n >> 2) * 8);
          }
          param_1[3] = (long)(plVar11 + 1);
          *plVar11 = (long)puVar17;
          pbVar14 = (byte *)*param_1;
          pbVar5 = (byte *)param_1[1];
        } while (pbVar14 != pbVar5);
      }
    }
  }
                    /* try { // try from 00bc631c to 00cc632b has its CatchHandler @ 00bc8cfc */
  return (undefined8 *)0x0;
}

~~~
