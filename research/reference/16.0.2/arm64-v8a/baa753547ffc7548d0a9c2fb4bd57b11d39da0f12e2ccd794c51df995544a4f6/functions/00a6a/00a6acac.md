# 00a6acac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00a6acac",
  "name": "FUN_00a6acac",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929",
  "source_text_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929"
}
~~~

## 呼び出し元

- [007ccf44](../007cc/007ccf44.md)
- [009d7bd0](../009d7/009d7bd0.md)
- [00a47f54](../00a47/00a47f54.md)

## 呼び出し先

- [005e08f0](../005e0/005e08f0.md)

## 疑似コード / UTF-8 230 bytes

~~~c

void FUN_00a6acac(long param_1,undefined4 param_2)

{
  uint uVar1;
  
  *(undefined4 *)(param_1 + 0x7c) = param_2;
  uVar1 = FUN_005e08f0();
  *(uint *)(param_1 + 0x84) = uVar1 & ((int)uVar1 >> 0x1f ^ 0xffffffffU);
  return;
}

~~~
