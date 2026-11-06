# 00a3afcc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a3afcc.md)

## 関数情報

~~~json
{
  "address": "00a3afcc",
  "name": "FUN_00a3afcc",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "829eb6052f200d360cb03d6b74bc588646bf0da024afb7e5db00f7285fb96047",
  "source_text_sha256": "829eb6052f200d360cb03d6b74bc588646bf0da024afb7e5db00f7285fb96047"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041c8f8](../0041c/0041c8f8.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00883cc0](../00883/00883cc0.md)
- [009e97e4](../009e9/009e97e4.md)
- [009e97fc](../009e9/009e97fc.md)
- [009ea92c](../009ea/009ea92c.md)

## 疑似コード 1/1 / UTF-8 1107 bytes

~~~c

void FUN_00a3afcc(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  uint uVar2;
  int iVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long lVar6;
  
  uVar5 = *param_2;
  iVar3 = *param_3;
  lVar6 = *(long *)(param_1 + 8);
  uVar4 = FUN_00883cc0(uVar5);
  uVar4 = FUN_009e97fc(uVar4,1);
  if (iVar3 == 2) {
    iVar3 = *(int *)(BYTE_ARRAY_0032ff39 + lVar6 + 0x23);
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    uVar1 = iVar3 >> 1 & 1;
    uVar2 = -uVar1;
    if (-1 < iVar3 >> 1) {
      uVar2 = uVar1;
    }
    FUN_009ea92c(uVar4,uVar2 + 2,uVar2 + 9);
    uVar4 = FUN_00883cc0(uVar5);
    uVar4 = FUN_009e97fc(uVar4,1);
    FUN_009e97e4(uVar4,1);
    return;
  }
  FUN_009e97e4(uVar4,0);
  if (iVar3 != 4) {
    if (iVar3 == 3) {
      uVar4 = FUN_00457e1c();
      uVar5 = 0xb;
    }
    else {
      if (iVar3 != 0) {
        return;
      }
      uVar4 = FUN_00457e1c();
      uVar5 = 10;
    }
    FUN_00459efc(uVar4,uVar5,0);
    return;
  }
  *(undefined4 *)(lVar6 + 0x3388) = 0x21;
  *(undefined1 *)(lVar6 + 0x3390) = 1;
  FUN_0041be0c();
  FUN_0041c8f8();
  return;
}

~~~
