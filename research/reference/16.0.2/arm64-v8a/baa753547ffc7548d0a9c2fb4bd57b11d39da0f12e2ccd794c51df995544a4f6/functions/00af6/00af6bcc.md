# 00af6bcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af6bcc",
  "name": "FUN_00af6bcc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "995cd0bf51d1088d7c8d260d8c9b94f7cbd69ed0c694f8f98c25ccc50df7c55a",
  "source_text_sha256": "995cd0bf51d1088d7c8d260d8c9b94f7cbd69ed0c694f8f98c25ccc50df7c55a"
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00711a48](../00711/00711a48.md)
- [00af5d2c](../00af5/00af5d2c.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00af6bcc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_00851550();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b10) != 0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
