# 00bcebe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcebe0.md)

## 関数情報

~~~json
{
  "address": "00bcebe0",
  "name": "FUN_00bcebe0",
  "size": 884,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b529b027cc2b372cc35769c166d1ca248080110866e02c8ac1627b93ee7a426",
  "source_text_sha256": "1b529b027cc2b372cc35769c166d1ca248080110866e02c8ac1627b93ee7a426"
}
~~~
## 呼び出し元

- [00bc2394](../00bc2/00bc2394.md)
- [00bce830](../00bce/00bce830.md)

## 呼び出し先

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc1034](../00bc1/00bc1034.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 関連文字列（未確認候補）

~~~text
"operator-="
~~~
## 疑似コード 1/1 / UTF-8 7661 bytes

~~~c

undefined8 * FUN_00bcebe0(long *param_1,undefined1 *param_2)

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
      if ((byte)(&UNK_00c178d8)[uVar16 * 0x10] < bVar4) {
        uVar14 = uVar16 + 1;
        uVar16 = uVar15;
      }
      else {
                    /* try { // try from 00bcec54 to 00ccec5f has its CatchHandler @ 00bcf270 */
        if (((&UNK_00c178d8)[uVar16 * 0x10] == bVar4) &&
           ((byte)(&UNK_00c178d9)[uVar16 * 0x10] < pbVar2[1])) {
          uVar14 = uVar16 + 1;
          uVar16 = uVar15;
        }
      }
      uVar15 = uVar16;
    } while (uVar16 != uVar14);
    lVar11 = uVar14 * 0x10;
                    /* try { // try from 00bcec7c to 00ccec8b has its CatchHandler @ 00bcf26c */
                    /* try { // try from 00bcec8c to 00ccec97 has its CatchHandler @ 00bcf258 */
    if (((&UNK_00c178d8)[lVar11] == bVar4) && ((&UNK_00c178d9)[lVar11] == pbVar2[1])) {
      bVar4 = (&UNK_00c178da)[lVar11];
                    /* try { // try from 00bcec98 to 00ccecab has its CatchHandler @ 00bcf248 */
      *param_1 = (long)(pbVar2 + 2);
      if (bVar4 == 8) {
        uVar5 = *(undefined1 *)((long)param_1 + 0x309);
                    /* try { // try from 00bcecac to 00ccecb7 has its CatchHandler @ 00bcf218 */
        lVar11 = param_1[0x61];
        *(undefined1 *)(param_1 + 0x61) = 0;
        uVar12 = uVar5;
                    /* try { // try from 00bcecb8 to 00ccecc7 has its CatchHandler @ 00bcf1f8 */
        if (param_2 != (undefined1 *)0x0) {
          uVar12 = 1;
        }
        *(undefined1 *)((long)param_1 + 0x309) = uVar12;
        lVar6 = FUN_00bbdd50();
                    /* try { // try from 00bcecc8 to 00ccecdf has its CatchHandler @ 00bcf1b4 */
        if (lVar6 == 0) {
          puVar8 = (undefined8 *)0x0;
        }
        else {
          if (param_2 != (undefined1 *)0x0) {
            *param_2 = 1;
          }
                    /* try { // try from 00bcece0 to 00cced47 has its CatchHandler @ 00bce4cc */
          pvVar17 = (void *)param_1[0x266];
          lVar13 = *(long *)((long)pvVar17 + 8);
          puVar7 = pvVar17;
          if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
            puVar7 = malloc(0x1000);
            if (puVar7 == (void *)0x0) goto LAB_00bcef50;
            lVar13 = 0;
            *puVar7 = pvVar17;
            puVar7[1] = 0;
            param_1[0x266] = (long)puVar7;
          }
          *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
          puVar8 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
          *puVar8 = &PTR_FUN_00c19078;
          *(long *)((long)puVar7 + lVar13 + 0x20) = lVar6;
          *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 4;
                    /* try { // try from 00bced48 to 00cced87 has its CatchHandler @ 00bcf2fc */
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
      if ((bVar4 == 4) && (((&UNK_00c178db)[lVar11] & 1) == 0)) {
        return (undefined8 *)0x0;
      }
      __s = *(char **)(&UNK_00c178e0 + lVar11);
                    /* try { // try from 00bceebc to 00cceef3 has its CatchHandler @ 00bcf148 */
      sVar9 = strlen(__s);
      pvVar17 = (void *)param_1[0x266];
      lVar11 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (0xfffffffffffff00f < lVar11 - 0xfd0U) {
LAB_00bcef00:
                    /* try { // try from 00bcef00 to 00ccef0f has its CatchHandler @ 00bcf140 */
                    /* try { // try from 00bcef10 to 00ccef27 has its CatchHandler @ 00bcf13c */
        *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
        puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
        *puVar7 = &PTR_FUN_00c17798;
        *(char **)((long)puVar8 + lVar11 + 0x20) = __s;
        *(size_t *)((long)puVar8 + lVar11 + 0x28) = sVar9;
                    /* try { // try from 00bcef28 to 00ccf35f has its CatchHandler @ 00bce4cc */
        *(undefined1 *)((long)puVar8 + lVar11 + 0x18) = 8;
        *(ushort *)((long)puVar8 + lVar11 + 0x19) =
             *(ushort *)((long)puVar8 + lVar11 + 0x19) & 0xf000 | 0x540;
        return puVar7;
      }
      puVar8 = malloc(0x1000);
      if (puVar8 != (void *)0x0) {
        lVar11 = 0;
                    /* try { // try from 00bceef4 to 00cceeff has its CatchHandler @ 00bcf144 */
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
        goto LAB_00bcef00;
      }
      goto LAB_00bcef50;
    }
    if (*(short *)pbVar2 == 0x696c) {
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1034();
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bcef50;
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c190e8;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 0x14;
      goto LAB_00bcee60;
    }
  }
  if ((pbVar2 != pbVar3) && (*pbVar2 == 0x76)) {
    pbVar1 = pbVar2 + 1;
    *param_1 = (long)pbVar1;
                    /* try { // try from 00bced88 to 00cced93 has its CatchHandler @ 00bcf1a0 */
    if ((pbVar3 != pbVar1) && (*pbVar1 - 0x30 < 10)) {
                    /* try { // try from 00bced94 to 00cceda3 has its CatchHandler @ 00bcf180 */
      *param_1 = (long)(pbVar2 + 2);
      lVar11 = FUN_00bc1034();
                    /* try { // try from 00bceda4 to 00ccedbb has its CatchHandler @ 00bcf14c */
      if (lVar11 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar17 = (void *)param_1[0x266];
      lVar6 = *(long *)((long)pvVar17 + 8);
                    /* try { // try from 00bcedbc to 00cceebb has its CatchHandler @ 00bce4cc */
      puVar8 = pvVar17;
      if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bcef50:
                    /* WARNING: Subroutine does not return */
          std::terminate();
        }
        lVar6 = 0;
        *puVar8 = pvVar17;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      lVar13 = (long)puVar8 + lVar6;
      ppuVar10 = &PTR_FUN_00c19078;
      *(long *)((long)puVar8 + 8) = lVar6 + 0x20;
      uVar12 = 4;
LAB_00bcee60:
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
