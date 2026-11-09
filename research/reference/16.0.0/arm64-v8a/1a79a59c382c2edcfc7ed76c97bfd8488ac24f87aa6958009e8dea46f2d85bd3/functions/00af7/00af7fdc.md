# 00af7fdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af7fdc",
  "name": "FUN_00af7fdc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e390f4dbb6af2ba71b3a23792b8b149feb32171f0c859ff8a7568f92a78ff83",
  "source_text_sha256": "4e390f4dbb6af2ba71b3a23792b8b149feb32171f0c859ff8a7568f92a78ff83"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00af7fdc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00af7ff0 to 00bf7ff3 has its CatchHandler @ 00af83f4 */
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b8c) = param_3;
                    /* try { // try from 00af8018 to 00bf803b has its CatchHandler @ 00af8358 */
  return;
}

~~~
