# 00afce9c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afce9c",
  "name": "FUN_00afce9c",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e4a65c799469ea73902490172707516a2f99b6640d990328d96fe2e9cfe1954",
  "source_text_sha256": "7e4a65c799469ea73902490172707516a2f99b6640d990328d96fe2e9cfe1954"
}
~~~

## 呼び出し元

- [00716d50](../00716/00716d50.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 389 bytes

~~~c

void FUN_00afce9c(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_005e73e0(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008514b8();
    lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
    *(int *)(lVar1 + 0x84bfc) = *(int *)(lVar1 + 0x84bfc) + param_3;
  }
  return;
}

~~~
