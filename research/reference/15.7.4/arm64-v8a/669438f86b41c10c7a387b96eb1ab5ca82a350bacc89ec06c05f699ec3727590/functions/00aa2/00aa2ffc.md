# 00aa2ffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00aa2ffc",
  "name": "FUN_00aa2ffc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c0ba816b0813260d7ea3d37dac4a70191d02f27c27fe9ba201f85dad16528b4",
  "source_text_sha256": "2c0ba816b0813260d7ea3d37dac4a70191d02f27c27fe9ba201f85dad16528b4"
}
~~~

## 呼び出し元

- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 396 bytes

~~~c

bool FUN_00aa2ffc(int param_1,int param_2,int param_3)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(lVar2 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9feac) != 0;
  }
  return bVar1;
}

~~~
