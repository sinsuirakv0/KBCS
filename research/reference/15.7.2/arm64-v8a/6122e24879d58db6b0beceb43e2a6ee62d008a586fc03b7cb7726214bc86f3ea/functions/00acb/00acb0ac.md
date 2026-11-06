# 00acb0ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "6b03d6619afa14ef4752ca5f72039c794a5b1ffe0f9f3c11ff22d5909cc791b4",
  "source_text_sha256": "6b03d6619afa14ef4752ca5f72039c794a5b1ffe0f9f3c11ff22d5909cc791b4"
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

## 疑似コード / UTF-8 3478 bytes

~~~c

long FUN_00acb0ac(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  long *plVar4;
  long lVar5;
  undefined8 *puVar6;
  void *__ptr;
  undefined8 uVar7;
  long lVar8;
  undefined8 *puVar9;
  long lVar10;
  ulong uVar11;
  long *plVar12;
  long *plVar13;
  undefined8 *puVar14;
  void *local_90;
  long *local_88;
  long *local_80;
  void *pvStack_78;
  long *local_70;
  long *local_68;
  undefined1 local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  lVar8 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar8 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_70 = param_1 + 2;
    lVar10 = *local_70 - *param_1 >> 3;
    uVar11 = lVar10 * 0x5555555555555556;
    if (uVar11 < uVar1 || uVar11 - uVar1 == 0) {
      uVar11 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar10 * -0x5555555555555555)) {
      uVar11 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar11 == 0) {
      local_90 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar11) goto LAB_00acb2c0;
      local_90 = (void *)_Znwm(uVar11 * 0x18);
    }
    local_60 = 0;
    plVar12 = (long *)((long)local_90 + lVar8 * 8);
    pvStack_78 = (void *)((long)local_90 + uVar11 * 0x18);
    lVar8 = *param_2;
    lVar10 = param_2[1];
    lVar2 = lVar10 - lVar8;
    *plVar12 = 0;
    plVar12[1] = 0;
    plVar12[2] = 0;
    local_80 = plVar12;
    local_88 = plVar12;
    local_68 = plVar12;
    if (lVar2 != 0) {
      if (0xaaaaaaaaaaaaaaa < (ulong)((lVar2 >> 3) * -0x5555555555555555)) {
        if (*(long *)(lVar3 + 0x28) == local_58) {
          uVar7 = FUN_005f064c(plVar12);
          plVar12[1] = 0xaaaaaaaaaaaaaaa;
          FUN_0062c99c(&local_68);
          FUN_00acb44c(&local_90);
          if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00bd6fec(uVar7);
          }
        }
        goto LAB_00acb32c;
      }
      lVar5 = _Znwm(lVar2);
      *plVar12 = lVar5;
      plVar12[1] = lVar5;
      plVar12[2] = lVar5 + lVar2;
      lVar8 = FUN_0062ca28(plVar12 + 2,lVar8,lVar10,lVar5);
      plVar12[1] = lVar8;
    }
    local_80 = local_80 + 3;
    FUN_00acb330(param_1,&local_90);
    plVar12 = local_88;
    lVar8 = param_1[1];
    while (plVar4 = local_80, plVar4 != plVar12) {
      plVar13 = plVar4 + -3;
      puVar14 = (undefined8 *)*plVar13;
      local_80 = plVar13;
      if (puVar14 != (undefined8 *)0x0) {
        puVar9 = (undefined8 *)plVar4[-2];
        puVar6 = puVar14;
        if (puVar9 != puVar14) {
          do {
            puVar6 = puVar9 + -3;
            __ptr = (void *)*puVar6;
            if (__ptr != (void *)0x0) {
              puVar9[-2] = __ptr;
              _ZdlPv(__ptr);
            }
            puVar9 = puVar6;
          } while (puVar6 != puVar14);
          puVar6 = (undefined8 *)*plVar13;
        }
        plVar4[-2] = (long)puVar14;
        _ZdlPv(puVar6);
      }
    }
    local_80 = plVar4;
    if (local_90 != (void *)0x0) {
      _ZdlPv(local_90);
    }
    if (*(long *)(lVar3 + 0x28) == local_58) {
      return lVar8;
    }
  }
  else {
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00acb32c;
    FUN_00acb508(param_1);
LAB_00acb2c0:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
  }
LAB_00acb32c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
