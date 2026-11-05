# 00bace3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bace3c.md)

## 関数情報

~~~json
{
  "address": "00bace3c",
  "name": "_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE6do_outERS1_PKDiS5_RS5_PDuS7_RS7_",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a1dd0a0e081dd03e6553c6b5f1ecfb9f01d5158f72fbbf3ffa1acba62193a19",
  "source_text_sha256": "1a1dd0a0e081dd03e6553c6b5f1ecfb9f01d5158f72fbbf3ffa1acba62193a19"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 2016 bytes

~~~c

undefined8
_ZNKSt6__ndk17codecvtIDiDu9mbstate_tE6do_outERS1_PKDiS5_RS5_PDuS7_RS7_
          (undefined8 param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  uint uVar1;
  byte bVar2;
  undefined8 uVar3;
  byte *pbVar4;
  
  do {
    if (param_4 <= param_3) {
      uVar3 = 0;
                    /* catch() { ... } // from try @ 00bacd90 with catch @ 00bacf48 */
LAB_00bacf58:
                    /* catch() { ... } // from try @ 00bace28 with catch @ 00bacf58 */
      *param_5 = param_3;
      *param_8 = param_6;
      return uVar3;
    }
    uVar1 = *param_3;
    if (0x10 < uVar1 >> 0x10 || (uVar1 & 0xfffff800) == 0xd800) {
      uVar3 = 2;
      goto LAB_00bacf58;
    }
                    /* try { // try from 00bace78 to 00cad07b has its CatchHandler @ 00bacc84 */
    bVar2 = (byte)uVar1;
    if (uVar1 < 0x80) {
      if (param_7 - (long)param_6 < 1) goto LAB_00bacf54;
      pbVar4 = param_6 + 1;
      *param_6 = bVar2;
    }
    else if (uVar1 < 0x800) {
      if (param_7 - (long)param_6 < 2) goto LAB_00bacf54;
      pbVar4 = param_6 + 2;
      *param_6 = (byte)(uVar1 >> 6) | 0xc0;
      param_6[1] = bVar2 & 0x3f | 0x80;
    }
    else if (uVar1 >> 0x10 == 0) {
      if (param_7 - (long)param_6 < 3) {
LAB_00bacf54:
        uVar3 = 1;
        goto LAB_00bacf58;
      }
      pbVar4 = param_6 + 3;
      *param_6 = (byte)(uVar1 >> 0xc) | 0xe0;
      param_6[1] = (byte)(uVar1 >> 6) & 0x3f | 0x80;
      param_6[2] = bVar2 & 0x3f | 0x80;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00bacf54;
      pbVar4 = param_6 + 4;
      *param_6 = (byte)(uVar1 >> 0x12) | 0xf0;
      param_6[1] = (byte)(uVar1 >> 0xc) & 0x3f | 0x80;
      param_6[2] = (byte)(uVar1 >> 6) & 0x3f | 0x80;
      param_6[3] = bVar2 & 0x3f | 0x80;
    }
                    /* try { // try from 00bace54 to 00cace77 has its CatchHandler @ 00bacff8 */
    param_3 = param_3 + 1;
    param_6 = pbVar4;
  } while( true );
}

~~~
