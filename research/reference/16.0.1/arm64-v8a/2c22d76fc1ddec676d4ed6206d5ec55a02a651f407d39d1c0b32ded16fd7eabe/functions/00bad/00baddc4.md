# 00baddc4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00baddc4",
  "name": "FUN_00baddc4",
  "size": 684,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e54edfe0c1ca16fc43532f97c9c53950db12a8891c99508e5c2d1482fcaa516",
  "source_text_sha256": "9e54edfe0c1ca16fc43532f97c9c53950db12a8891c99508e5c2d1482fcaa516"
}
~~~

## 呼び出し元

- [00bad3f8](../00bad/00bad3f8.md)
- [00bae070](../00bae/00bae070.md)
- [00bae558](../00bae/00bae558.md)

## 呼び出し先

- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 6282 bytes

~~~c

undefined8 FUN_00baddc4(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3)

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
  long lVar13;
  long lVar14;
  
                    /* catch() { ... } // from try @ 00badc30 with catch @ 00baddd0 */
  pbVar12 = (byte *)*param_2;
  pbVar11 = (byte *)*param_1;
  lVar14 = *(long *)(pbVar12 + 0x80);
  lVar13 = *(long *)(pbVar11 + 0x80);
  if (lVar14 == lVar13) {
    bVar4 = *pbVar11;
                    /* catch() { ... } // from try @ 00badc1c with catch @ 00bade0c */
    bVar5 = *pbVar12;
                    /* catch() { ... } // from try @ 00badc04 with catch @ 00bade1c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar11 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar12 + 8);
    }
                    /* catch() { ... } // from try @ 00badadc with catch @ 00bade2c */
    sVar3 = uVar1;
                    /* catch() { ... } // from try @ 00badc24 with catch @ 00bade30 */
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 == 0) {
LAB_00bade58:
      uVar6 = 0;
                    /* catch() { ... } // from try @ 00bada04 with catch @ 00bade64 */
      if (uVar2 < uVar1) {
        uVar6 = 0xffffffff;
      }
    }
    else {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      uVar6 = memcmp(pbVar9,pbVar10,sVar3);
      if (uVar6 == 0) goto LAB_00bade58;
    }
                    /* catch() { ... } // from try @ 00bad774 with catch @ 00bade68 */
    uVar6 = uVar6 >> 0x1f;
  }
  else {
    uVar6 = (uint)(lVar14 < lVar13);
  }
  pbVar9 = (byte *)*param_3;
  if (*(long *)(pbVar9 + 0x80) == lVar14) {
    bVar4 = *pbVar12;
    bVar5 = *pbVar9;
                    /* catch() { ... } // from try @ 00bad768 with catch @ 00bade9c */
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar12 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar9 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar10 = *(byte **)(pbVar9 + 0x10);
      __s2 = *(byte **)(pbVar12 + 0x10);
                    /* catch() { ... } // from try @ 00bad71c with catch @ 00badec0 */
      if ((bVar5 & 1) == 0) {
        pbVar10 = pbVar9 + 1;
      }
                    /* catch() { ... } // from try @ 00bad704 with catch @ 00badec8 */
      if ((bVar4 & 1) == 0) {
        __s2 = pbVar12 + 1;
      }
                    /* catch() { ... } // from try @ 00bad7b4 with catch @ 00baded0
                       catch() { ... } // from try @ 00bad9e8 with catch @ 00baded0 */
      uVar7 = memcmp(pbVar10,__s2,sVar3);
                    /* catch() { ... } // from try @ 00bad8fc with catch @ 00baded4 */
      if (uVar7 != 0) {
        uVar7 = uVar7 >> 0x1f;
        goto joined_r0x00badf64;
      }
    }
    uVar7 = 0;
    if (uVar2 < uVar1) {
      uVar7 = 0xffffffff;
    }
    uVar7 = uVar7 >> 0x1f;
  }
  else {
    uVar7 = (uint)(*(long *)(pbVar9 + 0x80) < lVar14);
  }
joined_r0x00badf64:
  if (uVar6 == 0) {
    if (uVar7 == 0) {
      return 0;
    }
    *param_2 = pbVar9;
    *param_3 = pbVar12;
    pbVar11 = (byte *)*param_2;
    pbVar12 = (byte *)*param_1;
                    /* catch() { ... } // from try @ 00bad7fc with catch @ 00badef4 */
    if (*(long *)(pbVar11 + 0x80) == *(long *)(pbVar12 + 0x80)) {
                    /* catch() { ... } // from try @ 00bad7ec with catch @ 00badf04 */
      bVar4 = *pbVar12;
                    /* catch() { ... } // from try @ 00bad7e0 with catch @ 00badf08 */
      bVar5 = *pbVar11;
                    /* catch() { ... } // from try @ 00badbac with catch @ 00badf10
                       catch() { ... } // from try @ 00badd88 with catch @ 00badf10 */
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
            return 1;
          }
          goto LAB_00bae02c;
        }
      }
      if (uVar1 <= uVar2) {
        return 1;
      }
    }
    else if (*(long *)(pbVar12 + 0x80) <= *(long *)(pbVar11 + 0x80)) {
      return 1;
    }
LAB_00bae02c:
    *param_1 = pbVar11;
    *param_2 = pbVar12;
    return 2;
  }
  if (uVar7 != 0) {
    *param_1 = pbVar9;
    *param_3 = pbVar11;
    return 1;
  }
  *param_1 = pbVar12;
  *param_2 = pbVar11;
  pbVar12 = (byte *)*param_3;
  if (*(long *)(pbVar12 + 0x80) == lVar13) {
    bVar4 = *pbVar11;
    bVar5 = *pbVar12;
    uVar1 = (ulong)(bVar4 >> 1);
    if ((bVar4 & 1) != 0) {
      uVar1 = *(ulong *)(pbVar11 + 8);
    }
    uVar2 = (ulong)(bVar5 >> 1);
    if ((bVar5 & 1) != 0) {
      uVar2 = *(ulong *)(pbVar12 + 8);
    }
    sVar3 = uVar1;
    if (uVar2 <= uVar1) {
      sVar3 = uVar2;
    }
    if (sVar3 != 0) {
      pbVar9 = *(byte **)(pbVar12 + 0x10);
      pbVar10 = *(byte **)(pbVar11 + 0x10);
      if ((bVar5 & 1) == 0) {
        pbVar9 = pbVar12 + 1;
      }
      if ((bVar4 & 1) == 0) {
        pbVar10 = pbVar11 + 1;
      }
      iVar8 = memcmp(pbVar9,pbVar10,sVar3);
      if (iVar8 != 0) {
        if (-1 < iVar8) {
          return 1;
        }
        goto LAB_00bae040;
      }
    }
    if (uVar1 <= uVar2) {
      return 1;
    }
  }
  else if (lVar13 <= *(long *)(pbVar12 + 0x80)) {
    return 1;
  }
LAB_00bae040:
  *param_2 = pbVar12;
  *param_3 = pbVar11;
  return 2;
}

~~~
