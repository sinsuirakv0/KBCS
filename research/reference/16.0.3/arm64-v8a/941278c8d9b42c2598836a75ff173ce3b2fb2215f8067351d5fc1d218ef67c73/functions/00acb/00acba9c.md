# 00acba9c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acba9c",
  "name": "FUN_00acba9c",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f7e45853ff9fe2d6f98f073284f7b7e8a024412b4236a2cfafc757cad4b36091",
  "source_text_sha256": "f7e45853ff9fe2d6f98f073284f7b7e8a024412b4236a2cfafc757cad4b36091"
}
~~~

## 呼び出し元

- [00830b70](../00830/00830b70.md)
- [0099803c](../00998/0099803c.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 603 bytes

~~~c

void FUN_00acba9c(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0xa0) != '\0') {
    uVar4 = FUN_00467bc0();
    iVar1 = *(int *)(param_1 + 0xa4) * 0x14;
    if (0xfe < iVar1) {
      iVar1 = 0xff;
    }
    FUN_00467e8c(uVar4,0,0,0,iVar1);
    lVar5 = FUN_008524fc();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_008524fc();
    uVar2 = FUN_0046cd24();
    FUN_008524fc();
    uVar3 = FUN_0046cde4();
    FUN_004682b4(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~
