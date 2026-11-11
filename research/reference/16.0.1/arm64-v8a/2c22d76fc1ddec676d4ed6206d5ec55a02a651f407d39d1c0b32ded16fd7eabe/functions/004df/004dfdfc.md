# 004dfdfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "004dfdfc",
  "name": "_ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE",
  "size": 1432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3b9ddd202beb206003f0b7ddc720ba41c067d390b320ccf3fecb9390e6803ac",
  "source_text_sha256": "c3b9ddd202beb206003f0b7ddc720ba41c067d390b320ccf3fecb9390e6803ac"
}
~~~

## 呼び出し元

- [00c59320](../00c59/00c59320.md)

## 呼び出し先

- [0043ddd8](../0043d/0043ddd8.md)
- [004aec64](../004ae/004aec64.md)
- [004b87b4](../004b8/004b87b4.md)
- [004b9c38](../004b9/004b9c38.md)
- [00540920](../00540/00540920.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)
- [00c58090](../00c58/00c58090.md)
- [00c58660](../00c58/00c58660.md)
- [00c58ac0](../00c58/00c58ac0.md)
- [00c58ad0](../00c58/00c58ad0.md)
- [00c58b20](../00c58/00c58b20.md)
- [00c58b40](../00c58/00c58b40.md)
- [00c58c40](../00c58/00c58c40.md)
- [00c58ca0](../00c58/00c58ca0.md)
- [00c58cb0](../00c58/00c58cb0.md)
- [00c58cc0](../00c58/00c58cc0.md)
- [0112a058](../0112a/0112a058.md)

## 関連文字列（未確認候補）

~~~text
"Modular_Reducer: Never initalized"
~~~

## 疑似コード / UTF-8 7948 bytes

~~~c

void _ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE
               (undefined8 *param_1,long *param_2,long *param_3)

{
  long lVar1;
  long lVar2;
  long lVar3;
  int *piVar4;
  void *pvVar5;
  void *pvVar6;
  int iVar7;
  undefined8 uVar8;
  long lVar9;
  size_t sVar10;
  long lVar11;
  long lVar12;
  ulong uVar13;
  ulong uVar14;
  long lVar15;
  void *local_c0;
  void *local_b8;
  long local_b0;
  undefined4 local_a8;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  int local_88;
  int *local_78;
  int *local_70;
  long local_68;
  undefined4 local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  if (param_2[0xc] == 0) {
    uVar8 = __cxa_allocate_exception(0x20);
    FUN_0043ddd8(&local_78,"Modular_Reducer: Never initalized");
    FUN_004aec64(uVar8,&local_78);
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar8,PTR__ZTIN5Botan13Invalid_StateE_00c9ad48,FUN_00535868);
    }
  }
  else {
    lVar9 = *param_3;
    lVar12 = param_3[1];
    lVar11 = lVar12 - lVar9;
    lVar15 = lVar11 >> 2;
    lVar1 = lVar15;
    while ((lVar11 != 0 && (*(int *)(lVar9 + -4 + lVar1 * 4) == 0))) {
      lVar1 = lVar1 + -1;
      lVar11 = lVar1;
    }
    lVar2 = param_2[1] - *param_2;
    lVar11 = lVar2 >> 2;
    if (lVar2 != 0) {
      do {
        if (*(int *)(*param_2 + -4 + lVar11 * 4) != 0) break;
        lVar11 = lVar11 + -1;
      } while (lVar11 != 0);
    }
    iVar7 = FUN_004b87b4(lVar9,lVar1);
    if (iVar7 < 0) {
      if ((int)param_3[3] == 0) {
        if (*(long *)(lVar3 + 0x28) == local_58) {
          _ZN5BotanplERKNS_6BigIntES2_(param_1,param_3,param_2);
          return;
        }
      }
      else if (*(long *)(lVar3 + 0x28) == local_58) {
        _ZN5Botan6BigIntC2ERKS0_(param_1,param_3);
        return;
      }
    }
    else {
      if (lVar12 != lVar9) {
        do {
          if (*(int *)(lVar9 + -4 + lVar15 * 4) != 0) break;
          lVar15 = lVar15 + -1;
        } while (lVar15 != 0);
      }
      lVar1 = param_2[5] - param_2[4];
      lVar12 = lVar1 >> 2;
      if (lVar1 != 0) {
        do {
          if (*(int *)(param_2[4] + -4 + lVar12 * 4) != 0) break;
          lVar12 = lVar12 + -1;
        } while (lVar12 != 0);
      }
      iVar7 = FUN_004b87b4(lVar9,lVar15);
      if (iVar7 < 0) {
        _ZN5Botan6BigIntC2ERKS0_(&local_78,param_3);
        local_60 = 1;
        uVar14 = param_2[0xc] * 0x20 - 0x20;
        if (uVar14 != 0) {
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          lVar12 = (long)local_70 - (long)local_78;
          while ((lVar12 != 0 && (local_78[lVar9 + -1] == 0))) {
            lVar9 = lVar9 + -1;
            lVar12 = lVar9;
          }
          FUN_004b9c38(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004e0008:
            do {
              if (lVar9 == 0) goto LAB_004e001c;
              if (*piVar4 != 0) goto LAB_004e0024;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004e0008;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004e001c:
          local_60 = 1;
        }
LAB_004e0024:
        _ZN5Botan6BigIntmLERKS0_(&local_78,param_2 + 8);
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 != 0) {
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          lVar12 = (long)local_70 - (long)local_78;
          while ((lVar12 != 0 && (local_78[lVar9 + -1] == 0))) {
            lVar9 = lVar9 + -1;
            lVar12 = lVar9;
          }
          FUN_004b9c38(local_78,lVar9,uVar14 >> 5,0);
          lVar9 = (long)local_70 - (long)local_78 >> 2;
          piVar4 = local_78;
          if ((long)local_70 - (long)local_78 == 0) {
joined_r0x004e0098:
            do {
              if (lVar9 == 0) goto LAB_004e00ac;
              if (*piVar4 != 0) goto LAB_004e00b4;
              lVar9 = lVar9 + -1;
              piVar4 = piVar4 + 1;
            } while( true );
          }
          do {
            if (local_78[lVar9 + -1] != 0) goto joined_r0x004e0098;
            lVar9 = lVar9 + -1;
          } while (lVar9 != 0);
LAB_004e00ac:
          local_60 = 1;
        }
LAB_004e00b4:
        _ZN5Botan6BigIntmLERKS0_(&local_78,param_2);
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 == 0) {
          if ((long)local_70 - (long)local_78 != 0) {
            memset(local_78,0,(long)local_70 - (long)local_78);
          }
        }
        else {
          uVar14 = uVar14 >> 5;
          uVar13 = (long)local_70 - (long)local_78 >> 2;
          if (uVar14 < uVar13) {
            lVar9 = uVar13 - (uVar14 + 1);
            if ((lVar9 != 0) && (sVar10 = lVar9 * 4, sVar10 != 0)) {
              memset(local_78 + uVar14 + 1,0,sVar10);
            }
            local_78[uVar14] = 0;
          }
        }
        _ZN5Botan6BigIntC2ERKS0_(&local_a0,param_3);
        local_88 = 1;
        uVar14 = param_2[0xc] * 0x20 + 0x20;
        if (uVar14 == 0) {
          if (pvStack_98 != local_a0) {
            memset(local_a0,0,(long)pvStack_98 - (long)local_a0);
          }
        }
        else {
          uVar13 = (long)pvStack_98 - (long)local_a0 >> 2;
          uVar14 = uVar14 >> 5;
          if (uVar14 < uVar13) {
            lVar9 = uVar13 - (uVar14 + 1);
            if ((lVar9 != 0) && (sVar10 = lVar9 * 4, sVar10 != 0)) {
              memset((void *)((long)local_a0 + (uVar14 + 1) * 4),0,sVar10);
            }
            *(undefined4 *)((long)local_a0 + uVar14 * 4) = 0;
          }
        }
        _ZN5Botan6BigIntmIERKS0_(&local_a0,&local_78);
        if (local_88 == 0) {
          local_b8 = (void *)0x0;
          local_b0 = 0;
          local_c0 = (void *)0x0;
          uVar13 = param_2[0xc] + 1U & 0x7ffffffffffffff;
          uVar14 = uVar13 + 1;
          local_a8 = 1;
          lVar9 = 0;
          if ((uVar14 & 7) != 0) {
            lVar9 = 8 - (uVar14 & 7);
          }
          FUN_00540920(&local_c0,lVar9 + uVar14);
          lVar9 = uVar13 * 4;
          *(uint *)((long)local_c0 + lVar9) = *(uint *)((long)local_c0 + lVar9) | 1;
          _ZN5Botan6BigIntpLERKS0_(&local_a0,&local_c0);
          pvVar5 = local_c0;
          if (local_c0 != (void *)0x0) {
            local_b8 = local_c0;
            (*(code *)PTR_memset_00c67738)(local_c0,0,local_b0 - (long)local_c0);
            free(pvVar5);
          }
        }
        while (iVar7 = _ZNK5Botan6BigInt3cmpERKS0_b(&local_a0,param_2,1), lVar9 = local_90,
              pvVar6 = pvStack_98, pvVar5 = local_a0, -1 < iVar7) {
          _ZN5Botan6BigIntmIERKS0_(&local_a0,param_2);
        }
        if ((int)param_3[3] == 1) {
          local_a0 = (void *)0x0;
          pvStack_98 = (void *)0x0;
          local_90 = 0;
          param_1[2] = lVar9;
          param_1[1] = pvVar6;
          *param_1 = pvVar5;
          *(int *)(param_1 + 3) = local_88;
        }
        else {
          _ZN5BotanmiERKNS_6BigIntES2_(param_1,param_2,&local_a0);
          pvVar5 = local_a0;
          if (local_a0 != (void *)0x0) {
            pvStack_98 = local_a0;
            (*(code *)PTR_memset_00c67738)(local_a0,0,local_90 - (long)local_a0);
            free(pvVar5);
          }
        }
        if (local_78 != (int *)0x0) {
          local_70 = local_78;
          (*(code *)PTR_memset_00c67738)(local_78,0,local_68 - (long)local_78);
          free(local_78);
        }
        if (*(long *)(lVar3 + 0x28) == local_58) {
          return;
        }
      }
      else if (*(long *)(lVar3 + 0x28) == local_58) {
        _ZN5BotanrmERKNS_6BigIntES2_(param_1,param_3,param_2);
        return;
      }
    }
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
