# 00b2abcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b2abcc",
  "name": "FUN_00b2abcc",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9464a69311f1457bc9e77a127fc18a6d32f099b4dcbf42a1b2d2d90bbd9ea61d",
  "source_text_sha256": "9464a69311f1457bc9e77a127fc18a6d32f099b4dcbf42a1b2d2d90bbd9ea61d"
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0054075c](../00540/0054075c.md)
- [00794b6c](../00794/00794b6c.md)
- [0080da5c](../0080d/0080da5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 2596 bytes

~~~c

long FUN_00b2abcc(long *param_1,long *param_2)

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
      if (0xaaaaaaaaaaaaaaa < uVar9) goto LAB_00b2ada0;
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
    FUN_0054075c(local_78,lVar8,lVar2,(lVar2 - lVar8 >> 3) * -0x5555555555555555);
    local_70 = local_70 + 3;
    FUN_0080da5c(param_1,&local_80);
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
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00b2add8;
    FUN_00794b6c(param_1);
LAB_00b2ada0:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_00440ec0();
    }
  }
LAB_00b2add8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
