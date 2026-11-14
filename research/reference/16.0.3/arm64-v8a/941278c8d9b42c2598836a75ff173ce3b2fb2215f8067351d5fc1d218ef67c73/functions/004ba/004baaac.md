# 004baaac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004baaac",
  "name": "_ZN5BotanrsERKNS_6BigIntEm",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3604d2a6cfd92d5cade5852652548e4c2b671aae1946540add308241ad0b24f",
  "source_text_sha256": "e3604d2a6cfd92d5cade5852652548e4c2b671aae1946540add308241ad0b24f"
}
~~~

## 呼び出し元

- [00c59d80](../00c59/00c59d80.md)

## 呼び出し先

- [00c599c0](../00c59/00c599c0.md)
- [00c59be0](../00c59/00c59be0.md)
- [00c59cc0](../00c59/00c59cc0.md)

## 疑似コード / UTF-8 2923 bytes

~~~c

void _ZN5BotanrsERKNS_6BigIntEm(long *param_1,long *param_2,ulong param_3)

{
  uint uVar1;
  uint uVar2;
  undefined8 *puVar3;
  bool bVar4;
  ulong uVar5;
  long lVar6;
  undefined4 *puVar7;
  ulong uVar8;
  ulong uVar9;
  long lVar10;
  uint uVar11;
  undefined4 *puVar12;
  undefined8 *puVar13;
  long lVar14;
  undefined8 *puVar15;
  ulong uVar16;
  ulong uVar17;
  undefined8 uVar18;
  undefined8 uVar19;
  undefined8 uVar20;
  
  if (param_3 == 0) {
    _ZN5Botan6BigIntC2ERKS0_(param_1,param_2);
    return;
  }
  lVar6 = *param_2;
  lVar14 = param_2[1] - lVar6;
  uVar17 = lVar14 >> 2;
  uVar8 = uVar17;
  if (lVar14 != 0) {
    do {
      if (*(int *)(lVar6 + -4 + uVar8 * 4) != 0) goto LAB_004baaf8;
      uVar8 = uVar8 - 1;
    } while (uVar8 != 0);
LAB_004bac34:
    _ZN5Botan6BigIntC1Em(param_1,0);
    return;
  }
LAB_004baaf8:
  if (uVar8 == 0) goto LAB_004bac34;
  uVar8 = uVar8 - 1;
  if (uVar8 < uVar17) {
    uVar11 = *(uint *)(lVar6 + uVar8 * 4);
  }
  else {
    uVar11 = 0;
  }
  lVar14 = 0x20;
  do {
    if ((uVar11 >> (ulong)((int)lVar14 - 1U & 0x1f) & 1) != 0) break;
    lVar14 = lVar14 + -1;
  } while (lVar14 != 0);
  if (lVar14 + uVar8 * 0x20 <= param_3) goto LAB_004bac34;
  uVar8 = param_3 >> 5;
  if (param_2[1] != lVar6) {
    do {
      if (*(int *)(lVar6 + -4 + uVar17 * 4) != 0) break;
      uVar17 = uVar17 - 1;
    } while (uVar17 != 0);
  }
  _ZN5Botan6BigIntC1ENS0_4SignEm(param_1,(int)param_2[3],uVar17 - uVar8);
  uVar5 = uVar17 - uVar8;
  if (uVar17 < uVar8) {
    return;
  }
  if (uVar5 == 0) {
    return;
  }
  lVar6 = *param_1;
  lVar14 = *param_2;
  param_3 = param_3 & 0x1f;
  if ((uVar5 < 8) || (lVar10 = uVar8 * 4 + lVar14, (ulong)(lVar6 - lVar10) < 0x20)) {
    uVar9 = 0;
  }
  else {
    uVar9 = uVar5 & 0xfffffffffffffff8;
    puVar13 = (undefined8 *)(lVar10 + 0x10);
    puVar15 = (undefined8 *)(lVar6 + 0x10);
    uVar16 = uVar9;
    do {
      puVar3 = puVar13 + -1;
      uVar18 = puVar13[-2];
      uVar20 = puVar13[1];
      uVar19 = *puVar13;
      uVar16 = uVar16 - 8;
      puVar13 = puVar13 + 4;
      puVar15[-1] = *puVar3;
      puVar15[-2] = uVar18;
      puVar15[1] = uVar20;
      *puVar15 = uVar19;
      puVar15 = puVar15 + 4;
    } while (uVar16 != 0);
    if (uVar5 == uVar9) goto LAB_004babec;
  }
  lVar10 = (uVar9 + uVar8) - uVar17;
  puVar7 = (undefined4 *)(lVar14 + uVar9 * 4 + uVar8 * 4);
  puVar12 = (undefined4 *)(lVar6 + uVar9 * 4);
  do {
    bVar4 = lVar10 != -1;
    lVar10 = lVar10 + 1;
    *puVar12 = *puVar7;
    puVar7 = puVar7 + 1;
    puVar12 = puVar12 + 1;
  } while (bVar4);
LAB_004babec:
  if (param_3 != 0) {
    uVar11 = 0;
    do {
      lVar14 = uVar5 * 4;
      uVar5 = uVar5 - 1;
      uVar1 = *(uint *)(lVar6 + -4 + lVar14);
      uVar2 = uVar1 >> param_3 | uVar11;
      uVar11 = uVar1 << (ulong)(0x20U - (int)param_3 & 0x1f);
      *(uint *)(lVar6 + -4 + lVar14) = uVar2;
    } while (uVar5 != 0);
  }
  return;
}

~~~
