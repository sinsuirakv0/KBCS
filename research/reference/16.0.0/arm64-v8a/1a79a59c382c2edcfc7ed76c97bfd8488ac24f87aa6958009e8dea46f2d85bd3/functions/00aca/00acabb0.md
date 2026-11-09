# 00acabb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acabb0",
  "name": "FUN_00acabb0",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4bd94e9c1ca4dfc4e4c825e29405b472826d02f5326a79816346cbd9e6a35b2",
  "source_text_sha256": "d4bd94e9c1ca4dfc4e4c825e29405b472826d02f5326a79816346cbd9e6a35b2"
}
~~~

## 呼び出し元

- [00680dc8](../00680/00680dc8.md)
- [006b53c4](../006b5/006b53c4.md)
- [0073edf4](../0073e/0073edf4.md)
- [00773854](../00773/00773854.md)
- [00789da0](../00789/00789da0.md)
- [007df0a8](../007df/007df0a8.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [008d3700](../008d3/008d3700.md)
- [008de8bc](../008de/008de8bc.md)
- [008f7cdc](../008f7/008f7cdc.md)
- [008feea4](../008fe/008feea4.md)
- [0091a9dc](../0091a/0091a9dc.md)
- [00996ea0](../00996/00996ea0.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ab6544](../00ab6/00ab6544.md)
- [00ac08a0](../00ac0/00ac08a0.md)
- [00ae0e64](../00ae0/00ae0e64.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00469bc4](../00469/00469bc4.md)
- [0046c984](../0046c/0046c984.md)
- [00489f0c](../00489/00489f0c.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acabb0(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_00467820();
  lVar3 = FUN_00489f0c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_008514b8();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  fVar7 = (float)(int)fVar7;
  FUN_00469bc4(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_008514b8();
  iVar1 = FUN_0046c984();
  lVar3 = FUN_008514b8();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_008514b8();
  FUN_00469bc4(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~
