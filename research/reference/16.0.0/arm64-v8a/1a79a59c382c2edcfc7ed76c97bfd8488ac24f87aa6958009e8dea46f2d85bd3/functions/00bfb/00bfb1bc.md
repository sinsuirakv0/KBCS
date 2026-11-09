# 00bfb1bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfb1bc",
  "name": "_ZNSt6__ndk18ios_base4initEPv",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acde8554ac3feef665b92a85df4419b1a07d924ab4dfc455ec64c78821db8f40",
  "source_text_sha256": "acde8554ac3feef665b92a85df4419b1a07d924ab4dfc455ec64c78821db8f40"
}
~~~

## 呼び出し元

- [00c57de0](../00c57/00c57de0.md)

## 呼び出し先

- [00c5a3a0](../00c5a/00c5a3a0.md)

## 疑似コード / UTF-8 948 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNSt6__ndk18ios_base4initEPv(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  uVar2 = _UNK_002c2ff8;
  uVar1 = _DAT_002c2ff0;
  *(long *)(param_1 + 0x28) = param_2;
  *(uint *)(param_1 + 0x20) = (uint)(param_2 == 0);
  *(undefined4 *)(param_1 + 0x24) = 0;
  *(undefined8 *)(param_1 + 0x18) = uVar2;
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  *(undefined4 *)(param_1 + 8) = 0x1002;
  *(undefined8 *)(param_1 + 0x40) = 0;
  *(undefined8 *)(param_1 + 0x38) = 0;
  *(undefined8 *)(param_1 + 0x50) = 0;
  *(undefined8 *)(param_1 + 0x48) = 0;
  *(undefined8 *)(param_1 + 0x60) = 0;
  *(undefined8 *)(param_1 + 0x58) = 0;
  *(undefined8 *)(param_1 + 0x70) = 0;
  *(undefined8 *)(param_1 + 0x68) = 0;
  *(undefined8 *)(param_1 + 0x80) = 0;
  *(undefined8 *)(param_1 + 0x78) = 0;
  _ZNSt6__ndk16localeC2Ev(param_1 + 0x30);
  return;
}

~~~
