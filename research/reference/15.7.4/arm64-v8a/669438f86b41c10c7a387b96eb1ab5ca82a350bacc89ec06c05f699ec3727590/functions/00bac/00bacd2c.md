# 00bacd2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bacc20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bac/00bacc20.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bacd2c",
  "name": "FUN_00bacd2c",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0ac4bbfd68c02383eab12320141fc0e3bb1096f398c26ed357e1bffe81be020",
  "source_text_sha256": "f0ac4bbfd68c02383eab12320141fc0e3bb1096f398c26ed357e1bffe81be020"
}
~~~

## 呼び出し元

- [00bacd10](../00bac/00bacd10.md)
- [00bad100](../00bad/00bad100.md)
- [00bad230](../00bad/00bad230.md)
- [00bad7c0](../00bad/00bad7c0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 3197 bytes

~~~c

int FUN_00bacd2c(byte *param_1,byte *param_2,ulong param_3,ulong param_4,uint param_5)

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
                    /* try { // try from 00bacd90 to 00cace8b has its CatchHandler @ 00bacd90
                       catch() { ... } // from try @ 00bacd90 with catch @ 00bacd90
                       catch() { ... } // from try @ 00bacef4 with catch @ 00bacd90
                       catch() { ... } // from try @ 00bacf84 with catch @ 00bacd90 */
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
LAB_00bace78:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xe0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00bace78;
            }
            if ((uVar7 & 0xe0) != 0xa0) break;
          }
                    /* try { // try from 00bace8c to 00cace97 has its CatchHandler @ 00bad074 */
                    /* try { // try from 00bace9c to 00caceaf has its CatchHandler @ 00bad054 */
          if (((pbVar3[2] & 0xc0) != 0x80) ||
             (param_4 < ((uVar5 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar3[2] & 0x3f))) break;
          lVar6 = 3;
        }
        else {
          if ((0xf4 < bVar1) || ((long)param_2 - (long)pbVar3 < 4)) break;
          uVar7 = (uint)pbVar3[1];
          if (uVar5 == 0xf4) {
            uVar8 = uVar7 & 0xf0;
LAB_00baceb4:
            if (uVar8 != 0x80) break;
          }
          else {
            if (uVar5 != 0xf0) {
              uVar8 = uVar7 & 0xc0;
              goto LAB_00baceb4;
            }
            if (0x2f < uVar7 - 0x90) break;
          }
                    /* try { // try from 00baced0 to 00cacef3 has its CatchHandler @ 00bad084 */
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
                    /* try { // try from 00bacef4 to 00cacf33 has its CatchHandler @ 00bacd90 */
      if ((param_2 <= pbVar3) || (bVar2 = param_3 <= uVar4, uVar4 = uVar4 + 1, bVar2)) break;
    } while( true );
  }
  return (int)pbVar3 - (int)param_1;
}

~~~
