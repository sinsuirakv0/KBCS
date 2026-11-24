# 00aafaa4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aafa34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aaf/00aafa34.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-21c9026f8775677cf7aa6e94a2519e7d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ab0a98`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ab0/00ab0a98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-af1328d4e9a6ab8ea34093d04d50802e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aafaa4",
  "name": "FUN_00aafaa4",
  "size": 1500,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2a2e80129a25659dad0d2ea57788af5e7e49d3dac6d2d26fd34948a80de6116",
  "source_text_sha256": "d2a2e80129a25659dad0d2ea57788af5e7e49d3dac6d2d26fd34948a80de6116",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aafaa4",
        "00ab007b"
      ],
      [
        "00ab00d0",
        "00ab00d3"
      ]
    ],
    "bytes_sha256": "d17cbada33b75734013d1f7432016384796b2255ae6af3c143a2acb1673d9835",
    "instruction_count": 375,
    "instruction_bytes": 1500,
    "body_bytes": 1500,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1f4c4](../00b1f/00b1f4c4.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [00440f00](../00440/00440f00.md)
- [0048795c](../00487/0048795c.md)
- [0048797c](../00487/0048797c.md)
- [00487e60](../00487/00487e60.md)
- [00488598](../00488/00488598.md)
- [00488698](../00488/00488698.md)
- [008003d0](../00800/008003d0.md)
- [00800684](../00800/00800684.md)
- [0086950c](../00869/0086950c.md)
- [00ab17f4](../00ab1/00ab17f4.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)
- [00c580d0](../00c58/00c580d0.md)

## 関連文字列（未確認候補）

~~~text
"MapStage_Shortcut.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 15136 bytes

~~~c

void FUN_00aafaa4(long *param_1)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  long lVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined5 uVar6;
  undefined5 uVar7;
  undefined3 uVar8;
  undefined5 uVar9;
  undefined5 uVar10;
  undefined *puVar11;
  int iVar12;
  int iVar13;
  undefined4 uVar14;
  undefined4 uVar15;
  undefined4 uVar16;
  undefined4 uVar17;
  int iVar18;
  ulong uVar19;
  long *plVar20;
  void *pvVar21;
  long *plVar22;
  long *plVar23;
  ulong uVar24;
  ulong uVar25;
  long *plVar26;
  long *plVar27;
  long lVar28;
  void *pvVar29;
  long *plVar30;
  undefined4 local_1ec;
  undefined4 local_1e8;
  undefined1 local_1e4;
  byte local_1e0;
  char local_1df [8];
  char acStack_1d7 [5];
  undefined2 uStack_1d2;
  char cStack_1d0;
  char acStack_1cf [5];
  undefined1 uStack_1ca;
  undefined1 uStack_1c9;
  undefined **local_1c8;
  void *local_1c0;
  void *local_1b8;
  byte local_1a8;
  void *local_198;
  long local_180;
  undefined *local_178 [8];
  byte local_138;
  void *local_128;
  undefined1 auStack_110 [160];
  long local_70;
  
  lVar3 = tpidr_el0;
  local_70 = *(long *)(lVar3 + 0x28);
  FUN_00487e60(&local_1c8);
  plVar26 = param_1 + 1;
                    /* try { // try from 00aafae8 to 00bafb0f has its CatchHandler @ 00aafdf0 */
  local_1c8 = &PTR_FUN_00c64e08;
  FUN_0086950c(param_1,*plVar26);
  *param_1 = (long)plVar26;
  plVar27 = param_1 + 4;
  param_1[2] = 0;
  *plVar26 = 0;
  FUN_0086950c(param_1 + 3,*plVar27);
  uVar9 = s_MapStage_Shortcut_csv_002b6b66._16_5_;
  uVar8 = s_MapStage_Shortcut_csv_002b6b66._13_3_;
  uVar6 = s_MapStage_Shortcut_csv_002b6b66._8_5_;
  uVar4 = s_MapStage_Shortcut_csv_002b6b66._0_8_;
  local_1e0 = 0x2a;
                    /* try { // try from 00aafb30 to 00bafb53 has its CatchHandler @ 00aafdb4 */
  param_1[3] = (long)plVar27;
  param_1[5] = 0;
  *plVar27 = 0;
  uVar10 = s_MapStage_Shortcut_csv_002b6b66._16_5_;
  uVar7 = s_MapStage_Shortcut_csv_002b6b66._8_5_;
  uVar5 = s_MapStage_Shortcut_csv_002b6b66._0_8_;
  s_MapStage_Shortcut_csv_002b6b66[8] = (char)uVar6;
  s_MapStage_Shortcut_csv_002b6b66[9] = SUB51(uVar6,1);
  s_MapStage_Shortcut_csv_002b6b66[10] = SUB51(uVar6,2);
  s_MapStage_Shortcut_csv_002b6b66[0xb] = SUB51(uVar6,3);
  s_MapStage_Shortcut_csv_002b6b66[0xc] = SUB51(uVar6,4);
  acStack_1d7[0] = s_MapStage_Shortcut_csv_002b6b66[8];
  acStack_1d7[1] = s_MapStage_Shortcut_csv_002b6b66[9];
  acStack_1d7[2] = s_MapStage_Shortcut_csv_002b6b66[10];
  acStack_1d7[3] = s_MapStage_Shortcut_csv_002b6b66[0xb];
  acStack_1d7[4] = s_MapStage_Shortcut_csv_002b6b66[0xc];
  s_MapStage_Shortcut_csv_002b6b66[0] = (char)uVar4;
  s_MapStage_Shortcut_csv_002b6b66[1] = SUB81(uVar4,1);
  s_MapStage_Shortcut_csv_002b6b66[2] = SUB81(uVar4,2);
  s_MapStage_Shortcut_csv_002b6b66[3] = SUB81(uVar4,3);
  s_MapStage_Shortcut_csv_002b6b66[4] = SUB81(uVar4,4);
  s_MapStage_Shortcut_csv_002b6b66[5] = SUB81(uVar4,5);
  s_MapStage_Shortcut_csv_002b6b66[6] = SUB81(uVar4,6);
  s_MapStage_Shortcut_csv_002b6b66[7] = SUB81(uVar4,7);
  local_1df[0] = s_MapStage_Shortcut_csv_002b6b66[0];
  local_1df[1] = s_MapStage_Shortcut_csv_002b6b66[1];
  local_1df[2] = s_MapStage_Shortcut_csv_002b6b66[2];
  local_1df[3] = s_MapStage_Shortcut_csv_002b6b66[3];
  local_1df[4] = s_MapStage_Shortcut_csv_002b6b66[4];
  local_1df[5] = s_MapStage_Shortcut_csv_002b6b66[5];
  local_1df[6] = s_MapStage_Shortcut_csv_002b6b66[6];
  local_1df[7] = s_MapStage_Shortcut_csv_002b6b66[7];
  uStack_1d2 = (undefined2)uVar8;
  cStack_1d0 = SUB31(uVar8,2);
  s_MapStage_Shortcut_csv_002b6b66[0x10] = (char)uVar9;
  s_MapStage_Shortcut_csv_002b6b66[0x11] = SUB51(uVar9,1);
  s_MapStage_Shortcut_csv_002b6b66[0x12] = SUB51(uVar9,2);
  s_MapStage_Shortcut_csv_002b6b66[0x13] = SUB51(uVar9,3);
  s_MapStage_Shortcut_csv_002b6b66[0x14] = SUB51(uVar9,4);
  acStack_1cf[0] = s_MapStage_Shortcut_csv_002b6b66[0x10];
  acStack_1cf[1] = s_MapStage_Shortcut_csv_002b6b66[0x11];
  acStack_1cf[2] = s_MapStage_Shortcut_csv_002b6b66[0x12];
  acStack_1cf[3] = s_MapStage_Shortcut_csv_002b6b66[0x13];
  acStack_1cf[4] = s_MapStage_Shortcut_csv_002b6b66[0x14];
  uStack_1ca = 0;
  s_MapStage_Shortcut_csv_002b6b66._0_8_ = uVar5;
  s_MapStage_Shortcut_csv_002b6b66._8_5_ = uVar7;
  s_MapStage_Shortcut_csv_002b6b66._16_5_ = uVar10;
                    /* try { // try from 00aafb58 to 00bafb5f has its CatchHandler @ 00aafe30 */
  uVar19 = FUN_00b11188(&local_1c8,&local_1e0,0,0);
  if ((local_1e0 & 1) != 0) {
    _ZdlPv((void *)CONCAT17(uStack_1c9,CONCAT16(uStack_1ca,CONCAT51(acStack_1cf,cStack_1d0))));
  }
  if ((uVar19 & 1) != 0) {
    while (uVar19 = FUN_0048795c(&local_1c8), (uVar19 & 1) != 0) {
      iVar12 = FUN_0048797c(&local_1c8,0);
                    /* try { // try from 00aafbcc to 00bafbef has its CatchHandler @ 00aafd6c */
      iVar13 = FUN_0048797c(&local_1c8,1);
      uVar14 = FUN_0048797c(&local_1c8,2);
      uVar15 = FUN_008003d0();
      uVar14 = FUN_00800684(uVar14);
                    /* try { // try from 00aafbf4 to 00bafc03 has its CatchHandler @ 00aafdf8 */
      uVar16 = FUN_0048797c(&local_1c8,3);
                    /* try { // try from 00aafc04 to 00bafd63 has its CatchHandler @ 00aaf9dc */
      uVar17 = FUN_0048797c(&local_1c8,4);
      iVar18 = FUN_00488598(&local_1c8);
      if ((iVar18 < 6) || (iVar18 = FUN_0048797c(&local_1c8,5), iVar18 == -1)) {
        local_1e4 = 0;
      }
      else {
        uVar17 = FUN_0048797c(&local_1c8,5);
        local_1e4 = 1;
      }
      iVar18 = FUN_00488598(&local_1c8);
      if (iVar18 < 7) {
        local_1e8 = 0xffffffff;
      }
      else {
        local_1e8 = FUN_0048797c(&local_1c8,6);
      }
      iVar18 = FUN_00488598(&local_1c8);
      if (iVar18 < 8) {
        local_1ec = 0xffffffff;
      }
      else {
        local_1ec = FUN_0048797c(&local_1c8,7);
      }
      plVar22 = plVar27;
      if (iVar12 == 1) {
        while (plVar20 = (long *)*plVar22, plVar30 = plVar22, (long *)*plVar22 != (long *)0x0) {
                    /* try { // try from 00aafd64 to 00bafd6b has its CatchHandler @ 00aafe50 */
          while (plVar22 = plVar20, (int)plVar22[4] <= iVar13) {
                    /* catch() { ... } // from try @ 00aafbcc with catch @ 00aafd6c
                       try { // try from 00aafd6c to 00bafe77 has its CatchHandler @ 00aaf9dc */
            if (iVar13 <= (int)plVar22[4]) goto LAB_00aafddc;
            plVar20 = (long *)plVar22[1];
            if ((long *)plVar22[1] == (long *)0x0) {
              plVar30 = plVar22 + 1;
              goto LAB_00aafd80;
            }
          }
        }
LAB_00aafd80:
        plVar20 = (long *)_Znwm(0x40);
        plVar20[2] = (long)plVar22;
        plVar20[6] = 0;
        plVar20[7] = 0;
        plVar20[5] = 0;
        *plVar20 = 0;
        plVar20[1] = 0;
                    /* catch() { ... } // from try @ 00aafb90 with catch @ 00aafda4 */
        *plVar30 = (long)plVar20;
        plVar23 = (long *)param_1[3];
        *(int *)(plVar20 + 4) = iVar13;
                    /* catch() { ... } // from try @ 00aafb30 with catch @ 00aafdb4 */
        plVar22 = plVar20;
        if (*plVar23 != 0) {
          param_1[3] = *plVar23;
          plVar22 = (long *)*plVar30;
        }
        FUN_0043bbe4(param_1[4],plVar22);
        param_1[5] = param_1[5] + 1;
        plVar22 = plVar20;
LAB_00aafddc:
        puVar2 = (undefined4 *)plVar22[6];
        if (puVar2 < (undefined4 *)plVar22[7]) {
          *puVar2 = uVar15;
          puVar2[1] = uVar14;
                    /* catch() { ... } // from try @ 00aafae8 with catch @ 00aafdf0 */
          puVar2[2] = uVar16;
          puVar2[3] = uVar17;
                    /* catch() { ... } // from try @ 00aafbf4 with catch @ 00aafdf8 */
          puVar2[4] = local_1e8;
          puVar2[5] = local_1ec;
          puVar2[7] = 0;
          *(undefined1 *)(puVar2 + 6) = local_1e4;
          plVar22[6] = (long)(puVar2 + 8);
        }
        else {
          pvVar29 = (void *)plVar22[5];
          lVar28 = (long)puVar2 - (long)pvVar29 >> 5;
          uVar19 = lVar28 + 1;
          if (uVar19 >> 0x3b != 0) goto LAB_00ab004c;
          uVar24 = plVar22[7] - (long)pvVar29;
                    /* catch() { ... } // from try @ 00aafb58 with catch @ 00aafe30 */
          uVar25 = (long)uVar24 >> 4;
          if (uVar25 <= uVar19) {
            uVar25 = uVar19;
          }
          if (0x7fffffffffffffdf < uVar24) {
            uVar25 = 0x7ffffffffffffff;
          }
          if (uVar25 != 0) {
                    /* catch() { ... } // from try @ 00aafa28 with catch @ 00aafe50
                       catch() { ... } // from try @ 00aafd64 with catch @ 00aafe50 */
            if (uVar25 >> 0x3b == 0) {
              pvVar21 = (void *)_Znwm(uVar25 << 5);
              goto LAB_00aaff2c;
            }
            goto LAB_00ab0064;
          }
          pvVar21 = (void *)0x0;
LAB_00aaff2c:
          puVar1 = (undefined4 *)((long)pvVar21 + lVar28 * 0x20);
          puVar1[4] = local_1e8;
          puVar1[5] = local_1ec;
          *puVar1 = uVar15;
          puVar1[1] = uVar14;
          puVar1[2] = uVar16;
          puVar1[3] = uVar17;
                    /* try { // try from 00aaff58 to 00baff5b has its CatchHandler @ 00ab0418 */
          *(undefined1 *)(puVar1 + 6) = local_1e4;
          puVar1[7] = 0;
          memcpy(pvVar21,pvVar29,(long)puVar2 - (long)pvVar29);
          plVar22[5] = (long)pvVar21;
          plVar22[6] = (long)(puVar1 + 8);
                    /* try { // try from 00aaff68 to 00baff73 has its CatchHandler @ 00ab0410 */
          plVar22[7] = (long)((long)pvVar21 + uVar25 * 0x20);
          if (pvVar29 != (void *)0x0) {
                    /* try { // try from 00aaff74 to 00baff7f has its CatchHandler @ 00ab0408 */
            _ZdlPv(pvVar29);
          }
          plVar22[6] = (long)(puVar1 + 8);
        }
      }
      else {
        plVar22 = plVar26;
        if (iVar12 == 0) {
          while (plVar20 = (long *)*plVar22, plVar30 = plVar22, (long *)*plVar22 != (long *)0x0) {
            while (plVar22 = plVar20, (int)plVar22[4] <= iVar13) {
              if (iVar13 <= (int)plVar22[4]) goto LAB_00aafe6c;
              plVar20 = (long *)plVar22[1];
              if ((long *)plVar22[1] == (long *)0x0) {
                plVar30 = plVar22 + 1;
                goto LAB_00aafcf4;
              }
            }
          }
LAB_00aafcf4:
          plVar20 = (long *)_Znwm(0x40);
          plVar20[2] = (long)plVar22;
          plVar20[6] = 0;
          plVar20[7] = 0;
          plVar20[5] = 0;
          *plVar20 = 0;
          plVar20[1] = 0;
          *plVar30 = (long)plVar20;
          plVar23 = (long *)*param_1;
          *(int *)(plVar20 + 4) = iVar13;
          plVar22 = plVar20;
          if (*plVar23 != 0) {
            *param_1 = *plVar23;
            plVar22 = (long *)*plVar30;
          }
          FUN_0043bbe4(param_1[1],plVar22);
          param_1[2] = param_1[2] + 1;
          plVar22 = plVar20;
LAB_00aafe6c:
          puVar2 = (undefined4 *)plVar22[6];
          if (puVar2 < (undefined4 *)plVar22[7]) {
            *puVar2 = uVar15;
            puVar2[1] = uVar14;
                    /* try { // try from 00aafb90 to 00bafbb3 has its CatchHandler @ 00aafda4 */
            puVar2[2] = uVar16;
            puVar2[3] = uVar17;
            puVar2[4] = local_1e8;
            puVar2[5] = local_1ec;
            puVar2[7] = 0;
            *(undefined1 *)(puVar2 + 6) = local_1e4;
            plVar22[6] = (long)(puVar2 + 8);
          }
          else {
            pvVar29 = (void *)plVar22[5];
            lVar28 = (long)puVar2 - (long)pvVar29 >> 5;
            uVar19 = lVar28 + 1;
            if (uVar19 >> 0x3b != 0) {
LAB_00ab004c:
              if (*(long *)(lVar3 + 0x28) == local_70) {
                FUN_00ab17f4();
LAB_00ab0064:
                if (*(long *)(lVar3 + 0x28) == local_70) {
                    /* WARNING: Subroutine does not return */
                  FUN_00440f00();
                }
              }
              goto LAB_00ab00d0;
            }
            uVar24 = plVar22[7] - (long)pvVar29;
            uVar25 = (long)uVar24 >> 4;
            if (uVar25 <= uVar19) {
              uVar25 = uVar19;
            }
            if (0x7fffffffffffffdf < uVar24) {
              uVar25 = 0x7ffffffffffffff;
            }
            if (uVar25 == 0) {
              pvVar21 = (void *)0x0;
            }
            else {
              if (uVar25 >> 0x3b != 0) goto LAB_00ab0064;
              pvVar21 = (void *)_Znwm(uVar25 << 5);
            }
            puVar1 = (undefined4 *)((long)pvVar21 + lVar28 * 0x20);
            puVar1[4] = local_1e8;
            puVar1[5] = local_1ec;
            *puVar1 = uVar15;
            puVar1[1] = uVar14;
                    /* try { // try from 00aafefc to 00baff57 has its CatchHandler @ 00aafefc
                       catch() { ... } // from try @ 00aafefc with catch @ 00aafefc
                       catch() { ... } // from try @ 00ab037c with catch @ 00aafefc */
            puVar1[2] = uVar16;
            puVar1[3] = uVar17;
            *(undefined1 *)(puVar1 + 6) = local_1e4;
            puVar1[7] = 0;
            memcpy(pvVar21,pvVar29,(long)puVar2 - (long)pvVar29);
            plVar22[5] = (long)pvVar21;
            plVar22[6] = (long)(puVar1 + 8);
            plVar22[7] = (long)((long)pvVar21 + uVar25 * 0x20);
            if (pvVar29 != (void *)0x0) {
              _ZdlPv(pvVar29);
            }
            plVar22[6] = (long)(puVar1 + 8);
          }
        }
      }
    }
                    /* try { // try from 00aaff80 to 00baff87 has its CatchHandler @ 00ab0400 */
    FUN_00488698(&local_1c8);
  }
  puVar11 = 
  PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88;
  local_180 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_1c8 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
  *(undefined8 *)((long)&local_180 + *(long *)(local_180 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88 +
        0x18);
  local_178[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                 + 0x10;
                    /* try { // try from 00aaffcc to 00baffeb has its CatchHandler @ 00ab03e8 */
  if ((local_138 & 1) != 0) {
    _ZdlPv(local_128);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_180,puVar11 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_110);
                    /* try { // try from 00aafffc to 00bb0007 has its CatchHandler @ 00ab03d0 */
  if ((local_1a8 & 1) != 0) {
    _ZdlPv(local_198);
  }
  if (local_1c0 != (void *)0x0) {
    local_1b8 = local_1c0;
    _ZdlPv(local_1c0);
  }
                    /* try { // try from 00ab0018 to 00bb0027 has its CatchHandler @ 00ab03c4 */
  if (*(long *)(lVar3 + 0x28) == local_70) {
    return;
  }
LAB_00ab00d0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aafaa4"></a> `00aafaa4` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00aafaa8"></a> `00aafaa8` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafaac"></a> `00aafaac` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aafab0"></a> `00aafab0` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aafab4"></a> `00aafab4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aafab8"></a> `00aafab8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aafabc"></a> `00aafabc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aafac0"></a> `00aafac0` | `ff c3 06 d1` | sub sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00aafac4"></a> `00aafac4` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aafac8"></a> `00aafac8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aafacc"></a> `00aafacc` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafad0"></a> `00aafad0` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00aafad4"></a> `00aafad4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aafad8"></a> `00aafad8` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aafadc"></a> `00aafadc` | `e1 60 e7 97` | bl 0x00487e60 | `UNCONDITIONAL_CALL`
<a id="insn-00aafae0"></a> `00aafae0` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aafae4"></a> `00aafae4` | `a8 0d 00 b0` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-00aafae8"></a> `00aafae8` | `08 21 38 91` | add x8,x8,#0xe08 | `FALL_THROUGH`
<a id="insn-00aafaec"></a> `00aafaec` | `61 8e 40 f8` | ldr x1,[x19, #0x8]! | `FALL_THROUGH`
<a id="insn-00aafaf0"></a> `00aafaf0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aafaf4"></a> `00aafaf4` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aafaf8"></a> `00aafaf8` | `85 e6 f6 97` | bl 0x0086950c | `UNCONDITIONAL_CALL`
<a id="insn-00aafafc"></a> `00aafafc` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aafb00"></a> `00aafb00` | `80 62 00 91` | add x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00aafb04"></a> `00aafb04` | `93 02 00 f9` | str x19,[x20] | `FALL_THROUGH`
<a id="insn-00aafb08"></a> `00aafb08` | `a1 0e 42 f8` | ldr x1,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-00aafb0c"></a> `00aafb0c` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb10"></a> `00aafb10` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb14"></a> `00aafb14` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00aafb18"></a> `00aafb18` | `7d e6 f6 97` | bl 0x0086950c | `UNCONDITIONAL_CALL`
<a id="insn-00aafb1c"></a> `00aafb1c` | `48 05 80 52` | mov w8,#0x2a | `FALL_THROUGH`
<a id="insn-00aafb20"></a> `00aafb20` | `29 c0 ff f0` | adrp x9,0x2b6000 | `FALL_THROUGH`
<a id="insn-00aafb24"></a> `00aafb24` | `29 99 2d 91` | add x9,x9,#0xb66 | `FALL_THROUGH`
<a id="insn-00aafb28"></a> `00aafb28` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aafb2c"></a> `00aafb2c` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aafb30"></a> `00aafb30` | `28 d1 40 f8` | ldur x8,[x9, #0xd] | `FALL_THROUGH`
<a id="insn-00aafb34"></a> `00aafb34` | `95 0e 00 f9` | str x21,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00aafb38"></a> `00aafb38` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aafb3c"></a> `00aafb3c` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aafb40"></a> `00aafb40` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-00aafb44"></a> `00aafb44` | `e0 13 83 3c` | stur q0,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aafb48"></a> `00aafb48` | `e8 e3 03 f8` | stur x8,[sp, #0x3e] | `FALL_THROUGH`
<a id="insn-00aafb4c"></a> `00aafb4c` | `ff 1b 01 39` | strb wzr,[sp, #0x46] | `FALL_THROUGH`
<a id="insn-00aafb50"></a> `00aafb50` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafb54"></a> `00aafb54` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00aafb58"></a> `00aafb58` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aafb5c"></a> `00aafb5c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aafb60"></a> `00aafb60` | `8a 85 01 94` | bl 0x00b11188 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb64"></a> `00aafb64` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aafb68"></a> `00aafb68` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aafb6c"></a> `00aafb6c` | `68 00 00 36` | tbz w8,#0x0,0x00aafb78 | `CONDITIONAL_JUMP`
<a id="insn-00aafb70"></a> `00aafb70` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aafb74"></a> `00aafb74` | `03 a1 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb78"></a> `00aafb78` | `93 20 00 36` | tbz w19,#0x0,0x00aaff88 | `CONDITIONAL_JUMP`
<a id="insn-00aafb7c"></a> `00aafb7c` | `f4 0f 00 f9` | str x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aafb80"></a> `00aafb80` | `0a 00 00 14` | b 0x00aafba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafb84"></a> `00aafb84` | `e9 ab 44 29` | ldp w9,w10,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aafb88"></a> `00aafb88` | `14 55 00 29` | stp w20,w21,[x8] | `FALL_THROUGH`
<a id="insn-00aafb8c"></a> `00aafb8c` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aafb90"></a> `00aafb90` | `16 5d 01 29` | stp w22,w23,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aafb94"></a> `00aafb94` | `0a 25 02 29` | stp w10,w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aafb98"></a> `00aafb98` | `e9 2f 40 b9` | ldr w9,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aafb9c"></a> `00aafb9c` | `1f 1d 00 b9` | str wzr,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aafba0"></a> `00aafba0` | `09 61 00 39` | strb w9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00aafba4"></a> `00aafba4` | `74 1b 00 f9` | str x20,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aafba8"></a> `00aafba8` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafbac"></a> `00aafbac` | `6c 5f e7 97` | bl 0x0048795c | `UNCONDITIONAL_CALL`
<a id="insn-00aafbb0"></a> `00aafbb0` | `80 1e 00 36` | tbz w0,#0x0,0x00aaff80 | `CONDITIONAL_JUMP`
<a id="insn-00aafbb4"></a> `00aafbb4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafbb8"></a> `00aafbb8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aafbbc"></a> `00aafbbc` | `70 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafbc0"></a> `00aafbc0` | `fb 03 00 2a` | mov w27,w0 | `FALL_THROUGH`
<a id="insn-00aafbc4"></a> `00aafbc4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafbc8"></a> `00aafbc8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aafbcc"></a> `00aafbcc` | `6c 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafbd0"></a> `00aafbd0` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00aafbd4"></a> `00aafbd4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafbd8"></a> `00aafbd8` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00aafbdc"></a> `00aafbdc` | `68 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafbe0"></a> `00aafbe0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aafbe4"></a> `00aafbe4` | `fb 41 f5 97` | bl 0x008003d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aafbe8"></a> `00aafbe8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aafbec"></a> `00aafbec` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00aafbf0"></a> `00aafbf0` | `a5 42 f5 97` | bl 0x00800684 | `UNCONDITIONAL_CALL`
<a id="insn-00aafbf4"></a> `00aafbf4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aafbf8"></a> `00aafbf8` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafbfc"></a> `00aafbfc` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00aafc00"></a> `00aafc00` | `5f 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafc04"></a> `00aafc04` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aafc08"></a> `00aafc08` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc0c"></a> `00aafc0c` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aafc10"></a> `00aafc10` | `5b 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafc14"></a> `00aafc14` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aafc18"></a> `00aafc18` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc1c"></a> `00aafc1c` | `5f 62 e7 97` | bl 0x00488598 | `UNCONDITIONAL_CALL`
<a id="insn-00aafc20"></a> `00aafc20` | `1f 18 00 71` | cmp w0,#0x6 | `FALL_THROUGH`
<a id="insn-00aafc24"></a> `00aafc24` | `ab 01 00 54` | b.lt 0x00aafc58 | `CONDITIONAL_JUMP`
<a id="insn-00aafc28"></a> `00aafc28` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc2c"></a> `00aafc2c` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00aafc30"></a> `00aafc30` | `53 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafc34"></a> `00aafc34` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aafc38"></a> `00aafc38` | `00 01 00 54` | b.eq 0x00aafc58 | `CONDITIONAL_JUMP`
<a id="insn-00aafc3c"></a> `00aafc3c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc40"></a> `00aafc40` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00aafc44"></a> `00aafc44` | `4e 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafc48"></a> `00aafc48` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafc4c"></a> `00aafc4c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00aafc50"></a> `00aafc50` | `e8 2f 00 b9` | str w8,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aafc54"></a> `00aafc54` | `02 00 00 14` | b 0x00aafc5c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafc58"></a> `00aafc58` | `ff 2f 00 b9` | str wzr,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aafc5c"></a> `00aafc5c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc60"></a> `00aafc60` | `4e 62 e7 97` | bl 0x00488598 | `UNCONDITIONAL_CALL`
<a id="insn-00aafc64"></a> `00aafc64` | `1f 1c 00 71` | cmp w0,#0x7 | `FALL_THROUGH`
<a id="insn-00aafc68"></a> `00aafc68` | `8a 00 00 54` | b.ge 0x00aafc78 | `CONDITIONAL_JUMP`
<a id="insn-00aafc6c"></a> `00aafc6c` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aafc70"></a> `00aafc70` | `e8 2b 00 b9` | str w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aafc74"></a> `00aafc74` | `05 00 00 14` | b 0x00aafc88 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafc78"></a> `00aafc78` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc7c"></a> `00aafc7c` | `c1 00 80 52` | mov w1,#0x6 | `FALL_THROUGH`
<a id="insn-00aafc80"></a> `00aafc80` | `3f 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafc84"></a> `00aafc84` | `e0 2b 00 b9` | str w0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aafc88"></a> `00aafc88` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafc8c"></a> `00aafc8c` | `43 62 e7 97` | bl 0x00488598 | `UNCONDITIONAL_CALL`
<a id="insn-00aafc90"></a> `00aafc90` | `1f 20 00 71` | cmp w0,#0x8 | `FALL_THROUGH`
<a id="insn-00aafc94"></a> `00aafc94` | `8a 00 00 54` | b.ge 0x00aafca4 | `CONDITIONAL_JUMP`
<a id="insn-00aafc98"></a> `00aafc98` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aafc9c"></a> `00aafc9c` | `e8 27 00 b9` | str w8,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aafca0"></a> `00aafca0` | `05 00 00 14` | b 0x00aafcb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafca4"></a> `00aafca4` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aafca8"></a> `00aafca8` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00aafcac"></a> `00aafcac` | `34 5f e7 97` | bl 0x0048797c | `UNCONDITIONAL_CALL`
<a id="insn-00aafcb0"></a> `00aafcb0` | `e0 27 00 b9` | str w0,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aafcb4"></a> `00aafcb4` | `7f 07 00 71` | cmp w27,#0x1 | `FALL_THROUGH`
<a id="insn-00aafcb8"></a> `00aafcb8` | `a0 04 00 54` | b.eq 0x00aafd4c | `CONDITIONAL_JUMP`
<a id="insn-00aafcbc"></a> `00aafcbc` | `7b f7 ff 35` | cbnz w27,0x00aafba8 | `CONDITIONAL_JUMP`
<a id="insn-00aafcc0"></a> `00aafcc0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafcc4"></a> `00aafcc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafcc8"></a> `00aafcc8` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00aafccc"></a> `00aafccc` | `48 01 00 b4` | cbz x8,0x00aafcf4 | `CONDITIONAL_JUMP`
<a id="insn-00aafcd0"></a> `00aafcd0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00aafcd4"></a> `00aafcd4` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafcd8"></a> `00aafcd8` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00aafcdc"></a> `00aafcdc` | `4b ff ff 54` | b.lt 0x00aafcc4 | `CONDITIONAL_JUMP`
<a id="insn-00aafce0"></a> `00aafce0` | `1f 01 1a 6b` | cmp w8,w26 | `FALL_THROUGH`
<a id="insn-00aafce4"></a> `00aafce4` | `2a 0c 00 54` | b.ge 0x00aafe68 | `CONDITIONAL_JUMP`
<a id="insn-00aafce8"></a> `00aafce8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aafcec"></a> `00aafcec` | `28 ff ff b5` | cbnz x8,0x00aafcd0 | `CONDITIONAL_JUMP`
<a id="insn-00aafcf0"></a> `00aafcf0` | `7c 22 00 91` | add x28,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aafcf4"></a> `00aafcf4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aafcf8"></a> `00aafcf8` | `9a a0 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aafcfc"></a> `00aafcfc` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd00"></a> `00aafd00` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aafd04"></a> `00aafd04` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00aafd08"></a> `00aafd08` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aafd0c"></a> `00aafd0c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aafd10"></a> `00aafd10` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aafd14"></a> `00aafd14` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aafd18"></a> `00aafd18` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00aafd1c"></a> `00aafd1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafd20"></a> `00aafd20` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aafd24"></a> `00aafd24` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aafd28"></a> `00aafd28` | `68 00 00 b4` | cbz x8,0x00aafd34 | `CONDITIONAL_JUMP`
<a id="insn-00aafd2c"></a> `00aafd2c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafd30"></a> `00aafd30` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00aafd34"></a> `00aafd34` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aafd38"></a> `00aafd38` | `ab 2f e6 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00aafd3c"></a> `00aafd3c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd40"></a> `00aafd40` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafd44"></a> `00aafd44` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd48"></a> `00aafd48` | `49 00 00 14` | b 0x00aafe6c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafd4c"></a> `00aafd4c` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aafd50"></a> `00aafd50` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aafd54"></a> `00aafd54` | `fc 03 13 aa` | mov x28,x19 | `FALL_THROUGH`
<a id="insn-00aafd58"></a> `00aafd58` | `48 01 00 b4` | cbz x8,0x00aafd80 | `CONDITIONAL_JUMP`
<a id="insn-00aafd5c"></a> `00aafd5c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00aafd60"></a> `00aafd60` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafd64"></a> `00aafd64` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00aafd68"></a> `00aafd68` | `4b ff ff 54` | b.lt 0x00aafd50 | `CONDITIONAL_JUMP`
<a id="insn-00aafd6c"></a> `00aafd6c` | `1f 01 1a 6b` | cmp w8,w26 | `FALL_THROUGH`
<a id="insn-00aafd70"></a> `00aafd70` | `4a 03 00 54` | b.ge 0x00aafdd8 | `CONDITIONAL_JUMP`
<a id="insn-00aafd74"></a> `00aafd74` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aafd78"></a> `00aafd78` | `28 ff ff b5` | cbnz x8,0x00aafd5c | `CONDITIONAL_JUMP`
<a id="insn-00aafd7c"></a> `00aafd7c` | `7c 22 00 91` | add x28,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aafd80"></a> `00aafd80` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aafd84"></a> `00aafd84` | `77 a0 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aafd88"></a> `00aafd88` | `13 08 00 f9` | str x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd8c"></a> `00aafd8c` | `f3 0f 40 f9` | ldr x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aafd90"></a> `00aafd90` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00aafd94"></a> `00aafd94` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aafd98"></a> `00aafd98` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aafd9c"></a> `00aafd9c` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aafda0"></a> `00aafda0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aafda4"></a> `00aafda4` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-00aafda8"></a> `00aafda8` | `68 82 41 f8` | ldur x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aafdac"></a> `00aafdac` | `1a 20 00 b9` | str w26,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aafdb0"></a> `00aafdb0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aafdb4"></a> `00aafdb4` | `68 00 00 b4` | cbz x8,0x00aafdc0 | `CONDITIONAL_JUMP`
<a id="insn-00aafdb8"></a> `00aafdb8` | `68 82 01 f8` | stur x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aafdbc"></a> `00aafdbc` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00aafdc0"></a> `00aafdc0` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aafdc4"></a> `00aafdc4` | `88 2f e6 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00aafdc8"></a> `00aafdc8` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aafdcc"></a> `00aafdcc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafdd0"></a> `00aafdd0` | `68 16 00 f9` | str x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aafdd4"></a> `00aafdd4` | `02 00 00 14` | b 0x00aafddc | `UNCONDITIONAL_JUMP`
<a id="insn-00aafdd8"></a> `00aafdd8` | `fb 03 13 aa` | mov x27,x19 | `FALL_THROUGH`
<a id="insn-00aafddc"></a> `00aafddc` | `68 27 43 a9` | ldp x8,x9,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aafde0"></a> `00aafde0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aafde4"></a> `00aafde4` | `62 01 00 54` | b.cs 0x00aafe10 | `CONDITIONAL_JUMP`
<a id="insn-00aafde8"></a> `00aafde8` | `e9 ab 44 29` | ldp w9,w10,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aafdec"></a> `00aafdec` | `14 55 00 29` | stp w20,w21,[x8] | `FALL_THROUGH`
<a id="insn-00aafdf0"></a> `00aafdf0` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aafdf4"></a> `00aafdf4` | `16 5d 01 29` | stp w22,w23,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aafdf8"></a> `00aafdf8` | `0a 25 02 29` | stp w10,w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aafdfc"></a> `00aafdfc` | `e9 2f 40 b9` | ldr w9,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aafe00"></a> `00aafe00` | `1f 1d 00 b9` | str wzr,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aafe04"></a> `00aafe04` | `09 61 00 39` | strb w9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00aafe08"></a> `00aafe08` | `74 1b 00 f9` | str x20,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aafe0c"></a> `00aafe0c` | `67 ff ff 17` | b 0x00aafba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafe10"></a> `00aafe10` | `60 a3 00 91` | add x0,x27,#0x28 | `FALL_THROUGH`
<a id="insn-00aafe14"></a> `00aafe14` | `1a 00 40 f9` | ldr x26,[x0] | `FALL_THROUGH`
<a id="insn-00aafe18"></a> `00aafe18` | `1c 01 1a cb` | sub x28,x8,x26 | `FALL_THROUGH`
<a id="insn-00aafe1c"></a> `00aafe1c` | `98 ff 45 93` | asr x24,x28,#0x5 | `FALL_THROUGH`
<a id="insn-00aafe20"></a> `00aafe20` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aafe24"></a> `00aafe24` | `0a fd 7b d3` | lsr x10,x8,#0x3b | `FALL_THROUGH`
<a id="insn-00aafe28"></a> `00aafe28` | `2a 11 00 b5` | cbnz x10,0x00ab004c | `CONDITIONAL_JUMP`
<a id="insn-00aafe2c"></a> `00aafe2c` | `29 01 1a cb` | sub x9,x9,x26 | `FALL_THROUGH`
<a id="insn-00aafe30"></a> `00aafe30` | `2a fd 44 93` | asr x10,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00aafe34"></a> `00aafe34` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00aafe38"></a> `00aafe38` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-00aafe3c"></a> `00aafe3c` | `ea e7 7b b2` | orr x10,xzr,#0x7fffffffffffffe0 | `FALL_THROUGH`
<a id="insn-00aafe40"></a> `00aafe40` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00aafe44"></a> `00aafe44` | `09 00 ff 92` | mov x9,#0x7ffffffffffffff | `FALL_THROUGH`
<a id="insn-00aafe48"></a> `00aafe48` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00aafe4c"></a> `00aafe4c` | `f9 06 00 b4` | cbz x25,0x00aaff28 | `CONDITIONAL_JUMP`
<a id="insn-00aafe50"></a> `00aafe50` | `28 ff 7b d3` | lsr x8,x25,#0x3b | `FALL_THROUGH`
<a id="insn-00aafe54"></a> `00aafe54` | `88 10 00 b5` | cbnz x8,0x00ab0064 | `CONDITIONAL_JUMP`
<a id="insn-00aafe58"></a> `00aafe58` | `20 eb 7b d3` | lsl x0,x25,#0x5 | `FALL_THROUGH`
<a id="insn-00aafe5c"></a> `00aafe5c` | `41 a0 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aafe60"></a> `00aafe60` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aafe64"></a> `00aafe64` | `32 00 00 14` | b 0x00aaff2c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafe68"></a> `00aafe68` | `fb 03 13 aa` | mov x27,x19 | `FALL_THROUGH`
<a id="insn-00aafe6c"></a> `00aafe6c` | `68 27 43 a9` | ldp x8,x9,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aafe70"></a> `00aafe70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aafe74"></a> `00aafe74` | `83 e8 ff 54` | b.cc 0x00aafb84 | `CONDITIONAL_JUMP`
<a id="insn-00aafe78"></a> `00aafe78` | `60 a3 00 91` | add x0,x27,#0x28 | `FALL_THROUGH`
<a id="insn-00aafe7c"></a> `00aafe7c` | `1a 00 40 f9` | ldr x26,[x0] | `FALL_THROUGH`
<a id="insn-00aafe80"></a> `00aafe80` | `1c 01 1a cb` | sub x28,x8,x26 | `FALL_THROUGH`
<a id="insn-00aafe84"></a> `00aafe84` | `98 ff 45 93` | asr x24,x28,#0x5 | `FALL_THROUGH`
<a id="insn-00aafe88"></a> `00aafe88` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aafe8c"></a> `00aafe8c` | `0a fd 7b d3` | lsr x10,x8,#0x3b | `FALL_THROUGH`
<a id="insn-00aafe90"></a> `00aafe90` | `ea 0d 00 b5` | cbnz x10,0x00ab004c | `CONDITIONAL_JUMP`
<a id="insn-00aafe94"></a> `00aafe94` | `29 01 1a cb` | sub x9,x9,x26 | `FALL_THROUGH`
<a id="insn-00aafe98"></a> `00aafe98` | `2a fd 44 93` | asr x10,x9,#0x4 | `FALL_THROUGH`
<a id="insn-00aafe9c"></a> `00aafe9c` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00aafea0"></a> `00aafea0` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-00aafea4"></a> `00aafea4` | `ea e7 7b b2` | orr x10,xzr,#0x7fffffffffffffe0 | `FALL_THROUGH`
<a id="insn-00aafea8"></a> `00aafea8` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00aafeac"></a> `00aafeac` | `09 00 ff 92` | mov x9,#0x7ffffffffffffff | `FALL_THROUGH`
<a id="insn-00aafeb0"></a> `00aafeb0` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00aafeb4"></a> `00aafeb4` | `f9 00 00 b4` | cbz x25,0x00aafed0 | `CONDITIONAL_JUMP`
<a id="insn-00aafeb8"></a> `00aafeb8` | `28 ff 7b d3` | lsr x8,x25,#0x3b | `FALL_THROUGH`
<a id="insn-00aafebc"></a> `00aafebc` | `48 0d 00 b5` | cbnz x8,0x00ab0064 | `CONDITIONAL_JUMP`
<a id="insn-00aafec0"></a> `00aafec0` | `20 eb 7b d3` | lsl x0,x25,#0x5 | `FALL_THROUGH`
<a id="insn-00aafec4"></a> `00aafec4` | `27 a0 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aafec8"></a> `00aafec8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aafecc"></a> `00aafecc` | `02 00 00 14` | b 0x00aafed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafed0"></a> `00aafed0` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aafed4"></a> `00aafed4` | `e9 ab 44 29` | ldp w9,w10,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aafed8"></a> `00aafed8` | `68 16 18 8b` | add x8,x19,x24, LSL #0x5 | `FALL_THROUGH`
<a id="insn-00aafedc"></a> `00aafedc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aafee0"></a> `00aafee0` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00aafee4"></a> `00aafee4` | `e2 03 1c aa` | mov x2,x28 | `FALL_THROUGH`
<a id="insn-00aafee8"></a> `00aafee8` | `0a 25 02 29` | stp w10,w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aafeec"></a> `00aafeec` | `e9 2f 40 b9` | ldr w9,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aafef0"></a> `00aafef0` | `14 55 00 29` | stp w20,w21,[x8] | `FALL_THROUGH`
<a id="insn-00aafef4"></a> `00aafef4` | `75 16 19 8b` | add x21,x19,x25, LSL #0x5 | `FALL_THROUGH`
<a id="insn-00aafef8"></a> `00aafef8` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aafefc"></a> `00aafefc` | `16 5d 01 29` | stp w22,w23,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaff00"></a> `00aaff00` | `09 61 00 39` | strb w9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00aaff04"></a> `00aaff04` | `1f 1d 00 b9` | str wzr,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaff08"></a> `00aaff08` | `72 a0 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff0c"></a> `00aaff0c` | `73 d3 02 a9` | stp x19,x20,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00aaff10"></a> `00aaff10` | `75 1f 00 f9` | str x21,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00aaff14"></a> `00aaff14` | `7a 00 00 b4` | cbz x26,0x00aaff20 | `CONDITIONAL_JUMP`
<a id="insn-00aaff18"></a> `00aaff18` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00aaff1c"></a> `00aaff1c` | `19 a0 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff20"></a> `00aaff20` | `74 1b 00 f9` | str x20,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aaff24"></a> `00aaff24` | `21 ff ff 17` | b 0x00aafba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaff28"></a> `00aaff28` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aaff2c"></a> `00aaff2c` | `e9 ab 44 29` | ldp w9,w10,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aaff30"></a> `00aaff30` | `68 16 18 8b` | add x8,x19,x24, LSL #0x5 | `FALL_THROUGH`
<a id="insn-00aaff34"></a> `00aaff34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaff38"></a> `00aaff38` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00aaff3c"></a> `00aaff3c` | `e2 03 1c aa` | mov x2,x28 | `FALL_THROUGH`
<a id="insn-00aaff40"></a> `00aaff40` | `0a 25 02 29` | stp w10,w9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aaff44"></a> `00aaff44` | `e9 2f 40 b9` | ldr w9,[sp, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaff48"></a> `00aaff48` | `14 55 00 29` | stp w20,w21,[x8] | `FALL_THROUGH`
<a id="insn-00aaff4c"></a> `00aaff4c` | `75 16 19 8b` | add x21,x19,x25, LSL #0x5 | `FALL_THROUGH`
<a id="insn-00aaff50"></a> `00aaff50` | `14 81 00 91` | add x20,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aaff54"></a> `00aaff54` | `16 5d 01 29` | stp w22,w23,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aaff58"></a> `00aaff58` | `09 61 00 39` | strb w9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00aaff5c"></a> `00aaff5c` | `1f 1d 00 b9` | str wzr,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaff60"></a> `00aaff60` | `5c a0 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff64"></a> `00aaff64` | `73 d3 02 a9` | stp x19,x20,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00aaff68"></a> `00aaff68` | `75 1f 00 f9` | str x21,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00aaff6c"></a> `00aaff6c` | `7a 00 00 b4` | cbz x26,0x00aaff78 | `CONDITIONAL_JUMP`
<a id="insn-00aaff70"></a> `00aaff70` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00aaff74"></a> `00aaff74` | `03 a0 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff78"></a> `00aaff78` | `74 1b 00 f9` | str x20,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00aaff7c"></a> `00aaff7c` | `0b ff ff 17` | b 0x00aafba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaff80"></a> `00aaff80` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaff84"></a> `00aaff84` | `c5 61 e7 97` | bl 0x00488698 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff88"></a> `00aaff88` | `48 0f 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aaff8c"></a> `00aaff8c` | `55 0f 00 f0` | adrp x21,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aaff90"></a> `00aaff90` | `f4 23 01 91` | add x20,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00aaff94"></a> `00aaff94` | `08 41 46 f9` | ldr x8,[x8, #0xc80] | `FALL_THROUGH`
<a id="insn-00aaff98"></a> `00aaff98` | `b5 46 46 f9` | ldr x21,[x21, #0xc88] | `FALL_THROUGH`
<a id="insn-00aaff9c"></a> `00aaff9c` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-00aaffa0"></a> `00aaffa0` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00aaffa4"></a> `00aaffa4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aaffa8"></a> `00aaffa8` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aaffac"></a> `00aaffac` | `e9 4b 00 f9` | str x9,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aaffb0"></a> `00aaffb0` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00aaffb4"></a> `00aaffb4` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00aaffb8"></a> `00aaffb8` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aaffbc"></a> `00aaffbc` | `48 0f 00 f0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-00aaffc0"></a> `00aaffc0` | `08 49 46 f9` | ldr x8,[x8, #0xc90] | `FALL_THROUGH`
<a id="insn-00aaffc4"></a> `00aaffc4` | `e9 63 43 39` | ldrb w9,[sp, #0xd8] | `FALL_THROUGH`
<a id="insn-00aaffc8"></a> `00aaffc8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00aaffcc"></a> `00aaffcc` | `e8 4f 00 f9` | str x8,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00aaffd0"></a> `00aaffd0` | `69 00 00 36` | tbz w9,#0x0,0x00aaffdc | `CONDITIONAL_JUMP`
<a id="insn-00aaffd4"></a> `00aaffd4` | `e0 77 40 f9` | ldr x0,[sp, #0xe8] | `FALL_THROUGH`
<a id="insn-00aaffd8"></a> `00aaffd8` | `ea 9f 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aaffdc"></a> `00aaffdc` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-00aaffe0"></a> `00aaffe0` | `24 a0 06 94` | bl 0x00c58070 | `UNCONDITIONAL_CALL`
<a id="insn-00aaffe4"></a> `00aaffe4` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00aaffe8"></a> `00aaffe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaffec"></a> `00aaffec` | `25 a0 06 94` | bl 0x00c58080 | `UNCONDITIONAL_CALL`
<a id="insn-00aafff0"></a> `00aafff0` | `80 e2 02 91` | add x0,x20,#0xb8 | `FALL_THROUGH`
<a id="insn-00aafff4"></a> `00aafff4` | `27 a0 06 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00aafff8"></a> `00aafff8` | `e8 a3 41 39` | ldrb w8,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aafffc"></a> `00aafffc` | `68 00 00 36` | tbz w8,#0x0,0x00ab0008 | `CONDITIONAL_JUMP`
<a id="insn-00ab0000"></a> `00ab0000` | `e0 3f 40 f9` | ldr x0,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00ab0004"></a> `00ab0004` | `df 9f 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0008"></a> `00ab0008` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab000c"></a> `00ab000c` | `60 00 00 b4` | cbz x0,0x00ab0018 | `CONDITIONAL_JUMP`
<a id="insn-00ab0010"></a> `00ab0010` | `e0 2f 00 f9` | str x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00ab0014"></a> `00ab0014` | `db 9f 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0018"></a> `00ab0018` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab001c"></a> `00ab001c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0020"></a> `00ab0020` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ab0024"></a> `00ab0024` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0028"></a> `00ab0028` | `41 05 00 54` | b.ne 0x00ab00d0 | `CONDITIONAL_JUMP`
<a id="insn-00ab002c"></a> `00ab002c` | `ff c3 06 91` | add sp,sp,#0x1b0 | `FALL_THROUGH`
<a id="insn-00ab0030"></a> `00ab0030` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab0034"></a> `00ab0034` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0038"></a> `00ab0038` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab003c"></a> `00ab003c` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0040"></a> `00ab0040` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0044"></a> `00ab0044` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00ab0048"></a> `00ab0048` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ab004c"></a> `00ab004c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0050"></a> `00ab0050` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0054"></a> `00ab0054` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ab0058"></a> `00ab0058` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab005c"></a> `00ab005c` | `a1 03 00 54` | b.ne 0x00ab00d0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0060"></a> `00ab0060` | `e5 05 00 94` | bl 0x00ab17f4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0064"></a> `00ab0064` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0068"></a> `00ab0068` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab006c"></a> `00ab006c` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ab0070"></a> `00ab0070` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0074"></a> `00ab0074` | `e1 02 00 54` | b.ne 0x00ab00d0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0078"></a> `00ab0078` | `a2 43 e6 97` | bl 0x00440f00 | `CALL_TERMINATOR`
<a id="insn-00ab00d0"></a> `00ab00d0` | `b8 9f 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aafaa4`](#insn-00aafaa4) 範囲 `[['00aafaa4', '00aafae7']]`
  - `FALL_THROUGH` [`00aafae4`](#insn-00aafae4) → [`00aafae8`](#insn-00aafae8)
- ブロック [`00aafae8`](#insn-00aafae8) 範囲 `[['00aafae8', '00aafb2f']]`
  - `FALL_THROUGH` [`00aafb2c`](#insn-00aafb2c) → [`00aafb30`](#insn-00aafb30)
- ブロック [`00aafb30`](#insn-00aafb30) 範囲 `[['00aafb30', '00aafb57']]`
  - `FALL_THROUGH` [`00aafb54`](#insn-00aafb54) → [`00aafb58`](#insn-00aafb58)
- ブロック [`00aafb58`](#insn-00aafb58) 範囲 `[['00aafb58', '00aafb6f']]`
  - `CONDITIONAL_JUMP` [`00aafb6c`](#insn-00aafb6c) → [`00aafb78`](#insn-00aafb78)
  - `FALL_THROUGH` [`00aafb6c`](#insn-00aafb6c) → [`00aafb70`](#insn-00aafb70)
- ブロック [`00aafb70`](#insn-00aafb70) 範囲 `[['00aafb70', '00aafb77']]`
  - `FALL_THROUGH` [`00aafb74`](#insn-00aafb74) → [`00aafb78`](#insn-00aafb78)
- ブロック [`00aafb78`](#insn-00aafb78) 範囲 `[['00aafb78', '00aafb7b']]`
  - `CONDITIONAL_JUMP` [`00aafb78`](#insn-00aafb78) → [`00aaff88`](#insn-00aaff88)
  - `FALL_THROUGH` [`00aafb78`](#insn-00aafb78) → [`00aafb7c`](#insn-00aafb7c)
- ブロック [`00aafb7c`](#insn-00aafb7c) 範囲 `[['00aafb7c', '00aafb83']]`
  - `UNCONDITIONAL_JUMP` [`00aafb80`](#insn-00aafb80) → [`00aafba8`](#insn-00aafba8)
- ブロック [`00aafb84`](#insn-00aafb84) 範囲 `[['00aafb84', '00aafb8f']]`
  - `FALL_THROUGH` [`00aafb8c`](#insn-00aafb8c) → [`00aafb90`](#insn-00aafb90)
- ブロック [`00aafb90`](#insn-00aafb90) 範囲 `[['00aafb90', '00aafba7']]`
  - `FALL_THROUGH` [`00aafba4`](#insn-00aafba4) → [`00aafba8`](#insn-00aafba8)
- ブロック [`00aafba8`](#insn-00aafba8) 範囲 `[['00aafba8', '00aafbb3']]`
  - `CONDITIONAL_JUMP` [`00aafbb0`](#insn-00aafbb0) → [`00aaff80`](#insn-00aaff80)
  - `FALL_THROUGH` [`00aafbb0`](#insn-00aafbb0) → [`00aafbb4`](#insn-00aafbb4)
- ブロック [`00aafbb4`](#insn-00aafbb4) 範囲 `[['00aafbb4', '00aafbcb']]`
  - `FALL_THROUGH` [`00aafbc8`](#insn-00aafbc8) → [`00aafbcc`](#insn-00aafbcc)
- ブロック [`00aafbcc`](#insn-00aafbcc) 範囲 `[['00aafbcc', '00aafbf3']]`
  - `FALL_THROUGH` [`00aafbf0`](#insn-00aafbf0) → [`00aafbf4`](#insn-00aafbf4)
- ブロック [`00aafbf4`](#insn-00aafbf4) 範囲 `[['00aafbf4', '00aafc03']]`
  - `FALL_THROUGH` [`00aafc00`](#insn-00aafc00) → [`00aafc04`](#insn-00aafc04)
- ブロック [`00aafc04`](#insn-00aafc04) 範囲 `[['00aafc04', '00aafc27']]`
  - `CONDITIONAL_JUMP` [`00aafc24`](#insn-00aafc24) → [`00aafc58`](#insn-00aafc58)
  - `FALL_THROUGH` [`00aafc24`](#insn-00aafc24) → [`00aafc28`](#insn-00aafc28)
- ブロック [`00aafc28`](#insn-00aafc28) 範囲 `[['00aafc28', '00aafc3b']]`
  - `CONDITIONAL_JUMP` [`00aafc38`](#insn-00aafc38) → [`00aafc58`](#insn-00aafc58)
  - `FALL_THROUGH` [`00aafc38`](#insn-00aafc38) → [`00aafc3c`](#insn-00aafc3c)
- ブロック [`00aafc3c`](#insn-00aafc3c) 範囲 `[['00aafc3c', '00aafc57']]`
  - `UNCONDITIONAL_JUMP` [`00aafc54`](#insn-00aafc54) → [`00aafc5c`](#insn-00aafc5c)
- ブロック [`00aafc58`](#insn-00aafc58) 範囲 `[['00aafc58', '00aafc5b']]`
  - `FALL_THROUGH` [`00aafc58`](#insn-00aafc58) → [`00aafc5c`](#insn-00aafc5c)
- ブロック [`00aafc5c`](#insn-00aafc5c) 範囲 `[['00aafc5c', '00aafc6b']]`
  - `CONDITIONAL_JUMP` [`00aafc68`](#insn-00aafc68) → [`00aafc78`](#insn-00aafc78)
  - `FALL_THROUGH` [`00aafc68`](#insn-00aafc68) → [`00aafc6c`](#insn-00aafc6c)
- ブロック [`00aafc6c`](#insn-00aafc6c) 範囲 `[['00aafc6c', '00aafc77']]`
  - `UNCONDITIONAL_JUMP` [`00aafc74`](#insn-00aafc74) → [`00aafc88`](#insn-00aafc88)
- ブロック [`00aafc78`](#insn-00aafc78) 範囲 `[['00aafc78', '00aafc87']]`
  - `FALL_THROUGH` [`00aafc84`](#insn-00aafc84) → [`00aafc88`](#insn-00aafc88)
- ブロック [`00aafc88`](#insn-00aafc88) 範囲 `[['00aafc88', '00aafc97']]`
  - `CONDITIONAL_JUMP` [`00aafc94`](#insn-00aafc94) → [`00aafca4`](#insn-00aafca4)
  - `FALL_THROUGH` [`00aafc94`](#insn-00aafc94) → [`00aafc98`](#insn-00aafc98)
- ブロック [`00aafc98`](#insn-00aafc98) 範囲 `[['00aafc98', '00aafca3']]`
  - `UNCONDITIONAL_JUMP` [`00aafca0`](#insn-00aafca0) → [`00aafcb4`](#insn-00aafcb4)
- ブロック [`00aafca4`](#insn-00aafca4) 範囲 `[['00aafca4', '00aafcb3']]`
  - `FALL_THROUGH` [`00aafcb0`](#insn-00aafcb0) → [`00aafcb4`](#insn-00aafcb4)
- ブロック [`00aafcb4`](#insn-00aafcb4) 範囲 `[['00aafcb4', '00aafcbb']]`
  - `CONDITIONAL_JUMP` [`00aafcb8`](#insn-00aafcb8) → [`00aafd4c`](#insn-00aafd4c)
  - `FALL_THROUGH` [`00aafcb8`](#insn-00aafcb8) → [`00aafcbc`](#insn-00aafcbc)
- ブロック [`00aafcbc`](#insn-00aafcbc) 範囲 `[['00aafcbc', '00aafcbf']]`
  - `CONDITIONAL_JUMP` [`00aafcbc`](#insn-00aafcbc) → [`00aafba8`](#insn-00aafba8)
  - `FALL_THROUGH` [`00aafcbc`](#insn-00aafcbc) → [`00aafcc0`](#insn-00aafcc0)
- ブロック [`00aafcc0`](#insn-00aafcc0) 範囲 `[['00aafcc0', '00aafcc3']]`
  - `FALL_THROUGH` [`00aafcc0`](#insn-00aafcc0) → [`00aafcc4`](#insn-00aafcc4)
- ブロック [`00aafcc4`](#insn-00aafcc4) 範囲 `[['00aafcc4', '00aafccf']]`
  - `CONDITIONAL_JUMP` [`00aafccc`](#insn-00aafccc) → [`00aafcf4`](#insn-00aafcf4)
  - `FALL_THROUGH` [`00aafccc`](#insn-00aafccc) → [`00aafcd0`](#insn-00aafcd0)
- ブロック [`00aafcd0`](#insn-00aafcd0) 範囲 `[['00aafcd0', '00aafcdf']]`
  - `CONDITIONAL_JUMP` [`00aafcdc`](#insn-00aafcdc) → [`00aafcc4`](#insn-00aafcc4)
  - `FALL_THROUGH` [`00aafcdc`](#insn-00aafcdc) → [`00aafce0`](#insn-00aafce0)
- ブロック [`00aafce0`](#insn-00aafce0) 範囲 `[['00aafce0', '00aafce7']]`
  - `CONDITIONAL_JUMP` [`00aafce4`](#insn-00aafce4) → [`00aafe68`](#insn-00aafe68)
  - `FALL_THROUGH` [`00aafce4`](#insn-00aafce4) → [`00aafce8`](#insn-00aafce8)
- ブロック [`00aafce8`](#insn-00aafce8) 範囲 `[['00aafce8', '00aafcef']]`
  - `CONDITIONAL_JUMP` [`00aafcec`](#insn-00aafcec) → [`00aafcd0`](#insn-00aafcd0)
  - `FALL_THROUGH` [`00aafcec`](#insn-00aafcec) → [`00aafcf0`](#insn-00aafcf0)
- ブロック [`00aafcf0`](#insn-00aafcf0) 範囲 `[['00aafcf0', '00aafcf3']]`
  - `FALL_THROUGH` [`00aafcf0`](#insn-00aafcf0) → [`00aafcf4`](#insn-00aafcf4)
- ブロック [`00aafcf4`](#insn-00aafcf4) 範囲 `[['00aafcf4', '00aafd2b']]`
  - `CONDITIONAL_JUMP` [`00aafd28`](#insn-00aafd28) → [`00aafd34`](#insn-00aafd34)
  - `FALL_THROUGH` [`00aafd28`](#insn-00aafd28) → [`00aafd2c`](#insn-00aafd2c)
- ブロック [`00aafd2c`](#insn-00aafd2c) 範囲 `[['00aafd2c', '00aafd33']]`
  - `FALL_THROUGH` [`00aafd30`](#insn-00aafd30) → [`00aafd34`](#insn-00aafd34)
- ブロック [`00aafd34`](#insn-00aafd34) 範囲 `[['00aafd34', '00aafd4b']]`
  - `UNCONDITIONAL_JUMP` [`00aafd48`](#insn-00aafd48) → [`00aafe6c`](#insn-00aafe6c)
- ブロック [`00aafd4c`](#insn-00aafd4c) 範囲 `[['00aafd4c', '00aafd4f']]`
  - `FALL_THROUGH` [`00aafd4c`](#insn-00aafd4c) → [`00aafd50`](#insn-00aafd50)
- ブロック [`00aafd50`](#insn-00aafd50) 範囲 `[['00aafd50', '00aafd5b']]`
  - `CONDITIONAL_JUMP` [`00aafd58`](#insn-00aafd58) → [`00aafd80`](#insn-00aafd80)
  - `FALL_THROUGH` [`00aafd58`](#insn-00aafd58) → [`00aafd5c`](#insn-00aafd5c)
- ブロック [`00aafd5c`](#insn-00aafd5c) 範囲 `[['00aafd5c', '00aafd63']]`
  - `FALL_THROUGH` [`00aafd60`](#insn-00aafd60) → [`00aafd64`](#insn-00aafd64)
- ブロック [`00aafd64`](#insn-00aafd64) 範囲 `[['00aafd64', '00aafd6b']]`
  - `CONDITIONAL_JUMP` [`00aafd68`](#insn-00aafd68) → [`00aafd50`](#insn-00aafd50)
  - `FALL_THROUGH` [`00aafd68`](#insn-00aafd68) → [`00aafd6c`](#insn-00aafd6c)
- ブロック [`00aafd6c`](#insn-00aafd6c) 範囲 `[['00aafd6c', '00aafd73']]`
  - `CONDITIONAL_JUMP` [`00aafd70`](#insn-00aafd70) → [`00aafdd8`](#insn-00aafdd8)
  - `FALL_THROUGH` [`00aafd70`](#insn-00aafd70) → [`00aafd74`](#insn-00aafd74)
- ブロック [`00aafd74`](#insn-00aafd74) 範囲 `[['00aafd74', '00aafd7b']]`
  - `CONDITIONAL_JUMP` [`00aafd78`](#insn-00aafd78) → [`00aafd5c`](#insn-00aafd5c)
  - `FALL_THROUGH` [`00aafd78`](#insn-00aafd78) → [`00aafd7c`](#insn-00aafd7c)
- ブロック [`00aafd7c`](#insn-00aafd7c) 範囲 `[['00aafd7c', '00aafd7f']]`
  - `FALL_THROUGH` [`00aafd7c`](#insn-00aafd7c) → [`00aafd80`](#insn-00aafd80)
- ブロック [`00aafd80`](#insn-00aafd80) 範囲 `[['00aafd80', '00aafda3']]`
  - `FALL_THROUGH` [`00aafda0`](#insn-00aafda0) → [`00aafda4`](#insn-00aafda4)
- ブロック [`00aafda4`](#insn-00aafda4) 範囲 `[['00aafda4', '00aafdb3']]`
  - `FALL_THROUGH` [`00aafdb0`](#insn-00aafdb0) → [`00aafdb4`](#insn-00aafdb4)
- ブロック [`00aafdb4`](#insn-00aafdb4) 範囲 `[['00aafdb4', '00aafdb7']]`
  - `CONDITIONAL_JUMP` [`00aafdb4`](#insn-00aafdb4) → [`00aafdc0`](#insn-00aafdc0)
  - `FALL_THROUGH` [`00aafdb4`](#insn-00aafdb4) → [`00aafdb8`](#insn-00aafdb8)
- ブロック [`00aafdb8`](#insn-00aafdb8) 範囲 `[['00aafdb8', '00aafdbf']]`
  - `FALL_THROUGH` [`00aafdbc`](#insn-00aafdbc) → [`00aafdc0`](#insn-00aafdc0)
- ブロック [`00aafdc0`](#insn-00aafdc0) 範囲 `[['00aafdc0', '00aafdd7']]`
  - `UNCONDITIONAL_JUMP` [`00aafdd4`](#insn-00aafdd4) → [`00aafddc`](#insn-00aafddc)
- ブロック [`00aafdd8`](#insn-00aafdd8) 範囲 `[['00aafdd8', '00aafddb']]`
  - `FALL_THROUGH` [`00aafdd8`](#insn-00aafdd8) → [`00aafddc`](#insn-00aafddc)
- ブロック [`00aafddc`](#insn-00aafddc) 範囲 `[['00aafddc', '00aafde7']]`
  - `CONDITIONAL_JUMP` [`00aafde4`](#insn-00aafde4) → [`00aafe10`](#insn-00aafe10)
  - `FALL_THROUGH` [`00aafde4`](#insn-00aafde4) → [`00aafde8`](#insn-00aafde8)
- ブロック [`00aafde8`](#insn-00aafde8) 範囲 `[['00aafde8', '00aafdef']]`
  - `FALL_THROUGH` [`00aafdec`](#insn-00aafdec) → [`00aafdf0`](#insn-00aafdf0)
- ブロック [`00aafdf0`](#insn-00aafdf0) 範囲 `[['00aafdf0', '00aafdf7']]`
  - `FALL_THROUGH` [`00aafdf4`](#insn-00aafdf4) → [`00aafdf8`](#insn-00aafdf8)
- ブロック [`00aafdf8`](#insn-00aafdf8) 範囲 `[['00aafdf8', '00aafe0f']]`
  - `UNCONDITIONAL_JUMP` [`00aafe0c`](#insn-00aafe0c) → [`00aafba8`](#insn-00aafba8)
- ブロック [`00aafe10`](#insn-00aafe10) 範囲 `[['00aafe10', '00aafe2b']]`
  - `CONDITIONAL_JUMP` [`00aafe28`](#insn-00aafe28) → [`00ab004c`](#insn-00ab004c)
  - `FALL_THROUGH` [`00aafe28`](#insn-00aafe28) → [`00aafe2c`](#insn-00aafe2c)
- ブロック [`00aafe2c`](#insn-00aafe2c) 範囲 `[['00aafe2c', '00aafe2f']]`
  - `FALL_THROUGH` [`00aafe2c`](#insn-00aafe2c) → [`00aafe30`](#insn-00aafe30)
- ブロック [`00aafe30`](#insn-00aafe30) 範囲 `[['00aafe30', '00aafe4f']]`
  - `CONDITIONAL_JUMP` [`00aafe4c`](#insn-00aafe4c) → [`00aaff28`](#insn-00aaff28)
  - `FALL_THROUGH` [`00aafe4c`](#insn-00aafe4c) → [`00aafe50`](#insn-00aafe50)
- ブロック [`00aafe50`](#insn-00aafe50) 範囲 `[['00aafe50', '00aafe57']]`
  - `CONDITIONAL_JUMP` [`00aafe54`](#insn-00aafe54) → [`00ab0064`](#insn-00ab0064)
  - `FALL_THROUGH` [`00aafe54`](#insn-00aafe54) → [`00aafe58`](#insn-00aafe58)
- ブロック [`00aafe58`](#insn-00aafe58) 範囲 `[['00aafe58', '00aafe67']]`
  - `UNCONDITIONAL_JUMP` [`00aafe64`](#insn-00aafe64) → [`00aaff2c`](#insn-00aaff2c)
- ブロック [`00aafe68`](#insn-00aafe68) 範囲 `[['00aafe68', '00aafe6b']]`
  - `FALL_THROUGH` [`00aafe68`](#insn-00aafe68) → [`00aafe6c`](#insn-00aafe6c)
- ブロック [`00aafe6c`](#insn-00aafe6c) 範囲 `[['00aafe6c', '00aafe77']]`
  - `CONDITIONAL_JUMP` [`00aafe74`](#insn-00aafe74) → [`00aafb84`](#insn-00aafb84)
  - `FALL_THROUGH` [`00aafe74`](#insn-00aafe74) → [`00aafe78`](#insn-00aafe78)
- ブロック [`00aafe78`](#insn-00aafe78) 範囲 `[['00aafe78', '00aafe93']]`
  - `CONDITIONAL_JUMP` [`00aafe90`](#insn-00aafe90) → [`00ab004c`](#insn-00ab004c)
  - `FALL_THROUGH` [`00aafe90`](#insn-00aafe90) → [`00aafe94`](#insn-00aafe94)
- ブロック [`00aafe94`](#insn-00aafe94) 範囲 `[['00aafe94', '00aafeb7']]`
  - `CONDITIONAL_JUMP` [`00aafeb4`](#insn-00aafeb4) → [`00aafed0`](#insn-00aafed0)
  - `FALL_THROUGH` [`00aafeb4`](#insn-00aafeb4) → [`00aafeb8`](#insn-00aafeb8)
- ブロック [`00aafeb8`](#insn-00aafeb8) 範囲 `[['00aafeb8', '00aafebf']]`
  - `CONDITIONAL_JUMP` [`00aafebc`](#insn-00aafebc) → [`00ab0064`](#insn-00ab0064)
  - `FALL_THROUGH` [`00aafebc`](#insn-00aafebc) → [`00aafec0`](#insn-00aafec0)
- ブロック [`00aafec0`](#insn-00aafec0) 範囲 `[['00aafec0', '00aafecf']]`
  - `UNCONDITIONAL_JUMP` [`00aafecc`](#insn-00aafecc) → [`00aafed4`](#insn-00aafed4)
- ブロック [`00aafed0`](#insn-00aafed0) 範囲 `[['00aafed0', '00aafed3']]`
  - `FALL_THROUGH` [`00aafed0`](#insn-00aafed0) → [`00aafed4`](#insn-00aafed4)
- ブロック [`00aafed4`](#insn-00aafed4) 範囲 `[['00aafed4', '00aafefb']]`
  - `FALL_THROUGH` [`00aafef8`](#insn-00aafef8) → [`00aafefc`](#insn-00aafefc)
- ブロック [`00aafefc`](#insn-00aafefc) 範囲 `[['00aafefc', '00aaff17']]`
  - `CONDITIONAL_JUMP` [`00aaff14`](#insn-00aaff14) → [`00aaff20`](#insn-00aaff20)
  - `FALL_THROUGH` [`00aaff14`](#insn-00aaff14) → [`00aaff18`](#insn-00aaff18)
- ブロック [`00aaff18`](#insn-00aaff18) 範囲 `[['00aaff18', '00aaff1f']]`
  - `FALL_THROUGH` [`00aaff1c`](#insn-00aaff1c) → [`00aaff20`](#insn-00aaff20)
- ブロック [`00aaff20`](#insn-00aaff20) 範囲 `[['00aaff20', '00aaff27']]`
  - `UNCONDITIONAL_JUMP` [`00aaff24`](#insn-00aaff24) → [`00aafba8`](#insn-00aafba8)
- ブロック [`00aaff28`](#insn-00aaff28) 範囲 `[['00aaff28', '00aaff2b']]`
  - `FALL_THROUGH` [`00aaff28`](#insn-00aaff28) → [`00aaff2c`](#insn-00aaff2c)
- ブロック [`00aaff2c`](#insn-00aaff2c) 範囲 `[['00aaff2c', '00aaff57']]`
  - `FALL_THROUGH` [`00aaff54`](#insn-00aaff54) → [`00aaff58`](#insn-00aaff58)
- ブロック [`00aaff58`](#insn-00aaff58) 範囲 `[['00aaff58', '00aaff67']]`
  - `FALL_THROUGH` [`00aaff64`](#insn-00aaff64) → [`00aaff68`](#insn-00aaff68)
- ブロック [`00aaff68`](#insn-00aaff68) 範囲 `[['00aaff68', '00aaff6f']]`
  - `CONDITIONAL_JUMP` [`00aaff6c`](#insn-00aaff6c) → [`00aaff78`](#insn-00aaff78)
  - `FALL_THROUGH` [`00aaff6c`](#insn-00aaff6c) → [`00aaff70`](#insn-00aaff70)
- ブロック [`00aaff70`](#insn-00aaff70) 範囲 `[['00aaff70', '00aaff73']]`
  - `FALL_THROUGH` [`00aaff70`](#insn-00aaff70) → [`00aaff74`](#insn-00aaff74)
- ブロック [`00aaff74`](#insn-00aaff74) 範囲 `[['00aaff74', '00aaff77']]`
  - `FALL_THROUGH` [`00aaff74`](#insn-00aaff74) → [`00aaff78`](#insn-00aaff78)
- ブロック [`00aaff78`](#insn-00aaff78) 範囲 `[['00aaff78', '00aaff7f']]`
  - `UNCONDITIONAL_JUMP` [`00aaff7c`](#insn-00aaff7c) → [`00aafba8`](#insn-00aafba8)
- ブロック [`00aaff80`](#insn-00aaff80) 範囲 `[['00aaff80', '00aaff87']]`
  - `FALL_THROUGH` [`00aaff84`](#insn-00aaff84) → [`00aaff88`](#insn-00aaff88)
- ブロック [`00aaff88`](#insn-00aaff88) 範囲 `[['00aaff88', '00aaffcb']]`
  - `FALL_THROUGH` [`00aaffc8`](#insn-00aaffc8) → [`00aaffcc`](#insn-00aaffcc)
- ブロック [`00aaffcc`](#insn-00aaffcc) 範囲 `[['00aaffcc', '00aaffd3']]`
  - `CONDITIONAL_JUMP` [`00aaffd0`](#insn-00aaffd0) → [`00aaffdc`](#insn-00aaffdc)
  - `FALL_THROUGH` [`00aaffd0`](#insn-00aaffd0) → [`00aaffd4`](#insn-00aaffd4)
- ブロック [`00aaffd4`](#insn-00aaffd4) 範囲 `[['00aaffd4', '00aaffdb']]`
  - `FALL_THROUGH` [`00aaffd8`](#insn-00aaffd8) → [`00aaffdc`](#insn-00aaffdc)
- ブロック [`00aaffdc`](#insn-00aaffdc) 範囲 `[['00aaffdc', '00aafffb']]`
  - `FALL_THROUGH` [`00aafff8`](#insn-00aafff8) → [`00aafffc`](#insn-00aafffc)
- ブロック [`00aafffc`](#insn-00aafffc) 範囲 `[['00aafffc', '00aaffff']]`
  - `CONDITIONAL_JUMP` [`00aafffc`](#insn-00aafffc) → [`00ab0008`](#insn-00ab0008)
  - `FALL_THROUGH` [`00aafffc`](#insn-00aafffc) → [`00ab0000`](#insn-00ab0000)
- ブロック [`00ab0000`](#insn-00ab0000) 範囲 `[['00ab0000', '00ab0007']]`
  - `FALL_THROUGH` [`00ab0004`](#insn-00ab0004) → [`00ab0008`](#insn-00ab0008)
- ブロック [`00ab0008`](#insn-00ab0008) 範囲 `[['00ab0008', '00ab000f']]`
  - `CONDITIONAL_JUMP` [`00ab000c`](#insn-00ab000c) → [`00ab0018`](#insn-00ab0018)
  - `FALL_THROUGH` [`00ab000c`](#insn-00ab000c) → [`00ab0010`](#insn-00ab0010)
- ブロック [`00ab0010`](#insn-00ab0010) 範囲 `[['00ab0010', '00ab0017']]`
  - `FALL_THROUGH` [`00ab0014`](#insn-00ab0014) → [`00ab0018`](#insn-00ab0018)
- ブロック [`00ab0018`](#insn-00ab0018) 範囲 `[['00ab0018', '00ab002b']]`
  - `CONDITIONAL_JUMP` [`00ab0028`](#insn-00ab0028) → [`00ab00d0`](#insn-00ab00d0)
  - `FALL_THROUGH` [`00ab0028`](#insn-00ab0028) → [`00ab002c`](#insn-00ab002c)
- ブロック [`00ab002c`](#insn-00ab002c) 範囲 `[['00ab002c', '00ab004b']]`
- ブロック [`00ab004c`](#insn-00ab004c) 範囲 `[['00ab004c', '00ab005f']]`
  - `CONDITIONAL_JUMP` [`00ab005c`](#insn-00ab005c) → [`00ab00d0`](#insn-00ab00d0)
  - `FALL_THROUGH` [`00ab005c`](#insn-00ab005c) → [`00ab0060`](#insn-00ab0060)
- ブロック [`00ab0060`](#insn-00ab0060) 範囲 `[['00ab0060', '00ab0063']]`
  - `FALL_THROUGH` [`00ab0060`](#insn-00ab0060) → [`00ab0064`](#insn-00ab0064)
- ブロック [`00ab0064`](#insn-00ab0064) 範囲 `[['00ab0064', '00ab0077']]`
  - `CONDITIONAL_JUMP` [`00ab0074`](#insn-00ab0074) → [`00ab00d0`](#insn-00ab00d0)
  - `FALL_THROUGH` [`00ab0074`](#insn-00ab0074) → [`00ab0078`](#insn-00ab0078)
- ブロック [`00ab0078`](#insn-00ab0078) 範囲 `[['00ab0078', '00ab007b']]`
- ブロック [`00ab00d0`](#insn-00ab00d0) 範囲 `[['00ab00d0', '00ab00d3']]`

## 命令位置別の参照

- [`00aafaa4`](#insn-00aafaa4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafaa8`](#insn-00aafaa8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafaac`](#insn-00aafaac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafab0`](#insn-00aafab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafab4`](#insn-00aafab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafab8`](#insn-00aafab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafad0`](#insn-00aafad0) → `Stack[-0x210]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafad8`](#insn-00aafad8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafadc`](#insn-00aafadc) → [`00487e60`](../00487/00487e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e60` · 推定シンボル `None` · 推定型 `None`
- [`00aafaf4`](#insn-00aafaf4) → `00c64e08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aafaf4`](#insn-00aafaf4) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafaf8`](#insn-00aafaf8) → [`0086950c`](../00869/0086950c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086950c` · 推定シンボル `None` · 推定型 `None`
- [`00aafb10`](#insn-00aafb10) → `Stack[-0x200]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb18`](#insn-00aafb18) → [`0086950c`](../00869/0086950c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086950c` · 推定シンボル `None` · 推定型 `None`
- [`00aafb28`](#insn-00aafb28) → `002b6b66`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aafb2c`](#insn-00aafb2c) → `Stack[-0x1e0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb30`](#insn-00aafb30) → `002b6b73`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aafb3c`](#insn-00aafb3c) → `Stack[-0x208]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb44`](#insn-00aafb44) → `Stack[-0x1df]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb48`](#insn-00aafb48) → `Stack[-0x1d2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb4c`](#insn-00aafb4c) → `Stack[-0x1ca]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb60`](#insn-00aafb60) → [`00b11188`](../00b11/00b11188.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b11188` · 推定シンボル `None` · 推定型 `None`
- [`00aafb64`](#insn-00aafb64) → `Stack[-0x1e0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb6c`](#insn-00aafb6c) → [`00aafb78`](#insn-00aafb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb70`](#insn-00aafb70) → `Stack[-0x1d0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb74`](#insn-00aafb74) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aafb78`](#insn-00aafb78) → [`00aaff88`](#insn-00aaff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb7c`](#insn-00aafb7c) → `Stack[-0x1f8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb80`](#insn-00aafb80) → [`00aafba8`](#insn-00aafba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb84`](#insn-00aafb84) → `Stack[-0x1ec]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb98`](#insn-00aafb98) → `Stack[-0x1e4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafbac`](#insn-00aafbac) → [`0048795c`](../00487/0048795c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048795c` · 推定シンボル `None` · 推定型 `None`
- [`00aafbb0`](#insn-00aafbb0) → [`00aaff80`](#insn-00aaff80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafbbc`](#insn-00aafbbc) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafbcc`](#insn-00aafbcc) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafbdc`](#insn-00aafbdc) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafbe4`](#insn-00aafbe4) → [`008003d0`](../00800/008003d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008003d0` · 推定シンボル `None` · 推定型 `None`
- [`00aafbf0`](#insn-00aafbf0) → [`00800684`](../00800/00800684.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800684` · 推定シンボル `None` · 推定型 `None`
- [`00aafc00`](#insn-00aafc00) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafc10`](#insn-00aafc10) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafc1c`](#insn-00aafc1c) → [`00488598`](../00488/00488598.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488598` · 推定シンボル `None` · 推定型 `None`
- [`00aafc24`](#insn-00aafc24) → [`00aafc58`](#insn-00aafc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc30`](#insn-00aafc30) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafc38`](#insn-00aafc38) → [`00aafc58`](#insn-00aafc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc44`](#insn-00aafc44) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafc50`](#insn-00aafc50) → `Stack[-0x1e4]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc54`](#insn-00aafc54) → [`00aafc5c`](#insn-00aafc5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc58`](#insn-00aafc58) → `Stack[-0x1e4]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc60`](#insn-00aafc60) → [`00488598`](../00488/00488598.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488598` · 推定シンボル `None` · 推定型 `None`
- [`00aafc68`](#insn-00aafc68) → [`00aafc78`](#insn-00aafc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc70`](#insn-00aafc70) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc74`](#insn-00aafc74) → [`00aafc88`](#insn-00aafc88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc80`](#insn-00aafc80) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafc84`](#insn-00aafc84) → `Stack[-0x1e8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc8c`](#insn-00aafc8c) → [`00488598`](../00488/00488598.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488598` · 推定シンボル `None` · 推定型 `None`
- [`00aafc94`](#insn-00aafc94) → [`00aafca4`](#insn-00aafca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc9c`](#insn-00aafc9c) → `Stack[-0x1ec]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafca0`](#insn-00aafca0) → [`00aafcb4`](#insn-00aafcb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcac`](#insn-00aafcac) → [`0048797c`](../00487/0048797c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048797c` · 推定シンボル `None` · 推定型 `None`
- [`00aafcb0`](#insn-00aafcb0) → `Stack[-0x1ec]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcb8`](#insn-00aafcb8) → [`00aafd4c`](#insn-00aafd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcbc`](#insn-00aafcbc) → [`00aafba8`](#insn-00aafba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcc0`](#insn-00aafcc0) → `Stack[-0x200]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafccc`](#insn-00aafccc) → [`00aafcf4`](#insn-00aafcf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcdc`](#insn-00aafcdc) → [`00aafcc4`](#insn-00aafcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafce4`](#insn-00aafce4) → [`00aafe68`](#insn-00aafe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcec`](#insn-00aafcec) → [`00aafcd0`](#insn-00aafcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcf8`](#insn-00aafcf8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aafd00`](#insn-00aafd00) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd28`](#insn-00aafd28) → [`00aafd34`](#insn-00aafd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd38`](#insn-00aafd38) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00aafd48`](#insn-00aafd48) → [`00aafe6c`](#insn-00aafe6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd4c`](#insn-00aafd4c) → `Stack[-0x208]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd58`](#insn-00aafd58) → [`00aafd80`](#insn-00aafd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd68`](#insn-00aafd68) → [`00aafd50`](#insn-00aafd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd70`](#insn-00aafd70) → [`00aafdd8`](#insn-00aafdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd78`](#insn-00aafd78) → [`00aafd5c`](#insn-00aafd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd84`](#insn-00aafd84) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aafd8c`](#insn-00aafd8c) → `Stack[-0x1f8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdb4`](#insn-00aafdb4) → [`00aafdc0`](#insn-00aafdc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdc4`](#insn-00aafdc4) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00aafdd4`](#insn-00aafdd4) → [`00aafddc`](#insn-00aafddc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafde4`](#insn-00aafde4) → [`00aafe10`](#insn-00aafe10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafde8`](#insn-00aafde8) → `Stack[-0x1ec]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdfc`](#insn-00aafdfc) → `Stack[-0x1e4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe0c`](#insn-00aafe0c) → [`00aafba8`](#insn-00aafba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe28`](#insn-00aafe28) → [`00ab004c`](#insn-00ab004c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe4c`](#insn-00aafe4c) → [`00aaff28`](#insn-00aaff28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe54`](#insn-00aafe54) → [`00ab0064`](#insn-00ab0064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe5c`](#insn-00aafe5c) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aafe64`](#insn-00aafe64) → [`00aaff2c`](#insn-00aaff2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe74`](#insn-00aafe74) → [`00aafb84`](#insn-00aafb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe90`](#insn-00aafe90) → [`00ab004c`](#insn-00ab004c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafeb4`](#insn-00aafeb4) → [`00aafed0`](#insn-00aafed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafebc`](#insn-00aafebc) → [`00ab0064`](#insn-00ab0064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafec4`](#insn-00aafec4) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aafecc`](#insn-00aafecc) → [`00aafed4`](#insn-00aafed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafed4`](#insn-00aafed4) → `Stack[-0x1ec]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafeec`](#insn-00aafeec) → `Stack[-0x1e4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff08`](#insn-00aaff08) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaff14`](#insn-00aaff14) → [`00aaff20`](#insn-00aaff20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff1c`](#insn-00aaff1c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aaff24`](#insn-00aaff24) → [`00aafba8`](#insn-00aafba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff2c`](#insn-00aaff2c) → `Stack[-0x1ec]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff44`](#insn-00aaff44) → `Stack[-0x1e4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff60`](#insn-00aaff60) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aaff6c`](#insn-00aaff6c) → [`00aaff78`](#insn-00aaff78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff74`](#insn-00aaff74) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aaff7c`](#insn-00aaff7c) → [`00aafba8`](#insn-00aafba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff84`](#insn-00aaff84) → [`00488698`](../00488/00488698.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488698` · 推定シンボル `None` · 推定型 `None`
- [`00aaff94`](#insn-00aaff94) → `00c9ac80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaff98`](#insn-00aaff98) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaffa0`](#insn-00aaffa0) → `00c932d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`00aaffa8`](#insn-00aaffa8) → `00c658e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aaffa8`](#insn-00aaffa8) → `Stack[-0x1c8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffac`](#insn-00aaffac) → `00c910e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaffac`](#insn-00aaffac) → `Stack[-0x180]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffb0`](#insn-00aaffb0) → `00c910c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`00aaffb4`](#insn-00aaffb4) → `00c932e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`00aaffb8`](#insn-00aaffb8) → `00c91108`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaffc0`](#insn-00aaffc0) → `00c9ac90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aaffc4`](#insn-00aaffc4) → `Stack[-0x138]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffcc`](#insn-00aaffcc) → `00c90cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`00aaffcc`](#insn-00aaffcc) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffd0`](#insn-00aaffd0) → [`00aaffdc`](#insn-00aaffdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffd4`](#insn-00aaffd4) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffd8`](#insn-00aaffd8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aaffe0`](#insn-00aaffe0) → [`00c58070`](../00c58/00c58070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58070` · 推定シンボル `None` · 推定型 `None`
- [`00aaffe4`](#insn-00aaffe4) → `00c932d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`00aaffec`](#insn-00aaffec) → [`00c58080`](../00c58/00c58080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58080` · 推定シンボル `None` · 推定型 `None`
- [`00aafff4`](#insn-00aafff4) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00aafff8`](#insn-00aafff8) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafffc`](#insn-00aafffc) → [`00ab0008`](#insn-00ab0008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0000`](#insn-00ab0000) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0004`](#insn-00ab0004) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00ab0008`](#insn-00ab0008) → `Stack[-0x1c0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab000c`](#insn-00ab000c) → [`00ab0018`](#insn-00ab0018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0010`](#insn-00ab0010) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0014`](#insn-00ab0014) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00ab0018`](#insn-00ab0018) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0020`](#insn-00ab0020) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0028`](#insn-00ab0028) → [`00ab00d0`](#insn-00ab00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0030`](#insn-00ab0030) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0034`](#insn-00ab0034) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0038`](#insn-00ab0038) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab003c`](#insn-00ab003c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0040`](#insn-00ab0040) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0044`](#insn-00ab0044) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab004c`](#insn-00ab004c) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0054`](#insn-00ab0054) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab005c`](#insn-00ab005c) → [`00ab00d0`](#insn-00ab00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0060`](#insn-00ab0060) → [`00ab17f4`](../00ab1/00ab17f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab17f4` · 推定シンボル `None` · 推定型 `None`
- [`00ab0064`](#insn-00ab0064) → `Stack[-0x210]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab006c`](#insn-00ab006c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0074`](#insn-00ab0074) → [`00ab00d0`](#insn-00ab00d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0078`](#insn-00ab0078) → [`00440f00`](../00440/00440f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440f00` · 推定シンボル `None` · 推定型 `None`
- [`00ab00d0`](#insn-00ab00d0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aafaa4`](#insn-00aafaa4)

~~~json
{
  "source": "00aafaa4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafaa8`](#insn-00aafaa8)

~~~json
{
  "source": "00aafaa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafaac`](#insn-00aafaac)

~~~json
{
  "source": "00aafaac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafab0`](#insn-00aafab0)

~~~json
{
  "source": "00aafab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafab4`](#insn-00aafab4)

~~~json
{
  "source": "00aafab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafab8`](#insn-00aafab8)

~~~json
{
  "source": "00aafab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafad0`](#insn-00aafad0)

~~~json
{
  "source": "00aafad0",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafad8`](#insn-00aafad8)

~~~json
{
  "source": "00aafad8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafadc`](#insn-00aafadc)

~~~json
{
  "source": "00aafadc",
  "target": "00487e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafaf4`](#insn-00aafaf4)

~~~json
{
  "source": "00aafaf4",
  "target": "00c64e08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64e08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aafaf4`](#insn-00aafaf4)

~~~json
{
  "source": "00aafaf4",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafaf8`](#insn-00aafaf8)

~~~json
{
  "source": "00aafaf8",
  "target": "0086950c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb10`](#insn-00aafb10)

~~~json
{
  "source": "00aafb10",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb18`](#insn-00aafb18)

~~~json
{
  "source": "00aafb18",
  "target": "0086950c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb28`](#insn-00aafb28)

~~~json
{
  "source": "00aafb28",
  "target": "002b6b66",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b6b66",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "4d617053746167655f53686f72746375742e63737600",
  "capture_start": "002b6b66",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafb2c`](#insn-00aafb2c)

~~~json
{
  "source": "00aafb2c",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb30`](#insn-00aafb30)

~~~json
{
  "source": "00aafb30",
  "target": "002b6b73",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b6b66",
  "offset": 13,
  "size": 22,
  "datatype": "string",
  "bytes": "4d617053746167655f53686f72746375742e63737600",
  "capture_start": "002b6b66",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafb3c`](#insn-00aafb3c)

~~~json
{
  "source": "00aafb3c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb44`](#insn-00aafb44)

~~~json
{
  "source": "00aafb44",
  "target": "Stack[-0x1df]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb48`](#insn-00aafb48)

~~~json
{
  "source": "00aafb48",
  "target": "Stack[-0x1d2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb4c`](#insn-00aafb4c)

~~~json
{
  "source": "00aafb4c",
  "target": "Stack[-0x1ca]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb60`](#insn-00aafb60)

~~~json
{
  "source": "00aafb60",
  "target": "00b11188",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb64`](#insn-00aafb64)

~~~json
{
  "source": "00aafb64",
  "target": "Stack[-0x1e0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb6c`](#insn-00aafb6c)

~~~json
{
  "source": "00aafb6c",
  "target": "00aafb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb70`](#insn-00aafb70)

~~~json
{
  "source": "00aafb70",
  "target": "Stack[-0x1d0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb74`](#insn-00aafb74)

~~~json
{
  "source": "00aafb74",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb78`](#insn-00aafb78)

~~~json
{
  "source": "00aafb78",
  "target": "00aaff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb7c`](#insn-00aafb7c)

~~~json
{
  "source": "00aafb7c",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb80`](#insn-00aafb80)

~~~json
{
  "source": "00aafb80",
  "target": "00aafba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb84`](#insn-00aafb84)

~~~json
{
  "source": "00aafb84",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb98`](#insn-00aafb98)

~~~json
{
  "source": "00aafb98",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafbac`](#insn-00aafbac)

~~~json
{
  "source": "00aafbac",
  "target": "0048795c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbb0`](#insn-00aafbb0)

~~~json
{
  "source": "00aafbb0",
  "target": "00aaff80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafbbc`](#insn-00aafbbc)

~~~json
{
  "source": "00aafbbc",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbcc`](#insn-00aafbcc)

~~~json
{
  "source": "00aafbcc",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbdc`](#insn-00aafbdc)

~~~json
{
  "source": "00aafbdc",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbe4`](#insn-00aafbe4)

~~~json
{
  "source": "00aafbe4",
  "target": "008003d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbf0`](#insn-00aafbf0)

~~~json
{
  "source": "00aafbf0",
  "target": "00800684",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc00`](#insn-00aafc00)

~~~json
{
  "source": "00aafc00",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc10`](#insn-00aafc10)

~~~json
{
  "source": "00aafc10",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc1c`](#insn-00aafc1c)

~~~json
{
  "source": "00aafc1c",
  "target": "00488598",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc24`](#insn-00aafc24)

~~~json
{
  "source": "00aafc24",
  "target": "00aafc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc30`](#insn-00aafc30)

~~~json
{
  "source": "00aafc30",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc38`](#insn-00aafc38)

~~~json
{
  "source": "00aafc38",
  "target": "00aafc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc44`](#insn-00aafc44)

~~~json
{
  "source": "00aafc44",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc50`](#insn-00aafc50)

~~~json
{
  "source": "00aafc50",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc54`](#insn-00aafc54)

~~~json
{
  "source": "00aafc54",
  "target": "00aafc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc58`](#insn-00aafc58)

~~~json
{
  "source": "00aafc58",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc60`](#insn-00aafc60)

~~~json
{
  "source": "00aafc60",
  "target": "00488598",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc68`](#insn-00aafc68)

~~~json
{
  "source": "00aafc68",
  "target": "00aafc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc70`](#insn-00aafc70)

~~~json
{
  "source": "00aafc70",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc74`](#insn-00aafc74)

~~~json
{
  "source": "00aafc74",
  "target": "00aafc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc80`](#insn-00aafc80)

~~~json
{
  "source": "00aafc80",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc84`](#insn-00aafc84)

~~~json
{
  "source": "00aafc84",
  "target": "Stack[-0x1e8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc8c`](#insn-00aafc8c)

~~~json
{
  "source": "00aafc8c",
  "target": "00488598",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc94`](#insn-00aafc94)

~~~json
{
  "source": "00aafc94",
  "target": "00aafca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc9c`](#insn-00aafc9c)

~~~json
{
  "source": "00aafc9c",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafca0`](#insn-00aafca0)

~~~json
{
  "source": "00aafca0",
  "target": "00aafcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcac`](#insn-00aafcac)

~~~json
{
  "source": "00aafcac",
  "target": "0048797c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafcb0`](#insn-00aafcb0)

~~~json
{
  "source": "00aafcb0",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcb8`](#insn-00aafcb8)

~~~json
{
  "source": "00aafcb8",
  "target": "00aafd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcbc`](#insn-00aafcbc)

~~~json
{
  "source": "00aafcbc",
  "target": "00aafba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcc0`](#insn-00aafcc0)

~~~json
{
  "source": "00aafcc0",
  "target": "Stack[-0x200]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafccc`](#insn-00aafccc)

~~~json
{
  "source": "00aafccc",
  "target": "00aafcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcdc`](#insn-00aafcdc)

~~~json
{
  "source": "00aafcdc",
  "target": "00aafcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafce4`](#insn-00aafce4)

~~~json
{
  "source": "00aafce4",
  "target": "00aafe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcec`](#insn-00aafcec)

~~~json
{
  "source": "00aafcec",
  "target": "00aafcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcf8`](#insn-00aafcf8)

~~~json
{
  "source": "00aafcf8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafd00`](#insn-00aafd00)

~~~json
{
  "source": "00aafd00",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd28`](#insn-00aafd28)

~~~json
{
  "source": "00aafd28",
  "target": "00aafd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd38`](#insn-00aafd38)

~~~json
{
  "source": "00aafd38",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafd48`](#insn-00aafd48)

~~~json
{
  "source": "00aafd48",
  "target": "00aafe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd4c`](#insn-00aafd4c)

~~~json
{
  "source": "00aafd4c",
  "target": "Stack[-0x208]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd58`](#insn-00aafd58)

~~~json
{
  "source": "00aafd58",
  "target": "00aafd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd68`](#insn-00aafd68)

~~~json
{
  "source": "00aafd68",
  "target": "00aafd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd70`](#insn-00aafd70)

~~~json
{
  "source": "00aafd70",
  "target": "00aafdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd78`](#insn-00aafd78)

~~~json
{
  "source": "00aafd78",
  "target": "00aafd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd84`](#insn-00aafd84)

~~~json
{
  "source": "00aafd84",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafd8c`](#insn-00aafd8c)

~~~json
{
  "source": "00aafd8c",
  "target": "Stack[-0x1f8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdb4`](#insn-00aafdb4)

~~~json
{
  "source": "00aafdb4",
  "target": "00aafdc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdc4`](#insn-00aafdc4)

~~~json
{
  "source": "00aafdc4",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafdd4`](#insn-00aafdd4)

~~~json
{
  "source": "00aafdd4",
  "target": "00aafddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafde4`](#insn-00aafde4)

~~~json
{
  "source": "00aafde4",
  "target": "00aafe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafde8`](#insn-00aafde8)

~~~json
{
  "source": "00aafde8",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdfc`](#insn-00aafdfc)

~~~json
{
  "source": "00aafdfc",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe0c`](#insn-00aafe0c)

~~~json
{
  "source": "00aafe0c",
  "target": "00aafba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe28`](#insn-00aafe28)

~~~json
{
  "source": "00aafe28",
  "target": "00ab004c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe4c`](#insn-00aafe4c)

~~~json
{
  "source": "00aafe4c",
  "target": "00aaff28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe54`](#insn-00aafe54)

~~~json
{
  "source": "00aafe54",
  "target": "00ab0064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe5c`](#insn-00aafe5c)

~~~json
{
  "source": "00aafe5c",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafe64`](#insn-00aafe64)

~~~json
{
  "source": "00aafe64",
  "target": "00aaff2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe74`](#insn-00aafe74)

~~~json
{
  "source": "00aafe74",
  "target": "00aafb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe90`](#insn-00aafe90)

~~~json
{
  "source": "00aafe90",
  "target": "00ab004c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafeb4`](#insn-00aafeb4)

~~~json
{
  "source": "00aafeb4",
  "target": "00aafed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafebc`](#insn-00aafebc)

~~~json
{
  "source": "00aafebc",
  "target": "00ab0064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafec4`](#insn-00aafec4)

~~~json
{
  "source": "00aafec4",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafecc`](#insn-00aafecc)

~~~json
{
  "source": "00aafecc",
  "target": "00aafed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafed4`](#insn-00aafed4)

~~~json
{
  "source": "00aafed4",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafeec`](#insn-00aafeec)

~~~json
{
  "source": "00aafeec",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff08`](#insn-00aaff08)

~~~json
{
  "source": "00aaff08",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff14`](#insn-00aaff14)

~~~json
{
  "source": "00aaff14",
  "target": "00aaff20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff1c`](#insn-00aaff1c)

~~~json
{
  "source": "00aaff1c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff24`](#insn-00aaff24)

~~~json
{
  "source": "00aaff24",
  "target": "00aafba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff2c`](#insn-00aaff2c)

~~~json
{
  "source": "00aaff2c",
  "target": "Stack[-0x1ec]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff44`](#insn-00aaff44)

~~~json
{
  "source": "00aaff44",
  "target": "Stack[-0x1e4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff60`](#insn-00aaff60)

~~~json
{
  "source": "00aaff60",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff6c`](#insn-00aaff6c)

~~~json
{
  "source": "00aaff6c",
  "target": "00aaff78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff74`](#insn-00aaff74)

~~~json
{
  "source": "00aaff74",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff7c`](#insn-00aaff7c)

~~~json
{
  "source": "00aaff7c",
  "target": "00aafba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff84`](#insn-00aaff84)

~~~json
{
  "source": "00aaff84",
  "target": "00488698",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff94`](#insn-00aaff94)

~~~json
{
  "source": "00aaff94",
  "target": "00c9ac80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaff98`](#insn-00aaff98)

~~~json
{
  "source": "00aaff98",
  "target": "00c9ac88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffa0`](#insn-00aaffa0)

~~~json
{
  "source": "00aaffa0",
  "target": "00c932d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffa8`](#insn-00aaffa8)

~~~json
{
  "source": "00aaffa8",
  "target": "00c658e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c658e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffa8`](#insn-00aaffa8)

~~~json
{
  "source": "00aaffa8",
  "target": "Stack[-0x1c8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffac`](#insn-00aaffac)

~~~json
{
  "source": "00aaffac",
  "target": "00c910e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffac`](#insn-00aaffac)

~~~json
{
  "source": "00aaffac",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffb0`](#insn-00aaffb0)

~~~json
{
  "source": "00aaffb0",
  "target": "00c910c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c910c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c910c8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aaffb4`](#insn-00aaffb4)

~~~json
{
  "source": "00aaffb4",
  "target": "00c932e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffb8`](#insn-00aaffb8)

~~~json
{
  "source": "00aaffb8",
  "target": "00c91108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91108",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffc0`](#insn-00aaffc0)

~~~json
{
  "source": "00aaffc0",
  "target": "00c9ac90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffc4`](#insn-00aaffc4)

~~~json
{
  "source": "00aaffc4",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffcc`](#insn-00aaffcc)

~~~json
{
  "source": "00aaffcc",
  "target": "00c90cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90cc8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00aaffcc`](#insn-00aaffcc)

~~~json
{
  "source": "00aaffcc",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffd0`](#insn-00aaffd0)

~~~json
{
  "source": "00aaffd0",
  "target": "00aaffdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffd4`](#insn-00aaffd4)

~~~json
{
  "source": "00aaffd4",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffd8`](#insn-00aaffd8)

~~~json
{
  "source": "00aaffd8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaffe0`](#insn-00aaffe0)

~~~json
{
  "source": "00aaffe0",
  "target": "00c58070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaffe4`](#insn-00aaffe4)

~~~json
{
  "source": "00aaffe4",
  "target": "00c932d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c932d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aaffec`](#insn-00aaffec)

~~~json
{
  "source": "00aaffec",
  "target": "00c58080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafff4`](#insn-00aafff4)

~~~json
{
  "source": "00aafff4",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafff8`](#insn-00aafff8)

~~~json
{
  "source": "00aafff8",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafffc`](#insn-00aafffc)

~~~json
{
  "source": "00aafffc",
  "target": "00ab0008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0000`](#insn-00ab0000)

~~~json
{
  "source": "00ab0000",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0004`](#insn-00ab0004)

~~~json
{
  "source": "00ab0004",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0008`](#insn-00ab0008)

~~~json
{
  "source": "00ab0008",
  "target": "Stack[-0x1c0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab000c`](#insn-00ab000c)

~~~json
{
  "source": "00ab000c",
  "target": "00ab0018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0010`](#insn-00ab0010)

~~~json
{
  "source": "00ab0010",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0014`](#insn-00ab0014)

~~~json
{
  "source": "00ab0014",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0018`](#insn-00ab0018)

~~~json
{
  "source": "00ab0018",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0020`](#insn-00ab0020)

~~~json
{
  "source": "00ab0020",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0028`](#insn-00ab0028)

~~~json
{
  "source": "00ab0028",
  "target": "00ab00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0030`](#insn-00ab0030)

~~~json
{
  "source": "00ab0030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0034`](#insn-00ab0034)

~~~json
{
  "source": "00ab0034",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0038`](#insn-00ab0038)

~~~json
{
  "source": "00ab0038",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab003c`](#insn-00ab003c)

~~~json
{
  "source": "00ab003c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0040`](#insn-00ab0040)

~~~json
{
  "source": "00ab0040",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0044`](#insn-00ab0044)

~~~json
{
  "source": "00ab0044",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab004c`](#insn-00ab004c)

~~~json
{
  "source": "00ab004c",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0054`](#insn-00ab0054)

~~~json
{
  "source": "00ab0054",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab005c`](#insn-00ab005c)

~~~json
{
  "source": "00ab005c",
  "target": "00ab00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0060`](#insn-00ab0060)

~~~json
{
  "source": "00ab0060",
  "target": "00ab17f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0064`](#insn-00ab0064)

~~~json
{
  "source": "00ab0064",
  "target": "Stack[-0x210]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab006c`](#insn-00ab006c)

~~~json
{
  "source": "00ab006c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0074`](#insn-00ab0074)

~~~json
{
  "source": "00ab0074",
  "target": "00ab00d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0078`](#insn-00ab0078)

~~~json
{
  "source": "00ab0078",
  "target": "00440f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab00d0`](#insn-00ab00d0)

~~~json
{
  "source": "00ab00d0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
