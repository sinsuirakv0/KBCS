# 00bbdd1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbdd1c",
  "name": "FUN_00bbdd1c",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05327dc88c6fb177b473859e41e7b3b9d46a8040d10169ab86318f8f3e8c6b80",
  "source_text_sha256": "05327dc88c6fb177b473859e41e7b3b9d46a8040d10169ab86318f8f3e8c6b80"
}
~~~

## 呼び出し元

- [00bbd308](../00bbd/00bbd308.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbf39c](../00bbf/00bbf39c.md)
- [00bc93c8](../00bc9/00bc93c8.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined1  [16] FUN_00bbdd1c(long *param_1,ulong param_2)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined1 auVar4 [16];
  
  auVar4._0_8_ = (byte *)*param_1;
  pbVar1 = (byte *)param_1[1];
  pbVar2 = auVar4._0_8_;
                    /* try { // try from 00bbdd38 to 00cbdd43 has its CatchHandler @ 00bbe190 */
                    /* try { // try from 00bbdd44 to 00cbdd53 has its CatchHandler @ 00bbe18c */
  if ((((param_2 & 1) != 0) && (auVar4._0_8_ != pbVar1)) && (*auVar4._0_8_ == 0x6e)) {
    pbVar2 = auVar4._0_8_ + 1;
    *param_1 = (long)pbVar2;
  }
  if ((pbVar1 == pbVar2) || (*pbVar2 - 0x3a < 0xfffffff6)) {
                    /* try { // try from 00bbdd78 to 00cbdd83 has its CatchHandler @ 00bbe190 */
    return ZEXT816(0);
  }
  do {
                    /* try { // try from 00bbdd84 to 00cbdd93 has its CatchHandler @ 00bbe18c */
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
