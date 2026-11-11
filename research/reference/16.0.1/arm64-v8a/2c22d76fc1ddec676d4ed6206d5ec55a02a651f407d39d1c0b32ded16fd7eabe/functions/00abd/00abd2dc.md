# 00abd2dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00abd2dc",
  "name": "FUN_00abd2dc",
  "size": 968,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07db65f7a8420cd9c72f940cd68facdbd0816d7548852814497763b73d03212c",
  "source_text_sha256": "07db65f7a8420cd9c72f940cd68facdbd0816d7548852814497763b73d03212c"
}
~~~

## 呼び出し元

- [00abe7f8](../00abe/00abe7f8.md)
- [00ac1d40](../00ac1/00ac1d40.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [0046da48](../0046d/0046da48.md)
- [00470840](../00470/00470840.md)
- [0049f3f0](../0049f/0049f3f0.md)
- [00615cd0](../00615/00615cd0.md)
- [00800378](../00800/00800378.md)
- [0080062c](../00800/0080062c.md)
- [008056ec](../00805/008056ec.md)
- [0080b3c8](../0080b/0080b3c8.md)
- [008514f8](../00851/008514f8.md)
- [00860588](../00860/00860588.md)
- [00a65dec](../00a65/00a65dec.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)

## 疑似コード / UTF-8 6993 bytes

~~~c

undefined4 FUN_00abd2dc(long param_1)

{
  undefined4 *puVar1;
  undefined4 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  int iVar9;
  undefined8 uVar10;
  ulong uVar11;
  void *__dest;
  undefined8 *puVar12;
  ulong uVar13;
  ulong uVar14;
  undefined8 *extraout_x8;
  undefined8 *puVar15;
  ulong uVar16;
  void *pvVar17;
  undefined4 *puVar18;
  long lVar19;
  void *local_a0;
  void *pvStack_98;
  undefined8 local_90;
  undefined8 *local_80;
  undefined8 *local_78;
  undefined8 *local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  if (*(int *)(param_1 + 0x38) == -1) {
LAB_00abd328:
    local_80 = (undefined8 *)0x0;
    local_78 = (undefined8 *)0x0;
    lVar19 = *(long *)(param_1 + 8);
    local_70 = (undefined8 *)0x0;
    if (*(long *)(param_1 + 0x10) == lVar19) {
      uVar7 = 1;
    }
    else {
      uVar11 = 0;
      do {
        if (-1 < *(int *)(lVar19 + uVar11 * 4)) {
          local_a0 = (void *)0x0;
          pvStack_98 = (void *)0x0;
          local_90 = 0;
          if (local_78 < local_70) {
            *local_78 = 0;
            local_78[1] = 0;
            local_78[2] = 0;
            local_78[1] = 0;
            *local_78 = 0;
            local_78[2] = 0;
            local_78 = local_78 + 3;
          }
          else {
            local_78 = (undefined8 *)FUN_00615cd0(&local_80,&local_a0);
            if (local_a0 != (void *)0x0) {
              pvStack_98 = local_a0;
              _ZdlPv(local_a0);
            }
          }
        }
        puVar12 = local_78;
        if (local_78 == local_80) {
          if (*(long *)(lVar3 + 0x28) != local_68) goto LAB_00abd6f4;
          FUN_0080b3c8(&local_80);
          goto LAB_00abd650;
        }
        if ((ulong)(*(long *)(param_1 + 0x10) - *(long *)(param_1 + 8) >> 2) <= uVar11) {
          if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
            FUN_0049f3f0((long *)(param_1 + 8));
          }
          goto LAB_00abd6f4;
        }
        uVar7 = FUN_0046da48(*(undefined4 *)(*(long *)(param_1 + 8) + uVar11 * 4));
        puVar2 = (undefined4 *)puVar12[-2];
        if (puVar2 < (undefined4 *)puVar12[-1]) {
          puVar18 = puVar2 + 1;
          *puVar2 = uVar7;
        }
        else {
          puVar15 = puVar12 + -3;
          pvVar17 = (void *)*puVar15;
          lVar19 = (long)puVar2 - (long)pvVar17 >> 2;
          uVar14 = lVar19 + 1;
          if (uVar14 >> 0x3e != 0) goto LAB_00abd66c;
          uVar13 = (long)puVar12[-1] - (long)pvVar17;
          uVar16 = (long)uVar13 >> 1;
          if (uVar16 <= uVar14) {
            uVar16 = uVar14;
          }
          if (0x7ffffffffffffffb < uVar13) {
            uVar16 = 0x3fffffffffffffff;
          }
          if (uVar16 == 0) {
            __dest = (void *)0x0;
          }
          else {
            if (uVar16 >> 0x3e != 0) {
              if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                FUN_00440ec0();
              }
              goto LAB_00abd6f4;
            }
            __dest = (void *)_Znwm(uVar16 << 2);
                    /* try { // try from 00abd45c to 00bbd603 has its CatchHandler @ 00abd45c
                       catch() { ... } // from try @ 00abd45c with catch @ 00abd45c
                       catch() { ... } // from try @ 00abd6f8 with catch @ 00abd45c */
          }
          puVar1 = (undefined4 *)((long)__dest + lVar19 * 4);
          puVar18 = puVar1 + 1;
          *puVar1 = uVar7;
          memcpy(__dest,pvVar17,(long)puVar2 - (long)pvVar17);
          puVar12[-3] = __dest;
          puVar12[-2] = puVar18;
          puVar12[-1] = (void *)((long)__dest + uVar16 * 4);
          if (pvVar17 != (void *)0x0) {
            _ZdlPv(pvVar17);
          }
        }
        puVar12[-2] = puVar18;
        uVar11 = uVar11 + 1;
        lVar19 = *(long *)(param_1 + 8);
      } while (uVar11 < (ulong)(*(long *)(param_1 + 0x10) - lVar19 >> 2));
      puVar12 = local_80;
      if (local_78 != local_80) {
        uVar11 = 0;
        do {
          uVar14 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
          if (uVar14 < uVar11 || uVar14 - uVar11 == 0) goto LAB_00abd650;
          lVar19 = local_80[uVar11 * 3];
          if ((local_80 + uVar11 * 3)[1] == lVar19) {
LAB_00abd580:
            uVar7 = 0;
            puVar12 = local_78;
            puVar15 = local_78;
            puVar5 = local_80;
            goto joined_r0x00abd5a8;
          }
          uVar14 = 0;
          while( true ) {
            uVar7 = *(undefined4 *)(lVar19 + uVar14 * 4);
            uVar8 = FUN_00800378(uVar7);
            uVar7 = FUN_0080062c(uVar7);
            iVar9 = *(int *)(param_1 + 0x3c);
            if (iVar9 == -1) {
              iVar9 = FUN_008056ec(uVar8,uVar7);
              iVar9 = iVar9 + -1;
            }
            iVar9 = FUN_00a65dec(uVar8,uVar7,iVar9,*(undefined4 *)(param_1 + 0x40),0);
            uVar16 = ((long)local_78 - (long)local_80 >> 3) * -0x5555555555555555;
            if (iVar9 != 0) break;
            if (uVar16 < uVar11 || uVar16 - uVar11 == 0) goto LAB_00abd650;
            uVar14 = uVar14 + 1;
            lVar19 = local_80[uVar11 * 3];
            if ((ulong)((local_80 + uVar11 * 3)[1] - lVar19 >> 2) <= uVar14) goto LAB_00abd580;
          }
          uVar11 = uVar11 + 1;
          puVar12 = local_78;
        } while (uVar11 <= uVar16 && uVar16 - uVar11 != 0);
      }
      uVar7 = 1;
      puVar15 = puVar12;
      puVar5 = local_80;
      if (local_80 != (undefined8 *)0x0) {
joined_r0x00abd5a8:
        while (puVar4 = puVar12, puVar6 = local_80, puVar4 != local_80) {
          puVar12 = puVar4 + -3;
          pvVar17 = (void *)*puVar12;
          puVar15 = puVar5;
          local_80 = puVar6;
          if (pvVar17 != (void *)0x0) {
            puVar4[-2] = pvVar17;
            local_80 = puVar5;
            _ZdlPv(pvVar17);
            puVar15 = local_80;
            puVar5 = local_80;
            local_80 = puVar6;
          }
        }
        local_78 = local_80;
        local_80 = puVar5;
        _ZdlPv(puVar15);
      }
    }
  }
  else {
    uVar10 = FUN_008514f8();
    uVar11 = FUN_00860588(uVar10,*(undefined4 *)(param_1 + 0x38));
    if ((uVar11 & 1) != 0) goto LAB_00abd328;
    uVar7 = 0;
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00abd604 to 00bbd6f7 has its CatchHandler @ 00abd7b8 */
    return uVar7;
  }
LAB_00abd6f4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
LAB_00abd650:
  if (*(long *)(lVar3 + 0x28) == local_68) {
    FUN_0080b3c8(&local_80);
    puVar15 = extraout_x8;
LAB_00abd66c:
    if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
      FUN_00470840(puVar15);
    }
  }
  goto LAB_00abd6f4;
}

~~~
