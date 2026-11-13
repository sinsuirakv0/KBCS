# 00afc0ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afc0ec",
  "name": "FUN_00afc0ec",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f09bcdb535ae0ef8f847b593e03a53678e10f48b14fbe32e8e9ecf79ba78e429",
  "source_text_sha256": "f09bcdb535ae0ef8f847b593e03a53678e10f48b14fbe32e8e9ecf79ba78e429"
}
~~~

## 呼び出し元

- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 307 bytes

~~~c

void FUN_00afc0ec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a5c) = 0;
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a60) = 1;
  return;
}

~~~
