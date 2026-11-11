# 00ac9aec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ac9aec",
  "name": "FUN_00ac9aec",
  "size": 996,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "362079c43759e15534431f383f3059d1b6fb256ee7449c2294c176ff771debc7",
  "source_text_sha256": "362079c43759e15534431f383f3059d1b6fb256ee7449c2294c176ff771debc7"
}
~~~

## 呼び出し元

- [00788cac](../00788/00788cac.md)
- [0082ee20](../0082e/0082ee20.md)
- [008cabc0](../008ca/008cabc0.md)
- [008d1c40](../008d1/008d1c40.md)
- [008fe9e4](../008fe/008fe9e4.md)
- [00a3de58](../00a3d/00a3de58.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [005d8bc8](../005d8/005d8bc8.md)
- [008514f8](../00851/008514f8.md)
- [008b6f18](../008b6/008b6f18.md)
- [008b6f30](../008b6/008b6f30.md)
- [008b6fec](../008b6/008b6fec.md)
- [00a46784](../00a46/00a46784.md)
- [00a468c8](../00a46/00a468c8.md)
- [00a468d8](../00a46/00a468d8.md)
- [00a468fc](../00a46/00a468fc.md)
- [00ac871c](../00ac8/00ac871c.md)
- [00acb3e0](../00acb/00acb3e0.md)
- [00acb3e4](../00acb/00acb3e4.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 6498 bytes

~~~c

void FUN_00ac9aec(long param_1,undefined8 param_2,undefined4 param_3,long *param_4)

{
  long lVar1;
  undefined *puVar2;
  undefined *puVar3;
  long *plVar4;
  long **pplVar5;
  undefined8 uVar6;
  undefined ***pppuVar7;
  long lVar8;
  long *plVar9;
  long *local_d0;
  long *local_c8;
  undefined **local_c0 [4];
  undefined ***local_a0;
  long *local_90 [4];
  long **local_70;
  long local_58;
  
                    /* catch() { ... } // from try @ 00ac96f4 with catch @ 00ac9af0 */
                    /* catch() { ... } // from try @ 00ac96e4 with catch @ 00ac9af4 */
                    /* catch() { ... } // from try @ 00ac99d0 with catch @ 00ac9afc */
                    /* catch() { ... } // from try @ 00ac95e0 with catch @ 00ac9b00
                       catch() { ... } // from try @ 00ac99c0 with catch @ 00ac9b00 */
                    /* catch() { ... } // from try @ 00ac9764 with catch @ 00ac9b08 */
  lVar1 = tpidr_el0;
                    /* catch() { ... } // from try @ 00ac959c with catch @ 00ac9b10 */
                    /* catch() { ... } // from try @ 00ac958c with catch @ 00ac9b14 */
  local_58 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00ac96cc with catch @ 00ac9b1c */
  *(undefined4 *)(param_1 + 4) = param_3;
                    /* catch() { ... } // from try @ 00ac99b4 with catch @ 00ac9b20 */
  plVar4 = (long *)param_4[4];
                    /* catch() { ... } // from try @ 00ac9838 with catch @ 00ac9b24 */
  if (plVar4 == (long *)0x0) {
                    /* catch() { ... } // from try @ 00ac9530 with catch @ 00ac9b44 */
    local_70 = (long **)0x0;
                    /* catch() { ... } // from try @ 00ac9900 with catch @ 00ac9b48
                       catch() { ... } // from try @ 00ac9ae0 with catch @ 00ac9b48 */
  }
  else {
                    /* catch() { ... } // from try @ 00ac977c with catch @ 00ac9b28 */
                    /* catch() { ... } // from try @ 00ac9a10 with catch @ 00ac9b2c */
    if (plVar4 == param_4) {
      local_70 = local_90;
                    /* catch() { ... } // from try @ 00ac992c with catch @ 00ac9b50 */
                    /* catch() { ... } // from try @ 00ac985c with catch @ 00ac9b60
                       catch() { ... } // from try @ 00ac9ac8 with catch @ 00ac9b60 */
      (**(code **)(*param_4 + 0x18))(param_4,local_90);
    }
    else {
                    /* catch() { ... } // from try @ 00ac9978 with catch @ 00ac9b34 */
      local_70 = (long **)(**(code **)(*plVar4 + 0x10))();
                    /* catch() { ... } // from try @ 00ac9a28 with catch @ 00ac9b3c */
                    /* catch() { ... } // from try @ 00ac97b8 with catch @ 00ac9b40 */
    }
  }
                    /* catch() { ... } // from try @ 00ac98a4 with catch @ 00ac9b68 */
  FUN_0057bea8(local_90,param_1 + 0xb0);
  if (local_70 == local_90) {
    lVar8 = 0x20;
    pplVar5 = local_90;
LAB_00ac9b98:
    (**(code **)((long)*pplVar5 + lVar8))();
  }
  else if (local_70 != (long **)0x0) {
    lVar8 = 0x28;
    pplVar5 = local_70;
    goto LAB_00ac9b98;
  }
  FUN_00ac871c(param_1,4,0x21d,0x5f,0x5f);
  FUN_00a468fc(local_90,param_2,0x33,0x24c,9);
  (**(code **)(*local_90[0] + 0x10))(local_90[0],1);
  FUN_00a468c8(0x3f800000,0x3f800000);
  plVar4 = local_90[0];
  FUN_00a468fc(&local_d0,param_2,0xffffffff,0,3);
  local_c8 = local_d0;
  local_d0 = (long *)0x0;
  plVar4 = (long *)FUN_00a46784(plVar4,&local_c8);
  (**(code **)(*plVar4 + 0x10))(plVar4,1);
  plVar4 = local_c8;
  puVar2 = PTR_DAT_00c9b368;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(PTR_DAT_00c9b368 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_d0;
  puVar3 = PTR_DAT_00c9b370;
  local_d0 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(PTR_DAT_00c9b370 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_90[0];
  FUN_00a468fc(&local_d0,param_2,0,0,0xc);
  local_c8 = local_d0;
  local_d0 = (long *)0x0;
  plVar4 = (long *)FUN_00a46784(plVar4,&local_c8);
  (**(code **)(*plVar4 + 0x10))(plVar4,1);
  uVar6 = FUN_00a468c8(0x40000000,0x40000000);
  FUN_00a468d8(uVar6,0);
  plVar4 = local_c8;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_d0;
  local_d0 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  lVar8 = FUN_008514f8();
  local_c8 = local_90[0];
  local_a0 = local_c0;
  local_90[0] = (long *)0x0;
  local_c0[0] = &PTR_FUN_00c8d7c0;
  uVar6 = FUN_008b6fec(lVar8 + 0x2f38,*(undefined4 *)(param_1 + 4),4,0x21d,0x5f,0x5f,&local_c8,
                       local_c0);
  uVar6 = FUN_008b6f18(uVar6,0);
  FUN_008b6f30(uVar6,1);
  if (local_a0 == local_c0) {
    lVar8 = 0x20;
    pppuVar7 = local_c0;
  }
  else {
    if (local_a0 == (undefined ***)0x0) goto LAB_00ac9e20;
    lVar8 = 0x28;
    pppuVar7 = local_a0;
  }
  (**(code **)((long)*pppuVar7 + lVar8))();
LAB_00ac9e20:
  plVar4 = local_c8;
  local_c8 = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  plVar4 = local_90[0];
  local_90[0] = (long *)0x0;
  if (plVar4 != (long *)0x0) {
    plVar9 = (long *)plVar4[0x16];
    *plVar4 = (long)(puVar3 + 0x10);
    if ((plVar9 != (long *)0x0) && (lVar8 = FUN_00c53d00(0xffffffffffffffff,plVar9 + 1), lVar8 == 0)
       ) {
      (**(code **)(*plVar9 + 0x10))(plVar9);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar9);
    }
    *plVar4 = (long)(puVar2 + 0x10);
    FUN_005d8bc8(plVar4 + 10);
    _ZdlPv(plVar4);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
