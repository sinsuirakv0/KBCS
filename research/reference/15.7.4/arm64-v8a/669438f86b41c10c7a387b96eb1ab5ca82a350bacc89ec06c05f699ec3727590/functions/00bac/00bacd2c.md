# 00bacd2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bacce8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00bacce8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/detail_skipped-0023.md#compare-ef782359a59c81f650a1cf80c6d95f89)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
