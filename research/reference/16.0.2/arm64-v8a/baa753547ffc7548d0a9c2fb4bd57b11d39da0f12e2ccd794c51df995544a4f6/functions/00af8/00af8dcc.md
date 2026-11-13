# 00af8dcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af8dcc",
  "name": "FUN_00af8dcc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7bebeffcaa2f4a72a75a48a85c0bcccc9f16152c6db36a92acb5e244b1db8256",
  "source_text_sha256": "7bebeffcaa2f4a72a75a48a85c0bcccc9f16152c6db36a92acb5e244b1db8256"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)
- [00af3590](../00af3/00af3590.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af8dcc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00af8e00 to 00bf8e03 has its CatchHandler @ 00af9224 */
                    /* try { // try from 00af8e04 to 00bf8e6b has its CatchHandler @ 00af8d00 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84990) = param_3;
  return;
}

~~~
