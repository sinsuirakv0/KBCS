# 00afbcd8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afbcd8",
  "name": "FUN_00afbcd8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f52fed429aa2388891a26de79ab0f6dd4ef3c7c08a91a974e420d1a2b160aa16",
  "source_text_sha256": "f52fed429aa2388891a26de79ab0f6dd4ef3c7c08a91a974e420d1a2b160aa16"
}
~~~

## 呼び出し元

- [005f2d28](../005f2/005f2d28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 345 bytes

~~~c

void FUN_00afbcd8(int param_1,int param_2,int param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbcd8 to 00bfbceb has its CatchHandler @ 00afcadc */
  lVar1 = FUN_008514b8();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84b20) = *(int *)(lVar1 + 0x84b20) + param_3;
  return;
}

~~~
