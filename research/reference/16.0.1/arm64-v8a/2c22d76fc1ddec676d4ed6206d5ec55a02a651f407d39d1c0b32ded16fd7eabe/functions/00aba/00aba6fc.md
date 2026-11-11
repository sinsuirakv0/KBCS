# 00aba6fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aba6fc",
  "name": "FUN_00aba6fc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97eaf635c28f3406172d3a413bf794c29af4aa8dcf067db01133c67460621767",
  "source_text_sha256": "97eaf635c28f3406172d3a413bf794c29af4aa8dcf067db01133c67460621767"
}
~~~

## 呼び出し元

- [005fe66c](../005fe/005fe66c.md)
- [00605254](../00605/00605254.md)
- [007bda44](../007bd/007bda44.md)
- [007caac8](../007ca/007caac8.md)
- [007df0e8](../007df/007df0e8.md)
- [007efca8](../007ef/007efca8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)
- [00b3e410](../00b3e/00b3e410.md)

## 疑似コード / UTF-8 121 bytes

~~~c

void FUN_00aba6fc(void)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  FUN_00b3e410(lVar1 + 0x2350,0xa1);
  return;
}

~~~
