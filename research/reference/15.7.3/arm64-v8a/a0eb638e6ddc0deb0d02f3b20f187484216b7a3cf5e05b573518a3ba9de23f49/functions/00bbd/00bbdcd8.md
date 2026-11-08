# 00bbdcd8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbdcd8",
  "name": "FUN_00bbdcd8",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eff7d43d021d0ad2a702d57539234b2e499b2b859ff011d2bee5709c6102af2c",
  "source_text_sha256": "eff7d43d021d0ad2a702d57539234b2e499b2b859ff011d2bee5709c6102af2c"
}
~~~

## 呼び出し元

- [00bbd2c4](../00bbd/00bbd2c4.md)
- [00bbde18](../00bbd/00bbde18.md)
- [00bbf358](../00bbf/00bbf358.md)
- [00bc9384](../00bc9/00bc9384.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined1  [16] FUN_00bbdcd8(long *param_1,ulong param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined1 auVar4 [16];
  
  auVar4._0_8_ = (byte *)*param_1;
  pbVar1 = (byte *)param_1[1];
  pbVar2 = auVar4._0_8_;
                    /* try { // try from 00bbdcf4 to 00cbdcff has its CatchHandler @ 00bbe14c */
                    /* try { // try from 00bbdd00 to 00cbdd0f has its CatchHandler @ 00bbe148 */
  if ((((param_2 & 1) != 0) && (auVar4._0_8_ != pbVar1)) && (*auVar4._0_8_ == 0x6e)) {
    pbVar2 = auVar4._0_8_ + 1;
    *param_1 = (long)pbVar2;
  }
  if ((pbVar1 == pbVar2) || (*pbVar2 - 0x3a < 0xfffffff6)) {
                    /* try { // try from 00bbdd34 to 00cbdd3f has its CatchHandler @ 00bbe14c */
    return ZEXT816(0);
  }
  do {
                    /* try { // try from 00bbdd40 to 00cbdd4f has its CatchHandler @ 00bbe148 */
    pbVar3 = pbVar2;
    if (*pbVar2 - 0x3a < 0xfffffff6) break;
    pbVar2 = pbVar2 + 1;
    *param_1 = (long)pbVar2;
    pbVar3 = pbVar1;
  } while (pbVar2 != pbVar1);
  auVar4._8_8_ = (long)pbVar3 - (long)auVar4._0_8_;
  return auVar4;
}

~~~
