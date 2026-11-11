# 00bffdf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bffdf4",
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

- [00c58290](../00c58/00c58290.md)
- [00c5a7d0](../00c5a/00c5a7d0.md)
- [00c5e2e0](../00c5e/00c5e2e0.md)

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
