# 00acba0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acba0c",
  "name": "FUN_00acba0c",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "861e3624ba8fd93ea7915794ff31487f4c9f48b63260373eacd4c3e2d76225c0",
  "source_text_sha256": "861e3624ba8fd93ea7915794ff31487f4c9f48b63260373eacd4c3e2d76225c0"
}
~~~

## 呼び出し元

- [0078a214](../0078a/0078a214.md)
- [00830b70](../00830/00830b70.md)
- [00900040](../00900/00900040.md)
- [00a3f56c](../00a3f/00a3f56c.md)
- [00ac1b00](../00ac1/00ac1b00.md)

## 呼び出し先

- [00467bc0](../00467/00467bc0.md)
- [00467e8c](../00467/00467e8c.md)
- [004682b4](../00468/004682b4.md)
- [0046cd24](../0046c/0046cd24.md)
- [0046cde4](../0046c/0046cde4.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 534 bytes

~~~c

void FUN_00acba0c(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0x94) != '\0') {
    uVar4 = FUN_00467bc0();
    FUN_00467e8c(uVar4,0,0,0,*(int *)(param_1 + 0x90) * 0x14);
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
