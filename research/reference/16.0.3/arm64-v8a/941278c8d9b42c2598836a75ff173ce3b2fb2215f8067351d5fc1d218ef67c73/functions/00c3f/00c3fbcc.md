# 00c3fbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00c3fbcc",
  "name": "FUN_00c3fbcc",
  "size": 964,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da9bc0e923ed3b2346e92f901d15e1c04c1f5b669ecb0e3729e2078d9ba52ce7",
  "source_text_sha256": "da9bc0e923ed3b2346e92f901d15e1c04c1f5b669ecb0e3729e2078d9ba52ce7"
}
~~~

## 呼び出し元

- [00c3bd5c](../00c3b/00c3bd5c.md)
- [00c3d29c](../00c3d/00c3d29c.md)
- [00c40e0c](../00c40/00c40e0c.md)
- [00c4c6b8](../00c4c/00c4c6b8.md)

## 呼び出し先

- [00c40a00](../00c40/00c40a00.md)
- [00c40ad8](../00c40/00c40ad8.md)
- [00c58fe0](../00c58/00c58fe0.md)
- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)
- [00c5b140](../00c5b/00c5b140.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

## 関連文字列（未確認候補）

~~~text
"auto"
~~~

## 疑似コード / UTF-8 6693 bytes

~~~c

undefined8 * FUN_00c3fbcc(long *param_1)

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
  
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  if ((pbVar1 != pbVar2) && (*pbVar1 == 0x54)) {
                    /* try { // try from 00c3fc00 to 00d3fca7 has its CatchHandler @ 00c4052c */
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
                    /* try { // try from 00c3fca8 to 00d3fcb3 has its CatchHandler @ 00c40510 */
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
                FUN_00c40a00(param_1 + 0x53,&local_48);
                    /* try { // try from 00c3ff10 to 00d3ff1f has its CatchHandler @ 00c40484 */
              }
              puVar4 = (undefined8 *)FUN_00c40ad8(param_1,&DAT_002a1d8c);
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
LAB_00c3ff88:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar7 = 0;
            *puVar4 = pvVar14;
            puVar4[1] = 0;
                    /* try { // try from 00c3fe1c to 00d3ff0f has its CatchHandler @ 00c4049c */
            param_1[0x266] = (long)puVar4;
          }
          *(long *)((long)puVar4 + 8) = lVar7 + 0x30;
          puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
          *puVar12 = &PTR_FUN_00c987c0;
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
          if (puVar4 == (void *)0x0) goto LAB_00c3ff88;
          lVar7 = 0;
          *puVar4 = pvVar14;
          puVar4[1] = 0;
          param_1[0x266] = (long)puVar4;
        }
        *(long *)((long)puVar4 + 8) = lVar7 + 0x20;
                    /* try { // try from 00c3fd1c to 00d3fdc7 has its CatchHandler @ 00c40540 */
        puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
        *puVar12 = &PTR_FUN_00c986e0;
        *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 8;
        *(ushort *)((long)puVar4 + lVar7 + 0x19) =
             *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
        *(byte **)((long)puVar4 + lVar7 + 0x20) = pbVar1;
        *(long *)((long)puVar4 + lVar7 + 0x28) = (long)pbVar11 - (long)pbVar1;
        return puVar12;
      }
    }
  }
  return (undefined8 *)0x0;
}

~~~
