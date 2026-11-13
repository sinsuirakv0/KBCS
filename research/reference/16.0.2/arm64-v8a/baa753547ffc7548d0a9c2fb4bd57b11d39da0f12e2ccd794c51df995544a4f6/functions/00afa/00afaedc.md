# 00afaedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afaedc",
  "name": "FUN_00afaedc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc322cab1fd2c3012636ff1b88f9f3ef96b2bb2af9225699ddb44179c01a9273",
  "source_text_sha256": "cc322cab1fd2c3012636ff1b88f9f3ef96b2bb2af9225699ddb44179c01a9273"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afaedc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b1c) != 0;
}

~~~
