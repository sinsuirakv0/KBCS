# 00aeffd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aeffd8",
  "name": "FUN_00aeffd8",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46e24b343e6ee9cea11cdfd59c0ee312d51c517d37de9f0c5147adb5b65cef0c",
  "source_text_sha256": "46e24b343e6ee9cea11cdfd59c0ee312d51c517d37de9f0c5147adb5b65cef0c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6f50](../008b6/008b6f50.md)
- [00b0b640](../00b0b/00b0b640.md)

## 疑似コード / UTF-8 760 bytes

~~~c

void FUN_00aeffd8(long param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  long lVar6;
  
  iVar1 = *param_3;
  uVar5 = *param_2;
  if (iVar1 == 4) {
    lVar6 = *(long *)(param_1 + 8);
    uVar3 = FUN_008b6f50(uVar5);
    if ((uVar3 & 1) == 0) {
      return;
    }
    FUN_00b0b640(lVar6 + 0x3d8,*(long *)(param_1 + 0x10),*(long *)(param_1 + 0x10) + 0x510,0);
    return;
  }
  if (iVar1 == 3) {
    uVar2 = FUN_0047acf4();
    uVar3 = FUN_008b6f50(uVar5);
    uVar4 = 0xb;
    if ((uVar3 & 1) == 0) {
      uVar4 = 0xf;
    }
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_0047acf4();
    uVar4 = 10;
  }
  FUN_0047cdd4(uVar2,uVar4,0);
  return;
}

~~~
