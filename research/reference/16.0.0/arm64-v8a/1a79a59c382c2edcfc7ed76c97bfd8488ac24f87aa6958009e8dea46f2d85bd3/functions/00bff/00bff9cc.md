# 00bff9cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bff9cc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c",
  "source_text_sha256": "d9c62fb3932e93eed1441149527fdad124489992bb30cc6927657248217a277c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e90](../00c57/00c57e90.md)
- [00c5a3d0](../00c5a/00c5a3d0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

## 疑似コード / UTF-8 1299 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  undefined1 auStack_28 [8];
  
  _ZNSt6__ndk16localeC1ERKS0_(auStack_28,param_1 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  _ZNSt6__ndk16localeaSERKS0_(param_2 + 8,auStack_28);
  _ZNSt6__ndk16localeD1Ev(auStack_28);
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *(undefined8 *)(param_1 + 0x10) = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_2 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x18);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_2 + 0x18) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x20);
  *(undefined8 *)(param_1 + 0x20) = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_2 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x28);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_2 + 0x28) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x30);
  *(undefined8 *)(param_1 + 0x30) = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_2 + 0x30) = uVar1;
  uVar1 = *(undefined8 *)(param_1 + 0x38);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_2 + 0x38) = uVar1;
  return;
}

~~~
