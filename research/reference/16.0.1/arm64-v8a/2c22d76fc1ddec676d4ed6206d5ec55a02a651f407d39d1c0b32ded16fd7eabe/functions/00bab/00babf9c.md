# 00babf9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00babb74`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00babb74.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-09ebef1885c37002251a84fb83d17858)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bac038`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bac/00bac038.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-9767a3a77a5d1da00e55980500024fa9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babf9c",
  "name": "FUN_00babf9c",
  "size": 2484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28f58857bd6323b09f4d942f0d149d7edfc07b594b464b889f237d236720fdaa",
  "source_text_sha256": "28f58857bd6323b09f4d942f0d149d7edfc07b594b464b889f237d236720fdaa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babf9c",
        "00bac94f"
      ]
    ],
    "bytes_sha256": "498877a52635152d88cad1eef57cc7685b48789fc4355f688b7624ae287e8eb1",
    "instruction_count": 621,
    "instruction_bytes": 2484,
    "body_bytes": 2484,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b82b58](../00b82/00b82b58.md)
- [00b82cb8](../00b82/00b82cb8.md)
- [00babf9c](../00bab/00babf9c.md)

## 呼び出し先

- [00babf9c](../00bab/00babf9c.md)
- [00bac950](../00bac/00bac950.md)
- [00bacbfc](../00bac/00bacbfc.md)
- [00bace04](../00bac/00bace04.md)
- [00bad0e4](../00bad/00bad0e4.md)
- [00c58050](../00c58/00c58050.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 28559 bytes

~~~c

void FUN_00babf9c(undefined8 *param_1,undefined8 *param_2)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  undefined8 *puVar6;
  bool bVar7;
  int iVar8;
  int iVar9;
  ulong uVar10;
  long lVar11;
  byte *pbVar12;
  byte *pbVar13;
  byte *pbVar14;
  byte *pbVar15;
  undefined8 *puVar16;
  undefined8 *puVar17;
  undefined8 *puVar18;
  undefined8 *puVar19;
  byte *pbVar20;
  undefined8 *puVar21;
  ulong uVar22;
  long lVar23;
  long lVar24;
  
                    /* catch() { ... } // from try @ 00baa944 with catch @ 00babf9c */
                    /* catch() { ... } // from try @ 00baa7a8 with catch @ 00babfbc */
LAB_00babfc4:
  puVar16 = param_2 + -1;
  puVar18 = param_1;
LAB_00babfd8:
  param_1 = puVar18;
  lVar11 = (long)param_2 - (long)param_1;
                    /* catch() { ... } // from try @ 00ba9d68 with catch @ 00babfdc */
  uVar10 = lVar11 >> 3;
                    /* try { // try from 00bac678 to 00cac6af has its CatchHandler @ 00bac76c */
  switch(uVar10) {
  case 0:
  case 1:
    goto switchD_00bac684_caseD_0;
  case 2:
    pbVar15 = (byte *)param_2[-1];
    pbVar20 = (byte *)*param_1;
    bVar7 = *(ulong *)(pbVar20 + 0x80) <= *(ulong *)(pbVar15 + 0x80);
    if (*(ulong *)(pbVar15 + 0x80) == *(ulong *)(pbVar20 + 0x80)) {
      bVar4 = *pbVar20;
      bVar5 = *pbVar15;
                    /* try { // try from 00bac6b0 to 00cac76f has its CatchHandler @ 00bac4ec */
      uVar10 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar10 = *(ulong *)(pbVar20 + 8);
      }
      uVar22 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar22 = *(ulong *)(pbVar15 + 8);
      }
      sVar3 = uVar10;
      if (uVar22 <= uVar10) {
        sVar3 = uVar22;
      }
      if (sVar3 != 0) {
        pbVar12 = *(byte **)(pbVar15 + 0x10);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac64c with catch @ 00bac6d8
                        */
        pbVar13 = *(byte **)(pbVar20 + 0x10);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac62c with catch @ 00bac6dc
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac5fc with catch @ 00bac6e0
                        */
        if ((bVar5 & 1) == 0) {
          pbVar12 = pbVar15 + 1;
        }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac5d8 with catch @ 00bac6e4
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac5a8 with catch @ 00bac6e8
                        */
        if ((bVar4 & 1) == 0) {
          pbVar13 = pbVar20 + 1;
        }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac588 with catch @ 00bac6ec
                        */
        iVar8 = memcmp(pbVar12,pbVar13,sVar3);
        if (iVar8 != 0) {
          if (-1 < iVar8) {
            return;
          }
          goto LAB_00bac928;
        }
      }
      bVar7 = uVar10 <= uVar22;
    }
    if (bVar7) {
      return;
    }
LAB_00bac928:
    *param_1 = pbVar15;
    param_2[-1] = pbVar20;
    return;
  case 3:
                    /* try { // try from 00bac8b0 to 00cac8bb has its CatchHandler @ 00bac960 */
    FUN_00bac950(param_1,param_1 + 1,puVar16);
    return;
  case 4:
                    /* try { // try from 00bac8d0 to 00cac8db has its CatchHandler @ 00bac95c */
                    /* try { // try from 00bac8dc to 00cac8fb has its CatchHandler @ 00bac9ac */
    FUN_00bacbfc(param_1,param_1 + 1,param_1 + 2,puVar16);
    return;
  case 5:
                    /* try { // try from 00bac8fc to 00cac933 has its CatchHandler @ 00bac9f0 */
    FUN_00bace04(param_1,param_1 + 1,param_1 + 2,param_1 + 3,puVar16);
    return;
  default:
    if (0xf7 < lVar11) {
      uVar22 = uVar10;
                    /* catch() { ... } // from try @ 00baa930 with catch @ 00babffc */
      if ((long)uVar10 < 0) {
        uVar22 = uVar10 + 1;
      }
                    /* catch() { ... } // from try @ 00baa794 with catch @ 00bac000 */
                    /* catch() { ... } // from try @ 00baa538 with catch @ 00bac004 */
                    /* catch() { ... } // from try @ 00ba9d54 with catch @ 00bac008 */
                    /* catch() { ... } // from try @ 00baa90c with catch @ 00bac00c */
                    /* catch() { ... } // from try @ 00baa770 with catch @ 00bac010 */
      puVar18 = (undefined8 *)((long)param_1 + (uVar22 & 0x3ffffffffffffffe) * 4);
                    /* catch() { ... } // from try @ 00baa514 with catch @ 00bac014 */
      if (lVar11 < 0x1f39) {
        iVar8 = FUN_00bac950(param_1,puVar18,puVar16);
      }
      else {
                    /* catch() { ... } // from try @ 00ba9d30 with catch @ 00bac018 */
        uVar22 = uVar10 + 3;
        if (-1 < (long)uVar10) {
          uVar22 = uVar10;
        }
                    /* catch() { ... } // from try @ 00bab8ac with catch @ 00bac028 */
                    /* catch() { ... } // from try @ 00bab508 with catch @ 00bac02c */
        lVar11 = (uVar22 & 0x7ffffffffffffffc) * 2;
                    /* catch() { ... } // from try @ 00bab170 with catch @ 00bac030 */
                    /* catch() { ... } // from try @ 00baae64 with catch @ 00bac034 */
                    /* catch() { ... } // from try @ 00baa484 with catch @ 00bac038 */
                    /* catch() { ... } // from try @ 00baa16c with catch @ 00bac03c */
                    /* catch() { ... } // from try @ 00baa6dc with catch @ 00bac040 */
        iVar8 = FUN_00bace04(param_1,(long)param_1 + lVar11,puVar18,(long)puVar18 + lVar11,puVar16);
      }
      pbVar20 = (byte *)*param_1;
                    /* catch() { ... } // from try @ 00baaa30 with catch @ 00bac05c */
      pbVar15 = (byte *)*puVar18;
                    /* catch() { ... } // from try @ 00baa894 with catch @ 00bac060 */
                    /* catch() { ... } // from try @ 00ba9e50 with catch @ 00bac064 */
      uVar10 = *(ulong *)(pbVar20 + 0x80);
      uVar22 = *(ulong *)(pbVar15 + 0x80);
      puVar17 = puVar16;
      if (uVar10 == uVar22) {
        bVar4 = *pbVar15;
        bVar5 = *pbVar20;
                    /* catch() { ... } // from try @ 00baa54c with catch @ 00bac090
                       catch() { ... } // from try @ 00baa690 with catch @ 00bac090 */
        uVar2 = (ulong)(bVar4 >> 1);
        if ((bVar4 & 1) != 0) {
          uVar2 = *(ulong *)(pbVar15 + 8);
        }
        uVar1 = (ulong)(bVar5 >> 1);
        if ((bVar5 & 1) != 0) {
          uVar1 = *(ulong *)(pbVar20 + 8);
        }
        sVar3 = uVar2;
        if (uVar1 <= uVar2) {
          sVar3 = uVar1;
        }
        if (sVar3 != 0) {
                    /* catch() { ... } // from try @ 00ba9bc8 with catch @ 00bac0b0 */
          pbVar12 = *(byte **)(pbVar20 + 0x10);
                    /* catch() { ... } // from try @ 00ba9bf4 with catch @ 00bac0b4 */
          pbVar13 = *(byte **)(pbVar15 + 0x10);
          if ((bVar5 & 1) == 0) {
            pbVar12 = pbVar20 + 1;
          }
          if ((bVar4 & 1) == 0) {
            pbVar13 = pbVar15 + 1;
          }
          iVar9 = memcmp(pbVar12,pbVar13,sVar3);
                    /* catch() { ... } // from try @ 00baaa50 with catch @ 00bac0cc */
          if (iVar9 != 0) {
                    /* catch() { ... } // from try @ 00baa8b4 with catch @ 00bac0d0 */
            if (-1 < iVar9) goto LAB_00bac0ec;
            goto LAB_00bac19c;
          }
        }
                    /* catch() { ... } // from try @ 00ba95f8 with catch @ 00bac0e4 */
        if (uVar2 <= uVar1) goto LAB_00bac0ec;
      }
      else {
                    /* catch() { ... } // from try @ 00baa6fc with catch @ 00bac0d8 */
        if (uVar22 <= uVar10) {
LAB_00bac0ec:
          if (param_1 != param_2 + -2) {
            puVar17 = param_2 + -2;
            do {
              pbVar12 = (byte *)*puVar17;
              bVar7 = uVar22 <= *(ulong *)(pbVar12 + 0x80);
              if (*(ulong *)(pbVar12 + 0x80) == uVar22) {
                bVar4 = *pbVar15;
                bVar5 = *pbVar12;
                    /* catch() { ... } // from try @ 00ba959c with catch @ 00bac13c */
                    /* catch() { ... } // from try @ 00ba9be8 with catch @ 00bac144 */
                uVar2 = (ulong)(bVar4 >> 1);
                if ((bVar4 & 1) != 0) {
                  uVar2 = *(ulong *)(pbVar15 + 8);
                }
                uVar1 = (ulong)(bVar5 >> 1);
                if ((bVar5 & 1) != 0) {
                  uVar1 = *(ulong *)(pbVar12 + 8);
                }
                    /* catch() { ... } // from try @ 00ba963c with catch @ 00bac158
                       catch() { ... } // from try @ 00ba9a34 with catch @ 00bac158 */
                sVar3 = uVar2;
                    /* catch() { ... } // from try @ 00ba9b30 with catch @ 00bac15c */
                if (uVar1 <= uVar2) {
                  sVar3 = uVar1;
                }
                    /* catch() { ... } // from try @ 00ba9b80 with catch @ 00bac160 */
                if (sVar3 == 0) {
LAB_00bac108:
                  bVar7 = uVar2 <= uVar1;
                  goto LAB_00bac110;
                }
                    /* catch() { ... } // from try @ 00ba9854 with catch @ 00bac164 */
                pbVar13 = *(byte **)(pbVar12 + 0x10);
                if ((bVar5 & 1) == 0) {
                  pbVar13 = pbVar12 + 1;
                }
                    /* catch() { ... } // from try @ 00ba982c with catch @ 00bac174 */
                pbVar14 = pbVar15 + 1;
                    /* catch() { ... } // from try @ 00ba976c with catch @ 00bac178 */
                if ((bVar4 & 1) != 0) {
                  pbVar14 = *(byte **)(pbVar15 + 0x10);
                }
                iVar9 = memcmp(pbVar13,pbVar14,sVar3);
                if (iVar9 == 0) goto LAB_00bac108;
                if (iVar9 < 0) goto LAB_00bac18c;
              }
              else {
LAB_00bac110:
                if (!bVar7) {
LAB_00bac18c:
                  *param_1 = pbVar12;
                  *puVar17 = pbVar20;
                    /* catch() { ... } // from try @ 00ba98cc with catch @ 00bac198 */
                  iVar8 = iVar8 + 1;
                  goto LAB_00bac19c;
                }
              }
              puVar17 = puVar17 + -1;
                    /* catch() { ... } // from try @ 00ba95ec with catch @ 00bac118 */
            } while (param_1 != puVar17);
          }
          pbVar15 = (byte *)*puVar16;
          puVar17 = param_1 + 1;
          if (uVar10 == *(ulong *)(pbVar15 + 0x80)) {
                    /* try { // try from 00bac304 to 00cac30f has its CatchHandler @ 00bac468 */
            bVar4 = *pbVar15;
            bVar5 = *pbVar20;
            uVar22 = (ulong)(bVar4 >> 1);
            if ((bVar4 & 1) != 0) {
              uVar22 = *(ulong *)(pbVar15 + 8);
            }
                    /* try { // try from 00bac324 to 00cac32f has its CatchHandler @ 00bac464 */
            uVar2 = (ulong)(bVar5 >> 1);
            if ((bVar5 & 1) != 0) {
              uVar2 = *(ulong *)(pbVar20 + 8);
            }
            sVar3 = uVar22;
            if (uVar2 <= uVar22) {
              sVar3 = uVar2;
            }
            if (sVar3 != 0) {
              pbVar12 = *(byte **)(pbVar20 + 0x10);
              pbVar13 = *(byte **)(pbVar15 + 0x10);
              if ((bVar5 & 1) == 0) {
                pbVar12 = pbVar20 + 1;
              }
              if ((bVar4 & 1) == 0) {
                pbVar13 = pbVar15 + 1;
              }
                    /* try { // try from 00bac354 to 00cac35f has its CatchHandler @ 00bac460 */
              iVar8 = memcmp(pbVar12,pbVar13,sVar3);
              if (iVar8 != 0) {
                if (-1 < iVar8) goto LAB_00bac480;
                goto LAB_00bac520;
              }
            }
            if (uVar22 <= uVar2) {
LAB_00bac480:
              if (puVar17 == puVar16) {
                return;
              }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac2d4 with catch @ 00bac490
                        */
              puVar17 = param_1 + 2;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac2b0 with catch @ 00bac494
                        */
              do {
                pbVar12 = (byte *)puVar17[-1];
                bVar7 = *(ulong *)(pbVar12 + 0x80) <= uVar10;
                if (uVar10 == *(ulong *)(pbVar12 + 0x80)) {
                  bVar4 = *pbVar12;
                  bVar5 = *pbVar20;
                  uVar22 = (ulong)(bVar4 >> 1);
                  if ((bVar4 & 1) != 0) {
                    uVar22 = *(ulong *)(pbVar12 + 8);
                  }
                  uVar2 = (ulong)(bVar5 >> 1);
                  if ((bVar5 & 1) != 0) {
                    uVar2 = *(ulong *)(pbVar20 + 8);
                  }
                  sVar3 = uVar22;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac3f4 with catch @ 00bac4e8
                        */
                  if (uVar2 <= uVar22) {
                    sVar3 = uVar2;
                  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac6b0 with catch @ 00bac4ec
                        */
                  if (sVar3 == 0) {
LAB_00bac498:
                    bVar7 = uVar22 <= uVar2;
                    goto LAB_00bac49c;
                  }
                  pbVar14 = *(byte **)(pbVar12 + 0x10);
                  pbVar13 = pbVar20 + 1;
                  if ((bVar5 & 1) != 0) {
                    pbVar13 = *(byte **)(pbVar20 + 0x10);
                  }
                  if ((bVar4 & 1) == 0) {
                    pbVar14 = pbVar12 + 1;
                  }
                  iVar8 = memcmp(pbVar13,pbVar14,sVar3);
                  if (iVar8 == 0) goto LAB_00bac498;
                  if (iVar8 < 0) goto LAB_00bac514;
                }
                else {
LAB_00bac49c:
                  if (!bVar7) goto LAB_00bac514;
                }
                puVar17 = puVar17 + 1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac3d4 with catch @ 00bac4a4
                        */
                if (param_2 == puVar17) {
                  return;
                }
              } while( true );
            }
          }
          else {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac354 with catch @ 00bac460
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac324 with catch @ 00bac464
                        */
            if (*(ulong *)(pbVar15 + 0x80) <= uVar10) goto LAB_00bac480;
          }
          goto LAB_00bac520;
        }
      }
LAB_00bac19c:
      puVar19 = param_1 + 1;
      puVar6 = puVar18;
      if (puVar19 < puVar17) {
LAB_00bac1b0:
        puVar18 = puVar6;
                    /* catch() { ... } // from try @ 00ba9a3c with catch @ 00bac1b0 */
        pbVar15 = (byte *)*puVar18;
                    /* catch() { ... } // from try @ 00ba985c with catch @ 00bac1b4 */
        uVar10 = *(ulong *)(pbVar15 + 0x80);
        puVar21 = puVar19;
        do {
          pbVar20 = (byte *)*puVar21;
          if (*(ulong *)(pbVar20 + 0x80) == uVar10) {
                    /* catch() { ... } // from try @ 00ba96b4 with catch @ 00bac1dc */
            bVar4 = *pbVar15;
                    /* catch() { ... } // from try @ 00ba9684 with catch @ 00bac1e4 */
            bVar5 = *pbVar20;
                    /* catch() { ... } // from try @ 00ba9690 with catch @ 00bac1e8 */
                    /* catch() { ... } // from try @ 00ba96a0 with catch @ 00bac1ec */
                    /* catch() { ... } // from try @ 00ba9678 with catch @ 00bac1f0 */
            uVar22 = (ulong)(bVar4 >> 1);
                    /* catch() { ... } // from try @ 00bab950 with catch @ 00bac1f8 */
            if ((bVar4 & 1) != 0) {
              uVar22 = *(ulong *)(pbVar15 + 8);
            }
            uVar2 = (ulong)(bVar5 >> 1);
            if ((bVar5 & 1) != 0) {
              uVar2 = *(ulong *)(pbVar20 + 8);
            }
            sVar3 = uVar22;
            if (uVar2 <= uVar22) {
              sVar3 = uVar2;
            }
            if (sVar3 != 0) {
              pbVar12 = *(byte **)(pbVar20 + 0x10);
              if ((bVar5 & 1) == 0) {
                pbVar12 = pbVar20 + 1;
              }
              pbVar13 = pbVar15 + 1;
              if ((bVar4 & 1) != 0) {
                pbVar13 = *(byte **)(pbVar15 + 0x10);
              }
              iVar9 = memcmp(pbVar12,pbVar13,sVar3);
              if (iVar9 != 0) {
                if (iVar9 < 0) goto LAB_00bac1c8;
                goto LAB_00bac248;
              }
            }
            if (uVar22 <= uVar2) goto LAB_00bac248;
          }
          else if (uVar10 <= *(ulong *)(pbVar20 + 0x80)) goto LAB_00bac248;
LAB_00bac1c8:
          puVar21 = puVar21 + 1;
        } while( true );
      }
      if (puVar19 != puVar18) goto LAB_00bac38c;
      goto LAB_00bac410;
    }
    FUN_00bac950(param_1,param_1 + 1,param_1 + 2);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac558 with catch @ 00bac714
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac534 with catch @ 00bac718
                        */
    if (param_1 + 3 == param_2) {
      return;
    }
    lVar11 = 0;
    puVar18 = param_1 + 3;
    puVar16 = param_1 + 2;
  }
LAB_00bac740:
  puVar17 = puVar18;
  pbVar20 = (byte *)*puVar17;
  pbVar15 = (byte *)*puVar16;
  uVar10 = *(ulong *)(pbVar20 + 0x80);
  if (uVar10 == *(ulong *)(pbVar15 + 0x80)) {
    bVar4 = *pbVar15;
    bVar5 = *pbVar20;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac678 with catch @ 00bac76c
                        */
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac934 with catch @ 00bac770
                        */
    uVar22 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar22 = *(ulong *)(pbVar15 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar20 + 8);
    }
    sVar3 = uVar22;
    if (uVar2 <= uVar22) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar12 = *(byte **)(pbVar20 + 0x10);
      pbVar13 = *(byte **)(pbVar15 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar12 = pbVar20 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar13 = pbVar15 + 1;
      }
      iVar8 = memcmp(pbVar12,pbVar13,sVar3);
      if (iVar8 != 0) {
        if (iVar8 < 0) goto LAB_00bac7cc;
        goto LAB_00bac730;
      }
    }
    if (uVar2 < uVar22) {
LAB_00bac7cc:
      *puVar17 = pbVar15;
      puVar18 = puVar16;
      if (puVar16 != param_1) {
        lVar24 = lVar11;
                    /* try { // try from 00bac7dc to 00cac7e7 has its CatchHandler @ 00bac998 */
        do {
          pbVar15 = *(byte **)((long)param_1 + lVar24 + 8);
                    /* try { // try from 00bac80c to 00cac817 has its CatchHandler @ 00bac970 */
          puVar18 = puVar16;
          if (uVar10 == *(ulong *)(pbVar15 + 0x80)) {
            bVar4 = *pbVar15;
            bVar5 = *pbVar20;
                    /* try { // try from 00bac82c to 00cac837 has its CatchHandler @ 00bac96c */
            uVar22 = (ulong)(bVar4 >> 1);
            if ((bVar4 & 1) != 0) {
              uVar22 = *(ulong *)(pbVar15 + 8);
            }
            uVar2 = (ulong)(bVar5 >> 1);
            if ((bVar5 & 1) != 0) {
              uVar2 = *(ulong *)(pbVar20 + 8);
            }
            sVar3 = uVar22;
            if (uVar2 <= uVar22) {
              sVar3 = uVar2;
            }
            if (sVar3 != 0) {
              pbVar13 = *(byte **)(pbVar15 + 0x10);
              pbVar12 = pbVar20 + 1;
              if ((bVar5 & 1) != 0) {
                pbVar12 = *(byte **)(pbVar20 + 0x10);
              }
                    /* try { // try from 00bac85c to 00cac867 has its CatchHandler @ 00bac968 */
              if ((bVar4 & 1) == 0) {
                pbVar13 = pbVar15 + 1;
              }
              iVar8 = memcmp(pbVar12,pbVar13,sVar3);
              if (iVar8 != 0) {
                if (iVar8 < 0) goto LAB_00bac7ec;
                break;
              }
            }
                    /* try { // try from 00bac880 to 00cac88b has its CatchHandler @ 00bac964 */
            if (uVar22 <= uVar2) {
              puVar18 = (undefined8 *)((long)param_1 + lVar24 + 0x10);
              break;
            }
          }
          else if (*(ulong *)(pbVar15 + 0x80) <= uVar10) break;
LAB_00bac7ec:
          lVar23 = lVar24 + -8;
          puVar16 = puVar16 + -1;
          *(byte **)((long)param_1 + lVar24 + 0x10) = pbVar15;
          puVar18 = param_1;
          lVar24 = lVar23;
        } while (lVar23 != -0x10);
      }
      *puVar18 = pbVar20;
    }
  }
  else if (uVar10 < *(ulong *)(pbVar15 + 0x80)) goto LAB_00bac7cc;
LAB_00bac730:
  lVar11 = lVar11 + 8;
  puVar18 = puVar17 + 1;
  puVar16 = puVar17;
  if (puVar17 + 1 == param_2) {
switchD_00bac684_caseD_0:
                    /* try { // try from 00bac934 to 00cac9f3 has its CatchHandler @ 00bac770 */
    return;
  }
  goto LAB_00bac740;
  while (uVar10 <= *(ulong *)(pbVar12 + 0x80)) {
LAB_00bac248:
    puVar17 = puVar17 + -1;
    pbVar12 = (byte *)*puVar17;
    if (*(ulong *)(pbVar12 + 0x80) == uVar10) {
      bVar4 = *pbVar15;
      bVar5 = *pbVar12;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac42c with catch @ 00bac268
                        */
      uVar22 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar22 = *(ulong *)(pbVar15 + 8);
      }
      uVar2 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar2 = *(ulong *)(pbVar12 + 8);
      }
      sVar3 = uVar22;
      if (uVar2 <= uVar22) {
        sVar3 = uVar2;
      }
      if (sVar3 != 0) {
        pbVar13 = *(byte **)(pbVar12 + 0x10);
        if ((bVar5 & 1) == 0) {
          pbVar13 = pbVar12 + 1;
        }
        pbVar14 = pbVar15 + 1;
        if ((bVar4 & 1) != 0) {
          pbVar14 = *(byte **)(pbVar15 + 0x10);
        }
        iVar9 = memcmp(pbVar13,pbVar14,sVar3);
        if (iVar9 != 0) {
          if (iVar9 < 0) break;
          goto LAB_00bac248;
        }
      }
      if (uVar2 < uVar22) break;
      goto LAB_00bac248;
    }
  }
  if (puVar21 <= puVar17) {
    puVar19 = puVar21 + 1;
    *puVar21 = pbVar12;
                    /* try { // try from 00bac2d4 to 00cac2df has its CatchHandler @ 00bac490 */
    iVar8 = iVar8 + 1;
    *puVar17 = pbVar20;
    puVar6 = puVar17;
    if (puVar18 != puVar21) {
      puVar6 = puVar18;
    }
    goto LAB_00bac1b0;
  }
                    /* try { // try from 00bac378 to 00cac383 has its CatchHandler @ 00bac45c */
  puVar19 = puVar21;
  if (puVar21 == puVar18) goto LAB_00bac410;
LAB_00bac38c:
  pbVar15 = (byte *)*puVar18;
  pbVar20 = (byte *)*puVar19;
  if (*(ulong *)(pbVar15 + 0x80) == *(ulong *)(pbVar20 + 0x80)) {
    bVar4 = *pbVar20;
                    /* try { // try from 00bac3a8 to 00cac3b3 has its CatchHandler @ 00bac458 */
    bVar5 = *pbVar15;
    uVar10 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar10 = *(ulong *)(pbVar20 + 8);
    }
    uVar22 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00bac3c8 to 00cac3d3 has its CatchHandler @ 00bac454 */
    if ((bVar5 & 1) != 0) {
      uVar22 = *(ulong *)(pbVar15 + 8);
    }
    sVar3 = uVar10;
    if (uVar22 <= uVar10) {
      sVar3 = uVar22;
    }
                    /* try { // try from 00bac3d4 to 00cac3f3 has its CatchHandler @ 00bac4a4 */
    if (sVar3 != 0) {
      pbVar12 = *(byte **)(pbVar15 + 0x10);
      pbVar13 = *(byte **)(pbVar20 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar12 = pbVar15 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar13 = pbVar20 + 1;
      }
      iVar9 = memcmp(pbVar12,pbVar13,sVar3);
                    /* try { // try from 00bac3f4 to 00cac42b has its CatchHandler @ 00bac4e8 */
      if (iVar9 != 0) {
        if (-1 < iVar9) goto LAB_00bac410;
        goto LAB_00bac404;
      }
    }
    if (uVar10 <= uVar22) goto LAB_00bac410;
  }
  else if (*(ulong *)(pbVar20 + 0x80) <= *(ulong *)(pbVar15 + 0x80)) goto LAB_00bac410;
LAB_00bac404:
  iVar8 = iVar8 + 1;
  *puVar19 = pbVar15;
  *puVar18 = pbVar20;
LAB_00bac410:
  if (iVar8 == 0) {
    uVar10 = FUN_00bad0e4(param_1,puVar19);
                    /* try { // try from 00bac42c to 00cac4eb has its CatchHandler @ 00bac268 */
    uVar22 = FUN_00bad0e4(puVar19 + 1,param_2);
    if ((uVar22 & 1) != 0) goto LAB_00bac664;
    puVar18 = puVar19 + 1;
    if ((uVar10 & 1) != 0) goto LAB_00babfd8;
  }
  if ((long)param_2 - (long)puVar19 <= (long)puVar19 - (long)param_1) {
                    /* try { // try from 00bac658 to 00cac677 has its CatchHandler @ 00bac728 */
    FUN_00babf9c(puVar19 + 1,param_2);
    param_2 = puVar19;
    goto LAB_00babfc4;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac3c8 with catch @ 00bac454
                        */
  FUN_00babf9c(param_1,puVar19);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac3a8 with catch @ 00bac458
                        */
  puVar18 = puVar19 + 1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac378 with catch @ 00bac45c
                        */
  goto LAB_00babfd8;
LAB_00bac664:
  param_2 = puVar19;
  if ((uVar10 & 1) != 0) {
    return;
  }
  goto LAB_00babfc4;
LAB_00bac514:
  puVar17[-1] = pbVar15;
  *puVar16 = pbVar12;
LAB_00bac520:
  puVar19 = puVar16;
  if (puVar17 == puVar16) {
    return;
  }
LAB_00bac530:
  pbVar15 = (byte *)*param_1;
                    /* try { // try from 00bac534 to 00cac53f has its CatchHandler @ 00bac718 */
  uVar10 = *(ulong *)(pbVar15 + 0x80);
  puVar18 = puVar17;
  do {
    pbVar20 = (byte *)*puVar18;
    if (uVar10 == *(ulong *)(pbVar20 + 0x80)) {
                    /* try { // try from 00bac558 to 00cac563 has its CatchHandler @ 00bac714 */
      bVar4 = *pbVar20;
      bVar5 = *pbVar15;
      uVar22 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar22 = *(ulong *)(pbVar20 + 8);
      }
      uVar2 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar2 = *(ulong *)(pbVar15 + 8);
      }
      sVar3 = uVar22;
      if (uVar2 <= uVar22) {
        sVar3 = uVar2;
      }
                    /* try { // try from 00bac588 to 00cac593 has its CatchHandler @ 00bac6ec */
      if (sVar3 != 0) {
        pbVar13 = *(byte **)(pbVar20 + 0x10);
        pbVar12 = pbVar15 + 1;
        if ((bVar5 & 1) != 0) {
          pbVar12 = *(byte **)(pbVar15 + 0x10);
        }
        if ((bVar4 & 1) == 0) {
          pbVar13 = pbVar20 + 1;
        }
        iVar8 = memcmp(pbVar12,pbVar13,sVar3);
                    /* try { // try from 00bac5a8 to 00cac5b3 has its CatchHandler @ 00bac6e8 */
        if (iVar8 != 0) {
          if (-1 < iVar8) goto LAB_00bac544;
          break;
        }
      }
      if (uVar2 < uVar22) break;
    }
    else if (uVar10 < *(ulong *)(pbVar20 + 0x80)) break;
LAB_00bac544:
    puVar18 = puVar18 + 1;
  } while( true );
  while (uVar10 < *(ulong *)(pbVar12 + 0x80)) {
LAB_00bac5c4:
    puVar19 = puVar19 + -1;
    pbVar12 = (byte *)*puVar19;
    if (uVar10 == *(ulong *)(pbVar12 + 0x80)) {
      bVar4 = *pbVar12;
                    /* try { // try from 00bac5d8 to 00cac5e3 has its CatchHandler @ 00bac6e4 */
      bVar5 = *pbVar15;
      uVar22 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar22 = *(ulong *)(pbVar12 + 8);
      }
      uVar2 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar2 = *(ulong *)(pbVar15 + 8);
      }
                    /* try { // try from 00bac5fc to 00cac607 has its CatchHandler @ 00bac6e0 */
      sVar3 = uVar22;
      if (uVar2 <= uVar22) {
        sVar3 = uVar2;
      }
      if (sVar3 != 0) {
        pbVar14 = *(byte **)(pbVar12 + 0x10);
        pbVar13 = pbVar15 + 1;
        if ((bVar5 & 1) != 0) {
          pbVar13 = *(byte **)(pbVar15 + 0x10);
        }
        if ((bVar4 & 1) == 0) {
          pbVar14 = pbVar12 + 1;
        }
        iVar8 = memcmp(pbVar13,pbVar14,sVar3);
        if (iVar8 != 0) {
          if (-1 < iVar8) break;
          goto LAB_00bac5c4;
        }
      }
      if (uVar22 <= uVar2) break;
      goto LAB_00bac5c4;
    }
  }
  if (puVar19 <= puVar18) goto LAB_00babfd8;
  puVar17 = puVar18 + 1;
  *puVar18 = pbVar12;
  *puVar19 = pbVar20;
                    /* try { // try from 00bac64c to 00cac657 has its CatchHandler @ 00bac6d8 */
  goto LAB_00bac530;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babf9c"></a> `00babf9c` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00babfa0"></a> `00babfa0` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babfa4"></a> `00babfa4` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babfa8"></a> `00babfa8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babfac"></a> `00babfac` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00babfb0"></a> `00babfb0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00babfb4"></a> `00babfb4` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00babfb8"></a> `00babfb8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00babfbc"></a> `00babfbc` | `fc 03 01 aa` | mov x28,x1 | `FALL_THROUGH`
<a id="insn-00babfc0"></a> `00babfc0` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00babfc4"></a> `00babfc4` | `88 23 00 d1` | sub x8,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00babfc8"></a> `00babfc8` | `fc 23 01 a9` | stp x28,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babfcc"></a> `00babfcc` | `88 43 00 d1` | sub x8,x28,#0x10 | `FALL_THROUGH`
<a id="insn-00babfd0"></a> `00babfd0` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00babfd4"></a> `00babfd4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babfd8"></a> `00babfd8` | `89 03 16 cb` | sub x9,x28,x22 | `FALL_THROUGH`
<a id="insn-00babfdc"></a> `00babfdc` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00babfe0"></a> `00babfe0` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00babfe4"></a> `00babfe4` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00babfe8"></a> `00babfe8` | `49 34 00 54` | b.ls 0x00bac670 | `CONDITIONAL_JUMP`
<a id="insn-00babfec"></a> `00babfec` | `3f dd 03 f1` | cmp x9,#0xf7 | `FALL_THROUGH`
<a id="insn-00babff0"></a> `00babff0` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babff4"></a> `00babff4` | `4d 38 00 54` | b.le 0x00bac6fc | `CONDITIONAL_JUMP`
<a id="insn-00babff8"></a> `00babff8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00babffc"></a> `00babffc` | `0a a5 88 9a` | cinc x10,x8,lt | `FALL_THROUGH`
<a id="insn-00bac000"></a> `00bac000` | `4a f5 7e d3` | lsl x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bac004"></a> `00bac004` | `4a f1 7d 92` | and x10,x10,#-0x8 | `FALL_THROUGH`
<a id="insn-00bac008"></a> `00bac008` | `2b e7 83 52` | mov w11,#0x1f39 | `FALL_THROUGH`
<a id="insn-00bac00c"></a> `00bac00c` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bac010"></a> `00bac010` | `73 03 0a 8b` | add x19,x27,x10 | `FALL_THROUGH`
<a id="insn-00bac014"></a> `00bac014` | `ab 01 00 54` | b.lt 0x00bac048 | `CONDITIONAL_JUMP`
<a id="insn-00bac018"></a> `00bac018` | `09 0d 00 91` | add x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bac01c"></a> `00bac01c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bac020"></a> `00bac020` | `28 b1 88 9a` | csel x8,x9,x8,lt | `FALL_THROUGH`
<a id="insn-00bac024"></a> `00bac024` | `e4 0f 40 f9` | ldr x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac028"></a> `00bac028` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac02c"></a> `00bac02c` | `08 f1 7d 92` | and x8,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00bac030"></a> `00bac030` | `61 03 08 8b` | add x1,x27,x8 | `FALL_THROUGH`
<a id="insn-00bac034"></a> `00bac034` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bac038"></a> `00bac038` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac03c"></a> `00bac03c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bac040"></a> `00bac040` | `71 03 00 94` | bl 0x00bace04 | `UNCONDITIONAL_CALL`
<a id="insn-00bac044"></a> `00bac044` | `05 00 00 14` | b 0x00bac058 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac048"></a> `00bac048` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac04c"></a> `00bac04c` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac050"></a> `00bac050` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bac054"></a> `00bac054` | `3f 02 00 94` | bl 0x00bac950 | `UNCONDITIONAL_CALL`
<a id="insn-00bac058"></a> `00bac058` | `78 03 40 f9` | ldr x24,[x27] | `FALL_THROUGH`
<a id="insn-00bac05c"></a> `00bac05c` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bac060"></a> `00bac060` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00bac064"></a> `00bac064` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00bac068"></a> `00bac068` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bac06c"></a> `00bac06c` | `b9 42 40 f9` | ldr x25,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bac070"></a> `00bac070` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bac074"></a> `00bac074` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bac078"></a> `00bac078` | `01 03 00 54` | b.ne 0x00bac0d8 | `CONDITIONAL_JUMP`
<a id="insn-00bac07c"></a> `00bac07c` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bac080"></a> `00bac080` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac084"></a> `00bac084` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bac088"></a> `00bac088` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bac08c"></a> `00bac08c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac090"></a> `00bac090` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac094"></a> `00bac094` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac098"></a> `00bac098` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac09c"></a> `00bac09c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0a0"></a> `00bac0a0` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac0a4"></a> `00bac0a4` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bac0a8"></a> `00bac0a8` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bac0ac"></a> `00bac0ac` | `c2 01 00 b4` | cbz x2,0x00bac0e4 | `CONDITIONAL_JUMP`
<a id="insn-00bac0b0"></a> `00bac0b0` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bac0b4"></a> `00bac0b4` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac0b8"></a> `00bac0b8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0bc"></a> `00bac0bc` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bac0c0"></a> `00bac0c0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0c4"></a> `00bac0c4` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bac0c8"></a> `00bac0c8` | `e2 af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac0cc"></a> `00bac0cc` | `c0 00 00 34` | cbz w0,0x00bac0e4 | `CONDITIONAL_JUMP`
<a id="insn-00bac0d0"></a> `00bac0d0` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bac0dc | `CONDITIONAL_JUMP`
<a id="insn-00bac0d4"></a> `00bac0d4` | `06 00 00 14` | b 0x00bac0ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bac0d8"></a> `00bac0d8` | `a2 00 00 54` | b.cs 0x00bac0ec | `CONDITIONAL_JUMP`
<a id="insn-00bac0dc"></a> `00bac0dc` | `fc 0f 40 f9` | ldr x28,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac0e0"></a> `00bac0e0` | `2f 00 00 14` | b 0x00bac19c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac0e4"></a> `00bac0e4` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bac0e8"></a> `00bac0e8` | `a3 ff ff 54` | b.cc 0x00bac0dc | `CONDITIONAL_JUMP`
<a id="insn-00bac0ec"></a> `00bac0ec` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bac0f0"></a> `00bac0f0` | `fa 2b 00 b9` | str w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac0f4"></a> `00bac0f4` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bac0f8"></a> `00bac0f8` | `80 0f 00 54` | b.eq 0x00bac2e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac0fc"></a> `00bac0fc` | `fc 07 40 f9` | ldr x28,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bac100"></a> `00bac100` | `ba 06 00 91` | add x26,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bac104"></a> `00bac104` | `07 00 00 14` | b 0x00bac120 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac108"></a> `00bac108` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bac10c"></a> `00bac10c` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac110"></a> `00bac110` | `e3 03 00 54` | b.cc 0x00bac18c | `CONDITIONAL_JUMP`
<a id="insn-00bac114"></a> `00bac114` | `9c 23 00 d1` | sub x28,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00bac118"></a> `00bac118` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00bac11c"></a> `00bac11c` | `60 0e 00 54` | b.eq 0x00bac2e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac120"></a> `00bac120` | `93 03 40 f9` | ldr x19,[x28] | `FALL_THROUGH`
<a id="insn-00bac124"></a> `00bac124` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac128"></a> `00bac128` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bac12c"></a> `00bac12c` | `21 ff ff 54` | b.ne 0x00bac110 | `CONDITIONAL_JUMP`
<a id="insn-00bac130"></a> `00bac130` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bac134"></a> `00bac134` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac138"></a> `00bac138` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bac13c"></a> `00bac13c` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac140"></a> `00bac140` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac144"></a> `00bac144` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac148"></a> `00bac148` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac14c"></a> `00bac14c` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac150"></a> `00bac150` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac154"></a> `00bac154` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac158"></a> `00bac158` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bac15c"></a> `00bac15c` | `62 33 94 9a` | csel x2,x27,x20,cc | `FALL_THROUGH`
<a id="insn-00bac160"></a> `00bac160` | `42 fd ff b4` | cbz x2,0x00bac108 | `CONDITIONAL_JUMP`
<a id="insn-00bac164"></a> `00bac164` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac168"></a> `00bac168` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac16c"></a> `00bac16c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac170"></a> `00bac170` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bac174"></a> `00bac174` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac178"></a> `00bac178` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bac17c"></a> `00bac17c` | `b5 af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac180"></a> `00bac180` | `40 fc ff 34` | cbz w0,0x00bac108 | `CONDITIONAL_JUMP`
<a id="insn-00bac184"></a> `00bac184` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac188"></a> `00bac188` | `60 fc ff 36` | tbz w0,#0x1f,0x00bac114 | `CONDITIONAL_JUMP`
<a id="insn-00bac18c"></a> `00bac18c` | `fa 2b 40 b9` | ldr w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac190"></a> `00bac190` | `73 03 00 f9` | str x19,[x27] | `FALL_THROUGH`
<a id="insn-00bac194"></a> `00bac194` | `98 03 00 f9` | str x24,[x28] | `FALL_THROUGH`
<a id="insn-00bac198"></a> `00bac198` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00bac19c"></a> `00bac19c` | `78 23 00 91` | add x24,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac1a0"></a> `00bac1a0` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00bac1a4"></a> `00bac1a4` | `1f 03 1c eb` | cmp x24,x28 | `FALL_THROUGH`
<a id="insn-00bac1a8"></a> `00bac1a8` | `e2 0d 00 54` | b.cs 0x00bac364 | `CONDITIONAL_JUMP`
<a id="insn-00bac1ac"></a> `00bac1ac` | `fa 2b 00 b9` | str w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac1b0"></a> `00bac1b0` | `3b 03 40 f9` | ldr x27,[x25] | `FALL_THROUGH`
<a id="insn-00bac1b4"></a> `00bac1b4` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00bac1b8"></a> `00bac1b8` | `79 43 40 f9` | ldr x25,[x27, #0x80] | `FALL_THROUGH`
<a id="insn-00bac1bc"></a> `00bac1bc` | `7a 07 00 91` | add x26,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1c0"></a> `00bac1c0` | `03 00 00 14` | b 0x00bac1cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac1c4"></a> `00bac1c4` | `22 04 00 54` | b.cs 0x00bac248 | `CONDITIONAL_JUMP`
<a id="insn-00bac1c8"></a> `00bac1c8` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bac1cc"></a> `00bac1cc` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00bac1d0"></a> `00bac1d0` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bac1d4"></a> `00bac1d4` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bac1d8"></a> `00bac1d8` | `61 ff ff 54` | b.ne 0x00bac1c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac1dc"></a> `00bac1dc` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00bac1e0"></a> `00bac1e0` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bac1e4"></a> `00bac1e4` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac1e8"></a> `00bac1e8` | `ab 06 40 f9` | ldr x11,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac1ec"></a> `00bac1ec` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1f0"></a> `00bac1f0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1f4"></a> `00bac1f4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1f8"></a> `00bac1f8` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac1fc"></a> `00bac1fc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac200"></a> `00bac200` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac204"></a> `00bac204` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bac208"></a> `00bac208` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bac20c"></a> `00bac20c` | `62 01 00 b4` | cbz x2,0x00bac238 | `CONDITIONAL_JUMP`
<a id="insn-00bac210"></a> `00bac210` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac214"></a> `00bac214` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bac218"></a> `00bac218` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac21c"></a> `00bac21c` | `40 15 95 9a` | csinc x0,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00bac220"></a> `00bac220` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac224"></a> `00bac224` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bac228"></a> `00bac228` | `8a af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac22c"></a> `00bac22c` | `60 00 00 34` | cbz w0,0x00bac238 | `CONDITIONAL_JUMP`
<a id="insn-00bac230"></a> `00bac230` | `c0 fc ff 37` | tbnz w0,#0x1f,0x00bac1c8 | `CONDITIONAL_JUMP`
<a id="insn-00bac234"></a> `00bac234` | `05 00 00 14` | b 0x00bac248 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac238"></a> `00bac238` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bac23c"></a> `00bac23c` | `63 fc ff 54` | b.cc 0x00bac1c8 | `CONDITIONAL_JUMP`
<a id="insn-00bac240"></a> `00bac240` | `02 00 00 14` | b 0x00bac248 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac244"></a> `00bac244` | `c3 03 00 54` | b.cc 0x00bac2bc | `CONDITIONAL_JUMP`
<a id="insn-00bac248"></a> `00bac248` | `93 8f 5f f8` | ldr x19,[x28, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bac24c"></a> `00bac24c` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac250"></a> `00bac250` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bac254"></a> `00bac254` | `81 ff ff 54` | b.ne 0x00bac244 | `CONDITIONAL_JUMP`
<a id="insn-00bac258"></a> `00bac258` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00bac25c"></a> `00bac25c` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bac260"></a> `00bac260` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bac264"></a> `00bac264` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac268"></a> `00bac268` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac26c"></a> `00bac26c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac270"></a> `00bac270` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac274"></a> `00bac274` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac278"></a> `00bac278` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac27c"></a> `00bac27c` | `b7 01 8b 9a` | csel x23,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac280"></a> `00bac280` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00bac284"></a> `00bac284` | `82 32 97 9a` | csel x2,x20,x23,cc | `FALL_THROUGH`
<a id="insn-00bac288"></a> `00bac288` | `62 01 00 b4` | cbz x2,0x00bac2b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac28c"></a> `00bac28c` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac290"></a> `00bac290` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bac294"></a> `00bac294` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac298"></a> `00bac298` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bac29c"></a> `00bac29c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac2a0"></a> `00bac2a0` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bac2a4"></a> `00bac2a4` | `6b af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac2a8"></a> `00bac2a8` | `60 00 00 34` | cbz w0,0x00bac2b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac2ac"></a> `00bac2ac` | `e0 fc ff 36` | tbz w0,#0x1f,0x00bac248 | `CONDITIONAL_JUMP`
<a id="insn-00bac2b0"></a> `00bac2b0` | `03 00 00 14` | b 0x00bac2bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac2b4"></a> `00bac2b4` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00bac2b8"></a> `00bac2b8` | `82 fc ff 54` | b.cs 0x00bac248 | `CONDITIONAL_JUMP`
<a id="insn-00bac2bc"></a> `00bac2bc` | `1f 03 1c eb` | cmp x24,x28 | `FALL_THROUGH`
<a id="insn-00bac2c0"></a> `00bac2c0` | `a8 05 00 54` | b.hi 0x00bac374 | `CONDITIONAL_JUMP`
<a id="insn-00bac2c4"></a> `00bac2c4` | `e8 2b 40 b9` | ldr w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac2c8"></a> `00bac2c8` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00bac2cc"></a> `00bac2cc` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bac2d0"></a> `00bac2d0` | `13 87 00 f8` | str x19,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bac2d4"></a> `00bac2d4` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac2d8"></a> `00bac2d8` | `95 03 00 f9` | str x21,[x28] | `FALL_THROUGH`
<a id="insn-00bac2dc"></a> `00bac2dc` | `e8 2b 00 b9` | str w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac2e0"></a> `00bac2e0` | `99 03 96 9a` | csel x25,x28,x22,eq | `FALL_THROUGH`
<a id="insn-00bac2e4"></a> `00bac2e4` | `b3 ff ff 17` | b 0x00bac1b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac2e8"></a> `00bac2e8` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac2ec"></a> `00bac2ec` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bac2f0"></a> `00bac2f0` | `17 01 40 f9` | ldr x23,[x8] | `FALL_THROUGH`
<a id="insn-00bac2f4"></a> `00bac2f4` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bac2f8"></a> `00bac2f8` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bac2fc"></a> `00bac2fc` | `76 23 00 91` | add x22,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac300"></a> `00bac300` | `01 0b 00 54` | b.ne 0x00bac460 | `CONDITIONAL_JUMP`
<a id="insn-00bac304"></a> `00bac304` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bac308"></a> `00bac308` | `ea 06 40 f9` | ldr x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bac30c"></a> `00bac30c` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bac310"></a> `00bac310` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bac314"></a> `00bac314` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac318"></a> `00bac318` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac31c"></a> `00bac31c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac320"></a> `00bac320` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac324"></a> `00bac324` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac328"></a> `00bac328` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac32c"></a> `00bac32c` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac330"></a> `00bac330` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bac334"></a> `00bac334` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bac338"></a> `00bac338` | `02 0a 00 b4` | cbz x2,0x00bac478 | `CONDITIONAL_JUMP`
<a id="insn-00bac33c"></a> `00bac33c` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bac340"></a> `00bac340` | `eb 0a 40 f9` | ldr x11,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bac344"></a> `00bac344` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac348"></a> `00bac348` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bac34c"></a> `00bac34c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac350"></a> `00bac350` | `61 15 97 9a` | csinc x1,x11,x23,ne | `FALL_THROUGH`
<a id="insn-00bac354"></a> `00bac354` | `3f af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac358"></a> `00bac358` | `00 09 00 34` | cbz w0,0x00bac478 | `CONDITIONAL_JUMP`
<a id="insn-00bac35c"></a> `00bac35c` | `20 09 f8 36` | tbz w0,#0x1f,0x00bac480 | `CONDITIONAL_JUMP`
<a id="insn-00bac360"></a> `00bac360` | `70 00 00 14` | b 0x00bac520 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac364"></a> `00bac364` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac368"></a> `00bac368` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bac36c"></a> `00bac36c` | `01 01 00 54` | b.ne 0x00bac38c | `CONDITIONAL_JUMP`
<a id="insn-00bac370"></a> `00bac370` | `28 00 00 14` | b 0x00bac410 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac374"></a> `00bac374` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac378"></a> `00bac378` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac37c"></a> `00bac37c` | `fa 2b 40 b9` | ldr w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac380"></a> `00bac380` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00bac384"></a> `00bac384` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bac388"></a> `00bac388` | `40 04 00 54` | b.eq 0x00bac410 | `CONDITIONAL_JUMP`
<a id="insn-00bac38c"></a> `00bac38c` | `33 03 40 f9` | ldr x19,[x25] | `FALL_THROUGH`
<a id="insn-00bac390"></a> `00bac390` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00bac394"></a> `00bac394` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac398"></a> `00bac398` | `a9 42 40 f9` | ldr x9,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bac39c"></a> `00bac39c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bac3a0"></a> `00bac3a0` | `01 03 00 54` | b.ne 0x00bac400 | `CONDITIONAL_JUMP`
<a id="insn-00bac3a4"></a> `00bac3a4` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bac3a8"></a> `00bac3a8` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac3ac"></a> `00bac3ac` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bac3b0"></a> `00bac3b0` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac3b4"></a> `00bac3b4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3b8"></a> `00bac3b8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3bc"></a> `00bac3bc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3c0"></a> `00bac3c0` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac3c4"></a> `00bac3c4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3c8"></a> `00bac3c8` | `b7 01 8b 9a` | csel x23,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac3cc"></a> `00bac3cc` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00bac3d0"></a> `00bac3d0` | `82 32 97 9a` | csel x2,x20,x23,cc | `FALL_THROUGH`
<a id="insn-00bac3d4"></a> `00bac3d4` | `c2 04 00 b4` | cbz x2,0x00bac46c | `CONDITIONAL_JUMP`
<a id="insn-00bac3d8"></a> `00bac3d8` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac3dc"></a> `00bac3dc` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac3e0"></a> `00bac3e0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3e4"></a> `00bac3e4` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bac3e8"></a> `00bac3e8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3ec"></a> `00bac3ec` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bac3f0"></a> `00bac3f0` | `18 af 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac3f4"></a> `00bac3f4` | `c0 03 00 34` | cbz w0,0x00bac46c | `CONDITIONAL_JUMP`
<a id="insn-00bac3f8"></a> `00bac3f8` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bac404 | `CONDITIONAL_JUMP`
<a id="insn-00bac3fc"></a> `00bac3fc` | `05 00 00 14` | b 0x00bac410 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac400"></a> `00bac400` | `82 00 00 54` | b.cs 0x00bac410 | `CONDITIONAL_JUMP`
<a id="insn-00bac404"></a> `00bac404` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00bac408"></a> `00bac408` | `13 03 00 f9` | str x19,[x24] | `FALL_THROUGH`
<a id="insn-00bac40c"></a> `00bac40c` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-00bac410"></a> `00bac410` | `7a 01 00 35` | cbnz w26,0x00bac43c | `CONDITIONAL_JUMP`
<a id="insn-00bac414"></a> `00bac414` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac418"></a> `00bac418` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bac41c"></a> `00bac41c` | `32 03 00 94` | bl 0x00bad0e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bac420"></a> `00bac420` | `16 23 00 91` | add x22,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bac424"></a> `00bac424` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bac428"></a> `00bac428` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bac42c"></a> `00bac42c` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bac430"></a> `00bac430` | `2d 03 00 94` | bl 0x00bad0e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bac434"></a> `00bac434` | `80 11 00 37` | tbnz w0,#0x0,0x00bac664 | `CONDITIONAL_JUMP`
<a id="insn-00bac438"></a> `00bac438` | `17 dd 07 37` | tbnz w23,#0x0,0x00babfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bac43c"></a> `00bac43c` | `08 03 1b cb` | sub x8,x24,x27 | `FALL_THROUGH`
<a id="insn-00bac440"></a> `00bac440` | `89 03 18 cb` | sub x9,x28,x24 | `FALL_THROUGH`
<a id="insn-00bac444"></a> `00bac444` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bac448"></a> `00bac448` | `4a 10 00 54` | b.ge 0x00bac650 | `CONDITIONAL_JUMP`
<a id="insn-00bac44c"></a> `00bac44c` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac450"></a> `00bac450` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bac454"></a> `00bac454` | `d2 fe ff 97` | bl 0x00babf9c | `UNCONDITIONAL_CALL`
<a id="insn-00bac458"></a> `00bac458` | `16 23 00 91` | add x22,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bac45c"></a> `00bac45c` | `df fe ff 17` | b 0x00babfd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac460"></a> `00bac460` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac464"></a> `00bac464` | `e2 00 00 54` | b.cs 0x00bac480 | `CONDITIONAL_JUMP`
<a id="insn-00bac468"></a> `00bac468` | `2e 00 00 14` | b 0x00bac520 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac46c"></a> `00bac46c` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00bac470"></a> `00bac470` | `a3 fc ff 54` | b.cc 0x00bac404 | `CONDITIONAL_JUMP`
<a id="insn-00bac474"></a> `00bac474` | `e7 ff ff 17` | b 0x00bac410 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac478"></a> `00bac478` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bac47c"></a> `00bac47c` | `23 05 00 54` | b.cc 0x00bac520 | `CONDITIONAL_JUMP`
<a id="insn-00bac480"></a> `00bac480` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac484"></a> `00bac484` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bac488"></a> `00bac488` | `40 25 00 54` | b.eq 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac48c"></a> `00bac48c` | `15 07 00 91` | add x21,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bac490"></a> `00bac490` | `76 43 00 91` | add x22,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bac494"></a> `00bac494` | `06 00 00 14` | b 0x00bac4ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bac498"></a> `00bac498` | `9f 02 19 eb` | cmp x20,x25 | `FALL_THROUGH`
<a id="insn-00bac49c"></a> `00bac49c` | `c3 03 00 54` | b.cc 0x00bac514 | `CONDITIONAL_JUMP`
<a id="insn-00bac4a0"></a> `00bac4a0` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bac4a4"></a> `00bac4a4` | `9f 03 16 eb` | cmp x28,x22 | `FALL_THROUGH`
<a id="insn-00bac4a8"></a> `00bac4a8` | `40 24 00 54` | b.eq 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac4ac"></a> `00bac4ac` | `d3 82 5f f8` | ldur x19,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00bac4b0"></a> `00bac4b0` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac4b4"></a> `00bac4b4` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00bac4b8"></a> `00bac4b8` | `21 ff ff 54` | b.ne 0x00bac49c | `CONDITIONAL_JUMP`
<a id="insn-00bac4bc"></a> `00bac4bc` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac4c0"></a> `00bac4c0` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac4c4"></a> `00bac4c4` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bac4c8"></a> `00bac4c8` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bac4cc"></a> `00bac4cc` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4d0"></a> `00bac4d0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4d4"></a> `00bac4d4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4d8"></a> `00bac4d8` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac4dc"></a> `00bac4dc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4e0"></a> `00bac4e0` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac4e4"></a> `00bac4e4` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00bac4e8"></a> `00bac4e8` | `22 33 94 9a` | csel x2,x25,x20,cc | `FALL_THROUGH`
<a id="insn-00bac4ec"></a> `00bac4ec` | `62 fd ff b4` | cbz x2,0x00bac498 | `CONDITIONAL_JUMP`
<a id="insn-00bac4f0"></a> `00bac4f0` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bac4f4"></a> `00bac4f4` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac4f8"></a> `00bac4f8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4fc"></a> `00bac4fc` | `a0 02 8a 9a` | csel x0,x21,x10,eq | `FALL_THROUGH`
<a id="insn-00bac500"></a> `00bac500` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac504"></a> `00bac504` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bac508"></a> `00bac508` | `d2 ae 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac50c"></a> `00bac50c` | `60 fc ff 34` | cbz w0,0x00bac498 | `CONDITIONAL_JUMP`
<a id="insn-00bac510"></a> `00bac510` | `80 fc ff 36` | tbz w0,#0x1f,0x00bac4a0 | `CONDITIONAL_JUMP`
<a id="insn-00bac514"></a> `00bac514` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac518"></a> `00bac518` | `d7 82 1f f8` | stur x23,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00bac51c"></a> `00bac51c` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00bac520"></a> `00bac520` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac524"></a> `00bac524` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bac528"></a> `00bac528` | `40 20 00 54` | b.eq 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac52c"></a> `00bac52c` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac530"></a> `00bac530` | `78 03 40 f9` | ldr x24,[x27] | `FALL_THROUGH`
<a id="insn-00bac534"></a> `00bac534` | `1b 43 40 f9` | ldr x27,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bac538"></a> `00bac538` | `19 07 00 91` | add x25,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bac53c"></a> `00bac53c` | `03 00 00 14` | b 0x00bac548 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac540"></a> `00bac540` | `23 04 00 54` | b.cc 0x00bac5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac544"></a> `00bac544` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bac548"></a> `00bac548` | `d5 02 40 f9` | ldr x21,[x22] | `FALL_THROUGH`
<a id="insn-00bac54c"></a> `00bac54c` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bac550"></a> `00bac550` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bac554"></a> `00bac554` | `61 ff ff 54` | b.ne 0x00bac540 | `CONDITIONAL_JUMP`
<a id="insn-00bac558"></a> `00bac558` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bac55c"></a> `00bac55c` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac560"></a> `00bac560` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bac564"></a> `00bac564` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bac568"></a> `00bac568` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac56c"></a> `00bac56c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac570"></a> `00bac570` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac574"></a> `00bac574` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac578"></a> `00bac578` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac57c"></a> `00bac57c` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac580"></a> `00bac580` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bac584"></a> `00bac584` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bac588"></a> `00bac588` | `62 01 00 b4` | cbz x2,0x00bac5b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac58c"></a> `00bac58c` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bac590"></a> `00bac590` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac594"></a> `00bac594` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac598"></a> `00bac598` | `20 03 8a 9a` | csel x0,x25,x10,eq | `FALL_THROUGH`
<a id="insn-00bac59c"></a> `00bac59c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac5a0"></a> `00bac5a0` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bac5a4"></a> `00bac5a4` | `ab ae 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac5a8"></a> `00bac5a8` | `60 00 00 34` | cbz w0,0x00bac5b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac5ac"></a> `00bac5ac` | `c0 fc ff 36` | tbz w0,#0x1f,0x00bac544 | `CONDITIONAL_JUMP`
<a id="insn-00bac5b0"></a> `00bac5b0` | `05 00 00 14` | b 0x00bac5c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac5b4"></a> `00bac5b4` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bac5b8"></a> `00bac5b8` | `62 fc ff 54` | b.cs 0x00bac544 | `CONDITIONAL_JUMP`
<a id="insn-00bac5bc"></a> `00bac5bc` | `02 00 00 14` | b 0x00bac5c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac5c0"></a> `00bac5c0` | `c2 03 00 54` | b.cs 0x00bac638 | `CONDITIONAL_JUMP`
<a id="insn-00bac5c4"></a> `00bac5c4` | `f3 8e 5f f8` | ldr x19,[x23, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bac5c8"></a> `00bac5c8` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac5cc"></a> `00bac5cc` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bac5d0"></a> `00bac5d0` | `81 ff ff 54` | b.ne 0x00bac5c0 | `CONDITIONAL_JUMP`
<a id="insn-00bac5d4"></a> `00bac5d4` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac5d8"></a> `00bac5d8` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac5dc"></a> `00bac5dc` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bac5e0"></a> `00bac5e0` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bac5e4"></a> `00bac5e4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac5e8"></a> `00bac5e8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac5ec"></a> `00bac5ec` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac5f0"></a> `00bac5f0` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac5f4"></a> `00bac5f4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac5f8"></a> `00bac5f8` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac5fc"></a> `00bac5fc` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bac600"></a> `00bac600` | `42 33 94 9a` | csel x2,x26,x20,cc | `FALL_THROUGH`
<a id="insn-00bac604"></a> `00bac604` | `62 01 00 b4` | cbz x2,0x00bac630 | `CONDITIONAL_JUMP`
<a id="insn-00bac608"></a> `00bac608` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bac60c"></a> `00bac60c` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac610"></a> `00bac610` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac614"></a> `00bac614` | `20 03 8a 9a` | csel x0,x25,x10,eq | `FALL_THROUGH`
<a id="insn-00bac618"></a> `00bac618` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac61c"></a> `00bac61c` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bac620"></a> `00bac620` | `8c ae 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac624"></a> `00bac624` | `60 00 00 34` | cbz w0,0x00bac630 | `CONDITIONAL_JUMP`
<a id="insn-00bac628"></a> `00bac628` | `e0 fc ff 37` | tbnz w0,#0x1f,0x00bac5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac62c"></a> `00bac62c` | `03 00 00 14` | b 0x00bac638 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac630"></a> `00bac630` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bac634"></a> `00bac634` | `83 fc ff 54` | b.cc 0x00bac5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac638"></a> `00bac638` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bac63c"></a> `00bac63c` | `e2 cc ff 54` | b.cs 0x00babfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bac640"></a> `00bac640` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac644"></a> `00bac644` | `d3 86 00 f8` | str x19,[x22], #0x8 | `FALL_THROUGH`
<a id="insn-00bac648"></a> `00bac648` | `f5 02 00 f9` | str x21,[x23] | `FALL_THROUGH`
<a id="insn-00bac64c"></a> `00bac64c` | `b9 ff ff 17` | b 0x00bac530 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac650"></a> `00bac650` | `00 23 00 91` | add x0,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bac654"></a> `00bac654` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bac658"></a> `00bac658` | `51 fe ff 97` | bl 0x00babf9c | `UNCONDITIONAL_CALL`
<a id="insn-00bac65c"></a> `00bac65c` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00bac660"></a> `00bac660` | `59 fe ff 17` | b 0x00babfc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac664"></a> `00bac664` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00bac668"></a> `00bac668` | `f7 ca 07 36` | tbz w23,#0x0,0x00babfc4 | `CONDITIONAL_JUMP`
<a id="insn-00bac66c"></a> `00bac66c` | `b1 00 00 14` | b 0x00bac930 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac670"></a> `00bac670` | `09 bb ff d0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00bac674"></a> `00bac674` | `29 01 08 91` | add x9,x9,#0x200 | `FALL_THROUGH`
<a id="insn-00bac678"></a> `00bac678` | `8a 00 00 10` | adr x10,0xbac688 | `FALL_THROUGH`
<a id="insn-00bac67c"></a> `00bac67c` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac680"></a> `00bac680` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bac684"></a> `00bac684` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00bac688"></a> `00bac688` | `93 83 5f f8` | ldur x19,[x28, #-0x8] | `FALL_THROUGH`
<a id="insn-00bac68c"></a> `00bac68c` | `75 03 40 f9` | ldr x21,[x27] | `FALL_THROUGH`
<a id="insn-00bac690"></a> `00bac690` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac694"></a> `00bac694` | `a9 42 40 f9` | ldr x9,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bac698"></a> `00bac698` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bac69c"></a> `00bac69c` | `41 14 00 54` | b.ne 0x00bac924 | `CONDITIONAL_JUMP`
<a id="insn-00bac6a0"></a> `00bac6a0` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bac6a4"></a> `00bac6a4` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bac6a8"></a> `00bac6a8` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bac6ac"></a> `00bac6ac` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac6b0"></a> `00bac6b0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6b4"></a> `00bac6b4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6b8"></a> `00bac6b8` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6bc"></a> `00bac6bc` | `96 01 8a 9a` | csel x22,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac6c0"></a> `00bac6c0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6c4"></a> `00bac6c4` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac6c8"></a> `00bac6c8` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00bac6cc"></a> `00bac6cc` | `c2 32 94 9a` | csel x2,x22,x20,cc | `FALL_THROUGH`
<a id="insn-00bac6d0"></a> `00bac6d0` | `82 12 00 b4` | cbz x2,0x00bac920 | `CONDITIONAL_JUMP`
<a id="insn-00bac6d4"></a> `00bac6d4` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac6d8"></a> `00bac6d8` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bac6dc"></a> `00bac6dc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6e0"></a> `00bac6e0` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bac6e4"></a> `00bac6e4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac6e8"></a> `00bac6e8` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bac6ec"></a> `00bac6ec` | `59 ae 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac6f0"></a> `00bac6f0` | `80 11 00 34` | cbz w0,0x00bac920 | `CONDITIONAL_JUMP`
<a id="insn-00bac6f4"></a> `00bac6f4` | `a0 11 f8 37` | tbnz w0,#0x1f,0x00bac928 | `CONDITIONAL_JUMP`
<a id="insn-00bac6f8"></a> `00bac6f8` | `8e 00 00 14` | b 0x00bac930 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac6fc"></a> `00bac6fc` | `75 43 00 91` | add x21,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bac700"></a> `00bac700` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac704"></a> `00bac704` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac708"></a> `00bac708` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bac70c"></a> `00bac70c` | `91 00 00 94` | bl 0x00bac950 | `UNCONDITIONAL_CALL`
<a id="insn-00bac710"></a> `00bac710` | `68 63 00 91` | add x8,x27,#0x18 | `FALL_THROUGH`
<a id="insn-00bac714"></a> `00bac714` | `1f 01 1c eb` | cmp x8,x28 | `FALL_THROUGH`
<a id="insn-00bac718"></a> `00bac718` | `c0 10 00 54` | b.eq 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac71c"></a> `00bac71c` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bac720"></a> `00bac720` | `08 00 00 14` | b 0x00bac740 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac724"></a> `00bac724` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00bac728"></a> `00bac728` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac72c"></a> `00bac72c` | `17 03 00 f9` | str x23,[x24] | `FALL_THROUGH`
<a id="insn-00bac730"></a> `00bac730` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bac734"></a> `00bac734` | `1f 01 1c eb` | cmp x8,x28 | `FALL_THROUGH`
<a id="insn-00bac738"></a> `00bac738` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bac73c"></a> `00bac73c` | `a0 0f 00 54` | b.eq 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac740"></a> `00bac740` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00bac744"></a> `00bac744` | `17 01 40 f9` | ldr x23,[x8] | `FALL_THROUGH`
<a id="insn-00bac748"></a> `00bac748` | `13 03 40 f9` | ldr x19,[x24] | `FALL_THROUGH`
<a id="insn-00bac74c"></a> `00bac74c` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bac750"></a> `00bac750` | `f9 42 40 f9` | ldr x25,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bac754"></a> `00bac754` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac758"></a> `00bac758` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bac75c"></a> `00bac75c` | `01 03 00 54` | b.ne 0x00bac7bc | `CONDITIONAL_JUMP`
<a id="insn-00bac760"></a> `00bac760` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac764"></a> `00bac764` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac768"></a> `00bac768` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bac76c"></a> `00bac76c` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bac770"></a> `00bac770` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac774"></a> `00bac774` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac778"></a> `00bac778` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac77c"></a> `00bac77c` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac780"></a> `00bac780` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac784"></a> `00bac784` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac788"></a> `00bac788` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bac78c"></a> `00bac78c` | `82 32 9a 9a` | csel x2,x20,x26,cc | `FALL_THROUGH`
<a id="insn-00bac790"></a> `00bac790` | `a2 01 00 b4` | cbz x2,0x00bac7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac794"></a> `00bac794` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bac798"></a> `00bac798` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac79c"></a> `00bac79c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac7a0"></a> `00bac7a0` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bac7a4"></a> `00bac7a4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac7a8"></a> `00bac7a8` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bac7ac"></a> `00bac7ac` | `29 ae 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac7b0"></a> `00bac7b0` | `a0 00 00 34` | cbz w0,0x00bac7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac7b4"></a> `00bac7b4` | `e0 fb ff 36` | tbz w0,#0x1f,0x00bac730 | `CONDITIONAL_JUMP`
<a id="insn-00bac7b8"></a> `00bac7b8` | `05 00 00 14` | b 0x00bac7cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac7bc"></a> `00bac7bc` | `a2 fb ff 54` | b.cs 0x00bac730 | `CONDITIONAL_JUMP`
<a id="insn-00bac7c0"></a> `00bac7c0` | `03 00 00 14` | b 0x00bac7cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac7c4"></a> `00bac7c4` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bac7c8"></a> `00bac7c8` | `42 fb ff 54` | b.cs 0x00bac730 | `CONDITIONAL_JUMP`
<a id="insn-00bac7cc"></a> `00bac7cc` | `1f 03 1b eb` | cmp x24,x27 | `FALL_THROUGH`
<a id="insn-00bac7d0"></a> `00bac7d0` | `b3 02 00 f9` | str x19,[x21] | `FALL_THROUGH`
<a id="insn-00bac7d4"></a> `00bac7d4` | `c0 fa ff 54` | b.eq 0x00bac72c | `CONDITIONAL_JUMP`
<a id="insn-00bac7d8"></a> `00bac7d8` | `e8 06 00 91` | add x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bac7dc"></a> `00bac7dc` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bac7e0"></a> `00bac7e0` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac7e4"></a> `00bac7e4` | `07 00 00 14` | b 0x00bac800 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac7e8"></a> `00bac7e8` | `02 fa ff 54` | b.cs 0x00bac728 | `CONDITIONAL_JUMP`
<a id="insn-00bac7ec"></a> `00bac7ec` | `5a 23 00 d1` | sub x26,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00bac7f0"></a> `00bac7f0` | `18 23 00 d1` | sub x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bac7f4"></a> `00bac7f4` | `5f 43 00 b1` | cmn x26,#0x10 | `FALL_THROUGH`
<a id="insn-00bac7f8"></a> `00bac7f8` | `93 0b 00 f9` | str x19,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00bac7fc"></a> `00bac7fc` | `40 f9 ff 54` | b.eq 0x00bac724 | `CONDITIONAL_JUMP`
<a id="insn-00bac800"></a> `00bac800` | `7c 03 1a 8b` | add x28,x27,x26 | `FALL_THROUGH`
<a id="insn-00bac804"></a> `00bac804` | `93 07 40 f9` | ldr x19,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00bac808"></a> `00bac808` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bac80c"></a> `00bac80c` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bac810"></a> `00bac810` | `c1 fe ff 54` | b.ne 0x00bac7e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac814"></a> `00bac814` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac818"></a> `00bac818` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bac81c"></a> `00bac81c` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bac820"></a> `00bac820` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bac824"></a> `00bac824` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac828"></a> `00bac828` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac82c"></a> `00bac82c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac830"></a> `00bac830` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bac834"></a> `00bac834` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac838"></a> `00bac838` | `bb 01 8b 9a` | csel x27,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bac83c"></a> `00bac83c` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bac840"></a> `00bac840` | `82 32 9b 9a` | csel x2,x20,x27,cc | `FALL_THROUGH`
<a id="insn-00bac844"></a> `00bac844` | `a2 01 00 b4` | cbz x2,0x00bac878 | `CONDITIONAL_JUMP`
<a id="insn-00bac848"></a> `00bac848` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bac84c"></a> `00bac84c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bac850"></a> `00bac850` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bac854"></a> `00bac854` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bac858"></a> `00bac858` | `20 01 8a 9a` | csel x0,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00bac85c"></a> `00bac85c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac860"></a> `00bac860` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bac864"></a> `00bac864` | `fb ad 02 94` | bl 0x00c58050 | `UNCONDITIONAL_CALL`
<a id="insn-00bac868"></a> `00bac868` | `80 00 00 34` | cbz w0,0x00bac878 | `CONDITIONAL_JUMP`
<a id="insn-00bac86c"></a> `00bac86c` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac870"></a> `00bac870` | `e0 fb ff 37` | tbnz w0,#0x1f,0x00bac7ec | `CONDITIONAL_JUMP`
<a id="insn-00bac874"></a> `00bac874` | `ad ff ff 17` | b 0x00bac728 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac878"></a> `00bac878` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bac87c"></a> `00bac87c` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac880"></a> `00bac880` | `63 fb ff 54` | b.cc 0x00bac7ec | `CONDITIONAL_JUMP`
<a id="insn-00bac884"></a> `00bac884` | `68 03 1a 8b` | add x8,x27,x26 | `FALL_THROUGH`
<a id="insn-00bac888"></a> `00bac888` | `18 41 00 91` | add x24,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bac88c"></a> `00bac88c` | `a7 ff ff 17` | b 0x00bac728 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac890"></a> `00bac890` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac894"></a> `00bac894` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac898"></a> `00bac898` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac89c"></a> `00bac89c` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bac8a0"></a> `00bac8a0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bac8a4"></a> `00bac8a4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bac8a8"></a> `00bac8a8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bac8ac"></a> `00bac8ac` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bac8b0"></a> `00bac8b0` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac8b4"></a> `00bac8b4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bac8b8"></a> `00bac8b8` | `26 00 00 14` | b 0x00bac950 | `CALL_TERMINATOR`
<a id="insn-00bac8bc"></a> `00bac8bc` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac8c0"></a> `00bac8c0` | `62 43 00 91` | add x2,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bac8c4"></a> `00bac8c4` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac8c8"></a> `00bac8c8` | `e3 0f 40 f9` | ldr x3,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac8cc"></a> `00bac8cc` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bac8d0"></a> `00bac8d0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bac8d4"></a> `00bac8d4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bac8d8"></a> `00bac8d8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bac8dc"></a> `00bac8dc` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bac8e0"></a> `00bac8e0` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac8e4"></a> `00bac8e4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bac8e8"></a> `00bac8e8` | `c5 00 00 14` | b 0x00bacbfc | `CALL_TERMINATOR`
<a id="insn-00bac8ec"></a> `00bac8ec` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bac8f0"></a> `00bac8f0` | `62 43 00 91` | add x2,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bac8f4"></a> `00bac8f4` | `63 63 00 91` | add x3,x27,#0x18 | `FALL_THROUGH`
<a id="insn-00bac8f8"></a> `00bac8f8` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bac8fc"></a> `00bac8fc` | `e4 0f 40 f9` | ldr x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bac900"></a> `00bac900` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bac904"></a> `00bac904` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bac908"></a> `00bac908` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bac90c"></a> `00bac90c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bac910"></a> `00bac910` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bac914"></a> `00bac914` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac918"></a> `00bac918` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bac91c"></a> `00bac91c` | `3a 01 00 14` | b 0x00bace04 | `CALL_TERMINATOR`
<a id="insn-00bac920"></a> `00bac920` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-00bac924"></a> `00bac924` | `62 00 00 54` | b.cs 0x00bac930 | `CONDITIONAL_JUMP`
<a id="insn-00bac928"></a> `00bac928` | `73 03 00 f9` | str x19,[x27] | `FALL_THROUGH`
<a id="insn-00bac92c"></a> `00bac92c` | `95 83 1f f8` | stur x21,[x28, #-0x8] | `FALL_THROUGH`
<a id="insn-00bac930"></a> `00bac930` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bac934"></a> `00bac934` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bac938"></a> `00bac938` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bac93c"></a> `00bac93c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bac940"></a> `00bac940` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bac944"></a> `00bac944` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac948"></a> `00bac948` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bac94c"></a> `00bac94c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babf9c`](#insn-00babf9c) 範囲 `[['00babf9c', '00babfbb']]`
  - `FALL_THROUGH` [`00babfb8`](#insn-00babfb8) → [`00babfbc`](#insn-00babfbc)
- ブロック [`00babfbc`](#insn-00babfbc) 範囲 `[['00babfbc', '00babfc3']]`
  - `FALL_THROUGH` [`00babfc0`](#insn-00babfc0) → [`00babfc4`](#insn-00babfc4)
- ブロック [`00babfc4`](#insn-00babfc4) 範囲 `[['00babfc4', '00babfd7']]`
  - `FALL_THROUGH` [`00babfd4`](#insn-00babfd4) → [`00babfd8`](#insn-00babfd8)
- ブロック [`00babfd8`](#insn-00babfd8) 範囲 `[['00babfd8', '00babfdb']]`
  - `FALL_THROUGH` [`00babfd8`](#insn-00babfd8) → [`00babfdc`](#insn-00babfdc)
- ブロック [`00babfdc`](#insn-00babfdc) 範囲 `[['00babfdc', '00babfeb']]`
  - `CONDITIONAL_JUMP` [`00babfe8`](#insn-00babfe8) → [`00bac670`](#insn-00bac670)
  - `FALL_THROUGH` [`00babfe8`](#insn-00babfe8) → [`00babfec`](#insn-00babfec)
- ブロック [`00babfec`](#insn-00babfec) 範囲 `[['00babfec', '00babff7']]`
  - `CONDITIONAL_JUMP` [`00babff4`](#insn-00babff4) → [`00bac6fc`](#insn-00bac6fc)
  - `FALL_THROUGH` [`00babff4`](#insn-00babff4) → [`00babff8`](#insn-00babff8)
- ブロック [`00babff8`](#insn-00babff8) 範囲 `[['00babff8', '00babffb']]`
  - `FALL_THROUGH` [`00babff8`](#insn-00babff8) → [`00babffc`](#insn-00babffc)
- ブロック [`00babffc`](#insn-00babffc) 範囲 `[['00babffc', '00babfff']]`
  - `FALL_THROUGH` [`00babffc`](#insn-00babffc) → [`00bac000`](#insn-00bac000)
- ブロック [`00bac000`](#insn-00bac000) 範囲 `[['00bac000', '00bac003']]`
  - `FALL_THROUGH` [`00bac000`](#insn-00bac000) → [`00bac004`](#insn-00bac004)
- ブロック [`00bac004`](#insn-00bac004) 範囲 `[['00bac004', '00bac007']]`
  - `FALL_THROUGH` [`00bac004`](#insn-00bac004) → [`00bac008`](#insn-00bac008)
- ブロック [`00bac008`](#insn-00bac008) 範囲 `[['00bac008', '00bac00b']]`
  - `FALL_THROUGH` [`00bac008`](#insn-00bac008) → [`00bac00c`](#insn-00bac00c)
- ブロック [`00bac00c`](#insn-00bac00c) 範囲 `[['00bac00c', '00bac00f']]`
  - `FALL_THROUGH` [`00bac00c`](#insn-00bac00c) → [`00bac010`](#insn-00bac010)
- ブロック [`00bac010`](#insn-00bac010) 範囲 `[['00bac010', '00bac013']]`
  - `FALL_THROUGH` [`00bac010`](#insn-00bac010) → [`00bac014`](#insn-00bac014)
- ブロック [`00bac014`](#insn-00bac014) 範囲 `[['00bac014', '00bac017']]`
  - `CONDITIONAL_JUMP` [`00bac014`](#insn-00bac014) → [`00bac048`](#insn-00bac048)
  - `FALL_THROUGH` [`00bac014`](#insn-00bac014) → [`00bac018`](#insn-00bac018)
- ブロック [`00bac018`](#insn-00bac018) 範囲 `[['00bac018', '00bac027']]`
  - `FALL_THROUGH` [`00bac024`](#insn-00bac024) → [`00bac028`](#insn-00bac028)
- ブロック [`00bac028`](#insn-00bac028) 範囲 `[['00bac028', '00bac02b']]`
  - `FALL_THROUGH` [`00bac028`](#insn-00bac028) → [`00bac02c`](#insn-00bac02c)
- ブロック [`00bac02c`](#insn-00bac02c) 範囲 `[['00bac02c', '00bac02f']]`
  - `FALL_THROUGH` [`00bac02c`](#insn-00bac02c) → [`00bac030`](#insn-00bac030)
- ブロック [`00bac030`](#insn-00bac030) 範囲 `[['00bac030', '00bac033']]`
  - `FALL_THROUGH` [`00bac030`](#insn-00bac030) → [`00bac034`](#insn-00bac034)
- ブロック [`00bac034`](#insn-00bac034) 範囲 `[['00bac034', '00bac037']]`
  - `FALL_THROUGH` [`00bac034`](#insn-00bac034) → [`00bac038`](#insn-00bac038)
- ブロック [`00bac038`](#insn-00bac038) 範囲 `[['00bac038', '00bac03b']]`
  - `FALL_THROUGH` [`00bac038`](#insn-00bac038) → [`00bac03c`](#insn-00bac03c)
- ブロック [`00bac03c`](#insn-00bac03c) 範囲 `[['00bac03c', '00bac03f']]`
  - `FALL_THROUGH` [`00bac03c`](#insn-00bac03c) → [`00bac040`](#insn-00bac040)
- ブロック [`00bac040`](#insn-00bac040) 範囲 `[['00bac040', '00bac047']]`
  - `UNCONDITIONAL_JUMP` [`00bac044`](#insn-00bac044) → [`00bac058`](#insn-00bac058)
- ブロック [`00bac048`](#insn-00bac048) 範囲 `[['00bac048', '00bac057']]`
  - `FALL_THROUGH` [`00bac054`](#insn-00bac054) → [`00bac058`](#insn-00bac058)
- ブロック [`00bac058`](#insn-00bac058) 範囲 `[['00bac058', '00bac05b']]`
  - `FALL_THROUGH` [`00bac058`](#insn-00bac058) → [`00bac05c`](#insn-00bac05c)
- ブロック [`00bac05c`](#insn-00bac05c) 範囲 `[['00bac05c', '00bac05f']]`
  - `FALL_THROUGH` [`00bac05c`](#insn-00bac05c) → [`00bac060`](#insn-00bac060)
- ブロック [`00bac060`](#insn-00bac060) 範囲 `[['00bac060', '00bac063']]`
  - `FALL_THROUGH` [`00bac060`](#insn-00bac060) → [`00bac064`](#insn-00bac064)
- ブロック [`00bac064`](#insn-00bac064) 範囲 `[['00bac064', '00bac07b']]`
  - `CONDITIONAL_JUMP` [`00bac078`](#insn-00bac078) → [`00bac0d8`](#insn-00bac0d8)
  - `FALL_THROUGH` [`00bac078`](#insn-00bac078) → [`00bac07c`](#insn-00bac07c)
- ブロック [`00bac07c`](#insn-00bac07c) 範囲 `[['00bac07c', '00bac08f']]`
  - `FALL_THROUGH` [`00bac08c`](#insn-00bac08c) → [`00bac090`](#insn-00bac090)
- ブロック [`00bac090`](#insn-00bac090) 範囲 `[['00bac090', '00bac0af']]`
  - `CONDITIONAL_JUMP` [`00bac0ac`](#insn-00bac0ac) → [`00bac0e4`](#insn-00bac0e4)
  - `FALL_THROUGH` [`00bac0ac`](#insn-00bac0ac) → [`00bac0b0`](#insn-00bac0b0)
- ブロック [`00bac0b0`](#insn-00bac0b0) 範囲 `[['00bac0b0', '00bac0b3']]`
  - `FALL_THROUGH` [`00bac0b0`](#insn-00bac0b0) → [`00bac0b4`](#insn-00bac0b4)
- ブロック [`00bac0b4`](#insn-00bac0b4) 範囲 `[['00bac0b4', '00bac0cb']]`
  - `FALL_THROUGH` [`00bac0c8`](#insn-00bac0c8) → [`00bac0cc`](#insn-00bac0cc)
- ブロック [`00bac0cc`](#insn-00bac0cc) 範囲 `[['00bac0cc', '00bac0cf']]`
  - `CONDITIONAL_JUMP` [`00bac0cc`](#insn-00bac0cc) → [`00bac0e4`](#insn-00bac0e4)
  - `FALL_THROUGH` [`00bac0cc`](#insn-00bac0cc) → [`00bac0d0`](#insn-00bac0d0)
- ブロック [`00bac0d0`](#insn-00bac0d0) 範囲 `[['00bac0d0', '00bac0d3']]`
  - `CONDITIONAL_JUMP` [`00bac0d0`](#insn-00bac0d0) → [`00bac0dc`](#insn-00bac0dc)
  - `FALL_THROUGH` [`00bac0d0`](#insn-00bac0d0) → [`00bac0d4`](#insn-00bac0d4)
- ブロック [`00bac0d4`](#insn-00bac0d4) 範囲 `[['00bac0d4', '00bac0d7']]`
  - `UNCONDITIONAL_JUMP` [`00bac0d4`](#insn-00bac0d4) → [`00bac0ec`](#insn-00bac0ec)
- ブロック [`00bac0d8`](#insn-00bac0d8) 範囲 `[['00bac0d8', '00bac0db']]`
  - `CONDITIONAL_JUMP` [`00bac0d8`](#insn-00bac0d8) → [`00bac0ec`](#insn-00bac0ec)
  - `FALL_THROUGH` [`00bac0d8`](#insn-00bac0d8) → [`00bac0dc`](#insn-00bac0dc)
- ブロック [`00bac0dc`](#insn-00bac0dc) 範囲 `[['00bac0dc', '00bac0e3']]`
  - `UNCONDITIONAL_JUMP` [`00bac0e0`](#insn-00bac0e0) → [`00bac19c`](#insn-00bac19c)
- ブロック [`00bac0e4`](#insn-00bac0e4) 範囲 `[['00bac0e4', '00bac0eb']]`
  - `CONDITIONAL_JUMP` [`00bac0e8`](#insn-00bac0e8) → [`00bac0dc`](#insn-00bac0dc)
  - `FALL_THROUGH` [`00bac0e8`](#insn-00bac0e8) → [`00bac0ec`](#insn-00bac0ec)
- ブロック [`00bac0ec`](#insn-00bac0ec) 範囲 `[['00bac0ec', '00bac0fb']]`
  - `CONDITIONAL_JUMP` [`00bac0f8`](#insn-00bac0f8) → [`00bac2e8`](#insn-00bac2e8)
  - `FALL_THROUGH` [`00bac0f8`](#insn-00bac0f8) → [`00bac0fc`](#insn-00bac0fc)
- ブロック [`00bac0fc`](#insn-00bac0fc) 範囲 `[['00bac0fc', '00bac107']]`
  - `UNCONDITIONAL_JUMP` [`00bac104`](#insn-00bac104) → [`00bac120`](#insn-00bac120)
- ブロック [`00bac108`](#insn-00bac108) 範囲 `[['00bac108', '00bac10f']]`
  - `FALL_THROUGH` [`00bac10c`](#insn-00bac10c) → [`00bac110`](#insn-00bac110)
- ブロック [`00bac110`](#insn-00bac110) 範囲 `[['00bac110', '00bac113']]`
  - `CONDITIONAL_JUMP` [`00bac110`](#insn-00bac110) → [`00bac18c`](#insn-00bac18c)
  - `FALL_THROUGH` [`00bac110`](#insn-00bac110) → [`00bac114`](#insn-00bac114)
- ブロック [`00bac114`](#insn-00bac114) 範囲 `[['00bac114', '00bac117']]`
  - `FALL_THROUGH` [`00bac114`](#insn-00bac114) → [`00bac118`](#insn-00bac118)
- ブロック [`00bac118`](#insn-00bac118) 範囲 `[['00bac118', '00bac11f']]`
  - `CONDITIONAL_JUMP` [`00bac11c`](#insn-00bac11c) → [`00bac2e8`](#insn-00bac2e8)
  - `FALL_THROUGH` [`00bac11c`](#insn-00bac11c) → [`00bac120`](#insn-00bac120)
- ブロック [`00bac120`](#insn-00bac120) 範囲 `[['00bac120', '00bac12f']]`
  - `CONDITIONAL_JUMP` [`00bac12c`](#insn-00bac12c) → [`00bac110`](#insn-00bac110)
  - `FALL_THROUGH` [`00bac12c`](#insn-00bac12c) → [`00bac130`](#insn-00bac130)
- ブロック [`00bac130`](#insn-00bac130) 範囲 `[['00bac130', '00bac13b']]`
  - `FALL_THROUGH` [`00bac138`](#insn-00bac138) → [`00bac13c`](#insn-00bac13c)
- ブロック [`00bac13c`](#insn-00bac13c) 範囲 `[['00bac13c', '00bac143']]`
  - `FALL_THROUGH` [`00bac140`](#insn-00bac140) → [`00bac144`](#insn-00bac144)
- ブロック [`00bac144`](#insn-00bac144) 範囲 `[['00bac144', '00bac157']]`
  - `FALL_THROUGH` [`00bac154`](#insn-00bac154) → [`00bac158`](#insn-00bac158)
- ブロック [`00bac158`](#insn-00bac158) 範囲 `[['00bac158', '00bac15b']]`
  - `FALL_THROUGH` [`00bac158`](#insn-00bac158) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac15c`](#insn-00bac15c) 範囲 `[['00bac15c', '00bac15f']]`
  - `FALL_THROUGH` [`00bac15c`](#insn-00bac15c) → [`00bac160`](#insn-00bac160)
- ブロック [`00bac160`](#insn-00bac160) 範囲 `[['00bac160', '00bac163']]`
  - `CONDITIONAL_JUMP` [`00bac160`](#insn-00bac160) → [`00bac108`](#insn-00bac108)
  - `FALL_THROUGH` [`00bac160`](#insn-00bac160) → [`00bac164`](#insn-00bac164)
- ブロック [`00bac164`](#insn-00bac164) 範囲 `[['00bac164', '00bac173']]`
  - `FALL_THROUGH` [`00bac170`](#insn-00bac170) → [`00bac174`](#insn-00bac174)
- ブロック [`00bac174`](#insn-00bac174) 範囲 `[['00bac174', '00bac177']]`
  - `FALL_THROUGH` [`00bac174`](#insn-00bac174) → [`00bac178`](#insn-00bac178)
- ブロック [`00bac178`](#insn-00bac178) 範囲 `[['00bac178', '00bac183']]`
  - `CONDITIONAL_JUMP` [`00bac180`](#insn-00bac180) → [`00bac108`](#insn-00bac108)
  - `FALL_THROUGH` [`00bac180`](#insn-00bac180) → [`00bac184`](#insn-00bac184)
- ブロック [`00bac184`](#insn-00bac184) 範囲 `[['00bac184', '00bac18b']]`
  - `CONDITIONAL_JUMP` [`00bac188`](#insn-00bac188) → [`00bac114`](#insn-00bac114)
  - `FALL_THROUGH` [`00bac188`](#insn-00bac188) → [`00bac18c`](#insn-00bac18c)
- ブロック [`00bac18c`](#insn-00bac18c) 範囲 `[['00bac18c', '00bac197']]`
  - `FALL_THROUGH` [`00bac194`](#insn-00bac194) → [`00bac198`](#insn-00bac198)
- ブロック [`00bac198`](#insn-00bac198) 範囲 `[['00bac198', '00bac19b']]`
  - `FALL_THROUGH` [`00bac198`](#insn-00bac198) → [`00bac19c`](#insn-00bac19c)
- ブロック [`00bac19c`](#insn-00bac19c) 範囲 `[['00bac19c', '00bac1ab']]`
  - `CONDITIONAL_JUMP` [`00bac1a8`](#insn-00bac1a8) → [`00bac364`](#insn-00bac364)
  - `FALL_THROUGH` [`00bac1a8`](#insn-00bac1a8) → [`00bac1ac`](#insn-00bac1ac)
- ブロック [`00bac1ac`](#insn-00bac1ac) 範囲 `[['00bac1ac', '00bac1af']]`
  - `FALL_THROUGH` [`00bac1ac`](#insn-00bac1ac) → [`00bac1b0`](#insn-00bac1b0)
- ブロック [`00bac1b0`](#insn-00bac1b0) 範囲 `[['00bac1b0', '00bac1b3']]`
  - `FALL_THROUGH` [`00bac1b0`](#insn-00bac1b0) → [`00bac1b4`](#insn-00bac1b4)
- ブロック [`00bac1b4`](#insn-00bac1b4) 範囲 `[['00bac1b4', '00bac1c3']]`
  - `UNCONDITIONAL_JUMP` [`00bac1c0`](#insn-00bac1c0) → [`00bac1cc`](#insn-00bac1cc)
- ブロック [`00bac1c4`](#insn-00bac1c4) 範囲 `[['00bac1c4', '00bac1c7']]`
  - `CONDITIONAL_JUMP` [`00bac1c4`](#insn-00bac1c4) → [`00bac248`](#insn-00bac248)
  - `FALL_THROUGH` [`00bac1c4`](#insn-00bac1c4) → [`00bac1c8`](#insn-00bac1c8)
- ブロック [`00bac1c8`](#insn-00bac1c8) 範囲 `[['00bac1c8', '00bac1cb']]`
  - `FALL_THROUGH` [`00bac1c8`](#insn-00bac1c8) → [`00bac1cc`](#insn-00bac1cc)
- ブロック [`00bac1cc`](#insn-00bac1cc) 範囲 `[['00bac1cc', '00bac1db']]`
  - `CONDITIONAL_JUMP` [`00bac1d8`](#insn-00bac1d8) → [`00bac1c4`](#insn-00bac1c4)
  - `FALL_THROUGH` [`00bac1d8`](#insn-00bac1d8) → [`00bac1dc`](#insn-00bac1dc)
- ブロック [`00bac1dc`](#insn-00bac1dc) 範囲 `[['00bac1dc', '00bac1e3']]`
  - `FALL_THROUGH` [`00bac1e0`](#insn-00bac1e0) → [`00bac1e4`](#insn-00bac1e4)
- ブロック [`00bac1e4`](#insn-00bac1e4) 範囲 `[['00bac1e4', '00bac1e7']]`
  - `FALL_THROUGH` [`00bac1e4`](#insn-00bac1e4) → [`00bac1e8`](#insn-00bac1e8)
- ブロック [`00bac1e8`](#insn-00bac1e8) 範囲 `[['00bac1e8', '00bac1eb']]`
  - `FALL_THROUGH` [`00bac1e8`](#insn-00bac1e8) → [`00bac1ec`](#insn-00bac1ec)
- ブロック [`00bac1ec`](#insn-00bac1ec) 範囲 `[['00bac1ec', '00bac1ef']]`
  - `FALL_THROUGH` [`00bac1ec`](#insn-00bac1ec) → [`00bac1f0`](#insn-00bac1f0)
- ブロック [`00bac1f0`](#insn-00bac1f0) 範囲 `[['00bac1f0', '00bac1f7']]`
  - `FALL_THROUGH` [`00bac1f4`](#insn-00bac1f4) → [`00bac1f8`](#insn-00bac1f8)
- ブロック [`00bac1f8`](#insn-00bac1f8) 範囲 `[['00bac1f8', '00bac20f']]`
  - `CONDITIONAL_JUMP` [`00bac20c`](#insn-00bac20c) → [`00bac238`](#insn-00bac238)
  - `FALL_THROUGH` [`00bac20c`](#insn-00bac20c) → [`00bac210`](#insn-00bac210)
- ブロック [`00bac210`](#insn-00bac210) 範囲 `[['00bac210', '00bac22f']]`
  - `CONDITIONAL_JUMP` [`00bac22c`](#insn-00bac22c) → [`00bac238`](#insn-00bac238)
  - `FALL_THROUGH` [`00bac22c`](#insn-00bac22c) → [`00bac230`](#insn-00bac230)
- ブロック [`00bac230`](#insn-00bac230) 範囲 `[['00bac230', '00bac233']]`
  - `CONDITIONAL_JUMP` [`00bac230`](#insn-00bac230) → [`00bac1c8`](#insn-00bac1c8)
  - `FALL_THROUGH` [`00bac230`](#insn-00bac230) → [`00bac234`](#insn-00bac234)
- ブロック [`00bac234`](#insn-00bac234) 範囲 `[['00bac234', '00bac237']]`
  - `UNCONDITIONAL_JUMP` [`00bac234`](#insn-00bac234) → [`00bac248`](#insn-00bac248)
- ブロック [`00bac238`](#insn-00bac238) 範囲 `[['00bac238', '00bac23f']]`
  - `CONDITIONAL_JUMP` [`00bac23c`](#insn-00bac23c) → [`00bac1c8`](#insn-00bac1c8)
  - `FALL_THROUGH` [`00bac23c`](#insn-00bac23c) → [`00bac240`](#insn-00bac240)
- ブロック [`00bac240`](#insn-00bac240) 範囲 `[['00bac240', '00bac243']]`
  - `UNCONDITIONAL_JUMP` [`00bac240`](#insn-00bac240) → [`00bac248`](#insn-00bac248)
- ブロック [`00bac244`](#insn-00bac244) 範囲 `[['00bac244', '00bac247']]`
  - `CONDITIONAL_JUMP` [`00bac244`](#insn-00bac244) → [`00bac2bc`](#insn-00bac2bc)
  - `FALL_THROUGH` [`00bac244`](#insn-00bac244) → [`00bac248`](#insn-00bac248)
- ブロック [`00bac248`](#insn-00bac248) 範囲 `[['00bac248', '00bac257']]`
  - `CONDITIONAL_JUMP` [`00bac254`](#insn-00bac254) → [`00bac244`](#insn-00bac244)
  - `FALL_THROUGH` [`00bac254`](#insn-00bac254) → [`00bac258`](#insn-00bac258)
- ブロック [`00bac258`](#insn-00bac258) 範囲 `[['00bac258', '00bac267']]`
  - `FALL_THROUGH` [`00bac264`](#insn-00bac264) → [`00bac268`](#insn-00bac268)
- ブロック [`00bac268`](#insn-00bac268) 範囲 `[['00bac268', '00bac28b']]`
  - `CONDITIONAL_JUMP` [`00bac288`](#insn-00bac288) → [`00bac2b4`](#insn-00bac2b4)
  - `FALL_THROUGH` [`00bac288`](#insn-00bac288) → [`00bac28c`](#insn-00bac28c)
- ブロック [`00bac28c`](#insn-00bac28c) 範囲 `[['00bac28c', '00bac2ab']]`
  - `CONDITIONAL_JUMP` [`00bac2a8`](#insn-00bac2a8) → [`00bac2b4`](#insn-00bac2b4)
  - `FALL_THROUGH` [`00bac2a8`](#insn-00bac2a8) → [`00bac2ac`](#insn-00bac2ac)
- ブロック [`00bac2ac`](#insn-00bac2ac) 範囲 `[['00bac2ac', '00bac2af']]`
  - `CONDITIONAL_JUMP` [`00bac2ac`](#insn-00bac2ac) → [`00bac248`](#insn-00bac248)
  - `FALL_THROUGH` [`00bac2ac`](#insn-00bac2ac) → [`00bac2b0`](#insn-00bac2b0)
- ブロック [`00bac2b0`](#insn-00bac2b0) 範囲 `[['00bac2b0', '00bac2b3']]`
  - `UNCONDITIONAL_JUMP` [`00bac2b0`](#insn-00bac2b0) → [`00bac2bc`](#insn-00bac2bc)
- ブロック [`00bac2b4`](#insn-00bac2b4) 範囲 `[['00bac2b4', '00bac2bb']]`
  - `CONDITIONAL_JUMP` [`00bac2b8`](#insn-00bac2b8) → [`00bac248`](#insn-00bac248)
  - `FALL_THROUGH` [`00bac2b8`](#insn-00bac2b8) → [`00bac2bc`](#insn-00bac2bc)
- ブロック [`00bac2bc`](#insn-00bac2bc) 範囲 `[['00bac2bc', '00bac2c3']]`
  - `CONDITIONAL_JUMP` [`00bac2c0`](#insn-00bac2c0) → [`00bac374`](#insn-00bac374)
  - `FALL_THROUGH` [`00bac2c0`](#insn-00bac2c0) → [`00bac2c4`](#insn-00bac2c4)
- ブロック [`00bac2c4`](#insn-00bac2c4) 範囲 `[['00bac2c4', '00bac2d3']]`
  - `FALL_THROUGH` [`00bac2d0`](#insn-00bac2d0) → [`00bac2d4`](#insn-00bac2d4)
- ブロック [`00bac2d4`](#insn-00bac2d4) 範囲 `[['00bac2d4', '00bac2e7']]`
  - `UNCONDITIONAL_JUMP` [`00bac2e4`](#insn-00bac2e4) → [`00bac1b0`](#insn-00bac1b0)
- ブロック [`00bac2e8`](#insn-00bac2e8) 範囲 `[['00bac2e8', '00bac303']]`
  - `CONDITIONAL_JUMP` [`00bac300`](#insn-00bac300) → [`00bac460`](#insn-00bac460)
  - `FALL_THROUGH` [`00bac300`](#insn-00bac300) → [`00bac304`](#insn-00bac304)
- ブロック [`00bac304`](#insn-00bac304) 範囲 `[['00bac304', '00bac323']]`
  - `FALL_THROUGH` [`00bac320`](#insn-00bac320) → [`00bac324`](#insn-00bac324)
- ブロック [`00bac324`](#insn-00bac324) 範囲 `[['00bac324', '00bac33b']]`
  - `CONDITIONAL_JUMP` [`00bac338`](#insn-00bac338) → [`00bac478`](#insn-00bac478)
  - `FALL_THROUGH` [`00bac338`](#insn-00bac338) → [`00bac33c`](#insn-00bac33c)
- ブロック [`00bac33c`](#insn-00bac33c) 範囲 `[['00bac33c', '00bac353']]`
  - `FALL_THROUGH` [`00bac350`](#insn-00bac350) → [`00bac354`](#insn-00bac354)
- ブロック [`00bac354`](#insn-00bac354) 範囲 `[['00bac354', '00bac35b']]`
  - `CONDITIONAL_JUMP` [`00bac358`](#insn-00bac358) → [`00bac478`](#insn-00bac478)
  - `FALL_THROUGH` [`00bac358`](#insn-00bac358) → [`00bac35c`](#insn-00bac35c)
- ブロック [`00bac35c`](#insn-00bac35c) 範囲 `[['00bac35c', '00bac35f']]`
  - `CONDITIONAL_JUMP` [`00bac35c`](#insn-00bac35c) → [`00bac480`](#insn-00bac480)
  - `FALL_THROUGH` [`00bac35c`](#insn-00bac35c) → [`00bac360`](#insn-00bac360)
- ブロック [`00bac360`](#insn-00bac360) 範囲 `[['00bac360', '00bac363']]`
  - `UNCONDITIONAL_JUMP` [`00bac360`](#insn-00bac360) → [`00bac520`](#insn-00bac520)
- ブロック [`00bac364`](#insn-00bac364) 範囲 `[['00bac364', '00bac36f']]`
  - `CONDITIONAL_JUMP` [`00bac36c`](#insn-00bac36c) → [`00bac38c`](#insn-00bac38c)
  - `FALL_THROUGH` [`00bac36c`](#insn-00bac36c) → [`00bac370`](#insn-00bac370)
- ブロック [`00bac370`](#insn-00bac370) 範囲 `[['00bac370', '00bac373']]`
  - `UNCONDITIONAL_JUMP` [`00bac370`](#insn-00bac370) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac374`](#insn-00bac374) 範囲 `[['00bac374', '00bac377']]`
  - `FALL_THROUGH` [`00bac374`](#insn-00bac374) → [`00bac378`](#insn-00bac378)
- ブロック [`00bac378`](#insn-00bac378) 範囲 `[['00bac378', '00bac38b']]`
  - `CONDITIONAL_JUMP` [`00bac388`](#insn-00bac388) → [`00bac410`](#insn-00bac410)
  - `FALL_THROUGH` [`00bac388`](#insn-00bac388) → [`00bac38c`](#insn-00bac38c)
- ブロック [`00bac38c`](#insn-00bac38c) 範囲 `[['00bac38c', '00bac3a3']]`
  - `CONDITIONAL_JUMP` [`00bac3a0`](#insn-00bac3a0) → [`00bac400`](#insn-00bac400)
  - `FALL_THROUGH` [`00bac3a0`](#insn-00bac3a0) → [`00bac3a4`](#insn-00bac3a4)
- ブロック [`00bac3a4`](#insn-00bac3a4) 範囲 `[['00bac3a4', '00bac3a7']]`
  - `FALL_THROUGH` [`00bac3a4`](#insn-00bac3a4) → [`00bac3a8`](#insn-00bac3a8)
- ブロック [`00bac3a8`](#insn-00bac3a8) 範囲 `[['00bac3a8', '00bac3c7']]`
  - `FALL_THROUGH` [`00bac3c4`](#insn-00bac3c4) → [`00bac3c8`](#insn-00bac3c8)
- ブロック [`00bac3c8`](#insn-00bac3c8) 範囲 `[['00bac3c8', '00bac3d3']]`
  - `FALL_THROUGH` [`00bac3d0`](#insn-00bac3d0) → [`00bac3d4`](#insn-00bac3d4)
- ブロック [`00bac3d4`](#insn-00bac3d4) 範囲 `[['00bac3d4', '00bac3d7']]`
  - `CONDITIONAL_JUMP` [`00bac3d4`](#insn-00bac3d4) → [`00bac46c`](#insn-00bac46c)
  - `FALL_THROUGH` [`00bac3d4`](#insn-00bac3d4) → [`00bac3d8`](#insn-00bac3d8)
- ブロック [`00bac3d8`](#insn-00bac3d8) 範囲 `[['00bac3d8', '00bac3f3']]`
  - `FALL_THROUGH` [`00bac3f0`](#insn-00bac3f0) → [`00bac3f4`](#insn-00bac3f4)
- ブロック [`00bac3f4`](#insn-00bac3f4) 範囲 `[['00bac3f4', '00bac3f7']]`
  - `CONDITIONAL_JUMP` [`00bac3f4`](#insn-00bac3f4) → [`00bac46c`](#insn-00bac46c)
  - `FALL_THROUGH` [`00bac3f4`](#insn-00bac3f4) → [`00bac3f8`](#insn-00bac3f8)
- ブロック [`00bac3f8`](#insn-00bac3f8) 範囲 `[['00bac3f8', '00bac3fb']]`
  - `CONDITIONAL_JUMP` [`00bac3f8`](#insn-00bac3f8) → [`00bac404`](#insn-00bac404)
  - `FALL_THROUGH` [`00bac3f8`](#insn-00bac3f8) → [`00bac3fc`](#insn-00bac3fc)
- ブロック [`00bac3fc`](#insn-00bac3fc) 範囲 `[['00bac3fc', '00bac3ff']]`
  - `UNCONDITIONAL_JUMP` [`00bac3fc`](#insn-00bac3fc) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac400`](#insn-00bac400) 範囲 `[['00bac400', '00bac403']]`
  - `CONDITIONAL_JUMP` [`00bac400`](#insn-00bac400) → [`00bac410`](#insn-00bac410)
  - `FALL_THROUGH` [`00bac400`](#insn-00bac400) → [`00bac404`](#insn-00bac404)
- ブロック [`00bac404`](#insn-00bac404) 範囲 `[['00bac404', '00bac40f']]`
  - `FALL_THROUGH` [`00bac40c`](#insn-00bac40c) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac410`](#insn-00bac410) 範囲 `[['00bac410', '00bac413']]`
  - `CONDITIONAL_JUMP` [`00bac410`](#insn-00bac410) → [`00bac43c`](#insn-00bac43c)
  - `FALL_THROUGH` [`00bac410`](#insn-00bac410) → [`00bac414`](#insn-00bac414)
- ブロック [`00bac414`](#insn-00bac414) 範囲 `[['00bac414', '00bac42b']]`
  - `FALL_THROUGH` [`00bac428`](#insn-00bac428) → [`00bac42c`](#insn-00bac42c)
- ブロック [`00bac42c`](#insn-00bac42c) 範囲 `[['00bac42c', '00bac437']]`
  - `CONDITIONAL_JUMP` [`00bac434`](#insn-00bac434) → [`00bac664`](#insn-00bac664)
  - `FALL_THROUGH` [`00bac434`](#insn-00bac434) → [`00bac438`](#insn-00bac438)
- ブロック [`00bac438`](#insn-00bac438) 範囲 `[['00bac438', '00bac43b']]`
  - `CONDITIONAL_JUMP` [`00bac438`](#insn-00bac438) → [`00babfd8`](#insn-00babfd8)
  - `FALL_THROUGH` [`00bac438`](#insn-00bac438) → [`00bac43c`](#insn-00bac43c)
- ブロック [`00bac43c`](#insn-00bac43c) 範囲 `[['00bac43c', '00bac44b']]`
  - `CONDITIONAL_JUMP` [`00bac448`](#insn-00bac448) → [`00bac650`](#insn-00bac650)
  - `FALL_THROUGH` [`00bac448`](#insn-00bac448) → [`00bac44c`](#insn-00bac44c)
- ブロック [`00bac44c`](#insn-00bac44c) 範囲 `[['00bac44c', '00bac453']]`
  - `FALL_THROUGH` [`00bac450`](#insn-00bac450) → [`00bac454`](#insn-00bac454)
- ブロック [`00bac454`](#insn-00bac454) 範囲 `[['00bac454', '00bac457']]`
  - `FALL_THROUGH` [`00bac454`](#insn-00bac454) → [`00bac458`](#insn-00bac458)
- ブロック [`00bac458`](#insn-00bac458) 範囲 `[['00bac458', '00bac45b']]`
  - `FALL_THROUGH` [`00bac458`](#insn-00bac458) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac45c`](#insn-00bac45c) 範囲 `[['00bac45c', '00bac45f']]`
  - `UNCONDITIONAL_JUMP` [`00bac45c`](#insn-00bac45c) → [`00babfd8`](#insn-00babfd8)
- ブロック [`00bac460`](#insn-00bac460) 範囲 `[['00bac460', '00bac463']]`
  - `FALL_THROUGH` [`00bac460`](#insn-00bac460) → [`00bac464`](#insn-00bac464)
- ブロック [`00bac464`](#insn-00bac464) 範囲 `[['00bac464', '00bac467']]`
  - `CONDITIONAL_JUMP` [`00bac464`](#insn-00bac464) → [`00bac480`](#insn-00bac480)
  - `FALL_THROUGH` [`00bac464`](#insn-00bac464) → [`00bac468`](#insn-00bac468)
- ブロック [`00bac468`](#insn-00bac468) 範囲 `[['00bac468', '00bac46b']]`
  - `UNCONDITIONAL_JUMP` [`00bac468`](#insn-00bac468) → [`00bac520`](#insn-00bac520)
- ブロック [`00bac46c`](#insn-00bac46c) 範囲 `[['00bac46c', '00bac473']]`
  - `CONDITIONAL_JUMP` [`00bac470`](#insn-00bac470) → [`00bac404`](#insn-00bac404)
  - `FALL_THROUGH` [`00bac470`](#insn-00bac470) → [`00bac474`](#insn-00bac474)
- ブロック [`00bac474`](#insn-00bac474) 範囲 `[['00bac474', '00bac477']]`
  - `UNCONDITIONAL_JUMP` [`00bac474`](#insn-00bac474) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac478`](#insn-00bac478) 範囲 `[['00bac478', '00bac47f']]`
  - `CONDITIONAL_JUMP` [`00bac47c`](#insn-00bac47c) → [`00bac520`](#insn-00bac520)
  - `FALL_THROUGH` [`00bac47c`](#insn-00bac47c) → [`00bac480`](#insn-00bac480)
- ブロック [`00bac480`](#insn-00bac480) 範囲 `[['00bac480', '00bac48b']]`
  - `CONDITIONAL_JUMP` [`00bac488`](#insn-00bac488) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac488`](#insn-00bac488) → [`00bac48c`](#insn-00bac48c)
- ブロック [`00bac48c`](#insn-00bac48c) 範囲 `[['00bac48c', '00bac48f']]`
  - `FALL_THROUGH` [`00bac48c`](#insn-00bac48c) → [`00bac490`](#insn-00bac490)
- ブロック [`00bac490`](#insn-00bac490) 範囲 `[['00bac490', '00bac493']]`
  - `FALL_THROUGH` [`00bac490`](#insn-00bac490) → [`00bac494`](#insn-00bac494)
- ブロック [`00bac494`](#insn-00bac494) 範囲 `[['00bac494', '00bac497']]`
  - `UNCONDITIONAL_JUMP` [`00bac494`](#insn-00bac494) → [`00bac4ac`](#insn-00bac4ac)
- ブロック [`00bac498`](#insn-00bac498) 範囲 `[['00bac498', '00bac49b']]`
  - `FALL_THROUGH` [`00bac498`](#insn-00bac498) → [`00bac49c`](#insn-00bac49c)
- ブロック [`00bac49c`](#insn-00bac49c) 範囲 `[['00bac49c', '00bac49f']]`
  - `CONDITIONAL_JUMP` [`00bac49c`](#insn-00bac49c) → [`00bac514`](#insn-00bac514)
  - `FALL_THROUGH` [`00bac49c`](#insn-00bac49c) → [`00bac4a0`](#insn-00bac4a0)
- ブロック [`00bac4a0`](#insn-00bac4a0) 範囲 `[['00bac4a0', '00bac4a3']]`
  - `FALL_THROUGH` [`00bac4a0`](#insn-00bac4a0) → [`00bac4a4`](#insn-00bac4a4)
- ブロック [`00bac4a4`](#insn-00bac4a4) 範囲 `[['00bac4a4', '00bac4ab']]`
  - `CONDITIONAL_JUMP` [`00bac4a8`](#insn-00bac4a8) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac4a8`](#insn-00bac4a8) → [`00bac4ac`](#insn-00bac4ac)
- ブロック [`00bac4ac`](#insn-00bac4ac) 範囲 `[['00bac4ac', '00bac4bb']]`
  - `CONDITIONAL_JUMP` [`00bac4b8`](#insn-00bac4b8) → [`00bac49c`](#insn-00bac49c)
  - `FALL_THROUGH` [`00bac4b8`](#insn-00bac4b8) → [`00bac4bc`](#insn-00bac4bc)
- ブロック [`00bac4bc`](#insn-00bac4bc) 範囲 `[['00bac4bc', '00bac4e7']]`
  - `FALL_THROUGH` [`00bac4e4`](#insn-00bac4e4) → [`00bac4e8`](#insn-00bac4e8)
- ブロック [`00bac4e8`](#insn-00bac4e8) 範囲 `[['00bac4e8', '00bac4eb']]`
  - `FALL_THROUGH` [`00bac4e8`](#insn-00bac4e8) → [`00bac4ec`](#insn-00bac4ec)
- ブロック [`00bac4ec`](#insn-00bac4ec) 範囲 `[['00bac4ec', '00bac4ef']]`
  - `CONDITIONAL_JUMP` [`00bac4ec`](#insn-00bac4ec) → [`00bac498`](#insn-00bac498)
  - `FALL_THROUGH` [`00bac4ec`](#insn-00bac4ec) → [`00bac4f0`](#insn-00bac4f0)
- ブロック [`00bac4f0`](#insn-00bac4f0) 範囲 `[['00bac4f0', '00bac50f']]`
  - `CONDITIONAL_JUMP` [`00bac50c`](#insn-00bac50c) → [`00bac498`](#insn-00bac498)
  - `FALL_THROUGH` [`00bac50c`](#insn-00bac50c) → [`00bac510`](#insn-00bac510)
- ブロック [`00bac510`](#insn-00bac510) 範囲 `[['00bac510', '00bac513']]`
  - `CONDITIONAL_JUMP` [`00bac510`](#insn-00bac510) → [`00bac4a0`](#insn-00bac4a0)
  - `FALL_THROUGH` [`00bac510`](#insn-00bac510) → [`00bac514`](#insn-00bac514)
- ブロック [`00bac514`](#insn-00bac514) 範囲 `[['00bac514', '00bac51f']]`
  - `FALL_THROUGH` [`00bac51c`](#insn-00bac51c) → [`00bac520`](#insn-00bac520)
- ブロック [`00bac520`](#insn-00bac520) 範囲 `[['00bac520', '00bac52b']]`
  - `CONDITIONAL_JUMP` [`00bac528`](#insn-00bac528) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac528`](#insn-00bac528) → [`00bac52c`](#insn-00bac52c)
- ブロック [`00bac52c`](#insn-00bac52c) 範囲 `[['00bac52c', '00bac52f']]`
  - `FALL_THROUGH` [`00bac52c`](#insn-00bac52c) → [`00bac530`](#insn-00bac530)
- ブロック [`00bac530`](#insn-00bac530) 範囲 `[['00bac530', '00bac533']]`
  - `FALL_THROUGH` [`00bac530`](#insn-00bac530) → [`00bac534`](#insn-00bac534)
- ブロック [`00bac534`](#insn-00bac534) 範囲 `[['00bac534', '00bac53f']]`
  - `UNCONDITIONAL_JUMP` [`00bac53c`](#insn-00bac53c) → [`00bac548`](#insn-00bac548)
- ブロック [`00bac540`](#insn-00bac540) 範囲 `[['00bac540', '00bac543']]`
  - `CONDITIONAL_JUMP` [`00bac540`](#insn-00bac540) → [`00bac5c4`](#insn-00bac5c4)
  - `FALL_THROUGH` [`00bac540`](#insn-00bac540) → [`00bac544`](#insn-00bac544)
- ブロック [`00bac544`](#insn-00bac544) 範囲 `[['00bac544', '00bac547']]`
  - `FALL_THROUGH` [`00bac544`](#insn-00bac544) → [`00bac548`](#insn-00bac548)
- ブロック [`00bac548`](#insn-00bac548) 範囲 `[['00bac548', '00bac557']]`
  - `CONDITIONAL_JUMP` [`00bac554`](#insn-00bac554) → [`00bac540`](#insn-00bac540)
  - `FALL_THROUGH` [`00bac554`](#insn-00bac554) → [`00bac558`](#insn-00bac558)
- ブロック [`00bac558`](#insn-00bac558) 範囲 `[['00bac558', '00bac587']]`
  - `FALL_THROUGH` [`00bac584`](#insn-00bac584) → [`00bac588`](#insn-00bac588)
- ブロック [`00bac588`](#insn-00bac588) 範囲 `[['00bac588', '00bac58b']]`
  - `CONDITIONAL_JUMP` [`00bac588`](#insn-00bac588) → [`00bac5b4`](#insn-00bac5b4)
  - `FALL_THROUGH` [`00bac588`](#insn-00bac588) → [`00bac58c`](#insn-00bac58c)
- ブロック [`00bac58c`](#insn-00bac58c) 範囲 `[['00bac58c', '00bac5a7']]`
  - `FALL_THROUGH` [`00bac5a4`](#insn-00bac5a4) → [`00bac5a8`](#insn-00bac5a8)
- ブロック [`00bac5a8`](#insn-00bac5a8) 範囲 `[['00bac5a8', '00bac5ab']]`
  - `CONDITIONAL_JUMP` [`00bac5a8`](#insn-00bac5a8) → [`00bac5b4`](#insn-00bac5b4)
  - `FALL_THROUGH` [`00bac5a8`](#insn-00bac5a8) → [`00bac5ac`](#insn-00bac5ac)
- ブロック [`00bac5ac`](#insn-00bac5ac) 範囲 `[['00bac5ac', '00bac5af']]`
  - `CONDITIONAL_JUMP` [`00bac5ac`](#insn-00bac5ac) → [`00bac544`](#insn-00bac544)
  - `FALL_THROUGH` [`00bac5ac`](#insn-00bac5ac) → [`00bac5b0`](#insn-00bac5b0)
- ブロック [`00bac5b0`](#insn-00bac5b0) 範囲 `[['00bac5b0', '00bac5b3']]`
  - `UNCONDITIONAL_JUMP` [`00bac5b0`](#insn-00bac5b0) → [`00bac5c4`](#insn-00bac5c4)
- ブロック [`00bac5b4`](#insn-00bac5b4) 範囲 `[['00bac5b4', '00bac5bb']]`
  - `CONDITIONAL_JUMP` [`00bac5b8`](#insn-00bac5b8) → [`00bac544`](#insn-00bac544)
  - `FALL_THROUGH` [`00bac5b8`](#insn-00bac5b8) → [`00bac5bc`](#insn-00bac5bc)
- ブロック [`00bac5bc`](#insn-00bac5bc) 範囲 `[['00bac5bc', '00bac5bf']]`
  - `UNCONDITIONAL_JUMP` [`00bac5bc`](#insn-00bac5bc) → [`00bac5c4`](#insn-00bac5c4)
- ブロック [`00bac5c0`](#insn-00bac5c0) 範囲 `[['00bac5c0', '00bac5c3']]`
  - `CONDITIONAL_JUMP` [`00bac5c0`](#insn-00bac5c0) → [`00bac638`](#insn-00bac638)
  - `FALL_THROUGH` [`00bac5c0`](#insn-00bac5c0) → [`00bac5c4`](#insn-00bac5c4)
- ブロック [`00bac5c4`](#insn-00bac5c4) 範囲 `[['00bac5c4', '00bac5d3']]`
  - `CONDITIONAL_JUMP` [`00bac5d0`](#insn-00bac5d0) → [`00bac5c0`](#insn-00bac5c0)
  - `FALL_THROUGH` [`00bac5d0`](#insn-00bac5d0) → [`00bac5d4`](#insn-00bac5d4)
- ブロック [`00bac5d4`](#insn-00bac5d4) 範囲 `[['00bac5d4', '00bac5d7']]`
  - `FALL_THROUGH` [`00bac5d4`](#insn-00bac5d4) → [`00bac5d8`](#insn-00bac5d8)
- ブロック [`00bac5d8`](#insn-00bac5d8) 範囲 `[['00bac5d8', '00bac5fb']]`
  - `FALL_THROUGH` [`00bac5f8`](#insn-00bac5f8) → [`00bac5fc`](#insn-00bac5fc)
- ブロック [`00bac5fc`](#insn-00bac5fc) 範囲 `[['00bac5fc', '00bac607']]`
  - `CONDITIONAL_JUMP` [`00bac604`](#insn-00bac604) → [`00bac630`](#insn-00bac630)
  - `FALL_THROUGH` [`00bac604`](#insn-00bac604) → [`00bac608`](#insn-00bac608)
- ブロック [`00bac608`](#insn-00bac608) 範囲 `[['00bac608', '00bac627']]`
  - `CONDITIONAL_JUMP` [`00bac624`](#insn-00bac624) → [`00bac630`](#insn-00bac630)
  - `FALL_THROUGH` [`00bac624`](#insn-00bac624) → [`00bac628`](#insn-00bac628)
- ブロック [`00bac628`](#insn-00bac628) 範囲 `[['00bac628', '00bac62b']]`
  - `CONDITIONAL_JUMP` [`00bac628`](#insn-00bac628) → [`00bac5c4`](#insn-00bac5c4)
  - `FALL_THROUGH` [`00bac628`](#insn-00bac628) → [`00bac62c`](#insn-00bac62c)
- ブロック [`00bac62c`](#insn-00bac62c) 範囲 `[['00bac62c', '00bac62f']]`
  - `UNCONDITIONAL_JUMP` [`00bac62c`](#insn-00bac62c) → [`00bac638`](#insn-00bac638)
- ブロック [`00bac630`](#insn-00bac630) 範囲 `[['00bac630', '00bac637']]`
  - `CONDITIONAL_JUMP` [`00bac634`](#insn-00bac634) → [`00bac5c4`](#insn-00bac5c4)
  - `FALL_THROUGH` [`00bac634`](#insn-00bac634) → [`00bac638`](#insn-00bac638)
- ブロック [`00bac638`](#insn-00bac638) 範囲 `[['00bac638', '00bac63f']]`
  - `CONDITIONAL_JUMP` [`00bac63c`](#insn-00bac63c) → [`00babfd8`](#insn-00babfd8)
  - `FALL_THROUGH` [`00bac63c`](#insn-00bac63c) → [`00bac640`](#insn-00bac640)
- ブロック [`00bac640`](#insn-00bac640) 範囲 `[['00bac640', '00bac64b']]`
  - `FALL_THROUGH` [`00bac648`](#insn-00bac648) → [`00bac64c`](#insn-00bac64c)
- ブロック [`00bac64c`](#insn-00bac64c) 範囲 `[['00bac64c', '00bac64f']]`
  - `UNCONDITIONAL_JUMP` [`00bac64c`](#insn-00bac64c) → [`00bac530`](#insn-00bac530)
- ブロック [`00bac650`](#insn-00bac650) 範囲 `[['00bac650', '00bac657']]`
  - `FALL_THROUGH` [`00bac654`](#insn-00bac654) → [`00bac658`](#insn-00bac658)
- ブロック [`00bac658`](#insn-00bac658) 範囲 `[['00bac658', '00bac663']]`
  - `UNCONDITIONAL_JUMP` [`00bac660`](#insn-00bac660) → [`00babfc4`](#insn-00babfc4)
- ブロック [`00bac664`](#insn-00bac664) 範囲 `[['00bac664', '00bac66b']]`
  - `CONDITIONAL_JUMP` [`00bac668`](#insn-00bac668) → [`00babfc4`](#insn-00babfc4)
  - `FALL_THROUGH` [`00bac668`](#insn-00bac668) → [`00bac66c`](#insn-00bac66c)
- ブロック [`00bac66c`](#insn-00bac66c) 範囲 `[['00bac66c', '00bac66f']]`
  - `UNCONDITIONAL_JUMP` [`00bac66c`](#insn-00bac66c) → [`00bac930`](#insn-00bac930)
- ブロック [`00bac670`](#insn-00bac670) 範囲 `[['00bac670', '00bac677']]`
  - `FALL_THROUGH` [`00bac674`](#insn-00bac674) → [`00bac678`](#insn-00bac678)
- ブロック [`00bac678`](#insn-00bac678) 範囲 `[['00bac678', '00bac683']]`
  - `FALL_THROUGH` [`00bac680`](#insn-00bac680) → [`00bac684`](#insn-00bac684)
- ブロック [`00bac684`](#insn-00bac684) 範囲 `[['00bac684', '00bac687']]`
  - `COMPUTED_JUMP` [`00bac684`](#insn-00bac684) → [`00bac930`](#insn-00bac930)
  - `COMPUTED_JUMP` [`00bac684`](#insn-00bac684) → [`00bac688`](#insn-00bac688)
  - `COMPUTED_JUMP` [`00bac684`](#insn-00bac684) → [`00bac890`](#insn-00bac890)
  - `COMPUTED_JUMP` [`00bac684`](#insn-00bac684) → [`00bac8bc`](#insn-00bac8bc)
  - `COMPUTED_JUMP` [`00bac684`](#insn-00bac684) → [`00bac8ec`](#insn-00bac8ec)
- ブロック [`00bac688`](#insn-00bac688) 範囲 `[['00bac688', '00bac69f']]`
  - `CONDITIONAL_JUMP` [`00bac69c`](#insn-00bac69c) → [`00bac924`](#insn-00bac924)
  - `FALL_THROUGH` [`00bac69c`](#insn-00bac69c) → [`00bac6a0`](#insn-00bac6a0)
- ブロック [`00bac6a0`](#insn-00bac6a0) 範囲 `[['00bac6a0', '00bac6af']]`
  - `FALL_THROUGH` [`00bac6ac`](#insn-00bac6ac) → [`00bac6b0`](#insn-00bac6b0)
- ブロック [`00bac6b0`](#insn-00bac6b0) 範囲 `[['00bac6b0', '00bac6d3']]`
  - `CONDITIONAL_JUMP` [`00bac6d0`](#insn-00bac6d0) → [`00bac920`](#insn-00bac920)
  - `FALL_THROUGH` [`00bac6d0`](#insn-00bac6d0) → [`00bac6d4`](#insn-00bac6d4)
- ブロック [`00bac6d4`](#insn-00bac6d4) 範囲 `[['00bac6d4', '00bac6d7']]`
  - `FALL_THROUGH` [`00bac6d4`](#insn-00bac6d4) → [`00bac6d8`](#insn-00bac6d8)
- ブロック [`00bac6d8`](#insn-00bac6d8) 範囲 `[['00bac6d8', '00bac6db']]`
  - `FALL_THROUGH` [`00bac6d8`](#insn-00bac6d8) → [`00bac6dc`](#insn-00bac6dc)
- ブロック [`00bac6dc`](#insn-00bac6dc) 範囲 `[['00bac6dc', '00bac6df']]`
  - `FALL_THROUGH` [`00bac6dc`](#insn-00bac6dc) → [`00bac6e0`](#insn-00bac6e0)
- ブロック [`00bac6e0`](#insn-00bac6e0) 範囲 `[['00bac6e0', '00bac6e3']]`
  - `FALL_THROUGH` [`00bac6e0`](#insn-00bac6e0) → [`00bac6e4`](#insn-00bac6e4)
- ブロック [`00bac6e4`](#insn-00bac6e4) 範囲 `[['00bac6e4', '00bac6e7']]`
  - `FALL_THROUGH` [`00bac6e4`](#insn-00bac6e4) → [`00bac6e8`](#insn-00bac6e8)
- ブロック [`00bac6e8`](#insn-00bac6e8) 範囲 `[['00bac6e8', '00bac6eb']]`
  - `FALL_THROUGH` [`00bac6e8`](#insn-00bac6e8) → [`00bac6ec`](#insn-00bac6ec)
- ブロック [`00bac6ec`](#insn-00bac6ec) 範囲 `[['00bac6ec', '00bac6f3']]`
  - `CONDITIONAL_JUMP` [`00bac6f0`](#insn-00bac6f0) → [`00bac920`](#insn-00bac920)
  - `FALL_THROUGH` [`00bac6f0`](#insn-00bac6f0) → [`00bac6f4`](#insn-00bac6f4)
- ブロック [`00bac6f4`](#insn-00bac6f4) 範囲 `[['00bac6f4', '00bac6f7']]`
  - `CONDITIONAL_JUMP` [`00bac6f4`](#insn-00bac6f4) → [`00bac928`](#insn-00bac928)
  - `FALL_THROUGH` [`00bac6f4`](#insn-00bac6f4) → [`00bac6f8`](#insn-00bac6f8)
- ブロック [`00bac6f8`](#insn-00bac6f8) 範囲 `[['00bac6f8', '00bac6fb']]`
  - `UNCONDITIONAL_JUMP` [`00bac6f8`](#insn-00bac6f8) → [`00bac930`](#insn-00bac930)
- ブロック [`00bac6fc`](#insn-00bac6fc) 範囲 `[['00bac6fc', '00bac713']]`
  - `FALL_THROUGH` [`00bac710`](#insn-00bac710) → [`00bac714`](#insn-00bac714)
- ブロック [`00bac714`](#insn-00bac714) 範囲 `[['00bac714', '00bac717']]`
  - `FALL_THROUGH` [`00bac714`](#insn-00bac714) → [`00bac718`](#insn-00bac718)
- ブロック [`00bac718`](#insn-00bac718) 範囲 `[['00bac718', '00bac71b']]`
  - `CONDITIONAL_JUMP` [`00bac718`](#insn-00bac718) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac718`](#insn-00bac718) → [`00bac71c`](#insn-00bac71c)
- ブロック [`00bac71c`](#insn-00bac71c) 範囲 `[['00bac71c', '00bac723']]`
  - `UNCONDITIONAL_JUMP` [`00bac720`](#insn-00bac720) → [`00bac740`](#insn-00bac740)
- ブロック [`00bac724`](#insn-00bac724) 範囲 `[['00bac724', '00bac727']]`
  - `FALL_THROUGH` [`00bac724`](#insn-00bac724) → [`00bac728`](#insn-00bac728)
- ブロック [`00bac728`](#insn-00bac728) 範囲 `[['00bac728', '00bac72b']]`
  - `FALL_THROUGH` [`00bac728`](#insn-00bac728) → [`00bac72c`](#insn-00bac72c)
- ブロック [`00bac72c`](#insn-00bac72c) 範囲 `[['00bac72c', '00bac72f']]`
  - `FALL_THROUGH` [`00bac72c`](#insn-00bac72c) → [`00bac730`](#insn-00bac730)
- ブロック [`00bac730`](#insn-00bac730) 範囲 `[['00bac730', '00bac73f']]`
  - `CONDITIONAL_JUMP` [`00bac73c`](#insn-00bac73c) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac73c`](#insn-00bac73c) → [`00bac740`](#insn-00bac740)
- ブロック [`00bac740`](#insn-00bac740) 範囲 `[['00bac740', '00bac75f']]`
  - `CONDITIONAL_JUMP` [`00bac75c`](#insn-00bac75c) → [`00bac7bc`](#insn-00bac7bc)
  - `FALL_THROUGH` [`00bac75c`](#insn-00bac75c) → [`00bac760`](#insn-00bac760)
- ブロック [`00bac760`](#insn-00bac760) 範囲 `[['00bac760', '00bac76b']]`
  - `FALL_THROUGH` [`00bac768`](#insn-00bac768) → [`00bac76c`](#insn-00bac76c)
- ブロック [`00bac76c`](#insn-00bac76c) 範囲 `[['00bac76c', '00bac76f']]`
  - `FALL_THROUGH` [`00bac76c`](#insn-00bac76c) → [`00bac770`](#insn-00bac770)
- ブロック [`00bac770`](#insn-00bac770) 範囲 `[['00bac770', '00bac793']]`
  - `CONDITIONAL_JUMP` [`00bac790`](#insn-00bac790) → [`00bac7c4`](#insn-00bac7c4)
  - `FALL_THROUGH` [`00bac790`](#insn-00bac790) → [`00bac794`](#insn-00bac794)
- ブロック [`00bac794`](#insn-00bac794) 範囲 `[['00bac794', '00bac7b3']]`
  - `CONDITIONAL_JUMP` [`00bac7b0`](#insn-00bac7b0) → [`00bac7c4`](#insn-00bac7c4)
  - `FALL_THROUGH` [`00bac7b0`](#insn-00bac7b0) → [`00bac7b4`](#insn-00bac7b4)
- ブロック [`00bac7b4`](#insn-00bac7b4) 範囲 `[['00bac7b4', '00bac7b7']]`
  - `CONDITIONAL_JUMP` [`00bac7b4`](#insn-00bac7b4) → [`00bac730`](#insn-00bac730)
  - `FALL_THROUGH` [`00bac7b4`](#insn-00bac7b4) → [`00bac7b8`](#insn-00bac7b8)
- ブロック [`00bac7b8`](#insn-00bac7b8) 範囲 `[['00bac7b8', '00bac7bb']]`
  - `UNCONDITIONAL_JUMP` [`00bac7b8`](#insn-00bac7b8) → [`00bac7cc`](#insn-00bac7cc)
- ブロック [`00bac7bc`](#insn-00bac7bc) 範囲 `[['00bac7bc', '00bac7bf']]`
  - `CONDITIONAL_JUMP` [`00bac7bc`](#insn-00bac7bc) → [`00bac730`](#insn-00bac730)
  - `FALL_THROUGH` [`00bac7bc`](#insn-00bac7bc) → [`00bac7c0`](#insn-00bac7c0)
- ブロック [`00bac7c0`](#insn-00bac7c0) 範囲 `[['00bac7c0', '00bac7c3']]`
  - `UNCONDITIONAL_JUMP` [`00bac7c0`](#insn-00bac7c0) → [`00bac7cc`](#insn-00bac7cc)
- ブロック [`00bac7c4`](#insn-00bac7c4) 範囲 `[['00bac7c4', '00bac7cb']]`
  - `CONDITIONAL_JUMP` [`00bac7c8`](#insn-00bac7c8) → [`00bac730`](#insn-00bac730)
  - `FALL_THROUGH` [`00bac7c8`](#insn-00bac7c8) → [`00bac7cc`](#insn-00bac7cc)
- ブロック [`00bac7cc`](#insn-00bac7cc) 範囲 `[['00bac7cc', '00bac7d7']]`
  - `CONDITIONAL_JUMP` [`00bac7d4`](#insn-00bac7d4) → [`00bac72c`](#insn-00bac72c)
  - `FALL_THROUGH` [`00bac7d4`](#insn-00bac7d4) → [`00bac7d8`](#insn-00bac7d8)
- ブロック [`00bac7d8`](#insn-00bac7d8) 範囲 `[['00bac7d8', '00bac7db']]`
  - `FALL_THROUGH` [`00bac7d8`](#insn-00bac7d8) → [`00bac7dc`](#insn-00bac7dc)
- ブロック [`00bac7dc`](#insn-00bac7dc) 範囲 `[['00bac7dc', '00bac7e7']]`
  - `UNCONDITIONAL_JUMP` [`00bac7e4`](#insn-00bac7e4) → [`00bac800`](#insn-00bac800)
- ブロック [`00bac7e8`](#insn-00bac7e8) 範囲 `[['00bac7e8', '00bac7eb']]`
  - `CONDITIONAL_JUMP` [`00bac7e8`](#insn-00bac7e8) → [`00bac728`](#insn-00bac728)
  - `FALL_THROUGH` [`00bac7e8`](#insn-00bac7e8) → [`00bac7ec`](#insn-00bac7ec)
- ブロック [`00bac7ec`](#insn-00bac7ec) 範囲 `[['00bac7ec', '00bac7ff']]`
  - `CONDITIONAL_JUMP` [`00bac7fc`](#insn-00bac7fc) → [`00bac724`](#insn-00bac724)
  - `FALL_THROUGH` [`00bac7fc`](#insn-00bac7fc) → [`00bac800`](#insn-00bac800)
- ブロック [`00bac800`](#insn-00bac800) 範囲 `[['00bac800', '00bac80b']]`
  - `FALL_THROUGH` [`00bac808`](#insn-00bac808) → [`00bac80c`](#insn-00bac80c)
- ブロック [`00bac80c`](#insn-00bac80c) 範囲 `[['00bac80c', '00bac813']]`
  - `CONDITIONAL_JUMP` [`00bac810`](#insn-00bac810) → [`00bac7e8`](#insn-00bac7e8)
  - `FALL_THROUGH` [`00bac810`](#insn-00bac810) → [`00bac814`](#insn-00bac814)
- ブロック [`00bac814`](#insn-00bac814) 範囲 `[['00bac814', '00bac82b']]`
  - `FALL_THROUGH` [`00bac828`](#insn-00bac828) → [`00bac82c`](#insn-00bac82c)
- ブロック [`00bac82c`](#insn-00bac82c) 範囲 `[['00bac82c', '00bac847']]`
  - `CONDITIONAL_JUMP` [`00bac844`](#insn-00bac844) → [`00bac878`](#insn-00bac878)
  - `FALL_THROUGH` [`00bac844`](#insn-00bac844) → [`00bac848`](#insn-00bac848)
- ブロック [`00bac848`](#insn-00bac848) 範囲 `[['00bac848', '00bac85b']]`
  - `FALL_THROUGH` [`00bac858`](#insn-00bac858) → [`00bac85c`](#insn-00bac85c)
- ブロック [`00bac85c`](#insn-00bac85c) 範囲 `[['00bac85c', '00bac86b']]`
  - `CONDITIONAL_JUMP` [`00bac868`](#insn-00bac868) → [`00bac878`](#insn-00bac878)
  - `FALL_THROUGH` [`00bac868`](#insn-00bac868) → [`00bac86c`](#insn-00bac86c)
- ブロック [`00bac86c`](#insn-00bac86c) 範囲 `[['00bac86c', '00bac873']]`
  - `CONDITIONAL_JUMP` [`00bac870`](#insn-00bac870) → [`00bac7ec`](#insn-00bac7ec)
  - `FALL_THROUGH` [`00bac870`](#insn-00bac870) → [`00bac874`](#insn-00bac874)
- ブロック [`00bac874`](#insn-00bac874) 範囲 `[['00bac874', '00bac877']]`
  - `UNCONDITIONAL_JUMP` [`00bac874`](#insn-00bac874) → [`00bac728`](#insn-00bac728)
- ブロック [`00bac878`](#insn-00bac878) 範囲 `[['00bac878', '00bac87f']]`
  - `FALL_THROUGH` [`00bac87c`](#insn-00bac87c) → [`00bac880`](#insn-00bac880)
- ブロック [`00bac880`](#insn-00bac880) 範囲 `[['00bac880', '00bac883']]`
  - `CONDITIONAL_JUMP` [`00bac880`](#insn-00bac880) → [`00bac7ec`](#insn-00bac7ec)
  - `FALL_THROUGH` [`00bac880`](#insn-00bac880) → [`00bac884`](#insn-00bac884)
- ブロック [`00bac884`](#insn-00bac884) 範囲 `[['00bac884', '00bac88f']]`
  - `UNCONDITIONAL_JUMP` [`00bac88c`](#insn-00bac88c) → [`00bac728`](#insn-00bac728)
- ブロック [`00bac890`](#insn-00bac890) 範囲 `[['00bac890', '00bac8af']]`
  - `FALL_THROUGH` [`00bac8ac`](#insn-00bac8ac) → [`00bac8b0`](#insn-00bac8b0)
- ブロック [`00bac8b0`](#insn-00bac8b0) 範囲 `[['00bac8b0', '00bac8bb']]`
- ブロック [`00bac8bc`](#insn-00bac8bc) 範囲 `[['00bac8bc', '00bac8cf']]`
  - `FALL_THROUGH` [`00bac8cc`](#insn-00bac8cc) → [`00bac8d0`](#insn-00bac8d0)
- ブロック [`00bac8d0`](#insn-00bac8d0) 範囲 `[['00bac8d0', '00bac8db']]`
  - `FALL_THROUGH` [`00bac8d8`](#insn-00bac8d8) → [`00bac8dc`](#insn-00bac8dc)
- ブロック [`00bac8dc`](#insn-00bac8dc) 範囲 `[['00bac8dc', '00bac8eb']]`
- ブロック [`00bac8ec`](#insn-00bac8ec) 範囲 `[['00bac8ec', '00bac8fb']]`
  - `FALL_THROUGH` [`00bac8f8`](#insn-00bac8f8) → [`00bac8fc`](#insn-00bac8fc)
- ブロック [`00bac8fc`](#insn-00bac8fc) 範囲 `[['00bac8fc', '00bac91f']]`
- ブロック [`00bac920`](#insn-00bac920) 範囲 `[['00bac920', '00bac923']]`
  - `FALL_THROUGH` [`00bac920`](#insn-00bac920) → [`00bac924`](#insn-00bac924)
- ブロック [`00bac924`](#insn-00bac924) 範囲 `[['00bac924', '00bac927']]`
  - `CONDITIONAL_JUMP` [`00bac924`](#insn-00bac924) → [`00bac930`](#insn-00bac930)
  - `FALL_THROUGH` [`00bac924`](#insn-00bac924) → [`00bac928`](#insn-00bac928)
- ブロック [`00bac928`](#insn-00bac928) 範囲 `[['00bac928', '00bac92f']]`
  - `FALL_THROUGH` [`00bac92c`](#insn-00bac92c) → [`00bac930`](#insn-00bac930)
- ブロック [`00bac930`](#insn-00bac930) 範囲 `[['00bac930', '00bac933']]`
  - `FALL_THROUGH` [`00bac930`](#insn-00bac930) → [`00bac934`](#insn-00bac934)
- ブロック [`00bac934`](#insn-00bac934) 範囲 `[['00bac934', '00bac94f']]`

## 命令位置別の参照

- [`00babfa0`](#insn-00babfa0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfa4`](#insn-00babfa4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfa8`](#insn-00babfa8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfac`](#insn-00babfac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfb0`](#insn-00babfb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfb4`](#insn-00babfb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfc8`](#insn-00babfc8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfd4`](#insn-00babfd4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfe8`](#insn-00babfe8) → [`00bac670`](#insn-00bac670) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babff0`](#insn-00babff0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babff4`](#insn-00babff4) → [`00bac6fc`](#insn-00bac6fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac014`](#insn-00bac014) → [`00bac048`](#insn-00bac048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac024`](#insn-00bac024) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac040`](#insn-00bac040) → [`00bace04`](../00bac/00bace04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bace04` · 推定シンボル `None` · 推定型 `None`
- [`00bac044`](#insn-00bac044) → [`00bac058`](#insn-00bac058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac048`](#insn-00bac048) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac054`](#insn-00bac054) → [`00bac950`](../00bac/00bac950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac950` · 推定シンボル `None` · 推定型 `None`
- [`00bac078`](#insn-00bac078) → [`00bac0d8`](#insn-00bac0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0ac`](#insn-00bac0ac) → [`00bac0e4`](#insn-00bac0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0c8`](#insn-00bac0c8) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac0cc`](#insn-00bac0cc) → [`00bac0e4`](#insn-00bac0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0d0`](#insn-00bac0d0) → [`00bac0dc`](#insn-00bac0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0d4`](#insn-00bac0d4) → [`00bac0ec`](#insn-00bac0ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0d8`](#insn-00bac0d8) → [`00bac0ec`](#insn-00bac0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0dc`](#insn-00bac0dc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0e0`](#insn-00bac0e0) → [`00bac19c`](#insn-00bac19c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0e8`](#insn-00bac0e8) → [`00bac0dc`](#insn-00bac0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0ec`](#insn-00bac0ec) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0f0`](#insn-00bac0f0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0f8`](#insn-00bac0f8) → [`00bac2e8`](#insn-00bac2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0fc`](#insn-00bac0fc) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac104`](#insn-00bac104) → [`00bac120`](#insn-00bac120) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac10c`](#insn-00bac10c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac110`](#insn-00bac110) → [`00bac18c`](#insn-00bac18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac11c`](#insn-00bac11c) → [`00bac2e8`](#insn-00bac2e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac12c`](#insn-00bac12c) → [`00bac110`](#insn-00bac110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac160`](#insn-00bac160) → [`00bac108`](#insn-00bac108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac17c`](#insn-00bac17c) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac180`](#insn-00bac180) → [`00bac108`](#insn-00bac108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac184`](#insn-00bac184) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac188`](#insn-00bac188) → [`00bac114`](#insn-00bac114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac18c`](#insn-00bac18c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1a8`](#insn-00bac1a8) → [`00bac364`](#insn-00bac364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1ac`](#insn-00bac1ac) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1c0`](#insn-00bac1c0) → [`00bac1cc`](#insn-00bac1cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1c4`](#insn-00bac1c4) → [`00bac248`](#insn-00bac248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1d8`](#insn-00bac1d8) → [`00bac1c4`](#insn-00bac1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac20c`](#insn-00bac20c) → [`00bac238`](#insn-00bac238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac228`](#insn-00bac228) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac22c`](#insn-00bac22c) → [`00bac238`](#insn-00bac238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac230`](#insn-00bac230) → [`00bac1c8`](#insn-00bac1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac234`](#insn-00bac234) → [`00bac248`](#insn-00bac248) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac23c`](#insn-00bac23c) → [`00bac1c8`](#insn-00bac1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac240`](#insn-00bac240) → [`00bac248`](#insn-00bac248) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac244`](#insn-00bac244) → [`00bac2bc`](#insn-00bac2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac254`](#insn-00bac254) → [`00bac244`](#insn-00bac244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac288`](#insn-00bac288) → [`00bac2b4`](#insn-00bac2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a4`](#insn-00bac2a4) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a8`](#insn-00bac2a8) → [`00bac2b4`](#insn-00bac2b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2ac`](#insn-00bac2ac) → [`00bac248`](#insn-00bac248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2b0`](#insn-00bac2b0) → [`00bac2bc`](#insn-00bac2bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2b8`](#insn-00bac2b8) → [`00bac248`](#insn-00bac248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2c0`](#insn-00bac2c0) → [`00bac374`](#insn-00bac374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2c4`](#insn-00bac2c4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2dc`](#insn-00bac2dc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2e4`](#insn-00bac2e4) → [`00bac1b0`](#insn-00bac1b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2e8`](#insn-00bac2e8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac300`](#insn-00bac300) → [`00bac460`](#insn-00bac460) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac328`](#insn-00bac328) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac338`](#insn-00bac338) → [`00bac478`](#insn-00bac478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac354`](#insn-00bac354) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac358`](#insn-00bac358) → [`00bac478`](#insn-00bac478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac35c`](#insn-00bac35c) → [`00bac480`](#insn-00bac480) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac360`](#insn-00bac360) → [`00bac520`](#insn-00bac520) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac364`](#insn-00bac364) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac36c`](#insn-00bac36c) → [`00bac38c`](#insn-00bac38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac370`](#insn-00bac370) → [`00bac410`](#insn-00bac410) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac374`](#insn-00bac374) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac378`](#insn-00bac378) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac37c`](#insn-00bac37c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac388`](#insn-00bac388) → [`00bac410`](#insn-00bac410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3a0`](#insn-00bac3a0) → [`00bac400`](#insn-00bac400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3d4`](#insn-00bac3d4) → [`00bac46c`](#insn-00bac46c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3f0`](#insn-00bac3f0) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac3f4`](#insn-00bac3f4) → [`00bac46c`](#insn-00bac46c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3f8`](#insn-00bac3f8) → [`00bac404`](#insn-00bac404) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3fc`](#insn-00bac3fc) → [`00bac410`](#insn-00bac410) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac400`](#insn-00bac400) → [`00bac410`](#insn-00bac410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac410`](#insn-00bac410) → [`00bac43c`](#insn-00bac43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac41c`](#insn-00bac41c) → [`00bad0e4`](../00bad/00bad0e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad0e4` · 推定シンボル `None` · 推定型 `None`
- [`00bac430`](#insn-00bac430) → [`00bad0e4`](../00bad/00bad0e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad0e4` · 推定シンボル `None` · 推定型 `None`
- [`00bac434`](#insn-00bac434) → [`00bac664`](#insn-00bac664) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac438`](#insn-00bac438) → [`00babfd8`](#insn-00babfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac448`](#insn-00bac448) → [`00bac650`](#insn-00bac650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac454`](#insn-00bac454) → [`00babf9c`](#insn-00babf9c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babf9c` · 推定シンボル `None` · 推定型 `None`
- [`00bac45c`](#insn-00bac45c) → [`00babfd8`](#insn-00babfd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac460`](#insn-00bac460) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac464`](#insn-00bac464) → [`00bac480`](#insn-00bac480) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac468`](#insn-00bac468) → [`00bac520`](#insn-00bac520) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac470`](#insn-00bac470) → [`00bac404`](#insn-00bac404) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac474`](#insn-00bac474) → [`00bac410`](#insn-00bac410) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac47c`](#insn-00bac47c) → [`00bac520`](#insn-00bac520) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac480`](#insn-00bac480) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac488`](#insn-00bac488) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac494`](#insn-00bac494) → [`00bac4ac`](#insn-00bac4ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac49c`](#insn-00bac49c) → [`00bac514`](#insn-00bac514) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4a8`](#insn-00bac4a8) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac4b8`](#insn-00bac4b8) → [`00bac49c`](#insn-00bac49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4ec`](#insn-00bac4ec) → [`00bac498`](#insn-00bac498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac508`](#insn-00bac508) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac50c`](#insn-00bac50c) → [`00bac498`](#insn-00bac498) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac510`](#insn-00bac510) → [`00bac4a0`](#insn-00bac4a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac514`](#insn-00bac514) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac520`](#insn-00bac520) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac528`](#insn-00bac528) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac52c`](#insn-00bac52c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac53c`](#insn-00bac53c) → [`00bac548`](#insn-00bac548) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac540`](#insn-00bac540) → [`00bac5c4`](#insn-00bac5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac554`](#insn-00bac554) → [`00bac540`](#insn-00bac540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac588`](#insn-00bac588) → [`00bac5b4`](#insn-00bac5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5a4`](#insn-00bac5a4) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac5a8`](#insn-00bac5a8) → [`00bac5b4`](#insn-00bac5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5ac`](#insn-00bac5ac) → [`00bac544`](#insn-00bac544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5b0`](#insn-00bac5b0) → [`00bac5c4`](#insn-00bac5c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5b8`](#insn-00bac5b8) → [`00bac544`](#insn-00bac544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5bc`](#insn-00bac5bc) → [`00bac5c4`](#insn-00bac5c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5c0`](#insn-00bac5c0) → [`00bac638`](#insn-00bac638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5d0`](#insn-00bac5d0) → [`00bac5c0`](#insn-00bac5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac604`](#insn-00bac604) → [`00bac630`](#insn-00bac630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac620`](#insn-00bac620) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac624`](#insn-00bac624) → [`00bac630`](#insn-00bac630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac628`](#insn-00bac628) → [`00bac5c4`](#insn-00bac5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac62c`](#insn-00bac62c) → [`00bac638`](#insn-00bac638) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac634`](#insn-00bac634) → [`00bac5c4`](#insn-00bac5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac63c`](#insn-00bac63c) → [`00babfd8`](#insn-00babfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac640`](#insn-00bac640) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac64c`](#insn-00bac64c) → [`00bac530`](#insn-00bac530) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac658`](#insn-00bac658) → [`00babf9c`](#insn-00babf9c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00babf9c` · 推定シンボル `None` · 推定型 `None`
- [`00bac660`](#insn-00bac660) → [`00babfc4`](#insn-00babfc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac668`](#insn-00bac668) → [`00babfc4`](#insn-00babfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac66c`](#insn-00bac66c) → [`00bac930`](#insn-00bac930) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac67c`](#insn-00bac67c) → `0030e200`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::switchdataD_0030e200` · 推定型 `byte`
- [`00bac684`](#insn-00bac684) → [`00bac930`](#insn-00bac930) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac684`](#insn-00bac684) → [`00bac688`](#insn-00bac688) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_2` · 推定型 `None`
- [`00bac684`](#insn-00bac684) → [`00bac890`](#insn-00bac890) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_3` · 推定型 `None`
- [`00bac684`](#insn-00bac684) → [`00bac8bc`](#insn-00bac8bc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_4` · 推定型 `None`
- [`00bac684`](#insn-00bac684) → [`00bac8ec`](#insn-00bac8ec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_5` · 推定型 `None`
- [`00bac69c`](#insn-00bac69c) → [`00bac924`](#insn-00bac924) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6d0`](#insn-00bac6d0) → [`00bac920`](#insn-00bac920) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6ec`](#insn-00bac6ec) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac6f0`](#insn-00bac6f0) → [`00bac920`](#insn-00bac920) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6f4`](#insn-00bac6f4) → [`00bac928`](#insn-00bac928) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6f8`](#insn-00bac6f8) → [`00bac930`](#insn-00bac930) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac70c`](#insn-00bac70c) → [`00bac950`](../00bac/00bac950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac950` · 推定シンボル `None` · 推定型 `None`
- [`00bac718`](#insn-00bac718) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac720`](#insn-00bac720) → [`00bac740`](#insn-00bac740) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac728`](#insn-00bac728) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac73c`](#insn-00bac73c) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac75c`](#insn-00bac75c) → [`00bac7bc`](#insn-00bac7bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac790`](#insn-00bac790) → [`00bac7c4`](#insn-00bac7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7ac`](#insn-00bac7ac) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac7b0`](#insn-00bac7b0) → [`00bac7c4`](#insn-00bac7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7b4`](#insn-00bac7b4) → [`00bac730`](#insn-00bac730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7b8`](#insn-00bac7b8) → [`00bac7cc`](#insn-00bac7cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7bc`](#insn-00bac7bc) → [`00bac730`](#insn-00bac730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7c0`](#insn-00bac7c0) → [`00bac7cc`](#insn-00bac7cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7c8`](#insn-00bac7c8) → [`00bac730`](#insn-00bac730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7d4`](#insn-00bac7d4) → [`00bac72c`](#insn-00bac72c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7e0`](#insn-00bac7e0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7e4`](#insn-00bac7e4) → [`00bac800`](#insn-00bac800) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7e8`](#insn-00bac7e8) → [`00bac728`](#insn-00bac728) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7fc`](#insn-00bac7fc) → [`00bac724`](#insn-00bac724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac810`](#insn-00bac810) → [`00bac7e8`](#insn-00bac7e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac844`](#insn-00bac844) → [`00bac878`](#insn-00bac878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac850`](#insn-00bac850) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac864`](#insn-00bac864) → [`00c58050`](../00c58/00c58050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58050` · 推定シンボル `None` · 推定型 `None`
- [`00bac868`](#insn-00bac868) → [`00bac878`](#insn-00bac878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac86c`](#insn-00bac86c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac870`](#insn-00bac870) → [`00bac7ec`](#insn-00bac7ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac874`](#insn-00bac874) → [`00bac728`](#insn-00bac728) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac87c`](#insn-00bac87c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac880`](#insn-00bac880) → [`00bac7ec`](#insn-00bac7ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac88c`](#insn-00bac88c) → [`00bac728`](#insn-00bac728) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac898`](#insn-00bac898) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac89c`](#insn-00bac89c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8a0`](#insn-00bac8a0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8a4`](#insn-00bac8a4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8a8`](#insn-00bac8a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8ac`](#insn-00bac8ac) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8b0`](#insn-00bac8b0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8b8`](#insn-00bac8b8) → [`00bac950`](../00bac/00bac950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac950` · 推定シンボル `None` · 推定型 `None`
- [`00bac8c8`](#insn-00bac8c8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8cc`](#insn-00bac8cc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8d0`](#insn-00bac8d0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8d4`](#insn-00bac8d4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8d8`](#insn-00bac8d8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8dc`](#insn-00bac8dc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8e0`](#insn-00bac8e0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8e8`](#insn-00bac8e8) → [`00bacbfc`](../00bac/00bacbfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacbfc` · 推定シンボル `None` · 推定型 `None`
- [`00bac8fc`](#insn-00bac8fc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac900`](#insn-00bac900) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac904`](#insn-00bac904) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac908`](#insn-00bac908) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac90c`](#insn-00bac90c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac910`](#insn-00bac910) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac914`](#insn-00bac914) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac91c`](#insn-00bac91c) → [`00bace04`](../00bac/00bace04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bace04` · 推定シンボル `None` · 推定型 `None`
- [`00bac924`](#insn-00bac924) → [`00bac930`](#insn-00bac930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bac684::caseD_0` · 推定型 `None`
- [`00bac930`](#insn-00bac930) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac934`](#insn-00bac934) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac938`](#insn-00bac938) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac93c`](#insn-00bac93c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac940`](#insn-00bac940) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac944`](#insn-00bac944) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babfa0`](#insn-00babfa0)

~~~json
{
  "source": "00babfa0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfa4`](#insn-00babfa4)

~~~json
{
  "source": "00babfa4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfa8`](#insn-00babfa8)

~~~json
{
  "source": "00babfa8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfac`](#insn-00babfac)

~~~json
{
  "source": "00babfac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfb0`](#insn-00babfb0)

~~~json
{
  "source": "00babfb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfb4`](#insn-00babfb4)

~~~json
{
  "source": "00babfb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfc8`](#insn-00babfc8)

~~~json
{
  "source": "00babfc8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfd4`](#insn-00babfd4)

~~~json
{
  "source": "00babfd4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe8`](#insn-00babfe8)

~~~json
{
  "source": "00babfe8",
  "target": "00bac670",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babff0`](#insn-00babff0)

~~~json
{
  "source": "00babff0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babff4`](#insn-00babff4)

~~~json
{
  "source": "00babff4",
  "target": "00bac6fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac014`](#insn-00bac014)

~~~json
{
  "source": "00bac014",
  "target": "00bac048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac024`](#insn-00bac024)

~~~json
{
  "source": "00bac024",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac040`](#insn-00bac040)

~~~json
{
  "source": "00bac040",
  "target": "00bace04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac044`](#insn-00bac044)

~~~json
{
  "source": "00bac044",
  "target": "00bac058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac048`](#insn-00bac048)

~~~json
{
  "source": "00bac048",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac054`](#insn-00bac054)

~~~json
{
  "source": "00bac054",
  "target": "00bac950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac078`](#insn-00bac078)

~~~json
{
  "source": "00bac078",
  "target": "00bac0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0ac`](#insn-00bac0ac)

~~~json
{
  "source": "00bac0ac",
  "target": "00bac0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0c8`](#insn-00bac0c8)

~~~json
{
  "source": "00bac0c8",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac0cc`](#insn-00bac0cc)

~~~json
{
  "source": "00bac0cc",
  "target": "00bac0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0d0`](#insn-00bac0d0)

~~~json
{
  "source": "00bac0d0",
  "target": "00bac0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0d4`](#insn-00bac0d4)

~~~json
{
  "source": "00bac0d4",
  "target": "00bac0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0d8`](#insn-00bac0d8)

~~~json
{
  "source": "00bac0d8",
  "target": "00bac0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0dc`](#insn-00bac0dc)

~~~json
{
  "source": "00bac0dc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0e0`](#insn-00bac0e0)

~~~json
{
  "source": "00bac0e0",
  "target": "00bac19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0e8`](#insn-00bac0e8)

~~~json
{
  "source": "00bac0e8",
  "target": "00bac0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0ec`](#insn-00bac0ec)

~~~json
{
  "source": "00bac0ec",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0f0`](#insn-00bac0f0)

~~~json
{
  "source": "00bac0f0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0f8`](#insn-00bac0f8)

~~~json
{
  "source": "00bac0f8",
  "target": "00bac2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0fc`](#insn-00bac0fc)

~~~json
{
  "source": "00bac0fc",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac104`](#insn-00bac104)

~~~json
{
  "source": "00bac104",
  "target": "00bac120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac10c`](#insn-00bac10c)

~~~json
{
  "source": "00bac10c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac110`](#insn-00bac110)

~~~json
{
  "source": "00bac110",
  "target": "00bac18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac11c`](#insn-00bac11c)

~~~json
{
  "source": "00bac11c",
  "target": "00bac2e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac12c`](#insn-00bac12c)

~~~json
{
  "source": "00bac12c",
  "target": "00bac110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac160`](#insn-00bac160)

~~~json
{
  "source": "00bac160",
  "target": "00bac108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac17c`](#insn-00bac17c)

~~~json
{
  "source": "00bac17c",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac180`](#insn-00bac180)

~~~json
{
  "source": "00bac180",
  "target": "00bac108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac184`](#insn-00bac184)

~~~json
{
  "source": "00bac184",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac188`](#insn-00bac188)

~~~json
{
  "source": "00bac188",
  "target": "00bac114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac18c`](#insn-00bac18c)

~~~json
{
  "source": "00bac18c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1a8`](#insn-00bac1a8)

~~~json
{
  "source": "00bac1a8",
  "target": "00bac364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1ac`](#insn-00bac1ac)

~~~json
{
  "source": "00bac1ac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1c0`](#insn-00bac1c0)

~~~json
{
  "source": "00bac1c0",
  "target": "00bac1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1c4`](#insn-00bac1c4)

~~~json
{
  "source": "00bac1c4",
  "target": "00bac248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1d8`](#insn-00bac1d8)

~~~json
{
  "source": "00bac1d8",
  "target": "00bac1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac20c`](#insn-00bac20c)

~~~json
{
  "source": "00bac20c",
  "target": "00bac238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac228`](#insn-00bac228)

~~~json
{
  "source": "00bac228",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac22c`](#insn-00bac22c)

~~~json
{
  "source": "00bac22c",
  "target": "00bac238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac230`](#insn-00bac230)

~~~json
{
  "source": "00bac230",
  "target": "00bac1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac234`](#insn-00bac234)

~~~json
{
  "source": "00bac234",
  "target": "00bac248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac23c`](#insn-00bac23c)

~~~json
{
  "source": "00bac23c",
  "target": "00bac1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac240`](#insn-00bac240)

~~~json
{
  "source": "00bac240",
  "target": "00bac248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac244`](#insn-00bac244)

~~~json
{
  "source": "00bac244",
  "target": "00bac2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac254`](#insn-00bac254)

~~~json
{
  "source": "00bac254",
  "target": "00bac244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac288`](#insn-00bac288)

~~~json
{
  "source": "00bac288",
  "target": "00bac2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2a4`](#insn-00bac2a4)

~~~json
{
  "source": "00bac2a4",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac2a8`](#insn-00bac2a8)

~~~json
{
  "source": "00bac2a8",
  "target": "00bac2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2ac`](#insn-00bac2ac)

~~~json
{
  "source": "00bac2ac",
  "target": "00bac248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2b0`](#insn-00bac2b0)

~~~json
{
  "source": "00bac2b0",
  "target": "00bac2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2b8`](#insn-00bac2b8)

~~~json
{
  "source": "00bac2b8",
  "target": "00bac248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2c0`](#insn-00bac2c0)

~~~json
{
  "source": "00bac2c0",
  "target": "00bac374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2c4`](#insn-00bac2c4)

~~~json
{
  "source": "00bac2c4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2dc`](#insn-00bac2dc)

~~~json
{
  "source": "00bac2dc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2e4`](#insn-00bac2e4)

~~~json
{
  "source": "00bac2e4",
  "target": "00bac1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2e8`](#insn-00bac2e8)

~~~json
{
  "source": "00bac2e8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac300`](#insn-00bac300)

~~~json
{
  "source": "00bac300",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac328`](#insn-00bac328)

~~~json
{
  "source": "00bac328",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac338`](#insn-00bac338)

~~~json
{
  "source": "00bac338",
  "target": "00bac478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac354`](#insn-00bac354)

~~~json
{
  "source": "00bac354",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac358`](#insn-00bac358)

~~~json
{
  "source": "00bac358",
  "target": "00bac478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac35c`](#insn-00bac35c)

~~~json
{
  "source": "00bac35c",
  "target": "00bac480",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac360`](#insn-00bac360)

~~~json
{
  "source": "00bac360",
  "target": "00bac520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac364`](#insn-00bac364)

~~~json
{
  "source": "00bac364",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac36c`](#insn-00bac36c)

~~~json
{
  "source": "00bac36c",
  "target": "00bac38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac370`](#insn-00bac370)

~~~json
{
  "source": "00bac370",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac374`](#insn-00bac374)

~~~json
{
  "source": "00bac374",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac378`](#insn-00bac378)

~~~json
{
  "source": "00bac378",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac37c`](#insn-00bac37c)

~~~json
{
  "source": "00bac37c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac388`](#insn-00bac388)

~~~json
{
  "source": "00bac388",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3a0`](#insn-00bac3a0)

~~~json
{
  "source": "00bac3a0",
  "target": "00bac400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3d4`](#insn-00bac3d4)

~~~json
{
  "source": "00bac3d4",
  "target": "00bac46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3f0`](#insn-00bac3f0)

~~~json
{
  "source": "00bac3f0",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac3f4`](#insn-00bac3f4)

~~~json
{
  "source": "00bac3f4",
  "target": "00bac46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3f8`](#insn-00bac3f8)

~~~json
{
  "source": "00bac3f8",
  "target": "00bac404",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3fc`](#insn-00bac3fc)

~~~json
{
  "source": "00bac3fc",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac400`](#insn-00bac400)

~~~json
{
  "source": "00bac400",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac410`](#insn-00bac410)

~~~json
{
  "source": "00bac410",
  "target": "00bac43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac41c`](#insn-00bac41c)

~~~json
{
  "source": "00bac41c",
  "target": "00bad0e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac430`](#insn-00bac430)

~~~json
{
  "source": "00bac430",
  "target": "00bad0e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac434`](#insn-00bac434)

~~~json
{
  "source": "00bac434",
  "target": "00bac664",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac438`](#insn-00bac438)

~~~json
{
  "source": "00bac438",
  "target": "00babfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac448`](#insn-00bac448)

~~~json
{
  "source": "00bac448",
  "target": "00bac650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac454`](#insn-00bac454)

~~~json
{
  "source": "00bac454",
  "target": "00babf9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac45c`](#insn-00bac45c)

~~~json
{
  "source": "00bac45c",
  "target": "00babfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac460`](#insn-00bac460)

~~~json
{
  "source": "00bac460",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac464`](#insn-00bac464)

~~~json
{
  "source": "00bac464",
  "target": "00bac480",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac468`](#insn-00bac468)

~~~json
{
  "source": "00bac468",
  "target": "00bac520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac470`](#insn-00bac470)

~~~json
{
  "source": "00bac470",
  "target": "00bac404",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac474`](#insn-00bac474)

~~~json
{
  "source": "00bac474",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac47c`](#insn-00bac47c)

~~~json
{
  "source": "00bac47c",
  "target": "00bac520",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac480`](#insn-00bac480)

~~~json
{
  "source": "00bac480",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac488`](#insn-00bac488)

~~~json
{
  "source": "00bac488",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac494`](#insn-00bac494)

~~~json
{
  "source": "00bac494",
  "target": "00bac4ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac49c`](#insn-00bac49c)

~~~json
{
  "source": "00bac49c",
  "target": "00bac514",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4a8`](#insn-00bac4a8)

~~~json
{
  "source": "00bac4a8",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4b8`](#insn-00bac4b8)

~~~json
{
  "source": "00bac4b8",
  "target": "00bac49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4ec`](#insn-00bac4ec)

~~~json
{
  "source": "00bac4ec",
  "target": "00bac498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac508`](#insn-00bac508)

~~~json
{
  "source": "00bac508",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac50c`](#insn-00bac50c)

~~~json
{
  "source": "00bac50c",
  "target": "00bac498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac510`](#insn-00bac510)

~~~json
{
  "source": "00bac510",
  "target": "00bac4a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac514`](#insn-00bac514)

~~~json
{
  "source": "00bac514",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac520`](#insn-00bac520)

~~~json
{
  "source": "00bac520",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac528`](#insn-00bac528)

~~~json
{
  "source": "00bac528",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac52c`](#insn-00bac52c)

~~~json
{
  "source": "00bac52c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac53c`](#insn-00bac53c)

~~~json
{
  "source": "00bac53c",
  "target": "00bac548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac540`](#insn-00bac540)

~~~json
{
  "source": "00bac540",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac554`](#insn-00bac554)

~~~json
{
  "source": "00bac554",
  "target": "00bac540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac588`](#insn-00bac588)

~~~json
{
  "source": "00bac588",
  "target": "00bac5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5a4`](#insn-00bac5a4)

~~~json
{
  "source": "00bac5a4",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac5a8`](#insn-00bac5a8)

~~~json
{
  "source": "00bac5a8",
  "target": "00bac5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5ac`](#insn-00bac5ac)

~~~json
{
  "source": "00bac5ac",
  "target": "00bac544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5b0`](#insn-00bac5b0)

~~~json
{
  "source": "00bac5b0",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5b8`](#insn-00bac5b8)

~~~json
{
  "source": "00bac5b8",
  "target": "00bac544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5bc`](#insn-00bac5bc)

~~~json
{
  "source": "00bac5bc",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5c0`](#insn-00bac5c0)

~~~json
{
  "source": "00bac5c0",
  "target": "00bac638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5d0`](#insn-00bac5d0)

~~~json
{
  "source": "00bac5d0",
  "target": "00bac5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac604`](#insn-00bac604)

~~~json
{
  "source": "00bac604",
  "target": "00bac630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac620`](#insn-00bac620)

~~~json
{
  "source": "00bac620",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac624`](#insn-00bac624)

~~~json
{
  "source": "00bac624",
  "target": "00bac630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac628`](#insn-00bac628)

~~~json
{
  "source": "00bac628",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac62c`](#insn-00bac62c)

~~~json
{
  "source": "00bac62c",
  "target": "00bac638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac634`](#insn-00bac634)

~~~json
{
  "source": "00bac634",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac63c`](#insn-00bac63c)

~~~json
{
  "source": "00bac63c",
  "target": "00babfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac640`](#insn-00bac640)

~~~json
{
  "source": "00bac640",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac64c`](#insn-00bac64c)

~~~json
{
  "source": "00bac64c",
  "target": "00bac530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac658`](#insn-00bac658)

~~~json
{
  "source": "00bac658",
  "target": "00babf9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac660`](#insn-00bac660)

~~~json
{
  "source": "00bac660",
  "target": "00babfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac668`](#insn-00bac668)

~~~json
{
  "source": "00bac668",
  "target": "00babfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac66c`](#insn-00bac66c)

~~~json
{
  "source": "00bac66c",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac67c`](#insn-00bac67c)

~~~json
{
  "source": "00bac67c",
  "target": "0030e200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e200",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "aa",
  "capture_start": "0030e200",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00bac688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00bac890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00bac8bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00bac8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac69c`](#insn-00bac69c)

~~~json
{
  "source": "00bac69c",
  "target": "00bac924",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6d0`](#insn-00bac6d0)

~~~json
{
  "source": "00bac6d0",
  "target": "00bac920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6ec`](#insn-00bac6ec)

~~~json
{
  "source": "00bac6ec",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac6f0`](#insn-00bac6f0)

~~~json
{
  "source": "00bac6f0",
  "target": "00bac920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6f4`](#insn-00bac6f4)

~~~json
{
  "source": "00bac6f4",
  "target": "00bac928",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6f8`](#insn-00bac6f8)

~~~json
{
  "source": "00bac6f8",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac70c`](#insn-00bac70c)

~~~json
{
  "source": "00bac70c",
  "target": "00bac950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac718`](#insn-00bac718)

~~~json
{
  "source": "00bac718",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac720`](#insn-00bac720)

~~~json
{
  "source": "00bac720",
  "target": "00bac740",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac728`](#insn-00bac728)

~~~json
{
  "source": "00bac728",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac73c`](#insn-00bac73c)

~~~json
{
  "source": "00bac73c",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac75c`](#insn-00bac75c)

~~~json
{
  "source": "00bac75c",
  "target": "00bac7bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac790`](#insn-00bac790)

~~~json
{
  "source": "00bac790",
  "target": "00bac7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7ac`](#insn-00bac7ac)

~~~json
{
  "source": "00bac7ac",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac7b0`](#insn-00bac7b0)

~~~json
{
  "source": "00bac7b0",
  "target": "00bac7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7b4`](#insn-00bac7b4)

~~~json
{
  "source": "00bac7b4",
  "target": "00bac730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7b8`](#insn-00bac7b8)

~~~json
{
  "source": "00bac7b8",
  "target": "00bac7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7bc`](#insn-00bac7bc)

~~~json
{
  "source": "00bac7bc",
  "target": "00bac730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7c0`](#insn-00bac7c0)

~~~json
{
  "source": "00bac7c0",
  "target": "00bac7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7c8`](#insn-00bac7c8)

~~~json
{
  "source": "00bac7c8",
  "target": "00bac730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7d4`](#insn-00bac7d4)

~~~json
{
  "source": "00bac7d4",
  "target": "00bac72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7e0`](#insn-00bac7e0)

~~~json
{
  "source": "00bac7e0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7e4`](#insn-00bac7e4)

~~~json
{
  "source": "00bac7e4",
  "target": "00bac800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7e8`](#insn-00bac7e8)

~~~json
{
  "source": "00bac7e8",
  "target": "00bac728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7fc`](#insn-00bac7fc)

~~~json
{
  "source": "00bac7fc",
  "target": "00bac724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac810`](#insn-00bac810)

~~~json
{
  "source": "00bac810",
  "target": "00bac7e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac844`](#insn-00bac844)

~~~json
{
  "source": "00bac844",
  "target": "00bac878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac850`](#insn-00bac850)

~~~json
{
  "source": "00bac850",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac864`](#insn-00bac864)

~~~json
{
  "source": "00bac864",
  "target": "00c58050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac868`](#insn-00bac868)

~~~json
{
  "source": "00bac868",
  "target": "00bac878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac86c`](#insn-00bac86c)

~~~json
{
  "source": "00bac86c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac870`](#insn-00bac870)

~~~json
{
  "source": "00bac870",
  "target": "00bac7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac874`](#insn-00bac874)

~~~json
{
  "source": "00bac874",
  "target": "00bac728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac87c`](#insn-00bac87c)

~~~json
{
  "source": "00bac87c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac880`](#insn-00bac880)

~~~json
{
  "source": "00bac880",
  "target": "00bac7ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac88c`](#insn-00bac88c)

~~~json
{
  "source": "00bac88c",
  "target": "00bac728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac898`](#insn-00bac898)

~~~json
{
  "source": "00bac898",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac89c`](#insn-00bac89c)

~~~json
{
  "source": "00bac89c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8a0`](#insn-00bac8a0)

~~~json
{
  "source": "00bac8a0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8a4`](#insn-00bac8a4)

~~~json
{
  "source": "00bac8a4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8a8`](#insn-00bac8a8)

~~~json
{
  "source": "00bac8a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8ac`](#insn-00bac8ac)

~~~json
{
  "source": "00bac8ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8b0`](#insn-00bac8b0)

~~~json
{
  "source": "00bac8b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8b8`](#insn-00bac8b8)

~~~json
{
  "source": "00bac8b8",
  "target": "00bac950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac8c8`](#insn-00bac8c8)

~~~json
{
  "source": "00bac8c8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8cc`](#insn-00bac8cc)

~~~json
{
  "source": "00bac8cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8d0`](#insn-00bac8d0)

~~~json
{
  "source": "00bac8d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8d4`](#insn-00bac8d4)

~~~json
{
  "source": "00bac8d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8d8`](#insn-00bac8d8)

~~~json
{
  "source": "00bac8d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8dc`](#insn-00bac8dc)

~~~json
{
  "source": "00bac8dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8e0`](#insn-00bac8e0)

~~~json
{
  "source": "00bac8e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8e8`](#insn-00bac8e8)

~~~json
{
  "source": "00bac8e8",
  "target": "00bacbfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac8fc`](#insn-00bac8fc)

~~~json
{
  "source": "00bac8fc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac900`](#insn-00bac900)

~~~json
{
  "source": "00bac900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac904`](#insn-00bac904)

~~~json
{
  "source": "00bac904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac908`](#insn-00bac908)

~~~json
{
  "source": "00bac908",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac90c`](#insn-00bac90c)

~~~json
{
  "source": "00bac90c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac910`](#insn-00bac910)

~~~json
{
  "source": "00bac910",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac914`](#insn-00bac914)

~~~json
{
  "source": "00bac914",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac91c`](#insn-00bac91c)

~~~json
{
  "source": "00bac91c",
  "target": "00bace04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac924`](#insn-00bac924)

~~~json
{
  "source": "00bac924",
  "target": "00bac930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac930`](#insn-00bac930)

~~~json
{
  "source": "00bac930",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac934`](#insn-00bac934)

~~~json
{
  "source": "00bac934",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac938`](#insn-00bac938)

~~~json
{
  "source": "00bac938",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac93c`](#insn-00bac93c)

~~~json
{
  "source": "00bac93c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac940`](#insn-00bac940)

~~~json
{
  "source": "00bac940",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac944`](#insn-00bac944)

~~~json
{
  "source": "00bac944",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
