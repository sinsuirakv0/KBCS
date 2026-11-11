# 00bacbfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bacbfc",
  "name": "FUN_00bacbfc",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a340bc3814cac81fbd5d648a5966233b6841c944a993b86d33104265c44dcf71",
  "source_text_sha256": "a340bc3814cac81fbd5d648a5966233b6841c944a993b86d33104265c44dcf71"
}
~~~

## 呼び出し元

- [00babf9c](../00bab/00babf9c.md)
- [00bace04](../00bac/00bace04.md)
- [00bad0e4](../00bad/00bad0e4.md)

## 呼び出し先

- [00bac950](../00bac/00bac950.md)
- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 5695 bytes

~~~c

int FUN_00bacbfc(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
  
                    /* try { // try from 00bacc14 to 00cacc1f has its CatchHandler @ 00bacda4 */
  iVar6 = FUN_00bac950();
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
                    /* try { // try from 00bacc40 to 00cacc4b has its CatchHandler @ 00bacd94 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* try { // try from 00bacc64 to 00cacc6f has its CatchHandler @ 00bacd90 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bacc78 to 00cacc7f has its CatchHandler @ 00bace68 */
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
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
                    /* try { // try from 00bacc9c to 00cacca7 has its CatchHandler @ 00bacd80 */
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00baccb8;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00baccb8:
  *param_3 = pbVar11;
                    /* try { // try from 00baccbc to 00caccc7 has its CatchHandler @ 00bacd7c */
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
                    /* try { // try from 00baccc8 to 00cacce3 has its CatchHandler @ 00bace1c */
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bacce4 to 00cacd53 has its CatchHandler @ 00bacea0 */
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
        goto LAB_00bacd48;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacd48:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
                    /* try { // try from 00bacd54 to 00cacea3 has its CatchHandler @ 00bac9f4 */
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 2;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00baccbc with catch @ 00bacd7c */
                    /* catch() { ... } // from try @ 00bacc9c with catch @ 00bacd80 */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
                    /* catch() { ... } // from try @ 00bacc64 with catch @ 00bacd90 */
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
                    /* catch() { ... } // from try @ 00bacc40 with catch @ 00bacd94 */
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
                    /* catch() { ... } // from try @ 00bacc14 with catch @ 00bacda4 */
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bacbf4 with catch @ 00bacda8 */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00bacba8 with catch @ 00bacdb8 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
                    /* catch() { ... } // from try @ 00bacb84 with catch @ 00bacdbc */
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bacdcc;
      }
    }
                    /* catch() { ... } // from try @ 00baca94 with catch @ 00bacdf8 */
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bacdcc:
                    /* catch() { ... } // from try @ 00bacb58 with catch @ 00bacdcc */
                    /* catch() { ... } // from try @ 00bacb38 with catch @ 00bacdd0 */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00bacb04 with catch @ 00bacde0 */
                    /* catch() { ... } // from try @ 00bacae0 with catch @ 00bacde4 */
                    /* catch() { ... } // from try @ 00bacab4 with catch @ 00bacdf4 */
  return iVar6 + 3;
}

~~~
