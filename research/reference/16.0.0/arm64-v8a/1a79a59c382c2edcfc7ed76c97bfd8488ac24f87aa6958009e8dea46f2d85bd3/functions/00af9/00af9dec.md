# 00af9dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00af9dec",
  "name": "FUN_00af9dec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad57a7239cfd81ad34e91b4a9b1b10c1abe97c2ee91a56b83b95f91f6b0b9d39",
  "source_text_sha256": "ad57a7239cfd81ad34e91b4a9b1b10c1abe97c2ee91a56b83b95f91f6b0b9d39"
}
~~~

## 呼び出し元

- [00713ce4](../00713/00713ce4.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af9dec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84ad8);
}

~~~
