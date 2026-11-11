# 00a9edec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00a9edec",
  "name": "FUN_00a9edec",
  "size": 856,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa43ae8a97754eba4b4080e55f19a913f920dceae6fba7b7a9de9b8b08b308f3",
  "source_text_sha256": "fa43ae8a97754eba4b4080e55f19a913f920dceae6fba7b7a9de9b8b08b308f3"
}
~~~

## 呼び出し元

- [00a9c6f0](../00a9c/00a9c6f0.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [008001ec](../00800/008001ec.md)
- [00804074](../00804/00804074.md)
- [0080645c](../00806/0080645c.md)
- [00806614](../00806/00806614.md)
- [008514f8](../00851/008514f8.md)
- [00860588](../00860/00860588.md)
- [009a9760](../009a9/009a9760.md)
- [009a9770](../009a9/009a9770.md)
- [009ad980](../009ad/009ad980.md)
- [009b1e90](../009b1/009b1e90.md)
- [00a31b78](../00a31/00a31b78.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)

## 疑似コード / UTF-8 5534 bytes

~~~c

undefined4 FUN_00a9edec(undefined8 param_1,long *param_2,uint param_3)

{
  int iVar1;
  long lVar2;
  byte bVar3;
  undefined4 uVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  undefined8 *__dest;
  ulong uVar8;
  ulong uVar9;
  undefined8 *puVar10;
  undefined8 *puVar11;
  undefined8 uVar12;
  undefined8 *puVar13;
  size_t __n;
  undefined8 *local_98;
  undefined8 *local_90;
  undefined8 *local_88;
  undefined8 *local_80;
  undefined8 *local_78;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  lVar6 = FUN_008514f8();
  iVar5 = *(int *)(*param_2 + 0x20);
  iVar1 = *(int *)(*param_2 + 100);
  FUN_009ad980(&local_80,*(undefined8 *)(lVar6 + 0x2268));
  local_98 = (undefined8 *)0x0;
  local_90 = (undefined8 *)0x0;
  local_88 = (undefined8 *)0x0;
  puVar11 = local_80;
  if (local_80 == local_78) {
    uVar4 = 1;
    puVar11 = local_90;
  }
  else {
    do {
      uVar12 = *puVar11;
      uVar4 = FUN_009a9760(uVar12);
      uVar4 = FUN_008001ec(4,uVar4);
      if (iVar5 == 6) {
        lVar7 = FUN_00a31b78(lVar6 + 0x510,uVar4);
        puVar13 = local_98;
        if (lVar7 != 0) {
                    /* try { // try from 00a9eea8 to 00b9eeef has its CatchHandler @ 00aa134c */
          if (local_90 < local_88) goto LAB_00a9ee60;
          __n = (long)local_90 - (long)local_98;
          lVar7 = (long)__n >> 3;
          uVar8 = lVar7 + 1;
          if (uVar8 >> 0x3d != 0) {
LAB_00a9f10c:
            if (*(long *)(lVar2 + 0x28) == local_68) {
              FUN_009b1e90(&local_98);
              goto LAB_00a9f128;
            }
            goto LAB_00a9f194;
          }
          uVar9 = (long)local_88 - (long)local_98 >> 2;
          if (uVar9 <= uVar8) {
            uVar9 = uVar8;
          }
          if (0x7ffffffffffffff7 < (ulong)((long)local_88 - (long)local_98)) {
            uVar9 = 0x1fffffffffffffff;
          }
          if (uVar9 == 0) {
LAB_00a9ef6c:
            __dest = (undefined8 *)0x0;
            puVar13 = local_98;
          }
          else {
            if (uVar9 >> 0x3d != 0) goto LAB_00a9f128;
            __dest = (undefined8 *)_Znwm(uVar9 << 3);
          }
LAB_00a9ef70:
          puVar10 = __dest + lVar7 + 1;
          __dest[lVar7] = uVar12;
          memcpy(__dest,puVar13,__n);
          local_98 = __dest;
          local_90 = puVar10;
          local_88 = __dest + uVar9;
          if (puVar13 != (undefined8 *)0x0) {
            _ZdlPv(puVar13);
            local_90 = puVar10;
          }
        }
      }
      else {
                    /* try { // try from 00a9ef00 to 00b9f3a7 has its CatchHandler @ 00aa1348 */
        lVar7 = FUN_00a31b78(lVar6 + 0x510,uVar4);
        puVar13 = local_98;
        if (lVar7 == 0) {
          if (local_88 <= local_90) {
            __n = (long)local_90 - (long)local_98;
            lVar7 = (long)__n >> 3;
            uVar8 = lVar7 + 1;
            if (uVar8 >> 0x3d != 0) goto LAB_00a9f10c;
            uVar9 = (long)local_88 - (long)local_98 >> 2;
            if (uVar9 <= uVar8) {
              uVar9 = uVar8;
            }
            if (0x7ffffffffffffff7 < (ulong)((long)local_88 - (long)local_98)) {
              uVar9 = 0x1fffffffffffffff;
            }
            if (uVar9 == 0) goto LAB_00a9ef6c;
            if (uVar9 >> 0x3d == 0) {
              __dest = (undefined8 *)_Znwm(uVar9 << 3);
              goto LAB_00a9ef70;
            }
LAB_00a9f128:
            if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440ec0();
            }
            goto LAB_00a9f194;
          }
LAB_00a9ee60:
          *local_90 = uVar12;
          local_90 = local_90 + 1;
        }
      }
      puVar13 = local_90;
      puVar11 = puVar11 + 1;
    } while (puVar11 != local_78);
    if (local_98 == local_90) {
      uVar4 = 1;
      puVar11 = local_90;
    }
    else {
      puVar11 = local_98;
      if (iVar1 == 1) {
        do {
          uVar12 = *puVar11;
          iVar5 = FUN_009a9770(uVar12);
          uVar4 = FUN_009a9760(uVar12);
          if ((param_3 & 1) == 0) {
            if (iVar5 - 1U < 2) goto LAB_00a9f048;
          }
          else {
            uVar8 = FUN_00804074(4,uVar4);
            if (((uVar8 & 1) != 0) && (uVar8 = FUN_00806614(4,uVar4), (uVar8 & 1) != 0)) {
              uVar4 = FUN_0080645c(4,uVar4);
              bVar3 = FUN_00860588(lVar6,uVar4);
              if ((iVar5 - 1U < 2 & bVar3) != 0) goto LAB_00a9f048;
            }
          }
          puVar11 = puVar11 + 1;
        } while (puVar11 != puVar13);
LAB_00a9f090:
        uVar4 = 1;
        puVar13 = local_98;
        puVar11 = local_90;
      }
      else {
        do {
          iVar5 = FUN_009a9770(*puVar11);
          if (iVar1 == 0) {
            if (iVar5 != 0) goto LAB_00a9f090;
          }
          else if (iVar1 == 2) {
            if (iVar5 != 3) goto LAB_00a9f090;
          }
          else if ((iVar1 == 3) && (iVar5 != 4)) goto LAB_00a9f090;
          puVar11 = puVar11 + 1;
        } while (puVar11 != puVar13);
LAB_00a9f048:
        uVar4 = 0;
        puVar13 = local_98;
        puVar11 = local_90;
      }
    }
    local_90 = puVar13;
    if (local_90 != (undefined8 *)0x0) {
      _ZdlPv(local_90);
      puVar11 = local_90;
    }
  }
  local_90 = puVar11;
  if (local_80 != (undefined8 *)0x0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar4;
  }
LAB_00a9f194:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
