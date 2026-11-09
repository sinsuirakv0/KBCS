# 00afb4dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afb4dc",
  "name": "FUN_00afb4dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06",
  "source_text_sha256": "ed5f1eb3c4adea43fc06bc09e94993e7e7ed0c7dbc0044a9253965ec22bbfd06"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 403 bytes

~~~c

void FUN_00afb4dc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afb4f4 to 00bfb4ff has its CatchHandler @ 00afc9b4 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afb500 to 00bfb513 has its CatchHandler @ 00afc994 */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b8) = param_3 & 1;
  return;
}

~~~
