# 00af4fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af4fdc",
  "name": "FUN_00af4fdc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "692a798fd25675e838ca81b367e63f2b422323a4d8ed217efce5fa9e7b18ccc4",
  "source_text_sha256": "692a798fd25675e838ca81b367e63f2b422323a4d8ed217efce5fa9e7b18ccc4"
}
~~~

## 呼び出し元

- [0066b684](../0066b/0066b684.md)
- [00716a50](../00716/00716a50.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 508 bytes

~~~c

void FUN_00af4fdc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af4fdc to 00bf4fe3 has its CatchHandler @ 00af51c8 */
                    /* try { // try from 00af4fe4 to 00bf4ffb has its CatchHandler @ 00af51dc */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00af4ffc to 00bf5043 has its CatchHandler @ 00af51e4 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848f0) = param_3;
  return;
}

~~~
