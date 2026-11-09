# 00afbd2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afbd2c",
  "name": "FUN_00afbd2c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea2876587d6fcd8fee68eaee0feab41636cf2ad45df78108e8bba3b15f9edb6a",
  "source_text_sha256": "ea2876587d6fcd8fee68eaee0feab41636cf2ad45df78108e8bba3b15f9edb6a"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00afbd2c(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afbd54 to 00bfbd57 has its CatchHandler @ 00afca14 */
                    /* try { // try from 00afbd58 to 00bfbe97 has its CatchHandler @ 00afb2b0 */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b24) = param_3;
  return;
}

~~~
