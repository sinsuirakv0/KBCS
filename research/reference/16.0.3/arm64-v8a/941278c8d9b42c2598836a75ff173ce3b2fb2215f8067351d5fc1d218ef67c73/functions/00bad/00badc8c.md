# 00badc8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00badc8c",
  "name": "FUN_00badc8c",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bcf55a0873947dc5df6005a28008f053ef4401023a6fdb142b7efc8ac4eb513",
  "source_text_sha256": "0bcf55a0873947dc5df6005a28008f053ef4401023a6fdb142b7efc8ac4eb513"
}
~~~

## 呼び出し元

- [00bad02c](../00bad/00bad02c.md)
- [00bade94](../00bad/00bade94.md)
- [00bae174](../00bae/00bae174.md)

## 呼び出し先

- [00bad9e0](../00bad/00bad9e0.md)
- [00c590f0](../00c59/00c590f0.md)

## 疑似コード / UTF-8 5873 bytes

~~~c

int FUN_00badc8c(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
  
                    /* try { // try from 00badca4 to 00cadcaf has its CatchHandler @ 00baddf8 */
  iVar6 = FUN_00bad9e0();
  pbVar11 = (byte *)*param_4;
  pbVar12 = (byte *)*param_3;
                    /* try { // try from 00badcc8 to 00cadcd3 has its CatchHandler @ 00baddf4 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
                    /* try { // try from 00badcdc to 00cadce3 has its CatchHandler @ 00badecc */
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
                    /* try { // try from 00badd00 to 00cadd0b has its CatchHandler @ 00badde4 */
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
                    /* try { // try from 00badd20 to 00cadd2b has its CatchHandler @ 00badde0 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
      iVar7 = memcmp(pbVar9,pbVar10,sVar3);
                    /* try { // try from 00badd2c to 00cadd47 has its CatchHandler @ 00bade80 */
      if (iVar7 != 0) {
        if (-1 < iVar7) {
          return iVar6;
        }
        goto LAB_00badd48;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar6;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar6;
  }
LAB_00badd48:
                    /* try { // try from 00badd48 to 00caddb7 has its CatchHandler @ 00badf04 */
  *param_3 = pbVar11;
  *param_4 = pbVar12;
  pbVar11 = (byte *)*param_3;
  pbVar12 = (byte *)*param_2;
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
                    /* try { // try from 00baddb8 to 00cadf07 has its CatchHandler @ 00bada58 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00baddd8;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
    return iVar7;
  }
LAB_00baddd8:
  *param_2 = pbVar11;
  *param_3 = pbVar12;
                    /* catch() { ... } // from try @ 00badd20 with catch @ 00badde0 */
  pbVar11 = (byte *)*param_2;
                    /* catch() { ... } // from try @ 00badd00 with catch @ 00badde4 */
  pbVar12 = (byte *)*param_1;
  iVar7 = iVar6 + 2;
                    /* catch() { ... } // from try @ 00badcc8 with catch @ 00baddf4 */
                    /* catch() { ... } // from try @ 00badca4 with catch @ 00baddf8 */
  if (*(ulong *)(pbVar11 + 0x80) == *(ulong *)(pbVar12 + 0x80)) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00badc78 with catch @ 00bade08 */
                    /* catch() { ... } // from try @ 00badc58 with catch @ 00bade0c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
                    /* catch() { ... } // from try @ 00badc0c with catch @ 00bade1c */
    uVar2 = (ulong)(bVar5 >> 1);
                    /* catch() { ... } // from try @ 00badbe8 with catch @ 00bade20 */
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar11 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
                    /* catch() { ... } // from try @ 00badbbc with catch @ 00bade30 */
      pbVar9 = *(byte **)(pbVar11 + 0x10);
                    /* catch() { ... } // from try @ 00badb9c with catch @ 00bade34 */
      pbVar10 = *(byte **)(pbVar12 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar11 + 1;
      }
                    /* catch() { ... } // from try @ 00badb68 with catch @ 00bade44 */
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00badb44 with catch @ 00bade48 */
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return iVar7;
        }
        goto LAB_00bade5c;
      }
    }
    if (uVar1 <= uVar2) {
      return iVar7;
    }
  }
  else {
                    /* catch() { ... } // from try @ 00badb18 with catch @ 00bade58 */
    if (*(ulong *)(pbVar12 + 0x80) <= *(ulong *)(pbVar11 + 0x80)) {
      return iVar7;
    }
  }
LAB_00bade5c:
                    /* catch() { ... } // from try @ 00badaf8 with catch @ 00bade5c */
  *param_1 = pbVar11;
  *param_2 = pbVar12;
                    /* catch() { ... } // from try @ 00badac0 with catch @ 00bade6c */
                    /* catch() { ... } // from try @ 00bada9c with catch @ 00bade70 */
                    /* catch() { ... } // from try @ 00badd2c with catch @ 00bade80 */
  return iVar6 + 3;
}

~~~
