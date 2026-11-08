# 00bac0ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bac0ec",
  "name": "FUN_00bac0ec",
  "size": 660,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "494c2b9c764a29c5eb6621ead771a3eb51fa301563260ed8b786ede6857d3afd",
  "source_text_sha256": "494c2b9c764a29c5eb6621ead771a3eb51fa301563260ed8b786ede6857d3afd"
}
~~~

## 呼び出し元

- [00bac084](../00bac/00bac084.md)
- [00bac664](../00bac/00bac664.md)
- [00baecf0](../00bae/00baecf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 5203 bytes

~~~c

bool FUN_00bac0ec(long param_1,byte *param_2,long *param_3,long param_4,ushort *param_5,
                 long *param_6,ulong param_7,uint param_8)

{
  uint uVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  ushort *puVar5;
  byte *pbVar6;
  long lVar7;
  uint uVar8;
  ushort *puVar9;
  uint uVar10;
  
  *param_3 = param_1;
  *param_6 = param_4;
  pbVar6 = (byte *)*param_3;
  if (((((param_8 >> 2 & 1) != 0) && (2 < (long)param_2 - (long)pbVar6)) && (*pbVar6 == 0xef)) &&
     ((pbVar6[1] == 0xbb && (pbVar6[2] == 0xbf)))) {
    pbVar6 = pbVar6 + 3;
    *param_3 = (long)pbVar6;
  }
  if (param_2 <= pbVar6) {
    return false;
  }
  puVar5 = (ushort *)*param_6;
  do {
    puVar9 = puVar5;
    if (param_5 <= puVar9) break;
    bVar2 = *pbVar6;
    if (param_7 < bVar2) {
      return (bool)2;
    }
    if ((char)bVar2 < '\0') {
      if (bVar2 < 0xc2) {
        return (bool)2;
      }
                    /* try { // try from 00bac19c to 00cac1a7 has its CatchHandler @ 00bac2e0 */
      uVar8 = (uint)bVar2;
      if (bVar2 < 0xe0) {
                    /* try { // try from 00bac1ac to 00cac1bf has its CatchHandler @ 00bac2c0 */
        if ((long)param_2 - (long)pbVar6 < 2) {
          return true;
        }
        if ((pbVar6[1] & 0xc0) != 0x80) {
          return (bool)2;
        }
                    /* try { // try from 00bac1c0 to 00cac1db has its CatchHandler @ 00bac28c */
        uVar8 = pbVar6[1] & 0x3f | (bVar2 & 0x1f) << 6;
        if (param_7 < uVar8) {
          return (bool)2;
        }
        *puVar9 = (ushort)uVar8;
        pbVar6 = pbVar6 + 2;
      }
      else if (uVar8 < 0xf0) {
        if ((long)param_2 - (long)pbVar6 < 2) {
          return true;
        }
        uVar10 = (uint)pbVar6[1];
        if (uVar8 == 0xed) {
          uVar8 = uVar10 & 0xe0;
joined_r0x00bac254:
          if (uVar8 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar8 != 0xe0) {
            uVar8 = uVar10 & 0xc0;
                    /* try { // try from 00bac260 to 00cac26b has its CatchHandler @ 00bac32c */
            goto joined_r0x00bac254;
          }
          if ((uVar10 & 0xe0) != 0xa0) {
            return (bool)2;
          }
        }
        if ((long)param_2 - (long)pbVar6 == 2) {
          return true;
        }
                    /* try { // try from 00bac280 to 00cac28b has its CatchHandler @ 00bac2f4 */
                    /* catch() { ... } // from try @ 00bac1c0 with catch @ 00bac28c
                       try { // try from 00bac28c to 00cac357 has its CatchHandler @ 00babe04 */
        if (((pbVar6[2] & 0xc0) != 0x80) ||
           (uVar8 = (uVar10 & 0x3f) << 6, uVar10 = pbVar6[2] & 0x3f,
           param_7 < ((uint)bVar2 << 0xc & 0xffc0 | uVar8 | uVar10))) {
          return (bool)2;
        }
        *puVar9 = (ushort)((uint)bVar2 << 0xc) | (ushort)uVar8 | (ushort)uVar10;
        pbVar6 = pbVar6 + 3;
      }
      else {
        if (0xf4 < uVar8) {
          return (bool)2;
        }
        lVar7 = (long)param_2 - (long)pbVar6;
        if (lVar7 < 2) {
          return true;
        }
        bVar3 = pbVar6[1];
        uVar10 = (uint)bVar3;
        if (bVar2 == 0xf4) {
          uVar1 = uVar10 & 0xf0;
joined_r0x00bac2ac:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar8 != 0xf0) {
            uVar1 = uVar10 & 0xc0;
            goto joined_r0x00bac2ac;
          }
          if (0x2f < uVar10 - 0x90) {
            return (bool)2;
          }
        }
                    /* catch() { ... } // from try @ 00bac1ac with catch @ 00bac2c0 */
        if (lVar7 == 2) {
          return true;
        }
        bVar2 = pbVar6[2];
        if ((bVar2 & 0xc0) != 0x80) {
          return (bool)2;
        }
        if (lVar7 == 3) {
          return true;
        }
                    /* catch() { ... } // from try @ 00bac19c with catch @ 00bac2e0 */
        bVar4 = pbVar6[3];
        if ((bVar4 & 0xc0) != 0x80) {
          return (bool)2;
        }
                    /* catch() { ... } // from try @ 00bac280 with catch @ 00bac2f4 */
        if ((long)param_5 - (long)puVar9 < 4) {
          return true;
        }
                    /* catch() { ... } // from try @ 00babfd4 with catch @ 00bac304 */
        if (param_7 < (((ulong)uVar8 & 7) << 0x12 | ((ulong)bVar3 & 0x3f) << 0xc |
                       ((ulong)bVar2 & 0x3f) << 6 | (ulong)bVar4 & 0x3f)) {
          return (bool)2;
        }
                    /* catch() { ... } // from try @ 00bac260 with catch @ 00bac32c */
        puVar9[1] = bVar4 & 0x3f | (bVar2 & 0xf) << 6 | 0xdc00;
        *param_6 = (long)(puVar9 + 1);
        lVar7 = *param_3;
        *puVar9 = ((ushort)((uVar10 & 0xf) << 2) |
                   (ushort)(((uVar8 & 7) << 2 | bVar3 >> 4 & 3) << 6) | bVar2 >> 4 & 3) + 0x3fc0 |
                  0xd800;
        pbVar6 = (byte *)(lVar7 + 4);
      }
    }
    else {
      *puVar9 = (ushort)bVar2;
      pbVar6 = pbVar6 + 1;
    }
    *param_3 = (long)pbVar6;
    lVar7 = *param_6;
    *param_6 = lVar7 + 2;
    pbVar6 = (byte *)*param_3;
    puVar5 = (ushort *)(lVar7 + 2);
  } while (pbVar6 < param_2);
  return param_5 <= puVar9;
}

~~~
