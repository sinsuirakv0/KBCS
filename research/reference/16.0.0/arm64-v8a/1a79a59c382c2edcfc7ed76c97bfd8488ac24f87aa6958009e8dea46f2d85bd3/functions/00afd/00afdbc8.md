# 00afdbc8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afdbc8",
  "name": "FUN_00afdbc8",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f3cbfaca8e3bdf815fe4efeace16e500eef2685b71b65c3a888bab9b718544d3",
  "source_text_sha256": "f3cbfaca8e3bdf815fe4efeace16e500eef2685b71b65c3a888bab9b718544d3"
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afdbc8(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c94);
}

~~~
