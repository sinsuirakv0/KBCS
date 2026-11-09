# 00b2bffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b2bffc",
  "name": "FUN_00b2bffc",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64",
  "source_text_sha256": "0b3bda01d92781a8ce4f070c697c64b6484d112e668ed2f6307af88f11cdcb64"
}
~~~

## 呼び出し元

- [0043b618](../0043b/0043b618.md)

## 呼び出し先

- [0043e90c](../0043e/0043e90c.md)
- [0043f4f4](../0043f/0043f4f4.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047b78c](../0047b/0047b78c.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 202 bytes

~~~c

void FUN_00b2bffc(void)

{
  long *plVar1;
  
  plVar1 = (long *)FUN_008514b8();
  (**(code **)(*plVar1 + 0x28))();
  FUN_0047acb4();
  FUN_0047b78c();
  FUN_0043e90c();
  FUN_0043f4f4();
  return;
}

~~~
