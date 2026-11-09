# 00affb3c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00affb3c",
  "name": "FUN_00affb3c",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4036a8623f168a20d2ccd884287421a810fa5ae01058952c06ecdfce7e4bc657",
  "source_text_sha256": "4036a8623f168a20d2ccd884287421a810fa5ae01058952c06ecdfce7e4bc657"
}
~~~

## 呼び出し元

- [0098c828](../0098c/0098c828.md)
- [00affc2c](../00aff/00affc2c.md)

## 呼び出し先

- [0046da7c](../0046d/0046da7c.md)
- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00afe6c0](../00afe/00afe6c0.md)

## 疑似コード / UTF-8 711 bytes

~~~c

int FUN_00affb3c(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
  lVar3 = FUN_008514b8();
  uVar4 = FUN_005e73e0(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar4 & 1) == 0) {
    iVar2 = 0;
  }
  else {
    lVar3 = FUN_008514b8();
    iVar2 = *(int *)(lVar3 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0xa05c8);
    iVar1 = FUN_00afe6c0(param_1,param_2,param_3,0x19,0);
                    /* catch() { ... } // from try @ 00aff548 with catch @ 00affbc0 */
    iVar2 = FUN_0046da7c(iVar2 + iVar1 * -100,0);
    iVar1 = FUN_00afe6c0(param_1,param_2,param_3,0x3f4,0);
    iVar2 = (((100 - iVar1) * (iVar2 / 100)) / 100) * 100;
  }
  return iVar2;
}

~~~
