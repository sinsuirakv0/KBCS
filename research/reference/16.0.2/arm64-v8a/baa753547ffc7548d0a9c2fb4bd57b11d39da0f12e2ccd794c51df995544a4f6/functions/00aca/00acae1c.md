# 00acae1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acae1c",
  "name": "FUN_00acae1c",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cf2b7717ccb3ccdb353f3d841145c33a8fdac91d9fadec558bc972cd3aaa989",
  "source_text_sha256": "1cf2b7717ccb3ccdb353f3d841145c33a8fdac91d9fadec558bc972cd3aaa989"
}
~~~

## 呼び出し元

- [00680e48](../00680/00680e48.md)
- [006b545c](../006b5/006b545c.md)
- [0073ee8c](../0073e/0073ee8c.md)
- [007738ec](../00773/007738ec.md)
- [00789e38](../00789/00789e38.md)
- [007df140](../007df/007df140.md)
- [0082fbc4](../0082f/0082fbc4.md)
- [008cb698](../008cb/008cb698.md)
- [008d38f0](../008d3/008d38f0.md)
- [008deaac](../008de/008deaac.md)
- [008f7ecc](../008f7/008f7ecc.md)
- [008ff094](../008ff/008ff094.md)
- [0091abcc](../0091a/0091abcc.md)
- [00997090](../00997/00997090.md)
- [00a3e578](../00a3e/00a3e578.md)
- [00a79c74](../00a79/00a79c74.md)
- [00ab67b0](../00ab6/00ab67b0.md)
- [00ac0b0c](../00ac0/00ac0b0c.md)
- [00ae1328](../00ae1/00ae1328.md)

## 呼び出し先

- [004678a0](../00467/004678a0.md)
- [00469c44](../00469/00469c44.md)
- [0046ca04](../0046c/0046ca04.md)
- [00489f8c](../00489/00489f8c.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 1838 bytes

~~~c

void FUN_00acae1c(undefined8 param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  float fVar7;
  
  uVar2 = FUN_004678a0();
  lVar3 = FUN_00489f8c(param_2,0);
  iVar4 = (int)((float)*(int *)(lVar3 + 0xc) * 1.25);
  lVar3 = FUN_00851550();
  fVar7 = (float)*(int *)(lVar3 + 0x44e364) * 1.25;
  iVar5 = (int)fVar7;
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                    (float)(*(int *)(lVar3 + 0x44e360) << 1)),0,iVar5,iVar4,0);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)(((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                    (float)*(int *)(lVar3 + 0x44e360)),0,iVar5,iVar4,1);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  fVar7 = (float)(int)fVar7;
  FUN_00469c44(uVar2,param_2,
               (int)(((((float)iVar1 * 0.5 + -572.0) - (float)iVar6) -
                     (float)(*(int *)(lVar3 + 0x44e360) << 1)) - fVar7),0,iVar5,iVar4,1);
  FUN_00851550();
  iVar1 = FUN_0046ca04();
  lVar3 = FUN_00851550();
  iVar6 = *(int *)((long)&fde_table_entry_00333f80.data_loc + lVar3);
  lVar3 = FUN_00851550();
  FUN_00469c44(uVar2,param_2,
               (int)((((float)iVar6 + (float)iVar1 * 0.5 + (float)param_3) -
                     (float)*(int *)(lVar3 + 0x44e360)) + fVar7),0,iVar5,iVar4,0);
  return;
}

~~~
