# 00aca7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aca7ac",
  "name": "FUN_00aca7ac",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46534f1daf495d0918287df2e50222c127c7c4529608418f7ae9625c2fffa27b",
  "source_text_sha256": "46534f1daf495d0918287df2e50222c127c7c4529608418f7ae9625c2fffa27b"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467aec](../00467/00467aec.md)
- [00467f14](../00467/00467f14.md)
- [0046c984](../0046c/0046c984.md)
- [0046ca44](../0046c/0046ca44.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 534 bytes

~~~c

void FUN_00aca7ac(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0x94) != '\0') {
    uVar4 = FUN_00467820();
    FUN_00467aec(uVar4,0,0,0,*(int *)(param_1 + 0x90) * 0x14);
    lVar5 = FUN_008514b8();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_008514b8();
    uVar2 = FUN_0046c984();
    FUN_008514b8();
    uVar3 = FUN_0046ca44();
    FUN_00467f14(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~
