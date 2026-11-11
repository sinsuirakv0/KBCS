# 00bfbaa8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bfbaa8",
  "name": "_ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727",
  "source_text_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727"
}
~~~

## 呼び出し元

- [00c582c0](../00c58/00c582c0.md)

## 呼び出し先

- [00c58500](../00c58/00c58500.md)

## 疑似コード / UTF-8 509 bytes

~~~c

ulong _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 1;
  if ((*(byte *)(param_1 + 0x24) & 1) == 0) {
    return param_1;
  }
  uVar2 = __cxa_rethrow();
  *(uint *)(uVar2 + 0x20) = *(uint *)(uVar2 + 0x20) | 4;
  if ((*(byte *)(uVar2 + 0x24) >> 2 & 1) == 0) {
    return uVar2;
  }
  uVar1 = __cxa_rethrow();
  uVar2 = (ulong)DAT_00ca4808;
  DAT_00ca4808 = uVar1;
  return uVar2;
}

~~~
