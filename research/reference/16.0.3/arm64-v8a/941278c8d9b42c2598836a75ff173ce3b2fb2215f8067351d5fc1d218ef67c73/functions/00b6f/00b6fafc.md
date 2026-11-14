# 00b6fafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b6fafc",
  "name": "_ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 652,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "881e031e4b9d3b940aff366a9057494a1afd1ca8bcbae5afc4c2a59a6715a626",
  "source_text_sha256": "881e031e4b9d3b940aff366a9057494a1afd1ca8bcbae5afc4c2a59a6715a626"
}
~~~

## 呼び出し元

- [00c5d810](../00c5d/00c5d810.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59020](../00c59/00c59020.md)
- [00c59150](../00c59/00c59150.md)
- [00c5d080](../00c5d/00c5d080.md)
- [00c5d0a0](../00c5d/00c5d0a0.md)
- [00c5d7c0](../00c5d/00c5d7c0.md)

## 疑似コード / UTF-8 4173 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long param_1,undefined8 param_2)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  void *pvVar4;
  ulong *puVar5;
  ulong uVar6;
  byte local_b0 [8];
  ulong local_a8;
  void *local_a0;
  byte local_98 [16];
  void *local_88;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  long local_48;
  
  lVar3 = tpidr_el0;
  local_48 = *(long *)(lVar3 + 0x28);
  lVar1 = param_1 + 0x140;
  if ((*(byte *)(param_1 + 0x140) & 1) == 0) {
    if (*(byte *)(param_1 + 0x140) >> 1 != 0) {
LAB_00b6fb48:
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                (lVar1,&DAT_002b4cef,1);
    }
  }
  else if (*(long *)(param_1 + 0x148) != 0) goto LAB_00b6fb48;
  if ((*(byte *)(param_1 + 0x590) & 1) == 0) {
    if (*(byte *)(param_1 + 0x590) >> 1 != 0) goto LAB_00b6fb70;
LAB_00b6fb94:
    uVar6 = 0;
    uStack_58 = 0;
    local_50 = (void *)0x0;
    local_60 = 0;
  }
  else {
    if (*(long *)(param_1 + 0x598) == 0) goto LAB_00b6fb94;
LAB_00b6fb70:
    _ZN11flatbuffers12AbsolutePathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
              (&local_60,param_1 + 0x590);
    uVar6 = local_60 & 0xff;
  }
  uVar2 = uVar6 >> 1;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((uVar6 & 1) != 0) {
    uVar2 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar2)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((*(byte *)(param_1 + 0x590) & 1) == 0) {
    if (*(byte *)(param_1 + 0x590) >> 1 == 0) goto LAB_00b6fc04;
  }
  else if (*(long *)(param_1 + 0x598) == 0) goto LAB_00b6fc04;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
            (lVar1,&DAT_002b0a42,1);
LAB_00b6fc04:
  _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_98,*(undefined4 *)(param_1 + 0x18));
  puVar5 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (local_98,&DAT_002bd7f8,2);
  uStack_78 = puVar5[1];
  local_80 = *puVar5;
  local_70 = (void *)puVar5[2];
  *puVar5 = 0;
  puVar5[1] = 0;
  puVar5[2] = 0;
  _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_b0,*(long *)(param_1 + 8) - *(long *)(param_1 + 0x10));
  uVar6 = (ulong)(local_b0[0] >> 1);
  pvVar4 = (void *)((ulong)local_b0 | 1);
  if ((local_b0[0] & 1) != 0) {
    uVar6 = local_a8;
    pvVar4 = local_a0;
  }
  puVar5 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (&local_80,pvVar4,uVar6);
  uStack_58 = puVar5[1];
  local_60 = *puVar5;
  local_50 = (void *)puVar5[2];
  puVar5[1] = 0;
  puVar5[2] = 0;
  *puVar5 = 0;
  uVar6 = local_60 >> 1 & 0x7f;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((local_60 & 1) != 0) {
    uVar6 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar6)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_b0[0] & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    _ZdlPv(local_88);
  }
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_60,&DAT_002bd7f8,param_2);
  uVar6 = local_60 >> 1 & 0x7f;
  pvVar4 = (void *)((ulong)&local_60 | 1);
  if ((local_60 & 1) != 0) {
    uVar6 = uStack_58;
    pvVar4 = local_50;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm(lVar1,pvVar4,uVar6)
  ;
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if (*(long *)(lVar3 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
