# 00baafa8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
  "source_text_sha256": "653b771484036286579e6c3f036ba0c382ae54dd4dafe4f3a2d65ec8d7ddc40a"
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
