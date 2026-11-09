# 00aefbb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

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
