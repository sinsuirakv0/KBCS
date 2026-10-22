# 00bbd1fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbd1fc.md)

## 関数情報

~~~json
{
  "address": "00bbd1fc",
  "name": "FUN_00bbd1fc",
  "size": 2524,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4297530d908b2894a9a7a49af1529706f5f0132d0d928d73caec3582efa8a0f",
  "source_text_sha256": "b4297530d908b2894a9a7a49af1529706f5f0132d0d928d73caec3582efa8a0f"
}
~~~
## 呼び出し元

- [00bbcb04](../00bbc/00bbcb04.md)
- [00bbd1fc](../00bbd/00bbd1fc.md)
- [00bbf290](../00bbf/00bbf290.md)
- [00bbf9c4](../00bbf/00bbf9c4.md)
- [00bc47d4](../00bc4/00bc47d4.md)

## 呼び出し先

- [00bbb090](../00bbb/00bbb090.md)
- [00bbd1fc](../00bbd/00bbd1fc.md)
- [00bbdc10](../00bbd/00bbdc10.md)
- [00bbdc9c](../00bbd/00bbdc9c.md)
- [00bbdd50](../00bbd/00bbdd50.md)
- [00bbf0e8](../00bbf/00bbf0e8.md)
- [00bbf290](../00bbf/00bbf290.md)
- [00bbf9c4](../00bbf/00bbf9c4.md)
- [00bbfdc4](../00bbf/00bbfdc4.md)
- [00bbfe64](../00bbf/00bbfe64.md)
- [00bbffc0](../00bbf/00bbffc0.md)
- [00bc00b4](../00bc0/00bc00b4.md)
- [00bc0294](../00bc0/00bc0294.md)
- [00bc0344](../00bc0/00bc0344.md)
- [00bc03f4](../00bc0/00bc03f4.md)
- [00bc04a4](../00bc0/00bc04a4.md)
- [00bc0554](../00bc0/00bc0554.md)
- [00bc0604](../00bc0/00bc0604.md)
- [00bc07b4](../00bc0/00bc07b4.md)
- [00bc0864](../00bc0/00bc0864.md)
- [00bc090c](../00bc0/00bc090c.md)
- [00bc09bc](../00bc0/00bc09bc.md)
- [00bc0a6c](../00bc0/00bc0a6c.md)
- [00bc0b18](../00bc0/00bc0b18.md)
- [00bc0bc8](../00bc0/00bc0bc8.md)
- [00bc2e00](../00bc2/00bc2e00.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"guard variable for "
"initializer for module "
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
"shrinkToSize() can't expand!"
"thread-local wrapper routine for "
~~~
## 疑似コード 1/2 / UTF-8 24572 bytes

~~~c

undefined8 * FUN_00bbd1fc(long *param_1)

{
  char cVar1;
  undefined1 uVar2;
  uint uVar3;
  undefined1 auVar4 [16];
  undefined1 auVar5 [16];
  undefined1 auVar6 [16];
  undefined1 auVar7 [16];
  undefined1 auVar8 [16];
  undefined1 auVar9 [16];
  undefined1 auVar10 [16];
  bool bVar11;
  ulong uVar12;
  undefined8 *puVar13;
  undefined8 *puVar14;
  long *plVar15;
  long extraout_x1;
  long lVar16;
  long lVar17;
  byte *pbVar18;
  char *pcVar19;
  char *pcVar20;
  byte *pbVar21;
  ushort uVar22;
  byte bVar23;
  undefined8 *puVar24;
  undefined8 uVar25;
  long lVar26;
  long *plVar27;
  ulong uVar28;
  ulong uVar29;
  void *pvVar30;
  size_t sVar31;
  long *plVar32;
  undefined1 auVar33 [16];
  long local_150;
  long local_148;
  undefined1 local_140 [16];
  undefined8 local_130;
  undefined8 *local_128;
  undefined8 local_120;
  undefined1 local_118 [8];
  ulong local_110;
  char local_108;
  undefined1 auStack_100 [160];
  
                    /* catch() { ... } // from try @ 00bbcfb0 with catch @ 00bbd200
                       catch() { ... } // from try @ 00bbcfe8 with catch @ 00bbd200 */
                    /* catch() { ... } // from try @ 00bbc86c with catch @ 00bbd204 */
                    /* catch() { ... } // from try @ 00bbc724 with catch @ 00bbd208 */
                    /* catch() { ... } // from try @ 00bbc3bc with catch @ 00bbd20c */
                    /* catch() { ... } // from try @ 00bbcc9c with catch @ 00bbd21c */
                    /* catch() { ... } // from try @ 00bbba8c with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbbbf0 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbbca4 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbbdb0 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbbfe8 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbc164 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbc488 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbc598 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbc644 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbcaa4 with catch @ 00bbd220
                       catch() { ... } // from try @ 00bbcdc0 with catch @ 00bbd220 */
                    /* catch() { ... } // from try @ 00bbcf4c with catch @ 00bbd224
                       catch() { ... } // from try @ 00bbcf98 with catch @ 00bbd224 */
                    /* catch() { ... } // from try @ 00bbcf30 with catch @ 00bbd228
                       catch() { ... } // from try @ 00bbcf80 with catch @ 00bbd228 */
                    /* catch() { ... } // from try @ 00bbcf14 with catch @ 00bbd22c
                       catch() { ... } // from try @ 00bbcf68 with catch @ 00bbd22c */
  FUN_00bbf0e8(auStack_100,param_1);
  auVar8._8_8_ = local_140._8_8_;
  auVar8._0_8_ = local_140._0_8_;
  auVar33._8_8_ = local_140._8_8_;
  auVar33._0_8_ = local_140._0_8_;
                    /* catch() { ... } // from try @ 00bbc374 with catch @ 00bbd230 */
  pcVar19 = (char *)*param_1;
  pcVar20 = (char *)param_1[1];
  if (pcVar20 == pcVar19) {
LAB_00bbd2c4:
                    /* catch() { ... } // from try @ 00bbbe2c with catch @ 00bbd2c4 */
                    /* catch() { ... } // from try @ 00bbb98c with catch @ 00bbd2c8 */
                    /* catch() { ... } // from try @ 00bbcbe0 with catch @ 00bbd2cc */
                    /* catch() { ... } // from try @ 00bbcb38 with catch @ 00bbd2d0 */
                    /* catch() { ... } // from try @ 00bbc830 with catch @ 00bbd2d4 */
                    /* catch() { ... } // from try @ 00bbcb2c with catch @ 00bbd2d8
                       catch() { ... } // from try @ 00bbcc8c with catch @ 00bbd2d8 */
    local_120 = (local_120 >> 0x10 & 0xffff) << 0x10;
                    /* catch() { ... } // from try @ 00bbc930 with catch @ 00bbd2dc */
    local_110 = param_1[0x5b] - param_1[0x5a] >> 3;
                    /* catch() { ... } // from try @ 00bbc6c8 with catch @ 00bbd2e0 */
    local_118[0] = 0;
                    /* catch() { ... } // from try @ 00bbc324 with catch @ 00bbd2e4 */
    local_108 = '\0';
    puVar13 = (undefined8 *)FUN_00bbf290(param_1,&local_120);
    auVar33._8_8_ = local_140._8_8_;
    auVar33._0_8_ = local_140._0_8_;
    auVar4._8_8_ = local_140._8_8_;
    auVar4._0_8_ = local_140._0_8_;
    local_128 = puVar13;
    if (puVar13 == (undefined8 *)0x0) goto LAB_00bbdb48;
    lVar16 = param_1[0x5a];
                    /* catch() { ... } // from try @ 00bbb998 with catch @ 00bbd314 */
    uVar12 = param_1[0x5b] - lVar16 >> 3;
                    /* catch() { ... } // from try @ 00bbc50c with catch @ 00bbd318 */
                    /* catch() { ... } // from try @ 00bbc98c with catch @ 00bbd31c */
    if (local_110 < uVar12) {
                    /* catch() { ... } // from try @ 00bbbfc4 with catch @ 00bbd320 */
      puVar24 = (undefined8 *)param_1[0x53];
                    /* catch() { ... } // from try @ 00bbbbcc with catch @ 00bbd324 */
      if ((puVar24 != (undefined8 *)param_1[0x54]) &&
         (plVar27 = (long *)*puVar24, plVar27 != (long *)0x0)) {
        lVar26 = *(long *)(lVar16 + local_110 * 8);
        lVar17 = *plVar27;
        uVar28 = *(ulong *)(lVar26 + 0x10);
        uVar29 = local_110;
        if (uVar28 < (ulong)(plVar27[1] - lVar17 >> 3)) {
          do {
            uVar29 = uVar29 + 1;
                    /* try { // try from 00bbd358 to 00cbd3db has its CatchHandler @ 00bbd358
                       catch() { ... } // from try @ 00bbd358 with catch @ 00bbd358
                       catch() { ... } // from try @ 00bbde28 with catch @ 00bbd358 */
            *(undefined8 *)(lVar26 + 0x18) = *(undefined8 *)(lVar17 + uVar28 * 8);
            if (uVar12 == uVar29) goto LAB_00bbd450;
            plVar27 = (long *)*puVar24;
            if (plVar27 == (long *)0x0) break;
            lVar26 = *(long *)(lVar16 + uVar29 * 8);
            lVar17 = *plVar27;
            uVar28 = *(ulong *)(lVar26 + 0x10);
          } while (uVar28 < (ulong)(plVar27[1] - lVar17 >> 3));
          if (uVar12 <= uVar29) goto LAB_00bbd458;
        }
      }
    }
    else {
                    /* try { // try from 00bbd448 to 00cbd453 has its CatchHandler @ 00bbe07c */
      if (uVar12 < local_110) {
                    /* try { // try from 00bbdbac to 00cbdbb7 has its CatchHandler @ 00bbe084 */
                    /* try { // try from 00bbdbb8 to 00cbdbc7 has its CatchHandler @ 00bbe080 */
                    /* WARNING: Subroutine does not return */
        FUN_00bbb090("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0x87,
                     "shrinkToSize() can\'t expand!");
      }
LAB_00bbd450:
                    /* try { // try from 00bbd454 to 00cbd497 has its CatchHandler @ 00bbe088 */
      param_1[0x5b] = lVar16 + local_110 * 8;
LAB_00bbd458:
      pbVar18 = (byte *)*param_1;
      pbVar21 = (byte *)param_1[1];
      local_140 = auVar4;
      if ((pbVar21 == pbVar18) ||
         ((local_140 = auVar33, *pbVar18 - 0x2e < 0x32 &&
          ((1L << ((ulong)(*pbVar18 - 0x2e) & 0x3f) & 0x2000000800001U) != 0)))) goto LAB_00bbdb48;
      local_130 = 0;
                    /* try { // try from 00bbd4bc to 00cbd4c7 has its CatchHandler @ 00bbe07c */
                    /* try { // try from 00bbd4c8 to 00cbd50b has its CatchHandler @ 00bbe088 */
      if (((ulong)((long)pbVar21 - (long)pbVar18) < 0xd) ||
         (*(long *)pbVar18 != 0x6c62616e65396155 || *(long *)(pbVar18 + 5) != 0x4966695f656c6261)) {
LAB_00bbd4d0:
        local_148 = 0;
        if (((local_120 & 1) == 0) && (local_120._1_1_ != '\0')) {
          local_148 = FUN_00bbdd50(param_1);
          auVar33 = local_140;
          if (local_148 == 0) goto LAB_00bbdb44;
        }
        pcVar19 = (char *)*param_1;
        pcVar20 = (char *)param_1[1];
        local_140._0_8_ = 0;
        local_140._8_8_ = 0;
        auVar33 = ZEXT816(0);
        if ((pcVar19 == pcVar20) || (*pcVar19 != 'v')) {
          lVar16 = param_1[2];
          lVar17 = param_1[3];
          plVar27 = param_1 + 5;
          do {
            puVar13 = (undefined8 *)FUN_00bbdd50(param_1);
            auVar33._8_8_ = local_140._8_8_;
            auVar33._0_8_ = local_140._0_8_;
            if (puVar13 == (undefined8 *)0x0) goto LAB_00bbdb44;
                    /* try { // try from 00bbd804 to 00cbd80f has its CatchHandler @ 00bbdeec */
            plVar32 = (long *)param_1[3];
            puVar24 = puVar13;
                    /* try { // try from 00bbd810 to 00cbd853 has its CatchHandler @ 00bbdfb8 */
            if ((local_108 != '\0') && (lVar17 - lVar16 == (long)plVar32 - param_1[2])) {
              pvVar30 = (void *)param_1[0x266];
              lVar26 = *(long *)((long)pvVar30 + 8);
              puVar14 = pvVar30;
              if (lVar26 - 0xfd0U < 0xfffffffffffff010) {
                puVar14 = malloc(0x1000);
                if (puVar14 == (void *)0x0) goto LAB_00bbdbc4;
                lVar26 = 0;
                *puVar14 = pvVar30;
                puVar14[1] = 0;
                param_1[0x266] = (long)puVar14;
              }
              *(long *)((long)puVar14 + 8) = lVar26 + 0x20;
              puVar24 = (undefined8 *)((long)puVar14 + lVar26 + 0x10);
              *puVar24 = &PTR_FUN_00c19858;
              *(undefined1 *)((long)puVar14 + lVar26 + 0x18) = 0x57;
                    /* try { // try from 00bbd878 to 00cbd87f has its CatchHandler @ 00bbe08c */
              *(undefined8 **)((long)puVar14 + lVar26 + 0x20) = puVar13;
              *(ushort *)((long)puVar14 + lVar26 + 0x19) =
                   *(ushort *)((long)puVar14 + lVar26 + 0x19) & 0xf000 | 0x540;
              plVar32 = (long *)param_1[3];
            }
            if (plVar32 == (long *)param_1[4]) {
              plVar15 = (long *)param_1[2];
              sVar31 = (long)plVar32 - (long)plVar15;
              if (plVar15 == plVar27) {
                pvVar30 = malloc(sVar31 * 2);
                    /* try { // try from 00bbd8c4 to 00cbd8d3 has its CatchHandler @ 00bbdfa0 */
                if (pvVar30 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                  abort();
                }
                if (plVar32 != plVar27) {
                    /* try { // try from 00bbd8d4 to 00cbd8e7 has its CatchHandler @ 00bbdf88 */
                  memcpy(pvVar30,plVar27,sVar31);
                }
                param_1[2] = (long)pvVar30;
              }
              else {
                pvVar30 = realloc(plVar15,sVar31 * 2);
                param_1[2] = (long)pvVar30;
                if (pvVar30 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                  abort();
                }
              }
              plVar32 = (long *)((long)pvVar30 + sVar31);
              param_1[3] = (long)plVar32;
              param_1[4] = (long)((long)pvVar30 + ((long)sVar31 >> 2) * 8);
            }
            param_1[3] = (long)(plVar32 + 1);
            *plVar32 = (long)puVar24;
          } while (((byte *)param_1[1] != (byte *)*param_1) &&
                  ((uVar3 = *(byte *)*param_1 - 0x2e, 0x31 < uVar3 ||
                   ((1L << ((ulong)uVar3 & 0x3f) & 0x2000800800001U) == 0))));
          auVar33 = FUN_00bbfe64(param_1,lVar17 - lVar16 >> 3);
          pcVar19 = (char *)*param_1;
          pcVar20 = (char *)param_1[1];
        }
        else {
          pcVar19 = pcVar19 + 1;
          *param_1 = (long)pcVar19;
        }
        local_150 = 0;
        local_140 = auVar33;
                    /* try { // try from 00bbd950 to 00cbd95b has its CatchHandler @ 00bbdee8 */
        if ((pcVar19 != pcVar20) && (*pcVar19 == 'Q')) {
          uVar2 = *(undefined1 *)((long)param_1 + 0x30a);
                    /* try { // try from 00bbd95c to 00cbd99f has its CatchHandler @ 00bbdf84 */
          *param_1 = (long)(pcVar19 + 1);
          *(undefined1 *)((long)param_1 + 0x30a) = 1;
          local_150 = FUN_00bc2e00(param_1);
          *(undefined1 *)((long)param_1 + 0x30a) = uVar2;
          auVar33 = local_140;
          if (local_150 == 0) goto LAB_00bbdb44;
        }
        puVar13 = (undefined8 *)
                  FUN_00bbffc0(param_1,&local_148,&local_128,local_140,&local_130,&local_150,
                               (ulong)&local_120 | 4,local_118);
        goto LAB_00bbdb48;
      }
      lVar16 = param_1[2];
      lVar17 = param_1[3];
      pbVar18 = pbVar18 + 0xd;
      plVar27 = param_1 + 5;
      *param_1 = (long)pbVar18;
                    /* try { // try from 00bbda98 to 00cbdaa3 has its CatchHandler @ 00bbe08c */
      while( true ) {
                    /* try { // try from 00bbdad8 to 00cbdadf has its CatchHandler @ 00bbe08c */
        if ((pbVar18 != pbVar21) && (*pbVar18 == 0x45)) {
          *param_1 = (long)(pbVar18 + 1);
          local_140 = FUN_00bbfe64(param_1,lVar17 - lVar16 >> 3);
          local_130 = FUN_00bbfdc4(param_1,local_140);
          goto LAB_00bbd4d0;
        }
        lVar26 = FUN_00bbf9c4(param_1);
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
        if (lVar26 == 0) break;
        plVar32 = (long *)param_1[3];
        if (plVar32 == (long *)param_1[4]) {
          plVar15 = (long *)param_1[2];
          sVar31 = (long)plVar32 - (long)plVar15;
          if (plVar15 == plVar27) {
                    /* try { // try from 00bbdb14 to 00cbdb1f has its CatchHandler @ 00bbdf50 */
            pvVar30 = malloc(sVar31 * 2);
            if (pvVar30 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
                    /* try { // try from 00bbdb20 to 00cbdb2f has its CatchHandler @ 00bbdf3c */
            if (plVar32 != plVar27) {
                    /* try { // try from 00bbdb30 to 00cbdb43 has its CatchHandler @ 00bbdf24 */
              memcpy(pvVar30,plVar27,sVar31);
            }
            param_1[2] = (long)pvVar30;
          }
          else {
            pvVar30 = realloc(plVar15,sVar31 * 2);
                    /* try { // try from 00bbdaa4 to 00cbdab3 has its CatchHandler @ 00bbdee4 */
            param_1[2] = (long)pvVar30;
            if (pvVar30 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
          }
          plVar32 = (long *)((long)pvVar30 + sVar31);
          param_1[3] = (long)plVar32;
          param_1[4] = (long)((long)pvVar30 + ((long)sVar31 >> 2) * 8);
        }
        param_1[3] = (long)(plVar32 + 1);
        *plVar32 = lVar26;
        pbVar18 = (byte *)*param_1;
        pbVar21 = (byte *)param_1[1];
      }
    }
  }
  else if (*pcVar19 == 'G') {
    if (1 < (ulong)((long)pcVar20 - (long)pcVar19)) {
      cVar1 = pcVar19[1];
      if (cVar1 == 'I') {
        *param_1 = (long)(pcVar19 + 2);
        local_120 = 0;
        uVar29 = FUN_00bc0bc8(param_1,&local_120);
        uVar12 = local_120;
        auVar5._8_8_ = local_140._8_8_;
        auVar5._0_8_ = local_140._0_8_;
        puVar13 = (undefined8 *)0x0;
        if (((uVar29 & 1) != 0) || (local_140 = auVar5, local_120 == 0)) goto LAB_00bbdb48;
        pvVar30 = (void *)param_1[0x266];
        lVar16 = *(long *)((long)pvVar30 + 8);
        puVar24 = pvVar30;
        if (lVar16 - 0xfc0U < 0xfffffffffffff010) {
          puVar24 = malloc(0x1000);
          if (puVar24 == (void *)0x0) {
LAB_00bbdbc4:
                    /* WARNING: Subroutine does not return */
            std::terminate();
          }
          lVar16 = 0;
          *puVar24 = pvVar30;
          puVar24[1] = 0;
          param_1[0x266] = (long)puVar24;
        }
        *(long *)((long)puVar24 + 8) = lVar16 + 0x30;
                    /* try { // try from 00bbd6c8 to 00cbd6d3 has its CatchHandler @ 00bbe094 */
        puVar13 = (undefined8 *)((long)puVar24 + lVar16 + 0x10);
        *puVar13 = &PTR_FUN_00c176a8;
        uVar22 = *(ushort *)((long)puVar24 + lVar16 + 0x19);
                    /* try { // try from 00bbd6d4 to 00cbd713 has its CatchHandler @ 00bbe09c */
        uVar25 = 0x17;
        *(ulong *)((long)puVar24 + lVar16 + 0x30) = uVar12;
        *(undefined1 *)((long)puVar24 + lVar16 + 0x18) = 0x15;
        pcVar19 = "initializer for module ";
LAB_00bbd6e8:
        puVar13[2] = pcVar19;
        puVar13[3] = uVar25;
        *(ushort *)((long)puVar13 + 9) = uVar22 & 0xf000 | 0x540;
        goto LAB_00bbdb48;
      }
      if (cVar1 == 'R') {
                    /* try { // try from 00bbd5a4 to 00cbd5ab has its CatchHandler @ 00bbe08c */
        *param_1 = (long)(pcVar19 + 2);
        local_120 = FUN_00bbf290(param_1,0);
        auVar10._8_8_ = local_140._8_8_;
        auVar10._0_8_ = local_140._0_8_;
        auVar9._8_8_ = local_140._8_8_;
        auVar9._0_8_ = local_140._0_8_;
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
        if (local_120 != 0) {
          pbVar18 = (byte *)*param_1;
          pbVar21 = (byte *)param_1[1];
          if (pbVar21 == pbVar18) {
LAB_00bbd648:
            puVar13 = (undefined8 *)FUN_00bc0b18(param_1,&local_120);
            goto LAB_00bbdb48;
          }
          bVar23 = *pbVar18;
                    /* try { // try from 00bbd5e4 to 00cbd5ef has its CatchHandler @ 00bbe018 */
          if ((bVar23 < 0x30) || ((0x39 < bVar23 && (0x19 < bVar23 - 0x41)))) {
            bVar11 = true;
                    /* try { // try from 00bbd5f0 to 00cbd5ff has its CatchHandler @ 00bbe004 */
            if (pbVar18 != pbVar21) {
LAB_00bbd5f4:
              if (bVar23 == 0x5f) {
                    /* try { // try from 00bbd600 to 00cbd613 has its CatchHandler @ 00bbdfec */
                *param_1 = (long)(pbVar18 + 1);
                goto LAB_00bbd648;
              }
            }
LAB_00bbd644:
            auVar33 = auVar9;
            if (bVar11) goto LAB_00bbd648;
          }
          else {
            do {
              bVar23 = *pbVar18;
              if ((bVar23 < 0x30) || ((0x39 < bVar23 && (0x19 < bVar23 - 0x41)))) {
                bVar11 = false;
                if (pbVar18 == pbVar21) goto LAB_00bbd644;
                goto LAB_00bbd5f4;
              }
              pbVar18 = pbVar18 + 1;
              *param_1 = (long)pbVar18;
              auVar33 = auVar10;
            } while (pbVar18 != pbVar21);
          }
        }
      }
      else {
        auVar33 = auVar8;
        if (cVar1 == 'V') {
          *param_1 = (long)(pcVar19 + 2);
          lVar16 = FUN_00bbf290(param_1,0);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if (lVar16 != 0) {
            pvVar30 = (void *)param_1[0x266];
            lVar17 = *(long *)((long)pvVar30 + 8);
                    /* try { // try from 00bbd3dc to 00cbd3e7 has its CatchHandler @ 00bbe06c */
            puVar24 = pvVar30;
            if (lVar17 - 0xfc0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbd3e8 to 00cbd3f7 has its CatchHandler @ 00bbe034 */
              puVar24 = malloc(0x1000);
              if (puVar24 == (void *)0x0) goto LAB_00bbdbc4;
                    /* try { // try from 00bbd3f8 to 00cbd40b has its CatchHandler @ 00bbe01c */
              lVar17 = 0;
              *puVar24 = pvVar30;
              puVar24[1] = 0;
              param_1[0x266] = (long)puVar24;
            }
            *(long *)((long)puVar24 + 8) = lVar17 + 0x30;
            puVar13 = (undefined8 *)((long)puVar24 + lVar17 + 0x10);
            *puVar13 = &PTR_FUN_00c176a8;
            uVar22 = *(ushort *)((long)puVar24 + lVar17 + 0x19);
            uVar25 = 0x13;
            *(long *)((long)puVar24 + lVar17 + 0x30) = lVar16;
            *(undefined1 *)((long)puVar24 + lVar17 + 0x18) = 0x15;
            pcVar19 = "guard variable for ";
            goto LAB_00bbd6e8;
          }
        }
      }
    }
  }
  else {
    if (*pcVar19 != 'T') goto LAB_00bbd2c4;
    if ((ulong)((long)pcVar20 - (long)pcVar19) < 2) {
LAB_00bbd76c:
                    /* try { // try from 00bbd76c to 00cbd777 has its CatchHandler @ 00bbdfe8 */
      pcVar19 = pcVar19 + 1;
      *param_1 = (long)pcVar19;
                    /* try { // try from 00bbd778 to 00cbd787 has its CatchHandler @ 00bbdfd4 */
      if (pcVar20 == pcVar19) {
        bVar11 = false;
      }
      else {
        bVar11 = *pcVar19 == 'v';
                    /* try { // try from 00bbd788 to 00cbd79b has its CatchHandler @ 00bbdfbc */
      }
      uVar12 = FUN_00bc0604(param_1);
      auVar33._8_8_ = local_140._8_8_;
      auVar33._0_8_ = local_140._0_8_;
      if ((uVar12 & 1) == 0) {
        local_120 = FUN_00bbd1fc(param_1);
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
        if (local_120 != 0) {
          if (bVar11) {
            puVar13 = (undefined8 *)FUN_00bc09bc();
          }
          else {
            puVar13 = (undefined8 *)FUN_00bc0a6c(param_1,&local_120);
          }
          goto LAB_00bbdb48;
        }
      }
    }
    else {
      bVar23 = pcVar19[1];
      if (bVar23 < 0x53) {
        if (bVar23 < 0x48) {
          if (bVar23 == 0x41) {
            *param_1 = (long)(pcVar19 + 2);
            local_120 = FUN_00bbf9c4(param_1);
            auVar33._8_8_ = local_140._8_8_;
            auVar33._0_8_ = local_140._0_8_;
            if (local_120 != 0) {
                    /* try { // try from 00bbd9c4 to 00cbd9cb has its CatchHandler @ 00bbe08c */
              puVar13 = (undefined8 *)FUN_00bc0294(param_1,&local_120);
              goto LAB_00bbdb48;
            }
          }
          else {
                    /* try { // try from 00bbd530 to 00cbd53b has its CatchHandler @ 00bbe07c */
            if (bVar23 != 0x43) goto LAB_00bbd76c;
            *param_1 = (long)(pcVar19 + 2);
                    /* try { // try from 00bbd53c to 00cbd57f has its CatchHandler @ 00bbe088 */
            local_120 = FUN_00bbdd50(param_1);
            auVar33._8_8_ = local_140._8_8_;
            auVar33._0_8_ = local_140._0_8_;
            if (local_120 != 0) {
              FUN_00bbdc10(param_1,1);
              auVar7._8_8_ = local_140._8_8_;
              auVar7._0_8_ = local_140._0_8_;
              auVar6._8_8_ = local_140._8_8_;
              auVar6._0_8_ = local_140._0_8_;
              auVar33._8_8_ = local_140._8_8_;
              auVar33._0_8_ = local_140._0_8_;
              if (((extraout_x1 != 0) &&
                  (pcVar19 = (char *)*param_1, auVar33 = auVar6, pcVar19 != (char *)param_1[1])) &&
                 (auVar33 = auVar7, *pcVar19 == '_')) {
                *param_1 = (long)(pcVar19 + 1);
                local_140._0_8_ = FUN_00bbdd50(param_1);
                auVar33._8_8_ = local_140._8_8_;
                auVar33._0_8_ = local_140._0_8_;
                if (local_140._0_8_ != 0) {
                  puVar13 = (undefined8 *)FUN_00bc0864(param_1,local_140,&local_120);
                  goto LAB_00bbdb48;
                }
              }
            }
          }
        }
        else if (bVar23 == 0x48) {
          *param_1 = (long)(pcVar19 + 2);
          local_120 = FUN_00bbf290(param_1,0);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if (local_120 != 0) {
            puVar13 = (undefined8 *)FUN_00bc090c(param_1,&local_120);
            goto LAB_00bbdb48;
          }
        }
        else {
          if (bVar23 != 0x49) goto LAB_00bbd76c;
          *param_1 = (long)(pcVar19 + 2);
          local_120 = FUN_00bbdd50(param_1);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if (local_120 != 0) {
                    /* try { // try from 00bbd72c to 00cbd733 has its CatchHandler @ 00bbe08c */
            puVar13 = (undefined8 *)FUN_00bc04a4(param_1,&local_120);
            goto LAB_00bbdb48;
          }
        }
      }
~~~
## 疑似コード 2/2 / UTF-8 3486 bytes

~~~c
      else if (bVar23 < 0x56) {
        if (bVar23 == 0x53) {
          *param_1 = (long)(pcVar19 + 2);
          local_120 = FUN_00bbdd50(param_1);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if (local_120 != 0) {
            puVar13 = (undefined8 *)FUN_00bc0554(param_1,&local_120);
            goto LAB_00bbdb48;
          }
        }
        else {
          if (bVar23 != 0x54) goto LAB_00bbd76c;
          *param_1 = (long)(pcVar19 + 2);
          local_120 = FUN_00bbdd50(param_1);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if (local_120 != 0) {
            puVar13 = (undefined8 *)FUN_00bc03f4(param_1,&local_120);
            goto LAB_00bbdb48;
          }
        }
      }
      else if (bVar23 == 0x56) {
                    /* try { // try from 00bbda00 to 00cbda0b has its CatchHandler @ 00bbdf80 */
        *param_1 = (long)(pcVar19 + 2);
        local_120 = FUN_00bbdd50(param_1);
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
                    /* try { // try from 00bbda0c to 00cbda1b has its CatchHandler @ 00bbdf6c */
        if (local_120 != 0) {
                    /* try { // try from 00bbda1c to 00cbda2f has its CatchHandler @ 00bbdf54 */
          puVar13 = (undefined8 *)FUN_00bc0344(param_1,&local_120);
          goto LAB_00bbdb48;
        }
      }
      else if (bVar23 == 0x57) {
        *param_1 = (long)(pcVar19 + 2);
        local_120 = FUN_00bbf290(param_1,0);
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
        if (local_120 != 0) {
          puVar13 = (undefined8 *)
                    FUN_00bbdc9c(param_1,"thread-local wrapper routine for ",&local_120);
          goto LAB_00bbdb48;
        }
      }
      else {
        if (bVar23 != 99) goto LAB_00bbd76c;
        *param_1 = (long)(pcVar19 + 2);
        uVar12 = FUN_00bc0604(param_1);
        auVar33._8_8_ = local_140._8_8_;
        auVar33._0_8_ = local_140._0_8_;
        if ((uVar12 & 1) == 0) {
          uVar12 = FUN_00bc0604(param_1);
          auVar33._8_8_ = local_140._8_8_;
          auVar33._0_8_ = local_140._0_8_;
          if ((uVar12 & 1) == 0) {
                    /* catch() { ... } // from try @ 00bbc314 with catch @ 00bbd2a4 */
                    /* catch() { ... } // from try @ 00bbbe38 with catch @ 00bbd2a8 */
            local_120 = FUN_00bbd1fc(param_1);
            auVar33._8_8_ = local_140._8_8_;
            auVar33._0_8_ = local_140._0_8_;
                    /* catch() { ... } // from try @ 00bbbf88 with catch @ 00bbd2ac */
                    /* catch() { ... } // from try @ 00bbc810 with catch @ 00bbd2b0 */
            if (local_120 != 0) {
                    /* catch() { ... } // from try @ 00bbc6a8 with catch @ 00bbd2b4 */
                    /* catch() { ... } // from try @ 00bbc504 with catch @ 00bbd2b8 */
                    /* catch() { ... } // from try @ 00bbc304 with catch @ 00bbd2bc */
              puVar13 = (undefined8 *)FUN_00bc07b4(param_1,&local_120);
                    /* catch() { ... } // from try @ 00bbbb94 with catch @ 00bbd2c0 */
              goto LAB_00bbdb48;
            }
          }
        }
      }
    }
  }
LAB_00bbdb44:
  puVar13 = (undefined8 *)0x0;
  local_140 = auVar33;
LAB_00bbdb48:
  FUN_00bc00b4(auStack_100);
  return puVar13;
}

~~~
