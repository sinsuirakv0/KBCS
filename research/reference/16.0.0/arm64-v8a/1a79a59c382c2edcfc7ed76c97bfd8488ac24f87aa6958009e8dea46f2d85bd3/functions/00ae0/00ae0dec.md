# 00ae0dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00ae0dec",
  "name": "FUN_00ae0dec",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b5e46ff9d5aae287c454a1b048d54c82af0b68df633822709c6c49effd7b486",
  "source_text_sha256": "8b5e46ff9d5aae287c454a1b048d54c82af0b68df633822709c6c49effd7b486"
}
~~~

## 呼び出し元

- [00ad6d50](../00ad6/00ad6d50.md)

## 呼び出し先

- [009df498](../009df/009df498.md)
- [009e0e24](../009e0/009e0e24.md)
- [009e2df8](../009e2/009e2df8.md)

## 疑似コード / UTF-8 557 bytes

~~~c

void FUN_00ae0dec(long param_1,int param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  undefined4 *puVar3;
  
  uVar1 = FUN_009e0e24(param_1 + 0x50,0xffffffff,0xffffffff);
  if ((uVar1 & 1) == 0) {
    puVar3 = (undefined4 *)(param_1 + (long)param_2 * 4 + 0x49934);
  }
  else {
    lVar2 = FUN_009e2df8(param_1 + 0x50,0xffffffff,0xffffffff);
    if (lVar2 == 0) {
      return;
    }
    lVar2 = FUN_009df498(lVar2,param_2);
    if (lVar2 == 0) {
      return;
    }
    puVar3 = (undefined4 *)(lVar2 + 4);
  }
  *puVar3 = param_3;
  return;
}

~~~
