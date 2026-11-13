# 00af7fbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af7fbc",
  "name": "FUN_00af7fbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cfb5d03c98aa7b824a81bc9aed865f62aa6c7eab4fe67df00fe72b074d37c13e",
  "source_text_sha256": "cfb5d03c98aa7b824a81bc9aed865f62aa6c7eab4fe67df00fe72b074d37c13e"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00af7fbc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af7fd8 to 00bf8033 has its CatchHandler @ 00af7e34 */
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84aec) = param_3;
  return;
}

~~~
