# 00bcecec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bcebe0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bce/00bcebe0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bcecec",
  "name": "FUN_00bcecec",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ae0b729de4a58a7f5f191206cab98233d4a29434281ea9ffcc1e956e642c6b6",
  "source_text_sha256": "7ae0b729de4a58a7f5f191206cab98233d4a29434281ea9ffcc1e956e642c6b6"
}
~~~

## 呼び出し元

- [00bc24a0](../00bc2/00bc24a0.md)
- [00bce93c](../00bce/00bce93c.md)

## 呼び出し先

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bc1140](../00bc1/00bc1140.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~

## 疑似コード / UTF-8 7460 bytes

~~~c

undefined8 * FUN_00bcecec(long *param_1,undefined1 *param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  byte bVar4;
  undefined1 uVar5;
  long lVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  size_t sVar9;
  undefined **ppuVar10;
  long lVar11;
  undefined1 uVar12;
  long lVar13;
  ulong uVar14;
  ulong uVar15;
  ulong uVar16;
  char *__s;
  void *pvVar17;
  
  pbVar2 = (byte *)*param_1;
  pbVar3 = (byte *)param_1[1];
  if (1 < (ulong)((long)pbVar3 - (long)pbVar2)) {
    bVar4 = *pbVar2;
    uVar14 = 0;
    uVar15 = 0x3d;
    do {
      uVar16 = uVar14 + uVar15 >> 1;
      if ((byte)(&UNK_00c179d8)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else {
                    /* try { // try from 00bced60 to 00cced6b has its CatchHandler @ 00bcf37c */
        if (((&UNK_00c179d8)[uVar16 * 0x10] == bVar4) &&
           ((byte)(&UNK_00c179d9)[uVar16 * 0x10] < pbVar2[1])) {
          uVar14 = uVar16 + 1;
          uVar16 = uVar15;
        }
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
                    /* try { // try from 00bced88 to 00cced97 has its CatchHandler @ 00bcf378 */
                    /* try { // try from 00bced98 to 00cceda3 has its CatchHandler @ 00bcf364 */
    if (((&UNK_00c179d8)[lVar11] == bVar4) && ((&UNK_00c179d9)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c179da)[lVar11];
                    /* try { // try from 00bceda4 to 00ccedb7 has its CatchHandler @ 00bcf354 */
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
                    /* try { // try from 00bcedb8 to 00ccedc3 has its CatchHandler @ 00bcf324 */
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
                    /* try { // try from 00bcedc4 to 00ccedd3 has its CatchHandler @ 00bcf304 */
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00bbde5c();
                    /* try { // try from 00bcedd4 to 00ccedeb has its CatchHandler @ 00bcf2c0 */
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
                    /* try { // try from 00bcedec to 00ccee53 has its CatchHandler @ 00bce5d8 */
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00bcf05c;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c19178;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
                    /* try { // try from 00bcee54 to 00ccee93 has its CatchHandler @ 00bcf408 */
          *(ushort *)((long)puVar7 + lVar13 + 0x19) =
               *(ushort *)((long)puVar7 + lVar13 + 0x19) & 0xf000 | 0x540;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar5;
        *(char *)(param_1 + 0x61) = (char)lVar11;
        return puVar8;
      }
      if (10 < bVar4) {
        return (undefined8 *)0x0;
      }
      if ((bVar4 == 4) && (((&UNK_00c179db)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c179e0 + lVar11);
                    /* try { // try from 00bcefc8 to 00ccefff has its CatchHandler @ 00bcf254 */
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00bcf00c:
                    /* try { // try from 00bcf00c to 00ccf01b has its CatchHandler @ 00bcf24c */
                    /* try { // try from 00bcf01c to 00ccf033 has its CatchHandler @ 00bcf248 */
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c17898;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
                    /* try { // try from 00bcf034 to 00ccf46b has its CatchHandler @ 00bce5d8 */
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
                    /* try { // try from 00bcf000 to 00ccf00b has its CatchHandler @ 00bcf250 */
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00bcf00c;
      }
      goto LAB_00bcf05c;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1140();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bcf05c;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c191e8;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00bcef6c;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
                    /* try { // try from 00bcee94 to 00ccee9f has its CatchHandler @ 00bcf2ac */
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
                    /* try { // try from 00bceea0 to 00cceeaf has its CatchHandler @ 00bcf28c */
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1140();
                    /* try { // try from 00bceeb0 to 00cceec7 has its CatchHandler @ 00bcf258 */
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
                    /* try { // try from 00bceec8 to 00ccefc7 has its CatchHandler @ 00bce5d8 */
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bcf05c:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19178;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00bcef6c:
      *(undefined8 *)(lVar13 + 0x10) = ppuVar10;
      *(undefined1 *)(lVar13 + 0x18) = uVar12;
      *(long *)(lVar13 + 0x20) = lVar11;
      *(ushort *)(lVar13 + 0x19) = *(ushort *)(lVar13 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar13 + 0x10);
    }
  }
  return (undefined8 *)0x0;
}

~~~
