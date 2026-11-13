# 00af6cac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af6cac",
  "name": "FUN_00af6cac",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5",
  "source_text_sha256": "4181316bf6c179a6649767a700ae5a4965d8bc92967f10d5d3e66ec1ac8d30e5"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 400 bytes

~~~c

void FUN_00af6cac(int param_1,int param_2,uint param_3)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  
  lVar1 = FUN_00851550();
  uVar2 = FUN_005e7460(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_00851550();
  lVar1 = 0x44;
  if ((uVar2 & 1) != 0) {
    lVar1 = 0x40;
  }
  *(uint *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + lVar1 + 0x848c8) = param_3 & 1;
  return;
}

~~~
