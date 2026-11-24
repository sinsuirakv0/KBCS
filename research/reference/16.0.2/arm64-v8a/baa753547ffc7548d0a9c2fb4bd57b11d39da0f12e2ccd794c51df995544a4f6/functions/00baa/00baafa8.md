# 00baafa8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baaf0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baaf0c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-45c34439d7d8b85166642b8e6945e31d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00babf9c`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bab/00babf9c.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0009.md#compare-31f091f93a7b25b7aaea198013cc0238)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baafa8",
  "name": "FUN_00baafa8",
  "size": 2332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "653b771484036286579e6c3f036ba0c382ae54dd4dafe4f3a2d65ec8d7ddc40a",
  "source_text_sha256": "653b771484036286579e6c3f036ba0c382ae54dd4dafe4f3a2d65ec8d7ddc40a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baafa8",
        "00bab8c3"
      ]
    ],
    "bytes_sha256": "bf5e23abeb34293fb946588dcf1a5b842e223717aa8057012382c50321098c21",
    "instruction_count": 583,
    "instruction_bytes": 2332,
    "body_bytes": 2332,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b7fed8](../00b7f/00b7fed8.md)
- [00b802b4](../00b80/00b802b4.md)

## 呼び出し先

- [00c57fb0](../00c57/00c57fb0.md)
- [00c58680](../00c58/00c58680.md)
- [00c58690](../00c58/00c58690.md)
- [00c5c280](../00c5c/00c5c280.md)
- [00c5c290](../00c5c/00c5c290.md)
- [00c5d220](../00c5d/00c5d220.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 18300 bytes

~~~c

void FUN_00baafa8(byte **param_1,byte **param_2,long param_3)

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
  
                    /* try { // try from 00baafbc to 00caafc7 has its CatchHandler @ 00babd50 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00baafdc to 00caafe7 has its CatchHandler @ 00babd4c */
  switch(*(undefined4 *)(param_3 + 0xa0)) {
  case 0:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab008 to 00cab013 has its CatchHandler @ 00babd0c */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) goto LAB_00bab3d8;
                    /* try { // try from 00bab02c to 00cab037 has its CatchHandler @ 00babccc */
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
LAB_00bab408:
                    /* try { // try from 00bab414 to 00cab41f has its CatchHandler @ 00baba80 */
      iVar6 = 10;
      goto LAB_00bab41c;
    }
    goto LAB_00bab258;
  case 1:
                    /* try { // try from 00bab254 to 00cab263 has its CatchHandler @ 00bab9d8 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab3a4 to 00cab3af has its CatchHandler @ 00bababc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab3d8;
                    /* try { // try from 00bab3c8 to 00cab3d3 has its CatchHandler @ 00babab8 */
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00bab408;
    }
    goto LAB_00bab258;
  case 2:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab1e0 to 00cab24f has its CatchHandler @ 00bac0a0 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab3d8;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00bab408;
    }
    goto LAB_00bab258;
  case 3:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab324 to 00cab32f has its CatchHandler @ 00babb3c */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bab338 to 00cab33b has its CatchHandler @ 00babb1c */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab558 to 00cab577 has its CatchHandler @ 00babe4c */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bab578 to 00cab5e7 has its CatchHandler @ 00bac09c */
              goto LAB_00bab594;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab594:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
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
                    /* try { // try from 00bab828 to 00cab833 has its CatchHandler @ 00baba20 */
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
                    /* try { // try from 00bab0c8 to 00cab0d3 has its CatchHandler @ 00babc5c */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab3d8;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00bab0f4 to 00cab0ff has its CatchHandler @ 00babc10 */
        } while (bVar9 != 0);
      }
      goto LAB_00bab408;
    }
LAB_00bab258:
    uVar13 = 0;
joined_r0x00bab450:
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(byte *)param_2;
    }
                    /* try { // try from 00bab464 to 00cab46f has its CatchHandler @ 00baba6c */
    bVar3 = (uVar13 & 0xff) <= (uVar14 & 0xff);
LAB_00bab468:
    bVar3 = !bVar3;
    break;
  case 5:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab490 to 00cab49b has its CatchHandler @ 00baba44 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bab4b4 to 00cab4bf has its CatchHandler @ 00baba40 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab698 to 00cab6a3 has its CatchHandler @ 00babb18 */
              iVar6 = 0x10;
              goto LAB_00bab6b8;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab6b8:
      local_40 = pbVar15;
                    /* try { // try from 00bab6bc to 00cab6c7 has its CatchHandler @ 00babb14 */
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
      uVar11 = 0;
                    /* try { // try from 00bab6d0 to 00cab6d3 has its CatchHandler @ 00babaf4 */
      if ((local_40 != pbVar15) && (*local_40 == 0)) {
        if (lVar5 < 0x8000) {
                    /* try { // try from 00bab84c to 00cab857 has its CatchHandler @ 00baba1c */
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
                    /* try { // try from 00bab4e0 to 00cab4eb has its CatchHandler @ 00baba30 */
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab710 to 00cab71b has its CatchHandler @ 00babacc */
              iVar6 = 0x10;
              goto LAB_00bab738;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
                    /* try { // try from 00bab504 to 00cab50f has its CatchHandler @ 00baba08 */
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab738:
      local_40 = pbVar15;
                    /* try { // try from 00bab73c to 00cab747 has its CatchHandler @ 00baba98 */
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
      uVar13 = 0;
                    /* try { // try from 00bab760 to 00cab76b has its CatchHandler @ 00baba94 */
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
    goto LAB_00bab468;
  case 7:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab358 to 00cab363 has its CatchHandler @ 00babae4 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bab378 to 00cab383 has its CatchHandler @ 00babae0 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab5ec to 00cab5fb has its CatchHandler @ 00bab9d0 */
              iVar6 = 0x10;
                    /* try { // try from 00bab5fc to 00cab60f has its CatchHandler @ 00bab9cc */
              goto LAB_00bab614;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab614:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
      fVar18 = 0.0;
                    /* try { // try from 00bab650 to 00cab66b has its CatchHandler @ 00babeb4 */
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
                    /* try { // try from 00bab530 to 00cab53b has its CatchHandler @ 00bab9f8 */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab78c to 00cab797 has its CatchHandler @ 00baba84 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab7ac to 00cab7b7 has its CatchHandler @ 00baba68 */
              iVar6 = 0x10;
              goto LAB_00bab7cc;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab7cc:
      local_40 = pbVar15;
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
                    /* try { // try from 00bab7d8 to 00cab7e3 has its CatchHandler @ 00baba58 */
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
    goto LAB_00bab468;
  case 9:
    local_40 = (byte *)0x0;
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab118 to 00cab123 has its CatchHandler @ 00babc0c */
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
                    /* try { // try from 00bab144 to 00cab14f has its CatchHandler @ 00babbc0 */
    bVar3 = (long)*param_1 < (long)*param_2;
    break;
  case 10:
    local_40 = (byte *)0x0;
                    /* try { // try from 00bab2b8 to 00cab2d3 has its CatchHandler @ 00babeb8 */
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
                    /* try { // try from 00bab300 to 00cab30b has its CatchHandler @ 00babb40 */
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
                    /* try { // try from 00bab89c to 00cab8a7 has its CatchHandler @ 00bab9f0 */
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
    bVar3 = *param_2 <= *param_1;
    goto LAB_00bab468;
  case 0xb:
    if ((param_1 == (byte **)0x0) || (fVar18 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab058 to 00cab063 has its CatchHandler @ 00babcbc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      fVar16 = strtof((char *)pbVar15,(char **)&local_40);
      fVar18 = 0.0;
                    /* try { // try from 00bab078 to 00cab083 has its CatchHandler @ 00babc7c */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = fVar16, NAN(fVar16))) {
        fVar18 = NAN;
      }
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
                    /* try { // try from 00bab0a4 to 00cab0af has its CatchHandler @ 00babc6c */
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = fVar16 < fVar18;
    break;
  case 0xc:
    if ((param_1 == (byte **)0x0) || (dVar19 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab168 to 00cab173 has its CatchHandler @ 00babbbc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      dVar17 = strtod((char *)pbVar15,(char **)&local_40);
      dVar19 = 0.0;
                    /* try { // try from 00bab194 to 00cab19f has its CatchHandler @ 00babb70 */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (dVar19 = dVar17, NAN(dVar17))) {
        dVar19 = NAN;
      }
    }
                    /* try { // try from 00bab1b4 to 00cab1bf has its CatchHandler @ 00babb6c */
    dVar17 = dVar19;
    if (param_1 != (byte **)0x0) {
      dVar17 = (double)*param_1;
    }
    if (param_2 != (byte **)0x0) {
                    /* try { // try from 00bab1c0 to 00cab1df has its CatchHandler @ 00babecc */
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
LAB_00bab3d8:
  if ((uVar13 != 0x30) || ((pbVar15[lVar8] & 0xdf) != 0x58)) goto LAB_00bab408;
                    /* try { // try from 00bab3f4 to 00cab3ff has its CatchHandler @ 00babaa8 */
  iVar6 = 0x10;
LAB_00bab41c:
  local_40 = pbVar15;
  uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                    *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b900);
  uVar13 = 0;
                    /* try { // try from 00bab440 to 00cab44b has its CatchHandler @ 00baba70 */
  if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfe < uVar4)) {
    uVar13 = 0xff;
  }
  goto joined_r0x00bab450;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baafa8"></a> `00baafa8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baafac"></a> `00baafac` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baafb0"></a> `00baafb0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baafb4"></a> `00baafb4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baafb8"></a> `00baafb8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baafbc"></a> `00baafbc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baafc0"></a> `00baafc0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00baafc4"></a> `00baafc4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baafc8"></a> `00baafc8` | `48 a0 40 b9` | ldr w8,[x2, #0xa0] | `FALL_THROUGH`
<a id="insn-00baafcc"></a> `00baafcc` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00baafd0"></a> `00baafd0` | `c8 13 00 54` | b.hi 0x00bab248 | `CONDITIONAL_JUMP`
<a id="insn-00baafd4"></a> `00baafd4` | `29 bb ff 90` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `29 cd 08 91` | add x9,x9,#0x233 | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `ca 00 00 10` | adr x10,0xbaaff4 | `FALL_THROUGH`
<a id="insn-00baafe0"></a> `00baafe0` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baafe4"></a> `00baafe4` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00baafe8"></a> `00baafe8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baafec"></a> `00baafec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00baaff4"></a> `00baaff4` | `54 00 00 b4` | cbz x20,0x00baaffc | `CONDITIONAL_JUMP`
<a id="insn-00baaff8"></a> `00baaff8` | `13 13 00 b5` | cbnz x19,0x00bab258 | `CONDITIONAL_JUMP`
<a id="insn-00baaffc"></a> `00baaffc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab00c"></a> `00bab00c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `a9 1f 00 34` | cbz w9,0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab018"></a> `00bab018` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab028"></a> `00bab028` | `83 1d 00 54` | b.cc 0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab02c"></a> `00bab02c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab030"></a> `00bab030` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab034"></a> `00bab034` | `49 ff ff 35` | cbnz w9,0x00bab01c | `CONDITIONAL_JUMP`
<a id="insn-00bab038"></a> `00bab038` | `f4 00 00 14` | b 0x00bab408 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab03c"></a> `00bab03c` | `74 00 00 b4` | cbz x20,0x00bab048 | `CONDITIONAL_JUMP`
<a id="insn-00bab040"></a> `00bab040` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00bab044"></a> `00bab044` | `b3 02 00 b5` | cbnz x19,0x00bab098 | `CONDITIONAL_JUMP`
<a id="insn-00bab048"></a> `00bab048` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab04c"></a> `00bab04c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab050"></a> `00bab050` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab054"></a> `00bab054` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab058"></a> `00bab058` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab05c"></a> `00bab05c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab060"></a> `00bab060` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab064"></a> `00bab064` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab068"></a> `00bab068` | `86 b5 02 94` | bl 0x00c58680 | `UNCONDITIONAL_CALL`
<a id="insn-00bab06c"></a> `00bab06c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab070"></a> `00bab070` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00bab074"></a> `00bab074` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab078"></a> `00bab078` | `00 01 00 54` | b.eq 0x00bab098 | `CONDITIONAL_JUMP`
<a id="insn-00bab07c"></a> `00bab07c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab080"></a> `00bab080` | `c8 00 00 35` | cbnz w8,0x00bab098 | `CONDITIONAL_JUMP`
<a id="insn-00bab084"></a> `00bab084` | `00 20 20 1e` | fcmp s0,s0 | `FALL_THROUGH`
<a id="insn-00bab088"></a> `00bab088` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00bab08c"></a> `00bab08c` | `67 00 00 54` | b.vc 0x00bab098 | `CONDITIONAL_JUMP`
<a id="insn-00bab090"></a> `00bab090` | `08 f8 af 52` | mov w8,#0x7fc00000 | `FALL_THROUGH`
<a id="insn-00bab094"></a> `00bab094` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00bab098"></a> `00bab098` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bab09c"></a> `00bab09c` | `54 00 00 b4` | cbz x20,0x00bab0a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab0a0"></a> `00bab0a0` | `80 02 40 bd` | ldr s0,[x20] | `FALL_THROUGH`
<a id="insn-00bab0a4"></a> `00bab0a4` | `53 00 00 b4` | cbz x19,0x00bab0ac | `CONDITIONAL_JUMP`
<a id="insn-00bab0a8"></a> `00bab0a8` | `61 02 40 bd` | ldr s1,[x19] | `FALL_THROUGH`
<a id="insn-00bab0ac"></a> `00bab0ac` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bab0b0"></a> `00bab0b0` | `46 00 00 14` | b 0x00bab1c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab0b4"></a> `00bab0b4` | `54 00 00 b4` | cbz x20,0x00bab0bc | `CONDITIONAL_JUMP`
<a id="insn-00bab0b8"></a> `00bab0b8` | `13 0d 00 b5` | cbnz x19,0x00bab258 | `CONDITIONAL_JUMP`
<a id="insn-00bab0bc"></a> `00bab0bc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab0c0"></a> `00bab0c0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab0c4"></a> `00bab0c4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab0c8"></a> `00bab0c8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab0cc"></a> `00bab0cc` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab0d0"></a> `00bab0d0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab0d4"></a> `00bab0d4` | `a9 19 00 34` | cbz w9,0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab0d8"></a> `00bab0d8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab0dc"></a> `00bab0dc` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab0e0"></a> `00bab0e0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab0e4"></a> `00bab0e4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab0e8"></a> `00bab0e8` | `83 17 00 54` | b.cc 0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab0ec"></a> `00bab0ec` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab0f0"></a> `00bab0f0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab0f4"></a> `00bab0f4` | `49 ff ff 35` | cbnz w9,0x00bab0dc | `CONDITIONAL_JUMP`
<a id="insn-00bab0f8"></a> `00bab0f8` | `c4 00 00 14` | b 0x00bab408 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab0fc"></a> `00bab0fc` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bab100"></a> `00bab100` | `54 00 00 b4` | cbz x20,0x00bab108 | `CONDITIONAL_JUMP`
<a id="insn-00bab104"></a> `00bab104` | `53 01 00 b5` | cbnz x19,0x00bab12c | `CONDITIONAL_JUMP`
<a id="insn-00bab108"></a> `00bab108` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab10c"></a> `00bab10c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab110"></a> `00bab110` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab114"></a> `00bab114` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab118"></a> `00bab118` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab11c"></a> `00bab11c` | `41 01 89 9a` | csel x1,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab120"></a> `00bab120` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bab124"></a> `00bab124` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bab128"></a> `00bab128` | `56 c4 02 94` | bl 0x00c5c280 | `UNCONDITIONAL_CALL`
<a id="insn-00bab12c"></a> `00bab12c` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bab130"></a> `00bab130` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab134"></a> `00bab134` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bab138"></a> `00bab138` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bab13c"></a> `00bab13c` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bab140"></a> `00bab140` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bab144"></a> `00bab144` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab148"></a> `00bab148` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab14c"></a> `00bab14c` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab150"></a> `00bab150` | `c7 00 00 14` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab154"></a> `00bab154` | `74 00 00 b4` | cbz x20,0x00bab160 | `CONDITIONAL_JUMP`
<a id="insn-00bab158"></a> `00bab158` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bab15c"></a> `00bab15c` | `b3 02 00 b5` | cbnz x19,0x00bab1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab160"></a> `00bab160` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab164"></a> `00bab164` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab168"></a> `00bab168` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab16c"></a> `00bab16c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab170"></a> `00bab170` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab174"></a> `00bab174` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab178"></a> `00bab178` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab17c"></a> `00bab17c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab180"></a> `00bab180` | `44 b5 02 94` | bl 0x00c58690 | `UNCONDITIONAL_CALL`
<a id="insn-00bab184"></a> `00bab184` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab188"></a> `00bab188` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bab18c"></a> `00bab18c` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab190"></a> `00bab190` | `00 01 00 54` | b.eq 0x00bab1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab194"></a> `00bab194` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab198"></a> `00bab198` | `c8 00 00 35` | cbnz w8,0x00bab1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab19c"></a> `00bab19c` | `00 20 60 1e` | fcmp d0,d0 | `FALL_THROUGH`
<a id="insn-00bab1a0"></a> `00bab1a0` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00bab1a4"></a> `00bab1a4` | `67 00 00 54` | b.vc 0x00bab1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1a8"></a> `00bab1a8` | `08 ff ef d2` | mov x8,#0x7ff8000000000000 | `FALL_THROUGH`
<a id="insn-00bab1ac"></a> `00bab1ac` | `01 01 67 9e` | fmov d1,x8 | `FALL_THROUGH`
<a id="insn-00bab1b0"></a> `00bab1b0` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bab1b4"></a> `00bab1b4` | `54 00 00 b4` | cbz x20,0x00bab1bc | `CONDITIONAL_JUMP`
<a id="insn-00bab1b8"></a> `00bab1b8` | `80 02 40 fd` | ldr d0,[x20] | `FALL_THROUGH`
<a id="insn-00bab1bc"></a> `00bab1bc` | `53 00 00 b4` | cbz x19,0x00bab1c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab1c0"></a> `00bab1c0` | `61 02 40 fd` | ldr d1,[x19] | `FALL_THROUGH`
<a id="insn-00bab1c4"></a> `00bab1c4` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00bab1c8"></a> `00bab1c8` | `e0 57 9f 1a` | cset w0,mi | `FALL_THROUGH`
<a id="insn-00bab1cc"></a> `00bab1cc` | `a8 00 00 14` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1d0"></a> `00bab1d0` | `54 00 00 b4` | cbz x20,0x00bab1d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab1d4"></a> `00bab1d4` | `33 04 00 b5` | cbnz x19,0x00bab258 | `CONDITIONAL_JUMP`
<a id="insn-00bab1d8"></a> `00bab1d8` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab1dc"></a> `00bab1dc` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab1e0"></a> `00bab1e0` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab1e4"></a> `00bab1e4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab1e8"></a> `00bab1e8` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab1ec"></a> `00bab1ec` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab1f0"></a> `00bab1f0` | `c9 10 00 34` | cbz w9,0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab1f4"></a> `00bab1f4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab1f8"></a> `00bab1f8` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab1fc"></a> `00bab1fc` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab200"></a> `00bab200` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab204"></a> `00bab204` | `a3 0e 00 54` | b.cc 0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab208"></a> `00bab208` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab20c"></a> `00bab20c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab210"></a> `00bab210` | `49 ff ff 35` | cbnz w9,0x00bab1f8 | `CONDITIONAL_JUMP`
<a id="insn-00bab214"></a> `00bab214` | `7d 00 00 14` | b 0x00bab408 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab218"></a> `00bab218` | `14 08 00 b4` | cbz x20,0x00bab318 | `CONDITIONAL_JUMP`
<a id="insn-00bab21c"></a> `00bab21c` | `f3 07 00 b4` | cbz x19,0x00bab318 | `CONDITIONAL_JUMP`
<a id="insn-00bab220"></a> `00bab220` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab224"></a> `00bab224` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab228"></a> `00bab228` | `34 30 00 b5` | cbnz x20,0x00bab82c | `CONDITIONAL_JUMP`
<a id="insn-00bab22c"></a> `00bab22c` | `81 01 00 14` | b 0x00bab830 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab230"></a> `00bab230` | `54 09 00 b4` | cbz x20,0x00bab358 | `CONDITIONAL_JUMP`
<a id="insn-00bab234"></a> `00bab234` | `33 09 00 b4` | cbz x19,0x00bab358 | `CONDITIONAL_JUMP`
<a id="insn-00bab238"></a> `00bab238` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab23c"></a> `00bab23c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab240"></a> `00bab240` | `f4 20 00 b5` | cbnz x20,0x00bab65c | `CONDITIONAL_JUMP`
<a id="insn-00bab244"></a> `00bab244` | `07 01 00 14` | b 0x00bab660 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab248"></a> `00bab248` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bab24c"></a> `00bab24c` | `88 00 00 14` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab250"></a> `00bab250` | `54 0a 00 b4` | cbz x20,0x00bab398 | `CONDITIONAL_JUMP`
<a id="insn-00bab254"></a> `00bab254` | `33 0a 00 b4` | cbz x19,0x00bab398 | `CONDITIONAL_JUMP`
<a id="insn-00bab258"></a> `00bab258` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab25c"></a> `00bab25c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab260"></a> `00bab260` | `b4 0f 00 b5` | cbnz x20,0x00bab454 | `CONDITIONAL_JUMP`
<a id="insn-00bab264"></a> `00bab264` | `7d 00 00 14` | b 0x00bab458 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab268"></a> `00bab268` | `54 11 00 b4` | cbz x20,0x00bab490 | `CONDITIONAL_JUMP`
<a id="insn-00bab26c"></a> `00bab26c` | `33 11 00 b4` | cbz x19,0x00bab490 | `CONDITIONAL_JUMP`
<a id="insn-00bab270"></a> `00bab270` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab274"></a> `00bab274` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab278"></a> `00bab278` | `34 2f 00 b5` | cbnz x20,0x00bab85c | `CONDITIONAL_JUMP`
<a id="insn-00bab27c"></a> `00bab27c` | `79 01 00 14` | b 0x00bab860 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab280"></a> `00bab280` | `94 12 00 b4` | cbz x20,0x00bab4d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab284"></a> `00bab284` | `73 12 00 b4` | cbz x19,0x00bab4d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab288"></a> `00bab288` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab28c"></a> `00bab28c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab290"></a> `00bab290` | `14 27 00 b5` | cbnz x20,0x00bab770 | `CONDITIONAL_JUMP`
<a id="insn-00bab294"></a> `00bab294` | `38 01 00 14` | b 0x00bab774 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab298"></a> `00bab298` | `d4 13 00 b4` | cbz x20,0x00bab510 | `CONDITIONAL_JUMP`
<a id="insn-00bab29c"></a> `00bab29c` | `b3 13 00 b4` | cbz x19,0x00bab510 | `CONDITIONAL_JUMP`
<a id="insn-00bab2a0"></a> `00bab2a0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab2a4"></a> `00bab2a4` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab2a8"></a> `00bab2a8` | `f4 2a 00 b5` | cbnz x20,0x00bab804 | `CONDITIONAL_JUMP`
<a id="insn-00bab2ac"></a> `00bab2ac` | `57 01 00 14` | b 0x00bab808 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab2b0"></a> `00bab2b0` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bab2b4"></a> `00bab2b4` | `54 00 00 b4` | cbz x20,0x00bab2bc | `CONDITIONAL_JUMP`
<a id="insn-00bab2b8"></a> `00bab2b8` | `33 2f 00 b5` | cbnz x19,0x00bab89c | `CONDITIONAL_JUMP`
<a id="insn-00bab2bc"></a> `00bab2bc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab2c0"></a> `00bab2c0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab2c4"></a> `00bab2c4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab2c8"></a> `00bab2c8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab2cc"></a> `00bab2cc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2d0"></a> `00bab2d0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab2d4"></a> `00bab2d4` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2d8"></a> `00bab2d8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bab2dc"></a> `00bab2dc` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bab2e0"></a> `00bab2e0` | `ec c3 02 94` | bl 0x00c5c290 | `UNCONDITIONAL_CALL`
<a id="insn-00bab2e4"></a> `00bab2e4` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab2e8"></a> `00bab2e8` | `a8 2d 00 b4` | cbz x8,0x00bab89c | `CONDITIONAL_JUMP`
<a id="insn-00bab2ec"></a> `00bab2ec` | `80 2d 00 36` | tbz w0,#0x0,0x00bab89c | `CONDITIONAL_JUMP`
<a id="insn-00bab2f0"></a> `00bab2f0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab2f4"></a> `00bab2f4` | `29 2c 00 34` | cbz w9,0x00bab878 | `CONDITIONAL_JUMP`
<a id="insn-00bab2f8"></a> `00bab2f8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bab2fc"></a> `00bab2fc` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab300"></a> `00bab300` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab304"></a> `00bab304` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bab308"></a> `00bab308` | `a3 2b 00 54` | b.cc 0x00bab87c | `CONDITIONAL_JUMP`
<a id="insn-00bab30c"></a> `00bab30c` | `09 1d 40 38` | ldrb w9,[x8, #0x1]! | `FALL_THROUGH`
<a id="insn-00bab310"></a> `00bab310` | `69 ff ff 35` | cbnz w9,0x00bab2fc | `CONDITIONAL_JUMP`
<a id="insn-00bab314"></a> `00bab314` | `5a 01 00 14` | b 0x00bab87c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab318"></a> `00bab318` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab31c"></a> `00bab31c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab320"></a> `00bab320` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab324"></a> `00bab324` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab328"></a> `00bab328` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab32c"></a> `00bab32c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab330"></a> `00bab330` | `89 12 00 34` | cbz w9,0x00bab580 | `CONDITIONAL_JUMP`
<a id="insn-00bab334"></a> `00bab334` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab338"></a> `00bab338` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab33c"></a> `00bab33c` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab340"></a> `00bab340` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab344"></a> `00bab344` | `63 10 00 54` | b.cc 0x00bab550 | `CONDITIONAL_JUMP`
<a id="insn-00bab348"></a> `00bab348` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab34c"></a> `00bab34c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab350"></a> `00bab350` | `49 ff ff 35` | cbnz w9,0x00bab338 | `CONDITIONAL_JUMP`
<a id="insn-00bab354"></a> `00bab354` | `8b 00 00 14` | b 0x00bab580 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab358"></a> `00bab358` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab35c"></a> `00bab35c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab360"></a> `00bab360` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab364"></a> `00bab364` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab368"></a> `00bab368` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab36c"></a> `00bab36c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab370"></a> `00bab370` | `89 14 00 34` | cbz w9,0x00bab600 | `CONDITIONAL_JUMP`
<a id="insn-00bab374"></a> `00bab374` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab378"></a> `00bab378` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab37c"></a> `00bab37c` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab380"></a> `00bab380` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab384"></a> `00bab384` | `63 12 00 54` | b.cc 0x00bab5d0 | `CONDITIONAL_JUMP`
<a id="insn-00bab388"></a> `00bab388` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab38c"></a> `00bab38c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab390"></a> `00bab390` | `49 ff ff 35` | cbnz w9,0x00bab378 | `CONDITIONAL_JUMP`
<a id="insn-00bab394"></a> `00bab394` | `9b 00 00 14` | b 0x00bab600 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab398"></a> `00bab398` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab39c"></a> `00bab39c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab3a0"></a> `00bab3a0` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab3a4"></a> `00bab3a4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3a8"></a> `00bab3a8` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab3ac"></a> `00bab3ac` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab3b0"></a> `00bab3b0` | `c9 02 00 34` | cbz w9,0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab3b4"></a> `00bab3b4` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3b8"></a> `00bab3b8` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab3bc"></a> `00bab3bc` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab3c0"></a> `00bab3c0` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab3c4"></a> `00bab3c4` | `a3 00 00 54` | b.cc 0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab3c8"></a> `00bab3c8` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab3cc"></a> `00bab3cc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3d0"></a> `00bab3d0` | `49 ff ff 35` | cbnz w9,0x00bab3b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab3d4"></a> `00bab3d4` | `0d 00 00 14` | b 0x00bab408 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab3d8"></a> `00bab3d8` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab3dc"></a> `00bab3dc` | `61 01 00 54` | b.ne 0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab3e0"></a> `00bab3e0` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab3e4"></a> `00bab3e4` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab3e8"></a> `00bab3e8` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab3ec"></a> `00bab3ec` | `e1 00 00 54` | b.ne 0x00bab408 | `CONDITIONAL_JUMP`
<a id="insn-00bab3f0"></a> `00bab3f0` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab3f4"></a> `00bab3f4` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab3f8"></a> `00bab3f8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab3fc"></a> `00bab3fc` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab400"></a> `00bab400` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab404"></a> `00bab404` | `06 00 00 14` | b 0x00bab41c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab408"></a> `00bab408` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab40c"></a> `00bab40c` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab410"></a> `00bab410` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab414"></a> `00bab414` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab418"></a> `00bab418` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab41c"></a> `00bab41c` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab420"></a> `00bab420` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab424"></a> `00bab424` | `7f c7 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab428"></a> `00bab428` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab42c"></a> `00bab42c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab430"></a> `00bab430` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab434"></a> `00bab434` | `c0 00 00 54` | b.eq 0x00bab44c | `CONDITIONAL_JUMP`
<a id="insn-00bab438"></a> `00bab438` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab43c"></a> `00bab43c` | `89 00 00 35` | cbnz w9,0x00bab44c | `CONDITIONAL_JUMP`
<a id="insn-00bab440"></a> `00bab440` | `1f fc 03 f1` | cmp x0,#0xff | `FALL_THROUGH`
<a id="insn-00bab444"></a> `00bab444` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00bab448"></a> `00bab448` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bab44c"></a> `00bab44c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab450"></a> `00bab450` | `54 00 00 b4` | cbz x20,0x00bab458 | `CONDITIONAL_JUMP`
<a id="insn-00bab454"></a> `00bab454` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab458"></a> `00bab458` | `53 00 00 b4` | cbz x19,0x00bab460 | `CONDITIONAL_JUMP`
<a id="insn-00bab45c"></a> `00bab45c` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab460"></a> `00bab460` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab464"></a> `00bab464` | `3f 01 28 6b` | cmp w9,w8, UXTB  | `FALL_THROUGH`
<a id="insn-00bab468"></a> `00bab468` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00bab46c"></a> `00bab46c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bab470"></a> `00bab470` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab474"></a> `00bab474` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bab478"></a> `00bab478` | `41 22 00 54` | b.ne 0x00bab8c0 | `CONDITIONAL_JUMP`
<a id="insn-00bab47c"></a> `00bab47c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab480"></a> `00bab480` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab484"></a> `00bab484` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab488"></a> `00bab488` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bab48c"></a> `00bab48c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bab490"></a> `00bab490` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab494"></a> `00bab494` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab498"></a> `00bab498` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab49c"></a> `00bab49c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4a0"></a> `00bab4a0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab4a4"></a> `00bab4a4` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab4a8"></a> `00bab4a8` | `e9 0f 00 34` | cbz w9,0x00bab6a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab4ac"></a> `00bab4ac` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4b0"></a> `00bab4b0` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab4b4"></a> `00bab4b4` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab4b8"></a> `00bab4b8` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab4bc"></a> `00bab4bc` | `c3 0d 00 54` | b.cc 0x00bab674 | `CONDITIONAL_JUMP`
<a id="insn-00bab4c0"></a> `00bab4c0` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab4c4"></a> `00bab4c4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4c8"></a> `00bab4c8` | `49 ff ff 35` | cbnz w9,0x00bab4b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab4cc"></a> `00bab4cc` | `76 00 00 14` | b 0x00bab6a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab4d0"></a> `00bab4d0` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab4d4"></a> `00bab4d4` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab4d8"></a> `00bab4d8` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab4dc"></a> `00bab4dc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4e0"></a> `00bab4e0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab4e4"></a> `00bab4e4` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab4e8"></a> `00bab4e8` | `e9 11 00 34` | cbz w9,0x00bab724 | `CONDITIONAL_JUMP`
<a id="insn-00bab4ec"></a> `00bab4ec` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4f0"></a> `00bab4f0` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab4f4"></a> `00bab4f4` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab4f8"></a> `00bab4f8` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab4fc"></a> `00bab4fc` | `c3 0f 00 54` | b.cc 0x00bab6f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab500"></a> `00bab500` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab504"></a> `00bab504` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab508"></a> `00bab508` | `49 ff ff 35` | cbnz w9,0x00bab4f0 | `CONDITIONAL_JUMP`
<a id="insn-00bab50c"></a> `00bab50c` | `86 00 00 14` | b 0x00bab724 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab510"></a> `00bab510` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab514"></a> `00bab514` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab518"></a> `00bab518` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab51c"></a> `00bab51c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab520"></a> `00bab520` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab524"></a> `00bab524` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab528"></a> `00bab528` | `89 14 00 34` | cbz w9,0x00bab7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab52c"></a> `00bab52c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab530"></a> `00bab530` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab534"></a> `00bab534` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab538"></a> `00bab538` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab53c"></a> `00bab53c` | `63 12 00 54` | b.cc 0x00bab788 | `CONDITIONAL_JUMP`
<a id="insn-00bab540"></a> `00bab540` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab544"></a> `00bab544` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab548"></a> `00bab548` | `49 ff ff 35` | cbnz w9,0x00bab530 | `CONDITIONAL_JUMP`
<a id="insn-00bab54c"></a> `00bab54c` | `9b 00 00 14` | b 0x00bab7b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab550"></a> `00bab550` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab554"></a> `00bab554` | `61 01 00 54` | b.ne 0x00bab580 | `CONDITIONAL_JUMP`
<a id="insn-00bab558"></a> `00bab558` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab55c"></a> `00bab55c` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab560"></a> `00bab560` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab564"></a> `00bab564` | `e1 00 00 54` | b.ne 0x00bab580 | `CONDITIONAL_JUMP`
<a id="insn-00bab568"></a> `00bab568` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab56c"></a> `00bab56c` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab570"></a> `00bab570` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab574"></a> `00bab574` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab578"></a> `00bab578` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab57c"></a> `00bab57c` | `06 00 00 14` | b 0x00bab594 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab580"></a> `00bab580` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab584"></a> `00bab584` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab588"></a> `00bab588` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab58c"></a> `00bab58c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab590"></a> `00bab590` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab594"></a> `00bab594` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab598"></a> `00bab598` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab59c"></a> `00bab59c` | `21 c7 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab5a0"></a> `00bab5a0` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab5a4"></a> `00bab5a4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab5a8"></a> `00bab5a8` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab5ac"></a> `00bab5ac` | `c0 13 00 54` | b.eq 0x00bab824 | `CONDITIONAL_JUMP`
<a id="insn-00bab5b0"></a> `00bab5b0` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab5b4"></a> `00bab5b4` | `89 13 00 35` | cbnz w9,0x00bab824 | `CONDITIONAL_JUMP`
<a id="insn-00bab5b8"></a> `00bab5b8` | `1f fc 01 f1` | cmp x0,#0x7f | `FALL_THROUGH`
<a id="insn-00bab5bc"></a> `00bab5bc` | `ed 12 00 54` | b.le 0x00bab818 | `CONDITIONAL_JUMP`
<a id="insn-00bab5c0"></a> `00bab5c0` | `e8 0f 80 52` | mov w8,#0x7f | `FALL_THROUGH`
<a id="insn-00bab5c4"></a> `00bab5c4` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab5c8"></a> `00bab5c8` | `34 13 00 b5` | cbnz x20,0x00bab82c | `CONDITIONAL_JUMP`
<a id="insn-00bab5cc"></a> `00bab5cc` | `99 00 00 14` | b 0x00bab830 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab5d0"></a> `00bab5d0` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab5d4"></a> `00bab5d4` | `61 01 00 54` | b.ne 0x00bab600 | `CONDITIONAL_JUMP`
<a id="insn-00bab5d8"></a> `00bab5d8` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab5dc"></a> `00bab5dc` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab5e0"></a> `00bab5e0` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab5e4"></a> `00bab5e4` | `e1 00 00 54` | b.ne 0x00bab600 | `CONDITIONAL_JUMP`
<a id="insn-00bab5e8"></a> `00bab5e8` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab5ec"></a> `00bab5ec` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab5f0"></a> `00bab5f0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab5f4"></a> `00bab5f4` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab5f8"></a> `00bab5f8` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab5fc"></a> `00bab5fc` | `06 00 00 14` | b 0x00bab614 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab600"></a> `00bab600` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab604"></a> `00bab604` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab608"></a> `00bab608` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab60c"></a> `00bab60c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab610"></a> `00bab610` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab614"></a> `00bab614` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab618"></a> `00bab618` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab61c"></a> `00bab61c` | `01 c7 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab620"></a> `00bab620` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab624"></a> `00bab624` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab628"></a> `00bab628` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab62c"></a> `00bab62c` | `40 01 00 54` | b.eq 0x00bab654 | `CONDITIONAL_JUMP`
<a id="insn-00bab630"></a> `00bab630` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab634"></a> `00bab634` | `09 01 00 35` | cbnz w9,0x00bab654 | `CONDITIONAL_JUMP`
<a id="insn-00bab638"></a> `00bab638` | `08 00 b0 12` | mov w8,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00bab63c"></a> `00bab63c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab640"></a> `00bab640` | `ac 00 00 54` | b.gt 0x00bab654 | `CONDITIONAL_JUMP`
<a id="insn-00bab644"></a> `00bab644` | `e8 83 61 b2` | orr x8,xzr,#-0x80000000 | `FALL_THROUGH`
<a id="insn-00bab648"></a> `00bab648` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab64c"></a> `00bab64c` | `08 00 b0 52` | mov w8,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bab650"></a> `00bab650` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab654"></a> `00bab654` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab658"></a> `00bab658` | `54 00 00 b4` | cbz x20,0x00bab660 | `CONDITIONAL_JUMP`
<a id="insn-00bab65c"></a> `00bab65c` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab660"></a> `00bab660` | `53 00 00 b4` | cbz x19,0x00bab668 | `CONDITIONAL_JUMP`
<a id="insn-00bab664"></a> `00bab664` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab668"></a> `00bab668` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab66c"></a> `00bab66c` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab670"></a> `00bab670` | `7f ff ff 17` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab674"></a> `00bab674` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab678"></a> `00bab678` | `61 01 00 54` | b.ne 0x00bab6a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab67c"></a> `00bab67c` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab680"></a> `00bab680` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab684"></a> `00bab684` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab688"></a> `00bab688` | `e1 00 00 54` | b.ne 0x00bab6a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab68c"></a> `00bab68c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab690"></a> `00bab690` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab694"></a> `00bab694` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab698"></a> `00bab698` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab69c"></a> `00bab69c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab6a0"></a> `00bab6a0` | `06 00 00 14` | b 0x00bab6b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6a4"></a> `00bab6a4` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab6a8"></a> `00bab6a8` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab6ac"></a> `00bab6ac` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab6b0"></a> `00bab6b0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab6b4"></a> `00bab6b4` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab6b8"></a> `00bab6b8` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab6bc"></a> `00bab6bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab6c0"></a> `00bab6c0` | `d8 c6 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab6c4"></a> `00bab6c4` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab6c8"></a> `00bab6c8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab6cc"></a> `00bab6cc` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab6d0"></a> `00bab6d0` | `20 0c 00 54` | b.eq 0x00bab854 | `CONDITIONAL_JUMP`
<a id="insn-00bab6d4"></a> `00bab6d4` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab6d8"></a> `00bab6d8` | `e9 0b 00 35` | cbnz w9,0x00bab854 | `CONDITIONAL_JUMP`
<a id="insn-00bab6dc"></a> `00bab6dc` | `1f 20 40 f1` | cmp x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab6e0"></a> `00bab6e0` | `4b 0b 00 54` | b.lt 0x00bab848 | `CONDITIONAL_JUMP`
<a id="insn-00bab6e4"></a> `00bab6e4` | `e8 ff 8f 52` | mov w8,#0x7fff | `FALL_THROUGH`
<a id="insn-00bab6e8"></a> `00bab6e8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab6ec"></a> `00bab6ec` | `94 0b 00 b5` | cbnz x20,0x00bab85c | `CONDITIONAL_JUMP`
<a id="insn-00bab6f0"></a> `00bab6f0` | `5c 00 00 14` | b 0x00bab860 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6f4"></a> `00bab6f4` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab6f8"></a> `00bab6f8` | `61 01 00 54` | b.ne 0x00bab724 | `CONDITIONAL_JUMP`
<a id="insn-00bab6fc"></a> `00bab6fc` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab700"></a> `00bab700` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab704"></a> `00bab704` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab708"></a> `00bab708` | `e1 00 00 54` | b.ne 0x00bab724 | `CONDITIONAL_JUMP`
<a id="insn-00bab70c"></a> `00bab70c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab710"></a> `00bab710` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab714"></a> `00bab714` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab718"></a> `00bab718` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab71c"></a> `00bab71c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab720"></a> `00bab720` | `06 00 00 14` | b 0x00bab738 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab724"></a> `00bab724` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab728"></a> `00bab728` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab72c"></a> `00bab72c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab730"></a> `00bab730` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab734"></a> `00bab734` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab738"></a> `00bab738` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab73c"></a> `00bab73c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab740"></a> `00bab740` | `b8 c6 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab744"></a> `00bab744` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab748"></a> `00bab748` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab74c"></a> `00bab74c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab750"></a> `00bab750` | `c0 00 00 54` | b.eq 0x00bab768 | `CONDITIONAL_JUMP`
<a id="insn-00bab754"></a> `00bab754` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab758"></a> `00bab758` | `89 00 00 35` | cbnz w9,0x00bab768 | `CONDITIONAL_JUMP`
<a id="insn-00bab75c"></a> `00bab75c` | `e8 ff 9f 52` | mov w8,#0xffff | `FALL_THROUGH`
<a id="insn-00bab760"></a> `00bab760` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab764"></a> `00bab764` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bab768"></a> `00bab768` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab76c"></a> `00bab76c` | `54 00 00 b4` | cbz x20,0x00bab774 | `CONDITIONAL_JUMP`
<a id="insn-00bab770"></a> `00bab770` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab774"></a> `00bab774` | `53 00 00 b4` | cbz x19,0x00bab77c | `CONDITIONAL_JUMP`
<a id="insn-00bab778"></a> `00bab778` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab77c"></a> `00bab77c` | `29 3d 00 12` | and w9,w9,#0xffff | `FALL_THROUGH`
<a id="insn-00bab780"></a> `00bab780` | `3f 21 28 6b` | cmp w9,w8, UXTH  | `FALL_THROUGH`
<a id="insn-00bab784"></a> `00bab784` | `39 ff ff 17` | b 0x00bab468 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab788"></a> `00bab788` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab78c"></a> `00bab78c` | `61 01 00 54` | b.ne 0x00bab7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab790"></a> `00bab790` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab794"></a> `00bab794` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab798"></a> `00bab798` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab79c"></a> `00bab79c` | `e1 00 00 54` | b.ne 0x00bab7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab7a0"></a> `00bab7a0` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab7a4"></a> `00bab7a4` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab7a8"></a> `00bab7a8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab7ac"></a> `00bab7ac` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab7b0"></a> `00bab7b0` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab7b4"></a> `00bab7b4` | `06 00 00 14` | b 0x00bab7cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab7b8"></a> `00bab7b8` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab7bc"></a> `00bab7bc` | `08 81 44 f9` | ldr x8,[x8, #0x900] | `FALL_THROUGH`
<a id="insn-00bab7c0"></a> `00bab7c0` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab7c4"></a> `00bab7c4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab7c8"></a> `00bab7c8` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab7cc"></a> `00bab7cc` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab7d0"></a> `00bab7d0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab7d4"></a> `00bab7d4` | `93 c6 02 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00bab7d8"></a> `00bab7d8` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab7dc"></a> `00bab7dc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab7e0"></a> `00bab7e0` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab7e4"></a> `00bab7e4` | `c0 00 00 54` | b.eq 0x00bab7fc | `CONDITIONAL_JUMP`
<a id="insn-00bab7e8"></a> `00bab7e8` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab7ec"></a> `00bab7ec` | `89 00 00 35` | cbnz w9,0x00bab7fc | `CONDITIONAL_JUMP`
<a id="insn-00bab7f0"></a> `00bab7f0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bab7f4"></a> `00bab7f4` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab7f8"></a> `00bab7f8` | `08 30 9f 5a` | csinv w8,w0,wzr,cc | `FALL_THROUGH`
<a id="insn-00bab7fc"></a> `00bab7fc` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab800"></a> `00bab800` | `54 00 00 b4` | cbz x20,0x00bab808 | `CONDITIONAL_JUMP`
<a id="insn-00bab804"></a> `00bab804` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab808"></a> `00bab808` | `53 00 00 b4` | cbz x19,0x00bab810 | `CONDITIONAL_JUMP`
<a id="insn-00bab80c"></a> `00bab80c` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab810"></a> `00bab810` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab814"></a> `00bab814` | `15 ff ff 17` | b 0x00bab468 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab818"></a> `00bab818` | `1f 00 02 b1` | cmn x0,#0x80 | `FALL_THROUGH`
<a id="insn-00bab81c"></a> `00bab81c` | `e8 0f 80 12` | mov w8,#0xffffff80 | `FALL_THROUGH`
<a id="insn-00bab820"></a> `00bab820` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab824"></a> `00bab824` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab828"></a> `00bab828` | `54 00 00 b4` | cbz x20,0x00bab830 | `CONDITIONAL_JUMP`
<a id="insn-00bab82c"></a> `00bab82c` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab830"></a> `00bab830` | `53 00 00 b4` | cbz x19,0x00bab838 | `CONDITIONAL_JUMP`
<a id="insn-00bab834"></a> `00bab834` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab838"></a> `00bab838` | `29 1d 00 13` | sxtb w9,w9 | `FALL_THROUGH`
<a id="insn-00bab83c"></a> `00bab83c` | `3f 81 28 6b` | cmp w9,w8, SXTB  | `FALL_THROUGH`
<a id="insn-00bab840"></a> `00bab840` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab844"></a> `00bab844` | `0a ff ff 17` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab848"></a> `00bab848` | `1f 20 40 b1` | cmn x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab84c"></a> `00bab84c` | `e8 ff 8f 12` | mov w8,#0xffff8000 | `FALL_THROUGH`
<a id="insn-00bab850"></a> `00bab850` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab854"></a> `00bab854` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab858"></a> `00bab858` | `54 00 00 b4` | cbz x20,0x00bab860 | `CONDITIONAL_JUMP`
<a id="insn-00bab85c"></a> `00bab85c` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab860"></a> `00bab860` | `53 00 00 b4` | cbz x19,0x00bab868 | `CONDITIONAL_JUMP`
<a id="insn-00bab864"></a> `00bab864` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab868"></a> `00bab868` | `29 3d 00 13` | sxth w9,w9 | `FALL_THROUGH`
<a id="insn-00bab86c"></a> `00bab86c` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00bab870"></a> `00bab870` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab874"></a> `00bab874` | `fe fe ff 17` | b 0x00bab46c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab878"></a> `00bab878` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bab87c"></a> `00bab87c` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab880"></a> `00bab880` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab884"></a> `00bab884` | `28 81 88 9a` | csel x8,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bab888"></a> `00bab888` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab88c"></a> `00bab88c` | `1f b5 00 71` | cmp w8,#0x2d | `FALL_THROUGH`
<a id="insn-00bab890"></a> `00bab890` | `61 00 00 54` | b.ne 0x00bab89c | `CONDITIONAL_JUMP`
<a id="insn-00bab894"></a> `00bab894` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00bab898"></a> `00bab898` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab89c"></a> `00bab89c` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bab8a0"></a> `00bab8a0` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab8a4"></a> `00bab8a4` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bab8a8"></a> `00bab8a8` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bab8ac"></a> `00bab8ac` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bab8b0"></a> `00bab8b0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bab8b4"></a> `00bab8b4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab8b8"></a> `00bab8b8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab8bc"></a> `00bab8bc` | `eb fe ff 17` | b 0x00bab468 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab8c0"></a> `00bab8c0` | `bc b1 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baafa8`](#insn-00baafa8) 範囲 `[['00baafa8', '00baafbb']]`
  - `FALL_THROUGH` [`00baafb8`](#insn-00baafb8) → [`00baafbc`](#insn-00baafbc)
- ブロック [`00baafbc`](#insn-00baafbc) 範囲 `[['00baafbc', '00baafd3']]`
  - `CONDITIONAL_JUMP` [`00baafd0`](#insn-00baafd0) → [`00bab248`](#insn-00bab248)
  - `FALL_THROUGH` [`00baafd0`](#insn-00baafd0) → [`00baafd4`](#insn-00baafd4)
- ブロック [`00baafd4`](#insn-00baafd4) 範囲 `[['00baafd4', '00baafdb']]`
  - `FALL_THROUGH` [`00baafd8`](#insn-00baafd8) → [`00baafdc`](#insn-00baafdc)
- ブロック [`00baafdc`](#insn-00baafdc) 範囲 `[['00baafdc', '00baafef']]`
  - `FALL_THROUGH` [`00baafec`](#insn-00baafec) → [`00baaff0`](#insn-00baaff0)
- ブロック [`00baaff0`](#insn-00baaff0) 範囲 `[['00baaff0', '00baaff3']]`
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00baaff4`](#insn-00baaff4)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab250`](#insn-00bab250)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab1d0`](#insn-00bab1d0)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab218`](#insn-00bab218)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab0b4`](#insn-00bab0b4)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab268`](#insn-00bab268)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab280`](#insn-00bab280)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab230`](#insn-00bab230)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab298`](#insn-00bab298)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab0fc`](#insn-00bab0fc)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab2b0`](#insn-00bab2b0)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab03c`](#insn-00bab03c)
  - `COMPUTED_JUMP` [`00baaff0`](#insn-00baaff0) → [`00bab154`](#insn-00bab154)
- ブロック [`00baaff4`](#insn-00baaff4) 範囲 `[['00baaff4', '00baaff7']]`
  - `CONDITIONAL_JUMP` [`00baaff4`](#insn-00baaff4) → [`00baaffc`](#insn-00baaffc)
  - `FALL_THROUGH` [`00baaff4`](#insn-00baaff4) → [`00baaff8`](#insn-00baaff8)
- ブロック [`00baaff8`](#insn-00baaff8) 範囲 `[['00baaff8', '00baaffb']]`
  - `CONDITIONAL_JUMP` [`00baaff8`](#insn-00baaff8) → [`00bab258`](#insn-00bab258)
  - `FALL_THROUGH` [`00baaff8`](#insn-00baaff8) → [`00baaffc`](#insn-00baaffc)
- ブロック [`00baaffc`](#insn-00baaffc) 範囲 `[['00baaffc', '00bab007']]`
  - `FALL_THROUGH` [`00bab004`](#insn-00bab004) → [`00bab008`](#insn-00bab008)
- ブロック [`00bab008`](#insn-00bab008) 範囲 `[['00bab008', '00bab017']]`
  - `CONDITIONAL_JUMP` [`00bab014`](#insn-00bab014) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab014`](#insn-00bab014) → [`00bab018`](#insn-00bab018)
- ブロック [`00bab018`](#insn-00bab018) 範囲 `[['00bab018', '00bab01b']]`
  - `FALL_THROUGH` [`00bab018`](#insn-00bab018) → [`00bab01c`](#insn-00bab01c)
- ブロック [`00bab01c`](#insn-00bab01c) 範囲 `[['00bab01c', '00bab02b']]`
  - `CONDITIONAL_JUMP` [`00bab028`](#insn-00bab028) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00bab028`](#insn-00bab028) → [`00bab02c`](#insn-00bab02c)
- ブロック [`00bab02c`](#insn-00bab02c) 範囲 `[['00bab02c', '00bab037']]`
  - `CONDITIONAL_JUMP` [`00bab034`](#insn-00bab034) → [`00bab01c`](#insn-00bab01c)
  - `FALL_THROUGH` [`00bab034`](#insn-00bab034) → [`00bab038`](#insn-00bab038)
- ブロック [`00bab038`](#insn-00bab038) 範囲 `[['00bab038', '00bab03b']]`
  - `UNCONDITIONAL_JUMP` [`00bab038`](#insn-00bab038) → [`00bab408`](#insn-00bab408)
- ブロック [`00bab03c`](#insn-00bab03c) 範囲 `[['00bab03c', '00bab03f']]`
  - `CONDITIONAL_JUMP` [`00bab03c`](#insn-00bab03c) → [`00bab048`](#insn-00bab048)
  - `FALL_THROUGH` [`00bab03c`](#insn-00bab03c) → [`00bab040`](#insn-00bab040)
- ブロック [`00bab040`](#insn-00bab040) 範囲 `[['00bab040', '00bab047']]`
  - `CONDITIONAL_JUMP` [`00bab044`](#insn-00bab044) → [`00bab098`](#insn-00bab098)
  - `FALL_THROUGH` [`00bab044`](#insn-00bab044) → [`00bab048`](#insn-00bab048)
- ブロック [`00bab048`](#insn-00bab048) 範囲 `[['00bab048', '00bab057']]`
  - `FALL_THROUGH` [`00bab054`](#insn-00bab054) → [`00bab058`](#insn-00bab058)
- ブロック [`00bab058`](#insn-00bab058) 範囲 `[['00bab058', '00bab077']]`
  - `FALL_THROUGH` [`00bab074`](#insn-00bab074) → [`00bab078`](#insn-00bab078)
- ブロック [`00bab078`](#insn-00bab078) 範囲 `[['00bab078', '00bab07b']]`
  - `CONDITIONAL_JUMP` [`00bab078`](#insn-00bab078) → [`00bab098`](#insn-00bab098)
  - `FALL_THROUGH` [`00bab078`](#insn-00bab078) → [`00bab07c`](#insn-00bab07c)
- ブロック [`00bab07c`](#insn-00bab07c) 範囲 `[['00bab07c', '00bab083']]`
  - `CONDITIONAL_JUMP` [`00bab080`](#insn-00bab080) → [`00bab098`](#insn-00bab098)
  - `FALL_THROUGH` [`00bab080`](#insn-00bab080) → [`00bab084`](#insn-00bab084)
- ブロック [`00bab084`](#insn-00bab084) 範囲 `[['00bab084', '00bab08f']]`
  - `CONDITIONAL_JUMP` [`00bab08c`](#insn-00bab08c) → [`00bab098`](#insn-00bab098)
  - `FALL_THROUGH` [`00bab08c`](#insn-00bab08c) → [`00bab090`](#insn-00bab090)
- ブロック [`00bab090`](#insn-00bab090) 範囲 `[['00bab090', '00bab097']]`
  - `FALL_THROUGH` [`00bab094`](#insn-00bab094) → [`00bab098`](#insn-00bab098)
- ブロック [`00bab098`](#insn-00bab098) 範囲 `[['00bab098', '00bab09f']]`
  - `CONDITIONAL_JUMP` [`00bab09c`](#insn-00bab09c) → [`00bab0a4`](#insn-00bab0a4)
  - `FALL_THROUGH` [`00bab09c`](#insn-00bab09c) → [`00bab0a0`](#insn-00bab0a0)
- ブロック [`00bab0a0`](#insn-00bab0a0) 範囲 `[['00bab0a0', '00bab0a3']]`
  - `FALL_THROUGH` [`00bab0a0`](#insn-00bab0a0) → [`00bab0a4`](#insn-00bab0a4)
- ブロック [`00bab0a4`](#insn-00bab0a4) 範囲 `[['00bab0a4', '00bab0a7']]`
  - `CONDITIONAL_JUMP` [`00bab0a4`](#insn-00bab0a4) → [`00bab0ac`](#insn-00bab0ac)
  - `FALL_THROUGH` [`00bab0a4`](#insn-00bab0a4) → [`00bab0a8`](#insn-00bab0a8)
- ブロック [`00bab0a8`](#insn-00bab0a8) 範囲 `[['00bab0a8', '00bab0ab']]`
  - `FALL_THROUGH` [`00bab0a8`](#insn-00bab0a8) → [`00bab0ac`](#insn-00bab0ac)
- ブロック [`00bab0ac`](#insn-00bab0ac) 範囲 `[['00bab0ac', '00bab0b3']]`
  - `UNCONDITIONAL_JUMP` [`00bab0b0`](#insn-00bab0b0) → [`00bab1c8`](#insn-00bab1c8)
- ブロック [`00bab0b4`](#insn-00bab0b4) 範囲 `[['00bab0b4', '00bab0b7']]`
  - `CONDITIONAL_JUMP` [`00bab0b4`](#insn-00bab0b4) → [`00bab0bc`](#insn-00bab0bc)
  - `FALL_THROUGH` [`00bab0b4`](#insn-00bab0b4) → [`00bab0b8`](#insn-00bab0b8)
- ブロック [`00bab0b8`](#insn-00bab0b8) 範囲 `[['00bab0b8', '00bab0bb']]`
  - `CONDITIONAL_JUMP` [`00bab0b8`](#insn-00bab0b8) → [`00bab258`](#insn-00bab258)
  - `FALL_THROUGH` [`00bab0b8`](#insn-00bab0b8) → [`00bab0bc`](#insn-00bab0bc)
- ブロック [`00bab0bc`](#insn-00bab0bc) 範囲 `[['00bab0bc', '00bab0c7']]`
  - `FALL_THROUGH` [`00bab0c4`](#insn-00bab0c4) → [`00bab0c8`](#insn-00bab0c8)
- ブロック [`00bab0c8`](#insn-00bab0c8) 範囲 `[['00bab0c8', '00bab0d7']]`
  - `CONDITIONAL_JUMP` [`00bab0d4`](#insn-00bab0d4) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab0d4`](#insn-00bab0d4) → [`00bab0d8`](#insn-00bab0d8)
- ブロック [`00bab0d8`](#insn-00bab0d8) 範囲 `[['00bab0d8', '00bab0db']]`
  - `FALL_THROUGH` [`00bab0d8`](#insn-00bab0d8) → [`00bab0dc`](#insn-00bab0dc)
- ブロック [`00bab0dc`](#insn-00bab0dc) 範囲 `[['00bab0dc', '00bab0eb']]`
  - `CONDITIONAL_JUMP` [`00bab0e8`](#insn-00bab0e8) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00bab0e8`](#insn-00bab0e8) → [`00bab0ec`](#insn-00bab0ec)
- ブロック [`00bab0ec`](#insn-00bab0ec) 範囲 `[['00bab0ec', '00bab0f3']]`
  - `FALL_THROUGH` [`00bab0f0`](#insn-00bab0f0) → [`00bab0f4`](#insn-00bab0f4)
- ブロック [`00bab0f4`](#insn-00bab0f4) 範囲 `[['00bab0f4', '00bab0f7']]`
  - `CONDITIONAL_JUMP` [`00bab0f4`](#insn-00bab0f4) → [`00bab0dc`](#insn-00bab0dc)
  - `FALL_THROUGH` [`00bab0f4`](#insn-00bab0f4) → [`00bab0f8`](#insn-00bab0f8)
- ブロック [`00bab0f8`](#insn-00bab0f8) 範囲 `[['00bab0f8', '00bab0fb']]`
  - `UNCONDITIONAL_JUMP` [`00bab0f8`](#insn-00bab0f8) → [`00bab408`](#insn-00bab408)
- ブロック [`00bab0fc`](#insn-00bab0fc) 範囲 `[['00bab0fc', '00bab103']]`
  - `CONDITIONAL_JUMP` [`00bab100`](#insn-00bab100) → [`00bab108`](#insn-00bab108)
  - `FALL_THROUGH` [`00bab100`](#insn-00bab100) → [`00bab104`](#insn-00bab104)
- ブロック [`00bab104`](#insn-00bab104) 範囲 `[['00bab104', '00bab107']]`
  - `CONDITIONAL_JUMP` [`00bab104`](#insn-00bab104) → [`00bab12c`](#insn-00bab12c)
  - `FALL_THROUGH` [`00bab104`](#insn-00bab104) → [`00bab108`](#insn-00bab108)
- ブロック [`00bab108`](#insn-00bab108) 範囲 `[['00bab108', '00bab117']]`
  - `FALL_THROUGH` [`00bab114`](#insn-00bab114) → [`00bab118`](#insn-00bab118)
- ブロック [`00bab118`](#insn-00bab118) 範囲 `[['00bab118', '00bab12b']]`
  - `FALL_THROUGH` [`00bab128`](#insn-00bab128) → [`00bab12c`](#insn-00bab12c)
- ブロック [`00bab12c`](#insn-00bab12c) 範囲 `[['00bab12c', '00bab143']]`
  - `FALL_THROUGH` [`00bab140`](#insn-00bab140) → [`00bab144`](#insn-00bab144)
- ブロック [`00bab144`](#insn-00bab144) 範囲 `[['00bab144', '00bab153']]`
  - `UNCONDITIONAL_JUMP` [`00bab150`](#insn-00bab150) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab154`](#insn-00bab154) 範囲 `[['00bab154', '00bab157']]`
  - `CONDITIONAL_JUMP` [`00bab154`](#insn-00bab154) → [`00bab160`](#insn-00bab160)
  - `FALL_THROUGH` [`00bab154`](#insn-00bab154) → [`00bab158`](#insn-00bab158)
- ブロック [`00bab158`](#insn-00bab158) 範囲 `[['00bab158', '00bab15f']]`
  - `CONDITIONAL_JUMP` [`00bab15c`](#insn-00bab15c) → [`00bab1b0`](#insn-00bab1b0)
  - `FALL_THROUGH` [`00bab15c`](#insn-00bab15c) → [`00bab160`](#insn-00bab160)
- ブロック [`00bab160`](#insn-00bab160) 範囲 `[['00bab160', '00bab167']]`
  - `FALL_THROUGH` [`00bab164`](#insn-00bab164) → [`00bab168`](#insn-00bab168)
- ブロック [`00bab168`](#insn-00bab168) 範囲 `[['00bab168', '00bab193']]`
  - `CONDITIONAL_JUMP` [`00bab190`](#insn-00bab190) → [`00bab1b0`](#insn-00bab1b0)
  - `FALL_THROUGH` [`00bab190`](#insn-00bab190) → [`00bab194`](#insn-00bab194)
- ブロック [`00bab194`](#insn-00bab194) 範囲 `[['00bab194', '00bab19b']]`
  - `CONDITIONAL_JUMP` [`00bab198`](#insn-00bab198) → [`00bab1b0`](#insn-00bab1b0)
  - `FALL_THROUGH` [`00bab198`](#insn-00bab198) → [`00bab19c`](#insn-00bab19c)
- ブロック [`00bab19c`](#insn-00bab19c) 範囲 `[['00bab19c', '00bab1a7']]`
  - `CONDITIONAL_JUMP` [`00bab1a4`](#insn-00bab1a4) → [`00bab1b0`](#insn-00bab1b0)
  - `FALL_THROUGH` [`00bab1a4`](#insn-00bab1a4) → [`00bab1a8`](#insn-00bab1a8)
- ブロック [`00bab1a8`](#insn-00bab1a8) 範囲 `[['00bab1a8', '00bab1af']]`
  - `FALL_THROUGH` [`00bab1ac`](#insn-00bab1ac) → [`00bab1b0`](#insn-00bab1b0)
- ブロック [`00bab1b0`](#insn-00bab1b0) 範囲 `[['00bab1b0', '00bab1b3']]`
  - `FALL_THROUGH` [`00bab1b0`](#insn-00bab1b0) → [`00bab1b4`](#insn-00bab1b4)
- ブロック [`00bab1b4`](#insn-00bab1b4) 範囲 `[['00bab1b4', '00bab1b7']]`
  - `CONDITIONAL_JUMP` [`00bab1b4`](#insn-00bab1b4) → [`00bab1bc`](#insn-00bab1bc)
  - `FALL_THROUGH` [`00bab1b4`](#insn-00bab1b4) → [`00bab1b8`](#insn-00bab1b8)
- ブロック [`00bab1b8`](#insn-00bab1b8) 範囲 `[['00bab1b8', '00bab1bb']]`
  - `FALL_THROUGH` [`00bab1b8`](#insn-00bab1b8) → [`00bab1bc`](#insn-00bab1bc)
- ブロック [`00bab1bc`](#insn-00bab1bc) 範囲 `[['00bab1bc', '00bab1bf']]`
  - `CONDITIONAL_JUMP` [`00bab1bc`](#insn-00bab1bc) → [`00bab1c4`](#insn-00bab1c4)
  - `FALL_THROUGH` [`00bab1bc`](#insn-00bab1bc) → [`00bab1c0`](#insn-00bab1c0)
- ブロック [`00bab1c0`](#insn-00bab1c0) 範囲 `[['00bab1c0', '00bab1c3']]`
  - `FALL_THROUGH` [`00bab1c0`](#insn-00bab1c0) → [`00bab1c4`](#insn-00bab1c4)
- ブロック [`00bab1c4`](#insn-00bab1c4) 範囲 `[['00bab1c4', '00bab1c7']]`
  - `FALL_THROUGH` [`00bab1c4`](#insn-00bab1c4) → [`00bab1c8`](#insn-00bab1c8)
- ブロック [`00bab1c8`](#insn-00bab1c8) 範囲 `[['00bab1c8', '00bab1cf']]`
  - `UNCONDITIONAL_JUMP` [`00bab1cc`](#insn-00bab1cc) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab1d0`](#insn-00bab1d0) 範囲 `[['00bab1d0', '00bab1d3']]`
  - `CONDITIONAL_JUMP` [`00bab1d0`](#insn-00bab1d0) → [`00bab1d8`](#insn-00bab1d8)
  - `FALL_THROUGH` [`00bab1d0`](#insn-00bab1d0) → [`00bab1d4`](#insn-00bab1d4)
- ブロック [`00bab1d4`](#insn-00bab1d4) 範囲 `[['00bab1d4', '00bab1d7']]`
  - `CONDITIONAL_JUMP` [`00bab1d4`](#insn-00bab1d4) → [`00bab258`](#insn-00bab258)
  - `FALL_THROUGH` [`00bab1d4`](#insn-00bab1d4) → [`00bab1d8`](#insn-00bab1d8)
- ブロック [`00bab1d8`](#insn-00bab1d8) 範囲 `[['00bab1d8', '00bab1df']]`
  - `FALL_THROUGH` [`00bab1dc`](#insn-00bab1dc) → [`00bab1e0`](#insn-00bab1e0)
- ブロック [`00bab1e0`](#insn-00bab1e0) 範囲 `[['00bab1e0', '00bab1f3']]`
  - `CONDITIONAL_JUMP` [`00bab1f0`](#insn-00bab1f0) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab1f0`](#insn-00bab1f0) → [`00bab1f4`](#insn-00bab1f4)
- ブロック [`00bab1f4`](#insn-00bab1f4) 範囲 `[['00bab1f4', '00bab1f7']]`
  - `FALL_THROUGH` [`00bab1f4`](#insn-00bab1f4) → [`00bab1f8`](#insn-00bab1f8)
- ブロック [`00bab1f8`](#insn-00bab1f8) 範囲 `[['00bab1f8', '00bab207']]`
  - `CONDITIONAL_JUMP` [`00bab204`](#insn-00bab204) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00bab204`](#insn-00bab204) → [`00bab208`](#insn-00bab208)
- ブロック [`00bab208`](#insn-00bab208) 範囲 `[['00bab208', '00bab213']]`
  - `CONDITIONAL_JUMP` [`00bab210`](#insn-00bab210) → [`00bab1f8`](#insn-00bab1f8)
  - `FALL_THROUGH` [`00bab210`](#insn-00bab210) → [`00bab214`](#insn-00bab214)
- ブロック [`00bab214`](#insn-00bab214) 範囲 `[['00bab214', '00bab217']]`
  - `UNCONDITIONAL_JUMP` [`00bab214`](#insn-00bab214) → [`00bab408`](#insn-00bab408)
- ブロック [`00bab218`](#insn-00bab218) 範囲 `[['00bab218', '00bab21b']]`
  - `CONDITIONAL_JUMP` [`00bab218`](#insn-00bab218) → [`00bab318`](#insn-00bab318)
  - `FALL_THROUGH` [`00bab218`](#insn-00bab218) → [`00bab21c`](#insn-00bab21c)
- ブロック [`00bab21c`](#insn-00bab21c) 範囲 `[['00bab21c', '00bab21f']]`
  - `CONDITIONAL_JUMP` [`00bab21c`](#insn-00bab21c) → [`00bab318`](#insn-00bab318)
  - `FALL_THROUGH` [`00bab21c`](#insn-00bab21c) → [`00bab220`](#insn-00bab220)
- ブロック [`00bab220`](#insn-00bab220) 範囲 `[['00bab220', '00bab22b']]`
  - `CONDITIONAL_JUMP` [`00bab228`](#insn-00bab228) → [`00bab82c`](#insn-00bab82c)
  - `FALL_THROUGH` [`00bab228`](#insn-00bab228) → [`00bab22c`](#insn-00bab22c)
- ブロック [`00bab22c`](#insn-00bab22c) 範囲 `[['00bab22c', '00bab22f']]`
  - `UNCONDITIONAL_JUMP` [`00bab22c`](#insn-00bab22c) → [`00bab830`](#insn-00bab830)
- ブロック [`00bab230`](#insn-00bab230) 範囲 `[['00bab230', '00bab233']]`
  - `CONDITIONAL_JUMP` [`00bab230`](#insn-00bab230) → [`00bab358`](#insn-00bab358)
  - `FALL_THROUGH` [`00bab230`](#insn-00bab230) → [`00bab234`](#insn-00bab234)
- ブロック [`00bab234`](#insn-00bab234) 範囲 `[['00bab234', '00bab237']]`
  - `CONDITIONAL_JUMP` [`00bab234`](#insn-00bab234) → [`00bab358`](#insn-00bab358)
  - `FALL_THROUGH` [`00bab234`](#insn-00bab234) → [`00bab238`](#insn-00bab238)
- ブロック [`00bab238`](#insn-00bab238) 範囲 `[['00bab238', '00bab243']]`
  - `CONDITIONAL_JUMP` [`00bab240`](#insn-00bab240) → [`00bab65c`](#insn-00bab65c)
  - `FALL_THROUGH` [`00bab240`](#insn-00bab240) → [`00bab244`](#insn-00bab244)
- ブロック [`00bab244`](#insn-00bab244) 範囲 `[['00bab244', '00bab247']]`
  - `UNCONDITIONAL_JUMP` [`00bab244`](#insn-00bab244) → [`00bab660`](#insn-00bab660)
- ブロック [`00bab248`](#insn-00bab248) 範囲 `[['00bab248', '00bab24f']]`
  - `UNCONDITIONAL_JUMP` [`00bab24c`](#insn-00bab24c) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab250`](#insn-00bab250) 範囲 `[['00bab250', '00bab253']]`
  - `CONDITIONAL_JUMP` [`00bab250`](#insn-00bab250) → [`00bab398`](#insn-00bab398)
  - `FALL_THROUGH` [`00bab250`](#insn-00bab250) → [`00bab254`](#insn-00bab254)
- ブロック [`00bab254`](#insn-00bab254) 範囲 `[['00bab254', '00bab257']]`
  - `CONDITIONAL_JUMP` [`00bab254`](#insn-00bab254) → [`00bab398`](#insn-00bab398)
  - `FALL_THROUGH` [`00bab254`](#insn-00bab254) → [`00bab258`](#insn-00bab258)
- ブロック [`00bab258`](#insn-00bab258) 範囲 `[['00bab258', '00bab263']]`
  - `CONDITIONAL_JUMP` [`00bab260`](#insn-00bab260) → [`00bab454`](#insn-00bab454)
  - `FALL_THROUGH` [`00bab260`](#insn-00bab260) → [`00bab264`](#insn-00bab264)
- ブロック [`00bab264`](#insn-00bab264) 範囲 `[['00bab264', '00bab267']]`
  - `UNCONDITIONAL_JUMP` [`00bab264`](#insn-00bab264) → [`00bab458`](#insn-00bab458)
- ブロック [`00bab268`](#insn-00bab268) 範囲 `[['00bab268', '00bab26b']]`
  - `CONDITIONAL_JUMP` [`00bab268`](#insn-00bab268) → [`00bab490`](#insn-00bab490)
  - `FALL_THROUGH` [`00bab268`](#insn-00bab268) → [`00bab26c`](#insn-00bab26c)
- ブロック [`00bab26c`](#insn-00bab26c) 範囲 `[['00bab26c', '00bab26f']]`
  - `CONDITIONAL_JUMP` [`00bab26c`](#insn-00bab26c) → [`00bab490`](#insn-00bab490)
  - `FALL_THROUGH` [`00bab26c`](#insn-00bab26c) → [`00bab270`](#insn-00bab270)
- ブロック [`00bab270`](#insn-00bab270) 範囲 `[['00bab270', '00bab27b']]`
  - `CONDITIONAL_JUMP` [`00bab278`](#insn-00bab278) → [`00bab85c`](#insn-00bab85c)
  - `FALL_THROUGH` [`00bab278`](#insn-00bab278) → [`00bab27c`](#insn-00bab27c)
- ブロック [`00bab27c`](#insn-00bab27c) 範囲 `[['00bab27c', '00bab27f']]`
  - `UNCONDITIONAL_JUMP` [`00bab27c`](#insn-00bab27c) → [`00bab860`](#insn-00bab860)
- ブロック [`00bab280`](#insn-00bab280) 範囲 `[['00bab280', '00bab283']]`
  - `CONDITIONAL_JUMP` [`00bab280`](#insn-00bab280) → [`00bab4d0`](#insn-00bab4d0)
  - `FALL_THROUGH` [`00bab280`](#insn-00bab280) → [`00bab284`](#insn-00bab284)
- ブロック [`00bab284`](#insn-00bab284) 範囲 `[['00bab284', '00bab287']]`
  - `CONDITIONAL_JUMP` [`00bab284`](#insn-00bab284) → [`00bab4d0`](#insn-00bab4d0)
  - `FALL_THROUGH` [`00bab284`](#insn-00bab284) → [`00bab288`](#insn-00bab288)
- ブロック [`00bab288`](#insn-00bab288) 範囲 `[['00bab288', '00bab293']]`
  - `CONDITIONAL_JUMP` [`00bab290`](#insn-00bab290) → [`00bab770`](#insn-00bab770)
  - `FALL_THROUGH` [`00bab290`](#insn-00bab290) → [`00bab294`](#insn-00bab294)
- ブロック [`00bab294`](#insn-00bab294) 範囲 `[['00bab294', '00bab297']]`
  - `UNCONDITIONAL_JUMP` [`00bab294`](#insn-00bab294) → [`00bab774`](#insn-00bab774)
- ブロック [`00bab298`](#insn-00bab298) 範囲 `[['00bab298', '00bab29b']]`
  - `CONDITIONAL_JUMP` [`00bab298`](#insn-00bab298) → [`00bab510`](#insn-00bab510)
  - `FALL_THROUGH` [`00bab298`](#insn-00bab298) → [`00bab29c`](#insn-00bab29c)
- ブロック [`00bab29c`](#insn-00bab29c) 範囲 `[['00bab29c', '00bab29f']]`
  - `CONDITIONAL_JUMP` [`00bab29c`](#insn-00bab29c) → [`00bab510`](#insn-00bab510)
  - `FALL_THROUGH` [`00bab29c`](#insn-00bab29c) → [`00bab2a0`](#insn-00bab2a0)
- ブロック [`00bab2a0`](#insn-00bab2a0) 範囲 `[['00bab2a0', '00bab2ab']]`
  - `CONDITIONAL_JUMP` [`00bab2a8`](#insn-00bab2a8) → [`00bab804`](#insn-00bab804)
  - `FALL_THROUGH` [`00bab2a8`](#insn-00bab2a8) → [`00bab2ac`](#insn-00bab2ac)
- ブロック [`00bab2ac`](#insn-00bab2ac) 範囲 `[['00bab2ac', '00bab2af']]`
  - `UNCONDITIONAL_JUMP` [`00bab2ac`](#insn-00bab2ac) → [`00bab808`](#insn-00bab808)
- ブロック [`00bab2b0`](#insn-00bab2b0) 範囲 `[['00bab2b0', '00bab2b7']]`
  - `CONDITIONAL_JUMP` [`00bab2b4`](#insn-00bab2b4) → [`00bab2bc`](#insn-00bab2bc)
  - `FALL_THROUGH` [`00bab2b4`](#insn-00bab2b4) → [`00bab2b8`](#insn-00bab2b8)
- ブロック [`00bab2b8`](#insn-00bab2b8) 範囲 `[['00bab2b8', '00bab2bb']]`
  - `CONDITIONAL_JUMP` [`00bab2b8`](#insn-00bab2b8) → [`00bab89c`](#insn-00bab89c)
  - `FALL_THROUGH` [`00bab2b8`](#insn-00bab2b8) → [`00bab2bc`](#insn-00bab2bc)
- ブロック [`00bab2bc`](#insn-00bab2bc) 範囲 `[['00bab2bc', '00bab2eb']]`
  - `CONDITIONAL_JUMP` [`00bab2e8`](#insn-00bab2e8) → [`00bab89c`](#insn-00bab89c)
  - `FALL_THROUGH` [`00bab2e8`](#insn-00bab2e8) → [`00bab2ec`](#insn-00bab2ec)
- ブロック [`00bab2ec`](#insn-00bab2ec) 範囲 `[['00bab2ec', '00bab2ef']]`
  - `CONDITIONAL_JUMP` [`00bab2ec`](#insn-00bab2ec) → [`00bab89c`](#insn-00bab89c)
  - `FALL_THROUGH` [`00bab2ec`](#insn-00bab2ec) → [`00bab2f0`](#insn-00bab2f0)
- ブロック [`00bab2f0`](#insn-00bab2f0) 範囲 `[['00bab2f0', '00bab2f7']]`
  - `CONDITIONAL_JUMP` [`00bab2f4`](#insn-00bab2f4) → [`00bab878`](#insn-00bab878)
  - `FALL_THROUGH` [`00bab2f4`](#insn-00bab2f4) → [`00bab2f8`](#insn-00bab2f8)
- ブロック [`00bab2f8`](#insn-00bab2f8) 範囲 `[['00bab2f8', '00bab2fb']]`
  - `FALL_THROUGH` [`00bab2f8`](#insn-00bab2f8) → [`00bab2fc`](#insn-00bab2fc)
- ブロック [`00bab2fc`](#insn-00bab2fc) 範囲 `[['00bab2fc', '00bab2ff']]`
  - `FALL_THROUGH` [`00bab2fc`](#insn-00bab2fc) → [`00bab300`](#insn-00bab300)
- ブロック [`00bab300`](#insn-00bab300) 範囲 `[['00bab300', '00bab30b']]`
  - `CONDITIONAL_JUMP` [`00bab308`](#insn-00bab308) → [`00bab87c`](#insn-00bab87c)
  - `FALL_THROUGH` [`00bab308`](#insn-00bab308) → [`00bab30c`](#insn-00bab30c)
- ブロック [`00bab30c`](#insn-00bab30c) 範囲 `[['00bab30c', '00bab313']]`
  - `CONDITIONAL_JUMP` [`00bab310`](#insn-00bab310) → [`00bab2fc`](#insn-00bab2fc)
  - `FALL_THROUGH` [`00bab310`](#insn-00bab310) → [`00bab314`](#insn-00bab314)
- ブロック [`00bab314`](#insn-00bab314) 範囲 `[['00bab314', '00bab317']]`
  - `UNCONDITIONAL_JUMP` [`00bab314`](#insn-00bab314) → [`00bab87c`](#insn-00bab87c)
- ブロック [`00bab318`](#insn-00bab318) 範囲 `[['00bab318', '00bab323']]`
  - `FALL_THROUGH` [`00bab320`](#insn-00bab320) → [`00bab324`](#insn-00bab324)
- ブロック [`00bab324`](#insn-00bab324) 範囲 `[['00bab324', '00bab333']]`
  - `CONDITIONAL_JUMP` [`00bab330`](#insn-00bab330) → [`00bab580`](#insn-00bab580)
  - `FALL_THROUGH` [`00bab330`](#insn-00bab330) → [`00bab334`](#insn-00bab334)
- ブロック [`00bab334`](#insn-00bab334) 範囲 `[['00bab334', '00bab337']]`
  - `FALL_THROUGH` [`00bab334`](#insn-00bab334) → [`00bab338`](#insn-00bab338)
- ブロック [`00bab338`](#insn-00bab338) 範囲 `[['00bab338', '00bab347']]`
  - `CONDITIONAL_JUMP` [`00bab344`](#insn-00bab344) → [`00bab550`](#insn-00bab550)
  - `FALL_THROUGH` [`00bab344`](#insn-00bab344) → [`00bab348`](#insn-00bab348)
- ブロック [`00bab348`](#insn-00bab348) 範囲 `[['00bab348', '00bab353']]`
  - `CONDITIONAL_JUMP` [`00bab350`](#insn-00bab350) → [`00bab338`](#insn-00bab338)
  - `FALL_THROUGH` [`00bab350`](#insn-00bab350) → [`00bab354`](#insn-00bab354)
- ブロック [`00bab354`](#insn-00bab354) 範囲 `[['00bab354', '00bab357']]`
  - `UNCONDITIONAL_JUMP` [`00bab354`](#insn-00bab354) → [`00bab580`](#insn-00bab580)
- ブロック [`00bab358`](#insn-00bab358) 範囲 `[['00bab358', '00bab373']]`
  - `CONDITIONAL_JUMP` [`00bab370`](#insn-00bab370) → [`00bab600`](#insn-00bab600)
  - `FALL_THROUGH` [`00bab370`](#insn-00bab370) → [`00bab374`](#insn-00bab374)
- ブロック [`00bab374`](#insn-00bab374) 範囲 `[['00bab374', '00bab377']]`
  - `FALL_THROUGH` [`00bab374`](#insn-00bab374) → [`00bab378`](#insn-00bab378)
- ブロック [`00bab378`](#insn-00bab378) 範囲 `[['00bab378', '00bab387']]`
  - `CONDITIONAL_JUMP` [`00bab384`](#insn-00bab384) → [`00bab5d0`](#insn-00bab5d0)
  - `FALL_THROUGH` [`00bab384`](#insn-00bab384) → [`00bab388`](#insn-00bab388)
- ブロック [`00bab388`](#insn-00bab388) 範囲 `[['00bab388', '00bab393']]`
  - `CONDITIONAL_JUMP` [`00bab390`](#insn-00bab390) → [`00bab378`](#insn-00bab378)
  - `FALL_THROUGH` [`00bab390`](#insn-00bab390) → [`00bab394`](#insn-00bab394)
- ブロック [`00bab394`](#insn-00bab394) 範囲 `[['00bab394', '00bab397']]`
  - `UNCONDITIONAL_JUMP` [`00bab394`](#insn-00bab394) → [`00bab600`](#insn-00bab600)
- ブロック [`00bab398`](#insn-00bab398) 範囲 `[['00bab398', '00bab3a3']]`
  - `FALL_THROUGH` [`00bab3a0`](#insn-00bab3a0) → [`00bab3a4`](#insn-00bab3a4)
- ブロック [`00bab3a4`](#insn-00bab3a4) 範囲 `[['00bab3a4', '00bab3b3']]`
  - `CONDITIONAL_JUMP` [`00bab3b0`](#insn-00bab3b0) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab3b0`](#insn-00bab3b0) → [`00bab3b4`](#insn-00bab3b4)
- ブロック [`00bab3b4`](#insn-00bab3b4) 範囲 `[['00bab3b4', '00bab3b7']]`
  - `FALL_THROUGH` [`00bab3b4`](#insn-00bab3b4) → [`00bab3b8`](#insn-00bab3b8)
- ブロック [`00bab3b8`](#insn-00bab3b8) 範囲 `[['00bab3b8', '00bab3c7']]`
  - `CONDITIONAL_JUMP` [`00bab3c4`](#insn-00bab3c4) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00bab3c4`](#insn-00bab3c4) → [`00bab3c8`](#insn-00bab3c8)
- ブロック [`00bab3c8`](#insn-00bab3c8) 範囲 `[['00bab3c8', '00bab3d3']]`
  - `CONDITIONAL_JUMP` [`00bab3d0`](#insn-00bab3d0) → [`00bab3b8`](#insn-00bab3b8)
  - `FALL_THROUGH` [`00bab3d0`](#insn-00bab3d0) → [`00bab3d4`](#insn-00bab3d4)
- ブロック [`00bab3d4`](#insn-00bab3d4) 範囲 `[['00bab3d4', '00bab3d7']]`
  - `UNCONDITIONAL_JUMP` [`00bab3d4`](#insn-00bab3d4) → [`00bab408`](#insn-00bab408)
- ブロック [`00bab3d8`](#insn-00bab3d8) 範囲 `[['00bab3d8', '00bab3df']]`
  - `CONDITIONAL_JUMP` [`00bab3dc`](#insn-00bab3dc) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab3dc`](#insn-00bab3dc) → [`00bab3e0`](#insn-00bab3e0)
- ブロック [`00bab3e0`](#insn-00bab3e0) 範囲 `[['00bab3e0', '00bab3ef']]`
  - `CONDITIONAL_JUMP` [`00bab3ec`](#insn-00bab3ec) → [`00bab408`](#insn-00bab408)
  - `FALL_THROUGH` [`00bab3ec`](#insn-00bab3ec) → [`00bab3f0`](#insn-00bab3f0)
- ブロック [`00bab3f0`](#insn-00bab3f0) 範囲 `[['00bab3f0', '00bab3f3']]`
  - `FALL_THROUGH` [`00bab3f0`](#insn-00bab3f0) → [`00bab3f4`](#insn-00bab3f4)
- ブロック [`00bab3f4`](#insn-00bab3f4) 範囲 `[['00bab3f4', '00bab407']]`
  - `UNCONDITIONAL_JUMP` [`00bab404`](#insn-00bab404) → [`00bab41c`](#insn-00bab41c)
- ブロック [`00bab408`](#insn-00bab408) 範囲 `[['00bab408', '00bab413']]`
  - `FALL_THROUGH` [`00bab410`](#insn-00bab410) → [`00bab414`](#insn-00bab414)
- ブロック [`00bab414`](#insn-00bab414) 範囲 `[['00bab414', '00bab41b']]`
  - `FALL_THROUGH` [`00bab418`](#insn-00bab418) → [`00bab41c`](#insn-00bab41c)
- ブロック [`00bab41c`](#insn-00bab41c) 範囲 `[['00bab41c', '00bab437']]`
  - `CONDITIONAL_JUMP` [`00bab434`](#insn-00bab434) → [`00bab44c`](#insn-00bab44c)
  - `FALL_THROUGH` [`00bab434`](#insn-00bab434) → [`00bab438`](#insn-00bab438)
- ブロック [`00bab438`](#insn-00bab438) 範囲 `[['00bab438', '00bab43f']]`
  - `CONDITIONAL_JUMP` [`00bab43c`](#insn-00bab43c) → [`00bab44c`](#insn-00bab44c)
  - `FALL_THROUGH` [`00bab43c`](#insn-00bab43c) → [`00bab440`](#insn-00bab440)
- ブロック [`00bab440`](#insn-00bab440) 範囲 `[['00bab440', '00bab44b']]`
  - `FALL_THROUGH` [`00bab448`](#insn-00bab448) → [`00bab44c`](#insn-00bab44c)
- ブロック [`00bab44c`](#insn-00bab44c) 範囲 `[['00bab44c', '00bab453']]`
  - `CONDITIONAL_JUMP` [`00bab450`](#insn-00bab450) → [`00bab458`](#insn-00bab458)
  - `FALL_THROUGH` [`00bab450`](#insn-00bab450) → [`00bab454`](#insn-00bab454)
- ブロック [`00bab454`](#insn-00bab454) 範囲 `[['00bab454', '00bab457']]`
  - `FALL_THROUGH` [`00bab454`](#insn-00bab454) → [`00bab458`](#insn-00bab458)
- ブロック [`00bab458`](#insn-00bab458) 範囲 `[['00bab458', '00bab45b']]`
  - `CONDITIONAL_JUMP` [`00bab458`](#insn-00bab458) → [`00bab460`](#insn-00bab460)
  - `FALL_THROUGH` [`00bab458`](#insn-00bab458) → [`00bab45c`](#insn-00bab45c)
- ブロック [`00bab45c`](#insn-00bab45c) 範囲 `[['00bab45c', '00bab45f']]`
  - `FALL_THROUGH` [`00bab45c`](#insn-00bab45c) → [`00bab460`](#insn-00bab460)
- ブロック [`00bab460`](#insn-00bab460) 範囲 `[['00bab460', '00bab463']]`
  - `FALL_THROUGH` [`00bab460`](#insn-00bab460) → [`00bab464`](#insn-00bab464)
- ブロック [`00bab464`](#insn-00bab464) 範囲 `[['00bab464', '00bab467']]`
  - `FALL_THROUGH` [`00bab464`](#insn-00bab464) → [`00bab468`](#insn-00bab468)
- ブロック [`00bab468`](#insn-00bab468) 範囲 `[['00bab468', '00bab46b']]`
  - `FALL_THROUGH` [`00bab468`](#insn-00bab468) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab46c`](#insn-00bab46c) 範囲 `[['00bab46c', '00bab47b']]`
  - `CONDITIONAL_JUMP` [`00bab478`](#insn-00bab478) → [`00bab8c0`](#insn-00bab8c0)
  - `FALL_THROUGH` [`00bab478`](#insn-00bab478) → [`00bab47c`](#insn-00bab47c)
- ブロック [`00bab47c`](#insn-00bab47c) 範囲 `[['00bab47c', '00bab48f']]`
- ブロック [`00bab490`](#insn-00bab490) 範囲 `[['00bab490', '00bab4ab']]`
  - `CONDITIONAL_JUMP` [`00bab4a8`](#insn-00bab4a8) → [`00bab6a4`](#insn-00bab6a4)
  - `FALL_THROUGH` [`00bab4a8`](#insn-00bab4a8) → [`00bab4ac`](#insn-00bab4ac)
- ブロック [`00bab4ac`](#insn-00bab4ac) 範囲 `[['00bab4ac', '00bab4af']]`
  - `FALL_THROUGH` [`00bab4ac`](#insn-00bab4ac) → [`00bab4b0`](#insn-00bab4b0)
- ブロック [`00bab4b0`](#insn-00bab4b0) 範囲 `[['00bab4b0', '00bab4b3']]`
  - `FALL_THROUGH` [`00bab4b0`](#insn-00bab4b0) → [`00bab4b4`](#insn-00bab4b4)
- ブロック [`00bab4b4`](#insn-00bab4b4) 範囲 `[['00bab4b4', '00bab4bf']]`
  - `CONDITIONAL_JUMP` [`00bab4bc`](#insn-00bab4bc) → [`00bab674`](#insn-00bab674)
  - `FALL_THROUGH` [`00bab4bc`](#insn-00bab4bc) → [`00bab4c0`](#insn-00bab4c0)
- ブロック [`00bab4c0`](#insn-00bab4c0) 範囲 `[['00bab4c0', '00bab4cb']]`
  - `CONDITIONAL_JUMP` [`00bab4c8`](#insn-00bab4c8) → [`00bab4b0`](#insn-00bab4b0)
  - `FALL_THROUGH` [`00bab4c8`](#insn-00bab4c8) → [`00bab4cc`](#insn-00bab4cc)
- ブロック [`00bab4cc`](#insn-00bab4cc) 範囲 `[['00bab4cc', '00bab4cf']]`
  - `UNCONDITIONAL_JUMP` [`00bab4cc`](#insn-00bab4cc) → [`00bab6a4`](#insn-00bab6a4)
- ブロック [`00bab4d0`](#insn-00bab4d0) 範囲 `[['00bab4d0', '00bab4df']]`
  - `FALL_THROUGH` [`00bab4dc`](#insn-00bab4dc) → [`00bab4e0`](#insn-00bab4e0)
- ブロック [`00bab4e0`](#insn-00bab4e0) 範囲 `[['00bab4e0', '00bab4eb']]`
  - `CONDITIONAL_JUMP` [`00bab4e8`](#insn-00bab4e8) → [`00bab724`](#insn-00bab724)
  - `FALL_THROUGH` [`00bab4e8`](#insn-00bab4e8) → [`00bab4ec`](#insn-00bab4ec)
- ブロック [`00bab4ec`](#insn-00bab4ec) 範囲 `[['00bab4ec', '00bab4ef']]`
  - `FALL_THROUGH` [`00bab4ec`](#insn-00bab4ec) → [`00bab4f0`](#insn-00bab4f0)
- ブロック [`00bab4f0`](#insn-00bab4f0) 範囲 `[['00bab4f0', '00bab4ff']]`
  - `CONDITIONAL_JUMP` [`00bab4fc`](#insn-00bab4fc) → [`00bab6f4`](#insn-00bab6f4)
  - `FALL_THROUGH` [`00bab4fc`](#insn-00bab4fc) → [`00bab500`](#insn-00bab500)
- ブロック [`00bab500`](#insn-00bab500) 範囲 `[['00bab500', '00bab503']]`
  - `FALL_THROUGH` [`00bab500`](#insn-00bab500) → [`00bab504`](#insn-00bab504)
- ブロック [`00bab504`](#insn-00bab504) 範囲 `[['00bab504', '00bab50b']]`
  - `CONDITIONAL_JUMP` [`00bab508`](#insn-00bab508) → [`00bab4f0`](#insn-00bab4f0)
  - `FALL_THROUGH` [`00bab508`](#insn-00bab508) → [`00bab50c`](#insn-00bab50c)
- ブロック [`00bab50c`](#insn-00bab50c) 範囲 `[['00bab50c', '00bab50f']]`
  - `UNCONDITIONAL_JUMP` [`00bab50c`](#insn-00bab50c) → [`00bab724`](#insn-00bab724)
- ブロック [`00bab510`](#insn-00bab510) 範囲 `[['00bab510', '00bab52b']]`
  - `CONDITIONAL_JUMP` [`00bab528`](#insn-00bab528) → [`00bab7b8`](#insn-00bab7b8)
  - `FALL_THROUGH` [`00bab528`](#insn-00bab528) → [`00bab52c`](#insn-00bab52c)
- ブロック [`00bab52c`](#insn-00bab52c) 範囲 `[['00bab52c', '00bab52f']]`
  - `FALL_THROUGH` [`00bab52c`](#insn-00bab52c) → [`00bab530`](#insn-00bab530)
- ブロック [`00bab530`](#insn-00bab530) 範囲 `[['00bab530', '00bab53f']]`
  - `CONDITIONAL_JUMP` [`00bab53c`](#insn-00bab53c) → [`00bab788`](#insn-00bab788)
  - `FALL_THROUGH` [`00bab53c`](#insn-00bab53c) → [`00bab540`](#insn-00bab540)
- ブロック [`00bab540`](#insn-00bab540) 範囲 `[['00bab540', '00bab54b']]`
  - `CONDITIONAL_JUMP` [`00bab548`](#insn-00bab548) → [`00bab530`](#insn-00bab530)
  - `FALL_THROUGH` [`00bab548`](#insn-00bab548) → [`00bab54c`](#insn-00bab54c)
- ブロック [`00bab54c`](#insn-00bab54c) 範囲 `[['00bab54c', '00bab54f']]`
  - `UNCONDITIONAL_JUMP` [`00bab54c`](#insn-00bab54c) → [`00bab7b8`](#insn-00bab7b8)
- ブロック [`00bab550`](#insn-00bab550) 範囲 `[['00bab550', '00bab557']]`
  - `CONDITIONAL_JUMP` [`00bab554`](#insn-00bab554) → [`00bab580`](#insn-00bab580)
  - `FALL_THROUGH` [`00bab554`](#insn-00bab554) → [`00bab558`](#insn-00bab558)
- ブロック [`00bab558`](#insn-00bab558) 範囲 `[['00bab558', '00bab567']]`
  - `CONDITIONAL_JUMP` [`00bab564`](#insn-00bab564) → [`00bab580`](#insn-00bab580)
  - `FALL_THROUGH` [`00bab564`](#insn-00bab564) → [`00bab568`](#insn-00bab568)
- ブロック [`00bab568`](#insn-00bab568) 範囲 `[['00bab568', '00bab577']]`
  - `FALL_THROUGH` [`00bab574`](#insn-00bab574) → [`00bab578`](#insn-00bab578)
- ブロック [`00bab578`](#insn-00bab578) 範囲 `[['00bab578', '00bab57f']]`
  - `UNCONDITIONAL_JUMP` [`00bab57c`](#insn-00bab57c) → [`00bab594`](#insn-00bab594)
- ブロック [`00bab580`](#insn-00bab580) 範囲 `[['00bab580', '00bab593']]`
  - `FALL_THROUGH` [`00bab590`](#insn-00bab590) → [`00bab594`](#insn-00bab594)
- ブロック [`00bab594`](#insn-00bab594) 範囲 `[['00bab594', '00bab5af']]`
  - `CONDITIONAL_JUMP` [`00bab5ac`](#insn-00bab5ac) → [`00bab824`](#insn-00bab824)
  - `FALL_THROUGH` [`00bab5ac`](#insn-00bab5ac) → [`00bab5b0`](#insn-00bab5b0)
- ブロック [`00bab5b0`](#insn-00bab5b0) 範囲 `[['00bab5b0', '00bab5b7']]`
  - `CONDITIONAL_JUMP` [`00bab5b4`](#insn-00bab5b4) → [`00bab824`](#insn-00bab824)
  - `FALL_THROUGH` [`00bab5b4`](#insn-00bab5b4) → [`00bab5b8`](#insn-00bab5b8)
- ブロック [`00bab5b8`](#insn-00bab5b8) 範囲 `[['00bab5b8', '00bab5bf']]`
  - `CONDITIONAL_JUMP` [`00bab5bc`](#insn-00bab5bc) → [`00bab818`](#insn-00bab818)
  - `FALL_THROUGH` [`00bab5bc`](#insn-00bab5bc) → [`00bab5c0`](#insn-00bab5c0)
- ブロック [`00bab5c0`](#insn-00bab5c0) 範囲 `[['00bab5c0', '00bab5cb']]`
  - `CONDITIONAL_JUMP` [`00bab5c8`](#insn-00bab5c8) → [`00bab82c`](#insn-00bab82c)
  - `FALL_THROUGH` [`00bab5c8`](#insn-00bab5c8) → [`00bab5cc`](#insn-00bab5cc)
- ブロック [`00bab5cc`](#insn-00bab5cc) 範囲 `[['00bab5cc', '00bab5cf']]`
  - `UNCONDITIONAL_JUMP` [`00bab5cc`](#insn-00bab5cc) → [`00bab830`](#insn-00bab830)
- ブロック [`00bab5d0`](#insn-00bab5d0) 範囲 `[['00bab5d0', '00bab5d7']]`
  - `CONDITIONAL_JUMP` [`00bab5d4`](#insn-00bab5d4) → [`00bab600`](#insn-00bab600)
  - `FALL_THROUGH` [`00bab5d4`](#insn-00bab5d4) → [`00bab5d8`](#insn-00bab5d8)
- ブロック [`00bab5d8`](#insn-00bab5d8) 範囲 `[['00bab5d8', '00bab5e7']]`
  - `CONDITIONAL_JUMP` [`00bab5e4`](#insn-00bab5e4) → [`00bab600`](#insn-00bab600)
  - `FALL_THROUGH` [`00bab5e4`](#insn-00bab5e4) → [`00bab5e8`](#insn-00bab5e8)
- ブロック [`00bab5e8`](#insn-00bab5e8) 範囲 `[['00bab5e8', '00bab5eb']]`
  - `FALL_THROUGH` [`00bab5e8`](#insn-00bab5e8) → [`00bab5ec`](#insn-00bab5ec)
- ブロック [`00bab5ec`](#insn-00bab5ec) 範囲 `[['00bab5ec', '00bab5fb']]`
  - `FALL_THROUGH` [`00bab5f8`](#insn-00bab5f8) → [`00bab5fc`](#insn-00bab5fc)
- ブロック [`00bab5fc`](#insn-00bab5fc) 範囲 `[['00bab5fc', '00bab5ff']]`
  - `UNCONDITIONAL_JUMP` [`00bab5fc`](#insn-00bab5fc) → [`00bab614`](#insn-00bab614)
- ブロック [`00bab600`](#insn-00bab600) 範囲 `[['00bab600', '00bab613']]`
  - `FALL_THROUGH` [`00bab610`](#insn-00bab610) → [`00bab614`](#insn-00bab614)
- ブロック [`00bab614`](#insn-00bab614) 範囲 `[['00bab614', '00bab62f']]`
  - `CONDITIONAL_JUMP` [`00bab62c`](#insn-00bab62c) → [`00bab654`](#insn-00bab654)
  - `FALL_THROUGH` [`00bab62c`](#insn-00bab62c) → [`00bab630`](#insn-00bab630)
- ブロック [`00bab630`](#insn-00bab630) 範囲 `[['00bab630', '00bab637']]`
  - `CONDITIONAL_JUMP` [`00bab634`](#insn-00bab634) → [`00bab654`](#insn-00bab654)
  - `FALL_THROUGH` [`00bab634`](#insn-00bab634) → [`00bab638`](#insn-00bab638)
- ブロック [`00bab638`](#insn-00bab638) 範囲 `[['00bab638', '00bab643']]`
  - `CONDITIONAL_JUMP` [`00bab640`](#insn-00bab640) → [`00bab654`](#insn-00bab654)
  - `FALL_THROUGH` [`00bab640`](#insn-00bab640) → [`00bab644`](#insn-00bab644)
- ブロック [`00bab644`](#insn-00bab644) 範囲 `[['00bab644', '00bab64f']]`
  - `FALL_THROUGH` [`00bab64c`](#insn-00bab64c) → [`00bab650`](#insn-00bab650)
- ブロック [`00bab650`](#insn-00bab650) 範囲 `[['00bab650', '00bab653']]`
  - `FALL_THROUGH` [`00bab650`](#insn-00bab650) → [`00bab654`](#insn-00bab654)
- ブロック [`00bab654`](#insn-00bab654) 範囲 `[['00bab654', '00bab65b']]`
  - `CONDITIONAL_JUMP` [`00bab658`](#insn-00bab658) → [`00bab660`](#insn-00bab660)
  - `FALL_THROUGH` [`00bab658`](#insn-00bab658) → [`00bab65c`](#insn-00bab65c)
- ブロック [`00bab65c`](#insn-00bab65c) 範囲 `[['00bab65c', '00bab65f']]`
  - `FALL_THROUGH` [`00bab65c`](#insn-00bab65c) → [`00bab660`](#insn-00bab660)
- ブロック [`00bab660`](#insn-00bab660) 範囲 `[['00bab660', '00bab663']]`
  - `CONDITIONAL_JUMP` [`00bab660`](#insn-00bab660) → [`00bab668`](#insn-00bab668)
  - `FALL_THROUGH` [`00bab660`](#insn-00bab660) → [`00bab664`](#insn-00bab664)
- ブロック [`00bab664`](#insn-00bab664) 範囲 `[['00bab664', '00bab667']]`
  - `FALL_THROUGH` [`00bab664`](#insn-00bab664) → [`00bab668`](#insn-00bab668)
- ブロック [`00bab668`](#insn-00bab668) 範囲 `[['00bab668', '00bab673']]`
  - `UNCONDITIONAL_JUMP` [`00bab670`](#insn-00bab670) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab674`](#insn-00bab674) 範囲 `[['00bab674', '00bab67b']]`
  - `CONDITIONAL_JUMP` [`00bab678`](#insn-00bab678) → [`00bab6a4`](#insn-00bab6a4)
  - `FALL_THROUGH` [`00bab678`](#insn-00bab678) → [`00bab67c`](#insn-00bab67c)
- ブロック [`00bab67c`](#insn-00bab67c) 範囲 `[['00bab67c', '00bab68b']]`
  - `CONDITIONAL_JUMP` [`00bab688`](#insn-00bab688) → [`00bab6a4`](#insn-00bab6a4)
  - `FALL_THROUGH` [`00bab688`](#insn-00bab688) → [`00bab68c`](#insn-00bab68c)
- ブロック [`00bab68c`](#insn-00bab68c) 範囲 `[['00bab68c', '00bab697']]`
  - `FALL_THROUGH` [`00bab694`](#insn-00bab694) → [`00bab698`](#insn-00bab698)
- ブロック [`00bab698`](#insn-00bab698) 範囲 `[['00bab698', '00bab6a3']]`
  - `UNCONDITIONAL_JUMP` [`00bab6a0`](#insn-00bab6a0) → [`00bab6b8`](#insn-00bab6b8)
- ブロック [`00bab6a4`](#insn-00bab6a4) 範囲 `[['00bab6a4', '00bab6b7']]`
  - `FALL_THROUGH` [`00bab6b4`](#insn-00bab6b4) → [`00bab6b8`](#insn-00bab6b8)
- ブロック [`00bab6b8`](#insn-00bab6b8) 範囲 `[['00bab6b8', '00bab6bb']]`
  - `FALL_THROUGH` [`00bab6b8`](#insn-00bab6b8) → [`00bab6bc`](#insn-00bab6bc)
- ブロック [`00bab6bc`](#insn-00bab6bc) 範囲 `[['00bab6bc', '00bab6cf']]`
  - `FALL_THROUGH` [`00bab6cc`](#insn-00bab6cc) → [`00bab6d0`](#insn-00bab6d0)
- ブロック [`00bab6d0`](#insn-00bab6d0) 範囲 `[['00bab6d0', '00bab6d3']]`
  - `CONDITIONAL_JUMP` [`00bab6d0`](#insn-00bab6d0) → [`00bab854`](#insn-00bab854)
  - `FALL_THROUGH` [`00bab6d0`](#insn-00bab6d0) → [`00bab6d4`](#insn-00bab6d4)
- ブロック [`00bab6d4`](#insn-00bab6d4) 範囲 `[['00bab6d4', '00bab6db']]`
  - `CONDITIONAL_JUMP` [`00bab6d8`](#insn-00bab6d8) → [`00bab854`](#insn-00bab854)
  - `FALL_THROUGH` [`00bab6d8`](#insn-00bab6d8) → [`00bab6dc`](#insn-00bab6dc)
- ブロック [`00bab6dc`](#insn-00bab6dc) 範囲 `[['00bab6dc', '00bab6e3']]`
  - `CONDITIONAL_JUMP` [`00bab6e0`](#insn-00bab6e0) → [`00bab848`](#insn-00bab848)
  - `FALL_THROUGH` [`00bab6e0`](#insn-00bab6e0) → [`00bab6e4`](#insn-00bab6e4)
- ブロック [`00bab6e4`](#insn-00bab6e4) 範囲 `[['00bab6e4', '00bab6ef']]`
  - `CONDITIONAL_JUMP` [`00bab6ec`](#insn-00bab6ec) → [`00bab85c`](#insn-00bab85c)
  - `FALL_THROUGH` [`00bab6ec`](#insn-00bab6ec) → [`00bab6f0`](#insn-00bab6f0)
- ブロック [`00bab6f0`](#insn-00bab6f0) 範囲 `[['00bab6f0', '00bab6f3']]`
  - `UNCONDITIONAL_JUMP` [`00bab6f0`](#insn-00bab6f0) → [`00bab860`](#insn-00bab860)
- ブロック [`00bab6f4`](#insn-00bab6f4) 範囲 `[['00bab6f4', '00bab6fb']]`
  - `CONDITIONAL_JUMP` [`00bab6f8`](#insn-00bab6f8) → [`00bab724`](#insn-00bab724)
  - `FALL_THROUGH` [`00bab6f8`](#insn-00bab6f8) → [`00bab6fc`](#insn-00bab6fc)
- ブロック [`00bab6fc`](#insn-00bab6fc) 範囲 `[['00bab6fc', '00bab70b']]`
  - `CONDITIONAL_JUMP` [`00bab708`](#insn-00bab708) → [`00bab724`](#insn-00bab724)
  - `FALL_THROUGH` [`00bab708`](#insn-00bab708) → [`00bab70c`](#insn-00bab70c)
- ブロック [`00bab70c`](#insn-00bab70c) 範囲 `[['00bab70c', '00bab70f']]`
  - `FALL_THROUGH` [`00bab70c`](#insn-00bab70c) → [`00bab710`](#insn-00bab710)
- ブロック [`00bab710`](#insn-00bab710) 範囲 `[['00bab710', '00bab723']]`
  - `UNCONDITIONAL_JUMP` [`00bab720`](#insn-00bab720) → [`00bab738`](#insn-00bab738)
- ブロック [`00bab724`](#insn-00bab724) 範囲 `[['00bab724', '00bab737']]`
  - `FALL_THROUGH` [`00bab734`](#insn-00bab734) → [`00bab738`](#insn-00bab738)
- ブロック [`00bab738`](#insn-00bab738) 範囲 `[['00bab738', '00bab73b']]`
  - `FALL_THROUGH` [`00bab738`](#insn-00bab738) → [`00bab73c`](#insn-00bab73c)
- ブロック [`00bab73c`](#insn-00bab73c) 範囲 `[['00bab73c', '00bab753']]`
  - `CONDITIONAL_JUMP` [`00bab750`](#insn-00bab750) → [`00bab768`](#insn-00bab768)
  - `FALL_THROUGH` [`00bab750`](#insn-00bab750) → [`00bab754`](#insn-00bab754)
- ブロック [`00bab754`](#insn-00bab754) 範囲 `[['00bab754', '00bab75b']]`
  - `CONDITIONAL_JUMP` [`00bab758`](#insn-00bab758) → [`00bab768`](#insn-00bab768)
  - `FALL_THROUGH` [`00bab758`](#insn-00bab758) → [`00bab75c`](#insn-00bab75c)
- ブロック [`00bab75c`](#insn-00bab75c) 範囲 `[['00bab75c', '00bab75f']]`
  - `FALL_THROUGH` [`00bab75c`](#insn-00bab75c) → [`00bab760`](#insn-00bab760)
- ブロック [`00bab760`](#insn-00bab760) 範囲 `[['00bab760', '00bab767']]`
  - `FALL_THROUGH` [`00bab764`](#insn-00bab764) → [`00bab768`](#insn-00bab768)
- ブロック [`00bab768`](#insn-00bab768) 範囲 `[['00bab768', '00bab76f']]`
  - `CONDITIONAL_JUMP` [`00bab76c`](#insn-00bab76c) → [`00bab774`](#insn-00bab774)
  - `FALL_THROUGH` [`00bab76c`](#insn-00bab76c) → [`00bab770`](#insn-00bab770)
- ブロック [`00bab770`](#insn-00bab770) 範囲 `[['00bab770', '00bab773']]`
  - `FALL_THROUGH` [`00bab770`](#insn-00bab770) → [`00bab774`](#insn-00bab774)
- ブロック [`00bab774`](#insn-00bab774) 範囲 `[['00bab774', '00bab777']]`
  - `CONDITIONAL_JUMP` [`00bab774`](#insn-00bab774) → [`00bab77c`](#insn-00bab77c)
  - `FALL_THROUGH` [`00bab774`](#insn-00bab774) → [`00bab778`](#insn-00bab778)
- ブロック [`00bab778`](#insn-00bab778) 範囲 `[['00bab778', '00bab77b']]`
  - `FALL_THROUGH` [`00bab778`](#insn-00bab778) → [`00bab77c`](#insn-00bab77c)
- ブロック [`00bab77c`](#insn-00bab77c) 範囲 `[['00bab77c', '00bab787']]`
  - `UNCONDITIONAL_JUMP` [`00bab784`](#insn-00bab784) → [`00bab468`](#insn-00bab468)
- ブロック [`00bab788`](#insn-00bab788) 範囲 `[['00bab788', '00bab78b']]`
  - `FALL_THROUGH` [`00bab788`](#insn-00bab788) → [`00bab78c`](#insn-00bab78c)
- ブロック [`00bab78c`](#insn-00bab78c) 範囲 `[['00bab78c', '00bab78f']]`
  - `CONDITIONAL_JUMP` [`00bab78c`](#insn-00bab78c) → [`00bab7b8`](#insn-00bab7b8)
  - `FALL_THROUGH` [`00bab78c`](#insn-00bab78c) → [`00bab790`](#insn-00bab790)
- ブロック [`00bab790`](#insn-00bab790) 範囲 `[['00bab790', '00bab79f']]`
  - `CONDITIONAL_JUMP` [`00bab79c`](#insn-00bab79c) → [`00bab7b8`](#insn-00bab7b8)
  - `FALL_THROUGH` [`00bab79c`](#insn-00bab79c) → [`00bab7a0`](#insn-00bab7a0)
- ブロック [`00bab7a0`](#insn-00bab7a0) 範囲 `[['00bab7a0', '00bab7ab']]`
  - `FALL_THROUGH` [`00bab7a8`](#insn-00bab7a8) → [`00bab7ac`](#insn-00bab7ac)
- ブロック [`00bab7ac`](#insn-00bab7ac) 範囲 `[['00bab7ac', '00bab7b7']]`
  - `UNCONDITIONAL_JUMP` [`00bab7b4`](#insn-00bab7b4) → [`00bab7cc`](#insn-00bab7cc)
- ブロック [`00bab7b8`](#insn-00bab7b8) 範囲 `[['00bab7b8', '00bab7cb']]`
  - `FALL_THROUGH` [`00bab7c8`](#insn-00bab7c8) → [`00bab7cc`](#insn-00bab7cc)
- ブロック [`00bab7cc`](#insn-00bab7cc) 範囲 `[['00bab7cc', '00bab7d7']]`
  - `FALL_THROUGH` [`00bab7d4`](#insn-00bab7d4) → [`00bab7d8`](#insn-00bab7d8)
- ブロック [`00bab7d8`](#insn-00bab7d8) 範囲 `[['00bab7d8', '00bab7e7']]`
  - `CONDITIONAL_JUMP` [`00bab7e4`](#insn-00bab7e4) → [`00bab7fc`](#insn-00bab7fc)
  - `FALL_THROUGH` [`00bab7e4`](#insn-00bab7e4) → [`00bab7e8`](#insn-00bab7e8)
- ブロック [`00bab7e8`](#insn-00bab7e8) 範囲 `[['00bab7e8', '00bab7ef']]`
  - `CONDITIONAL_JUMP` [`00bab7ec`](#insn-00bab7ec) → [`00bab7fc`](#insn-00bab7fc)
  - `FALL_THROUGH` [`00bab7ec`](#insn-00bab7ec) → [`00bab7f0`](#insn-00bab7f0)
- ブロック [`00bab7f0`](#insn-00bab7f0) 範囲 `[['00bab7f0', '00bab7fb']]`
  - `FALL_THROUGH` [`00bab7f8`](#insn-00bab7f8) → [`00bab7fc`](#insn-00bab7fc)
- ブロック [`00bab7fc`](#insn-00bab7fc) 範囲 `[['00bab7fc', '00bab803']]`
  - `CONDITIONAL_JUMP` [`00bab800`](#insn-00bab800) → [`00bab808`](#insn-00bab808)
  - `FALL_THROUGH` [`00bab800`](#insn-00bab800) → [`00bab804`](#insn-00bab804)
- ブロック [`00bab804`](#insn-00bab804) 範囲 `[['00bab804', '00bab807']]`
  - `FALL_THROUGH` [`00bab804`](#insn-00bab804) → [`00bab808`](#insn-00bab808)
- ブロック [`00bab808`](#insn-00bab808) 範囲 `[['00bab808', '00bab80b']]`
  - `CONDITIONAL_JUMP` [`00bab808`](#insn-00bab808) → [`00bab810`](#insn-00bab810)
  - `FALL_THROUGH` [`00bab808`](#insn-00bab808) → [`00bab80c`](#insn-00bab80c)
- ブロック [`00bab80c`](#insn-00bab80c) 範囲 `[['00bab80c', '00bab80f']]`
  - `FALL_THROUGH` [`00bab80c`](#insn-00bab80c) → [`00bab810`](#insn-00bab810)
- ブロック [`00bab810`](#insn-00bab810) 範囲 `[['00bab810', '00bab817']]`
  - `UNCONDITIONAL_JUMP` [`00bab814`](#insn-00bab814) → [`00bab468`](#insn-00bab468)
- ブロック [`00bab818`](#insn-00bab818) 範囲 `[['00bab818', '00bab823']]`
  - `FALL_THROUGH` [`00bab820`](#insn-00bab820) → [`00bab824`](#insn-00bab824)
- ブロック [`00bab824`](#insn-00bab824) 範囲 `[['00bab824', '00bab827']]`
  - `FALL_THROUGH` [`00bab824`](#insn-00bab824) → [`00bab828`](#insn-00bab828)
- ブロック [`00bab828`](#insn-00bab828) 範囲 `[['00bab828', '00bab82b']]`
  - `CONDITIONAL_JUMP` [`00bab828`](#insn-00bab828) → [`00bab830`](#insn-00bab830)
  - `FALL_THROUGH` [`00bab828`](#insn-00bab828) → [`00bab82c`](#insn-00bab82c)
- ブロック [`00bab82c`](#insn-00bab82c) 範囲 `[['00bab82c', '00bab82f']]`
  - `FALL_THROUGH` [`00bab82c`](#insn-00bab82c) → [`00bab830`](#insn-00bab830)
- ブロック [`00bab830`](#insn-00bab830) 範囲 `[['00bab830', '00bab833']]`
  - `CONDITIONAL_JUMP` [`00bab830`](#insn-00bab830) → [`00bab838`](#insn-00bab838)
  - `FALL_THROUGH` [`00bab830`](#insn-00bab830) → [`00bab834`](#insn-00bab834)
- ブロック [`00bab834`](#insn-00bab834) 範囲 `[['00bab834', '00bab837']]`
  - `FALL_THROUGH` [`00bab834`](#insn-00bab834) → [`00bab838`](#insn-00bab838)
- ブロック [`00bab838`](#insn-00bab838) 範囲 `[['00bab838', '00bab847']]`
  - `UNCONDITIONAL_JUMP` [`00bab844`](#insn-00bab844) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab848`](#insn-00bab848) 範囲 `[['00bab848', '00bab84b']]`
  - `FALL_THROUGH` [`00bab848`](#insn-00bab848) → [`00bab84c`](#insn-00bab84c)
- ブロック [`00bab84c`](#insn-00bab84c) 範囲 `[['00bab84c', '00bab853']]`
  - `FALL_THROUGH` [`00bab850`](#insn-00bab850) → [`00bab854`](#insn-00bab854)
- ブロック [`00bab854`](#insn-00bab854) 範囲 `[['00bab854', '00bab85b']]`
  - `CONDITIONAL_JUMP` [`00bab858`](#insn-00bab858) → [`00bab860`](#insn-00bab860)
  - `FALL_THROUGH` [`00bab858`](#insn-00bab858) → [`00bab85c`](#insn-00bab85c)
- ブロック [`00bab85c`](#insn-00bab85c) 範囲 `[['00bab85c', '00bab85f']]`
  - `FALL_THROUGH` [`00bab85c`](#insn-00bab85c) → [`00bab860`](#insn-00bab860)
- ブロック [`00bab860`](#insn-00bab860) 範囲 `[['00bab860', '00bab863']]`
  - `CONDITIONAL_JUMP` [`00bab860`](#insn-00bab860) → [`00bab868`](#insn-00bab868)
  - `FALL_THROUGH` [`00bab860`](#insn-00bab860) → [`00bab864`](#insn-00bab864)
- ブロック [`00bab864`](#insn-00bab864) 範囲 `[['00bab864', '00bab867']]`
  - `FALL_THROUGH` [`00bab864`](#insn-00bab864) → [`00bab868`](#insn-00bab868)
- ブロック [`00bab868`](#insn-00bab868) 範囲 `[['00bab868', '00bab877']]`
  - `UNCONDITIONAL_JUMP` [`00bab874`](#insn-00bab874) → [`00bab46c`](#insn-00bab46c)
- ブロック [`00bab878`](#insn-00bab878) 範囲 `[['00bab878', '00bab87b']]`
  - `FALL_THROUGH` [`00bab878`](#insn-00bab878) → [`00bab87c`](#insn-00bab87c)
- ブロック [`00bab87c`](#insn-00bab87c) 範囲 `[['00bab87c', '00bab893']]`
  - `CONDITIONAL_JUMP` [`00bab890`](#insn-00bab890) → [`00bab89c`](#insn-00bab89c)
  - `FALL_THROUGH` [`00bab890`](#insn-00bab890) → [`00bab894`](#insn-00bab894)
- ブロック [`00bab894`](#insn-00bab894) 範囲 `[['00bab894', '00bab89b']]`
  - `FALL_THROUGH` [`00bab898`](#insn-00bab898) → [`00bab89c`](#insn-00bab89c)
- ブロック [`00bab89c`](#insn-00bab89c) 範囲 `[['00bab89c', '00bab8bf']]`
  - `UNCONDITIONAL_JUMP` [`00bab8bc`](#insn-00bab8bc) → [`00bab468`](#insn-00bab468)
- ブロック [`00bab8c0`](#insn-00bab8c0) 範囲 `[['00bab8c0', '00bab8c3']]`

## 命令位置別の参照

- [`00baafac`](#insn-00baafac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb0`](#insn-00baafb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb4`](#insn-00baafb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc4`](#insn-00baafc4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafd0`](#insn-00baafd0) → [`00bab248`](#insn-00bab248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baaff0::default` · 推定型 `None`
- [`00baafe0`](#insn-00baafe0) → `0030e233`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::switchdataD_0030e233` · 推定型 `byte`
- [`00baaff0`](#insn-00baaff0) → [`00baaff4`](#insn-00baaff4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_0` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab250`](#insn-00bab250) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_1` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab1d0`](#insn-00bab1d0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_2` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab218`](#insn-00bab218) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_3` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab0b4`](#insn-00bab0b4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_4` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab268`](#insn-00bab268) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_5` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab280`](#insn-00bab280) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_6` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab230`](#insn-00bab230) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_7` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab298`](#insn-00bab298) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_8` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab0fc`](#insn-00bab0fc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_9` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab2b0`](#insn-00bab2b0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_a` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab03c`](#insn-00bab03c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_b` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00bab154`](#insn-00bab154) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaff0::caseD_c` · 推定型 `None`
- [`00baaff4`](#insn-00baaff4) → [`00baaffc`](#insn-00baaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaff8`](#insn-00baaff8) → [`00bab258`](#insn-00bab258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab014`](#insn-00bab014) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab028`](#insn-00bab028) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab034`](#insn-00bab034) → [`00bab01c`](#insn-00bab01c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab038`](#insn-00bab038) → [`00bab408`](#insn-00bab408) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab03c`](#insn-00bab03c) → [`00bab048`](#insn-00bab048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab044`](#insn-00bab044) → [`00bab098`](#insn-00bab098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab068`](#insn-00bab068) → [`00c58680`](../00c58/00c58680.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58680` · 推定シンボル `None` · 推定型 `None`
- [`00bab06c`](#insn-00bab06c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab078`](#insn-00bab078) → [`00bab098`](#insn-00bab098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab080`](#insn-00bab080) → [`00bab098`](#insn-00bab098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab08c`](#insn-00bab08c) → [`00bab098`](#insn-00bab098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab09c`](#insn-00bab09c) → [`00bab0a4`](#insn-00bab0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a4`](#insn-00bab0a4) → [`00bab0ac`](#insn-00bab0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b0`](#insn-00bab0b0) → [`00bab1c8`](#insn-00bab1c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b4`](#insn-00bab0b4) → [`00bab0bc`](#insn-00bab0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b8`](#insn-00bab0b8) → [`00bab258`](#insn-00bab258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0d4`](#insn-00bab0d4) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e8`](#insn-00bab0e8) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f4`](#insn-00bab0f4) → [`00bab0dc`](#insn-00bab0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f8`](#insn-00bab0f8) → [`00bab408`](#insn-00bab408) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0fc`](#insn-00bab0fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab100`](#insn-00bab100) → [`00bab108`](#insn-00bab108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab104`](#insn-00bab104) → [`00bab12c`](#insn-00bab12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab128`](#insn-00bab128) → [`00c5c280`](../00c5c/00c5c280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c280` · 推定シンボル `None` · 推定型 `None`
- [`00bab140`](#insn-00bab140) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab144`](#insn-00bab144) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab150`](#insn-00bab150) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab154`](#insn-00bab154) → [`00bab160`](#insn-00bab160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab15c`](#insn-00bab15c) → [`00bab1b0`](#insn-00bab1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab17c`](#insn-00bab17c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab180`](#insn-00bab180) → [`00c58690`](../00c58/00c58690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58690` · 推定シンボル `None` · 推定型 `None`
- [`00bab184`](#insn-00bab184) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab190`](#insn-00bab190) → [`00bab1b0`](#insn-00bab1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab198`](#insn-00bab198) → [`00bab1b0`](#insn-00bab1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1a4`](#insn-00bab1a4) → [`00bab1b0`](#insn-00bab1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b4`](#insn-00bab1b4) → [`00bab1bc`](#insn-00bab1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1bc`](#insn-00bab1bc) → [`00bab1c4`](#insn-00bab1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1cc`](#insn-00bab1cc) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1d0`](#insn-00bab1d0) → [`00bab1d8`](#insn-00bab1d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1d4`](#insn-00bab1d4) → [`00bab258`](#insn-00bab258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f0`](#insn-00bab1f0) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab204`](#insn-00bab204) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab210`](#insn-00bab210) → [`00bab1f8`](#insn-00bab1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab214`](#insn-00bab214) → [`00bab408`](#insn-00bab408) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab218`](#insn-00bab218) → [`00bab318`](#insn-00bab318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab21c`](#insn-00bab21c) → [`00bab318`](#insn-00bab318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab228`](#insn-00bab228) → [`00bab82c`](#insn-00bab82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab22c`](#insn-00bab22c) → [`00bab830`](#insn-00bab830) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab230`](#insn-00bab230) → [`00bab358`](#insn-00bab358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab234`](#insn-00bab234) → [`00bab358`](#insn-00bab358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab240`](#insn-00bab240) → [`00bab65c`](#insn-00bab65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab244`](#insn-00bab244) → [`00bab660`](#insn-00bab660) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab24c`](#insn-00bab24c) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab250`](#insn-00bab250) → [`00bab398`](#insn-00bab398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab254`](#insn-00bab254) → [`00bab398`](#insn-00bab398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab260`](#insn-00bab260) → [`00bab454`](#insn-00bab454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab264`](#insn-00bab264) → [`00bab458`](#insn-00bab458) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab268`](#insn-00bab268) → [`00bab490`](#insn-00bab490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab26c`](#insn-00bab26c) → [`00bab490`](#insn-00bab490) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab278`](#insn-00bab278) → [`00bab85c`](#insn-00bab85c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab27c`](#insn-00bab27c) → [`00bab860`](#insn-00bab860) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab280`](#insn-00bab280) → [`00bab4d0`](#insn-00bab4d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab284`](#insn-00bab284) → [`00bab4d0`](#insn-00bab4d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab290`](#insn-00bab290) → [`00bab770`](#insn-00bab770) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab294`](#insn-00bab294) → [`00bab774`](#insn-00bab774) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab298`](#insn-00bab298) → [`00bab510`](#insn-00bab510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab29c`](#insn-00bab29c) → [`00bab510`](#insn-00bab510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2a8`](#insn-00bab2a8) → [`00bab804`](#insn-00bab804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2ac`](#insn-00bab2ac) → [`00bab808`](#insn-00bab808) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b0`](#insn-00bab2b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b4`](#insn-00bab2b4) → [`00bab2bc`](#insn-00bab2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b8`](#insn-00bab2b8) → [`00bab89c`](#insn-00bab89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e0`](#insn-00bab2e0) → [`00c5c290`](../00c5c/00c5c290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c290` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e4`](#insn-00bab2e4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e8`](#insn-00bab2e8) → [`00bab89c`](#insn-00bab89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2ec`](#insn-00bab2ec) → [`00bab89c`](#insn-00bab89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f4`](#insn-00bab2f4) → [`00bab878`](#insn-00bab878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab308`](#insn-00bab308) → [`00bab87c`](#insn-00bab87c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab310`](#insn-00bab310) → [`00bab2fc`](#insn-00bab2fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab314`](#insn-00bab314) → [`00bab87c`](#insn-00bab87c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab330`](#insn-00bab330) → [`00bab580`](#insn-00bab580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab344`](#insn-00bab344) → [`00bab550`](#insn-00bab550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab350`](#insn-00bab350) → [`00bab338`](#insn-00bab338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab354`](#insn-00bab354) → [`00bab580`](#insn-00bab580) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab370`](#insn-00bab370) → [`00bab600`](#insn-00bab600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab384`](#insn-00bab384) → [`00bab5d0`](#insn-00bab5d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab390`](#insn-00bab390) → [`00bab378`](#insn-00bab378) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab394`](#insn-00bab394) → [`00bab600`](#insn-00bab600) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3b0`](#insn-00bab3b0) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3c4`](#insn-00bab3c4) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3d0`](#insn-00bab3d0) → [`00bab3b8`](#insn-00bab3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3d4`](#insn-00bab3d4) → [`00bab408`](#insn-00bab408) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3dc`](#insn-00bab3dc) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3ec`](#insn-00bab3ec) → [`00bab408`](#insn-00bab408) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f4`](#insn-00bab3f4) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab400`](#insn-00bab400) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab404`](#insn-00bab404) → [`00bab41c`](#insn-00bab41c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab40c`](#insn-00bab40c) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab410`](#insn-00bab410) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab41c`](#insn-00bab41c) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab424`](#insn-00bab424) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab428`](#insn-00bab428) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab434`](#insn-00bab434) → [`00bab44c`](#insn-00bab44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab43c`](#insn-00bab43c) → [`00bab44c`](#insn-00bab44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab450`](#insn-00bab450) → [`00bab458`](#insn-00bab458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab458`](#insn-00bab458) → [`00bab460`](#insn-00bab460) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab470`](#insn-00bab470) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab478`](#insn-00bab478) → [`00bab8c0`](#insn-00bab8c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab47c`](#insn-00bab47c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab480`](#insn-00bab480) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab484`](#insn-00bab484) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4a8`](#insn-00bab4a8) → [`00bab6a4`](#insn-00bab6a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4bc`](#insn-00bab4bc) → [`00bab674`](#insn-00bab674) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4c8`](#insn-00bab4c8) → [`00bab4b0`](#insn-00bab4b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4cc`](#insn-00bab4cc) → [`00bab6a4`](#insn-00bab6a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4e8`](#insn-00bab4e8) → [`00bab724`](#insn-00bab724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4fc`](#insn-00bab4fc) → [`00bab6f4`](#insn-00bab6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab508`](#insn-00bab508) → [`00bab4f0`](#insn-00bab4f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab50c`](#insn-00bab50c) → [`00bab724`](#insn-00bab724) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab528`](#insn-00bab528) → [`00bab7b8`](#insn-00bab7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab53c`](#insn-00bab53c) → [`00bab788`](#insn-00bab788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab548`](#insn-00bab548) → [`00bab530`](#insn-00bab530) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab54c`](#insn-00bab54c) → [`00bab7b8`](#insn-00bab7b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab554`](#insn-00bab554) → [`00bab580`](#insn-00bab580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab564`](#insn-00bab564) → [`00bab580`](#insn-00bab580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab56c`](#insn-00bab56c) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab578`](#insn-00bab578) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab57c`](#insn-00bab57c) → [`00bab594`](#insn-00bab594) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab584`](#insn-00bab584) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab588`](#insn-00bab588) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab594`](#insn-00bab594) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab59c`](#insn-00bab59c) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab5a0`](#insn-00bab5a0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5ac`](#insn-00bab5ac) → [`00bab824`](#insn-00bab824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5b4`](#insn-00bab5b4) → [`00bab824`](#insn-00bab824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5bc`](#insn-00bab5bc) → [`00bab818`](#insn-00bab818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5c8`](#insn-00bab5c8) → [`00bab82c`](#insn-00bab82c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5cc`](#insn-00bab5cc) → [`00bab830`](#insn-00bab830) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5d4`](#insn-00bab5d4) → [`00bab600`](#insn-00bab600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5e4`](#insn-00bab5e4) → [`00bab600`](#insn-00bab600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5ec`](#insn-00bab5ec) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab5f8`](#insn-00bab5f8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5fc`](#insn-00bab5fc) → [`00bab614`](#insn-00bab614) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab604`](#insn-00bab604) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab608`](#insn-00bab608) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab614`](#insn-00bab614) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab61c`](#insn-00bab61c) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab620`](#insn-00bab620) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab62c`](#insn-00bab62c) → [`00bab654`](#insn-00bab654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab634`](#insn-00bab634) → [`00bab654`](#insn-00bab654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab640`](#insn-00bab640) → [`00bab654`](#insn-00bab654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab658`](#insn-00bab658) → [`00bab660`](#insn-00bab660) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab660`](#insn-00bab660) → [`00bab668`](#insn-00bab668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab670`](#insn-00bab670) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab678`](#insn-00bab678) → [`00bab6a4`](#insn-00bab6a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab688`](#insn-00bab688) → [`00bab6a4`](#insn-00bab6a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab690`](#insn-00bab690) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab69c`](#insn-00bab69c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6a0`](#insn-00bab6a0) → [`00bab6b8`](#insn-00bab6b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6a8`](#insn-00bab6a8) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab6ac`](#insn-00bab6ac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6b8`](#insn-00bab6b8) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab6c0`](#insn-00bab6c0) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab6c4`](#insn-00bab6c4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d0`](#insn-00bab6d0) → [`00bab854`](#insn-00bab854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d8`](#insn-00bab6d8) → [`00bab854`](#insn-00bab854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6e0`](#insn-00bab6e0) → [`00bab848`](#insn-00bab848) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6ec`](#insn-00bab6ec) → [`00bab85c`](#insn-00bab85c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6f0`](#insn-00bab6f0) → [`00bab860`](#insn-00bab860) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6f8`](#insn-00bab6f8) → [`00bab724`](#insn-00bab724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab708`](#insn-00bab708) → [`00bab724`](#insn-00bab724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab710`](#insn-00bab710) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab71c`](#insn-00bab71c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab720`](#insn-00bab720) → [`00bab738`](#insn-00bab738) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab728`](#insn-00bab728) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab72c`](#insn-00bab72c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab738`](#insn-00bab738) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab740`](#insn-00bab740) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab744`](#insn-00bab744) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab750`](#insn-00bab750) → [`00bab768`](#insn-00bab768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab758`](#insn-00bab758) → [`00bab768`](#insn-00bab768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab76c`](#insn-00bab76c) → [`00bab774`](#insn-00bab774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab774`](#insn-00bab774) → [`00bab77c`](#insn-00bab77c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab784`](#insn-00bab784) → [`00bab468`](#insn-00bab468) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab78c`](#insn-00bab78c) → [`00bab7b8`](#insn-00bab7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab79c`](#insn-00bab79c) → [`00bab7b8`](#insn-00bab7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7a4`](#insn-00bab7a4) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab7b0`](#insn-00bab7b0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7b4`](#insn-00bab7b4) → [`00bab7cc`](#insn-00bab7cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7bc`](#insn-00bab7bc) → `00c9b900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab7c0`](#insn-00bab7c0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7cc`](#insn-00bab7cc) → `011262e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab7d4`](#insn-00bab7d4) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00bab7d8`](#insn-00bab7d8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7e4`](#insn-00bab7e4) → [`00bab7fc`](#insn-00bab7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7ec`](#insn-00bab7ec) → [`00bab7fc`](#insn-00bab7fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab800`](#insn-00bab800) → [`00bab808`](#insn-00bab808) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab808`](#insn-00bab808) → [`00bab810`](#insn-00bab810) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab814`](#insn-00bab814) → [`00bab468`](#insn-00bab468) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab828`](#insn-00bab828) → [`00bab830`](#insn-00bab830) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab830`](#insn-00bab830) → [`00bab838`](#insn-00bab838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab844`](#insn-00bab844) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab858`](#insn-00bab858) → [`00bab860`](#insn-00bab860) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab860`](#insn-00bab860) → [`00bab868`](#insn-00bab868) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab874`](#insn-00bab874) → [`00bab46c`](#insn-00bab46c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab890`](#insn-00bab890) → [`00bab89c`](#insn-00bab89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab898`](#insn-00bab898) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8b0`](#insn-00bab8b0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8b4`](#insn-00bab8b4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8bc`](#insn-00bab8bc) → [`00bab468`](#insn-00bab468) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab8c0`](#insn-00bab8c0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baafac`](#insn-00baafac)

~~~json
{
  "source": "00baafac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb0`](#insn-00baafb0)

~~~json
{
  "source": "00baafb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb4`](#insn-00baafb4)

~~~json
{
  "source": "00baafb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc4`](#insn-00baafc4)

~~~json
{
  "source": "00baafc4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafd0`](#insn-00baafd0)

~~~json
{
  "source": "00baafd0",
  "target": "00bab248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafe0`](#insn-00baafe0)

~~~json
{
  "source": "00baafe0",
  "target": "0030e233",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e233",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e233",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00baaff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab250",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00bab154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff4`](#insn-00baaff4)

~~~json
{
  "source": "00baaff4",
  "target": "00baaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff8`](#insn-00baaff8)

~~~json
{
  "source": "00baaff8",
  "target": "00bab258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab014`](#insn-00bab014)

~~~json
{
  "source": "00bab014",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab028`](#insn-00bab028)

~~~json
{
  "source": "00bab028",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab034`](#insn-00bab034)

~~~json
{
  "source": "00bab034",
  "target": "00bab01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab038`](#insn-00bab038)

~~~json
{
  "source": "00bab038",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab03c`](#insn-00bab03c)

~~~json
{
  "source": "00bab03c",
  "target": "00bab048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab044`](#insn-00bab044)

~~~json
{
  "source": "00bab044",
  "target": "00bab098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab068`](#insn-00bab068)

~~~json
{
  "source": "00bab068",
  "target": "00c58680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab06c`](#insn-00bab06c)

~~~json
{
  "source": "00bab06c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab078`](#insn-00bab078)

~~~json
{
  "source": "00bab078",
  "target": "00bab098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab080`](#insn-00bab080)

~~~json
{
  "source": "00bab080",
  "target": "00bab098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab08c`](#insn-00bab08c)

~~~json
{
  "source": "00bab08c",
  "target": "00bab098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab09c`](#insn-00bab09c)

~~~json
{
  "source": "00bab09c",
  "target": "00bab0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0a4`](#insn-00bab0a4)

~~~json
{
  "source": "00bab0a4",
  "target": "00bab0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b0`](#insn-00bab0b0)

~~~json
{
  "source": "00bab0b0",
  "target": "00bab1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b4`](#insn-00bab0b4)

~~~json
{
  "source": "00bab0b4",
  "target": "00bab0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b8`](#insn-00bab0b8)

~~~json
{
  "source": "00bab0b8",
  "target": "00bab258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0d4`](#insn-00bab0d4)

~~~json
{
  "source": "00bab0d4",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0e8`](#insn-00bab0e8)

~~~json
{
  "source": "00bab0e8",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f4`](#insn-00bab0f4)

~~~json
{
  "source": "00bab0f4",
  "target": "00bab0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f8`](#insn-00bab0f8)

~~~json
{
  "source": "00bab0f8",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0fc`](#insn-00bab0fc)

~~~json
{
  "source": "00bab0fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab100`](#insn-00bab100)

~~~json
{
  "source": "00bab100",
  "target": "00bab108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab104`](#insn-00bab104)

~~~json
{
  "source": "00bab104",
  "target": "00bab12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab128`](#insn-00bab128)

~~~json
{
  "source": "00bab128",
  "target": "00c5c280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab140`](#insn-00bab140)

~~~json
{
  "source": "00bab140",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab144`](#insn-00bab144)

~~~json
{
  "source": "00bab144",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab150`](#insn-00bab150)

~~~json
{
  "source": "00bab150",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab154`](#insn-00bab154)

~~~json
{
  "source": "00bab154",
  "target": "00bab160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab15c`](#insn-00bab15c)

~~~json
{
  "source": "00bab15c",
  "target": "00bab1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab17c`](#insn-00bab17c)

~~~json
{
  "source": "00bab17c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab180`](#insn-00bab180)

~~~json
{
  "source": "00bab180",
  "target": "00c58690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab184`](#insn-00bab184)

~~~json
{
  "source": "00bab184",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab190`](#insn-00bab190)

~~~json
{
  "source": "00bab190",
  "target": "00bab1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab198`](#insn-00bab198)

~~~json
{
  "source": "00bab198",
  "target": "00bab1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1a4`](#insn-00bab1a4)

~~~json
{
  "source": "00bab1a4",
  "target": "00bab1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b4`](#insn-00bab1b4)

~~~json
{
  "source": "00bab1b4",
  "target": "00bab1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1bc`](#insn-00bab1bc)

~~~json
{
  "source": "00bab1bc",
  "target": "00bab1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1cc`](#insn-00bab1cc)

~~~json
{
  "source": "00bab1cc",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1d0`](#insn-00bab1d0)

~~~json
{
  "source": "00bab1d0",
  "target": "00bab1d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1d4`](#insn-00bab1d4)

~~~json
{
  "source": "00bab1d4",
  "target": "00bab258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f0`](#insn-00bab1f0)

~~~json
{
  "source": "00bab1f0",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab204`](#insn-00bab204)

~~~json
{
  "source": "00bab204",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab210`](#insn-00bab210)

~~~json
{
  "source": "00bab210",
  "target": "00bab1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab214`](#insn-00bab214)

~~~json
{
  "source": "00bab214",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab218`](#insn-00bab218)

~~~json
{
  "source": "00bab218",
  "target": "00bab318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab21c`](#insn-00bab21c)

~~~json
{
  "source": "00bab21c",
  "target": "00bab318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab228`](#insn-00bab228)

~~~json
{
  "source": "00bab228",
  "target": "00bab82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab22c`](#insn-00bab22c)

~~~json
{
  "source": "00bab22c",
  "target": "00bab830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab230`](#insn-00bab230)

~~~json
{
  "source": "00bab230",
  "target": "00bab358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab234`](#insn-00bab234)

~~~json
{
  "source": "00bab234",
  "target": "00bab358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab240`](#insn-00bab240)

~~~json
{
  "source": "00bab240",
  "target": "00bab65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab244`](#insn-00bab244)

~~~json
{
  "source": "00bab244",
  "target": "00bab660",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab24c`](#insn-00bab24c)

~~~json
{
  "source": "00bab24c",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab250`](#insn-00bab250)

~~~json
{
  "source": "00bab250",
  "target": "00bab398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab254`](#insn-00bab254)

~~~json
{
  "source": "00bab254",
  "target": "00bab398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab260`](#insn-00bab260)

~~~json
{
  "source": "00bab260",
  "target": "00bab454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab264`](#insn-00bab264)

~~~json
{
  "source": "00bab264",
  "target": "00bab458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab268`](#insn-00bab268)

~~~json
{
  "source": "00bab268",
  "target": "00bab490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab26c`](#insn-00bab26c)

~~~json
{
  "source": "00bab26c",
  "target": "00bab490",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab278`](#insn-00bab278)

~~~json
{
  "source": "00bab278",
  "target": "00bab85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab27c`](#insn-00bab27c)

~~~json
{
  "source": "00bab27c",
  "target": "00bab860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab280`](#insn-00bab280)

~~~json
{
  "source": "00bab280",
  "target": "00bab4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab284`](#insn-00bab284)

~~~json
{
  "source": "00bab284",
  "target": "00bab4d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab290`](#insn-00bab290)

~~~json
{
  "source": "00bab290",
  "target": "00bab770",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab294`](#insn-00bab294)

~~~json
{
  "source": "00bab294",
  "target": "00bab774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab298`](#insn-00bab298)

~~~json
{
  "source": "00bab298",
  "target": "00bab510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab29c`](#insn-00bab29c)

~~~json
{
  "source": "00bab29c",
  "target": "00bab510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2a8`](#insn-00bab2a8)

~~~json
{
  "source": "00bab2a8",
  "target": "00bab804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2ac`](#insn-00bab2ac)

~~~json
{
  "source": "00bab2ac",
  "target": "00bab808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b0`](#insn-00bab2b0)

~~~json
{
  "source": "00bab2b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b4`](#insn-00bab2b4)

~~~json
{
  "source": "00bab2b4",
  "target": "00bab2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b8`](#insn-00bab2b8)

~~~json
{
  "source": "00bab2b8",
  "target": "00bab89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e0`](#insn-00bab2e0)

~~~json
{
  "source": "00bab2e0",
  "target": "00c5c290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab2e4`](#insn-00bab2e4)

~~~json
{
  "source": "00bab2e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e8`](#insn-00bab2e8)

~~~json
{
  "source": "00bab2e8",
  "target": "00bab89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2ec`](#insn-00bab2ec)

~~~json
{
  "source": "00bab2ec",
  "target": "00bab89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f4`](#insn-00bab2f4)

~~~json
{
  "source": "00bab2f4",
  "target": "00bab878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab308`](#insn-00bab308)

~~~json
{
  "source": "00bab308",
  "target": "00bab87c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab310`](#insn-00bab310)

~~~json
{
  "source": "00bab310",
  "target": "00bab2fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab314`](#insn-00bab314)

~~~json
{
  "source": "00bab314",
  "target": "00bab87c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab330`](#insn-00bab330)

~~~json
{
  "source": "00bab330",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab344`](#insn-00bab344)

~~~json
{
  "source": "00bab344",
  "target": "00bab550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab350`](#insn-00bab350)

~~~json
{
  "source": "00bab350",
  "target": "00bab338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab354`](#insn-00bab354)

~~~json
{
  "source": "00bab354",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab370`](#insn-00bab370)

~~~json
{
  "source": "00bab370",
  "target": "00bab600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab384`](#insn-00bab384)

~~~json
{
  "source": "00bab384",
  "target": "00bab5d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab390`](#insn-00bab390)

~~~json
{
  "source": "00bab390",
  "target": "00bab378",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab394`](#insn-00bab394)

~~~json
{
  "source": "00bab394",
  "target": "00bab600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3b0`](#insn-00bab3b0)

~~~json
{
  "source": "00bab3b0",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3c4`](#insn-00bab3c4)

~~~json
{
  "source": "00bab3c4",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3d0`](#insn-00bab3d0)

~~~json
{
  "source": "00bab3d0",
  "target": "00bab3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3d4`](#insn-00bab3d4)

~~~json
{
  "source": "00bab3d4",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3dc`](#insn-00bab3dc)

~~~json
{
  "source": "00bab3dc",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3ec`](#insn-00bab3ec)

~~~json
{
  "source": "00bab3ec",
  "target": "00bab408",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f4`](#insn-00bab3f4)

~~~json
{
  "source": "00bab3f4",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab400`](#insn-00bab400)

~~~json
{
  "source": "00bab400",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab404`](#insn-00bab404)

~~~json
{
  "source": "00bab404",
  "target": "00bab41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab40c`](#insn-00bab40c)

~~~json
{
  "source": "00bab40c",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab410`](#insn-00bab410)

~~~json
{
  "source": "00bab410",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab41c`](#insn-00bab41c)

~~~json
{
  "source": "00bab41c",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab424`](#insn-00bab424)

~~~json
{
  "source": "00bab424",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab428`](#insn-00bab428)

~~~json
{
  "source": "00bab428",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab434`](#insn-00bab434)

~~~json
{
  "source": "00bab434",
  "target": "00bab44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab43c`](#insn-00bab43c)

~~~json
{
  "source": "00bab43c",
  "target": "00bab44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab450`](#insn-00bab450)

~~~json
{
  "source": "00bab450",
  "target": "00bab458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab458`](#insn-00bab458)

~~~json
{
  "source": "00bab458",
  "target": "00bab460",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab470`](#insn-00bab470)

~~~json
{
  "source": "00bab470",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab478`](#insn-00bab478)

~~~json
{
  "source": "00bab478",
  "target": "00bab8c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab47c`](#insn-00bab47c)

~~~json
{
  "source": "00bab47c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab480`](#insn-00bab480)

~~~json
{
  "source": "00bab480",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab484`](#insn-00bab484)

~~~json
{
  "source": "00bab484",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4a8`](#insn-00bab4a8)

~~~json
{
  "source": "00bab4a8",
  "target": "00bab6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4bc`](#insn-00bab4bc)

~~~json
{
  "source": "00bab4bc",
  "target": "00bab674",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4c8`](#insn-00bab4c8)

~~~json
{
  "source": "00bab4c8",
  "target": "00bab4b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4cc`](#insn-00bab4cc)

~~~json
{
  "source": "00bab4cc",
  "target": "00bab6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4e8`](#insn-00bab4e8)

~~~json
{
  "source": "00bab4e8",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4fc`](#insn-00bab4fc)

~~~json
{
  "source": "00bab4fc",
  "target": "00bab6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab508`](#insn-00bab508)

~~~json
{
  "source": "00bab508",
  "target": "00bab4f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab50c`](#insn-00bab50c)

~~~json
{
  "source": "00bab50c",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab528`](#insn-00bab528)

~~~json
{
  "source": "00bab528",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab53c`](#insn-00bab53c)

~~~json
{
  "source": "00bab53c",
  "target": "00bab788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab548`](#insn-00bab548)

~~~json
{
  "source": "00bab548",
  "target": "00bab530",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab54c`](#insn-00bab54c)

~~~json
{
  "source": "00bab54c",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab554`](#insn-00bab554)

~~~json
{
  "source": "00bab554",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab564`](#insn-00bab564)

~~~json
{
  "source": "00bab564",
  "target": "00bab580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab56c`](#insn-00bab56c)

~~~json
{
  "source": "00bab56c",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab578`](#insn-00bab578)

~~~json
{
  "source": "00bab578",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab57c`](#insn-00bab57c)

~~~json
{
  "source": "00bab57c",
  "target": "00bab594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab584`](#insn-00bab584)

~~~json
{
  "source": "00bab584",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab588`](#insn-00bab588)

~~~json
{
  "source": "00bab588",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab594`](#insn-00bab594)

~~~json
{
  "source": "00bab594",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab59c`](#insn-00bab59c)

~~~json
{
  "source": "00bab59c",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab5a0`](#insn-00bab5a0)

~~~json
{
  "source": "00bab5a0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5ac`](#insn-00bab5ac)

~~~json
{
  "source": "00bab5ac",
  "target": "00bab824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5b4`](#insn-00bab5b4)

~~~json
{
  "source": "00bab5b4",
  "target": "00bab824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5bc`](#insn-00bab5bc)

~~~json
{
  "source": "00bab5bc",
  "target": "00bab818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5c8`](#insn-00bab5c8)

~~~json
{
  "source": "00bab5c8",
  "target": "00bab82c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5cc`](#insn-00bab5cc)

~~~json
{
  "source": "00bab5cc",
  "target": "00bab830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5d4`](#insn-00bab5d4)

~~~json
{
  "source": "00bab5d4",
  "target": "00bab600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5e4`](#insn-00bab5e4)

~~~json
{
  "source": "00bab5e4",
  "target": "00bab600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5ec`](#insn-00bab5ec)

~~~json
{
  "source": "00bab5ec",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab5f8`](#insn-00bab5f8)

~~~json
{
  "source": "00bab5f8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5fc`](#insn-00bab5fc)

~~~json
{
  "source": "00bab5fc",
  "target": "00bab614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab604`](#insn-00bab604)

~~~json
{
  "source": "00bab604",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab608`](#insn-00bab608)

~~~json
{
  "source": "00bab608",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab614`](#insn-00bab614)

~~~json
{
  "source": "00bab614",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab61c`](#insn-00bab61c)

~~~json
{
  "source": "00bab61c",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab620`](#insn-00bab620)

~~~json
{
  "source": "00bab620",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab62c`](#insn-00bab62c)

~~~json
{
  "source": "00bab62c",
  "target": "00bab654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab634`](#insn-00bab634)

~~~json
{
  "source": "00bab634",
  "target": "00bab654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab640`](#insn-00bab640)

~~~json
{
  "source": "00bab640",
  "target": "00bab654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab658`](#insn-00bab658)

~~~json
{
  "source": "00bab658",
  "target": "00bab660",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab660`](#insn-00bab660)

~~~json
{
  "source": "00bab660",
  "target": "00bab668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab670`](#insn-00bab670)

~~~json
{
  "source": "00bab670",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab678`](#insn-00bab678)

~~~json
{
  "source": "00bab678",
  "target": "00bab6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab688`](#insn-00bab688)

~~~json
{
  "source": "00bab688",
  "target": "00bab6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab690`](#insn-00bab690)

~~~json
{
  "source": "00bab690",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab69c`](#insn-00bab69c)

~~~json
{
  "source": "00bab69c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6a0`](#insn-00bab6a0)

~~~json
{
  "source": "00bab6a0",
  "target": "00bab6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6a8`](#insn-00bab6a8)

~~~json
{
  "source": "00bab6a8",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab6ac`](#insn-00bab6ac)

~~~json
{
  "source": "00bab6ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6b8`](#insn-00bab6b8)

~~~json
{
  "source": "00bab6b8",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab6c0`](#insn-00bab6c0)

~~~json
{
  "source": "00bab6c0",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab6c4`](#insn-00bab6c4)

~~~json
{
  "source": "00bab6c4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d0`](#insn-00bab6d0)

~~~json
{
  "source": "00bab6d0",
  "target": "00bab854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d8`](#insn-00bab6d8)

~~~json
{
  "source": "00bab6d8",
  "target": "00bab854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6e0`](#insn-00bab6e0)

~~~json
{
  "source": "00bab6e0",
  "target": "00bab848",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6ec`](#insn-00bab6ec)

~~~json
{
  "source": "00bab6ec",
  "target": "00bab85c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6f0`](#insn-00bab6f0)

~~~json
{
  "source": "00bab6f0",
  "target": "00bab860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6f8`](#insn-00bab6f8)

~~~json
{
  "source": "00bab6f8",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab708`](#insn-00bab708)

~~~json
{
  "source": "00bab708",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab710`](#insn-00bab710)

~~~json
{
  "source": "00bab710",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab71c`](#insn-00bab71c)

~~~json
{
  "source": "00bab71c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab720`](#insn-00bab720)

~~~json
{
  "source": "00bab720",
  "target": "00bab738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab728`](#insn-00bab728)

~~~json
{
  "source": "00bab728",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab72c`](#insn-00bab72c)

~~~json
{
  "source": "00bab72c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab738`](#insn-00bab738)

~~~json
{
  "source": "00bab738",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab740`](#insn-00bab740)

~~~json
{
  "source": "00bab740",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab744`](#insn-00bab744)

~~~json
{
  "source": "00bab744",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab750`](#insn-00bab750)

~~~json
{
  "source": "00bab750",
  "target": "00bab768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab758`](#insn-00bab758)

~~~json
{
  "source": "00bab758",
  "target": "00bab768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab76c`](#insn-00bab76c)

~~~json
{
  "source": "00bab76c",
  "target": "00bab774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab774`](#insn-00bab774)

~~~json
{
  "source": "00bab774",
  "target": "00bab77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab784`](#insn-00bab784)

~~~json
{
  "source": "00bab784",
  "target": "00bab468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab78c`](#insn-00bab78c)

~~~json
{
  "source": "00bab78c",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab79c`](#insn-00bab79c)

~~~json
{
  "source": "00bab79c",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7a4`](#insn-00bab7a4)

~~~json
{
  "source": "00bab7a4",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab7b0`](#insn-00bab7b0)

~~~json
{
  "source": "00bab7b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7b4`](#insn-00bab7b4)

~~~json
{
  "source": "00bab7b4",
  "target": "00bab7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7bc`](#insn-00bab7bc)

~~~json
{
  "source": "00bab7bc",
  "target": "00c9b900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b900",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab7c0`](#insn-00bab7c0)

~~~json
{
  "source": "00bab7c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7cc`](#insn-00bab7cc)

~~~json
{
  "source": "00bab7cc",
  "target": "011262e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab7d4`](#insn-00bab7d4)

~~~json
{
  "source": "00bab7d4",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab7d8`](#insn-00bab7d8)

~~~json
{
  "source": "00bab7d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7e4`](#insn-00bab7e4)

~~~json
{
  "source": "00bab7e4",
  "target": "00bab7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7ec`](#insn-00bab7ec)

~~~json
{
  "source": "00bab7ec",
  "target": "00bab7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab800`](#insn-00bab800)

~~~json
{
  "source": "00bab800",
  "target": "00bab808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab808`](#insn-00bab808)

~~~json
{
  "source": "00bab808",
  "target": "00bab810",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab814`](#insn-00bab814)

~~~json
{
  "source": "00bab814",
  "target": "00bab468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab828`](#insn-00bab828)

~~~json
{
  "source": "00bab828",
  "target": "00bab830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab830`](#insn-00bab830)

~~~json
{
  "source": "00bab830",
  "target": "00bab838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab844`](#insn-00bab844)

~~~json
{
  "source": "00bab844",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab858`](#insn-00bab858)

~~~json
{
  "source": "00bab858",
  "target": "00bab860",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab860`](#insn-00bab860)

~~~json
{
  "source": "00bab860",
  "target": "00bab868",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab874`](#insn-00bab874)

~~~json
{
  "source": "00bab874",
  "target": "00bab46c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab890`](#insn-00bab890)

~~~json
{
  "source": "00bab890",
  "target": "00bab89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab898`](#insn-00bab898)

~~~json
{
  "source": "00bab898",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8b0`](#insn-00bab8b0)

~~~json
{
  "source": "00bab8b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8b4`](#insn-00bab8b4)

~~~json
{
  "source": "00bab8b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8bc`](#insn-00bab8bc)

~~~json
{
  "source": "00bab8bc",
  "target": "00bab468",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab8c0`](#insn-00bab8c0)

~~~json
{
  "source": "00bab8c0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
