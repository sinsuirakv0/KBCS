# 00afacd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afacd4",
  "name": "FUN_00afacd4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fdc74426ceb3943c85c92dc839e183f83ef14688e7fe7f392f4a9449419a3f05",
  "source_text_sha256": "fdc74426ceb3943c85c92dc839e183f83ef14688e7fe7f392f4a9449419a3f05"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afacd4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afacd4 to 00bfacf7 has its CatchHandler @ 00afac20 */
  lVar1 = FUN_00851550();
                    /* try { // try from 00afacf8 to 00bfad0f has its CatchHandler @ 00afb404 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a2c) = param_3 & 1;
  return;
}

~~~
