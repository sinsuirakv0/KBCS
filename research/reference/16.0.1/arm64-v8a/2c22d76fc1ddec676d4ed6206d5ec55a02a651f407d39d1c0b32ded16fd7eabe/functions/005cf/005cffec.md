# 005cffec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005cffec",
  "name": "FUN_005cffec",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1291dbd585dbd90cdd3e44682f2c977966aab8ab04fd37ff777ec80f67d42d71",
  "source_text_sha256": "1291dbd585dbd90cdd3e44682f2c977966aab8ab04fd37ff777ec80f67d42d71"
}
~~~

## 呼び出し元

- [005cf6c0](../005cf/005cf6c0.md)
- [005d69f0](../005d6/005d69f0.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [005d01d0](../005d0/005d01d0.md)
- [005d0370](../005d0/005d0370.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 3004 bytes

~~~c

long FUN_005cffec(long *param_1,undefined8 *param_2)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  void *pvVar6;
  long lVar7;
  long lVar8;
  undefined8 uVar9;
  ulong uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  void *local_70;
  undefined8 *local_68;
  undefined8 *local_60;
  void *pvStack_58;
  long *local_50;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  lVar7 = param_1[1] - *param_1 >> 5;
  uVar1 = lVar7 * -0x5555555555555555 + 1;
  if (uVar1 < 0x2aaaaaaaaaaaaab) {
    local_50 = param_1 + 2;
    lVar8 = *local_50 - *param_1 >> 5;
    uVar10 = lVar8 * 0x5555555555555556;
    if (uVar10 < uVar1 || uVar10 - uVar1 == 0) {
      uVar10 = uVar1;
    }
    if (0x155555555555554 < (ulong)(lVar8 * -0x5555555555555555)) {
      uVar10 = 0x2aaaaaaaaaaaaaa;
    }
    if (uVar10 == 0) {
      local_70 = (void *)0x0;
    }
    else {
      if (0x2aaaaaaaaaaaaaa < uVar10) goto LAB_005d0194;
      local_70 = (void *)_Znwm(uVar10 * 0x60);
    }
    uVar12 = *param_2;
    uVar14 = param_2[3];
    uVar13 = param_2[2];
    local_68 = (undefined8 *)((long)local_70 + lVar7 * 0x20);
    uVar9 = param_2[6];
    uVar11 = *(undefined8 *)((long)param_2 + 0x55);
    pvStack_58 = (void *)((long)local_70 + uVar10 * 0x60);
    local_68[1] = param_2[1];
    *local_68 = uVar12;
    local_68[3] = uVar14;
    local_68[2] = uVar13;
    uVar14 = param_2[5];
    uVar13 = param_2[4];
    local_68[6] = uVar9;
    uVar9 = param_2[9];
    uVar12 = param_2[10];
    local_68[5] = uVar14;
    local_68[4] = uVar13;
    uVar13 = param_2[7];
    local_68[8] = param_2[8];
    local_68[7] = uVar13;
    *(undefined8 *)((long)local_68 + 0x55) = uVar11;
    local_68[9] = uVar9;
    local_68[10] = uVar12;
    local_60 = local_68 + 0xc;
    param_2[4] = 0;
    param_2[5] = 0;
    param_2[8] = 0;
    param_2[9] = 0;
    param_2[6] = 0;
    param_2[7] = 0;
    FUN_005d01d0(param_1,&local_70);
    puVar3 = local_68;
    lVar7 = param_1[1];
    while (puVar4 = local_60, local_60 != puVar3) {
      pvVar6 = (void *)local_60[-5];
      puVar5 = local_60 + -0xc;
      if (pvVar6 != (void *)0x0) {
        local_60[-4] = pvVar6;
        local_60 = local_60 + -0xc;
        _ZdlPv(pvVar6);
        puVar5 = local_60;
      }
      local_60 = puVar5;
      pvVar6 = (void *)puVar4[-8];
      if (pvVar6 != (void *)0x0) {
        puVar4[-7] = pvVar6;
        _ZdlPv(pvVar6);
      }
    }
    if (local_70 != (void *)0x0) {
      _ZdlPv(local_70);
    }
    if (*(long *)(lVar2 + 0x28) == local_48) {
      return lVar7;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != local_48) goto LAB_005d01cc;
    FUN_005d0370(param_1);
LAB_005d0194:
    if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      FUN_00440ec0();
    }
  }
LAB_005d01cc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
