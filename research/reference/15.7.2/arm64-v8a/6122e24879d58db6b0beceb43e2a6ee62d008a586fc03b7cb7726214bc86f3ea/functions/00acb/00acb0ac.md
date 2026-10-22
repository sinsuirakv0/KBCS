# 00acb0ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acb0ac.md)

## 関数情報

~~~json
{
  "address": "00acb0ac",
  "name": "FUN_00acb0ac",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9ea47cc48d1ad468d19b6733280cd358879ecd6cebf1910159d3bea2c834d59e",
  "source_text_sha256": "9ea47cc48d1ad468d19b6733280cd358879ecd6cebf1910159d3bea2c834d59e"
}
~~~
## 呼び出し元

- [00abf464](../00abf/00abf464.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [005f064c](../005f0/005f064c.md)
- [0062c99c](../0062c/0062c99c.md)
- [0062ca28](../0062c/0062ca28.md)
- [00acb330](../00acb/00acb330.md)
- [00acb44c](../00acb/00acb44c.md)
- [00acb508](../00acb/00acb508.md)
- [00bd6fec](../00bd6/00bd6fec.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 3663 bytes

~~~c

long FUN_00acb0ac(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  void *pvVar4;
  undefined8 uVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 *puVar8;
  long lVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  void *local_90;
  undefined8 *local_88;
  undefined8 *local_80;
  void *pvStack_78;
  long *local_70;
  undefined8 *local_68;
  undefined1 local_60;
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar7 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar7 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_70 = param_1 + 2;
    lVar9 = *local_70 - *param_1 >> 3;
    uVar10 = lVar9 * 0x5555555555555556;
    if (uVar10 < uVar1 || uVar10 - uVar1 == 0) {
      uVar10 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar9 * -0x5555555555555555)) {
      uVar10 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar10 == 0) {
      local_90 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar10) goto LAB_00acb2c0;
      local_90 = operator_new(uVar10 * 0x18);
    }
    local_60 = 0;
    puVar11 = (undefined8 *)((long)local_90 + lVar7 * 8);
    pvStack_78 = (void *)((long)local_90 + uVar10 * 0x18);
    lVar7 = *param_2;
    lVar9 = param_2[1];
    uVar1 = lVar9 - lVar7;
    *puVar11 = 0;
    puVar11[1] = 0;
    puVar11[2] = 0;
    local_80 = puVar11;
    local_88 = puVar11;
    local_68 = puVar11;
    if (uVar1 != 0) {
      if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar1 >> 3) * -0x5555555555555555)) {
        if (*(long *)(lVar2 + 0x28) == local_58) {
          uVar5 = FUN_005f064c(puVar11);
          puVar11[1] = 0xaaaaaaaaaaaaaaa;
          FUN_0062c99c(&local_68);
          FUN_00acb44c(&local_90);
          if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00bd6fec(uVar5);
          }
        }
        goto LAB_00acb32c;
      }
      pvVar4 = operator_new(uVar1);
      *puVar11 = pvVar4;
      puVar11[1] = pvVar4;
      puVar11[2] = (long)pvVar4 + uVar1;
      uVar5 = FUN_0062ca28(puVar11 + 2,lVar7,lVar9,pvVar4);
      puVar11[1] = uVar5;
    }
    local_80 = local_80 + 3;
    FUN_00acb330(param_1,&local_90);
    puVar11 = local_88;
    lVar7 = param_1[1];
    while (puVar3 = local_80, puVar3 != puVar11) {
      puVar12 = puVar3 + -3;
      puVar13 = (undefined8 *)*puVar12;
      local_80 = puVar12;
      if (puVar13 != (undefined8 *)0x0) {
        puVar8 = (undefined8 *)puVar3[-2];
        puVar6 = puVar13;
        if (puVar8 != puVar13) {
          do {
            puVar6 = puVar8 + -3;
            pvVar4 = (void *)*puVar6;
            if (pvVar4 != (void *)0x0) {
              puVar8[-2] = pvVar4;
              operator_delete(pvVar4);
            }
            puVar8 = puVar6;
          } while (puVar6 != puVar13);
          puVar6 = (undefined8 *)*puVar12;
        }
        puVar3[-2] = puVar13;
        operator_delete(puVar6);
      }
    }
    local_80 = puVar3;
    if (local_90 != (void *)0x0) {
      operator_delete(local_90);
    }
    if (*(long *)(lVar2 + 0x28) == local_58) {
      return lVar7;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != local_58) goto LAB_00acb32c;
    FUN_00acb508(param_1);
LAB_00acb2c0:
    if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
  }
LAB_00acb32c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
