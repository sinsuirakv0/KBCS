# 00acafc4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00acafc4",
  "name": "FUN_00acafc4",
  "size": 656,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8891e93fac1ef4c78ddad3caf4e8b602c0f6341fea7766c101f9b1c8b7f74089",
  "source_text_sha256": "8891e93fac1ef4c78ddad3caf4e8b602c0f6341fea7766c101f9b1c8b7f74089"
}
~~~

## 呼び出し元

- [007890e0](../00789/007890e0.md)
- [0082fe24](../0082f/0082fe24.md)
- [008cbbc0](../008cb/008cbbc0.md)
- [008ff9e4](../008ff/008ff9e4.md)
- [00a3eea0](../00a3e/00a3eea0.md)
- [00ac14b8](../00ac1/00ac14b8.md)

## 呼び出し先

- [0046cd24](../0046c/0046cd24.md)
- [0048a2ac](../0048a/0048a2ac.md)
- [005d8fb8](../005d8/005d8fb8.md)
- [008524fc](../00852/008524fc.md)
- [008b7f1c](../008b7/008b7f1c.md)
- [008b7ff0](../008b7/008b7ff0.md)
- [00a477cc](../00a47/00a477cc.md)
- [00a47910](../00a47/00a47910.md)
- [00a47944](../00a47/00a47944.md)
- [00acc5a8](../00acc/00acc5a8.md)
- [00acc5ac](../00acc/00acc5ac.md)
- [00c54d90](../00c54/00c54d90.md)
- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 疑似コード / UTF-8 3023 bytes

~~~c

void FUN_00acafc4(long param_1,undefined8 param_2,undefined8 param_3,undefined4 param_4)

{
  long lVar1;
  undefined *puVar2;
  undefined *puVar3;
  int iVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined ***pppuVar8;
  long *plVar9;
  long *local_a8;
  long *local_a0;
  long *local_98;
  undefined **local_90 [4];
  undefined ***local_70;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  *(undefined4 *)(param_1 + 8) = param_4;
  FUN_008524fc();
  iVar4 = FUN_0046cd24();
  lVar5 = FUN_0048a2ac(param_3,0xb);
  iVar4 = iVar4 - *(int *)(lVar5 + 8);
  FUN_00a47944(&local_98,param_2,iVar4 + 0x2d,0x261,0x15);
  (**(code **)(*local_98 + 0x10))(local_98,1);
  FUN_00a47910(0x3f800000,0x3f800000);
  plVar6 = local_98;
  FUN_00a47944(&local_a8,param_2,0x1c,0xfffffff8,0x12);
  local_a0 = local_a8;
  local_a8 = (long *)0x0;
  plVar6 = (long *)FUN_00a477cc(plVar6,&local_a0);
  (**(code **)(*plVar6 + 0x10))(plVar6,1);
  plVar6 = local_a0;
  puVar2 = PTR_DAT_00c9c408;
  local_a0 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    *plVar6 = (long)(PTR_DAT_00c9c408 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  plVar6 = local_a8;
  puVar3 = PTR_DAT_00c9c410;
  local_a8 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    plVar9 = (long *)plVar6[0x16];
    *plVar6 = (long)(PTR_DAT_00c9c410 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  lVar5 = FUN_008524fc();
  local_70 = local_90;
  local_a0 = local_98;
  local_98 = (long *)0x0;
  local_90[0] = &PTR_FUN_00c8e8e0;
  uVar7 = FUN_008b7ff0(lVar5 + 0x2f38,*(undefined4 *)(param_1 + 8),iVar4 + -2,0x238,0x4b,0x52,
                       &local_a0,local_90);
  FUN_008b7f1c(uVar7,0);
  if (local_70 == local_90) {
    lVar5 = 0x20;
    pppuVar8 = local_90;
  }
  else {
    if (local_70 == (undefined ***)0x0) goto LAB_00acb1a4;
    lVar5 = 0x28;
    pppuVar8 = local_70;
  }
  (**(code **)((long)*pppuVar8 + lVar5))();
LAB_00acb1a4:
  plVar6 = local_a0;
  local_a0 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  plVar6 = local_98;
  local_98 = (long *)0x0;
  if (plVar6 != (long *)0x0) {
    plVar9 = (long *)plVar6[0x16];
    *plVar6 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar5 = FUN_00c54d90(0xffffffffffffffff,plVar9 + 1), lVar5 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar6 = (long)(puVar2 + 0x10);
    FUN_005d8fb8(plVar6 + 10);
    _ZdlPv(plVar6);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
