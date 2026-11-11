# 00babf9c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
  "source_text_sha256": "28f58857bd6323b09f4d942f0d149d7edfc07b594b464b889f237d236720fdaa"
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
