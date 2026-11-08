# 00acf8cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acf8cc",
  "name": "FUN_00acf8cc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "61796864e70a63628a6cf55c3b7ddf5559f4e0bc6258f5e99a12260b198a32e9",
  "source_text_sha256": "61796864e70a63628a6cf55c3b7ddf5559f4e0bc6258f5e99a12260b198a32e9"
}
~~~

## 呼び出し元

- [005e53dc](../005e5/005e53dc.md)
- [0063e818](../0063e/0063e818.md)
- [0063e8b4](../0063e/0063e8b4.md)
- [0063ea04](../0063e/0063ea04.md)
- [006e34b0](../006e3/006e34b0.md)
- [006fd890](../006fd/006fd890.md)
- [00733374](../00733/00733374.md)
- [0073a8e0](../0073a/0073a8e0.md)
- [008e0bc0](../008e0/008e0bc0.md)
- [008e68f8](../008e6/008e68f8.md)
- [0092bc08](../0092b/0092bc08.md)
- [00934148](../00934/00934148.md)
- [00947d70](../00947/00947d70.md)
- [0094847c](../00948/0094847c.md)
- [00965df0](../00965/00965df0.md)
- [00999d28](../00999/00999d28.md)
- [009f4a74](../009f4/009f4a74.md)
- [00a82394](../00a82/00a82394.md)

## 呼び出し先

- [00adc050](../00adc/00adc050.md)

## 疑似コード / UTF-8 140 bytes

~~~c

ushort FUN_00acf8cc(void)

{
  ushort uVar1;
  
  uVar1 = FUN_00adc050();
  if (49999 < uVar1) {
    uVar1 = 50000;
  }
  return uVar1;
}

~~~
