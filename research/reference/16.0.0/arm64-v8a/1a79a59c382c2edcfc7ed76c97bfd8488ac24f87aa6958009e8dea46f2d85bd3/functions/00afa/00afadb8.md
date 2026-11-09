# 00afadb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afadb8",
  "name": "FUN_00afadb8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "706c7915da66015fa2a9f8df68d926e75d6fe29255a4bea80cc1455b37837cf4",
  "source_text_sha256": "706c7915da66015fa2a9f8df68d926e75d6fe29255a4bea80cc1455b37837cf4"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)
- [00a51dcc](../00a51/00a51dcc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00afadb8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b5c) = param_3;
                    /* try { // try from 00afadfc to 00bfae0b has its CatchHandler @ 00afb1c4 */
  return;
}

~~~
