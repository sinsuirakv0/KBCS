# 00baaae4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
  "source_text_sha256": "340a88fead96e4fd4bfe3ed704ef28125257f03fc3703b064c8f33ddd0afdf44"
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
