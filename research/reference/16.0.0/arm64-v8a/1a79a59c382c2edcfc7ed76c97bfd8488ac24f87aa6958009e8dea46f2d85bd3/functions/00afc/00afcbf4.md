# 00afcbf4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afcbf4",
  "name": "FUN_00afcbf4",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "795eb84a7076584132d1af7587022c02060dce2d24acf856d33560d0b1748118",
  "source_text_sha256": "795eb84a7076584132d1af7587022c02060dce2d24acf856d33560d0b1748118"
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00afcbf4(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c) = iVar3 + param_3;
  }
  return;
}

~~~
