# 00baccbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00baccbc",
  "name": "FUN_00baccbc",
  "size": 788,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "370a2e8a4b76d52d0178bc0f030a61df1c493df2b3d97f304025552de6e19597",
  "source_text_sha256": "370a2e8a4b76d52d0178bc0f030a61df1c493df2b3d97f304025552de6e19597"
}
~~~

## 呼び出し元

- [00babb74](../00bab/00babb74.md)

## 呼び出し先

- [00bac528](../00bac/00bac528.md)
- [00bac7d4](../00bac/00bac7d4.md)
- [00bac9dc](../00bac/00bac9dc.md)
- [00c57c50](../00c57/00c57c50.md)

## 疑似コード / UTF-8 7446 bytes

~~~c

bool FUN_00baccbc(undefined8 *param_1,undefined8 *param_2)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  undefined8 *puVar7;
  byte *pbVar8;
  byte *pbVar9;
  byte *pbVar10;
  undefined8 *puVar11;
  long lVar12;
  byte *pbVar13;
  undefined8 *puVar14;
  ulong uVar15;
  long lVar16;
  long lVar17;
  int local_6c;
  
  switch((long)param_2 - (long)param_1 >> 3) {
  case 0:
  case 1:
    break;
  case 2:
    pbVar10 = (byte *)param_2[-1];
    pbVar13 = (byte *)*param_1;
    if (*(ulong *)(pbVar10 + 0x80) == *(ulong *)(pbVar13 + 0x80)) {
      bVar4 = *pbVar13;
      bVar5 = *pbVar10;
      uVar15 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar15 = *(ulong *)(pbVar13 + 8);
      }
      uVar1 = (ulong)(bVar5 >> 1);
      if ((bVar5 & 1) != 0) {
        uVar1 = *(ulong *)(pbVar10 + 8);
      }
      sVar3 = uVar15;
      if (uVar1 <= uVar15) {
        sVar3 = uVar1;
      }
      if (sVar3 != 0) {
        pbVar8 = *(byte **)(pbVar10 + 0x10);
                    /* try { // try from 00bacd60 to 00cacd6b has its CatchHandler @ 00bad424 */
        pbVar9 = *(byte **)(pbVar13 + 0x10);
        if ((bVar5 & 1) == 0) {
          pbVar8 = pbVar10 + 1;
        }
        if ((bVar4 & 1) == 0) {
          pbVar9 = pbVar13 + 1;
        }
        iVar6 = memcmp(pbVar8,pbVar9,sVar3);
        if (iVar6 != 0) {
          if (-1 < iVar6) {
            return true;
          }
          goto LAB_00bacf88;
        }
      }
      if (uVar15 <= uVar1) {
        return true;
      }
    }
    else if (*(ulong *)(pbVar13 + 0x80) <= *(ulong *)(pbVar10 + 0x80)) {
      return true;
    }
LAB_00bacf88:
    *param_1 = pbVar10;
    param_2[-1] = pbVar13;
    break;
  case 3:
    FUN_00bac528(param_1,param_1 + 1,param_2 + -1);
    break;
  case 4:
    FUN_00bac7d4(param_1,param_1 + 1,param_1 + 2,param_2 + -1);
    break;
  case 5:
                    /* try { // try from 00bacf6c to 00cacfbf has its CatchHandler @ 00bacca8 */
    FUN_00bac9dc(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
    break;
  default:
                    /* try { // try from 00bacd84 to 00cacd8f has its CatchHandler @ 00bad420 */
    FUN_00bac528(param_1,param_1 + 1,param_1 + 2);
                    /* try { // try from 00bacd98 to 00cacda3 has its CatchHandler @ 00bad400 */
    if (param_1 + 3 != param_2) {
                    /* try { // try from 00bacda4 to 00cacdaf has its CatchHandler @ 00bad3f0 */
      lVar12 = 0;
      local_6c = 0;
      puVar14 = param_1 + 3;
      puVar11 = param_1 + 2;
      do {
        puVar7 = puVar14;
        pbVar13 = (byte *)*puVar7;
        pbVar10 = (byte *)*puVar11;
                    /* try { // try from 00bacdf0 to 00cacdfb has its CatchHandler @ 00bad3bc */
        uVar15 = *(ulong *)(pbVar13 + 0x80);
        if (uVar15 == *(ulong *)(pbVar10 + 0x80)) {
          bVar4 = *pbVar10;
          bVar5 = *pbVar13;
                    /* try { // try from 00bace14 to 00cace1f has its CatchHandler @ 00bad3b8 */
          uVar1 = (ulong)(bVar4 >> 1);
          if ((bVar4 & 1) != 0) {
            uVar1 = *(ulong *)(pbVar10 + 8);
          }
                    /* try { // try from 00bace24 to 00cace2f has its CatchHandler @ 00bad3b0 */
          uVar2 = (ulong)(bVar5 >> 1);
          if ((bVar5 & 1) != 0) {
            uVar2 = *(ulong *)(pbVar13 + 8);
          }
          sVar3 = uVar1;
          if (uVar2 <= uVar1) {
            sVar3 = uVar2;
          }
          if (sVar3 != 0) {
            pbVar8 = *(byte **)(pbVar13 + 0x10);
            pbVar9 = *(byte **)(pbVar10 + 0x10);
                    /* try { // try from 00bace44 to 00cace4f has its CatchHandler @ 00bad39c */
            if ((bVar5 & 1) == 0) {
              pbVar8 = pbVar13 + 1;
            }
            if ((bVar4 & 1) == 0) {
              pbVar9 = pbVar10 + 1;
            }
            iVar6 = memcmp(pbVar8,pbVar9,sVar3);
            if (iVar6 != 0) {
              if (iVar6 < 0) goto LAB_00bace78;
              goto LAB_00bacdd4;
            }
          }
                    /* try { // try from 00bace70 to 00cace7b has its CatchHandler @ 00bad390 */
          if (uVar2 < uVar1) {
LAB_00bace78:
            *puVar7 = pbVar10;
            puVar14 = puVar11;
            if (puVar11 != param_1) {
              lVar17 = lVar12;
                    /* try { // try from 00bace94 to 00cace9f has its CatchHandler @ 00bad38c */
              do {
                pbVar10 = *(byte **)((long)param_1 + lVar17 + 8);
                if (uVar15 == *(ulong *)(pbVar10 + 0x80)) {
                    /* try { // try from 00bacec4 to 00cacecf has its CatchHandler @ 00bad370 */
                  bVar4 = *pbVar10;
                  bVar5 = *pbVar13;
                    /* try { // try from 00baced0 to 00cacedb has its CatchHandler @ 00bad36c */
                    /* try { // try from 00bacedc to 00cacee7 has its CatchHandler @ 00bad368 */
                  uVar1 = (ulong)(bVar4 >> 1);
                  if ((bVar4 & 1) != 0) {
                    uVar1 = *(ulong *)(pbVar10 + 8);
                  }
                  uVar2 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00bacee8 to 00cacef3 has its CatchHandler @ 00bad364 */
                  if ((bVar5 & 1) != 0) {
                    uVar2 = *(ulong *)(pbVar13 + 8);
                  }
                  sVar3 = uVar1;
                  if (uVar2 <= uVar1) {
                    sVar3 = uVar2;
                  }
                  puVar14 = puVar11;
                  if (sVar3 != 0) {
                    /* try { // try from 00bacf04 to 00cacf1f has its CatchHandler @ 00bad434 */
                    pbVar9 = *(byte **)(pbVar10 + 0x10);
                    pbVar8 = pbVar13 + 1;
                    if ((bVar5 & 1) != 0) {
                      pbVar8 = *(byte **)(pbVar13 + 0x10);
                    }
                    if ((bVar4 & 1) == 0) {
                      pbVar9 = pbVar10 + 1;
                    }
                    iVar6 = memcmp(pbVar8,pbVar9,sVar3);
                    if (iVar6 != 0) {
                      if (iVar6 < 0) goto LAB_00bace9c;
                      break;
                    }
                  }
                  if (uVar1 <= uVar2) break;
                }
                else if (*(ulong *)(pbVar10 + 0x80) <= uVar15) {
                  puVar14 = (undefined8 *)((long)param_1 + lVar17 + 0x10);
                  break;
                }
LAB_00bace9c:
                lVar16 = lVar17 + -8;
                puVar11 = puVar11 + -1;
                    /* try { // try from 00bacea4 to 00caceaf has its CatchHandler @ 00bad384 */
                *(byte **)((long)param_1 + lVar17 + 0x10) = pbVar10;
                puVar14 = param_1;
                lVar17 = lVar16;
              } while (lVar16 != -0x10);
            }
            *puVar14 = pbVar13;
            local_6c = local_6c + 1;
                    /* try { // try from 00bacdc8 to 00cacdd3 has its CatchHandler @ 00bad3c8 */
            if (local_6c == 8) {
                    /* try { // try from 00bacfc0 to 00cacfcb has its CatchHandler @ 00bad35c */
              return puVar7 + 1 == param_2;
            }
          }
        }
        else if (uVar15 < *(ulong *)(pbVar10 + 0x80)) goto LAB_00bace78;
LAB_00bacdd4:
        lVar12 = lVar12 + 8;
        puVar14 = puVar7 + 1;
        puVar11 = puVar7;
      } while (puVar7 + 1 != param_2);
    }
  }
  return true;
}

~~~
