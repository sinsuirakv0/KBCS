# 00bacfd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-41040b2212f7c058e96c8c16d52d471d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bad3f8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-e62212ec52f10edc4ec0edb02db1114a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacfd0",
  "name": "FUN_00bacfd0",
  "size": 2508,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92ec78018948c716ce37d6f0cdd44b1725ef0d92b0a939f2c9ffa51c700f0fdf",
  "source_text_sha256": "92ec78018948c716ce37d6f0cdd44b1725ef0d92b0a939f2c9ffa51c700f0fdf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacfd0",
        "00bad99b"
      ]
    ],
    "bytes_sha256": "1c95637da7ef287ba7631e2b3a9cb76b85cc2de603a1e2e5656f0ab150ee0eab",
    "instruction_count": 627,
    "instruction_bytes": 2508,
    "body_bytes": 2508,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b82730](../00b82/00b82730.md)
- [00b82890](../00b82/00b82890.md)
- [00bacfd0](../00bac/00bacfd0.md)

## 呼び出し先

- [00bacfd0](../00bac/00bacfd0.md)
- [00bad99c](../00bad/00bad99c.md)
- [00badc48](../00bad/00badc48.md)
- [00bade50](../00bad/00bade50.md)
- [00bae130](../00bae/00bae130.md)
- [00c57c50](../00c57/00c57c50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 24427 bytes

~~~c

void FUN_00bacfd0(undefined8 *param_1,undefined8 *param_2)

{
  size_t sVar1;
  byte bVar2;
  byte bVar3;
  undefined8 *puVar4;
  int iVar5;
  int iVar6;
  ulong uVar7;
  ulong uVar8;
  long lVar9;
  byte *pbVar10;
  byte *pbVar11;
  byte *pbVar12;
  byte *pbVar13;
  undefined8 *puVar14;
  undefined8 *puVar15;
  undefined8 *puVar16;
  undefined8 *puVar17;
  byte *pbVar18;
  undefined8 *puVar19;
  long lVar20;
  long lVar21;
  long lVar22;
  
                    /* try { // try from 00bacfe4 to 00cacfef has its CatchHandler @ 00bad358 */
LAB_00bacff8:
                    /* try { // try from 00bacff8 to 00cad003 has its CatchHandler @ 00bad350 */
  puVar14 = param_2 + -1;
                    /* try { // try from 00bad004 to 00cad00f has its CatchHandler @ 00bad340 */
  puVar16 = param_1;
LAB_00bad00c:
  param_1 = puVar16;
  lVar9 = (long)param_2 - (long)param_1;
  uVar8 = lVar9 >> 3;
  switch(uVar8) {
  case 0:
  case 1:
    goto switchD_00bad6c8_caseD_0;
  case 2:
    pbVar13 = (byte *)param_2[-1];
    pbVar18 = (byte *)*param_1;
    if (*(long *)(pbVar13 + 0x80) == *(long *)(pbVar18 + 0x80)) {
      bVar2 = *pbVar18;
      bVar3 = *pbVar13;
      uVar8 = (ulong)(bVar2 >> 1);
                    /* try { // try from 00bad700 to 00cad70b has its CatchHandler @ 00badcd8 */
      if ((bVar2 & 1) != 0) {
        uVar8 = *(ulong *)(pbVar18 + 8);
      }
      uVar7 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar7 = *(ulong *)(pbVar13 + 8);
      }
      sVar1 = uVar8;
      if (uVar7 <= uVar8) {
        sVar1 = uVar7;
      }
      if (sVar1 != 0) {
        pbVar10 = *(byte **)(pbVar13 + 0x10);
        pbVar11 = *(byte **)(pbVar18 + 0x10);
        if ((bVar3 & 1) == 0) {
          pbVar10 = pbVar13 + 1;
        }
        if ((bVar2 & 1) == 0) {
          pbVar11 = pbVar18 + 1;
        }
        iVar5 = memcmp(pbVar10,pbVar11,sVar1);
        if (iVar5 != 0) {
          if (-1 < iVar5) {
            return;
          }
          goto LAB_00bad968;
        }
      }
      if (uVar8 <= uVar7) {
        return;
      }
    }
    else if (*(long *)(pbVar18 + 0x80) <= *(long *)(pbVar13 + 0x80)) {
      return;
    }
LAB_00bad968:
    *param_1 = pbVar13;
    param_2[-1] = pbVar18;
    return;
  case 3:
                    /* try { // try from 00bad8e0 to 00cad8e7 has its CatchHandler @ 00badc30 */
    FUN_00bad99c(param_1,param_1 + 1,puVar14);
    return;
  case 4:
    FUN_00badc48(param_1,param_1 + 1,param_1 + 2,puVar14);
    return;
  case 5:
    FUN_00bade50(param_1,param_1 + 1,param_1 + 2,param_1 + 3,puVar14);
    return;
  default:
                    /* try { // try from 00bad028 to 00cad033 has its CatchHandler @ 00bad2f4 */
    if (0xf7 < lVar9) {
      uVar7 = uVar8;
      if ((long)uVar8 < 0) {
        uVar7 = uVar8 + 1;
      }
      puVar16 = (undefined8 *)((long)param_1 + (uVar7 & 0x3ffffffffffffffe) * 4);
      if (lVar9 < 0x1f39) {
        iVar5 = FUN_00bad99c(param_1,puVar16,puVar14);
      }
      else {
                    /* try { // try from 00bad050 to 00cad05b has its CatchHandler @ 00bad2e8 */
        uVar7 = uVar8 + 3;
        if (-1 < (long)uVar8) {
          uVar7 = uVar8;
        }
        lVar9 = (uVar7 & 0x7ffffffffffffffc) * 2;
                    /* try { // try from 00bad074 to 00cad07f has its CatchHandler @ 00bad2e4 */
        iVar5 = FUN_00bade50(param_1,(long)param_1 + lVar9,puVar16,(long)puVar16 + lVar9,puVar14);
      }
      pbVar18 = (byte *)*param_1;
      pbVar13 = (byte *)*puVar16;
      lVar9 = *(long *)(pbVar18 + 0x80);
      lVar20 = *(long *)(pbVar13 + 0x80);
                    /* try { // try from 00bad0a4 to 00cad0bb has its CatchHandler @ 00bad2cc */
      puVar15 = puVar14;
      if (lVar9 == lVar20) {
        bVar2 = *pbVar13;
        bVar3 = *pbVar18;
                    /* try { // try from 00bad0bc to 00cad0c7 has its CatchHandler @ 00bad2b4 */
        uVar8 = (ulong)(bVar2 >> 1);
        if ((bVar2 & 1) != 0) {
          uVar8 = *(ulong *)(pbVar13 + 8);
        }
        uVar7 = (ulong)(bVar3 >> 1);
        if ((bVar3 & 1) != 0) {
          uVar7 = *(ulong *)(pbVar18 + 8);
        }
        sVar1 = uVar8;
        if (uVar7 <= uVar8) {
          sVar1 = uVar7;
        }
                    /* try { // try from 00bad0e0 to 00cad0eb has its CatchHandler @ 00bad29c */
        if (sVar1 != 0) {
          pbVar10 = *(byte **)(pbVar18 + 0x10);
          pbVar11 = *(byte **)(pbVar13 + 0x10);
          if ((bVar3 & 1) == 0) {
            pbVar10 = pbVar18 + 1;
          }
          if ((bVar2 & 1) == 0) {
            pbVar11 = pbVar13 + 1;
          }
          iVar6 = memcmp(pbVar10,pbVar11,sVar1);
          if (iVar6 != 0) {
            if (-1 < iVar6) goto LAB_00bad120;
            goto LAB_00bad1d8;
          }
        }
        if (uVar8 <= uVar7) goto LAB_00bad120;
      }
      else if (lVar20 <= lVar9) {
LAB_00bad120:
                    /* try { // try from 00bad12c to 00cad137 has its CatchHandler @ 00bad28c */
        if (param_1 != param_2 + -2) {
          puVar15 = param_2 + -2;
          do {
            pbVar10 = (byte *)*puVar15;
            if (*(long *)(pbVar10 + 0x80) == lVar20) {
                    /* try { // try from 00bad15c to 00cad167 has its CatchHandler @ 00bad270 */
              bVar2 = *pbVar13;
              bVar3 = *pbVar10;
                    /* try { // try from 00bad168 to 00cad173 has its CatchHandler @ 00bad26c */
                    /* try { // try from 00bad174 to 00cad17f has its CatchHandler @ 00bad268 */
              uVar8 = (ulong)(bVar2 >> 1);
              if ((bVar2 & 1) != 0) {
                uVar8 = *(ulong *)(pbVar13 + 8);
              }
              uVar7 = (ulong)(bVar3 >> 1);
              if ((bVar3 & 1) != 0) {
                uVar7 = *(ulong *)(pbVar10 + 8);
              }
              sVar1 = uVar8;
              if (uVar7 <= uVar8) {
                sVar1 = uVar7;
              }
              if (sVar1 != 0) {
                pbVar11 = *(byte **)(pbVar10 + 0x10);
                if ((bVar3 & 1) == 0) {
                  pbVar11 = pbVar10 + 1;
                }
                    /* try { // try from 00bad1a0 to 00cad1ab has its CatchHandler @ 00bad264 */
                pbVar12 = pbVar13 + 1;
                if ((bVar2 & 1) != 0) {
                  pbVar12 = *(byte **)(pbVar13 + 0x10);
                }
                iVar6 = memcmp(pbVar11,pbVar12,sVar1);
                if (iVar6 != 0) {
                  if (iVar6 < 0) goto LAB_00bad1c8;
                  goto LAB_00bad140;
                }
              }
                    /* try { // try from 00bad1bc to 00cad1db has its CatchHandler @ 00bad360 */
              if (uVar7 < uVar8) {
LAB_00bad1c8:
                *param_1 = pbVar10;
                *puVar15 = pbVar18;
                iVar5 = iVar5 + 1;
                goto LAB_00bad1d8;
              }
            }
            else {
                    /* try { // try from 00bad13c to 00cad147 has its CatchHandler @ 00bad284 */
              if (*(long *)(pbVar10 + 0x80) < lVar20) goto LAB_00bad1c8;
            }
LAB_00bad140:
            puVar15 = puVar15 + -1;
          } while (param_1 != puVar15);
        }
        pbVar13 = (byte *)*puVar14;
        puVar15 = param_1 + 1;
        if (lVar9 == *(long *)(pbVar13 + 0x80)) {
                    /* catch() { ... } // from try @ 00bad004 with catch @ 00bad340 */
          bVar2 = *pbVar13;
          bVar3 = *pbVar18;
                    /* catch() { ... } // from try @ 00bacff8 with catch @ 00bad350 */
                    /* catch() { ... } // from try @ 00bacfe4 with catch @ 00bad358 */
          uVar8 = (ulong)(bVar2 >> 1);
                    /* catch() { ... } // from try @ 00bacfc0 with catch @ 00bad35c */
          if ((bVar2 & 1) != 0) {
            uVar8 = *(ulong *)(pbVar13 + 8);
          }
                    /* catch() { ... } // from try @ 00bad1bc with catch @ 00bad360 */
          uVar7 = (ulong)(bVar3 >> 1);
                    /* catch() { ... } // from try @ 00bacee8 with catch @ 00bad364 */
                    /* catch() { ... } // from try @ 00bacedc with catch @ 00bad368 */
          if ((bVar3 & 1) != 0) {
            uVar7 = *(ulong *)(pbVar18 + 8);
          }
                    /* catch() { ... } // from try @ 00baced0 with catch @ 00bad36c */
          sVar1 = uVar8;
                    /* catch() { ... } // from try @ 00bacec4 with catch @ 00bad370 */
          if (uVar7 <= uVar8) {
            sVar1 = uVar7;
          }
          if (sVar1 != 0) {
            pbVar10 = *(byte **)(pbVar18 + 0x10);
            pbVar11 = *(byte **)(pbVar13 + 0x10);
                    /* catch() { ... } // from try @ 00bacea4 with catch @ 00bad384 */
            if ((bVar3 & 1) == 0) {
              pbVar10 = pbVar18 + 1;
            }
                    /* catch() { ... } // from try @ 00bace94 with catch @ 00bad38c */
            if ((bVar2 & 1) == 0) {
              pbVar11 = pbVar13 + 1;
            }
                    /* catch() { ... } // from try @ 00bace70 with catch @ 00bad390 */
            iVar5 = memcmp(pbVar10,pbVar11,sVar1);
            if (iVar5 != 0) {
              if (-1 < iVar5) goto LAB_00bad4bc;
              goto LAB_00bad564;
            }
          }
          if (uVar8 <= uVar7) goto LAB_00bad4bc;
        }
        else {
                    /* catch() { ... } // from try @ 00bacf20 with catch @ 00bad49c */
                    /* try { // try from 00bad4a0 to 00cad507 has its CatchHandler @ 00bad4a0
                       catch() { ... } // from try @ 00bad4a0 with catch @ 00bad4a0
                       catch() { ... } // from try @ 00badb94 with catch @ 00bad4a0 */
          if (*(long *)(pbVar13 + 0x80) <= lVar9) {
LAB_00bad4bc:
            if (puVar15 == puVar14) {
              return;
            }
            puVar15 = param_1 + 2;
            do {
              pbVar10 = (byte *)puVar15[-1];
              if (lVar9 == *(long *)(pbVar10 + 0x80)) {
                bVar2 = *pbVar10;
                bVar3 = *pbVar18;
                    /* try { // try from 00bad508 to 00cad513 has its CatchHandler @ 00badccc */
                uVar8 = (ulong)(bVar2 >> 1);
                if ((bVar2 & 1) != 0) {
                  uVar8 = *(ulong *)(pbVar10 + 8);
                }
                uVar7 = (ulong)(bVar3 >> 1);
                if ((bVar3 & 1) != 0) {
                  uVar7 = *(ulong *)(pbVar18 + 8);
                }
                sVar1 = uVar8;
                    /* try { // try from 00bad520 to 00cad527 has its CatchHandler @ 00badcc4 */
                if (uVar7 <= uVar8) {
                  sVar1 = uVar7;
                }
                if (sVar1 != 0) {
                  pbVar12 = *(byte **)(pbVar10 + 0x10);
                  pbVar11 = pbVar18 + 1;
                  if ((bVar3 & 1) != 0) {
                    pbVar11 = *(byte **)(pbVar18 + 0x10);
                  }
                  if ((bVar2 & 1) == 0) {
                    pbVar12 = pbVar10 + 1;
                  }
                  iVar5 = memcmp(pbVar11,pbVar12,sVar1);
                  if (iVar5 != 0) {
                    if (-1 < iVar5) goto LAB_00bad4d8;
                    goto LAB_00bad558;
                  }
                }
                if (uVar7 < uVar8) goto LAB_00bad558;
              }
              else if (lVar9 < *(long *)(pbVar10 + 0x80)) goto LAB_00bad558;
LAB_00bad4d8:
              puVar15 = puVar15 + 1;
              if (param_2 == puVar15) {
                return;
              }
            } while( true );
          }
        }
        goto LAB_00bad564;
      }
LAB_00bad1d8:
      puVar17 = param_1 + 1;
                    /* try { // try from 00bad1dc to 00cad227 has its CatchHandler @ 00bad498 */
      puVar4 = puVar16;
      if (puVar17 < puVar15) {
LAB_00bad1ec:
        puVar16 = puVar4;
        pbVar13 = (byte *)*puVar16;
        lVar9 = *(long *)(pbVar13 + 0x80);
        puVar19 = puVar17;
        do {
          pbVar18 = (byte *)*puVar19;
          if (*(long *)(pbVar18 + 0x80) == lVar9) {
            bVar2 = *pbVar13;
            bVar3 = *pbVar18;
                    /* try { // try from 00bad228 to 00cad49f has its CatchHandler @ 00bacca8 */
            uVar8 = (ulong)(bVar2 >> 1);
            if ((bVar2 & 1) != 0) {
              uVar8 = *(ulong *)(pbVar13 + 8);
            }
            uVar7 = (ulong)(bVar3 >> 1);
            if ((bVar3 & 1) != 0) {
              uVar7 = *(ulong *)(pbVar18 + 8);
            }
            sVar1 = uVar8;
            if (uVar7 <= uVar8) {
              sVar1 = uVar7;
            }
            if (sVar1 != 0) {
              pbVar10 = *(byte **)(pbVar18 + 0x10);
              if ((bVar3 & 1) == 0) {
                pbVar10 = pbVar18 + 1;
              }
              pbVar11 = pbVar13 + 1;
              if ((bVar2 & 1) != 0) {
                pbVar11 = *(byte **)(pbVar13 + 0x10);
              }
                    /* catch() { ... } // from try @ 00bad1a0 with catch @ 00bad264 */
              iVar6 = memcmp(pbVar10,pbVar11,sVar1);
                    /* catch() { ... } // from try @ 00bad174 with catch @ 00bad268 */
              if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00bad168 with catch @ 00bad26c */
                if (iVar6 < 0) goto LAB_00bad204;
                goto LAB_00bad284;
              }
            }
            if (uVar8 <= uVar7) goto LAB_00bad284;
          }
          else if (lVar9 <= *(long *)(pbVar18 + 0x80)) goto LAB_00bad284;
LAB_00bad204:
          puVar19 = puVar19 + 1;
        } while( true );
      }
      if (puVar17 != puVar16) goto LAB_00bad3c8;
      goto LAB_00bad44c;
    }
    FUN_00bad99c(param_1,param_1 + 1,param_1 + 2);
    if (param_1 + 3 == param_2) {
      return;
    }
    lVar9 = 0;
    puVar16 = param_1 + 3;
    puVar14 = param_1 + 2;
  }
LAB_00bad784:
  puVar15 = puVar16;
  pbVar18 = (byte *)*puVar15;
  pbVar13 = (byte *)*puVar14;
  lVar20 = *(long *)(pbVar18 + 0x80);
  if (lVar20 == *(long *)(pbVar13 + 0x80)) {
    bVar2 = *pbVar13;
    bVar3 = *pbVar18;
    uVar8 = (ulong)(bVar2 >> 1);
    if ((bVar2 & 1) != 0) {
      uVar8 = *(ulong *)(pbVar13 + 8);
    }
    uVar7 = (ulong)(bVar3 >> 1);
    if ((bVar3 & 1) != 0) {
      uVar7 = *(ulong *)(pbVar18 + 8);
    }
    sVar1 = uVar8;
    if (uVar7 <= uVar8) {
      sVar1 = uVar7;
    }
    if (sVar1 != 0) {
      pbVar10 = *(byte **)(pbVar18 + 0x10);
      pbVar11 = *(byte **)(pbVar13 + 0x10);
      if ((bVar3 & 1) == 0) {
        pbVar10 = pbVar18 + 1;
      }
                    /* try { // try from 00bad7ec to 00cad7f3 has its CatchHandler @ 00badcd4 */
      if ((bVar2 & 1) == 0) {
        pbVar11 = pbVar13 + 1;
      }
      iVar5 = memcmp(pbVar10,pbVar11,sVar1);
      if (iVar5 != 0) {
        if (iVar5 < 0) goto LAB_00bad810;
        goto LAB_00bad774;
      }
    }
                    /* try { // try from 00bad808 to 00cad80f has its CatchHandler @ 00badc68 */
    if (uVar7 < uVar8) {
LAB_00bad810:
      *puVar15 = pbVar13;
      puVar16 = puVar14;
      if (puVar14 != param_1) {
        lVar22 = lVar9;
        do {
          pbVar13 = *(byte **)((long)param_1 + lVar22 + 8);
          puVar16 = puVar14;
          if (lVar20 == *(long *)(pbVar13 + 0x80)) {
            bVar2 = *pbVar13;
            bVar3 = *pbVar18;
            uVar8 = (ulong)(bVar2 >> 1);
            if ((bVar2 & 1) != 0) {
              uVar8 = *(ulong *)(pbVar13 + 8);
            }
            uVar7 = (ulong)(bVar3 >> 1);
            if ((bVar3 & 1) != 0) {
              uVar7 = *(ulong *)(pbVar18 + 8);
            }
            sVar1 = uVar8;
            if (uVar7 <= uVar8) {
              sVar1 = uVar7;
            }
            if (sVar1 != 0) {
              pbVar11 = *(byte **)(pbVar13 + 0x10);
              pbVar10 = pbVar18 + 1;
              if ((bVar3 & 1) != 0) {
                pbVar10 = *(byte **)(pbVar18 + 0x10);
              }
              if ((bVar2 & 1) == 0) {
                pbVar11 = pbVar13 + 1;
              }
              iVar5 = memcmp(pbVar10,pbVar11,sVar1);
              if (iVar5 != 0) {
                if (iVar5 < 0) goto LAB_00bad830;
                break;
              }
            }
            if (uVar8 <= uVar7) {
              puVar16 = (undefined8 *)((long)param_1 + lVar22 + 0x10);
              break;
            }
          }
          else if (*(long *)(pbVar13 + 0x80) <= lVar20) break;
LAB_00bad830:
          lVar21 = lVar22 + -8;
          puVar14 = puVar14 + -1;
          *(byte **)((long)param_1 + lVar22 + 0x10) = pbVar13;
          puVar16 = param_1;
          lVar22 = lVar21;
        } while (lVar21 != -0x10);
      }
      *puVar16 = pbVar18;
    }
  }
  else if (lVar20 < *(long *)(pbVar13 + 0x80)) goto LAB_00bad810;
LAB_00bad774:
  lVar9 = lVar9 + 8;
  puVar16 = puVar15 + 1;
  puVar14 = puVar15;
  if (puVar15 + 1 == param_2) {
switchD_00bad6c8_caseD_0:
    return;
  }
  goto LAB_00bad784;
  while (lVar9 <= *(long *)(pbVar10 + 0x80)) {
LAB_00bad284:
    puVar15 = puVar15 + -1;
                    /* catch() { ... } // from try @ 00bad13c with catch @ 00bad284 */
    pbVar10 = (byte *)*puVar15;
                    /* catch() { ... } // from try @ 00bad12c with catch @ 00bad28c */
                    /* catch() { ... } // from try @ 00bad108 with catch @ 00bad290 */
    if (*(long *)(pbVar10 + 0x80) == lVar9) {
      bVar2 = *pbVar13;
                    /* catch() { ... } // from try @ 00bad0e0 with catch @ 00bad29c */
      bVar3 = *pbVar10;
      uVar8 = (ulong)(bVar2 >> 1);
      if ((bVar2 & 1) != 0) {
        uVar8 = *(ulong *)(pbVar13 + 8);
      }
                    /* catch() { ... } // from try @ 00bad0bc with catch @ 00bad2b4 */
      uVar7 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar7 = *(ulong *)(pbVar10 + 8);
      }
      sVar1 = uVar8;
      if (uVar7 <= uVar8) {
        sVar1 = uVar7;
      }
      if (sVar1 != 0) {
        pbVar11 = *(byte **)(pbVar10 + 0x10);
                    /* catch() { ... } // from try @ 00bad0a4 with catch @ 00bad2cc */
        if ((bVar3 & 1) == 0) {
          pbVar11 = pbVar10 + 1;
        }
        pbVar12 = pbVar13 + 1;
        if ((bVar2 & 1) != 0) {
          pbVar12 = *(byte **)(pbVar13 + 0x10);
        }
        iVar6 = memcmp(pbVar11,pbVar12,sVar1);
                    /* catch() { ... } // from try @ 00bad074 with catch @ 00bad2e4 */
        if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00bad050 with catch @ 00bad2e8 */
          if (iVar6 < 0) break;
          goto LAB_00bad284;
        }
      }
                    /* catch() { ... } // from try @ 00bad028 with catch @ 00bad2f4 */
      if (uVar7 < uVar8) break;
      goto LAB_00bad284;
    }
  }
  if (puVar19 <= puVar15) {
    puVar17 = puVar19 + 1;
    *puVar19 = pbVar10;
    iVar5 = iVar5 + 1;
    *puVar15 = pbVar18;
    puVar4 = puVar15;
    if (puVar16 != puVar19) {
      puVar4 = puVar16;
    }
    goto LAB_00bad1ec;
  }
                    /* catch() { ... } // from try @ 00bace24 with catch @ 00bad3b0 */
                    /* catch() { ... } // from try @ 00bace14 with catch @ 00bad3b8 */
                    /* catch() { ... } // from try @ 00bacdf0 with catch @ 00bad3bc */
  puVar17 = puVar19;
  if (puVar19 == puVar16) goto LAB_00bad44c;
LAB_00bad3c8:
                    /* catch() { ... } // from try @ 00bacdc8 with catch @ 00bad3c8 */
  pbVar13 = (byte *)*puVar16;
  pbVar18 = (byte *)*puVar17;
  if (*(long *)(pbVar13 + 0x80) == *(long *)(pbVar18 + 0x80)) {
    bVar2 = *pbVar18;
    bVar3 = *pbVar13;
                    /* catch() { ... } // from try @ 00bacda4 with catch @ 00bad3f0 */
    uVar8 = (ulong)(bVar2 >> 1);
    if ((bVar2 & 1) != 0) {
      uVar8 = *(ulong *)(pbVar18 + 8);
    }
                    /* catch() { ... } // from try @ 00bacd98 with catch @ 00bad400 */
    uVar7 = (ulong)(bVar3 >> 1);
    if ((bVar3 & 1) != 0) {
      uVar7 = *(ulong *)(pbVar13 + 8);
    }
    sVar1 = uVar8;
    if (uVar7 <= uVar8) {
      sVar1 = uVar7;
    }
    if (sVar1 != 0) {
      pbVar10 = *(byte **)(pbVar13 + 0x10);
      pbVar11 = *(byte **)(pbVar18 + 0x10);
                    /* catch() { ... } // from try @ 00bacd84 with catch @ 00bad420 */
      if ((bVar3 & 1) == 0) {
        pbVar10 = pbVar13 + 1;
      }
                    /* catch() { ... } // from try @ 00bacd60 with catch @ 00bad424 */
      if ((bVar2 & 1) == 0) {
        pbVar11 = pbVar18 + 1;
      }
      iVar6 = memcmp(pbVar10,pbVar11,sVar1);
      if (iVar6 != 0) {
                    /* catch() { ... } // from try @ 00bacf04 with catch @ 00bad434 */
        if (-1 < iVar6) goto LAB_00bad44c;
        goto LAB_00bad440;
      }
    }
    if (uVar8 <= uVar7) goto LAB_00bad44c;
  }
  else if (*(long *)(pbVar18 + 0x80) <= *(long *)(pbVar13 + 0x80)) goto LAB_00bad44c;
LAB_00bad440:
  iVar5 = iVar5 + 1;
  *puVar17 = pbVar13;
  *puVar16 = pbVar18;
LAB_00bad44c:
  if (iVar5 == 0) {
    uVar8 = FUN_00bae130(param_1,puVar17);
    uVar7 = FUN_00bae130(puVar17 + 1,param_2);
    if ((uVar7 & 1) != 0) goto LAB_00bad6a8;
    puVar16 = puVar17 + 1;
    if ((uVar8 & 1) != 0) goto LAB_00bad00c;
  }
  if ((long)param_2 - (long)puVar17 <= (long)puVar17 - (long)param_1) {
    FUN_00bacfd0(puVar17 + 1,param_2);
    param_2 = puVar17;
    goto LAB_00bacff8;
  }
  FUN_00bacfd0(param_1,puVar17);
  puVar16 = puVar17 + 1;
                    /* catch() { ... } // from try @ 00bad1dc with catch @ 00bad498 */
  goto LAB_00bad00c;
LAB_00bad6a8:
  param_2 = puVar17;
  if ((uVar8 & 1) != 0) {
    return;
  }
  goto LAB_00bacff8;
LAB_00bad558:
  puVar15[-1] = pbVar13;
  *puVar14 = pbVar10;
LAB_00bad564:
  puVar17 = puVar14;
                    /* try { // try from 00bad56c to 00cad577 has its CatchHandler @ 00badca0 */
  if (puVar15 == puVar14) {
    return;
  }
LAB_00bad574:
  pbVar13 = (byte *)*param_1;
                    /* try { // try from 00bad578 to 00cad587 has its CatchHandler @ 00badc6c */
  lVar9 = *(long *)(pbVar13 + 0x80);
  puVar16 = puVar15;
  do {
    pbVar18 = (byte *)*puVar16;
    if (lVar9 == *(long *)(pbVar18 + 0x80)) {
      bVar2 = *pbVar18;
      bVar3 = *pbVar13;
      uVar8 = (ulong)(bVar2 >> 1);
                    /* try { // try from 00bad5b8 to 00cad5cb has its CatchHandler @ 00badcd4 */
      if ((bVar2 & 1) != 0) {
        uVar8 = *(ulong *)(pbVar18 + 8);
      }
      uVar7 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar7 = *(ulong *)(pbVar13 + 8);
      }
      sVar1 = uVar8;
      if (uVar7 <= uVar8) {
        sVar1 = uVar7;
      }
      if (sVar1 != 0) {
        pbVar11 = *(byte **)(pbVar18 + 0x10);
        pbVar10 = pbVar13 + 1;
        if ((bVar3 & 1) != 0) {
          pbVar10 = *(byte **)(pbVar13 + 0x10);
        }
                    /* try { // try from 00bad5e4 to 00cad5eb has its CatchHandler @ 00badd0c */
        if ((bVar2 & 1) == 0) {
          pbVar11 = pbVar18 + 1;
        }
        iVar5 = memcmp(pbVar10,pbVar11,sVar1);
        if (iVar5 != 0) {
                    /* try { // try from 00bad5f0 to 00cad5ff has its CatchHandler @ 00badd08 */
          if (-1 < iVar5) goto LAB_00bad588;
          break;
        }
      }
      if (uVar7 < uVar8) break;
    }
    else if (lVar9 < *(long *)(pbVar18 + 0x80)) break;
LAB_00bad588:
    puVar16 = puVar16 + 1;
  } while( true );
  while (lVar9 < *(long *)(pbVar10 + 0x80)) {
LAB_00bad608:
    puVar17 = puVar17 + -1;
    pbVar10 = (byte *)*puVar17;
    if (lVar9 == *(long *)(pbVar10 + 0x80)) {
      bVar2 = *pbVar10;
      bVar3 = *pbVar13;
      uVar8 = (ulong)(bVar2 >> 1);
      if ((bVar2 & 1) != 0) {
        uVar8 = *(ulong *)(pbVar10 + 8);
      }
      uVar7 = (ulong)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar7 = *(ulong *)(pbVar13 + 8);
      }
      sVar1 = uVar8;
      if (uVar7 <= uVar8) {
        sVar1 = uVar7;
      }
      if (sVar1 != 0) {
        pbVar12 = *(byte **)(pbVar10 + 0x10);
        pbVar11 = pbVar13 + 1;
        if ((bVar3 & 1) != 0) {
          pbVar11 = *(byte **)(pbVar13 + 0x10);
        }
        if ((bVar2 & 1) == 0) {
          pbVar12 = pbVar10 + 1;
        }
        iVar5 = memcmp(pbVar11,pbVar12,sVar1);
        if (iVar5 != 0) {
          if (-1 < iVar5) break;
          goto LAB_00bad608;
        }
      }
      if (uVar8 <= uVar7) break;
      goto LAB_00bad608;
    }
  }
  if (puVar17 <= puVar16) goto LAB_00bad00c;
  puVar15 = puVar16 + 1;
  *puVar16 = pbVar10;
  *puVar17 = pbVar18;
  goto LAB_00bad574;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacfd0"></a> `00bacfd0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bacfd4"></a> `00bacfd4` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bacfd8"></a> `00bacfd8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bacfdc"></a> `00bacfdc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bacfe0"></a> `00bacfe0` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bacfe4"></a> `00bacfe4` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bacfe8"></a> `00bacfe8` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bacfec"></a> `00bacfec` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bacff0"></a> `00bacff0` | `fc 03 01 aa` | mov x28,x1 | `FALL_THROUGH`
<a id="insn-00bacff4"></a> `00bacff4` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bacff8"></a> `00bacff8` | `88 23 00 d1` | sub x8,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00bacffc"></a> `00bacffc` | `fc 23 01 a9` | stp x28,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad000"></a> `00bad000` | `88 43 00 d1` | sub x8,x28,#0x10 | `FALL_THROUGH`
<a id="insn-00bad004"></a> `00bad004` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00bad008"></a> `00bad008` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bad00c"></a> `00bad00c` | `89 03 16 cb` | sub x9,x28,x22 | `FALL_THROUGH`
<a id="insn-00bad010"></a> `00bad010` | `28 fd 43 93` | asr x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bad014"></a> `00bad014` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00bad018"></a> `00bad018` | `1f 15 00 f1` | cmp x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bad01c"></a> `00bad01c` | `c9 34 00 54` | b.ls 0x00bad6b4 | `CONDITIONAL_JUMP`
<a id="insn-00bad020"></a> `00bad020` | `3f dd 03 f1` | cmp x9,#0xf7 | `FALL_THROUGH`
<a id="insn-00bad024"></a> `00bad024` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad028"></a> `00bad028` | `cd 38 00 54` | b.le 0x00bad740 | `CONDITIONAL_JUMP`
<a id="insn-00bad02c"></a> `00bad02c` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bad030"></a> `00bad030` | `0a a5 88 9a` | cinc x10,x8,lt | `FALL_THROUGH`
<a id="insn-00bad034"></a> `00bad034` | `4a f5 7e d3` | lsl x10,x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bad038"></a> `00bad038` | `4a f1 7d 92` | and x10,x10,#-0x8 | `FALL_THROUGH`
<a id="insn-00bad03c"></a> `00bad03c` | `2b e7 83 52` | mov w11,#0x1f39 | `FALL_THROUGH`
<a id="insn-00bad040"></a> `00bad040` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bad044"></a> `00bad044` | `73 03 0a 8b` | add x19,x27,x10 | `FALL_THROUGH`
<a id="insn-00bad048"></a> `00bad048` | `ab 01 00 54` | b.lt 0x00bad07c | `CONDITIONAL_JUMP`
<a id="insn-00bad04c"></a> `00bad04c` | `09 0d 00 91` | add x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bad050"></a> `00bad050` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bad054"></a> `00bad054` | `28 b1 88 9a` | csel x8,x9,x8,lt | `FALL_THROUGH`
<a id="insn-00bad058"></a> `00bad058` | `e4 0f 40 f9` | ldr x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad05c"></a> `00bad05c` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad060"></a> `00bad060` | `08 f1 7d 92` | and x8,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00bad064"></a> `00bad064` | `61 03 08 8b` | add x1,x27,x8 | `FALL_THROUGH`
<a id="insn-00bad068"></a> `00bad068` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bad06c"></a> `00bad06c` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad070"></a> `00bad070` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bad074"></a> `00bad074` | `77 03 00 94` | bl 0x00bade50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad078"></a> `00bad078` | `05 00 00 14` | b 0x00bad08c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad07c"></a> `00bad07c` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad080"></a> `00bad080` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad084"></a> `00bad084` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bad088"></a> `00bad088` | `45 02 00 94` | bl 0x00bad99c | `UNCONDITIONAL_CALL`
<a id="insn-00bad08c"></a> `00bad08c` | `78 03 40 f9` | ldr x24,[x27] | `FALL_THROUGH`
<a id="insn-00bad090"></a> `00bad090` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00bad094"></a> `00bad094` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00bad098"></a> `00bad098` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00bad09c"></a> `00bad09c` | `08 43 40 f9` | ldr x8,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bad0a0"></a> `00bad0a0` | `b9 42 40 f9` | ldr x25,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bad0a4"></a> `00bad0a4` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bad0a8"></a> `00bad0a8` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bad0ac"></a> `00bad0ac` | `01 03 00 54` | b.ne 0x00bad10c | `CONDITIONAL_JUMP`
<a id="insn-00bad0b0"></a> `00bad0b0` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bad0b4"></a> `00bad0b4` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad0b8"></a> `00bad0b8` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad0bc"></a> `00bad0bc` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad0c0"></a> `00bad0c0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0c4"></a> `00bad0c4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0c8"></a> `00bad0c8` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0cc"></a> `00bad0cc` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad0d0"></a> `00bad0d0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0d4"></a> `00bad0d4` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad0d8"></a> `00bad0d8` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bad0dc"></a> `00bad0dc` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bad0e0"></a> `00bad0e0` | `c2 01 00 b4` | cbz x2,0x00bad118 | `CONDITIONAL_JUMP`
<a id="insn-00bad0e4"></a> `00bad0e4` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad0e8"></a> `00bad0e8` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad0ec"></a> `00bad0ec` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0f0"></a> `00bad0f0` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bad0f4"></a> `00bad0f4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad0f8"></a> `00bad0f8` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bad0fc"></a> `00bad0fc` | `d5 aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad100"></a> `00bad100` | `c0 00 00 34` | cbz w0,0x00bad118 | `CONDITIONAL_JUMP`
<a id="insn-00bad104"></a> `00bad104` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bad110 | `CONDITIONAL_JUMP`
<a id="insn-00bad108"></a> `00bad108` | `06 00 00 14` | b 0x00bad120 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad10c"></a> `00bad10c` | `aa 00 00 54` | b.ge 0x00bad120 | `CONDITIONAL_JUMP`
<a id="insn-00bad110"></a> `00bad110` | `fc 0f 40 f9` | ldr x28,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad114"></a> `00bad114` | `31 00 00 14` | b 0x00bad1d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad118"></a> `00bad118` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bad11c"></a> `00bad11c` | `a3 ff ff 54` | b.cc 0x00bad110 | `CONDITIONAL_JUMP`
<a id="insn-00bad120"></a> `00bad120` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bad124"></a> `00bad124` | `fa 2b 00 b9` | str w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad128"></a> `00bad128` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bad12c"></a> `00bad12c` | `c0 0f 00 54` | b.eq 0x00bad324 | `CONDITIONAL_JUMP`
<a id="insn-00bad130"></a> `00bad130` | `fc 07 40 f9` | ldr x28,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bad134"></a> `00bad134` | `ba 06 00 91` | add x26,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bad138"></a> `00bad138` | `05 00 00 14` | b 0x00bad14c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad13c"></a> `00bad13c` | `6b 04 00 54` | b.lt 0x00bad1c8 | `CONDITIONAL_JUMP`
<a id="insn-00bad140"></a> `00bad140` | `9c 23 00 d1` | sub x28,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00bad144"></a> `00bad144` | `7f 03 1c eb` | cmp x27,x28 | `FALL_THROUGH`
<a id="insn-00bad148"></a> `00bad148` | `e0 0e 00 54` | b.eq 0x00bad324 | `CONDITIONAL_JUMP`
<a id="insn-00bad14c"></a> `00bad14c` | `93 03 40 f9` | ldr x19,[x28] | `FALL_THROUGH`
<a id="insn-00bad150"></a> `00bad150` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad154"></a> `00bad154` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bad158"></a> `00bad158` | `21 ff ff 54` | b.ne 0x00bad13c | `CONDITIONAL_JUMP`
<a id="insn-00bad15c"></a> `00bad15c` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bad160"></a> `00bad160` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad164"></a> `00bad164` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bad168"></a> `00bad168` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad16c"></a> `00bad16c` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad170"></a> `00bad170` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad174"></a> `00bad174` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad178"></a> `00bad178` | `9b 01 8a 9a` | csel x27,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad17c"></a> `00bad17c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad180"></a> `00bad180` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad184"></a> `00bad184` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bad188"></a> `00bad188` | `62 33 94 9a` | csel x2,x27,x20,cc | `FALL_THROUGH`
<a id="insn-00bad18c"></a> `00bad18c` | `82 01 00 b4` | cbz x2,0x00bad1bc | `CONDITIONAL_JUMP`
<a id="insn-00bad190"></a> `00bad190` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad194"></a> `00bad194` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad198"></a> `00bad198` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad19c"></a> `00bad19c` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bad1a0"></a> `00bad1a0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad1a4"></a> `00bad1a4` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bad1a8"></a> `00bad1a8` | `aa aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad1ac"></a> `00bad1ac` | `80 00 00 34` | cbz w0,0x00bad1bc | `CONDITIONAL_JUMP`
<a id="insn-00bad1b0"></a> `00bad1b0` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad1b4"></a> `00bad1b4` | `60 fc ff 36` | tbz w0,#0x1f,0x00bad140 | `CONDITIONAL_JUMP`
<a id="insn-00bad1b8"></a> `00bad1b8` | `04 00 00 14` | b 0x00bad1c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad1bc"></a> `00bad1bc` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bad1c0"></a> `00bad1c0` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad1c4"></a> `00bad1c4` | `e2 fb ff 54` | b.cs 0x00bad140 | `CONDITIONAL_JUMP`
<a id="insn-00bad1c8"></a> `00bad1c8` | `fa 2b 40 b9` | ldr w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad1cc"></a> `00bad1cc` | `73 03 00 f9` | str x19,[x27] | `FALL_THROUGH`
<a id="insn-00bad1d0"></a> `00bad1d0` | `98 03 00 f9` | str x24,[x28] | `FALL_THROUGH`
<a id="insn-00bad1d4"></a> `00bad1d4` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00bad1d8"></a> `00bad1d8` | `78 23 00 91` | add x24,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad1dc"></a> `00bad1dc` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00bad1e0"></a> `00bad1e0` | `1f 03 1c eb` | cmp x24,x28 | `FALL_THROUGH`
<a id="insn-00bad1e4"></a> `00bad1e4` | `e2 0d 00 54` | b.cs 0x00bad3a0 | `CONDITIONAL_JUMP`
<a id="insn-00bad1e8"></a> `00bad1e8` | `fa 2b 00 b9` | str w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad1ec"></a> `00bad1ec` | `3b 03 40 f9` | ldr x27,[x25] | `FALL_THROUGH`
<a id="insn-00bad1f0"></a> `00bad1f0` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00bad1f4"></a> `00bad1f4` | `79 43 40 f9` | ldr x25,[x27, #0x80] | `FALL_THROUGH`
<a id="insn-00bad1f8"></a> `00bad1f8` | `7a 07 00 91` | add x26,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00bad1fc"></a> `00bad1fc` | `03 00 00 14` | b 0x00bad208 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad200"></a> `00bad200` | `2a 04 00 54` | b.ge 0x00bad284 | `CONDITIONAL_JUMP`
<a id="insn-00bad204"></a> `00bad204` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bad208"></a> `00bad208` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00bad20c"></a> `00bad20c` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bad210"></a> `00bad210` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bad214"></a> `00bad214` | `61 ff ff 54` | b.ne 0x00bad200 | `CONDITIONAL_JUMP`
<a id="insn-00bad218"></a> `00bad218` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00bad21c"></a> `00bad21c` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bad220"></a> `00bad220` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bad224"></a> `00bad224` | `ab 06 40 f9` | ldr x11,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad228"></a> `00bad228` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad22c"></a> `00bad22c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad230"></a> `00bad230` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad234"></a> `00bad234` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad238"></a> `00bad238` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad23c"></a> `00bad23c` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad240"></a> `00bad240` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bad244"></a> `00bad244` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bad248"></a> `00bad248` | `62 01 00 b4` | cbz x2,0x00bad274 | `CONDITIONAL_JUMP`
<a id="insn-00bad24c"></a> `00bad24c` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad250"></a> `00bad250` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bad254"></a> `00bad254` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad258"></a> `00bad258` | `40 15 95 9a` | csinc x0,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00bad25c"></a> `00bad25c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad260"></a> `00bad260` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bad264"></a> `00bad264` | `7b aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad268"></a> `00bad268` | `60 00 00 34` | cbz w0,0x00bad274 | `CONDITIONAL_JUMP`
<a id="insn-00bad26c"></a> `00bad26c` | `c0 fc ff 37` | tbnz w0,#0x1f,0x00bad204 | `CONDITIONAL_JUMP`
<a id="insn-00bad270"></a> `00bad270` | `05 00 00 14` | b 0x00bad284 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad274"></a> `00bad274` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bad278"></a> `00bad278` | `63 fc ff 54` | b.cc 0x00bad204 | `CONDITIONAL_JUMP`
<a id="insn-00bad27c"></a> `00bad27c` | `02 00 00 14` | b 0x00bad284 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad280"></a> `00bad280` | `cb 03 00 54` | b.lt 0x00bad2f8 | `CONDITIONAL_JUMP`
<a id="insn-00bad284"></a> `00bad284` | `93 8f 5f f8` | ldr x19,[x28, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bad288"></a> `00bad288` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad28c"></a> `00bad28c` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bad290"></a> `00bad290` | `81 ff ff 54` | b.ne 0x00bad280 | `CONDITIONAL_JUMP`
<a id="insn-00bad294"></a> `00bad294` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-00bad298"></a> `00bad298` | `6a 07 40 f9` | ldr x10,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00bad29c"></a> `00bad29c` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bad2a0"></a> `00bad2a0` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad2a4"></a> `00bad2a4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2a8"></a> `00bad2a8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2ac"></a> `00bad2ac` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2b0"></a> `00bad2b0` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad2b4"></a> `00bad2b4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2b8"></a> `00bad2b8` | `b7 01 8b 9a` | csel x23,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad2bc"></a> `00bad2bc` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00bad2c0"></a> `00bad2c0` | `82 32 97 9a` | csel x2,x20,x23,cc | `FALL_THROUGH`
<a id="insn-00bad2c4"></a> `00bad2c4` | `62 01 00 b4` | cbz x2,0x00bad2f0 | `CONDITIONAL_JUMP`
<a id="insn-00bad2c8"></a> `00bad2c8` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad2cc"></a> `00bad2cc` | `6b 0b 40 f9` | ldr x11,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00bad2d0"></a> `00bad2d0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2d4"></a> `00bad2d4` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bad2d8"></a> `00bad2d8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad2dc"></a> `00bad2dc` | `41 03 8b 9a` | csel x1,x26,x11,eq | `FALL_THROUGH`
<a id="insn-00bad2e0"></a> `00bad2e0` | `5c aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad2e4"></a> `00bad2e4` | `60 00 00 34` | cbz w0,0x00bad2f0 | `CONDITIONAL_JUMP`
<a id="insn-00bad2e8"></a> `00bad2e8` | `e0 fc ff 36` | tbz w0,#0x1f,0x00bad284 | `CONDITIONAL_JUMP`
<a id="insn-00bad2ec"></a> `00bad2ec` | `03 00 00 14` | b 0x00bad2f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad2f0"></a> `00bad2f0` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00bad2f4"></a> `00bad2f4` | `82 fc ff 54` | b.cs 0x00bad284 | `CONDITIONAL_JUMP`
<a id="insn-00bad2f8"></a> `00bad2f8` | `1f 03 1c eb` | cmp x24,x28 | `FALL_THROUGH`
<a id="insn-00bad2fc"></a> `00bad2fc` | `a8 05 00 54` | b.hi 0x00bad3b0 | `CONDITIONAL_JUMP`
<a id="insn-00bad300"></a> `00bad300` | `e8 2b 40 b9` | ldr w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad304"></a> `00bad304` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00bad308"></a> `00bad308` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bad30c"></a> `00bad30c` | `13 87 00 f8` | str x19,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bad310"></a> `00bad310` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad314"></a> `00bad314` | `95 03 00 f9` | str x21,[x28] | `FALL_THROUGH`
<a id="insn-00bad318"></a> `00bad318` | `e8 2b 00 b9` | str w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad31c"></a> `00bad31c` | `99 03 96 9a` | csel x25,x28,x22,eq | `FALL_THROUGH`
<a id="insn-00bad320"></a> `00bad320` | `b3 ff ff 17` | b 0x00bad1ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bad324"></a> `00bad324` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad328"></a> `00bad328` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bad32c"></a> `00bad32c` | `17 01 40 f9` | ldr x23,[x8] | `FALL_THROUGH`
<a id="insn-00bad330"></a> `00bad330` | `e8 42 40 f9` | ldr x8,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bad334"></a> `00bad334` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bad338"></a> `00bad338` | `76 23 00 91` | add x22,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad33c"></a> `00bad33c` | `01 0b 00 54` | b.ne 0x00bad49c | `CONDITIONAL_JUMP`
<a id="insn-00bad340"></a> `00bad340` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bad344"></a> `00bad344` | `ea 06 40 f9` | ldr x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bad348"></a> `00bad348` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad34c"></a> `00bad34c` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad350"></a> `00bad350` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad354"></a> `00bad354` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad358"></a> `00bad358` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad35c"></a> `00bad35c` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad360"></a> `00bad360` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad364"></a> `00bad364` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad368"></a> `00bad368` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad36c"></a> `00bad36c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bad370"></a> `00bad370` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bad374"></a> `00bad374` | `02 0a 00 b4` | cbz x2,0x00bad4b4 | `CONDITIONAL_JUMP`
<a id="insn-00bad378"></a> `00bad378` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad37c"></a> `00bad37c` | `eb 0a 40 f9` | ldr x11,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bad380"></a> `00bad380` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad384"></a> `00bad384` | `40 15 98 9a` | csinc x0,x10,x24,ne | `FALL_THROUGH`
<a id="insn-00bad388"></a> `00bad388` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad38c"></a> `00bad38c` | `61 15 97 9a` | csinc x1,x11,x23,ne | `FALL_THROUGH`
<a id="insn-00bad390"></a> `00bad390` | `30 aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad394"></a> `00bad394` | `00 09 00 34` | cbz w0,0x00bad4b4 | `CONDITIONAL_JUMP`
<a id="insn-00bad398"></a> `00bad398` | `20 09 f8 36` | tbz w0,#0x1f,0x00bad4bc | `CONDITIONAL_JUMP`
<a id="insn-00bad39c"></a> `00bad39c` | `72 00 00 14` | b 0x00bad564 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad3a0"></a> `00bad3a0` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad3a4"></a> `00bad3a4` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bad3a8"></a> `00bad3a8` | `01 01 00 54` | b.ne 0x00bad3c8 | `CONDITIONAL_JUMP`
<a id="insn-00bad3ac"></a> `00bad3ac` | `28 00 00 14` | b 0x00bad44c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad3b0"></a> `00bad3b0` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad3b4"></a> `00bad3b4` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad3b8"></a> `00bad3b8` | `fa 2b 40 b9` | ldr w26,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad3bc"></a> `00bad3bc` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00bad3c0"></a> `00bad3c0` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bad3c4"></a> `00bad3c4` | `40 04 00 54` | b.eq 0x00bad44c | `CONDITIONAL_JUMP`
<a id="insn-00bad3c8"></a> `00bad3c8` | `33 03 40 f9` | ldr x19,[x25] | `FALL_THROUGH`
<a id="insn-00bad3cc"></a> `00bad3cc` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00bad3d0"></a> `00bad3d0` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad3d4"></a> `00bad3d4` | `a9 42 40 f9` | ldr x9,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bad3d8"></a> `00bad3d8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bad3dc"></a> `00bad3dc` | `01 03 00 54` | b.ne 0x00bad43c | `CONDITIONAL_JUMP`
<a id="insn-00bad3e0"></a> `00bad3e0` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bad3e4"></a> `00bad3e4` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad3e8"></a> `00bad3e8` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bad3ec"></a> `00bad3ec` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad3f0"></a> `00bad3f0` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad3f4"></a> `00bad3f4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad3f8"></a> `00bad3f8` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad3fc"></a> `00bad3fc` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad400"></a> `00bad400` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad404"></a> `00bad404` | `b7 01 8b 9a` | csel x23,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad408"></a> `00bad408` | `9f 02 17 eb` | cmp x20,x23 | `FALL_THROUGH`
<a id="insn-00bad40c"></a> `00bad40c` | `82 32 97 9a` | csel x2,x20,x23,cc | `FALL_THROUGH`
<a id="insn-00bad410"></a> `00bad410` | `c2 04 00 b4` | cbz x2,0x00bad4a8 | `CONDITIONAL_JUMP`
<a id="insn-00bad414"></a> `00bad414` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad418"></a> `00bad418` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad41c"></a> `00bad41c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad420"></a> `00bad420` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bad424"></a> `00bad424` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad428"></a> `00bad428` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bad42c"></a> `00bad42c` | `09 aa 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad430"></a> `00bad430` | `c0 03 00 34` | cbz w0,0x00bad4a8 | `CONDITIONAL_JUMP`
<a id="insn-00bad434"></a> `00bad434` | `60 00 f8 37` | tbnz w0,#0x1f,0x00bad440 | `CONDITIONAL_JUMP`
<a id="insn-00bad438"></a> `00bad438` | `05 00 00 14` | b 0x00bad44c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad43c"></a> `00bad43c` | `8a 00 00 54` | b.ge 0x00bad44c | `CONDITIONAL_JUMP`
<a id="insn-00bad440"></a> `00bad440` | `5a 07 00 11` | add w26,w26,#0x1 | `FALL_THROUGH`
<a id="insn-00bad444"></a> `00bad444` | `13 03 00 f9` | str x19,[x24] | `FALL_THROUGH`
<a id="insn-00bad448"></a> `00bad448` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-00bad44c"></a> `00bad44c` | `7a 01 00 35` | cbnz w26,0x00bad478 | `CONDITIONAL_JUMP`
<a id="insn-00bad450"></a> `00bad450` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad454"></a> `00bad454` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bad458"></a> `00bad458` | `36 03 00 94` | bl 0x00bae130 | `UNCONDITIONAL_CALL`
<a id="insn-00bad45c"></a> `00bad45c` | `16 23 00 91` | add x22,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bad460"></a> `00bad460` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bad464"></a> `00bad464` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bad468"></a> `00bad468` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bad46c"></a> `00bad46c` | `31 03 00 94` | bl 0x00bae130 | `UNCONDITIONAL_CALL`
<a id="insn-00bad470"></a> `00bad470` | `c0 11 00 37` | tbnz w0,#0x0,0x00bad6a8 | `CONDITIONAL_JUMP`
<a id="insn-00bad474"></a> `00bad474` | `d7 dc 07 37` | tbnz w23,#0x0,0x00bad00c | `CONDITIONAL_JUMP`
<a id="insn-00bad478"></a> `00bad478` | `08 03 1b cb` | sub x8,x24,x27 | `FALL_THROUGH`
<a id="insn-00bad47c"></a> `00bad47c` | `89 03 18 cb` | sub x9,x28,x24 | `FALL_THROUGH`
<a id="insn-00bad480"></a> `00bad480` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bad484"></a> `00bad484` | `8a 10 00 54` | b.ge 0x00bad694 | `CONDITIONAL_JUMP`
<a id="insn-00bad488"></a> `00bad488` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad48c"></a> `00bad48c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bad490"></a> `00bad490` | `d0 fe ff 97` | bl 0x00bacfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bad494"></a> `00bad494` | `16 23 00 91` | add x22,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bad498"></a> `00bad498` | `dd fe ff 17` | b 0x00bad00c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad49c"></a> `00bad49c` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad4a0"></a> `00bad4a0` | `ea 00 00 54` | b.ge 0x00bad4bc | `CONDITIONAL_JUMP`
<a id="insn-00bad4a4"></a> `00bad4a4` | `30 00 00 14` | b 0x00bad564 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad4a8"></a> `00bad4a8` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00bad4ac"></a> `00bad4ac` | `a3 fc ff 54` | b.cc 0x00bad440 | `CONDITIONAL_JUMP`
<a id="insn-00bad4b0"></a> `00bad4b0` | `e7 ff ff 17` | b 0x00bad44c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad4b4"></a> `00bad4b4` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bad4b8"></a> `00bad4b8` | `63 05 00 54` | b.cc 0x00bad564 | `CONDITIONAL_JUMP`
<a id="insn-00bad4bc"></a> `00bad4bc` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad4c0"></a> `00bad4c0` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bad4c4"></a> `00bad4c4` | `60 25 00 54` | b.eq 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad4c8"></a> `00bad4c8` | `15 07 00 91` | add x21,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bad4cc"></a> `00bad4cc` | `76 43 00 91` | add x22,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bad4d0"></a> `00bad4d0` | `05 00 00 14` | b 0x00bad4e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad4d4"></a> `00bad4d4` | `2b 04 00 54` | b.lt 0x00bad558 | `CONDITIONAL_JUMP`
<a id="insn-00bad4d8"></a> `00bad4d8` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bad4dc"></a> `00bad4dc` | `9f 03 16 eb` | cmp x28,x22 | `FALL_THROUGH`
<a id="insn-00bad4e0"></a> `00bad4e0` | `80 24 00 54` | b.eq 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad4e4"></a> `00bad4e4` | `d3 82 5f f8` | ldur x19,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00bad4e8"></a> `00bad4e8` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad4ec"></a> `00bad4ec` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00bad4f0"></a> `00bad4f0` | `21 ff ff 54` | b.ne 0x00bad4d4 | `CONDITIONAL_JUMP`
<a id="insn-00bad4f4"></a> `00bad4f4` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bad4f8"></a> `00bad4f8` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad4fc"></a> `00bad4fc` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad500"></a> `00bad500` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad504"></a> `00bad504` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad508"></a> `00bad508` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad50c"></a> `00bad50c` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad510"></a> `00bad510` | `99 01 8a 9a` | csel x25,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad514"></a> `00bad514` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad518"></a> `00bad518` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad51c"></a> `00bad51c` | `3f 03 14 eb` | cmp x25,x20 | `FALL_THROUGH`
<a id="insn-00bad520"></a> `00bad520` | `22 33 94 9a` | csel x2,x25,x20,cc | `FALL_THROUGH`
<a id="insn-00bad524"></a> `00bad524` | `62 01 00 b4` | cbz x2,0x00bad550 | `CONDITIONAL_JUMP`
<a id="insn-00bad528"></a> `00bad528` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad52c"></a> `00bad52c` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad530"></a> `00bad530` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad534"></a> `00bad534` | `a0 02 8a 9a` | csel x0,x21,x10,eq | `FALL_THROUGH`
<a id="insn-00bad538"></a> `00bad538` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad53c"></a> `00bad53c` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bad540"></a> `00bad540` | `c4 a9 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad544"></a> `00bad544` | `60 00 00 34` | cbz w0,0x00bad550 | `CONDITIONAL_JUMP`
<a id="insn-00bad548"></a> `00bad548` | `80 fc ff 36` | tbz w0,#0x1f,0x00bad4d8 | `CONDITIONAL_JUMP`
<a id="insn-00bad54c"></a> `00bad54c` | `03 00 00 14` | b 0x00bad558 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad550"></a> `00bad550` | `9f 02 19 eb` | cmp x20,x25 | `FALL_THROUGH`
<a id="insn-00bad554"></a> `00bad554` | `22 fc ff 54` | b.cs 0x00bad4d8 | `CONDITIONAL_JUMP`
<a id="insn-00bad558"></a> `00bad558` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad55c"></a> `00bad55c` | `d7 82 1f f8` | stur x23,[x22, #-0x8] | `FALL_THROUGH`
<a id="insn-00bad560"></a> `00bad560` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00bad564"></a> `00bad564` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad568"></a> `00bad568` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bad56c"></a> `00bad56c` | `20 20 00 54` | b.eq 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad570"></a> `00bad570` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad574"></a> `00bad574` | `78 03 40 f9` | ldr x24,[x27] | `FALL_THROUGH`
<a id="insn-00bad578"></a> `00bad578` | `1b 43 40 f9` | ldr x27,[x24, #0x80] | `FALL_THROUGH`
<a id="insn-00bad57c"></a> `00bad57c` | `19 07 00 91` | add x25,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bad580"></a> `00bad580` | `03 00 00 14` | b 0x00bad58c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad584"></a> `00bad584` | `2b 04 00 54` | b.lt 0x00bad608 | `CONDITIONAL_JUMP`
<a id="insn-00bad588"></a> `00bad588` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bad58c"></a> `00bad58c` | `d5 02 40 f9` | ldr x21,[x22] | `FALL_THROUGH`
<a id="insn-00bad590"></a> `00bad590` | `a8 42 40 f9` | ldr x8,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bad594"></a> `00bad594` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bad598"></a> `00bad598` | `61 ff ff 54` | b.ne 0x00bad584 | `CONDITIONAL_JUMP`
<a id="insn-00bad59c"></a> `00bad59c` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bad5a0"></a> `00bad5a0` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad5a4"></a> `00bad5a4` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad5a8"></a> `00bad5a8` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad5ac"></a> `00bad5ac` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5b0"></a> `00bad5b0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5b4"></a> `00bad5b4` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5b8"></a> `00bad5b8` | `93 01 8a 9a` | csel x19,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad5bc"></a> `00bad5bc` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5c0"></a> `00bad5c0` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad5c4"></a> `00bad5c4` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bad5c8"></a> `00bad5c8` | `62 32 94 9a` | csel x2,x19,x20,cc | `FALL_THROUGH`
<a id="insn-00bad5cc"></a> `00bad5cc` | `62 01 00 b4` | cbz x2,0x00bad5f8 | `CONDITIONAL_JUMP`
<a id="insn-00bad5d0"></a> `00bad5d0` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad5d4"></a> `00bad5d4` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad5d8"></a> `00bad5d8` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5dc"></a> `00bad5dc` | `20 03 8a 9a` | csel x0,x25,x10,eq | `FALL_THROUGH`
<a id="insn-00bad5e0"></a> `00bad5e0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad5e4"></a> `00bad5e4` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bad5e8"></a> `00bad5e8` | `9a a9 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad5ec"></a> `00bad5ec` | `60 00 00 34` | cbz w0,0x00bad5f8 | `CONDITIONAL_JUMP`
<a id="insn-00bad5f0"></a> `00bad5f0` | `c0 fc ff 36` | tbz w0,#0x1f,0x00bad588 | `CONDITIONAL_JUMP`
<a id="insn-00bad5f4"></a> `00bad5f4` | `05 00 00 14` | b 0x00bad608 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad5f8"></a> `00bad5f8` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00bad5fc"></a> `00bad5fc` | `62 fc ff 54` | b.cs 0x00bad588 | `CONDITIONAL_JUMP`
<a id="insn-00bad600"></a> `00bad600` | `02 00 00 14` | b 0x00bad608 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad604"></a> `00bad604` | `ca 03 00 54` | b.ge 0x00bad67c | `CONDITIONAL_JUMP`
<a id="insn-00bad608"></a> `00bad608` | `f3 8e 5f f8` | ldr x19,[x23, #-0x8]! | `FALL_THROUGH`
<a id="insn-00bad60c"></a> `00bad60c` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad610"></a> `00bad610` | `7f 03 08 eb` | cmp x27,x8 | `FALL_THROUGH`
<a id="insn-00bad614"></a> `00bad614` | `81 ff ff 54` | b.ne 0x00bad604 | `CONDITIONAL_JUMP`
<a id="insn-00bad618"></a> `00bad618` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bad61c"></a> `00bad61c` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad620"></a> `00bad620` | `09 03 40 39` | ldrb w9,[x24] | `FALL_THROUGH`
<a id="insn-00bad624"></a> `00bad624` | `0b 07 40 f9` | ldr x11,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bad628"></a> `00bad628` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad62c"></a> `00bad62c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad630"></a> `00bad630` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad634"></a> `00bad634` | `9a 01 8a 9a` | csel x26,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad638"></a> `00bad638` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad63c"></a> `00bad63c` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad640"></a> `00bad640` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bad644"></a> `00bad644` | `42 33 94 9a` | csel x2,x26,x20,cc | `FALL_THROUGH`
<a id="insn-00bad648"></a> `00bad648` | `62 01 00 b4` | cbz x2,0x00bad674 | `CONDITIONAL_JUMP`
<a id="insn-00bad64c"></a> `00bad64c` | `0a 0b 40 f9` | ldr x10,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bad650"></a> `00bad650` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad654"></a> `00bad654` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad658"></a> `00bad658` | `20 03 8a 9a` | csel x0,x25,x10,eq | `FALL_THROUGH`
<a id="insn-00bad65c"></a> `00bad65c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad660"></a> `00bad660` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bad664"></a> `00bad664` | `7b a9 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad668"></a> `00bad668` | `60 00 00 34` | cbz w0,0x00bad674 | `CONDITIONAL_JUMP`
<a id="insn-00bad66c"></a> `00bad66c` | `e0 fc ff 37` | tbnz w0,#0x1f,0x00bad608 | `CONDITIONAL_JUMP`
<a id="insn-00bad670"></a> `00bad670` | `03 00 00 14` | b 0x00bad67c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad674"></a> `00bad674` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bad678"></a> `00bad678` | `83 fc ff 54` | b.cc 0x00bad608 | `CONDITIONAL_JUMP`
<a id="insn-00bad67c"></a> `00bad67c` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00bad680"></a> `00bad680` | `62 cc ff 54` | b.cs 0x00bad00c | `CONDITIONAL_JUMP`
<a id="insn-00bad684"></a> `00bad684` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad688"></a> `00bad688` | `d3 86 00 f8` | str x19,[x22], #0x8 | `FALL_THROUGH`
<a id="insn-00bad68c"></a> `00bad68c` | `f5 02 00 f9` | str x21,[x23] | `FALL_THROUGH`
<a id="insn-00bad690"></a> `00bad690` | `b9 ff ff 17` | b 0x00bad574 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad694"></a> `00bad694` | `00 23 00 91` | add x0,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bad698"></a> `00bad698` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bad69c"></a> `00bad69c` | `4d fe ff 97` | bl 0x00bacfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bad6a0"></a> `00bad6a0` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00bad6a4"></a> `00bad6a4` | `55 fe ff 17` | b 0x00bacff8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad6a8"></a> `00bad6a8` | `fc 03 18 aa` | mov x28,x24 | `FALL_THROUGH`
<a id="insn-00bad6ac"></a> `00bad6ac` | `77 ca 07 36` | tbz w23,#0x0,0x00bacff8 | `CONDITIONAL_JUMP`
<a id="insn-00bad6b0"></a> `00bad6b0` | `b0 00 00 14` | b 0x00bad970 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad6b4"></a> `00bad6b4` | `09 bb ff b0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00bad6b8"></a> `00bad6b8` | `29 31 07 91` | add x9,x9,#0x1cc | `FALL_THROUGH`
<a id="insn-00bad6bc"></a> `00bad6bc` | `8a 00 00 10` | adr x10,0xbad6cc | `FALL_THROUGH`
<a id="insn-00bad6c0"></a> `00bad6c0` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bad6c4"></a> `00bad6c4` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bad6c8"></a> `00bad6c8` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00bad6cc"></a> `00bad6cc` | `93 83 5f f8` | ldur x19,[x28, #-0x8] | `FALL_THROUGH`
<a id="insn-00bad6d0"></a> `00bad6d0` | `75 03 40 f9` | ldr x21,[x27] | `FALL_THROUGH`
<a id="insn-00bad6d4"></a> `00bad6d4` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad6d8"></a> `00bad6d8` | `a9 42 40 f9` | ldr x9,[x21, #0x80] | `FALL_THROUGH`
<a id="insn-00bad6dc"></a> `00bad6dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bad6e0"></a> `00bad6e0` | `21 14 00 54` | b.ne 0x00bad964 | `CONDITIONAL_JUMP`
<a id="insn-00bad6e4"></a> `00bad6e4` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bad6e8"></a> `00bad6e8` | `aa 06 40 f9` | ldr x10,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bad6ec"></a> `00bad6ec` | `69 02 40 39` | ldrb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bad6f0"></a> `00bad6f0` | `6b 06 40 f9` | ldr x11,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad6f4"></a> `00bad6f4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad6f8"></a> `00bad6f8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad6fc"></a> `00bad6fc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad700"></a> `00bad700` | `96 01 8a 9a` | csel x22,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad704"></a> `00bad704` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad708"></a> `00bad708` | `b4 01 8b 9a` | csel x20,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad70c"></a> `00bad70c` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00bad710"></a> `00bad710` | `c2 32 94 9a` | csel x2,x22,x20,cc | `FALL_THROUGH`
<a id="insn-00bad714"></a> `00bad714` | `e2 13 00 b4` | cbz x2,0x00bad990 | `CONDITIONAL_JUMP`
<a id="insn-00bad718"></a> `00bad718` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad71c"></a> `00bad71c` | `ab 0a 40 f9` | ldr x11,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bad720"></a> `00bad720` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad724"></a> `00bad724` | `40 15 93 9a` | csinc x0,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bad728"></a> `00bad728` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad72c"></a> `00bad72c` | `61 15 95 9a` | csinc x1,x11,x21,ne | `FALL_THROUGH`
<a id="insn-00bad730"></a> `00bad730` | `48 a9 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad734"></a> `00bad734` | `e0 12 00 34` | cbz w0,0x00bad990 | `CONDITIONAL_JUMP`
<a id="insn-00bad738"></a> `00bad738` | `80 11 f8 37` | tbnz w0,#0x1f,0x00bad968 | `CONDITIONAL_JUMP`
<a id="insn-00bad73c"></a> `00bad73c` | `8d 00 00 14` | b 0x00bad970 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad740"></a> `00bad740` | `75 43 00 91` | add x21,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bad744"></a> `00bad744` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad748"></a> `00bad748` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad74c"></a> `00bad74c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bad750"></a> `00bad750` | `93 00 00 94` | bl 0x00bad99c | `UNCONDITIONAL_CALL`
<a id="insn-00bad754"></a> `00bad754` | `68 63 00 91` | add x8,x27,#0x18 | `FALL_THROUGH`
<a id="insn-00bad758"></a> `00bad758` | `1f 01 1c eb` | cmp x8,x28 | `FALL_THROUGH`
<a id="insn-00bad75c"></a> `00bad75c` | `a0 10 00 54` | b.eq 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad760"></a> `00bad760` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bad764"></a> `00bad764` | `08 00 00 14` | b 0x00bad784 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad768"></a> `00bad768` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00bad76c"></a> `00bad76c` | `fc 0b 40 f9` | ldr x28,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bad770"></a> `00bad770` | `17 03 00 f9` | str x23,[x24] | `FALL_THROUGH`
<a id="insn-00bad774"></a> `00bad774` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bad778"></a> `00bad778` | `1f 01 1c eb` | cmp x8,x28 | `FALL_THROUGH`
<a id="insn-00bad77c"></a> `00bad77c` | `d6 22 00 91` | add x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bad780"></a> `00bad780` | `80 0f 00 54` | b.eq 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad784"></a> `00bad784` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00bad788"></a> `00bad788` | `17 01 40 f9` | ldr x23,[x8] | `FALL_THROUGH`
<a id="insn-00bad78c"></a> `00bad78c` | `13 03 40 f9` | ldr x19,[x24] | `FALL_THROUGH`
<a id="insn-00bad790"></a> `00bad790` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bad794"></a> `00bad794` | `f9 42 40 f9` | ldr x25,[x23, #0x80] | `FALL_THROUGH`
<a id="insn-00bad798"></a> `00bad798` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad79c"></a> `00bad79c` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bad7a0"></a> `00bad7a0` | `01 03 00 54` | b.ne 0x00bad800 | `CONDITIONAL_JUMP`
<a id="insn-00bad7a4"></a> `00bad7a4` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bad7a8"></a> `00bad7a8` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad7ac"></a> `00bad7ac` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bad7b0"></a> `00bad7b0` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bad7b4"></a> `00bad7b4` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7b8"></a> `00bad7b8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7bc"></a> `00bad7bc` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7c0"></a> `00bad7c0` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad7c4"></a> `00bad7c4` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7c8"></a> `00bad7c8` | `ba 01 8b 9a` | csel x26,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad7cc"></a> `00bad7cc` | `9f 02 1a eb` | cmp x20,x26 | `FALL_THROUGH`
<a id="insn-00bad7d0"></a> `00bad7d0` | `82 32 9a 9a` | csel x2,x20,x26,cc | `FALL_THROUGH`
<a id="insn-00bad7d4"></a> `00bad7d4` | `a2 01 00 b4` | cbz x2,0x00bad808 | `CONDITIONAL_JUMP`
<a id="insn-00bad7d8"></a> `00bad7d8` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bad7dc"></a> `00bad7dc` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad7e0"></a> `00bad7e0` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7e4"></a> `00bad7e4` | `40 15 97 9a` | csinc x0,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bad7e8"></a> `00bad7e8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad7ec"></a> `00bad7ec` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bad7f0"></a> `00bad7f0` | `18 a9 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad7f4"></a> `00bad7f4` | `a0 00 00 34` | cbz w0,0x00bad808 | `CONDITIONAL_JUMP`
<a id="insn-00bad7f8"></a> `00bad7f8` | `e0 fb ff 36` | tbz w0,#0x1f,0x00bad774 | `CONDITIONAL_JUMP`
<a id="insn-00bad7fc"></a> `00bad7fc` | `05 00 00 14` | b 0x00bad810 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad800"></a> `00bad800` | `aa fb ff 54` | b.ge 0x00bad774 | `CONDITIONAL_JUMP`
<a id="insn-00bad804"></a> `00bad804` | `03 00 00 14` | b 0x00bad810 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad808"></a> `00bad808` | `5f 03 14 eb` | cmp x26,x20 | `FALL_THROUGH`
<a id="insn-00bad80c"></a> `00bad80c` | `42 fb ff 54` | b.cs 0x00bad774 | `CONDITIONAL_JUMP`
<a id="insn-00bad810"></a> `00bad810` | `1f 03 1b eb` | cmp x24,x27 | `FALL_THROUGH`
<a id="insn-00bad814"></a> `00bad814` | `b3 02 00 f9` | str x19,[x21] | `FALL_THROUGH`
<a id="insn-00bad818"></a> `00bad818` | `c0 fa ff 54` | b.eq 0x00bad770 | `CONDITIONAL_JUMP`
<a id="insn-00bad81c"></a> `00bad81c` | `e8 06 00 91` | add x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bad820"></a> `00bad820` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00bad824"></a> `00bad824` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad828"></a> `00bad828` | `07 00 00 14` | b 0x00bad844 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad82c"></a> `00bad82c` | `0a fa ff 54` | b.ge 0x00bad76c | `CONDITIONAL_JUMP`
<a id="insn-00bad830"></a> `00bad830` | `5a 23 00 d1` | sub x26,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00bad834"></a> `00bad834` | `18 23 00 d1` | sub x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00bad838"></a> `00bad838` | `5f 43 00 b1` | cmn x26,#0x10 | `FALL_THROUGH`
<a id="insn-00bad83c"></a> `00bad83c` | `93 0b 00 f9` | str x19,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00bad840"></a> `00bad840` | `40 f9 ff 54` | b.eq 0x00bad768 | `CONDITIONAL_JUMP`
<a id="insn-00bad844"></a> `00bad844` | `7c 03 1a 8b` | add x28,x27,x26 | `FALL_THROUGH`
<a id="insn-00bad848"></a> `00bad848` | `93 07 40 f9` | ldr x19,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00bad84c"></a> `00bad84c` | `68 42 40 f9` | ldr x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bad850"></a> `00bad850` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bad854"></a> `00bad854` | `c1 fe ff 54` | b.ne 0x00bad82c | `CONDITIONAL_JUMP`
<a id="insn-00bad858"></a> `00bad858` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bad85c"></a> `00bad85c` | `6a 06 40 f9` | ldr x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bad860"></a> `00bad860` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bad864"></a> `00bad864` | `eb 06 40 f9` | ldr x11,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bad868"></a> `00bad868` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad86c"></a> `00bad86c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad870"></a> `00bad870` | `2d fd 41 d3` | lsr x13,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad874"></a> `00bad874` | `94 01 8a 9a` | csel x20,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00bad878"></a> `00bad878` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad87c"></a> `00bad87c` | `bb 01 8b 9a` | csel x27,x13,x11,eq | `FALL_THROUGH`
<a id="insn-00bad880"></a> `00bad880` | `9f 02 1b eb` | cmp x20,x27 | `FALL_THROUGH`
<a id="insn-00bad884"></a> `00bad884` | `82 32 9b 9a` | csel x2,x20,x27,cc | `FALL_THROUGH`
<a id="insn-00bad888"></a> `00bad888` | `a2 01 00 b4` | cbz x2,0x00bad8bc | `CONDITIONAL_JUMP`
<a id="insn-00bad88c"></a> `00bad88c` | `ea 0a 40 f9` | ldr x10,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00bad890"></a> `00bad890` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bad894"></a> `00bad894` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bad898"></a> `00bad898` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bad89c"></a> `00bad89c` | `20 01 8a 9a` | csel x0,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00bad8a0"></a> `00bad8a0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad8a4"></a> `00bad8a4` | `61 15 93 9a` | csinc x1,x11,x19,ne | `FALL_THROUGH`
<a id="insn-00bad8a8"></a> `00bad8a8` | `ea a8 02 94` | bl 0x00c57c50 | `UNCONDITIONAL_CALL`
<a id="insn-00bad8ac"></a> `00bad8ac` | `80 00 00 34` | cbz w0,0x00bad8bc | `CONDITIONAL_JUMP`
<a id="insn-00bad8b0"></a> `00bad8b0` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad8b4"></a> `00bad8b4` | `e0 fb ff 37` | tbnz w0,#0x1f,0x00bad830 | `CONDITIONAL_JUMP`
<a id="insn-00bad8b8"></a> `00bad8b8` | `ad ff ff 17` | b 0x00bad76c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad8bc"></a> `00bad8bc` | `7f 03 14 eb` | cmp x27,x20 | `FALL_THROUGH`
<a id="insn-00bad8c0"></a> `00bad8c0` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bad8c4"></a> `00bad8c4` | `63 fb ff 54` | b.cc 0x00bad830 | `CONDITIONAL_JUMP`
<a id="insn-00bad8c8"></a> `00bad8c8` | `68 03 1a 8b` | add x8,x27,x26 | `FALL_THROUGH`
<a id="insn-00bad8cc"></a> `00bad8cc` | `18 41 00 91` | add x24,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bad8d0"></a> `00bad8d0` | `a7 ff ff 17` | b 0x00bad76c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad8d4"></a> `00bad8d4` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad8d8"></a> `00bad8d8` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad8dc"></a> `00bad8dc` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad8e0"></a> `00bad8e0` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bad8e4"></a> `00bad8e4` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bad8e8"></a> `00bad8e8` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bad8ec"></a> `00bad8ec` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad8f0"></a> `00bad8f0` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad8f4"></a> `00bad8f4` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad8f8"></a> `00bad8f8` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bad8fc"></a> `00bad8fc` | `28 00 00 14` | b 0x00bad99c | `CALL_TERMINATOR`
<a id="insn-00bad900"></a> `00bad900` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad904"></a> `00bad904` | `62 43 00 91` | add x2,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bad908"></a> `00bad908` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad90c"></a> `00bad90c` | `e3 0f 40 f9` | ldr x3,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad910"></a> `00bad910` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bad914"></a> `00bad914` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bad918"></a> `00bad918` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bad91c"></a> `00bad91c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad920"></a> `00bad920` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad924"></a> `00bad924` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad928"></a> `00bad928` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bad92c"></a> `00bad92c` | `c7 00 00 14` | b 0x00badc48 | `CALL_TERMINATOR`
<a id="insn-00bad930"></a> `00bad930` | `61 23 00 91` | add x1,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00bad934"></a> `00bad934` | `62 43 00 91` | add x2,x27,#0x10 | `FALL_THROUGH`
<a id="insn-00bad938"></a> `00bad938` | `63 63 00 91` | add x3,x27,#0x18 | `FALL_THROUGH`
<a id="insn-00bad93c"></a> `00bad93c` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bad940"></a> `00bad940` | `e4 0f 40 f9` | ldr x4,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bad944"></a> `00bad944` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bad948"></a> `00bad948` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bad94c"></a> `00bad94c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bad950"></a> `00bad950` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad954"></a> `00bad954` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad958"></a> `00bad958` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad95c"></a> `00bad95c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bad960"></a> `00bad960` | `3c 01 00 14` | b 0x00bade50 | `CALL_TERMINATOR`
<a id="insn-00bad964"></a> `00bad964` | `6a 00 00 54` | b.ge 0x00bad970 | `CONDITIONAL_JUMP`
<a id="insn-00bad968"></a> `00bad968` | `73 03 00 f9` | str x19,[x27] | `FALL_THROUGH`
<a id="insn-00bad96c"></a> `00bad96c` | `95 83 1f f8` | stur x21,[x28, #-0x8] | `FALL_THROUGH`
<a id="insn-00bad970"></a> `00bad970` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bad974"></a> `00bad974` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bad978"></a> `00bad978` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bad97c"></a> `00bad97c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bad980"></a> `00bad980` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bad984"></a> `00bad984` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bad988"></a> `00bad988` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bad98c"></a> `00bad98c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bad990"></a> `00bad990` | `9f 02 16 eb` | cmp x20,x22 | `FALL_THROUGH`
<a id="insn-00bad994"></a> `00bad994` | `a3 fe ff 54` | b.cc 0x00bad968 | `CONDITIONAL_JUMP`
<a id="insn-00bad998"></a> `00bad998` | `f6 ff ff 17` | b 0x00bad970 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bacfd0`](#insn-00bacfd0) 範囲 `[['00bacfd0', '00bacfe3']]`
  - `FALL_THROUGH` [`00bacfe0`](#insn-00bacfe0) → [`00bacfe4`](#insn-00bacfe4)
- ブロック [`00bacfe4`](#insn-00bacfe4) 範囲 `[['00bacfe4', '00bacff7']]`
  - `FALL_THROUGH` [`00bacff4`](#insn-00bacff4) → [`00bacff8`](#insn-00bacff8)
- ブロック [`00bacff8`](#insn-00bacff8) 範囲 `[['00bacff8', '00bad003']]`
  - `FALL_THROUGH` [`00bad000`](#insn-00bad000) → [`00bad004`](#insn-00bad004)
- ブロック [`00bad004`](#insn-00bad004) 範囲 `[['00bad004', '00bad00b']]`
  - `FALL_THROUGH` [`00bad008`](#insn-00bad008) → [`00bad00c`](#insn-00bad00c)
- ブロック [`00bad00c`](#insn-00bad00c) 範囲 `[['00bad00c', '00bad01f']]`
  - `CONDITIONAL_JUMP` [`00bad01c`](#insn-00bad01c) → [`00bad6b4`](#insn-00bad6b4)
  - `FALL_THROUGH` [`00bad01c`](#insn-00bad01c) → [`00bad020`](#insn-00bad020)
- ブロック [`00bad020`](#insn-00bad020) 範囲 `[['00bad020', '00bad027']]`
  - `FALL_THROUGH` [`00bad024`](#insn-00bad024) → [`00bad028`](#insn-00bad028)
- ブロック [`00bad028`](#insn-00bad028) 範囲 `[['00bad028', '00bad02b']]`
  - `CONDITIONAL_JUMP` [`00bad028`](#insn-00bad028) → [`00bad740`](#insn-00bad740)
  - `FALL_THROUGH` [`00bad028`](#insn-00bad028) → [`00bad02c`](#insn-00bad02c)
- ブロック [`00bad02c`](#insn-00bad02c) 範囲 `[['00bad02c', '00bad04b']]`
  - `CONDITIONAL_JUMP` [`00bad048`](#insn-00bad048) → [`00bad07c`](#insn-00bad07c)
  - `FALL_THROUGH` [`00bad048`](#insn-00bad048) → [`00bad04c`](#insn-00bad04c)
- ブロック [`00bad04c`](#insn-00bad04c) 範囲 `[['00bad04c', '00bad04f']]`
  - `FALL_THROUGH` [`00bad04c`](#insn-00bad04c) → [`00bad050`](#insn-00bad050)
- ブロック [`00bad050`](#insn-00bad050) 範囲 `[['00bad050', '00bad073']]`
  - `FALL_THROUGH` [`00bad070`](#insn-00bad070) → [`00bad074`](#insn-00bad074)
- ブロック [`00bad074`](#insn-00bad074) 範囲 `[['00bad074', '00bad07b']]`
  - `UNCONDITIONAL_JUMP` [`00bad078`](#insn-00bad078) → [`00bad08c`](#insn-00bad08c)
- ブロック [`00bad07c`](#insn-00bad07c) 範囲 `[['00bad07c', '00bad08b']]`
  - `FALL_THROUGH` [`00bad088`](#insn-00bad088) → [`00bad08c`](#insn-00bad08c)
- ブロック [`00bad08c`](#insn-00bad08c) 範囲 `[['00bad08c', '00bad0a3']]`
  - `FALL_THROUGH` [`00bad0a0`](#insn-00bad0a0) → [`00bad0a4`](#insn-00bad0a4)
- ブロック [`00bad0a4`](#insn-00bad0a4) 範囲 `[['00bad0a4', '00bad0af']]`
  - `CONDITIONAL_JUMP` [`00bad0ac`](#insn-00bad0ac) → [`00bad10c`](#insn-00bad10c)
  - `FALL_THROUGH` [`00bad0ac`](#insn-00bad0ac) → [`00bad0b0`](#insn-00bad0b0)
- ブロック [`00bad0b0`](#insn-00bad0b0) 範囲 `[['00bad0b0', '00bad0bb']]`
  - `FALL_THROUGH` [`00bad0b8`](#insn-00bad0b8) → [`00bad0bc`](#insn-00bad0bc)
- ブロック [`00bad0bc`](#insn-00bad0bc) 範囲 `[['00bad0bc', '00bad0df']]`
  - `FALL_THROUGH` [`00bad0dc`](#insn-00bad0dc) → [`00bad0e0`](#insn-00bad0e0)
- ブロック [`00bad0e0`](#insn-00bad0e0) 範囲 `[['00bad0e0', '00bad0e3']]`
  - `CONDITIONAL_JUMP` [`00bad0e0`](#insn-00bad0e0) → [`00bad118`](#insn-00bad118)
  - `FALL_THROUGH` [`00bad0e0`](#insn-00bad0e0) → [`00bad0e4`](#insn-00bad0e4)
- ブロック [`00bad0e4`](#insn-00bad0e4) 範囲 `[['00bad0e4', '00bad103']]`
  - `CONDITIONAL_JUMP` [`00bad100`](#insn-00bad100) → [`00bad118`](#insn-00bad118)
  - `FALL_THROUGH` [`00bad100`](#insn-00bad100) → [`00bad104`](#insn-00bad104)
- ブロック [`00bad104`](#insn-00bad104) 範囲 `[['00bad104', '00bad107']]`
  - `CONDITIONAL_JUMP` [`00bad104`](#insn-00bad104) → [`00bad110`](#insn-00bad110)
  - `FALL_THROUGH` [`00bad104`](#insn-00bad104) → [`00bad108`](#insn-00bad108)
- ブロック [`00bad108`](#insn-00bad108) 範囲 `[['00bad108', '00bad10b']]`
  - `UNCONDITIONAL_JUMP` [`00bad108`](#insn-00bad108) → [`00bad120`](#insn-00bad120)
- ブロック [`00bad10c`](#insn-00bad10c) 範囲 `[['00bad10c', '00bad10f']]`
  - `CONDITIONAL_JUMP` [`00bad10c`](#insn-00bad10c) → [`00bad120`](#insn-00bad120)
  - `FALL_THROUGH` [`00bad10c`](#insn-00bad10c) → [`00bad110`](#insn-00bad110)
- ブロック [`00bad110`](#insn-00bad110) 範囲 `[['00bad110', '00bad117']]`
  - `UNCONDITIONAL_JUMP` [`00bad114`](#insn-00bad114) → [`00bad1d8`](#insn-00bad1d8)
- ブロック [`00bad118`](#insn-00bad118) 範囲 `[['00bad118', '00bad11f']]`
  - `CONDITIONAL_JUMP` [`00bad11c`](#insn-00bad11c) → [`00bad110`](#insn-00bad110)
  - `FALL_THROUGH` [`00bad11c`](#insn-00bad11c) → [`00bad120`](#insn-00bad120)
- ブロック [`00bad120`](#insn-00bad120) 範囲 `[['00bad120', '00bad12b']]`
  - `FALL_THROUGH` [`00bad128`](#insn-00bad128) → [`00bad12c`](#insn-00bad12c)
- ブロック [`00bad12c`](#insn-00bad12c) 範囲 `[['00bad12c', '00bad12f']]`
  - `CONDITIONAL_JUMP` [`00bad12c`](#insn-00bad12c) → [`00bad324`](#insn-00bad324)
  - `FALL_THROUGH` [`00bad12c`](#insn-00bad12c) → [`00bad130`](#insn-00bad130)
- ブロック [`00bad130`](#insn-00bad130) 範囲 `[['00bad130', '00bad13b']]`
  - `UNCONDITIONAL_JUMP` [`00bad138`](#insn-00bad138) → [`00bad14c`](#insn-00bad14c)
- ブロック [`00bad13c`](#insn-00bad13c) 範囲 `[['00bad13c', '00bad13f']]`
  - `CONDITIONAL_JUMP` [`00bad13c`](#insn-00bad13c) → [`00bad1c8`](#insn-00bad1c8)
  - `FALL_THROUGH` [`00bad13c`](#insn-00bad13c) → [`00bad140`](#insn-00bad140)
- ブロック [`00bad140`](#insn-00bad140) 範囲 `[['00bad140', '00bad14b']]`
  - `CONDITIONAL_JUMP` [`00bad148`](#insn-00bad148) → [`00bad324`](#insn-00bad324)
  - `FALL_THROUGH` [`00bad148`](#insn-00bad148) → [`00bad14c`](#insn-00bad14c)
- ブロック [`00bad14c`](#insn-00bad14c) 範囲 `[['00bad14c', '00bad15b']]`
  - `CONDITIONAL_JUMP` [`00bad158`](#insn-00bad158) → [`00bad13c`](#insn-00bad13c)
  - `FALL_THROUGH` [`00bad158`](#insn-00bad158) → [`00bad15c`](#insn-00bad15c)
- ブロック [`00bad15c`](#insn-00bad15c) 範囲 `[['00bad15c', '00bad167']]`
  - `FALL_THROUGH` [`00bad164`](#insn-00bad164) → [`00bad168`](#insn-00bad168)
- ブロック [`00bad168`](#insn-00bad168) 範囲 `[['00bad168', '00bad173']]`
  - `FALL_THROUGH` [`00bad170`](#insn-00bad170) → [`00bad174`](#insn-00bad174)
- ブロック [`00bad174`](#insn-00bad174) 範囲 `[['00bad174', '00bad18f']]`
  - `CONDITIONAL_JUMP` [`00bad18c`](#insn-00bad18c) → [`00bad1bc`](#insn-00bad1bc)
  - `FALL_THROUGH` [`00bad18c`](#insn-00bad18c) → [`00bad190`](#insn-00bad190)
- ブロック [`00bad190`](#insn-00bad190) 範囲 `[['00bad190', '00bad19f']]`
  - `FALL_THROUGH` [`00bad19c`](#insn-00bad19c) → [`00bad1a0`](#insn-00bad1a0)
- ブロック [`00bad1a0`](#insn-00bad1a0) 範囲 `[['00bad1a0', '00bad1af']]`
  - `CONDITIONAL_JUMP` [`00bad1ac`](#insn-00bad1ac) → [`00bad1bc`](#insn-00bad1bc)
  - `FALL_THROUGH` [`00bad1ac`](#insn-00bad1ac) → [`00bad1b0`](#insn-00bad1b0)
- ブロック [`00bad1b0`](#insn-00bad1b0) 範囲 `[['00bad1b0', '00bad1b7']]`
  - `CONDITIONAL_JUMP` [`00bad1b4`](#insn-00bad1b4) → [`00bad140`](#insn-00bad140)
  - `FALL_THROUGH` [`00bad1b4`](#insn-00bad1b4) → [`00bad1b8`](#insn-00bad1b8)
- ブロック [`00bad1b8`](#insn-00bad1b8) 範囲 `[['00bad1b8', '00bad1bb']]`
  - `UNCONDITIONAL_JUMP` [`00bad1b8`](#insn-00bad1b8) → [`00bad1c8`](#insn-00bad1c8)
- ブロック [`00bad1bc`](#insn-00bad1bc) 範囲 `[['00bad1bc', '00bad1c7']]`
  - `CONDITIONAL_JUMP` [`00bad1c4`](#insn-00bad1c4) → [`00bad140`](#insn-00bad140)
  - `FALL_THROUGH` [`00bad1c4`](#insn-00bad1c4) → [`00bad1c8`](#insn-00bad1c8)
- ブロック [`00bad1c8`](#insn-00bad1c8) 範囲 `[['00bad1c8', '00bad1d7']]`
  - `FALL_THROUGH` [`00bad1d4`](#insn-00bad1d4) → [`00bad1d8`](#insn-00bad1d8)
- ブロック [`00bad1d8`](#insn-00bad1d8) 範囲 `[['00bad1d8', '00bad1db']]`
  - `FALL_THROUGH` [`00bad1d8`](#insn-00bad1d8) → [`00bad1dc`](#insn-00bad1dc)
- ブロック [`00bad1dc`](#insn-00bad1dc) 範囲 `[['00bad1dc', '00bad1e7']]`
  - `CONDITIONAL_JUMP` [`00bad1e4`](#insn-00bad1e4) → [`00bad3a0`](#insn-00bad3a0)
  - `FALL_THROUGH` [`00bad1e4`](#insn-00bad1e4) → [`00bad1e8`](#insn-00bad1e8)
- ブロック [`00bad1e8`](#insn-00bad1e8) 範囲 `[['00bad1e8', '00bad1eb']]`
  - `FALL_THROUGH` [`00bad1e8`](#insn-00bad1e8) → [`00bad1ec`](#insn-00bad1ec)
- ブロック [`00bad1ec`](#insn-00bad1ec) 範囲 `[['00bad1ec', '00bad1ff']]`
  - `UNCONDITIONAL_JUMP` [`00bad1fc`](#insn-00bad1fc) → [`00bad208`](#insn-00bad208)
- ブロック [`00bad200`](#insn-00bad200) 範囲 `[['00bad200', '00bad203']]`
  - `CONDITIONAL_JUMP` [`00bad200`](#insn-00bad200) → [`00bad284`](#insn-00bad284)
  - `FALL_THROUGH` [`00bad200`](#insn-00bad200) → [`00bad204`](#insn-00bad204)
- ブロック [`00bad204`](#insn-00bad204) 範囲 `[['00bad204', '00bad207']]`
  - `FALL_THROUGH` [`00bad204`](#insn-00bad204) → [`00bad208`](#insn-00bad208)
- ブロック [`00bad208`](#insn-00bad208) 範囲 `[['00bad208', '00bad217']]`
  - `CONDITIONAL_JUMP` [`00bad214`](#insn-00bad214) → [`00bad200`](#insn-00bad200)
  - `FALL_THROUGH` [`00bad214`](#insn-00bad214) → [`00bad218`](#insn-00bad218)
- ブロック [`00bad218`](#insn-00bad218) 範囲 `[['00bad218', '00bad227']]`
  - `FALL_THROUGH` [`00bad224`](#insn-00bad224) → [`00bad228`](#insn-00bad228)
- ブロック [`00bad228`](#insn-00bad228) 範囲 `[['00bad228', '00bad24b']]`
  - `CONDITIONAL_JUMP` [`00bad248`](#insn-00bad248) → [`00bad274`](#insn-00bad274)
  - `FALL_THROUGH` [`00bad248`](#insn-00bad248) → [`00bad24c`](#insn-00bad24c)
- ブロック [`00bad24c`](#insn-00bad24c) 範囲 `[['00bad24c', '00bad263']]`
  - `FALL_THROUGH` [`00bad260`](#insn-00bad260) → [`00bad264`](#insn-00bad264)
- ブロック [`00bad264`](#insn-00bad264) 範囲 `[['00bad264', '00bad267']]`
  - `FALL_THROUGH` [`00bad264`](#insn-00bad264) → [`00bad268`](#insn-00bad268)
- ブロック [`00bad268`](#insn-00bad268) 範囲 `[['00bad268', '00bad26b']]`
  - `CONDITIONAL_JUMP` [`00bad268`](#insn-00bad268) → [`00bad274`](#insn-00bad274)
  - `FALL_THROUGH` [`00bad268`](#insn-00bad268) → [`00bad26c`](#insn-00bad26c)
- ブロック [`00bad26c`](#insn-00bad26c) 範囲 `[['00bad26c', '00bad26f']]`
  - `CONDITIONAL_JUMP` [`00bad26c`](#insn-00bad26c) → [`00bad204`](#insn-00bad204)
  - `FALL_THROUGH` [`00bad26c`](#insn-00bad26c) → [`00bad270`](#insn-00bad270)
- ブロック [`00bad270`](#insn-00bad270) 範囲 `[['00bad270', '00bad273']]`
  - `UNCONDITIONAL_JUMP` [`00bad270`](#insn-00bad270) → [`00bad284`](#insn-00bad284)
- ブロック [`00bad274`](#insn-00bad274) 範囲 `[['00bad274', '00bad27b']]`
  - `CONDITIONAL_JUMP` [`00bad278`](#insn-00bad278) → [`00bad204`](#insn-00bad204)
  - `FALL_THROUGH` [`00bad278`](#insn-00bad278) → [`00bad27c`](#insn-00bad27c)
- ブロック [`00bad27c`](#insn-00bad27c) 範囲 `[['00bad27c', '00bad27f']]`
  - `UNCONDITIONAL_JUMP` [`00bad27c`](#insn-00bad27c) → [`00bad284`](#insn-00bad284)
- ブロック [`00bad280`](#insn-00bad280) 範囲 `[['00bad280', '00bad283']]`
  - `CONDITIONAL_JUMP` [`00bad280`](#insn-00bad280) → [`00bad2f8`](#insn-00bad2f8)
  - `FALL_THROUGH` [`00bad280`](#insn-00bad280) → [`00bad284`](#insn-00bad284)
- ブロック [`00bad284`](#insn-00bad284) 範囲 `[['00bad284', '00bad28b']]`
  - `FALL_THROUGH` [`00bad288`](#insn-00bad288) → [`00bad28c`](#insn-00bad28c)
- ブロック [`00bad28c`](#insn-00bad28c) 範囲 `[['00bad28c', '00bad28f']]`
  - `FALL_THROUGH` [`00bad28c`](#insn-00bad28c) → [`00bad290`](#insn-00bad290)
- ブロック [`00bad290`](#insn-00bad290) 範囲 `[['00bad290', '00bad293']]`
  - `CONDITIONAL_JUMP` [`00bad290`](#insn-00bad290) → [`00bad280`](#insn-00bad280)
  - `FALL_THROUGH` [`00bad290`](#insn-00bad290) → [`00bad294`](#insn-00bad294)
- ブロック [`00bad294`](#insn-00bad294) 範囲 `[['00bad294', '00bad29b']]`
  - `FALL_THROUGH` [`00bad298`](#insn-00bad298) → [`00bad29c`](#insn-00bad29c)
- ブロック [`00bad29c`](#insn-00bad29c) 範囲 `[['00bad29c', '00bad2b3']]`
  - `FALL_THROUGH` [`00bad2b0`](#insn-00bad2b0) → [`00bad2b4`](#insn-00bad2b4)
- ブロック [`00bad2b4`](#insn-00bad2b4) 範囲 `[['00bad2b4', '00bad2c7']]`
  - `CONDITIONAL_JUMP` [`00bad2c4`](#insn-00bad2c4) → [`00bad2f0`](#insn-00bad2f0)
  - `FALL_THROUGH` [`00bad2c4`](#insn-00bad2c4) → [`00bad2c8`](#insn-00bad2c8)
- ブロック [`00bad2c8`](#insn-00bad2c8) 範囲 `[['00bad2c8', '00bad2cb']]`
  - `FALL_THROUGH` [`00bad2c8`](#insn-00bad2c8) → [`00bad2cc`](#insn-00bad2cc)
- ブロック [`00bad2cc`](#insn-00bad2cc) 範囲 `[['00bad2cc', '00bad2e3']]`
  - `FALL_THROUGH` [`00bad2e0`](#insn-00bad2e0) → [`00bad2e4`](#insn-00bad2e4)
- ブロック [`00bad2e4`](#insn-00bad2e4) 範囲 `[['00bad2e4', '00bad2e7']]`
  - `CONDITIONAL_JUMP` [`00bad2e4`](#insn-00bad2e4) → [`00bad2f0`](#insn-00bad2f0)
  - `FALL_THROUGH` [`00bad2e4`](#insn-00bad2e4) → [`00bad2e8`](#insn-00bad2e8)
- ブロック [`00bad2e8`](#insn-00bad2e8) 範囲 `[['00bad2e8', '00bad2eb']]`
  - `CONDITIONAL_JUMP` [`00bad2e8`](#insn-00bad2e8) → [`00bad284`](#insn-00bad284)
  - `FALL_THROUGH` [`00bad2e8`](#insn-00bad2e8) → [`00bad2ec`](#insn-00bad2ec)
- ブロック [`00bad2ec`](#insn-00bad2ec) 範囲 `[['00bad2ec', '00bad2ef']]`
  - `UNCONDITIONAL_JUMP` [`00bad2ec`](#insn-00bad2ec) → [`00bad2f8`](#insn-00bad2f8)
- ブロック [`00bad2f0`](#insn-00bad2f0) 範囲 `[['00bad2f0', '00bad2f3']]`
  - `FALL_THROUGH` [`00bad2f0`](#insn-00bad2f0) → [`00bad2f4`](#insn-00bad2f4)
- ブロック [`00bad2f4`](#insn-00bad2f4) 範囲 `[['00bad2f4', '00bad2f7']]`
  - `CONDITIONAL_JUMP` [`00bad2f4`](#insn-00bad2f4) → [`00bad284`](#insn-00bad284)
  - `FALL_THROUGH` [`00bad2f4`](#insn-00bad2f4) → [`00bad2f8`](#insn-00bad2f8)
- ブロック [`00bad2f8`](#insn-00bad2f8) 範囲 `[['00bad2f8', '00bad2ff']]`
  - `CONDITIONAL_JUMP` [`00bad2fc`](#insn-00bad2fc) → [`00bad3b0`](#insn-00bad3b0)
  - `FALL_THROUGH` [`00bad2fc`](#insn-00bad2fc) → [`00bad300`](#insn-00bad300)
- ブロック [`00bad300`](#insn-00bad300) 範囲 `[['00bad300', '00bad323']]`
  - `UNCONDITIONAL_JUMP` [`00bad320`](#insn-00bad320) → [`00bad1ec`](#insn-00bad1ec)
- ブロック [`00bad324`](#insn-00bad324) 範囲 `[['00bad324', '00bad33f']]`
  - `CONDITIONAL_JUMP` [`00bad33c`](#insn-00bad33c) → [`00bad49c`](#insn-00bad49c)
  - `FALL_THROUGH` [`00bad33c`](#insn-00bad33c) → [`00bad340`](#insn-00bad340)
- ブロック [`00bad340`](#insn-00bad340) 範囲 `[['00bad340', '00bad34f']]`
  - `FALL_THROUGH` [`00bad34c`](#insn-00bad34c) → [`00bad350`](#insn-00bad350)
- ブロック [`00bad350`](#insn-00bad350) 範囲 `[['00bad350', '00bad357']]`
  - `FALL_THROUGH` [`00bad354`](#insn-00bad354) → [`00bad358`](#insn-00bad358)
- ブロック [`00bad358`](#insn-00bad358) 範囲 `[['00bad358', '00bad35b']]`
  - `FALL_THROUGH` [`00bad358`](#insn-00bad358) → [`00bad35c`](#insn-00bad35c)
- ブロック [`00bad35c`](#insn-00bad35c) 範囲 `[['00bad35c', '00bad35f']]`
  - `FALL_THROUGH` [`00bad35c`](#insn-00bad35c) → [`00bad360`](#insn-00bad360)
- ブロック [`00bad360`](#insn-00bad360) 範囲 `[['00bad360', '00bad363']]`
  - `FALL_THROUGH` [`00bad360`](#insn-00bad360) → [`00bad364`](#insn-00bad364)
- ブロック [`00bad364`](#insn-00bad364) 範囲 `[['00bad364', '00bad367']]`
  - `FALL_THROUGH` [`00bad364`](#insn-00bad364) → [`00bad368`](#insn-00bad368)
- ブロック [`00bad368`](#insn-00bad368) 範囲 `[['00bad368', '00bad36b']]`
  - `FALL_THROUGH` [`00bad368`](#insn-00bad368) → [`00bad36c`](#insn-00bad36c)
- ブロック [`00bad36c`](#insn-00bad36c) 範囲 `[['00bad36c', '00bad36f']]`
  - `FALL_THROUGH` [`00bad36c`](#insn-00bad36c) → [`00bad370`](#insn-00bad370)
- ブロック [`00bad370`](#insn-00bad370) 範囲 `[['00bad370', '00bad377']]`
  - `CONDITIONAL_JUMP` [`00bad374`](#insn-00bad374) → [`00bad4b4`](#insn-00bad4b4)
  - `FALL_THROUGH` [`00bad374`](#insn-00bad374) → [`00bad378`](#insn-00bad378)
- ブロック [`00bad378`](#insn-00bad378) 範囲 `[['00bad378', '00bad383']]`
  - `FALL_THROUGH` [`00bad380`](#insn-00bad380) → [`00bad384`](#insn-00bad384)
- ブロック [`00bad384`](#insn-00bad384) 範囲 `[['00bad384', '00bad38b']]`
  - `FALL_THROUGH` [`00bad388`](#insn-00bad388) → [`00bad38c`](#insn-00bad38c)
- ブロック [`00bad38c`](#insn-00bad38c) 範囲 `[['00bad38c', '00bad38f']]`
  - `FALL_THROUGH` [`00bad38c`](#insn-00bad38c) → [`00bad390`](#insn-00bad390)
- ブロック [`00bad390`](#insn-00bad390) 範囲 `[['00bad390', '00bad397']]`
  - `CONDITIONAL_JUMP` [`00bad394`](#insn-00bad394) → [`00bad4b4`](#insn-00bad4b4)
  - `FALL_THROUGH` [`00bad394`](#insn-00bad394) → [`00bad398`](#insn-00bad398)
- ブロック [`00bad398`](#insn-00bad398) 範囲 `[['00bad398', '00bad39b']]`
  - `CONDITIONAL_JUMP` [`00bad398`](#insn-00bad398) → [`00bad4bc`](#insn-00bad4bc)
  - `FALL_THROUGH` [`00bad398`](#insn-00bad398) → [`00bad39c`](#insn-00bad39c)
- ブロック [`00bad39c`](#insn-00bad39c) 範囲 `[['00bad39c', '00bad39f']]`
  - `UNCONDITIONAL_JUMP` [`00bad39c`](#insn-00bad39c) → [`00bad564`](#insn-00bad564)
- ブロック [`00bad3a0`](#insn-00bad3a0) 範囲 `[['00bad3a0', '00bad3ab']]`
  - `CONDITIONAL_JUMP` [`00bad3a8`](#insn-00bad3a8) → [`00bad3c8`](#insn-00bad3c8)
  - `FALL_THROUGH` [`00bad3a8`](#insn-00bad3a8) → [`00bad3ac`](#insn-00bad3ac)
- ブロック [`00bad3ac`](#insn-00bad3ac) 範囲 `[['00bad3ac', '00bad3af']]`
  - `UNCONDITIONAL_JUMP` [`00bad3ac`](#insn-00bad3ac) → [`00bad44c`](#insn-00bad44c)
- ブロック [`00bad3b0`](#insn-00bad3b0) 範囲 `[['00bad3b0', '00bad3b7']]`
  - `FALL_THROUGH` [`00bad3b4`](#insn-00bad3b4) → [`00bad3b8`](#insn-00bad3b8)
- ブロック [`00bad3b8`](#insn-00bad3b8) 範囲 `[['00bad3b8', '00bad3bb']]`
  - `FALL_THROUGH` [`00bad3b8`](#insn-00bad3b8) → [`00bad3bc`](#insn-00bad3bc)
- ブロック [`00bad3bc`](#insn-00bad3bc) 範囲 `[['00bad3bc', '00bad3c7']]`
  - `CONDITIONAL_JUMP` [`00bad3c4`](#insn-00bad3c4) → [`00bad44c`](#insn-00bad44c)
  - `FALL_THROUGH` [`00bad3c4`](#insn-00bad3c4) → [`00bad3c8`](#insn-00bad3c8)
- ブロック [`00bad3c8`](#insn-00bad3c8) 範囲 `[['00bad3c8', '00bad3df']]`
  - `CONDITIONAL_JUMP` [`00bad3dc`](#insn-00bad3dc) → [`00bad43c`](#insn-00bad43c)
  - `FALL_THROUGH` [`00bad3dc`](#insn-00bad3dc) → [`00bad3e0`](#insn-00bad3e0)
- ブロック [`00bad3e0`](#insn-00bad3e0) 範囲 `[['00bad3e0', '00bad3ef']]`
  - `FALL_THROUGH` [`00bad3ec`](#insn-00bad3ec) → [`00bad3f0`](#insn-00bad3f0)
- ブロック [`00bad3f0`](#insn-00bad3f0) 範囲 `[['00bad3f0', '00bad3ff']]`
  - `FALL_THROUGH` [`00bad3fc`](#insn-00bad3fc) → [`00bad400`](#insn-00bad400)
- ブロック [`00bad400`](#insn-00bad400) 範囲 `[['00bad400', '00bad413']]`
  - `CONDITIONAL_JUMP` [`00bad410`](#insn-00bad410) → [`00bad4a8`](#insn-00bad4a8)
  - `FALL_THROUGH` [`00bad410`](#insn-00bad410) → [`00bad414`](#insn-00bad414)
- ブロック [`00bad414`](#insn-00bad414) 範囲 `[['00bad414', '00bad41f']]`
  - `FALL_THROUGH` [`00bad41c`](#insn-00bad41c) → [`00bad420`](#insn-00bad420)
- ブロック [`00bad420`](#insn-00bad420) 範囲 `[['00bad420', '00bad423']]`
  - `FALL_THROUGH` [`00bad420`](#insn-00bad420) → [`00bad424`](#insn-00bad424)
- ブロック [`00bad424`](#insn-00bad424) 範囲 `[['00bad424', '00bad433']]`
  - `CONDITIONAL_JUMP` [`00bad430`](#insn-00bad430) → [`00bad4a8`](#insn-00bad4a8)
  - `FALL_THROUGH` [`00bad430`](#insn-00bad430) → [`00bad434`](#insn-00bad434)
- ブロック [`00bad434`](#insn-00bad434) 範囲 `[['00bad434', '00bad437']]`
  - `CONDITIONAL_JUMP` [`00bad434`](#insn-00bad434) → [`00bad440`](#insn-00bad440)
  - `FALL_THROUGH` [`00bad434`](#insn-00bad434) → [`00bad438`](#insn-00bad438)
- ブロック [`00bad438`](#insn-00bad438) 範囲 `[['00bad438', '00bad43b']]`
  - `UNCONDITIONAL_JUMP` [`00bad438`](#insn-00bad438) → [`00bad44c`](#insn-00bad44c)
- ブロック [`00bad43c`](#insn-00bad43c) 範囲 `[['00bad43c', '00bad43f']]`
  - `CONDITIONAL_JUMP` [`00bad43c`](#insn-00bad43c) → [`00bad44c`](#insn-00bad44c)
  - `FALL_THROUGH` [`00bad43c`](#insn-00bad43c) → [`00bad440`](#insn-00bad440)
- ブロック [`00bad440`](#insn-00bad440) 範囲 `[['00bad440', '00bad44b']]`
  - `FALL_THROUGH` [`00bad448`](#insn-00bad448) → [`00bad44c`](#insn-00bad44c)
- ブロック [`00bad44c`](#insn-00bad44c) 範囲 `[['00bad44c', '00bad44f']]`
  - `CONDITIONAL_JUMP` [`00bad44c`](#insn-00bad44c) → [`00bad478`](#insn-00bad478)
  - `FALL_THROUGH` [`00bad44c`](#insn-00bad44c) → [`00bad450`](#insn-00bad450)
- ブロック [`00bad450`](#insn-00bad450) 範囲 `[['00bad450', '00bad473']]`
  - `CONDITIONAL_JUMP` [`00bad470`](#insn-00bad470) → [`00bad6a8`](#insn-00bad6a8)
  - `FALL_THROUGH` [`00bad470`](#insn-00bad470) → [`00bad474`](#insn-00bad474)
- ブロック [`00bad474`](#insn-00bad474) 範囲 `[['00bad474', '00bad477']]`
  - `CONDITIONAL_JUMP` [`00bad474`](#insn-00bad474) → [`00bad00c`](#insn-00bad00c)
  - `FALL_THROUGH` [`00bad474`](#insn-00bad474) → [`00bad478`](#insn-00bad478)
- ブロック [`00bad478`](#insn-00bad478) 範囲 `[['00bad478', '00bad487']]`
  - `CONDITIONAL_JUMP` [`00bad484`](#insn-00bad484) → [`00bad694`](#insn-00bad694)
  - `FALL_THROUGH` [`00bad484`](#insn-00bad484) → [`00bad488`](#insn-00bad488)
- ブロック [`00bad488`](#insn-00bad488) 範囲 `[['00bad488', '00bad497']]`
  - `FALL_THROUGH` [`00bad494`](#insn-00bad494) → [`00bad498`](#insn-00bad498)
- ブロック [`00bad498`](#insn-00bad498) 範囲 `[['00bad498', '00bad49b']]`
  - `UNCONDITIONAL_JUMP` [`00bad498`](#insn-00bad498) → [`00bad00c`](#insn-00bad00c)
- ブロック [`00bad49c`](#insn-00bad49c) 範囲 `[['00bad49c', '00bad49f']]`
  - `FALL_THROUGH` [`00bad49c`](#insn-00bad49c) → [`00bad4a0`](#insn-00bad4a0)
- ブロック [`00bad4a0`](#insn-00bad4a0) 範囲 `[['00bad4a0', '00bad4a3']]`
  - `CONDITIONAL_JUMP` [`00bad4a0`](#insn-00bad4a0) → [`00bad4bc`](#insn-00bad4bc)
  - `FALL_THROUGH` [`00bad4a0`](#insn-00bad4a0) → [`00bad4a4`](#insn-00bad4a4)
- ブロック [`00bad4a4`](#insn-00bad4a4) 範囲 `[['00bad4a4', '00bad4a7']]`
  - `UNCONDITIONAL_JUMP` [`00bad4a4`](#insn-00bad4a4) → [`00bad564`](#insn-00bad564)
- ブロック [`00bad4a8`](#insn-00bad4a8) 範囲 `[['00bad4a8', '00bad4af']]`
  - `CONDITIONAL_JUMP` [`00bad4ac`](#insn-00bad4ac) → [`00bad440`](#insn-00bad440)
  - `FALL_THROUGH` [`00bad4ac`](#insn-00bad4ac) → [`00bad4b0`](#insn-00bad4b0)
- ブロック [`00bad4b0`](#insn-00bad4b0) 範囲 `[['00bad4b0', '00bad4b3']]`
  - `UNCONDITIONAL_JUMP` [`00bad4b0`](#insn-00bad4b0) → [`00bad44c`](#insn-00bad44c)
- ブロック [`00bad4b4`](#insn-00bad4b4) 範囲 `[['00bad4b4', '00bad4bb']]`
  - `CONDITIONAL_JUMP` [`00bad4b8`](#insn-00bad4b8) → [`00bad564`](#insn-00bad564)
  - `FALL_THROUGH` [`00bad4b8`](#insn-00bad4b8) → [`00bad4bc`](#insn-00bad4bc)
- ブロック [`00bad4bc`](#insn-00bad4bc) 範囲 `[['00bad4bc', '00bad4c7']]`
  - `CONDITIONAL_JUMP` [`00bad4c4`](#insn-00bad4c4) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad4c4`](#insn-00bad4c4) → [`00bad4c8`](#insn-00bad4c8)
- ブロック [`00bad4c8`](#insn-00bad4c8) 範囲 `[['00bad4c8', '00bad4d3']]`
  - `UNCONDITIONAL_JUMP` [`00bad4d0`](#insn-00bad4d0) → [`00bad4e4`](#insn-00bad4e4)
- ブロック [`00bad4d4`](#insn-00bad4d4) 範囲 `[['00bad4d4', '00bad4d7']]`
  - `CONDITIONAL_JUMP` [`00bad4d4`](#insn-00bad4d4) → [`00bad558`](#insn-00bad558)
  - `FALL_THROUGH` [`00bad4d4`](#insn-00bad4d4) → [`00bad4d8`](#insn-00bad4d8)
- ブロック [`00bad4d8`](#insn-00bad4d8) 範囲 `[['00bad4d8', '00bad4e3']]`
  - `CONDITIONAL_JUMP` [`00bad4e0`](#insn-00bad4e0) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad4e0`](#insn-00bad4e0) → [`00bad4e4`](#insn-00bad4e4)
- ブロック [`00bad4e4`](#insn-00bad4e4) 範囲 `[['00bad4e4', '00bad4f3']]`
  - `CONDITIONAL_JUMP` [`00bad4f0`](#insn-00bad4f0) → [`00bad4d4`](#insn-00bad4d4)
  - `FALL_THROUGH` [`00bad4f0`](#insn-00bad4f0) → [`00bad4f4`](#insn-00bad4f4)
- ブロック [`00bad4f4`](#insn-00bad4f4) 範囲 `[['00bad4f4', '00bad507']]`
  - `FALL_THROUGH` [`00bad504`](#insn-00bad504) → [`00bad508`](#insn-00bad508)
- ブロック [`00bad508`](#insn-00bad508) 範囲 `[['00bad508', '00bad51f']]`
  - `FALL_THROUGH` [`00bad51c`](#insn-00bad51c) → [`00bad520`](#insn-00bad520)
- ブロック [`00bad520`](#insn-00bad520) 範囲 `[['00bad520', '00bad527']]`
  - `CONDITIONAL_JUMP` [`00bad524`](#insn-00bad524) → [`00bad550`](#insn-00bad550)
  - `FALL_THROUGH` [`00bad524`](#insn-00bad524) → [`00bad528`](#insn-00bad528)
- ブロック [`00bad528`](#insn-00bad528) 範囲 `[['00bad528', '00bad547']]`
  - `CONDITIONAL_JUMP` [`00bad544`](#insn-00bad544) → [`00bad550`](#insn-00bad550)
  - `FALL_THROUGH` [`00bad544`](#insn-00bad544) → [`00bad548`](#insn-00bad548)
- ブロック [`00bad548`](#insn-00bad548) 範囲 `[['00bad548', '00bad54b']]`
  - `CONDITIONAL_JUMP` [`00bad548`](#insn-00bad548) → [`00bad4d8`](#insn-00bad4d8)
  - `FALL_THROUGH` [`00bad548`](#insn-00bad548) → [`00bad54c`](#insn-00bad54c)
- ブロック [`00bad54c`](#insn-00bad54c) 範囲 `[['00bad54c', '00bad54f']]`
  - `UNCONDITIONAL_JUMP` [`00bad54c`](#insn-00bad54c) → [`00bad558`](#insn-00bad558)
- ブロック [`00bad550`](#insn-00bad550) 範囲 `[['00bad550', '00bad557']]`
  - `CONDITIONAL_JUMP` [`00bad554`](#insn-00bad554) → [`00bad4d8`](#insn-00bad4d8)
  - `FALL_THROUGH` [`00bad554`](#insn-00bad554) → [`00bad558`](#insn-00bad558)
- ブロック [`00bad558`](#insn-00bad558) 範囲 `[['00bad558', '00bad563']]`
  - `FALL_THROUGH` [`00bad560`](#insn-00bad560) → [`00bad564`](#insn-00bad564)
- ブロック [`00bad564`](#insn-00bad564) 範囲 `[['00bad564', '00bad56b']]`
  - `FALL_THROUGH` [`00bad568`](#insn-00bad568) → [`00bad56c`](#insn-00bad56c)
- ブロック [`00bad56c`](#insn-00bad56c) 範囲 `[['00bad56c', '00bad56f']]`
  - `CONDITIONAL_JUMP` [`00bad56c`](#insn-00bad56c) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad56c`](#insn-00bad56c) → [`00bad570`](#insn-00bad570)
- ブロック [`00bad570`](#insn-00bad570) 範囲 `[['00bad570', '00bad573']]`
  - `FALL_THROUGH` [`00bad570`](#insn-00bad570) → [`00bad574`](#insn-00bad574)
- ブロック [`00bad574`](#insn-00bad574) 範囲 `[['00bad574', '00bad577']]`
  - `FALL_THROUGH` [`00bad574`](#insn-00bad574) → [`00bad578`](#insn-00bad578)
- ブロック [`00bad578`](#insn-00bad578) 範囲 `[['00bad578', '00bad583']]`
  - `UNCONDITIONAL_JUMP` [`00bad580`](#insn-00bad580) → [`00bad58c`](#insn-00bad58c)
- ブロック [`00bad584`](#insn-00bad584) 範囲 `[['00bad584', '00bad587']]`
  - `CONDITIONAL_JUMP` [`00bad584`](#insn-00bad584) → [`00bad608`](#insn-00bad608)
  - `FALL_THROUGH` [`00bad584`](#insn-00bad584) → [`00bad588`](#insn-00bad588)
- ブロック [`00bad588`](#insn-00bad588) 範囲 `[['00bad588', '00bad58b']]`
  - `FALL_THROUGH` [`00bad588`](#insn-00bad588) → [`00bad58c`](#insn-00bad58c)
- ブロック [`00bad58c`](#insn-00bad58c) 範囲 `[['00bad58c', '00bad59b']]`
  - `CONDITIONAL_JUMP` [`00bad598`](#insn-00bad598) → [`00bad584`](#insn-00bad584)
  - `FALL_THROUGH` [`00bad598`](#insn-00bad598) → [`00bad59c`](#insn-00bad59c)
- ブロック [`00bad59c`](#insn-00bad59c) 範囲 `[['00bad59c', '00bad5b7']]`
  - `FALL_THROUGH` [`00bad5b4`](#insn-00bad5b4) → [`00bad5b8`](#insn-00bad5b8)
- ブロック [`00bad5b8`](#insn-00bad5b8) 範囲 `[['00bad5b8', '00bad5cf']]`
  - `CONDITIONAL_JUMP` [`00bad5cc`](#insn-00bad5cc) → [`00bad5f8`](#insn-00bad5f8)
  - `FALL_THROUGH` [`00bad5cc`](#insn-00bad5cc) → [`00bad5d0`](#insn-00bad5d0)
- ブロック [`00bad5d0`](#insn-00bad5d0) 範囲 `[['00bad5d0', '00bad5e3']]`
  - `FALL_THROUGH` [`00bad5e0`](#insn-00bad5e0) → [`00bad5e4`](#insn-00bad5e4)
- ブロック [`00bad5e4`](#insn-00bad5e4) 範囲 `[['00bad5e4', '00bad5ef']]`
  - `CONDITIONAL_JUMP` [`00bad5ec`](#insn-00bad5ec) → [`00bad5f8`](#insn-00bad5f8)
  - `FALL_THROUGH` [`00bad5ec`](#insn-00bad5ec) → [`00bad5f0`](#insn-00bad5f0)
- ブロック [`00bad5f0`](#insn-00bad5f0) 範囲 `[['00bad5f0', '00bad5f3']]`
  - `CONDITIONAL_JUMP` [`00bad5f0`](#insn-00bad5f0) → [`00bad588`](#insn-00bad588)
  - `FALL_THROUGH` [`00bad5f0`](#insn-00bad5f0) → [`00bad5f4`](#insn-00bad5f4)
- ブロック [`00bad5f4`](#insn-00bad5f4) 範囲 `[['00bad5f4', '00bad5f7']]`
  - `UNCONDITIONAL_JUMP` [`00bad5f4`](#insn-00bad5f4) → [`00bad608`](#insn-00bad608)
- ブロック [`00bad5f8`](#insn-00bad5f8) 範囲 `[['00bad5f8', '00bad5ff']]`
  - `CONDITIONAL_JUMP` [`00bad5fc`](#insn-00bad5fc) → [`00bad588`](#insn-00bad588)
  - `FALL_THROUGH` [`00bad5fc`](#insn-00bad5fc) → [`00bad600`](#insn-00bad600)
- ブロック [`00bad600`](#insn-00bad600) 範囲 `[['00bad600', '00bad603']]`
  - `UNCONDITIONAL_JUMP` [`00bad600`](#insn-00bad600) → [`00bad608`](#insn-00bad608)
- ブロック [`00bad604`](#insn-00bad604) 範囲 `[['00bad604', '00bad607']]`
  - `CONDITIONAL_JUMP` [`00bad604`](#insn-00bad604) → [`00bad67c`](#insn-00bad67c)
  - `FALL_THROUGH` [`00bad604`](#insn-00bad604) → [`00bad608`](#insn-00bad608)
- ブロック [`00bad608`](#insn-00bad608) 範囲 `[['00bad608', '00bad617']]`
  - `CONDITIONAL_JUMP` [`00bad614`](#insn-00bad614) → [`00bad604`](#insn-00bad604)
  - `FALL_THROUGH` [`00bad614`](#insn-00bad614) → [`00bad618`](#insn-00bad618)
- ブロック [`00bad618`](#insn-00bad618) 範囲 `[['00bad618', '00bad64b']]`
  - `CONDITIONAL_JUMP` [`00bad648`](#insn-00bad648) → [`00bad674`](#insn-00bad674)
  - `FALL_THROUGH` [`00bad648`](#insn-00bad648) → [`00bad64c`](#insn-00bad64c)
- ブロック [`00bad64c`](#insn-00bad64c) 範囲 `[['00bad64c', '00bad66b']]`
  - `CONDITIONAL_JUMP` [`00bad668`](#insn-00bad668) → [`00bad674`](#insn-00bad674)
  - `FALL_THROUGH` [`00bad668`](#insn-00bad668) → [`00bad66c`](#insn-00bad66c)
- ブロック [`00bad66c`](#insn-00bad66c) 範囲 `[['00bad66c', '00bad66f']]`
  - `CONDITIONAL_JUMP` [`00bad66c`](#insn-00bad66c) → [`00bad608`](#insn-00bad608)
  - `FALL_THROUGH` [`00bad66c`](#insn-00bad66c) → [`00bad670`](#insn-00bad670)
- ブロック [`00bad670`](#insn-00bad670) 範囲 `[['00bad670', '00bad673']]`
  - `UNCONDITIONAL_JUMP` [`00bad670`](#insn-00bad670) → [`00bad67c`](#insn-00bad67c)
- ブロック [`00bad674`](#insn-00bad674) 範囲 `[['00bad674', '00bad67b']]`
  - `CONDITIONAL_JUMP` [`00bad678`](#insn-00bad678) → [`00bad608`](#insn-00bad608)
  - `FALL_THROUGH` [`00bad678`](#insn-00bad678) → [`00bad67c`](#insn-00bad67c)
- ブロック [`00bad67c`](#insn-00bad67c) 範囲 `[['00bad67c', '00bad683']]`
  - `CONDITIONAL_JUMP` [`00bad680`](#insn-00bad680) → [`00bad00c`](#insn-00bad00c)
  - `FALL_THROUGH` [`00bad680`](#insn-00bad680) → [`00bad684`](#insn-00bad684)
- ブロック [`00bad684`](#insn-00bad684) 範囲 `[['00bad684', '00bad693']]`
  - `UNCONDITIONAL_JUMP` [`00bad690`](#insn-00bad690) → [`00bad574`](#insn-00bad574)
- ブロック [`00bad694`](#insn-00bad694) 範囲 `[['00bad694', '00bad6a7']]`
  - `UNCONDITIONAL_JUMP` [`00bad6a4`](#insn-00bad6a4) → [`00bacff8`](#insn-00bacff8)
- ブロック [`00bad6a8`](#insn-00bad6a8) 範囲 `[['00bad6a8', '00bad6af']]`
  - `CONDITIONAL_JUMP` [`00bad6ac`](#insn-00bad6ac) → [`00bacff8`](#insn-00bacff8)
  - `FALL_THROUGH` [`00bad6ac`](#insn-00bad6ac) → [`00bad6b0`](#insn-00bad6b0)
- ブロック [`00bad6b0`](#insn-00bad6b0) 範囲 `[['00bad6b0', '00bad6b3']]`
  - `UNCONDITIONAL_JUMP` [`00bad6b0`](#insn-00bad6b0) → [`00bad970`](#insn-00bad970)
- ブロック [`00bad6b4`](#insn-00bad6b4) 範囲 `[['00bad6b4', '00bad6c7']]`
  - `FALL_THROUGH` [`00bad6c4`](#insn-00bad6c4) → [`00bad6c8`](#insn-00bad6c8)
- ブロック [`00bad6c8`](#insn-00bad6c8) 範囲 `[['00bad6c8', '00bad6cb']]`
  - `COMPUTED_JUMP` [`00bad6c8`](#insn-00bad6c8) → [`00bad970`](#insn-00bad970)
  - `COMPUTED_JUMP` [`00bad6c8`](#insn-00bad6c8) → [`00bad6cc`](#insn-00bad6cc)
  - `COMPUTED_JUMP` [`00bad6c8`](#insn-00bad6c8) → [`00bad8d4`](#insn-00bad8d4)
  - `COMPUTED_JUMP` [`00bad6c8`](#insn-00bad6c8) → [`00bad900`](#insn-00bad900)
  - `COMPUTED_JUMP` [`00bad6c8`](#insn-00bad6c8) → [`00bad930`](#insn-00bad930)
- ブロック [`00bad6cc`](#insn-00bad6cc) 範囲 `[['00bad6cc', '00bad6e3']]`
  - `CONDITIONAL_JUMP` [`00bad6e0`](#insn-00bad6e0) → [`00bad964`](#insn-00bad964)
  - `FALL_THROUGH` [`00bad6e0`](#insn-00bad6e0) → [`00bad6e4`](#insn-00bad6e4)
- ブロック [`00bad6e4`](#insn-00bad6e4) 範囲 `[['00bad6e4', '00bad6ff']]`
  - `FALL_THROUGH` [`00bad6fc`](#insn-00bad6fc) → [`00bad700`](#insn-00bad700)
- ブロック [`00bad700`](#insn-00bad700) 範囲 `[['00bad700', '00bad717']]`
  - `CONDITIONAL_JUMP` [`00bad714`](#insn-00bad714) → [`00bad990`](#insn-00bad990)
  - `FALL_THROUGH` [`00bad714`](#insn-00bad714) → [`00bad718`](#insn-00bad718)
- ブロック [`00bad718`](#insn-00bad718) 範囲 `[['00bad718', '00bad737']]`
  - `CONDITIONAL_JUMP` [`00bad734`](#insn-00bad734) → [`00bad990`](#insn-00bad990)
  - `FALL_THROUGH` [`00bad734`](#insn-00bad734) → [`00bad738`](#insn-00bad738)
- ブロック [`00bad738`](#insn-00bad738) 範囲 `[['00bad738', '00bad73b']]`
  - `CONDITIONAL_JUMP` [`00bad738`](#insn-00bad738) → [`00bad968`](#insn-00bad968)
  - `FALL_THROUGH` [`00bad738`](#insn-00bad738) → [`00bad73c`](#insn-00bad73c)
- ブロック [`00bad73c`](#insn-00bad73c) 範囲 `[['00bad73c', '00bad73f']]`
  - `UNCONDITIONAL_JUMP` [`00bad73c`](#insn-00bad73c) → [`00bad970`](#insn-00bad970)
- ブロック [`00bad740`](#insn-00bad740) 範囲 `[['00bad740', '00bad75f']]`
  - `CONDITIONAL_JUMP` [`00bad75c`](#insn-00bad75c) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad75c`](#insn-00bad75c) → [`00bad760`](#insn-00bad760)
- ブロック [`00bad760`](#insn-00bad760) 範囲 `[['00bad760', '00bad767']]`
  - `UNCONDITIONAL_JUMP` [`00bad764`](#insn-00bad764) → [`00bad784`](#insn-00bad784)
- ブロック [`00bad768`](#insn-00bad768) 範囲 `[['00bad768', '00bad76b']]`
  - `FALL_THROUGH` [`00bad768`](#insn-00bad768) → [`00bad76c`](#insn-00bad76c)
- ブロック [`00bad76c`](#insn-00bad76c) 範囲 `[['00bad76c', '00bad76f']]`
  - `FALL_THROUGH` [`00bad76c`](#insn-00bad76c) → [`00bad770`](#insn-00bad770)
- ブロック [`00bad770`](#insn-00bad770) 範囲 `[['00bad770', '00bad773']]`
  - `FALL_THROUGH` [`00bad770`](#insn-00bad770) → [`00bad774`](#insn-00bad774)
- ブロック [`00bad774`](#insn-00bad774) 範囲 `[['00bad774', '00bad783']]`
  - `CONDITIONAL_JUMP` [`00bad780`](#insn-00bad780) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad780`](#insn-00bad780) → [`00bad784`](#insn-00bad784)
- ブロック [`00bad784`](#insn-00bad784) 範囲 `[['00bad784', '00bad7a3']]`
  - `CONDITIONAL_JUMP` [`00bad7a0`](#insn-00bad7a0) → [`00bad800`](#insn-00bad800)
  - `FALL_THROUGH` [`00bad7a0`](#insn-00bad7a0) → [`00bad7a4`](#insn-00bad7a4)
- ブロック [`00bad7a4`](#insn-00bad7a4) 範囲 `[['00bad7a4', '00bad7d7']]`
  - `CONDITIONAL_JUMP` [`00bad7d4`](#insn-00bad7d4) → [`00bad808`](#insn-00bad808)
  - `FALL_THROUGH` [`00bad7d4`](#insn-00bad7d4) → [`00bad7d8`](#insn-00bad7d8)
- ブロック [`00bad7d8`](#insn-00bad7d8) 範囲 `[['00bad7d8', '00bad7eb']]`
  - `FALL_THROUGH` [`00bad7e8`](#insn-00bad7e8) → [`00bad7ec`](#insn-00bad7ec)
- ブロック [`00bad7ec`](#insn-00bad7ec) 範囲 `[['00bad7ec', '00bad7f7']]`
  - `CONDITIONAL_JUMP` [`00bad7f4`](#insn-00bad7f4) → [`00bad808`](#insn-00bad808)
  - `FALL_THROUGH` [`00bad7f4`](#insn-00bad7f4) → [`00bad7f8`](#insn-00bad7f8)
- ブロック [`00bad7f8`](#insn-00bad7f8) 範囲 `[['00bad7f8', '00bad7fb']]`
  - `CONDITIONAL_JUMP` [`00bad7f8`](#insn-00bad7f8) → [`00bad774`](#insn-00bad774)
  - `FALL_THROUGH` [`00bad7f8`](#insn-00bad7f8) → [`00bad7fc`](#insn-00bad7fc)
- ブロック [`00bad7fc`](#insn-00bad7fc) 範囲 `[['00bad7fc', '00bad7ff']]`
  - `UNCONDITIONAL_JUMP` [`00bad7fc`](#insn-00bad7fc) → [`00bad810`](#insn-00bad810)
- ブロック [`00bad800`](#insn-00bad800) 範囲 `[['00bad800', '00bad803']]`
  - `CONDITIONAL_JUMP` [`00bad800`](#insn-00bad800) → [`00bad774`](#insn-00bad774)
  - `FALL_THROUGH` [`00bad800`](#insn-00bad800) → [`00bad804`](#insn-00bad804)
- ブロック [`00bad804`](#insn-00bad804) 範囲 `[['00bad804', '00bad807']]`
  - `UNCONDITIONAL_JUMP` [`00bad804`](#insn-00bad804) → [`00bad810`](#insn-00bad810)
- ブロック [`00bad808`](#insn-00bad808) 範囲 `[['00bad808', '00bad80f']]`
  - `CONDITIONAL_JUMP` [`00bad80c`](#insn-00bad80c) → [`00bad774`](#insn-00bad774)
  - `FALL_THROUGH` [`00bad80c`](#insn-00bad80c) → [`00bad810`](#insn-00bad810)
- ブロック [`00bad810`](#insn-00bad810) 範囲 `[['00bad810', '00bad81b']]`
  - `CONDITIONAL_JUMP` [`00bad818`](#insn-00bad818) → [`00bad770`](#insn-00bad770)
  - `FALL_THROUGH` [`00bad818`](#insn-00bad818) → [`00bad81c`](#insn-00bad81c)
- ブロック [`00bad81c`](#insn-00bad81c) 範囲 `[['00bad81c', '00bad82b']]`
  - `UNCONDITIONAL_JUMP` [`00bad828`](#insn-00bad828) → [`00bad844`](#insn-00bad844)
- ブロック [`00bad82c`](#insn-00bad82c) 範囲 `[['00bad82c', '00bad82f']]`
  - `CONDITIONAL_JUMP` [`00bad82c`](#insn-00bad82c) → [`00bad76c`](#insn-00bad76c)
  - `FALL_THROUGH` [`00bad82c`](#insn-00bad82c) → [`00bad830`](#insn-00bad830)
- ブロック [`00bad830`](#insn-00bad830) 範囲 `[['00bad830', '00bad843']]`
  - `CONDITIONAL_JUMP` [`00bad840`](#insn-00bad840) → [`00bad768`](#insn-00bad768)
  - `FALL_THROUGH` [`00bad840`](#insn-00bad840) → [`00bad844`](#insn-00bad844)
- ブロック [`00bad844`](#insn-00bad844) 範囲 `[['00bad844', '00bad857']]`
  - `CONDITIONAL_JUMP` [`00bad854`](#insn-00bad854) → [`00bad82c`](#insn-00bad82c)
  - `FALL_THROUGH` [`00bad854`](#insn-00bad854) → [`00bad858`](#insn-00bad858)
- ブロック [`00bad858`](#insn-00bad858) 範囲 `[['00bad858', '00bad88b']]`
  - `CONDITIONAL_JUMP` [`00bad888`](#insn-00bad888) → [`00bad8bc`](#insn-00bad8bc)
  - `FALL_THROUGH` [`00bad888`](#insn-00bad888) → [`00bad88c`](#insn-00bad88c)
- ブロック [`00bad88c`](#insn-00bad88c) 範囲 `[['00bad88c', '00bad8af']]`
  - `CONDITIONAL_JUMP` [`00bad8ac`](#insn-00bad8ac) → [`00bad8bc`](#insn-00bad8bc)
  - `FALL_THROUGH` [`00bad8ac`](#insn-00bad8ac) → [`00bad8b0`](#insn-00bad8b0)
- ブロック [`00bad8b0`](#insn-00bad8b0) 範囲 `[['00bad8b0', '00bad8b7']]`
  - `CONDITIONAL_JUMP` [`00bad8b4`](#insn-00bad8b4) → [`00bad830`](#insn-00bad830)
  - `FALL_THROUGH` [`00bad8b4`](#insn-00bad8b4) → [`00bad8b8`](#insn-00bad8b8)
- ブロック [`00bad8b8`](#insn-00bad8b8) 範囲 `[['00bad8b8', '00bad8bb']]`
  - `UNCONDITIONAL_JUMP` [`00bad8b8`](#insn-00bad8b8) → [`00bad76c`](#insn-00bad76c)
- ブロック [`00bad8bc`](#insn-00bad8bc) 範囲 `[['00bad8bc', '00bad8c7']]`
  - `CONDITIONAL_JUMP` [`00bad8c4`](#insn-00bad8c4) → [`00bad830`](#insn-00bad830)
  - `FALL_THROUGH` [`00bad8c4`](#insn-00bad8c4) → [`00bad8c8`](#insn-00bad8c8)
- ブロック [`00bad8c8`](#insn-00bad8c8) 範囲 `[['00bad8c8', '00bad8d3']]`
  - `UNCONDITIONAL_JUMP` [`00bad8d0`](#insn-00bad8d0) → [`00bad76c`](#insn-00bad76c)
- ブロック [`00bad8d4`](#insn-00bad8d4) 範囲 `[['00bad8d4', '00bad8df']]`
  - `FALL_THROUGH` [`00bad8dc`](#insn-00bad8dc) → [`00bad8e0`](#insn-00bad8e0)
- ブロック [`00bad8e0`](#insn-00bad8e0) 範囲 `[['00bad8e0', '00bad8ff']]`
- ブロック [`00bad900`](#insn-00bad900) 範囲 `[['00bad900', '00bad92f']]`
- ブロック [`00bad930`](#insn-00bad930) 範囲 `[['00bad930', '00bad963']]`
- ブロック [`00bad964`](#insn-00bad964) 範囲 `[['00bad964', '00bad967']]`
  - `CONDITIONAL_JUMP` [`00bad964`](#insn-00bad964) → [`00bad970`](#insn-00bad970)
  - `FALL_THROUGH` [`00bad964`](#insn-00bad964) → [`00bad968`](#insn-00bad968)
- ブロック [`00bad968`](#insn-00bad968) 範囲 `[['00bad968', '00bad96f']]`
  - `FALL_THROUGH` [`00bad96c`](#insn-00bad96c) → [`00bad970`](#insn-00bad970)
- ブロック [`00bad970`](#insn-00bad970) 範囲 `[['00bad970', '00bad98f']]`
- ブロック [`00bad990`](#insn-00bad990) 範囲 `[['00bad990', '00bad997']]`
  - `CONDITIONAL_JUMP` [`00bad994`](#insn-00bad994) → [`00bad968`](#insn-00bad968)
  - `FALL_THROUGH` [`00bad994`](#insn-00bad994) → [`00bad998`](#insn-00bad998)
- ブロック [`00bad998`](#insn-00bad998) 範囲 `[['00bad998', '00bad99b']]`
  - `UNCONDITIONAL_JUMP` [`00bad998`](#insn-00bad998) → [`00bad970`](#insn-00bad970)

## 命令位置別の参照

- [`00bacfd4`](#insn-00bacfd4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfd8`](#insn-00bacfd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfdc`](#insn-00bacfdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfe0`](#insn-00bacfe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfe4`](#insn-00bacfe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacfe8`](#insn-00bacfe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacffc`](#insn-00bacffc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad008`](#insn-00bad008) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad01c`](#insn-00bad01c) → [`00bad6b4`](#insn-00bad6b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad024`](#insn-00bad024) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad028`](#insn-00bad028) → [`00bad740`](#insn-00bad740) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad048`](#insn-00bad048) → [`00bad07c`](#insn-00bad07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad058`](#insn-00bad058) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad074`](#insn-00bad074) → [`00bade50`](../00bad/00bade50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bade50` · 推定シンボル `None` · 推定型 `None`
- [`00bad078`](#insn-00bad078) → [`00bad08c`](#insn-00bad08c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad07c`](#insn-00bad07c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad088`](#insn-00bad088) → [`00bad99c`](../00bad/00bad99c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad99c` · 推定シンボル `None` · 推定型 `None`
- [`00bad0ac`](#insn-00bad0ac) → [`00bad10c`](#insn-00bad10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0e0`](#insn-00bad0e0) → [`00bad118`](#insn-00bad118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad0fc`](#insn-00bad0fc) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad100`](#insn-00bad100) → [`00bad118`](#insn-00bad118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad104`](#insn-00bad104) → [`00bad110`](#insn-00bad110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad108`](#insn-00bad108) → [`00bad120`](#insn-00bad120) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad10c`](#insn-00bad10c) → [`00bad120`](#insn-00bad120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad110`](#insn-00bad110) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad114`](#insn-00bad114) → [`00bad1d8`](#insn-00bad1d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad11c`](#insn-00bad11c) → [`00bad110`](#insn-00bad110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad120`](#insn-00bad120) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad124`](#insn-00bad124) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad12c`](#insn-00bad12c) → [`00bad324`](#insn-00bad324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad130`](#insn-00bad130) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad138`](#insn-00bad138) → [`00bad14c`](#insn-00bad14c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad13c`](#insn-00bad13c) → [`00bad1c8`](#insn-00bad1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad148`](#insn-00bad148) → [`00bad324`](#insn-00bad324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad158`](#insn-00bad158) → [`00bad13c`](#insn-00bad13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad18c`](#insn-00bad18c) → [`00bad1bc`](#insn-00bad1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1a8`](#insn-00bad1a8) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad1ac`](#insn-00bad1ac) → [`00bad1bc`](#insn-00bad1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1b0`](#insn-00bad1b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1b4`](#insn-00bad1b4) → [`00bad140`](#insn-00bad140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1b8`](#insn-00bad1b8) → [`00bad1c8`](#insn-00bad1c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1c0`](#insn-00bad1c0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1c4`](#insn-00bad1c4) → [`00bad140`](#insn-00bad140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1c8`](#insn-00bad1c8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1e4`](#insn-00bad1e4) → [`00bad3a0`](#insn-00bad3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1e8`](#insn-00bad1e8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad1fc`](#insn-00bad1fc) → [`00bad208`](#insn-00bad208) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad200`](#insn-00bad200) → [`00bad284`](#insn-00bad284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad214`](#insn-00bad214) → [`00bad200`](#insn-00bad200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad248`](#insn-00bad248) → [`00bad274`](#insn-00bad274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad264`](#insn-00bad264) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad268`](#insn-00bad268) → [`00bad274`](#insn-00bad274) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad26c`](#insn-00bad26c) → [`00bad204`](#insn-00bad204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad270`](#insn-00bad270) → [`00bad284`](#insn-00bad284) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad278`](#insn-00bad278) → [`00bad204`](#insn-00bad204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad27c`](#insn-00bad27c) → [`00bad284`](#insn-00bad284) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad280`](#insn-00bad280) → [`00bad2f8`](#insn-00bad2f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad290`](#insn-00bad290) → [`00bad280`](#insn-00bad280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2c4`](#insn-00bad2c4) → [`00bad2f0`](#insn-00bad2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2e0`](#insn-00bad2e0) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad2e4`](#insn-00bad2e4) → [`00bad2f0`](#insn-00bad2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2e8`](#insn-00bad2e8) → [`00bad284`](#insn-00bad284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2ec`](#insn-00bad2ec) → [`00bad2f8`](#insn-00bad2f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2f4`](#insn-00bad2f4) → [`00bad284`](#insn-00bad284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad2fc`](#insn-00bad2fc) → [`00bad3b0`](#insn-00bad3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad300`](#insn-00bad300) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad318`](#insn-00bad318) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad320`](#insn-00bad320) → [`00bad1ec`](#insn-00bad1ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad324`](#insn-00bad324) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad33c`](#insn-00bad33c) → [`00bad49c`](#insn-00bad49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad364`](#insn-00bad364) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad374`](#insn-00bad374) → [`00bad4b4`](#insn-00bad4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad390`](#insn-00bad390) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad394`](#insn-00bad394) → [`00bad4b4`](#insn-00bad4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad398`](#insn-00bad398) → [`00bad4bc`](#insn-00bad4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad39c`](#insn-00bad39c) → [`00bad564`](#insn-00bad564) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3a0`](#insn-00bad3a0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3a8`](#insn-00bad3a8) → [`00bad3c8`](#insn-00bad3c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3ac`](#insn-00bad3ac) → [`00bad44c`](#insn-00bad44c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3b0`](#insn-00bad3b0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3b4`](#insn-00bad3b4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3b8`](#insn-00bad3b8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3c4`](#insn-00bad3c4) → [`00bad44c`](#insn-00bad44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad3dc`](#insn-00bad3dc) → [`00bad43c`](#insn-00bad43c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad410`](#insn-00bad410) → [`00bad4a8`](#insn-00bad4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad42c`](#insn-00bad42c) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad430`](#insn-00bad430) → [`00bad4a8`](#insn-00bad4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad434`](#insn-00bad434) → [`00bad440`](#insn-00bad440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad438`](#insn-00bad438) → [`00bad44c`](#insn-00bad44c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad43c`](#insn-00bad43c) → [`00bad44c`](#insn-00bad44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad44c`](#insn-00bad44c) → [`00bad478`](#insn-00bad478) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad458`](#insn-00bad458) → [`00bae130`](../00bae/00bae130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae130` · 推定シンボル `None` · 推定型 `None`
- [`00bad46c`](#insn-00bad46c) → [`00bae130`](../00bae/00bae130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae130` · 推定シンボル `None` · 推定型 `None`
- [`00bad470`](#insn-00bad470) → [`00bad6a8`](#insn-00bad6a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad474`](#insn-00bad474) → [`00bad00c`](#insn-00bad00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad484`](#insn-00bad484) → [`00bad694`](#insn-00bad694) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad490`](#insn-00bad490) → [`00bacfd0`](#insn-00bacfd0) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bad498`](#insn-00bad498) → [`00bad00c`](#insn-00bad00c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad49c`](#insn-00bad49c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4a0`](#insn-00bad4a0) → [`00bad4bc`](#insn-00bad4bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4a4`](#insn-00bad4a4) → [`00bad564`](#insn-00bad564) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4ac`](#insn-00bad4ac) → [`00bad440`](#insn-00bad440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4b0`](#insn-00bad4b0) → [`00bad44c`](#insn-00bad44c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4b8`](#insn-00bad4b8) → [`00bad564`](#insn-00bad564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4bc`](#insn-00bad4bc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4c4`](#insn-00bad4c4) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad4d0`](#insn-00bad4d0) → [`00bad4e4`](#insn-00bad4e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4d4`](#insn-00bad4d4) → [`00bad558`](#insn-00bad558) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad4e0`](#insn-00bad4e0) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad4f0`](#insn-00bad4f0) → [`00bad4d4`](#insn-00bad4d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad524`](#insn-00bad524) → [`00bad550`](#insn-00bad550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad540`](#insn-00bad540) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad544`](#insn-00bad544) → [`00bad550`](#insn-00bad550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad548`](#insn-00bad548) → [`00bad4d8`](#insn-00bad4d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad54c`](#insn-00bad54c) → [`00bad558`](#insn-00bad558) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad554`](#insn-00bad554) → [`00bad4d8`](#insn-00bad4d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad558`](#insn-00bad558) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad564`](#insn-00bad564) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad56c`](#insn-00bad56c) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad570`](#insn-00bad570) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad580`](#insn-00bad580) → [`00bad58c`](#insn-00bad58c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad584`](#insn-00bad584) → [`00bad608`](#insn-00bad608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad598`](#insn-00bad598) → [`00bad584`](#insn-00bad584) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5cc`](#insn-00bad5cc) → [`00bad5f8`](#insn-00bad5f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5e8`](#insn-00bad5e8) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad5ec`](#insn-00bad5ec) → [`00bad5f8`](#insn-00bad5f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5f0`](#insn-00bad5f0) → [`00bad588`](#insn-00bad588) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5f4`](#insn-00bad5f4) → [`00bad608`](#insn-00bad608) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5fc`](#insn-00bad5fc) → [`00bad588`](#insn-00bad588) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad600`](#insn-00bad600) → [`00bad608`](#insn-00bad608) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad604`](#insn-00bad604) → [`00bad67c`](#insn-00bad67c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad614`](#insn-00bad614) → [`00bad604`](#insn-00bad604) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad648`](#insn-00bad648) → [`00bad674`](#insn-00bad674) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad664`](#insn-00bad664) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad668`](#insn-00bad668) → [`00bad674`](#insn-00bad674) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad66c`](#insn-00bad66c) → [`00bad608`](#insn-00bad608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad670`](#insn-00bad670) → [`00bad67c`](#insn-00bad67c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad678`](#insn-00bad678) → [`00bad608`](#insn-00bad608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad680`](#insn-00bad680) → [`00bad00c`](#insn-00bad00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad684`](#insn-00bad684) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad690`](#insn-00bad690) → [`00bad574`](#insn-00bad574) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad69c`](#insn-00bad69c) → [`00bacfd0`](#insn-00bacfd0) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bad6a4`](#insn-00bad6a4) → [`00bacff8`](#insn-00bacff8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad6ac`](#insn-00bad6ac) → [`00bacff8`](#insn-00bacff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad6b0`](#insn-00bad6b0) → [`00bad970`](#insn-00bad970) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad6c0`](#insn-00bad6c0) → `0030e1cc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::switchdataD_0030e1cc` · 推定型 `byte`
- [`00bad6c8`](#insn-00bad6c8) → [`00bad970`](#insn-00bad970) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad6c8`](#insn-00bad6c8) → [`00bad6cc`](#insn-00bad6cc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_2` · 推定型 `None`
- [`00bad6c8`](#insn-00bad6c8) → [`00bad8d4`](#insn-00bad8d4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_3` · 推定型 `None`
- [`00bad6c8`](#insn-00bad6c8) → [`00bad900`](#insn-00bad900) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_4` · 推定型 `None`
- [`00bad6c8`](#insn-00bad6c8) → [`00bad930`](#insn-00bad930) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_5` · 推定型 `None`
- [`00bad6e0`](#insn-00bad6e0) → [`00bad964`](#insn-00bad964) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad714`](#insn-00bad714) → [`00bad990`](#insn-00bad990) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad730`](#insn-00bad730) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad734`](#insn-00bad734) → [`00bad990`](#insn-00bad990) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad738`](#insn-00bad738) → [`00bad968`](#insn-00bad968) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad73c`](#insn-00bad73c) → [`00bad970`](#insn-00bad970) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad750`](#insn-00bad750) → [`00bad99c`](../00bad/00bad99c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad99c` · 推定シンボル `None` · 推定型 `None`
- [`00bad75c`](#insn-00bad75c) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad764`](#insn-00bad764) → [`00bad784`](#insn-00bad784) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad76c`](#insn-00bad76c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad780`](#insn-00bad780) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad7a0`](#insn-00bad7a0) → [`00bad800`](#insn-00bad800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad7d4`](#insn-00bad7d4) → [`00bad808`](#insn-00bad808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad7f0`](#insn-00bad7f0) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad7f4`](#insn-00bad7f4) → [`00bad808`](#insn-00bad808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad7f8`](#insn-00bad7f8) → [`00bad774`](#insn-00bad774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad7fc`](#insn-00bad7fc) → [`00bad810`](#insn-00bad810) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad800`](#insn-00bad800) → [`00bad774`](#insn-00bad774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad804`](#insn-00bad804) → [`00bad810`](#insn-00bad810) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad80c`](#insn-00bad80c) → [`00bad774`](#insn-00bad774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad818`](#insn-00bad818) → [`00bad770`](#insn-00bad770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad824`](#insn-00bad824) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad828`](#insn-00bad828) → [`00bad844`](#insn-00bad844) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad82c`](#insn-00bad82c) → [`00bad76c`](#insn-00bad76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad840`](#insn-00bad840) → [`00bad768`](#insn-00bad768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad854`](#insn-00bad854) → [`00bad82c`](#insn-00bad82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad888`](#insn-00bad888) → [`00bad8bc`](#insn-00bad8bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad894`](#insn-00bad894) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8a8`](#insn-00bad8a8) → [`00c57c50`](../00c57/00c57c50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c50` · 推定シンボル `None` · 推定型 `None`
- [`00bad8ac`](#insn-00bad8ac) → [`00bad8bc`](#insn-00bad8bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8b0`](#insn-00bad8b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8b4`](#insn-00bad8b4) → [`00bad830`](#insn-00bad830) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8b8`](#insn-00bad8b8) → [`00bad76c`](#insn-00bad76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8c0`](#insn-00bad8c0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8c4`](#insn-00bad8c4) → [`00bad830`](#insn-00bad830) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8d0`](#insn-00bad8d0) → [`00bad76c`](#insn-00bad76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8dc`](#insn-00bad8dc) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8e0`](#insn-00bad8e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8e4`](#insn-00bad8e4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8e8`](#insn-00bad8e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8ec`](#insn-00bad8ec) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8f0`](#insn-00bad8f0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8f4`](#insn-00bad8f4) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8fc`](#insn-00bad8fc) → [`00bad99c`](../00bad/00bad99c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bad99c` · 推定シンボル `None` · 推定型 `None`
- [`00bad90c`](#insn-00bad90c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad910`](#insn-00bad910) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad914`](#insn-00bad914) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad918`](#insn-00bad918) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad91c`](#insn-00bad91c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad920`](#insn-00bad920) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad924`](#insn-00bad924) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad92c`](#insn-00bad92c) → [`00badc48`](../00bad/00badc48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00badc48` · 推定シンボル `None` · 推定型 `None`
- [`00bad940`](#insn-00bad940) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad944`](#insn-00bad944) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad948`](#insn-00bad948) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad94c`](#insn-00bad94c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad950`](#insn-00bad950) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad954`](#insn-00bad954) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad958`](#insn-00bad958) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad960`](#insn-00bad960) → [`00bade50`](../00bad/00bade50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bade50` · 推定シンボル `None` · 推定型 `None`
- [`00bad964`](#insn-00bad964) → [`00bad970`](#insn-00bad970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`
- [`00bad970`](#insn-00bad970) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad974`](#insn-00bad974) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad978`](#insn-00bad978) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad97c`](#insn-00bad97c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad980`](#insn-00bad980) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad984`](#insn-00bad984) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad994`](#insn-00bad994) → [`00bad968`](#insn-00bad968) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad998`](#insn-00bad998) → [`00bad970`](#insn-00bad970) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bad6c8::caseD_0` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacfd4`](#insn-00bacfd4)

~~~json
{
  "source": "00bacfd4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfd8`](#insn-00bacfd8)

~~~json
{
  "source": "00bacfd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfdc`](#insn-00bacfdc)

~~~json
{
  "source": "00bacfdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfe0`](#insn-00bacfe0)

~~~json
{
  "source": "00bacfe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfe4`](#insn-00bacfe4)

~~~json
{
  "source": "00bacfe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacfe8`](#insn-00bacfe8)

~~~json
{
  "source": "00bacfe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacffc`](#insn-00bacffc)

~~~json
{
  "source": "00bacffc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad008`](#insn-00bad008)

~~~json
{
  "source": "00bad008",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad01c`](#insn-00bad01c)

~~~json
{
  "source": "00bad01c",
  "target": "00bad6b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad024`](#insn-00bad024)

~~~json
{
  "source": "00bad024",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad028`](#insn-00bad028)

~~~json
{
  "source": "00bad028",
  "target": "00bad740",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad048`](#insn-00bad048)

~~~json
{
  "source": "00bad048",
  "target": "00bad07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad058`](#insn-00bad058)

~~~json
{
  "source": "00bad058",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad074`](#insn-00bad074)

~~~json
{
  "source": "00bad074",
  "target": "00bade50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad078`](#insn-00bad078)

~~~json
{
  "source": "00bad078",
  "target": "00bad08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad07c`](#insn-00bad07c)

~~~json
{
  "source": "00bad07c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad088`](#insn-00bad088)

~~~json
{
  "source": "00bad088",
  "target": "00bad99c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad0ac`](#insn-00bad0ac)

~~~json
{
  "source": "00bad0ac",
  "target": "00bad10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0e0`](#insn-00bad0e0)

~~~json
{
  "source": "00bad0e0",
  "target": "00bad118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad0fc`](#insn-00bad0fc)

~~~json
{
  "source": "00bad0fc",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad100`](#insn-00bad100)

~~~json
{
  "source": "00bad100",
  "target": "00bad118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad104`](#insn-00bad104)

~~~json
{
  "source": "00bad104",
  "target": "00bad110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad108`](#insn-00bad108)

~~~json
{
  "source": "00bad108",
  "target": "00bad120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad10c`](#insn-00bad10c)

~~~json
{
  "source": "00bad10c",
  "target": "00bad120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad110`](#insn-00bad110)

~~~json
{
  "source": "00bad110",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad114`](#insn-00bad114)

~~~json
{
  "source": "00bad114",
  "target": "00bad1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad11c`](#insn-00bad11c)

~~~json
{
  "source": "00bad11c",
  "target": "00bad110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad120`](#insn-00bad120)

~~~json
{
  "source": "00bad120",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad124`](#insn-00bad124)

~~~json
{
  "source": "00bad124",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad12c`](#insn-00bad12c)

~~~json
{
  "source": "00bad12c",
  "target": "00bad324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad130`](#insn-00bad130)

~~~json
{
  "source": "00bad130",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad138`](#insn-00bad138)

~~~json
{
  "source": "00bad138",
  "target": "00bad14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad13c`](#insn-00bad13c)

~~~json
{
  "source": "00bad13c",
  "target": "00bad1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad148`](#insn-00bad148)

~~~json
{
  "source": "00bad148",
  "target": "00bad324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad158`](#insn-00bad158)

~~~json
{
  "source": "00bad158",
  "target": "00bad13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad18c`](#insn-00bad18c)

~~~json
{
  "source": "00bad18c",
  "target": "00bad1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1a8`](#insn-00bad1a8)

~~~json
{
  "source": "00bad1a8",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad1ac`](#insn-00bad1ac)

~~~json
{
  "source": "00bad1ac",
  "target": "00bad1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1b0`](#insn-00bad1b0)

~~~json
{
  "source": "00bad1b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1b4`](#insn-00bad1b4)

~~~json
{
  "source": "00bad1b4",
  "target": "00bad140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1b8`](#insn-00bad1b8)

~~~json
{
  "source": "00bad1b8",
  "target": "00bad1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1c0`](#insn-00bad1c0)

~~~json
{
  "source": "00bad1c0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1c4`](#insn-00bad1c4)

~~~json
{
  "source": "00bad1c4",
  "target": "00bad140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1c8`](#insn-00bad1c8)

~~~json
{
  "source": "00bad1c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1e4`](#insn-00bad1e4)

~~~json
{
  "source": "00bad1e4",
  "target": "00bad3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1e8`](#insn-00bad1e8)

~~~json
{
  "source": "00bad1e8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad1fc`](#insn-00bad1fc)

~~~json
{
  "source": "00bad1fc",
  "target": "00bad208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad200`](#insn-00bad200)

~~~json
{
  "source": "00bad200",
  "target": "00bad284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad214`](#insn-00bad214)

~~~json
{
  "source": "00bad214",
  "target": "00bad200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad248`](#insn-00bad248)

~~~json
{
  "source": "00bad248",
  "target": "00bad274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad264`](#insn-00bad264)

~~~json
{
  "source": "00bad264",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad268`](#insn-00bad268)

~~~json
{
  "source": "00bad268",
  "target": "00bad274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad26c`](#insn-00bad26c)

~~~json
{
  "source": "00bad26c",
  "target": "00bad204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad270`](#insn-00bad270)

~~~json
{
  "source": "00bad270",
  "target": "00bad284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad278`](#insn-00bad278)

~~~json
{
  "source": "00bad278",
  "target": "00bad204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad27c`](#insn-00bad27c)

~~~json
{
  "source": "00bad27c",
  "target": "00bad284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad280`](#insn-00bad280)

~~~json
{
  "source": "00bad280",
  "target": "00bad2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad290`](#insn-00bad290)

~~~json
{
  "source": "00bad290",
  "target": "00bad280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2c4`](#insn-00bad2c4)

~~~json
{
  "source": "00bad2c4",
  "target": "00bad2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2e0`](#insn-00bad2e0)

~~~json
{
  "source": "00bad2e0",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad2e4`](#insn-00bad2e4)

~~~json
{
  "source": "00bad2e4",
  "target": "00bad2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2e8`](#insn-00bad2e8)

~~~json
{
  "source": "00bad2e8",
  "target": "00bad284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2ec`](#insn-00bad2ec)

~~~json
{
  "source": "00bad2ec",
  "target": "00bad2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2f4`](#insn-00bad2f4)

~~~json
{
  "source": "00bad2f4",
  "target": "00bad284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad2fc`](#insn-00bad2fc)

~~~json
{
  "source": "00bad2fc",
  "target": "00bad3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad300`](#insn-00bad300)

~~~json
{
  "source": "00bad300",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad318`](#insn-00bad318)

~~~json
{
  "source": "00bad318",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad320`](#insn-00bad320)

~~~json
{
  "source": "00bad320",
  "target": "00bad1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad324`](#insn-00bad324)

~~~json
{
  "source": "00bad324",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad33c`](#insn-00bad33c)

~~~json
{
  "source": "00bad33c",
  "target": "00bad49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad364`](#insn-00bad364)

~~~json
{
  "source": "00bad364",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad374`](#insn-00bad374)

~~~json
{
  "source": "00bad374",
  "target": "00bad4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad390`](#insn-00bad390)

~~~json
{
  "source": "00bad390",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad394`](#insn-00bad394)

~~~json
{
  "source": "00bad394",
  "target": "00bad4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad398`](#insn-00bad398)

~~~json
{
  "source": "00bad398",
  "target": "00bad4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad39c`](#insn-00bad39c)

~~~json
{
  "source": "00bad39c",
  "target": "00bad564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3a0`](#insn-00bad3a0)

~~~json
{
  "source": "00bad3a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3a8`](#insn-00bad3a8)

~~~json
{
  "source": "00bad3a8",
  "target": "00bad3c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3ac`](#insn-00bad3ac)

~~~json
{
  "source": "00bad3ac",
  "target": "00bad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3b0`](#insn-00bad3b0)

~~~json
{
  "source": "00bad3b0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3b4`](#insn-00bad3b4)

~~~json
{
  "source": "00bad3b4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3b8`](#insn-00bad3b8)

~~~json
{
  "source": "00bad3b8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3c4`](#insn-00bad3c4)

~~~json
{
  "source": "00bad3c4",
  "target": "00bad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad3dc`](#insn-00bad3dc)

~~~json
{
  "source": "00bad3dc",
  "target": "00bad43c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad410`](#insn-00bad410)

~~~json
{
  "source": "00bad410",
  "target": "00bad4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad42c`](#insn-00bad42c)

~~~json
{
  "source": "00bad42c",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad430`](#insn-00bad430)

~~~json
{
  "source": "00bad430",
  "target": "00bad4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad434`](#insn-00bad434)

~~~json
{
  "source": "00bad434",
  "target": "00bad440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad438`](#insn-00bad438)

~~~json
{
  "source": "00bad438",
  "target": "00bad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad43c`](#insn-00bad43c)

~~~json
{
  "source": "00bad43c",
  "target": "00bad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad44c`](#insn-00bad44c)

~~~json
{
  "source": "00bad44c",
  "target": "00bad478",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad458`](#insn-00bad458)

~~~json
{
  "source": "00bad458",
  "target": "00bae130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad46c`](#insn-00bad46c)

~~~json
{
  "source": "00bad46c",
  "target": "00bae130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad470`](#insn-00bad470)

~~~json
{
  "source": "00bad470",
  "target": "00bad6a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad474`](#insn-00bad474)

~~~json
{
  "source": "00bad474",
  "target": "00bad00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad484`](#insn-00bad484)

~~~json
{
  "source": "00bad484",
  "target": "00bad694",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad490`](#insn-00bad490)

~~~json
{
  "source": "00bad490",
  "target": "00bacfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad498`](#insn-00bad498)

~~~json
{
  "source": "00bad498",
  "target": "00bad00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad49c`](#insn-00bad49c)

~~~json
{
  "source": "00bad49c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4a0`](#insn-00bad4a0)

~~~json
{
  "source": "00bad4a0",
  "target": "00bad4bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4a4`](#insn-00bad4a4)

~~~json
{
  "source": "00bad4a4",
  "target": "00bad564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4ac`](#insn-00bad4ac)

~~~json
{
  "source": "00bad4ac",
  "target": "00bad440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4b0`](#insn-00bad4b0)

~~~json
{
  "source": "00bad4b0",
  "target": "00bad44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4b8`](#insn-00bad4b8)

~~~json
{
  "source": "00bad4b8",
  "target": "00bad564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4bc`](#insn-00bad4bc)

~~~json
{
  "source": "00bad4bc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4c4`](#insn-00bad4c4)

~~~json
{
  "source": "00bad4c4",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4d0`](#insn-00bad4d0)

~~~json
{
  "source": "00bad4d0",
  "target": "00bad4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4d4`](#insn-00bad4d4)

~~~json
{
  "source": "00bad4d4",
  "target": "00bad558",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4e0`](#insn-00bad4e0)

~~~json
{
  "source": "00bad4e0",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad4f0`](#insn-00bad4f0)

~~~json
{
  "source": "00bad4f0",
  "target": "00bad4d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad524`](#insn-00bad524)

~~~json
{
  "source": "00bad524",
  "target": "00bad550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad540`](#insn-00bad540)

~~~json
{
  "source": "00bad540",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad544`](#insn-00bad544)

~~~json
{
  "source": "00bad544",
  "target": "00bad550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad548`](#insn-00bad548)

~~~json
{
  "source": "00bad548",
  "target": "00bad4d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad54c`](#insn-00bad54c)

~~~json
{
  "source": "00bad54c",
  "target": "00bad558",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad554`](#insn-00bad554)

~~~json
{
  "source": "00bad554",
  "target": "00bad4d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad558`](#insn-00bad558)

~~~json
{
  "source": "00bad558",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad564`](#insn-00bad564)

~~~json
{
  "source": "00bad564",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad56c`](#insn-00bad56c)

~~~json
{
  "source": "00bad56c",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad570`](#insn-00bad570)

~~~json
{
  "source": "00bad570",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad580`](#insn-00bad580)

~~~json
{
  "source": "00bad580",
  "target": "00bad58c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad584`](#insn-00bad584)

~~~json
{
  "source": "00bad584",
  "target": "00bad608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad598`](#insn-00bad598)

~~~json
{
  "source": "00bad598",
  "target": "00bad584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5cc`](#insn-00bad5cc)

~~~json
{
  "source": "00bad5cc",
  "target": "00bad5f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5e8`](#insn-00bad5e8)

~~~json
{
  "source": "00bad5e8",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad5ec`](#insn-00bad5ec)

~~~json
{
  "source": "00bad5ec",
  "target": "00bad5f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5f0`](#insn-00bad5f0)

~~~json
{
  "source": "00bad5f0",
  "target": "00bad588",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5f4`](#insn-00bad5f4)

~~~json
{
  "source": "00bad5f4",
  "target": "00bad608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5fc`](#insn-00bad5fc)

~~~json
{
  "source": "00bad5fc",
  "target": "00bad588",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad600`](#insn-00bad600)

~~~json
{
  "source": "00bad600",
  "target": "00bad608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad604`](#insn-00bad604)

~~~json
{
  "source": "00bad604",
  "target": "00bad67c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad614`](#insn-00bad614)

~~~json
{
  "source": "00bad614",
  "target": "00bad604",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad648`](#insn-00bad648)

~~~json
{
  "source": "00bad648",
  "target": "00bad674",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad664`](#insn-00bad664)

~~~json
{
  "source": "00bad664",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad668`](#insn-00bad668)

~~~json
{
  "source": "00bad668",
  "target": "00bad674",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad66c`](#insn-00bad66c)

~~~json
{
  "source": "00bad66c",
  "target": "00bad608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad670`](#insn-00bad670)

~~~json
{
  "source": "00bad670",
  "target": "00bad67c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad678`](#insn-00bad678)

~~~json
{
  "source": "00bad678",
  "target": "00bad608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad680`](#insn-00bad680)

~~~json
{
  "source": "00bad680",
  "target": "00bad00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad684`](#insn-00bad684)

~~~json
{
  "source": "00bad684",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad690`](#insn-00bad690)

~~~json
{
  "source": "00bad690",
  "target": "00bad574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad69c`](#insn-00bad69c)

~~~json
{
  "source": "00bad69c",
  "target": "00bacfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad6a4`](#insn-00bad6a4)

~~~json
{
  "source": "00bad6a4",
  "target": "00bacff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6ac`](#insn-00bad6ac)

~~~json
{
  "source": "00bad6ac",
  "target": "00bacff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6b0`](#insn-00bad6b0)

~~~json
{
  "source": "00bad6b0",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6c0`](#insn-00bad6c0)

~~~json
{
  "source": "00bad6c0",
  "target": "0030e1cc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e1cc",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "a9",
  "capture_start": "0030e1cc",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bad6c8`](#insn-00bad6c8)

~~~json
{
  "source": "00bad6c8",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6c8`](#insn-00bad6c8)

~~~json
{
  "source": "00bad6c8",
  "target": "00bad6cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6c8`](#insn-00bad6c8)

~~~json
{
  "source": "00bad6c8",
  "target": "00bad8d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6c8`](#insn-00bad6c8)

~~~json
{
  "source": "00bad6c8",
  "target": "00bad900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6c8`](#insn-00bad6c8)

~~~json
{
  "source": "00bad6c8",
  "target": "00bad930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad6e0`](#insn-00bad6e0)

~~~json
{
  "source": "00bad6e0",
  "target": "00bad964",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad714`](#insn-00bad714)

~~~json
{
  "source": "00bad714",
  "target": "00bad990",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad730`](#insn-00bad730)

~~~json
{
  "source": "00bad730",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad734`](#insn-00bad734)

~~~json
{
  "source": "00bad734",
  "target": "00bad990",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad738`](#insn-00bad738)

~~~json
{
  "source": "00bad738",
  "target": "00bad968",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad73c`](#insn-00bad73c)

~~~json
{
  "source": "00bad73c",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad750`](#insn-00bad750)

~~~json
{
  "source": "00bad750",
  "target": "00bad99c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad75c`](#insn-00bad75c)

~~~json
{
  "source": "00bad75c",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad764`](#insn-00bad764)

~~~json
{
  "source": "00bad764",
  "target": "00bad784",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad76c`](#insn-00bad76c)

~~~json
{
  "source": "00bad76c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad780`](#insn-00bad780)

~~~json
{
  "source": "00bad780",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad7a0`](#insn-00bad7a0)

~~~json
{
  "source": "00bad7a0",
  "target": "00bad800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad7d4`](#insn-00bad7d4)

~~~json
{
  "source": "00bad7d4",
  "target": "00bad808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad7f0`](#insn-00bad7f0)

~~~json
{
  "source": "00bad7f0",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad7f4`](#insn-00bad7f4)

~~~json
{
  "source": "00bad7f4",
  "target": "00bad808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad7f8`](#insn-00bad7f8)

~~~json
{
  "source": "00bad7f8",
  "target": "00bad774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad7fc`](#insn-00bad7fc)

~~~json
{
  "source": "00bad7fc",
  "target": "00bad810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad800`](#insn-00bad800)

~~~json
{
  "source": "00bad800",
  "target": "00bad774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad804`](#insn-00bad804)

~~~json
{
  "source": "00bad804",
  "target": "00bad810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad80c`](#insn-00bad80c)

~~~json
{
  "source": "00bad80c",
  "target": "00bad774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad818`](#insn-00bad818)

~~~json
{
  "source": "00bad818",
  "target": "00bad770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad824`](#insn-00bad824)

~~~json
{
  "source": "00bad824",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad828`](#insn-00bad828)

~~~json
{
  "source": "00bad828",
  "target": "00bad844",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad82c`](#insn-00bad82c)

~~~json
{
  "source": "00bad82c",
  "target": "00bad76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad840`](#insn-00bad840)

~~~json
{
  "source": "00bad840",
  "target": "00bad768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad854`](#insn-00bad854)

~~~json
{
  "source": "00bad854",
  "target": "00bad82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad888`](#insn-00bad888)

~~~json
{
  "source": "00bad888",
  "target": "00bad8bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad894`](#insn-00bad894)

~~~json
{
  "source": "00bad894",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8a8`](#insn-00bad8a8)

~~~json
{
  "source": "00bad8a8",
  "target": "00c57c50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad8ac`](#insn-00bad8ac)

~~~json
{
  "source": "00bad8ac",
  "target": "00bad8bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8b0`](#insn-00bad8b0)

~~~json
{
  "source": "00bad8b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8b4`](#insn-00bad8b4)

~~~json
{
  "source": "00bad8b4",
  "target": "00bad830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8b8`](#insn-00bad8b8)

~~~json
{
  "source": "00bad8b8",
  "target": "00bad76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8c0`](#insn-00bad8c0)

~~~json
{
  "source": "00bad8c0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8c4`](#insn-00bad8c4)

~~~json
{
  "source": "00bad8c4",
  "target": "00bad830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8d0`](#insn-00bad8d0)

~~~json
{
  "source": "00bad8d0",
  "target": "00bad76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8dc`](#insn-00bad8dc)

~~~json
{
  "source": "00bad8dc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8e0`](#insn-00bad8e0)

~~~json
{
  "source": "00bad8e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8e4`](#insn-00bad8e4)

~~~json
{
  "source": "00bad8e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8e8`](#insn-00bad8e8)

~~~json
{
  "source": "00bad8e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8ec`](#insn-00bad8ec)

~~~json
{
  "source": "00bad8ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8f0`](#insn-00bad8f0)

~~~json
{
  "source": "00bad8f0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8f4`](#insn-00bad8f4)

~~~json
{
  "source": "00bad8f4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8fc`](#insn-00bad8fc)

~~~json
{
  "source": "00bad8fc",
  "target": "00bad99c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad90c`](#insn-00bad90c)

~~~json
{
  "source": "00bad90c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad910`](#insn-00bad910)

~~~json
{
  "source": "00bad910",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad914`](#insn-00bad914)

~~~json
{
  "source": "00bad914",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad918`](#insn-00bad918)

~~~json
{
  "source": "00bad918",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad91c`](#insn-00bad91c)

~~~json
{
  "source": "00bad91c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad920`](#insn-00bad920)

~~~json
{
  "source": "00bad920",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad924`](#insn-00bad924)

~~~json
{
  "source": "00bad924",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad92c`](#insn-00bad92c)

~~~json
{
  "source": "00bad92c",
  "target": "00badc48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad940`](#insn-00bad940)

~~~json
{
  "source": "00bad940",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad944`](#insn-00bad944)

~~~json
{
  "source": "00bad944",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad948`](#insn-00bad948)

~~~json
{
  "source": "00bad948",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad94c`](#insn-00bad94c)

~~~json
{
  "source": "00bad94c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad950`](#insn-00bad950)

~~~json
{
  "source": "00bad950",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad954`](#insn-00bad954)

~~~json
{
  "source": "00bad954",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad958`](#insn-00bad958)

~~~json
{
  "source": "00bad958",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad960`](#insn-00bad960)

~~~json
{
  "source": "00bad960",
  "target": "00bade50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bad964`](#insn-00bad964)

~~~json
{
  "source": "00bad964",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad970`](#insn-00bad970)

~~~json
{
  "source": "00bad970",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad974`](#insn-00bad974)

~~~json
{
  "source": "00bad974",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad978`](#insn-00bad978)

~~~json
{
  "source": "00bad978",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad97c`](#insn-00bad97c)

~~~json
{
  "source": "00bad97c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad980`](#insn-00bad980)

~~~json
{
  "source": "00bad980",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad984`](#insn-00bad984)

~~~json
{
  "source": "00bad984",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad994`](#insn-00bad994)

~~~json
{
  "source": "00bad994",
  "target": "00bad968",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad998`](#insn-00bad998)

~~~json
{
  "source": "00bad998",
  "target": "00bad970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
