# 00baaf0c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baaae4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baaae4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-366c229a2a6f309d5d96ee7e176458bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baafa8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baa/00baafa8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-45c34439d7d8b85166642b8e6945e31d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaf0c",
  "name": "FUN_00baaf0c",
  "size": 2332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff757ca189fc60fb4fcc832925f03fd467ffa98af81eb0b7f4a8baf6b441e4e0",
  "source_text_sha256": "ff757ca189fc60fb4fcc832925f03fd467ffa98af81eb0b7f4a8baf6b441e4e0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaf0c",
        "00bab827"
      ]
    ],
    "bytes_sha256": "212e85c78ee50559ce154805780f09769b0e3d527b25ae3078e5649b94a041b4",
    "instruction_count": 583,
    "instruction_bytes": 2332,
    "body_bytes": 2332,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b7fe3c](../00b7f/00b7fe3c.md)
- [00b80218](../00b80/00b80218.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c585b0](../00c58/00c585b0.md)
- [00c585c0](../00c58/00c585c0.md)
- [00c5c1b0](../00c5c/00c5c1b0.md)
- [00c5c1c0](../00c5c/00c5c1c0.md)
- [00c5d150](../00c5d/00c5d150.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 18494 bytes

~~~c

void FUN_00baaf0c(byte **param_1,byte **param_2,long param_3)

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
  
                    /* try { // try from 00baaf18 to 00caaf23 has its CatchHandler @ 00babd4c */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00baaf2c to 00caaf2f has its CatchHandler @ 00babd2c */
                    /* try { // try from 00baaf4c to 00caaf57 has its CatchHandler @ 00babce0 */
  switch(*(undefined4 *)(param_3 + 0xa0)) {
  case 0:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00baaf6c to 00caaf77 has its CatchHandler @ 00babcdc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) goto LAB_00bab33c;
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00baaf98 to 00caafa3 has its CatchHandler @ 00babc9c */
        } while (uVar13 != 0);
      }
LAB_00bab36c:
      iVar6 = 10;
      goto LAB_00bab380;
    }
    goto LAB_00bab1bc;
  case 1:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab308 to 00cab313 has its CatchHandler @ 00baba70 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab33c;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00bab334 to 00cab33f has its CatchHandler @ 00baba4c */
        } while (bVar9 != 0);
      }
      goto LAB_00bab36c;
    }
    goto LAB_00bab1bc;
  case 2:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab144 to 00cab14f has its CatchHandler @ 00babafc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
                    /* try { // try from 00bab150 to 00cab16f has its CatchHandler @ 00babe5c */
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab33c;
          bVar9 = pbVar15[lVar8];
                    /* try { // try from 00bab170 to 00cab1df has its CatchHandler @ 00bac030 */
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00bab36c;
    }
    goto LAB_00bab1bc;
  case 3:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
                    /* try { // try from 00bab290 to 00cab29b has its CatchHandler @ 00babad0 */
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab4c0 to 00cab4cb has its CatchHandler @ 00bab988 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bab4dc to 00cab4e7 has its CatchHandler @ 00bab984 */
              goto LAB_00bab4f8;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00bab2b4 to 00cab2bf has its CatchHandler @ 00babacc */
        } while (uVar13 != 0);
      }
                    /* try { // try from 00bab4e8 to 00cab507 has its CatchHandler @ 00babddc */
      iVar6 = 10;
LAB_00bab4f8:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
                    /* try { // try from 00bab508 to 00cab577 has its CatchHandler @ 00bac02c */
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
                    /* try { // try from 00bab78c to 00cab797 has its CatchHandler @ 00bab9e4 */
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
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
                    /* try { // try from 00bab034 to 00cab03f has its CatchHandler @ 00babbfc */
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00bab33c;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
                    /* try { // try from 00bab058 to 00cab063 has its CatchHandler @ 00babbec */
        } while (bVar9 != 0);
      }
      goto LAB_00bab36c;
    }
LAB_00bab1bc:
    uVar13 = 0;
joined_r0x00bab3b4:
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(byte *)param_2;
    }
    bVar3 = (uVar13 & 0xff) <= (uVar14 & 0xff);
LAB_00bab3cc:
    bVar3 = !bVar3;
    break;
  case 5:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab3f4 to 00cab3ff has its CatchHandler @ 00bab9fc */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bab420 to 00cab42b has its CatchHandler @ 00bab9d4 */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab5e0 to 00cab5fb has its CatchHandler @ 00babe44 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
              goto LAB_00bab61c;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab61c:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
                    /* try { // try from 00bab628 to 00cab633 has its CatchHandler @ 00babaa8 */
      uVar11 = 0;
      if ((local_40 != pbVar15) && (*local_40 == 0)) {
        if (lVar5 < 0x8000) {
          uVar11 = (ushort)lVar5;
          if (lVar5 < -0x7fff) {
            uVar11 = 0x8000;
          }
        }
        else {
                    /* try { // try from 00bab64c to 00cab657 has its CatchHandler @ 00babaa4 */
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
                    /* try { // try from 00bab1e4 to 00cab1f3 has its CatchHandler @ 00bab968 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
                    /* try { // try from 00bab444 to 00cab44f has its CatchHandler @ 00bab9d0 */
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab660 to 00cab663 has its CatchHandler @ 00baba84 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bab680 to 00cab68b has its CatchHandler @ 00baba60 */
              goto LAB_00bab69c;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab69c:
      local_40 = pbVar15;
                    /* try { // try from 00bab6a0 to 00cab6ab has its CatchHandler @ 00baba5c */
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
      uVar13 = 0;
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfffe < uVar4)) {
        uVar13 = 0xffff;
      }
    }
    else {
      uVar13 = 0;
                    /* try { // try from 00bab1f4 to 00cab207 has its CatchHandler @ 00bab964 */
    }
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(ushort *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(ushort *)param_2;
    }
    bVar3 = (uVar13 & 0xffff) <= (uVar14 & 0xffff);
    goto LAB_00bab3cc;
  case 7:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab2c8 to 00cab2cb has its CatchHandler @ 00babaac */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
                    /* try { // try from 00bab2e8 to 00cab2f3 has its CatchHandler @ 00baba74 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
              goto LAB_00bab578;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab578:
      local_40 = pbVar15;
                    /* try { // try from 00bab57c to 00cab58b has its CatchHandler @ 00bab960 */
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
      fVar18 = 0.0;
                    /* try { // try from 00bab58c to 00cab59f has its CatchHandler @ 00bab95c */
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
                    /* try { // try from 00bab494 to 00cab49f has its CatchHandler @ 00bab998 */
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab6f0 to 00cab6fb has its CatchHandler @ 00baba24 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
              goto LAB_00bab730;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
                    /* try { // try from 00bab71c to 00cab727 has its CatchHandler @ 00baba14 */
      iVar6 = 10;
LAB_00bab730:
      local_40 = pbVar15;
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
                    /* try { // try from 00bab73c to 00cab747 has its CatchHandler @ 00bab9f8 */
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
                    /* try { // try from 00bab768 to 00cab773 has its CatchHandler @ 00bab9e8 */
      fVar16 = *(float *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = (uint)fVar18 <= (uint)fVar16;
    goto LAB_00bab3cc;
  case 9:
    local_40 = (byte *)0x0;
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      lVar8 = param_3 + 0xc1;
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        lVar8 = *(long *)(param_3 + 0xd0);
      }
                    /* try { // try from 00bab084 to 00cab08f has its CatchHandler @ 00babba0 */
      _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib(&local_40,lVar8,0,1);
    }
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
                    /* try { // try from 00bab0a8 to 00cab0b3 has its CatchHandler @ 00babb9c */
    bVar3 = (long)*param_1 < (long)*param_2;
    break;
  case 10:
    local_40 = (byte *)0x0;
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar4 = _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib(&local_40,pbVar15,0,1);
                    /* try { // try from 00bab248 to 00cab263 has its CatchHandler @ 00babe48 */
      if ((local_40 != (byte *)0x0) && ((uVar4 & 1) != 0)) {
        uVar13 = (uint)*pbVar15;
        pbVar7 = pbVar15;
        if (*pbVar15 != 0) {
          do {
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
                    /* try { // try from 00bab808 to 00cab813 has its CatchHandler @ 00bab99c */
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
    bVar3 = *param_2 <= *param_1;
    goto LAB_00bab3cc;
  case 0xb:
    if ((param_1 == (byte **)0x0) || (fVar18 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00baafbc to 00caafc7 has its CatchHandler @ 00babc5c */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      fVar16 = strtof((char *)pbVar15,(char **)&local_40);
      fVar18 = 0.0;
                    /* try { // try from 00baafe8 to 00caaff3 has its CatchHandler @ 00babc4c */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = fVar16, NAN(fVar16))) {
        fVar18 = NAN;
      }
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
                    /* try { // try from 00bab008 to 00cab013 has its CatchHandler @ 00babc0c */
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = fVar16 < fVar18;
    break;
  case 0xc:
    if ((param_1 == (byte **)0x0) || (dVar19 = 0.0, param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab0d4 to 00cab0df has its CatchHandler @ 00babb50 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      dVar17 = strtod((char *)pbVar15,(char **)&local_40);
      dVar19 = 0.0;
                    /* try { // try from 00bab0f8 to 00cab103 has its CatchHandler @ 00babb4c */
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (dVar19 = dVar17, NAN(dVar17))) {
        dVar19 = NAN;
      }
    }
    dVar17 = dVar19;
    if (param_1 != (byte **)0x0) {
      dVar17 = (double)*param_1;
    }
    if (param_2 != (byte **)0x0) {
                    /* try { // try from 00bab124 to 00cab12f has its CatchHandler @ 00babb00 */
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
                    /* try { // try from 00bab3d0 to 00cab3db has its CatchHandler @ 00baba00 */
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(bVar3);
  }
  return;
LAB_00bab33c:
  if ((uVar13 != 0x30) || ((pbVar15[lVar8] & 0xdf) != 0x58)) goto LAB_00bab36c;
                    /* try { // try from 00bab358 to 00cab363 has its CatchHandler @ 00baba48 */
  iVar6 = 0x10;
LAB_00bab380:
  local_40 = pbVar15;
                    /* try { // try from 00bab384 to 00cab38f has its CatchHandler @ 00baba38 */
  uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                    *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b830);
  uVar13 = 0;
                    /* try { // try from 00bab3a4 to 00cab3af has its CatchHandler @ 00baba10 */
  if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfe < uVar4)) {
    uVar13 = 0xff;
  }
  goto joined_r0x00bab3b4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaf0c"></a> `00baaf0c` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baaf10"></a> `00baaf10` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaf14"></a> `00baaf14` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaf18"></a> `00baaf18` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaf1c"></a> `00baaf1c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baaf20"></a> `00baaf20` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baaf24"></a> `00baaf24` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00baaf28"></a> `00baaf28` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baaf2c"></a> `00baaf2c` | `48 a0 40 b9` | ldr w8,[x2, #0xa0] | `FALL_THROUGH`
<a id="insn-00baaf30"></a> `00baaf30` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00baaf34"></a> `00baaf34` | `c8 13 00 54` | b.hi 0x00bab1ac | `CONDITIONAL_JUMP`
<a id="insn-00baaf38"></a> `00baaf38` | `29 bb ff 90` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00baaf3c"></a> `00baaf3c` | `29 cd 07 91` | add x9,x9,#0x1f3 | `FALL_THROUGH`
<a id="insn-00baaf40"></a> `00baaf40` | `ca 00 00 10` | adr x10,0xbaaf58 | `FALL_THROUGH`
<a id="insn-00baaf44"></a> `00baaf44` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baaf48"></a> `00baaf48` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00baaf4c"></a> `00baaf4c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baaf50"></a> `00baaf50` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baaf54"></a> `00baaf54` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00baaf58"></a> `00baaf58` | `54 00 00 b4` | cbz x20,0x00baaf60 | `CONDITIONAL_JUMP`
<a id="insn-00baaf5c"></a> `00baaf5c` | `13 13 00 b5` | cbnz x19,0x00bab1bc | `CONDITIONAL_JUMP`
<a id="insn-00baaf60"></a> `00baaf60` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baaf64"></a> `00baaf64` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baaf68"></a> `00baaf68` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baaf6c"></a> `00baaf6c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf70"></a> `00baaf70` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baaf74"></a> `00baaf74` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baaf78"></a> `00baaf78` | `a9 1f 00 34` | cbz w9,0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00baaf7c"></a> `00baaf7c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf80"></a> `00baaf80` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baaf84"></a> `00baaf84` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baaf88"></a> `00baaf88` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baaf8c"></a> `00baaf8c` | `83 1d 00 54` | b.cc 0x00bab33c | `CONDITIONAL_JUMP`
<a id="insn-00baaf90"></a> `00baaf90` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baaf94"></a> `00baaf94` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf98"></a> `00baaf98` | `49 ff ff 35` | cbnz w9,0x00baaf80 | `CONDITIONAL_JUMP`
<a id="insn-00baaf9c"></a> `00baaf9c` | `f4 00 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00baafa0"></a> `00baafa0` | `74 00 00 b4` | cbz x20,0x00baafac | `CONDITIONAL_JUMP`
<a id="insn-00baafa4"></a> `00baafa4` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00baafa8"></a> `00baafa8` | `b3 02 00 b5` | cbnz x19,0x00baaffc | `CONDITIONAL_JUMP`
<a id="insn-00baafac"></a> `00baafac` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baafb0"></a> `00baafb0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baafb4"></a> `00baafb4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baafb8"></a> `00baafb8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baafbc"></a> `00baafbc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baafc0"></a> `00baafc0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baafc4"></a> `00baafc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baafc8"></a> `00baafc8` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00baafcc"></a> `00baafcc` | `79 b5 02 94` | bl 0x00c585b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baafd0"></a> `00baafd0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00baafd4"></a> `00baafd4` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `00 01 00 54` | b.eq 0x00baaffc | `CONDITIONAL_JUMP`
<a id="insn-00baafe0"></a> `00baafe0` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00baafe4"></a> `00baafe4` | `c8 00 00 35` | cbnz w8,0x00baaffc | `CONDITIONAL_JUMP`
<a id="insn-00baafe8"></a> `00baafe8` | `00 20 20 1e` | fcmp s0,s0 | `FALL_THROUGH`
<a id="insn-00baafec"></a> `00baafec` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `67 00 00 54` | b.vc 0x00baaffc | `CONDITIONAL_JUMP`
<a id="insn-00baaff4"></a> `00baaff4` | `08 f8 af 52` | mov w8,#0x7fc00000 | `FALL_THROUGH`
<a id="insn-00baaff8"></a> `00baaff8` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00baaffc"></a> `00baaffc` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `54 00 00 b4` | cbz x20,0x00bab008 | `CONDITIONAL_JUMP`
<a id="insn-00bab004"></a> `00bab004` | `80 02 40 bd` | ldr s0,[x20] | `FALL_THROUGH`
<a id="insn-00bab008"></a> `00bab008` | `53 00 00 b4` | cbz x19,0x00bab010 | `CONDITIONAL_JUMP`
<a id="insn-00bab00c"></a> `00bab00c` | `61 02 40 bd` | ldr s1,[x19] | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `46 00 00 14` | b 0x00bab12c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab018"></a> `00bab018` | `54 00 00 b4` | cbz x20,0x00bab020 | `CONDITIONAL_JUMP`
<a id="insn-00bab01c"></a> `00bab01c` | `13 0d 00 b5` | cbnz x19,0x00bab1bc | `CONDITIONAL_JUMP`
<a id="insn-00bab020"></a> `00bab020` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab028"></a> `00bab028` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab02c"></a> `00bab02c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab030"></a> `00bab030` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab034"></a> `00bab034` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab038"></a> `00bab038` | `a9 19 00 34` | cbz w9,0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab03c"></a> `00bab03c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab040"></a> `00bab040` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab044"></a> `00bab044` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab048"></a> `00bab048` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab04c"></a> `00bab04c` | `83 17 00 54` | b.cc 0x00bab33c | `CONDITIONAL_JUMP`
<a id="insn-00bab050"></a> `00bab050` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab054"></a> `00bab054` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab058"></a> `00bab058` | `49 ff ff 35` | cbnz w9,0x00bab040 | `CONDITIONAL_JUMP`
<a id="insn-00bab05c"></a> `00bab05c` | `c4 00 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab060"></a> `00bab060` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bab064"></a> `00bab064` | `54 00 00 b4` | cbz x20,0x00bab06c | `CONDITIONAL_JUMP`
<a id="insn-00bab068"></a> `00bab068` | `53 01 00 b5` | cbnz x19,0x00bab090 | `CONDITIONAL_JUMP`
<a id="insn-00bab06c"></a> `00bab06c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab070"></a> `00bab070` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab074"></a> `00bab074` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab078"></a> `00bab078` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab07c"></a> `00bab07c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab080"></a> `00bab080` | `41 01 89 9a` | csel x1,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab084"></a> `00bab084` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bab088"></a> `00bab088` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bab08c"></a> `00bab08c` | `49 c4 02 94` | bl 0x00c5c1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab090"></a> `00bab090` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bab094"></a> `00bab094` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab098"></a> `00bab098` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bab09c"></a> `00bab09c` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bab0a0"></a> `00bab0a0` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bab0a4"></a> `00bab0a4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bab0a8"></a> `00bab0a8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab0ac"></a> `00bab0ac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab0b0"></a> `00bab0b0` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab0b4"></a> `00bab0b4` | `c7 00 00 14` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab0b8"></a> `00bab0b8` | `74 00 00 b4` | cbz x20,0x00bab0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab0bc"></a> `00bab0bc` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bab0c0"></a> `00bab0c0` | `b3 02 00 b5` | cbnz x19,0x00bab114 | `CONDITIONAL_JUMP`
<a id="insn-00bab0c4"></a> `00bab0c4` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab0c8"></a> `00bab0c8` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab0cc"></a> `00bab0cc` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab0d0"></a> `00bab0d0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab0d4"></a> `00bab0d4` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab0d8"></a> `00bab0d8` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab0dc"></a> `00bab0dc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab0e0"></a> `00bab0e0` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab0e4"></a> `00bab0e4` | `37 b5 02 94` | bl 0x00c585c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab0e8"></a> `00bab0e8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab0ec"></a> `00bab0ec` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00bab0f0"></a> `00bab0f0` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab0f4"></a> `00bab0f4` | `00 01 00 54` | b.eq 0x00bab114 | `CONDITIONAL_JUMP`
<a id="insn-00bab0f8"></a> `00bab0f8` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab0fc"></a> `00bab0fc` | `c8 00 00 35` | cbnz w8,0x00bab114 | `CONDITIONAL_JUMP`
<a id="insn-00bab100"></a> `00bab100` | `00 20 60 1e` | fcmp d0,d0 | `FALL_THROUGH`
<a id="insn-00bab104"></a> `00bab104` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00bab108"></a> `00bab108` | `67 00 00 54` | b.vc 0x00bab114 | `CONDITIONAL_JUMP`
<a id="insn-00bab10c"></a> `00bab10c` | `08 ff ef d2` | mov x8,#0x7ff8000000000000 | `FALL_THROUGH`
<a id="insn-00bab110"></a> `00bab110` | `01 01 67 9e` | fmov d1,x8 | `FALL_THROUGH`
<a id="insn-00bab114"></a> `00bab114` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00bab118"></a> `00bab118` | `54 00 00 b4` | cbz x20,0x00bab120 | `CONDITIONAL_JUMP`
<a id="insn-00bab11c"></a> `00bab11c` | `80 02 40 fd` | ldr d0,[x20] | `FALL_THROUGH`
<a id="insn-00bab120"></a> `00bab120` | `53 00 00 b4` | cbz x19,0x00bab128 | `CONDITIONAL_JUMP`
<a id="insn-00bab124"></a> `00bab124` | `61 02 40 fd` | ldr d1,[x19] | `FALL_THROUGH`
<a id="insn-00bab128"></a> `00bab128` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00bab12c"></a> `00bab12c` | `e0 57 9f 1a` | cset w0,mi | `FALL_THROUGH`
<a id="insn-00bab130"></a> `00bab130` | `a8 00 00 14` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab134"></a> `00bab134` | `54 00 00 b4` | cbz x20,0x00bab13c | `CONDITIONAL_JUMP`
<a id="insn-00bab138"></a> `00bab138` | `33 04 00 b5` | cbnz x19,0x00bab1bc | `CONDITIONAL_JUMP`
<a id="insn-00bab13c"></a> `00bab13c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab140"></a> `00bab140` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab144"></a> `00bab144` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab148"></a> `00bab148` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab14c"></a> `00bab14c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab150"></a> `00bab150` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab154"></a> `00bab154` | `c9 10 00 34` | cbz w9,0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab158"></a> `00bab158` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab15c"></a> `00bab15c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab160"></a> `00bab160` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab164"></a> `00bab164` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab168"></a> `00bab168` | `a3 0e 00 54` | b.cc 0x00bab33c | `CONDITIONAL_JUMP`
<a id="insn-00bab16c"></a> `00bab16c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab170"></a> `00bab170` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab174"></a> `00bab174` | `49 ff ff 35` | cbnz w9,0x00bab15c | `CONDITIONAL_JUMP`
<a id="insn-00bab178"></a> `00bab178` | `7d 00 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab17c"></a> `00bab17c` | `14 08 00 b4` | cbz x20,0x00bab27c | `CONDITIONAL_JUMP`
<a id="insn-00bab180"></a> `00bab180` | `f3 07 00 b4` | cbz x19,0x00bab27c | `CONDITIONAL_JUMP`
<a id="insn-00bab184"></a> `00bab184` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab188"></a> `00bab188` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab18c"></a> `00bab18c` | `34 30 00 b5` | cbnz x20,0x00bab790 | `CONDITIONAL_JUMP`
<a id="insn-00bab190"></a> `00bab190` | `81 01 00 14` | b 0x00bab794 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab194"></a> `00bab194` | `54 09 00 b4` | cbz x20,0x00bab2bc | `CONDITIONAL_JUMP`
<a id="insn-00bab198"></a> `00bab198` | `33 09 00 b4` | cbz x19,0x00bab2bc | `CONDITIONAL_JUMP`
<a id="insn-00bab19c"></a> `00bab19c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab1a0"></a> `00bab1a0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab1a4"></a> `00bab1a4` | `f4 20 00 b5` | cbnz x20,0x00bab5c0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1a8"></a> `00bab1a8` | `07 01 00 14` | b 0x00bab5c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1ac"></a> `00bab1ac` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bab1b0"></a> `00bab1b0` | `88 00 00 14` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1b4"></a> `00bab1b4` | `54 0a 00 b4` | cbz x20,0x00bab2fc | `CONDITIONAL_JUMP`
<a id="insn-00bab1b8"></a> `00bab1b8` | `33 0a 00 b4` | cbz x19,0x00bab2fc | `CONDITIONAL_JUMP`
<a id="insn-00bab1bc"></a> `00bab1bc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab1c0"></a> `00bab1c0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab1c4"></a> `00bab1c4` | `b4 0f 00 b5` | cbnz x20,0x00bab3b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab1c8"></a> `00bab1c8` | `7d 00 00 14` | b 0x00bab3bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1cc"></a> `00bab1cc` | `54 11 00 b4` | cbz x20,0x00bab3f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab1d0"></a> `00bab1d0` | `33 11 00 b4` | cbz x19,0x00bab3f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab1d4"></a> `00bab1d4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab1d8"></a> `00bab1d8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab1dc"></a> `00bab1dc` | `34 2f 00 b5` | cbnz x20,0x00bab7c0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1e0"></a> `00bab1e0` | `79 01 00 14` | b 0x00bab7c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1e4"></a> `00bab1e4` | `94 12 00 b4` | cbz x20,0x00bab434 | `CONDITIONAL_JUMP`
<a id="insn-00bab1e8"></a> `00bab1e8` | `73 12 00 b4` | cbz x19,0x00bab434 | `CONDITIONAL_JUMP`
<a id="insn-00bab1ec"></a> `00bab1ec` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab1f0"></a> `00bab1f0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab1f4"></a> `00bab1f4` | `14 27 00 b5` | cbnz x20,0x00bab6d4 | `CONDITIONAL_JUMP`
<a id="insn-00bab1f8"></a> `00bab1f8` | `38 01 00 14` | b 0x00bab6d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1fc"></a> `00bab1fc` | `d4 13 00 b4` | cbz x20,0x00bab474 | `CONDITIONAL_JUMP`
<a id="insn-00bab200"></a> `00bab200` | `b3 13 00 b4` | cbz x19,0x00bab474 | `CONDITIONAL_JUMP`
<a id="insn-00bab204"></a> `00bab204` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab208"></a> `00bab208` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab20c"></a> `00bab20c` | `f4 2a 00 b5` | cbnz x20,0x00bab768 | `CONDITIONAL_JUMP`
<a id="insn-00bab210"></a> `00bab210` | `57 01 00 14` | b 0x00bab76c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab214"></a> `00bab214` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bab218"></a> `00bab218` | `54 00 00 b4` | cbz x20,0x00bab220 | `CONDITIONAL_JUMP`
<a id="insn-00bab21c"></a> `00bab21c` | `33 2f 00 b5` | cbnz x19,0x00bab800 | `CONDITIONAL_JUMP`
<a id="insn-00bab220"></a> `00bab220` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab224"></a> `00bab224` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab228"></a> `00bab228` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab22c"></a> `00bab22c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab230"></a> `00bab230` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab234"></a> `00bab234` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab238"></a> `00bab238` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bab23c"></a> `00bab23c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bab240"></a> `00bab240` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bab244"></a> `00bab244` | `df c3 02 94` | bl 0x00c5c1c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab248"></a> `00bab248` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab24c"></a> `00bab24c` | `a8 2d 00 b4` | cbz x8,0x00bab800 | `CONDITIONAL_JUMP`
<a id="insn-00bab250"></a> `00bab250` | `80 2d 00 36` | tbz w0,#0x0,0x00bab800 | `CONDITIONAL_JUMP`
<a id="insn-00bab254"></a> `00bab254` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab258"></a> `00bab258` | `29 2c 00 34` | cbz w9,0x00bab7dc | `CONDITIONAL_JUMP`
<a id="insn-00bab25c"></a> `00bab25c` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bab260"></a> `00bab260` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab264"></a> `00bab264` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab268"></a> `00bab268` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00bab26c"></a> `00bab26c` | `a3 2b 00 54` | b.cc 0x00bab7e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab270"></a> `00bab270` | `09 1d 40 38` | ldrb w9,[x8, #0x1]! | `FALL_THROUGH`
<a id="insn-00bab274"></a> `00bab274` | `69 ff ff 35` | cbnz w9,0x00bab260 | `CONDITIONAL_JUMP`
<a id="insn-00bab278"></a> `00bab278` | `5a 01 00 14` | b 0x00bab7e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab27c"></a> `00bab27c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab280"></a> `00bab280` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab284"></a> `00bab284` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab288"></a> `00bab288` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab28c"></a> `00bab28c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab290"></a> `00bab290` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab294"></a> `00bab294` | `89 12 00 34` | cbz w9,0x00bab4e4 | `CONDITIONAL_JUMP`
<a id="insn-00bab298"></a> `00bab298` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab29c"></a> `00bab29c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab2a0"></a> `00bab2a0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab2a4"></a> `00bab2a4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab2a8"></a> `00bab2a8` | `63 10 00 54` | b.cc 0x00bab4b4 | `CONDITIONAL_JUMP`
<a id="insn-00bab2ac"></a> `00bab2ac` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab2b0"></a> `00bab2b0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2b4"></a> `00bab2b4` | `49 ff ff 35` | cbnz w9,0x00bab29c | `CONDITIONAL_JUMP`
<a id="insn-00bab2b8"></a> `00bab2b8` | `8b 00 00 14` | b 0x00bab4e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab2bc"></a> `00bab2bc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab2c0"></a> `00bab2c0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab2c4"></a> `00bab2c4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab2c8"></a> `00bab2c8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2cc"></a> `00bab2cc` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab2d0"></a> `00bab2d0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab2d4"></a> `00bab2d4` | `89 14 00 34` | cbz w9,0x00bab564 | `CONDITIONAL_JUMP`
<a id="insn-00bab2d8"></a> `00bab2d8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2dc"></a> `00bab2dc` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab2e0"></a> `00bab2e0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab2e4"></a> `00bab2e4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab2e8"></a> `00bab2e8` | `63 12 00 54` | b.cc 0x00bab534 | `CONDITIONAL_JUMP`
<a id="insn-00bab2ec"></a> `00bab2ec` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab2f0"></a> `00bab2f0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab2f4"></a> `00bab2f4` | `49 ff ff 35` | cbnz w9,0x00bab2dc | `CONDITIONAL_JUMP`
<a id="insn-00bab2f8"></a> `00bab2f8` | `9b 00 00 14` | b 0x00bab564 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab2fc"></a> `00bab2fc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab300"></a> `00bab300` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab304"></a> `00bab304` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab308"></a> `00bab308` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab30c"></a> `00bab30c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab310"></a> `00bab310` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab314"></a> `00bab314` | `c9 02 00 34` | cbz w9,0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab318"></a> `00bab318` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab31c"></a> `00bab31c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab320"></a> `00bab320` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab324"></a> `00bab324` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab328"></a> `00bab328` | `a3 00 00 54` | b.cc 0x00bab33c | `CONDITIONAL_JUMP`
<a id="insn-00bab32c"></a> `00bab32c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab330"></a> `00bab330` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab334"></a> `00bab334` | `49 ff ff 35` | cbnz w9,0x00bab31c | `CONDITIONAL_JUMP`
<a id="insn-00bab338"></a> `00bab338` | `0d 00 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab33c"></a> `00bab33c` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab340"></a> `00bab340` | `61 01 00 54` | b.ne 0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab344"></a> `00bab344` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab348"></a> `00bab348` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab34c"></a> `00bab34c` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab350"></a> `00bab350` | `e1 00 00 54` | b.ne 0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab354"></a> `00bab354` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab358"></a> `00bab358` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab35c"></a> `00bab35c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab360"></a> `00bab360` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab364"></a> `00bab364` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab368"></a> `00bab368` | `06 00 00 14` | b 0x00bab380 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab36c"></a> `00bab36c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab370"></a> `00bab370` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab374"></a> `00bab374` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab378"></a> `00bab378` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab37c"></a> `00bab37c` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab380"></a> `00bab380` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab384"></a> `00bab384` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab388"></a> `00bab388` | `72 c7 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab38c"></a> `00bab38c` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab390"></a> `00bab390` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab394"></a> `00bab394` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab398"></a> `00bab398` | `c0 00 00 54` | b.eq 0x00bab3b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab39c"></a> `00bab39c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab3a0"></a> `00bab3a0` | `89 00 00 35` | cbnz w9,0x00bab3b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab3a4"></a> `00bab3a4` | `1f fc 03 f1` | cmp x0,#0xff | `FALL_THROUGH`
<a id="insn-00bab3a8"></a> `00bab3a8` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00bab3ac"></a> `00bab3ac` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bab3b0"></a> `00bab3b0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab3b4"></a> `00bab3b4` | `54 00 00 b4` | cbz x20,0x00bab3bc | `CONDITIONAL_JUMP`
<a id="insn-00bab3b8"></a> `00bab3b8` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab3bc"></a> `00bab3bc` | `53 00 00 b4` | cbz x19,0x00bab3c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab3c0"></a> `00bab3c0` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab3c4"></a> `00bab3c4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab3c8"></a> `00bab3c8` | `3f 01 28 6b` | cmp w9,w8, UXTB  | `FALL_THROUGH`
<a id="insn-00bab3cc"></a> `00bab3cc` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00bab3d0"></a> `00bab3d0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bab3d4"></a> `00bab3d4` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab3d8"></a> `00bab3d8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bab3dc"></a> `00bab3dc` | `41 22 00 54` | b.ne 0x00bab824 | `CONDITIONAL_JUMP`
<a id="insn-00bab3e0"></a> `00bab3e0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab3e4"></a> `00bab3e4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab3e8"></a> `00bab3e8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab3ec"></a> `00bab3ec` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bab3f0"></a> `00bab3f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bab3f4"></a> `00bab3f4` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab3f8"></a> `00bab3f8` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab3fc"></a> `00bab3fc` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab400"></a> `00bab400` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab404"></a> `00bab404` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab408"></a> `00bab408` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab40c"></a> `00bab40c` | `e9 0f 00 34` | cbz w9,0x00bab608 | `CONDITIONAL_JUMP`
<a id="insn-00bab410"></a> `00bab410` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab414"></a> `00bab414` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab418"></a> `00bab418` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab41c"></a> `00bab41c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab420"></a> `00bab420` | `c3 0d 00 54` | b.cc 0x00bab5d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab424"></a> `00bab424` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab428"></a> `00bab428` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab42c"></a> `00bab42c` | `49 ff ff 35` | cbnz w9,0x00bab414 | `CONDITIONAL_JUMP`
<a id="insn-00bab430"></a> `00bab430` | `76 00 00 14` | b 0x00bab608 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab434"></a> `00bab434` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab438"></a> `00bab438` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab43c"></a> `00bab43c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab440"></a> `00bab440` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab444"></a> `00bab444` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab448"></a> `00bab448` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab44c"></a> `00bab44c` | `e9 11 00 34` | cbz w9,0x00bab688 | `CONDITIONAL_JUMP`
<a id="insn-00bab450"></a> `00bab450` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab454"></a> `00bab454` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab458"></a> `00bab458` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab45c"></a> `00bab45c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab460"></a> `00bab460` | `c3 0f 00 54` | b.cc 0x00bab658 | `CONDITIONAL_JUMP`
<a id="insn-00bab464"></a> `00bab464` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab468"></a> `00bab468` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab46c"></a> `00bab46c` | `49 ff ff 35` | cbnz w9,0x00bab454 | `CONDITIONAL_JUMP`
<a id="insn-00bab470"></a> `00bab470` | `86 00 00 14` | b 0x00bab688 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab474"></a> `00bab474` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab478"></a> `00bab478` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab47c"></a> `00bab47c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab480"></a> `00bab480` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab484"></a> `00bab484` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab488"></a> `00bab488` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab48c"></a> `00bab48c` | `89 14 00 34` | cbz w9,0x00bab71c | `CONDITIONAL_JUMP`
<a id="insn-00bab490"></a> `00bab490` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab494"></a> `00bab494` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab498"></a> `00bab498` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab49c"></a> `00bab49c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab4a0"></a> `00bab4a0` | `63 12 00 54` | b.cc 0x00bab6ec | `CONDITIONAL_JUMP`
<a id="insn-00bab4a4"></a> `00bab4a4` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab4a8"></a> `00bab4a8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab4ac"></a> `00bab4ac` | `49 ff ff 35` | cbnz w9,0x00bab494 | `CONDITIONAL_JUMP`
<a id="insn-00bab4b0"></a> `00bab4b0` | `9b 00 00 14` | b 0x00bab71c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab4b4"></a> `00bab4b4` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab4b8"></a> `00bab4b8` | `61 01 00 54` | b.ne 0x00bab4e4 | `CONDITIONAL_JUMP`
<a id="insn-00bab4bc"></a> `00bab4bc` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab4c0"></a> `00bab4c0` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab4c4"></a> `00bab4c4` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab4c8"></a> `00bab4c8` | `e1 00 00 54` | b.ne 0x00bab4e4 | `CONDITIONAL_JUMP`
<a id="insn-00bab4cc"></a> `00bab4cc` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab4d0"></a> `00bab4d0` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab4d4"></a> `00bab4d4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab4d8"></a> `00bab4d8` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab4dc"></a> `00bab4dc` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab4e0"></a> `00bab4e0` | `06 00 00 14` | b 0x00bab4f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab4e4"></a> `00bab4e4` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab4e8"></a> `00bab4e8` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab4ec"></a> `00bab4ec` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab4f0"></a> `00bab4f0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab4f4"></a> `00bab4f4` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab4f8"></a> `00bab4f8` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab4fc"></a> `00bab4fc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab500"></a> `00bab500` | `14 c7 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab504"></a> `00bab504` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab508"></a> `00bab508` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab50c"></a> `00bab50c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab510"></a> `00bab510` | `c0 13 00 54` | b.eq 0x00bab788 | `CONDITIONAL_JUMP`
<a id="insn-00bab514"></a> `00bab514` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab518"></a> `00bab518` | `89 13 00 35` | cbnz w9,0x00bab788 | `CONDITIONAL_JUMP`
<a id="insn-00bab51c"></a> `00bab51c` | `1f fc 01 f1` | cmp x0,#0x7f | `FALL_THROUGH`
<a id="insn-00bab520"></a> `00bab520` | `ed 12 00 54` | b.le 0x00bab77c | `CONDITIONAL_JUMP`
<a id="insn-00bab524"></a> `00bab524` | `e8 0f 80 52` | mov w8,#0x7f | `FALL_THROUGH`
<a id="insn-00bab528"></a> `00bab528` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab52c"></a> `00bab52c` | `34 13 00 b5` | cbnz x20,0x00bab790 | `CONDITIONAL_JUMP`
<a id="insn-00bab530"></a> `00bab530` | `99 00 00 14` | b 0x00bab794 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab534"></a> `00bab534` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab538"></a> `00bab538` | `61 01 00 54` | b.ne 0x00bab564 | `CONDITIONAL_JUMP`
<a id="insn-00bab53c"></a> `00bab53c` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab540"></a> `00bab540` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab544"></a> `00bab544` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab548"></a> `00bab548` | `e1 00 00 54` | b.ne 0x00bab564 | `CONDITIONAL_JUMP`
<a id="insn-00bab54c"></a> `00bab54c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab550"></a> `00bab550` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab554"></a> `00bab554` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab558"></a> `00bab558` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab55c"></a> `00bab55c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab560"></a> `00bab560` | `06 00 00 14` | b 0x00bab578 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab564"></a> `00bab564` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab568"></a> `00bab568` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab56c"></a> `00bab56c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab570"></a> `00bab570` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab574"></a> `00bab574` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab578"></a> `00bab578` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab57c"></a> `00bab57c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab580"></a> `00bab580` | `f4 c6 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab584"></a> `00bab584` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab588"></a> `00bab588` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab58c"></a> `00bab58c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab590"></a> `00bab590` | `40 01 00 54` | b.eq 0x00bab5b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab594"></a> `00bab594` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab598"></a> `00bab598` | `09 01 00 35` | cbnz w9,0x00bab5b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab59c"></a> `00bab59c` | `08 00 b0 12` | mov w8,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00bab5a0"></a> `00bab5a0` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab5a4"></a> `00bab5a4` | `ac 00 00 54` | b.gt 0x00bab5b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab5a8"></a> `00bab5a8` | `e8 83 61 b2` | orr x8,xzr,#-0x80000000 | `FALL_THROUGH`
<a id="insn-00bab5ac"></a> `00bab5ac` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab5b0"></a> `00bab5b0` | `08 00 b0 52` | mov w8,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bab5b4"></a> `00bab5b4` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab5b8"></a> `00bab5b8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab5bc"></a> `00bab5bc` | `54 00 00 b4` | cbz x20,0x00bab5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab5c0"></a> `00bab5c0` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab5c4"></a> `00bab5c4` | `53 00 00 b4` | cbz x19,0x00bab5cc | `CONDITIONAL_JUMP`
<a id="insn-00bab5c8"></a> `00bab5c8` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab5cc"></a> `00bab5cc` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab5d0"></a> `00bab5d0` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab5d4"></a> `00bab5d4` | `7f ff ff 17` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab5d8"></a> `00bab5d8` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab5dc"></a> `00bab5dc` | `61 01 00 54` | b.ne 0x00bab608 | `CONDITIONAL_JUMP`
<a id="insn-00bab5e0"></a> `00bab5e0` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab5e4"></a> `00bab5e4` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab5e8"></a> `00bab5e8` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab5ec"></a> `00bab5ec` | `e1 00 00 54` | b.ne 0x00bab608 | `CONDITIONAL_JUMP`
<a id="insn-00bab5f0"></a> `00bab5f0` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab5f4"></a> `00bab5f4` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab5f8"></a> `00bab5f8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab5fc"></a> `00bab5fc` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab600"></a> `00bab600` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab604"></a> `00bab604` | `06 00 00 14` | b 0x00bab61c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab608"></a> `00bab608` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab60c"></a> `00bab60c` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab610"></a> `00bab610` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab614"></a> `00bab614` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab618"></a> `00bab618` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab61c"></a> `00bab61c` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab620"></a> `00bab620` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab624"></a> `00bab624` | `cb c6 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab628"></a> `00bab628` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab62c"></a> `00bab62c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab630"></a> `00bab630` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab634"></a> `00bab634` | `20 0c 00 54` | b.eq 0x00bab7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab638"></a> `00bab638` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab63c"></a> `00bab63c` | `e9 0b 00 35` | cbnz w9,0x00bab7b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab640"></a> `00bab640` | `1f 20 40 f1` | cmp x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab644"></a> `00bab644` | `4b 0b 00 54` | b.lt 0x00bab7ac | `CONDITIONAL_JUMP`
<a id="insn-00bab648"></a> `00bab648` | `e8 ff 8f 52` | mov w8,#0x7fff | `FALL_THROUGH`
<a id="insn-00bab64c"></a> `00bab64c` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab650"></a> `00bab650` | `94 0b 00 b5` | cbnz x20,0x00bab7c0 | `CONDITIONAL_JUMP`
<a id="insn-00bab654"></a> `00bab654` | `5c 00 00 14` | b 0x00bab7c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab658"></a> `00bab658` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab65c"></a> `00bab65c` | `61 01 00 54` | b.ne 0x00bab688 | `CONDITIONAL_JUMP`
<a id="insn-00bab660"></a> `00bab660` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab664"></a> `00bab664` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab668"></a> `00bab668` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab66c"></a> `00bab66c` | `e1 00 00 54` | b.ne 0x00bab688 | `CONDITIONAL_JUMP`
<a id="insn-00bab670"></a> `00bab670` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab674"></a> `00bab674` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab678"></a> `00bab678` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab67c"></a> `00bab67c` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab680"></a> `00bab680` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab684"></a> `00bab684` | `06 00 00 14` | b 0x00bab69c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab688"></a> `00bab688` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab68c"></a> `00bab68c` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab690"></a> `00bab690` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab694"></a> `00bab694` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab698"></a> `00bab698` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab69c"></a> `00bab69c` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab6a0"></a> `00bab6a0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab6a4"></a> `00bab6a4` | `ab c6 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab6a8"></a> `00bab6a8` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab6ac"></a> `00bab6ac` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab6b0"></a> `00bab6b0` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab6b4"></a> `00bab6b4` | `c0 00 00 54` | b.eq 0x00bab6cc | `CONDITIONAL_JUMP`
<a id="insn-00bab6b8"></a> `00bab6b8` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab6bc"></a> `00bab6bc` | `89 00 00 35` | cbnz w9,0x00bab6cc | `CONDITIONAL_JUMP`
<a id="insn-00bab6c0"></a> `00bab6c0` | `e8 ff 9f 52` | mov w8,#0xffff | `FALL_THROUGH`
<a id="insn-00bab6c4"></a> `00bab6c4` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab6c8"></a> `00bab6c8` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bab6cc"></a> `00bab6cc` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab6d0"></a> `00bab6d0` | `54 00 00 b4` | cbz x20,0x00bab6d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab6d4"></a> `00bab6d4` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab6d8"></a> `00bab6d8` | `53 00 00 b4` | cbz x19,0x00bab6e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab6dc"></a> `00bab6dc` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab6e0"></a> `00bab6e0` | `29 3d 00 12` | and w9,w9,#0xffff | `FALL_THROUGH`
<a id="insn-00bab6e4"></a> `00bab6e4` | `3f 21 28 6b` | cmp w9,w8, UXTH  | `FALL_THROUGH`
<a id="insn-00bab6e8"></a> `00bab6e8` | `39 ff ff 17` | b 0x00bab3cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab6ec"></a> `00bab6ec` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab6f0"></a> `00bab6f0` | `61 01 00 54` | b.ne 0x00bab71c | `CONDITIONAL_JUMP`
<a id="insn-00bab6f4"></a> `00bab6f4` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab6f8"></a> `00bab6f8` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab6fc"></a> `00bab6fc` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab700"></a> `00bab700` | `e1 00 00 54` | b.ne 0x00bab71c | `CONDITIONAL_JUMP`
<a id="insn-00bab704"></a> `00bab704` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab708"></a> `00bab708` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab70c"></a> `00bab70c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab710"></a> `00bab710` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab714"></a> `00bab714` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab718"></a> `00bab718` | `06 00 00 14` | b 0x00bab730 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab71c"></a> `00bab71c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab720"></a> `00bab720` | `08 19 44 f9` | ldr x8,[x8, #0x830] | `FALL_THROUGH`
<a id="insn-00bab724"></a> `00bab724` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab728"></a> `00bab728` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab72c"></a> `00bab72c` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab730"></a> `00bab730` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab734"></a> `00bab734` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab738"></a> `00bab738` | `86 c6 02 94` | bl 0x00c5d150 | `UNCONDITIONAL_CALL`
<a id="insn-00bab73c"></a> `00bab73c` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab740"></a> `00bab740` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab744"></a> `00bab744` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab748"></a> `00bab748` | `c0 00 00 54` | b.eq 0x00bab760 | `CONDITIONAL_JUMP`
<a id="insn-00bab74c"></a> `00bab74c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab750"></a> `00bab750` | `89 00 00 35` | cbnz w9,0x00bab760 | `CONDITIONAL_JUMP`
<a id="insn-00bab754"></a> `00bab754` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bab758"></a> `00bab758` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab75c"></a> `00bab75c` | `08 30 9f 5a` | csinv w8,w0,wzr,cc | `FALL_THROUGH`
<a id="insn-00bab760"></a> `00bab760` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab764"></a> `00bab764` | `54 00 00 b4` | cbz x20,0x00bab76c | `CONDITIONAL_JUMP`
<a id="insn-00bab768"></a> `00bab768` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab76c"></a> `00bab76c` | `53 00 00 b4` | cbz x19,0x00bab774 | `CONDITIONAL_JUMP`
<a id="insn-00bab770"></a> `00bab770` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab774"></a> `00bab774` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab778"></a> `00bab778` | `15 ff ff 17` | b 0x00bab3cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab77c"></a> `00bab77c` | `1f 00 02 b1` | cmn x0,#0x80 | `FALL_THROUGH`
<a id="insn-00bab780"></a> `00bab780` | `e8 0f 80 12` | mov w8,#0xffffff80 | `FALL_THROUGH`
<a id="insn-00bab784"></a> `00bab784` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab788"></a> `00bab788` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab78c"></a> `00bab78c` | `54 00 00 b4` | cbz x20,0x00bab794 | `CONDITIONAL_JUMP`
<a id="insn-00bab790"></a> `00bab790` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab794"></a> `00bab794` | `53 00 00 b4` | cbz x19,0x00bab79c | `CONDITIONAL_JUMP`
<a id="insn-00bab798"></a> `00bab798` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab79c"></a> `00bab79c` | `29 1d 00 13` | sxtb w9,w9 | `FALL_THROUGH`
<a id="insn-00bab7a0"></a> `00bab7a0` | `3f 81 28 6b` | cmp w9,w8, SXTB  | `FALL_THROUGH`
<a id="insn-00bab7a4"></a> `00bab7a4` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab7a8"></a> `00bab7a8` | `0a ff ff 17` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab7ac"></a> `00bab7ac` | `1f 20 40 b1` | cmn x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab7b0"></a> `00bab7b0` | `e8 ff 8f 12` | mov w8,#0xffff8000 | `FALL_THROUGH`
<a id="insn-00bab7b4"></a> `00bab7b4` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab7b8"></a> `00bab7b8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab7bc"></a> `00bab7bc` | `54 00 00 b4` | cbz x20,0x00bab7c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab7c0"></a> `00bab7c0` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab7c4"></a> `00bab7c4` | `53 00 00 b4` | cbz x19,0x00bab7cc | `CONDITIONAL_JUMP`
<a id="insn-00bab7c8"></a> `00bab7c8` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab7cc"></a> `00bab7cc` | `29 3d 00 13` | sxth w9,w9 | `FALL_THROUGH`
<a id="insn-00bab7d0"></a> `00bab7d0` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00bab7d4"></a> `00bab7d4` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab7d8"></a> `00bab7d8` | `fe fe ff 17` | b 0x00bab3d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab7dc"></a> `00bab7dc` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bab7e0"></a> `00bab7e0` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab7e4"></a> `00bab7e4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab7e8"></a> `00bab7e8` | `28 81 88 9a` | csel x8,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bab7ec"></a> `00bab7ec` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab7f0"></a> `00bab7f0` | `1f b5 00 71` | cmp w8,#0x2d | `FALL_THROUGH`
<a id="insn-00bab7f4"></a> `00bab7f4` | `61 00 00 54` | b.ne 0x00bab800 | `CONDITIONAL_JUMP`
<a id="insn-00bab7f8"></a> `00bab7f8` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00bab7fc"></a> `00bab7fc` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab800"></a> `00bab800` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bab804"></a> `00bab804` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab808"></a> `00bab808` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bab80c"></a> `00bab80c` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bab810"></a> `00bab810` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bab814"></a> `00bab814` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bab818"></a> `00bab818` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab81c"></a> `00bab81c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab820"></a> `00bab820` | `eb fe ff 17` | b 0x00bab3cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bab824"></a> `00bab824` | `af b1 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaf0c`](#insn-00baaf0c) 範囲 `[['00baaf0c', '00baaf17']]`
  - `FALL_THROUGH` [`00baaf14`](#insn-00baaf14) → [`00baaf18`](#insn-00baaf18)
- ブロック [`00baaf18`](#insn-00baaf18) 範囲 `[['00baaf18', '00baaf2b']]`
  - `FALL_THROUGH` [`00baaf28`](#insn-00baaf28) → [`00baaf2c`](#insn-00baaf2c)
- ブロック [`00baaf2c`](#insn-00baaf2c) 範囲 `[['00baaf2c', '00baaf37']]`
  - `CONDITIONAL_JUMP` [`00baaf34`](#insn-00baaf34) → [`00bab1ac`](#insn-00bab1ac)
  - `FALL_THROUGH` [`00baaf34`](#insn-00baaf34) → [`00baaf38`](#insn-00baaf38)
- ブロック [`00baaf38`](#insn-00baaf38) 範囲 `[['00baaf38', '00baaf4b']]`
  - `FALL_THROUGH` [`00baaf48`](#insn-00baaf48) → [`00baaf4c`](#insn-00baaf4c)
- ブロック [`00baaf4c`](#insn-00baaf4c) 範囲 `[['00baaf4c', '00baaf53']]`
  - `FALL_THROUGH` [`00baaf50`](#insn-00baaf50) → [`00baaf54`](#insn-00baaf54)
- ブロック [`00baaf54`](#insn-00baaf54) 範囲 `[['00baaf54', '00baaf57']]`
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00baaf58`](#insn-00baaf58)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab1b4`](#insn-00bab1b4)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab134`](#insn-00bab134)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab17c`](#insn-00bab17c)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab018`](#insn-00bab018)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab1cc`](#insn-00bab1cc)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab1e4`](#insn-00bab1e4)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab194`](#insn-00bab194)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab1fc`](#insn-00bab1fc)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab060`](#insn-00bab060)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab214`](#insn-00bab214)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00baafa0`](#insn-00baafa0)
  - `COMPUTED_JUMP` [`00baaf54`](#insn-00baaf54) → [`00bab0b8`](#insn-00bab0b8)
- ブロック [`00baaf58`](#insn-00baaf58) 範囲 `[['00baaf58', '00baaf5b']]`
  - `CONDITIONAL_JUMP` [`00baaf58`](#insn-00baaf58) → [`00baaf60`](#insn-00baaf60)
  - `FALL_THROUGH` [`00baaf58`](#insn-00baaf58) → [`00baaf5c`](#insn-00baaf5c)
- ブロック [`00baaf5c`](#insn-00baaf5c) 範囲 `[['00baaf5c', '00baaf5f']]`
  - `CONDITIONAL_JUMP` [`00baaf5c`](#insn-00baaf5c) → [`00bab1bc`](#insn-00bab1bc)
  - `FALL_THROUGH` [`00baaf5c`](#insn-00baaf5c) → [`00baaf60`](#insn-00baaf60)
- ブロック [`00baaf60`](#insn-00baaf60) 範囲 `[['00baaf60', '00baaf6b']]`
  - `FALL_THROUGH` [`00baaf68`](#insn-00baaf68) → [`00baaf6c`](#insn-00baaf6c)
- ブロック [`00baaf6c`](#insn-00baaf6c) 範囲 `[['00baaf6c', '00baaf7b']]`
  - `CONDITIONAL_JUMP` [`00baaf78`](#insn-00baaf78) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00baaf78`](#insn-00baaf78) → [`00baaf7c`](#insn-00baaf7c)
- ブロック [`00baaf7c`](#insn-00baaf7c) 範囲 `[['00baaf7c', '00baaf7f']]`
  - `FALL_THROUGH` [`00baaf7c`](#insn-00baaf7c) → [`00baaf80`](#insn-00baaf80)
- ブロック [`00baaf80`](#insn-00baaf80) 範囲 `[['00baaf80', '00baaf8f']]`
  - `CONDITIONAL_JUMP` [`00baaf8c`](#insn-00baaf8c) → [`00bab33c`](#insn-00bab33c)
  - `FALL_THROUGH` [`00baaf8c`](#insn-00baaf8c) → [`00baaf90`](#insn-00baaf90)
- ブロック [`00baaf90`](#insn-00baaf90) 範囲 `[['00baaf90', '00baaf97']]`
  - `FALL_THROUGH` [`00baaf94`](#insn-00baaf94) → [`00baaf98`](#insn-00baaf98)
- ブロック [`00baaf98`](#insn-00baaf98) 範囲 `[['00baaf98', '00baaf9b']]`
  - `CONDITIONAL_JUMP` [`00baaf98`](#insn-00baaf98) → [`00baaf80`](#insn-00baaf80)
  - `FALL_THROUGH` [`00baaf98`](#insn-00baaf98) → [`00baaf9c`](#insn-00baaf9c)
- ブロック [`00baaf9c`](#insn-00baaf9c) 範囲 `[['00baaf9c', '00baaf9f']]`
  - `UNCONDITIONAL_JUMP` [`00baaf9c`](#insn-00baaf9c) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00baafa0`](#insn-00baafa0) 範囲 `[['00baafa0', '00baafa3']]`
  - `CONDITIONAL_JUMP` [`00baafa0`](#insn-00baafa0) → [`00baafac`](#insn-00baafac)
  - `FALL_THROUGH` [`00baafa0`](#insn-00baafa0) → [`00baafa4`](#insn-00baafa4)
- ブロック [`00baafa4`](#insn-00baafa4) 範囲 `[['00baafa4', '00baafab']]`
  - `CONDITIONAL_JUMP` [`00baafa8`](#insn-00baafa8) → [`00baaffc`](#insn-00baaffc)
  - `FALL_THROUGH` [`00baafa8`](#insn-00baafa8) → [`00baafac`](#insn-00baafac)
- ブロック [`00baafac`](#insn-00baafac) 範囲 `[['00baafac', '00baafbb']]`
  - `FALL_THROUGH` [`00baafb8`](#insn-00baafb8) → [`00baafbc`](#insn-00baafbc)
- ブロック [`00baafbc`](#insn-00baafbc) 範囲 `[['00baafbc', '00baafdf']]`
  - `CONDITIONAL_JUMP` [`00baafdc`](#insn-00baafdc) → [`00baaffc`](#insn-00baaffc)
  - `FALL_THROUGH` [`00baafdc`](#insn-00baafdc) → [`00baafe0`](#insn-00baafe0)
- ブロック [`00baafe0`](#insn-00baafe0) 範囲 `[['00baafe0', '00baafe7']]`
  - `CONDITIONAL_JUMP` [`00baafe4`](#insn-00baafe4) → [`00baaffc`](#insn-00baaffc)
  - `FALL_THROUGH` [`00baafe4`](#insn-00baafe4) → [`00baafe8`](#insn-00baafe8)
- ブロック [`00baafe8`](#insn-00baafe8) 範囲 `[['00baafe8', '00baaff3']]`
  - `CONDITIONAL_JUMP` [`00baaff0`](#insn-00baaff0) → [`00baaffc`](#insn-00baaffc)
  - `FALL_THROUGH` [`00baaff0`](#insn-00baaff0) → [`00baaff4`](#insn-00baaff4)
- ブロック [`00baaff4`](#insn-00baaff4) 範囲 `[['00baaff4', '00baaffb']]`
  - `FALL_THROUGH` [`00baaff8`](#insn-00baaff8) → [`00baaffc`](#insn-00baaffc)
- ブロック [`00baaffc`](#insn-00baaffc) 範囲 `[['00baaffc', '00bab003']]`
  - `CONDITIONAL_JUMP` [`00bab000`](#insn-00bab000) → [`00bab008`](#insn-00bab008)
  - `FALL_THROUGH` [`00bab000`](#insn-00bab000) → [`00bab004`](#insn-00bab004)
- ブロック [`00bab004`](#insn-00bab004) 範囲 `[['00bab004', '00bab007']]`
  - `FALL_THROUGH` [`00bab004`](#insn-00bab004) → [`00bab008`](#insn-00bab008)
- ブロック [`00bab008`](#insn-00bab008) 範囲 `[['00bab008', '00bab00b']]`
  - `CONDITIONAL_JUMP` [`00bab008`](#insn-00bab008) → [`00bab010`](#insn-00bab010)
  - `FALL_THROUGH` [`00bab008`](#insn-00bab008) → [`00bab00c`](#insn-00bab00c)
- ブロック [`00bab00c`](#insn-00bab00c) 範囲 `[['00bab00c', '00bab00f']]`
  - `FALL_THROUGH` [`00bab00c`](#insn-00bab00c) → [`00bab010`](#insn-00bab010)
- ブロック [`00bab010`](#insn-00bab010) 範囲 `[['00bab010', '00bab017']]`
  - `UNCONDITIONAL_JUMP` [`00bab014`](#insn-00bab014) → [`00bab12c`](#insn-00bab12c)
- ブロック [`00bab018`](#insn-00bab018) 範囲 `[['00bab018', '00bab01b']]`
  - `CONDITIONAL_JUMP` [`00bab018`](#insn-00bab018) → [`00bab020`](#insn-00bab020)
  - `FALL_THROUGH` [`00bab018`](#insn-00bab018) → [`00bab01c`](#insn-00bab01c)
- ブロック [`00bab01c`](#insn-00bab01c) 範囲 `[['00bab01c', '00bab01f']]`
  - `CONDITIONAL_JUMP` [`00bab01c`](#insn-00bab01c) → [`00bab1bc`](#insn-00bab1bc)
  - `FALL_THROUGH` [`00bab01c`](#insn-00bab01c) → [`00bab020`](#insn-00bab020)
- ブロック [`00bab020`](#insn-00bab020) 範囲 `[['00bab020', '00bab033']]`
  - `FALL_THROUGH` [`00bab030`](#insn-00bab030) → [`00bab034`](#insn-00bab034)
- ブロック [`00bab034`](#insn-00bab034) 範囲 `[['00bab034', '00bab03b']]`
  - `CONDITIONAL_JUMP` [`00bab038`](#insn-00bab038) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab038`](#insn-00bab038) → [`00bab03c`](#insn-00bab03c)
- ブロック [`00bab03c`](#insn-00bab03c) 範囲 `[['00bab03c', '00bab03f']]`
  - `FALL_THROUGH` [`00bab03c`](#insn-00bab03c) → [`00bab040`](#insn-00bab040)
- ブロック [`00bab040`](#insn-00bab040) 範囲 `[['00bab040', '00bab04f']]`
  - `CONDITIONAL_JUMP` [`00bab04c`](#insn-00bab04c) → [`00bab33c`](#insn-00bab33c)
  - `FALL_THROUGH` [`00bab04c`](#insn-00bab04c) → [`00bab050`](#insn-00bab050)
- ブロック [`00bab050`](#insn-00bab050) 範囲 `[['00bab050', '00bab057']]`
  - `FALL_THROUGH` [`00bab054`](#insn-00bab054) → [`00bab058`](#insn-00bab058)
- ブロック [`00bab058`](#insn-00bab058) 範囲 `[['00bab058', '00bab05b']]`
  - `CONDITIONAL_JUMP` [`00bab058`](#insn-00bab058) → [`00bab040`](#insn-00bab040)
  - `FALL_THROUGH` [`00bab058`](#insn-00bab058) → [`00bab05c`](#insn-00bab05c)
- ブロック [`00bab05c`](#insn-00bab05c) 範囲 `[['00bab05c', '00bab05f']]`
  - `UNCONDITIONAL_JUMP` [`00bab05c`](#insn-00bab05c) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00bab060`](#insn-00bab060) 範囲 `[['00bab060', '00bab067']]`
  - `CONDITIONAL_JUMP` [`00bab064`](#insn-00bab064) → [`00bab06c`](#insn-00bab06c)
  - `FALL_THROUGH` [`00bab064`](#insn-00bab064) → [`00bab068`](#insn-00bab068)
- ブロック [`00bab068`](#insn-00bab068) 範囲 `[['00bab068', '00bab06b']]`
  - `CONDITIONAL_JUMP` [`00bab068`](#insn-00bab068) → [`00bab090`](#insn-00bab090)
  - `FALL_THROUGH` [`00bab068`](#insn-00bab068) → [`00bab06c`](#insn-00bab06c)
- ブロック [`00bab06c`](#insn-00bab06c) 範囲 `[['00bab06c', '00bab083']]`
  - `FALL_THROUGH` [`00bab080`](#insn-00bab080) → [`00bab084`](#insn-00bab084)
- ブロック [`00bab084`](#insn-00bab084) 範囲 `[['00bab084', '00bab08f']]`
  - `FALL_THROUGH` [`00bab08c`](#insn-00bab08c) → [`00bab090`](#insn-00bab090)
- ブロック [`00bab090`](#insn-00bab090) 範囲 `[['00bab090', '00bab0a7']]`
  - `FALL_THROUGH` [`00bab0a4`](#insn-00bab0a4) → [`00bab0a8`](#insn-00bab0a8)
- ブロック [`00bab0a8`](#insn-00bab0a8) 範囲 `[['00bab0a8', '00bab0b7']]`
  - `UNCONDITIONAL_JUMP` [`00bab0b4`](#insn-00bab0b4) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab0b8`](#insn-00bab0b8) 範囲 `[['00bab0b8', '00bab0bb']]`
  - `CONDITIONAL_JUMP` [`00bab0b8`](#insn-00bab0b8) → [`00bab0c4`](#insn-00bab0c4)
  - `FALL_THROUGH` [`00bab0b8`](#insn-00bab0b8) → [`00bab0bc`](#insn-00bab0bc)
- ブロック [`00bab0bc`](#insn-00bab0bc) 範囲 `[['00bab0bc', '00bab0c3']]`
  - `CONDITIONAL_JUMP` [`00bab0c0`](#insn-00bab0c0) → [`00bab114`](#insn-00bab114)
  - `FALL_THROUGH` [`00bab0c0`](#insn-00bab0c0) → [`00bab0c4`](#insn-00bab0c4)
- ブロック [`00bab0c4`](#insn-00bab0c4) 範囲 `[['00bab0c4', '00bab0d3']]`
  - `FALL_THROUGH` [`00bab0d0`](#insn-00bab0d0) → [`00bab0d4`](#insn-00bab0d4)
- ブロック [`00bab0d4`](#insn-00bab0d4) 範囲 `[['00bab0d4', '00bab0f7']]`
  - `CONDITIONAL_JUMP` [`00bab0f4`](#insn-00bab0f4) → [`00bab114`](#insn-00bab114)
  - `FALL_THROUGH` [`00bab0f4`](#insn-00bab0f4) → [`00bab0f8`](#insn-00bab0f8)
- ブロック [`00bab0f8`](#insn-00bab0f8) 範囲 `[['00bab0f8', '00bab0ff']]`
  - `CONDITIONAL_JUMP` [`00bab0fc`](#insn-00bab0fc) → [`00bab114`](#insn-00bab114)
  - `FALL_THROUGH` [`00bab0fc`](#insn-00bab0fc) → [`00bab100`](#insn-00bab100)
- ブロック [`00bab100`](#insn-00bab100) 範囲 `[['00bab100', '00bab10b']]`
  - `CONDITIONAL_JUMP` [`00bab108`](#insn-00bab108) → [`00bab114`](#insn-00bab114)
  - `FALL_THROUGH` [`00bab108`](#insn-00bab108) → [`00bab10c`](#insn-00bab10c)
- ブロック [`00bab10c`](#insn-00bab10c) 範囲 `[['00bab10c', '00bab113']]`
  - `FALL_THROUGH` [`00bab110`](#insn-00bab110) → [`00bab114`](#insn-00bab114)
- ブロック [`00bab114`](#insn-00bab114) 範囲 `[['00bab114', '00bab11b']]`
  - `CONDITIONAL_JUMP` [`00bab118`](#insn-00bab118) → [`00bab120`](#insn-00bab120)
  - `FALL_THROUGH` [`00bab118`](#insn-00bab118) → [`00bab11c`](#insn-00bab11c)
- ブロック [`00bab11c`](#insn-00bab11c) 範囲 `[['00bab11c', '00bab11f']]`
  - `FALL_THROUGH` [`00bab11c`](#insn-00bab11c) → [`00bab120`](#insn-00bab120)
- ブロック [`00bab120`](#insn-00bab120) 範囲 `[['00bab120', '00bab123']]`
  - `CONDITIONAL_JUMP` [`00bab120`](#insn-00bab120) → [`00bab128`](#insn-00bab128)
  - `FALL_THROUGH` [`00bab120`](#insn-00bab120) → [`00bab124`](#insn-00bab124)
- ブロック [`00bab124`](#insn-00bab124) 範囲 `[['00bab124', '00bab127']]`
  - `FALL_THROUGH` [`00bab124`](#insn-00bab124) → [`00bab128`](#insn-00bab128)
- ブロック [`00bab128`](#insn-00bab128) 範囲 `[['00bab128', '00bab12b']]`
  - `FALL_THROUGH` [`00bab128`](#insn-00bab128) → [`00bab12c`](#insn-00bab12c)
- ブロック [`00bab12c`](#insn-00bab12c) 範囲 `[['00bab12c', '00bab133']]`
  - `UNCONDITIONAL_JUMP` [`00bab130`](#insn-00bab130) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab134`](#insn-00bab134) 範囲 `[['00bab134', '00bab137']]`
  - `CONDITIONAL_JUMP` [`00bab134`](#insn-00bab134) → [`00bab13c`](#insn-00bab13c)
  - `FALL_THROUGH` [`00bab134`](#insn-00bab134) → [`00bab138`](#insn-00bab138)
- ブロック [`00bab138`](#insn-00bab138) 範囲 `[['00bab138', '00bab13b']]`
  - `CONDITIONAL_JUMP` [`00bab138`](#insn-00bab138) → [`00bab1bc`](#insn-00bab1bc)
  - `FALL_THROUGH` [`00bab138`](#insn-00bab138) → [`00bab13c`](#insn-00bab13c)
- ブロック [`00bab13c`](#insn-00bab13c) 範囲 `[['00bab13c', '00bab143']]`
  - `FALL_THROUGH` [`00bab140`](#insn-00bab140) → [`00bab144`](#insn-00bab144)
- ブロック [`00bab144`](#insn-00bab144) 範囲 `[['00bab144', '00bab14f']]`
  - `FALL_THROUGH` [`00bab14c`](#insn-00bab14c) → [`00bab150`](#insn-00bab150)
- ブロック [`00bab150`](#insn-00bab150) 範囲 `[['00bab150', '00bab157']]`
  - `CONDITIONAL_JUMP` [`00bab154`](#insn-00bab154) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab154`](#insn-00bab154) → [`00bab158`](#insn-00bab158)
- ブロック [`00bab158`](#insn-00bab158) 範囲 `[['00bab158', '00bab15b']]`
  - `FALL_THROUGH` [`00bab158`](#insn-00bab158) → [`00bab15c`](#insn-00bab15c)
- ブロック [`00bab15c`](#insn-00bab15c) 範囲 `[['00bab15c', '00bab16b']]`
  - `CONDITIONAL_JUMP` [`00bab168`](#insn-00bab168) → [`00bab33c`](#insn-00bab33c)
  - `FALL_THROUGH` [`00bab168`](#insn-00bab168) → [`00bab16c`](#insn-00bab16c)
- ブロック [`00bab16c`](#insn-00bab16c) 範囲 `[['00bab16c', '00bab16f']]`
  - `FALL_THROUGH` [`00bab16c`](#insn-00bab16c) → [`00bab170`](#insn-00bab170)
- ブロック [`00bab170`](#insn-00bab170) 範囲 `[['00bab170', '00bab177']]`
  - `CONDITIONAL_JUMP` [`00bab174`](#insn-00bab174) → [`00bab15c`](#insn-00bab15c)
  - `FALL_THROUGH` [`00bab174`](#insn-00bab174) → [`00bab178`](#insn-00bab178)
- ブロック [`00bab178`](#insn-00bab178) 範囲 `[['00bab178', '00bab17b']]`
  - `UNCONDITIONAL_JUMP` [`00bab178`](#insn-00bab178) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00bab17c`](#insn-00bab17c) 範囲 `[['00bab17c', '00bab17f']]`
  - `CONDITIONAL_JUMP` [`00bab17c`](#insn-00bab17c) → [`00bab27c`](#insn-00bab27c)
  - `FALL_THROUGH` [`00bab17c`](#insn-00bab17c) → [`00bab180`](#insn-00bab180)
- ブロック [`00bab180`](#insn-00bab180) 範囲 `[['00bab180', '00bab183']]`
  - `CONDITIONAL_JUMP` [`00bab180`](#insn-00bab180) → [`00bab27c`](#insn-00bab27c)
  - `FALL_THROUGH` [`00bab180`](#insn-00bab180) → [`00bab184`](#insn-00bab184)
- ブロック [`00bab184`](#insn-00bab184) 範囲 `[['00bab184', '00bab18f']]`
  - `CONDITIONAL_JUMP` [`00bab18c`](#insn-00bab18c) → [`00bab790`](#insn-00bab790)
  - `FALL_THROUGH` [`00bab18c`](#insn-00bab18c) → [`00bab190`](#insn-00bab190)
- ブロック [`00bab190`](#insn-00bab190) 範囲 `[['00bab190', '00bab193']]`
  - `UNCONDITIONAL_JUMP` [`00bab190`](#insn-00bab190) → [`00bab794`](#insn-00bab794)
- ブロック [`00bab194`](#insn-00bab194) 範囲 `[['00bab194', '00bab197']]`
  - `CONDITIONAL_JUMP` [`00bab194`](#insn-00bab194) → [`00bab2bc`](#insn-00bab2bc)
  - `FALL_THROUGH` [`00bab194`](#insn-00bab194) → [`00bab198`](#insn-00bab198)
- ブロック [`00bab198`](#insn-00bab198) 範囲 `[['00bab198', '00bab19b']]`
  - `CONDITIONAL_JUMP` [`00bab198`](#insn-00bab198) → [`00bab2bc`](#insn-00bab2bc)
  - `FALL_THROUGH` [`00bab198`](#insn-00bab198) → [`00bab19c`](#insn-00bab19c)
- ブロック [`00bab19c`](#insn-00bab19c) 範囲 `[['00bab19c', '00bab1a7']]`
  - `CONDITIONAL_JUMP` [`00bab1a4`](#insn-00bab1a4) → [`00bab5c0`](#insn-00bab5c0)
  - `FALL_THROUGH` [`00bab1a4`](#insn-00bab1a4) → [`00bab1a8`](#insn-00bab1a8)
- ブロック [`00bab1a8`](#insn-00bab1a8) 範囲 `[['00bab1a8', '00bab1ab']]`
  - `UNCONDITIONAL_JUMP` [`00bab1a8`](#insn-00bab1a8) → [`00bab5c4`](#insn-00bab5c4)
- ブロック [`00bab1ac`](#insn-00bab1ac) 範囲 `[['00bab1ac', '00bab1b3']]`
  - `UNCONDITIONAL_JUMP` [`00bab1b0`](#insn-00bab1b0) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab1b4`](#insn-00bab1b4) 範囲 `[['00bab1b4', '00bab1b7']]`
  - `CONDITIONAL_JUMP` [`00bab1b4`](#insn-00bab1b4) → [`00bab2fc`](#insn-00bab2fc)
  - `FALL_THROUGH` [`00bab1b4`](#insn-00bab1b4) → [`00bab1b8`](#insn-00bab1b8)
- ブロック [`00bab1b8`](#insn-00bab1b8) 範囲 `[['00bab1b8', '00bab1bb']]`
  - `CONDITIONAL_JUMP` [`00bab1b8`](#insn-00bab1b8) → [`00bab2fc`](#insn-00bab2fc)
  - `FALL_THROUGH` [`00bab1b8`](#insn-00bab1b8) → [`00bab1bc`](#insn-00bab1bc)
- ブロック [`00bab1bc`](#insn-00bab1bc) 範囲 `[['00bab1bc', '00bab1c7']]`
  - `CONDITIONAL_JUMP` [`00bab1c4`](#insn-00bab1c4) → [`00bab3b8`](#insn-00bab3b8)
  - `FALL_THROUGH` [`00bab1c4`](#insn-00bab1c4) → [`00bab1c8`](#insn-00bab1c8)
- ブロック [`00bab1c8`](#insn-00bab1c8) 範囲 `[['00bab1c8', '00bab1cb']]`
  - `UNCONDITIONAL_JUMP` [`00bab1c8`](#insn-00bab1c8) → [`00bab3bc`](#insn-00bab3bc)
- ブロック [`00bab1cc`](#insn-00bab1cc) 範囲 `[['00bab1cc', '00bab1cf']]`
  - `CONDITIONAL_JUMP` [`00bab1cc`](#insn-00bab1cc) → [`00bab3f4`](#insn-00bab3f4)
  - `FALL_THROUGH` [`00bab1cc`](#insn-00bab1cc) → [`00bab1d0`](#insn-00bab1d0)
- ブロック [`00bab1d0`](#insn-00bab1d0) 範囲 `[['00bab1d0', '00bab1d3']]`
  - `CONDITIONAL_JUMP` [`00bab1d0`](#insn-00bab1d0) → [`00bab3f4`](#insn-00bab3f4)
  - `FALL_THROUGH` [`00bab1d0`](#insn-00bab1d0) → [`00bab1d4`](#insn-00bab1d4)
- ブロック [`00bab1d4`](#insn-00bab1d4) 範囲 `[['00bab1d4', '00bab1df']]`
  - `CONDITIONAL_JUMP` [`00bab1dc`](#insn-00bab1dc) → [`00bab7c0`](#insn-00bab7c0)
  - `FALL_THROUGH` [`00bab1dc`](#insn-00bab1dc) → [`00bab1e0`](#insn-00bab1e0)
- ブロック [`00bab1e0`](#insn-00bab1e0) 範囲 `[['00bab1e0', '00bab1e3']]`
  - `UNCONDITIONAL_JUMP` [`00bab1e0`](#insn-00bab1e0) → [`00bab7c4`](#insn-00bab7c4)
- ブロック [`00bab1e4`](#insn-00bab1e4) 範囲 `[['00bab1e4', '00bab1e7']]`
  - `CONDITIONAL_JUMP` [`00bab1e4`](#insn-00bab1e4) → [`00bab434`](#insn-00bab434)
  - `FALL_THROUGH` [`00bab1e4`](#insn-00bab1e4) → [`00bab1e8`](#insn-00bab1e8)
- ブロック [`00bab1e8`](#insn-00bab1e8) 範囲 `[['00bab1e8', '00bab1eb']]`
  - `CONDITIONAL_JUMP` [`00bab1e8`](#insn-00bab1e8) → [`00bab434`](#insn-00bab434)
  - `FALL_THROUGH` [`00bab1e8`](#insn-00bab1e8) → [`00bab1ec`](#insn-00bab1ec)
- ブロック [`00bab1ec`](#insn-00bab1ec) 範囲 `[['00bab1ec', '00bab1f3']]`
  - `FALL_THROUGH` [`00bab1f0`](#insn-00bab1f0) → [`00bab1f4`](#insn-00bab1f4)
- ブロック [`00bab1f4`](#insn-00bab1f4) 範囲 `[['00bab1f4', '00bab1f7']]`
  - `CONDITIONAL_JUMP` [`00bab1f4`](#insn-00bab1f4) → [`00bab6d4`](#insn-00bab6d4)
  - `FALL_THROUGH` [`00bab1f4`](#insn-00bab1f4) → [`00bab1f8`](#insn-00bab1f8)
- ブロック [`00bab1f8`](#insn-00bab1f8) 範囲 `[['00bab1f8', '00bab1fb']]`
  - `UNCONDITIONAL_JUMP` [`00bab1f8`](#insn-00bab1f8) → [`00bab6d8`](#insn-00bab6d8)
- ブロック [`00bab1fc`](#insn-00bab1fc) 範囲 `[['00bab1fc', '00bab1ff']]`
  - `CONDITIONAL_JUMP` [`00bab1fc`](#insn-00bab1fc) → [`00bab474`](#insn-00bab474)
  - `FALL_THROUGH` [`00bab1fc`](#insn-00bab1fc) → [`00bab200`](#insn-00bab200)
- ブロック [`00bab200`](#insn-00bab200) 範囲 `[['00bab200', '00bab203']]`
  - `CONDITIONAL_JUMP` [`00bab200`](#insn-00bab200) → [`00bab474`](#insn-00bab474)
  - `FALL_THROUGH` [`00bab200`](#insn-00bab200) → [`00bab204`](#insn-00bab204)
- ブロック [`00bab204`](#insn-00bab204) 範囲 `[['00bab204', '00bab20f']]`
  - `CONDITIONAL_JUMP` [`00bab20c`](#insn-00bab20c) → [`00bab768`](#insn-00bab768)
  - `FALL_THROUGH` [`00bab20c`](#insn-00bab20c) → [`00bab210`](#insn-00bab210)
- ブロック [`00bab210`](#insn-00bab210) 範囲 `[['00bab210', '00bab213']]`
  - `UNCONDITIONAL_JUMP` [`00bab210`](#insn-00bab210) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab214`](#insn-00bab214) 範囲 `[['00bab214', '00bab21b']]`
  - `CONDITIONAL_JUMP` [`00bab218`](#insn-00bab218) → [`00bab220`](#insn-00bab220)
  - `FALL_THROUGH` [`00bab218`](#insn-00bab218) → [`00bab21c`](#insn-00bab21c)
- ブロック [`00bab21c`](#insn-00bab21c) 範囲 `[['00bab21c', '00bab21f']]`
  - `CONDITIONAL_JUMP` [`00bab21c`](#insn-00bab21c) → [`00bab800`](#insn-00bab800)
  - `FALL_THROUGH` [`00bab21c`](#insn-00bab21c) → [`00bab220`](#insn-00bab220)
- ブロック [`00bab220`](#insn-00bab220) 範囲 `[['00bab220', '00bab247']]`
  - `FALL_THROUGH` [`00bab244`](#insn-00bab244) → [`00bab248`](#insn-00bab248)
- ブロック [`00bab248`](#insn-00bab248) 範囲 `[['00bab248', '00bab24f']]`
  - `CONDITIONAL_JUMP` [`00bab24c`](#insn-00bab24c) → [`00bab800`](#insn-00bab800)
  - `FALL_THROUGH` [`00bab24c`](#insn-00bab24c) → [`00bab250`](#insn-00bab250)
- ブロック [`00bab250`](#insn-00bab250) 範囲 `[['00bab250', '00bab253']]`
  - `CONDITIONAL_JUMP` [`00bab250`](#insn-00bab250) → [`00bab800`](#insn-00bab800)
  - `FALL_THROUGH` [`00bab250`](#insn-00bab250) → [`00bab254`](#insn-00bab254)
- ブロック [`00bab254`](#insn-00bab254) 範囲 `[['00bab254', '00bab25b']]`
  - `CONDITIONAL_JUMP` [`00bab258`](#insn-00bab258) → [`00bab7dc`](#insn-00bab7dc)
  - `FALL_THROUGH` [`00bab258`](#insn-00bab258) → [`00bab25c`](#insn-00bab25c)
- ブロック [`00bab25c`](#insn-00bab25c) 範囲 `[['00bab25c', '00bab25f']]`
  - `FALL_THROUGH` [`00bab25c`](#insn-00bab25c) → [`00bab260`](#insn-00bab260)
- ブロック [`00bab260`](#insn-00bab260) 範囲 `[['00bab260', '00bab26f']]`
  - `CONDITIONAL_JUMP` [`00bab26c`](#insn-00bab26c) → [`00bab7e0`](#insn-00bab7e0)
  - `FALL_THROUGH` [`00bab26c`](#insn-00bab26c) → [`00bab270`](#insn-00bab270)
- ブロック [`00bab270`](#insn-00bab270) 範囲 `[['00bab270', '00bab277']]`
  - `CONDITIONAL_JUMP` [`00bab274`](#insn-00bab274) → [`00bab260`](#insn-00bab260)
  - `FALL_THROUGH` [`00bab274`](#insn-00bab274) → [`00bab278`](#insn-00bab278)
- ブロック [`00bab278`](#insn-00bab278) 範囲 `[['00bab278', '00bab27b']]`
  - `UNCONDITIONAL_JUMP` [`00bab278`](#insn-00bab278) → [`00bab7e0`](#insn-00bab7e0)
- ブロック [`00bab27c`](#insn-00bab27c) 範囲 `[['00bab27c', '00bab28f']]`
  - `FALL_THROUGH` [`00bab28c`](#insn-00bab28c) → [`00bab290`](#insn-00bab290)
- ブロック [`00bab290`](#insn-00bab290) 範囲 `[['00bab290', '00bab297']]`
  - `CONDITIONAL_JUMP` [`00bab294`](#insn-00bab294) → [`00bab4e4`](#insn-00bab4e4)
  - `FALL_THROUGH` [`00bab294`](#insn-00bab294) → [`00bab298`](#insn-00bab298)
- ブロック [`00bab298`](#insn-00bab298) 範囲 `[['00bab298', '00bab29b']]`
  - `FALL_THROUGH` [`00bab298`](#insn-00bab298) → [`00bab29c`](#insn-00bab29c)
- ブロック [`00bab29c`](#insn-00bab29c) 範囲 `[['00bab29c', '00bab2ab']]`
  - `CONDITIONAL_JUMP` [`00bab2a8`](#insn-00bab2a8) → [`00bab4b4`](#insn-00bab4b4)
  - `FALL_THROUGH` [`00bab2a8`](#insn-00bab2a8) → [`00bab2ac`](#insn-00bab2ac)
- ブロック [`00bab2ac`](#insn-00bab2ac) 範囲 `[['00bab2ac', '00bab2b3']]`
  - `FALL_THROUGH` [`00bab2b0`](#insn-00bab2b0) → [`00bab2b4`](#insn-00bab2b4)
- ブロック [`00bab2b4`](#insn-00bab2b4) 範囲 `[['00bab2b4', '00bab2b7']]`
  - `CONDITIONAL_JUMP` [`00bab2b4`](#insn-00bab2b4) → [`00bab29c`](#insn-00bab29c)
  - `FALL_THROUGH` [`00bab2b4`](#insn-00bab2b4) → [`00bab2b8`](#insn-00bab2b8)
- ブロック [`00bab2b8`](#insn-00bab2b8) 範囲 `[['00bab2b8', '00bab2bb']]`
  - `UNCONDITIONAL_JUMP` [`00bab2b8`](#insn-00bab2b8) → [`00bab4e4`](#insn-00bab4e4)
- ブロック [`00bab2bc`](#insn-00bab2bc) 範囲 `[['00bab2bc', '00bab2c7']]`
  - `FALL_THROUGH` [`00bab2c4`](#insn-00bab2c4) → [`00bab2c8`](#insn-00bab2c8)
- ブロック [`00bab2c8`](#insn-00bab2c8) 範囲 `[['00bab2c8', '00bab2d7']]`
  - `CONDITIONAL_JUMP` [`00bab2d4`](#insn-00bab2d4) → [`00bab564`](#insn-00bab564)
  - `FALL_THROUGH` [`00bab2d4`](#insn-00bab2d4) → [`00bab2d8`](#insn-00bab2d8)
- ブロック [`00bab2d8`](#insn-00bab2d8) 範囲 `[['00bab2d8', '00bab2db']]`
  - `FALL_THROUGH` [`00bab2d8`](#insn-00bab2d8) → [`00bab2dc`](#insn-00bab2dc)
- ブロック [`00bab2dc`](#insn-00bab2dc) 範囲 `[['00bab2dc', '00bab2e7']]`
  - `FALL_THROUGH` [`00bab2e4`](#insn-00bab2e4) → [`00bab2e8`](#insn-00bab2e8)
- ブロック [`00bab2e8`](#insn-00bab2e8) 範囲 `[['00bab2e8', '00bab2eb']]`
  - `CONDITIONAL_JUMP` [`00bab2e8`](#insn-00bab2e8) → [`00bab534`](#insn-00bab534)
  - `FALL_THROUGH` [`00bab2e8`](#insn-00bab2e8) → [`00bab2ec`](#insn-00bab2ec)
- ブロック [`00bab2ec`](#insn-00bab2ec) 範囲 `[['00bab2ec', '00bab2f7']]`
  - `CONDITIONAL_JUMP` [`00bab2f4`](#insn-00bab2f4) → [`00bab2dc`](#insn-00bab2dc)
  - `FALL_THROUGH` [`00bab2f4`](#insn-00bab2f4) → [`00bab2f8`](#insn-00bab2f8)
- ブロック [`00bab2f8`](#insn-00bab2f8) 範囲 `[['00bab2f8', '00bab2fb']]`
  - `UNCONDITIONAL_JUMP` [`00bab2f8`](#insn-00bab2f8) → [`00bab564`](#insn-00bab564)
- ブロック [`00bab2fc`](#insn-00bab2fc) 範囲 `[['00bab2fc', '00bab307']]`
  - `FALL_THROUGH` [`00bab304`](#insn-00bab304) → [`00bab308`](#insn-00bab308)
- ブロック [`00bab308`](#insn-00bab308) 範囲 `[['00bab308', '00bab317']]`
  - `CONDITIONAL_JUMP` [`00bab314`](#insn-00bab314) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab314`](#insn-00bab314) → [`00bab318`](#insn-00bab318)
- ブロック [`00bab318`](#insn-00bab318) 範囲 `[['00bab318', '00bab31b']]`
  - `FALL_THROUGH` [`00bab318`](#insn-00bab318) → [`00bab31c`](#insn-00bab31c)
- ブロック [`00bab31c`](#insn-00bab31c) 範囲 `[['00bab31c', '00bab32b']]`
  - `CONDITIONAL_JUMP` [`00bab328`](#insn-00bab328) → [`00bab33c`](#insn-00bab33c)
  - `FALL_THROUGH` [`00bab328`](#insn-00bab328) → [`00bab32c`](#insn-00bab32c)
- ブロック [`00bab32c`](#insn-00bab32c) 範囲 `[['00bab32c', '00bab333']]`
  - `FALL_THROUGH` [`00bab330`](#insn-00bab330) → [`00bab334`](#insn-00bab334)
- ブロック [`00bab334`](#insn-00bab334) 範囲 `[['00bab334', '00bab337']]`
  - `CONDITIONAL_JUMP` [`00bab334`](#insn-00bab334) → [`00bab31c`](#insn-00bab31c)
  - `FALL_THROUGH` [`00bab334`](#insn-00bab334) → [`00bab338`](#insn-00bab338)
- ブロック [`00bab338`](#insn-00bab338) 範囲 `[['00bab338', '00bab33b']]`
  - `UNCONDITIONAL_JUMP` [`00bab338`](#insn-00bab338) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00bab33c`](#insn-00bab33c) 範囲 `[['00bab33c', '00bab343']]`
  - `CONDITIONAL_JUMP` [`00bab340`](#insn-00bab340) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab340`](#insn-00bab340) → [`00bab344`](#insn-00bab344)
- ブロック [`00bab344`](#insn-00bab344) 範囲 `[['00bab344', '00bab353']]`
  - `CONDITIONAL_JUMP` [`00bab350`](#insn-00bab350) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab350`](#insn-00bab350) → [`00bab354`](#insn-00bab354)
- ブロック [`00bab354`](#insn-00bab354) 範囲 `[['00bab354', '00bab357']]`
  - `FALL_THROUGH` [`00bab354`](#insn-00bab354) → [`00bab358`](#insn-00bab358)
- ブロック [`00bab358`](#insn-00bab358) 範囲 `[['00bab358', '00bab36b']]`
  - `UNCONDITIONAL_JUMP` [`00bab368`](#insn-00bab368) → [`00bab380`](#insn-00bab380)
- ブロック [`00bab36c`](#insn-00bab36c) 範囲 `[['00bab36c', '00bab37f']]`
  - `FALL_THROUGH` [`00bab37c`](#insn-00bab37c) → [`00bab380`](#insn-00bab380)
- ブロック [`00bab380`](#insn-00bab380) 範囲 `[['00bab380', '00bab383']]`
  - `FALL_THROUGH` [`00bab380`](#insn-00bab380) → [`00bab384`](#insn-00bab384)
- ブロック [`00bab384`](#insn-00bab384) 範囲 `[['00bab384', '00bab39b']]`
  - `CONDITIONAL_JUMP` [`00bab398`](#insn-00bab398) → [`00bab3b0`](#insn-00bab3b0)
  - `FALL_THROUGH` [`00bab398`](#insn-00bab398) → [`00bab39c`](#insn-00bab39c)
- ブロック [`00bab39c`](#insn-00bab39c) 範囲 `[['00bab39c', '00bab3a3']]`
  - `CONDITIONAL_JUMP` [`00bab3a0`](#insn-00bab3a0) → [`00bab3b0`](#insn-00bab3b0)
  - `FALL_THROUGH` [`00bab3a0`](#insn-00bab3a0) → [`00bab3a4`](#insn-00bab3a4)
- ブロック [`00bab3a4`](#insn-00bab3a4) 範囲 `[['00bab3a4', '00bab3af']]`
  - `FALL_THROUGH` [`00bab3ac`](#insn-00bab3ac) → [`00bab3b0`](#insn-00bab3b0)
- ブロック [`00bab3b0`](#insn-00bab3b0) 範囲 `[['00bab3b0', '00bab3b7']]`
  - `CONDITIONAL_JUMP` [`00bab3b4`](#insn-00bab3b4) → [`00bab3bc`](#insn-00bab3bc)
  - `FALL_THROUGH` [`00bab3b4`](#insn-00bab3b4) → [`00bab3b8`](#insn-00bab3b8)
- ブロック [`00bab3b8`](#insn-00bab3b8) 範囲 `[['00bab3b8', '00bab3bb']]`
  - `FALL_THROUGH` [`00bab3b8`](#insn-00bab3b8) → [`00bab3bc`](#insn-00bab3bc)
- ブロック [`00bab3bc`](#insn-00bab3bc) 範囲 `[['00bab3bc', '00bab3bf']]`
  - `CONDITIONAL_JUMP` [`00bab3bc`](#insn-00bab3bc) → [`00bab3c4`](#insn-00bab3c4)
  - `FALL_THROUGH` [`00bab3bc`](#insn-00bab3bc) → [`00bab3c0`](#insn-00bab3c0)
- ブロック [`00bab3c0`](#insn-00bab3c0) 範囲 `[['00bab3c0', '00bab3c3']]`
  - `FALL_THROUGH` [`00bab3c0`](#insn-00bab3c0) → [`00bab3c4`](#insn-00bab3c4)
- ブロック [`00bab3c4`](#insn-00bab3c4) 範囲 `[['00bab3c4', '00bab3cb']]`
  - `FALL_THROUGH` [`00bab3c8`](#insn-00bab3c8) → [`00bab3cc`](#insn-00bab3cc)
- ブロック [`00bab3cc`](#insn-00bab3cc) 範囲 `[['00bab3cc', '00bab3cf']]`
  - `FALL_THROUGH` [`00bab3cc`](#insn-00bab3cc) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab3d0`](#insn-00bab3d0) 範囲 `[['00bab3d0', '00bab3df']]`
  - `CONDITIONAL_JUMP` [`00bab3dc`](#insn-00bab3dc) → [`00bab824`](#insn-00bab824)
  - `FALL_THROUGH` [`00bab3dc`](#insn-00bab3dc) → [`00bab3e0`](#insn-00bab3e0)
- ブロック [`00bab3e0`](#insn-00bab3e0) 範囲 `[['00bab3e0', '00bab3f3']]`
- ブロック [`00bab3f4`](#insn-00bab3f4) 範囲 `[['00bab3f4', '00bab40f']]`
  - `CONDITIONAL_JUMP` [`00bab40c`](#insn-00bab40c) → [`00bab608`](#insn-00bab608)
  - `FALL_THROUGH` [`00bab40c`](#insn-00bab40c) → [`00bab410`](#insn-00bab410)
- ブロック [`00bab410`](#insn-00bab410) 範囲 `[['00bab410', '00bab413']]`
  - `FALL_THROUGH` [`00bab410`](#insn-00bab410) → [`00bab414`](#insn-00bab414)
- ブロック [`00bab414`](#insn-00bab414) 範囲 `[['00bab414', '00bab41f']]`
  - `FALL_THROUGH` [`00bab41c`](#insn-00bab41c) → [`00bab420`](#insn-00bab420)
- ブロック [`00bab420`](#insn-00bab420) 範囲 `[['00bab420', '00bab423']]`
  - `CONDITIONAL_JUMP` [`00bab420`](#insn-00bab420) → [`00bab5d8`](#insn-00bab5d8)
  - `FALL_THROUGH` [`00bab420`](#insn-00bab420) → [`00bab424`](#insn-00bab424)
- ブロック [`00bab424`](#insn-00bab424) 範囲 `[['00bab424', '00bab42f']]`
  - `CONDITIONAL_JUMP` [`00bab42c`](#insn-00bab42c) → [`00bab414`](#insn-00bab414)
  - `FALL_THROUGH` [`00bab42c`](#insn-00bab42c) → [`00bab430`](#insn-00bab430)
- ブロック [`00bab430`](#insn-00bab430) 範囲 `[['00bab430', '00bab433']]`
  - `UNCONDITIONAL_JUMP` [`00bab430`](#insn-00bab430) → [`00bab608`](#insn-00bab608)
- ブロック [`00bab434`](#insn-00bab434) 範囲 `[['00bab434', '00bab443']]`
  - `FALL_THROUGH` [`00bab440`](#insn-00bab440) → [`00bab444`](#insn-00bab444)
- ブロック [`00bab444`](#insn-00bab444) 範囲 `[['00bab444', '00bab44f']]`
  - `CONDITIONAL_JUMP` [`00bab44c`](#insn-00bab44c) → [`00bab688`](#insn-00bab688)
  - `FALL_THROUGH` [`00bab44c`](#insn-00bab44c) → [`00bab450`](#insn-00bab450)
- ブロック [`00bab450`](#insn-00bab450) 範囲 `[['00bab450', '00bab453']]`
  - `FALL_THROUGH` [`00bab450`](#insn-00bab450) → [`00bab454`](#insn-00bab454)
- ブロック [`00bab454`](#insn-00bab454) 範囲 `[['00bab454', '00bab463']]`
  - `CONDITIONAL_JUMP` [`00bab460`](#insn-00bab460) → [`00bab658`](#insn-00bab658)
  - `FALL_THROUGH` [`00bab460`](#insn-00bab460) → [`00bab464`](#insn-00bab464)
- ブロック [`00bab464`](#insn-00bab464) 範囲 `[['00bab464', '00bab46f']]`
  - `CONDITIONAL_JUMP` [`00bab46c`](#insn-00bab46c) → [`00bab454`](#insn-00bab454)
  - `FALL_THROUGH` [`00bab46c`](#insn-00bab46c) → [`00bab470`](#insn-00bab470)
- ブロック [`00bab470`](#insn-00bab470) 範囲 `[['00bab470', '00bab473']]`
  - `UNCONDITIONAL_JUMP` [`00bab470`](#insn-00bab470) → [`00bab688`](#insn-00bab688)
- ブロック [`00bab474`](#insn-00bab474) 範囲 `[['00bab474', '00bab48f']]`
  - `CONDITIONAL_JUMP` [`00bab48c`](#insn-00bab48c) → [`00bab71c`](#insn-00bab71c)
  - `FALL_THROUGH` [`00bab48c`](#insn-00bab48c) → [`00bab490`](#insn-00bab490)
- ブロック [`00bab490`](#insn-00bab490) 範囲 `[['00bab490', '00bab493']]`
  - `FALL_THROUGH` [`00bab490`](#insn-00bab490) → [`00bab494`](#insn-00bab494)
- ブロック [`00bab494`](#insn-00bab494) 範囲 `[['00bab494', '00bab4a3']]`
  - `CONDITIONAL_JUMP` [`00bab4a0`](#insn-00bab4a0) → [`00bab6ec`](#insn-00bab6ec)
  - `FALL_THROUGH` [`00bab4a0`](#insn-00bab4a0) → [`00bab4a4`](#insn-00bab4a4)
- ブロック [`00bab4a4`](#insn-00bab4a4) 範囲 `[['00bab4a4', '00bab4af']]`
  - `CONDITIONAL_JUMP` [`00bab4ac`](#insn-00bab4ac) → [`00bab494`](#insn-00bab494)
  - `FALL_THROUGH` [`00bab4ac`](#insn-00bab4ac) → [`00bab4b0`](#insn-00bab4b0)
- ブロック [`00bab4b0`](#insn-00bab4b0) 範囲 `[['00bab4b0', '00bab4b3']]`
  - `UNCONDITIONAL_JUMP` [`00bab4b0`](#insn-00bab4b0) → [`00bab71c`](#insn-00bab71c)
- ブロック [`00bab4b4`](#insn-00bab4b4) 範囲 `[['00bab4b4', '00bab4bb']]`
  - `CONDITIONAL_JUMP` [`00bab4b8`](#insn-00bab4b8) → [`00bab4e4`](#insn-00bab4e4)
  - `FALL_THROUGH` [`00bab4b8`](#insn-00bab4b8) → [`00bab4bc`](#insn-00bab4bc)
- ブロック [`00bab4bc`](#insn-00bab4bc) 範囲 `[['00bab4bc', '00bab4bf']]`
  - `FALL_THROUGH` [`00bab4bc`](#insn-00bab4bc) → [`00bab4c0`](#insn-00bab4c0)
- ブロック [`00bab4c0`](#insn-00bab4c0) 範囲 `[['00bab4c0', '00bab4cb']]`
  - `CONDITIONAL_JUMP` [`00bab4c8`](#insn-00bab4c8) → [`00bab4e4`](#insn-00bab4e4)
  - `FALL_THROUGH` [`00bab4c8`](#insn-00bab4c8) → [`00bab4cc`](#insn-00bab4cc)
- ブロック [`00bab4cc`](#insn-00bab4cc) 範囲 `[['00bab4cc', '00bab4db']]`
  - `FALL_THROUGH` [`00bab4d8`](#insn-00bab4d8) → [`00bab4dc`](#insn-00bab4dc)
- ブロック [`00bab4dc`](#insn-00bab4dc) 範囲 `[['00bab4dc', '00bab4e3']]`
  - `UNCONDITIONAL_JUMP` [`00bab4e0`](#insn-00bab4e0) → [`00bab4f8`](#insn-00bab4f8)
- ブロック [`00bab4e4`](#insn-00bab4e4) 範囲 `[['00bab4e4', '00bab4e7']]`
  - `FALL_THROUGH` [`00bab4e4`](#insn-00bab4e4) → [`00bab4e8`](#insn-00bab4e8)
- ブロック [`00bab4e8`](#insn-00bab4e8) 範囲 `[['00bab4e8', '00bab4f7']]`
  - `FALL_THROUGH` [`00bab4f4`](#insn-00bab4f4) → [`00bab4f8`](#insn-00bab4f8)
- ブロック [`00bab4f8`](#insn-00bab4f8) 範囲 `[['00bab4f8', '00bab507']]`
  - `FALL_THROUGH` [`00bab504`](#insn-00bab504) → [`00bab508`](#insn-00bab508)
- ブロック [`00bab508`](#insn-00bab508) 範囲 `[['00bab508', '00bab513']]`
  - `CONDITIONAL_JUMP` [`00bab510`](#insn-00bab510) → [`00bab788`](#insn-00bab788)
  - `FALL_THROUGH` [`00bab510`](#insn-00bab510) → [`00bab514`](#insn-00bab514)
- ブロック [`00bab514`](#insn-00bab514) 範囲 `[['00bab514', '00bab51b']]`
  - `CONDITIONAL_JUMP` [`00bab518`](#insn-00bab518) → [`00bab788`](#insn-00bab788)
  - `FALL_THROUGH` [`00bab518`](#insn-00bab518) → [`00bab51c`](#insn-00bab51c)
- ブロック [`00bab51c`](#insn-00bab51c) 範囲 `[['00bab51c', '00bab523']]`
  - `CONDITIONAL_JUMP` [`00bab520`](#insn-00bab520) → [`00bab77c`](#insn-00bab77c)
  - `FALL_THROUGH` [`00bab520`](#insn-00bab520) → [`00bab524`](#insn-00bab524)
- ブロック [`00bab524`](#insn-00bab524) 範囲 `[['00bab524', '00bab52f']]`
  - `CONDITIONAL_JUMP` [`00bab52c`](#insn-00bab52c) → [`00bab790`](#insn-00bab790)
  - `FALL_THROUGH` [`00bab52c`](#insn-00bab52c) → [`00bab530`](#insn-00bab530)
- ブロック [`00bab530`](#insn-00bab530) 範囲 `[['00bab530', '00bab533']]`
  - `UNCONDITIONAL_JUMP` [`00bab530`](#insn-00bab530) → [`00bab794`](#insn-00bab794)
- ブロック [`00bab534`](#insn-00bab534) 範囲 `[['00bab534', '00bab53b']]`
  - `CONDITIONAL_JUMP` [`00bab538`](#insn-00bab538) → [`00bab564`](#insn-00bab564)
  - `FALL_THROUGH` [`00bab538`](#insn-00bab538) → [`00bab53c`](#insn-00bab53c)
- ブロック [`00bab53c`](#insn-00bab53c) 範囲 `[['00bab53c', '00bab54b']]`
  - `CONDITIONAL_JUMP` [`00bab548`](#insn-00bab548) → [`00bab564`](#insn-00bab564)
  - `FALL_THROUGH` [`00bab548`](#insn-00bab548) → [`00bab54c`](#insn-00bab54c)
- ブロック [`00bab54c`](#insn-00bab54c) 範囲 `[['00bab54c', '00bab563']]`
  - `UNCONDITIONAL_JUMP` [`00bab560`](#insn-00bab560) → [`00bab578`](#insn-00bab578)
- ブロック [`00bab564`](#insn-00bab564) 範囲 `[['00bab564', '00bab577']]`
  - `FALL_THROUGH` [`00bab574`](#insn-00bab574) → [`00bab578`](#insn-00bab578)
- ブロック [`00bab578`](#insn-00bab578) 範囲 `[['00bab578', '00bab57b']]`
  - `FALL_THROUGH` [`00bab578`](#insn-00bab578) → [`00bab57c`](#insn-00bab57c)
- ブロック [`00bab57c`](#insn-00bab57c) 範囲 `[['00bab57c', '00bab58b']]`
  - `FALL_THROUGH` [`00bab588`](#insn-00bab588) → [`00bab58c`](#insn-00bab58c)
- ブロック [`00bab58c`](#insn-00bab58c) 範囲 `[['00bab58c', '00bab593']]`
  - `CONDITIONAL_JUMP` [`00bab590`](#insn-00bab590) → [`00bab5b8`](#insn-00bab5b8)
  - `FALL_THROUGH` [`00bab590`](#insn-00bab590) → [`00bab594`](#insn-00bab594)
- ブロック [`00bab594`](#insn-00bab594) 範囲 `[['00bab594', '00bab59b']]`
  - `CONDITIONAL_JUMP` [`00bab598`](#insn-00bab598) → [`00bab5b8`](#insn-00bab5b8)
  - `FALL_THROUGH` [`00bab598`](#insn-00bab598) → [`00bab59c`](#insn-00bab59c)
- ブロック [`00bab59c`](#insn-00bab59c) 範囲 `[['00bab59c', '00bab5a7']]`
  - `CONDITIONAL_JUMP` [`00bab5a4`](#insn-00bab5a4) → [`00bab5b8`](#insn-00bab5b8)
  - `FALL_THROUGH` [`00bab5a4`](#insn-00bab5a4) → [`00bab5a8`](#insn-00bab5a8)
- ブロック [`00bab5a8`](#insn-00bab5a8) 範囲 `[['00bab5a8', '00bab5b7']]`
  - `FALL_THROUGH` [`00bab5b4`](#insn-00bab5b4) → [`00bab5b8`](#insn-00bab5b8)
- ブロック [`00bab5b8`](#insn-00bab5b8) 範囲 `[['00bab5b8', '00bab5bf']]`
  - `CONDITIONAL_JUMP` [`00bab5bc`](#insn-00bab5bc) → [`00bab5c4`](#insn-00bab5c4)
  - `FALL_THROUGH` [`00bab5bc`](#insn-00bab5bc) → [`00bab5c0`](#insn-00bab5c0)
- ブロック [`00bab5c0`](#insn-00bab5c0) 範囲 `[['00bab5c0', '00bab5c3']]`
  - `FALL_THROUGH` [`00bab5c0`](#insn-00bab5c0) → [`00bab5c4`](#insn-00bab5c4)
- ブロック [`00bab5c4`](#insn-00bab5c4) 範囲 `[['00bab5c4', '00bab5c7']]`
  - `CONDITIONAL_JUMP` [`00bab5c4`](#insn-00bab5c4) → [`00bab5cc`](#insn-00bab5cc)
  - `FALL_THROUGH` [`00bab5c4`](#insn-00bab5c4) → [`00bab5c8`](#insn-00bab5c8)
- ブロック [`00bab5c8`](#insn-00bab5c8) 範囲 `[['00bab5c8', '00bab5cb']]`
  - `FALL_THROUGH` [`00bab5c8`](#insn-00bab5c8) → [`00bab5cc`](#insn-00bab5cc)
- ブロック [`00bab5cc`](#insn-00bab5cc) 範囲 `[['00bab5cc', '00bab5d7']]`
  - `UNCONDITIONAL_JUMP` [`00bab5d4`](#insn-00bab5d4) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab5d8`](#insn-00bab5d8) 範囲 `[['00bab5d8', '00bab5df']]`
  - `CONDITIONAL_JUMP` [`00bab5dc`](#insn-00bab5dc) → [`00bab608`](#insn-00bab608)
  - `FALL_THROUGH` [`00bab5dc`](#insn-00bab5dc) → [`00bab5e0`](#insn-00bab5e0)
- ブロック [`00bab5e0`](#insn-00bab5e0) 範囲 `[['00bab5e0', '00bab5ef']]`
  - `CONDITIONAL_JUMP` [`00bab5ec`](#insn-00bab5ec) → [`00bab608`](#insn-00bab608)
  - `FALL_THROUGH` [`00bab5ec`](#insn-00bab5ec) → [`00bab5f0`](#insn-00bab5f0)
- ブロック [`00bab5f0`](#insn-00bab5f0) 範囲 `[['00bab5f0', '00bab607']]`
  - `UNCONDITIONAL_JUMP` [`00bab604`](#insn-00bab604) → [`00bab61c`](#insn-00bab61c)
- ブロック [`00bab608`](#insn-00bab608) 範囲 `[['00bab608', '00bab61b']]`
  - `FALL_THROUGH` [`00bab618`](#insn-00bab618) → [`00bab61c`](#insn-00bab61c)
- ブロック [`00bab61c`](#insn-00bab61c) 範囲 `[['00bab61c', '00bab627']]`
  - `FALL_THROUGH` [`00bab624`](#insn-00bab624) → [`00bab628`](#insn-00bab628)
- ブロック [`00bab628`](#insn-00bab628) 範囲 `[['00bab628', '00bab637']]`
  - `CONDITIONAL_JUMP` [`00bab634`](#insn-00bab634) → [`00bab7b8`](#insn-00bab7b8)
  - `FALL_THROUGH` [`00bab634`](#insn-00bab634) → [`00bab638`](#insn-00bab638)
- ブロック [`00bab638`](#insn-00bab638) 範囲 `[['00bab638', '00bab63f']]`
  - `CONDITIONAL_JUMP` [`00bab63c`](#insn-00bab63c) → [`00bab7b8`](#insn-00bab7b8)
  - `FALL_THROUGH` [`00bab63c`](#insn-00bab63c) → [`00bab640`](#insn-00bab640)
- ブロック [`00bab640`](#insn-00bab640) 範囲 `[['00bab640', '00bab647']]`
  - `CONDITIONAL_JUMP` [`00bab644`](#insn-00bab644) → [`00bab7ac`](#insn-00bab7ac)
  - `FALL_THROUGH` [`00bab644`](#insn-00bab644) → [`00bab648`](#insn-00bab648)
- ブロック [`00bab648`](#insn-00bab648) 範囲 `[['00bab648', '00bab64b']]`
  - `FALL_THROUGH` [`00bab648`](#insn-00bab648) → [`00bab64c`](#insn-00bab64c)
- ブロック [`00bab64c`](#insn-00bab64c) 範囲 `[['00bab64c', '00bab653']]`
  - `CONDITIONAL_JUMP` [`00bab650`](#insn-00bab650) → [`00bab7c0`](#insn-00bab7c0)
  - `FALL_THROUGH` [`00bab650`](#insn-00bab650) → [`00bab654`](#insn-00bab654)
- ブロック [`00bab654`](#insn-00bab654) 範囲 `[['00bab654', '00bab657']]`
  - `UNCONDITIONAL_JUMP` [`00bab654`](#insn-00bab654) → [`00bab7c4`](#insn-00bab7c4)
- ブロック [`00bab658`](#insn-00bab658) 範囲 `[['00bab658', '00bab65f']]`
  - `CONDITIONAL_JUMP` [`00bab65c`](#insn-00bab65c) → [`00bab688`](#insn-00bab688)
  - `FALL_THROUGH` [`00bab65c`](#insn-00bab65c) → [`00bab660`](#insn-00bab660)
- ブロック [`00bab660`](#insn-00bab660) 範囲 `[['00bab660', '00bab66f']]`
  - `CONDITIONAL_JUMP` [`00bab66c`](#insn-00bab66c) → [`00bab688`](#insn-00bab688)
  - `FALL_THROUGH` [`00bab66c`](#insn-00bab66c) → [`00bab670`](#insn-00bab670)
- ブロック [`00bab670`](#insn-00bab670) 範囲 `[['00bab670', '00bab67f']]`
  - `FALL_THROUGH` [`00bab67c`](#insn-00bab67c) → [`00bab680`](#insn-00bab680)
- ブロック [`00bab680`](#insn-00bab680) 範囲 `[['00bab680', '00bab687']]`
  - `UNCONDITIONAL_JUMP` [`00bab684`](#insn-00bab684) → [`00bab69c`](#insn-00bab69c)
- ブロック [`00bab688`](#insn-00bab688) 範囲 `[['00bab688', '00bab69b']]`
  - `FALL_THROUGH` [`00bab698`](#insn-00bab698) → [`00bab69c`](#insn-00bab69c)
- ブロック [`00bab69c`](#insn-00bab69c) 範囲 `[['00bab69c', '00bab69f']]`
  - `FALL_THROUGH` [`00bab69c`](#insn-00bab69c) → [`00bab6a0`](#insn-00bab6a0)
- ブロック [`00bab6a0`](#insn-00bab6a0) 範囲 `[['00bab6a0', '00bab6b7']]`
  - `CONDITIONAL_JUMP` [`00bab6b4`](#insn-00bab6b4) → [`00bab6cc`](#insn-00bab6cc)
  - `FALL_THROUGH` [`00bab6b4`](#insn-00bab6b4) → [`00bab6b8`](#insn-00bab6b8)
- ブロック [`00bab6b8`](#insn-00bab6b8) 範囲 `[['00bab6b8', '00bab6bf']]`
  - `CONDITIONAL_JUMP` [`00bab6bc`](#insn-00bab6bc) → [`00bab6cc`](#insn-00bab6cc)
  - `FALL_THROUGH` [`00bab6bc`](#insn-00bab6bc) → [`00bab6c0`](#insn-00bab6c0)
- ブロック [`00bab6c0`](#insn-00bab6c0) 範囲 `[['00bab6c0', '00bab6cb']]`
  - `FALL_THROUGH` [`00bab6c8`](#insn-00bab6c8) → [`00bab6cc`](#insn-00bab6cc)
- ブロック [`00bab6cc`](#insn-00bab6cc) 範囲 `[['00bab6cc', '00bab6d3']]`
  - `CONDITIONAL_JUMP` [`00bab6d0`](#insn-00bab6d0) → [`00bab6d8`](#insn-00bab6d8)
  - `FALL_THROUGH` [`00bab6d0`](#insn-00bab6d0) → [`00bab6d4`](#insn-00bab6d4)
- ブロック [`00bab6d4`](#insn-00bab6d4) 範囲 `[['00bab6d4', '00bab6d7']]`
  - `FALL_THROUGH` [`00bab6d4`](#insn-00bab6d4) → [`00bab6d8`](#insn-00bab6d8)
- ブロック [`00bab6d8`](#insn-00bab6d8) 範囲 `[['00bab6d8', '00bab6db']]`
  - `CONDITIONAL_JUMP` [`00bab6d8`](#insn-00bab6d8) → [`00bab6e0`](#insn-00bab6e0)
  - `FALL_THROUGH` [`00bab6d8`](#insn-00bab6d8) → [`00bab6dc`](#insn-00bab6dc)
- ブロック [`00bab6dc`](#insn-00bab6dc) 範囲 `[['00bab6dc', '00bab6df']]`
  - `FALL_THROUGH` [`00bab6dc`](#insn-00bab6dc) → [`00bab6e0`](#insn-00bab6e0)
- ブロック [`00bab6e0`](#insn-00bab6e0) 範囲 `[['00bab6e0', '00bab6eb']]`
  - `UNCONDITIONAL_JUMP` [`00bab6e8`](#insn-00bab6e8) → [`00bab3cc`](#insn-00bab3cc)
- ブロック [`00bab6ec`](#insn-00bab6ec) 範囲 `[['00bab6ec', '00bab6ef']]`
  - `FALL_THROUGH` [`00bab6ec`](#insn-00bab6ec) → [`00bab6f0`](#insn-00bab6f0)
- ブロック [`00bab6f0`](#insn-00bab6f0) 範囲 `[['00bab6f0', '00bab6f3']]`
  - `CONDITIONAL_JUMP` [`00bab6f0`](#insn-00bab6f0) → [`00bab71c`](#insn-00bab71c)
  - `FALL_THROUGH` [`00bab6f0`](#insn-00bab6f0) → [`00bab6f4`](#insn-00bab6f4)
- ブロック [`00bab6f4`](#insn-00bab6f4) 範囲 `[['00bab6f4', '00bab703']]`
  - `CONDITIONAL_JUMP` [`00bab700`](#insn-00bab700) → [`00bab71c`](#insn-00bab71c)
  - `FALL_THROUGH` [`00bab700`](#insn-00bab700) → [`00bab704`](#insn-00bab704)
- ブロック [`00bab704`](#insn-00bab704) 範囲 `[['00bab704', '00bab71b']]`
  - `UNCONDITIONAL_JUMP` [`00bab718`](#insn-00bab718) → [`00bab730`](#insn-00bab730)
- ブロック [`00bab71c`](#insn-00bab71c) 範囲 `[['00bab71c', '00bab72f']]`
  - `FALL_THROUGH` [`00bab72c`](#insn-00bab72c) → [`00bab730`](#insn-00bab730)
- ブロック [`00bab730`](#insn-00bab730) 範囲 `[['00bab730', '00bab73b']]`
  - `FALL_THROUGH` [`00bab738`](#insn-00bab738) → [`00bab73c`](#insn-00bab73c)
- ブロック [`00bab73c`](#insn-00bab73c) 範囲 `[['00bab73c', '00bab74b']]`
  - `CONDITIONAL_JUMP` [`00bab748`](#insn-00bab748) → [`00bab760`](#insn-00bab760)
  - `FALL_THROUGH` [`00bab748`](#insn-00bab748) → [`00bab74c`](#insn-00bab74c)
- ブロック [`00bab74c`](#insn-00bab74c) 範囲 `[['00bab74c', '00bab753']]`
  - `CONDITIONAL_JUMP` [`00bab750`](#insn-00bab750) → [`00bab760`](#insn-00bab760)
  - `FALL_THROUGH` [`00bab750`](#insn-00bab750) → [`00bab754`](#insn-00bab754)
- ブロック [`00bab754`](#insn-00bab754) 範囲 `[['00bab754', '00bab75f']]`
  - `FALL_THROUGH` [`00bab75c`](#insn-00bab75c) → [`00bab760`](#insn-00bab760)
- ブロック [`00bab760`](#insn-00bab760) 範囲 `[['00bab760', '00bab767']]`
  - `CONDITIONAL_JUMP` [`00bab764`](#insn-00bab764) → [`00bab76c`](#insn-00bab76c)
  - `FALL_THROUGH` [`00bab764`](#insn-00bab764) → [`00bab768`](#insn-00bab768)
- ブロック [`00bab768`](#insn-00bab768) 範囲 `[['00bab768', '00bab76b']]`
  - `FALL_THROUGH` [`00bab768`](#insn-00bab768) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab76c`](#insn-00bab76c) 範囲 `[['00bab76c', '00bab76f']]`
  - `CONDITIONAL_JUMP` [`00bab76c`](#insn-00bab76c) → [`00bab774`](#insn-00bab774)
  - `FALL_THROUGH` [`00bab76c`](#insn-00bab76c) → [`00bab770`](#insn-00bab770)
- ブロック [`00bab770`](#insn-00bab770) 範囲 `[['00bab770', '00bab773']]`
  - `FALL_THROUGH` [`00bab770`](#insn-00bab770) → [`00bab774`](#insn-00bab774)
- ブロック [`00bab774`](#insn-00bab774) 範囲 `[['00bab774', '00bab77b']]`
  - `UNCONDITIONAL_JUMP` [`00bab778`](#insn-00bab778) → [`00bab3cc`](#insn-00bab3cc)
- ブロック [`00bab77c`](#insn-00bab77c) 範囲 `[['00bab77c', '00bab787']]`
  - `FALL_THROUGH` [`00bab784`](#insn-00bab784) → [`00bab788`](#insn-00bab788)
- ブロック [`00bab788`](#insn-00bab788) 範囲 `[['00bab788', '00bab78b']]`
  - `FALL_THROUGH` [`00bab788`](#insn-00bab788) → [`00bab78c`](#insn-00bab78c)
- ブロック [`00bab78c`](#insn-00bab78c) 範囲 `[['00bab78c', '00bab78f']]`
  - `CONDITIONAL_JUMP` [`00bab78c`](#insn-00bab78c) → [`00bab794`](#insn-00bab794)
  - `FALL_THROUGH` [`00bab78c`](#insn-00bab78c) → [`00bab790`](#insn-00bab790)
- ブロック [`00bab790`](#insn-00bab790) 範囲 `[['00bab790', '00bab793']]`
  - `FALL_THROUGH` [`00bab790`](#insn-00bab790) → [`00bab794`](#insn-00bab794)
- ブロック [`00bab794`](#insn-00bab794) 範囲 `[['00bab794', '00bab797']]`
  - `CONDITIONAL_JUMP` [`00bab794`](#insn-00bab794) → [`00bab79c`](#insn-00bab79c)
  - `FALL_THROUGH` [`00bab794`](#insn-00bab794) → [`00bab798`](#insn-00bab798)
- ブロック [`00bab798`](#insn-00bab798) 範囲 `[['00bab798', '00bab79b']]`
  - `FALL_THROUGH` [`00bab798`](#insn-00bab798) → [`00bab79c`](#insn-00bab79c)
- ブロック [`00bab79c`](#insn-00bab79c) 範囲 `[['00bab79c', '00bab7ab']]`
  - `UNCONDITIONAL_JUMP` [`00bab7a8`](#insn-00bab7a8) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab7ac`](#insn-00bab7ac) 範囲 `[['00bab7ac', '00bab7b7']]`
  - `FALL_THROUGH` [`00bab7b4`](#insn-00bab7b4) → [`00bab7b8`](#insn-00bab7b8)
- ブロック [`00bab7b8`](#insn-00bab7b8) 範囲 `[['00bab7b8', '00bab7bf']]`
  - `CONDITIONAL_JUMP` [`00bab7bc`](#insn-00bab7bc) → [`00bab7c4`](#insn-00bab7c4)
  - `FALL_THROUGH` [`00bab7bc`](#insn-00bab7bc) → [`00bab7c0`](#insn-00bab7c0)
- ブロック [`00bab7c0`](#insn-00bab7c0) 範囲 `[['00bab7c0', '00bab7c3']]`
  - `FALL_THROUGH` [`00bab7c0`](#insn-00bab7c0) → [`00bab7c4`](#insn-00bab7c4)
- ブロック [`00bab7c4`](#insn-00bab7c4) 範囲 `[['00bab7c4', '00bab7c7']]`
  - `CONDITIONAL_JUMP` [`00bab7c4`](#insn-00bab7c4) → [`00bab7cc`](#insn-00bab7cc)
  - `FALL_THROUGH` [`00bab7c4`](#insn-00bab7c4) → [`00bab7c8`](#insn-00bab7c8)
- ブロック [`00bab7c8`](#insn-00bab7c8) 範囲 `[['00bab7c8', '00bab7cb']]`
  - `FALL_THROUGH` [`00bab7c8`](#insn-00bab7c8) → [`00bab7cc`](#insn-00bab7cc)
- ブロック [`00bab7cc`](#insn-00bab7cc) 範囲 `[['00bab7cc', '00bab7db']]`
  - `UNCONDITIONAL_JUMP` [`00bab7d8`](#insn-00bab7d8) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab7dc`](#insn-00bab7dc) 範囲 `[['00bab7dc', '00bab7df']]`
  - `FALL_THROUGH` [`00bab7dc`](#insn-00bab7dc) → [`00bab7e0`](#insn-00bab7e0)
- ブロック [`00bab7e0`](#insn-00bab7e0) 範囲 `[['00bab7e0', '00bab7f7']]`
  - `CONDITIONAL_JUMP` [`00bab7f4`](#insn-00bab7f4) → [`00bab800`](#insn-00bab800)
  - `FALL_THROUGH` [`00bab7f4`](#insn-00bab7f4) → [`00bab7f8`](#insn-00bab7f8)
- ブロック [`00bab7f8`](#insn-00bab7f8) 範囲 `[['00bab7f8', '00bab7ff']]`
  - `FALL_THROUGH` [`00bab7fc`](#insn-00bab7fc) → [`00bab800`](#insn-00bab800)
- ブロック [`00bab800`](#insn-00bab800) 範囲 `[['00bab800', '00bab807']]`
  - `FALL_THROUGH` [`00bab804`](#insn-00bab804) → [`00bab808`](#insn-00bab808)
- ブロック [`00bab808`](#insn-00bab808) 範囲 `[['00bab808', '00bab823']]`
  - `UNCONDITIONAL_JUMP` [`00bab820`](#insn-00bab820) → [`00bab3cc`](#insn-00bab3cc)
- ブロック [`00bab824`](#insn-00bab824) 範囲 `[['00bab824', '00bab827']]`

## 命令位置別の参照

- [`00baaf10`](#insn-00baaf10) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf14`](#insn-00baaf14) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf18`](#insn-00baaf18) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf28`](#insn-00baaf28) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf34`](#insn-00baaf34) → [`00bab1ac`](#insn-00bab1ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baaf54::default` · 推定型 `None`
- [`00baaf44`](#insn-00baaf44) → `0030e1f3`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::switchdataD_0030e1f3` · 推定型 `byte`
- [`00baaf54`](#insn-00baaf54) → [`00baaf58`](#insn-00baaf58) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_0` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab1b4`](#insn-00bab1b4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_1` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab134`](#insn-00bab134) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_2` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab17c`](#insn-00bab17c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_3` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab018`](#insn-00bab018) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_4` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab1cc`](#insn-00bab1cc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_5` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab1e4`](#insn-00bab1e4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_6` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab194`](#insn-00bab194) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_7` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab1fc`](#insn-00bab1fc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_8` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab060`](#insn-00bab060) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_9` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab214`](#insn-00bab214) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_a` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00baafa0`](#insn-00baafa0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_b` · 推定型 `None`
- [`00baaf54`](#insn-00baaf54) → [`00bab0b8`](#insn-00bab0b8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baaf54::caseD_c` · 推定型 `None`
- [`00baaf58`](#insn-00baaf58) → [`00baaf60`](#insn-00baaf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf5c`](#insn-00baaf5c) → [`00bab1bc`](#insn-00bab1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf78`](#insn-00baaf78) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf8c`](#insn-00baaf8c) → [`00bab33c`](#insn-00bab33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf98`](#insn-00baaf98) → [`00baaf80`](#insn-00baaf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf9c`](#insn-00baaf9c) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa0`](#insn-00baafa0) → [`00baafac`](#insn-00baafac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafa8`](#insn-00baafa8) → [`00baaffc`](#insn-00baaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc8`](#insn-00baafc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafcc`](#insn-00baafcc) → [`00c585b0`](../00c58/00c585b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c585b0` · 推定シンボル `None` · 推定型 `None`
- [`00baafd0`](#insn-00baafd0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafdc`](#insn-00baafdc) → [`00baaffc`](#insn-00baaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafe4`](#insn-00baafe4) → [`00baaffc`](#insn-00baaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaff0`](#insn-00baaff0) → [`00baaffc`](#insn-00baaffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab000`](#insn-00bab000) → [`00bab008`](#insn-00bab008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab008`](#insn-00bab008) → [`00bab010`](#insn-00bab010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab014`](#insn-00bab014) → [`00bab12c`](#insn-00bab12c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab018`](#insn-00bab018) → [`00bab020`](#insn-00bab020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab01c`](#insn-00bab01c) → [`00bab1bc`](#insn-00bab1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab038`](#insn-00bab038) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab04c`](#insn-00bab04c) → [`00bab33c`](#insn-00bab33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab058`](#insn-00bab058) → [`00bab040`](#insn-00bab040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab05c`](#insn-00bab05c) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab060`](#insn-00bab060) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → [`00bab06c`](#insn-00bab06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab068`](#insn-00bab068) → [`00bab090`](#insn-00bab090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab08c`](#insn-00bab08c) → [`00c5c1b0`](../00c5c/00c5c1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a4`](#insn-00bab0a4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a8`](#insn-00bab0a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b4`](#insn-00bab0b4) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b8`](#insn-00bab0b8) → [`00bab0c4`](#insn-00bab0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0c0`](#insn-00bab0c0) → [`00bab114`](#insn-00bab114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e0`](#insn-00bab0e0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e4`](#insn-00bab0e4) → [`00c585c0`](../00c58/00c585c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c585c0` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e8`](#insn-00bab0e8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f4`](#insn-00bab0f4) → [`00bab114`](#insn-00bab114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0fc`](#insn-00bab0fc) → [`00bab114`](#insn-00bab114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab108`](#insn-00bab108) → [`00bab114`](#insn-00bab114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab118`](#insn-00bab118) → [`00bab120`](#insn-00bab120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab120`](#insn-00bab120) → [`00bab128`](#insn-00bab128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab130`](#insn-00bab130) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab134`](#insn-00bab134) → [`00bab13c`](#insn-00bab13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab138`](#insn-00bab138) → [`00bab1bc`](#insn-00bab1bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab154`](#insn-00bab154) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab168`](#insn-00bab168) → [`00bab33c`](#insn-00bab33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab174`](#insn-00bab174) → [`00bab15c`](#insn-00bab15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab178`](#insn-00bab178) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab17c`](#insn-00bab17c) → [`00bab27c`](#insn-00bab27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab180`](#insn-00bab180) → [`00bab27c`](#insn-00bab27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab18c`](#insn-00bab18c) → [`00bab790`](#insn-00bab790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab190`](#insn-00bab190) → [`00bab794`](#insn-00bab794) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab194`](#insn-00bab194) → [`00bab2bc`](#insn-00bab2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab198`](#insn-00bab198) → [`00bab2bc`](#insn-00bab2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1a4`](#insn-00bab1a4) → [`00bab5c0`](#insn-00bab5c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1a8`](#insn-00bab1a8) → [`00bab5c4`](#insn-00bab5c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b0`](#insn-00bab1b0) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b4`](#insn-00bab1b4) → [`00bab2fc`](#insn-00bab2fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b8`](#insn-00bab1b8) → [`00bab2fc`](#insn-00bab2fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c4`](#insn-00bab1c4) → [`00bab3b8`](#insn-00bab3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c8`](#insn-00bab1c8) → [`00bab3bc`](#insn-00bab3bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1cc`](#insn-00bab1cc) → [`00bab3f4`](#insn-00bab3f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1d0`](#insn-00bab1d0) → [`00bab3f4`](#insn-00bab3f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1dc`](#insn-00bab1dc) → [`00bab7c0`](#insn-00bab7c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e0`](#insn-00bab1e0) → [`00bab7c4`](#insn-00bab7c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e4`](#insn-00bab1e4) → [`00bab434`](#insn-00bab434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e8`](#insn-00bab1e8) → [`00bab434`](#insn-00bab434) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f4`](#insn-00bab1f4) → [`00bab6d4`](#insn-00bab6d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f8`](#insn-00bab1f8) → [`00bab6d8`](#insn-00bab6d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1fc`](#insn-00bab1fc) → [`00bab474`](#insn-00bab474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab200`](#insn-00bab200) → [`00bab474`](#insn-00bab474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab20c`](#insn-00bab20c) → [`00bab768`](#insn-00bab768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab210`](#insn-00bab210) → [`00bab76c`](#insn-00bab76c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab214`](#insn-00bab214) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab218`](#insn-00bab218) → [`00bab220`](#insn-00bab220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab21c`](#insn-00bab21c) → [`00bab800`](#insn-00bab800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab244`](#insn-00bab244) → [`00c5c1c0`](../00c5c/00c5c1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bab248`](#insn-00bab248) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab24c`](#insn-00bab24c) → [`00bab800`](#insn-00bab800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab250`](#insn-00bab250) → [`00bab800`](#insn-00bab800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab258`](#insn-00bab258) → [`00bab7dc`](#insn-00bab7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab26c`](#insn-00bab26c) → [`00bab7e0`](#insn-00bab7e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab274`](#insn-00bab274) → [`00bab260`](#insn-00bab260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab278`](#insn-00bab278) → [`00bab7e0`](#insn-00bab7e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab294`](#insn-00bab294) → [`00bab4e4`](#insn-00bab4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2a8`](#insn-00bab2a8) → [`00bab4b4`](#insn-00bab4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b4`](#insn-00bab2b4) → [`00bab29c`](#insn-00bab29c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b8`](#insn-00bab2b8) → [`00bab4e4`](#insn-00bab4e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2d4`](#insn-00bab2d4) → [`00bab564`](#insn-00bab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e8`](#insn-00bab2e8) → [`00bab534`](#insn-00bab534) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f4`](#insn-00bab2f4) → [`00bab2dc`](#insn-00bab2dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f8`](#insn-00bab2f8) → [`00bab564`](#insn-00bab564) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab314`](#insn-00bab314) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab328`](#insn-00bab328) → [`00bab33c`](#insn-00bab33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab334`](#insn-00bab334) → [`00bab31c`](#insn-00bab31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab338`](#insn-00bab338) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab340`](#insn-00bab340) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab350`](#insn-00bab350) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab358`](#insn-00bab358) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab364`](#insn-00bab364) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab368`](#insn-00bab368) → [`00bab380`](#insn-00bab380) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab370`](#insn-00bab370) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab374`](#insn-00bab374) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab380`](#insn-00bab380) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab388`](#insn-00bab388) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab38c`](#insn-00bab38c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab398`](#insn-00bab398) → [`00bab3b0`](#insn-00bab3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3a0`](#insn-00bab3a0) → [`00bab3b0`](#insn-00bab3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3b4`](#insn-00bab3b4) → [`00bab3bc`](#insn-00bab3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3bc`](#insn-00bab3bc) → [`00bab3c4`](#insn-00bab3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3d4`](#insn-00bab3d4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3dc`](#insn-00bab3dc) → [`00bab824`](#insn-00bab824) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3e0`](#insn-00bab3e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3e4`](#insn-00bab3e4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3e8`](#insn-00bab3e8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab40c`](#insn-00bab40c) → [`00bab608`](#insn-00bab608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab420`](#insn-00bab420) → [`00bab5d8`](#insn-00bab5d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab42c`](#insn-00bab42c) → [`00bab414`](#insn-00bab414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab430`](#insn-00bab430) → [`00bab608`](#insn-00bab608) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab44c`](#insn-00bab44c) → [`00bab688`](#insn-00bab688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab460`](#insn-00bab460) → [`00bab658`](#insn-00bab658) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab46c`](#insn-00bab46c) → [`00bab454`](#insn-00bab454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab470`](#insn-00bab470) → [`00bab688`](#insn-00bab688) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab48c`](#insn-00bab48c) → [`00bab71c`](#insn-00bab71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4a0`](#insn-00bab4a0) → [`00bab6ec`](#insn-00bab6ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4ac`](#insn-00bab4ac) → [`00bab494`](#insn-00bab494) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4b0`](#insn-00bab4b0) → [`00bab71c`](#insn-00bab71c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4b8`](#insn-00bab4b8) → [`00bab4e4`](#insn-00bab4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4c8`](#insn-00bab4c8) → [`00bab4e4`](#insn-00bab4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4d0`](#insn-00bab4d0) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab4dc`](#insn-00bab4dc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4e0`](#insn-00bab4e0) → [`00bab4f8`](#insn-00bab4f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4e8`](#insn-00bab4e8) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab4ec`](#insn-00bab4ec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab4f8`](#insn-00bab4f8) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab500`](#insn-00bab500) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab504`](#insn-00bab504) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab510`](#insn-00bab510) → [`00bab788`](#insn-00bab788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab518`](#insn-00bab518) → [`00bab788`](#insn-00bab788) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab520`](#insn-00bab520) → [`00bab77c`](#insn-00bab77c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab52c`](#insn-00bab52c) → [`00bab790`](#insn-00bab790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab530`](#insn-00bab530) → [`00bab794`](#insn-00bab794) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab538`](#insn-00bab538) → [`00bab564`](#insn-00bab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab548`](#insn-00bab548) → [`00bab564`](#insn-00bab564) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab550`](#insn-00bab550) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab55c`](#insn-00bab55c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab560`](#insn-00bab560) → [`00bab578`](#insn-00bab578) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab568`](#insn-00bab568) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab56c`](#insn-00bab56c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab578`](#insn-00bab578) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab580`](#insn-00bab580) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab584`](#insn-00bab584) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab590`](#insn-00bab590) → [`00bab5b8`](#insn-00bab5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab598`](#insn-00bab598) → [`00bab5b8`](#insn-00bab5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5a4`](#insn-00bab5a4) → [`00bab5b8`](#insn-00bab5b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5bc`](#insn-00bab5bc) → [`00bab5c4`](#insn-00bab5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5c4`](#insn-00bab5c4) → [`00bab5cc`](#insn-00bab5cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5d4`](#insn-00bab5d4) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5dc`](#insn-00bab5dc) → [`00bab608`](#insn-00bab608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5ec`](#insn-00bab5ec) → [`00bab608`](#insn-00bab608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab5f4`](#insn-00bab5f4) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab600`](#insn-00bab600) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab604`](#insn-00bab604) → [`00bab61c`](#insn-00bab61c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab60c`](#insn-00bab60c) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab610`](#insn-00bab610) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab61c`](#insn-00bab61c) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab624`](#insn-00bab624) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab628`](#insn-00bab628) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab634`](#insn-00bab634) → [`00bab7b8`](#insn-00bab7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab63c`](#insn-00bab63c) → [`00bab7b8`](#insn-00bab7b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab644`](#insn-00bab644) → [`00bab7ac`](#insn-00bab7ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab650`](#insn-00bab650) → [`00bab7c0`](#insn-00bab7c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab654`](#insn-00bab654) → [`00bab7c4`](#insn-00bab7c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab65c`](#insn-00bab65c) → [`00bab688`](#insn-00bab688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab66c`](#insn-00bab66c) → [`00bab688`](#insn-00bab688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab674`](#insn-00bab674) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab680`](#insn-00bab680) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab684`](#insn-00bab684) → [`00bab69c`](#insn-00bab69c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab68c`](#insn-00bab68c) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab690`](#insn-00bab690) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab69c`](#insn-00bab69c) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab6a4`](#insn-00bab6a4) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab6a8`](#insn-00bab6a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6b4`](#insn-00bab6b4) → [`00bab6cc`](#insn-00bab6cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6bc`](#insn-00bab6bc) → [`00bab6cc`](#insn-00bab6cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d0`](#insn-00bab6d0) → [`00bab6d8`](#insn-00bab6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d8`](#insn-00bab6d8) → [`00bab6e0`](#insn-00bab6e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6e8`](#insn-00bab6e8) → [`00bab3cc`](#insn-00bab3cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6f0`](#insn-00bab6f0) → [`00bab71c`](#insn-00bab71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab700`](#insn-00bab700) → [`00bab71c`](#insn-00bab71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab708`](#insn-00bab708) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab714`](#insn-00bab714) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab718`](#insn-00bab718) → [`00bab730`](#insn-00bab730) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab720`](#insn-00bab720) → `00c9b830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab724`](#insn-00bab724) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab730`](#insn-00bab730) → `011261e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab738`](#insn-00bab738) → [`00c5d150`](../00c5d/00c5d150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d150` · 推定シンボル `None` · 推定型 `None`
- [`00bab73c`](#insn-00bab73c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab748`](#insn-00bab748) → [`00bab760`](#insn-00bab760) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab750`](#insn-00bab750) → [`00bab760`](#insn-00bab760) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab764`](#insn-00bab764) → [`00bab76c`](#insn-00bab76c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab76c`](#insn-00bab76c) → [`00bab774`](#insn-00bab774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab778`](#insn-00bab778) → [`00bab3cc`](#insn-00bab3cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab78c`](#insn-00bab78c) → [`00bab794`](#insn-00bab794) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab794`](#insn-00bab794) → [`00bab79c`](#insn-00bab79c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7a8`](#insn-00bab7a8) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7bc`](#insn-00bab7bc) → [`00bab7c4`](#insn-00bab7c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7c4`](#insn-00bab7c4) → [`00bab7cc`](#insn-00bab7cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7d8`](#insn-00bab7d8) → [`00bab3d0`](#insn-00bab3d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7f4`](#insn-00bab7f4) → [`00bab800`](#insn-00bab800) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab7fc`](#insn-00bab7fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab814`](#insn-00bab814) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab818`](#insn-00bab818) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab820`](#insn-00bab820) → [`00bab3cc`](#insn-00bab3cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab824`](#insn-00bab824) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaf10`](#insn-00baaf10)

~~~json
{
  "source": "00baaf10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf14`](#insn-00baaf14)

~~~json
{
  "source": "00baaf14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf18`](#insn-00baaf18)

~~~json
{
  "source": "00baaf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf28`](#insn-00baaf28)

~~~json
{
  "source": "00baaf28",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf34`](#insn-00baaf34)

~~~json
{
  "source": "00baaf34",
  "target": "00bab1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf44`](#insn-00baaf44)

~~~json
{
  "source": "00baaf44",
  "target": "0030e1f3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e1f3",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e1f3",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00baaf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00baafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf54`](#insn-00baaf54)

~~~json
{
  "source": "00baaf54",
  "target": "00bab0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf58`](#insn-00baaf58)

~~~json
{
  "source": "00baaf58",
  "target": "00baaf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf5c`](#insn-00baaf5c)

~~~json
{
  "source": "00baaf5c",
  "target": "00bab1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf78`](#insn-00baaf78)

~~~json
{
  "source": "00baaf78",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf8c`](#insn-00baaf8c)

~~~json
{
  "source": "00baaf8c",
  "target": "00bab33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf98`](#insn-00baaf98)

~~~json
{
  "source": "00baaf98",
  "target": "00baaf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf9c`](#insn-00baaf9c)

~~~json
{
  "source": "00baaf9c",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa0`](#insn-00baafa0)

~~~json
{
  "source": "00baafa0",
  "target": "00baafac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafa8`](#insn-00baafa8)

~~~json
{
  "source": "00baafa8",
  "target": "00baaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc8`](#insn-00baafc8)

~~~json
{
  "source": "00baafc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafcc`](#insn-00baafcc)

~~~json
{
  "source": "00baafcc",
  "target": "00c585b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baafd0`](#insn-00baafd0)

~~~json
{
  "source": "00baafd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafdc`](#insn-00baafdc)

~~~json
{
  "source": "00baafdc",
  "target": "00baaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafe4`](#insn-00baafe4)

~~~json
{
  "source": "00baafe4",
  "target": "00baaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff0`](#insn-00baaff0)

~~~json
{
  "source": "00baaff0",
  "target": "00baaffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab000`](#insn-00bab000)

~~~json
{
  "source": "00bab000",
  "target": "00bab008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab008`](#insn-00bab008)

~~~json
{
  "source": "00bab008",
  "target": "00bab010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab014`](#insn-00bab014)

~~~json
{
  "source": "00bab014",
  "target": "00bab12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab018`](#insn-00bab018)

~~~json
{
  "source": "00bab018",
  "target": "00bab020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab01c`](#insn-00bab01c)

~~~json
{
  "source": "00bab01c",
  "target": "00bab1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab038`](#insn-00bab038)

~~~json
{
  "source": "00bab038",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab04c`](#insn-00bab04c)

~~~json
{
  "source": "00bab04c",
  "target": "00bab33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab058`](#insn-00bab058)

~~~json
{
  "source": "00bab058",
  "target": "00bab040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab05c`](#insn-00bab05c)

~~~json
{
  "source": "00bab05c",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab060`](#insn-00bab060)

~~~json
{
  "source": "00bab060",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "00bab06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab068`](#insn-00bab068)

~~~json
{
  "source": "00bab068",
  "target": "00bab090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab08c`](#insn-00bab08c)

~~~json
{
  "source": "00bab08c",
  "target": "00c5c1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab0a4`](#insn-00bab0a4)

~~~json
{
  "source": "00bab0a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0a8`](#insn-00bab0a8)

~~~json
{
  "source": "00bab0a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b4`](#insn-00bab0b4)

~~~json
{
  "source": "00bab0b4",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b8`](#insn-00bab0b8)

~~~json
{
  "source": "00bab0b8",
  "target": "00bab0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0c0`](#insn-00bab0c0)

~~~json
{
  "source": "00bab0c0",
  "target": "00bab114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0e0`](#insn-00bab0e0)

~~~json
{
  "source": "00bab0e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0e4`](#insn-00bab0e4)

~~~json
{
  "source": "00bab0e4",
  "target": "00c585c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab0e8`](#insn-00bab0e8)

~~~json
{
  "source": "00bab0e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f4`](#insn-00bab0f4)

~~~json
{
  "source": "00bab0f4",
  "target": "00bab114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0fc`](#insn-00bab0fc)

~~~json
{
  "source": "00bab0fc",
  "target": "00bab114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab108`](#insn-00bab108)

~~~json
{
  "source": "00bab108",
  "target": "00bab114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab118`](#insn-00bab118)

~~~json
{
  "source": "00bab118",
  "target": "00bab120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab120`](#insn-00bab120)

~~~json
{
  "source": "00bab120",
  "target": "00bab128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab130`](#insn-00bab130)

~~~json
{
  "source": "00bab130",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab134`](#insn-00bab134)

~~~json
{
  "source": "00bab134",
  "target": "00bab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab138`](#insn-00bab138)

~~~json
{
  "source": "00bab138",
  "target": "00bab1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab154`](#insn-00bab154)

~~~json
{
  "source": "00bab154",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab168`](#insn-00bab168)

~~~json
{
  "source": "00bab168",
  "target": "00bab33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab174`](#insn-00bab174)

~~~json
{
  "source": "00bab174",
  "target": "00bab15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab178`](#insn-00bab178)

~~~json
{
  "source": "00bab178",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab17c`](#insn-00bab17c)

~~~json
{
  "source": "00bab17c",
  "target": "00bab27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab180`](#insn-00bab180)

~~~json
{
  "source": "00bab180",
  "target": "00bab27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab18c`](#insn-00bab18c)

~~~json
{
  "source": "00bab18c",
  "target": "00bab790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab190`](#insn-00bab190)

~~~json
{
  "source": "00bab190",
  "target": "00bab794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab194`](#insn-00bab194)

~~~json
{
  "source": "00bab194",
  "target": "00bab2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab198`](#insn-00bab198)

~~~json
{
  "source": "00bab198",
  "target": "00bab2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1a4`](#insn-00bab1a4)

~~~json
{
  "source": "00bab1a4",
  "target": "00bab5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1a8`](#insn-00bab1a8)

~~~json
{
  "source": "00bab1a8",
  "target": "00bab5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b0`](#insn-00bab1b0)

~~~json
{
  "source": "00bab1b0",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b4`](#insn-00bab1b4)

~~~json
{
  "source": "00bab1b4",
  "target": "00bab2fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b8`](#insn-00bab1b8)

~~~json
{
  "source": "00bab1b8",
  "target": "00bab2fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1c4`](#insn-00bab1c4)

~~~json
{
  "source": "00bab1c4",
  "target": "00bab3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1c8`](#insn-00bab1c8)

~~~json
{
  "source": "00bab1c8",
  "target": "00bab3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1cc`](#insn-00bab1cc)

~~~json
{
  "source": "00bab1cc",
  "target": "00bab3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1d0`](#insn-00bab1d0)

~~~json
{
  "source": "00bab1d0",
  "target": "00bab3f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1dc`](#insn-00bab1dc)

~~~json
{
  "source": "00bab1dc",
  "target": "00bab7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e0`](#insn-00bab1e0)

~~~json
{
  "source": "00bab1e0",
  "target": "00bab7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e4`](#insn-00bab1e4)

~~~json
{
  "source": "00bab1e4",
  "target": "00bab434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e8`](#insn-00bab1e8)

~~~json
{
  "source": "00bab1e8",
  "target": "00bab434",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f4`](#insn-00bab1f4)

~~~json
{
  "source": "00bab1f4",
  "target": "00bab6d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f8`](#insn-00bab1f8)

~~~json
{
  "source": "00bab1f8",
  "target": "00bab6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1fc`](#insn-00bab1fc)

~~~json
{
  "source": "00bab1fc",
  "target": "00bab474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab200`](#insn-00bab200)

~~~json
{
  "source": "00bab200",
  "target": "00bab474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab20c`](#insn-00bab20c)

~~~json
{
  "source": "00bab20c",
  "target": "00bab768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab210`](#insn-00bab210)

~~~json
{
  "source": "00bab210",
  "target": "00bab76c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab214`](#insn-00bab214)

~~~json
{
  "source": "00bab214",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab218`](#insn-00bab218)

~~~json
{
  "source": "00bab218",
  "target": "00bab220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab21c`](#insn-00bab21c)

~~~json
{
  "source": "00bab21c",
  "target": "00bab800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab244`](#insn-00bab244)

~~~json
{
  "source": "00bab244",
  "target": "00c5c1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab248`](#insn-00bab248)

~~~json
{
  "source": "00bab248",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab24c`](#insn-00bab24c)

~~~json
{
  "source": "00bab24c",
  "target": "00bab800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab250`](#insn-00bab250)

~~~json
{
  "source": "00bab250",
  "target": "00bab800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab258`](#insn-00bab258)

~~~json
{
  "source": "00bab258",
  "target": "00bab7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab26c`](#insn-00bab26c)

~~~json
{
  "source": "00bab26c",
  "target": "00bab7e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab274`](#insn-00bab274)

~~~json
{
  "source": "00bab274",
  "target": "00bab260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab278`](#insn-00bab278)

~~~json
{
  "source": "00bab278",
  "target": "00bab7e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab294`](#insn-00bab294)

~~~json
{
  "source": "00bab294",
  "target": "00bab4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2a8`](#insn-00bab2a8)

~~~json
{
  "source": "00bab2a8",
  "target": "00bab4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b4`](#insn-00bab2b4)

~~~json
{
  "source": "00bab2b4",
  "target": "00bab29c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b8`](#insn-00bab2b8)

~~~json
{
  "source": "00bab2b8",
  "target": "00bab4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2d4`](#insn-00bab2d4)

~~~json
{
  "source": "00bab2d4",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e8`](#insn-00bab2e8)

~~~json
{
  "source": "00bab2e8",
  "target": "00bab534",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f4`](#insn-00bab2f4)

~~~json
{
  "source": "00bab2f4",
  "target": "00bab2dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f8`](#insn-00bab2f8)

~~~json
{
  "source": "00bab2f8",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab314`](#insn-00bab314)

~~~json
{
  "source": "00bab314",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab328`](#insn-00bab328)

~~~json
{
  "source": "00bab328",
  "target": "00bab33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab334`](#insn-00bab334)

~~~json
{
  "source": "00bab334",
  "target": "00bab31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab338`](#insn-00bab338)

~~~json
{
  "source": "00bab338",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab340`](#insn-00bab340)

~~~json
{
  "source": "00bab340",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab350`](#insn-00bab350)

~~~json
{
  "source": "00bab350",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab358`](#insn-00bab358)

~~~json
{
  "source": "00bab358",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab364`](#insn-00bab364)

~~~json
{
  "source": "00bab364",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab368`](#insn-00bab368)

~~~json
{
  "source": "00bab368",
  "target": "00bab380",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab370`](#insn-00bab370)

~~~json
{
  "source": "00bab370",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab374`](#insn-00bab374)

~~~json
{
  "source": "00bab374",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab380`](#insn-00bab380)

~~~json
{
  "source": "00bab380",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab388`](#insn-00bab388)

~~~json
{
  "source": "00bab388",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab38c`](#insn-00bab38c)

~~~json
{
  "source": "00bab38c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab398`](#insn-00bab398)

~~~json
{
  "source": "00bab398",
  "target": "00bab3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3a0`](#insn-00bab3a0)

~~~json
{
  "source": "00bab3a0",
  "target": "00bab3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3b4`](#insn-00bab3b4)

~~~json
{
  "source": "00bab3b4",
  "target": "00bab3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3bc`](#insn-00bab3bc)

~~~json
{
  "source": "00bab3bc",
  "target": "00bab3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3d4`](#insn-00bab3d4)

~~~json
{
  "source": "00bab3d4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3dc`](#insn-00bab3dc)

~~~json
{
  "source": "00bab3dc",
  "target": "00bab824",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3e0`](#insn-00bab3e0)

~~~json
{
  "source": "00bab3e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3e4`](#insn-00bab3e4)

~~~json
{
  "source": "00bab3e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3e8`](#insn-00bab3e8)

~~~json
{
  "source": "00bab3e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab40c`](#insn-00bab40c)

~~~json
{
  "source": "00bab40c",
  "target": "00bab608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab420`](#insn-00bab420)

~~~json
{
  "source": "00bab420",
  "target": "00bab5d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab42c`](#insn-00bab42c)

~~~json
{
  "source": "00bab42c",
  "target": "00bab414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab430`](#insn-00bab430)

~~~json
{
  "source": "00bab430",
  "target": "00bab608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab44c`](#insn-00bab44c)

~~~json
{
  "source": "00bab44c",
  "target": "00bab688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab460`](#insn-00bab460)

~~~json
{
  "source": "00bab460",
  "target": "00bab658",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab46c`](#insn-00bab46c)

~~~json
{
  "source": "00bab46c",
  "target": "00bab454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab470`](#insn-00bab470)

~~~json
{
  "source": "00bab470",
  "target": "00bab688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab48c`](#insn-00bab48c)

~~~json
{
  "source": "00bab48c",
  "target": "00bab71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4a0`](#insn-00bab4a0)

~~~json
{
  "source": "00bab4a0",
  "target": "00bab6ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4ac`](#insn-00bab4ac)

~~~json
{
  "source": "00bab4ac",
  "target": "00bab494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4b0`](#insn-00bab4b0)

~~~json
{
  "source": "00bab4b0",
  "target": "00bab71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4b8`](#insn-00bab4b8)

~~~json
{
  "source": "00bab4b8",
  "target": "00bab4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4c8`](#insn-00bab4c8)

~~~json
{
  "source": "00bab4c8",
  "target": "00bab4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4d0`](#insn-00bab4d0)

~~~json
{
  "source": "00bab4d0",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab4dc`](#insn-00bab4dc)

~~~json
{
  "source": "00bab4dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4e0`](#insn-00bab4e0)

~~~json
{
  "source": "00bab4e0",
  "target": "00bab4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4e8`](#insn-00bab4e8)

~~~json
{
  "source": "00bab4e8",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab4ec`](#insn-00bab4ec)

~~~json
{
  "source": "00bab4ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab4f8`](#insn-00bab4f8)

~~~json
{
  "source": "00bab4f8",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab500`](#insn-00bab500)

~~~json
{
  "source": "00bab500",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab504`](#insn-00bab504)

~~~json
{
  "source": "00bab504",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab510`](#insn-00bab510)

~~~json
{
  "source": "00bab510",
  "target": "00bab788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab518`](#insn-00bab518)

~~~json
{
  "source": "00bab518",
  "target": "00bab788",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab520`](#insn-00bab520)

~~~json
{
  "source": "00bab520",
  "target": "00bab77c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab52c`](#insn-00bab52c)

~~~json
{
  "source": "00bab52c",
  "target": "00bab790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab530`](#insn-00bab530)

~~~json
{
  "source": "00bab530",
  "target": "00bab794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab538`](#insn-00bab538)

~~~json
{
  "source": "00bab538",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab548`](#insn-00bab548)

~~~json
{
  "source": "00bab548",
  "target": "00bab564",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab550`](#insn-00bab550)

~~~json
{
  "source": "00bab550",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab55c`](#insn-00bab55c)

~~~json
{
  "source": "00bab55c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab560`](#insn-00bab560)

~~~json
{
  "source": "00bab560",
  "target": "00bab578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab568`](#insn-00bab568)

~~~json
{
  "source": "00bab568",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab56c`](#insn-00bab56c)

~~~json
{
  "source": "00bab56c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab578`](#insn-00bab578)

~~~json
{
  "source": "00bab578",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab580`](#insn-00bab580)

~~~json
{
  "source": "00bab580",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab584`](#insn-00bab584)

~~~json
{
  "source": "00bab584",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab590`](#insn-00bab590)

~~~json
{
  "source": "00bab590",
  "target": "00bab5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab598`](#insn-00bab598)

~~~json
{
  "source": "00bab598",
  "target": "00bab5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5a4`](#insn-00bab5a4)

~~~json
{
  "source": "00bab5a4",
  "target": "00bab5b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5bc`](#insn-00bab5bc)

~~~json
{
  "source": "00bab5bc",
  "target": "00bab5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5c4`](#insn-00bab5c4)

~~~json
{
  "source": "00bab5c4",
  "target": "00bab5cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5d4`](#insn-00bab5d4)

~~~json
{
  "source": "00bab5d4",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5dc`](#insn-00bab5dc)

~~~json
{
  "source": "00bab5dc",
  "target": "00bab608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5ec`](#insn-00bab5ec)

~~~json
{
  "source": "00bab5ec",
  "target": "00bab608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab5f4`](#insn-00bab5f4)

~~~json
{
  "source": "00bab5f4",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab600`](#insn-00bab600)

~~~json
{
  "source": "00bab600",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab604`](#insn-00bab604)

~~~json
{
  "source": "00bab604",
  "target": "00bab61c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab60c`](#insn-00bab60c)

~~~json
{
  "source": "00bab60c",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab610`](#insn-00bab610)

~~~json
{
  "source": "00bab610",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab61c`](#insn-00bab61c)

~~~json
{
  "source": "00bab61c",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab624`](#insn-00bab624)

~~~json
{
  "source": "00bab624",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab628`](#insn-00bab628)

~~~json
{
  "source": "00bab628",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab634`](#insn-00bab634)

~~~json
{
  "source": "00bab634",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab63c`](#insn-00bab63c)

~~~json
{
  "source": "00bab63c",
  "target": "00bab7b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab644`](#insn-00bab644)

~~~json
{
  "source": "00bab644",
  "target": "00bab7ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab650`](#insn-00bab650)

~~~json
{
  "source": "00bab650",
  "target": "00bab7c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab654`](#insn-00bab654)

~~~json
{
  "source": "00bab654",
  "target": "00bab7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab65c`](#insn-00bab65c)

~~~json
{
  "source": "00bab65c",
  "target": "00bab688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab66c`](#insn-00bab66c)

~~~json
{
  "source": "00bab66c",
  "target": "00bab688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab674`](#insn-00bab674)

~~~json
{
  "source": "00bab674",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab680`](#insn-00bab680)

~~~json
{
  "source": "00bab680",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab684`](#insn-00bab684)

~~~json
{
  "source": "00bab684",
  "target": "00bab69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab68c`](#insn-00bab68c)

~~~json
{
  "source": "00bab68c",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab690`](#insn-00bab690)

~~~json
{
  "source": "00bab690",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab69c`](#insn-00bab69c)

~~~json
{
  "source": "00bab69c",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab6a4`](#insn-00bab6a4)

~~~json
{
  "source": "00bab6a4",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab6a8`](#insn-00bab6a8)

~~~json
{
  "source": "00bab6a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6b4`](#insn-00bab6b4)

~~~json
{
  "source": "00bab6b4",
  "target": "00bab6cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6bc`](#insn-00bab6bc)

~~~json
{
  "source": "00bab6bc",
  "target": "00bab6cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d0`](#insn-00bab6d0)

~~~json
{
  "source": "00bab6d0",
  "target": "00bab6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d8`](#insn-00bab6d8)

~~~json
{
  "source": "00bab6d8",
  "target": "00bab6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6e8`](#insn-00bab6e8)

~~~json
{
  "source": "00bab6e8",
  "target": "00bab3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6f0`](#insn-00bab6f0)

~~~json
{
  "source": "00bab6f0",
  "target": "00bab71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab700`](#insn-00bab700)

~~~json
{
  "source": "00bab700",
  "target": "00bab71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab708`](#insn-00bab708)

~~~json
{
  "source": "00bab708",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab714`](#insn-00bab714)

~~~json
{
  "source": "00bab714",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab718`](#insn-00bab718)

~~~json
{
  "source": "00bab718",
  "target": "00bab730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab720`](#insn-00bab720)

~~~json
{
  "source": "00bab720",
  "target": "00c9b830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab724`](#insn-00bab724)

~~~json
{
  "source": "00bab724",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab730`](#insn-00bab730)

~~~json
{
  "source": "00bab730",
  "target": "011261e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011261e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab738`](#insn-00bab738)

~~~json
{
  "source": "00bab738",
  "target": "00c5d150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab73c`](#insn-00bab73c)

~~~json
{
  "source": "00bab73c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab748`](#insn-00bab748)

~~~json
{
  "source": "00bab748",
  "target": "00bab760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab750`](#insn-00bab750)

~~~json
{
  "source": "00bab750",
  "target": "00bab760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab764`](#insn-00bab764)

~~~json
{
  "source": "00bab764",
  "target": "00bab76c",
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
- 参照命令 [`00bab778`](#insn-00bab778)

~~~json
{
  "source": "00bab778",
  "target": "00bab3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab78c`](#insn-00bab78c)

~~~json
{
  "source": "00bab78c",
  "target": "00bab794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab794`](#insn-00bab794)

~~~json
{
  "source": "00bab794",
  "target": "00bab79c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7a8`](#insn-00bab7a8)

~~~json
{
  "source": "00bab7a8",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7bc`](#insn-00bab7bc)

~~~json
{
  "source": "00bab7bc",
  "target": "00bab7c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7c4`](#insn-00bab7c4)

~~~json
{
  "source": "00bab7c4",
  "target": "00bab7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7d8`](#insn-00bab7d8)

~~~json
{
  "source": "00bab7d8",
  "target": "00bab3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7f4`](#insn-00bab7f4)

~~~json
{
  "source": "00bab7f4",
  "target": "00bab800",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab7fc`](#insn-00bab7fc)

~~~json
{
  "source": "00bab7fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab814`](#insn-00bab814)

~~~json
{
  "source": "00bab814",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab818`](#insn-00bab818)

~~~json
{
  "source": "00bab818",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab820`](#insn-00bab820)

~~~json
{
  "source": "00bab820",
  "target": "00bab3cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab824`](#insn-00bab824)

~~~json
{
  "source": "00bab824",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
