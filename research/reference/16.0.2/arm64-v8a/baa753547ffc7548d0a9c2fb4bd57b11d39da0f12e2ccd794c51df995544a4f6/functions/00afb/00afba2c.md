# 00afba2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afba2c",
  "name": "FUN_00afba2c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7d92ab254f0fecad4d40b39a270aeac1934392f7a53392bf7ce27ca044d9ddaf",
  "source_text_sha256": "7d92ab254f0fecad4d40b39a270aeac1934392f7a53392bf7ce27ca044d9ddaf"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00afba2c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afba30 to 00bfba3b has its CatchHandler @ 00afcae8 */
                    /* try { // try from 00afba3c to 00bfba7b has its CatchHandler @ 00afb4a0 */
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c2c) = param_3;
  return;
}

~~~
