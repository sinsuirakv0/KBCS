# 00bacea0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bacea0",
  "name": "FUN_00bacea0",
  "size": 736,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea8198534676c489d46334c57d0c277138d7d48d046fbb5180bad38674f9e82f",
  "source_text_sha256": "ea8198534676c489d46334c57d0c277138d7d48d046fbb5180bad38674f9e82f"
}
~~~

## 呼び出し元

- [00bac038](../00bac/00bac038.md)
- [00bad180](../00bad/00bad180.md)

## 呼び出し先

- [00bacc98](../00bac/00bacc98.md)
- [00c58120](../00c58/00c58120.md)

## 疑似コード / UTF-8 7079 bytes

~~~c

int FUN_00bacea0(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
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
  
  iVar6 = FUN_00bacc98();
                    /* catch() { ... } // from try @ 00bacae0 with catch @ 00baced8
                       catch() { ... } // from try @ 00bacb88 with catch @ 00baced8
                       catch() { ... } // from try @ 00bacc2c with catch @ 00baced8
                       catch() { ... } // from try @ 00bacce8 with catch @ 00baced8 */
  pbVar11 = (byte *)*param_5;
  pbVar12 = (byte *)*param_4;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00bacd54 with catch @ 00bacf10 */
                    /* try { // try from 00bacf14 to 00cacfcb has its CatchHandler @ 00bacf14
                       catch() { ... } // from try @ 00bacf14 with catch @ 00bacf14
                       catch() { ... } // from try @ 00bad1d8 with catch @ 00bacf14
                       catch() { ... } // from try @ 00bad494 with catch @ 00bacf14 */
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
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00bacfa0;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00bacfa0:
  *param_4 = pbVar11;
  *param_5 = pbVar12;
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
  iVar7 = iVar6 + 1;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bacfcc to 00cacfd7 has its CatchHandler @ 00bad690 */
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
                    /* try { // try from 00bacff0 to 00cacffb has its CatchHandler @ 00bad68c */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bad004 to 00cad00f has its CatchHandler @ 00bad66c */
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* try { // try from 00bad010 to 00cad01b has its CatchHandler @ 00bad65c */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bad030;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bad030:
  *param_3 = pbVar11;
                    /* try { // try from 00bad034 to 00cad03f has its CatchHandler @ 00bad634 */
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
  iVar7 = iVar6 + 2;
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
                    /* try { // try from 00bad05c to 00cad067 has its CatchHandler @ 00bad628 */
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
                    /* try { // try from 00bad080 to 00cad08b has its CatchHandler @ 00bad624 */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar11 + 0x10);
      pbVar10 = *(byte **)(pbVar12 + 0x10);
                    /* try { // try from 00bad090 to 00cad09b has its CatchHandler @ 00bad61c */
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
        goto LAB_00bad0c0;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else {
                    /* try { // try from 00bad0b0 to 00cad0bb has its CatchHandler @ 00bad608 */
    if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return iVar7;
    }
  }
LAB_00bad0c0:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
  pbVar11 = (byte *)*param_2;
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 3;
                    /* try { // try from 00bad0dc to 00cad0e7 has its CatchHandler @ 00bad5fc */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
                    /* try { // try from 00bad100 to 00cad10b has its CatchHandler @ 00bad5f8 */
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
                    /* try { // try from 00bad110 to 00cad11b has its CatchHandler @ 00bad5f0 */
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
                    /* try { // try from 00bad130 to 00cad13b has its CatchHandler @ 00bad5dc */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bad144;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00bad144:
                    /* try { // try from 00bad148 to 00cad153 has its CatchHandler @ 00bad5d4 */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* try { // try from 00bad154 to 00cad15f has its CatchHandler @ 00bad5d0 */
                    /* try { // try from 00bad170 to 00cad18b has its CatchHandler @ 00bad6a0 */
  return iVar6 + 4;
}

~~~
