# 00afc6ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afc6ac",
  "name": "FUN_00afc6ac",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59988d865a148fd6822487b1390e2d5d497944689e9c637f39a66f68fe2a19cf",
  "source_text_sha256": "59988d865a148fd6822487b1390e2d5d497944689e9c637f39a66f68fe2a19cf"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [0070eab4](../0070e/0070eab4.md)
- [00711a48](../00711/00711a48.md)
- [00715558](../00715/00715558.md)
- [00716de8](../00716/00716de8.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afc6ac(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b60) = param_3 & 1;
  return;
}

~~~
