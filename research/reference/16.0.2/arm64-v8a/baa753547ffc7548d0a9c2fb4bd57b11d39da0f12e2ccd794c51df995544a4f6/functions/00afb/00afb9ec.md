# 00afb9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afb9ec",
  "name": "FUN_00afb9ec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b317c855b1b7276e59551d09efce45291c64bfefcba2a64fac37b7a410f8cdc5",
  "source_text_sha256": "b317c855b1b7276e59551d09efce45291c64bfefcba2a64fac37b7a410f8cdc5"
}
~~~

## 呼び出し元

- [00715558](../00715/00715558.md)
- [00716de8](../00716/00716de8.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afb9ec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c2c);
}

~~~
