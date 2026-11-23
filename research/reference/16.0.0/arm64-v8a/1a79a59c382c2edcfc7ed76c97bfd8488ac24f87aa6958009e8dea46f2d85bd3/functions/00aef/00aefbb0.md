# 00aefbb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a90784`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90784.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0053.md#compare-dffff552ed9d136769fce556db2308b1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefbb0",
  "name": "FUN_00aefbb0",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a3f92a531927823cc78e2733d1ada6cd3d9517840b85a5542bd57d3d6db2cef",
  "source_text_sha256": "4a3f92a531927823cc78e2733d1ada6cd3d9517840b85a5542bd57d3d6db2cef"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b6f0c](../008b6/008b6f0c.md)
- [00b0b218](../00b0b/00b0b218.md)

## 疑似コード / UTF-8 2778 bytes

~~~c

void FUN_00aefbb0(long param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  long lVar6;
  
                    /* try { // try from 00aefbc0 to 00befbc3 has its CatchHandler @ 00aefc0c */
  iVar1 = *param_3;
  uVar5 = *param_2;
  if (iVar1 == 4) {
    lVar6 = *(long *)(param_1 + 8);
    uVar3 = FUN_008b6f0c(uVar5);
    if ((uVar3 & 1) == 0) {
      return;
    }
                    /* catch() { ... } // from try @ 00aefe00 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00aeff30 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00af00e4 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00af0298 with catch @ 00aefc4c */
    FUN_00b0b218(lVar6 + 0x3d8,*(long *)(param_1 + 0x10),*(long *)(param_1 + 0x10) + 0x510,0);
    return;
  }
                    /* try { // try from 00aefbd4 to 00befbd7 has its CatchHandler @ 00aefc08 */
  if (iVar1 == 3) {
                    /* try { // try from 00aefbe8 to 00befbeb has its CatchHandler @ 00aefc04 */
    uVar2 = FUN_0047acb4();
    uVar3 = FUN_008b6f0c(uVar5);
                    /* try { // try from 00aefbfc to 00befbff has its CatchHandler @ 00aefc00 */
    uVar4 = 0xb;
                    /* catch() { ... } // from try @ 00aefb1c with catch @ 00aefc00
                       catch() { ... } // from try @ 00aefbfc with catch @ 00aefc00
                       try { // try from 00aefc00 to 00befc4b has its CatchHandler @ 00aef744 */
                    /* catch() { ... } // from try @ 00aefaa8 with catch @ 00aefc04
                       catch() { ... } // from try @ 00aefbe8 with catch @ 00aefc04 */
    if ((uVar3 & 1) == 0) {
      uVar4 = 0xf;
    }
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_0047acb4();
    uVar4 = 10;
  }
                    /* catch() { ... } // from try @ 00aef9ac with catch @ 00aefc0c
                       catch() { ... } // from try @ 00aefbc0 with catch @ 00aefc0c */
                    /* catch() { ... } // from try @ 00aef92c with catch @ 00aefc10
                       catch() { ... } // from try @ 00aefbac with catch @ 00aefc10 */
                    /* catch() { ... } // from try @ 00aef8b4 with catch @ 00aefc14
                       catch() { ... } // from try @ 00aefb98 with catch @ 00aefc14 */
                    /* catch() { ... } // from try @ 00aef83c with catch @ 00aefc18
                       catch() { ... } // from try @ 00aefb84 with catch @ 00aefc18 */
                    /* catch() { ... } // from try @ 00aef7c4 with catch @ 00aefc1c
                       catch() { ... } // from try @ 00aefb70 with catch @ 00aefc1c */
  FUN_0047cd94(uVar2,uVar4,0);
  return;
}

~~~
