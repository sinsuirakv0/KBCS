# 00af8eec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af8eec",
  "name": "FUN_00af8eec",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "438fab30a90a44cda0c84671c96f12011c27f349ed5725e4655fe1bc832807ea",
  "source_text_sha256": "438fab30a90a44cda0c84671c96f12011c27f349ed5725e4655fe1bc832807ea"
}
~~~

## 呼び出し元

- [00713d7c](../00713/00713d7c.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00af8eec(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84998);
}

~~~
