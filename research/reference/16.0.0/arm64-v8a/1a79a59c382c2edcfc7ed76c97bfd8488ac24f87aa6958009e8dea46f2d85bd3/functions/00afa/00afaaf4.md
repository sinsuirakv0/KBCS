# 00afaaf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afaaf4",
  "name": "FUN_00afaaf4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35e2efa5d1d9d37a4f47b821ab51a3e86a6485294542108048c2c4465645a6ee",
  "source_text_sha256": "35e2efa5d1d9d37a4f47b821ab51a3e86a6485294542108048c2c4465645a6ee"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)
- [00a51dcc](../00a51/00a51dcc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afaaf4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afab08 to 00bfab1f has its CatchHandler @ 00afb214 */
  lVar1 = FUN_008514b8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) = param_3 & 1;
  return;
}

~~~
