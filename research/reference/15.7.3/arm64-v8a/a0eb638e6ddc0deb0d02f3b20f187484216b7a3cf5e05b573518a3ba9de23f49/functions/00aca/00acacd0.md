# 00acacd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acacd0",
  "name": "FUN_00acacd0",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96823905f8308be8a322b4b9e0d876de5223618e64c6751795efc63d94fb63ce",
  "source_text_sha256": "96823905f8308be8a322b4b9e0d876de5223618e64c6751795efc63d94fb63ce"
}
~~~

## 呼び出し元

- [00abf52c](../00abf/00abf52c.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [0051d884](../0051d/0051d884.md)
- [0076a658](../0076a/0076a658.md)
- [007d95c0](../007d9/007d95c0.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 2596 bytes

~~~c

long FUN_00acacd0(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  byte *pbVar7;
  long lVar8;
  ulong uVar9;
  undefined8 *puVar10;
  byte *pbVar11;
  byte *pbVar12;
  void *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  void *pvStack_68;
  long *local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  lVar6 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar6 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_60 = param_1 + 2;
    lVar8 = *local_60 - *param_1 >> 3;
    uVar9 = lVar8 * 0x5555555555555556;
    if (uVar9 < uVar1 || uVar9 - uVar1 == 0) {
      uVar9 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      uVar9 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar9 == 0) {
      local_80 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00acaea4;
      local_80 = (void *)_Znwm(uVar9 * 0x18);
    }
    lVar8 = *param_2;
    lVar2 = param_2[1];
    local_78 = (undefined8 *)((long)local_80 + lVar6 * 8);
    pvStack_68 = (void *)((long)local_80 + uVar9 * 0x18);
    local_78[1] = 0;
    local_78[2] = 0;
    *local_78 = 0;
    local_70 = local_78;
    FUN_0051d884(local_78,lVar8,lVar2,(lVar2 - lVar8 >> 3) * -0x5555555555555555);
    local_70 = local_70 + 3;
    FUN_007d95c0(param_1,&local_80);
    puVar5 = local_78;
    lVar6 = param_1[1];
    while (puVar4 = local_70, puVar4 != puVar5) {
      puVar10 = puVar4 + -3;
      pbVar11 = (byte *)*puVar10;
      local_70 = puVar10;
      if (pbVar11 != (byte *)0x0) {
        pbVar7 = (byte *)puVar4[-2];
        pbVar12 = pbVar11;
        if (pbVar7 != pbVar11) {
          do {
            pbVar12 = pbVar7 + -0x18;
            if ((*pbVar12 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar7 + -8));
            }
            pbVar7 = pbVar12;
          } while (pbVar12 != pbVar11);
          pbVar12 = (byte *)*puVar10;
        }
        puVar4[-2] = pbVar11;
        _ZdlPv(pbVar12);
      }
    }
    local_70 = puVar4;
    if (local_80 != (void *)0x0) {
      _ZdlPv(local_80);
    }
    if (*(long *)(lVar3 + 0x28) == local_58) {
      return lVar6;
    }
  }
  else {
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00acaedc;
    FUN_0076a658(param_1);
LAB_00acaea4:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
  }
LAB_00acaedc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
