# 00acadac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00acadac",
  "name": "FUN_00acadac",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4cfca376a8422fdb563d57e24dbc93b7bb11c1f0313ee0dedb662ecb15e8772b",
  "source_text_sha256": "4cfca376a8422fdb563d57e24dbc93b7bb11c1f0313ee0dedb662ecb15e8772b"
}
~~~

## 呼び出し元

- [00680e08](../00680/00680e08.md)
- [006b5404](../006b5/006b5404.md)
- [0073ee34](../0073e/0073ee34.md)
- [00773894](../00773/00773894.md)
- [00789de0](../00789/00789de0.md)
- [007df0e8](../007df/007df0e8.md)
- [0082fb6c](../0082f/0082fb6c.md)
- [008cb644](../008cb/008cb644.md)
- [008d389c](../008d3/008d389c.md)
- [008dea58](../008de/008dea58.md)
- [008f7e78](../008f7/008f7e78.md)
- [008ff040](../008ff/008ff040.md)
- [0091ab78](../0091a/0091ab78.md)
- [0099703c](../00997/0099703c.md)
- [00a3e524](../00a3e/00a3e524.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ab6740](../00ab6/00ab6740.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)
- [00ae128c](../00ae1/00ae128c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00469c04](../00469/00469c04.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [00489f4c](../00489/00489f4c.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acadac(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_00467860();
  lVar3 = FUN_00489f4c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_008514f8();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  fVar7 = (float)(int)fVar7;
  FUN_00469c04(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_008514f8();
  iVar1 = FUN_0046c9c4();
  lVar3 = FUN_008514f8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514f8();
  FUN_00469c04(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~
