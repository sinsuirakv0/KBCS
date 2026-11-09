# 00b0ccac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b0ccac",
  "name": "FUN_00b0ccac",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee9437754fa8f60bb46b7a1d08f634830168304821feb74a93e14eece91229d2",
  "source_text_sha256": "ee9437754fa8f60bb46b7a1d08f634830168304821feb74a93e14eece91229d2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b9134](../008b9/008b9134.md)
- [00b0b218](../00b0b/00b0b218.md)
- [00b0be2c](../00b0b/00b0be2c.md)

## 疑似コード / UTF-8 714 bytes

~~~c

void FUN_00b0ccac(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  uint uVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  uVar1 = *param_4;
  if (*param_3 == 5) {
    lVar3 = *(long *)(param_1 + 8);
    if (uVar1 == 1) {
      FUN_00b0b218(lVar3,*(undefined8 *)(param_1 + 0x10),*(undefined8 *)(param_1 + 0x18),
                   *(undefined4 *)(lVar3 + 0x48));
      return;
    }
    if (uVar1 == 0) {
      FUN_00b0be2c(lVar3,*(undefined4 *)(lVar3 + 0x48),0xffffffff,0,0);
      return;
    }
  }
  else if ((*param_3 == 2) && (uVar1 < 2)) {
    uVar4 = *param_2;
    uVar2 = FUN_0047acb4();
    FUN_0047cd94(uVar2,0xb,0);
    FUN_008b9134(uVar4);
    return;
  }
  return;
}

~~~
