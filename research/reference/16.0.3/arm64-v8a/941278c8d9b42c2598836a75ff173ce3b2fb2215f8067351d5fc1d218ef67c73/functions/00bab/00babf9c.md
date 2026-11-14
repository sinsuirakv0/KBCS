# 00babf9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

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
  "source_text_sha256": "bd0028919ac821d40bcab25756346e58d718de7735c6573f8504b39756b9133b"
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
