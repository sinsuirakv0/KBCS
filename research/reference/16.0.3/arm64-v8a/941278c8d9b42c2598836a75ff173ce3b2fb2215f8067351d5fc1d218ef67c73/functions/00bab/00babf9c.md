# 00babf9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baafa8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baafa8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-31f091f93a7b25b7aaea198013cc0238)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babf9c",
  "name": "FUN_00babf9c",
  "size": 2332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd0028919ac821d40bcab25756346e58d718de7735c6573f8504b39756b9133b",
  "source_text_sha256": "bd0028919ac821d40bcab25756346e58d718de7735c6573f8504b39756b9133b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babf9c",
        "00bac8b7"
      ]
    ],
    "bytes_sha256": "f2650e08c2594c24f4d3236b1df5e4a4ab023a7474abe3717bb99e16b53b4462",
    "instruction_count": 583,
    "instruction_bytes": 2332,
    "body_bytes": 2332,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b80ecc](../00b80/00b80ecc.md)
- [00b812a8](../00b81/00b812a8.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c59650](../00c59/00c59650.md)
- [00c59660](../00c59/00c59660.md)
- [00c5d250](../00c5d/00c5d250.md)
- [00c5d260](../00c5d/00c5d260.md)
- [00c5e1f0](../00c5e/00c5e1f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 18300 bytes

~~~c

void FUN_00babf9c(byte **param_1,byte **param_2,long param_3)

{
  byte *pbVar1;
  long lVar2;
  bool bVar3;
  ulong uVar4;
  longlong lVar5;
  int iVar6;
  byte *pbVar7;
  long lVar8;
  byte bVar9;
  byte bVar10;
  ushort uVar11;
  ushort uVar12;
  uint uVar13;
  uint uVar14;
  byte *pbVar15;
  float fVar16;
  double dVar17;
  float fVar18;
  double dVar19;
  byte *local_40;
  long local_38;
  
                    /* try { // try from 00babfb0 to 00cabfbb has its CatchHandler @ 00bacd44 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00babfd0 to 00cabfdb has its CatchHandler @ 00bacd40 */
  switch(*(undefined4 *)(param_3 + 0xa0)) {
  case 0:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00babffc to 00cac007 has its CatchHandler @ 00bacd00 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) goto LAB_00bac3cc;
                    /* try { // try from 00bac020 to 00cac02b has its CatchHandler @ 00baccc0 */
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
LAB_00bac3fc:
                    /* try { // try from 00bac408 to 00cac413 has its CatchHandler @ 00baca74 */
      iVar6 = 10;
      goto LAB_00bac410;
    }
    goto LAB_00bac24c;
  case 1:
                    /* try { // try from 00bac248 to 00cac257 has its CatchHandler @ 00bac9cc */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac398 to 00cac3a3 has its CatchHandler @ 00bacab0 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bac3cc;
                    /* try { // try from 00bac3bc to 00cac3c7 has its CatchHandler @ 00bacaac */
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00bac3fc;
    }
    goto LAB_00bac24c;
  case 2:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac1d4 to 00cac243 has its CatchHandler @ 00bad094 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bac3cc;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00bac3fc;
    }
    goto LAB_00bac24c;
  case 3:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac318 to 00cac323 has its CatchHandler @ 00bacb30 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bac32c to 00cac32f has its CatchHandler @ 00bacb10 */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bac54c to 00cac56b has its CatchHandler @ 00bace40 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bac56c to 00cac5db has its CatchHandler @ 00bad090 */
              goto LAB_00bac588;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bac588:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
      bVar9 = 0;
      if ((local_40 != pbVar15) && (*local_40 == 0)) {
        if (lVar5 < 0x80) {
          bVar9 = (byte)lVar5;
          if (lVar5 < -0x7f) {
            bVar9 = 0x80;
          }
        }
        else {
          bVar9 = 0x7f;
        }
      }
    }
    else {
      bVar9 = 0;
    }
                    /* try { // try from 00bac81c to 00cac827 has its CatchHandler @ 00baca14 */
    bVar10 = bVar9;
    if (param_1 != (byte **)0x0) {
      bVar10 = *(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      bVar9 = *(byte *)param_2;
    }
    bVar3 = (char)bVar10 < (char)bVar9;
    break;
  case 4:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac0bc to 00cac0c7 has its CatchHandler @ 00bacc50 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bac3cc;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00bac0e8 to 00cac0f3 has its CatchHandler @ 00bacc04 */
        } while (bVar9 != 0);
      }
      goto LAB_00bac3fc;
    }
LAB_00bac24c:
    uVar13 = 0;
joined_r0x00bac444:
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(byte *)param_2;
    }
                    /* try { // try from 00bac458 to 00cac463 has its CatchHandler @ 00baca60 */
    bVar3 = (uVar13 & 0xff) <= (uVar14 & 0xff);
LAB_00bac45c:
    bVar3 = !bVar3;
    break;
  case 5:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac484 to 00cac48f has its CatchHandler @ 00baca38 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bac4a8 to 00cac4b3 has its CatchHandler @ 00baca34 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bac68c to 00cac697 has its CatchHandler @ 00bacb0c */
              iVar6 = 0x10;
              goto LAB_00bac6ac;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bac6ac:
      local_40 = pbVar15;
                    /* try { // try from 00bac6b0 to 00cac6bb has its CatchHandler @ 00bacb08 */
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
      uVar11 = 0;
                    /* try { // try from 00bac6c4 to 00cac6c7 has its CatchHandler @ 00bacae8 */
      if ((local_40 != pbVar15) && (*local_40 == 0)) {
        if (lVar5 < 0x8000) {
                    /* try { // try from 00bac840 to 00cac84b has its CatchHandler @ 00baca10 */
          uVar11 = (ushort)lVar5;
          if (lVar5 < -0x7fff) {
            uVar11 = 0x8000;
          }
        }
        else {
          uVar11 = 0x7fff;
        }
      }
    }
    else {
      uVar11 = 0;
    }
    uVar12 = uVar11;
    if (param_1 != (byte **)0x0) {
      uVar12 = *(ushort *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar11 = *(ushort *)param_2;
    }
    bVar3 = (short)uVar12 < (short)uVar11;
    break;
  case 6:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
                    /* try { // try from 00bac4d4 to 00cac4df has its CatchHandler @ 00baca24 */
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bac704 to 00cac70f has its CatchHandler @ 00bacac0 */
              iVar6 = 0x10;
              goto LAB_00bac72c;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
                    /* try { // try from 00bac4f8 to 00cac503 has its CatchHandler @ 00bac9fc */
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bac72c:
      local_40 = pbVar15;
                    /* try { // try from 00bac730 to 00cac73b has its CatchHandler @ 00baca8c */
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
      uVar13 = 0;
                    /* try { // try from 00bac754 to 00cac75f has its CatchHandler @ 00baca88 */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfffe < uVar4)) {
        uVar13 = 0xffff;
      }
    }
    else {
      uVar13 = 0;
    }
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(ushort *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(ushort *)param_2;
    }
    bVar3 = (uVar13 & 0xffff) <= (uVar14 & 0xffff);
    goto LAB_00bac45c;
  case 7:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac34c to 00cac357 has its CatchHandler @ 00bacad8 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bac36c to 00cac377 has its CatchHandler @ 00bacad4 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bac5e0 to 00cac5ef has its CatchHandler @ 00bac9c4 */
              iVar6 = 0x10;
                    /* try { // try from 00bac5f0 to 00cac603 has its CatchHandler @ 00bac9c0 */
              goto LAB_00bac608;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bac608:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
      fVar18 = 0.0;
                    /* try { // try from 00bac644 to 00cac65f has its CatchHandler @ 00bacea8 */
      if ((((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = NAN, lVar5 < 0x80000000)) &&
         (fVar18 = (float)lVar5, lVar5 < -0x7fffffff)) {
        fVar18 = -0.0;
      }
    }
    else {
      fVar18 = 0.0;
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = (int)fVar16 < (int)fVar18;
    break;
  case 8:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bac524 to 00cac52f has its CatchHandler @ 00bac9ec */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bac780 to 00cac78b has its CatchHandler @ 00baca78 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bac7a0 to 00cac7ab has its CatchHandler @ 00baca5c */
              iVar6 = 0x10;
              goto LAB_00bac7c0;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bac7c0:
      local_40 = pbVar15;
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
                    /* try { // try from 00bac7cc to 00cac7d7 has its CatchHandler @ 00baca4c */
      fVar18 = 0.0;
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = (float)uVar4, 0xfffffffe < uVar4)
         ) {
        fVar18 = -NAN;
      }
    }
    else {
      fVar18 = 0.0;
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = (uint)fVar18 <= (uint)fVar16;
    goto LAB_00bac45c;
  case 9:
    local_40 = (byte *)0x0;
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac10c to 00cac117 has its CatchHandler @ 00bacc00 */
      lVar8 = param_3 + 0xc1;
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        lVar8 = *(long *)(param_3 + 0xd0);
      }
      _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib(&local_40,lVar8,0,1);
    }
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
                    /* try { // try from 00bac138 to 00cac143 has its CatchHandler @ 00bacbb4 */
    bVar3 = (long)*param_1 < (long)*param_2;
    break;
  case 10:
    local_40 = (byte *)0x0;
                    /* try { // try from 00bac2ac to 00cac2c7 has its CatchHandler @ 00baceac */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar4 = _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib(&local_40,pbVar15,0,1);
      if ((local_40 != (byte *)0x0) && ((uVar4 & 1) != 0)) {
        uVar13 = (uint)*pbVar15;
        pbVar7 = pbVar15;
        if (*pbVar15 != 0) {
          do {
                    /* try { // try from 00bac2f4 to 00cac2ff has its CatchHandler @ 00bacb34 */
            if (uVar13 - 0x30 < 10) break;
            pbVar7 = pbVar7 + 1;
            uVar13 = (uint)*pbVar7;
          } while (uVar13 != 0);
        }
        pbVar1 = pbVar7 + -1;
        if (pbVar7 <= pbVar15) {
          pbVar1 = pbVar7;
        }
        if (*pbVar1 == 0x2d) {
          local_40 = (byte *)0xffffffffffffffff;
        }
      }
    }
                    /* try { // try from 00bac890 to 00cac89b has its CatchHandler @ 00bac9e4 */
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
    bVar3 = *param_2 <= *param_1;
    goto LAB_00bac45c;
  case 0xb:
    if ((param_1 == (byte **)0x0) || (fVar18 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac04c to 00cac057 has its CatchHandler @ 00baccb0 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      fVar16 = strtof((char *)pbVar15,(char **)&local_40);
      fVar18 = 0.0;
                    /* try { // try from 00bac06c to 00cac077 has its CatchHandler @ 00bacc70 */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = fVar16, NAN(fVar16))) {
        fVar18 = NAN;
      }
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
                    /* try { // try from 00bac098 to 00cac0a3 has its CatchHandler @ 00bacc60 */
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = fVar16 < fVar18;
    break;
  case 0xc:
    if ((param_1 == (byte **)0x0) || (dVar19 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00bac15c to 00cac167 has its CatchHandler @ 00bacbb0 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      dVar17 = strtod((char *)pbVar15,(char **)&local_40);
      dVar19 = 0.0;
                    /* try { // try from 00bac188 to 00cac193 has its CatchHandler @ 00bacb64 */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (dVar19 = dVar17, NAN(dVar17))) {
        dVar19 = NAN;
      }
    }
                    /* try { // try from 00bac1a8 to 00cac1b3 has its CatchHandler @ 00bacb60 */
    dVar17 = dVar19;
    if (param_1 != (byte **)0x0) {
      dVar17 = (double)*param_1;
    }
    if (param_2 != (byte **)0x0) {
                    /* try { // try from 00bac1b4 to 00cac1d3 has its CatchHandler @ 00bacec0 */
      dVar19 = (double)*param_2;
    }
    bVar3 = false;
    if (!NAN(dVar17) && !NAN(dVar19)) {
      bVar3 = dVar17 < dVar19;
    }
    break;
  default:
    bVar3 = false;
  }
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(bVar3);
  }
  return;
LAB_00bac3cc:
  if ((uVar13 != 0x30) || ((pbVar15[lVar8] & 0xdf) != 0x58)) goto LAB_00bac3fc;
                    /* try { // try from 00bac3e8 to 00cac3f3 has its CatchHandler @ 00baca9c */
  iVar6 = 0x10;
LAB_00bac410:
  local_40 = pbVar15;
  uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                    *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9c8d0);
  uVar13 = 0;
                    /* try { // try from 00bac434 to 00cac43f has its CatchHandler @ 00baca64 */
  if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfe < uVar4)) {
    uVar13 = 0xff;
  }
  goto joined_r0x00bac444;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babf9c"></a> `00babf9c` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00babfa0"></a> `00babfa0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babfa4"></a> `00babfa4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babfa8"></a> `00babfa8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babfac"></a> `00babfac` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00babfb0"></a> `00babfb0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00babfb4"></a> `00babfb4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00babfb8"></a> `00babfb8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babfbc"></a> `00babfbc` | `48 a0 40 b9` | ldr w8,[x2, #0xa0] | `FALL_THROUGH`
<a id="insn-00babfc0"></a> `00babfc0` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00babfc4"></a> `00babfc4` | `c8 13 00 54` | b.hi 0x00bac23c | `CONDITIONAL_JUMP`
<a id="insn-00babfc8"></a> `00babfc8` | `09 bb ff f0` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00babfcc"></a> `00babfcc` | `29 cd 09 91` | add x9,x9,#0x273 | `FALL_THROUGH`
<a id="insn-00babfd0"></a> `00babfd0` | `ca 00 00 10` | adr x10,0xbabfe8 | `FALL_THROUGH`
<a id="insn-00babfd4"></a> `00babfd4` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00babfd8"></a> `00babfd8` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00babfdc"></a> `00babfdc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00babfe0"></a> `00babfe0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00babfe4"></a> `00babfe4` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00babfe8"></a> `00babfe8` | `54 00 00 b4` | cbz x20,0x00babff0 | `CONDITIONAL_JUMP`
<a id="insn-00babfec"></a> `00babfec` | `13 13 00 b5` | cbnz x19,0x00bac24c | `CONDITIONAL_JUMP`
<a id="insn-00babff0"></a> `00babff0` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00babff4"></a> `00babff4` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00babff8"></a> `00babff8` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00babffc"></a> `00babffc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac000"></a> `00bac000` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac004"></a> `00bac004` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac008"></a> `00bac008` | `a9 1f 00 34` | cbz w9,0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac00c"></a> `00bac00c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac010"></a> `00bac010` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac014"></a> `00bac014` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac018"></a> `00bac018` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac01c"></a> `00bac01c` | `83 1d 00 54` | b.cc 0x00bac3cc | `CONDITIONAL_JUMP`
<a id="insn-00bac020"></a> `00bac020` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac024"></a> `00bac024` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac028"></a> `00bac028` | `49 ff ff 35` | cbnz w9,0x00bac010 | `CONDITIONAL_JUMP`
<a id="insn-00bac02c"></a> `00bac02c` | `f4 00 00 14` | b 0x00bac3fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac030"></a> `00bac030` | `74 00 00 b4` | cbz x20,0x00bac03c | `CONDITIONAL_JUMP`
<a id="insn-00bac034"></a> `00bac034` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00bac038"></a> `00bac038` | `b3 02 00 b5` | cbnz x19,0x00bac08c | `CONDITIONAL_JUMP`
<a id="insn-00bac03c"></a> `00bac03c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac040"></a> `00bac040` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac044"></a> `00bac044` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac048"></a> `00bac048` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac04c"></a> `00bac04c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac050"></a> `00bac050` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac054"></a> `00bac054` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac058"></a> `00bac058` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac05c"></a> `00bac05c` | `7d b5 02 94` | bl 0x00c59650 | `UNCONDITIONAL_CALL`
<a id="insn-00bac060"></a> `00bac060` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac064"></a> `00bac064` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00bac068"></a> `00bac068` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bac06c"></a> `00bac06c` | `00 01 00 54` | b.eq 0x00bac08c | `CONDITIONAL_JUMP`
<a id="insn-00bac070"></a> `00bac070` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bac074"></a> `00bac074` | `c8 00 00 35` | cbnz w8,0x00bac08c | `CONDITIONAL_JUMP`
<a id="insn-00bac078"></a> `00bac078` | `00 20 20 1e` | fcmp s0,s0 | `FALL_THROUGH`
<a id="insn-00bac07c"></a> `00bac07c` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00bac080"></a> `00bac080` | `67 00 00 54` | b.vc 0x00bac08c | `CONDITIONAL_JUMP`
<a id="insn-00bac084"></a> `00bac084` | `08 f8 af 52` | mov w8,#0x7fc00000 | `FALL_THROUGH`
<a id="insn-00bac088"></a> `00bac088` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00bac08c"></a> `00bac08c` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bac090"></a> `00bac090` | `54 00 00 b4` | cbz x20,0x00bac098 | `CONDITIONAL_JUMP`
<a id="insn-00bac094"></a> `00bac094` | `80 02 40 bd` | ldr s0,[x20] | `FALL_THROUGH`
<a id="insn-00bac098"></a> `00bac098` | `53 00 00 b4` | cbz x19,0x00bac0a0 | `CONDITIONAL_JUMP`
<a id="insn-00bac09c"></a> `00bac09c` | `61 02 40 bd` | ldr s1,[x19] | `FALL_THROUGH`
<a id="insn-00bac0a0"></a> `00bac0a0` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bac0a4"></a> `00bac0a4` | `46 00 00 14` | b 0x00bac1bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac0a8"></a> `00bac0a8` | `54 00 00 b4` | cbz x20,0x00bac0b0 | `CONDITIONAL_JUMP`
<a id="insn-00bac0ac"></a> `00bac0ac` | `13 0d 00 b5` | cbnz x19,0x00bac24c | `CONDITIONAL_JUMP`
<a id="insn-00bac0b0"></a> `00bac0b0` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac0b4"></a> `00bac0b4` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac0b8"></a> `00bac0b8` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac0bc"></a> `00bac0bc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0c0"></a> `00bac0c0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac0c4"></a> `00bac0c4` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac0c8"></a> `00bac0c8` | `a9 19 00 34` | cbz w9,0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac0cc"></a> `00bac0cc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0d0"></a> `00bac0d0` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac0d4"></a> `00bac0d4` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac0d8"></a> `00bac0d8` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac0dc"></a> `00bac0dc` | `83 17 00 54` | b.cc 0x00bac3cc | `CONDITIONAL_JUMP`
<a id="insn-00bac0e0"></a> `00bac0e0` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac0e4"></a> `00bac0e4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac0e8"></a> `00bac0e8` | `49 ff ff 35` | cbnz w9,0x00bac0d0 | `CONDITIONAL_JUMP`
<a id="insn-00bac0ec"></a> `00bac0ec` | `c4 00 00 14` | b 0x00bac3fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac0f0"></a> `00bac0f0` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bac0f4"></a> `00bac0f4` | `54 00 00 b4` | cbz x20,0x00bac0fc | `CONDITIONAL_JUMP`
<a id="insn-00bac0f8"></a> `00bac0f8` | `53 01 00 b5` | cbnz x19,0x00bac120 | `CONDITIONAL_JUMP`
<a id="insn-00bac0fc"></a> `00bac0fc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac100"></a> `00bac100` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac104"></a> `00bac104` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac108"></a> `00bac108` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bac10c"></a> `00bac10c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac110"></a> `00bac110` | `41 01 89 9a` | csel x1,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac114"></a> `00bac114` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bac118"></a> `00bac118` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bac11c"></a> `00bac11c` | `4d c4 02 94` | bl 0x00c5d250 | `UNCONDITIONAL_CALL`
<a id="insn-00bac120"></a> `00bac120` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bac124"></a> `00bac124` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bac128"></a> `00bac128` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bac12c"></a> `00bac12c` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bac130"></a> `00bac130` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bac134"></a> `00bac134` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bac138"></a> `00bac138` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bac13c"></a> `00bac13c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bac140"></a> `00bac140` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bac144"></a> `00bac144` | `c7 00 00 14` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac148"></a> `00bac148` | `74 00 00 b4` | cbz x20,0x00bac154 | `CONDITIONAL_JUMP`
<a id="insn-00bac14c"></a> `00bac14c` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bac150"></a> `00bac150` | `b3 02 00 b5` | cbnz x19,0x00bac1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac154"></a> `00bac154` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac158"></a> `00bac158` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac15c"></a> `00bac15c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac160"></a> `00bac160` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac164"></a> `00bac164` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac168"></a> `00bac168` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac16c"></a> `00bac16c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac170"></a> `00bac170` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac174"></a> `00bac174` | `3b b5 02 94` | bl 0x00c59660 | `UNCONDITIONAL_CALL`
<a id="insn-00bac178"></a> `00bac178` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac17c"></a> `00bac17c` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bac180"></a> `00bac180` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bac184"></a> `00bac184` | `00 01 00 54` | b.eq 0x00bac1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac188"></a> `00bac188` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bac18c"></a> `00bac18c` | `c8 00 00 35` | cbnz w8,0x00bac1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac190"></a> `00bac190` | `00 20 60 1e` | fcmp d0,d0 | `FALL_THROUGH`
<a id="insn-00bac194"></a> `00bac194` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00bac198"></a> `00bac198` | `67 00 00 54` | b.vc 0x00bac1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac19c"></a> `00bac19c` | `08 ff ef d2` | mov x8,#0x7ff8000000000000 | `FALL_THROUGH`
<a id="insn-00bac1a0"></a> `00bac1a0` | `01 01 67 9e` | fmov d1,x8 | `FALL_THROUGH`
<a id="insn-00bac1a4"></a> `00bac1a4` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bac1a8"></a> `00bac1a8` | `54 00 00 b4` | cbz x20,0x00bac1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bac1ac"></a> `00bac1ac` | `80 02 40 fd` | ldr d0,[x20] | `FALL_THROUGH`
<a id="insn-00bac1b0"></a> `00bac1b0` | `53 00 00 b4` | cbz x19,0x00bac1b8 | `CONDITIONAL_JUMP`
<a id="insn-00bac1b4"></a> `00bac1b4` | `61 02 40 fd` | ldr d1,[x19] | `FALL_THROUGH`
<a id="insn-00bac1b8"></a> `00bac1b8` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00bac1bc"></a> `00bac1bc` | `e0 57 9f 1a` | cset w0,mi | `FALL_THROUGH`
<a id="insn-00bac1c0"></a> `00bac1c0` | `a8 00 00 14` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac1c4"></a> `00bac1c4` | `54 00 00 b4` | cbz x20,0x00bac1cc | `CONDITIONAL_JUMP`
<a id="insn-00bac1c8"></a> `00bac1c8` | `33 04 00 b5` | cbnz x19,0x00bac24c | `CONDITIONAL_JUMP`
<a id="insn-00bac1cc"></a> `00bac1cc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac1d0"></a> `00bac1d0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac1d4"></a> `00bac1d4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac1d8"></a> `00bac1d8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1dc"></a> `00bac1dc` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac1e0"></a> `00bac1e0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac1e4"></a> `00bac1e4` | `c9 10 00 34` | cbz w9,0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac1e8"></a> `00bac1e8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac1ec"></a> `00bac1ec` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac1f0"></a> `00bac1f0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac1f4"></a> `00bac1f4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac1f8"></a> `00bac1f8` | `a3 0e 00 54` | b.cc 0x00bac3cc | `CONDITIONAL_JUMP`
<a id="insn-00bac1fc"></a> `00bac1fc` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac200"></a> `00bac200` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac204"></a> `00bac204` | `49 ff ff 35` | cbnz w9,0x00bac1ec | `CONDITIONAL_JUMP`
<a id="insn-00bac208"></a> `00bac208` | `7d 00 00 14` | b 0x00bac3fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac20c"></a> `00bac20c` | `14 08 00 b4` | cbz x20,0x00bac30c | `CONDITIONAL_JUMP`
<a id="insn-00bac210"></a> `00bac210` | `f3 07 00 b4` | cbz x19,0x00bac30c | `CONDITIONAL_JUMP`
<a id="insn-00bac214"></a> `00bac214` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac218"></a> `00bac218` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac21c"></a> `00bac21c` | `34 30 00 b5` | cbnz x20,0x00bac820 | `CONDITIONAL_JUMP`
<a id="insn-00bac220"></a> `00bac220` | `81 01 00 14` | b 0x00bac824 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac224"></a> `00bac224` | `54 09 00 b4` | cbz x20,0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac228"></a> `00bac228` | `33 09 00 b4` | cbz x19,0x00bac34c | `CONDITIONAL_JUMP`
<a id="insn-00bac22c"></a> `00bac22c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac230"></a> `00bac230` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac234"></a> `00bac234` | `f4 20 00 b5` | cbnz x20,0x00bac650 | `CONDITIONAL_JUMP`
<a id="insn-00bac238"></a> `00bac238` | `07 01 00 14` | b 0x00bac654 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac23c"></a> `00bac23c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bac240"></a> `00bac240` | `88 00 00 14` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac244"></a> `00bac244` | `54 0a 00 b4` | cbz x20,0x00bac38c | `CONDITIONAL_JUMP`
<a id="insn-00bac248"></a> `00bac248` | `33 0a 00 b4` | cbz x19,0x00bac38c | `CONDITIONAL_JUMP`
<a id="insn-00bac24c"></a> `00bac24c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac250"></a> `00bac250` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac254"></a> `00bac254` | `b4 0f 00 b5` | cbnz x20,0x00bac448 | `CONDITIONAL_JUMP`
<a id="insn-00bac258"></a> `00bac258` | `7d 00 00 14` | b 0x00bac44c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac25c"></a> `00bac25c` | `54 11 00 b4` | cbz x20,0x00bac484 | `CONDITIONAL_JUMP`
<a id="insn-00bac260"></a> `00bac260` | `33 11 00 b4` | cbz x19,0x00bac484 | `CONDITIONAL_JUMP`
<a id="insn-00bac264"></a> `00bac264` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac268"></a> `00bac268` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac26c"></a> `00bac26c` | `34 2f 00 b5` | cbnz x20,0x00bac850 | `CONDITIONAL_JUMP`
<a id="insn-00bac270"></a> `00bac270` | `79 01 00 14` | b 0x00bac854 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac274"></a> `00bac274` | `94 12 00 b4` | cbz x20,0x00bac4c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac278"></a> `00bac278` | `73 12 00 b4` | cbz x19,0x00bac4c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac27c"></a> `00bac27c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac280"></a> `00bac280` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac284"></a> `00bac284` | `14 27 00 b5` | cbnz x20,0x00bac764 | `CONDITIONAL_JUMP`
<a id="insn-00bac288"></a> `00bac288` | `38 01 00 14` | b 0x00bac768 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac28c"></a> `00bac28c` | `d4 13 00 b4` | cbz x20,0x00bac504 | `CONDITIONAL_JUMP`
<a id="insn-00bac290"></a> `00bac290` | `b3 13 00 b4` | cbz x19,0x00bac504 | `CONDITIONAL_JUMP`
<a id="insn-00bac294"></a> `00bac294` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac298"></a> `00bac298` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac29c"></a> `00bac29c` | `f4 2a 00 b5` | cbnz x20,0x00bac7f8 | `CONDITIONAL_JUMP`
<a id="insn-00bac2a0"></a> `00bac2a0` | `57 01 00 14` | b 0x00bac7fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac2a4"></a> `00bac2a4` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bac2a8"></a> `00bac2a8` | `54 00 00 b4` | cbz x20,0x00bac2b0 | `CONDITIONAL_JUMP`
<a id="insn-00bac2ac"></a> `00bac2ac` | `33 2f 00 b5` | cbnz x19,0x00bac890 | `CONDITIONAL_JUMP`
<a id="insn-00bac2b0"></a> `00bac2b0` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac2b4"></a> `00bac2b4` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac2b8"></a> `00bac2b8` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac2bc"></a> `00bac2bc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bac2c0"></a> `00bac2c0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac2c4"></a> `00bac2c4` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac2c8"></a> `00bac2c8` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bac2cc"></a> `00bac2cc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bac2d0"></a> `00bac2d0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bac2d4"></a> `00bac2d4` | `e3 c3 02 94` | bl 0x00c5d260 | `UNCONDITIONAL_CALL`
<a id="insn-00bac2d8"></a> `00bac2d8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac2dc"></a> `00bac2dc` | `a8 2d 00 b4` | cbz x8,0x00bac890 | `CONDITIONAL_JUMP`
<a id="insn-00bac2e0"></a> `00bac2e0` | `80 2d 00 36` | tbz w0,#0x0,0x00bac890 | `CONDITIONAL_JUMP`
<a id="insn-00bac2e4"></a> `00bac2e4` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac2e8"></a> `00bac2e8` | `29 2c 00 34` | cbz w9,0x00bac86c | `CONDITIONAL_JUMP`
<a id="insn-00bac2ec"></a> `00bac2ec` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bac2f0"></a> `00bac2f0` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac2f4"></a> `00bac2f4` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac2f8"></a> `00bac2f8` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bac2fc"></a> `00bac2fc` | `a3 2b 00 54` | b.cc 0x00bac870 | `CONDITIONAL_JUMP`
<a id="insn-00bac300"></a> `00bac300` | `09 1d 40 38` | ldrb w9,[x8, #0x1]! | `FALL_THROUGH`
<a id="insn-00bac304"></a> `00bac304` | `69 ff ff 35` | cbnz w9,0x00bac2f0 | `CONDITIONAL_JUMP`
<a id="insn-00bac308"></a> `00bac308` | `5a 01 00 14` | b 0x00bac870 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac30c"></a> `00bac30c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac310"></a> `00bac310` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac314"></a> `00bac314` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac318"></a> `00bac318` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac31c"></a> `00bac31c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac320"></a> `00bac320` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac324"></a> `00bac324` | `89 12 00 34` | cbz w9,0x00bac574 | `CONDITIONAL_JUMP`
<a id="insn-00bac328"></a> `00bac328` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac32c"></a> `00bac32c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac330"></a> `00bac330` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac334"></a> `00bac334` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac338"></a> `00bac338` | `63 10 00 54` | b.cc 0x00bac544 | `CONDITIONAL_JUMP`
<a id="insn-00bac33c"></a> `00bac33c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac340"></a> `00bac340` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac344"></a> `00bac344` | `49 ff ff 35` | cbnz w9,0x00bac32c | `CONDITIONAL_JUMP`
<a id="insn-00bac348"></a> `00bac348` | `8b 00 00 14` | b 0x00bac574 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac34c"></a> `00bac34c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac350"></a> `00bac350` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac354"></a> `00bac354` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac358"></a> `00bac358` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac35c"></a> `00bac35c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac360"></a> `00bac360` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac364"></a> `00bac364` | `89 14 00 34` | cbz w9,0x00bac5f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac368"></a> `00bac368` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac36c"></a> `00bac36c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac370"></a> `00bac370` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac374"></a> `00bac374` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac378"></a> `00bac378` | `63 12 00 54` | b.cc 0x00bac5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bac37c"></a> `00bac37c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac380"></a> `00bac380` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac384"></a> `00bac384` | `49 ff ff 35` | cbnz w9,0x00bac36c | `CONDITIONAL_JUMP`
<a id="insn-00bac388"></a> `00bac388` | `9b 00 00 14` | b 0x00bac5f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac38c"></a> `00bac38c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac390"></a> `00bac390` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac394"></a> `00bac394` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac398"></a> `00bac398` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac39c"></a> `00bac39c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac3a0"></a> `00bac3a0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac3a4"></a> `00bac3a4` | `c9 02 00 34` | cbz w9,0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac3a8"></a> `00bac3a8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3ac"></a> `00bac3ac` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac3b0"></a> `00bac3b0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac3b4"></a> `00bac3b4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac3b8"></a> `00bac3b8` | `a3 00 00 54` | b.cc 0x00bac3cc | `CONDITIONAL_JUMP`
<a id="insn-00bac3bc"></a> `00bac3bc` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac3c0"></a> `00bac3c0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac3c4"></a> `00bac3c4` | `49 ff ff 35` | cbnz w9,0x00bac3ac | `CONDITIONAL_JUMP`
<a id="insn-00bac3c8"></a> `00bac3c8` | `0d 00 00 14` | b 0x00bac3fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bac3cc"></a> `00bac3cc` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac3d0"></a> `00bac3d0` | `61 01 00 54` | b.ne 0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac3d4"></a> `00bac3d4` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac3d8"></a> `00bac3d8` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac3dc"></a> `00bac3dc` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac3e0"></a> `00bac3e0` | `e1 00 00 54` | b.ne 0x00bac3fc | `CONDITIONAL_JUMP`
<a id="insn-00bac3e4"></a> `00bac3e4` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac3e8"></a> `00bac3e8` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac3ec"></a> `00bac3ec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac3f0"></a> `00bac3f0` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac3f4"></a> `00bac3f4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac3f8"></a> `00bac3f8` | `06 00 00 14` | b 0x00bac410 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac3fc"></a> `00bac3fc` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac400"></a> `00bac400` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac404"></a> `00bac404` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac408"></a> `00bac408` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac40c"></a> `00bac40c` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac410"></a> `00bac410` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac414"></a> `00bac414` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac418"></a> `00bac418` | `76 c7 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac41c"></a> `00bac41c` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac420"></a> `00bac420` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac424"></a> `00bac424` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac428"></a> `00bac428` | `c0 00 00 54` | b.eq 0x00bac440 | `CONDITIONAL_JUMP`
<a id="insn-00bac42c"></a> `00bac42c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac430"></a> `00bac430` | `89 00 00 35` | cbnz w9,0x00bac440 | `CONDITIONAL_JUMP`
<a id="insn-00bac434"></a> `00bac434` | `1f fc 03 f1` | cmp x0,#0xff | `FALL_THROUGH`
<a id="insn-00bac438"></a> `00bac438` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00bac43c"></a> `00bac43c` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bac440"></a> `00bac440` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac444"></a> `00bac444` | `54 00 00 b4` | cbz x20,0x00bac44c | `CONDITIONAL_JUMP`
<a id="insn-00bac448"></a> `00bac448` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac44c"></a> `00bac44c` | `53 00 00 b4` | cbz x19,0x00bac454 | `CONDITIONAL_JUMP`
<a id="insn-00bac450"></a> `00bac450` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac454"></a> `00bac454` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac458"></a> `00bac458` | `3f 01 28 6b` | cmp w9,w8, UXTB  | `FALL_THROUGH`
<a id="insn-00bac45c"></a> `00bac45c` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00bac460"></a> `00bac460` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bac464"></a> `00bac464` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bac468"></a> `00bac468` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bac46c"></a> `00bac46c` | `41 22 00 54` | b.ne 0x00bac8b4 | `CONDITIONAL_JUMP`
<a id="insn-00bac470"></a> `00bac470` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bac474"></a> `00bac474` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bac478"></a> `00bac478` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bac47c"></a> `00bac47c` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bac480"></a> `00bac480` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bac484"></a> `00bac484` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac488"></a> `00bac488` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac48c"></a> `00bac48c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac490"></a> `00bac490` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac494"></a> `00bac494` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac498"></a> `00bac498` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac49c"></a> `00bac49c` | `e9 0f 00 34` | cbz w9,0x00bac698 | `CONDITIONAL_JUMP`
<a id="insn-00bac4a0"></a> `00bac4a0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4a4"></a> `00bac4a4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac4a8"></a> `00bac4a8` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac4ac"></a> `00bac4ac` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac4b0"></a> `00bac4b0` | `c3 0d 00 54` | b.cc 0x00bac668 | `CONDITIONAL_JUMP`
<a id="insn-00bac4b4"></a> `00bac4b4` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac4b8"></a> `00bac4b8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4bc"></a> `00bac4bc` | `49 ff ff 35` | cbnz w9,0x00bac4a4 | `CONDITIONAL_JUMP`
<a id="insn-00bac4c0"></a> `00bac4c0` | `76 00 00 14` | b 0x00bac698 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac4c4"></a> `00bac4c4` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac4c8"></a> `00bac4c8` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac4cc"></a> `00bac4cc` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac4d0"></a> `00bac4d0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4d4"></a> `00bac4d4` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac4d8"></a> `00bac4d8` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac4dc"></a> `00bac4dc` | `e9 11 00 34` | cbz w9,0x00bac718 | `CONDITIONAL_JUMP`
<a id="insn-00bac4e0"></a> `00bac4e0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4e4"></a> `00bac4e4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac4e8"></a> `00bac4e8` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac4ec"></a> `00bac4ec` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac4f0"></a> `00bac4f0` | `c3 0f 00 54` | b.cc 0x00bac6e8 | `CONDITIONAL_JUMP`
<a id="insn-00bac4f4"></a> `00bac4f4` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac4f8"></a> `00bac4f8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac4fc"></a> `00bac4fc` | `49 ff ff 35` | cbnz w9,0x00bac4e4 | `CONDITIONAL_JUMP`
<a id="insn-00bac500"></a> `00bac500` | `86 00 00 14` | b 0x00bac718 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac504"></a> `00bac504` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bac508"></a> `00bac508` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bac50c"></a> `00bac50c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bac510"></a> `00bac510` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac514"></a> `00bac514` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bac518"></a> `00bac518` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bac51c"></a> `00bac51c` | `89 14 00 34` | cbz w9,0x00bac7ac | `CONDITIONAL_JUMP`
<a id="insn-00bac520"></a> `00bac520` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac524"></a> `00bac524` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bac528"></a> `00bac528` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac52c"></a> `00bac52c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bac530"></a> `00bac530` | `63 12 00 54` | b.cc 0x00bac77c | `CONDITIONAL_JUMP`
<a id="insn-00bac534"></a> `00bac534` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac538"></a> `00bac538` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac53c"></a> `00bac53c` | `49 ff ff 35` | cbnz w9,0x00bac524 | `CONDITIONAL_JUMP`
<a id="insn-00bac540"></a> `00bac540` | `9b 00 00 14` | b 0x00bac7ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bac544"></a> `00bac544` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac548"></a> `00bac548` | `61 01 00 54` | b.ne 0x00bac574 | `CONDITIONAL_JUMP`
<a id="insn-00bac54c"></a> `00bac54c` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac550"></a> `00bac550` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac554"></a> `00bac554` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac558"></a> `00bac558` | `e1 00 00 54` | b.ne 0x00bac574 | `CONDITIONAL_JUMP`
<a id="insn-00bac55c"></a> `00bac55c` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac560"></a> `00bac560` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac564"></a> `00bac564` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac568"></a> `00bac568` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac56c"></a> `00bac56c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac570"></a> `00bac570` | `06 00 00 14` | b 0x00bac588 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac574"></a> `00bac574` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac578"></a> `00bac578` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac57c"></a> `00bac57c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac580"></a> `00bac580` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac584"></a> `00bac584` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac588"></a> `00bac588` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac58c"></a> `00bac58c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac590"></a> `00bac590` | `18 c7 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac594"></a> `00bac594` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac598"></a> `00bac598` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac59c"></a> `00bac59c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac5a0"></a> `00bac5a0` | `c0 13 00 54` | b.eq 0x00bac818 | `CONDITIONAL_JUMP`
<a id="insn-00bac5a4"></a> `00bac5a4` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac5a8"></a> `00bac5a8` | `89 13 00 35` | cbnz w9,0x00bac818 | `CONDITIONAL_JUMP`
<a id="insn-00bac5ac"></a> `00bac5ac` | `1f fc 01 f1` | cmp x0,#0x7f | `FALL_THROUGH`
<a id="insn-00bac5b0"></a> `00bac5b0` | `ed 12 00 54` | b.le 0x00bac80c | `CONDITIONAL_JUMP`
<a id="insn-00bac5b4"></a> `00bac5b4` | `e8 0f 80 52` | mov w8,#0x7f | `FALL_THROUGH`
<a id="insn-00bac5b8"></a> `00bac5b8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac5bc"></a> `00bac5bc` | `34 13 00 b5` | cbnz x20,0x00bac820 | `CONDITIONAL_JUMP`
<a id="insn-00bac5c0"></a> `00bac5c0` | `99 00 00 14` | b 0x00bac824 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac5c4"></a> `00bac5c4` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac5c8"></a> `00bac5c8` | `61 01 00 54` | b.ne 0x00bac5f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac5cc"></a> `00bac5cc` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac5d0"></a> `00bac5d0` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac5d4"></a> `00bac5d4` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac5d8"></a> `00bac5d8` | `e1 00 00 54` | b.ne 0x00bac5f4 | `CONDITIONAL_JUMP`
<a id="insn-00bac5dc"></a> `00bac5dc` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac5e0"></a> `00bac5e0` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac5e4"></a> `00bac5e4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac5e8"></a> `00bac5e8` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac5ec"></a> `00bac5ec` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac5f0"></a> `00bac5f0` | `06 00 00 14` | b 0x00bac608 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac5f4"></a> `00bac5f4` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac5f8"></a> `00bac5f8` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac5fc"></a> `00bac5fc` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac600"></a> `00bac600` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac604"></a> `00bac604` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac608"></a> `00bac608` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac60c"></a> `00bac60c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac610"></a> `00bac610` | `f8 c6 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac614"></a> `00bac614` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac618"></a> `00bac618` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac61c"></a> `00bac61c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac620"></a> `00bac620` | `40 01 00 54` | b.eq 0x00bac648 | `CONDITIONAL_JUMP`
<a id="insn-00bac624"></a> `00bac624` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac628"></a> `00bac628` | `09 01 00 35` | cbnz w9,0x00bac648 | `CONDITIONAL_JUMP`
<a id="insn-00bac62c"></a> `00bac62c` | `08 00 b0 12` | mov w8,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00bac630"></a> `00bac630` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bac634"></a> `00bac634` | `ac 00 00 54` | b.gt 0x00bac648 | `CONDITIONAL_JUMP`
<a id="insn-00bac638"></a> `00bac638` | `e8 83 61 b2` | orr x8,xzr,#-0x80000000 | `FALL_THROUGH`
<a id="insn-00bac63c"></a> `00bac63c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bac640"></a> `00bac640` | `08 00 b0 52` | mov w8,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bac644"></a> `00bac644` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bac648"></a> `00bac648` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac64c"></a> `00bac64c` | `54 00 00 b4` | cbz x20,0x00bac654 | `CONDITIONAL_JUMP`
<a id="insn-00bac650"></a> `00bac650` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac654"></a> `00bac654` | `53 00 00 b4` | cbz x19,0x00bac65c | `CONDITIONAL_JUMP`
<a id="insn-00bac658"></a> `00bac658` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac65c"></a> `00bac65c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bac660"></a> `00bac660` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bac664"></a> `00bac664` | `7f ff ff 17` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac668"></a> `00bac668` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac66c"></a> `00bac66c` | `61 01 00 54` | b.ne 0x00bac698 | `CONDITIONAL_JUMP`
<a id="insn-00bac670"></a> `00bac670` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac674"></a> `00bac674` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac678"></a> `00bac678` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac67c"></a> `00bac67c` | `e1 00 00 54` | b.ne 0x00bac698 | `CONDITIONAL_JUMP`
<a id="insn-00bac680"></a> `00bac680` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac684"></a> `00bac684` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac688"></a> `00bac688` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac68c"></a> `00bac68c` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac690"></a> `00bac690` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac694"></a> `00bac694` | `06 00 00 14` | b 0x00bac6ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bac698"></a> `00bac698` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac69c"></a> `00bac69c` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac6a0"></a> `00bac6a0` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac6a4"></a> `00bac6a4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac6a8"></a> `00bac6a8` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac6ac"></a> `00bac6ac` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac6b0"></a> `00bac6b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac6b4"></a> `00bac6b4` | `cf c6 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac6b8"></a> `00bac6b8` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac6bc"></a> `00bac6bc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac6c0"></a> `00bac6c0` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac6c4"></a> `00bac6c4` | `20 0c 00 54` | b.eq 0x00bac848 | `CONDITIONAL_JUMP`
<a id="insn-00bac6c8"></a> `00bac6c8` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac6cc"></a> `00bac6cc` | `e9 0b 00 35` | cbnz w9,0x00bac848 | `CONDITIONAL_JUMP`
<a id="insn-00bac6d0"></a> `00bac6d0` | `1f 20 40 f1` | cmp x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bac6d4"></a> `00bac6d4` | `4b 0b 00 54` | b.lt 0x00bac83c | `CONDITIONAL_JUMP`
<a id="insn-00bac6d8"></a> `00bac6d8` | `e8 ff 8f 52` | mov w8,#0x7fff | `FALL_THROUGH`
<a id="insn-00bac6dc"></a> `00bac6dc` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac6e0"></a> `00bac6e0` | `94 0b 00 b5` | cbnz x20,0x00bac850 | `CONDITIONAL_JUMP`
<a id="insn-00bac6e4"></a> `00bac6e4` | `5c 00 00 14` | b 0x00bac854 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac6e8"></a> `00bac6e8` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac6ec"></a> `00bac6ec` | `61 01 00 54` | b.ne 0x00bac718 | `CONDITIONAL_JUMP`
<a id="insn-00bac6f0"></a> `00bac6f0` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac6f4"></a> `00bac6f4` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac6f8"></a> `00bac6f8` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac6fc"></a> `00bac6fc` | `e1 00 00 54` | b.ne 0x00bac718 | `CONDITIONAL_JUMP`
<a id="insn-00bac700"></a> `00bac700` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac704"></a> `00bac704` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac708"></a> `00bac708` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac70c"></a> `00bac70c` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac710"></a> `00bac710` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac714"></a> `00bac714` | `06 00 00 14` | b 0x00bac72c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac718"></a> `00bac718` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac71c"></a> `00bac71c` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac720"></a> `00bac720` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac724"></a> `00bac724` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac728"></a> `00bac728` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac72c"></a> `00bac72c` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac730"></a> `00bac730` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac734"></a> `00bac734` | `af c6 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac738"></a> `00bac738` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac73c"></a> `00bac73c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac740"></a> `00bac740` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac744"></a> `00bac744` | `c0 00 00 54` | b.eq 0x00bac75c | `CONDITIONAL_JUMP`
<a id="insn-00bac748"></a> `00bac748` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac74c"></a> `00bac74c` | `89 00 00 35` | cbnz w9,0x00bac75c | `CONDITIONAL_JUMP`
<a id="insn-00bac750"></a> `00bac750` | `e8 ff 9f 52` | mov w8,#0xffff | `FALL_THROUGH`
<a id="insn-00bac754"></a> `00bac754` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bac758"></a> `00bac758` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bac75c"></a> `00bac75c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac760"></a> `00bac760` | `54 00 00 b4` | cbz x20,0x00bac768 | `CONDITIONAL_JUMP`
<a id="insn-00bac764"></a> `00bac764` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac768"></a> `00bac768` | `53 00 00 b4` | cbz x19,0x00bac770 | `CONDITIONAL_JUMP`
<a id="insn-00bac76c"></a> `00bac76c` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac770"></a> `00bac770` | `29 3d 00 12` | and w9,w9,#0xffff | `FALL_THROUGH`
<a id="insn-00bac774"></a> `00bac774` | `3f 21 28 6b` | cmp w9,w8, UXTH  | `FALL_THROUGH`
<a id="insn-00bac778"></a> `00bac778` | `39 ff ff 17` | b 0x00bac45c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac77c"></a> `00bac77c` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bac780"></a> `00bac780` | `61 01 00 54` | b.ne 0x00bac7ac | `CONDITIONAL_JUMP`
<a id="insn-00bac784"></a> `00bac784` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bac788"></a> `00bac788` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bac78c"></a> `00bac78c` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bac790"></a> `00bac790` | `e1 00 00 54` | b.ne 0x00bac7ac | `CONDITIONAL_JUMP`
<a id="insn-00bac794"></a> `00bac794` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac798"></a> `00bac798` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac79c"></a> `00bac79c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac7a0"></a> `00bac7a0` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bac7a4"></a> `00bac7a4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac7a8"></a> `00bac7a8` | `06 00 00 14` | b 0x00bac7c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac7ac"></a> `00bac7ac` | `88 07 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bac7b0"></a> `00bac7b0` | `08 69 44 f9` | ldr x8,[x8, #0x8d0] | `FALL_THROUGH`
<a id="insn-00bac7b4"></a> `00bac7b4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bac7b8"></a> `00bac7b8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bac7bc"></a> `00bac7bc` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bac7c0"></a> `00bac7c0` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bac7c4"></a> `00bac7c4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bac7c8"></a> `00bac7c8` | `8a c6 02 94` | bl 0x00c5e1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bac7cc"></a> `00bac7cc` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bac7d0"></a> `00bac7d0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bac7d4"></a> `00bac7d4` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bac7d8"></a> `00bac7d8` | `c0 00 00 54` | b.eq 0x00bac7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bac7dc"></a> `00bac7dc` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bac7e0"></a> `00bac7e0` | `89 00 00 35` | cbnz w9,0x00bac7f0 | `CONDITIONAL_JUMP`
<a id="insn-00bac7e4"></a> `00bac7e4` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bac7e8"></a> `00bac7e8` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bac7ec"></a> `00bac7ec` | `08 30 9f 5a` | csinv w8,w0,wzr,cc | `FALL_THROUGH`
<a id="insn-00bac7f0"></a> `00bac7f0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac7f4"></a> `00bac7f4` | `54 00 00 b4` | cbz x20,0x00bac7fc | `CONDITIONAL_JUMP`
<a id="insn-00bac7f8"></a> `00bac7f8` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac7fc"></a> `00bac7fc` | `53 00 00 b4` | cbz x19,0x00bac804 | `CONDITIONAL_JUMP`
<a id="insn-00bac800"></a> `00bac800` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac804"></a> `00bac804` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bac808"></a> `00bac808` | `15 ff ff 17` | b 0x00bac45c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac80c"></a> `00bac80c` | `1f 00 02 b1` | cmn x0,#0x80 | `FALL_THROUGH`
<a id="insn-00bac810"></a> `00bac810` | `e8 0f 80 12` | mov w8,#0xffffff80 | `FALL_THROUGH`
<a id="insn-00bac814"></a> `00bac814` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bac818"></a> `00bac818` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac81c"></a> `00bac81c` | `54 00 00 b4` | cbz x20,0x00bac824 | `CONDITIONAL_JUMP`
<a id="insn-00bac820"></a> `00bac820` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac824"></a> `00bac824` | `53 00 00 b4` | cbz x19,0x00bac82c | `CONDITIONAL_JUMP`
<a id="insn-00bac828"></a> `00bac828` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac82c"></a> `00bac82c` | `29 1d 00 13` | sxtb w9,w9 | `FALL_THROUGH`
<a id="insn-00bac830"></a> `00bac830` | `3f 81 28 6b` | cmp w9,w8, SXTB  | `FALL_THROUGH`
<a id="insn-00bac834"></a> `00bac834` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bac838"></a> `00bac838` | `0a ff ff 17` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac83c"></a> `00bac83c` | `1f 20 40 b1` | cmn x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bac840"></a> `00bac840` | `e8 ff 8f 12` | mov w8,#0xffff8000 | `FALL_THROUGH`
<a id="insn-00bac844"></a> `00bac844` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bac848"></a> `00bac848` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bac84c"></a> `00bac84c` | `54 00 00 b4` | cbz x20,0x00bac854 | `CONDITIONAL_JUMP`
<a id="insn-00bac850"></a> `00bac850` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bac854"></a> `00bac854` | `53 00 00 b4` | cbz x19,0x00bac85c | `CONDITIONAL_JUMP`
<a id="insn-00bac858"></a> `00bac858` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bac85c"></a> `00bac85c` | `29 3d 00 13` | sxth w9,w9 | `FALL_THROUGH`
<a id="insn-00bac860"></a> `00bac860` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00bac864"></a> `00bac864` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bac868"></a> `00bac868` | `fe fe ff 17` | b 0x00bac460 | `UNCONDITIONAL_JUMP`
<a id="insn-00bac86c"></a> `00bac86c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bac870"></a> `00bac870` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bac874"></a> `00bac874` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bac878"></a> `00bac878` | `28 81 88 9a` | csel x8,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bac87c"></a> `00bac87c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bac880"></a> `00bac880` | `1f b5 00 71` | cmp w8,#0x2d | `FALL_THROUGH`
<a id="insn-00bac884"></a> `00bac884` | `61 00 00 54` | b.ne 0x00bac890 | `CONDITIONAL_JUMP`
<a id="insn-00bac888"></a> `00bac888` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00bac88c"></a> `00bac88c` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bac890"></a> `00bac890` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bac894"></a> `00bac894` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bac898"></a> `00bac898` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bac89c"></a> `00bac89c` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bac8a0"></a> `00bac8a0` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bac8a4"></a> `00bac8a4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bac8a8"></a> `00bac8a8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bac8ac"></a> `00bac8ac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bac8b0"></a> `00bac8b0` | `eb fe ff 17` | b 0x00bac45c | `UNCONDITIONAL_JUMP`
<a id="insn-00bac8b4"></a> `00bac8b4` | `b3 b1 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babf9c`](#insn-00babf9c) 範囲 `[['00babf9c', '00babfaf']]`
  - `FALL_THROUGH` [`00babfac`](#insn-00babfac) → [`00babfb0`](#insn-00babfb0)
- ブロック [`00babfb0`](#insn-00babfb0) 範囲 `[['00babfb0', '00babfc7']]`
  - `CONDITIONAL_JUMP` [`00babfc4`](#insn-00babfc4) → [`00bac23c`](#insn-00bac23c)
  - `FALL_THROUGH` [`00babfc4`](#insn-00babfc4) → [`00babfc8`](#insn-00babfc8)
- ブロック [`00babfc8`](#insn-00babfc8) 範囲 `[['00babfc8', '00babfcf']]`
  - `FALL_THROUGH` [`00babfcc`](#insn-00babfcc) → [`00babfd0`](#insn-00babfd0)
- ブロック [`00babfd0`](#insn-00babfd0) 範囲 `[['00babfd0', '00babfe3']]`
  - `FALL_THROUGH` [`00babfe0`](#insn-00babfe0) → [`00babfe4`](#insn-00babfe4)
- ブロック [`00babfe4`](#insn-00babfe4) 範囲 `[['00babfe4', '00babfe7']]`
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00babfe8`](#insn-00babfe8)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac244`](#insn-00bac244)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac1c4`](#insn-00bac1c4)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac20c`](#insn-00bac20c)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac0a8`](#insn-00bac0a8)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac25c`](#insn-00bac25c)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac274`](#insn-00bac274)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac224`](#insn-00bac224)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac28c`](#insn-00bac28c)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac0f0`](#insn-00bac0f0)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac2a4`](#insn-00bac2a4)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac030`](#insn-00bac030)
  - `COMPUTED_JUMP` [`00babfe4`](#insn-00babfe4) → [`00bac148`](#insn-00bac148)
- ブロック [`00babfe8`](#insn-00babfe8) 範囲 `[['00babfe8', '00babfeb']]`
  - `CONDITIONAL_JUMP` [`00babfe8`](#insn-00babfe8) → [`00babff0`](#insn-00babff0)
  - `FALL_THROUGH` [`00babfe8`](#insn-00babfe8) → [`00babfec`](#insn-00babfec)
- ブロック [`00babfec`](#insn-00babfec) 範囲 `[['00babfec', '00babfef']]`
  - `CONDITIONAL_JUMP` [`00babfec`](#insn-00babfec) → [`00bac24c`](#insn-00bac24c)
  - `FALL_THROUGH` [`00babfec`](#insn-00babfec) → [`00babff0`](#insn-00babff0)
- ブロック [`00babff0`](#insn-00babff0) 範囲 `[['00babff0', '00babffb']]`
  - `FALL_THROUGH` [`00babff8`](#insn-00babff8) → [`00babffc`](#insn-00babffc)
- ブロック [`00babffc`](#insn-00babffc) 範囲 `[['00babffc', '00bac00b']]`
  - `CONDITIONAL_JUMP` [`00bac008`](#insn-00bac008) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac008`](#insn-00bac008) → [`00bac00c`](#insn-00bac00c)
- ブロック [`00bac00c`](#insn-00bac00c) 範囲 `[['00bac00c', '00bac00f']]`
  - `FALL_THROUGH` [`00bac00c`](#insn-00bac00c) → [`00bac010`](#insn-00bac010)
- ブロック [`00bac010`](#insn-00bac010) 範囲 `[['00bac010', '00bac01f']]`
  - `CONDITIONAL_JUMP` [`00bac01c`](#insn-00bac01c) → [`00bac3cc`](#insn-00bac3cc)
  - `FALL_THROUGH` [`00bac01c`](#insn-00bac01c) → [`00bac020`](#insn-00bac020)
- ブロック [`00bac020`](#insn-00bac020) 範囲 `[['00bac020', '00bac02b']]`
  - `CONDITIONAL_JUMP` [`00bac028`](#insn-00bac028) → [`00bac010`](#insn-00bac010)
  - `FALL_THROUGH` [`00bac028`](#insn-00bac028) → [`00bac02c`](#insn-00bac02c)
- ブロック [`00bac02c`](#insn-00bac02c) 範囲 `[['00bac02c', '00bac02f']]`
  - `UNCONDITIONAL_JUMP` [`00bac02c`](#insn-00bac02c) → [`00bac3fc`](#insn-00bac3fc)
- ブロック [`00bac030`](#insn-00bac030) 範囲 `[['00bac030', '00bac033']]`
  - `CONDITIONAL_JUMP` [`00bac030`](#insn-00bac030) → [`00bac03c`](#insn-00bac03c)
  - `FALL_THROUGH` [`00bac030`](#insn-00bac030) → [`00bac034`](#insn-00bac034)
- ブロック [`00bac034`](#insn-00bac034) 範囲 `[['00bac034', '00bac03b']]`
  - `CONDITIONAL_JUMP` [`00bac038`](#insn-00bac038) → [`00bac08c`](#insn-00bac08c)
  - `FALL_THROUGH` [`00bac038`](#insn-00bac038) → [`00bac03c`](#insn-00bac03c)
- ブロック [`00bac03c`](#insn-00bac03c) 範囲 `[['00bac03c', '00bac04b']]`
  - `FALL_THROUGH` [`00bac048`](#insn-00bac048) → [`00bac04c`](#insn-00bac04c)
- ブロック [`00bac04c`](#insn-00bac04c) 範囲 `[['00bac04c', '00bac06b']]`
  - `FALL_THROUGH` [`00bac068`](#insn-00bac068) → [`00bac06c`](#insn-00bac06c)
- ブロック [`00bac06c`](#insn-00bac06c) 範囲 `[['00bac06c', '00bac06f']]`
  - `CONDITIONAL_JUMP` [`00bac06c`](#insn-00bac06c) → [`00bac08c`](#insn-00bac08c)
  - `FALL_THROUGH` [`00bac06c`](#insn-00bac06c) → [`00bac070`](#insn-00bac070)
- ブロック [`00bac070`](#insn-00bac070) 範囲 `[['00bac070', '00bac077']]`
  - `CONDITIONAL_JUMP` [`00bac074`](#insn-00bac074) → [`00bac08c`](#insn-00bac08c)
  - `FALL_THROUGH` [`00bac074`](#insn-00bac074) → [`00bac078`](#insn-00bac078)
- ブロック [`00bac078`](#insn-00bac078) 範囲 `[['00bac078', '00bac083']]`
  - `CONDITIONAL_JUMP` [`00bac080`](#insn-00bac080) → [`00bac08c`](#insn-00bac08c)
  - `FALL_THROUGH` [`00bac080`](#insn-00bac080) → [`00bac084`](#insn-00bac084)
- ブロック [`00bac084`](#insn-00bac084) 範囲 `[['00bac084', '00bac08b']]`
  - `FALL_THROUGH` [`00bac088`](#insn-00bac088) → [`00bac08c`](#insn-00bac08c)
- ブロック [`00bac08c`](#insn-00bac08c) 範囲 `[['00bac08c', '00bac093']]`
  - `CONDITIONAL_JUMP` [`00bac090`](#insn-00bac090) → [`00bac098`](#insn-00bac098)
  - `FALL_THROUGH` [`00bac090`](#insn-00bac090) → [`00bac094`](#insn-00bac094)
- ブロック [`00bac094`](#insn-00bac094) 範囲 `[['00bac094', '00bac097']]`
  - `FALL_THROUGH` [`00bac094`](#insn-00bac094) → [`00bac098`](#insn-00bac098)
- ブロック [`00bac098`](#insn-00bac098) 範囲 `[['00bac098', '00bac09b']]`
  - `CONDITIONAL_JUMP` [`00bac098`](#insn-00bac098) → [`00bac0a0`](#insn-00bac0a0)
  - `FALL_THROUGH` [`00bac098`](#insn-00bac098) → [`00bac09c`](#insn-00bac09c)
- ブロック [`00bac09c`](#insn-00bac09c) 範囲 `[['00bac09c', '00bac09f']]`
  - `FALL_THROUGH` [`00bac09c`](#insn-00bac09c) → [`00bac0a0`](#insn-00bac0a0)
- ブロック [`00bac0a0`](#insn-00bac0a0) 範囲 `[['00bac0a0', '00bac0a7']]`
  - `UNCONDITIONAL_JUMP` [`00bac0a4`](#insn-00bac0a4) → [`00bac1bc`](#insn-00bac1bc)
- ブロック [`00bac0a8`](#insn-00bac0a8) 範囲 `[['00bac0a8', '00bac0ab']]`
  - `CONDITIONAL_JUMP` [`00bac0a8`](#insn-00bac0a8) → [`00bac0b0`](#insn-00bac0b0)
  - `FALL_THROUGH` [`00bac0a8`](#insn-00bac0a8) → [`00bac0ac`](#insn-00bac0ac)
- ブロック [`00bac0ac`](#insn-00bac0ac) 範囲 `[['00bac0ac', '00bac0af']]`
  - `CONDITIONAL_JUMP` [`00bac0ac`](#insn-00bac0ac) → [`00bac24c`](#insn-00bac24c)
  - `FALL_THROUGH` [`00bac0ac`](#insn-00bac0ac) → [`00bac0b0`](#insn-00bac0b0)
- ブロック [`00bac0b0`](#insn-00bac0b0) 範囲 `[['00bac0b0', '00bac0bb']]`
  - `FALL_THROUGH` [`00bac0b8`](#insn-00bac0b8) → [`00bac0bc`](#insn-00bac0bc)
- ブロック [`00bac0bc`](#insn-00bac0bc) 範囲 `[['00bac0bc', '00bac0cb']]`
  - `CONDITIONAL_JUMP` [`00bac0c8`](#insn-00bac0c8) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac0c8`](#insn-00bac0c8) → [`00bac0cc`](#insn-00bac0cc)
- ブロック [`00bac0cc`](#insn-00bac0cc) 範囲 `[['00bac0cc', '00bac0cf']]`
  - `FALL_THROUGH` [`00bac0cc`](#insn-00bac0cc) → [`00bac0d0`](#insn-00bac0d0)
- ブロック [`00bac0d0`](#insn-00bac0d0) 範囲 `[['00bac0d0', '00bac0df']]`
  - `CONDITIONAL_JUMP` [`00bac0dc`](#insn-00bac0dc) → [`00bac3cc`](#insn-00bac3cc)
  - `FALL_THROUGH` [`00bac0dc`](#insn-00bac0dc) → [`00bac0e0`](#insn-00bac0e0)
- ブロック [`00bac0e0`](#insn-00bac0e0) 範囲 `[['00bac0e0', '00bac0e7']]`
  - `FALL_THROUGH` [`00bac0e4`](#insn-00bac0e4) → [`00bac0e8`](#insn-00bac0e8)
- ブロック [`00bac0e8`](#insn-00bac0e8) 範囲 `[['00bac0e8', '00bac0eb']]`
  - `CONDITIONAL_JUMP` [`00bac0e8`](#insn-00bac0e8) → [`00bac0d0`](#insn-00bac0d0)
  - `FALL_THROUGH` [`00bac0e8`](#insn-00bac0e8) → [`00bac0ec`](#insn-00bac0ec)
- ブロック [`00bac0ec`](#insn-00bac0ec) 範囲 `[['00bac0ec', '00bac0ef']]`
  - `UNCONDITIONAL_JUMP` [`00bac0ec`](#insn-00bac0ec) → [`00bac3fc`](#insn-00bac3fc)
- ブロック [`00bac0f0`](#insn-00bac0f0) 範囲 `[['00bac0f0', '00bac0f7']]`
  - `CONDITIONAL_JUMP` [`00bac0f4`](#insn-00bac0f4) → [`00bac0fc`](#insn-00bac0fc)
  - `FALL_THROUGH` [`00bac0f4`](#insn-00bac0f4) → [`00bac0f8`](#insn-00bac0f8)
- ブロック [`00bac0f8`](#insn-00bac0f8) 範囲 `[['00bac0f8', '00bac0fb']]`
  - `CONDITIONAL_JUMP` [`00bac0f8`](#insn-00bac0f8) → [`00bac120`](#insn-00bac120)
  - `FALL_THROUGH` [`00bac0f8`](#insn-00bac0f8) → [`00bac0fc`](#insn-00bac0fc)
- ブロック [`00bac0fc`](#insn-00bac0fc) 範囲 `[['00bac0fc', '00bac10b']]`
  - `FALL_THROUGH` [`00bac108`](#insn-00bac108) → [`00bac10c`](#insn-00bac10c)
- ブロック [`00bac10c`](#insn-00bac10c) 範囲 `[['00bac10c', '00bac11f']]`
  - `FALL_THROUGH` [`00bac11c`](#insn-00bac11c) → [`00bac120`](#insn-00bac120)
- ブロック [`00bac120`](#insn-00bac120) 範囲 `[['00bac120', '00bac137']]`
  - `FALL_THROUGH` [`00bac134`](#insn-00bac134) → [`00bac138`](#insn-00bac138)
- ブロック [`00bac138`](#insn-00bac138) 範囲 `[['00bac138', '00bac147']]`
  - `UNCONDITIONAL_JUMP` [`00bac144`](#insn-00bac144) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac148`](#insn-00bac148) 範囲 `[['00bac148', '00bac14b']]`
  - `CONDITIONAL_JUMP` [`00bac148`](#insn-00bac148) → [`00bac154`](#insn-00bac154)
  - `FALL_THROUGH` [`00bac148`](#insn-00bac148) → [`00bac14c`](#insn-00bac14c)
- ブロック [`00bac14c`](#insn-00bac14c) 範囲 `[['00bac14c', '00bac153']]`
  - `CONDITIONAL_JUMP` [`00bac150`](#insn-00bac150) → [`00bac1a4`](#insn-00bac1a4)
  - `FALL_THROUGH` [`00bac150`](#insn-00bac150) → [`00bac154`](#insn-00bac154)
- ブロック [`00bac154`](#insn-00bac154) 範囲 `[['00bac154', '00bac15b']]`
  - `FALL_THROUGH` [`00bac158`](#insn-00bac158) → [`00bac15c`](#insn-00bac15c)
- ブロック [`00bac15c`](#insn-00bac15c) 範囲 `[['00bac15c', '00bac187']]`
  - `CONDITIONAL_JUMP` [`00bac184`](#insn-00bac184) → [`00bac1a4`](#insn-00bac1a4)
  - `FALL_THROUGH` [`00bac184`](#insn-00bac184) → [`00bac188`](#insn-00bac188)
- ブロック [`00bac188`](#insn-00bac188) 範囲 `[['00bac188', '00bac18f']]`
  - `CONDITIONAL_JUMP` [`00bac18c`](#insn-00bac18c) → [`00bac1a4`](#insn-00bac1a4)
  - `FALL_THROUGH` [`00bac18c`](#insn-00bac18c) → [`00bac190`](#insn-00bac190)
- ブロック [`00bac190`](#insn-00bac190) 範囲 `[['00bac190', '00bac19b']]`
  - `CONDITIONAL_JUMP` [`00bac198`](#insn-00bac198) → [`00bac1a4`](#insn-00bac1a4)
  - `FALL_THROUGH` [`00bac198`](#insn-00bac198) → [`00bac19c`](#insn-00bac19c)
- ブロック [`00bac19c`](#insn-00bac19c) 範囲 `[['00bac19c', '00bac1a3']]`
  - `FALL_THROUGH` [`00bac1a0`](#insn-00bac1a0) → [`00bac1a4`](#insn-00bac1a4)
- ブロック [`00bac1a4`](#insn-00bac1a4) 範囲 `[['00bac1a4', '00bac1a7']]`
  - `FALL_THROUGH` [`00bac1a4`](#insn-00bac1a4) → [`00bac1a8`](#insn-00bac1a8)
- ブロック [`00bac1a8`](#insn-00bac1a8) 範囲 `[['00bac1a8', '00bac1ab']]`
  - `CONDITIONAL_JUMP` [`00bac1a8`](#insn-00bac1a8) → [`00bac1b0`](#insn-00bac1b0)
  - `FALL_THROUGH` [`00bac1a8`](#insn-00bac1a8) → [`00bac1ac`](#insn-00bac1ac)
- ブロック [`00bac1ac`](#insn-00bac1ac) 範囲 `[['00bac1ac', '00bac1af']]`
  - `FALL_THROUGH` [`00bac1ac`](#insn-00bac1ac) → [`00bac1b0`](#insn-00bac1b0)
- ブロック [`00bac1b0`](#insn-00bac1b0) 範囲 `[['00bac1b0', '00bac1b3']]`
  - `CONDITIONAL_JUMP` [`00bac1b0`](#insn-00bac1b0) → [`00bac1b8`](#insn-00bac1b8)
  - `FALL_THROUGH` [`00bac1b0`](#insn-00bac1b0) → [`00bac1b4`](#insn-00bac1b4)
- ブロック [`00bac1b4`](#insn-00bac1b4) 範囲 `[['00bac1b4', '00bac1b7']]`
  - `FALL_THROUGH` [`00bac1b4`](#insn-00bac1b4) → [`00bac1b8`](#insn-00bac1b8)
- ブロック [`00bac1b8`](#insn-00bac1b8) 範囲 `[['00bac1b8', '00bac1bb']]`
  - `FALL_THROUGH` [`00bac1b8`](#insn-00bac1b8) → [`00bac1bc`](#insn-00bac1bc)
- ブロック [`00bac1bc`](#insn-00bac1bc) 範囲 `[['00bac1bc', '00bac1c3']]`
  - `UNCONDITIONAL_JUMP` [`00bac1c0`](#insn-00bac1c0) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac1c4`](#insn-00bac1c4) 範囲 `[['00bac1c4', '00bac1c7']]`
  - `CONDITIONAL_JUMP` [`00bac1c4`](#insn-00bac1c4) → [`00bac1cc`](#insn-00bac1cc)
  - `FALL_THROUGH` [`00bac1c4`](#insn-00bac1c4) → [`00bac1c8`](#insn-00bac1c8)
- ブロック [`00bac1c8`](#insn-00bac1c8) 範囲 `[['00bac1c8', '00bac1cb']]`
  - `CONDITIONAL_JUMP` [`00bac1c8`](#insn-00bac1c8) → [`00bac24c`](#insn-00bac24c)
  - `FALL_THROUGH` [`00bac1c8`](#insn-00bac1c8) → [`00bac1cc`](#insn-00bac1cc)
- ブロック [`00bac1cc`](#insn-00bac1cc) 範囲 `[['00bac1cc', '00bac1d3']]`
  - `FALL_THROUGH` [`00bac1d0`](#insn-00bac1d0) → [`00bac1d4`](#insn-00bac1d4)
- ブロック [`00bac1d4`](#insn-00bac1d4) 範囲 `[['00bac1d4', '00bac1e7']]`
  - `CONDITIONAL_JUMP` [`00bac1e4`](#insn-00bac1e4) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac1e4`](#insn-00bac1e4) → [`00bac1e8`](#insn-00bac1e8)
- ブロック [`00bac1e8`](#insn-00bac1e8) 範囲 `[['00bac1e8', '00bac1eb']]`
  - `FALL_THROUGH` [`00bac1e8`](#insn-00bac1e8) → [`00bac1ec`](#insn-00bac1ec)
- ブロック [`00bac1ec`](#insn-00bac1ec) 範囲 `[['00bac1ec', '00bac1fb']]`
  - `CONDITIONAL_JUMP` [`00bac1f8`](#insn-00bac1f8) → [`00bac3cc`](#insn-00bac3cc)
  - `FALL_THROUGH` [`00bac1f8`](#insn-00bac1f8) → [`00bac1fc`](#insn-00bac1fc)
- ブロック [`00bac1fc`](#insn-00bac1fc) 範囲 `[['00bac1fc', '00bac207']]`
  - `CONDITIONAL_JUMP` [`00bac204`](#insn-00bac204) → [`00bac1ec`](#insn-00bac1ec)
  - `FALL_THROUGH` [`00bac204`](#insn-00bac204) → [`00bac208`](#insn-00bac208)
- ブロック [`00bac208`](#insn-00bac208) 範囲 `[['00bac208', '00bac20b']]`
  - `UNCONDITIONAL_JUMP` [`00bac208`](#insn-00bac208) → [`00bac3fc`](#insn-00bac3fc)
- ブロック [`00bac20c`](#insn-00bac20c) 範囲 `[['00bac20c', '00bac20f']]`
  - `CONDITIONAL_JUMP` [`00bac20c`](#insn-00bac20c) → [`00bac30c`](#insn-00bac30c)
  - `FALL_THROUGH` [`00bac20c`](#insn-00bac20c) → [`00bac210`](#insn-00bac210)
- ブロック [`00bac210`](#insn-00bac210) 範囲 `[['00bac210', '00bac213']]`
  - `CONDITIONAL_JUMP` [`00bac210`](#insn-00bac210) → [`00bac30c`](#insn-00bac30c)
  - `FALL_THROUGH` [`00bac210`](#insn-00bac210) → [`00bac214`](#insn-00bac214)
- ブロック [`00bac214`](#insn-00bac214) 範囲 `[['00bac214', '00bac21f']]`
  - `CONDITIONAL_JUMP` [`00bac21c`](#insn-00bac21c) → [`00bac820`](#insn-00bac820)
  - `FALL_THROUGH` [`00bac21c`](#insn-00bac21c) → [`00bac220`](#insn-00bac220)
- ブロック [`00bac220`](#insn-00bac220) 範囲 `[['00bac220', '00bac223']]`
  - `UNCONDITIONAL_JUMP` [`00bac220`](#insn-00bac220) → [`00bac824`](#insn-00bac824)
- ブロック [`00bac224`](#insn-00bac224) 範囲 `[['00bac224', '00bac227']]`
  - `CONDITIONAL_JUMP` [`00bac224`](#insn-00bac224) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac224`](#insn-00bac224) → [`00bac228`](#insn-00bac228)
- ブロック [`00bac228`](#insn-00bac228) 範囲 `[['00bac228', '00bac22b']]`
  - `CONDITIONAL_JUMP` [`00bac228`](#insn-00bac228) → [`00bac34c`](#insn-00bac34c)
  - `FALL_THROUGH` [`00bac228`](#insn-00bac228) → [`00bac22c`](#insn-00bac22c)
- ブロック [`00bac22c`](#insn-00bac22c) 範囲 `[['00bac22c', '00bac237']]`
  - `CONDITIONAL_JUMP` [`00bac234`](#insn-00bac234) → [`00bac650`](#insn-00bac650)
  - `FALL_THROUGH` [`00bac234`](#insn-00bac234) → [`00bac238`](#insn-00bac238)
- ブロック [`00bac238`](#insn-00bac238) 範囲 `[['00bac238', '00bac23b']]`
  - `UNCONDITIONAL_JUMP` [`00bac238`](#insn-00bac238) → [`00bac654`](#insn-00bac654)
- ブロック [`00bac23c`](#insn-00bac23c) 範囲 `[['00bac23c', '00bac243']]`
  - `UNCONDITIONAL_JUMP` [`00bac240`](#insn-00bac240) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac244`](#insn-00bac244) 範囲 `[['00bac244', '00bac247']]`
  - `CONDITIONAL_JUMP` [`00bac244`](#insn-00bac244) → [`00bac38c`](#insn-00bac38c)
  - `FALL_THROUGH` [`00bac244`](#insn-00bac244) → [`00bac248`](#insn-00bac248)
- ブロック [`00bac248`](#insn-00bac248) 範囲 `[['00bac248', '00bac24b']]`
  - `CONDITIONAL_JUMP` [`00bac248`](#insn-00bac248) → [`00bac38c`](#insn-00bac38c)
  - `FALL_THROUGH` [`00bac248`](#insn-00bac248) → [`00bac24c`](#insn-00bac24c)
- ブロック [`00bac24c`](#insn-00bac24c) 範囲 `[['00bac24c', '00bac257']]`
  - `CONDITIONAL_JUMP` [`00bac254`](#insn-00bac254) → [`00bac448`](#insn-00bac448)
  - `FALL_THROUGH` [`00bac254`](#insn-00bac254) → [`00bac258`](#insn-00bac258)
- ブロック [`00bac258`](#insn-00bac258) 範囲 `[['00bac258', '00bac25b']]`
  - `UNCONDITIONAL_JUMP` [`00bac258`](#insn-00bac258) → [`00bac44c`](#insn-00bac44c)
- ブロック [`00bac25c`](#insn-00bac25c) 範囲 `[['00bac25c', '00bac25f']]`
  - `CONDITIONAL_JUMP` [`00bac25c`](#insn-00bac25c) → [`00bac484`](#insn-00bac484)
  - `FALL_THROUGH` [`00bac25c`](#insn-00bac25c) → [`00bac260`](#insn-00bac260)
- ブロック [`00bac260`](#insn-00bac260) 範囲 `[['00bac260', '00bac263']]`
  - `CONDITIONAL_JUMP` [`00bac260`](#insn-00bac260) → [`00bac484`](#insn-00bac484)
  - `FALL_THROUGH` [`00bac260`](#insn-00bac260) → [`00bac264`](#insn-00bac264)
- ブロック [`00bac264`](#insn-00bac264) 範囲 `[['00bac264', '00bac26f']]`
  - `CONDITIONAL_JUMP` [`00bac26c`](#insn-00bac26c) → [`00bac850`](#insn-00bac850)
  - `FALL_THROUGH` [`00bac26c`](#insn-00bac26c) → [`00bac270`](#insn-00bac270)
- ブロック [`00bac270`](#insn-00bac270) 範囲 `[['00bac270', '00bac273']]`
  - `UNCONDITIONAL_JUMP` [`00bac270`](#insn-00bac270) → [`00bac854`](#insn-00bac854)
- ブロック [`00bac274`](#insn-00bac274) 範囲 `[['00bac274', '00bac277']]`
  - `CONDITIONAL_JUMP` [`00bac274`](#insn-00bac274) → [`00bac4c4`](#insn-00bac4c4)
  - `FALL_THROUGH` [`00bac274`](#insn-00bac274) → [`00bac278`](#insn-00bac278)
- ブロック [`00bac278`](#insn-00bac278) 範囲 `[['00bac278', '00bac27b']]`
  - `CONDITIONAL_JUMP` [`00bac278`](#insn-00bac278) → [`00bac4c4`](#insn-00bac4c4)
  - `FALL_THROUGH` [`00bac278`](#insn-00bac278) → [`00bac27c`](#insn-00bac27c)
- ブロック [`00bac27c`](#insn-00bac27c) 範囲 `[['00bac27c', '00bac287']]`
  - `CONDITIONAL_JUMP` [`00bac284`](#insn-00bac284) → [`00bac764`](#insn-00bac764)
  - `FALL_THROUGH` [`00bac284`](#insn-00bac284) → [`00bac288`](#insn-00bac288)
- ブロック [`00bac288`](#insn-00bac288) 範囲 `[['00bac288', '00bac28b']]`
  - `UNCONDITIONAL_JUMP` [`00bac288`](#insn-00bac288) → [`00bac768`](#insn-00bac768)
- ブロック [`00bac28c`](#insn-00bac28c) 範囲 `[['00bac28c', '00bac28f']]`
  - `CONDITIONAL_JUMP` [`00bac28c`](#insn-00bac28c) → [`00bac504`](#insn-00bac504)
  - `FALL_THROUGH` [`00bac28c`](#insn-00bac28c) → [`00bac290`](#insn-00bac290)
- ブロック [`00bac290`](#insn-00bac290) 範囲 `[['00bac290', '00bac293']]`
  - `CONDITIONAL_JUMP` [`00bac290`](#insn-00bac290) → [`00bac504`](#insn-00bac504)
  - `FALL_THROUGH` [`00bac290`](#insn-00bac290) → [`00bac294`](#insn-00bac294)
- ブロック [`00bac294`](#insn-00bac294) 範囲 `[['00bac294', '00bac29f']]`
  - `CONDITIONAL_JUMP` [`00bac29c`](#insn-00bac29c) → [`00bac7f8`](#insn-00bac7f8)
  - `FALL_THROUGH` [`00bac29c`](#insn-00bac29c) → [`00bac2a0`](#insn-00bac2a0)
- ブロック [`00bac2a0`](#insn-00bac2a0) 範囲 `[['00bac2a0', '00bac2a3']]`
  - `UNCONDITIONAL_JUMP` [`00bac2a0`](#insn-00bac2a0) → [`00bac7fc`](#insn-00bac7fc)
- ブロック [`00bac2a4`](#insn-00bac2a4) 範囲 `[['00bac2a4', '00bac2ab']]`
  - `CONDITIONAL_JUMP` [`00bac2a8`](#insn-00bac2a8) → [`00bac2b0`](#insn-00bac2b0)
  - `FALL_THROUGH` [`00bac2a8`](#insn-00bac2a8) → [`00bac2ac`](#insn-00bac2ac)
- ブロック [`00bac2ac`](#insn-00bac2ac) 範囲 `[['00bac2ac', '00bac2af']]`
  - `CONDITIONAL_JUMP` [`00bac2ac`](#insn-00bac2ac) → [`00bac890`](#insn-00bac890)
  - `FALL_THROUGH` [`00bac2ac`](#insn-00bac2ac) → [`00bac2b0`](#insn-00bac2b0)
- ブロック [`00bac2b0`](#insn-00bac2b0) 範囲 `[['00bac2b0', '00bac2df']]`
  - `CONDITIONAL_JUMP` [`00bac2dc`](#insn-00bac2dc) → [`00bac890`](#insn-00bac890)
  - `FALL_THROUGH` [`00bac2dc`](#insn-00bac2dc) → [`00bac2e0`](#insn-00bac2e0)
- ブロック [`00bac2e0`](#insn-00bac2e0) 範囲 `[['00bac2e0', '00bac2e3']]`
  - `CONDITIONAL_JUMP` [`00bac2e0`](#insn-00bac2e0) → [`00bac890`](#insn-00bac890)
  - `FALL_THROUGH` [`00bac2e0`](#insn-00bac2e0) → [`00bac2e4`](#insn-00bac2e4)
- ブロック [`00bac2e4`](#insn-00bac2e4) 範囲 `[['00bac2e4', '00bac2eb']]`
  - `CONDITIONAL_JUMP` [`00bac2e8`](#insn-00bac2e8) → [`00bac86c`](#insn-00bac86c)
  - `FALL_THROUGH` [`00bac2e8`](#insn-00bac2e8) → [`00bac2ec`](#insn-00bac2ec)
- ブロック [`00bac2ec`](#insn-00bac2ec) 範囲 `[['00bac2ec', '00bac2ef']]`
  - `FALL_THROUGH` [`00bac2ec`](#insn-00bac2ec) → [`00bac2f0`](#insn-00bac2f0)
- ブロック [`00bac2f0`](#insn-00bac2f0) 範囲 `[['00bac2f0', '00bac2f3']]`
  - `FALL_THROUGH` [`00bac2f0`](#insn-00bac2f0) → [`00bac2f4`](#insn-00bac2f4)
- ブロック [`00bac2f4`](#insn-00bac2f4) 範囲 `[['00bac2f4', '00bac2ff']]`
  - `CONDITIONAL_JUMP` [`00bac2fc`](#insn-00bac2fc) → [`00bac870`](#insn-00bac870)
  - `FALL_THROUGH` [`00bac2fc`](#insn-00bac2fc) → [`00bac300`](#insn-00bac300)
- ブロック [`00bac300`](#insn-00bac300) 範囲 `[['00bac300', '00bac307']]`
  - `CONDITIONAL_JUMP` [`00bac304`](#insn-00bac304) → [`00bac2f0`](#insn-00bac2f0)
  - `FALL_THROUGH` [`00bac304`](#insn-00bac304) → [`00bac308`](#insn-00bac308)
- ブロック [`00bac308`](#insn-00bac308) 範囲 `[['00bac308', '00bac30b']]`
  - `UNCONDITIONAL_JUMP` [`00bac308`](#insn-00bac308) → [`00bac870`](#insn-00bac870)
- ブロック [`00bac30c`](#insn-00bac30c) 範囲 `[['00bac30c', '00bac317']]`
  - `FALL_THROUGH` [`00bac314`](#insn-00bac314) → [`00bac318`](#insn-00bac318)
- ブロック [`00bac318`](#insn-00bac318) 範囲 `[['00bac318', '00bac327']]`
  - `CONDITIONAL_JUMP` [`00bac324`](#insn-00bac324) → [`00bac574`](#insn-00bac574)
  - `FALL_THROUGH` [`00bac324`](#insn-00bac324) → [`00bac328`](#insn-00bac328)
- ブロック [`00bac328`](#insn-00bac328) 範囲 `[['00bac328', '00bac32b']]`
  - `FALL_THROUGH` [`00bac328`](#insn-00bac328) → [`00bac32c`](#insn-00bac32c)
- ブロック [`00bac32c`](#insn-00bac32c) 範囲 `[['00bac32c', '00bac33b']]`
  - `CONDITIONAL_JUMP` [`00bac338`](#insn-00bac338) → [`00bac544`](#insn-00bac544)
  - `FALL_THROUGH` [`00bac338`](#insn-00bac338) → [`00bac33c`](#insn-00bac33c)
- ブロック [`00bac33c`](#insn-00bac33c) 範囲 `[['00bac33c', '00bac347']]`
  - `CONDITIONAL_JUMP` [`00bac344`](#insn-00bac344) → [`00bac32c`](#insn-00bac32c)
  - `FALL_THROUGH` [`00bac344`](#insn-00bac344) → [`00bac348`](#insn-00bac348)
- ブロック [`00bac348`](#insn-00bac348) 範囲 `[['00bac348', '00bac34b']]`
  - `UNCONDITIONAL_JUMP` [`00bac348`](#insn-00bac348) → [`00bac574`](#insn-00bac574)
- ブロック [`00bac34c`](#insn-00bac34c) 範囲 `[['00bac34c', '00bac367']]`
  - `CONDITIONAL_JUMP` [`00bac364`](#insn-00bac364) → [`00bac5f4`](#insn-00bac5f4)
  - `FALL_THROUGH` [`00bac364`](#insn-00bac364) → [`00bac368`](#insn-00bac368)
- ブロック [`00bac368`](#insn-00bac368) 範囲 `[['00bac368', '00bac36b']]`
  - `FALL_THROUGH` [`00bac368`](#insn-00bac368) → [`00bac36c`](#insn-00bac36c)
- ブロック [`00bac36c`](#insn-00bac36c) 範囲 `[['00bac36c', '00bac37b']]`
  - `CONDITIONAL_JUMP` [`00bac378`](#insn-00bac378) → [`00bac5c4`](#insn-00bac5c4)
  - `FALL_THROUGH` [`00bac378`](#insn-00bac378) → [`00bac37c`](#insn-00bac37c)
- ブロック [`00bac37c`](#insn-00bac37c) 範囲 `[['00bac37c', '00bac387']]`
  - `CONDITIONAL_JUMP` [`00bac384`](#insn-00bac384) → [`00bac36c`](#insn-00bac36c)
  - `FALL_THROUGH` [`00bac384`](#insn-00bac384) → [`00bac388`](#insn-00bac388)
- ブロック [`00bac388`](#insn-00bac388) 範囲 `[['00bac388', '00bac38b']]`
  - `UNCONDITIONAL_JUMP` [`00bac388`](#insn-00bac388) → [`00bac5f4`](#insn-00bac5f4)
- ブロック [`00bac38c`](#insn-00bac38c) 範囲 `[['00bac38c', '00bac397']]`
  - `FALL_THROUGH` [`00bac394`](#insn-00bac394) → [`00bac398`](#insn-00bac398)
- ブロック [`00bac398`](#insn-00bac398) 範囲 `[['00bac398', '00bac3a7']]`
  - `CONDITIONAL_JUMP` [`00bac3a4`](#insn-00bac3a4) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac3a4`](#insn-00bac3a4) → [`00bac3a8`](#insn-00bac3a8)
- ブロック [`00bac3a8`](#insn-00bac3a8) 範囲 `[['00bac3a8', '00bac3ab']]`
  - `FALL_THROUGH` [`00bac3a8`](#insn-00bac3a8) → [`00bac3ac`](#insn-00bac3ac)
- ブロック [`00bac3ac`](#insn-00bac3ac) 範囲 `[['00bac3ac', '00bac3bb']]`
  - `CONDITIONAL_JUMP` [`00bac3b8`](#insn-00bac3b8) → [`00bac3cc`](#insn-00bac3cc)
  - `FALL_THROUGH` [`00bac3b8`](#insn-00bac3b8) → [`00bac3bc`](#insn-00bac3bc)
- ブロック [`00bac3bc`](#insn-00bac3bc) 範囲 `[['00bac3bc', '00bac3c7']]`
  - `CONDITIONAL_JUMP` [`00bac3c4`](#insn-00bac3c4) → [`00bac3ac`](#insn-00bac3ac)
  - `FALL_THROUGH` [`00bac3c4`](#insn-00bac3c4) → [`00bac3c8`](#insn-00bac3c8)
- ブロック [`00bac3c8`](#insn-00bac3c8) 範囲 `[['00bac3c8', '00bac3cb']]`
  - `UNCONDITIONAL_JUMP` [`00bac3c8`](#insn-00bac3c8) → [`00bac3fc`](#insn-00bac3fc)
- ブロック [`00bac3cc`](#insn-00bac3cc) 範囲 `[['00bac3cc', '00bac3d3']]`
  - `CONDITIONAL_JUMP` [`00bac3d0`](#insn-00bac3d0) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac3d0`](#insn-00bac3d0) → [`00bac3d4`](#insn-00bac3d4)
- ブロック [`00bac3d4`](#insn-00bac3d4) 範囲 `[['00bac3d4', '00bac3e3']]`
  - `CONDITIONAL_JUMP` [`00bac3e0`](#insn-00bac3e0) → [`00bac3fc`](#insn-00bac3fc)
  - `FALL_THROUGH` [`00bac3e0`](#insn-00bac3e0) → [`00bac3e4`](#insn-00bac3e4)
- ブロック [`00bac3e4`](#insn-00bac3e4) 範囲 `[['00bac3e4', '00bac3e7']]`
  - `FALL_THROUGH` [`00bac3e4`](#insn-00bac3e4) → [`00bac3e8`](#insn-00bac3e8)
- ブロック [`00bac3e8`](#insn-00bac3e8) 範囲 `[['00bac3e8', '00bac3fb']]`
  - `UNCONDITIONAL_JUMP` [`00bac3f8`](#insn-00bac3f8) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac3fc`](#insn-00bac3fc) 範囲 `[['00bac3fc', '00bac407']]`
  - `FALL_THROUGH` [`00bac404`](#insn-00bac404) → [`00bac408`](#insn-00bac408)
- ブロック [`00bac408`](#insn-00bac408) 範囲 `[['00bac408', '00bac40f']]`
  - `FALL_THROUGH` [`00bac40c`](#insn-00bac40c) → [`00bac410`](#insn-00bac410)
- ブロック [`00bac410`](#insn-00bac410) 範囲 `[['00bac410', '00bac42b']]`
  - `CONDITIONAL_JUMP` [`00bac428`](#insn-00bac428) → [`00bac440`](#insn-00bac440)
  - `FALL_THROUGH` [`00bac428`](#insn-00bac428) → [`00bac42c`](#insn-00bac42c)
- ブロック [`00bac42c`](#insn-00bac42c) 範囲 `[['00bac42c', '00bac433']]`
  - `CONDITIONAL_JUMP` [`00bac430`](#insn-00bac430) → [`00bac440`](#insn-00bac440)
  - `FALL_THROUGH` [`00bac430`](#insn-00bac430) → [`00bac434`](#insn-00bac434)
- ブロック [`00bac434`](#insn-00bac434) 範囲 `[['00bac434', '00bac43f']]`
  - `FALL_THROUGH` [`00bac43c`](#insn-00bac43c) → [`00bac440`](#insn-00bac440)
- ブロック [`00bac440`](#insn-00bac440) 範囲 `[['00bac440', '00bac447']]`
  - `CONDITIONAL_JUMP` [`00bac444`](#insn-00bac444) → [`00bac44c`](#insn-00bac44c)
  - `FALL_THROUGH` [`00bac444`](#insn-00bac444) → [`00bac448`](#insn-00bac448)
- ブロック [`00bac448`](#insn-00bac448) 範囲 `[['00bac448', '00bac44b']]`
  - `FALL_THROUGH` [`00bac448`](#insn-00bac448) → [`00bac44c`](#insn-00bac44c)
- ブロック [`00bac44c`](#insn-00bac44c) 範囲 `[['00bac44c', '00bac44f']]`
  - `CONDITIONAL_JUMP` [`00bac44c`](#insn-00bac44c) → [`00bac454`](#insn-00bac454)
  - `FALL_THROUGH` [`00bac44c`](#insn-00bac44c) → [`00bac450`](#insn-00bac450)
- ブロック [`00bac450`](#insn-00bac450) 範囲 `[['00bac450', '00bac453']]`
  - `FALL_THROUGH` [`00bac450`](#insn-00bac450) → [`00bac454`](#insn-00bac454)
- ブロック [`00bac454`](#insn-00bac454) 範囲 `[['00bac454', '00bac457']]`
  - `FALL_THROUGH` [`00bac454`](#insn-00bac454) → [`00bac458`](#insn-00bac458)
- ブロック [`00bac458`](#insn-00bac458) 範囲 `[['00bac458', '00bac45b']]`
  - `FALL_THROUGH` [`00bac458`](#insn-00bac458) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac45c`](#insn-00bac45c) 範囲 `[['00bac45c', '00bac45f']]`
  - `FALL_THROUGH` [`00bac45c`](#insn-00bac45c) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac460`](#insn-00bac460) 範囲 `[['00bac460', '00bac46f']]`
  - `CONDITIONAL_JUMP` [`00bac46c`](#insn-00bac46c) → [`00bac8b4`](#insn-00bac8b4)
  - `FALL_THROUGH` [`00bac46c`](#insn-00bac46c) → [`00bac470`](#insn-00bac470)
- ブロック [`00bac470`](#insn-00bac470) 範囲 `[['00bac470', '00bac483']]`
- ブロック [`00bac484`](#insn-00bac484) 範囲 `[['00bac484', '00bac49f']]`
  - `CONDITIONAL_JUMP` [`00bac49c`](#insn-00bac49c) → [`00bac698`](#insn-00bac698)
  - `FALL_THROUGH` [`00bac49c`](#insn-00bac49c) → [`00bac4a0`](#insn-00bac4a0)
- ブロック [`00bac4a0`](#insn-00bac4a0) 範囲 `[['00bac4a0', '00bac4a3']]`
  - `FALL_THROUGH` [`00bac4a0`](#insn-00bac4a0) → [`00bac4a4`](#insn-00bac4a4)
- ブロック [`00bac4a4`](#insn-00bac4a4) 範囲 `[['00bac4a4', '00bac4a7']]`
  - `FALL_THROUGH` [`00bac4a4`](#insn-00bac4a4) → [`00bac4a8`](#insn-00bac4a8)
- ブロック [`00bac4a8`](#insn-00bac4a8) 範囲 `[['00bac4a8', '00bac4b3']]`
  - `CONDITIONAL_JUMP` [`00bac4b0`](#insn-00bac4b0) → [`00bac668`](#insn-00bac668)
  - `FALL_THROUGH` [`00bac4b0`](#insn-00bac4b0) → [`00bac4b4`](#insn-00bac4b4)
- ブロック [`00bac4b4`](#insn-00bac4b4) 範囲 `[['00bac4b4', '00bac4bf']]`
  - `CONDITIONAL_JUMP` [`00bac4bc`](#insn-00bac4bc) → [`00bac4a4`](#insn-00bac4a4)
  - `FALL_THROUGH` [`00bac4bc`](#insn-00bac4bc) → [`00bac4c0`](#insn-00bac4c0)
- ブロック [`00bac4c0`](#insn-00bac4c0) 範囲 `[['00bac4c0', '00bac4c3']]`
  - `UNCONDITIONAL_JUMP` [`00bac4c0`](#insn-00bac4c0) → [`00bac698`](#insn-00bac698)
- ブロック [`00bac4c4`](#insn-00bac4c4) 範囲 `[['00bac4c4', '00bac4d3']]`
  - `FALL_THROUGH` [`00bac4d0`](#insn-00bac4d0) → [`00bac4d4`](#insn-00bac4d4)
- ブロック [`00bac4d4`](#insn-00bac4d4) 範囲 `[['00bac4d4', '00bac4df']]`
  - `CONDITIONAL_JUMP` [`00bac4dc`](#insn-00bac4dc) → [`00bac718`](#insn-00bac718)
  - `FALL_THROUGH` [`00bac4dc`](#insn-00bac4dc) → [`00bac4e0`](#insn-00bac4e0)
- ブロック [`00bac4e0`](#insn-00bac4e0) 範囲 `[['00bac4e0', '00bac4e3']]`
  - `FALL_THROUGH` [`00bac4e0`](#insn-00bac4e0) → [`00bac4e4`](#insn-00bac4e4)
- ブロック [`00bac4e4`](#insn-00bac4e4) 範囲 `[['00bac4e4', '00bac4f3']]`
  - `CONDITIONAL_JUMP` [`00bac4f0`](#insn-00bac4f0) → [`00bac6e8`](#insn-00bac6e8)
  - `FALL_THROUGH` [`00bac4f0`](#insn-00bac4f0) → [`00bac4f4`](#insn-00bac4f4)
- ブロック [`00bac4f4`](#insn-00bac4f4) 範囲 `[['00bac4f4', '00bac4f7']]`
  - `FALL_THROUGH` [`00bac4f4`](#insn-00bac4f4) → [`00bac4f8`](#insn-00bac4f8)
- ブロック [`00bac4f8`](#insn-00bac4f8) 範囲 `[['00bac4f8', '00bac4ff']]`
  - `CONDITIONAL_JUMP` [`00bac4fc`](#insn-00bac4fc) → [`00bac4e4`](#insn-00bac4e4)
  - `FALL_THROUGH` [`00bac4fc`](#insn-00bac4fc) → [`00bac500`](#insn-00bac500)
- ブロック [`00bac500`](#insn-00bac500) 範囲 `[['00bac500', '00bac503']]`
  - `UNCONDITIONAL_JUMP` [`00bac500`](#insn-00bac500) → [`00bac718`](#insn-00bac718)
- ブロック [`00bac504`](#insn-00bac504) 範囲 `[['00bac504', '00bac51f']]`
  - `CONDITIONAL_JUMP` [`00bac51c`](#insn-00bac51c) → [`00bac7ac`](#insn-00bac7ac)
  - `FALL_THROUGH` [`00bac51c`](#insn-00bac51c) → [`00bac520`](#insn-00bac520)
- ブロック [`00bac520`](#insn-00bac520) 範囲 `[['00bac520', '00bac523']]`
  - `FALL_THROUGH` [`00bac520`](#insn-00bac520) → [`00bac524`](#insn-00bac524)
- ブロック [`00bac524`](#insn-00bac524) 範囲 `[['00bac524', '00bac533']]`
  - `CONDITIONAL_JUMP` [`00bac530`](#insn-00bac530) → [`00bac77c`](#insn-00bac77c)
  - `FALL_THROUGH` [`00bac530`](#insn-00bac530) → [`00bac534`](#insn-00bac534)
- ブロック [`00bac534`](#insn-00bac534) 範囲 `[['00bac534', '00bac53f']]`
  - `CONDITIONAL_JUMP` [`00bac53c`](#insn-00bac53c) → [`00bac524`](#insn-00bac524)
  - `FALL_THROUGH` [`00bac53c`](#insn-00bac53c) → [`00bac540`](#insn-00bac540)
- ブロック [`00bac540`](#insn-00bac540) 範囲 `[['00bac540', '00bac543']]`
  - `UNCONDITIONAL_JUMP` [`00bac540`](#insn-00bac540) → [`00bac7ac`](#insn-00bac7ac)
- ブロック [`00bac544`](#insn-00bac544) 範囲 `[['00bac544', '00bac54b']]`
  - `CONDITIONAL_JUMP` [`00bac548`](#insn-00bac548) → [`00bac574`](#insn-00bac574)
  - `FALL_THROUGH` [`00bac548`](#insn-00bac548) → [`00bac54c`](#insn-00bac54c)
- ブロック [`00bac54c`](#insn-00bac54c) 範囲 `[['00bac54c', '00bac55b']]`
  - `CONDITIONAL_JUMP` [`00bac558`](#insn-00bac558) → [`00bac574`](#insn-00bac574)
  - `FALL_THROUGH` [`00bac558`](#insn-00bac558) → [`00bac55c`](#insn-00bac55c)
- ブロック [`00bac55c`](#insn-00bac55c) 範囲 `[['00bac55c', '00bac56b']]`
  - `FALL_THROUGH` [`00bac568`](#insn-00bac568) → [`00bac56c`](#insn-00bac56c)
- ブロック [`00bac56c`](#insn-00bac56c) 範囲 `[['00bac56c', '00bac573']]`
  - `UNCONDITIONAL_JUMP` [`00bac570`](#insn-00bac570) → [`00bac588`](#insn-00bac588)
- ブロック [`00bac574`](#insn-00bac574) 範囲 `[['00bac574', '00bac587']]`
  - `FALL_THROUGH` [`00bac584`](#insn-00bac584) → [`00bac588`](#insn-00bac588)
- ブロック [`00bac588`](#insn-00bac588) 範囲 `[['00bac588', '00bac5a3']]`
  - `CONDITIONAL_JUMP` [`00bac5a0`](#insn-00bac5a0) → [`00bac818`](#insn-00bac818)
  - `FALL_THROUGH` [`00bac5a0`](#insn-00bac5a0) → [`00bac5a4`](#insn-00bac5a4)
- ブロック [`00bac5a4`](#insn-00bac5a4) 範囲 `[['00bac5a4', '00bac5ab']]`
  - `CONDITIONAL_JUMP` [`00bac5a8`](#insn-00bac5a8) → [`00bac818`](#insn-00bac818)
  - `FALL_THROUGH` [`00bac5a8`](#insn-00bac5a8) → [`00bac5ac`](#insn-00bac5ac)
- ブロック [`00bac5ac`](#insn-00bac5ac) 範囲 `[['00bac5ac', '00bac5b3']]`
  - `CONDITIONAL_JUMP` [`00bac5b0`](#insn-00bac5b0) → [`00bac80c`](#insn-00bac80c)
  - `FALL_THROUGH` [`00bac5b0`](#insn-00bac5b0) → [`00bac5b4`](#insn-00bac5b4)
- ブロック [`00bac5b4`](#insn-00bac5b4) 範囲 `[['00bac5b4', '00bac5bf']]`
  - `CONDITIONAL_JUMP` [`00bac5bc`](#insn-00bac5bc) → [`00bac820`](#insn-00bac820)
  - `FALL_THROUGH` [`00bac5bc`](#insn-00bac5bc) → [`00bac5c0`](#insn-00bac5c0)
- ブロック [`00bac5c0`](#insn-00bac5c0) 範囲 `[['00bac5c0', '00bac5c3']]`
  - `UNCONDITIONAL_JUMP` [`00bac5c0`](#insn-00bac5c0) → [`00bac824`](#insn-00bac824)
- ブロック [`00bac5c4`](#insn-00bac5c4) 範囲 `[['00bac5c4', '00bac5cb']]`
  - `CONDITIONAL_JUMP` [`00bac5c8`](#insn-00bac5c8) → [`00bac5f4`](#insn-00bac5f4)
  - `FALL_THROUGH` [`00bac5c8`](#insn-00bac5c8) → [`00bac5cc`](#insn-00bac5cc)
- ブロック [`00bac5cc`](#insn-00bac5cc) 範囲 `[['00bac5cc', '00bac5db']]`
  - `CONDITIONAL_JUMP` [`00bac5d8`](#insn-00bac5d8) → [`00bac5f4`](#insn-00bac5f4)
  - `FALL_THROUGH` [`00bac5d8`](#insn-00bac5d8) → [`00bac5dc`](#insn-00bac5dc)
- ブロック [`00bac5dc`](#insn-00bac5dc) 範囲 `[['00bac5dc', '00bac5df']]`
  - `FALL_THROUGH` [`00bac5dc`](#insn-00bac5dc) → [`00bac5e0`](#insn-00bac5e0)
- ブロック [`00bac5e0`](#insn-00bac5e0) 範囲 `[['00bac5e0', '00bac5ef']]`
  - `FALL_THROUGH` [`00bac5ec`](#insn-00bac5ec) → [`00bac5f0`](#insn-00bac5f0)
- ブロック [`00bac5f0`](#insn-00bac5f0) 範囲 `[['00bac5f0', '00bac5f3']]`
  - `UNCONDITIONAL_JUMP` [`00bac5f0`](#insn-00bac5f0) → [`00bac608`](#insn-00bac608)
- ブロック [`00bac5f4`](#insn-00bac5f4) 範囲 `[['00bac5f4', '00bac607']]`
  - `FALL_THROUGH` [`00bac604`](#insn-00bac604) → [`00bac608`](#insn-00bac608)
- ブロック [`00bac608`](#insn-00bac608) 範囲 `[['00bac608', '00bac623']]`
  - `CONDITIONAL_JUMP` [`00bac620`](#insn-00bac620) → [`00bac648`](#insn-00bac648)
  - `FALL_THROUGH` [`00bac620`](#insn-00bac620) → [`00bac624`](#insn-00bac624)
- ブロック [`00bac624`](#insn-00bac624) 範囲 `[['00bac624', '00bac62b']]`
  - `CONDITIONAL_JUMP` [`00bac628`](#insn-00bac628) → [`00bac648`](#insn-00bac648)
  - `FALL_THROUGH` [`00bac628`](#insn-00bac628) → [`00bac62c`](#insn-00bac62c)
- ブロック [`00bac62c`](#insn-00bac62c) 範囲 `[['00bac62c', '00bac637']]`
  - `CONDITIONAL_JUMP` [`00bac634`](#insn-00bac634) → [`00bac648`](#insn-00bac648)
  - `FALL_THROUGH` [`00bac634`](#insn-00bac634) → [`00bac638`](#insn-00bac638)
- ブロック [`00bac638`](#insn-00bac638) 範囲 `[['00bac638', '00bac643']]`
  - `FALL_THROUGH` [`00bac640`](#insn-00bac640) → [`00bac644`](#insn-00bac644)
- ブロック [`00bac644`](#insn-00bac644) 範囲 `[['00bac644', '00bac647']]`
  - `FALL_THROUGH` [`00bac644`](#insn-00bac644) → [`00bac648`](#insn-00bac648)
- ブロック [`00bac648`](#insn-00bac648) 範囲 `[['00bac648', '00bac64f']]`
  - `CONDITIONAL_JUMP` [`00bac64c`](#insn-00bac64c) → [`00bac654`](#insn-00bac654)
  - `FALL_THROUGH` [`00bac64c`](#insn-00bac64c) → [`00bac650`](#insn-00bac650)
- ブロック [`00bac650`](#insn-00bac650) 範囲 `[['00bac650', '00bac653']]`
  - `FALL_THROUGH` [`00bac650`](#insn-00bac650) → [`00bac654`](#insn-00bac654)
- ブロック [`00bac654`](#insn-00bac654) 範囲 `[['00bac654', '00bac657']]`
  - `CONDITIONAL_JUMP` [`00bac654`](#insn-00bac654) → [`00bac65c`](#insn-00bac65c)
  - `FALL_THROUGH` [`00bac654`](#insn-00bac654) → [`00bac658`](#insn-00bac658)
- ブロック [`00bac658`](#insn-00bac658) 範囲 `[['00bac658', '00bac65b']]`
  - `FALL_THROUGH` [`00bac658`](#insn-00bac658) → [`00bac65c`](#insn-00bac65c)
- ブロック [`00bac65c`](#insn-00bac65c) 範囲 `[['00bac65c', '00bac667']]`
  - `UNCONDITIONAL_JUMP` [`00bac664`](#insn-00bac664) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac668`](#insn-00bac668) 範囲 `[['00bac668', '00bac66f']]`
  - `CONDITIONAL_JUMP` [`00bac66c`](#insn-00bac66c) → [`00bac698`](#insn-00bac698)
  - `FALL_THROUGH` [`00bac66c`](#insn-00bac66c) → [`00bac670`](#insn-00bac670)
- ブロック [`00bac670`](#insn-00bac670) 範囲 `[['00bac670', '00bac67f']]`
  - `CONDITIONAL_JUMP` [`00bac67c`](#insn-00bac67c) → [`00bac698`](#insn-00bac698)
  - `FALL_THROUGH` [`00bac67c`](#insn-00bac67c) → [`00bac680`](#insn-00bac680)
- ブロック [`00bac680`](#insn-00bac680) 範囲 `[['00bac680', '00bac68b']]`
  - `FALL_THROUGH` [`00bac688`](#insn-00bac688) → [`00bac68c`](#insn-00bac68c)
- ブロック [`00bac68c`](#insn-00bac68c) 範囲 `[['00bac68c', '00bac697']]`
  - `UNCONDITIONAL_JUMP` [`00bac694`](#insn-00bac694) → [`00bac6ac`](#insn-00bac6ac)
- ブロック [`00bac698`](#insn-00bac698) 範囲 `[['00bac698', '00bac6ab']]`
  - `FALL_THROUGH` [`00bac6a8`](#insn-00bac6a8) → [`00bac6ac`](#insn-00bac6ac)
- ブロック [`00bac6ac`](#insn-00bac6ac) 範囲 `[['00bac6ac', '00bac6af']]`
  - `FALL_THROUGH` [`00bac6ac`](#insn-00bac6ac) → [`00bac6b0`](#insn-00bac6b0)
- ブロック [`00bac6b0`](#insn-00bac6b0) 範囲 `[['00bac6b0', '00bac6c3']]`
  - `FALL_THROUGH` [`00bac6c0`](#insn-00bac6c0) → [`00bac6c4`](#insn-00bac6c4)
- ブロック [`00bac6c4`](#insn-00bac6c4) 範囲 `[['00bac6c4', '00bac6c7']]`
  - `CONDITIONAL_JUMP` [`00bac6c4`](#insn-00bac6c4) → [`00bac848`](#insn-00bac848)
  - `FALL_THROUGH` [`00bac6c4`](#insn-00bac6c4) → [`00bac6c8`](#insn-00bac6c8)
- ブロック [`00bac6c8`](#insn-00bac6c8) 範囲 `[['00bac6c8', '00bac6cf']]`
  - `CONDITIONAL_JUMP` [`00bac6cc`](#insn-00bac6cc) → [`00bac848`](#insn-00bac848)
  - `FALL_THROUGH` [`00bac6cc`](#insn-00bac6cc) → [`00bac6d0`](#insn-00bac6d0)
- ブロック [`00bac6d0`](#insn-00bac6d0) 範囲 `[['00bac6d0', '00bac6d7']]`
  - `CONDITIONAL_JUMP` [`00bac6d4`](#insn-00bac6d4) → [`00bac83c`](#insn-00bac83c)
  - `FALL_THROUGH` [`00bac6d4`](#insn-00bac6d4) → [`00bac6d8`](#insn-00bac6d8)
- ブロック [`00bac6d8`](#insn-00bac6d8) 範囲 `[['00bac6d8', '00bac6e3']]`
  - `CONDITIONAL_JUMP` [`00bac6e0`](#insn-00bac6e0) → [`00bac850`](#insn-00bac850)
  - `FALL_THROUGH` [`00bac6e0`](#insn-00bac6e0) → [`00bac6e4`](#insn-00bac6e4)
- ブロック [`00bac6e4`](#insn-00bac6e4) 範囲 `[['00bac6e4', '00bac6e7']]`
  - `UNCONDITIONAL_JUMP` [`00bac6e4`](#insn-00bac6e4) → [`00bac854`](#insn-00bac854)
- ブロック [`00bac6e8`](#insn-00bac6e8) 範囲 `[['00bac6e8', '00bac6ef']]`
  - `CONDITIONAL_JUMP` [`00bac6ec`](#insn-00bac6ec) → [`00bac718`](#insn-00bac718)
  - `FALL_THROUGH` [`00bac6ec`](#insn-00bac6ec) → [`00bac6f0`](#insn-00bac6f0)
- ブロック [`00bac6f0`](#insn-00bac6f0) 範囲 `[['00bac6f0', '00bac6ff']]`
  - `CONDITIONAL_JUMP` [`00bac6fc`](#insn-00bac6fc) → [`00bac718`](#insn-00bac718)
  - `FALL_THROUGH` [`00bac6fc`](#insn-00bac6fc) → [`00bac700`](#insn-00bac700)
- ブロック [`00bac700`](#insn-00bac700) 範囲 `[['00bac700', '00bac703']]`
  - `FALL_THROUGH` [`00bac700`](#insn-00bac700) → [`00bac704`](#insn-00bac704)
- ブロック [`00bac704`](#insn-00bac704) 範囲 `[['00bac704', '00bac717']]`
  - `UNCONDITIONAL_JUMP` [`00bac714`](#insn-00bac714) → [`00bac72c`](#insn-00bac72c)
- ブロック [`00bac718`](#insn-00bac718) 範囲 `[['00bac718', '00bac72b']]`
  - `FALL_THROUGH` [`00bac728`](#insn-00bac728) → [`00bac72c`](#insn-00bac72c)
- ブロック [`00bac72c`](#insn-00bac72c) 範囲 `[['00bac72c', '00bac72f']]`
  - `FALL_THROUGH` [`00bac72c`](#insn-00bac72c) → [`00bac730`](#insn-00bac730)
- ブロック [`00bac730`](#insn-00bac730) 範囲 `[['00bac730', '00bac747']]`
  - `CONDITIONAL_JUMP` [`00bac744`](#insn-00bac744) → [`00bac75c`](#insn-00bac75c)
  - `FALL_THROUGH` [`00bac744`](#insn-00bac744) → [`00bac748`](#insn-00bac748)
- ブロック [`00bac748`](#insn-00bac748) 範囲 `[['00bac748', '00bac74f']]`
  - `CONDITIONAL_JUMP` [`00bac74c`](#insn-00bac74c) → [`00bac75c`](#insn-00bac75c)
  - `FALL_THROUGH` [`00bac74c`](#insn-00bac74c) → [`00bac750`](#insn-00bac750)
- ブロック [`00bac750`](#insn-00bac750) 範囲 `[['00bac750', '00bac753']]`
  - `FALL_THROUGH` [`00bac750`](#insn-00bac750) → [`00bac754`](#insn-00bac754)
- ブロック [`00bac754`](#insn-00bac754) 範囲 `[['00bac754', '00bac75b']]`
  - `FALL_THROUGH` [`00bac758`](#insn-00bac758) → [`00bac75c`](#insn-00bac75c)
- ブロック [`00bac75c`](#insn-00bac75c) 範囲 `[['00bac75c', '00bac763']]`
  - `CONDITIONAL_JUMP` [`00bac760`](#insn-00bac760) → [`00bac768`](#insn-00bac768)
  - `FALL_THROUGH` [`00bac760`](#insn-00bac760) → [`00bac764`](#insn-00bac764)
- ブロック [`00bac764`](#insn-00bac764) 範囲 `[['00bac764', '00bac767']]`
  - `FALL_THROUGH` [`00bac764`](#insn-00bac764) → [`00bac768`](#insn-00bac768)
- ブロック [`00bac768`](#insn-00bac768) 範囲 `[['00bac768', '00bac76b']]`
  - `CONDITIONAL_JUMP` [`00bac768`](#insn-00bac768) → [`00bac770`](#insn-00bac770)
  - `FALL_THROUGH` [`00bac768`](#insn-00bac768) → [`00bac76c`](#insn-00bac76c)
- ブロック [`00bac76c`](#insn-00bac76c) 範囲 `[['00bac76c', '00bac76f']]`
  - `FALL_THROUGH` [`00bac76c`](#insn-00bac76c) → [`00bac770`](#insn-00bac770)
- ブロック [`00bac770`](#insn-00bac770) 範囲 `[['00bac770', '00bac77b']]`
  - `UNCONDITIONAL_JUMP` [`00bac778`](#insn-00bac778) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac77c`](#insn-00bac77c) 範囲 `[['00bac77c', '00bac77f']]`
  - `FALL_THROUGH` [`00bac77c`](#insn-00bac77c) → [`00bac780`](#insn-00bac780)
- ブロック [`00bac780`](#insn-00bac780) 範囲 `[['00bac780', '00bac783']]`
  - `CONDITIONAL_JUMP` [`00bac780`](#insn-00bac780) → [`00bac7ac`](#insn-00bac7ac)
  - `FALL_THROUGH` [`00bac780`](#insn-00bac780) → [`00bac784`](#insn-00bac784)
- ブロック [`00bac784`](#insn-00bac784) 範囲 `[['00bac784', '00bac793']]`
  - `CONDITIONAL_JUMP` [`00bac790`](#insn-00bac790) → [`00bac7ac`](#insn-00bac7ac)
  - `FALL_THROUGH` [`00bac790`](#insn-00bac790) → [`00bac794`](#insn-00bac794)
- ブロック [`00bac794`](#insn-00bac794) 範囲 `[['00bac794', '00bac79f']]`
  - `FALL_THROUGH` [`00bac79c`](#insn-00bac79c) → [`00bac7a0`](#insn-00bac7a0)
- ブロック [`00bac7a0`](#insn-00bac7a0) 範囲 `[['00bac7a0', '00bac7ab']]`
  - `UNCONDITIONAL_JUMP` [`00bac7a8`](#insn-00bac7a8) → [`00bac7c0`](#insn-00bac7c0)
- ブロック [`00bac7ac`](#insn-00bac7ac) 範囲 `[['00bac7ac', '00bac7bf']]`
  - `FALL_THROUGH` [`00bac7bc`](#insn-00bac7bc) → [`00bac7c0`](#insn-00bac7c0)
- ブロック [`00bac7c0`](#insn-00bac7c0) 範囲 `[['00bac7c0', '00bac7cb']]`
  - `FALL_THROUGH` [`00bac7c8`](#insn-00bac7c8) → [`00bac7cc`](#insn-00bac7cc)
- ブロック [`00bac7cc`](#insn-00bac7cc) 範囲 `[['00bac7cc', '00bac7db']]`
  - `CONDITIONAL_JUMP` [`00bac7d8`](#insn-00bac7d8) → [`00bac7f0`](#insn-00bac7f0)
  - `FALL_THROUGH` [`00bac7d8`](#insn-00bac7d8) → [`00bac7dc`](#insn-00bac7dc)
- ブロック [`00bac7dc`](#insn-00bac7dc) 範囲 `[['00bac7dc', '00bac7e3']]`
  - `CONDITIONAL_JUMP` [`00bac7e0`](#insn-00bac7e0) → [`00bac7f0`](#insn-00bac7f0)
  - `FALL_THROUGH` [`00bac7e0`](#insn-00bac7e0) → [`00bac7e4`](#insn-00bac7e4)
- ブロック [`00bac7e4`](#insn-00bac7e4) 範囲 `[['00bac7e4', '00bac7ef']]`
  - `FALL_THROUGH` [`00bac7ec`](#insn-00bac7ec) → [`00bac7f0`](#insn-00bac7f0)
- ブロック [`00bac7f0`](#insn-00bac7f0) 範囲 `[['00bac7f0', '00bac7f7']]`
  - `CONDITIONAL_JUMP` [`00bac7f4`](#insn-00bac7f4) → [`00bac7fc`](#insn-00bac7fc)
  - `FALL_THROUGH` [`00bac7f4`](#insn-00bac7f4) → [`00bac7f8`](#insn-00bac7f8)
- ブロック [`00bac7f8`](#insn-00bac7f8) 範囲 `[['00bac7f8', '00bac7fb']]`
  - `FALL_THROUGH` [`00bac7f8`](#insn-00bac7f8) → [`00bac7fc`](#insn-00bac7fc)
- ブロック [`00bac7fc`](#insn-00bac7fc) 範囲 `[['00bac7fc', '00bac7ff']]`
  - `CONDITIONAL_JUMP` [`00bac7fc`](#insn-00bac7fc) → [`00bac804`](#insn-00bac804)
  - `FALL_THROUGH` [`00bac7fc`](#insn-00bac7fc) → [`00bac800`](#insn-00bac800)
- ブロック [`00bac800`](#insn-00bac800) 範囲 `[['00bac800', '00bac803']]`
  - `FALL_THROUGH` [`00bac800`](#insn-00bac800) → [`00bac804`](#insn-00bac804)
- ブロック [`00bac804`](#insn-00bac804) 範囲 `[['00bac804', '00bac80b']]`
  - `UNCONDITIONAL_JUMP` [`00bac808`](#insn-00bac808) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac80c`](#insn-00bac80c) 範囲 `[['00bac80c', '00bac817']]`
  - `FALL_THROUGH` [`00bac814`](#insn-00bac814) → [`00bac818`](#insn-00bac818)
- ブロック [`00bac818`](#insn-00bac818) 範囲 `[['00bac818', '00bac81b']]`
  - `FALL_THROUGH` [`00bac818`](#insn-00bac818) → [`00bac81c`](#insn-00bac81c)
- ブロック [`00bac81c`](#insn-00bac81c) 範囲 `[['00bac81c', '00bac81f']]`
  - `CONDITIONAL_JUMP` [`00bac81c`](#insn-00bac81c) → [`00bac824`](#insn-00bac824)
  - `FALL_THROUGH` [`00bac81c`](#insn-00bac81c) → [`00bac820`](#insn-00bac820)
- ブロック [`00bac820`](#insn-00bac820) 範囲 `[['00bac820', '00bac823']]`
  - `FALL_THROUGH` [`00bac820`](#insn-00bac820) → [`00bac824`](#insn-00bac824)
- ブロック [`00bac824`](#insn-00bac824) 範囲 `[['00bac824', '00bac827']]`
  - `CONDITIONAL_JUMP` [`00bac824`](#insn-00bac824) → [`00bac82c`](#insn-00bac82c)
  - `FALL_THROUGH` [`00bac824`](#insn-00bac824) → [`00bac828`](#insn-00bac828)
- ブロック [`00bac828`](#insn-00bac828) 範囲 `[['00bac828', '00bac82b']]`
  - `FALL_THROUGH` [`00bac828`](#insn-00bac828) → [`00bac82c`](#insn-00bac82c)
- ブロック [`00bac82c`](#insn-00bac82c) 範囲 `[['00bac82c', '00bac83b']]`
  - `UNCONDITIONAL_JUMP` [`00bac838`](#insn-00bac838) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac83c`](#insn-00bac83c) 範囲 `[['00bac83c', '00bac83f']]`
  - `FALL_THROUGH` [`00bac83c`](#insn-00bac83c) → [`00bac840`](#insn-00bac840)
- ブロック [`00bac840`](#insn-00bac840) 範囲 `[['00bac840', '00bac847']]`
  - `FALL_THROUGH` [`00bac844`](#insn-00bac844) → [`00bac848`](#insn-00bac848)
- ブロック [`00bac848`](#insn-00bac848) 範囲 `[['00bac848', '00bac84f']]`
  - `CONDITIONAL_JUMP` [`00bac84c`](#insn-00bac84c) → [`00bac854`](#insn-00bac854)
  - `FALL_THROUGH` [`00bac84c`](#insn-00bac84c) → [`00bac850`](#insn-00bac850)
- ブロック [`00bac850`](#insn-00bac850) 範囲 `[['00bac850', '00bac853']]`
  - `FALL_THROUGH` [`00bac850`](#insn-00bac850) → [`00bac854`](#insn-00bac854)
- ブロック [`00bac854`](#insn-00bac854) 範囲 `[['00bac854', '00bac857']]`
  - `CONDITIONAL_JUMP` [`00bac854`](#insn-00bac854) → [`00bac85c`](#insn-00bac85c)
  - `FALL_THROUGH` [`00bac854`](#insn-00bac854) → [`00bac858`](#insn-00bac858)
- ブロック [`00bac858`](#insn-00bac858) 範囲 `[['00bac858', '00bac85b']]`
  - `FALL_THROUGH` [`00bac858`](#insn-00bac858) → [`00bac85c`](#insn-00bac85c)
- ブロック [`00bac85c`](#insn-00bac85c) 範囲 `[['00bac85c', '00bac86b']]`
  - `UNCONDITIONAL_JUMP` [`00bac868`](#insn-00bac868) → [`00bac460`](#insn-00bac460)
- ブロック [`00bac86c`](#insn-00bac86c) 範囲 `[['00bac86c', '00bac86f']]`
  - `FALL_THROUGH` [`00bac86c`](#insn-00bac86c) → [`00bac870`](#insn-00bac870)
- ブロック [`00bac870`](#insn-00bac870) 範囲 `[['00bac870', '00bac887']]`
  - `CONDITIONAL_JUMP` [`00bac884`](#insn-00bac884) → [`00bac890`](#insn-00bac890)
  - `FALL_THROUGH` [`00bac884`](#insn-00bac884) → [`00bac888`](#insn-00bac888)
- ブロック [`00bac888`](#insn-00bac888) 範囲 `[['00bac888', '00bac88f']]`
  - `FALL_THROUGH` [`00bac88c`](#insn-00bac88c) → [`00bac890`](#insn-00bac890)
- ブロック [`00bac890`](#insn-00bac890) 範囲 `[['00bac890', '00bac8b3']]`
  - `UNCONDITIONAL_JUMP` [`00bac8b0`](#insn-00bac8b0) → [`00bac45c`](#insn-00bac45c)
- ブロック [`00bac8b4`](#insn-00bac8b4) 範囲 `[['00bac8b4', '00bac8b7']]`

## 命令位置別の参照

- [`00babfa0`](#insn-00babfa0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfa4`](#insn-00babfa4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfa8`](#insn-00babfa8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfb8`](#insn-00babfb8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfc4`](#insn-00babfc4) → [`00bac23c`](#insn-00bac23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00babfe4::default` · 推定型 `None`
- [`00babfd4`](#insn-00babfd4) → `0030e273`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::switchdataD_0030e273` · 推定型 `byte`
- [`00babfe4`](#insn-00babfe4) → [`00babfe8`](#insn-00babfe8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_0` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac244`](#insn-00bac244) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_1` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac1c4`](#insn-00bac1c4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_2` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac20c`](#insn-00bac20c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_3` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac0a8`](#insn-00bac0a8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_4` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac25c`](#insn-00bac25c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_5` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac274`](#insn-00bac274) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_6` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac224`](#insn-00bac224) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_7` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac28c`](#insn-00bac28c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_8` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac0f0`](#insn-00bac0f0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_9` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac2a4`](#insn-00bac2a4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_a` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac030`](#insn-00bac030) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_b` · 推定型 `None`
- [`00babfe4`](#insn-00babfe4) → [`00bac148`](#insn-00bac148) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00babfe4::caseD_c` · 推定型 `None`
- [`00babfe8`](#insn-00babfe8) → [`00babff0`](#insn-00babff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babfec`](#insn-00babfec) → [`00bac24c`](#insn-00bac24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac008`](#insn-00bac008) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac01c`](#insn-00bac01c) → [`00bac3cc`](#insn-00bac3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac028`](#insn-00bac028) → [`00bac010`](#insn-00bac010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac02c`](#insn-00bac02c) → [`00bac3fc`](#insn-00bac3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac030`](#insn-00bac030) → [`00bac03c`](#insn-00bac03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac038`](#insn-00bac038) → [`00bac08c`](#insn-00bac08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac058`](#insn-00bac058) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac05c`](#insn-00bac05c) → [`00c59650`](../00c59/00c59650.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59650` · 推定シンボル `None` · 推定型 `None`
- [`00bac060`](#insn-00bac060) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac06c`](#insn-00bac06c) → [`00bac08c`](#insn-00bac08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac074`](#insn-00bac074) → [`00bac08c`](#insn-00bac08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac080`](#insn-00bac080) → [`00bac08c`](#insn-00bac08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac090`](#insn-00bac090) → [`00bac098`](#insn-00bac098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac098`](#insn-00bac098) → [`00bac0a0`](#insn-00bac0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0a4`](#insn-00bac0a4) → [`00bac1bc`](#insn-00bac1bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0a8`](#insn-00bac0a8) → [`00bac0b0`](#insn-00bac0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0ac`](#insn-00bac0ac) → [`00bac24c`](#insn-00bac24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0c8`](#insn-00bac0c8) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0dc`](#insn-00bac0dc) → [`00bac3cc`](#insn-00bac3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0e8`](#insn-00bac0e8) → [`00bac0d0`](#insn-00bac0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0ec`](#insn-00bac0ec) → [`00bac3fc`](#insn-00bac3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0f0`](#insn-00bac0f0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0f4`](#insn-00bac0f4) → [`00bac0fc`](#insn-00bac0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac0f8`](#insn-00bac0f8) → [`00bac120`](#insn-00bac120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac11c`](#insn-00bac11c) → [`00c5d250`](../00c5d/00c5d250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d250` · 推定シンボル `None` · 推定型 `None`
- [`00bac134`](#insn-00bac134) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac138`](#insn-00bac138) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac144`](#insn-00bac144) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac148`](#insn-00bac148) → [`00bac154`](#insn-00bac154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac150`](#insn-00bac150) → [`00bac1a4`](#insn-00bac1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac170`](#insn-00bac170) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac174`](#insn-00bac174) → [`00c59660`](../00c59/00c59660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59660` · 推定シンボル `None` · 推定型 `None`
- [`00bac178`](#insn-00bac178) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac184`](#insn-00bac184) → [`00bac1a4`](#insn-00bac1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac18c`](#insn-00bac18c) → [`00bac1a4`](#insn-00bac1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac198`](#insn-00bac198) → [`00bac1a4`](#insn-00bac1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1a8`](#insn-00bac1a8) → [`00bac1b0`](#insn-00bac1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1b0`](#insn-00bac1b0) → [`00bac1b8`](#insn-00bac1b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1c0`](#insn-00bac1c0) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1c4`](#insn-00bac1c4) → [`00bac1cc`](#insn-00bac1cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1c8`](#insn-00bac1c8) → [`00bac24c`](#insn-00bac24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1e4`](#insn-00bac1e4) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac1f8`](#insn-00bac1f8) → [`00bac3cc`](#insn-00bac3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac204`](#insn-00bac204) → [`00bac1ec`](#insn-00bac1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac208`](#insn-00bac208) → [`00bac3fc`](#insn-00bac3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac20c`](#insn-00bac20c) → [`00bac30c`](#insn-00bac30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac210`](#insn-00bac210) → [`00bac30c`](#insn-00bac30c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac21c`](#insn-00bac21c) → [`00bac820`](#insn-00bac820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac220`](#insn-00bac220) → [`00bac824`](#insn-00bac824) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac224`](#insn-00bac224) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac228`](#insn-00bac228) → [`00bac34c`](#insn-00bac34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac234`](#insn-00bac234) → [`00bac650`](#insn-00bac650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac238`](#insn-00bac238) → [`00bac654`](#insn-00bac654) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac240`](#insn-00bac240) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac244`](#insn-00bac244) → [`00bac38c`](#insn-00bac38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac248`](#insn-00bac248) → [`00bac38c`](#insn-00bac38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac254`](#insn-00bac254) → [`00bac448`](#insn-00bac448) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac258`](#insn-00bac258) → [`00bac44c`](#insn-00bac44c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac25c`](#insn-00bac25c) → [`00bac484`](#insn-00bac484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac260`](#insn-00bac260) → [`00bac484`](#insn-00bac484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac26c`](#insn-00bac26c) → [`00bac850`](#insn-00bac850) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac270`](#insn-00bac270) → [`00bac854`](#insn-00bac854) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac274`](#insn-00bac274) → [`00bac4c4`](#insn-00bac4c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac278`](#insn-00bac278) → [`00bac4c4`](#insn-00bac4c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac284`](#insn-00bac284) → [`00bac764`](#insn-00bac764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac288`](#insn-00bac288) → [`00bac768`](#insn-00bac768) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac28c`](#insn-00bac28c) → [`00bac504`](#insn-00bac504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac290`](#insn-00bac290) → [`00bac504`](#insn-00bac504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac29c`](#insn-00bac29c) → [`00bac7f8`](#insn-00bac7f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a0`](#insn-00bac2a0) → [`00bac7fc`](#insn-00bac7fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a4`](#insn-00bac2a4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2a8`](#insn-00bac2a8) → [`00bac2b0`](#insn-00bac2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2ac`](#insn-00bac2ac) → [`00bac890`](#insn-00bac890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2d4`](#insn-00bac2d4) → [`00c5d260`](../00c5d/00c5d260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d260` · 推定シンボル `None` · 推定型 `None`
- [`00bac2d8`](#insn-00bac2d8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2dc`](#insn-00bac2dc) → [`00bac890`](#insn-00bac890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2e0`](#insn-00bac2e0) → [`00bac890`](#insn-00bac890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2e8`](#insn-00bac2e8) → [`00bac86c`](#insn-00bac86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac2fc`](#insn-00bac2fc) → [`00bac870`](#insn-00bac870) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac304`](#insn-00bac304) → [`00bac2f0`](#insn-00bac2f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac308`](#insn-00bac308) → [`00bac870`](#insn-00bac870) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac324`](#insn-00bac324) → [`00bac574`](#insn-00bac574) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac338`](#insn-00bac338) → [`00bac544`](#insn-00bac544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac344`](#insn-00bac344) → [`00bac32c`](#insn-00bac32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac348`](#insn-00bac348) → [`00bac574`](#insn-00bac574) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac364`](#insn-00bac364) → [`00bac5f4`](#insn-00bac5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac378`](#insn-00bac378) → [`00bac5c4`](#insn-00bac5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac384`](#insn-00bac384) → [`00bac36c`](#insn-00bac36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac388`](#insn-00bac388) → [`00bac5f4`](#insn-00bac5f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3a4`](#insn-00bac3a4) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3b8`](#insn-00bac3b8) → [`00bac3cc`](#insn-00bac3cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3c4`](#insn-00bac3c4) → [`00bac3ac`](#insn-00bac3ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3c8`](#insn-00bac3c8) → [`00bac3fc`](#insn-00bac3fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3d0`](#insn-00bac3d0) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3e0`](#insn-00bac3e0) → [`00bac3fc`](#insn-00bac3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3e8`](#insn-00bac3e8) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac3f4`](#insn-00bac3f4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac3f8`](#insn-00bac3f8) → [`00bac410`](#insn-00bac410) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac400`](#insn-00bac400) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac404`](#insn-00bac404) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac410`](#insn-00bac410) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac418`](#insn-00bac418) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac41c`](#insn-00bac41c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac428`](#insn-00bac428) → [`00bac440`](#insn-00bac440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac430`](#insn-00bac430) → [`00bac440`](#insn-00bac440) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac444`](#insn-00bac444) → [`00bac44c`](#insn-00bac44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac44c`](#insn-00bac44c) → [`00bac454`](#insn-00bac454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac464`](#insn-00bac464) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac46c`](#insn-00bac46c) → [`00bac8b4`](#insn-00bac8b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac470`](#insn-00bac470) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac474`](#insn-00bac474) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac478`](#insn-00bac478) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac49c`](#insn-00bac49c) → [`00bac698`](#insn-00bac698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4b0`](#insn-00bac4b0) → [`00bac668`](#insn-00bac668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4bc`](#insn-00bac4bc) → [`00bac4a4`](#insn-00bac4a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4c0`](#insn-00bac4c0) → [`00bac698`](#insn-00bac698) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4dc`](#insn-00bac4dc) → [`00bac718`](#insn-00bac718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4f0`](#insn-00bac4f0) → [`00bac6e8`](#insn-00bac6e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac4fc`](#insn-00bac4fc) → [`00bac4e4`](#insn-00bac4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac500`](#insn-00bac500) → [`00bac718`](#insn-00bac718) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac51c`](#insn-00bac51c) → [`00bac7ac`](#insn-00bac7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac530`](#insn-00bac530) → [`00bac77c`](#insn-00bac77c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac53c`](#insn-00bac53c) → [`00bac524`](#insn-00bac524) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac540`](#insn-00bac540) → [`00bac7ac`](#insn-00bac7ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac548`](#insn-00bac548) → [`00bac574`](#insn-00bac574) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac558`](#insn-00bac558) → [`00bac574`](#insn-00bac574) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac560`](#insn-00bac560) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac56c`](#insn-00bac56c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac570`](#insn-00bac570) → [`00bac588`](#insn-00bac588) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac578`](#insn-00bac578) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac57c`](#insn-00bac57c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac588`](#insn-00bac588) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac590`](#insn-00bac590) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac594`](#insn-00bac594) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5a0`](#insn-00bac5a0) → [`00bac818`](#insn-00bac818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5a8`](#insn-00bac5a8) → [`00bac818`](#insn-00bac818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5b0`](#insn-00bac5b0) → [`00bac80c`](#insn-00bac80c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5bc`](#insn-00bac5bc) → [`00bac820`](#insn-00bac820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5c0`](#insn-00bac5c0) → [`00bac824`](#insn-00bac824) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5c8`](#insn-00bac5c8) → [`00bac5f4`](#insn-00bac5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5d8`](#insn-00bac5d8) → [`00bac5f4`](#insn-00bac5f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5e0`](#insn-00bac5e0) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac5ec`](#insn-00bac5ec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5f0`](#insn-00bac5f0) → [`00bac608`](#insn-00bac608) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac5f8`](#insn-00bac5f8) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac5fc`](#insn-00bac5fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac608`](#insn-00bac608) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac610`](#insn-00bac610) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac614`](#insn-00bac614) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac620`](#insn-00bac620) → [`00bac648`](#insn-00bac648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac628`](#insn-00bac628) → [`00bac648`](#insn-00bac648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac634`](#insn-00bac634) → [`00bac648`](#insn-00bac648) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac64c`](#insn-00bac64c) → [`00bac654`](#insn-00bac654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac654`](#insn-00bac654) → [`00bac65c`](#insn-00bac65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac664`](#insn-00bac664) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac66c`](#insn-00bac66c) → [`00bac698`](#insn-00bac698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac67c`](#insn-00bac67c) → [`00bac698`](#insn-00bac698) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac684`](#insn-00bac684) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac690`](#insn-00bac690) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac694`](#insn-00bac694) → [`00bac6ac`](#insn-00bac6ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac69c`](#insn-00bac69c) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac6a0`](#insn-00bac6a0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6ac`](#insn-00bac6ac) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac6b4`](#insn-00bac6b4) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac6b8`](#insn-00bac6b8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6c4`](#insn-00bac6c4) → [`00bac848`](#insn-00bac848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6cc`](#insn-00bac6cc) → [`00bac848`](#insn-00bac848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6d4`](#insn-00bac6d4) → [`00bac83c`](#insn-00bac83c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6e0`](#insn-00bac6e0) → [`00bac850`](#insn-00bac850) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6e4`](#insn-00bac6e4) → [`00bac854`](#insn-00bac854) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6ec`](#insn-00bac6ec) → [`00bac718`](#insn-00bac718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac6fc`](#insn-00bac6fc) → [`00bac718`](#insn-00bac718) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac704`](#insn-00bac704) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac710`](#insn-00bac710) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac714`](#insn-00bac714) → [`00bac72c`](#insn-00bac72c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac71c`](#insn-00bac71c) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac720`](#insn-00bac720) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac72c`](#insn-00bac72c) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac734`](#insn-00bac734) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac738`](#insn-00bac738) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac744`](#insn-00bac744) → [`00bac75c`](#insn-00bac75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac74c`](#insn-00bac74c) → [`00bac75c`](#insn-00bac75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac760`](#insn-00bac760) → [`00bac768`](#insn-00bac768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac768`](#insn-00bac768) → [`00bac770`](#insn-00bac770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac778`](#insn-00bac778) → [`00bac45c`](#insn-00bac45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac780`](#insn-00bac780) → [`00bac7ac`](#insn-00bac7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac790`](#insn-00bac790) → [`00bac7ac`](#insn-00bac7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac798`](#insn-00bac798) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac7a4`](#insn-00bac7a4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7a8`](#insn-00bac7a8) → [`00bac7c0`](#insn-00bac7c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7b0`](#insn-00bac7b0) → `00c9c8d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bac7b4`](#insn-00bac7b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7c0`](#insn-00bac7c0) → `011272a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bac7c8`](#insn-00bac7c8) → [`00c5e1f0`](../00c5e/00c5e1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e1f0` · 推定シンボル `None` · 推定型 `None`
- [`00bac7cc`](#insn-00bac7cc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7d8`](#insn-00bac7d8) → [`00bac7f0`](#insn-00bac7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7e0`](#insn-00bac7e0) → [`00bac7f0`](#insn-00bac7f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7f4`](#insn-00bac7f4) → [`00bac7fc`](#insn-00bac7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac7fc`](#insn-00bac7fc) → [`00bac804`](#insn-00bac804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac808`](#insn-00bac808) → [`00bac45c`](#insn-00bac45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac81c`](#insn-00bac81c) → [`00bac824`](#insn-00bac824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac824`](#insn-00bac824) → [`00bac82c`](#insn-00bac82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac838`](#insn-00bac838) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac84c`](#insn-00bac84c) → [`00bac854`](#insn-00bac854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac854`](#insn-00bac854) → [`00bac85c`](#insn-00bac85c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac868`](#insn-00bac868) → [`00bac460`](#insn-00bac460) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac884`](#insn-00bac884) → [`00bac890`](#insn-00bac890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac88c`](#insn-00bac88c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8a4`](#insn-00bac8a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8a8`](#insn-00bac8a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8b0`](#insn-00bac8b0) → [`00bac45c`](#insn-00bac45c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bac8b4`](#insn-00bac8b4) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babfa0`](#insn-00babfa0)

~~~json
{
  "source": "00babfa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfa4`](#insn-00babfa4)

~~~json
{
  "source": "00babfa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfa8`](#insn-00babfa8)

~~~json
{
  "source": "00babfa8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfb8`](#insn-00babfb8)

~~~json
{
  "source": "00babfb8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfc4`](#insn-00babfc4)

~~~json
{
  "source": "00babfc4",
  "target": "00bac23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfd4`](#insn-00babfd4)

~~~json
{
  "source": "00babfd4",
  "target": "0030e273",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e273",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e273",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00babfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe4`](#insn-00babfe4)

~~~json
{
  "source": "00babfe4",
  "target": "00bac148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfe8`](#insn-00babfe8)

~~~json
{
  "source": "00babfe8",
  "target": "00babff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babfec`](#insn-00babfec)

~~~json
{
  "source": "00babfec",
  "target": "00bac24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac008`](#insn-00bac008)

~~~json
{
  "source": "00bac008",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac01c`](#insn-00bac01c)

~~~json
{
  "source": "00bac01c",
  "target": "00bac3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac028`](#insn-00bac028)

~~~json
{
  "source": "00bac028",
  "target": "00bac010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac02c`](#insn-00bac02c)

~~~json
{
  "source": "00bac02c",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac030`](#insn-00bac030)

~~~json
{
  "source": "00bac030",
  "target": "00bac03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac038`](#insn-00bac038)

~~~json
{
  "source": "00bac038",
  "target": "00bac08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac058`](#insn-00bac058)

~~~json
{
  "source": "00bac058",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac05c`](#insn-00bac05c)

~~~json
{
  "source": "00bac05c",
  "target": "00c59650",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac060`](#insn-00bac060)

~~~json
{
  "source": "00bac060",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac06c`](#insn-00bac06c)

~~~json
{
  "source": "00bac06c",
  "target": "00bac08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac074`](#insn-00bac074)

~~~json
{
  "source": "00bac074",
  "target": "00bac08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac080`](#insn-00bac080)

~~~json
{
  "source": "00bac080",
  "target": "00bac08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac090`](#insn-00bac090)

~~~json
{
  "source": "00bac090",
  "target": "00bac098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac098`](#insn-00bac098)

~~~json
{
  "source": "00bac098",
  "target": "00bac0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0a4`](#insn-00bac0a4)

~~~json
{
  "source": "00bac0a4",
  "target": "00bac1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0a8`](#insn-00bac0a8)

~~~json
{
  "source": "00bac0a8",
  "target": "00bac0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0ac`](#insn-00bac0ac)

~~~json
{
  "source": "00bac0ac",
  "target": "00bac24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0c8`](#insn-00bac0c8)

~~~json
{
  "source": "00bac0c8",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0dc`](#insn-00bac0dc)

~~~json
{
  "source": "00bac0dc",
  "target": "00bac3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0e8`](#insn-00bac0e8)

~~~json
{
  "source": "00bac0e8",
  "target": "00bac0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0ec`](#insn-00bac0ec)

~~~json
{
  "source": "00bac0ec",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0f0`](#insn-00bac0f0)

~~~json
{
  "source": "00bac0f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0f4`](#insn-00bac0f4)

~~~json
{
  "source": "00bac0f4",
  "target": "00bac0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac0f8`](#insn-00bac0f8)

~~~json
{
  "source": "00bac0f8",
  "target": "00bac120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac11c`](#insn-00bac11c)

~~~json
{
  "source": "00bac11c",
  "target": "00c5d250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac134`](#insn-00bac134)

~~~json
{
  "source": "00bac134",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac138`](#insn-00bac138)

~~~json
{
  "source": "00bac138",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac144`](#insn-00bac144)

~~~json
{
  "source": "00bac144",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac148`](#insn-00bac148)

~~~json
{
  "source": "00bac148",
  "target": "00bac154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac150`](#insn-00bac150)

~~~json
{
  "source": "00bac150",
  "target": "00bac1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac170`](#insn-00bac170)

~~~json
{
  "source": "00bac170",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac174`](#insn-00bac174)

~~~json
{
  "source": "00bac174",
  "target": "00c59660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac178`](#insn-00bac178)

~~~json
{
  "source": "00bac178",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac184`](#insn-00bac184)

~~~json
{
  "source": "00bac184",
  "target": "00bac1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac18c`](#insn-00bac18c)

~~~json
{
  "source": "00bac18c",
  "target": "00bac1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac198`](#insn-00bac198)

~~~json
{
  "source": "00bac198",
  "target": "00bac1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1a8`](#insn-00bac1a8)

~~~json
{
  "source": "00bac1a8",
  "target": "00bac1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1b0`](#insn-00bac1b0)

~~~json
{
  "source": "00bac1b0",
  "target": "00bac1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1c0`](#insn-00bac1c0)

~~~json
{
  "source": "00bac1c0",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1c4`](#insn-00bac1c4)

~~~json
{
  "source": "00bac1c4",
  "target": "00bac1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1c8`](#insn-00bac1c8)

~~~json
{
  "source": "00bac1c8",
  "target": "00bac24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1e4`](#insn-00bac1e4)

~~~json
{
  "source": "00bac1e4",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac1f8`](#insn-00bac1f8)

~~~json
{
  "source": "00bac1f8",
  "target": "00bac3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac204`](#insn-00bac204)

~~~json
{
  "source": "00bac204",
  "target": "00bac1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac208`](#insn-00bac208)

~~~json
{
  "source": "00bac208",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac20c`](#insn-00bac20c)

~~~json
{
  "source": "00bac20c",
  "target": "00bac30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac210`](#insn-00bac210)

~~~json
{
  "source": "00bac210",
  "target": "00bac30c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac21c`](#insn-00bac21c)

~~~json
{
  "source": "00bac21c",
  "target": "00bac820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac220`](#insn-00bac220)

~~~json
{
  "source": "00bac220",
  "target": "00bac824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac224`](#insn-00bac224)

~~~json
{
  "source": "00bac224",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac228`](#insn-00bac228)

~~~json
{
  "source": "00bac228",
  "target": "00bac34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac234`](#insn-00bac234)

~~~json
{
  "source": "00bac234",
  "target": "00bac650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac238`](#insn-00bac238)

~~~json
{
  "source": "00bac238",
  "target": "00bac654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac240`](#insn-00bac240)

~~~json
{
  "source": "00bac240",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac244`](#insn-00bac244)

~~~json
{
  "source": "00bac244",
  "target": "00bac38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac248`](#insn-00bac248)

~~~json
{
  "source": "00bac248",
  "target": "00bac38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac254`](#insn-00bac254)

~~~json
{
  "source": "00bac254",
  "target": "00bac448",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac258`](#insn-00bac258)

~~~json
{
  "source": "00bac258",
  "target": "00bac44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac25c`](#insn-00bac25c)

~~~json
{
  "source": "00bac25c",
  "target": "00bac484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac260`](#insn-00bac260)

~~~json
{
  "source": "00bac260",
  "target": "00bac484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac26c`](#insn-00bac26c)

~~~json
{
  "source": "00bac26c",
  "target": "00bac850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac270`](#insn-00bac270)

~~~json
{
  "source": "00bac270",
  "target": "00bac854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac274`](#insn-00bac274)

~~~json
{
  "source": "00bac274",
  "target": "00bac4c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac278`](#insn-00bac278)

~~~json
{
  "source": "00bac278",
  "target": "00bac4c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac284`](#insn-00bac284)

~~~json
{
  "source": "00bac284",
  "target": "00bac764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac288`](#insn-00bac288)

~~~json
{
  "source": "00bac288",
  "target": "00bac768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac28c`](#insn-00bac28c)

~~~json
{
  "source": "00bac28c",
  "target": "00bac504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac290`](#insn-00bac290)

~~~json
{
  "source": "00bac290",
  "target": "00bac504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac29c`](#insn-00bac29c)

~~~json
{
  "source": "00bac29c",
  "target": "00bac7f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2a0`](#insn-00bac2a0)

~~~json
{
  "source": "00bac2a0",
  "target": "00bac7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2a4`](#insn-00bac2a4)

~~~json
{
  "source": "00bac2a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2a8`](#insn-00bac2a8)

~~~json
{
  "source": "00bac2a8",
  "target": "00bac2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2ac`](#insn-00bac2ac)

~~~json
{
  "source": "00bac2ac",
  "target": "00bac890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2d4`](#insn-00bac2d4)

~~~json
{
  "source": "00bac2d4",
  "target": "00c5d260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac2d8`](#insn-00bac2d8)

~~~json
{
  "source": "00bac2d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2dc`](#insn-00bac2dc)

~~~json
{
  "source": "00bac2dc",
  "target": "00bac890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2e0`](#insn-00bac2e0)

~~~json
{
  "source": "00bac2e0",
  "target": "00bac890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2e8`](#insn-00bac2e8)

~~~json
{
  "source": "00bac2e8",
  "target": "00bac86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac2fc`](#insn-00bac2fc)

~~~json
{
  "source": "00bac2fc",
  "target": "00bac870",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac304`](#insn-00bac304)

~~~json
{
  "source": "00bac304",
  "target": "00bac2f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac308`](#insn-00bac308)

~~~json
{
  "source": "00bac308",
  "target": "00bac870",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac324`](#insn-00bac324)

~~~json
{
  "source": "00bac324",
  "target": "00bac574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac338`](#insn-00bac338)

~~~json
{
  "source": "00bac338",
  "target": "00bac544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac344`](#insn-00bac344)

~~~json
{
  "source": "00bac344",
  "target": "00bac32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac348`](#insn-00bac348)

~~~json
{
  "source": "00bac348",
  "target": "00bac574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac364`](#insn-00bac364)

~~~json
{
  "source": "00bac364",
  "target": "00bac5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac378`](#insn-00bac378)

~~~json
{
  "source": "00bac378",
  "target": "00bac5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac384`](#insn-00bac384)

~~~json
{
  "source": "00bac384",
  "target": "00bac36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac388`](#insn-00bac388)

~~~json
{
  "source": "00bac388",
  "target": "00bac5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3a4`](#insn-00bac3a4)

~~~json
{
  "source": "00bac3a4",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3b8`](#insn-00bac3b8)

~~~json
{
  "source": "00bac3b8",
  "target": "00bac3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3c4`](#insn-00bac3c4)

~~~json
{
  "source": "00bac3c4",
  "target": "00bac3ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3c8`](#insn-00bac3c8)

~~~json
{
  "source": "00bac3c8",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3d0`](#insn-00bac3d0)

~~~json
{
  "source": "00bac3d0",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3e0`](#insn-00bac3e0)

~~~json
{
  "source": "00bac3e0",
  "target": "00bac3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3e8`](#insn-00bac3e8)

~~~json
{
  "source": "00bac3e8",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac3f4`](#insn-00bac3f4)

~~~json
{
  "source": "00bac3f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac3f8`](#insn-00bac3f8)

~~~json
{
  "source": "00bac3f8",
  "target": "00bac410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac400`](#insn-00bac400)

~~~json
{
  "source": "00bac400",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac404`](#insn-00bac404)

~~~json
{
  "source": "00bac404",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac410`](#insn-00bac410)

~~~json
{
  "source": "00bac410",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac418`](#insn-00bac418)

~~~json
{
  "source": "00bac418",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac41c`](#insn-00bac41c)

~~~json
{
  "source": "00bac41c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac428`](#insn-00bac428)

~~~json
{
  "source": "00bac428",
  "target": "00bac440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac430`](#insn-00bac430)

~~~json
{
  "source": "00bac430",
  "target": "00bac440",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac444`](#insn-00bac444)

~~~json
{
  "source": "00bac444",
  "target": "00bac44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac44c`](#insn-00bac44c)

~~~json
{
  "source": "00bac44c",
  "target": "00bac454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac464`](#insn-00bac464)

~~~json
{
  "source": "00bac464",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac46c`](#insn-00bac46c)

~~~json
{
  "source": "00bac46c",
  "target": "00bac8b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac470`](#insn-00bac470)

~~~json
{
  "source": "00bac470",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac474`](#insn-00bac474)

~~~json
{
  "source": "00bac474",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac478`](#insn-00bac478)

~~~json
{
  "source": "00bac478",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac49c`](#insn-00bac49c)

~~~json
{
  "source": "00bac49c",
  "target": "00bac698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4b0`](#insn-00bac4b0)

~~~json
{
  "source": "00bac4b0",
  "target": "00bac668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4bc`](#insn-00bac4bc)

~~~json
{
  "source": "00bac4bc",
  "target": "00bac4a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4c0`](#insn-00bac4c0)

~~~json
{
  "source": "00bac4c0",
  "target": "00bac698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4dc`](#insn-00bac4dc)

~~~json
{
  "source": "00bac4dc",
  "target": "00bac718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4f0`](#insn-00bac4f0)

~~~json
{
  "source": "00bac4f0",
  "target": "00bac6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac4fc`](#insn-00bac4fc)

~~~json
{
  "source": "00bac4fc",
  "target": "00bac4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac500`](#insn-00bac500)

~~~json
{
  "source": "00bac500",
  "target": "00bac718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac51c`](#insn-00bac51c)

~~~json
{
  "source": "00bac51c",
  "target": "00bac7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac530`](#insn-00bac530)

~~~json
{
  "source": "00bac530",
  "target": "00bac77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac53c`](#insn-00bac53c)

~~~json
{
  "source": "00bac53c",
  "target": "00bac524",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac540`](#insn-00bac540)

~~~json
{
  "source": "00bac540",
  "target": "00bac7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac548`](#insn-00bac548)

~~~json
{
  "source": "00bac548",
  "target": "00bac574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac558`](#insn-00bac558)

~~~json
{
  "source": "00bac558",
  "target": "00bac574",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac560`](#insn-00bac560)

~~~json
{
  "source": "00bac560",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac56c`](#insn-00bac56c)

~~~json
{
  "source": "00bac56c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac570`](#insn-00bac570)

~~~json
{
  "source": "00bac570",
  "target": "00bac588",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac578`](#insn-00bac578)

~~~json
{
  "source": "00bac578",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac57c`](#insn-00bac57c)

~~~json
{
  "source": "00bac57c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac588`](#insn-00bac588)

~~~json
{
  "source": "00bac588",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac590`](#insn-00bac590)

~~~json
{
  "source": "00bac590",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac594`](#insn-00bac594)

~~~json
{
  "source": "00bac594",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5a0`](#insn-00bac5a0)

~~~json
{
  "source": "00bac5a0",
  "target": "00bac818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5a8`](#insn-00bac5a8)

~~~json
{
  "source": "00bac5a8",
  "target": "00bac818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5b0`](#insn-00bac5b0)

~~~json
{
  "source": "00bac5b0",
  "target": "00bac80c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5bc`](#insn-00bac5bc)

~~~json
{
  "source": "00bac5bc",
  "target": "00bac820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5c0`](#insn-00bac5c0)

~~~json
{
  "source": "00bac5c0",
  "target": "00bac824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5c8`](#insn-00bac5c8)

~~~json
{
  "source": "00bac5c8",
  "target": "00bac5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5d8`](#insn-00bac5d8)

~~~json
{
  "source": "00bac5d8",
  "target": "00bac5f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5e0`](#insn-00bac5e0)

~~~json
{
  "source": "00bac5e0",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac5ec`](#insn-00bac5ec)

~~~json
{
  "source": "00bac5ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5f0`](#insn-00bac5f0)

~~~json
{
  "source": "00bac5f0",
  "target": "00bac608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac5f8`](#insn-00bac5f8)

~~~json
{
  "source": "00bac5f8",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac5fc`](#insn-00bac5fc)

~~~json
{
  "source": "00bac5fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac608`](#insn-00bac608)

~~~json
{
  "source": "00bac608",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac610`](#insn-00bac610)

~~~json
{
  "source": "00bac610",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac614`](#insn-00bac614)

~~~json
{
  "source": "00bac614",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac620`](#insn-00bac620)

~~~json
{
  "source": "00bac620",
  "target": "00bac648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac628`](#insn-00bac628)

~~~json
{
  "source": "00bac628",
  "target": "00bac648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac634`](#insn-00bac634)

~~~json
{
  "source": "00bac634",
  "target": "00bac648",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac64c`](#insn-00bac64c)

~~~json
{
  "source": "00bac64c",
  "target": "00bac654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac654`](#insn-00bac654)

~~~json
{
  "source": "00bac654",
  "target": "00bac65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac664`](#insn-00bac664)

~~~json
{
  "source": "00bac664",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac66c`](#insn-00bac66c)

~~~json
{
  "source": "00bac66c",
  "target": "00bac698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac67c`](#insn-00bac67c)

~~~json
{
  "source": "00bac67c",
  "target": "00bac698",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac684`](#insn-00bac684)

~~~json
{
  "source": "00bac684",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac690`](#insn-00bac690)

~~~json
{
  "source": "00bac690",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac694`](#insn-00bac694)

~~~json
{
  "source": "00bac694",
  "target": "00bac6ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac69c`](#insn-00bac69c)

~~~json
{
  "source": "00bac69c",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac6a0`](#insn-00bac6a0)

~~~json
{
  "source": "00bac6a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6ac`](#insn-00bac6ac)

~~~json
{
  "source": "00bac6ac",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac6b4`](#insn-00bac6b4)

~~~json
{
  "source": "00bac6b4",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac6b8`](#insn-00bac6b8)

~~~json
{
  "source": "00bac6b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6c4`](#insn-00bac6c4)

~~~json
{
  "source": "00bac6c4",
  "target": "00bac848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6cc`](#insn-00bac6cc)

~~~json
{
  "source": "00bac6cc",
  "target": "00bac848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6d4`](#insn-00bac6d4)

~~~json
{
  "source": "00bac6d4",
  "target": "00bac83c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6e0`](#insn-00bac6e0)

~~~json
{
  "source": "00bac6e0",
  "target": "00bac850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6e4`](#insn-00bac6e4)

~~~json
{
  "source": "00bac6e4",
  "target": "00bac854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6ec`](#insn-00bac6ec)

~~~json
{
  "source": "00bac6ec",
  "target": "00bac718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac6fc`](#insn-00bac6fc)

~~~json
{
  "source": "00bac6fc",
  "target": "00bac718",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac704`](#insn-00bac704)

~~~json
{
  "source": "00bac704",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac710`](#insn-00bac710)

~~~json
{
  "source": "00bac710",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac714`](#insn-00bac714)

~~~json
{
  "source": "00bac714",
  "target": "00bac72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac71c`](#insn-00bac71c)

~~~json
{
  "source": "00bac71c",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac720`](#insn-00bac720)

~~~json
{
  "source": "00bac720",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac72c`](#insn-00bac72c)

~~~json
{
  "source": "00bac72c",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac734`](#insn-00bac734)

~~~json
{
  "source": "00bac734",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac738`](#insn-00bac738)

~~~json
{
  "source": "00bac738",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac744`](#insn-00bac744)

~~~json
{
  "source": "00bac744",
  "target": "00bac75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac74c`](#insn-00bac74c)

~~~json
{
  "source": "00bac74c",
  "target": "00bac75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac760`](#insn-00bac760)

~~~json
{
  "source": "00bac760",
  "target": "00bac768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac768`](#insn-00bac768)

~~~json
{
  "source": "00bac768",
  "target": "00bac770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac778`](#insn-00bac778)

~~~json
{
  "source": "00bac778",
  "target": "00bac45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac780`](#insn-00bac780)

~~~json
{
  "source": "00bac780",
  "target": "00bac7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac790`](#insn-00bac790)

~~~json
{
  "source": "00bac790",
  "target": "00bac7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac798`](#insn-00bac798)

~~~json
{
  "source": "00bac798",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac7a4`](#insn-00bac7a4)

~~~json
{
  "source": "00bac7a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7a8`](#insn-00bac7a8)

~~~json
{
  "source": "00bac7a8",
  "target": "00bac7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7b0`](#insn-00bac7b0)

~~~json
{
  "source": "00bac7b0",
  "target": "00c9c8d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bac7b4`](#insn-00bac7b4)

~~~json
{
  "source": "00bac7b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7c0`](#insn-00bac7c0)

~~~json
{
  "source": "00bac7c0",
  "target": "011272a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011272a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bac7c8`](#insn-00bac7c8)

~~~json
{
  "source": "00bac7c8",
  "target": "00c5e1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bac7cc`](#insn-00bac7cc)

~~~json
{
  "source": "00bac7cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7d8`](#insn-00bac7d8)

~~~json
{
  "source": "00bac7d8",
  "target": "00bac7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7e0`](#insn-00bac7e0)

~~~json
{
  "source": "00bac7e0",
  "target": "00bac7f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7f4`](#insn-00bac7f4)

~~~json
{
  "source": "00bac7f4",
  "target": "00bac7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac7fc`](#insn-00bac7fc)

~~~json
{
  "source": "00bac7fc",
  "target": "00bac804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac808`](#insn-00bac808)

~~~json
{
  "source": "00bac808",
  "target": "00bac45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac81c`](#insn-00bac81c)

~~~json
{
  "source": "00bac81c",
  "target": "00bac824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac824`](#insn-00bac824)

~~~json
{
  "source": "00bac824",
  "target": "00bac82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac838`](#insn-00bac838)

~~~json
{
  "source": "00bac838",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac84c`](#insn-00bac84c)

~~~json
{
  "source": "00bac84c",
  "target": "00bac854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac854`](#insn-00bac854)

~~~json
{
  "source": "00bac854",
  "target": "00bac85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac868`](#insn-00bac868)

~~~json
{
  "source": "00bac868",
  "target": "00bac460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac884`](#insn-00bac884)

~~~json
{
  "source": "00bac884",
  "target": "00bac890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac88c`](#insn-00bac88c)

~~~json
{
  "source": "00bac88c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8a4`](#insn-00bac8a4)

~~~json
{
  "source": "00bac8a4",
  "target": "Stack[-0x40]",
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
- 参照命令 [`00bac8b0`](#insn-00bac8b0)

~~~json
{
  "source": "00bac8b0",
  "target": "00bac45c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bac8b4`](#insn-00bac8b4)

~~~json
{
  "source": "00bac8b4",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
