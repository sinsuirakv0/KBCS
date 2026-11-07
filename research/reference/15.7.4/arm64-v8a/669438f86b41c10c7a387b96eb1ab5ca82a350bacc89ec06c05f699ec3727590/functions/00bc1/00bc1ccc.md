# 00bc1ccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bc1bc0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1bc0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bc1ccc",
  "name": "FUN_00bc1ccc",
  "size": 964,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5140b3ba974a38c08d1026dad10bc9c0f54dc978a27c32ac0fd166195eaf429d",
  "source_text_sha256": "5140b3ba974a38c08d1026dad10bc9c0f54dc978a27c32ac0fd166195eaf429d"
}
~~~

## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbf39c](../00bbf/00bbf39c.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bce7b8](../00bce/00bce7b8.md)

## 呼び出し先

- [00bc2b00](../00bc2/00bc2b00.md)
- [00bc2bd8](../00bc2/00bc2bd8.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"auto"
~~~

## 疑似コード / UTF-8 6596 bytes

~~~c

undefined8 * FUN_00bc1ccc(long *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined8 *puVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  byte *pbVar10;
  byte *pbVar11;
  undefined8 *puVar12;
  size_t __n;
  ulong uVar13;
  void *pvVar14;
  long *plVar15;
  undefined8 local_48;
  
                    /* try { // try from 00bc1cd8 to 00cc1d57 has its CatchHandler @ 00bc8b14 */
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  if ((pbVar1 != pbVar2) && (*pbVar1 == 0x54)) {
    pbVar11 = pbVar1 + 1;
    *param_1 = (long)pbVar11;
    if (pbVar11 != pbVar2) {
      if (*pbVar11 == 0x4c) {
        pbVar11 = pbVar1 + 2;
        *param_1 = (long)pbVar11;
        if (pbVar2 == pbVar11) {
          return (undefined8 *)0x0;
        }
        if (*pbVar11 - 0x3a < 0xfffffff6) {
          return (undefined8 *)0x0;
        }
        lVar7 = 0;
        pbVar3 = pbVar1 + 4;
        do {
          pbVar11 = pbVar3;
          pbVar10 = pbVar11 + -1;
          *param_1 = (long)pbVar10;
          lVar8 = (ulong)pbVar11[-2] + lVar7 * 10;
          lVar7 = lVar8 + -0x30;
          if (pbVar10 == pbVar2) break;
          pbVar3 = pbVar11 + 1;
        } while (pbVar11[-1] - 0x30 < 10);
        if (pbVar10 == pbVar2) {
          return (undefined8 *)0x0;
        }
        if (pbVar11[-1] != 0x5f) {
          return (undefined8 *)0x0;
        }
        uVar9 = lVar8 - 0x2f;
        *param_1 = (long)pbVar11;
      }
      else {
        uVar9 = 0;
      }
      if (pbVar11 != pbVar2) {
        if (*pbVar11 == 0x5f) {
          uVar13 = 0;
        }
        else {
          if (*pbVar11 - 0x3a < 0xfffffff6) {
            return (undefined8 *)0x0;
          }
          lVar7 = 0;
          pbVar3 = pbVar11;
          do {
            pbVar11 = pbVar3 + 1;
            *param_1 = (long)pbVar11;
            lVar8 = (ulong)*pbVar3 + lVar7 * 10;
            lVar7 = lVar8 + -0x30;
            if (pbVar11 == pbVar2) break;
            pbVar3 = pbVar11;
          } while (*pbVar11 - 0x30 < 10);
          if (pbVar11 == pbVar2) {
            return (undefined8 *)0x0;
          }
          if (*pbVar11 != 0x5f) {
            return (undefined8 *)0x0;
          }
          uVar13 = lVar8 - 0x2f;
        }
        *param_1 = (long)(pbVar11 + 1);
        if (*(char *)((long)param_1 + 0x30a) == '\0') {
          if ((*(char *)((long)param_1 + 0x309) == '\0') || (uVar9 != 0)) {
                    /* try { // try from 00bc1fa8 to 00cc1fd3 has its CatchHandler @ 00bc8a90 */
            uVar6 = param_1[0x54] - param_1[0x53] >> 3;
            if ((uVar9 < uVar6) &&
               ((plVar15 = *(long **)(param_1[0x53] + uVar9 * 8), plVar15 != (long *)0x0 &&
                (uVar13 < (ulong)(plVar15[1] - *plVar15 >> 3))))) {
              return *(undefined8 **)(*plVar15 + uVar13 * 8);
            }
            if (uVar6 < uVar9) {
              return (undefined8 *)0x0;
            }
            if (param_1[0x62] == uVar9) {
              if (uVar9 == uVar6) {
                local_48 = 0;
                FUN_00bc2b00(param_1 + 0x53,&local_48);
              }
                    /* try { // try from 00bc2034 to 00cc203b has its CatchHandler @ 00bc88e0 */
              puVar4 = (undefined8 *)FUN_00bc2bd8(param_1,&DAT_002925bc);
              return puVar4;
            }
            return (undefined8 *)0x0;
          }
          pvVar14 = (void *)param_1[0x266];
          lVar7 = *(long *)((long)pvVar14 + 8);
          puVar4 = pvVar14;
          if (lVar7 - 0xfc0U < 0xfffffffffffff010) {
            puVar4 = malloc(0x1000);
            if (puVar4 == (void *)0x0) {
LAB_00bc2088:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar7 = 0;
            *puVar4 = pvVar14;
            puVar4[1] = 0;
            param_1[0x266] = (long)puVar4;
          }
          *(long *)((long)puVar4 + 8) = lVar7 + 0x30;
          puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
          *puVar12 = &PTR_FUN_00c17978;
          *(ulong *)((long)puVar4 + lVar7 + 0x20) = uVar13;
          *(undefined8 *)((long)puVar4 + lVar7 + 0x28) = 0;
          *(undefined1 *)((long)puVar4 + lVar7 + 0x30) = 0;
          *(ushort *)((long)puVar4 + lVar7 + 0x19) =
               *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0xa80;
          plVar15 = (long *)param_1[0x5b];
          plVar5 = (long *)param_1[0x5c];
          *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 0x2c;
          if (plVar15 == plVar5) {
            plVar5 = (long *)param_1[0x5a];
            __n = (long)plVar15 - (long)plVar5;
            if (plVar5 == param_1 + 0x5d) {
              pvVar14 = malloc(__n * 2);
              if (pvVar14 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
              if (plVar15 != plVar5) {
                memmove(pvVar14,plVar5,__n);
              }
              param_1[0x5a] = (long)pvVar14;
            }
            else {
              pvVar14 = realloc(plVar5,__n * 2);
              param_1[0x5a] = (long)pvVar14;
              if (pvVar14 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
            }
            plVar15 = (long *)((long)pvVar14 + __n);
            param_1[0x5c] = (long)((long)pvVar14 + ((long)__n >> 2) * 8);
          }
          param_1[0x5b] = (long)(plVar15 + 1);
          *plVar15 = (long)puVar12;
          return puVar12;
        }
        pvVar14 = (void *)param_1[0x266];
        lVar7 = *(long *)((long)pvVar14 + 8);
        puVar4 = pvVar14;
        if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
          puVar4 = malloc(0x1000);
          if (puVar4 == (void *)0x0) goto LAB_00bc2088;
          lVar7 = 0;
          *puVar4 = pvVar14;
          puVar4[1] = 0;
          param_1[0x266] = (long)puVar4;
        }
        *(long *)((long)puVar4 + 8) = lVar7 + 0x20;
        puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
        *puVar12 = &PTR_FUN_00c17898;
        *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 8;
        *(ushort *)((long)puVar4 + lVar7 + 0x19) =
             *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
        *(byte **)((long)puVar4 + lVar7 + 0x20) = pbVar1;
        *(long *)((long)puVar4 + lVar7 + 0x28) = (long)pbVar11 - (long)pbVar1;
        return puVar12;
                    /* try { // try from 00bc1e44 to 00cc1ec3 has its CatchHandler @ 00bc8b20 */
      }
    }
  }
  return (undefined8 *)0x0;
}

~~~
