# 00bd1eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bd1eec.md)

## 関数情報

~~~json
{
  "address": "00bd1eec",
  "name": "FUN_00bd1eec",
  "size": 700,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b39c05fe0ef35e70de5533c9adebed518cf726e7d1bcefb6afa13b3d0c33f637",
  "source_text_sha256": "b39c05fe0ef35e70de5533c9adebed518cf726e7d1bcefb6afa13b3d0c33f637"
}
~~~
## 呼び出し元

- [00bbdd50](../00bbd/00bbdd50.md)

## 呼び出し先

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc2e00](../00bc2/00bc2e00.md)
- [00bd38b4](../00bd3/00bd38b4.md)
- [00bd3954](../00bd3/00bd3954.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

## 疑似コード 1/1 / UTF-8 5919 bytes

~~~c

undefined8 * FUN_00bd1eec(long *param_1)

{
  byte *pbVar1;
  char *pcVar2;
  short *psVar3;
  char *pcVar4;
  byte *pbVar5;
  byte bVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  ushort uVar9;
  long lVar10;
  long lVar11;
  byte *pbVar12;
  long lVar13;
  byte *pbVar14;
  byte *pbVar15;
  void *pvVar16;
  long local_40;
  undefined8 *local_38;
  
  psVar3 = (short *)*param_1;
  pbVar5 = (byte *)param_1[1];
                    /* try { // try from 00bd1f20 to 00cd1f33 has its CatchHandler @ 00bd2840 */
  if (((ulong)((long)pbVar5 - (long)psVar3) < 2) || (*psVar3 != 0x7644)) {
LAB_00bd1f24:
    puVar7 = (undefined8 *)0x0;
  }
  else {
    pbVar1 = (byte *)(psVar3 + 1);
    *param_1 = (long)pbVar1;
    if ((pbVar5 == pbVar1) || (bVar6 = *pbVar1, bVar6 < 0x31)) {
LAB_00bd20d8:
      lVar13 = FUN_00bc2e00();
      if (lVar13 == 0) {
        return (undefined8 *)0x0;
      }
      pcVar4 = (char *)*param_1;
                    /* try { // try from 00bd20ec to 00cd20f3 has its CatchHandler @ 00bd2944 */
      if ((pcVar4 == (char *)param_1[1]) || (*pcVar4 != '_')) goto LAB_00bd1f24;
      *param_1 = (long)(pcVar4 + 1);
      lVar10 = FUN_00bbdd50(param_1);
      if (lVar10 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar16 = (void *)param_1[0x266];
                    /* try { // try from 00bd211c to 00cd2123 has its CatchHandler @ 00bd2934 */
      lVar11 = *(long *)((long)pvVar16 + 8);
      puVar8 = pvVar16;
      if (lVar11 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bd21a4:
                    /* WARNING: Subroutine does not return */
          std::terminate();
        }
        lVar11 = 0;
        *puVar8 = pvVar16;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
                    /* try { // try from 00bd2148 to 00cd214f has its CatchHandler @ 00bd2904 */
                    /* try { // try from 00bd2150 to 00cd216f has its CatchHandler @ 00bd2994 */
      *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
      puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
      *puVar7 = &PTR_FUN_00c19e78;
      uVar9 = *(ushort *)((long)puVar8 + lVar11 + 0x19);
      *(long *)((long)puVar8 + lVar11 + 0x20) = lVar10;
      *(long *)((long)puVar8 + lVar11 + 0x28) = lVar13;
    }
    else {
      if (bVar6 < 0x3a) {
        pbVar14 = (byte *)(psVar3 + 1);
        pbVar12 = pbVar1;
        do {
          pbVar15 = pbVar14;
          if (*pbVar12 - 0x3a < 0xfffffff6) break;
          pbVar12 = pbVar12 + 1;
                    /* try { // try from 00bd1f84 to 00cd1f8f has its CatchHandler @ 00bd29d8 */
          pbVar14 = pbVar14 + 1;
          *param_1 = (long)pbVar12;
          pbVar15 = pbVar5;
        } while (pbVar12 != pbVar5);
        pvVar16 = (void *)param_1[0x266];
        lVar13 = *(long *)((long)pvVar16 + 8);
        puVar7 = pvVar16;
        if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
          puVar7 = malloc(0x1000);
          if (puVar7 == (void *)0x0) goto LAB_00bd21a4;
          lVar13 = 0;
          *puVar7 = pvVar16;
          puVar7[1] = 0;
          param_1[0x266] = (long)puVar7;
        }
        *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
        local_38 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
        *local_38 = &PTR_FUN_00c17798;
        *(byte **)((long)puVar7 + lVar13 + 0x20) = pbVar1;
        *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 8;
                    /* try { // try from 00bd2008 to 00cd200f has its CatchHandler @ 00bd2864 */
        *(long *)((long)puVar7 + lVar13 + 0x28) = (long)pbVar15 - (long)pbVar1;
        *(ushort *)((long)puVar7 + lVar13 + 0x19) =
             *(ushort *)((long)puVar7 + lVar13 + 0x19) & 0xf000 | 0x540;
        pcVar4 = (char *)*param_1;
        if ((pcVar4 != (char *)param_1[1]) && (*pcVar4 == '_')) {
                    /* try { // try from 00bd202c to 00cd2033 has its CatchHandler @ 00bd2a04 */
          pcVar2 = pcVar4 + 1;
                    /* try { // try from 00bd2034 to 00cd2073 has its CatchHandler @ 00bd1b6c */
          *param_1 = (long)pcVar2;
          if ((pcVar2 != (char *)param_1[1]) && (*pcVar2 == 'p')) {
            *param_1 = (long)(pcVar4 + 2);
            puVar7 = (undefined8 *)FUN_00bd38b4(param_1,&local_38);
            return puVar7;
          }
          local_40 = FUN_00bbdd50();
          if (local_40 == 0) {
            return (undefined8 *)0x0;
          }
          puVar7 = (undefined8 *)FUN_00bd3954(param_1,&local_40,&local_38);
          return puVar7;
        }
        goto LAB_00bd1f24;
      }
      if (bVar6 != 0x5f) goto LAB_00bd20d8;
      *param_1 = (long)psVar3 + 3;
      lVar13 = FUN_00bbdd50();
      if (lVar13 == 0) {
        return (undefined8 *)0x0;
      }
                    /* try { // try from 00bd2074 to 00cd20c7 has its CatchHandler @ 00bd29ec */
      pvVar16 = (void *)param_1[0x266];
      lVar10 = *(long *)((long)pvVar16 + 8);
      puVar8 = pvVar16;
      if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bd21a4;
        lVar10 = 0;
        *puVar8 = pvVar16;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      *(long *)((long)puVar8 + 8) = lVar10 + 0x20;
      puVar7 = (undefined8 *)((long)puVar8 + lVar10 + 0x10);
      *puVar7 = &PTR_FUN_00c19e78;
      uVar9 = *(ushort *)((long)puVar8 + lVar10 + 0x19);
      *(long *)((long)puVar8 + lVar10 + 0x20) = lVar13;
      *(undefined8 *)((long)puVar8 + lVar10 + 0x28) = 0;
    }
    *(undefined1 *)(puVar7 + 1) = 0x1d;
    *(ushort *)((long)puVar7 + 9) = uVar9 & 0xf000 | 0x540;
  }
                    /* try { // try from 00bd1f38 to 00cd1f4b has its CatchHandler @ 00bd2860 */
  return puVar7;
}

~~~
