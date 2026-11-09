# 00bfb6ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bfb6ac",
  "name": "_ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f",
  "source_text_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f"
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c58100](../00c58/00c58100.md)

## 疑似コード / UTF-8 360 bytes

~~~c

ulong _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 4;
  if ((*(byte *)(param_1 + 0x24) >> 2 & 1) == 0) {
    return param_1;
  }
  uVar1 = __cxa_rethrow();
  uVar2 = (ulong)DAT_00ca4408;
  DAT_00ca4408 = uVar1;
  return uVar2;
}

~~~
