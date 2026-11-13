# 00afac8c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afac8c",
  "name": "FUN_00afac8c",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d305724967ad2b31e3b67658635851cc4a22a1d1cc57ef84283c566cb8421dfe",
  "source_text_sha256": "d305724967ad2b31e3b67658635851cc4a22a1d1cc57ef84283c566cb8421dfe"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 280 bytes

~~~c

bool FUN_00afac8c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00afacbc to 00bfacd3 has its CatchHandler @ 00afb408 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a2c) != 0;
}

~~~
