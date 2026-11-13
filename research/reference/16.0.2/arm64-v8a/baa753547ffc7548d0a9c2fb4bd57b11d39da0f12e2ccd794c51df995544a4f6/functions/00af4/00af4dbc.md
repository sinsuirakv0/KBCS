# 00af4dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af4dbc",
  "name": "FUN_00af4dbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5bb030ba65ca1830bcaff4a288e88813d028473469741a4763e7f55da8c74f17",
  "source_text_sha256": "5bb030ba65ca1830bcaff4a288e88813d028473469741a4763e7f55da8c74f17"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)
- [00a52034](../00a52/00a52034.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00af4dbc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a94) = param_3;
  return;
}

~~~
