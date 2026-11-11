# 00a2dddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00a2dddc",
  "name": "FUN_00a2dddc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "49be9be86752d039ca7e895eca198b29b7a5fdcf0839a1e9a0433e974f665bc9",
  "source_text_sha256": "49be9be86752d039ca7e895eca198b29b7a5fdcf0839a1e9a0433e974f665bc9"
}
~~~

## 呼び出し元

- [00a2b2e8](../00a2b/00a2b2e8.md)

## 呼び出し先

- [00480b90](../00480/00480b90.md)
- [00480d48](../00480/00480d48.md)
- [00480e28](../00480/00480e28.md)
- [005c179c](../005c1/005c179c.md)
- [00691800](../00691/00691800.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 3340 bytes

~~~c

void FUN_00a2dddc(long *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  byte bVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  long *plVar6;
  bool bVar7;
  undefined8 *puVar8;
  long *plVar9;
  long *plVar10;
  undefined8 *puVar11;
  undefined8 *local_80;
  undefined8 local_78;
  ulong local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  FUN_00480b90(param_2,(short)param_1[5]);
  plVar9 = (long *)param_1[3];
  while (plVar9 != param_1 + 4) {
    bVar2 = *(byte *)(plVar9 + 4);
    FUN_00480b90(param_2,*(undefined4 *)((long)plVar9 + 0x1c));
    FUN_00480d48(param_2,bVar2 & 1);
    plVar6 = (long *)plVar9[1];
    plVar10 = plVar9;
    if ((long *)plVar9[1] == (long *)0x0) {
      do {
        plVar9 = (long *)plVar10[2];
        bVar7 = (long *)*plVar9 != plVar10;
        plVar10 = plVar9;
      } while (bVar7);
    }
    else {
      do {
        plVar9 = plVar6;
        plVar6 = (long *)*plVar9;
      } while ((long *)*plVar9 != (long *)0x0);
    }
  }
  FUN_00480b90(param_2,(short)param_1[8]);
  plVar9 = (long *)param_1[6];
  if (plVar9 != param_1 + 7) {
    do {
      lVar4 = plVar9[4];
      local_78 = 0;
      local_70 = 0;
      local_80 = &local_78;
      FUN_00691800(&local_80,plVar9[5],plVar9 + 6);
      FUN_00480b90(param_2,(int)lVar4);
      FUN_00480b90(param_2,local_70 & 0xffff);
      puVar8 = local_80;
      while (puVar8 != &local_78) {
        uVar1 = *(undefined4 *)(puVar8 + 4);
        FUN_00480b90(param_2,*(undefined4 *)((long)puVar8 + 0x1c));
        FUN_00480b90(param_2,uVar1);
        puVar5 = (undefined8 *)puVar8[1];
        puVar11 = puVar8;
        if ((undefined8 *)puVar8[1] == (undefined8 *)0x0) {
          do {
            puVar8 = (undefined8 *)puVar11[2];
            bVar7 = (undefined8 *)*puVar8 != puVar11;
            puVar11 = puVar8;
          } while (bVar7);
        }
        else {
          do {
            puVar8 = puVar5;
            puVar5 = (undefined8 *)*puVar8;
          } while ((undefined8 *)*puVar8 != (undefined8 *)0x0);
        }
      }
      FUN_005c179c(&local_80,local_78);
      plVar6 = (long *)plVar9[1];
      plVar10 = plVar9;
      if ((long *)plVar9[1] == (long *)0x0) {
        do {
          plVar9 = (long *)plVar10[2];
          bVar7 = (long *)*plVar9 != plVar10;
          plVar10 = plVar9;
        } while (bVar7);
      }
      else {
        do {
          plVar9 = plVar6;
          plVar6 = (long *)*plVar9;
        } while ((long *)*plVar9 != (long *)0x0);
      }
    } while (plVar9 != param_1 + 7);
  }
  FUN_00480b90(param_2,(short)param_1[2]);
  plVar9 = (long *)*param_1;
  while (plVar9 != param_1 + 1) {
    uVar1 = *(undefined4 *)(plVar9 + 4);
    FUN_00480b90(param_2,*(undefined4 *)((long)plVar9 + 0x1c));
    FUN_00480e28(param_2,uVar1);
    plVar6 = (long *)plVar9[1];
    plVar10 = plVar9;
    if ((long *)plVar9[1] == (long *)0x0) {
      do {
        plVar9 = (long *)plVar10[2];
        bVar7 = (long *)*plVar9 != plVar10;
        plVar10 = plVar9;
      } while (bVar7);
    }
    else {
      do {
        plVar9 = plVar6;
        plVar6 = (long *)*plVar9;
      } while ((long *)*plVar9 != (long *)0x0);
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
