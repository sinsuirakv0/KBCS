# 00afaf6c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afaf6c",
  "name": "FUN_00afaf6c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa29c11bb3b1867eca8f6824da7c915fba759b2b19e657af379d68eebea812e6",
  "source_text_sha256": "fa29c11bb3b1867eca8f6824da7c915fba759b2b19e657af379d68eebea812e6"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afaf6c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afaf98 to 00bfaf9b has its CatchHandler @ 00afb240 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b94) = param_3 & 1;
  return;
}

~~~
