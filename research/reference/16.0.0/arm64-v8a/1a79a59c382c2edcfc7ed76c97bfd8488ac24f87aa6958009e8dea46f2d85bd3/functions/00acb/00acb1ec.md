# 00acb1ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acb1ec",
  "name": "FUN_00acb1ec",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bf71fced50f5d714c9f67dba176312a2c4dc82a46487ac97b08c9ad5f26ead84",
  "source_text_sha256": "bf71fced50f5d714c9f67dba176312a2c4dc82a46487ac97b08c9ad5f26ead84"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459d34](../00459/00459d34.md)
- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008514b8](../00851/008514b8.md)
- [008b6e60](../008b6/008b6e60.md)
- [00a466e0](../00a46/00a466e0.md)
- [00a466f8](../00a46/00a466f8.md)
- [00a469c0](../00a46/00a469c0.md)

## 疑似コード / UTF-8 1433 bytes

~~~c

void FUN_00acb1ec(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  uint uVar2;
  int iVar3;
  undefined8 uVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  
  uVar7 = *param_2;
  iVar3 = *param_3;
  uVar4 = FUN_008b6e60(uVar7);
  uVar4 = FUN_00a466f8(uVar4,1);
  if (iVar3 == 2) {
    lVar5 = FUN_008514b8();
    iVar3 = *(int *)((long)&fde_table_entry_00337d90.initial_loc + lVar5);
    if (iVar3 < 0) {
      iVar3 = iVar3 + 1;
    }
    uVar1 = iVar3 >> 1 & 1;
    uVar2 = -uVar1;
    if (-1 < iVar3 >> 1) {
      uVar2 = uVar1;
    }
    FUN_00a469c0(uVar4,uVar2 + 0xc);
    uVar4 = FUN_008b6e60(uVar7);
    uVar4 = FUN_00a466f8(uVar4,1);
    FUN_00a466e0(uVar4,1);
    return;
  }
  FUN_00a466e0(uVar4,0);
  if (iVar3 != 4) {
    if (iVar3 == 3) {
      uVar4 = FUN_0047acb4();
      uVar7 = 0xb;
    }
    else {
      if (iVar3 != 0) {
        return;
      }
      uVar4 = FUN_0047acb4();
      uVar7 = 10;
    }
    FUN_0047cd94(uVar4,uVar7,0);
    return;
  }
  lVar5 = FUN_008514b8();
  plVar6 = *(long **)((long)&fde_table_entry_00337e60.initial_loc + lVar5);
  if (plVar6 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00acb2d4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar6 + 0x30))();
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00459d34();
}

~~~
