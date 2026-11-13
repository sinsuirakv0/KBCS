# 00afafb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afafb8",
  "name": "FUN_00afafb8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68f6726607d4113ee6e7987ddc69136267c0ab64ce4c22d9f83a21b3aeece37a",
  "source_text_sha256": "68f6726607d4113ee6e7987ddc69136267c0ab64ce4c22d9f83a21b3aeece37a"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)
- [00a52034](../00a52/00a52034.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afafb8(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00afafec to 00bfaffb has its CatchHandler @ 00afb3b4 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) = param_3 & 1;
                    /* try { // try from 00afaffc to 00bfb03f has its CatchHandler @ 00afac20 */
  return;
}

~~~
