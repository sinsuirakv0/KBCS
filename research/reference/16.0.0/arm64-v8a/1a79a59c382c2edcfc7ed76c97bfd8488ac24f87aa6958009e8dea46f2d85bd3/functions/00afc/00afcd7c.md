# 00afcd7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afcd7c",
  "name": "FUN_00afcd7c",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fda00cbea4222361d8c1e2a7c15d554f90df6e1460382b0c7eb4d9806ddb24f",
  "source_text_sha256": "9fda00cbea4222361d8c1e2a7c15d554f90df6e1460382b0c7eb4d9806ddb24f"
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00afcd7c(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a64);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a64) = iVar3 + param_3;
  }
  return;
}

~~~
