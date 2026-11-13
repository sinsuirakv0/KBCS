# 00bac9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bac9ec",
  "name": "FUN_00bac9ec",
  "size": 684,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05748742102e8d1ef861a58f532fcbaef1d359518cf53c5b981a0dc6ee1b8d78",
  "source_text_sha256": "05748742102e8d1ef861a58f532fcbaef1d359518cf53c5b981a0dc6ee1b8d78"
}
~~~

## 呼び出し元

- [00bac038](../00bac/00bac038.md)
- [00bacc98](../00bac/00bacc98.md)
- [00bad180](../00bad/00bad180.md)

## 呼び出し先

- [00c58120](../00c58/00c58120.md)

## 疑似コード / UTF-8 6813 bytes

~~~c

undefined8 FUN_00bac9ec(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3)

{
  ulong uVar1;
  ulong uVar2;
  size_t sVar3;
  byte bVar4;
  byte bVar5;
  uint uVar6;
  uint uVar7;
  int iVar8;
  byte *pbVar9;
  byte *pbVar10;
  byte *__s2;
  byte *pbVar11;
  byte *pbVar12;
  ulong uVar13;
  ulong uVar14;
  
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac84c with catch @ 00baca08
                        */
  pbVar12 = (byte *)*param_2;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac828 with catch @ 00baca0c
                        */
  pbVar11 = (byte *)*param_1;
  uVar14 = *(ulong *)(pbVar12 + 0x80);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac94c with catch @ 00baca1c
                        */
  uVar13 = *(ulong *)(pbVar11 + 0x80);
  if (uVar14 == uVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
    uVar2 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    uVar1 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar2;
    if (uVar1 <= uVar2) {
      sVar3 = uVar1;
    }
    if (sVar3 == 0) {
LAB_00baca80:
      uVar6 = 0;
      if (uVar1 < uVar2) {
        uVar6 = 0xffffffff;
      }
    }
    else {
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bac96c with catch @ 00baca60
                        */
      pbVar9 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bacdc4 with catch @ 00baca64 */
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      uVar6 = memcmp(pbVar9,pbVar10,sVar3);
      if (uVar6 == 0) goto LAB_00baca80;
    }
    uVar6 = uVar6 >> 0x1f;
  }
  else {
    uVar6 = (uint)(uVar14 < uVar13);
  }
  pbVar9 = (byte *)*param_3;
                    /* try { // try from 00bacaa8 to 00cacab3 has its CatchHandler @ 00bace7c */
  if (*(ulong *)(pbVar9 + 0x80) == uVar14) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar9;
    uVar14 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar14 = *(ulong *)(pbVar12 + 8);
    }
                    /* try { // try from 00bacacc to 00cacad7 has its CatchHandler @ 00bace78 */
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar9 + 8);
    }
    sVar3 = uVar14;
    if (uVar2 <= uVar14) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* try { // try from 00bacae0 to 00cacae7 has its CatchHandler @ 00baced8 */
      pbVar10 = *(byte **)(pbVar9 + 0x10);
      __s2 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar10 = pbVar9 + 1;
      }
      if ((bVar4 & 1) == 0) {
        __s2 = pbVar12 + 1;
      }
      uVar7 = memcmp(pbVar10,__s2,sVar3);
      if (uVar7 != 0) {
        uVar7 = uVar7 >> 0x1f;
                    /* try { // try from 00bacb04 to 00cacb0f has its CatchHandler @ 00bace68 */
        goto joined_r0x00bacb8c;
      }
    }
                    /* try { // try from 00bacba8 to 00cacbb3 has its CatchHandler @ 00bace40 */
    uVar7 = 0;
    if (uVar2 < uVar14) {
      uVar7 = 0xffffffff;
    }
    uVar7 = uVar7 >> 0x1f;
  }
  else {
                    /* try { // try from 00bacb88 to 00cacb8b has its CatchHandler @ 00baced8 */
    uVar7 = (uint)(*(ulong *)(pbVar9 + 0x80) < uVar14);
  }
joined_r0x00bacb8c:
  if (uVar6 == 0) {
    if (uVar7 == 0) {
      return 0;
    }
    *param_2 = pbVar9;
    *param_3 = pbVar12;
    pbVar11 = (byte *)*param_2;
    pbVar12 = (byte *)*param_1;
                    /* try { // try from 00bacb24 to 00cacb2f has its CatchHandler @ 00bace64 */
    if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
      bVar4 = *pbVar12;
      bVar5 = *pbVar11;
      uVar13 = (ulong)(bVar4 >> 1);
      if ((bVar4 & 1) != 0) {
        uVar13 = *(ulong *)(pbVar12 + 8);
      }
      uVar14 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00bacb50 to 00cacb5b has its CatchHandler @ 00bace54 */
      if ((bVar5 & 1) != 0) {
        uVar14 = *(ulong *)(pbVar11 + 8);
      }
      sVar3 = uVar13;
      if (uVar14 <= uVar13) {
        sVar3 = uVar14;
      }
      if (sVar3 != 0) {
        pbVar9 = *(byte **)(pbVar11 + 0x10);
        pbVar10 = *(byte **)(pbVar12 + 0x10);
        if ((bVar5 & 1) == 0) {
          pbVar9 = pbVar11 + 1;
        }
                    /* try { // try from 00bacb74 to 00cacb7f has its CatchHandler @ 00bace50 */
        if ((bVar4 & 1) == 0) {
          pbVar10 = pbVar12 + 1;
        }
        iVar8 = memcmp(pbVar9,pbVar10,sVar3);
        if (iVar8 != 0) {
          if (-1 < iVar8) {
            return 1;
          }
          goto LAB_00bacc54;
        }
      }
      if (uVar13 <= uVar14) {
        return 1;
      }
    }
    else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return 1;
    }
LAB_00bacc54:
    *param_1 = pbVar11;
    *param_2 = pbVar12;
    return 2;
  }
  if (uVar7 != 0) {
    *param_1 = pbVar9;
    *param_3 = pbVar11;
    return 1;
  }
                    /* try { // try from 00bacbc8 to 00cacbd3 has its CatchHandler @ 00bace3c */
  *param_1 = pbVar12;
  *param_2 = pbVar11;
  pbVar12 = (byte *)*param_3;
  if (*(ulong *)(pbVar12 + 0x80) == uVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
                    /* try { // try from 00bacbf4 to 00cacbff has its CatchHandler @ 00bace2c */
    uVar13 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar13 = *(ulong *)(pbVar11 + 8);
    }
    uVar14 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar14 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar13;
    if (uVar14 <= uVar13) {
      sVar3 = uVar14;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bacc18 to 00cacc23 has its CatchHandler @ 00bace28 */
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
                    /* try { // try from 00bacc2c to 00cacc43 has its CatchHandler @ 00baced8 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return 1;
        }
        goto LAB_00bacc68;
      }
    }
                    /* try { // try from 00bacc64 to 00cacc6f has its CatchHandler @ 00bace18 */
    if (uVar13 <= uVar14) {
      return 1;
    }
  }
  else if (uVar13 <= *(ulong *)(pbVar12 + 0x80)) {
    return 1;
  }
LAB_00bacc68:
  *param_2 = pbVar12;
  *param_3 = pbVar11;
                    /* try { // try from 00bacc84 to 00cacc8f has its CatchHandler @ 00bace14 */
  return 2;
}

~~~
