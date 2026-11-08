# 00bacce8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bacce8",
  "name": "FUN_00bacce8",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00384c0eaf2ff263f49e87a7b7e91a7610b3ba9e6988300c75e1faa53a7755e0",
  "source_text_sha256": "00384c0eaf2ff263f49e87a7b7e91a7610b3ba9e6988300c75e1faa53a7755e0"
}
~~~

## 呼び出し元

- [00bacccc](../00bac/00bacccc.md)
- [00bad0bc](../00bad/00bad0bc.md)
- [00bad1ec](../00bad/00bad1ec.md)
- [00bad77c](../00bad/00bad77c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3197 bytes

~~~c

int FUN_00bacce8(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

{
  byte bVar1;
  bool bVar2;
  byte *pbVar3;
  ulong uVar4;
  uint uVar5;
  long lVar6;
  uint uVar7;
  uint uVar8;
  
  pbVar3 = param_1;
  if ((((2 < (long)param_2 - (long)param_1) && ((param_5 >> 2 & 1) != 0)) && (*param_1 == 0xef)) &&
     (param_1[1] == 0xbb)) {
    lVar6 = 3;
    if (param_1[2] != 0xbf) {
      lVar6 = 0;
    }
    pbVar3 = param_1 + lVar6;
  }
  if ((pbVar3 < param_2) && (param_3 != 0)) {
    uVar4 = 1;
    do {
      bVar1 = *pbVar3;
                    /* try { // try from 00bacd4c to 00cace47 has its CatchHandler @ 00bacd4c
                       catch() { ... } // from try @ 00bacd4c with catch @ 00bacd4c
                       catch() { ... } // from try @ 00baceb0 with catch @ 00bacd4c
                       catch() { ... } // from try @ 00bacf40 with catch @ 00bacd4c */
      if ((char)bVar1 < '\0') {
        if (bVar1 < 0xc2) break;
        uVar5 = (uint)bVar1;
        if (bVar1 < 0xe0) {
          if ((((long)param_2 - (long)pbVar3 < 2) || ((pbVar3[1] & 0xc0) != 0x80)) ||
             (param_4 < (pbVar3[1] & 0x3f | (uVar5 & 0x1f) << 6))) break;
          lVar6 = 2;
        }
        else if (bVar1 < 0xf0) {
          if ((long)param_2 - (long)pbVar3 < 3) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xed) {
            uVar8 = uVar7 & 0xe0;
LAB_00bace34:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace34;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
                    /* try { // try from 00bace48 to 00cace53 has its CatchHandler @ 00bad030 */
                    /* try { // try from 00bace58 to 00cace6b has its CatchHandler @ 00bad010 */
          if (((pbVar3[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar5 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar3[2] & 0x3f))) break;
          lVar6 = 3;
        }
        else {
          if ((0xf4 < bVar1) || ((long)param_2 - (long)pbVar3 < 4)) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xf4) {
            uVar8 = uVar7 & 0xf0;
LAB_00bace70:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xf0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace70;
            }
            if (0x2f < uVar7 - 0x90) break;
          }
                    /* try { // try from 00bace8c to 00caceaf has its CatchHandler @ 00bad040 */
          if ((((pbVar3[2] & 0xc0) != 0x80) || ((pbVar3[3] & 0xc0) != 0x80)) ||
             (param_4 < ((uVar5 & 7) << 0x12 | (uVar7 & 0x3f) << 0xc | (pbVar3[2] & 0x3f) << 6 |
                        pbVar3[3] & 0x3f))) break;
          lVar6 = 4;
        }
      }
      else {
        if (param_4 < bVar1) break;
        lVar6 = 1;
      }
      pbVar3 = pbVar3 + lVar6;
                    /* try { // try from 00baceb0 to 00caceef has its CatchHandler @ 00bacd4c */
      if ((param_2 <= pbVar3) || (bVar2 = param_3 <= uVar4, uVar4 = uVar4 + 1, bVar2)) break;
    } while( true );
  }
  return (int)pbVar3 - (int)param_1;
}

~~~
