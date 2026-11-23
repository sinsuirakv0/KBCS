# 00bbd1fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbd2c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-be4b6524bb12f82041563cac099ec756)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "8f076acf1f4d6f7f56f617139716f600b5ae640f7550d4e021e7342895def71d",
  "source_text_sha256": "8f076acf1f4d6f7f56f617139716f600b5ae640f7550d4e021e7342895def71d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbd1fc",
        "00bbdbd7"
      ]
    ],
    "bytes_sha256": "c08fed96a7e58303d2380428375e7802257a5b2edd3dc0d7545ce51be4770876",
    "instruction_count": 631,
    "instruction_bytes": 2524,
    "body_bytes": 2524,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 27420 bytes

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
            _ZSt9terminatev();
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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbd1fc"></a> `00bbd1fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbd200"></a> `00bbd200` | `ff 83 05 d1` | sub sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00bbd204"></a> `00bbd204` | `fd 7b 10 a9` | stp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00bbd208"></a> `00bbd208` | `fc 6f 11 a9` | stp x28,x27,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bbd20c"></a> `00bbd20c` | `fa 67 12 a9` | stp x26,x25,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbd210"></a> `00bbd210` | `f8 5f 13 a9` | stp x24,x23,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbd214"></a> `00bbd214` | `f6 57 14 a9` | stp x22,x21,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbd218"></a> `00bbd218` | `f4 4f 15 a9` | stp x20,x19,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbd21c"></a> `00bbd21c` | `fd 03 04 91` | add x29,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00bbd220"></a> `00bbd220` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbd224"></a> `00bbd224` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbd228"></a> `00bbd228` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbd22c"></a> `00bbd22c` | `af 07 00 94` | bl 0x00bbf0e8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd230"></a> `00bbd230` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbd234"></a> `00bbd234` | `2a 01 08 eb` | subs x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd238"></a> `00bbd238` | `60 04 00 54` | b.eq 0x00bbd2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd23c"></a> `00bbd23c` | `0b 01 40 39` | ldrb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bbd240"></a> `00bbd240` | `7f 1d 01 71` | cmp w11,#0x47 | `FALL_THROUGH`
<a id="insn-00bbd244"></a> `00bbd244` | `a0 0a 00 54` | b.eq 0x00bbd398 | `CONDITIONAL_JUMP`
<a id="insn-00bbd248"></a> `00bbd248` | `7f 51 01 71` | cmp w11,#0x54 | `FALL_THROUGH`
<a id="insn-00bbd24c"></a> `00bbd24c` | `c1 03 00 54` | b.ne 0x00bbd2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd250"></a> `00bbd250` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd254"></a> `00bbd254` | `c3 28 00 54` | b.cc 0x00bbd76c | `CONDITIONAL_JUMP`
<a id="insn-00bbd258"></a> `00bbd258` | `0a 05 40 39` | ldrb w10,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbd25c"></a> `00bbd25c` | `5f 49 01 71` | cmp w10,#0x52 | `FALL_THROUGH`
<a id="insn-00bbd260"></a> `00bbd260` | `ed 15 00 54` | b.le 0x00bbd51c | `CONDITIONAL_JUMP`
<a id="insn-00bbd264"></a> `00bbd264` | `5f 55 01 71` | cmp w10,#0x55 | `FALL_THROUGH`
<a id="insn-00bbd268"></a> `00bbd268` | `6d 26 00 54` | b.le 0x00bbd734 | `CONDITIONAL_JUMP`
<a id="insn-00bbd26c"></a> `00bbd26c` | `5f 59 01 71` | cmp w10,#0x56 | `FALL_THROUGH`
<a id="insn-00bbd270"></a> `00bbd270` | `60 3c 00 54` | b.eq 0x00bbd9fc | `CONDITIONAL_JUMP`
<a id="insn-00bbd274"></a> `00bbd274` | `5f 5d 01 71` | cmp w10,#0x57 | `FALL_THROUGH`
<a id="insn-00bbd278"></a> `00bbd278` | `a0 3e 00 54` | b.eq 0x00bbda4c | `CONDITIONAL_JUMP`
<a id="insn-00bbd27c"></a> `00bbd27c` | `5f 8d 01 71` | cmp w10,#0x63 | `FALL_THROUGH`
<a id="insn-00bbd280"></a> `00bbd280` | `61 27 00 54` | b.ne 0x00bbd76c | `CONDITIONAL_JUMP`
<a id="insn-00bbd284"></a> `00bbd284` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd288"></a> `00bbd288` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd28c"></a> `00bbd28c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd290"></a> `00bbd290` | `dd 0c 00 94` | bl 0x00bc0604 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd294"></a> `00bbd294` | `80 45 00 37` | tbnz w0,#0x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd298"></a> `00bbd298` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd29c"></a> `00bbd29c` | `da 0c 00 94` | bl 0x00bc0604 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd2a0"></a> `00bbd2a0` | `20 45 00 37` | tbnz w0,#0x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd2a4"></a> `00bbd2a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd2a8"></a> `00bbd2a8` | `d5 ff ff 97` | bl 0x00bbd1fc | `UNCONDITIONAL_CALL`
<a id="insn-00bbd2ac"></a> `00bbd2ac` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd2b0"></a> `00bbd2b0` | `a0 44 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd2b4"></a> `00bbd2b4` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd2b8"></a> `00bbd2b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd2bc"></a> `00bbd2bc` | `3e 0d 00 94` | bl 0x00bc07b4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd2c0"></a> `00bbd2c0` | `ef 01 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd2c4"></a> `00bbd2c4` | `68 6e 41 f9` | ldr x8,[x19, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bbd2c8"></a> `00bbd2c8` | `69 6a 41 f9` | ldr x9,[x19, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bbd2cc"></a> `00bbd2cc` | `f9 03 01 91` | add x25,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd2d0"></a> `00bbd2d0` | `ff 83 00 79` | strh wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd2d4"></a> `00bbd2d4` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd2d8"></a> `00bbd2d8` | `ff 47 00 b9` | str wzr,[sp, #0x44] | `FALL_THROUGH`
<a id="insn-00bbd2dc"></a> `00bbd2dc` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bbd2e0"></a> `00bbd2e0` | `ff 23 01 39` | strb wzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbd2e4"></a> `00bbd2e4` | `ff 63 01 39` | strb wzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbd2e8"></a> `00bbd2e8` | `e8 2b 00 f9` | str x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbd2ec"></a> `00bbd2ec` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd2f0"></a> `00bbd2f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd2f4"></a> `00bbd2f4` | `e7 07 00 94` | bl 0x00bbf290 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd2f8"></a> `00bbd2f8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbd2fc"></a> `00bbd2fc` | `e0 1f 00 f9` | str x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbd300"></a> `00bbd300` | `40 42 00 b4` | cbz x0,0x00bbdb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbd304"></a> `00bbd304` | `69 6e 41 f9` | ldr x9,[x19, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bbd308"></a> `00bbd308` | `68 6a 41 f9` | ldr x8,[x19, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bbd30c"></a> `00bbd30c` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd310"></a> `00bbd310` | `e9 2b 40 f9` | ldr x9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbd314"></a> `00bbd314` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbd318"></a> `00bbd318` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbd31c"></a> `00bbd31c` | `62 09 00 54` | b.cs 0x00bbd448 | `CONDITIONAL_JUMP`
<a id="insn-00bbd320"></a> `00bbd320` | `6b 4e 41 f9` | ldr x11,[x19, #0x298] | `FALL_THROUGH`
<a id="insn-00bbd324"></a> `00bbd324` | `6c 52 41 f9` | ldr x12,[x19, #0x2a0] | `FALL_THROUGH`
<a id="insn-00bbd328"></a> `00bbd328` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00bbd32c"></a> `00bbd32c` | `c0 40 00 54` | b.eq 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd330"></a> `00bbd330` | `6d 01 40 f9` | ldr x13,[x11] | `FALL_THROUGH`
<a id="insn-00bbd334"></a> `00bbd334` | `8d 40 00 b4` | cbz x13,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd338"></a> `00bbd338` | `0c 79 69 f8` | ldr x12,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bbd33c"></a> `00bbd33c` | `ad 39 40 a9` | ldp x13,x14,[x13] | `FALL_THROUGH`
<a id="insn-00bbd340"></a> `00bbd340` | `8f 09 40 f9` | ldr x15,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd344"></a> `00bbd344` | `ce 01 0d cb` | sub x14,x14,x13 | `FALL_THROUGH`
<a id="insn-00bbd348"></a> `00bbd348` | `ff 0d 8e eb` | cmp x15,x14, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bbd34c"></a> `00bbd34c` | `c2 3f 00 54` | b.cs 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd350"></a> `00bbd350` | `30 05 00 91` | add x16,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd354"></a> `00bbd354` | `ad 79 6f f8` | ldr x13,[x13, x15, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bbd358"></a> `00bbd358` | `5f 01 10 eb` | cmp x10,x16 | `FALL_THROUGH`
<a id="insn-00bbd35c"></a> `00bbd35c` | `8d 0d 00 f9` | str x13,[x12, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd360"></a> `00bbd360` | `80 07 00 54` | b.eq 0x00bbd450 | `CONDITIONAL_JUMP`
<a id="insn-00bbd364"></a> `00bbd364` | `6d 01 40 f9` | ldr x13,[x11] | `FALL_THROUGH`
<a id="insn-00bbd368"></a> `00bbd368` | `ee 03 10 aa` | mov x14,x16 | `FALL_THROUGH`
<a id="insn-00bbd36c"></a> `00bbd36c` | `0d 01 00 b4` | cbz x13,0x00bbd38c | `CONDITIONAL_JUMP`
<a id="insn-00bbd370"></a> `00bbd370` | `0c 79 6e f8` | ldr x12,[x8, x14, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bbd374"></a> `00bbd374` | `ad 41 40 a9` | ldp x13,x16,[x13] | `FALL_THROUGH`
<a id="insn-00bbd378"></a> `00bbd378` | `8f 09 40 f9` | ldr x15,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd37c"></a> `00bbd37c` | `10 02 0d cb` | sub x16,x16,x13 | `FALL_THROUGH`
<a id="insn-00bbd380"></a> `00bbd380` | `ff 0d 90 eb` | cmp x15,x16, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bbd384"></a> `00bbd384` | `d0 05 00 91` | add x16,x14,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd388"></a> `00bbd388` | `63 fe ff 54` | b.cc 0x00bbd354 | `CONDITIONAL_JUMP`
<a id="insn-00bbd38c"></a> `00bbd38c` | `df 01 0a eb` | cmp x14,x10 | `FALL_THROUGH`
<a id="insn-00bbd390"></a> `00bbd390` | `42 06 00 54` | b.cs 0x00bbd458 | `CONDITIONAL_JUMP`
<a id="insn-00bbd394"></a> `00bbd394` | `ec 01 00 14` | b 0x00bbdb44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd398"></a> `00bbd398` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd39c"></a> `00bbd39c` | `43 3d 00 54` | b.cc 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3a0"></a> `00bbd3a0` | `09 05 40 39` | ldrb w9,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbd3a4"></a> `00bbd3a4` | `3f 25 01 71` | cmp w9,#0x49 | `FALL_THROUGH`
<a id="insn-00bbd3a8"></a> `00bbd3a8` | `80 15 00 54` | b.eq 0x00bbd658 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3ac"></a> `00bbd3ac` | `3f 49 01 71` | cmp w9,#0x52 | `FALL_THROUGH`
<a id="insn-00bbd3b0"></a> `00bbd3b0` | `80 0f 00 54` | b.eq 0x00bbd5a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3b4"></a> `00bbd3b4` | `3f 59 01 71` | cmp w9,#0x56 | `FALL_THROUGH`
<a id="insn-00bbd3b8"></a> `00bbd3b8` | `61 3c 00 54` | b.ne 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3bc"></a> `00bbd3bc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd3c0"></a> `00bbd3c0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd3c4"></a> `00bbd3c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd3c8"></a> `00bbd3c8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbd3cc"></a> `00bbd3cc` | `b1 07 00 94` | bl 0x00bbf290 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd3d0"></a> `00bbd3d0` | `a0 3b 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3d4"></a> `00bbd3d4` | `75 9a 49 f9` | ldr x21,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd3d8"></a> `00bbd3d8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd3dc"></a> `00bbd3dc` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bbd3e0"></a> `00bbd3e0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbd3e4"></a> `00bbd3e4` | `48 01 00 54` | b.hi 0x00bbd40c | `CONDITIONAL_JUMP`
<a id="insn-00bbd3e8"></a> `00bbd3e8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbd3ec"></a> `00bbd3ec` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbd3f0"></a> `00bbd3f0` | `38 7f 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd3f4"></a> `00bbd3f4` | `80 3e 00 b4` | cbz x0,0x00bbdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd3f8"></a> `00bbd3f8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbd3fc"></a> `00bbd3fc` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbd400"></a> `00bbd400` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbd404"></a> `00bbd404` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd408"></a> `00bbd408` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbd40c"></a> `00bbd40c` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd410"></a> `00bbd410` | `b4 02 08 8b` | add x20,x21,x8 | `FALL_THROUGH`
<a id="insn-00bbd414"></a> `00bbd414` | `c8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbd418"></a> `00bbd418` | `08 a1 1a 91` | add x8,x8,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bbd41c"></a> `00bbd41c` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd420"></a> `00bbd420` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbd424"></a> `00bbd424` | `88 0e 01 f8` | str x8,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbd428"></a> `00bbd428` | `89 92 40 78` | ldurh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd42c"></a> `00bbd42c` | `a8 02 80 52` | mov w8,#0x15 | `FALL_THROUGH`
<a id="insn-00bbd430"></a> `00bbd430` | `6b 02 80 52` | mov w11,#0x13 | `FALL_THROUGH`
<a id="insn-00bbd434"></a> `00bbd434` | `80 12 00 f9` | str x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd438"></a> `00bbd438` | `88 22 00 39` | strb w8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd43c"></a> `00bbd43c` | `08 b7 ff f0` | adrp x8,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bbd440"></a> `00bbd440` | `08 3d 08 91` | add x8,x8,#0x20f | `FALL_THROUGH`
<a id="insn-00bbd444"></a> `00bbd444` | `a9 00 00 14` | b 0x00bbd6e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd448"></a> `00bbd448` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbd44c"></a> `00bbd44c` | `c3 3a 00 54` | b.cc 0x00bbdba4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd450"></a> `00bbd450` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbd454"></a> `00bbd454` | `68 6e 01 f9` | str x8,[x19, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bbd458"></a> `00bbd458` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd45c"></a> `00bbd45c` | `0a 01 09 eb` | subs x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd460"></a> `00bbd460` | `40 37 00 54` | b.eq 0x00bbdb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbd464"></a> `00bbd464` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00bbd468"></a> `00bbd468` | `6b b9 00 51` | sub w11,w11,#0x2e | `FALL_THROUGH`
<a id="insn-00bbd46c"></a> `00bbd46c` | `7f c5 00 71` | cmp w11,#0x31 | `FALL_THROUGH`
<a id="insn-00bbd470"></a> `00bbd470` | `08 01 00 54` | b.hi 0x00bbd490 | `CONDITIONAL_JUMP`
<a id="insn-00bbd474"></a> `00bbd474` | `2c 00 80 52` | mov w12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd478"></a> `00bbd478` | `8b 21 cb 9a` | lsl x11,x12,x11 | `FALL_THROUGH`
<a id="insn-00bbd47c"></a> `00bbd47c` | `2c 00 80 d2` | mov x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd480"></a> `00bbd480` | `0c 10 a0 f2` | movk x12,#0x80, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbd484"></a> `00bbd484` | `4c 00 e0 f2` | movk x12,#0x2, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbd488"></a> `00bbd488` | `7f 01 0c ea` | tst x11,x12 | `FALL_THROUGH`
<a id="insn-00bbd48c"></a> `00bbd48c` | `e1 35 00 54` | b.ne 0x00bbdb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbd490"></a> `00bbd490` | `5f 35 00 f1` | cmp x10,#0xd | `FALL_THROUGH`
<a id="insn-00bbd494"></a> `00bbd494` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbd498"></a> `00bbd498` | `c3 01 00 54` | b.cc 0x00bbd4d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd49c"></a> `00bbd49c` | `ac 2a 8c d2` | mov x12,#0x6155 | `FALL_THROUGH`
<a id="insn-00bbd4a0"></a> `00bbd4a0` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00bbd4a4"></a> `00bbd4a4` | `2b 51 40 f8` | ldur x11,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-00bbd4a8"></a> `00bbd4a8` | `2c a7 ac f2` | movk x12,#0x6539, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbd4ac"></a> `00bbd4ac` | `cc 2d cc f2` | movk x12,#0x616e, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbd4b0"></a> `00bbd4b0` | `4c 8c ed f2` | movk x12,#0x6c62, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbd4b4"></a> `00bbd4b4` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00bbd4b8"></a> `00bbd4b8` | `2a 4c 8c d2` | mov x10,#0x6261 | `FALL_THROUGH`
<a id="insn-00bbd4bc"></a> `00bbd4bc` | `8a ad ac f2` | movk x10,#0x656c, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbd4c0"></a> `00bbd4c0` | `ea 2b cd f2` | movk x10,#0x695f, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbd4c4"></a> `00bbd4c4` | `ca 2c e9 f2` | movk x10,#0x4966, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbd4c8"></a> `00bbd4c8` | `60 01 4a fa` | ccmp x11,x10,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbd4cc"></a> `00bbd4cc` | `c0 2d 00 54` | b.eq 0x00bbda84 | `CONDITIONAL_JUMP`
<a id="insn-00bbd4d0"></a> `00bbd4d0` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd4d4"></a> `00bbd4d4` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd4d8"></a> `00bbd4d8` | `e8 00 00 37` | tbnz w8,#0x0,0x00bbd4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd4dc"></a> `00bbd4dc` | `e8 07 41 39` | ldrb w8,[sp, #0x41] | `FALL_THROUGH`
<a id="insn-00bbd4e0"></a> `00bbd4e0` | `a8 00 00 34` | cbz w8,0x00bbd4f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd4e4"></a> `00bbd4e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd4e8"></a> `00bbd4e8` | `1a 02 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd4ec"></a> `00bbd4ec` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd4f0"></a> `00bbd4f0` | `a0 32 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd4f4"></a> `00bbd4f4` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd4f8"></a> `00bbd4f8` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd4fc"></a> `00bbd4fc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd500"></a> `00bbd500` | `40 16 00 54` | b.eq 0x00bbd7c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd504"></a> `00bbd504` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbd508"></a> `00bbd508` | `5f d9 01 71` | cmp w10,#0x76 | `FALL_THROUGH`
<a id="insn-00bbd50c"></a> `00bbd50c` | `e1 15 00 54` | b.ne 0x00bbd7c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd510"></a> `00bbd510` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd514"></a> `00bbd514` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbd518"></a> `00bbd518` | `0a 01 00 14` | b 0x00bbd940 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd51c"></a> `00bbd51c` | `5f 1d 01 71` | cmp w10,#0x47 | `FALL_THROUGH`
<a id="insn-00bbd520"></a> `00bbd520` | `ec 0e 00 54` | b.gt 0x00bbd6fc | `CONDITIONAL_JUMP`
<a id="insn-00bbd524"></a> `00bbd524` | `5f 05 01 71` | cmp w10,#0x41 | `FALL_THROUGH`
<a id="insn-00bbd528"></a> `00bbd528` | `00 24 00 54` | b.eq 0x00bbd9a8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd52c"></a> `00bbd52c` | `5f 0d 01 71` | cmp w10,#0x43 | `FALL_THROUGH`
<a id="insn-00bbd530"></a> `00bbd530` | `e1 11 00 54` | b.ne 0x00bbd76c | `CONDITIONAL_JUMP`
<a id="insn-00bbd534"></a> `00bbd534` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd538"></a> `00bbd538` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd53c"></a> `00bbd53c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd540"></a> `00bbd540` | `04 02 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd544"></a> `00bbd544` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd548"></a> `00bbd548` | `e0 2f 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd54c"></a> `00bbd54c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd550"></a> `00bbd550` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd554"></a> `00bbd554` | `af 01 00 94` | bl 0x00bbdc10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd558"></a> `00bbd558` | `61 2f 00 b4` | cbz x1,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd55c"></a> `00bbd55c` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbd560"></a> `00bbd560` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd564"></a> `00bbd564` | `00 2f 00 54` | b.eq 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd568"></a> `00bbd568` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbd56c"></a> `00bbd56c` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbd570"></a> `00bbd570` | `a1 2e 00 54` | b.ne 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd574"></a> `00bbd574` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd578"></a> `00bbd578` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd57c"></a> `00bbd57c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd580"></a> `00bbd580` | `f4 01 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd584"></a> `00bbd584` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd588"></a> `00bbd588` | `e0 2d 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd58c"></a> `00bbd58c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbd590"></a> `00bbd590` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd594"></a> `00bbd594` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd598"></a> `00bbd598` | `b3 0c 00 94` | bl 0x00bc0864 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd59c"></a> `00bbd59c` | `38 01 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd5a0"></a> `00bbd5a0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd5a4"></a> `00bbd5a4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd5a8"></a> `00bbd5a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd5ac"></a> `00bbd5ac` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbd5b0"></a> `00bbd5b0` | `38 07 00 94` | bl 0x00bbf290 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd5b4"></a> `00bbd5b4` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd5b8"></a> `00bbd5b8` | `60 2c 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5bc"></a> `00bbd5bc` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbd5c0"></a> `00bbd5c0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd5c4"></a> `00bbd5c4` | `20 04 00 54` | b.eq 0x00bbd648 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5c8"></a> `00bbd5c8` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bbd5cc"></a> `00bbd5cc` | `5f c1 00 71` | cmp w10,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd5d0"></a> `00bbd5d0` | `c3 00 00 54` | b.cc 0x00bbd5e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5d4"></a> `00bbd5d4` | `5f e9 00 71` | cmp w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bbd5d8"></a> `00bbd5d8` | `03 02 00 54` | b.cc 0x00bbd618 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5dc"></a> `00bbd5dc` | `4b 05 01 51` | sub w11,w10,#0x41 | `FALL_THROUGH`
<a id="insn-00bbd5e0"></a> `00bbd5e0` | `7f 65 00 71` | cmp w11,#0x19 | `FALL_THROUGH`
<a id="insn-00bbd5e4"></a> `00bbd5e4` | `a9 01 00 54` | b.ls 0x00bbd618 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5e8"></a> `00bbd5e8` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd5ec"></a> `00bbd5ec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd5f0"></a> `00bbd5f0` | `a0 02 00 54` | b.eq 0x00bbd644 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5f4"></a> `00bbd5f4` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bbd5f8"></a> `00bbd5f8` | `61 02 00 54` | b.ne 0x00bbd644 | `CONDITIONAL_JUMP`
<a id="insn-00bbd5fc"></a> `00bbd5fc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd600"></a> `00bbd600` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd604"></a> `00bbd604` | `11 00 00 14` | b 0x00bbd648 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd608"></a> `00bbd608` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd60c"></a> `00bbd60c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd610"></a> `00bbd610` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd614"></a> `00bbd614` | `80 29 00 54` | b.eq 0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd618"></a> `00bbd618` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bbd61c"></a> `00bbd61c` | `5f c1 00 71` | cmp w10,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd620"></a> `00bbd620` | `c3 00 00 54` | b.cc 0x00bbd638 | `CONDITIONAL_JUMP`
<a id="insn-00bbd624"></a> `00bbd624` | `5f e9 00 71` | cmp w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bbd628"></a> `00bbd628` | `03 ff ff 54` | b.cc 0x00bbd608 | `CONDITIONAL_JUMP`
<a id="insn-00bbd62c"></a> `00bbd62c` | `4b 05 01 51` | sub w11,w10,#0x41 | `FALL_THROUGH`
<a id="insn-00bbd630"></a> `00bbd630` | `7f 65 00 71` | cmp w11,#0x19 | `FALL_THROUGH`
<a id="insn-00bbd634"></a> `00bbd634` | `a9 fe ff 54` | b.ls 0x00bbd608 | `CONDITIONAL_JUMP`
<a id="insn-00bbd638"></a> `00bbd638` | `eb 03 1f 2a` | mov w11,wzr | `FALL_THROUGH`
<a id="insn-00bbd63c"></a> `00bbd63c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd640"></a> `00bbd640` | `a1 fd ff 54` | b.ne 0x00bbd5f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd644"></a> `00bbd644` | `0b 28 00 34` | cbz w11,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd648"></a> `00bbd648` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd64c"></a> `00bbd64c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd650"></a> `00bbd650` | `32 0d 00 94` | bl 0x00bc0b18 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd654"></a> `00bbd654` | `0a 01 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd658"></a> `00bbd658` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd65c"></a> `00bbd65c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd660"></a> `00bbd660` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd664"></a> `00bbd664` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd668"></a> `00bbd668` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd66c"></a> `00bbd66c` | `57 0d 00 94` | bl 0x00bc0bc8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd670"></a> `00bbd670` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bbd674"></a> `00bbd674` | `a0 26 00 37` | tbnz w0,#0x0,0x00bbdb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbd678"></a> `00bbd678` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd67c"></a> `00bbd67c` | `75 26 00 b4` | cbz x21,0x00bbdb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbd680"></a> `00bbd680` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd684"></a> `00bbd684` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd688"></a> `00bbd688` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bbd68c"></a> `00bbd68c` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbd690"></a> `00bbd690` | `08 01 00 54` | b.hi 0x00bbd6b0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd694"></a> `00bbd694` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbd698"></a> `00bbd698` | `8e 7e 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd69c"></a> `00bbd69c` | `40 29 00 b4` | cbz x0,0x00bbdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd6a0"></a> `00bbd6a0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbd6a4"></a> `00bbd6a4` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbd6a8"></a> `00bbd6a8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbd6ac"></a> `00bbd6ac` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd6b0"></a> `00bbd6b0` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd6b4"></a> `00bbd6b4` | `d4 02 08 8b` | add x20,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbd6b8"></a> `00bbd6b8` | `c8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbd6bc"></a> `00bbd6bc` | `08 a1 1a 91` | add x8,x8,#0x6a8 | `FALL_THROUGH`
<a id="insn-00bbd6c0"></a> `00bbd6c0` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd6c4"></a> `00bbd6c4` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbd6c8"></a> `00bbd6c8` | `88 0e 01 f8` | str x8,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbd6cc"></a> `00bbd6cc` | `89 92 40 78` | ldurh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd6d0"></a> `00bbd6d0` | `a8 02 80 52` | mov w8,#0x15 | `FALL_THROUGH`
<a id="insn-00bbd6d4"></a> `00bbd6d4` | `eb 02 80 52` | mov w11,#0x17 | `FALL_THROUGH`
<a id="insn-00bbd6d8"></a> `00bbd6d8` | `95 12 00 f9` | str x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd6dc"></a> `00bbd6dc` | `88 22 00 39` | strb w8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd6e0"></a> `00bbd6e0` | `08 b7 ff d0` | adrp x8,0x29f000 | `FALL_THROUGH`
<a id="insn-00bbd6e4"></a> `00bbd6e4` | `08 85 07 91` | add x8,x8,#0x1e1 | `FALL_THROUGH`
<a id="insn-00bbd6e8"></a> `00bbd6e8` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbd6ec"></a> `00bbd6ec` | `88 2e 01 a9` | stp x8,x11,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd6f0"></a> `00bbd6f0` | `28 01 0a 2a` | orr w8,w9,w10 | `FALL_THROUGH`
<a id="insn-00bbd6f4"></a> `00bbd6f4` | `88 92 00 78` | sturh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd6f8"></a> `00bbd6f8` | `14 01 00 14` | b 0x00bbdb48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd6fc"></a> `00bbd6fc` | `5f 21 01 71` | cmp w10,#0x48 | `FALL_THROUGH`
<a id="insn-00bbd700"></a> `00bbd700` | `80 16 00 54` | b.eq 0x00bbd9d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd704"></a> `00bbd704` | `5f 25 01 71` | cmp w10,#0x49 | `FALL_THROUGH`
<a id="insn-00bbd708"></a> `00bbd708` | `21 03 00 54` | b.ne 0x00bbd76c | `CONDITIONAL_JUMP`
<a id="insn-00bbd70c"></a> `00bbd70c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd710"></a> `00bbd710` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd714"></a> `00bbd714` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd718"></a> `00bbd718` | `8e 01 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd71c"></a> `00bbd71c` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd720"></a> `00bbd720` | `20 21 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd724"></a> `00bbd724` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd728"></a> `00bbd728` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd72c"></a> `00bbd72c` | `5e 0b 00 94` | bl 0x00bc04a4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd730"></a> `00bbd730` | `d3 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd734"></a> `00bbd734` | `5f 4d 01 71` | cmp w10,#0x53 | `FALL_THROUGH`
<a id="insn-00bbd738"></a> `00bbd738` | `60 17 00 54` | b.eq 0x00bbda24 | `CONDITIONAL_JUMP`
<a id="insn-00bbd73c"></a> `00bbd73c` | `5f 51 01 71` | cmp w10,#0x54 | `FALL_THROUGH`
<a id="insn-00bbd740"></a> `00bbd740` | `61 01 00 54` | b.ne 0x00bbd76c | `CONDITIONAL_JUMP`
<a id="insn-00bbd744"></a> `00bbd744` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd748"></a> `00bbd748` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd74c"></a> `00bbd74c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd750"></a> `00bbd750` | `80 01 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd754"></a> `00bbd754` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd758"></a> `00bbd758` | `60 1f 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd75c"></a> `00bbd75c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd760"></a> `00bbd760` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd764"></a> `00bbd764` | `24 0b 00 94` | bl 0x00bc03f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd768"></a> `00bbd768` | `c5 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd76c"></a> `00bbd76c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd770"></a> `00bbd770` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd774"></a> `00bbd774` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd778"></a> `00bbd778` | `a0 00 00 54` | b.eq 0x00bbd78c | `CONDITIONAL_JUMP`
<a id="insn-00bbd77c"></a> `00bbd77c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bbd780"></a> `00bbd780` | `1f d9 01 71` | cmp w8,#0x76 | `FALL_THROUGH`
<a id="insn-00bbd784"></a> `00bbd784` | `f4 17 9f 1a` | cset w20,eq | `FALL_THROUGH`
<a id="insn-00bbd788"></a> `00bbd788` | `02 00 00 14` | b 0x00bbd790 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd78c"></a> `00bbd78c` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00bbd790"></a> `00bbd790` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd794"></a> `00bbd794` | `9c 0b 00 94` | bl 0x00bc0604 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd798"></a> `00bbd798` | `60 1d 00 37` | tbnz w0,#0x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd79c"></a> `00bbd79c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd7a0"></a> `00bbd7a0` | `97 fe ff 97` | bl 0x00bbd1fc | `UNCONDITIONAL_CALL`
<a id="insn-00bbd7a4"></a> `00bbd7a4` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd7a8"></a> `00bbd7a8` | `e0 1c 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd7ac"></a> `00bbd7ac` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd7b0"></a> `00bbd7b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd7b4"></a> `00bbd7b4` | `74 00 00 34` | cbz w20,0x00bbd7c0 | `CONDITIONAL_JUMP`
<a id="insn-00bbd7b8"></a> `00bbd7b8` | `81 0c 00 94` | bl 0x00bc09bc | `UNCONDITIONAL_CALL`
<a id="insn-00bbd7bc"></a> `00bbd7bc` | `b0 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd7c0"></a> `00bbd7c0` | `ab 0c 00 94` | bl 0x00bc0a6c | `UNCONDITIONAL_CALL`
<a id="insn-00bbd7c4"></a> `00bbd7c4` | `ae 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd7c8"></a> `00bbd7c8` | `69 22 41 a9` | ldp x9,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd7cc"></a> `00bbd7cc` | `3c 00 80 d2` | mov x28,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd7d0"></a> `00bbd7d0` | `1c 10 a0 f2` | movk x28,#0x80, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbd7d4"></a> `00bbd7d4` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bbd7d8"></a> `00bbd7d8` | `14 a8 80 52` | mov w20,#0x540 | `FALL_THROUGH`
<a id="insn-00bbd7dc"></a> `00bbd7dc` | `1c 01 c0 f2` | movk x28,#0x8, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbd7e0"></a> `00bbd7e0` | `3b 00 80 52` | mov w27,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd7e4"></a> `00bbd7e4` | `1a 01 09 cb` | sub x26,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbd7e8"></a> `00bbd7e8` | `5c 00 e0 f2` | movk x28,#0x2, LSL #48 | `FALL_THROUGH`
<a id="insn-00bbd7ec"></a> `00bbd7ec` | `48 ff 43 93` | asr x8,x26,#0x3 | `FALL_THROUGH`
<a id="insn-00bbd7f0"></a> `00bbd7f0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd7f4"></a> `00bbd7f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd7f8"></a> `00bbd7f8` | `56 01 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd7fc"></a> `00bbd7fc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbd800"></a> `00bbd800` | `20 1a 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd804"></a> `00bbd804` | `e8 63 41 39` | ldrb w8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbd808"></a> `00bbd808` | `78 0e 40 f9` | ldr x24,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd80c"></a> `00bbd80c` | `08 04 00 34` | cbz w8,0x00bbd88c | `CONDITIONAL_JUMP`
<a id="insn-00bbd810"></a> `00bbd810` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd814"></a> `00bbd814` | `08 03 08 cb` | sub x8,x24,x8 | `FALL_THROUGH`
<a id="insn-00bbd818"></a> `00bbd818` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00bbd81c"></a> `00bbd81c` | `81 03 00 54` | b.ne 0x00bbd88c | `CONDITIONAL_JUMP`
<a id="insn-00bbd820"></a> `00bbd820` | `77 9a 49 f9` | ldr x23,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd824"></a> `00bbd824` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd828"></a> `00bbd828` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbd82c"></a> `00bbd82c` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbd830"></a> `00bbd830` | `08 01 00 54` | b.hi 0x00bbd850 | `CONDITIONAL_JUMP`
<a id="insn-00bbd834"></a> `00bbd834` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbd838"></a> `00bbd838` | `26 7e 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd83c"></a> `00bbd83c` | `40 1c 00 b4` | cbz x0,0x00bbdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd840"></a> `00bbd840` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbd844"></a> `00bbd844` | `17 7c 00 a9` | stp x23,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbd848"></a> `00bbd848` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbd84c"></a> `00bbd84c` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbd850"></a> `00bbd850` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbd854"></a> `00bbd854` | `e8 02 08 8b` | add x8,x23,x8 | `FALL_THROUGH`
<a id="insn-00bbd858"></a> `00bbd858` | `ea 0a 80 52` | mov w10,#0x57 | `FALL_THROUGH`
<a id="insn-00bbd85c"></a> `00bbd85c` | `e9 06 00 f9` | str x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd860"></a> `00bbd860` | `e9 02 00 90` | adrp x9,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbd864"></a> `00bbd864` | `29 61 21 91` | add x9,x9,#0x858 | `FALL_THROUGH`
<a id="insn-00bbd868"></a> `00bbd868` | `09 0d 01 f8` | str x9,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbd86c"></a> `00bbd86c` | `09 91 40 78` | ldurh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd870"></a> `00bbd870` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd874"></a> `00bbd874` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbd878"></a> `00bbd878` | `16 09 00 f9` | str x22,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd87c"></a> `00bbd87c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bbd880"></a> `00bbd880` | `29 01 14 2a` | orr w9,w9,w20 | `FALL_THROUGH`
<a id="insn-00bbd884"></a> `00bbd884` | `09 91 00 78` | sturh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00bbd888"></a> `00bbd888` | `78 0e 40 f9` | ldr x24,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd88c"></a> `00bbd88c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd890"></a> `00bbd890` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00bbd894"></a> `00bbd894` | `21 03 00 54` | b.ne 0x00bbd8f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd898"></a> `00bbd898` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd89c"></a> `00bbd89c` | `17 03 00 cb` | sub x23,x24,x0 | `FALL_THROUGH`
<a id="insn-00bbd8a0"></a> `00bbd8a0` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00bbd8a4"></a> `00bbd8a4` | `e1 fa 7f d3` | lsl x1,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd8a8"></a> `00bbd8a8` | `a0 00 00 54` | b.eq 0x00bbd8bc | `CONDITIONAL_JUMP`
<a id="insn-00bbd8ac"></a> `00bbd8ac` | `29 7e 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd8b0"></a> `00bbd8b0` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd8b4"></a> `00bbd8b4` | `a0 01 00 b5` | cbnz x0,0x00bbd8e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbd8b8"></a> `00bbd8b8` | `c5 00 00 14` | b 0x00bbdbcc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd8bc"></a> `00bbd8bc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbd8c0"></a> `00bbd8c0` | `04 7e 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd8c4"></a> `00bbd8c4` | `80 18 00 b4` | cbz x0,0x00bbdbd4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd8c8"></a> `00bbd8c8` | `1f 03 15 eb` | cmp x24,x21 | `FALL_THROUGH`
<a id="insn-00bbd8cc"></a> `00bbd8cc` | `c0 00 00 54` | b.eq 0x00bbd8e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd8d0"></a> `00bbd8d0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbd8d4"></a> `00bbd8d4` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bbd8d8"></a> `00bbd8d8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbd8dc"></a> `00bbd8dc` | `f5 75 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd8e0"></a> `00bbd8e0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbd8e4"></a> `00bbd8e4` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd8e8"></a> `00bbd8e8` | `e8 fe 42 93` | asr x8,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd8ec"></a> `00bbd8ec` | `18 00 17 8b` | add x24,x0,x23 | `FALL_THROUGH`
<a id="insn-00bbd8f0"></a> `00bbd8f0` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbd8f4"></a> `00bbd8f4` | `78 a2 01 a9` | stp x24,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd8f8"></a> `00bbd8f8` | `08 23 00 91` | add x8,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bbd8fc"></a> `00bbd8fc` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbd900"></a> `00bbd900` | `16 03 00 f9` | str x22,[x24] | `FALL_THROUGH`
<a id="insn-00bbd904"></a> `00bbd904` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbd908"></a> `00bbd908` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd90c"></a> `00bbd90c` | `00 01 00 54` | b.eq 0x00bbd92c | `CONDITIONAL_JUMP`
<a id="insn-00bbd910"></a> `00bbd910` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bbd914"></a> `00bbd914` | `08 b9 00 51` | sub w8,w8,#0x2e | `FALL_THROUGH`
<a id="insn-00bbd918"></a> `00bbd918` | `1f c5 00 71` | cmp w8,#0x31 | `FALL_THROUGH`
<a id="insn-00bbd91c"></a> `00bbd91c` | `c8 f6 ff 54` | b.hi 0x00bbd7f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd920"></a> `00bbd920` | `68 23 c8 9a` | lsl x8,x27,x8 | `FALL_THROUGH`
<a id="insn-00bbd924"></a> `00bbd924` | `1f 01 1c ea` | tst x8,x28 | `FALL_THROUGH`
<a id="insn-00bbd928"></a> `00bbd928` | `60 f6 ff 54` | b.eq 0x00bbd7f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbd92c"></a> `00bbd92c` | `e1 07 40 f9` | ldr x1,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbd930"></a> `00bbd930` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd934"></a> `00bbd934` | `4c 09 00 94` | bl 0x00bbfe64 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd938"></a> `00bbd938` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd93c"></a> `00bbd93c` | `e0 07 02 a9` | stp x0,x1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbd940"></a> `00bbd940` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbd944"></a> `00bbd944` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd948"></a> `00bbd948` | `c0 01 00 54` | b.eq 0x00bbd980 | `CONDITIONAL_JUMP`
<a id="insn-00bbd94c"></a> `00bbd94c` | `28 01 40 39` | ldrb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbd950"></a> `00bbd950` | `1f 45 01 71` | cmp w8,#0x51 | `FALL_THROUGH`
<a id="insn-00bbd954"></a> `00bbd954` | `61 01 00 54` | b.ne 0x00bbd980 | `CONDITIONAL_JUMP`
<a id="insn-00bbd958"></a> `00bbd958` | `75 2a 4c 39` | ldrb w21,[x19, #0x30a] | `FALL_THROUGH`
<a id="insn-00bbd95c"></a> `00bbd95c` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd960"></a> `00bbd960` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbd964"></a> `00bbd964` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd968"></a> `00bbd968` | `69 2a 0c 39` | strb w9,[x19, #0x30a] | `FALL_THROUGH`
<a id="insn-00bbd96c"></a> `00bbd96c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd970"></a> `00bbd970` | `24 15 00 94` | bl 0x00bc2e00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd974"></a> `00bbd974` | `75 2a 0c 39` | strb w21,[x19, #0x30a] | `FALL_THROUGH`
<a id="insn-00bbd978"></a> `00bbd978` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbd97c"></a> `00bbd97c` | `40 0e 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd980"></a> `00bbd980` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bbd984"></a> `00bbd984` | `e2 e3 00 91` | add x2,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbd988"></a> `00bbd988` | `e3 83 00 91` | add x3,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbd98c"></a> `00bbd98c` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbd990"></a> `00bbd990` | `e5 43 00 91` | add x5,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbd994"></a> `00bbd994` | `26 03 7e b2` | orr x6,x25,#0x4 | `FALL_THROUGH`
<a id="insn-00bbd998"></a> `00bbd998` | `27 23 00 91` | add x7,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00bbd99c"></a> `00bbd99c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd9a0"></a> `00bbd9a0` | `88 09 00 94` | bl 0x00bbffc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd9a4"></a> `00bbd9a4` | `36 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd9a8"></a> `00bbd9a8` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd9ac"></a> `00bbd9ac` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd9b0"></a> `00bbd9b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd9b4"></a> `00bbd9b4` | `04 08 00 94` | bl 0x00bbf9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd9b8"></a> `00bbd9b8` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd9bc"></a> `00bbd9bc` | `40 0c 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd9c0"></a> `00bbd9c0` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd9c4"></a> `00bbd9c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd9c8"></a> `00bbd9c8` | `33 0a 00 94` | bl 0x00bc0294 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd9cc"></a> `00bbd9cc` | `2c 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd9d0"></a> `00bbd9d0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbd9d4"></a> `00bbd9d4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbd9d8"></a> `00bbd9d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd9dc"></a> `00bbd9dc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbd9e0"></a> `00bbd9e0` | `2c 06 00 94` | bl 0x00bbf290 | `UNCONDITIONAL_CALL`
<a id="insn-00bbd9e4"></a> `00bbd9e4` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbd9e8"></a> `00bbd9e8` | `e0 0a 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbd9ec"></a> `00bbd9ec` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbd9f0"></a> `00bbd9f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbd9f4"></a> `00bbd9f4` | `c6 0b 00 94` | bl 0x00bc090c | `UNCONDITIONAL_CALL`
<a id="insn-00bbd9f8"></a> `00bbd9f8` | `21 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbd9fc"></a> `00bbd9fc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbda00"></a> `00bbda00` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbda04"></a> `00bbda04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda08"></a> `00bbda08` | `d2 00 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbda0c"></a> `00bbda0c` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbda10"></a> `00bbda10` | `a0 09 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbda14"></a> `00bbda14` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbda18"></a> `00bbda18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda1c"></a> `00bbda1c` | `4a 0a 00 94` | bl 0x00bc0344 | `UNCONDITIONAL_CALL`
<a id="insn-00bbda20"></a> `00bbda20` | `17 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbda24"></a> `00bbda24` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbda28"></a> `00bbda28` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbda2c"></a> `00bbda2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda30"></a> `00bbda30` | `c8 00 00 94` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bbda34"></a> `00bbda34` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbda38"></a> `00bbda38` | `60 08 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbda3c"></a> `00bbda3c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbda40"></a> `00bbda40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda44"></a> `00bbda44` | `c4 0a 00 94` | bl 0x00bc0554 | `UNCONDITIONAL_CALL`
<a id="insn-00bbda48"></a> `00bbda48` | `0d 00 00 14` | b 0x00bbda7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbda4c"></a> `00bbda4c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbda50"></a> `00bbda50` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbda54"></a> `00bbda54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda58"></a> `00bbda58` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbda5c"></a> `00bbda5c` | `0d 06 00 94` | bl 0x00bbf290 | `UNCONDITIONAL_CALL`
<a id="insn-00bbda60"></a> `00bbda60` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbda64"></a> `00bbda64` | `00 07 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbda68"></a> `00bbda68` | `41 b7 ff b0` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbda6c"></a> `00bbda6c` | `21 6c 11 91` | add x1,x1,#0x45b | `FALL_THROUGH`
<a id="insn-00bbda70"></a> `00bbda70` | `e2 03 01 91` | add x2,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bbda74"></a> `00bbda74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbda78"></a> `00bbda78` | `89 00 00 94` | bl 0x00bbdc9c | `UNCONDITIONAL_CALL`
<a id="insn-00bbda7c"></a> `00bbda7c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbda80"></a> `00bbda80` | `32 00 00 14` | b 0x00bbdb48 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbda84"></a> `00bbda84` | `6b 2a 41 a9` | ldp x11,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbda88"></a> `00bbda88` | `29 35 00 91` | add x9,x9,#0xd | `FALL_THROUGH`
<a id="insn-00bbda8c"></a> `00bbda8c` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bbda90"></a> `00bbda90` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbda94"></a> `00bbda94` | `4a 01 0b cb` | sub x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbda98"></a> `00bbda98` | `54 fd 43 93` | asr x20,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbda9c"></a> `00bbda9c` | `0d 00 00 14` | b 0x00bbdad0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdaa0"></a> `00bbdaa0` | `ac 7d 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdaa4"></a> `00bbdaa4` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdaa8"></a> `00bbdaa8` | `00 09 00 b4` | cbz x0,0x00bbdbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bbdaac"></a> `00bbdaac` | `c8 fe 42 93` | asr x8,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00bbdab0"></a> `00bbdab0` | `17 00 16 8b` | add x23,x0,x22 | `FALL_THROUGH`
<a id="insn-00bbdab4"></a> `00bbdab4` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbdab8"></a> `00bbdab8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbdabc"></a> `00bbdabc` | `77 a2 01 a9` | stp x23,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdac0"></a> `00bbdac0` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bbdac4"></a> `00bbdac4` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdac8"></a> `00bbdac8` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00bbdacc"></a> `00bbdacc` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbdad0"></a> `00bbdad0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbdad4"></a> `00bbdad4` | `80 00 00 54` | b.eq 0x00bbdae4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdad8"></a> `00bbdad8` | `28 01 40 39` | ldrb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bbdadc"></a> `00bbdadc` | `1f 15 01 71` | cmp w8,#0x45 | `FALL_THROUGH`
<a id="insn-00bbdae0"></a> `00bbdae0` | `c0 04 00 54` | b.eq 0x00bbdb78 | `CONDITIONAL_JUMP`
<a id="insn-00bbdae4"></a> `00bbdae4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbdae8"></a> `00bbdae8` | `b7 07 00 94` | bl 0x00bbf9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdaec"></a> `00bbdaec` | `c0 02 00 b4` | cbz x0,0x00bbdb44 | `CONDITIONAL_JUMP`
<a id="insn-00bbdaf0"></a> `00bbdaf0` | `77 a2 41 a9` | ldp x23,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbdaf4"></a> `00bbdaf4` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bbdaf8"></a> `00bbdaf8` | `41 fe ff 54` | b.ne 0x00bbdac0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdafc"></a> `00bbdafc` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbdb00"></a> `00bbdb00` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdb04"></a> `00bbdb04` | `f6 02 00 cb` | sub x22,x23,x0 | `FALL_THROUGH`
<a id="insn-00bbdb08"></a> `00bbdb08` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00bbdb0c"></a> `00bbdb0c` | `c1 fa 7f d3` | lsl x1,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdb10"></a> `00bbdb10` | `81 fc ff 54` | b.ne 0x00bbdaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb14"></a> `00bbdb14` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbdb18"></a> `00bbdb18` | `6e 7d 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb1c"></a> `00bbdb1c` | `a0 05 00 b4` | cbz x0,0x00bbdbd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbdb20"></a> `00bbdb20` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00bbdb24"></a> `00bbdb24` | `c0 00 00 54` | b.eq 0x00bbdb3c | `CONDITIONAL_JUMP`
<a id="insn-00bbdb28"></a> `00bbdb28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbdb2c"></a> `00bbdb2c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbdb30"></a> `00bbdb30` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbdb34"></a> `00bbdb34` | `5f 75 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb38"></a> `00bbdb38` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbdb3c"></a> `00bbdb3c` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbdb40"></a> `00bbdb40` | `db ff ff 17` | b 0x00bbdaac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdb44"></a> `00bbdb44` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bbdb48"></a> `00bbdb48` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbdb4c"></a> `00bbdb4c` | `5a 09 00 94` | bl 0x00bc00b4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb50"></a> `00bbdb50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbdb54"></a> `00bbdb54` | `f4 4f 55 a9` | ldp x20,x19,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bbdb58"></a> `00bbdb58` | `f6 57 54 a9` | ldp x22,x21,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00bbdb5c"></a> `00bbdb5c` | `f8 5f 53 a9` | ldp x24,x23,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00bbdb60"></a> `00bbdb60` | `fa 67 52 a9` | ldp x26,x25,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00bbdb64"></a> `00bbdb64` | `fc 6f 51 a9` | ldp x28,x27,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00bbdb68"></a> `00bbdb68` | `fd 7b 50 a9` | ldp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00bbdb6c"></a> `00bbdb6c` | `ff 83 05 91` | add sp,sp,#0x160 | `FALL_THROUGH`
<a id="insn-00bbdb70"></a> `00bbdb70` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbdb74"></a> `00bbdb74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbdb78"></a> `00bbdb78` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdb7c"></a> `00bbdb7c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbdb80"></a> `00bbdb80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbdb84"></a> `00bbdb84` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbdb88"></a> `00bbdb88` | `b7 08 00 94` | bl 0x00bbfe64 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb8c"></a> `00bbdb8c` | `e0 07 02 a9` | stp x0,x1,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbdb90"></a> `00bbdb90` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdb94"></a> `00bbdb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbdb98"></a> `00bbdb98` | `8b 08 00 94` | bl 0x00bbfdc4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdb9c"></a> `00bbdb9c` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbdba0"></a> `00bbdba0` | `4c fe ff 17` | b 0x00bbd4d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdba4"></a> `00bbdba4` | `a0 b6 ff 90` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bbdba8"></a> `00bbdba8` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bbdbac"></a> `00bbdbac` | `21 b7 ff b0` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbdbb0"></a> `00bbdbb0` | `21 f4 01 91` | add x1,x1,#0x7d | `FALL_THROUGH`
<a id="insn-00bbdbb4"></a> `00bbdbb4` | `23 b7 ff b0` | adrp x3,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbdbb8"></a> `00bbdbb8` | `63 dc 02 91` | add x3,x3,#0xb7 | `FALL_THROUGH`
<a id="insn-00bbdbbc"></a> `00bbdbbc` | `e2 10 80 52` | mov w2,#0x87 | `FALL_THROUGH`
<a id="insn-00bbdbc0"></a> `00bbdbc0` | `34 f5 ff 97` | bl 0x00bbb090 | `CALL_TERMINATOR`
<a id="insn-00bbdbc4"></a> `00bbdbc4` | `43 75 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`
<a id="insn-00bbdbc8"></a> `00bbdbc8` | `7e 81 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bbdbcc"></a> `00bbdbcc` | `7d 81 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bbdbd0"></a> `00bbdbd0` | `7c 81 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bbdbd4"></a> `00bbdbd4` | `7b 81 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbd1fc`](#insn-00bbd1fc) 範囲 `[['00bbd1fc', '00bbd1ff']]`
  - `FALL_THROUGH` [`00bbd1fc`](#insn-00bbd1fc) → [`00bbd200`](#insn-00bbd200)
- ブロック [`00bbd200`](#insn-00bbd200) 範囲 `[['00bbd200', '00bbd203']]`
  - `FALL_THROUGH` [`00bbd200`](#insn-00bbd200) → [`00bbd204`](#insn-00bbd204)
- ブロック [`00bbd204`](#insn-00bbd204) 範囲 `[['00bbd204', '00bbd207']]`
  - `FALL_THROUGH` [`00bbd204`](#insn-00bbd204) → [`00bbd208`](#insn-00bbd208)
- ブロック [`00bbd208`](#insn-00bbd208) 範囲 `[['00bbd208', '00bbd20b']]`
  - `FALL_THROUGH` [`00bbd208`](#insn-00bbd208) → [`00bbd20c`](#insn-00bbd20c)
- ブロック [`00bbd20c`](#insn-00bbd20c) 範囲 `[['00bbd20c', '00bbd21b']]`
  - `FALL_THROUGH` [`00bbd218`](#insn-00bbd218) → [`00bbd21c`](#insn-00bbd21c)
- ブロック [`00bbd21c`](#insn-00bbd21c) 範囲 `[['00bbd21c', '00bbd21f']]`
  - `FALL_THROUGH` [`00bbd21c`](#insn-00bbd21c) → [`00bbd220`](#insn-00bbd220)
- ブロック [`00bbd220`](#insn-00bbd220) 範囲 `[['00bbd220', '00bbd223']]`
  - `FALL_THROUGH` [`00bbd220`](#insn-00bbd220) → [`00bbd224`](#insn-00bbd224)
- ブロック [`00bbd224`](#insn-00bbd224) 範囲 `[['00bbd224', '00bbd227']]`
  - `FALL_THROUGH` [`00bbd224`](#insn-00bbd224) → [`00bbd228`](#insn-00bbd228)
- ブロック [`00bbd228`](#insn-00bbd228) 範囲 `[['00bbd228', '00bbd22b']]`
  - `FALL_THROUGH` [`00bbd228`](#insn-00bbd228) → [`00bbd22c`](#insn-00bbd22c)
- ブロック [`00bbd22c`](#insn-00bbd22c) 範囲 `[['00bbd22c', '00bbd22f']]`
  - `FALL_THROUGH` [`00bbd22c`](#insn-00bbd22c) → [`00bbd230`](#insn-00bbd230)
- ブロック [`00bbd230`](#insn-00bbd230) 範囲 `[['00bbd230', '00bbd23b']]`
  - `CONDITIONAL_JUMP` [`00bbd238`](#insn-00bbd238) → [`00bbd2c4`](#insn-00bbd2c4)
  - `FALL_THROUGH` [`00bbd238`](#insn-00bbd238) → [`00bbd23c`](#insn-00bbd23c)
- ブロック [`00bbd23c`](#insn-00bbd23c) 範囲 `[['00bbd23c', '00bbd247']]`
  - `CONDITIONAL_JUMP` [`00bbd244`](#insn-00bbd244) → [`00bbd398`](#insn-00bbd398)
  - `FALL_THROUGH` [`00bbd244`](#insn-00bbd244) → [`00bbd248`](#insn-00bbd248)
- ブロック [`00bbd248`](#insn-00bbd248) 範囲 `[['00bbd248', '00bbd24f']]`
  - `CONDITIONAL_JUMP` [`00bbd24c`](#insn-00bbd24c) → [`00bbd2c4`](#insn-00bbd2c4)
  - `FALL_THROUGH` [`00bbd24c`](#insn-00bbd24c) → [`00bbd250`](#insn-00bbd250)
- ブロック [`00bbd250`](#insn-00bbd250) 範囲 `[['00bbd250', '00bbd257']]`
  - `CONDITIONAL_JUMP` [`00bbd254`](#insn-00bbd254) → [`00bbd76c`](#insn-00bbd76c)
  - `FALL_THROUGH` [`00bbd254`](#insn-00bbd254) → [`00bbd258`](#insn-00bbd258)
- ブロック [`00bbd258`](#insn-00bbd258) 範囲 `[['00bbd258', '00bbd263']]`
  - `CONDITIONAL_JUMP` [`00bbd260`](#insn-00bbd260) → [`00bbd51c`](#insn-00bbd51c)
  - `FALL_THROUGH` [`00bbd260`](#insn-00bbd260) → [`00bbd264`](#insn-00bbd264)
- ブロック [`00bbd264`](#insn-00bbd264) 範囲 `[['00bbd264', '00bbd26b']]`
  - `CONDITIONAL_JUMP` [`00bbd268`](#insn-00bbd268) → [`00bbd734`](#insn-00bbd734)
  - `FALL_THROUGH` [`00bbd268`](#insn-00bbd268) → [`00bbd26c`](#insn-00bbd26c)
- ブロック [`00bbd26c`](#insn-00bbd26c) 範囲 `[['00bbd26c', '00bbd273']]`
  - `CONDITIONAL_JUMP` [`00bbd270`](#insn-00bbd270) → [`00bbd9fc`](#insn-00bbd9fc)
  - `FALL_THROUGH` [`00bbd270`](#insn-00bbd270) → [`00bbd274`](#insn-00bbd274)
- ブロック [`00bbd274`](#insn-00bbd274) 範囲 `[['00bbd274', '00bbd27b']]`
  - `CONDITIONAL_JUMP` [`00bbd278`](#insn-00bbd278) → [`00bbda4c`](#insn-00bbda4c)
  - `FALL_THROUGH` [`00bbd278`](#insn-00bbd278) → [`00bbd27c`](#insn-00bbd27c)
- ブロック [`00bbd27c`](#insn-00bbd27c) 範囲 `[['00bbd27c', '00bbd283']]`
  - `CONDITIONAL_JUMP` [`00bbd280`](#insn-00bbd280) → [`00bbd76c`](#insn-00bbd76c)
  - `FALL_THROUGH` [`00bbd280`](#insn-00bbd280) → [`00bbd284`](#insn-00bbd284)
- ブロック [`00bbd284`](#insn-00bbd284) 範囲 `[['00bbd284', '00bbd297']]`
  - `CONDITIONAL_JUMP` [`00bbd294`](#insn-00bbd294) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd294`](#insn-00bbd294) → [`00bbd298`](#insn-00bbd298)
- ブロック [`00bbd298`](#insn-00bbd298) 範囲 `[['00bbd298', '00bbd2a3']]`
  - `CONDITIONAL_JUMP` [`00bbd2a0`](#insn-00bbd2a0) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd2a0`](#insn-00bbd2a0) → [`00bbd2a4`](#insn-00bbd2a4)
- ブロック [`00bbd2a4`](#insn-00bbd2a4) 範囲 `[['00bbd2a4', '00bbd2a7']]`
  - `FALL_THROUGH` [`00bbd2a4`](#insn-00bbd2a4) → [`00bbd2a8`](#insn-00bbd2a8)
- ブロック [`00bbd2a8`](#insn-00bbd2a8) 範囲 `[['00bbd2a8', '00bbd2ab']]`
  - `FALL_THROUGH` [`00bbd2a8`](#insn-00bbd2a8) → [`00bbd2ac`](#insn-00bbd2ac)
- ブロック [`00bbd2ac`](#insn-00bbd2ac) 範囲 `[['00bbd2ac', '00bbd2af']]`
  - `FALL_THROUGH` [`00bbd2ac`](#insn-00bbd2ac) → [`00bbd2b0`](#insn-00bbd2b0)
- ブロック [`00bbd2b0`](#insn-00bbd2b0) 範囲 `[['00bbd2b0', '00bbd2b3']]`
  - `CONDITIONAL_JUMP` [`00bbd2b0`](#insn-00bbd2b0) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd2b0`](#insn-00bbd2b0) → [`00bbd2b4`](#insn-00bbd2b4)
- ブロック [`00bbd2b4`](#insn-00bbd2b4) 範囲 `[['00bbd2b4', '00bbd2b7']]`
  - `FALL_THROUGH` [`00bbd2b4`](#insn-00bbd2b4) → [`00bbd2b8`](#insn-00bbd2b8)
- ブロック [`00bbd2b8`](#insn-00bbd2b8) 範囲 `[['00bbd2b8', '00bbd2bb']]`
  - `FALL_THROUGH` [`00bbd2b8`](#insn-00bbd2b8) → [`00bbd2bc`](#insn-00bbd2bc)
- ブロック [`00bbd2bc`](#insn-00bbd2bc) 範囲 `[['00bbd2bc', '00bbd2bf']]`
  - `FALL_THROUGH` [`00bbd2bc`](#insn-00bbd2bc) → [`00bbd2c0`](#insn-00bbd2c0)
- ブロック [`00bbd2c0`](#insn-00bbd2c0) 範囲 `[['00bbd2c0', '00bbd2c3']]`
  - `UNCONDITIONAL_JUMP` [`00bbd2c0`](#insn-00bbd2c0) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd2c4`](#insn-00bbd2c4) 範囲 `[['00bbd2c4', '00bbd2c7']]`
  - `FALL_THROUGH` [`00bbd2c4`](#insn-00bbd2c4) → [`00bbd2c8`](#insn-00bbd2c8)
- ブロック [`00bbd2c8`](#insn-00bbd2c8) 範囲 `[['00bbd2c8', '00bbd2cb']]`
  - `FALL_THROUGH` [`00bbd2c8`](#insn-00bbd2c8) → [`00bbd2cc`](#insn-00bbd2cc)
- ブロック [`00bbd2cc`](#insn-00bbd2cc) 範囲 `[['00bbd2cc', '00bbd2cf']]`
  - `FALL_THROUGH` [`00bbd2cc`](#insn-00bbd2cc) → [`00bbd2d0`](#insn-00bbd2d0)
- ブロック [`00bbd2d0`](#insn-00bbd2d0) 範囲 `[['00bbd2d0', '00bbd2d3']]`
  - `FALL_THROUGH` [`00bbd2d0`](#insn-00bbd2d0) → [`00bbd2d4`](#insn-00bbd2d4)
- ブロック [`00bbd2d4`](#insn-00bbd2d4) 範囲 `[['00bbd2d4', '00bbd2d7']]`
  - `FALL_THROUGH` [`00bbd2d4`](#insn-00bbd2d4) → [`00bbd2d8`](#insn-00bbd2d8)
- ブロック [`00bbd2d8`](#insn-00bbd2d8) 範囲 `[['00bbd2d8', '00bbd2db']]`
  - `FALL_THROUGH` [`00bbd2d8`](#insn-00bbd2d8) → [`00bbd2dc`](#insn-00bbd2dc)
- ブロック [`00bbd2dc`](#insn-00bbd2dc) 範囲 `[['00bbd2dc', '00bbd2df']]`
  - `FALL_THROUGH` [`00bbd2dc`](#insn-00bbd2dc) → [`00bbd2e0`](#insn-00bbd2e0)
- ブロック [`00bbd2e0`](#insn-00bbd2e0) 範囲 `[['00bbd2e0', '00bbd2e3']]`
  - `FALL_THROUGH` [`00bbd2e0`](#insn-00bbd2e0) → [`00bbd2e4`](#insn-00bbd2e4)
- ブロック [`00bbd2e4`](#insn-00bbd2e4) 範囲 `[['00bbd2e4', '00bbd303']]`
  - `CONDITIONAL_JUMP` [`00bbd300`](#insn-00bbd300) → [`00bbdb48`](#insn-00bbdb48)
  - `FALL_THROUGH` [`00bbd300`](#insn-00bbd300) → [`00bbd304`](#insn-00bbd304)
- ブロック [`00bbd304`](#insn-00bbd304) 範囲 `[['00bbd304', '00bbd313']]`
  - `FALL_THROUGH` [`00bbd310`](#insn-00bbd310) → [`00bbd314`](#insn-00bbd314)
- ブロック [`00bbd314`](#insn-00bbd314) 範囲 `[['00bbd314', '00bbd317']]`
  - `FALL_THROUGH` [`00bbd314`](#insn-00bbd314) → [`00bbd318`](#insn-00bbd318)
- ブロック [`00bbd318`](#insn-00bbd318) 範囲 `[['00bbd318', '00bbd31b']]`
  - `FALL_THROUGH` [`00bbd318`](#insn-00bbd318) → [`00bbd31c`](#insn-00bbd31c)
- ブロック [`00bbd31c`](#insn-00bbd31c) 範囲 `[['00bbd31c', '00bbd31f']]`
  - `CONDITIONAL_JUMP` [`00bbd31c`](#insn-00bbd31c) → [`00bbd448`](#insn-00bbd448)
  - `FALL_THROUGH` [`00bbd31c`](#insn-00bbd31c) → [`00bbd320`](#insn-00bbd320)
- ブロック [`00bbd320`](#insn-00bbd320) 範囲 `[['00bbd320', '00bbd323']]`
  - `FALL_THROUGH` [`00bbd320`](#insn-00bbd320) → [`00bbd324`](#insn-00bbd324)
- ブロック [`00bbd324`](#insn-00bbd324) 範囲 `[['00bbd324', '00bbd32f']]`
  - `CONDITIONAL_JUMP` [`00bbd32c`](#insn-00bbd32c) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd32c`](#insn-00bbd32c) → [`00bbd330`](#insn-00bbd330)
- ブロック [`00bbd330`](#insn-00bbd330) 範囲 `[['00bbd330', '00bbd337']]`
  - `CONDITIONAL_JUMP` [`00bbd334`](#insn-00bbd334) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd334`](#insn-00bbd334) → [`00bbd338`](#insn-00bbd338)
- ブロック [`00bbd338`](#insn-00bbd338) 範囲 `[['00bbd338', '00bbd34f']]`
  - `CONDITIONAL_JUMP` [`00bbd34c`](#insn-00bbd34c) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd34c`](#insn-00bbd34c) → [`00bbd350`](#insn-00bbd350)
- ブロック [`00bbd350`](#insn-00bbd350) 範囲 `[['00bbd350', '00bbd353']]`
  - `FALL_THROUGH` [`00bbd350`](#insn-00bbd350) → [`00bbd354`](#insn-00bbd354)
- ブロック [`00bbd354`](#insn-00bbd354) 範囲 `[['00bbd354', '00bbd357']]`
  - `FALL_THROUGH` [`00bbd354`](#insn-00bbd354) → [`00bbd358`](#insn-00bbd358)
- ブロック [`00bbd358`](#insn-00bbd358) 範囲 `[['00bbd358', '00bbd363']]`
  - `CONDITIONAL_JUMP` [`00bbd360`](#insn-00bbd360) → [`00bbd450`](#insn-00bbd450)
  - `FALL_THROUGH` [`00bbd360`](#insn-00bbd360) → [`00bbd364`](#insn-00bbd364)
- ブロック [`00bbd364`](#insn-00bbd364) 範囲 `[['00bbd364', '00bbd36f']]`
  - `CONDITIONAL_JUMP` [`00bbd36c`](#insn-00bbd36c) → [`00bbd38c`](#insn-00bbd38c)
  - `FALL_THROUGH` [`00bbd36c`](#insn-00bbd36c) → [`00bbd370`](#insn-00bbd370)
- ブロック [`00bbd370`](#insn-00bbd370) 範囲 `[['00bbd370', '00bbd38b']]`
  - `CONDITIONAL_JUMP` [`00bbd388`](#insn-00bbd388) → [`00bbd354`](#insn-00bbd354)
  - `FALL_THROUGH` [`00bbd388`](#insn-00bbd388) → [`00bbd38c`](#insn-00bbd38c)
- ブロック [`00bbd38c`](#insn-00bbd38c) 範囲 `[['00bbd38c', '00bbd393']]`
  - `CONDITIONAL_JUMP` [`00bbd390`](#insn-00bbd390) → [`00bbd458`](#insn-00bbd458)
  - `FALL_THROUGH` [`00bbd390`](#insn-00bbd390) → [`00bbd394`](#insn-00bbd394)
- ブロック [`00bbd394`](#insn-00bbd394) 範囲 `[['00bbd394', '00bbd397']]`
  - `UNCONDITIONAL_JUMP` [`00bbd394`](#insn-00bbd394) → [`00bbdb44`](#insn-00bbdb44)
- ブロック [`00bbd398`](#insn-00bbd398) 範囲 `[['00bbd398', '00bbd39f']]`
  - `CONDITIONAL_JUMP` [`00bbd39c`](#insn-00bbd39c) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd39c`](#insn-00bbd39c) → [`00bbd3a0`](#insn-00bbd3a0)
- ブロック [`00bbd3a0`](#insn-00bbd3a0) 範囲 `[['00bbd3a0', '00bbd3ab']]`
  - `CONDITIONAL_JUMP` [`00bbd3a8`](#insn-00bbd3a8) → [`00bbd658`](#insn-00bbd658)
  - `FALL_THROUGH` [`00bbd3a8`](#insn-00bbd3a8) → [`00bbd3ac`](#insn-00bbd3ac)
- ブロック [`00bbd3ac`](#insn-00bbd3ac) 範囲 `[['00bbd3ac', '00bbd3b3']]`
  - `CONDITIONAL_JUMP` [`00bbd3b0`](#insn-00bbd3b0) → [`00bbd5a0`](#insn-00bbd5a0)
  - `FALL_THROUGH` [`00bbd3b0`](#insn-00bbd3b0) → [`00bbd3b4`](#insn-00bbd3b4)
- ブロック [`00bbd3b4`](#insn-00bbd3b4) 範囲 `[['00bbd3b4', '00bbd3bb']]`
  - `CONDITIONAL_JUMP` [`00bbd3b8`](#insn-00bbd3b8) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd3b8`](#insn-00bbd3b8) → [`00bbd3bc`](#insn-00bbd3bc)
- ブロック [`00bbd3bc`](#insn-00bbd3bc) 範囲 `[['00bbd3bc', '00bbd3d3']]`
  - `CONDITIONAL_JUMP` [`00bbd3d0`](#insn-00bbd3d0) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd3d0`](#insn-00bbd3d0) → [`00bbd3d4`](#insn-00bbd3d4)
- ブロック [`00bbd3d4`](#insn-00bbd3d4) 範囲 `[['00bbd3d4', '00bbd3db']]`
  - `FALL_THROUGH` [`00bbd3d8`](#insn-00bbd3d8) → [`00bbd3dc`](#insn-00bbd3dc)
- ブロック [`00bbd3dc`](#insn-00bbd3dc) 範囲 `[['00bbd3dc', '00bbd3e7']]`
  - `CONDITIONAL_JUMP` [`00bbd3e4`](#insn-00bbd3e4) → [`00bbd40c`](#insn-00bbd40c)
  - `FALL_THROUGH` [`00bbd3e4`](#insn-00bbd3e4) → [`00bbd3e8`](#insn-00bbd3e8)
- ブロック [`00bbd3e8`](#insn-00bbd3e8) 範囲 `[['00bbd3e8', '00bbd3f7']]`
  - `CONDITIONAL_JUMP` [`00bbd3f4`](#insn-00bbd3f4) → [`00bbdbc4`](#insn-00bbdbc4)
  - `FALL_THROUGH` [`00bbd3f4`](#insn-00bbd3f4) → [`00bbd3f8`](#insn-00bbd3f8)
- ブロック [`00bbd3f8`](#insn-00bbd3f8) 範囲 `[['00bbd3f8', '00bbd40b']]`
  - `FALL_THROUGH` [`00bbd408`](#insn-00bbd408) → [`00bbd40c`](#insn-00bbd40c)
- ブロック [`00bbd40c`](#insn-00bbd40c) 範囲 `[['00bbd40c', '00bbd447']]`
  - `UNCONDITIONAL_JUMP` [`00bbd444`](#insn-00bbd444) → [`00bbd6e8`](#insn-00bbd6e8)
- ブロック [`00bbd448`](#insn-00bbd448) 範囲 `[['00bbd448', '00bbd44f']]`
  - `CONDITIONAL_JUMP` [`00bbd44c`](#insn-00bbd44c) → [`00bbdba4`](#insn-00bbdba4)
  - `FALL_THROUGH` [`00bbd44c`](#insn-00bbd44c) → [`00bbd450`](#insn-00bbd450)
- ブロック [`00bbd450`](#insn-00bbd450) 範囲 `[['00bbd450', '00bbd453']]`
  - `FALL_THROUGH` [`00bbd450`](#insn-00bbd450) → [`00bbd454`](#insn-00bbd454)
- ブロック [`00bbd454`](#insn-00bbd454) 範囲 `[['00bbd454', '00bbd457']]`
  - `FALL_THROUGH` [`00bbd454`](#insn-00bbd454) → [`00bbd458`](#insn-00bbd458)
- ブロック [`00bbd458`](#insn-00bbd458) 範囲 `[['00bbd458', '00bbd463']]`
  - `CONDITIONAL_JUMP` [`00bbd460`](#insn-00bbd460) → [`00bbdb48`](#insn-00bbdb48)
  - `FALL_THROUGH` [`00bbd460`](#insn-00bbd460) → [`00bbd464`](#insn-00bbd464)
- ブロック [`00bbd464`](#insn-00bbd464) 範囲 `[['00bbd464', '00bbd473']]`
  - `CONDITIONAL_JUMP` [`00bbd470`](#insn-00bbd470) → [`00bbd490`](#insn-00bbd490)
  - `FALL_THROUGH` [`00bbd470`](#insn-00bbd470) → [`00bbd474`](#insn-00bbd474)
- ブロック [`00bbd474`](#insn-00bbd474) 範囲 `[['00bbd474', '00bbd48f']]`
  - `CONDITIONAL_JUMP` [`00bbd48c`](#insn-00bbd48c) → [`00bbdb48`](#insn-00bbdb48)
  - `FALL_THROUGH` [`00bbd48c`](#insn-00bbd48c) → [`00bbd490`](#insn-00bbd490)
- ブロック [`00bbd490`](#insn-00bbd490) 範囲 `[['00bbd490', '00bbd49b']]`
  - `CONDITIONAL_JUMP` [`00bbd498`](#insn-00bbd498) → [`00bbd4d0`](#insn-00bbd4d0)
  - `FALL_THROUGH` [`00bbd498`](#insn-00bbd498) → [`00bbd49c`](#insn-00bbd49c)
- ブロック [`00bbd49c`](#insn-00bbd49c) 範囲 `[['00bbd49c', '00bbd4bb']]`
  - `FALL_THROUGH` [`00bbd4b8`](#insn-00bbd4b8) → [`00bbd4bc`](#insn-00bbd4bc)
- ブロック [`00bbd4bc`](#insn-00bbd4bc) 範囲 `[['00bbd4bc', '00bbd4c7']]`
  - `FALL_THROUGH` [`00bbd4c4`](#insn-00bbd4c4) → [`00bbd4c8`](#insn-00bbd4c8)
- ブロック [`00bbd4c8`](#insn-00bbd4c8) 範囲 `[['00bbd4c8', '00bbd4cf']]`
  - `CONDITIONAL_JUMP` [`00bbd4cc`](#insn-00bbd4cc) → [`00bbda84`](#insn-00bbda84)
  - `FALL_THROUGH` [`00bbd4cc`](#insn-00bbd4cc) → [`00bbd4d0`](#insn-00bbd4d0)
- ブロック [`00bbd4d0`](#insn-00bbd4d0) 範囲 `[['00bbd4d0', '00bbd4db']]`
  - `CONDITIONAL_JUMP` [`00bbd4d8`](#insn-00bbd4d8) → [`00bbd4f4`](#insn-00bbd4f4)
  - `FALL_THROUGH` [`00bbd4d8`](#insn-00bbd4d8) → [`00bbd4dc`](#insn-00bbd4dc)
- ブロック [`00bbd4dc`](#insn-00bbd4dc) 範囲 `[['00bbd4dc', '00bbd4e3']]`
  - `CONDITIONAL_JUMP` [`00bbd4e0`](#insn-00bbd4e0) → [`00bbd4f4`](#insn-00bbd4f4)
  - `FALL_THROUGH` [`00bbd4e0`](#insn-00bbd4e0) → [`00bbd4e4`](#insn-00bbd4e4)
- ブロック [`00bbd4e4`](#insn-00bbd4e4) 範囲 `[['00bbd4e4', '00bbd4f3']]`
  - `CONDITIONAL_JUMP` [`00bbd4f0`](#insn-00bbd4f0) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd4f0`](#insn-00bbd4f0) → [`00bbd4f4`](#insn-00bbd4f4)
- ブロック [`00bbd4f4`](#insn-00bbd4f4) 範囲 `[['00bbd4f4', '00bbd503']]`
  - `CONDITIONAL_JUMP` [`00bbd500`](#insn-00bbd500) → [`00bbd7c8`](#insn-00bbd7c8)
  - `FALL_THROUGH` [`00bbd500`](#insn-00bbd500) → [`00bbd504`](#insn-00bbd504)
- ブロック [`00bbd504`](#insn-00bbd504) 範囲 `[['00bbd504', '00bbd50f']]`
  - `CONDITIONAL_JUMP` [`00bbd50c`](#insn-00bbd50c) → [`00bbd7c8`](#insn-00bbd7c8)
  - `FALL_THROUGH` [`00bbd50c`](#insn-00bbd50c) → [`00bbd510`](#insn-00bbd510)
- ブロック [`00bbd510`](#insn-00bbd510) 範囲 `[['00bbd510', '00bbd51b']]`
  - `UNCONDITIONAL_JUMP` [`00bbd518`](#insn-00bbd518) → [`00bbd940`](#insn-00bbd940)
- ブロック [`00bbd51c`](#insn-00bbd51c) 範囲 `[['00bbd51c', '00bbd523']]`
  - `CONDITIONAL_JUMP` [`00bbd520`](#insn-00bbd520) → [`00bbd6fc`](#insn-00bbd6fc)
  - `FALL_THROUGH` [`00bbd520`](#insn-00bbd520) → [`00bbd524`](#insn-00bbd524)
- ブロック [`00bbd524`](#insn-00bbd524) 範囲 `[['00bbd524', '00bbd52b']]`
  - `CONDITIONAL_JUMP` [`00bbd528`](#insn-00bbd528) → [`00bbd9a8`](#insn-00bbd9a8)
  - `FALL_THROUGH` [`00bbd528`](#insn-00bbd528) → [`00bbd52c`](#insn-00bbd52c)
- ブロック [`00bbd52c`](#insn-00bbd52c) 範囲 `[['00bbd52c', '00bbd52f']]`
  - `FALL_THROUGH` [`00bbd52c`](#insn-00bbd52c) → [`00bbd530`](#insn-00bbd530)
- ブロック [`00bbd530`](#insn-00bbd530) 範囲 `[['00bbd530', '00bbd533']]`
  - `CONDITIONAL_JUMP` [`00bbd530`](#insn-00bbd530) → [`00bbd76c`](#insn-00bbd76c)
  - `FALL_THROUGH` [`00bbd530`](#insn-00bbd530) → [`00bbd534`](#insn-00bbd534)
- ブロック [`00bbd534`](#insn-00bbd534) 範囲 `[['00bbd534', '00bbd53b']]`
  - `FALL_THROUGH` [`00bbd538`](#insn-00bbd538) → [`00bbd53c`](#insn-00bbd53c)
- ブロック [`00bbd53c`](#insn-00bbd53c) 範囲 `[['00bbd53c', '00bbd54b']]`
  - `CONDITIONAL_JUMP` [`00bbd548`](#insn-00bbd548) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd548`](#insn-00bbd548) → [`00bbd54c`](#insn-00bbd54c)
- ブロック [`00bbd54c`](#insn-00bbd54c) 範囲 `[['00bbd54c', '00bbd55b']]`
  - `CONDITIONAL_JUMP` [`00bbd558`](#insn-00bbd558) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd558`](#insn-00bbd558) → [`00bbd55c`](#insn-00bbd55c)
- ブロック [`00bbd55c`](#insn-00bbd55c) 範囲 `[['00bbd55c', '00bbd567']]`
  - `CONDITIONAL_JUMP` [`00bbd564`](#insn-00bbd564) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd564`](#insn-00bbd564) → [`00bbd568`](#insn-00bbd568)
- ブロック [`00bbd568`](#insn-00bbd568) 範囲 `[['00bbd568', '00bbd573']]`
  - `CONDITIONAL_JUMP` [`00bbd570`](#insn-00bbd570) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd570`](#insn-00bbd570) → [`00bbd574`](#insn-00bbd574)
- ブロック [`00bbd574`](#insn-00bbd574) 範囲 `[['00bbd574', '00bbd58b']]`
  - `CONDITIONAL_JUMP` [`00bbd588`](#insn-00bbd588) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd588`](#insn-00bbd588) → [`00bbd58c`](#insn-00bbd58c)
- ブロック [`00bbd58c`](#insn-00bbd58c) 範囲 `[['00bbd58c', '00bbd59f']]`
  - `UNCONDITIONAL_JUMP` [`00bbd59c`](#insn-00bbd59c) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd5a0`](#insn-00bbd5a0) 範囲 `[['00bbd5a0', '00bbd5a3']]`
  - `FALL_THROUGH` [`00bbd5a0`](#insn-00bbd5a0) → [`00bbd5a4`](#insn-00bbd5a4)
- ブロック [`00bbd5a4`](#insn-00bbd5a4) 範囲 `[['00bbd5a4', '00bbd5bb']]`
  - `CONDITIONAL_JUMP` [`00bbd5b8`](#insn-00bbd5b8) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd5b8`](#insn-00bbd5b8) → [`00bbd5bc`](#insn-00bbd5bc)
- ブロック [`00bbd5bc`](#insn-00bbd5bc) 範囲 `[['00bbd5bc', '00bbd5c7']]`
  - `CONDITIONAL_JUMP` [`00bbd5c4`](#insn-00bbd5c4) → [`00bbd648`](#insn-00bbd648)
  - `FALL_THROUGH` [`00bbd5c4`](#insn-00bbd5c4) → [`00bbd5c8`](#insn-00bbd5c8)
- ブロック [`00bbd5c8`](#insn-00bbd5c8) 範囲 `[['00bbd5c8', '00bbd5d3']]`
  - `CONDITIONAL_JUMP` [`00bbd5d0`](#insn-00bbd5d0) → [`00bbd5e8`](#insn-00bbd5e8)
  - `FALL_THROUGH` [`00bbd5d0`](#insn-00bbd5d0) → [`00bbd5d4`](#insn-00bbd5d4)
- ブロック [`00bbd5d4`](#insn-00bbd5d4) 範囲 `[['00bbd5d4', '00bbd5db']]`
  - `CONDITIONAL_JUMP` [`00bbd5d8`](#insn-00bbd5d8) → [`00bbd618`](#insn-00bbd618)
  - `FALL_THROUGH` [`00bbd5d8`](#insn-00bbd5d8) → [`00bbd5dc`](#insn-00bbd5dc)
- ブロック [`00bbd5dc`](#insn-00bbd5dc) 範囲 `[['00bbd5dc', '00bbd5e3']]`
  - `FALL_THROUGH` [`00bbd5e0`](#insn-00bbd5e0) → [`00bbd5e4`](#insn-00bbd5e4)
- ブロック [`00bbd5e4`](#insn-00bbd5e4) 範囲 `[['00bbd5e4', '00bbd5e7']]`
  - `CONDITIONAL_JUMP` [`00bbd5e4`](#insn-00bbd5e4) → [`00bbd618`](#insn-00bbd618)
  - `FALL_THROUGH` [`00bbd5e4`](#insn-00bbd5e4) → [`00bbd5e8`](#insn-00bbd5e8)
- ブロック [`00bbd5e8`](#insn-00bbd5e8) 範囲 `[['00bbd5e8', '00bbd5ef']]`
  - `FALL_THROUGH` [`00bbd5ec`](#insn-00bbd5ec) → [`00bbd5f0`](#insn-00bbd5f0)
- ブロック [`00bbd5f0`](#insn-00bbd5f0) 範囲 `[['00bbd5f0', '00bbd5f3']]`
  - `CONDITIONAL_JUMP` [`00bbd5f0`](#insn-00bbd5f0) → [`00bbd644`](#insn-00bbd644)
  - `FALL_THROUGH` [`00bbd5f0`](#insn-00bbd5f0) → [`00bbd5f4`](#insn-00bbd5f4)
- ブロック [`00bbd5f4`](#insn-00bbd5f4) 範囲 `[['00bbd5f4', '00bbd5fb']]`
  - `CONDITIONAL_JUMP` [`00bbd5f8`](#insn-00bbd5f8) → [`00bbd644`](#insn-00bbd644)
  - `FALL_THROUGH` [`00bbd5f8`](#insn-00bbd5f8) → [`00bbd5fc`](#insn-00bbd5fc)
- ブロック [`00bbd5fc`](#insn-00bbd5fc) 範囲 `[['00bbd5fc', '00bbd5ff']]`
  - `FALL_THROUGH` [`00bbd5fc`](#insn-00bbd5fc) → [`00bbd600`](#insn-00bbd600)
- ブロック [`00bbd600`](#insn-00bbd600) 範囲 `[['00bbd600', '00bbd607']]`
  - `UNCONDITIONAL_JUMP` [`00bbd604`](#insn-00bbd604) → [`00bbd648`](#insn-00bbd648)
- ブロック [`00bbd608`](#insn-00bbd608) 範囲 `[['00bbd608', '00bbd617']]`
  - `CONDITIONAL_JUMP` [`00bbd614`](#insn-00bbd614) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd614`](#insn-00bbd614) → [`00bbd618`](#insn-00bbd618)
- ブロック [`00bbd618`](#insn-00bbd618) 範囲 `[['00bbd618', '00bbd623']]`
  - `CONDITIONAL_JUMP` [`00bbd620`](#insn-00bbd620) → [`00bbd638`](#insn-00bbd638)
  - `FALL_THROUGH` [`00bbd620`](#insn-00bbd620) → [`00bbd624`](#insn-00bbd624)
- ブロック [`00bbd624`](#insn-00bbd624) 範囲 `[['00bbd624', '00bbd62b']]`
  - `CONDITIONAL_JUMP` [`00bbd628`](#insn-00bbd628) → [`00bbd608`](#insn-00bbd608)
  - `FALL_THROUGH` [`00bbd628`](#insn-00bbd628) → [`00bbd62c`](#insn-00bbd62c)
- ブロック [`00bbd62c`](#insn-00bbd62c) 範囲 `[['00bbd62c', '00bbd637']]`
  - `CONDITIONAL_JUMP` [`00bbd634`](#insn-00bbd634) → [`00bbd608`](#insn-00bbd608)
  - `FALL_THROUGH` [`00bbd634`](#insn-00bbd634) → [`00bbd638`](#insn-00bbd638)
- ブロック [`00bbd638`](#insn-00bbd638) 範囲 `[['00bbd638', '00bbd643']]`
  - `CONDITIONAL_JUMP` [`00bbd640`](#insn-00bbd640) → [`00bbd5f4`](#insn-00bbd5f4)
  - `FALL_THROUGH` [`00bbd640`](#insn-00bbd640) → [`00bbd644`](#insn-00bbd644)
- ブロック [`00bbd644`](#insn-00bbd644) 範囲 `[['00bbd644', '00bbd647']]`
  - `CONDITIONAL_JUMP` [`00bbd644`](#insn-00bbd644) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd644`](#insn-00bbd644) → [`00bbd648`](#insn-00bbd648)
- ブロック [`00bbd648`](#insn-00bbd648) 範囲 `[['00bbd648', '00bbd657']]`
  - `UNCONDITIONAL_JUMP` [`00bbd654`](#insn-00bbd654) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd658`](#insn-00bbd658) 範囲 `[['00bbd658', '00bbd677']]`
  - `CONDITIONAL_JUMP` [`00bbd674`](#insn-00bbd674) → [`00bbdb48`](#insn-00bbdb48)
  - `FALL_THROUGH` [`00bbd674`](#insn-00bbd674) → [`00bbd678`](#insn-00bbd678)
- ブロック [`00bbd678`](#insn-00bbd678) 範囲 `[['00bbd678', '00bbd67f']]`
  - `CONDITIONAL_JUMP` [`00bbd67c`](#insn-00bbd67c) → [`00bbdb48`](#insn-00bbdb48)
  - `FALL_THROUGH` [`00bbd67c`](#insn-00bbd67c) → [`00bbd680`](#insn-00bbd680)
- ブロック [`00bbd680`](#insn-00bbd680) 範囲 `[['00bbd680', '00bbd693']]`
  - `CONDITIONAL_JUMP` [`00bbd690`](#insn-00bbd690) → [`00bbd6b0`](#insn-00bbd6b0)
  - `FALL_THROUGH` [`00bbd690`](#insn-00bbd690) → [`00bbd694`](#insn-00bbd694)
- ブロック [`00bbd694`](#insn-00bbd694) 範囲 `[['00bbd694', '00bbd69f']]`
  - `CONDITIONAL_JUMP` [`00bbd69c`](#insn-00bbd69c) → [`00bbdbc4`](#insn-00bbdbc4)
  - `FALL_THROUGH` [`00bbd69c`](#insn-00bbd69c) → [`00bbd6a0`](#insn-00bbd6a0)
- ブロック [`00bbd6a0`](#insn-00bbd6a0) 範囲 `[['00bbd6a0', '00bbd6af']]`
  - `FALL_THROUGH` [`00bbd6ac`](#insn-00bbd6ac) → [`00bbd6b0`](#insn-00bbd6b0)
- ブロック [`00bbd6b0`](#insn-00bbd6b0) 範囲 `[['00bbd6b0', '00bbd6c7']]`
  - `FALL_THROUGH` [`00bbd6c4`](#insn-00bbd6c4) → [`00bbd6c8`](#insn-00bbd6c8)
- ブロック [`00bbd6c8`](#insn-00bbd6c8) 範囲 `[['00bbd6c8', '00bbd6d3']]`
  - `FALL_THROUGH` [`00bbd6d0`](#insn-00bbd6d0) → [`00bbd6d4`](#insn-00bbd6d4)
- ブロック [`00bbd6d4`](#insn-00bbd6d4) 範囲 `[['00bbd6d4', '00bbd6e7']]`
  - `FALL_THROUGH` [`00bbd6e4`](#insn-00bbd6e4) → [`00bbd6e8`](#insn-00bbd6e8)
- ブロック [`00bbd6e8`](#insn-00bbd6e8) 範囲 `[['00bbd6e8', '00bbd6fb']]`
  - `UNCONDITIONAL_JUMP` [`00bbd6f8`](#insn-00bbd6f8) → [`00bbdb48`](#insn-00bbdb48)
- ブロック [`00bbd6fc`](#insn-00bbd6fc) 範囲 `[['00bbd6fc', '00bbd703']]`
  - `CONDITIONAL_JUMP` [`00bbd700`](#insn-00bbd700) → [`00bbd9d0`](#insn-00bbd9d0)
  - `FALL_THROUGH` [`00bbd700`](#insn-00bbd700) → [`00bbd704`](#insn-00bbd704)
- ブロック [`00bbd704`](#insn-00bbd704) 範囲 `[['00bbd704', '00bbd70b']]`
  - `CONDITIONAL_JUMP` [`00bbd708`](#insn-00bbd708) → [`00bbd76c`](#insn-00bbd76c)
  - `FALL_THROUGH` [`00bbd708`](#insn-00bbd708) → [`00bbd70c`](#insn-00bbd70c)
- ブロック [`00bbd70c`](#insn-00bbd70c) 範囲 `[['00bbd70c', '00bbd723']]`
  - `CONDITIONAL_JUMP` [`00bbd720`](#insn-00bbd720) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd720`](#insn-00bbd720) → [`00bbd724`](#insn-00bbd724)
- ブロック [`00bbd724`](#insn-00bbd724) 範囲 `[['00bbd724', '00bbd72b']]`
  - `FALL_THROUGH` [`00bbd728`](#insn-00bbd728) → [`00bbd72c`](#insn-00bbd72c)
- ブロック [`00bbd72c`](#insn-00bbd72c) 範囲 `[['00bbd72c', '00bbd733']]`
  - `UNCONDITIONAL_JUMP` [`00bbd730`](#insn-00bbd730) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd734`](#insn-00bbd734) 範囲 `[['00bbd734', '00bbd73b']]`
  - `CONDITIONAL_JUMP` [`00bbd738`](#insn-00bbd738) → [`00bbda24`](#insn-00bbda24)
  - `FALL_THROUGH` [`00bbd738`](#insn-00bbd738) → [`00bbd73c`](#insn-00bbd73c)
- ブロック [`00bbd73c`](#insn-00bbd73c) 範囲 `[['00bbd73c', '00bbd743']]`
  - `CONDITIONAL_JUMP` [`00bbd740`](#insn-00bbd740) → [`00bbd76c`](#insn-00bbd76c)
  - `FALL_THROUGH` [`00bbd740`](#insn-00bbd740) → [`00bbd744`](#insn-00bbd744)
- ブロック [`00bbd744`](#insn-00bbd744) 範囲 `[['00bbd744', '00bbd75b']]`
  - `CONDITIONAL_JUMP` [`00bbd758`](#insn-00bbd758) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd758`](#insn-00bbd758) → [`00bbd75c`](#insn-00bbd75c)
- ブロック [`00bbd75c`](#insn-00bbd75c) 範囲 `[['00bbd75c', '00bbd76b']]`
  - `UNCONDITIONAL_JUMP` [`00bbd768`](#insn-00bbd768) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd76c`](#insn-00bbd76c) 範囲 `[['00bbd76c', '00bbd777']]`
  - `FALL_THROUGH` [`00bbd774`](#insn-00bbd774) → [`00bbd778`](#insn-00bbd778)
- ブロック [`00bbd778`](#insn-00bbd778) 範囲 `[['00bbd778', '00bbd77b']]`
  - `CONDITIONAL_JUMP` [`00bbd778`](#insn-00bbd778) → [`00bbd78c`](#insn-00bbd78c)
  - `FALL_THROUGH` [`00bbd778`](#insn-00bbd778) → [`00bbd77c`](#insn-00bbd77c)
- ブロック [`00bbd77c`](#insn-00bbd77c) 範囲 `[['00bbd77c', '00bbd787']]`
  - `FALL_THROUGH` [`00bbd784`](#insn-00bbd784) → [`00bbd788`](#insn-00bbd788)
- ブロック [`00bbd788`](#insn-00bbd788) 範囲 `[['00bbd788', '00bbd78b']]`
  - `UNCONDITIONAL_JUMP` [`00bbd788`](#insn-00bbd788) → [`00bbd790`](#insn-00bbd790)
- ブロック [`00bbd78c`](#insn-00bbd78c) 範囲 `[['00bbd78c', '00bbd78f']]`
  - `FALL_THROUGH` [`00bbd78c`](#insn-00bbd78c) → [`00bbd790`](#insn-00bbd790)
- ブロック [`00bbd790`](#insn-00bbd790) 範囲 `[['00bbd790', '00bbd79b']]`
  - `CONDITIONAL_JUMP` [`00bbd798`](#insn-00bbd798) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd798`](#insn-00bbd798) → [`00bbd79c`](#insn-00bbd79c)
- ブロック [`00bbd79c`](#insn-00bbd79c) 範囲 `[['00bbd79c', '00bbd7ab']]`
  - `CONDITIONAL_JUMP` [`00bbd7a8`](#insn-00bbd7a8) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd7a8`](#insn-00bbd7a8) → [`00bbd7ac`](#insn-00bbd7ac)
- ブロック [`00bbd7ac`](#insn-00bbd7ac) 範囲 `[['00bbd7ac', '00bbd7b7']]`
  - `CONDITIONAL_JUMP` [`00bbd7b4`](#insn-00bbd7b4) → [`00bbd7c0`](#insn-00bbd7c0)
  - `FALL_THROUGH` [`00bbd7b4`](#insn-00bbd7b4) → [`00bbd7b8`](#insn-00bbd7b8)
- ブロック [`00bbd7b8`](#insn-00bbd7b8) 範囲 `[['00bbd7b8', '00bbd7bf']]`
  - `UNCONDITIONAL_JUMP` [`00bbd7bc`](#insn-00bbd7bc) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd7c0`](#insn-00bbd7c0) 範囲 `[['00bbd7c0', '00bbd7c7']]`
  - `UNCONDITIONAL_JUMP` [`00bbd7c4`](#insn-00bbd7c4) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd7c8`](#insn-00bbd7c8) 範囲 `[['00bbd7c8', '00bbd7f3']]`
  - `FALL_THROUGH` [`00bbd7f0`](#insn-00bbd7f0) → [`00bbd7f4`](#insn-00bbd7f4)
- ブロック [`00bbd7f4`](#insn-00bbd7f4) 範囲 `[['00bbd7f4', '00bbd803']]`
  - `CONDITIONAL_JUMP` [`00bbd800`](#insn-00bbd800) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd800`](#insn-00bbd800) → [`00bbd804`](#insn-00bbd804)
- ブロック [`00bbd804`](#insn-00bbd804) 範囲 `[['00bbd804', '00bbd80f']]`
  - `CONDITIONAL_JUMP` [`00bbd80c`](#insn-00bbd80c) → [`00bbd88c`](#insn-00bbd88c)
  - `FALL_THROUGH` [`00bbd80c`](#insn-00bbd80c) → [`00bbd810`](#insn-00bbd810)
- ブロック [`00bbd810`](#insn-00bbd810) 範囲 `[['00bbd810', '00bbd81f']]`
  - `CONDITIONAL_JUMP` [`00bbd81c`](#insn-00bbd81c) → [`00bbd88c`](#insn-00bbd88c)
  - `FALL_THROUGH` [`00bbd81c`](#insn-00bbd81c) → [`00bbd820`](#insn-00bbd820)
- ブロック [`00bbd820`](#insn-00bbd820) 範囲 `[['00bbd820', '00bbd833']]`
  - `CONDITIONAL_JUMP` [`00bbd830`](#insn-00bbd830) → [`00bbd850`](#insn-00bbd850)
  - `FALL_THROUGH` [`00bbd830`](#insn-00bbd830) → [`00bbd834`](#insn-00bbd834)
- ブロック [`00bbd834`](#insn-00bbd834) 範囲 `[['00bbd834', '00bbd83f']]`
  - `CONDITIONAL_JUMP` [`00bbd83c`](#insn-00bbd83c) → [`00bbdbc4`](#insn-00bbdbc4)
  - `FALL_THROUGH` [`00bbd83c`](#insn-00bbd83c) → [`00bbd840`](#insn-00bbd840)
- ブロック [`00bbd840`](#insn-00bbd840) 範囲 `[['00bbd840', '00bbd84f']]`
  - `FALL_THROUGH` [`00bbd84c`](#insn-00bbd84c) → [`00bbd850`](#insn-00bbd850)
- ブロック [`00bbd850`](#insn-00bbd850) 範囲 `[['00bbd850', '00bbd877']]`
  - `FALL_THROUGH` [`00bbd874`](#insn-00bbd874) → [`00bbd878`](#insn-00bbd878)
- ブロック [`00bbd878`](#insn-00bbd878) 範囲 `[['00bbd878', '00bbd88b']]`
  - `FALL_THROUGH` [`00bbd888`](#insn-00bbd888) → [`00bbd88c`](#insn-00bbd88c)
- ブロック [`00bbd88c`](#insn-00bbd88c) 範囲 `[['00bbd88c', '00bbd897']]`
  - `CONDITIONAL_JUMP` [`00bbd894`](#insn-00bbd894) → [`00bbd8f8`](#insn-00bbd8f8)
  - `FALL_THROUGH` [`00bbd894`](#insn-00bbd894) → [`00bbd898`](#insn-00bbd898)
- ブロック [`00bbd898`](#insn-00bbd898) 範囲 `[['00bbd898', '00bbd8ab']]`
  - `CONDITIONAL_JUMP` [`00bbd8a8`](#insn-00bbd8a8) → [`00bbd8bc`](#insn-00bbd8bc)
  - `FALL_THROUGH` [`00bbd8a8`](#insn-00bbd8a8) → [`00bbd8ac`](#insn-00bbd8ac)
- ブロック [`00bbd8ac`](#insn-00bbd8ac) 範囲 `[['00bbd8ac', '00bbd8b7']]`
  - `CONDITIONAL_JUMP` [`00bbd8b4`](#insn-00bbd8b4) → [`00bbd8e8`](#insn-00bbd8e8)
  - `FALL_THROUGH` [`00bbd8b4`](#insn-00bbd8b4) → [`00bbd8b8`](#insn-00bbd8b8)
- ブロック [`00bbd8b8`](#insn-00bbd8b8) 範囲 `[['00bbd8b8', '00bbd8bb']]`
  - `UNCONDITIONAL_JUMP` [`00bbd8b8`](#insn-00bbd8b8) → [`00bbdbcc`](#insn-00bbdbcc)
- ブロック [`00bbd8bc`](#insn-00bbd8bc) 範囲 `[['00bbd8bc', '00bbd8c3']]`
  - `FALL_THROUGH` [`00bbd8c0`](#insn-00bbd8c0) → [`00bbd8c4`](#insn-00bbd8c4)
- ブロック [`00bbd8c4`](#insn-00bbd8c4) 範囲 `[['00bbd8c4', '00bbd8c7']]`
  - `CONDITIONAL_JUMP` [`00bbd8c4`](#insn-00bbd8c4) → [`00bbdbd4`](#insn-00bbdbd4)
  - `FALL_THROUGH` [`00bbd8c4`](#insn-00bbd8c4) → [`00bbd8c8`](#insn-00bbd8c8)
- ブロック [`00bbd8c8`](#insn-00bbd8c8) 範囲 `[['00bbd8c8', '00bbd8cf']]`
  - `CONDITIONAL_JUMP` [`00bbd8cc`](#insn-00bbd8cc) → [`00bbd8e4`](#insn-00bbd8e4)
  - `FALL_THROUGH` [`00bbd8cc`](#insn-00bbd8cc) → [`00bbd8d0`](#insn-00bbd8d0)
- ブロック [`00bbd8d0`](#insn-00bbd8d0) 範囲 `[['00bbd8d0', '00bbd8d3']]`
  - `FALL_THROUGH` [`00bbd8d0`](#insn-00bbd8d0) → [`00bbd8d4`](#insn-00bbd8d4)
- ブロック [`00bbd8d4`](#insn-00bbd8d4) 範囲 `[['00bbd8d4', '00bbd8e3']]`
  - `FALL_THROUGH` [`00bbd8e0`](#insn-00bbd8e0) → [`00bbd8e4`](#insn-00bbd8e4)
- ブロック [`00bbd8e4`](#insn-00bbd8e4) 範囲 `[['00bbd8e4', '00bbd8e7']]`
  - `FALL_THROUGH` [`00bbd8e4`](#insn-00bbd8e4) → [`00bbd8e8`](#insn-00bbd8e8)
- ブロック [`00bbd8e8`](#insn-00bbd8e8) 範囲 `[['00bbd8e8', '00bbd8f7']]`
  - `FALL_THROUGH` [`00bbd8f4`](#insn-00bbd8f4) → [`00bbd8f8`](#insn-00bbd8f8)
- ブロック [`00bbd8f8`](#insn-00bbd8f8) 範囲 `[['00bbd8f8', '00bbd90f']]`
  - `CONDITIONAL_JUMP` [`00bbd90c`](#insn-00bbd90c) → [`00bbd92c`](#insn-00bbd92c)
  - `FALL_THROUGH` [`00bbd90c`](#insn-00bbd90c) → [`00bbd910`](#insn-00bbd910)
- ブロック [`00bbd910`](#insn-00bbd910) 範囲 `[['00bbd910', '00bbd91f']]`
  - `CONDITIONAL_JUMP` [`00bbd91c`](#insn-00bbd91c) → [`00bbd7f4`](#insn-00bbd7f4)
  - `FALL_THROUGH` [`00bbd91c`](#insn-00bbd91c) → [`00bbd920`](#insn-00bbd920)
- ブロック [`00bbd920`](#insn-00bbd920) 範囲 `[['00bbd920', '00bbd92b']]`
  - `CONDITIONAL_JUMP` [`00bbd928`](#insn-00bbd928) → [`00bbd7f4`](#insn-00bbd7f4)
  - `FALL_THROUGH` [`00bbd928`](#insn-00bbd928) → [`00bbd92c`](#insn-00bbd92c)
- ブロック [`00bbd92c`](#insn-00bbd92c) 範囲 `[['00bbd92c', '00bbd93f']]`
  - `FALL_THROUGH` [`00bbd93c`](#insn-00bbd93c) → [`00bbd940`](#insn-00bbd940)
- ブロック [`00bbd940`](#insn-00bbd940) 範囲 `[['00bbd940', '00bbd94b']]`
  - `CONDITIONAL_JUMP` [`00bbd948`](#insn-00bbd948) → [`00bbd980`](#insn-00bbd980)
  - `FALL_THROUGH` [`00bbd948`](#insn-00bbd948) → [`00bbd94c`](#insn-00bbd94c)
- ブロック [`00bbd94c`](#insn-00bbd94c) 範囲 `[['00bbd94c', '00bbd94f']]`
  - `FALL_THROUGH` [`00bbd94c`](#insn-00bbd94c) → [`00bbd950`](#insn-00bbd950)
- ブロック [`00bbd950`](#insn-00bbd950) 範囲 `[['00bbd950', '00bbd957']]`
  - `CONDITIONAL_JUMP` [`00bbd954`](#insn-00bbd954) → [`00bbd980`](#insn-00bbd980)
  - `FALL_THROUGH` [`00bbd954`](#insn-00bbd954) → [`00bbd958`](#insn-00bbd958)
- ブロック [`00bbd958`](#insn-00bbd958) 範囲 `[['00bbd958', '00bbd95b']]`
  - `FALL_THROUGH` [`00bbd958`](#insn-00bbd958) → [`00bbd95c`](#insn-00bbd95c)
- ブロック [`00bbd95c`](#insn-00bbd95c) 範囲 `[['00bbd95c', '00bbd97f']]`
  - `CONDITIONAL_JUMP` [`00bbd97c`](#insn-00bbd97c) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd97c`](#insn-00bbd97c) → [`00bbd980`](#insn-00bbd980)
- ブロック [`00bbd980`](#insn-00bbd980) 範囲 `[['00bbd980', '00bbd9a7']]`
  - `UNCONDITIONAL_JUMP` [`00bbd9a4`](#insn-00bbd9a4) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd9a8`](#insn-00bbd9a8) 範囲 `[['00bbd9a8', '00bbd9bf']]`
  - `CONDITIONAL_JUMP` [`00bbd9bc`](#insn-00bbd9bc) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd9bc`](#insn-00bbd9bc) → [`00bbd9c0`](#insn-00bbd9c0)
- ブロック [`00bbd9c0`](#insn-00bbd9c0) 範囲 `[['00bbd9c0', '00bbd9c3']]`
  - `FALL_THROUGH` [`00bbd9c0`](#insn-00bbd9c0) → [`00bbd9c4`](#insn-00bbd9c4)
- ブロック [`00bbd9c4`](#insn-00bbd9c4) 範囲 `[['00bbd9c4', '00bbd9cf']]`
  - `UNCONDITIONAL_JUMP` [`00bbd9cc`](#insn-00bbd9cc) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd9d0`](#insn-00bbd9d0) 範囲 `[['00bbd9d0', '00bbd9eb']]`
  - `CONDITIONAL_JUMP` [`00bbd9e8`](#insn-00bbd9e8) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbd9e8`](#insn-00bbd9e8) → [`00bbd9ec`](#insn-00bbd9ec)
- ブロック [`00bbd9ec`](#insn-00bbd9ec) 範囲 `[['00bbd9ec', '00bbd9fb']]`
  - `UNCONDITIONAL_JUMP` [`00bbd9f8`](#insn-00bbd9f8) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbd9fc`](#insn-00bbd9fc) 範囲 `[['00bbd9fc', '00bbd9ff']]`
  - `FALL_THROUGH` [`00bbd9fc`](#insn-00bbd9fc) → [`00bbda00`](#insn-00bbda00)
- ブロック [`00bbda00`](#insn-00bbda00) 範囲 `[['00bbda00', '00bbda0b']]`
  - `FALL_THROUGH` [`00bbda08`](#insn-00bbda08) → [`00bbda0c`](#insn-00bbda0c)
- ブロック [`00bbda0c`](#insn-00bbda0c) 範囲 `[['00bbda0c', '00bbda13']]`
  - `CONDITIONAL_JUMP` [`00bbda10`](#insn-00bbda10) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbda10`](#insn-00bbda10) → [`00bbda14`](#insn-00bbda14)
- ブロック [`00bbda14`](#insn-00bbda14) 範囲 `[['00bbda14', '00bbda1b']]`
  - `FALL_THROUGH` [`00bbda18`](#insn-00bbda18) → [`00bbda1c`](#insn-00bbda1c)
- ブロック [`00bbda1c`](#insn-00bbda1c) 範囲 `[['00bbda1c', '00bbda23']]`
  - `UNCONDITIONAL_JUMP` [`00bbda20`](#insn-00bbda20) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbda24`](#insn-00bbda24) 範囲 `[['00bbda24', '00bbda3b']]`
  - `CONDITIONAL_JUMP` [`00bbda38`](#insn-00bbda38) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbda38`](#insn-00bbda38) → [`00bbda3c`](#insn-00bbda3c)
- ブロック [`00bbda3c`](#insn-00bbda3c) 範囲 `[['00bbda3c', '00bbda4b']]`
  - `UNCONDITIONAL_JUMP` [`00bbda48`](#insn-00bbda48) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbda4c`](#insn-00bbda4c) 範囲 `[['00bbda4c', '00bbda67']]`
  - `CONDITIONAL_JUMP` [`00bbda64`](#insn-00bbda64) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbda64`](#insn-00bbda64) → [`00bbda68`](#insn-00bbda68)
- ブロック [`00bbda68`](#insn-00bbda68) 範囲 `[['00bbda68', '00bbda7b']]`
  - `FALL_THROUGH` [`00bbda78`](#insn-00bbda78) → [`00bbda7c`](#insn-00bbda7c)
- ブロック [`00bbda7c`](#insn-00bbda7c) 範囲 `[['00bbda7c', '00bbda83']]`
  - `UNCONDITIONAL_JUMP` [`00bbda80`](#insn-00bbda80) → [`00bbdb48`](#insn-00bbdb48)
- ブロック [`00bbda84`](#insn-00bbda84) 範囲 `[['00bbda84', '00bbda97']]`
  - `FALL_THROUGH` [`00bbda94`](#insn-00bbda94) → [`00bbda98`](#insn-00bbda98)
- ブロック [`00bbda98`](#insn-00bbda98) 範囲 `[['00bbda98', '00bbda9f']]`
  - `UNCONDITIONAL_JUMP` [`00bbda9c`](#insn-00bbda9c) → [`00bbdad0`](#insn-00bbdad0)
- ブロック [`00bbdaa0`](#insn-00bbdaa0) 範囲 `[['00bbdaa0', '00bbdaa3']]`
  - `FALL_THROUGH` [`00bbdaa0`](#insn-00bbdaa0) → [`00bbdaa4`](#insn-00bbdaa4)
- ブロック [`00bbdaa4`](#insn-00bbdaa4) 範囲 `[['00bbdaa4', '00bbdaab']]`
  - `CONDITIONAL_JUMP` [`00bbdaa8`](#insn-00bbdaa8) → [`00bbdbc8`](#insn-00bbdbc8)
  - `FALL_THROUGH` [`00bbdaa8`](#insn-00bbdaa8) → [`00bbdaac`](#insn-00bbdaac)
- ブロック [`00bbdaac`](#insn-00bbdaac) 範囲 `[['00bbdaac', '00bbdabf']]`
  - `FALL_THROUGH` [`00bbdabc`](#insn-00bbdabc) → [`00bbdac0`](#insn-00bbdac0)
- ブロック [`00bbdac0`](#insn-00bbdac0) 範囲 `[['00bbdac0', '00bbdacf']]`
  - `FALL_THROUGH` [`00bbdacc`](#insn-00bbdacc) → [`00bbdad0`](#insn-00bbdad0)
- ブロック [`00bbdad0`](#insn-00bbdad0) 範囲 `[['00bbdad0', '00bbdad7']]`
  - `CONDITIONAL_JUMP` [`00bbdad4`](#insn-00bbdad4) → [`00bbdae4`](#insn-00bbdae4)
  - `FALL_THROUGH` [`00bbdad4`](#insn-00bbdad4) → [`00bbdad8`](#insn-00bbdad8)
- ブロック [`00bbdad8`](#insn-00bbdad8) 範囲 `[['00bbdad8', '00bbdae3']]`
  - `CONDITIONAL_JUMP` [`00bbdae0`](#insn-00bbdae0) → [`00bbdb78`](#insn-00bbdb78)
  - `FALL_THROUGH` [`00bbdae0`](#insn-00bbdae0) → [`00bbdae4`](#insn-00bbdae4)
- ブロック [`00bbdae4`](#insn-00bbdae4) 範囲 `[['00bbdae4', '00bbdaef']]`
  - `CONDITIONAL_JUMP` [`00bbdaec`](#insn-00bbdaec) → [`00bbdb44`](#insn-00bbdb44)
  - `FALL_THROUGH` [`00bbdaec`](#insn-00bbdaec) → [`00bbdaf0`](#insn-00bbdaf0)
- ブロック [`00bbdaf0`](#insn-00bbdaf0) 範囲 `[['00bbdaf0', '00bbdafb']]`
  - `CONDITIONAL_JUMP` [`00bbdaf8`](#insn-00bbdaf8) → [`00bbdac0`](#insn-00bbdac0)
  - `FALL_THROUGH` [`00bbdaf8`](#insn-00bbdaf8) → [`00bbdafc`](#insn-00bbdafc)
- ブロック [`00bbdafc`](#insn-00bbdafc) 範囲 `[['00bbdafc', '00bbdb13']]`
  - `CONDITIONAL_JUMP` [`00bbdb10`](#insn-00bbdb10) → [`00bbdaa0`](#insn-00bbdaa0)
  - `FALL_THROUGH` [`00bbdb10`](#insn-00bbdb10) → [`00bbdb14`](#insn-00bbdb14)
- ブロック [`00bbdb14`](#insn-00bbdb14) 範囲 `[['00bbdb14', '00bbdb1f']]`
  - `CONDITIONAL_JUMP` [`00bbdb1c`](#insn-00bbdb1c) → [`00bbdbd0`](#insn-00bbdbd0)
  - `FALL_THROUGH` [`00bbdb1c`](#insn-00bbdb1c) → [`00bbdb20`](#insn-00bbdb20)
- ブロック [`00bbdb20`](#insn-00bbdb20) 範囲 `[['00bbdb20', '00bbdb27']]`
  - `CONDITIONAL_JUMP` [`00bbdb24`](#insn-00bbdb24) → [`00bbdb3c`](#insn-00bbdb3c)
  - `FALL_THROUGH` [`00bbdb24`](#insn-00bbdb24) → [`00bbdb28`](#insn-00bbdb28)
- ブロック [`00bbdb28`](#insn-00bbdb28) 範囲 `[['00bbdb28', '00bbdb2f']]`
  - `FALL_THROUGH` [`00bbdb2c`](#insn-00bbdb2c) → [`00bbdb30`](#insn-00bbdb30)
- ブロック [`00bbdb30`](#insn-00bbdb30) 範囲 `[['00bbdb30', '00bbdb3b']]`
  - `FALL_THROUGH` [`00bbdb38`](#insn-00bbdb38) → [`00bbdb3c`](#insn-00bbdb3c)
- ブロック [`00bbdb3c`](#insn-00bbdb3c) 範囲 `[['00bbdb3c', '00bbdb43']]`
  - `UNCONDITIONAL_JUMP` [`00bbdb40`](#insn-00bbdb40) → [`00bbdaac`](#insn-00bbdaac)
- ブロック [`00bbdb44`](#insn-00bbdb44) 範囲 `[['00bbdb44', '00bbdb47']]`
  - `FALL_THROUGH` [`00bbdb44`](#insn-00bbdb44) → [`00bbdb48`](#insn-00bbdb48)
- ブロック [`00bbdb48`](#insn-00bbdb48) 範囲 `[['00bbdb48', '00bbdb77']]`
- ブロック [`00bbdb78`](#insn-00bbdb78) 範囲 `[['00bbdb78', '00bbdba3']]`
  - `UNCONDITIONAL_JUMP` [`00bbdba0`](#insn-00bbdba0) → [`00bbd4d0`](#insn-00bbd4d0)
- ブロック [`00bbdba4`](#insn-00bbdba4) 範囲 `[['00bbdba4', '00bbdbab']]`
  - `FALL_THROUGH` [`00bbdba8`](#insn-00bbdba8) → [`00bbdbac`](#insn-00bbdbac)
- ブロック [`00bbdbac`](#insn-00bbdbac) 範囲 `[['00bbdbac', '00bbdbb7']]`
  - `FALL_THROUGH` [`00bbdbb4`](#insn-00bbdbb4) → [`00bbdbb8`](#insn-00bbdbb8)
- ブロック [`00bbdbb8`](#insn-00bbdbb8) 範囲 `[['00bbdbb8', '00bbdbc3']]`
- ブロック [`00bbdbc4`](#insn-00bbdbc4) 範囲 `[['00bbdbc4', '00bbdbc7']]`
- ブロック [`00bbdbc8`](#insn-00bbdbc8) 範囲 `[['00bbdbc8', '00bbdbcb']]`
- ブロック [`00bbdbcc`](#insn-00bbdbcc) 範囲 `[['00bbdbcc', '00bbdbcf']]`
- ブロック [`00bbdbd0`](#insn-00bbdbd0) 範囲 `[['00bbdbd0', '00bbdbd3']]`
- ブロック [`00bbdbd4`](#insn-00bbdbd4) 範囲 `[['00bbdbd4', '00bbdbd7']]`

## 命令位置別の参照

- [`00bbd204`](#insn-00bbd204) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd208`](#insn-00bbd208) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd20c`](#insn-00bbd20c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd210`](#insn-00bbd210) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd214`](#insn-00bbd214) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd218`](#insn-00bbd218) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd22c`](#insn-00bbd22c) → [`00bbf0e8`](../00bbf/00bbf0e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf0e8` · 推定シンボル `None` · 推定型 `None`
- [`00bbd238`](#insn-00bbd238) → [`00bbd2c4`](#insn-00bbd2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd244`](#insn-00bbd244) → [`00bbd398`](#insn-00bbd398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd24c`](#insn-00bbd24c) → [`00bbd2c4`](#insn-00bbd2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd254`](#insn-00bbd254) → [`00bbd76c`](#insn-00bbd76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd260`](#insn-00bbd260) → [`00bbd51c`](#insn-00bbd51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd268`](#insn-00bbd268) → [`00bbd734`](#insn-00bbd734) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd270`](#insn-00bbd270) → [`00bbd9fc`](#insn-00bbd9fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd278`](#insn-00bbd278) → [`00bbda4c`](#insn-00bbda4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd280`](#insn-00bbd280) → [`00bbd76c`](#insn-00bbd76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd290`](#insn-00bbd290) → [`00bc0604`](../00bc0/00bc0604.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0604` · 推定シンボル `None` · 推定型 `None`
- [`00bbd294`](#insn-00bbd294) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd29c`](#insn-00bbd29c) → [`00bc0604`](../00bc0/00bc0604.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0604` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2a0`](#insn-00bbd2a0) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2a8`](#insn-00bbd2a8) → [`00bbd1fc`](#insn-00bbd1fc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd1fc` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2ac`](#insn-00bbd2ac) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2b0`](#insn-00bbd2b0) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2bc`](#insn-00bbd2bc) → [`00bc07b4`](../00bc0/00bc07b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc07b4` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2c0`](#insn-00bbd2c0) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2d0`](#insn-00bbd2d0) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2d8`](#insn-00bbd2d8) → `Stack[-0x11c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2e0`](#insn-00bbd2e0) → `Stack[-0x118]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2e4`](#insn-00bbd2e4) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2e8`](#insn-00bbd2e8) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2f4`](#insn-00bbd2f4) → [`00bbf290`](../00bbf/00bbf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf290` · 推定シンボル `None` · 推定型 `None`
- [`00bbd2fc`](#insn-00bbd2fc) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd300`](#insn-00bbd300) → [`00bbdb48`](#insn-00bbdb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd310`](#insn-00bbd310) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd31c`](#insn-00bbd31c) → [`00bbd448`](#insn-00bbd448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd32c`](#insn-00bbd32c) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd334`](#insn-00bbd334) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd34c`](#insn-00bbd34c) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd360`](#insn-00bbd360) → [`00bbd450`](#insn-00bbd450) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd36c`](#insn-00bbd36c) → [`00bbd38c`](#insn-00bbd38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd388`](#insn-00bbd388) → [`00bbd354`](#insn-00bbd354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd390`](#insn-00bbd390) → [`00bbd458`](#insn-00bbd458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd394`](#insn-00bbd394) → [`00bbdb44`](#insn-00bbdb44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd39c`](#insn-00bbd39c) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3a8`](#insn-00bbd3a8) → [`00bbd658`](#insn-00bbd658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3b0`](#insn-00bbd3b0) → [`00bbd5a0`](#insn-00bbd5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3b8`](#insn-00bbd3b8) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3cc`](#insn-00bbd3cc) → [`00bbf290`](../00bbf/00bbf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf290` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3d0`](#insn-00bbd3d0) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3e4`](#insn-00bbd3e4) → [`00bbd40c`](#insn-00bbd40c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3f0`](#insn-00bbd3f0) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd3f4`](#insn-00bbd3f4) → [`00bbdbc4`](#insn-00bbdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd424`](#insn-00bbd424) → `00c176a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbd444`](#insn-00bbd444) → [`00bbd6e8`](#insn-00bbd6e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd44c`](#insn-00bbd44c) → [`00bbdba4`](#insn-00bbdba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd460`](#insn-00bbd460) → [`00bbdb48`](#insn-00bbdb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd470`](#insn-00bbd470) → [`00bbd490`](#insn-00bbd490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd48c`](#insn-00bbd48c) → [`00bbdb48`](#insn-00bbdb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd494`](#insn-00bbd494) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd498`](#insn-00bbd498) → [`00bbd4d0`](#insn-00bbd4d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4cc`](#insn-00bbd4cc) → [`00bbda84`](#insn-00bbda84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4d0`](#insn-00bbd4d0) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4d4`](#insn-00bbd4d4) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4d8`](#insn-00bbd4d8) → [`00bbd4f4`](#insn-00bbd4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4dc`](#insn-00bbd4dc) → `Stack[-0x11f]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4e0`](#insn-00bbd4e0) → [`00bbd4f4`](#insn-00bbd4f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4e8`](#insn-00bbd4e8) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4ec`](#insn-00bbd4ec) → `Stack[-0x148]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4f0`](#insn-00bbd4f0) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd4f8`](#insn-00bbd4f8) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd500`](#insn-00bbd500) → [`00bbd7c8`](#insn-00bbd7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd50c`](#insn-00bbd50c) → [`00bbd7c8`](#insn-00bbd7c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd518`](#insn-00bbd518) → [`00bbd940`](#insn-00bbd940) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd520`](#insn-00bbd520) → [`00bbd6fc`](#insn-00bbd6fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd528`](#insn-00bbd528) → [`00bbd9a8`](#insn-00bbd9a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd530`](#insn-00bbd530) → [`00bbd76c`](#insn-00bbd76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd540`](#insn-00bbd540) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd544`](#insn-00bbd544) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd548`](#insn-00bbd548) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd554`](#insn-00bbd554) → [`00bbdc10`](00bbdc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdc10` · 推定シンボル `None` · 推定型 `None`
- [`00bbd558`](#insn-00bbd558) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd564`](#insn-00bbd564) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd570`](#insn-00bbd570) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd580`](#insn-00bbd580) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd584`](#insn-00bbd584) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd588`](#insn-00bbd588) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd598`](#insn-00bbd598) → [`00bc0864`](../00bc0/00bc0864.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0864` · 推定シンボル `None` · 推定型 `None`
- [`00bbd59c`](#insn-00bbd59c) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5b0`](#insn-00bbd5b0) → [`00bbf290`](../00bbf/00bbf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf290` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5b4`](#insn-00bbd5b4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5b8`](#insn-00bbd5b8) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5c4`](#insn-00bbd5c4) → [`00bbd648`](#insn-00bbd648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5d0`](#insn-00bbd5d0) → [`00bbd5e8`](#insn-00bbd5e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5d8`](#insn-00bbd5d8) → [`00bbd618`](#insn-00bbd618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5e4`](#insn-00bbd5e4) → [`00bbd618`](#insn-00bbd618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5f0`](#insn-00bbd5f0) → [`00bbd644`](#insn-00bbd644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd5f8`](#insn-00bbd5f8) → [`00bbd644`](#insn-00bbd644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd604`](#insn-00bbd604) → [`00bbd648`](#insn-00bbd648) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd614`](#insn-00bbd614) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd620`](#insn-00bbd620) → [`00bbd638`](#insn-00bbd638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd628`](#insn-00bbd628) → [`00bbd608`](#insn-00bbd608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd634`](#insn-00bbd634) → [`00bbd608`](#insn-00bbd608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd640`](#insn-00bbd640) → [`00bbd5f4`](#insn-00bbd5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd644`](#insn-00bbd644) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd650`](#insn-00bbd650) → [`00bc0b18`](../00bc0/00bc0b18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0b18` · 推定シンボル `None` · 推定型 `None`
- [`00bbd654`](#insn-00bbd654) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd668`](#insn-00bbd668) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd66c`](#insn-00bbd66c) → [`00bc0bc8`](../00bc0/00bc0bc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0bc8` · 推定シンボル `None` · 推定型 `None`
- [`00bbd674`](#insn-00bbd674) → [`00bbdb48`](#insn-00bbdb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd678`](#insn-00bbd678) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd67c`](#insn-00bbd67c) → [`00bbdb48`](#insn-00bbdb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd690`](#insn-00bbd690) → [`00bbd6b0`](#insn-00bbd6b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd698`](#insn-00bbd698) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd69c`](#insn-00bbd69c) → [`00bbdbc4`](#insn-00bbdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd6c8`](#insn-00bbd6c8) → `00c176a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbd6ec`](#insn-00bbd6ec) → `002a020f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd6ec`](#insn-00bbd6ec) → `0029f1e1`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbd6f8`](#insn-00bbd6f8) → [`00bbdb48`](#insn-00bbdb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd700`](#insn-00bbd700) → [`00bbd9d0`](#insn-00bbd9d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd708`](#insn-00bbd708) → [`00bbd76c`](#insn-00bbd76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd718`](#insn-00bbd718) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd71c`](#insn-00bbd71c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd720`](#insn-00bbd720) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd72c`](#insn-00bbd72c) → [`00bc04a4`](../00bc0/00bc04a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc04a4` · 推定シンボル `None` · 推定型 `None`
- [`00bbd730`](#insn-00bbd730) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd738`](#insn-00bbd738) → [`00bbda24`](#insn-00bbda24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd740`](#insn-00bbd740) → [`00bbd76c`](#insn-00bbd76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd750`](#insn-00bbd750) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd754`](#insn-00bbd754) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd758`](#insn-00bbd758) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd764`](#insn-00bbd764) → [`00bc03f4`](../00bc0/00bc03f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc03f4` · 推定シンボル `None` · 推定型 `None`
- [`00bbd768`](#insn-00bbd768) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd778`](#insn-00bbd778) → [`00bbd78c`](#insn-00bbd78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd788`](#insn-00bbd788) → [`00bbd790`](#insn-00bbd790) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd794`](#insn-00bbd794) → [`00bc0604`](../00bc0/00bc0604.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0604` · 推定シンボル `None` · 推定型 `None`
- [`00bbd798`](#insn-00bbd798) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7a0`](#insn-00bbd7a0) → [`00bbd1fc`](#insn-00bbd1fc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd1fc` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7a4`](#insn-00bbd7a4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7a8`](#insn-00bbd7a8) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7b4`](#insn-00bbd7b4) → [`00bbd7c0`](#insn-00bbd7c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7b8`](#insn-00bbd7b8) → [`00bc09bc`](../00bc0/00bc09bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc09bc` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7bc`](#insn-00bbd7bc) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7c0`](#insn-00bbd7c0) → [`00bc0a6c`](../00bc0/00bc0a6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0a6c` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7c4`](#insn-00bbd7c4) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7f0`](#insn-00bbd7f0) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd7f8`](#insn-00bbd7f8) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbd800`](#insn-00bbd800) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd804`](#insn-00bbd804) → `Stack[-0x108]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd80c`](#insn-00bbd80c) → [`00bbd88c`](#insn-00bbd88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd81c`](#insn-00bbd81c) → [`00bbd88c`](#insn-00bbd88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd830`](#insn-00bbd830) → [`00bbd850`](#insn-00bbd850) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd838`](#insn-00bbd838) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd83c`](#insn-00bbd83c) → [`00bbdbc4`](#insn-00bbdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd868`](#insn-00bbd868) → `00c19858`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbd894`](#insn-00bbd894) → [`00bbd8f8`](#insn-00bbd8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8a8`](#insn-00bbd8a8) → [`00bbd8bc`](#insn-00bbd8bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8ac`](#insn-00bbd8ac) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8b4`](#insn-00bbd8b4) → [`00bbd8e8`](#insn-00bbd8e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8b8`](#insn-00bbd8b8) → [`00bbdbcc`](#insn-00bbdbcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8c0`](#insn-00bbd8c0) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8c4`](#insn-00bbd8c4) → [`00bbdbd4`](#insn-00bbdbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8cc`](#insn-00bbd8cc) → [`00bbd8e4`](#insn-00bbd8e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd8dc`](#insn-00bbd8dc) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd90c`](#insn-00bbd90c) → [`00bbd92c`](#insn-00bbd92c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd91c`](#insn-00bbd91c) → [`00bbd7f4`](#insn-00bbd7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd928`](#insn-00bbd928) → [`00bbd7f4`](#insn-00bbd7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd92c`](#insn-00bbd92c) → `Stack[-0x158]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd934`](#insn-00bbd934) → [`00bbfe64`](../00bbf/00bbfe64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfe64` · 推定シンボル `None` · 推定型 `None`
- [`00bbd93c`](#insn-00bbd93c) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd944`](#insn-00bbd944) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd948`](#insn-00bbd948) → [`00bbd980`](#insn-00bbd980) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd954`](#insn-00bbd954) → [`00bbd980`](#insn-00bbd980) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd970`](#insn-00bbd970) → [`00bc2e00`](../00bc2/00bc2e00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2e00` · 推定シンボル `None` · 推定型 `None`
- [`00bbd978`](#insn-00bbd978) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd97c`](#insn-00bbd97c) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9a0`](#insn-00bbd9a0) → [`00bbffc0`](../00bbf/00bbffc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbffc0` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9a4`](#insn-00bbd9a4) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9b4`](#insn-00bbd9b4) → [`00bbf9c4`](../00bbf/00bbf9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf9c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9b8`](#insn-00bbd9b8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9bc`](#insn-00bbd9bc) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9c8`](#insn-00bbd9c8) → [`00bc0294`](../00bc0/00bc0294.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0294` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9cc`](#insn-00bbd9cc) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9e0`](#insn-00bbd9e0) → [`00bbf290`](../00bbf/00bbf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf290` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9e4`](#insn-00bbd9e4) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9e8`](#insn-00bbd9e8) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9f4`](#insn-00bbd9f4) → [`00bc090c`](../00bc0/00bc090c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc090c` · 推定シンボル `None` · 推定型 `None`
- [`00bbd9f8`](#insn-00bbd9f8) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda08`](#insn-00bbda08) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbda0c`](#insn-00bbda0c) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda10`](#insn-00bbda10) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda1c`](#insn-00bbda1c) → [`00bc0344`](../00bc0/00bc0344.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0344` · 推定シンボル `None` · 推定型 `None`
- [`00bbda20`](#insn-00bbda20) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda30`](#insn-00bbda30) → [`00bbdd50`](00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bbda34`](#insn-00bbda34) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda38`](#insn-00bbda38) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda44`](#insn-00bbda44) → [`00bc0554`](../00bc0/00bc0554.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc0554` · 推定シンボル `None` · 推定型 `None`
- [`00bbda48`](#insn-00bbda48) → [`00bbda7c`](#insn-00bbda7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda5c`](#insn-00bbda5c) → [`00bbf290`](../00bbf/00bbf290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf290` · 推定シンボル `None` · 推定型 `None`
- [`00bbda60`](#insn-00bbda60) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda64`](#insn-00bbda64) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda6c`](#insn-00bbda6c) → `002a645b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbda78`](#insn-00bbda78) → [`00bbdc9c`](00bbdc9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdc9c` · 推定シンボル `None` · 推定型 `None`
- [`00bbda80`](#insn-00bbda80) → [`00bbdb48`](#insn-00bbdb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbda9c`](#insn-00bbda9c) → [`00bbdad0`](#insn-00bbdad0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaa0`](#insn-00bbdaa0) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaa8`](#insn-00bbdaa8) → [`00bbdbc8`](#insn-00bbdbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdad4`](#insn-00bbdad4) → [`00bbdae4`](#insn-00bbdae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdae0`](#insn-00bbdae0) → [`00bbdb78`](#insn-00bbdb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdae8`](#insn-00bbdae8) → [`00bbf9c4`](../00bbf/00bbf9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf9c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaec`](#insn-00bbdaec) → [`00bbdb44`](#insn-00bbdb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdaf8`](#insn-00bbdaf8) → [`00bbdac0`](#insn-00bbdac0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb10`](#insn-00bbdb10) → [`00bbdaa0`](#insn-00bbdaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb18`](#insn-00bbdb18) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb1c`](#insn-00bbdb1c) → [`00bbdbd0`](#insn-00bbdbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb24`](#insn-00bbdb24) → [`00bbdb3c`](#insn-00bbdb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb34`](#insn-00bbdb34) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb40`](#insn-00bbdb40) → [`00bbdaac`](#insn-00bbdaac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb4c`](#insn-00bbdb4c) → [`00bc00b4`](../00bc0/00bc00b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc00b4` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb54`](#insn-00bbdb54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb58`](#insn-00bbdb58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb5c`](#insn-00bbdb5c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb60`](#insn-00bbdb60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb64`](#insn-00bbdb64) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb68`](#insn-00bbdb68) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb88`](#insn-00bbdb88) → [`00bbfe64`](../00bbf/00bbfe64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfe64` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb8c`](#insn-00bbdb8c) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb98`](#insn-00bbdb98) → [`00bbfdc4`](../00bbf/00bbfdc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfdc4` · 推定シンボル `None` · 推定型 `None`
- [`00bbdb9c`](#insn-00bbdb9c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdba0`](#insn-00bbdba0) → [`00bbd4d0`](#insn-00bbd4d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdba8`](#insn-00bbdba8) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdbb0`](#insn-00bbdbb0) → `002a207d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdbb8`](#insn-00bbdbb8) → `002a20b7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbdbc0`](#insn-00bbdbc0) → [`00bbb090`](../00bbb/00bbb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb090` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbc4`](#insn-00bbdbc4) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbc8`](#insn-00bbdbc8) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbcc`](#insn-00bbdbcc) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbd0`](#insn-00bbdbd0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdbd4`](#insn-00bbdbd4) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbd204`](#insn-00bbd204)

~~~json
{
  "source": "00bbd204",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd208`](#insn-00bbd208)

~~~json
{
  "source": "00bbd208",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd20c`](#insn-00bbd20c)

~~~json
{
  "source": "00bbd20c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd210`](#insn-00bbd210)

~~~json
{
  "source": "00bbd210",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd214`](#insn-00bbd214)

~~~json
{
  "source": "00bbd214",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd218`](#insn-00bbd218)

~~~json
{
  "source": "00bbd218",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd22c`](#insn-00bbd22c)

~~~json
{
  "source": "00bbd22c",
  "target": "00bbf0e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd238`](#insn-00bbd238)

~~~json
{
  "source": "00bbd238",
  "target": "00bbd2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd244`](#insn-00bbd244)

~~~json
{
  "source": "00bbd244",
  "target": "00bbd398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd24c`](#insn-00bbd24c)

~~~json
{
  "source": "00bbd24c",
  "target": "00bbd2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd254`](#insn-00bbd254)

~~~json
{
  "source": "00bbd254",
  "target": "00bbd76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd260`](#insn-00bbd260)

~~~json
{
  "source": "00bbd260",
  "target": "00bbd51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd268`](#insn-00bbd268)

~~~json
{
  "source": "00bbd268",
  "target": "00bbd734",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd270`](#insn-00bbd270)

~~~json
{
  "source": "00bbd270",
  "target": "00bbd9fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd278`](#insn-00bbd278)

~~~json
{
  "source": "00bbd278",
  "target": "00bbda4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd280`](#insn-00bbd280)

~~~json
{
  "source": "00bbd280",
  "target": "00bbd76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd290`](#insn-00bbd290)

~~~json
{
  "source": "00bbd290",
  "target": "00bc0604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd294`](#insn-00bbd294)

~~~json
{
  "source": "00bbd294",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd29c`](#insn-00bbd29c)

~~~json
{
  "source": "00bbd29c",
  "target": "00bc0604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd2a0`](#insn-00bbd2a0)

~~~json
{
  "source": "00bbd2a0",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2a8`](#insn-00bbd2a8)

~~~json
{
  "source": "00bbd2a8",
  "target": "00bbd1fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd2ac`](#insn-00bbd2ac)

~~~json
{
  "source": "00bbd2ac",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2b0`](#insn-00bbd2b0)

~~~json
{
  "source": "00bbd2b0",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2bc`](#insn-00bbd2bc)

~~~json
{
  "source": "00bbd2bc",
  "target": "00bc07b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd2c0`](#insn-00bbd2c0)

~~~json
{
  "source": "00bbd2c0",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2d0`](#insn-00bbd2d0)

~~~json
{
  "source": "00bbd2d0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2d8`](#insn-00bbd2d8)

~~~json
{
  "source": "00bbd2d8",
  "target": "Stack[-0x11c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2e0`](#insn-00bbd2e0)

~~~json
{
  "source": "00bbd2e0",
  "target": "Stack[-0x118]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2e4`](#insn-00bbd2e4)

~~~json
{
  "source": "00bbd2e4",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2e8`](#insn-00bbd2e8)

~~~json
{
  "source": "00bbd2e8",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd2f4`](#insn-00bbd2f4)

~~~json
{
  "source": "00bbd2f4",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd2fc`](#insn-00bbd2fc)

~~~json
{
  "source": "00bbd2fc",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd300`](#insn-00bbd300)

~~~json
{
  "source": "00bbd300",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd310`](#insn-00bbd310)

~~~json
{
  "source": "00bbd310",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd31c`](#insn-00bbd31c)

~~~json
{
  "source": "00bbd31c",
  "target": "00bbd448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd32c`](#insn-00bbd32c)

~~~json
{
  "source": "00bbd32c",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd334`](#insn-00bbd334)

~~~json
{
  "source": "00bbd334",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd34c`](#insn-00bbd34c)

~~~json
{
  "source": "00bbd34c",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd360`](#insn-00bbd360)

~~~json
{
  "source": "00bbd360",
  "target": "00bbd450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd36c`](#insn-00bbd36c)

~~~json
{
  "source": "00bbd36c",
  "target": "00bbd38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd388`](#insn-00bbd388)

~~~json
{
  "source": "00bbd388",
  "target": "00bbd354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd390`](#insn-00bbd390)

~~~json
{
  "source": "00bbd390",
  "target": "00bbd458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd394`](#insn-00bbd394)

~~~json
{
  "source": "00bbd394",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd39c`](#insn-00bbd39c)

~~~json
{
  "source": "00bbd39c",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3a8`](#insn-00bbd3a8)

~~~json
{
  "source": "00bbd3a8",
  "target": "00bbd658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3b0`](#insn-00bbd3b0)

~~~json
{
  "source": "00bbd3b0",
  "target": "00bbd5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3b8`](#insn-00bbd3b8)

~~~json
{
  "source": "00bbd3b8",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3cc`](#insn-00bbd3cc)

~~~json
{
  "source": "00bbd3cc",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd3d0`](#insn-00bbd3d0)

~~~json
{
  "source": "00bbd3d0",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3e4`](#insn-00bbd3e4)

~~~json
{
  "source": "00bbd3e4",
  "target": "00bbd40c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd3f0`](#insn-00bbd3f0)

~~~json
{
  "source": "00bbd3f0",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd3f4`](#insn-00bbd3f4)

~~~json
{
  "source": "00bbd3f4",
  "target": "00bbdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd424`](#insn-00bbd424)

~~~json
{
  "source": "00bbd424",
  "target": "00c176a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c176a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbd444`](#insn-00bbd444)

~~~json
{
  "source": "00bbd444",
  "target": "00bbd6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd44c`](#insn-00bbd44c)

~~~json
{
  "source": "00bbd44c",
  "target": "00bbdba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd460`](#insn-00bbd460)

~~~json
{
  "source": "00bbd460",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd470`](#insn-00bbd470)

~~~json
{
  "source": "00bbd470",
  "target": "00bbd490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd48c`](#insn-00bbd48c)

~~~json
{
  "source": "00bbd48c",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd494`](#insn-00bbd494)

~~~json
{
  "source": "00bbd494",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd498`](#insn-00bbd498)

~~~json
{
  "source": "00bbd498",
  "target": "00bbd4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4cc`](#insn-00bbd4cc)

~~~json
{
  "source": "00bbd4cc",
  "target": "00bbda84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4d0`](#insn-00bbd4d0)

~~~json
{
  "source": "00bbd4d0",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4d4`](#insn-00bbd4d4)

~~~json
{
  "source": "00bbd4d4",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4d8`](#insn-00bbd4d8)

~~~json
{
  "source": "00bbd4d8",
  "target": "00bbd4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4dc`](#insn-00bbd4dc)

~~~json
{
  "source": "00bbd4dc",
  "target": "Stack[-0x11f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4e0`](#insn-00bbd4e0)

~~~json
{
  "source": "00bbd4e0",
  "target": "00bbd4f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4e8`](#insn-00bbd4e8)

~~~json
{
  "source": "00bbd4e8",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd4ec`](#insn-00bbd4ec)

~~~json
{
  "source": "00bbd4ec",
  "target": "Stack[-0x148]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4f0`](#insn-00bbd4f0)

~~~json
{
  "source": "00bbd4f0",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd4f8`](#insn-00bbd4f8)

~~~json
{
  "source": "00bbd4f8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd500`](#insn-00bbd500)

~~~json
{
  "source": "00bbd500",
  "target": "00bbd7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd50c`](#insn-00bbd50c)

~~~json
{
  "source": "00bbd50c",
  "target": "00bbd7c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd518`](#insn-00bbd518)

~~~json
{
  "source": "00bbd518",
  "target": "00bbd940",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd520`](#insn-00bbd520)

~~~json
{
  "source": "00bbd520",
  "target": "00bbd6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd528`](#insn-00bbd528)

~~~json
{
  "source": "00bbd528",
  "target": "00bbd9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd530`](#insn-00bbd530)

~~~json
{
  "source": "00bbd530",
  "target": "00bbd76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd540`](#insn-00bbd540)

~~~json
{
  "source": "00bbd540",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd544`](#insn-00bbd544)

~~~json
{
  "source": "00bbd544",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd548`](#insn-00bbd548)

~~~json
{
  "source": "00bbd548",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd554`](#insn-00bbd554)

~~~json
{
  "source": "00bbd554",
  "target": "00bbdc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd558`](#insn-00bbd558)

~~~json
{
  "source": "00bbd558",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd564`](#insn-00bbd564)

~~~json
{
  "source": "00bbd564",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd570`](#insn-00bbd570)

~~~json
{
  "source": "00bbd570",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd580`](#insn-00bbd580)

~~~json
{
  "source": "00bbd580",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd584`](#insn-00bbd584)

~~~json
{
  "source": "00bbd584",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd588`](#insn-00bbd588)

~~~json
{
  "source": "00bbd588",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd598`](#insn-00bbd598)

~~~json
{
  "source": "00bbd598",
  "target": "00bc0864",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd59c`](#insn-00bbd59c)

~~~json
{
  "source": "00bbd59c",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5b0`](#insn-00bbd5b0)

~~~json
{
  "source": "00bbd5b0",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd5b4`](#insn-00bbd5b4)

~~~json
{
  "source": "00bbd5b4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5b8`](#insn-00bbd5b8)

~~~json
{
  "source": "00bbd5b8",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5c4`](#insn-00bbd5c4)

~~~json
{
  "source": "00bbd5c4",
  "target": "00bbd648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5d0`](#insn-00bbd5d0)

~~~json
{
  "source": "00bbd5d0",
  "target": "00bbd5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5d8`](#insn-00bbd5d8)

~~~json
{
  "source": "00bbd5d8",
  "target": "00bbd618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5e4`](#insn-00bbd5e4)

~~~json
{
  "source": "00bbd5e4",
  "target": "00bbd618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5f0`](#insn-00bbd5f0)

~~~json
{
  "source": "00bbd5f0",
  "target": "00bbd644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd5f8`](#insn-00bbd5f8)

~~~json
{
  "source": "00bbd5f8",
  "target": "00bbd644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd604`](#insn-00bbd604)

~~~json
{
  "source": "00bbd604",
  "target": "00bbd648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd614`](#insn-00bbd614)

~~~json
{
  "source": "00bbd614",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd620`](#insn-00bbd620)

~~~json
{
  "source": "00bbd620",
  "target": "00bbd638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd628`](#insn-00bbd628)

~~~json
{
  "source": "00bbd628",
  "target": "00bbd608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd634`](#insn-00bbd634)

~~~json
{
  "source": "00bbd634",
  "target": "00bbd608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd640`](#insn-00bbd640)

~~~json
{
  "source": "00bbd640",
  "target": "00bbd5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd644`](#insn-00bbd644)

~~~json
{
  "source": "00bbd644",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd650`](#insn-00bbd650)

~~~json
{
  "source": "00bbd650",
  "target": "00bc0b18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd654`](#insn-00bbd654)

~~~json
{
  "source": "00bbd654",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd668`](#insn-00bbd668)

~~~json
{
  "source": "00bbd668",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd66c`](#insn-00bbd66c)

~~~json
{
  "source": "00bbd66c",
  "target": "00bc0bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd674`](#insn-00bbd674)

~~~json
{
  "source": "00bbd674",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd678`](#insn-00bbd678)

~~~json
{
  "source": "00bbd678",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd67c`](#insn-00bbd67c)

~~~json
{
  "source": "00bbd67c",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd690`](#insn-00bbd690)

~~~json
{
  "source": "00bbd690",
  "target": "00bbd6b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd698`](#insn-00bbd698)

~~~json
{
  "source": "00bbd698",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd69c`](#insn-00bbd69c)

~~~json
{
  "source": "00bbd69c",
  "target": "00bbdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd6c8`](#insn-00bbd6c8)

~~~json
{
  "source": "00bbd6c8",
  "target": "00c176a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c176a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbd6ec`](#insn-00bbd6ec)

~~~json
{
  "source": "00bbd6ec",
  "target": "002a020f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a020f",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6775617264207661726961626c6520666f722000",
  "capture_start": "002a020f",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbd6ec`](#insn-00bbd6ec)

~~~json
{
  "source": "00bbd6ec",
  "target": "0029f1e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f1e1",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "696e697469616c697a657220666f72206d6f64756c652000",
  "capture_start": "0029f1e1",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbd6f8`](#insn-00bbd6f8)

~~~json
{
  "source": "00bbd6f8",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd700`](#insn-00bbd700)

~~~json
{
  "source": "00bbd700",
  "target": "00bbd9d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd708`](#insn-00bbd708)

~~~json
{
  "source": "00bbd708",
  "target": "00bbd76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd718`](#insn-00bbd718)

~~~json
{
  "source": "00bbd718",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd71c`](#insn-00bbd71c)

~~~json
{
  "source": "00bbd71c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd720`](#insn-00bbd720)

~~~json
{
  "source": "00bbd720",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd72c`](#insn-00bbd72c)

~~~json
{
  "source": "00bbd72c",
  "target": "00bc04a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd730`](#insn-00bbd730)

~~~json
{
  "source": "00bbd730",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd738`](#insn-00bbd738)

~~~json
{
  "source": "00bbd738",
  "target": "00bbda24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd740`](#insn-00bbd740)

~~~json
{
  "source": "00bbd740",
  "target": "00bbd76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd750`](#insn-00bbd750)

~~~json
{
  "source": "00bbd750",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd754`](#insn-00bbd754)

~~~json
{
  "source": "00bbd754",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd758`](#insn-00bbd758)

~~~json
{
  "source": "00bbd758",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd764`](#insn-00bbd764)

~~~json
{
  "source": "00bbd764",
  "target": "00bc03f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd768`](#insn-00bbd768)

~~~json
{
  "source": "00bbd768",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd778`](#insn-00bbd778)

~~~json
{
  "source": "00bbd778",
  "target": "00bbd78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd788`](#insn-00bbd788)

~~~json
{
  "source": "00bbd788",
  "target": "00bbd790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd794`](#insn-00bbd794)

~~~json
{
  "source": "00bbd794",
  "target": "00bc0604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd798`](#insn-00bbd798)

~~~json
{
  "source": "00bbd798",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7a0`](#insn-00bbd7a0)

~~~json
{
  "source": "00bbd7a0",
  "target": "00bbd1fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd7a4`](#insn-00bbd7a4)

~~~json
{
  "source": "00bbd7a4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7a8`](#insn-00bbd7a8)

~~~json
{
  "source": "00bbd7a8",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7b4`](#insn-00bbd7b4)

~~~json
{
  "source": "00bbd7b4",
  "target": "00bbd7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7b8`](#insn-00bbd7b8)

~~~json
{
  "source": "00bbd7b8",
  "target": "00bc09bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd7bc`](#insn-00bbd7bc)

~~~json
{
  "source": "00bbd7bc",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7c0`](#insn-00bbd7c0)

~~~json
{
  "source": "00bbd7c0",
  "target": "00bc0a6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd7c4`](#insn-00bbd7c4)

~~~json
{
  "source": "00bbd7c4",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7f0`](#insn-00bbd7f0)

~~~json
{
  "source": "00bbd7f0",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd7f8`](#insn-00bbd7f8)

~~~json
{
  "source": "00bbd7f8",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd800`](#insn-00bbd800)

~~~json
{
  "source": "00bbd800",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd804`](#insn-00bbd804)

~~~json
{
  "source": "00bbd804",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd80c`](#insn-00bbd80c)

~~~json
{
  "source": "00bbd80c",
  "target": "00bbd88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd81c`](#insn-00bbd81c)

~~~json
{
  "source": "00bbd81c",
  "target": "00bbd88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd830`](#insn-00bbd830)

~~~json
{
  "source": "00bbd830",
  "target": "00bbd850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd838`](#insn-00bbd838)

~~~json
{
  "source": "00bbd838",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd83c`](#insn-00bbd83c)

~~~json
{
  "source": "00bbd83c",
  "target": "00bbdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd868`](#insn-00bbd868)

~~~json
{
  "source": "00bbd868",
  "target": "00c19858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19858",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbd894`](#insn-00bbd894)

~~~json
{
  "source": "00bbd894",
  "target": "00bbd8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8a8`](#insn-00bbd8a8)

~~~json
{
  "source": "00bbd8a8",
  "target": "00bbd8bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8ac`](#insn-00bbd8ac)

~~~json
{
  "source": "00bbd8ac",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd8b4`](#insn-00bbd8b4)

~~~json
{
  "source": "00bbd8b4",
  "target": "00bbd8e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8b8`](#insn-00bbd8b8)

~~~json
{
  "source": "00bbd8b8",
  "target": "00bbdbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8c0`](#insn-00bbd8c0)

~~~json
{
  "source": "00bbd8c0",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd8c4`](#insn-00bbd8c4)

~~~json
{
  "source": "00bbd8c4",
  "target": "00bbdbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8cc`](#insn-00bbd8cc)

~~~json
{
  "source": "00bbd8cc",
  "target": "00bbd8e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd8dc`](#insn-00bbd8dc)

~~~json
{
  "source": "00bbd8dc",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd90c`](#insn-00bbd90c)

~~~json
{
  "source": "00bbd90c",
  "target": "00bbd92c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd91c`](#insn-00bbd91c)

~~~json
{
  "source": "00bbd91c",
  "target": "00bbd7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd928`](#insn-00bbd928)

~~~json
{
  "source": "00bbd928",
  "target": "00bbd7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd92c`](#insn-00bbd92c)

~~~json
{
  "source": "00bbd92c",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd934`](#insn-00bbd934)

~~~json
{
  "source": "00bbd934",
  "target": "00bbfe64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd93c`](#insn-00bbd93c)

~~~json
{
  "source": "00bbd93c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd944`](#insn-00bbd944)

~~~json
{
  "source": "00bbd944",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd948`](#insn-00bbd948)

~~~json
{
  "source": "00bbd948",
  "target": "00bbd980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd954`](#insn-00bbd954)

~~~json
{
  "source": "00bbd954",
  "target": "00bbd980",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd970`](#insn-00bbd970)

~~~json
{
  "source": "00bbd970",
  "target": "00bc2e00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd978`](#insn-00bbd978)

~~~json
{
  "source": "00bbd978",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd97c`](#insn-00bbd97c)

~~~json
{
  "source": "00bbd97c",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9a0`](#insn-00bbd9a0)

~~~json
{
  "source": "00bbd9a0",
  "target": "00bbffc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd9a4`](#insn-00bbd9a4)

~~~json
{
  "source": "00bbd9a4",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9b4`](#insn-00bbd9b4)

~~~json
{
  "source": "00bbd9b4",
  "target": "00bbf9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd9b8`](#insn-00bbd9b8)

~~~json
{
  "source": "00bbd9b8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9bc`](#insn-00bbd9bc)

~~~json
{
  "source": "00bbd9bc",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9c8`](#insn-00bbd9c8)

~~~json
{
  "source": "00bbd9c8",
  "target": "00bc0294",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd9cc`](#insn-00bbd9cc)

~~~json
{
  "source": "00bbd9cc",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9e0`](#insn-00bbd9e0)

~~~json
{
  "source": "00bbd9e0",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd9e4`](#insn-00bbd9e4)

~~~json
{
  "source": "00bbd9e4",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9e8`](#insn-00bbd9e8)

~~~json
{
  "source": "00bbd9e8",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbd9f4`](#insn-00bbd9f4)

~~~json
{
  "source": "00bbd9f4",
  "target": "00bc090c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbd9f8`](#insn-00bbd9f8)

~~~json
{
  "source": "00bbd9f8",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda08`](#insn-00bbda08)

~~~json
{
  "source": "00bbda08",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda0c`](#insn-00bbda0c)

~~~json
{
  "source": "00bbda0c",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda10`](#insn-00bbda10)

~~~json
{
  "source": "00bbda10",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda1c`](#insn-00bbda1c)

~~~json
{
  "source": "00bbda1c",
  "target": "00bc0344",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda20`](#insn-00bbda20)

~~~json
{
  "source": "00bbda20",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda30`](#insn-00bbda30)

~~~json
{
  "source": "00bbda30",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda34`](#insn-00bbda34)

~~~json
{
  "source": "00bbda34",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda38`](#insn-00bbda38)

~~~json
{
  "source": "00bbda38",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda44`](#insn-00bbda44)

~~~json
{
  "source": "00bbda44",
  "target": "00bc0554",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda48`](#insn-00bbda48)

~~~json
{
  "source": "00bbda48",
  "target": "00bbda7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda5c`](#insn-00bbda5c)

~~~json
{
  "source": "00bbda5c",
  "target": "00bbf290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda60`](#insn-00bbda60)

~~~json
{
  "source": "00bbda60",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda64`](#insn-00bbda64)

~~~json
{
  "source": "00bbda64",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda6c`](#insn-00bbda6c)

~~~json
{
  "source": "00bbda6c",
  "target": "002a645b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a645b",
  "offset": 0,
  "size": 34,
  "datatype": "string",
  "bytes": "7468726561642d6c6f63616c207772617070657220726f7574696e6520666f72",
  "capture_start": "002a645b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbda78`](#insn-00bbda78)

~~~json
{
  "source": "00bbda78",
  "target": "00bbdc9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbda80`](#insn-00bbda80)

~~~json
{
  "source": "00bbda80",
  "target": "00bbdb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbda9c`](#insn-00bbda9c)

~~~json
{
  "source": "00bbda9c",
  "target": "00bbdad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaa0`](#insn-00bbdaa0)

~~~json
{
  "source": "00bbdaa0",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdaa8`](#insn-00bbdaa8)

~~~json
{
  "source": "00bbdaa8",
  "target": "00bbdbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdad4`](#insn-00bbdad4)

~~~json
{
  "source": "00bbdad4",
  "target": "00bbdae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdae0`](#insn-00bbdae0)

~~~json
{
  "source": "00bbdae0",
  "target": "00bbdb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdae8`](#insn-00bbdae8)

~~~json
{
  "source": "00bbdae8",
  "target": "00bbf9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdaec`](#insn-00bbdaec)

~~~json
{
  "source": "00bbdaec",
  "target": "00bbdb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdaf8`](#insn-00bbdaf8)

~~~json
{
  "source": "00bbdaf8",
  "target": "00bbdac0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb10`](#insn-00bbdb10)

~~~json
{
  "source": "00bbdb10",
  "target": "00bbdaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb18`](#insn-00bbdb18)

~~~json
{
  "source": "00bbdb18",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb1c`](#insn-00bbdb1c)

~~~json
{
  "source": "00bbdb1c",
  "target": "00bbdbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb24`](#insn-00bbdb24)

~~~json
{
  "source": "00bbdb24",
  "target": "00bbdb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb34`](#insn-00bbdb34)

~~~json
{
  "source": "00bbdb34",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb40`](#insn-00bbdb40)

~~~json
{
  "source": "00bbdb40",
  "target": "00bbdaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb4c`](#insn-00bbdb4c)

~~~json
{
  "source": "00bbdb4c",
  "target": "00bc00b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb54`](#insn-00bbdb54)

~~~json
{
  "source": "00bbdb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb58`](#insn-00bbdb58)

~~~json
{
  "source": "00bbdb58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb5c`](#insn-00bbdb5c)

~~~json
{
  "source": "00bbdb5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb60`](#insn-00bbdb60)

~~~json
{
  "source": "00bbdb60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb64`](#insn-00bbdb64)

~~~json
{
  "source": "00bbdb64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb68`](#insn-00bbdb68)

~~~json
{
  "source": "00bbdb68",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb88`](#insn-00bbdb88)

~~~json
{
  "source": "00bbdb88",
  "target": "00bbfe64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb8c`](#insn-00bbdb8c)

~~~json
{
  "source": "00bbdb8c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdb98`](#insn-00bbdb98)

~~~json
{
  "source": "00bbdb98",
  "target": "00bbfdc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdb9c`](#insn-00bbdb9c)

~~~json
{
  "source": "00bbdb9c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdba0`](#insn-00bbdba0)

~~~json
{
  "source": "00bbdba0",
  "target": "00bbd4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdba8`](#insn-00bbdba8)

~~~json
{
  "source": "00bbdba8",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdbb0`](#insn-00bbdbb0)

~~~json
{
  "source": "00bbdbb0",
  "target": "002a207d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a207d",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f64",
  "capture_start": "002a207d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbdbb8`](#insn-00bbdbb8)

~~~json
{
  "source": "00bbdbb8",
  "target": "002a20b7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a20b7",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "736872696e6b546f53697a6528292063616e277420657870616e642100",
  "capture_start": "002a20b7",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdbc0`](#insn-00bbdbc0)

~~~json
{
  "source": "00bbdbc0",
  "target": "00bbb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbc4`](#insn-00bbdbc4)

~~~json
{
  "source": "00bbdbc4",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbc8`](#insn-00bbdbc8)

~~~json
{
  "source": "00bbdbc8",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbcc`](#insn-00bbdbcc)

~~~json
{
  "source": "00bbdbcc",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbd0`](#insn-00bbdbd0)

~~~json
{
  "source": "00bbdbd0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdbd4`](#insn-00bbdbd4)

~~~json
{
  "source": "00bbdbd4",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
