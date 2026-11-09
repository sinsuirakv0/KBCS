# 00af4efc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af4efc",
  "name": "FUN_00af4efc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a493ef86905fa8d326a4254f092e4cdec54eb2f4d396fd62ac6535df9c8bb22",
  "source_text_sha256": "8a493ef86905fa8d326a4254f092e4cdec54eb2f4d396fd62ac6535df9c8bb22"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 442 bytes

~~~c

void FUN_00af4efc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00af4f08 to 00bf4f0b has its CatchHandler @ 00af5168 */
                    /* try { // try from 00af4f0c to 00bf4f7b has its CatchHandler @ 00af4e08 */
  lVar1 = FUN_008514b8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x848e8) = *(int *)(lVar1 + 0x848e8) + param_3;
  return;
}

~~~
