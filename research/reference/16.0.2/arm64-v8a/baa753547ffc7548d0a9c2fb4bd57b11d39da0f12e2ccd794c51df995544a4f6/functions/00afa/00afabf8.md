# 00afabf8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afabf8",
  "name": "FUN_00afabf8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aa148c940043701189718dee88172aca95e88d4c911a84a666867c3593926668",
  "source_text_sha256": "aa148c940043701189718dee88172aca95e88d4c911a84a666867c3593926668"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 952 bytes

~~~c

bool FUN_00afabf8(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00afac20 to 00bfacbb has its CatchHandler @ 00afac20
                       catch() { ... } // from try @ 00afac20 with catch @ 00afac20
                       catch() { ... } // from try @ 00afacd4 with catch @ 00afac20
                       catch() { ... } // from try @ 00afad94 with catch @ 00afac20
                       catch() { ... } // from try @ 00afae60 with catch @ 00afac20
                       catch() { ... } // from try @ 00afaffc with catch @ 00afac20
                       catch() { ... } // from try @ 00afb04c with catch @ 00afac20
                       catch() { ... } // from try @ 00afb0f8 with catch @ 00afac20
                       catch() { ... } // from try @ 00afb1d4 with catch @ 00afac20 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a28) != 0;
}

~~~
