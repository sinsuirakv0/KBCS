# 00acf8bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00acf9c8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9c8.md)
<!-- /kbcs-version-next -->

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
  "source_sha256": "8648ba9c326fdce1cb23084ef27d4207841bcea0f95ba1d3b536e44f299c902e",
  "source_text_sha256": "8648ba9c326fdce1cb23084ef27d4207841bcea0f95ba1d3b536e44f299c902e"
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

## 疑似コード / UTF-8 576 bytes

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
