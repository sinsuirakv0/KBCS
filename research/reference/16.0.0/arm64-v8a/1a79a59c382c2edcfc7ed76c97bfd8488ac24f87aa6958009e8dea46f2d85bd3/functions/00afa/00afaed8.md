# 00afaed8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afaed8",
  "name": "FUN_00afaed8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6404f5f907fc188b6cc40f80a73dfb348b173ba21005d2f43609bcd6a5f20f7c",
  "source_text_sha256": "6404f5f907fc188b6cc40f80a73dfb348b173ba21005d2f43609bcd6a5f20f7c"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afaed8(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afaeec to 00bfaf07 has its CatchHandler @ 00afb228 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afaf08 to 00bfaf97 has its CatchHandler @ 00afaa30 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b90) = param_3 & 1;
  return;
}

~~~
