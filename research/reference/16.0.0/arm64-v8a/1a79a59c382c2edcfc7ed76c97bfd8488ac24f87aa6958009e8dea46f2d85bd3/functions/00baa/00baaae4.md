# 00baaae4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-9bee27ea03d2840368d2463d0392475c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00baaf0c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baaf0c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-366c229a2a6f309d5d96ee7e176458bd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaae4",
  "name": "FUN_00baaae4",
  "size": 2332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "340a88fead96e4fd4bfe3ed704ef28125257f03fc3703b064c8f33ddd0afdf44",
  "source_text_sha256": "340a88fead96e4fd4bfe3ed704ef28125257f03fc3703b064c8f33ddd0afdf44",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaae4",
        "00bab3ff"
      ]
    ],
    "bytes_sha256": "b9702c06a4e5c9ea8830870b8ba20b0b1148af9c8b5d08beb5790426f351b5fc",
    "instruction_count": 583,
    "instruction_bytes": 2332,
    "body_bytes": 2332,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b7fa14](../00b7f/00b7fa14.md)
- [00b7fdf0](../00b7f/00b7fdf0.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c581b0](../00c58/00c581b0.md)
- [00c581c0](../00c58/00c581c0.md)
- [00c5bdb0](../00c5b/00c5bdb0.md)
- [00c5bdc0](../00c5b/00c5bdc0.md)
- [00c5cd50](../00c5c/00c5cd50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 18591 bytes

~~~c

void FUN_00baaae4(byte **param_1,byte **param_2,long param_3)

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
  
                    /* try { // try from 00baaae4 to 00caaaef has its CatchHandler @ 00baba64 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00baab04 to 00caab0f has its CatchHandler @ 00baba24 */
  switch(*(undefined4 *)(param_3 + 0xa0)) {
  case 0:
                    /* try { // try from 00baab30 to 00caab3b has its CatchHandler @ 00baba14 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
                    /* try { // try from 00baab54 to 00caab5f has its CatchHandler @ 00bab9f4 */
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) goto LAB_00baaf14;
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
LAB_00baaf44:
                    /* try { // try from 00baaf48 to 00caaf53 has its CatchHandler @ 00bab900 */
                    /* try { // try from 00baaf54 to 00caaf73 has its CatchHandler @ 00babc60 */
      iVar6 = 10;
      goto LAB_00baaf58;
    }
    goto LAB_00baad94;
  case 1:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00baaed8 to 00caaee3 has its CatchHandler @ 00bab954 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
                    /* try { // try from 00baaefc to 00caaf07 has its CatchHandler @ 00bab950 */
          if (uVar13 - 0x30 < 10) goto LAB_00baaf14;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00baaf44;
    }
    goto LAB_00baad94;
  case 2:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00baad1c to 00caad27 has its CatchHandler @ 00babb50 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
                    /* try { // try from 00baad30 to 00caad33 has its CatchHandler @ 00babb30 */
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
          if (uVar13 - 0x30 < 10) goto LAB_00baaf14;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00baaf44;
    }
    goto LAB_00baad94;
  case 3:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00baae5c to 00caae67 has its CatchHandler @ 00bab9f0 */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab094 to 00cab09f has its CatchHandler @ 00bab8d4 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bab0b8 to 00cab0c3 has its CatchHandler @ 00bab8d0 */
              goto LAB_00bab0d0;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
                    /* try { // try from 00baae88 to 00caae93 has its CatchHandler @ 00bab9a4 */
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
                    /* try { // try from 00bab0cc to 00cab0cf has its CatchHandler @ 00bab8b0 */
      iVar6 = 10;
LAB_00bab0d0:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
      bVar9 = 0;
                    /* try { // try from 00bab0ec to 00cab0f7 has its CatchHandler @ 00bab878 */
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
    bVar10 = bVar9;
    if (param_1 != (byte **)0x0) {
      bVar10 = *(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      bVar9 = *(byte *)param_2;
    }
    bVar3 = (char)bVar10 < (char)bVar9;
                    /* try { // try from 00bab380 to 00cab38f has its CatchHandler @ 00bab764 */
    break;
  case 4:
                    /* try { // try from 00baabf4 to 00caabff has its CatchHandler @ 00bab964 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      bVar9 = *pbVar15;
      if (bVar9 != 0) {
        lVar8 = 1;
        do {
          uVar13 = (uint)bVar9;
                    /* try { // try from 00baac20 to 00caac2b has its CatchHandler @ 00bab918 */
          if (uVar13 - 0x30 < 10) goto LAB_00baaf14;
          bVar9 = pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (bVar9 != 0);
      }
      goto LAB_00baaf44;
    }
LAB_00baad94:
    uVar13 = 0;
                    /* try { // try from 00baad9c to 00caada7 has its CatchHandler @ 00babaa0 */
joined_r0x00baaf8c:
    uVar14 = uVar13;
    if (param_1 != (byte **)0x0) {
      uVar14 = (uint)*(byte *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      uVar13 = (uint)*(byte *)param_2;
    }
    bVar3 = (uVar13 & 0xff) <= (uVar14 & 0xff);
LAB_00baafa4:
    bVar3 = !bVar3;
    break;
  case 5:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
                    /* try { // try from 00baafe8 to 00caaff7 has its CatchHandler @ 00bab76c */
        lVar8 = 1;
        do {
                    /* try { // try from 00baaff8 to 00cab00b has its CatchHandler @ 00bab768 */
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab1d4 to 00cab1df has its CatchHandler @ 00bab804 */
              iVar6 = 0x10;
              goto LAB_00bab1f4;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab1f4:
      local_40 = pbVar15;
                    /* try { // try from 00bab1f8 to 00cab203 has its CatchHandler @ 00bab800 */
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
      uVar11 = 0;
      if ((local_40 != pbVar15) && (*local_40 == 0)) {
        if (lVar5 < 0x8000) {
          uVar11 = (ushort)lVar5;
          if (lVar5 < -0x7fff) {
            uVar11 = 0x8000;
          }
        }
        else {
                    /* try { // try from 00bab224 to 00cab22f has its CatchHandler @ 00bab7d8 */
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
                    /* try { // try from 00baadc0 to 00caadcb has its CatchHandler @ 00baba60 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab248 to 00cab253 has its CatchHandler @ 00bab7d4 */
              iVar6 = 0x10;
              goto LAB_00bab274;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab274:
                    /* try { // try from 00bab274 to 00cab27f has its CatchHandler @ 00bab7c4 */
      local_40 = pbVar15;
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
      uVar13 = 0;
                    /* try { // try from 00bab298 to 00cab2a3 has its CatchHandler @ 00bab79c */
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
    goto LAB_00baafa4;
  case 7:
                    /* try { // try from 00baad70 to 00caad7b has its CatchHandler @ 00babae0 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
                    /* try { // try from 00baaeac to 00caaeb7 has its CatchHandler @ 00bab9a0 */
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab10c to 00cab117 has its CatchHandler @ 00bab874 */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
              iVar6 = 0x10;
                    /* try { // try from 00bab138 to 00cab143 has its CatchHandler @ 00bab850 */
              goto LAB_00bab150;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab150:
      local_40 = pbVar15;
      lVar5 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
                    /* try { // try from 00bab15c to 00cab167 has its CatchHandler @ 00bab84c */
      fVar18 = 0.0;
                    /* try { // try from 00bab188 to 00cab193 has its CatchHandler @ 00bab83c */
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
                    /* try { // try from 00bab1a8 to 00cab1b3 has its CatchHandler @ 00bab814 */
    bVar3 = (int)fVar16 < (int)fVar18;
    break;
  case 8:
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00bab04c to 00cab067 has its CatchHandler @ 00babc4c */
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar13 = (uint)*pbVar15;
      if (*pbVar15 != 0) {
        lVar8 = 1;
        do {
          if (uVar13 - 0x30 < 10) {
                    /* try { // try from 00bab2c4 to 00cab2cf has its CatchHandler @ 00bab78c */
            if ((uVar13 == 0x30) && ((pbVar15[lVar8] & 0xdf) == 0x58)) {
                    /* try { // try from 00bab2e0 to 00cab2eb has its CatchHandler @ 00bab788 */
              iVar6 = 0x10;
                    /* try { // try from 00bab2ec to 00cab30b has its CatchHandler @ 00babbe0 */
              goto LAB_00bab308;
            }
            break;
          }
          uVar13 = (uint)pbVar15[lVar8];
          lVar8 = lVar8 + 1;
        } while (uVar13 != 0);
      }
      iVar6 = 10;
LAB_00bab308:
      local_40 = pbVar15;
                    /* try { // try from 00bab30c to 00cab37b has its CatchHandler @ 00babe30 */
      uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                        *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
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
    goto LAB_00baafa4;
  case 9:
    local_40 = (byte *)0x0;
                    /* try { // try from 00baac3c to 00caac47 has its CatchHandler @ 00bab914 */
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
                    /* try { // try from 00baac48 to 00caac67 has its CatchHandler @ 00babc64 */
      lVar8 = param_3 + 0xc1;
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        lVar8 = *(long *)(param_3 + 0xd0);
      }
      _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib(&local_40,lVar8,0,1);
    }
                    /* try { // try from 00baac68 to 00caacd7 has its CatchHandler @ 00babe38 */
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
    bVar3 = (long)*param_1 < (long)*param_2;
    break;
  case 10:
                    /* try { // try from 00baadec to 00caadf7 has its CatchHandler @ 00baba50 */
    local_40 = (byte *)0x0;
    if ((param_1 == (byte **)0x0) || (param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
                    /* try { // try from 00baae0c to 00caae17 has its CatchHandler @ 00baba10 */
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      uVar4 = _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib(&local_40,pbVar15,0,1);
      if ((local_40 != (byte *)0x0) && ((uVar4 & 1) != 0)) {
        uVar13 = (uint)*pbVar15;
        pbVar7 = pbVar15;
        if (*pbVar15 != 0) {
          do {
                    /* try { // try from 00baae38 to 00caae43 has its CatchHandler @ 00baba00 */
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
    if (param_1 == (byte **)0x0) {
      param_1 = &local_40;
    }
                    /* try { // try from 00bab3e4 to 00cab3ff has its CatchHandler @ 00babc48 */
    if (param_2 == (byte **)0x0) {
      param_2 = &local_40;
    }
    bVar3 = *param_2 <= *param_1;
    goto LAB_00baafa4;
  case 0xb:
                    /* try { // try from 00baab80 to 00caab8b has its CatchHandler @ 00bab9b8 */
    if ((param_1 == (byte **)0x0) || (fVar18 = 0.0, param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
                    /* try { // try from 00baaba4 to 00caabaf has its CatchHandler @ 00bab9b4 */
      fVar16 = strtof((char *)pbVar15,(char **)&local_40);
      fVar18 = 0.0;
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (fVar18 = fVar16, NAN(fVar16))) {
                    /* try { // try from 00baabd0 to 00caabdb has its CatchHandler @ 00bab968 */
        fVar18 = NAN;
      }
    }
    fVar16 = fVar18;
    if (param_1 != (byte **)0x0) {
      fVar16 = *(float *)param_1;
    }
    if (param_2 != (byte **)0x0) {
      fVar18 = *(float *)param_2;
    }
    bVar3 = fVar16 < fVar18;
    break;
  case 0xc:
    if ((param_1 == (byte **)0x0) || (dVar19 = 0.0, param_2 == (byte **)0x0)) {
      pbVar15 = (byte *)(param_3 + 0xc1);
      if ((*(byte *)(param_3 + 0xc0) & 1) != 0) {
        pbVar15 = *(byte **)(param_3 + 0xd0);
      }
      local_40 = pbVar15;
      dVar17 = strtod((char *)pbVar15,(char **)&local_40);
      dVar19 = 0.0;
      if (((local_40 != pbVar15) && (*local_40 == 0)) && (dVar19 = dVar17, NAN(dVar17))) {
        dVar19 = NAN;
      }
    }
    dVar17 = dVar19;
    if (param_1 != (byte **)0x0) {
      dVar17 = (double)*param_1;
    }
                    /* try { // try from 00baacf8 to 00caad03 has its CatchHandler @ 00babbc0 */
    if (param_2 != (byte **)0x0) {
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
LAB_00baaf14:
                    /* try { // try from 00baaf28 to 00caaf33 has its CatchHandler @ 00bab904 */
  if ((uVar13 != 0x30) || ((pbVar15[lVar8] & 0xdf) != 0x58)) goto LAB_00baaf44;
  iVar6 = 0x10;
LAB_00baaf58:
  local_40 = pbVar15;
  uVar4 = strtoll_l((char *)pbVar15,(char **)&local_40,iVar6,
                    *(__locale_t *)PTR__ZN11flatbuffers13ClassicLocale9instance_E_00c9b430);
  uVar13 = 0;
                    /* try { // try from 00baaf74 to 00caafe3 has its CatchHandler @ 00babe34 */
  if (((local_40 != pbVar15) && (*local_40 == 0)) && (uVar13 = (uint)uVar4, 0xfe < uVar4)) {
    uVar13 = 0xff;
  }
  goto joined_r0x00baaf8c;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaae4"></a> `00baaae4` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baaae8"></a> `00baaae8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaaec"></a> `00baaaec` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaaf0"></a> `00baaaf0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaaf4"></a> `00baaaf4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baaaf8"></a> `00baaaf8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00baaafc"></a> `00baaafc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00baab00"></a> `00baab00` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baab04"></a> `00baab04` | `48 a0 40 b9` | ldr w8,[x2, #0xa0] | `FALL_THROUGH`
<a id="insn-00baab08"></a> `00baab08` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00baab0c"></a> `00baab0c` | `c8 13 00 54` | b.hi 0x00baad84 | `CONDITIONAL_JUMP`
<a id="insn-00baab10"></a> `00baab10` | `29 bb ff 90` | adrp x9,0x30e000 | `FALL_THROUGH`
<a id="insn-00baab14"></a> `00baab14` | `29 cd 06 91` | add x9,x9,#0x1b3 | `FALL_THROUGH`
<a id="insn-00baab18"></a> `00baab18` | `ca 00 00 10` | adr x10,0xbaab30 | `FALL_THROUGH`
<a id="insn-00baab1c"></a> `00baab1c` | `2b 69 68 38` | ldrb w11,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baab20"></a> `00baab20` | `4a 09 0b 8b` | add x10,x10,x11, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00baab24"></a> `00baab24` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baab28"></a> `00baab28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baab2c"></a> `00baab2c` | `40 01 1f d6` | br x10 | `COMPUTED_JUMP`
<a id="insn-00baab30"></a> `00baab30` | `54 00 00 b4` | cbz x20,0x00baab38 | `CONDITIONAL_JUMP`
<a id="insn-00baab34"></a> `00baab34` | `13 13 00 b5` | cbnz x19,0x00baad94 | `CONDITIONAL_JUMP`
<a id="insn-00baab38"></a> `00baab38` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baab3c"></a> `00baab3c` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baab40"></a> `00baab40` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baab44"></a> `00baab44` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baab48"></a> `00baab48` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baab4c"></a> `00baab4c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baab50"></a> `00baab50` | `a9 1f 00 34` | cbz w9,0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baab54"></a> `00baab54` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baab58"></a> `00baab58` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baab5c"></a> `00baab5c` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baab60"></a> `00baab60` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baab64"></a> `00baab64` | `83 1d 00 54` | b.cc 0x00baaf14 | `CONDITIONAL_JUMP`
<a id="insn-00baab68"></a> `00baab68` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baab6c"></a> `00baab6c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baab70"></a> `00baab70` | `49 ff ff 35` | cbnz w9,0x00baab58 | `CONDITIONAL_JUMP`
<a id="insn-00baab74"></a> `00baab74` | `f4 00 00 14` | b 0x00baaf44 | `UNCONDITIONAL_JUMP`
<a id="insn-00baab78"></a> `00baab78` | `74 00 00 b4` | cbz x20,0x00baab84 | `CONDITIONAL_JUMP`
<a id="insn-00baab7c"></a> `00baab7c` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00baab80"></a> `00baab80` | `b3 02 00 b5` | cbnz x19,0x00baabd4 | `CONDITIONAL_JUMP`
<a id="insn-00baab84"></a> `00baab84` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baab88"></a> `00baab88` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baab8c"></a> `00baab8c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baab90"></a> `00baab90` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baab94"></a> `00baab94` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baab98"></a> `00baab98` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baab9c"></a> `00baab9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baaba0"></a> `00baaba0` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00baaba4"></a> `00baaba4` | `83 b5 02 94` | bl 0x00c581b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baaba8"></a> `00baaba8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00baabac"></a> `00baabac` | `e1 03 27 1e` | fmov s1,wzr | `FALL_THROUGH`
<a id="insn-00baabb0"></a> `00baabb0` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baabb4"></a> `00baabb4` | `00 01 00 54` | b.eq 0x00baabd4 | `CONDITIONAL_JUMP`
<a id="insn-00baabb8"></a> `00baabb8` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00baabbc"></a> `00baabbc` | `c8 00 00 35` | cbnz w8,0x00baabd4 | `CONDITIONAL_JUMP`
<a id="insn-00baabc0"></a> `00baabc0` | `00 20 20 1e` | fcmp s0,s0 | `FALL_THROUGH`
<a id="insn-00baabc4"></a> `00baabc4` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00baabc8"></a> `00baabc8` | `67 00 00 54` | b.vc 0x00baabd4 | `CONDITIONAL_JUMP`
<a id="insn-00baabcc"></a> `00baabcc` | `08 f8 af 52` | mov w8,#0x7fc00000 | `FALL_THROUGH`
<a id="insn-00baabd0"></a> `00baabd0` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00baabd4"></a> `00baabd4` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00baabd8"></a> `00baabd8` | `54 00 00 b4` | cbz x20,0x00baabe0 | `CONDITIONAL_JUMP`
<a id="insn-00baabdc"></a> `00baabdc` | `80 02 40 bd` | ldr s0,[x20] | `FALL_THROUGH`
<a id="insn-00baabe0"></a> `00baabe0` | `53 00 00 b4` | cbz x19,0x00baabe8 | `CONDITIONAL_JUMP`
<a id="insn-00baabe4"></a> `00baabe4` | `61 02 40 bd` | ldr s1,[x19] | `FALL_THROUGH`
<a id="insn-00baabe8"></a> `00baabe8` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00baabec"></a> `00baabec` | `46 00 00 14` | b 0x00baad04 | `UNCONDITIONAL_JUMP`
<a id="insn-00baabf0"></a> `00baabf0` | `54 00 00 b4` | cbz x20,0x00baabf8 | `CONDITIONAL_JUMP`
<a id="insn-00baabf4"></a> `00baabf4` | `13 0d 00 b5` | cbnz x19,0x00baad94 | `CONDITIONAL_JUMP`
<a id="insn-00baabf8"></a> `00baabf8` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baabfc"></a> `00baabfc` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baac00"></a> `00baac00` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baac04"></a> `00baac04` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baac08"></a> `00baac08` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baac0c"></a> `00baac0c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baac10"></a> `00baac10` | `a9 19 00 34` | cbz w9,0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baac14"></a> `00baac14` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baac18"></a> `00baac18` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baac1c"></a> `00baac1c` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baac20"></a> `00baac20` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baac24"></a> `00baac24` | `83 17 00 54` | b.cc 0x00baaf14 | `CONDITIONAL_JUMP`
<a id="insn-00baac28"></a> `00baac28` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baac2c"></a> `00baac2c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baac30"></a> `00baac30` | `49 ff ff 35` | cbnz w9,0x00baac18 | `CONDITIONAL_JUMP`
<a id="insn-00baac34"></a> `00baac34` | `c4 00 00 14` | b 0x00baaf44 | `UNCONDITIONAL_JUMP`
<a id="insn-00baac38"></a> `00baac38` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00baac3c"></a> `00baac3c` | `54 00 00 b4` | cbz x20,0x00baac44 | `CONDITIONAL_JUMP`
<a id="insn-00baac40"></a> `00baac40` | `53 01 00 b5` | cbnz x19,0x00baac68 | `CONDITIONAL_JUMP`
<a id="insn-00baac44"></a> `00baac44` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baac48"></a> `00baac48` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baac4c"></a> `00baac4c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baac50"></a> `00baac50` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00baac54"></a> `00baac54` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baac58"></a> `00baac58` | `41 01 89 9a` | csel x1,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baac5c"></a> `00baac5c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00baac60"></a> `00baac60` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00baac64"></a> `00baac64` | `53 c4 02 94` | bl 0x00c5bdb0 | `UNCONDITIONAL_CALL`
<a id="insn-00baac68"></a> `00baac68` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00baac6c"></a> `00baac6c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00baac70"></a> `00baac70` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00baac74"></a> `00baac74` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00baac78"></a> `00baac78` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00baac7c"></a> `00baac7c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00baac80"></a> `00baac80` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00baac84"></a> `00baac84` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00baac88"></a> `00baac88` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00baac8c"></a> `00baac8c` | `c7 00 00 14` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baac90"></a> `00baac90` | `74 00 00 b4` | cbz x20,0x00baac9c | `CONDITIONAL_JUMP`
<a id="insn-00baac94"></a> `00baac94` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00baac98"></a> `00baac98` | `b3 02 00 b5` | cbnz x19,0x00baacec | `CONDITIONAL_JUMP`
<a id="insn-00baac9c"></a> `00baac9c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baaca0"></a> `00baaca0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baaca4"></a> `00baaca4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baaca8"></a> `00baaca8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baacac"></a> `00baacac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baacb0"></a> `00baacb0` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baacb4"></a> `00baacb4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baacb8"></a> `00baacb8` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00baacbc"></a> `00baacbc` | `41 b5 02 94` | bl 0x00c581c0 | `UNCONDITIONAL_CALL`
<a id="insn-00baacc0"></a> `00baacc0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00baacc4"></a> `00baacc4` | `e1 03 67 9e` | fmov d1,xzr | `FALL_THROUGH`
<a id="insn-00baacc8"></a> `00baacc8` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baaccc"></a> `00baaccc` | `00 01 00 54` | b.eq 0x00baacec | `CONDITIONAL_JUMP`
<a id="insn-00baacd0"></a> `00baacd0` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00baacd4"></a> `00baacd4` | `c8 00 00 35` | cbnz w8,0x00baacec | `CONDITIONAL_JUMP`
<a id="insn-00baacd8"></a> `00baacd8` | `00 20 60 1e` | fcmp d0,d0 | `FALL_THROUGH`
<a id="insn-00baacdc"></a> `00baacdc` | `01 1c a0 4e` | mov v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00baace0"></a> `00baace0` | `67 00 00 54` | b.vc 0x00baacec | `CONDITIONAL_JUMP`
<a id="insn-00baace4"></a> `00baace4` | `08 ff ef d2` | mov x8,#0x7ff8000000000000 | `FALL_THROUGH`
<a id="insn-00baace8"></a> `00baace8` | `01 01 67 9e` | fmov d1,x8 | `FALL_THROUGH`
<a id="insn-00baacec"></a> `00baacec` | `20 1c a1 4e` | mov v0.16B,v1.16B | `FALL_THROUGH`
<a id="insn-00baacf0"></a> `00baacf0` | `54 00 00 b4` | cbz x20,0x00baacf8 | `CONDITIONAL_JUMP`
<a id="insn-00baacf4"></a> `00baacf4` | `80 02 40 fd` | ldr d0,[x20] | `FALL_THROUGH`
<a id="insn-00baacf8"></a> `00baacf8` | `53 00 00 b4` | cbz x19,0x00baad00 | `CONDITIONAL_JUMP`
<a id="insn-00baacfc"></a> `00baacfc` | `61 02 40 fd` | ldr d1,[x19] | `FALL_THROUGH`
<a id="insn-00baad00"></a> `00baad00` | `00 20 61 1e` | fcmp d0,d1 | `FALL_THROUGH`
<a id="insn-00baad04"></a> `00baad04` | `e0 57 9f 1a` | cset w0,mi | `FALL_THROUGH`
<a id="insn-00baad08"></a> `00baad08` | `a8 00 00 14` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baad0c"></a> `00baad0c` | `54 00 00 b4` | cbz x20,0x00baad14 | `CONDITIONAL_JUMP`
<a id="insn-00baad10"></a> `00baad10` | `33 04 00 b5` | cbnz x19,0x00baad94 | `CONDITIONAL_JUMP`
<a id="insn-00baad14"></a> `00baad14` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baad18"></a> `00baad18` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baad1c"></a> `00baad1c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baad20"></a> `00baad20` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baad24"></a> `00baad24` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baad28"></a> `00baad28` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baad2c"></a> `00baad2c` | `c9 10 00 34` | cbz w9,0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baad30"></a> `00baad30` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baad34"></a> `00baad34` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baad38"></a> `00baad38` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baad3c"></a> `00baad3c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baad40"></a> `00baad40` | `a3 0e 00 54` | b.cc 0x00baaf14 | `CONDITIONAL_JUMP`
<a id="insn-00baad44"></a> `00baad44` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baad48"></a> `00baad48` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baad4c"></a> `00baad4c` | `49 ff ff 35` | cbnz w9,0x00baad34 | `CONDITIONAL_JUMP`
<a id="insn-00baad50"></a> `00baad50` | `7d 00 00 14` | b 0x00baaf44 | `UNCONDITIONAL_JUMP`
<a id="insn-00baad54"></a> `00baad54` | `14 08 00 b4` | cbz x20,0x00baae54 | `CONDITIONAL_JUMP`
<a id="insn-00baad58"></a> `00baad58` | `f3 07 00 b4` | cbz x19,0x00baae54 | `CONDITIONAL_JUMP`
<a id="insn-00baad5c"></a> `00baad5c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baad60"></a> `00baad60` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baad64"></a> `00baad64` | `34 30 00 b5` | cbnz x20,0x00bab368 | `CONDITIONAL_JUMP`
<a id="insn-00baad68"></a> `00baad68` | `81 01 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00baad6c"></a> `00baad6c` | `54 09 00 b4` | cbz x20,0x00baae94 | `CONDITIONAL_JUMP`
<a id="insn-00baad70"></a> `00baad70` | `33 09 00 b4` | cbz x19,0x00baae94 | `CONDITIONAL_JUMP`
<a id="insn-00baad74"></a> `00baad74` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baad78"></a> `00baad78` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baad7c"></a> `00baad7c` | `f4 20 00 b5` | cbnz x20,0x00bab198 | `CONDITIONAL_JUMP`
<a id="insn-00baad80"></a> `00baad80` | `07 01 00 14` | b 0x00bab19c | `UNCONDITIONAL_JUMP`
<a id="insn-00baad84"></a> `00baad84` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00baad88"></a> `00baad88` | `88 00 00 14` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baad8c"></a> `00baad8c` | `54 0a 00 b4` | cbz x20,0x00baaed4 | `CONDITIONAL_JUMP`
<a id="insn-00baad90"></a> `00baad90` | `33 0a 00 b4` | cbz x19,0x00baaed4 | `CONDITIONAL_JUMP`
<a id="insn-00baad94"></a> `00baad94` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baad98"></a> `00baad98` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baad9c"></a> `00baad9c` | `b4 0f 00 b5` | cbnz x20,0x00baaf90 | `CONDITIONAL_JUMP`
<a id="insn-00baada0"></a> `00baada0` | `7d 00 00 14` | b 0x00baaf94 | `UNCONDITIONAL_JUMP`
<a id="insn-00baada4"></a> `00baada4` | `54 11 00 b4` | cbz x20,0x00baafcc | `CONDITIONAL_JUMP`
<a id="insn-00baada8"></a> `00baada8` | `33 11 00 b4` | cbz x19,0x00baafcc | `CONDITIONAL_JUMP`
<a id="insn-00baadac"></a> `00baadac` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baadb0"></a> `00baadb0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baadb4"></a> `00baadb4` | `34 2f 00 b5` | cbnz x20,0x00bab398 | `CONDITIONAL_JUMP`
<a id="insn-00baadb8"></a> `00baadb8` | `79 01 00 14` | b 0x00bab39c | `UNCONDITIONAL_JUMP`
<a id="insn-00baadbc"></a> `00baadbc` | `94 12 00 b4` | cbz x20,0x00bab00c | `CONDITIONAL_JUMP`
<a id="insn-00baadc0"></a> `00baadc0` | `73 12 00 b4` | cbz x19,0x00bab00c | `CONDITIONAL_JUMP`
<a id="insn-00baadc4"></a> `00baadc4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baadc8"></a> `00baadc8` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baadcc"></a> `00baadcc` | `14 27 00 b5` | cbnz x20,0x00bab2ac | `CONDITIONAL_JUMP`
<a id="insn-00baadd0"></a> `00baadd0` | `38 01 00 14` | b 0x00bab2b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baadd4"></a> `00baadd4` | `d4 13 00 b4` | cbz x20,0x00bab04c | `CONDITIONAL_JUMP`
<a id="insn-00baadd8"></a> `00baadd8` | `b3 13 00 b4` | cbz x19,0x00bab04c | `CONDITIONAL_JUMP`
<a id="insn-00baaddc"></a> `00baaddc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baade0"></a> `00baade0` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baade4"></a> `00baade4` | `f4 2a 00 b5` | cbnz x20,0x00bab340 | `CONDITIONAL_JUMP`
<a id="insn-00baade8"></a> `00baade8` | `57 01 00 14` | b 0x00bab344 | `UNCONDITIONAL_JUMP`
<a id="insn-00baadec"></a> `00baadec` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00baadf0"></a> `00baadf0` | `54 00 00 b4` | cbz x20,0x00baadf8 | `CONDITIONAL_JUMP`
<a id="insn-00baadf4"></a> `00baadf4` | `33 2f 00 b5` | cbnz x19,0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00baadf8"></a> `00baadf8` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baadfc"></a> `00baadfc` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baae00"></a> `00baae00` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baae04"></a> `00baae04` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00baae08"></a> `00baae08` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baae0c"></a> `00baae0c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baae10"></a> `00baae10` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00baae14"></a> `00baae14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00baae18"></a> `00baae18` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00baae1c"></a> `00baae1c` | `e9 c3 02 94` | bl 0x00c5bdc0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae20"></a> `00baae20` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00baae24"></a> `00baae24` | `a8 2d 00 b4` | cbz x8,0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00baae28"></a> `00baae28` | `80 2d 00 36` | tbz w0,#0x0,0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00baae2c"></a> `00baae2c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baae30"></a> `00baae30` | `29 2c 00 34` | cbz w9,0x00bab3b4 | `CONDITIONAL_JUMP`
<a id="insn-00baae34"></a> `00baae34` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00baae38"></a> `00baae38` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baae3c"></a> `00baae3c` | `29 c1 00 51` | sub w9,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baae40"></a> `00baae40` | `3f 29 00 71` | cmp w9,#0xa | `FALL_THROUGH`
<a id="insn-00baae44"></a> `00baae44` | `a3 2b 00 54` | b.cc 0x00bab3b8 | `CONDITIONAL_JUMP`
<a id="insn-00baae48"></a> `00baae48` | `09 1d 40 38` | ldrb w9,[x8, #0x1]! | `FALL_THROUGH`
<a id="insn-00baae4c"></a> `00baae4c` | `69 ff ff 35` | cbnz w9,0x00baae38 | `CONDITIONAL_JUMP`
<a id="insn-00baae50"></a> `00baae50` | `5a 01 00 14` | b 0x00bab3b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baae54"></a> `00baae54` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baae58"></a> `00baae58` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baae5c"></a> `00baae5c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baae60"></a> `00baae60` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baae64"></a> `00baae64` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baae68"></a> `00baae68` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baae6c"></a> `00baae6c` | `89 12 00 34` | cbz w9,0x00bab0bc | `CONDITIONAL_JUMP`
<a id="insn-00baae70"></a> `00baae70` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baae74"></a> `00baae74` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baae78"></a> `00baae78` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baae7c"></a> `00baae7c` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baae80"></a> `00baae80` | `63 10 00 54` | b.cc 0x00bab08c | `CONDITIONAL_JUMP`
<a id="insn-00baae84"></a> `00baae84` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baae88"></a> `00baae88` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baae8c"></a> `00baae8c` | `49 ff ff 35` | cbnz w9,0x00baae74 | `CONDITIONAL_JUMP`
<a id="insn-00baae90"></a> `00baae90` | `8b 00 00 14` | b 0x00bab0bc | `UNCONDITIONAL_JUMP`
<a id="insn-00baae94"></a> `00baae94` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baae98"></a> `00baae98` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baae9c"></a> `00baae9c` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baaea0"></a> `00baaea0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaea4"></a> `00baaea4` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baaea8"></a> `00baaea8` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baaeac"></a> `00baaeac` | `89 14 00 34` | cbz w9,0x00bab13c | `CONDITIONAL_JUMP`
<a id="insn-00baaeb0"></a> `00baaeb0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaeb4"></a> `00baaeb4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baaeb8"></a> `00baaeb8` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baaebc"></a> `00baaebc` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baaec0"></a> `00baaec0` | `63 12 00 54` | b.cc 0x00bab10c | `CONDITIONAL_JUMP`
<a id="insn-00baaec4"></a> `00baaec4` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baaec8"></a> `00baaec8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaecc"></a> `00baaecc` | `49 ff ff 35` | cbnz w9,0x00baaeb4 | `CONDITIONAL_JUMP`
<a id="insn-00baaed0"></a> `00baaed0` | `9b 00 00 14` | b 0x00bab13c | `UNCONDITIONAL_JUMP`
<a id="insn-00baaed4"></a> `00baaed4` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baaed8"></a> `00baaed8` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baaedc"></a> `00baaedc` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baaee0"></a> `00baaee0` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaee4"></a> `00baaee4` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baaee8"></a> `00baaee8` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baaeec"></a> `00baaeec` | `c9 02 00 34` | cbz w9,0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baaef0"></a> `00baaef0` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaef4"></a> `00baaef4` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baaef8"></a> `00baaef8` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baaefc"></a> `00baaefc` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baaf00"></a> `00baaf00` | `a3 00 00 54` | b.cc 0x00baaf14 | `CONDITIONAL_JUMP`
<a id="insn-00baaf04"></a> `00baaf04` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baaf08"></a> `00baaf08` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baaf0c"></a> `00baaf0c` | `49 ff ff 35` | cbnz w9,0x00baaef4 | `CONDITIONAL_JUMP`
<a id="insn-00baaf10"></a> `00baaf10` | `0d 00 00 14` | b 0x00baaf44 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf14"></a> `00baaf14` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baaf18"></a> `00baaf18` | `61 01 00 54` | b.ne 0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baaf1c"></a> `00baaf1c` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00baaf20"></a> `00baaf20` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00baaf24"></a> `00baaf24` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00baaf28"></a> `00baaf28` | `e1 00 00 54` | b.ne 0x00baaf44 | `CONDITIONAL_JUMP`
<a id="insn-00baaf2c"></a> `00baaf2c` | `88 07 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00baaf30"></a> `00baaf30` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00baaf34"></a> `00baaf34` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baaf38"></a> `00baaf38` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00baaf3c"></a> `00baaf3c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00baaf40"></a> `00baaf40` | `06 00 00 14` | b 0x00baaf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaf44"></a> `00baaf44` | `88 07 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00baaf48"></a> `00baaf48` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00baaf4c"></a> `00baaf4c` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00baaf50"></a> `00baaf50` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00baaf54"></a> `00baaf54` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00baaf58"></a> `00baaf58` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00baaf5c"></a> `00baaf5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00baaf60"></a> `00baaf60` | `7c c7 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00baaf64"></a> `00baaf64` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00baaf68"></a> `00baaf68` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00baaf6c"></a> `00baaf6c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00baaf70"></a> `00baaf70` | `c0 00 00 54` | b.eq 0x00baaf88 | `CONDITIONAL_JUMP`
<a id="insn-00baaf74"></a> `00baaf74` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00baaf78"></a> `00baaf78` | `89 00 00 35` | cbnz w9,0x00baaf88 | `CONDITIONAL_JUMP`
<a id="insn-00baaf7c"></a> `00baaf7c` | `1f fc 03 f1` | cmp x0,#0xff | `FALL_THROUGH`
<a id="insn-00baaf80"></a> `00baaf80` | `e8 1f 80 52` | mov w8,#0xff | `FALL_THROUGH`
<a id="insn-00baaf84"></a> `00baaf84` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00baaf88"></a> `00baaf88` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00baaf8c"></a> `00baaf8c` | `54 00 00 b4` | cbz x20,0x00baaf94 | `CONDITIONAL_JUMP`
<a id="insn-00baaf90"></a> `00baaf90` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00baaf94"></a> `00baaf94` | `53 00 00 b4` | cbz x19,0x00baaf9c | `CONDITIONAL_JUMP`
<a id="insn-00baaf98"></a> `00baaf98` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00baaf9c"></a> `00baaf9c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baafa0"></a> `00baafa0` | `3f 01 28 6b` | cmp w9,w8, UXTB  | `FALL_THROUGH`
<a id="insn-00baafa4"></a> `00baafa4` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00baafa8"></a> `00baafa8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00baafac"></a> `00baafac` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00baafb0"></a> `00baafb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baafb4"></a> `00baafb4` | `41 22 00 54` | b.ne 0x00bab3fc | `CONDITIONAL_JUMP`
<a id="insn-00baafb8"></a> `00baafb8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baafbc"></a> `00baafbc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baafc0"></a> `00baafc0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baafc4"></a> `00baafc4` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baafc8"></a> `00baafc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baafcc"></a> `00baafcc` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00baafd0"></a> `00baafd0` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00baafd4"></a> `00baafd4` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00baafd8"></a> `00baafd8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baafdc"></a> `00baafdc` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00baafe0"></a> `00baafe0` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00baafe4"></a> `00baafe4` | `e9 0f 00 34` | cbz w9,0x00bab1e0 | `CONDITIONAL_JUMP`
<a id="insn-00baafe8"></a> `00baafe8` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00baafec"></a> `00baafec` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00baaff4"></a> `00baaff4` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00baaff8"></a> `00baaff8` | `c3 0d 00 54` | b.cc 0x00bab1b0 | `CONDITIONAL_JUMP`
<a id="insn-00baaffc"></a> `00baaffc` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab000"></a> `00bab000` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab004"></a> `00bab004` | `49 ff ff 35` | cbnz w9,0x00baafec | `CONDITIONAL_JUMP`
<a id="insn-00bab008"></a> `00bab008` | `76 00 00 14` | b 0x00bab1e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab00c"></a> `00bab00c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab010"></a> `00bab010` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab014"></a> `00bab014` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab018"></a> `00bab018` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab01c"></a> `00bab01c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab020"></a> `00bab020` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab024"></a> `00bab024` | `e9 11 00 34` | cbz w9,0x00bab260 | `CONDITIONAL_JUMP`
<a id="insn-00bab028"></a> `00bab028` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab02c"></a> `00bab02c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab030"></a> `00bab030` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab034"></a> `00bab034` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab038"></a> `00bab038` | `c3 0f 00 54` | b.cc 0x00bab230 | `CONDITIONAL_JUMP`
<a id="insn-00bab03c"></a> `00bab03c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab040"></a> `00bab040` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab044"></a> `00bab044` | `49 ff ff 35` | cbnz w9,0x00bab02c | `CONDITIONAL_JUMP`
<a id="insn-00bab048"></a> `00bab048` | `86 00 00 14` | b 0x00bab260 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab04c"></a> `00bab04c` | `48 00 43 39` | ldrb w8,[x2, #0xc0] | `FALL_THROUGH`
<a id="insn-00bab050"></a> `00bab050` | `49 68 40 f9` | ldr x9,[x2, #0xd0] | `FALL_THROUGH`
<a id="insn-00bab054"></a> `00bab054` | `4a 04 03 91` | add x10,x2,#0xc1 | `FALL_THROUGH`
<a id="insn-00bab058"></a> `00bab058` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab05c"></a> `00bab05c` | `55 01 89 9a` | csel x21,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bab060"></a> `00bab060` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bab064"></a> `00bab064` | `89 14 00 34` | cbz w9,0x00bab2f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab068"></a> `00bab068` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab06c"></a> `00bab06c` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-00bab070"></a> `00bab070` | `2a c1 00 51` | sub w10,w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab074"></a> `00bab074` | `5f 29 00 71` | cmp w10,#0xa | `FALL_THROUGH`
<a id="insn-00bab078"></a> `00bab078` | `63 12 00 54` | b.cc 0x00bab2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bab07c"></a> `00bab07c` | `a9 6a 68 38` | ldrb w9,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab080"></a> `00bab080` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab084"></a> `00bab084` | `49 ff ff 35` | cbnz w9,0x00bab06c | `CONDITIONAL_JUMP`
<a id="insn-00bab088"></a> `00bab088` | `9b 00 00 14` | b 0x00bab2f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab08c"></a> `00bab08c` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab090"></a> `00bab090` | `61 01 00 54` | b.ne 0x00bab0bc | `CONDITIONAL_JUMP`
<a id="insn-00bab094"></a> `00bab094` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab098"></a> `00bab098` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab09c"></a> `00bab09c` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab0a0"></a> `00bab0a0` | `e1 00 00 54` | b.ne 0x00bab0bc | `CONDITIONAL_JUMP`
<a id="insn-00bab0a4"></a> `00bab0a4` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab0a8"></a> `00bab0a8` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab0ac"></a> `00bab0ac` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab0b0"></a> `00bab0b0` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab0b4"></a> `00bab0b4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab0b8"></a> `00bab0b8` | `06 00 00 14` | b 0x00bab0d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab0bc"></a> `00bab0bc` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab0c0"></a> `00bab0c0` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab0c4"></a> `00bab0c4` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab0c8"></a> `00bab0c8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab0cc"></a> `00bab0cc` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab0d0"></a> `00bab0d0` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab0d4"></a> `00bab0d4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab0d8"></a> `00bab0d8` | `1e c7 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab0dc"></a> `00bab0dc` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab0e0"></a> `00bab0e0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab0e4"></a> `00bab0e4` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab0e8"></a> `00bab0e8` | `c0 13 00 54` | b.eq 0x00bab360 | `CONDITIONAL_JUMP`
<a id="insn-00bab0ec"></a> `00bab0ec` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab0f0"></a> `00bab0f0` | `89 13 00 35` | cbnz w9,0x00bab360 | `CONDITIONAL_JUMP`
<a id="insn-00bab0f4"></a> `00bab0f4` | `1f fc 01 f1` | cmp x0,#0x7f | `FALL_THROUGH`
<a id="insn-00bab0f8"></a> `00bab0f8` | `ed 12 00 54` | b.le 0x00bab354 | `CONDITIONAL_JUMP`
<a id="insn-00bab0fc"></a> `00bab0fc` | `e8 0f 80 52` | mov w8,#0x7f | `FALL_THROUGH`
<a id="insn-00bab100"></a> `00bab100` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab104"></a> `00bab104` | `34 13 00 b5` | cbnz x20,0x00bab368 | `CONDITIONAL_JUMP`
<a id="insn-00bab108"></a> `00bab108` | `99 00 00 14` | b 0x00bab36c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab10c"></a> `00bab10c` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab110"></a> `00bab110` | `61 01 00 54` | b.ne 0x00bab13c | `CONDITIONAL_JUMP`
<a id="insn-00bab114"></a> `00bab114` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab118"></a> `00bab118` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab11c"></a> `00bab11c` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab120"></a> `00bab120` | `e1 00 00 54` | b.ne 0x00bab13c | `CONDITIONAL_JUMP`
<a id="insn-00bab124"></a> `00bab124` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab128"></a> `00bab128` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab12c"></a> `00bab12c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab130"></a> `00bab130` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab134"></a> `00bab134` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab138"></a> `00bab138` | `06 00 00 14` | b 0x00bab150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab13c"></a> `00bab13c` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab140"></a> `00bab140` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab144"></a> `00bab144` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab148"></a> `00bab148` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab14c"></a> `00bab14c` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab150"></a> `00bab150` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab154"></a> `00bab154` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab158"></a> `00bab158` | `fe c6 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab15c"></a> `00bab15c` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab160"></a> `00bab160` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab164"></a> `00bab164` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab168"></a> `00bab168` | `40 01 00 54` | b.eq 0x00bab190 | `CONDITIONAL_JUMP`
<a id="insn-00bab16c"></a> `00bab16c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab170"></a> `00bab170` | `09 01 00 35` | cbnz w9,0x00bab190 | `CONDITIONAL_JUMP`
<a id="insn-00bab174"></a> `00bab174` | `08 00 b0 12` | mov w8,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00bab178"></a> `00bab178` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab17c"></a> `00bab17c` | `ac 00 00 54` | b.gt 0x00bab190 | `CONDITIONAL_JUMP`
<a id="insn-00bab180"></a> `00bab180` | `e8 83 61 b2` | orr x8,xzr,#-0x80000000 | `FALL_THROUGH`
<a id="insn-00bab184"></a> `00bab184` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab188"></a> `00bab188` | `08 00 b0 52` | mov w8,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bab18c"></a> `00bab18c` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab190"></a> `00bab190` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab194"></a> `00bab194` | `54 00 00 b4` | cbz x20,0x00bab19c | `CONDITIONAL_JUMP`
<a id="insn-00bab198"></a> `00bab198` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab19c"></a> `00bab19c` | `53 00 00 b4` | cbz x19,0x00bab1a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab1a0"></a> `00bab1a0` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab1a4"></a> `00bab1a4` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab1a8"></a> `00bab1a8` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab1ac"></a> `00bab1ac` | `7f ff ff 17` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1b0"></a> `00bab1b0` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab1b4"></a> `00bab1b4` | `61 01 00 54` | b.ne 0x00bab1e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1b8"></a> `00bab1b8` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab1bc"></a> `00bab1bc` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab1c0"></a> `00bab1c0` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab1c4"></a> `00bab1c4` | `e1 00 00 54` | b.ne 0x00bab1e0 | `CONDITIONAL_JUMP`
<a id="insn-00bab1c8"></a> `00bab1c8` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab1cc"></a> `00bab1cc` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab1d0"></a> `00bab1d0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab1d4"></a> `00bab1d4` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab1d8"></a> `00bab1d8` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab1dc"></a> `00bab1dc` | `06 00 00 14` | b 0x00bab1f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab1e0"></a> `00bab1e0` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab1e4"></a> `00bab1e4` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab1e8"></a> `00bab1e8` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab1ec"></a> `00bab1ec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab1f0"></a> `00bab1f0` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab1f4"></a> `00bab1f4` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab1f8"></a> `00bab1f8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab1fc"></a> `00bab1fc` | `d5 c6 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab200"></a> `00bab200` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab204"></a> `00bab204` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab208"></a> `00bab208` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab20c"></a> `00bab20c` | `20 0c 00 54` | b.eq 0x00bab390 | `CONDITIONAL_JUMP`
<a id="insn-00bab210"></a> `00bab210` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab214"></a> `00bab214` | `e9 0b 00 35` | cbnz w9,0x00bab390 | `CONDITIONAL_JUMP`
<a id="insn-00bab218"></a> `00bab218` | `1f 20 40 f1` | cmp x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab21c"></a> `00bab21c` | `4b 0b 00 54` | b.lt 0x00bab384 | `CONDITIONAL_JUMP`
<a id="insn-00bab220"></a> `00bab220` | `e8 ff 8f 52` | mov w8,#0x7fff | `FALL_THROUGH`
<a id="insn-00bab224"></a> `00bab224` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab228"></a> `00bab228` | `94 0b 00 b5` | cbnz x20,0x00bab398 | `CONDITIONAL_JUMP`
<a id="insn-00bab22c"></a> `00bab22c` | `5c 00 00 14` | b 0x00bab39c | `UNCONDITIONAL_JUMP`
<a id="insn-00bab230"></a> `00bab230` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab234"></a> `00bab234` | `61 01 00 54` | b.ne 0x00bab260 | `CONDITIONAL_JUMP`
<a id="insn-00bab238"></a> `00bab238` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab23c"></a> `00bab23c` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab240"></a> `00bab240` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab244"></a> `00bab244` | `e1 00 00 54` | b.ne 0x00bab260 | `CONDITIONAL_JUMP`
<a id="insn-00bab248"></a> `00bab248` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab24c"></a> `00bab24c` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab250"></a> `00bab250` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab254"></a> `00bab254` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab258"></a> `00bab258` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab25c"></a> `00bab25c` | `06 00 00 14` | b 0x00bab274 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab260"></a> `00bab260` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab264"></a> `00bab264` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab268"></a> `00bab268` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab26c"></a> `00bab26c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab270"></a> `00bab270` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab274"></a> `00bab274` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab278"></a> `00bab278` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab27c"></a> `00bab27c` | `b5 c6 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab280"></a> `00bab280` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab284"></a> `00bab284` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab288"></a> `00bab288` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab28c"></a> `00bab28c` | `c0 00 00 54` | b.eq 0x00bab2a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab290"></a> `00bab290` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab294"></a> `00bab294` | `89 00 00 35` | cbnz w9,0x00bab2a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab298"></a> `00bab298` | `e8 ff 9f 52` | mov w8,#0xffff | `FALL_THROUGH`
<a id="insn-00bab29c"></a> `00bab29c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab2a0"></a> `00bab2a0` | `08 30 88 1a` | csel w8,w0,w8,cc | `FALL_THROUGH`
<a id="insn-00bab2a4"></a> `00bab2a4` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab2a8"></a> `00bab2a8` | `54 00 00 b4` | cbz x20,0x00bab2b0 | `CONDITIONAL_JUMP`
<a id="insn-00bab2ac"></a> `00bab2ac` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab2b0"></a> `00bab2b0` | `53 00 00 b4` | cbz x19,0x00bab2b8 | `CONDITIONAL_JUMP`
<a id="insn-00bab2b4"></a> `00bab2b4` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab2b8"></a> `00bab2b8` | `29 3d 00 12` | and w9,w9,#0xffff | `FALL_THROUGH`
<a id="insn-00bab2bc"></a> `00bab2bc` | `3f 21 28 6b` | cmp w9,w8, UXTH  | `FALL_THROUGH`
<a id="insn-00bab2c0"></a> `00bab2c0` | `39 ff ff 17` | b 0x00baafa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab2c4"></a> `00bab2c4` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-00bab2c8"></a> `00bab2c8` | `61 01 00 54` | b.ne 0x00bab2f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab2cc"></a> `00bab2cc` | `a8 6a 68 38` | ldrb w8,[x21, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bab2d0"></a> `00bab2d0` | `08 79 1a 12` | and w8,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-00bab2d4"></a> `00bab2d4` | `1f 61 01 71` | cmp w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bab2d8"></a> `00bab2d8` | `e1 00 00 54` | b.ne 0x00bab2f4 | `CONDITIONAL_JUMP`
<a id="insn-00bab2dc"></a> `00bab2dc` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab2e0"></a> `00bab2e0` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab2e4"></a> `00bab2e4` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab2e8"></a> `00bab2e8` | `02 02 80 52` | mov w2,#0x10 | `FALL_THROUGH`
<a id="insn-00bab2ec"></a> `00bab2ec` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab2f0"></a> `00bab2f0` | `06 00 00 14` | b 0x00bab308 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab2f4"></a> `00bab2f4` | `88 07 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab2f8"></a> `00bab2f8` | `08 19 42 f9` | ldr x8,[x8, #0x430] | `FALL_THROUGH`
<a id="insn-00bab2fc"></a> `00bab2fc` | `f5 03 00 f9` | str x21,[sp] | `FALL_THROUGH`
<a id="insn-00bab300"></a> `00bab300` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bab304"></a> `00bab304` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-00bab308"></a> `00bab308` | `03 01 40 f9` | ldr x3,[x8] | `FALL_THROUGH`
<a id="insn-00bab30c"></a> `00bab30c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab310"></a> `00bab310` | `90 c6 02 94` | bl 0x00c5cd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab314"></a> `00bab314` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00bab318"></a> `00bab318` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bab31c"></a> `00bab31c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00bab320"></a> `00bab320` | `c0 00 00 54` | b.eq 0x00bab338 | `CONDITIONAL_JUMP`
<a id="insn-00bab324"></a> `00bab324` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bab328"></a> `00bab328` | `89 00 00 35` | cbnz w9,0x00bab338 | `CONDITIONAL_JUMP`
<a id="insn-00bab32c"></a> `00bab32c` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bab330"></a> `00bab330` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00bab334"></a> `00bab334` | `08 30 9f 5a` | csinv w8,w0,wzr,cc | `FALL_THROUGH`
<a id="insn-00bab338"></a> `00bab338` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab33c"></a> `00bab33c` | `54 00 00 b4` | cbz x20,0x00bab344 | `CONDITIONAL_JUMP`
<a id="insn-00bab340"></a> `00bab340` | `89 02 40 b9` | ldr w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab344"></a> `00bab344` | `53 00 00 b4` | cbz x19,0x00bab34c | `CONDITIONAL_JUMP`
<a id="insn-00bab348"></a> `00bab348` | `68 02 40 b9` | ldr w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab34c"></a> `00bab34c` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bab350"></a> `00bab350` | `15 ff ff 17` | b 0x00baafa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab354"></a> `00bab354` | `1f 00 02 b1` | cmn x0,#0x80 | `FALL_THROUGH`
<a id="insn-00bab358"></a> `00bab358` | `e8 0f 80 12` | mov w8,#0xffffff80 | `FALL_THROUGH`
<a id="insn-00bab35c"></a> `00bab35c` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab360"></a> `00bab360` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab364"></a> `00bab364` | `54 00 00 b4` | cbz x20,0x00bab36c | `CONDITIONAL_JUMP`
<a id="insn-00bab368"></a> `00bab368` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab36c"></a> `00bab36c` | `53 00 00 b4` | cbz x19,0x00bab374 | `CONDITIONAL_JUMP`
<a id="insn-00bab370"></a> `00bab370` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab374"></a> `00bab374` | `29 1d 00 13` | sxtb w9,w9 | `FALL_THROUGH`
<a id="insn-00bab378"></a> `00bab378` | `3f 81 28 6b` | cmp w9,w8, SXTB  | `FALL_THROUGH`
<a id="insn-00bab37c"></a> `00bab37c` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab380"></a> `00bab380` | `0a ff ff 17` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab384"></a> `00bab384` | `1f 20 40 b1` | cmn x0,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bab388"></a> `00bab388` | `e8 ff 8f 12` | mov w8,#0xffff8000 | `FALL_THROUGH`
<a id="insn-00bab38c"></a> `00bab38c` | `08 c0 88 1a` | csel w8,w0,w8,gt | `FALL_THROUGH`
<a id="insn-00bab390"></a> `00bab390` | `e9 03 08 2a` | mov w9,w8 | `FALL_THROUGH`
<a id="insn-00bab394"></a> `00bab394` | `54 00 00 b4` | cbz x20,0x00bab39c | `CONDITIONAL_JUMP`
<a id="insn-00bab398"></a> `00bab398` | `89 02 40 79` | ldrh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bab39c"></a> `00bab39c` | `53 00 00 b4` | cbz x19,0x00bab3a4 | `CONDITIONAL_JUMP`
<a id="insn-00bab3a0"></a> `00bab3a0` | `68 02 40 79` | ldrh w8,[x19] | `FALL_THROUGH`
<a id="insn-00bab3a4"></a> `00bab3a4` | `29 3d 00 13` | sxth w9,w9 | `FALL_THROUGH`
<a id="insn-00bab3a8"></a> `00bab3a8` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00bab3ac"></a> `00bab3ac` | `e0 a7 9f 1a` | cset w0,lt | `FALL_THROUGH`
<a id="insn-00bab3b0"></a> `00bab3b0` | `fe fe ff 17` | b 0x00baafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab3b4"></a> `00bab3b4` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bab3b8"></a> `00bab3b8` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab3bc"></a> `00bab3bc` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bab3c0"></a> `00bab3c0` | `28 81 88 9a` | csel x8,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bab3c4"></a> `00bab3c4` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bab3c8"></a> `00bab3c8` | `1f b5 00 71` | cmp w8,#0x2d | `FALL_THROUGH`
<a id="insn-00bab3cc"></a> `00bab3cc` | `61 00 00 54` | b.ne 0x00bab3d8 | `CONDITIONAL_JUMP`
<a id="insn-00bab3d0"></a> `00bab3d0` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00bab3d4"></a> `00bab3d4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bab3d8"></a> `00bab3d8` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bab3dc"></a> `00bab3dc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab3e0"></a> `00bab3e0` | `89 12 88 9a` | csel x9,x20,x8,ne | `FALL_THROUGH`
<a id="insn-00bab3e4"></a> `00bab3e4` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bab3e8"></a> `00bab3e8` | `68 12 88 9a` | csel x8,x19,x8,ne | `FALL_THROUGH`
<a id="insn-00bab3ec"></a> `00bab3ec` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bab3f0"></a> `00bab3f0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bab3f4"></a> `00bab3f4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bab3f8"></a> `00bab3f8` | `eb fe ff 17` | b 0x00baafa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bab3fc"></a> `00bab3fc` | `b9 b1 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaae4`](#insn-00baaae4) 範囲 `[['00baaae4', '00baab03']]`
  - `FALL_THROUGH` [`00baab00`](#insn-00baab00) → [`00baab04`](#insn-00baab04)
- ブロック [`00baab04`](#insn-00baab04) 範囲 `[['00baab04', '00baab0f']]`
  - `CONDITIONAL_JUMP` [`00baab0c`](#insn-00baab0c) → [`00baad84`](#insn-00baad84)
  - `FALL_THROUGH` [`00baab0c`](#insn-00baab0c) → [`00baab10`](#insn-00baab10)
- ブロック [`00baab10`](#insn-00baab10) 範囲 `[['00baab10', '00baab2b']]`
  - `FALL_THROUGH` [`00baab28`](#insn-00baab28) → [`00baab2c`](#insn-00baab2c)
- ブロック [`00baab2c`](#insn-00baab2c) 範囲 `[['00baab2c', '00baab2f']]`
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baab30`](#insn-00baab30)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baad8c`](#insn-00baad8c)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baad0c`](#insn-00baad0c)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baad54`](#insn-00baad54)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baabf0`](#insn-00baabf0)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baada4`](#insn-00baada4)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baadbc`](#insn-00baadbc)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baad6c`](#insn-00baad6c)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baadd4`](#insn-00baadd4)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baac38`](#insn-00baac38)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baadec`](#insn-00baadec)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baab78`](#insn-00baab78)
  - `COMPUTED_JUMP` [`00baab2c`](#insn-00baab2c) → [`00baac90`](#insn-00baac90)
- ブロック [`00baab30`](#insn-00baab30) 範囲 `[['00baab30', '00baab33']]`
  - `CONDITIONAL_JUMP` [`00baab30`](#insn-00baab30) → [`00baab38`](#insn-00baab38)
  - `FALL_THROUGH` [`00baab30`](#insn-00baab30) → [`00baab34`](#insn-00baab34)
- ブロック [`00baab34`](#insn-00baab34) 範囲 `[['00baab34', '00baab37']]`
  - `CONDITIONAL_JUMP` [`00baab34`](#insn-00baab34) → [`00baad94`](#insn-00baad94)
  - `FALL_THROUGH` [`00baab34`](#insn-00baab34) → [`00baab38`](#insn-00baab38)
- ブロック [`00baab38`](#insn-00baab38) 範囲 `[['00baab38', '00baab53']]`
  - `CONDITIONAL_JUMP` [`00baab50`](#insn-00baab50) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baab50`](#insn-00baab50) → [`00baab54`](#insn-00baab54)
- ブロック [`00baab54`](#insn-00baab54) 範囲 `[['00baab54', '00baab57']]`
  - `FALL_THROUGH` [`00baab54`](#insn-00baab54) → [`00baab58`](#insn-00baab58)
- ブロック [`00baab58`](#insn-00baab58) 範囲 `[['00baab58', '00baab67']]`
  - `CONDITIONAL_JUMP` [`00baab64`](#insn-00baab64) → [`00baaf14`](#insn-00baaf14)
  - `FALL_THROUGH` [`00baab64`](#insn-00baab64) → [`00baab68`](#insn-00baab68)
- ブロック [`00baab68`](#insn-00baab68) 範囲 `[['00baab68', '00baab73']]`
  - `CONDITIONAL_JUMP` [`00baab70`](#insn-00baab70) → [`00baab58`](#insn-00baab58)
  - `FALL_THROUGH` [`00baab70`](#insn-00baab70) → [`00baab74`](#insn-00baab74)
- ブロック [`00baab74`](#insn-00baab74) 範囲 `[['00baab74', '00baab77']]`
  - `UNCONDITIONAL_JUMP` [`00baab74`](#insn-00baab74) → [`00baaf44`](#insn-00baaf44)
- ブロック [`00baab78`](#insn-00baab78) 範囲 `[['00baab78', '00baab7b']]`
  - `CONDITIONAL_JUMP` [`00baab78`](#insn-00baab78) → [`00baab84`](#insn-00baab84)
  - `FALL_THROUGH` [`00baab78`](#insn-00baab78) → [`00baab7c`](#insn-00baab7c)
- ブロック [`00baab7c`](#insn-00baab7c) 範囲 `[['00baab7c', '00baab7f']]`
  - `FALL_THROUGH` [`00baab7c`](#insn-00baab7c) → [`00baab80`](#insn-00baab80)
- ブロック [`00baab80`](#insn-00baab80) 範囲 `[['00baab80', '00baab83']]`
  - `CONDITIONAL_JUMP` [`00baab80`](#insn-00baab80) → [`00baabd4`](#insn-00baabd4)
  - `FALL_THROUGH` [`00baab80`](#insn-00baab80) → [`00baab84`](#insn-00baab84)
- ブロック [`00baab84`](#insn-00baab84) 範囲 `[['00baab84', '00baaba3']]`
  - `FALL_THROUGH` [`00baaba0`](#insn-00baaba0) → [`00baaba4`](#insn-00baaba4)
- ブロック [`00baaba4`](#insn-00baaba4) 範囲 `[['00baaba4', '00baabb7']]`
  - `CONDITIONAL_JUMP` [`00baabb4`](#insn-00baabb4) → [`00baabd4`](#insn-00baabd4)
  - `FALL_THROUGH` [`00baabb4`](#insn-00baabb4) → [`00baabb8`](#insn-00baabb8)
- ブロック [`00baabb8`](#insn-00baabb8) 範囲 `[['00baabb8', '00baabbf']]`
  - `CONDITIONAL_JUMP` [`00baabbc`](#insn-00baabbc) → [`00baabd4`](#insn-00baabd4)
  - `FALL_THROUGH` [`00baabbc`](#insn-00baabbc) → [`00baabc0`](#insn-00baabc0)
- ブロック [`00baabc0`](#insn-00baabc0) 範囲 `[['00baabc0', '00baabcb']]`
  - `CONDITIONAL_JUMP` [`00baabc8`](#insn-00baabc8) → [`00baabd4`](#insn-00baabd4)
  - `FALL_THROUGH` [`00baabc8`](#insn-00baabc8) → [`00baabcc`](#insn-00baabcc)
- ブロック [`00baabcc`](#insn-00baabcc) 範囲 `[['00baabcc', '00baabcf']]`
  - `FALL_THROUGH` [`00baabcc`](#insn-00baabcc) → [`00baabd0`](#insn-00baabd0)
- ブロック [`00baabd0`](#insn-00baabd0) 範囲 `[['00baabd0', '00baabd3']]`
  - `FALL_THROUGH` [`00baabd0`](#insn-00baabd0) → [`00baabd4`](#insn-00baabd4)
- ブロック [`00baabd4`](#insn-00baabd4) 範囲 `[['00baabd4', '00baabdb']]`
  - `CONDITIONAL_JUMP` [`00baabd8`](#insn-00baabd8) → [`00baabe0`](#insn-00baabe0)
  - `FALL_THROUGH` [`00baabd8`](#insn-00baabd8) → [`00baabdc`](#insn-00baabdc)
- ブロック [`00baabdc`](#insn-00baabdc) 範囲 `[['00baabdc', '00baabdf']]`
  - `FALL_THROUGH` [`00baabdc`](#insn-00baabdc) → [`00baabe0`](#insn-00baabe0)
- ブロック [`00baabe0`](#insn-00baabe0) 範囲 `[['00baabe0', '00baabe3']]`
  - `CONDITIONAL_JUMP` [`00baabe0`](#insn-00baabe0) → [`00baabe8`](#insn-00baabe8)
  - `FALL_THROUGH` [`00baabe0`](#insn-00baabe0) → [`00baabe4`](#insn-00baabe4)
- ブロック [`00baabe4`](#insn-00baabe4) 範囲 `[['00baabe4', '00baabe7']]`
  - `FALL_THROUGH` [`00baabe4`](#insn-00baabe4) → [`00baabe8`](#insn-00baabe8)
- ブロック [`00baabe8`](#insn-00baabe8) 範囲 `[['00baabe8', '00baabef']]`
  - `UNCONDITIONAL_JUMP` [`00baabec`](#insn-00baabec) → [`00baad04`](#insn-00baad04)
- ブロック [`00baabf0`](#insn-00baabf0) 範囲 `[['00baabf0', '00baabf3']]`
  - `CONDITIONAL_JUMP` [`00baabf0`](#insn-00baabf0) → [`00baabf8`](#insn-00baabf8)
  - `FALL_THROUGH` [`00baabf0`](#insn-00baabf0) → [`00baabf4`](#insn-00baabf4)
- ブロック [`00baabf4`](#insn-00baabf4) 範囲 `[['00baabf4', '00baabf7']]`
  - `CONDITIONAL_JUMP` [`00baabf4`](#insn-00baabf4) → [`00baad94`](#insn-00baad94)
  - `FALL_THROUGH` [`00baabf4`](#insn-00baabf4) → [`00baabf8`](#insn-00baabf8)
- ブロック [`00baabf8`](#insn-00baabf8) 範囲 `[['00baabf8', '00baac13']]`
  - `CONDITIONAL_JUMP` [`00baac10`](#insn-00baac10) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baac10`](#insn-00baac10) → [`00baac14`](#insn-00baac14)
- ブロック [`00baac14`](#insn-00baac14) 範囲 `[['00baac14', '00baac17']]`
  - `FALL_THROUGH` [`00baac14`](#insn-00baac14) → [`00baac18`](#insn-00baac18)
- ブロック [`00baac18`](#insn-00baac18) 範囲 `[['00baac18', '00baac1f']]`
  - `FALL_THROUGH` [`00baac1c`](#insn-00baac1c) → [`00baac20`](#insn-00baac20)
- ブロック [`00baac20`](#insn-00baac20) 範囲 `[['00baac20', '00baac27']]`
  - `CONDITIONAL_JUMP` [`00baac24`](#insn-00baac24) → [`00baaf14`](#insn-00baaf14)
  - `FALL_THROUGH` [`00baac24`](#insn-00baac24) → [`00baac28`](#insn-00baac28)
- ブロック [`00baac28`](#insn-00baac28) 範囲 `[['00baac28', '00baac33']]`
  - `CONDITIONAL_JUMP` [`00baac30`](#insn-00baac30) → [`00baac18`](#insn-00baac18)
  - `FALL_THROUGH` [`00baac30`](#insn-00baac30) → [`00baac34`](#insn-00baac34)
- ブロック [`00baac34`](#insn-00baac34) 範囲 `[['00baac34', '00baac37']]`
  - `UNCONDITIONAL_JUMP` [`00baac34`](#insn-00baac34) → [`00baaf44`](#insn-00baaf44)
- ブロック [`00baac38`](#insn-00baac38) 範囲 `[['00baac38', '00baac3b']]`
  - `FALL_THROUGH` [`00baac38`](#insn-00baac38) → [`00baac3c`](#insn-00baac3c)
- ブロック [`00baac3c`](#insn-00baac3c) 範囲 `[['00baac3c', '00baac3f']]`
  - `CONDITIONAL_JUMP` [`00baac3c`](#insn-00baac3c) → [`00baac44`](#insn-00baac44)
  - `FALL_THROUGH` [`00baac3c`](#insn-00baac3c) → [`00baac40`](#insn-00baac40)
- ブロック [`00baac40`](#insn-00baac40) 範囲 `[['00baac40', '00baac43']]`
  - `CONDITIONAL_JUMP` [`00baac40`](#insn-00baac40) → [`00baac68`](#insn-00baac68)
  - `FALL_THROUGH` [`00baac40`](#insn-00baac40) → [`00baac44`](#insn-00baac44)
- ブロック [`00baac44`](#insn-00baac44) 範囲 `[['00baac44', '00baac47']]`
  - `FALL_THROUGH` [`00baac44`](#insn-00baac44) → [`00baac48`](#insn-00baac48)
- ブロック [`00baac48`](#insn-00baac48) 範囲 `[['00baac48', '00baac67']]`
  - `FALL_THROUGH` [`00baac64`](#insn-00baac64) → [`00baac68`](#insn-00baac68)
- ブロック [`00baac68`](#insn-00baac68) 範囲 `[['00baac68', '00baac8f']]`
  - `UNCONDITIONAL_JUMP` [`00baac8c`](#insn-00baac8c) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00baac90`](#insn-00baac90) 範囲 `[['00baac90', '00baac93']]`
  - `CONDITIONAL_JUMP` [`00baac90`](#insn-00baac90) → [`00baac9c`](#insn-00baac9c)
  - `FALL_THROUGH` [`00baac90`](#insn-00baac90) → [`00baac94`](#insn-00baac94)
- ブロック [`00baac94`](#insn-00baac94) 範囲 `[['00baac94', '00baac9b']]`
  - `CONDITIONAL_JUMP` [`00baac98`](#insn-00baac98) → [`00baacec`](#insn-00baacec)
  - `FALL_THROUGH` [`00baac98`](#insn-00baac98) → [`00baac9c`](#insn-00baac9c)
- ブロック [`00baac9c`](#insn-00baac9c) 範囲 `[['00baac9c', '00baaccf']]`
  - `CONDITIONAL_JUMP` [`00baaccc`](#insn-00baaccc) → [`00baacec`](#insn-00baacec)
  - `FALL_THROUGH` [`00baaccc`](#insn-00baaccc) → [`00baacd0`](#insn-00baacd0)
- ブロック [`00baacd0`](#insn-00baacd0) 範囲 `[['00baacd0', '00baacd7']]`
  - `CONDITIONAL_JUMP` [`00baacd4`](#insn-00baacd4) → [`00baacec`](#insn-00baacec)
  - `FALL_THROUGH` [`00baacd4`](#insn-00baacd4) → [`00baacd8`](#insn-00baacd8)
- ブロック [`00baacd8`](#insn-00baacd8) 範囲 `[['00baacd8', '00baace3']]`
  - `CONDITIONAL_JUMP` [`00baace0`](#insn-00baace0) → [`00baacec`](#insn-00baacec)
  - `FALL_THROUGH` [`00baace0`](#insn-00baace0) → [`00baace4`](#insn-00baace4)
- ブロック [`00baace4`](#insn-00baace4) 範囲 `[['00baace4', '00baaceb']]`
  - `FALL_THROUGH` [`00baace8`](#insn-00baace8) → [`00baacec`](#insn-00baacec)
- ブロック [`00baacec`](#insn-00baacec) 範囲 `[['00baacec', '00baacf3']]`
  - `CONDITIONAL_JUMP` [`00baacf0`](#insn-00baacf0) → [`00baacf8`](#insn-00baacf8)
  - `FALL_THROUGH` [`00baacf0`](#insn-00baacf0) → [`00baacf4`](#insn-00baacf4)
- ブロック [`00baacf4`](#insn-00baacf4) 範囲 `[['00baacf4', '00baacf7']]`
  - `FALL_THROUGH` [`00baacf4`](#insn-00baacf4) → [`00baacf8`](#insn-00baacf8)
- ブロック [`00baacf8`](#insn-00baacf8) 範囲 `[['00baacf8', '00baacfb']]`
  - `CONDITIONAL_JUMP` [`00baacf8`](#insn-00baacf8) → [`00baad00`](#insn-00baad00)
  - `FALL_THROUGH` [`00baacf8`](#insn-00baacf8) → [`00baacfc`](#insn-00baacfc)
- ブロック [`00baacfc`](#insn-00baacfc) 範囲 `[['00baacfc', '00baacff']]`
  - `FALL_THROUGH` [`00baacfc`](#insn-00baacfc) → [`00baad00`](#insn-00baad00)
- ブロック [`00baad00`](#insn-00baad00) 範囲 `[['00baad00', '00baad03']]`
  - `FALL_THROUGH` [`00baad00`](#insn-00baad00) → [`00baad04`](#insn-00baad04)
- ブロック [`00baad04`](#insn-00baad04) 範囲 `[['00baad04', '00baad0b']]`
  - `UNCONDITIONAL_JUMP` [`00baad08`](#insn-00baad08) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00baad0c`](#insn-00baad0c) 範囲 `[['00baad0c', '00baad0f']]`
  - `CONDITIONAL_JUMP` [`00baad0c`](#insn-00baad0c) → [`00baad14`](#insn-00baad14)
  - `FALL_THROUGH` [`00baad0c`](#insn-00baad0c) → [`00baad10`](#insn-00baad10)
- ブロック [`00baad10`](#insn-00baad10) 範囲 `[['00baad10', '00baad13']]`
  - `CONDITIONAL_JUMP` [`00baad10`](#insn-00baad10) → [`00baad94`](#insn-00baad94)
  - `FALL_THROUGH` [`00baad10`](#insn-00baad10) → [`00baad14`](#insn-00baad14)
- ブロック [`00baad14`](#insn-00baad14) 範囲 `[['00baad14', '00baad1b']]`
  - `FALL_THROUGH` [`00baad18`](#insn-00baad18) → [`00baad1c`](#insn-00baad1c)
- ブロック [`00baad1c`](#insn-00baad1c) 範囲 `[['00baad1c', '00baad2f']]`
  - `CONDITIONAL_JUMP` [`00baad2c`](#insn-00baad2c) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baad2c`](#insn-00baad2c) → [`00baad30`](#insn-00baad30)
- ブロック [`00baad30`](#insn-00baad30) 範囲 `[['00baad30', '00baad33']]`
  - `FALL_THROUGH` [`00baad30`](#insn-00baad30) → [`00baad34`](#insn-00baad34)
- ブロック [`00baad34`](#insn-00baad34) 範囲 `[['00baad34', '00baad43']]`
  - `CONDITIONAL_JUMP` [`00baad40`](#insn-00baad40) → [`00baaf14`](#insn-00baaf14)
  - `FALL_THROUGH` [`00baad40`](#insn-00baad40) → [`00baad44`](#insn-00baad44)
- ブロック [`00baad44`](#insn-00baad44) 範囲 `[['00baad44', '00baad4f']]`
  - `CONDITIONAL_JUMP` [`00baad4c`](#insn-00baad4c) → [`00baad34`](#insn-00baad34)
  - `FALL_THROUGH` [`00baad4c`](#insn-00baad4c) → [`00baad50`](#insn-00baad50)
- ブロック [`00baad50`](#insn-00baad50) 範囲 `[['00baad50', '00baad53']]`
  - `UNCONDITIONAL_JUMP` [`00baad50`](#insn-00baad50) → [`00baaf44`](#insn-00baaf44)
- ブロック [`00baad54`](#insn-00baad54) 範囲 `[['00baad54', '00baad57']]`
  - `CONDITIONAL_JUMP` [`00baad54`](#insn-00baad54) → [`00baae54`](#insn-00baae54)
  - `FALL_THROUGH` [`00baad54`](#insn-00baad54) → [`00baad58`](#insn-00baad58)
- ブロック [`00baad58`](#insn-00baad58) 範囲 `[['00baad58', '00baad5b']]`
  - `CONDITIONAL_JUMP` [`00baad58`](#insn-00baad58) → [`00baae54`](#insn-00baae54)
  - `FALL_THROUGH` [`00baad58`](#insn-00baad58) → [`00baad5c`](#insn-00baad5c)
- ブロック [`00baad5c`](#insn-00baad5c) 範囲 `[['00baad5c', '00baad67']]`
  - `CONDITIONAL_JUMP` [`00baad64`](#insn-00baad64) → [`00bab368`](#insn-00bab368)
  - `FALL_THROUGH` [`00baad64`](#insn-00baad64) → [`00baad68`](#insn-00baad68)
- ブロック [`00baad68`](#insn-00baad68) 範囲 `[['00baad68', '00baad6b']]`
  - `UNCONDITIONAL_JUMP` [`00baad68`](#insn-00baad68) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00baad6c`](#insn-00baad6c) 範囲 `[['00baad6c', '00baad6f']]`
  - `CONDITIONAL_JUMP` [`00baad6c`](#insn-00baad6c) → [`00baae94`](#insn-00baae94)
  - `FALL_THROUGH` [`00baad6c`](#insn-00baad6c) → [`00baad70`](#insn-00baad70)
- ブロック [`00baad70`](#insn-00baad70) 範囲 `[['00baad70', '00baad73']]`
  - `CONDITIONAL_JUMP` [`00baad70`](#insn-00baad70) → [`00baae94`](#insn-00baae94)
  - `FALL_THROUGH` [`00baad70`](#insn-00baad70) → [`00baad74`](#insn-00baad74)
- ブロック [`00baad74`](#insn-00baad74) 範囲 `[['00baad74', '00baad7f']]`
  - `CONDITIONAL_JUMP` [`00baad7c`](#insn-00baad7c) → [`00bab198`](#insn-00bab198)
  - `FALL_THROUGH` [`00baad7c`](#insn-00baad7c) → [`00baad80`](#insn-00baad80)
- ブロック [`00baad80`](#insn-00baad80) 範囲 `[['00baad80', '00baad83']]`
  - `UNCONDITIONAL_JUMP` [`00baad80`](#insn-00baad80) → [`00bab19c`](#insn-00bab19c)
- ブロック [`00baad84`](#insn-00baad84) 範囲 `[['00baad84', '00baad8b']]`
  - `UNCONDITIONAL_JUMP` [`00baad88`](#insn-00baad88) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00baad8c`](#insn-00baad8c) 範囲 `[['00baad8c', '00baad8f']]`
  - `CONDITIONAL_JUMP` [`00baad8c`](#insn-00baad8c) → [`00baaed4`](#insn-00baaed4)
  - `FALL_THROUGH` [`00baad8c`](#insn-00baad8c) → [`00baad90`](#insn-00baad90)
- ブロック [`00baad90`](#insn-00baad90) 範囲 `[['00baad90', '00baad93']]`
  - `CONDITIONAL_JUMP` [`00baad90`](#insn-00baad90) → [`00baaed4`](#insn-00baaed4)
  - `FALL_THROUGH` [`00baad90`](#insn-00baad90) → [`00baad94`](#insn-00baad94)
- ブロック [`00baad94`](#insn-00baad94) 範囲 `[['00baad94', '00baad9b']]`
  - `FALL_THROUGH` [`00baad98`](#insn-00baad98) → [`00baad9c`](#insn-00baad9c)
- ブロック [`00baad9c`](#insn-00baad9c) 範囲 `[['00baad9c', '00baad9f']]`
  - `CONDITIONAL_JUMP` [`00baad9c`](#insn-00baad9c) → [`00baaf90`](#insn-00baaf90)
  - `FALL_THROUGH` [`00baad9c`](#insn-00baad9c) → [`00baada0`](#insn-00baada0)
- ブロック [`00baada0`](#insn-00baada0) 範囲 `[['00baada0', '00baada3']]`
  - `UNCONDITIONAL_JUMP` [`00baada0`](#insn-00baada0) → [`00baaf94`](#insn-00baaf94)
- ブロック [`00baada4`](#insn-00baada4) 範囲 `[['00baada4', '00baada7']]`
  - `CONDITIONAL_JUMP` [`00baada4`](#insn-00baada4) → [`00baafcc`](#insn-00baafcc)
  - `FALL_THROUGH` [`00baada4`](#insn-00baada4) → [`00baada8`](#insn-00baada8)
- ブロック [`00baada8`](#insn-00baada8) 範囲 `[['00baada8', '00baadab']]`
  - `CONDITIONAL_JUMP` [`00baada8`](#insn-00baada8) → [`00baafcc`](#insn-00baafcc)
  - `FALL_THROUGH` [`00baada8`](#insn-00baada8) → [`00baadac`](#insn-00baadac)
- ブロック [`00baadac`](#insn-00baadac) 範囲 `[['00baadac', '00baadb7']]`
  - `CONDITIONAL_JUMP` [`00baadb4`](#insn-00baadb4) → [`00bab398`](#insn-00bab398)
  - `FALL_THROUGH` [`00baadb4`](#insn-00baadb4) → [`00baadb8`](#insn-00baadb8)
- ブロック [`00baadb8`](#insn-00baadb8) 範囲 `[['00baadb8', '00baadbb']]`
  - `UNCONDITIONAL_JUMP` [`00baadb8`](#insn-00baadb8) → [`00bab39c`](#insn-00bab39c)
- ブロック [`00baadbc`](#insn-00baadbc) 範囲 `[['00baadbc', '00baadbf']]`
  - `CONDITIONAL_JUMP` [`00baadbc`](#insn-00baadbc) → [`00bab00c`](#insn-00bab00c)
  - `FALL_THROUGH` [`00baadbc`](#insn-00baadbc) → [`00baadc0`](#insn-00baadc0)
- ブロック [`00baadc0`](#insn-00baadc0) 範囲 `[['00baadc0', '00baadc3']]`
  - `CONDITIONAL_JUMP` [`00baadc0`](#insn-00baadc0) → [`00bab00c`](#insn-00bab00c)
  - `FALL_THROUGH` [`00baadc0`](#insn-00baadc0) → [`00baadc4`](#insn-00baadc4)
- ブロック [`00baadc4`](#insn-00baadc4) 範囲 `[['00baadc4', '00baadcf']]`
  - `CONDITIONAL_JUMP` [`00baadcc`](#insn-00baadcc) → [`00bab2ac`](#insn-00bab2ac)
  - `FALL_THROUGH` [`00baadcc`](#insn-00baadcc) → [`00baadd0`](#insn-00baadd0)
- ブロック [`00baadd0`](#insn-00baadd0) 範囲 `[['00baadd0', '00baadd3']]`
  - `UNCONDITIONAL_JUMP` [`00baadd0`](#insn-00baadd0) → [`00bab2b0`](#insn-00bab2b0)
- ブロック [`00baadd4`](#insn-00baadd4) 範囲 `[['00baadd4', '00baadd7']]`
  - `CONDITIONAL_JUMP` [`00baadd4`](#insn-00baadd4) → [`00bab04c`](#insn-00bab04c)
  - `FALL_THROUGH` [`00baadd4`](#insn-00baadd4) → [`00baadd8`](#insn-00baadd8)
- ブロック [`00baadd8`](#insn-00baadd8) 範囲 `[['00baadd8', '00baaddb']]`
  - `CONDITIONAL_JUMP` [`00baadd8`](#insn-00baadd8) → [`00bab04c`](#insn-00bab04c)
  - `FALL_THROUGH` [`00baadd8`](#insn-00baadd8) → [`00baaddc`](#insn-00baaddc)
- ブロック [`00baaddc`](#insn-00baaddc) 範囲 `[['00baaddc', '00baade7']]`
  - `CONDITIONAL_JUMP` [`00baade4`](#insn-00baade4) → [`00bab340`](#insn-00bab340)
  - `FALL_THROUGH` [`00baade4`](#insn-00baade4) → [`00baade8`](#insn-00baade8)
- ブロック [`00baade8`](#insn-00baade8) 範囲 `[['00baade8', '00baadeb']]`
  - `UNCONDITIONAL_JUMP` [`00baade8`](#insn-00baade8) → [`00bab344`](#insn-00bab344)
- ブロック [`00baadec`](#insn-00baadec) 範囲 `[['00baadec', '00baadf3']]`
  - `CONDITIONAL_JUMP` [`00baadf0`](#insn-00baadf0) → [`00baadf8`](#insn-00baadf8)
  - `FALL_THROUGH` [`00baadf0`](#insn-00baadf0) → [`00baadf4`](#insn-00baadf4)
- ブロック [`00baadf4`](#insn-00baadf4) 範囲 `[['00baadf4', '00baadf7']]`
  - `CONDITIONAL_JUMP` [`00baadf4`](#insn-00baadf4) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00baadf4`](#insn-00baadf4) → [`00baadf8`](#insn-00baadf8)
- ブロック [`00baadf8`](#insn-00baadf8) 範囲 `[['00baadf8', '00baae0b']]`
  - `FALL_THROUGH` [`00baae08`](#insn-00baae08) → [`00baae0c`](#insn-00baae0c)
- ブロック [`00baae0c`](#insn-00baae0c) 範囲 `[['00baae0c', '00baae27']]`
  - `CONDITIONAL_JUMP` [`00baae24`](#insn-00baae24) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00baae24`](#insn-00baae24) → [`00baae28`](#insn-00baae28)
- ブロック [`00baae28`](#insn-00baae28) 範囲 `[['00baae28', '00baae2b']]`
  - `CONDITIONAL_JUMP` [`00baae28`](#insn-00baae28) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00baae28`](#insn-00baae28) → [`00baae2c`](#insn-00baae2c)
- ブロック [`00baae2c`](#insn-00baae2c) 範囲 `[['00baae2c', '00baae33']]`
  - `CONDITIONAL_JUMP` [`00baae30`](#insn-00baae30) → [`00bab3b4`](#insn-00bab3b4)
  - `FALL_THROUGH` [`00baae30`](#insn-00baae30) → [`00baae34`](#insn-00baae34)
- ブロック [`00baae34`](#insn-00baae34) 範囲 `[['00baae34', '00baae37']]`
  - `FALL_THROUGH` [`00baae34`](#insn-00baae34) → [`00baae38`](#insn-00baae38)
- ブロック [`00baae38`](#insn-00baae38) 範囲 `[['00baae38', '00baae47']]`
  - `CONDITIONAL_JUMP` [`00baae44`](#insn-00baae44) → [`00bab3b8`](#insn-00bab3b8)
  - `FALL_THROUGH` [`00baae44`](#insn-00baae44) → [`00baae48`](#insn-00baae48)
- ブロック [`00baae48`](#insn-00baae48) 範囲 `[['00baae48', '00baae4f']]`
  - `CONDITIONAL_JUMP` [`00baae4c`](#insn-00baae4c) → [`00baae38`](#insn-00baae38)
  - `FALL_THROUGH` [`00baae4c`](#insn-00baae4c) → [`00baae50`](#insn-00baae50)
- ブロック [`00baae50`](#insn-00baae50) 範囲 `[['00baae50', '00baae53']]`
  - `UNCONDITIONAL_JUMP` [`00baae50`](#insn-00baae50) → [`00bab3b8`](#insn-00bab3b8)
- ブロック [`00baae54`](#insn-00baae54) 範囲 `[['00baae54', '00baae5b']]`
  - `FALL_THROUGH` [`00baae58`](#insn-00baae58) → [`00baae5c`](#insn-00baae5c)
- ブロック [`00baae5c`](#insn-00baae5c) 範囲 `[['00baae5c', '00baae6f']]`
  - `CONDITIONAL_JUMP` [`00baae6c`](#insn-00baae6c) → [`00bab0bc`](#insn-00bab0bc)
  - `FALL_THROUGH` [`00baae6c`](#insn-00baae6c) → [`00baae70`](#insn-00baae70)
- ブロック [`00baae70`](#insn-00baae70) 範囲 `[['00baae70', '00baae73']]`
  - `FALL_THROUGH` [`00baae70`](#insn-00baae70) → [`00baae74`](#insn-00baae74)
- ブロック [`00baae74`](#insn-00baae74) 範囲 `[['00baae74', '00baae83']]`
  - `CONDITIONAL_JUMP` [`00baae80`](#insn-00baae80) → [`00bab08c`](#insn-00bab08c)
  - `FALL_THROUGH` [`00baae80`](#insn-00baae80) → [`00baae84`](#insn-00baae84)
- ブロック [`00baae84`](#insn-00baae84) 範囲 `[['00baae84', '00baae87']]`
  - `FALL_THROUGH` [`00baae84`](#insn-00baae84) → [`00baae88`](#insn-00baae88)
- ブロック [`00baae88`](#insn-00baae88) 範囲 `[['00baae88', '00baae8f']]`
  - `CONDITIONAL_JUMP` [`00baae8c`](#insn-00baae8c) → [`00baae74`](#insn-00baae74)
  - `FALL_THROUGH` [`00baae8c`](#insn-00baae8c) → [`00baae90`](#insn-00baae90)
- ブロック [`00baae90`](#insn-00baae90) 範囲 `[['00baae90', '00baae93']]`
  - `UNCONDITIONAL_JUMP` [`00baae90`](#insn-00baae90) → [`00bab0bc`](#insn-00bab0bc)
- ブロック [`00baae94`](#insn-00baae94) 範囲 `[['00baae94', '00baaeab']]`
  - `FALL_THROUGH` [`00baaea8`](#insn-00baaea8) → [`00baaeac`](#insn-00baaeac)
- ブロック [`00baaeac`](#insn-00baaeac) 範囲 `[['00baaeac', '00baaeaf']]`
  - `CONDITIONAL_JUMP` [`00baaeac`](#insn-00baaeac) → [`00bab13c`](#insn-00bab13c)
  - `FALL_THROUGH` [`00baaeac`](#insn-00baaeac) → [`00baaeb0`](#insn-00baaeb0)
- ブロック [`00baaeb0`](#insn-00baaeb0) 範囲 `[['00baaeb0', '00baaeb3']]`
  - `FALL_THROUGH` [`00baaeb0`](#insn-00baaeb0) → [`00baaeb4`](#insn-00baaeb4)
- ブロック [`00baaeb4`](#insn-00baaeb4) 範囲 `[['00baaeb4', '00baaec3']]`
  - `CONDITIONAL_JUMP` [`00baaec0`](#insn-00baaec0) → [`00bab10c`](#insn-00bab10c)
  - `FALL_THROUGH` [`00baaec0`](#insn-00baaec0) → [`00baaec4`](#insn-00baaec4)
- ブロック [`00baaec4`](#insn-00baaec4) 範囲 `[['00baaec4', '00baaecf']]`
  - `CONDITIONAL_JUMP` [`00baaecc`](#insn-00baaecc) → [`00baaeb4`](#insn-00baaeb4)
  - `FALL_THROUGH` [`00baaecc`](#insn-00baaecc) → [`00baaed0`](#insn-00baaed0)
- ブロック [`00baaed0`](#insn-00baaed0) 範囲 `[['00baaed0', '00baaed3']]`
  - `UNCONDITIONAL_JUMP` [`00baaed0`](#insn-00baaed0) → [`00bab13c`](#insn-00bab13c)
- ブロック [`00baaed4`](#insn-00baaed4) 範囲 `[['00baaed4', '00baaed7']]`
  - `FALL_THROUGH` [`00baaed4`](#insn-00baaed4) → [`00baaed8`](#insn-00baaed8)
- ブロック [`00baaed8`](#insn-00baaed8) 範囲 `[['00baaed8', '00baaeef']]`
  - `CONDITIONAL_JUMP` [`00baaeec`](#insn-00baaeec) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baaeec`](#insn-00baaeec) → [`00baaef0`](#insn-00baaef0)
- ブロック [`00baaef0`](#insn-00baaef0) 範囲 `[['00baaef0', '00baaef3']]`
  - `FALL_THROUGH` [`00baaef0`](#insn-00baaef0) → [`00baaef4`](#insn-00baaef4)
- ブロック [`00baaef4`](#insn-00baaef4) 範囲 `[['00baaef4', '00baaefb']]`
  - `FALL_THROUGH` [`00baaef8`](#insn-00baaef8) → [`00baaefc`](#insn-00baaefc)
- ブロック [`00baaefc`](#insn-00baaefc) 範囲 `[['00baaefc', '00baaf03']]`
  - `CONDITIONAL_JUMP` [`00baaf00`](#insn-00baaf00) → [`00baaf14`](#insn-00baaf14)
  - `FALL_THROUGH` [`00baaf00`](#insn-00baaf00) → [`00baaf04`](#insn-00baaf04)
- ブロック [`00baaf04`](#insn-00baaf04) 範囲 `[['00baaf04', '00baaf0f']]`
  - `CONDITIONAL_JUMP` [`00baaf0c`](#insn-00baaf0c) → [`00baaef4`](#insn-00baaef4)
  - `FALL_THROUGH` [`00baaf0c`](#insn-00baaf0c) → [`00baaf10`](#insn-00baaf10)
- ブロック [`00baaf10`](#insn-00baaf10) 範囲 `[['00baaf10', '00baaf13']]`
  - `UNCONDITIONAL_JUMP` [`00baaf10`](#insn-00baaf10) → [`00baaf44`](#insn-00baaf44)
- ブロック [`00baaf14`](#insn-00baaf14) 範囲 `[['00baaf14', '00baaf1b']]`
  - `CONDITIONAL_JUMP` [`00baaf18`](#insn-00baaf18) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baaf18`](#insn-00baaf18) → [`00baaf1c`](#insn-00baaf1c)
- ブロック [`00baaf1c`](#insn-00baaf1c) 範囲 `[['00baaf1c', '00baaf27']]`
  - `FALL_THROUGH` [`00baaf24`](#insn-00baaf24) → [`00baaf28`](#insn-00baaf28)
- ブロック [`00baaf28`](#insn-00baaf28) 範囲 `[['00baaf28', '00baaf2b']]`
  - `CONDITIONAL_JUMP` [`00baaf28`](#insn-00baaf28) → [`00baaf44`](#insn-00baaf44)
  - `FALL_THROUGH` [`00baaf28`](#insn-00baaf28) → [`00baaf2c`](#insn-00baaf2c)
- ブロック [`00baaf2c`](#insn-00baaf2c) 範囲 `[['00baaf2c', '00baaf43']]`
  - `UNCONDITIONAL_JUMP` [`00baaf40`](#insn-00baaf40) → [`00baaf58`](#insn-00baaf58)
- ブロック [`00baaf44`](#insn-00baaf44) 範囲 `[['00baaf44', '00baaf47']]`
  - `FALL_THROUGH` [`00baaf44`](#insn-00baaf44) → [`00baaf48`](#insn-00baaf48)
- ブロック [`00baaf48`](#insn-00baaf48) 範囲 `[['00baaf48', '00baaf53']]`
  - `FALL_THROUGH` [`00baaf50`](#insn-00baaf50) → [`00baaf54`](#insn-00baaf54)
- ブロック [`00baaf54`](#insn-00baaf54) 範囲 `[['00baaf54', '00baaf57']]`
  - `FALL_THROUGH` [`00baaf54`](#insn-00baaf54) → [`00baaf58`](#insn-00baaf58)
- ブロック [`00baaf58`](#insn-00baaf58) 範囲 `[['00baaf58', '00baaf73']]`
  - `CONDITIONAL_JUMP` [`00baaf70`](#insn-00baaf70) → [`00baaf88`](#insn-00baaf88)
  - `FALL_THROUGH` [`00baaf70`](#insn-00baaf70) → [`00baaf74`](#insn-00baaf74)
- ブロック [`00baaf74`](#insn-00baaf74) 範囲 `[['00baaf74', '00baaf7b']]`
  - `CONDITIONAL_JUMP` [`00baaf78`](#insn-00baaf78) → [`00baaf88`](#insn-00baaf88)
  - `FALL_THROUGH` [`00baaf78`](#insn-00baaf78) → [`00baaf7c`](#insn-00baaf7c)
- ブロック [`00baaf7c`](#insn-00baaf7c) 範囲 `[['00baaf7c', '00baaf87']]`
  - `FALL_THROUGH` [`00baaf84`](#insn-00baaf84) → [`00baaf88`](#insn-00baaf88)
- ブロック [`00baaf88`](#insn-00baaf88) 範囲 `[['00baaf88', '00baaf8f']]`
  - `CONDITIONAL_JUMP` [`00baaf8c`](#insn-00baaf8c) → [`00baaf94`](#insn-00baaf94)
  - `FALL_THROUGH` [`00baaf8c`](#insn-00baaf8c) → [`00baaf90`](#insn-00baaf90)
- ブロック [`00baaf90`](#insn-00baaf90) 範囲 `[['00baaf90', '00baaf93']]`
  - `FALL_THROUGH` [`00baaf90`](#insn-00baaf90) → [`00baaf94`](#insn-00baaf94)
- ブロック [`00baaf94`](#insn-00baaf94) 範囲 `[['00baaf94', '00baaf97']]`
  - `CONDITIONAL_JUMP` [`00baaf94`](#insn-00baaf94) → [`00baaf9c`](#insn-00baaf9c)
  - `FALL_THROUGH` [`00baaf94`](#insn-00baaf94) → [`00baaf98`](#insn-00baaf98)
- ブロック [`00baaf98`](#insn-00baaf98) 範囲 `[['00baaf98', '00baaf9b']]`
  - `FALL_THROUGH` [`00baaf98`](#insn-00baaf98) → [`00baaf9c`](#insn-00baaf9c)
- ブロック [`00baaf9c`](#insn-00baaf9c) 範囲 `[['00baaf9c', '00baafa3']]`
  - `FALL_THROUGH` [`00baafa0`](#insn-00baafa0) → [`00baafa4`](#insn-00baafa4)
- ブロック [`00baafa4`](#insn-00baafa4) 範囲 `[['00baafa4', '00baafa7']]`
  - `FALL_THROUGH` [`00baafa4`](#insn-00baafa4) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00baafa8`](#insn-00baafa8) 範囲 `[['00baafa8', '00baafb7']]`
  - `CONDITIONAL_JUMP` [`00baafb4`](#insn-00baafb4) → [`00bab3fc`](#insn-00bab3fc)
  - `FALL_THROUGH` [`00baafb4`](#insn-00baafb4) → [`00baafb8`](#insn-00baafb8)
- ブロック [`00baafb8`](#insn-00baafb8) 範囲 `[['00baafb8', '00baafcb']]`
- ブロック [`00baafcc`](#insn-00baafcc) 範囲 `[['00baafcc', '00baafe7']]`
  - `CONDITIONAL_JUMP` [`00baafe4`](#insn-00baafe4) → [`00bab1e0`](#insn-00bab1e0)
  - `FALL_THROUGH` [`00baafe4`](#insn-00baafe4) → [`00baafe8`](#insn-00baafe8)
- ブロック [`00baafe8`](#insn-00baafe8) 範囲 `[['00baafe8', '00baafeb']]`
  - `FALL_THROUGH` [`00baafe8`](#insn-00baafe8) → [`00baafec`](#insn-00baafec)
- ブロック [`00baafec`](#insn-00baafec) 範囲 `[['00baafec', '00baaff7']]`
  - `FALL_THROUGH` [`00baaff4`](#insn-00baaff4) → [`00baaff8`](#insn-00baaff8)
- ブロック [`00baaff8`](#insn-00baaff8) 範囲 `[['00baaff8', '00baaffb']]`
  - `CONDITIONAL_JUMP` [`00baaff8`](#insn-00baaff8) → [`00bab1b0`](#insn-00bab1b0)
  - `FALL_THROUGH` [`00baaff8`](#insn-00baaff8) → [`00baaffc`](#insn-00baaffc)
- ブロック [`00baaffc`](#insn-00baaffc) 範囲 `[['00baaffc', '00bab007']]`
  - `CONDITIONAL_JUMP` [`00bab004`](#insn-00bab004) → [`00baafec`](#insn-00baafec)
  - `FALL_THROUGH` [`00bab004`](#insn-00bab004) → [`00bab008`](#insn-00bab008)
- ブロック [`00bab008`](#insn-00bab008) 範囲 `[['00bab008', '00bab00b']]`
  - `UNCONDITIONAL_JUMP` [`00bab008`](#insn-00bab008) → [`00bab1e0`](#insn-00bab1e0)
- ブロック [`00bab00c`](#insn-00bab00c) 範囲 `[['00bab00c', '00bab027']]`
  - `CONDITIONAL_JUMP` [`00bab024`](#insn-00bab024) → [`00bab260`](#insn-00bab260)
  - `FALL_THROUGH` [`00bab024`](#insn-00bab024) → [`00bab028`](#insn-00bab028)
- ブロック [`00bab028`](#insn-00bab028) 範囲 `[['00bab028', '00bab02b']]`
  - `FALL_THROUGH` [`00bab028`](#insn-00bab028) → [`00bab02c`](#insn-00bab02c)
- ブロック [`00bab02c`](#insn-00bab02c) 範囲 `[['00bab02c', '00bab03b']]`
  - `CONDITIONAL_JUMP` [`00bab038`](#insn-00bab038) → [`00bab230`](#insn-00bab230)
  - `FALL_THROUGH` [`00bab038`](#insn-00bab038) → [`00bab03c`](#insn-00bab03c)
- ブロック [`00bab03c`](#insn-00bab03c) 範囲 `[['00bab03c', '00bab047']]`
  - `CONDITIONAL_JUMP` [`00bab044`](#insn-00bab044) → [`00bab02c`](#insn-00bab02c)
  - `FALL_THROUGH` [`00bab044`](#insn-00bab044) → [`00bab048`](#insn-00bab048)
- ブロック [`00bab048`](#insn-00bab048) 範囲 `[['00bab048', '00bab04b']]`
  - `UNCONDITIONAL_JUMP` [`00bab048`](#insn-00bab048) → [`00bab260`](#insn-00bab260)
- ブロック [`00bab04c`](#insn-00bab04c) 範囲 `[['00bab04c', '00bab067']]`
  - `CONDITIONAL_JUMP` [`00bab064`](#insn-00bab064) → [`00bab2f4`](#insn-00bab2f4)
  - `FALL_THROUGH` [`00bab064`](#insn-00bab064) → [`00bab068`](#insn-00bab068)
- ブロック [`00bab068`](#insn-00bab068) 範囲 `[['00bab068', '00bab06b']]`
  - `FALL_THROUGH` [`00bab068`](#insn-00bab068) → [`00bab06c`](#insn-00bab06c)
- ブロック [`00bab06c`](#insn-00bab06c) 範囲 `[['00bab06c', '00bab07b']]`
  - `CONDITIONAL_JUMP` [`00bab078`](#insn-00bab078) → [`00bab2c4`](#insn-00bab2c4)
  - `FALL_THROUGH` [`00bab078`](#insn-00bab078) → [`00bab07c`](#insn-00bab07c)
- ブロック [`00bab07c`](#insn-00bab07c) 範囲 `[['00bab07c', '00bab087']]`
  - `CONDITIONAL_JUMP` [`00bab084`](#insn-00bab084) → [`00bab06c`](#insn-00bab06c)
  - `FALL_THROUGH` [`00bab084`](#insn-00bab084) → [`00bab088`](#insn-00bab088)
- ブロック [`00bab088`](#insn-00bab088) 範囲 `[['00bab088', '00bab08b']]`
  - `UNCONDITIONAL_JUMP` [`00bab088`](#insn-00bab088) → [`00bab2f4`](#insn-00bab2f4)
- ブロック [`00bab08c`](#insn-00bab08c) 範囲 `[['00bab08c', '00bab093']]`
  - `CONDITIONAL_JUMP` [`00bab090`](#insn-00bab090) → [`00bab0bc`](#insn-00bab0bc)
  - `FALL_THROUGH` [`00bab090`](#insn-00bab090) → [`00bab094`](#insn-00bab094)
- ブロック [`00bab094`](#insn-00bab094) 範囲 `[['00bab094', '00bab0a3']]`
  - `CONDITIONAL_JUMP` [`00bab0a0`](#insn-00bab0a0) → [`00bab0bc`](#insn-00bab0bc)
  - `FALL_THROUGH` [`00bab0a0`](#insn-00bab0a0) → [`00bab0a4`](#insn-00bab0a4)
- ブロック [`00bab0a4`](#insn-00bab0a4) 範囲 `[['00bab0a4', '00bab0b7']]`
  - `FALL_THROUGH` [`00bab0b4`](#insn-00bab0b4) → [`00bab0b8`](#insn-00bab0b8)
- ブロック [`00bab0b8`](#insn-00bab0b8) 範囲 `[['00bab0b8', '00bab0bb']]`
  - `UNCONDITIONAL_JUMP` [`00bab0b8`](#insn-00bab0b8) → [`00bab0d0`](#insn-00bab0d0)
- ブロック [`00bab0bc`](#insn-00bab0bc) 範囲 `[['00bab0bc', '00bab0cb']]`
  - `FALL_THROUGH` [`00bab0c8`](#insn-00bab0c8) → [`00bab0cc`](#insn-00bab0cc)
- ブロック [`00bab0cc`](#insn-00bab0cc) 範囲 `[['00bab0cc', '00bab0cf']]`
  - `FALL_THROUGH` [`00bab0cc`](#insn-00bab0cc) → [`00bab0d0`](#insn-00bab0d0)
- ブロック [`00bab0d0`](#insn-00bab0d0) 範囲 `[['00bab0d0', '00bab0eb']]`
  - `CONDITIONAL_JUMP` [`00bab0e8`](#insn-00bab0e8) → [`00bab360`](#insn-00bab360)
  - `FALL_THROUGH` [`00bab0e8`](#insn-00bab0e8) → [`00bab0ec`](#insn-00bab0ec)
- ブロック [`00bab0ec`](#insn-00bab0ec) 範囲 `[['00bab0ec', '00bab0f3']]`
  - `CONDITIONAL_JUMP` [`00bab0f0`](#insn-00bab0f0) → [`00bab360`](#insn-00bab360)
  - `FALL_THROUGH` [`00bab0f0`](#insn-00bab0f0) → [`00bab0f4`](#insn-00bab0f4)
- ブロック [`00bab0f4`](#insn-00bab0f4) 範囲 `[['00bab0f4', '00bab0fb']]`
  - `CONDITIONAL_JUMP` [`00bab0f8`](#insn-00bab0f8) → [`00bab354`](#insn-00bab354)
  - `FALL_THROUGH` [`00bab0f8`](#insn-00bab0f8) → [`00bab0fc`](#insn-00bab0fc)
- ブロック [`00bab0fc`](#insn-00bab0fc) 範囲 `[['00bab0fc', '00bab107']]`
  - `CONDITIONAL_JUMP` [`00bab104`](#insn-00bab104) → [`00bab368`](#insn-00bab368)
  - `FALL_THROUGH` [`00bab104`](#insn-00bab104) → [`00bab108`](#insn-00bab108)
- ブロック [`00bab108`](#insn-00bab108) 範囲 `[['00bab108', '00bab10b']]`
  - `UNCONDITIONAL_JUMP` [`00bab108`](#insn-00bab108) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00bab10c`](#insn-00bab10c) 範囲 `[['00bab10c', '00bab113']]`
  - `CONDITIONAL_JUMP` [`00bab110`](#insn-00bab110) → [`00bab13c`](#insn-00bab13c)
  - `FALL_THROUGH` [`00bab110`](#insn-00bab110) → [`00bab114`](#insn-00bab114)
- ブロック [`00bab114`](#insn-00bab114) 範囲 `[['00bab114', '00bab123']]`
  - `CONDITIONAL_JUMP` [`00bab120`](#insn-00bab120) → [`00bab13c`](#insn-00bab13c)
  - `FALL_THROUGH` [`00bab120`](#insn-00bab120) → [`00bab124`](#insn-00bab124)
- ブロック [`00bab124`](#insn-00bab124) 範囲 `[['00bab124', '00bab137']]`
  - `FALL_THROUGH` [`00bab134`](#insn-00bab134) → [`00bab138`](#insn-00bab138)
- ブロック [`00bab138`](#insn-00bab138) 範囲 `[['00bab138', '00bab13b']]`
  - `UNCONDITIONAL_JUMP` [`00bab138`](#insn-00bab138) → [`00bab150`](#insn-00bab150)
- ブロック [`00bab13c`](#insn-00bab13c) 範囲 `[['00bab13c', '00bab14f']]`
  - `FALL_THROUGH` [`00bab14c`](#insn-00bab14c) → [`00bab150`](#insn-00bab150)
- ブロック [`00bab150`](#insn-00bab150) 範囲 `[['00bab150', '00bab15b']]`
  - `FALL_THROUGH` [`00bab158`](#insn-00bab158) → [`00bab15c`](#insn-00bab15c)
- ブロック [`00bab15c`](#insn-00bab15c) 範囲 `[['00bab15c', '00bab16b']]`
  - `CONDITIONAL_JUMP` [`00bab168`](#insn-00bab168) → [`00bab190`](#insn-00bab190)
  - `FALL_THROUGH` [`00bab168`](#insn-00bab168) → [`00bab16c`](#insn-00bab16c)
- ブロック [`00bab16c`](#insn-00bab16c) 範囲 `[['00bab16c', '00bab173']]`
  - `CONDITIONAL_JUMP` [`00bab170`](#insn-00bab170) → [`00bab190`](#insn-00bab190)
  - `FALL_THROUGH` [`00bab170`](#insn-00bab170) → [`00bab174`](#insn-00bab174)
- ブロック [`00bab174`](#insn-00bab174) 範囲 `[['00bab174', '00bab17f']]`
  - `CONDITIONAL_JUMP` [`00bab17c`](#insn-00bab17c) → [`00bab190`](#insn-00bab190)
  - `FALL_THROUGH` [`00bab17c`](#insn-00bab17c) → [`00bab180`](#insn-00bab180)
- ブロック [`00bab180`](#insn-00bab180) 範囲 `[['00bab180', '00bab187']]`
  - `FALL_THROUGH` [`00bab184`](#insn-00bab184) → [`00bab188`](#insn-00bab188)
- ブロック [`00bab188`](#insn-00bab188) 範囲 `[['00bab188', '00bab18f']]`
  - `FALL_THROUGH` [`00bab18c`](#insn-00bab18c) → [`00bab190`](#insn-00bab190)
- ブロック [`00bab190`](#insn-00bab190) 範囲 `[['00bab190', '00bab197']]`
  - `CONDITIONAL_JUMP` [`00bab194`](#insn-00bab194) → [`00bab19c`](#insn-00bab19c)
  - `FALL_THROUGH` [`00bab194`](#insn-00bab194) → [`00bab198`](#insn-00bab198)
- ブロック [`00bab198`](#insn-00bab198) 範囲 `[['00bab198', '00bab19b']]`
  - `FALL_THROUGH` [`00bab198`](#insn-00bab198) → [`00bab19c`](#insn-00bab19c)
- ブロック [`00bab19c`](#insn-00bab19c) 範囲 `[['00bab19c', '00bab19f']]`
  - `CONDITIONAL_JUMP` [`00bab19c`](#insn-00bab19c) → [`00bab1a4`](#insn-00bab1a4)
  - `FALL_THROUGH` [`00bab19c`](#insn-00bab19c) → [`00bab1a0`](#insn-00bab1a0)
- ブロック [`00bab1a0`](#insn-00bab1a0) 範囲 `[['00bab1a0', '00bab1a3']]`
  - `FALL_THROUGH` [`00bab1a0`](#insn-00bab1a0) → [`00bab1a4`](#insn-00bab1a4)
- ブロック [`00bab1a4`](#insn-00bab1a4) 範囲 `[['00bab1a4', '00bab1a7']]`
  - `FALL_THROUGH` [`00bab1a4`](#insn-00bab1a4) → [`00bab1a8`](#insn-00bab1a8)
- ブロック [`00bab1a8`](#insn-00bab1a8) 範囲 `[['00bab1a8', '00bab1af']]`
  - `UNCONDITIONAL_JUMP` [`00bab1ac`](#insn-00bab1ac) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00bab1b0`](#insn-00bab1b0) 範囲 `[['00bab1b0', '00bab1b7']]`
  - `CONDITIONAL_JUMP` [`00bab1b4`](#insn-00bab1b4) → [`00bab1e0`](#insn-00bab1e0)
  - `FALL_THROUGH` [`00bab1b4`](#insn-00bab1b4) → [`00bab1b8`](#insn-00bab1b8)
- ブロック [`00bab1b8`](#insn-00bab1b8) 範囲 `[['00bab1b8', '00bab1c7']]`
  - `CONDITIONAL_JUMP` [`00bab1c4`](#insn-00bab1c4) → [`00bab1e0`](#insn-00bab1e0)
  - `FALL_THROUGH` [`00bab1c4`](#insn-00bab1c4) → [`00bab1c8`](#insn-00bab1c8)
- ブロック [`00bab1c8`](#insn-00bab1c8) 範囲 `[['00bab1c8', '00bab1d3']]`
  - `FALL_THROUGH` [`00bab1d0`](#insn-00bab1d0) → [`00bab1d4`](#insn-00bab1d4)
- ブロック [`00bab1d4`](#insn-00bab1d4) 範囲 `[['00bab1d4', '00bab1df']]`
  - `UNCONDITIONAL_JUMP` [`00bab1dc`](#insn-00bab1dc) → [`00bab1f4`](#insn-00bab1f4)
- ブロック [`00bab1e0`](#insn-00bab1e0) 範囲 `[['00bab1e0', '00bab1f3']]`
  - `FALL_THROUGH` [`00bab1f0`](#insn-00bab1f0) → [`00bab1f4`](#insn-00bab1f4)
- ブロック [`00bab1f4`](#insn-00bab1f4) 範囲 `[['00bab1f4', '00bab1f7']]`
  - `FALL_THROUGH` [`00bab1f4`](#insn-00bab1f4) → [`00bab1f8`](#insn-00bab1f8)
- ブロック [`00bab1f8`](#insn-00bab1f8) 範囲 `[['00bab1f8', '00bab20f']]`
  - `CONDITIONAL_JUMP` [`00bab20c`](#insn-00bab20c) → [`00bab390`](#insn-00bab390)
  - `FALL_THROUGH` [`00bab20c`](#insn-00bab20c) → [`00bab210`](#insn-00bab210)
- ブロック [`00bab210`](#insn-00bab210) 範囲 `[['00bab210', '00bab217']]`
  - `CONDITIONAL_JUMP` [`00bab214`](#insn-00bab214) → [`00bab390`](#insn-00bab390)
  - `FALL_THROUGH` [`00bab214`](#insn-00bab214) → [`00bab218`](#insn-00bab218)
- ブロック [`00bab218`](#insn-00bab218) 範囲 `[['00bab218', '00bab21f']]`
  - `CONDITIONAL_JUMP` [`00bab21c`](#insn-00bab21c) → [`00bab384`](#insn-00bab384)
  - `FALL_THROUGH` [`00bab21c`](#insn-00bab21c) → [`00bab220`](#insn-00bab220)
- ブロック [`00bab220`](#insn-00bab220) 範囲 `[['00bab220', '00bab223']]`
  - `FALL_THROUGH` [`00bab220`](#insn-00bab220) → [`00bab224`](#insn-00bab224)
- ブロック [`00bab224`](#insn-00bab224) 範囲 `[['00bab224', '00bab22b']]`
  - `CONDITIONAL_JUMP` [`00bab228`](#insn-00bab228) → [`00bab398`](#insn-00bab398)
  - `FALL_THROUGH` [`00bab228`](#insn-00bab228) → [`00bab22c`](#insn-00bab22c)
- ブロック [`00bab22c`](#insn-00bab22c) 範囲 `[['00bab22c', '00bab22f']]`
  - `UNCONDITIONAL_JUMP` [`00bab22c`](#insn-00bab22c) → [`00bab39c`](#insn-00bab39c)
- ブロック [`00bab230`](#insn-00bab230) 範囲 `[['00bab230', '00bab237']]`
  - `CONDITIONAL_JUMP` [`00bab234`](#insn-00bab234) → [`00bab260`](#insn-00bab260)
  - `FALL_THROUGH` [`00bab234`](#insn-00bab234) → [`00bab238`](#insn-00bab238)
- ブロック [`00bab238`](#insn-00bab238) 範囲 `[['00bab238', '00bab247']]`
  - `CONDITIONAL_JUMP` [`00bab244`](#insn-00bab244) → [`00bab260`](#insn-00bab260)
  - `FALL_THROUGH` [`00bab244`](#insn-00bab244) → [`00bab248`](#insn-00bab248)
- ブロック [`00bab248`](#insn-00bab248) 範囲 `[['00bab248', '00bab25f']]`
  - `UNCONDITIONAL_JUMP` [`00bab25c`](#insn-00bab25c) → [`00bab274`](#insn-00bab274)
- ブロック [`00bab260`](#insn-00bab260) 範囲 `[['00bab260', '00bab273']]`
  - `FALL_THROUGH` [`00bab270`](#insn-00bab270) → [`00bab274`](#insn-00bab274)
- ブロック [`00bab274`](#insn-00bab274) 範囲 `[['00bab274', '00bab28f']]`
  - `CONDITIONAL_JUMP` [`00bab28c`](#insn-00bab28c) → [`00bab2a4`](#insn-00bab2a4)
  - `FALL_THROUGH` [`00bab28c`](#insn-00bab28c) → [`00bab290`](#insn-00bab290)
- ブロック [`00bab290`](#insn-00bab290) 範囲 `[['00bab290', '00bab297']]`
  - `CONDITIONAL_JUMP` [`00bab294`](#insn-00bab294) → [`00bab2a4`](#insn-00bab2a4)
  - `FALL_THROUGH` [`00bab294`](#insn-00bab294) → [`00bab298`](#insn-00bab298)
- ブロック [`00bab298`](#insn-00bab298) 範囲 `[['00bab298', '00bab2a3']]`
  - `FALL_THROUGH` [`00bab2a0`](#insn-00bab2a0) → [`00bab2a4`](#insn-00bab2a4)
- ブロック [`00bab2a4`](#insn-00bab2a4) 範囲 `[['00bab2a4', '00bab2ab']]`
  - `CONDITIONAL_JUMP` [`00bab2a8`](#insn-00bab2a8) → [`00bab2b0`](#insn-00bab2b0)
  - `FALL_THROUGH` [`00bab2a8`](#insn-00bab2a8) → [`00bab2ac`](#insn-00bab2ac)
- ブロック [`00bab2ac`](#insn-00bab2ac) 範囲 `[['00bab2ac', '00bab2af']]`
  - `FALL_THROUGH` [`00bab2ac`](#insn-00bab2ac) → [`00bab2b0`](#insn-00bab2b0)
- ブロック [`00bab2b0`](#insn-00bab2b0) 範囲 `[['00bab2b0', '00bab2b3']]`
  - `CONDITIONAL_JUMP` [`00bab2b0`](#insn-00bab2b0) → [`00bab2b8`](#insn-00bab2b8)
  - `FALL_THROUGH` [`00bab2b0`](#insn-00bab2b0) → [`00bab2b4`](#insn-00bab2b4)
- ブロック [`00bab2b4`](#insn-00bab2b4) 範囲 `[['00bab2b4', '00bab2b7']]`
  - `FALL_THROUGH` [`00bab2b4`](#insn-00bab2b4) → [`00bab2b8`](#insn-00bab2b8)
- ブロック [`00bab2b8`](#insn-00bab2b8) 範囲 `[['00bab2b8', '00bab2c3']]`
  - `UNCONDITIONAL_JUMP` [`00bab2c0`](#insn-00bab2c0) → [`00baafa4`](#insn-00baafa4)
- ブロック [`00bab2c4`](#insn-00bab2c4) 範囲 `[['00bab2c4', '00bab2cb']]`
  - `CONDITIONAL_JUMP` [`00bab2c8`](#insn-00bab2c8) → [`00bab2f4`](#insn-00bab2f4)
  - `FALL_THROUGH` [`00bab2c8`](#insn-00bab2c8) → [`00bab2cc`](#insn-00bab2cc)
- ブロック [`00bab2cc`](#insn-00bab2cc) 範囲 `[['00bab2cc', '00bab2db']]`
  - `CONDITIONAL_JUMP` [`00bab2d8`](#insn-00bab2d8) → [`00bab2f4`](#insn-00bab2f4)
  - `FALL_THROUGH` [`00bab2d8`](#insn-00bab2d8) → [`00bab2dc`](#insn-00bab2dc)
- ブロック [`00bab2dc`](#insn-00bab2dc) 範囲 `[['00bab2dc', '00bab2df']]`
  - `FALL_THROUGH` [`00bab2dc`](#insn-00bab2dc) → [`00bab2e0`](#insn-00bab2e0)
- ブロック [`00bab2e0`](#insn-00bab2e0) 範囲 `[['00bab2e0', '00bab2eb']]`
  - `FALL_THROUGH` [`00bab2e8`](#insn-00bab2e8) → [`00bab2ec`](#insn-00bab2ec)
- ブロック [`00bab2ec`](#insn-00bab2ec) 範囲 `[['00bab2ec', '00bab2f3']]`
  - `UNCONDITIONAL_JUMP` [`00bab2f0`](#insn-00bab2f0) → [`00bab308`](#insn-00bab308)
- ブロック [`00bab2f4`](#insn-00bab2f4) 範囲 `[['00bab2f4', '00bab307']]`
  - `FALL_THROUGH` [`00bab304`](#insn-00bab304) → [`00bab308`](#insn-00bab308)
- ブロック [`00bab308`](#insn-00bab308) 範囲 `[['00bab308', '00bab30b']]`
  - `FALL_THROUGH` [`00bab308`](#insn-00bab308) → [`00bab30c`](#insn-00bab30c)
- ブロック [`00bab30c`](#insn-00bab30c) 範囲 `[['00bab30c', '00bab323']]`
  - `CONDITIONAL_JUMP` [`00bab320`](#insn-00bab320) → [`00bab338`](#insn-00bab338)
  - `FALL_THROUGH` [`00bab320`](#insn-00bab320) → [`00bab324`](#insn-00bab324)
- ブロック [`00bab324`](#insn-00bab324) 範囲 `[['00bab324', '00bab32b']]`
  - `CONDITIONAL_JUMP` [`00bab328`](#insn-00bab328) → [`00bab338`](#insn-00bab338)
  - `FALL_THROUGH` [`00bab328`](#insn-00bab328) → [`00bab32c`](#insn-00bab32c)
- ブロック [`00bab32c`](#insn-00bab32c) 範囲 `[['00bab32c', '00bab337']]`
  - `FALL_THROUGH` [`00bab334`](#insn-00bab334) → [`00bab338`](#insn-00bab338)
- ブロック [`00bab338`](#insn-00bab338) 範囲 `[['00bab338', '00bab33f']]`
  - `CONDITIONAL_JUMP` [`00bab33c`](#insn-00bab33c) → [`00bab344`](#insn-00bab344)
  - `FALL_THROUGH` [`00bab33c`](#insn-00bab33c) → [`00bab340`](#insn-00bab340)
- ブロック [`00bab340`](#insn-00bab340) 範囲 `[['00bab340', '00bab343']]`
  - `FALL_THROUGH` [`00bab340`](#insn-00bab340) → [`00bab344`](#insn-00bab344)
- ブロック [`00bab344`](#insn-00bab344) 範囲 `[['00bab344', '00bab347']]`
  - `CONDITIONAL_JUMP` [`00bab344`](#insn-00bab344) → [`00bab34c`](#insn-00bab34c)
  - `FALL_THROUGH` [`00bab344`](#insn-00bab344) → [`00bab348`](#insn-00bab348)
- ブロック [`00bab348`](#insn-00bab348) 範囲 `[['00bab348', '00bab34b']]`
  - `FALL_THROUGH` [`00bab348`](#insn-00bab348) → [`00bab34c`](#insn-00bab34c)
- ブロック [`00bab34c`](#insn-00bab34c) 範囲 `[['00bab34c', '00bab353']]`
  - `UNCONDITIONAL_JUMP` [`00bab350`](#insn-00bab350) → [`00baafa4`](#insn-00baafa4)
- ブロック [`00bab354`](#insn-00bab354) 範囲 `[['00bab354', '00bab35f']]`
  - `FALL_THROUGH` [`00bab35c`](#insn-00bab35c) → [`00bab360`](#insn-00bab360)
- ブロック [`00bab360`](#insn-00bab360) 範囲 `[['00bab360', '00bab367']]`
  - `CONDITIONAL_JUMP` [`00bab364`](#insn-00bab364) → [`00bab36c`](#insn-00bab36c)
  - `FALL_THROUGH` [`00bab364`](#insn-00bab364) → [`00bab368`](#insn-00bab368)
- ブロック [`00bab368`](#insn-00bab368) 範囲 `[['00bab368', '00bab36b']]`
  - `FALL_THROUGH` [`00bab368`](#insn-00bab368) → [`00bab36c`](#insn-00bab36c)
- ブロック [`00bab36c`](#insn-00bab36c) 範囲 `[['00bab36c', '00bab36f']]`
  - `CONDITIONAL_JUMP` [`00bab36c`](#insn-00bab36c) → [`00bab374`](#insn-00bab374)
  - `FALL_THROUGH` [`00bab36c`](#insn-00bab36c) → [`00bab370`](#insn-00bab370)
- ブロック [`00bab370`](#insn-00bab370) 範囲 `[['00bab370', '00bab373']]`
  - `FALL_THROUGH` [`00bab370`](#insn-00bab370) → [`00bab374`](#insn-00bab374)
- ブロック [`00bab374`](#insn-00bab374) 範囲 `[['00bab374', '00bab37f']]`
  - `FALL_THROUGH` [`00bab37c`](#insn-00bab37c) → [`00bab380`](#insn-00bab380)
- ブロック [`00bab380`](#insn-00bab380) 範囲 `[['00bab380', '00bab383']]`
  - `UNCONDITIONAL_JUMP` [`00bab380`](#insn-00bab380) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00bab384`](#insn-00bab384) 範囲 `[['00bab384', '00bab38f']]`
  - `FALL_THROUGH` [`00bab38c`](#insn-00bab38c) → [`00bab390`](#insn-00bab390)
- ブロック [`00bab390`](#insn-00bab390) 範囲 `[['00bab390', '00bab397']]`
  - `CONDITIONAL_JUMP` [`00bab394`](#insn-00bab394) → [`00bab39c`](#insn-00bab39c)
  - `FALL_THROUGH` [`00bab394`](#insn-00bab394) → [`00bab398`](#insn-00bab398)
- ブロック [`00bab398`](#insn-00bab398) 範囲 `[['00bab398', '00bab39b']]`
  - `FALL_THROUGH` [`00bab398`](#insn-00bab398) → [`00bab39c`](#insn-00bab39c)
- ブロック [`00bab39c`](#insn-00bab39c) 範囲 `[['00bab39c', '00bab39f']]`
  - `CONDITIONAL_JUMP` [`00bab39c`](#insn-00bab39c) → [`00bab3a4`](#insn-00bab3a4)
  - `FALL_THROUGH` [`00bab39c`](#insn-00bab39c) → [`00bab3a0`](#insn-00bab3a0)
- ブロック [`00bab3a0`](#insn-00bab3a0) 範囲 `[['00bab3a0', '00bab3a3']]`
  - `FALL_THROUGH` [`00bab3a0`](#insn-00bab3a0) → [`00bab3a4`](#insn-00bab3a4)
- ブロック [`00bab3a4`](#insn-00bab3a4) 範囲 `[['00bab3a4', '00bab3b3']]`
  - `UNCONDITIONAL_JUMP` [`00bab3b0`](#insn-00bab3b0) → [`00baafa8`](#insn-00baafa8)
- ブロック [`00bab3b4`](#insn-00bab3b4) 範囲 `[['00bab3b4', '00bab3b7']]`
  - `FALL_THROUGH` [`00bab3b4`](#insn-00bab3b4) → [`00bab3b8`](#insn-00bab3b8)
- ブロック [`00bab3b8`](#insn-00bab3b8) 範囲 `[['00bab3b8', '00bab3cf']]`
  - `CONDITIONAL_JUMP` [`00bab3cc`](#insn-00bab3cc) → [`00bab3d8`](#insn-00bab3d8)
  - `FALL_THROUGH` [`00bab3cc`](#insn-00bab3cc) → [`00bab3d0`](#insn-00bab3d0)
- ブロック [`00bab3d0`](#insn-00bab3d0) 範囲 `[['00bab3d0', '00bab3d7']]`
  - `FALL_THROUGH` [`00bab3d4`](#insn-00bab3d4) → [`00bab3d8`](#insn-00bab3d8)
- ブロック [`00bab3d8`](#insn-00bab3d8) 範囲 `[['00bab3d8', '00bab3e3']]`
  - `FALL_THROUGH` [`00bab3e0`](#insn-00bab3e0) → [`00bab3e4`](#insn-00bab3e4)
- ブロック [`00bab3e4`](#insn-00bab3e4) 範囲 `[['00bab3e4', '00bab3fb']]`
  - `UNCONDITIONAL_JUMP` [`00bab3f8`](#insn-00bab3f8) → [`00baafa4`](#insn-00baafa4)
- ブロック [`00bab3fc`](#insn-00bab3fc) 範囲 `[['00bab3fc', '00bab3ff']]`

## 命令位置別の参照

- [`00baaae8`](#insn-00baaae8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaaec`](#insn-00baaaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaaf0`](#insn-00baaaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab00`](#insn-00baab00) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab0c`](#insn-00baab0c) → [`00baad84`](#insn-00baad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00baab2c::default` · 推定型 `None`
- [`00baab1c`](#insn-00baab1c) → `0030e1b3`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::switchdataD_0030e1b3` · 推定型 `byte`
- [`00baab2c`](#insn-00baab2c) → [`00baab30`](#insn-00baab30) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_0` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baad8c`](#insn-00baad8c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_1` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baad0c`](#insn-00baad0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_2` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baad54`](#insn-00baad54) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_3` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baabf0`](#insn-00baabf0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_4` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baada4`](#insn-00baada4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_5` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baadbc`](#insn-00baadbc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_6` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baad6c`](#insn-00baad6c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_7` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baadd4`](#insn-00baadd4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_8` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baac38`](#insn-00baac38) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_9` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baadec`](#insn-00baadec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_a` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baab78`](#insn-00baab78) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_b` · 推定型 `None`
- [`00baab2c`](#insn-00baab2c) → [`00baac90`](#insn-00baac90) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00baab2c::caseD_c` · 推定型 `None`
- [`00baab30`](#insn-00baab30) → [`00baab38`](#insn-00baab38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab34`](#insn-00baab34) → [`00baad94`](#insn-00baad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab50`](#insn-00baab50) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab64`](#insn-00baab64) → [`00baaf14`](#insn-00baaf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab70`](#insn-00baab70) → [`00baab58`](#insn-00baab58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab74`](#insn-00baab74) → [`00baaf44`](#insn-00baaf44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab78`](#insn-00baab78) → [`00baab84`](#insn-00baab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab80`](#insn-00baab80) → [`00baabd4`](#insn-00baabd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaba0`](#insn-00baaba0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaba4`](#insn-00baaba4) → [`00c581b0`](../00c58/00c581b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581b0` · 推定シンボル `None` · 推定型 `None`
- [`00baaba8`](#insn-00baaba8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabb4`](#insn-00baabb4) → [`00baabd4`](#insn-00baabd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabbc`](#insn-00baabbc) → [`00baabd4`](#insn-00baabd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabc8`](#insn-00baabc8) → [`00baabd4`](#insn-00baabd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabd8`](#insn-00baabd8) → [`00baabe0`](#insn-00baabe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabe0`](#insn-00baabe0) → [`00baabe8`](#insn-00baabe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabec`](#insn-00baabec) → [`00baad04`](#insn-00baad04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf0`](#insn-00baabf0) → [`00baabf8`](#insn-00baabf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf4`](#insn-00baabf4) → [`00baad94`](#insn-00baad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac10`](#insn-00baac10) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac24`](#insn-00baac24) → [`00baaf14`](#insn-00baaf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac30`](#insn-00baac30) → [`00baac18`](#insn-00baac18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac34`](#insn-00baac34) → [`00baaf44`](#insn-00baaf44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac38`](#insn-00baac38) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac3c`](#insn-00baac3c) → [`00baac44`](#insn-00baac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac40`](#insn-00baac40) → [`00baac68`](#insn-00baac68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac64`](#insn-00baac64) → [`00c5bdb0`](../00c5b/00c5bdb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdb0` · 推定シンボル `None` · 推定型 `None`
- [`00baac7c`](#insn-00baac7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac80`](#insn-00baac80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac8c`](#insn-00baac8c) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac90`](#insn-00baac90) → [`00baac9c`](#insn-00baac9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac98`](#insn-00baac98) → [`00baacec`](#insn-00baacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb8`](#insn-00baacb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacbc`](#insn-00baacbc) → [`00c581c0`](../00c58/00c581c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581c0` · 推定シンボル `None` · 推定型 `None`
- [`00baacc0`](#insn-00baacc0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaccc`](#insn-00baaccc) → [`00baacec`](#insn-00baacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd4`](#insn-00baacd4) → [`00baacec`](#insn-00baacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baace0`](#insn-00baace0) → [`00baacec`](#insn-00baacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacf0`](#insn-00baacf0) → [`00baacf8`](#insn-00baacf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacf8`](#insn-00baacf8) → [`00baad00`](#insn-00baad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad08`](#insn-00baad08) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad0c`](#insn-00baad0c) → [`00baad14`](#insn-00baad14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad10`](#insn-00baad10) → [`00baad94`](#insn-00baad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad2c`](#insn-00baad2c) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad40`](#insn-00baad40) → [`00baaf14`](#insn-00baaf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad4c`](#insn-00baad4c) → [`00baad34`](#insn-00baad34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad50`](#insn-00baad50) → [`00baaf44`](#insn-00baaf44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad54`](#insn-00baad54) → [`00baae54`](#insn-00baae54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad58`](#insn-00baad58) → [`00baae54`](#insn-00baae54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad64`](#insn-00baad64) → [`00bab368`](#insn-00bab368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad68`](#insn-00baad68) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad6c`](#insn-00baad6c) → [`00baae94`](#insn-00baae94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad70`](#insn-00baad70) → [`00baae94`](#insn-00baae94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad7c`](#insn-00baad7c) → [`00bab198`](#insn-00bab198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad80`](#insn-00baad80) → [`00bab19c`](#insn-00bab19c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad88`](#insn-00baad88) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad8c`](#insn-00baad8c) → [`00baaed4`](#insn-00baaed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad90`](#insn-00baad90) → [`00baaed4`](#insn-00baaed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad9c`](#insn-00baad9c) → [`00baaf90`](#insn-00baaf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada0`](#insn-00baada0) → [`00baaf94`](#insn-00baaf94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada4`](#insn-00baada4) → [`00baafcc`](#insn-00baafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baada8`](#insn-00baada8) → [`00baafcc`](#insn-00baafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadb4`](#insn-00baadb4) → [`00bab398`](#insn-00bab398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadb8`](#insn-00baadb8) → [`00bab39c`](#insn-00bab39c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadbc`](#insn-00baadbc) → [`00bab00c`](#insn-00bab00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadc0`](#insn-00baadc0) → [`00bab00c`](#insn-00bab00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadcc`](#insn-00baadcc) → [`00bab2ac`](#insn-00bab2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd0`](#insn-00baadd0) → [`00bab2b0`](#insn-00bab2b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd4`](#insn-00baadd4) → [`00bab04c`](#insn-00bab04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd8`](#insn-00baadd8) → [`00bab04c`](#insn-00bab04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade4`](#insn-00baade4) → [`00bab340`](#insn-00bab340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade8`](#insn-00baade8) → [`00bab344`](#insn-00bab344) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadec`](#insn-00baadec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadf0`](#insn-00baadf0) → [`00baadf8`](#insn-00baadf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadf4`](#insn-00baadf4) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae1c`](#insn-00baae1c) → [`00c5bdc0`](../00c5b/00c5bdc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bdc0` · 推定シンボル `None` · 推定型 `None`
- [`00baae20`](#insn-00baae20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae24`](#insn-00baae24) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae28`](#insn-00baae28) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae30`](#insn-00baae30) → [`00bab3b4`](#insn-00bab3b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae44`](#insn-00baae44) → [`00bab3b8`](#insn-00bab3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae4c`](#insn-00baae4c) → [`00baae38`](#insn-00baae38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae50`](#insn-00baae50) → [`00bab3b8`](#insn-00bab3b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae6c`](#insn-00baae6c) → [`00bab0bc`](#insn-00bab0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae80`](#insn-00baae80) → [`00bab08c`](#insn-00bab08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae8c`](#insn-00baae8c) → [`00baae74`](#insn-00baae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae90`](#insn-00baae90) → [`00bab0bc`](#insn-00bab0bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaeac`](#insn-00baaeac) → [`00bab13c`](#insn-00bab13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaec0`](#insn-00baaec0) → [`00bab10c`](#insn-00bab10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaecc`](#insn-00baaecc) → [`00baaeb4`](#insn-00baaeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaed0`](#insn-00baaed0) → [`00bab13c`](#insn-00bab13c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaeec`](#insn-00baaeec) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf00`](#insn-00baaf00) → [`00baaf14`](#insn-00baaf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf0c`](#insn-00baaf0c) → [`00baaef4`](#insn-00baaef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf10`](#insn-00baaf10) → [`00baaf44`](#insn-00baaf44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf18`](#insn-00baaf18) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf28`](#insn-00baaf28) → [`00baaf44`](#insn-00baaf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf30`](#insn-00baaf30) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baaf3c`](#insn-00baaf3c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf40`](#insn-00baaf40) → [`00baaf58`](#insn-00baaf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf48`](#insn-00baaf48) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00baaf4c`](#insn-00baaf4c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf58`](#insn-00baaf58) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00baaf60`](#insn-00baaf60) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00baaf64`](#insn-00baaf64) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf70`](#insn-00baaf70) → [`00baaf88`](#insn-00baaf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf78`](#insn-00baaf78) → [`00baaf88`](#insn-00baaf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf8c`](#insn-00baaf8c) → [`00baaf94`](#insn-00baaf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaf94`](#insn-00baaf94) → [`00baaf9c`](#insn-00baaf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafac`](#insn-00baafac) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb4`](#insn-00baafb4) → [`00bab3fc`](#insn-00bab3fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafb8`](#insn-00baafb8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafbc`](#insn-00baafbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafc0`](#insn-00baafc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baafe4`](#insn-00baafe4) → [`00bab1e0`](#insn-00bab1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaff8`](#insn-00baaff8) → [`00bab1b0`](#insn-00bab1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab004`](#insn-00bab004) → [`00baafec`](#insn-00baafec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab008`](#insn-00bab008) → [`00bab1e0`](#insn-00bab1e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab024`](#insn-00bab024) → [`00bab260`](#insn-00bab260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab038`](#insn-00bab038) → [`00bab230`](#insn-00bab230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab044`](#insn-00bab044) → [`00bab02c`](#insn-00bab02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab048`](#insn-00bab048) → [`00bab260`](#insn-00bab260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab064`](#insn-00bab064) → [`00bab2f4`](#insn-00bab2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab078`](#insn-00bab078) → [`00bab2c4`](#insn-00bab2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab084`](#insn-00bab084) → [`00bab06c`](#insn-00bab06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab088`](#insn-00bab088) → [`00bab2f4`](#insn-00bab2f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab090`](#insn-00bab090) → [`00bab0bc`](#insn-00bab0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a0`](#insn-00bab0a0) → [`00bab0bc`](#insn-00bab0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0a8`](#insn-00bab0a8) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab0b4`](#insn-00bab0b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0b8`](#insn-00bab0b8) → [`00bab0d0`](#insn-00bab0d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0c0`](#insn-00bab0c0) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab0c4`](#insn-00bab0c4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0d0`](#insn-00bab0d0) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab0d8`](#insn-00bab0d8) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00bab0dc`](#insn-00bab0dc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0e8`](#insn-00bab0e8) → [`00bab360`](#insn-00bab360) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f0`](#insn-00bab0f0) → [`00bab360`](#insn-00bab360) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab0f8`](#insn-00bab0f8) → [`00bab354`](#insn-00bab354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab104`](#insn-00bab104) → [`00bab368`](#insn-00bab368) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab108`](#insn-00bab108) → [`00bab36c`](#insn-00bab36c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab110`](#insn-00bab110) → [`00bab13c`](#insn-00bab13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab120`](#insn-00bab120) → [`00bab13c`](#insn-00bab13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab128`](#insn-00bab128) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab134`](#insn-00bab134) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab138`](#insn-00bab138) → [`00bab150`](#insn-00bab150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab140`](#insn-00bab140) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab144`](#insn-00bab144) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab150`](#insn-00bab150) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab158`](#insn-00bab158) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00bab15c`](#insn-00bab15c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab168`](#insn-00bab168) → [`00bab190`](#insn-00bab190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab170`](#insn-00bab170) → [`00bab190`](#insn-00bab190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab17c`](#insn-00bab17c) → [`00bab190`](#insn-00bab190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab194`](#insn-00bab194) → [`00bab19c`](#insn-00bab19c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab19c`](#insn-00bab19c) → [`00bab1a4`](#insn-00bab1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1ac`](#insn-00bab1ac) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1b4`](#insn-00bab1b4) → [`00bab1e0`](#insn-00bab1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1c4`](#insn-00bab1c4) → [`00bab1e0`](#insn-00bab1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1cc`](#insn-00bab1cc) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab1d8`](#insn-00bab1d8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1dc`](#insn-00bab1dc) → [`00bab1f4`](#insn-00bab1f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1e4`](#insn-00bab1e4) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab1e8`](#insn-00bab1e8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab1f4`](#insn-00bab1f4) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab1fc`](#insn-00bab1fc) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00bab200`](#insn-00bab200) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab20c`](#insn-00bab20c) → [`00bab390`](#insn-00bab390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab214`](#insn-00bab214) → [`00bab390`](#insn-00bab390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab21c`](#insn-00bab21c) → [`00bab384`](#insn-00bab384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab228`](#insn-00bab228) → [`00bab398`](#insn-00bab398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab22c`](#insn-00bab22c) → [`00bab39c`](#insn-00bab39c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab234`](#insn-00bab234) → [`00bab260`](#insn-00bab260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab244`](#insn-00bab244) → [`00bab260`](#insn-00bab260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab24c`](#insn-00bab24c) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab258`](#insn-00bab258) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab25c`](#insn-00bab25c) → [`00bab274`](#insn-00bab274) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab264`](#insn-00bab264) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab268`](#insn-00bab268) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab274`](#insn-00bab274) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab27c`](#insn-00bab27c) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00bab280`](#insn-00bab280) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab28c`](#insn-00bab28c) → [`00bab2a4`](#insn-00bab2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab294`](#insn-00bab294) → [`00bab2a4`](#insn-00bab2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2a8`](#insn-00bab2a8) → [`00bab2b0`](#insn-00bab2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2b0`](#insn-00bab2b0) → [`00bab2b8`](#insn-00bab2b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2c0`](#insn-00bab2c0) → [`00baafa4`](#insn-00baafa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2c8`](#insn-00bab2c8) → [`00bab2f4`](#insn-00bab2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2d8`](#insn-00bab2d8) → [`00bab2f4`](#insn-00bab2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2e0`](#insn-00bab2e0) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab2ec`](#insn-00bab2ec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f0`](#insn-00bab2f0) → [`00bab308`](#insn-00bab308) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab2f8`](#insn-00bab2f8) → `00c9b430`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab2fc`](#insn-00bab2fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab308`](#insn-00bab308) → `01125de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN11flatbuffers13ClassicLocale9instance_E` · 推定型 `undefined8`
- [`00bab310`](#insn-00bab310) → [`00c5cd50`](../00c5c/00c5cd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cd50` · 推定シンボル `None` · 推定型 `None`
- [`00bab314`](#insn-00bab314) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab320`](#insn-00bab320) → [`00bab338`](#insn-00bab338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab328`](#insn-00bab328) → [`00bab338`](#insn-00bab338) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab33c`](#insn-00bab33c) → [`00bab344`](#insn-00bab344) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab344`](#insn-00bab344) → [`00bab34c`](#insn-00bab34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab350`](#insn-00bab350) → [`00baafa4`](#insn-00baafa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab364`](#insn-00bab364) → [`00bab36c`](#insn-00bab36c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab36c`](#insn-00bab36c) → [`00bab374`](#insn-00bab374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab380`](#insn-00bab380) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab394`](#insn-00bab394) → [`00bab39c`](#insn-00bab39c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab39c`](#insn-00bab39c) → [`00bab3a4`](#insn-00bab3a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3b0`](#insn-00bab3b0) → [`00baafa8`](#insn-00baafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3cc`](#insn-00bab3cc) → [`00bab3d8`](#insn-00bab3d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3d4`](#insn-00bab3d4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3ec`](#insn-00bab3ec) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f0`](#insn-00bab3f0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3f8`](#insn-00bab3f8) → [`00baafa4`](#insn-00baafa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab3fc`](#insn-00bab3fc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaae8`](#insn-00baaae8)

~~~json
{
  "source": "00baaae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaaec`](#insn-00baaaec)

~~~json
{
  "source": "00baaaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaaf0`](#insn-00baaaf0)

~~~json
{
  "source": "00baaaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab00`](#insn-00baab00)

~~~json
{
  "source": "00baab00",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab0c`](#insn-00baab0c)

~~~json
{
  "source": "00baab0c",
  "target": "00baad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab1c`](#insn-00baab1c)

~~~json
{
  "source": "00baab1c",
  "target": "0030e1b3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e1b3",
  "offset": 0,
  "size": 1,
  "datatype": "byte",
  "bytes": "00",
  "capture_start": "0030e1b3",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baad8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baad0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baad54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baabf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baada4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baadbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baad6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baadd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baadec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab2c`](#insn-00baab2c)

~~~json
{
  "source": "00baab2c",
  "target": "00baac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab30`](#insn-00baab30)

~~~json
{
  "source": "00baab30",
  "target": "00baab38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab34`](#insn-00baab34)

~~~json
{
  "source": "00baab34",
  "target": "00baad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab50`](#insn-00baab50)

~~~json
{
  "source": "00baab50",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab64`](#insn-00baab64)

~~~json
{
  "source": "00baab64",
  "target": "00baaf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab70`](#insn-00baab70)

~~~json
{
  "source": "00baab70",
  "target": "00baab58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab74`](#insn-00baab74)

~~~json
{
  "source": "00baab74",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab78`](#insn-00baab78)

~~~json
{
  "source": "00baab78",
  "target": "00baab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab80`](#insn-00baab80)

~~~json
{
  "source": "00baab80",
  "target": "00baabd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaba0`](#insn-00baaba0)

~~~json
{
  "source": "00baaba0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaba4`](#insn-00baaba4)

~~~json
{
  "source": "00baaba4",
  "target": "00c581b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaba8`](#insn-00baaba8)

~~~json
{
  "source": "00baaba8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabb4`](#insn-00baabb4)

~~~json
{
  "source": "00baabb4",
  "target": "00baabd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabbc`](#insn-00baabbc)

~~~json
{
  "source": "00baabbc",
  "target": "00baabd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabc8`](#insn-00baabc8)

~~~json
{
  "source": "00baabc8",
  "target": "00baabd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabd8`](#insn-00baabd8)

~~~json
{
  "source": "00baabd8",
  "target": "00baabe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabe0`](#insn-00baabe0)

~~~json
{
  "source": "00baabe0",
  "target": "00baabe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabec`](#insn-00baabec)

~~~json
{
  "source": "00baabec",
  "target": "00baad04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf0`](#insn-00baabf0)

~~~json
{
  "source": "00baabf0",
  "target": "00baabf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf4`](#insn-00baabf4)

~~~json
{
  "source": "00baabf4",
  "target": "00baad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac10`](#insn-00baac10)

~~~json
{
  "source": "00baac10",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac24`](#insn-00baac24)

~~~json
{
  "source": "00baac24",
  "target": "00baaf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac30`](#insn-00baac30)

~~~json
{
  "source": "00baac30",
  "target": "00baac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac34`](#insn-00baac34)

~~~json
{
  "source": "00baac34",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac38`](#insn-00baac38)

~~~json
{
  "source": "00baac38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac3c`](#insn-00baac3c)

~~~json
{
  "source": "00baac3c",
  "target": "00baac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac40`](#insn-00baac40)

~~~json
{
  "source": "00baac40",
  "target": "00baac68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac64`](#insn-00baac64)

~~~json
{
  "source": "00baac64",
  "target": "00c5bdb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac7c`](#insn-00baac7c)

~~~json
{
  "source": "00baac7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac80`](#insn-00baac80)

~~~json
{
  "source": "00baac80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac8c`](#insn-00baac8c)

~~~json
{
  "source": "00baac8c",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac90`](#insn-00baac90)

~~~json
{
  "source": "00baac90",
  "target": "00baac9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac98`](#insn-00baac98)

~~~json
{
  "source": "00baac98",
  "target": "00baacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb8`](#insn-00baacb8)

~~~json
{
  "source": "00baacb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacbc`](#insn-00baacbc)

~~~json
{
  "source": "00baacbc",
  "target": "00c581c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacc0`](#insn-00baacc0)

~~~json
{
  "source": "00baacc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaccc`](#insn-00baaccc)

~~~json
{
  "source": "00baaccc",
  "target": "00baacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd4`](#insn-00baacd4)

~~~json
{
  "source": "00baacd4",
  "target": "00baacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baace0`](#insn-00baace0)

~~~json
{
  "source": "00baace0",
  "target": "00baacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacf0`](#insn-00baacf0)

~~~json
{
  "source": "00baacf0",
  "target": "00baacf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacf8`](#insn-00baacf8)

~~~json
{
  "source": "00baacf8",
  "target": "00baad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad08`](#insn-00baad08)

~~~json
{
  "source": "00baad08",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad0c`](#insn-00baad0c)

~~~json
{
  "source": "00baad0c",
  "target": "00baad14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad10`](#insn-00baad10)

~~~json
{
  "source": "00baad10",
  "target": "00baad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad2c`](#insn-00baad2c)

~~~json
{
  "source": "00baad2c",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad40`](#insn-00baad40)

~~~json
{
  "source": "00baad40",
  "target": "00baaf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad4c`](#insn-00baad4c)

~~~json
{
  "source": "00baad4c",
  "target": "00baad34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad50`](#insn-00baad50)

~~~json
{
  "source": "00baad50",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad54`](#insn-00baad54)

~~~json
{
  "source": "00baad54",
  "target": "00baae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad58`](#insn-00baad58)

~~~json
{
  "source": "00baad58",
  "target": "00baae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad64`](#insn-00baad64)

~~~json
{
  "source": "00baad64",
  "target": "00bab368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad68`](#insn-00baad68)

~~~json
{
  "source": "00baad68",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad6c`](#insn-00baad6c)

~~~json
{
  "source": "00baad6c",
  "target": "00baae94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad70`](#insn-00baad70)

~~~json
{
  "source": "00baad70",
  "target": "00baae94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad7c`](#insn-00baad7c)

~~~json
{
  "source": "00baad7c",
  "target": "00bab198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad80`](#insn-00baad80)

~~~json
{
  "source": "00baad80",
  "target": "00bab19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad88`](#insn-00baad88)

~~~json
{
  "source": "00baad88",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad8c`](#insn-00baad8c)

~~~json
{
  "source": "00baad8c",
  "target": "00baaed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad90`](#insn-00baad90)

~~~json
{
  "source": "00baad90",
  "target": "00baaed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad9c`](#insn-00baad9c)

~~~json
{
  "source": "00baad9c",
  "target": "00baaf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada0`](#insn-00baada0)

~~~json
{
  "source": "00baada0",
  "target": "00baaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada4`](#insn-00baada4)

~~~json
{
  "source": "00baada4",
  "target": "00baafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baada8`](#insn-00baada8)

~~~json
{
  "source": "00baada8",
  "target": "00baafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadb4`](#insn-00baadb4)

~~~json
{
  "source": "00baadb4",
  "target": "00bab398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadb8`](#insn-00baadb8)

~~~json
{
  "source": "00baadb8",
  "target": "00bab39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadbc`](#insn-00baadbc)

~~~json
{
  "source": "00baadbc",
  "target": "00bab00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadc0`](#insn-00baadc0)

~~~json
{
  "source": "00baadc0",
  "target": "00bab00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadcc`](#insn-00baadcc)

~~~json
{
  "source": "00baadcc",
  "target": "00bab2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd0`](#insn-00baadd0)

~~~json
{
  "source": "00baadd0",
  "target": "00bab2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd4`](#insn-00baadd4)

~~~json
{
  "source": "00baadd4",
  "target": "00bab04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd8`](#insn-00baadd8)

~~~json
{
  "source": "00baadd8",
  "target": "00bab04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade4`](#insn-00baade4)

~~~json
{
  "source": "00baade4",
  "target": "00bab340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade8`](#insn-00baade8)

~~~json
{
  "source": "00baade8",
  "target": "00bab344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadec`](#insn-00baadec)

~~~json
{
  "source": "00baadec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadf0`](#insn-00baadf0)

~~~json
{
  "source": "00baadf0",
  "target": "00baadf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadf4`](#insn-00baadf4)

~~~json
{
  "source": "00baadf4",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae1c`](#insn-00baae1c)

~~~json
{
  "source": "00baae1c",
  "target": "00c5bdc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae20`](#insn-00baae20)

~~~json
{
  "source": "00baae20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae24`](#insn-00baae24)

~~~json
{
  "source": "00baae24",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae28`](#insn-00baae28)

~~~json
{
  "source": "00baae28",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae30`](#insn-00baae30)

~~~json
{
  "source": "00baae30",
  "target": "00bab3b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae44`](#insn-00baae44)

~~~json
{
  "source": "00baae44",
  "target": "00bab3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae4c`](#insn-00baae4c)

~~~json
{
  "source": "00baae4c",
  "target": "00baae38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae50`](#insn-00baae50)

~~~json
{
  "source": "00baae50",
  "target": "00bab3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae6c`](#insn-00baae6c)

~~~json
{
  "source": "00baae6c",
  "target": "00bab0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae80`](#insn-00baae80)

~~~json
{
  "source": "00baae80",
  "target": "00bab08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae8c`](#insn-00baae8c)

~~~json
{
  "source": "00baae8c",
  "target": "00baae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae90`](#insn-00baae90)

~~~json
{
  "source": "00baae90",
  "target": "00bab0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaeac`](#insn-00baaeac)

~~~json
{
  "source": "00baaeac",
  "target": "00bab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaec0`](#insn-00baaec0)

~~~json
{
  "source": "00baaec0",
  "target": "00bab10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaecc`](#insn-00baaecc)

~~~json
{
  "source": "00baaecc",
  "target": "00baaeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaed0`](#insn-00baaed0)

~~~json
{
  "source": "00baaed0",
  "target": "00bab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaeec`](#insn-00baaeec)

~~~json
{
  "source": "00baaeec",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf00`](#insn-00baaf00)

~~~json
{
  "source": "00baaf00",
  "target": "00baaf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf0c`](#insn-00baaf0c)

~~~json
{
  "source": "00baaf0c",
  "target": "00baaef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf10`](#insn-00baaf10)

~~~json
{
  "source": "00baaf10",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf18`](#insn-00baaf18)

~~~json
{
  "source": "00baaf18",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf28`](#insn-00baaf28)

~~~json
{
  "source": "00baaf28",
  "target": "00baaf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf30`](#insn-00baaf30)

~~~json
{
  "source": "00baaf30",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baaf3c`](#insn-00baaf3c)

~~~json
{
  "source": "00baaf3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf40`](#insn-00baaf40)

~~~json
{
  "source": "00baaf40",
  "target": "00baaf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf48`](#insn-00baaf48)

~~~json
{
  "source": "00baaf48",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00baaf4c`](#insn-00baaf4c)

~~~json
{
  "source": "00baaf4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf58`](#insn-00baaf58)

~~~json
{
  "source": "00baaf58",
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00baaf60`](#insn-00baaf60)

~~~json
{
  "source": "00baaf60",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaf64`](#insn-00baaf64)

~~~json
{
  "source": "00baaf64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf70`](#insn-00baaf70)

~~~json
{
  "source": "00baaf70",
  "target": "00baaf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf78`](#insn-00baaf78)

~~~json
{
  "source": "00baaf78",
  "target": "00baaf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf8c`](#insn-00baaf8c)

~~~json
{
  "source": "00baaf8c",
  "target": "00baaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaf94`](#insn-00baaf94)

~~~json
{
  "source": "00baaf94",
  "target": "00baaf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafac`](#insn-00baafac)

~~~json
{
  "source": "00baafac",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb4`](#insn-00baafb4)

~~~json
{
  "source": "00baafb4",
  "target": "00bab3fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafb8`](#insn-00baafb8)

~~~json
{
  "source": "00baafb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafbc`](#insn-00baafbc)

~~~json
{
  "source": "00baafbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafc0`](#insn-00baafc0)

~~~json
{
  "source": "00baafc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baafe4`](#insn-00baafe4)

~~~json
{
  "source": "00baafe4",
  "target": "00bab1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaff8`](#insn-00baaff8)

~~~json
{
  "source": "00baaff8",
  "target": "00bab1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab004`](#insn-00bab004)

~~~json
{
  "source": "00bab004",
  "target": "00baafec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab008`](#insn-00bab008)

~~~json
{
  "source": "00bab008",
  "target": "00bab1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab024`](#insn-00bab024)

~~~json
{
  "source": "00bab024",
  "target": "00bab260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab038`](#insn-00bab038)

~~~json
{
  "source": "00bab038",
  "target": "00bab230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab044`](#insn-00bab044)

~~~json
{
  "source": "00bab044",
  "target": "00bab02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab048`](#insn-00bab048)

~~~json
{
  "source": "00bab048",
  "target": "00bab260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab064`](#insn-00bab064)

~~~json
{
  "source": "00bab064",
  "target": "00bab2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab078`](#insn-00bab078)

~~~json
{
  "source": "00bab078",
  "target": "00bab2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab084`](#insn-00bab084)

~~~json
{
  "source": "00bab084",
  "target": "00bab06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab088`](#insn-00bab088)

~~~json
{
  "source": "00bab088",
  "target": "00bab2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab090`](#insn-00bab090)

~~~json
{
  "source": "00bab090",
  "target": "00bab0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0a0`](#insn-00bab0a0)

~~~json
{
  "source": "00bab0a0",
  "target": "00bab0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0a8`](#insn-00bab0a8)

~~~json
{
  "source": "00bab0a8",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab0b4`](#insn-00bab0b4)

~~~json
{
  "source": "00bab0b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0b8`](#insn-00bab0b8)

~~~json
{
  "source": "00bab0b8",
  "target": "00bab0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0c0`](#insn-00bab0c0)

~~~json
{
  "source": "00bab0c0",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab0c4`](#insn-00bab0c4)

~~~json
{
  "source": "00bab0c4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0d0`](#insn-00bab0d0)

~~~json
{
  "source": "00bab0d0",
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab0d8`](#insn-00bab0d8)

~~~json
{
  "source": "00bab0d8",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab0dc`](#insn-00bab0dc)

~~~json
{
  "source": "00bab0dc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0e8`](#insn-00bab0e8)

~~~json
{
  "source": "00bab0e8",
  "target": "00bab360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f0`](#insn-00bab0f0)

~~~json
{
  "source": "00bab0f0",
  "target": "00bab360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab0f8`](#insn-00bab0f8)

~~~json
{
  "source": "00bab0f8",
  "target": "00bab354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab104`](#insn-00bab104)

~~~json
{
  "source": "00bab104",
  "target": "00bab368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab108`](#insn-00bab108)

~~~json
{
  "source": "00bab108",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab110`](#insn-00bab110)

~~~json
{
  "source": "00bab110",
  "target": "00bab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab120`](#insn-00bab120)

~~~json
{
  "source": "00bab120",
  "target": "00bab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab128`](#insn-00bab128)

~~~json
{
  "source": "00bab128",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab134`](#insn-00bab134)

~~~json
{
  "source": "00bab134",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab138`](#insn-00bab138)

~~~json
{
  "source": "00bab138",
  "target": "00bab150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab140`](#insn-00bab140)

~~~json
{
  "source": "00bab140",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
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
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab158`](#insn-00bab158)

~~~json
{
  "source": "00bab158",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab15c`](#insn-00bab15c)

~~~json
{
  "source": "00bab15c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab168`](#insn-00bab168)

~~~json
{
  "source": "00bab168",
  "target": "00bab190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab170`](#insn-00bab170)

~~~json
{
  "source": "00bab170",
  "target": "00bab190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab17c`](#insn-00bab17c)

~~~json
{
  "source": "00bab17c",
  "target": "00bab190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab194`](#insn-00bab194)

~~~json
{
  "source": "00bab194",
  "target": "00bab19c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab19c`](#insn-00bab19c)

~~~json
{
  "source": "00bab19c",
  "target": "00bab1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1ac`](#insn-00bab1ac)

~~~json
{
  "source": "00bab1ac",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1b4`](#insn-00bab1b4)

~~~json
{
  "source": "00bab1b4",
  "target": "00bab1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1c4`](#insn-00bab1c4)

~~~json
{
  "source": "00bab1c4",
  "target": "00bab1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1cc`](#insn-00bab1cc)

~~~json
{
  "source": "00bab1cc",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab1d8`](#insn-00bab1d8)

~~~json
{
  "source": "00bab1d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1dc`](#insn-00bab1dc)

~~~json
{
  "source": "00bab1dc",
  "target": "00bab1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1e4`](#insn-00bab1e4)

~~~json
{
  "source": "00bab1e4",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab1e8`](#insn-00bab1e8)

~~~json
{
  "source": "00bab1e8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab1f4`](#insn-00bab1f4)

~~~json
{
  "source": "00bab1f4",
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab1fc`](#insn-00bab1fc)

~~~json
{
  "source": "00bab1fc",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab200`](#insn-00bab200)

~~~json
{
  "source": "00bab200",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab20c`](#insn-00bab20c)

~~~json
{
  "source": "00bab20c",
  "target": "00bab390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab214`](#insn-00bab214)

~~~json
{
  "source": "00bab214",
  "target": "00bab390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab21c`](#insn-00bab21c)

~~~json
{
  "source": "00bab21c",
  "target": "00bab384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab228`](#insn-00bab228)

~~~json
{
  "source": "00bab228",
  "target": "00bab398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab22c`](#insn-00bab22c)

~~~json
{
  "source": "00bab22c",
  "target": "00bab39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab234`](#insn-00bab234)

~~~json
{
  "source": "00bab234",
  "target": "00bab260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab244`](#insn-00bab244)

~~~json
{
  "source": "00bab244",
  "target": "00bab260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab24c`](#insn-00bab24c)

~~~json
{
  "source": "00bab24c",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab258`](#insn-00bab258)

~~~json
{
  "source": "00bab258",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab25c`](#insn-00bab25c)

~~~json
{
  "source": "00bab25c",
  "target": "00bab274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab264`](#insn-00bab264)

~~~json
{
  "source": "00bab264",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab268`](#insn-00bab268)

~~~json
{
  "source": "00bab268",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab274`](#insn-00bab274)

~~~json
{
  "source": "00bab274",
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab27c`](#insn-00bab27c)

~~~json
{
  "source": "00bab27c",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab280`](#insn-00bab280)

~~~json
{
  "source": "00bab280",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab28c`](#insn-00bab28c)

~~~json
{
  "source": "00bab28c",
  "target": "00bab2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab294`](#insn-00bab294)

~~~json
{
  "source": "00bab294",
  "target": "00bab2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2a8`](#insn-00bab2a8)

~~~json
{
  "source": "00bab2a8",
  "target": "00bab2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2b0`](#insn-00bab2b0)

~~~json
{
  "source": "00bab2b0",
  "target": "00bab2b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2c0`](#insn-00bab2c0)

~~~json
{
  "source": "00bab2c0",
  "target": "00baafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2c8`](#insn-00bab2c8)

~~~json
{
  "source": "00bab2c8",
  "target": "00bab2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2d8`](#insn-00bab2d8)

~~~json
{
  "source": "00bab2d8",
  "target": "00bab2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2e0`](#insn-00bab2e0)

~~~json
{
  "source": "00bab2e0",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab2ec`](#insn-00bab2ec)

~~~json
{
  "source": "00bab2ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f0`](#insn-00bab2f0)

~~~json
{
  "source": "00bab2f0",
  "target": "00bab308",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab2f8`](#insn-00bab2f8)

~~~json
{
  "source": "00bab2f8",
  "target": "00c9b430",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b430",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab2fc`](#insn-00bab2fc)

~~~json
{
  "source": "00bab2fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab308`](#insn-00bab308)

~~~json
{
  "source": "00bab308",
  "target": "01125de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125de0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab310`](#insn-00bab310)

~~~json
{
  "source": "00bab310",
  "target": "00c5cd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab314`](#insn-00bab314)

~~~json
{
  "source": "00bab314",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab320`](#insn-00bab320)

~~~json
{
  "source": "00bab320",
  "target": "00bab338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab328`](#insn-00bab328)

~~~json
{
  "source": "00bab328",
  "target": "00bab338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab33c`](#insn-00bab33c)

~~~json
{
  "source": "00bab33c",
  "target": "00bab344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab344`](#insn-00bab344)

~~~json
{
  "source": "00bab344",
  "target": "00bab34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab350`](#insn-00bab350)

~~~json
{
  "source": "00bab350",
  "target": "00baafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab364`](#insn-00bab364)

~~~json
{
  "source": "00bab364",
  "target": "00bab36c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab36c`](#insn-00bab36c)

~~~json
{
  "source": "00bab36c",
  "target": "00bab374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab380`](#insn-00bab380)

~~~json
{
  "source": "00bab380",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab394`](#insn-00bab394)

~~~json
{
  "source": "00bab394",
  "target": "00bab39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab39c`](#insn-00bab39c)

~~~json
{
  "source": "00bab39c",
  "target": "00bab3a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3b0`](#insn-00bab3b0)

~~~json
{
  "source": "00bab3b0",
  "target": "00baafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3cc`](#insn-00bab3cc)

~~~json
{
  "source": "00bab3cc",
  "target": "00bab3d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3d4`](#insn-00bab3d4)

~~~json
{
  "source": "00bab3d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3ec`](#insn-00bab3ec)

~~~json
{
  "source": "00bab3ec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f0`](#insn-00bab3f0)

~~~json
{
  "source": "00bab3f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3f8`](#insn-00bab3f8)

~~~json
{
  "source": "00bab3f8",
  "target": "00baafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab3fc`](#insn-00bab3fc)

~~~json
{
  "source": "00bab3fc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
