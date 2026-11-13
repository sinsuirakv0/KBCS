# 00b3bfbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b3bfbc",
  "name": "FUN_00b3bfbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b",
  "source_text_sha256": "cf81e6170c340491d223c1b0774faca564fa7c34f01db0b4601f01472fbcbb6b"
}
~~~

## 呼び出し元

- [005dbfbc](../005db/005dbfbc.md)
- [006971c0](../00697/006971c0.md)
- [0071e618](../0071e/0071e618.md)
- [008e49f4](../008e4/008e49f4.md)
- [008e5238](../008e5/008e5238.md)

## 呼び出し先

- [005e81d8](../005e8/005e81d8.md)

## 疑似コード / UTF-8 284 bytes

~~~c

void FUN_00b3bfbc(byte *param_1,int param_2)

{
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005e81d8();
  return;
}

~~~
