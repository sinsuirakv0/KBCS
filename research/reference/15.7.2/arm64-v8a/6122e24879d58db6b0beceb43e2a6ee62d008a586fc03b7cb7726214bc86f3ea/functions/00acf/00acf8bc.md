# 00acf8bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acf8bc.md)

## 関数情報

~~~json
{
  "address": "00acf8bc",
  "name": "FUN_00acf8bc",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1bd9bb53089e4ef8b71744d3c0e3db9cf5dc680990621d434c6c04f5fdd85270",
  "source_text_sha256": "1bd9bb53089e4ef8b71744d3c0e3db9cf5dc680990621d434c6c04f5fdd85270"
}
~~~
## 呼び出し元

- [0072f020](../0072f/0072f020.md)
- [00957f9c](../00957/00957f9c.md)
- [00960f9c](../00960/00960f9c.md)
- [009a9ce0](../009a9/009a9ce0.md)

## 呼び出し先

- [00adbf54](../00adb/00adbf54.md)
- [00adbf88](../00adb/00adbf88.md)

## 疑似コード 1/1 / UTF-8 605 bytes

~~~c

void FUN_00acf8bc(undefined8 param_1,int param_2)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  undefined8 uVar4;
  
  uVar4 = FUN_00adbf88();
  uVar1 = 50000;
  if ((uint)uVar4 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar4 >> 0x10) & 0xffff;
  }
  uVar1 = uVar1 + param_2;
  uVar3 = FUN_00adbf88(param_1);
  uVar3 = uVar3 & 0xffff;
  if (49999 < uVar3) {
    uVar3 = 50000;
  }
  uVar2 = 0xc3500000;
  if ((int)uVar1 < 0xc351) {
    uVar2 = (uVar1 & ((int)uVar1 >> 0x1f ^ 0xffffffffU)) << 0x10;
  }
  FUN_00adbf54(param_1,uVar2 | uVar3);
  DAT_00c23eb4 = 1;
  return;
}

~~~
