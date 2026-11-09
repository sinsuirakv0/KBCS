# 00bacfd0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
  "source_text_sha256": "92ec78018948c716ce37d6f0cdd44b1725ef0d92b0a939f2c9ffa51c700f0fdf"
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
