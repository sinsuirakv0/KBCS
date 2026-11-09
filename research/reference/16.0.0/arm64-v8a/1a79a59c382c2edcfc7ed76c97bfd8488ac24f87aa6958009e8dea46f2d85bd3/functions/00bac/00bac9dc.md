# 00bac9dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bac9dc",
  "name": "FUN_00bac9dc",
  "size": 736,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a32da9991f5090460fc8052fd86edec18e4fbb90041a9c3f4c005190d0e89a65",
  "source_text_sha256": "a32da9991f5090460fc8052fd86edec18e4fbb90041a9c3f4c005190d0e89a65"
}
~~~

## 呼び出し元

- [00babb74](../00bab/00babb74.md)
- [00baccbc](../00bac/00baccbc.md)

## 呼び出し先

- [00bac7d4](../00bac/00bac7d4.md)
- [00c57c50](../00c57/00c57c50.md)

## 疑似コード / UTF-8 7778 bytes

~~~c

int FUN_00bac9dc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                undefined8 *param_5)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *pbVar11;
  byte *pbVar12;
  
                    /* try { // try from 00bac9f8 to 00caca03 has its CatchHandler @ 00bacbac */
  iVar6 = FUN_00bac7d4();
  pbVar11 = (byte *)*param_5;
                    /* try { // try from 00baca18 to 00caca23 has its CatchHandler @ 00bacba8 */
  pbVar12 = (byte *)*param_4;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* try { // try from 00baca44 to 00caca4f has its CatchHandler @ 00bacb98 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
                    /* try { // try from 00baca68 to 00caca73 has its CatchHandler @ 00bacb94 */
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* try { // try from 00baca7c to 00caca83 has its CatchHandler @ 00bacc6c */
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar7 != 0) {
                    /* try { // try from 00bacaa0 to 00cacaab has its CatchHandler @ 00bacb84 */
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00bacadc;
      }
    }
                    /* try { // try from 00bacac0 to 00cacacb has its CatchHandler @ 00bacb80 */
                    /* try { // try from 00bacacc to 00cacae7 has its CatchHandler @ 00bacc20 */
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00bacadc:
  *param_4 = pbVar11;
  *param_5 = pbVar12;
  pbVar11 = (byte *)*param_4;
                    /* try { // try from 00bacae8 to 00cacb57 has its CatchHandler @ 00bacca4 */
  pbVar12 = (byte *)*param_3;
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacb6c;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacb6c:
  *param_3 = pbVar11;
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
  iVar7 = iVar6 + 2;
                    /* catch() { ... } // from try @ 00bacac0 with catch @ 00bacb80 */
                    /* catch() { ... } // from try @ 00bacaa0 with catch @ 00bacb84 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* catch() { ... } // from try @ 00baca68 with catch @ 00bacb94 */
                    /* catch() { ... } // from try @ 00baca44 with catch @ 00bacb98 */
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00baca18 with catch @ 00bacba8 */
    uVar1 = (ulong)(bVar4 >> 1);
                    /* catch() { ... } // from try @ 00bac9f8 with catch @ 00bacbac */
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* catch() { ... } // from try @ 00bac9ac with catch @ 00bacbbc */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
                    /* catch() { ... } // from try @ 00bac988 with catch @ 00bacbc0 */
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bac95c with catch @ 00bacbd0 */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
                    /* catch() { ... } // from try @ 00bac93c with catch @ 00bacbd4 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
                    /* catch() { ... } // from try @ 00bac908 with catch @ 00bacbe4 */
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacbfc;
      }
    }
                    /* catch() { ... } // from try @ 00bac8b8 with catch @ 00bacbf8 */
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacbfc:
                    /* catch() { ... } // from try @ 00bac898 with catch @ 00bacbfc */
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
  pbVar12 = (byte *)*param_1;
                    /* catch() { ... } // from try @ 00bac860 with catch @ 00bacc0c */
  iVar7 = iVar6 + 3;
                    /* catch() { ... } // from try @ 00bac83c with catch @ 00bacc10 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
                    /* catch() { ... } // from try @ 00bacacc with catch @ 00bacc20 */
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00bac874 with catch @ 00bacc6c
                       catch() { ... } // from try @ 00bac91c with catch @ 00bacc6c
                       catch() { ... } // from try @ 00bac9c0 with catch @ 00bacc6c
                       catch() { ... } // from try @ 00baca7c with catch @ 00bacc6c */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacc80;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacc80:
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00bacae8 with catch @ 00bacca4 */
                    /* try { // try from 00bacca8 to 00cacd5f has its CatchHandler @ 00bacca8
                       catch() { ... } // from try @ 00bacca8 with catch @ 00bacca8
                       catch() { ... } // from try @ 00bacf6c with catch @ 00bacca8
                       catch() { ... } // from try @ 00bad228 with catch @ 00bacca8 */
  return iVar6 + 4;
}

~~~
